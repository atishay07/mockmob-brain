"""Sync core tests: DESIGN.md section 10 items 1-6, 8-11 and 13, plus the plumbing around them.

Every test builds its own bare remote and clones under the system temp dir (see
``_gitfixture``), never touches GitHub, the real STATE_DIR or the user's git config.
Secret-looking samples are built at run time so this file never trips the scan.
"""
from __future__ import annotations

import json
import os
import random
import subprocess
import sys
import threading
import time
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

import _gitfixture as gf
from brainlib import config, gitops, safety, sync
from brainlib.lock import FileLock, pid_alive

BRAIN_DOT = Path(__file__).resolve().parents[1]
REQUIRED_KEYS = {
    "ok", "status", "message", "changed_files", "committed", "pushed", "unpushed", "blocked",
    "merged_both_sides", "saved_conflicts", "head", "at",
}
STATUSES = {"ok", "skipped", "offline", "auth", "locked", "conflict-saved", "error", "not-a-repo", "wrong-branch"}
FAKE_SSH = """\
import os, sys, time
pf = os.environ.get("FAKE_SSH_PIDFILE")
if pf:
    open(pf, "w").write(str(os.getpid()))
mode = os.environ.get("FAKE_SSH_MODE", "deny")
if mode == "hang":
    time.sleep(120)
sys.stderr.write("git@example.invalid: Permission denied (publickey).\\r\\n")
sys.stderr.write("fatal: Could not read from remote repository.\\r\\n")
sys.exit(255)
"""


# Fake secrets are assembled at run time so this file never matches safety.scan_text.
PW_LINE = "pass" + "word = " + "Zq8f3Lm92XvTn40P" + "aBcD" + chr(10)
API_LINE = "api" + "_key = " + "Zq8f3Lm92XvTn40P" + "aBcD" + chr(10)


def secret_sample() -> str:
    return "sk-" + "ant-" + "api03-" + "A1b2C3d4E5f6G7h8I9j0K1l2M3n4"


def fs_is_case_sensitive(folder: Path) -> bool:
    probe = folder / "CaseProbe.tmp"
    probe.write_text("x")
    try:
        return not (folder / "caseprobe.tmp").exists()
    finally:
        probe.unlink()


class SyncCase(unittest.TestCase):
    n_clones = 2

    def setUp(self):
        self.fx = gf.make_fixture(self.n_clones)
        self.addCleanup(self.fx.cleanup)
        self.a = self.fx.clones[0]
        self.b = self.fx.clones[1] if self.n_clones > 1 else None

    def assertShape(self, res):
        self.assertTrue(REQUIRED_KEYS <= set(res), f"missing keys: {REQUIRED_KEYS - set(res)}")
        self.assertIn(res["status"], STATUSES)
        self.assertIsInstance(res["ok"], bool)
        self.assertIsInstance(res["blocked"], list)
        self.assertIsInstance(res["changed_files"], list)
        self.assertRegex(res["at"], r"^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        return res

    def remote_has(self, rel):
        return rel in self.fx.remote_files()

    def sync_in_subprocess(self, clone, **kwargs):
        args = ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
        code = (
            "import sys, json\n"
            f"sys.path.insert(0, {str(BRAIN_DOT)!r})\n"
            "from brainlib import sync\n"
            f"print('RESULT' + json.dumps(sync.sync({args})))\n"
        )
        return subprocess.Popen(
            [sys.executable, "-c", code], env=clone.subprocess_env(), stdout=subprocess.PIPE,
            stderr=subprocess.PIPE, text=True,
        )

    @staticmethod
    def parse_result(proc, timeout=180):
        out, err = proc.communicate(timeout=timeout)
        for line in out.splitlines():
            if line.startswith("RESULT"):
                return json.loads(line[len("RESULT"):])
        raise AssertionError(f"no result from subprocess (rc={proc.returncode}): {out}\n{err}")


# ----------------------------------------------------------------------------
class BasicsTests(SyncCase):
    def test_commit_pending_commits_with_summary_and_person(self):
        rel = self.a.handover("ship the sync core")
        res = self.assertShape(self.a.commit_pending())
        self.assertEqual(res["status"], "ok")
        self.assertEqual(sorted(res["committed"]), sorted([rel, rel[:-5] + ".md"]))
        self.assertEqual(self.a.log_subjects(1), ["brain: ship the sync core (alice)"])
        self.assertEqual(self.a.must_git("status", "--porcelain").strip(), "")
        self.assertEqual(self.a.must_git("log", "-1", "--format=%an <%ae>").strip(), "Alice <alice@example.test>")
        self.assertEqual(res["unpushed"], 1)

    def test_commit_pending_nothing_to_do(self):
        res = self.assertShape(self.a.commit_pending())
        self.assertEqual((res["status"], res["committed"]), ("ok", []))

    def test_file_count_summary_without_a_handover(self):
        self.a.write("docs/one.md", "1\n")
        self.a.write("docs/two.md", "2\n")
        self.a.commit_pending()
        self.assertEqual(self.a.log_subjects(1), ["brain: 2 files (alice)"])

    def test_commit_pending_custom_message_and_paths(self):
        self.a.write("docs/one.md", "1\n")
        self.a.write("docs/two.md", "2\n")
        res = self.a.commit_pending("only one", paths=["docs/one.md"])
        self.assertEqual(res["committed"], ["docs/one.md"])
        self.assertEqual(self.a.log_subjects(1), ["brain: only one (alice)"])
        self.assertIn("?? docs/two.md", self.a.must_git("status", "--porcelain"))
        res = self.a.commit_pending(paths=[str(self.a.abs("docs/two.md"))])  # absolute paths are accepted
        self.assertEqual(res["committed"], ["docs/two.md"])

    def test_files_outside_the_allowlist_are_never_staged(self):
        self.a.write("src/app.py", "print('hi')\n")
        self.a.write("package.json", "{}\n")
        self.a.write("docs/ok.md", "ok\n")
        res = self.a.commit_pending()
        self.assertEqual(res["committed"], ["docs/ok.md"])
        self.assertEqual(res["blocked"], [])
        self.assertTrue(self.a.exists("src/app.py"))
        st = self.a.status()
        self.assertEqual(sorted(st["ignored_untracked"]), ["package.json", "src/app.py"])
        self.assertNotIn("src/app.py", self.a.tracked())

    def test_user_staged_files_outside_the_allowlist_do_not_sneak_in(self):
        self.a.write("src/app.py", "print('hi')\n")
        self.a.must_git("add", "src/app.py")
        self.a.write("docs/ok.md", "ok\n")
        res = self.a.commit_pending()
        self.assertEqual(res["committed"], ["docs/ok.md"])
        self.assertNotIn("src/app.py", self.a.tracked())

    def test_deletions_are_committed(self):
        self.a.abs("docs/STATUS.md").unlink()
        res = self.a.commit_pending()
        self.assertEqual(res["committed"], ["docs/STATUS.md"])
        self.assertNotIn("docs/STATUS.md", self.a.tracked())
        self.a.sync(force=True)
        self.assertFalse(self.remote_has("docs/STATUS.md"))

    def test_modifications_are_committed(self):
        self.a.write("docs/NOW.md", "# NOW\n\nchanged\n")
        res = self.a.commit_pending()
        self.assertEqual(res["committed"], ["docs/NOW.md"])

    def test_result_shape_everywhere(self):
        self.assertShape(self.a.status())
        self.assertShape(self.a.pull(force=True))
        self.assertShape(self.a.push())
        self.assertShape(self.a.sync(force=True))
        self.assertShape(self.a.commit_pending())
        with self.a.active():
            self.assertShape(sync.pull())  # throttled
        self.assertEqual(self.a.status()["status"], "ok")

    def test_wrong_branch_does_nothing(self):
        self.a.must_git("checkout", "-q", "-b", "scratch")
        self.a.write("docs/ok.md", "ok\n")
        head = self.a.head()
        for res in (self.a.commit_pending(), self.a.pull(force=True), self.a.push(), self.a.sync(force=True)):
            self.assertShape(res)
            self.assertEqual(res["status"], "wrong-branch")
            self.assertFalse(res["ok"])
        self.assertEqual(self.a.head(), head)
        self.assertEqual(self.a.status()["status"], "wrong-branch")
        self.assertNotIn("docs/ok.md", self.a.tracked())
        self.assertFalse(self.remote_has("docs/ok.md"))

    def test_not_a_repo(self):
        empty = self.fx.root / "empty-dir"
        empty.mkdir()
        cfg = json.loads((self.a.state_dir / "config.json").read_text())
        cfg["brain_dir"] = str(empty)
        (self.a.state_dir / "config.json").write_text(json.dumps(cfg))
        with self.a.active(MOCKMOB_BRAIN=empty):  # the environment variable outranks config.json
            results = [sync.status(), sync.pull(force=True), sync.push(), sync.sync(force=True), sync.commit_pending()]
        for res in results:
            self.assertShape(res)
            self.assertEqual(res["status"], "not-a-repo")

    def test_missing_remote_name_is_an_error_not_a_crash(self):
        self.a.must_git("remote", "remove", "origin")
        res = self.assertShape(self.a.sync(force=True))
        self.assertEqual(res["status"], "error")
        self.assertIn("remote", res["message"])

    def test_locked_when_another_sync_holds_the_lock(self):
        lock = FileLock(self.a.state_dir / "locks" / "git.lock")
        self.assertTrue(lock.acquire(0))
        self.addCleanup(lock.release)
        t0 = time.monotonic()
        with self.a.active():
            for res in (
                sync.pull(lock_timeout=0), sync.sync(lock_timeout=0), sync.push(lock_timeout=0.2),
                sync.commit_pending(lock_timeout=0.2),
            ):
                self.assertShape(res)
                self.assertEqual(res["status"], "locked")
        self.assertLess(time.monotonic() - t0, 5)

    def test_gitattributes_are_in_the_first_commit_and_match_the_repo_file(self):
        text = self.fx.remote_show(".gitattributes")
        self.assertIn("merge=union", text)
        repo_file = BRAIN_DOT.parent / ".gitattributes"
        if repo_file.exists():
            body = repo_file.read_text(encoding="utf-8")
            for line in ("* text=auto eol=lf", "docs/** merge=union", "context/** merge=union",
                         "playbook/** merge=union", "TEAM.md merge=union"):
                self.assertIn(line, body)
                self.assertIn(line, text)

    def test_pull_brings_changes_and_records_sync_json(self):
        self.a.write("docs/new.md", "hello\n")
        self.a.sync(force=True)
        res = self.assertShape(self.b.pull(force=True))
        self.assertEqual(res["status"], "ok")
        self.assertEqual(res["changed_files"], ["docs/new.md"])
        self.assertEqual(self.b.read("docs/new.md"), "hello\n")
        sj = self.b.state_json("sync")
        self.assertEqual(sj["changed_files"], ["docs/new.md"])
        self.assertEqual(sj["head"], self.b.head())
        self.assertEqual(sj["status"], "ok")
        for k in ("last_fetch_at", "last_pull_ok_at"):
            self.assertRegex(sj[k], r"^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        st = self.b.status()
        self.assertEqual(st["last_pull_ok_at"], sj["last_pull_ok_at"])
        self.assertEqual(st["unpushed"], 0)

    def test_pull_throttle_and_force(self):
        self.assertEqual(self.a.pull(force=True)["status"], "ok")
        self.b.write("docs/later.md", "x\n")
        self.b.sync(force=True)
        res = self.a.pull(min_interval=60)
        self.assertEqual(res["status"], "skipped")
        self.assertFalse(self.a.exists("docs/later.md"))
        self.assertEqual(self.a.pull(min_interval=0)["status"], "ok")
        self.assertTrue(self.a.exists("docs/later.md"))
        self.assertEqual(self.a.pull(force=True)["status"], "ok")

    def test_sync_when_nothing_to_do_is_skipped_or_ok(self):
        self.a.sync(force=True)
        res = self.assertShape(self.a.sync())  # within the 60 s throttle: nothing happens
        self.assertEqual(res["status"], "skipped")
        self.assertFalse(res["pushed"])

    def test_push_only_pushes_what_is_ahead(self):
        res = self.assertShape(self.a.push())
        self.assertEqual((res["status"], res["pushed"]), ("ok", False))
        self.a.write("docs/p.md", "p\n")
        res = self.a.push()
        self.assertEqual((res["status"], res["pushed"], res["unpushed"]), ("ok", True, 0))
        self.assertTrue(self.remote_has("docs/p.md"))

    def test_stale_own_claims_are_cleaned_up_after_a_pull(self):
        now = datetime.now(timezone.utc)

        def claim(person, name, age_h):
            last = (now - timedelta(hours=age_h)).strftime("%Y-%m-%dT%H:%M:%SZ")
            self.a.write(f"claims/{person}/{name}.json", json.dumps({"person": person, "last_active": last}))

        claim("alice", "old00001", 5)
        claim("alice", "new00001", 0.2)
        claim("bob", "old00002", 9)  # somebody else's: never touched by alice
        self.a.commit_pending()
        self.a.push()  # push alone never cleans claims up
        self.assertTrue(self.remote_has("claims/alice/old00001.json"))
        res = self.a.sync(force=True)
        self.assertFalse(self.a.exists("claims/alice/old00001.json"))
        self.assertTrue(self.a.exists("claims/alice/new00001.json"))
        self.assertTrue(self.a.exists("claims/bob/old00002.json"))
        self.assertFalse(self.remote_has("claims/alice/old00001.json"), res)
        self.assertTrue(self.remote_has("claims/alice/new00001.json"))
        self.assertTrue(self.remote_has("claims/bob/old00002.json"))


# ----------------------------------------------------------------------------
class TwoWritersTests(SyncCase):
    """Edge cases 1 and 2."""

    def test_two_handovers_at_the_same_moment_both_land(self):
        ra = self.a.handover("alice work", "20261106T100000.000001Z")
        rb = self.b.handover("bob work", "20261106T100000.000002Z")
        self.a.commit_pending()
        self.b.commit_pending()
        res_a = self.a.push()
        self.assertEqual((res_a["status"], res_a["pushed"]), ("ok", True))
        res_b = self.assertShape(self.b.sync(force=True))
        self.assertEqual(res_b["status"], "ok", res_b)
        self.assertTrue(res_b["pushed"])
        self.assertEqual(res_b["saved_conflicts"], [])
        files = self.fx.remote_files()
        for rel in (ra, ra[:-5] + ".md", rb, rb[:-5] + ".md"):
            self.assertIn(rel, files)
        self.a.pull(force=True)
        self.assertTrue(self.a.exists(rb))
        self.assertEqual(self.a.head(), self.b.head())
        self.assertEqual(self.b.status()["unpushed"], 0)
        self.assertEqual(self.fx.remote_git("for-each-ref", "refs/brain-backup").out.strip(), "")

    def test_two_processes_syncing_at_once_both_land(self):
        ra = self.a.handover("alice proc", "20261106T100000.000011Z")
        rb = self.b.handover("bob proc", "20261106T100000.000012Z")
        pa = self.sync_in_subprocess(self.a, force=True, lock_timeout=30)
        pb = self.sync_in_subprocess(self.b, force=True, lock_timeout=30)
        res = [self.parse_result(pa), self.parse_result(pb)]
        for r in res:
            self.assertIn(r["status"], ("ok", "skipped"), r)
            self.assertEqual(r["saved_conflicts"], [])
        # one more round so each side has the other's work
        self.a.sync(force=True)
        self.b.sync(force=True)
        files = self.fx.remote_files()
        for rel in (ra, rb, ra[:-5] + ".md", rb[:-5] + ".md"):
            self.assertIn(rel, files)
            self.assertTrue(self.a.exists(rel) and self.b.exists(rel))
        self.assertEqual(self.a.head(), self.b.head())

    def test_both_edit_now_md_union_merge_and_flag(self):
        self.a.write("docs/NOW.md", "# NOW\n\nline one\nalice says A\nline three\n")
        self.b.write("docs/NOW.md", "# NOW\n\nline one\nbob says B\nline three\n")
        self.assertEqual(self.a.sync(force=True)["status"], "ok")
        res = self.assertShape(self.b.sync(force=True))
        self.assertEqual(res["status"], "ok", res)
        self.assertEqual(res["merged_both_sides"], ["docs/NOW.md"])
        self.assertEqual(res["saved_conflicts"], [])
        text = self.b.read("docs/NOW.md")
        self.assertIn("alice says A", text)
        self.assertIn("bob says B", text)
        self.assertNotIn("<<<<", text)
        self.assertEqual(self.fx.remote_show("docs/NOW.md"), text)
        merged = self.b.state_json("merged")
        self.assertEqual(merged["files"], ["docs/NOW.md"])
        self.assertEqual(self.b.status()["merged_both_sides"], ["docs/NOW.md"])
        self.assertEqual(self.fx.remote_git("for-each-ref", "refs/brain-backup").out.strip(), "")

    def test_handovers_and_claims_are_not_flagged_as_merged(self):
        self.a.write("handoffs/mockmob/shared.md", "a\n")
        self.b.write("handoffs/mockmob/shared.md", "b\n")
        self.a.write("claims/alice/x.json", "{}")
        self.a.sync(force=True)
        res = self.b.sync(force=True)
        self.assertEqual(res["merged_both_sides"], [])

    def test_editing_a_flagged_file_counts_as_the_tidy(self):
        self.a.write("docs/NOW.md", "# NOW\n\nline one\nalice says A\nline three\n")
        self.b.write("docs/NOW.md", "# NOW\n\nline one\nbob says B\nline three\n")
        self.a.sync(force=True)
        self.b.sync(force=True)
        self.assertEqual(self.b.state_json("merged")["files"], ["docs/NOW.md"])
        self.b.write("docs/NOW.md", "# NOW\n\ntidied\n")
        self.b.commit_pending()
        self.assertEqual(self.b.state_json("merged")["files"], [])
        self.assertEqual(self.b.status()["merged_both_sides"], [])

    def test_clear_merged_helper(self):
        self.a.write("docs/NOW.md", "# NOW\n\nline one\nalice says A\nline three\n")
        self.b.write("docs/NOW.md", "# NOW\n\nline one\nbob says B\nline three\n")
        self.a.sync(force=True)
        self.b.sync(force=True)
        with self.b.active():
            sync.clear_merged()
        self.assertEqual(self.b.state_json("merged")["files"], [])


# ----------------------------------------------------------------------------
class ClashTests(SyncCase):
    """Edge case 3: nothing is ever lost, and clashes are flagged."""

    def converge(self, rel, text):
        self.a.write(rel, text)
        self.a.sync(force=True)
        self.b.sync(force=True)

    def test_json_clash_saves_a_conflict_copy_and_keeps_everything(self):
        base = '{\n  "name": "mockmob",\n  "phase": "base",\n  "owner": "x"\n}\n'
        self.converge("docs/spec.json", base)
        self.b.write("docs/spec.json", base.replace("base", "bob-edit"))
        rb = self.b.handover("bob side work")
        self.a.write("docs/spec.json", base.replace("base", "alice-edit"))
        self.assertEqual(self.a.sync(force=True)["status"], "ok")
        self.b.commit_pending()
        old_head = self.b.head()

        res = self.assertShape(self.b.sync(force=True))
        self.assertEqual(res["status"], "conflict-saved", res)
        self.assertTrue(res["ok"])
        self.assertEqual(res["saved_conflicts"], ["docs/spec.json"])
        # backup ref points at the pre-clash HEAD
        refs = self.b.refs("refs/brain-backup/")
        self.assertEqual(len(refs), 1, refs)
        self.assertEqual(self.b.must_git("rev-parse", refs[0]).strip(), old_head)
        self.assertEqual(res["backup_ref"], refs[0])
        # remote version kept in place, local version saved as a conflict copy
        self.assertEqual(self.b.read("docs/spec.json"), base.replace("base", "alice-edit"))
        copies = [p for p in self.b.tracked() if p.startswith("conflicts/") and p.endswith("docs/spec.json")]
        self.assertEqual(len(copies), 1, copies)
        self.assertRegex(copies[0], r"^conflicts/\d{8}T\d{6}Z-bob/docs/spec\.json$")
        self.assertEqual(self.b.read(copies[0]), base.replace("base", "bob-edit"))
        # unrelated local work survived and everything is shared
        self.assertTrue(self.b.exists(rb))
        self.assertIn(rb, self.fx.remote_files())
        self.assertIn(copies[0], self.fx.remote_files())
        self.assertEqual(self.fx.remote_show("docs/spec.json"), base.replace("base", "alice-edit"))
        self.assertIn("brain: kept both versions after a sync clash (bob)", self.b.log_subjects(5))
        self.assertEqual(res["unpushed"], 0)
        self.assertTrue(res["pushed"])
        self.assertEqual(self.b.state_json("sync")["status"], "conflict-saved")
        self.assertIn("docs/spec.json", self.b.state_json("merged")["files"])
        # the old local content is also reachable from the backup ref
        self.assertEqual(
            self.b.must_git("show", f"{refs[0]}:docs/spec.json").replace("\r\n", "\n"), base.replace("base", "bob-edit")
        )

    def test_modify_delete_local_modified_remote_deleted_restores_local(self):
        self.converge("docs/old.md", "old\ncontent\n")
        self.a.abs("docs/old.md").unlink()
        self.assertEqual(self.a.sync(force=True)["status"], "ok")
        self.assertFalse(self.remote_has("docs/old.md"))
        self.b.write("docs/old.md", "old\ncontent\nbob kept working on it\n")
        res = self.assertShape(self.b.sync(force=True))
        self.assertEqual(res["status"], "conflict-saved", res)
        self.assertEqual(res["saved_conflicts"], ["docs/old.md"])
        self.assertEqual(self.b.read("docs/old.md"), "old\ncontent\nbob kept working on it\n")
        self.assertEqual(self.fx.remote_show("docs/old.md"), "old\ncontent\nbob kept working on it\n")
        self.assertEqual(len(self.b.refs("refs/brain-backup/")), 1)
        actions = {d["path"]: d["action"] for d in res["conflict_details"]}
        self.assertIn("restored", actions["docs/old.md"])

    def test_delete_modify_local_deleted_remote_modified_keeps_remote(self):
        self.converge("docs/old2.md", "keep\nme\n")
        self.b.abs("docs/old2.md").unlink()
        self.a.write("docs/old2.md", "keep\nme\nalice improved it\n")
        self.assertEqual(self.a.sync(force=True)["status"], "ok")
        res = self.assertShape(self.b.sync(force=True))
        self.assertEqual(res["status"], "conflict-saved", res)
        self.assertEqual(res["saved_conflicts"], ["docs/old2.md"])
        self.assertEqual(self.b.read("docs/old2.md"), "keep\nme\nalice improved it\n")
        self.assertEqual(self.fx.remote_show("docs/old2.md"), "keep\nme\nalice improved it\n")
        self.assertEqual(len(self.b.refs("refs/brain-backup/")), 1)
        actions = {d["path"]: d["action"] for d in res["conflict_details"]}
        self.assertIn("kept-remote", actions["docs/old2.md"])

    def test_text_clash_outside_union_folders_is_union_merged_in_recovery(self):
        base = "# notes\nshared line\nthe contested line\nlast line\n"
        self.converge(".brain/notes.txt", base)
        self.b.write(".brain/notes.txt", base.replace("the contested line", "bob-edit"))
        self.a.write(".brain/notes.txt", base.replace("the contested line", "alice-edit"))
        self.assertEqual(self.a.sync(force=True)["status"], "ok")
        res = self.assertShape(self.b.sync(force=True))
        self.assertEqual(res["status"], "conflict-saved", res)
        text = self.b.read(".brain/notes.txt")
        self.assertIn("alice-edit", text)
        self.assertIn("bob-edit", text)
        self.assertIn("shared line", text)
        self.assertNotIn("<<<<", text)
        self.assertEqual(self.fx.remote_show(".brain/notes.txt"), text)
        self.assertEqual(res["saved_conflicts"], [".brain/notes.txt"])
        self.assertEqual(len(self.b.refs("refs/brain-backup/")), 1)

    def test_unrelated_local_changes_are_reapplied_after_a_clash(self):
        base = '{\n  "phase": "base"\n}\n'
        self.converge("docs/c.json", base)
        self.converge("docs/gone.md", "bye\n")
        self.b.write("docs/c.json", base.replace("base", "bob"))
        self.b.write("docs/b-only.md", "bob only\n")
        self.b.abs("docs/gone.md").unlink()
        self.a.write("docs/c.json", base.replace("base", "alice"))
        self.a.sync(force=True)
        res = self.b.sync(force=True)
        self.assertEqual(res["status"], "conflict-saved", res)
        self.assertEqual(res["saved_conflicts"], ["docs/c.json"])
        self.assertEqual(self.b.read("docs/b-only.md"), "bob only\n")
        self.assertFalse(self.b.exists("docs/gone.md"))
        self.assertIn("docs/b-only.md", self.fx.remote_files())
        self.assertNotIn("docs/gone.md", self.fx.remote_files())

    def test_unfinished_rebase_is_aborted_with_a_backup_before_syncing(self):
        base = '{\n  "phase": "base"\n}\n'
        self.converge("docs/c.json", base)
        self.b.write("docs/c.json", base.replace("base", "bob"))
        self.b.commit_pending()
        self.a.write("docs/c.json", base.replace("base", "alice"))
        self.a.sync(force=True)
        self.b.must_git("fetch", "-q", "origin")
        rb = self.b.git("rebase", "origin/main")
        self.assertFalse(rb.ok)
        gd = self.b.path / ".git"
        self.assertTrue((gd / "rebase-merge").exists() or (gd / "rebase-apply").exists())
        res = self.assertShape(self.b.sync(force=True))
        self.assertFalse((gd / "rebase-merge").exists() or (gd / "rebase-apply").exists())
        self.assertIn(res["status"], ("conflict-saved", "ok"))
        refs = self.b.refs("refs/brain-backup/")
        self.assertTrue(any(r.endswith("-aborted") for r in refs), refs)
        self.assertEqual(self.b.status()["in_progress"], False)
        self.assertEqual(self.b.read("docs/c.json"), base.replace("base", "alice"))

    # -- blocked local files must survive a pull ------------------------------
    def test_blocked_untracked_file_survives_a_pull_that_brings_the_same_path(self):
        secret_text = "token notes\n" + PW_LINE
        self.b.write("docs/clash.md", secret_text)
        self.assertEqual(self.b.commit_pending()["blocked"][0]["path"], "docs/clash.md")
        self.a.write("docs/clash.md", "remote version\n")
        self.a.sync(force=True)
        res = self.assertShape(self.b.pull(force=True))
        self.assertEqual(res["status"], "ok", res)
        self.assertEqual(self.b.read("docs/clash.md"), "remote version\n")
        kept = res["parked_conflicts"]
        self.assertEqual([k["path"] for k in kept], ["docs/clash.md"])
        self.assertEqual(Path(kept[0]["saved_to"]).read_text(encoding="utf-8"), secret_text)
        self.assertNotIn(secret_text, self.fx.remote_show("docs/clash.md"))

    def test_blocked_tracked_modification_survives_an_unrelated_pull(self):
        edited = "# NOW\n\nline one\n" + PW_LINE
        self.b.write("docs/NOW.md", edited)
        res = self.b.commit_pending()
        self.assertEqual([x["path"] for x in res["blocked"]], ["docs/NOW.md"])
        self.a.write("docs/STATUS.md", "# STATUS\n\nupdated\n")
        self.a.sync(force=True)
        res = self.b.sync(force=True)
        self.assertShape(res)
        self.assertEqual(res["status"], "ok", res)
        self.assertEqual(self.b.read("docs/NOW.md"), edited)  # still on disk, still modified
        self.assertEqual(self.b.read("docs/STATUS.md"), "# STATUS\n\nupdated\n")
        self.assertNotIn("password", self.fx.remote_show("docs/NOW.md"))
        self.assertEqual([x["path"] for x in res["blocked"]], ["docs/NOW.md"])

    def test_blocked_tracked_modification_is_preserved_when_remote_changed_it_too(self):
        edited = "# NOW\n\nline one\n" + PW_LINE
        self.b.write("docs/NOW.md", edited)
        self.b.commit_pending()
        self.a.write("docs/NOW.md", "# NOW\n\nalice rewrote it\n")
        self.a.sync(force=True)
        res = self.b.pull(force=True)
        self.assertEqual(res["status"], "ok", res)
        self.assertEqual(self.b.read("docs/NOW.md"), "# NOW\n\nalice rewrote it\n")
        kept = res["parked_conflicts"]
        self.assertEqual(Path(kept[0]["saved_to"]).read_text(encoding="utf-8"), edited)


# ----------------------------------------------------------------------------
class OfflineAndAuthTests(SyncCase):
    """Edge cases 4 and 5."""

    def fake_ssh_env(self, tmp: Path, mode: str, pidfile: Path | None = None) -> dict:
        script = tmp / "fake_ssh.py"
        script.write_text(FAKE_SSH, encoding="utf-8")
        cmd = f'"{Path(sys.executable).as_posix()}" "{script.as_posix()}"'
        env = {"GIT_SSH_COMMAND": cmd, "FAKE_SSH_MODE": mode}
        if pidfile:
            env["FAKE_SSH_PIDFILE"] = str(pidfile)
        return env

    def test_offline_missing_remote_then_push_later(self):
        good = str(self.fx.remote)
        self.a.set_remote_url(str(self.fx.root / "no-such-remote.git"))
        t0 = time.monotonic()
        res = self.assertShape(self.a.pull(force=True))
        self.assertEqual(res["status"], "offline", res)
        self.assertFalse(res["ok"])
        self.assertLess(time.monotonic() - t0, 8)
        self.assertEqual(self.a.state_json("sync")["status"], "offline")
        # work keeps going on the local copy
        rel = self.a.handover("written while offline")
        res = self.assertShape(self.a.sync(force=True))
        self.assertEqual(res["status"], "offline", res)
        self.assertEqual(res["committed"], [rel, rel[:-5] + ".md"])
        self.assertEqual(res["unpushed"], 1)
        self.assertFalse(res["pushed"])
        self.assertEqual(self.a.status()["unpushed"], 1)
        res = self.assertShape(self.a.push())
        self.assertEqual(res["status"], "offline", res)
        self.assertEqual(res["unpushed"], 1)
        self.assertNotIn(rel, self.fx.remote_files())
        # back online: the next sync pushes everything
        self.a.set_remote_url(good)
        res = self.assertShape(self.a.sync(force=True))
        self.assertEqual(res["status"], "ok", res)
        self.assertTrue(res["pushed"])
        self.assertEqual(res["unpushed"], 0)
        self.assertIn(rel, self.fx.remote_files())
        self.assertEqual(self.b.pull(force=True)["changed_files"], [rel, rel[:-5] + ".md"])

    def test_offline_unreachable_http_remote_is_fast(self):
        self.a.set_remote_url("http://127.0.0.1:9/x.git")
        self.a.handover("so that there is something to push")
        t0 = time.monotonic()
        res = self.assertShape(self.a.sync(force=True, timeout=6))
        self.assertEqual(res["status"], "offline", res)
        self.assertLess(time.monotonic() - t0, 15)
        res = self.a.push(timeout=6)
        self.assertEqual(res["status"], "offline", res)

    def test_auth_failure_is_reported_never_hangs(self):
        tmp = self.fx.root
        env = self.fake_ssh_env(tmp, "deny")
        self.a.set_remote_url("ssh://git@example.invalid/mockmob-brain.git")
        rel = self.a.handover("written while signed out")
        t0 = time.monotonic()
        with self.a.active(**env):
            pulled = sync.pull(force=True, timeout=8)
            pushed = sync.push(timeout=8)
            synced = sync.sync(force=True, timeout=8)
        self.assertLess(time.monotonic() - t0, 30)
        for res in (pulled, pushed, synced):
            self.assertShape(res)
            self.assertEqual(res["status"], "auth", res)
            self.assertFalse(res["ok"])
            self.assertIn("sign", res["message"].lower())
        self.assertEqual(synced["unpushed"], 1)
        self.assertEqual(self.a.state_json("sync")["status"], "auth")
        self.assertTrue(self.a.exists(rel))
        self.assertTrue(self.a.log_subjects(1)[0].startswith("brain: written while signed out"))

    def test_hanging_remote_times_out_and_the_process_tree_is_killed(self):
        pidfile = self.fx.root / "ssh.pid"
        env = self.fake_ssh_env(self.fx.root, "hang", pidfile)
        self.a.set_remote_url("ssh://git@example.invalid/mockmob-brain.git")
        t0 = time.monotonic()
        with self.a.active(**env):
            res = sync.pull(force=True, timeout=2)
        self.assertLess(time.monotonic() - t0, 20)
        self.assertShape(res)
        self.assertEqual(res["status"], "offline", res)
        if pidfile.exists():
            pid = int(pidfile.read_text())
            for _ in range(30):
                if not pid_alive(pid):
                    break
                time.sleep(0.2)
            self.assertFalse(pid_alive(pid), "the hung ssh process was left running")

    def test_gitops_run_kills_on_timeout(self):
        pidfile = self.fx.root / "ssh2.pid"
        env = self.fake_ssh_env(self.fx.root, "hang", pidfile)
        t0 = time.monotonic()
        r = gitops.run(["ls-remote", "ssh://git@example.invalid/x.git"], cwd=self.a.path, timeout=2, env=env)
        self.assertTrue(r.timed_out)
        self.assertEqual(gitops.classify(r), "offline")
        self.assertLess(time.monotonic() - t0, 20)

    def test_gitops_environment_never_prompts(self):
        env = gitops.build_env()
        self.assertEqual(env["GIT_TERMINAL_PROMPT"], "0")
        self.assertEqual(env["GCM_INTERACTIVE"], "Never")
        self.assertEqual(env["GIT_ASKPASS"], "")
        self.assertEqual(env["LC_ALL"], "C")
        self.assertEqual(env["GIT_EDITOR"], "true")
        r = gitops.run(["--version"], cwd=self.a.path, timeout=20)
        self.assertTrue(r.ok)
        self.assertTrue(r.out.startswith("git version"))
        r = gitops.run(["no-such-subcommand"], cwd=self.a.path, timeout=20)
        self.assertFalse(r.ok)  # a failing command returns, it does not raise

    def test_classifier_on_captured_stderr(self):
        gh = "https://github.com/atishay07/mockmob-brain.git"
        cases = [
            ("remote: Invalid username or password.\nfatal: Authentication failed for 'https://github.com/x/y.git/'", gh, "auth"),
            ("fatal: could not read Username for 'https://github.com': terminal prompts disabled", gh, "auth"),
            ("fatal: unable to access 'https://github.com/x/y.git/': The requested URL returned error: 403", gh, "auth"),
            ("remote: Repository not found.\nfatal: repository 'https://github.com/atishay07/mockmob-brain.git/' not found", gh, "auth"),
            ("git@github.com: Permission denied (publickey).\nfatal: Could not read from remote repository.", "git@github.com:a/b.git", "auth"),
            ("remote: Repository not found.\nfatal: repository 'https://git.example.org/x.git/' not found", "https://git.example.org/x.git", "error"),
            ("fatal: unable to access 'https://github.com/x/y.git/': Could not resolve host: github.com", gh, "offline"),
            ("fatal: unable to access 'https://github.com/x/y.git/': Failed to connect to github.com port 443 after 21038 ms: Couldn't connect to server", gh, "offline"),
            ("ssh: connect to host github.com port 22: Network is unreachable", gh, "offline"),
            ("ssh: connect to host github.com port 22: Connection timed out\nfatal: Could not read from remote repository.", gh, "offline"),
            ("fatal: unable to access 'https://x/': Recv failure: Connection reset by peer", gh, "offline"),
            ("fatal: unable to access 'http://127.0.0.1:9/x.git/': Failed to connect to 127.0.0.1 port 9: Connection refused", "", "offline"),
            ("fatal: '/nonexistent/remote.git' does not appear to be a git repository\nfatal: Could not read from remote repository.", "/nonexistent/remote.git", "offline"),
            ("fatal: Temporary failure in name resolution", gh, "offline"),
            (" ! [rejected]        HEAD -> main (non-fast-forward)\nerror: failed to push some refs", gh, "error"),
            ("fatal: refusing to merge unrelated histories", gh, "error"),
            ("", gh, "error"),
        ]
        for text, url, want in cases:
            self.assertEqual(gitops.classify(text, url), want, text)
        self.assertEqual(gitops.classify(gitops.Result(0, "", "")), "ok")
        self.assertEqual(gitops.classify(gitops.Result(124, "", "", True)), "offline")
        self.assertEqual(gitops.classify(gitops.Result(128, "", "Could not resolve host: x")), "offline")
        self.assertEqual(gitops.Result(128, "", "Authentication failed").kind(), "auth")
        self.assertTrue(gitops.is_non_fast_forward(" ! [rejected] main -> main (fetch first)"))
        self.assertFalse(gitops.is_non_fast_forward("fatal: Authentication failed"))


# ----------------------------------------------------------------------------
class ConcurrencyTests(SyncCase):
    """Edge case 6."""

    def assert_no_index_lock_trouble(self, results):
        for r in results:
            self.assertNotIn("index.lock", json.dumps(r), r)
            self.assertNotIn("Unable to create", json.dumps(r), r)
        log = self.a.state_dir / "logs" / "sync.log"
        if log.exists():
            self.assertNotIn("index.lock", log.read_text(encoding="utf-8", errors="replace"))

    def test_ten_threads_nonblocking(self):
        rel = self.a.handover("ten threads")
        results: list = []
        guard = threading.Lock()
        barrier = threading.Barrier(10)

        def worker():
            barrier.wait()
            r = sync.sync(force=True, lock_timeout=0)
            with guard:
                results.append(r)

        with self.a.active():
            threads = [threading.Thread(target=worker) for _ in range(10)]
            [t.start() for t in threads]
            [t.join(180) for t in threads]
        self.assertEqual(len(results), 10)
        for r in results:
            self.assertShape(r)
            self.assertIn(r["status"], ("ok", "skipped", "locked"), r)
        self.assertGreaterEqual(sum(1 for r in results if r["status"] != "locked"), 1)
        self.assert_no_index_lock_trouble(results)
        self.assertIn(rel, self.fx.remote_files())
        self.assertEqual(self.a.must_git("status", "--porcelain").strip(), "")
        self.assertEqual(self.a.status()["unpushed"], 0)
        self.assertFalse(FileLock(self.a.state_dir / "locks" / "git.lock").holder())

    def test_ten_threads_blocking_all_complete_in_turn(self):
        rel = self.a.handover("ten blocking threads")
        results: list = []
        guard = threading.Lock()
        barrier = threading.Barrier(10)

        def worker():
            barrier.wait()
            r = sync.sync(force=True, lock_timeout=120)
            with guard:
                results.append(r)

        with self.a.active():
            threads = [threading.Thread(target=worker) for _ in range(10)]
            [t.start() for t in threads]
            [t.join(300) for t in threads]
        self.assertEqual(len(results), 10)
        for r in results:
            self.assertIn(r["status"], ("ok", "skipped"), r)
        self.assertEqual(sum(1 for r in results if r["pushed"]), 1)
        self.assert_no_index_lock_trouble(results)
        self.assertIn(rel, self.fx.remote_files())
        self.assertEqual(self.a.must_git("status", "--porcelain").strip(), "")
        self.assertEqual(self.fx.remote_commit_count(), 2)  # initial + one handover commit

    def test_mixed_operations_from_many_threads(self):
        rels = [self.a.handover(f"mixed {i}", f"20261106T1100{i:02d}.000000Z") for i in range(3)]
        results: list = []
        guard = threading.Lock()
        ops = [
            lambda: sync.sync(force=True, lock_timeout=60),
            lambda: sync.sync(force=True, lock_timeout=60),
            lambda: sync.pull(force=True, lock_timeout=60),
            lambda: sync.push(lock_timeout=60),
            lambda: sync.push(lock_timeout=60),
            lambda: sync.commit_pending(lock_timeout=60),
            lambda: sync.commit_pending(lock_timeout=60),
            lambda: sync.status(),
            lambda: sync.sync(lock_timeout=0),
            lambda: sync.pull(lock_timeout=0),
        ]
        random.shuffle(ops)

        def worker(op):
            r = op()
            with guard:
                results.append(r)

        with self.a.active():
            threads = [threading.Thread(target=worker, args=(op,)) for op in ops]
            [t.start() for t in threads]
            [t.join(300) for t in threads]
        self.assertEqual(len(results), 10)
        for r in results:
            self.assertShape(r)
            self.assertIn(r["status"], ("ok", "skipped", "locked"), r)
        self.assert_no_index_lock_trouble(results)
        self.a.sync(force=True)
        for rel in rels:
            self.assertIn(rel, self.fx.remote_files())
        self.assertEqual(self.a.must_git("status", "--porcelain").strip(), "")

    def test_concurrent_processes_on_one_clone(self):
        rel = self.a.handover("process swarm")
        procs = [self.sync_in_subprocess(self.a, force=True, lock_timeout=60) for _ in range(4)]
        results = [self.parse_result(p) for p in procs]
        for r in results:
            self.assertIn(r["status"], ("ok", "skipped"), r)
        self.assert_no_index_lock_trouble(results)
        self.assertIn(rel, self.fx.remote_files())
        self.assertEqual(self.fx.remote_commit_count(), 2)

    def test_processes_with_zero_lock_timeout_return_locked_or_finish(self):
        self.a.handover("zero timeout swarm")
        procs = [self.sync_in_subprocess(self.a, force=True, lock_timeout=0) for _ in range(4)]
        results = [self.parse_result(p) for p in procs]
        for r in results:
            self.assertIn(r["status"], ("ok", "skipped", "locked"), r)
        self.assert_no_index_lock_trouble(results)
        self.a.sync(force=True)
        self.assertEqual(self.a.status()["unpushed"], 0)


# ----------------------------------------------------------------------------
class SafetyInSyncTests(SyncCase):
    """Edge cases 8, 9, 10 and 13: blocked files stay on disk and never reach git."""

    def blocked_map(self, res):
        return {b["path"]: b for b in res["blocked"]}

    def test_secret_in_a_doc_is_blocked_kept_and_flagged_with_its_line(self):
        secret = secret_sample()
        text = f"# notes\n\nsome words\nthe key is {secret} do not share\nend\n"
        self.a.write("docs/leaky.md", text)
        self.a.write("docs/clean.md", "all fine\n")
        res = self.assertShape(self.a.sync(force=True))
        self.assertEqual(res["status"], "ok", res)
        b = self.blocked_map(res)["docs/leaky.md"]
        self.assertEqual(b["line"], 4)
        self.assertIn("secret", b["reason"])
        self.assertEqual(self.a.read("docs/leaky.md"), text)  # never deleted or altered
        self.assertNotIn("docs/leaky.md", self.a.tracked())
        self.assertNotIn("docs/leaky.md", self.fx.remote_files())
        self.assertIn("docs/clean.md", self.fx.remote_files())
        # the secret is nowhere in history, results, state or the log
        self.assertEqual(self.a.must_git("log", "--all", "-S" + secret, "--format=%H").strip(), "")
        self.assertEqual(self.fx.remote_git("log", "--all", "-S" + secret, "--format=%H").out.strip(), "")
        self.assertNotIn(secret, json.dumps(res))
        self.assertNotIn(secret, json.dumps(self.a.state_json("blocked")))
        log = self.a.state_dir / "logs" / "sync.log"
        if log.exists():
            self.assertNotIn(secret, log.read_text(encoding="utf-8", errors="replace"))
        st = self.a.status()
        self.assertEqual([x["path"] for x in st["blocked"]], ["docs/leaky.md"])
        self.assertEqual(self.a.state_json("blocked")["files"][0]["line"], 4)

    def test_fixing_a_blocked_file_unblocks_it(self):
        self.a.write("docs/leaky.md", "a\nb\n" + PW_LINE)
        self.assertEqual(len(self.a.commit_pending()["blocked"]), 1)
        self.a.write("docs/leaky.md", "a\nb\npassword = [REDACTED]\n")
        res = self.a.commit_pending()
        self.assertEqual(res["blocked"], [])
        self.assertEqual(res["committed"], ["docs/leaky.md"])
        self.assertEqual(self.a.state_json("blocked")["files"], [])
        self.assertEqual(self.a.status()["blocked"], [])

    def test_blocked_file_that_disappears_leaves_the_list(self):
        self.a.write("docs/leaky.md", PW_LINE)
        self.a.commit_pending()
        self.a.abs("docs/leaky.md").unlink()
        self.assertEqual(self.a.commit_pending()["blocked"], [])
        self.assertEqual(self.a.state_json("blocked")["files"], [])

    def test_secret_added_to_a_tracked_file_is_not_committed(self):
        self.a.write("docs/NOW.md", "# NOW\n\nline one\n" + API_LINE)
        res = self.a.sync(force=True)
        self.assertEqual([b["path"] for b in res["blocked"]], ["docs/NOW.md"])
        self.assertNotIn("api_key", self.fx.remote_show("docs/NOW.md"))
        self.assertIn("api_key", self.a.read("docs/NOW.md"))

    def test_big_files_and_binaries_are_blocked(self):
        self.a.write("docs/big.md", ("line of text\n" * 300000)[: 3 * 1024 * 1024])
        self.a.write("docs/blob.bin", b"abc\0\1\2\3 binary")
        self.a.write("docs/latin1.md", b"caf\xe9 not utf8")
        self.a.write("context/pic.png", b"\x89PNG\r\n\x1a\n" + b"\0" * 100)
        self.a.write("docs/huge.png", b"\x89PNG\r\n\x1a\n" + b"\0" * (3 * 1024 * 1024))
        self.a.write("docs/small.png", b"\x89PNG\r\n\x1a\n" + b"\0" * 100)
        self.a.write("docs/small.webp", b"RIFF\0\0\0\0WEBPVP8 " + b"\0" * 100)
        self.a.write("docs/fine.md", "fine\n")
        res = self.assertShape(self.a.sync(force=True))
        blocked = self.blocked_map(res)
        self.assertEqual(
            sorted(blocked), ["context/pic.png", "docs/big.md", "docs/blob.bin", "docs/huge.png", "docs/latin1.md"]
        )
        self.assertIn("too large", blocked["docs/big.md"]["reason"])
        self.assertIn("too large", blocked["docs/huge.png"]["reason"])
        self.assertIn("binary", blocked["docs/blob.bin"]["reason"])
        self.assertIn("UTF-8", blocked["docs/latin1.md"]["reason"])
        files = self.fx.remote_files()
        for ok in ("docs/small.png", "docs/small.webp", "docs/fine.md"):
            self.assertIn(ok, files)
        for bad in blocked:
            self.assertNotIn(bad, files)
            self.assertTrue(self.a.exists(bad), f"{bad} must stay on disk")

    def test_path_too_long_is_blocked(self):
        rel = "docs/" + "x" * 60 + "/" + "y" * 60 + "/" + "z" * 52 + ".md"
        self.assertGreater(len(rel), 180)
        self.a.write(rel, "deep\n")
        res = self.assertShape(self.a.sync(force=True))
        self.assertIn("too long", self.blocked_map(res)[rel]["reason"])
        self.assertTrue(self.a.exists(rel))
        self.assertNotIn(rel, self.fx.remote_files())

    @unittest.skipIf(os.name == "nt", "Windows cannot create files with reserved names or these characters")
    def test_reserved_names_and_bad_characters_are_blocked(self):
        for rel in ("docs/con.md", "docs/aux/notes.md", "docs/a:b.md", "docs/q?.md", "docs/trailing."):
            self.a.write(rel, "x\n")
        res = self.assertShape(self.a.sync(force=True))
        blocked = self.blocked_map(res)
        for rel in ("docs/con.md", "docs/aux/notes.md", "docs/a:b.md", "docs/q?.md", "docs/trailing."):
            self.assertIn(rel, blocked)
            self.assertTrue(self.a.exists(rel))
            self.assertNotIn(rel, self.fx.remote_files())

    def test_reserved_names_are_blocked_in_the_commit_pipeline(self):
        """Same rule as above, driven through git status on every OS by faking the status entry."""
        seen = []
        real = safety.check_path

        def spy(rel, tracked=None, repo=None):
            reasons = real(rel, tracked=tracked, repo=repo)
            seen.append((rel, reasons))
            return reasons

        self.a.write("docs/fine.md", "fine\n")
        safety.check_path = spy
        try:
            self.a.commit_pending()
        finally:
            safety.check_path = real
        self.assertEqual(seen, [("docs/fine.md", [])])
        self.assertTrue(real("docs/con.md", tracked=[]))

    @unittest.skipUnless(os.name != "nt", "needs a case-sensitive file system with creatable odd names")
    def test_case_only_collision_is_blocked(self):
        if not fs_is_case_sensitive(self.a.path):
            self.skipTest("case-insensitive file system")
        self.a.write("docs/now.md", "lower\n")  # docs/NOW.md is tracked
        res = self.a.sync(force=True)
        self.assertIn("case-only", self.blocked_map(res)["docs/now.md"]["reason"])
        self.assertNotIn("docs/now.md", self.fx.remote_files())
        self.assertTrue(self.a.exists("docs/now.md"))

    def test_broken_python_in_dot_brain_is_blocked_and_never_pushed(self):
        self.a.write(".brain/brainlib/broken.py", "def x(:\n    pass\n")
        self.a.write(".brain/brainlib/good.py", "def x():\n    return 1\n")
        self.a.write("docs/example.py", "def not_checked(:\n")  # outside .brain/: not compiled
        res = self.assertShape(self.a.sync(force=True))
        blocked = self.blocked_map(res)
        self.assertEqual(list(blocked), [".brain/brainlib/broken.py"])
        self.assertIn("py_compile", blocked[".brain/brainlib/broken.py"]["reason"])
        self.assertEqual(blocked[".brain/brainlib/broken.py"]["line"], 1)
        files = self.fx.remote_files()
        self.assertNotIn(".brain/brainlib/broken.py", files)
        self.assertIn(".brain/brainlib/good.py", files)
        self.assertIn("docs/example.py", files)
        self.assertTrue(self.a.exists(".brain/brainlib/broken.py"))
        self.assertEqual(self.a.must_git("log", "--all", "--format=%H", "--", ".brain/brainlib/broken.py").strip(), "")
        # fixing it releases it
        self.a.write(".brain/brainlib/broken.py", "def x():\n    pass\n")
        res = self.a.sync(force=True)
        self.assertEqual(res["blocked"], [])
        self.assertIn(".brain/brainlib/broken.py", self.fx.remote_files())

    def test_a_broken_edit_to_a_tracked_dot_brain_file_is_not_pushed(self):
        self.a.write(".brain/hook.py", "print('v1')\n")
        self.a.sync(force=True)
        self.a.write(".brain/hook.py", "print('v2'\n")  # missing paren
        res = self.a.sync(force=True)
        self.assertEqual([b["path"] for b in res["blocked"]], [".brain/hook.py"])
        self.assertEqual(self.fx.remote_show(".brain/hook.py").strip(), "print('v1')")

    def test_blocked_files_do_not_stop_good_files(self):
        self.a.write("docs/leaky.md", PW_LINE)
        rel = self.a.handover("good one")
        res = self.a.sync(force=True)
        self.assertEqual(res["status"], "ok")
        self.assertIn(rel, self.fx.remote_files())
        self.assertEqual(len(res["blocked"]), 1)

    def test_check_path_against_the_live_repo(self):
        self.assertTrue(safety.check_path("docs/now.md", repo=self.a.path))
        self.assertEqual(safety.check_path("docs/NOW.md", repo=self.a.path), [])


# ----------------------------------------------------------------------------
class GitCallBudgetTests(SyncCase):
    """Each git subprocess costs 0.15-0.4 s on Windows, so the common paths must stay cheap."""

    def counted(self, fn):
        calls = []
        real = gitops.run

        def counting(args, cwd, timeout=30, **kw):
            calls.append(" ".join(str(a) for a in args))
            return real(args, cwd, timeout, **kw)

        gitops.run = counting
        try:
            res = fn()
        finally:
            gitops.run = real
        return res, calls

    def setUp(self):
        super().setUp()
        self.a.sync(force=True)  # everything pushed, tree clean

    def test_commit_pending_on_a_clean_tree_is_one_git_call(self):
        res, calls = self.counted(self.a.commit_pending)
        self.assertEqual(res["status"], "ok")
        self.assertEqual(len(calls), 1, calls)
        self.assertIn("status", calls[0])
        self.assertEqual(res["unpushed"], 0)

    def test_pull_on_a_clean_tree_with_nothing_new_is_at_most_four_calls(self):
        res, calls = self.counted(lambda: self.a.pull(force=True))
        self.assertEqual(res["status"], "ok", res)
        self.assertLessEqual(len(calls), 4, calls)
        self.assertEqual([c.split()[0] for c in calls], ["--no-optional-locks", "fetch"])  # status + fetch
        self.assertEqual((res["changed_files"], res["unpushed"]), ([], 0))

    def test_pull_on_a_clean_tree_with_new_remote_commits_is_at_most_seven_calls(self):
        self.b.sync(force=True)
        self.b.write("docs/NOW.md", "# NOW\n\nchanged by bob\n")
        self.b.handover("bob again")
        self.assertEqual(self.b.sync(force=True)["status"], "ok")
        res, calls = self.counted(lambda: self.a.pull(force=True))
        self.assertEqual(res["status"], "ok", res)
        self.assertLessEqual(len(calls), 7, calls)
        self.assertIn("docs/NOW.md", res["changed_files"])
        self.assertEqual(self.a.read("docs/NOW.md"), "# NOW\n\nchanged by bob\n")
        self.assertEqual(res["unpushed"], 0)

    def test_sync_with_nothing_to_do_is_cheap(self):
        res, calls = self.counted(lambda: self.a.sync(force=True))
        self.assertEqual(res["status"], "ok", res)
        self.assertLessEqual(len(calls), 4, calls)
        res, calls = self.counted(lambda: self.a.sync())  # inside the throttle window
        self.assertEqual(res["status"], "skipped", res)
        self.assertLessEqual(len(calls), 2, calls)

    def test_status_is_one_git_call(self):
        res, calls = self.counted(self.a.status)
        self.assertEqual(res["status"], "ok")
        self.assertLessEqual(len(calls), 2, calls)

    def test_throttled_pull_spawns_no_git_at_all(self):
        res, calls = self.counted(lambda: self.a.pull(min_interval=60))
        self.assertEqual(res["status"], "skipped")
        self.assertEqual(calls, [])

    def test_commit_with_a_pending_file_stays_small(self):
        self.a.handover("one pending handover")
        res, calls = self.counted(lambda: self.a.sync(force=True))
        self.assertEqual((res["status"], res["pushed"]), ("ok", True), res)
        self.assertLessEqual(len(calls), 10, calls)

    def test_offline_pull_fails_fast_and_cheaply(self):
        self.a.set_remote_url(str(self.fx.root / "gone.git"))
        res, calls = self.counted(lambda: self.a.pull(force=True))
        self.assertEqual(res["status"], "offline")
        self.assertLessEqual(len(calls), 3, calls)


class SpawnTests(SyncCase):
    n_clones = 1

    def setUp(self):
        super().setUp()
        self.script = self.fx.root / "standin.py"
        self.script.write_text(
            "import sys, time, pathlib\n"
            f"pathlib.Path({str(self.fx.root / 'argv.json')!r}).write_text(__import__('json').dumps(sys.argv[1:]))\n"
            "time.sleep(float(__import__('os').environ.get('STANDIN_SLEEP', '2.5')))\n",
            encoding="utf-8",
        )
        self.addCleanup(self.wait_for_children)  # runs before the fixture cleanup (LIFO)

    def wait_for_children(self):
        pidfile = self.a.state_dir / "locks" / "bg-sync.pid"
        deadline = time.time() + 20
        while time.time() < deadline:
            try:
                pid = json.loads(pidfile.read_text())["pid"]
            except (OSError, ValueError, KeyError):
                return
            if not pid_alive(pid):
                return
            time.sleep(0.2)

    def test_spawn_does_not_block_writes_pidfile_and_refuses_a_second(self):
        with self.a.active():
            t0 = time.monotonic()
            self.assertTrue(sync.spawn_background("test-reason", _script=self.script))
            self.assertLess(time.monotonic() - t0, 2.0)  # the stand-in sleeps 2.5 s
            pidfile = self.a.state_dir / "locks" / "bg-sync.pid"
            self.assertTrue(pidfile.exists())
            pid = json.loads(pidfile.read_text())["pid"]
            self.assertTrue(pid_alive(pid))
            t1 = time.monotonic()
            self.assertFalse(sync.spawn_background("second", _script=self.script))
            self.assertLess(time.monotonic() - t1, 1.5)
            for _ in range(100):
                if not pid_alive(pid):
                    break
                time.sleep(0.1)
            self.assertFalse(pid_alive(pid))
            argv = json.loads((self.fx.root / "argv.json").read_text())
            self.assertEqual(argv, ["sync", "--quiet", "--reason", "test-reason"])
            # the first one finished: a new one may start
            os.environ["STANDIN_SLEEP"] = "0.2"
            try:
                self.assertTrue(sync.spawn_background("third", _script=self.script))
            finally:
                os.environ.pop("STANDIN_SLEEP", None)

    def test_spawn_returns_false_when_the_script_is_missing(self):
        with self.a.active():
            self.assertFalse(sync.spawn_background("x", _script=self.fx.root / "nope.py"))
            self.assertFalse(sync.spawn_background("x"))  # no .brain/brain.py in the temp clone

    def test_stale_pidfile_does_not_block_a_spawn(self):
        pidfile = self.a.state_dir / "locks" / "bg-sync.pid"
        pidfile.parent.mkdir(parents=True, exist_ok=True)
        p = subprocess.Popen([sys.executable, "-c", "pass"])
        p.wait()
        pidfile.write_text(json.dumps({"pid": p.pid, "at": time.time()}))
        os.environ["STANDIN_SLEEP"] = "0.2"
        try:
            with self.a.active():
                self.assertTrue(sync.spawn_background("after-crash", _script=self.script))
        finally:
            os.environ.pop("STANDIN_SLEEP", None)

    def test_old_pidfile_of_a_reused_pid_does_not_block_forever(self):
        pidfile = self.a.state_dir / "locks" / "bg-sync.pid"
        pidfile.parent.mkdir(parents=True, exist_ok=True)
        pidfile.write_text(json.dumps({"pid": os.getpid(), "at": time.time() - 3600}))  # alive pid, ancient
        os.environ["STANDIN_SLEEP"] = "0.2"
        try:
            with self.a.active():
                self.assertTrue(sync.spawn_background("old", _script=self.script))
        finally:
            os.environ.pop("STANDIN_SLEEP", None)


class ConfigAndStateTests(unittest.TestCase):
    def setUp(self):
        import tempfile

        self.tmp = Path(tempfile.mkdtemp(prefix="mmb-cfg-"))
        self.addCleanup(gf.rmtree_force, self.tmp)
        self.saved = {k: os.environ.get(k) for k in ("MOCKMOB_BRAIN_STATE", "MOCKMOB_BRAIN")}
        os.environ["MOCKMOB_BRAIN_STATE"] = str(self.tmp / "state")
        os.environ.pop("MOCKMOB_BRAIN", None)
        self.addCleanup(self.restore_env)

    def restore_env(self):
        for k, v in self.saved.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v

    def test_state_dir_follows_the_environment(self):
        self.assertEqual(config.STATE_DIR, self.tmp / "state")
        os.environ["MOCKMOB_BRAIN_STATE"] = str(self.tmp / "other")
        self.assertEqual(config.state_dir(), self.tmp / "other")
        p = config.state_path("locks", "x.lock")
        self.assertTrue(p.parent.is_dir())

    def test_missing_config_gives_defaults(self):
        cfg = config.load()
        self.assertEqual((cfg.mode, cfg.branch, cfg.remote), ("standalone", "main", "origin"))
        self.assertTrue(cfg.person)
        self.assertTrue((cfg.brain_dir / ".brain" / "brainlib").is_dir())

    def test_env_brain_wins_over_config(self):
        cfg = config.load()
        cfg.brain_dir = self.tmp / "from-config"
        config.save(cfg)
        self.assertEqual(config.load().brain_dir, self.tmp / "from-config")
        os.environ["MOCKMOB_BRAIN"] = str(self.tmp / "from-env")
        self.assertEqual(config.load().brain_dir, self.tmp / "from-env")

    def test_save_load_roundtrip_and_extra_keys_survive(self):
        cfg = config.Config(person="zed", display_name="Zed", role="cto", email="z@example.test",
                            brain_dir=self.tmp / "b", code_dirs=[self.tmp / "code"], memory_dirs=[self.tmp / "mem"],
                            mode="bridge", vectors=False, python=sys.executable)
        cfg.extra["future_key"] = 7
        config.save(cfg)
        again = config.load()
        self.assertEqual((again.person, again.role, again.mode, again.vectors), ("zed", "cto", "bridge", False))
        self.assertEqual(again.code_dirs, [self.tmp / "code"])
        self.assertEqual(again.extra["future_key"], 7)

    def test_state_read_write_atomic(self):
        from brainlib import state

        self.assertEqual(state.read("nothing"), {})
        self.assertEqual(state.read("nothing", {"a": 1}), {"a": 1})
        state.write("sync", {"x": [1, 2, 3]})
        self.assertEqual(state.read("sync"), {"x": [1, 2, 3]})
        self.assertEqual(state.read("sync.json"), {"x": [1, 2, 3]})
        (config.state_dir() / "state" / "bad.json").write_text("{not json")
        self.assertEqual(state.read("bad"), {})
        leftovers = [p.name for p in (config.state_dir() / "state").iterdir() if ".tmp-" in p.name]
        self.assertEqual(leftovers, [])

    def test_state_writes_from_threads_never_corrupt(self):
        from brainlib import state

        def w(i):
            for j in range(20):
                state.write("race", {"i": i, "j": j, "pad": "x" * 500})

        ts = [threading.Thread(target=w, args=(i,)) for i in range(6)]
        [t.start() for t in ts]
        [t.join(60) for t in ts]
        d = state.read("race")
        self.assertEqual(len(d["pad"]), 500)

    def test_is_mockmob_cwd(self):
        brain = self.tmp / "brain"
        code = self.tmp / "code" / "mockmob"
        other = self.tmp / "elsewhere"
        for d in (brain / "docs", code / "app", other):
            d.mkdir(parents=True)
        cfg = config.Config(brain_dir=brain, code_dirs=[code])
        self.assertTrue(config.is_mockmob_cwd(brain, cfg))
        self.assertTrue(config.is_mockmob_cwd(brain / "docs", cfg))
        self.assertTrue(config.is_mockmob_cwd(code / "app", cfg))
        self.assertTrue(config.is_mockmob_cwd(str(code / "app").replace("\\", "/"), cfg))
        self.assertFalse(config.is_mockmob_cwd(other, cfg))
        self.assertFalse(config.is_mockmob_cwd("", cfg))
        if os.name == "nt":
            self.assertTrue(config.is_mockmob_cwd(str(code).upper(), cfg))

    def test_is_mockmob_cwd_by_origin_url(self):
        def make_repo(name, url):
            d = self.tmp / name
            (d / ".git").mkdir(parents=True)
            (d / ".git" / "config").write_text(f'[core]\n\tbare = false\n[remote "origin"]\n\turl = {url}\n')
            (d / "sub").mkdir()
            return d

        cfg = config.Config(brain_dir=self.tmp / "brain", code_dirs=[])
        code = make_repo("somewhere", "https://github.com/atishay07/mockmob.git")
        brainish = make_repo("somebrain", "https://github.com/atishay07/mockmob-brain.git")
        other = make_repo("unrelated", "https://github.com/someone/else.git")
        self.assertTrue(config.is_mockmob_cwd(code / "sub", cfg))
        self.assertFalse(config.is_mockmob_cwd(brainish / "sub", cfg))
        self.assertFalse(config.is_mockmob_cwd(other / "sub", cfg))
        cache = json.loads((config.state_dir() / "state" / "cwd-cache.json").read_text())
        self.assertTrue(len(cache) >= 3)
        (code / ".git" / "HEAD").write_text("0123456789abcdef0123456789abcdef01234567" + chr(10))
        self.assertEqual(config.repo_relative(code / "sub" / "file.txt"), ("mockmob", "HEAD", "sub/file.txt"))
        (code / ".git" / "HEAD").write_text("ref: refs/heads/feature/x\n")
        self.assertEqual(config.repo_relative(code / "sub" / "new" / "file.txt"), ("mockmob", "feature/x", "sub/new/file.txt"))
        self.assertIsNone(config.repo_relative(other / "sub" / "file.txt"))


if __name__ == "__main__":
    unittest.main()
