import json
import os
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from _brainenv import BrainEnv  # noqa: F401  (also puts .brain on sys.path)

from brainlib import handoff

AIOS_SCRIPTS = Path('C:/Users/atish/Desktop/AI OS/scripts')
KEYS = ['id', 'observed_at', 'agent', 'task', 'status', 'done', 'next', 'blockers', 'evidence', 'touched_files',
        'verification', 'cost_and_pending_requests', 'confidence']


class HandoffWriteTests(unittest.TestCase):
    def test_writes_json_and_md_with_continuum_layout(self):
        with BrainEnv() as env:
            md = handoff.write('mockmob', 'claude', 'Fix the login', 'Ship it', done='Did a thing', evidence=['a.log'],
                               touched=['src/a.ts'], blockers=['none'], verification='tests green', cost='0', person='atishay')
            self.assertEqual(md.suffix, '.md')
            self.assertEqual(md.parent, env.brain / 'handoffs' / 'mockmob')
            self.assertRegex(md.stem, r'^\d{8}T\d{6}\.\d{6}Z-[0-9a-f]{8}$')
            data = json.loads(md.with_suffix('.json').read_text(encoding='utf-8'))
            self.assertEqual(list(data), KEYS + ['person'])
            self.assertEqual(data['id'], md.stem)
            self.assertEqual(data['status'], 'active')
            self.assertEqual(data['evidence'], ['a.log'])
            self.assertEqual(data['touched_files'], ['src/a.ts'])
            self.assertEqual(data['confidence'], 'agent-reported; verify evidence before acting')
            self.assertEqual(data['person'], 'atishay')
            text = md.read_text(encoding='utf-8')
            self.assertTrue(text.startswith('---\ntitle: "Fix the login"\ntype: checkpoint\nstatus: active\nupdated: '))
            self.assertIn('\n---\n\n# Fix the login\n\n## id\n\n"' + md.stem + '"\n\n## observed_at\n', text)
            self.assertIn('## touched_files\n\n["src/a.ts"]\n', text)
            self.assertEqual(re.findall(r'^## (\w+)$', text, re.M), KEYS + ['person'])

    def test_person_defaults_to_configured_person(self):
        with BrainEnv(person='cto', display='CTO', role='member') as env:
            md = handoff.write('mockmob', 'codex', 't', 'n')
            self.assertEqual(json.loads(md.with_suffix('.json').read_text(encoding='utf-8'))['person'], 'cto')

    def test_redacts_secrets_and_strips_leaked_markup(self):
        with BrainEnv() as env:
            md = handoff.write('mockmob', 'claude', 'Key sk-ant-api03-' + 'a' * 40, 'next</next><parameter name="done">oops',
                               done='token ghp_' + 'b' * 30 + ' and API_' + 'KEY=' + 'supersecretvalue123', evidence=['pass' + 'word: ' + 'hunter2hunter2'])
            raw = md.with_suffix('.json').read_text(encoding='utf-8') + md.read_text(encoding='utf-8')
            self.assertNotIn('a' * 40, raw)
            self.assertNotIn('ghp_' + 'b' * 30, raw)
            self.assertNotIn('supersecretvalue123', raw)
            self.assertNotIn('hunter2hunter2', raw)
            self.assertNotIn('oops', raw)
            data = json.loads(md.with_suffix('.json').read_text(encoding='utf-8'))
            self.assertEqual(data['next'], 'next')

    def test_unique_files_and_no_staging_leftovers(self):
        with BrainEnv() as env:
            paths = {handoff.write('mockmob', 'claude', 't%d' % i, 'n') for i in range(25)}
            self.assertEqual(len(paths), 25)
            names = os.listdir(env.brain / 'handoffs' / 'mockmob')
            self.assertEqual(len(names), 50)
            self.assertFalse([n for n in names if '.tmp-' in n])

    def test_rejects_bad_project_slug(self):
        with BrainEnv():
            with self.assertRaises(ValueError):
                handoff.write('../evil', 'a', 't', 'n')

    def test_unicode_survives(self):
        with BrainEnv():
            md = handoff.write('mockmob', 'claude', 'Rupee ₹ and भारत', 'आगे')
            self.assertEqual(json.loads(md.with_suffix('.json').read_text(encoding='utf-8'))['task'], 'Rupee ₹ and भारत')


class HandoffScanTests(unittest.TestCase):
    def test_scan_newest_first_with_path_and_stamp(self):
        with BrainEnv() as env:
            env.handover('cto', task='old', minutes_ago=120)
            env.handover('cto', task='new', minutes_ago=1)
            env.handover('cto', task='mid', minutes_ago=60)
            found = handoff.scan('mockmob')
            self.assertEqual([d['task'] for d in found], ['new', 'mid', 'old'])
            self.assertTrue(all(isinstance(d['_path'], Path) and re.match(r'\d{8}T\d{6}\.\d{6}Z$', d['_stamp']) for d in found))
            self.assertEqual(len(handoff.scan('mockmob', limit=2)), 2)

    def test_scan_skips_invalid_json_and_tmp(self):
        with BrainEnv() as env:
            env.handover('cto', task='ok')
            folder = env.brain / 'handoffs' / 'mockmob'
            (folder / '20990101T000000.000000Z-deadbeef.json').write_text('{broken', encoding='utf-8')
            (folder / '20990101T000000.000001Z-deadbeef.json.tmp-abc').write_text('{}', encoding='utf-8')
            self.assertEqual([d['task'] for d in handoff.scan('mockmob')], ['ok'])

    def test_scan_missing_folder(self):
        with BrainEnv():
            self.assertEqual(handoff.scan('mockmob'), [])

    def test_classifiers(self):
        self.assertTrue(handoff.is_auto({'agent': 'claude-auto'}))
        self.assertTrue(handoff.is_owner_note({'agent': 'codex-owner-note'}))
        self.assertTrue(handoff.is_team_note({'agent': 'claude-team-note'}))
        self.assertTrue(handoff.is_probe({'agent': 'probe-agent', 'task': 'x'}))
        self.assertTrue(handoff.is_probe({'agent': 'claude', 'task': 'ran ACCTEST today'}))
        self.assertTrue(handoff.is_probe({'agent': 'claude', 'task': 'a test-token check'}))
        self.assertFalse(handoff.is_probe({'agent': 'claude', 'task': 'Fix login'}))
        self.assertTrue(handoff.is_real({'agent': 'claude', 'task': 'Fix login'}))
        for agent in ('claude-auto', 'codex-owner-note', 'x-team-note'):
            self.assertFalse(handoff.is_real({'agent': agent, 'task': 't'}))

    def test_person_of_falls_back_to_owner(self):
        with BrainEnv():
            self.assertEqual(handoff.person_of({'agent': 'claude'}), 'atishay')
            self.assertEqual(handoff.person_of({'agent': 'claude', 'person': 'cto'}), 'cto')

    def test_share_message(self):
        self.assertIn('shared with the team', handoff.share_message({'ok': True, 'unpushed': 0}, 'handoffs/mockmob/x.md'))
        text = handoff.share_message({'ok': False, 'status': 'offline', 'message': 'no network'}, 'handoffs/mockmob/x.md')
        self.assertIn('saved locally', text)
        self.assertIn('offline', text)


class ContinuumCompatibilityTests(unittest.TestCase):
    """Edge case 15: a handover written here reads correctly where AI OS reads it (same fields, same layout)."""

    def test_fields_the_continuum_packet_reads(self):
        with BrainEnv():
            md = handoff.write('mockmob', 'claude', 'Task', 'Next', done='d', status='paused', person='cto')
            data = json.loads(md.with_suffix('.json').read_text(encoding='utf-8'))
            for key in ('agent', 'task', 'status', 'next', 'blockers', 'observed_at', 'evidence', 'verification', 'done'):
                self.assertIn(key, data)
            self.assertIsNotNone(handoff.parse_time(data['observed_at']))
            self.assertIsInstance(data['blockers'], list)
            self.assertIsInstance(data['evidence'], list)

    @unittest.skipUnless((AIOS_SCRIPTS / 'brain.py').exists(), 'AI OS not on this machine')
    def test_layout_matches_ai_os_checkpoint(self):
        """Run AI OS brain.checkpoint against a temp CONTINUUM_ROOT and compare keys, order and .md layout."""
        with BrainEnv() as env, tempfile.TemporaryDirectory() as aios_root:
            script = (
                "import sys, argparse; sys.path.insert(0, %r)\n"
                "import brain\n"
                "a = argparse.Namespace(project='mockmob', agent='claude', task='Same task', status='active', done='did', next='then',"
                " blocker=['b1'], evidence=['e1'], touched=['t1'], verification='v', cost='c')\n"
                "brain.checkpoint(a)\n" % str(AIOS_SCRIPTS))
            env_vars = dict(os.environ, CONTINUUM_ROOT=aios_root, PYTHONIOENCODING='utf-8')
            proc = subprocess.run([sys.executable, '-B', '-c', script], env=env_vars, capture_output=True, text=True, timeout=60)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            theirs = sorted(Path(aios_root, 'handoffs', 'mockmob').glob('*.json'))[0]
            ours = handoff.write('mockmob', 'claude', 'Same task', 'then', done='did', status='active', evidence=['e1'],
                                 touched=['t1'], blockers=['b1'], verification='v', cost='c', person='atishay')
            their_data = json.loads(theirs.read_text(encoding='utf-8'))
            our_data = json.loads(ours.with_suffix('.json').read_text(encoding='utf-8'))
            self.assertEqual(list(our_data), list(their_data) + ['person'])
            for key in KEYS:
                if key not in ('id', 'observed_at'):
                    self.assertEqual(our_data[key], their_data[key], key)
            their_md = theirs.with_suffix('.md').read_text(encoding='utf-8')
            our_md = ours.read_text(encoding='utf-8')
            self.assertEqual(re.findall(r'^## (\w+)$', our_md, re.M)[:13], re.findall(r'^## (\w+)$', their_md, re.M))
            self.assertEqual(our_md.split('\n---\n')[0].splitlines()[:3], their_md.split('\n---\n')[0].splitlines()[:3])


if __name__ == '__main__':
    unittest.main()
