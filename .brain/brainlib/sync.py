"""Git sync core for the MockMob team brain (DESIGN.md sections 4 and 5).

Public API: ``commit_pending``, ``pull``, ``push``, ``sync``, ``spawn_background``,
``status``. Every function returns a result dict (see :func:`_result`) and never
raises. All git work goes through :mod:`gitops` under the ``locks/git.lock``
:class:`~lock.FileLock`; files that fail the safety checks stay on disk and are
reported in ``blocked``.
"""
from __future__ import annotations

import json
import os
import random
import re
import shutil
import subprocess
import sys
import tempfile
import time
import traceback
from datetime import datetime, timedelta, timezone
from pathlib import Path, PurePosixPath
from typing import Iterable

from . import config, gitops, safety, state
from .lock import FileLock, pid_alive

OK_STATUSES = ("ok", "skipped", "conflict-saved")
STALE_CLAIM_HOURS = 3
MERGED_KEEP_DAYS = 7
TEXT_EXTS = (".md", ".txt")
LOCAL_TIMEOUT = 30
REBASE_TIMEOUT = 90

__all__ = [
    "commit_pending", "pull", "push", "sync", "spawn_background", "status",
    "clear_merged",
]


# --------------------------------------------------------------------------
# small helpers
# --------------------------------------------------------------------------
def _now() -> datetime:
    return datetime.now(timezone.utc)


def _iso(dt: datetime | None = None) -> str:
    return (dt or _now()).strftime("%Y-%m-%dT%H:%M:%SZ")


def _parse_iso(text) -> datetime | None:
    if not text or not isinstance(text, str):
        return None
    try:
        return datetime.fromisoformat(text.strip().replace("Z", "+00:00")).astimezone(timezone.utc)
    except ValueError:
        return None


def _stamp() -> str:
    return _now().strftime("%Y%m%dT%H%M%SZ")


def _split_z(text: str) -> list[str]:
    return [p for p in text.split("\0") if p]


def _result(status: str = "ok", message: str = "", ok: bool | None = None, **extra) -> dict:
    r = {
        "ok": (status in OK_STATUSES) if ok is None else ok,
        "status": status,
        "message": message,
        "changed_files": [],
        "committed": [],
        "pushed": False,
        "unpushed": 0,
        "blocked": [],
        "merged_both_sides": [],
        "saved_conflicts": [],
        "head": "",
        "at": _iso(),
    }
    r.update(extra)
    return r


def _log(line: str) -> None:
    try:
        p = config.state_path("logs", "sync.log")
        try:
            if p.exists() and p.stat().st_size > 1_000_000:
                old1, old2 = p.with_name("sync.log.1"), p.with_name("sync.log.2")
                if old1.exists():
                    os.replace(old1, old2)
                os.replace(p, old1)
        except OSError:
            pass  # Windows: a background sync still holds the file open
        with open(p, "a", encoding="utf-8", errors="replace") as f:
            f.write(f"{_iso()} [{os.getpid()}] {line}\n")
    except Exception:
        pass


def _safe_state_write(name: str, data) -> None:
    try:
        state.write(name, data)
    except Exception as e:  # never let a state file break a sync
        _log(f"state write {name} failed: {e}")


_UNSET = object()
_SHA_RE = re.compile(r"^[0-9a-f]{40,64}$")


class _Repo:
    """Bundle of the config plus the git helpers every step needs.

    Hot paths avoid spawning git: HEAD, branch, refs, the remote URL and in-progress
    markers are read from ``.git`` directly, and HEAD / ahead are cached within one
    operation (``moved()`` drops the cache after anything that rewrites history).
    """

    def __init__(self, cfg: config.Config, lock: FileLock | None = None):
        self.cfg = cfg
        self.dir = Path(cfg.brain_dir)
        self.remote = cfg.remote or "origin"
        self.branch = cfg.branch or "main"
        self.lock = lock
        self.preflighted = False
        self._git_dir: Path | None = None
        self._common: Path | None = None
        self._head = _UNSET
        self._ahead: int | None = None
        self.git_calls = 0

    @property
    def remote_ref(self) -> str:
        return f"refs/remotes/{self.remote}/{self.branch}"

    def git(self, *args, timeout: float = LOCAL_TIMEOUT, input=None, env=None) -> gitops.Result:
        if self.lock is not None:
            self.lock.touch()
        self.git_calls += 1
        return gitops.run(list(args), cwd=self.dir, timeout=timeout, input=input, env=env)

    # -- file-system reads (no subprocess) ---------------------------------
    def git_dir(self) -> Path:
        if self._git_dir is None:
            self._git_dir = config.git_dir_of(self.dir) or (self.dir / ".git")
        return self._git_dir

    def common_dir(self) -> Path:
        if self._common is None:
            self._common = config.common_dir(self.git_dir())
        return self._common

    def _read_ref_fs(self, ref: str, depth: int = 0) -> str:
        if depth > 5:
            return ""
        for base in (self.common_dir(), self.git_dir()):
            try:
                text = (base / ref).read_text(encoding="utf-8").strip()
            except OSError:
                continue
            if _SHA_RE.match(text):
                return text
            if text.startswith("ref:"):
                return self._read_ref_fs(text[4:].strip(), depth + 1)
        try:
            for line in (self.common_dir() / "packed-refs").read_text(encoding="utf-8").splitlines():
                if line and line[0] not in "#^":
                    sha, _, name = line.partition(" ")
                    if name.strip() == ref and _SHA_RE.match(sha):
                        return sha
        except OSError:
            pass
        return ""

    def read_sha(self, ref: str) -> str:
        """Commit sha of ``ref``: file-system first, one ``rev-parse`` if that finds nothing."""
        sha = self._read_ref_fs(ref)
        if sha:
            return sha
        r = self.git("rev-parse", "--verify", "-q", ref + "^{commit}")
        return r.out.strip() if r.ok else ""

    def current_branch(self) -> str | None:
        """Branch name from ``.git/HEAD`` ('' when detached, None when unreadable)."""
        try:
            text = (self.git_dir() / "HEAD").read_text(encoding="utf-8").strip()
        except OSError:
            return None
        if text.startswith("ref:"):
            ref = text[4:].strip()
            return ref[len("refs/heads/"):] if ref.startswith("refs/heads/") else ref
        return ""

    def head(self) -> str:
        """HEAD sha ('' for an unborn branch); cached until ``moved()``."""
        if self._head is _UNSET:
            sha = ""
            try:
                text = (self.git_dir() / "HEAD").read_text(encoding="utf-8").strip()
            except OSError:
                text = ""
            if text.startswith("ref:"):
                sha = self._read_ref_fs(text[4:].strip())
            elif _SHA_RE.match(text):
                sha = text
            if not sha:
                r = self.git("rev-parse", "--verify", "-q", "HEAD")
                sha = r.out.strip() if r.ok else ""
            self._head = sha
        return self._head  # type: ignore[return-value]

    def moved(self, ahead: int | None = None) -> None:
        """HEAD was rewritten (commit, rebase, reset): forget cached values."""
        self._head = _UNSET
        self._ahead = ahead

    def remote_sha(self) -> str:
        return self.read_sha(self.remote_ref)

    def remote_url(self) -> str:
        url = config.remote_url(self.dir, self.remote)
        if url:
            return url
        r = self.git("config", "--get", f"remote.{self.remote}.url")  # e.g. set through an include
        return r.out.strip() if r.ok else ""

    def short(self, sha: str) -> str:
        return sha[:10] if sha else ""

    # -- git queries ----------------------------------------------------------
    def has_ref(self, ref: str) -> bool:
        return self.git("rev-parse", "--verify", "-q", ref + "^{commit}").ok

    def ahead(self) -> int:
        """Commits not yet on the remote-tracking branch (cached; free when HEAD == remote)."""
        if self._ahead is None:
            head = self.head()
            remote = self._read_ref_fs(self.remote_ref)
            if not head or (remote and head == remote):
                self._ahead = 0
            else:
                r = self.git("rev-list", "--count", f"{self.remote_ref}..HEAD")
                if not r.ok:  # never fetched: everything is unpushed
                    r = self.git("rev-list", "--count", "HEAD")
                try:
                    self._ahead = int(r.out.strip()) if r.ok else 0
                except ValueError:
                    self._ahead = 0
        return self._ahead

    def behind(self) -> int:
        head, remote = self.head(), self._read_ref_fs(self.remote_ref)
        if not head or not remote or head == remote:
            return 0
        r = self.git("rev-list", "--count", f"HEAD..{self.remote_ref}")
        try:
            return int(r.out.strip()) if r.ok else 0
        except ValueError:
            return 0

    def blob(self, rev: str, path: str) -> bytes | None:
        if not rev:
            return None
        r = self.git("cat-file", "blob", f"{rev}:{path}")
        return r.out_bytes if r.ok else None

    def names(self, *revs: str) -> list[str]:
        r = self.git("diff", "--name-only", "--no-renames", "-z", *revs)
        return _split_z(r.out) if r.ok else []

    def rel(self, p) -> str | None:
        """Repo-relative POSIX path for an absolute or relative path inside the repo."""
        s = str(p)
        if not os.path.isabs(s):
            return safety.norm_rel(s)
        try:
            tail = os.path.relpath(os.path.abspath(s), os.path.abspath(str(self.dir)))
        except ValueError:
            return None
        if tail == ".." or tail.startswith(".." + os.sep):
            return None
        return safety.norm_rel(tail)


def _load_repo(lock: FileLock | None = None) -> _Repo:
    return _Repo(config.load(), lock)


def _git_lock() -> FileLock:
    return FileLock(config.state_path("locks", "git.lock"), stale_after=120)


# --------------------------------------------------------------------------
# preflight: repo, in-progress rebase/merge, branch
# --------------------------------------------------------------------------
def _backup_ref(repo: _Repo, sha: str, suffix: str = "") -> str:
    """Point ``refs/brain-backup/<stamp>`` at ``sha``; returns the ref name ('' on failure)."""
    if not sha:
        return ""
    base = f"refs/brain-backup/{_stamp()}{suffix}"
    name, n = base, 1
    while repo.has_ref(name):
        n += 1
        name = f"{base}-{n}"
    r = repo.git("update-ref", name, sha)
    return name if r.ok else ""


def _abort_in_progress(repo: _Repo) -> str:
    """Abort a half-finished rebase/merge, keeping a backup ref. Returns a note ('' if none)."""
    gd = repo.git_dir()
    note = ""
    rebase = (gd / "rebase-merge").exists() or (gd / "rebase-apply").exists()
    merging = (gd / "MERGE_HEAD").exists()
    if not (rebase or merging):
        return ""
    sha = ""
    for cand in (gd / "rebase-merge" / "orig-head", gd / "ORIG_HEAD"):
        try:
            if rebase and cand.exists():
                sha = cand.read_text(encoding="utf-8").strip()
                break
        except OSError:
            pass
    if not sha:
        sha = repo.head()
    ref = _backup_ref(repo, sha, "-aborted")
    if rebase:
        repo.git("rebase", "--abort")
    if (gd / "MERGE_HEAD").exists():
        repo.git("merge", "--abort")
    repo.moved()
    note = f"aborted an unfinished {'rebase' if rebase else 'merge'}" + (f" (backup {ref})" if ref else "")
    _log(note)
    return note


def _preflight(repo: _Repo) -> tuple[dict | None, str]:
    """(result-to-return-or-None, note). Pure file-system checks: no git subprocess unless a
    half-finished rebase or merge has to be aborted."""
    if repo.preflighted:
        return None, ""
    if not repo.dir.is_dir() or not (repo.dir / ".git").exists() or repo.current_branch() is None:
        return _result("not-a-repo", f"{repo.dir} is not a git clone"), ""
    note = _abort_in_progress(repo)
    br = repo.current_branch()
    if br != repo.branch:
        return (
            _result(
                "wrong-branch",
                f"the brain clone is on '{br or 'a detached HEAD'}', not '{repo.branch}'; nothing was done",
                head=repo.head(),
            ),
            note,
        )
    repo.preflighted = True
    return None, note


# --------------------------------------------------------------------------
# status parsing and commit_pending
# --------------------------------------------------------------------------
def _read_status(repo: _Repo) -> tuple[list[tuple[str, str]], dict]:
    """One ``git status --porcelain=v2 --branch`` call.

    Returns ``(entries, info)``: ``entries`` are ``(xy, relpath)`` with v1-style two-letter
    codes (``" M"``, ``"??"``, ``"D "``...), ``info`` has ``oid`` / ``head`` / ``upstream`` /
    ``ahead`` / ``behind``. Also primes the repo's HEAD and ahead caches.
    """
    info: dict = {"oid": None, "head": None, "upstream": None, "ahead": None, "behind": None, "ok": False}
    r = repo.git("--no-optional-locks", "status", "--porcelain=v2", "-z", "--branch", "--untracked-files=all")
    if not r.ok:
        return [], info
    info["ok"] = True
    entries: list[tuple[str, str]] = []
    toks = r.out.split("\0")
    i = 0
    while i < len(toks):
        t = toks[i]
        i += 1
        if not t:
            continue
        if t.startswith("# branch.oid "):
            info["oid"] = t[len("# branch.oid "):]
        elif t.startswith("# branch.head "):
            info["head"] = t[len("# branch.head "):]
        elif t.startswith("# branch.upstream "):
            info["upstream"] = t[len("# branch.upstream "):]
        elif t.startswith("# branch.ab "):
            m = re.match(r"# branch\.ab \+(\d+) -(\d+)", t)
            if m:
                info["ahead"], info["behind"] = int(m.group(1)), int(m.group(2))
        elif t[0] == "1":
            parts = t.split(" ", 8)
            if len(parts) == 9:
                entries.append((parts[1].replace(".", " "), safety.norm_rel(parts[8])))
        elif t[0] == "2":
            parts = t.split(" ", 9)
            if len(parts) == 10:
                entries.append((parts[1].replace(".", " "), safety.norm_rel(parts[9])))
            i += 1  # the original path of the rename/copy follows
        elif t[0] == "u":
            parts = t.split(" ", 10)
            if len(parts) == 11:
                entries.append((parts[1].replace(".", " "), safety.norm_rel(parts[10])))
        elif t[0] == "?":
            entries.append(("??", safety.norm_rel(t[2:])))
    if info["oid"]:
        repo._head = "" if info["oid"] == "(initial)" else info["oid"]
        if info["upstream"] == f"{repo.remote}/{repo.branch}" and info["ahead"] is not None:
            repo._ahead = info["ahead"]
        else:
            repo._ahead = None
    return entries, info


def _matches(rel: str, wanted: list[str] | None) -> bool:
    if wanted is None:
        return True
    for w in wanted:
        w = w.rstrip("/")
        if rel == w or rel.startswith(w + "/"):
            return True
    return False


def _py_compile_problem(abs_path: Path, rel: str) -> dict | None:
    try:
        data = abs_path.read_bytes()
        compile(data, rel, "exec", dont_inherit=True)
    except SyntaxError as e:
        return {"reason": f"py_compile failed: {e.msg}", "line": e.lineno}
    except Exception as e:
        return {"reason": f"py_compile failed: {type(e).__name__}: {e}", "line": None}
    return None


def _commit_summary(repo: _Repo, paths: list[str]) -> str:
    for p in paths:
        if p.startswith("handoffs/") and p.endswith(".json"):
            try:
                d = json.loads((repo.dir / p).read_text(encoding="utf-8"))
                task = str(d.get("task") or "").strip().replace("\n", " ")
                if task:
                    return task[:60]
            except (OSError, ValueError):
                continue
    n = len(paths)
    return f"{n} file{'s' if n != 1 else ''}"


def _update_blocked(examined: set[str] | None, blocked: list[dict]) -> None:
    """Keep ``state/blocked.json`` current. ``examined=None`` means everything was checked."""
    prev = state.read("blocked", {})
    old = [e for e in prev.get("files", []) if isinstance(e, dict) and e.get("path")]
    since = {(e["path"], e.get("reason")): e.get("since") for e in old}
    now = _iso()
    new_entries = [
        {"path": b["path"], "reason": b["reason"], "line": b.get("line"),
         "since": since.get((b["path"], b["reason"])) or now}
        for b in blocked
    ]
    if examined is None:
        keep: list[dict] = []
    else:
        keep = [e for e in old if e["path"] not in examined]
    merged = {e["path"]: e for e in keep}
    merged.update({e["path"]: e for e in new_entries})
    if [(e["path"], e.get("reason"), e.get("line")) for e in old] == [
        (e["path"], e.get("reason"), e.get("line")) for e in merged.values()
    ]:
        return  # nothing changed: no write
    _safe_state_write("blocked", {"files": list(merged.values()), "at": now})


def _tidy_merged(committed: Iterable[str]) -> None:
    """A local edit to a file flagged for tidying counts as the tidy."""
    d = state.read("merged", {})
    entries = [e for e in d.get("entries", []) if isinstance(e, dict)]
    if not entries:
        return
    done = set(committed)
    left = [e for e in entries if e.get("path") not in done]
    if len(left) != len(entries):
        _write_merged(left)


def _write_merged(entries: list[dict]) -> None:
    cutoff = _now() - timedelta(days=MERGED_KEEP_DAYS)
    fresh = []
    for e in entries:
        at = _parse_iso(e.get("at"))
        if at is None or at >= cutoff:
            fresh.append(e)
    _safe_state_write("merged", {"files": sorted({e["path"] for e in fresh}), "entries": fresh, "at": _iso()})


def _record_merged(files: Iterable[str], head: str) -> None:
    files = list(files)
    d = state.read("merged", {})
    entries = {e["path"]: e for e in d.get("entries", []) if isinstance(e, dict) and e.get("path")}
    now = _iso()
    for f in files:
        entries[f] = {"path": f, "at": now, "head": head}
    _write_merged(list(entries.values()))


def clear_merged(paths: Iterable[str] | None = None) -> None:
    """Forget files flagged as merged from both sides (all of them when ``paths`` is None)."""
    if paths is None:
        _write_merged([])
    else:
        _tidy_merged(paths)


def _commit_locked(repo: _Repo, message: str | None = None, paths: list[str] | None = None) -> tuple[dict, list[tuple[str, str]]]:
    """Stage what is safe, leave the rest on disk, commit. Caller holds the git lock.

    A clean tree costs exactly one git call (status). Returns ``(result, leftovers)`` where
    leftovers are the (xy, relpath) status entries that were not committed (blocked or
    outside the allowlist).
    """
    pre, note = _preflight(repo)
    if pre is not None:
        return pre, []
    wanted = None
    if paths is not None:
        wanted = [p for p in (repo.rel(x) for x in paths) if p]
    entries, info = _read_status(repo)
    if not info["ok"]:
        return _result("error", "git status failed", head=repo.head()), []
    # The index must hold only what we stage now: drop anything somebody staged by hand.
    if any(xy[0] not in " ?U" for xy, _rel in entries):
        repo.git("reset", "-q")
        entries, info = _read_status(repo)
    tracked: list[str] | None = None
    to_stage: list[str] = []
    blocked: list[dict] = []
    leftovers: list[tuple[str, str]] = []
    examined: set[str] = set()
    for xy, rel in entries:
        if not _matches(rel, wanted):
            continue
        if not safety.is_allowed(rel) or "U" in xy or xy in ("AA", "DD"):
            leftovers.append((xy, rel))
            continue
        examined.add(rel)
        abs_path = repo.dir / rel
        deleted = "D" in xy or not os.path.lexists(abs_path)
        if deleted:
            to_stage.append(rel)
            continue
        problems: list[dict] = []
        if os.path.islink(abs_path):
            problems.append({"reason": "symlinks are not synced", "line": None})
        elif not abs_path.is_file():
            continue
        else:
            if tracked is None:
                tracked = safety.tracked_paths(repo.dir)
            for why in safety.check_path(rel, tracked=tracked):
                problems.append({"reason": why, "line": None})
            if not problems and rel.startswith(".brain/") and rel.endswith(".py"):
                p = _py_compile_problem(abs_path, rel)
                if p:
                    problems.append(p)
            if not problems:
                problems.extend(safety.check_file(abs_path, rel))
        if problems:
            first = problems[0]
            blocked.append({"path": rel, "reason": first["reason"], "line": first.get("line")})
            leftovers.append((xy, rel))
        else:
            to_stage.append(rel)
    _update_blocked(None if wanted is None else examined, blocked)

    msg_note = f"; {note}" if note else ""
    if not to_stage:
        return _result("ok", "nothing to commit" + msg_note, blocked=blocked, head=repo.head()), leftovers
    payload = "\0".join(to_stage) + "\0"
    add = repo.git("--literal-pathspecs", "add", "-A", "--pathspec-from-file=-", "--pathspec-file-nul", input=payload)
    if not add.ok:
        return _result("error", f"git add failed: {add.err.strip()[:300]}", blocked=blocked, head=repo.head()), leftovers
    if repo.git("diff", "--cached", "--quiet").code == 0:
        return _result("ok", "nothing to commit" + msg_note, blocked=blocked, head=repo.head()), leftovers
    person = repo.cfg.person or "unknown"
    if message and message.startswith("brain:"):
        full = message
    else:
        summary = (message or _commit_summary(repo, to_stage)).strip().replace("\n", " ")[:72]
        full = f"brain: {summary} ({person})"
    name = repo.cfg.display_name or person
    email = repo.cfg.email or f"{person}@users.noreply.local"
    c = repo.git(
        "-c", f"user.name={name}", "-c", f"user.email={email}", "-c", "commit.gpgsign=false",
        "commit", "-q", "--no-verify", "-m", full,
    )
    if not c.ok:
        repo.git("reset", "-q")
        return _result("error", f"git commit failed: {(c.err or c.out).strip()[:300]}", blocked=blocked, head=repo.head()), leftovers
    repo.moved(None if repo._ahead is None else repo._ahead + 1)
    _tidy_merged(to_stage)
    _log(f"committed {len(to_stage)} file(s): {full}")
    res = _result("ok", f"committed {len(to_stage)} file(s)" + msg_note, committed=list(to_stage), blocked=blocked, head=repo.head())
    return res, leftovers


def commit_pending(message: str | None = None, paths: list | None = None, *, lock_timeout: float = 10.0) -> dict:
    """Commit every safe, allowed change (or only ``paths``). Never raises."""
    try:
        cfg = config.load()
        lock = _git_lock()
        if not lock.acquire(lock_timeout):
            return _result("locked", "another sync holds the lock; it will commit pending files")
        try:
            repo = _Repo(cfg, lock)
            res, _ = _commit_locked(repo, message, paths)
            if res["status"] == "ok":
                res["unpushed"] = repo.ahead()
            return res
        finally:
            lock.release()
    except Exception as e:
        _log("commit_pending crashed: " + traceback.format_exc(limit=3))
        return _result("error", f"commit_pending failed: {type(e).__name__}: {e}")


# --------------------------------------------------------------------------
# pull
# --------------------------------------------------------------------------
def _record_sync(**fields) -> None:
    d = state.read("sync", {})
    d.update(fields)
    _safe_state_write("sync", d)


def _record_attempt(status: str, message: str, unpushed: int | None = None) -> None:
    f = {"status": status, "message": message, "last_attempt_at": _iso()}
    if unpushed is not None:
        f["unpushed"] = unpushed
    _record_sync(**f)


def _park_leftovers(repo: _Repo, leftovers: list[tuple[str, str]], ref: str) -> tuple[dict[str, bytes], Path | None]:
    """Save blocked / non-allowed local edits that a rebase or reset could touch.

    Tracked files with local modifications are reverted to HEAD for the duration (their
    content is parked on disk and in memory); untracked files are parked only when the
    remote tree holds the same path. Returns ``({path: bytes}, folder-holding-the-disk-copies)``;
    the folder is None when nothing was parked.
    """
    parked: dict[str, bytes] = {}
    if not leftovers:
        return parked, None
    remote_tree: set[str] | None = None
    keep_root: Path | None = None
    revert: list[str] = []
    for xy, rel in leftovers:
        p = repo.dir / rel
        if xy == "??":
            if remote_tree is None:
                r = repo.git("ls-tree", "-r", "--name-only", "-z", ref)
                remote_tree = set(_split_z(r.out)) if r.ok else set()
            if rel not in remote_tree:
                continue
        elif "D" in xy or not p.is_file():
            continue
        else:
            revert.append(rel)
        try:
            data = p.read_bytes()
        except OSError:
            continue
        parked[rel] = data
        if keep_root is None:
            keep_root = config.state_dir() / "state" / "preserved" / f"{_stamp()}-parked"
        dest = keep_root / rel
        try:
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(data)
        except OSError:
            pass
    for rel in revert:
        repo.git("--literal-pathspecs", "checkout", "-q", "--", rel)
    for xy, rel in leftovers:
        if xy == "??" and rel in parked:
            try:
                os.unlink(repo.dir / rel)
            except OSError:
                pass
    return parked, keep_root


def _unpark(repo: _Repo, parked: dict[str, bytes], old_head: str, new_head: str) -> list[dict]:
    """Put parked local edits back unless the remote changed the same file.

    Returns notes ``{path, saved_to}`` for files whose local copy had to stay in the
    machine-local ``state/preserved`` folder.
    """
    notes: list[dict] = []
    if not parked:
        return notes
    keep_root = config.state_dir() / "state" / "preserved" / f"{_stamp()}-clash"
    for rel, data in parked.items():
        before = repo.blob(old_head, rel)
        after = repo.blob(new_head, rel)
        dest = repo.dir / rel
        if before == after:
            try:
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(data)
            except OSError as e:
                _log(f"could not restore parked {rel}: {e}")
            continue
        saved = keep_root / rel
        try:
            saved.parent.mkdir(parents=True, exist_ok=True)
            saved.write_bytes(data)
            notes.append({"path": rel, "saved_to": str(saved)})
        except OSError as e:
            _log(f"could not preserve {rel}: {e}")
    return notes


def _conflict_dir(repo: _Repo, stamp: str) -> str:
    person = re.sub(r"[^A-Za-z0-9._-]+", "-", repo.cfg.person or "unknown") or "unknown"
    return f"conflicts/{stamp}-{person}"


def _recover_from_clash(
    repo: _Repo, old_head: str, ref: str, base: str, local_changed: list[str], parked: dict[str, bytes]
) -> dict:
    """The rebase stopped: save everything, reset to the remote, re-apply local work.

    Returns ``{"backup_ref", "saved", "details", "parked_notes"}``.
    """
    repo.git("rebase", "--abort")
    backup = _backup_ref(repo, old_head)
    reset = repo.git("reset", "-q", "--hard", ref)
    repo.moved()
    if not reset.ok:
        raise RuntimeError(f"git reset --hard {ref} failed: {reset.err.strip()[:300]}")
    stamp = _stamp()
    cdir = _conflict_dir(repo, stamp)
    saved: list[str] = []
    details: list[dict] = []
    for rel in local_changed:
        L = repo.blob(old_head, rel)
        R = repo.blob(ref, rel)
        B = repo.blob(base, rel) if base else None
        if L == R:
            continue
        target = repo.dir / rel
        if R == B:
            # the remote never touched it: simply re-apply the local change
            if L is None:
                try:
                    os.unlink(target)
                except OSError:
                    pass
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(L)
            continue
        if L is None:
            details.append({"path": rel, "action": "kept-remote (deleted locally, changed remotely)", "saved_to": None})
            saved.append(rel)
            continue
        if R is None:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(L)
            details.append({"path": rel, "action": "restored (deleted remotely, changed locally)", "saved_to": None})
            saved.append(rel)
            continue
        merged = None
        if PurePosixPath(rel).suffix.lower() in TEXT_EXTS:
            merged = _union_merge(L, B or b"", R)
        if merged is not None:
            target.write_bytes(merged)
            details.append({"path": rel, "action": "union-merged", "saved_to": None})
            saved.append(rel)
            continue
        dest_rel = f"{cdir}/{rel}"
        dest = repo.dir / dest_rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(L)
        details.append({"path": rel, "action": "local copy saved, remote version kept", "saved_to": dest_rel})
        saved.append(rel)
    new_head = repo.head()
    notes = _unpark(repo, parked, old_head, new_head)
    return {"backup_ref": backup, "saved": saved, "details": details, "parked_notes": notes, "conflict_dir": cdir}


def _union_merge(local: bytes, base: bytes, remote: bytes) -> bytes | None:
    """``git merge-file --union``; None when the inputs are not mergeable text."""
    try:
        for b in (local, base, remote):
            b.decode("utf-8")
    except UnicodeDecodeError:
        return None
    tmp = Path(tempfile.mkdtemp(prefix="mmb-merge-"))
    try:
        (tmp / "cur").write_bytes(local)
        (tmp / "base").write_bytes(base)
        (tmp / "other").write_bytes(remote)
        r = gitops.run(["merge-file", "-p", "--union", "cur", "base", "other"], cwd=tmp, timeout=30)
        if r.code != 0 or r.timed_out:
            return None
        return r.out_bytes
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def _cleanup_own_claims(repo: _Repo) -> list[str]:
    """Delete this person's claim files idle for more than 3 hours (committed on the next commit)."""
    removed: list[str] = []
    person = repo.cfg.person
    if not person:
        return removed
    folder = repo.dir / "claims" / person
    if not folder.is_dir():
        return removed
    cutoff = _now() - timedelta(hours=STALE_CLAIM_HOURS)
    for f in folder.glob("*.json"):
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
            last = _parse_iso(data.get("last_active") or data.get("started_at"))
        except (OSError, ValueError, AttributeError):
            last = None
        if last is None:
            try:
                last = datetime.fromtimestamp(f.stat().st_mtime, timezone.utc)
            except OSError:
                continue
        if last < cutoff:
            try:
                f.unlink()
                removed.append(safety.norm_rel(f.relative_to(repo.dir)))
            except OSError:
                pass
    return removed


def _pull_locked(repo: _Repo, force: bool, min_interval: float, timeout: float, pre=None) -> dict:
    """Fetch and rebase. ``pre`` is an already computed ``_commit_locked`` outcome (sync does the
    commit first); without it the pending files are committed after the throttle check.

    Call budget: clean tree and nothing new on the remote = status + fetch (2 git calls);
    clean tree with new remote commits = status, fetch, rev-list, rebase, diff (5).
    """
    pre_res, note = _preflight(repo)
    if pre_res is not None:
        return pre_res
    sync_state = state.read("sync", {})
    if not force and min_interval > 0:
        last = _parse_iso(sync_state.get("last_fetch_at"))
        if last is not None and (_now() - last).total_seconds() < min_interval:
            age = int((_now() - last).total_seconds())
            c_res = pre[0] if pre else {}
            return _result(
                "skipped", f"fetched {age}s ago", head=repo.head(), unpushed=repo.ahead(),
                blocked=c_res.get("blocked") or _blocked_now(), committed=list(c_res.get("committed", [])),
            )
    url = repo.remote_url()
    if not url:
        res = _result("error", f"no git remote named '{repo.remote}'", head=repo.head())
        _record_attempt("error", res["message"])
        return res
    commit_res, leftovers = pre if pre is not None else _commit_locked(repo)
    blocked = commit_res.get("blocked", [])
    committed = list(commit_res.get("committed", []))
    if commit_res["status"] not in ("ok",):
        commit_res["blocked"] = blocked
        return commit_res

    fetch = repo.git(
        "fetch", "--no-tags", "--quiet", repo.remote,
        f"+refs/heads/{repo.branch}:{repo.remote_ref}", timeout=timeout,
    )
    if not fetch.ok:
        text = fetch.err + fetch.out
        if "couldn't find remote ref" in text.lower():
            # An empty remote (a new GitHub repo, or the remote was re-created): drop any stale remote-tracking ref
            # left from an earlier remote, so every local commit counts as unpushed and the next push creates the branch.
            if repo._read_ref_fs(repo.remote_ref):
                repo.git("update-ref", "-d", repo.remote_ref)
                repo._ahead = None
            ahead = repo.ahead()
            _record_sync(last_fetch_at=_iso(), last_attempt_at=_iso(), status="ok",
                         message="remote has no branch yet", head=repo.head(), unpushed=ahead)
            return _result("ok", f"remote has no '{repo.branch}' branch yet", committed=committed,
                           blocked=blocked, head=repo.head(), unpushed=ahead)
        ahead = repo.ahead()
        kind = gitops.classify(fetch, url)
        if kind == "ok":
            kind = "error"
        msg = {
            "offline": "offline: could not reach the remote; using the local copy",
            "auth": "cannot reach the brain repo on GitHub: missing repo, no access, or sign-in needed",
            "error": f"git fetch failed: {text.strip()[:300]}",
        }[kind]
        _record_attempt(kind, msg, ahead)
        _log(f"fetch {kind}: {text.strip()[:200]}")
        return _result(kind, msg, committed=committed, blocked=blocked, head=repo.head(), unpushed=ahead)

    ref = repo.remote_ref
    old_head = repo.head()
    remote_sha = repo.remote_sha()
    if not old_head or not remote_sha:
        res = _result("error", "the brain clone has no commits yet" if not old_head else f"{ref} is missing after fetch")
        _record_attempt("error", res["message"])
        return res
    ahead_n, behind_n = 0, 0
    if remote_sha != old_head:
        lr = repo.git("rev-list", "--left-right", "--count", f"HEAD...{ref}")
        try:
            ahead_n, behind_n = (int(x) for x in lr.out.split())
        except ValueError:
            res = _result("error", f"could not compare HEAD with {ref}: {lr.err.strip()[:200]}")
            _record_attempt("error", res["message"])
            return res
    repo.moved(ahead_n)  # the fetch changed the remote ref: ahead is now known exactly
    contains_remote = behind_n == 0

    status = "ok"
    message = "up to date" if contains_remote else "pulled"
    saved: list[str] = []
    extra: dict = {}
    local_changed: list[str] = []
    remote_changed: list[str] = []
    if not contains_remote:
        base = ""
        if ahead_n > 0:  # diverged: we need to know which files both sides touched
            base = repo.git("merge-base", "HEAD", ref).out.strip()
            if base:
                local_changed = repo.names(base, "HEAD")
                remote_changed = repo.names(base, ref)
            else:  # unrelated histories: treat everything local as a local change
                lt = repo.git("ls-tree", "-r", "--name-only", "-z", "HEAD")
                rt = repo.git("ls-tree", "-r", "--name-only", "-z", ref)
                local_changed = _split_z(lt.out) if lt.ok else []
                remote_changed = _split_z(rt.out) if rt.ok else []
        parked, park_dir = _park_leftovers(repo, leftovers, ref)
        rb = repo.git("rebase", ref, timeout=REBASE_TIMEOUT)
        if rb.ok:
            repo.moved(ahead_n)  # replayed commits: same count, new shas
            notes = _unpark(repo, parked, old_head, repo.head())
            if notes:
                extra["parked_conflicts"] = notes
        else:
            _log(f"rebase stopped: {(rb.err or rb.out).strip()[:300]}")
            if not base:
                base = repo.git("merge-base", old_head, ref).out.strip()
            rec = _recover_from_clash(repo, old_head, ref, base, local_changed, parked)
            saved = rec["saved"]
            extra.update(
                backup_ref=rec["backup_ref"], conflict_details=rec["details"],
                conflict_dir=rec["conflict_dir"],
            )
            if rec["parked_notes"]:
                extra["parked_conflicts"] = rec["parked_notes"]
            status = "conflict-saved"
            who = repo.cfg.person or "unknown"
            cc, _ = _commit_locked(repo, message=f"brain: kept both versions after a sync clash ({who})")
            if cc["status"] != "ok":
                _log(f"clash commit problem: {cc['message']}")
            committed.extend(cc.get("committed", []))
            blocked = cc.get("blocked", blocked)
            message = (
                f"remote and local edits clashed on {len(saved)} file(s); both versions were kept "
                f"(backup {rec['backup_ref'] or 'n/a'})"
            )
        if park_dir is not None:  # every parked edit is back in place or saved elsewhere
            shutil.rmtree(park_dir, ignore_errors=True)
    new_head = repo.head()
    changed = repo.names(old_head, new_head) if new_head != old_head else []
    overlap = sorted(
        p for p in (set(local_changed) & set(remote_changed))
        if not p.startswith("handoffs/") and not p.startswith("claims/")
    )
    if overlap:
        _record_merged(overlap, new_head)
    removed_claims = _cleanup_own_claims(repo)
    if removed_claims:  # commit the clean-up now so the same sync can push it
        who = repo.cfg.person or "unknown"
        cc, _ = _commit_locked(repo, message=f"brain: removed stale claims ({who})", paths=removed_claims)
        committed.extend(cc.get("committed", []))
        new_head = repo.head()
    unpushed = repo.ahead()
    now = _iso()
    history = [h for h in sync_state.get("history", []) if isinstance(h, dict)]
    if changed:
        history.append({"at": now, "head": new_head, "files": changed[:200]})
    _record_sync(
        last_fetch_at=now, last_pull_ok_at=now, last_attempt_at=now, head=new_head,
        changed_files=changed, status=status, message=message, unpushed=unpushed,
        history=history[-10:],
    )
    _log(f"pull {status}: {len(changed)} changed, {len(overlap)} merged both sides, {unpushed} unpushed")
    res = _result(
        status, message, changed_files=changed, committed=committed, blocked=blocked,
        merged_both_sides=overlap, saved_conflicts=saved, head=new_head, unpushed=unpushed,
        removed_claims=removed_claims,
    )
    res.update(extra)
    return res


def _blocked_now() -> list[dict]:
    d = state.read("blocked", {})
    return [
        {"path": e["path"], "reason": e.get("reason", ""), "line": e.get("line")}
        for e in d.get("files", []) if isinstance(e, dict) and e.get("path")
    ]


def pull(*, force: bool = False, min_interval: float = 60, timeout: float = 8, lock_timeout: float = 0.0) -> dict:
    """Commit pending files, fetch and rebase onto the remote. Never raises."""
    try:
        cfg = config.load()
        lock = _git_lock()
        if not lock.acquire(lock_timeout):
            return _result("locked", "another sync is running; it will bring the local copy up to date")
        try:
            return _pull_locked(_Repo(cfg, lock), force, min_interval, timeout)
        finally:
            lock.release()
    except Exception as e:
        _log("pull crashed: " + traceback.format_exc(limit=3))
        return _result("error", f"pull failed: {type(e).__name__}: {e}")


# --------------------------------------------------------------------------
# push
# --------------------------------------------------------------------------
def _push_locked(repo: _Repo, timeout: float, retries: int, committed: list | None = None, blocked: list | None = None) -> dict:
    """Push what is ahead. ``committed``/``blocked`` given means the caller (sync) just ran the
    commit step, so it is not repeated; nothing ahead costs no git call at all."""
    pre, _note = _preflight(repo)
    if pre is not None:
        return pre
    url = repo.remote_url()
    if not url:
        return _result("error", f"no git remote named '{repo.remote}'", head=repo.head())
    if committed is None:
        commit_res, _left = _commit_locked(repo)
        if commit_res["status"] != "ok":
            return commit_res
        blocked = commit_res.get("blocked", [])
        committed = list(commit_res.get("committed", []))
    blocked = blocked or []
    committed = list(committed)
    ahead = repo.ahead()
    if ahead == 0 and repo.remote_sha():
        return _result("ok", "nothing to push", committed=committed, blocked=blocked, head=repo.head())
    attempt = 0
    changed: list[str] = []
    saved: list[str] = []
    merged: list[str] = []
    while True:
        r = repo.git("push", "--quiet", repo.remote, f"HEAD:refs/heads/{repo.branch}", timeout=timeout)
        if r.ok:
            now = _iso()
            repo.moved(0)
            _record_sync(last_push_ok_at=now, unpushed=0)
            _log(f"pushed {ahead} commit(s)")
            return _result(
                "ok", f"pushed {ahead} commit(s)", pushed=True, committed=committed, blocked=blocked,
                changed_files=changed, saved_conflicts=saved, merged_both_sides=merged,
                head=repo.head(), unpushed=0,
            )
        text = r.err + r.out
        if gitops.is_non_fast_forward(text) and attempt < max(0, retries):
            attempt += 1
            time.sleep(0.5 + random.random() * 1.5)
            p = _pull_locked(repo, force=True, min_interval=0, timeout=max(timeout, 8))
            if p["status"] not in OK_STATUSES:
                p["committed"] = committed
                p["unpushed"] = repo.ahead()
                return p
            changed = sorted(set(changed) | set(p.get("changed_files", [])))
            saved.extend(p.get("saved_conflicts", []))
            merged = sorted(set(merged) | set(p.get("merged_both_sides", [])))
            committed = list(dict.fromkeys([*committed, *p.get("committed", [])]))
            ahead = repo.ahead()
            continue
        kind = gitops.classify(r, url)
        if kind in ("offline", "auth"):
            msg = (
                "offline: saved locally; it will be pushed at the next sync" if kind == "offline"
                else "sign-in needed: saved locally; run the login command to share it"
            )
        elif gitops.is_non_fast_forward(text):
            kind, msg = "error", "push was rejected repeatedly (the remote keeps changing); it will retry at the next sync"
        else:
            kind, msg = "error", f"git push failed: {text.strip()[:300]}"
        _record_attempt(kind, msg, ahead)
        _record_sync(last_push_error=msg, last_push_error_at=_iso())
        _log(f"push {kind}: {text.strip()[:200]}")
        return _result(kind, msg, committed=committed, blocked=blocked, head=repo.head(), unpushed=ahead)


def push(*, timeout: float = 20, lock_timeout: float = 5.0, retries: int = 3) -> dict:
    """Commit pending files and push; on a non-fast-forward rejection pull and retry."""
    try:
        cfg = config.load()
        lock = _git_lock()
        if not lock.acquire(lock_timeout):
            return _result("locked", "another sync is running; it will push pending commits")
        try:
            return _push_locked(_Repo(cfg, lock), timeout, retries)
        finally:
            lock.release()
    except Exception as e:
        _log("push crashed: " + traceback.format_exc(limit=3))
        return _result("error", f"push failed: {type(e).__name__}: {e}")


# --------------------------------------------------------------------------
# sync
# --------------------------------------------------------------------------
def sync(*, force: bool = False, timeout: float = 8, lock_timeout: float = 0.0, reason: str = "") -> dict:
    """commit_pending, then pull, then push, all under one lock. Never raises."""
    try:
        cfg = config.load()
        lock = _git_lock()
        if not lock.acquire(lock_timeout):
            return _result("locked", "another sync is running; it will pick up pending changes", reason=reason)
        try:
            repo = _Repo(cfg, lock)
            _log(f"sync start reason={reason or '-'} force={force}")
            first = _commit_locked(repo)  # also runs the preflight (branch, in-progress rebase)
            if first[0]["status"] != "ok":
                first[0]["reason"] = reason
                return first[0]
            pulled = _pull_locked(repo, force=force, min_interval=60, timeout=timeout, pre=first)
            steps = {"pull": pulled["status"]}
            if pulled["status"] not in OK_STATUSES:
                # offline / auth / error: nothing more to try; commits stay local
                pulled["steps"] = steps
                pulled["reason"] = reason
                pulled["unpushed"] = repo.ahead()
                return pulled
            pushed = _push_locked(repo, timeout=max(timeout, 20), retries=3,
                                  committed=pulled.get("committed", []), blocked=pulled.get("blocked", []))
            steps["push"] = pushed["status"]
            out = _combine(pulled, pushed)
            out["steps"] = steps
            out["reason"] = reason
            return out
        finally:
            lock.release()
    except Exception as e:
        _log("sync crashed: " + traceback.format_exc(limit=3))
        return _result("error", f"sync failed: {type(e).__name__}: {e}", reason=reason)


def _combine(pulled: dict, pushed: dict) -> dict:
    out = dict(pulled)
    out["committed"] = sorted(set(pulled.get("committed", [])) | set(pushed.get("committed", [])))
    out["blocked"] = pushed.get("blocked") or pulled.get("blocked", [])
    out["changed_files"] = sorted(set(pulled.get("changed_files", [])) | set(pushed.get("changed_files", [])))
    out["saved_conflicts"] = list(dict.fromkeys([*pulled.get("saved_conflicts", []), *pushed.get("saved_conflicts", [])]))
    out["merged_both_sides"] = sorted(set(pulled.get("merged_both_sides", [])) | set(pushed.get("merged_both_sides", [])))
    out["pushed"] = bool(pushed.get("pushed"))
    out["unpushed"] = pushed.get("unpushed", 0)
    out["head"] = pushed.get("head") or pulled.get("head", "")
    out["at"] = _iso()
    if pushed["status"] not in OK_STATUSES:
        out["status"] = pushed["status"]
        out["message"] = pushed["message"]
        out["ok"] = False
        return out
    if out["saved_conflicts"] or pulled["status"] == "conflict-saved" or pushed["status"] == "conflict-saved":
        out["status"] = "conflict-saved"
        out["message"] = pulled["message"] if pulled["status"] == "conflict-saved" else pushed["message"]
        out["ok"] = True
        return out
    did_something = bool(out["pushed"] or out["committed"] or out["changed_files"])
    out["status"] = "ok" if did_something or pulled["status"] == "ok" else "skipped"
    bits = []
    if out["changed_files"]:
        bits.append(f"{len(out['changed_files'])} file(s) updated from the team")
    if out["pushed"]:
        bits.append("shared your changes")
    out["message"] = "; ".join(bits) or pulled["message"]
    out["ok"] = True
    return out


# --------------------------------------------------------------------------
# background spawn
# --------------------------------------------------------------------------
def _pidfile() -> Path:
    return config.state_path("locks", "bg-sync.pid")


def _read_pidfile() -> dict | None:
    try:
        raw = _pidfile().read_text(encoding="utf-8").strip()
    except OSError:
        return None
    try:
        data = json.loads(raw)
        if isinstance(data, dict):
            return data
        if isinstance(data, int):
            return {"pid": data}
    except ValueError:
        if raw.isdigit():
            return {"pid": int(raw)}
    return None


def _bg_running() -> bool:
    d = _read_pidfile()
    if not d:
        return False
    pid = d.get("pid")
    at = d.get("at")
    if not isinstance(pid, int) or not pid_alive(pid):
        return False
    if isinstance(at, (int, float)) and time.time() - at > 300:
        return False  # a background sync never runs this long; the pid was likely reused
    return True


def spawn_background(reason: str, _script: str | os.PathLike | None = None) -> bool:
    """Start a detached ``brain.py sync --quiet --reason R``. Never blocks.

    Returns False when one already runs (live ``locks/bg-sync.pid``) or the script is missing.
    ``_script`` overrides the target script (used by tests).
    """
    try:
        cfg = config.load()
        spawn_lock = FileLock(config.state_path("locks", "bg-spawn.lock"), stale_after=30)
        if not spawn_lock.acquire(0):
            return False
        try:
            if _bg_running():
                return False
            script = Path(_script) if _script else Path(cfg.brain_dir) / ".brain" / "brain.py"
            if not script.exists():
                _log(f"spawn_background: {script} not found")
                return False
            py = cfg.python if gitops.python_exe_ok(cfg.python) else sys.executable
            cmd = [py, str(script), "sync", "--quiet", "--reason", str(reason or "background")]
            env = dict(os.environ)
            env["MOCKMOB_BRAIN_STATE"] = str(config.state_dir())
            env["MOCKMOB_BRAIN"] = str(cfg.brain_dir)
            log_path = config.state_path("logs", "sync.log")
            logf = open(log_path, "ab")
            try:
                kwargs: dict = dict(
                    cwd=str(cfg.brain_dir), env=env, stdin=subprocess.DEVNULL, stdout=logf, stderr=logf,
                )
                if os.name == "nt":
                    base = (
                        gitops.DETACHED_PROCESS | gitops.CREATE_NEW_PROCESS_GROUP | gitops.CREATE_NO_WINDOW
                    )
                    try:
                        proc = subprocess.Popen(cmd, creationflags=base | gitops.CREATE_BREAKAWAY_FROM_JOB, **kwargs)
                    except OSError:
                        proc = subprocess.Popen(cmd, creationflags=base, **kwargs)
                else:
                    proc = subprocess.Popen(cmd, start_new_session=True, **kwargs)
            finally:
                logf.close()
            proc.returncode = 0  # deliberately detached: stop Popen.__del__ warning about a live child
            _safe_state_write_path(_pidfile(), {"pid": proc.pid, "at": time.time(), "reason": reason})
            return True
        finally:
            spawn_lock.release()
    except Exception as e:
        _log(f"spawn_background failed: {type(e).__name__}: {e}")
        return False


def _safe_state_write_path(path: Path, data: dict) -> None:
    tmp = path.with_name(f"{path.name}.tmp-{os.getpid()}")
    try:
        tmp.write_text(json.dumps(data), encoding="utf-8")
        for attempt in range(10):
            try:
                os.replace(tmp, path)
                return
            except PermissionError:
                time.sleep(0.02 * (attempt + 1))
    except OSError:
        pass
    finally:
        try:
            if tmp.exists():
                tmp.unlink()
        except OSError:
            pass


# --------------------------------------------------------------------------
# status
# --------------------------------------------------------------------------
def status() -> dict:
    """Read-only snapshot of the clone and the last sync (one git call). Never raises, takes no lock."""
    try:
        cfg = config.load()
        repo = _Repo(cfg)
        if not repo.dir.is_dir() or not (repo.dir / ".git").exists() or repo.current_branch() is None:
            return _result("not-a-repo", f"{repo.dir} is not a git clone")
        br = repo.current_branch() or ""
        gd = repo.git_dir()
        in_progress = any((gd / n).exists() for n in ("rebase-merge", "rebase-apply", "MERGE_HEAD"))
        entries, info = _read_status(repo)
        dirty = [rel for xy, rel in entries if safety.is_allowed(rel)]
        ignored = [rel for xy, rel in entries if xy == "??" and not safety.is_allowed(rel)]
        s = state.read("sync", {})
        merged = state.read("merged", {})
        st = "ok"
        msg = "clean" if not dirty else f"{len(dirty)} file(s) waiting to be committed"
        if br != repo.branch:
            st, msg = "wrong-branch", f"on '{br or 'detached HEAD'}', expected '{repo.branch}'"
        holder = FileLock(config.state_path("locks", "git.lock")).holder()
        if info.get("upstream") == f"{repo.remote}/{repo.branch}" and info.get("behind") is not None:
            behind = info["behind"]
        else:
            behind = repo.behind()
        return _result(
            st, msg,
            ok=(st == "ok"),
            head=repo.head(), unpushed=repo.ahead(), blocked=_blocked_now(),
            merged_both_sides=[p for p in merged.get("files", []) if isinstance(p, str)],
            changed_files=list(s.get("changed_files", [])),
            branch=br, behind=behind, dirty=dirty, ignored_untracked=ignored,
            in_progress=in_progress, lock_held=holder is not None,
            last_fetch_at=s.get("last_fetch_at"), last_pull_ok_at=s.get("last_pull_ok_at"),
            last_push_ok_at=s.get("last_push_ok_at"),
            last_sync_status=s.get("status"), last_sync_message=s.get("message"),
            remote_url=repo.remote_url(), brain_dir=str(repo.dir), state_dir=str(config.state_dir()),
        )
    except Exception as e:
        return _result("error", f"status failed: {type(e).__name__}: {e}")
