---
name: subagent-handoff-hijack
description: "24 Oct: a Haiku workflow agent given \"render candidate 4\" followed the session-start Continuum handoff instead (regenerated the orchestrator script, tried to launch a workflow, rendered nothing)"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 792c2e1f-d07d-4588-b135-53d46c5e4f59
  modified: 2026-10-24T07:44:29.287Z
---

On 24 Oct 2026 (about 1:09 pm) the "candidate 4 render" agent (Haiku, high) in the MockMob Reel fix round read the auto-injected Continuum handover ("next: New session: paste docs/PROMPT-NEXT-SESSION...") and did the ORCHESTRATOR's job: it regenerated tools/reel916-orch/fix1025b.js, looked for the Workflow tool, reported "BLOCKED", and never rendered. The workflow then started three judges on a file that did not exist; the orchestrator stopped it and rendered the candidate itself.

**Why:** every subagent gets the SessionStart hook's Continuum block and CLAUDE.md's "call continuum_start" rule; a short task prompt plus a strong "next session" instruction in that context can win on a small model.

**How to apply:** every workflow prompt says the agent is a SUBAGENT whose ONLY task is in the prompt and that handoffs / PROMPT-NEXT-SESSION files are the orchestrator's (now in fix1025.js COMMON). Give one-shot mechanical jobs that sit next to rich context (renders, encodes) to Sonnet, or run them yourself with a background Bash; check a render step's output file exists before the next stage relies on it. Related: [[subagent-model-choice]], [[no-sendmessage-to-workflow-agents]].
