"""Small atomic JSON state files under ``STATE_DIR/state/`` (machine-local, never in git)."""
from __future__ import annotations

import copy
import json
import os
import time
import uuid
from pathlib import Path

from . import config


def _path(name: str) -> Path:
    name = str(name)
    if not name.endswith(".json"):
        name += ".json"
    return config.state_path("state", name)


def read(name: str, default=None) -> dict:
    """Return the JSON content of ``state/<name>`` or ``default`` (``{}`` when None)."""
    p = _path(name)
    for attempt in range(5):
        try:
            with open(p, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            break
        except PermissionError:
            time.sleep(0.02 * (attempt + 1))  # Windows: file briefly locked by a replace
        except (OSError, ValueError):
            break
    return copy.deepcopy(default) if default is not None else {}


def write(name: str, data) -> None:
    """Atomically write JSON (tmp file + ``os.replace``)."""
    p = _path(name)
    tmp = p.with_name(f"{p.name}.tmp-{os.getpid()}-{uuid.uuid4().hex[:8]}")
    payload = json.dumps(data, indent=2, ensure_ascii=False, sort_keys=False)
    try:
        with open(tmp, "w", encoding="utf-8", newline="\n") as f:
            f.write(payload)
            f.flush()
            try:
                os.fsync(f.fileno())
            except OSError:
                pass
        last: Exception | None = None
        for attempt in range(15):
            try:
                os.replace(tmp, p)
                return
            except PermissionError as e:  # Windows: a reader holds the target open
                last = e
                time.sleep(0.02 * (attempt + 1))
        if last:
            raise last
    finally:
        try:
            if tmp.exists():
                tmp.unlink()
        except OSError:
            pass


def update(name: str, **fields) -> dict:
    """Read-modify-write helper: merge ``fields`` into the stored dict and return it."""
    d = read(name, {})
    d.update(fields)
    write(name, d)
    return d
