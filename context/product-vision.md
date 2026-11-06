# Product vision (owner-confirmed 11 Oct 2026, about 02:20 IST)

Atishay confirmed this direction after rejecting a plain rebuild. Their own words, with sources, are in [vision recovery](../audits/vision-recovery-20261011.md).

## What Continuum is
- "A complete agentic OS ... a self-made Obsidian kind of thing" where every agent on this computer (Claude Code, Codex) automatically feeds the brain and is fed by it. A harness "like T3 Code" where agents work together over one brain. MockMob is the main project.
- One integrated OS, not a hub of separate pages ("Everything should have been integrated").
- The look follows Atishay's references: the Jarvis HUD (brain centre stage, Claude Code | Codex switch, vitals, weekly usage gauge, directives, voice, terminals) and Jack Roberts' Agentic OS (sidebar workspace, Memory "visual cortex" graph with Neural / Sphere / Network modes and memory-source toggles). "When I open the final complete project, I should be amazed."

## Confirmed choices
- Shell: an Agentic OS-style sidebar workspace (Home, Agents, Memory, Projects, Usage, System). Home is a Jarvis-style HUD: the brain centre stage, vitals and usage on the left, each project's next action, blockers and "you asked to remember" on the right, the handover feed and terminals below.
- Build on the v2 hub (apps/3d-brain hub on port 4640); keep its richness; fix what is broken. Do not replace what Atishay sees with something sparser.
- Order: 1) one Memory core (single graph, Neural / Sphere / Network modes, memory-source toggles, search with sources, no lag); 2) Home HUD; 3) every control does something (Claude Code / Codex switch, Calm/Pro wired or removed, Graph and Cockpit folded in, Agents shows who is working on what). Then Projects/MockMob, Inbox, Schedule and System, voice last.
- Every change is previewed (screenshots or a side route) and approved by Atishay before it replaces anything on 4640.

## Rules that stay
Copy, never move or delete without OK; usage only from TokenMeter; unknown costs are unknown; no paid runs or deploys; agent runs only on Atishay's click; one owner for the product; short updates, IST times.

[Priorities](priorities.md) · [Continuum](../wiki/entities/continuum.md)
