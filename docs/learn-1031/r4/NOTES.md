# Round 4 notes (append only)

Cross-packet requests: write the packet, the file, the change and why. The orchestrator merges them.

## From R4-server (web/1101-r4-server), 1 Nov 2026

The contract fields are live in `src/lib/server/learn.js` and `data/learn/*.js`; route tests in `data/tests/learn_r3_home.test.mjs`, `learn_routes.test.mjs`, `learn_preview.test.mjs` pin them.

1. **R4-run, R4-explore, R4-home: where `place: { n, of }` is (ruling N).** Render it only through `chapterPlace(place)` / `chapterShort(place)`; `ref` is still there, for source lines only. `place` is null for a chapter that is not playable for the student (no cards, outside their part, retired): draw no label then.
   - Run and feed start, resume and GET /runs/:id: `body.chapter.place`.
   - Ends (run and feed): `body.chapter.place`; the feed end's `feed.next.place`; an end option of kind `next` carries `place`.
   - Chapter page (POST /runs/preview): `chapter.place`; `added.place` and `shrink.addNext.place`.
   - Explore covers: `covers[i].place`.
   - Learn home: every roadmap row (`parts[].units[].chapters[i].place`) and `roadmap.chapter.place` (the offer's chapter).
   - GET /api/learn/cards: `chapter.place` (one chapter) and `chapters[i].place` (the subject shelf).
2. **R4-home: `needsWorkFrom` (ruling V)** is on every roadmap row, always `'papers'` or `'learn'` ('learn' when the chapter has any Learn activity: a card state, a card moved past in a feed, an unfinished run). Draw "Needs work · from your papers" only when `verdict` is set and `needsWorkFrom === 'papers'`.
3. **R4-home: copy and rows that changed on the server (no client change needed beyond tests that pin the old words):**
   - The feed Or row's `line` is now "Scroll through the chapter, stop any time" (`FEED_ROW_LINE` in data/learn/roadmap.js). Any home test pinning "One card or question at a time" for the Or row needs the new line.
   - In `today` mode, when the offer's `sub` leads with due cards, there is no `revise` Or row (owner-eye#9). The Revise row's count always equals its `run.cardIds.length`.
   - The fix row's `run` (and the suggestions' fix `action.run`) now carries `fresh: true`. Pass `run` through whole when starting it (R4-run's `links.run` `fresh` option).
4. **R4-run: a Free stopped end can now come back with `stopped: false`.** When another run holds today's Free session, a stopped mix or feed that serves questions gets no Continue (the server would refuse its first question): the end answers `stopped: false` with the Free-done keys. A stopped level check is now ended (`stopped: false`, no Continue). A stopped Free mix or feed has no fix key on its end (server-security#1). Body `stopped` and the keys come from one expression.
5. **Orchestrator (keycards.js, no R4 packet owns it): `playable()` in `src/lib/server/keycards.js` keeps cards of retired chapters** (a retired `chapterByKey` result has no section, so `sectionAllowed` passes). Learn's due count now drops retired chapters (server-security#2), so `kc.dueCount` can be higher than Learn's `due.all` for a student who still holds states in a retired chapter. Request: in `playable()`, drop a card whose `syllabus.chapterByKey(card.chapterKey)?.retired` is true, so the Revise dot, R15 and Learn agree. The equality test (`due.all === kc.dueCount`) uses a fixture without retired states until then.

## R4-run requests (1 Nov 2026)

1. **R4-server, `src/lib/server/learn.js` runEnd (`chapterProgress`), for first-timer#4.** On Free, add `open` to the end payload's `progress` (the cards Free opens in this chapter, `info.counts.open`): `{ of, seen, before, open }`. Leave it out on Pro. Why: the run and feed ends now label the bar "5 of 45 cards seen · the rest open with Pro" once `seen >= open` and `open < of` (`progressLabel` in `src/components/learn2/stage/endModel.mjs`, pinned in `run/runView.test.mjs`). Without `open` the bar keeps reading "5 of 45 cards seen" (no regression, but the finding stays open).
2. **R4-server, ruling N, the run and feed payloads.** The run's session panel and the feed's desktop panel read `run.chapter.place` (`{ n, of }`) from the start payload and from `GET /api/learn/runs/:id` (`runBody`'s `chapter`). With no `place` they draw no chapter label at all (the old "Part 1, Ch 1" / "Ch 2, Part 1" lines are gone). So `place` is needed on `runBody`'s chapter object, for the start, the resume and the reload.

## R4-home (1 Nov 2026)
- To R4-server: `data/learn/roadmap.js` `coverageLine(row, { isPro })` still says "free card" when `isPro` is false. The home page no longer passes `isPro` (rows read the chapter's real `row.cards`, see `roadmapRow` in homeModel.mjs), so nothing on Learn home draws it now; if no other page uses that branch, it can go. Not blocking.
- To R4-server (confirming the contract R4-home renders): a roadmap row sends `needsWorkFrom: 'papers' | 'learn'` next to `verdict`; the row reads "Needs work · from your papers" only for `'papers'`. A missing field reads plainly "Needs work".
- To R4-server: the roadmap row must keep `cards` (the chapter's real card total) and `progress.of` (the open count; 5 on Free). The header's "5 Key cards free in each chapter" reads the largest `progress.of`; each row's total reads `cards`.

## R4-today (web/1101-r4-today), 1 Nov 2026
- **Test outside my files, edited minimally (merge note):** `data/tests/practice_parity_1020.test.mjs` line 57 pinned `<TodayCollegesStrip ... />` inside Today's `<header>`. With one strip built once (`const strip`, client-code#2) the header now holds `{strip}`; the test checks the one element in the page and `{strip}` in the header. Today owns `src/app/(app)/today/page.jsx`, so no other packet is affected.
- **For R4-home / the shell (not blocking):** on a brand-new student's 390x844 first screen the start card's swap row ("Or start with one of these", "A full mock", "Start with...") peeks half under the floating dock. TodayCue now stays away from it (it is in KEEP_CLEAR), so nothing is drawn over it, but first-timer#3's second half ("keep the alternatives row clear of the dock") is a clip by the dock, not by Today. If the shell's bottom padding or the dock height is touched in R4-home, check that row at 390x844. Today did not change its card height for it (refine, not rebuild).

## R4-explore requests (1 Nov 2026)

1. **R4-server, `place` (ruling N).** R4-explore renders `chapterPlace(place)` on the chapter page and `chapterShort(place)` on Explore covers, and nothing when `place` is missing. It reads `place` from: each cover in `/api/learn/covers`, `chapter` in `/api/learn/runs/preview` (and in `GET /api/learn/runs/:id` if the page reads it), and `shrink.addNext` (the "Add the next chapter" pile names it "Chapter 6").
2. **R4-server, cover line (owner-eye#10).** A cover's hook is today the first card the feed serves, and for Accountancy chapter 1 that is a fill-in-the-blank. The client now skips a cloze (two or more underscores, "[...]") or a front over 105 characters. It reads an optional `hooks` array (on the cover, in feed order, the first 5 card fronts as `{ front, kind, mustKnow }`) and takes the first readable one. Please send `hooks` (or make `hookOf` skip cloze fronts) in `data/learn/feed.js` / `learn.js` ~line 1392. Without it, a cloze-only cover shows "10 Key cards / and 6 questions" instead of the card.
3. **R4-server, tests you own.** `data/tests/learn_integration.test.mjs` (R9) matches the QuestionCard signature with `/actions = null, chapterTitle = null(, closed = false)? \}\)/`. R4-explore added the prop `hideChapter` BEFORE `actions` so that match still holds. Keep the regex as it is.
4. **Orchestrator, package.json.** `test:learn` does not list `src/components/feed/exploreModel.test.mjs` (it runs by hand today) or the new `src/components/feed/exploreR4.test.mjs`. Please add both to `test:learn` (12 + 14 tests; both green).
5. **Orchestrator, `src/app/preview/arena/ArenaPreviewClient.jsx` (not owned by any packet).** Its `SAMPLE` (the Rival view) still tags the goodwill stem "Partnership Fundamentals" (line ~81). Change it to `'Admission of Partner'` for the same reason as the Explore fixture. It is not on an Explore or Practice screen, so R4-explore left it.
6. **R4-today.** Practice's "Your papers" line now calls `chapterTitle(subject, chapter)` from `src/lib/today/chapterTitle.mjs` (via `weakestLine` in `repairsLine.mjs`). Keep that signature; your "Ratios" to "Accounting Ratios" fix then reaches Practice too.
7. **Orchestrator, a real-site check for Practice's chapter count.** In the preview the "14" comes from the syllabus (`unitsFor('accountancy', { option: defaultOption })`, the same 14 Learn plays). The live `/api/chapters` lists the chapters in the `chapters` table through `liveChapterRows`, so Accountancy shows 15 there if a Computerised Accounting System row exists. Learn hides that chapter because it has no cards (C2). If the table holds it, Practice says 15 and Learn 14 on the real site; say so if that should be reconciled (it is the route's file, not R4-explore's).
