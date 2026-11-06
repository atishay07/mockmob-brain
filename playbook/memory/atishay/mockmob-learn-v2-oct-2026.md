---
name: mockmob-learn-v2-oct-2026
description: "How MockMob Learn v2 was built/released (5 Oct 2026) — release worktree, content pipeline, two-phase import, local sign-in limits"
metadata:
  node_type: memory
  type: project
  originSessionId: d7e7bd6d-a948-4844-b80f-f7c15b7ef64b
  modified: 2026-10-04T19:29:06.532Z
---

Learn was rebuilt (5 Oct 2026) as one loop: Learn → Lock it in → Apply, after the owner said nobody could tell what Learn did. Released as origin/main 78a627f + d3ec177 from the isolated worktree `artifacts/study-suite/release` (branch `codex/connected-study-suite`); the original checkout's local main (6c5e05b, dirty owner work) was deliberately left alone and is now behind origin/main.

Content: authored in `data/study/authored/*.mjs` → `build-study-content.mjs` → `validate-study-content.mjs --write --strict` (needs git-ignored NCERT PDFs + WordNet dict under data/study/sources; missing sources quarantine) → `study-content-v2-import.mjs` (PGlite dry run) → `apply-study-content-v2.mjs insert|supersede|verify` (refuses any project except isrxrxzjocewrdureyhp). Insert before deploy, supersede after deploy.

**Why:** the owner judges by comprehension in the real UI, not by tests or routes.
**How to apply:** walk the journey as a student in the browser before claiming done. The browser pane only reaches localhost ports it started, and Supabase OAuth does not return to localhost:3011, so signed-in checks are easiest on www.mockmob.in after deploy (owner signs in there). Related: [[mockmob-differentiator-decision-oct-2026]].
