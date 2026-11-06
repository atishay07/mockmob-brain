# A1. The Explore feed: audit and refined design

1 Nov 2026. Auditor: A1 (learn-1101 audit workflow). Area: `src/components/learn2/feed/ChapterFeed.jsx`, `feed.css`,
`data/learn/feed.js`, and the feed block of `GET /api/learn/runs/:id/end` (`src/lib/server/learn.js`, `feedEnd`). Widths:
desktop 1440, 1366, 1024; phone 360 to 430. Night and Day.

**What I exercised.** I read 41 feed captures one by one from `tmp/learn-1101/audit/` (with index.md and its section 2
measurements) and `tmp/learn-1031/feed2/`, plus the run and Explore captures named below for comparison, and the code. I did
not open a browser or a phone (the capture step had already run; RAM rule). Every value proposed here is a design value, not a
measured result. Section 3.18 lists what must be measured once it is built.

**Judged against.**
- The owner's words LK20 to LK23 (OWNER-FEEDBACK-2026-10-31-LEARN.md, 1 Nov 1:25 am).
- FEED-2.md, the spec this build follows.
- BUILD-1101.md Part B, the main session's decisions, written before this audit. I agree with most of it; section 3.17 lists
  the points where I propose a change and why.
- The owner's standards (ui-ux-standards.md sections 3, 7, 8, 9, 10, 11), cited as "std".
- The research brain (AGENT_RULES.md, evidence T001-T009 and S014-S018, the 12-part test, the 0/1/2 rubric), cited as
  "research".
- DESIGN.md (Night Arena tokens, keys with a lip, the drill's answer sequence) and PRODUCT.md (the phone is the product, a
  budget Android on weak 4G; desktop is the minority case but must work).

---

## 0. The answer in brief

- **Keep the direction.** One item at a time, story ticks, a card you turn, Keep in one tap, questions graded in place, a
  checkpoint, a kept pile at the end. The owner likes it ("I really like the direction").
- **On a computer the feed fails at the one thing a feed must do: move on.** One wheel notch does nothing (a single wheel event
  has to be 400 to 460 px), there is no visible Next or Previous, and the keys are shown nowhere. The stage is a 560 px phone
  column in a 1440 px screen, holding a 500 x 668 card for two lines of text.
- **Desktop becomes a study stage in three parts,** not a wider phone column:
  - a quiet session panel on the left: the chapter, where you are, time left, the score, the kept pile, Stop here;
  - the item in the middle at reading width (a landscape card, or a question);
  - the rail on the right (Keep or Save, Chapter).
  Under the item sits one action bar: a labelled Previous on the left and, on the right, the one volt key that names the next
  step (Turn over, Next, See how it went). On a question not yet answered the options are the step, and a quiet Skip waits in
  that place. One wheel notch, one trackpad swipe, Down, j, Space or Enter each move exactly one item.
- **On a phone the full-screen vertical feed stays.** The card fits its words (no 620 px empty box), the rail moves into a
  bottom action bar so the card gets the full width, and the same volt key gives a student who does not swipe a visible way on.
  A gentle drag of 18% of the screen moves one item.
- **The line you needed opens in place under the options,** as in the run the owner called "quite good". It is never a sheet
  over the answers.
- **The lamp-lit object behind every item goes.** It sits in the far corner on desktop, and every Accountancy chapter shows the
  same picture (LK21).
- **Motion stays inside the standards.** Turn 340 ms (was 420), tick fill 300 ms (was 600), the drift is removed, and every
  other value is 160 to 320 ms.

---

## 1. What works and must be kept

1. **The rhythm:** one item per screen, a Key card first, about two cards per question, a checkpoint after 8, an end screen.
2. **The story ticks:** one segment per item, done in ink-2, the current one filling with the accent. Day already uses
   `--a-select` (#6f8700), which keeps 3:1 on paper (feed.css 24-26).
3. **The card turn** as the feed's signature: a 3D rotateY with hidden backfaces, and a 120 ms cross-fade under reduced motion
   (feed.css 51-52, 173-178).
4. **Keep in one tap:** the bookmark fills, a 1.15 pop, a small copy of the card flies away, the label becomes Kept. Free shows
   "Pro" only for a locked card (BUILD-1101 1.1).
5. **Server-graded answers with no key on the client.** Right fills the row volt with ink text and settles from 1.04. Wrong
   shakes 4 px and outlines the right row volt (ChapterFeed.jsx 406-420, feed.css 104-111). The drill in DESIGN.md resolves an
   answer the same way, so the feed stays in the brand's voice.
6. **The true, specific head on old mistakes:** "You missed this in Mock 4 on 24 Oct" (std R-156: concrete evidence, not
   hype).
7. **NCERT's own words in the reading face** (Literata, the 1 px book rule) with the source line ("Accountancy Part 1, Ch 2,
   p. 48"). This is the feed's trust.
8. **The lit card surface** (cool light from the top edge and grain, keycards.css 13-17). The owner asked for it (W-013), so
   it is not a decorative gradient by default. Keep it on cards only.
9. **The checkpoint gives a choice,** Keep going or Stop here (LK11: options, not one fixed path).
10. **The end:** the kept pile fanning open, plain lines ("Questions 2 of 3 right", "Fixed 2 old mistakes"), and three keys
    with one volt (Another 10 minutes, Next chapter, Back to Explore).
11. **Free is calm:** a line and a See Pro text key, never a modal (LK15; research T005: no threat-based upsell).
12. **A focus place:** no sidebar, tab row or dock while you study (CRITIQUE-1 R8).
13. **Keys already wired:** arrows, Page keys and Space move or turn; 1 to 4 and A to D answer; Escape closes the line
    (ChapterFeed.jsx 432-453).
14. **Accessibility basics:** a `feed` role with articles carrying `aria-posinset` and `aria-setsize`, the card is a button with
    a full label, visible focus rings, 44 px targets, and reduced motion honoured.
15. **Arena tokens only** (`--a-*`), so Night and Day both follow without forks.

---

## 2. Findings

### 2.0 Captures looked at
- Feed, `tmp/learn-1101/audit/`:
  - 10 loading (1440, 390);
  - 11 card front (1440 Night and Day, 1366, 390 Night and Day, 360);
  - 12 turned (1440, 1366, 390);
  - 13 kept (1440, 390);
  - 14 question (1440, 1366, 390, 360);
  - 15 right with streak (1440, 390);
  - 16 checkpoint (1440, 390);
  - 17 end (1440, 1366, 390, 360);
  - 18 wrong with the sheet (1440 Night and Day, 1366, 390, 360);
  - 19 Free end (1440, 390); 20 Free second feed (390);
  - 21 Goodwill, no questions (end 1440, first 390); 22 P&L, one question (first 1440, end 1440); 23 no cards (1440).
- `tmp/learn-1031/feed2/`: card front at 430.
- For comparison: run 50-card-front-1440 and 53-run-wrong-line-1440, Explore 01-explore-covers-1440.

### 2.1 Blocker

**F1. Desktop: there is no way to move on (LK20).**
- One wheel notch (deltaY 100), a trackpad-like burst (6 x 40) and three notches 1.3 s apart all leave the feed on item 0.
- A single wheel event moves only from 460 px (1440x900) or 400 px (1366x768). 30 x 40 px (1,200 px in total) still moves
  nothing.
- No visible Next or Previous control exists. The 21 ticks are plain spans.
- The keys work but are shown nowhere, and the only hint reads "Tap to turn it over" on a mouse device.
- Cause: native `scroll-snap-type: y mandatory` with `scroll-snap-stop: always` snaps every short wheel scroll back. The JS
  "rest" net (180 ms after the last scroll) never fires in time, because mandatory snapping has already returned to the start.
- Evidence: index.md section 2 (a1-a5, b, c); `11-feed-card-front-1440-night.png`, `11-feed-card-front-1366-night.png`;
  ChapterFeed.jsx 284-341, 96; feed.css 38-40.

### 2.2 High

**F2. Desktop composition: a phone column in an empty screen (LK20, "too much blank space everywhere").**
- The stage is 560 of 1440 px (38.9%), with 440 px empty on each side (403 px at 1366).
- The card is 500 x 668 for two lines of text.
- The chapter's only identity is a 13 px caption at the column's far right.
- The subject object sits at the screen's bottom-right corner, about 300 px from the content.
- Evidence: index.md (d); `11-feed-card-front-1440-night.png` and `-1440-day.png`; feed.css 12-13 (`--fx-top` 106 px,
  `--fx-side` = (100vw - 560px) / 2), 50 (card insets), 60 (a 30% spacer under the front).

**F3. Phone: a tall empty card with narrow text.**
- The card is 298 x 620 at 390, because the rail takes 60 px (the card is 76% of the width). It holds 1 to 4 lines.
- "What is goodwill?" uses about a tenth of its card.
- The front at 30 px in a 254 px measure wraps into ragged lines ("What is / reconstitution / of a / partnership firm?").
- Evidence: `11-feed-card-front-390-night.png`, `-360-night.png`, `02-feed-card-front-430-night.png` (feed2),
  `21-feed-chapter-no-questions-first-390-night.png`; feed.css 50, 60-61.

**F4. Phone: navigation by gesture only, with a high threshold.**
- A slow 300 px drag (36% of the screen) snapped back in 6 of 6 tries; the browser's own 800 px/s gesture in 6 of 6.
- Quick flicks moved one item in 2 of 6 tries.
- After a turn or an answer nothing on screen says how to go on. "Swipe up for the next one" shows once, 600 ms after the first
  answer.
- This breaks the owner rule "never hide features behind gestures alone" (std R-092) for students new to apps.
- Evidence: index.md (e, e2, e3); `15-feed-right-streak-390-night.png`, `12-feed-card-turned-390-night.png`;
  ChapterFeed.jsx 141.

**F5. The line you needed covers the answers (std slop item 1).**
- Desktop: a 1440 px wide bottom sheet lies over option D and the rail. At 1366x768 the NCERT line is cut off at the screen's
  foot.
- Phone 360, long question: the sheet sits at the bottom of a slot taller than the screen, out of view, and the right answer is
  below the fold too.
- Evidence: `18-feed-wrong-sheet-1440-night.png`, `-1366-night.png`, `-360-night.png`; feed.css 115 (positioned against the
  slot, not the screen); ChapterFeed.jsx 142-162.

**F6. Numbers disagree within one session (std R-006, T-130: one definition per count).**
- The checkpoint counts old-mistake retries as questions ("2 of 2 right" at item 8).
- The end leaves them out: "Questions 2 of 3 right", plus "Fixed 2 old mistakes".
- Evidence: `16-feed-checkpoint-1440-night.png` vs `17-feed-end-1440-night.png`; ChapterFeed.jsx 456-461 vs learn.js 997-998
  and 1069-1072.

**F7. The service's newer states are not drawn.** The feed handles only a 402 at the start, and only its `line`. It ignores:
- the `options` and `resume` of `FREE_SESSION_USED`;
- the four 409 kinds (`QUESTION_CHANGED`, `QUESTION_HELD`, `RUN_EXPIRED`, `RUN_ENDED`);
- its page's `runId` and `end` props (ChapterFeed.jsx 230: `Feed({ chapterKey, minutes })`);
- `kept.line` and `dueOffer` on the end screen.

A failed Keep is also silent (393-395). Evidence: ChapterFeed.jsx 203-220, 230, 257-260, 393-395; api.js 10-39; learn.js 1079,
1084.

### 2.3 Medium

- **F8. The subject object behind every item.**
  - It is 220 px at 18% opacity with a 6 px blur. On desktop it reads as a smudge in the far corner; on a phone it sits under
    the rail.
  - It is the same picture for every Accountancy chapter (LK21).
  - It costs a blurred layer per slot on budget phones.
  - Evidence: every feed capture; ChapterFeed.jsx 47-50; feed.css 45-46.
- **F9. Loading invents progress.** It shows one blank slab, six placeholder ticks and no title (research T002: count only real
  progress). Evidence: `10-feed-loading-1440-night.png`, `-390-night.png`; ChapterFeed.jsx 472, 483-485.
- **F10. The rail jumps between items.** On a card it sits at 66% of the height beside the card. On a question it drops to the
  screen's foot (bottom 22 px), 300 px below the options at 1440. Evidence: `11-feed-card-front-1440-night.png` vs
  `14-feed-question-1440-night.png`; feed.css 68-69.
- **F11. The end screen is not fully true or complete.**
  - It says "10 minutes on Admission of a Partner" even when the student stopped at the checkpoint after about 4 minutes. That
    is the chosen length, not time spent (research T002).
  - A cards-only feed's end says nothing about cards (Goodwill: no seen or kept line).
  - The pile clips the kind labels of the back cards ("Defini", "Formu").
  - "Back Wed" says neither what comes back nor where.
  - Evidence: `17-feed-end-1440-night.png`, `21-feed-chapter-no-questions-end-1440-night.png`, `13-feed-kept-1440-night.png`;
    learn.js 1078; ChapterFeed.jsx 193-194.
- **F12. The checkpoint is one number in an empty screen.** Its line says "save what you kept", although Keep has already saved
  them (BUILD-1101 R16 fixes the copy). Evidence: `16-feed-checkpoint-1440-night.png`; data/learn/feed.js 19.
- **F13. The Free limit screen.**
  - The title is left-aligned and the line centred.
  - It shows placeholder ticks and no chapter title.
  - It says "free feed", although the rule counts any Learn session (LK15).
  - It offers no free way to go on with this chapter.
  - Evidence: `20-feed-free-second-390-night.png`; ChapterFeed.jsx 486-499.
- **F14. Long stems on a 360 phone.** At 22 px the stem runs to 16 lines and pushes the options below the fold. Evidence:
  `18-feed-wrong-sheet-360-night.png`; feed.css 93.
- **F15. Front wrapping.** `.fx-front` is a flex container. A cloze card's text runs and blanks become separate flex items, so
  lines break at the blanks instead of between words. This is from the code: no cloze front is in the captures, so check one.
  Evidence: feed.css 61-62; ChapterFeed.jsx 41-45.
- **F16. A console warning.** React's "Can't perform a React state update on a component that hasn't mounted yet" appeared once
  on the feed at 390 (index.md section 3). The standards want zero console errors. I did not trace the cause; the start runs
  from a microtask inside a portal mount (ChapterFeed.jsx 264-271).

### 2.4 Low

- **F17.** The phone back sets NCERT at 20 px in a 254 px measure: 15 lines. At 17.5 px across the full width it is about 10.
  `12-feed-card-turned-390-night.png`; feed.css 64.
- **F18.** The back drops the prompt, so a turned card no longer says what was asked. `12-feed-card-turned-1440-night.png`.
- **F19.** Assertion-Reason stems run as one paragraph. `15-feed-right-streak-1440-night.png`.
- **F20.** The head "Question" says nothing; "Question 2 of 5" would.
- **F21.** A right answer has no visible words, only the volt row and a screen-reader status. The streak floats as a chip in its
  own lane. ChapterFeed.jsx 133, 519.
- **F22.** The empty-chapter screen shows placeholder ticks, has a full stop in its heading, and no volt lead.
  `23-feed-chapter-no-cards-first-1440-night.png`.
- **F23.** The current tick fills over 600 ms, after the move has already ended (std R-153: a small state change is 150 to
  220 ms). feed.css 26.
- **F24.** The web buzzes on a wrong answer (`vibrate([8, 40, 8])`). The app's haptic grammar says "nothing on a wrong answer"
  (A7 section 2.7), so the port needs one rule.
- **F25.** j, k, Home and End do nothing (index.md b).

---

## 3. The refined design

### 3.1 Principles (each with its evidence)
1. **One item, one named next step, at every width.** Every state has a key that names its step, in the same place (std R-093;
   research AGENT_RULES 7). It is volt when moving on is the step; on a question not yet answered the options are the step and
   a quiet Skip holds the place. Gestures, the wheel and keys are shortcuts to it, never the only way (std R-092; research
   S016: consistent navigation and identification).
2. **Text is not video.** On desktop the stage takes a reading width (600 to 720 px) with a landscape card. On a phone it takes
   the full width. The card's height follows its words.
3. **The side space carries only the session's real numbers** (std T-097, T-131: no dead bands; research T002, S015: honest
   progress).
4. **Nothing covers the answers** (std slop item 1, T-095).
5. **One gesture moves one item.** The pager owns the wheel, touch and keys.
6. **Motion answers an action** and stays within std R-153 (100 ms press, 150 to 220 ms small change, 220 to 350 ms result, up
   to 500 ms milestone).
7. **One study stage for the feed and the run** (BUILD-1101 B1): the same bars, keys and line-in-place, so they feel like one
   product.

### 3.2 Layout per width

**Bands.** Phone under 768 px. Tablet and small laptop 768 to 1199 px (1024 included). Desktop 1200 px and up. The bands go by
CSS width, so 200% zoom on a 1440 screen gets the phone layout, which is correct.

**Desktop (1200 px and up): one centred grid of five tracks.**
`grid-template-columns: P G1 S G2 R`:

| Width band | Example | Panel P | Gap G1 | Stage S | Gap G2 | Rail R | Group | Each side margin |
|---|---|---|---|---|---|---|---|---|
| 1200-1359 | 1280 | 216 | 40 | 600 | 24 | 64 | 944 | 168 (128 at 1200) |
| 1360-1599 | 1366, 1440 | 240 | 48 | 680 | 24 | 64 | 1056 | 155 at 1366, 192 at 1440 |
| 1600 and up | 1920 | 264 | 56 | 720 | 28 | 64 | 1132 | 394 at 1920 |

Vertical sizes (desktop):

| Viewport height | Padding top and bottom | Ticks, then gap | Gap above the action bar | Action bar | Item area at that height | Card min-height |
|---|---|---|---|---|---|---|
| 820 and up | 36 | 2, then 16 | 16 | 72 (key 52) | 722 at 900 | 360 |
| 700-819 | 28 | 2, then 14 | 16 | 72 | 608 at 768 | 340 |
| under 700 (1366x650 laptops) | 20 | 2, then 12 | 12 | 64 (key 48) | 520 at 650 | 300 |

- The panel and the rail span the stage column's full height.
- The stage column stacks the ticks, the item area (flex 1, one page of the pager) and the action bar.
- No top bar on desktop: Close lives in the panel.

**Tablet and small laptop (768 to 1199 px; the 1024 example).**
- Stage S 600 px plus G2 24 plus rail 64 = 688, centred. At 1024 that leaves 168 on each side; at 768, 40.
- Top bar over the stage (width S, 108 px): row 1 Close, title, counter; row 2 the ticks plus "About 6 min left"; row 3
  "Up next".
- The item area's height is the screen's minus 232 px, capped at 640. The 232 px are the top bar (108), the 12 px under it,
  the 16 px above the action bar, the action bar (72) and 24 px of padding at the foot. The action bar sits right under the item
  area (BUILD-1101 B1). At 1024x768 the item area is 536 px and the card's min-height 340.

**Phone (under 768 px).**

| | 360 x 780 | 390 x 844 | 430 x 932 |
|---|---|---|---|
| Side gutter | 16 | 16 | 16 |
| Card width | 328 | 358 | 398 |
| Top bar (plus the top safe area) | 62 | 62 | 62 |
| Action bar (plus the bottom safe area) | 78 | 78 | 78 |
| Item area (12 px gaps above and below) | 616 | 680 | 768 |
| Card min-height, `clamp(300px, 46dvh, 380px)` | 359 | 380 | 380 |

- **Short screens (height under 560 px, phone landscape):**
  - the top bar is 52 (row 40) and the action bar 64;
  - the card's min-height is 220 and the front type one step down;
  - the kept stamp moves into the card's foot.

**Sketch, desktop 1440 x 900, a card face up.**
```
x=192                                                                                         x=1248
Close                     == == == == == == == == == == == ==  (21 ticks, 680 wide)
                          +--------------------------------------------------------+
Admission of a            | Definition   Must-know                                  |    ( )
Partner                   |                                                         |    Keep
Ch 4, Accountancy Part 1  |  What is reconstitution of                              |
                          |  a partnership firm?                                    |    ( )
3 of 21                   |                                                         |    Chapter
About 6 min left          |  NCERT, Accountancy Part 1, Ch 2, p. 48                 |
------------------------  +--------------------------------------------------------+
Questions  2 of 3 right   In Revise
Kept       2   [pile]
------------------------
Up next: a question you
missed in Mock 4
                          [ ^ Previous  Up ]                       [ Turn over   Space ]
Stop here
```

**Sketch, phone 390 x 844, a card face up.**
```
+----------------------------------------+
| == == == == == == == == == == == == == |  ticks
| X  Admission of a Partner  [b]2  3 of 21 v |
|                                        |
| +------------------------------------+ |
| | Definition  Must-know              | |
| |                                    | |
| | What is reconstitution             | |
| | of a partnership firm?             | |
| |                                    | |
| | NCERT, Accountancy Part 1, Ch 2    | |
| +------------------------------------+ |
| In Revise                              |
|                                        |
|  ( )       [     Turn over     ]   ( ) |
|  Keep                          Chapter |
+----------------------------------------+
```

### 3.3 The session panel (desktop), the top bars (tablet, phone)

**Session panel (desktop).** A full-height flex column, top-aligned with the ticks. Text only, no boxes; rows separated by
hairlines.

| Part | Spec |
|---|---|
| Close | A key 44 px tall: X icon 18 (stroke 2.2) and "Close" in 15/650 ink-2. Padding 0 14 0 10, margin-left -10, radius 12. Hover: ink on `--a-hover`. It leaves the feed; the run stays resumable that day (BUILD-1101 1.3). |
| Gap | 28 (20 under 700 px tall) |
| Chapter title | Display face, 650 22/1.18, -0.02em, ink, at most 3 lines, balanced wrap |
| Ref | 6 px below: "Ch 4, Accountancy Part 1" in 13/1.4 ink-3. Data: add `run.chapter.ref` and `partTitle` (additive), or read them from the covers' fields. |
| Gap | 28 (20) |
| Position | "3" in display 700 30/1, tabular, ink, then " of 21" in display 600 20 ink-3 (the run's counter look) |
| Time left | 6 px below: "About 6 min left" in 13.5/1.4 ink-2. It sums `seconds` of the items not yet reached (BUILD-1101 1.5) and runs through `minutesFor`; under a minute it reads "Under a minute left". |
| Gap | 20 |
| Rows | A two-column grid (84 px label, then the value), rows at least 40 px, 1 px `--a-line` top rule. Label 13/600 ink-3, value 15/600 ink, tabular. **Questions:** "2 of 3 right", shown from the first answer, counting plain questions only (the end's rule, F6); under it, 13/600 accent-text "4 in a row" from 3 in a row. **Old mistakes:** "1 of 2 fixed", from the first mistake answered. **Kept:** "2" plus the mini pile (three cards 28 x 36, radius 6, 1 px line-strong, raised, each offset 4 px), shown from the first Keep; the pile is the Keep flight's target. Rows appear on the student's own action, so the shift is not counted in CLS. |
| Gap | 20 |
| Up next | 13/1.45 ink-3, at most 2 lines: "Up next: a Key card", "Up next: a question", "Up next: a question you missed in Mock 4", "Up next: a checkpoint", "Up next: how it went". Read from the next slot on the client. |
| Stop here | Pushed to the column's foot (`margin-top: auto`), so it lines up with the action bar. A text key 44 px, 14.5/650 ink, underlined in line-strong. It cuts the feed at the current item and shows the end (as the checkpoint's Stop here does). Hidden on the end screen. |

**Tablet top bar (108 px, width S).**
- Row 1 (44 px):
  - Close (as on desktop);
  - the title, centred, 14.5/650 ink-2, one line with an ellipsis;
  - on the right, the kept count (bookmark-fill glyph 14 in `--a-select` plus "2" in 13.5/650 ink-2, shown only after a Keep;
    the flight's target);
  - then the counter "3 of 21" ("3" in 650 ink, "of 21" in ink-3).
- Row 2 (20 px): the ticks (flex 1), a 12 px gap, then "About 6 min left" in 12.5 ink-3.
- Row 3 (18 px): "Up next: ..." in 13 ink-3.
- 12 px below the top bar.

**Phone top bar (62 px plus the top safe area).**
- Ticks 10 px under the safe area, full width minus the gutters.
- Then a 44 px row, 6 px lower:
  - Close: X icon 22 in a 44 px target, margin-left -10;
  - the title, left-aligned, 15/650 ink-2, one line with an ellipsis (it was right-aligned; the right now holds the counter);
  - the kept count (as on tablet; it appears with a 160 ms fade from scale 0.95);
  - the counter button "3 of 21" (13.5/650 tabular, plus a ChevronDown icon 14 inside the control, 44 px tall, padding 0 8).
    It opens "This feed" (P2, section 3.7).
- At 360 the title keeps about 136 px ("Admission of a Pa..."). That is why the streak lives in the verdict line on phones and
  not in this bar (section 3.17, change D).

**Ticks (all widths).**
- 2 px tall with 3 px gaps, at most 48 segments: done in ink-2, the current one filling with `--a-select` over 300 ms, ahead in
  `--a-line`.
- Over 48 items (a 20-minute cards-only feed), a single 2 px track with an `--a-select` fill scaled to position / total.
- They stay `aria-hidden`; the counter carries the number.

### 3.4 The Key card item

**Size.**
- The width is the stage S on desktop and tablet, and the screen minus 32 on a phone.
- The height is the taller face's (measure both faces, so nothing jumps on the turn), at least the min-height of section 3.2,
  at most the item area minus 28 (the stamp line).
- Radius 24, 1 px `--a-line-strong`, `--kc-surface`, `--a-shadow-1`.
- Padding: phone 20 20 18; tablet 28 32 24; desktop 32 40 28 (28 32 24 when S is 600).
- Vertical position: centred in the item area with a slight upward bias (`padding-bottom: 4dvh` on the page). Perspective 1200
  on a phone, 1600 on tablet and desktop.

**Front.** A grid with rows auto, 1fr, auto.
- **Kind line:** 13/600 ink-3, e.g. "Definition", with "Must-know" in accent-text (volt on Night, #4f6400 on Day).
- **Prompt:**
  - a block element, not flex (fixes F15); the blanks stay inline-block `kc-gap`;
  - `align-self: center`, display face 650, balanced wrap, `overflow-wrap: anywhere`;
  - the size goes by the length of the front in characters:

| Front length | Phone under 380 | Phone 380 and up | Tablet | Desktop, S 680-720 | Desktop, S 600 |
|---|---|---|---|---|---|
| up to 60 | 32/1.12 | 34/1.12 | 38/1.12 | 44/1.1 | 40/1.1 |
| 61-120 | 26/1.16 | 28/1.16 | 32/1.15 | 36/1.14 | 33/1.14 |
| over 120 | 21/1.3 | 22/1.3 | 25/1.28 | 28/1.26 | 26/1.26 |

  - letter-spacing -0.025em from 32 px, -0.02em at 26-31, -0.01em below.
- **Foot:** the source, a BookOpen icon 14 plus "NCERT, Accountancy Part 1, Ch 2, p. 48" in 12.5/1.4 ink-3. It tells the
  student where the answer comes from, and it anchors the bottom of the card instead of an empty band (BUILD-1101 B1).
- **No hint paragraph.** "Tap to turn it over" goes; the action bar's "Turn over" key does that job on every card.

**Back.**
- The kind line, then the prompt repeated small (phone 13, tablet 13.5, desktop 14; /1.4, 600 ink-3, at most 2 lines), so a
  turned card still says what was asked (F18).
- NCERT's line (`kc-ncert`): phone 17.5/1.62, tablet 18.5/1.62, desktop 20/1.6, at most 62ch.
- The source: 13/1.45 ink-3.
- If the back is taller than the card can be, the back face scrolls inside (`overflow-y: auto`, `overscroll-behavior: contain`).
  The pager's edge rule applies (section 3.7).

**The stamp line under the card.**
- 20 px reserved, 8 px below the card, 13/600 ink-2 with a bookmark-fill icon 14 in `--a-select`.
- Copy: "In Revise" for a new card, "In Revise, back Wed" for a held one (BUILD-1101 1.1). It replaces "Back Wed".
- On failure: "Not kept. Try again." in bad-text, `role="alert"`, and the key returns to Keep.

### 3.5 The question item

- **Layout.** Top-aligned, not centred, so the options never jump when the line opens below them. Page padding-top: phone 16,
  tablet 20, desktop `clamp(8px, 3vh, 32px)`. Width: the stage S, or the screen minus 32. Questions sit on the canvas (no card
  face); the options are the only boxes.
- **Head** (13/600 ink-3; tablet 13.5, desktop 14):
  - "Question 2 of 5" (its place among the feed's questions; F20);
  - an old mistake keeps its own head, "You missed this in Mock 4 on 24 Oct" or "You missed this yesterday" (BUILD-1101 R10),
    in ink-2.
- **Assertion-Reason.** When the stem matches `/^\s*Assertion\s*(\(A\))?\s*:\s*(.+?)\s*Reason\s*(\(R\))?\s*:\s*(.+)$/is`, set
  two blocks: a 13/700 ink-3 label "Assertion" over its text, then "Reason" over its text, 10 px apart (F19).
- **Stem** (body face, 650, at most 62ch):

| | Phone under 380 | Phone 380 and up | Tablet | Desktop |
|---|---|---|---|---|
| Stem up to 200 characters | 19/1.42 | 20/1.42 | 21/1.4 | 23/1.4 |
| Stem over 200 characters | 17.5/1.45 | 18/1.45 | 19/1.45 | 20/1.45 |
| Option text (550) | 15.5/1.4 | 16/1.4 | 16.5/1.4 | 17/1.4 |
| Option min-height and gap | 56, 10 | 56, 10 | 56, 10 | 58, 12 |

- **Options.**
  - Rows as today: 30 px letter chip with radius 9, padding 12 16, radius 16, 1 px line-strong, raised.
  - Two columns (`1fr 1fr`, gap 12) on tablet and desktop when every option is 28 characters or fewer after its letter is
    stripped ("Rs 25,200, Rs 16,800 and Nil" fits); otherwise one.
  - Keys 1 to 4 and A to D answer before the answer is in.
- **Pending.** The chosen row shows the spinner (as now), the other rows are disabled, and Skip is disabled.
- **Verdict line** (16 px under the options; phone 15/650, desktop 16/650, with an 18 px icon):
  - right: a Check icon in good-text and "Right." in ink;
  - from 3 in a row: "Right. 4 in a row." The number counts up in 160 ms. This replaces the floating chip (F21; section
    3.17, change D);
  - a right old mistake: the server's `fixedText` ("Right this time. Back on Wed to check it held.");
  - wrong: an X icon in bad-text and "Not quite. The answer is B." in ink (the run's wording).
- **The line you needed** (wrong only; it opens in place, 12 px under the verdict):
  - a block on `--a-raised`, 1 px `--a-line`, radius 16, padding 16 18 (phone 14 16);
  - the title "The line you needed" (display 700, phone 15, desktop 17);
  - NCERT's line (`kc-ncert`, phone 16.5/1.6, desktop 18/1.6, key words underlined with `kc-mark`), then the source (13
    ink-3);
  - locked on Free: the server's `line.text` plus a "See Pro" text key;
  - no linked card: the explanation in 15/1.55 ink-2.
- **Overflow.** If the page now overflows, it scrolls inside, and at +300 ms the line's title is scrolled into view, clear of the
  action bar (`scrollIntoView({ block: 'nearest' })`, smooth).
- **Desktop has no side panel for the line** (the brief asked). A right-hand panel needs either a column reserved and empty
  until a wrong answer (the blank space the owner dislikes) or a stage that slides sideways while the student reads. Inline
  keeps question, choice, key and line in one reading column, works unchanged from 360 to 1920, and matches the run the owner
  liked (`53-run-wrong-line-1440-night.png`). The cost: on a 1366x650 laptop a long question plus its line scrolls inside the
  item. Next stays pinned in the action bar, so that cost is small.

### 3.6 The rail and the action bar

**The rail** (desktop and tablet: column R; phone: the two side slots of the action bar).
- A key is a 48 px round glyph (1 px `--a-line`, raised, icon 22 stroke 1.9) with a 12/600 ink-2 label 4 px under it.
- On desktop and tablet the rail is vertically centred on the item area, with 16 px between keys, so it never jumps between items
  (F10).
- On: the glyph's icon fills in `--a-select` and the label turns ink.
- Hover (fine pointer): border `--a-line-hover`, background `--a-option-hover`. Pressed: scale 0.94 for 100 ms. Focus: a 2 px
  `--a-focus` ring 2 px out on the glyph. Busy: a 20 px spinner. Locked: label "Pro".

**The action bar.**
- Desktop and tablet:
  - width S, height 72 (64 when short), `space-between`;
  - left: Previous, a line key 48 px (`kc-btn--line`, padding 0 16 0 12) with a ChevronUp icon 18, "Previous" in 15/650
    ink-2, and on a fine pointer a `kc-kbd` "Up" keycap (an arrow glyph inside the keycap is allowed, since it names a key and is
    not appended text). Disabled on item 1 (opacity 0.45);
  - right: the step slot.
- Phone:
  - fixed to the bottom over the feed, background `--a-bg`, no hairline;
  - `grid-template-columns: 56px minmax(0, 1fr) 56px`, column-gap 12, padding 6 16 calc(8px + safe area);
  - side slots: the rail keys (left Keep or Save, right Chapter);
  - middle: the step slot, 52 px tall and the full column width, its centre level with the glyphs' centres.
- The step slot's primary is `kc-btn--volt`: height 52, radius 14, 650 16 px; at least 220 px wide on desktop; a `kc-kbd`
  "Space" keycap on fine pointers only. It is the screen's one volt key.

| Item and state | Phone bar | Desktop and tablet step slot (Previous always on the left) | Rail |
|---|---|---|---|
| Card, face up | Keep, **Turn over**, Chapter | **Turn over** (Space) | Keep, Chapter |
| Card, turned | Keep, **Next**, Chapter | **Next** (Space) | Kept or Keep, Chapter |
| Last item, done | ..., **See how it went**, ... | **See how it went** (Space) | as the item |
| Question, not answered | Save, Skip (line key, 52), Chapter | Skip (quiet text key, 48) | Save, Chapter |
| Question, pending | Save, Skip disabled, Chapter | Skip disabled | Save, Chapter |
| Question, answered | Save, **Next**, Chapter | **Next** (Space), fading in at +260 ms | Saved or Save, Chapter |
| Question left out (409) | Save hidden, **Next**, Chapter | **Next** | Chapter |
| Checkpoint | two keys 1fr 1fr: Stop here (line), **Keep going** | Stop here (line key 48) and **Keep going** (Space) | none |
| End | no bar (keys in the screen) | no bar | none |
| Loading | a key-shaped skeleton | a key-shaped skeleton | skeleton glyphs |

- **The turn changes the label.** On a card, the label crosses from "Turn over" to "Next" at the turn's midpoint (170 ms of 340).
  Turning back to the front keeps "Next": the card has been seen.

### 3.7 Moving between items

**The pager** (BUILD-1101 B1; it replaces native scroll-snap).
- The items sit in a track, one page per item-area height, moved with `transform: translateY` in 320 ms
  `cubic-bezier(0.32, 0.72, 0, 1)`.
- Every page is rendered. Pages more than 2 away get `content-visibility: auto; contain-intrinsic-size: auto 100%` for budget
  phones.
- The action bar, the panel and the rail sit outside the track, bound to the active item.

**Touch** (phone and touch tablets; use touch events with non-passive `touchmove`, so the edge hand-off can cancel the native
scroll).
- Tap: under 8 px of movement and under 300 ms is a tap (turn, choose, keys); the pager does nothing.
- Direction lock at 8 px. Vertical when |dy| > |dx|; a sideways gesture is ignored.
- If the touch started inside an item scroller (a long question, a long back) that can still move in the drag's direction, the
  native scroll runs and the pager stays out for that whole touch. Inner scrollers get `touch-action: pan-y` and
  `overscroll-behavior: contain`.
- Otherwise the track follows the finger 1:1, with resistance 0.35 past the first and the last page, and `preventDefault` on
  each move.
- Release: move one item when the drag is past 18% of the item area (152 px at 844) or the release velocity over the last 80 ms
  is above 0.35 px/ms in that direction. Never more than one item. Otherwise spring back in 320 ms on the same curve.
- A slow drag of a third of the screen now moves (F4).

**Wheel and trackpad** (any device with a wheel). One gesture moves one item. A gesture that begins inside scrollable content
ends there.
```js
const WHEEL = { notch: 50, step: 60, quiet: 220, line: 40 };
let acc = 0, lastAt = -Infinity, spent = false, innerAtStart = false;
function onWheel(e) {
  if (e.ctrlKey) return;                                             // pinch zoom on a trackpad
  const unit = e.deltaMode === 1 ? WHEEL.line : e.deltaMode === 2 ? itemAreaHeight() : 1;   // Firefox sends lines
  const dy = e.deltaY * unit;
  if (Math.abs(e.deltaX * unit) > Math.abs(dy)) return;              // sideways is not ours
  const fresh = e.timeStamp - lastAt > WHEEL.quiet;                  // 220 ms of quiet ends a gesture
  lastAt = e.timeStamp;
  const inner = scrollerThatCanMove(e.target, Math.sign(dy));        // the item's own scroller or the card back
  if (fresh) { acc = 0; spent = false; innerAtStart = Boolean(inner); }
  if (inner) return;                                                 // content scrolls first, natively
  e.preventDefault();                                                // the page behind never scrolls
  if (innerAtStart || spent || pager.moving) return;
  acc += dy;
  if (Math.abs(dy) >= WHEEL.notch || Math.abs(acc) >= WHEEL.step) {
    const dir = Math.sign(Math.abs(dy) >= WHEEL.notch ? dy : acc);  // a notch's own sign, else the gesture's sum
    spent = true; acc = 0;
    pager.go(pager.active + dir);
  }
}
stage.addEventListener('wheel', onWheel, { passive: false });
```
- `scrollerThatCanMove(el, dir)` walks up to the item's root. It returns the first element with `overflow-y` auto or scroll and
  `scrollHeight > clientHeight + 1` that can still move in `dir` (`scrollTop > 1` going up; `scrollTop + clientHeight <
  scrollHeight - 1` going down). Otherwise it returns null.
- Why this rule:
  - one mouse notch (100 or 120 px) moves at once;
  - a trackpad swipe moves after 60 px and its inertia tail is swallowed until 220 ms of quiet;
  - a Firefox notch (3 lines = 120 px) works.
- Known limit: a second deliberate swipe during a long inertia tail waits for the quiet. That is acceptable; short-video sites
  behave the same way.

**Keys** (window listener; ignored with Ctrl, Alt or Meta, or when focus is in a text field).

| Key | Does | Note |
|---|---|---|
| ArrowDown, PageDown, j | next item | skips the turn |
| ArrowUp, PageUp, k | previous item | |
| Space | turns a face-up card, otherwise next | When focus is on a button or link, that control acts instead; the card is a button, so Space on it turns it and nothing else. |
| Enter | the same as Space on the stage | a focused control activates itself |
| 1 to 4, a to d | answer the current question | only before its answer |
| Home | the first item | |
| End | the end screen | |
| Escape | closes "This feed" or the Keys list | never leaves the feed (the end summary is not lost by a stray key) |
| ? | opens the Keys list (desktop) | a small popover over the action bar listing this table |

**Focus and announcements.**
- A polite live region says "Card 4 of 21" or "Question 5 of 21" on each move (BUILD-1101 B1).
- After a move by an action-bar key, focus stays on that key, so repeated presses work.
- After a move by a shortcut, focus does not move.
- Each page is an `article` with `tabindex="-1"`, `aria-posinset`, `aria-setsize` and an `aria-label`. The track has
  `role="feed"`, `aria-roledescription="feed"` and `aria-label="Admission of a Partner, 21 items"`.

**Guards.**
- `html:has(.fx) { overscroll-behavior: none; }` stops the trackpad's two-finger history swipe and pull-to-refresh from leaving
  the feed.
- Clicks in the empty margins keep the keys working (as now, index.md b2).

**First-time affordances** (students new to apps and to computer-based tests).
- Every state has a named volt key (section 3.6), so nobody needs a gesture.
- Desktop, fine pointer: the keycaps inside Previous and the volt key. Plus one line, 12.5/1.4 ink-3, centred 10 px under the
  action bar, on the first three items of the student's first feed only: "The mouse wheel and the arrow keys move between items
  too." (localStorage `learn2.feed.keys.v1`, read in try/catch).
- Phone (P2): on the first feed only, after the first card is turned, the track nudges up 24 px and back once (two 180 ms legs,
  ease-out). It shows that the next item waits below without a sentence. None under reduced motion.
- Removed: "Tap to turn it over" and "Swipe up for the next one".

**This feed (P2; the visible Previous on a phone, and an overview).**
- The phone counter opens a bottom sheet:
  - max-height 70dvh, radius 22 22 0 0, `--a-sheet`;
  - the title "This feed" (display 700 17) with a Close X (44);
  - rows 52 px: the number (13 tabular ink-3), the kind and the first words (a card's front or the stem; 14.5/600 ink-2, one
    line with an ellipsis), and a state icon (Check for right, X for wrong, bookmark-fill for kept, a dot for seen, nothing for
    ahead);
  - the current row carries "Now" in accent-text;
  - a tap on a row closes the sheet (200 ms) and goes there;
  - at the foot, a text key "Stop here and see how it went".
- Reason: the owner rule against gesture-only features, and LK9 (easy control of your own study). Desktop does not need it
  (Previous and the keys are visible).

### 3.8 The checkpoint

- After items 8, 16 and so on, only when 4 or more items follow (BUILD-1101 1.4). It moves on only by a key, a swipe or the
  wheel.
- Content is centred in the item area, at most 420 px wide:
  - the number (display 700, phone 44/1.05, desktop 52/1.05, -0.03em, tabular): "2 of 3 right" once a plain question is
    answered, else "6 cards seen, 2 kept". Same definition as the panel and the end (F6);
  - 10 px below, 15.5/1.5 ink-2: "8 of 21 done. About 6 min left.";
  - 6 px below, the line (BUILD-1101 R16): "Keep going, or stop here. What you kept is already in Revise." Without a kept
    card: "Keep going, or stop here.";
  - on phones only, when kept > 0, the mini pile (three cards 28 x 36) 16 px above the number, so the pause shows what the
    student collected. Desktop already shows it in the panel.
- Keys are in the action bar (section 3.6): Stop here (line key) and Keep going (volt). On desktop, Keep going carries the
  "Space" keycap.

### 3.9 The end screen

- **Desktop and tablet (1024 and up).** Two columns inside 880 px, centred vertically (BUILD-1101 B2):
  - left (440): Close (as in the panel), the title, the done line, the kept pile, the lines;
  - right (400): the keys, the volt lead first;
  - gap 40; no rail, no action bar, no panel.
  - At 768-1023 and on phones, stacked in one column (at most 440 px wide; full width minus 32 on a phone). The phone keeps its
    top bar, whose counter reads "21 of 21", and hides the action bar.
- **Title.** The chapter title in display 750 (desktop 34/1.08, phone 28/1.12), -0.03em.
  - Then the done line (15.5/1.5 ink-2): "All 21 done in 9 min." or "You stopped at 8 of 21."
  - This replaces "10 minutes on Admission of a Partner", which is untrue after an early stop (F11; research T002).
  - Data: add `feed.done: { reached, of, minutes }` to the end (additive). `minutes` is the first event to the last, rounded,
    at least 1. Without it: "All 21 done." or "You stopped at 8 of 21."
- **Kept pile.**
  - The fan of up to four cards 112 x 140 (as now). Only the top card shows its kind and front; the cards behind show the
    three hairlines only, so no label is ever clipped (F11).
  - Under it: "6 kept" (700 ink) and the server's `kept.line` ("They are first in Revise.") in ink-2 (B1.1). The pile and
    "Back Wed" go.
  - Nothing kept: "Nothing kept this time. Keep a card and it comes back in Revise."
- **Lines** (hairline rows, 15/1.45, the label in 650 ink at 96 px), always in this order:
  - "Cards: 16 seen, 6 kept" (new; F11);
  - "Questions: 2 of 3 right";
  - "Old mistakes: 2 of 2 fixed" or "Old mistakes: 1 still open".
- **Keys** (each 52 px, full column width):
  - the lead "Another 10 minutes" (volt, `fresh: true`);
  - "Next chapter: Retirement and Death of a Partner" (line key);
  - the `dueOffer` "Revise 3 due cards, about 1 min" (line key, when present; new in the UI, F7);
  - "Back to Explore" (quiet text key, centred).
  - Free after the day's session: the lead is replaced by the server line with a "See Pro" text key, and the other keys
    stay.
- **Motion.** The fan opens as the end comes into view (320 ms with a 40 ms stagger, 440 ms in all, a milestone). Nothing
  else moves.

### 3.10 States

| State | Screen |
|---|---|
| **Loading** (the start request) | The final shape, no spinner, `aria-busy`, `role="status"` "Starting the feed". Ticks: one plain 2 px hairline (no invented segments; F9). Title: the real title if the link carries it, else a 140 x 14 skeleton bar. A card skeleton at the card's min-height: a kind bar 80 x 12, three prompt bars 86%, 72% and 40% of the width, 28 px tall with 12 px gaps, a foot bar 180 x 12. A key-shaped skeleton in the action bar. Desktop panel: the real Close, then skeleton title and number rows. Under reduced motion the skeleton does not shimmer. |
| **End loading** (`GET /end`) | The end's final shape: a title bar 60% x 32, a pile block 156 tall, two line rows, two key bars. |
| **Error** (start failed) | Centred, at most 420 px: "The feed did not start" (display 700 26), "Check your connection and try again." (15 ink-2), keys "Try again" (volt) and "Back to Explore" (quiet). No ticks. |
| **Empty** (no cards and no questions) | "Nothing to play here yet" (no full stop), "This chapter's cards and questions are still being checked.", keys "Back to Explore" (volt, the only real way on) and "Open the chapter" (line). No ticks, no counter (F22). |
| **Free, the day's session used** (402 `FREE_SESSION_USED`) | A calm full stage, centred, one alignment (F13): the title "Today's free session is used" (display 700 26), the server's `line`, then `options` as line keys, each with its `evidence` under the label in 13 ink-3, then a "See Pro" text key. When `resume` is present, the lead is a volt key, "Pick up where you stopped, 8 of 21". No ticks. |
| **Resumed** (`run.resumed`) | Opens on the first item not done, with the ticks filled to it. Phone and tablet: the title cross-fades to "Picked up at 9 of 21" for 2.4 s, then back (200 ms fades). Desktop: the same words as a line under the time left, until the first move. |
| **Question left out** (409 `QUESTION_CHANGED` or `QUESTION_HELD`) | The question's options are replaced by one 15/1.5 ink-2 line: "This question changed a moment ago, so it is left out." or "This question is in an open Mob paper, so it is left out for now." Next (volt) moves on. The item does not count. |
| **Run closed** (409 `RUN_EXPIRED` or `RUN_ENDED`) | Go to the end screen with what was done. |
| **Answer not saved** | "That answer was not saved. Try again." (`kc-err`, `role="alert"`) under the options, the options enabled again (as now). |
| **Keep failed** | The stamp line says "Not kept. Try again." (F7). |
| **Offline mid-feed** | Items already loaded keep working for reading. An answer or a Keep fails with the lines above. No extra banner. |

### 3.11 Motion

| What | Now | Proposed | Easing | Reduced motion |
|---|---|---|---|---|
| Move to another item | native snap | 320 ms `translateY` of the track | cubic-bezier(0.32, 0.72, 0, 1) | instant, with a 120 ms cross-fade |
| Touch follow | native | 1:1; 0.35 resistance past the ends | none | the same follow; release lands at once |
| Card turn | 420 ms | **340 ms** rotateY | cubic-bezier(0.32, 0.72, 0, 1) | 120 ms cross-fade |
| Key label swap on the turn | none | 120 ms opacity at 170 ms | ease-out | instant |
| Current tick fill | 600 ms | **300 ms** scaleX | `--ease-out` | instant |
| Object drift | 600 ms | **removed** with the object | none | none |
| Right row | 200 ms settle from 1.04 | keep | ease-out | colour only |
| Wrong row | 240 ms shake, 4 px twice | keep | linear | colour only |
| Other rows recede | instant to 0.55 | to 0.4 over 160 ms, starting at +90 ms | ease-out | instant |
| Verdict and the line open | sheet rise 280 ms | 240 ms grid rows 0fr to 1fr plus opacity, at +180 ms | cubic-bezier(0.23, 1, 0.32, 1) | instant |
| Next appears | none | opacity 160 ms at +260 ms (the drill's order in DESIGN.md) | ease-out | instant |
| Scroll the line into view | none | smooth, at +300 ms, only if needed | browser | instant |
| Keep pop | 180 ms to 1.15 | keep | ease-out | none |
| Keep flight | 320 ms to the rail's foot | 320 ms to the panel's pile (desktop) or the kept count (tablet, phone) | cubic-bezier(0.32, 0.72, 0, 1) | none; the count changes |
| Kept count bump | none | 160 ms rising 45% and fading in | ease-out | instant |
| Streak number | 220 ms | 160 ms, in the verdict line | ease-out | instant |
| End pile fan | 320 ms, 40 ms stagger | keep (440 ms, a milestone) | cubic-bezier(0.32, 0.72, 0, 1) | already fanned |
| First-feed nudge (phone, P2) | none | two legs of 180 ms, once | ease-out | none |

Why the two changes:
- **Turn, 420 to 340 ms.** A turn reveals a result (std R-153: 220 to 350 ms). It is the most repeated motion of the feed, 15 to
  40 times a session, and frequent motion must stay short. On this front-loaded curve 340 ms draws the same arc and lands
  sooner.
- **Drift and fill.** The drift answered no action; it is gone with the object. The fill of 600 ms ran on after the move had
  ended, so it now matches the 320 ms move.

Rules:
- Only transform and opacity animate (the line's grid rows are the one layout transition). No `transition: all`.
- **Haptics:** a turn 8 ms; a right answer 12 ms; a wrong answer none (F24, the app's grammar).

### 3.12 Copy (every string, sentence case, no middle dots, no exclamation marks)

- **Keys:** "Turn over", "Next", "See how it went", "Previous", "Skip", "Keep going", "Stop here", "Try again", "Back to
  Explore", "Open the chapter", "Another 10 minutes", "Next chapter: {title}", "Revise 3 due cards, about 1 min", "See Pro",
  "Close", "Stop here and see how it went".
- **Keycaps:** "Space", "Up" (an arrow glyph is allowed inside the keycap only).
- **Rail labels:** "Keep", "Kept", "Save", "Saved", "Chapter", "Pro".
- **Stamp:** "In Revise", "In Revise, back Wed", "Not kept. Try again."
- **Card foot:** "NCERT, Accountancy Part 1, Ch 2, p. 48" (from the card's source).
- **Question heads:** "Question 2 of 5", "You missed this in Mock 4 on 24 Oct", "You missed this yesterday".
- **Verdicts:** "Right.", "Right. 4 in a row.", "Right this time. Back on Wed to check it held." (server), "Not quite. The answer
  is B."
- **The line:** "The line you needed".
- **Session panel:** "3 of 21", "About 6 min left", "Under a minute left", "Questions", "2 of 3 right", "4 in a row", "Old
  mistakes", "1 of 2 fixed", "Kept", "Up next: a Key card", "Up next: a question", "Up next: a question you missed in Mock 4",
  "Up next: a checkpoint", "Up next: how it went", "Picked up where you stopped."
- **First-time line (desktop):** "The mouse wheel and the arrow keys move between items too."
- **Checkpoint:** "2 of 3 right", "6 cards seen, 2 kept", "8 of 21 done. About 6 min left.", "Keep going, or stop here. What you
  kept is already in Revise.", "Keep going, or stop here."
- **End:** "{chapter title}", "All 21 done in 9 min.", "You stopped at 8 of 21.", "6 kept", "They are first in Revise."
  (server), "Nothing kept this time. Keep a card and it comes back in Revise.", "Cards: 16 seen, 6 kept", "Questions: 2 of 3
  right", "Old mistakes: 2 of 2 fixed", "Old mistakes: 1 still open".
- **States:**
  - "Starting the feed" (screen reader);
  - "The feed did not start", "Check your connection and try again.";
  - "Nothing to play here yet", "This chapter's cards and questions are still being checked.";
  - "Today's free session is used" with the server line ("Your free Learn session for today is done. Explore questions stay
    free. Pro has as many as you like.");
  - "Pick up where you stopped, 8 of 21", "Picked up at 9 of 21";
  - "This question changed a moment ago, so it is left out.", "This question is in an open Mob paper, so it is left out for
    now.";
  - "That answer was not saved. Try again."
- **Screen readers:**
  - "Card 3 of 21", "Question 4 of 21", "Checkpoint after 8 of 21", "The end of the feed";
  - the card's label "Definition: What is reconstitution of a partnership firm? Turn it over to see NCERT's line." It was
    "Tap to turn it over", which is touch wording.
- **Removed:** "Tap to turn it over", "Swipe up for the next one", "Back Wed" (alone), "One feed a day on Free", "Your free feed
  for today is done", "10 minutes on {title}" (as the end title).

### 3.13 Night and Day

The design adds no new colours; every new element uses Arena tokens. The values below are from `src/app/(app)/arena.css`.

| Element | Night | Day |
|---|---|---|
| Ground | `--a-bg` #0b100e | #f4f5f0 |
| Card surface | `--kc-surface` over `--a-raised` #131a16 (cool light, grain) | over #ffffff |
| Card border | `--a-line-strong` #384736 | #bcc5b0 |
| Panel and row rules | `--a-line` #253026 | #dce1d4 |
| Text | ink #f2f4ec, ink-2 #bcc5b9, ink-3 #93a08f | #172016, #3d4a39, #56624f |
| Current tick, kept glyph, kept icon | `--a-select` #d2f000 | #6f8700 (3:1 on paper) |
| Must-know, "4 in a row", "Now" | `--a-accent-text` #d2f000 | #4f6400 |
| Volt key, right row | #d2f000 fill, #10140e text, #8ba000 lip | the same |
| Wrong row | `--a-bad-text` #ff9d92 border, `--a-bad-wash` | #b0291f, rgba(176, 41, 31, 0.08) |
| Verdict icons | `--a-good-text` #b6e36e, `--a-bad-text` | #3d6600, #b0291f |
| The line block | `--a-raised`, `--a-line` | the same tokens |
| Focus ring | `--a-focus` #d2f000 | #4f6400 |

Check at build:
- Day ink-3 on the white card (the foot, about 6:1);
- Night ink-3 on #131a16 (about 6:1);
- accent-text on Day's white card (#4f6400, about 6:1).

### 3.14 Accessibility

- **Targets:** 48 px for the action bar and rail keys, 44 px for Close, the counter and text keys. Focus is always visible.
- **Every action has a visible, named control.** Gestures and keys are only shortcuts.
- **Order:** the DOM order follows the visual order: Close, the item, the rail, the action bar, Stop here (desktop).
- **Screen readers:** the live region, the article labels, the card's full label, the verdict as a status, the line block
  labelled by its title.
- **Reduced motion:** see the motion table. No information depends on motion; the verdict always has words and an icon.
- **Zoom:** 200% on desktop falls into the phone layout and works.
- **No hidden layers:** the action bar's background must not swallow clicks outside its keys. Hit-test with
  `document.elementFromPoint` (std 11).

### 3.15 What to borrow from other products (the pattern, never the look)

| Product | Borrow | Do not copy |
|---|---|---|
| YouTube Shorts and TikTok on desktop | The clip stays in one place with its action column right beside it. Up and down controls sit at a fixed spot. One wheel notch or one arrow key moves one item. Here: the rail beside the stage, the wheel rule, the keys. | The portrait 9:16 stage (wrong for text), icon-only arrows, like counts and social numbers. |
| Instagram Reels and stories | Full-screen focus on a phone, the segmented story ticks, the round labelled rail keys. | Autoplay pace, endless scroll (the feed ends, with a summary), anything social. |
| Quizlet flashcards | A wide card in the middle of the desktop screen, click or Space to flip, back and forward right under the card with the position between them. | Its palette and card chrome. |
| Anki | One key at the bottom that changes with the state, with its keyboard key printed on it. | The dense rating grid and interval numbers (the feed's Keep is one tap). |
| Brilliant and Duolingo | A fixed action bar whose main key changes label with the state (check, then continue). The explanation appears where you answered. Skip as a quiet second key. Number keys answer. Progress across the top. | Hearts, lives, punitive streaks, sounds and mascots in the item (product rules forbid punitive streaks; Mobi stays out of the feed), full-screen rewards per answer. |

### 3.16 Mapping to the Flutter app (the phone port later)

- **Screen.** `lib/features/learn2/feed/` (A7's layout): a root route with no app bar, `Scaffold` on the ground token.
- **Pager.**
  - A vertical `PageView.builder` with `NeverScrollableScrollPhysics`, driven by a `GestureDetector` / `Listener` that applies
    the same numbers: 1:1 follow, 0.35 resistance at the ends, 18% of the page or 350 dp/s to move one page;
  - `animateToPage` in 320 ms with `Cubic(0.32, 0.72, 0, 1)`, and never more than one page per gesture.
  - This also fixes A7's nested-scroll caveat. At drag start, check the page's own `ScrollController.position`: if it can move
    in the drag's direction, the inner scroll owns the whole drag; otherwise the pager does. That is the web's
    edge-at-start rule, so long questions and the line in place can scroll inside a page.
- **Top bar.**
  - `SafeArea(bottom: false)`;
  - ticks as a `Row` of `Expanded` 2 dp bars with 3 dp gaps, the current one in a `TweenAnimationBuilder` (0 to 1, 300 ms);
  - a `Row` of Close (48 dp), the title (`TextOverflow.ellipsis`), the kept count (`GlobalKey`, the flight target) and the
    counter (opens "This feed" as a `showModalBottomSheet`).
- **Action bar.** `SafeArea(top: false)` with a `Row`:
  - `RailKey` (Keep or Save), an `Expanded` primary key (52 dp, volt) and `RailKey` (Chapter);
  - at the checkpoint, two `Expanded` keys.
- **Card turn.** A new `MmFlip`: `Transform` with `Matrix4.identity()..setEntry(3, 2, 0.0008)..rotateY(angle)`, 340 ms,
  `Cubic(0.32, 0.72, 0, 1)`, the faces swapping at 90 degrees. The card's height is the taller face (lay out both faces in a
  `Stack`, the hidden one with `Visibility(maintainSize: true)`). When `MediaQuery.disableAnimations` is set, an
  `AnimatedSwitcher` cross-fades in 120 ms. Haptic: a light tick.
- **Answers.**
  - right: an `AnimatedContainer` to volt plus `ScaleTransition` from 1.04 in 200 ms, with `Haptics.confirm()` after the
    server's grade;
  - wrong: `MmShake(size: 4, cycles: 2, haptic: false)` (A7's `cycles` parameter), with no haptic.
  - The line: `AnimatedSize` (240 ms) plus `FadeTransition`, then `Scrollable.ensureVisible(lineKey.currentContext!,
    duration: 280ms, alignmentPolicy: keepVisibleAtEnd)`.
- **Keep flight.** An `OverlayEntry` ghost (72 x 96 dp) from the card's `RenderBox` to the kept count's `GlobalKey`, 320 ms on
  the same curve (`MmFlight`).
- **Accessibility.** Each page sits in `Semantics(container: true, label: 'Card 3 of 21')`, and every page change calls
  `SemanticsService.announce`. Keys are at least 48 dp.
- **Tablets and Chromebooks** (1024 dp and up): the desktop three-part stage through `LayoutBuilder`. A hardware keyboard gets
  `Shortcuts` and `Actions` for the key table.
- **Performance.** No blur, no backdrop filter. A `RepaintBoundary` per page; PageView keeps one page each side.

### 3.17 Changes this audit proposes to BUILD-1101 Part B (for the main session to accept or reject)

- **A. Desktop pager.**
  - Part B says: two round chevron keys in the control column, `Previous` and `Next`, with tooltips.
  - Proposed: put a labelled "Previous" line key on the left of the action bar instead. The volt key on the right is then the
    only forward key.
  - Why:
    - two "Next" controls (a chevron and the volt key) say the same thing in different places, which confuses a student new to
      computers;
    - tooltip-only labels are hover-only information (std R-092, slop item 14);
    - back and forward under the item is the flashcard convention (3.15).
  - If the pager stays, give both keys a visible 12 px label under the glyph, like the rail keys.
- **B. Skip.** Part B shows nothing in the action bar until a question is answered. Proposed: "Skip" (a quiet key) until the
  answer. Otherwise a phone student who does not swipe has no visible way past a question.
- **C. The turn.** 380 ms in Part B; proposed 340 ms (std R-153; the most repeated motion).
- **D. The streak.**
  - Part B puts it in the top bar on phones. Proposed: in the verdict line on every width ("Right. 4 in a row."), plus the
    panel on desktop.
  - The phone top bar at 360 leaves about 136 px for the title once the counter and kept count are in; a chip would leave about
    44.
- **E. End title.**
  - Part B keeps "10 minutes on {title}".
  - Proposed: the chapter title plus a done line ("All 21 done in 9 min." or "You stopped at 8 of 21."), with the additive
    field `feed.done`. An early stop must not claim ten minutes (research T002).
- **F. Questions are top-aligned.**
  - Part B centres the item. Proposed: centre cards, top-align questions, so the options do not move when the line opens
    below them.
  - Part B's front sizes are kept, with one extra step under 380 px (32 instead of 34 for 60 characters or fewer).
- **G. One definition of "Questions"** on the checkpoint, the panel and the end: plain questions only, with old mistakes on
  their own line (F6).
- **H. No haptic on a wrong answer** (FEED-2 has `vibrate([8, 40, 8])`). The app's haptic grammar says nothing on a wrong
  answer (A7 section 2.7). One rule for both keeps the port simple, and a buzz on a miss reads as a penalty. Keep 8 ms on a
  turn and 12 ms on a right answer.

Agreed as written in Part B:
- the transform pager and its touch numbers;
- the wheel rule, plus deltaMode and the edge-at-start rule;
- the key map, plus `?`;
- the primary key's labels;
- the card fitting its content;
- the source on the front and the prompt repeated on the back;
- the line in place;
- removing the object;
- the Keep flight to the panel pile;
- the loading state at final shape;
- the two-column end on desktop;
- the calm Free stage.

### 3.18 Verification (what proves it; nothing here is measured yet)

1. **Desktop, real mouse** (Chrome, Edge and Firefox on Windows; std 11: real pointer events, not `element.click()`):
   - one notch moves exactly one item;
   - ten notches in a row move at most one per gesture gap;
   - a precision-touchpad swipe moves one;
   - a long question scrolls first and pages only on a new gesture from its edge.
2. **Keys:** every row of the key table. Space on a focused button does not double-act.
3. **Phone** (the owner's phone over the LAN, LK19; real fingers):
   - a slow drag of a third of the screen moves one;
   - a hard fling never moves two;
   - a drag inside a long question scrolls it;
   - pull-to-refresh never fires.
4. **Captures, Night and Day:** 360, 390, 430; 1024x768; 1366x650; 1366x768; 1440x900; 1920x1080. Every state of 3.10, and
   reduced motion.
5. **Run std 11's checks:**
   - `document.elementFromPoint` returns each key at its centre;
   - no horizontal scroll at 360;
   - CLS under 0.1 (rows appearing after the student's own input are excluded);
   - zero console errors (F16).
6. **One volt key per viewport** in every state. The right row's volt fill is a state, not an action (DESIGN.md: volt is the
   correct-answer fill).
7. **Numbers:** the checkpoint, the panel and the end agree for one scripted session (F6).
8. **Budget phone:** a 4x CPU throttle in DevTools, with no dropped frames over 50 ms during a move or a turn.
9. **The leading metric and the guardrail** (research test part 11; define now, wire only with the owner's OK):
   - lead: the share of started feeds that reach the first checkpoint, split by phone and desktop;
   - guardrail: the share of item views over 60 s with no input (stuck), and the question skip rate.
   The desktop stuck share must fall to about the phone's.

---

## 4. Anti-slop test and rubric (this area)

### 4.1 The 12-part acceptance test

| # | Part | Now | Proposed |
|---|---|---|---|
| 1 | Identity with the logo hidden | Partial. Volt, NCERT's serif and the ticks say MockMob; the blurred object and the empty column read as a generic dark Reels copy on desktop. | Pass. The lit card with NCERT's line and its page, the kept pile, the session numbers and the volt keycaps make a study feed no other product has. |
| 2 | One primary action | Fail on desktop (none visible); partial on a phone (none after a turn or an answer). | Pass. One named volt key in every state. |
| 3 | True content | Partial. Invented loading ticks, "10 minutes on" after an early stop, the checkpoint and end disagree. | Pass. Real counts with one definition; the done line. |
| 4 | Hierarchy at first scan | Partial. The item reads first, then nothing says what to do; the chapter is a 13 px caption. | Pass. The item, then the volt key, then the panel. |
| 5 | Intentional composition | Fail on desktop: a 560 px column, a far-corner object, a 668 px card for two lines. | Pass. The three-part stage; the card fits its words. |
| 6 | Typography by role | Partial. Roles are right, but there is one front size and a wrap bug, and the back is 20 px on phones. | Pass. Length-based sizes per width. |
| 7 | Every state | Partial. Loading, error, empty and Free exist; resume, the 409s, Free's options and a failed Keep do not. | Pass (3.10). |
| 8 | Accessible interaction | Partial. Keys hidden, gesture-only on phones, no j, k, Home or End. | Pass. Named keys, the full key map, announcements, 48 px. |
| 9 | No pseudo-evidence | Partial. Invented ticks; the time claim. | Pass. |
| 10 | Motion with a reason | Partial. The drift is decoration, the 600 ms fill lags, the 420 ms turn is over the band. | Pass. |
| 11 | One leading metric plus one guardrail | Fail. None named. | Partial. Named in 3.18, not wired. |
| 12 | What would be better without this | Fail. The object, the hint paragraph, the empty half of the card. | Pass. Each element earns its place; the panel shows only numbers that move with the student's actions. |

### 4.2 The 0/1/2 rubric

| Dimension | Now | Proposed (target) | Note |
|---|---|---|---|
| Task fit | 1 | 2 | On desktop it cannot move on. |
| Information architecture | 1 | 2 | The rail jumps, there is no next step, the chapter identity is weak. |
| Content truth | 1 | 2 | Invented ticks, the time claim, F6. |
| Readable hierarchy | 1 | 2 | |
| Visual specificity | 1 | 2 | Identity carried by the card, its source and the pile, not the object. |
| Accessibility | 1 | 2 | |
| Functional states | 1 | 2 | |
| Trust | 1 | 2 | Calm Free, honest counts. |
| Intentional motion | 1 | 2 | |
| Performance | 1 | 2 if 3.18 item 8 passes, 1 until then | A blurred layer per slot is removed. |
| Responsive integrity | 0 | 2 | Desktop is broken now. |
| Instrumentation | 0 | 1 | Defined, not wired. |
| **Total** | **10 of 24** | **23 of 24 (target, unverified)** | The rubric is an internal checklist, not proof (research); the owner signs off on a live link. |

---

## 5. Decisions note

- **User task.** A 16 to 17 year old CUET Commerce student plays a 5, 10 or 20 minute mix of one chapter's Key cards and
  questions. On a phone it is often one-handed late at night; on a 1366 laptop, with a mouse or a touchpad. The student must
  always see what to do next and be able to stop with what they kept.
- **Alternatives for desktop:**
  1. A bigger centred phone column. Rejected: it keeps the empty sides and the portrait card (LK20).
  2. A short-video stage, portrait, with chevrons at the screen's right edge. Rejected: text is not video, and icon-only arrows
     are hard to discover.
  3. **The three-part study stage. Chosen:** reading width, the session's real numbers beside it, one labelled bar under it.
  4. A side panel for the line. Rejected: a reserved empty column, or the stage moving while the student reads (3.5).
- **Trade-offs.**
  - The panel adds reading on desktop; it holds only numbers that change with the student's own actions, in ink-3 and ink-2.
  - Skip invites skipping. It stays quiet, and the end counts only answered questions.
- **Open questions** (for the main session; none blocks building):
  1. Should questions sit in a card face in both the feed and the run (CRITIQUE-1 asked for one look)? This audit keeps them on
     the canvas in the feed (lighter; the options are the only boxes). If the run keeps its card face, decide one look for
     both.
  2. "This feed" sheet and the phone nudge are P2; ship P1 first.
  3. Optional P3 work:
     - "See the line" after a right answer (needs `answer.line` on right answers and the Free allowance rule, R14);
     - a shared-element move from the Explore cover's Play into the feed.
- **Evidence.**
  - std: R-092, R-093, R-153, R-156, R-006, T-095, T-097, T-130, T-131, slop items 1, 13 and 14;
  - research: T002, T005, S014 (the "This feed" sheet and the Keys list hold secondary functions), S015, S016, S017 and S018
    (slop as missing intent: the decorative object);
  - owner: LK11, LK15, LK19, LK20, LK21, LK23.
- **Verification.** Section 3.18. Show the owner a live link on his phone and on his computer before calling it done (LK19,
  std 11).
