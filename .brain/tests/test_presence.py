import json
import unittest

from _brainenv import BrainEnv

from brainlib import presence


class PresenceTests(unittest.TestCase):
    def test_write_read_remove_claim(self):
        with BrainEnv(person='cto') as env:
            cfg = env.cfg()
            path = presence.write_claim(cfg, {'harness': 'claude', 'session': 'abcdef1234567890', 'repo': 'mockmob', 'branch': 'feat',
                                              'cwd_name': 'mockmob', 'task': 'Fix things', 'touched': ['a.ts', 'b.ts']})
            self.assertEqual(path, env.brain / 'claims' / 'cto' / 'abcdef12.json')
            data = json.loads(path.read_text(encoding='utf-8'))
            for key in ('person', 'harness', 'session', 'host', 'started_at', 'last_active', 'repo', 'branch', 'cwd_name', 'task', 'touched'):
                self.assertIn(key, data)
            self.assertEqual(data['person'], 'cto')
            self.assertEqual(data['touched'], ['a.ts', 'b.ts'])
            self.assertEqual(presence.read_claim(cfg, 'abcdef1234567890')['task'], 'Fix things')
            self.assertTrue(presence.remove_claim(cfg, 'abcdef1234567890'))
            self.assertFalse(path.exists())
            self.assertFalse(presence.remove_claim(cfg, 'abcdef1234567890'))

    def test_touched_capped_at_50_and_no_tmp_left(self):
        with BrainEnv(person='cto') as env:
            presence.write_claim(env.cfg(), {'session': 's1', 'touched': ['f%d' % i for i in range(80)]})
            data = json.loads((env.brain / 'claims' / 'cto' / 's1.json').read_text(encoding='utf-8'))
            self.assertEqual(len(data['touched']), 50)
            self.assertEqual(data['touched'][-1], 'f79')
            self.assertEqual([p.name for p in (env.brain / 'claims' / 'cto').iterdir()], ['s1.json'])

    def test_active_claims_window_and_exclusion(self):
        with BrainEnv() as env:
            env.claim('cto', session='aaaaaaaa', minutes_ago=5)
            env.claim('cto', session='bbbbbbbb', minutes_ago=181)  # older than 3 hours: ignored
            env.claim('dev2', session='cccccccc', minutes_ago=120)
            env.claim('atishay', session='dddddddd', minutes_ago=1)
            cfg = env.cfg()
            got = presence.active_claims(cfg)
            self.assertEqual({(c['person'], c['session'][:8]) for c in got},
                             {('cto', 'aaaaaaaa'), ('dev2', 'cccccccc'), ('atishay', 'dddddddd')})
            self.assertEqual(got[0]['person'], 'atishay')  # newest first
            others = presence.active_claims(cfg, exclude_person='atishay')
            self.assertEqual({c['person'] for c in others}, {'cto', 'dev2'})

    def test_bad_claim_file_is_ignored(self):
        with BrainEnv() as env:
            env.claim('cto', session='aaaaaaaa')
            (env.brain / 'claims' / 'cto' / 'broken.json').write_text('{nope', encoding='utf-8')
            self.assertEqual(len(presence.active_claims(env.cfg())), 1)

    def test_overlaps(self):
        with BrainEnv() as env:
            env.claim('cto', session='aaaaaaaa', touched=['src/App.tsx', 'docs/x.md'], repo='mockmob', branch='cto-branch')
            env.claim('atishay', session='bbbbbbbb', touched=['src/App.tsx'])
            env.claim('dev2', session='cccccccc', touched=['src/App.tsx'], repo='other-repo', minutes_ago=400)
            cfg = env.cfg()
            hits = presence.overlaps(cfg, 'src/App.tsx', exclude_person='atishay')
            self.assertEqual([c['person'] for c in hits], ['cto'])
            self.assertEqual(hits[0]['branch'], 'cto-branch')
            self.assertEqual(presence.overlaps(cfg, 'src\\app.tsx', exclude_person='atishay')[0]['person'], 'cto')
            self.assertEqual(presence.overlaps(cfg, 'src/Other.tsx', exclude_person='atishay'), [])
            self.assertEqual(presence.overlaps(cfg, 'src/App.tsx', exclude_person='atishay', repo='different'), [])

    def test_prune_own_removes_only_my_stale_claims(self):
        with BrainEnv(person='cto') as env:
            old = env.claim('cto', session='aaaaaaaa', minutes_ago=300)
            fresh = env.claim('cto', session='bbbbbbbb', minutes_ago=5)
            theirs = env.claim('atishay', session='cccccccc', minutes_ago=600)
            removed = presence.prune_own(env.cfg())
            self.assertEqual(len(removed), 1)
            self.assertFalse(old.exists())
            self.assertTrue(fresh.exists())
            self.assertTrue(theirs.exists())


if __name__ == '__main__':
    unittest.main()
