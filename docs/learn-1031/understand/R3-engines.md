# R3: Engines that could feed a time-boxed "chapter session" (Key cards plus MCQs)

Read-only map, 31 Oct 2026. Web code root `W` = `C:/Users/atish/Desktop/mockmob copy/wt-1031-keycards-web` (all paths below are under it unless they start with `app:`). The Android app is `wt-1031-keycards-app/flutter_app`; it mirrors the web rules (a port), so this report covers the web engines and notes the app mirror at the end. Nothing was changed, started or committed.

The one-line answer: **there is no engine today that takes "this chapter, N minutes" and returns a lined-up mix of Key cards and questions.** Every ingredient exists, but in four separate engines with four different schedulers, three different per-item time assumptions and three different entitlement systems. Revise (the only place cards and questions already play in one run) is a global "due today" queue with no chapter filter and no minutes input. Section 12 lists what is reusable and what is missing.

---

## 0. The numbers a designer needs first (seconds per item, as the code assumes)

| Item | Seconds | Where |
|---|---|---|
| Key card | **15** (`minutesPerCard: 0.25`), rounded up to whole minutes | `data/keycards.js:12` and `:185` `cardMinutes`; `src/components/revise/reviseQueue.js:30` `KEYCARD_SECONDS = 15`, `keycardMinutes` `:31`; app `keycards_rules.dart:17,31` |
| Revise question (the same wrong question again) | **40**, total rounded UP to the next 5 minutes | `data/revise.js:25` `secondsPerCard: 40`, `:26` `minuteStep: 5`, `minutesFor` `:55-58` |
| Quick practice MCQ | **60** (`durationPerQuestionSec: 60`) | `data/test_modes.js:19`; Start sheet `quickMinutes = round(10*60/60) = 10` (`src/components/start/startModel.mjs:137`) |
| Full mock / NTA question | 72 (3600 s / 50) | `data/test_modes.js:57,73` |
| Smart practice question | 45 easy, 60 medium, 90 hard | `data/test_modes.js:39` |
| Concept recall card (study engine) | 30 in the Learn library (`ceil(min(due,10)*0.5)` min, `src/components/study/StudyLibrary.jsx:67`); 36 after a lesson (`ceil(available*0.6)` min, min 2, `StudyRun.jsx:149`); counted as a 40 s slot inside Revise (`mergeQueue` `minutesFor(total - kc.length)`, `reviseQueue.js:84`) | three different guesses for one thing |
| Concept lesson | 5 to 7 min (`estimatedMinutes`, `data/study/pilot.json`), plus `LOCK_IN_MINUTES = 2` for its cards (`data/study/lesson_map.mjs:14`) | |
| Repair of one mistake | about 3 min each, rounded up to 5, at least 5 (`repairMinutes`, `src/lib/today/move.mjs:52`) | |

Plain arithmetic on those assumptions for the three durations the owner implied (5, 10, 20 minutes), if a session used Quick-practice timing for MCQs (60 s) and 15 s for cards:

| Box | Seconds | Example mixes that fit |
|---|---|---|
| 5 min | 300 | 8 cards (120) + 3 MCQ (180); or 20 cards only; or 5 MCQ only |
| 10 min | 600 | 16 cards (240) + 6 MCQ (360); or 12 cards (180) + 7 MCQ (420) |
| 20 min | 1200 | 30 cards (450) + 12 MCQ (720); Quick practice itself caps at 20 questions |

With Revise timing (40 s per question) the same boxes hold about 50 percent more questions. Real behaviour is unmeasured for cards: there is no stored per-card dwell time anywhere in `key_card_reviews` (it stores `scheduled_days` and `elapsed_days`, not seconds on screen). The only measured question time is paper telemetry (`data/time_decisions.js`, `data/paper_trace.js`), which is for papers, not practice-by-chapter.

**Free versus Pro changes these numbers sharply.** On Free, Key cards allow only **10 reviews a day in total** (`KEYCARD_RULES.free.reviewsPerDay`, `data/keycards.js:9`), so 10 cards is 2.5 minutes and the 11th rating of the day returns 402. Section 9 has the full table.

---

## 1. Quick practice by chapter (the only chapter-scoped question engine)

**What it is:** Quick practice is the `quick` mode of `TEST_MODES` (`data/test_modes.js:6-26`). It is the only mode allowed to narrow to chapters (`allowChapters: true`, `fineTuneScope` `:96-99`; a request with chapters on any other mode is refused `CHAPTERS_NOT_ALLOWED`, `fineTuneViolation` `:103-109`).

**Count and price (owner D65, 18 Oct):** counts 5, 10, 15, 20 (`countOptions`, `:18`; default 10). One credit per question (`creditPerQuestion: 1`, `practiceCreditCost` `:115-124`: 5 to 20 credits). Pro: free. DB spend actions `attempt_5`, `attempt_10`, `attempt_15`, `attempt_20` (`practiceCreditAction` `:128-133`). Max 20 questions, so max 20 minutes (`QUICK_PRACTICE_MAX`, `data/goal_minutes.js:14`).

**Free allowance:** one 10-question Quick set a day is included (`allowanceKindFor` returns `daily_practice` for `quick` and count 10, `data/practice_quote.js:11-17`; period is the IST day, `allowancePeriod` `data/learning_engine.js:157-163`). Also a 5-question baseline per launch subject once (`baseline:<subject>`, purpose `baseline`) and a first full mock per subject (`data/first_full_mock.js`). Any other count, or the second set of the day, is 1 credit a question. The included set only counts when the chapters are narrowed or not; the allowance is per count 10, not per chapter.

**How a session is created (web):**
1. Quote (read only): `GET /api/practice/quote?subject=&mode=quick&count=&purpose=` (`src/app/api/practice/quote/route.js:23-76`, rate limit 120). Returns `{ state, launchable, reasonCode, reason, subject, mode, count, durationSec, durationEstimated, entitlement, inventory:{state, ordinaryCount}, allowance:{kind,state}, creditCost, creditBalance, upgradeHref, idempotencyToken, expiresAt (60 s) }` (`buildPracticeQuote`, `data/practice_quote.js:38-123`). It checks only the SUBJECT count against `n`, not the chapter's count (`ordinaryCount >= n`, `:79-92`).
2. Start: `POST /api/sessions` with `{ subject, mode:'quick', count, chapters:'a,b' or chapter, generationKey (12 to 100 chars), difficulty? (Pro only), purpose?, tonightKey?, tonightMinutes? }` (`src/app/api/sessions/route.js:46` to `startPractice`, `src/lib/server/practiceSessions.js:32-139`). Up to 12 chapter names (`:47`), each validated with `isValidTopSyllabusPair` and canonicalised (`:49-50`); the chosen syllabus option (Accountancy AFS/CAS, Maths B1/B2) filters the pool (`loadSyllabusOption` `:72`).
3. The server picks the questions (`Database.getQuestions(subject, count, { mode, chapters, difficulty, requireEvidence:false, syllabusOption, ... })`, `:81-86`; pure picker `data/practice_pick.js`, ranking in `data/mock_question_selector.js`). If fewer than `count` come back for the chosen chapters it throws `INSUFFICIENT_PRACTICE_CONTENT` (`:88`) and nothing is charged. Difficulty mix for quick: easy 0.40, medium 0.40, hard 0.20 (`test_modes.js:20`); `recencyLimit: 3`, `maxPerConcept: 2`.
4. Charge after a full set exists: device-held ticket (`sealPractice`, AES-GCM, `data/practice_ticket.js`) or durable row via RPC `start_learning_session` (`LEARNING_SESSIONS_ENABLED`); response is `publicSessionView(row)` with questions (no key) and `meta.sessionTicket`.
5. The run page is `/test?subject=&count=&mode=quick&chapters=` (`src/app/(app)/dashboard/DashboardPageClient.jsx:443` `launchHref`). The clock is the whole paper: `expires_at = created + resolveDurationSec(mode, questions)`, 60 s a question (`practiceSessions.js:102`).
6. Finish: `PATCH /api/sessions` (`finishPractice`, `practiceSessions.js:141`) scores the paper in one go and writes the attempt row and `user_question_progress`.

**Per-answer feedback exists but is off and unused by web:** `POST /api/sessions/{id}/check {qid, answer, sessionTicket}` (`src/app/api/sessions/[id]/check/route.js`, `src/lib/server/sessionCheck.js`) reveals the key during quick or smart practice, gated by env `SESSION_CHECK_ENABLED === '1'` (route line ~22: otherwise 403 `check_not_available`). No web component calls it (grep of `src/components` finds nothing); not recorded in STATUS/NOW whether it is on in production. The first check is final and replaces the submitted answer at finish.

**The Start sheet and its "time options":** the Start sheet (`src/components/start/StartSheet.jsx`, model `startModel.mjs`) has NO time or count chooser. It lists rows that each open `/dashboard` set up for the session (`startRows` `startModel.mjs:~340-370`): Quick practice (`count 10`, "about 10 minutes"), Full mock (50 q, 60 min), NTA mode, "By chapter" (opens Practice with `?pick=chapters`: "Pick {Subject} chapters, then 10 questions"), Smart practice (15 q, Pro), "Choose your own". Only the Practice page itself (`DashboardPageClient.jsx:708-712`) has the count `Segmented` (5/10/15/20, hint "About {minutes} minutes") and the chapter picker (`ChapterPicker.jsx`, `chapterGroups.mjs`, link params `chapter`, `chapters`, `pick=chapters`, lines 286-292). Today's chooser is separate (section 11).

**Reusable for a chapter session:** the quote/start/credit/allowance plumbing, chapter canonicalisation, syllabus option, the `count` of 5/10/15/20 as the MCQ half. **Missing:** (a) it is a whole-paper, scored, credit-priced sitting, not an item you can interleave with cards; (b) no per-card interleave hook, no way to start it with fewer than 5 or in minutes; (c) quote checks subject inventory not chapter inventory (thin chapters fail only at start); (d) per-answer feedback not wired in web.

---

## 2. The Revise queue (the only engine that already mixes cards and questions)

**Files:** pure rules `src/components/revise/reviseQueue.js` (192 lines) and `data/revise.js`; server `src/lib/server/revise.js`; routes `src/app/api/me/revise/route.js` and `.../answer/route.js`; hook `src/components/revise/useRevise.js`; run UI `src/components/revise/ReviseRun.jsx`; badge store `src/lib/reviseDue.js`.

**Five sources, one run, one progress line** (`reviseQueue.js:1-20`, `SOURCES` `:27`, `KINDS` `:28`):
1. `questions`: wrong answers due today (`revise_cards`, mode `question`), same question again.
2. `again`: repaired mistakes due again (mode `again`, key hidden). A question due in 1 and 2 plays ONCE, as `again` (`mergeQueue` `:55-57`).
3. `checks`: a pending "Check it held" (a NEW question on the rule of a repair, from the day after the repair; `src/lib/server/revise.js:198-200`).
4. `cards`: concept recall cards due (study engine, played inside Revise by `ConceptRun`, `ReviseRun.jsx:285`).
5. `keycards`: Key cards due, after everything else, 15 s each, obey their own limits (never the cap below).

**Order and caps:** questions and repaired mistakes oldest due first, then lower box (`byDue` `reviseQueue.js:39`), then checks, then concept cards (max `CARD_CAP = 5`, `:26`), then Key cards (`:74`). The student's daily cap is **5 or 10** questions (`REVISE_RULES.capChoices`, `data/revise.js:23`; default 10; stored per device `mm.revise.cap`, `useRevise.js:201-206`), less what was answered today (`todaysQueue` `data/revise.js:81-88`). Checks are always included. `mergeQueue` returns `{ items, counts, total, minutes, unknown, dropped }` (`reviseQueue.js:51-85`); `minutes = minutesFor(total - kc.length) + keycardMinutes(kc.length)` (`:84`), i.e. 40 s per non-Key item rounded up to a 5-minute step plus 15 s per Key card rounded up to a minute.

**Endpoints:**
- `GET /api/me/revise?cap=5|10[&queue=1]` (`route.js:21-55`, rate limit 60). Without `queue=1` it is the plain v1 body (Review's row, Today); the Key cards counts ride on it as `keyCards:{due,today,minutes}` (`revise.js:144-149`). With `queue=1` it adds `queue` (version 2): `{ today, cap, items[], counts{questions,again,checks,cards,keycards?,back}, total, minutes, unknown, dropped, cardsAvailable, head, mix, boxes[4], rotation, nextDay, nextDayLabel }` (`composeQueue`, `revise.js:157-212`). No chapter or subject parameter exists. No minutes parameter exists. `?source=cards|again|questions|checks|keycards` is a client-side filter (`filterSource`, `reviseQueue.js:135-151`).
- `POST /api/me/revise/answer?cap=` `{ questionId, choice }` grades on the server and moves the card (`answerRevise`, `revise.js:222-272`). Returns `{ ok, correct, keyIndex, explanation (max 1500 chars, stored, no AI), outcome:'right'|'wrong'|'done', box, retired, dueDay, dueLabel, line }`. 409 `not_due`, `cap_reached`, `key_changed` (the card is retired if the key hash changed, `:249-252`), `question_unavailable`. Writes only `revise_cards`: no attempt row, no `user_question_progress`, no credits, no accuracy movement (`revise.js:8-9`, copy `revise.fine`).

**Scheduling (questions): a 4-box Leitner ladder, India days** (`data/revise.js:19-28`, `gradeCard` `:64-70`): box 1 due 1 day after a wrong answer, box 2 after 3 days, box 3 after 7, box 4 after 21. A right recall moves up one box; wrong goes to box 1, due next day; a right recall in box 4 retires the card (`outcome 'done'`). Seeding: on every GET, up to `seedMax = 200` newest wrong answers in `user_question_progress` (`last_correct=false`, `last_selected_key` not null) become cards in box 1, due the day after the wrong answer; a question answered wrong again after its card last changed is reset to box 1 (`planSeeds` `:107-127`, `seed` in `revise.js:77-98`). Cards of a still-open Mob paper are held back (`readHeldMobPapersSafe`). A card whose question is not `eligibleQuestion` (live, not deleted, not `disputed`, key readable, 2 or more options; `revise.js:39-42`) is skipped and the next takes its place.

**Mix of Key cards and questions:** already done in one run, in a fixed order (questions, repaired, checks, concept cards, Key cards), never interleaved. The run UI (`ReviseRun.jsx:393-515` `RunView`) shows `ticks` per item, a mix line (`mixParts`: "5 questions back, 1 Check it held, 2 concept cards, 6 Key cards") and plays each by kind: `QuestionCard` (`:159`), `CheckCard` (`:207`), `ConceptRun` (`:285`), `KeyCardRun` (`:344`, `KeyCardPlayer mode="revise"`). Copy strings shown to students: head "`{n} due today, about {m} minutes.`" (`COPY.revise.run.head`), "Nothing due today", position "`{k} of {n}`", kind lines "A question you got wrong", "A mistake you repaired", "Check it held: your Q{n} rule", "A card from {lesson}", "Key card"; foot "Free. Not counted in your marks or accuracy."; end "`{r} recalled, {w} come back tomorrow`".

**Key cards inside the queue:** `queue.readKeyCards = keycardsService().reviseSource(userId)` (`route.js:33`; `keycards.js:494-499`) which calls `dueCards(userId, {limit: 20})`. So at most **20** Key cards per Revise run, within Free's allowance. Absent when `KEY_CARDS_ENABLED` is not `'true'`.

**Reusable:** the whole run shell (ticks, mix line, per-kind players, server-confirmed answers, summary) and `mergeQueue` itself are directly reusable for a lined-up chapter session; items already carry `kind` and per-kind players already exist. **Missing:** chapter or subject scoping (the revise queue is global, all subjects); a minutes target (cap is questions only: 5 or 10); picking NEW questions of a chapter (Revise only replays the student's own wrong answers); picking Key cards by chapter (queue = global due plus global new); interleaving (fixed order).

---

## 3. Concepts lessons and study runs

**Content:** 21 published pilot lessons in `data/study/pilot.json` (v2) and 86 recall cards (`data/study/release.json`), authored in `data/study/authored/*.mjs`. Subjects: English, Accountancy, Business Studies, Economics only (`STUDY_SUBJECTS`, `data/study_engine.js:3`). Per chapter: English Vocabulary 6 lessons, one each for the other 14 chapters, e.g. Accountancy "Change in Profit Sharing Ratio" (1), "Admission of Partner" (1), "Share Capital" (1), "Accounting Ratios" (1). **There is no lesson for "Accounting for Partnership: Basic Concepts" (key `accountancy.partnership-fundamentals`).** Each lesson: `{ id, version, subject, chapter, conceptId, order, title, summary, estimatedMinutes (5 to 7), skill, objectives[], examLink, sourceRefs[], blocks[] }`; blocks 4 to 9 per lesson: explanation, steps, worked_example, mistake (reading) and `knowledge_check` items of type `choice`, `numeric`, `ratio`, `text` (labelled "Quick check, not scored"; `BLOCK_LABEL` `studyCopy.js:9`).

**Flags:** `STUDY_CONTENT_ENABLED === 'true'` for lessons; `STUDY_RECALL_ENABLED` for recall cards; `STUDY_GUIDED_PLAN_ENABLED` for the guided plan (`src/lib/server/study.js:13-14`, `learning.js:63,102`).

**Endpoints:** `GET /api/study/catalog` (`studyCatalog`, `study.js:104`: `{ units[] with status/read/inProgress/cardCount/memory, queue{dueCount,overdueCount,newAllowance,availableCount,newCount,pausedNew}, nextUnit, active, preferences, progress, subjects }`); `GET /api/study/units/{id}` (`studyUnit` `:108`, records an exposure; includes `siblings`, `recall{available,due,newAllowance,unseen,newCardsPerDay}`); `POST /api/study/runs {mode:'learn'|'recall', unitId?, unitIds?, mixed?, requestKey}` (`startStudyRun` `:179-225`); `GET /api/study/runs/{id}`; `POST /api/study/runs/{id}/events {type:'continue'|'answer'|'reveal'|'rate', itemId, value?, rating?, assisted?, expectedRevision, requestKey}` (`studyEvent` `:226`, state machine `studyTransition` in `data/study_engine.js:75-108`); `GET /api/study/summary?subject=&chapter=` (printable chapter summary, reading blocks only); `GET/PUT /api/study/preferences`. Every event is idempotent on `requestKey` and revision-checked (409 on conflict).

**Recall run:** `recallQueue(cards, states, at, introducedToday, limit=10, reviewCards)` (`study_engine.js:24-32`): due first (oldest), then unseen (`NEW_CARDS_PER_DAY = 5`, paused when more than 20 cards are over a day overdue), at most `limit` = **10** per run. New cards require the lesson to be read (`taughtRecallCards` `:9-12`, error `LESSON_NOT_READ`). A card can show a different form each review (meaning, gap fill, spelling, synonym) via `cardItem` variants `:120-125`. Ratings 1 to 4 (Forgot, Hard, Got it, Easy; `RATINGS` `studyCopy.js:26-31`); a checked wrong answer rates 1, assisted right 2, right 3 (`study_engine.js:97`). Scheduler: FSRS `request_retention 0.90`, no horizon cap (`data/study_scheduler.mjs`, `SCHEDULER_VERSION 'fsrs-5.4.2-retention-090-v1'`). After 3 lapses on one card the run says "You've missed this card a few times. Reread its lesson".

**Custom mixed recall (`mixed: true` plus `unitIds`, up to 20 lessons) is Pro only** (`startStudyRun`, `study.js:~186`, `PREMIUM_REQUIRED`; UI `StudyWorkspace.jsx:114-118` and the "Study preferences and weekly plan" fold, `:83-135`). This is the existing, buried, closest thing to "pick concepts, get a mixed run". It mixes recall CARDS across lessons only: no MCQs, no Key cards, no minutes.

**UI:** `/learn` is `StudyWorkspace` -> `StudyLibrary` (`src/components/study/StudyLibrary.jsx`): one volt "next lesson" pick (`conceptsPick`, `data/study/concepts_pick.mjs:59-100`: finish active, then costliest chapter with open mistakes from `/api/me/review`, then catalog `nextUnit`, then "practise"), a "Revise N concept cards" row, `LearnKeycardsRow` (`KeycardsLinks.jsx`, the way into Key cards: a single row), search, a 4-subject tab row (not the 6 Key cards subjects), "Where you lose marks" (max 4 rows, `LOSE_ROWS`), and an "All {Subject} chapters" accordion with "Practise this chapter" (`practiceHref(subject, chapter)` = `/dashboard?subject&chapter&mode=quick&count=10`) and "Read or print the chapter summary". End of a lesson (`LessonDone`, `StudyRun.jsx:123-163`): "Next: lock it in" (recall cards, "about N minutes"), "Then: apply it" (Practise {chapter}). End of recall (`ReviewDone` `:165-185`).

**Reusable:** idempotent run state machine and endpoints, FSRS cards, `GET /api/study/units/{id}` for per-lesson card counts, `studyChapterSummary` for a "what to read" source. **Missing:** lessons cover only 15 chapters and 0 of the owner's example chapter; no chapter-keyed API (units are filtered client-side by `chapter` name); no MCQ mix; the 4 study subjects differ from the 6 Key cards subjects; two parallel "card" systems (concept recall cards and Key cards) with different schedulers and ratings.

**Learning episodes (pathway probes, repair, checks) are blocked.** `data/learning_engine.js` and `src/lib/server/learning.js` implement the episode (`investigating`, `repairing`, `immediate_check`, `delayed_check_1`, `delayed_check_2`, `maintained`; 3 probes max, at least 3 independent check families, checks at least 1 day then 3 days then 7 days apart) but `data/recovery_pathways.json` has `"state": "blocked_sources"` and `pathways: []`, so `releasedPathways()` returns nothing (`learning.js:22-30`) and no episode can start (`startEpisode` throws `PATHWAY_AWAITING_SOURCES_AND_CALIBRATION`). The eight candidate concepts (`CONCEPT_BLUEPRINTS`, `learning_engine.js:7-16`: Accountancy sacrificing/gaining, revaluation; Economics national income, nominal/real; BST delegation, planning/controlling; English inference, main idea) are not served. Do not count episodes as a source for a chapter session.

**Repairs and the pending "Check it held"** (the nearest working equivalent of a repair loop): `src/services/recovery/*`, `data/repair_check.js`; played inside Revise as a `check` item via `/api/recovery/check` (`ReviseRun.jsx:207-283`, `data/repair_check_client.mjs`). Costs 1 credit per repair (Today copy "aiEach"); checks are free in Revise.

---

## 4. Key cards review RPC and scheduling

**Rules file:** `data/keycards.js` (254 lines, pure). Scheduler: `ts-fsrs` with `request_retention 0.9`, `enable_fuzz false`, `enable_short_term false`, `maximum_interval` = days from now to the exam horizon `2027-05-15` (`KEYCARD_RULES.examHorizon`, `schedule()` `:127-147`, belt-and-braces cap `:135`). Ratings: `Missed 1`, `Got it 3`, `Easy 4` (no Hard; `RATINGS` `:17`); UI labels "Missed", "Got it", "Easy", keys 1/2/3 (`kinds.js:39-43`). Modes: `revise`, `study`, `last_look` (`MODES` `:18`). `last_look` is logged and never moves the schedule and uses no allowance (`keycards.js:380-387`); a review older than the card's last one is logged as `late: true`, not scheduled (H2).

**Endpoint:** `POST /api/keycards/review { cardId, rating (1|3|4), mode, clientReviewedAt }` (`review()` `src/lib/server/keycards.js:356-410`) -> RPC `key_card_review(...)` (`supabase/migrations/20261031140000_key_cards.sql:93-182`, one transaction: replay check on `(user, card, client_key)`, review row, state move guarded by `p_expected_reps`, allowance claims). Responses: `{ ok, next:{due_at, interval_days}, today:{due,newLeft,reviewsLeft,minutes} }`; replay `{ok, replay:true}`; logged `{ok, late?}`; 409 `REVIEW_CONFLICT`, `CARD_SUSPENDED`; 402 `PRO_REQUIRED` with `reason` `keycard_reviews` (day's 10 used), `keycard_new` (day's 5 new used), `keycards` (a card Free cannot hold). Rating a card never added creates its state (`added_from` is `mistake` if mode `revise`, else `manual`, `keycards.js:394`), so Study ratings add the card to Revise on the spot (the page then flips "Add chapter to Revise" to "In Revise", `ChapterDeck.jsx:~120-170`).

**Queue (`dueQueue`, `data/keycards.js:165-182`):** 1. due cards (reviewed before, `due_at <= now`): Must-know first, then oldest due, then id; 2. new cards (added, never reviewed) in book order, chapter by chapter in syllabus order, up to the new allowance; new cards pause while more than `overduePauseNew = 40` are overdue (`:174`); suspended and unpublished cards skipped; default `limit 20`. `GET /api/keycards/due?limit=` (1 to 50; `dueCards` `keycards.js:335-347`) returns `{ cards:[{...card, state:{reps,lapses,due}}], today }`. **No chapter, subject or minutes parameter.** The server can already read per-chapter state rows (`loadStates(userId,{subject,chapter})`, `:183-188`) but no route passes `chapter` to the due queue.

**Counts (`today()`, `keycards.js:217-224`):** `due` = overdue count; `newLeft` = `min(newLeft, reviewsLeft)` (Free: 5 minus new used; Pro: 15 minus new used; `KEYCARD_RULES.pro.newPerDayChoices [10,15,25]` is declared but only the default 15 is used, `keycards.js:220`: the choice is not wired); `minutes = cardMinutes(playable)`.

**Deck and add:** `GET /api/keycards/deck?chapter=<key>` -> `{ chapter, cards (open cards whole, locked as stubs {id,kind,label,locked:true}), counts:{total,mustKnow,locked}, added[] }`; `POST /api/keycards/add {chapter}` or `{cardIds (max 100), from?:'mistake'}` -> `{ added, today }` (Pro: every Must-know card of the chapter; Free: the taste cards only).

**Reusable:** the review RPC, FSRS scheduling, `dueQueue`, `deck`, `add`, `memoryShare`, the player `KeyCardPlayer` (`src/components/keycards/KeyCard.jsx:197`, props `card, mode, position, active, detail, onRated, onLimit`; Space/Enter reveals, 1/2/3 rate; stamps one `clientReviewedAt` per card for idempotent retry). **Missing:** a chapter filter on the due queue; a way to pick cards in a chapter for a session without adding them all; card-to-question lookup (below).

---

## 5. Question-to-card links and "The line you needed"

**Data:** `data/keycards/links/<subject>.json` is `{ [questionId]: [cardId, ...] }` (one to two card ids each, 1.2 to 1.7 average). Sample key: `"00668b15-bfad-42ea-ae84-ae6a715d80c2": ["kc.accountancy.debentures.def-secured-debentures", "kc.accountancy.debentures.def-unsecured-debentures"]`. Loaded by `loadDecks` (`keycards.js:48-79`) per subject, served from files in the bundle (no DB egress). Counts across the 6 subjects: Accountancy 1,072 linked questions, Business Studies 267, Economics 296, English 155, Political Science 119, Biology 235 (about 2,144 total; some cards are shared). The link direction is question -> cards only. **There is no card -> questions index and no API for it**; building one means inverting these files (cheap, in memory).

**Coverage is very uneven (computed from the files):** per chapter the number of cards that have at least one linked question, and the number of linked questions. Accountancy: Partnership Fundamentals (the owner's example, "Accounting for Partnership: Basic Concepts") 46 cards, 33 Must-know, **9 cards linked to 11 questions**; Admission of Partner 53 cards, 16 linked, 159 questions; Change in Profit Sharing Ratio 8 cards, 4 linked, 136 questions; Retirement and Death 65 cards, 10 linked, 16 questions; Dissolution 59 cards, 17 linked, 20 questions; Goodwill 39 cards, 11 linked, 11 questions; Financial Statements of Company 85 cards, **2 linked, 3 questions**; Analysis of Financial Statements 16 cards, 1 linked, 2 questions. Political Science chapters have only 3 to 13 linked cards and 4 to 15 questions each. Many questions point at the same few cards (Accountancy "Change in Profit Sharing Ratio" has 136 questions on 4 cards: template-style questions).

**"The line you needed":** `GET /api/keycards/line?questionId=` (`line()`, `keycards.js:412-440`): the student must have answered the question (`attempt_count > 0`), the question must not be in a held Mob paper; `lineNeeded()` (`data/keycards.js:220-234`) takes precomputed links first (max 2 cards, source `linked`), else a lexical fallback over the question's chapter's Must-know cards (a card matches when its quote shares at least `minShared 3` content words with the question stem plus explanation and at least `minScore 0.35` of the quote's words; top 2, source `matched`), else `{cards:[], source:'none'}`. Free gets `lineNeededPerDay = 3` distinct questions a day (allowance kind `keycard_line`, reference = question id; the same question again uses nothing), then 402 `keycard_line`. Pro unlimited. Web UI: `src/components/keycards/LineYouNeeded.jsx` (under a wrong answer on the paper result; "The line you needed", "Linked to this question" or "Matched by its words", "Add both to Revise", Free count left). Hidden when source is `none`, when Key cards are off, on read failure, and on 402.

**Reusable for a session:** `lineNeeded()` with `cardsById` is exactly the "after a miss, show the line" step of a mixed session; the link files give "this question tests these cards" (question -> cards) so a question can be paired with its cards, or a card with the questions that test it (after inversion). **Missing:** the reverse index; chapter-level coverage guarantees (some chapters have almost no links, so a "card then its question" pairing fails for them); the fallback matcher is weak for English (one or two word quotes).

---

## 6. Chapter state (Holding / Getting there / Needs work / Too few answers / Not started)

**Files:** `data/chapter_state.js` (121 lines, pure); `GET /api/me/chapters?subject=` (`src/app/api/me/chapters/route.js`, `keycards.js:452-482`, behind `KEY_CARDS_ENABLED`); the same state is embedded per chapter in `GET /api/keycards` (`overview`, `keycards.js:238-277`, field `state:{state,label,fading}`).

**How computed (the header comment `chapter_state.js:1-16` is exact):**
- Each question counts once, by its latest answer (`user_question_progress.last_correct`), `n = distinct questions answered`, `right = those whose latest answer is right` (`tallyChapters` `:34-53`). Rows with `attempt_count = 0` or null `last_correct` are not counted. Chapter names resolve through the syllabus (aliases ok, retired chapters skipped).
- `stateFor` (`:62-80`): `none` (label "Not started") when `n = 0` and no cards added; `thin` ("Too few answers") when `n < CHAPTER_RULES.minAnswers = 6`; else Wilson interval of `right` out of `n`: upper bound < 55 percent -> `weak` ("Needs work"); lower bound >= 65 percent -> `strong` ("Holding"); otherwise `mid` ("Getting there"). `fading` only for `strong`: quiet for 21 days (`fadingDays`) or, among added Must-know cards, FSRS retrievability >= 0.9 for fewer than half of them (`memoryShare`, `keycards.js:237-243`). Unknown (failed progress read) is `{state:'unknown', label:'Could not load'}`, never "Not started".
- Free students get `state`, `label`, `fading`, `marksLost`, `available:{questions, cards}` per chapter; Pro also gets `n`, `right`, `reason` ("7 of 12 right on the latest try at each question. Cards: 14 of 20 holding"), `memory:{holding, added, mustKnow}` (`chapterStates` `:102-120`). No percent is ever returned under `n = 6`, and the copy never says "mastered".
- Inputs outside question answers: only Key card state moves it, and only for `none` versus `thin` (added cards make a chapter not "Not started") and `fading`; Revise answers write nothing to progress, so they never move it; Explore answers DO write `user_question_progress` (`src/app/api/questions/[id]/interact/route.js:278-330`, `updateLearningProgress`), as do Quick practice and mocks.
- `marksLost` per chapter comes from `chapterRows(loadReviewRecord)` (`data/review_chapters.mjs`), optional.
- Per-chapter `available.questions` comes from the daily inventory snapshot (`publicInventory().chapterCounts[subject][chapterName]`, `src/lib/server/inventory.js`); it is stale up to a day and after the 31 Oct pulls some chapters are thin (NOW.md: Accountancy "Financial Statements of Company" 1 question, Political Science "Recent Issues and Challenges" 4).

**Known inconsistency:** `chapter_state.js:3-5` states it does NOT replace the other weak-chapter rules (`prepos_insights`, `mock_swot`, `review_chapters`, `learning_weak`, the analytics route). The Learn page's "Where you lose marks" (marks lost, `/api/me/review`), the Today move's "weakest chapter" (PrepOS insights) and Key cards' chapter state are three different definitions. `docs/brain/intel-1031/CHAPTER-STATE-ADOPTION.md` (in the repo it names) lists which surfaces should move to it.

**Reusable:** the state words, Wilson rule, `available` counts: enough to rank "which chapter next" or show a state chip on a chapter picker. **Missing:** state only exists behind the Key cards flag and route; n and right are Pro-only.

---

## 7. Today's plan and next-move logic (the 10/20/30 chooser)

**Layers:**
1. Learning plan: `GET /api/learning/plan?minutes=&subject=` (`src/app/api/learning/plan/route.js` -> `learningRecord`, `src/lib/server/learning.js:63-137`; pure `learningPlan` `data/learning_engine.js:177-219`). Priority: resume an active session, fresh delayed check due, immediate check, repair, repeated-miss investigation (pathways not released, so these episode branches do not fire), baseline (never fires without released concepts), else **ordinary practice**: `Start {count} practice questions`, `href /dashboard?mode=quick&count={count}`, `count/review = practiceFor(minutes)`.
2. Guided sequence (`STUDY_GUIDED_PLAN_ENABLED`): `guidedSequence(plan, study, minutes, goal)` (`data/study_engine.js:144-182`) returns steps in order resume session, resume study, fresh check/repair, "Review N due cards" (`/learn?recall=due`), "Learn: {nextUnit.title}", practice ("Practise {n} questions" with `&subject&chapter` of the next unit). Time is shared by `allocateMinutes(minutes)` -> `[recall, learn, practice]`: 10 -> `[2,3,5]`, 20 -> `[4,6,10]`, 30 -> `[5,10,15]`, other lengths half practice, three tenths a lesson, the rest recall (`data/goal_minutes.js:55-67`); each step capped (`RECALL_STEP_MAX 10`, `LESSON_STEP_MAX 25`, practice 20 questions, 3 extra sets for goals over 30 min). `practiceFor(m)`: count = `min(m, 20)`, review = `min(m - count, 30)` (`goal_minutes.js:49-53`): 10 -> 10 q, 20 -> 20 q, 30 -> 20 q + 10 min of review.
3. Today's one move: `buildMove` (`src/lib/today/move.mjs:88-250`), first match wins: resume, failed, dayOne (10 questions), check, returning (7+ days away), firstRepair, **revise** (when `revise.due > 0`), repair, firstMock, smart (Pro, first week), practice (the plan's practice aimed at the top chapter with marks open). `done` replaces the later ones once tonight is recorded. `alternatives()` (`:~255`) lists the other moves ("Something else": repair, Revise, Quick practice, another subject, full mock, NTA, Mob, Review).
4. The chooser: `fitMove(move, chosen)` (`move.mjs:~290-310`) refits the single move to a length: a repair/Revise move takes as many as fit (`floor(chosen/3)` repairs; Revise `min(due, chosen)` questions, i.e. 1 minute a question there), a practice move picks `count = chosen >= 20 ? 20 : 10` and for 30+ minutes adds `review = min(chosen - 20, 30)`. UI: `src/components/today/TodayMove.jsx:176-270` (length chip with 10/20/30 presets via `isPreset`, "More time" panel from `src/components/goal/DailyMinutes.jsx` for 1 hour, 2 hours, "your own"); state is `useToday().minutes`/`setMinutes` -> `?minutes=` on the plan read (`useToday.js:73-78`). Length bounds 5 to 999 (`isMinutes`, `src/lib/goalMinutes.mjs:42`), account value in `getDailyMinutes`/`PUT /api/me/goal`.

**What it never does:** it ignores Key cards (`buildMove` reads `revise.due` only; the Key card counts are summed only in the `TodayQueue` line, `src/components/today/TodayQueue.jsx:30-33`, and kept apart as `keyCards`, `dueAll`, `minutesAll` in `useToday.js:42-61`); it never builds a mix, only one practice set; it is weakness-led (top chapter by marks open, Revise due, open mistakes), which is the exact "just focusing on the weaknesses" the owner called confusing; it has no chapter input from the student; and its "minutes" for Revise is a rough `max(5, ceil(due/5)*5)`.

**Reusable:** `allocateMinutes`, `practiceFor`, `fitMove`, the length chooser UI and the 5-to-999 minutes store are the existing "pick a time" vocabulary (10/20/30 plus More); `alternatives()` is the existing "other options" list. **Missing:** a mix-aware allocator (cards plus questions by minutes); chapter-aware planning; Key cards in the plan.

---

## 8. Explore (the feed that could host a "10-minute chapter lesson")

`/explore` -> `DiscoveryFeed` (`src/components/feed/DiscoveryFeed.jsx`, `QuestionCard.jsx`). Reads `GET /api/subjects`, `GET /api/chapters?subject=` (units and chapters, `src/app/api/chapters/route.js`), `GET /api/questions/feed?subject=&chapter=&difficulty=&search=&limit=&offset=` (`src/app/api/questions/feed/route.js`, no sign-in needed; default 20, max 50; order score desc, created desc; `readablePracticeQuestions` filter) and `GET /api/learning/summary`. Filters shown: subject, chapter, difficulty. **The feed response includes `correct_answer` and `explanation`** (`feed/route.js:~120`: `correct_answer: r.correct_answer, explanation: r.explanation`), and the card grades on the client (`questionFeedback`, `data/explore_feed.js:21-27`), then records `interactWithQuestion(q.id, {interaction_type:'attempted', metadata:{selected_key}})` -> `POST /api/questions/{id}/interact` which upserts `user_question_progress` (`attempt_count`, `correct_count`, `last_correct`, `last_selected_key`, `last_attempted_at`). So Explore answers are free, unlimited, and DO feed chapter state and Revise seeding (a wrong answer in Explore becomes a Revise card the next day). The separate `GET /api/questions/explore` (ranked, public shape with NO key and no explanation, `exploreRowOut`, `explore_feed.js:34-64`) is not what the page uses. The only Free limit in Explore is the 25 saved questions (402 -> Upgrade sheet).

**Reusable:** a free, chapter-filtered, unlimited question source with an existing grading and recording path; the card UI. **Missing:** a session/timer concept, any Key card, chapter-first entry (it starts from Subject then Chapter listboxes), a server-graded no-key path that records progress (the key ships to the client today; Revise's `/api/me/revise/answer` is the only server-graded free path, but it needs a `revise_cards` row).

---

## 9. Free and Pro limits that shape any session

| Thing | Free | Pro | Source |
|---|---|---|---|
| Key cards open | first 5 Must-know cards per chapter (the taste, book order); the rest are locked stubs; chapter with fewer than 5 Must-know has a smaller taste; Good-to-know never in taste | all | `data/keycards.js:9,66-80,83-88`; fixture `data/keycards/fixtures/taste.json` |
| Key card reviews | **10 a day, counted across Study and Revise** | unlimited | `key_card_review` `p_review_limit` (`keycards.js:398`, SQL `:128-141`) |
| New Key cards a day | 5 | 15 (default; choices 10/15/25 not wired) | `keycards.js:220`; `p_new_limit` `PRO_NEW_COUNT_ONLY = 100000` counts only for Pro (`:37`) |
| "The line you needed" | 3 questions a day | unlimited | `KEYCARD_RULES.free.lineNeededPerDay` |
| Add chapter to Revise | taste cards only (up to 5) | every Must-know | `chapterAddSet` `:91-96` |
| Print chapter sheet | not offered (Pro only, `isPro && must.length`, `ChapterDeck.jsx:~340`) | yes (no watermark exists in `keycards.css:350-360`) | |
| Quick practice | 1 credit a question (5 to 20); 1 free 10-question set a day; difficulty filter Pro only | free | `test_modes.js`, `practice_quote.js`, `practiceSessions.js:60` |
| Revise questions | free, no credits, 5 or 10 a day | same | `data/revise.js` |
| Concept lessons and recall | free | custom mixed recall (`mixed:true`) and weekly plan Pro | `study.js:~186`, `studyCopy.js:49` |
| Explore | free, unlimited; 25 saves | more saves | `feed` |
| Repairs | 1 credit each | credits too (Pro does not make Mobi free, D157) | Today copy |

Consequence: a 10-minute Free chapter session of cards plus MCQs is bounded by (a) 10 Key card ratings that day, (b) 5 new cards, (c) 5 taste cards in that chapter, (d) 1 credit per MCQ beyond the daily 10-question set. A session design must show what is open before the press and degrade to "read it" or Explore questions rather than a hard 402 midway. Existing limit copy lives in `kinds.js:351-357` `limitCopy` and `ReviseRun.jsx:344-369` (skip the remaining Key cards and go on).

---

## 10. Card content facts that matter for the "Must-know on everything" complaint (LK13)

- 5,800 published cards across 6 subjects: Accountancy 868, Biology 1,394, Business Studies 900, Economics 1,193, English 349, Political Science 1,096 (`data/keycards/manifest.json`). **3,916 (67.5 percent) are `importance: "must"`.** Accountancy 618/868 (71 percent).
- The "Must-know" tag is drawn on every such card by `CardHead` (`src/components/keycards/KeyCard.jsx:173`, `kc-tag`), plus "Asked in N past papers" when `asked > 0`; **`asked` is 0 on every one of the 5,800 cards** (computed), so no card has real past-paper evidence.
- "Must-know" also drives behaviour: Last look shows only Must-know (`LastLookMode`), Pro "Add chapter" adds only Must-know (`chapterAddSet`), Free taste = first 5 Must-know, due ordering puts Must-know first (`mustFirst`, `data/keycards.js:44`), Print sheet only Must-know, "The line you needed" fallback only considers Must-know. Changing the label or the rule is a content/rule change, not only copy.
- Card kinds (counts per chapter vary): definition, term, key_line, list, difference, steps, types, formula, fact, example, entry; English: word, idiom, one_word, usage, rule. `blanks[]` marks cloze text (kinds `term`, `key_line`). Card shape: `{ id, v, subject, chapterKey, chapter, unit, kind, front, back, quote, blanks[], source:{kind:'ncert', book, code, chapterNo, page, section}, importance:'must'|'good', asked, tags[], order, note?, addedIn?, quoteParts?, section? }`. Example: `kc.accountancy.accounting-ratios.def-a-ratio` ("What is a ratio?", Accountancy Ch 5 p. 194). Deck files are SHA-256 checked against the manifest on load; a mismatch turns that subject off (`loadDecks`, `keycards.js:62-67`).
- Owner's example chapter "Accounting for Partnership: Basic Concepts" is the NCERT block of key `accountancy.partnership-fundamentals` ("Partnership Fundamentals", `data/cuet_syllabus.js:105`) and also of `accountancy.profit-and-loss-appropriation-account` (`:106`): 46 cards (33 Must-know, 5 kinds mostly definition 5, key_line 8, fact 21, list 5, term 2, difference 4, types 1), 10 with cloze blanks; no Concepts lesson.

---

## 11. Quick reference: every endpoint a chapter session could touch

| Purpose | Endpoint | Chapter filter? | Minutes/count param? | Key hidden until answer? | Writes progress? |
|---|---|---|---|---|---|
| Chapters with state, counts | `GET /api/me/chapters?subject=` (flagged) | gives all chapters of a subject | no | n/a | no |
| Subject home with chapters, `today` | `GET /api/keycards` | all chapters | no | n/a | no |
| Chapter's cards | `GET /api/keycards/deck?chapter=` | yes (chapter key) | no | n/a (cards have back) | no |
| Due or new Key cards | `GET /api/keycards/due?limit=1..50` | **no** | limit | n/a | no |
| Rate a card | `POST /api/keycards/review` | n/a | n/a | n/a | key_card_states, reviews, allowances |
| Add cards | `POST /api/keycards/add` | yes (`chapter` or `cardIds`) | no | n/a | key_card_states |
| Line for a missed question | `GET /api/keycards/line?questionId=` | derived from question | no | n/a | allowance (Free) |
| Questions of a chapter, quote | `GET /api/practice/quote` | **no (subject only)** | count | n/a | no |
| Questions of a chapter, start | `POST /api/sessions` | yes (`chapters`, up to 12) | count 5/10/15/20 | yes (ticket) | at finish |
| Per-answer check | `POST /api/sessions/{id}/check` | n/a | n/a | reveals on check | session_check_log; **flag `SESSION_CHECK_ENABLED`** |
| Questions list | `GET /api/questions/feed` | yes (`chapter` name) | limit 1..50 | **no, key in response** | on interact |
| Questions (no key) | `GET /api/questions/explore` | yes | limit | yes | no |
| Record an Explore answer | `POST /api/questions/{id}/interact` | n/a | n/a | n/a | `user_question_progress` |
| Revise queue | `GET /api/me/revise?cap=&queue=1` | **no** | cap 5/10 | yes | seeds `revise_cards` |
| Answer a Revise question | `POST /api/me/revise/answer` | n/a | n/a | yes | `revise_cards` only |
| Concept catalog | `GET /api/study/catalog` | client filters by chapter name | no | n/a | no |
| Concept lesson / recall run | `POST /api/study/runs` | `unitId` (lesson), `unitIds` (Pro) | recall limit fixed 10 | yes | `study_card_states` |
| Plan | `GET /api/learning/plan?minutes=&subject=` | subject only | minutes 5..999 | n/a | no |
| Daily goal | `GET/PUT /api/me/goal`, `getDailyMinutes` | | minutes | | |
| Review record (marks lost per chapter) | `GET /api/me/review` | all chapters | no | n/a | no |

---

## 12. Reusable versus missing for "pick chapter + pick 5/10/20 min, get a lined-up mix of cards and questions"

**Reusable as is**
1. `data/keycards.js`: `schedule`, `dueQueue`, `tasteIds`, `chapterAddSet`, `lineNeeded`, `memoryShare`, `cardMinutes` (15 s); deck/add/review/line routes; `KeyCardPlayer`.
2. `data/chapter_state.js` plus `GET /api/me/chapters` for per-chapter state words and `available:{questions,cards}`.
3. Revise run shell: `mergeQueue`, `filterSource`, `mixParts`, per-kind players, server-confirmed answers, summary and the badge store (`reviseDue.js`).
4. `POST /api/me/revise/answer`: the one free, server-graded, no-key-leak MCQ path (needs a `revise_cards` row).
5. Quick practice: quote, start, credit and allowance plumbing, chapter canonicalisation; `/api/sessions/{id}/check` for per-answer feedback (if the flag is turned on).
6. Time vocabulary: `allocateMinutes`, `practiceFor`, `fitMove`, `DailyMinutes` (10/20/30, More up to 999), `USUAL_MINUTES`.
7. Question-to-card link files for pairing a missed or served question with its Key cards (and, once inverted, a card with its questions).

**Missing (must be built or decided)**
1. A **session composer**: input `{ chapterKey, minutes, isPro, now }`, output an ordered list of items `{ kind: 'keycard'|'question', ... }` with a time budget. Nothing computes a mix by minutes. Needs one agreed seconds-per-item (cards 15; MCQ 40 per Revise or 60 per Quick practice) and a split rule.
2. A **chapter filter on the Key card due/new queue** (`dueCards` has no `chapter`; `loadStates` already supports it). Also a way to include cards the student has not added (the queue only plays added cards), without the permanent side effect or the Free allowance trap.
3. A **server-graded MCQ source for new questions of a chapter** that does not charge credits, does not need a revise card and does not leak the key: today either `/api/me/revise/answer` (own wrong answers only), Quick practice (credit-priced whole paper), Explore feed (key in the response, client graded), or the disabled per-answer check. Decision needed on whether session answers should write `user_question_progress` (Explore does; Revise does not) because that is what moves chapter state and seeds Revise.
4. A **card -> questions index** (invert the link files), and an acceptance of its uneven coverage (Financial Statements of Company: 2 cards linked; Partnership Fundamentals: 9 of 46).
5. **Chapter inventory check at quote time** (the quote checks subject count only; thin chapters fail only at `INSUFFICIENT_PRACTICE_CONTENT`).
6. A **single chapter picker data source** for 6 subjects: chapter list (`GET /api/keycards` units), state (`/api/me/chapters`), question counts (inventory), card counts, and lesson availability (`/api/study/catalog`, 4 subjects, 15 chapters). They are four reads with different flags.
7. **Free allowance fit**: a plan that shows what is open (5 taste cards per chapter, 10 reviews a day, 5 new cards, daily 10-question set, credits) before starting, and degrades gracefully; today each limit is discovered on a 402 mid-run.
8. **Today integration**: `buildMove` has no Key cards and no chapter input; `fitMove` only resizes practice/Revise. The Explore integration the owner described (a custom feed to practise a chapter) has no timer, no cards.
9. **One definition of weak chapters** (marks lost vs PrepOS vs chapter state) so "what is lined up" and "next move" agree.
10. App parity: the Flutter app ports the Key cards rules (`flutter_app/lib/features/keycards/data/keycards_rules.dart` 15 s a card, `lib/core/models/mistake_lab_traps.dart:611` `keycardMinutes`, `lib/features/review/revise/revise_screen.dart:387,675` the Revise run) and the Key cards fixtures pin the taste and the rules, so any rule change needs the fixtures and the Dart port updated together.

**Observed risks to carry into design (read-only findings, not changes)**
- Free's 10 reviews a day are shared by Study and Revise; a Study round of 20 cards (`STUDY_ROUND = 20`, `ChapterDeck.jsx:118`) on Free hits the limit at the 11th rating and shows "Today's free reviews are used".
- The Revise "minutes" line rounds questions up to 5-minute steps, so "about 5 minutes" can hide 1 question, and a pure Key cards run says "about 1 minute".
- Revise answers never touch `user_question_progress`, so a chapter session built on Revise would not move "Holding / Getting there / Needs work".
- `/api/questions/feed` returns the answer key to the browser; any session built on it would inherit that.
- Concept recall cards and Key cards are two card systems with different scorers (FSRS 0.90 uncapped vs FSRS 0.90 capped at the exam date; ratings 1 to 4 vs 1, 3, 4), so a "cards" part of a session has to pick one or label both.
- The Learn Concepts subject tab row has 4 subjects; Key cards has 6 (adds Biology and Political Science), so a chapter-first Learn needs the union and an honest "no lesson yet" for the 2 extra and for most chapters.
- `OptionPicker` (`KeycardsHome.jsx:71-101`, LK2 "your part" glitch): after `saveOption` it calls `refreshHome()` which clears the shared read and re-renders the units from the option-filtered server answer, so the list reorders under the student's finger; this is the likely source of the owner's "shuffles it" report (not verified on a device).
