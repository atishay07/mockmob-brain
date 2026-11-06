"""MockMob team brain agent hook (standalone mode).

Run as:  <python> <brain>/.brain/hook.py <claude|codex> <SessionStart|UserPromptSubmit|PostToolUse|Stop|PreCompact|SessionEnd>
The JSON payload arrives on stdin. Never breaks a session: every error is logged to STATE_DIR/logs/hook-errors.log and
the process exits 0. Outside a MockMob folder it prints nothing and returns before importing anything heavy.
Stdlib only.
"""
from __future__ import annotations

import os
import re
import sys
from datetime import datetime, timedelta, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

HARNESSES = ('claude', 'codex')
EVENTS = ('SessionStart', 'UserPromptSubmit', 'PostToolUse', 'Stop', 'PreCompact', 'SessionEnd')
EDIT_TOOLS = ('edit', 'write', 'multiedit', 'notebookedit', 'apply_patch', 'applypatch')
PATCH_LINE = re.compile(r'^\*\*\* (Add|Update|Delete) File: (.+)$', re.M)
BG_PROMPT_EVERY = timedelta(minutes=5)
CLAIM_REFRESH = timedelta(minutes=10)
NOTE_ASKS = re.compile(r"\b(remember|don'?t forget|do not forget|keep in mind|tell the team|let the team know|share with the team)\b", re.I)
NOTE_LATER = re.compile(r'\b(next (session|time|chat|agent)|later|tomorrow|for the next|after this|the team|everyone|teammates?)\b', re.I)
NOTE_MAX = 600
AUTO_NEXT = 'Unverified auto-capture. Read the session transcript and live repo state before continuing.'


# --- tiny helpers (no brainlib import) ---------------------------------------------------------------------------

def now() -> datetime:
    return datetime.now(timezone.utc)


def parse_payload(text):
    # Some harnesses send raw Windows paths with single backslashes, which strict JSON rejects; escape only those.
    import json
    if not text.strip():
        return {}
    try:
        return json.loads(text)
    except ValueError:
        return json.loads(re.sub(r'\\(?!["\\/bfnrt]|u[0-9a-fA-F]{4})', r'\\\\', text))


def text_field(payload, key) -> str:
    value = payload.get(key)
    return value if isinstance(value, str) else ''


def session_id(payload) -> str:
    return str(payload.get('session_id') or '').strip() or 'unknown'


def parse_time(value):
    try:
        moment = datetime.fromisoformat(str(value))
    except (TypeError, ValueError):
        return None
    return moment if moment.tzinfo else moment.replace(tzinfo=timezone.utc)


def log_error(harness, event, exc):
    try:
        from brainlib import sessions
        sessions.log_error(harness, event, exc)
    except Exception:
        pass


def strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for item in value.values():
            yield from strings(item)
    elif isinstance(value, list):
        for item in value:
            yield from strings(item)


def edited_paths(payload) -> list:
    """Absolute paths a tool call edited (Claude Edit/Write/MultiEdit/NotebookEdit and Codex apply_patch)."""
    tool_input = payload.get('tool_input')
    tool_name = text_field(payload, 'tool_name')
    cwd = text_field(payload, 'cwd')
    found = []
    if isinstance(tool_input, dict):
        for key in ('file_path', 'notebook_path', 'path'):
            value = tool_input.get(key)
            if isinstance(value, str) and value.strip():
                found.append(value.strip())
    if not found or 'patch' in tool_name.lower():
        for text in strings(tool_input):
            found += [m.group(2).strip() for m in PATCH_LINE.finditer(text)]
    result = []
    for value in found:
        if cwd and not os.path.isabs(value):
            value = os.path.join(cwd, value)
        resolved = os.path.normpath(os.path.abspath(value))
        if resolved not in result:
            result.append(resolved)
    return result


def spawn(reason):
    try:
        from brainlib import sync
        return bool(sync.spawn_background(reason))
    except Exception as exc:
        log_error('hook', 'spawn:' + reason, exc)
        return False


def repo_info(path):
    """(repo_slug, branch, relpath) for a file inside a MockMob checkout, else None."""
    try:
        from brainlib import config
        return config.repo_relative(path)
    except Exception:
        return None


def cwd_repo(cwd):
    info = repo_info(os.path.join(cwd, '.brain-cwd-probe')) if cwd else None
    return (info[0], info[1]) if info else ('', '')


def claim_record(rec) -> dict:
    from brainlib import sessions
    return {'harness': rec.get('harness'), 'session': rec.get('session'), 'started_at': rec.get('started_at'),
            'last_active': rec.get('last_active'), 'repo': rec.get('repo', ''), 'branch': rec.get('branch', ''),
            'cwd_name': rec.get('cwd_name', ''), 'task': rec.get('task', ''), 'touched': sessions.touched_paths(rec, 50)}


def refresh_claim(cfg, rec, reason=''):
    from brainlib import presence
    stamp = now().isoformat()
    rec['last_active'] = stamp
    presence.write_claim(cfg, claim_record(rec))
    rec['claim_pushed_at'] = stamp
    if reason:
        spawn(reason)


# --- auto-capture --------------------------------------------------------------------------------------------------

def maybe_auto_capture(cfg, rec, event):
    """Write an auto-capture unless this person already saved a real handover after the session's last edit."""
    from brainlib import handoff, sessions
    last_edit = parse_time(rec.get('last_edit_at'))
    if last_edit is None:
        return None  # nothing was edited: nothing worth handing over
    last_auto = parse_time(rec.get('last_auto_capture_at'))
    if last_auto and last_auto >= last_edit:
        return None
    for d in handoff.scan('mockmob', limit=60):
        if handoff.person_of(d) == cfg.person and handoff.is_real(d):
            moment = parse_time(d.get('observed_at'))
            if moment and moment >= last_edit:
                return None
            break
    sid = str(rec.get('session') or 'unknown')
    turns = int(rec.get('turns', 0) or 0)
    last = str(rec.get('last_message') or '')
    path = handoff.write(
        'mockmob', rec.get('harness', 'claude') + '-auto', f"Auto-capture: {rec.get('harness', 'claude')} session {sessions.short(sid)}",
        AUTO_NEXT, done=f'Auto-captured at {event}. Turns: {turns}. Last message: {last[:400]}', status='paused',
        evidence=[rec['transcript_path']] if rec.get('transcript_path') else [],
        touched=sessions.touched_paths(rec, 30), verification='auto-captured by hook; not agent-verified',
        cost='unknown; hook does not see provider receipts', person=cfg.person)
    rec['last_auto_capture_at'] = now().isoformat()
    return path


def capture_stale_sessions(cfg, current_sid):
    from brainlib import presence, sessions
    for other in sessions.all_records():
        if str(other.get('session')) == current_sid or not sessions.is_stale(other):
            continue
        try:
            maybe_auto_capture(cfg, other, 'a session that ended without SessionEnd')
            other['status'] = 'ended'
            other['ended_at'] = other.get('last_active') or now().isoformat()
            other['ended_reason'] = 'stale'
            sessions.save(other)
            presence.remove_claim(cfg, other.get('session'))
        except Exception as exc:
            log_error(other.get('harness'), 'stale-capture', exc)


# --- events -----------------------------------------------------------------------------------------------------------

def on_session_start(harness, payload, cfg, cwd):
    from brainlib import config, memory_mirror, packet, presence, sessions, state, sync
    sid = session_id(payload)
    stamp = now().isoformat()
    rec = sessions.load_or_new(harness, sid, cwd, text_field(payload, 'transcript_path'))
    rec.update({'session': sid, 'cwd': cwd, 'status': 'running', 'ended_at': None, 'last_active': stamp, 'fed_until': stamp,
                'cwd_name': os.path.basename(cwd.rstrip('/\\')), 'transcript_path': text_field(payload, 'transcript_path') or rec.get('transcript_path', '')})
    sessions.save(rec)
    result = {}
    try:
        result = sync.pull(lock_timeout=3, min_interval=30, timeout=6) or {}
    except Exception as exc:
        log_error(harness, 'pull', exc)
    try:
        memory_mirror.mirror(cfg)
    except Exception as exc:
        log_error(harness, 'mirror', exc)
    rec['repo'], rec['branch'] = cwd_repo(cwd)
    try:
        presence.write_claim(cfg, claim_record(rec))
        rec['claim_pushed_at'] = stamp
    except Exception as exc:
        log_error(harness, 'claim', exc)
    try:
        capture_stale_sessions(cfg, sid)
    except Exception as exc:
        log_error(harness, 'stale', exc)
    try:
        sync.commit_pending(lock_timeout=0)  # try once: a running background sync commits it anyway
    except Exception as exc:
        log_error(harness, 'commit', exc)
    spawn('start')
    text = ''
    try:
        text = packet.build(cfg, session=sid, sync_result=result)
    except Exception as exc:
        log_error(harness, 'packet', exc)
    rec['fed_files'] = [str(p).replace('\\', '/') for p in (result.get('changed_files') or [])]
    rec['fed_blocked'] = [f"{b.get('path')}|{b.get('reason')}" for b in packet.blocked_items(state.read('blocked.json', {}))]
    rec['fed_merged'] = packet.merged_items(state.read('merged.json', {}))
    sessions.save(rec)
    state.write('seen.json', {**(state.read('seen.json', {}) or {}), 'last_seen_at': stamp, 'by': harness})
    return text


def note_agent(cfg, harness) -> str:
    return harness + ('-owner-note' if cfg.role == 'owner' else '-team-note')


def capture_note(cfg, harness, payload, rec):
    prompt = payload.get('prompt')
    if not isinstance(prompt, str) or len(prompt) > NOTE_MAX or not prompt.strip():
        return None
    if not (NOTE_ASKS.search(prompt) and NOTE_LATER.search(prompt)):
        return None
    from brainlib import handoff, sessions
    words = ' '.join(prompt.split())
    who = 'The owner' if cfg.role == 'owner' else (cfg.display_name or cfg.person)
    transcript = text_field(payload, 'transcript_path')
    return handoff.write(
        'mockmob', note_agent(cfg, harness), f'{who} asked to remember for later', 'Asked: ' + words,
        done=f'{who} typed this in a {harness} session ({sessions.short(session_id(payload))}): {words}', status='active',
        evidence=[transcript] if transcript else [], verification=f"captured from {who.lower() if who == 'The owner' else who}'s prompt by the UserPromptSubmit hook; these are their words",
        cost='none', person=cfg.person)


def news_lines(cfg, rec, current_now):
    from brainlib import handoff, packet, state
    fed_until = parse_time(rec.get('fed_until'))
    fed_files = set(rec.get('fed_files') or [])
    sync_state = state.read('sync.json', {}) or {}
    changed = {str(p).replace('\\', '/') for p in (sync_state.get('changed_files') or [])}
    fresh_files = changed - fed_files
    lines = []
    for d in handoff.scan('mockmob', limit=25):
        if handoff.is_auto(d) or handoff.is_probe(d) or handoff.person_of(d) == cfg.person:
            continue
        moment = parse_time(d.get('observed_at'))
        try:
            rel = d['_path'].relative_to(cfg.brain_dir).as_posix()
        except ValueError:
            rel = ''
        rel_md = rel[:-5] + '.md' if rel.endswith('.json') else rel
        if (fed_until and moment and moment > fed_until) or rel in fresh_files or rel_md in fresh_files:
            kind = 'note' if handoff.is_note(d) else 'handover'
            lines.append(f"- {handoff.person_of(d)} {kind} {packet.stamp_text(moment, current_now)}: {packet.flat(d.get('task'), 120)} | next: {packet.flat(d.get('next'), 220) or 'not recorded'} [{rel_md}]")
    rec['fed_files'] = sorted(fed_files | changed)[-300:]
    out = []
    if lines:
        out = ['MockMob team brain: new since this session was last updated:'] + lines[:6]
    fed_blocked = set(rec.get('fed_blocked') or [])
    new_blocked = [b for b in packet.blocked_items(state.read('blocked.json', {})) if f"{b.get('path')}|{b.get('reason')}" not in fed_blocked]
    for b in new_blocked[:4]:
        line_no = b.get('line')
        out.append(f"WARNING: {packet.flat(b.get('path'), 120)} is blocked from sharing: {packet.flat(b.get('reason'), 100)}" + (f' (line {line_no})' if line_no else '') + '. It stays on disk, uncommitted.')
    rec['fed_blocked'] = sorted(fed_blocked | {f"{b.get('path')}|{b.get('reason')}" for b in new_blocked})
    fed_merged = set(rec.get('fed_merged') or [])
    new_merged = [m for m in packet.merged_items(state.read('merged.json', {})) if m not in fed_merged]
    if new_merged:
        out.append('WARNING: both sides edited ' + ', '.join(packet.flat(m, 80) for m in new_merged[:5]) + '; tidy the merged text when convenient.')
    rec['fed_merged'] = sorted(fed_merged | set(new_merged))
    conflicts = [str(c) for c in (sync_state.get('saved_conflicts') or []) if str(c) not in set(rec.get('fed_conflicts') or [])]
    if conflicts:
        out.append('WARNING: a sync clash saved conflict copies: ' + ', '.join(packet.flat(c, 80) for c in conflicts[:4]) + '. Merge by hand; nothing was lost.')
        rec['fed_conflicts'] = sorted(set(rec.get('fed_conflicts') or []) | set(conflicts))
    return out


def on_prompt(harness, payload, cfg, cwd):
    from brainlib import handoff, presence, sessions, state
    sid = session_id(payload)
    current = now()
    rec = sessions.load_or_new(harness, sid, cwd, text_field(payload, 'transcript_path'))
    told = []
    spawned = False
    try:
        saved = capture_note(cfg, harness, payload, rec)
        if saved:
            told.append(f'MockMob team brain: your note was saved and will be shared with the team ({saved.relative_to(cfg.brain_dir).as_posix()}). '
                        'Nothing else is needed; do not say it lives only in your own memory.')
            spawned = spawn('note') or spawned
    except Exception as exc:
        log_error(harness, 'note', exc)
    try:
        told += news_lines(cfg, rec, current)
    except Exception as exc:
        log_error(harness, 'feed', exc)
    try:
        if not rec.get('task') and isinstance(payload.get('prompt'), str) and payload['prompt'].strip():
            rec['task'] = handoff.redact(' '.join(payload['prompt'].split()))[:120]
            if not rec.get('repo'):
                rec['repo'], rec['branch'] = cwd_repo(cwd)
            rec['cwd_name'] = rec.get('cwd_name') or os.path.basename(cwd.rstrip('/\\'))
            refresh_claim(cfg, rec, '' if spawned else 'claim')
            spawned = True
    except Exception as exc:
        log_error(harness, 'claim-task', exc)
    try:
        last_fetch = parse_time((state.read('sync.json', {}) or {}).get('last_fetch_at'))
        last_bg = parse_time(rec.get('bg_requested_at'))
        due = (last_fetch is None or current - last_fetch > BG_PROMPT_EVERY) and (last_bg is None or current - last_bg > BG_PROMPT_EVERY)
        if due and not spawned:
            spawn('prompt')
            rec['bg_requested_at'] = current.isoformat()
    except Exception as exc:
        log_error(harness, 'bg', exc)
    rec.update({'fed_until': current.isoformat(), 'last_active': current.isoformat()})
    sessions.save(rec)
    return handoff.redact('\n'.join(told)) + '\n' if told else ''


def on_post_tool_use(harness, payload, cfg, cwd):
    tool = text_field(payload, 'tool_name').lower()
    if tool and tool not in EDIT_TOOLS and 'patch' not in tool:
        return ''
    paths = edited_paths(payload)
    if not paths:
        return ''
    from brainlib import presence, sessions
    sid = session_id(payload)
    rec = sessions.load_or_new(harness, sid, cwd, text_field(payload, 'transcript_path'))
    first_edit = not rec.get('touched')
    warnings, warned = [], set(rec.get('warned') or [])
    for path in paths:
        info = repo_info(path)
        if not info:
            continue
        repo, branch, rel = info
        sessions.touch(rec, repo, branch, rel, path)
        rec['repo'] = rec.get('repo') or repo
        rec['branch'] = branch or rec.get('branch', '')
        for claim in presence.overlaps(cfg, rel, cfg.person, repo):
            key = f"{claim.get('person')}|{rel}"
            if key in warned:
                continue
            warned.add(key)
            warnings.append(f"MockMob team brain: {claim.get('person')} is also editing {rel} (branch {claim.get('branch') or '?'}, "
                            f"task: {str(claim.get('task') or 'unknown')[:100]}). Check with them or read their change before you overwrite it.")
    rec['warned'] = sorted(warned)
    rec['last_active'] = now().isoformat()
    last_push = parse_time(rec.get('claim_pushed_at'))
    if rec.get('touched') and (first_edit or last_push is None or now() - last_push > CLAIM_REFRESH):
        try:
            refresh_claim(cfg, rec, 'claim')
        except Exception as exc:
            log_error(harness, 'claim-refresh', exc)
    sessions.save(rec)
    if not warnings:
        return ''
    import json
    return json.dumps({'hookSpecificOutput': {'hookEventName': 'PostToolUse', 'additionalContext': '\n'.join(warnings)}}, ensure_ascii=False) + '\n'


def on_stop(harness, payload, cfg, cwd):
    from brainlib import handoff, sessions
    rec = sessions.load_or_new(harness, session_id(payload), cwd, text_field(payload, 'transcript_path'))
    rec['turns'] = int(rec.get('turns', 0) or 0) + 1
    rec['last_active'] = now().isoformat()
    message = payload.get('last_assistant_message')
    if isinstance(message, str) and message.strip():
        rec['last_message'] = handoff.redact(message)[:600]
    sessions.save(rec)
    return ''


def on_precompact(harness, payload, cfg, cwd):
    from brainlib import sessions
    rec = sessions.load_or_new(harness, session_id(payload), cwd, text_field(payload, 'transcript_path'))
    rec['last_active'] = now().isoformat()
    try:
        if maybe_auto_capture(cfg, rec, 'PreCompact'):
            spawn('precompact')
    finally:
        sessions.save(rec)
    return ''


def on_session_end(harness, payload, cfg, cwd):
    from brainlib import presence, sessions
    rec = sessions.load_or_new(harness, session_id(payload), cwd, text_field(payload, 'transcript_path'))
    stamp = now().isoformat()
    rec.update({'status': 'ended', 'ended_at': stamp, 'last_active': stamp})
    try:
        maybe_auto_capture(cfg, rec, 'SessionEnd')
    except Exception as exc:
        log_error(harness, 'auto-capture', exc)
    try:
        presence.remove_claim(cfg, rec.get('session'))
    except Exception as exc:
        log_error(harness, 'claim-remove', exc)
    sessions.save(rec)
    spawn('end')
    return ''


HANDLERS = {'SessionStart': on_session_start, 'UserPromptSubmit': on_prompt, 'PostToolUse': on_post_tool_use,
            'Stop': on_stop, 'PreCompact': on_precompact, 'SessionEnd': on_session_end}


def main(argv, stdin_text='') -> str:
    """Run one hook event and return the text for stdout. Never raises."""
    harness, event = (list(argv) + ['', ''])[:2]
    if os.environ.get('CONTINUUM_INTERNAL') == '1':
        return ''
    try:
        if harness not in HARNESSES or event not in EVENTS:
            raise ValueError(f'unknown harness or event: {harness!r} {event!r}')
        payload = parse_payload(stdin_text)
        if not isinstance(payload, dict):
            raise ValueError('hook payload is not a JSON object')
        cwd = text_field(payload, 'cwd') or os.getcwd()
        from brainlib import config
        cfg = config.load()
        if getattr(cfg, 'mode', 'standalone') == 'bridge':
            return ''  # the owner's AI OS supplies hooks in bridge mode
        if not config.is_mockmob_cwd(cwd, cfg):
            return ''
        return HANDLERS[event](harness, payload, cfg, cwd) or ''
    except Exception as exc:
        log_error(harness, event, exc)
        return ''


def read_stdin() -> str:
    try:
        return sys.stdin.buffer.read().decode('utf-8-sig', 'replace')
    except Exception:
        return ''


if __name__ == '__main__':
    try:
        try:
            sys.stdout.reconfigure(encoding='utf-8')
        except Exception:
            pass
        output = main(sys.argv[1:], read_stdin())
        sys.stdout.write(output)
        sys.stdout.flush()
    except Exception as exc:
        log_error('', '', exc)
    sys.exit(0)
