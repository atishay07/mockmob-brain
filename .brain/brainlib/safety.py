"""What may be committed automatically: path allowlist, path sanity, secret scan, size/binary checks."""
from __future__ import annotations

import os
import re
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Iterable

MAX_FILE_BYTES = 2 * 1024 * 1024
MAX_PATH_LEN = 180
IMAGE_EXTS = (".png", ".jpg", ".jpeg", ".webp")

_ALLOWED_DIRS = ("docs", "context", "handoffs", "playbook", "claims", "conflicts", ".brain")
_ALLOWED_FILES = {
    "TEAM.md", "README.md", "AGENTS.md", "CLAUDE.md", ".gitattributes", ".gitignore",
}
_RESERVED = {"CON", "PRN", "AUX", "NUL"} | {f"COM{i}" for i in range(1, 10)} | {f"LPT{i}" for i in range(1, 10)}
_BAD_CHARS = set('<>:"|?*')


def norm_rel(relpath) -> str:
    """POSIX-style relative path without a leading ``./``."""
    s = str(relpath).replace("\\", "/")
    while s.startswith("./"):
        s = s[2:]
    return s


def is_allowed(relpath) -> bool:
    """True if the path may be staged automatically (see DESIGN.md section 2)."""
    s = norm_rel(relpath)
    if not s or s.startswith("/") or re.match(r"^[A-Za-z]:", s):
        return False
    parts = [p for p in s.split("/") if p != ""]
    if not parts or any(p in (".", "..") for p in parts):
        return False
    if any(p == "__pycache__" for p in parts) or parts[-1].endswith(".pyc"):
        return False
    if len(parts) == 1:
        return parts[0] in _ALLOWED_FILES
    top = parts[0]
    if top == ".brain":
        return not (len(parts) >= 2 and parts[1] == "cache")
    return top in _ALLOWED_DIRS


# --------------------------------------------------------------------------
# path sanity
# --------------------------------------------------------------------------
def tracked_paths(cwd) -> list[str]:
    """Paths tracked in the repo at ``cwd`` (via git ls-files)."""
    from . import gitops

    r = gitops.run(["--no-optional-locks", "ls-files", "-z"], cwd=cwd, timeout=20)
    if not r.ok:
        return []
    return [p for p in r.out.split("\0") if p]


def check_path(relpath, tracked: Iterable[str] | None = None, repo=None) -> list[str]:
    """Reasons this path cannot be committed safely on every OS (empty list = fine).

    ``tracked`` is the list of already-tracked paths used for the case-only collision
    check; when omitted it is read from the repo at ``repo`` (default: the configured
    brain dir).
    """
    s = norm_rel(relpath)
    reasons: list[str] = []
    if len(s) > MAX_PATH_LEN:
        reasons.append(f"path too long ({len(s)} > {MAX_PATH_LEN} characters)")
    for seg in s.split("/"):
        if seg == "":
            continue
        base = seg.split(".")[0].rstrip(" ").upper()
        if base in _RESERVED:
            reasons.append(f"reserved Windows name '{seg}'")
        bad = sorted({c for c in seg if c in _BAD_CHARS or ord(c) < 32 or ord(c) == 127})
        if bad:
            shown = "".join(c if ord(c) >= 32 else f"\\x{ord(c):02x}" for c in bad)
            reasons.append(f"invalid character(s) {shown!r} in '{seg}'")
        if seg.endswith(".") or seg.endswith(" "):
            reasons.append(f"segment '{seg}' ends with a dot or space")
    if tracked is None:
        try:
            if repo is None:
                from . import config

                repo = config.load().brain_dir
            tracked = tracked_paths(repo)
        except Exception:
            tracked = []
    collision = _case_collision(s, tracked)
    if collision:
        reasons.append(f"case-only collision with tracked path '{collision}'")
    # de-duplicate, keep order
    seen = set()
    return [r for r in reasons if not (r in seen or seen.add(r))]


def _case_collision(rel: str, tracked: Iterable[str]) -> str | None:
    """A tracked path (or one of its directories) that differs from ``rel`` in case only."""
    parts = rel.split("/")
    for t in tracked:
        tp = norm_rel(t).split("/")
        for n in range(1, min(len(tp), len(parts)) + 1):
            if tp[n - 1] == parts[n - 1]:
                continue
            if tp[n - 1].lower() == parts[n - 1].lower():
                return "/".join(tp[:n])
            break
    return None


# --------------------------------------------------------------------------
# secret scan
# --------------------------------------------------------------------------
@dataclass(frozen=True)
class Finding:
    kind: str
    line: int
    excerpt: str


_PLACEHOLDER_RE = re.compile(
    r"xxx|<[^>]*>|your[-_ ]|example|redacted|placeholder|\.\.\.|\*\*\*|changeme|process\.env|os\.environ|getenv",
    re.I,
)

# (kind, compiled regex, group holding the secret value or 0 for the whole match)
_RULES: list[tuple[str, re.Pattern, int]] = [
    ("private-key", re.compile(r"-----BEGIN [A-Z0-9 ]*PRIVATE KEY-----.*?(?:-----END [A-Z0-9 ]*PRIVATE KEY-----|\Z)", re.S), 0),
    ("anthropic-key", re.compile(r"(?<![A-Za-z0-9])sk-ant-[A-Za-z0-9_\-]{20,}"), 0),
    ("openai-key", re.compile(r"(?<![A-Za-z0-9])sk-proj-[A-Za-z0-9_\-]{20,}"), 0),
    ("secret-key", re.compile(r"(?<![A-Za-z0-9])sk-[A-Za-z0-9_\-]{20,}"), 0),
    ("github-token", re.compile(r"(?<![A-Za-z0-9])(?:ghp_|gho_|github_pat_)[A-Za-z0-9_]{20,}"), 0),
    ("aws-key", re.compile(r"(?<![A-Za-z0-9])AKIA[0-9A-Z]{16}(?![A-Za-z0-9])"), 0),
    ("slack-token", re.compile(r"xox[abp]-[A-Za-z0-9\-]{10,}"), 0),
    ("razorpay-key", re.compile(r"rzp_(?:live|test)_[A-Za-z0-9]{10,}"), 0),
    # JWT: header starting eyJ, then two more base64url segments of 10+ chars, any total length
    ("jwt", re.compile(r"eyJ[A-Za-z0-9_\-]{5,}\.[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}"), 0),
    ("supabase-token", re.compile(r"(?<![A-Za-z0-9])sbp_[A-Za-z0-9]{20,}"), 0),
    ("google-api-key", re.compile(r"AIza[0-9A-Za-z_\-]{35}"), 0),
    ("pem-header", re.compile(r"-----BEGIN [A-Z0-9 ]+-----"), 0),
]


# Env-style assignments: NAME=value / name: "value" where the name says "secret".
_ASSIGN_RE = re.compile(
    r"""(?<![A-Za-z0-9_\-])([A-Za-z][A-Za-z0-9_\-]{1,80})["']?[ 	]*[=:][ 	]*["']?([A-Za-z0-9_\-+/=.]{16,})"""
)
_NAME_SPLIT_RE = re.compile(r"[_\-]+|(?<=[a-z0-9])(?=[A-Z])")
_KEY_WORDS = {"KEY", "SECRET", "TOKEN", "PASSWORD", "PASSWD", "PRIVATE", "CREDENTIAL", "CREDENTIALS", "APIKEY"}
_KEY_SUFFIXES = ("SECRET", "TOKEN", "PASSWORD", "PASSWD", "CREDENTIAL", "CREDENTIALS", "APIKEY")
_NOT_A_SECRET_LAST = {
    "PATH", "FILE", "DIR", "URL", "URI", "TYPE", "NAME", "FIELD", "HEADER", "LABEL", "ENV", "VAR",
    "VARIABLE", "LENGTH", "COUNT", "LIMIT", "TTL", "EXPIRES", "EXPIRY", "ID", "ENDPOINT", "HINT",
    "PROMPT", "POLICY",
}
_IDENT_VALUE_RES = (
    re.compile(r"[a-z][a-z0-9]*(?:\.[a-z_][a-z0-9_]*)+"),  # request.headers.authorization
    re.compile(r"[a-z]+(?:_[a-z]+)+"),  # some_variable_name
)


def _is_secret_name(name: str) -> bool:
    """KEY, SECRET, TOKEN, PASSWORD, PASSWD, PRIVATE or CREDENTIAL as a whole word of the name
    (split on ``_``, ``-`` and camelCase: SUPABASE_SERVICE_ROLE_KEY, apiKey, clientSecret)."""
    if re.search(r"service[_\-]?role", name, re.I):
        return True
    words = [w.upper() for w in _NAME_SPLIT_RE.split(name) if w]
    if not words:
        return False
    hit = any(w in _KEY_WORDS or w.endswith(_KEY_SUFFIXES) for w in words)
    if not hit:
        return False
    last = words[-1]
    return not (last in _NOT_A_SECRET_LAST and last not in _KEY_WORDS)


def _assignment_spans(text: str) -> list[tuple[int, int, str]]:
    out = []
    for m in _ASSIGN_RE.finditer(text):
        name, value = m.group(1), m.group(2)
        if not _is_secret_name(name):
            continue
        if value.startswith(("/", "./", "../")) or any(r.fullmatch(value) for r in _IDENT_VALUE_RES):
            continue
        out.append((m.start(2), m.end(2), value))
    return out


def _spans(text: str) -> list[tuple[str, int, int, str]]:
    """Non-overlapping (kind, start, end, matched_secret) in document order."""
    found: list[tuple[str, int, int, str]] = []
    taken: list[tuple[int, int]] = []

    def add(kind: str, s: int, e: int, matched: str) -> None:
        if _PLACEHOLDER_RE.search(matched):
            return
        if any(s < te and e > ts for ts, te in taken):
            return
        taken.append((s, e))
        found.append((kind, s, e, matched))

    for kind, rx, grp in _RULES:
        for m in rx.finditer(text):
            s, e = m.span(grp) if grp else m.span()
            add(kind, s, e, text[s:e])
    for s, e, value in _assignment_spans(text):
        add("generic-secret", s, e, value)
    found.sort(key=lambda x: x[1])
    return found


def redact(text: str) -> str:
    """Replace every secret-looking match with ``[REDACTED]``."""
    if not text:
        return text
    out = []
    last = 0
    for _kind, s, e, _m in _spans(text):
        out.append(text[last:s])
        out.append("[REDACTED]")
        last = e
    out.append(text[last:])
    return "".join(out)


def scan_text(text: str) -> list[Finding]:
    """Secret findings with a 1-based line number and a redacted excerpt."""
    if not text:
        return []
    spans = _spans(text)
    if not spans:
        return []
    line_starts = [0]
    for m in re.finditer(r"\n", text):
        line_starts.append(m.end())

    def line_of(pos: int) -> int:
        lo, hi = 0, len(line_starts) - 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if line_starts[mid] <= pos:
                lo = mid
            else:
                hi = mid - 1
        return lo + 1

    lines = text.split("\n")
    findings: list[Finding] = []
    for kind, s, _e, _m in spans:
        ln = line_of(s)
        raw = lines[ln - 1] if ln - 1 < len(lines) else ""
        excerpt = redact(raw).strip()
        if len(excerpt) > 140:
            excerpt = excerpt[:137] + "..."
        findings.append(Finding(kind, ln, excerpt))
    return findings


# --------------------------------------------------------------------------
# file content checks
# --------------------------------------------------------------------------
def check_bytes(relpath, data: bytes) -> list[dict]:
    """Blocking problems with this file's content: ``[{"reason": str, "line": int|None}]``."""
    rel = norm_rel(relpath)
    ext = PurePosixPath(rel).suffix.lower()
    size = len(data)
    if size > MAX_FILE_BYTES:
        return [{"reason": f"file too large ({size / 1048576:.1f} MB, limit 2 MB)", "line": None}]
    if ext in IMAGE_EXTS and rel.startswith("docs/"):
        return []
    if b"\0" in data:
        return [{"reason": "binary file (not text)", "line": None}]
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        return [{"reason": "not valid UTF-8 text", "line": None}]
    return [{"reason": f"secret: {f.kind}", "line": f.line, "excerpt": f.excerpt} for f in scan_text(text)]


def check_file(path, relpath=None) -> list[dict]:
    """Like :func:`check_bytes` for a file on disk (reads at most 2 MB + 1 byte)."""
    p = Path(path)
    rel = norm_rel(relpath if relpath is not None else p.name)
    try:
        size = p.stat().st_size
        if size > MAX_FILE_BYTES:
            return [{"reason": f"file too large ({size / 1048576:.1f} MB, limit 2 MB)", "line": None}]
        with open(p, "rb") as f:
            data = f.read(MAX_FILE_BYTES + 1)
    except OSError as e:
        return [{"reason": f"cannot read file: {e.strerror or e}", "line": None}]
    return check_bytes(rel, data)
