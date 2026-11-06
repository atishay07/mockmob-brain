---
name: worktree-remove-follows-junctions
description: "2 Nov: `git worktree remove --force` on Windows deleted through a node_modules junction and emptied the shared mockmob-next/node_modules for every web worktree"
metadata:
  node_type: memory
  type: feedback
  originSessionId: c4dbd3b5-f204-4be3-b317-5f8ec24375d4
  modified: 2026-11-02T05:19:06.299Z
---

On 2 Nov 2026 (~10:47 am IST) a subagent removed a temporary worktree with `git worktree remove --force`; the worktree's
node_modules was a junction (-> wt-1020-web16/node_modules -> mockmob-next/node_modules), and the removal emptied the real
folder, breaking tests and dev servers in every web worktree until `npm ci` in mockmob-next.

**Why:** all web worktrees share one node_modules through junctions; Windows removal follows them.

**How to apply:** before removing any worktree, delete its node_modules junction itself (`rmdir` on the link, never `rm -rf`
into it), then remove the worktree. Say this in every agent prompt that creates or removes worktrees. A branch that changes
dependencies gets its own real node_modules, never the shared junction. Real folders as of 2 Nov: wt-1101-r2-home and
wt-1101-content (its junction replaced by its own `npm ci`). Check a link with `(Get-Item <path>).LinkType` in PowerShell.
Related: [[agent-swarm-resource-hygiene]].
