---
name: council-skill
description: "26 Nov 2026 - the owner asked for an LLM council / roast-room skill on subscriptions (no API keys); built at ~/.claude/skills/council; GPT sits through Codex, Gemini needs his sign-in"
metadata:
  node_type: memory
  type: reference
  originSessionId: 9d2a0d17-12b8-4219-9c55-75319e5e7bf7
  modified: 2026-11-25T19:05:46.615Z
---

The owner asked (26 Nov 2026) for an "LLM Council" skill like the public ones: models from several companies debate and agree, plus "roast room" modes that take on famous personalities' ways of thinking. His condition: use the subscriptions on this PC, never API keys or OpenRouter ("that leads to paying API prices"); tell him when a sign-in step is his.

Built: `C:\Users\atish\.claude\skills\council\` (SKILL.md, `council.mjs`, `personas.md`). Positions alone, then anonymous review with a ranking, then the chair's verdict. A sitting's folder is `<project>/tmp/council/<date>-<slug>/`.

- GPT seat: Codex CLI, signed in with ChatGPT; the runner uses the lean `~/.codex-alt` home (see [[codex-image-gen-cheap]]). Works.
- Gemini seat: the Gemini CLI is installed (0.40.1) and NOT signed in. His step: run `gemini` in a terminal once and pick "Login with Google". The runner detects it and seats Gemini by itself after that.
- Claude seats: the chair's own subagents (opus, sonnet, haiku), each a fresh agent, never a fork.

First use: the phone landing declutter, `wt-1110-convert/tmp/council/2026-11-26-landing/verdict.md` (five seats, 5-0). Lesson from it: GPT's position was the vaguest and ranked last, but its review caught the same weak point the Claude seats did; the value was in the review round.

**How to apply:** he said he gets conflicting opinions from people and wants independent thinking, so convene it before contested design calls and say who sat. Where the council contradicts something he asked for in his own words (the Compass slider plays by itself, 18 Nov), his word stands; say so in the verdict. Related: [[orchestrator-thinks-agents-do]], [[web-restructure-rejected]].
