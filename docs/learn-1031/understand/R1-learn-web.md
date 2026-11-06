# R1: the website's Learn area, mapped (reading job only, no design, no code changed)

Written 31 Oct 2026 by the learn-web reader. Code read from `C:/Users/atish/Desktop/mockmob copy/wt-1031-keycards-web` (src paths below are relative to it). Screenshots looked at: `wt-1031-kc-ui/tmp/walk-1031/web` (entry-learn-row, cards-home, deck-*), `wt-1031-kc-realdeck/tmp/walk-1031/realdeck` (home-new-free, home-commerce-pro-accountancy, deck-ratios-read-free). Owner feedback read first: `docs/brain/OWNER-FEEDBACK-2026-10-31-LEARN.md` (items LK1 to LK14).

Nothing here was run live. Where I say a bug "probably" causes something, it is from reading code, not from reproducing it.

## 0. The one-paragraph picture

"Learn" is really two separate products glued by one row. (A) Concepts: 21 short lessons in 4 subjects (English, Accountancy, Business Studies, Economics) plus 86 recall cards, at `/learn`, `/learn/[id]`, `/study/[id]`, `/learn/summary`. (B) Key cards: 5,800 NCERT-line cards in 6 subjects (adds Biology and Political Science), at `/cards` and `/cards/[chapter]`, entered from Learn through one quiet row. They use different subject lists, different words, different layouts and different Free/Pro rules. The hub itself (`/learn`) is weakness-led: its single big yellow key is chosen from the student's wrong answers, and the main list is "Where you lose marks". A student who wants to choose a chapter and a time has no direct route: they must open a subject tab, open a chapter row, then a lesson, then a start key. No place in Learn takes a time.

## 1. How a student gets to Learn and to Key cards

| Where | What | File |
|---|---|---|
| Phone dock | Today, Practice, Start, Mob, You. No Learn tab. | `src/lib/arenaNavigation.js:62-65` |
| Practice place, tab row on phone / indented rows in desktop sidebar | Practice, Your papers, Learn, Explore, Saved. Learn only appears when `STUDY_CONTENT_ENABLED=true`. | `arenaNavigation.js:34,48`; `src/app/(app)/AppLayoutClient.jsx:321-327` |
| Practice page, a "door" card | "Learn / Short lessons on the ideas behind your mistakes." plus a "Next lesson" link and "All lessons" | `src/components/study/ConceptsPanel.jsx:24-34` |
| Today, Revise row | Key cards due are folded into the Revise line ("... N Key cards among them") | `src/components/today/TodayQueue.jsx:29-35` |
| Review chapter rows | "Key cards for this chapter" link, when that chapter has cards | `src/components/keycards/KeycardsLinks.jsx:28-40` (via `ChapterRows.jsx:200`, `ReviewChapters.jsx:147`) |
| Result page, under a wrong answer | "The line you needed", 1-2 cards, "Add to Revise" | `src/components/keycards/LineYouNeeded.jsx`; `ResultPageClient.jsx:515` |
| Learn hub | ONE row "Key cards" | `src/components/study/StudyLibrary.jsx:90` -> `KeycardsLinks.jsx:13-25` |
| Progress page | Study record card with "Open Learn" | `src/components/study/StudyProgress.jsx` |

There is no top-level nav item for Key cards. `AppLayoutClient.jsx:338-340` keeps "Learn" highlighted while on `/cards*`. So to reach Key cards on a phone: dock Practice (1) -> tab Learn (2) -> scroll past the big yellow card -> row "Key cards" (3) -> subject tab -> chapter (5). This is LK1 ("badly placed and very small"). Evidence: `entry-learn-row-390-night.png` shows the Key cards row as plain text with a thin chevron, below the big "Start the lesson" key, above the search box; it looks like a footnote of the card above it. At 1440 (`entry-learn-row-1440-night.png`) it is the same plain row in the main column.

Copy of the row, exactly (`KeycardsLinks.jsx:20-22`): title `Key cards`; line `NCERT’s exact lines, chapter by chapter. 5 cards due today.` when due, else `NCERT’s exact lines, chapter by chapter, each with its page.` The row is hidden when Key cards are off, loading or failed.

## 2. The Learn hub, `/learn`, top to bottom

Route: `src/app/(app)/learn/page.jsx` (11 lines) renders `StudyWorkspace` (`src/components/study/StudyWorkspace.jsx`). `/learn?recall=due` redirects to `/review/revise?source=cards`. `/learn?subject=accountancy` pre-selects a tab. Page title `Learn — MockMob`.

Data load: `StudyWorkspace.jsx:37-46` fetches `GET /api/study/catalog` (route `src/app/api/study/catalog/route.js` -> `studyCatalog()` in `src/lib/server/study.js:104`). `StudyLibrary` also calls `useReview()` = `GET /api/me/review` (`src/lib/reviewRead.js`, route `src/app/api/me/review/route.js`; the repo's own comment calls it the heaviest read on the site, cached 5 min). Key cards row calls `GET /api/keycards` (`src/components/keycards/api.js:21`).

### 2.1 States of the page

| State | What shows | Where |
|---|---|---|
| Catalog loading | h1 "Learn", lede, skeleton of the big card and 4 bars (aria "Loading Learn") | `StudyWorkspace.jsx:64-66` |
| Catalog failed | `Concepts did not load.` plus "Your saved lessons and progress are safe." (if the error says could not be saved) else the error text; buttons "Try again", "Sign in" (401), "Practise questions" | `StudyWorkspace.jsx:60-63` |
| Lessons switched off (`state:'disabled'`) | `Lessons are switched off right now. Your saved progress is kept. You can still practise questions and take mocks.` and a "Practise questions" key | `StudyWorkspace.jsx:70` |
| Review loading (catalog ready) | big card replaced by a 3-bar skeleton, aria "Finding your next lesson"; subject area is a 3-bar skeleton | `StudyLibrary.jsx:76,107` |
| Review failed (`state:'unavailable'`) | note `Your mistakes did not load, so lessons are not ordered by marks yet.` and a "Try again" text button | `StudyLibrary.jsx:108` |
| Brand new student (no papers) | no "Where you lose marks"; big card = kind `next`, lead "Start here."; sidebar "0 of 21 lessons read, 0 cards in Revise, 0 cards recalled" | `concepts_pick.mjs:90-98`, `StudyLibrary.jsx:137-141` |
| Everything read, nothing costly | big card title "Every lesson is read", reason "Nothing is waiting. Practise a chapter or take a mock to find what to study next.", key "Practise questions" -> `/dashboard` | `concepts_pick.mjs:99` |

For a new student the first lesson is chosen by `studyRecord()` (`study.js:93-97`): no weak chapter, so the subject with the fewest lessons read, ties broken by `prefs.subjects` order, whose default is `['english','accountancy','business_studies','economics']` (`data/study_engine.js:3,6`). So a brand-new commerce student is told "Start here." on an English vocabulary lesson, "Clear or unclear: words about expression" (summary shown as "Lucid, concise, coherent, ambiguous, obscure."), key text "Start the lesson, 7 minutes" (5 min lesson plus 2 for recall; see 2.3). Their subject tab also starts on English.

### 2.2 Layout and sections, in order of appearance (`StudyLibrary.jsx`)

Two-column board at wide width (`cx-board`: main column plus a right "aside"), one column on a phone with the aside's contents at the end.

1. Header (`:71-72`). h1 `Learn`. Lede `Short lessons on the ideas behind your mistakes.` (Note the lede promises mistakes-led learning.)
2. THE NEXT-LESSON CARD, `cx-next`, the only yellow key (`:76-83`). Content comes from `conceptsPick({catalog, review})` in `data/study/concepts_pick.mjs:59-100`. Four kinds, in this strict priority order, and only ONE is ever shown:
   - `finish`: an unfinished lesson (`catalog.active.mode==='learn'`). Title = lesson title. Lead `Finish this next.` Reason `You stopped at step {k} of {n}. Everything before it is saved.` Key `Finish the lesson, step {k} of {n}` (link to `/study/{runId}`).
   - `mistakes`: the costliest chapter (by marks, from the review) that has an unread or in-progress lesson. Lead `Read this next.` Reason `{n} of your open mistakes are in its chapter, {chapter}.` (or `{n} questions you left blank are in its chapter, ...`). Key `Start the lesson, {m} minutes` (m = lesson minutes + 2, or 2 if already read). Button starts a run directly (POST `/api/study/runs {mode:'learn', unitId}`) and goes to `/study/{runId}`, skipping the lesson overview.
   - `next`: `catalog.nextUnit` (server's rotation). Lead `Start here.` when nothing is read, else `Read this next.` Reason = the lesson's summary as a sentence.
   - `practise`: see table above.
   Under the key, a cost line: `Free. Its 5 cards then join Revise, where 8 are due today.` (or `Free.` with no cards). In the screenshot at 390 the card's heading is cut off under the sticky header (the full-page capture was taken scrolled), so the real first screen on a phone is: header, then this card (title, reason, key, cost line).
3. Error banner for a failed run start (`:84`), copy from `studyCopy.js:211-224` (`friendlyError`).
4. Optional "continue" row: if there is an active recall run: `Finish your Revise session` / `You stopped at card {k} of {n}. Everything before it is saved.` (`:86`).
5. Optional "Revise" row: `Revise {n} concept card(s)` / `From lessons you have read. About {m} minutes, free.` (button, starts a recall run, `:87`). Shown only when `queue.dueCount>0` and recall is enabled. Note it is concept cards (the 86 lesson cards), NOT Key cards.
6. THE KEY CARDS ROW (`:90`, section 1).
7. Search box (`:92-93`). Placeholder `Search chapters and lessons`. Needs 2+ characters. Searches lesson title, chapter, summary, skill (`searchConcepts`, `concepts_pick.mjs:144`). While a query is on, the tabs and sections are replaced by "Results": `{n} lessons, {m} chapters without one` and rows; chapters without lessons link to practice; empty text `Nothing matches that. Try a chapter name or a topic.` It does NOT search Key cards.
8. Subject tabs (`:102-104`): always the same four, in alphabetical order (Accountancy, Business Studies, Economics, English), each with its 3D `SubjectObject` image. Not filtered by the student's own CUET subjects. Roving-tabindex tablist with arrow keys. The tab shown as selected before the student ever taps is `pick?.unit?.subject || firstSubject` (`:46`): it CHANGES when the review read finishes (see problems).
9. "Where you lose marks" (`:109-116`), only if the selected subject has chapters with open cost. Heading `Where you lose marks`, side text `From your papers`. Up to 4 chapters (`LOSE_ROWS=4`). Each chapter: name, `−35` (marks lost, red, with sr text "marks lost") and meta e.g. `5 open mistakes, 1 blank. 1 lesson` or `4 open mistakes, 1 blank. No lesson yet. Practise the chapter`. Chapters with a lesson list the lessons below (ring + title + one line + minutes). Chapters with no lesson are one link row to practice. Marks: wrong = 6, blank = 5 (`data/result_next_move.mjs:16-17`), summed over open items from `GET /api/me/review` `chapters[]` (`data/review_input.mjs:99-137`: `marks`, `openWrong`, `blank`).
10. "All {Subject} chapters" (`:118-131`). Heading plus `{n} lessons, {k} of {m} chapters` (or `Lessons are still being prepared`). Every syllabus chapter of the subject (7 English, 16 Accountancy, 13 Business Studies, 18 Economics) as a collapsed row (SmoothDetails): name, red `−n` if costly, meta `2 lessons, 1 read` or `No lesson yet. Practice ready`. Opened: its lessons, then two text links `Practise this chapter` and (only if it has lessons) `Read or print the chapter summary`. Foot: `Chapters follow the CUET UG 2026 syllabus.` Only 15 of the 54 chapters have a lesson at all (the 21 lessons cover 15 chapter names); the other 39 rows open to just "Practise this chapter".
11. Aside / record column (`:137-146`): `{read} of {of} lessons read`, `{cards} cards in Revise`, `{recalled} cards recalled`; link `See your marks in Progress`; `Study preferences` (collapsible, section 4); row `Test it in a full mock` / `50 questions, 60 minutes. Shows which chapters still cost marks. Access and cost are shown first.` -> `/dashboard?mode=full`. On a phone this block is at the very bottom of a long page.

A lesson row (`Lesson`, `:23-28`) is: a 36px progress ring (`UnitRing.jsx`: empty dashed ring = not started, arc = in progress, full arc = read/lock in, badge = cards due, tick = learned), title, one line (`New. {summary}` / `In progress, step k of n. ...` / `{n} cards due in Revise today` / the summary if read), and `{m} min` or `Read`. Link goes to `/learn/{id}` (the overview), carrying `?from=chapter:{subject}:{chapter}` when it came from a costly chapter.

### 2.3 What "N minutes" means on the key

`startMinutes = estimatedMinutes + LOCK_IN_MINUTES(2)` when unread, `2` when read (`concepts_pick.mjs:39`, `lesson_map.mjs:14`). Lesson `estimatedMinutes` are 5 to 7 (list in section 6). So "Start the lesson, 9 minutes" in the screenshot is a 7-minute Accountancy lesson plus 2 for recall. Lessons and a recall step are the only timed things; "Apply" (practise 10 questions) is stated as "about 10 min, separate".

## 3. How the Learn hub's special parts work

### "Read this next." (the big card)
Pure function `conceptsPick` (`data/study/concepts_pick.mjs:59-100`), inputs: catalog (`units`, `active`, `nextUnit`, `progress`, `queue`) and review (`state`, `chapters`, `reviseDue.total`). Priority: unfinished > costliest chapter with an unread lesson > server's next > practise. Due recall cards are explicitly never the pick ("they live in Revise"). It returns exactly one pick; there is no second option, no "or", no time choice. That is the owner's "not dynamic, just one thing" (LK11). The same function drives Practice's "Next lesson" link (`practicePanel`, `:174-183`), so both places always agree.

### "Where you lose marks"
See 2.2 item 9. Weakness-led by construction: it only exists if the student has taken papers and has open mistakes. A new or never-wrong student never sees it. The word "marks" here is a count of marks not earned, shown as a minus.

### The Key cards row
See sections 1 and 7.

### "Study preferences" (`StudyWorkspace.jsx:83-136`, in the aside)
Collapsed by default. Title `Study preferences` (Pro: `Study preferences and weekly plan`). Inside:
- Fieldset `Subjects to plan for`: 4 checkboxes (the 4 Concept subjects). Default all four.
- `Usual study time`: `DailyMinutes` picker (`src/components/goal/DailyMinutes.jsx`), presets 10/20/30 plus longer choices; held in account, with a device fallback if the server only accepts 10/20/30 (`refusedLonger`, `:80,104-105`).
- Button `Save preferences`. `PUT /api/study/preferences` with `expectedRevision`; success text `Saved. Today will plan around these choices.` (or a "saved on this device" line).
- `Weekly plan and mixed revision`: Free sees `A saved day-by-day plan and custom mixed revision come with Pro. Lessons, reviews and Today’s plan are free.` and a "See Pro" link. Pro sees a 7-day grid (Monday to Sunday, a subject Listbox and a minutes Listbox each), `Save weekly plan`, then `Review concepts you have already learned. New cards appear after you finish their lesson.`, a checklist `Concepts to mix in one revision session, up to 20` of read lessons, and `Start mixed revision` (POST `/api/study/runs {mode:'recall', mixed:true, unitIds}`; server throws PREMIUM_REQUIRED for Free, `study.js:188`).
What it actually changes: `prefs.subjects` and `minutes` feed Today's plan (`LearningNextAction`, `/api/learning/plan`) and the server's `nextUnit` rotation (`study.js:96-97`). It does not filter what Learn shows (catalog is always `allSubjects:true`, `study.js:105`). So "Subjects to plan for" does not change the four tabs. This setting is buried in the aside, collapsed, and its name does not say it controls Today.

### "Test it in a full mock"
A plain link row to `/dashboard?mode=full` (`StudyLibrary.jsx:145`), no lesson/chapter context carried. It is one of two places (with the Today plan) that says marks and mocks.

### Where the time-boxed mix already exists (not in Learn)
Today's `LearningNextAction` (`src/components/LearningNextAction.jsx`) has the 10/20/30 min segmented control and builds a `plan.sequence` of recall, one lesson, practice (`guidedSequence`, `data/study_engine.js:144-175`; the minutes are split by `allocateMinutes`). It excludes Key cards. It is the closest existing thing to the owner's "pick a time, get a mix", but it lives on Today and is chosen by the engine, not by the student.

## 4. Lessons: overview, player, finish

### `/learn/[id]` overview (`LessonOverview.jsx`, data `GET /api/study/units/{id}` -> `studyUnit()` in `study.js:108`)
Copy and structure: back link (`Learn`, `Back`, or `Back to Question {n}` depending on `?from=`); h1 lesson title; meta `Accountancy, Admission of Partner. A 7-minute lesson and 5 cards. In progress, 3 due now.`; a FromBlock saying why you are here (`You are here from Question 42, Mock 3` / `5 open mistakes in this chapter` / `Today put this lesson first`); ONE yellow key whose label depends on status: `Start the lesson, 9 minutes` / `Resume the lesson, step k of n` / `Lock it in, {n} cards` / `Practise {chapter}`; secondary `Read the lesson again`, `Practise this chapter`; a 3-step list Learn / Lock it in / Apply with times; `You’ll be able to` objectives; `How CUET asks this:`; collapsed "Inside the lesson" outline; `More in {chapter}` siblings; collapsed `Sources and version`; and `Print a summary` (browser print of the lesson's reading blocks, no watermark, available to Free).

### `/study/[id]` the player (`StudyRun.jsx`, `StudyBlocks.jsx`; events `POST /api/study/runs/{id}/events`)
Learn mode: header `Lesson: {title}`, `Step k of n`, pips, a stage with label (The idea / Worked example / Compare / Common mistake / Method / New words / Concept map / Quick check, not scored), reading blocks with key `Next: {next title}` / `Try a quick check` / `Finish lesson`, checks with feedback. Recall mode: `Recall: {title}`, `Card k of n`, `Say or write your answer first, then check it.`, key `Check your recall`, ratings Forgot / Hard / Got it / Easy (hints "Shows again soon", "Shorter gap", "Normal gap", "Longer gap"), after each rating `Saved. “{word}” comes back in 3 days.` The card flies away on rate (`studyFeel.js flyAway`, soft click on a right answer). An AI helper `StudyHelp` sits under each step. Footer `Every answer is saved as you go. You can leave and continue later from Concepts or Today.` (the page is called Learn everywhere else; this copy still says "Concepts", also in `StudyRun.jsx:67,77`, `studyCopy.js:221`, `StudyChapterSummary.jsx:149` "Back to Concepts", and the loading text in `learn/page.jsx`.)

Finish screens: `LessonDone` (Mobi reaction, `Lesson complete`, `You got 2 of 3 quick checks right on the first try.`, `This lesson covered`, `Next: lock it in` with a key `Lock it in with 5 cards`, `Then: apply it` with `Practise {chapter}`, links `Back to Concepts` and `Today`) and `ReviewDone` (`{n} of {m} remembered`, list of cards with `Next in 3 days`, "Revisit what slipped", next step).

### `/learn/summary?subject=&chapter=` (`StudyChapterSummary.jsx`, `GET /api/study/summary` -> `studyChapterSummary`)
Shows the reading blocks of every published lesson in the chapter, with `Print or save as PDF` (browser print). Warns `This covers {n} published lesson(s), not the complete chapter.` No watermark, no Pro gate on the API (`study.js:163-168`). Reached only from an opened chapter row in "All chapters" (3 clicks).

## 5. Free vs Pro in Learn

| Thing | Free | Pro |
|---|---|---|
| Lessons, concept recall cards, Revise of them, summary and print | Open | Open (same) |
| Study preferences: subjects, usual time | Yes | Yes |
| Weekly day-by-day plan, mixed revision | Locked (`PREMIUM_REQUIRED`), shown as a Pro line | Yes |
| Key cards: cards per chapter | 5 "taste" cards (first 5 Must-know in book order, `data/keycards.js:66-80`); rest are one locked row | All |
| Key cards: Study reviews | 10 reviews/day, 5 new cards/day (`KEYCARD_RULES.free`, `data/keycards.js:9`) | No review cap; new cards counted 15/day default |
| Key cards: Add chapter to Revise | Adds the taste cards | Adds only the Must-know cards; others one at a time from the card menu |
| Key cards: Last look | the open Must-know cards (so at most 5) | all Must-know cards |
| Key cards: Print chapter sheet | Hidden | Shown (Must-know cards only) |
| Key cards home | One dismissable Pro line `Pro opens every card in every chapter and keeps them on a schedule.` | none; plus a Pro-only reason line on the deck ("7 of 12 right on the latest try at each question. Cards: 14 of 20 holding.") from `/api/me/chapters` |

## 6. The real content that Learn can offer today

- Concept lessons: 21 (`data/study/pilot.json`, `release.json`): English 8 (6 vocabulary of 5 min, Main idea 6, Stated/inferred 6), Accountancy 4 (Sacrificing and gaining ratios 7, Revaluation 7, Authorised/issued/subscribed 5, Current and quick ratio 5), Business Studies 5 (6, 7, 5, 5, 5), Economics 4 (7, 7, 5, 5). Recall cards 86 (3 to 5 per lesson). They cover 15 chapter names out of 54 chapters across 4 subjects. Everything in the Learn hub's 39 other chapters is "No lesson yet".
- Key cards: 5,800 cards, 6 subjects, 73 chapters with cards (accountancy 868/14, biology 1394/13, business studies 900/11, economics 1193/17, english 349/2, political science 1096/16). Card kinds: definition, term, key line, list, difference, steps, types, formula, fact, example, entry (journal entry), quote; English: word, idiom, one word, usage, rule. Every card has a book source and page (English: "Written for MockMob"). Cards carry `importance` of `must` or `good`.
- MUST-KNOW SHARE (LK13): 3,916 of 5,800 cards (67.5 %) are tagged `must`: accountancy 618/868 (71 %), biology 916/1394 (66 %), business studies 629/900 (70 %), economics 832/1193 (70 %), english 193/349 (55 %), political science 728/1096 (66 %). The `Must-know` tag (a yellow-green outlined chip) is drawn on every such card header (`KeyCard.jsx:173`, style `.kc-tag` at `keycards.css:185`) in Read, Study, Last look and Revise, plus the deck head count `26 cards, 18 Must-know`, the empty text `No Must-know cards are open in this chapter yet.`, Pro's `Adds the 18 Must-know cards. Good-to-know cards you add one at a time.` and `Print chapter sheet` (Must-know only). So the tag is on two of every three cards, which is why it reads as noise. The Free "taste" and Pro's "Add chapter" both depend on the same flag, so it is not only a label.

## 7. Key cards, screen by screen

### `/cards` home (`KeycardsHome.jsx`, data `GET /api/keycards`, built in `src/lib/server/keycards.js:238-277`)
- Head: h1 `Key cards`, `NCERT’s exact lines, chapter by chapter, each with the page it is on.`
- Today box: `14 cards due today` / `About 4 minutes in Revise, with the rest of today’s work.` with yellow `Revise now` (-> `/review/revise`); or `Nothing due today` / `Open a chapter and add it to Revise. Its cards come back there when they are due.` (no key).
- Free only: dismissable Pro line (InlineNudge).
- Subject tabs: only the student's own CUET subjects (`me.subjects.filter(isTopSubject)`), in the order of the student's subject list (not alphabetical), each with its object image. This is a different list and order from Learn's tabs.
- OptionPicker (the "Your part" control; `KeycardsHome.jsx:71-101`) for subjects with options: Accountancy `Part` = `Analysis of Financial Statements` or `Computerised Accounting`; Mathematics and Computer Science `Section` (B1/B2). Label `Your part in Accountancy`, a two-button radio group; hint `Choose your part and only its chapters show here and in your practice. Until then, both parts show.` / after choosing `Only that part’s chapters show here and in your practice. You can change it at any time.` / `Saving your choice` / `Your choice was not saved. Try again.` Saving: `PUT /api/me/subject-options` (`keycards.js:484-490`, upsert), then `refreshHome()` refetches the whole home body. The same option also filters practice questions and Revise.
- Units and chapter rows: grouped by CUET unit (Accountancy: "Accounting for Partnership", "Reconstitution of a Partnership firm", "Dissolution of Partnership Firm", "Company Accounts: ...", "Analysis of Financial Statements", then the Computerised Accounting System). Each row: title, `Accountancy Part 2, Ch 5`, optional chip (`CUET only` / `CBSE teaches this in Class 11`), a state word with a small pie glyph (`Not started`, `Too few answers`, `Needs work`, `Getting there`, `Holding`, `Could not load`, optional `, fading`), counts `165 cards, 2 due`, and for Free `5 of 165 open`. A long Accountancy list is roughly 14 rows tall on a phone. For Free almost every chapter says "5 of N open", which repeats on every row (`home-new-free-390-night.png`).
- Other states: loading skeleton, `Key cards are not open yet`, `No subjects to show`, error with "Try again".
- Entry to a chapter: tap a row -> `/cards/{subject.chapter-slug}`.

### `/cards/[chapter]` deck (`ChapterDeck.jsx`, data `GET /api/keycards/deck?chapter=` and, Pro only, `GET /api/me/chapters?subject=`)
Head: back `Key cards`, optional unit, h1 chapter title, `Business Studies Part 1, Ch 1`, chip, Pro reason line. Side/summary (on phones it sits BELOW the mode tabs in Read, hidden in Study and Last look): `26 cards, 18 Must-know` (Free: `5 of 165 cards open, 114 Must-know in all`), the one yellow key `Add chapter to Revise` (turns to `In Revise. Due cards come back there.` once everything is scheduled), the fine line (`Adds the 5 open cards. Free reviews 10 cards a day.`), and Pro `Print chapter sheet`. Then a 3-way segmented control `Read | Study | Last look` (tablist, sliding thumb, `?mode=study|last` kept in the URL). Source of truth for what each is:

| Mode | What it really is | Content | Writes |
|---|---|---|---|
| Read | A long vertical list (an `ol`) of every open card in book order: kind label, `Must-know` chip, `Asked in 1 past paper`, a "..." menu (`Report this card`; Pro: `Add this card to Revise`), the front as a small prompt, NCERT's words in a serif, the source line, and `In short` paraphrase. Free: after the open cards, one locked row `160 more cards in this chapter.` plus the Pro gate. | all open cards (up to 165 for Accounting Ratios on Pro) | none |
| Study | Recall session, 20 cards a round: front, `Show answer` (Space, or tap the card), then `Missed / Got it / Easy` (keys 1, 2, 3). Counter `1 of 26`, progress bar. Fine line `Each card you rate joins Revise: Missed brings it back soon, Got it and Easy space it out.` End screen `5 cards studied` with counts and keys `Study the next 20` / `Add chapter to Revise` / `Study again` / `Read the chapter`. Free limits: `Today’s free reviews are used`, `Today’s new cards are used`. | all open cards (including Good-to-know on Pro) | each rating POSTs `/api/keycards/review` mode `study`, which creates the card's schedule (so it joins Revise) |
| Last look | One card at a time, Previous / Next, swipe or arrow keys, `2 of 18`. Same card face as Read (kind, chip, front, NCERT words, source) but without the "In short" line or the menu. Fine line `Must-know only, and nothing is scheduled. Swipe to move on.` End: `That was every Must-know card` / `18 cards, nothing scheduled. Last look never changes when a card comes back.` / `Look again`. | open Must-know cards only | logs nothing in the UI; the server accepts mode `last_look` and never moves the schedule |

LK7 ("Last look vs Read is unclear"): the two show nearly the same card; the real differences are one-at-a-time vs one long scroll, Must-know only vs all, and no In short/menu. Neither the tab label nor the one-line hint says "quick flip-through of the key ones". The screenshots `deck-last-look-390-night.png` and `deck-read-pro-390-night.png` show this: Read on a phone with a real Pro deck is 14,688 px tall at 390 wide (a 26-card chapter), 5,690 px for the Free Accounting Ratios deck; the segmented control and a stats line sit above 4-5 screens of cards.

LK4 ("Read has a weird layout"): at 1440 the title is huge, stats and the Revise state sit in a right column far from the cards, and the card list is a long ruled list; on a phone the summary/Add key block is below the tab row and above the list, so the first screen is title, ref, reason, tabs, stats, key, then cards. Chips and menus repeat on every entry.

LK5 (Study is liked; wants motion): Study uses `KeyCardPlayer` (`KeyCard.jsx:197-287`). Motion today is only a 240 ms fade/rise in (`kc-in`), a 220 ms reveal of the answer, a 180 ms fade of the rate keys, `:active` press scale on the buttons, and a progress bar width. There is NO fly-away of the card and no sound on rating, although the concept-recall player has both (`StudyRun.jsx:53-57`, `studyFeel.js:104,126`, `flyAway`, `softClick`) and could be reused. The rating copy is `Missed`, `Got it`, `Easy` (`kinds.js:39-43`); `Got it` is the yellow default (`.kc-rate__btn[data-rating='3']`). Motion respects reduced-motion (`keycards.css:345-347`).

LK6 (print sheet + watermark): `Print chapter sheet` is `window.print()` (`ChapterDeck.jsx:379`) on a hidden `PrintSheet` portal (`:235-258`) styled in `@media print` (`keycards.css:349-366`): title, one reference line, the Must-know cards in NCERT's words with source, Georgia/serif. Pro only. There is NO watermark anywhere in the repo (grep for "watermark" finds nothing in src, public or data scripts). The lesson "Print a summary" (`LessonOverview.jsx:133`) and the chapter summary page ("Print or save as PDF") are likewise unmarked and free. The owner's wish: a MockMob mark repeated over the printed page. The owner's words mention "Got it" and "Print chapter sheet" together, but they are two different places: Got it is a Study rating, Print chapter sheet is a text button in the deck's side column (hidden on phones while in Study and Last look).

### Study end tallies
The end counts `Missed / Got it / Easy` are shown as big numbers; nothing animates there.

### Revise integration (for completeness)
`/review/revise?source=keycards` plays due Key cards after mistakes, checks and concept cards (`src/components/revise/reviseQueue.js:9-31`, 15 s a card). Today folds the count in. Not part of Learn but it is where scheduled cards come back.

## 8. Everything a student can do from Learn, and clicks

Counting from having `/learn` open on a phone (1 click = 1 tap or link). "Scroll" is not counted.

| Goal | Clicks | Route |
|---|---|---|
| Start the lesson Learn recommends | 1 (key) | POST run then `/study/{id}`, skips the overview |
| Finish an unfinished lesson | 1 | `/study/{runId}` |
| Revise due concept cards | 1 | POST recall run then `/study/{id}`; row only shows if cards are due |
| Open a lesson that costs marks (listed under the chosen tab) | 1 to overview, 2 to start it | `/learn/{id}?from=chapter:...` |
| Open any lesson in a subject | tab (1) + open chapter row (2) + lesson row (3) + start key (4) | `/learn/{id}` |
| Practise a chapter (10 questions, quick mode) | tab + open chapter + `Practise this chapter` = 3, then the practice setup page has its own start | `/dashboard?subject=&chapter=&mode=quick&count=10` |
| Read or print a chapter's lesson summary | tab + open chapter + link = 3, then Print = 4 (browser dialog) | `/learn/summary?subject=&chapter=` |
| Search a lesson or chapter | type 2+ letters, then 1 | results list on the same page |
| Choose a subject | 1 (tab) | same page |
| See marks | 1 | `/progress` |
| Take a full mock | 1 | `/dashboard?mode=full` |
| Set usual study time or subjects | open Preferences (1), change (1+), Save (1) = 3 | `PUT /api/study/preferences` |
| Pro: weekly plan | open (1) + 2 taps per day cell + Save | same |
| Pro: mixed revision of chosen concepts | open (1) + tick concepts + Start (1) = 3+ | `POST /api/study/runs {mixed}` |
| Open Key cards home | 1 (row) | `/cards` |
| Open a chapter's Key cards | 2 (row + chapter); 3 if another subject tab | `/cards/{key}` |
| Study that chapter's cards | 3 (row, chapter, Study tab) then Show answer + rating per card | `?mode=study` |
| Last look at the Must-know cards | 3 | `?mode=last` |
| Add a chapter's cards to Revise | 3 (row, chapter, key) | `POST /api/keycards/add` |
| Choose "Your part" (Accountancy) | 2 (row, then a part button; the subject tab first if not Accountancy) | `PUT /api/me/subject-options` |
| Revise Key cards due | 2 (Key cards row, `Revise now`) | `/review/revise` |
| Print a chapter sheet (Pro) | 3 (row, chapter, Print) | `window.print()` |
| Report a card | menu (1) + item (2) + text + send | `POST /api/keycards/report` |
| Pick a time and get a mix of cards and questions | NOT POSSIBLE from Learn | the nearest thing is Today's 10/20/30 plan |
| See what is where (a map of all lessons, cards, practice for a chapter) | NOT AVAILABLE; "All chapters" is closest but lists only lessons, and Key cards are on another page | |
| Revise specific cards of one's choosing (Key cards) | Add a whole chapter (3) or, Pro only, a single card from its menu | |

## 9. Weakness-led versus student-chosen

Weakness-led (steered by wrong answers):
- The one big key at the top (kind `mistakes` outranks `next`).
- The section "Where you lose marks" (appears only with papers; ordered by marks lost).
- The red `−n` on chapter rows.
- The lede "Short lessons on the ideas behind your mistakes."
- The side text "Shows which chapters still cost marks".
- Which subject tab is open first (follows the lesson on the big card, until the student taps a tab).
- The Pro-only reason line in a Key cards deck and the state word ("Needs work").
- Practice panel "Next lesson" uses the same pick.

Student-chosen (but buried): subject tabs, All chapters list, search, Study preferences, the Key cards row and all of Key cards (subject, chapter, mode), Revise now, mixed revision (Pro), full mock. The student never picks a goal, a length of time or "what I want to do" (learn a new idea, memorise lines, recap before the exam, test myself).

## 10. Problems seen (code and UX), each with where

1. Key cards entry is a quiet row between two big things, one level under Practice -> Learn. `StudyLibrary.jsx:90`, `KeycardsLinks.jsx:13-25`; shot `entry-learn-row-390-night.png`. (LK1)
2. Probable cause of "Your part" glitch (LK2): after the PUT succeeds, `choose()` runs `refreshHome()` then, in `finally`, `setPending(null)` immediately (`KeycardsHome.jsx:80-85`). `current = pending || subject.option` (`:77`) then falls back to the OLD saved option (or none) until the refetch lands, so the highlighted choice snaps back, then jumps again when the new body arrives; the chapter list then loses one part's units and the new rows play a 260 ms staggered rise (`.kc-row` animation, `keycards.css:111`). With nothing saved before, no choice shows as chosen during the gap. If the refetch fails, the picker stays on the old state with no error. Also: `useKeycardsHome` keeps the stale body (`api.js:44-56`), there is no optimistic option. Not reproduced.
3. Learn hub tab flip: `subject = chosen || pick?.unit?.subject || firstSubject` (`StudyLibrary.jsx:46`). Before the review read ends the selected tab is `firstSubject`; when it ends it switches to the picked lesson's subject and the panel (`key={subject}`) remounts, so a student can see the subject change under their finger. Likely a second source of "glitches and shuffles". Not reproduced.
4. Mode flash: `ChapterDeck` starts in `'read'` and sets the real `?mode=` one microtask later (`ChapterDeck.jsx:272-275`), so a link to `?mode=study` briefly renders Read.
5. Two subject lists and two orders: Learn shows 4 fixed subjects alphabetically (`StudyLibrary.jsx:24`); Key cards shows the student's own subjects in their own order, including Biology and Political Science that Learn has no tab for (`keycards.js:246`). A science student sees Key cards but an unrelated four-subject Learn.
6. Two vocabularies and three names: "Learn", "Concepts" (still in `StudyRun.jsx:67,77,119`, `StudyWorkspace.jsx:63`, `StudyChapterSummary.jsx:149`, `studyCopy.js:221`, `learn/page.jsx` loading text), "lessons", "Key cards", "cards in Revise", "recall cards", "Lock it in".
7. Study's end key and the deck's "Add chapter to Revise" disagree: the key says it adds only the Must-know cards for Pro (`ChapterDeck.jsx:337`) but Study puts EVERY card the student rates (including Good-to-know) into Revise (`:174`, review route). Pro "Study" also works over all open cards while Last look is Must-know only.
8. "Must-know" on 67.5 % of cards (section 6) is a chip on every header; it carries real meaning for Free taste and Pro add-set, so it can't just be hidden without changing those rules.
9. The Read view is one very long scroll (14,688 px tall for a 26-card chapter on a phone, 5,690 for Free Accounting Ratios); the mode tabs scroll away; on a phone the chapter stats and Add key come after the tabs and before the list; there is no progress, jump, or "where am I".
10. Learn has no place for a time. The only time controls are "Usual study time" in the collapsed Preferences (affects Today) and Today's own 10/20/30. A Learn session cannot be sized.
11. Learn's search does not cover Key cards; Key cards has no search at all.
12. Only 21 lessons for 54 chapters; every other chapter row says "No lesson yet. Practice ready", so the hub looks emptier than the content actually is (Key cards cover 73 chapters).
13. Print: no watermark; `window.print()` of an invisible portal; lesson summary and chapter summary print are free and unmarked; the Study end screen does not offer print (the print key is in the chapter summary column, hidden on phones in Study and Last look by `keycards.css:372-374`).
14. Next-action is one fixed pick, and for a brand-new commerce student it is an English vocabulary lesson, regardless of their chosen subjects.
15. Heavy page read: Learn calls `/api/me/review` (the repo's heaviest read) and `/api/keycards` on every open, plus the catalog; skeleton states cover all three but the key pops in late.

## 11. Open questions (for the main session)
- Is Key cards `STUDY_CONTENT_ENABLED`-independent? Yes: Key cards flag is `KEY_CARDS_ENABLED` (`keycards.js:22`), Learn's flag is `STUDY_CONTENT_ENABLED`; Key cards can be on while Learn is off, then the only way in (the Learn row) disappears. The nav hides Learn when study is off (`AppLayoutClient.jsx:321`), so Key cards would have no door at all.
- Should the 4 Concept subjects follow the student's own subjects (and add Biology and Political Science, which have only cards)?
- What is the owner's intended meaning of "Fitzmeen downloading" (his note says to confirm: probably "preventing" or "fine with downloading but with our mark")?
