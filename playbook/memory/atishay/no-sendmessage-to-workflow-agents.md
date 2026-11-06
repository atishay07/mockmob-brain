---
name: no-sendmessage-to-workflow-agents
description: SendMessage to a running Workflow agent resumes a DUPLICATE copy in the same worktree; use a shared coordination file instead
metadata:
  node_type: memory
  type: feedback
  originSessionId: b7e1b5da-f870-46f3-a18e-ee64c0679147
  modified: 2026-10-20T11:29:19.855Z
---

Never SendMessage to an agent that a Workflow spawned while it is still running. On 20 Oct 2026 (session b7e1b5da) relaying a contract note to three Mob V4 workflow agents "resumed" each one as a second live copy in the same worktree; they collided, and stopping them killed the originals too (about 4 minutes lost, one restart workflow).

**Why:** the workflow runner owns those agents; SendMessage starts a separate resumed instance from the same transcript.

**How to apply:** put cross-agent contracts in the prompt up front; for mid-run coordination use an append-only file (e.g. mockmob-next/tmp/v4-coord.md) that every agent is told to read every 15 minutes. SendMessage is fine for agents started with the Agent tool. Related: [[agent-swarm-resource-hygiene]], [[orchestrator-thinks-agents-do]].
