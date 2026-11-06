# Brief: Disk clean-up of stale build output (model haiku), launched 2026-10-18T20:33:14.124Z

Free disk space on C: safely. Folder: C:\Users\atish\Desktop\mockmob copy. It holds many git worktrees named wt-*. Delete ONLY these git-ignored build output folders inside STALE worktrees: flutter_app\build, flutter_app\.dart_tool, flutter_app\android\.gradle, .next (web build cache). NEVER delete any tracked file, never run git clean, never delete a whole worktree, never touch node_modules (they are junctions to a shared folder; deleting through a junction would destroy the shared copy).

ACTIVE worktrees you must NOT touch at all: wt-v15-2, wt-v15-3, wt-rel10, wt-rel11, wt-rel9b, wt-rig-r9, wt-rig-site, wt-rig-base, any folder starting with wt-1019, mockmob-hotfix, mockmob-next.

Steps: 1) Run `powershell -NoProfile -Command "Get-PSDrive C | Select-Object Used,Free"` and note free space. 2) For each other wt-* folder, check each of the four paths exists; confirm it is git-ignored with `git -C <worktree> check-ignore -q <relative path>` (skip it if not ignored); confirm it is not a junction or symlink (PowerShell: (Get-Item <path>).LinkType must be empty); then delete it with `cmd /c rmdir /s /q "<path>"`. 3) Report free space after, how much was freed, and the list of deleted paths (count per worktree). Do not delete anything else.
