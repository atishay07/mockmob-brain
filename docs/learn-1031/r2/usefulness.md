# Learn v2, round 2: usefulness and logic (LK33)

1 Nov 2026. Lens: is every feature useful, is the next action always clear and dynamic (LK11), what is confusing or a dead end, and what would bring a student back every day. I walked it twice:

- **(a) a first-time Free student** with no history (fixture `student=new&plan=free`);
- **(b) a returning Pro student two weeks before CUET** (fixture `student=commerce&plan=pro`, with an exam date assumed).

Images are in `tmp/learn-1101/r2-before/`. The code I read: `src/lib/server/learn.js`, `data/learn/{suggest,compose,allowance,seconds}.js`, `data/chapter_state.js`, `src/components/learn2/**` and `data/keycards/decks/*`.

## The one-paragraph diagnosis

Learn has strong parts: the composer, Key cards, the line you needed, honest minutes, and the Free rule. What it lacks is a **spine**. Nothing tells a student where they are in the subject, and nothing tells them what "done" looks like for a chapter.

So every screen fills the gap with choices of equal weight:

- three suggestion cards;
- three count keys;
- a search field;
- a 15-row map whose state words ("Too few answers", "Getting there") measure question accuracy, not progress.

The result is "Start with…", then "Next in the book", then a jump to the next chapter after one third of the current one. Nothing ever says "you are on chapter 2 of 15, 31 of 53 cards seen, keep going".

The owner's LK27 ("Start learning…", "Your roadmap") is the right fix, and it is a logic change before it is a layout change. Items 1-5 build that spine. Everything after them hangs off it.

---

## Ranked list (value / effort)

### 1. A roadmap hero is the first thing on Learn home: one offer, never a row of numbers
- **Surface:** Learn home, both students.
- **What is wrong:**
  - 87 / 86-full (first-timer): the screen goes subject objects, then the search field, then the line "Nothing in Revise yet. Cards you study land here.", then three big cards of equal weight ("Start with…", "Find your level" with a ghost key that reads as disabled, "As a feed"), then 15 rows.
  - 88-full (returning): it leads with "9 due today / 6 missed lately / 26 in Revise", then "Pick up…", "3 cards due in…" and "Fix them…".
  - Nothing says where the student is in the book.
- **Why it matters:**
  - LK27 word for word: a straight offer to start learning, and never a status line.
  - LK11: the next action must be clear and dynamic.
  - A 16-year-old new to CBT cannot rank three cards. They need one key and one sentence of why.
- **Exact fix (layout, top to bottom under the subject loop):**
  - Roadmap hero. It is the only card on the page, with no nested card inside it. 20px padding, radius 20.
    - Label line, 15px ink-2: `Accountancy roadmap`
    - Title, 28/32 bold, by mode:
      - new: `Start learning Accountancy`
      - continue: `Keep going with Accountancy`
      - final: see item 6
    - One line, 16px ink-1:
      - new: `Chapter 1 of 15 · Accounting for Partnership: Basic Concepts`
      - continue: `Chapter 4 of 15 · Admission of a Partner · 31 of 53 cards seen`
    - Route strip: one node per chapter in book order, 8px dots, 6px gap, a single row. Done chapters are volt-filled. The current chapter is a 12px volt ring. Not started is ink-3.
      - On a phone, 15 nodes fit in 15 × 14px = 210px.
      - Tapping the strip scrolls to the chapter map (300ms, ease-out).
    - The key: 56px, full width, volt.
      - new: `Start chapter 1, 10 min`
      - continue: `Continue, 10 min`
      - an unfinished run younger than 24 h: `Pick up where you stopped, 5 min`
    - Under the key, a 15px link: `Pick another chapter`. It scrolls to the map.
  - Then at most two secondary rows (52px, icon + text + chevron, no card). Each is drawn **only when its count is above 0**:
    - `9 cards due · about 2 min`
    - `Fix 6 open mistakes · about 6 min`
  - Then the search field. A first-timer does not need search before they have learned anything.
  - Then the chapter map.
- **Motion:**
  - On entry, the strip's nodes fill left to right: a 24ms stagger, 180ms each, ease-out.
  - The current node grows once, scale 1, 1.15, 1, over 400ms. It never loops.
  - With reduced motion, all of this is static.
- **Server:** GET `/api/learn/subject` returns a new `roadmap` object:

  ```
  {
    mode: 'new' | 'continue' | 'next' | 'final' | 'freeDone',
    position: { chapterKey, index, of },
    seen: { cards, of },
    chapters: [{ key, seen, of }],
    action: { label, run }
  }
  ```

  It is built by a pure `data/learn/roadmap.js` from the same `chapterInfo` rows. `suggestions()` drops to two secondary kinds (due, fix), so the hero owns pickup, start and next.
- **Files:**
  - new: `data/learn/roadmap.js` and `data/learn/roadmap.test.mjs`
  - `src/lib/server/learn.js` (the subject read, ~l.528)
  - `data/learn/suggest.js` (the order)
  - new: `src/components/learn2/home/RoadmapHero.jsx`
  - `LearnHome.jsx` (order l.289-317)
  - `Suggestions.jsx`, `learn-home.css`
  - `docs/brain/learn-1031/API-CONTRACT.md`

### 2. Stay in a chapter until its cards are seen once; do not jump to the next one after a third of it
- **Surface:** the run end, and Learn home's "next" suggestion.
- **What is wrong:**
  - 55-run-end: the student saw 16 of 46 cards, and the lead is `Next: Profit and Loss Appropriation Account`. `endOptions()` leads with the next chapter unless `missed >= 3` (suggest.js `if (missed >= 3 || !nextOpt)`).
  - On home, `make.next()` picks "the first unstarted chapter after the latest activity". Chapter 1, with 30 unseen cards, is never offered again. It only comes back as a 24-hour pick-up, and only if the run was left unfinished.
  - The composer serves Must-know cards first, so the 30 cards left behind are exactly the ones never shown.
- **Why it matters:** a roadmap is meaningless if the app itself abandons chapters. It is also the main reason a returning student has "nothing to do" except chase numbers.
- **Exact fix:** add a `continue` kind.
  - The chapter of the latest Learn activity that still has 3 or more **unseen open** cards continues. Unseen means no `key_card_states` row and no feed show.
  - Copy:
    - home hero: `Keep going with Accounting for Partnership: Basic Concepts · 30 new cards left`
    - end lead title: `30 new cards left here`, key `Next 10 minutes here`
    - second option: `Next chapter: Profit and Loss Appropriation Account`
  - Below 3 unseen open cards, `next` behaves as today.
  - Free's open set is the 5 taste cards, so Free moves on after 5 cards. That is correct, and it needs no special case.
- **Files:**
  - `data/learn/suggest.js` (`make.continue`, order, the `endOptions` input `unseen`)
  - `src/lib/server/learn.js`: `chapterInfo` adds `unseen = open.filter(no state && !shownAt)`; `end()` passes it at ~l.1072
  - tests in `data/learn/*.test.mjs`

### 3. Chapter rows show progress through the chapter, not a question-accuracy verdict
- **Surface:** the chapter map (86-full, 88-full) and the chapter page header (89).
- **What is wrong:**
  - The rows read `Too few answers`, `Getting there`, `Needs work`, `Holding`, `Not started`. These are Wilson bounds on question accuracy (`data/chapter_state.js stateFor`).
  - "Too few answers 3 due" (88, Profit and Loss) reads to a 16-year-old like a scolding.
  - After a 20-card run, a row still says nothing about how far through the chapter the student is.
  - A feed never moves the state at all (item 7).
- **Why it matters:** "progress through the syllabus" is the daily-return engine the brief asks for. LK30's blank space is better used by real progress than by words.
- **Exact fix:**
  - The meta line becomes coverage.
    - Pro: `31 of 46 cards seen · 4 of 10 questions tried`
    - Free: `5 of 5 free cards seen`
  - Under the title, a 3px hairline (ink-3 track, volt fill, width = seen / of).
  - It is coverage, never mastery: no %, no "mastered" (product rules).
  - The state word is shown only from `CHAPTER_RULES.minAnswers` answers on, and only `Needs work` or `Holding`. `Too few answers` and `Getting there` leave Learn. They stay on Your record.
  - The chapter page header reads `Part 1, Ch 1 · 16 of 46 cards seen` in place of `Getting there`.
- **Files:**
  - `src/lib/server/learn.js` (`chapterRow`, `rowMeta` l.336-352; `seen` counted from states plus feed shows)
  - `ChapterMap.jsx`, `homeModel.mjs` (`metaLine`, `rowSpoken`), `ChapterPage.jsx`, `learn-home.css`, `homeModel.test.mjs`

### 4. Never draw a zero key; the count keys go under the hero and appear only when they hold something
- **Surface:** the shelf keys (88, and the owner's live "0 … Revise 0" line).
- **What is wrong:** `ShelfKeys.jsx` hides the row only when **all three** counts are 0 (comment: "Zero is a true value: it is drawn, quiet"). A student who studied today therefore gets `0 due today · 0 missed lately · 16 in Revise` as the first thing under the search field. That matches the owner's transcription ("0 in, revise 0").
- **Why it matters:** LK27, and the brief's rule "never show a line of zeros as the lead".
- **Exact fix:**
  - `shelfKeys()` drops every key whose count is 0.
  - With one key left, it is a single 44px text row, not a key: `16 cards in Revise · next ones back Wed`, from `revisePileGroups`.
  - The whole block moves below the roadmap hero and the two secondary rows.
- **Files:** `homeModel.mjs shelfKeys`, `ShelfKeys.jsx`, `LearnHome.jsx`, `homeModel.test.mjs`

### 5. "Today's 10 minutes": one daily run per subject that folds due cards into the roadmap chapter
- **Surface:** the hero key for a returning student.
- **What is wrong:** 88 offers three separate runs of 1, 5 and 3 minutes (due cards, pick-up, fix). Each one starts, ends and shows its own end screen. Revising due cards and moving forward are two different trips.
- **Why it matters:** the daily habit. One key, about 10 minutes, and the student is done for the day in that subject. That is what brings a 16-year-old back (Duolingo's whole loop).
- **Exact fix:**
  - The returning hero key is `Today's 10 minutes`, with this line under it, one line, 15px ink-2: `9 due cards, then 6 new ones in Admission of a Partner`.
  - Compose a `mix` on the roadmap chapter with extra `cardIds` = due cards from any chapter. Due cards take at most 40% of the budget, and the rest flows to the chapter's new cards and questions. One open mistake is added at 10 min.
  - It counts as Free's one session, the same as `mix`.
  - The end line is `Accountancy done for today. 9 cards come back Wed.`
- **Files:**
  - `data/learn/compose.js` (`cardIds` on a mix, the 40% due cap)
  - `src/lib/server/learn.js` (`start` accepts `cardIds` for mix)
  - `roadmap.js` (`action.run`), `RunEnd.jsx`

### 6. A final-weeks mode for the returning Pro student (21 days or fewer to CUET)
- **Surface:** the hero and the suggestions for (b).
- **What is wrong:**
  - Two weeks before the exam, Learn still offers `Next in the book: …`, 10 minutes of new cards.
  - `study_goals.exam_date` exists (`src/lib/server/studyRoad.js`), and `data/cuet_chapter_priorities.json` ranks chapters. Learn reads neither.
  - The recap is per chapter only (the "Or a quick recap" link on 89).
- **Why it matters:** for (b), the useful moves are, in order:
  1. sweep the Must-know lines of every chapter, the high-frequency ones first;
  2. fix open mistakes;
  3. due cards;
  4. full mocks.

  New low-importance cards are noise at that point.
- **Exact fix:** when the exam is 21 days away or less, `roadmap.mode = 'final'`.
  - Title: `14 days to CUET: Accountancy`
  - Line: `Sweep the Must-know lines, the chapters CUET asks most first`
  - Key: `Must-know sweep, 12 min`. This is a `recap` over `cardIds` = Must-know cards, ordered by the priority list, then `Needs work`, then book order. Each sweep continues where the last one stopped (a `sweepCursor` in `start_state`).
  - The secondary rows are `Fix 6 open mistakes · about 6 min` and `Full mock · 50 questions, 60 min`.
  - The composer serves new cards only when `importance === 'must'`.
  - The route strip shows sweep coverage (`chapters swept`).
- **Files:**
  - `learn.js` (read the exam date in the snapshot)
  - `roadmap.js`
  - `compose.js` (recap over `cardIds`; a `mustOnly` flag on new cards)
  - `suggest.js` (hide `next` in final mode)

### 7. A feed counts as learning: the cards it shows move the roadmap
- **Surface:** the Explore feed (10-18, 91, 95), then Learn home.
- **What is wrong:**
  - `studied = tally.n > 0 || mine.some(reps > 0)` (learn.js `chapterInfo`). Feed shows are neither of those.
  - So a first-timer who plays the Explore feed for chapter 2 returns to Learn home and still sees `Start with Accounting for Partnership…`, chapter 2 `Not started`.
  - Explore and Learn are two front doors to near-identical sessions (90 `Play 10 minutes`; 86 `Start 10 minutes`), and progress is split between them.
- **Why it matters:** LK18 makes the feed the standout phone feature. If it does not count, the student's best minutes are invisible.
- **Exact fix:**
  - `seen` (item 3) includes cards whose back was turned in a feed (the `seenBack` event, already sent).
  - The roadmap position moves to a chapter played in a feed.
  - Each Explore cover's foot line shows the same coverage, `12 of 53 cards seen`, in place of the static `5 Key cards, 7 questions`.
  - The covers open at the roadmap chapter, not always at Ch 1.
- **Files:** `learn.js` (`chapterInfo` seen/studied), `data/learn/feed.js`, `ExploreCovers.jsx`, `coverModel.js`

### 8. The feed end and the run end: lead with what moved, in one line, then one key
- **Surface:** the end screens: 55-run-end, 95-feed-end-free-full, 96-run-end-free.
- **What is wrong:**
  - Five blocks before the key:
    - a title;
    - `All 20 done in 1 min.`;
    - a fanned card pile;
    - `16 in Revise / 14 back Wed, 2 back in 20 days`;
    - a three-row table;
    - and on Free, a two-sentence paragraph.
  - Zeros and negatives lead: `Nothing kept this time. Keep a card and it comes back in Revise.`, `5 seen, 0 kept`, `0 of 2 fixed, 2 still open`.
- **Why it matters:** LK31, word for word ("too many lines and walls of text"). The end is also the moment to show roadmap progress, which is the reason to come back tomorrow.
- **Exact fix (order):**
  1. The title, the chapter name (24/28).
  2. One line: `21 of 46 cards seen · 2 of 2 right · 1 mistake fixed`. Any part that is 0 is left out.
  3. The route strip with this chapter's node. Its hairline grows from the old seen value to the new one: 600ms, ease-out, starting 200ms after mount.
  4. One line: `14 cards come back Wed`.
  5. The lead key (from item 2).
  6. At most two text rows.
  - On Free with the session used, one line above the key: `Questions in Learn are back tomorrow.` with a `See Pro` link at the end of the same line.
  - Delete the table, the "Nothing kept" line and the second Free sentence.
- **Files:** `RunEnd.jsx`, `RunParts.jsx`, `ChapterFeed.jsx` (end), `learn.js end()` (one `summary` string built from non-zero parts), `run.css`, `feed.css`

### 9. The first feed teaches its own gesture before the student is stuck
- **Surface:** the feed, first visit (91-first-item, 91-after-4s).
- **What is wrong:**
  - The only cue is a 24px bump of the track. It fires only after `Turn over`, only on a coarse pointer, once, and with no words (`ChapterFeed.jsx` l.264-270).
  - At 4 s nothing appears (91-after-4s). The owner had to discover the swipe (LK29).
  - The space between the card and the bar is empty (LK30).
- **Exact fix:** on the first feed (`NUDGE` unset):
  - The next item's top 48px peeks above the bottom bar: the track is offset by -48px with a 12px fade.
  - Above the bar, a 32px chip, centred, 14px: `Swipe up for the next one`, with a chevron.
    - The chevron rises 8px and settles twice, 2 × 600ms ease-in-out, starting 1.2 s after load.
    - It leaves on the first move or after 6 s (opacity 0 over 200ms).
  - The bump after the first turn stays.
  - Mark it as seen after item 2.
  - Desktop keeps its keys line.
- **Files:** `ChapterFeed.jsx`, `feed.css`

### 10. One word for "comes back later": drop Keep and fold Saved into it
- **Surface:**
  - the feed's `Keep` (91);
  - the Practice row's `Saved` tab (81, 82);
  - `in Revise` (88);
  - Your papers' `8 to revise` (88).
- **What is wrong:**
  - There are four words for nearly the same idea.
  - Rated cards in a run join Revise automatically (55: "16 in Revise"). In a feed, only kept ones do, and the end says "0 kept".
  - A first-timer has no model of how Keep, Saved and Revise differ. This is part of LK26's confusion.
- **Exact fix:**
  - Rename the feed's `Keep` to `Revise later`, keeping the same bookmark glyph. Its toast reads `Added to Revise. Back tomorrow.` (1.6 s).
  - In Learn's copy, "Revise" is the one word for cards that come back.
  - On a phone, the Practice row loses `Saved`: it becomes a filter chip inside Explore (`Saved questions`), so the row is Practice, Learn, Your papers, Explore. That is four tabs, and all four fit at 390 without the scroll arrow.
- **Files:** `ChapterFeed.jsx`, `learn.js` (feed end copy), `src/lib/arenaNavigation.js` (`practicePages`), the Explore filter, `nav.test.mjs`

### 11. Find your level: remember the result, and stop presenting it as a rival key
- **Surface:** Learn home for a new student (87), and the level run end.
- **What is wrong:**
  - `levelPick` names the chapter to start, but only on that end screen (learn.js ~l.1083). Nothing is stored. The next visit says `Start with Accounting for Partnership…` again.
  - On home it is the second big card, with a ghost key that reads as disabled.
- **Exact fix:**
  - Store `{ subject, chapterKey, at }` in the run's `start_state.levelPick`. `roadmap.js` uses the newest pick as the new student's position: `Start with Goodwill: Nature and Valuation · your 6-question check said start here`.
  - On home it becomes a 15px link under the hero key: `Not sure where to start? Take a 6-question check`.
- **Files:** `learn.js` (end() level branch, snapshot), `roadmap.js`, `RoadmapHero.jsx`, `Suggestions.jsx` (drop `level` from the cards)

### 12. The chapter page is a progress page with one key, not a control panel
- **Surface:** the chapter page (89-fresh-free-full, 89-returning-pro-full).
- **What is wrong:** a first-timer meets all of these at once:
  - `How long have you got?`;
  - four segments;
  - two or three piles, with `Tap a pile to leave it out`;
  - a key and a two-line caption;
  - `Or a quick recap: the 5 Must-know lines`;
  - `Everything in this chapter` with four rows;
  - and the closing line `No lesson yet. No open mistakes.`, two negatives.

  Leaving a pile out is an expert control on the main path.
- **Exact fix:**
  - The header: the title, then `Ch 1 · 16 of 46 cards seen` with the hairline from item 3.
  - The time chips (5 / 10 / 20 / Your own) stay.
  - The piles become one read-only line, 16px: `16 Key cards, 2 questions, 2 of your mistakes`.
  - A 15px link, `Change the mix`, opens the piles in a sheet.
  - The key, `Start 10 minutes`. No caption: the line "Stop whenever you like; what you do is saved" goes to the stop sheet.
  - The recap moves into the rows as `Quick recap · 12 Must-know lines, about 2 min`.
  - Delete `No lesson yet. No open mistakes.`
  - A row that has nothing in it is not drawn.
- **Files:** `ChapterPage.jsx`, `chapterModel.mjs`, `chapter.css`, `chapterModel.test.mjs`

### 13. Due cards are revised inside Learn, never sent to another page
- **Surface:** the end options, and the home due row.
- **What is wrong:** `endOptions().dueOpt` links to `/review/revise?source=keycards`, a different page with a different player. The home `due` suggestion starts a Learn `cards` run. The same cards, two players.
- **Exact fix:** `dueOpt` becomes `run: { kind: 'cards', cardIds: dueIds (≤100), minutes }`. The label is `Revise 9 due cards · about 2 min`.
- **Files:** `data/learn/suggest.js endOptions`, `learn.js` (pass `dueIds` across the subject), the tests

### 14. Free's day has a shape: after the session, the hero says what is still free and when the rest returns
- **Surface:** Learn home for Free after the session (no shot yet), and 95/96.
- **What is wrong:**
  - After one 10-minute session (95: "All 12 done in 1 min"), the only signal is the end-screen paragraph.
  - Home then shows the same three cards with `Key cards only today.` appended to the evidence lines (suggest.js `finish`).
- **Exact fix:** the hero switches to `mode: 'freeDone'`.
  - Title: `Back tomorrow for chapter 2`
  - Line: `Your 5 cards from today come back Wed.`
  - Key: `Questions in Explore, free`, which goes to `/explore`.
  - One link: `See Pro`.

  It names the limit only at the limit (LK15's CTO rule), as one line.
- **Files:** `roadmap.js`, `RoadmapHero.jsx`, `suggest.js` (drop the evidence suffix once the hero owns it)

### 15. "Your part" is asked once, in the hero, not dumped mid-list
- **Surface:** the Accountancy map (86-full, 88-full: `Your part` with two boxes and `Both parts show until you choose.` between Part 2's units).
- **What is wrong:**
  - A first-timer scrolls into a choice they did not expect.
  - Until they choose, "chapter N of 15" counts chapters they will never sit.
- **Exact fix:**
  - When `part.option.chosen` is null, the hero shows two chips under its line: `Which Part 2 does your school teach?` with `Analysis of Financial Statements` and `Computerised Accounting`.
  - The roadmap counts only the chapters both parts share until the choice is made.
  - The mid-list block stays only as a quiet `Change your part` row.
- **Files:** `RoadmapHero.jsx`, `roadmap.js`, `ChapterMap.jsx`

### 16. Dead and thin chapters stay out of the roadmap and go to the content queue (LK34)
- **Surface:** the map (86-full: `Computerised Accounting System · Nothing to practise here yet.`).
- **What is wrong:**
  - A row with nothing in it is a dead end.
  - Thin decks by chapter, from `data/keycards/decks`:
    - Accountancy: Change in Profit Sharing Ratio 8, Analysis of Financial Statements 16, Comparative and Common Size Statements 18, Computerised Accounting 0.
    - Economics: Market Equilibrium 24.
  - English has 349 cards across only 2 of its sections (Vocabulary 283, Correct Word Usage 66). At 18 s a new card, that is about 1.7 h, below LK34's 3-hour floor.
  - The other five decks clear 3 h on cards alone: Accountancy 868 ≈ 4.3 h, Business Studies 900, Economics 1193, Political Science 1096, Biology 1394.
  - Every other CUET subject has no deck. Learn there is questions only.
- **Exact fix:**
  - The roadmap skips chapters with 0 cards and 0 questions. They are drawn last in a muted group, `Coming soon`, with no chevron.
  - The content queue order:
    1. English (Factual Passage, Literary Passage and Para Jumbles have no cards)
    2. Accountancy's four thin chapters, to 40 cards each
    3. Market Equilibrium
    4. the next subjects by student count
- **Files:** `roadmap.js`, `ChapterMap.jsx`, plus the content plan (not code)

### 17. Explore's question list: verify de-duplication before the owner sees it
- **Surface:** Explore below the covers (90-full).
- **What is wrong:** the page is 7410px tall. Two questions ("Goodwill brought in by an incoming partner…" and "Assets are ₹50,000…") repeat about 10 times each. This is most likely the preview fixture, but production has no test for it.
- **Exact fix:**
  - Dedupe by question id and stem hash in the list read.
  - The first load is 10 items, then `Load more questions`.
  - Add a test.
- **Files:** `data/explore_feed.js`, the Explore page component, a test

---

## Aside, outside Learn (for the lead)

Today (85-full) shows `72 marks they cost you` and weak chapters with `30 marks`, which is close to the product rule "no marks to recover". Today also shows `Revise 0 due today` as a tile. Both belong to the Today lane, but they will read as the same "zeros and marks" problem to the owner.
