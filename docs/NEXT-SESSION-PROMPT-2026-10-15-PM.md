# Paste this as the first message of the next session

Continue MockMob from session cc0bf1af, which stopped safely at about 14:00 IST on 15 Oct at the usage limit. Everything is committed. No workflow, server or build is running.

1. Call continuum_start for project "mockmob".
2. Read fully, in order:
   - C:\Users\atish\Desktop\mockmob copy\mockmob-next\docs\brain\HANDOFF-2026-10-15-AFTERNOON.md
   - HANDOFF-2026-10-15-MIDDAY.md (same folder), sections 1 and 7 of HANDOFF-2026-10-15-FULL.md
   - the memory files web-restructure-rejected.md, features-over-retesting.md, mockmob-design-direction.md and quality-bar-and-stop-rule.md
3. Then, in order:
   a. **Website v2** (wt-web-v2, branch web/v2-1015, WIP cf51d4d8). Run the stopped check: review against web-restructure-rejected.md (nothing plainer or less animated than live), lint, the suites once, one build, and fixes. Then start preview_start "web-v2-local" and give me http://localhost:3110 with the pages to look at. I review on the local server, not HTML files. Push only after my OK.
   b. **Mistake Lab v4, the USP.** Read mockmob-next/tmp/mistake-lab-v4/SPEC.md and concept.html, and the visions in the wf_7a498cbc-116 journal. Show me the concept in a few lines. Build slice 1 on web (wt-web-refine, web/alive-1015) and the app (wt-phase2, ui/phase2) together, then merge it into web/v2-1015. It must be deep, truthful, easy to understand, and something no one else can give.
   c. **App:** check feature wave 1 (WIP 6e6db1aa) once. Remove K0's screens for the cut features (chapters, formats, week review), and keep revise, rulebook and leaks only if the Lab spec uses them. Merge into feat/app-and-web, build APK v6, zip it and send it.
   d. **Web halves** of motion and art (M1, M2, I1, I2): build them into web/v2-1015 from the webHandoff notes in the wf_7f70b018-bc2 journal.
   e. When I have done one repair, verify the v3 cost in runtime_ai_requests.

Rules:
- Depth over breadth: perfect one feature rather than add many. Never simplify by cutting richness.
- Opus for all owner-visible UI. Light checks once per wave; no emulator recordings unless I ask.
- Never drive my browser, sign in or create accounts.
- Fan out agents on disjoint paths. Give honest percentages.
- Stop at about 95% usage with a handoff. The usage hook may show my other account's number right after a switch.
