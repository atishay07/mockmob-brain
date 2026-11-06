"""One-way mirror of a person's Claude auto-memory (MockMob project) into playbook/memory/<person>/.

Skips `type: user` files (personal), files over 200 KB and files the secret scanner flags. A mirrored file is
deleted only when this mirror created it and its source is gone. Stdlib only.
"""
from __future__ import annotations

import hashlib
import os
import re
import time
from pathlib import Path

from . import safety, state

MAX_BYTES = 200 * 1024
TYPE_USER = re.compile(r'^type:\s*["\']?user["\']?\s*$', re.I | re.M)
STATE_NAME = 'mirror.json'


def front_matter(text: str) -> str:
    text = text.lstrip('﻿')
    if not text.startswith('---'):
        return ''
    end = text.find('\n---', 3)
    return text[3:end] if end > 0 else ''


def is_user_type(text: str) -> bool:
    return bool(TYPE_USER.search(front_matter(text)))


def _sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _write_bytes(path: Path, data: bytes):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name('.' + path.name + '.tmp-' + os.urandom(4).hex())
    tmp.write_bytes(data)
    for attempt in range(10):
        try:
            os.replace(tmp, path)
            return
        except PermissionError:
            if attempt == 9:
                raise
            time.sleep(0.02 * (attempt + 1))


def sources(cfg) -> dict:
    """name -> Path for every *.md in the memory dirs; the newer file wins when two dirs share a name."""
    found = {}
    for folder in cfg.memory_dirs or []:
        folder = Path(folder)
        if not folder.is_dir():
            continue
        for path in folder.glob('*.md'):
            if not path.is_file():
                continue
            old = found.get(path.name)
            if old is None or path.stat().st_mtime > old.stat().st_mtime:
                found[path.name] = path
    return found


def mirror(cfg) -> dict:
    """Copy changed memory files into playbook/memory/<person>/. Returns {changed: [names], blocked: [{name, reason, line}]}."""
    target_dir = Path(cfg.brain_dir) / 'playbook' / 'memory' / str(cfg.person)
    book = state.read(STATE_NAME, {}) or {}
    created = dict(book.get('created') or {})  # name -> sha of what the mirror wrote
    changed, blocked, keep = [], [], set()
    src = sources(cfg)
    for name, path in sorted(src.items()):
        try:
            data = path.read_bytes()
        except OSError:
            continue
        if len(data) > MAX_BYTES:
            blocked.append({'name': name, 'reason': 'larger than 200 KB', 'line': 0})
            keep.add(name)
            continue
        try:
            text = data.decode('utf-8')
        except UnicodeDecodeError:
            blocked.append({'name': name, 'reason': 'not valid UTF-8 text', 'line': 0})
            keep.add(name)
            continue
        if is_user_type(text):
            continue  # personal memory stays on this machine (and an old copy is removed below)
        findings = safety.scan_text(text)
        if findings:
            first = findings[0]
            blocked.append({'name': name, 'reason': 'possible secret: ' + str(getattr(first, 'kind', 'secret')),
                            'line': int(getattr(first, 'line', 0) or 0)})
            keep.add(name)  # never touch an existing mirrored copy on a blocked source
            continue
        keep.add(name)
        dest = target_dir / name
        try:
            same = dest.is_file() and dest.read_bytes() == data
        except OSError:
            same = False
        if not same:
            _write_bytes(dest, data)
            changed.append(name)
        created[name] = _sha(data)
    for name in list(created):
        if name in keep:
            continue
        dest = target_dir / name
        try:
            dest.unlink()
            changed.append(name)
        except FileNotFoundError:
            pass
        except OSError:
            continue
        created.pop(name, None)
    state.write(STATE_NAME, {'created': created, 'blocked': blocked})
    return {'changed': changed, 'blocked': blocked}
