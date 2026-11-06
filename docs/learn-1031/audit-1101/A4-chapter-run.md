# A4: the chapter page, the run player and the run end (audit and refined design, 1 Nov 2026)

**Scope.** `src/components/learn2/chapter/**` (ChapterPage.jsx, chapter.css) and `src/components/learn2/run/**` (RunPlayer.jsx,
RunEnd.jsx, run.css; runMath.js read only), plus the server strings they print (`data/learn/compose.js`, `data/learn/suggest.js`,
`src/lib/server/learn.js`).

**Inputs.** The captures in `tmp/learn-1101/audit/` (40 to 48 chapter, 50 to 59 run and end, and 11, 14, 17, 18 of the feed for
consistency) and the measurements in its `index.md`; the code above; OWNER-FEEDBACK-2026-10-31-LEARN.md (LK1 to LK23, newest 1 Nov
1:25 am); DESIGN-SPEC A1 to A12; CRITIQUE-1 (C1 to C6, R1 to R7); FEED-2; BUILD-1101 Part B (B1, B2) as context; the owner's UI
standards (slop list, done check); the research brain's AGENT_RULES and its 12-part test; DESIGN.md and PRODUCT.md.

**What I exercised.** I read every capture listed above and the code. I did not run a browser (the capture step had run; RAM rule).
Two things are **derived, not captured**: the page at 1024 px with the sidebar, and a real 1366 x 768 laptop, whose browser shows
about 1366 x 650 of page. Both are marked "derived".

**How this file sits with BUILD-1101.** Part B there decides the frame (B1: one study stage for the feed and the run; B2: the run,
the chapter page and the end). This file gives the exact values B1 and B2 leave open, and section 5 lists the eight places where I
recommend something different, each with its evidence.

---

## 0. In short

- **The chapter page is right and stays.** The owner called the chapter run "quite good" and liked that "the customization according
  to the time adjusts the questions". Keep the flow, the control, the piles and the one volt key. Fix: the Start key falls below the
  fold on a real 1366 x 768 laptop and sits half under the app dock at 360 x 780; the jargon note "Ratings join Revise. Questions are
  free."; the two-column board crushing the page at 1024; the same Accountancy object on every chapter (his LK21 complaint); and three
  places where the screen says one thing and does another (the "Next chapter" pile, Free's forced-out piles, the "10 min" segment that
  turns into "9 min").
- **The run's plumbing is solid; its composition is the problem the owner named.** On a 1440 x 900 screen the item is a 640 x 300
  landscape box with a 23 px prompt, about 400 px empty on each side, 180 px empty above and 240 px below. On a phone it is a tall,
  mostly empty box over a 180 px band that holds only "In Revise 0". Proposed: B1's frame with exact values. On desktop a session
  panel shows the piles the student chose being worked down and the Revise pile the cards fly into; the card is a real flashcard
  whose type scales with its length (44 px on desktop); the keys sit right under it. On a phone the card fills the space between the
  top bar and the action bar.
- **A wrong answer is a wall of text in a box inside a box.** Questions move off the card face onto the page, as in the feed; one
  option component is shared with the feed (volt fill for a right pick, volt outline for the key); the line you needed comes first,
  and the explanation folds behind "Why C".
- **The end repeats every number, and on Free it shows a volt "See Pro" with no reason** (the server's line is dropped). Proposed: the
  feed end's form (label and value lines, a pile of real card faces, the chapter's state change as the one milestone motion), two
  columns on desktop, and on Free the line with a See Pro text key while the volt goes to the first thing that still works today.
- **Two missing controls that make it more useful:** a calm "Stop for now?" sheet that shows what you did (today only rounds of 20
  cards can finish early), and a visible "Pick up where you stopped" on the chapter page (BUILD 1.3 resumes silently today).
- **Score:** 0/1/2 rubric now 14, 16 and 17 of 24 (chapter, run, end); the proposal targets 22, 22 and 22 once its checks pass
  (section 4).

---

## 1. What works and must be kept

**Chapter page**
1. The route is his LK10 flow and he called it "quite good": title and state, "How long have you got?", piles that re-balance with
   the length, `Start 10 minutes`, the quick recap (40-chapter-10min-*, 41-chapter-5min-*, 42-chapter-20min-*: 10/1/1 at 5 min,
   16/3/2 at 10, 32/7/3 at 20).
2. The length control: one segmented control with a sliding thumb (240 ms), arrow keys, Home and End; "Your own" with three presets
   (30 min, 45 min, 1 hour), a 5-minute stepper and `Use 35 minutes`, a focus trap and Escape (43-chapter-own-*).
3. The piles as the page's one object: three papers, a faint print hint (two lines, four option dots, a red margin), counts that roll
   in 180 ms, a fan that re-spreads in 220 ms, "Left out / Tap to put back" at 40 %, the last pile that shakes.
4. One volt key that always names the length (A1, T007: a specific call to action).
5. The quick recap as a secondary text key with its count and minutes.
6. "In this chapter" as the place that shows what is where (LK10), hairline rows, no box.
7. The skeleton at final size: CLS 0 to 0.003 on every chapter capture (index.md section 3).
8. The state ring shared with the chapter map (C4).
9. The remembered length (T001: a default from real context, visible and editable).

**Run player**
10. Server truth: grading on the server with no key on the client; a card leaves only after the server accepts its rating; real
    return-day stamps; the Revise count from the server (T002: progress counts only finished items).
11. The book face: NCERT's words in Literata with a 1 px rule and the page source (51-run-card-revealed-*).
12. Keys: Space, 1 2 3, A to D or 1 to 4, Enter, the arrows in a recap; focus moves to each new item; live regions.
13. The first-run coach lines, once each (A11).
14. The Got it flight (A4 values) with the next card rising at 220 ms, so no frame is empty.
15. The fixed-mistake moment (check draws in 200 ms, Mobi nods for 900 ms).
16. The line's card coming back later in the run, with its note.
17. Calm failure states: "This run did not start", "Your answer did not reach us. Try again.", "Your run is saved".
18. The recap player (Previous, Next, a 72 px swipe or a quick flick) and the 20-card rounds of a cards run.

**Run end**
19. "10 minutes on {chapter}" and Mobi's one reaction matched to the result (endAct).
20. The Revise pile fanned open with real return days (A4).
21. "moved from Getting there to Holding" (Pro only, never from Not started).
22. A lead plus three named options, each with a reason (LK11: a dynamic next action with options), and Back to the chapter.

---

## 2. Findings, by severity

Each finding: what I saw, the evidence (capture and file:line), the rule, and where the fix is.

### Blocker (the owner named it)

**F1. Run, desktop: a small landscape card in an empty window.** At 1440 x 900 the stage is one 640 px column; the card is
640 x 300 with a 23 px prompt in its top-left corner; about 400 px are empty on each side, 180 px above, 240 px below. The same at
1366 x 768 and in Day. Evidence: 50-run-card-front-1440-night.png, -1366-night, -1440-day, 51-run-card-revealed-1440-night,
52-run-question-1440-night, 54-run-lesson-1440-night; run.css lines 11 (`--lr-col: min(100% - 32px, 640px)`), 20 to 24 (centred
stage), 64 to 67 (`min-height: 300px`); keycards.css line 291 (prompt `clamp(19px, 2.3vw, 23px)`). Rule: LK22 "too much blank space";
standards 3 (no dead bands; one visual anchor that carries information). This composition came from CRITIQUE-1 R5 ("centre the card
vertically ... max 640 px column"). Fix: 3.3.1 to 3.3.6.

### High

**F2. Run, phone: a tall empty card and a dead band.** At 390 x 844 the card is at least 50dvh (422 px) with the prompt at 19 px
top-left (the clamp's floor), so about 60 % of the card is empty; under it a band of about 180 px holds only "In Revise 0" and its
glyph, then the keys. Evidence:
50-run-card-front-390-night, -360-night, 52-run-question-390-night (the band also holds "Tap the answer you think is right."),
54-run-lesson-390-night; run.css lines 66, 158, 193; RunPlayer.jsx line 732. Fix: 3.3.1, 3.3.2, 3.3.5.

**F3. Free end after the day's session: a volt "See Pro" and no reason.** The server sends
`lead: { line: 'Your free Learn session for today is done. ...', label: 'See Pro', href: '/pricing' }` (learn.js line 1054);
RunEnd draws only `label` and `evidence` (RunEnd.jsx lines 41 to 47), so the line never shows and the screen's one primary action is
an unexplained upsell (57-run-free-end-390-night.png). Rules: LK15 (the limit is said in one line, only at the limit), BUILD 1.6 ("the
lead is the line with a See Pro text key"), AGENT_RULES 18 (say what happens next) and the standards' honest-money rules (section 13:
no pressure, T005, T009). Fix: 3.4.4.

**F4. Chapter page, a real laptop: Start is below the fold.** At 1366 x 768 the Start key sits at y 708 to 752, its note and the recap
below the fold (40-chapter-10min-1366-night.png). A 1366 x 768 laptop with browser tabs and the Windows taskbar shows about
1366 x 650 of page (the owner's own check size), where the whole key is below the fold. Derived from the capture plus about 118 px of
browser chrome. Fix: 3.2.2.

**F5. Chapter page, 360 x 780: the Start key half under the app dock.** Key top at 667 css px, dock top at about 705; the label is
faded under the dock's fade (40-chapter-10min-360-night.png). Slop list 1 (floating UI over a control at a target size). Fix: 3.2.3.

**F6. A wrong answer is a wall of text, in a box inside a box.** Verdict, a 3-line explanation with More, then "The line you needed"
as a sunken panel inside the question's card, then "This card comes back later in this run."; at 1440 x 900 and at 390 the line
needs a scroll (53-run-wrong-line-1440-night and -bottom, 53-run-wrong-line-390-night and -bottom; RunPlayer.jsx lines 261 to 292).
Rules: LK11 (no walls of text), standards 3 (never nest cards). Fix: 3.3.6.

**F7. The run and the feed answer in different colours.** Run: the key row washes green with a green letter chip and a green check;
feed: a right pick fills volt and the key is outlined volt (53-run-wrong-line-1440-night against 18-feed-wrong-sheet-390-night;
run.css lines 113 to 120 against feed.css lines 104 to 111). The task asks shared parts to match; DESIGN.md's drill fills a right
answer volt. Fix: 3.3.6.

### Medium

**F8. Questions sit inside a card face in the run**, so the option boxes are boxes inside a box (52-run-question-*), while the feed
shows the stem and options on the page (14-feed-question-1440-night). CRITIQUE-1 R2 asked for "the same card face as the feed" when
the feed still had one; the feed has dropped it. Fix: 3.3.6.

**F9. "Ratings join Revise. Questions are free."** Two product nouns and no plain verb; "Questions are free" means nothing on Pro and
is wrong on a chapter with no questions (47-chapter-no-questions-1440-night). Evidence: compose.js lines 44 to 45 and 471,
ChapterPage.jsx line 449. BUILD B2 removes it. Fix: 3.2.5.

**F10. The lesson item asks one thing and its volt key does another.** The card says "Read it first", the outline key opens the
lesson, the volt "Next" skips it (54-run-lesson-1440-night; RunPlayer.jsx lines 297 to 306 and 727 to 730). Opening the lesson leaves
the run with no way back; in the preview `links.lesson()` goes to Learn home (links.js line 50). Fix: 3.3.9.

**F11. The same Accountancy object heads every chapter.** The calculator and ledger sit on Basic Concepts, Admission and Goodwill
alike (40, 46, 47; ChapterPage.jsx line 477). LK21 is this complaint about the covers; B1 and B4 remove the object from the feed, the
run and the covers. Fix: 3.2.1.

**F12. At 1024 px the board crushes the main column (derived).** With the 232 px sidebar (arena.css line 180) the board is about
732 px; from 1024 it splits into main, a 320 px shelf and a 56 px gap (chapter.css lines 35 to 38), leaving about 356 px for the
title, the control and three piles of about 100 px. Not captured. Fix: 3.2.2.

**F13. A capped or short run rewrites the chosen segment.** The student taps "10 min" and the segment then reads "9 min"
(44-chapter-free-1440-night, 45-chapter-new-390-night; ChapterPage.jsx lines 85 to 87, from CRITIQUE-1 C3). A control must keep
showing what was chosen; the real length belongs on the key. Fix: 3.2.4.

**F14. The "Next chapter" pile looks like an add and acts like a link.** A dashed paper with a plus, among piles that toggle in
place, opens the next chapter's page, and its title is cut ("Profit and Loss Approp...") (44-*, 45-*; ChapterPage.jsx lines 246 to
258). The server can already add the next chapter to this run (`addNext`, learn.js line 568). Fix: 3.2.4.

**F15. Free's Key-cards-only day: forced-out piles look toggleable (code).** After another run claims the day, the server forces
Questions and Your mistakes out (learn.js line 565); the page draws them "Left out / Tap to put back", and a tap cannot put them back
(ChapterPage.jsx lines 428 to 434). Not captured. Fix: 3.2.4.

**F16. The end says each number twice, as three hero figures.** "16 cards rated, 16 got it", "3 questions answered, 3 of 3 right",
"2 mistakes fixed, 2 of 2" (55-run-end-*; RunEnd.jsx lines 114 to 120). Slop list 15 (the hero-metric template). Fix: 3.4.2.

**F17. Shelf copy and dead rows.** "10 questions, all tied to these cards", "3 open. Fix them with their lines.", "7-minute lesson,
not read yet. Read it alone"; on Goodwill three of five rows are empty states (47; ChapterPage.jsx lines 330 to 355). Rules:
standards 7 (plain words), 3 (empty lanes collapse to one quiet line). Fix: 3.2.6.

**F18. The piles and the shelf list the same three names with different numbers** (16 and 46 Key cards, 3 and 10 Questions, 2 and 3
mistakes) and nothing says which is this run and which is the chapter (40-chapter-10min-1440-night). Fix: 3.2.6.

**F19. No way to stop early and see what you did.** Close leaves; only a cards run's rounds offer "Finish here". A student with 4
minutes left has no "stop here" (LK9: easy self-control). Fix: 3.3.10.

**F20. Resume is invisible (code).** BUILD 1.3 makes a start resume today's unfinished run of the same chapter, but the chapter page
still says `Start 10 minutes` and shows a fresh mix. The key would do something other than it says. Fix: 3.2.4.

### Low

**F21. The progress pips read as Morse code on a phone**: grouped by kind with 2 px minimums (50-run-card-front-390-night,
-360-night; RunPlayer.jsx lines 102 to 118, run.css lines 51 to 54). Fix: 3.3.2.

**F22. The end's lead key is held back 480 ms** (run.css line 242). A usable control waits on an animation (standards 8). Fix: 3.5.

**F23. Free's look line repeats under every look card** (RunPlayer.jsx line 736; 59-run-free-limit-*). Fix: 3.3.8.

**F24. The run hides the chapter title on a phone** (run.css line 43) while the feed shows it (11-feed-card-front-390-night). Fix:
3.3.2.

**F25. A pile line cuts a number at 360**: "2 of 3, about 2 ..." (40-chapter-10min-360-night). Standards 2: never truncate figures.
Fix: 3.2.4.

**F26. Three place names before the title on a phone**: the "Learn" chip, "< Learn", "Accountancy, Part 1"
(40-chapter-10min-390-night). Fix: 3.2.1.

**F27. Three widths and three right edges at 1440**: control 560 px, piles 692 px, key 300 px (40-chapter-10min-1440-night;
chapter.css lines 59, 122, 219). Fix: 3.2.2.

**F28. "Tap the answer you think is right." under every question** fills the action bar (52-run-question-*; RunPlayer.jsx line 726).
Fix: 3.3.6.

**F29. One mistake label, two looks**: amber in the run, text-3 in the feed (52-* against 18-*). Fix: 3.3.6.

**F30. Return days in three forms**: "back on Wed", "back in 20 days" on the end, "Back Wed" on the stamp (55-*). Fix: 3.6.

**F31. A single-pile chapter does not say why** the others are missing (47: one pile, blank space to its right, the reason only in
the shelf). Fix: 3.2.5.

**F32. One console warning in my area**: React's "state update on a component that hasn't mounted yet" on the chapter page at 390
during the lengths job (index.md section 3, chapter-lengths 390). Suspect: OwnSheet's portal and its placing effect. Fix: reproduce by
opening and closing Your own at 390, fix before the next capture.

---

## 3. The refined design

### 3.0 Experience brief (standards section 1)
- **Job.** A 16 to 17 year old picked a chapter in Learn; they want to study it for the time they have, then know what to do next.
- **Outcome.** One action per screen: Start the run; turn the card, rate it; answer; go on; take the next step at the end.
- **Data truth.** Every count comes from the dry run or the run (real); return days are the server's; nothing is estimated except
  "about N min", which says "about".
- **States.** Loading, error, refreshing, stale, short chapter, single kind, Free taste, Free capped, Free used, resume, first visit,
  pending answer, failed answer, question changed, run ended elsewhere, stopped early.
- **Persistence.** A rating or an answer counts once the server acknowledges it; nothing says "saved" before that (A4).
- **Feel.** Concentrate during the run, acknowledge at the end. Motion answers each action; one authored moment per screen.
- **Acceptance.** Section 3.10.

### 3.1 Six rules these screens share
1. **Cards are objects; questions sit on the page.** A Key card is drawn as a card. A question is a stem and option rows, never a
   box inside a box.
2. **The piles you chose are what you work down.** Chapter page piles, then the session panel's piles (desktop), then the end's lines.
3. **The item is the anchor.** The space beside it carries real numbers about this session, never decoration.
4. **One volt action per viewport:** Start, Show answer, Got it, Next, Read the lesson, the end's lead.
5. **Plain words.** "Revise" stays as the name of a place; it is never used as jargon ("Ratings join Revise").
6. **The same parts as the feed:** top bar, ticks, card face, option rows, the line you needed, the end form, the stop sheet.

### 3.2 The chapter page

#### 3.2.1 The head
- **Back link:** chevron-left 18 px plus the subject's name, `Accountancy`; 44 px target; 600 14px; ink-2; it goes where it goes
  today (`links.home(subject)`). This names the place once (F26).
- **Eyebrow:** the unit's name only when it does not repeat the title's start (Admission: "Reconstitution of a Partnership firm");
  otherwise none. 13px/1.3 600 text-3 on a phone, 14px from 600 px.
- **Title:** kc-title, `font-size: clamp(26px, 3vw, 44px)` (26 px on phones, about 31 at 1024, 41 at 1366, 43 at 1440),
  line-height 1.04, letter-spacing -0.035em, text-wrap balance, max-width 600px. Under 375 px: 25px.
- **Ref line:** `Part 1, Ch 1` (part and chapter, a comma, no dot), then the state ring and its label, gap 14px; 14px on a phone,
  15px from 600 px.
- **The chapter numeral (replaces the subject object, F11):** from 640 px only; the chapter's number from its ref (`1`, `12`);
  Gabarito 800, 112px, line-height 0.82, letter-spacing -0.05em, tabular-nums; colour `var(--a-line-strong)` (Night #384736, Day
  #bcc5b0); `aria-hidden="true"` (the ref line says it); the head is `grid-template-columns: minmax(0, 1fr) auto; column-gap: 24px`,
  the numeral top-aligned with the title (`align-self: start; margin-top: 4px`). No numeral when the chapter has no number. No subject
  object anywhere on this page. Below 640 px: nothing beside the title (the title takes the full width).
- **Spacing:** back link to the next line 6px (keep `margin-bottom: -6px` on the 44 px target); eyebrow to title 6px; title to ref
  line 10px; head to the lined-up block 28px (20px on a phone). **No hairline divider** above "How long have you got?".

#### 3.2.2 Layout per width (container queries, F4, F12, F27)
- `.lc-board { container-type: inline-size; display: grid; gap: 32px; }`
- `@container (min-width: 920px)`: `grid-template-columns: minmax(0, 1fr) 300px; column-gap: 40px;` the shelf
  `position: sticky; top: 88px; align-self: start; margin-top: 38px` (its heading lines up with the eyebrow, or with the title when
  there is no eyebrow).
  - 1440 x 900 and 1366 x 768 (board 1080 px): main 740, shelf 300.
  - 1024 with the sidebar (board about 732) and 768 to 1023 (board about 728): one column; the shelf follows the Start block,
    `max-width: 640px`.
  - Phones: one column.
- **The lined-up block:** `.lc-lined { container-type: inline-size; width: 100%; max-width: 692px; display: grid; }`
- `@container (min-width: 600px)` inside the block:
  - **Control row:** `display: grid; grid-template-columns: auto minmax(0, 1fr); align-items: center; column-gap: 20px;`, the heading
    "How long have you got?" (Gabarito 700 19px/1.25, -0.015em) on the left and the segmented control filling the rest (about 467 px
    at 692), so the control's right edge is the piles' right edge.
  - **Piles:** three: `grid-template-columns: repeat(3, 212px); column-gap: 28px` (692 px). Four: `repeat(4, minmax(0, 1fr));
    column-gap: 20px` (about 158 px each). Two: `repeat(2, 212px)`, one: `212px`, both left-aligned. Fan `aspect-ratio: 3 / 2`
    (212 x 141).
  - **Start row:** `display: grid; grid-template-columns: auto minmax(0, 1fr); align-items: center; column-gap: 20px;` the key
    (54 px tall, `min-width: 300px`) and the quiet line beside it (500 13.5px/1.45 text-2, at most 2 lines, `max-width: 360px`).
  - **Recap:** the text key on the next row, `margin-top: 4px`.
  - Vertical: control row to piles 16px; fan to its label 8px; labels to the Start row 20px.
- `@media (min-width: 1024px) and (max-height: 700px)`: fan `aspect-ratio: 16 / 9` (212 x 119); head to block 20px.
- **Check (worked out from today's 25 px page top and these values):** at 1366 x 650 with the sidebar (the max-height rule applies),
  Pro, three piles, an eyebrow and the first-visit coach line, the Start key's bottom lands at about 612 px; without the eyebrow and
  the coach line at about 563. Today it is at about 752.

#### 3.2.3 Phone values (block narrower than 600 px; F5)
- Side padding 16px (unchanged). Back link 44 px. Eyebrow 13px. Title 26px (25 under 375 px). Ref line 14px.
- Head to block 20px. Heading 17px/1.25 700; heading to control 10px; control 48 px tall (unchanged).
- Piles: three columns, gap 12px; four piles 2 x 2 (unchanged), gap 16px 14px; fan `aspect-ratio: 4 / 3`. Label 650 14px/1.25;
  minutes 500 12.5px/1.3 text-3 on one line, never cut (the "of 3" moves onto the paper, 3.2.4).
- First-visit coach line: 500 13.5px/1.4 text-2, 8px under the labels.
- Start key: full width, 52 px, 16px under the labels (or the coach line). The quiet line under it (13.5px text-2, 8px), then the
  recap text key.
- **Check (worked out):** at 360 x 780 in the worst case (a three-line title, an eyebrow and the first-visit coach line) the key's
  bottom lands at about 640 px with the dock's top at about 705, so about 65 px clear; Basic Concepts on a return visit about 591; at
  390 x 844 the dock sits 64 px lower. Today the key's top is at 667.

#### 3.2.4 The piles, every state
The paper, the hint, the tick, the counts and the timing stay as they are (section 1, item 3). Changes:

| State | Paper | On the paper | Label | Line under | Behaviour |
|---|---|---|---|---|---|
| In | as today | the count | Key cards | about 4 min | button, `aria-pressed="true"` |
| In, fewer than open (mistakes) | as today | `2` then `of 3` (600 14px text-3, baseline, 4 px gap) | Your mistakes | about 2 min | as In (F25) |
| Left out | opacity 0.4 | Left out | Questions | Tap to put back | toggles back |
| Held (Free, Key cards only today) | opacity 0.4; top paper border 1.5px dashed `--lc-edge-hi` | Tomorrow | Questions | Back tomorrow | not a button: `aria-disabled="true"`, `aria-describedby` the quiet line; no shake (F15) |
| Last one in, tapped | as In | the count | | | shake 4 px (300 ms) and the quiet line reads "Keep at least one pile in." for 2.4 s (`aria-live="polite"`) |
| Add the next chapter (short chapter) | dashed paper, plus 22px | (the plus) | Add the next chapter | Ch 3, fills your 10 min | button `aria-pressed="false"`, `aria-label` with the full title; tap = dry run with `addNext: true` (F14) |
| Next chapter added | solid paper, tick in | `+3` with `min` (14px) | Ch 3 added | Tap to remove | button `aria-pressed="true"`; tap = dry run without it; Start passes `addNext: true` |
| Refreshing | count at 0.72 (unchanged) | | | | `aria-busy` |
| Loading | the skeleton (unchanged) | | | | none |

- **The length control never rewrites a choice (F13, reverses CRITIQUE-1 C3).** The selected segment keeps what was chosen (`10 min`,
  `20 min`, `35 min`). The real length shows on the key (`Start 9 minutes`) and the reason in the quiet line (3.2.5).
- **"+3":** the added minutes are the dry run's `realMinutes` with the next chapter minus the one without it.
- **Resume (F20).** When the dry run says today's run of this chapter is unfinished (`resume`, a new field, 3.9), a resume row comes
  first, 20px under the head: "You stopped at 6 of 21 today." (650 15px ink) and "About 5 min left." (500 13.5px text-2) on the left,
  the volt `Pick up where you stopped` on the right (min-width 260px; full width under the text on a phone), then a hairline and the
  lined-up block as usual. In that state the Start key is a line key (`kc-btn--line`) reading `Start a new 10 minutes` and sends
  `fresh: true`; one volt on the page.

#### 3.2.5 Under the key: one quiet line, by priority (F9, F31)
1. **Free, Key cards only today:** "Your free Learn session today is used, so this one is Key cards only. Questions come back
   tomorrow." (the server's `free.text`).
2. **Free, chose more than 10:** "Free sessions are up to 10 minutes. Pro has any length." (`capped.text`).
3. **Short:** the server's shrink line by reason (BUILD 1.5): "This chapter has about 7 minutes of new things today."
4. **One kind only:** no questions: "Only Key cards here for now. This chapter's questions are still being checked."; no cards:
   "Only questions here for now. This chapter's Key cards are not ready yet."
5. **First visit to this chapter:** "Cards and questions, one at a time. Stop whenever you like; what you do is saved."
6. **Otherwise:** nothing (the line takes no space).

`Ratings join Revise. Questions are free.` and `Ratings join Revise, so cards come back when they are due.` go (compose.js `NOTE`,
`NOTE_FIRST`; U4 stops reading `data.note`).

#### 3.2.6 The shelf: "Everything in this chapter" (F17, F18)
- Heading `Everything in this chapter`, Gabarito 700 17px/1.3, 6px under. The words "everything" and the piles' "Start 10 minutes"
  now say which list is the run and which is the chapter.
- Link rows as today (64 px minimum, hairlines, a chevron icon at the end), only rows that lead somewhere:

| Row | Line (500 13.5px text-2) | Opens |
|---|---|---|
| Key cards | Pro: `All 46, 12 in Revise` (or `All 46, by section` when none in Revise); Free: `46 cards, Free opens 5` | the cards view |
| Questions only | `10 questions in this chapter` | a run of questions only (as today) |
| Your mistakes | `3 open. Fix them in about 3 min` | a run of the mistakes only (as today) |
| {Lesson title} | `7-minute lesson, not read yet` or `7-minute lesson, read` | the lesson |
| Print sheet | `12 Must-know lines, with your name`; Free: lock 13px and `Part of Pro` | the Must-know cards |

- What is missing collapses into one quiet line after the rows (500 13px/1.45 text-3, 10px above): "No lesson yet. No open
  mistakes." or "Questions are still being checked. No lesson yet."
- Free's taste lives here only (`Free opens 5`); the Key cards pile shows its minutes, not "5 open on Free" (LK15: the limit line
  only at the limit; T003).

### 3.3 The run player

#### 3.3.1 The frame per width (B1, with values; F1, F2)

| Width | Columns | Top bar | The item | Action bar |
|---|---|---|---|---|
| under 768 (360 to 430 phones) | one, side padding 16px | 88 px: row 1 44 px, row 2 20 px | **a card fills the space** between the bars: `height: calc(100dvh - 88px - var(--lr-bar-h) - 12px)`, at least 300 px; a question starts 12px under the top bar | sticky at the bottom, about 100 px with the safe area |
| 768 to 1199 (tablets, 1024 laptops) | one, 600 px, centred | 88 px, the same two rows; Close shows its word | card `min-height: clamp(340px, 50vh, 480px)`, grows with its content | in flow, 16px under the item |
| 1200 and up (1366, 1440) | **session panel 240, stage 640, side column 72, gaps 40** (a 1032 px group, centred) | 64 px: Close over the panel, the ticks over the stage | card `min-height: clamp(360px, 52vh, 520px)`, grows with its content up to `calc(100vh - 206px)` | in flow, 16px under the card, in the stage column |

- **Vertical.** From 768 px, the row (panel, stage, side column) is centred in the space under the top bar, at least 24px from it and
  from the window's foot; the panel and the card share their top edge (`align-items: start` inside the row). On a phone the item is
  anchored 12px under the top bar.
- **Overflow.** An item taller than its space scrolls inside its own box (`overflow-y: auto; overscroll-behavior: contain`); the keys
  never leave the screen.
- **What this buys (worked out):** at 1440 x 900 the group is 1032 px wide, 72 % of the window (today the card is 640 px, 44 %); the
  card and its keys fill about 67 % of the height under the top bar (today about 45 %), with about 136 px above and below and the panel
  filling the left with real numbers; at 1366 x 650 the card is 360 px and the band about 65 px; at 390 x 844 the card is about 644 px
  tall and ends 12px above the action bar (no dead band). If the owner still reads 136 px as empty, raise the desktop minimum to
  `clamp(360px, 56vh, 540px)` (band about 118 px at 900), not the column width.

#### 3.3.2 The top bar (F21, F24)
- **Phone and tablet, row 1 (44 px):** Close (phone: an X of 22px in a 44 px target, `aria-label="Close"`; tablet: X and `Close`,
  650 15px), the chapter title (600 13px text-2, one line, ellipsis, flex 1), the Revise count (a 20 x 24 stacked-card glyph and the
  count, 700 13px; the count hidden at 0 while the glyph stays as the flight target; `aria-label="In Revise 2"`), the position `3 of 21`
  (14px; `3` 700 ink, `of 21` text-3).
- **Row 2 (20 px):** the ticks (flex 1) and `about 9 min left` (500 12.5px text-3, tabular, `min-width: 10ch`, right).
- **Desktop (64 px):** Close (X and `Close`, 44 px target) at the left edge of the panel column; the ticks across the stage column,
  centred in the bar's height. Nothing else (the panel holds the rest).
- **Ticks (the feed's, shared):** one per item, 3 px tall, 3 px gaps, radius 2; done `var(--a-ink-2)`, later `var(--a-line)`, the
  current one fills `var(--a-select)` from the left in 320 ms. No grouping by kind. Over 40 items: one 3 px bar, done in ink-2, with a
  4 px volt mark at the current position.

#### 3.3.3 The session panel (1200 px and up)
Text on the page, no boxes, hairlines between groups, 240 px wide:
1. **The chapter:** its title in Gabarito 700 20px/1.2, -0.015em, ink, wrapping (never cut); `Part 1, Ch 1` in 13px text-3 under it;
   20px below.
2. **Where you are:** `3` in Gabarito 700 28px tabular ink with ` of 21` in 15px text-3; `About 7 min left` 13.5px text-2; `Up next:
   2 cards, then a question` 13px text-3 (wraps to 2 lines at most); 20px below, then a hairline.
3. **The piles you chose, worked down:** one row per pile in this run (Key cards, Questions, Your mistakes, Lesson), 36 px tall: a
   26 x 20 mini fan (two under-papers at -4 and 3 degrees, the top paper with the same hint as on the chapter page, the mistakes paper
   with its red margin), the label (600 14px text-2) and `3 of 12` (14px tabular, right). The row of the item on screen: label in ink
   700 and `aria-current="step"`. A hairline after.
4. **Revise:** the pile glyph at 40 x 48 (today's three stacked cards at 1.35 times), `In Revise` (13px text-2) and the count
   (Gabarito 800 24px ink). The stamp (`Back Wed`, 700 13px text-2) shows under it for 900 ms after a rating. The flight lands here.
5. **After the first answer:** `Right so far: 2 of 3` (13.5px text-2); from 3 right in a row, `4 in a row` (13px, the number in
   accent text).
6. **`Stop here`:** a text key (44 px target, 650 14.5px, underline in line-strong) that opens the stop sheet (3.3.10).

A recap (kind recap) shows groups 1 and 2 only, with `12 Must-know lines` instead of the piles. A cards run (Study these) shows the Key
cards row only.

#### 3.3.4 The side column (1200 px and up, 72 px)
- **A question:** `Save`, a 48 px round key (1px line, raised surface), bookmark 22px, the label `Save` (600 12px text-2) 4px under
  it; saved: the glyph fills volt with a 1.15 pop (180 ms), label `Saved`; Free's save limit (402): label `Pro`, the tap opens the
  upgrade sheet (as the feed does).
- **A card or a lesson:** empty. The card's "..." menu (Report this card) stays on the card.
- Top-aligned with the card.

#### 3.3.5 The action bar
- **Phone:** `position: sticky; bottom: 0; padding: 10px 16px max(12px, env(safe-area-inset-bottom)); background: var(--a-bg)` with
  the 16px fade above (keep); the keys (52 px), then 6px, then the status line (20 px, always reserved).
- **From 768 px:** in flow, 16px under the item; keys centred: one key 360 px wide, two keys 420, the three rating keys 520; the
  status line under them (20 px reserved).

| The item, its state | Keys | The volt |
|---|---|---|
| Card, front | `Show answer` [Space] | Show answer |
| Card, turned | `Missed` [1], `Got it` [2], `Easy` [3] | Got it |
| Card, turned, past Free's ratings (a look) | `Next` [Enter] | Next |
| Question, not answered | none: the options are the action | none |
| Question, sending | none; the picked row shows the spinner | none |
| Question, answered | under 1200 px: the `Save` icon key (48 x 56, label under) then `Next` [Enter]; from 1200 `Next` only (Save is in the side column) | Next |
| The last item, done | `See how it went` [Enter] | it |
| Lesson | `Skip it` (line, one third) and `Read the lesson` [Enter] (two thirds) | Read the lesson |
| Recap card | `Previous` (line) and `Next`, or `Finish` on the last | Next |

The status line shows one thing at a time: the stamp (900 ms), a first-run coach line, Free's look line (once per run), an error
("That rating was not saved. Try again." in bad text), or a skip note (3.3.11). It is `min-height: 20px`, 500 13.5px/1.45, centred;
a first-run coach line or Free's line may take two lines on a 360 px phone (once per student or per run), never more. Keyboard chips
(`kc-kbd`) show only on fine pointers.

#### 3.3.6 The card face and the question (shared with the feed; F6, F7, F8, F28, F29)

**The card face**
- Box: radius 24px; border 1px `var(--a-line-strong)`; background `var(--kc-surface)`; shadow `var(--a-shadow-1)`, turned
  `var(--a-shadow-2)`; padding 20px 20px 18px (phone), 26px 28px 22px (tablet), 32px 36px 28px (desktop).
- Layout: `display: grid; grid-template-rows: auto 1fr auto` (head, body, foot).
- **Head** (28 px minimum): the kind (600 13px text-3, `Definition`) and `Must-know` (accent text, no box) when it is; on the right
  the stage tag (12.5px text-3: `Due today`, `Back from earlier`, `The line you needed`), then the "..." menu (44 px target).
- **Body, the front:** Gabarito 650; size by the front's length: up to 60 characters 34px phone, 40 tablet, 44 desktop; 61 to 120:
  28, 32, 36; longer: 22, 26, 28 (B1). Line-height 1.12; letter-spacing -0.02em (-0.025em from 36px); text-wrap balance;
  `max-width: 22ch`; left-aligned; vertically centred in the body with `padding-bottom: 8%` so it sits a little above the middle.
  Blanks keep their underline (`kc-gap`).
- **Foot (front only):** the source, 500 12.5px/1.4 text-3 with a 14px book icon: `NCERT, Accountancy Part 1, Ch 1, p. 1` (where the
  answer will come from, B1).
- **The first-card coach** goes to the status line, not into the card: "Say the answer in your head, then show it."
- **Turning:** the 3D flip of B1 (380 ms). Both faces take the measured taller face's height (on a phone the card already fills the
  stage).
- **The back:** the same head; the prompt small (600 13.5px/1.4 text-3, wraps in full); 12px; a 1px hairline `var(--a-line)`; 14px;
  NCERT's words in Literata at 20px/1.55 desktop, 19px tablet, 18px/1.6 phone, `max-width: 60ch`; 8px; the source (12.5px text-3);
  10px; `In short` (14px/1.55 text-2). A long back scrolls inside the face.

**The question (on the page, no card face)**
- **Head:** `Question`, or the mistake label with a 14px `History` icon: `You missed this in Mock 3 on 16 Oct`; 600 13px text-2 in
  the run and the feed alike (F29).
- **Stem:** Hanken Grotesk 650, 21px/1.42 phone, 22px/1.42 from 768; over 200 characters 500 17px/1.58; steps as a list (keep
  `stemParts` and its rule).
- **Options (one component for the run and the feed):** min-height 58 px phone, 56 from 768; padding 11px 14px; radius 16px; border 1px
  line-strong; raised background; gap 10px; the letter chip 30 x 30, radius 9px, `var(--a-letter)`; text 550 16px/1.4; a 20 px mark
  column.
- **Option states:**

| State | Look |
|---|---|
| Picked, sending | border ink-3; a 16px spinner in the mark column |
| Right (the pick) | background #d2f000, border #d2f000, ink #10140e; chip `rgb(16 20 14 / 0.12)`; a check |
| Key (the pick was wrong) | border `var(--a-select)` plus an inset 1px of it; a check in accent text |
| Wrong (the pick) | border bad-text; background bad-wash; an X in bad-text |
| The rest | opacity 0.4 |

- **The verdict** (visible, `role="status"`): right: `Right.` and the explanation's first sentence (500 15px text-2); wrong: `Not
  quite. The answer is C.` (650 16px); a mistake retried right: `Right this time. Back on Wed to check it held.` with the check that
  draws and Mobi's nod; when Revise retires it, `Fixed. You missed this in Mock 3 on 16 Oct.` (BUILD 1.8).
- **Wrong, the line you needed (in place, under the verdict):** a panel, radius 16px, `var(--a-sunken)`, padding 14px 16px 16px; title
  `The line you needed` (Gabarito 700 15px) with the card's kind (12.5px text-3); NCERT's words at 17px/1.6 with the key words
  underlined (`kc-mark`); the source (12.5px text-3); when its card comes back, a foot line above a hairline: `You'll see this card
  again later in this run.` (13.5px text-2). Under the panel, `Why C` (a text key, 44 px target, 650 14px, underlined) opens the
  explanation in place (15px/1.6 text-2): progressive disclosure for the secondary text, while the frequent action (Next) stays in
  view (S014). With no line card, the explanation shows open (3 lines and More).
- **Right:** `See the line` (as today) opens the same panel.
- **Coach:** "Tap the answer you think is right." in the status line on the first question of a student's first run only (F28).
- **Free's locked line (A5 R14):** the panel shows its text and a `See Pro` text key, as the feed does.

#### 3.3.7 The flight and the Revise pile
- Keep A4's motion and timings (3.5). The target is the session panel's glyph from 1200 px, the top bar's glyph below it (on a phone
  the arc goes up and to the right, a short trip).
- The first card in: the count appears 0 to 1 with the 1.12 pop.

#### 3.3.8 Free inside a run (F23)
- **A look card** (past today's 10 ratings or 5 new cards): after `Show answer` the bar shows `Next` [Enter] (volt) instead of the
  three keys. The status line says it **once per run**: "You've used today's 10 free card ratings. The rest show their answers but
  won't be added to Revise." or "You've used today's 5 new free cards. The rest show their answers but won't be added to Revise."
- **A second tab's answer after the day is used (402):** the run ends calmly on the end screen with the Free block (3.4.4).

#### 3.3.9 The lesson item (F10)
- On the card face: the kind `Lesson, 7 min`; the lesson's title at the front's size; under it 500 15px/1.5 text-2: "Read this first.
  Its cards come next in this run."
- Keys: `Skip it` (line) and `Read the lesson` (volt).
- `Read the lesson` opens the lesson with a way back: `links.lesson(id, { back: <this run's href with run=<id>> })`; the lesson page
  shows `Back to your run` in its top bar and as a volt key at its end. Coming back resumes the run (`GET /api/learn/runs/:id`) at the
  next item; the lesson counts as done. In the preview `links.lesson()` must keep the run (today it goes to Learn home).
- `Skip it` logs a look and goes on.

#### 3.3.10 Stopping and closing (F19)
- **Close with nothing done:** leave at once to the chapter page.
- **Close, or `Stop here`, after at least one item:** a small sheet. Phone: a bottom sheet, radius 22px 22px 0 0, `var(--a-sheet)`,
  padding 16px plus the safe area. From 768 px: a 400 px dialog in the middle. Title `Stop for now?` (Gabarito 700 17px); line `7 of 21
  done. Everything you did is saved.` (500 14.5px text-2); keys, full width, 10px apart: `See how it went` (volt; the end screen for
  what was done), `Keep going` (line), `Leave, pick it up later today` (text key; the chapter page; BUILD 1.3 resumes it). Escape and
  a tap outside mean Keep going. Focus is trapped and returns to the opener. No guilt copy (T005).

#### 3.3.11 Recap, rounds, loading, errors
- **Recap:** the card shows its back at once (answers showing, no flip, no stage tag); keys `Previous` and `Next`; the status line
  once: "Answers are showing. Nothing is scheduled."; swipe and arrows as today.
- **Recap end:** `That was all 12 Must-know lines.`, `Nothing was scheduled.`, `Study these 12` (volt), `Quick recap again` (line),
  `Back to the chapter` (text).
- **Round (a cards run, every 20):** in the stage, `20` (Gabarito 800 56px tabular) and `cards rated` (15px text-2), then `12 more
  are lined up.` (15px text-2); keys `Next round` (volt) and `Finish here` (line).
- **Loading:** the skeleton at its final shape: the top bar with tick placeholders, a card at its min-height and radius 24px, the key;
  on desktop three panel lines. No spinner.
- **Start failed and nothing lined up:** keep as today.
- **409 question changed or held:** skip the item; the status line for 3 s: "This question was updated, so it was skipped." or "This
  question is in a paper that is still open, so it was skipped."
- **409 run ended or expired:** go to its end screen.

#### 3.3.12 Keys
Space or Enter turns a card; 1, 2, 3 rate it; A to D or 1 to 4 answer; Enter goes on after an answer, on a look card and on the
lesson (Read); the arrows move a recap; Escape closes the report form and the stop sheet. Ignored while typing.

### 3.4 The run end

#### 3.4.1 Layout
- **Phone:** one column, side padding 16px, 24px from the top, groups 24px apart.
- **768 to 1023:** one column, 600 px, centred.
- **1024 and up:** two columns inside 880 px (B2): left 488, right 344, gap 48; top padding `clamp(32px, 8vh, 72px)`; the right column
  starts level with the title.

#### 3.4.2 Left: what happened (F16)
1. **Title:** the lead line (`10 minutes on`, or `Stopped at 7 of 21 in` after a stop) 600 15px text-2; the chapter's name Gabarito
   750 `clamp(28px, 3vw, 38px)`/1.08, -0.03em; Mobi to the title's right, 72 px phone, 84 desktop, his one reaction (keep endAct).
2. **The state change** (Pro, when it moved): the 24 px ring, `Holding` (Gabarito 700 17px, good text) and `was Getting there`
   (13.5px text-3); `aria-label="This chapter moved from Getting there to Holding."`; the ring fills from half to whole in 500 ms (the
   screen's one authored moment); 12px under the title.
3. **The Revise pile, with real faces** (the feed end's kept pile): up to 4 cards this run sent to Revise, fanned (rotate `(i - mid) x
   7deg`, x `(i - mid) x 26px`); cards 104 x 132 desktop, 96 x 122 phone; the top card shows its kind (10.5px) and its front
   (Gabarito 650 12.5px/1.28, 5 lines at most), the others three hairlines. Under it `16 in Revise` (700 15px ink) and `14 back Wed, 2
   back in 20 days` (14px text-2). Nothing sent: no pile, one line "No cards went to Revise this time."
4. **The lines** (the feed end's rows): the label (650 15px ink, `min-width: 112px`) and the value (500 15px text-2, tabular), rows
   44 px minimum with hairlines, only rows with something in them:
   - `Key cards` `16 rated, all got it`, or `16 rated: 12 got it, 3 easy, 1 missed`
   - `Questions` `3 of 3 right`
   - `Old mistakes` `2 of 2 fixed`, or `1 of 2 fixed, 1 still open`
5. **Free, ratings past the limit in this run:** one quiet line, 13.5px text-3: "Free opened 5 of this chapter's 46 cards."

#### 3.4.3 Right: what next
1. **The lead:** a heading that names it (Gabarito 700 17px/1.3, 2 lines at most): `Next: Profit and Loss Appropriation Account`, or
   `Another 5 minutes here`, or `Fix 2 open mistakes`; its reason under it (13.5px text-3: `The next chapter in your book.`, `1 missed
   card, 3 new cards left here`, `Admission of a Partner`); then the volt key, full column width, 54 px: `Start 10 minutes` for a run
   (the same words as the chapter page), else the action's own verb (`Revise 12 due cards`, `Take the full mock`). Visible at once
   (F22).
2. **Options** (up to 3): rows 64 px minimum, hairlines, label 650 15.5px, reason 13.5px text-3, a chevron icon (keep R6: equal, no
   fill).
3. `Back to the chapter` (a text key, 44 px).

#### 3.4.4 Free after the day's session (F3)
- At the top of the right column: `Your free Learn session for today is done.` (650 15.5px ink); `Explore questions stay free. Pro has
  as many as you like.` (14px text-2); `See Pro`, a text key (44 px target, 650 14.5px, underlined) that opens the upgrade sheet. No
  volt See Pro, no modal on load.
- The volt goes to the first option the server sends (Revise N due cards, else the quick recap, else questions on this chapter in
  Explore), drawn as the lead (heading, reason, key); the rest as rows.

#### 3.4.5 Stopped early
The lead line reads `Stopped at 7 of 21 in`; the lines count what was done; the options as usual.

### 3.5 Motion
`ease-out` here is `cubic-bezier(0.22, 1, 0.36, 1)`; `flight` is `cubic-bezier(0.32, 0.72, 0, 1)`. Only transform and opacity move,
except the line panel's height (B1). No ease-in, nothing from scale 0, no `transition: all`.

| Moment | What moves | Time | Curve | Reduced motion |
|---|---|---|---|---|
| Chapter: a length tap | the thumb slides | 240 ms | ease-out | at once |
| Chapter: counts change | the numbers roll | 180 ms | out | at once |
| Chapter: the fan | the under-papers re-spread | 220 ms | ease-out | none |
| Chapter: pile hover (hover: hover only) | lift 3 px, hairline brightens | 150 ms | ease-out | none |
| Chapter: pile press | scale 0.98 | 100 ms | ease-out | none |
| Chapter: leave out, put back | opacity 1 to 0.4 and back | 220 ms | ease-out | at once |
| Chapter: last pile | shake 4 px | 300 ms | as today | none; the line says it |
| Chapter: add the next chapter | dashed to solid, plus to tick | 150 ms | ease-out | at once |
| Chapter: page load | piles rise 8 px, 40 ms apart (the page's one load moment) | 260 ms | ease-out | none |
| Your own sheet, phone | rises 24 px with opacity | 280 ms | flight | 120 ms fade |
| Your own popover, wide | scale 0.96 to 1 with opacity, from the top right | 180 ms | ease-out | 120 ms fade |
| Run: it opens | the layer fades in; the first item rises 8 px, 60 ms later | 160 ms, 240 ms | ease-out | 120 ms fade |
| Run: Show answer | the card turns (rotateY 0 to 180); `navigator.vibrate(8)` where supported | 380 ms | flight | 120 ms cross-fade |
| Run: the keys change | old keys fade (100 ms); new keys rise 6 px, 40 ms apart | 180 ms | ease-out | at once |
| Run: Got it, Easy | A4: lift 4 px and 0.96 (100 ms), then an arc into the pile to 0.18 and out (320 ms; Easy 280) | 420 ms, 380 ms | flight | the card fades in 120 ms |
| Run: Missed | tilts -3 degrees, drops 64 px, fades | 260 ms | flight | 120 ms fade |
| Run: the next item | rises 8 px, starting at 220 ms | 240 ms | ease-out | 120 ms fade |
| Run: the Revise count | 1 to 1.12 to 1 when the card lands | 180 ms | ease-out | none |
| Run: the stamp | in 120 ms, holds, out 200 ms | 900 ms | ease-out | plain text for 1.5 s |
| Run: ticks | the current one fills; a done one changes colour | 320 ms, 200 ms | ease-out | at once |
| Run: waiting for a grade | the spinner, only while waiting | 900 ms a turn | linear | a still icon |
| Run: right | the row fills volt and settles from 1.04; `vibrate(12)` | 200 ms | ease-out | colour only |
| Run: wrong | the row shakes 4 px twice; `vibrate([8, 40, 8])` | 240 ms | linear | colour only |
| Run: the other rows | fade to 0.4 | 160 ms | ease-out | at once |
| Run: the verdict | rises 8 px | 200 ms | ease-out | at once |
| Run: the line opens | rows 0fr to 1fr with opacity; NCERT's words rise 8 px 40 ms later | 240 ms, 200 ms | ease-out | at once |
| Run: a retried mistake right | the check draws (120 ms late); Mobi nods | 200 ms, 900 ms | ease-out | still |
| Run: the stop sheet | as the Your own sheet | | | |
| End: the title | rises 8 px | 240 ms | ease-out | at once |
| End: the state change | the ring fills, `Holding` fades in, at 200 ms | 500 ms | ease-out | at once |
| End: the pile | the cards fan open, 40 ms apart, at 300 ms | 320 ms | flight | at once |
| End: the keys | do not animate (visible at once) | | | |

Optional, only after checking `node_modules/next/dist/docs/` for view transitions in this Next version: the three chapter piles morph
into the session panel's piles when the run opens (shared names `lc-pile-cards`, `lc-pile-questions`, `lc-pile-mistakes`, 320 ms,
flight). Without support, nothing.

### 3.6 Copy (old, new, who owns the string)

| Where | Old | New | Owner |
|---|---|---|---|
| Chapter, under the key | Ratings join Revise. Questions are free. | (gone) | S1 compose.js `NOTE`, U4 |
| Chapter, first visit | Ratings join Revise, so cards come back when they are due. | Cards and questions, one at a time. Stop whenever you like; what you do is saved. | S1 `NOTE_FIRST`, U4 |
| Chapter, back link | Learn | Accountancy | U4 |
| Chapter, eyebrow and ref | Accountancy, Part 1 / Ch 1 | (no eyebrow) / Part 1, Ch 1 | U4 |
| Pile, mistakes | 2 of 3, about 2 min | `2 of 3` on the paper; about 2 min | U4 |
| Pile, next chapter | Next chapter / Profit and Loss Approp... | Add the next chapter / Ch 3, fills your 10 min; then Ch 3 added / Tap to remove | U4 |
| Pile, Free held | Left out / Tap to put back | Tomorrow / Back tomorrow | U4 |
| Pile, the last one | (a shake only) | Keep at least one pile in. | U4 |
| Shelf heading | In this chapter | Everything in this chapter | U4 |
| Shelf, questions | Questions / 10 questions, all tied to these cards | Questions only / 10 questions in this chapter | U4 |
| Shelf, mistakes | 3 open. Fix them with their lines. | 3 open. Fix them in about 3 min | U4 |
| Shelf, lesson | 7-minute lesson, not read yet. Read it alone | 7-minute lesson, not read yet | U4 |
| Shelf, empty rows | No lesson for this chapter yet / None open in this chapter | No lesson yet. No open mistakes. (one line) | U4 |
| Chapter, resume (new) | | You stopped at 6 of 21 today. / About 5 min left. / Pick up where you stopped / Start a new 10 minutes | U4 |
| Run, lesson | Read it first; its cards follow in this run. / Open the lesson / Next | Read this first. Its cards come next in this run. / Read the lesson / Skip it | U4 |
| Run, every question | Tap the answer you think is right. | (once, first question of the first run) | U4 |
| Run, the last item | Next / Finish | See how it went | U4 |
| Run, first wrong answer | Here is the NCERT line you needed. | (gone; the panel's title says it) | U4 |
| Run, the line's foot | This card comes back later in this run. | You'll see this card again later in this run. | U4 |
| Run, Free looks | Today's 10 free card ratings are used. The rest of your cards show without ratings. | You've used today's 10 free card ratings. The rest show their answers but won't be added to Revise. (once a run) | S2a `LOOKS_TEXT` |
| Run, Free looks (new cards) | Today's 5 new free cards are used. The rest of your cards show without ratings. | You've used today's 5 new free cards. The rest show their answers but won't be added to Revise. | S2a `LOOKS_TEXT` |
| Run, stop (new) | | Stop for now? / 7 of 21 done. Everything you did is saved. / See how it went / Keep going / Leave, pick it up later today | U4 |
| Run, skips (new) | | This question was updated, so it was skipped. / This question is in a paper that is still open, so it was skipped. | U4 |
| End, moved | {chapter} moved from Getting there to Holding. | Holding / was Getting there (aria: This chapter moved from Getting there to Holding.) | U4 |
| End, Revise | 16 cards joined Revise / 14 back on Wed | 16 in Revise / 14 back Wed, 2 back in 20 days | U4; S1 `stamps.js` label |
| End, numbers | 16 cards rated, 16 got it (and two more) | Key cards: 16 rated, all got it / Questions: 3 of 3 right / Old mistakes: 2 of 2 fixed | U4 |
| End, lead | Next: Profit and Loss Appropriation Account, 10 minutes (in the key) | Next: Profit and Loss Appropriation Account (heading) / Start 10 minutes (key) | U4, S2a fields |
| End, option reason | 3 new ones | 3 new cards left here | S1 `suggest.js` |
| End, Free | See Pro (volt, alone) | Your free Learn session for today is done. / Explore questions stay free. Pro has as many as you like. / See Pro (text key) | U4 |
| Recap end | That was every Must-know card. / 12 cards, nothing scheduled. | That was all 12 Must-know lines. / Nothing was scheduled. | U4 |
| Round | Round 1 done / 20 cards rated. 12 more are lined up. | 20 / cards rated / 12 more are lined up. | U4 |

Every string: sentence case, no middle dots, no exclamation marks, no arrows in the text, no "mastered", no percentages of mastery.

### 3.7 Night and Day

| Element | Night | Day |
|---|---|---|
| Page | `--a-bg` #0b100e | #f4f5f0 |
| Card face | `--kc-surface` over #131a16 (cool light rgb(118 168 255 / 0.13) and grain, inside the card only) | over #ffffff, cool light rgb(70 120 220 / 0.09) |
| Card border, shadow | `--a-line-strong` #384736; `--a-shadow-1`, turned `--a-shadow-2` | #bcc5b0; the Day shadows |
| The volt key | #d2f000, ink #10140e, a 3 px #8ba000 lip | the same |
| Volt as text (Must-know, the streak number) | `--a-accent-text` #d2f000 | #4f6400 |
| A right pick | fill #d2f000, ink #10140e | the same |
| The key after a wrong pick | `--a-select` #d2f000 outline | #6f8700 |
| A wrong pick | wash rgba(255, 122, 107, 0.1), border and X #ff9d92 | rgba(176, 41, 31, 0.08), #b0291f |
| The line panel | `--a-sunken` #0f1512 | #eef0e8 |
| Text roles | ink #f2f4ec, ink-2 #bcc5b9, ink-3 #93a08f | #172016, #3d4a39, #56624f |
| The chapter numeral | `--a-line-strong` #384736 | #bcc5b0 |
| Holding | `--a-good-text` #b6e36e | #3d6600 |
| Sheets | `--a-sheet` #0e1411 | #eef0e8 |
| Ticks | done ink-2, later `--a-line`, current `--a-select` | the same roles |

Night stays subtle: no glow, no gradient wash on the page, no blur on content.

### 3.8 Accessibility (WCAG 2.2 AA, S016)
- **Chapter:** the length radiogroup as today; piles are buttons with `aria-pressed` and full labels ("Key cards: 16, about 4 min.
  Tap to leave it out"); held piles `aria-disabled="true"` with the quiet line as their description; the add pile has the full next
  chapter title in its label; the numeral is hidden from screen readers; the resume row's key says what it resumes.
- **Run:** focus moves to the new item's heading on every advance (keep); a polite live region says `Card 3 of 21` or `Question 4 of
  21`; the turned card hides its front from screen readers and the other way round (as the feed); the rating keys stay a group named
  "How well did you recall it?"; the options a group named "Choose one answer"; the verdict and the status line are polite live
  regions; the stop sheet is a dialog with a focus trap and returns focus to Close or Stop here.
- **Targets:** 44 px everywhere, 52 px for the action keys, 48 px for icon keys.
- **Contrast:** text-3 on the page and on the card face is above 4.5:1 in both themes; the numeral is decorative (its information is
  in the ref line).
- **Zoom:** at 200 % a 1440 window is 720 CSS px, so the phone layout applies; nothing is cut.

### 3.9 Data and other packets (additive fields only)
- **POST /api/learn/runs/preview (S2a):** `shrink.addNext.ref` (`'Ch 3'`); `piles[].held: 'free' | null`; `resume: null | { runId,
  done, of, minutesLeft }`; `firstVisit: boolean` (the client stops reading `note`).
- **GET /api/learn/runs/:id/end (S2a):** `reviseCards: [{ id, kind, front, mustKnow }]` (at most 4, the run's Got it and Easy cards in
  run order); `lead.title`, `lead.minutes`, `lead.kind` (`next`, `here`, `fix`, `revise`, `recap`, `mock`, `explore`).
- **Strings (S1, S2a):** `NOTE` and `NOTE_FIRST` (compose.js), `LOOKS_TEXT` (learn.js), the return-day label `back Wed` (stamps.js),
  the option reason `3 new cards left here` (suggest.js).
- **Lessons (P and the lessons owner):** `links.lesson(id, { back })` and `Back to your run` on the lesson page; the preview keeps the
  run.
- **Shared with the feed (U1):** the option row, the line panel, the card face, the ticks, the end form and the stop sheet are one
  set of parts. Build them once; the main session names their owner. Until then both packets follow the values in this section.

### 3.10 Acceptance: what to capture and measure
- **Sizes:** 1440 x 900, 1366 x 650 (the real laptop), 1024 x 650 (sidebar on), 390 x 844, 360 x 780; Night and Day at 1440 and 390.
- **Chapter states:** Pro 10 min; first visit; Free taste; Free capped (20 chosen); Free Key cards only; short with the add pile,
  then added; Goodwill (one pile); Admission at 20 (lesson pile); resume; Your own open; skeleton; error.
- **Chapter measures:** the whole Start key inside the viewport at 1366 x 650 and at least 24 px above the dock at 360 x 780 and 390
  x 844, first visit included; `document.elementFromPoint` at the key's centre returns the key; no sideways scroll at 360; CLS under
  0.01.
- **Run states:** front, turned, Got it flight frames at 0, 120, 260 and 420 ms, Missed, a look past the limit, a question sending,
  right, wrong with the line, Why C open, a retried mistake right, the lesson, a recap card, a round, the stop sheet, loading, start
  failed, a skipped question.
- **Run measures:** at 1440 x 900 the panel, stage and side column span about 1032 px and the band above the card is at most 140 px;
  at 390 x 844 the card ends within 12 px of the action bar; the keys stay on screen while a long item scrolls inside.
- **End states:** Pro with a moved chapter; nothing sent to Revise; Free first run; Free after the day's session; stopped early; a
  cards run; the recap end.
- **Every time:** real pointer clicks (CDP mouse) on every primary key; keyboard only; reduced motion; no console warnings.

---

## 4. The anti-slop test and the 0/1/2 rubric

### 4.1 The 12-part test (AGENT_RULES, the research brain)

| # | Test | Now | Proposed |
|---|---|---|---|
| 1 | Identity with the logo hidden | Partial: piles, the book face and volt keys are MockMob's; the run's centred box is generic | Pass: the piles carry from the chapter to the session panel to the end; book face; chapter numeral |
| 2 | One primary action | Partial: the lesson's volt skips the lesson; Free's end makes See Pro the volt | Pass: one volt per viewport, always the step itself |
| 3 | True content | Partial: "Questions are free" on a chapter with none; a "9 min" segment the student never chose; the Free line dropped | Pass: every line real and said where it applies |
| 4 | Hierarchy at first scan | Partial: a 23 px prompt in a big box; the wrong answer's wall | Pass: the front at 34 to 44 px; the line before the explanation |
| 5 | Intentional composition | Fail on the run's desktop; partial on the chapter page (three widths) | Pass: 240 / 640 / 72 frame; shared edges on the chapter page |
| 6 | Typography by role | Partial: the same prompt size at 360 and 1440 | Pass: front sizes by length and width; stem in the reading face |
| 7 | Every state | Partial: no Free held piles, no resume, no stop, the lesson has no way back | Pass: section 3.2.4, 3.3.8 to 3.3.11, 3.4.4 and 3.4.5 |
| 8 | Accessible interaction | Partial: the Start key under the dock at 360; below the fold at 1366 x 650 | Pass after the measures in 3.10 |
| 9 | No pseudo-evidence | Pass: counts, stamps and grades are the server's | Pass |
| 10 | Motion with a reason | Partial: the end's lead waits 480 ms; Show answer only fades | Pass: every move answers an action (3.5) |
| 11 | One leading metric and one guardrail | Fail: nothing instrumented | Pass when A12 is wired: leading, the share of started runs that reach their end screen; guardrail, runs over 125 % of the chosen time; second guardrail, closes within the first two items |
| 12 | What would be better without this? | Partial: "In Revise 0", the hint line, dead shelf rows, the subject object | Pass: each removed or moved to where it carries information |

### 4.2 The slop list (standards section 10), now
- **1 floating UI over a control:** yes (the dock over the Start key at 360 x 780).
- **3 identical tiles:** partly (the end's three hero figures; the piles read as stat tiles at a glance, CRITIQUE-1 C1).
- **4 jargon:** yes ("Ratings join Revise", "tied to these cards", "their lines", "Read it alone").
- **5 dead states:** partly (three empty shelf rows on Goodwill; "In Revise 0").
- **15 hero-metric template:** yes (the end).
- **16 clean but generic:** partly (the run's centred box).
- Not present: decorative gradients on the page, glow, glass on content, `transition: all`, ease-in, scale(0), pure black,
  monospace labels, emoji, arrows in button text, all-caps eyebrows, fake truth, hover-only controls, an invisible overlay (no
  hit-test failures in index.md).

### 4.3 The 0/1/2 rubric (0 missing, 1 partial, 2 validated)
Proposed scores are targets: they count as 2 only after the checks in 3.10 pass on a real browser.

| Dimension | Chapter now | Chapter proposed | Run now | Run proposed | End now | End proposed |
|---|---|---|---|---|---|---|
| Task fit | 2 (his LK10 flow, "quite good") | 2 | 2 | 2 | 2 | 2 |
| Information architecture | 1 (piles and shelf say the same names; a pile that is a link) | 2 | 1 (three unrelated corners; title hidden on a phone) | 2 | 1 (numbers twice) | 2 |
| Content truth | 1 (the note; the rewritten segment) | 2 | 2 | 2 | 1 (the Free line dropped) | 2 |
| Readable hierarchy | 2 | 2 | 1 (small prompt; the wrong-answer wall) | 2 | 2 | 2 |
| Visual specificity | 1 (one object for every chapter) | 2 | 1 (a generic centred box) | 2 | 1 (hero figures) | 2 |
| Accessibility | 1 (the dock over the key at 360) | 2 | 2 | 2 | 2 | 2 |
| Functional states | 1 (no Free held, no resume) | 2 | 1 (lesson return, no stop) | 2 | 2 | 2 |
| Trust | 1 ("Questions are free") | 2 | 2 | 2 | 1 (a volt See Pro with no reason) | 2 |
| Intentional motion | 2 | 2 | 1 (no turn; noisy pips) | 2 | 1 (the lead waits 480 ms) | 2 |
| Performance | 1 (one React warning) | 2 | 2 | 2 | 2 | 2 |
| Responsive integrity | 1 (360, 1366 x 650, 1024) | 2 | 1 (desktop empty, phone band) | 2 | 2 | 2 |
| Instrumentation | 0 | 0 until A12 is wired (needs usage consent) | 0 | 0 | 0 | 0 |
| **Total of 24** | **14** | **22** | **16** | **22** | **17** | **22** |

---

## 5. Where this differs from BUILD-1101 Part B or earlier decisions

1. **The phone card fills the stage** (B1 says "centred" and "at least 300 px"). Its upper limit, "the space between the top bar and
   the action bar", is my value: a 300 px card centred on an 844 px screen brings back the empty bands of F2. From 768 px the card is
   centred as B1 says.
2. **The end shows lines, not "the numbers"** (B2). Three big figures with labels is the hero-metric template (slop 15) and today it
   repeats every number (F16); the feed end already uses lines and, per B3, shares B2's two-column end, so one form serves both.
3. **The chapter head shows the chapter's numeral, not the subject object** (B2 "keep its structure"). LK21's complaint (the same
   Accountancy object on every chapter) applies here too, and B1 and B4 remove the object everywhere else. This is a visible change:
   show it to the owner on the live prototype.
4. **The length segment never rewrites the choice** (reverses CRITIQUE-1 C3): a control that changes its own label reads as a bug
   (44-chapter-free-1440-night); the key and one line carry the real length.
5. **Questions do not sit on a card face** (reverses CRITIQUE-1 R2, written when the feed still had one): no box inside a box, and the
   feed v2 already shows questions on the page.
6. **The shelf heading becomes "Everything in this chapter"** (B2 keeps "In this chapter"): one word that separates the chapter from
   the run's piles (F18).
7. **A stop sheet** (new): LK9 asks for easy control, and B1's session panel already has a `Stop here` for the feed.
8. **A resume row on the chapter page** (new): BUILD 1.3 resumes silently; without the row the volt key says one thing and does
   another.

Owner-visible changes to show him first (he judges only live prototypes, LK19): the chapter numeral head, the run on a 1440 screen
(the panel, the flashcard, the turn) and on his phone, and the end with real card faces.
