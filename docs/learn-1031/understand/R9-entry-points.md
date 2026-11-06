# R9: Entry points to Learn and Key cards (31 Oct 2026)

Reading job only. Nothing was changed, built or run. Sources: web code in `wt-1031-keycards-web` (paths below are under `src/`), app code in `wt-1031-keycards-app/flutter_app/lib`, the owner's feedback file, `docs/design-decisions/pass-1019/WEB-NAV-1019.md`, `pass-1017/LEARN-REVIEW-1017.md`, `pass-1019pm/PRACTICE-COLLEGES-GOAL-1019PM.md`, the master ledger, and the walk PNGs (entry-learn-row, entry-today-revise, cards-home-free-390, result-line-you-needed on web; 01-learn-door on the app). Where a size or position is inferred from CSS or a screenshot and not measured on a live page, it says "about".

## 1. The short version

- Key cards has **no navigation entry of its own anywhere**. Its only permanent door is a single hairline text row ("Key cards", one grey line under it) inside the Learn page, below the lime "Read this next" panel. Everything else that reaches it is incidental: a link on Review chapter rows, the Revise tile's sub-line "3 Key cards among them", and Revise itself (which plays due Key cards but cannot browse them).
- Learn is **not a place**. On the web it is the third row in a list of five sub-pages under Practice (sidebar, 13.5 px, indented) and the third tab in a sideways row on a phone. In the app it is the third "door" of a segmented switch inside Practice. It never gets a dock slot.
- The owner's LK1 ("badly placed and too small") is literally accurate: the path is Practice, then Learn, then a row that looks like a footnote, then a subject tab, then a chapter row. That is 3 clicks on desktop and 4 taps on a phone before any card is seen, and a new student has no reason to start the journey (no tour stop, no Guide text, no Start sheet row, no Today module, no link from Explore).
- Past IA decisions constrain the fix: five places everywhere (D105, D114), 5-slot dock with a fixed lime Start key (NAV-1017 A1), 44 px targets (W-079), one volt fill per viewport (W-075), "never merge pages" (15 Oct rejection), and every page keeps its route (R3). Section 6 lists the options against those.

## 2. Web, 1440 px (sidebar, from 1024 px)

Shell: `app/(app)/layout.js` reads `STUDY_CONTENT_ENABLED` (line 19) and passes `studyEnabled` to `AppLayoutClient.jsx`. Line 321 `showStudy = studyEnabled || previewRoute==='/learn'`; line 323 `keepLearn` filters the Learn row out of every nav group when the flag is off. Rows come from `lib/arenaNavigation.js`.

Sidebar, top to bottom (`arenaNavigation`, lines 44-53; groups have no visible headers, they are "places"):

| Row | Style | Notes |
|---|---|---|
| Start a session | full-width lime key under the logo (`StartKey variant="sidebar"`, line 392) | outlined while a page owns a volt key (data-start-quiet, lines 206-219) |
| Today | place, bold 15 px | |
| Practice | place, bold 15 px | `/dashboard` |
| Your papers | sub, 13.5 px / weight 550, indented 28 px, "8 due" badge (Revise count) | `/review` |
| **Learn** | sub, same style | `/learn`, only if `STUDY_CONTENT_ENABLED` |
| Explore | sub | `/explore` |
| Saved | sub | `/saved` |
| Mob (if MOB_ENABLED), Your standing | place + sub | |
| You | place | |
| Progress, Your standing (Mob off), Marks trend, Colleges "DU cutoffs", Wallet (rule above), Guide, "Show me around" | subs | |
| Ask Mobi | raised door at the foot, 52 px, face + "He explains any answer." | `arena-mobi-door` |
| Night / Day / System | foot | |

- **Learn row size:** `arena-nav-link--sub` is `min-height: 44px; font-size: 13.5px; font-weight: 550` (arena.css 249-255). In a window shorter than 980 px with a fine pointer and both Learn and Mob present, rows shrink to 38 px (arena.css 2025-2027). The sidebar is 232 px wide.
- **Key cards in the sidebar:** none. `isActive('learn')` is also true for `/study/*` and for `/cards` and `/cards/*` (AppLayoutClient 339-340), so on Key cards the **Learn** row is the lit one and the top bar says "Learn" (currentTitle falls through to the Learn tab's label) while the page's own h1 says "Key cards".
- **Clicks to a chapter's cards at 1440:** Practice is not needed first, because the Learn sub-row is always visible: Learn (1) -> "Key cards" row (2) -> chapter row (3) -> deck opens in Read mode. Study or Last look is a 4th click on the segmented control (`?mode=study|last`). First subject is chosen by default (`subjects[0]`); another subject adds 1 click.
- **Would a new student notice it?** The sidebar row says "Learn", which promises lessons. Nothing in the rail hints at cards. The Key cards row inside Learn is below the fold's first block (see section 4).

## 3. Web, 390 px (phone and tablet below 1024 px)

### 3.1 The dock (`AppLayoutClient.jsx` 527-548, `arena.css` 1605-1760, `nav-places.css` 55-66)
- Capsule of five slots (Mob on) or four (Mob off, `data-slots=4`): **Today, Practice, Start (centre key), Mob, You**. `mobileNavigation` returns Today, Practice, Mob only; the shell inserts the Start key at index 2 and the You button last.
- Slot size at 390: about 70 x 64 px (WEB-NAV-1019 measured "Dock slots are 70 x 64 px, and the centre Start key is 56 x 56 px"). With Mob off, about 87 px. Icons 24 px, labels 11 px (10 px below 380, gutter 8 below 360). Capsule width is `min(100% - 32px, 440px)`, grid `repeat(5, minmax(0,1fr))`, lens a rounded plate 4 px narrower than its slot.
- **Practice carries the Revise badge** ("8 due"). Learn, Key cards, Explore, Saved, Your papers and `/study/*`, `/cards/*` all mark Practice as "within" (`PLACE_PAGES.practice` in arenaNavigation.js line 95, `dockPlaceOf`). So the dock tells a student they are in Practice while on Key cards, which is correct and unhelpful at once.
- You opens the You sheet (below). Learn is **not** in it (it left the More sheet when Concepts moved into Practice, D105/D126-era; a stale CSS comment at arena.css line ~259 still says "Learn's own row at the top of the phone sheet (D20)").

### 3.2 The You sheet (`youSheetGroups`, arenaNavigation.js 70-77)
Account card (name, Sign out, "Show me around", Guide), Ask Mobi row, "Your progress" (Progress, Marks trend, Your standing when Mob is off), "Your plan" (Colleges, Wallet), Contribute (if on), Night/Day. No Learn, no Key cards.

### 3.3 Practice's row of tabs (`PlaceTabs.jsx`, `placeTabs` in arenaNavigation.js 82-88)
- Tabs in order: **Practice, Your papers (with "8 to revise" count), Learn, Explore, Saved**. 44 px tall pills, 14 px / weight 650, padding 16 px sideways (nav-places.css 97-130). The row scrolls; a peek algorithm steers the padding so the tab under the right edge shows 30-70% of itself, and a one-time 24 px nudge plays the first time on a device (localStorage). At 390 px the mock-up showed Explore cut; with the "8 to revise" count widening Your papers, Learn is likely the peeking tab (not measured on a live page).
- The row is drawn **only on exact tab hrefs** (`at()` checks `tab.href === path`). It is therefore **not drawn on `/cards`, `/cards/<chapter>`, `/learn/<id>`, `/study/<id>`, `/learn/summary`**. A phone student on Key cards has no sideways row; the way out is the in-page "Key cards" back link (44 px high, 14 px text, `.kc-back`) or the dock.
- **Taps to a chapter's cards at 390:** Practice on the dock (1) -> Learn tab (2; may need a sideways swipe) -> scroll to the "Key cards" row (3; it sits under the 400 px lime panel, so at or just below the first screen) -> subject tab if not the first (0-1) -> chapter row (4) -> Read. Study mode is a 5th tap. 

### 3.4 What a first-time student sees
Nothing about Key cards before the Learn page. The Guide tour has a "Learn" stop ("Short lessons on a concept, a recall check to lock it in, then practice questions on it.", `lib/appTour.mjs` 14-15) and no Key cards stop. `HelpPageClient.jsx` has no Key cards copy.

## 4. The Learn page itself (where the only permanent door lives)

`app/(app)/learn/page.jsx` -> `components/study/StudyWorkspace.jsx` -> `StudyLibrary.jsx`. `?recall=due` redirects to `/review/revise?source=cards`.

Order on the page (StudyLibrary.jsx 69-148):
1. h1 "Learn", lede "Short lessons on the ideas behind your mistakes."
2. The lime "Read this next" panel (`cx-next`): one pick from where marks are lost (title, reason, one key "Start the lesson, 9 minutes", cost line "Free. Its 5 cards then join Revise, where 8 are due today."). **One fixed suggestion, one key** (this is the owner's "not dynamic" point, LK11).
3. Optional row "Finish your Revise session" / "Revise N concept cards".
4. **`<LearnKeycardsRow />`** (`components/keycards/KeycardsLinks.jsx` 13-24): `.cx-row`, a `<b>` "Key cards" at 15.5 px / 650 and one 13.5 px grey line: "NCERT's exact lines, chapter by chapter. 5 cards due today." (or without the count: "NCERT's exact lines, chapter by chapter, each with its page."), chevron at the right. It has no icon, no fill, no border except the bottom hairline; it looks identical to the "Revise N concept cards" row above it. It renders null while Key cards load, are off or fail, so the page shifts when it appears. At 390 it is about 75 px tall and begins at roughly 600-700 px down.
5. Search field ("Search chapters and lessons"), subject tabs (4 subjects only: Accountancy, Business Studies, Economics, English; `SUBJECTS` in studyCopy), "Where you lose marks" (up to 4 chapter groups, each with lessons), "All <subject> chapters" (accordion per chapter: lessons, "Practise this chapter", "Read or print the chapter summary").
6. Side column at 1440 (`cx-side`): "0 of 21 lessons read / 0 cards in Revise / 0 cards recalled", "See your marks in Progress", study preferences, "Test it in a full mock".

Key cards home (`components/keycards/KeycardsHome.jsx`, route `/cards`): h1 "Key cards", lede "NCERT's exact lines, chapter by chapter, each with the page it is on.", a Today block ("5 cards due today" + "Revise now" lime key, or "Nothing due today"), the Free Pro nudge, a subject tab row (SubjectObject + name, 5+ subjects overflow at 390), the "Your <part> in <subject>" radio picker for Accountancy, Maths and Computer Science (`OptionPicker`), then chapter rows with state word + glyph and "26 cards / 5 of 26 open". Chapter deck (`/cards/<key>`, `ChapterDeck.jsx`): back link "Key cards", header, "Add chapter to Revise", "Print chapter sheet" (Pro), segmented modes **Read | Study | Last look** (`MODES` in kinds.js; `?mode=study|last`).

**LK2 hint (the shuffling "Your part"):** `choose()` in `OptionPicker` saves the option, then `refreshHome()` re-reads GET /api/keycards. The server filters `unitsFor(subject, {option})` (lib/server/keycards.js ~252), so the chapter list under the picker is replaced in place with no loading state and no transition, and `blocksOf` regroups the units. That is the most likely cause of what he saw. Not verified in a browser.

## 5. Every other entry point, one by one

| # | Where | Label and form | Size / position | Taps from the surface it sits on | New student notices it? |
|---|---|---|---|---|---|
| 1 | Sidebar (1440) | "Learn" sub-row under Practice | 44 px row, 13.5 px, indented | Learn 1, Key cards row 2, chapter 3 | Sees "Learn"; nothing says Key cards |
| 2 | Phone Practice tab row | "Learn" third tab | 44 px pill, may peek at the edge | Practice 1, Learn 2, row 3, chapter 4 | Low; depends on the swipe nudge |
| 3 | Learn page | "Key cards" text row | about 75 px, no fill, under the lime panel | 1 from Learn | Low: reads as a footnote, shifts layout when it loads |
| 4 | Practice page, "Learn" door card (`dashboard/ConceptsPanel.jsx`, drawn only when studyEnabled) | h2 "Learn", "Short lessons on the ideas behind your mistakes.", "Next lesson" link, "All lessons" | Right half of a two-card row (Your papers left) at 1440; stacked on a phone, below the setup | 1 to Learn | It names lessons only; **no Key cards mention** |
| 5 | Review chapter rows (`review/ChapterRows.jsx` line 200, `ReviewChapters.jsx` line 147) | "Key cards for this chapter" with "N cards open, in NCERT's exact words" (`ChapterKeycardsLink`, class `rvw-lesson`, 14-15 px underlined) | Inside an opened chapter, next to "Learn the idea first" | Your papers 1, open chapter 2, link 3 | Only after opening a chapter with mistakes; this is the single contextual door into a **chapter's** deck |
| 6 | Today, "Repairs and Revise" section (`today/TodayQueue.jsx`) | Tile "Revise 8 due today", sub-line "8 waiting, 8 today. Free, about 11 min, 3 Key cards among them" | Half-width tile in the Today side column; on a phone it is section 7, far down | 1 to Revise run | Counts only; no way to see which cards or open a chapter |
| 7 | Today lead card and its two alternatives (`lib/today/move.mjs`, `lead.mjs`) | Moves: resume, check, repair, Start 10 questions, Start Revise, timed mock, smart practice. Alternatives list (`alternatives`, lines 253-263): repair, revise, quick, another subject, mock, NTA, Mob, review | Top of Today | n/a | **No Learn or Key cards move exists at all**; no `/learn` or `/cards` href in `lib/today` |
| 8 | Revise run (`/review/revise`, `revise/ReviseRun.jsx`) | Plays due Key cards as the 5th source after questions, again, checks and concept cards ("Showing your Key cards." when `?source=keycards` filtered); mix line "N Key cards" | Full-screen run, dock hidden | Today tile 1 | The student only gets cards **that were added**; Revise is the schedule, not a library |
| 9 | Result, wrong answer (`ResultPageClient.jsx` 515; `keycards/LineYouNeeded.jsx`) | h4 "The line you needed", chip "Linked to this question" / "Matched by its words", the NCERT line(s) in the book face with "Accountancy Part 1, Ch 2, p. 54", button "Add both to Revise" / "Add to Revise", "2 more lines like this today on Free." | Between the explanation and the repair box; compact card | Result already open | Strong moment, but **it has no link to the chapter's deck**: only "Add to Revise". Hidden when `source` is none, Key cards off, read fails or Free is out (402) |
| 10 | Progress (`study/StudyProgress.jsx`) | "Open Learn", "Review due cards" (-> `/learn?recall=due` -> `/review/revise?source=cards`), "Lock in new cards" | Study record block | Progress 1 | `source=cards` means **concept cards only**; due Key cards are not in that filter (`reviseQueue.js` `wanted.cards = ['card']`) |
| 11 | Start sheet (`start/startModel.mjs` `startRows`, lines 335-377) | Hero (plan), Quick practice, Full mock, NTA mode, By chapter, Smart practice, Choose your own | Centre key, 56 px on the dock, lime | Start 1, row 2 | **No Learn or cards session.** Every row opens Practice set up |
| 12 | Explore (`feed/DiscoveryFeed.jsx`) | "One question. One useful step.", subject / chapter / difficulty filters, question cards; side links "Open saved questions", "Review your timed sessions", "See progress" | 4th tab on a phone (often cut) | n/a | No link to Learn or cards; today it is questions only |
| 13 | Guide tour, Help page | Tour stop "Learn"; no Key cards copy | | | Not mentioned |
| 14 | Direct URLs | `/cards`, `/cards?subject=<id>`, `/cards/<chapterKey>`, `?mode=read|study|last`, `/learn`, `/learn?subject=`, `/learn/<unitId>`, `/learn/summary?subject=&chapter=`, `/study/<runId>`, `/review/revise?source=cards|again|questions|checks|keycards` | | | `/cards` routes are not gated by `STUDY_CONTENT_ENABLED`, only by the server's `KEY_CARDS_ENABLED` ("Key cards are not open yet" state) |

Flags and gating, so the redesign knows what hides what: `STUDY_CONTENT_ENABLED` hides the Learn sidebar row, the Learn tab, the Practice Learn card, the Guide stop, the Learn page and, because the only permanent Key cards door lives in Learn, effectively the Key cards entry. `KEY_CARDS_ENABLED` (server) makes every Key cards entry draw nothing (`useKeycardsHome` -> `off`), by design ("an entry point never leads to an empty or broken page", KeycardsLinks.jsx header).

## 6. The app (Flutter, `ui/1031-keycards`, base v16)

- **Bar:** Today, Practice, Start (centre key, an action), Mob, You (`core/router/app_shell.dart`, `routes.dart` 26-31). Learn is not a tab ("Learn is no longer a tab", router.dart 498).
- **Practice has three doors** (D126, Practice C): a segmented switch under Practice's title, `PracticeDoorSwitch` (`practice/widgets/door_switch.dart`): Practise | Your papers (open-mistakes count) | Learn. Track 52 dp, each door a 48 dp target, 240 ms slide, `showLearn` false while Learn is off server-side. `/learn` alone redirects to `/practice?door=learn` (`AppRoutes.learnDoor`).
- **Key cards entry:** `KeyCardsLearnEntry` (`keycards/widgets/keycards_entries.dart`, used at `learn/screens/learn_screen.dart` line 548): a `LearnLinkRow` titled "Key cards" with "19 due today, about 5 minutes" (or "Nothing due today", or the first-visit line "NCERT's exact lines, chapter by chapter."), pushed over the shell with `context.push(AppRoutes.keyCards)`. In the walk (01-learn-door-night-pro.png) it sits fourth on the Learn door: "How Learn works" mascot header, the lime "Read this next" panel, "Revise 12 concept cards", then "Key cards", then search. It is around 70-75% down a 1600 px screen, above the search field.
- **Second door:** `KeyCardsChapterLink` under a chapter in Review/Your papers ("Key cards for <chapter>", underlined 14.5 px, 44 dp min height, `chapter_mistakes.dart`).
- **Taps to a chapter's cards:** Practice tab 1, Learn door 2, Key cards row 3, (subject), chapter row 4, Read. Same as the phone web.
- **Not present in the app:** any Key cards or Learn card on Today (the Today feature has no learn or keycard code; its only mention is the Revise count), any Start-sheet row, any bar slot. Revise (`review/revise/revise_screen.dart`) plays due Key cards. The result's `line_you_needed.dart` and `answer_row.dart` carry "The line you needed".
- Other Learn doors in the app: Practice setup screen and the confirm sheet each have a "concepts" callback that goes to `learnDoor` (`practice_setup_screen.dart` 76, `confirm_sheet.dart` 26); a lesson link from a chapter's mistakes (`chapter_mistakes.dart` 158, `outcome_views.dart` 845).

## 7. Past IA decisions found (so the redesign does not reopen them by accident)

| ID | Where found | What it fixes |
|---|---|---|
| D20 | master ledger line 106; WEB-NAV-1019 line 17; AppLayoutClient 337 comment | "Learn needs a clear place." Still OPEN in the ledger ("clear place in navigation and a real refinement pass"). Comment: a lesson or recall run at `/study/<id>` belongs to Learn, so Learn stays current. |
| D105 / D114 | arenaNavigation.js header; AppLayoutClient 324-326 | The five places everywhere: Today, Practice, Start (action), Mob, You. Option A confirmed 19 Oct. Review moved into Practice as "Your papers"; Colleges left the dock (D104). "Moved, never removed." |
| D126 (Practice C, owner H7) | app `door_switch.dart`; ConceptsPanel.jsx comment | H7: "Your paper and learn section should not be hidden ... It seems like something extra." Learn and Your papers became doors/cards of Practice. The web did this as two cards (`pr-doors`) plus the phone tab row. |
| NAV-1017 (8.2, A1) | dashboard/DashboardPageClient 138-139; LEARN-REVIEW-1017 line 74, 239, 323, 570 | Concepts left the phone dock for More on 17 Oct; the round lime Start key beside the capsule is the owner's chosen A1 and is "chrome": one accepted second fill. The dock never changes with the page. |
| W-079 | WEB-NAV-1019 line 21; arena.css | Rail rows are 44 px (compact 38 px on short mouse windows). |
| W-075 | AppLayoutClient 221-231 | One volt key per viewport; the dock Start key goes quiet while the page's own key is on screen (`data-page-primary`). |
| D6, N17, G24, G27 | WEB-NAV-1019; PlaceTabs.jsx | Ask Mobi never below the theme control; "Show me around" stays visible; Mob must be findable (G17); the sideways tab row needs a peek, a first-view nudge and edge fades. |
| 15 Oct web-restructure rejection | WEB-NAV-1019 line 24 | "He rejected the navigation merged into 5 places with denser pages." Regrouping links is allowed; merging pages is not. |
| KEYCARDS-BUILD-SPEC section 3 | `cards/page.jsx` comment, AppLayoutClient 338 | "No new top-level tab": Key cards live inside Learn/Practice, reached from Learn and Review's chapters. The spec file itself was not found on disk in this checkout (only referenced). The owner's 31 Oct feedback (LK1) now contradicts "no tab of its own" in spirit; it asks for a first-class place. |
| NAV-1017/WEB-NAV page counts | WEB-NAV-1019 line 21 | The rail needs 976 px for option A at 44 px rows; it already compacts in a normal 780-900 px window and scrolls. |

## 8. Options to make Learn and Key cards first-class, and what the code says about each

Constraints that bind every option: no route removed (R3); five dock slots at 70 px with a 56 px Start key; labels 11 px (10 px below 380); targets at least 44 px; one lime fill per viewport; web and app should keep the same map; the owner rejects merging pages, and wants real renders before anything ships (ledger, LK14).

**Option 1. Promote Learn to its own sidebar place (web only), with Key cards as a sub-row.**
- Rail: Today, Practice (Your papers, Explore, Saved), **Learn (Key cards, Revise)**, Mob, You. A place row is 44 px bold 15 px; two subs add 88 px.
- For: the rail has no group headers, so a place is just a bold row; it answers D20 and LK1 on desktop; Key cards gets a named row at the same weight as Practice.
- Against: breaks "same five as the app" (D114) on desktop; the rail is already 976 px tall at 44 px rows and compacts to 36-38 px in a 900 px window, so about 90-130 px more means the rail scrolls on most laptops (WEB-NAV measured 911 / 976 / 1044 px for now / A / B). A phone cannot copy it without a sixth dock slot.

**Option 2. Keep Learn inside Practice, but make it first and make Key cards a sibling tab/sub-row (cheapest, no dock change).**
- Reorder `PRACTICE_PAGES` to Practice, **Learn**, Your papers, Explore, Saved; add a "Key cards" page to the group (or make Learn a hub whose first control is a Lessons | Key cards | Revise switch like the app's door switch). `placeTabs` today draws the row only on exact hrefs, so `/cards` would need `/cards` and `/cards/*` to count as "at" (or the row stays on top of deck pages) so a phone student can move sideways.
- For: matches the app's door model (D126) and the owner's "all of this in the flow" (LK8); Learn is visible at 390 without a swipe; one added sidebar row (44 px) is nearly free; the top bar stops saying "Learn" over a "Key cards" page when Key cards has its own tab.
- Against: the tab row is already too long at 390 (Explore or Saved cut); six tabs make it worse. Practice's dock badge ("8 due") would still sit on the whole place, so the dock does not say "Learn lives here".

**Option 3. A phone dock slot for Learn.**
- A sixth slot (Today, Practice, Learn, Start, Mob, You) gives about 58 px slots at 390, versus 70 now; with a 56 px Start key and the lens 4 px narrower, labels such as "Practice" at 11 px (about 46-50 px wide) leave 3-6 px each side; below 380 px the code already drops labels to 10 px because the lens ran into the letters at 360 (arena.css 1741-1752, D13). Swapping rather than adding (for example replacing Mob) breaks G17 "the Mob must be easy to find" and D105.
- For: the strongest answer to "very small, badly placed" on a phone; one tap from anywhere.
- Against: the capsule loses its calm 5-up rhythm, `grid-template-columns: repeat(5, ...)`, the lens maths (`--abn-i`, `nth-child` rules in arena.css 1696-1702 and nav-places.css 62-64) and the tour/dockPlaceOf all assume five (four with Mob off); 44 px targets at 360 px width are at risk; it also diverges from the app bar. This is the option with the highest regression risk and the most conflict with owner decisions.

**Option 4. A "Study" module on Today.**
- Today already has a pool of whole moves (`choiceMoves`, `alternatives`) and two outlined tiles (`TodayQueue`). Add a Learn move ("Read the next lesson, 9 minutes" or "Revise 5 Key cards, 2 minutes") to the pool and to the lead's two alternates, and/or a third tile "Learn" beside Repairs and Revise. The owner's LK11 asks exactly for a dynamic next action with options; this repo already has the swap-the-lead mechanism (`onPick`, kept in sessionStorage for the day) that gives "options, not one fixed suggestion".
- For: puts it where a student already starts (Today is the dock's first slot); no navigation change; consistent with D126's "not hidden".
- Against: `TodayQueue`'s grid is two tiles at 390 (about 175 px each); a third stacks. Today is already long (a phone student reaches Repairs and Revise as section 7); the lead logic (`move.mjs`, `lead.mjs`, first-week path `firstWeek.mjs`) is large and tested; adding a move changes snapshots. The first-week rail has no Learn step.

**Option 5. A row in the Start sheet.**
- `startRows` could add "Study a chapter" (pick a subject, a chapter, a length of 5/10/15 minutes; opens the Learn flow of LK10), sitting between "By chapter" and "Smart practice". The sheet is already the one place with subject chips and a duration language (Quick 10, Full, NTA).
- For: reachable from every page on the web and the app (centre key, 2 taps); free of nav changes; matches "pick a subject, concept, time" literally.
- Against: the sheet is already seven rows plus a hero, all of them paid or priced practice (`costLine`), and the owner has been wary of density; Learn is free and credit-free, so the cost slot would read "Free". Rows say "Set up" and open Practice, so a new target needs its own route.

**Option 6. Use Explore as the "feed" door for chapter runs (LK12).**
- Explore's page is `DiscoveryFeed`: a subject/chapter/difficulty filter bar over a list of question cards. A "10-minute chapter run" would be a mixed feed of Key cards and MCQs for the chosen chapter; the filters already exist. Explore is the fourth tab in Practice's row, so on a phone it is the least visible tab.
- For: no new route; a natural place for "a customised feed".
- Against: Explore says "separate from your timed mock score" and is questions only; it needs its own entry from Learn (a "Practise this chapter as a feed" action) or it will remain hidden.

**Option 7. Link "The line you needed" to its chapter deck (no nav change, high value).**
- `LineYouNeeded.jsx` shows the card(s) and "Add to Revise" only. Each card's `source` names its book chapter, and `findChapter` / `slugChapter` / `links.deck(key)` already exist in `keycards/kinds.js` and `links.js`. A quiet link "Open this chapter's cards" turns the best contextual moment into an entry point (and mirrors Review's `ChapterKeycardsLink`).
- Against: the result page is dense, and `LineYouNeeded` hides itself on many questions (source none, Free out), so it cannot be the only door.

**Combination the code makes cheapest, for the main session to judge:** Option 2 (Learn first in the Practice group, Key cards as a visible sibling, deck pages keep the row on a phone) + Option 4 (one Study module in Today's alternates) + Option 7 (link from the result). None touches the dock, the rail's height, or the five places. Option 1 and 3 need an owner decision because they cross D114 and the 5-slot dock.

## 9. Problems seen

1. Key cards has no nav entry; its one permanent door is a footnote-weight row below the lime panel in Learn (StudyLibrary.jsx 89-90, KeycardsLinks.jsx 13-24), hidden while loading so the page jumps.
2. `/cards` and `/cards/<chapter>` get no Practice tab row on a phone (`placeTabs` matches exact hrefs only), so a student there can go only back or to the dock.
3. On `/cards` the top bar says "Learn" while the h1 says "Key cards" (isActive 'learn' includes `/cards`; AppLayoutClient 339-340, 366-369), and the sidebar lights Learn.
4. "Review due cards" and "Lock in new cards" (Progress) go to `/review/revise?source=cards`, which filters to concept cards only, not Key cards.
5. Today, the Start sheet, Explore, the tour and Guide say nothing about Key cards; Today's Revise tile only counts them.
6. The Practice page's Learn card (ConceptsPanel) names only the next lesson and "All lessons".
7. "The line you needed" has no link to the chapter's deck.
8. Learn's lead is one fixed pick (`conceptsPick`), so the next action is not dynamic (owner LK11).
9. Learn's sidebar row is a 13.5 px, weight-550 sub-row, smaller than its siblings' parent rows; the Learn tab can be the cut tab on a phone.
10. Stale comment in arena.css (~259): "Learn's own row at the top of the phone sheet (D20)", no longer true.
11. LK2: choosing a part reshuffles the chapter list in place with no loading or transition (hypothesis from code, not reproduced).
12. Nothing here verified on a live account or an emulator; the dock slot widths are from WEB-NAV-1019's measurement and the CSS, not re-measured.

## 10. Files to open first

- `src/lib/arenaNavigation.js` (places, tabs, dock, `PLACE_PAGES`)
- `src/app/(app)/AppLayoutClient.jsx` (shell, `isActive`, dock, sheet, flags)
- `src/components/nav/PlaceTabs.jsx`, `src/app/(app)/nav-places.css`, `src/app/(app)/arena.css` 1605-1760
- `src/components/study/StudyLibrary.jsx`, `src/components/keycards/KeycardsLinks.jsx`, `KeycardsHome.jsx`, `ChapterDeck.jsx`, `LineYouNeeded.jsx`, `links.js`, `kinds.js`
- `src/components/today/TodayQueue.jsx`, `src/lib/today/move.mjs`, `src/components/start/startModel.mjs`
- App: `flutter_app/lib/features/practice/widgets/door_switch.dart`, `features/learn/screens/learn_screen.dart`, `features/keycards/widgets/keycards_entries.dart`, `core/router/routes.dart`, `router.dart`
- Design history: `docs/design-decisions/pass-1019/WEB-NAV-1019.md`, `pass-1017/LEARN-REVIEW-1017.md`, `pass-1019pm/PRACTICE-COLLEGES-GOAL-1019PM.md`
