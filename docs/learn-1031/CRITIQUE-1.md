# Learn redesign, critique 1 (taste critic, 31 Oct 2026 night)

**Source:** all 147 captures in `wt-1031-learn-v2/tmp/learn-1031/final/`. I read every 1440 Night shot, most 1440 Day and 390 shots one by one, and the tall 390 home, Find and chapter pages in slices. I judged them against OWNER-FEEDBACK-2026-10-31-LEARN (LK1-LK14), DESIGN-SPEC (B plus A1-A12), the 15-point checklist and the slop list. I also checked the deck data behind the Must-know finding.
**Format:** OWNER-TASTE-PROFILE section 4. Within each area, findings are ranked by what he would notice first.

## Overall verdict: REFINE (good direction, not ready for him)

**Like:**
- The route is literally his LK10 flow: subject loop, chapter map, chapter page, "How long have you got?", piles, then "Start 10 minutes".
- There is one volt key per screen almost everywhere.
- The Key card face with the NCERT book face and page source looks good.
- The "Quick recap" naming is the same on every screen.
- The session end offers real next options, and "moved from Getting there to Holding" is a good line.
- The Start sheet row and Learn second in the tabs both landed.

**What he will say in the first 30 seconds:**
1. "Everything still says Must-know." He named this himself (LK13). It is on every card in every view.
2. The chapter page piles read as three dark stat tiles with a number, not a tangible stack ("close to a form" again).
3. Got it has no visible flight. The card vanishes, the stage is empty, and "In Revise 0" sits in the far corner. He asked for this motion by name (LK5).
4. Counts disagree from screen to screen (24 against 27 due, Find says 9).

Fix these four before he sees anything.

### The first eight he would notice (cross-area)
1. Must-know on about 71% of cards. **Engine, cards, run.**
2. Due counts disagree across screens, and even between Night and Day of the same screen. **Engine.**
3. The piles are flat tiles, not fanned paper. **Chapter.**
4. The Got it flight and Revise pile are invisible or far away. **Run.**
5. The mistake question is a 10-15 line wall, with options below the fold at 390. **Run.**
6. The session end says the same numbers twice. **Run.**
7. The home suggestion cards at 390 are crushed: 4-line titles and 2-line button labels. **Home.**
8. Explore feed: the coach line is hidden under the keys at 390, and there are two volt keys on the lead card screen. **Feed.**

---

## Engine (data, composer, counts)

**E1. [All surfaces > Must-know, every viewport, both themes] REGRESSION (against his explicit ask).**
- **Like:** Must-know shows as a word in the kind line in Cards, Find and the feed.
- **See:** the re-tier overlay (B5) is not applied. In `data/keycards/decks/accountancy.json`, 618 of 868 cards have `importance: 'must'` (71%).
  - Accounting for Partnership: Basic Concepts shows 33 Must-know of 46 cards.
  - Admission of a Partner shows 41 of 53.
  - The Economics suggestion offers "Quick recap: Production and Costs, its 66 Must-know lines" out of 79 cards.
  - Find shows "618 Must-know in 14 chapters".
  - The first screen of the Cards view has Must-know in volt on 4 of 4 rows. The Must-know filter keeps 33 of 46, so the filter barely filters.
  - "Quick recap: the 33 Must-know lines, about 6 min" is not a quick recap.
- **Fails:** #9, #10, A10, B5 ("everything just has a must know mark to it, which makes it kind of weird").
- **Fix:** apply the B5 overlay in the loader that `learnPreview.js` reads (counts at lines 197, 417, 456, 620 all take `x.importance === 'must'`).
  - The target is about one card in four, tops by `asked` then `order`: about 12 for Basic Concepts, 13 for Admission and about 217 for Accountancy.
  - Assert it in a test: share of must per chapter between 0.2 and 0.3, at least 1 per chapter.
- **Like in:** Anki's flagged subset, which is a small set by design.
- **Where to look:** `/preview/arena?view=learn2-cards&chapter=accountancy.partnership-fundamentals&f=must`, and Find shelves.

**E2. [Sidebar "Learn, Key cards" due badge against Find against suggestions, 1440 and 390] REFINE.**
- **See:** the counts disagree.
  - The sidebar shows 24 due on Learn home, chapter, Explore and Practice, but 27 on every Cards view, Quick recap and Find.
  - On the same chapter page, Night shows 27 and Day shows 24.
  - Find's shelf says "Due today 9, about 3 min".
  - The home suggestion says "3 cards due".
  - The 390 dock says "8 due" (Your papers), right next to Learn content.
  - A student reading 24, 27, 9 and 3 for "due" loses trust.
- **Fails:** #10 ("every count agrees"), A12 acceptance ("every count true to the fixture data").
- **Fix:** one `dueAll` source, with the same filter for the sidebar, the Find shelf and the chapter rows. The suggestion stays per chapter but names its chapter (it does).
  - Make the preview student deterministic per `kcs`, so Night and Day of one shot agree.
  - Add a test: the sidebar badge equals Find `due.count` for the same student.
- **Where to look:** `src/lib/server/learnPreview.js` around 615 (`dueAll`) and wherever the arena sidebar badge reads its count.

**E3. [Run composer, the mistake question as item 3] REFINE.**
- **See:** a 10-15 line ordering stem lands third in a 10-minute run. At 390 only option A shows above the fold.
- **Fails:** #3, LK11 ("lines and lines of text").
- **Fix:** in the composer, cap a turn at about 60 words of stem when picking the in-run mistake. If the only open mistake is long, place it last or second-last (A3 says the last item is the likeliest right answer, so second-last) and never before item 5.
- **Where to look:** `learn2-run&kind=mix`, item 3.

**E4. [Content: Basic Concepts deck] REFINE.**
- **See:**
  - Quick recap cards 1 and 2 are near-duplicates ("Define partnership." then "What is partnership?") with different answers.
  - Card 1's source reads "Accountancy Part 1, Ch 2, p. 48" inside the Ch 1 deck.
- **Fails:** #9, #6.
- **Fix:** de-duplicate same-concept cards within a chapter (keep the one that quotes the Act), and check that `source.chapter` matches `chapterKey`.
- **Where to look:** `06-quick-recap-*` and `-next`.

**E5. [Lined-up counts against shelf counts] REFINE.**
- **See:**
  - The pile says "2 Your mistakes" while the shelf row says "3 open" on the same screen, with no reason given.
  - Free shows "5 Questions, about 6 min" while Pro shows "3 Questions, about 3 min", so the rate per question differs.
  - The end screen says "5 questions answered" after a pile of 3 questions plus 2 mistakes.
- **Fix:**
  - When the pile holds fewer mistakes than are open, its minutes line reads "2 of 3, about 2 min".
  - Use one seconds-per-question constant (60 s).
  - The end screen counts mistakes separately from questions ("3 questions, 2 mistakes fixed").
- **Where to look:** `03-chapter-partnership-10-pro`, `-free`, `05-run-end-*`.

**E6. Free preview student and Your papers.** A brand-new Free student shows "Your papers, 8 to revise". If the fixture is global, scope it to the student, or the new-student story (A7) is not true. **Where to look:** `01-home-new-free-*`.

---

## Home (Learn home, nav)

**H1. [Learn home > suggestions, 390, both themes] REFINE.**
- **Like:** three suggestions of three kinds with real evidence lines, and a lead with the volt key.
- **See:** the two small cards are 175 px wide.
  - Their titles wrap to 4 lines ("3 cards due in / Accounting for / Partnership: / Basic Concepts").
  - The key label "Fix them, 10 minutes" breaks onto two lines inside the button.
  - Two of the three suggestions name the same chapter, so the row reads as one long chapter name repeated.
- **Fails:** #7, #11, LK11 ("lines and lines of text").
- **Fix:** at 390, stack the two secondary suggestions as full-width 72 px rows under the lead: a kind word in the label role ("Due", "Fix"), the chapter in one line with ellipsis, the evidence in one line, and a 44 px key on the right with a short label ("Revise", "Fix, 10 min"). Keep the side-by-side layout at 768 and up.
- **Like in:** Revolut's stacked "For you" rows.
- **Where to look:** `01-home-pro-accountancy-390-*`, `01-home-new-free-390-*`.

**H2. [Learn home > subject loop, 390] REFINE.**
- **See:** "English" is cut to "Englis" under the round scroll button, so the fourth object looks broken.
- **Fails:** #11.
- **Fix:** add a 48 px right fade mask on the loop. Put the chevron button over the fade, never over a label, or drop it on touch (the loop scrolls).
- **Where to look:** every 390 Learn shot, and the Practice tab row has the same issue.

**H3. [Learn home > lead suggestion art, 1440] REFINE.**
- **See:** the lead card carries a 60 px grey stacked-paper glyph at the bottom-right, the only art on the card. The chapter page beside it uses the lamp-lit calculator. The glyph is gone at 390.
- **Fails:** #2, #1 ("rich, lamp-lit 3D art").
- **Fix:** use the subject's lamp-lit object at 96 px, lit, top-right of the lead card, at both widths.
- **Where to look:** `01-home-*-1440-*`.

**H4. [Learn home > headings, 1440 and 390] REFINE.**
- **See:**
  - "Learn" (h1) plus "Accountancy" (an equally large h2) plus "Chapters" (h2) stack three display headings before the first chapter.
  - At 390 the subject heading disappears and only the count line remains.
  - "Economics / Business Economics" uses a slash.
  - "Retirement/Death of a Partner" uses a slash where the book says "and".
- **Fails:** #7, A10.
- **Fix:** drop the "Accountancy" h2 at 1440 and put "868 Key cards, 15 chapters, 4 lessons" under the selected object's label. Write "Economics, Business Economics" or just "Economics". Use the NCERT chapter title, "Retirement and Death of a Partner".
- **Where to look:** `01-home-pro-economics-1440`, the 390 map.

**H5. [Learn home > foot of the map, 390] REFINE.**
- **See:**
  - An empty bordered row, then a second hairline, then "Study plan" and "Your record" as underlined text links.
  - Under them, about 500 px of empty page.
  - "Computerised Accounting System" reads "No Key cards yet." with "Needs work" under it.
- **Fails:** #7, #11.
- **Fix:**
  - Remove the empty row.
  - Make the foot two 44 px pressable rows with an icon and a one-line reason ("Study plan, 3 chapters a week"; "Your record, 46 cards in Revise").
  - Trim the bottom padding to dock height plus 24 px.
- **Where to look:** `01-home-pro-accountancy-390-*`, the last slice.

**H6. [Nav > sidebar "Learn, Key cards", 1440] REFINE (LK1 is only half met).**
- **Like:** Learn second, with the due count.
- **See:** it is still a 13 px indented sub-row under Practice, the same size as "Saved". He said the way in was "very small". The N1 alternate fixes the size but pushes Ask Mobi and the theme switch off a 900 px screen.
- **Fails:** #15, LK1.
- **Fix:**
  - Default: give the Learn sub-row the parent row's 15 px weight and a 2 px volt left tick when it has due cards.
  - N1: tighten the "You" group spacing by 4 px per row, or collapse "Wallet, Guide, Show me around" behind "More", so the theme switch shows at 900.
- **Where to look:** `08-nav-sidebar-*`, `08-nav-n1-alternate-sidebar-1440-night`.

**H7. [Nav > Start sheet "Learn a chapter", 390 and 1440] REFINE.**
- **See:**
  - The row uses a flat document glyph between the stopwatch and NTA art.
  - Its copy ends "Free." while every row around it says "Included with Pro" for a Pro student.
  - "Set up" opens Learn rather than starting.
- **Fails:** #2, #10, A7 ("each suggestion key starts at once").
- **Fix:**
  - Use the lamp-lit subject object.
  - Copy: "Key cards and questions on one chapter, 5 to 20 minutes" plus "Included" in the same style as its neighbours.
  - Key: "Pick a chapter" (honest, since it opens the map).
- **Where to look:** `08-nav-start-sheet-*-learn-row`.

---

## Chapter page

**C1. [Chapter > the piles, 390 and 1440, both themes] REFINE (the screen's whole idea).**
- **Like:** the order: time, then piles, then "Start 10 minutes", then "Ratings join Revise. Questions are free.", then the quick recap. The left-out state ("Left out / Tap to put back") with counts that re-balance (16 to 24, 4 min to 7 min) is right.
- **See:** each pile is one dark rounded tile with a ghost outline behind it. The rotation (-4, 0, 3 degrees) is not visible, the papers do not fan, and the count sits on an empty face with a tiny icon. At a glance these are three stat cards, not things you pick up. Nothing says they are tappable except a volt-coloured coach line.
- **Fails:** #2, #4, #5 ("it should never look like just a basic form"; A1 "tangible piles").
- **Fix:**
  - Draw 3 papers per pile at rotate(-4deg), rotate(0deg) and rotate(3deg), offset 3-5 px, each with the 1 px hairline.
  - Put a faint content hint on the top paper: two 1 px text lines for Key cards, four option dots for Questions, a red margin tick for Your mistakes.
  - Hover and focus lift the pile 3 px with the hairline brightening (150 ms ease-out).
  - Active: scale 0.98.
  - Add a small "In" or "Left out" toggle mark top-right of each pile, so the tap affordance is on the object, not only in the coach line.
  - The coach line goes to the secondary ink, not volt, so the Start key is the only volt on the page.
- **Like in:** Apple Wallet's stacked passes, and the Practice "Ways to practise" cards he praised.
- **Where to look:** `03-chapter-partnership-10-pro-*`, `03-chapter-pile-left-out-*`.

**C2. [Chapter > Admission at 20 min, four piles, 390] REFINE.**
- **See:**
  - With four piles each tile is about 75 px wide.
  - "Your mistakes" wraps to two lines while the others take one, so the labels do not align.
  - The Lesson pile has no fan at all (one flat tile), so it reads as a different control.
  - About 300 px of empty page sits under the shelf.
- **Fails:** #7, #11.
- **Fix:**
  - At 390 with four piles, use a 2 x 2 grid of piles (each about 170 px), or shorten the label to "Mistakes" on narrow widths with the full name in aria-label.
  - Give Lesson the same 3-paper fan (with a book-spine edge as its hint).
  - Trim the bottom space.
- **Where to look:** `03-chapter-admission-20-pro-lesson-390-*`.

**C3. [Chapter > Free variant, 1440 and 390] REFINE.**
- **See:** under the volt key there are four separate text lines:
  - "Free opens 5 of this chapter's 46 cards. This chapter has enough for about 9 minutes today."
  - "Add the next chapter, Profit and Loss Appropriation Account"
  - "Ratings join Revise. Questions are free."
  - "Or a quick recap: the 5 Must-know lines, about 1 min"

  The time control still shows "10 min" selected while the key says "Start 9 minutes". The Key cards shelf row packs four facts into a wrapping line ("46 cards, 5 open on Free, 33 Must-know, 5 in Revise").
- **Fails:** #7, LK11 ("an overload of information").
- **Fix:**
  - Fold the Free and enough-for lines into the Key cards pile's minutes line ("5 open on Free").
  - Make "Add the next chapter" a fourth, dashed "+" pile ("Next chapter, +4 min") instead of a text link.
  - Keep exactly one quiet line under the key.
  - When the pool caps the time, the thumb's label reads "9 min".
  - The shelf meta takes two facts at most ("46 cards, 5 open on Free").
- **Where to look:** `03-chapter-partnership-10-free-*`.

**C4. [Chapter > title block, 390 and 1440] REFINE.**
- **See:**
  - The eyebrow "Accounting for Partnership" repeats the first three words of the title "Accounting for Partnership: Basic Concepts".
  - The state dot "Getting there" is a grey dot here but a half-ring on the map.
- **Fails:** #10.
- **Fix:**
  - When the unit name is a prefix of the title, show the eyebrow as "Accountancy, Part 1".
  - Use the same ring glyph as the map row.
- **Where to look:** `03-chapter-partnership-10-*`.

**C5. [Chapter > layout shift on load, 390] REFINE.**
- **See:** CLS 0.10-0.17 in the first 1.2 s. The piles and the shelf arrive after the title, so everything below jumps.
- **Fails:** #11, DESIGN-SPEC acceptance ("no layout shift").
- **Fix:** render the time control and three placeholder piles at their final size (pile 160 x 128 at 390) from the first paint. Keep the Start key's slot reserved at 52 px.
- **Where to look:** `03-chapter-*-390`.

**C6. [Chapter > 1440 composition] REFINE.**
- **See:** the left column ends at about 790 px. The right "In this chapter" panel is a boxed card while the left is open page, so the two columns have different weights. The lower 40% of the screen is empty.
- **Fix:**
  - Drop the box on the right panel (hairline rows on the page, as at 390), or box the lined-up block too.
  - Raise the piles to 160 px tall so the lined-up block fills the first screen as B intended.
- **Where to look:** `03-chapter-*-1440-*`.

---

## Run (player, end, Quick recap player, Explore feed)

**R1. [Run > Got it flight, 1440 and 390] REGRESSION against his one praised ask (LK5).**
- **Like:** the "Back Tue" stamp uses the server's real date.
- **See:**
  - At 40 ms the card has only shrunk slightly in place.
  - At 150 ms the stage is empty except the deck edge. No card is in flight and no next card is rising.
  - "In Revise 0" has not ticked.
  - At 1440 the pile sits at the far bottom-right of the window, about 700 px from the card, so even a working flight would cross half the screen away from the keys.
  - The stamp is a tilted outlined chip above-left of the keys, not under them, and the first-run coach line stays on screen next to it.
- **Fails:** #12 ("motion must be beyond Duolingo"), A4.
- **Fix:**
  - Put the Revise pile 16 px right of the rating row (1440) or right-aligned just above it (390, as now), never in the window corner.
  - Flight: lift 4 px and scale 0.96 (100 ms), then translate along a two-segment arc to the pile with scale to 0.18 and opacity to 0 (320 ms, cubic-bezier(0.32, 0.72, 0, 1)).
  - Start the next card's 8 px rise at 220 ms, so there is never an empty frame.
  - Pop the pile count at 1.12 (180 ms) when the flight lands.
  - The stamp line sits centred under the keys and replaces the coach line while it shows.
  - Capture frames at 0, 120, 260 and 420 ms to prove it.
- **Like in:** Apple Mail's swipe-to-archive flight into the toolbar.
- **Where to look:** `04-run-gotit-flight-*` and `-stamp`.

**R2. [Run > mistake MCQ, 390 and 1440] REFINE.**
- **See:**
  - The stem is a single 10-15 line paragraph with the four steps (A) to (D) inline. At 390 the screen is all stem, with option A at the fold and B to D under the fixed footer.
  - The question sits as plain text on the page, while the feed shows the same kind of question inside a card face.
  - The mistake label is amber "Your mistake, from Mock 3" here but "You missed this in Mock 4 on 24 Oct" in the feed.
- **Fails:** #7, #10, LK11.
- **Fix:**
  - When a stem contains "(A) ... (B) ...", render the steps as a numbered list with 8 px gaps.
  - Put run questions in the same card face as the feed (one look for every question).
  - One label everywhere: "You missed this in Mock 3 on 16 Oct".
  - See E3 for placement.
- **Where to look:** `04-run-mcq-*`, `04-run-fixed-mistake-*`.

**R3. [Run > wrong answer and "the line you needed", 1440 and 390] REFINE.**
- **Like:** the explanation clipped with "More". The NCERT line in the book face with its page. "This card comes back later in this run."
- **See:**
  - The view auto-scrolls so the student's own wrong pick (A) is off screen; only the right answer B is visible.
  - The block says "Here is the NCERT line you needed." and then "The line you needed": two headings for one thing.
  - The verdict copy is "Not quite. The answer is B." here and "Not this one. The answer is B." in the feed.
  - The explanation column is about 500 px inside a 640 px column.
- **Fails:** #10, A11.
- **Fix:**
  - Scroll so the picked option is the top row in view.
  - Drop the coach sentence when the heading is present (or show the coach once as the heading itself).
  - One verdict string: "Not quite. The answer is B."
  - Explanation at full column width.
- **Where to look:** `04-run-wrong-line-*` and `-bottom`, `07-feed-question-wrong-*`.

**R4. [Run > "Fixed" moment, both widths] REFINE.**
- **See:** fixing a mistake from a mock (the best moment in the run) is one line with a small check icon, the same weight as any text.
- **Fails:** #8, #12 ("Mobi reacting on where your marks go was good").
- **Fix:**
  - The line rises 8 px with a volt check that draws in 200 ms.
  - A small Mobi nod at 40 px appears beside it for 900 ms.
  - "Fixed" is in the success ink, bold.
  - Reduced motion: static.
- **Where to look:** `04-run-fixed-mistake-*`.

**R5. [Run > player frame, 1440] REFINE.**
- **See:**
  - All content sits in the top 600 px. "Up next" floats at the top-right, and the Revise pile floats at the bottom-right corner, so the eye has three unrelated corners.
  - On the fixed-mistake and wrong shots the Next key touches the bottom edge of the 900 px window and is cut.
  - The progress line is one bar, not the volt pips B asks for.
  - The card's "Must-know" is a boxed chip (`KeyCard.jsx` line 173, `kc-tag`), unlike the plain word elsewhere.
- **Fails:** #11, #10, A10 ("no box").
- **Fix:**
  - Centre the card vertically in the stage (max 640 px column), with "Up next" as one quiet line under the progress bar.
  - Keep 24 px under the last key (scroll the stage, not the key off screen).
  - Pips grouped by kind.
  - Render Must-know as volt text with no border in `kc-tag` for every surface (this file is shared, so coordinate with the cards owner).
- **Where to look:** `04-run-card-front-1440-*`, `04-run-fixed-mistake-1440-*`.

**R6. [Session end, 390 and 1440] REFINE.**
- **Like:** the numbers row. The Revise fan "14 back on Tue, 2 back in 20 days". The state-moved line. The dynamic next options.
- **See:**
  - The table repeats the numbers row line for line: "16 cards rated" then "Cards 16 got it", "5 questions answered" then "5 of 5 right", "2 mistakes fixed" then "2 of 2 fixed."
  - Only one table row ends with a full stop.
  - Mobi is the same static pose on a perfect Pro run and on the Free run.
  - At 1440 the middle option ("Fix 2 open mistakes") has a filled background the others lack.
  - There is no visible "Back to the chapter" without scrolling.
  - Free says "9 minutes on" after the student chose 10.
- **Fails:** #7, #8, #10.
- **Fix:**
  - Keep the numbers row and replace the table with one line of detail under each number ("16 got it", "5 of 5 right", "2 of 2").
  - Mobi plays the nod on a run with 80% or more right, and "thinking" when 3 or more cards are missed.
  - The three options get the same treatment, with hover only on pointer hover.
  - Add "Back to the chapter" as a 44 px text button under the options, inside the first screen at 1440.
- **Where to look:** `05-run-end-*`.

**R7. [Quick recap player, 390 and 1440] REFINE.**
- **See:** the recap card shows "Due today", which means nothing in a pass where nothing is scheduled. Previous and Next carry chevrons appended to the label.
- **Fails:** standards (no arrows appended to button text), #9.
- **Fix:** hide the due meta in `last_look` mode, and use plain "Previous" and "Next".
- **Where to look:** `06-quick-recap-*`.

**R8. [Explore feed, 390 both themes] REFINE.**
- **See:**
  - The coach line "Tap the card to see the NCERT line..." is half covered by the Show answer and Keep/Next keys, and it stays after the answer is revealed.
  - The feed keeps the Explore tab row and the dock at 390, so the card gets about 60% of the screen and the dock's Start key competes with the feed's keys.
  - At 1440 the Show answer key sits about 290 px below the card.
- **Fails:** #11, #4, #3.
- **Fix:**
  - The coach line sits between card and keys with 12 px clearance and hides on reveal.
  - The feed is a focus page like the run: no tab row, no dock, a Close at the top.
  - At 1440 the keys sit 24 px under the card.
- **Where to look:** `07-feed-card-front-*`, `07-feed-card-revealed-*`.

**R9. [Explore > lead card, 390 and 1440] REFINE.**
- **Like:** "Run this chapter as a feed" with the real mix ("16 Key cards and 5 questions, one at a time").
- **See:**
  - At 1440 the sidebar's volt "Start a session" sits beside the volt "Start the feed". At 390 the dock's volt Start does the same: two volt keys on one screen.
  - "5 min" and "20 min" are small underlined links under 44 px.
  - The question list below labels the same chapter "Partnership Fundamentals", not its title.
  - The card loads late and pushes the list down (CLS 0.13).
- **Fails:** #3, #10, #11.
- **Fix:**
  - Quiet the sidebar and dock Start while the lead card's key is on screen (W-075).
  - Make the lengths a small 3-way segmented control (5, 10, 20) at 44 px, with the key label following ("Start the feed, 10 minutes").
  - Use the chapter title in the Explore filter label.
  - Reserve the lead card's height from first paint.
- **Where to look:** `07-explore-lead-card-*`.

---

## Cards (Cards view, Find)

**K1. [Cards view > rows, 1440 and 390] REFINE (after E1 the screen changes a lot).**
- **Like:** answers folded behind "Show". Sections with counts and a sticky jump list at 1440. The open row with source, "Study this card" and "In Revise".
- **See:**
  - Every row's kind line is "Definition / Must-know (volt) / In Revise / Missed lately", so the eye reads a column of volt words, not the questions.
  - Folded rows are about 100 px tall with one line of text, so a 46-card chapter is still a long scroll of text.
- **Fails:** #7, LK4, LK11.
- **Fix:**
  - After E1, Must-know shows on about 1 row in 4.
  - "In Revise" becomes a 6 px dot before the kind word, not text.
  - "Missed lately" stays as text in the error ink.
  - Folded row height 64 px.
  - The open row is drawn on the card face surface (the same paper as the player), so opening a row feels like turning a card over.
- **Where to look:** `06-cards-all-folded-*`, `06-cards-row-open-*`.

**K2. [Cards view > filter control, 390] REFINE.**
- **See:**
  - The four filters wrap into a 2 x 2 boxed grid.
  - The selected "All 46" has a volt outline.
  - With "Show answers" on in Day, the toggle is solid volt.
  - With the volt "Study these 46", that makes three volt marks in the first screen. It reads like a settings form.
- **Fails:** #5, #3 ("one volt key per screen").
- **Fix:**
  - At 390, make the filters a single horizontally scrolling row of chips with one sliding indicator, selected in the ink fill (not volt).
  - The switch "on" uses the ink colour.
  - Volt stays only on the Study key.
- **Where to look:** `06-cards-*-390-*`.

**K3. [Cards view > sticky section bars, 1440] REFINE.**
- **See:** scrolled, two sticky bars stack ("Introduction 1" over "1.1 Nature of Partnership 13").
- **Fix:** one sticky slot. The next section bar pushes the previous one up (`position: sticky; top: 64px` on every bar, inside per-section containers, so each releases at its section's end).
- **Where to look:** `06-cards-row-open-1440-*`.

**K4. [Cards view > pick checkboxes, 1440] REFINE.**
- **See:** the 20 px checkboxes hang in the gutter, outside the column's left edge, on some rows only (hover and focus), so the left edge looks ragged.
- **Fix:** reserve a 28 px pick column inside the row grid. The box fades in (120 ms) on hover and focus without moving the text.
- **Where to look:** `06-cards-row-open-1440`, `02-find-goodwill-pro-1440`.

**K5. [Cards view > load shift, 1440] REFINE.**
- **See:** CLS 0.28 on every Cards shot (0.33 once).
- **Fix:** skeleton section list and 6 rows at final height. Render the filter counts from the chapter row already in cache.
- **Where to look:** `06-cards-*-1440`.

**K6. [Find > shelves, 1440] REFINE.**
- **See:**
  - Four big numbers with plain outlined buttons under them, in a row, then 280 px of empty page. It reads as a stats table, not "a place that shows what is where".
  - The sub-line reads "last 14 days" (B says 7).
  - "618 Must-know" (E1).
- **Fails:** #2, #15, LK10 ("easily shows them what to find where").
- **Fix:**
  - Draw the four shelves as the same paper piles as the chapter page (count on the top paper, label and line under, the whole pile the button), so Learn has one visual idea.
  - Under them, a short "By chapter" list (chapter name, due, in Revise) so the empty half carries useful content.
- **Where to look:** `02-find-shelves-*`.

**K7. [Find > results "goodwill", 1440 and 390] REFINE.**
- **Like:** the highlighted match in the line.
- **See:**
  - Results show the NCERT answers open, though A5 says Find keeps answers folded.
  - The header says "1 chapter, 50 cards", the chapter row "39 cards" and the group "27", three numbers for one search.
  - The chapter name appears twice in a row.
  - The highlight draws a boxed background plus underline on every hit (heavy at 390).
- **Fails:** #10, A5.
- **Fix:**
  - Fold answers, showing the match in the front, and the quote only if the match is only in the quote.
  - Header: "27 cards in 1 chapter" with the chapter row as the group header.
  - Highlight with underline only, 2 px volt-dim.
- **Where to look:** `02-find-goodwill-pro-*`.

**K8. [Cards view > Free, 1440] REFINE.**
- **See:** the header says "5 cards", so a Free student never sees that the chapter has 46. The "41 more cards" Pro row from B is not visible in the first screen.
- **Fix:**
  - Header: "46 cards, 5 open on Free".
  - The locked row sits in book order where the first locked card would be, with one quiet "See Pro" (no volt).
- **Where to look:** `06-cards-all-free-*`.

---

## Not verified by these captures (needs a capture or a check before the owner sees it)
- Reduced motion for the flight, the piles and the count roll. No `prefers-reduced-motion` captures exist.
- The count roll (180 ms) and fan re-spread (220 ms) when the length changes. There are only end-state frames.
- The short screen recording of the first 6 items of a 10-minute run at 390 Night (DESIGN-SPEC acceptance).
- The A11 coach lines showing once only: the second-visit captures are missing.
- Focus rings on piles and filter chips, with keyboard only.

## Owners
- **Engine:** E1-E6. E1 and E2 block the owner review.
- **Home:** H1-H7.
- **Chapter:** C1-C6. C1 blocks.
- **Run:** R1-R9. R1 blocks.
  - The R5 `kc-tag` change is in shared `src/components/keycards/KeyCard.jsx`; coordinate with Cards.
  - R8 and R9 are in `learn2/feed`.
- **Cards:** K1-K8.
