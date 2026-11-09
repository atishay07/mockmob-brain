---
name: junction-create-with-powershell
description: "10 Nov 2026 — `cmd //c mklink /J` from Git Bash made a broken node_modules junction (target C:\\C:\\...); create junctions with PowerShell New-Item"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 585e670b-982c-44d4-b5f2-1ceca346163e
  modified: 2026-11-09T20:55:35.392Z
---

Create a worktree's `node_modules` junction with PowerShell, not `mklink` through Git Bash:
`New-Item -ItemType Junction -Path node_modules -Target "C:\Users\atish\Desktop\mockmob copy\wt-1103-web-cards\node_modules"`,
then `Test-Path node_modules\next\dist\bin\next`.

**Why:** on 10 Nov 2026 `cmd //c "mklink /J node_modules \"C:\\Users\\...\""` from the Bash tool reported success but
the junction pointed at `C:\C:\Users\...`; `ls node_modules` still printed a name, and the dev server died with
"Cannot find module .../next/dist/bin/next".

**How to apply:** after creating any junction, check a real file through it before starting a server or a build. To
remove a broken one use `cmd /c rmdir node_modules` (the link only), never a recursive delete; see
[[worktree-remove-follows-junctions]] and [[vercel-hobby-and-turbopack-junction]].
