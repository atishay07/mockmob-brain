"""MockMob team brain search: one SQLite file, FTS5 keyword search, optional local vectors.

Port of Continuum's apps/rag/rag.py (same ranking: FTS5 BM25 + bge-small-en-v1.5 vectors through fastembed,
reciprocal rank fusion, exact-literal route, freshness metadata, incremental index, budgeted inline refresh,
detached embed worker with its own lock). Only the corpus and the storage locations differ.

Corpus (project "mockmob" for everything, read only, never written):
  * brain repo: every *.md under docs/, context/, handoffs/mockmob/, playbook/ plus TEAM.md, AGENTS.md, README.md.
    Doc ids are "brain/<relative path>".
  * each code dir: root AGENTS.md, CLAUDE.md, DESIGN.md, PRODUCT.md, README.md and docs/**/*.md except docs/brain/**.
    Doc ids are "mockmob/<relative path>".

Storage: STATE_DIR/index/rag.sqlite (STATE_DIR = env MOCKMOB_BRAIN_STATE or ~/.mockmob-brain); model cache in
STATE_DIR/models unless env MOCKMOB_BRAIN_MODELS is set.

fastembed, numpy and truststore are imported lazily. Without fastembed, everything works in keyword mode and
vectors_status says "keyword only". Set MOCKMOB_BRAIN_NO_VECTORS=1 to force that.

This module is self-contained (stdlib only) on purpose: the embed worker runs it as a plain script.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import re
import sqlite3
import subprocess
import sys
import time
import warnings
from datetime import datetime, timezone
from pathlib import Path

EMBED_MODEL = os.environ.get("RAG_EMBED_MODEL", "BAAI/bge-small-en-v1.5")
QUERY_PREFIX = "Represent this sentence for searching relevant passages: "

BRAIN_FOLDERS = ("docs", "context", "handoffs/mockmob", "playbook")
BRAIN_TOP_FILES = ("TEAM.md", "AGENTS.md", "README.md")
CODE_TOP_FILES = ("AGENTS.md", "CLAUDE.md", "DESIGN.md", "PRODUCT.md", "README.md")
# Never indexed: env files, key material, dependency and build folders. Secret-looking content is also skipped.
SKIP_PATH_PARTS = {"node_modules", ".git", "dist", "build", ".next"}
SKIP_NAME_RE = re.compile(r"(^\.env|\.pem$|\.key$|\.p12$|\.pfx$|id_rsa|\.keystore$)", re.I)
SECRET_CONTENT_RE = re.compile(
    r"(-----BEGIN [A-Z ]*PRIVATE KEY-----|sk-[A-Za-z0-9_-]{20,}|ghp_[A-Za-z0-9]{30,}|AKIA[0-9A-Z]{16}|"
    r"(?:api[_-]?key|secret|password|access[_-]?token)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{16,})", re.I)
STOP = set(
    "a an the and or of to for from in on with is are was were be been it this that what which how can "
    "should do does did my your me we our you i actual current latest please continue working work whatever "
    "part left find about where when why who there their its at by as if so not no yes".split()
)
CHUNK_CHARS = 1200
MAX_LINE = 2000
RRF_K = 60
CANDIDATES = int(os.environ.get("RAG_CANDIDATES", "200"))  # fused candidates kept before reading chunk rows


# ---- paths and settings (resolved at call time so tests and installers can switch them with env vars) -------------
def state_dir() -> Path:
    return Path(os.environ.get("MOCKMOB_BRAIN_STATE") or (Path.home() / ".mockmob-brain"))


def _read_config() -> dict:
    try:
        data = json.loads((state_dir() / "config.json").read_text(encoding="utf-8-sig"))
        return data if isinstance(data, dict) else {}
    except (OSError, ValueError):
        return {}


def default_db_path() -> Path:
    return state_dir() / "index" / "rag.sqlite"


def models_dir() -> Path:
    env = os.environ.get("MOCKMOB_BRAIN_MODELS")
    path = Path(env) if env else state_dir() / "models"
    path.mkdir(parents=True, exist_ok=True)
    return path


def resolve_brain_dir() -> Path:
    """env MOCKMOB_BRAIN > config.json brain_dir > the repo that holds this file."""
    env = os.environ.get("MOCKMOB_BRAIN")
    if env:
        return Path(env)
    cfg = _read_config().get("brain_dir")
    if cfg:
        return Path(cfg)
    return Path(__file__).resolve().parents[3]


def resolve_code_dirs() -> list[Path]:
    env = os.environ.get("MOCKMOB_BRAIN_CODE_DIRS")
    if env is not None:
        return [Path(p) for p in env.split(os.pathsep) if p]
    return [Path(p) for p in (_read_config().get("code_dirs") or []) if p]


def worker_python() -> str:
    """The interpreter that has fastembed: config.json python if it exists, else the running one."""
    py = _read_config().get("python")
    if py and Path(py).exists():
        return str(py)
    return sys.executable


def vectors_available() -> bool:
    """fastembed + numpy importable (checked without importing them) and vectors not switched off."""
    if os.environ.get("MOCKMOB_BRAIN_NO_VECTORS") == "1":
        return False
    if _read_config().get("vectors") is False:
        return False
    try:
        return importlib.util.find_spec("fastembed") is not None and importlib.util.find_spec("numpy") is not None
    except (ImportError, ValueError):
        return False


def iso(ts: float) -> str:
    return datetime.fromtimestamp(ts, tz=timezone.utc).date().isoformat()


# ---- corpus ------------------------------------------------------------------------------------------------------
def _skipped_by_path(rel_parts: tuple[str, ...], name: str) -> bool:
    return bool(SKIP_NAME_RE.search(name)) or any(p in SKIP_PATH_PARTS for p in rel_parts[:-1])


def _rglob_md(base: Path, root: Path):
    for p in sorted(base.rglob("*.md")):
        try:
            if p.is_symlink() or not p.is_file():
                continue
            rel = p.relative_to(root)
        except (OSError, ValueError):
            continue
        if _skipped_by_path(rel.parts, p.name):
            continue
        yield p, rel


def build_sources(brain_dir: Path | None = None, code_dirs=None):
    """Yield (project, doc_id, path) for every corpus file, in a stable order. First occurrence of a doc id wins."""
    brain_dir = Path(brain_dir) if brain_dir else resolve_brain_dir()
    code_dirs = [Path(c) for c in (resolve_code_dirs() if code_dirs is None else code_dirs)]
    seen: set[str] = set()

    def emit(project, doc_id, path):
        if doc_id in seen:
            return None
        seen.add(doc_id)
        return project, doc_id, path

    for name in BRAIN_TOP_FILES:
        p = brain_dir / name
        if p.is_file() and not p.is_symlink():
            hit = emit("mockmob", f"brain/{name}", p)
            if hit:
                yield hit
    for folder in BRAIN_FOLDERS:
        base = brain_dir / folder
        if base.is_dir():
            for p, rel in _rglob_md(base, brain_dir):
                hit = emit("mockmob", "brain/" + rel.as_posix(), p)
                if hit:
                    yield hit
    for code in code_dirs:
        if not code.is_dir():
            continue
        for name in CODE_TOP_FILES:
            p = code / name
            if p.is_file() and not p.is_symlink():
                hit = emit("mockmob", f"mockmob/{name}", p)
                if hit:
                    yield hit
        docs = code / "docs"
        if docs.is_dir():
            for p, rel in _rglob_md(docs, code):
                if rel.parts[:2] == ("docs", "brain"):
                    continue
                hit = emit("mockmob", "mockmob/" + rel.as_posix(), p)
                if hit:
                    yield hit


def chunk_text(text: str, target: int = CHUNK_CHARS):
    """Pack lines into ~target-character chunks; break at markdown headings once a chunk is half full."""
    pieces = []  # (line_no, text) for each line slice
    for number, line in enumerate(text.splitlines(), 1):
        for offset in range(0, max(1, len(line)), MAX_LINE):
            pieces.append((number, line[offset:offset + MAX_LINE]))
    chunks, buf, size, start = [], [], 0, None
    for number, part in pieces:
        heading = part.startswith("#")
        if buf and (size + len(part) > target or (heading and size >= target // 2)):
            chunks.append((start, "\n".join(buf)))
            buf, size = [], 0
        if not buf:
            start = number
        buf.append(part)
        size += len(part) + 1
    if buf:
        chunks.append((start, "\n".join(buf)))
    return chunks


def connect(db_path: Path | None = None) -> sqlite3.Connection:
    db_path = Path(db_path or default_db_path())
    db_path.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(db_path, timeout=30)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA journal_mode=WAL")
    con.executescript(
        """
        CREATE TABLE IF NOT EXISTS docs (
            id TEXT PRIMARY KEY, project TEXT NOT NULL, title TEXT NOT NULL,
            path TEXT NOT NULL, size INTEGER NOT NULL, mtime REAL NOT NULL, modified TEXT NOT NULL,
            sha TEXT NOT NULL DEFAULT '', source_date TEXT NOT NULL DEFAULT '',
            source_date_basis TEXT NOT NULL DEFAULT '', supersedes TEXT NOT NULL DEFAULT '',
            skipped TEXT NOT NULL DEFAULT '');
        CREATE TABLE IF NOT EXISTS meta (key TEXT PRIMARY KEY, value TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS chunks (
            id INTEGER PRIMARY KEY, doc_id TEXT NOT NULL, project TEXT NOT NULL,
            modified TEXT NOT NULL, line INTEGER NOT NULL, body TEXT NOT NULL);
        CREATE INDEX IF NOT EXISTS chunks_doc ON chunks(doc_id);
        CREATE VIRTUAL TABLE IF NOT EXISTS chunks_fts USING fts5(body, tokenize='unicode61');
        CREATE TABLE IF NOT EXISTS vecs (chunk_id INTEGER PRIMARY KEY, emb BLOB NOT NULL);
        """
    )
    return con


# ---- retrieval metadata: source_date, supersedes, stale flag, literal-ID route -----------------------------------
def _meta_default() -> bool:
    """On by default (the owner's Continuum runs with metadata on); RAG_META=0 turns it off."""
    return os.environ.get("RAG_META", "1") != "0"


META = _meta_default()
STALE_DAYS = int(os.environ.get("RAG_STALE_DAYS", "14"))  # project state older than this is "stale, verify"
EXACT_WEIGHT = float(os.environ.get("RAG_EXACT_WEIGHT", "2.0"))  # fusion weight of the literal-ID route
RECENCY_BOOST = float(os.environ.get("RAG_RECENCY_BOOST", "0.10"))  # "current"/"latest" queries only
SUPERSEDED_FACTOR = float(os.environ.get("RAG_SUPERSEDED_FACTOR", "0.7"))  # "current"/"latest" queries only
STATE_DOC_NAMES = {"status.md", "now.md", "claude_handover.md", "project_context.md", "priorities.md"}
STATE_DOC_PREFIXES = ("brain/handoffs/", "brain/context/")
CURRENT_SIGNAL_RE = re.compile(r"\b(current|currently|latest|now|today|right now|as of|up to date|newest|most recent)\b", re.I)

_DATE_RE = r"(\d{4})-(\d{2})-(\d{2})"
_FRONT_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
_FRONT_DATE_RE = re.compile(r"^(?:source_date|date|updated|last_updated)\s*:\s*['\"]?" + _DATE_RE, re.I | re.M)
_FRONT_TITLE_RE = re.compile(r"^title\s*:\s*(.+)$", re.I | re.M)
_HEADER_DATE_RE = re.compile(r"^[ \t>*_-]*(?:date|updated|last updated|as of|source date)[ \t*_]*[:\-][ \t*_]*" + _DATE_RE, re.I | re.M)
_NAME_DATE_RE = re.compile(r"(?<!\d)(20[2-3]\d)-?(0[1-9]|1[0-2])-?(0[1-9]|[12]\d|3[01])(?!\d)")
_SUPERSEDES_RE = re.compile(r"^[ \t>*_-]*supersedes[ \t*_]*:[ \t*_]*(.+)$", re.I | re.M)


def _today():
    env = os.environ.get("RAG_TODAY")
    if env:
        return datetime.strptime(env, "%Y-%m-%d").date()
    return datetime.now(timezone.utc).date()


def _valid_date(y, m, d):
    try:
        day = datetime(int(y), int(m), int(d)).date()
    except ValueError:
        return None
    # a date more than a year ahead is not a source date (typo or placeholder); fall through to the next signal
    return day.isoformat() if day.toordinal() <= _today().toordinal() + 366 else None


def date_from_name(doc_id: str) -> str | None:
    """YYYYMMDD or YYYY-MM-DD in the file name (handovers, dated reports)."""
    m = _NAME_DATE_RE.search(doc_id.rsplit("/", 1)[-1])
    return _valid_date(*m.groups()) if m else None


def effective_modified(doc_id: str, mtime: float) -> str:
    """The date used for since/until: a date in the file name (handovers carry their own stamp), else file mtime.
    A fresh clone gives every file the clone time, so the name date is the better signal when there is one."""
    return date_from_name(doc_id) or iso(mtime)


def derive_source_date(doc_id: str, text: str | None, modified: str) -> tuple[str, str]:
    """When the content says it is from, not when the file was last touched. Returns (YYYY-MM-DD, basis)."""
    if text:
        front = _FRONT_RE.match(text)
        if front:
            m = _FRONT_DATE_RE.search(front.group(1))
            if m and _valid_date(*m.groups()):
                return _valid_date(*m.groups()), "frontmatter"
        head = "\n".join(text.splitlines()[:40])
        m = _HEADER_DATE_RE.search(head)
        if m and _valid_date(*m.groups()):
            return _valid_date(*m.groups()), "header"
    by_name = date_from_name(doc_id)
    if by_name:
        return by_name, "filename"
    return modified, "mtime"


def parse_supersedes(text: str) -> list[str]:
    """`supersedes: <path or title>[, ...]` lines in a note (first 80 lines)."""
    out: list[str] = []
    for m in _SUPERSEDES_RE.finditer("\n".join(text.splitlines()[:80])):
        for part in re.split(r"[;,]", m.group(1)):
            part = part.strip().strip("`'\"*[]() ")
            if part and part not in out:
                out.append(part[:200])
    return out[:10]


def is_state_doc(doc_id: str) -> bool:
    return doc_id.rsplit("/", 1)[-1].lower() in STATE_DOC_NAMES or doc_id.startswith(STATE_DOC_PREFIXES)


# A literal is something that must match character for character: ids, versions, hashes, paths, quoted strings.
_LIT_PATTERNS = (
    ("quoted", re.compile(r"\"([^\"\n]{3,120})\"|`([^`\n]{3,120})`|(?<!\w)'([^'\n]{4,120})'(?!\w)")),
    ("path", re.compile(r"(?:[A-Za-z]:[\\/])?(?:[\w.@-]+[\\/])+[\w.@-]+|\b[\w-]+\.(?:md|py|js|mjs|json|ps1|css|html|toml|sqlite|ts|tsx|txt|yml|yaml)\b")),
    ("request_id", re.compile(r"\b[A-Za-z][A-Za-z0-9]{1,9}-\d{1,6}\b")),
    ("version", re.compile(r"\bv\d+(?:\.\d+)+\b|\b\d+\.\d+\.\d+(?:[-+][\w.]+)?\b", re.I)),
    ("hash", re.compile(r"\b(?=[0-9a-f]*\d)(?=[0-9a-f]*[a-f])[0-9a-f]{7,64}\b", re.I)),
)


def extract_literals(query: str) -> list[dict]:
    """Literal strings in a query that deserve an exact-match search. Deduplicated, at most 6."""
    found: list[dict] = []
    seen: set[str] = set()
    for kind, pat in _LIT_PATTERNS:
        for m in pat.finditer(query):
            text = next((g for g in m.groups() if g), None) if m.groups() else None
            text = (text or m.group(0)).strip().rstrip(".,;:?!")
            key = text.lower()
            if len(text) < 3 or key in seen:
                continue
            seen.add(key)
            found.append({"kind": kind, "text": text})
    return found[:6]


def query_mode_signal(query: str) -> str | None:
    return "current" if CURRENT_SIGNAL_RE.search(query) else None


def exact_ranks(con, literals, project, since, until, per_literal: int = 40) -> tuple[list[int], dict[int, list[str]]]:
    """Chunks that contain a literal verbatim. FTS finds candidates by the literal's tokens as a phrase;
    a substring test then confirms the exact characters (case-insensitive; path separators accepted either way)."""
    clauses, args = _filters(project, since, until)
    ids: list[int] = []
    hits: dict[int, list[str]] = {}
    for lit in literals:
        variants = {lit["text"].lower()}
        if "\\" in lit["text"] or "/" in lit["text"]:
            variants |= {lit["text"].lower().replace("\\", "/"), lit["text"].lower().replace("/", "\\")}
        tokens = re.findall(r"[a-z0-9]+", lit["text"].lower())
        if not tokens:
            continue
        phrase = '"' + " ".join(tokens) + '"'
        where = " AND ".join(["chunks_fts MATCH ?"] + clauses)
        rows = con.execute(
            f"SELECT c.id AS id, c.body AS body FROM chunks_fts JOIN chunks c ON c.id = chunks_fts.rowid "
            f"WHERE {where} ORDER BY bm25(chunks_fts) LIMIT ?", [phrase, *args, per_literal * 3]).fetchall()
        kept = 0
        for r in rows:
            if kept >= per_literal:
                break
            if any(v in r["body"].lower() for v in variants):
                if r["id"] not in hits:
                    ids.append(r["id"])
                hits.setdefault(r["id"], []).append(lit["text"])
                kept += 1
    return ids, hits


def name_route(con, query, project, since, until) -> list[int]:
    """A query word that names a state document ("status" -> STATUS.md, "now" -> NOW.md) pulls that document's
    first chunk into the candidates: a generic query like "current project status" matches many chunks and the
    status file's own chunk can fall outside the candidate cut."""
    stems = {n.rsplit(".", 1)[0] for n in STATE_DOC_NAMES}
    words = {w for w in re.findall(r"[a-z0-9_]+", query.lower())} & stems
    if not words:
        return []
    clauses, args = _filters(project, since, until)
    out: list[int] = []
    for r in con.execute("SELECT id FROM docs WHERE lower(id) IN (%s) OR %s" % (
            ",".join("?" * len(words)),
            " OR ".join("lower(id) LIKE ?" for _ in words)),
            [f"{w}.md" for w in words] + [f"%/{w}.md" for w in words]).fetchall():
        where = " AND ".join(["c.doc_id = ?"] + clauses)
        rows = con.execute(f"SELECT c.id FROM chunks c WHERE {where} ORDER BY c.line LIMIT 1", [r["id"], *args]).fetchall()
        out += [x["id"] for x in rows]
    return out


def normalize_title(title: str) -> str:
    return re.sub(r"\s+", " ", (title or "").strip().lower())


def _supersession_map(con) -> dict[str, list[str]]:
    """target (lowercased path, basename or normalized title) -> doc ids that declare `supersedes:` it."""
    out: dict[str, list[str]] = {}
    for r in con.execute("SELECT id, supersedes FROM docs WHERE supersedes != ''"):
        for target in (t.strip() for t in r["supersedes"].split(",")):
            if target:
                out.setdefault(normalize_title(target), []).append(r["id"])
    return out


def doc_freshness(row, supmap: dict, today=None) -> dict:
    """Metadata block for one result document. `row` needs id, title, modified, source_date, source_date_basis, supersedes."""
    today = today or _today()
    sdate, basis = row["source_date"], row["source_date_basis"]
    if not sdate:
        sdate, basis = derive_source_date(row["id"], None, row["modified"])
        basis = basis + " (not backfilled)"
    try:
        age = (today - datetime.strptime(sdate, "%Y-%m-%d").date()).days
    except ValueError:
        age = None
    state = is_state_doc(row["id"])
    base = row["id"].rsplit("/", 1)[-1]
    by = []
    rel = row["id"].split("/", 1)[1] if row["id"].startswith(("brain/", "mockmob/")) else row["id"]
    for key in (row["id"], rel, base, row["title"]):
        by += supmap.get(normalize_title(key), [])
    by = [b for b in dict.fromkeys(by) if b != row["id"]]
    stale = bool(state and age is not None and age > STALE_DAYS)
    if by:
        label = "superseded"
    elif stale:
        label = "stale, verify"
    elif age is not None and age < 0:
        label = "date in the future, verify"
    else:
        label = "current" if state else "dated"
    return {"source_date": sdate, "source_date_basis": basis, "age_days": age, "state_doc": state, "stale": stale,
            "freshness": label, "supersedes": [t.strip() for t in (row["supersedes"] or "").split(",") if t.strip()],
            "superseded_by": by}


# ---- indexing ----------------------------------------------------------------------------------------------------
def _delete_doc(con: sqlite3.Connection, doc_id: str) -> None:
    con.execute("DELETE FROM chunks_fts WHERE rowid IN (SELECT id FROM chunks WHERE doc_id=?)", (doc_id,))
    con.execute("DELETE FROM vecs WHERE chunk_id IN (SELECT id FROM chunks WHERE doc_id=?)", (doc_id,))
    con.execute("DELETE FROM chunks WHERE doc_id=?", (doc_id,))


def _title_of(text: str, path: Path) -> str:
    heading = re.search(r"^# (.+)", text, re.M)
    if heading:
        return heading.group(1).strip()
    front = _FRONT_RE.match(text)
    if front:
        m = _FRONT_TITLE_RE.search(front.group(1))
        if m and m.group(1).strip().strip("'\""):
            return m.group(1).strip().strip("'\"")[:200]
    return path.stem


def index(db_path: Path | None = None, brain_dir: Path | None = None, code_dirs=None,
          vectors: bool = False, budget_s: float | None = None) -> dict:
    """Incremental: unchanged (size, mtime) is skipped; changed mtime is re-hashed and only re-chunked if the
    bytes differ; files that disappeared are removed from every table."""
    con = connect(db_path)
    existing = {r["id"]: (r["size"], r["mtime"], r["sha"]) for r in con.execute("SELECT id, size, mtime, sha FROM docs")}
    sources = []
    for project, doc_id, path in build_sources(brain_dir, code_dirs):
        sources.append((project, doc_id, path))
    # the budget starts after enumeration: walking the corpus is not the part that may be cut short
    deadline = None if budget_s is None else time.time() + budget_s
    seen = {doc_id for _, doc_id, _ in sources}
    removed = set(existing) - seen  # deletions are cheap: do them first so a budget cut never leaves them behind
    for doc_id in removed:
        _delete_doc(con, doc_id)
        con.execute("DELETE FROM docs WHERE id=?", (doc_id,))
    changed, touched_only, skipped, complete = 0, 0, 0, True
    for project, doc_id, path in sources:
        if deadline is not None and time.time() > deadline:
            complete = False
            break
        try:
            st = path.stat()
            old = existing.get(doc_id)
            if old and old[0] == st.st_size and old[1] == st.st_mtime:
                continue
            raw = path.read_bytes()
        except OSError:
            continue  # vanished or locked mid-run: the next refresh sees it again
        sha = hashlib.sha256(raw).hexdigest()
        modified = effective_modified(doc_id, st.st_mtime)
        if old and old[2] == sha:  # touched but identical bytes: refresh metadata only
            con.execute("UPDATE docs SET size=?, mtime=?, modified=? WHERE id=?", (st.st_size, st.st_mtime, modified, doc_id))
            con.execute("UPDATE chunks SET modified=? WHERE doc_id=?", (modified, doc_id))
            touched_only += 1
            continue
        text = raw.decode("utf-8", errors="replace")
        _delete_doc(con, doc_id)
        if SECRET_CONTENT_RE.search(text):  # kept out of the index, remembered so it is not re-read every refresh
            con.execute(
                "INSERT OR REPLACE INTO docs (id, project, title, path, size, mtime, modified, sha, skipped) "
                "VALUES (?,?,?,?,?,?,?,?,?)",
                (doc_id, project, path.stem, str(path), st.st_size, st.st_mtime, modified, sha, "secret_like"))
            skipped += 1
            continue
        sdate, sbasis = derive_source_date(doc_id, text, modified)
        con.execute(
            "INSERT OR REPLACE INTO docs (id, project, title, path, size, mtime, modified, sha, source_date, "
            "source_date_basis, supersedes, skipped) VALUES (?,?,?,?,?,?,?,?,?,?,?,'')",
            (doc_id, project, _title_of(text, path), str(path), st.st_size, st.st_mtime, modified, sha, sdate, sbasis,
             ", ".join(parse_supersedes(text))))
        for line, body in chunk_text(text):
            cur = con.execute(
                "INSERT INTO chunks (doc_id, project, modified, line, body) VALUES (?,?,?,?,?)",
                (doc_id, project, modified, line, body))
            con.execute("INSERT INTO chunks_fts (rowid, body) VALUES (?,?)", (cur.lastrowid, body))
        changed += 1
    if complete:  # a partial run leaves the age stale so the next search continues the work
        con.execute("INSERT OR REPLACE INTO meta (key, value) VALUES ('last_indexed_at', ?)",
                    (datetime.now(timezone.utc).isoformat(timespec="seconds"),))
    con.commit()
    embedded = embed_pending(con) if vectors else 0
    stats = stats_of(con)
    stats.update({"docs_changed": changed, "docs_metadata_only": touched_only, "docs_skipped_secret": skipped,
                  "docs_removed": len(removed), "chunks_embedded": embedded, "complete": complete})
    con.close()
    return stats


def changed_on_disk(db_path: Path | None = None, brain_dir: Path | None = None, code_dirs=None) -> bool:
    """Cheap check (a stat walk of the corpus, no reads): a file is new, gone or has a different size or mtime."""
    con = connect(db_path)
    try:
        existing = {r["id"]: (r["size"], r["mtime"]) for r in con.execute("SELECT id, size, mtime FROM docs")}
    finally:
        con.close()
    seen = set()
    for _, doc_id, path in build_sources(brain_dir, code_dirs):
        seen.add(doc_id)
        old = existing.get(doc_id)
        try:
            st = path.stat()
        except OSError:
            return True
        if old is None or old[0] != st.st_size or old[1] != st.st_mtime:
            return True
    return bool(set(existing) - seen)


def freshness(db_path: Path | None = None) -> dict:
    """Index age and newest indexed file time, attached to every search response."""
    con = connect(db_path)
    try:
        row = con.execute("SELECT value FROM meta WHERE key='last_indexed_at'").fetchone()
        newest = con.execute("SELECT MAX(mtime) FROM docs").fetchone()[0]
        last = datetime.fromisoformat(row[0]) if row else None
        age = round((datetime.now(timezone.utc) - last).total_seconds() / 60, 1) if last else None
        return {
            "last_indexed_at": last.isoformat(timespec="seconds") if last else None,
            "index_age_minutes": age,
            "newest_indexed_file_modified": datetime.fromtimestamp(newest, tz=timezone.utc).isoformat(timespec="seconds") if newest else None,
            "docs": con.execute("SELECT COUNT(*) FROM docs WHERE skipped=''").fetchone()[0],
        }
    finally:
        con.close()


def stats_of(con: sqlite3.Connection) -> dict:
    out = {"docs": con.execute("SELECT COUNT(*) FROM docs WHERE skipped=''").fetchone()[0],
           "chunks": con.execute("SELECT COUNT(*) FROM chunks").fetchone()[0],
           "vectors": con.execute("SELECT COUNT(*) FROM vecs").fetchone()[0]}
    out["by_project"] = {r[0]: r[1] for r in con.execute("SELECT project, COUNT(*) FROM docs WHERE skipped='' GROUP BY project")}
    return out


def stats(db_path: Path | None = None) -> dict:
    con = connect(db_path)
    try:
        return stats_of(con)
    finally:
        con.close()


# ---- locks, embed worker, refresh --------------------------------------------------------------------------------
LOCK_STALE_SECONDS = 15 * 60
EMBED_RETRY_SECONDS = 10 * 60  # after a failed embed run, do not respawn the worker for this long
REFRESH_BUDGET_S = float(os.environ.get("RAG_REFRESH_BUDGET_S", "3"))


def _lock_path(db_path: Path | None, kind: str) -> Path:
    """Separate locks so a long embedding run never blocks the keyword refresh."""
    return Path(db_path or default_db_path()).with_suffix(f".{kind}.lock")


def _acquire(lock: Path) -> bool:
    try:
        if lock.exists() and time.time() - lock.stat().st_mtime > LOCK_STALE_SECONDS:
            lock.unlink()
        lock.parent.mkdir(parents=True, exist_ok=True)
        fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        return False
    except OSError:
        return False
    os.write(fd, str(os.getpid()).encode())
    os.close(fd)
    return True


def _release(lock: Path) -> None:
    try:
        lock.unlink()
    except OSError:
        pass


def _lock_is_live(lock: Path) -> bool:
    """A lock counts only while it is younger than LOCK_STALE_SECONDS; a dead worker's lock must not block forever."""
    try:
        if time.time() - lock.stat().st_mtime > LOCK_STALE_SECONDS:
            lock.unlink(missing_ok=True)
            return False
        return True
    except FileNotFoundError:
        return False
    except OSError:
        return True


def embedding_running(db_path: Path | None = None) -> bool:
    return _lock_is_live(_lock_path(db_path, "embed"))


def pending_embeddings(db_path: Path | None = None) -> int:
    """Chunks that have no vector yet (everything is embedded: the corpus is small)."""
    con = connect(db_path)
    try:
        return con.execute("SELECT COUNT(*) FROM chunks c LEFT JOIN vecs v ON v.chunk_id = c.id "
                           "WHERE v.chunk_id IS NULL").fetchone()[0]
    finally:
        con.close()


def _embed_error(con) -> str | None:
    """The last embed failure if it is recent enough to hold off a retry, else None."""
    row = con.execute("SELECT value FROM meta WHERE key='embed_error'").fetchone()
    if not row:
        return None
    try:
        at, _, msg = row[0].partition("|")
        if time.time() - float(at) < EMBED_RETRY_SECONDS:
            return msg or "unknown error"
    except ValueError:
        pass
    return None


def vectors_status(db_path: Path | None = None, pending: int | None = None) -> str:
    """"keyword only" (no fastembed, or switched off), "vectors refreshing", or "vectors current"."""
    if not vectors_available():
        return "keyword only"
    con = connect(db_path)
    try:
        err = _embed_error(con)
    finally:
        con.close()
    if err:
        return f"keyword only (vectors failed, will retry: {err[:80]})"
    pending = pending_embeddings(db_path) if pending is None else pending
    if pending > 0 or embedding_running(db_path):
        return "vectors refreshing"
    return "vectors current"


def _spawn_embed_worker(db_path: Path | None) -> None:
    """Start `rag.py embed-pending` detached. The worker takes the embed lock; if it is held, the worker exits."""
    args = [worker_python(), str(Path(__file__).resolve()), "embed-pending"]
    if db_path:
        args += ["--db", str(db_path)]
    log_path = Path(db_path or default_db_path()).with_suffix(".embed.log")
    log_path.parent.mkdir(parents=True, exist_ok=True)
    if log_path.exists() and log_path.stat().st_size > 1_000_000:
        log_path.write_bytes(b"")
    log = open(log_path, "ab")
    try:
        if os.name == "nt":
            base = subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.CREATE_NO_WINDOW
            try:
                proc = subprocess.Popen(args, stdin=subprocess.DEVNULL, stdout=log, stderr=log, close_fds=True,
                                        creationflags=base | 0x01000000)  # CREATE_BREAKAWAY_FROM_JOB
            except OSError:  # the parent's job object forbids breakaway
                proc = subprocess.Popen(args, stdin=subprocess.DEVNULL, stdout=log, stderr=log, close_fds=True,
                                        creationflags=base)
        else:
            proc = subprocess.Popen(args, stdin=subprocess.DEVNULL, stdout=log, stderr=log, close_fds=True,
                                    start_new_session=True)
        with warnings.catch_warnings():  # never waited on: the worker outlives this process
            warnings.simplefilter("ignore", ResourceWarning)
            del proc
    finally:
        log.close()


def _maybe_spawn_worker(db_path: Path | None, pending: int) -> bool:
    if not (pending and vectors_available() and not embedding_running(db_path)):
        return False
    con = connect(db_path)
    try:
        if _embed_error(con):
            return False
    finally:
        con.close()
    try:
        _spawn_embed_worker(db_path)
        return True
    except OSError:
        return False


def ensure_fresh(max_age_minutes: float = 30, db_path: Path | None = None, budget_s: float | None = None,
                 background: bool = True, brain_dir: Path | None = None, code_dirs=None) -> dict:
    """Keyword refresh inline within a time budget; new vectors are embedded by a background run.

    The index is refreshed when it was never built, is older than max_age_minutes, or a corpus file changed on
    disk (stat walk), so a file that arrived with a pull is searchable at once. Inline work is deletions and FTS
    rows. Embedding never runs in the search path. A partial inline run leaves the age stale so the next search
    continues it.
    """
    budget_s = REFRESH_BUDGET_S if budget_s is None else budget_s
    info = freshness(db_path)
    idx_lock = _lock_path(db_path, "index")
    stale = (info["index_age_minutes"] is None or info["index_age_minutes"] >= max_age_minutes
             or changed_on_disk(db_path, brain_dir, code_dirs))
    if not stale:
        pending = pending_embeddings(db_path)
        spawned = bool(background) and _maybe_spawn_worker(db_path, pending)
        return {"refreshed": False, "vectors_refreshing": bool(vectors_available() and (pending > 0 or embedding_running(db_path))),
                "pending_embeddings": pending, "vectors_status": vectors_status(db_path, pending),
                "worker_started": spawned, **info}
    if not _acquire(idx_lock):
        return {"refreshed": False, "reason": "refresh already running",
                "vectors_refreshing": embedding_running(db_path), "vectors_status": vectors_status(db_path), **info}
    try:
        stats = index(db_path=db_path, brain_dir=brain_dir, code_dirs=code_dirs, vectors=False, budget_s=budget_s)
    finally:
        _release(idx_lock)
    pending = pending_embeddings(db_path)
    spawned = bool(background) and _maybe_spawn_worker(db_path, pending)
    return {
        "refreshed": True,
        "keyword_refresh": "complete" if stats["complete"] else "partial",
        "docs_changed": stats["docs_changed"], "docs_removed": stats["docs_removed"],
        "vectors_refreshing": bool(vectors_available() and (spawned or pending > 0 or embedding_running(db_path))),
        "pending_embeddings": pending, "vectors_status": vectors_status(db_path, pending),
        "worker_started": spawned, **freshness(db_path),
    }


def build_index(db_path: Path | None = None, brain_dir: Path | None = None, code_dirs=None,
                vectors: bool = False, lock_wait_s: float = 60.0) -> dict:
    """Full incremental index with no time budget, under the index lock (waits up to lock_wait_s for another run).
    vectors=True also embeds inline (slow: loads the model). Used by the installer and `brain.py index`."""
    idx_lock = _lock_path(db_path, "index")
    deadline = time.time() + lock_wait_s
    while not _acquire(idx_lock):
        if time.time() > deadline:
            return {"complete": False, "reason": "index lock held by another run"}
        time.sleep(0.2)
    try:
        return index(db_path=db_path, brain_dir=brain_dir, code_dirs=code_dirs, vectors=vectors, budget_s=None)
    finally:
        _release(idx_lock)


def embed_in_background(db_path: Path | None = None, batch: int = 64) -> dict:
    """Worker entry point: takes the embed lock, embeds pending chunks in batches, releases the lock.
    A failure (no network for the model download, no fastembed) is recorded so searches do not respawn it at once."""
    lock = _lock_path(db_path, "embed")
    if not _acquire(lock):
        return {"embedded": 0, "reason": "embedding already running"}
    try:
        con = connect(db_path)
        try:
            try:
                done = embed_pending(con, batch=batch, lock=lock)
                con.execute("DELETE FROM meta WHERE key='embed_error'")
                con.commit()
                return {"embedded": done}
            except Exception as exc:  # noqa: BLE001 - record and report, never crash the worker silently
                msg = f"{type(exc).__name__}: {exc}"[:300].replace("\n", " ")
                con.execute("INSERT OR REPLACE INTO meta (key, value) VALUES ('embed_error', ?)", (f"{time.time()}|{msg}",))
                con.commit()
                return {"embedded": 0, "error": msg}
        finally:
            con.close()
    finally:
        _release(lock)


def _inject_truststore() -> None:
    try:  # some machines have no system CA store for Python; truststore makes model downloads use it
        import truststore
        truststore.inject_into_ssl()
    except ImportError:
        pass


_MODEL: dict = {}


def _text_model():
    if "m" not in _MODEL:
        _inject_truststore()
        from fastembed import TextEmbedding  # imported lazily: keyword search must work without it
        _MODEL["m"] = TextEmbedding(EMBED_MODEL, cache_dir=str(models_dir()))
    return _MODEL["m"]


def embed_pending(con: sqlite3.Connection, batch: int = 64, lock: Path | None = None) -> int:
    """Embed chunks that have no vector yet with a local fastembed model (no paid API)."""
    import numpy as np

    rows = con.execute(
        "SELECT c.id, c.body FROM chunks c LEFT JOIN vecs v ON v.chunk_id=c.id WHERE v.chunk_id IS NULL ORDER BY c.id"
    ).fetchall()
    if not rows:
        return 0
    model = _text_model()
    done = 0
    for start in range(0, len(rows), batch):
        part = rows[start:start + batch]
        vectors = np.asarray(list(model.embed([r["body"] for r in part])), dtype=np.float32)
        vectors /= np.maximum(np.linalg.norm(vectors, axis=1, keepdims=True), 1e-12)
        con.executemany("INSERT OR REPLACE INTO vecs (chunk_id, emb) VALUES (?,?)",
                        [(r["id"], v.tobytes()) for r, v in zip(part, vectors)])
        con.commit()  # per batch: an interrupted run keeps what it finished
        done += len(part)
        if lock is not None:
            try:
                os.utime(lock)  # keep the lock fresh during a long run
            except OSError:
                pass
    return done


# ---- search ------------------------------------------------------------------------------------------------------
def _fts_query(query: str) -> str:
    words = list(dict.fromkeys(w for w in re.findall(r"[a-z0-9]+", query.lower()) if w not in STOP))[:16]
    return " OR ".join('"' + w + '"' for w in words)


def _filters(project, since, until):
    clauses, args = [], []
    if project and project != "all":
        clauses.append("c.project = ?")
        args.append(project)
    if since:
        clauses.append("c.modified >= ?")
        args.append(since)
    if until:
        clauses.append("c.modified <= ?")
        args.append(until)
    return clauses, args


RAW_PRIOR = float(os.environ.get("RAG_RAW_PRIOR", "1.0"))
DROP_COMMON_FRAC = float(os.environ.get("RAG_DROP_COMMON_FRAC", "0.2"))  # 0 = keep every term
_DF: dict = {}


def _db_key(con) -> str:
    return str(con.execute("PRAGMA database_list").fetchone()[2])


def _drop_common(con, query: str) -> str:
    """Remove query terms that occur in more than DROP_COMMON_FRAC of chunks. They add cost and little ranking."""
    if DROP_COMMON_FRAC <= 0:
        return query
    gen = (_db_key(con), con.execute("SELECT MAX(id) FROM chunks").fetchone()[0],
           con.execute("SELECT COUNT(*) FROM chunks").fetchone()[0])
    if _DF.get("_gen") != gen:
        _DF.clear()
        _DF["_total"] = gen[2]
        _DF["_gen"] = gen
    n = _DF["_total"]
    words = list(dict.fromkeys(w for w in re.findall(r"[a-z0-9]+", query.lower()) if w not in STOP))
    for w in words:
        if w not in _DF:
            _DF[w] = con.execute("SELECT COUNT(*) FROM chunks_fts WHERE chunks_fts MATCH ?", (f'"{w}"',)).fetchone()[0]
    rare = [w for w in words if _DF[w] <= DROP_COMMON_FRAC * n]
    if len(words) < 3:
        return query  # short queries are kept whole
    # Always keep at least the two rarest terms: dropping the common ones must never leave one word that matches
    # everywhere.
    if len(rare) < 2:
        rare = sorted(words, key=lambda w: _DF[w])[:2]
    return " ".join(w for w in words if w in rare)


def keyword_ranks(con, query, project, since, until, limit=200):
    query = _drop_common(con, query)
    match = _fts_query(query)
    if not match:
        return [], []
    clauses, args = _filters(project, since, until)
    where = " AND ".join(["chunks_fts MATCH ?"] + clauses)
    rows = con.execute(
        f"SELECT c.id AS id, bm25(chunks_fts) AS score FROM chunks_fts JOIN chunks c ON c.id = chunks_fts.rowid "
        f"WHERE {where} ORDER BY score LIMIT ?",
        [match, *args, limit],
    ).fetchall()
    return [r["id"] for r in rows], [-r["score"] for r in rows]


_VEC_CACHE: dict = {}
_MASK_CACHE: dict = {}
_QUERY_CACHE: dict = {}  # query text -> normalized embedding (repeat queries skip the model)


def vector_ranks(con, query, project, since, until, limit=200):
    import numpy as np

    clauses, args = _filters(project, since, until)
    where = ("WHERE " + " AND ".join(clauses)) if clauses else ""
    count, top_id = con.execute("SELECT COUNT(*), COALESCE(MAX(chunk_id), 0) FROM vecs").fetchone()
    key = (_db_key(con), count, top_id)
    if _VEC_CACHE.get("key") != key:
        rows = con.execute("SELECT chunk_id, emb FROM vecs").fetchall()
        _VEC_CACHE.update(key=key, ids=np.array([r[0] for r in rows]),
                          mat=np.vstack([np.frombuffer(r[1], dtype=np.float32) for r in rows]) if rows else None)
    if _VEC_CACHE["mat"] is None:
        return [], []
    ids = _VEC_CACHE["ids"]
    # The allowed-id mask depends only on the filter and the index contents, so it is cached per filter and
    # rebuilt when the chunk, document or vector counts change.
    gen = (con.execute("SELECT MAX(id) FROM chunks").fetchone()[0],
           con.execute("SELECT COUNT(*) FROM docs").fetchone()[0], count)
    mkey = (key, gen, where, tuple(args))
    mask = _MASK_CACHE.get(mkey)
    if mask is None:
        allowed = {r[0] for r in con.execute(f"SELECT c.id FROM chunks c {where}", args).fetchall()}
        mask = np.fromiter((i in allowed for i in ids), dtype=bool, count=len(ids))
        _MASK_CACHE.clear()  # keep only the current generation
        _MASK_CACHE[mkey] = mask
    if not mask.any():
        return [], []
    qv = _QUERY_CACHE.get(query)
    if qv is None:
        model = _text_model()
        qv = np.asarray(list(model.embed([QUERY_PREFIX + query])), dtype=np.float32)[0]
        qv /= max(float(np.linalg.norm(qv)), 1e-12)
        if len(_QUERY_CACHE) >= 256:
            _QUERY_CACHE.pop(next(iter(_QUERY_CACHE)))
        _QUERY_CACHE[query] = qv
    sims = _VEC_CACHE["mat"][mask] @ qv
    kept = ids[mask]
    top = np.argsort(-sims)[:limit]
    return [int(kept[i]) for i in top], [float(sims[i]) for i in top]


# Source-type weights: curated pages (context, docs, handovers) get a small lift over everything else.
SOURCE_BOOST = os.environ.get("RAG_SOURCE_BOOST", "1") == "1"
SOURCE_WEIGHT = float(os.environ.get("RAG_SOURCE_WEIGHT", "1.03"))
CURATED_PREFIXES = ("brain/context/", "brain/docs/", "brain/handoffs/")
HANDOFF_WEIGHT = float(os.environ.get("RAG_HANDOFF_WEIGHT", str(SOURCE_WEIGHT)))
ROOT_WEIGHT = float(os.environ.get("RAG_ROOT_WEIGHT", "1.0"))


def _source_weight(doc_id: str, raw_prior: float) -> float:
    if SOURCE_BOOST and doc_id.startswith("brain/handoffs/"):
        return HANDOFF_WEIGHT
    if SOURCE_BOOST and doc_id.startswith(CURATED_PREFIXES):
        return SOURCE_WEIGHT
    return 1.0


def search_ex(query: str, project: str | None = None, since: str | None = None, until: str | None = None,
              limit: int = 5, mode: str = "keyword", db_path: Path | None = None,
              kw_weight: float = 1.0, vec_weight: float = 1.0, min_cos: float | None = None,
              raw_prior: float | None = None, meta: bool | None = None) -> dict:
    """Top-`limit` documents plus how they were found: {"results": [...], "mode_used": "keyword"|"hybrid", "note"?}.

    mode keyword = FTS5 bm25; hybrid = FTS5 + vectors with reciprocal rank fusion. Hybrid quietly falls back to
    keyword when fastembed is missing or nothing is embedded yet (mode_used says which one ran).
    meta adds the literal-ID exact-match route, "current"/"latest" queries preferring newer and non-superseded
    notes, and source_date, freshness, supersedes and exact-match fields on every result.
    """
    limit = max(1, min(int(limit), 100))
    meta = META if meta is None else meta
    if mode not in ("keyword", "hybrid"):
        raise ValueError(f"unknown mode {mode!r}")
    if raw_prior is None:
        raw_prior = RAW_PRIOR
    con = connect(db_path)
    try:
        mode_used, note = "keyword", None
        fused: dict[int, float] = {}
        k_ids, _ = keyword_ranks(con, query, project, since, until)
        for rank, cid in enumerate(k_ids):
            fused[cid] = fused.get(cid, 0.0) + kw_weight / (RRF_K + rank + 1)
        if mode == "hybrid":
            if not vectors_available():
                note = "keyword only: fastembed is not installed or vectors are switched off"
            elif con.execute("SELECT 1 FROM vecs LIMIT 1").fetchone() is None:
                note = "keyword only: vectors are not built yet"
            else:
                try:
                    v_ids, v_sims = vector_ranks(con, query, project, since, until)
                except Exception as exc:  # noqa: BLE001 - a broken model must not break search
                    v_ids, v_sims = None, None
                    note = f"keyword only: vector search failed ({type(exc).__name__})"
                if v_ids is not None:
                    mode_used = "hybrid"
                    if min_cos is not None and (not v_sims or v_sims[0] < min_cos):
                        return {"results": [], "mode_used": mode_used}  # abstain
                    for rank, cid in enumerate(v_ids):
                        fused[cid] = fused.get(cid, 0.0) + vec_weight / (RRF_K + rank + 1)
        literals, exact_hits = [], {}
        if meta:
            literals = extract_literals(query)
            e_ids, exact_hits = exact_ranks(con, literals, project, since, until) if literals else ([], {})
            for rank, cid in enumerate(e_ids):
                fused[cid] = fused.get(cid, 0.0) + EXACT_WEIGHT / (RRF_K + rank + 1)
            for rank, cid in enumerate(name_route(con, query, project, since, until)):
                fused[cid] = fused.get(cid, 0.0) + EXACT_WEIGHT / (RRF_K + rank + 1)
        out: dict = {"results": [], "mode_used": mode_used}
        if note:
            out["note"] = note
        if not fused:
            return out
        ordered = sorted(fused.items(), key=lambda kv: -kv[1])[:CANDIDATES]
        ids = [cid for cid, _ in ordered]
        marks = ",".join("?" * len(ids))
        rows = {r["id"]: r for r in con.execute(
            f"SELECT c.id, c.doc_id, c.project, c.modified, c.line, c.body, d.title, d.source_date, "
            f"d.source_date_basis, d.supersedes FROM chunks c JOIN docs d ON d.id = c.doc_id "
            f"WHERE c.id IN ({marks})", ids)}
        # A concurrent refresh can delete a chunk between ranking and this read; skip ids that are gone.
        ordered = [(cid, score) for cid, score in ordered if cid in rows]
        ordered = sorted(
            ((cid, score * _source_weight(rows[cid]["doc_id"], raw_prior)) for cid, score in ordered),
            key=lambda kv: -kv[1])
        supmap, signal, fresh_by_doc = {}, None, {}
        if meta:
            supmap = _supersession_map(con)
            signal = query_mode_signal(query)
            for cid, _ in ordered:
                d = rows[cid]["doc_id"]
                if d not in fresh_by_doc:
                    fresh_by_doc[d] = doc_freshness({"id": d, "title": rows[cid]["title"], "modified": rows[cid]["modified"],
                                                     "source_date": rows[cid]["source_date"],
                                                     "source_date_basis": rows[cid]["source_date_basis"],
                                                     "supersedes": rows[cid]["supersedes"]}, supmap)
            if signal == "current":
                def _adj(kv):
                    f = fresh_by_doc[rows[kv[0]]["doc_id"]]
                    factor = 1.0
                    if f["age_days"] is not None and f["age_days"] >= 0:
                        factor += RECENCY_BOOST * (1 - min(f["age_days"], 365) / 365)
                    if f["superseded_by"]:
                        factor *= SUPERSEDED_FACTOR
                    return (kv[0], kv[1] * factor)
                ordered = sorted((_adj(kv) for kv in ordered), key=lambda kv: -kv[1])
        best: dict[str, dict] = {}
        terms = set(_fts_query(query).replace('"', "").split(" OR ")) - {""}
        for cid, score in ordered:
            r = rows[cid]
            if r["doc_id"] in best:
                continue
            body = r["body"]
            hit_terms = sorted(t for t in terms if re.search(r"\b" + re.escape(t) + r"\b", body.lower()))
            best[r["doc_id"]] = {
                "rank": 0, "file": r["doc_id"], "title": r["title"], "project": r["project"],
                "line": r["line"], "modified": r["modified"], "score": round(score, 6),
                "matched_terms": hit_terms, "excerpt": body[:900],
            }
            if meta:
                best[r["doc_id"]].update(fresh_by_doc[r["doc_id"]])
                best[r["doc_id"]]["exact_match"] = exact_hits.get(cid, [])
                if signal:
                    best[r["doc_id"]]["query_mode"] = signal
            if len(best) >= limit:
                break
        results = list(best.values())
        for i, item in enumerate(results, 1):
            item["rank"] = i
        out["results"] = results
        return out
    finally:
        con.close()


def search(query: str, project: str | None = None, since: str | None = None, until: str | None = None,
           limit: int = 5, mode: str = "keyword", db_path: Path | None = None, **kw) -> list[dict]:
    """List of result dicts (see search_ex)."""
    return search_ex(query, project, since, until, limit, mode, db_path, **kw)["results"]


def keyword_search(query: str, limit: int = 8, db_path: Path | None = None, brain_dir: Path | None = None,
                   code_dirs=None, refresh: bool = True) -> list[dict]:
    """For the continuum_search tool: [{score, file, line, title, excerpt}], keyword (FTS) only.
    `file` is relative to the brain repo, or prefixed "mockmob/" for a file in the code repo."""
    limit = max(1, min(int(limit), 20))
    if refresh:
        try:
            ensure_fresh(db_path=db_path, brain_dir=brain_dir, code_dirs=code_dirs)
        except Exception:  # noqa: BLE001 - a failed refresh must not block search
            pass
    out = []
    for r in search(query, "mockmob", limit=limit, mode="keyword", db_path=db_path):
        file = r["file"][len("brain/"):] if r["file"].startswith("brain/") else r["file"]
        out.append({"score": r["score"], "file": file, "line": r["line"], "title": r["title"],
                    "excerpt": r["excerpt"][:300]})
    return out


# ---- confidence flag (cross-encoder; optional, slower) -----------------------------------------------------------
CE_MODEL = os.environ.get("RAG_RERANK_MODEL", "BAAI/bge-reranker-v2-m3-int8")
CE_THRESHOLD = float(os.environ.get("RAG_CONFIDENCE_THRESHOLD", "-0.6"))
_CE: dict = {}
CE_LOCK = __import__("threading").Lock()  # one cross-encoder call at a time: concurrent calls each grow ONNX memory


def release_reranker() -> None:
    import gc
    _CE.pop("model", None)
    gc.collect()


def _reranker():
    if "model" not in _CE:
        _inject_truststore()
        from fastembed.rerank.cross_encoder import TextCrossEncoder
        _CE["model"] = TextCrossEncoder(CE_MODEL, cache_dir=str(models_dir()))
    return _CE["model"]


def top_rerank_score(query: str, results: list[dict], db_path: Path | None = None) -> float | None:
    """Best cross-encoder score over the candidate chunks, scoring full chunk bodies (not excerpts)."""
    if not results:
        return None
    con = connect(db_path)
    try:
        bodies = []
        for r in results:
            row = con.execute("SELECT body FROM chunks WHERE doc_id=? AND line=? LIMIT 1", (r["file"], r["line"])).fetchone()
            bodies.append(row[0] if row else r["excerpt"])
    finally:
        con.close()
    with CE_LOCK:
        try:
            scores = list(_reranker().rerank(query, bodies))
        finally:
            release_reranker()
    return float(max(scores))


def search_with_status(query: str, project: str | None = None, since: str | None = None, until: str | None = None,
                       limit: int = 5, mode: str = "hybrid", db_path: Path | None = None,
                       threshold: float | None = None, meta: bool | None = None) -> dict:
    """Search plus a confidence flag. Results are never dropped; low_confidence marks weak matches.
    Keyword mode (or no vectors) is not scored, so its confidence block says so instead of inventing a value."""
    limit = max(1, min(int(limit), 20))
    t = CE_THRESHOLD if threshold is None else threshold
    first = search_ex(query, project, since, until, 20 if mode == "hybrid" else limit, mode, db_path, meta=meta)
    if mode != "hybrid" or first["mode_used"] != "hybrid":
        first["results"] = first["results"][:limit]
        first["confidence"] = {"scored": False, "low_confidence": None,
                               "note": "not scored: needs hybrid mode with vectors built"}
        return first
    try:
        top = top_rerank_score(query, first["results"], db_path)
    except Exception as exc:  # noqa: BLE001 - the flag is optional: report it unscored rather than fail
        first["results"] = first["results"][:limit]
        first["confidence"] = {"scored": False, "low_confidence": None,
                               "note": f"not scored: reranker unavailable ({type(exc).__name__})"}
        return first
    low = top is None or top < t
    first["results"] = first["results"][:limit]
    first["confidence"] = {
        "scored": True, "reranker": CE_MODEL, "threshold": t,
        "top_score": None if top is None else round(top, 3), "low_confidence": bool(low),
        "note": "no confident match: results are the closest sources, verify before relying on them" if low else "confident",
    }
    return first


# ---- CLI (also the embed worker entry point) ---------------------------------------------------------------------
def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="cmd", required=True)
    p_index = sub.add_parser("index", help="build or refresh the SQLite index")
    p_index.add_argument("--vectors", action="store_true", help="also embed new chunks with the local model")
    sub.add_parser("stats")
    p_embed = sub.add_parser("embed-pending", help="background worker: embed chunks that have no vector yet")
    p_embed.add_argument("--db", default=None)
    p_refresh = sub.add_parser("refresh", help="re-index if stale or changed on disk")
    p_refresh.add_argument("--max-age", type=float, default=30)
    p_refresh.add_argument("--no-vectors", action="store_true")
    p_search = sub.add_parser("search")
    p_search.add_argument("query")
    p_search.add_argument("--project", choices=["continuum", "mockmob", "all"], default=None)
    p_search.add_argument("--since")
    p_search.add_argument("--until")
    p_search.add_argument("--limit", type=int, default=5)
    p_search.add_argument("--mode", choices=["keyword", "hybrid"], default="keyword")
    args = parser.parse_args(argv)
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, OSError):
        pass
    if args.cmd == "index":
        print(json.dumps(build_index(vectors=args.vectors), indent=2))
    elif args.cmd == "embed-pending":
        print(json.dumps(embed_in_background(Path(args.db) if args.db else None), indent=2))
    elif args.cmd == "refresh":
        print(json.dumps(ensure_fresh(args.max_age, background=not args.no_vectors), indent=2))
    elif args.cmd == "stats":
        print(json.dumps(stats(), indent=2))
    else:
        ensure_fresh()
        print(json.dumps(search_ex(args.query, args.project, args.since, args.until, args.limit, args.mode),
                         indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
