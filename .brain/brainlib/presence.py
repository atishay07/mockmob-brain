"""Who is working on what right now: claims/<person>/<session8>.json inside the brain repo.

Each person writes only their own folder. A claim is ignored once its last_active is more than 3 hours old.
Stdlib only.
"""
from __future__ import annotations

import json
import os
import re
import socket
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

ACTIVE = timedelta(hours=3)
MAX_TOUCHED = 50
SAFE = re.compile(r'[^A-Za-z0-9_.-]')


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def parse_time(value):
    try:
        moment = datetime.fromisoformat(str(value))
    except (TypeError, ValueError):
        return None
    return moment if moment.tzinfo else moment.replace(tzinfo=timezone.utc)


def _slug(value) -> str:
    return SAFE.sub('_', str(value or '')) or 'unknown'


def short(session) -> str:
    return _slug(str(session or 'unknown')[:8])


def claims_dir(cfg) -> Path:
    return Path(cfg.brain_dir) / 'claims'


def claim_path(cfg, session, person=None) -> Path:
    return claims_dir(cfg) / _slug(person or cfg.person) / (short(session) + '.json')


def _replace_retry(tmp: Path, path: Path, tries: int = 10):
    for attempt in range(tries):
        try:
            os.replace(tmp, path)
            return
        except PermissionError:
            if attempt == tries - 1:
                raise
            time.sleep(0.02 * (attempt + 1))


def write_claim(cfg, rec: dict) -> Path:
    """Write (or refresh) this person's claim for rec['session']. Missing fields get defaults."""
    stamp = now_iso()
    claim = {
        'person': cfg.person,
        'harness': rec.get('harness', ''),
        'session': str(rec.get('session', '')),
        'host': rec.get('host') or socket.gethostname(),
        'started_at': rec.get('started_at') or stamp,
        'last_active': rec.get('last_active') or stamp,
        'repo': rec.get('repo', ''),
        'branch': rec.get('branch', ''),
        'cwd_name': rec.get('cwd_name', ''),
        'task': str(rec.get('task', ''))[:200],
        'touched': [str(p) for p in list(rec.get('touched') or [])][-MAX_TOUCHED:],
    }
    claim['person'] = cfg.person  # one writer per folder: always the configured person
    path = claim_path(cfg, claim['session'])
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name('.' + path.name + '.tmp-' + os.urandom(4).hex())
    tmp.write_text(json.dumps(claim, ensure_ascii=False, indent=2), encoding='utf-8', newline='\n')
    _replace_retry(tmp, path)
    return path


def remove_claim(cfg, session) -> bool:
    path = claim_path(cfg, session)
    try:
        path.unlink()
        return True
    except FileNotFoundError:
        return False
    except OSError:
        return False


def read_claim(cfg, session):
    try:
        return json.loads(claim_path(cfg, session).read_text(encoding='utf-8'))
    except (OSError, ValueError):
        return None


def all_claims(cfg) -> list:
    out = []
    root = claims_dir(cfg)
    if not root.is_dir():
        return out
    for path in sorted(root.glob('*/*.json')):
        try:
            data = json.loads(path.read_text(encoding='utf-8'))
        except (OSError, ValueError):
            continue
        if isinstance(data, dict):
            data['_path'] = path
            out.append(data)
    return out


def active_claims(cfg, exclude_person=None, now=None) -> list:
    """Claims with activity in the last 3 hours, newest first. Older ones are ignored (their owner deletes them at the next sync)."""
    now = now or datetime.now(timezone.utc)
    out = []
    for claim in all_claims(cfg):
        if exclude_person and str(claim.get('person')) == str(exclude_person):
            continue
        moment = parse_time(claim.get('last_active'))
        if moment is None or now - moment > ACTIVE:
            continue
        out.append(claim)
    out.sort(key=lambda c: str(c.get('last_active')), reverse=True)
    return out


def _norm(path) -> str:
    text = str(path).replace('\\', '/')
    while text.startswith('./'):
        text = text[2:]
    return text.casefold()


def overlaps(cfg, relpath, exclude_person=None, repo=None) -> list:
    """Active claims by other people that touched the same repo-relative path (same repo when `repo` is given)."""
    target = _norm(relpath)
    found = []
    for claim in active_claims(cfg, exclude_person):
        if repo and claim.get('repo') and claim.get('repo') != repo:
            continue
        if any(_norm(p) == target for p in claim.get('touched') or []):
            found.append(claim)
    return found


def prune_own(cfg, older_than=ACTIVE, now=None) -> list:
    """Delete this person's claims whose last_active is older than `older_than`. Returns the removed paths."""
    now = now or datetime.now(timezone.utc)
    removed = []
    for claim in all_claims(cfg):
        if str(claim.get('person')) != str(cfg.person):
            continue
        moment = parse_time(claim.get('last_active'))
        if moment is None or now - moment > older_than:
            try:
                Path(claim['_path']).unlink()
                removed.append(str(claim['_path']))
            except OSError:
                pass
    return removed
