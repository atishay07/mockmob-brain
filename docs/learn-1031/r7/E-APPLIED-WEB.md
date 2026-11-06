# E applied on the web (branch web/1104-english)

4 Nov 2026. The WEB side of `E-ENGLISH.md` (101 rows) is applied on `web/1104-english`. The App side is not touched (no `flutter_app/` in
this worktree). This file is the list the app pass needs: every shared word that changed, every row applied, skipped or adjusted, and
what was changed beyond the table's named lines.

## 1. Shared words (`data/learn/words.js`) and what the app and the parity cases must mirror

`tool/learn2_parity/words.mjs` and `flutter_app/` do not exist in this worktree, so the parity cases were not edited. Change these on
the app side (`LearnWords`, `learn_words_parity_test.dart`, the cases in `tool/learn2_parity/words.mjs`) in the same commit:

| WORDS key / export | Old | New |
|---|---|---|
| `WORDS.coachRatings` | Missed it brings a card back soonest. Easy sends it furthest away. | How well did you know it? Missed it brings the card back soon. Got it, in a few days. Easy, much later. |
| `reviseQuestions(n)` (a function; Today uses it too) | Revise · 5 questions | Revise 5 questions |
| `missedWords(scheduled, inRun)` (a function; not named in the table, row 7's rule) | in this run, then tomorrow | in this session, then tomorrow |

No other `WORDS` key changed. Other shared lines that moved on the web (the app has twins, row numbers in brackets):

- `data/learn/allowance.js` `FREE_CAPPED` (13): On Free, a session is up to 10 minutes. With Pro, pick any length.
- `data/learn/stamps.js` `IN_RUN` (7, extension): Back later in this session. The server stamp is now "Back in this session, then tomorrow".
- `endModel.mjs` `FREE_REST_PRO` (15): "The rest open with Pro." and the label reads "5 of 45 cards seen. The rest open with Pro."
- `data/learn/feed.js` `CHECKPOINT_LINE` (23) and `keptLine` (24).
- `compose.js` `NOTE`, `NOTE_FIRST` (6), `RATINGS_USED` (48), `shrinkText` (51 to 53).
- `kinds.js` `RATINGS` label (3), `PRO_LINE` (43), `limitCopy` (46, 49, 50), `addedLine` (74).

## 2. Rows applied as written (web part)

1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15, 16, 17, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35, 36, 37, 41, 42, 43, 44,
46, 47, 48, 49, 50, 51, 52, 53, 54, 56, 58, 60, 61, 63, 65, 66, 71, 72, 73, 74, 80, 81, 82, 83, 84, 85, 86, 87, 88, 90, 91, 92, 93, 94,
95, 96, 97, 98, 99, 100, 101 (see the scope of 101 below).

Where a row names a Web line number, the line had moved; the "Before" text was searched for instead. Row 33 was applied to both
endings (`DiscoveryFeed.jsx`, the list view and the paged view) as one text. Row 42 keeps "Swipe to move on" where it shows.

## 3. Rows that needed a check first

- **Row 46 (confirmed).** Learn's `ratingsLeft` is `KEYCARD_RULES.free.reviewsPerDay - allowanceUsed('keycard_review')`
  (`src/lib/server/learn.js:247`), the same 10 a day and the same allowance as Key cards' `keycard_reviews` (`data/keycards.js`,
  `src/lib/server/keycards.js:250`). So "card ratings" is true on both. The two Key cards limit titles are now one title:
  "Today's free card ratings are used".
- **Row 69 (confirmed, wording from the row's alternative).** "Lowest" is the lowest share right among the chapters the level
  check's questions came from (`levelPick`, `data/learn/stamps.js`), so it is the weakest part, not a lowest single score. The end's
  sub line is now "Your weakest part: 3 of 6 right" and the server's own `evidence` line matches.
- **Row 89 (skipped).** The row asks for the owner's OK first. The labels come from the server (`data/chapter_state.js`
  `STATE_LABELS`), are pinned by KEYCARDS-BUILD-SPEC and its tests, and the run end parses "moved from X to Holding" out of the
  server's sentence. "Holding" and "Holding, fading" are unchanged.

## 4. Rows adjusted (the text differs from the "After")

- **11** (`roadmap.js`): "N left", not "N cards and questions to go". The run's item count includes a lesson item, so "cards and
  questions" is not always true; the row allowed "3 left" for that case.
- **18**: `marksText` is now "35 marks" (the row's second option), the spoken line "35 marks left in this chapter", and the sort is
  "Most marks left". No "+35". The figure is not drawn on a row today (only the model and its tests use it).
- **38** (`QuestionCard.jsx`): "No difficulty", not "No chapter". The "Unlabelled" pill is the difficulty tag; the chapter span
  already falls back to "Practice question". "No chapter" would have been false.
- **55** (`ChapterPage.jsx`): "We couldn't update the plan. You're seeing the last one." The row says "the length", but this line
  also shows when a pile switch or Add next chapter fails to refresh, so "length" would sometimes be wrong.
- **59** (no change): the web already reads "Fills your 10 min" (and "Chapter 6, fills your 10 min"), which says more than the row's
  "Fills your time". The app's bare "Fills" still needs it.
- **79** (no change): the web's key already says "Study again" (and "Study again from the start" after a round).
- **62** (no change, as the row says): "Print chapter sheet" stays.
- **Row 101** uses the straight apostrophe in `data/learn/`, `learn2` and `keycards` strings (double-quoted) and the typographic one
  in `feed/` and `kinds.js`, to match each file's existing style.

## 5. Rows not applied because they are App-only

14, 30, 39, 40, 57, 68, 70, 75, 76, 77, 78. Rows 45, 64 and 67 are App-only in the table, but the same line exists on the web feed
or run, so the web twin was applied (section 6).

## 6. Beyond the named lines (same rule, same word; the app needs the twin)

- Row 7's "run" to "session": `RunPlayer.jsx` "Nothing to line up here yet" is now "Nothing here yet", "for this run" is "for this
  session", the round line "5 more are lined up" is "5 more to go." (row 67's web twin), `ChapterPage.jsx` aria labels
  ("added to this session", "Getting this chapter ready"), `stamps.js` `IN_RUN`, `learn.js` stamp, `words.js` `missedWords`,
  `compose.js` "Nothing is lined up in this chapter yet." is "Nothing is ready in this chapter yet."
- Row 19's third copy: `RunParts.jsx` verdict "Not quite. It's B." is "Not quite. The answer is B."
- Row 43's sentence appeared as a literal in six more places, now the same words: `proNudge.mjs` (the keycards line and the
  Upgrade sheet lede, which also says "10 card ratings" now), `LineYouNeeded.jsx`, `learn.js` (the locked line and "Free opened N
  of this chapter's M cards").
- Row 26: the Up next feed key `homeModel.mjs` "Play · 10 min" is "Start · 10 min" (test `r7Webfull` updated). The Or row's label
  "Play this chapter as a feed" is unchanged (see section 7).
- Row 45's twin: `ChapterFeed.jsx` "This card is on Pro." and "Saving more questions is on Pro." now say "part of Pro".
- Row 64's twin: `ChapterFeed.jsx` end error line is "The summary didn't load, but everything you did is saved."
- Row 4: `ChapterDeck.jsx` hint "Space shows the answer" is "Space turns the card over". `KeyCard.jsx` takes `WORDS.turnOver`.
- Row 73: `FindView.jsx` "Add a word to narrow it." is "Type another word to narrow it."
- Row 100: the busy label "Submitting…" is "Sending…".
- Row 94 also changes the Today page, which uses `reviseQuestions` ("Revise 5 questions"). Three Today tests pinned the old line and
  were updated (`today_r3`, `today_1018`, `today_release10`).
- `ChapterMap.jsx` `verdictWord` cut at " · "; it now cuts at the first comma (row 16 changed the separator).
- `chapterModel.mjs` recognises the server's new `RATINGS_USED` text (row 48) when it picks its own line (row 47).
- `IconShowcase.jsx` sample row says "Chapter sheet" (row 61).

**Scope of row 101.** Applied in `data/learn/`, `src/components/learn2`, `keycards`, `feed`, `revise`, `proNudge.mjs` (the saves
line) and `learn.js`. About 40 lines. Not applied to Mob, payments, Today, profile, billing, AI, the result and review pages or any
server log or developer message (more than 400 more "did not / could not" lines); that is a separate pass if wanted.

## 7. Found, not in the table, not changed

- `chapterModel.mjs` `runSummary`: "21 steps · about 10 min" (the word "steps" and a middle dot in a line; rules 2 and 3).
- `homeModel.mjs` `subjectLine` ("14 chapters · 866 Key cards · 4 lessons") and `roadmap.js` `coverageLine` ("31 of 46 cards seen ·
  4 of 10 questions tried") use the dot as a list separator (rule 2).
- `roadmap.js` Or row label "Play this chapter as a feed" (row 26's reasoning applies).
- `compose.js` overdue note "Revise first: 46 due" (the client adds "cards").
- `learn.js` `LOOKS_TEXT`: "Today's 10 free card ratings are used." and "Today's 5 new free cards are used." (older form than rows 48 and 49).
- `kinds.js` and `chapter_state.js` unknown-state label "Could not load".
- `UploadForm.jsx` joins rule-violation messages with " · ".
- `proNudge.mjs` title "Every Key card, on a schedule", "kept on a schedule in Revise" and the Cards page description.
- `compose.js` `startLabel` ("Start 10 minutes") is the server's label; the client already turns it into "Start · 10 min".

## 8. Checks

- `npm run test:learn`: 426 of 426 pass. `npm run test:keycards-ui`: 40 of 40. `npm run test:keycards`: 124 of 124.
- `npx eslint src data/learn`: clean.
- All of `data/tests/*.test.mjs` and every `src/**/*.test.*` (4,401 tests): 26 failures remain, all in files this branch does not
  touch (`authored_w2`, `brand_icons_1103`, `inventory_fingerprint`, `mob_v3*`, `next_move_parity`, `nta_engine`,
  `round5_completion`, `study_content`). The same files fail the same way on an export of the branch's starting commit (30 failures
  there), so they are not from this change. `brand_icons_1103` looks for `OR_ICON` in `RoadmapHero.jsx`, which the Up next module
  replaced.
- Tests whose expected strings were changed on purpose: `learn_words`, `learn_compose`, `learn_feed`, `learn_preview`,
  `learn_roadmap`, `learn_routes`, `learn_suggest`, `learn_r3_home`, `keycards_ui`, `keycards_option_choice`, `community_1018`,
  `pro_nudge_1018`, `today_r3`, `today_1018`, `today_release10`, `chapterModel`, `coverModel`, `homeModel`, `r7Webfull`, `runView`.
  `learn_compose` also gained two asserts for the row 51 sentence (`shrinkText('cap', ...)`).
