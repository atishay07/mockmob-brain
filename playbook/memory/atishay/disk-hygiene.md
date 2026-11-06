---
name: disk-hygiene
description: "C: fills from agent worktree build output (.next, flutter build) and temp leftovers; sweep script exists and must run before builds and after every wave"
metadata:
  node_type: memory
  type: feedback
  originSessionId: b7e1b5da-f870-46f3-a18e-ee64c0679147
  modified: 2026-10-21T08:13:01.928Z
---

C: has filled twice: 14 Oct (temp leftovers, 200 GB freed) and again 21 Oct 2026 (1 GB free at 12:20 am). The owner's words, 21 Oct: "We had a standing rule ... every agent will, from now on, follow practices that will not fill up the space again ... in just barely 2, 3 days, you have filled 200 GB again."

**Why:** every agent worktree (about 300 since 17 Oct) that builds leaves `.next` (0.5-1 GB) or `flutter_app/build` (2-5 GB) and `.dart_tool`; nobody deleted them after merging, and the rule was never a script.

**How to apply:** run `bash "C:\Users\atish\Desktop\mockmob copy\scripts\sweep_build_output.sh" "<regex of active worktrees>"` before any build and at the end of every wave; tell every agent to delete its own `.next`/`build` when done; prune merged worktrees (`git worktree remove`) at session end. Related: [[agent-swarm-resource-hygiene]], [[emulator-ram-rule]].

**Standing floor (owner, 21 Oct 1:40 pm): keep at least 50 GB free on C: at all times.** In the promo-film project the big swings were 60 fps PNG frame sequences (10-15 GB per full-film render) and open-source TTS models and venvs (about 40 GB, removed 21 Oct). Delete frame folders right after encoding and check `df -h /c` before big renders.

**Never rm -rf or `git worktree remove` a worktree whose node_modules is a junction** (21 Oct 12:42 am: it emptied mockmob-next/node_modules; `npm ci` restored it). Use `bash scripts/remove_worktree.sh <wt...>`, which unlinks the junction first (`cmd //c rmdir`).
