---
name: no-useless-background-work
description: "7 Nov: owner annoyed by AI OS pop-up windows and CPU-eating background jobs; nothing may run when its output isn't needed; scheduled jobs windowless"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 204dccba-6bad-4e60-8bb6-73166cbdb15c
  modified: 2026-11-06T19:43:30.669Z
---

On 7 Nov 2026 the owner complained about two things on his PC:
- AI OS windows "randomly keep popping onto my screen".
- Background work ate 100% of the CPU so agents couldn't start.

He said nothing should run "uselessly", "for no reason", or for "a job which doesn't need to be done".

Causes found and fixed that night:
- **Duplicate indexers.** A stale-lock bug let two `rag.py embed-pending` workers run at once, both re-embedding already-done chunks. Now there is a heartbeat, a skip for done rows, and idle priority.
- **Pop-up windows.** Four 15-minute scheduled tasks started console `python.exe`. They now start with `pythonw.exe`, and nightly steps use CREATE_NO_WINDOW.
- **Hub briefs nobody saw.** The hub's AI-brief loop made about 360 Haiku `claude -p` calls a day on his subscription and re-read every session file every 2 minutes, even with the hub closed. It now runs only within 30 minutes of a browser view (`ai.note_view`).

**Why:** his PC is shared by many agents. Background work that nobody consumes steals CPU, RAM and subscription usage, and flashing windows interrupt him.

**How to apply:**
- Any new background loop, scheduled job or worker must be windowless and low priority. It must run only when its output is needed: on demand, or when its inputs changed.
- Lock files need a heartbeat.
- Profile with py-spy before guessing; it is installed at `~/AppData/Roaming/Python/Python312/Scripts/py-spy.exe`.

Related: [[agent-swarm-resource-hygiene]], [[disk-hygiene]].
