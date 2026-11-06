# Brief: A3 app result and Review (model opus), launched 2026-10-18T20:31:29.726Z

You are owner A3 of the MockMob app (Flutter) for the 19 Oct fix: THE MOMENT AFTER SUBMIT, THE RESULT, AND REVIEW AS "YOUR PAPERS". First read C:\Users\atish\Desktop\mockmob copy\mockmob-next\docs\brain\BRIEF-1019-COMMON.md completely (bases, tools, emulator lock, what to return); it is part of this brief. Branch ui/1019-a3-result, folder wt-1019-a3 (from ab04b067).

THE RULES (verbatim from PLAN-1019 section 0; obey every one):
- **R1. Fresh-account first.** Every app and web check starts on a brand-new account (onboarding to Today to Practice to a paper to the result to Review to the Mob), then on the seeded heavy account. Both at 360 dp, plus 390 and 1440 for web, Night and Day.
- **R2. The 17-year-old test (G23).** For every screen, write one line: "What does a first-time student think this screen wants from them?" If the answer is not obvious in 3 seconds, it is a finding.
- **R3. Never hide to fix.** Removing or hiding any visible feature needs his explicit say-so. With billing off, Pro-only features are visible but locked (D101).
- **R4. Regression diff.** Before any release, screenshot the same screens on the previous release and the candidate, side by side. Any lost gradient, texture, motion or feature is a HIGH unless he asked for it.
- **R5. Motion is part of done.** Every result, accept and reveal animation is checked as a frame sequence on device (the emulator is fine), compared with the approved version's durations and curves.
- **R6. Copy in his voice (D84).** Persuasive, plain, grammatical English. No clipped fragments, no dropped articles, no telegram style. Read every new line aloud. If it would not appear in a good consumer app, rewrite it.
- **R7. One owner per surface.** Fewer, larger branches. Each has a single owner who knows the whole surface. The main session merges early, not at the end.
- **R8. Mock-up first** for anything that changes a layout (D107, D110, and his standing rule): 2-3 options as images, he picks, then the build.

YOUR ITEMS (SPEC and DONE WHEN verbatim from PLAN-1019 section 1):

**G22 + D108: the moment after Submit.**
- SPEC:
  - Restore the approved reveal animation exactly, from the sha in FORENSICS.md.
  - Then: a completion line ("Paper saved. 7 of 10 right."), the marks counting up (tabular figures, 600-900 ms ease-out), one dominant next move, and "See this paper" (G20).
  - The result screen on mobile must be big, clear and one thing at a time; no clutter above the fold.
  - Check on the emulator after a 10-question practice and after a full mock.
- DONE WHEN: the frame sequence matches the approved reveal, and he sees the moment on his phone.
(FORENSICS: v13 1178a9e7 (10-17 04:21) unmounted FinishStage from practice_result_screen.dart; FinishStage (lib/features/practice/widgets/finish_stage.dart: the sheet inks in bubble by bubble, the figure counts up and is stamped with a medium haptic, a ring and 14 shards for a good set, then Mobi reacts and the success haptic follows, gated by the Celebrations setting) and FinishCeremony still exist but nothing mounts them. RESTORE the mount as it was at 68f63c11 (the parent of 1178a9e7), keeping the v13 layers under it (onSettled stages what appears below). Full and NTA mocks keep the sealed sheet, the 4-card recap and the full-result reveal: verify them too. "Paper saved." must be true: show it only after the server confirms the save.)

**G20 + D106: Review becomes Practice > Your papers.**
- SPEC, top to bottom:
  1. A stats strip: papers sat, the latest marks with their trend, open repairs.
  2. A subject filter (chips, with a scroll cue).
  3. "Your papers": newest first. Each row shows the paper name, subject, marks out of the maximum, and date (12-hour time). A tap opens that paper's result and answers.
  4. "Mistakes to repair" by chapter (the current Review content, decluttered).
- After a paper, "See this paper" on the result screen deep-links to its row.
- DONE WHEN: a fresh account after 1 paper sees it at the top, and a heavy account filters by subject.
(Owner A1 moves the Review screen INTO the Practice tab as "Your papers" (navigation and routes only). You own the CONTENT of that screen: lib/features/review/** and the result screens lib/features/result/** and practice_result_screen.dart, finish_stage.dart. Keep the D18 "leads with weak chapters" value inside "Mistakes to repair". Numbers must agree everywhere (the 18 Oct walk found repair counts 139 / 19 / 2 and full mocks 5 / 13 / 8 disagreeing: make the strip, the rows and the chapter list read the same record). A fresh account with no papers sees a friendly first step ("Sit your first paper", one key), never an empty page.)

FILE OWNERSHIP: lib/features/review/**, lib/features/result/**, lib/features/practice/screens/practice_result_screen.dart, lib/features/practice/widgets/finish_stage.dart and finish_ceremony. Not the bar, Practice tiles or routes (A1), not Today (A2b), not onboarding (A2a), not the estimate (A5).

CHECKS before you return: flutter analyze clean; unit tests (Your papers order, filter, empty state, deep link from the result, numbers agree, "Paper saved" only after the save); goldens (open old and new; 360 and 412; Night and Day; 1.3x). Then, holding the emulator lock: a FRESH staging account sits a 10-question practice and you capture the moment after Submit as a FRAME SEQUENCE (adb screenrecord or rapid screencaps; open the frames) and compare its timings with FinishStage's approved durations at 68f63c11; then a full mock's sealed sheet and reveal on a heavy account; then Your papers on both accounts (filter by subject on the heavy one). R2 line per screen; R4 side-by-side with v15.2 (mockmob-next\tmp\app-walk-1018g shots or the v15.2 APK). Commit as you go. Return as the common brief says.
