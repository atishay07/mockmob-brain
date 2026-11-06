"""Thin, never-hanging wrapper around the git command line.

Everything that talks to git goes through :func:`run`. It never raises on a
nonzero exit, never lets git prompt for credentials, kills the whole process
tree on timeout, and classifies network and auth failures.
"""
from __future__ import annotations

import os
import re
import shutil
import signal
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Mapping, Sequence

IS_WINDOWS = os.name == "nt"

# Windows creation flags (defined here so POSIX imports stay clean).
CREATE_NO_WINDOW = 0x08000000
CREATE_NEW_PROCESS_GROUP = 0x00000200
DETACHED_PROCESS = 0x00000008
CREATE_BREAKAWAY_FROM_JOB = 0x01000000

GIT_ENV = {
    "GIT_TERMINAL_PROMPT": "0",
    "GCM_INTERACTIVE": "Never",
    "GIT_ASKPASS": "",
    "LC_ALL": "C",
    "GIT_EDITOR": "true",
    "GIT_PAGER": "cat",
    "GIT_MERGE_AUTOEDIT": "no",
}


@dataclass(frozen=True)
class Result:
    code: int
    out: str
    err: str
    timed_out: bool = False
    out_bytes: bytes = field(default=b"", repr=False, compare=False)  # raw stdout (binary-safe)

    @property
    def ok(self) -> bool:
        return self.code == 0 and not self.timed_out

    def kind(self, remote_url: str = "") -> str:
        """'ok', 'offline', 'auth' or 'error' (see :func:`classify`)."""
        return classify(self, remote_url)


def git_exe() -> str:
    return shutil.which("git") or "git"


def build_env(extra: Mapping[str, str] | None = None) -> dict:
    env = dict(os.environ)
    env.update(GIT_ENV)
    if extra:
        env.update(extra)
    return env


def kill_tree(proc: subprocess.Popen) -> None:
    """Kill a process and all its children."""
    try:
        if IS_WINDOWS:
            subprocess.run(
                ["taskkill", "/T", "/F", "/PID", str(proc.pid)],
                stdin=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                creationflags=CREATE_NO_WINDOW,
                timeout=15,
            )
        else:
            try:
                os.killpg(proc.pid, signal.SIGKILL)
            except (ProcessLookupError, PermissionError):
                pass
    except Exception:
        pass
    try:
        proc.kill()
    except Exception:
        pass


def _decode(b: bytes | None) -> str:
    if not b:
        return ""
    return b.decode("utf-8", errors="replace")


def run(
    args: Sequence[str],
    cwd: str | os.PathLike,
    timeout: float = 30,
    *,
    input: bytes | str | None = None,
    env: Mapping[str, str] | None = None,
) -> Result:
    """Run ``git <args>`` in ``cwd``. Never raises on a nonzero exit.

    ``args`` excludes the leading ``git``. On timeout the process tree is killed
    and ``timed_out=True`` is returned.
    """
    cmd = [git_exe(), "-c", "core.quotepath=off", *[str(a) for a in args]]
    if isinstance(input, str):
        input = input.encode("utf-8")
    kwargs: dict = dict(
        cwd=str(cwd),
        env=build_env(env),
        stdin=subprocess.PIPE if input is not None else subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if IS_WINDOWS:
        kwargs["creationflags"] = CREATE_NO_WINDOW
    else:
        kwargs["start_new_session"] = True
    try:
        proc = subprocess.Popen(cmd, **kwargs)
    except FileNotFoundError:
        return Result(127, "", "git: command not found (is git installed and on PATH?)")
    except OSError as e:
        return Result(126, "", f"could not start git: {e}")
    try:
        out, err = proc.communicate(input=input, timeout=timeout)
        return Result(proc.returncode, _decode(out), _decode(err), False, out or b"")
    except subprocess.TimeoutExpired:
        kill_tree(proc)
        try:
            out, err = proc.communicate(timeout=5)
        except Exception:
            out, err = b"", b""
        return Result(124, _decode(out), _decode(err) or "git timed out", True, out or b"")
    except Exception as e:  # pragma: no cover - defensive
        kill_tree(proc)
        return Result(125, "", f"git run failed: {e}")


# --------------------------------------------------------------------------
# failure classification
# --------------------------------------------------------------------------
_OFFLINE_PATTERNS = [
    "could not resolve host",
    "could not resolve hostname",
    "temporary failure in name resolution",
    "name or service not known",
    "nodename nor servname",
    "network is unreachable",
    "network unreachable",
    "no route to host",
    "connection refused",
    "connection reset",
    "connection timed out",
    "connection closed by remote host",
    "operation timed out",
    "timed out",
    "failed to connect",
    "couldn't connect to server",
    "could not connect to server",
    "unable to connect",
    "unable to look up",
    "ssl_connect",
    "ssl connection",
    "tls connection",
    "the remote end hung up unexpectedly",
    "early eof",
    "does not appear to be a git repository",
    "could not read from remote repository",
    "unable to update url base from redirection",
    "rpc failed",
    "http/2 stream",
    "send failure",
    "recv failure",
]

_AUTH_RE = re.compile(
    r"authentication failed|"
    r"\b403\b|\b401\b|"
    r"could not read username|could not read password|"
    r"terminal prompts disabled|"
    r"permission denied \(publickey|"
    r"invalid username or password|"
    r"support for password authentication was removed|"
    r"access denied|bad credentials|"
    r"host key verification failed|"
    r"remote: permission to .* denied|"
    r"the requested url returned error: 40[13]",
    re.I,
)


def classify(result_or_text, remote_url: str = "") -> str:
    """Classify a git outcome as 'ok', 'offline', 'auth' or 'error'.

    ``offline``: could not resolve host, timed out, network unreachable,
    connection refused/reset, or a remote that does not exist / is not reachable.
    ``auth``: authentication failed, 403, could not read Username, or
    "repository not found" when the remote is GitHub.
    """
    if isinstance(result_or_text, Result):
        if result_or_text.ok:
            return "ok"
        if result_or_text.timed_out:
            return "offline"
        text = result_or_text.err + "\n" + result_or_text.out
    else:
        text = str(result_or_text or "")
    low = text.lower()
    # A DNS or socket failure wins over anything else in the text.
    hard_offline = (
        "could not resolve host",
        "could not resolve hostname",
        "temporary failure in name resolution",
        "name or service not known",
        "network is unreachable",
        "no route to host",
        "connection refused",
        "connection timed out",
        "failed to connect",
        "couldn't connect to server",
        "could not connect to server",
    )
    if any(p in low for p in hard_offline):
        return "offline"
    if _AUTH_RE.search(text):
        return "auth"
    if "repository not found" in low and "github.com" in (remote_url + low).lower():
        return "auth"
    if any(p in low for p in _OFFLINE_PATTERNS):
        return "offline"
    return "error"


def is_non_fast_forward(text: str) -> bool:
    low = (text or "").lower()
    return any(
        s in low
        for s in (
            "non-fast-forward",
            "fetch first",
            "[rejected]",
            "failed to push some refs",
            "updates were rejected",
            "tip of your current branch is behind",
        )
    )


def python_exe_ok(path: str | None) -> bool:
    return bool(path) and Path(path).exists()
