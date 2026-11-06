"""Cross-process file lock (O_CREAT|O_EXCL) with stale-lock recovery.

The lock file holds ``{"pid", "host", "at", "token"}``. A lock is stale when its
process is dead (same host only) or when the file is older than ``stale_after``
seconds (holders of long operations call :meth:`FileLock.touch`). A stale lock is
broken atomically: it is renamed to ``<lock>.stale-<rand>`` and acquisition
retries.
"""
from __future__ import annotations

import json
import os
import random
import socket
import time
import uuid
from pathlib import Path

IS_WINDOWS = os.name == "nt"


class LockTimeout(TimeoutError):
    pass


def pid_alive(pid: int) -> bool:
    """True if a process with this pid exists (best effort)."""
    try:
        pid = int(pid)
    except (TypeError, ValueError):
        return False
    if pid <= 0:
        return False
    if pid == os.getpid():
        return True
    if not IS_WINDOWS:
        try:
            os.kill(pid, 0)
        except ProcessLookupError:
            return False
        except PermissionError:
            return True
        except OSError:
            return False
        return True
    import ctypes
    from ctypes import wintypes

    PROCESS_QUERY_LIMITED_INFORMATION = 0x1000
    STILL_ACTIVE = 259
    ERROR_ACCESS_DENIED = 5
    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    kernel32.OpenProcess.restype = wintypes.HANDLE
    kernel32.OpenProcess.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.DWORD]
    handle = kernel32.OpenProcess(PROCESS_QUERY_LIMITED_INFORMATION, False, pid)
    if not handle:
        return ctypes.get_last_error() == ERROR_ACCESS_DENIED
    try:
        code = wintypes.DWORD()
        kernel32.GetExitCodeProcess.argtypes = [wintypes.HANDLE, ctypes.POINTER(wintypes.DWORD)]
        if kernel32.GetExitCodeProcess(handle, ctypes.byref(code)):
            return code.value == STILL_ACTIVE
        return True
    finally:
        kernel32.CloseHandle.argtypes = [wintypes.HANDLE]
        kernel32.CloseHandle(handle)


class FileLock:
    def __init__(self, path, stale_after: float = 120, timeout: float = 10.0):
        self.path = Path(path)
        self.stale_after = float(stale_after)
        self.default_timeout = float(timeout)  # used only by the context manager
        self._token: str | None = None
        self._held = False

    # -- helpers ----------------------------------------------------------
    @property
    def held(self) -> bool:
        return self._held

    def _read(self) -> tuple[dict | None, float | None]:
        """(content or None if unreadable/empty, mtime or None if the file is gone)."""
        try:
            st = os.stat(self.path)
        except FileNotFoundError:
            return None, None
        except OSError:
            return None, time.time()
        try:
            raw = self.path.read_text(encoding="utf-8")
            data = json.loads(raw) if raw.strip() else None
            return (data if isinstance(data, dict) else None), st.st_mtime
        except (OSError, ValueError):
            return None, st.st_mtime

    def _is_stale(self, data: dict | None, mtime: float | None) -> bool:
        if mtime is None:
            return False  # gone: nothing to break, just retry
        age = time.time() - mtime
        if data is None:
            # empty or half-written: only stale once it has clearly been abandoned
            return age > min(self.stale_after, 5.0)
        if age > self.stale_after:
            return True
        host = data.get("host")
        if host in (None, "", socket.gethostname()):
            pid = data.get("pid")
            if isinstance(pid, int) and not pid_alive(pid):
                return True
        return False

    def _break_stale(self, seen: dict | None, seen_mtime: float | None) -> None:
        """Atomically move a stale lock aside. Never destroys a lock that is not the one seen."""
        aside = self.path.with_name(f"{self.path.name}.stale-{uuid.uuid4().hex[:8]}")
        try:
            os.rename(self.path, aside)
        except FileNotFoundError:
            return
        except OSError:
            return  # Windows: briefly held open; the next retry sorts it out
        # Verify we moved the same lock we judged stale (another breaker may have won the race
        # and a fresh lock may have appeared in between).
        moved, _ = self._read_path(aside)
        if seen is not None and moved is not None and moved.get("token") != seen.get("token"):
            try:
                os.link(aside, self.path)  # put the live lock back (exclusive)
            except OSError:
                pass
        try:
            os.unlink(aside)
        except OSError:
            pass

    @staticmethod
    def _read_path(p: Path):
        try:
            raw = p.read_text(encoding="utf-8")
            data = json.loads(raw) if raw.strip() else None
            return (data if isinstance(data, dict) else None), None
        except (OSError, ValueError):
            return None, None

    def _try_create(self) -> bool:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY
        try:
            fd = os.open(self.path, flags)
        except FileExistsError:
            return False
        except PermissionError:
            return False  # Windows: delete-pending file, try again shortly
        token = uuid.uuid4().hex
        payload = json.dumps(
            {"pid": os.getpid(), "host": socket.gethostname(), "at": time.time(), "token": token}
        )
        try:
            os.write(fd, payload.encode("utf-8"))
        finally:
            os.close(fd)
        self._token = token
        self._held = True
        return True

    # -- public API -------------------------------------------------------
    def acquire(self, timeout: float = 0) -> bool:
        """Try to take the lock, waiting up to ``timeout`` seconds (0 = try once)."""
        deadline = time.monotonic() + max(0.0, float(timeout))
        while True:
            if self._try_create():
                return True
            data, mtime = self._read()
            if self._is_stale(data, mtime):
                self._break_stale(data, mtime)
                if self._try_create():
                    return True
            if time.monotonic() >= deadline:
                return False
            time.sleep(min(0.05 + random.random() * 0.05, max(0.0, deadline - time.monotonic())))

    def touch(self) -> None:
        """Refresh the lock's age (call between long steps so it is not judged stale)."""
        if self._held:
            try:
                os.utime(self.path, None)
            except OSError:
                pass

    def release(self) -> None:
        if not self._held:
            return
        self._held = False
        token, self._token = self._token, None
        data, _ = self._read()
        if data is not None and data.get("token") not in (None, token):
            return  # someone else's lock now; never delete it
        for attempt in range(10):
            try:
                os.unlink(self.path)
                return
            except FileNotFoundError:
                return
            except PermissionError:
                time.sleep(0.02 * (attempt + 1))
            except OSError:
                return

    def holder(self) -> dict | None:
        """The current holder's record, or None when the lock is free or stale."""
        data, mtime = self._read()
        if mtime is None or self._is_stale(data, mtime):
            return None
        return data or {}

    def __enter__(self) -> "FileLock":
        if not self.acquire(self.default_timeout):
            raise LockTimeout(f"could not acquire {self.path} within {self.default_timeout}s")
        return self

    def __exit__(self, *exc) -> None:
        self.release()
