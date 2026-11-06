import json
import os
import subprocess
import sys
import time
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest import mock

from _brainenv import BrainEnv, BRAIN_TOOLS, iso

import hook
from brainlib import handoff, sessions

SID = 'sess-0001-abcdef'
SHORT = 'sess-000'


def run(env, event, harness='claude', sid=SID, **extra):
    payload = env.hook_payload(sid, **extra)
    return hook.main([harness, event], json.dumps(payload))


def record(env, harness='claude', sid=SID):
    return sessions.load(harness, sid)


def seed_session(env, sid=SID, harness='claude', **fields):
    rec = sessions.new_record(harness, sid, str(env.code), str(env.tmp / 't.jsonl'))
    rec.update(fields)
    sessions.save(rec)
    return rec


def autos(env):
    return [d for d in handoff.scan('mockmob') if handoff.is_auto(d)]


def error_log(env):
    path = env.state / 'logs' / 'hook-errors.log'
    return path.read_text(encoding='utf-8') if path.exists() else ''


class NotMockMobTests(unittest.TestCase):
    def test_other_cwd_prints_nothing_does_nothing_and_is_fast(self):
        with BrainEnv() as env:
            first = env.tmp / 'elsewhere-1'
            second = env.tmp / 'elsewhere-2'
            first.mkdir()
            second.mkdir()
            hook.main(['claude', 'SessionStart'], json.dumps({'session_id': 'x', 'cwd': str(first)}))  # warm the imports
            started = time.perf_counter()
            out = hook.main(['claude', 'SessionStart'], json.dumps({'session_id': 'y', 'cwd': str(second)}))
            elapsed_ms = (time.perf_counter() - started) * 1000
            self.assertEqual(out, '')
            self.assertLess(elapsed_ms, 100, f'non-MockMob hook took {elapsed_ms:.0f} ms')
            self.assertEqual(env.fake.calls, [])
            self.assertFalse((env.state / 'sessions').exists() and list((env.state / 'sessions').iterdir()))
            for event in ('UserPromptSubmit', 'PostToolUse', 'Stop', 'PreCompact', 'SessionEnd'):
                self.assertEqual(hook.main(['codex', event], json.dumps({'session_id': 'z', 'cwd': str(second), 'prompt': 'hi'})), '')
            self.assertEqual(env.fake.calls, [])

    def test_subprocess_other_cwd_exits_zero_silently(self):
        with BrainEnv(fake_sync=False) as env:
            other = env.tmp / 'elsewhere'
            other.mkdir()
            started = time.perf_counter()
            proc = subprocess.run([sys.executable, str(BRAIN_TOOLS / 'hook.py'), 'claude', 'SessionStart'],
                                  input=json.dumps({'session_id': 'x', 'cwd': str(other)}).encode(), capture_output=True, timeout=30)
            elapsed = time.perf_counter() - started
            self.assertEqual(proc.returncode, 0, proc.stderr)
            self.assertEqual(proc.stdout, b'')
            print(f'\n[info] non-MockMob hook process wall time {elapsed * 1000:.0f} ms (interpreter start included)', file=sys.stderr)

    def test_bridge_mode_and_internal_runs_are_silent(self):
        with BrainEnv(mode='bridge') as env:
            self.assertEqual(run(env, 'SessionStart'), '')
            self.assertEqual(env.fake.calls, [])
        with BrainEnv() as env:
            with mock.patch.dict(os.environ, {'CONTINUUM_INTERNAL': '1'}):
                self.assertEqual(run(env, 'SessionStart'), '')
            self.assertEqual(env.fake.calls, [])


class SessionStartTests(unittest.TestCase):
    def test_start_pulls_mirrors_claims_commits_spawns_and_prints_packet(self):
        with BrainEnv(memory=True) as env:
            (env.mem / 'a.md').write_text('---\ntype: feedback\n---\nx\n', encoding='utf-8')
            env.handover('cto', task='CTO did X', next='Review it', minutes_ago=30)
            out = run(env, 'SessionStart')
            self.assertIn('MOCKMOB TEAM BRAIN | Atishay (owner)', out)
            self.assertIn('CTO did X', out)
            self.assertFalse(out.lstrip().startswith('{'))  # plain text, like AI OS hook.py for SessionStart
            pull = [c for c in env.fake.calls if c[0] == 'pull'][0]
            self.assertEqual((pull[2]['lock_timeout'], pull[2]['min_interval'], pull[2]['timeout']), (3, 30, 6))
            names = env.fake.names()
            self.assertLess(names.index('pull'), names.index('commit_pending'))
            self.assertLess(names.index('commit_pending'), names.index('spawn_background'))
            self.assertEqual(env.fake.spawn_reasons(), ['start'])
            self.assertTrue((env.brain / 'playbook' / 'memory' / 'atishay' / 'a.md').exists())
            rec = record(env)
            self.assertEqual((rec['status'], rec['repo'], rec['branch'], rec['task']), ('running', 'mockmob', 'feature-x', ''))
            claim = json.loads((env.brain / 'claims' / 'atishay' / (SHORT + '.json')).read_text(encoding='utf-8'))
            self.assertEqual((claim['repo'], claim['branch'], claim['task'], claim['harness']), ('mockmob', 'feature-x', '', 'claude'))
            self.assertIn('last_seen_at', env.state_json('seen'))

    def test_pull_failure_still_gives_a_packet_and_logs(self):
        with BrainEnv() as env:
            env.fake.results['pull'] = mock.Mock(side_effect=RuntimeError('network exploded'))
            out = run(env, 'SessionStart')
            self.assertIn('MOCKMOB TEAM BRAIN', out)
            self.assertIn('network exploded', error_log(env))

    def test_offline_packet_says_so(self):
        with BrainEnv(pull={'ok': True, 'status': 'offline', 'message': 'could not resolve host'}) as env:
            env.state_json('sync', {'last_pull_ok_at': iso(-120)})
            self.assertIn('OFFLINE: using the local copy', run(env, 'SessionStart'))

    def test_dead_session_becomes_auto_capture_at_next_start(self):
        """Edge case 7: a session that died without SessionEnd is captured by the next SessionStart."""
        with BrainEnv() as env:
            old = seed_session(env, sid='dead-session-0001', last_active=iso(-200), turns=4, last_message='Was fixing nav',
                               last_edit_at=iso(-210), touched=[{'path': 'src/Nav.tsx', 'repo': 'mockmob', 'at': iso(-210)}])
            env.claim('atishay', session='dead-session-0001', task='Nav work')
            quiet = seed_session(env, sid='quiet-session-002', last_active=iso(-200), turns=1)  # stale but never edited
            live = seed_session(env, sid='live-session-0003', last_active=iso(-30), last_edit_at=iso(-35))
            run(env, 'SessionStart')
            captured = autos(env)
            self.assertEqual(len(captured), 1)
            self.assertEqual(captured[0]['agent'], 'claude-auto')
            self.assertEqual(captured[0]['person'], 'atishay')
            self.assertIn('dead-ses', captured[0]['task'])
            self.assertIn('Was fixing nav', captured[0]['done'])
            self.assertEqual(captured[0]['touched_files'], ['src/Nav.tsx'])
            self.assertEqual(captured[0]['status'], 'paused')
            self.assertEqual(sessions.load('claude', 'dead-session-0001')['status'], 'ended')
            self.assertEqual(sessions.load('claude', 'quiet-session-002')['status'], 'ended')
            self.assertEqual(sessions.load('claude', 'live-session-0003')['status'], 'running')
            self.assertFalse((env.brain / 'claims' / 'atishay' / 'dead-ses.json').exists())
            run(env, 'SessionStart', sid='another-session-004')
            self.assertEqual(len(autos(env)), 1)  # not captured twice

    def test_changed_files_shown_in_packet_are_not_repeated_by_the_first_prompt(self):
        with BrainEnv() as env:
            path = env.handover('cto', task='Skewed old handover', minutes_ago=900)
            rel = path.relative_to(env.brain).as_posix()
            env.fake.results['pull'] = {'changed_files': [rel]}
            env.state_json('seen', {'last_seen_at': iso(-5)})
            env.state_json('sync', {'changed_files': [rel], 'last_fetch_at': iso(0)})
            out = run(env, 'SessionStart')
            self.assertIn('Skewed old handover', out.split('New since your last session:')[1])
            self.assertNotIn('Skewed old handover', run(env, 'UserPromptSubmit', prompt='go'))


class PromptTests(unittest.TestCase):
    def prompt(self, env, text, **kw):
        return run(env, 'UserPromptSubmit', prompt=text, **kw)

    def test_no_network_inline(self):
        with BrainEnv() as env:
            seed_session(env, task='already set')
            env.state_json('sync', {'last_fetch_at': iso(-60)})
            self.prompt(env, 'hello')
            self.assertEqual([n for n in env.fake.names() if n not in ('spawn_background',)], [])

    def test_background_pull_when_last_fetch_is_older_than_five_minutes_and_throttled(self):
        with BrainEnv() as env:
            seed_session(env, task='already set')
            env.state_json('sync', {'last_fetch_at': iso(-10)})
            self.prompt(env, 'one')
            self.assertEqual(env.fake.spawn_reasons(), ['prompt'])
            self.prompt(env, 'two')
            self.assertEqual(env.fake.spawn_reasons(), ['prompt'])  # not again within 5 minutes
        with BrainEnv() as env:
            seed_session(env, task='already set')
            env.state_json('sync', {'last_fetch_at': iso(-1)})
            self.prompt(env, 'one')
            self.assertEqual(env.fake.spawn_reasons(), [])

    def test_feeds_other_peoples_new_handovers_once(self):
        with BrainEnv() as env:
            seed_session(env, task='t', fed_until=iso(-10))
            env.handover('cto', task='CTO shipped the menu', next='Test it on a phone', minutes_ago=2)
            env.handover('atishay', task='My own handover', minutes_ago=1)
            env.handover('cto', task='CTO auto thing', agent='claude-auto', minutes_ago=1)
            env.handover('cto', task='Older than the last prompt', minutes_ago=60)
            out = self.prompt(env, 'continue')
            self.assertIn('CTO shipped the menu', out)
            self.assertIn('Test it on a phone', out)
            self.assertNotIn('My own handover', out)
            self.assertNotIn('CTO auto thing', out)
            self.assertNotIn('Older than the last prompt', out)
            self.assertEqual(self.prompt(env, 'again'), '')
            env.handover('dev2', task='Dev2 landed a fix', minutes_ago=0)
            self.assertIn('Dev2 landed a fix', self.prompt(env, 'and again'))

    def test_file_arrived_by_pull_counts_even_with_old_timestamp(self):
        with BrainEnv() as env:
            seed_session(env, task='t', fed_until=iso(-1))
            path = env.handover('cto', task='Backdated by clock skew', minutes_ago=500)
            rel = path.relative_to(env.brain).as_posix()
            env.state_json('sync', {'last_fetch_at': iso(0), 'changed_files': [rel]})
            self.assertIn('Backdated by clock skew', self.prompt(env, 'go'))
            self.assertNotIn('Backdated by clock skew', self.prompt(env, 'go'))

    def test_new_blocked_file_warning_once(self):
        with BrainEnv() as env:
            seed_session(env, task='t')
            env.state_json('blocked', {'files': [{'path': 'docs/leak.md', 'reason': 'possible secret: github token', 'line': 3}]})
            out = self.prompt(env, 'go')
            self.assertIn('docs/leak.md', out)
            self.assertIn('line 3', out)
            self.assertEqual(self.prompt(env, 'go'), '')

    def test_owner_note_is_saved_shared_and_not_for_ordinary_prompts(self):
        with BrainEnv() as env:
            seed_session(env, task='t')
            out = self.prompt(env, "Remember for the next session: we always use pnpm, never npm")
            notes = [d for d in handoff.scan('mockmob') if handoff.is_owner_note(d)]
            self.assertEqual(len(notes), 1)
            self.assertEqual(notes[0]['agent'], 'claude-owner-note')
            self.assertEqual(notes[0]['person'], 'atishay')
            self.assertIn('we always use pnpm, never npm', notes[0]['next'])
            self.assertIn('saved', out)
            self.assertIn('note', env.fake.spawn_reasons())
            self.prompt(env, 'please fix the login page')
            self.prompt(env, 'remember this ' + 'x' * 700 + ' for later')
            self.assertEqual(len([d for d in handoff.scan('mockmob') if handoff.is_note(d)]), 1)

    def test_team_note_for_non_owner_and_codex_harness(self):
        with BrainEnv(person='cto', display='CTO', role='member') as env:
            seed_session(env, harness='codex', task='t')
            run(env, 'UserPromptSubmit', harness='codex', prompt="Don't forget to tell the team the API key rotates on Friday")
            notes = [d for d in handoff.scan('mockmob') if handoff.is_team_note(d)]
            self.assertEqual(len(notes), 1)
            self.assertEqual(notes[0]['agent'], 'codex-team-note')
            self.assertEqual(notes[0]['person'], 'cto')

    def test_first_prompt_sets_claim_task_redacted_and_cut(self):
        with BrainEnv() as env:
            run(env, 'SessionStart')
            env.fake.calls.clear()
            secret = 'sk-ant-api03-' + 'k' * 40
            self.prompt(env, 'Fix the nav bar ' + secret + ' ' + 'long ' * 60)
            rec = record(env)
            self.assertLessEqual(len(rec['task']), 120)
            self.assertTrue(rec['task'].startswith('Fix the nav bar'))
            self.assertNotIn('k' * 40, rec['task'])
            claim = json.loads((env.brain / 'claims' / 'atishay' / (SHORT + '.json')).read_text(encoding='utf-8'))
            self.assertEqual(claim['task'], rec['task'])
            self.assertEqual(env.fake.spawn_reasons(), ['claim'])
            self.prompt(env, 'second prompt must not replace the task')
            self.assertEqual(record(env)['task'], rec['task'])

    def test_prompt_without_session_record_does_not_crash(self):
        with BrainEnv() as env:
            self.assertEqual(self.prompt(env, 'hello'), '')
            self.assertEqual(error_log(env), '')


class PostToolUseTests(unittest.TestCase):
    def edit(self, env, rel='src/App.tsx', tool='Edit', **kw):
        path = env.code / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.touch()
        return run(env, 'PostToolUse', tool_name=tool, tool_input={'file_path': str(path)}, **kw)

    def test_records_touched_path_refreshes_claim_and_spawns(self):
        with BrainEnv() as env:
            run(env, 'SessionStart')
            env.fake.calls.clear()
            self.assertEqual(self.edit(env), '')
            rec = record(env)
            self.assertEqual([(t['path'], t['repo'], t['branch']) for t in rec['touched']], [('src/App.tsx', 'mockmob', 'feature-x')])
            self.assertIsNotNone(rec['last_edit_at'])
            claim = json.loads((env.brain / 'claims' / 'atishay' / (SHORT + '.json')).read_text(encoding='utf-8'))
            self.assertEqual(claim['touched'], ['src/App.tsx'])
            self.assertEqual(env.fake.spawn_reasons(), ['claim'])
            self.edit(env, 'src/Other.tsx')  # claim was pushed a moment ago: no new refresh
            self.assertEqual(env.fake.spawn_reasons(), ['claim'])
            self.assertEqual(record(env)['touched'][-1]['path'], 'src/Other.tsx')

    def test_claim_refreshes_again_after_ten_minutes(self):
        with BrainEnv() as env:
            run(env, 'SessionStart')
            self.edit(env)
            rec = record(env)
            rec['claim_pushed_at'] = iso(-11)
            sessions.save(rec)
            env.fake.calls.clear()
            self.edit(env, 'src/Third.tsx')
            self.assertEqual(env.fake.spawn_reasons(), ['claim'])

    def test_warns_when_another_person_is_editing_the_same_file_once(self):
        with BrainEnv() as env:
            env.claim('cto', session='aaaaaaaa', task='Rebuilding the app shell', touched=['src/App.tsx'], branch='cto-shell')
            out = self.edit(env)
            data = json.loads(out)
            self.assertEqual(data['hookSpecificOutput']['hookEventName'], 'PostToolUse')
            text = data['hookSpecificOutput']['additionalContext']
            self.assertIn('cto', text)
            self.assertIn('cto-shell', text)
            self.assertIn('src/App.tsx', text)
            self.assertEqual(self.edit(env), '')  # warned once per person and file
            self.assertEqual(self.edit(env, 'src/Unrelated.tsx'), '')

    def test_ignores_non_edit_tools_and_files_outside_mockmob(self):
        with BrainEnv() as env:
            self.assertEqual(run(env, 'PostToolUse', tool_name='Bash', tool_input={'command': 'ls'}), '')
            self.assertIsNone(record(env))
            outside = env.tmp / 'notes.txt'
            outside.write_text('x', encoding='utf-8')
            run(env, 'PostToolUse', tool_name='Write', tool_input={'file_path': str(outside)})
            rec = record(env)
            self.assertEqual(rec.get('touched', []), [] if rec else [])

    def test_codex_apply_patch_paths(self):
        with BrainEnv() as env:
            patch = '*** Begin Patch\n*** Update File: src/Patched.ts\n@@\n-a\n+b\n*** Add File: src/New.ts\n+x\n*** End Patch\n'
            run(env, 'PostToolUse', harness='codex', tool_name='apply_patch', tool_input={'input': patch})
            rec = record(env, 'codex')
            self.assertEqual(sorted(t['path'] for t in rec['touched']), ['src/New.ts', 'src/Patched.ts'])

    def test_edited_paths_helper(self):
        got = hook.edited_paths({'tool_name': 'Edit', 'cwd': str(Path.cwd()), 'tool_input': {'file_path': 'a/b.txt'}})
        self.assertEqual(got, [os.path.normpath(os.path.abspath(os.path.join(str(Path.cwd()), 'a/b.txt')))])
        self.assertEqual(hook.edited_paths({'tool_name': 'NotebookEdit', 'tool_input': {'notebook_path': str(Path.cwd() / 'n.ipynb')}}),
                         [str(Path.cwd() / 'n.ipynb')])


class StopTests(unittest.TestCase):
    def test_stop_bumps_turns_and_stores_redacted_message(self):
        with BrainEnv() as env:
            msg = 'Done. Key was sk-ant-api03-' + 'z' * 40 + ' ' + 'blah ' * 300
            run(env, 'Stop', last_assistant_message=msg)
            run(env, 'Stop', last_assistant_message='Second message')
            rec = record(env)
            self.assertEqual(rec['turns'], 2)
            self.assertEqual(rec['last_message'], 'Second message')
            run(env, 'Stop', last_assistant_message=msg)
            rec = record(env)
            self.assertLessEqual(len(rec['last_message']), 600)
            self.assertNotIn('z' * 40, rec['last_message'])
            self.assertEqual(env.fake.calls, [])  # no git


class AutoCaptureTests(unittest.TestCase):
    def test_precompact_captures_when_edits_have_no_handover_and_only_once(self):
        with BrainEnv() as env:
            seed_session(env, turns=5, last_message='Halfway', last_edit_at=iso(-30),
                         touched=[{'path': 'src/A.tsx', 'repo': 'mockmob', 'at': iso(-30)}])
            self.assertEqual(run(env, 'PreCompact'), '')
            self.assertEqual(len(autos(env)), 1)
            self.assertEqual(env.fake.spawn_reasons(), ['precompact'])
            self.assertIn('Turns: 5', autos(env)[0]['done'])
            self.assertEqual(autos(env)[0]['verification'], 'auto-captured by hook; not agent-verified')
            run(env, 'PreCompact')
            self.assertEqual(len(autos(env)), 1)

    def test_no_capture_when_a_real_handover_followed_the_last_edit(self):
        with BrainEnv() as env:
            seed_session(env, turns=5, last_edit_at=iso(-30))
            handoff.write('mockmob', 'claude', 'Real handover', 'next', person='atishay')
            run(env, 'PreCompact')
            self.assertEqual(autos(env), [])
            self.assertEqual(env.fake.spawn_reasons(), [])

    def test_capture_when_edit_is_newer_than_the_last_real_handover(self):
        with BrainEnv() as env:
            path = env.handover('atishay', task='Older real', minutes_ago=40)
            seed_session(env, turns=2, last_edit_at=iso(-5))
            run(env, 'PreCompact')
            self.assertEqual(len(autos(env)), 1)

    def test_other_peoples_handover_does_not_count_and_no_edits_means_no_capture(self):
        with BrainEnv() as env:
            env.handover('cto', task='CTO real', minutes_ago=1)
            seed_session(env, turns=2, last_edit_at=iso(-5))
            run(env, 'PreCompact')
            self.assertEqual(len(autos(env)), 1)
        with BrainEnv() as env:
            seed_session(env, turns=9)
            run(env, 'PreCompact')
            self.assertEqual(autos(env), [])

    def test_session_end_captures_removes_claim_spawns_and_is_quick(self):
        with BrainEnv() as env:
            run(env, 'SessionStart')
            path = env.code / 'src' / 'A.tsx'
            path.parent.mkdir(parents=True)
            path.touch()
            run(env, 'PostToolUse', tool_name='Write', tool_input={'file_path': str(path)})
            run(env, 'Stop', last_assistant_message='Almost there')
            env.fake.calls.clear()
            claim = env.brain / 'claims' / 'atishay' / (SHORT + '.json')
            self.assertTrue(claim.exists())
            started = time.perf_counter()
            self.assertEqual(run(env, 'SessionEnd'), '')
            self.assertLess(time.perf_counter() - started, 1.5)
            self.assertFalse(claim.exists())
            self.assertEqual(len(autos(env)), 1)
            self.assertIn('Almost there', autos(env)[0]['done'])
            self.assertEqual(autos(env)[0]['touched_files'], ['src/A.tsx'])
            rec = record(env)
            self.assertEqual(rec['status'], 'ended')
            self.assertEqual(env.fake.names(), ['spawn_background'])  # nothing slow inline: no pull, push or commit
            self.assertEqual(env.fake.spawn_reasons(), ['end'])


class ResilienceTests(unittest.TestCase):
    def test_garbage_stdin_unknown_event_and_config_failure_never_raise(self):
        with BrainEnv() as env:
            self.assertEqual(hook.main(['claude', 'SessionStart'], '{not json'), '')
            self.assertEqual(hook.main(['claude', 'SessionStart'], '[1, 2]'), '')
            self.assertEqual(hook.main(['claude', 'Bogus'], '{}'), '')
            self.assertEqual(hook.main([], ''), '')
            with mock.patch('brainlib.config.load', side_effect=RuntimeError('config blew up')):
                self.assertEqual(run(env, 'SessionStart'), '')
            log = error_log(env)
            self.assertIn('config blew up', log)
            self.assertIn('unknown harness or event', log)

    def test_windows_paths_with_single_backslashes_are_repaired(self):
        with BrainEnv() as env:
            raw = '{"session_id": "s1", "cwd": "%s", "prompt": "hi"}' % str(env.code)
            self.assertIsInstance(hook.parse_payload(raw), dict)
            self.assertEqual(hook.parse_payload(raw)['cwd'], str(env.code))

    def test_handler_exception_is_swallowed_and_logged(self):
        with BrainEnv() as env:
            with mock.patch.object(hook, 'on_prompt', side_effect=ValueError('handler broke')):
                with mock.patch.dict(hook.HANDLERS, {'UserPromptSubmit': hook.on_prompt}):
                    self.assertEqual(run(env, 'UserPromptSubmit', prompt='x'), '')
            self.assertIn('handler broke', error_log(env))

    def test_error_log_rotates_at_one_megabyte(self):
        with BrainEnv() as env:
            log = env.state / 'logs' / 'hook-errors.log'
            log.parent.mkdir(parents=True)
            log.write_text('x' * (1024 * 1024 + 10), encoding='utf-8')
            sessions.log_error('claude', 'Test', RuntimeError('after rotate'))
            self.assertIn('after rotate', log.read_text(encoding='utf-8'))
            self.assertTrue((env.state / 'logs' / 'hook-errors.log.1').exists())
            self.assertLess(log.stat().st_size, 2000)

    def test_subprocess_session_start_with_real_modules_exits_zero_with_packet(self):
        """The real sync engine on a brain that is not a git repo: no crash, no hang, a packet still prints."""
        with BrainEnv(fake_sync=False) as env:
            env.write('docs/NOW.md', 'Now: testing\n')
            payload = json.dumps(env.hook_payload()).encode()
            started = time.perf_counter()
            proc = subprocess.run([sys.executable, str(BRAIN_TOOLS / 'hook.py'), 'claude', 'SessionStart'], input=payload,
                                  capture_output=True, timeout=60, env=dict(os.environ, PYTHONIOENCODING='utf-8'))
            self.assertEqual(proc.returncode, 0, proc.stderr)
            self.assertLess(time.perf_counter() - started, 30)
            text = proc.stdout.decode('utf-8')
            self.assertIn('MOCKMOB TEAM BRAIN', text)
            self.assertIn('Now: testing', text)


if __name__ == '__main__':
    unittest.main()
