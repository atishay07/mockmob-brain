"""MockMob team brain command line.

  python .brain/brain.py sync [--quiet] [--reason R]     commit, pull and push (what the background sync runs)
  python .brain/brain.py pull | push | status | doctor | login | claims
  python .brain/brain.py packet [--task T]               print the start packet
  python .brain/brain.py checkpoint --project mockmob --agent A --task T --next N [--done D --status S
        --evidence E* --touched F* --blocker B* --verification V --cost C]
  python .brain/brain.py search QUERY [--limit N]        keyword search
  python .brain/brain.py index [--vectors] | embed-pending | mirror-memory

Stdlib only. Exit code 0 on success, 1 on a failed sync or check, 2 on bad input.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)


def out(text=''):
    sys.stdout.write(str(text) + '\n')
    sys.stdout.flush()


def dumps(value) -> str:
    return json.dumps(value, indent=2, ensure_ascii=False, default=str)


def summary(res: dict) -> str:
    res = res or {}
    parts = [f"status={res.get('status')}", f"ok={res.get('ok')}"]
    for key in ('committed', 'pushed', 'unpushed'):
        if res.get(key):
            parts.append(f'{key}={res[key] if not isinstance(res[key], list) else len(res[key])}')
    if res.get('changed_files'):
        parts.append(f"changed={len(res['changed_files'])} file(s)")
    if res.get('blocked'):
        parts.append(f"blocked={len(res['blocked'])}")
    if res.get('merged_both_sides'):
        parts.append(f"merged_both_sides={len(res['merged_both_sides'])}")
    if res.get('saved_conflicts'):
        parts.append(f"saved_conflicts={len(res['saved_conflicts'])}")
    text = ' '.join(parts)
    if res.get('message'):
        text += f"\n{res['message']}"
    for item in (res.get('blocked') or [])[:10]:
        if isinstance(item, dict):
            text += f"\n  blocked: {item.get('path')}: {item.get('reason')}" + (f" (line {item['line']})" if item.get('line') else '')
    return text


def cmd_sync(args, cfg):
    from brainlib import memory_mirror, sync
    try:
        memory_mirror.mirror(cfg)
    except Exception as exc:
        _log('mirror', exc)
    res = sync.sync(force=bool(args.force), reason=args.reason or '', timeout=args.timeout)
    for _ in range(3):
        # Handovers, claims or notes written while this sync ran would otherwise wait for the next one.
        if res.get('status') in ('offline', 'auth', 'error', 'wrong-branch', 'not-a-repo'):
            break
        st = sync.status()
        if not st.get('dirty') and not st.get('unpushed'):
            break
        res = sync.sync(force=True, reason=(args.reason or '') + '+drain', timeout=args.timeout, lock_timeout=10.0)
    if not args.quiet:
        out(summary(res))
    return 0 if res.get('ok') else 1


def cmd_pull(args, cfg):
    from brainlib import sync
    res = sync.pull(force=True, timeout=args.timeout, lock_timeout=5.0)
    out(summary(res))
    return 0 if res.get('ok') else 1


def cmd_push(args, cfg):
    from brainlib import sync
    res = sync.push(timeout=args.timeout)
    out(summary(res))
    return 0 if res.get('ok') else 1


def cmd_status(args, cfg):
    from brainlib import presence, state, sync
    info = {'person': cfg.person, 'role': cfg.role, 'mode': cfg.mode, 'brain_dir': str(cfg.brain_dir),
            'code_dirs': [str(p) for p in cfg.code_dirs], 'memory_dirs': [str(p) for p in cfg.memory_dirs]}
    try:
        info['sync'] = sync.status()
    except Exception as exc:
        info['sync'] = {'error': f'{type(exc).__name__}: {exc}'}
    try:
        info['active_claims'] = len(presence.active_claims(cfg))
    except Exception:
        pass
    try:
        from brainlib.search import rag
        info['index'] = rag.freshness()
        info['vectors_status'] = rag.vectors_status()
    except Exception as exc:
        info['index'] = {'error': f'{type(exc).__name__}: {exc}'}
    out(dumps(info))
    return 0


def cmd_doctor(args, cfg):
    from brainlib import gitops
    checks = []

    def check(name, ok, detail=''):
        checks.append(bool(ok))
        out(f"[{'ok' if ok else 'FAIL'}] {name}" + (f': {detail}' if detail else ''))

    check('python 3.10+', sys.version_info >= (3, 10), sys.version.split()[0])
    check('git on PATH', shutil.which('git'), shutil.which('git') or 'not found')
    brain = Path(cfg.brain_dir)
    check('brain folder is a git clone', (brain / '.git').exists(), str(brain))
    check('config.json present', _config_exists(), str(_config_path()))
    check('code repo configured', bool(cfg.code_dirs) or cfg.mode == 'bridge', ', '.join(map(str, cfg.code_dirs)) or 'none (the code repo rules and docs will be missing)')
    try:
        import sqlite3
        con = sqlite3.connect(':memory:')
        con.execute('CREATE VIRTUAL TABLE t USING fts5(x)')
        check('sqlite FTS5', True)
    except Exception as exc:
        check('sqlite FTS5', False, str(exc))
    try:
        from brainlib import sync
        st = sync.status()
        check('sync status', st.get('ok', True), f"{st.get('status')}: unpushed={st.get('unpushed')} blocked={len(st.get('blocked') or [])}")
        res = gitops.run(['ls-remote', '--exit-code', cfg.remote, cfg.branch], cwd=str(brain), timeout=15)
        kind = res.kind() if hasattr(res, 'kind') else ('ok' if res.code == 0 else 'error')
        check('remote reachable', res.code == 0, 'ok' if res.code == 0 else f"{kind}" + (f" (run: {sys.executable} {Path(HERE) / 'brain.py'} login)" if kind == 'auth' else ''))
    except Exception as exc:
        check('sync engine', False, f'{type(exc).__name__}: {exc}')
    try:
        from brainlib.search import rag
        fresh = rag.freshness()
        check('search index', fresh.get('docs', 0) > 0, f"{fresh.get('docs')} docs, age {fresh.get('index_age_minutes')} min, {rag.vectors_status()}")
    except Exception as exc:
        check('search index', False, f'{type(exc).__name__}: {exc}')
    return 0 if all(checks) else 1


def _config_path():
    from brainlib import config
    return config.config_file()


def _config_exists() -> bool:
    try:
        return _config_path().is_file()
    except Exception:
        return False


def cmd_login(args, cfg):
    """Interactive fetch so Git Credential Manager can show its browser sign-in. Inherits the terminal."""
    env = dict(os.environ)
    for key in ('GIT_TERMINAL_PROMPT', 'GCM_INTERACTIVE', 'GIT_ASKPASS'):
        env.pop(key, None)
    git = shutil.which('git') or 'git'
    out(f'Signing in to GitHub for {cfg.remote}/{cfg.branch}. A browser window may open; finish the sign-in there.')
    code = subprocess.call([git, '-C', str(cfg.brain_dir), 'fetch', cfg.remote, cfg.branch], env=env)
    out('Signed in: git can reach the team brain.' if code == 0 else 'Sign-in did not finish. Run this command again.')
    return 0 if code == 0 else 1


def cmd_packet(args, cfg):
    from brainlib import packet
    sys.stdout.write(packet.build(cfg, task=args.task or ''))
    sys.stdout.flush()
    return 0


def cmd_checkpoint(args, cfg):
    from brainlib import handoff
    if args.project != 'mockmob':
        out("This team brain holds only the project 'mockmob'.")
        return 2
    path = handoff.write(args.project, args.agent, args.task, args.next, done=args.done or '', status=args.status,
                         evidence=args.evidence or [], touched=args.touched or [], blockers=args.blocker or [],
                         verification=args.verification or '', cost=args.cost or '', person=cfg.person)
    rel = path.relative_to(Path(cfg.brain_dir)).as_posix()
    pushed = {}
    try:
        from brainlib import sync
        pushed = sync.push(timeout=15, lock_timeout=12) or {}
        if pushed.get('status') == 'locked':
            sync.spawn_background('checkpoint')
    except Exception as exc:
        pushed = {'ok': False, 'status': 'error', 'message': str(exc)[:160]}
    out(handoff.share_message(pushed, rel))
    return 0


def cmd_search(args, cfg):
    from brainlib.search import rag
    hits = rag.keyword_search(args.query, limit=args.limit)
    out(dumps(hits))
    return 0


def cmd_index(args, cfg):
    from brainlib.search import rag
    out(dumps(rag.build_index(vectors=bool(args.vectors))))
    return 0


def cmd_embed_pending(args, cfg):
    from brainlib.search import rag
    out(dumps(rag.embed_in_background()))
    return 0


def cmd_mirror_memory(args, cfg):
    from brainlib import memory_mirror
    out(dumps(memory_mirror.mirror(cfg)))
    return 0


def cmd_claims(args, cfg):
    from brainlib import packet, presence
    now = datetime.now(timezone.utc)
    claims = presence.active_claims(cfg, now=now)
    if not claims:
        out('No active claims (nobody has edited in the last 3 hours).')
        return 0
    for claim in claims:
        touched = ', '.join(str(p) for p in (claim.get('touched') or [])[-6:])
        out(f"{claim.get('person')} | {claim.get('repo') or '?'}@{claim.get('branch') or '?'} | active {packet.ago(packet.parse_time(claim.get('last_active')), now)}"
            f" | {packet.flat(claim.get('task'), 100) or 'no task yet'}" + (f' | {touched}' if touched else ''))
    return 0


def _log(where, exc):
    try:
        from brainlib import sessions
        sessions.log_error('cli', where, exc)
    except Exception:
        pass


def build_parser():
    parser = argparse.ArgumentParser(prog='brain.py', description='MockMob team brain')
    sub = parser.add_subparsers(dest='cmd', required=True)
    p = sub.add_parser('sync', help='commit, pull and push')
    p.add_argument('--quiet', action='store_true')
    p.add_argument('--reason', default='')
    p.add_argument('--force', action='store_true')
    p.add_argument('--timeout', type=float, default=20)
    p.set_defaults(func=cmd_sync)
    for name, func in (('pull', cmd_pull), ('push', cmd_push)):
        p = sub.add_parser(name)
        p.add_argument('--timeout', type=float, default=20)
        p.set_defaults(func=func)
    for name, func in (('status', cmd_status), ('doctor', cmd_doctor), ('login', cmd_login), ('claims', cmd_claims),
                       ('embed-pending', cmd_embed_pending), ('mirror-memory', cmd_mirror_memory)):
        sub.add_parser(name).set_defaults(func=func)
    p = sub.add_parser('packet')
    p.add_argument('--task', default='')
    p.set_defaults(func=cmd_packet)
    p = sub.add_parser('checkpoint')
    p.add_argument('--project', required=True)
    p.add_argument('--agent', required=True)
    p.add_argument('--task', required=True)
    p.add_argument('--next', required=True)
    p.add_argument('--done', default='')
    p.add_argument('--status', default='active', choices=['active', 'paused', 'blocked', 'complete'])
    p.add_argument('--evidence', action='append')
    p.add_argument('--touched', action='append')
    p.add_argument('--blocker', action='append')
    p.add_argument('--verification', default='')
    p.add_argument('--cost', default='')
    p.set_defaults(func=cmd_checkpoint)
    p = sub.add_parser('search')
    p.add_argument('query')
    p.add_argument('--limit', type=int, default=8)
    p.set_defaults(func=cmd_search)
    p = sub.add_parser('index')
    p.add_argument('--vectors', action='store_true')
    p.set_defaults(func=cmd_index)
    return parser


def main(argv=None) -> int:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding='utf-8', errors='replace')
        except Exception:
            pass
    args = build_parser().parse_args(argv)
    try:
        from brainlib import config
        cfg = config.load()
        return int(args.func(args, cfg) or 0)
    except KeyboardInterrupt:
        return 130
    except Exception as exc:
        _log(args.cmd, exc)
        sys.stderr.write(f'brain.py {args.cmd} failed: {type(exc).__name__}: {exc}\n')
        return 1


if __name__ == '__main__':
    sys.exit(main())
