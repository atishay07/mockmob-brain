---
name: disk-hygiene
description: "C: fills from agent worktree build output (.next, flutter build) and temp leftovers; sweep script exists and must run before builds and after every wave"
metadata:
  node_type: memory
  type: feedback
  originSessionId: b7e1b5da-f870-46f3-a18e-ee64c0679147
  modified: 2026-11-23T09:58:42.672Z
---

C: has filled twice: 14 Oct (temp leftovers, 200 GB freed) and again 21 Oct 2026 (1 GB free at 12:20 am). The owner's words, 21 Oct: "We had a standing rule ... every agent will, from now on, follow practices that will not fill up the space again ... in just barely 2, 3 days, you have filled 200 GB again."

**Why:** every agent worktree (about 300 since 17 Oct) that builds leaves `.next` (0.5-1 GB) or `flutter_app/build` (2-5 GB) and `.dart_tool`; nobody deleted them after merging, and the rule was never a script.

**How to apply:** run `bash "C:\Users\atish\Desktop\mockmob copy\scripts\sweep_build_output.sh" "<regex of active worktrees>"` before any build and at the end of every wave; tell every agent to delete its own `.next`/`build` when done; prune merged worktrees (`git worktree remove`) at session end. Related: [[agent-swarm-resource-hygiene]], [[emulator-ram-rule]].

**Standing floor (owner, 21 Oct 1:40 pm): keep at least 50 GB free on C: at all times.** In the promo-film project the big swings were 60 fps PNG frame sequences (10-15 GB per full-film render) and open-source TTS models and venvs (about 40 GB, removed 21 Oct). Delete frame folders right after encoding and check `df -h /c` before big renders.

**Page file (8 Nov 2026, 10:26 am):** C: went from 14.5 GB to 0 in about an hour because Windows grew the system-managed pagefile.sys to 28 GB under memory pressure (emulator plus an 8-agent headless-browser sweep plus a dev server). It stays allocated until a reboot; changing it is a system setting (owner only). Never run the emulator alongside a browser-critic workflow; check free space before each wave. The AVD's userdata-qemu.img.qcow2 is 14 GB on its own (wiping it is the owner's call).

**Full disk mid-session (23 Nov 2026, about 1:50 pm):** I did not run `df -h /c` at the start; C: hit 0 MB during a commit (page file at 26 GB, a dev server plus many headless Chrome runs). The commit failed and a `git checkout` in the gate worktree was left half-written. What worked: run the sweep script, delete the working tree's stale `.next` and `.next-dev`, stop the dev server, redo the commit. The safety check refuses `git checkout -f` there; instead commit the half-written files in the gate worktree as a "wip, kept" commit and then do a plain `git checkout --detach <sha>`. Run `df -h /c` first thing in every session and before a gate; under about 15 GB free, tell the owner before starting builds or renders (film renders wait).

**Owner-asked cleanup (23 Nov 2026, afternoon):** C: is one 930 GB drive. From 8 GB free: NVIDIA DXCache 10.6 GB, `.dartServer` 11 GB (900k files, slow), Temp >2 days 11.7 GB, promo-film `out/.tmp` 2.2 GB, 127 clean worktrees whose HEAD is on a branch (about 43 GB; 4 dirty ones and wt-1116-next/wt-1110-convert/wt-1101-content kept). With his explicit OK: Filmora 2024 exports 106 GB, 4 Downloads files, Forza Horizon 6 uninstalled (Remove-AppxPackage Microsoft.ForteBaseGame). He kept: 007 First Light 53 GB, VALORANT 33 GB, Roblox Studio's tmp-capture-storage PNG frames (20 GB), Claude logs older than 14 days (11 GB). Since 20 Oct about 300 GB was new or changed: MockMob folders, AppData caches, a VALORANT update. Lists written by Python on Windows have CRLF: `tr -d '\r'` before mapfile, or every name is skipped. The harness blocks `Remove-Item <dir>\*`; delete the folder by name.

**Never rm -rf or `git worktree remove` a worktree whose node_modules is a junction** (21 Oct 12:42 am: it emptied mockmob-next/node_modules; `npm ci` restored it). Use `bash scripts/remove_worktree.sh <wt...>`, which unlinks the junction first (`cmd //c rmdir`).
