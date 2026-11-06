# How to choose models for agents and subagents (owner-confirmed)

## Current rule (owner, 24 Oct 2026, about 00:10 IST): it supersedes the routing rules above for Claude agents
In Atishay's words: "The only case when Sonnet is to be used is when something is very easy to do and speed matters more than the task difficulty... you should not use any rules to think about when to deploy Opus or when to deploy Sonnet. Only remember you have infinite resources. You can choose to spawn Opus every time... Mix it between both of them... The only criterion is the best possible design."

What this means:
- Choose each agent's model and effort for the best possible result, case by case, with no fixed size or cost rules.
- Opus is the default for anything that needs thinking, judgement or taste: design, hard builds, testing, review, verification.
- Sonnet only for easy, mechanical work where speed matters more than difficulty.
- Effort is chosen per task too. The earlier "medium or lower" cap no longer applies.

Source: Atishay's own words, 10 Oct 2026 (orchestration rules) and 11 Oct 2026 about 23:55 IST (refinement). Applies to Claude Code and Codex sessions in every project. Evidence status: owner statement.

- The main session orchestrates: plans, delegates, reviews, and keeps shipping while subagents work. Subagent effort medium or lower.
- Claude side: Sonnet for UI/UX, exploration and any long-running task; Haiku only for short, bounded work.
- Long task rule, in Atishay's words: Haiku "is not actually built or meant for any task which is expected to exceed 100k, 150k tokens ... It's not good with long tasks ... if something is a long-running task which will run for more than 10, 20, 30 minutes, then it's usually not a wise thing." So: estimate size and duration before delegating; anything likely over about 100k tokens or 10-20 minutes goes to Sonnet.
- Refinement (owner, 13 Oct 2026 about 01:35 IST): Opus orchestrates, Sonnet is the heavy workhorse, Haiku is for minimal code-only tasks. Opus subagents are allowed when a task is really important and Opus quality is needed (for example strategic or creative planning); the orchestrator may also do such work itself when required. Otherwise keep the current workflow.
- Codex side (earlier owner rule): choose each subagent and effort deliberately; prefer GPT-6 Luna for subagents; avoid GPT-6.1 Sol for bulk work because it roughly doubles usage.
- Continuum's own background calls (short claude -p summaries, triage, briefs) may stay on Haiku: each is a single small call.
- Post a short progress update about every 30 minutes on long work; ask when how to proceed is genuinely unclear.
