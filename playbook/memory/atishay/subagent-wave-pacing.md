---
name: subagent-wave-pacing
description: "Measured pacing (31 Oct, 1 Nov): 20-agent cap; Sonnet card authoring ~1.2% of the 5-h window per NCERT PDF (author+review); Opus critics reading screenshots are the expensive part"
metadata:
  node_type: memory
  type: reference
  originSessionId: 16f96fa8-b613-46a8-9eb0-5f9361c78fcd
  modified: 2026-11-01T18:10:17.146Z
---

Measured in the 31 Oct Key cards session (Team plan, Agent tool, Sonnet content agents of ~100-300k tokens each):
- The Agent tool refuses a 21st concurrent subagent ("Concurrent subagent limit reached ... 20"); queue the rest and launch as slots free. Workflows cap at min(16, CPUs-2) = 14 here.
- 20 at once (incl. 2 Opus UI agents with screenshot loops) burned about 2.5% of the 5-hour window per minute; 6-9 at once about 1% per minute. get_usage readings lag, so judge the rate over 5+ minutes.
- To land near 90% at the window reset, divide headroom by minutes left and hold concurrency to match; launch heavy waves right after a reset.

Measured 1 Nov (Learn v2 rounds 3-4 and the subscription card waves):
- Card waves (one Sonnet author + one Sonnet reviewer per NCERT chapter PDF, effort high): about 345k tokens and about 1.2% of the window per PDF. Chemistry's 10 PDFs at K=3 took 43 min. All 108 remaining PDFs fit in about 1.5 windows.
- A 73-agent review round (5 Opus critics each reading 180 screenshots, plus Opus/Sonnet skeptics) took about half a window by itself. For a look after fixes, prefer a local capture plus the orchestrator viewing ~15 key shots, or one Sonnet critic.
- Five fix packets (2 Opus + 3 Sonnet, ~50 min) took about 15-18%.

Related: [[agent-swarm-resource-hygiene]], [[subagent-model-choice]], [[workflow-resume-prefix-cache]], [[workflow-agent-stalls]].


Update 5 Nov 2026: a 7-packet Opus build round (build + judges + reviews) plus an 18-agent Sonnet content wave ran out the 5-hour window in about 3.5 h and moved the weekly meter 62% -> 76%; 7 builders died mid-work with uncommitted edits. Resume with a continuation prompt ("read git status/diff first, finish, do not restart"), Sonnet for spec-clear packets, and one review at integration instead of per packet.
