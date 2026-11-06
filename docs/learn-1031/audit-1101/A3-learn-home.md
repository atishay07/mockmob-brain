# A3: Learn home, Find and the Key cards view (audit and refined design, 1 Nov 2026)

**Scope (packet U3):** `src/components/learn2/home/**` (LearnHome, SubjectShelf, Suggestions, ChapterMap, homeModel,
learn-home.css) and `src/components/learn2/cards/**` (FindView, CardsView, CardList, cardsShared, cards.css), desktop
1440, 1366 and 1024, phone 360 to 430, Night and Day.

**Owner input this answers:** LK20-LK23 (1 Nov, 1:25 am: "many things have too much blank space or need a lot of UI
refinement", "refine and think about the UI/UX of this entire thing, the entire logic behind it, and making it more
useful"), and the earlier LK1 (the way to Key cards is too small), LK9 (student control), LK10 (subject, chapter, time,
plus "a separate section that easily shows them what exactly to find where ... revise some specific cards"), LK11 (no
walls of text, a clear and dynamic next action with options), LK13 (too many Must-know marks), LK18 (Find is a search
field inside Learn).

**What I looked at:**
- Captures in `tmp/learn-1101/audit/`: 30-home-top (1440, 1366, 390, 360 Night; 1440 and 390 Day), 31-home-chapters,
  32-home-search-focused, 33-home-search-goodwill, 34-home-new, 35-home-free, 36-home-full (1440 and 390), 60-cards-all,
  61-cards-must-know, 62-cards-free-top, 63-cards-free-locked (1440 and 390), and index.md sections 1 to 5 (load times,
  CLS, "first chapter row below the first screen"). For Day on the Cards view (not captured in this build) the older
  `tmp/learn-1031/final/06-cards-answers-shown-390-day.png`; for the focus state `tmp/learn-1031/feed2/11-13`.
- Code: every file in my area; the service bodies it reads (`src/lib/server/learn.js`: subject, cards, shelves, search);
  `data/learn/suggest.js`, `data/learn/compose.js` (explicit card sets); `links.js`; `ReviseRun.jsx`; `practice.css`
  (the subject shelf); `arena.css` (shell widths, tokens); `motion-kit.css` (motion tokens).
- Standards and specs: ui-ux-standards.md (slop list, done check), AGENT_RULES.md, EVIDENCE_INDEX.csv,
  ai-slop-independent.md, DESIGN.md; DESIGN-SPEC.md (A5, A7, A10), design/B-chapters.md 3.1 and 3.7, CRITIQUE-1.md
  (H1-H7, K1-K8), FEED-2.md section 7, BUILD-1101.md (Part 1, B5, B6).

**What I did not do:** no browser, server or capture was started (the capture step ran; RAM rule). 1024 px was not
captured, so the 1024 findings are read from the CSS and marked "inferred". Find and the Key cards view were not captured
in Day in this build. Nothing here is verified on a device; section 3.11 lists the checks that will.

---

## 1. What works and must be kept

1. **The LK10 structure**, in this order: subject row, search field, three suggestions, the chapters in book order, the
   foot row (Study plan, Your record). BUILD-1101 B5 keeps it; this audit refines it and adds nothing above the subject row.
2. **The subject row** (Practice's shelf, owner-praised): the lamp-lit objects, the lamp moving on a pick, the stepped-back
   unchosen objects, the volt rule under the chosen name, the sideways peek on a phone, one subject shared with Practice.
3. **One volt key per viewport** (the lead suggestion's), the sidebar Start quietened by `data-page-primary`, outlined
   secondary keys, keycap press on the volt key.
4. **Suggestions**: always three, three kinds, a real evidence line each, keys that start at once (A7), engine R9 (no
   chapter twice, due runs hold only due cards, fix runs hold only mistakes) now landing in `data/learn/suggest.js`.
5. **Chapter rows**: the state word plus ring shape (never colour alone), one true meta line, the card count, keyed rows,
   whole-row link with 44 px plus targets, hover and press states, and the part switch's no-jump cross-fade (the LK2 fix).
6. **Search inside Learn** (LK18): 2-character minimum, 240 ms debounce, underline-only match highlight, answers folded
   with the match shown where it sits (A5), "Add a word to narrow it" when results are capped, the locked-matches line
   on Free.
7. **The Key cards view**: answers folded behind Show plus the "Show answers" switch; filter chips with real counts and
   one sliding ink indicator (volt stays on Study); the single sticky section slot; the 240 px section rail at 1100 plus;
   the open row drawn on the card face with Study this card, Add to Revise, Report; Pick and the pick bar; Free's 5 open
   cards in full with one locked line in book order and a quiet See Pro (no volt); the "Quick recap" naming.
8. **The system**: Arena tokens only (`--a-*`), so Night and Day follow; skeletons drawn at final shape; error states
   with Try again; reduced motion landing at once; NCERT's words in the reading face with the book rule.

---

## 2. Findings, by severity

Screenshot names are in `tmp/learn-1101/audit/`. Line numbers are as of commit 69768fa2b plus the working tree on 1 Nov
(`data/learn/suggest.js` is being edited by S1, so it is cited by function).

### High

**A3-01. No chapter row on the first screen at 1366x768, 390x844 or 360x780.** The core path (pick a chapter, LK10) starts
below the fold because the header stack is tall: H1 (40 px plus 30 px gap), the subject row (about 160 px with 96 px
objects at 1024 plus), a 56 px search field, 208 px suggestion tiles, then the Chapters head. On a phone the H1 repeats the
selected "Learn" tab right above it, and a count line repeats the placeholder's "868 Key cards".
- Evidence: `30-home-top-1366-night.png` (Chapters head at y 702, no row); index.md section 3 ("Learn home first chapter
  row was below the first screen" at 1366, 390 and 360); `30-home-top-390-night.png`; `learn-home.css:27,33,40,115,141`.
- Fix: section 3.1 budget. Target: two chapter rows fully visible at 1366x768, the lead tile plus one more suggestion
  fully visible at 390x844.

**A3-02. A dead band of about 365 px in every chapter row at 1440.** Titles end near x 640; the state column starts at x 1005
(`minmax(0, 1fr) 178px 124px 18px`). Fifteen rows of it read as a spreadsheet, the "too much blank space" of LK22.
- Evidence: `31-home-chapters-1440-night.png`, `36-home-full-1440-night.png`; `learn-home.css:228`.
- Fix: one two-line row anatomy at every width, and from a 960 px container the map as a book spread (Part 1 and Part 2
  side by side). Section 3.2.6.

**A3-03. "Your cards" (Due today, Missed lately, In Revise) are invisible until the student focuses the search field.**
Nothing on Learn home says they exist; the placeholder reads "Search 868 Key cards". That is a feature behind a gesture
(audience rule), it repeats LK1 ("the way to Key cards ... very small"), and it misses LK10's "separate section that easily
shows them what exactly to find where". AGENT_RULES 10 and S014: progressive disclosure is for rare controls, not frequent
ones. Focusing the field also swaps about 1,000 px of page (suggestions and chapters out, piles in) before a key is typed.
- Evidence: `30-home-top-1440-night.png` against `32-home-search-focused-1440-night.png`; `LearnHome.jsx:146-152`,
  `FindView.jsx:319-324`.
- Fix: a row of three shelf keys in the find band (under the field on a phone, beside it on desktop); a key opens that
  set in place. Typing, not focusing, swaps the panel. Sections 3.2.3 and 3.3.

**A3-04. "Study these 46" (Key cards view, filter All) plays a 10-minute run, not the 46 cards it names.** For All, the key
starts `kind: 'cards', minutes: 10` with no card ids, so the composer picks by minutes; only an explicit card set ignores
minutes. The label shows `counts.all`.
- Evidence: `CardsView.jsx:227-232,286`; `data/learn/compose.js` ("an explicit set ... minutes ignored", the `cardIds`
  branch); `60-cards-all-1440-night.png`, `60-cards-all-390-night.png`.
- Fix: send the visible card ids for every filter, at most 100. Over 100: "Study the first 100, in book order". Section 3.4.

**A3-05. "Due today 9: Revise these" opens the shared Revise run**, which plays every subject and all four Revise sources
(Key cards, again, questions, checks) as one session; in production the link has no `source=keycards`. The number shown
(9, this subject) and what plays differ, and the sidebar says "27 due" on the same screen.
- Evidence: `FindView.jsx:112`; `links.js:51` (`'/review/revise'`); `ReviseRun.jsx:4-17`;
  `32-home-search-focused-1440-night.png` (9) beside the sidebar (27).
- Fix: the Due key opens this subject's due cards and its key "Revise these 9" starts a Learn `cards` run of exactly
  those ids (the feed end's `dueOffer` pattern, BUILD 1.2). Needs `filter=due` on `GET /api/learn/cards?subject=` (S2a,
  section 3.10). Until then: link to `/review/revise?source=keycards` and show `due.all` with the label "due today, all
  subjects".

**A3-06. The Free note shows on Learn home before any limit.** "Free opens 5 cards in every chapter. Pro opens all 868." sits
above the suggestions for every Free student, new ones included. BUILD-1101 1.6 and B5: the Free line only at the real
limit; the owner's "no obvious disclaimers".
- Evidence: `34-home-new-1440-night.png`, `34-home-new-390-night.png`, `35-home-free-1440-night.png`,
  `35-home-free-390-night.png`; `LearnHome.jsx:52-64,159`; `learn.js:541` (`freeNote`).
- Fix: render only `data.free` (today's session used) as one quiet line; never `freeNote`. The card limit already shows
  where it bites (the locked line in the cards list, the locked-matches line in search).

### Medium

**A3-07. Empty bands inside the suggestion tiles.** `min-height` 196 px (phone) and 208 px (900 px plus) with the key pushed
down by `margin-top: auto`: about 42 px empty between the lead's evidence and its key at 1440, about 34 px at 390, 22 to
42 px in the small tiles. B5 asks for "no empty bands inside tiles, the Pick up tile's key right under its text, tiles that
align on one baseline".
- Evidence: `30-home-top-1440-night.png`, `30-home-top-390-night.png`; `learn-home.css:115,119-121,125,141`.
- Fix: no min-height; CSS subgrid rows so titles, evidence and keys align across tiles with the key right under the
  tallest evidence. Section 3.2.4.

**A3-08. The lead tile repeats the subject object already lit in the subject row 250 px above.** The same calculator twice on
one screen is LK21's complaint in small (every Accountancy cover showed the same object). It also costs the lead title
96 to 120 px of width, so "Pick up Admission of a Partner" wraps to two lines at 1440.
- Evidence: `30-home-top-1440-night.png`, `34-home-new-390-night.png`; `Suggestions.jsx:37`, `learn-home.css:116,126,144`.
- Fix: remove it; a pick-up lead gets a thin progress track of the real `done of of` instead (T002: only completed steps).

**A3-09. Kickers above the suggestion titles** ("Due", "Fix", "Level"): the slop list's "kickers above headings" (standards
section 4 and 10). The titles then read as long sentences ("3 open mistakes in Accounting for Partnership: Basic
Concepts").
- Evidence: `30-home-top-1440-night.png`; `Suggestions.jsx:32-38`; `homeModel.mjs:111-112`.
- Fix: drop the kind line; set the engine's `headline` in bold inside the title (B 3.1 already split `headline` and
  `chapterTitle` for this). Section 3.2.4.

**A3-10. Two search fields on one page.** "Search 868 Key cards" under the subjects and "Search chapters" in the map head;
the first already searches chapters and lessons. A student has to guess which to use (S016: consistent identification).
- Evidence: `30-home-top-1440-night.png` (y 389 and y 702); `ChapterMap.jsx:264-268`.
- Fix: one field. The map's filter goes; chapter matches lead the results.

**A3-11. The sort's "Marks open" is inert.** The service sends `marksOpen: null` on every row, so choosing it only flattens
the list in book order.
- Evidence: `ChapterMap.jsx:155`; `learn.js:353`; `homeModel.mjs:70-88`.
- Fix: Book order, Due first, Needs work first; "Marks open" appears only when at least one row has a figure (S2a wires
  the existing marks-lost read; B 3.1).

**A3-12. New student: the third suggestion "Search any card" duplicates the search field right above it, and the map shows
fifteen identical "Not started" words** (a wall of the same unknown, slop list 5).
- Evidence: `34-home-new-1440-night.png`; `data/learn/suggest.js` (`make.search`, the `isNew` order).
- Fix: the UI never draws a `search` suggestion on Learn home; S1 offers a different third kind (section 3.10). When every
  row is Not started, one line under the head replaces the fifteen words.

**A3-13. Search results waste the width and cannot be studied as a set.** At 1440 the card text stops at 62ch while Show sits
at the far right (about 430 px between). On a phone the H1 and subject row stay above the results, so only one and a half
results show. There is no "Study these" or Pick for results (picking works only through the desktop hover checkbox), so
"find goodwill, then revise those cards", the heart of LK10's "revise some specific cards", has no key.
- Evidence: `33-home-search-goodwill-1440-night.png`, `33-home-search-goodwill-390-night.png`; `FindView.jsx:241-265`;
  `cards.css:130`.
- Fix: results use the Cards view's layout (a 240 px chapter rail plus the list) from a 980 px container, the phone docks
  the field, and results get Show answers, Pick, Quick recap these N and Study these N. Section 3.3.

**A3-14. Find's shelves are four big equal tiles of mostly empty paper.** 124 px stacks with one number each; at 390 they fill
the whole first screen as a 2 x 2 grid (slop list 3: identical tiles at the same weight).
- Evidence: `32-home-search-focused-1440-night.png`, `32-home-search-focused-390-night.png`; `cards.css:224-239`;
  `FindView.jsx:76-119`.
- Fix: replaced by the 56 px shelf keys (A3-03); the piles stay the chapter page's idea.

**A3-15. Search and shelf state live only in memory.** Back from a result's chapter returns to Learn home with the query and the
shelf gone.
- Evidence: `LearnHome.jsx:129-133` (only `lv=find`); `FindView.jsx:165` (`browse` in state).
- Fix: `q` and `shelf` in the URL (replaceState, 400 ms after typing settles) and restored on load. Section 3.3.6.

**A3-16. Opening a shelf reads every chapter separately** (up to 15 requests in batches of 6) though the one-request subject
read exists. On a budget phone on patchy 4G that is seconds.
- Evidence: `FindView.jsx:39-58`; `api.js:127-128` (`subjectCards`).
- Fix: `subjectCards({ subject, filter })`.

**A3-17. The In Revise mark is an unexplained 6 px dot** hanging 10 px left of the column: 5 px from the screen edge at 390,
with nothing on screen that says what it means (shape only, standards section 5).
- Evidence: `60-cards-all-390-night.png`, `61-cards-must-know-390-night.png`, `63-cards-free-locked-390-night.png`;
  `cards.css:118`; `CardList.jsx:52`.
- Fix: the words "In Revise" in ink-3 at the end of the kind line.

**A3-18. Under a filter every row repeats the filter's own tag, and one-card sections each get a full bar.** Under Must-know,
twelve volt "Must-know" words (LK13's feeling again), and 12 cards sit under 8 bars of 44 px.
- Evidence: `61-cards-must-know-1440-night.png`, `61-cards-must-know-390-night.png`; `CardList.jsx:54-55`;
  `cards.css:89-93`.
- Fix: hide the active filter's tag; compact section bars under a filter. Section 3.4.

**A3-19. Phone chapter rows are three lines, about 92 to 100 px** (title / ref and meta / state and count): fifteen rows are
about 1,450 px of scroll.
- Evidence: `31-home-chapters-390-night.png`, `36-home-full-390-night.png`; `learn-home.css:207`.
- Fix: the two-line anatomy (64 to 72 px). Section 3.2.6.

**A3-20. "Ch 2" on three rows in a row, "Ch 1" twice.** The app splits NCERT chapters into topics, so the refs repeat and read
like a numbering bug.
- Evidence: `31-home-chapters-1440-night.png`, `31-home-chapters-390-night.png`.
- Fix: show the ref only where it changes from the row above in the same unit.

**A3-21. The layout switches on viewport width, but from 1024 px the 232 px sidebar takes the width** (main padding-left 252 px),
so at 1024 the 3-up suggestion row (a 900 px viewport query) gives about 200 px small tiles (inferred, not captured).
- Evidence: `learn-home.css:139-145`; `arena.css:164-181`.
- Fix: a size container on `.lh`; every Learn home switch reads the container. Section 3.1.

**A3-22. Motion: two staggered entrances on every load, and result rows rise again on every new query.** Tiles rise in 50 ms
steps, then rows in 24 ms steps (standards section 8: one authored page-load moment, no identical fade-ups per section);
CardList rows animate on mount, so each query replays a cascade.
- Evidence: `learn-home.css:95,205`; `cards.css:110`.
- Fix: one load moment (the tiles); the map and new results cross-fade. Section 3.6.

**A3-23. The focused search field draws a 2 px volt outline plus a 3 px volt wash ring**, the loudest volt mark on screen.
DESIGN.md's field focus is an ink border plus the soft ring, with no outline.
- Evidence: `32-home-search-focused-1440-night.png`, `33-home-search-goodwill-390-night.png`; `cards.css:212-213`.
- Fix: field focus per DESIGN.md (section 3.2.3); outlines stay on buttons and links.

### Low

**A3-24. A dead-end row.** "Computerised Accounting System" reads "Needs work" with "No Key cards yet." and has nothing to play
(its feed opens on "Nothing to play in this chapter yet").
- Evidence: `36-home-full-1440-night.png` (last row); index.md section 1 (23-feed-chapter-no-cards).
- Fix: meta "Nothing to practise here yet.", title in ink-2.

**A3-25. "Your part" choices carry no counts.** Choosing Computerised Accounting leaves one chapter with no cards; the student
cannot see that before choosing.
- Evidence: `36-home-full-1440-night.png`.
- Fix: a count line under each choice ("5 chapters", "1 chapter").

**A3-26. Part and unit headings are inverted.** The part (a whole book) is 14 px ink-2, the unit under it 15 px display ink.
- Evidence: `31-home-chapters-1440-night.png`; `learn-home.css:193,198`.
- Fix: part 17 px display ink; unit 13.5 px ink-3.

**A3-27. Key cards view at 1440: three left edges.** The back link sits at x 280, the section rail at x 350, the list at x 645.
- Evidence: `60-cards-all-1440-night.png`; `CardsView.jsx:239-262`.
- Fix: the back link becomes the first item of `.l2c-layout`, spanning both columns.

**A3-28. Layout shift on Learn home** of 0.011 to 0.069 (0.069 at 360): skeleton tiles and rows are not the real heights.
- Evidence: index.md section 3 (home-top 360 night, CLS 0.069).
- Fix: skeletons at the new final heights (section 3.5).

**A3-29. Due counts change scope by surface without saying so:** the sidebar "Learn, Key cards 27 due" counts all subjects,
the page counts Accountancy (9), the suggestion counts a chapter (3).
- Evidence: `32-home-search-focused-1440-night.png`.
- Fix: the Due key's accessible name names its subject; the sidebar badge gets the tooltip "Due today in all subjects"
  (packet P).

**A3-30. "Too few answers" reads as a reprimand to a 16-year-old.** It is the shared label in `data/chapter_state.js:21`, so
it changes product-wide; the owner's call. Suggested: "Few answers yet".

---

## 3. The refined design

**The idea in one paragraph.** Learn home stays the student's desk for one subject, in the same order, with less air and
nothing hidden: the subjects, then a **find band** (the search field and three shelf keys, the "separate section" of LK10
in one line), then the three suggestions sized to their content, then the chapters as a book's contents (on desktop the
two parts face each other like an open book). Search and the shelves open in place as the subject-wide Key cards view, the
same component as a chapter's Key cards view, so finding and revising specific cards is one idea everywhere. Every number on
a key is exactly what that key plays.

### 3.1 Layout by width

`.lh` becomes a size container: `container: lh / inline-size;` (width stays `min(100%, 1040px)`). Every Learn home switch
below reads the container width, not the viewport (A3-21). Shell numbers: the sidebar shows from a 1024 px viewport (main
padding-left 252 px); at 1366 and 1440 the container is 1040 px; at 1024 about 740 px; phones use the shell's 15 px gutter.

The H1 and the subject row's object size follow the viewport (they belong to the shell's 1024 px switch); everything else
follows the container.

| Container width (typical viewport) | Find band | Suggestions | Chapters |
|---|---|---|---|
| under 560 (phones 360 to 430) | field, then 3 keys in a row | lead card, then 2 compact rows | one column, two-line rows |
| 560 to 879 (tablets; a 1024 px window with the sidebar, about 740) | field, then 3 keys | lead full width, two tiles side by side | one column, max 760 px; sticky part titles from a 1024 viewport |
| 880 to 959 (about 940 to 1010 without the sidebar, 1150 to 1230 with it) | field and keys in one row from 900 | 3-up, subgrid | one column, max 760 px |
| 960 and up (1280, 1366, 1440) | one row: field and keys | 3-up, subgrid | book spread, two columns |

| Viewport | H1 | Subject row |
|---|---|---|
| under 1024 | visually hidden (the selected Learn tab names the page) | Practice's phone shelf (72 px objects, 96 px items, the peek) |
| 1024 and up | visible, 40 px | 80 px objects, spread across the row as on Practice |

Spacing (4-point scale, explicit margins instead of the uniform `gap`): H1 to subject row 12 px; subject row to find band
20 px (phone 14 px); find band to Free line or suggestions 24 px (phone 20 px); suggestions to Chapters head 32 px (phone
28 px); Chapters head to the first part title 8 px; map to foot 28 px (phone 24 px).

**Vertical budget, 1366x768 Night** (top bar 63 px):

| Block | Now (y) | Proposed (y) |
|---|---|---|
| H1 "Learn" | 95 to 137 | 91 to 133 |
| Subject row | about 170 to 327 | 145 to 282 (137 px) |
| Search field | 362 to 418 | find band 302 to 354 (field and keys, 52 px) |
| Suggestions | 448 to 656 | 378 to 558 (about 180 px) |
| Chapters head | 680 to 724 | 590 to 630 |
| First chapter row | below 768 | 692 to 756, one per part, both fully visible |

**Vertical budget, 390x844 Night** (shell header and tab row end at 126):

| Block | Now (y) | Proposed (y) |
|---|---|---|
| H1 "Learn" | 150 to 180 | hidden (the selected tab says Learn) |
| Subject row | 205 to 330 | 136 to 264 |
| Search field | 355 to 410 | 278 to 330 (52 px) |
| Count line | 434 | removed (the placeholder says 868 Key cards) |
| Shelf keys | none | 340 to 396 (56 px) |
| Lead suggestion | 468 to 663 | 416 to 598 (about 182 px) |
| Second suggestion | 674, half under the dock | 606 to 690, fully visible |
| Third suggestion | below | 698 to 782, partly under the dock (top at about 765) |

At 360x780 the lead is fully visible above the dock. At 430x932 all three suggestions are.

### 3.2 Components, exact values

#### 3.2.1 H1
- From a 1024 px viewport: unchanged ("Learn", 750 40 px/1.04 display, -0.035em).
- Below 1024: visually hidden, kept for screen readers (`position: absolute; width: 1px; height: 1px; overflow: hidden;
  clip-path: inset(50%); white-space: nowrap;`). The selected "Learn" tab above it already names the page.

#### 3.2.2 Subject row (`SubjectShelf`, overrides in `learn-home.css`)
- Phone and tablet: unchanged (Practice's 72 px objects, 96 px items, 14 px names, the peek).
- From 1024: `--pr-obj: 80px` (from 96), name 16 px/700, the chosen subject's counts line 13.5 px ink-2 (unchanged,
  "868 Key cards, 15 chapters, 4 lessons"), item `padding-bottom: 10px`. Row height about 137 px. The items keep
  Practice's spread across the width (consistency with the praised shelf).
- Remove the phone counts line under the search (`.lh-subject` block below 1024); the chosen subject's name stays the
  object's label and the region keeps an sr-only heading.

#### 3.2.3 The find band (`.lh-find`): the search field and the shelf keys
Container under 900: two rows (field, then keys, 10 px apart). From 900: one row, `display: grid;
grid-template-columns: minmax(320px, 1fr) auto; column-gap: 12px; align-items: center;`.

**Field** (shared `.l2f-search`):
- 52 px tall (from 56), radius 14 px, 1 px `--a-line-strong`, background `--a-raised`, 16 px/500 text (no iOS zoom),
  search icon 20 px at 16 px from the left, padding `0 48px`.
- Placeholder "Search 868 Key cards" (the count from `subject.cards`); a subject with no cards: "Search chapters and
  lessons".
- Focus (DESIGN.md field focus, A3-23): `outline: none; border-color: var(--a-ink-3); box-shadow: 0 0 0 3px
  var(--a-volt-wash);`. No volt outline on the field.
- Desktop (`(hover: hover) and (pointer: fine)`, field empty and not focused): a 22 x 22 px key hint "/" at 14 px from the
  right (12 px/600, 1 px solid currentColor, radius 6 px, ink-3, opacity 0.7). Pressing "/" anywhere outside a text field
  focuses the search (`aria-keyshortcuts="/"`).
- Clear: the 44 x 44 px x when there is text (unchanged).
- Cancel: a 44 px text key (15 px/650 ink) beside the field while it has text, and on a phone while it has focus. Cancel
  clears, blurs, returns to the chapters and restores the page's scroll position from before the focus.

**Shelf keys** (new `ShelfKeys` in `home/`): three keys in this order, from `GET /api/learn/shelves`:

| Key | Visible label | What it does | Accessible name |
|---|---|---|---|
| Due today | `9` / `due today` | opens the subject's due cards in place; its volt key "Revise these 9" starts a Learn `cards` run of exactly those ids | "Due today: 9 Accountancy cards. Show them" |
| Missed lately | `6` / `missed lately` | opens the missed set in place | "Missed lately: 6 cards in the last 14 days. Show them" |
| In Revise | `26` / `in Revise` | opens the held set in place | "In Revise: 26 cards in 3 chapters. Show them" |

- Phone and tablet (two lines): `display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 8px;` each key 56 px
  tall, radius 14 px, padding `8px 12px`, left-aligned: count 18 px/1 750 display, tabular; label 12.5 px/1.2 600 ink-2,
  4 px under it. Width at 390: 114 px; at 360: 104 px (fits "missed lately").
- From 900 (inline, one line): 52 px tall, padding `0 16px`, count 16 px/750 display tabular ink, 6 px, label 14.5 px/600
  ink-2. Total width about 412 px; the field takes the rest (about 616 px at 1040).
- Rest: background `--a-raised`, 1 px `--a-line-strong`. Hover (fine pointer): border `--a-line-hover`, background
  `--a-hover`. Focus-visible: 2 px `--a-focus`, offset 2 px. Press: scale 0.97 (100 ms), release on `--mm-press-lift`
  (445 ms).
- Selected (its set is open below): `aria-pressed="true"`, background `--a-ink`, count and label `--a-bg`, border
  transparent (the same ink fill as the filter chips), 160 ms `--mm-ease-out` on background-color.
- Zero: count and label ink-3, border `--a-line`, `aria-disabled="true"`, no hover, accessible name "No cards due today"
  (or "None missed lately", "Nothing in Revise yet"). Still drawn: zero is a true value.
- All three zero (a new student): the keys collapse to one line (14 px/1.45 ink-3), "Nothing in Revise yet. Cards you study
  land here." (under the field at every width).
- A subject with no cards: no shelf keys and no line.
- Must-know is not a home key (LK13: the subject-wide set is 229 cards and not a first-screen action). It stays one tap
  away as the fourth chip inside the opened set (3.3.4), and per chapter in the Key cards view.

#### 3.2.4 Suggestions (`Suggestions.jsx`)
- Remove the kind line (`.lh-sug__kind`) and the lead's `SubjectObject` (A3-08, A3-09).
- Title: the lead uses the engine's `title`, all 700. The other two set the engine's `headline` in bold inside the title:
  `<b>{headline}</b>{title.slice(headline.length)}` when `title` starts with `headline` (rest weight 500, ink), else `title`.
  So "**3 cards due** in Accounting Ratios", "**3 open mistakes** in Change in Profit Sharing Ratio", "**Next in the
  book**: Retirement and Death of a Partner".
- A `search` suggestion is never drawn on Learn home (the field is on screen). If the engine sends one, draw two tiles
  (`grid-template-columns: minmax(0, 1.45fr) minmax(0, 1fr)`). S1 replaces it (3.10).
- Pick-up lead only: a progress track under the evidence: `role="img"`, `aria-label="6 of 16 done"`, 4 px tall, radius
  2 px, width 100% up to 240 px, track `--a-line`, fill `--a-ink-2` at `done / of`. It fills once per visit (3.6).
- No `min-height` anywhere.

**Container 880 and up (3-up):**
```css
.lh-sugs { display: grid; grid-template-columns: minmax(0, 1.45fr) minmax(0, 1fr) minmax(0, 1fr);
           grid-template-rows: repeat(4, auto); column-gap: 12px; }
.lh-sug  { grid-row: span 4; display: grid; grid-template-rows: subgrid; row-gap: 6px; }
/* rows: 1 title, 2 evidence, 3 track (pick-up only; empty elsewhere), 4 key (align-self: end, margin-top 8px) */
```
- Lead: padding `20px 20px 18px`, radius 20 px, title 22 px/1.18 700 display -0.022em, evidence 15 px/1.45 500 ink-2,
  volt key 48 px, auto width, min-width 200 px.
- Others: padding `18px 18px 16px`, radius 18 px, title 16 px/1.35, evidence 14 px/1.45 ink-2, outlined key 44 px, full
  tile width.
- Surface, border and shadow unchanged (`--lh-surface`, 1 px `--a-line`, `--a-shadow-1`).
- Expected height about 170 to 190 px (now 208 px plus the bands).

**Container 560 to 879:** the lead spans both columns; the two others sit side by side sharing subgrid rows.

**Under 560 (phones):**
- Lead card: padding `18px 16px 16px`, radius 20 px, title 22 px/1.18 (no clamp), evidence 15 px/1.45 ink-2, the track
  (pick-up), volt key full width, 48 px. About 182 px tall.
- Compact rows (unchanged grid `minmax(0, 1fr) auto`, padding `12px 12px 12px 16px`, radius 16 px): title 15 px/1.3 with the
  bold headline (no clamp: chapter names are names, standards section 2); evidence 13 px/1.4 ink-3 on one line with
  ellipsis (long low-value text; its full text is the key's `aria-describedby`); the key 44 px, min-width 88 px, short
  label (`shortAction`, unchanged: "Revise", "Fix, 10 min"). About 84 px tall.

#### 3.2.5 The Free line (only at the real limit)
- Drop `FreeNote` and `freeNote` from Learn home.
- When `data.free` is not null (today's Learn session is used): one line under the find band, above the suggestions:
  the server's text ("Your free Learn session for today is done. Explore questions stay free. Pro has as many as you
  like.") 14 px/1.5 500 ink-2, then the text key "See Pro" (650, underline `--a-line-strong`, 44 px target) opening
  `openUpgrade({ trigger: 'learn_home' })`. No modal, no volt. A 44 px dismiss x hides it until the next IST day
  (localStorage key `mm:learn:free-line:<IST day>`).
- The suggestions' own evidence lines then carry "Key cards only today." (engine R9.6).

#### 3.2.6 Chapters (`ChapterMap.jsx`)
**Head:** `display: grid; grid-template-columns: minmax(0, 1fr) auto; align-items: center;` "Chapters" (750 20 px/1.2
display, -0.02em) and the sort button (unchanged look). The map's "Search chapters" field and its live region go (A3-10).
- Sort menu items: "Book order" (default), "Due first" (due desc, then open mistakes desc, then book order), "Needs work
  first" (Needs work, Getting there, Too few answers, Not started, Holding, then unknown; ties in book order). "Marks open"
  is listed only when at least one row has a `marksOpen` figure.
- Every row is Not started (a new student): one line under the head, 13.5 px/1.45 ink-3, "All 15 chapters are new to
  you.", and the rows draw no state word or ring.

**Row anatomy, every width (A3-02, A3-19):**
```css
.lh-row__link { display: grid; grid-template-columns: minmax(0, 1fr) auto 16px;
                grid-template-areas: 'title count chev' 'sub sub chev';
                column-gap: 12px; row-gap: 4px; align-items: baseline; min-height: 64px; padding: 10px 4px; }
.lh-row__title { grid-area: title; font: 650 16px/1.35 var(--font-body); color: var(--a-ink); text-wrap: pretty; }
.lh-row__count { grid-area: count; font: 600 13.5px/1.35 var(--font-body); color: var(--a-ink-2);
                 font-variant-numeric: tabular-nums; white-space: nowrap; }
.lh-row__sub   { grid-area: sub; display: flex; flex-wrap: wrap; align-items: center; gap: 2px 12px;
                 font: 500 13px/1.4 var(--font-body); color: var(--a-ink-2); }
.lh-row__state { display: inline-flex; align-items: center; gap: 6px; font-weight: 600; } /* ring 14 px */
.lh-row__chev  { grid-area: chev; align-self: center; width: 16px; color: var(--a-ink-3); }
```
- Line 1: the chapter title, then "46 cards" right-aligned on the title's first baseline, then the chevron.
- Line 2: the ring and state word (colours unchanged: Needs work `--a-warn-text`, Holding `--a-good-text`, Not started and
  Too few answers ink-3), then the meta: "Ch 1, 3 due, 3 open mistakes". The ref ("Ch 1") shows only where it differs
  from the row above in the same unit (A3-20); in a sorted flat list it always shows.
- No cards and no questions: title ink-2, meta "Nothing to practise here yet." (A3-24).
- Hover, focus, press: unchanged. No entrance animation on rows (3.6).

**Book spread, container 960 and up:**
- Two parts: `.lh-map__parts { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); column-gap: 48px;
  align-items: start; }`, one part per column, DOM order = book order. Three or more parts flow into the same grid row by
  row.
- One part (English): the part's units flow into `columns: 2; column-gap: 48px;`, each unit `break-inside: avoid`, the
  part title `column-span: all`.
- A sorted list: one flat list in `columns: 2; column-gap: 48px;`, rows `break-inside: avoid`.
- Sticky part titles are off in the spread (each column starts with its title); they stay sticky in the one-column map
  from 1024.
- Column width at 1040: 496 px. The Chapters head and the foot span both columns.

**Part and unit headings (A3-26):** part title 700 17 px/1.25 display, -0.01em, ink, padding-bottom 6 px (28 px above it
in the one-column map); unit title 650 13.5 px/1.3 body, ink-3, padding `12px 0 4px`.

**Part switch (A3-25):** each choice gets a second line "5 chapters" / "1 chapter" (12.5 px/1.3 ink-3, counted from the
units carrying that `optionId`); buttons min-height 56 px. Everything else unchanged (thumb 240 ms, held choice, hint line).

**Foot:** unchanged rows; full width under the map (both columns in the spread).

### 3.3 Find: search, results and the opened sets

#### 3.3.1 Focus and typing
- Focusing the field with no text swaps nothing (A3-03). On a phone or any coarse pointer it docks the field: scroll so the
  field's top sits 8 px under the top bar (`behavior: 'smooth'`, instant under reduced motion), so the keyboard does not
  cover what follows.
- From the first typed character (results from 2 characters, debounce 240 ms, unchanged) the panel under the find band
  shows results; clearing the text brings the chapters back.
- While results or an opened set show, the find band is sticky: `position: sticky; top: var(--arena-topbar-h, 63px);
  z-index: 6; background: var(--a-bg); padding-block: 8px;` with a 1 px `--a-line` bottom border once it sticks.
- Recent searches (P2, device convenience): on focus with empty text, a popover under the field lists up to 5 of this
  subject's recent queries (localStorage `mm:learn:recent:v1`), 44 px rows, a "Clear" text key in its head; Escape or a
  pick closes it; it never covers the field.

#### 3.3.2 Results panel
- Container 980 and up: `display: grid; grid-template-columns: 240px minmax(0, 680px); column-gap: 48px;` (the Key cards
  view's own layout). The left rail: "In 4 chapters" (13 px/1.2 650 ink-3) and one 44 px row per chapter with its match
  count, jumping to that group (`goToSection`, unchanged); sticky at `top: 140px` under the sticky find band. Under 980:
  one column.
- Head: "Results for “goodwill”" (700 18 px/1.3 display) and, on the same line, "50 cards in 4 chapters" (600 14 px ink-3,
  tabular, `role="status"`), plus ", 1 lesson" when there are lessons.
- Tools row (as the Key cards view): "Show answers" switch, "Pick".
- Keys row: "Quick recap these 50" (outlined) and "Study these 50" (volt, the panel's one volt key) when 1 to 100 cards
  are open matches; over 100: no volt key and the line "120 cards match. Pick up to 100 to study them, or add a word."
  (13 px/1.5 ink-3). Both keys pass the result card ids (at most 100).
- Chapter matches (a chapter not already a group below) and lessons: up to 3 rows each, then "Show all 7 chapters" as a
  text key.
- Card groups: CardList, answers folded, the match underlined (unchanged).
- Empty: "Nothing matches “goodwil”." (700 18 px) and "Check the spelling, or try a term from the book." (15 px ink-2).
- Error: unchanged (`ErrorState`, "Search did not load").
- Loading: the head line and 6 rows at 64 px (skeleton).

#### 3.3.3 Phone results
One column under the docked, sticky find band; the H1 and subject row have scrolled away; head, tools and keys as above.
The shelf keys stay visible under the field, so a student can jump from a search to a set and back.

#### 3.3.4 An opened set (a shelf key pressed): the subject-wide Key cards view
- Head: a 44 px "Chapters" back key with a chevron icon inside it (returns to the chapters and unpresses the key), then the
  set's name (700 20 px display) and its line (14 px ink-3, tabular): "6 cards in 3 chapters, missed in the last 14 days",
  "26 cards in 3 chapters", "9 cards in 3 chapters, about 2 min" (Due today).
- Chips: Due today 9, Missed lately 6, In Revise 26, Must-know 229 (the same `FilterChips`, ink indicator), the pressed
  key's set selected. On a phone the row scrolls and fades at its edge (unchanged behaviour).
- Tools and keys as results. For Due today the keys are one volt "Revise these 9" (a `cards` run of the due ids; no recap,
  due cards need ratings). For the other sets: "Quick recap these 6" and "Study these 6".
- Groups by chapter (the bar is the chapter title linking to its chapter page). Container 980 and up: the chapter rail on
  the left.
- Data: `subjectCards({ subject, filter })`, one request (A3-16). Due today needs `filter=due` (S2a); until it lands, the
  Due key keeps the interim link of A3-05.
- Empty set: the key is disabled, so an opened set is never empty; if it becomes empty while open (cards rated elsewhere),
  "Nothing here now." (18 px) and "Rate a card in a run and it joins Revise." (15 px ink-2).

#### 3.3.5 Volt and the sidebar
In results and opened sets the panel's Study key carries `data-page-primary`, so the sidebar Start stays quiet (one volt
per viewport, existing mechanism). The lead suggestion is hidden while a panel is open.

#### 3.3.6 URL and back (A3-15)
- `q` (replaceState 400 ms after typing settles; removed when empty) and `shelf` (`due` | `missed` | `revise` | `must`).
- `LearnHome` takes `initialQuery` and `initialShelf` (the `/learn/find` page and the preview pass them, packet P) and draws
  the matching panel on load, so Back from a result's chapter or card returns to the same results or set.

#### 3.3.7 Keyboard
"/" focuses the field; Escape clears and cancels; Down from the field moves focus to the first result's row (P2); Tab order:
subjects, field, shelf keys, suggestion keys, sort, rows.

### 3.4 The Key cards view (chapter scope)
- **Back link** (A3-27): the first item of `.l2c-layout`, `grid-column: 1 / -1` from 1100, so it aligns with the rail.
- **Header:** "Key cards" at `clamp(28px, 6vw, 40px)`; one line under it (14.5 px/1.45 ink-2, tabular): Pro "Accountancy,
  Ch 1, 46 cards"; Free "Accountancy, Ch 1, 5 of 46 cards open on Free". The right-aligned count goes. Saves about 30 px on
  a phone.
- **Kind line** (A3-17, A3-18): remove the hanging dot; "In Revise" becomes words at the end of the kind line (600 13 px
  ink-3). The active filter's own tag is not drawn (Must-know under Must-know, In Revise under In Revise, Missed lately
  under Missed lately).
- **Keys** (A3-04): every filter passes the visible card ids (at most 100). All: "Study these 46" (true). Over 100 cards:
  "Study the first 100, in book order". Filtered: "Quick recap these 12" and "Study these 12" (unchanged). Keys keep their
  auto width on a phone and stack full width only when two do not fit (unchanged).
- **Section bars under a filter:** padding `10px 0 6px`, 650 13 px/1.3 body ink-3, bottom border `--a-line`. Under All:
  unchanged.
- **Free:** unchanged except the header line. The locked line stays where the first locked card would sit, with the quiet
  See Pro.
- Everything else stays (3 in section 1).

### 3.5 States

| State | Learn home | Find |
|---|---|---|
| Loading | Subject row from the profile at once; skeletons at final size: field 52, keys 3 x 56 (phone) or inline 52, lead 182 / 180, compact rows 84, head 40, 8 rows at 64 (A3-28) | head line and 6 rows at 64 |
| Error | Unchanged ("Learn did not load", "Check your connection and try again. Your cards and their schedule are safe.", Try again); the subject row and the field stay usable | unchanged |
| New student | Keys collapse to the one line; suggestions Start, Level and S1's third kind; "All 15 chapters are new to you." | as Pro |
| Free, before the limit | No Free line anywhere on Learn home | locked-matches line under results (unchanged) |
| Free, session used | The Free line (3.2.5); suggestion evidence "Key cards only today." | unchanged |
| Subject with no cards | Field "Search chapters and lessons"; no keys; rows "No Key cards yet. Questions ready." | chapters and lessons only |
| A chapter with nothing to play | Row meta "Nothing to practise here yet." | not listed in sets |
| Returning after days | Suggestions from the engine (pick-up expires per BUILD 1.3); keys show today's counts | URL restores |
| Sorted | One flat list (two columns in the spread), ref on every row | not applicable |
| Reduced motion | No rise, no track fill, fades 120 ms linear, instant scrolls | same |

### 3.6 Motion (every animation answers an action or shows a state)

| What | Motion | Duration and curve | Reduced motion |
|---|---|---|---|
| Page load (the one authored moment) | the three tiles rise 6 px and fade in, 50 ms apart | 260 ms `--mm-ease-out` | 120 ms fade |
| Rows on load | none (they arrive with the panel's fade) | | |
| Subject pick | the lamp moves (unchanged); the body below cross-fades from its skeleton | lamp unchanged; 200 ms `--mm-ease-out` | 120 ms fade |
| Panel swap (chapters to results or a set, and back) | out: opacity to 0; in: opacity and 4 px rise | out 90 ms `--mm-ease-exit`; in 210 ms `--mm-ease-out` | 120 ms fade |
| New query, same panel | the list dims to 0.55 while reading, then cross-fades; no per-row rise | 150 ms `--mm-ease-out` | instant |
| Shelf key press | scale 0.97, release lift | 100 ms; release `--mm-press-lift` 445 ms | none |
| Shelf key selected | background to ink fill | 160 ms `--mm-ease-out` | instant |
| Pick-up track | fill scales from 0 to done/of from the left | 420 ms `--mm-ease-emphasized`, once per visit | static |
| Field dock (phone focus) | page scroll | browser smooth (about 240 ms) | instant |
| Cancel appears | fade | 160 ms `--mm-ease-out` | none |
| Recent searches popover | opacity and translateY(-4px) to 0 | 160 ms `--mm-ease-out`; exit 120 ms | 120 ms fade |
| Row hover | background, chevron 2 px nudge | 150 ms / 200 ms (unchanged) | colour only |
| Chapter row to chapter page | the shell's push transition (`mm-push`) | existing | existing |
| Optional (P2) | the row title morphs into the chapter page's H1 (a shared view-transition name `lh-ch-<key>`, U4 sets the same name) | 320 ms `--mm-ease-drawer` | none |

Only transform and opacity animate (plus the existing grid-row fold in CardList and the part switch's height). No
`transition: all`, no ease-in, no scale from 0. The reduced column applies under both `prefers-reduced-motion: reduce`
and `:root[data-motion='reduced']`, as the current files already do.

### 3.7 Copy (exact strings)

| Where | String |
|---|---|
| Field placeholder | "Search 868 Key cards" / no cards: "Search chapters and lessons" |
| Shelf keys | "9 due today", "6 missed lately", "26 in Revise" (count and label on two lines on a phone) |
| Keys, all zero | "Nothing in Revise yet. Cards you study land here." |
| Due key, interim (before S2a) | "27 due today, all subjects" |
| Free line | the server's `free.text`, then "See Pro" |
| Suggestion titles | lead: the engine's `title`; others: bold `headline` plus the rest of `title` |
| Sort | "Book order", "Due first", "Needs work first" (and "Marks open" only with figures) |
| New student map | "All 15 chapters are new to you." |
| Row meta | "Ch 1, 3 due, 3 open mistakes"; nothing to play: "Nothing to practise here yet." |
| Part switch counts | "5 chapters", "1 chapter" |
| Results head | "Results for “goodwill”", "50 cards in 4 chapters", ", 1 lesson" |
| Results keys | "Quick recap these 50", "Study these 50"; over 100: "120 cards match. Pick up to 100 to study them, or add a word." |
| Results empty | "Nothing matches “goodwil”." / "Check the spelling, or try a term from the book." |
| Set heads | "Due today" / "9 cards in 3 chapters, about 2 min"; "Missed lately" / "6 cards in 3 chapters, missed in the last 14 days"; "In Revise" / "26 cards in 3 chapters"; "Must-know" / "229 cards in 14 chapters" |
| Set back key | "Chapters" (with a chevron icon inside the key) |
| Due set key | "Revise these 9" |
| Key cards header | "Accountancy, Ch 1, 46 cards"; Free: "Accountancy, Ch 1, 5 of 46 cards open on Free" |
| Key cards, over 100 | "Study the first 100, in book order" |
| Set emptied while open | "Nothing here now." / "Rate a card in a run and it joins Revise." |

All sentence case, no exclamation marks, no middle dots, no arrows appended to text, numbers as numerals.

### 3.8 Night and Day
- Only `--a-*` tokens; no new literals except the existing volt key colours.
- Shelf key, Night: background `#131a16`, border `#384736`, count `#f2f4ec`, label `#bcc5b9`; selected: fill `#f2f4ec`, text
  `#0b100e`. Day: background `#ffffff`, border `#bcc5b0`, count `#172016`, label `#3d4a39`; selected: fill `#172016`, text
  `#f4f5f0`.
- Track: Night `#253026` with `#bcc5b9`; Day `#dce1d4` with `#3d4a39`.
- Field focus ring: `--a-volt-wash` (7% volt on Night, 8% olive on Day) with the ink-3 border.
- The lit tile surface (cool top light and grain, owner W-013) stays on the suggestion tiles only. Night stays subtle: no
  new glows, gradients or glass.

### 3.9 Accessibility
- Shelf keys are `<button aria-pressed>` with the names in 3.2.3; disabled ones use `aria-disabled` with a reason in the name.
- The results count is a polite live region; the panel region keeps `role="region"` with its name ("Results", "Missed
  lately").
- Focus returns to the pressed key on "Chapters" and to the field on Cancel.
- The spread keeps DOM order equal to reading order (Part 1, then Part 2).
- Targets: keys 52 to 56 px, rows 64 px, text keys 44 px. Contrast: ink-3 on raised is above 4.5:1 in both themes.
- No state by colour alone: state words stay; In Revise becomes words.

### 3.10 Requests to other packets (write them into `tmp/learn-1101/build-notes.md`)
- **S2a (service and routes):** `filter=due` on `GET /api/learn/cards?subject=` (live, not suspended, open, due today;
  the same rule as `shelves.due`), and document `headline` and `chapterTitle` on suggestions in API-CONTRACT.md (the body
  already carries them). Optional: wire `marksOpen` from the marks-lost read.
- **S1 (engine):** for a new student, replace the third `search` suggestion with a feed suggestion: title "Chapter 1 as a
  feed", headline "As a feed", evidence "One card or question at a time, 10 minutes.", key "Open the feed" (href to the
  chapter's feed, `links.feed(key, 10)`). Optional: skip the `due` suggestion when every due card of the subject sits in
  that one chapter (the Due key already offers them).
- **P (pages):** `/learn/find` and the preview pass `q` and `shelf` to `LearnHome` (`initialQuery`, `initialShelf`); the
  production `links.revise()` gets `?source=keycards` for the interim; the sidebar due badge tooltip "Due today in all
  subjects".
- **U4 (chapter page):** only for the P2 title morph, the same view-transition name on the chapter H1.

### 3.11 Acceptance (what the builder proves, then captures)
1. 1366x768: the first chapter row of each part fully visible without scrolling. 390x844: the lead and the second
   suggestion fully visible above the dock. 360x780: the lead fully visible.
2. No row or tile has an empty band over 24 px at 1440 (measure the gap between the last text box and the next element).
3. Exactly one volt fill per viewport on home, results, an opened set and the Key cards view, at 1440, 1366, 390 and 360,
   Night and Day.
4. Every number on a key equals what it plays: Study these N starts N items; Revise these 9 starts 9; the Due key's count
   equals the run's cards.
5. Free before the limit: no Free line on Learn home. After the day's session: the line, once.
6. Back from a result's card or chapter restores the query and its results; from a set, the set.
7. Real-pointer clicks (not `element.click()`) on a subject, a shelf key, each suggestion key, a chapter row, the sort menu
   and each item, the part switch, the field, Clear and Cancel; `document.elementFromPoint` on each target returns it.
8. Keyboard: "/" focuses the field, Escape cancels, focus is visible on every control, Tab order as 3.3.7.
9. Reduced motion: no rise, no track fill, fades of 120 ms.
10. CLS under 0.01 on Learn home load at 360, 390, 1366 and 1440.
11. No horizontal scroll at 360; the three shelf keys fit at 360.
12. Captures (Night, plus Day where marked): home top 1440/1366/1024/390/360 (Day 1440 and 390); home full 1440 and 390;
    new student 1440 and 390; Free with the session used 1440 and 390; results "goodwill" 1440 and 390 (Day 390); an opened
    set (Missed lately) 1440 and 390; Key cards All and Must-know 1440 and 390 (Day 390); Key cards Free locked 390.

---

## 4. Anti-slop test and rubric (this area)

### 4.1 The 12-part anti-slop acceptance test

| # | Test | Now | Proposed (target, to verify after the build) |
|---|---|---|---|
| 1 | Identity with the logo hidden | Pass: lamp-lit subject objects, NCERT book face, volt keycaps | Pass (objects stay in the subject row; the book spread adds a book-like identity) |
| 2 | One primary action | Pass: one volt per viewport | Pass, including results and sets |
| 3 | True content | Partial: "Study these 46" plays a 10-minute run; "Due today 9" plays all subjects; an inert sort | Pass: every key plays its number (A3-04, A3-05, A3-11) |
| 4 | Hierarchy at first scan | Partial: no chapter on the first screen at 1366 and on phones; kickers; inverted part and unit | Pass: chapters on the first screen; headline-led tiles; part over unit |
| 5 | Intentional composition | Fail: dead bands in rows (365 px), tiles (42 px), results (430 px); piles of empty paper | Pass: two-line rows, the spread, subgrid tiles, rail plus list for results |
| 6 | Typography by role | Partial: kicker labels; part smaller than unit | Pass: display H1, part 17, tile titles 22/16, body 16, labels 13 |
| 7 | Every state | Partial: a wall of "Not started", "None yet" piles, the Free note before the limit | Pass: collapsed new-student lines, zero keys, Free only at the limit, set-emptied state |
| 8 | Accessible interaction | Partial: In Revise by a dot only; a 2 px volt outline plus ring on the field | Pass: words, field focus per DESIGN.md, live counts, focus return |
| 9 | No pseudo-evidence | Partial: due counts of three scopes unlabelled | Pass: scopes named |
| 10 | Motion with a reason | Partial: two staggered load cascades; rows rise on every query | Pass: one load moment; motion only for presses, swaps and the real progress track |
| 11 | One leading metric plus one guardrail | Fail: none for Learn home | Partial: defined below, not yet wired |
| 12 | "What would be better without this?" | Fail: the Free note, the second search field, the duplicate H1 and count line on a phone, the lead's repeated object, the "Search any card" tile | Pass: each removed or merged, with its job kept elsewhere |

**Leading metric and guardrail (only with usage-data consent, as A12):** leading: the share of Learn home visits that start
a run or open a chapter within 60 seconds (events `learn_home_view` and `learn_home_action { source: suggestion | chapter
| shelf | search, kind }`). Guardrail: the share of searches that end with no results or a Cancel without opening anything
(`learn_search { chars, results }`).

### 4.2 The 0/1/2 rubric (0 missing, 1 partial, 2 validated)

| Dimension | Now | Proposed (target) | Why |
|---|---|---|---|
| Task fit | 1 | 2 | LK10's flow is there, but the cards section hides behind a focus and chapters sit below the fold |
| Information architecture | 1 | 2 | two search fields, piles reached only by focus; proposed: one field, the find band, sets as the subject Key cards view |
| Content truth | 1 | 2 | A3-04, A3-05, A3-11 |
| Readable hierarchy | 1 | 2 | kickers, inverted headings, a 3-line phone row |
| Visual specificity | 1 | 2 | distinctive objects and book face, but the repeated object and generic big-number piles |
| Accessibility | 1 | 2 | dot-only state, volt field outline; proposed fixes plus live counts |
| Functional states | 1 | 2 | the Free note too early, walls of "Not started", "None yet" piles |
| Trust | 1 | 2 | unlabelled count scopes, a disclaimer before any limit |
| Intentional motion | 1 | 2 | two cascades and per-query rises; proposed one load moment |
| Performance | 1 | 1 | up to 15 requests per shelf and CLS 0.069 at 360 now; the fixes are in the spec, but only a device run can earn the 2 |
| Responsive integrity | 1 | 2 | viewport queries against a sidebar layout (1024), 3-line phone rows; proposed container queries and one row anatomy |
| Instrumentation | 0 | 1 | no metric now; defined, not yet wired |
| **Total** | **11 / 24** | **22 / 24 (target)** | The proposed scores are design targets; they count only after the builder's captures and the checks in 3.11. |

**Standards done check against the slop list (section 10), now:** floating UI covering content: none found (the dock pads
the page). Decorative gradients: none (the lit surface is the owner-asked card light). Identical tiles: the four Find piles
(fixed by the keys). Build talk: none. Missing states: the Free note too early, the wall of Not started. `transition: all`,
ease-in, scale(0): none. Pure black: none. Monospace costume: none. Glow or glass on content: none. AI clichés or
exclamation marks: none. Arrows appended to text: none. Kickers above headings: the suggestion kind words (fixed).
Fake truth: the "Study these 46" and Due key counts (fixed). Hover-only essentials: picking from search results on desktop
(fixed with Pick). Decoration standing in for structure: the lead's repeated object (removed). Invisible overlays: not
checked here (no browser in this step; check 7 in 3.11 covers it).
