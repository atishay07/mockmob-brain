# How to choose models for agents and subagents (owner-confirmed)

## Effort levels for sub-agents: a guide, not a rule (owner, 17 Nov 2026, about 12:45 am IST)

In Atishay's words: "usually optimize agents using effort levels. For Opus, you can vary from medium to x high. For Fable, use medium to high, x high. Low and max are not very useful, and medium also is not useful in most cases. Opus at x high provides better results at cheaper costs. Fable medium can be useful in very limited circumstances." And: "many times it's better to switch effort levels and models. For example, Opus on medium can usually be way better than Sonnet on X high. If the task is not scoped well enough, Sonnet can be more inefficient many times ... These should not be restrictive standing rules. The model should use its intelligence at that time for that task to set effort levels, but it should be a proper guide." He asked that it be researched, not taken on his word. Also his: "For 3D work, Fable is clearly the winner."

**Always pass the effort explicitly when starting an agent, and be able to say which level each one runs at.** An agent started with no effort runs at its agent type's default, which the orchestrator cannot read. (API defaults differ by model: Opus 5.5 medium, Fable 5.2 high, Sonnet 5.5 high, Haiku 5.5 medium; the same word is a different amount of thinking on each model.)

### What Anthropic's own guidance says (read 17 Nov 2026 from the bundled claude-api skill: model-migration and cost-optimization)
- Judge cost per finished task, not per token. A stronger model at lower effort often beats a weaker model at high effort; a cheap run that fails still bills, then the retry.
- Opus 5.5: start at medium and test the neighbours; xhigh and max only where a gain is measured; at xhigh turns run long.
- Fable 5.2: start at high. "Most of the capability gain arrives by high"; xhigh "raised scores slightly ... and used many more tokens"; low suits "well-specified tasks, and high-volume workloads such as fast, intelligent subagents"; medium for interactive and everyday work; max for measuring the ceiling. At low and medium it is more likely to stop early on agentic work: say "finish the whole task" in the brief.
- Sonnet 5.5: medium for agentic coding and multistep tool use, low for simple generation, extraction and search; at low it is more likely to skip verifying a change.
- Lower the effort rather than writing "think less"; effort barely changes how long replies are (ask for length in the prompt).

### A small real test (17 Nov 2026; nine read-only agents on the MockMob repo; ONE run per cell, so treat it as a pointer, not proof)
Task A, tightly scoped (three factual questions with file and line evidence; one has a trap: a hard cap that overrides what the control flow suggests):

| Model and effort | Tokens | Tool calls | Time | Result |
|---|---|---|---|---|
| Sonnet xhigh | 103k | 11 | 92 s | all three right |
| Opus medium | 97k | 7 | 91 s | one WRONG (missed the cap, answered 4 where the truth is 2) |
| Opus xhigh | 108k | 9 | 92 s | all right, the most exact |
| Fable medium | 108k | 5 | 81 s | all right |
| Fable high | 107k | 10 | 86 s | all right |

Task B, loosely worded (the owner's one sentence about a reminder chip; "write the plan a developer needs"; scored by me against ten things a good plan should catch):

| Model and effort | Tokens | Tool calls | Time | Score | What it missed or added |
|---|---|---|---|---|---|
| Opus medium | 104k | 11 | 106 s | about 6.5 | right core plan; no preview check, no stale comments elsewhere, no product consequence |
| Sonnet xhigh | 141k | 27 | 192 s | about 7.5 | found the preview and five stale comments; wrongly said "no layout gap"; added unasked doc work |
| Opus xhigh | 138k | 32 | 255 s | about 9 | launch date, the UTC/IST boundary test, and the consequence (four days a week the page loses its only entry) |
| Fable high | 147k | 28 | 188 s | about 9 | the layout shift, a wasted network read, the same consequence |

What it showed, honestly:
- **A sub-agent has a fixed cost of about 90-100k tokens and 80-90 seconds whatever the model or effort.** For a small scoped task the effort level changed neither cost nor time; it only changed whether the answer was right. So do not pick low or medium to "save" on small tasks, and do not start an agent at all for something two tool calls settle.
- **Opus medium was the only one to get a fact wrong, and was the shallowest on the loose task** (though the quickest). On this sample his "medium is not useful in most cases" held for Opus.
- **Opus xhigh matched Fable high on the loose task** at about the same tokens (Opus tokens cost half of Fable's at list price) but took a third longer. His "Opus at xhigh gives better results at cheaper cost" held for depth; Fable high was faster.
- **Sonnet xhigh was not cheap:** on the loose task it used as many tokens and as much time as Fable high for a weaker plan, and it invented extra work. On the scoped task it was correct. His "a badly scoped task makes Sonnet inefficient" held.
- **"Opus medium beats Sonnet xhigh" did NOT show here:** Sonnet xhigh was more thorough than Opus medium on both tasks, at 1.4 times the tokens and 1.8 times the time on the loose one. The comparison that did hold: when tempted to run Sonnet at xhigh, run Opus at high or xhigh instead (same tokens, better result).
- Not tested: building code, long runs, UI taste, low, max, Haiku, Fable xhigh. Re-run a sweep like this when the models change (cost: about 1 million sub-agent tokens).

### How to choose (use judgement; these are starting points)
Ask four things about the task: how completely is it specified, what does a wrong or shallow answer cost, does it need taste, how long will it run.

| The task | Start with |
|---|---|
| Money, credits, security, data rules; code review; anything where a missed case is expensive | Opus xhigh (a second, independent Opus xhigh for the review) |
| A loosely worded request, a plan, a diagnosis, "work out what this means" | Opus xhigh, or Fable high when speed matters or taste is involved |
| UI and product design work judged on taste; a redesign; copy with a voice | Fable high (xhigh only for the single hardest long piece) |
| 3D, Blender or Mobi art direction | Fable (owner's rule), high |
| A well-specified build lane with tests or a gate to catch mistakes | Opus high |
| A fully specified, mechanical change or a bulk repeat of a proven pattern | Sonnet medium or high; Opus medium is the alternative when judgement may still be needed |
| A precise fact-finding question whose answer will be relied on | Opus high or xhigh, Fable medium, or Sonnet high and above: never Opus medium on trust |
| Many small, well-specified pieces at volume | Fable low or Haiku are Anthropic's suggestion; untested here, so check the first few results |
| Measuring a ceiling, or a problem with no time limit | max, rarely; not for routine sub-agents |

Planning notes:
- Scope first. A sharper brief is worth more than a higher effort level; effort cannot recover facts the brief left out.
- Mix levels inside one piece of work: decide and specify at high effort on the strongest model, execute the mechanical parts lower, review at xhigh.
- Lower effort stops earlier and verifies less: when using medium or low, say "finish the whole task and verify it" in the brief and name the check.
- Fewer, larger agents beat many tiny ones (the fixed cost above); batch related questions into one agent.
- xhigh runs long: plan for it (background, no short timeouts), and keep it for work where depth pays.
- The 5-hour usage window is the real limit in practice: six build agents (five Opus, one Fable, default effort) used about 35 percent of a window in 40 minutes on 16 Nov.

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
