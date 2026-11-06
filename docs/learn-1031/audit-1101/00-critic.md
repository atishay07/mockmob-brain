# 00. Critic: what the Learn v2 audits miss, where they disagree, and the order of work

1 Nov 2026, about 3:30 am IST. Completeness critic over A1 to A8 of the learn-1101 workflow. Read-only: the only file written
is this one. No browser, emulator or server was started, nothing was committed, no database was touched.

**What I read.** A1 to A8 in full. BUILD-1101.md in full: its Part B7 (3:15 am) already settles most UI conflicts, so this file
checks B7 too. FEED-2.md. The owner's verbatim file (LK1 to LK23) and the ledger rows LK1 to LK23. CRITIQUE-1 (E1 to E6, R8,
R9, "Not verified"). DESIGN-SPEC (A1 to A12). ui-ux-standards sections 7 to 13. AGENT_RULES. The capture index
`tmp/learn-1101/audit/index.md`.

**What I exercised (evidence, not opinion).**
- Code at HEAD `b4b42db98` (3:08 am) and the working tree at 3:23 am. U1 to U4 are editing now; `src/components/learn2/stage/`
  is new and uncommitted.
- Read-only calls to the running preview: `GET /api/learn/covers` and `GET /api/learn/cards` for Pro and Free, `commerce` and
  `new`. Six run starts (`POST /api/learn/runs`) in my own preview sessions (`_s=critic1101*`), so no other agent's in-memory
  student was touched. Nothing reaches a database.
- `stemParts` (`run/runMath.js`) run in node over the 53 fixture questions. Card id lengths over the 5,806 deck cards against
  `BODY_MAX`.
- Captures looked at: `01-explore-covers-1440-night`, `18-feed-wrong-sheet-1366-night`, `40-chapter-10min-360-night`,
  `34-home-new-390-night`.

**Read this first: the audits describe three different builds.**
- A5, A6 and A7 were written about 1:50 am against the old preview (`learnPreview.js` holding runs in Maps). S2b and S2a then
  landed the migration, the service and the routes (2:33 and 2:34 am), P the pages (2:47 am) and S1 the engine rules (3:07 am).
- All 138 captures were taken 1:36 to 2:36 am, before S1. Every screenshot shows the old engine ("Start 9 minutes", "10
  minutes on", "One feed a day on Free", no LK15 on runs).
- A1, A2, A3, A4 and A8 were written from those captures plus the S2a code.

So some logic findings are fixed in the engine and only wait for the UI to read the new fields, and some audit claims are no
longer true (section 3). Anything marked "live" below was checked between 3:12 and 3:25 am.

---

## 1. Owner items no audit covers, or covers only in part

| Item | Covered by | What is missing |
|---|---|---|
| LK1 way to Key cards | A3-03 (shelf keys on Learn home) | Navigation level not re-audited: CRITIQUE-1 H6 said LK1 was "only half met" (the sidebar row says "Learn, Key cards", the phone path is Practice, Learn tab, scroll). |
| **LK2 part switch glitch** | A3 section 1.5 lists the cross-fade as working | **Nobody exercised it.** No capture or test taps between the parts (index.md has none). The ledger still says LIVE-UNCHECKED. |
| LK3, LK8, LK9, LK11 | A3, A4 (stop sheet, resume row), A1 (Stop here) | Covered. |
| LK4 Read layout | A3 (Cards view) | Covered. |
| LK5 motion on Got it | A4 keeps the flight | No frame capture or recording. CRITIQUE-1 listed it as not verified; it still is. |
| **LK6 print sheet with the watermark** | **None** | v2 has no print path. The chapter shelf's "Print sheet" row (`chapter/chapterModel.mjs:101`) links to the Must-know list (`ChapterPage.jsx:334`, `links.cards(chapterKey, 'must')`). Nothing in `learn2/cards` or `learn2/home` prints. The watermarked sheet (`PrintSheet` with `PrintMark`) exists only in v1 (`keycards/ChapterDeck.jsx:250-258`). A4's shelf table keeps the row and says it "Opens: the Must-know cards". With the flag on, the sheet he asked for leaves Learn. |
| **LK7 Read vs Last look** | Not re-tested | v2 still has three ways to look at answers: the Cards view's "Show answers", "Quick recap" (answers showing, nothing scheduled) and "Study these" (rated). A3 adds "Quick recap these N" beside "Study these N" on every search result and shelf set, which multiplies the pair he could not tell apart. |
| LK10, LK12 | A3, A1, A2 | Covered. |
| **LK13 Must-know** | A2 (covers), A3-18 (filter views) | **Not covered inside feeds and runs.** Live: every card in a 10-minute feed is Must-know (Pro Admission 11 of 11, Pro new Basic Concepts 10 of 10, Free new Admission 5 of 5; a 10-minute chapter run 12 of 14). The re-tier is applied (Basic Concepts has 12 Must-know of 46, `GET /api/learn/cards` counts), but the composer serves Must-know first, so the run is all Must-know, and A1 3.4, B1 and the new `stage/CardFace.jsx:44-54` print "Must-know" on every one. That is "everything just has a must know mark to it" again. |
| LK14 | Process | |
| LK15 | A5 R5, A6 6, BUILD 1.6; built (`data/learn/allowance.js`, claim at the first answer) | UI states covered by A1, A2, A3, A4. Gap: after the claim a Free feed is refused while a Free chapter run becomes Key cards only, and covers then offer only "Questions on this chapter". A Free student has no cards-only feed (decision, 5.4). |
| LK16, LK17 | Closed, answered | |
| LK18 the feed as a standout phone feature | A1 | No audit saw it on a phone. All phone captures are headless 390 and 360 emulation with synthetic touch (index.md section 4). No motion recording. |
| LK19 live prototype on his phone | None | No audit opened this build over the LAN. His next look needs the LAN link and the desktop link. |
| LK20, LK22 | A1, A8; A4 | Covered. |
| LK21 | A2 (covers), A3-08 (lead tile), A1 F8 (feed), A4 F11 (chapter head) | Covered. The chapter page is still open (section 2, row 13). |
| **LK23 "we have the systems around it"** | **None** | Outside `learn2`, only `DiscoveryFeed.jsx` (covers) and `AppLayoutClient.jsx` (the sidebar row) link into v2. Review's chapter rows ("Key cards for this chapter"), the Result's "The line you needed", Today's Revise tile and alternatives, the Start sheet's "Learn a chapter", Progress and Revise still lead to v1. `/cards` and `/cards/<chapter>` (v1 Read, Study, Last look) are not redirected: `NEXT_PUBLIC_LEARN2` is read only in `learn/page.jsx`, `learn/params.js`, `ExploreCovers.jsx` and `links.js`. Turning the flag on would put two Key cards worlds side by side (LK7 and LK8 again). |
| CRITIQUE-1 E4 (open) | None | Still true. "Define partnership." (`def-partnership`, source p. 48) and "What is partnership?" (`def-partnership-meaning`, p. 1) are both in the Basic Concepts deck, and "Define partnership." is now chapter 1's cover hook and the first card of a new student's chapter 1 feed (live). Five Accountancy chapters cite their book under two spellings (for example "Accountancy : Partnership Accounts" and "Accountancy – Partnership Accounts"; "Accountancy Part 2: Company Accounts ..." and "Accountancy : Company Accounts ..."); the new source foot on every card (A1 3.4, B1) will print both. |
| CRITIQUE-1 E6 (open) | None | Still true in the preview he will open: `student=new` shows "Your papers, 8 to revise" and the dock's "8 due" (`34-home-new-390-night.png`). A first-time student is shown work he never did. |
| CRITIQUE-1 R9 (Explore label) | A2 F13 | Covered, but the fix needs `src/components/feed/QuestionCard.jsx:94`, which no packet owns (section 2, last note). |
| `/learn/run` focus route | Built by P (no shell, no view transition) | No audit has looked at the production pages behind the flag (section 4, item 8). |

---

## 2. Contradictions, and which side is right

| # | Topic | One side | Other side | Right, and why | Status |
|---|---|---|---|---|---|
| 1 | Desktop way on | A1: a labelled Previous and one volt step key in an action bar under the item; a transform pager; wheel moves at a 50 px notch or a 60 px sum, then nothing until 220 ms of quiet | A8 3.4 and B1: two 48 px chevron keys with tooltips beside the stage; A8's wheel moves at 24 px, then a 450 ms lock, native snap kept | A1. Tooltip names are hover-only (std 9, R-092); two forward controls confuse a first-time student. A8's lock also double-moves on a trackpad: inertia events come every 16 ms, so its accumulator never resets (that needs a 120 ms gap) and fires again when the 450 ms lock ends | Decided (B7 A) |
| 2 | Card semantics | A1 1.14 and 3.7: "the card is a button with a full label" | A8 F1: a `role="button"` hides the NCERT line from readers | A8 (a button's children are presentational) | Decided (B7) |
| 3 | The line you needed | A1, A4, B1: in place under the options | A8 3.3: one sheet at the feed root | In place: one stage with the run he called "quite good", nothing over the answers (slop 1) | Decided |
| 4 | Card turn | A1: 340 ms | A4 and B1: 380; A8 and A7: 420 | 340 (R-153: a result is 220 to 350 ms; it is the most repeated motion) | Decided (B7 C). A4's motion table still says 380 for the run |
| 5 | Ticks | A1: 2 px, fill 300 ms, ahead in `--a-line` | A4: 3 px, 320 ms; A8: keeps 600 ms but makes ahead ticks visible (1.22:1 on Day) | A1's size and timing with A8's ahead colour | Decided in parts; `stage.css` now has 2 px and 300 ms |
| 6 | Options after an answer | A1 and A4: the rest fade to opacity 0.4 | A8 F14: 0.55 is already 3.79:1 on Day; use ink-3, no opacity | A8. WCAG exempts inactive controls, but the distractors are what a student reads to learn after the verdict | Decided (B7 F14) |
| 7 | Haptic on a wrong answer | A4 3.5 and FEED-2: `vibrate([8, 40, 8])` | A1 H and A7: none | None (the app's haptic grammar; a buzz on a miss reads as a penalty) | Decided for the feed; A4's run table still has it |
| 8 | The line block's surface | A1: `--a-raised` and a 1 px line | A4: `--a-sunken`; A8: no surface, a hairline | One component (U1), A1's: questions are on the page now, so nothing nests | Not stated; settle once in `stage.css` |
| 9 | Close and Escape | A1: Close leaves at once; Escape never leaves | A4: Close after one item opens "Stop for now?"; A8 3.1 and 3.7: Escape closes the feed and the run | One rule for both: after at least one item, Close and Escape open the stop sheet; before any item, Close leaves. It keeps A1's "a stray key never loses the summary" and A4's LK9 control | Open: B7 makes the stop sheet a shared part, but the feed's Close still "leaves" |
| 10 | End title | A1 and B7 E: the chapter title and a done line ("All 21 done in 9 min.", "You stopped at 8 of 21.") | A4 3.4.2: keep "10 minutes on"; BUILD 1.5: "the end title ... use[s] `run.asked`" | A1 (T002: say what was done). BUILD 1.5's `run.asked` should drive the next options only. The run end also needs a `done` field: B7's server list adds only `feed.done` | Open (S3, U4) |
| 11 | Start key on a phone | A4 3.2.3: re-space the page so the key lands about 65 px above the dock at 360x780 | A8 3.7: an opaque sticky Start bar above the dock under 1024 px | A8's mechanism with A4's spacing. A4's arithmetic uses the device height; Chrome shows about 56 px less with its URL bar, and four piles (2 x 2) or a three-line title push the key further. Pad the page by bar plus dock so nothing is covered (AGENT_RULES 32) | B7 takes the finding (A8 F12), not a mechanism |
| 12 | Phone card height | A4: fill the stage | A1: fit the words, `clamp(300px, 46dvh, 380px)` | A1 | Decided |
| 13 | Chapter page identity | A4 F11: drop the subject object, show a numeral | B7: keep the object (once per page) | Neither is proven. A2 3.5 shows numerals repeat (three "Ch 2" in a row), and his LK21 words were "chapter fields are all showing just the accountancy logos". Build B7's page and let him see it without the object as well (LK19); no numeral | Decided by B7; put to him |
| 14 | Cover art | A2: the feed's opening Key card | A6 4.12 `motif` (a chapter-object map); A5 R12 `art.object`; A7 10.5 a large chapter number; BUILD B4 a fanned stack and a numeral | A2. No per-chapter art exists (A7 2.7: 29 subject objects, none per chapter); a `motif` means new paid art he did not ask for; numerals repeat | Decided (B7); keep `motif` and `art.object` out of the contract |
| 15 | Volt on covers, phone | A2: the For you cover's key only, never moving | A7 4.6 and BUILD B4: the snapped cover's key | A2 (he called a volt that moves with scroll a bug on Practice, 17 Oct F12) | Decided (B7); A7 still wrong |
| 16 | Cover student line | A2: no due counts (a feed never serves due cards) | BUILD 1.9 and A7: "3 due, 2 old mistakes"; live HEAD: "3 due, 3 old mistakes" | A2 | Decided (B7 #4); not in the code yet |
| 17 | Hook rule | A2 and B7 #4: the first card of the 10-minute feed dry run | BUILD 1.9 and HEAD (`learn.js:1144`): the first open Must-know card in book order | A2, extended: the hook of the length on screen (counts already come from per-length dry runs), and no hook when that run has no card. Live, the HEAD rule already breaks the promise (section 3) | Open (S3) |
| 18 | Keep | A5 R1, BUILD 1.1, HEAD: added to Revise as new, no rating, "In Revise" | A6 4.7: a rating of 3 with its stamp; A7 4.6: "Back Tue", "Pro" after a 402 | BUILD 1.1 (built) | Decided; A6 and A7 stale |
| 19 | LK15 claim | A5 R5, BUILD 1.6 and Part 2, HEAD: at the first answered question | A6 6 and its migration draft: at the start, in `learn_start_run`; every other start answers 402 | BUILD (built; a refresh or a mis-tap never spends the day) | Decided; A6 7.1 superseded |
| 20 | Free copy | BUILD: "Free sessions are up to 10 minutes. Pro has any length." and the session line | A8: "Free feeds run up to 10 minutes."; A6: "Your free feed for today is done ..." and "Today's free session is {chapter} ..."; FEED-2: "Your free feed ..." | BUILD (one rule for runs and feeds) | Decided |
| 21 | A question left out (409) | A1 3.10: one line and the volt Next | A8 3.5: "Press Down for the next one." (touch: "Swipe up for the next one.") | A1 (never point at a gesture as the way on) | Decided (B7 A) |
| 22 | Answer keys | A1: 1 to 4, a to d | A8: 1 to 6, A to F, and S for Keep or Save | A8 (the run already takes 1 to 6) | Not stated |
| 23 | Cover arrows | A2: in the section head, disabled at the ends | A8 3.6: over the row's edges, hidden at the ends | A2 (no control floating over covers; stable positions) | Decided (B7) |
| 24 | Search focus | A3: focus changes nothing; typing opens results | A8 F21: open Find on pointerdown or click, not on keyboard focus | A3 (simpler; WCAG 3.2.1 either way) | Decided (B7) |
| 25 | Feed length memory | A2: its own key `mm:explore:feedMinutes` | A8: the chapter page's `mm:learn2:minutes` | A2 (a 35-minute chapter choice is not a feed choice; T001) | Decided (B7) |
| 26 | Skip | A1 B: a quiet Skip on an unanswered feed question | A4 3.3.5: no key until a run question is answered | Recommend Skip in the run too, logged as a skip and never as a mistake: a forced guess writes false mistakes and false "right"s into Revise | Open |

File ownership conflicts in BUILD Part 3:
- P owns `src/app/(app)/explore/**`; U2 owns `src/app/(app)/explore/explore.css`. They overlap.
- No packet owns `src/components/feed/QuestionCard.jsx` (A2 F13: the chapter title in the question meta) or
  `src/components/keycards/keycards.css` (A2 4.4 widens `--kc-surface` to `.fxc`; the feed and the run use it too).

---

## 3. Claims I checked

### 3.1 Not true, or no longer true at HEAD

| Claim | Where | What is true now | Evidence |
|---|---|---|---|
| The covers row stops at 8 chapters | A5 F19; A6 4.12; A8's copy "Showing 5 minute feeds, 8 chapters." | No cap: 14 Accountancy covers | `data/learn/feed.js:20` (`maxCovers: null`); live covers read: 14 for all four students |
| Keep writes a fake Got it review; "Back Tue"; "Pro" after a daily 402 | A5 F6 (true then); A6 4.7 and A7 4.6 (as design) | Keep adds the card as new (`kc.add`, `addedFrom: 'manual'`), no rating, stamp "In Revise" | `src/lib/server/learn.js:925-944` |
| The feed starts a new run on every mount; a refresh locks Free out | A5 F7 | The server resumes the same chapter and kind on the same IST day, and by `resume` or `requestKey`. Only the client still ignores `resumed` and `?run=` (A8 F11 is the true part) | `learn.js:643-672`; `ChapterFeed.jsx:230` is still `Feed({ chapterKey, minutes })` |
| LK15 is a feed-only rule | A5 F20; index.md section 5 | Built for `mix` and `feed`, claimed at the first answer | `learn.js:420-431, 875`; S1 and S2b notes |
| The preview is not database-agnostic; the migration claims at the start | A6 sections 0, 1, 7.1 | `createLearn` over the memory client (06d7b40f5); the claim lives in `learn_record_event` (BUILD Part 2) | commit log; build notes |
| The Admission hook is exactly the first card its feed shows (the premise of the cover design) | A2 3.3 | **Not true live.** Pro `commerce`: hook "What is reconstitution of a partnership firm?", the feed opens on "If this amount is paid to the old partners directly (privately) ...". Free `new`: same hook, the feed opens on "What is the sacrificing ratio?". Only Basic Concepts matched. S1's order (R3) and feed pool changed the first card | covers read against `POST /api/learn/runs` (isolated sessions) |
| Headings, the panel title, the numeral and the round count in "Gabarito" | A4 3.2 to 3.4 | The display face is Bricolage Grotesque; Gabarito is declared only for a rollback and is not preloaded. Use `var(--font-display)` | `src/app/layout.js:12-24`; `src/app/globals.css:9` |
| "Print sheet ... Opens: the Must-know cards" kept as working | A4 3.2.6 | A row named Print sheet opens a list, and nothing in v2 prints (LK6) | `chapterModel.mjs:101`; `ChapterPage.jsx:334` |
| The part switch's no-jump cross-fade (the LK2 fix) works | A3 section 1.5 | Not exercised in this build | index.md (no part-switch interaction) |
| An 8,000-character body is enough for 100 card ids | BUILD Part 2 (A6 said 4,000 was too small) | The 100 longest real ids make a 10,016-character start body: a 413 on "Study these 100". Ids run to 106 characters (median 63) | `src/lib/server/learnHttp.js:27`; 5,806 deck cards |
| Free covers read "1 minute, 5 Key cards" | A2 F8 | Now "2 minutes" (18 s a card since S1). The finding stands with the new number | live covers read |

### 3.2 Confirmed by looking
- A2 F1, F2, F3: four copies of the calculator (three covers and the list head), four volt fills with the sidebar's Start, exactly
  three covers and no peek (`01-explore-covers-1440-night.png`).
- A1 F5 and A8 F3: at 1366x768 the sheet covers option D and cuts the NCERT line (`18-feed-wrong-sheet-1366-night.png`).
- A4 F5, F25, F26 and A8 F12, F13: at 360x780 the Start key is half under the dock and dimmed by its fade; "2 of 3, about 2 ..."
  is cut (`40-chapter-10min-360-night.png`).
- A3-01, A3-06, A3-08 at 390: no chapter row on the first screen; the Free note shows for a new student; the lead tile repeats
  the subject object (`34-home-new-390-night.png`).
- Code: A1 F1 (`feed.css:38-40`, mandatory snap with `scroll-snap-stop: always`); A8 F1 (`ChapterFeed.jsx:73`); A8 F19
  (`covers.css:12`, 40 px); A2 F6 (`links.js:49`); A3-04 (`CardsView.jsx:231`, no card ids for All).
- No answer key in any of the six live run bodies. Honest length works: Pro 10-minute feeds sum to 543 and 553 seconds.

---

## 4. The missing modality (what nobody looked at)

1. **Real question content.** 6 of the 53 fixture questions are match-the-column (List-I and List-II). Both renderers lose them.
   - The feed: `<h2 className="fx-stem">{q.body}</h2>` (`ChapterFeed.jsx:112`) with no `white-space` rule (`feed.css:93`), so
     the stored line breaks collapse into one paragraph.
   - The run and the new shared `stage/Question.jsx:31-41`: `stemParts` (`runMath.js:93-112`) first collapses all whitespace
     and matches only (A) to (F), lower-case roman and digits, so List-II's (I) to (IV) never split. Run in node: in 3 of the 6
     the whole List-II block is glued into step (D)'s text.
   - A1 F19 caught only Assertion-Reason. CUET Accountancy leans on match, statement (I, II, III) and case stems, and the bank
     has 1,072 Accountancy questions no audit rendered. A whole stem as an `h2` is also a heading of up to 1,186 characters.
2. **Widths and viewports.** Captured: 1440x900, 1366x768, 390x844, 360x780. Never captured: 1024 (the sidebar takes 252 px,
   so Learn home, the chapter page and Explore get about 740 px), 1366x650 (the standards' own desktop size and his laptop),
   1920x1080, 412 and 430, 768 tablet, phone landscape. Every fold check (A2 4.10, A3 3.1, A4 3.2.3) uses the device height;
   Chrome on a phone shows about 56 px less with the URL bar.
3. **Day.** Six screens at 1440 and 390 only. Never in Day: Find, the Cards view, every end screen, the checkpoint, Free and
   new-student states, the run's question and wrong line, the stop sheet.
4. **Real input and devices.** Synthetic wheel and touch only (index.md section 4): no notched wheel or trackpad on his PC, no
   finger, no budget Android, no LAN look.
5. **Keyboard, screen reader, reduced motion, zoom.** Specified by A8 and A1 3.14; none was run.
6. **Motion.** No recording or frame sheet of the turn, Keep, Got it, the line opening or the pager. He wants it "very cool"
   and judges it live.
7. **Performance.** Warm development timings and CLS only. No 4x CPU throttle, INP, long tasks or bundle size; every feed item
   renders a 3D card (A1 3.7's `content-visibility` is unmeasured).
8. **The production pages behind the flag** (`/learn`, `/learn/find`, `/learn/c/<key>`, `/learn/c/<key>/cards`, `/learn/run`,
   `/explore/run`, built at 2:47 am) were never captured. With the flag off they answer the not-found page with HTTP 200 in
   development (P's note). Nobody checked a production build, or that the live Explore page and `/learn` are unchanged with
   the flag off (B7's condition for Option A).
9. **The other subjects.** Every UI capture is Accountancy. Business Studies has no fixture questions (cards-only feeds in the
   preview), Economics has 61-character titles and 114-character hooks, English has no NCERT ref.
10. **The Free returning student** (live). Free `commerce`, Basic Concepts, a 10-minute feed: 8 items, 0 cards, 8 questions,
    opening on two old mistakes (`XXQQQQQQ`), while its cover shows the card hook "Define partnership.". Once a Free student's
    5 open cards sit in Revise (the feed never serves them), every Free feed of that chapter is a question list. For a new Free
    student, 10 of 14 Accountancy covers read "5 Key cards, 2 minutes" (fixture); a returning one sees "1 minute" covers.
11. **Pro at 20 minutes** (live, a new Pro student): 8 of 14 covers stop at the 40-new-card cap (13 to 15 minutes). A2's mix line rule ("16 Key
    cards, all it has today" when short) would be false there: those chapters have up to 164 cards. Free covers carry
    `capped: true` even when the feed is 2 minutes.
12. **The level run's end** ("Start with <chapter>", added by S1) is drawn by no audit.
13. **The Flutter port (A7) predates B7** and is stale in about 20 places: the backdrop object, 600 ms ticks, a 420 ms flip, a
    Next key at the rail's foot, the line as a bottom sheet, the streak chip, "Back Tue" and "Pro" on Keep, "Tap to turn it
    over" and "Swipe up for the next one", the volt on the snapped cover, "3 due" on covers, `FREE_FEED_USED`, a Close that
    asks nothing, grouped pips, count-up end numbers, the "Ratings join Revise" note, the lead tile object, four Find piles,
    the "Next chapter" link pile, the "Marks open" sort and a run-only right-answer look instead of the shared volt row.
14. **Instrumentation.** Every audit names a leading metric and a guardrail; none is wired or in a consent plan, so part 11 of
    the 12-part test fails everywhere.
15. **Explore's question list still sends `correct_answer`** (A5 3.3). "No key on the client before an answer" holds for
    Learn's routes, but the same questions' keys are readable from Explore's list. Pre-existing; record it.
16. **Console.** The React warning "update on a component that hasn't mounted yet" (A1 F16, A4 F32, A8 F27) is unexplained.

---

## 5. The work, in order

### 5.1 Order
P0 is what he sees next (a link on his phone and his computer, LK19). P1 comes before the flag can go on. P2 after.
Packets in different rows run in parallel.

1. **L (S3)**: the fields the UI waits on: the hook per length with a no-card answer, `studentLine` without due, `resume`,
   `refLine`, `name`, the run end's `done`, and stem blocks for match and statement questions (L1 to L4).
2. **F (U1)**: the shared stage with the agreed values (section 2 rows 4 to 9) and no Must-know tag; then the feed (F1 to F5).
3. **E (U2)**: covers on the hook, one volt, arrows and pager, the Free limit action (E1 to E3).
4. **C (U4)**: the chapter page first (Start key, note, segment, held piles, resume), then the run on U1's parts (C1 to C5).
5. **H (U3)**: Learn home's first screen, shelf keys, keys that play their numbers, the Free line (H1, H2).
6. **R (P)**: preview truth for his look (R1).
7. The verification pass (5.3) by the main session, then his look.
8. P1 across packets: print sheet, LK2 test, LK7 trim, `/cards` redirects and entry points, body cap, Free composition, content
   fixes, flag-off parity, the app plan's re-base.

### 5.2 Packets and their must-fix items

**L: logic and server** (S3 now. Files: `src/lib/server/{learn,learnPreview,learnHttp}.js`, `data/learn/**`,
`src/components/learn2/run/runMath.js`, `src/components/learn2/api.js`, `API-CONTRACT.md`, their tests; content fixes in
`data/keycards/**`.)
- **P0 L1** Hook per length: `counts[m].hook` is the first card item of that length's dry run, with `id`; `null` when the run has
  no card, so the cover shows its questions-only face with a true line. Test: a feed started after a covers read opens on
  `counts[m].hook.id` at 5, 10 and 20, Pro and Free, new and returning.
- **P0 L2** `stemParts` keeps the stored line breaks and returns blocks for List-I and List-II (upper-case roman, P Q R S and
  1 to 4 too), Statement I and II, and Assertion and Reason. One parser for the feed and the run (`stage/Question.jsx` already
  imports it). Test over the 6 match and the Assertion-Reason fixture questions: List-II never lands inside (D).
- **P0 L3** B7 #4: `studentLine` without due, `resume`, `refLine`, `name`, `history`, "First in the syllabus".
- **P0 L4** The run end gets `done: { reached, of, minutes }` (B7 adds only `feed.done`). BUILD 1.5's `run.asked` feeds the
  next options, not the title.
- **P1 L5** Free returning feeds (decision 5.4.1). Recommended: when a Free student has no fresh open card in a chapter, serve
  that chapter's open cards held in Revise as looks, due ones included (shown, never rated, nothing scheduled), so a Free feed
  keeps its cards. Otherwise the cover says "Your 5 free cards are in Revise".
- **P1 L6** Covers: `capped` only when the 10-minute clamp changed the mix; `shrink.reason` per length, so a mix line never says
  "all it has today" when the 40-card cap is the reason.
- **P1 L7** `BODY_MAX` to 16,000 (or count ids, not characters). Test with the 100 longest ids.
- **P1 L8** Content: E4 (keep one of "Define partnership." and "What is partnership?", the one that quotes the Act; fix or
  quarantine the p. 48 source in the Ch 1 deck; a test that `source.chapter` matches the deck's chapter). One display name per
  book for the source foot.
- **P1 L9** Contract: no `motif`, no `art.object`; the Free and 402 copy is BUILD's only.

**F: the feed and the shared stage** (U1. Files: `src/components/learn2/feed/**` except the covers files,
`src/components/learn2/stage/**`; give U1 `src/components/keycards/keycards.css`, the others request changes.)
- **P0 F1** A1 3.2 to 3.7 (accepted): the stage, the action bar, the pager, the keys. Verify that one wheel notch and one
  trackpad swipe move one item on a real Windows PC.
- **P0 F2** LK13: the card face prints no "Must-know" in feeds and runs, where every card is Must-know because the composer
  serves them first (`stage/CardFace.jsx:54`). The word stays in the Cards view, its filter and Find.
- **P0 F3** The stem draws L2's blocks (List-I and List-II as two lists, side by side from 768 px) in a `p` with an id, not an
  `h2`; the heading is "Question 2 of 5".
- **P0 F4** Section 2 rows 4 to 9 written once in `stage.css` (340 ms turn; 2 px ticks filling in 300 ms with A8's ahead colour;
  ink-3 rest options; no buzz on a wrong answer; one line block; one option height) and the Close and Escape rule (row 9).
- **P0 F5** A8 F1, F2, F5, F7 to F11 and F16 to F18 (accepted in B7); keys 1 to 6 and A to F.
- **P1 F6** The "This feed" sheet and the one-time nudge (in scope per B7).

**E: Explore page and covers** (U2. Files: `ExploreCovers.jsx`, `covers.css`, `coverModel.*`, `DiscoveryFeed.jsx`,
`explore.css`; add `src/components/feed/QuestionCard.jsx`, or pass the chapter title in from DiscoveryFeed.)
- **P0 E1** Covers on the hook (A2 4.1 to 4.5) with L1's hook per length, the no-card face, and a locked hook never shown as an
  empty block or "null".
- **P0 E2** One volt (the lead, `data-page-primary`), arrows in the head, the phone pager "1 of 14", the site's
  SegmentedControl at 44 px.
- **P0 E3** Free at the day's limit: every key reads "Questions on this chapter", no refused Play; the capped line only when 20
  is picked.
- **P1 E4** Option A behind the flag only, plus a test or a screenshot diff proving `/explore` with the flag off is unchanged.
- **P1 E5** `?subject&chapter` (with P's `links.explore`), chapter titles in the question meta, the default subject from the
  student (A2 F16), the mix line by `shrink.reason` (L6).

**H: Learn home, Find, cards** (U3. Files: `src/components/learn2/home/**`, `src/components/learn2/cards/**`.)
- **P0 H1** A3-01: the first chapter row of each part at 1366x768 and 1366x650; the lead and the second suggestion at 390 in
  Chrome with its URL bar showing.
- **P0 H2** A3-03 to A3-06: shelf keys; every key plays its number ("Study these N", "Revise these 9"); no Free note before the
  limit.
- **P1 H3** LK6: a Print key in the Cards view (Pro) that draws the v1 sheet (`components/print/PrintMark`, `PrintHead`) with the
  student's name and the watermark on every page. Free sees the lock only in the chapter shelf.
- **P1 H4** LK2: a test that taps between the two parts quickly on a slow network and asserts the tapped choice holds and no row
  reorders, plus one capture.
- **P1 H5** LK7 (a change to B7, which took A3 in full): drop "Quick recap these N" from search results and shelf sets. Quick
  recap stays the chapter page's text key and the Must-know set's key, so each place has one way to read and one way to study.
- **P1 H6** The rest of A3 (accepted).

**C: chapter page and run** (U4. Files: `src/components/learn2/chapter/**`, `src/components/learn2/run/**` except
`runMath.js`.)
- **P0 C1** The Start key fully visible above the dock at 360x640 (Chrome's viewport) and inside 1366x650: A8's opaque sticky
  bar under 1024 px with A4's spacing, the page padded by bar plus dock.
- **P0 C2** The note removed, the segment never rewritten, held piles on Free, the resume row (accepted).
- **P0 C3** The run on U1's parts. None of A4's divergent values: no 380 ms turn, no wrong-answer buzz, no opacity 0.4, no
  sunken line block, no 3 px ticks, no Gabarito.
- **P0 C4** Free end: the server's line and a See Pro text key; the volt on the first option that still works.
- **P0 C5** The "Print sheet" row opens H3's print, or reads "Must-know cards" until H3 lands.
- **P1 C6** The end as lines with L4's `done`; the stop sheet; the lesson's way back; Skip in the run (decision 5.4.4).

**R: production routes and the systems around Learn** (packet P. Files: `src/app/(app)/learn/**`,
`src/app/(app)/explore/run/**` only (not `explore.css`), `src/components/learn2/links.js`, `src/app/preview/**`,
`AppLayoutClient.jsx` (Learn row and focus routes); new: `src/app/(app)/cards/**`; and one named owner for the entry-point files
in R3.)
- **P0 R1** Preview truth for his look: scope "Your papers" and the dock counts to the student (`student=new` shows "8 to
  revise", E6).
- **P1 R2** Under the flag, `/cards` and `/cards/<chapter>` redirect to `/learn` and `/learn/c/<key>/cards`; `?mode=study` goes
  to the chapter page, `?mode=last` to `?f=must`.
- **P1 R3** Entry points behind the flag (LK23): Review's chapter rows, the Result's "The line you needed", Today's Revise tile
  and alternatives, the Start sheet's "Learn a chapter", Progress, Revise's end. These files belong to no packet today.
- **P1 R4** A production build check (`next build`, `next start`): flag off, the new routes answer 404 and the live pages are
  unchanged; flag on, the focus routes draw no shell.
- **P2 R5** The migration's rolled-back dry run and the staging walk (A6 9.9); then he applies it.

**App** (A7, after he approves the web): re-base the plan on B7 before T18 to T21 (section 4, item 13).

### 5.3 The verification pass (main session, before his look)
- Sizes: 360x640, 390x740, 412x915, 768x1024, 1024x768, 1366x650, 1440x900, 1920x1080. Night and Day for every state.
  Reduced motion. Keyboard only. NVDA on the feed card and a wrong answer.
- Real input: a notched wheel and a trackpad on Windows; one budget Android over the LAN.
- Recordings: the turn, Keep, Got it, the line opening and the pager, with frames at 0, 120, 260 and 420 ms.
- Content: one match-the-column, one statement, one Assertion-Reason and one 1,000-character case stem, in the feed and the run.
- Truth: the cover hook equals the feed's first card; every key's number equals what it plays; a Free returning student.
- Zero console warnings; CLS at most 0.01 on load; a 4x CPU throttle with no long task over 50 ms during a move or a turn.
- Score each screen on the 12-part test and the 0/1/2 rubric again, from these captures, not from the audits' targets.

### 5.4 Decisions to put to him (one line each)
1. Free returning feeds: show his 5 free cards again as looks once they are in Revise (recommended), or let a Free feed become
   questions only.
2. Must-know is not printed on feed and run cards, where all of them are Must-know; it stays in the Cards view (LK13; the CTO
   can take this and tell him).
3. The chapter page with and without the subject object: he picks on the live page.
4. A quiet Skip in chapter runs too; a skipped question is never a mistake.
5. After the web is approved: apply the migration (after the dry run), turn on the flags, then the app.
