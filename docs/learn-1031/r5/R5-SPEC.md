# Round 5 build spec (2 Nov 2026, about 10:15 am IST): owner items LK36-LK49

Owner's words: `mockmob-next/docs/brain/OWNER-FEEDBACK-2026-10-31-LEARN.md`, section "2 Nov 2026, about 10 am" (read it first, all of it).
Base: origin/main a16fbd62e (Learn v2 rounds 2-4 and Key cards live). Earlier specs: `r2/R2-SPEC.md`, `r3/R3-SPEC.md`, `r4/R4-SPEC.md`;
shared words `data/learn/words.js`, `data/learn/allowance.js`. The owner's UI standards: `C:\Users\atish\Desktop\AI OS\wiki\concepts\ui-ux-standards.md`
(run its done check). DESIGN.md and PRODUCT.md at the repo root win over generic taste.

Every packet: its own worktree and branch (below); commit there; **never push, merge, deploy, or write to production**; no production
sign-in. Dev servers only through `preview_start` with the named launch config; before starting one, write your name into a free
`C:\Users\atish\Desktop\mockmob copy\tmp-devslots\slot-1` or `slot-2` (a file; none free means wait and retry every few minutes) and delete it
when you stop the server. Signed-in pages are seen through the dev preview (`/preview/arena`, see R4-SPEC "look"; the Learn engine
answers at `/preview/arena/realdeck?_to=/api/learn/...&_plan=pro|free&_student=commerce|new&_s=<session>`). Look at every changed screen
at 390 and 1440 px, Night and Day, before you report. Kill only your own processes. RAM: keep Next dev + browser under ~4 GB.

## Packet A: options in a stable shuffled order (LK44) — wt-1102-shuffle, branch web/1102-shuffle

Fact (production, verified rows, read 2 Nov): keys skew to A. Accountancy A 1,206 / B 96 / C 62 / D 41; most older subjects alike;
the Claude-authored waves are balanced. NTA papers already shuffle (`src/lib/server/ntaPaper.js`, `data/nta_engine.js` shuffleKey).
Quick papers ("quick papers never shuffle options", `src/lib/server/mob/deps.js`), Learn v2 (`servedOptions`/`keyLetter` in
`src/lib/server/learn.js`), the Explore question stream and possibly saved/mistake surfaces serve the stored order.

1. Audit every place a student is shown options and every place an answer is graded or stored; write the table (surface, shuffled now?,
   what is persisted: letter as served / stored index / text, who reads it later) into `docs/brain/learn-1031/r5/A-OPTIONS.md`.
2. One shared helper: a stable permutation per question id (seeded from the id, the same for every student and every surface, so a
   question looks the same in Learn, Explore and a quick paper), with the NTA engine's own eligibility rules for items that must keep
   their order (all/none of the above, "both A and B", statement combinations, sequences; reuse `isPermutationOptions`,
   `listedOrderKeyReasons` and friends rather than new rules). Served letters A-D are relabelled in served order; the key moves with
   its option.
3. Apply it to every unshuffled surface, with grading through the same mapping. Anything persisted must keep its meaning for old
   rows and for other surfaces (past attempts, result review, mistakes, mistake repair, saved questions, Mob frozen papers: a frozen
   paper must keep one order for all players). Prefer persisting option identity (stored index or text) over a served letter.
4. Prove it: a script that serves every verified question through each surface and prints the served-key distribution per subject
   (about 25% each), plus unit tests for stability (same id, same order, every call), grading round trips, the kept-order items,
   and old persisted rows. Run `npm run test:learn`, `npm run test:recovery`, the question and payment suites, and every suite your
   change touches. The app reads options and sends the letter it was served: confirm the app's Learn API path needs no change.
5. No database write and no migration. Report the table, the distribution before/after, the suites, and anything you could not cover.

## Packet B1: the study stage tells the truth (LK38, LK45 fixes 2 and 4, LK40) — wt-1102-stage, branch web/1102-stage-r5

1. **Missed it / Got it / Easy (LK38).** Today: FSRS ratings 1/3/4 (`schedule()` in `data/keycards.js`); every rated card is
   scheduled, but the end's "N in Revise" pile (`pileOf` in learn.js) counts only 3 and 4, so Missed it looks like nothing, and no
   screen says when a card returns. Do:
   - Server: each card item served to a student who may rate it carries `returns: { missed, got, easy }`: the words for when that
     rating would bring it back, from `schedule(state, r, now)` for r = 1, 3, 4 (one shared words function in `data/learn/words.js`:
     under 1.5 days "tomorrow", then "in N days" to 13, "in N weeks" to 8 weeks, then "in N months"). If a run re-shows a missed card
     later in the same run, the missed words say so truthfully (read compose.js: find out; never claim what does not happen).
   - The three keys keep their names and gain a second line: "Missed it / back tomorrow", "Got it / back in 3 days",
     "Easy / back in 2 weeks". After a rating, the card's stamp says where it went ("Back tomorrow", "Back in 3 days"). Once per
     student, one coach line under the keys: "Missed it brings a card back soonest. Easy sends it furthest away."
   - The pile counts every rated card (1, 3, 4): "In Revise" means scheduled. Keep Revise's own due counts as they are.
2. **Fix 2 (LK45): one count.** The stop sheet ("3 of 18 done", `itemsDone` in `feed/ChapterFeed.jsx` and the run player) and the end
   ("9 of 18 done", from the server) must say the same number for the same moment. Read how the server's end counts done, make the
   client's stop sheet use that same rule (both feed and run), and pin it with a test.
3. **Fix 4 (LK45): a Revise run says Revise.** A run whose cards come from more than one chapter (Revise due cards, a Find set's
   "Study these") gets the head line "Revise" (a set's own name when it has one), no "Chapter N of M" place, and its end says the same.
   Server `runBody` chapter block; words in words.js.
4. **Scroll (LK40).** On the web stage, a wheel or trackpad scroll over the question, its options or a card that cannot scroll further
   scrolls the page/stage as the student expects; nothing traps the wheel (check `overscroll-behavior`, inner scrollers, the pager's
   wheel handling). Desktop 1440 and phone 390. Test it for real in the browser with the mouse wheel.
5. Tests: `npm run test:learn` and the learn2 component tests; look at every changed screen (390, 1440, Night, Day).

## Packet C1: the top bar, the tab order, the scroll speed (LK42, LK46, LK47) — wt-1102-chrome, branch web/1102-chrome

1. **Top bar (LK42).** He: the Pro badge, the credits and the wallet symbol look low quality; rethink the top bar (web and app; this
   packet is the web). Read the current bar on phone and desktop, signed in Pro and Free. Redesign the account cluster into one calm,
   high-quality piece (what it says, what a tap opens, icon or none, Free vs Pro, credits number with its unit), by the owner's UI
   standards and his research brain rules. Build it for real behind nothing (it is a refinement, not a rebuild); the owner judges it
   live before it ships, so keep it in its own commits.
2. **Tab order (LK46).** The four equal tabs read Practice, Papers, Learn, Explore (phone tabs and desktop sidebar alike).
3. **Scroll speed (LK47).** "The scroll speed on the entire website feels like a lot ... in the first section of the website." Find
   what drives scrolling on the landing page's first section (a smooth-scroll library, wheel handlers, scroll-linked animation, CSS
   `scroll-behavior`) and make it feel like a normal page scroll; keep reduced motion right.
4. Tests for what you touch; look at 390 and 1440, Night and Day, signed in and out where it applies.

## Later (after the 1:20 pm usage reset): B2 cards and desktop scale (LK39, LK41, LK43, mock-up first), C2 run choices (LK37), the app port of all of it.
