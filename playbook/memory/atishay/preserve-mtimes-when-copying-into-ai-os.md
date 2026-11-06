---
name: preserve-mtimes-when-copying-into-ai-os
description: "6 Nov: copying ~2,000 files into an AI OS-indexed folder with new mtimes made continuum search re-index for 10+ minutes; keep mtimes (copy2 / os.utime)"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 204dccba-6bad-4e60-8bb6-73166cbdb15c
  modified: 2026-11-06T16:10:40.363Z
---

AI OS keyword search (`scripts/search.py`) fingerprints files by size and mtime. It has no content check, and deletes passages per file from an unindexed FTS table. When about 2,000 handover files reappeared with new mtimes (copied into the team brain, then linked back by junction), `continuum_start` with a task ran for over 10 minutes. A killed run rolls back, so the problem repeats on every start.

**Why:** a mass mtime change makes every file look changed, and each changed file costs a full table scan.

**How to apply:** when moving, copying or re-linking many files inside AI OS-indexed folders (`handoffs/`, `wiki/`, `context/`, `raw/`), keep their mtimes (`shutil.copy2`, or `os.utime` from the originals). Afterwards, time one `python -B scripts/brain.py search "x"`; it should take a few seconds. Related: [[team-shared-brain-plan]].
