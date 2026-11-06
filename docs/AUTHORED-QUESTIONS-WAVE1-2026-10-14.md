# Agent-authored NTA questions, wave 1 (14 Oct 2026)

Why: the paid factory cannot run (no qualified generator, four-subject code limit, no long passages, expired prices, USD 10.04 left; see FACTORY-RUN-2026-10-14.md). Claude agents on the owner's plan were used instead; no API spend and no ledger change.

Pipeline per question:
1. Sonnet author per batch of 20 (15 for English passage sets), following each subject blueprint and the owner's definition of a 10.
2. Five blind Haiku solvers, two quality judges (NTA-AGENT-RUBRIC) and three CUET-fit judges (NTA-CUET-FIT-RUBRIC).
3. Accepted only if at least 4 of 5 solvers matched the key, both quality judges scored 7 or more with no flag, and the fit median was 8 or more with fewer than two fit flags.
4. Independent Opus spot-check of 90 random accepted items: 74 NTA-ready, 15 practice-grade, 1 reject (one unsound key).
5. Sonnet expert pass over all 496 accepted: 341 ready, 138 repaired (option balance, stem cues, explanations, labels), 2 practice, 15 reject.
6. The 138 repaired items were re-solved blind by three Haiku solvers. All 138 matched the key at least 2 of 3 times.

Result: 479 NTA-grade candidates.

| Subject | Candidates |
| --- | --- |
| Chemistry | 95 |
| English (12 passage sets of 220-300 words) | 59 |
| History | 82 |
| Political Science | 83 |
| Psychology | 79 |
| Sociology | 81 |

Content: docs/brain/reports/authored/wave1-candidates-2026-10-14.json (source "claude-authored-2026-10-14"). Raw files: tmp/authored/.

Not done: publication to the live bank (needs owner approval). Then each published row needs the NTA score records (agent scores, fit scores, content hashes) so the engine can admit it. Wave 2 (Geography, Computer Science, Mathematics, General Test, Biology, English verbal, more History and Political Science) waits until the app UI blitz lands.

Publication and score tooling (prepared 14 Oct, not run against any database): docs/brain/RUNBOOK-PUBLISH-AUTHORED-2026-10-14.md.

Fresh pass and rewording (14 Oct, after the engine check): the 60 repaired-text questions were re-judged on their final text (two quality and three fit judges each; claude-haiku-5-5 throughout). 56 passed; 4 failed and are dropped (an English fit median of 6, a History duplicate-options flag, two Political Science quality scores of 6). The 19 questions the NTA engine refused (15 stems with "according to" or "based on", 3 sign-only Chemistry option sets, 1 "mainly") were minimally reworded under the same ids and re-judged with 5 fresh blind solvers (all 5 of 5) and five fresh judges; all 19 pass. Final set: 475 questions (Chemistry 95, English 58, History 81, Political Science 81, Psychology 79, Sociology 81) in docs/brain/reports/authored/wave1-candidates-final-2026-10-14.json; the original 479 stay in wave1-candidates-2026-10-14.json. The engine admits all 475 offline. One English set (english__p1__set3) is left with 3 questions and is not served in NTA mode; Political Science "Globalisation" has no authored question left.
