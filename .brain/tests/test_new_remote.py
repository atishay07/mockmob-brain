"""The first sync into a brand-new GitHub repo: empty, or created with a README. The brain must go up on its own,
without a clash and without rewriting every file. Uses _gitfixture; never touches GitHub."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))

import _gitfixture as gf  # noqa: E402
from brainlib import gitops  # noqa: E402


class NewRemoteTests(unittest.TestCase):
    def setUp(self):
        self.fx = gf.make_fixture(1)
        self.addCleanup(self.fx.cleanup)
        self.a = self.fx.clones[0]
        self.a.write('docs/NOW.md', '# NOW\n\nbrain content\n')
        self.a.handover('written before the repo existed')
        with self.a.active():
            self.a.commit_pending()

    def new_bare(self, name, readme=False):
        root = Path(self.fx.root)
        bare = root / f'{name}.git'
        env = self.fx.git_env()
        gitops.run(['init', '-q', '--bare', '-b', 'main', str(bare)], cwd=root, timeout=60, env=env)
        if readme:
            seed = root / f'{name}-seed'
            seed.mkdir()
            gitops.run(['init', '-q', '-b', 'main'], cwd=seed, timeout=60, env=env)
            (seed / 'README.md').write_text('# mockmob-brain\n', encoding='utf-8')
            (seed / '.gitignore').write_text('node_modules/\n', encoding='utf-8')
            gitops.run(['add', '.'], cwd=seed, timeout=60, env=env)
            gitops.run(['-c', 'user.name=gh', '-c', 'user.email=gh@example.com', 'commit', '-qm', 'Initial commit'], cwd=seed, timeout=60, env=env)
            gitops.run(['push', '-q', str(bare), 'main'], cwd=seed, timeout=60, env=env)
        return bare

    def files_on(self, bare):
        r = gitops.run(['ls-tree', '-r', '--name-only', 'main'], cwd=bare, timeout=60, env=self.fx.git_env())
        return set(r.out.split()) if r.ok else set()

    def test_empty_new_remote_gets_everything_even_with_a_stale_tracking_ref(self):
        with self.a.active():
            self.a.sync()  # the old remote: leaves refs/remotes/origin/main pointing at our HEAD
        bare = self.new_bare('fresh')
        self.a.set_remote_url(str(bare))
        with self.a.active():
            res = self.a.sync(force=True)
        self.assertTrue(res['ok'], res)
        self.assertIn('docs/NOW.md', self.files_on(bare))
        self.assertTrue(any(f.startswith('handoffs/') for f in self.files_on(bare)))

    def test_new_remote_with_a_readme_is_adopted_not_clashed(self):
        bare = self.new_bare('withreadme', readme=True)
        self.a.set_remote_url(str(bare))
        self.a.git('update-ref', '-d', 'refs/remotes/origin/main')
        tracked_before = self.a.tracked()
        with self.a.active():
            res = self.a.sync(force=True)
        self.assertTrue(res['ok'], res)
        files = self.files_on(bare)
        self.assertIn('docs/NOW.md', files)
        self.assertTrue(tracked_before <= files, tracked_before - files)
        self.assertEqual(self.a.read('docs/NOW.md'), '# NOW\n\nbrain content\n')
        self.assertFalse(self.a.refs('refs/brain-backup/*'), 'no clash fallback should have run')

    def test_a_real_unrelated_remote_is_not_adopted(self):
        bare = self.new_bare('other', readme=True)
        env = self.fx.git_env()
        seed = Path(self.fx.root) / 'other-seed'
        (seed / 'docs').mkdir()
        (seed / 'docs' / 'SOMEONE-ELSES.md').write_text('# not ours\n', encoding='utf-8')
        gitops.run(['add', '.'], cwd=seed, timeout=60, env=env)
        gitops.run(['-c', 'user.name=x', '-c', 'user.email=x@example.com', 'commit', '-qm', 'other work'], cwd=seed, timeout=60, env=env)
        gitops.run(['push', '-q', str(bare), 'main'], cwd=seed, timeout=60, env=env)
        self.a.set_remote_url(str(bare))
        self.a.git('update-ref', '-d', 'refs/remotes/origin/main')
        with self.a.active():
            self.a.sync(force=True)
        log = gitops.run(['log', '--format=%s', 'main'], cwd=bare, timeout=60, env=env).out
        self.assertNotIn("adopt the new GitHub repo's starter commit", log)


if __name__ == '__main__':
    unittest.main()
