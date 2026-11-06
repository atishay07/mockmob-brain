"""Machine-local session records for the hooks: STATE_DIR/sessions/<harness>-<sid>.json (never in git).

Also the hook error log (STATE_DIR/logs/hook-errors.log, rotated at 1 MB, two old copies kept). Stdlib only, and
log_error works even when the rest of brainlib cannot be imported.
"""
from __future__ import annotations

import json
import os
import re
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

STALE_AFTER = timedelta(hours=2)
LOG_MAX = 1024 * 1024
SAFE = re.compile(r'[^A-Za-z0-9_.-]')


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def parse_time(value):
    try:
        moment = datetime.fromisoformat(str(value))
    except (TypeError, ValueError):
        return None
    return moment if moment.tzinfo else moment.replace(tzinfo=timezone.utc)


def fallback_state_dir() -> Path:
    env = os.environ.get('MOCKMOB_BRAIN_STATE')
    return Path(env) if env else Path.home() / '.mockmob-brain'


def state_dir() -> Path:
    try:
        from . import config
        return Path(config.STATE_DIR)
    except Exception:
        return fallback_state_dir()


def log_error(harness, event, exc) -> None:
    """Append one line to logs/hook-errors.log. Never raises."""
    try:
        folder = state_dir() / 'logs'
        folder.mkdir(parents=True, exist_ok=True)
        log = folder / 'hook-errors.log'
        try:
            if log.exists() and log.stat().st_size > LOG_MAX:
                old1, old2 = log.with_name(log.name + '.1'), log.with_name(log.name + '.2')
                if old1.exists():
                    os.replace(old1, old2)
                os.replace(log, old1)
        except OSError:
            pass
        text = ' '.join([now_iso(), str(harness or ''), str(event or ''), type(exc).__name__ + ':', str(exc)])
        with log.open('a', encoding='utf-8') as handle:
            handle.write(text.replace('\n', ' ')[:600] + '\n')
    except Exception:
        pass


def sessions_dir() -> Path:
    path = state_dir() / 'sessions'
    path.mkdir(parents=True, exist_ok=True)
    return path


def safe_id(sid) -> str:
    return SAFE.sub('_', str(sid or 'unknown'))[:120] or 'unknown'


def short(sid) -> str:
    return safe_id(sid)[:8]


def record_path(harness, sid) -> Path:
    return sessions_dir() / f'{harness}-{safe_id(sid)}.json'


def new_record(harness, sid, cwd='', transcript='') -> dict:
    stamp = now_iso()
    return {'harness': harness, 'session': str(sid), 'cwd': cwd, 'transcript_path': transcript,
            'started_at': stamp, 'last_active': stamp, 'ended_at': None, 'status': 'running', 'turns': 0,
            'touched': [], 'last_message': '', 'task': '', 'repo': '', 'branch': '', 'cwd_name': '',
            'fed_until': stamp, 'fed_files': [], 'fed_blocked': [], 'warned': [],
            'last_edit_at': None, 'last_auto_capture_at': None, 'claim_pushed_at': None, 'bg_requested_at': None}


def _read(path: Path):
    for attempt in range(8):
        try:
            value = json.loads(path.read_text(encoding='utf-8'))
            return value if isinstance(value, dict) else None
        except FileNotFoundError:
            return None
        except PermissionError:  # Windows: another hook process is replacing the file this instant
            if attempt == 7:
                return None
            time.sleep(0.01 * (attempt + 1))
        except (OSError, ValueError):
            return None
    return None


def load(harness, sid):
    return _read(record_path(harness, sid))


def load_or_new(harness, sid, cwd='', transcript='') -> dict:
    return load(harness, sid) or new_record(harness, sid, cwd, transcript)


def save(rec: dict) -> Path:
    path = record_path(rec.get('harness', 'claude'), rec.get('session', 'unknown'))
    tmp = path.with_name('.' + path.name + '.tmp-' + os.urandom(4).hex())
    tmp.write_text(json.dumps(rec, ensure_ascii=False, indent=1), encoding='utf-8', newline='\n')
    for attempt in range(10):
        try:
            os.replace(tmp, path)
            return path
        except PermissionError:
            if attempt == 9:
                raise
            time.sleep(0.02 * (attempt + 1))
    return path


def all_records() -> list:
    rows = []
    for path in sorted(sessions_dir().glob('*.json')):
        rec = _read(path)
        if rec is not None:
            rows.append(rec)
    return rows


def touch(rec: dict, repo: str, branch: str, relpath: str, abs_path: str = '') -> None:
    """Record an edited file. `touched` keeps the last 200 distinct repo-relative paths, newest last."""
    stamp = now_iso()
    kept = [t for t in rec.get('touched', []) if isinstance(t, dict) and not (t.get('path') == relpath and t.get('repo') == repo)]
    kept.append({'path': relpath, 'repo': repo, 'branch': branch, 'abs': abs_path, 'at': stamp})
    rec['touched'] = kept[-200:]
    rec['last_edit_at'] = stamp


def touched_paths(rec: dict, count=50) -> list:
    return [str(t.get('path')) for t in rec.get('touched', []) if isinstance(t, dict) and t.get('path')][-count:]


def is_stale(rec: dict, now=None) -> bool:
    """Still marked running but silent for 2 hours: the session died without a SessionEnd."""
    now = now or datetime.now(timezone.utc)
    if rec.get('status') != 'running' or rec.get('ended_at'):
        return False
    last = parse_time(rec.get('last_active'))
    return last is not None and now - last > STALE_AFTER
