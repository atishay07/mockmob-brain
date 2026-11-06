"""Test helper: a temporary bare "GitHub" remote with an initial commit plus N clones.

Each clone has its own ``MOCKMOB_BRAIN_STATE`` directory and ``config.json``. Nothing
touches the network, the real STATE_DIR or the user's git config.

    fx = make_fixture(n_clones=2)          # in a TestCase: self.addCleanup(fx.cleanup)
    a, b = fx.clones
    a.write("docs/NOW.md", "...")
    res = a.sync(force=True)               # runs brainlib.sync.sync() with a's environment
    with b.active():                       # or switch the environment yourself
        res = sync.pull(force=True)

Import order: ``import _gitfixture`` first (it puts ``.brain`` on ``sys.path``), then
``from brainlib import ...``.
"""
from __future__ import annotations

import contextlib
import json
import os
import shutil
import stat
import subprocess
import sys
import tempfile
import uuid
from pathlib import Path

BRAIN_DOT = Path(__file__).resolve().parents[1]  # <repo>/.brain
if str(BRAIN_DOT) not in sys.path:
    sys.path.insert(0, str(BRAIN_DOT))

from brainlib import gitops  # noqa: E402

GITATTRIBUTES_TEXT = """* text=auto eol=lf

# Prose that several people append to: keep both sides' lines instead of stopping on a clash.
docs/** merge=union
context/** merge=union
playbook/** merge=union
TEAM.md merge=union

# JSON must stay valid: never union-merge it. A real clash stops the rebase and the sync
# saves a conflict copy instead.
*.json merge=text
"""

SEED_FILES = {
    ".gitattributes": GITATTRIBUTES_TEXT,
    "README.md": "# test brain\n",
    "TEAM.md": "# Team\n\n- alice (owner)\n- bob (cto)\n",
    "docs/NOW.md": "# NOW\n\nline one\nline two\nline three\n",
    "docs/STATUS.md": "# STATUS\n\n## 6 Nov\n\nall good\n",
    "context/working-rules.md": "# Working rules\n\n## Standing rules\n\n- be kind\n",
    "handoffs/mockmob/README.md": "handovers go here\n",
}


def rmtree_force(path) -> None:
    """Remove a tree even when git left read-only files (Windows)."""

    def _onerror(func, p, _exc):
        try:
            os.chmod(p, stat.S_IWRITE)
            func(p)
        except OSError:
            pass

    shutil.rmtree(path, onerror=_onerror)


class Clone:
    def __init__(self, fixture: "Fixture", name: str, path: Path, state_dir: Path):
        self.fixture = fixture
        self.name = name
        self.person = name
        self.path = path
        self.state_dir = state_dir

    # -- environment ----------------------------------------------------
    def env_vars(self) -> dict:
        return {
            "MOCKMOB_BRAIN_STATE": str(self.state_dir),
            "MOCKMOB_BRAIN": str(self.path),
            "GIT_CONFIG_GLOBAL": str(self.fixture.empty_gitconfig),
            "GIT_CONFIG_NOSYSTEM": "1",
        }

    def subprocess_env(self, extra: dict | None = None) -> dict:
        env = dict(os.environ)
        env.update(self.env_vars())
        if extra:
            env.update(extra)
        return env

    @contextlib.contextmanager
    def active(self, **extra):
        """Point this process's environment at this clone (restored on exit)."""
        updates = {**self.env_vars(), **{k: str(v) for k, v in extra.items()}}
        saved = {k: os.environ.get(k) for k in updates}
        os.environ.update(updates)
        try:
            yield self
        finally:
            for k, v in saved.items():
                if v is None:
                    os.environ.pop(k, None)
                else:
                    os.environ[k] = v

    # -- git + files ------------------------------------------------------
    def git(self, *args, timeout: float = 60) -> gitops.Result:
        return gitops.run(list(args), cwd=self.path, timeout=timeout, env=self.env_vars())

    def must_git(self, *args) -> str:
        r = self.git(*args)
        if not r.ok:
            raise AssertionError(f"git {' '.join(args)} failed in {self.name}: {r.err.strip()}")
        return r.out

    def abs(self, rel: str) -> Path:
        return self.path / rel

    def write(self, rel: str, content="", binary: bool = False) -> Path:
        p = self.path / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(content, bytes):
            p.write_bytes(content)
        else:
            p.write_bytes(content.encode("utf-8"))
        return p

    def read(self, rel: str) -> str:
        return (self.path / rel).read_text(encoding="utf-8")

    def exists(self, rel: str) -> bool:
        return (self.path / rel).exists()

    def head(self) -> str:
        return self.must_git("rev-parse", "HEAD").strip()

    def log_subjects(self, n: int = 10) -> list[str]:
        return self.must_git("log", f"-{n}", "--format=%s").splitlines()

    def tracked(self) -> set[str]:
        return {p for p in self.must_git("ls-files", "-z").split("\0") if p}

    def set_remote_url(self, url: str) -> None:
        self.must_git("remote", "set-url", "origin", str(url))

    def refs(self, pattern: str) -> list[str]:
        return [l.split()[-1] for l in self.must_git("for-each-ref", pattern).splitlines() if l.strip()]

    def handover(self, task: str, stamp: str | None = None) -> str:
        """Write a minimal handover pair like handoff.write would; returns the json relpath."""
        sid = uuid.uuid4().hex[:8]
        stem = f"{stamp or '20261106T120000.000000Z'}-{sid}"
        rel = f"handoffs/mockmob/{stem}.json"
        self.write(rel, json.dumps({"id": sid, "task": task, "agent": "test", "person": self.person}, indent=2) + "\n")
        self.write(f"handoffs/mockmob/{stem}.md", f"---\ntitle: {task}\n---\n\n## task\n\n{task}\n")
        return rel

    # -- convenience wrappers around brainlib.sync --------------------------
    def sync(self, **kw) -> dict:
        from brainlib import sync

        with self.active():
            return sync.sync(**kw)

    def pull(self, **kw) -> dict:
        from brainlib import sync

        with self.active():
            return sync.pull(**kw)

    def push(self, **kw) -> dict:
        from brainlib import sync

        with self.active():
            return sync.push(**kw)

    def commit_pending(self, *a, **kw) -> dict:
        from brainlib import sync

        with self.active():
            return sync.commit_pending(*a, **kw)

    def status(self) -> dict:
        from brainlib import sync

        with self.active():
            return sync.status()

    def state_json(self, name: str) -> dict:
        p = self.state_dir / "state" / (name if name.endswith(".json") else name + ".json")
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            return {}


class Fixture:
    def __init__(self, root: Path):
        self.root = root
        self.remote = root / "remote.git"
        self.empty_gitconfig = root / "empty.gitconfig"
        self.empty_gitconfig.write_text("", encoding="utf-8")
        self.clones: list[Clone] = []

    def remote_git(self, *args, timeout: float = 60) -> gitops.Result:
        return gitops.run(list(args), cwd=self.remote, timeout=timeout, env=self.git_env())

    def git_env(self) -> dict:
        return {"GIT_CONFIG_GLOBAL": str(self.empty_gitconfig), "GIT_CONFIG_NOSYSTEM": "1"}

    def remote_files(self, ref: str = "main") -> set[str]:
        r = self.remote_git("ls-tree", "-r", "--name-only", "-z", ref)
        return {p for p in r.out.split("\0") if p} if r.ok else set()

    def remote_show(self, path: str, ref: str = "main") -> str | None:
        r = self.remote_git("show", f"{ref}:{path}")
        return r.out if r.ok else None

    def remote_log(self, n: int = 20) -> list[str]:
        return self.remote_git("log", f"-{n}", "--format=%s", "main").out.splitlines()

    def remote_commit_count(self) -> int:
        return int(self.remote_git("rev-list", "--count", "main").out.strip() or 0)

    def add_clone(self, name: str) -> Clone:
        path = self.root / name
        state_dir = self.root / f"{name}-state"
        state_dir.mkdir(parents=True, exist_ok=True)
        r = gitops.run(["clone", "-q", str(self.remote), str(path)], cwd=self.root, timeout=120, env=self.git_env())
        if not r.ok:
            raise RuntimeError(f"clone failed: {r.err}")
        clone = Clone(self, name, path, state_dir)
        for k, v in (
            ("user.name", name.capitalize()),
            ("user.email", f"{name}@example.test"),
            ("pull.rebase", "true"),
            ("rebase.autoStash", "true"),
            ("core.autocrlf", "false"),
            ("core.longpaths", "true"),
            ("fetch.prune", "true"),
        ):
            clone.must_git("config", k, v)
        cfg = {
            "version": 1,
            "person": name,
            "display_name": name.capitalize(),
            "role": "member",
            "email": f"{name}@example.test",
            "brain_dir": str(path),
            "code_dirs": [],
            "memory_dirs": [],
            "branch": "main",
            "remote": "origin",
            "mode": "standalone",
            "vectors": False,
            "python": sys.executable,
        }
        (state_dir / "config.json").write_text(json.dumps(cfg, indent=2), encoding="utf-8")
        self.clones.append(clone)
        return clone

    def cleanup(self) -> None:
        rmtree_force(self.root)

    def __enter__(self) -> "Fixture":
        return self

    def __exit__(self, *exc) -> None:
        self.cleanup()


def make_fixture(n_clones: int = 2, names=("alice", "bob", "carol", "dave"), seed_files: dict | None = None,
                 prefix: str = "mmb-") -> Fixture:
    """A bare remote with one initial commit (``.gitattributes`` first) and ``n_clones`` clones."""
    root = Path(tempfile.mkdtemp(prefix=prefix, dir=tempfile.gettempdir()))
    fx = Fixture(root)
    try:
        env = fx.git_env()
        r = gitops.run(["init", "-q", "--bare", "-b", "main", str(fx.remote)], cwd=root, timeout=60, env=env)
        if not r.ok:
            raise RuntimeError(f"git init --bare failed: {r.err}")
        seed = root / "seed"
        for args in (
            ["clone", "-q", str(fx.remote), str(seed)],
        ):
            r = gitops.run(args, cwd=root, timeout=60, env=env)
            if not r.ok and "empty repository" not in r.err:
                raise RuntimeError(f"seed clone failed: {r.err}")
        gitops.run(["checkout", "-q", "-B", "main"], cwd=seed, timeout=30, env=env)
        for rel, text in {**SEED_FILES, **(seed_files or {})}.items():
            p = seed / rel
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(text.encode("utf-8") if isinstance(text, str) else text)
        steps = [
            ["add", "-A"],
            ["-c", "user.name=Seed", "-c", "user.email=seed@example.test", "-c", "commit.gpgsign=false",
             "commit", "-q", "-m", "brain: initial"],
            ["push", "-q", "origin", "main"],
        ]
        for args in steps:
            r = gitops.run(args, cwd=seed, timeout=60, env=env)
            if not r.ok:
                raise RuntimeError(f"seed step {args[0]} failed: {r.err}")
        rmtree_force(seed)
        for i in range(n_clones):
            fx.add_clone(names[i] if i < len(names) else f"user{i}")
    except Exception:
        fx.cleanup()
        raise
    return fx
