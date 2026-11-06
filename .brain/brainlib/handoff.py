"""Session handovers in Continuum format (byte-compatible with AI OS scripts/brain.py checkpoint()).

Files: handoffs/<project>/<YYYYmmddTHHMMSS.ffffffZ>-<8 hex>.json and .md, append-only, one pair per handover.
Stdlib only.
"""
from __future__ import annotations

import json
import os
import re
import time
from datetime import datetime, timezone
from pathlib import Path

SLUG = re.compile(r'[a-z0-9-]+')

# Same patterns as AI OS brain.py SECRET_PATTERNS, so redaction is identical on every machine.
SECRET_PATTERNS = [
    (re.compile(r'\b(?:sk-(?:proj-|ant-api\d+-)?)[A-Za-z0-9_-]{20,}'), '[REDACTED_KEY]'),
    (re.compile(r'\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|AIza[A-Za-z0-9_-]{25,})'), '[REDACTED_KEY]'),
    (re.compile(r'\beyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+'), '[REDACTED_TOKEN]'),
    (re.compile(r'(?im)(\b(?:[A-Z_]*(?:API_KEY|SECRET|ACCESS_TOKEN|PASSWORD)|authorization)\s*[:=]\s*)([^\s,;]{8,})'), r'\1[REDACTED_VALUE]'),
    (re.compile(r'\b(?:xox[abp]-[A-Za-z0-9-]{10,}|AKIA[0-9A-Z]{16}|sbp_[A-Za-z0-9]{20,}|rzp_(?:live|test)_[A-Za-z0-9]{10,})'), '[REDACTED_KEY]'),
]

# Agent-side argument leaks such as '</next><parameter name="done">' must not end up in the record.
LEAK = re.compile(r'\s*</?(?:next|done|task|blocker|blockers|evidence|touched|verification|cost|parameter|invoke|function_calls)(?:\s[^>]*)?>[\s\S]*$')

PROBE = re.compile(r'probe|test-token|ACCTEST', re.I)
CONFIDENCE = 'agent-reported; verify evidence before acting'


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def redact(text):
    text = str(text)
    for pattern, replacement in SECRET_PATTERNS:
        text = pattern.sub(replacement, text)
    try:  # the shared safety scanner, when present, catches the rest (private key blocks and so on)
        from . import safety
        text = safety.redact(text)
    except Exception:
        pass
    return text


def _cut(x):
    return LEAK.sub('', x) if isinstance(x, str) else x


def _clean(value):
    if isinstance(value, (list, tuple)):
        return [redact(_cut(str(x))) for x in value]
    return redact(_cut(value if isinstance(value, str) else ('' if value is None else str(value))))


def _as_list(value):
    if value is None:
        return []
    if isinstance(value, (str, bytes)):
        return [value] if value else []
    return list(value)


def brain_dir(root=None) -> Path:
    if root:
        return Path(root)
    from . import config
    return Path(config.load().brain_dir)


def default_person() -> str:
    try:
        from . import config
        return str(config.load().person or '')
    except Exception:
        return ''


def _replace_retry(tmp: Path, path: Path, tries: int = 10):
    for attempt in range(tries):
        try:
            os.replace(tmp, path)
            return
        except PermissionError:  # Windows: another process holds the file for an instant
            if attempt == tries - 1:
                raise
            time.sleep(0.02 * (attempt + 1))


def _write_text(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + '.tmp-' + os.urandom(5).hex())
    tmp.write_text(text, encoding='utf-8', newline='\n')
    _replace_retry(tmp, path)


def _link_from_here(folder: Path, root: Path):
    def fix(match):
        # Links that exist at the brain root are re-pointed so they resolve from this folder; broken ones lose their link syntax.
        target = match.group(1)
        if re.match(r'\w+://', target) or target.startswith('#'):
            return match.group(0)
        path = root / target.split('#')[0]
        if path.exists():
            return '](' + Path(os.path.relpath(path, folder)).as_posix() + ')'
        return '] (' + target + ')'
    return fix


def write(project, agent, task, next, done='', status='active', evidence=(), touched=(), blockers=(),
          verification='', cost='', person=None, root=None) -> Path:
    """Write one handover pair and return the path of the .md file. `root` overrides the brain dir (tests)."""
    if not SLUG.fullmatch(str(project)):
        raise ValueError('Project must be a lowercase slug.')
    base = brain_dir(root)
    folder = base / 'handoffs' / project
    folder.mkdir(parents=True, exist_ok=True)
    person = person or default_person()
    entry = None
    for _ in range(5):
        stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
        ident = stamp + '-' + os.urandom(4).hex()
        entry = {'id': ident, 'observed_at': now(), 'agent': _clean(agent), 'task': _clean(task), 'status': status,
                 'done': _clean(done), 'next': _clean(next), 'blockers': _clean(_as_list(blockers)),
                 'evidence': _clean(_as_list(evidence)), 'touched_files': _clean(_as_list(touched)),
                 'verification': _clean(verification), 'cost_and_pending_requests': _clean(cost), 'confidence': CONFIDENCE}
        if person:
            entry['person'] = _clean(person)
        final_json = folder / (ident + '.json')
        staged = final_json.with_name(final_json.name + '.tmp-' + os.urandom(5).hex())
        staged.write_text(json.dumps(entry, ensure_ascii=False, indent=2), encoding='utf-8', newline='\n')
        try:
            os.link(staged, final_json)  # the final name appears only complete, and the link fails if it exists
        except FileExistsError:
            continue
        except OSError:
            if final_json.exists():
                continue
            with final_json.open('x', encoding='utf-8', newline='\n') as handle:
                handle.write(staged.read_text(encoding='utf-8'))
        finally:
            try:
                staged.unlink()
            except OSError:
                pass
        break
    else:
        raise OSError('could not allocate a unique handover id')
    rendered = lambda v: re.sub(r'\]\(([^)]+)\)', _link_from_here(folder, base), json.dumps(v, ensure_ascii=False))
    title = entry['task']
    front = (f'---\ntitle: {json.dumps(title, ensure_ascii=False)}\ntype: checkpoint\nstatus: {status}\n'
             f'updated: {now()[:10]}\n---\n\n# {title}\n\n')
    body = front + '\n'.join(f'## {k}\n\n{rendered(v)}\n' for k, v in entry.items())
    md = folder / (ident + '.md')
    _write_text(md, body)
    return md


def scan(project='mockmob', limit=None, root=None) -> list:
    """Handover dicts, newest first by filename stamp, with `_path` (Path) and `_stamp` (str) added."""
    folder = brain_dir(root) / 'handoffs' / project
    if not SLUG.fullmatch(str(project)) or not folder.is_dir():
        return []
    out = []
    for path in sorted(folder.glob('*.json'), reverse=True):
        if '.tmp-' in path.name:
            continue
        try:
            data = json.loads(path.read_text(encoding='utf-8'))
        except (OSError, ValueError):
            continue
        if not isinstance(data, dict):
            continue
        data['_path'] = path
        data['_stamp'] = path.stem.split('-', 1)[0]
        out.append(data)
        if limit and len(out) >= limit:
            break
    return out


def _agent(d) -> str:
    return str(d.get('agent') or '')


def is_auto(d) -> bool:
    return _agent(d).endswith('-auto')


def is_owner_note(d) -> bool:
    return _agent(d).endswith('-owner-note')


def is_team_note(d) -> bool:
    return _agent(d).endswith('-team-note')


def is_note(d) -> bool:
    return is_owner_note(d) or is_team_note(d)


def is_probe(d) -> bool:
    return bool(PROBE.search(_agent(d))) or bool(PROBE.search(str(d.get('task') or ''))) or d.get('probe') is True


def is_real(d) -> bool:
    """A real handover: not an auto-capture, a note or a probe."""
    return not (is_auto(d) or is_note(d) or is_probe(d))


def owner_id(root=None) -> str:
    try:
        data = json.loads((brain_dir(root) / '.brain' / 'team.json').read_text(encoding='utf-8-sig'))
        for person in data.get('people', []):
            if person.get('role') == 'owner' and person.get('id'):
                return str(person['id'])
        people = data.get('people', [])
        if people and people[0].get('id'):
            return str(people[0]['id'])
    except (OSError, ValueError, AttributeError, TypeError):
        pass
    return 'atishay'


def person_of(d, root=None) -> str:
    """The `person` key if present; older Continuum files have none and belong to the owner."""
    value = d.get('person')
    return str(value) if value else owner_id(root)


def parse_time(value):
    try:
        moment = datetime.fromisoformat(str(value))
    except (TypeError, ValueError):
        return None
    return moment if moment.tzinfo else moment.replace(tzinfo=timezone.utc)


def share_message(push_result, rel) -> str:
    """The sentence continuum_checkpoint and `brain.py checkpoint` print after saving."""
    res = push_result or {}
    if res.get('ok') and not res.get('unpushed'):
        return f'{rel}: saved and shared with the team'
    reason = res.get('status') or res.get('message') or 'not synced yet'
    if res.get('message') and res.get('status') not in (None, res.get('message')):
        reason = f"{res.get('status')}: {res.get('message')}"
    return f'{rel}: saved locally; it will be shared at the next sync ({reason})'
