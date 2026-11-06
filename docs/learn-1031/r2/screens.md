# Learn v2 round 2: screen findings (1 Nov 2026)

Lens: every Learn screen at 390 and 1440, for LK24 (clutter), LK27 (open with an offer to start, not zeros), LK29 (first-time cues), LK30 (blank space) and LK31 (end screens: too many lines). Evidence: `tmp/learn-1101/r2-before/` (named below by file). Ranked by what the owner will feel first on his phone.

Rules used on every item: one primary action per screen; never lead with a zero or a line of zeros; no nested cards; sentence case; no gradients or glow; motion 150-220 ms for state, 220-350 ms for a result, reduced motion = instant or a 120 ms fade.

**End-screen formula (LK31):** the chapter name as a quiet line (15 px, ink-2), a headline (34 px display), up to 3 numbers in one row (32 px tabular numerals, 13 px label under each), and 1-2 actions (one volt, one text key). Nothing else. Any number that is 0 is dropped, not shown. The top-right "17 of 17" counter, the table rows and every extra "Back to ..." key go. Close (X) is the way out.

---

## 1. Run end: 20 lines become 6 (LK31)
- **Wrong:** `55-run-end-390-night.png` is a scroll page: a 3-line title, a done line, the pile, "16 in Revise", "14 back Wed, 2 back in 20 days", a 3-row table (which repeats "16"), "Next: Profit and Loss Appropriation Account", "The next chapter in your book.", Start, then 3 more option rows and "Back to the chapter". That is 4 exits and about 20 lines. At 1440 (`55-run-end-1440-night.png`) the right column is a menu and the bottom 40% is empty.
- **Why:** this is his "too many lines and walls of text" (LK31). A 16-year-old wants one thing: "did I do well, what now".
- **Fix (exact copy, Pro):**
  - Line: `Accounting for Partnership: Basic Concepts` (15 px, ink-2, 1 line, ellipsis)
  - Headline: `20 done in 9 min` (or `Stopped at 7 of 20`). Mobi (64 px) sits to the right of the headline, not floating 120 px away.
  - Numbers row (3 equal columns, no hairlines): `16` / `in Revise, back Wed` · `2 of 2` / `questions right` · `1 of 2` / `mistakes fixed`. Drop a column whose value is 0. The "1 still open" moves into the second action.
  - The pile: keep it as the visual, at 72% scale (cards 104x132 at 390), centred above the numbers. It replaces the "16 in Revise" heading and its return-days line.
  - Action 1 (volt, full width at 390, 360 px at 1440), two lines inside the key: `Next chapter, 10 min` / `Profit and Loss Appropriation Account` (13 px, 70% ink).
  - Action 2 (text key, centred): `Fix 1 open mistake, 2 min` when one is open; else `Another 5 minutes here`. Drop "Test it in a full mock" (it lives in Practice) and "Back to the chapter" (the X does it).
  - 1440: one centred column 560 px wide, top at 120 px; no right column.
  - Motion: the numbers count up 0 to value over 300 ms ease-out, 60 ms stagger; the pile fans in at 220 ms; Mobi nods once (rotate -6deg to 0, 420 ms) on arrival and winks on tap (LK32's "reactive Mobi" applied here). Reduced motion: final state at once.
- **Files:** `src/components/learn2/run/RunEnd.jsx`, `run/runView.mjs` (`endLines`, `reviseSummary`, `leadView`), `run/run.css` (`.lr-endform*`, `.lr-rpile*`), `src/lib/server/learn.js` (the option list it returns: cap at 1 extra), `run/runView.test.mjs`.

## 2. Feed end and Free feed end: same formula, top-aligned, no zeros (LK31, LK30)
- **Wrong:** `18-feed-end-390-night.png`: "3 kept" + "They are first in Revise." then a table whose first row says "12 seen, 3 kept" again, two buttons, "Back to Explore", and a "17 of 17" counter. `95-feed-end-free-390-day.png`: the block is vertically centred with 290 px of empty cream above it, leads with "Nothing kept this time. Keep a card and it comes back in Revise.", shows "5 seen, 0 kept", a 2-line Free paragraph, See Pro, and no volt key at all. `18-feed-end-1440-day.png`: 200 px blank top, left and right columns float.
- **Fix (exact copy):**
  - Line: `Admission of a Partner`. Headline: `17 done in 6 min`.
  - Numbers: `3` / `kept for Revise` · `3 of 3` / `questions right` · `1 of 2` / `mistakes fixed`. With 0 kept: no pile, no "Nothing kept" line, the first number becomes `12` / `cards seen`.
  - Pro actions: volt `Another 10 minutes`; text key `Next: Retirement and Death of a Partner`. Remove "Back to Explore" and the "17 of 17" counter.
  - Free actions: one 13 px line above the keys: `Today's free session is done. Pro has no daily limit.` with `See Pro` as an inline text key at its end; volt `Quick recap, 1 min`; text key `Questions on this chapter`.
  - Layout: top-aligned at 72 px (390) / 120 px (1440), one 560 px column at 1440.
- **Files:** `src/components/learn2/feed/ChapterFeed.jsx` (end block about lines 560-600, `endRows` about 57-66, `panelRows` about 413), `stage/EndForm.jsx`, `stage/stage.css` (`.st-endform*`, `.st-pile*`), `stage/stageText.mjs` (`doneLine`).

## 3. Explore feed: a visible "swipe up" cue on the first visit (LK29)
- **Wrong:** `91-feed-first-visit-first-item-390-night.png` and `91-feed-first-visit-after-4s-390-night.png` are identical: no cue at all after 4 s. The only nudge in code is a 24 px, 360 ms bob of the track that fires once, only on a coarse pointer, only after the first "Turn over" (`ChapterFeed.jsx` 264-270). He missed it. The story ticks at the top suggest tap-to-advance like Instagram, but it moves by a vertical swipe.
- **Fix:**
  - Peek: on every feed item at 390, the next item's top edge shows 28 px above the action bar (the card height shrinks by 44 px). It says "there is more below" without words, always.
  - First-visit cue (until the student has moved once, by any means): a chip centred 12 px above the action bar: chevron-up icon + `Swipe up for the next one` (phone) / `Scroll or press ↓ for the next one` (desktop, replaces the current bottom hint line). The chip bobs translateY 0 to -6 px, 900 ms ease-in-out, 3 times, then rests. It fades out (160 ms) on the first move, and only then is the flag written (today it is written when it is shown).
  - After the first "Turn over", the step key reads `Next` with a chevron-down, and the track does a 40 px peek-and-return (420 ms, spring-like ease `cubic-bezier(.2,.8,.2,1)`), on all pointers, not only coarse.
  - Reduced motion: chip shown, no bob, no peek animation.
- **Files:** `src/components/learn2/feed/ChapterFeed.jsx` (hints, `turn`), `stage/Stage.jsx` (`ActionBar` hint slot), `stage/stage.css`, `stage/usePager.js` (peek offset), `feed/feedModel.mjs`.

## 4. Learn home on a phone: the offer first, the furniture after (LK27, LK24)
- **Wrong:** `30-home-top-390-day.png`: header, the Practice tab row, a 300 px subject strip of 3D objects, the search field, three stat tiles, and only then the first action (the volt sits at 68% of the screen height). `86-learn-home-fresh-free-full-390-night.png`: a new student's first line is "Nothing in Revise yet. Cards you study land here." (an announcement of nothing), then three stacked cards (Start / Find your level / Chapter 1 as a feed), three competing actions.
- **Fix:**
  - Subject strip: one row of 40 px objects + name chips, 64 px tall (from 300). The selected one gets the volt underline, as now.
  - Directly under it, the hero (no card box, just type on the page): new student: headline `Start learning Accountancy`, line `Chapter 1, Accounting for Partnership: Basic Concepts. 10 min of cards and questions.`, volt `Start 10 minutes`. Returning: `Pick up Admission of a Partner`, line `6 of 16 done. About 5 min left.`, volt `Pick up, 5 min`.
  - Under the hero, two text keys in one row: `Find your level, 6 min` · `Try it as a feed`. The two other cards go.
  - The search field moves below the hero. The three stat tiles become a single row of text keys under the field, each hidden when 0: `9 due today · 6 missed lately · 26 in Revise`. All zero: nothing at all (delete the "Nothing in Revise yet" line).
  - The chapter list heading becomes `Your roadmap` with the line `15 chapters, in book order` (his words, LK27).
- **Files:** `src/components/learn2/home/LearnHome.jsx`, `home/SubjectShelf.jsx`, `home/ShelfKeys.jsx` (line 19 and zero keys), `home/Suggestions.jsx`, `home/homeModel.mjs`, `home/learn-home.css`, `home/__tests__`.

## 5. Run and feed card at 390: one tall card, no voids (LK30)
- **Wrong:** `50-run-card-front-390-night.png`: 140 px of nothing above the card, 165 px below it, and inside the card the question floats in the middle with 220 px of empty card around it. `51-run-card-revealed-390-night.png`: the answer sits in the top half, 270 px of empty card under it, then another 300 px void. `52-run-question-390-night.png`: the options end at 47% of the screen and the rest is black down to "Skip". Same in the feed (`91-...-390-night.png`).
- **Fix:**
  - The card fills from 16 px under the progress ticks to 16 px above the action bar (flex: 1, min-height 420 px); it is a story page, not a floating tile. Front: the question top-aligned at 28 px inside, 34 px display; the source at the card's foot. Back: question (15 px, ink-2), hairline, answer (24 px NCERT serif), source right under the answer.
  - The flip stays a 3D turn at 320 ms; the card does not change size between front and back (no layout jump).
  - Question screen: stem and options start at the top; the action bar (Skip) sits right under the last option when the content is short (`justify-content: start`, bar `margin-top: 24px`, sticky only when content overflows).
- **Files:** `src/components/learn2/run/RunParts.jsx`, `run/run.css` (`.lr-body`, `.lr-card*`, `.lr-bar`), `stage/CardFace.jsx`, `stage/stage.css` (`.st-page`, `.st-front`).

## 6. Wrong answer at 390: the question disappears and the line is a wall (LK31)
- **Wrong:** `53-run-wrong-line-390-night.png` (and `-day`): after a wrong pick the page scrolls so the stem is gone; the student sees "Not quite. The answer is C." without the question. "The line you needed" then shows two full NCERT paragraphs (Fixed and Fluctuating) in 24 px serif, 10 lines, cut by the fade.
- **Fix:**
  - Scroll so the stem's last line stays in view: scroll to `stem.bottom - 56px`, not to the options row. If the stem is longer than 3 lines, it collapses to its first 2 lines + `…` with a tap to expand.
  - The line box shows at most 4 lines (19 px serif, line-height 1.5) with a 32 px fade and a text key `Read the whole line`; for a two-part "Difference" card, show the part that matches the right option first (here: Fixed Capital).
  - The verdict reads `Not quite. It's C.` on one line in the same row as the line box's title, saving a row.
- **Files:** `src/components/learn2/stage/Question.jsx` (line 159 `scrollToRow` target), `src/components/keycards/LineYouNeeded.jsx`, `run/run.css` / `stage/stage.css`.

## 7. Stop sheet: three exits become two, and no "0 of 1 right" (LK24, LK31)
- **Wrong:** `54-run-stop-sheet-390-night.png`: "5 of 20 done. 0 of 1 question right. 4 sent to Revise. Everything you did is saved." (a zero, three facts), then "End here, see how it went", "Keep going", "Leave for now, pick up later today", plus the X. A first-timer cannot tell "End here" from "Leave for now". Same in `93-run-stop-sheet-390-day.png`, `94-feed-stop-sheet-390-night.png`.
- **Fix (exact copy):** title `Stop for now?`; body `5 of 20 done. It's all saved.`; volt `Stop here`; line key `Keep going`. Drop the third key: Stop here shows the end screen and the run stays open to pick up today (home and chapter page already offer "Pick up"). The X closes the sheet (= keep going). Sheet rises 260 ms `cubic-bezier(.2,.8,.2,1)`; Day scrim `rgba(20,24,20,.28)` (93-day reads muddy grey at the current strength).
- **Check first:** that ending a run keeps it resumable the same day on the server; if not, make it so before removing "Leave for now".
- **Files:** `src/components/learn2/stage/Sheet.jsx` (`StopSheet`), `run/RunPlayer.jsx` (about 482-495), `feed/ChapterFeed.jsx` (about 335, 616), `src/lib/server/learn.js` if resume needs it, `stage/stage.css`.

## 8. Chapter page: fewer lines, and fill the space with what is lined up (LK30, LK10, LK24)
- **Wrong:** `89-chapter-fresh-free-full-390-day.png`: a 3-line 44 px title, "Tap a pile to leave it out.", a 2-line "Cards and questions, one at a time. Stop whenever you like; what you do is saved." under Start, a 2-line recap link (`40-chapter-10min-390-night.png`), then "No lesson yet. No open mistakes." (announcing two absences), then 300 px of nothing. `40-chapter-10min-1440-night.png`: the bottom half of the page is empty and the piles are just numbers.
- **Fix:**
  - Title 32 px, max 2 lines, `text-wrap: balance`; object 64 px.
  - Delete the first-visit line under Start (the run's own first-card coach already says it) and the "No lesson yet. No open mistakes." line (hide rows that have nothing).
  - Recap link on one line: `Quick recap: 12 Must-know lines, 2 min`.
  - New "First up" row under Start (fills the void with the thing he asked for in LK10, "see what is lined up"): 3 mini card fronts (140x96, 13 px display, real fronts from the dry run), horizontal scroll at 390, a row at 1440. Tapping one opens the Key cards view at that card. Motion: they deal in from 12 px below, 220 ms, 50 ms stagger, when the time choice changes.
  - 1440: left column 640 px; the "Everything in this chapter" list stays right but its top aligns with "How long have you got?", not with the title.
  - Copy fix: "46 cards, Free opens 5" becomes `46 cards. 5 open on Free.`
- **Files:** `src/components/learn2/chapter/ChapterPage.jsx` (around 360, 515), `chapter/chapterModel.mjs` (`FIRST_VISIT_LINE`, line 95 `missing`), `chapter/chapter.css`, `chapter/chapterModel.test.mjs`.

## 9. Free "session used" screen: one message, not two; three actions, not five (LK31, LK24)
- **Wrong:** `21-feed-free-refused-390-night.png`: the headline "Today's free session is used" and the body "Your free Learn session for today is done..." say the same thing; then 4 full-width keys and See Pro; top 450 px empty (centred block).
- **Fix:** top-aligned at 120 px. Headline `Today's free session is used`; line `Explore questions stay free. Pro has no daily limit.`; volt `Pick up where you stopped` with sub-line `Admission of a Partner, 1 of 12`; line key `Revise 3 due cards, 1 min`; text key `See Pro`. Remove "Quick recap" and "Questions on this chapter in Explore" keys here (Close returns to Explore).
- **Files:** `src/components/learn2/feed/ChapterFeed.jsx` (about 490-510), `run/RunPlayer.jsx` (about 575-595, the run's version), `src/lib/server/learn.js` (the line text).

## 10. 1440 run: a rail of zeros, and the card jumps between items (LK30, product rule)
- **Wrong:** `51-run-card-revealed-1440-day.png`: the left rail leads with "Key cards 0 of 16, Questions 0 of 2, Your mistakes 0 of 2, In Revise 0": a column of zeros. The card's top is at 232 px here and the question's at 120 px in `53-run-wrong-line-1440-night.png`, so the stage jumps on every item. The bottom 220 px is empty.
- **Fix:** before an item of a kind is done, the row reads its total: `16 Key cards`, `2 questions`, `2 old mistakes`; after, `4 of 16`. "In Revise" is hidden until it is 1 or more, then it counts up (220 ms). The stage is top-anchored at 120 px for every item; cards get min-height 440 px at 1440 so the keys sit at a steady y.
- **Files:** `src/components/learn2/run/RunParts.jsx` (rail), `run/runView.mjs`, `run/run.css`.

## 11. Card faces in the end pile break mid-word
- **Wrong:** `96-run-end-free-390-night.png`: the top card reads "The Partnershi / p Act does not require". `.lr-rpile__front` uses `overflow-wrap: break-word; hyphens: manual` in a 13 px, 104 px card.
- **Fix:** `overflow-wrap: normal; word-break: normal; hyphens: auto;` with `lang="en"` on the element (as `.st-pile__f` has), and shrink to 12 px when the longest word is over 11 characters (do it in JS from the front text). Same check for `.st-pile__f`.
- **Files:** `src/components/learn2/run/run.css` (line 410), `run/RunEnd.jsx` (add `lang`), `stage/stage.css` (line 264).

## 12. Checkpoint: one line, not three; content up, not centred in a void (LK30, LK31)
- **Wrong:** `16-feed-checkpoint-390-night.png`: "1 of 1 right", "8 of 17 done. About 6 min left.", "Keep going, or end here. What you kept is already in Revise." in the middle of 900 px of black.
- **Fix:** block at 30% height. Headline `1 of 1 right`; one line `8 of 17 done, about 6 min left.`; drop the third line (`CHECKPOINT_LINE`). Under it, the kept pile (if any) as the small fan, 80 px. Keys as now (End here / Keep going). Headline number pops 0.96 to 1, 220 ms.
- **Files:** `src/components/learn2/feed/feedModel.mjs` (line 43, `CHECKPOINT_LINE`), `feed/ChapterFeed.jsx`, `feed/feed.css`.

## 13. Run top bar at 390: slimmer, and the unexplained "4"
- **Wrong:** `52-run-question-390-night.png`: "Accounting for Partnershi..." truncated, a deck icon with a bare "4", "5 of 20", and a second row "about 9 min left": 2 rows, 140 px, one unlabeled number.
- **Fix:** one row, 56 px: X · ticks (flex) · `5 of 20` · pile icon with the count. Drop the chapter title on phones (it is on the chapter page and the end). "About 9 min left" moves under the ticks only at checkpoints. The pile count gets `aria-label="4 sent to Revise"` and, the first time it goes from 0 to 1, a 1.6 s tooltip `Sent to Revise`. Saves about 70 px for the card (item 5).
- **Files:** `src/components/learn2/run/RunParts.jsx`, `run/run.css` (`.lr-top*`).

## 14. Find has no identity of its own
- **Wrong:** `92-find-pro-390-night.png` is the Learn home with a Cancel key: the pick-up card and the "3 cards due" card still fill the screen under a focused field. `92-find-fresh-free-1440-night.png` is the Learn home exactly.
- **Fix:** in Find (`lv=find` or a focused field), the hero, suggestions and roadmap hide (160 ms fade); the field sits at the top; under it, the three shelves as list sections with real card fronts: `Due today`, `Missed lately`, `In Revise` (each hidden when empty), each with one key `Revise these 9`. New student with nothing: one line `Search any word from the book, like "goodwill".` and 4 suggestion chips.
- **Files:** `src/components/learn2/home/LearnHome.jsx` (around 159, 206), `cards/FindView.jsx`, `home/learn-home.css`.

## 15. Revise was not captured
- **Wrong:** no shot shows the In Revise set (FindView "A set") or a Revise run. It is a named surface in this round's lens.
- **Fix:** add `view=learn2&lv=find&shelf=revise` (390 and 1440, both themes) and a cards run of due ids to `scripts/design-audit/learn-1101-final-capture.mjs` before round 2 sign-off; apply item 14's layout to it.
- **Files:** `scripts/design-audit/learn-1101-final-capture.mjs`.

## 16. The Practice tab row on depth screens (LK26, LK24)
- **Wrong:** `40-chapter-10min-390-night.png`, `42-chapter-resume-390-night.png`: the 5-tab horizontal row (Practice, Learn, Your papers..., cut off, with an arrow) takes 130 px on the chapter page, above "< Accountancy". A first-timer sees two navigations stacked.
- **Fix (keeps the current nav, which the owner approved):** on Learn depth screens (chapter page, Key cards, Find) hide the row at 390 and keep only the back link `< Accountancy`, which gets the 44 px target. On top-level pages, shorten the third tab to `Papers` with its count badge so 4 tabs fit at 390 without the arrow.
- **Files:** `src/lib/arenaNavigation.js` (`placeTabs`), the arena shell that draws the row, `chapter/ChapterPage.jsx`.

## 17. Chapter page with an unfinished run: two primaries
- **Wrong:** `42-chapter-resume-390-night.png`: "Pick up where you stopped" (volt), then a hairline, the whole time picker, the piles, and "Start a new 10 minutes": two complete flows.
- **Fix:** keep the resume block; collapse the picker under a text key `Start fresh instead` that expands it (240 ms height). Copy: `You stopped at 6 of 16 today. About 5 min left.` on one line.
- **Files:** `src/components/learn2/chapter/ChapterPage.jsx`, `chapter/chapter.css`.

## 18. Day theme: a blue-violet tint on every card surface (no gradients)
- **Wrong:** `51-run-card-revealed-1440-day.png`, `30-home-top-390-day.png`, `89-chapter-fresh-free-full-390-day.png`: card tops wash to a cool lavender from `radial-gradient(... var(--kc-cool) ...)`; in Night it reads as a blue glow (`50-run-card-front-390-night.png`). The owner's rule is no gradients or glow, and the hue is off the green-cream palette.
- **Fix:** replace the radial with a flat surface + the grain: Day `#ffffff` with a 1 px `rgba(28,40,28,.10)` border; Night `#1b241e`. Contrast checked otherwise: Day text and the volt keys pass; the faded options (B, D in `53-run-wrong-line-390-day.png`) are about 4.2:1, raise them to ink-2 at 100%.
- **Files:** `src/components/learn2/chapter/chapter.css` (9, 19), `feed/covers.css` (83), `home/learn-home.css` (14), `src/components/keycards/keycards.css` (`--kc-cool`).

## 19. 1440 feed: tools float off the card, the rail is mostly empty (LK20, LK30)
- **Wrong:** `91-feed-first-visit-first-item-1440-night.png`: Keep and Chapter float in a column 30 px right of the card; the rail has 3 lines then 550 px of nothing with "Stop here" at the bottom; 230 px gap between card and keys.
- **Fix:** Keep and Chapter join the action bar left of "Turn over" (icon + label keys, 44 px). The card grows to min-height 480 px and the keys sit 24 px under it. The rail gets an "Up next" stack: the next 3 items as 13 px one-line titles with their kind (`Card`, `Question`), the current one marked; "Stop here" moves under it.
- **Files:** `src/components/learn2/feed/ChapterFeed.jsx`, `stage/Stage.jsx` (`ActionBar` left/right), `feed/feed.css`, `stage/stage.css`.

## 20. First-time coach lines: shorter and once
- **Wrong:** `51-run-card-revealed-390-night.png`: "Got it sends the card to Revise. It comes back when it is due." (2 lines) under the rating keys.
- **Fix:** `Got it: it comes back when it's due.` (1 line), shown for the first 2 cards only, then never (flag in localStorage, try/catch).
- **Files:** `src/components/learn2/run/RunPlayer.jsx` (552-554).
