"""Agent-side code against the real sync engine, two clones and a bare remote (no mocks of brainlib)."""
import json
import unittest
from pathlib import Path

from _gitfixture import make_fixture

import hook
from brainlib import config, handoff, packet, presence, sessions


def add_code_repo(clone):
    """A fake MockMob code checkout next to the clone, registered as its code_dir."""
    code = clone.path.parent / f'{clone.name}-code' / 'mockmob'
    (code / '.git').mkdir(parents=True)
    (code / '.git' / 'config').write_text('[remote "origin"]\n\turl = https://github.com/atishay07/mockmob.git\n', encoding='utf-8')
    (code / '.git' / 'HEAD').write_text(f'ref: refs/heads/{clone.name}-branch\n', encoding='utf-8')
    cfg_path = clone.state_dir / 'config.json'
    cfg = json.loads(cfg_path.read_text(encoding='utf-8'))
    cfg['code_dirs'] = [str(code)]
    cfg_path.write_text(json.dumps(cfg), encoding='utf-8')
    return code


class RealSyncIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.fx = make_fixture(2)
        self.addCleanup(self.fx.cleanup)
        self.a, self.b = self.fx.clones
        self.code = {c.name: add_code_repo(c) for c in self.fx.clones}

    def fire(self, clone, event, sid, **payload):
        data = {'session_id': sid, 'cwd': str(self.code[clone.name]), 'transcript_path': ''}
        data.update(payload)
        with clone.active():
            return hook.main(['claude', event], json.dumps(data))

    def test_two_clones_write_handovers_and_both_reach_the_remote(self):
        """Edge case 1 with the real handover writer: both push, both files survive, nothing conflicts."""
        from brainlib import sync
        with self.a.active():
            first = handoff.write('mockmob', 'claude', 'Alice task', 'alice next')
        with self.b.active():
            second = handoff.write('mockmob', 'claude', 'Bob task', 'bob next')
            self.assertTrue(sync.push()['ok'])
        with self.a.active():
            res = sync.push()
        self.assertTrue(res['ok'], res)
        remote = self.fx.remote_files()
        for md in (first, second):
            rel = md.relative_to(md.parents[2]).as_posix()
            self.assertIn(rel, remote)
            self.assertIn(rel[:-3] + '.json', remote)
        with self.b.active():
            self.assertTrue(sync.pull(force=True)['ok'])
            cfg = config.load()
            text = packet.build(cfg)
        self.assertIn('Alice task', text)
        self.assertIn('alice |', text)
        self.assertIn('Bob task', text)

    def test_session_flow_across_two_people(self):
        sid_a, sid_b = 'alice-session-0001', 'bob-session-00002'
        out = self.fire(self.a, 'SessionStart', sid_a)
        self.assertIn('MOCKMOB TEAM BRAIN | Alice (member)', out)
        self.fire(self.a, 'UserPromptSubmit', sid_a, prompt='Rebuild the app shell')
        edited = self.code['alice'] / 'src' / 'App.tsx'
        edited.parent.mkdir(parents=True)
        edited.write_text('x', encoding='utf-8')
        self.assertEqual(self.fire(self.a, 'PostToolUse', sid_a, tool_name='Edit', tool_input={'file_path': str(edited)}), '')
        res = self.a.sync(force=True)
        self.assertTrue(res['ok'], res)
        self.assertIn(f'claims/alice/{sid_a[:8]}.json', self.fx.remote_files())
        claim = json.loads(self.fx.remote_show(f'claims/alice/{sid_a[:8]}.json'))
        self.assertEqual((claim['task'], claim['touched'], claim['branch'], claim['repo']),
                         ('Rebuild the app shell', ['src/App.tsx'], 'alice-branch', 'mockmob'))

        packet_b = self.fire(self.b, 'SessionStart', sid_b)
        self.assertIn('Working right now:', packet_b)
        self.assertIn('alice on mockmob@alice-branch: Rebuild the app shell', packet_b)
        other = self.code['bob'] / 'src' / 'App.tsx'
        other.parent.mkdir(parents=True)
        other.write_text('y', encoding='utf-8')
        warn = self.fire(self.b, 'PostToolUse', sid_b, tool_name='Write', tool_input={'file_path': str(other)})
        text = json.loads(warn)['hookSpecificOutput']['additionalContext']
        self.assertIn('alice', text)
        self.assertIn('alice-branch', text)

        self.fire(self.a, 'Stop', sid_a, last_assistant_message='Shell half done')
        self.assertEqual(self.fire(self.a, 'SessionEnd', sid_a), '')
        auto = [d for d in handoff.scan('mockmob', root=self.a.path) if handoff.is_auto(d)]
        self.assertEqual(len(auto), 1)
        self.assertEqual(auto[0]['person'], 'alice')
        self.assertFalse((self.a.path / 'claims' / 'alice' / f'{sid_a[:8]}.json').exists())
        res = self.a.sync(force=True)
        self.assertTrue(res['ok'], res)
        self.assertNotIn(f'claims/alice/{sid_a[:8]}.json', self.fx.remote_files())
        self.assertTrue([f for f in self.fx.remote_files() if f.startswith('handoffs/mockmob/') and f.endswith('.json')])

        # Bob's next prompt after a pull: real handovers are fed, alice's auto-capture is not
        self.b.pull(force=True)
        with self.b.active():
            handoff.write('mockmob', 'claude', 'Bob finished', 'done', person='bob')
        self.b.sync(force=True)
        self.a.pull(force=True)
        fed = self.fire(self.a, 'UserPromptSubmit', sid_a, prompt='what did bob do')
        self.assertIn('Bob finished', fed)
        self.assertNotIn('Shell half done', fed)


if __name__ == '__main__':
    unittest.main()
