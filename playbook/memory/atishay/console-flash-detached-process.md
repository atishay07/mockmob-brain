---
name: console-flash-detached-process
description: "16 Nov 2026: terminals flashing on the owner's PC came from background jobs started with DETACHED_PROCESS; use CREATE_NO_WINDOW; disk cleanup facts"
metadata:
  node_type: memory
  type: reference
  originSessionId: ec03baf1-09ed-4ab6-80be-4f81fc956a95
  modified: 2026-11-16T06:07:22.231Z
---

The owner's PC had terminal windows popping in and out for about a minute, stealing focus, for days. Cause found 16 Nov 2026: background jobs in AI OS (`scripts/hook.py` ingest, `scripts/brain.py` RAG refresh, `scripts/autopilot.py`, `scripts/team_bridge.py`, `apps/rag/rag.py`) and the team brain (`mockmob-brain/.brain/brainlib/sync.py`) were started with `DETACHED_PROCESS` (0x8). A console program started that way has no console, so every console child it runs (git, powershell) gets its own visible window. `CREATE_NO_WINDOW` (0x08000000) gives a hidden console the children inherit; Windows ignores it when combined with 0x8. Measured: 12 visible windows the old way, 0 the new way. Backups are beside each file as `*.bak-nowindow-20261116`. Services already running keep the old flags until they restart (a sign-out or reboot).

When starting any background process on this PC: never DETACHED_PROCESS; use CREATE_NO_WINDOW | CREATE_NEW_PROCESS_GROUP. See [[no-useless-background-work]].

Disk (same day, 17.8 GB free at the start): safe wins were `pip cache purge` (6.5 GB), temp files older than 3 days (3 GB), `.next*` build folders in finished worktrees (7 GB). Large and his to decide: old Claude session subagent logs under `~/.claude/projects/C--Users-atish-Desktop-mockmob-copy` (about 16 GB older than 14 days), `mockmob-next/tmp` (13 GB of October walks and APKs), the emulator image (17 GB), Downloads (21 GB). See [[disk-hygiene]].
