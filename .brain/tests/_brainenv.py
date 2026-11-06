"""Shared fixtures for the agent-side tests: a temp brain, temp state dir, temp code repo, and a fake sync engine.

Nothing here touches the real STATE_DIR, ~/.claude, ~/.codex or GitHub.
"""
from __future__ import annotations

import json
import os
import shutil
import sys
import tempfile
import types
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest import mock

BRAIN_TOOLS = Path(__file__).resolve().parents[1]  # <repo>/.brain
if str(BRAIN_TOOLS) not in sys.path:
    sys.path.insert(0, str(BRAIN_TOOLS))

import brainlib  # noqa: E402


def iso(delta_minutes=0) -> str:
    return (datetime.now(timezone.utc) + timedelta(minutes=delta_minutes)).isoformat()


class FakeSync(types.SimpleNamespace):
    """Records every call; results are configurable per function."""

    def __init__(self, **results):
        super().__init__(calls=[], results=dict(results))
        ok = {'ok': True, 'status': 'ok', 'message': '', 'changed_files': [], 'committed': False, 'pushed': False,
              'unpushed': 0, 'blocked': [], 'merged_both_sides': [], 'saved_conflicts': [], 'head': 'abc', 'at': iso()}
        self.defaults = ok

    def _call(self, name, args, kwargs):
        self.calls.append((name, args, kwargs))
        value = self.results.get(name)
        if callable(value):
            value = value(*args, **kwargs)
        return dict(self.defaults, **(value or {}))

    def pull(self, *a, **k):
        return self._call('pull', a, k)

    def push(self, *a, **k):
        return self._call('push', a, k)

    def sync(self, *a, **k):
        return self._call('sync', a, k)

    def commit_pending(self, *a, **k):
        return self._call('commit_pending', a, k)

    def status(self, *a, **k):
        return self._call('status', a, k)

    def spawn_background(self, reason, *a, **k):
        self.calls.append(('spawn_background', (reason,) + a, k))
        return True

    def names(self):
        return [c[0] for c in self.calls]

    def spawn_reasons(self):
        return [c[1][0] for c in self.calls if c[0] == 'spawn_background']


class BrainEnv:
    """Context manager: temp brain dir, state dir, code repo (with a fake origin), env vars, config.json."""

    def __init__(self, person='atishay', display='Atishay', role='owner', memory=False, mode='standalone', fake_sync=True, **sync_results):
        self.person, self.display, self.role, self.mode = person, display, role, mode
        self.memory = memory
        self.fake = FakeSync(**sync_results) if fake_sync else None
        self._stack = []

    def __enter__(self):
        self.tmp = Path(tempfile.mkdtemp(prefix='mmbrain-test-')).resolve()
        self.brain = self.tmp / 'brain'
        self.state = self.tmp / 'state'
        self.code = self.tmp / 'code' / 'mockmob'
        self.mem = self.tmp / 'memory'
        for path in (self.brain, self.state, self.code, self.mem):
            path.mkdir(parents=True)
        (self.brain / '.git').mkdir()
        (self.brain / '.brain').mkdir()
        (self.brain / '.brain' / 'team.json').write_text(json.dumps({'people': [
            {'id': 'atishay', 'name': 'Atishay', 'role': 'owner', 'email': '', 'domains': ['product']}]}), encoding='utf-8')
        (self.code / '.git').mkdir()
        (self.code / '.git' / 'config').write_text('[remote "origin"]\n\turl = https://github.com/atishay07/mockmob.git\n', encoding='utf-8')
        (self.code / '.git' / 'HEAD').write_text('ref: refs/heads/feature-x\n', encoding='utf-8')
        patcher = mock.patch.dict(os.environ, {'MOCKMOB_BRAIN_STATE': str(self.state), 'MOCKMOB_BRAIN': str(self.brain)})
        patcher.start()
        self._stack.append(patcher)
        os.environ.pop('CONTINUUM_INTERNAL', None)
        self.write_config()
        if self.fake is not None:
            for p in (mock.patch.dict(sys.modules, {'brainlib.sync': self.fake}),
                      mock.patch.object(brainlib, 'sync', self.fake, create=True)):
                p.start()
                self._stack.append(p)
        return self

    def write_config(self, **over):
        cfg = {'version': 1, 'person': self.person, 'display_name': self.display, 'role': self.role,
               'email': f'{self.person}@example.com', 'brain_dir': str(self.brain), 'code_dirs': [str(self.code)],
               'memory_dirs': [str(self.mem)] if self.memory else [], 'branch': 'main', 'remote': 'origin',
               'mode': self.mode, 'vectors': False, 'python': sys.executable}
        cfg.update(over)
        (self.state / 'config.json').write_text(json.dumps(cfg), encoding='utf-8')

    def __exit__(self, *exc):
        for p in reversed(self._stack):
            try:
                p.stop()
            except Exception:
                pass
        shutil.rmtree(self.tmp, ignore_errors=True)
        return False

    # --- helpers -------------------------------------------------------------------------------------------------
    def cfg(self):
        from brainlib import config
        return config.load()

    def write(self, rel, text):
        path = self.brain / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding='utf-8', newline='\n')
        return path

    def handover(self, person, task='A task', next='Do the next thing', agent='claude', status='active', minutes_ago=0,
                 done='', stamp_suffix=None):
        """Write a handover JSON as if another person's clone had pushed it (observed_at set back by minutes_ago)."""
        when = datetime.now(timezone.utc) - timedelta(minutes=minutes_ago)
        ident = when.strftime('%Y%m%dT%H%M%S.%fZ') + '-' + (stamp_suffix or os.urandom(4).hex())
        entry = {'id': ident, 'observed_at': when.isoformat(), 'agent': agent, 'task': task, 'status': status, 'done': done,
                 'next': next, 'blockers': [], 'evidence': [], 'touched_files': [], 'verification': '',
                 'cost_and_pending_requests': '', 'confidence': 'agent-reported; verify evidence before acting'}
        if person:
            entry['person'] = person
        folder = self.brain / 'handoffs' / 'mockmob'
        folder.mkdir(parents=True, exist_ok=True)
        (folder / (ident + '.json')).write_text(json.dumps(entry, indent=2), encoding='utf-8')
        (folder / (ident + '.md')).write_text('# ' + task + '\n', encoding='utf-8')
        return folder / (ident + '.json')

    def claim(self, person, session='abcd1234', task='Doing things', touched=(), repo='mockmob', branch='main', minutes_ago=1):
        folder = self.brain / 'claims' / person
        folder.mkdir(parents=True, exist_ok=True)
        data = {'person': person, 'harness': 'claude', 'session': session, 'host': 'h', 'started_at': iso(-minutes_ago - 5),
                'last_active': iso(-minutes_ago), 'repo': repo, 'branch': branch, 'cwd_name': 'mockmob', 'task': task,
                'touched': list(touched)}
        (folder / (session[:8] + '.json')).write_text(json.dumps(data), encoding='utf-8')
        return folder / (session[:8] + '.json')

    def state_json(self, name, data=None):
        path = self.state / 'state' / (name + '.json')
        if data is not None:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(data), encoding='utf-8')
        try:
            return json.loads(path.read_text(encoding='utf-8'))
        except (OSError, ValueError):
            return {}

    def hook_payload(self, sid='sess-0001-abcdef', **extra):
        payload = {'session_id': sid, 'cwd': str(self.code), 'transcript_path': str(self.tmp / 't.jsonl')}
        payload.update(extra)
        return payload
