---
name: no-fable-when-limited
description: "17 Nov 2026: Fable limit hit mid-wave (3 lanes died); owner said don't spawn Fable agents, use Opus or do it in context"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 5d81fcac-1f7d-429d-a866-b6bab8e4d67d
  modified: 2026-11-16T21:52:39.978Z
---

On 17 Nov 2026 (about 2:27 am IST) the Fable usage limit was hit while three Fable lanes were building; they stopped with partial work and their workflow steps hung waiting to retry. The owner: "From now on, don't spawn Fable agents. Stick to Opus ... or don't spawn agents. Just do most of the work in this context window."

**Why:** Fable's separate limit can cut a wave in half; stalled Fable steps in a workflow can wake when the limit resets and collide with work done since.

**How to apply:** Default sub-agents to Opus (pass effort). If a Fable lane dies, commit its partial work as WIP, finish it yourself, and stop the workflow before the reset time. See [[subagent-model-choice]], [[resume-subagents-after-limit]].
