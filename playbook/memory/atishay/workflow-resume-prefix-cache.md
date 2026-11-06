---
name: workflow-resume-prefix-cache
description: Workflow resumeFromRunId reuses only the unchanged PREFIX of agent() calls in call order; to re-route a stopped run, write a fresh script with just the remaining steps
metadata:
  type: feedback
---

24 Oct 2026, 4:40 am (Reel night): I stopped a 10-lane workflow at 72 % of the 5-hour window to re-route it to Sonnet, and relaunched an edited copy with resumeFromRunId. Its first lane's call had changed, so every call after it in call order ran LIVE again, even ones whose prompt + opts were byte-identical (finished builds restarted; stopped within 30 s).

**Why:** the resume cache is an ordered prefix, not a content match; in parallel lanes, one edited early call invalidates everything after it.

**How to apply:**
- To change models, prompts or concurrency of a stopped run, generate a FRESH script that runs only the steps left (pull the pending failures and results from the old journal.jsonl), as tools/reel916-orch/mk_resume3.py does.
- Use resumeFromRunId only for the same script and args (a crash or limit stop).
- Pace by usage before launching big Opus fan-outs: ~10 Opus agents burned about 1 % of the 5-hour window per minute ([[agent-swarm-resource-hygiene]], [[subagent-model-choice]]).
