import io
import json
import os
import subprocess
import sys
import unittest
from pathlib import Path
from unittest import mock

from _brainenv import BrainEnv, BRAIN_TOOLS

import mcp_continuum as mcp
from brainlib import handoff

NEW_SESSION = {'jsonrpc': '2.0', 'id': 1, 'method': 'initialize', 'params': {'protocolVersion': '2025-06-18', 'capabilities': {}, 'clientInfo': {'name': 't', 'version': '1'}}}


def rpc(method, params=None, id=2):
    msg = {'jsonrpc': '2.0', 'id': id, 'method': method}
    if params is not None:
        msg['params'] = params
    return mcp.handle(msg)


def call(name, arguments=None, id=3):
    return rpc('tools/call', {'name': name, 'arguments': arguments or {}}, id)


def text_of(response):
    return response['result']['content'][0]['text']


def is_error(response):
    return bool(response['result'].get('isError'))


class ProtocolTests(unittest.TestCase):
    def test_initialize_echoes_supported_version_and_has_instructions(self):
        for version in ('2025-06-18', '2025-03-26', '2024-11-05'):
            res = mcp.handle(dict(NEW_SESSION, params={'protocolVersion': version}))
            self.assertEqual(res['result']['protocolVersion'], version)
        res = mcp.handle(dict(NEW_SESSION, params={'protocolVersion': '1999-01-01'}))
        self.assertIn(res['result']['protocolVersion'], mcp.SUPPORTED_PROTOCOLS)
        self.assertEqual(res['result']['serverInfo']['name'], 'continuum')
        self.assertTrue(res['result']['instructions'].startswith('Start with continuum_start.'))
        self.assertIn('tools', res['result']['capabilities'])

    def test_notifications_get_no_reply_and_ping_works(self):
        self.assertIsNone(mcp.handle({'jsonrpc': '2.0', 'method': 'notifications/initialized'}))
        self.assertEqual(rpc('ping')['result'], {})

    def test_tools_list_matches_continuum_schemas(self):
        tools = {t['name']: t for t in rpc('tools/list')['result']['tools']}
        self.assertEqual(set(tools), {'continuum_start', 'continuum_search', 'continuum_read', 'continuum_checkpoint', 'continuum_sync', 'continuum_status'})
        cp = tools['continuum_checkpoint']['inputSchema']
        self.assertEqual(cp['required'], ['project', 'agent', 'task', 'next'])
        self.assertEqual(cp['properties']['status']['enum'], ['active', 'paused', 'blocked', 'complete'])
        self.assertEqual(cp['properties']['evidence'], {'type': 'array', 'items': {'type': 'string'}})
        self.assertFalse(cp['additionalProperties'])
        self.assertEqual(tools['continuum_start']['inputSchema']['required'], ['project'])
        self.assertEqual(tools['continuum_read']['inputSchema']['properties']['lines']['maximum'], 200)
        self.assertEqual(tools['continuum_search']['inputSchema']['properties']['limit']['maximum'], 20)
        self.assertTrue(tools['continuum_search']['annotations']['readOnlyHint'])
        self.assertFalse(tools['continuum_checkpoint']['annotations']['readOnlyHint'])

    def test_unknown_method_and_bad_requests_are_json_rpc_errors(self):
        self.assertEqual(rpc('resources/list')['error']['code'], -32601)
        self.assertEqual(mcp.handle({'jsonrpc': '1.0', 'id': 5, 'method': 'ping'})['error']['code'], -32600)
        self.assertEqual(mcp.handle([1])['error']['code'], -32600)
        self.assertEqual(mcp.handle({'jsonrpc': '2.0', 'id': 6, 'method': 'ping', 'params': 'x'})['error']['code'], -32602)

    def test_unknown_tool_and_bad_arguments_are_tool_errors_not_crashes(self):
        with BrainEnv():
            self.assertTrue(is_error(call('nope')))
            self.assertIn('Unknown tool', text_of(call('nope')))
            self.assertIn('Missing argument: query', text_of(call('continuum_search', {})))
            self.assertIn('Unknown argument: x', text_of(call('continuum_search', {'query': 'a', 'x': 1})))
            self.assertIn('Invalid limit', text_of(call('continuum_search', {'query': 'a', 'limit': 99})))
            self.assertIn('Invalid status', text_of(call('continuum_checkpoint', {'project': 'mockmob', 'agent': 'a', 'task': 't', 'next': 'n', 'status': 'weird'})))
            self.assertIn('Arguments must be an object', text_of(mcp.handle({'jsonrpc': '2.0', 'id': 1, 'method': 'tools/call', 'params': {'name': 'continuum_sync', 'arguments': [1]}})))

    def test_tool_exception_returns_is_error(self):
        with BrainEnv() as env:
            env.fake.results['sync'] = mock.Mock(side_effect=RuntimeError('git exploded'))
            res = call('continuum_sync')
            self.assertTrue(is_error(res))
            self.assertIn('git exploded', text_of(res))


class ReadTests(unittest.TestCase):
    def read(self, path, **kw):
        return call('continuum_read', dict(path=path, **kw))

    def test_reads_a_brain_file_with_paging(self):
        with BrainEnv() as env:
            env.write('docs/NOW.md', '\n'.join(f'line {i}' for i in range(1, 251)))
            res = self.read('docs/NOW.md', lines=100)
            data = json.loads(text_of(res))
            self.assertEqual((data['path'], data['startLine'], data['totalLines'], data['nextLine']), ('docs/NOW.md', 1, 250, 101))
            self.assertTrue(data['text'].startswith('line 1\n'))
            data = json.loads(text_of(self.read('docs/NOW.md', startLine=201, lines=200)))
            self.assertIsNone(data['nextLine'])
            self.assertTrue(data['text'].endswith('line 250'))

    def test_search_result_prefixes_resolve(self):
        with BrainEnv() as env:
            env.write('docs/A.md', 'brain doc')
            (env.code / 'AGENTS.md').write_text('code repo agents', encoding='utf-8')
            self.assertEqual(json.loads(text_of(self.read('brain/docs/A.md')))['text'], 'brain doc')
            self.assertEqual(json.loads(text_of(self.read('mockmob/AGENTS.md')))['text'], 'code repo agents')
            self.assertEqual(json.loads(text_of(self.read('docs\\A.md')))['text'], 'brain doc')

    def test_refuses_absolute_paths_dotdot_and_escapes(self):
        with BrainEnv() as env:
            secret = env.tmp / 'secret.md'
            secret.write_text('TOP SECRET', encoding='utf-8')
            env.write('docs/ok.md', 'fine')
            bad = [str(secret), '/etc/passwd', 'C:\\Windows\\win.ini', 'C:/Windows/win.ini', '\\\\server\\share\\x.md', '~/x.md',
                   '../secret.md', 'docs/../../secret.md', 'docs\\..\\..\\secret.md', 'mockmob/../../secret.md', '..', 'docs/..', '',
                   'docs/ok.md\x00.png']
            for path in bad:
                res = self.read(path) if path else call('continuum_read', {'path': ''})
                self.assertTrue(is_error(res), f'{path!r} should be refused')
                self.assertNotIn('TOP SECRET', text_of(res))

    def test_refuses_symlink_escape_git_dir_binary_and_missing(self):
        with BrainEnv() as env:
            outside = env.tmp / 'outside'
            outside.mkdir()
            (outside / 'x.md').write_text('OUTSIDE', encoding='utf-8')
            link = env.brain / 'docs' / 'link'
            (env.brain / 'docs').mkdir()
            try:
                os.symlink(outside, link, target_is_directory=True)
            except (OSError, NotImplementedError):
                link = None
            if link is not None:
                res = self.read('docs/link/x.md')
                self.assertTrue(is_error(res))
                self.assertNotIn('OUTSIDE', text_of(res))
            (env.brain / '.git' / 'config').write_text('[core]', encoding='utf-8')
            self.assertTrue(is_error(self.read('.git/config')))
            env.write('docs/pic.png', 'not really')
            self.assertTrue(is_error(self.read('docs/pic.png')))
            self.assertIn('No such file', text_of(self.read('docs/missing.md')))

    def test_sibling_directory_with_shared_prefix_is_not_inside(self):
        with BrainEnv() as env:
            sibling = env.tmp / 'brain-evil'
            sibling.mkdir()
            (sibling / 'x.md').write_text('EVIL', encoding='utf-8')
            self.assertTrue(is_error(self.read('../brain-evil/x.md')))


class StartAndCheckpointTests(unittest.TestCase):
    def test_start_requires_mockmob_and_returns_packet_after_pull(self):
        with BrainEnv() as env:
            res = call('continuum_start', {'project': 'campusos'})
            self.assertTrue(is_error(res))
            self.assertIn('only the MockMob team brain', text_of(res))
            env.handover('cto', task='CTO handover for start', minutes_ago=5)
            res = call('continuum_start', {'project': 'mockmob', 'task': ''})
            self.assertFalse(is_error(res))
            self.assertIn('MOCKMOB TEAM BRAIN', text_of(res))
            self.assertIn('CTO handover for start', text_of(res))
            pull = [c for c in env.fake.calls if c[0] == 'pull'][0]
            self.assertEqual((pull[2]['lock_timeout'], pull[2]['min_interval']), (5, 30))

    def test_start_with_task_includes_hits(self):
        with BrainEnv():
            fake = mock.Mock()
            fake.search.return_value = [{'file': 'docs/NOW.md', 'line': 4, 'title': 'Now'}]
            with mock.patch.dict(sys.modules, {'brainlib.search.rag': fake}), mock.patch('brainlib.search.rag', fake, create=True):
                text = text_of(call('continuum_start', {'project': 'mockmob', 'task': 'nav bar'}))
            self.assertIn('docs/NOW.md:4', text)

    def test_checkpoint_writes_pushes_and_says_shared(self):
        with BrainEnv(push={'ok': True, 'status': 'ok', 'pushed': True, 'unpushed': 0}) as env:
            res = call('continuum_checkpoint', {'project': 'mockmob', 'agent': 'claude', 'task': 'Did a thing', 'next': 'Do more',
                                                 'done': 'stuff', 'status': 'paused', 'evidence': ['e'], 'touched': ['f'], 'blockers': ['b'],
                                                 'verification': 'v', 'cost': 'c'})
            self.assertFalse(is_error(res))
            text = text_of(res)
            self.assertRegex(text, r'^handoffs/mockmob/\d{8}T\d{6}\.\d{6}Z-[0-9a-f]{8}\.md: saved and shared with the team$')
            rel = text.split(':')[0]
            data = json.loads((env.brain / rel).with_suffix('.json').read_text(encoding='utf-8'))
            self.assertEqual((data['task'], data['status'], data['person'], data['blockers'], data['touched_files']),
                             ('Did a thing', 'paused', 'atishay', ['b'], ['f']))
            push = [c for c in env.fake.calls if c[0] == 'push']
            self.assertEqual(len(push), 1)
            self.assertEqual(push[0][2]['timeout'], 15)

    def test_checkpoint_offline_is_saved_locally_with_reason(self):
        with BrainEnv(push={'ok': False, 'status': 'offline', 'message': 'could not resolve host', 'unpushed': 1}) as env:
            res = call('continuum_checkpoint', {'project': 'mockmob', 'agent': 'codex', 'task': 'T', 'next': 'N'})
            self.assertFalse(is_error(res))
            self.assertIn('saved locally; it will be shared at the next sync (offline', text_of(res))
            self.assertEqual(len(handoff.scan('mockmob')), 1)

    def test_checkpoint_push_exception_still_saves(self):
        with BrainEnv() as env:
            env.fake.results['push'] = mock.Mock(side_effect=RuntimeError('boom'))
            res = call('continuum_checkpoint', {'project': 'mockmob', 'agent': 'codex', 'task': 'T', 'next': 'N'})
            self.assertIn('saved locally', text_of(res))
            self.assertEqual(len(handoff.scan('mockmob')), 1)

    def test_checkpoint_rejects_other_projects_and_redacts(self):
        with BrainEnv() as env:
            self.assertTrue(is_error(call('continuum_checkpoint', {'project': 'continuum', 'agent': 'a', 'task': 't', 'next': 'n'})))
            self.assertTrue(is_error(call('continuum_checkpoint', {'project': '../x', 'agent': 'a', 'task': 't', 'next': 'n'})))
            self.assertFalse((env.brain / 'handoffs' / 'continuum').exists())
            call('continuum_checkpoint', {'project': 'mockmob', 'agent': 'a', 'task': 't', 'next': 'use sk-ant-api03-' + 'm' * 40})
            self.assertNotIn('m' * 40, json.dumps(handoff.scan('mockmob'), default=str))


class SearchSyncStatusTests(unittest.TestCase):
    def test_search_returns_json_list_via_keyword_search(self):
        with BrainEnv():
            fake = mock.Mock()
            fake.keyword_search.return_value = [{'score': 1.5, 'file': 'docs/NOW.md', 'line': 3, 'title': 'Now', 'excerpt': 'x'}]
            with mock.patch.dict(sys.modules, {'brainlib.search.rag': fake}), mock.patch('brainlib.search.rag', fake, create=True):
                res = call('continuum_search', {'query': 'status', 'limit': 4})
            self.assertEqual(json.loads(text_of(res))[0]['file'], 'docs/NOW.md')
            self.assertEqual(fake.keyword_search.call_args.kwargs['limit'], 4)

    def test_sync_and_status(self):
        with BrainEnv(sync={'status': 'ok', 'committed': True, 'pushed': True}, status={'status': 'ok', 'unpushed': 0, 'blocked': []}) as env:
            res = json.loads(text_of(call('continuum_sync')))
            self.assertEqual((res['status'], res['committed']), ('ok', True))
            sync_call = [c for c in env.fake.calls if c[0] == 'sync'][0]
            self.assertTrue(sync_call[2]['force'])
            fake = mock.Mock()
            fake.freshness.return_value = {'docs': 12, 'index_age_minutes': 1.0}
            fake.vectors_status.return_value = 'keyword only'
            with mock.patch.dict(sys.modules, {'brainlib.search.rag': fake}), mock.patch('brainlib.search.rag', fake, create=True):
                info = json.loads(text_of(call('continuum_status')))
            self.assertEqual(info['index']['docs'], 12)
            self.assertEqual(info['sync']['status'], 'ok')
            self.assertEqual(info['person'], 'atishay')


class StdioTests(unittest.TestCase):
    def test_serve_handles_lines_blank_lines_garbage_and_bom(self):
        with BrainEnv():
            lines = ['\ufeff' + json.dumps(NEW_SESSION), '', 'this is not json', json.dumps({'jsonrpc': '2.0', 'method': 'notifications/initialized'}),
                     json.dumps({'jsonrpc': '2.0', 'id': 2, 'method': 'tools/list'})]
            out = io.StringIO()
            mcp.serve(iter(l + '\n' for l in lines), out)
            replies = [json.loads(l) for l in out.getvalue().splitlines()]
            self.assertEqual([r.get('id') for r in replies], [1, None, 2])
            self.assertEqual(replies[1]['error']['code'], -32700)
            self.assertEqual(len(replies[2]['result']['tools']), 6)

    def test_real_process_round_trip_utf8_and_clean_exit(self):
        with BrainEnv(fake_sync=False) as env:
            env.write('docs/NOW.md', 'Rupee ₹ ready\nसब ठीक है\n')
            requests = [NEW_SESSION, {'jsonrpc': '2.0', 'method': 'notifications/initialized'},
                        {'jsonrpc': '2.0', 'id': 2, 'method': 'tools/list'},
                        {'jsonrpc': '2.0', 'id': 3, 'method': 'tools/call', 'params': {'name': 'continuum_read', 'arguments': {'path': 'docs/NOW.md'}}},
                        {'jsonrpc': '2.0', 'id': 4, 'method': 'tools/call', 'params': {'name': 'continuum_read', 'arguments': {'path': '../x.md'}}},
                        {'jsonrpc': '2.0', 'id': 5, 'method': 'bogus/method'}]
            data = ''.join(json.dumps(r) + '\n' for r in requests).encode('utf-8')
            proc = subprocess.run([sys.executable, str(BRAIN_TOOLS / 'mcp_continuum.py')], input=data, capture_output=True, timeout=60,
                                  env=dict(os.environ, PYTHONIOENCODING='ascii'))
            self.assertEqual(proc.returncode, 0, proc.stderr)
            self.assertFalse(proc.stdout.startswith(b'\xef\xbb\xbf'))
            self.assertNotIn(b'\r\n', proc.stdout)
            replies = {r['id']: r for r in (json.loads(l) for l in proc.stdout.decode('utf-8').splitlines())}
            self.assertEqual(set(replies), {1, 2, 3, 4, 5})
            self.assertIn('₹', json.loads(text_of(replies[3]))['text'])
            self.assertTrue(replies[4]['result']['isError'])
            self.assertEqual(replies[5]['error']['code'], -32601)
            self.assertEqual(len(replies[2]['result']['tools']), 6)


if __name__ == '__main__':
    unittest.main()
