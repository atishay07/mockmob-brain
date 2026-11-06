# 09. Final critic: the 1 Nov final captures, read as the owner would

1 Nov 2026. Read-only review. The only file written is this one. No browser was started (the captures already existed), no
server, no commit, no database.

**What I looked at.** The owner's verbatim file (LK1-LK23) and ledger rows LK1-LK23. BUILD-1101 Part B with B7.
`00-critic.md`. ui-ux-standards sections 10 and 11. `tmp/learn-1101/final/index.md`, `index.json` (measures, pages) and all
182 PNGs. I read the phone sizes (390 Night, 360 Night, 390 Day) side by side, the desktop sizes (1366x650, 1024, 1440 Day) as a
grid, and every 1440 Night still on its own. I extracted the text of `70-print-chapter-sheet.pdf`. I read components only
to find where each fix goes.

**What these captures cannot prove.** They are headless Chromium with synthetic input on the dev preview. They don't show a
real wheel or trackpad, a finger, the LAN phone, reduced motion, a screen reader or a CPU throttle, and they contain no motion.
The wheel, trackpad and key measures in `index.json` all pass at 1440x900 and 1366x650.

---

## 1. Per screen: does it answer his feedback now?

| Screen (files) | His items | Verdict |
|---|---|---|
| Explore covers (`01-explore-covers-*`, `02-*`) | LK21, LK12, LK18 | **Answered.** No subject object on any cover. Each cover shows the chapter's own opening card as its art (`01-explore-covers-1440-night`: "Persons who have entered into partnership...", "What is goodwill?"). The For you cover has the only volt key, desktop has arrows, and phones have a `1 of 14` pager (`01-explore-covers-390-night`). When the For you cover leaves the view, the dock's Start takes the volt (`02-explore-covers-second-390-night`), so one volt stays in view. **Two misses.** Admission's art is "If this amount is paid to the old partners..." (`02-explore-covers-paged-1440-night`): "this amount" points at nothing (M4). On Free, the For you cover contradicts itself (M3). |
| Explore, flag off (`04-explore-flag-off-*`) | B7 condition | Shows the old page ("One question. One useful step.", the calculator, Subject/Chapter/Difficulty). CLS is **0.137 at 390** (index pages). Check whether live has the same shift before calling it parity. |
| Feed card, front, turned, kept (`10-*`, `11-*`, `12-*`) | LK20, LK13, LK5 | **LK20 answered.** Desktop has the panel (title, `1 of 16`, `About 10 min left`, Kept pile, `Up next`), the stage and the rail (Keep, Chapter). The bar holds `Previous (Up)` and one volt key that says what it does (`Turn over`, then `Next`, with a Space keycap), plus the line "The mouse wheel and the arrow keys move between items too." (`10-feed-card-front-1440-night`). Measures: one notch moves one item, a trackpad burst moves one, three notches move three. **LK13 answered:** no Must-know mark on feed cards. Some empty space remains: at 1440x900 about 230 px between the card and the bar, and the left panel is empty below `Up next`. It no longer reads as "stuck". Keep: the card fills volt, the label reads `Kept` and the line reads `In Revise` (`12-feed-kept-*`). |
| Feed question, right, streak, wrong (`13-*`, `14-*`, `15-*`) | LK20, LK11 | Questions get `Skip` until answered. Right answers show `Right. 3 in a row.` in the verdict line and the panel (`14-feed-right-streak-1440-night`). The line you needed opens in place under the options, with nothing covering them (`15-feed-wrong-line-1440-night`). **Miss:** after a wrong answer at 1366x650, 390 and 360, the auto-scroll cuts the question mid-line under the top bar (M2). Match-the-column questions on a phone fill the first screen with no hint that options are below (M10). |
| Checkpoint and stop sheet (`16-*`, `17-*`) | LK9, LK11 | Two choices (`Stop here`, `Keep going`) plus honest numbers. The phone checkpoint has about 380 px of empty space above and below a single line (`16-feed-checkpoint-390-night`) (nice-to-have N1). The stop sheet's `Stop here` and `Leave, pick it up later today` can't be told apart (M9). |
| Feed end (`18-*`) | LK11 | **Answered.** Chapter title, `All 17 done in 1 min.` (the capture clicked fast; the number is true), the kept pile drawn from real card faces, three lines that add up (12 + 3 + 2 = 17), then `Another 10 minutes` (volt), `Next chapter: ...` and `Back to Explore`. The next action is dynamic and offers options. |
| Free feed and refused (`20-*`, `21-*`) | LK15 | A calm full stage, no modal. Four ways that still work, the lead in volt, then `See Pro` (`21-feed-free-refused-390-night`). Good. |
| Learn home, search (`30-*`, `31-*`, `32-*`) | LK1, LK3, LK9, LK10, LK11 | Subject row, search with three shelves, three suggestions (Pick up in volt, Revise, Fix), and chapters in book order. Search results have one `Show answers` toggle and one `Study these 50` key (LK7 trimmed). **Misses:** the sidebar says `27 due` while Learn says `9 due today` (M5). At 1366x650 and 1024 the first chapter row is below the first screen (M6; the capture's own note says the same). On phones the mistakes tile cuts its line to "with t..." (M7). |
| Chapter page (`40-*`, `41-*`, `42-*`) | LK22, LK10, LK6 | **Answered.** Title, `How long have you got?`, three piles whose minutes add up to the Start key (5 + 3 + 2 = 10; Free 2 + 6 + 2 = 10), `Tap a pile to leave it out.`, the volt Start, the quick recap as a text key, and `Everything in this chapter` on the right. Start sits above the dock at 360 and 390 (`40-chapter-10min-360-night`). The resume row reads `You stopped at 6 of 16 today` with `Pick up where you stopped` and a neutral `Start a new 10 minutes` (`42-chapter-resume-*`). Free's line shows only once 20 is picked (`41-*`). `Print sheet, 14 Must-know lines, with your name` is in the shelf (LK6). |
| Run (`50-*` to `55-*`, `82-*`, `83-*`) | LK22, LK5, LK13 | The panel shows piles (`Key cards 0 of 16`, `Questions 0 of 2`, `Your mistakes 0 of 2`, `In Revise 0`). The card front has no Must-know. The back keeps the prompt on top. The rating row reads `Missed`, `Got it` (volt), `Easy`, with one line on what Got it does. The wrong line opens in place with `You'll see this card again later in this run.`. **Misses:** on desktop the card is 467 px tall for a one-line prompt and its back is about half empty (M8). A Statement I/II/III question is one paragraph (M1). On a phone, the wrong answer scrolls the student's own pick out of view (M2). |
| Run end (`55-*`) | LK11 | **Answered.** Title, done line, `16 in Revise, 14 back Wed, 2 back in 20 days`, and three lines. The lead is `Next: Profit and Loss Appropriation Account` with `Start 10 minutes` (volt), then `Another 5 minutes here`, `Fix 2 open mistakes`, `Test it in a full mock` and `Back to the chapter`. |
| Key cards view (`60-*`, `61-*`) | LK4, LK7, LK13 | Sections rail on desktop. The filters `All 46`, `Must-know 12`, `In Revise 12` and `Missed lately 3` give a sane Must-know share (12 of 46). One `Show answers`, one `Study these N`. The content duplicate is still there: `Define partnership.` and `What is partnership?` are both Must-know (`60-cards-all-390-night`; 00-critic E4). |
| Print sheet (`70-*`, PDF) | LK6 | **Answered.** The diagonal `mockmob` watermark repeats across the page, the logo heads it, and the foot reads "Printed for Preview from mockmob.in on 1 Nov 2026.", with NCERT's words and the page for each line. The capture's PDF has text at x = 0 (no margin) because Playwright's `page.pdf` ignores CSS `@page` without `preferCSSPageSize`. `printSheet.css:6` sets 16/14/20 mm, so check one real Ctrl+P before calling it done. |
| Real content (`80-*` to `83-*`) | 00-critic §4.1 | Match-the-column renders as two lists (side by side from 768 px) and Assertion-Reason as two labelled parts. **Statements are not split** (M1). |

---

## 2. Must-fix (blockers and highs only)

None is a blocker. No dead end, no second volt key, no overlap that hides a key, and no console error or failed request in any job.
Ten highs, ordered by what a 16-year-old meets first.

**M1. Statement questions are a wall of text** (`82-real-statements-1440-night`, `82-real-statements-360-night`).
"Read the following statements ... Statement I: ... Statement II: ... Statement III: ..." prints as one 6-line bold paragraph
(11 lines at 360), in the feed and the run. This is LK11's "lines and lines of text", on CUET's most common stem after MCQ.
- Fix: add `statementList(stem)` to `src/components/learn2/stage/stageText.mjs`.
  - Split on `/Statement\s+(I{1,3}|IV|V|[1-5])\s*[:.–-]\s*/g`. When there are 2 or more, return `{ lead, items: [{ label, text }], tail }`.
  - The tail starts at "Choose" or "Which" when present.
- Draw it in `stage/Question.jsx` the same way as `matchLists`: a label column of 36 px, items in body weight (400, 16 px, line-height 1.45, 8 px gap), the lead keeping the stem style.
- Add a test over the fixture questions with "Statement".

**M2. A wrong answer scrolls away what the student picked and cuts the question mid-line** (`53-run-wrong-line-390-night`,
`53-run-wrong-line-360-night`, `15-feed-wrong-line-1366-night`, `15-feed-wrong-line-390-night`).
In the run on phones, the chosen row A (red) is off screen; at 360 even the right row is cut, so he sees "The answer is C" and
not what he chose. In the feed at 1366x650 (his laptop), "writing off?" sits half under the ticks.
- Fix: scroll to the **chosen row**, not to the line's title. Use `scrollIntoView({ block: 'start' })` with `scroll-margin-top: 12px` on the option row.
  - Files: `stage/Question.jsx:141-147` and `run/RunPlayer.jsx:335-342`.
- Give the inner scroller a top fade while `scrollTop > 0`: `mask-image: linear-gradient(to bottom, transparent 0, #000 24px)`.
  - Files: `stage/stage.css` and `run/run.css` `.lr-body`.
- Check at 360x780, 390x844 and 1366x650.

**M3. Free cover says "pick up where you stopped" but its key says "Questions on this chapter"** (`03-explore-free-day-used-390-night`,
`03-explore-free-day-used-1440-night`).
The feed itself offers `Pick up where you stopped, 1 of 12` as its lead (`21-feed-free-refused-390-night`), so the cover sends him
the wrong way.
- Fix in `src/components/learn2/feed/coverModel.js:78-81`: check `c.resume?.of` before `freeDone`. Return `Pick up, N minutes` and open the feed with `?run=`.
- Only covers without a resume read `Questions on this chapter`.
- Add a case to `coverModel.test.mjs`.

**M4. The first thing a Pro student reads in Admission makes no sense on its own** (`10-feed-card-front-390-night`,
`10-feed-card-front-1440-night`, `02-explore-covers-paged-1440-night`).
The cover art and the first card both read "If **this amount** is paid to the old partners directly (privately) by the new
partner, ___ is passed in the books of the firm." Nothing says which amount.
- Fix the hook and first-card rule in the feed composer (`src/lib/server/learn.js` hook and first item, `data/learn/feed.js`):
  - Skip fronts that open with an anaphor (`/^(if\s+)?(this|these|that|such|it|they|the above|the same)\b/i`).
  - Prefer a Definition or Term card at position 1. Free already opens on "What is the sacrificing ratio?" (`20-feed-free-first-*`).
- Add a test: the first card of every 10-minute feed passes that check, and `cover.hook.id` equals the feed's first card.
- Rewording the card itself is a content change, so put it to him and don't do it on our own.

**M5. Two "due" numbers for Learn that don't agree** (`30-home-top-1440-night`, `41-chapter-free-20-capped-1440-night`).
The sidebar reads `Learn, Key cards 27 due` (Free: `20 due`), and Learn opens on `9 due today`. The badge comes from v1's keycards
home (`src/app/(app)/AppLayoutClient.jsx:91-93`, `useKeycardsHome().today.due`, all subjects). The shelf is v2, Accountancy only
(`home/homeModel.mjs:205`).
- Fix: under Learn v2, take the badge from the v2 home and sum it across subjects.
- Show each subject's due count on the subject row (`Economics, 12 due`, ink-2, 13 px) so the numbers add up. File: `home/SubjectShelf.jsx`.

**M6. Learn home: no chapter row on the first screen at 1366x650 or 1024** (`30-home-top-1366-night` and `-1024-night` in the
desktop grid; the capture's note: "Learn home first chapter row is covered by off screen").
The subject row takes about 150 px for four objects. 00-critic's P0 H1 asked for the first chapter row at 1366x650.
- Fix (`home/SubjectShelf.jsx`, `home/learn-home.css`):
  - From 1024 px, make the subject row one line of four chips: the object at 40 px to the left of the name, and the chosen subject's meta inline.
  - The row is 72 px tall at most.
  - Bring the suggestion tiles' padding from 20 to 16 px.
- Target: the top of the "Part 1, Partnership Accounts" first row at y ≤ 600 at 1366x650.

**M7. Learn home phone: the mistakes tile cuts its own line** (`30-home-top-390-night`, `30-home-top-360-night`,
`31-home-search-focused-390-night`).
"3 open mistakes in Accounting for Partnership: Basic Concepts" wraps to 4 lines beside `Fix, about 3 min`, and the source line
ends "From Mock 3 on 16 Oct, with t...". Cut text, and it says "the lines you needed" on desktop only.
- Fix: under 600 px, stack the key under the text as a full-width neutral key (44 px), as the lead tile does, and drop the line clamp.
- Copy: `From Mock 3 on 16 Oct.` Files: `home/Suggestions.jsx`, `home/learn-home.css`.

**M8. The run's card on desktop is a tall empty box** (`50-run-card-front-1440-night`, `51-run-card-revealed-1440-night`).
The card is 467 px tall for "What is partnership?", and its back leaves about 245 px empty under a 3-line answer. B1 and B7 set desktop to fit its
content with a 360 px floor, which the feed already has (`10-feed-card-front-1440-night`, 360 px). This is LK22's "too much
blank space" on the screen he called "quite good".
- Fix `src/components/learn2/run/run.css`:
  - Line 224: `.lr-card { min-height: clamp(320px, 52vh, 520px); }` becomes `clamp(300px, 40vh, 360px)`.
  - Line 216 (tablet): `clamp(340px, 50vh, 480px)` becomes `clamp(300px, 46dvh, 380px)`.
- Both faces then measure to the taller one, as in the feed.

**M9. The stop sheet's two ways out read the same** (`17-feed-stop-sheet-390-night`, `54-run-stop-sheet-1440-night`).
`Stop here` (volt) and `Leave, pick it up later today` give no hint that one ends the session and shows the summary while the other keeps it to resume.
- Copy: volt `End here, see how it went`, then `Keep going`, then the text key `Leave for now, pick up later today`.
- The checkpoint's second key becomes `End here`. File: `stage/Sheet.jsx` (and the checkpoint copy in `feed/ChapterFeed.jsx` / `run/RunPlayer.jsx`).

**M10. Long match questions on a phone hide the options with only `Skip` in the bar** (`13-feed-question-390-night`,
`13-feed-question-360-night`, `80-real-match-the-column-and-longest-360-night`).
The first screen is the stem and List-I/List-II in bold, the options are below, and the only key is `Skip`. A first-timer reads that as "skip
this".
- Fix: while the first option is below the fold, show a quiet `Options below` chip with a down chevron (36 px tall, ink-2, centred 8 px above the bar). Tap scrolls to option A. Hide it once A is in view.
- Set list items in body weight (400), not the stem's bold.
- Files: `stage/Question.jsx`, `stage/Stage.jsx`, `stage/stage.css`.

---

## 3. Nice-to-have (short)

- N1. Phone checkpoint: move the block to the upper third and put the kept pile and `Up next: 9 Key cards and 2 questions` under it, so it isn't one line in about 760 px of dark (`16-feed-checkpoint-390-night`).
- N2. Cloze (Key line) backs say the sentence twice: the small prompt and then NCERT's line (`11-feed-card-turned-390-night`). For cloze cards, skip the small prompt.
- N3. Covers and Learn home status words: `Too few answers` → `Not enough answers yet`; `Holding` → `Steady` (`01-explore-covers-1440-night`, `30-home-top-1440-night`).
- N4. The feed's and the run's phone top bars differ (feed: ticks on top, `4 of 16 ⌄`, kept count; run: pile glyph, ticks below with the time). Use one bar (`10-*` vs `50-*`).
- N5. The run's phone question has no Save until answered, while the feed has Save and Chapter (`52-run-question-390-night`).
- N6. Questions-only run panel shows `In Revise 0` with an empty pile (`82-real-statements-1440-night`). Hide it when the run has no cards.
- N7. A right-edge fade on the desktop cover row instead of a hard cut through the fifth cover's letters (`01-explore-covers-1440-night`).
- N8. Content: keep one of `Define partnership.` / `What is partnership?` (both Must-know; `60-cards-all-*`). NCERT's own "transfered" spelling shows in the line (`53-run-wrong-line-*`); leave it as quoted.
- N9. Check flag-off Explore's CLS 0.137 at 390 against live, and the Free refused stage's CLS 0.02-0.048 (target 0.01).
- N10. Print: one real Ctrl+P to confirm the 16/14/20 mm margins and that the footer clears the last source line.

---

## 4. The 0/1/2 rubric, per area, from these captures only

0 = fails, 1 = works with clear gaps, 2 = meets the bar. A11y and performance are capped at 1 because none was exercised
(no screen reader, keyboard walk beyond the key measures, reduced motion or throttle).

| Area | Fit | Action clarity | Data truth | Continuity | Agency | Visual craft | Feedback | Emotional fit | A11y | Perf | Return value | Total /22 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Explore covers | 2 | 2 | 1 (M3, M4) | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | **18** |
| Feed | 2 | 2 | 2 | 2 | 2 | 1 (M2, M10, desktop gap) | 2 | 2 | 1 | 1 | 2 | **19** |
| Chapter page | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | **19** |
| Run and run end | 2 | 1 (M9) | 2 | 2 | 2 | 1 (M1, M2, M8) | 2 | 2 | 1 | 1 | 2 | **18** |
| Learn home and search | 2 | 2 | 1 (M5) | 2 | 2 | 1 (M6, M7) | 1 | 2 | 1 | 1 | 2 | **17** |
| Key cards view | 2 | 2 | 1 (E4 duplicate) | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | **16** |
| Print sheet | 2 | 2 | 2 | 1 | 1 | 1 (margins unproven) | n/a | 2 | 1 | 1 | 2 | **15/20** |

**Bottom line.** This build answers LK20, LK21, LK22 (mostly), LK13, LK6, LK7 and LK11 on screen. What would still read as
"unfinished" to him: the statements wall (M1), a wrong answer that hides your own pick (M2), the cover that says one thing and does
another on Free (M3), a first card about "this amount" (M4), two due counts (M5) and the tall empty run card (M8). Fix M1 to M10, then
re-capture `15-*`, `30-*`, `50-*`, `53-*` and `82-*` at 360, 390 and 1366x650.
