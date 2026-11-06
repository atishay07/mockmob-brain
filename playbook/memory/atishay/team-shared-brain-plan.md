---
name: team-shared-brain-plan
description: "6 Nov: MockMob team brain built (private repo atishay07/mockmob-brain, clone C:\\Users\\atish\\mockmob-brain); owner in bridge mode, CTO installs standalone; GitHub repo creation was pending"
metadata:
  node_type: memory
  type: project
  originSessionId: 204dccba-6bad-4e60-8bb6-73166cbdb15c
  modified: 2026-11-06T16:10:35.771Z
---

Team as of 6 Nov 2026: the owner and the CTO only (no CM yet).

Built on 6 Nov: the team brain at `C:\Users\atish\mockmob-brain`, remote `https://github.com/atishay07/mockmob-brain.git` (private). It holds the docs moved from the code repo's `docs/brain`, the context mirrored from AI OS, every MockMob handover, the playbook (mirrored Claude memory), claims, and the tools in `.brain/` (design in `.brain/DESIGN.md`).

- **Owner machine, bridge mode** (`~/.mockmob-brain/config.json`):
  - AI OS `handoffs/mockmob` is a junction into the brain.
  - `AI OS/scripts/team_bridge.py` is called from hook.py and brain.py: pull at start, background push, claims, edit warnings, mirrors, and a transition catch-up of code-repo `docs/brain` edits until 6 Dec.
  - The old handovers folder is archived at `AI OS/archive/handoffs-mockmob-pre-team-20261106`.
- **CTO machine:** clone the repo, then run `python ~/mockmob-brain/.brain/install.py` (standalone). It gives the same `continuum_*` and `rag_search` tool names.
- **Status on 6 Nov, about 9:45 pm:** the GitHub repo did not exist yet; 10 commits are waiting and push automatically once it exists (empty or README-initialised). Branch `chore/team-brain-pointer` on the code repo (AGENTS.md pointer, docs/brain frozen) still needs a merge.

**Why:** the context lived only on the owner's PC, and the living docs sat on a side branch of the public code repo.

**How to apply:** for MockMob docs, read and update the brain's `docs/`, not the code repo's `docs/brain`. Never run git in the brain by hand. Related: [[preserve-mtimes-when-copying-into-ai-os]], [[single-session-no-subsessions]].
