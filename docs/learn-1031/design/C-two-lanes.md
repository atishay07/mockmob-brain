# Learn concept C: two lanes, "For you" and "Your way"

Written 31 Oct 2026 (evening) as a design concept only. No code was changed. Inputs: the owner's LK1-LK14 (OWNER-FEEDBACK-2026-10-31-LEARN.md), the nine maps in `learn-1031/understand/` (R1-R9), OWNER-TASTE-PROFILE.md, the ledger's Never again and Keep lists, AGENT_RULES.md, and the walk screenshots (web `entry-learn-row-1440-night`, `deck-study-answer-390-night`; realdeck `home-commerce-pro-accountancy-390-night`; app `01-learn-door-night-pro`). The CTO decisions B1-B8 are treated as fixed.

Counts used below come from the maps: chapter card totals and Must-know re-tier figures from R6 (rule R2: top quarter, at least 6, at most 40), linked questions from R3 and R4, lessons from R1. Card and question wording inside wireframes is sample wording to show layout; the build shows the deck's own card and the bank's own question. Where the maps have no number (for example a chapter's full question bank), the wireframe shows the linked-question count and says so.

---

## 1. The idea

**In three sentences.** Learn opens on one screen with two labelled lanes: "For you", where MockMob puts three next moves side by side, each with the evidence behind it, how sure it is, and a 5, 10 or 20 minute choice; and "Your way", where the student picks a subject and a chapter themselves, and finds or revises any card in the Library. Whichever lane they start from, they land in the same place: a chapter page that shows everything the chapter holds and what is lined up, a time chooser, and one Start key that names the session, which then plays Key cards and questions mixed together, in Study's own card player. The same session reaches the student from Today, the Start sheet, the result screen and Explore (as a 10-minute chapter run), so Key cards stop being a footnote row and become the core of Learn.

**Why this answers LK1-LK14**

| LK | What he said, short | How this concept answers it |
|---|---|---|
| LK1 | The way to Key cards is badly placed and too small | Learn moves to the second tab of Practice (web phone row, web sidebar, app door switch). Key cards are no longer a row inside Learn: Learn's home is built from them (both lanes lead to card sessions). Five more doors: a Learn tile on Today, a "Study a chapter" row in the Start sheet, "Open this chapter" and "10 minutes on this chapter" under the line you needed on results, Explore's chapter runs, and Review's chapter link (kept). New student reaches a first Key card in 3 taps on a phone (section 2.5). |
| LK2 | "Your part" glitches and shuffles | The part choice becomes one quiet line under the subject chips ("Your part: Analysis of Financial Statements. Change"), opening a two-choice sheet. The choice is held locally until the server agrees (R2's fix), the chapter list keeps stable keys and animates its height, and rows never replay their entrance. |
| LK3 | Learn as a whole is not good or easy to use | One home with two named lanes replaces the stack of lesson card, concept-card row, Key cards row, search, four subject tabs, "Where you lose marks" and accordions. One subject list (the student's own subjects), one chapter list, one chapter page. |
| LK4 | Read inside a chapter has a weird layout | Read moves to the Library (section 3.7): cards grouped by NCERT section with a sticky section index, the question visible and the NCERT answer folded until tapped, a "Show all answers" switch, and a "One at a time" view. No more 14,688 px scroll with a tag row on every card. |
| LK5 | Study is right; add motion, for example on Got it | Study's player is kept exactly (front, Show answer, Missed / Got it / Easy, 20-card rounds on the web) and becomes the Key card turn inside every session. Got it now sends the card up into a "kept" pile with its next date stamped ("Back in 3 days"); section 5 has values. |
| LK6 | Print sheet: keep it, watermark it all over | The print sheet stays Pro, reachable from the chapter page, the session end and a Library selection, with the lowercase mockmob mark tiled diagonally on every page and "Printed for Aarav" plus the date on every page (section 3.9). |
| LK7 | Last look vs Read is unclear | Last look stops being a mode (B4). Its job lives in two places with self-explaining names: "Quick recap, 5 min" in the time chooser (the readout says "Only the 13 Must-know cards, answers showing, nothing scheduled") and the "Must-know only" filter in the Library, whose "One at a time" view keeps the swipe pager. |
| LK8 | Integrate better, tastefully, in the flow | Every door (Today, Start, result, Explore, Review, Learn's lanes) leads to the same chapter page and the same session; one player; one end screen; one set of names. |
| LK9 | Easy self-control, not only weakness-led | "Your way" is a full lane on the same screen, never under the fold of a recommendation. Weakness becomes one source of For-you moves and one sort option ("Marks lost") on the chapter list, not the organising idea. |
| LK10 | Subject, chapter, see what is lined up, pick a time, get a mix; plus a separate place to find and revise | Your way lane (subject, chapter) to the chapter page ("What's here", "Lined up for 10 minutes") to the time chooser to the mixed session. The Library is the separate place: search everything, filter, tick cards, "Revise these 8". |
| LK11 | No walls of text; next action clear, dynamic, with options | For you shows three moves of different kinds, each one line of evidence, a "How sure" word and its own length chips; the lead is volt, the other two are quiet. Every page has one volt key and two or three named options beside it. Copy is one idea per line; cards keep NCERT's words only where the card is the content. |
| LK12 | Cards are the core; bring them to Explore as a chapter feed | Learn's home is cards first. Explore gains "Chapter runs": a 10-minute vertical feed alternating Key cards and questions for one chapter, ending with a summary (section 3.8). |
| LK13 | Too many cards carry Must-know | Must-know is re-tiered to about one card in four (B5). The chip box is removed; a thin volt rule on the card's left edge and the word "Must-know" in the kind line mark it, so it reads as a rare signal (section 3.10). |
| LK14 | Think longer, ideate better | Section 4 composes sessions from real engines with real numbers and states what the server must add; section 6 lists risks; section 7 walks two students through their first 60 seconds. Mock-ups in real renders go to him before anything ships (Never again 1). |

---

## 2. Information architecture

### 2.1 Every place in Learn

| Place | Route (web) | App route | What it is |
|---|---|---|---|
| Learn home | `/learn` | `/practice?door=learn` | Two lanes: For you (three moves) and Your way (subject, chapter list, Library and Revise doors). |
| Chapter page | `/learn/c/<chapterKey>` (new); `/cards/<chapterKey>` redirects here, keeping `?mode=study` | `/learn/c/<chapterKey>`; `/cards/<key>` redirects | "What's here" (Key cards, lesson, questions), "Lined up", the time chooser, Start, options. |
| Time chooser | inline on the chapter page; a sheet from For-you cards, the Start sheet and Today | same | Quick recap 5 min, 5, 10, 20 minutes, Your own. Live readout of the mix. |
| Session | `/learn/s/<sessionId>` (full screen, dock hidden) | `/learn/s/<id>` (pushed over the shell) | Mixed Key cards, questions, and in 20-minute sessions a lesson. One progress line. |
| Session end | same route, end state | same | What moved, the lines you needed, three next moves, print (Pro). |
| Study (cards only) | `/learn/c/<key>?mode=study` | same | Today's Study mode, unchanged in structure: 20-card rounds on the web. Reached from the chapter page option "Study the cards only". |
| Library | `/learn/library` with `?subject=&chapter=&q=&filter=` | `/learn/library` | Find and revise: search every card, lesson and chapter; filters; card list grouped by NCERT section; One at a time view; select and revise. Home of the old Read. |
| Lesson | `/learn/<unitId>` and `/study/<runId>` (kept) | kept | The 21 lessons; also played as a turn inside a 20-minute session. |
| Revise | `/review/revise` (kept) | kept | The daily due queue across everything. Unchanged; reached from Learn's Revise door and Today. |
| Print sheet | print view of the chapter page or a Library selection | system share sheet with a watermarked PDF | Pro. Watermarked on every page. |
| Explore chapter run | `/explore/run/<chapterKey>` | `/practice/stream/run/<chapterKey>` | A 10-minute vertical feed of one chapter's Key cards and questions. Nothing is scheduled unless the student taps Keep. |

Old routes kept as redirects (no route removed): `/cards` to `/learn?lane=yours`, `/cards?subject=x` to `/learn?lane=yours&subject=x`, `/cards/<key>?mode=last` to `/learn/library?chapter=<key>&filter=mustknow&view=one`, `/learn/summary?subject=&chapter=` stays (the lesson summary), `/learn?recall=due` stays.

### 2.2 How they connect

```
                    Today tile "Learn"  ─┐
            Start sheet "Study a chapter"┤
  Result "10 minutes on this chapter"    ┤
  Review chapter "Key cards for ..."     ┤
                                         ▼
 Practice tab "Learn" ──► LEARN HOME ──────────────► CHAPTER PAGE ──► SESSION ──► SESSION END
                           │  For you lane:            │  What's here     │            │ next moves loop
                           │  3 moves, length chips ───┼──────────────────┘            │ back to a session,
                           │  (a move can start a      │  Lined up + time              │ the chapter page,
                           │   session directly)       │  Start (volt)                 │ Learn home, or print
                           │                           │  options:                     │
                           │  Your way lane:           │   Study the cards only ──► STUDY (20-card rounds)
                           │  subject, chapter list ───┘   Questions only ──► Quick practice setup (kept)
                           │  Library door ──────────► LIBRARY ◄── Open in Library   Read the lesson ──► LESSON
                           │  Revise door ───────────► REVISE (kept)
                           │
 Explore "Chapter runs" ──────────────────────────────► EXPLORE RUN (10 min) ──► run end ──► chapter page
```

Rules: every nested page has a clear Back button with a word ("Learn", "Admission of a Partner"), not only an icon (D43). The Practice tab row is drawn on every Learn route on the phone web (R9 problem 2), so a student on a chapter page can move sideways.

### 2.3 Website navigation

**1440 sidebar** (B1 holds; only the Practice group's order changes and Learn gains a second word):

```
┌──────────────────────────────┐
│ mockmob.                     │
│ [ ▶ Start a session        ] │
│                              │
│ ▣ Today                      │
│ ◷ Practice                   │
│     Learn, Key cards   6 due │   <- moved from third to first under Practice; second word like
│     Your papers        8 due │      "Colleges, DU cutoffs"; badge = Key cards due today
│     Explore                  │
│     Saved                    │
│ ◎ Mob                        │
│ ◯ You                        │
│     Progress ...             │
└──────────────────────────────┘
```

The Learn row is lit on `/learn/*`, `/cards/*` and `/study/*`, and the top bar title follows the page ("Admission of a Partner", "Library"), not "Learn" over a "Key cards" heading (R9 problem 3).

**390 phone web**: dock unchanged (Today, Practice, Start, Mob, You). Practice's tab row becomes `Practice | Learn | Your papers | Explore | Saved`, so Learn is visible without a sideways swipe at 390 (Practice about 84 px, Learn about 70 px, Your papers about 130 px with its count; Explore peeks). The row is drawn on every Learn route. Practice remembers the last tab for the day, so a returning student who studied yesterday lands on Learn with one tap on the dock.

### 2.4 App navigation

- Dock unchanged (Today, Practice, Start, Mob, You).
- Practice door switch order becomes `Practise | Learn | Your papers` (B1 allows the door order). The door remembers the last choice for the day.
- **Start sheet** (the loved sheet, N11; same row style, nothing else moved): one new row "Study a chapter", under "By chapter":

```
  ┌───────────────────────────────────────────────┐
  │ (cards art)  Study a chapter              >   │
  │              Key cards and questions,          │
  │              5 to 20 minutes. Free taste       │
  └───────────────────────────────────────────────┘
```
Tapping it slides the sheet to a second step inside the same sheet: "Your chapters" (the last three chapters studied, then "All chapters" with search), a time segment (5 / 10 / 20 / Your own), and the volt key "Start 10 minutes". On the web the sheet behaves the same.

- **Today**: a "Learn" tile joins the Repairs and Revise tiles (web `TodayQueue`, app `today_body`), showing For you's lead move only:

```
  ┌───────────────────────────────────────────┐
  │ Learn                                      │
  │ Admission of a Partner                     │
  │ 6 Key cards due, 3 open mistakes.          │
  │ [ Start 10 minutes ]          Other moves  │
  └───────────────────────────────────────────┘
```
"Other moves" opens Learn on the For you lane. Today's lead card logic is not rebuilt: the Learn move joins its alternatives pool ("Something else") as one more move kind, so Today's swap-the-lead mechanism can make it the lead.

- **Result screen**: under "The line you needed", two quiet links: "Open Admission of a Partner" (chapter page) and "10 minutes on this chapter" (opens the time chooser sheet with that chapter set).

### 2.5 Taps from opening the site to studying a chapter's cards

Counted to the first Key card on screen. "Before" figures from R1 and R9.

| Surface | Student | Path | Taps now | Taps before |
|---|---|---|---|---|
| Web 390 | New | Practice (1), Learn tab (2), For you lead "Start 10 minutes" (3) | 3 | 5 (to Read), 6 for Study |
| Web 390 | New, own chapter | Practice (1), Learn (2), chapter row in Your way (3), "Start 10 minutes" (4) | 4 | 6 |
| Web 390 | Returning | Today tile "Start 10 minutes" (1) | 1 | 4-5 |
| Web 390 | Returning, own chapter | Practice (1, opens on Learn), chapter row (2), Start (3) | 3 | 5 |
| Web 1440 | New | sidebar "Learn, Key cards" (1), lead Start (2) | 2 | 3 (to Read), 4 for Study |
| Web 1440 | New, own chapter | Learn (1), chapter row (2), Start (3) | 3 | 4 |
| Web 1440 | Returning | Today tile Start (1) | 1 | 3-4 |
| App | New | Practice (1), Learn door (2), lead Start (3) | 3 | 5-6 |
| App | Returning | Today tile Start (1); or Start key (1), "Study a chapter" with the last chapter preselected (2), Start (3) | 1 or 3 | 5 |

### 2.6 One navigation change that needs his approval (separate option, not part of the base concept)

**N1: on the desktop website only, Learn becomes its own sidebar place.** The dock and the app bar do not change (B1). The rail gains one bold row and loses nothing:

```
 Base concept (no approval needed)       N1 (needs his yes)
 ◷ Practice                              ◷ Practice
     Learn, Key cards   6 due                Your papers        8 due
     Your papers        8 due                Explore
     Explore                                 Saved
     Saved                               ✦ Learn                6 due
 ◎ Mob                                       Library
                                         ◎ Mob
```
For: at 1440 the most-used study place gets the same weight as Practice and the Library gets its own row. Against: the desktop rail no longer mirrors the phone's five places exactly (D114), and the rail grows by one 44 px row (it already compacts at about 900 px windows, WEB-NAV-1019). Recommendation: show it to him as a render beside the base; build the base either way.

---

## 3. Screens

Conventions in the wireframes: `[ Start 10 minutes ]` in caps-free brackets is the one volt key; `( 10 min )` is a chip; `>` is a row chevron; `(obj)` is the lamp-lit subject object; `▍` is the thin volt Must-know rule. Glass appears only on the top bar, the dock, the sticky lane switch and sheets. Night and Day use the same layout; Night stays the subtle charcoal (Never again 4).

### 3.1 Learn home

**Hierarchy**: lane headings are equal in type size ("For you", "Your way"); For you comes first because it holds the page's one volt key; Your way starts inside the first screen at 1440 and is one tap away on a phone (lane switch). The lead move is the one leading action; the two alternates and the whole Your way lane are the options beside it.

**1440, returning Pro student (Commerce: Accountancy, Business Studies, Economics, English)**

```
┌sidebar┐┌───────────────────────────────────────────────────────────────────────────────────────────────────┐
│       ││ Learn                                                              Your plan   Print sheets (Pro) │
│       ││ Key cards, lessons and questions, chapter by chapter.                                              │
│       ││                                                                                                     │
│       ││ For you                                     Three next moves from your schedule and your answers.  │
│       ││ ┌──────────────────────────────────────────┐ ┌───────────────────────────┐ ┌───────────────────────────┐
│       ││ │ (obj) Accountancy, Part 1 Ch 2           │ │ (obj) Business Studies    │ │ (obj) Accountancy         │
│       ││ │ Admission of a Partner                   │ │ Planning                  │ │ Accounting Ratios         │
│       ││ │ 6 Key cards are due and 3 of your open   │ │ Pick up where you stopped:│ │ Quick recap of the 40     │
│       ││ │ mistakes are in this chapter.            │ │ cards 21 to 51 are new.   │ │ Must-know cards. Last     │
│       ││ │ How sure: Sure                           │ │ How sure: Sure            │ │ seen 9 days ago.          │
│       ││ │ ( 5 )( 10 min )( 20 )                    │ │ ( 5 )( 10 min )( 20 )     │ │ How sure: Likely          │
│       ││ │ 6 due cards, 6 new, 2 mistakes back,     │ │ 12 new cards, 6 questions │ │ ( Quick recap, 5 min )    │
│       ││ │ 4 new questions                          │ │                           │ │ 18 of 40, oldest first    │
│       ││ │ [ Start 10 minutes                     ] │ │ Start 10 minutes        > │ │ Start the recap         > │
│       ││ └──────────────────────────────────────────┘ └───────────────────────────┘ └───────────────────────────┘
│       ││                                                                                                     │
│       ││ Your way                                                                                            │
│       ││ ( (obj) Accountancy )( (obj) Business Studies )( (obj) Economics )( (obj) English )                 │
│       ││ Your part: Analysis of Financial Statements.  Change                                                │
│       ││ ┌ Find a chapter ─────────────────────────┐  Sort: Book order  Marks lost        ┌ Library ─────────┐
│       ││ └──────────────────────────────────────────┘                                     │ Find any card,   │
│       ││ Accounting for Partnership                                                       │ revise the ones  │
│       ││  Accounting for Partnership: Basic Concepts   46 Key cards   11 qs  Getting there >│ you choose.      │
│       ││  Accountancy Part 1, Ch 1                                                        │ 868 cards      > │
│       ││ Reconstitution of a Partnership firm                                             ├ Revise ──────────┤
│       ││  Change in Profit Sharing Ratio      8 Key cards   1 lesson  136 qs  Needs work > │ 24 due today,    │
│       ││  Goodwill: Nature and Valuation     39 Key cards             11 qs  Holding    > │ about 10 minutes │
│       ││  Admission of a Partner             53 Key cards   1 lesson  159 qs  6 due     > │ Revise now     > │
│       ││  Retirement/Death of a Partner      65 Key cards             16 qs  Getting... > ├──────────────────┤
│       ││  ...                                                                             │ 4 of 21 lessons  │
│       ││ Chapters follow the CUET UG 2026 syllabus.                                       │ read. 212 cards  │
│       ││                                                                                  │ in Revise.       │
│       ││                                                                                  │ See your marks > │
└───────┘└──────────────────────────────────────────────────────────────────────────────────┴──────────────────┘
```

Notes on the 1440 layout:
- For you is a row of three: the lead is 1.4 times as wide and carries the volt key; the other two have the same anatomy but a quiet text-and-chevron key. Cards are separate surfaces in one row, never nested.
- Each move holds exactly four lines of meaning: where (subject object, subject, chapter), why (one evidence sentence), how sure (one word), how long (chips and the readout of what plays). The readout changes live when a chip is tapped.
- Your way's chapter rows show what each chapter holds ("53 Key cards", "1 lesson", "159 qs" are the questions linked to its cards when the full bank count is not loaded) and one state word. Questions counts come from `available.questions` once the composer read carries it; until then the linked count is shown with the label "linked questions" on hover and in the screen-reader name.
- "Sort: Marks lost" re-orders the list by marks lost and shows the red "−35" on rows; in book order the minus figure does not show (folds "Where you lose marks").
- Right column: Library and Revise doors, then the record line (folds the old aside). "Your plan" in the header opens the Study preferences sheet (subjects to plan for, usual time, Pro weekly plan); nothing there is dropped.

**390, same student**

```
┌──────────────────────────────────────┐
│ mockmob.                    (68) (P) │  glass top bar
├──────────────────────────────────────┤
│ Practice  [Learn]  Your papers  Expl │  Practice tab row, Learn second
├──────────────────────────────────────┤
│ Learn                                │
│ ┌──────────────────────────────────┐ │
│ │ [ For you ]      Your way        │ │  glass lane switch, sticky under the top bar;
│ └──────────────────────────────────┘ │  one indicator slides; tap scrolls to the lane
│                                      │
│ For you                              │
│ Three next moves from your schedule  │
│ and your answers.                    │
│ ┌──────────────────────────────────┐ │
│ │ (obj) Accountancy, Part 1 Ch 2   │ │
│ │ Admission of a Partner           │ │
│ │ 6 Key cards are due and 3 open   │ │
│ │ mistakes are in this chapter.    │ │
│ │ How sure: Sure                   │ │
│ │ (  5  )( 10 min )(  20  )        │ │
│ │ 6 due cards, 6 new, 2 mistakes   │ │
│ │ back, 4 new questions            │ │
│ │ [ Start 10 minutes             ] │ │
│ └──────────────────────────────────┘ │
│ (obj) Planning                     > │
│ Business Studies. Cards 21 to 51     │
│ are new. 10 min                      │
│ ──────────────────────────────────── │
│ (obj) Accounting Ratios            > │
│ Quick recap of 40 Must-know cards,   │
│ last seen 9 days ago. 5 min          │
│                                      │
│ Your way                             │
│ ┌────────────────┐┌────────────────┐ │
│ │ Library        ││ Revise         │ │  two half-width doors, never below the list
│ │ Find any card  ││ 24 due, 10 min │ │
│ └────────────────┘└────────────────┘ │
│ ((obj) Accountancy)((obj) Business S │  subject chips, sideways, peek + one-time nudge
│ Your part: Analysis of Financial     │
│ Statements.  Change                  │
│ ┌ Find a chapter ──────────────────┐ │
│ └──────────────────────────────────┘ │
│ Accounting for Partnership           │
│ Accounting for Partnership: Basic  > │
│ Concepts                             │
│ 46 Key cards, 11 questions           │
│ ◐ Getting there                      │
│ ──────────────────────────────────── │
│ Admission of a Partner             > │
│ 53 Key cards, 1 lesson, 159 qs       │
│ ◔ Needs work            6 due        │
│ ...                                  │
├──────────────────────────────────────┤
│ Today  Practice  (Start)  Mob  You   │  dock, unchanged
└──────────────────────────────────────┘
```

At 390 the alternates are compact rows with their default length shown; tapping an alternate's row opens the time chooser sheet for that move (one tap to Start from there), so the lead stays the only volt key in the viewport (W-075).

**App**: the same content inside Practice's Learn door (Practice owns the title and the pull). Differences: the lane switch is an `MmSegmented` pinned under the door switch; the Library and Revise doors are two `MmSurface.plain` tiles; haptic selection tick on lane change and chip change; "On this phone" (offline packs) moves to the Library (section 3.7).

**States**

| State | What shows |
|---|---|
| New student, no history | For you heading line reads "Three ways to start. You have not studied here yet, so these are starting points." Moves (from their own subjects in order): "Accounting for Partnership: Basic Concepts. Chapter 1 of Accountancy, the place most students begin. How sure: A first guess. 10 min"; "Business Studies: Nature and Significance of Management. A 5-minute taste. How sure: A first guess. 5 min"; "Find your level: 6 Accountancy questions, 6 min. How sure: A first guess". First-visit coach line under the lane switch, once: "For you: we pick. Your way: you pick." with a small Mobi pointing at the switch; it leaves after the first tap anywhere. Your way shows the full chapter list with "Not started" states. Never fewer than three moves (G12). |
| Returning | As drawn. Moves recompute after every session and every Revise run. |
| Free | Same lanes and moves. Readouts are honest about the taste: "5 Key cards (the Free taste) and 8 questions". One quiet Pro line at the foot of For you, dismissable: "Pro opens every card in every chapter and keeps them on a schedule. See Pro". No Pro ask before a real limit (D181). |
| Pro | As drawn; no Pro line. |
| For you loading | Three skeleton surfaces at final size (no layout jump when the key arrives); Your way renders as soon as its own read lands. |
| For you failed | Lane body: "Your next moves did not load. Your way still works." and "Try again". Your way is unaffected (separate read). |
| Your way loading | Subject chips and six row skeletons. |
| Your way failed | "Chapters did not load. Check your connection and try again. Your cards and their schedule are safe." with "Try again". |
| A subject with no Key cards (for example Mathematics) | Chapters still list, each "Questions only. No Key cards yet for Mathematics." For you never proposes it for cards. |
| Key cards switched off | Lanes show lessons and questions only; the Library door reads "Key cards open here soon"; no empty pages (R2's rule kept). |
| Offline (app) | Strip "Offline. Showing what this phone kept. As of 9:40 pm." For you keeps only moves whose decks are kept on the phone, labelled "Cards only while offline". Questions-carrying moves show "Needs a connection". |

### 3.2 Choosing a subject and a chapter

This is the Your way lane plus the "Find a chapter" field; there is no separate page (one chapter list, B2).

- **Subject chips**: the student's own CUET subjects in their own order (not a fixed alphabetical four), each with its object. Science students see Biology and Political Science alongside lessons-less subjects. The selected chip is remembered (account, then device).
- **Your part** (LK2): one line under the chips for Accountancy, Mathematics and Computer Science: "Your part: Analysis of Financial Statements. Change". Before any choice: "Both parts show until you choose yours. Choose". "Change" opens a small sheet:

```
 ┌──────────────────────────────────────┐
 │ Your part in Accountancy             │
 │ ( ● Analysis of Financial Statements)│
 │ (   Computerised Accounting         )│
 │ Only that part's chapters show here  │
 │ and in your practice. You can change │
 │ it at any time.                      │
 └──────────────────────────────────────┘
```
On tap: the dot moves at once and stays (held locally until the server body agrees), the sheet closes after 200 ms, the line under the chips reads "Saving your part" then the part name; the list below removes or adds the part's unit with a 240 ms height change, rows keyed by chapter key, no re-entrance. Failure: the dot returns with "Your part was not saved. Try again." under the line, the list unchanged.

- **Find a chapter**: filters the list as the student types (chapter titles, NCERT titles and aliases); "No chapter matches 'xyz'. Search the Library for cards instead" links to the Library with the query.
- **Rows**: grouped by CUET unit (heading only when a unit has more than one chapter). Row anatomy at 390: title (16, 650), what it holds on one line, state word and glyph with due count at the right. Whole row is one pressable (press scale 0.985, selection haptic on the app; rows look like buttons, F5).

**States**: new student (every row "Not started", no due counts); a chapter with no cards ("Questions only"); a chapter with neither cards nor questions ready (row reads "Being prepared", not pressable, dimmed); Free (no "5 of 46 open" repeated on every row; the taste is stated once on the chapter page); loading, failed and offline as in 3.1.

### 3.3 The chapter page: what's lined up

**Hierarchy**: chapter title; "What's here" (three numbers, value before label, R9); "Lined up" with the time chooser and a readout; the volt Start key naming the session (T001); three options beside it; then a short look at the first cards so the page is not only numbers.

**1440, Admission of a Partner, returning Pro**

```
┌sidebar┐┌──────────────────────────────────────────────────────────────────────────────────────────┐
│       ││ < Learn                                                          Print sheet   ...         │
│       ││ Reconstitution of a Partnership firm                                                       │
│       ││ Admission of a Partner                                                       (obj, large)  │
│       ││ Accountancy Part 1, Ch 2                                                                   │
│       ││ ◔ Needs work. 7 of 12 right on your latest try at each question. Cards: 14 of 20 holding.  │
│       ││                                                                                             │
│       ││ What's here                                                                                 │
│       ││ ┌──────────────────────────┬──────────────────────────┬──────────────────────────┐          │
│       ││ │ 53                       │ 1                        │ 159                      │          │
│       ││ │ Key cards                │ lesson                   │ questions on its cards   │          │
│       ││ │ 13 Must-know, 6 due,     │ Revaluation of assets    │ You answered 12. 3 open  │          │
│       ││ │ 27 you have not seen     │ and liabilities, 7 min.  │ mistakes.                │          │
│       ││ │ Add the 13 Must-know     │ Not read yet.            │                          │          │
│       ││ │ to Revise                │                          │                          │          │
│       ││ └──────────────────────────┴──────────────────────────┴──────────────────────────┘          │
│       ││                                                                                             │
│       ││ Lined up                                                                                    │
│       ││ ( Quick recap, 5 min )(  5 min  )[ 10 min ](  20 min  )(  Your own  )                       │
│       ││                                                                                             │
│       ││  6  Key cards due, Must-know first        about 2 min                                      │
│       ││  6  new Key cards, in book order          about 2 min                                      │
│       ││  2  of your open mistakes, back           about 2 min                                      │
│       ││  4  new questions, 2 of them on today's new cards     about 4 min                          │
│       ││                                                                                             │
│       ││ [ Start 10 minutes: 12 Key cards and 6 questions                                         ] │
│       ││ Cards you rate join Revise. Missed cards come back once at the end.                        │
│       ││                                                                                             │
│       ││ Or   Study the cards only      Questions only      Read the lesson, 7 min      Open in Library │
│       ││                                                                                             │
│       ││ First cards in book order                                                     See all 53 > │
│       ││ ▍Definition  Must-know   What is sacrificing ratio?                                         │
│       ││  Term                    The new partner brings in his share of ______ in cash.             │
│       ││  Key line                On admission, the old firm comes to an end and a new firm ...     │
└───────┘└──────────────────────────────────────────────────────────────────────────────────────────────┘
```

**390, same**

```
┌──────────────────────────────────────┐
│ Practice  [Learn]  Your papers  Expl │
├──────────────────────────────────────┤
│ [ < Learn ]                 Print ...│  Back is a pill with a word (D43)
│ Admission of a Partner        (obj)  │
│ Accountancy Part 1, Ch 2             │
│ ◔ Needs work                         │
│                                      │
│ What's here                          │
│ ┌────────────┬───────────┬─────────┐ │
│ │ 53         │ 1         │ 159     │ │
│ │ Key cards  │ lesson    │ questions│ │
│ │ 6 due      │ 7 min     │ 3 open  │ │
│ │            │ not read  │ mistakes│ │
│ └────────────┴───────────┴─────────┘ │
│ 13 Must-know. Add them to Revise     │
│                                      │
│ Lined up                             │
│ ┌──────────────────────────────────┐ │
│ │Recap│ 5 min│[10 min]│20 min│ Own │ │  one sunken track, one sliding thumb
│ └──────────────────────────────────┘ │
│  6  Key cards due                    │
│  6  new Key cards                    │
│  2  open mistakes, back              │
│  4  new questions                    │
│ [ Start 10 minutes                 ] │
│ 12 Key cards and 6 questions. Cards  │
│ you rate join Revise.                │
│                                      │
│ Study the cards only               > │
│ Questions only                     > │
│ Read the lesson, 7 min             > │
│ Open in Library                    > │
├──────────────────────────────────────┤
│ Today  Practice  (Start)  Mob  You   │
└──────────────────────────────────────┘
```

**App**: same order. "Print sheet" becomes "Share sheet" in the `...` menu, which shares a watermarked PDF (section 3.9). The Start key sits above the gesture bar with a real gap (D40).

**What each option does**
- "Study the cards only": today's Study mode, unchanged (front, Show answer, Missed / Got it / Easy; rounds of 20 on the web, `Study the next 20` at a round end) plus the new Got it motion.
- "Questions only": opens Quick practice setup for this chapter (count 5, 10, 15, 20), unchanged; price shown there as today.
- "Read the lesson, 7 min": the lesson overview. Shown only when the chapter has a lesson; otherwise this option is absent and nothing says "No lesson yet".
- "Open in Library": the Library filtered to this chapter (section 3.7).
- `...` menu: Print sheet (Pro; Free sees it with a small lock and "Pro" and gets the honest sheet), Report a problem with this chapter, Your part (when relevant).

**States**

| State | What shows |
|---|---|
| New student, Accounting for Partnership: Basic Concepts | What's here: "46 Key cards, 12 Must-know, all new to you"; no lesson column (the row collapses to two columns: Key cards, questions); "11 questions on its cards". Lined up at 10 min: "12 new Key cards, in book order" and "6 questions". If fewer than 6 chapter questions are unseen: "4 new questions. That is every question on this chapter's cards for now, so the rest is Key cards." |
| Free, Admission of a Partner | What's here: "53 Key cards. 5 open on Free". Lined up at 10 min: "5 Key cards, the Free taste" and "8 questions (8 of your 10 free today)". Line under the key: "Free fills 10 minutes today with more questions. Pro opens all 53 cards." Study the cards only plays the 5 open cards. |
| Free, out of the day's allowance | Readout: "Today's free card reviews and questions are used. Mistakes back are still free: 2 now, about 2 min." Key becomes "Start 2 minutes". A second line: "Your free reviews come back tomorrow. See Pro". |
| Pro | As drawn. |
| Everything done today in this chapter | Lined up: "Nothing is due here. 10 minutes would be 12 new Key cards and 6 new questions." The key still starts. |
| Chapter with every card seen and nothing due | "Every card here is on its schedule. Next due Thursday 5 November. 10 minutes now: 6 questions and 12 cards you saw longest ago." |
| Loading | Title renders from the list read (known), numbers and readout as skeletons at final size; Start key disabled with "Lining up". |
| Error | "This chapter did not load. Check your connection and try again. Nothing you added is lost." with "Try again" and "Back to Learn". |
| Not in the syllabus (old link) | "This chapter is not in the CUET syllabus now. Your other chapters are in Learn." and "See all chapters". |
| Offline (app) | Questions column reads "Needs a connection". Lined up offers cards only: "Offline: 12 Key cards, about 3 min. Questions come back when you are online." Ratings go to the outbox ("Saved on this phone"). |

### 3.4 Choosing the time

One control everywhere (chapter page, For-you cards, the Start sheet step, Today's "Other moves", Explore): `Quick recap, 5 min | 5 min | 10 min | 20 min | Your own`. One sunken track, one thumb that slides (N5). The readout below changes live; it never shows a number the composer did not compute (R18, AS9).

| Choice | What it means | Readout example (Admission of a Partner, Pro) |
|---|---|---|
| Quick recap, 5 min | Must-know cards only, answers showing, nothing scheduled, no allowance used (the old Last look) | "Only the 13 Must-know cards, answers showing. Nothing is scheduled. About 4 minutes." |
| 5 min | Mix | "6 Key cards and 3 questions" |
| 10 min (default) | Mix | "12 Key cards and 6 questions" |
| 20 min | Mix; includes an unread lesson first when the chapter has one | "Revaluation of assets and liabilities (7 min), then 18 Key cards and 7 questions" |
| Your own | A sheet with a stepper: 15, 25, 30, 45, 60, 90 minutes and a free number field (5 to 180). Never capped below what the chapter holds (H1). | "45 minutes: the lesson, all 53 Key cards and 22 questions. That is everything here; after that it is questions from your other Accountancy chapters." |

**"Your own" sheet (390)**

```
 ┌──────────────────────────────────────┐
 │ How long today?                      │
 │      ( − )      45 min      ( + )    │  steps of 5; long-press repeats
 │ ( 15 )( 25 )( 30 )( 45 )( 60 )( 90 ) │
 │ The lesson, all 53 Key cards and 22  │
 │ questions. That is everything in     │
 │ this chapter.                        │
 │ [ Start 45 minutes                 ] │
 └──────────────────────────────────────┘
```

The chooser remembers the last length per student ("Last time you chose 10 minutes" appears as the default's caption once, T001 and R13). The default is 10 min for a new student.

States: loading (readout skeleton, thumb usable, Start disabled with "Lining up"); the composer failed ("We could not line this up. Try again", the options stay); Free (each readout line names the allowance it uses); offline (cards only, as 3.3).

### 3.5 The mixed session player

Full screen, dock hidden (like Revise). Top: a hairline progress made of pips, one per item, cards as short pips and questions as long pips, so the mix is visible without a legend; "7 of 18" at left; "About 6 min left" at right; a Back pill "End" that asks nothing and goes to the end screen with what was done (no confirm sheet, D53). The "kept" counter (cards rated Got it or Easy) sits top right as a small stack mark with a number.

**Key card turn, 390** (Study's player, unchanged structure)

```
┌──────────────────────────────────────┐
│ [ End ]   ▮▮▮▮▮▮▬▮▮▬▮▮▬▮▮▬▮▮      ▤ 4 │  pips: ▮ card, ▬ question; ▤ 4 = kept pile
│ 7 of 18                 About 6 min  │
│                                      │
│ ┌──────────────────────────────────┐ │
│ │▍Definition  Must-know        ... │ │  Must-know rule only on ~1 card in 4
│ │                                  │ │
│ │ What is sacrificing ratio?       │ │  display face, 22-23
│ │ - - - - - - - - - - - - - - - - -│ │
│ │                                  │ │
│ │                                  │ │
│ └──────────────────────────────────┘ │
│                                      │
│ [ Show answer                      ] │
│ Say it in your head first.           │  first card of a student's first session only
└──────────────────────────────────────┘
```
Revealed:
```
│ ┌──────────────────────────────────┐ │
│ │▍Definition  Must-know        ... │ │
│ │ What is sacrificing ratio?       │ │
│ │ - - - - - - - - - - - - - - - - -│ │
│ │ ┃ The ratio in which the old     │ │  NCERT's words, Literata
│ │ ┃ partners agree to sacrifice    │ │
│ │ ┃ their share of profit in favour│ │
│ │ ┃ of the incoming partner.       │ │
│ │ Accountancy Part 1, Ch 2         │ │
│ │ In short  What the old partners  │ │
│ │ give up for the new one.         │ │
│ └──────────────────────────────────┘ │
│ ( Missed )[ Got it ]( Easy )         │
│ Missed: back tomorrow. Got it and    │
│ Easy space it out.                   │
```
Keys: Space or Enter reveals; 1, 2, 3 rate (web hint on desktop as today). Rating posts `mode: study` (or `last_look` in Quick recap, where the rating row is replaced by `Next`, since answers already show).

**Question turn, 390**

```
│ 8 of 18                 About 5 min  │
│ ┌──────────────────────────────────┐ │
│ │ Question  On the card you just saw│ │  "On the card you just saw" only when linked
│ │ At the time of admission of a    │ │
│ │ new partner, the General Reserve │ │
│ │ is credited to:                  │ │
│ └──────────────────────────────────┘ │
│ ( A  Old partners in their old ratio)│
│ ( B  All partners in the new ratio  )│
│ ( C  The new partner only           )│
│ ( D  Old partners in the sacrificing)│
│ (    ratio                          )│
```
Pick is final and checked on the server (no key in the payload).

**Wrong answer, showing the line you needed**

```
│ ( A  Old partners in their old ratio)│  inked green, tick
│ ( B  All partners in the new ratio  )│  red outline, cross: your pick
│ The answer is A.                     │
│ Reserves built before the admission  │  the bank's explanation, max 3 lines,
│ belong to the old partners.     More │  "More" expands the rest
│ ┌──────────────────────────────────┐ │
│ │ The line you needed              │ │  slides up from under the explanation
│ │ ┃ Accumulated profits, losses and│ │
│ │ ┃ reserves are transferred to the│ │
│ │ ┃ old partners' capital accounts │ │
│ │ ┃ in their old ratio.            │ │
│ │ Accountancy Part 1, Ch 2         │ │
│ │ Linked to this question. Back in │ │
│ │ Revise tomorrow.                 │ │
│ └──────────────────────────────────┘ │
│ [ Next                             ] │
```
The card is scheduled into Revise as Missed automatically (it is the card the student just failed to use); the line under it says so. When no link exists and the text matcher finds one: "Matched by its words." When neither: the block does not show (no fake line).

**1440**: the stage is a centred 640 px column; at its right a quiet 260 px panel: chapter name, "Lined up" list with ticks as items finish, "Kept 4", "Back soon 1". At its left nothing. Keyboard: A to D or 1 to 4 for options, Enter for Next.

**Lesson turn (20-minute sessions)**: the lesson player (StudyRun) plays in place with its own step pips nested under the session pip, then its lesson cards ("Lock it in") as card turns. The session's time readout counts the lesson's minutes.

**States**

| State | What shows |
|---|---|
| First session ever | Three coach lines, each once in the student's life: on the first card "Say it in your head first."; on the first reveal "Missed: back tomorrow. Got it and Easy space it out."; on the first question "Pick one. If you miss it, you see the NCERT line you needed." |
| Free limit reached mid-session | Never mid-session by surprise: the composer only lines up what fits. If the allowance changed in another tab, the turn reads "Today's free card reviews are used. The rest of this session is questions." and the session continues. |
| Rating not saved | Under the keys: "That rating was not saved. Try again." The card stays. |
| Answer not checked | "We could not check that answer. Try again." Choice stays selected. |
| Offline (app) | Card turns continue to the outbox; question turns are skipped with "Saved for when you are online" and listed at the end. |
| Ran out of time early (student fast) | Session ends at the last item; it never pads. |
| End early | "End" goes straight to the session end with what was done. |

### 3.6 The session end, with next options

**390**

```
┌──────────────────────────────────────┐
│                         (Mobi, glad) │  Mobi reacts to the tally, one per screen
│ 10 minutes on Admission of a Partner │
│                                      │
│  9          3          4/6           │  count up, 600 ms
│  kept       back soon  questions     │
│  Got it 7, Easy 2. Missed 3, back    │
│  tomorrow.                           │
│                                      │
│ Lines you needed                     │
│ ┃ Accumulated profits, losses and  > │
│ ┃ reserves are transferred to ...    │
│                                      │
│ Next                                 │
│ ┌──────────────────────────────────┐ │
│ │ Fix the 3 missed cards now       │ │
│ │ They are fresh. About 1 min.     │ │
│ │ [ Start 1 minute               ] │ │
│ └──────────────────────────────────┘ │
│ Another 10 minutes here            > │
│ 21 new Key cards and 4 questions     │
│ left in this chapter.                │
│ ──────────────────────────────────── │
│ Next chapter in the book           > │
│ Retirement/Death of a Partner,       │
│ 65 Key cards.                        │
│ ──────────────────────────────────── │
│ Print this chapter's sheet  (Pro)    │
│ Back to Learn                        │
└──────────────────────────────────────┘
```

**1440**: two columns; left the tally and lines you needed, right "Next" with the same three moves stacked; the kept pile mark fans out once (480 ms) beside the tally.

**Next-move rules** (always three, of different kinds, each with its reason): 1. if anything was missed: "Fix the N missed cards now" (in-session relearn, only those cards, about 15 s each); else if the student answered fewer than half the questions right: "Try 5 more questions here"; else "Quick recap of this chapter's Must-know". 2. "Another 10 minutes here" when the chapter has unseen cards or questions; otherwise "Revise: 24 due across your subjects". 3. "Next chapter in the book" (book order within the unit), or for a chapter with an unread lesson "Read the lesson, 7 min". Plus "Test it in a full mock" appears in place of move 3 once the student has finished every chapter of a unit (folds the old "Test it in a full mock" row).

**States**: Free ("Free today: 2 card reviews and 2 questions left." and the Pro line once); a session ended early ("You did 7 of 18. The rest stays lined up for next time." and move 2 becomes "Finish this session, 11 left"); all right ("Every card kept and 6 of 6 right." Mobi cheers once, no confetti); offline (app) ("Saved on this phone. It is sent when you are back online.").

### 3.7 The Library: find and revise (new home of Read, Last look folded in)

The separate place of LK10. It answers "where is what" and "let me revise these exact cards".

**Hierarchy**: search first; filter chips; the chapter's cards grouped by NCERT section, each card one line until opened; selection bar appears when cards are ticked; the one volt key is "Revise these N" while a selection exists, otherwise there is no volt key on the page (it is a reference place).

**1440, Library filtered to Admission of a Partner**

```
┌sidebar┐┌───────────────────────────────────────────────────────────────────────────────────────────┐
│       ││ < Learn                                                                                     │
│       ││ Library                                                                                     │
│       ││ ┌ Search every card, lesson and chapter ─────────────────────────────────────────────────┐ │
│       ││ └─────────────────────────────────────────────────────────────────────────────────────────┘ │
│       ││ ( Accountancy v )( Admission of a Partner v )( Must-know only )( In Revise )( Missed lately )│
│       ││ ( All kinds v )                              View:  [ List ]  One at a time   Show answers ○│
│       ││                                                                                             │
│       ││ ┌ Sections ───────────┐  53 Key cards. 13 Must-know. 1 lesson.                              │
│       ││ │ 3.1 Admission of a  │                                                                     │
│       ││ │     partner      9  │  3.1 Admission of a partner                                         │
│       ││ │ 3.2 New profit      │  □ ▍Definition  Must-know  What is admission of a partner?        v │
│       ││ │     sharing ratio 8 │  □  Key line             On admission, the old firm comes to an … v │
│       ││ │ 3.3 Sacrificing     │  □  List                 Rights a new partner acquires          v │
│       ││ │     ratio        6  │                                                                     │
│       ││ │ 3.4 Goodwill     11 │  3.3 Sacrificing ratio                                              │
│       ││ │ 3.5 Revaluation  10 │  ■ ▍Definition  Must-know  What is sacrificing ratio?           ^ │
│       ││ │ 3.6 Capitals      9 │     ┃ The ratio in which the old partners agree to sacrifice their  │
│       ││ │                     │     ┃ share of profit in favour of the incoming partner.            │
│       ││ │ Lesson              │     Accountancy Part 1, Ch 2   In Revise, back Tuesday 3 Nov   ...  │
│       ││ │ Revaluation of      │  ■  Formula              Sacrificing ratio                      v │
│       ││ │ assets and          │  □  Entry                Goodwill brought in cash               v │
│       ││ │ liabilities, 7 min  │                                                                     │
│       ││ └─────────────────────┘                                                                     │
│       ││ ┌─────────────────────────────────────────────────────────────────────────────────────────┐ │
│       ││ │ 2 cards chosen        Clear     Add to Revise     Print these (Pro)   [ Revise these 2 ] │ │  glass bar
│       ││ └─────────────────────────────────────────────────────────────────────────────────────────┘ │
└───────┘└───────────────────────────────────────────────────────────────────────────────────────────┘
```

**390**

```
┌──────────────────────────────────────┐
│ [ < Learn ]                          │
│ Library                              │
│ ┌ Search every card and chapter ───┐ │
│ └──────────────────────────────────┘ │
│ (Admission of a Partner v)(Must-know │  chips scroll sideways with a peek
│ List | One at a time    Answers ○    │
│ 53 Key cards. 13 Must-know.          │
│ Jump to: 3.3 Sacrificing ratio     v │  sticky section jump, one line
│                                      │
│ 3.3 Sacrificing ratio                │
│ □ ▍Definition  Must-know           v │
│   What is sacrificing ratio?         │
│ □  Formula                         v │
│   Sacrificing ratio                  │
│ □  Entry                           v │
│   Goodwill brought in cash           │
│ ...                                  │
├──────────────────────────────────────┤
│ 2 chosen   Add to Revise  [Revise 2] │  glass selection bar above the dock
└──────────────────────────────────────┘
```

**What lives here**
- **Read, refined (LK4)**: the same card faces and NCERT text, but folded: question line visible, answer behind a tap (or all answers with "Show answers" on). Grouped by `source.section` (every card carries it, R5). Kind label once per card, the Must-know rule on about one in four, "In short" and the source under the opened answer, the `...` menu (Add this card to Revise, Report this card) on the opened card only. No tag row on closed cards.
- **Last look, folded (B4)**: the "Must-know only" chip plus the "One at a time" view is exactly the old Last look (Must-know, one card at a time, swipe or arrow keys, Previous and Next, answers showing, nothing scheduled). The "One at a time" view works with any filter, so a student can flip through "Missed lately" too. The old link `/cards/<key>?mode=last` lands here with both set.
- **Revise chosen cards (LK10)**: tick cards (or "Choose all 13" on a filter) and "Revise these N" starts a session of exactly those cards (cards only, no time chooser needed: "13 cards, about 4 min" shows on the bar). Across chapters works too (folds Pro's "mixed revision" of lesson cards, which also appear here under their lesson).
- **Search**: across every card's question, answer and NCERT words, lesson titles and chapter names in the student's subjects. Results grouped by chapter, with the matching words in bold. A chapter result opens the chapter page; a card result opens in place.
- **Filters**: subject, chapter, Must-know only, In Revise, Missed lately (rated Missed in the last 14 days), kind (Definition, Formula, Entry, List, and the rest).
- **On this phone (app)**: keep-for-offline switches per subject, moved here from the Learn door foot.

**States**: new student (no "In Revise" or "Missed lately" results: "Nothing here yet. Cards you study land in Revise and show here."); Free (the 5 open cards per chapter are whole; the rest show as one line "48 more cards in this chapter are part of Pro" in their sections' place, no per-card locks; search matches locked cards and shows them as "Part of Pro" with the question line only); Pro (all); no results ("No card matches 'goodwil'. Try fewer words, or a chapter name."); loading (list skeleton, filters usable); error ("The cards did not load. Check your connection and try again."); offline (app: kept decks only, "Showing chapters kept on this phone").

### 3.8 Explore chapter feed

Explore keeps everything it has (D21): the filters and the question list stay below. A new band sits at the top of Explore: "Chapter runs".

**Explore top band, 390**

```
│ One question. One useful step.      │  existing head
│ ┌──────────────────────────────────┐ │
│ │ Chapter runs                     │ │
│ │ 10 minutes on one chapter: Key   │ │
│ │ cards and questions, one at a    │ │
│ │ time. Nothing changes your       │ │
│ │ schedule unless you keep a card. │ │
│ │ (Admission of a Partner v)       │ │  defaults to For you's lead chapter
│ │ [ Start a 10-minute run        ] │ │
│ └──────────────────────────────────┘ │
│ Subject  Chapter  Difficulty         │  existing filters, unchanged
```

**The run, 390**: a vertical feed, one item per screen, snap scrolling (swipe up for the next, down to go back; buttons do the same, D90).

```
┌──────────────────────────────────────┐
│ [ End ]  Admission of a Partner      │
│ ▮▮▬▮▬▮▮▬▮▬▮▮▬     4 of 14  6 min left│
│                                      │
│ Key card                             │
│ What is sacrificing ratio?           │
│                                      │
│        Tap to see NCERT's line       │
│                                      │
│ ┌──────────┐            ┌──────────┐ │
│ │  Keep    │            │  Next  v │ │
│ └──────────┘            └──────────┘ │
│ Keep sends it to Revise.             │  first card of the first run only
└──────────────────────────────────────┘
```
Question items use Explore's own question card (one answer, instant reason), with "The line you needed" under a wrong answer when a link exists. Order: card, card, question, repeating; a question linked to a card shown in this run follows it.

**Run end**: "10 minutes on Admission of a Partner. You kept 3 cards and got 4 of 5 questions right." Next: "Do this chapter properly: 10 minutes in Learn" (to the chapter page, the volt key), "Another run" , "Another chapter".

**1440**: a centred 560 px feed column; right panel with the chapter, items left, and the cards kept.

**How it differs from a Learn session** (said once on the band and once on the end screen, never as a disclaimer): Explore runs show answers on a tap and change nothing unless the student taps Keep; Learn sessions rate every card and schedule it.

**States**: Free (the 5 open cards of the chapter, then questions only: "That was the Free taste of this chapter's cards. The rest of the run is questions."; questions in Explore stay free and unlimited); new student (chapter chooser defaults to Chapter 1 of their first subject); a chapter with no cards (the run is questions only and says so on the band); loading ("Lining up your run"); error ("The run did not load. Try again"); offline (app: "Runs need a connection. Your kept chapters are in Learn.").

### 3.9 The print sheet, watermarked

Pro. Entry points: chapter page header "Print sheet" (`...` on phones), session end, Library selection "Print these". Contents: the chapter's Must-know cards (after re-tier: Admission of a Partner prints 13), or the chosen cards. On the app, "Share sheet" makes the same page as a PDF and opens the system share sheet.

**A4 page**

```
┌──────────────────────────────────────────────────────────────┐
│  mockmob                         Admission of a Partner      │  header: wordmark left, chapter right
│                                  Accountancy Part 1, Ch 2    │
│ ╲ mockmob ╲      ╲ mockmob ╲      ╲ mockmob ╲      ╲ mockmob │  tiled wordmark, 30 degrees, 7% ink,
│   1. What is sacrificing ratio?                              │  on every page, behind the text
│      The ratio in which the old partners agree to sacrifice  │
│ mo   their share of profit in favour of the incoming      ╲  │
│      partner.                                  p. ref     mo │
│ ╲ mockmob ╲      ╲ mockmob ╲      ╲ mockmob ╲      ╲ mockmob │
│   2. ...                                                     │
│                                                              │
│ ──────────────────────────────────────────────────────────── │
│  Printed for Aarav on Saturday 31 October 2026.  mockmob.in   │  footer on every page
│  13 Must-know cards in NCERT's exact words.      Page 1 of 2 │
└──────────────────────────────────────────────────────────────┘
```

Build rules: the tile is a repeated fixed-position element per page (prints without "background graphics"); "Printed for <first name>" uses the account's first name only (no email or phone on paper, R8 2.4); the text stays real text (readable by screen readers on screen); the on-screen preview shows the same tiles so the student sees what they get. Free sees "Print sheet" with "Pro" and the honest sheet on tap: "Pro prints a watermarked sheet of any chapter's Must-know cards." The lesson summary print ("Print a summary", "Print or save as PDF") gets the same tile and footer.

### 3.10 Where Must-know shows after the re-tier

After B5: Admission of a Partner 13 of 53, Accounting for Partnership: Basic Concepts 12 of 46, Accounting Ratios 40 of 164, Planning 13 of 51 (R6, rule R2).

| Place | How it shows |
|---|---|
| Card head (session, Study, Library) | A 3 px volt rule on the card's left edge and the word "Must-know" in volt text after the kind label. No outlined pill. About one card in four, so it reads as a signal. |
| Chapter page | "13 Must-know" inside the Key cards column; "Add the 13 Must-know to Revise". |
| Time chooser | "Quick recap, 5 min" plays only Must-know. |
| Library | "Must-know only" chip; the count in the chapter line. |
| Print sheet | Must-know cards by default. |
| Free taste | The first 5 Must-know cards in book order (rule unchanged, set smaller). |
| First meeting | A small "What is Must-know?" link the first time the word appears for a student; it opens one line: "The quarter of this chapter most tied to exam questions, NCERT definitions and the chapter summary." |

"Asked in N past papers" stays hidden while `asked` is 0 on every card (R6); it returns only with real data.

---

## 4. The session recipe

### 4.1 Seconds per item

| Item | Seconds | Why |
|---|---|---|
| Key card | 15, plus 10% for reading the answer = 16.5 | The code's unit (`KEYCARD_RULES.minutesPerCard 0.25`, `KEYCARD_SECONDS 15`), B7. |
| Question (new or back) | 60, plus 10% for the reason and the line you needed = 66 | Quick practice's 60 s (`durationPerQuestionSec`), B7. Revise's 40 s is not used, so one number covers both question kinds. |
| Lesson | its `estimatedMinutes` (5 to 7) times 60 | Lesson data. Its lesson cards count as Key-card-length turns. |
| Missed card coming back once at the end | 16.5 | Played only if time remains. |

The readout rounds to whole minutes. Real dwell is not measured today (R3); the session logs seconds per item from the first release so the numbers can be corrected (metric: median seconds per item kind; guardrail: sessions that end over 125% of the chosen time).

### 4.2 Composition

Per 5 minutes the base block is 6 Key cards (99 s) and 3 questions (198 s) = 297 s. Cards are a third of the time and two thirds of the items, so a session feels card-led while questions test them.

| Length | Mix (Pro) | Seconds |
|---|---|---|
| Quick recap, 5 min | Must-know only, answers showing, up to 18 cards (oldest-seen first), `last_look` | up to 297 |
| 5 min | 6 cards, 3 questions | 297 |
| 10 min | 12 cards, 6 questions | 594 |
| 20 min | 24 cards, 12 questions; or, when the chapter has an unread lesson: the lesson (7 min), 18 cards, 7 questions | 1188 or 1179 |
| Your own N min | the lesson first if unread and N is 20 or more, then N/5 blocks | N x 60 or less |

**Filling the card slots, in order**: 1. this chapter's due Key cards (Must-know first, then oldest due), from `dueQueue` with a chapter filter; 2. cards rated Missed in the last 14 days; 3. new cards in book order (Must-know first when the session is 5 minutes, plain book order otherwise), within the day's new-card allowance (Pro 15, Free 5).

**Filling the question slots, in order**: 1. this chapter's open mistakes due in Revise (at most a third of the slots; graded by `/api/me/revise/answer`, free, move the Revise box as today); 2. questions linked to the new cards in this session (card to question index), each placed right after its card; 3. other chapter questions the student has not answered in 30 days, difficulty 40 / 40 / 20 like Quick practice.

**Interleave**: card, card, question, repeating, with a linked question pulled forward to follow its card; the lesson (if any) first; missed cards once at the end if time remains.

**Shortfall**: if cards run out, questions fill the time, and the other way round; if both run out, the session is shorter and the readout says so before the press ("That is everything in this chapter: about 7 minutes."). Never pads with other chapters unless "Your own" says so.

**Worked examples**
- Admission of a Partner, returning Pro, 10 min: 6 due cards, 6 new cards; 2 mistakes back, 2 questions linked to the new cards, 2 other chapter questions. 18 items, 594 s.
- Accounting for Partnership: Basic Concepts, new Pro student, 10 min: 12 new cards in book order; 6 questions from the 11 on its cards (linked coverage is 9 of 46 cards, R3), so only some questions follow their card.
- Accounting Ratios, Quick recap, 5 min: 18 of the 40 Must-know cards, the ones seen longest ago first; the readout says "18 of 40".

### 4.3 Free and Pro, honestly (D206, B8)

| | Free | Pro |
|---|---|---|
| Key cards in a session | The chapter's 5 open (taste) cards; at most 10 card reviews and 5 new cards a day, across sessions, Study and Revise | Every card; 15 new a day by default |
| Questions in a session | Open mistakes back: free, as in Revise. New questions: count against the day's included 10 questions (the included 10-question set, counted per question for Learn) | Free |
| Filling the time | When cards run short, more questions fill the time up to the day's 10. Free 10 min on Admission of a Partner: 5 cards and 8 questions = 610 s. Free 20 min: 5 cards and 10 questions, about 12 minutes; the readout says "Free fits about 12 minutes here today." | The full time |
| Quick recap | The 5 open Must-know cards, about 2 min; no allowance used | All Must-know |
| Library | 5 open cards per chapter whole; the rest named as Pro in place | All |
| Explore runs | 5 open cards (no allowance used: nothing is scheduled) plus free Explore questions | All cards |
| Print | Not offered; seen with "Pro" | Yes, watermarked |
| Pro prompt | Only at a real limit, once per screen (D181) | none |

### 4.4 What is reused and what the server must add

**Reused as is**: `KeyCardPlayer` and the review RPC (`POST /api/keycards/review`, modes `study` and `last_look`); FSRS scheduling and `dueQueue`; `lineNeeded()` and the link files; `/api/me/revise/answer` for mistakes back; the Revise run shell's mixed-item ideas (`mergeQueue`, per-kind players, server-confirmed answers); the lesson run (`/api/study/runs`); chapter state (`chapter_state.js`, `/api/me/chapters`); Quick practice setup for "Questions only"; Explore's feed and question card; `useDragCommit` for the feed and One at a time; `DailyMinutes` for "Your own"; the Today alternatives pool; `studyFeel.js` (`flyAway`, `softClick`) and the app's `card_stack.dart`.

**Server must add** (web routes; the app calls the same):
1. `GET /api/learn/home?subject=`: one read for both lanes: three For-you moves (kind, chapter, evidence sentence, how sure, default minutes, readout) and the subject's chapters with cards, Must-know, due, unseen, lessons, questions available, open mistakes, state. Replaces four reads (catalog, Key cards home, chapters, review) on Learn's open (R1 problem 15).
2. `GET /api/learn/plan?chapter=&minutes=&kind=mix|recap`: the composer's dry run for the readout, including the Free fit. No writes.
3. `POST /api/learn/sessions {chapter, minutes, kind, cardIds?, requestKey}`: composes and returns items (questions without keys, a signed session ticket).
4. `POST /api/learn/sessions/{id}/answer {itemId, choice}`: server-graded; returns `correct`, `keyIndex`, explanation, and the line needed; writes `user_question_progress` (add `learn` to the allowed `flow_context` values) so chapter state moves and Revise seeds as today; counts Free's daily questions per question.
5. A chapter filter on `dueCards` (`loadStates` already supports it) and a card-to-questions index (invert the link files at load).
6. The Must-know tier overlay (R6 rule R2) applied in `loadDecks`, so no deck hash or verdict changes.
7. `GET /api/learn/search?q=&subject=` over deck text held in memory, lessons and chapters.
8. `GET /api/explore/run?chapter=&minutes=10`: card ids (open ones) interleaved with question ids; cards logged with `last_look`; Keep uses `POST /api/keycards/add {cardIds}`.
9. Today: `buildMove` alternatives gain a `learn` move from the home read; Start sheet gains the row and its step.
10. The For-you move engine, a pure function shared by web and app (Dart port held equal by test, as the Key cards rules are): kinds Due, Fix (open mistakes with linked cards), Continue (last chapter, next unseen cards), Next (next chapter in book order), Recap (Must-know of a chapter not seen for 7 days or more), Lesson (unread lesson in a chapter the student studies), Start (no history). It always returns three moves of three different kinds; ties break by the student's subject order. "How sure": Sure (from the schedule or the student's own answers, 6 or more), Likely (fewer than 6 answers, or a text-matched line), A first guess (no history).

---

## 5. Motion

All values use the existing tokens where they exist (web `--ease-out`, app `Motion.ui 200 ms`, `Motion.card 240 ms`, enter 360 ms). Every motion has a reduced-motion version that keeps the information (R31, AS10).

| What moves | How | Duration and curve | Reduced motion |
|---|---|---|---|
| **Got it** (LK5) | Key presses (scale 0.96, 100 ms). The card lifts 24 px, drifts toward the kept pile top right, tilts 3 degrees, shrinks to 0.94 and fades; the pile mark ticks up with a 1.0 to 1.12 to 1.0 pop; a stamp line "Back in 3 days" (the server's `interval_days`) rises in under the keys for 700 ms. Next card rises 12 px and fades in, 60 ms after the flight starts. Soft click (web, Celebrations setting); haptic `confirm` (app). Flight starts only after the server acknowledges (as today); while waiting, the key shows its spinner. | flight 300 ms, cubic-bezier(0.2, 0.8, 0.2, 1); pop 160 ms; stamp 200 ms in, 700 ms hold, 200 ms out; next card 240 ms ease-out | Card cross-fades out and the next in, 120 ms; the stamp text still shows for 1.2 s; the pile number changes without the pop |
| **Easy** | Same path, a longer arc past the pile; stamp "Back in 9 days" | flight 340 ms | as Got it |
| **Missed** | Card slides 32 px left and drops 8 px, tilts -2 degrees, fades; the "back soon" count at the right of the counter ticks; stamp "Back tomorrow". No red flash, no shake. Haptic `tick`. | 260 ms ease-out | cross-fade 120 ms; stamp text shows |
| Show answer | Card grows to fit; the NCERT lines fade in with an 8 px rise; the rating row replaces the Show answer key by cross-fade | grow 220 ms; text 220 ms, 40 ms delay; keys 180 ms | instant height; 120 ms fade |
| Question pick | Picked option fills; correct option inks green with its tick; wrong pick gets the red outline | 180 ms ease-out | instant colours |
| The line you needed | Slides up 16 px from under the explanation and fades in | 280 ms, 120 ms after the verdict | fade 120 ms |
| Session pips | Each pip fills left to right as its item finishes | 200 ms ease-out | instant |
| Time chooser | One thumb slides on the track (N5); readout numbers cross-fade and count | thumb spring stiffness 400, damping 32 (about 240 ms); numbers 200 ms | thumb jumps; numbers change |
| For you moves | Enter with a 40 ms stagger, 8 px rise; a length chip change cross-fades only the readout and the key label | 280 ms; readout 160 ms | no stagger; 120 ms fade |
| Lane switch (390) | Indicator slides; page scrolls to the lane | 240 ms; scroll 360 ms ease-out | indicator jumps; instant scroll |
| Your part change (LK2) | Sheet closes; the list height animates; removed rows fade, added rows fade in; no entrance re-run | sheet 200 ms; height 240 ms; rows 160 ms | instant |
| Library card open | Height grows, answer fades in | 200 ms ease-out | instant |
| One at a time | Card follows the finger 1:1 (`useDragCommit`), commits past 35% or a 700 px/s fling, springs home otherwise | spring as `useDragCommit` | buttons only, 120 ms fade |
| Session end | Tallies count up; the kept pile fans out once (app `card_stack.dart`; web port); Mobi reacts once | count 600 ms ease-out; fan 480 ms | numbers shown final; no fan; Mobi still pose |
| Explore run | Snap between items; next item rises 12 px | 240 ms ease-out | snap with 120 ms fade |

Nothing loops, nothing glows, and no motion is worse than today's (Never again 5).

---

## 6. Folded, moved, kept, and the risks

### 6.1 Folded or moved (nothing he can see is dropped)

| Today | Where it goes |
|---|---|
| Learn's one "Read this next" card (`conceptsPick`) | Becomes one source of For-you moves (kinds Lesson and Fix); now one of three. |
| "Revise N concept cards" row | A For-you move when due ("12 lesson cards are due, 5 min") and the Revise door. |
| "Finish your Revise session" row | A For-you move of kind Continue, first while it exists. |
| Key cards row in Learn | Gone as a row because Learn itself is the Key cards home; its due count is the Learn sidebar badge and the Revise door. |
| `/cards` home: Today box "N cards due, Revise now" | The Revise door in Your way. |
| `/cards` subject tabs and chapter rows | Your way's subject chips and chapter list (one list with lessons). |
| "Your part" radio block | One line plus a sheet (3.2). |
| Learn's four subject tabs | The student's own subjects in Your way. |
| "Where you lose marks" | For-you Fix moves, and "Sort: Marks lost" with the red minus figures. |
| "All {subject} chapters" accordions, "Practise this chapter", "Read or print the chapter summary" | The chapter page: "Questions only", "Read the lesson", and the lesson summary print. |
| Search "chapters and lessons" | Your way's "Find a chapter" and the Library's search (now cards too). |
| Aside: lessons read, cards in Revise, cards recalled, "See your marks in Progress" | Record line under the Revise door. |
| Study preferences and weekly plan (Pro), mixed revision (Pro) | "Your plan" sheet from Learn's header; mixed revision is the Library's "Revise these N" across chapters. |
| "Test it in a full mock" | A session-end next move once a unit is done, and the record column link at 1440. |
| Deck head, "Add chapter to Revise" | Chapter page: "Add the 13 Must-know to Revise". |
| Deck Read mode | Library list view (3.7). |
| Deck Last look mode | "Quick recap, 5 min" in the time chooser and Library's Must-know only plus One at a time. |
| Deck Study mode | Kept; "Study the cards only" on the chapter page, and the Key card turn in every session. |
| Card menu: Report, Add this card | Library opened card and session card menu. |
| Print chapter sheet | Chapter page, session end, Library selection; watermarked. |
| App "Share chapter sheet" (plain text) | "Share sheet" as a watermarked PDF. |
| App "How Learn works" first-visit header | The one-time lane coach line with Mobi. |
| App "On this phone" offline packs | The Library. |
| The word "Concepts" (R1 problem 6) | Gone: "Learn", "lesson", "lesson cards". |

### 6.2 Kept unchanged

Study mode's structure and copy (front, Show answer, Missed / Got it / Easy, keys 1-3, 20-card rounds on the web, round end); the card faces and NCERT text rules (D202); Revise and its queue; the lesson player and lesson overview; "The line you needed" block (it gains two links); Explore's filters and question list; the dock and app bar; the Start sheet's existing rows; Today's lead logic; the Free numbers in B8; the state words (Not started, Too few answers, Needs work, Getting there, Holding) and the rule against "mastered".

### 6.3 Risks

1. **For you could feel like the old single pick with two extras.** Mitigation: three moves of different kinds every time, each with its own length and evidence; tests assert three distinct kinds for new, returning, Free and offline fixtures.
2. **New questions in sessions need a server-graded, keyless path that writes progress.** This is new server work (4.4 items 3-4) and touches how chapter state moves; a bug here moves states wrongly. Ship behind a flag; until it is on, sessions use mistakes back plus linked questions only through Revise grading, and the readout says "questions from your mistakes".
3. **Free's included 10-question set counted per question** changes an allowance rule (`daily_practice` per set today). It needs a migration-free counter and tests on both web and app.
4. **Thin linked coverage** (about one card in five; Financial Statements of a Company has 2 linked cards) means "on the card you just saw" shows rarely in some chapters. The label only appears when true; never claimed otherwise.
5. **Chapter question counts** are not in the maps (only linked counts). The home read must carry `available.questions`; until then rows show linked counts labelled as such.
6. **Two lanes at 390 make a long page.** The lane switch, compact alternates and the Library and Revise doors above the list keep the first screen to the lead move and the switch; measured in renders before he sees it.
7. **Route moves** (`/cards` to `/learn/c`) break saved links and app deep links if redirects miss a case; every old route is a tested redirect.
8. **Must-know overlay** changes the Free taste set and Pro's add-set for every chapter; fixtures and the Dart rules port change together (R3 item 10).
9. **App parity**: 46 Key cards goldens and the Learn door tests break; the redesign lands on web and app together (D157), with goldens regenerated only after his approval of renders.
10. **Watermark is a deterrent, not a lock** (R8 2.4). Copy never claims it prevents copying.
11. **He has not confirmed the meaning of "Fitzmeen downloading".** The sheet stays printable with the mark; if he meant "prevent downloading", the app's PDF share becomes print-only.

---

## 7. First 60 seconds

### 7.1 A brand-new 16-year-old (Commerce: Accountancy, Business Studies, Economics, English), Free, on a phone (web 390), signed in a minute ago

- **0 s.** Lands on Today. Below the lead card, the new Learn tile: "Accounting for Partnership: Basic Concepts. Chapter 1 of Accountancy. A first guess. [ Start 10 minutes ] Other moves." She does not tap it; she taps Practice on the dock.
- **4 s.** Practice opens; its tab row reads Practice, Learn, Your papers, Explore. She taps Learn.
- **6 s.** Learn: the glass lane switch "For you | Your way" and, once, a small Mobi with "For you: we pick. Your way: you pick." The lead move: "Accounting for Partnership: Basic Concepts. Chapter 1 of Accountancy, the place most students begin. How sure: A first guess." Chips 5, 10, 20 with 10 lit; readout "5 Key cards, the Free taste, and 8 questions". Two quieter rows: a 5-minute Business Studies taste and "Find your level: 6 Accountancy questions".
- **10 s.** She wants Business Studies instead. She taps "Your way"; the page glides to the lane. Chips: Accountancy, Business Studies, Economics, English. She taps Business Studies; the list shows Nature and Significance of Management at the top, "67 Key cards", "Not started".
- **16 s.** She taps the chapter. The page: "What's here: 67 Key cards, questions on its cards"; "Lined up" with 10 min lit: "5 Key cards, the Free taste. 8 questions (8 of your 10 free today)". She drags the thumb to 5 min; the readout changes to "5 Key cards and 3 questions".
- **22 s.** She taps "Start 5 minutes". The first card: "Definition  Must-know. Define management (Harold Koontz and Heinz Weihrich)." Under the key: "Say it in your head first."
- **30 s.** She taps Show answer. NCERT's line appears; under the keys, once: "Missed: back tomorrow. Got it and Easy space it out." She taps Got it. The card lifts into the pile at top right, which reads 1, and "Back in 3 days" shows under the keys.
- **40 s.** Second card, Easy; third item a question: "Pick one. If you miss it, you see the NCERT line you needed." She picks wrong. The right option inks green; the explanation; then "The line you needed" slides up with the book's line and "Back in Revise tomorrow."
- **60 s.** She is on item 5 of 8 with "About 2 min left" and knows what every key does without having read a help page.

### 7.2 A returning Pro student with 5 open mistakes (web 1440)

State: last session two days ago in Admission of a Partner; 5 open mistakes, 3 of them in Admission of a Partner and 2 in Accounting Ratios; 6 Key cards due there; Business Studies Planning was left at card 20.

- **0 s.** Opens www.mockmob.in; Today. The Learn tile: "Admission of a Partner. 6 Key cards due, 3 open mistakes. [ Start 10 minutes ] Other moves." Today's lead is a Revise move; the tile sits beside the Revise and Repairs tiles.
- **3 s.** He wants to see his choices first, so he clicks "Learn, Key cards  6 due" in the sidebar.
- **5 s.** For you, three across: Admission of a Partner ("6 Key cards are due and 3 of your open mistakes are in this chapter. How sure: Sure", 10 min, readout "6 due cards, 6 new, 2 mistakes back, 4 new questions"); Planning ("Pick up where you stopped: cards 21 to 51 are new"); Accounting Ratios ("Quick recap of the 40 Must-know cards. Last seen 9 days ago. How sure: Likely"). Your way below, with Accountancy chips and the chapter list; Revise door "24 due today, about 10 minutes".
- **9 s.** He clicks 20 on the lead move; the readout becomes "Revaluation of assets and liabilities (7 min), then 18 Key cards and 7 questions" and the key "Start 20 minutes". He decides that is too long tonight and clicks 10 again.
- **14 s.** He presses "Start 10 minutes". Pips show the mix: cards short, questions long. First item: a due card, Definition, Must-know, "What is sacrificing ratio?". Space, then 2: Got it, the card flies into the pile, "Back in 8 days".
- **25 s.** Item 3 is one of his open mistakes, labelled "Your mistake from Mock 3, Question 42". He gets it right this time; the Revise box moves up; the line reads "Right. Back in Revise in 3 days."
- **45 s.** A linked question follows a new card ("On the card you just saw"). He misses it; the line you needed appears with "Linked to this question. Back in Revise tomorrow."
- **60 s.** He is on item 7 of 18, "About 6 min left", the kept pile at 4, and the right panel shows "Lined up" ticking down. When he finishes, the end screen will offer "Fix the 2 missed cards now, about 1 min", "Another 10 minutes here: 21 new Key cards and 4 questions left", and "Next chapter in the book: Retirement/Death of a Partner, 65 Key cards", plus "Print this chapter's sheet" with his name on every page.

---

Evidence used for non-obvious choices: T001 (the Start key names the session and its counts; editable defaults from real context), T002 and R17 (pips and "7 of 18" count only real items), R18 and AS9 (readouts only from the composer, "How sure" from real data, no "Asked in N papers" while the data is empty), S014 and R10 (the Library holds rare actions; frequent ones stay on the chapter page), S016 and R11 (one name per thing; Read and Last look become self-describing controls), T004 and R16 (remembered subject, part, length and last chapter), T005 and R22 (no loss framing at Free limits), R7 with the MockMob overlay (one lead with evidence and confidence plus visible alternates), R31 and AS10 (every motion shows a state change and has a reduced-motion version), R12 (vertical lists at 390).
