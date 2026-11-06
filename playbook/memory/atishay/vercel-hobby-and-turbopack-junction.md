---
name: vercel-hobby-and-turbopack-junction
description: "4 Nov: Vercel is Hobby (100 deployments/day, 1 build at a time) so never push hundreds of branches (use archive tags); Turbopack panics on a junctioned node_modules, build it in wt-1101-content"
metadata:
  node_type: memory
  type: reference
  originSessionId: c5a8da45-5c74-46ba-abca-73f6160b75cd
  modified: 2026-11-03T21:30:50.157Z
---

- **Vercel plan is Hobby** (checked 4 Nov 2026 via get_git_deployment_context): 100 deployments a day, one build at a time. Every pushed branch starts a preview build, so pushing many branches queues ahead of production and can hit the daily cap. For archiving, push `archive/<branch>` **tags**: a tag push started no deployment (tested 4 Nov). Push only the few branches people need.
- **Turbopack (`next build`, what Vercel runs) panics locally on a junctioned node_modules** ("Symlink [project]/node_modules is invalid, it points out of the filesystem root"). `next build --webpack` works in junction worktrees. For the Turbopack gate, check out the ship commit detached in `wt-1101-content` (real node_modules) and build there. See [[vercel-font-fetch-flake]], [[worktree-remove-follows-junctions]].
- **Commands for the owner** must name the repository (`git -C "C:\Users\atish\Desktop\mockmob copy\mockmob-next" ...`): he runs them from `C:\Users\atish\Desktop\mockmob copy`, which is not a git repository.
- The auto-mode classifier blocked a 610 MB push to GitHub (as data exfiltration) and killing orphaned processes; leave those to the owner, with the exact command.
