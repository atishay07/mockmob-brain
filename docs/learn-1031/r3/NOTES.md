# Round 3 notes (append only)

Cross-packet requests: write the packet, the file, the change and why. The orchestrator merges them.

## From R3-run (1 Nov 2026)

1. **R3-home, `src/components/learn2/home/**` (homeModel `shortAction`, the suggestion cards):** `data/learn/suggest.js` now says every suggestion key in ruling W's words. Labels changed: pickup `Pick up, 4 minutes` -> `Continue · 4 min`; due `Revise these` -> `Revise 5 due cards · 1 min`; fix `Fix them, about 3 minutes` -> `Fix 3 open mistakes · 3 min`; recap `Start the recap` -> `Quick recap · 2 min`; start and next `Start 10 minutes` -> `Start · 10 min`; level title and headline `Find your level` -> `Skip what you already know` (WORDS.skipKnown), evidence `6 questions · about 6 min`, key `Start · 6 min`. `shortAction` (and its test, `homeModel.test.mjs` lines 91-93, 136) still expects the old forms: please make it pass the new labels through (or shorten them by the same W words). Why: ruling W, one word for each thing.
2. **R3-home, Learn home's Free-done block:** the feed refusal block is built in `src/components/learn2/stage/FreeUsed.jsx` (headline `FREE_DONE_HEADLINE`, line `FREE_DONE_LINE`, main key `See Pro`, then a quiet "Or" label and at most 2 rows with a hairline and a right chevron, in ruling F's order). The row rule is the pure `freeUsedRows(data)` in `src/components/learn2/stage/endModel.mjs` (tested in `run/runView.test.mjs`). Please match its words (and, if you like, its look), or import `freeUsedRows` for the order. Note `FREE_SESSION_DONE` is now `${FREE_DONE_HEADLINE} ${FREE_DONE_LINE}`, so any place that shows `free.text` from `/api/learn/subject` or `/api/learn/covers` now shows those two sentences together.
3. **R3-explore, `src/components/learn2/feed/coverModel.js` and `ExploreCovers.jsx` (the covers are yours by the packet table, though they sit in `feed/`):** I left them alone. They still say `N old mistakes to fix` and the key `Pick up, 4 minutes` (`keyLabelOf`, `studentLineOf`, tests in `coverModel.test.mjs`). X4 and W want `N open mistakes to fix` and `Continue · 4 min`. Also `src/components/learn2/chapter/chapterModel.test.mjs:24` feeds the old `FREE_CARDS_ONLY` text as an input string (the test still passes; the real line is now "That was today's free session, so this one is Key cards only. Questions come back tomorrow.").
4. **Whoever owns `src/components/learn2/links.js` (unowned in the table):** `links.run()` has no `fresh` parameter, so the feed end's fix key appends `&fresh=1` to the href itself (the run player reads `?fresh=1`). A `fresh` argument in `links.run`/`runHref` would be cleaner.
5. **Orchestrator, server copy outside my functions in `src/lib/server/learn.js`:** `/api/learn/subject` and `/api/learn/covers` return `free: { text: FREE_SESSION_DONE }` (now the shared headline and line). The home packet owns how it is drawn.

## R3-home (Sonnet), 1 Nov 2026
- **R3-run (owns `data/learn/allowance.js`):** `data/learn/roadmap.js` now imports `FREE_DONE_HEADLINE` and `FREE_DONE_LINE` from `allowance.js` and the labels from `words.js` (`WORDS`, `withMinutes`, `reviseDue`, `fixMistakes`, `wholeMinutes`). Keep those exports and their names. Learn home's Free-done block is `FREE_DONE_HEADLINE`, `FREE_DONE_LINE`, main key "See Pro", then Or rows in ruling F's order (Continue, Revise N due cards, Answer single questions). The feed refusal screen must show the same block word for word; its Or rows read the `options` the 402 sends (`sessionUsed` in `learn.js`, yours): please give them the same labels (`withMinutes(WORDS.continue, n)`, `reviseDue(n, m)`, `WORDS.singles`) and drop "Quick recap of this chapter" and "Questions on this chapter in Explore" from the refusal block if ruling F's three rows are the whole block.
- **R3-run (`start()` resume branch):** Learn home's "Continue" row for a stopped feed sends `{ chapterKey, minutes, kind: 'feed', leaveOut: [], resume: <run id> }`; `start()` resumes by `resume` before any kind rule, so keep that first branch as it is (a test in `data/tests/learn_r3_home.test.mjs` pins it).
- **Orchestrator (merge):** `package.json` `test:learn` gets two new files from this packet: `data/tests/learn_r3_home.test.mjs` (after `learn_words`) and `src/components/learn2/home/__tests__/r3Home.test.mjs` (after `nav.test.mjs`). If another packet edits the same line, keep every file name.
- **R3-explore:** `src/components/learn2/cards/FindView.jsx` has no owner in the table; I changed two strings in its due fallback only ("9 due" became "9 due cards", ruling W). `ShelfKeys.jsx` is deleted (the status line under the search is gone, R4); `shelfKeys()` in `homeModel.mjs` stays for Find's rows. `SubjectShelf` no longer takes `dues`.
- **R3-today / R3-explore:** the sidebar and the dock no longer show a due number. `src/lib/nav/dueCount.mjs` now exports `LEARN_DOT_LABEL`, `REVISE_DOT_LABEL` and `dotName`; `dueBadge`, `dueTabBadge`, `dueWords` and `dueLabel` are gone. Any page that imported them must use the dot labels or draw nothing.

## R3-today (1 Nov 2026, evening)
- To R3-explore (preview arena fixtures, `src/app/preview/arena/previewFirstWeek.js` line 28): the insight chapters use names that are not stored syllabus names ('Goodwill', 'Ratios'). Real data stores 'Goodwill Valuation'. Today now names a chapter by `chapterTitle(subject, name)` (`src/lib/today/chapterTitle.mjs`, canonical title from `data/cuet_syllabus.js`, plus a unique first-words fallback so 'Goodwill' reads "Goodwill: Nature and Valuation" in the fixture). Please switch the fixture to stored names so the preview shows what production shows.
- To R3-home (shell, ruling Z and S2): Today shows no due number and no dot of its own. The sidebar "Learn 27 due" and "Your papers 8 due" badges and the dock "8 due" are yours, as are the aria-labels on every dot including the Papers tab dot.
- To the orchestrator: `data/learn/words.js` was read-only for me. Today now imports `WORDS.continue` and `reviseQuestions` from it. No change needed.

## R3-explore (web/1101-r3-explore), 1 Nov 2026

**Requests to the orchestrator (one line each, please keep on merge):**
- `src/lib/server/learn.js` (preview function, not in any packet's list): one added line in the dry run's response, `cardsSeen: info.coverage.seen` after `firstVisit`. The chapter page's Quick recap (X6) shows only when `cardsSeen > 0` (an older server without the field falls back to "not a first visit").
- R3-run (`src/components/learn2/feed/**`): Explore's own files in that folder are R3-explore's by the packet table ("its covers"): `ExploreCovers.jsx`, `coverModel.js`, `coverModel.test.mjs`, `covers.css`. R3-run keeps `ChapterFeed.jsx`, `feedModel.mjs` and the rest. If R3-run touched `ExploreCovers.jsx` or `coverModel.js`, the merge needs a look.
- `data/learn/feed.js` and `src/lib/server/learn.js` (~L1417) still build the feed lines "N old mistakes to fix" ("old"). Explore's covers rewrite "old" to "open" on the client (`coverModel.js` `openWords`), so the page is right now; the server text should say "open mistakes" too (ruling W) so the covers' lead line and the feed's own lines agree at the source.
- `data/practice_quote.js` L117 still sends "Included with your Pro access (valid until ...)" as `reason`; Practice no longer draws it for Pro (X5), but the mobile app and any other reader of the quote still gets it.
- `src/app/preview/arena/ArenaPreviewClient.jsx` (shared with R3-today, who adds a `/api/today` fixture): R3-explore changed only the `/api/bookmarks` GET line (a brand-new student, `student=new`, has 0 saved; the others see 2 that are in the syllabus) and added a comment line above it.
- `data/tests/web_fixa_1019.test.mjs`: the Practice-heading assertion now pins "What are we practising?" with no greeting name (X5, "the hero is one line"). Name dropped on purpose; if the owner wants the name back it needs a design for a one-line heading at 390.

**Left or decided (see the packet return for the full list):**
- X5 "P3's Practice change survived": the commit named in the spec (739687993) is only P3's notes commit; the change is 40323de94 (and a8c43474e). `git diff 40323de94 HEAD` on the dashboard, Explore, Saved and chapter files is empty before this packet (only ChapterFeed/feedModel/ChapterPage 3 lines/chapter.css moved), so no Practice code was lost in the merge. What still showed "Included" came from three places P3 had not removed: the server quote's reason line, the bar's price, and the "Your access" panel.

**X7, the hydration error with `&l2=off` (needs R3-home's file):** reproduced on `/preview/arena?view=explore&l2=off`: one hydration error, and it is in the app shell, not in Explore. `src/app/(app)/AppLayoutClient.jsx` ~L97 reads the address inside `useState(() => ... typeof window === 'undefined' ? false : ...)`, so the server draws the Learn nav row (`data-tour="nav-learn"`, `/preview/study`) and the client's first render draws Your papers (`nav-review`). R3-explore changed `src/components/learn2/flag.js` (new `useL2Off()`, a `useSyncExternalStore` whose server snapshot is "not off"; `useLearn2On()` uses it, no `useSearchParams`) and made `DiscoveryFeed.jsx` and `ExploreCovers.jsx` read the flag through it. flag.js is in no packet's list, so R3-home please keep that file as it is here. The shell needs this change (applied here, run on :3483 and the console was clean, then reverted because the file is R3-home's; `navAlt` just below it has the same shape and should get the same treatment):
```diff
-import { LEARN2_ENV_ON } from '@/components/learn2/flag';
+import { LEARN2_ENV_ON, useL2Off } from '@/components/learn2/flag';
@@
-  const [l2Off] = useState(() => {
-    if (!previewRoute || typeof window === 'undefined') return false;
-    try { return new URLSearchParams(window.location.search).get('l2') === 'off'; } catch { return false; }
-  });
+  const l2OffAddress = useL2Off();
+  const l2Off = Boolean(previewRoute) && l2OffAddress;
```
Until that lands, the l2=off page still logs that one shell hydration error. Console texts: tmp/learn-1101/r3-after/explore/explore-l2off-1440-console-before-shell-fix.txt (the error) and explore-l2off-390-console-with-shell-fix.txt (clean: only HMR and a not-found.css preload warning).

## R3-hero (1 Nov 2026)
- No request for another packet's files.
- H4 left as is: the Day room's answer-sheet marks are painted into the image (scene-empty-allclear-day); there is no HTML or SVG overlay on Day to thin out. Making Day as sparse as Night needs a repainted Day image (an image-generation job), not code. Say if you want it.
