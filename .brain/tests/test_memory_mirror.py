import os
import time
import unittest
from pathlib import Path

from _brainenv import BrainEnv

from brainlib import memory_mirror


def put(folder, name, text, mtime=None):
    path = Path(folder) / name
    path.write_text(text, encoding='utf-8', newline='\n')
    if mtime:
        os.utime(path, (mtime, mtime))
    return path


class MemoryMirrorTests(unittest.TestCase):
    def test_copies_new_and_changed_files_only(self):
        with BrainEnv(memory=True) as env:
            put(env.mem, 'MEMORY.md', '- [A](a.md) - first\n')
            put(env.mem, 'a.md', '---\nname: a\ntype: feedback\n---\nbody\n')
            res = memory_mirror.mirror(env.cfg())
            self.assertEqual(sorted(res['changed']), ['MEMORY.md', 'a.md'])
            dest = env.brain / 'playbook' / 'memory' / 'atishay'
            self.assertEqual((dest / 'a.md').read_text(encoding='utf-8'), '---\nname: a\ntype: feedback\n---\nbody\n')
            self.assertEqual(memory_mirror.mirror(env.cfg())['changed'], [])
            put(env.mem, 'a.md', '---\nname: a\ntype: feedback\n---\nbody v2\n')
            self.assertEqual(memory_mirror.mirror(env.cfg())['changed'], ['a.md'])
            self.assertIn('v2', (dest / 'a.md').read_text(encoding='utf-8'))

    def test_skips_user_type_big_and_secret_files(self):
        with BrainEnv(memory=True) as env:
            put(env.mem, 'me.md', '---\nname: me\ntype: user\n---\nI am private\n')
            put(env.mem, 'big.md', 'x' * (200 * 1024 + 1))
            put(env.mem, 'leak.md', '---\ntype: reference\n---\nline\nkey: sk-ant-api03-' + 'q' * 40 + '\n')
            put(env.mem, 'ok.md', '---\ntype: project\n---\nfine\n')
            res = memory_mirror.mirror(env.cfg())
            dest = env.brain / 'playbook' / 'memory' / 'atishay'
            self.assertEqual(res['changed'], ['ok.md'])
            self.assertEqual(sorted(p.name for p in dest.iterdir()), ['ok.md'])
            blocked = {b['name']: b for b in res['blocked']}
            self.assertEqual(set(blocked), {'big.md', 'leak.md'})
            self.assertEqual(blocked['leak.md']['line'], 5)
            self.assertNotIn('sk-ant', str(res))

    def test_newer_file_wins_across_dirs(self):
        with BrainEnv(memory=True) as env:
            other = env.tmp / 'memory2'
            other.mkdir()
            env.write_config(memory_dirs=[str(env.mem), str(other)])
            now = time.time()
            put(env.mem, 'same.md', 'older\n', mtime=now - 1000)
            put(other, 'same.md', 'newer\n', mtime=now)
            memory_mirror.mirror(env.cfg())
            self.assertEqual((env.brain / 'playbook' / 'memory' / 'atishay' / 'same.md').read_text(encoding='utf-8'), 'newer\n')

    def test_deletes_only_files_the_mirror_created_when_source_is_gone(self):
        with BrainEnv(memory=True) as env:
            dest = env.brain / 'playbook' / 'memory' / 'atishay'
            dest.mkdir(parents=True)
            (dest / 'hand-made.md').write_text('someone put this here', encoding='utf-8')
            src = put(env.mem, 'gone.md', 'will go\n')
            memory_mirror.mirror(env.cfg())
            self.assertTrue((dest / 'gone.md').exists())
            src.unlink()
            res = memory_mirror.mirror(env.cfg())
            self.assertIn('gone.md', res['changed'])
            self.assertFalse((dest / 'gone.md').exists())
            self.assertTrue((dest / 'hand-made.md').exists())

    def test_blocked_source_keeps_existing_mirrored_copy(self):
        with BrainEnv(memory=True) as env:
            put(env.mem, 'n.md', 'clean\n')
            memory_mirror.mirror(env.cfg())
            put(env.mem, 'n.md', 'password: ' + 'z' * 20 + '\n')
            res = memory_mirror.mirror(env.cfg())
            self.assertEqual([b['name'] for b in res['blocked']], ['n.md'])
            self.assertEqual((env.brain / 'playbook' / 'memory' / 'atishay' / 'n.md').read_text(encoding='utf-8'), 'clean\n')

    def test_no_memory_dirs_is_a_noop(self):
        with BrainEnv() as env:
            self.assertEqual(memory_mirror.mirror(env.cfg()), {'changed': [], 'blocked': []})

    def test_front_matter_detection(self):
        self.assertTrue(memory_mirror.is_user_type('---\nname: x\ntype: user\n---\n'))
        self.assertTrue(memory_mirror.is_user_type('---\ntype: "user"\n---\n'))
        self.assertFalse(memory_mirror.is_user_type('---\ntype: feedback\n---\ntype: user\n'))
        self.assertFalse(memory_mirror.is_user_type('no front matter\ntype: user\n'))


if __name__ == '__main__':
    unittest.main()
