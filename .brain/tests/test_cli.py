import contextlib
import io
import json
import os
import subprocess
import sys
import unittest
from unittest import mock

from _brainenv import BrainEnv, BRAIN_TOOLS

import brain as cli
from brainlib import handoff


def run_cli(*argv):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = cli.main(list(argv))
    return code, out.getvalue(), err.getvalue()


class CliTests(unittest.TestCase):
    def test_help_lists_every_command(self):
        proc = subprocess.run([sys.executable, str(BRAIN_TOOLS / 'brain.py'), '--help'], capture_output=True, text=True, timeout=30)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        for name in ('sync', 'pull', 'push', 'status', 'doctor', 'login', 'packet', 'checkpoint', 'search', 'index', 'embed-pending',
                     'mirror-memory', 'claims'):
            self.assertIn(name, proc.stdout)

    def test_bad_input_exits_two(self):
        with self.assertRaises(SystemExit) as caught:
            with contextlib.redirect_stderr(io.StringIO()):
                cli.main(['checkpoint', '--project', 'mockmob'])
        self.assertEqual(caught.exception.code, 2)

    def test_sync_quiet_mirrors_memory_then_syncs_with_reason(self):
        with BrainEnv(memory=True, sync={'status': 'ok'}) as env:
            (env.mem / 'a.md').write_text('---\ntype: project\n---\nhello\n', encoding='utf-8')
            code, out, _ = run_cli('sync', '--quiet', '--reason', 'prompt')
            self.assertEqual((code, out), (0, ''))
            self.assertTrue((env.brain / 'playbook' / 'memory' / 'atishay' / 'a.md').exists())
            call = [c for c in env.fake.calls if c[0] == 'sync'][0]
            self.assertEqual(call[2]['reason'], 'prompt')

    def test_sync_prints_summary_and_exit_code_follows_ok(self):
        with BrainEnv(sync={'ok': False, 'status': 'offline', 'message': 'could not resolve host', 'unpushed': 2,
                            'blocked': [{'path': 'docs/x.md', 'reason': 'possible secret', 'line': 4}]}):
            code, out, _ = run_cli('sync')
            self.assertEqual(code, 1)
            self.assertIn('status=offline', out)
            self.assertIn('could not resolve host', out)
            self.assertIn('blocked: docs/x.md: possible secret (line 4)', out)
        with BrainEnv(sync={'status': 'ok', 'committed': True}):
            code, out, _ = run_cli('sync')
            self.assertEqual(code, 0)
            self.assertIn('status=ok', out)

    def test_pull_and_push(self):
        with BrainEnv() as env:
            self.assertEqual(run_cli('pull')[0], 0)
            self.assertEqual(run_cli('push')[0], 0)
            pull = [c for c in env.fake.calls if c[0] == 'pull'][0]
            self.assertTrue(pull[2]['force'])
            self.assertIn('push', env.fake.names())

    def test_checkpoint_writes_handover_and_shares_it(self):
        with BrainEnv(person='cto', display='CTO', role='member') as env:
            code, out, _ = run_cli('checkpoint', '--project', 'mockmob', '--agent', 'claude', '--task', 'CLI task', '--next', 'CLI next',
                                   '--done', 'did it', '--status', 'paused', '--evidence', 'e1', '--evidence', 'e2', '--touched', 'a.ts',
                                   '--blocker', 'b1', '--verification', 'ran tests', '--cost', 'free')
            self.assertEqual(code, 0)
            self.assertIn('saved and shared with the team', out)
            data = handoff.scan('mockmob')[0]
            self.assertEqual((data['task'], data['next'], data['status'], data['evidence'], data['touched_files'], data['blockers'],
                              data['verification'], data['cost_and_pending_requests'], data['person']),
                             ('CLI task', 'CLI next', 'paused', ['e1', 'e2'], ['a.ts'], ['b1'], 'ran tests', 'free', 'cto'))
            self.assertIn('push', env.fake.names())

    def test_checkpoint_refuses_other_project(self):
        with BrainEnv() as env:
            code, out, _ = run_cli('checkpoint', '--project', 'continuum', '--agent', 'a', '--task', 't', '--next', 'n')
            self.assertEqual(code, 2)
            self.assertEqual(handoff.scan('mockmob'), [])

    def test_packet_command_with_and_without_task(self):
        with BrainEnv() as env:
            env.handover('cto', task='Visible in CLI packet', minutes_ago=3)
            code, out, _ = run_cli('packet')
            self.assertEqual(code, 0)
            self.assertIn('MOCKMOB TEAM BRAIN', out)
            self.assertIn('Visible in CLI packet', out)
            fake = mock.Mock()
            fake.search.return_value = [{'file': 'docs/NOW.md', 'line': 1, 'title': 'Now'}]
            with mock.patch.dict(sys.modules, {'brainlib.search.rag': fake}), mock.patch('brainlib.search.rag', fake, create=True):
                _, out, _ = run_cli('packet', '--task', 'the nav')
            self.assertIn('docs/NOW.md:1', out)

    def test_claims_command(self):
        with BrainEnv() as env:
            self.assertIn('No active claims', run_cli('claims')[1])
            env.claim('cto', session='aaaaaaaa', task='Rewrite nav', touched=['src/Nav.tsx'], branch='nav')
            code, out, _ = run_cli('claims')
            self.assertEqual(code, 0)
            self.assertIn('cto | mockmob@nav', out)
            self.assertIn('Rewrite nav', out)
            self.assertIn('src/Nav.tsx', out)

    def test_mirror_memory_command(self):
        with BrainEnv(memory=True) as env:
            (env.mem / 'm.md').write_text('---\ntype: reference\n---\nx\n', encoding='utf-8')
            code, out, _ = run_cli('mirror-memory')
            self.assertEqual(code, 0)
            self.assertEqual(json.loads(out)['changed'], ['m.md'])

    def test_search_index_and_embed_pending_call_the_rag_module(self):
        with BrainEnv():
            fake = mock.Mock()
            fake.keyword_search.return_value = [{'score': 2.0, 'file': 'docs/NOW.md', 'line': 1, 'title': 'Now', 'excerpt': 'e'}]
            fake.build_index.return_value = {'complete': True, 'docs': 3}
            fake.embed_in_background.return_value = {'embedded': 0}
            with mock.patch.dict(sys.modules, {'brainlib.search.rag': fake}), mock.patch('brainlib.search.rag', fake, create=True):
                code, out, _ = run_cli('search', 'nav bar', '--limit', '3')
                self.assertEqual(code, 0)
                self.assertEqual(json.loads(out)[0]['file'], 'docs/NOW.md')
                self.assertEqual(fake.keyword_search.call_args.kwargs['limit'], 3)
                self.assertEqual(json.loads(run_cli('index', '--vectors')[1])['docs'], 3)
                self.assertEqual(fake.build_index.call_args.kwargs['vectors'], True)
                self.assertEqual(json.loads(run_cli('embed-pending')[1]), {'embedded': 0})

    def test_status_command(self):
        with BrainEnv(status={'status': 'ok', 'unpushed': 1}) as env:
            fake = mock.Mock()
            fake.freshness.return_value = {'docs': 5}
            fake.vectors_status.return_value = 'keyword only'
            with mock.patch.dict(sys.modules, {'brainlib.search.rag': fake}), mock.patch('brainlib.search.rag', fake, create=True):
                code, out, _ = run_cli('status')
            info = json.loads(out)
            self.assertEqual((code, info['person'], info['sync']['unpushed'], info['index']['docs']), (0, 'atishay', 1, 5))

    def test_failures_are_reported_not_traceback_dumped(self):
        with BrainEnv() as env:
            env.fake.results['pull'] = mock.Mock(side_effect=RuntimeError('kaput'))
            code, out, err = run_cli('pull')
            self.assertEqual(code, 1)
            self.assertIn('kaput', err)
            self.assertNotIn('Traceback', err)

    def test_login_runs_an_interactive_fetch_without_prompt_blockers(self):
        with BrainEnv() as env:
            with mock.patch.dict(os.environ, {'GIT_TERMINAL_PROMPT': '0', 'GCM_INTERACTIVE': 'Never', 'GIT_ASKPASS': 'x'}), \
                    mock.patch.object(cli.subprocess, 'call', return_value=0) as call:
                code, out, _ = run_cli('login')
            self.assertEqual(code, 0)
            args, kwargs = call.call_args
            self.assertEqual(args[0][1:3], ['-C', str(env.brain)])
            self.assertEqual(args[0][3:], ['fetch', 'origin', 'main'])
            for key in ('GIT_TERMINAL_PROMPT', 'GCM_INTERACTIVE', 'GIT_ASKPASS'):
                self.assertNotIn(key, kwargs['env'])
            with mock.patch.object(cli.subprocess, 'call', return_value=128):
                self.assertEqual(run_cli('login')[0], 1)

    def test_doctor_reports_checks(self):
        with BrainEnv(status={'status': 'ok'}) as env:
            fake = mock.Mock()
            fake.freshness.return_value = {'docs': 4, 'index_age_minutes': 1.0}
            fake.vectors_status.return_value = 'keyword only'
            with mock.patch.dict(sys.modules, {'brainlib.search.rag': fake}), mock.patch('brainlib.search.rag', fake, create=True), \
                    mock.patch('brainlib.gitops.run', return_value=mock.Mock(code=0, kind=lambda *a: 'ok')):
                code, out, _ = run_cli('doctor')
            self.assertIn('[ok] python 3.10+', out)
            self.assertIn('[ok] remote reachable', out)
            self.assertIn('[ok] search index', out)
            self.assertIn('[ok] code repo configured', out)
            with mock.patch.dict(sys.modules, {'brainlib.search.rag': fake}), mock.patch('brainlib.search.rag', fake, create=True), \
                    mock.patch('brainlib.gitops.run', return_value=mock.Mock(code=128, kind=lambda *a: 'auth')):
                code, out, _ = run_cli('doctor')
            self.assertEqual(code, 1)
            self.assertIn('[FAIL] remote reachable: auth', out)
            self.assertIn('login', out)


if __name__ == '__main__':
    unittest.main()
