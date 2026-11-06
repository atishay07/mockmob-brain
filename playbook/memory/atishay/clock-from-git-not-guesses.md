---
name: clock-from-git-not-guesses
description: "2 Nov: I labelled STATUS/NOW entries 1-2 hours late by guessing the time; read the clock (git commit time or get_usage reset maths) before writing any time"
metadata:
  node_type: memory
  type: feedback
  originSessionId: ddd9a45c-465a-4aca-a19a-3798d499db2b
  modified: 2026-11-01T23:05:59.397Z
---

On 2 Nov 2026 I wrote "about 5:30 am", "5:50 am" and "6:45 am IST" into STATUS.md and NOW.md for releases made at about
4:15 and 4:35 am IST, and the handoff's own "4:20 am" start was also off (the session began about 3:27 am). Fixed the same
morning.

**Why:** the owner reads these files to know what happened when ("be honest", progress honesty); wrong times mislead him
and the next session.

**How to apply:**
- Before writing a time, read it: `git log -1 --format=%ad --date=format:%H:%M` in a worktree prints local IST; or work
  back from `get_usage` (`resetsAt` in UTC + 5:30, minus `resetsIn`). Git Bash ignores `TZ=Asia/Kolkata` (prints UTC).
- Never carry a time forward from a handoff without checking it.

Related: [[time-and-estimates-format]], [[owner-master-ledger]].
