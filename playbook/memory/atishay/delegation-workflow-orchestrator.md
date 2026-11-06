---
name: delegation-workflow-orchestrator
description: "Owner's preferred agent workflow on MockMob - Opus orchestrates/plans, Sonnet does heavy lifting, Haiku basic tasks"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 71150a0f-0d49-4294-a41f-f71cd49c46c7
  modified: 2026-10-08T19:00:57.350Z
---

Act as orchestrator: Opus plans, integrates and makes final judgments; assign heavy implementation/analysis tasks to Sonnet subagents and basic/bounded tasks (searches, drafting, simple audits) to Haiku subagents.

**Why:** owner (9 Oct 2026) researched this as best for token efficiency and output quality; their Claude usage is limited.

**How to apply:** for multi-step generator/app work, write a plan, then spawn Sonnet for code-heavy or reasoning-heavy pieces (e.g. new contract versions, blind answer derivations) and Haiku for audits/drafts; keep Opus context for review and decisions. Related: [[mockmob-cuet-fit-generator-oct-2026]].
