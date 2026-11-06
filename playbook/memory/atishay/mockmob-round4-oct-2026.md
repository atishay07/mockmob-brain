---
name: mockmob-round4-oct-2026
description: Round 4 (3 Oct 2026) Pip guide + regression lessons; how to verify MockMob locally without fooling yourself
metadata:
  node_type: memory
  type: project
  originSessionId: 1fd4f091-c37a-4fb9-bba4-d2991912b6cc
  modified: 2026-10-03T08:49:56.256Z
---

Round 4 shipped locally (not deployed): one Pip "perch handoff" guide on the homepage (PipGuide.jsx), restored Arena entry/exam-day card motion, Result next step from computePrepOSInsights. Records: docs/brain/ROUND4-NOTES.md, MOTION.md.

Non-obvious lessons:
- Never animate `transform` on the Arena shell or a page `.view`: they contain position:fixed UI (sidebar, phone dock, modals) that re-anchors mid-animation. Fade containers, rise leaves. Round 3 "fixed" this by switching all motion off, which the owner reported as a regression.
- Owner wants Pip as ONE travelling, reacting character, not per-section stickers; no Pip motion while answering.
- Grid `auto` tracks + nowrap text silently cut panels off (body overflow-x hidden hides it); root-overflow checks miss it, so measure element escape.

**Why:** these cost a full round of owner feedback.
**How to apply:** open the dev server via http://localhost:3000 (127.0.0.1 fails the HMR origin check and never hydrates); bring the chrome-devtools page to front or rAF drops to ~2fps; `window.__pipSlow = N` (dev only) slows Pip flights for frame captures. Related: [[mockmob-owner-round2-oct-2026]].
