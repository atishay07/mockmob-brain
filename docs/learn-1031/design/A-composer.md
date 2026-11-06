# Learn concept A: "the composer leads"

Design concept, 31 Oct 2026, written by a design subagent for the CTO session. Nothing is built. It follows the owner's words in `OWNER-FEEDBACK-2026-10-31-LEARN.md` (LK1-LK14), the maps in `learn-1031/understand/R1-R9`, his taste profile, the ledger's Never again and Keep lists, his research rules (`AGENT_RULES.md`, evidence IDs cited as T001, S014 and so on, rule numbers as R7, anti-slop parts as AS2) and the CTO's decisions B1-B8. Counts come from the maps (deck counts and re-tiered Must-know from R6 rule R2; lessons from R1 and R3; linked questions from R3 and R4). Where a number depends on a live student, the wireframe says so.

---

## 1. The idea

**In three sentences.** Learn opens on one tangible object, the composer: a sentence the student builds by tapping its words ("Study **Admission of a Partner** for **10 minutes**"), with the session it will make drawn live underneath as real piles of Key cards and questions, and one lime Start key. Every suggestion Learn makes is a pre-filled composer state with its reason, so the student always sees three or four options, picks one or edits any word, and only Start begins anything. Behind the composer sit the two places the owner asked for: the chapter map (every chapter, everything it holds) and Find and revise (search any card, filter, revise or recap exactly the cards you pick), which is the new home of Read and of Last look's job.

**How it answers LK1-LK14**

| LK | His point | How concept A answers it |
|---|---|---|
| LK1 | The way to Key cards is badly placed and too small | Key cards stop being a destination behind a row. They are the main ingredient of the hero object on Learn. Learn moves to second in the Practice doors (web tab row, sidebar, app door switch), gets a "Learn a chapter" row in the Start sheet, a Learn card in Today's suggestions and swipe stack, a "Open this chapter in Learn" link under every "The line you needed", and a chapter feed in Explore. Section 2. |
| LK2 | "Your part" glitches and reorders | The part choice moves into the chapter picker sheet as a two-option toggle with an optimistic, held selection; the list re-flows with stable keys and a 220 ms FLIP, never a swap. Bug cause and fix in R2 section 5 are adopted as the base. Section 3.2. |
| LK3 | Learn as a whole is hard to use | One page grammar: compose, or browse the map, or find. Three places, one name each. Section 2. |
| LK4 | Read has a weird layout | Read becomes Find and revise: cards grouped by NCERT section with a section index, compact rows that open to the full card, filters as chips, selection. No 14,688 px scroll. Section 3.7. |
| LK5 | Study is right; add motion on Got it | Study keeps its structure (B3). Got it now sends the card to a visible "Revise pile" with its real return date stamped on it. Section 5. |
| LK6 | Print sheet with our watermark all over | Kept for Pro, tiled lowercase mockmob mark on every page plus "Printed for Aarav" on each page; the app shares a marked PDF instead of plain text. Section 3.9. |
| LK7 | Last look vs Read is confusing | Neither survives as a mode name. Read is Find and revise (a library). Last look's job is "Quick recap, 5 min" in the time chooser and the "Must-know only" filter (B4). One sentence explains each where it appears. |
| LK8 | Integrate everything better, in the flow | Lessons, Key cards, questions, open mistakes and Revise all feed one composer and one session player. One subject switcher, one chapter list (B2). |
| LK9 | Easy self-control, not weakness-led | Every word of the composer is the student's to change. Weakness becomes one suggestion among several, with its reason, never the organising idea. The student's own last composition wins over any suggestion for 12 hours. |
| LK10 | Subject, chapter, see what is lined up, time, a mix; plus a separate find-and-revise place | The composer is literally his flow: subject chip, chapter word, live "lined up" piles, time bubbles, Start. Find and revise is the separate place. |
| LK11 | No walls of text; next action clear, dynamic, with options | One lime Start key per screen. Next to it, three or four suggestion cards that change with the student's state, each one line of reason. No paragraph anywhere on Learn home. |
| LK12 | Cards are the core; bring them to Explore as a chapter feed | The composer's ingredients are Key cards first. Explore gets a "Chapter feed": the same engine, played as a swipe-up feed, cards answer-up, questions graded, bounded to the chosen minutes. Section 3.8. |
| LK13 | Too many Must-know marks | Must-know shows on the re-tiered quarter (B5) as a small mark in the kind line, not a pill, and becomes a filter and the Quick recap set. Section 3.10. |
| LK14 | Think longer, ideate better | The recipe (section 4) is computed from real engines and counts; every option has a defined state for new, returning, Free, Pro, empty, loading, error and offline. |

**Why this angle is right for him.** He praised the Start sheet twice ("Really love... Everything is super refined", N11) and asked Learn to follow a flow that is a sequence of choices. The composer is a Start-sheet sibling for learning: the same subject chips with the lamp-lit objects, the same row rhythm, the same glass sheet for pickers, the same single lime key. It is tangible (D3: "leading and interactive UI which leads you to the next thing"), it is never a form (it is a sentence with live consequences, T001: a prefilled, editable default with a result-aware button), and it gives options without losing the one leading action (R7 read with LK11; R8 precedent: Seneca's "For you" band).

---

## 2. Information architecture

### 2.1 Every place in Learn

| # | Place | Route (web) | App route | What it is for |
|---|---|---|---|---|
| P1 | Learn home | `/learn` | `/practice?door=learn` | The composer (hero), suggestions, the Find bar, the chapter map |
| P2 | Chapter picker | sheet over any page | bottom sheet | Choose subject and chapter (and the Accountancy part); also "Everything due today" |
| P3 | Chapter page ("what is lined up") | `/learn/c/<chapterKey>` (old `/cards/<key>` redirects here) | `/learn/c/:key` | Everything one chapter holds, with the composer pinned and pre-filled |
| P4 | Time chooser | inside the composer; "Your own" opens a small sheet | same | 5, 10, 20 minutes, Quick recap 5 min, your own length |
| P5 | Session player | `/learn/s/<sessionId>` | `/learn/s/:id` (pushed over the shell) | The mixed run: Key card turns, question turns, lesson steps |
| P6 | Session end | same route, end state | same | Tally, where the cards went, three next options |
| P7 | Study | `/learn/c/<chapterKey>/study` (old `?mode=study` redirects) | `/learn/c/:key/study` | Study mode, unchanged in structure: the whole chapter in book order, 20-card rounds |
| P8 | Find and revise | `/learn/find` (`?subject=&chapter=&filter=`) ; old `/cards` redirects here with the subject set | `/learn/find` | Search, filter and pick any cards; revise, recap, add to Revise or print what you picked. The new home of Read |
| P9 | Quick recap | player in recap mode, `/learn/s/<id>` with `plan=recap` | same | Last look's job: answers showing, one at a time, nothing scheduled |
| P10 | Lesson | `/learn/<unitId>` and `/study/<runId>` (kept) | kept | The 21 lessons, unchanged, now also playable as a step inside a session |
| P11 | Explore chapter feed | `/explore?feed=<chapterKey>&min=10` | `/practice/stream?feed=` | The same engine as a swipe-up feed |
| P12 | Print sheet | print layer on P3 and P8 (Pro) | marked PDF share | Must-know or picked cards, watermarked |

Revise (`/review/revise`) stays where it is (Your papers) and stays the one name for the schedule. Learn reaches it through the composer's "Everything due today" scope and through a suggestion card.

### 2.2 How they connect

```
                         Today (suggestion card, swipe stack, Revise tile)
                         Start sheet ("Learn a chapter" row)
                         Result ("Open this chapter in Learn")
                         Explore ("Chapter feed")
                                   |
                                   v
   Practice doors  -->  P1 LEARN HOME
   (Learn is 2nd)       +-----------------------------------------------+
                        | COMPOSER  [subject] [chapter] [time]  (Start) |--Start--> P5 SESSION --> P6 END
                        |   live piles: cards / questions / lesson      |                           |  |  |
                        +-----------------------------------------------+                           |  |  +--> P3 next chapter
                        | SUGGESTIONS (3-4 pre-filled composer states)   |--tap loads composer        |  +-----> P8 the cards you missed
                        | FIND BAR  ------------------------------------>|--> P8 FIND AND REVISE      +--------> P5 another round
                        | CHAPTER MAP (subject chips, units, chapters)   |--tap--> P3 CHAPTER PAGE
                        +-----------------------------------------------+          | composer pinned (same component)
                         chapter word in composer --> P2 PICKER SHEET              | Study all cards  --> P7 STUDY
                                                                                    | Find a card      --> P8 (filtered)
                                                                                    | Read the lesson  --> P10
                                                                                    | Practise 10 questions --> Quick practice setup
                                                                                    | Revise my mistakes    --> Revise (chapter filter)
                                                                                    | Print sheet (Pro)     --> P12
   P8 FIND AND REVISE: pick cards --> "Revise these 8" (P5, cards only, rated)
                                  --> "Recap these 8" (P9, nothing scheduled)
                                  --> "Add 8 to Revise" / "Print these 8" (Pro)
```

The composer is one component with two skins: the hero on P1 and P3, and a glass bottom sheet when opened from Today, the Start sheet, Explore or the result. The sheet version has the same three words, the same piles and the same Start key.

### 2.3 Navigation, website 1440 (sidebar)

No new place. Learn moves up inside Practice and gains a count (B1, D126).

```
 [ Start a session ]            <- lime key, quiet while a page owns the volt key (W-075)
   Today
   Practice
     Learn            24 due    <- moved from 3rd to 1st sub-row; count = Key cards due
     Your papers       8 due
     Explore
     Saved
   Mob, with friends
     Your standing
   You
     Progress ...
```

- Learn's sub-row carries the Key cards due count in the same style as "Your papers 8 due" (it is a real number from `GET /api/keycards`, hidden at 0).
- `/learn/*`, `/learn/find`, `/learn/c/*`, `/learn/s/*` and the redirected `/cards*` all light "Learn" and the top bar says "Learn" (fixes R9 problem 3: the bar said Learn over a page titled Key cards).
- The Start sheet (sidebar key) gains one row, section 2.6.

### 2.4 Navigation, website 390 (phone)

- Dock unchanged: Today, Practice, Start, Mob, You (B1, H5).
- Practice's tab row becomes **Practice, Learn, Your papers, Explore, Saved**. At 390 the first three fit with no swipe; Explore peeks as the scroll cue (G27).
- The tab row now also draws on `/learn/*` pages (R9 problem 2: today it disappears on `/cards`), so a student on a chapter page can move sideways. The session player hides it (and the dock), like Revise does.
- The Practice dock badge keeps the Revise count; the Learn tab carries its own "24" count chip.

### 2.5 Navigation, app

- Bar unchanged: Today, Practice, Start, Mob, You (D105, H5).
- Practice door switch becomes **Practise | Learn | Your papers** (Learn moves to the middle, 48 dp targets, same 240 ms sliding thumb). `/learn` keeps redirecting to `/practice?door=learn`.
- The Learn door shows exactly the phone layout of P1 (section 3.1, 390).
- Key cards screens (`/cards`, `/cards/:chapter`) redirect to `/learn/find` and `/learn/c/:key`.

### 2.6 Learn's prominence from elsewhere (no nav change)

| Surface | What is added | Copy |
|---|---|---|
| Start sheet (web and app) | One row between "By chapter" and "Smart practice". It opens the composer as a sheet, with the subject already set by the sheet's chosen subject chip | Title "Learn a chapter", line "Key cards and questions, 5 to 20 minutes", cost slot "Free taste" on Free, "Included" on Pro |
| Today, lead card's alternatives (web) | A Learn move joins the pool (`alternatives()`): it is a composer state | "Learn: Admission of a Partner, 10 minutes" |
| Today, Suggested for you swipe stack (app) | A Learn card type. Right swipe makes it Up next exactly as today (D94: it never starts anything); tapping Start on the lead opens the composer sheet pre-filled | Title "Admission of a Partner", evidence line "5 open mistakes, 13 cards tied to them", cost line "10 minutes, free" |
| Today, Revise tile | Unchanged; the Key cards line now links "See them in Learn" | "3 Key cards among them. See them in Learn" |
| Result, "The line you needed" | A quiet link under "Add both to Revise" | "Open this chapter in Learn" (goes to P3 with the composer pre-filled) |
| Review chapter rows | "Key cards for this chapter" becomes | "Learn this chapter" (P3) |
| Explore | A "Chapter feed" band at the top (section 3.8) | "Feed me a chapter" |
| Guide tour | The Learn stop is rewritten | "Pick a chapter and a length. Learn lines up Key cards and questions for you." |

### 2.7 One navigation change that needs his yes (drawn separately; not part of the concept unless he approves)

**Option N, desktop sidebar only: Learn becomes its own place.**

```
   Today
   Practice
     Your papers   8 due
     Explore
     Saved
   Learn           24 due      <- bold place row, 15 px, like Practice
     Find and revise
   Mob, with friends
   You
```

- For: on a 1440 screen Learn reads as a first-class place, not a sub-page, which is the strongest answer to LK1 on the website (the main product).
- Against: breaks "same five places as the app" (D114) on desktop only; adds about 44 px to a rail that already compacts below 900 px tall (WEB-NAV-1019 measured 976 px). The phone dock and the app bar do not change under this option.
- Ask: "Learn as its own place in the desktop sidebar, phone unchanged?" Yes / Keep it inside Practice.

### 2.8 Taps from opening the site to studying a chapter's cards

Counting taps or clicks; scrolling is not counted. "Studying" means the first Key card is on screen.

| Student | Surface | Path | Taps |
|---|---|---|---|
| New, phone web | Today | dock Practice (1), Learn tab (2), Start 10 minutes on the pre-filled composer (3) | 3 |
| New, phone web, chooses a chapter | Today | Practice (1), Learn (2), chapter word (3), chapter row in the sheet (4), Start (5) | 5 |
| New, any page | Start key | Start (1), Learn a chapter (2), Start 10 minutes (3) | 3 |
| New, 1440 | Today | Learn sub-row (1), Start (2) | 2 |
| Returning, phone web | Today | tap the Learn alternative under the lead card (1), Start in the composer sheet (2) | 2 |
| Returning, 1440 | Today | Learn (1), Start (2) (the composer holds their last chapter and length) | 2 |
| Returning, app | Today | swipe the Learn card right (1, Up next), Start on the lead (2), Start in the composer sheet (3) | 3 |
| Any, wants Study mode (whole chapter, rounds of 20) | Learn | chapter row on the map (1), Study all 53 (2) | 2 from Learn |
| Any, wants one specific card | Learn | Find bar (1), type "sacrificing", tap the result (2) | 2 from Learn |

Today the same jobs take 4 to 5 taps on a phone and need the student to find a footnote row (R9 section 3.3).

---

## 3. Screens

Conventions for the wireframes. `[ Lime key ]` is the one volt fill on screen. `( Quiet key )` is an outlined or text key. `{ chip }` is a pressable chip. `<obj>` is the lamp-lit 3D subject object. `~~` marks glass chrome (sheets and bars only, never content). All copy is the real copy, sentence case. Numbers are real deck numbers unless marked "live"; a student's due counts, mistakes and dates are live values shown as examples. The sacrificing ratio definition and formula cards (p. 54) are real cards seen in the walk; the question stem, the "Key line" row and the "Gaining ratio, p. 55" line are illustrative items, to be replaced by real deck and bank items in the renders.

### 3.1 P1 Learn home

**Hierarchy.** 1) The composer, with its Start key (the only lime key). 2) Suggestions beside it (1440) or under it (390). 3) The Find bar. 4) The chapter map. Mobi appears once, on the composer, reacting to the length chosen.

**One leading action:** "Start 10 minutes". **Options beside it:** three or four suggestion cards, each loads the composer; the three words of the composer; "Find a card".

#### 1440, returning Pro student (Accountancy, 5 open mistakes in Admission of a Partner, 24 cards due)

```
+--sidebar--+------------------------------------------------------------------------------------------------+
| [Start a  |  Learn                                                                                         |
|  session] |  Pick a chapter and a length. We line up the Key cards and questions.                          |
| Today     |                                                                                                |
| Practice  |  +----------------------------------------------------------+  Or load one of these           |
|  Learn 24 |  |  <calculator obj>                              (Mobi)    |  +----------------------------+ |
|  Your     |  |                                                          |  | > Loaded                   | |
|  papers 8 |  |  Study  [ Admission of a Partner v ]                     |  | Admission of a Partner     | |
|  Explore  |  |  for    [ 10 minutes v ]                                 |  | 5 open mistakes. 13 cards  | |
|  Saved    |  |  Accountancy {change}                                    |  | are tied to them.          | |
| Mob       |  |                                                          |  +----------------------------+ |
| You       |  |  Lined up                                                |  | Revise what is due         | |
|           |  |   _____      _____                                       |  | 24 Key cards in 5 chapters | |
|           |  |  |_____|    (  ?  )                                      |  | About 6 minutes            | |
|           |  |  |_____|    (  ?  )                                      |  +----------------------------+ |
|           |  |  |_____|    (  ?  )                                      |  | Next in the book           | |
|           |  |  12 Key     6 questions                                  |  | Retirement/Death of a      | |
|           |  |  cards                                                   |  | Partner. 65 cards, new     | |
|           |  |  4 due today, 3 Must-know. Each question follows the     |  +----------------------------+ |
|           |  |  card it tests.                                          |  | Quick recap                | |
|           |  |                                                          |  | Goodwill: Nature and       | |
|           |  |  { 5 }  ( 10 )  { 20 }  { Quick recap }  { Your own }    |  | Valuation. 10 Must-know    | |
|           |  |                                                          |  | cards, nothing scheduled   | |
|           |  |  [         Start 10 minutes          ]                   |  +----------------------------+ |
|           |  |  Free for you on Pro. Cards you rate join Revise.        |                                 |
|           |  +----------------------------------------------------------+                                 |
|           |                                                                                                |
|           |  +------------------------------------------------------------------------------------------+ |
|           |  | (search)  Find any card, lesson or chapter                         Find and revise  >      | |
|           |  +------------------------------------------------------------------------------------------+ |
|           |                                                                                                |
|           |  Chapters                                                                                      |
|           |  {<obj> Accountancy}  {<obj> Business Studies}  {<obj> Economics}  {<obj> English}  ...        |
|           |  Your part  ( Analysis of Financial Statements )  { Computerised Accounting }                  |
|           |                                                                                                |
|           |  Accounting for Partnership                                                                    |
|           |  +-----------------------------+ +-----------------------------+                               |
|           |  | Accounting for Partnership: | | Profit and Loss              |                              |
|           |  | Basic Concepts              | | Appropriation Account        |                              |
|           |  | Part 1, Ch 1   Getting there| | Not started                  |                              |
|           |  | 46 cards, 3 due             | | 42 cards                     |                              |
|           |  +-----------------------------+ +-----------------------------+                               |
|           |  Reconstitution of a Partnership firm                                                          |
|           |  +-----------------------------+ +-----------------------------+ +-------------------------+  |
|           |  | Change in Profit Sharing    | | Goodwill: Nature and        | | Admission of a Partner  |  |
|           |  | Ratio        Needs work     | | Valuation      Holding      | | Getting there           |  |
|           |  | 8 cards, 1 lesson           | | 39 cards                    | | 53 cards, 1 lesson,     |  |
|           |  |                             | |                             | | 5 mistakes              |  |
|           |  +-----------------------------+ +-----------------------------+ +-------------------------+  |
|           |  ... every unit, in NCERT order                                                                |
+-----------+------------------------------------------------------------------------------------------------+
```

- The composer card is 760 px wide; the suggestions column is 340 px; both top-aligned. The chapter map is a 3-column grid of pressable tiles (F5: they read as buttons: hover lift 2 px, chevron on hover, 44 px minimum targets).
- Chapter tile line: state word (Not started, Too few answers, Needs work, Getting there, Holding, from `chapter_state.js`) and counts that only name what exists: "53 cards, 1 lesson, 5 mistakes". No marks-lost minus numbers on Learn (that lens lives in Your papers, LK9, C2).
- The loaded suggestion shows "Loaded" with a volt hairline on its left edge (not a fill). Tapping another suggestion moves that marker and rolls the composer words.

#### 390, the same student

```
+------------------------------------------+
| mockmob.                       (68) (P)  |
|------------------------------------------|
| { Practice } ( Learn 24 ) { Your papers 8 } { Exp
|------------------------------------------|
|                                          |
| Learn                                    |
|                                          |
| +--------------------------------------+ |
| |                        <calc obj>    | |
| | Study                                | |
| | [ Admission of a Partner v ]         | |
| | for [ 10 minutes v ]                 | |
| | Accountancy {change}                 | |
| |                                      | |
| |  _____     _____                     | |
| | |_____|   (  ?  )                    | |
| | |_____|   (  ?  )                    | |
| | 12 Key    6 questions                | |
| | cards                                | |
| | 4 due today, 3 Must-know             | |
| |                                      | |
| | {5} (10) {20} {Recap} {Your own}     | |
| |                                      | |
| | [       Start 10 minutes       ]     | |
| +--------------------------------------+ |
|                                          |
| Or load one of these                     |
| +-------------------+ +-----------------+|
| | > Loaded          | | Revise what is  ||
| | Admission of a    | | due             ||
| | Partner           | | 24 Key cards,   ||
| | 5 open mistakes   | | about 6 min     ||
| +-------------------+ +-----------------+|
|   (snap row; the 2nd card peeks)         |
|                                          |
| +--------------------------------------+ |
| | (search) Find any card or chapter    | |
| +--------------------------------------+ |
|                                          |
| Chapters                                 |
| {<obj> Accountancy} {<obj> Business Stu  |
|                                          |
| Accounting for Partnership               |
| Accounting for Partnership: Basic    >   |
| Concepts                                 |
| Getting there          46 cards, 3 due   |
| ---------------------------------------- |
| Profit and Loss Appropriation        >   |
| Account                                  |
| Not started                  42 cards    |
| ...                                      |
|~~[Today] [Practice] (Start) [Mob] [You]~~|
+------------------------------------------+
```

- The composer fills the first screen down to the Start key at about 640 px on a 844 px phone, with a real gap under the status bar (D40) and nothing under the dock.
- The part picker sits under the subject chips in the map only when Accountancy, Mathematics or Computer Science is chosen, as two pill options on one line (it no longer pushes chapters off the first screen, R5 problem 10).

#### App (Learn door)

Same as 390, inside Practice with the door switch above it ("Practise | Learn | Your papers"). Differences: the composer sheet versions use the app's glass sheet; Start fires `hapticsProvider.confirm()`; the piles use the app's `card_stack.dart` pile art.

#### States of P1

| State | What shows |
|---|---|
| New student, no history | Composer pre-filled with the student's first CUET subject (from onboarding), its first chapter in NCERT order, 10 minutes. Reason line under the piles: "Chapter 1 in the book. A good place to start." Four suggestions (G12: never one): "Start at chapter 1" (loaded), "Most questions are tied to its cards: Admission of a Partner, 159 questions" (true from the link files), "Quick recap, 5 minutes: Accounting for Partnership: Basic Concepts. Nothing scheduled", "Pick your own chapter". Mobi first-visit line beside the composer, once: "Tap any word to change it." |
| Returning | Composer holds the student's last composition if it was set in the last 12 hours, else the lead suggestion (rule in section 4.6). Suggestions are recomputed on every visit. |
| Free | Same composer. The piles show what Free really gets for this chapter (section 4.4), for example "5 Key cards, 6 questions, about 7 minutes" and one quiet line under the Start key: "Free opens 5 cards a chapter. Pro lines up all 53." No modal, no Pro ask before a real limit (D181). |
| Pro | As drawn. Line under Start: "Cards you rate join Revise." |
| Empty: subject with no cards and no lessons (for example Computerised Accounting System) | The chapter word still works; piles show only questions: "No Key cards for this chapter yet. 10 questions instead." Start becomes "Start 10 minutes of questions". |
| Empty: chapter with no questions in the bank | Piles show cards only; line "No questions in this chapter yet, so this is all Key cards." |
| Loading | The composer frame and its words draw at once from the last kept state (local storage on web, kept copy on the app); the piles show a 2-line shimmer for at most 600 ms, then count up. Suggestions draw as three grey card outlines. Nothing jumps: every block has a fixed height. |
| Error (catalog or Key cards read fails) | The composer stays usable with what loaded; the failed part says so in its own slot: "Key cards did not load. Questions still work." with "Try again". Never a full-page error while anything works (R2 section 5 fix). |
| Learn switched off (flag) | The Learn door and tab hide; Start sheet row hides; Today card hides. Same rule as today: an entry never leads to a broken page. |
| Offline (app) | Strip under the title: "Offline. Showing what this phone kept." Composer works for chapters whose decks are kept; piles show cards only: "Questions come back when you are online." Start reads "Start 10 minutes of Key cards". Chapters not kept show "Needs a connection" in the picker. |

### 3.2 P2 Choosing subject and chapter (the picker sheet)

Opened by tapping the chapter word or the subject "change" in the composer, from any skin.

**Hierarchy.** Subject chips on top (one switcher for all of Learn, B2), the part toggle if the subject has parts, a search field, then units and chapters. One row is "Everything due today" at the very top. Leading action: tapping a chapter row (it closes the sheet and rolls the composer word). No Start key here: Start belongs to the composer (one lime key).

#### 390

```
+------------------------------------------+
|~~~~~~~~~~~~~~~~ grab bar ~~~~~~~~~~~~~~~~|
|~ Choose a chapter                 (Done)~|
|~                                        ~|
|~ {<obj> Accountancy} {<obj> Business St ~|
|~                                        ~|
|~ Your part                              ~|
|~ ( Analysis of Financial ) { Computer-  ~|
|~ (   Statements          ) { ised Acc.  ~|
|~ Only that part's chapters show here    ~|
|~ and in your practice.                  ~|
|~                                        ~|
|~ +------------------------------------+ ~|
|~ | (search) Search Accountancy        | ~|
|~ +------------------------------------+ ~|
|~                                        ~|
|~ Everything due today                 > ~|
|~ 24 Key cards in 5 chapters, Revise     ~|
|~ -------------------------------------- ~|
|~ Accounting for Partnership             ~|
|~ Accounting for Partnership: Basic    > ~|
|~ Concepts        Getting there  46 cards ~|
|~ Profit and Loss Appropriation        > ~|
|~ Account          Not started  42 cards ~|
|~ Reconstitution of a Partnership firm   ~|
|~ Change in Profit Sharing Ratio       > ~|
|~ Needs work      8 cards, 1 lesson      ~|
|~ Goodwill: Nature and Valuation       > ~|
|~ Holding                     39 cards   ~|
|~ Admission of a Partner          (tick) ~|
|~ Getting there   53 cards, 1 lesson     ~|
|~ ...                                    ~|
+------------------------------------------+
```

At 1440 the same content is a 520 px popover anchored to the chapter word, with the subject chips as a row and the chapters in two columns per unit.

**LK2 behaviour.** Tapping "Computerised Accounting" sets the toggle at once and holds it (local `saved` state until the server body agrees, R2 section 5 minimal fix). Rows keep stable keys by chapter key. The five Analysis of Financial Statements chapters fade and collapse (180 ms) while the Computerised Accounting System row slides in (220 ms FLIP), and the list never reorders. The line under the toggle has a fixed height and reads "Saving your choice" until the save lands. On failure the toggle stays where the student put it with "Not saved yet. Try again." and a retry.

**States.** Loading: chips and 6 row shimmers. Error: "Chapters did not load. Try again." Offline (app): chapters without a kept deck are dimmed with "Needs a connection". Free: every chapter is listed; no lock icons on rows (Free sees 5 cards in every chapter, so every row is usable).

### 3.3 P3 The chapter's "what is lined up" page

This replaces the deck page's header, counts, Add, Share and the Read / Study / Last look switch (R5 measured 1,080 px of chrome before the first card on a phone).

**Hierarchy.** 1) Title block with the subject object and three numbers. 2) The composer, pinned and pre-filled with this chapter (the leading action is still its Start key). 3) "In this chapter": one row per thing the chapter holds, each with its own quiet action (the options).

#### 1440, Pro, returning

```
+-----------+------------------------------------------------------------------------------------------------+
| sidebar   |  ( < Learn )                                                                                   |
|           |                                                                                                |
|           |  Admission of a Partner                                               <calculator obj>         |
|           |  Accountancy Part 1, Ch 2                                                                      |
|           |                                                                                                |
|           |     53              13               4                  5                                      |
|           |     Key cards       Must-know        due today          open mistakes                          |
|           |                                                                                                |
|           |  Getting there. 7 of 12 right on the latest try at each question. Cards: 14 of 20 holding.     |
|           |                                                                                                |
|           |  +-------------------------------------------+   In this chapter                               |
|           |  | Study  Admission of a Partner             |   ------------------------------------------    |
|           |  | for [ 10 minutes v ]                      |   Key cards                                     |
|           |  |   _____      _____                        |   53 cards, 13 Must-know, 20 in Revise          |
|           |  |  |_____|    (  ?  )                       |   ( Study all 53 )  ( Find a card )             |
|           |  |  12 Key      6 questions                  |   ------------------------------------------    |
|           |  |  cards                                    |   Lesson                                        |
|           |  |  4 due, 5 tied to your mistakes           |   Revaluation of assets and liabilities         |
|           |  |                                           |   7 minutes, new                                |
|           |  | {5} (10) {20} {Recap} {Your own}          |   ( Read the lesson )   ( Add it to the session )|
|           |  |                                           |   ------------------------------------------    |
|           |  | [        Start 10 minutes        ]        |   Questions                                     |
|           |  +-------------------------------------------+   159 questions are tied to these cards         |
|           |                                                   ( Practise 10 questions )                     |
|           |                                                   ------------------------------------------    |
|           |                                                   Your mistakes here                            |
|           |                                                   5 open, 1 left blank                          |
|           |                                                   ( Revise them, about 5 minutes )              |
|           |                                                   ------------------------------------------    |
|           |                                                   Print sheet                                   |
|           |                                                   The 13 Must-know cards, with your name on     |
|           |                                                   every page  ( Print )                         |
+-----------+------------------------------------------------------------------------------------------------+
```

#### 390, Free, new to this chapter

```
+------------------------------------------+
| ( < Learn )                              |
|                                          |
| Accounting for Partnership:   <calc obj> |
| Basic Concepts                           |
| Accountancy Part 1, Ch 1                 |
|                                          |
|   46          12           0             |
|   Key cards   Must-know    due today     |
|                                          |
| +--------------------------------------+ |
| | for [ 10 minutes v ]                 | |
| |  _____     _____                     | |
| | |_____|   (  ?  )                    | |
| | 5 Key     6 questions                | |
| | cards                                | |
| | About 7 minutes. Free opens 5 cards  | |
| | a chapter.                           | |
| | {5} (10) {20} {Recap} {Your own}     | |
| | [       Start 7 minutes        ]     | |
| +--------------------------------------+ |
|                                          |
| In this chapter                          |
| Key cards                                |
| 5 of 46 open on Free, 12 Must-know       |
| ( Study the 5 )   ( Find a card )        |
| ---------------------------------------- |
| Lesson                                   |
| No lesson for this chapter yet           |
| ---------------------------------------- |
| Questions                                |
| 11 questions are tied to these cards     |
| ( Practise 10 questions )                |
| ---------------------------------------- |
| Pro opens all 46 cards and the print     |
| sheet.                     ( See Pro )   |
|~~[Today] [Practice] (Start) [Mob] [You]~~|
+------------------------------------------+
```

- The four numbers are value-before-label (R9). "Due today" and "open mistakes" are hidden when 0 for a new student, so a new student sees two or three numbers, never zeros that read as failure.
- The Pro reason line (state word plus "7 of 12 right...") is kept from today and shown only on Pro with 6 or more answers (no percent under 6, chapter_state rule).
- "Add it to the session" adds the lesson ingredient to the composer (the piles grow a third pile, "1 lesson, 7 min", and the readout recomputes).
- The Free "Start 7 minutes" is honest: the Free session for a 10-minute choice is shorter because only 5 cards are open (section 4.4).

#### States of P3

| State | What shows |
|---|---|
| Loading | Title and reference from the map's cached row; numbers shimmer; composer frame drawn |
| Chapter has no Key cards | Key cards row: "No Key cards for this chapter yet". Composer piles: questions only |
| Chapter has no questions | Questions row: "No questions in this chapter yet". Composer: cards only |
| Chapter left the syllabus or bad link | "This chapter is not in Learn. It may have left the CUET syllabus, or the link is old." ( See all chapters ) |
| Error | Each row fails alone with its own "Try again"; the composer stays |
| Offline (app) | Numbers from the kept deck; Questions and Your mistakes rows: "Needs a connection"; composer cards only |
| Free | As drawn: "5 of 46 open on Free"; one Pro line at the foot, never more than one per screen |

### 3.4 P4 Choosing the time

The time row lives inside the composer. It is not a segmented form control; it is a row of five bubbles with one sliding volt-outline indicator (N5: one indicator slides, never two boxes).

```
 { 5 }  ( 10 )  { 20 }  { Quick recap }  { Your own }
         ^^^^ indicator
```

- Tapping a length moves the indicator (240 ms) and the piles grow or shrink with a count-up (section 5). That is the live readout D47 and N1 asked for: the control visibly does something.
- **Quick recap** (B4): the length is fixed at about 5 minutes; the piles change to one pile, "13 Must-know cards, answers showing", and the line under it reads "A fast look at the core lines. Nothing is scheduled." Start reads "Start the recap".
- **Your own** opens a small sheet (glass chrome):

```
+------------------------------------------+
|~ How long?                              ~|
|~                                        ~|
|~   {15}  {30}  {45}  {1 hour}           ~|
|~                                        ~|
|~        (-)    25 minutes    (+)        ~|
|~                                        ~|
|~ This chapter fills about 34 minutes.   ~|
|~ Longer runs carry on into the next     ~|
|~ chapter, Retirement/Death of a Partner.~|
|~                                        ~|
|~ [            Use 25 minutes         ] ~|
+------------------------------------------+
```

- No upper cap (H1: never cap a motivated student). When the minutes exceed what the chapter holds, the readout says so and offers to continue into the next chapter in book order; the student can change that chapter in the same sheet.
- The chosen length is remembered per student (T004, R16), and Today's usual minutes are the first default when no Learn length was ever chosen (10 if nothing is known).

### 3.5 P5 The mixed session player

Full screen, dock and tab row hidden (like Revise). The top bar is glass chrome.

**Hierarchy.** 1) The item (card or question). 2) Its one action (Show answer, or the options). 3) A thin progress bar and "7 of 18". A clear "End" button, not only an icon (D43).

#### A Key card turn, 390 (front, then revealed) — this is Study's player, unchanged in structure

```
+------------------------------------------+
|~ ( End )  Admission of a Partner   7/18 ~|
|~ =========-------------  about 6 min left~|
|                                          |
|  Key card. Definition, Must-know         |
|  +------------------------------------+  |
|  |                                    |  |
|  |  What is the sacrificing ratio?    |  |
|  |                                    |  |
|  |  - - - - - - - - - - - - - - - - - |  |
|  |                                    |  |
|  +------------------------------------+  |
|                                          |
|  [          Show the answer         ]    |
|                                          |
|  ( Revise pile: 6 )                      |
+------------------------------------------+

            ...after Show the answer...

+------------------------------------------+
|~ ( End )  Admission of a Partner   7/18 ~|
|~ =========-------------  about 6 min left~|
|  Key card. Definition, Must-know         |
|  +------------------------------------+  |
|  |  What is the sacrificing ratio?    |  |
|  |  ----------------------------------|  |
|  | | The ratio in which the old       |  |
|  | | partners agree to sacrifice      |  |
|  | | their share of profit in favour  |  |
|  | | of the incoming partner is       |  |
|  | | called sacrificing ratio.        |  |
|  |  Accountancy Part 1, Ch 2, p. 54   |  |
|  +------------------------------------+  |
|                                          |
|  How did it go?                          |
|  ( Missed )  [ Got it ]  ( Easy )        |
|                                          |
|  ( Revise pile: 6 )                      |
+------------------------------------------+
```

- The card face, the NCERT words in the book face, the reference, Show the answer, Missed / Got it / Easy with keys 1, 2, 3 and Space are Study's exactly (B3). "Got it" keeps its volt fill as today on the website (it is the one volt element after reveal; the Show the answer key is gone by then).
- "Revise pile: 6" is a small stack mark at the bottom left. It counts the cards this session has scheduled. Got it and Easy fly the card into it (section 5).

#### A question turn, 1440 (the next item, linked to the card above)

```
+-----------+------------------------------------------------------------------------------------------------+
|           |~ ( End )   Admission of a Partner          8 of 18    =========---------   about 6 min left   ~|
|           |                                                                                                |
|           |   Question. Tests the card you just saw                                                       |
|           |   +----------------------------------------------------------------------------------------+  |
|           |   | A and B share profits 3:2. C is admitted for 1/5 share, which he takes 1/10 from A and |  |
|           |   | 1/10 from B. What is the sacrificing ratio of A and B?                                  |  |
|           |   +----------------------------------------------------------------------------------------+  |
|           |   (A)  1:1                                                                                    |
|           |   (B)  3:2                                                                                    |
|           |   (C)  2:3                                                                                    |
|           |   (D)  1:2                                                                                    |
|           |                                                                                                |
|           |   Pick an answer. It is checked on our side, then you see why.                                 |
+-----------+------------------------------------------------------------------------------------------------+
```

- "Tests the card you just saw" shows only when the question is linked to that card in the link files; otherwise the label is "Question" alone (R4 gap 2: never claim a pairing that does not exist).
- One tap answers (no confirm), as in Explore and Revise. The answer is checked by the server (no key in the payload, section 4.5).

#### A wrong answer, showing the line you needed, 390

```
+------------------------------------------+
|~ ( End )  Admission of a Partner   8/18 ~|
|~ ==========------------  about 5 min left~|
|  Question                                |
|  A and B share profits 3:2. C is         |
|  admitted for 1/5 share, which he takes  |
|  1/10 from A and 1/10 from B. What is    |
|  the sacrificing ratio of A and B?       |
|                                          |
|  (A) 1:1                     correct  v  |
|  (B) 3:2                     your pick x |
|  (C) 2:3                                 |
|  (D) 1:2                                 |
|                                          |
|  The answer is A. Each gives up 1/10,    |
|  so they sacrifice equally.              |
|                                          |
|  The line you needed                     |
|  | The ratio in which the old partners   |
|  | agree to sacrifice their share of     |
|  | profit in favour of the incoming      |
|  | partner is called sacrificing ratio.  |
|  Accountancy Part 1, Ch 2, p. 54         |
|  This card comes back in this session.   |
|                                          |
|  [            Next             ]         |
+------------------------------------------+
```

- The line comes from the link files first, else the matcher (R3 section 5). Inside a session it costs no Free "line" allowance when the card is one of the session's own cards. If the card is locked on Free: "The line for this is in a Pro card." and no gate sheet.
- "This card comes back in this session": the linked card is re-queued once, 3 items later, as a Key card turn (the recipe's one in-session repeat).
- A right answer shows "Right. Keep the reasoning." and the explanation collapsed to one line with "Why" to open it (no wall of text).

#### A lesson step (when the lesson is an ingredient)

The lesson plays first, using the existing lesson player blocks (The idea, Worked example, Common mistake, Quick check, not scored) inside the same top bar. Its own recall cards follow it as Key-card-style turns labelled "Card from the lesson". The step count for the lesson is shown as part of the session total.

#### States of P5

| State | What shows |
|---|---|
| Starting | The composer card expands into the player (section 5). If the session read is slow, the first item is a Key card from the kept deck, so something is on screen at once |
| Rating not saved | Under the keys: "That rating was not saved. Try again." The card stays (as today) |
| Answer not checked (network) | "Not checked yet. Try again." The pick stays highlighted |
| Free reviews used mid-session (should not happen: the composer sizes Free sessions to what is left) | If it does: "Today's free card reviews are used. The questions in this session still work." ( Go on with the questions ) |
| Offline (app) | Card turns work and queue in the outbox; question turns are not in an offline session (it was composed as cards only) |
| End early | ( End ) asks nothing: it goes to the end screen with what was done. Everything rated is already saved |
| Resume | Leaving and coming back within 12 hours shows a "Finish your session, 7 of 18" suggestion that loads first |

### 3.6 P6 Session end, with next options

**Hierarchy.** 1) What happened, in three numbers. 2) Where the cards went (the Revise pile fans open). 3) One lead next option (lime) and two or three others. Mobi reacts once to the tally.

#### 390

```
+------------------------------------------+
|~ ( Done )                               ~|
|                                          |
|  10 minutes on Admission of a Partner    |
|                              (Mobi nods) |
|     9            3            4 of 6     |
|     Got it       Missed       questions  |
|     or Easy                  right       |
|                                          |
|  Your Revise pile                        |
|  [card][card][card][card] +8             |
|  3 back tomorrow, 7 on Tuesday,          |
|  2 on 9 Nov                              |
|                                          |
|  The 2 lines you needed                  |
|  Sacrificing ratio, p. 54           >    |
|  Gaining ratio, p. 55               >    |
|                                          |
|  What next                               |
|  [ Go again on the 3 you missed, 1 min ] |
|                                          |
|  ( Another 10 minutes here )             |
|  ( Next chapter: Retirement/Death of a   |
|    Partner )                             |
|  ( Read the 13 Must-know cards )         |
|                                          |
|  ( Print sheet )   ( Back to Learn )     |
+------------------------------------------+
```

- Return dates are the server's real `next.due_at` values, grouped, in plain dates (no "mastered", no percent).
- **Lead rule (dynamic, LK11):** 3 or more cards missed: "Go again on the N you missed". Else 2 or more questions wrong: "Revise the N questions you missed". Else the chapter still has unseen open cards: "Another 10 minutes here". Else: "Next chapter: <next in book order>". The other options are the remaining three of these, plus "Read the 13 Must-know cards" (opens P8 filtered) and, on Pro, Print.
- At 1440 the same content is two columns: the tally and the pile on the left, the What next list on the right.
- Free: one line above What next: "Pro lines up all 53 cards in this chapter." with ( See Pro ). This is a real limit moment (the Free session ran out of open cards), so D181 allows it.

### 3.7 P8 Find and revise (the new home of Read, with Last look's job folded in)

**What it is.** A library of every Key card and lesson, searchable, filterable, grouped by NCERT section, where the student picks exactly what to revise. It answers LK10's "separate section that easily shows them what exactly to find where, or ... separately revise ... some specific cards".

**Hierarchy.** 1) Search field. 2) Filter chips. 3) Results grouped by chapter and NCERT section, as compact rows that open to the full card. 4) When cards are ticked, a glass action bar rises with the actions. Leading action: none until something is picked (it is a browsing place); with a selection, "Revise these 8" is the lime key.

#### 1440

```
+-----------+------------------------------------------------------------------------------------------------+
| sidebar   |  ( < Learn )   Find and revise                                                                 |
|           |  +------------------------------------------------------------------------------------------+  |
|           |  | (search) ratio                                                                           |  |
|           |  +------------------------------------------------------------------------------------------+  |
|           |  { Accountancy v }  { Admission of a Partner v }  ( Must-know only )  { In Revise }           |
|           |  { Missed last time }  { Kind v }                                    9 cards match            |
|           |                                                                                                |
|           |  Sections            | Admission of a Partner                                                  |
|           |  2.4 New profit      |  2.5 Sacrificing ratio                                                  |
|           |      sharing ratio 3 |  [ ] Definition, Must-know                                              |
|           |  2.5 Sacrificing     |      What is the sacrificing ratio?                                     |
|           |      ratio         4 |      The ratio in which the old partners agree to sacrifice their...    |
|           |  2.7 Goodwill      2 |      p. 54                                                    In Revise |
|           |                      |  [ ] Formula                                                            |
|           |                      |      Sacrificing ratio                                                  |
|           |                      |      Old Share of Profit - New Share of Profit                          |
|           |                      |      p. 54                                                              |
|           |                      |  [x] Key line                                                           |
|           |                      |      The incoming partner brings in his share of ______ ...             |
|           |                      |      p. 55                                              Missed Tuesday  |
|           |                      |  ...                                                                    |
|           |                                                                                                |
|           |~ 3 picked      ( Recap these )   ( Add to Revise )   ( Print these )   [ Revise these 3 ]    ~|
+-----------+------------------------------------------------------------------------------------------------+
```

- A row shows the kind (with Must-know only when true), the front, the first line of the NCERT words (truncated with an ellipsis at the end of a word), the page and the card's state ("In Revise", "Missed Tuesday", "Due today"). Tapping the row opens it in place to the full card (NCERT words, source, In short, the report menu), 220 ms height animation. This keeps every piece of the old Read entry, one tap away, so nothing is lost (Never again 2), while the list stays scannable (R12).
- The section index (left at 1440) comes from `source.section` on every card. It jumps and shows counts.
- "Must-know only" is B4's filter. "Recap these" plays the picked or filtered cards in the Quick recap player (answers showing, one at a time, nothing scheduled, server `mode: last_look`). "Revise these 3" plays them in the session player with ratings (scheduled). "Add to Revise" schedules without playing. "Print these" is Pro.
- With no chapter filter and no query, the page opens on the student's current subject, grouped by unit and chapter, collapsed to chapters with counts ("Admission of a Partner, 53 cards, 13 Must-know").

#### 390

```
+------------------------------------------+
| ( < Learn )  Find and revise             |
| +--------------------------------------+ |
| | (search) Find a card or chapter      | |
| +--------------------------------------+ |
| {Accountancy v} {Admission of a Pa..v}   |
| (Must-know only) {In Revise} {Missed} >  |
|                                          |
| 2.5 Sacrificing ratio            4 cards |
| ---------------------------------------- |
| [ ] Definition, Must-know                |
|     What is the sacrificing ratio?       |
|     The ratio in which the old part...   |
|     p. 54                    In Revise   |
| ---------------------------------------- |
| [ ] Formula                              |
|     Sacrificing ratio                    |
|     Old Share of Profit - New Share...   |
|     p. 54                                |
| ---------------------------------------- |
| 2.7 Goodwill                     2 cards |
| ...                                      |
|~ 2 picked  (Recap) (Add)  [Revise these 2]~|
+------------------------------------------+
```

- The section header is sticky while its cards scroll under it. Long-press or the tick box picks a card; a first-visit coach line under the filters says once: "Tick cards to revise just those."
- Free: the 5 open cards per chapter are full rows; the rest show as one row per chapter, "41 more cards in this chapter are in Pro", in place of the first locked card (as Read did). Search finds locked cards by their front and says "In Pro" on the row, so a Free student learns what exists (D206: a taste of everything).
- Lessons appear in results as rows with a lesson mark: "Lesson. Revaluation of assets and liabilities, 7 minutes" (opens P10).

**States.** Loading: 6 row shimmers under live filters. No match: "Nothing matches 'ratoi'. Try a chapter name or a word from the book." Empty filter (for example In Revise with nothing added): "No cards in Revise from this chapter yet. Rate a card in a session and it lands here." Error: "Cards did not load. Try again." Offline (app): searches kept decks only, with "Searching what this phone kept".

### 3.8 P11 Explore chapter feed

**Where.** A band at the top of Explore (web) and a new first row in the app's "Untimed questions" screen header. Explore's question list stays below it, unchanged (Keep: Explore, D21).

#### Band, 1440 and 390

```
+------------------------------------------------------------------+
|  Feed me  [ Admission of a Partner v ]  for  [ 10 minutes v ]    |
|  Key cards and questions, one after another. Swipe up for next.  |
|                                          ( Start the feed )      |
+------------------------------------------------------------------+
```

The key is an outlined quiet key here: Explore's page has no lime key of its own and the dock Start key stays the one volt fill (W-075). The band is the composer's sheet skin flattened, with the same two words.

#### The feed, 390 (one item per screen, swipe up or tap Next)

```
+------------------------------------------+
|~ ( End )  Chapter feed    3 of about 16 ~|
|                                          |
|  Key card. Formula                       |
|                                          |
|  Sacrificing ratio                       |
|                                          |
|  | Old Share of Profit -                 |
|  | New Share of Profit                   |
|  Accountancy Part 1, Ch 2, p. 54         |
|                                          |
|  In short: what each old partner gives   |
|  up for the new one.                     |
|                                          |
|  ( Keep this card )                      |
|                                          |
|              swipe up                    |
|  ( Previous )            [ Next ]        |
+------------------------------------------+
```

- In the feed, cards show their answers (no rating) and nothing is scheduled; "Keep this card" adds it to Revise. Questions are answered and explained as in Explore today and recorded with `flow_context: 'explore'`, so they move chapter state and seed Revise like any Explore answer. This is the honest difference from a Learn session, and the band line says it in one sentence the first time: "The feed is for browsing. A Learn session schedules what you rate."
- First run: the top card nudges 24 px up and settles, with the line "Swipe up for the next one" (D90: teach the gesture). Every swipe has a button doing the same thing (Next, Previous).
- Bounded: after about the chosen minutes, an end card: "That was 10 minutes. 9 cards, 5 questions, 4 right." ( Another 10 minutes ) ( Open this chapter in Learn ).
- Free: cards are the 5 open ones, then a single item "41 more cards in this chapter are in Pro" that does not block; the feed continues with questions (Explore questions are free and unlimited today, and stay so).

### 3.9 P12 The print sheet with the watermark

Pro only (B6). Reached from P3 ("Print sheet"), P6 ("Print sheet") and P8 ("Print these"). The website prints from a print layer; the app builds a PDF on the phone and opens the share sheet with the PDF (the plain-text "Share chapter sheet" is folded into this; nothing unmarked leaves the app).

#### One printed page (A4)

```
+--------------------------------------------------------------+
|  mockmob.          mockmob.          mockmob.          mockm |   <- the lowercase wordmark, tiled at
|        mockmob.          mockmob.          mockmob.          |      -30 degrees, 7 percent black, 64 mm
|  Admission of a Partner                                      |      apart, on every page, over and under
|  Accountancy Part 1, Ch 2. 13 Must-know cards in NCERT's     |      the text (it never hides a word: it
|  exact words, each with its page.    mockmob.          mockm |      is light enough to read through)
|                                                              |
|  1. What is the sacrificing ratio?                           |
|     The ratio in which the old partners agree to sacrifice   |
|     their share of profit in favour of the incoming partner  |
|     is called sacrificing ratio.          mockmob.           |
|     Accountancy Part 1, Ch 2, p. 54                          |
|                                                              |
|  2. Sacrificing ratio                                        |
|     Old Share of Profit - New Share of Profit                |
|     Accountancy Part 1, Ch 2, p. 54                          |
|  mockmob.          mockmob.          mockmob.          mockm |
|  ...                                                         |
|--------------------------------------------------------------|
|  Printed for Aarav on 31 Oct 2026, 6:40 pm. mockmob.in       |
|  Page 1 of 3                                                 |
+--------------------------------------------------------------+
```

- The mark is a repeated element positioned per page (not a CSS background), so it prints even with "Background graphics" off (R2 note). The footer line repeats on every page: "Printed for <first name> on <date>, <12-hour time>. mockmob.in. Page n of N". First name only, no email or phone (privacy, R8 section 2.4).
- What prints: from P3 the chapter's Must-know cards (the re-tiered set, for example 13); from P8 exactly the picked cards, or the filtered set if none are picked; from P6 the session's cards.
- On screen, before the print dialog, a one-line preview sheet: "13 cards, 3 pages, with your name on every page." ( Print ). Free sees "Print sheet" in the chapter row with "Pro" beside it; tapping it opens the existing Pro sheet (it is a real limit).
- Copy for the owner to confirm (his "Fitzmeen downloading" guess): this design reads it as "fine for them to download, but it must carry our mark". If he meant "prevent downloading", the app's PDF share becomes print-only and the web keeps print with no "Save as PDF" hint; the mark stays either way.

### 3.10 Where Must-know shows after the re-tier

Must-know becomes the top quarter of each chapter (B5; R6 rule R2: score by question links, card kind and NCERT Summary sections; at least 6, at most 40; 1,427 of 5,800 cards; median 18 a chapter). It shows in five places, always the same word:

| Place | How it shows |
|---|---|
| A card's kind line (session, Study, Find, feed, Revise) | "Definition, Must-know" with a 6 px volt dot before "Must-know". No pill, no outline. On about one card in four |
| Chapter page | The number "13 Must-know" in the title block |
| Composer readout | "3 Must-know" inside the cards pile line, and the Must-know cards in the pile carry a volt corner |
| Find and revise | The "Must-know only" filter chip |
| Quick recap and the print sheet | They play and print the Must-know set by default |

Rules that used the old flag move with it: the Free taste becomes the first 5 Must-know cards of the new tier in book order (each chapter has at least 6, so every chapter still has 5); Pro "Add chapter to Revise" (now "Add the 13 Must-know cards to Revise" on P3's Key cards row menu) adds the new tier; due ordering stays Must-know first. Delivered as the tier overlay file R6 recommends, so no deck hash or manifest changes.

---

## 4. The session recipe

### 4.1 Inputs and the time model

Input: `{ scope: chapterKey | 'due', minutes, plan: 'mix' | 'recap', include: {cards, questions, lesson}, isPro, now }`.

Seconds per item (B7): a Key card 15 s (the code's own figure, `KEYCARD_RULES.minutesPerCard 0.25`), a question 60 s (Quick practice's figure, `durationPerQuestionSec 60`), plus 10 percent for reading feedback. So the usable budget is `minutes x 60 / 1.1`.

Why these: 15 s matches how long a reveal and a rating take on Study's short NCERT lines; 60 s is the existing practice clock and leaves room for the explanation and the line you needed after a wrong answer. Revise's 40 s per question replays a question the student has already seen, which is faster than a new one, so it is not used here. Neither figure is measured (R3: no per-card dwell is stored). The session records real seconds per item from the first day, and the readout's estimate is recalibrated per student after 3 sessions (shown as "about", never as a promise).

### 4.2 The split: two cards for every question

| Choice | Key cards | Questions | Lesson | Raw seconds | With 10 % | Readout |
|---|---|---|---|---|---|---|
| 5 min | 6 | 3 | no | 90 + 180 = 270 | 297 | "6 Key cards, 3 questions" |
| 10 min | 12 | 6 | no | 180 + 360 = 540 | 594 | "12 Key cards, 6 questions" |
| 20 min | 24 | 12 | offered | 360 + 720 = 1,080 | 1,188 | "24 Key cards, 12 questions" |
| 20 min with the lesson | 12 + the lesson's 5 cards | 6 | 7 min lesson | 420 + 255 + 360 = 1,035 | 1,139 | "1 lesson, 17 cards, 6 questions" |
| Quick recap | about 18 (all Must-know, cap 20) | 0 | no | up to 300 | n/a | "13 Must-know cards, answers showing" |
| Your own, N min | 1.2 N | 0.6 N | at 15 min and above, if unread | | | as computed |

Rule: per minute, 1.2 cards and 0.6 questions (18 s + 36 s = 54 s, plus 10 percent = 59.4 s). The interleave is card, card, question, with a linked question placed straight after the card it tests. The 10-minute choice in his words ("a 10-minute lesson") gives 18 items, which keeps each session short enough to finish (Seneca caps items per topic for the same reason, R8).

Cards only and questions only are possible by tapping a pile off ("Left out"); the remaining ingredient takes the whole budget (10 minutes of cards = 36 cards; of questions = 9).

### 4.3 What fills each slot, from real engines

**Key card slots, in this order** (all from `data/keycards.js` and the deck, filtered by chapter):
1. Cards of this chapter due today (`dueQueue` ordering: Must-know first, then oldest due). Uses `loadStates(userId, {chapter})`, which already exists.
2. Cards linked to the student's open mistakes in this chapter (question -> card link files, `lineNeeded` sources).
3. Cards rated Missed in the last 7 days and not yet due.
4. New cards in book order, Must-know before Good-to-know within each NCERT section.
Cards in the session are rated with Study's player (`mode: 'study'`), so a rated card joins Revise exactly as Study does today.

**Question slots, in this order:**
1. The student's own wrong answers in this chapter that are due in Revise (they play through `POST /api/me/revise/answer`, unchanged, and move the Leitner box).
2. Questions linked to the cards played in this session, not attempted in the last 14 days (needs the inverted link index).
3. Other questions of the chapter, unseen first, difficulty 40 / 40 / 20 easy, medium, hard (Quick practice's mix).
Thin link chapters (Accounting for Partnership: Basic Concepts has 9 linked cards and 11 linked questions; Financial Statements of a Company has 2 and 3) fall through to step 3 and never claim a pairing.

**Lesson slot:** the chapter's unread lesson from `/api/study/catalog` (15 chapters have one), played with the existing run engine, then its recall cards ("Card from the lesson"). Offered by default at 15 minutes and above; addable at any length from P3, in which case cards and questions shrink to fit and the readout says the new mix.

**Scope "Everything due today" (Revise):** the Revise queue (`mergeQueue`) trimmed to the minutes: questions 40 s, Key cards 15 s, as Revise counts them today. This is the only place Learn uses Revise's 40 s, because these are replays.

**Quick recap:** the chapter's Must-know cards in book order, answers showing, `mode: 'last_look'` (logged, never scheduled, no allowance), at most 20 cards (about 5 minutes).

**One in-session repeat:** a card rated Missed, or the line you needed after a wrong answer, comes back once, 3 items later. It adds about 15 s; the time left line accounts for it.

### 4.4 Free and Pro, honestly

| | Free (a taste, D206) | Pro |
|---|---|---|
| Key cards in a session | The chapter's 5 open cards (first 5 Must-know of the new tier); within today's 10 reviews and 5 new cards | Every card; no new-card cap inside a session the student composed (H1); the daily 15 new cards governs only what Revise introduces by itself |
| Questions | Drawn from today's included 10 questions (the same daily set Quick practice uses); the readout says "Uses 6 of today's 10 free questions". After that: 1 credit a question, shown before Start ("6 questions, 6 credits. You have 68."), or leave questions out | Unlimited, no credits |
| Lesson | Free (lessons are free today) | Free |
| Quick recap | The open Must-know cards (5) | All Must-know |
| The line you needed | Free inside a session for the session's own cards; outside, 3 a day as today | Unlimited |
| Find and revise | Search everything; the 5 open cards per chapter are full; locked cards listed with "In Pro" | Everything; pick any cards |
| Print sheet | Not offered (Pro line) | Yes |
| Explore feed | 5 open cards, then questions (free, unlimited) | All cards |

What a Free student sees for "10 minutes" on Admission of a Partner: "5 Key cards, 6 questions. About 7 minutes. Uses 6 of today's 10 free questions." and the Start key reads "Start 7 minutes". The composer never promises 10 minutes it cannot fill, and never hits a 402 mid-session: it sizes the session to what is left today (reviews left, new cards left, questions left). If nothing is left: "Today's free cards are used. They come back tomorrow." with the options "Questions only, 10 minutes" (credits shown) and "Quick recap, nothing scheduled" (recap uses no allowance).

### 4.5 Reused, and what the server must add

**Reused as is:** the Key card review RPC and FSRS schedule; `dueQueue`, `tasteIds`, `chapterAddSet`, `lineNeeded`; `KeyCardPlayer` (Study's player); the Revise answer route for own mistakes; the Revise run shell (`ReviseRun` ticks, per-kind players, summary) as the base of the session player; the lesson run engine and blocks; Quick practice's chapter canonicalisation and syllabus option; `chapter_state.js` and `GET /api/me/chapters`; `allocateMinutes` vocabulary and `DailyMinutes` for "Your own"; the app's outbox, kept decks and `card_stack.dart`; `useDragCommit` (web) for the feed.

**The server must add:**
1. `GET /api/learn/compose?scope=&minutes=&plan=&include=` (read only, cheap): returns the readout (counts by ingredient, Must-know count, due count, linked-to-mistakes count, Free limits left, estimated seconds). It drives the live piles. Cached per student for 60 s.
2. `POST /api/learn/sessions` `{scope, minutes, plan, include, requestKey}`: freezes the ordered item list and returns it (cards whole; questions without key or explanation).
3. `POST /api/learn/sessions/{id}/answer` `{itemId, choice, requestKey}`: server-graded, no credit for Pro or within the Free included set, writes `user_question_progress` (so Learn sessions move chapter state and seed Revise, as Explore does), returns `{correct, keyIndex, explanation, line: [cards]}`. Own-mistake items route to the existing Revise answer.
4. A chapter filter on the Key card due queue (`dueCards({chapter})`; `loadStates` already supports it).
5. The inverted link index (card -> questions), built in memory from the link files on load.
6. A session record (`learn_sessions`: student, scope, minutes, items, seconds per item, ended_at) for resume, the end screen and recalibrating the time model.
7. The Must-know tier overlay file applied in `loadDecks` (R6), and the same rules in the Dart port and fixtures.
8. A `minutes` parameter on the Revise queue for the "Everything due today" scope.
9. A chapter inventory check in the readout (R3 missing 5: thin chapters must fail in the readout, never at Start).

### 4.6 How suggestions are chosen (pre-filled composer states)

Computed on the client from reads Learn already makes (`/api/keycards`, `/api/me/chapters`, `/api/me/revise`, the catalog), at most four, never one (G12):

1. **Finish your session** (an unfinished session in the last 12 hours): "Finish your session, 7 of 18".
2. **Mistakes, with the cards behind them** (a chapter with open mistakes from the last 14 days and linked cards): "Admission of a Partner. 5 open mistakes. 13 cards are tied to them."
3. **Revise what is due** (10 or more Key cards due): "Revise what is due. 24 Key cards in 5 chapters. About 6 minutes."
4. **Pick up where you were** (last chapter studied, unfinished): "Goodwill: Nature and Valuation. You stopped at card 14 of 39."
5. **Next in the book** (the next chapter in NCERT order after the last finished one): "Retirement/Death of a Partner. 65 cards, new."
6. **Quick recap** (a chapter with Must-know cards rated before and none due): "Quick recap. Goodwill: Nature and Valuation. 10 Must-know cards, nothing scheduled."
7. **Another subject** (when every suggestion is in one subject and the student has more): "Business Studies: Nature and Significance of Management."

Which one is loaded into the composer: the student's own composition from the last 12 hours, if any (their choice beats ours, LK9); else the first of 1-5 that applies. Every suggestion's reason is a fact from their record (MockMob overlay rule 1; AS9). For a new student the reasons are book facts only ("Chapter 1 in the book"), never invented history.

---

## 5. Motion

All curves: `ease-out` = `cubic-bezier(0.2, 0.8, 0.2, 1)`; springs are critically damped unless stated. Motion explains state (R31, AS10). Reduced motion: every transform becomes a 120 ms opacity change, and every piece of information carried by motion is also in text.

| What moves | Motion | Duration and curve | Reduced motion |
|---|---|---|---|
| Composer word change (picker or suggestion) | The old word slides up 12 px and fades, the new one rises from 12 px below; the line re-wraps with a FLIP on the words after it | 220 ms ease-out, new word starts 40 ms after the old leaves | Cross-fade 120 ms |
| Loading a suggestion | The tapped suggestion card lifts 2 px and its title travels into the composer's chapter word (shared element); the "Loaded" hairline slides to the new card | 360 ms spring (stiffness 380, damping 32); hairline 240 ms ease-out | The word cross-fades; the hairline jumps |
| Time bubbles | One volt-outline indicator slides to the chosen bubble (N5: one indicator) | 240 ms ease-out | Jumps |
| The piles | Cards are added to or taken off the top of each pile one at a time, 30 ms apart, max 8 animated then the rest snap; the count under the pile counts up or down | 280 ms per card, count-up 400 ms ease-out | Counts change instantly |
| Leaving an ingredient out | The pile tilts back 6 degrees, dims to 40 percent and gets the label "Left out" | 200 ms ease-out | Dim only |
| Start | Key press scale 0.97 (100 ms); the composer card expands to fill the screen and becomes the player frame; the first card deals off the cards pile into the centre | 420 ms spring (stiffness 300, damping 30) | Fade to the player, 160 ms |
| Show the answer (Study, kept) | Answer reveals as today (fade and 8 px rise) | 220 ms (unchanged) | Unchanged |
| **Got it (his ask, LK5)** | The card lifts (scale 1.02, 80 ms), tilts 4 degrees, and flies down-left into the "Revise pile" mark, shrinking to its size; a stamp "Back on Tuesday" (from the server's `next.due_at`) shows on the card for the flight; the pile count ticks up with a 1.0 to 1.15 to 1.0 pop; the next card rises in. Soft click (existing `studyFeel.softClick`, honours the sound setting); app: `haptics.confirm()` | Lift 80 ms, flight 420 ms spring (stiffness 260, damping 26), pop 180 ms, next card 240 ms starting at 300 ms | The card fades out, the line "Back on Tuesday" shows under the keys for 1.2 s, the count changes |
| Easy | Same as Got it, flight a little longer and higher; stamp "Back on 9 Nov" | 480 ms | As Got it |
| Missed | The card drops 6 px, then slides left into a "Soon" slot beside the pile; stamp "Back tomorrow" or "Back in this session"; app: `haptics.tick()` | 360 ms ease-out | Text line only |
| A question answered | Picked option ink fills from the tap point (Study's ink motion); right answer inks green; wrong pick tints red, then the right one inks | 200 ms ease-out | Colour change only |
| The line you needed | Slides up under the explanation | 280 ms ease-out | Appears |
| Progress bar | Width eases; time-left text updates every item | 260 ms ease-out | Jumps |
| Session end | The Revise pile fans out into the row of card marks and the return-date line types in by group; tally numbers count up; Mobi reacts once (nod for under half right, cheer for most right) | Fan 480 ms spring, count-up 600 ms ease-out, Mobi 900 ms | Static row and numbers |
| Part toggle (LK2) | Toggle indicator slides; leaving chapter rows collapse; arriving rows slide in; rows never reorder | 180 ms collapse, 220 ms FLIP | Instant swap, no reorder |
| Find: open a row to the full card | Height animates; the NCERT words fade in | 220 ms ease-out | Instant |
| Find: picking cards | The tick draws; the action bar rises from below (glass) | 160 ms tick, 240 ms bar | Instant |
| Explore feed swipe | Follows the finger 1:1 (`useDragCommit`), commits past 35 percent or 700 px/s, the next item rises; first run nudge 24 px up | Spring 300 / 30 | Next and Previous buttons, fade |
| Sheets (picker, Your own) | Glass sheet rises, backdrop dims to 40 percent | 320 ms spring | Fade |

Motion is never worse than today's: Study's reveal, keys, thumb and progress are kept and only added to (Never again 5).

---

## 6. What is folded or moved, what is kept, the risks

### 6.1 Folded or moved (nothing he can see is dropped)

| Today | Where it goes |
|---|---|
| Learn hub's "Read this next" lime panel (one pick) | Becomes one of the suggestions (the lesson pick appears as "Read the lesson: Sacrificing and gaining ratios, 7 minutes" when it is the best fact), and the lesson is an ingredient |
| "Where you lose marks" and the red minus numbers | The mistakes suggestion on Learn; the chapter page's "Your mistakes here" row; the full marks-lost view stays in Your papers (D18, N13) |
| "All <Subject> chapters" accordion | The chapter map (one list for lessons and Key cards, 6 subjects) |
| Learn's 4-subject tabs and Key cards' subject tabs | One subject switcher (B2), the student's own subjects first, then the others |
| Key cards home `/cards` (Today box, Pro line, chips, part picker, rows) | Today box: the "Revise what is due" suggestion and the Learn tab count. Part picker: P2 and the map. Rows: the chapter map. Pro line: the composer's Free line. `/cards` redirects to Find |
| Deck page header, counts, reason line | Chapter page title block and numbers; reason line kept on Pro |
| "Add chapter to Revise" | Chapter page, Key cards row menu: "Add the 13 Must-know cards to Revise"; Find: "Add to Revise" for any pick |
| Read mode | Find and revise (grouped, searchable; every element of a Read entry is one tap away) |
| Last look | "Quick recap, 5 min" in the time chooser, "Recap these" in Find, the "Must-know only" filter (B4) |
| Study mode | Kept, as "Study all 53" on the chapter page and as the card turn of every session (B3) |
| Print chapter sheet (web) and Share chapter sheet (app) | Print sheet with the watermark (web print, app PDF share) |
| Per-card "Add this card to Revise" and "Report this card" menu | In Find's opened card and in the session card's menu |
| "Revise N concept cards" row | The lesson ingredient's cards and Revise; also a suggestion when due |
| Study preferences (subjects, usual time) and Pro weekly plan and mixed revision | Usual time feeds the composer's default length; the preferences fold moves to You > Study plan (unchanged content); Pro mixed revision of lessons becomes Find's "Revise these" with lessons pickable |
| Search ("Search chapters and lessons") | The Find bar, now covering Key cards too |
| "Test it in a full mock" row | The session end's options include it when the subject has had 3 sessions this week: "Test it in a full mock" |
| Learn record line ("0 of 21 lessons read ...") | Chapter page numbers and You > Progress (unchanged) |
| Today's Key cards line, Review's "Key cards for this chapter", result's line | Kept, relabelled to point at Learn (section 2.6) |

### 6.2 Kept unchanged

Study's structure and player (B3); the card faces, NCERT words and references (D202); FSRS scheduling and ratings Missed / Got it / Easy; Revise and its run; the 21 lessons and their player; the bottom bar and the Start sheet (one row added, nothing changed); Explore's question list; the swipe stack (one card type added); chapter state words; the result page (one link added); the Free numbers (B8).

### 6.3 Risks

| Risk | Why | Mitigation |
|---|---|---|
| The composer reads as a form | It has three choices and a button | It is a sentence, the defaults are always filled, the consequence is drawn live, and a suggestion fills all three in one tap. The critic checks it against taste item 5 in a real render before anything ships |
| Too much on Learn home at 390 | Composer, suggestions, Find bar, map | Order is fixed and each block is one idea; suggestions are a snap row, not a stack; the map is below the fold by design |
| Two cards-only paths (Study all, and a cards-only session) | Both exist | Different jobs, each said in its label: "Study all 53" (whole chapter, book order, rounds of 20) vs "10 minutes" (lined up for you). Kept because Study is what he praised |
| Free questions draw on the daily included set | A Learn session could spend the set a student meant for Quick practice | The readout says so before Start; Explore questions remain free and unlimited |
| Time estimates are unmeasured | 15 s and 60 s are guesses | Always "about"; real seconds recorded from day one; recalibrated per student after 3 sessions |
| Link coverage is thin (about one card in five; 13 percent in Political Science) | "Tests the card you just saw" would rarely show | It shows only on real links; other questions are chapter-level and labelled "Question" |
| Server-graded answers are new code | Today's free graded path is Revise-only | New route reuses Revise's grading pattern; key never in the payload |
| Must-know re-tier changes Free taste and Pro add sets | Behaviour, not just a label | Overlay file plus fixtures and the Dart port updated together; taste stays 5 per chapter (every chapter has at least 6) |
| Redirecting `/cards` routes | Old links, the app's routes | Redirect every old route (`/cards`, `/cards/<key>`, `?mode=study`, `?mode=last`, `?mode=last-look`) to its new home |
| Practice door reorder | Muscle memory for "Your papers" | It is one position; the count chip keeps Your papers easy to spot. Shown to him in the mock-up first |
| Refine vs rebuild | He rejected rebuilt screens three times | He asked for this flow himself (LK10); everything he praised is kept; real renders at 390 and 1440, Night and Day, go to him before any build (Never again 1, LK14) |

---

## 7. First 60 seconds

### 7.1 Aarav, 16, new, commerce (Accountancy, Business Studies, Economics, English), Free, phone web, 7:40 pm

| Second | What he sees and does |
|---|---|
| 0 | Today. Under the lead card's alternatives he sees "Learn: Accounting for Partnership: Basic Concepts, 10 minutes". He has also seen the Learn tab in Practice during the tour. He taps the alternative |
| 3 | A glass sheet rises: the composer. "Study Accounting for Partnership: Basic Concepts for 10 minutes." Two small piles: "5 Key cards, 6 questions." Line: "About 7 minutes. Free opens 5 cards a chapter. Uses 6 of today's 10 free questions." Mobi beside it: "Tap any word to change it." |
| 8 | He taps "10 minutes", sees the bubbles; taps 5. The indicator slides; the piles shrink to "5 Key cards, 3 questions, about 5 minutes". He taps 10 again |
| 14 | He taps "Start 7 minutes". The sheet grows into the player; a card deals to the centre: the chapter's first Must-know card, a definition, front only. One lime key: "Show the answer" |
| 20 | He taps it. The NCERT definition appears with its book, chapter and page. Keys: Missed, Got it, Easy. He taps Got it |
| 22 | The card tilts and flies into the small pile at the bottom left; the stamp on it says "Back on Monday"; the pile reads 1. The next card rises. He understands, without being told, that Got it put the card somewhere and when it returns |
| 40 | Two cards later, a question: "Question. Tests the card you just saw" (a linked one). He picks wrong. The right option inks green, his turns red, the one-line reason shows, and "The line you needed" slides up with the definition he just rated. "This card comes back in this session." |
| 55 | Next. He is in the flow of the owner's LK10 example, 4 taps after Today, with no paragraph read |

### 7.2 Meera, returning, Pro, app, 5 open mistakes in Admission of a Partner, 24 Key cards due, 9:10 pm

| Second | What she sees and does |
|---|---|
| 0 | Today. In "Suggested for you" the top card reads "Admission of a Partner. 5 open mistakes, 13 cards tied to them. 10 minutes." She swipes it right: it moves into the lead card as Up next (nothing starts, D94) |
| 4 | She taps Start on the lead. The composer sheet: "Study Admission of a Partner for 10 minutes." Piles: "12 Key cards, 6 questions. 4 due today, 5 tied to your mistakes, 3 Must-know." |
| 9 | She would rather go longer tonight. She taps 20. The piles grow to 24 and 12, and a third pile appears: "1 lesson, 7 minutes: Revaluation of assets and liabilities. Leave it out?" She taps the lesson pile to leave it out (it dims, "Left out"); the readout says "24 Key cards, 12 questions, about 20 minutes" |
| 15 | She notices the suggestions row under the composer: "Revise what is due. 24 Key cards in 5 chapters." She keeps her choice and taps "Start 20 minutes". Haptic confirm |
| 18 | First item: one of her own wrong questions from Mock 2 ("A question you got wrong"), played through Revise's grading. She gets it right this time; Revise moves it up a box |
| 30 | Next, the card linked to it. She taps Show the answer, rates Easy: the card flies farther into the pile, stamped "Back on 12 Nov" |
| 45 | A new linked question; right. Progress "4 of 36", "about 18 min left". |
| 60 | She is working her weak chapter, but because she chose it, at the length she chose, with the alternatives in view the whole time (LK9, LK11). At the end, the lead option will be "Go again on the 3 you missed, 1 minute", with "Next chapter: Retirement/Death of a Partner" and "Revise what is due, 24 cards" beside it |

---

## Appendix: evidence and rules this concept leans on

- T001 (prefilled, editable defaults with a result-aware button): the composer's pre-filled sentence and "Start 10 minutes" naming the session; R13 (defaults backed by real context: last composition, usual minutes, book order).
- T002 and R17 (labelled steps, truthful progress): "7 of 18", time left as "about", no percentages.
- T004 and R16 (authorship persisted): the last composition and length are remembered.
- T005 and R22 (no coercive loss framing): the Free line states limits plainly; no countdowns.
- S014 and R10 (progressive disclosure for secondary functions only): Find's rows open to the full card; the Key cards entry is never hidden.
- S016 and R11 (consistent identification): one name per thing (Key cards, lesson, questions, Revise, Must-know); Read and Last look retired as names.
- R7 with AS2 (one primary action) read together with LK11: one lime Start, suggestions as subordinate options with reasons.
- R18 (say what happens next): the live piles and the Free line.
- AS9 (no pseudo-evidence): suggestion reasons are record facts; "Tests the card you just saw" only on real links; Must-know on a quarter of cards by a stated rule.
- R31 and AS10 (motion with purpose): Got it shows where the card went and when it returns.
