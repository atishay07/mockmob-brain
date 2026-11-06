---
name: build-and-look-loop
description: "20 Oct: every building agent captures visuals continuously while it builds, critiques each, improves in the same loop; walks never stall on sign-in"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 801f0d1a-2efd-451c-9fc9-8b548c3a6c86
  modified: 2026-10-19T19:08:49.040Z
---

Every agent that builds UI must capture visuals continuously while it works (emulator screenshots and motion frame sequences, or goldens opened with Read), look at each for anything out of place or that could be better, and fix it in the same loop. Build and test go hand in hand; no "build now, walk at the end".

**Why:** owner D150 (20 Oct 12:40 am): "if testing and working go hand in hand, we can always achieve a better result". On 19-20 Oct an emulator walk spent an hour stuck on staging sign-in and never tested the Mob; the owner watched it and called it wasted. A truth audit found v11 missed the things he looks at most (course search, clock, finish screen) because fixes were tested on the wrong field and never seen on device.

**How to apply:** put this loop in every UI brief. Walks use the fixture/demo mode or a scripted fast staging sign-in, never OTP typing; time-box any sign-in trouble to 10 minutes. The main session reviews the captures against the owner's words before he sees anything. Related: [[device-truth-testing]], [[orchestrator-thinks-agents-do]].
