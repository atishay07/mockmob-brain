---
name: subagent-model-choice
description: "Pick subagent models per task (24 Oct 3:30 am newest): Opus only for real thinking/taste; Sonnet when context is given and it just needs doing (Opus can harm there); Haiku medium/high for small jobs; xhigh only Sonnet/Opus; max rarely; speed matters"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 604ced81-3aa7-4deb-b42c-f324ca5f51e2
  modified: 2026-10-20T16:17:01.634Z
---

**NEWEST (24 Oct 2026, about 3:30 am IST, Reel night; wins over everything below):** "use the subagent interaction judiciously between Opus and Sonnet, and even Haiku ... Your objective is not to just save tokens. Mainly ... use the appropriate model for appropriate things because speed is also important. For many tasks, Opus is not only overkill, but it can also harm it, because not everything needs a lot of thinking. If you are giving it enough context and it just needs to do it, then Sonnet is perfect for that." "for smaller tasks, like less than maybe 100,000 or 200,000 tokens, Haiku can also be used at medium or high effort only. Extra high is reserved for Sonnet and Opus, and use max effort level only rarely."
- Opus (high, xhigh when it truly needs deep thought): open-ended design / taste calls, judges against a reference, hard debugging.
- Sonnet (medium/high; xhigh allowed): a lane with an exact spec from the orchestrator, fix rounds with a failure list, sound sync, renders + gates with measurement, independent checkers that follow a checklist.
- Haiku (medium or high, never low per this rule, never xhigh): small bounded jobs under about 100k-200k tokens: run a render script, extract frames, run a known check, copy/deliver files.
- max effort: almost never.
- Orchestrator writes exact specs so Sonnet can just do it ([[orchestrator-thinks-agents-do]]).

Choose the model per agent, not by default. 12 Oct the owner allowed Opus at high effort for important work ("you can also spawn Opus on a high effort level as a subagent ... You have the flexibility"). 13 Oct he questioned running about ten Opus agents: "only do it if you actually think it is worth it", "It's not an issue even if it consumes a lot of limit, but it will take a lot more time."

**Why:** usage is affordable; wall-clock time is what he minds. Opus at high effort is slower per agent, and the first app pass defaulted almost every builder to Opus without a per-task reason.

**How to apply:**
- Opus, high effort: signature design and motion (the Mobi rig, the result reveal), hard multi-step flows (NTA mode, practice correctness), security and auth, integration across features, final fix passes, design or plan synthesis.
- Sonnet: research and inventories, porting existing website features, routine screens, checklist reviewers (truth and flow, performance and accessibility), mechanical edits.
- Time is set by the slowest sequential chain; cut sequential rounds (run a second review round only when the first finds serious issues) before downgrading critical-path agents.
- State the routing in the reply when launching a workflow. Keep memory limits on the PC in mind ([[emulator-ram-rule]]). See also [[mockmob-design-direction]].

**20 Oct 2026, 7:34 pm IST (D188), newest:** he caught 14 Opus agents in one review workflow (3 reviewers plus 11 per-finding verifiers): "Is there any reason to only use Opus here?" The cause was that workflow `agent()` calls with no `model` inherit the main session's Opus. Usage is not a constraint for him ("even 100 agents if required"), but speed and efficiency are.
- Always pass `model` on every `agent()` and Agent call.
- Per-finding verifiers, walkers and screenshot capture are Sonnet.
- Opus is for taste judges, motion and tricky logic fixes only.

**Owner restated it again (15 Oct 2026, ~21:30 IST). This wins over everything below it:** "Why are you using 10 Opus agents/subagents at once?"
- **Sonnet does the heavy lifting:** builders, features, ports, perf passes, truth and flow reviews, checkers.
- **Haiku:** basic, quick tasks under about 5 minutes and about 100k-200k tokens: moving things around, running a known check, tagging.
- **Opus subagents only for complex UI/UX, extreme motion graphics and polish passes.**
- Planning and orchestration are the main session's job. Do not spawn planner or synthesis subagents for them.
- Re-route models every time a run is resumed or copied. Don't inherit an older script's choices. On 15 Oct a resumed run used 11 Opus agents because it copied the previous script.
- **Set effort explicitly on every workflow agent:**
  - Opus motion and design: high;
  - Sonnet builders: medium, or high for tricky logic;
  - Sonnet checkers and reviewers: medium;
  - Haiku: low.
  - Omitting it inherits the session's effort.

**Design skills (16 Oct 2026, ~00:50 IST):** every design-level agent (UI, motion, visual polish, critique) loads three skills with the Skill tool: ui-ux-standards first (the owner's rules; its section 10 AI-slop list wins every conflict), then impeccable (critique and polish), then frontend-design (visual direction). Before this, agents had been told only to follow ui-ux-standards.

**Owner restated the routing (14 Oct 2026, ~14:15 IST), this wins over the lines above:**
- Opus: the orchestrator, and important tasks that need the best quality (it is fine to use several when the work is important).
- Sonnet: the main heavy lifter for code and for frontend UI/UX design.
- Haiku: smaller tasks under about 100k tokens: routine work such as handing over code, basic code, checking, tagging, judging, solving, and bounded content generation such as authoring a batch of questions.
He objected to spawning many Sonnet agents to write questions ("It will just eat up the usage so much"): question authoring and verification go to Haiku.
