"""FileLock: exclusivity, stale-lock recovery, timeouts, cross-process behaviour."""
from __future__ import annotations

import json
import os
import shutil
import socket
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from pathlib import Path

import _gitfixture  # noqa: F401  (puts .brain on sys.path)
from brainlib.lock import FileLock, LockTimeout, pid_alive

BRAIN_DOT = Path(__file__).resolve().parents[1]


def dead_pid() -> int:
    p = subprocess.Popen([sys.executable, "-c", "pass"])
    p.wait()
    return p.pid


class LockTests(unittest.TestCase):
    def setUp(self):
        self.dir = Path(tempfile.mkdtemp(prefix="mmb-lock-"))
        self.addCleanup(shutil.rmtree, self.dir, True)
        self.path = self.dir / "locks" / "git.lock"

    def write_lock(self, pid, at=None, host=None, token="foreign"):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(
            json.dumps({"pid": pid, "host": host or socket.gethostname(), "at": at or time.time(), "token": token}),
            encoding="utf-8",
        )

    def test_acquire_release_and_exclusivity(self):
        a, b = FileLock(self.path), FileLock(self.path)
        self.assertTrue(a.acquire(0))
        self.assertTrue(self.path.exists())
        data = json.loads(self.path.read_text(encoding="utf-8"))
        self.assertEqual(data["pid"], os.getpid())
        self.assertEqual(data["host"], socket.gethostname())
        self.assertIn("at", data)
        self.assertFalse(b.acquire(0))
        a.release()
        self.assertFalse(self.path.exists())
        self.assertTrue(b.acquire(0))
        b.release()

    def test_context_manager_and_timeout(self):
        with FileLock(self.path) as lk:
            self.assertTrue(lk.held)
            t0 = time.monotonic()
            with self.assertRaises(LockTimeout):
                with FileLock(self.path, timeout=0.3):
                    pass
            self.assertLess(time.monotonic() - t0, 3)
        self.assertFalse(self.path.exists())

    def test_acquire_waits_for_release(self):
        a = FileLock(self.path)
        self.assertTrue(a.acquire(0))
        threading.Timer(0.4, a.release).start()
        b = FileLock(self.path)
        t0 = time.monotonic()
        self.assertTrue(b.acquire(5))
        self.assertGreaterEqual(time.monotonic() - t0, 0.3)
        b.release()

    def test_acquire_zero_returns_immediately(self):
        a = FileLock(self.path)
        a.acquire(0)
        t0 = time.monotonic()
        self.assertFalse(FileLock(self.path).acquire(0))
        self.assertLess(time.monotonic() - t0, 1)
        a.release()

    def test_stale_lock_dead_pid_is_broken(self):
        self.write_lock(dead_pid())
        lk = FileLock(self.path)
        self.assertTrue(lk.acquire(0))
        data = json.loads(self.path.read_text(encoding="utf-8"))
        self.assertEqual(data["pid"], os.getpid())
        lk.release()
        self.assertEqual([p.name for p in self.path.parent.glob("*.stale-*")], [])

    def test_stale_lock_by_age_even_if_pid_alive(self):
        self.write_lock(os.getpid())
        old = time.time() - 1000
        os.utime(self.path, (old, old))
        lk = FileLock(self.path, stale_after=120)
        self.assertTrue(lk.acquire(0))
        lk.release()

    def test_fresh_lock_of_live_process_is_respected(self):
        self.write_lock(os.getpid())
        self.assertFalse(FileLock(self.path, stale_after=120).acquire(0))

    def test_other_host_lock_judged_by_age_only(self):
        self.write_lock(dead_pid(), host="some-other-machine")
        self.assertFalse(FileLock(self.path, stale_after=120).acquire(0))
        old = time.time() - 1000
        os.utime(self.path, (old, old))
        self.assertTrue(FileLock(self.path, stale_after=120).acquire(0))

    def test_empty_lock_file_is_stale_only_when_abandoned(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text("", encoding="utf-8")
        self.assertFalse(FileLock(self.path, stale_after=120).acquire(0))
        old = time.time() - 60
        os.utime(self.path, (old, old))
        self.assertTrue(FileLock(self.path, stale_after=120).acquire(0))

    def test_touch_keeps_a_long_running_lock_fresh(self):
        a = FileLock(self.path, stale_after=2)
        a.acquire(0)
        for _ in range(4):
            time.sleep(0.7)
            a.touch()
            self.assertFalse(FileLock(self.path, stale_after=2).acquire(0))
        a.release()

    def test_release_never_deletes_someone_elses_lock(self):
        a = FileLock(self.path)
        a.acquire(0)
        self.write_lock(os.getpid(), token="someone-else")
        a.release()
        self.assertTrue(self.path.exists())
        self.assertEqual(json.loads(self.path.read_text(encoding="utf-8"))["token"], "someone-else")

    def test_release_without_acquire_is_harmless(self):
        FileLock(self.path).release()
        self.write_lock(os.getpid())
        FileLock(self.path).release()
        self.assertTrue(self.path.exists())

    def test_holder(self):
        a = FileLock(self.path)
        self.assertIsNone(a.holder())
        a.acquire(0)
        self.assertEqual(FileLock(self.path).holder()["pid"], os.getpid())
        a.release()
        self.assertIsNone(a.holder())

    def test_pid_alive(self):
        self.assertTrue(pid_alive(os.getpid()))
        self.assertFalse(pid_alive(dead_pid()))
        self.assertFalse(pid_alive(0))
        self.assertFalse(pid_alive("not a pid"))

    def test_threads_never_overlap(self):
        counter = {"inside": 0, "max": 0, "done": 0}
        guard = threading.Lock()

        def worker():
            lk = FileLock(self.path)
            for _ in range(3):
                self.assertTrue(lk.acquire(30))
                with guard:
                    counter["inside"] += 1
                    counter["max"] = max(counter["max"], counter["inside"])
                time.sleep(0.01)
                with guard:
                    counter["inside"] -= 1
                    counter["done"] += 1
                lk.release()

        threads = [threading.Thread(target=worker) for _ in range(8)]
        [t.start() for t in threads]
        [t.join(60) for t in threads]
        self.assertEqual(counter["done"], 24)
        self.assertEqual(counter["max"], 1)

    def test_processes_never_overlap(self):
        log = self.dir / "order.log"
        code = (
            "import sys, time\n"
            f"sys.path.insert(0, {str(BRAIN_DOT)!r})\n"
            "from brainlib.lock import FileLock\n"
            f"lk = FileLock({str(self.path)!r})\n"
            "n = sys.argv[1]\n"
            "for i in range(3):\n"
            "    assert lk.acquire(60)\n"
            f"    open({str(log)!r}, 'a').write('start-%s\\n' % n)\n"
            "    time.sleep(0.05)\n"
            f"    open({str(log)!r}, 'a').write('end-%s\\n' % n)\n"
            "    lk.release()\n"
        )
        procs = [subprocess.Popen([sys.executable, "-c", code, str(i)]) for i in range(4)]
        for p in procs:
            self.assertEqual(p.wait(120), 0)
        lines = log.read_text().split()
        self.assertEqual(len(lines), 24)
        for i in range(0, len(lines), 2):  # every start is immediately followed by its own end
            self.assertTrue(lines[i].startswith("start-"))
            self.assertEqual(lines[i + 1], lines[i].replace("start-", "end-"))

    def test_killed_holder_does_not_block_forever(self):
        code = (
            "import sys, time\n"
            f"sys.path.insert(0, {str(BRAIN_DOT)!r})\n"
            "from brainlib.lock import FileLock\n"
            f"lk = FileLock({str(self.path)!r})\n"
            "assert lk.acquire(5)\n"
            "print('held', flush=True)\n"
            "time.sleep(60)\n"
        )
        p = subprocess.Popen([sys.executable, "-c", code], stdout=subprocess.PIPE)
        try:
            self.assertEqual(p.stdout.readline().strip(), b"held")
            self.assertFalse(FileLock(self.path).acquire(0))
        finally:
            p.kill()
            p.wait()
            p.stdout.close()
        self.assertTrue(FileLock(self.path).acquire(5))


if __name__ == "__main__":
    unittest.main()
