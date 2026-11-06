"""Machine-local configuration for the MockMob team brain.

``STATE_DIR`` is ``$MOCKMOB_BRAIN_STATE`` or ``~/.mockmob-brain``. It is read at
access time (module ``__getattr__``), so tests and tools may switch the
environment variable between calls. Assigning ``config.STATE_DIR = path``
explicitly overrides the environment.
"""
from __future__ import annotations

import json
import os
import re
import sys
import time
import uuid
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

IS_WINDOWS = os.name == "nt"
CONFIG_VERSION = 1


def state_dir() -> Path:
    override = globals().get("STATE_DIR")  # explicit assignment wins
    if override:
        return Path(override)
    env = os.environ.get("MOCKMOB_BRAIN_STATE")
    if env:
        return Path(os.path.expanduser(env))
    return Path.home() / ".mockmob-brain"


def __getattr__(name: str):  # PEP 562: dynamic STATE_DIR
    if name == "STATE_DIR":
        return state_dir()
    raise AttributeError(name)


def state_path(*parts: str) -> Path:
    """``STATE_DIR/<parts...>``; creates the parent directories."""
    p = state_dir().joinpath(*parts)
    p.parent.mkdir(parents=True, exist_ok=True)
    return p


def config_file() -> Path:
    return state_dir() / "config.json"


# --------------------------------------------------------------------------
# Config
# --------------------------------------------------------------------------
def _default_brain_dir() -> Path:
    here = Path(__file__).resolve()
    for parent in here.parents:
        if (parent / ".git").exists():
            return parent
    return here.parents[2]  # <brain>/.brain/brainlib/config.py


def slugify(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", (text or "").strip().lower()).strip("-")
    return s or "unknown"


@dataclass
class Config:
    version: int = CONFIG_VERSION
    person: str = ""
    display_name: str = ""
    role: str = "member"
    email: str = ""
    brain_dir: Path = field(default_factory=_default_brain_dir)
    code_dirs: list = field(default_factory=list)
    memory_dirs: list = field(default_factory=list)
    branch: str = "main"
    remote: str = "origin"
    mode: str = "standalone"
    vectors: bool = True
    python: str = ""
    extra: dict = field(default_factory=dict)  # unknown keys, preserved on save

    def to_json(self) -> dict:
        d = {
            "version": self.version,
            "person": self.person,
            "display_name": self.display_name,
            "role": self.role,
            "email": self.email,
            "brain_dir": str(self.brain_dir),
            "code_dirs": [str(p) for p in self.code_dirs],
            "memory_dirs": [str(p) for p in self.memory_dirs],
            "branch": self.branch,
            "remote": self.remote,
            "mode": self.mode,
            "vectors": self.vectors,
            "python": self.python,
        }
        for k, v in self.extra.items():
            d.setdefault(k, v)
        return d


def _path_list(value) -> list:
    out = []
    for item in value or []:
        if isinstance(item, (str, os.PathLike)) and str(item).strip():
            out.append(Path(os.path.expanduser(str(item))))
    return out


def _git_config_value(key: str, cwd: Path | None) -> str:
    try:
        from . import gitops

        r = gitops.run(["config", "--get", key], cwd=cwd if cwd and cwd.exists() else Path.cwd(), timeout=5)
        return r.out.strip() if r.ok else ""
    except Exception:
        return ""


def load() -> Config:
    """Load ``config.json``; a missing or broken file yields defaults."""
    raw: dict = {}
    try:
        with open(config_file(), "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, dict):
            raw = data
    except (OSError, ValueError):
        raw = {}

    env_brain = os.environ.get("MOCKMOB_BRAIN")
    if env_brain:
        brain_dir = Path(os.path.expanduser(env_brain))
    elif raw.get("brain_dir"):
        brain_dir = Path(os.path.expanduser(str(raw["brain_dir"])))
    else:
        brain_dir = _default_brain_dir()

    known = {
        "version", "person", "display_name", "role", "email", "brain_dir", "code_dirs",
        "memory_dirs", "branch", "remote", "mode", "vectors", "python",
    }
    cfg = Config(
        version=int(raw.get("version") or CONFIG_VERSION),
        person=str(raw.get("person") or ""),
        display_name=str(raw.get("display_name") or ""),
        role=str(raw.get("role") or "member"),
        email=str(raw.get("email") or ""),
        brain_dir=brain_dir,
        code_dirs=_path_list(raw.get("code_dirs")),
        memory_dirs=_path_list(raw.get("memory_dirs")),
        branch=str(raw.get("branch") or "main"),
        remote=str(raw.get("remote") or "origin"),
        mode=str(raw.get("mode") or "standalone"),
        vectors=bool(raw.get("vectors", True)),
        python=str(raw.get("python") or ""),
        extra={k: v for k, v in raw.items() if k not in known},
    )
    if not cfg.person or not cfg.display_name or not cfg.email:
        git_name = _git_config_value("user.name", brain_dir)
        if not cfg.person:
            cfg.person = slugify(git_name) if git_name else slugify(_os_user())
        if not cfg.display_name:
            cfg.display_name = git_name or cfg.person
        if not cfg.email:
            cfg.email = _git_config_value("user.email", brain_dir) or f"{cfg.person}@users.noreply.local"
    if not cfg.python:
        cfg.python = sys.executable
    return cfg


def _os_user() -> str:
    try:
        import getpass

        return getpass.getuser()
    except Exception:
        return "unknown"


def save(cfg: Config) -> None:
    """Atomically write ``config.json``."""
    p = config_file()
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_name(f"{p.name}.tmp-{os.getpid()}-{uuid.uuid4().hex[:8]}")
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        json.dump(cfg.to_json(), f, indent=2, ensure_ascii=False)
    for attempt in range(15):
        try:
            os.replace(tmp, p)
            return
        except PermissionError:
            time.sleep(0.02 * (attempt + 1))
    os.replace(tmp, p)


# --------------------------------------------------------------------------
# cwd classification
# --------------------------------------------------------------------------
def _norm(p) -> str:
    return os.path.normcase(os.path.normpath(os.path.abspath(str(p))))


def _under(child: str, parent: str) -> bool:
    if not parent:
        return False
    return child == parent or child.startswith(parent.rstrip("\\/") + os.sep)


def find_git_root(start) -> Path | None:
    """Nearest ancestor (or self) that contains ``.git`` (dir or file)."""
    p = Path(os.path.abspath(str(start)))
    for cand in [p, *p.parents]:
        try:
            if (cand / ".git").exists():
                return cand
        except OSError:
            continue
    return None


def _git_dir_of(root: Path) -> Path | None:
    dot = root / ".git"
    try:
        if dot.is_dir():
            return dot
        if dot.is_file():
            text = dot.read_text(encoding="utf-8", errors="replace").strip()
            if text.lower().startswith("gitdir:"):
                gd = Path(text.split(":", 1)[1].strip())
                if not gd.is_absolute():
                    gd = (root / gd).resolve()
                return gd
    except OSError:
        pass
    return None


def _common_dir(gitdir: Path) -> Path:
    try:
        cd = gitdir / "commondir"
        if cd.is_file():
            rel = cd.read_text(encoding="utf-8", errors="replace").strip()
            p = Path(rel)
            return p if p.is_absolute() else (gitdir / p).resolve()
    except OSError:
        pass
    return gitdir


def remote_url(root, name: str = "origin") -> str:
    """URL of remote ``name`` for the repo at ``root``, read from .git/config (no subprocess)."""
    gd = _git_dir_of(Path(root))
    if gd is None:
        return ""
    cfg_file = _common_dir(gd) / "config"
    try:
        text = cfg_file.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""
    in_remote = False
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("["):
            m = re.match(r'^\[remote\s+"([^"]*)"\]', s, re.I)
            in_remote = bool(m) and m.group(1) == name
            continue
        if in_remote:
            m = re.match(r"^url\s*=\s*(.+)$", s, re.I)
            if m:
                return m.group(1).strip()
    return ""


def origin_url(root: Path) -> str:
    """The ``origin`` URL of the repo at ``root``."""
    return remote_url(root, "origin")


# Public names for the git-dir helpers (sync.py reads refs and HEAD without spawning git).
def git_dir_of(root) -> Path | None:
    return _git_dir_of(Path(root))


def common_dir(gitdir) -> Path:
    return _common_dir(Path(gitdir))


def _is_mockmob_url(url: str) -> bool:
    low = url.lower().replace("\\", "/")
    return "atishay07/mockmob" in low and "mockmob-brain" not in low


def _cache_read() -> dict:
    try:
        with open(state_path("state", "cwd-cache.json"), "r", encoding="utf-8") as f:
            d = json.load(f)
        return d if isinstance(d, dict) else {}
    except (OSError, ValueError):
        return {}


def _cache_write(cache: dict) -> None:
    try:
        if len(cache) > 400:
            items = sorted(cache.items(), key=lambda kv: kv[1].get("at", 0), reverse=True)[:300]
            cache = dict(items)
        from . import state

        state.write("cwd-cache", cache)
    except Exception:
        pass


def is_mockmob_cwd(cwd, cfg: Config | None = None) -> bool:
    """True if ``cwd`` is in the brain, a configured code dir, or a MockMob code checkout."""
    if not cwd:
        return False
    cfg = cfg or load()
    c = _norm(cwd)
    roots = [_norm(cfg.brain_dir), *[_norm(d) for d in cfg.code_dirs]]
    if any(_under(c, r) for r in roots):
        return True
    try:
        real = _norm(os.path.realpath(str(cwd)))
        if real != c and any(_under(real, r) for r in roots):
            return True
    except OSError:
        pass
    # Origin check (cached; answered from .git/config, no subprocess).
    now = time.time()
    cache = _cache_read()
    hit = cache.get(c)
    if isinstance(hit, dict) and now - float(hit.get("at", 0)) < (30 * 86400 if hit.get("v") else 3600):
        return bool(hit.get("v"))
    answer = False
    root = find_git_root(cwd)
    if root is not None:
        url = origin_url(root)
        answer = _is_mockmob_url(url)
    cache[c] = {"v": answer, "at": now}
    _cache_write(cache)
    return answer


def _read_head_branch(root: Path) -> str:
    gd = _git_dir_of(root)
    if gd is None:
        return ""
    try:
        head = (gd / "HEAD").read_text(encoding="utf-8", errors="replace").strip()
    except OSError:
        return ""
    if head.startswith("ref:"):
        ref = head.split(":", 1)[1].strip()
        return ref[len("refs/heads/"):] if ref.startswith("refs/heads/") else ref
    return "HEAD"  # detached


def repo_relative(path) -> tuple[str, str, str] | None:
    """For a file in a MockMob code checkout: ``(repo_slug, branch, relpath)``.

    ``repo_slug`` is the repository name from the origin URL (``mockmob`` for
    ``atishay07/mockmob``), or the checkout folder name when there is no origin.
    ``relpath`` is POSIX-style and relative to the checkout root. Returns None
    when the file is not inside a MockMob code checkout.
    """
    try:
        p = Path(os.path.abspath(str(path)))
    except (OSError, ValueError):
        return None
    root = find_git_root(p if p.is_dir() else p.parent)
    if root is None:
        return None
    cfg = load()
    tl = _norm(root)
    cache = _cache_read()
    key = "root:" + tl
    hit = cache.get(key)
    info = None
    if isinstance(hit, dict) and time.time() - float(hit.get("at", 0)) < 86400:
        info = hit
    if info is None:
        url = origin_url(root)
        is_code = _is_mockmob_url(url) or any(_under(tl, _norm(d)) for d in cfg.code_dirs)
        if tl == _norm(cfg.brain_dir):
            is_code = False  # the brain repo itself is not a code checkout
        slug = ""
        if url:
            slug = re.sub(r"\.git$", "", url.rstrip("/\\").replace("\\", "/").rsplit("/", 1)[-1].rsplit(":", 1)[-1])
        info = {"v": is_code, "slug": slug or root.name.lower(), "at": time.time()}
        cache[key] = info
        _cache_write(cache)
    if not info.get("v"):
        return None
    try:
        rel = os.path.relpath(str(p), str(root)).replace("\\", "/")
    except ValueError:
        return None
    if rel.startswith(".."):
        return None
    return (info["slug"], _read_head_branch(root), rel)
