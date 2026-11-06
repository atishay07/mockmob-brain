# Learn, final design spec (CTO decision, 31 Oct 2026 evening)

**Base:** `design/B-chapters.md` ("the chapter is the home"), chosen by both judges (`design/judge-1.md`, `judge-2.md`) as the
literal route of the owner's LK10 flow. Build B exactly as written **except where an amendment below says otherwise**.
Amendments take ideas from `design/A-composer.md` and `design/C-two-lanes.md`. B1-B8 (bar frozen, one Learn, Study kept,
Last look folded, Must-know re-tier, watermark, 5/10/20/own, Free taste) still hold.

## Amendments to B

**A1. The chapter page's lined-up block uses live piles, not a chip row and a sentence** (A's idea; fixes "close to a form").
- Row 1, length: one segmented control `5 min | 10 min | 20 min | Your own`, one sliding thumb (N5), 48 px tall.
- Row 2, the piles: up to four tangible piles side by side, each a small fan of 2-3 paper cards drawn in CSS (not images),
  in the Night/Day card surfaces with a 1 px hairline, slightly rotated (-4, 0, 3 degrees). On each pile: the count in large
  tabular numerals, the label under it, the minutes under that:
  `16` / `Key cards` / `about 4 min`, `5` / `Questions` / `about 6 min`, `2` / `Your mistakes` / `about 2 min`, and only at 20+
  minutes with an unread lesson: `1` / `Lesson` / `7 min`. Piles with 0 items are not drawn.
- Tapping a pile leaves it out: it dims to 35%, its count is replaced by "Left out", the others re-balance their counts to
  keep the length (the composer's dry run), and at least one pile must stay in (the last one cannot be left out; it shakes
  4 px once). First visit only, one coach line under the piles: "Tap a pile to leave it out." "Cards only" = Questions and
  Your mistakes left out. There is no separate Mix control.
- Counts roll to their new values in 180 ms when the length or piles change; the fan re-spreads in 220 ms.
- The volt key: `Start 10 minutes` (always names the length). Under it, one quiet line: `Ratings join Revise. Questions are free.`
- Under that, a secondary text button (not volt): `Or a quick recap: the 12 Must-know lines, about 3 min`. It starts the recap
  (answers showing, one at a time, nothing scheduled, mode last_look).

**A2. One name for Last look's job: "Quick recap"**, everywhere (chapter page text button, Cards view action
"Quick recap these 12", session end option "Quick recap of this chapter, 3 min"). The words "Flip through" and "Last look"
are not used anywhere.

**A3. Order inside a run (learning-science fixes from judge 2).**
- An open mistake is retried as a question BEFORE its line is shown. Right: "Fixed. You missed this in Mock 3 on 16 Oct." and
  the line you needed shows collapsed under it ("See the line"). Wrong again: the explanation, then "The line you needed" open,
  and its card re-inserted 3 items later.
- A question linked to a card in this run is placed 3 to 6 items after that card, never straight after it.
- The first item is a card; the last item is the question with the best chance of a right answer (B 4.3 rule kept).

**A4. Got it flies into a Revise pile with the real return day** (A's idea, replaces B's flight into a pip).
- The player has a small Revise pile at its bottom-right (a 36 px stacked-card glyph with the run's count, "In Revise 4").
- Got it: the card lifts 4 px and scales to 0.96 (100 ms), then flies along a gentle arc into the pile while shrinking and
  fading (320 ms, cubic-bezier(0.32, 0.72, 0, 1)); the pile's count ticks up with a 1.12 pop (180 ms); a stamp line under
  the rating keys reads the server's real next date: "Back Tue" when within 7 days, else "Back in 12 days" (900 ms).
- Easy: the same, 280 ms, stamp "Back in 9 days". Missed: tilts -3 degrees and slides down behind the deck edge (260 ms),
  stamp "Back later in this run". The next card rises 8 px into place (240 ms).
- Session end fans the Revise pile open with grouped return days: "6 back on Tue, 3 back on Fri, 2 later today".
- Reduced motion: cross-fades (120 ms), the stamp as plain text for 1.5 s.

**A5. Find and the chapter's Cards view keep answers folded** (C's idea: self-testing in the revise place).
- Each row shows the kind line and the front; the NCERT line is folded behind "Show" on the row. A switch at the top,
  "Show answers", opens all. Tapping a row opens it in place (B's open row with source, In short and its actions).
- Filters: All, Must-know, In Revise, Missed lately. The filtered set's actions: `Quick recap these 12` (one at a time,
  answers showing, nothing scheduled) and `Study these 12` (Study mode, ratings). One volt key at a time: Study these.

**A6. The Explore chapter feed asks for a tap, not a rating** (C and A).
- A card item shows its front; tap the card (or Space) to see NCERT's line; a `Keep` key adds that card to Revise
  (Pro; Free within its 5 open cards). Nothing is scheduled unless kept. Swipe up (or Next) at any time: no forced rating.
- Questions are answered in place with the line you needed on a wrong answer (as in a run).
- It is bounded: 10 minutes by default (5 and 20 offered on the lead card) and ends with the session end screen.
- Feed answers log with flow_context 'learn'.

**A7. Suggestions on Learn home: always three, of three different kinds**, each with one line of evidence (C's rule,
asserted by tests over new, returning, Free and thin fixtures).
- Kinds: Pick up (an unfinished run), Due (due cards in a chapter), Fix (open mistakes), Next (next chapter in book order),
  Start (a new student's first chapter), Level (Find your level), Recap (only after the chapter was studied before).
- New student: `Start with Accounting for Partnership: Basic Concepts` / "Chapter 1 of your Accountancy book. 10 minutes of
  its Key cards and questions." [Start 10 minutes]; `Find your level` / "6 questions from your first chapters, about
  6 minutes."; `Search any card` / "868 Accountancy cards, by term or line." Never a recap of an unseen chapter.
- Each suggestion key starts at once (no pre-fill step).

**A8. Navigation (no owner approval needed):** Practice tab row and app doors put Learn second (Practice, Learn, Your papers,
Explore, Saved / Practise | Learn | Your papers); the web sidebar's first Practice sub-row is "Learn, Key cards" with the
due count; the Start sheet gains the one row "Learn a chapter" (B 2.2); Today gains one Learn move in its alternatives;
"The line you needed" on results gains "Open {chapter}"; Review's chapter rows say "Learn this chapter, 10 minutes".
B's N1 (Learn as its own desktop sidebar place) is drawn as an alternate render for the owner's call, not built as default.

**A9. Money and limits:** questions inside Learn runs and the Explore feed are free, untimed and unscored, on the same
footing as Explore today (put to the owner as reversible). Cards keep the Free taste (5 open per chapter) and the 10 ratings
a day; after the 10th, cards show as looks with one line and no modal. The first Pro sheet appears only at a real limit (D181).

**A10. Copy:** B's vocabulary (Learn, Key cards, lesson, questions, Revise, Must-know). Sentence case; no middle dots in
strings; 12-hour times; no exclamation marks; no "mastered", no mastery percent. Must-know shows as the word in the kind
line, volt text, no box, on about one card in four.

**A11. First-run coach lines, once each, never again after:** player first card: "Say the answer in your head, then show it.";
first rating: "Got it sends the card to Revise. It comes back when it is due."; first wrong answer: "Here is the NCERT
line you needed."; piles: "Tap a pile to leave it out."

**A12. Instrumentation (when usage-data consent is given):** time from opening Learn to the first item on screen; runs that end
over 125% of the chosen time (guardrail); per item kind, median seconds (to recalibrate 15 s and 60 s).

## The first slice (real renders for the owner, website, before any app work)
Built for real (components, the pure composer and suggestion engine with tests), shown through the development preview
with the real decks, the Must-know overlay and real questions (`data/fixtures/learn-preview-questions.json`), not wired to
production routes yet. Screens, each at 390 and 1440, Night and Day:
1. Learn home, Chapters: returning Pro (Accountancy), new Free student.
2. Learn home, Find: shelves and search results for "goodwill".
3. Chapter page: Accounting for Partnership: Basic Concepts at 10 min; Admission of Partner at 20 min with the lesson pile;
   the Free variant; a pile left out.
4. Session player: card front, card revealed, Got it flight frames, an MCQ, a wrong answer with the line you needed, a retried
   mistake marked Fixed.
5. Session end with the Revise pile fanned.
6. Cards view: grouped by section, answers folded, one row open, the Must-know filter with Quick recap; Quick recap one at a time.
7. Explore feed: the lead card in Explore and one feed card, one feed question.
8. Navigation: the Practice tab row at 390, the sidebar at 1440, the Start sheet row; plus the N1 alternate sidebar.
Plus a short screen recording of a 10-minute run (the first 6 items) at 390 Night.

Acceptance before he sees anything: the 15-point taste checklist and the slop list on every capture, a real-pointer click
through the run, no layout shift, reduced motion checked, every count true to the fixture data.
