---
name: dont-stop-for-handover
description: "16 Nov 2026: owner found the session stopped for 7 hours at 81% usage after writing a handoff; he wants work to continue until everything is finalized, no stop for handover"
metadata:
  node_type: memory
  type: feedback
  originSessionId: ec03baf1-09ed-4ab6-80be-4f81fc956a95
  modified: 2026-11-16T04:53:24.799Z
---

On 16 Nov 2026 (about 10:20 am IST) the owner wrote: "No need to stop for handover or anything. You stopped 7 hours ago. I don't know why, but anyway, the usage is fresh now ... Continue everything ... and only stop when you think everything has been finalized, and then report to me that everything is done now." I had stopped starting new work at 81% of the 5-hour window, written the handoff and ended the turn; the window then reset while nothing ran.

**Why:** an idle session costs him hours; a usage limit pauses the session by itself and he can resume it.

**How to apply:** keep building until the list is finished. Write the handoff and checkpoint in passing (they are still wanted), but do not end the turn or stop launching work because usage is high; if the limit is near, keep long-running lanes going so the work in flight finishes. Report "done" only when everything on the list is finalized. Newer than the stop rule in [[quality-bar-and-stop-rule]]; see also [[weekly-limit-keep-working]], [[overnight-autonomy-relay]].
