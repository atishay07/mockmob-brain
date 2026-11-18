---
name: pre-gate-checks
description: "18 Nov 2026 — before the 15-minute release gate, run test:app and the landing checklist by hand; lanes only run the suites their brief names"
metadata:
  node_type: memory
  type: project
  originSessionId: 777be139-a000-4c98-9286-70590b597225
  modified: 2026-11-18T16:15:29.954Z
---

Before starting the MockMob release gate (`wt-1116-next/tmp/gate2.sh`), run two things in the release worktree first:
`npm run test:app` (about a minute) and `node --test data/tests/landing_checklist_1104.test.mjs`.

**Why:** on 18 Nov 2026 a lane (arena-b) moved Practice's ticket heading from the mode to the subject, against owner note G26; no suite the lane ran said so, and `src/components/start/__tests__/startModel.test.mjs` caught it only inside the full gate, costing a second 15-minute gate. The same evening `landing_checklist_1104.test.mjs` (the owner's landing checklist, L-040: no keyframe may animate a layout property) flagged my own `dd-marker-run` keyframe after it was already live: that file is in no `test:*` script, so the gate never runs it.

**How to apply:** after merging lanes and before every gate. In lane briefs, name `src/components/start/__tests__/startModel.test.mjs` for anything touching Practice. Related: [[gate-in-wt-1116-next]], [[landing-checklist-gate]].
