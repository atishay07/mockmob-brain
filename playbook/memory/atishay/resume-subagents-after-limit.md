---
name: resume-subagents-after-limit
description: 10 Nov 2026 — sub-agents killed by the 5-hour limit keep their context; resume by agent id with SendMessage after the reset; ~5 Fable agents burn a window in an hour
metadata:
  node_type: memory
  type: feedback
  originSessionId: 896125b8-1f9e-4660-b761-2d31487746ee
  modified: 2026-11-10T15:05:02.601Z
---

When the 5-hour usage limit stops a turn, Agent-tool sub-agents fail with a rate-limit error but their work so far is saved (edits stay in the working tree, uncommitted). After the reset, `SendMessage` to the **agent id** (the `a…` id from the spawn result) resumes each one where it stopped; the short name given at spawn (`mob`, `pricing`) is not reachable once it has failed.

**Why:** on 10 Nov 2026 five Fable sub-agents plus the main session used about 83% of a 5-hour window in roughly one hour; two were cut off mid-task and the owner had to say "Try again" after the reset. Resuming by id finished both in 8 and 13 minutes instead of redoing the work.

**How to apply:** keep parallel Fable agents to two or three at a time, give each a time box and a notes file, and check `get_usage` before each wave. On a resume, tell the agent what changed while it was stopped (dev server restarted, files others fixed) and to be economical with captures. The in-app Browser pane stops drawing screenshots when it is hidden; headless Playwright captures (tmp tools like `walk.mjs`) keep working. See [[subagent-wave-pacing]] and [[agent-swarm-resource-hygiene]].
