# A7: Learn v2 and the Explore feed in the Android app (build plan)

Written 1 Nov 2026, about 1:50 am IST, for the main session. READ-ONLY audit: no file was edited, nothing was built, no emulator, Gradle,
dev server or browser was started, no database was touched. I ran the 71 existing node tests of the Learn engine in the web worktree (all pass:
`learn_compose`, `learn_suggest`, `learn_search`, `learn_feed`, `learn_preview`, `runMath`, `homeModel`). I did NOT run `flutter analyze` or any Flutter test,
so the green state of the base branch is not verified here (gate T01).

Code roots used below (paths are relative to them):
- App: `C:/Users/atish/Desktop/mockmob copy/wt-1031-keycards-app/flutter_app` (written `app:`).
- Web: `C:/Users/atish/Desktop/mockmob copy/wt-1031-learn-v2` (written `web:`).
- Specs: `C:/Users/atish/Desktop/mockmob copy/mockmob-next/docs/brain/learn-1031/` (written `spec:`).

---

## 0. The short version

1. **Start from `ui/1031-keycards`** (head 98c41a73e, folder `wt-1031-keycards-app`). It is the newest app work (31 Oct 12:56 pm), sits 16 commits above v16
   (pubspec 1.0.18+16), contains 131 of the 136 `ui/*` branches (the other five are older, 14 to 18 Oct, see section 1), has a clean tree and is merged nowhere. The Flutter app inside `mockmob-next`
   (`feat/app-and-web`) was last touched on 16 Oct and is stale. Cut `ui/1101-learn-app` in a new worktree from 98c41a73e.
2. **The app has no Learn v2 and no `/api/learn` client.** It has four older card systems (lessons, concept cards, Key cards, Revise), a Learn door that is a lesson library,
   Key cards home and deck screens, and the Untimed questions stream. Everything v2 needs is new UI over a new thin client. The composer, suggestions, search and feed rules stay on the
   server; the app calls the same `/api/learn` routes as the web.
3. **There are no production `/api/learn` routes.** They exist only in the dev preview (`web:src/lib/server/learnPreview.js`). The app can still be built and walked now, two ways:
   recorded fixtures (tests, goldens, the demo build), and a debug-only client that calls the dev preview's unauthenticated route
   (`/preview/arena/realdeck?_to=/api/learn/...&_plan=&_student=&_s=`), which runs the real composer on a seeded student. Reaching a real phone needs the production routes first.
4. **No navigation slot is added.** The feed gets three doors: a "Chapter feeds" row in Practise's More ways in that opens a new Explore page of covers; a feed card in Today's deck;
   and a "play it as a feed" key on the chapter page and the run end. Learn stays a door of Practice. The door order in the code is not the one in the brief (see 2.1).
5. **Build order:** data layer and demo; Learn home with the chapter page and piles; the run player with the Got it flight and the end screen; the full-screen vertical feed;
   Cards view and Find; entry points; offline cards-only runs last. Size: about 60 to 90 agent-hours, about 12 to 16 hours of wall clock with 5 or 6 parallel streams, first walkable
   slice (home, chapter, run, end on demo data) in about 5 hours. These are estimates, not measurements.
6. **Biggest risks:** no production routes; the LK15 Free rule has no server shape; a vertical scroll inside a vertical pager does not chain in Flutter; the web contract is still moving
   (the feed files changed at 1:00 and 1:10 am today); RAM on a 2 GB AVD beside a 2 GB Gradle daemon; golden churn; the chapter cover art (LK21) is open on the web; a haptic rule conflict.
7. **Decisions needed before starting** are in section 10 (13 items; five need the owner or the CTO's call: Free session rule, door order, cover art, wrong-answer haptic, feed way in).

---

## 1. Which branch the app work starts from (verified with git)

| Worktree | Branch | Last commit | Note |
|---|---|---|---|
| `wt-1031-keycards-app` | `ui/1031-keycards` | 31 Oct 12:56 pm, 98c41a73e | newest; clean; pubspec 1.0.18+16 (no bump); not merged anywhere |
| `wt-1020-v16` | `ui/1020-v16` | 21 Oct 3:38 am, f72207c27 "Version 1.0.18+16" | ancestor of the Key cards branch |
| `wt-1020-v16walk`, `-v16fixa`, `-v16-nudges`, `-v16-welcome`, `-v16-mobwelcome`, `-v16-sweep` | `ui/1020-v16-*` | 21 Oct | all ancestors (merged) |
| `wt-1020-v15app`, `wt-1020-v15walk`, `wt-v15-3`, `wt-rev-apptests`, `wt-phase2b`, `wt-w2l`, `wt-w3-*`, `wt-w4-*` | older | 16 to 20 Oct | all ancestors |
| `mockmob-next` (`feat/app-and-web`) | its `flutter_app` last changed 16 Oct (fd3fca291) | stale | v16 is not an ancestor of it or of `main` |

Checked with `git merge-base --is-ancestor` over every local `ui/*` branch: 131 of 136 are inside 98c41a73e, among them `ui/1020-v15`, `ui/1020-v16` and its `-fixa`, `-walk`, `-sweep`, `-welcome`, `-mobwelcome`, `-nudges`,
`ui/v16-1020`, `ui/phase2b-1016`, `ui/mobi-look-1016`, and the heads 72af51558 (the v17 release merge), 9e6ad500f, 2485e83ea. The five that are not: `ui/art-1016` (16 Oct), `ui/ask-insights` (14 Oct),
`ui/owner-1016` (17 Oct), `ui/phase2` (16 Oct), `ui/v15-today` (18 Oct). `git cherry` shows `ui/phase2` is present upstream by patch and the other four carry 16 commits that are not (2, 11, 2 and 1); all five are older than v16
and probably superseded by later rewrites, but that was not checked commit by commit, so none of it is "newer app work". `git diff --stat ui/1020-v16 98c41a73e -- flutter_app` is
92 files, +24,517 and -43 (most of it the 16k-line `display_parity.json` fixture); `pubspec.yaml` is unchanged, so the Key cards app has not been version-bumped or released
(`web:docs/brain/NOW.md`, 31 Oct: "App version 17 can wait for the redesign").

Recommendation: new branch `ui/1101-learn-app` from 98c41a73e, worktree `wt-1101-learn-app` (Flutter has no node_modules junction to protect). Version 17 carries Key cards and Learn v2 together
(`tool/bump_version.py`, `tool/build_release_aab.sh --bump`).

Gate before the first new commit (T01): the log holds a STOP POINT commit (9d6cc2f3d, 31 Oct 3:40 am, "owner usage 93%") that 7820a3ac8 reviewed. Run, once, through
`bash tool/flutter_locked.sh`: `analyze`, the unit folders `keycards learn practice today insights motion core_ui`, and the golden folders `keycards` and `learn`. Record the result in the branch notes.

---

## 2. Today's app, verified against the code

### 2.1 Where R5 and the brief are wrong or stale

1. **Door order.** The code is Practise | Your papers | Learn: `app:lib/features/practice/widgets/door_switch.dart:40` (`[practise, papers, if (showLearn) learn]`), enum order
   `app:lib/features/practice/model/practice_door.dart:8-11`, stage direction by enum index `app:lib/features/practice/widgets/door_stage.dart:48`. The brief and the earlier session summary say
   "Practise | Learn | Your papers"; DESIGN-SPEC A8 asks for that order. Changing it touches three files, `practice_order_test.dart` and the door goldens. The owner said the navigation stays exactly
   as it is, so this is a decision (10.6), not a free tweak.
2. **R5 problem 3 (rating keys on the gesture bar) is already fixed.** Commit 97e17ce93 (31 Oct 12:23 pm) makes `KcKeepInView` leave `MediaQuery.paddingOf(context).bottom + 16`
   (`app:lib/features/keycards/widgets/key_card_parts.dart:731-732`). What is still true: the deck page spends about 1,080 px before the first card, and a session scrolls its header away.
3. **Route names collide.** `/learn/run/:runId` and `/learn/:unitId` already belong to the lesson engine (`app:lib/core/router/router.dart:502-509`), and `ActionRouter` maps the website's
   `/study/<id>` to `/learn/run/<id>` (`app:lib/core/router/action_router.dart:197`). The v2 session needs its own path (`/learn/session`), and the website's `/learn/run?...` and
   `/explore/run?...` links need new mappings.
4. **Revise has no cards-only source.** `ReviseScreen` takes no `source` parameter (`app:lib/features/review/revise/revise_screen.dart:53`), so the web's Find shelf link `/review/revise?source=keycards`
   has no app equivalent, and Revise plays questions before Key cards (R5 problem 2).
5. **The Untimed questions stream grades on the phone.** `/api/questions/feed` sends the key and `PracticeCard` reads `question.correctKey`
   (`app:lib/features/insights/widgets/practice_card.dart:81-86`). Learn v2 grades on the server (no key before an answer), so the stream controller and card cannot carry v2 questions; only their look can be reused.
6. **`MmDragCommit` is sideways only** (`app:lib/core/motion/drag_commit.dart:114`, `MmSidewaysDragRecognizer`). It fits the Quick recap swipe, not a vertical feed.
7. **Confirmed true:** dock = Today, Practice, Mob, You with Start as the centre key (`app:lib/core/widgets/bar/bar_tabs.dart:13-18`); Learn is `PracticeDoor.learn => LearnScreen(embedded: true)`
   (`app:lib/features/practice/practice_screen.dart:575`); the Key cards row sits at `app:lib/features/learn/screens/learn_screen.dart:548`; Key cards routes `/cards` and `/cards/:chapter` at
   `app:lib/core/router/router.dart:513-514`; Study is one session of every open card with no rounds; Last look sends nothing.

### 2.2 The Learn door
- Mounted inside Practice's one `ListView`: Practice owns the title, the pull and the scroll (`practice_screen.dart:501-580`), the door switch is `PracticeDoorSwitch`, the content swaps in `PracticeDoorStage`.
- Visible only while lessons are not switched off: `_learnOpen` reads `learnCatalogProvider` (`practice_screen.dart:132-137`). v2 must key the door on its own flag, because Key cards and questions exist without lessons.
- Content today (`learn_screen.dart` `_content`, about 312-560): lede, first-visit "How Learn works", one lime "Read this next" panel (`conceptsPick`), the concept-cards row, the Key cards row, a lessons search,
  subject chips, "Where your marks slip", every chapter as `ChapterFold`, record line, "Test it in a full mock", `OfflinePacks`. This is what v2 replaces: LK3, LK9, LK11 (one fixed suggestion).
- Practice's own pull reads `learnCatalogProvider` for this door (`practice_screen.dart:149-153`); v2 needs the pull to invalidate `learnSubjectProvider` instead.

### 2.3 Key cards (what exists, what v2 reuses)
- Data layer, all reusable as is: `lib/features/keycards/data/keycards_api.dart` (review, add, report, line, due, deck, my chapters, set option), `keycards_providers.dart` (home, deck, due, line providers, `rateKeyCard`),
  `keycards_reviews.dart` (outbox: `KeyCardsOutbox.reviewKey(cardId, at)` makes a replay idempotent), `keycards_cache.dart` (kept home, decks, due queue, 48-hour reviewed map), `keycards_rules.dart` (the web's
  limits held equal by test), `keycards_lines.dart` (display rules held equal by `display_parity_test`), `keycards_models.dart` (`KeyCard.tryParse` already parses the card inside a run item).
- UI reusable: `KcBack`, `KcBlankText`, `KcReference`, `KcCardMenu` and the report sheet, `KcLockedRow`, `KcLinkAction`, `KcRatingKeys` (three equal keys), `KcStudyFace`, `KcKindLine`.
- UI replaced: `keycards_home_screen.dart` (418 lines; the Part picker is the LK2 source), `keycards_deck_screen.dart` (398; Read, Study, Last look), `KeyCardsLearnEntry`.
- `KcKindLine` draws "Must-know" as an outlined pill (`key_card_parts.dart:62-118`, `KcTag`); LK13 and DESIGN-SPEC 3.10 want the word in volt text with no box.
- Wiring: `lib/app_overrides.dart:31-40` (`liveAppOverrides({keyCards})`); every provider defaults to Off so a screen without the override draws nothing and calls nothing.

### 2.4 The question stream (the app's Explore, `/practice/stream`)
- `StreamScreen` (341 lines): header, `StreamFilterBar`, one question at a time in a `ListView` under an `AnimatedSwitcher`, a bottom bar with Previous, Next and Skip; `StreamController` pages
  `/api/questions/feed` 12 at a time with client-held keys and an `_seen` set. The way in is one plain row `StreamEntry` ("Untimed questions", `app:lib/features/insights/widgets/entry_points.dart:108-120`)
  at the end of the Practise door (`app:lib/features/practice/widgets/more_rows.dart:34`).
- Actions under a question (`QuestionActions`): Save, vote, flag, Ask why. Save is `saveControllerProvider.set(questionId, saved, source)` -> `POST /api/bookmarks` (Free 25 saves, 402 `SaveLimitReached`),
  usable by id, so the feed's Save rail can reuse it (`saved_repository.dart:90-128`).
- The app has no page called Explore; the word appears only in comments.

### 2.5 Today's swipe stack
- `app:lib/features/today/widgets/suggested_stack.dart` (2,773 lines) is "Suggested for you" under the lead card; deck logic in `logic/suggested_deck.dart` (602 lines); the cards are the choices
  `buildChoices` makes (`logic/glance_builder.dart:122`).
- Rules that bind a Learn card there: a swipe never starts a session (`SuggestedCard.swipeable`), the card waits for its key; every swipe has a visible button doing the same thing (D90); the first run teaches
  itself (`DeckCoach`), reduced motion keeps the finger-follow but swaps at once; kinds passed on often sink (`DeckMemory`).
- The physics is horizontal and uses `MmDragCommit`. The feed does not reuse it, but it must copy the D90 rule (a visible way to the next item, which is exactly what the owner missed on a PC, LK20).

### 2.6 API client and auth
- `app:lib/core/api/api_client.dart`: dio, bearer header from `ApiTokenProvider.accountToken()`, refresh once on 401 then sign out, `expectUserId` guard (nothing is sent if the account changed), typed `ApiError`,
  client-side 429 hold per route family and read or write (`_bucket`, lines 220-226: only `/api/study` and `/api/learning` share the `learning` bucket; `/api/learn/runs/*` would all fall in the bucket `api/learn/runs`),
  GET retried twice and writes never unless the caller passes `retries`, `Idempotency-Key` header supported, `_OriginGuard` refuses any origin but `API_BASE_URL` (a test build never reaches production).
- v2 writes (`answer`, `rate`, `runs`) are idempotent per item id on the server (`web:src/lib/server/learnPreview.js:531, 579`), so the app may pass `retries: 1` and an idempotency key.

### 2.7 Theme, widgets, motion, haptics, art
- Tokens: `MmColors` Night and Day (ground, raised, line, ink, ink2, ink3, volt, voltInk, accentText, wrongSurface, wrongBorder, wrongText, selectedSurface), `MmSpace` (4 scale, gutter 16), `MmRadius`, `MmTarget`
  (min 48, option 56), `MmType` roles (Bricolage display and title, Hanken body). Widgets: `KeyButton` (volt, `.secondary`, `.quiet`, `.option`), `MmSegmented<T>` (N segments, one sliding thumb, 220 ms, `showBubbles: false`),
  `MmChip`/`ChipRail`, `showMmSheet`, `StateView`, `Skeleton`, `InlineBanner` (+ `offlineStrip`), `MmSurface` (hero, plain, inset), `ReceiptLine`, `MmPageHeader` (back label and fallback route), `MmCountUp`.
- Motion: tokens come from `shared/motion-tokens.json` through `motion_tokens.g.dart` (`python tool/gen_motion_tokens.py`; "change a value there, never here"), `Motion.ui` 200 ms, `Motion.card` 240 ms, `Motion.glide`,
  `Springs.{smooth,snappy,settle,lift,release,celebrate}`, `MmStagger`/`MmEntrance`, `MmOverlapSwitcher`, `MmShake` (4 dp, 3 cycles, 220 ms, fires `warn()` unless `haptic: false`), `MmObjectReact`, `MmFlight`
  (a subject object flies between two screens), `MmFoldExit`, `MmSizeEase`. **Guard:** `test/unit/motion/motion_guard_test.dart` forbids new bare `AnimatedSwitcher(` and `Curves.ease*` outside `lib/core/motion`.
- Haptics (`lib/core/haptics/haptics.dart:111-125`): tick for selections, light for start, a flip and a primary commit, medium for a seal, `confirm()` only after a server acknowledgement, `segmentTick`, `toggle`,
  `gestureStart/End`; "Nothing on a wrong answer and nothing on errors." Precedent: the concept checks use one `MmShake` for a miss with no haptic (M4, 15 Oct).
- Art: one photo-real object per subject (29 `assets/art/obj-*.webp` files; `assets/art` is 7 MB in all), shown by `SubjectEmblem`/`ObjectEmblem`; there is no per-chapter art anywhere (LK21 has no app data to lean on).
- Unused today but available: `CardStackMark` (a pile of 1 to 3 paper cards that fans out and breathes), `RunPips` (one slim segment per step), `StepSwap` (a rated card flies off 56 dp), `FeedbackMobi`.

### 2.8 Tests, goldens, demo and walk tooling
- 795 test files, 3,222 golden PNGs. Goldens are Night and Day pairs at 360 by 780 (`test/helpers/golden_harness.dart`, `pumpMockmob`); Key cards use `kcGolden(name, build, overrides)` at 360 by 800
  (`test/golden/keycards/kc_golden_support.dart`, `MM_PREVIEW_DIR` also writes plain PNGs to look at). Counts now: learn 71 PNG, keycards 70, today 194, practice 243, insights 182.
- Gates a new feature must pass: `motion_guard_test`, `motion_tokens_test`, `haptic_grammar_test`, `a11y/guidelines_test` (48 dp targets, labels, contrast, both themes), `display_parity_test`, `keycards_rules_test`.
- Demo build: `test/device_demo/demo_main.dart` is the real app signed in as a fixture student, repositories replaced by memory fixtures, separate application id `in.mockmob.app.demo.debug`, never shipped
  (`docs/DEMO-BUILD.md`); Key cards demo data in `demo_keycards.dart` and `demo_keycards_decks.dart` (six real chapters, Free by default, `--dart-define=DEMO_PRO=true` for Pro).
- Walk tooling: `tool/emu_rec.sh` (functions `t`, `sw`, `back`, `shot`, `tapd "label regex"`, `labels`, `rec_start`, `rec_stop`), `tool/frame_sheet.py` (frame grids from a clip), `tool/android_env.sh`,
  `tool/flutter_locked.sh` (at most 2 heavy Flutter commands at once on this PC). Last walk: `tmp/walk-1031/app/*.png` (names like `14b-study-revealed-night-pro.png`, variants night, day, pro, free, font2, offline).
  AVD `mockmob_budget`: 720 by 1600, 300 dpi, 2048 MB RAM, Android 34 Google Play x86_64.

---

## 3. What the app must match (the web feature as it stands)

- The de facto contract is what `web:src/lib/server/learnPreview.js:827-843` answers, not only `spec:API-CONTRACT.md`. Fields the written contract lacks and the app needs: `GET /api/learn/covers`;
  `rate` with `{keep:true}`; `402 {error:'FREE_FEED_USED', reason:'learn_feed', line}`; `runs` response `resumed`, `added`, `looks`; item `look`, `recap`; answer `fixedText`, `line.collapsed`,
  `line.locked/text`, `reinsert.item`; preview `piles[].minutesLabel/of`, `coach`, `realMinutes`, `shrink.addNext.label`, `added`, `shelf`; end `feed {title, kept, lines, lead, free, next}`, `numbers.detail`;
  cards `counts.total`, `lockedCount`; shelves `due.all/subjects`, `missed.days`; request `addNext:true` and `resume`.
- The behaviours are in `spec:DESIGN-SPEC.md` (B plus A1 to A12), `spec:design/B-chapters.md` (sections 3.1 to 3.10, 4.6, 5, 6), and `web:docs/brain/learn-1031/FEED-2.md`.
- **Still moving:** the web feed was edited today at 1:00 am (`ChapterFeed.jsx`) and 1:10 am (`feed.css`) and `ExploreCovers.jsx` at 12:47 am, uncommitted, after the owner's 1:25 am look (LK20 no way to the next item,
  too much blank space; LK21 every Accountancy cover shows the same object). The app should copy the refined feed after the main session's refinement spec, not FEED-2 as first written (T19 freezes there).

---

## 4. Screen-by-screen build plan

New code lives in `lib/features/learn2/` (mirrors `web:src/components/learn2/`): `data/`, `models/`, `screens/`, `widgets/`, `feed/`. Legacy Learn and Key cards screens stay behind the server flag until the owner approves (T29).
Every screen: Night and Day, 360 dp first and 412 dp checked, text scale 1.0 and 1.3, reduced motion, offline where the data allows, 48 dp targets, sentence case, no middle dots, 12-hour times,
no "mastered", no mastery percent, no "marks to recover", no exclamation marks, no arrows on keys, no new bare `AnimatedSwitcher` and no `Curves.ease*` (use `MmOverlapSwitcher` and `Motion`).

### 4.1 Learn home (replaces the content of `PracticeDoor.learn`)
- **Reuse:** `SubjectTiles` (add a compact variant so the first screen still shows the lead suggestion, two small ones and the map's first heading; today's tile is 132 dp), `subjectChoices`, `practiceSubjectProvider`
  (the Learn and Practice subject is one shared state, B 3.2; map ids with `canonicalSubject`), `LearnSearchField` (new hint "Search 868 Key cards", FEED-2 section 7), `HowConcepts` (first-visit line rewritten:
  "Pick a chapter, pick a time. Your cards and questions are lined up.", hides after the first chapter opens), `KcStateLine` (state ring and word), `OfflinePacks`, `MmStagger`, `StateView`, `InlineBanner.offlineStrip`.
- **New:** `LearnHome` (embedded; Practice keeps the title, pull and scroll), heading with one true counts line, `LearnSuggestions`, `LearnChapterMap`, `LearnFindPanel` (4.5), foot row ("Study plan" sheet from
  `StudyLength`/`/api/study/preferences`, "On this phone", "Your record").
- **Suggestions:** always three of three different kinds from the server; the lead is larger with the subject object and the page's one volt key; the other two are compact rows with outlined keys; every key starts at once
  (a `run` posts to `/api/learn/runs`; the one `href` a suggestion sends is `/learn/find?subject=`, which focuses the search field). Evidence line under each. The 390 dp crush in CRITIQUE-1 (item 7 of the first eight:
  four-line titles, two-line keys) is the thing to check first.
- **Chapter map:** parts with pinned headings (`SliverPersistentHeader`), unit headings only when they say something (`unitHeading`), rows of at least 64 dp (title up to two lines, ref, state ring and word, card count,
  one meta line from the server), press scale 0.985 with a selection haptic, rows keyed by `chapter.key`. Sort menu "Book order | Marks open" (`marksOpen` from the server, else the existing `learnChapterCostsProvider`).
  No separate chapter filter: the one search field covers chapters, lessons and cards (it replaces the old Chapters | Find toggle).
- **Part switch (LK2, the shuffle bug):** a two-way `MmSegmented(showBubbles: false)` at the option unit. The tapped side stays chosen at once and is held locally until the server body agrees; the hint line has a fixed height
  and doubles as "Saving your choice"; only the option unit below cross-fades (out 160 ms, in 220 ms inside a 240 ms height ease, `MmOverlapSwitcher.fade` and `MmSizeEase`); nothing above moves and nothing re-sorts;
  `PUT /api/me/subject-options` is the existing `KeyCardsApi.setOption`; a refetch keeps the previous body on screen; a failed save slides the thumb back with "Your choice was not saved. Try again."
- **Free line:** the server sends `freeNote` ("Free opens 5 cards in every chapter. Pro opens all 868."). The product rule says Free limits show only at the real limit, so default to not showing it here and show the
  true line where it bites (chapter page, locked row). Decision 10.12.
- **States:** skeleton at the final heights (no layout shift), error ("Learn did not load", "Check your connection and try again. Your cards and their schedule are safe."), offline strip with kept data and "As of 9:40 pm"
  (rows for kept chapters bright, others dimmed with "Needs a connection"), new student set of suggestions, thin subject (English note), a chapter with no cards ("No Key cards yet. Questions ready."), lessons or Key cards off
  (server data decides what rows say), 404 `LEARN_OFF` falls back to the legacy door.
- **Data:** `GET /api/learn/subject`, `/api/learn/shelves`, `/api/learn/search`.
- **Motion:** door entrance as today (`MmStagger` 0 to 4); map rows rise 6 dp, 24 ms stagger, first 12 only, once per visit.

### 4.2 Chapter page (`/learn/c/:chapterKey`, root page, no dock)
- **Reuse:** `MmPageHeader` (back label "Learn", fallback `learnDoor`), `MmSegmented` for the length, `showMmSheet` for "Your own", `KcStateLine`, `SubjectEmblem`, `KeyButton`, `MmShake`, `MmCountUp`, `StateView`, `Skeleton`,
  `keyCardsMyChaptersProvider` (Pro reason line), `StudyLength` for the default minutes (10, 20 or 30 on the account), `LearnPaths.practiseChapter` for the Questions row.
- **New:** `ChapterPage`, `LearnPiles` (T10), `OwnLengthSheet` (presets 30 min, 45 min, 1 hour, then a 5-minute stepper to 120), `ShelfRows`, `usePreview`-style provider.
- **Layout (390):** back, unit or part line, title (type.title), ref and state, then "How long have you got?" with `5 min | 10 min | 20 min | Your own`, then the piles, the volt "Start 10 minutes" (always names the length),
  one quiet line ("Ratings join Revise. Questions are free."), the secondary text key "Or a quick recap: the 12 Must-know lines, about 3 min", then the shelf "In this chapter": Key cards, Questions, Your mistakes, Lesson, Print sheet.
  Add a quiet "Play it as a feed" text key under Start (decision 10.4).
- **Piles (DESIGN-SPEC A1):** up to four, each three paper cards fanned (-4, 0, 3 degrees) painted with a `CustomPainter` in the card surface and a 1 dp hairline (extend `CardStackMark`), the count in tabular
  numerals, the label, the minutes. Tapping a pile leaves it out: it dims to 35%, reads "Left out", the others re-balance from a new preview; the last pile cannot be left out and shakes 4 dp once
  (`MmShake(haptic:false)`); first-visit coach line "Tap a pile to leave it out."; counts roll in 180 ms, the fan re-spreads in 220 ms; a dashed "Next chapter" pile when the chapter runs short (`shrink.addNext`).
- **Data:** `POST /api/learn/runs/preview` on every change, debounced about 120 ms, a stale answer dropped, the previous numbers kept on screen while a new one loads, the whole main column drawn at its real sizes
  before the first answer. The last length is kept on the phone (`learn2_minutes`).
- **States:** new student ("Not started", first-visit note), returning, Free (honest taste sentence and the ratings-used line), honest shrink ("This chapter has enough for about 12 minutes today", Start names 12),
  no cards, no questions, loading, error with the shelf rows still open, offline ("Cards only" chosen, other chips disabled, "Questions need a connection").

### 4.3 Run player (`/learn/session`, then `/learn/session/:runId`; root page, no dock)
- **Reuse:** `KcBack`, `KcBlankText`, `KcKindLine`, `KcReference`, `KcCardMenu` (report), `KcRatingKeys`, `KcLockedRow`, `RunPips` (extend to grouped pips), `FeedbackMobi`/`MobiRation`, `MmDragCommit` (Quick recap swipe),
  `MmOverlapSwitcher`, `SemanticsService.sendAnnouncement` (as `KeyCardRun` does), option-tile styling from `PracticeCard._OptionTile` (extract a public `LearnOptionTile`), `Haptics.confirm/tick/light`.
- **New:** `SessionScreen`, `LearnRunController` (T11), `TopLine`, `CardTurn`, `QuestionTurn`, `LessonTurn`, `RevisePile`, `StampLine`, `CoachLine`, `RoundBreak`, `RunEnd`, `MmFlyTo` (core/motion, an arc flight overlay that
  measures two global rects) and `run_math.dart`.
- **Top line:** Close (48 dp, asks nothing, every answer is already saved), chapter title, "7 of 20", pips grouped by kind that count only finished items, "about 6 min left" (`minutesLeftLine`).
- **Pinned rating bar:** a bottom bar with the bottom inset, never auto-scroll (the legacy deck scrolled its header away). Missed, Got it, Easy are three equal grey keys; the tapped key inks volt with a spinner; the card leaves only after
  the server acknowledged. Failure line "That rating was not saved. Try again."
- **Card turn:** kind line, stage tag ("Due today", "Back from earlier"; none in a recap), front, "Show answer" (volt), reveal (dashed rule draws 160 ms, answer rises 8 dp and fades 220 ms, front dims), then the three keys.
- **Got it, Easy, Missed (DESIGN-SPEC A4, CRITIQUE R1):** lift 4 dp and scale 0.96 (100 ms), then fly along a gentle arc into the Revise pile while shrinking to about 0.18 and fading (320 ms,
  `Cubic(0.32, 0.72, 0, 1)`), the next card rises 8 dp starting at about 220 ms so there is no empty frame, the pile count pops to 1.12 (180 ms), a stamp line centred under the keys reads the server's real day
  ("Back Tue", "Back in 12 days") for about 900 ms. Easy is the same at 280 ms. Missed tilts -3 degrees and slides down behind the deck edge (260 ms), stamp "Back later in this run". Haptics: `confirm()` for Got it and Easy
  after the acknowledgement, `tick()` for Missed. The pile sits at the bottom right beside or just above the keys, never in a screen corner. Reduced motion: cross-fade 120 ms, the stamp as text for 1.5 s.
  A tap during the flight is ignored, not queued.
- **Question turn:** head ("Question" or the server's `mistake.label`), the stem through `stemParts` (a long stem with inline steps splits into lead, steps and ask; CRITIQUE R2), four rows of at least 56 dp,
  the first tap locks the options and shows a pending state, the server grades (`answer`), right = selected surface, ink border, check, settle 1.04 in 200 ms; wrong = `MmShake(size: 4, haptic: false)`, wrong colours, the key row marked;
  then the explanation (first line, "More"), `fixedText` for an open mistake answered right ("Fixed. You missed this in Mock 3 on 16 Oct." with the line collapsed under "See the line"), the line you needed
  (`KcBack(compact)` with its reference; inside a run it does not spend Free's 3 lines a day; a locked card shows the Pro line once per run), "This card comes back later in this run." with `reinsert.item` placed at `at`.
  Failure: "Your answer did not reach us. Try again." keeping the pick; retry resends the same item id.
- **Free looks:** an item with `look: true` shows one "Next" key and the server's one line; the look is logged with `rate(rating:3)` fire and forget (the web does the same).
- **Lesson turn:** open the existing lesson route (`AppRoutes.learnUnit`), mark the item read with `rate` on return.
- **Kinds:** `recap` (answers showing, one at a time, Previous and Next, horizontal drag through `MmDragCommit`, "Nothing here is scheduled", end "That was every Must-know card."), `cards` (Study in rounds of 20 with a
  round break "Round 1 done" and "Next round" or "Finish here"), `level` (six questions).
- **End:** title ("10 minutes on ..."), three numbers that count up (400 ms, 60 ms apart) with one detail line each, the result lines, the Revise pile fanned with grouped return days ("6 back on Tue, 3 back on Fri"),
  `moved` ("moved from Getting there to Holding"), Free's line with a text "See Pro" (no modal), Mobi once matched to the result (`endAct` port, respects `MobiRation` and the Celebrations setting),
  the volt lead key and three options, each a new run or a mapped route. The server's `href` values need a map in the app: `/review/revise?source=keycards` ("Revise N due cards") has no app target (2.1 item 4), so until
  Revise gets a cards-only source it becomes a `kind:'cards'` run seeded from `GET /api/keycards/due`; `/test?subject=&count=50&mode=full` ("Test it in a full mock") goes to `TodayLinks.fullMock`; `/learn/find` focuses the search field.
- **Coach lines (A11):** first card "Say the answer in your head, then show it.", first rating "Got it sends the card to Revise. It comes back when it is due.", first wrong answer "Here is the NCERT line you needed.",
  piles "Tap a pile to leave it out."; each once, kept in `learn2_coach_v1`.
- **Leaving:** close and the back gesture leave at once (`PopScope`), the run stays resumable 24 hours (`POST /api/learn/runs {resume}` after a process death; the route carries the run id once it exists).
- **Offline:** a rating that cannot reach the server falls back to the Key cards outbox (`rateKeyCard`, mode `study`, `clientReviewedAt`) with a local re-insert of a Missed card and "Saved on this phone" at the end;
  an answer says it needs a connection.

### 4.4 Key cards view (the new Read and Last look; `/learn/c/:chapterKey/cards[?f=must|revise|missed]`)
- **Reuse:** `KcReadCard` pieces, `KcBack`, `KcReference`, `KcCardMenu`, `KcLockedRow`, `ChipRail`, `MmSwitch`, `MmSizeEase`, `showMmSheet`, `KeyCardsApi.add`.
- **New:** `CardsView`, `CardSectionList` (`CustomScrollView` with a pinned `SliverPersistentHeader` per NCERT section and its count), `CardRow`, `PickBar`, `SectionJumpSheet`.
- Filters All, Must-know, In Revise, Missed lately with real counts (one sliding indicator, a phone row that scrolls sideways); tools row "Show answers" (folded by default), Sections (jump sheet), Pick (long press, plus a visible key for TalkBack);
  rows show the kind line (Must-know as a volt word, an In Revise dot, Missed lately), the front, the NCERT line folded behind "Show" and clipped to two lines; a row opens in place (240 ms spring) to the full line, source,
  "In short" and its actions (Study this card, Add to Revise for Pro, Report); one volt key at a time: with a filter "Quick recap these 12" (answers showing, nothing scheduled) beside "Study these 12"; with none "Study these 46".
  Pick mode bottom bar "8 picked, Study these 8, Add to Revise, Clear" starts a `cardIds` run. Free: open cards whole, one locked row with the server's `lockedLine`, filter counts say "open".
- Filter locally from one `GET /api/learn/cards?chapter=` read (each card carries `inRevise` and `missedLately`); counts come from the server.

### 4.5 Find (inside Learn home, not a toggle)
- Focusing the search field opens Find in place; Cancel returns to the chapters. Before typing: four shelves as paper piles with the real counts (Due today, Missed lately, In Revise, Must-know) and "By chapter".
  After two characters: results for chapters, lessons and cards with the matched words underlined from the server's `match` spans, one honest header ("27 cards in 1 chapter"), locked cards as stubs (`locked: true`),
  answers folded (a card whose match is only in NCERT's words shows that line). Pick mode as in 4.4.
- **API gap:** the web builds a shelf's set by reading each chapter's cards (14 to 17 calls, `web:src/components/learn2/cards/FindView.jsx:39-46`). The app should not. Ask for one `GET /api/learn/cards?subject=&set=due|missed|revise|must`
  grouped by chapter. Until it exists, "Revise these" starts a `kind:'cards'` run seeded by `GET /api/keycards/due?limit=` (exists).

### 4.6 Explore: covers page and the full-screen vertical feed
**Way in (no nav slot):** one row "Chapter feeds" ("Cards and questions, one at a time.") above "Untimed questions" in Practise's More ways in (`more_rows.dart`), opening a new `ExploreScreen` at `/explore`
(root page, back to Practice); a feed card in Today's deck; "Play it as a feed" on the chapter page and the run end; ActionRouter maps the website's `/explore` (no filters) to this page and keeps
filtered `/explore` links on the stream. "Untimed questions" stays exactly as it is (LK15: unlimited). Alternative considered: a covers shelf on Learn home under the suggestions (more visible, but it crowds the first screen, LK11).

**Explore page:** header "Explore", the `5 | 10 | 20 min` control (applies to every cover), the subject chips (shared subject state), Free's note when the day's feed is used, a snap row of covers
(`PageView`, viewport fraction about 0.78): the chapter art (decision 10.5), "For you" and its reason on the first ("3 due, 2 open mistakes"), the real title at 22 sp, the line from `covers[].counts[length]`
("10 minutes, 16 Key cards and 5 questions"), a Play key (volt only on the snapped cover, so there is one volt key in view); under the row a quiet link "Untimed questions". Data: `GET /api/learn/covers`.

**Feed screen (`/explore/feed?chapter=&min=`, root page, no bar):**
- Structure: `Scaffold` ground, a vertical `PageView.builder` (one slot per item, a checkpoint slot after every 8 items, an end slot), a top overlay with the segmented ticks (2 dp, 3 dp gaps; done = ink2,
  current fills volt left to right in 600 ms, later = hairline), a 48 dp close, the real chapter title right-aligned (13 sp, one line), and the streak chip lane.
- Backdrop: the subject object at 18% and blurred 6 px, bottom right, bleeding off the edge, drifting up 8 dp in 600 ms as the page becomes active, mounted only for the active page and its neighbours. Do not blur at run time:
  bake soft variants (about 220 px, 18% opacity) with a tool script next to `tool/convert_art.py`, so a 3 GB phone pays nothing per frame.
- Anchor content to the top and let the card fit its content (ui-ux-standards section 3: no dead bands). A short front must not sit in a tall empty card; this is the owner's "too much blank space" (LK20, LK22).
- A visible Next key (D90, LK20): a small key at the foot of the rail plus TalkBack scroll and custom actions; FEED-2 as written has only the hint "Swipe up for the next one". Free paging, no gating, "Rate it first" is gone.
- **Key card page:** kind line (Must-know as a volt word), the front at about 30 sp, tap anywhere flips (`MmFlip`: rotateY, 420 ms, `Cubic(0.32,0.72,0,1)`, faces swap at 90 degrees; reduced motion cross-fades 120 ms; `light()` haptic),
  the back shows NCERT's line through `KcBack` and the source through `KcReference`. Right rail at about two thirds down: Keep (bookmark glyph fills volt with a 1.15 pop in 180 ms, a 72 by 96 ghost of the card flies to the rail's foot
  in 320 ms, label "Kept", stamp "Back Tue", `confirm()` after the server says 200) and Chapter. Free: Keep works within the day's new-card allowance; after a 402 the label reads "Pro" and taps open the Pro sheet
  (`ProReason.keycards`). Only the very first card of a student's first feed shows "Tap to turn it over". A swipe past a card without Keep schedules nothing.
- **Question page:** head ("Question" or the mistake label), stem at 22 sp (long stems through `stemParts`, folded like `PracticeCard._Passage` with "Read all" so the page never needs its own scroll), four rows of at least 56 dp,
  server-graded. Right: the row fills volt with ink text and settles 1.04 over 200 ms, `confirm()`, the streak chip "4 in a row" from 3 right answers, counting up in place, no confetti. Wrong: `MmShake(size: 4, haptic: false)` twice
  (240 ms), the row turns the wrong colour, the right row outlines volt, and a bottom sheet rises in 280 ms titled "The line you needed" with the NCERT line and source (or "The answer is B", or the locked line with "See Pro").
  Rail: Save (`saveControllerProvider.set`, 402 shows "Pro") and Chapter. "Swipe up for the next one" fades in after 600 ms the first time only.
  (`MmShake` fixes 3 cycles in 220 ms, FEED-2 says twice in 240 ms: add a `cycles` parameter, or accept three; S.)
- **Checkpoint** every 8 items, the one interstitial: a large tabular number (`checkpointNumber`: "5 of 6 right" or "6 cards seen, 2 kept"), the line, keys "Keep going" (volt) and "Stop here" (cuts the feed to that point and shows the end). It moves on only by a swipe or a key.
- **End:** title, the kept pile fanned (up to four small cards, count, the real return day), "Questions: 5 of 6 right", "Fixed: 1 old mistake", keys "Another 10 minutes" (volt), "Next chapter: ...", "Back to Explore"; Free's second feed shows
  the server's line and a text "See Pro", no modal (LK15). Data: `GET /api/learn/runs/:id/end` `.feed`.
- **States:** skeleton at final shape, Free used (402 `FREE_FEED_USED`: "One feed a day on Free" with the line, "Open the chapter", "Back to Explore"), error ("The feed did not start", Try again),
  empty ("Nothing to play in this chapter yet."), offline ("The feed needs a connection").
- **Accessibility:** each page is a labelled node "Card 3 of 21", live announcements, custom actions (Turn over, Keep, Next), 48 dp targets, large text 1.3 without clipping.
- **Nested scroll caveat (R03):** a vertical scroll inside a vertical `PageView` does not hand its drag to the pager in Flutter. The pages therefore never scroll: long stems fold, a long NCERT back face scrolls only if a
  spike (T20) proves an overscroll hand-off (`OverscrollNotification` to the page controller) works on the AVD.

### 4.7 Entry points (no new slots)
- Practice doors: reorder only if decision 10.6 says so (`practice_door.dart`, `door_switch.dart`, `door_stage.dart`, `practice_order_test`, goldens).
- Practise More ways in: add "Chapter feeds" above "Untimed questions" (`more_rows.dart`).
- Start sheet: one row "Learn a chapter" in the `modes` list beside Quick 10 (`app:lib/core/router/quick_start.dart:633`; the app's sheet has no By chapter or Smart row to sit between, so the row goes after Quick 10 and before the
  Full mock and NTA pair). Opens Learn home on the current subject, or the chapter page if the student was in a chapter in the last 7 days.
- Today: one Learn move and one feed card in the Suggested deck (`glance_builder.dart` `buildChoices`, `suggested_deck.dart` `SuggestedCard`, `TodayLinks`); Learn data reaches Today through one cached `learnSubjectProvider` read.
  A card whose action starts a session already waits for its key (`swipeable`).
- Review: chapter rows say "Learn this chapter, 10 minutes" (replaces "Key cards for <chapter>": `KeyCardsChapterLink`, `app:lib/features/keycards/widgets/keycards_entries.dart:43`, used at
  `app:lib/features/review/widgets/chapter_mistakes.dart:171`; R5 quoted other line numbers for this file, which is only 83 lines long);
  "The line you needed" gains a quiet "Open <chapter>" link (`line_you_needed.dart`).
- Router: `/cards` redirects to `/practice?door=learn&subject=`; `/cards/:key` to `/learn/c/:key/cards`; `?mode=study` to the chapter page with Cards only chosen; `?mode=last-look` to `/cards?f=must`;
  `ActionRouter` maps `/learn/c/<key>`, `/learn/c/<key>/cards`, `/learn/run?...` (to `/learn/session`), `/explore/run?...` (to `/explore/feed`) and keeps `/study/<id>` on the lesson run.
  The manifest already lists `/learn` and `/explore` as App Links; `/cards` is not listed and need not be.

---

## 5. Reuse and new, file by file, with effort (S under 1 hour, M 2 to 4 hours, L over 4 hours of one agent)

| File or area | Action | Effort |
|---|---|---|
| `core/api/api_client.dart` | one line: put `/api/learn` in a bucket of its own (or the `learning` one) | S |
| `learn2/data/learn_models.dart` | new: subject (parts, units, rows, option), suggestion, preview (piles, shrink, recap, shelf), run and items (sealed card, question, lesson), answer, rate, end (+ feed block), cards, shelves, search (spans), covers; reuse `KeyCard.tryParse` | M |
| `learn2/data/learn_api.dart` | new: interface, `HttpLearnApi`, `OffLearnApi`, errors `LearnOff`, `LearnProRequired(reason, line)` | M |
| `learn2/data/learn_providers.dart` | new: `learnV2OnProvider`, `learnSubjectProvider.family` (keeps previous data), preview, shelves, search, covers, kept copy | M |
| `app_overrides.dart` | wire `HttpLearnApi` next to the Key cards override | S |
| `learn2/data/run_controller.dart` | new: start or resume, items with re-insert, answer, rate, keep, end, Free looks and limit, offline fallback, coach flags, stale taps ignored | L |
| `learn2/data/run_math.dart`, `home_model.dart`, `feed_rules.dart` | new Dart ports of `runMath.js`, `homeModel.mjs`, `data/learn/feed.js` (slots, checkpoint number, cover line) with JSON parity fixtures | M |
| `learn2/data/learn2_prefs.dart` | new: last minutes, coach flags, feed hints, how-seen | S |
| `learn2/screens/learn_home.dart` + widgets | new (4.1) | L |
| `learn2/screens/chapter_page.dart` + `learn_piles.dart` | new (4.2); piles are the signature object | L + L |
| `learn2/screens/session_screen.dart`, `run_end.dart`, turns, `revise_pile.dart` | new (4.3) | L + M |
| `core/motion/fly_to.dart`, `flip.dart` | new: arc flight overlay, 3D flip with reduced-motion fallback | M |
| `learn2/screens/cards_view.dart`, `find_panel.dart` | new (4.4, 4.5) | M + M |
| `learn2/data/sheet_pdf.dart` | new: watermarked PDF and share (LK6); needs a dependency (decision 10.9) | M |
| `learn2/screens/explore_screen.dart`, `feed/*` | new (4.6) | M + L + M + M |
| `practice/widgets/more_rows.dart`, `core/router/quick_start.dart`, `today/logic/glance_builder.dart`, `suggested_deck.dart`, `copy_suggested.dart`, `review/widgets/chapter_mistakes.dart`, `keycards/widgets/line_you_needed.dart`, `keycards_entries.dart` | modify (4.7) | M together |
| `practice/model/practice_door.dart`, `door_switch.dart`, `door_stage.dart` | reorder only if 10.6 says so | S |
| `core/router/routes.dart`, `router.dart`, `action_router.dart` | new routes, legacy redirects, mappings | S |
| `keycards/widgets/key_card_parts.dart` (`KcKindLine`) | Must-know as a volt word, no box (LK13); regenerate all Key cards goldens | S |
| `pro_nudge/copy.dart` | add `ProReason.learnFeed` and its sheet head | S |
| `shared/motion-tokens.json`, `motion_tokens.g.dart` | add the run and feed numbers and `Cubic(0.32,0.72,0,1)`; run `tool/gen_motion_tokens.py`; `motion_tokens_test` | S |
| `pubspec.yaml` | `pdf` (pure Dart) if on-device PDF is chosen | S |
| `tool/` | `bake_soft_objects.py` (feed backdrops), `walk_learn2.sh` | S + M |
| `test/device_demo/demo_learn.dart`, `test/fixtures/learn/*.json` | new: stateful fake `LearnApi` over recorded web responses, debug-only `PreviewLearnApi`, demo flags (`DEMO_PRO`, `DEMO_NEW`) | M |
| `learn2/data/offline_composer.dart`, `learn_cache.dart` | new (later): cards-only run from kept decks with a parity test | L |
| Legacy: `learn_screen.dart` content, `keycards_home_screen.dart`, `keycards_deck_screen.dart` | keep behind the flag, delete after approval | S |

---

## 6. API routes the app needs (the same `/api/learn` routes)

| Route | Used by | Today | App notes |
|---|---|---|---|
| `GET /api/learn/subject?subject=` | Learn home, Today, Start | dev preview only | 404 `LEARN_OFF` falls back to the legacy door; `subjects` feeds the row; `parts[].option` feeds the part switch |
| `POST /api/learn/runs/preview` | chapter page | dev preview only | debounce, drop stale, keep previous; `addNext` |
| `POST /api/learn/runs` | start, resume, feed | dev preview only | kinds `mix`, `cards`, `recap`, `feed`, `level`; `resume`; `cardIds` up to 100; 402 `FREE_FEED_USED` |
| `POST /api/learn/runs/:id/answer` | run, feed | dev preview only | no key before an answer; idempotent per item id |
| `POST /api/learn/runs/:id/rate` | run, feed Keep | dev preview only | `{rating}` or `{keep:true}`; `look`, `reinsert`, `limit`, `stamp` |
| `GET /api/learn/runs/:id/end` | end, feed end | dev preview only | `feed` block for kind feed |
| `GET /api/learn/cards?chapter=&filter=` | Cards view | dev preview only | needs a sibling `subject=&set=` (4.5) |
| `GET /api/learn/shelves?subject=` | Find | dev preview only | counts only |
| `GET /api/learn/search?subject=&q=` | Find | dev preview only | spans per field |
| `GET /api/learn/covers?subject=` | Explore | dev preview only; missing from `API-CONTRACT.md` | counts for 5, 10, 20 |

Unchanged routes the app keeps using: `/api/keycards/review` (outbox, `clientReviewedAt`), `/add`, `/report`, `/line`, `/due`, `/deck` (kept decks), `/api/me/subject-options`, `/api/me/chapters`,
`/api/bookmarks` (feed Save), `/api/study/*` (lessons), `/api/study/preferences`, `/api/questions/feed` and `/interact` (Untimed questions).

What production must provide for the app (ask the web track): the same bearer `auth(request)` and a `learnHttp` wrapper modelled on `web:src/lib/server/keycardsHttp.js` (flag, 401, rate limit, body cap), with the body cap
raised from 4,000 characters (100 card ids do not fit); idempotency (`Idempotency-Key` or `requestKey`) on `runs`, `answer` and `rate`; `clientReviewedAt` accepted on `rate` for offline replays; `resume` documented;
the LK15 shape (10.3); a sheet-code route for the PDF footer (`print_sheets`, B 4.6 item 8); the missing contract fields in section 3 written into `API-CONTRACT.md`.

---

## 7. Order, streams and estimate

Slices (each ends with goldens opened and an emulator walk):
- **S0 foundation (about 2 hours, blocks the rest):** T01 to T05. The main session writes the Dart interfaces first so streams can start against them.
- **S1 home, chapter, piles:** T06 to T10.
- **S2 run, flights, end:** T11 to T14 (T11 first; the feed reuses its controller).
- **S3 Cards view, Find, PDF:** T15 to T17.
- **S4 Explore and the feed:** T18 to T21, then entry points T22 and T23.
- **S5 offline, release, polish:** T24, T26 to T29. T25 (tests and goldens) runs through every slice, owned by stream G.

Streams (one agent each, Sonnet by default, Opus only for the piles, the flights and the feed's feel):
A foundation and demo; B home, Find, entry points; C chapter page and piles; D run controller, player, flights, end; E Cards view, PDF, Review and line links; F Explore and the feed; G tests, goldens, walk (continuous).
One integrator owns `router.dart`, `routes.dart`, copy files, `app_overrides.dart` and the golden regeneration (PNG conflicts are painful); streams commit only inside `learn2/` and their own tests.

Estimate: about 60 to 90 agent-hours. Critical path: contract freeze, then T02, T11, T12/T13, T19 to T21. About 12 to 16 hours of wall clock with 6 parallel streams including two refinement rounds; the first walkable slice in about 5 hours;
the feed walkable in about 8 hours. Pace waves against the usage window (about 1% a minute at 6 to 9 agents).

---

## 8. Test plan

**Unit and widget (`test/unit/learn2/`):**
- Models and API against recorded web responses (`test/fixtures/learn/*.json`, header names the web commit); `OffLearnApi`; error mapping (`LEARN_OFF`, `FREE_FEED_USED`, 402 reasons).
- Parity tests (JSON generated from the web modules by a node script on `web/1031-learn-v2`, committed into the app branch, like `display_parity.json`): `run_math` (itemSeconds, minutesLeftLine, upNextLine, pipGroups, reinsertAt, stemParts,
  optionText, firstLine, endAct), `home_model` (subjectLine, metaLine, unitHeading, state shapes, option units, marks-open sort), `feed_rules` (feedSlots, checkpointNumber, coverLine), the offline cards-only composer.
- `LearnRunController`: answer replay is idempotent, a Missed card re-inserts once at least 3 items later, a linked question lands 3 to 6 items after its card, Free looks and the limit line, a tap during a flight is ignored,
  close and resume, offline fallback to the outbox, no success shown before the acknowledgement.
- Regression for LK2: the tapped part stays chosen through save and re-read, rows keyed by chapter key, no reorder, failure slides back.
- Piles: leave out, the last pile shakes and stays, counts follow the preview, large text; length control; Free and shrink sentences.
- Feed: pager swipe and Next key, checkpoint after 8 items, Stop here, flip, Keep (pop, ghost, "Kept", 402 shows "Pro"), right and wrong states, streak chip from 3, Free used screen, end screen, the first-run hints once.
- Copy lint: no "mastered", "mastery", mastery percent, "marks to recover", middle dots, exclamation marks, 24-hour times in `learn2` strings.
- Gates that must stay green: `motion_guard_test`, `motion_tokens_test`, `haptic_grammar_test`, `a11y/guidelines_test` extended to the new screens (48 dp, labels, contrast, both themes), `keycards_*`, `display_parity_test`,
  `action_router_test`, `practice_order_test`, `quick_start_sheet_test`, `suggested_stack_test`, `today_builder_test`.

**Goldens to add (`test/golden/learn2/`, Night and Day, 360 by 800, about 60 names, about 120 PNGs):**
1. Home: returning Pro, new Free, Find shelves, Find results, offline, skeleton, error, part switch before and after.
2. Chapter: 10 min, 20 min with the lesson pile, Free, a pile left out, short chapter with the next-chapter pile, offline, loading.
3. Run: card front, revealed, Got it flight at mid-frame, Missed, question, wrong with the line, Fixed, recap, Free look, round break, lesson, end, end Free.
4. Cards view: all, Must-know filter, one row open, pick mode, Free locked row, empty filter.
5. Feed: Explore covers, card front, back, Kept, question, right, wrong with the sheet, checkpoint, end, Free used, loading, error.
6. Entry points: Practise more rows, Start sheet row, Today deck with the Learn and feed cards, Review link, line you needed link.
Also at 412 dp and at text scale 1.3 for home, chapter, the question turn and the feed question.

**Goldens to update:** `golden/keycards/*` (the Must-know word, 70 PNGs) and `golden/learn/*` (the door replaced; lesson, run and done goldens stay), `golden/practice/*` (More rows, door order if changed), the Start sheet, Today deck.

**Emulator walk (the owner judges app work only from this):** demo build (`demo_main.dart`) on AVD `mockmob_budget`, screenshots plus short recordings through `tool/emu_rec.sh`, named like the last walk.
Scripts: `tool/walk_learn2.sh` (new) sources `emu_rec.sh`. Matrix: Night and Day; Pro and Free; new and returning; font scale 1.0 and 1.3 (`font2`); offline (airplane mode); reduced motion (`adb shell settings put global animator_duration_scale 0`).
Scenes: Learn home, a part switch, Find, chapter 5 and 20 minutes with a pile left out, a 10-minute run from the first card to the end with a wrong answer and a retried mistake, a Quick recap, Cards view with a pick, Explore covers,
a feed through a flip, Keep, a wrong answer sheet, the checkpoint and the end, Free's second feed, Back from each (gesture and key), a rotation of the app between cards (process resume). Motion frames: the Got it flight at 0, 120, 260 and
420 ms and the flip, from a recording through `tool/frame_sheet.py`. Per ledger item (LK1 to LK23) report the screenshot, not "tests pass". Real taps through `adb`, no `ensureVisible` shortcuts.
The owner sees the walk as recordings and stills; his phone only when he says it is connected, with the demo build (separate id) removed afterwards.

---

## 9. Risks

Severity and the exact fix for each are in section 12. In short:
- **R01 no production routes** (release blocker, not a build blocker): the routes exist only in the dev preview.
- **R02 LK15 undefined:** no server shape, counting rule or clamp for Free's one session a day; the Free UI cannot be finished without it.
- **R03 nested scroll in the pager:** Flutter does not chain a vertical scroll into a vertical `PageView`, so a long back face or a tall question could trap the student on one page (the very complaint of LK20).
- **R04 contract drift:** the web feed and covers were still changing at 1:10 am, and the written contract lacks covers, Keep and the Free feed 402; models written now may be rewritten.
- **R05 RAM and leftovers:** AVD 2 GB (`hw.ramSize=2048`), Gradle `-Xmx2G` plus Kotlin `-Xmx1G` (`android/gradle.properties`), `flutter_locked.sh` gives two slots, a `next dev --webpack` server costs 2 to 4 GB of commit
  (port 3451, not running now), `flutter_tools.*` leftovers are about 200 MB each. Rules: check Available MBytes first; one emulator, stop it while many builders compile; `gradlew --stop` after every build; kill only your own
  `flutter_tester`, `dartaotruntime`, Gradle and node processes; use `next build` and `next start` for a fixed-commit server; run only `test/golden/learn2` and the touched unit folders, never the whole 3,222-PNG suite per agent;
  sweep temp after each run; never leave the demo build on the owner's phone.
- **R06 golden churn:** the Must-know word touches all 70 Key cards PNGs; replacing the door touches 71 learn PNGs plus practice, start and today.
- **R07 door order and route collisions:** the code order is not the brief's order; `/learn/run/:id` is already the lesson run and `/study/<id>` maps to it.
- **R08 haptic rule conflict:** FEED-2 asks for a double tick on a wrong answer; the app's grammar says nothing on a wrong answer.
- **R09 chapter cover art (LK21):** the app has one object per subject and no per-chapter art; the web has not chosen a replacement.
- **R10 Must-know re-tier:** the overlay changes `importance` and so the Free taste; `taste.json`, `display_parity.json` and kept decks were made before it.
- **R11 release train:** Key cards is not in any Play build yet (v16 is 1.0.18+16); Learn v2 rides with it as version 17; the Play steps and the upload key are the owner's.
- **R12 shelf sets need N reads:** the web reads every chapter to build a Find shelf; on a phone that is 14 to 17 calls.
- **R13 long stems at 360 dp and large text:** CRITIQUE R2 (a 10 to 15 line stem with the options under the fold) is worse on a phone; 56 dp rows at text scale 1.3 need room.
- **R14 Free line outside the limit:** the product rule says Free limits show only at the real limit; `freeNote` shows on Learn home all the time.
- **R15 resume after process death:** Android kills a backgrounded app; the written contract has no way to reopen a run except `POST /runs {resume}`, which the preview supports but the contract does not list.
- **R16 how the owner judges the app:** he judges only from the emulator walk (and a live prototype on his phone for web); the feed's feel (swipe, flip, flight) is poorly shown by stills.

---

## 10. Decisions needed before starting

1. **Base and release:** confirm `ui/1031-keycards` as the base and that version 17 (1.0.19+17) ships Key cards and Learn v2 together, behind the server flag with the legacy door as fallback. (CTO.)
2. **Production `/api/learn` and the freeze:** who wires it, when, and the web commit the app freezes against. Until then the app uses fixtures and the debug preview client. (Main session, web track.)
3. **LK15 shape:** does a Quick recap, a cards-only run or Find your level count as Free's one session a day; is the 10-minute cap a clamp or a refusal; the response code and the one limit line; where the line shows (only at the limit);
   the server allowance (the plan is "like first_full_mock"). Explore's Untimed questions stay unlimited. (CTO, with the owner's consent already recorded as LK15.)
4. **Feed way in:** the recommendation in 4.6 (Practise row opening an Explore page, a Today card, a key on the chapter page and run end) versus a covers shelf on Learn home. (Owner or CTO; he judges it in the walk.)
5. **Chapter cover art (LK21):** the web track decides first. For the app, no new paid art: a typographic cover (large chapter number, part line, the small subject object) or a procedural paper stack keyed by chapter; new art only if he asks.
6. **Door order:** keep Practise | Your papers | Learn (what exists, "navigation stays exactly") or move to Practise | Learn | Your papers (DESIGN-SPEC A8). Recommend keeping it until he sees the walk. (Owner.)
7. **Wrong-answer haptic:** the app grammar says none (and M4 used a shake with no haptic); FEED-2 says a double tick. Recommend none, shake only, `MmShake(haptic:false)`. (CTO.)
8. **Offline scope for v2.0:** online only first, with the offline strip and a "Needs a connection" state; the cards-only offline composer in slice 5. (CTO.)
9. **Watermarked sheet (LK6):** on-device PDF with the `pdf` package and embedded fonts (new dependency), a server-rendered PDF, or an interim plain-text share with a visible mark line. Recommend on-device PDF with a server sheet code. (CTO.)
10. **Concept cards row and old extras:** confirm Learn home drops "Revise N concept cards" (Revise already plays them, B 6.1) and keeps lessons, summary, offline packs, study plan and record in the foot row. (CTO.)
11. **Lesson in a run:** reuse the existing lesson screens and return to the run, rather than a new in-run lesson player. (CTO.)
12. **Free line on Learn home:** hide `freeNote` by default and show Free facts only where they bite. (CTO against the product rule; the web shows it today.)
13. **Instrumentation A12:** needs the server's `usage.js` allowlist before the app may queue the events; do it in slice 5 or drop it. (Web track.)

---

## 11. Evidence index

- Branch facts: `git -C mockmob-next worktree list`, `git merge-base --is-ancestor` runs above, `git diff --stat ui/1020-v16 98c41a73e -- flutter_app`.
- Door and Learn door: `practice_screen.dart:132-153, 501-580`, `door_switch.dart:40`, `practice_door.dart:8-27`, `door_stage.dart:48`, `learn_screen.dart:312-560`, `router.dart:502-514`, `routes.dart:48, 75, 124-125`.
- Key cards: `keycards_providers.dart:56-178`, `keycards_reviews.dart:41-50`, `keycards_cache.dart`, `key_card_parts.dart:62-118, 535-600, 697-750`, `keycards_entries.dart:16, 43`, `app_overrides.dart:31-40`.
- Stream: `stream_screen.dart`, `stream_controller.dart`, `feed_api.dart:27-42`, `practice_card.dart:26-87`, `question_actions.dart`, `saved_repository.dart:90-128`, `more_rows.dart:34`, `entry_points.dart:108-120`.
- Today: `suggested_stack.dart` (header comment lines 1-31), `suggested_deck.dart`, `glance_builder.dart:122`, `links.dart`.
- Motion and haptics: `drag_commit.dart:114`, `shake.dart`, `springs.dart`, `flight.dart:78`, `haptics.dart:111-125`, `motion.dart:1-140`, `motion_guard_test.dart`.
- Tooling: `tool/emu_rec.sh`, `tool/flutter_locked.sh`, `tool/android_env.sh`, `android/gradle.properties`, `docs/DEMO-BUILD.md`, `test/device_demo/demo_keycards.dart`, `test/golden/keycards/kc_golden_support.dart`.
- Web: `web:src/lib/server/learnPreview.js:827-843`, `web:src/components/learn2/api.js`, `web:data/learn/{compose,suggest,search,feed,stamps}.js`, `web:src/lib/server/keycardsHttp.js`, `web:src/lib/server/keycardsPreview.js:131-160`.
- Specs: `spec:DESIGN-SPEC.md`, `spec:API-CONTRACT.md`, `spec:design/B-chapters.md` (2.2, 3.1 to 3.10, 4.6, 5, 6), `spec:understand/R4-explore.md:182` (the D90 rule), `spec:CRITIQUE-1.md`, `web:docs/brain/learn-1031/FEED-2.md`,
  `mockmob-next/docs/brain/OWNER-FEEDBACK-2026-10-31-LEARN.md` (LK15 to LK23).

---

## 12. Build tasks and risks (the ids used in the returned result)

Severity: blocker = must exist or be settled before the rest can move; high = core of the feature; medium = needed for a complete build; low = can slip.

| Id | Sev | Task | Effort |
|---|---|---|---|
| T01 | blocker | Cut `ui/1101-learn-app` from 98c41a73e in a new worktree; run the baseline gate once (analyze, unit folders keycards, learn, practice, today, insights, motion, core_ui, golden keycards and learn) and record it | S |
| T02 | blocker | Data layer: `learn_models`, `LearnApi` (Http, Off), providers, `learnV2OnProvider` with the legacy-door fallback, `liveAppOverrides` wiring, `_bucket` line | M |
| T03 | blocker | Fixtures and demo: record web responses to `test/fixtures/learn/*.json`, stateful `DemoLearnApi`, debug-only `PreviewLearnApi` to the dev preview route, demo flags | M |
| T04 | high | Dart ports with parity fixtures: `run_math`, `home_model`, `feed_rules` | M |
| T05 | high | Plumbing: routes, legacy `/cards` redirects, ActionRouter, copy file, prefs, motion tokens and flight curve, `ProReason.learnFeed`, `MmShake` cycles; motion guard stays green | S to M |
| T06 | high | Learn home shell: shared subject state, compact subject row, heading line, search field, first-visit line, states, entrance | M |
| T07 | high | Suggestions: lead and two compact cards, keys start at once, href mapping | M |
| T08 | high | Chapter map with the part switch (LK2), sort, pinned parts, rows, keys by chapter | L |
| T09 | high | Chapter page: head, length control, own-length sheet, preview provider, Start, note, recap key, shelf rows, states | L |
| T10 | high | Piles widget: three fanned papers, count roll, leave out, last pile shakes, next-chapter pile | L |
| T11 | blocker | Run controller: start, resume, answer, rate, keep, end, re-insert, Free looks, offline fallback, coach flags | L |
| T12 | high | Run player: top line, pinned rating bar, card turn, question turn, lesson turn, recap, rounds, coach lines | L |
| T13 | high | Got it, Easy, Missed flights, Revise pile, stamp, haptics (`MmFlyTo`) | M |
| T14 | high | Run end: count-up numbers, lines, fanned Revise pile, Mobi once, lead key and three options | M |
| T15 | medium | Cards view: filters, folded rows, open in place, sections, pick mode, Free locked row | M |
| T16 | medium | Find in place: shelves, search with spans, pick; ask for a set endpoint | M |
| T17 | medium | Print or save PDF with the MockMob mark (LK6): dependency, fonts, server sheet code | M |
| T18 | high | Explore covers page: length control, snap row, real counts, one volt Play, cover art | M |
| T19 | high | Feed shell: vertical pager, ticks, close, title, checkpoint, end, states, visible Next | L |
| T20 | high | Feed card item: flip, Keep with ghost flight and stamp, rail, hints; nested-scroll spike | M |
| T21 | high | Feed question item: four rows, server grading, right and wrong motion, streak chip, line sheet, Save | M |
| T22 | medium | Entry points: Practise row, Start row, Today moves, Review link, line-you-needed link, door order (if decided) | M |
| T23 | medium | Must-know as a volt word with no box (LK13) in `KcKindLine`; regenerate Key cards goldens | S |
| T24 | medium | Offline cards-only slice: kept-deck composer with a parity test, outbox ratings, strip and dimmed rows | L |
| T25 | high | Tests and goldens: unit, parity, controller, gates, about 120 new PNGs | L |
| T26 | high | `tool/walk_learn2.sh`, the walk matrix, motion frame sheets | M |
| T27 | medium | Release: bump to 1.0.19+17, AAB, flag rollout order, Play notes | S |
| T28 | low | Instrumentation A12, after the server allowlist | S |
| T29 | low | Remove the legacy Learn door and Key cards screens after the owner approves | S |

| Id | Sev | Risk |
|---|---|---|
| R01 | blocker | No production `/api/learn` routes (dev preview only) |
| R02 | high | LK15 Free session rule has no server shape |
| R03 | high | Nested vertical scroll inside the vertical pager |
| R04 | high | Contract drift while the web feed and covers change |
| R05 | high | RAM, Gradle and temp leftovers on a 2 GB emulator PC |
| R06 | medium | Golden churn across Key cards, learn, practice, start and today |
| R07 | medium | Door order differs from the brief; route names collide |
| R08 | medium | Haptic rule conflict on a wrong answer |
| R09 | medium | Chapter cover art (LK21) unresolved |
| R10 | medium | Must-know re-tier against taste and parity fixtures and kept decks |
| R11 | medium | Release train: Key cards is not in a Play build yet |
| R12 | medium | Find shelf sets need one read per chapter |
| R13 | medium | Long stems and text scale 1.3 at 360 dp |
| R14 | low | Free line shown outside the real limit |
| R15 | medium | Resume after process death |
| R16 | medium | The owner judges only from the walk |
