# Learn, concept B: "the chapter is the home"

Design concept only. No code was changed. Written 31 Oct 2026 for the CTO session. Inputs: the owner's words (LK1 to LK14), the nine maps in `learn-1031/understand/` (R1 to R9), OWNER-TASTE-PROFILE, the ledger's Never again and Keep lists, AGENT_RULES, and the walk screenshots. Decisions B1 to B8 are treated as fixed. Evidence IDs (T001, S014 and so on) and rule numbers (R7, AS9) point at the owner's research brain. Counts come from the maps; where a count is not in the maps it is written as `{n}` and named as a gap in section 4.

**Vocabulary used everywhere, student copy included (B2).** Learn (the place). Key cards (the 5,800 NCERT-line cards). Lesson (the 21 short lessons). Questions (MCQs). Revise (the global due queue). Must-know (the re-tiered quarter). The word "Concepts" is gone. The mixed thing a student starts on a chapter has no new noun: the button names the time ("Start 10 minutes") and the end screen names what was done ("10 minutes on Admission of Partner"). This keeps the vocabulary at the five words above.

---

## 1. The idea

**In three sentences.** Learn opens on your subject's chapter map, laid out the way the NCERT books and the CUET units are, and every chapter on it says at a glance what it holds and how you stand. Tapping a chapter opens its own page, where everything for that chapter is lined up in one place: a ready mix of Key cards and questions sized to the time you pick (5, 10, 20 minutes or your own), plus the cards to browse and revise, the lesson, your open mistakes and the print sheet. Three short suggestions sit above the map so a student who does not want to choose can tap one, but the map, not the suggestion, is the home, so the student is always in charge.

**Why this answers the owner.** The owner's own flow (LK10) is literally the route through this concept: subject switcher, chapter map, chapter page ("what is lined up"), time, Start, mixed run. The "separate place that shows what is where" is the Find view of Learn and the Cards view of each chapter, one component in two scopes.

| LK | His point | How concept B answers it |
|---|---|---|
| LK1 | The way to Key cards is badly placed and too small | Key cards stop being a separate place behind a footnote row. Learn itself opens on the chapter map where every chapter row shows its card count, and the Learn door moves to second place in Practice (web tabs, sidebar, app doors). New doors: a Start sheet row, a Today alternative, a link from "The line you needed", an Explore lead card (section 2). The sidebar label becomes "Learn, Key cards" using the pattern the rail already uses for "Mob, with friends". |
| LK2 | "Your part" glitches and shuffles | The part choice moves to where it matters: inside the map, at the Part 2 option unit, as a two-way switch. It is optimistic and held until the server agrees, and only the one unit below it cross-fades. Nothing above it moves and nothing reorders (section 3.2). The R2 fix is folded in. |
| LK3 | The Learn section is not good or easy to use | Two levels only: map and chapter. Every chapter page has the same anatomy. One leading action per screen (R7), every other path one tap away. |
| LK4 | Read mode has a weird layout | Read becomes the chapter's Cards view: cards grouped by NCERT section with sticky section names, two-line answers that open in place, filters on top, a jump list, and actions on the opened card only. No 14,688 px scroll of full cards. |
| LK5 | Study is right; add motion, for example on Got it | Study keeps its structure (B3). Got it now sends the card into the round's pile with a short flight and a "Back in 3 days" receipt from the server's real interval (section 5). Study lives on the chapter page as "Cards only" and in the Cards view as "Study these". |
| LK6 | Print sheet: keep it, watermark it all over | The sheet stays Pro (B6), prints whatever the Cards view is filtered to (Must-know by default), and carries a tiled mockmob wordmark on every page plus "Printed for Aarav" and a short sheet code in every footer (section 3.9). The app sends the same sheet as a PDF. |
| LK7 | Last look vs Read is unclear | Last look stops being a mode (B4). Its job is in two clearly named places: the "Must-know" filter in Cards with a "Flip through these 12" action, and "Quick recap, 5 min" in the time chooser. Read stops being a mode too; it is the Cards view. No two modes show the same card any more. |
| LK8 | Integrate everything better, in the flow | One subject switcher, one chapter list, one chapter page for lessons, Key cards, questions and mistakes (B2). The same chapter page is reached from Learn, Today, Start, Review, the result and Explore. |
| LK9 | Easy self-control, not only weakness-led | The map is in book order by default; the student picks. Weakness becomes one of three suggestions and an optional sort ("Marks open") on the map, never the organising idea. |
| LK10 | Subject, chapter, what is lined up, time, a mix; plus a separate find-and-revise place | Exactly the screens in 3.1 to 3.6, plus Find (3.7). |
| LK11 | No walls of text; next action clear, dynamic, with options | Each screen has one volt key and two or three named alternatives beside it, each with its reason. Suggestions change with what the student did last. Rows carry one line of meta, not paragraphs. |
| LK12 | Cards are the core; a chapter feed in Explore | Cards lead every chapter page and every mix. Explore gets a chapter feed (one item per screen, 10 minutes by default) built from the same recipe (3.8). |
| LK13 | Too many Must-know marks | Must-know is re-tiered to about one card in four (B5), and the mark becomes a short word in the card's kind line, not a boxed chip (3.10). |
| LK14 | Think longer, ideate better | Section 4 gives the exact recipe with seconds and counts per chapter; section 6 names the risks; nothing he can see is dropped. |

---

## 2. Information architecture

### 2.1 Every place in Learn

```
LEARN (route /learn, app: Practice > Learn door)
 |
 |-- Learn home: two views under one header, switched by a 2-way control
 |     |-- Chapters  (default)  /learn?subject=accountancy
 |     |     suggestions row (3) + subject switcher + chapter map (book order)
 |     |
 |     '-- Find                 /learn/find?subject=accountancy
 |           search (chapters, lessons, Key cards) + your card shelves
 |           (Due today, Missed lately, In Revise, Must-know) + pick cards
 |
 '-- Chapter page              /learn/c/accountancy.partnership-fundamentals
       |-- Lined up: time chooser + the mix preview + Start         (top)
       |-- In this chapter: Key cards, lesson, questions,
       |                    your mistakes, print sheet               (shelf)
       |
       |-- Cards view          /learn/c/<key>/cards[?f=must|revise|missed]
       |     (Find scoped to one chapter; the new home of Read and Last look)
       |-- Lesson              /learn/<unitId> (existing overview, kept)
       |-- Session player      /learn/run/<sessionId>   (dock hidden)
       |     '-- Session end   same route, end state
       '-- Print sheet         print layer of the Cards view (Pro)

EXPLORE (existing /explore)
 '-- Chapter feed              /explore/run/<sessionId> (same engine, feed skin)
```

Old routes are kept and redirect, so no link breaks (R3): `/cards` to `/learn?subject=<first>`, `/cards?subject=x` to `/learn?subject=x`, `/cards/<key>` to `/learn/c/<key>/cards`, `/cards/<key>?mode=study` to the chapter page with "Cards only" chosen, `?mode=last` to `/learn/c/<key>/cards?f=must`, `/learn/summary?subject=&chapter=` stays and is linked from the lesson row. App: `/cards` and `/cards/:key` redirect to the same app routes; `/learn` keeps redirecting to `/practice?door=learn`.

How they connect:

| From | To | Control |
|---|---|---|
| Learn home, suggestion | Session player (starts at once) | the suggestion's own key |
| Learn home, chapter row | Chapter page | whole row |
| Learn home, Find result (chapter) | Chapter page | row |
| Learn home, Find result (card) | Cards view of its chapter, card opened | row |
| Chapter page | Session player | "Start 10 minutes" (volt) |
| Chapter page, Key cards row | Cards view | row |
| Chapter page, lesson row | Lesson overview | row |
| Chapter page, questions row | Practice set up for this chapter (Quick practice, existing) | row |
| Chapter page, mistakes row | Session player in "Your mistakes" mix (open mistakes plus their lines) | row |
| Cards view | Session player, cards only, chosen cards | "Study these 12" |
| Cards view | Print sheet | "Print sheet" (Pro) |
| Session end | Chapter page, the next chapter, another 5 minutes, Revise | four options |
| Explore, chapter filter set | Chapter feed | the lead card above the question list |

### 2.2 Where Learn sits in navigation

**Web, 1440 (sidebar, unchanged five places).** The Practice place keeps its sub-rows; Learn moves to the first sub-row and gains the rail's existing "name, detail" pattern:

```
 [>] Start a session
 Today
 Practice
    Learn, Key cards              5 due      <- moved first, 44 px row
    Your papers                   8 due
    Explore
    Saved
 Mob, with friends
    Your standing
 You
    ...
```

The "5 due" count on the Learn row is Key cards due today (from `today.due`); "8 due" on Your papers stays the Revise question count. The row is lit on `/learn*` and on the old `/cards*` redirects. The top bar title says "Learn" and the page h1 says the subject's name ("Accountancy") on the home and the chapter name on a chapter page, so the bar and the h1 never disagree (R9 problem 3).

**Web, 390 (phone).** The dock stays Today, Practice, Start, Mob, You (B1, H5). Practice's sideways tab row becomes **Practice, Learn, Your papers, Explore, Saved**, so Learn is the second tab and always fully visible at 390 (R9 measured Explore as the cut tab). The tab row now also draws on `/learn/c/*` pages (the row today draws only on exact hrefs), so a phone student on a chapter can move sideways without Back.

**Practice page itself (web and app).** The existing Learn door card (`ConceptsPanel`) is refined, not replaced: it gets the subject object art, a live line and two keys.

```
 Learn
 Accounting for Partnership: Basic Concepts      [ Pick up, 10 minutes ]
 46 Key cards, 3 due. You stopped at 6 of 16.       All chapters
```

**App.** Dock unchanged. The Practice door switch (D126) becomes **Practise | Learn | Your papers**. Learn door content is the Learn home below. The chapter page, Cards view and player are pushed over the shell (`root: true`) with a full-width Back button at the top left, labelled "Learn" (D43).

**Start sheet (web and app).** One row is added, in the existing row style, between "By chapter" and "Smart practice". Nothing else in the praised sheet moves (N11).

```
 Learn a chapter
 Key cards and questions, 5 to 20 minutes. Free.          Set up
```

It opens the Learn home on the student's current subject; if the student was on a chapter in the last 7 days, it opens that chapter page instead.

**Today (web and app).** Learn enters Today's existing move pool, not a new section:
- `alternatives()` gains one Learn move when the student has opened Learn before: "Pick up Admission of Partner, 10 minutes" (the last chapter, the time last used). It can be swapped into the lead like any alternative.
- A brand-new student (no papers, no Learn history) gets "Try 5 minutes of Key cards" as the third first-week alternative, opening the chapter page of the first chapter in their first subject.
- The Revise tile's sub-line "3 Key cards among them" becomes a link to Find with the "Due today" shelf open.

**Result and Review.** "The line you needed" gains a quiet link under its cards: "Open Accounting for Partnership: Basic Concepts". Review chapter rows replace "Key cards for this chapter" with "Learn this chapter, 10 minutes", which opens the chapter page with 10 minutes chosen.

**Explore.** When a chapter is chosen in Explore's filter, a lead card appears above the questions: "Run this chapter as a feed, 10 minutes. Key cards and questions." (3.8). Without a chapter it shows "Pick a chapter to run it as a feed."

### 2.3 Taps from opening the site to studying a chapter's cards

Counted from the first screen after sign-in (Today). A tap is a click or tap; scrolls are not counted. "Studying" means the first Key card is on screen.

| Student | Surface | Path | Taps |
|---|---|---|---|
| New | Web 1440 | Sidebar "Learn, Key cards" (1), chapter row "Accounting for Partnership: Basic Concepts" (2), "Start 10 minutes" (3) | **3** |
| New | Web 390 | Dock Practice (1), Learn tab (2), chapter row (3), Start (4) | **4** |
| New | Web 390, via Today | Today alternative "Try 5 minutes of Key cards" (1), Start (2) | **2** |
| New | App | Practice (1), Learn door (2), chapter row (3), Start (4) | **4** |
| Returning | Web 1440 | Sidebar Learn (1), first suggestion "Pick up Admission of Partner, 10 min" key (2) | **2** |
| Returning | Web 390 / app | Today's Learn alternative swapped in, or its key (1) | **1** |
| Returning | Web 390 / app, through Learn | Practice (1), Learn (2), suggestion key (3) | **3** |
| Returning, cards only (Study) | Web 1440 | Learn (1), chapter (2), "Cards only" (3), Start (4) | **4** |

Today, for comparison (R1, R9): 3 clicks at 1440 and 4 to 5 taps on a phone to reach a deck in Read mode, and Study is one more.

---

## 3. Screens

Conventions in the wireframes: `[ Start 10 minutes ]` is the one volt key; `( 10 min )` is a selected choice; `Option` text in a row is a secondary key or link; `>` at a row end is the chevron; `(obj)` is a lamp-lit 3D subject object; `|` lines are column edges. Night is the default drawing; Day uses the same layout with the Day tokens. Glass is only on the dock, the top bar and sheets.

### 3.1 Learn home: Chapters view

**Hierarchy.** (1) Subject title with the subject switcher; (2) the suggestions row, three cards, the first one leading; (3) the chapter map. One volt key: the first suggestion's key. Options beside it: the other two suggestions, every chapter row, and the Find view.

**1440, returning Pro student, Accountancy.**

```
| sidebar |  Learn                                         ( Chapters | Find )          |
|         |                                                                              |
|         |  (obj)Accountancy  (obj)Business Studies  (obj)Economics  (obj)English       |
|         |   ^ the praised subjects loop, reused; selected object lit, others dimmed      |
|         |                                                                              |
|         |  Accountancy                          868 Key cards, 14 chapters, 4 lessons  |
|         |                                                                              |
|         |  +----------------------------+ +-------------------------+ +----------------+|
|         |  | Pick up                    | | 3 cards due             | | 2 open mistakes||
|         |  | Admission of Partner       | | Accounting Ratios       | | Change in      ||
|         |  | You stopped at 6 of 16.    | | Due today, about        | | Profit Sharing ||
|         |  | About 4 minutes left.      | | 1 minute.               | | Ratio, with the||
|         |  | [ Pick up, 4 minutes ]     | | Revise these            | | lines you need.||
|         |  +----------------------------+ +-------------------------+ | Fix them, 5 min||
|         |                                                             +----------------+|
|         |  Chapters                               Book order v   Search chapters       |
|         |                                                                              |
|         |  PART 1  Partnership Accounts                                                |
|         |  Accounting for Partnership                                                  |
|         |  ------------------------------------------------------------------------   |
|         |  Accounting for Partnership: Basic Concepts   (o) Getting there   46 cards  >|
|         |  Ch 1                                              3 due, no lesson yet       |
|         |  ------------------------------------------------------------------------   |
|         |  Profit and Loss Appropriation Account        ( ) Too few answers 42 cards  >|
|         |  Ch 1                                              3 due                      |
|         |  Reconstitution of a Partnership Firm                                        |
|         |  ------------------------------------------------------------------------   |
|         |  Change in Profit Sharing Ratio               (o) Needs work      8 cards   >|
|         |  Ch 2                                              1 lesson, 2 open mistakes  |
|         |  Goodwill: Nature and Valuation               (*) Holding         39 cards  >|
|         |  Admission of Partner                         (o) Getting there   53 cards  >|
|         |  Ch 3                                              1 lesson, 6 of 16 done today|
|         |  Retirement and Death of a Partner            ( ) Not started     65 cards  >|
|         |  Dissolution of Partnership Firm              ( ) Not started     59 cards  >|
|         |                                                                              |
|         |  PART 2  Company Accounts and Analysis of Financial Statements               |
|         |  Company Accounts                                                            |
|         |  Share Capital                                ( ) Not started    106 cards  >|
|         |  Debentures                                   ( ) Not started     86 cards  >|
|         |  Your part   ( Analysis of Financial Statements | Computerised Accounting )  |
|         |  Only your part's chapters show here and in your practice.                   |
|         |  Financial Statements of a Company            ( ) Not started     85 cards  >|
|         |  Analysis of Financial Statements             ( ) Not started     16 cards  >|
|         |  Comparative and Common Size Statements       ( ) Not started     18 cards  >|
|         |  Accounting Ratios                            (o) Getting there  164 cards  >|
|         |  Ch 5                                              3 due, 1 lesson            |
|         |  Cash Flow Statement                          ( ) Not started     81 cards  >|
|         |                                                                              |
|         |  Chapters follow the CUET UG 2026 syllabus and the NCERT books.              |
|         |  Study plan    On this device: 12 lessons and cards kept     Your record     |
```

Notes:
- "PART 1" is not drawn in capitals in the build; it is written here in capitals only to mark the level. Real copy: "Part 1, Partnership Accounts" in the label role (sentence case, no tracking, T-061).
- Row anatomy (one row, 64 px at 1440, two lines): chapter name; the NCERT chapter ref; the state ring and word from `chapter_state` (Not started, Too few answers, Needs work, Getting there, Holding, with ", fading"); the card count; one meta line that only says what is true and useful now (due count, lesson, open mistakes, progress today). Never more than one meta line. No "5 of 46 open" repeated on every Free row (see Free state).
- Sort control "Book order" opens a two-item menu: Book order (default) and Marks open. "Marks open" re-sorts by the existing marks-lost read and shows the red "−35" on rows; this is the folded "Where you lose marks" section (nothing dropped, but it is a lens the student chooses, LK9).
- Search here filters the map as you type (chapters and lessons). Card search lives in Find.
- The foot row holds the folded Learn extras: "Study plan" (the old Study preferences and Pro weekly plan, now a sheet), the app's "On this phone" offline packs, and "Your record" (lessons read, cards in Revise, cards recalled), each one tap.

**390, the same student.**

```
+------------------------------------------+
| mockmob.                    (40)  (P)    |  top bar (glass)
| Practice  Learn  Your papers  Explore >  |  tab row, Learn selected
|------------------------------------------|
| Learn                 ( Chapters | Find )|
|                                          |
|  (obj)       (obj)        (obj)     (ob  |  subjects loop, scrolls
|  Accountancy Business St. Economics      |
|                                          |
| +--------------------------------------+ |
| | Pick up                              | |
| | Admission of Partner                 | |
| | You stopped at 6 of 16. About 4      | |
| | minutes left.                        | |
| | [        Pick up, 4 minutes        ] | |
| +--------------------------------------+ |
| +-----------------+ +------------------+ |
| | 3 cards due     | | 2 open mistakes  | |  two smaller cards,
| | Accounting      | | Change in Profit | |  side by side, 44 px
| | Ratios, 1 min   | | Sharing Ratio,   | |  keys inside
| | Revise these    | | 5 min. Fix them  | |
| +-----------------+ +------------------+ |
|                                          |
| Chapters                    Book order v |
| Part 1, Partnership Accounts             |
| Accounting for Partnership               |
| ---------------------------------------- |
| Accounting for Partnership:            > |
| Basic Concepts                           |
| (o) Getting there   46 cards, 3 due      |
| ---------------------------------------- |
| Profit and Loss Appropriation          > |
| Account                                  |
| ( ) Too few answers   42 cards, 3 due    |
| ---------------------------------------- |
| ...                                      |
|  ( Today  Practice  [>]  Mob  You )      |  dock (glass)
+------------------------------------------+
```

At 390 the first chapter row starts at about 760 px on an 844 px screen when all three suggestions show; the student sees the lead suggestion, the two small ones and the map's first heading without scrolling. The subjects loop is 112 px tall here (objects 72 px).

**App.** Same order inside the Learn door. The door's own title is Practice's; Learn's h1 is the subject name. The "How Learn works" Mobi header (first visit only) is kept and rewritten: "Pick a chapter, pick a time. Your cards and questions are lined up." with Mobi pointing at the first chapter row; it hides after the first chapter is opened.

**States.**

| State | What shows |
|---|---|
| New student, no history | Suggestions become a first-run set built from the syllabus, never one card (G12): "Start with Accounting for Partnership: Basic Concepts / Chapter 1 of Part 1. Ten minutes of its Key cards and questions. [ Start 10 minutes ]", "Quick recap: Share Capital / Its 27 Must-know lines, about 7 minutes.", "Find any card / Search all 868 Accountancy cards." The subject is the student's first CUET subject (not English by default, R1 problem 14). No state words on rows yet: every ring is empty and reads "Not started". |
| Returning | As drawn. Suggestion 1 is chosen in this order: an unfinished run; a chapter opened in the last 7 days; the first not-started chapter after the last finished one in book order. Suggestion 2: due cards (largest chapter count). Suggestion 3: open mistakes (chapter with most), else "Next in the book: {chapter}". Each names its reason (MockMob overlay). |
| Free | The suggestion keys are the same. Rows show the full card count; a single line under the subject title says "Free opens 5 cards in every chapter. Pro opens all 868." with "See Pro", dismissable (InlineNudge). No per-row "5 of 46 open". |
| Thin subject (English: 2 chapters) | The map shows the two chapters and the English note "English cards are written for MockMob, not taken from an NCERT book." under the subject title. |
| A chapter with no cards (Computerised Accounting System) | Row reads "No Key cards yet. Questions ready." and opens a chapter page whose lined-up mix is questions only. |
| Loading | Subjects loop drawn at once from the profile; suggestions and map show skeletons of the same height (no layout shift, R9 problem 1); aria "Loading Learn". |
| Error | The map area: "Learn did not load" / "Check your connection and try again. Your cards and their schedule are safe." with "Try again". The subjects loop stays usable. |
| Partial (chapter states failed) | Rows show counts with the word "Could not load" in place of the state; nothing reads "Not started" falsely. |
| Lessons switched off | Lesson words disappear from rows; nothing else changes. |
| Key cards switched off | Rows show lessons and questions only; card counts hide; the page still opens (R9: the only door must not depend on one flag). |
| Offline (app) | Strip "Offline. Showing what this phone kept." with "As of 9:40 pm"; rows for kept chapters are full brightness, others are dimmed and say "Needs a connection". Suggestions limited to kept chapters, cards only. |

### 3.2 Choosing the subject and the chapter (and the part fix)

- **Subject switcher.** The subjects loop from Practice (praised, D4), filtered to the student's own CUET subjects in their own order, with Biology and Political Science included (six Key cards subjects; R1 problem 5). Selected subject is remembered per device and on the account. The Learn and Practice selections are one shared state.
- **Chapter choosing.** The map is the chooser. A long subject (Economics, 17 chapters) gets a sticky part heading while scrolling and a "Search chapters" field that filters rows live.
- **The part choice (LK2).** Drawn at the Part 2 option point, not above the map:

```
 Your part   ( Analysis of Financial Statements | Computerised Accounting )
 Only your part's chapters show here and in your practice.
```

Behaviour: one sliding indicator (N5). Tap moves it at once and it stays there. The choice is held locally until the server body agrees (the R2 `saved` fix), and the hint line keeps a fixed height ("Saving your choice" uses the same line). Only the option unit below the switch changes: its rows cross-fade out (160 ms) and the other part's rows fade in (220 ms) in a container whose height animates (240 ms). Rows above never move, nothing is re-sorted, row keys are chapter keys (not positions). If the save fails, the indicator slides back with "Your choice was not saved. Try again." and the list never blanks (a failed refetch keeps the previous body). With nothing saved, the switch shows "Both parts show until you choose." and neither side is lit; both units show.

### 3.3 The chapter page: what is lined up

**Hierarchy.** (1) Chapter name and where it sits; (2) the lined-up block: time chooser, the mix preview in one sentence plus a small fanned stack, and the one volt key "Start 10 minutes"; (3) the shelf "In this chapter" with five rows; (4) nothing else. Options beside the lead: "Cards only" and "Quick recap" (inside the chooser) and the five shelf rows.

**1440, Pro, returning, Accounting for Partnership: Basic Concepts.**

```
| sidebar |  < Learn                                                                    |
|         |                                                                              |
|         |  Accounting for Partnership                          +----------------------+|
|         |  Accounting for Partnership: Basic Concepts          |  In this chapter     ||
|         |  Accountancy Part 1, Ch 1      (o) Getting there     |                      ||
|         |  7 of 11 right on the latest try at each question.   |  Key cards        >  ||
|         |                                         (obj)        |  46 cards, 12 Must-  ||
|         |  -----------------------------------------------     |  know, 5 in Revise   ||
|         |  How long have you got?                              |  ------------------  ||
|         |                                                      |  Questions        >  ||
|         |   ( 5 min )  (( 10 min ))  ( 20 min )  ( Your own )  |  11 tied to these    ||
|         |                                                      |  cards, {q} in all   ||
|         |   Mix   (( Cards and questions )) ( Cards only )     |  ------------------  ||
|         |         ( Quick recap, 5 min )                       |  Your mistakes    >  ||
|         |                                                      |  3 open. Fix them    ||
|         |   [stack]  Lined up: 3 due cards, 10 new cards,      |  with their lines.   ||
|         |   [art  ]  your 2 open mistakes and 5 questions.     |  ------------------  ||
|         |                                                      |  Lesson              ||
|         |   [            Start 10 minutes            ]         |  No lesson for this  ||
|         |   Ratings join Revise. Questions are free.           |  chapter yet.        ||
|         |                                                      |  ------------------  ||
|         |                                                      |  Print sheet      >  ||
|         |                                                      |  12 Must-know lines, ||
|         |                                                      |  with your name      ||
|         |                                                      +----------------------+|
```

The right column is 320 px, sticky. The lined-up block is the left column's whole first screen, so the leading action never scrolls away at 1440 x 900. The object art is the subject's lamp-lit object at 120 px, lit when the chapter has something due.

**390, same.**

```
+------------------------------------------+
| mockmob.                    (40)  (P)    |
| Practice  Learn  Your papers  Explore >  |
|------------------------------------------|
| < Learn                                  |  44 px back key
|                                          |
| Accounting for Partnership     (obj)     |
| Accounting for Partnership:              |
| Basic Concepts                           |
| Part 1, Ch 1   (o) Getting there         |
|                                          |
| How long have you got?                   |
| +-------+ +--------+ +-------+ +-------+ |
| | 5 min | |10 min  | |20 min | | Your  | |  one sliding thumb,
| |       | |(chosen)| |       | | own   | |  48 px tall
| +-------+ +--------+ +-------+ +-------+ |
| (( Cards and questions )) ( Cards only ) |  chips, 44 px,
| ( Quick recap, 5 min )                   |  wrap to 2 lines
|                                          |
| [stack] Lined up: 3 due cards, 10 new    |
| [art  ] cards, your 2 open mistakes and  |
|         5 questions.                     |
|                                          |
| [          Start 10 minutes          ]   |
| Ratings join Revise. Questions are free. |
|                                          |
| In this chapter                          |
| ---------------------------------------- |
| Key cards                              > |
| 46 cards, 12 Must-know, 5 in Revise      |
| ---------------------------------------- |
| Questions                              > |
| 11 tied to these cards                   |
| ---------------------------------------- |
| Your mistakes                          > |
| 3 open. Fix them with their lines.       |
| ---------------------------------------- |
| Lesson                                   |
| No lesson for this chapter yet.          |
| ---------------------------------------- |
| Print sheet                            > |
| 12 Must-know lines, with your name       |
|  ( Today  Practice  [>]  Mob  You )      |
+------------------------------------------+
```

The Start key sits at about 640 px on an 844 px phone. When the volt key is on screen, the dock's Start key goes quiet (W-075, existing rule).

**A chapter with a lesson (Admission of Partner, 20 minutes chosen).** The preview sentence names the lesson first, because the 20-minute recipe includes an unread lesson:

```
 Lined up: the lesson "Revaluation of assets and liabilities" (7 min),
 then 2 due cards, 12 new cards and 6 questions.
 [            Start 20 minutes            ]
```

The shelf's lesson row then reads "Revaluation of assets and liabilities / 7-minute lesson, not read yet. Read it alone" and opens the existing lesson overview (`/learn/<unitId>`), kept unchanged.

**States.**

| State | What shows |
|---|---|
| New student | Time defaults to 10 min (no history; a stated safe default, T001). State line reads "Not started". Mix sentence: "Lined up: 10 new cards and 5 questions. Your first cards are the chapter's Must-know lines." Under the key: "Ratings join Revise, so cards come back when they are due." (first visit only, then the short form). |
| Returning | Default time = the time the student used last in Learn (R13: shown as chosen, editable). Pro reason line from `/api/me/chapters` as today. |
| Free | Mix sentence is honest about the taste: "Lined up: 5 open cards and 7 questions. Free opens 5 of this chapter's 46 cards." Key cards row: "46 cards, 5 open on Free". Print sheet row stays visible: "Print sheet / Part of Pro" with a lock glyph, opening the Pro sheet (D101). If today's 10 card ratings are used: "Today's 10 free card ratings are used. Your cards show without ratings; questions are free." The key still starts. |
| Free, 20 min in a thin-card chapter | "Lined up: 5 open cards and 15 questions." Never a padded or fake mix. |
| Not enough content | If the chapter's pool cannot fill the time: "This chapter has enough for about 12 minutes today." and the key reads "Start 12 minutes", with an option "Add the next chapter, Profit and Loss Appropriation Account". |
| No cards (Computerised Accounting) | Mix chips hide; sentence "Lined up: 10 questions."; Key cards row "No Key cards for this chapter yet". |
| No questions in the chapter (thin pool) | Mix sentence: "Lined up: 18 cards. Questions for this chapter are being checked."; "Cards and questions" chip is disabled with that reason. |
| Loading | Title and ref render from the map's cached row instantly; chooser renders; preview sentence shows a one-line skeleton; Start is disabled with aria "Lining up your cards". |
| Error | Preview area: "We could not line this up. Try again." with "Try again"; shelf rows still open. |
| Offline (app) | Chooser shows "Cards only" chosen and the other chips disabled: "Questions need a connection." Cards come from the kept deck; ratings go to the existing outbox. |

### 3.4 Choosing the time

The chooser is on the chapter page, inline, never a separate form step (Never again 3). It is two rows.

1. **Length:** 5 min, 10 min, 20 min, Your own. One indicator slides between them (N5). "Your own" opens a small sheet with the existing `DailyMinutes` picker (presets 30 min, 45 min, 1 hour, then a stepper in 5-minute steps up to 120; never capped below what the student asks, H1). The chosen custom value then replaces the tile's label: "35 min".
2. **Mix:** Cards and questions (default), Cards only, Quick recap, 5 min.
   - Cards only is Study (B3): the same front, Show answer, Missed / Got it / Easy, rounds of 20. Length maps to rounds: 5 min is one round of 20, 10 min two rounds, 20 min four rounds; the sentence says "One round of 20 cards, about 5 minutes."
   - Quick recap, 5 min is Last look's job (B4): Must-know cards only, answers showing, one at a time, nothing scheduled, no ratings, no allowance used (mode `last_look`). Choosing it sets the length to 5 min and greys the other lengths with "A recap is one pass of the Must-know lines." The sentence: "12 Must-know lines, about 3 minutes. Nothing is scheduled."

**Live readout (D47, N1).** The preview sentence and the fanned stack update on every change, within 150 ms, from the composer's dry run (section 4). The stack art shows up to three fanned paper cards with the counts printed on their edges ("13 cards", "5 questions", "2 mistakes"); the cards slide in or out when counts change. The Start key always names the length: "Start 5 minutes", "Start 20 minutes", "Start the recap".

### 3.5 The session player

**Hierarchy.** (1) The item; (2) its one action; (3) a thin top line with progress and an exit. No dock, no sidebar (focus page, like Revise). The page is a single centred column, 640 px wide at 1440.

**Top line (both widths).**

```
 Close        Accounting for Partnership: Basic Concepts       7 of 20
 [=========================------------------------------]   about 6 min left
```

Progress uses pips grouped in the background colour with the done part filled volt (truthful: counts only finished items, T002, R17). "About 6 min left" is recomputed from the remaining items with the same seconds. "Close" asks nothing: every answer is already saved; closing returns to the chapter page, whose lead suggestion becomes "Pick up, 6 minutes".

**A Key card turn, front (1440).** The player is Study's `KeyCardPlayer` (B3) placed in the run:

```
            +----------------------------------------------------------+
            |  Definition   Must-know                              ... |
            |                                                          |
            |  What is a partnership, as the Indian Partnership        |
            |  Act, 1932 defines it?                                   |
            |                                                          |
            |  - - - - - - - - - - - - - - - - - - - - - - - - - - -   |
            |                                                          |
            +----------------------------------------------------------+
                        [        Show answer   Space        ]
```

**Revealed:**

```
            +----------------------------------------------------------+
            |  Definition   Must-know                              ... |
            |  What is a partnership, as the Indian Partnership        |
            |  Act, 1932 defines it?                                   |
            |  - - - - - - - - - - - - - - - - - - - - - - - - - - -   |
            |  | Partnership is the relation between persons who      |
            |  | have agreed to share the profits of a business       |
            |  | carried on by all or any of them acting for all.     |
            |  Accountancy Part 1, Ch 1, p. {p}                        |
            |  In short: an agreement to share profit, and each can    |
            |  act for all.                                            |
            +----------------------------------------------------------+
               [ Missed  1 ]   [ Got it  2 ]   [ Easy  3 ]
                Each card you rate joins Revise.
```

The text above is the Partnership Act definition as NCERT quotes it; the build shows the card's own `quote`, `source.page` and `note` from the deck, never this sample.

**390, Key card revealed.**

```
+------------------------------------------+
| Close                         7 of 20    |
| [=============------------]  6 min left  |
|                                          |
| +--------------------------------------+ |
| | Definition  Must-know            ... | |
| | What is a partnership, as the        | |
| | Indian Partnership Act, 1932         | |
| | defines it?                          | |
| | - - - - - - - - - - - - - - - - - -  | |
| | | Partnership is the relation        | |
| | | between persons who have agreed    | |
| | | to share the profits of a business | |
| | | carried on by all or any of them   | |
| | | acting for all.                    | |
| | Accountancy Part 1, Ch 1, p. {p}     | |
| | In short: an agreement to share      | |
| | profit, and each can act for all.    | |
| +--------------------------------------+ |
|                                          |
| [ Missed ]   [  Got it  ]   [  Easy  ]   |  pinned to the bottom,
|                                          |  safe-area aware
+------------------------------------------+
```

The rating row is pinned above the gesture bar on phones (fixes the app's keys landing on the gesture bar, R5 problem 3). "Got it" is the visually default key on the web (as today); the app keeps three equal keys (as today). Keys 1, 2, 3 and Space work on the web.

**An MCQ turn (390).** Questions are graded on the server (section 4); the options lock on the first tap.

```
+------------------------------------------+
| Close                         8 of 20    |
| [==============-----------]  5 min left  |
|                                          |
| Question                                 |
| In the absence of a partnership deed,    |
| interest on partners' capital is:        |
|                                          |
| +--------------------------------------+ |
| | A  Allowed at 6% a year              | |
| +--------------------------------------+ |
| +--------------------------------------+ |
| | B  Not allowed                       | |
| +--------------------------------------+ |
| +--------------------------------------+ |
| | C  Allowed at the bank rate          | |
| +--------------------------------------+ |
| +--------------------------------------+ |
| | D  Allowed at 12% a year             | |
| +--------------------------------------+ |
+------------------------------------------+
```

(The question is illustrative of the chapter; the build serves bank questions only.)

**A wrong answer, with the line you needed (390).**

```
+------------------------------------------+
| Close                         8 of 20    |
| ...question as above...                  |
| | A  Allowed at 6% a year         (x)  | |  red with icon
| | B  Not allowed                  (v)  | |  green with icon
|                                          |
| The answer is B.                         |
| Without a deed, the Act's rules apply,   |
| and the Act allows no interest on        |
| capital.                                 |
|                                          |
| The line you needed                      |
| +--------------------------------------+ |
| | Key line   Linked to this question   | |
| | | No interest is allowed on capital  | |
| | | when there is no partnership deed. | |
| | Accountancy Part 1, Ch 1, p. {p}     | |
| +--------------------------------------+ |
|  This card comes back later in this run. |
|                                          |
| [             Next             ]         |
+------------------------------------------+
```

Rules for the wrong-answer turn:
- The explanation is the question's stored explanation (no AI call, no wall: clipped at 3 lines with "More").
- "The line you needed" uses `lineNeeded()` with the run's chapter cards (linked first, matched by words second). Inside a Learn run it does not spend Free's 3-a-day line allowance, because the card is already one of the chapter's open cards; if the needed card is locked for Free, the block shows "The line for this is in a card that is part of Pro." with See Pro, once per run.
- The linked card is inserted again 3 items later as a Key card turn (if not already rated Got it or Easy in this run), so the student meets the line once more in the same run: "This card comes back later in this run." This is the in-run version of the schedule, said in plain words.
- A right answer shows "Right. B, not allowed." and the explanation's first line; "Next" is the volt key. On the web Enter goes to the next item.

**1440 player.** Same column, centred, 640 px; the chapter name sits in the top line; a quiet column at the right of the page (outside the item, 240 px) holds "Up next: 2 cards, then a question" so the mix is visible without a strip to decode. It disappears below 1100 px.

**Lesson turn (20-minute runs with an unread lesson).** The existing lesson player (`/study/<runId>` steps, quick checks) plays first, inside this run's top line ("Lesson, step 2 of 7"). Its own recall cards follow it as Key-card-style turns with the kind line "From the lesson" and four ratings as today (their engine is kept; the word "concept" is not shown).

**States.**

| State | What shows |
|---|---|
| Rating sending | The pressed key shows a small spinner; the card does not leave until the server accepts (no success before acknowledgement, UXS 7). Offline in the app: accepted into the outbox, then leaves; a quiet "Saved on this phone" line in the end screen. |
| Rating failed | "That rating was not saved. Try again." under the keys; the card stays. |
| Answer failed | "Your answer did not reach us. Try again." with the options still locked to the student's pick; retry resends the same `requestKey`. |
| Free ratings used mid-run | The current card finishes as a look: the keys become one key "Next", with one line "Today's 10 free card ratings are used. The rest of your cards show without ratings." Questions continue. No 402 screen mid-run. |
| Card reported | The "..." menu (Report this card, Add this card to Revise for Pro Good-to-know) stays on the card head, as today. |
| Leaving mid-run | Close, the browser back or the app back gesture leaves at once; the run is resumable for 24 hours from Learn home and Today. |
| Reduced motion | See section 5. |

### 3.6 Session end, with next options

**Hierarchy.** (1) What happened, in numbers with units; (2) what moved (cards into Revise, mistakes fixed); (3) one volt key and three named alternatives, each with its reason (LK11). Mobi appears once, sized to the free space, reacting to the result.

**390.**

```
+------------------------------------------+
|                                  (Mobi)  |
| 10 minutes on                            |
| Accounting for Partnership:              |
| Basic Concepts                           |
|                                          |
|  13        5          2                  |
|  cards     questions  mistakes           |
|  rated     answered   fixed              |
|                                          |
| Cards   9 got it, 2 easy, 2 missed       |
|         Missed ones come back tomorrow.  |
| Questions  4 of 5 right                  |
| Mistakes   2 of 3 fixed. 1 still open.   |
|                                          |
| [  Next: Profit and Loss Appropriation  ]|
| [  Account, 10 minutes                  ]|
|                                          |
|  Another 5 minutes here                > |
|  2 missed cards, 3 new ones              |
|  -------------------------------------   |
|  Fix your last open mistake            > |
|  Change in Profit Sharing Ratio, 2 min   |
|  -------------------------------------   |
|  Test it in a full mock                > |
|  50 questions, 60 minutes                |
|                                          |
|  Back to the chapter                     |
+------------------------------------------+
```

How the four options are chosen (dynamic, LK11):
- Lead: if the student missed 3 or more cards, "Another 5 minutes here" leads instead of the next chapter; otherwise "Next: {next chapter in book order}, {same length}". The lead's key starts at once.
- Second: "Another 5 minutes here" (or "Next chapter" if it was swapped into the lead).
- Third: an open mistake elsewhere in the subject, else "Revise {n} due cards, {m} min" if Revise has due items, else "Quick recap of this chapter, 3 minutes".
- Fourth: "Test it in a full mock" (folded from Learn's aside, R1 2.2 item 11).
- "Back to the chapter" is a text link.

Numbers count up (section 5). The end lists no percentages under six answers and never says "mastered" (KEYCARDS-BUILD-SPEC product rules). Pro sees one more line when the chapter state moved: "Admission of Partner moved from Needs work to Getting there." Free sees, only if a real limit was met during the run (D181): "Free opened 5 of this chapter's 46 cards. Pro opens all of them and keeps them on a schedule." with See Pro.

**1440.** The same content in a 720 px centred column; the four options sit as a 2 x 2 grid of rows under the lead key, each 72 px, so the eye reads the lead first, then the options.

### 3.7 Find, and the chapter's Cards view (the new home of Read, with Last look folded in)

Find is the same component in two scopes: the whole subject (Learn home, "Find") and one chapter (Cards view). This is the owner's "separate section that easily shows what to find where, and lets them revise specific cards".

**Find, subject scope, 1440.**

```
| sidebar |  Learn                                        ( Chapters | (Find) )       |
|         |  (obj)Accountancy  (obj)Business Studies  ...                                |
|         |                                                                              |
|         |  [ Search Accountancy: a term, a line, a chapter                       ]     |
|         |                                                                              |
|         |  Your cards                                                                  |
|         |  Due today         Missed lately       In Revise          Must-know          |
|         |  24 cards          7 cards             118 cards          225 cards           |
|         |  about 6 min       last 7 days         across 9 chapters  in 14 chapters      |
|         |  Revise these      Study these         Browse             Browse              |
|         |                                                                              |
|         |  Results for "goodwill"                                   3 chapters, 21 cards|
|         |  Goodwill: Nature and Valuation   chapter   39 cards                      >   |
|         |  Admission of Partner             Definition  Goodwill is the value of the    |
|         |                                   reputation of a firm ...      p. {p}    >   |
|         |  Retirement and Death of a Partner  Key line  The gaining ratio is used to    |
|         |                                   ...                            p. {p}   >   |
```

- Search covers chapter names, lesson titles and Key cards (front, quote, kind), served by a new subject index (section 4). It needs 2 characters, shows the match in the line, and each card result opens its chapter's Cards view with that card opened.
- "Your cards" are four shelves, each one tap. Their numbers are live. "Revise these" starts the global Revise run filtered to Key cards (`/review/revise?source=keycards`), "Study these" starts a cards-only run over that set (rounds of 20), "Browse" opens the set in the Cards view layout across chapters.
- Picking cards: in any list, a long press (app) or the checkbox that appears on hover and focus (web) enters "Pick" mode; a bottom bar then reads "8 picked [ Study these 8 ]  Add to Revise  Clear". "Add to Revise" for single cards stays Pro (today's rule); Free can study picked open cards. This is where the old Pro "mixed revision" (pick lessons, start a mixed recall) is folded in: picking across chapters and "Study these" covers it, now for Key cards and lesson cards alike.

**Cards view, chapter scope (the new Read), 390.**

```
+------------------------------------------+
| < Accounting for Partnership: Basic Co.. |
| Key cards                     46 cards   |
|                                          |
| ((All 46)) (Must-know 12) (In Revise 5)  |  one sliding indicator
| (Missed 2)                               |
|                                          |
| [ Flip through these 46 ]   Print sheet  |
|                                          |
| 1.2 Partnership Deed           12 cards  |  sticky section name
| ---------------------------------------- |
| Definition  Must-know                    |
| What is a partnership deed?              |
| | The written agreement which contains   |
| | the terms of partnership ...  More     |  2 lines, then More
| ---------------------------------------- |
| List                                     |
| What does a partnership deed usually     |
| contain?                                 |
| | 1. Names and addresses of the firm     |
| | and its partners ...          More     |
| ---------------------------------------- |
| ...                                      |
| 1.3 Provisions in the absence ...  9     |
| ---------------------------------------- |
+------------------------------------------+
```

(The section names and lines above illustrate the layout; the build groups by each card's real `source.section` and shows its real text.)

- **Grouping:** by `source.section` in book order, each section with its card count; the section bar sticks while its cards scroll. A "Sections" button in the header opens a jump list (all section names with counts). This turns 46 or 164 cards into 6 to 14 short groups instead of one 14,688 px list (LK4).
- **Card row:** kind line (kind, then "Must-know" as a word when true, then "In Revise" tick when true), the front in the body face, the NCERT words in the book face clipped to two lines. Tap "More" or the row: the row grows in place to the full NCERT text, source line, "In short" and the actions row "Study this card", "Add to Revise" (Pro), "Report". Only the open row shows actions, so menus do not repeat on every card.
- **Filters:** All, Must-know, In Revise, Missed (lately). The count on each chip is real. "Must-know" plus "Flip through these 12" is Last look's job, one card at a time, answers showing, nothing scheduled (mode `last_look`), swipe or arrow keys, "Previous" and "Next" keys; it ends with "That was every Must-know card. 12 cards, nothing scheduled." and two keys "Flip through again" and "Study these 12".
- **Primary action in this view:** "Flip through these {n}" when a filter is on; "Study these 46" in the bottom bar when no filter is on (it opens Cards only for the chapter). One volt key at a time.
- **Free:** the five open taste cards show in full; after them, where the first locked card would sit in book order, one row: "41 more cards in this chapter. Pro opens every card in every chapter and keeps them on a schedule." with See Pro. Filters count open cards only and say so: "Must-know 5 open".

**1440 Cards view.** Two columns: a 240 px sticky section list on the left (the jump list always visible, current section lit), the card rows in a 680 px column on the right, the filter chips and "Flip through" above them. The "Print sheet" key sits next to the filters.

**States.**

| State | What shows |
|---|---|
| Empty filter | "No missed cards in the last 7 days." / "No cards from this chapter are in Revise yet. Rate a card in a run and it joins." |
| No search results | "Nothing matches that. Try a term from the book or a chapter name." |
| Loading | Section bars and 6 row skeletons at real height. |
| Error | "The cards did not load. Check your connection and try again. Nothing you added is lost." |
| Offline (app) | Kept decks fully browsable; search runs on kept decks only with a line "Searching what this phone kept." |

### 3.8 The Explore chapter feed

Same composer and turns as the Learn run (section 4), a different skin: one item per screen, the next item comes up with a vertical swipe, and it starts from Explore (LK12). It is bounded: it ends after the chosen time with the same end screen, so it is never an endless scroll (R8 research "avoid" 4).

**Entry, Explore with a chapter chosen (390).**

```
| Explore                                  |
| Subject: Accountancy   Chapter: Admiss.. |
|                                          |
| +--------------------------------------+ |
| | (obj)  Run this chapter as a feed    | |
| | Admission of Partner                 | |
| | 10 minutes: 12 Key cards and 6       | |
| | questions, one at a time.            | |
| | [       Start the feed        ]      | |
| |  5 min   20 min                      | |
| +--------------------------------------+ |
| (existing question list continues)       |
```

**The feed (390).**

```
+------------------------------------------+
| Close   Admission of Partner   4 of 18   |
|                                          |
| +--------------------------------------+ |
| | Key line                             | |
| |                                      | |
| | The new partner brings in his share  | |
| | of ________ in cash.                 | |
| |                                      | |
| |                                      | |
| +--------------------------------------+ |
|            [   Show answer   ]           |
|                                          |
|       Swipe up for the next one          |  first run only
+------------------------------------------+
```

- The first time, a coach line teaches the gesture and the button that does the same thing (D90): "Swipe up for the next one, or tap Next." After two swipes it never shows again.
- Swipe up only works after the item is answered or rated, so a swipe never skips a rating silently; before that, the card rubber-bands at 0.35 (the `useDragCommit` rule) and the line "Rate it first" appears.
- Ratings in the feed join Revise exactly as in a Learn run (one line on the first card: "Ratings here join Revise, like in Learn."). D94's rule holds: nothing changes the schedule without a visible key.
- 1440: the feed is a 560 px column centred with the item filling about 70 percent of the viewport height; the mouse wheel or the Down key moves to the next item; a right column shows "Open the chapter" and the time left.
- App: "Untimed questions" (the app's Explore) gets the same lead card above its stream when a chapter filter is set, and the same feed screen.
- The feed logs answers with `flow_context: 'learn'` (a new allowed value), so they update chapter state like Explore answers do today.

### 3.9 The print sheet with the watermark

Pro only (B6). Reached from the chapter page's "Print sheet" row and the Cards view's "Print sheet" key. It prints the Cards view's current filter (Must-know by default; "All 46" if that filter is on), with a short confirm sheet that says what will print:

```
 Print sheet
 12 Must-know lines of Accounting for Partnership: Basic Concepts,
 in NCERT's words, with page numbers. About 2 pages.
 Every page carries the mockmob mark and your first name.
 [  Print or save as PDF  ]      Print all 46 cards instead
```

**The printed page (A4).**

```
+--------------------------------------------------------------+
| mockmob.                         Accounting for Partnership: |
|                                  Basic Concepts              |
|   m o c k m o b .            m o c k m o b .                 |
|                 m o c k m o b .            m o c k m o b .   |
| 1. What is a partnership, as the Indian Partnership Act,     |
|    1932 defines it?                                          |
|    Partnership is the relation between persons who have      |
|    agreed to share the profits of a business carried on by   |
|    all or any of them acting for all.                        |
|    Accountancy Part 1, Ch 1, p. {p}                          |
|   m o c k m o b .            m o c k m o b .                 |
| 2. ...                                                       |
|                 m o c k m o b .            m o c k m o b .   |
|                                                              |
|--------------------------------------------------------------|
| Printed for Aarav on 31 Oct 2026, 9:40 pm. Sheet MM-7F3K.    |
| mockmob.in        For your own study. Page 1 of 2            |
+--------------------------------------------------------------+
```

- The tiled mark is the lowercase mockmob wordmark, rotated -30 degrees, about 34 mm wide, repeated every 70 mm across and down, at 7 percent black. It is a fixed-position SVG layer drawn per page in `@media print`, not a CSS background, so it prints even when the browser's "Background graphics" is off (R2 note). It sits behind the text and never crosses below 4.5:1 text contrast.
- The header carries the full-colour mark (printed in black ink). The footer carries the student's first name only, the date and time in 12-hour form, and a short sheet code that maps to the account on the server (traceable without printing an email or phone number, R8 2.4).
- The same layout prints from the lesson's "Print a summary" and the chapter summary page, which today print with no mark; those stay free and gain the same footer (nothing dropped; LK6 asks for the mark on what can be copied).
- App: "Print or save" builds the same PDF on the phone (same mark, same footer) and opens the Android share sheet with the PDF. This replaces today's plain-text "Share chapter sheet" (the share stays; the text form, which carried no mark, goes).
- The page states the deterrent honestly by carrying the name; the product never claims the sheet "cannot be copied".

### 3.10 Where Must-know shows after the re-tier

Must-know becomes about one card in four per chapter (B5; R6 rule R2: top 25 percent by links, kind and Summary sections, at least 6, at most 40). Real results: Accounting for Partnership: Basic Concepts 12 of 46; Admission of Partner 13 of 53; Accounting Ratios 40 of 164; Change in Profit Sharing Ratio 6 of 8; Accountancy in all 225 of 868 (26 percent).

| Place | How it shows |
|---|---|
| Card kind line (player, Cards view, Find) | The word "Must-know" in the volt text colour after the kind, no box, no fill: `Definition   Must-know`. Shown on about one card in four. Good-to-know cards show the kind only. |
| Chapter row (map) | Not shown (one meta line rule). |
| Chapter page shelf | "46 cards, 12 Must-know, 5 in Revise". |
| Cards view filter | "Must-know 12", with "Flip through these 12". |
| Time chooser | "Quick recap, 5 min" plays Must-know only. |
| Find shelf | "Must-know, 225 cards in 14 chapters". |
| Print sheet | Prints Must-know by default. |
| Behaviour (unchanged rules, new set) | Free taste = the first 5 Must-know cards in book order (every chapter has at least 6, so every taste stays 5); Pro "Add chapter to Revise" (now in the Key cards row's menu, see section 6) adds the Must-know set; the due queue puts Must-know first. |

The overlay ships as a tier file applied in `loadDecks` (R6: no deck, hash or verdict change). The "Asked in N past papers" line stays hidden because `asked` is 0 on every card; it returns only when real paper data exists (AS9).

---

## 4. The session recipe

### 4.1 Seconds per item, and why

| Item | Seconds | Why |
|---|---|---|
| Key card (rated) | 15 | The constant already in both codebases (`minutesPerCard 0.25`, `KEYCARD_SECONDS`, app `keycards_rules.dart`); B7. |
| Key card, recap (answer showing, no rating) | 10 | A read-through has no recall step; this lets "Quick recap, 5 min" hold up to 27 cards, so it covers every chapter's Must-know set (max 40 needs 7 minutes and says so). |
| MCQ (new or an open mistake) | 60 | Quick practice's own rate (`durationPerQuestionSec 60`); B7. Revise's 40 s is for a question already seen; using 60 for all keeps one honest number. |
| Lesson | its `estimatedMinutes` (5 to 7) | Authored. |
| Feedback reading | +10 percent on the total | B7: the explanation and the line you needed after an answer. |

**Budget formula.** Usable seconds `B = minutes x 60 / 1.1`. 5 min: 272 s. 10 min: 545 s. 20 min: 1,090 s. Your own: same formula.

### 4.2 Ingredients, all from existing engines

| Code | Pool | Engine reused | What the server must add |
|---|---|---|---|
| M | Open mistakes in this chapter (Revise question cards due, or open wrong answers) | `revise_cards`, `/api/me/revise/answer` grading | a chapter filter on the Revise queue read |
| D | Due Key cards in this chapter, Must-know first | `dueQueue`, `loadStates({subject, chapter})` | pass `chapter` into `dueCards` |
| N | New Key cards in this chapter, book order, Must-know first | `deck`, `tasteIds`, Free/Pro allowances | include not-yet-added cards (rating adds them, as Study does today) |
| L | Questions linked to the cards in this run, unseen first | link files `data/keycards/links/*.json` | the inverted card-to-questions index (in memory) |
| Q | Other chapter questions, unseen first, easy 40 / medium 40 / hard 20 | the practice picker (`practice_pick.js`), `readablePracticeQuestions` | an unseen-first filter from `user_question_progress` |
| U | The chapter's unread lesson and its recall cards | study runs | a `unitId` for the chapter from the catalog |

### 4.3 Composition rules

1. **Split.** Mixed runs aim for 45 percent of `B` on cards and 55 percent on questions. Time one side cannot use (a small deck, Free's 5 open cards, a thin question pool) flows to the other side before anything shrinks. Cards only and recap are 100 percent cards.
2. **Fill order.** Lesson U first (only when the length is 20 minutes or more and the chapter has an unread lesson). Then M (1 for 5 min, 2 for 10 min, 3 for 20 min). Then D (all due, up to the card budget). Then N to the card budget. Then L (questions on cards in this run). Then Q to the question budget.
3. **Order on screen.** Blocks of three: two or three cards, then one question, preferring a question linked to a card just shown. An open mistake is placed right after its linked card when one exists (so the line comes before the retry). The first item is always a card (a calm start). The last item is a question the student has the best chance of getting right (an easy one or one linked to a card rated Got it), so the run ends on a right answer when the pool allows.
4. **Re-insertion.** A card rated Missed or a card behind a wrong answer comes back once, 3 items later, inside the same run, without extra rating cost when it is only shown as a look.
5. **Caps.** No more than 40 new cards in one run (the new-cards pause rule for heavy backlog stays: new cards pause while more than 40 are overdue, `overduePauseNew`). No more than 20 questions in a single 20-minute block; longer custom runs repeat the recipe in 20-minute blocks and may add the next chapter in book order when this chapter's pools run out, saying so before Start.
6. **Honest shrink.** If pools cannot fill `B`, the chooser says the real length ("enough for about 12 minutes today") before Start. Nothing is padded.

### 4.4 The three standard lengths, worked on real chapters

**Pro, returning, Accounting for Partnership: Basic Concepts** (46 cards, 12 Must-know, 9 cards linked to 11 questions, no lesson; student has 3 due cards and 3 open mistakes here):

| Length | Cards | Questions | Seconds (x 1.1) | On screen |
|---|---|---|---|---|
| 5 min | 3 due + 6 new = 9 (135 s) | 1 mistake + 1 linked = 2 (120 s) | 255 x 1.1 = 281 s | "3 due cards, 6 new cards, 1 open mistake and 1 question" |
| 10 min | 3 due + 13 new = 16 (240 s) | 2 mistakes + 3 linked = 5 (300 s) | 540 x 1.1 = 594 s | "3 due cards, 13 new cards, your 2 open mistakes and 3 questions" |
| 20 min | 3 due + 30 new = 33 (495 s) | 3 mistakes + 6 linked + 1 other = 10 (600 s) | 1,095 x 1.1 = 1,205 s | "3 due cards, 30 new cards, your 3 open mistakes and 7 questions" |

(The 3.3 wireframe shows the 10-minute sentence with 10 new cards and 5 questions, the new-student variant; the composer's dry run decides the exact words.)

**Pro, Admission of Partner, 20 minutes** (53 cards, 13 Must-know, lesson "Revaluation of assets and liabilities" unread, 16 cards linked to 159 questions): lesson 420 s, then 2 due + 12 new = 14 cards (210 s), 6 questions (360 s): 990 x 1.1 = 1,089 s.

**Free, Accounting for Partnership: Basic Concepts** (5 open taste cards; 10 ratings and 5 new cards a day):

| Length | Cards | Questions | Line before Start |
|---|---|---|---|
| 5 min | 5 (75 s) | 3 (180 s) | "5 open cards and 3 questions. Free opens 5 of this chapter's 46 cards." |
| 10 min | 5 (75 s) | 7 (420 s) | "5 open cards and 7 questions." |
| 20 min | 5 (75 s) | 15 (900 s) | "5 open cards and 15 questions." |

**Cards only:** 5 min is one round of 20 (300 s; the round-of-20 rule, B3), 10 min two rounds, 20 min four rounds. On Free it is the 5 open cards, then "You studied the 5 open cards." with the Pro gate, as today.

**Quick recap:** the chapter's Must-know cards at 10 s each: Basic Concepts 12 cards, about 2 minutes ("about 3 minutes" with the 10 percent and the page turns); Accounting Ratios 40 cards, about 7 minutes (the label then says "Quick recap, 7 min"). Free: the 5 open Must-know cards.

### 4.5 Free and Pro, honestly (D206, B8)

| | Free | Pro |
|---|---|---|
| Chapter map, chapter page, chooser, Find, search | all | all |
| Key cards in a run | the 5 taste cards per chapter | every card |
| Card ratings | 10 a day across Learn, Explore feed and Revise; 5 new cards a day; after the 10th the cards still show, as looks | no cap on reviews; 15 new a day (default) |
| Questions in a Learn run or the Explore feed | free, untimed, unscored, no credits (the same footing as Explore today) | the same |
| Quick practice (the scored 10-question set, Practice) | one included set a day, then 1 credit a question (unchanged) | free |
| Quick recap | the 5 open Must-know cards | all Must-know cards |
| The line you needed inside a run | shown when the card is open; a locked card shows the Pro line once | always |
| Pick cards, "Study these" | open cards | all |
| Add one card to Revise | no (as today) | yes |
| Print sheet | visible, locked | yes |
| Study plan (weekly plan) | the usual-time choice; the weekly grid locked (as today) | yes |

The first Pro sheet appears only at a real limit (D181): the 11th rating attempt in a day, or tapping a locked card or the print row.

### 4.6 What the server must add (and what it reuses)

New:
1. `GET /api/learn/subject?subject=` one read for the map: units, chapters (key, title, NCERT ref), card and Must-know counts, lesson ids, chapter state, due count, open mistakes, question count from the inventory, the student's part choice, and the last run. Replaces four reads with four different flags (R3 gap 6).
2. `POST /api/learn/runs/preview {chapterKey, minutes, mix}` the composer's dry run (counts only, no writes, cacheable for 60 s) for the live readout.
3. `POST /api/learn/runs {chapterKey | cardIds[], minutes, mix, requestKey}` composes and stores the run server-side; returns items with no answer keys.
4. `POST /api/learn/runs/{id}/answer {itemId, choice, requestKey}` grades on the server, returns `{correct, keyIndex, explanation, line}` and writes `user_question_progress` with `flow_context: 'learn'` (same effects as an Explore answer: chapter state moves, a wrong answer seeds Revise).
5. `GET /api/learn/search?subject=&q=` over chapters, lessons and Key cards (decks are already in memory per subject).
6. The Must-know tier overlay in `loadDecks`; the inverted link index; the chapter filter in `dueCards`; an unseen-first question filter.
7. `flow_context` accepts `learn`.
8. A sheet code table (`print_sheets: code, user_id, chapter_key, created_at`) for the watermark footer.

Reused unchanged: `POST /api/keycards/review` (modes `study` and `last_look`), FSRS scheduling and allowances, `lineNeeded()`, `KeyCardPlayer`, the Revise run shell's mixed-kind rendering ideas, the study run engine for lessons, `chapter_state`, `DailyMinutes`, `useDragCommit`, the app outbox.

App: the same endpoints; offline runs are composed on the phone from kept decks (cards only) with the existing `KeyCardRules.dueQueue` port; the composer's rules get a Dart port held equal by a parity test, like the display rules today.

---

## 5. Motion

All durations use the product's existing tokens where they exist (`Motion.ui` 200 ms, `Motion.card` 240 ms, enter 360 ms). Curve: `--ease-out` = cubic-bezier(0.22, 1, 0.36, 1) for enter and move; cubic-bezier(0.32, 0.72, 0, 1) for flights; springs in the app via `springs.dart` (stiffness 420, damping 34). Nothing animates from scale 0; nothing uses `transition: all`. Every motion below answers an action or shows a state (R31, AS10).

| What | Motion | Duration | Reduced motion |
|---|---|---|---|
| Got it (Study, runs, feed) | The card lifts 4 px and scales to 0.96 (100 ms), then flies up and right toward the run's progress line, shrinking to the size of the next pip while fading; the pip fills volt with a 1.15 pop and settles. Under the rating keys a receipt line fades in for 900 ms: "Back in 3 days" (from the server's `next.interval_days`). App: `confirm()` haptic on acceptance. The next card rises 8 px into place. | lift 100 ms, flight 320 ms, pip pop 180 ms, next card 240 ms | Card cross-fades out in 120 ms, the pip fills without the pop, the receipt line shows as text for 1.5 s. |
| Easy | Same flight, slightly faster (280 ms), and the pip gets a thin second ring; receipt "Back in 9 days". | 280 ms | As Got it. |
| Missed | The card tilts -3 degrees and slides down and back behind the deck edge (it will return); receipt "Back later in this run" or "Back tomorrow". App: `tick()` haptic. | 260 ms | Cross-fade, text receipt. |
| Show answer | The dashed rule draws left to right (160 ms), the answer rises 8 px and fades in (220 ms), the front dims to the secondary ink. | 220 ms | Instant swap with a 100 ms fade. |
| MCQ pick | The picked option presses (100 ms); the verdict colours ink in from the left edge of the option (200 ms); "The line you needed" slides up 16 px and fades in after the explanation (280 ms, 120 ms delay). | 100 to 400 ms total | Instant colour, the line appears without movement. |
| Start a run | The chapter page's fanned stack art moves to the player's card position and becomes the first card (shared element), while the page fades to the focus background. | 360 ms | Plain 150 ms cross-fade. |
| Time chooser | One thumb slides between length tiles (240 ms, N5); the stack art re-fans and its counts roll to the new numbers (180 ms); the Start key's label cross-fades. | 180 to 240 ms | Thumb jumps; counts change at once. |
| Part switch (LK2) | One indicator slides (240 ms); the option unit's rows cross-fade (out 160 ms, in 220 ms) inside a height animation (240 ms); nothing else moves. | 240 ms | Instant swap of the unit; no height animation. |
| Chapter row tap | The row presses (scale 0.985, 100 ms); the chapter name moves into the chapter page title position (shared element, 300 ms) on the web with the View Transitions API where supported, otherwise a 200 ms fade. | 300 ms | 150 ms fade. |
| Cards view row open | Height grows to fit with the full NCERT text fading in (240 ms spring in the app). | 240 ms | Instant. |
| Flip through (recap) | Horizontal slide of 8 percent width with fade, following the finger 1:1 (the app's existing Last look motion, now also on the web via `useDragCommit`). | 240 ms | Fade only. |
| Session end | The three numbers count up from 0 (400 ms, staggered 60 ms); Mobi plays one reaction matched to the result (good run: nod; many missed: thinking). The lead key arrives last (rise 8 px, 240 ms). This is the one authored moment on the screen. | up to 520 ms total | Numbers appear at once; Mobi shows its still pose. |
| Explore feed swipe | The item follows the finger up; past 35 percent or a 700 px/s fling it commits and the next item slides in from below; before an answer it rubber-bands at 0.35. | 260 ms | Next item appears with a 120 ms fade. |
| Map entrance | Rows rise 6 px and fade, 24 ms stagger, first 12 only, once per visit (existing `kc-rise`). Not replayed when a part or sort changes. | 260 ms | None. |

Never slowed: a control is usable before its animation ends (a second tap during a flight rates the next card only after it is on screen; taps during the flight are ignored, not queued).

---

## 6. What is folded or moved, what is kept, and the risks

### 6.1 Folded or moved (nothing he can see is dropped)

| Today | Where it goes |
|---|---|
| Key cards home `/cards` (Today box, subject tabs, part picker, chapter rows) | Learn home: the map is the chapter list; due cards are the Find shelf "Due today" and a suggestion; the part picker sits in the map at the Part 2 option. `/cards` redirects. |
| Learn hub's "Read this next" single card | The suggestions row (three, the first leading). |
| "Where you lose marks" | The map's "Marks open" sort plus the red marks number on rows in that sort; open mistakes per chapter on the chapter shelf; a suggestion when relevant. |
| "All {subject} chapters" accordions | The map (with lessons shown on their chapter rows and in the chapter page). |
| Learn search | Map filter (chapters, lessons) and Find search (adds Key cards). |
| Revise N concept cards row | Revise (it already plays them) and the Find shelf "Due today"; lesson cards appear after their lesson in runs. |
| Study preferences, Pro weekly plan | "Study plan" sheet from the map's foot row; the usual time becomes the chooser's default. |
| Pro mixed revision of chosen lessons | Find's Pick mode, "Study these". |
| Record line, "See your marks in Progress" | "Your record" at the map's foot; Progress link inside it. |
| "Test it in a full mock" | Session end option 4. |
| Chapter deck header, counts, "Add chapter to Revise" | Chapter page shelf "Key cards" row; "Add chapter to Revise" moves into the Key cards row's "..." menu and the Cards view header menu (Pro adds the Must-know set, Free the taste, as today). Rating in a run adds cards one by one, which is the main route now. |
| Read mode | Cards view (grouped, filterable, searchable). |
| Study mode | "Cards only" in the chooser and "Study these" in Cards and Find; same player, same rounds. |
| Last look | Must-know filter with "Flip through these 12", and "Quick recap, 5 min". |
| Print chapter sheet | Print sheet row and Cards view key, with the watermark. |
| App "Share chapter sheet" (text) | "Print or save" (watermarked PDF to the share sheet). |
| Lesson overview, player, summary page | Kept, linked from the chapter page's lesson row. |
| "How Learn works" (app first visit) | Kept, rewritten for the new flow. |
| On this phone (offline packs, app) | Map foot row. |
| The line you needed (result) | Kept, plus a link to its chapter page. |
| Review's "Key cards for this chapter" | "Learn this chapter, 10 minutes". |

### 6.2 Kept unchanged

The dock and the five places (B1, H5); the Start sheet layout (one row added only); the Practice UI and subjects loop (reused in Learn); Today's layout (one move added to its pool); the Key card face (kind line, prompt, NCERT words in the book face, source, In short); Study's structure, keys and rounds (B3); the FSRS scheduling, allowances and the review RPC; the card report flow; the lesson engine and screens; Revise; chapter state words and the no-mastery rules; Explore's question list (the feed is added above it); Night and Day tokens; glass only on chrome.

### 6.3 Risks, and what to do about each

| Risk | Why it matters | Mitigation |
|---|---|---|
| The map is long for Accountancy (14 rows) and Economics (17) on a phone | A long list can read as "lines of text" (LK11) | One meta line per row, part and unit grouping, sticky part headings, live filter, suggestions above. Walk Economics at 390 before showing him. |
| The owner may want Learn to feel like more than a list | He praised rich, lamp-lit art and rejected "basic" | The subjects loop and chapter-page object art carry the richness; chapter rows stay calm on purpose (R12). Show real renders, not wireframes (LK14, Never again 1). |
| Question pools per chapter are thin or unknown (`{q}`) | "Not enough content" states could appear often | Build the preview on the live inventory; the honest-shrink rule; measure pool sizes per chapter before launch and list the chapters under 10 questions. |
| Questions in Learn are free and unlimited | Could look like it undercuts Pro (D206) | Cards stay the gated value; questions match Explore, which is already free. Put the line "Questions are free" plainly so it reads as a gift, not a leak. Flag to the owner as a decision he can reverse. |
| Server grading path is new | A key leak or a double write would be a regression | Model on `/api/me/revise/answer` (server-held key, idempotent `requestKey`); tests for replay and no key in payloads. |
| Free's 10 ratings run out mid-run | A 402 mid-run feels broken | Look turns after the 10th, one line, no modal; the chooser warns before Start when fewer than the run's cards remain. |
| Must-know re-tier changes the Free taste and the "Add chapter" set | Students who already added cards see a different count | Overlay, not deck edits; existing card states are untouched; the count line changes only for new adds. |
| Two Mixed runs (Learn and Explore feed) could feel duplicated | Confusion like Read vs Last look | Same recipe, same names, same end screen; the feed is described as "this chapter as a feed". If he finds it duplicate, the feed can link to the same run with only the skin changed. |
| The app's back-gesture and pinned rating keys | Keys on the gesture bar were already a bug | Pinned bar with safe-area insets; emulator walk with screenshots (device-truth rule). |
| Watermark legibility | A heavy mark hurts reading; a light one may not show on cheap printers | 7 percent black, tested on a real laser print and a phone PDF viewer; footer text is always solid. |
| Copy drift between web and app | Already 14 drift items today (R5) | One copy file per surface checked by a parity test, as the display rules are today. |

### 6.4 One navigation change that needs his approval (drawn separately)

**Option N1 (needs the owner's yes): Learn as its own sidebar place on the desktop website only.**

```
 [>] Start a session
 Today
 Practice
    Your papers        8 due
    Explore
    Saved
 Learn                  5 due     <- a place, bold 15 px, its own icon
    Key cards to revise           <- sub-row: opens Find, Due today
 Mob, with friends
 You
```

What it gains: Learn and Key cards read as a first-class place at 1440, the place the owner said was "very small". What it costs: the website's desktop map stops matching the app's five places (D114); the rail grows by one row (44 px) and scrolls sooner on short laptop windows. The phone dock and the app bar do not change under N1. Without his yes, concept B ships with Learn as the first sub-row of Practice (2.2), which needs no approval.

---

## 7. The first 60 seconds

### 7.1 A brand-new 16-year-old (commerce, Free, no papers yet), on a phone, website

- **0 s.** She finishes onboarding and lands on Today. Among Today's first-week alternatives she sees "Try 5 minutes of Key cards / Accounting for Partnership: Basic Concepts, chapter 1 of your Accountancy book." She taps it.
- **4 s.** The chapter page opens. The title and "Part 1, Ch 1" sit next to the lamp-lit calculator object. "How long have you got?" shows 5 min chosen (from the alternative). The sentence reads: "Lined up: 5 open cards and 3 questions. Free opens 5 of this chapter's 46 cards." Under the volt "Start 5 minutes": "Ratings join Revise, so cards come back when they are due."
- **8 s.** She taps Start. The fanned card art slides into the first card. Top line: "1 of 8, about 5 min left".
- **10 s.** Card 1, Definition, Must-know: "What is a partnership, as the Indian Partnership Act, 1932 defines it?" She thinks, taps "Show answer"; the NCERT line rises in.
- **18 s.** She taps Got it. The card flies into the first pip; "Back in 3 days" fades in under the keys. She now knows what Got it does without being told.
- **20 to 40 s.** Cards 2 and 3, then a question. She picks "Allowed at 6% a year". It turns red; B turns green; "The answer is B." and two lines of reason; then "The line you needed" slides up with the card that says no interest is allowed without a deed, and "This card comes back later in this run."
- **45 s.** "Next". Card 4 rises in. The top line says "about 3 min left".
- **60 s.** She is mid-run, has seen both kinds of turn, the feedback loop and the honest time left, and has not read a single paragraph of instructions. When the run ends she gets "Next: Profit and Loss Appropriation Account, 5 minutes" as the lead with "Another 5 minutes here" and "Quick recap of this chapter" beside it.

If she had come through Practice instead: Practice (1), Learn tab (2): the Learn home shows "Start with Accounting for Partnership: Basic Concepts / Chapter 1 of Part 1. Ten minutes of its Key cards and questions." with the volt key, and two more suggestions beside it (a recap, a search). No English vocabulary lesson is pushed at a commerce student (R1 problem 14).

### 7.2 A returning student with 5 open mistakes (Pro, desktop at 1440)

His record: Admission of Partner run stopped at 6 of 16 yesterday; 5 open mistakes, 3 in Change in Profit Sharing Ratio and 2 in Admission of Partner; 24 Key cards due across Accountancy.

- **0 s.** He opens mockmob.in; Today's lead is his Revise move; one alternative reads "Pick up Admission of Partner, 4 minutes". He wants to choose himself, so he clicks "Learn, Key cards  5 due" in the sidebar.
- **3 s.** Learn home, Accountancy. Three suggestions: "Pick up Admission of Partner / You stopped at 6 of 16. About 4 minutes left. [ Pick up, 4 minutes ]", "3 cards due / Accounting Ratios, about 1 minute", "3 open mistakes / Change in Profit Sharing Ratio, with the lines you need. Fix them, 5 min". The map below shows Change in Profit Sharing Ratio with "Needs work" and "1 lesson, 3 open mistakes".
- **8 s.** He ignores the lead and clicks the Change in Profit Sharing Ratio row instead (his choice, LK9).
- **10 s.** Chapter page. 10 min is preselected (his last length). Sentence: "Lined up: 2 of your open mistakes, 2 due cards, 4 new cards and 5 questions." (the chapter has only 8 cards, 6 of them Must-know, so the unused card time flows to questions; it has 136 linked questions, so the question pool is deep). The shelf shows the lesson "Sacrificing and gaining ratios / 7-minute lesson, read" and "Your mistakes / 3 open".
- **13 s.** He switches to 20 min. The thumb slides; the sentence rolls to "Lined up: your 3 open mistakes, all 8 cards and 13 questions." He goes back to 10 min.
- **16 s.** Start 10 minutes. First item: the card "Sacrificing ratio" (Formula, Must-know), linked to his first open mistake.
- **26 s.** Got it; "Back in 3 days". Then his old mistake comes back as a question, right after its line. He gets it right: "Right. Old ratio minus new ratio." The top line's quiet count reads "1 of 2 mistakes fixed".
- **40 to 60 s.** Two due cards, then a new question; he misses one; the line you needed appears and the card is queued three items later. At 60 s he is five items in, with "about 7 min left", and the session end will offer "Fix your last open mistake" or "Next: Goodwill: Nature and Valuation, 10 minutes" depending on how the run goes.

---

Files and evidence this concept rests on: `docs/brain/OWNER-FEEDBACK-2026-10-31-LEARN.md`; `docs/brain/learn-1031/understand/R1` to `R9`; `docs/brain/OWNER-TASTE-PROFILE.md`; `docs/brain/OWNER-MASTER-LEDGER.md` (Never again, Keep); `docs/research/premium-ux-ui-2026-10/AGENT_RULES.md` (R7, R8, R10, R12, R13, R17, R18, R31, the MockMob overlay; T001, T002, S014, S016); walk screenshots `wt-1031-kc-ui/tmp/walk-1031/web/entry-learn-row-390-night.png`, `wt-1031-kc-realdeck/tmp/walk-1031/realdeck/deck-ratios-study-answer-1440-night.png`, `home-commerce-pro-accountancy-1440-night.png`, `deck-ratios-read-pro-390-night.png`, `wt-1031-keycards-app/tmp/walk-1031/app/01-learn-door-night-pro.png`. Next step before any build: real renders of 3.1, 3.3, 3.5 and 3.6 at 390 and 1440, Night and Day, shown to the owner (LK14, Never again 1).
