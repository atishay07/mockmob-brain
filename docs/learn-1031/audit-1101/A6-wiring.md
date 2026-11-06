# A6: Learn v2 and the Explore feed on production data (wiring plan)

1 Nov 2026. A read-only audit of branch `web/1031-learn-v2` by a workflow subagent. Nothing was edited, built, deployed or
written to any database, and no database was read. The only check run was the existing unit tests:
`node --test data/tests/learn_compose.test.mjs learn_feed learn_suggest learn_search learn_preview keycards_routes`: 75 of 75 pass.

Sources: `src/components/learn2/**`, `src/lib/server/{learnPreview,keycardsPreview,keycards,keycardsHttp,keycardsMemoryDb,
keycardsSyllabus,firstFullMock,review,revise,study,answerHold,accountDeletion,rateLimit,learningHttp,mobileCors}.js`,
`src/lib/auth.ts`, `src/app/preview/arena/{previewRealDecks.js,realdeck/route.js,ArenaPreviewClient.jsx}`, the bookmarks,
interact, explore and keycards routes, `data/learn/*.js`, `data/{keycards,chapter_state,practice_pick,practice_source,
practice_library,practice_progress,question_reads,question_row_cache,attempt_question_ids,first_full_mock,learning_engine,
mistake_repair,answer_integrity,cuet_syllabus}.js`, migrations `0005`, `0007`, `0010`, `0028`, `20261002120000`,
`20261004154217`, `20261013094000`, `20261013120000`, `20261015210100`, `20261020150100`, `20261031140000`, the
`data/tests/{keycards_db,keycards_routes,learn_preview,app_bearer_routes,egress_*}` tests, the Flutter `ApiClient` and
`KeyCardsApi` (`wt-1031-keycards-app/flutter_app/lib`), `API-CONTRACT.md`, `DESIGN-SPEC.md`, `FEED-2.md`, R4, R5, R9 and the
owner's feedback file (LK1 to LK23). Next.js here is 16.2.4: route `params` is a Promise
(`node_modules/next/dist/docs/01-app/03-api-reference/03-file-conventions/route.md`, lines 82 to 95).

---

## 0. The decisions, on one page

1. **The preview is not database-agnostic.** `learnPreview.js` reads and changes in-memory arrays and maps directly. Only card
   ratings go through a real service (`kc.review` over the memory client). Production routes cannot call it. The fix is the
   Key cards pattern: one injectable service, `createLearn({ db, ... })`, run by production over Supabase and by the tests and
   the preview over the memory client. The preview then runs production code, and its existing tests become parity tests.
2. **A run lives in a new table, `learn_runs`.** Each finished item is a row in `learn_run_events`, whose primary key
   `(run_id, item_id)` is the idempotency lock. A feed is a run with `kind = 'feed'`. `study_runs` and `recovery_sessions`
   are not reused: one is Study's lesson engine, the other is a scored paper.
3. **Answers count like Explore's answers today (A9).** One transaction writes the event, increments `user_question_progress`
   and adds a `question_interactions` row with `flow_context = 'learn'`. Nothing writes to `attempts`, `recovery_sessions` or
   any credit table, so mock scores, papers and Review's paper mistakes cannot move.
4. **LK15 is held on the server** as `learning_allowances` rows of kind `learn_session`, period `<IST day>:<slot>`. The claim is
   made in the same transaction as the run row (the pattern of `start_learning_session` and `first_full_mock`). A replayed
   request key is the same run. A same-day re-entry to the unfinished session resumes it instead of answering 402.
5. **Key card ratings use the existing service** with two additive options: a per-item replay key, so a retry can never rate
   twice, and `withToday: false`, so a rating does not re-read all of a student's card states.
6. **Questions come from the shared subject pool** (`createPracticeSource().loadLightPool()`, cached per server). Never
   `select('*')`. Picked evidence-managed rows are verified on full rows at run start (`readRowsCached`). The key is read from
   the live row only at answer time.
7. **Questions from a student's open Mob paper never enter a run, a mistake or a grade.** Otherwise Learn reveals a key
   before the paper closes for the Mob.
8. **One migration file and its undo.** It adds two tables, two functions and widens one check. It is tested on PGlite,
   then dry-run on production in a transaction that rolls back. The owner applies it, because auto mode blocks production
   writes.
9. **Two flags flip together:** the server's `LEARN2_ENABLED` (new; off answers 404 `LEARN_OFF`) and the existing client
   flag `NEXT_PUBLIC_LEARN2`, which already gates the Explore covers in the live Explore page (`DiscoveryFeed.jsx:123`).
10. **The same routes serve the Flutter app.** `auth(request)` reads the bearer token first and then the cookie
    (`src/lib/auth.ts:87-129`). Every route takes `(request)` and joins `data/tests/app_bearer_routes.test.mjs`.

---

## 1. How the preview answers `/api/learn/*` today

The chain, end to end:

1. The client wrappers in `src/components/learn2/api.js` call `fetch('/api/learn/...')`. They send no request key and no
   resume id.
2. Inside `/preview/arena`, `ArenaPreviewClient.jsx:167-223` replaces `window.fetch`.
   - `previewRealDecks.js:9` (`isKeycardsPath`) sends `/api/learn/*`, `/api/keycards*`, `/api/me/chapters` and
     `/api/me/subject-options` to `/preview/arena/realdeck?_to=<path>&_plan=&_student=&_s=`.
3. `src/app/preview/arena/realdeck/route.js` imports `keycardsPreview.js` only when `NODE_ENV !== 'production'`.
   - Production answers 404.
   - `previewOff()` (`keycardsPreview.js:21`) also refuses on `VERCEL_ENV=production`.
4. `keycardsPreview.previewAnswer` makes or reuses one in-memory student per `(student, plan, session)`:
   - `createKeycards` over `fakeDb(tables)` (`keycardsMemoryDb.js`), with seeded tables, then `learnSeed()` (line 119);
   - every `_to` starting with `/api/learn/` goes to `learnPreview.learnAnswer` (line 165).
5. `learnPreview.learnAnswer` (lines 827-844) dispatches 11 handlers.

**Can production reuse it?** Part by part:

| Part | Today | Reusable in production? |
|---|---|---|
| `data/learn/{compose,suggest,search,stamps,feed}.js`, `data/keycards.js`, `data/chapter_state.js` | Pure, no I/O, tested | Yes, as they are |
| Card ratings (`kc.review`) | The real Key cards service over the memory client and the `key_card_review` mirror | Yes, with two additive options (section 4.6) |
| Card content | `entry.decks.byId`, unfiltered (`learnPreview.js:353`) | No. Production must use `kc`'s `published()`, so cards suspended for everyone (3 or more reports, view `key_card_suspended`) stay out |
| Questions and keys | 53 fixture questions with their keys, held in process (`data/fixtures/learn-preview-questions.json`) | No. Production uses the bank pool, eligibility verdicts, and the key from the live row at answer time |
| Lessons | `data/study/pilot.json` | No. Production uses Study's published units and `study_progress_summary` |
| Runs, mistakes, lessons read, feeds started | `entry.learn = { runs: Map, mistakes: Map, lessonsRead: Set, feeds: [] }` (line 89) | No. These need tables |
| Answers | Changes `entry.tables.user_question_progress` in place, including a `flow_context` field that the production table does not have (lines 537-539) | No. Production uses one transactional function (section 7) |
| Free feed limit | Counts feeds in an in-memory array, feeds only, with no 10-minute cap (lines 496-499, 516) | No. LK15 is not built anywhere yet (section 6) |
| View builders (`chapterInfo`, `publicItem`, `runBody`, `runEnd`, `feedEnd`, `subjectRead`, `previewRead`, `coversRead`, `cardsRead`, `shelvesRead`, `searchRead`) | Read from `ctx` | Yes, about 70% of the code, once they read from a per-request snapshot object instead of `entry` |

**Conclusion.** Refactor `learnPreview.js` into `src/lib/server/learn.js` (`createLearn`, no `server-only`, injectable). Its
data access goes through a Supabase-shaped client. `learnPreview.js` shrinks to building the preview's memory tables and seed,
then calling `createLearn` over `fakeDb`. `learn_preview.test.mjs` and `learn_feed.test.mjs` then prove that production
handlers return the bodies the renders were approved on.

---

## 2. The production architecture

New files, all following `keycards.js` and `keycardsHttp.js`:

- **`data/learn/questions.js`** (pure)
  - `servedOptions(row)`: `normalizeAnswerOptions` from `data/answer_integrity.js`, plus the preview's rule that strips a
    repeated "A. " only when every option has it.
  - `keyLetter(row)`: `resolveAnswerCorrectIndex`, then the served key.
  - `words(row)`.
  - `questionIndexFrom({ rows, managedIds, links, syllabus })`: returns `Map(chapterKey -> [{ id, chapter, difficulty, words,
    cards, managed, chash, body, options }])`. Passage-linked rows are left out (`isPassageLinkedQuestion`, as quick practice
    does).
  - `openMistakes(progressRows, index, held)` and `mistakeLabel` inputs.
- **`data/learn/allowance.js`** (pure)
  - `LEARN_FREE = { sessionsPerDay: 1, maxMinutes: 10, countedKinds: ['mix', 'feed'] }`.
  - `freeSession({ isPro, used, kind, minutes })`, which returns `{ canStart, clampTo, line }`. It replaces `freeFeed` in
    `feed.js`, so a feed and a chapter run share one rule.
- **`src/lib/server/learn.js`**: `createLearn(deps)`, which returns
  `{ subject, preview, start, run, answer, rate, end, cards, shelves, search, covers }`, each answering `{ http, body }`. Its
  dependencies:
  - `db`: a Supabase-like client;
  - `kc`: from `keycardsService()`;
  - `decks`, `syllabus`;
  - `getUser(id)`: `Database.getUserById`, always fresh, never the 30-second auth cache;
  - `questionIndex(subject)`;
  - `verifyRows(ids)`: `readRowsCached` plus `readablePracticeQuestions`;
  - `lessonsFor(userId, subject)`;
  - `heldQuestions(userId)`: `readHeldMobPapers`;
  - `mistakeLabels(userId, subject, items)`;
  - `now()`, `newId()`.
- **`src/lib/server/learnStore.js`**: every query and function call of section 3 and section 7, through the injected client.
  It contains no handler logic.
- **`src/lib/server/learnHttp.js`** (`server-only`): the wrapper, in this order:
  1. the flag (`LEARN2_ENABLED === 'true' && keyCardsEnabled()`, otherwise 404 `{ error: 'LEARN_OFF' }`);
  2. `auth(request)` (401);
  3. `checkPersistentRateLimit(request, { route: '/api/learn', limit: 120, keyParts: [userId] })` (429);
  4. for writes, a body of at most 4,000 characters that is a JSON object (413 or 422);
  5. `Cache-Control: no-store`;
  6. any thrown error answers 503 `{ error: 'LEARN_UNAVAILABLE', message }`.

  `learnService()` builds one service per process from `supabaseAdmin()`, `keycardsService()`, `decksOnce()`,
  `loadKeycardsSyllabus()` and the dependencies above.
- **12 route files** under `src/app/api/learn/`: `subject`, `runs` (POST), `runs/preview`, `runs/[id]` (GET, new),
  `runs/[id]/answer`, `runs/[id]/rate`, `runs/[id]/end`, `cards`, `shelves`, `search`, `covers`.
  - Each is `export const dynamic = 'force-dynamic'` with `export async function GET(request)` or
    `export async function POST(request, { params })`, and calls `const { id } = await params`.
  - The `export async function` form is what `app_bearer_routes.test.mjs` matches; the Key cards routes' `export const GET =`
    form would not match.

Additive changes to existing files:

| File | Change |
|---|---|
| `src/lib/server/keycards.js` | `review(userId, body, opts)` gains `opts.clientKey` (the replay key, overriding the raw `clientReviewedAt`), `opts.withToday` (default `true`; `false` skips `todayNow()` and answers `today: null`), and `opts.me` (skip the second users read). Return `published` and `playable` from `createKeycards`. The HTTP route passes no options, so its behaviour is unchanged. |
| `src/lib/server/keycardsMemoryDb.js` | The keys of `learn_runs` and `learn_run_events`. Mirrors of `learn_start_run`, `learn_record_event` and `attempt_question_ids`, statement for statement. The query operators `lte`, `lt`, `gte`, `is`, `not`, `maybeSingle` and `delete`. |
| `src/lib/server/learnPreview.js` | Becomes the seed (memory tables plus fixture index, lessons and labels) over `createLearn`. |
| `src/lib/server/accountDeletion.js` | Adds `learn_run_events`, then `learn_runs`, to `DELETION_STEPS`. |
| `src/lib/server/study.js` | Exports a light `lessonsFor(userId, subject)`: `publishedContent()` from the content cache plus one `study_progress_summary` call. It returns `[]` when `STUDY_CONTENT_ENABLED` is off. |
| `data/learn/suggest.js` | `endOptions` takes `freeSessionUsed`: no run lead on Free once the day's session is used, and the line in its place. `mistakeLabel(null, '16 Oct')` reads "You missed this on 16 Oct". |
| `src/components/learn2/api.js`, `RunPlayer.jsx`, `ChapterFeed.jsx` | Send `requestKey` (one id per start tap, kept in `sessionStorage` for the page) and `resume`. Put `?run=<id>` in the URL after a start (`router.replace`), and read `GET /api/learn/runs/:id` on reload. Handle 402 `FREE_SESSION_USED` (its `line` and `resume`) and 409 `QUESTION_CHANGED`. |
| `src/components/learn2/cards/FindView.jsx` | One `GET /api/learn/cards?subject=&filter=` call instead of one call per chapter (section 4.9). |

---

## 3. The per-request snapshot (one set of reads per request, never one per chapter)

Every handler that draws chapters loads one snapshot in parallel, then computes every chapter in memory. Bytes are JSON on the
wire, keys included. "Typical" is a Commerce student two months in: 120 Accountancy card states, 250 answered Accountancy
questions, 400 states in all. "Heavy" is a daily Pro student: 868 Accountancy states, 1,500 answered, 3,000 states in all.

| # | Read | Exact query | Rows typical / heavy | Bytes typical / heavy |
|---|---|---|---|---|
| S1 | Plan and subjects | `Database.getUserById(userId)` (`users`, one row) | 1 | about 1.5 KB |
| S2 | Section options | `student_subject_options` `select('subject,option').eq('user_id')` | 0 to 6 | under 0.5 KB |
| S3 | Card states | `key_card_states` `select('card_id,chapter_key,reps,lapses,due_at,last_review_at,last_rating,suspended,st:schedule->stability,lr:schedule->>last_review,sst:schedule->state,sdue:schedule->>due').eq('user_id').eq('subject')`, plus `.eq('chapter_key')` on chapter routes, `.order('card_id').range()` paged at 1,000 | 120 / 868 (chapter: 10 to 80) | 31 KB / 226 KB |
| S4 | Answered progress | `readAnsweredProgress(db, userId, { subject, columns: 'question_id,subject,chapter,attempt_count,last_correct,last_selected_key,last_attempted_at' })`, paged and ordered. Chapter routes add `.in('chapter', storedNamesFor(subject, chapter.name))` (`cuet_syllabus.js:674`) | 250 / 1,500 (chapter: 20 to 150) | 48 KB / 285 KB |
| S5 | Today's allowances | `learning_allowances` `select('kind,period,reference').eq('user_id').in('kind', ['keycard_review','keycard_new','learn_session']).like('period', '<IST day>:%')` | at most 16 | under 1.5 KB |
| S6 | Unfinished runs | `learn_runs` `select('id,kind,subject,chapter_key,minutes,leave_out,item_count,done_count,seconds_left,created_at').eq('user_id').is('ended_at', null).gte('created_at', now - 24 h).order('created_at', desc).limit(5)` | at most 5 | about 1 KB |
| S7 | Held Mob questions | `readHeldMobPapers(db, userId, now)` (`answerHold.js:19`): recent Mob attempts and their `details` | 0 to 3 | 0 to 15 KB |
| S8 | Published cards | `kc.published()`: the `key_card_suspended` view, cached 5 minutes per process | 0 per request on a hit | 0 |
| S9 | Question index | Built from `createPracticeSource({ db, subjectId, mode: quick, opts: {} }).loadLightPool()`, which shares the practice pool cache key `[subject, null, null, null]` and revalidates with two head counts after 5 minutes. Then `readable()` verdicts for legacy rows, links from `data/keycards/links/<subject>.json`, and stem lengths. Kept per subject for 5 minutes per process | 0 on a hit; the cold pool is about 2 MB, once per instance per subject | 0 on a hit |
| S10 | Lessons | `lessonsFor`: units from Study's content cache (`STUDY_CACHE_TTL_MS` 60 s) plus `rpc('study_progress_summary')` | 1 call | under 2 KB |

Rules every read keeps:
- `select('*')` on `questions` is never used. The light pool has no `evidence` or `provenance`. Full rows go only through
  `readRowsCached`, for picked managed rows.
- `key_card_states` is never read with its `schedule` JSON (about 575 bytes a row). Four json-path stubs feed
  `retrievability`. A parity test proves the stubs give the same chapter state as full rows.
- Every list read is ordered and paged at 1,000 (PostgREST max-rows). Every `.in()` list is cut into pieces of 100.
- What "unknown" means: if S1, S3, S4 or S5 fails, the request answers 503. It never shows a zero for "could not look"
  (review.js L12). If S10 fails, `lesson` is null. If S7 fails, the request may still count questions, but every question is
  refused for serving and grading (fail closed). If S6 fails, there is no Pick up.

---

## 4. The routes, one by one

The shapes below are what `learnPreview.js` returns today, which is the de facto contract the renders were approved on.
`API-CONTRACT.md` is behind it (task T20). "Add" marks additive fields. Nothing is renamed, except the preview-only 402 code
noted under 4.3.

### 4.1 GET /api/learn/subject?subject=
- **Used by:** Learn home (`LearnHome.jsx:113`) and Find (`FindView.jsx:40, 169`).
- **Input:** `subject` is optional. The default is the student's first top subject (`isTopSubject`) that has a deck or a
  question pool. Anything else is 404 `SUBJECT_NOT_FOUND`.
- **Reads:** S1 to S10, subject scope.
- **Logic:** `subjectRead` (`learnPreview.js:393-450`) over the snapshot. Per chapter:
  - cards from `published`; Free sees the taste cards;
  - states S3;
  - questions from S9, less S7;
  - open mistakes from S4 (section 5.3);
  - the lesson from S10;
  - the tally (`tallyChapters`), memory (`memoryShare` over the stubs), state (`stateFor`), and the unfinished run from S6.

  Then come the suggestions (`suggest.js`) and the level pool, filtered by the saved section.
- **Writes:** none.
- **Response:** unchanged (`plan, student, subjects, subject, freeNote, suggestions[3], parts[]`). The fix suggestion's
  evidence keeps its "With the lines you needed." form when the place is unknown (Phase 1; section 5.3).
- **No home yet:** `ChapterRow.marksOpen` stays null. Phase 2 can fill it for Pro from `loadReviewRecord` plus `chapterRows`,
  as `GET /api/me/chapters` already does.
- **Size:** 4 to 7 database round trips in parallel. About 85 KB typical and 515 KB heavy (section 8).

### 4.2 POST /api/learn/runs/preview
- **Used by:** the chapter page on each length or pile change (`ChapterPage.jsx:57`).
- **Body:** `{ chapterKey, minutes (1-240), leaveOut ⊆ [cards, questions, mistakes, lesson], addNext? }`. An invalid body is 422.
  An unknown chapter or a retired one is 404 `CHAPTER_NOT_FOUND`.
- **Reads:** S1, S2, S3 and S4 at chapter scope, S5 to S10.
- **Logic:** `previewRead` (lines 464-489): `composeRun` (mix), `dryRun`, the recap compose and `nextChapterOf`. `addNext`
  stays supported, but the client never sends it (the next chapter is a link, `ChapterPage.jsx:498`).
- **Add (Free only):** `freeSession: { used, maxMinutes: 10, line }`. When `minutes > 10`, the piles are composed at 10 and
  `free.text` says so. The line appears only once he picks a length past the limit (LK15: "only at the real limit").
- **Add (optional):** `byMinutes` for 5, 10 and 20 in one answer, so a length switch costs no request (CPU only).
- **Writes:** none.
- **Size:** about 10 to 40 KB a call.

### 4.3 POST /api/learn/runs (start, feed start, resume)
- **Used by:** `RunPlayer.jsx:395`, `ChapterFeed.jsx:253`, and Find's "Study these".
- **Body:** `{ chapterKey?, cardIds? (at most 100 strings of at most 120 characters), minutes, leaveOut, kind: mix|recap|cards|feed|level, requestKey (add: 8 to 100 characters [A-Za-z0-9_-]), resume? (add: a run id), addNext? }`.

**Flow:**
1. **Validate.** A request with neither `chapterKey` nor `cardIds` is 422 `CHAPTER_OR_CARDS_REQUIRED`.
2. **Resume.** If `resume` names the student's own run, not ended, under 24 hours old and unfinished, answer 200 with
   `runBody(run, { resumed: true })`. Otherwise keep the preview's implicit match: the same chapter and kind, and `minutes`
   equal to the minutes left.
3. **Snapshot.** Read S1 to S10 at chapter scope.
4. **LK15** (Free, kind in `countedKinds`). If today's `learn_session` row is held by an unfinished run of the same chapter
   and kind, resume that run. If it is held by any other run, answer 402. A kind of `mix` or `feed` is clamped to 10 minutes.
5. **Compose** with `composeRun`, through `createRun` and `withNext`. Free's `ratingsLeft` and `newLeft` come from S5.
6. **Verify the questions.** Run `verifyRows` over the picked managed question ids. Drop the rows that fail and compose again,
   for at most 3 rounds (the `MAX_VERIFY_ROUNDS` idea of `practice_pick.js`). Never pad. A run that ends shorter says its real
   length (shrink).
7. **Labels.** Resolve labels only for the run's mistake items (section 5.3).
8. **Build the row.** `id = 'lr_' + 24 hex characters`. `items` are stored compact, with no keys. A question item carries
   `chash = questions.content_hash` (or `updated_at`) for the check at answer time. Also store `seconds`,
   `start_state = chapter state`, `looks` and `added`.
9. **Call `rpc('learn_start_run', ...)`** (section 7). It answers one of:
   - `ok`;
   - `replay`: load the run and answer `runBody`, `resumed` when it has events;
   - `used`: 402 `{ error: 'FREE_SESSION_USED', reason: 'learn_session', line, resume: { id, chapterKey, title, done, of, minutesLeft, kind } | null }`;
   - `key_conflict`: 409 `IDEMPOTENCY_CONFLICT`.

   The preview's `FREE_FEED_USED` / `learn_feed` code exists only in the preview. The client reads only the status and
   `line`, so it is replaced in the same change and recorded in the contract.

**Response:** `runBody` as in `learnPreview.js:366-376`: `{ id, kind, chapter, minutes, items[], revisePile, resumed, added, looks }`.
- Card items carry the published card object.
- Question items carry only `{ id, body, options[{key,text}] }` and `mistake`.
- Add `free: { text } | null` when the length was clamped.

**Writes, in one transaction:** 1 `learn_runs` row (3 to 6 KB), at most 1 `learning_allowances` row, and up to about 20
`learning_question_exposure` rows. These are the exposure rows practice starts already write, so a later recovery check never
reuses a question shown in Learn.

**Reads beyond the snapshot:**
- the stamp query of `readRowsCached` (about 70 bytes a row, at most 20 ids);
- full rows only on a cache miss (at most 20 × 35 KB cold, usually 0, because every student shares the same chapter's rows);
- at most 3 small label reads when the run has mistakes.

### 4.4 GET /api/learn/runs/:id (new)
- **What for:** a reload, or the app reopening a run. It is the student's own run (`.eq('user_id')`; another student's id is
  404 `RUN_NOT_FOUND`).
- **Reads:** the run row and its events (`item_id` only).
- **Response:** `runBody(run, { resumed: true })`, the undone items only. An ended run answers 409 `RUN_ENDED` with
  `{ endHref }`.
- **Rows:** 1, plus at most 60.

### 4.5 POST /api/learn/runs/:id/answer
- **Body:** `{ itemId (at most 120 characters), choice }`.
- **Reads:**
  - S1 (plan, for the locked line);
  - the run row (`id,user_id,kind,subject,chapter_key,items,limit_line,ended_at,created_at`);
  - the replay probe: `learn_run_events select('body').eq('run_id').eq('item_id')`. A hit answers the stored body at once,
    with the line's card rebuilt from the decks, and nothing else is read;
  - the question, narrow: `questions select('id,subject,chapter,question,body,options,correct_index,correct_answer,explanation,status,is_deleted,verification_state,content_hash,updated_at').eq('id').maybeSingle()`. Never `*`;
  - S7 for that one id.
- **Checks:**
  - The item must be a question of this run. Otherwise 422 `ITEM_NOT_A_QUESTION`. A foreign or unknown run is 404.
  - The run must be under 48 hours old. Otherwise 409 `RUN_EXPIRED`.
  - `choice` must be one of the served option keys. Otherwise 422 `INVALID_CHOICE`.
  - The row must be live, not deleted, not disputed, with its `chash` unchanged. Otherwise 409 `QUESTION_CHANGED`, and nothing
    is written. This is the rule of `sessionCheck.resolveKey`: only a current, unchanged key is used.
  - The question must not be held by a Mob paper. Otherwise 409 `QUESTION_HELD`.
- **Logic:** as `runAnswer` (lines 522-565).
  - `correct = choice === keyLetter(row)`.
  - `fixed` is true when the answer is right and `origin === 'mistake'`.
  - The line comes from `lineNeeded` over the bundled links and the published cards. On Free, a non-taste card is a
    `lockedStub` with the Pro line. Inside a run the line uses no allowance; this keeps the preview's rule and is noted for the
    owner.
  - A wrong answer whose card is open asks for a re-insert. The function adds it at most once per card per run, and not after
    the card was rated Got it or Easy in this run.
- **Writes, in one call** of `rpc('learn_record_event', { kind: 'answer', ... })`: the event, the progress upsert, the
  interaction row (`flow_context 'learn'`), the counters and the re-insert (section 7).
- **Response:** unchanged: `{ correct, key, explanation, fixed, fixedText, line, reinsert: null | { itemId, at, item } }`. The
  key and the explanation leave the server only in this answer.
- **Size:** about 6 to 10 KB read, 4 rows written.

### 4.6 POST /api/learn/runs/:id/rate `{ itemId, rating: 1|3|4 }`
- **Branches,** as `runRate` (lines 567-627):
  - A **lesson item** writes an event of kind `lesson` and nothing else. Study's own completion marks a lesson as read.
  - A **recap item or recap run** calls `kc.review(userId, { cardId, rating, mode: 'last_look', clientReviewedAt: now }, { clientKey, withToday: false, me })`. That is logged without a schedule and without an allowance; the event kind is `recap`.
  - A **look,** or any rating once the run's limit is set, writes an event of kind `look` and calls no review.
  - Anything else calls `kc.review(..., mode: 'study', { clientKey, withToday: false, me })`:
    - 402 `keycard_reviews` or `keycard_new`: the event is kind `look` with `p_limit_line`, and the answer is
      `{ ok, saved: false, look: true, stamp: null, revisePile, limit }`. The rest of the run plays as looks.
    - 409 `REVIEW_CONFLICT`: read the state again and try once more, then answer 409.
    - `ok` or `replay`: `due_at` gives the stamp (`returnDay`). A Missed rating on a card whose stage is not `again` asks for
      a re-insert, and the stamp becomes "Back later in this run".
- **The replay key:** `clientKey = 'learn:' + sha256(runId + ':' + itemId).slice(0, 40)`. It fits `key_card_reviews.client_key`
  (at most 100 characters), so `key_card_review()` answers `replay` to a retried rating. Today the preview sends
  `clientReviewedAt: iso(now)` (`learnPreview.js:590, 611`), which is a new key on every retry. A retry would rate the card
  twice and use a second Free slot.
- **Writes:** `key_card_reviews` 1, `key_card_states` 1, `learning_allowances` 0 to 2 (Free), `learn_run_events` 1, and the
  `learn_runs` counters.
- **Response:** unchanged, plus `replay: true` on a replay.
- **Size:** about 6 to 8 KB, against about 300 KB for a heavy student if the review's `today` recount were kept (risk R2).

### 4.7 POST /api/learn/runs/:id/rate `{ itemId, keep: true }` (the feed's Keep)
- **Reads:** the run, and one `key_card_states` row for the card.
- **If the card is already in Revise** (not suspended, `reps > 0`): the stamp comes from its `due_at`, and nothing is scheduled.
- **Otherwise:** `kc.review(rating 3, mode 'study', { clientKey, withToday: false })`.
  - 402 answers 402 `{ error: 'PRO_REQUIRED', reason }`. Nothing is recorded, so a Keep after an upgrade still works.
  - `ok` gives the stamp from `due_at`.
- **The event:** kind `keep`, with `card_id`, `due_at`, and `body: { kept, stamp, already }`.
- **Response:** `{ ok, kept: true, stamp, revisePile, limit: null }`. A swipe without Keep writes nothing (A6).

### 4.8 GET /api/learn/runs/:id/end
- **Reads:**
  - the run;
  - its events (at most 60 rows: `item_id,kind,question_id,card_id,correct,fixed,origin,rating,due_at`);
  - S1 to S9 at subject scope, for the chapter state now, mistakes elsewhere, the subject's due count and the next chapter;
  - S5 for LK15.
- **Logic:** `runEnd` and `feedEnd` (lines 629-716) over the events:
  - `n(r)` counts the `rate` events;
  - looks are the `look` and `recap` events;
  - answered means `answer` events not from a mistake;
  - fixed counts `fixed` events;
  - kept comes from the `keep` events.
- **LK15:** on Free with the day's session used (always true at the end of a session it claimed), `endOptions` offers no run
  lead and puts the line in its place. The feed end keeps its free line. Today the preview applies this to feeds only.
- **Writes:** `update learn_runs set ended_at = now() where id = :id and user_id = :u and ended_at is null`. This is
  idempotent: a repeated GET computes the same numbers.
- **Response:** unchanged: `{ feed, title, numbers{cards,questions,fixed,mistakes,detail}, lines, revisePile[], moved, free, lead, options }`.
- **Size:** about 85 KB typical.

### 4.9 GET /api/learn/cards?chapter=&filter=all|must|revise|missed (plus the new ?subject=&filter=)
- **Reads:** S1, S3 at chapter scope, S4 at chapter scope (open mistakes whose linked cards count as "Missed lately"), and S8.
- **Logic:** `cardsRead` (lines 744-774). "Missed lately" is the last 7 days (`MISSED_DAYS`, line 40).
- **Add:** `?subject=<id>&filter=` answers `{ plan, lockedCount, chapters: [{ key, title, cards: [...] }] }` in one request,
  from S3 and S4 at subject scope. Find's shelves today make one request per chapter, 6 at a time
  (`FindView.jsx:39-58`): about 15 to 20 requests for Accountancy each time a shelf opens.

### 4.10 GET /api/learn/shelves?subject=
- **Reads:** S1, S3 and S4 at subject scope, and S8.
- **The all-subject due count** (the sidebar badge, CRITIQUE E2) is `kc.dueCount(userId)`, the same function the Key cards
  overview uses, so the two always agree. Narrow its read to the rows that are due:
  `.eq('suspended', false).gt('reps', 0).lte('due_at', now)`. That is 10 to 50 rows instead of every state, and the result is
  the same, because only due rows count.
- **Response:** unchanged: `{ due{count,minutes,all,subjects}, missed{count,days}, revise{count,chapters}, must{count,chapters} }`.

### 4.11 GET /api/learn/search?subject=&q=
- **Reads:** S1 only (plan). Decks, `published` and lesson titles all come from memory.
- **Input:** `q` is at most 80 characters, with at least 2 characters to search (`SEARCH_RULES`).
- **Logic:** `searchSubject`. A locked card returns only `lockedStub` and never its words (pinned by `learn_search.test.mjs`).
- **Size:** about 1.5 KB of database reads.

### 4.12 GET /api/learn/covers?subject=
- **Used by:** `ExploreCovers`, already mounted on the live Explore page (`DiscoveryFeed.jsx:123`) and hidden unless
  `NEXT_PUBLIC_LEARN2 === 'on'`. When signed out, the route answers 401 and the row hides (`ExploreCovers.jsx:40`).
- **Reads:** S1 to S9 at subject scope, and S5 for the Free line.
- **Logic:** `coversRead` (lines 722-742): at most 8 covers × 3 lengths of `composeRun`, in memory only.
- **Add:**
  - `motif` per cover: a key from a static chapter-to-object map (`data/learn/motifs.js`, no database). The cover can then draw
    a chapter object instead of the subject's (LK21: every Accountancy cover showed the same object).
  - On Free: `free: { text, maxMinutes: 10 }`.
- **Size:** about 85 KB typical.

### 4.13 POST /api/bookmarks (the feed's Save)
This is reused as it is. It already takes `auth(request)` (bearer or cookie), stops Free at 25 saves with a 402
(`FREE_BOOKMARK_LIMIT`), and is in `app_bearer_routes.test.mjs`. No change.

---

## 5. Run state, answers and idempotency

### 5.1 Where things live
- **`learn_runs`** holds one row per run or feed:
  - the items, compact: id, type, `cardId` / `questionId` / `lessonId`, stage, origin, links, look, recap, the mistake label,
    `chash` and seconds;
  - the counters `item_count`, `done_count` and `seconds_left`, so Learn home and Pick up never read `items`;
  - `start_state`, `added`, `looks`, `limit_line`, `reinserted[]`, `extra`, `session_claimed`, `ended_at`.
- **`learn_run_events`** holds one row per finished item. Its body is compact: verdict fields and ids. Card objects and the
  explanation are rebuilt on a replay.
- **Not `study_runs`.** Its `mode` check is `learn | recall`, meaning Study lessons, and its start function insists on Study
  content checks (`20261004154217_connected_study_suite.sql:19-26, 49-70`). **Not `recovery_sessions`.** That is a scored
  paper, finalised into `attempts`.

### 5.2 What an answer moves and what it does not

| Written (in `learn_record_event`) | Effect |
|---|---|
| `learn_run_events` row | The run's own log; the replay lock |
| `user_question_progress` upsert: `seen_count+1, attempt_count+1, correct_count+right, last_selected_key, last_correct, last_*_at` | Chapter state (Key cards and Learn), the practice picker's seen set, Revise seeds (a wrong answer can become a Revise question), the learning summary's solved count. The same footing as an Explore answer today (A9) |
| `question_interactions` row: `attempted`, `flow_context 'learn'`, `session_id = run id`, metadata `{ selected_key, is_correct, item_id, run_kind }` | The exposure history that `repairCheckStore.js:40` and `start_learning_episode` read, so a Learn question is never offered as a "fresh" check later. DESIGN-SPEC A6 asks for exactly this flow |

| Never written | So these cannot move |
|---|---|
| `attempts`, `recovery_sessions`, `session_check_log` | Mock scores, papers sat, "Mock 3" numbering, Review's paper mistakes, Where you stand, Compass |
| `credit_transactions`, `spend_credits` | Learn questions are free (A9 and LK15). Free's only gate is the one session a day |
| `recovery_review_queue` | Unlike the session finaliser (`20261013094000_session_finaliser.sql:36-39`), a Learn miss queues nothing in recovery |

### 5.3 Open mistakes and their labels
- **What counts as open:** an S4 row with `attempt_count > 0`, `last_correct = false` and a non-empty `last_selected_key`. A
  blank in a mock is not a mistake: `substr('ABCD', 0, 1)` is empty in the finaliser. The question must also be in the
  chapter's servable index and not held. The list runs oldest first.
- **When it closes:** a right answer anywhere (Learn, Explore, a paper) flips `last_correct`, so the mistake closes. That is
  what "Fixed" means in Learn.
- **The label `{ where, when }`,** resolved only for the mistake items of a run, so a run with no mistakes costs nothing:
  - `when` is the IST short date of `last_attempted_at`.
  - `where` is `Learn` or `Explore feed` when the newest wrong `learn_run_events` row for that question matches
    `last_attempted_at`. This needs the index `learn_run_events_question`.
  - Otherwise `where` comes from papers: `readAttemptQuestionIds(db, { userId, subject, limit: 40 })` (ids only; `null` when
    the function is missing, and then `where = null`; never the heavy snapshot read), plus the subject's slim attempts
    (`id,subject,completed_at,mode:selection_meta->>mode`). `sourceLabels` (`repairRun.js:133`) gives "Mock 3". The newest
    paper that holds the question at or before `last_attempted_at` wins.
- **Phase 1 for Learn home** passes no `where` to the suggestion engine. Its "fix" line then reads "With the lines you
  needed.", not "From Mock 3 on 16 Oct, with the lines you needed."

### 5.4 The idempotency matrix

| Action | Lock | A retry or double tap |
|---|---|---|
| Start | `unique (user_id, request_key)` inside `learn_start_run` | Returns the same run (`replay`), with no second allowance row |
| Start without a key (old client) | Server fallback: the same student, chapter, kind and minutes in the last 10 s with no events | Returns that run |
| Answer, rate, keep, look, lesson | `primary key (run_id, item_id)`, with the run row locked `for update` | Returns the stored body; nothing is counted twice |
| Card review inside rate or keep | `key_card_reviews (user_id, card_id, client_key)` with the per-item key | `key_card_review()` answers `replay`; no second schedule move, no second Free slot |
| Re-insert | The function finds the position under the run lock; once per card (`reinserted[]`) | Positions stay right when two answers race |
| End | `where ended_at is null` | The same numbers again |
| Concurrent starts by one Free student | The `learning_allowances` primary key | One run wins; the other gets 402 with `resume` |

**Expiry.** Pick up offers runs under 24 hours old (as the preview does). Answers are taken until 48 hours after the start,
then 409 `RUN_EXPIRED`.

---

## 6. LK15: Free's one Learn session a day, held on the server

Owner rule LK15, decided and not yet built: Free gets one Learn session a day (a chapter run or the Explore feed), up to
10 minutes, with its questions free. Explore's plain question swipe stays unlimited. Pro has any number, of any length. The
limit line shows only at the real limit.

| | First full mock free (`firstFullMock.js`) | Today's included set (`start_learning_session`) | Learn session (this plan) |
|---|---|---|---|
| Row | `learning_allowances(kind 'first_full_mock:<subject>', period 'ever', reference = session id)` | `kind = quota`, `period = IST day` (`allowancePeriod`, `learning_engine.js:157`) | `kind 'learn_session'`, `period '<IST day>:<slot>'` (slot 1 to N, N = 1), `reference = run id` |
| Lock | Primary key; a 23505 is read back: `mine` or `taken` | `users` row `for update`, then exists-or-insert | Primary key, inside `learn_start_run`; no `users` lock |
| Claimed | At start, even if abandoned | At start, with the session row | At start, in the same transaction as the run row, so a failed run insert claims nothing |
| Replay | The same session id is `mine` | The same `request_key` | The same `request_key` is `replay` |
| Unknown | "Unknown is never free" | Raises | Answers 503; never a second free session |
| Re-entry | n/a | n/a | An unfinished session run of the same chapter and kind resumes. Any other start answers 402 with `resume` |

The rule in code (`data/learn/allowance.js`):
- `countedKinds = ['mix', 'feed']`. `cards` (Find's "Study these"), `recap` and `level` are left out: the first two are already
  limited by the card allowance, and `level` is a 6-question placement. This needs the owner's word (D1).
- Free's counted runs are clamped to 10 minutes, and the start answer carries `free.text`.
- Free uses no slot on a resume, a replay or an "Add the next chapter".
- On Free, the end screen of the day's session shows the line in place of run leads, for chapter runs as well as feeds.

Copy for the CTO to settle:
- Feed: "Your free feed for today is done. Pro has as many as you like." (exists).
- Chapter runs: "Your free Learn session for today is done. Pro has as many as you like." (new).
- The 402 with `resume`: "Today's free session is {chapter}. Pick it up, or Pro has as many as you like." (new).

---

## 7. Migrations (drafts; saved, never applied by this plan)

### 7.1 `supabase/migrations/20261101150000_learn_runs.sql`

```sql
-- Learn v2 runs and the Explore chapter feed (docs/brain/learn-1031/audit-1101/A6-wiring.md, 1 Nov 2026).
-- Two new tables, two functions, and one widened check. No existing row changes.
--   learn_runs          one composed run or feed: its items (ids only, never an answer key), counters and state
--   learn_run_events    one row per finished item; the primary key (run_id, item_id) is the idempotency lock
--   learn_start_run()   the run row, Free's daily session claim (learning_allowances 'learn_session') and the question
--                       exposure rows, in one transaction; a replayed request_key is the same run
--   learn_record_event() one item's outcome in one transaction: the event, the progress upsert, the interaction row
--                       (flow_context 'learn'), the re-inserted card and the counters
--   question_interactions.flow_context also accepts 'learn' (server-only: the generic interact route still refuses it)
-- Security: RLS on, no policy, service role only; both functions SECURITY DEFINER with an empty search_path and execute
-- for service_role only. Account deletion: DELETION_STEPS lists both tables (events first) BEFORE this is applied.
-- SAVED ONLY. Dry runs: data/tests/learn_db.test.mjs (PGlite), then a rolled-back production dry run.
-- Undo: supabase/undo/20261101150000_learn_runs.undo.sql

create table if not exists public.learn_runs (
  id text primary key check (char_length(id) <= 60),
  user_id text not null references public.users (id) on delete cascade,
  request_key text not null check (char_length(request_key) between 8 and 100),
  kind text not null check (kind in ('mix', 'cards', 'recap', 'feed', 'level')),
  subject text not null,
  chapter_key text not null,
  asked_minutes smallint not null check (asked_minutes between 1 and 240),
  minutes smallint not null check (minutes between 0 and 240),
  leave_out text[] not null default '{}',
  items jsonb not null check (jsonb_typeof(items) = 'array'),
  item_count smallint not null default 0,
  done_count smallint not null default 0,
  seconds_left integer not null default 0,
  reinserted text[] not null default '{}',
  extra smallint not null default 0,
  start_state jsonb,
  added jsonb,
  looks jsonb,
  limit_line text check (limit_line is null or char_length(limit_line) <= 300),
  session_claimed boolean not null default false,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  ended_at timestamptz,
  unique (user_id, request_key)
);
create index if not exists learn_runs_owner_recent on public.learn_runs (user_id, created_at desc);
create index if not exists learn_runs_open on public.learn_runs (user_id, created_at desc) where ended_at is null;

create table if not exists public.learn_run_events (
  run_id text not null references public.learn_runs (id) on delete cascade,
  item_id text not null check (char_length(item_id) <= 120),
  user_id text not null references public.users (id) on delete cascade,
  kind text not null check (kind in ('answer', 'rate', 'look', 'recap', 'keep', 'lesson')),
  question_id text,
  card_id text,
  choice text check (choice is null or char_length(choice) <= 2),
  correct boolean,
  fixed boolean,
  origin text check (origin is null or origin in ('mistake', 'linked', 'chapter')),
  rating smallint check (rating is null or rating in (1, 3, 4)),
  due_at timestamptz,
  body jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now(),
  primary key (run_id, item_id)
);
create index if not exists learn_run_events_question on public.learn_run_events (user_id, question_id, created_at desc)
  where question_id is not null;

alter table public.learn_runs enable row level security;
alter table public.learn_run_events enable row level security;
revoke all on public.learn_runs, public.learn_run_events from public, anon, authenticated;
grant all on public.learn_runs, public.learn_run_events to service_role;

-- Returns { status: 'ok' | 'replay' | 'used' | 'key_conflict', id?, reference?, claimed? }.
create or replace function public.learn_start_run(p_row jsonb, p_quota_kind text, p_day text, p_quota_limit int, p_question_ids text[])
returns jsonb
language plpgsql
security definer
set search_path = ''
as $$
declare
  v_user text := p_row->>'user_id';
  v_run public.learn_runs%rowtype;
  v_ref text;
  v_slot int;
  v_claimed boolean := false;
begin
  if v_user is null or coalesce(p_row->>'id', '') = '' or coalesce(p_row->>'request_key', '') = '' then
    raise exception 'learn_start_run: bad input';
  end if;
  select * into v_run from public.learn_runs r where r.user_id = v_user and r.request_key = p_row->>'request_key';
  if found then
    if v_run.kind <> p_row->>'kind' or v_run.chapter_key <> p_row->>'chapter_key' then
      return jsonb_build_object('status', 'key_conflict');
    end if;
    return jsonb_build_object('status', 'replay', 'id', v_run.id);
  end if;
  if p_quota_kind is not null then
    for v_slot in 1 .. greatest(coalesce(p_quota_limit, 0), 0) loop
      insert into public.learning_allowances (user_id, kind, period, reference)
        values (v_user, p_quota_kind, p_day || ':' || v_slot, p_row->>'id')
        on conflict do nothing;
      if found then v_claimed := true; exit; end if;
    end loop;
    if not v_claimed then
      select a.reference into v_ref from public.learning_allowances a
        where a.user_id = v_user and a.kind = p_quota_kind and a.period like p_day || ':%'
        order by a.created_at desc limit 1;
      return jsonb_build_object('status', 'used', 'reference', v_ref);
    end if;
  end if;
  insert into public.learn_runs (id, user_id, request_key, kind, subject, chapter_key, asked_minutes, minutes, leave_out,
      items, item_count, seconds_left, start_state, added, looks, session_claimed)
    values (p_row->>'id', v_user, p_row->>'request_key', p_row->>'kind', p_row->>'subject', p_row->>'chapter_key',
      (p_row->>'asked_minutes')::smallint, (p_row->>'minutes')::smallint,
      coalesce(array(select jsonb_array_elements_text(coalesce(p_row->'leave_out', '[]'::jsonb))), '{}'::text[]),
      p_row->'items', jsonb_array_length(p_row->'items'), coalesce((p_row->>'seconds')::int, 0),
      p_row->'start_state', p_row->'added', p_row->'looks', v_claimed)
    on conflict (user_id, request_key) do nothing;
  if not found then
    -- A concurrent start with the same key won: undo this claim (the whole function rolls back); the caller replays.
    raise exception 'learn_start_run: concurrent start';
  end if;
  insert into public.learning_question_exposure (user_id, question_id, reference)
    select v_user, q, p_row->>'id' from unnest(coalesce(p_question_ids, '{}'::text[])) as q
    on conflict do nothing;
  return jsonb_build_object('status', 'ok', 'id', p_row->>'id', 'claimed', v_claimed);
end;
$$;

-- Returns { status: 'ok' | 'replay' | 'not_found' | 'no_item', body?, reinsert?: { item_id, at }, revise_pile? }.
-- p_event: { kind, question_id?, card_id?, choice?, correct?, fixed?, origin?, rating?, due_at?, seconds, body }
-- p_progress: null | { question_id, subject, chapter, selected_key, correct }
-- p_interaction: null | { question_id, metadata }
-- p_reinsert: null | { item, card_id, gap, seconds, unless_rated_well }
create or replace function public.learn_record_event(p_user text, p_run text, p_item text, p_event jsonb, p_progress jsonb,
  p_interaction jsonb, p_reinsert jsonb, p_limit_line text)
returns jsonb
language plpgsql
security definer
set search_path = ''
as $$
declare
  v_run public.learn_runs%rowtype;
  v_body jsonb;
  v_at int;
  v_pos int;
  v_id text;
  v_reinsert jsonb := null;
begin
  select * into v_run from public.learn_runs r where r.id = p_run and r.user_id = p_user for update;
  if not found then return jsonb_build_object('status', 'not_found'); end if;
  select e.body into v_body from public.learn_run_events e where e.run_id = p_run and e.item_id = p_item;
  if found then return jsonb_build_object('status', 'replay', 'body', v_body); end if;
  select (x.ord - 1)::int into v_at from jsonb_array_elements(v_run.items) with ordinality as x(item, ord)
    where x.item->>'id' = p_item;
  if v_at is null then return jsonb_build_object('status', 'no_item'); end if;

  if p_reinsert is not null
     and not ((p_reinsert->>'card_id') = any (v_run.reinserted))
     and not (coalesce((p_reinsert->>'unless_rated_well')::boolean, false) and exists (
       select 1 from public.learn_run_events e where e.run_id = p_run and e.card_id = p_reinsert->>'card_id' and e.rating in (3, 4))) then
    v_pos := least(jsonb_array_length(v_run.items), v_at + coalesce((p_reinsert->>'gap')::int, 3));
    v_id := v_run.id || '-r' || (v_run.extra + 1);
    v_reinsert := jsonb_build_object('item_id', v_id, 'at', v_pos);
    update public.learn_runs set
      items = jsonb_insert(items, array[v_pos::text], (p_reinsert->'item') || jsonb_build_object('id', v_id), false),
      extra = extra + 1,
      reinserted = array_append(reinserted, p_reinsert->>'card_id'),
      item_count = item_count + 1,
      seconds_left = seconds_left + coalesce((p_reinsert->>'seconds')::int, 0)
      where id = p_run;
  end if;

  v_body := coalesce(p_event->'body', '{}'::jsonb)
    || case when v_reinsert is null then '{}'::jsonb else jsonb_build_object('reinsert', v_reinsert) end;
  insert into public.learn_run_events (run_id, item_id, user_id, kind, question_id, card_id, choice, correct, fixed, origin, rating, due_at, body)
    values (p_run, p_item, p_user, p_event->>'kind', p_event->>'question_id', p_event->>'card_id', p_event->>'choice',
      (p_event->>'correct')::boolean, (p_event->>'fixed')::boolean, p_event->>'origin', (p_event->>'rating')::smallint,
      (p_event->>'due_at')::timestamptz, v_body);

  if p_progress is not null then
    insert into public.user_question_progress as g (user_id, question_id, subject, chapter, seen_count, attempt_count,
        correct_count, skip_count, last_selected_key, last_correct, last_seen_at, last_attempted_at, updated_at)
      values (p_user, p_progress->>'question_id', p_progress->>'subject', p_progress->>'chapter', 1, 1,
        case when (p_progress->>'correct')::boolean then 1 else 0 end, 0, p_progress->>'selected_key',
        (p_progress->>'correct')::boolean, now(), now(), now())
      on conflict (user_id, question_id) do update set
        seen_count = g.seen_count + 1, attempt_count = g.attempt_count + 1, correct_count = g.correct_count + excluded.correct_count,
        last_selected_key = excluded.last_selected_key, last_correct = excluded.last_correct,
        last_seen_at = now(), last_attempted_at = now(), updated_at = now();
  end if;
  if p_interaction is not null then
    insert into public.question_interactions (question_id, user_id, interaction_type, session_id, flow_context, metadata)
      values (p_interaction->>'question_id', p_user, 'attempted', p_run, 'learn', coalesce(p_interaction->'metadata', '{}'::jsonb));
  end if;
  update public.learn_runs set
    done_count = done_count + 1,
    seconds_left = greatest(0, seconds_left - coalesce((p_event->>'seconds')::int, 0)),
    limit_line = coalesce(p_limit_line, limit_line),
    updated_at = now()
    where id = p_run;
  return jsonb_build_object('status', 'ok', 'body', v_body, 'reinsert', v_reinsert,
    'revise_pile', (select count(*) from public.learn_run_events e where e.run_id = p_run and e.kind = 'rate' and e.rating in (3, 4)));
end;
$$;

revoke all on function public.learn_start_run(jsonb, text, text, int, text[]) from public, anon, authenticated;
grant execute on function public.learn_start_run(jsonb, text, text, int, text[]) to service_role;
revoke all on function public.learn_record_event(text, text, text, jsonb, jsonb, jsonb, jsonb, text) from public, anon, authenticated;
grant execute on function public.learn_record_event(text, text, text, jsonb, jsonb, jsonb, jsonb, text) to service_role;

-- flow_context gains 'learn'. The repo holds two definitions of the old check (0007 chk_qi_flow_context, 0010 the inline
-- question_interactions_flow_context_check), so drop whichever exists by its definition. NOT VALID then VALIDATE: the scan
-- of an append-only table runs under SHARE UPDATE EXCLUSIVE, so writes go on; every existing row already passes.
do $$
declare c record;
begin
  for c in
    select con.conname from pg_constraint con
    where con.conrelid = 'public.question_interactions'::regclass and con.contype = 'c'
      and pg_get_constraintdef(con.oid) ilike '%flow_context%'
  loop
    execute format('alter table public.question_interactions drop constraint %I', c.conname);
  end loop;
end
$$;
alter table public.question_interactions add constraint question_interactions_flow_context_check
  check (flow_context is null or flow_context in ('mock', 'review', 'explore', 'shadow', 'learn')) not valid;
alter table public.question_interactions validate constraint question_interactions_flow_context_check;
```

Notes:
- `learning_allowances` (`20261002120000_connected_learning.sql:3-6`), `learning_question_exposure` (lines 23-26) and
  `user_question_progress` (`0028:21-37`) exist in production. Production applied the Key cards migration on 31 Oct
  (`HANDOFF-2026-10-31-KEYCARDS-3.md:26-30`).
- `question_interactions.question_id` and `user_id` must be `text` for the inserts above. That is the `0010` shape. The `0005`
  shape (uuid) cannot be production, because `user_question_progress.question_id text` references `questions(id)`. The dry
  run confirms it anyway (7.3).
- `jsonb_insert` at an index equal to the length appends; the PGlite test pins it.

### 7.2 `supabase/undo/20261101150000_learn_runs.undo.sql`

```sql
-- Undo of supabase/migrations/20261101150000_learn_runs.sql. Drops the two functions and the two Learn tables with every row in
-- them (runs and their item log). What the runs recorded elsewhere stays where it belongs: user_question_progress and
-- key_card_reviews keep their rows, and question_interactions keeps its 'learn' rows as history. learning_allowances rows of
-- kind 'learn_session' are left (inert without the code); delete them only on the owner's word. Run only with the owner's grant.
drop function if exists public.learn_record_event(text, text, text, jsonb, jsonb, jsonb, jsonb, text);
drop function if exists public.learn_start_run(jsonb, text, text, int, text[]);
drop table if exists public.learn_run_events;
drop table if exists public.learn_runs;
do $$
declare c record;
begin
  for c in
    select con.conname from pg_constraint con
    where con.conrelid = 'public.question_interactions'::regclass and con.contype = 'c'
      and pg_get_constraintdef(con.oid) ilike '%flow_context%'
  loop
    execute format('alter table public.question_interactions drop constraint %I', c.conname);
  end loop;
end
$$;
-- The four old values again. NOT VALID keeps the 'learn' rows already written while refusing new ones. For a fully validated
-- check instead, first run: update public.question_interactions set flow_context = 'explore' where flow_context = 'learn';
-- then add the constraint without NOT VALID.
alter table public.question_interactions add constraint chk_qi_flow_context
  check (flow_context is null or flow_context in ('mock', 'review', 'explore', 'shadow')) not valid;
```

### 7.3 The dry run, in order
1. **PGlite** (`data/tests/learn_db.test.mjs`, the `keycards_db.test.mjs` pattern):
   - Stub `users`, `questions(id text)`, `user_question_progress` (the 0028 shape), `question_interactions` (the 0010 shape with
     its inline check), `learning_allowances` and `learning_question_exposure`.
   - Apply the migration twice (it must be idempotent).
   - Check both functions: `prosecdef = true`, `proconfig = {search_path=""}`, and execute allowed for `service_role` only.
   - Behaviours: a replay; `used`; two concurrent starts (one claim); `key_conflict`; an event replay with no double progress
     increment; the `'learn'` interaction accepted; the generic values still accepted and a bogus value refused; the re-insert
     position, once per card and not after a well-rated card; the counters.
   - Then the undo: no `learn_*` objects left, the old check back, and a `'learn'` insert refused.
2. **Production read-only pre-checks** (run by the owner or the main session):
   - `select conname, pg_get_constraintdef(oid) from pg_constraint where conrelid = 'public.question_interactions'::regclass and contype = 'c';`
   - `select column_name, data_type from information_schema.columns where table_name = 'question_interactions';`
   - `select flow_context, count(*) from public.question_interactions group by 1;`
   - `select to_regclass('public.learn_runs'), to_regclass('public.learn_run_events');` (both null)
   - `select count(*) from public.learning_allowances where kind = 'learn_session';` (0)
3. **A rolled-back production dry run:** one transaction that runs the file, asserts the objects and grants, then ends with
   `RAISE EXCEPTION 'dry run ok'`, so nothing persists (the evidence pattern of `20261017160000_revise_cards_mode.sql`). Then
   the same on staging (`onwkqxmjqjrhfbjjdydu`), applied through the migration tool, and left migrated.
4. **The production apply** by the owner (auto mode blocks production writes), after the code with `DELETION_STEPS` is
   deployed with the flag off. Then the step 2 checks again, and the undo is saved next to it.

No second migration is needed for launch. Later, an optional retention job (T23) deletes `learn_run_events` and empties
`learn_runs.items` after 30 days. `user_question_progress` and `key_card_reviews` keep the durable history.

---

## 8. Egress and performance

| Route | DB round trips (parallel) | Rows typical / heavy | Read bytes typical / heavy | Written |
|---|---|---|---|---|
| GET subject | 6 to 8 | about 380 / 2,400 | about 85 KB / 515 KB | none |
| POST runs/preview | 6 to 8 | 30 to 230 | 10 to 40 KB | none |
| POST runs (start) | 8 to 11, plus 1 function call | the preview's, plus at most 20 stamps (plus 3 label reads) | 15 to 45 KB warm; plus up to 700 KB cold full rows (shared) | 1 run, 0 to 1 allowance, at most 20 exposure rows |
| GET runs/:id | 2 | 1, plus at most 60 | about 8 KB | none |
| POST answer | 4 to 5, plus 1 function call | about 4 | about 6 to 10 KB | 1 event, 1 progress, 1 interaction (plus a run update) |
| POST rate / keep | 3 to 4, plus 2 function calls | about 3 | about 6 to 8 KB | 1 review, 1 state, 0 to 2 allowances, 1 event |
| GET end | 7 to 9 | the subject read, plus at most 60 | about 85 KB / 515 KB | 1 update |
| GET cards (chapter) | 4 | 30 to 230 | 10 to 40 KB | none |
| GET cards (subject, new) | 4 | the subject read | about 80 KB | none |
| GET shelves | 5 | the subject read, plus 10 to 50 due rows | about 85 KB | none |
| GET search | 2 | 1 | about 1.5 KB | none |
| GET covers | 6 to 8 | the subject read | about 85 KB / 515 KB | none |

Shared content (decks, links, the syllabus, the question pool, Study's units and the suspension view) comes from process
memory and costs about 0 per request.

**N+1 removed or prevented:**
1. One snapshot per request. The preview's `chapterInfo` without a cache re-filters every table per chapter; in production
   every chapter is computed from S3 and S4 in memory. A test pins a constant query count: 14 chapters ask no more than 2 do.
2. Find's shelves: 1 request instead of one per chapter (4.9).
3. A rating no longer re-reads all states: `withToday: false` (4.6). Today `review()` calls `todayNow()` on every outcome
   (`keycards.js:411-413`), which pages through every `key_card_states` row of the student (about 3,000 rows for a heavy Pro
   student).
4. The due badge reads only due rows (4.10).
5. Labels are read only for a run's mistake items (5.3), never per chapter on Learn home.

**Rules already pinned by `data/tests/egress_*` that Learn keeps:**
- `QUESTION_READ_SELECT` and the light pool, never `*` (`egress_question_reads`);
- full rows through `readRowsCached` (`question_row_cache.js`);
- 1,000-row pages and 100-id pieces (`practice_progress.js`);
- slim attempt reads through the `attempt_question_ids` function with a fallback (`egress_ids`);
- shared reads kept briefly (`ttl_memo.js`, `egress_misc`);
- the pool cache and subject token (`practice_source.js:78-100`).

**Phase 2 (optional):** one `learn_subject_facts(p_user, p_subject)` function returning S3 and S4 as compact arrays in one row.
It cuts the JSON key overhead of the two largest reads by about half (typical 85 KB to about 45 KB). Do this only if the
dashboards show it matters.

**Latency.** The snapshot is about 7 parallel calls, so one or two round-trip times (about 60 to 150 ms from Mumbai). Composing
is under 5 ms; covers compose 24 times, under 30 ms.

---

## 9. The test plan

All are `node:test`, with no network and no production. Run them with `npm run test:recovery` and the question and payment
suites, as AGENTS.md asks.

1. **`data/tests/learn_routes.test.mjs`:** `createLearn` over the extended `fakeDb`, decks built in the test (the
   `keycards_routes.test.mjs` pattern) and a fixture question index. Per handler:
   - **subject:** shapes for a new Free student and a returning Pro student; three suggestion kinds; counts true to the seeded
     tables; a failed progress read answers 503, never zeros; a held Mob question is not counted as playable; a
     passage-linked question is left out; a card suspended for everyone is left out; the AFS/CAS option filters chapters.
   - **preview:** the piles at 5, 10 and 20; Free at 20 gives the clamp line; shrink and `addNext`; recap.
   - **start:**
     - a replay by `requestKey` gives the same body, one run and one allowance row;
     - a second Free session answers 402 with `line` and `resume`;
     - a same-day re-entry to the same chapter and kind resumes;
     - Pro is unlimited;
     - `cards`, `recap` and `level` are not counted;
     - Free's 20 is clamped to 10;
     - a managed pick that fails verification is replaced;
     - no key, `correct_*` or explanation in the body;
     - exposure rows are written.
   - **getRun:** a foreign run is 404; the resumed list has only undone items.
   - **answer:**
     - grading on the server;
     - a replay gives an identical body and leaves `attempt_count` unchanged;
     - the progress increments are exact;
     - the interaction row has `flow_context 'learn'`;
     - fixed and `fixedText`;
     - a wrong answer re-inserts once per card, and never after the card was rated Got it;
     - `QUESTION_CHANGED` and `QUESTION_HELD` write nothing;
     - a non-question item answers 422;
     - an expired run answers 409.
   - **rate:**
     - Got it's stamp is a real FSRS date;
     - Missed re-inserts with "Back later in this run";
     - a retried rating leaves exactly one `key_card_reviews` row;
     - Free's 11th rating gives looks and one limit line;
     - a recap is logged as `last_look`;
     - a look and a lesson call no review;
     - `kc.review` was called with `withToday: false` (the fake's log shows no all-states page).
   - **keep:** the first Keep schedules; a card already in Revise keeps its schedule; Free past the new-card allowance answers
     402 `PRO_REQUIRED`; a replay.
   - **end:** E5 numbers and lines; the Revise pile groups; `moved` on Pro; LK15 options on Free; the feed's kept pile;
     `ended_at` is idempotent.
   - **cards:** the four filters; `lockedLine`; "Missed lately" over 7 days, plus open mistakes; the subject-wide variant equals
     the per-chapter reads put together.
   - **shelves:** `due.all === kc.dueCount` (E2); the due-only read equals the full read.
   - **search:** Free stubs never carry locked words.
   - **covers:** the order; counts at 5, 10 and 20; the Free line once used; `motif` present.
2. **`data/tests/learn_db.test.mjs`** (PGlite): section 7.3 step 1.
3. **`data/tests/learn_egress.test.mjs`:**
   - a counting fake;
   - a constant query count per route whatever the chapter count;
   - no `select('*')` and no bare `schedule` column in learn server sources (a static check);
   - parity of the chapter state between the stub read and full rows over generated schedules;
   - the progress read ordered and paged;
   - the Find shelf in one request.
4. **`data/tests/app_bearer_routes.test.mjs`:** add all 12 Learn route files to `BEARER_ROUTES`.
5. **`data/tests/learn_static.test.mjs`:**
   - no AI or paid-model import in `src/lib/server/learn*.js` or `data/learn/*.js` (no `openai`, `anthropic`, `runtimeAi`,
     `budgetLedger`);
   - no production route imports `learnPreview`, `keycardsPreview` or `keycardsMemoryDb`;
   - every route calls `learnHttp`.
6. **Parity:** `learn_preview.test.mjs` and `learn_feed.test.mjs` stay green unchanged once the preview runs `createLearn` over
   the memory client. This proves the production handlers return the bodies the renders showed.
7. **Account deletion:** a test that `DELETION_STEPS` holds `learn_run_events` before `learn_runs` (children first).
8. **`keycards_routes.test.mjs`:** stays green. Add cases for the new `review` options: `clientKey` replay, `withToday: false`,
   and that the route's behaviour is unchanged.
9. **Staging walk,** before the flag goes on:
   - one Free and one Pro test account on staging;
   - start, answer, rate, keep, end;
   - Free's second start answers 402;
   - a reload mid-run resumes;
   - the rows are checked in the tables;
   - the owner judges the result on his phone (LK19).

---

## 10. How the Flutter app calls the same routes

- **Transport:** the app's dio `ApiClient` (`flutter_app/lib/core/api/api_client.dart:65-355`) sends
  `Authorization: Bearer <access token>` and refreshes once on a 401. `auth(request)` verifies the bearer first, so every Learn
  route serves the app unchanged. CORS is not involved: Flutter is native, and `mobileCors.js` is for Capacitor origins only.
- **An interface like `KeyCardsApi`:** `LearnApi` in `lib/features/learn2/data/learn_api.dart`, one method per route:
  `subject`, `previewRun`, `startRun(requestKey: uuid)`, `run(id)`, `answer`, `rate`, `keep`, `end`, `cards`, `cardsForSubject`,
  `shelves`, `search` and `covers`. It sits behind a provider, so tests and the device demo can swap it.
- **Errors:**

  | Server answer | App error |
  |---|---|
  | 404 `LEARN_OFF` | `LearnOff`: hide every entry, as `KeyCardsOff` does |
  | 402 `FREE_SESSION_USED` | `LearnSessionUsed(line, resume)` |
  | 402 `PRO_REQUIRED` on Keep | `KeyCardsProRequired(reason)` |
  | 409 `QUESTION_CHANGED` or `QUESTION_HELD` | Skip the item with one line |
  | 409 `RUN_EXPIRED` or `RUN_ENDED` | Go to the end screen |
  | Anything else | `ApiError` |

- **Retries are safe by design:** a start retried after a timeout carries the same `requestKey`, and an answer, rating or Keep
  carries the same `itemId`. The 401 refresh-and-resend path cannot count twice.
- **No offline play:** unlike Key cards' outbox, a run is held on the server. Offline shows the existing offline state.
- **Parsing:** the app reuses `KeyCard.tryParse` (`keycards_models.dart:54-135`) for card items, the same shape as the deck
  route.
- **Order:** the app work starts after the web routes are live and the owner approves the live prototype (LK18, LK19).

---

## 11. Build order and gates

1. **Pure helpers, then the refactor** (`createLearn` plus the memory client). The preview runs production code; all existing
   tests stay green. Production behaviour does not change.
2. **The migration, its undo and the PGlite test.** The store, the functions' memory mirrors and `learn_routes.test.mjs`.
3. **`learnHttp` and the 12 routes,** behind `LEARN2_ENABLED` (off). Add `DELETION_STEPS`, the Key cards `review` options, and
   the bearer, egress and static tests. Deploy with the flag off: account deletion skips missing tables, so shipping the steps
   before the tables is safe.
4. **Client changes:** `requestKey`, `resume`, the run id in the URL, `GET /api/learn/runs/:id`, the subject-wide shelf read,
   the 402 and 409 states, the LK15 copy, and the Missed lately copy fix (T21).
5. **Pages behind the two flags:** `/learn` (v2, keeping `/learn/[id]` and `/learn/summary`), `/learn/find`, `/learn/c/[key]`,
   `/learn/c/[key]/cards`, `/learn/run` and `/explore/run`. The covers on `/explore` are already mounted.
6. **The migration:** PGlite, then staging, then the rolled-back production dry run, then the owner applies it.
7. **The staging walk** (9.9). Then the owner sets `LEARN2_ENABLED=true` and `NEXT_PUBLIC_LEARN2=on`, and redeploys.
8. **The app's `LearnApi`.**

---

## 12. Risks (also returned as findings)

- **R1, high.** A Free student who reloads mid-run starts a second run and gets 402. The client sends no request key and no
  resume (`RunPlayer.jsx:395`; the `resume` in `Suggestions.jsx:27-31` is never passed to `startRun`). The implicit resume needs
  `minutes` to equal the minutes left. Fixed by T5, T13 and the same-day re-entry rule.
- **R2, high.** Each Key card rating re-reads all of a student's states for the `today` numbers (`keycards.js:411-413`). Fixed
  by `withToday: false`.
- **R3, high.** A retried rating rates twice and uses a second Free slot (`learnPreview.js:590, 611`). Fixed by the per-item
  `clientKey`.
- **R4, high.** Open Mob paper questions in a Learn run would show their key early. Fixed by S7, failing closed.
- **R5, medium.** The `flow_context` check has two historical names. A plain `ADD CONSTRAINT` would scan an append-only table
  under an exclusive lock. Handled by drop-by-definition and `NOT VALID` then `VALIDATE`.
- **R6, medium.** If the tables exist before `DELETION_STEPS` lists them, account deletion fails closed for every Learn user
  (`20261013120000_deletion_processor.sql:17-18, 74-86`). Ship the code first.
- **R7, medium.** "Fixed" has two meanings. Learn's open mistake is "the last answer was wrong"; Review's is "wrong in a paper
  and not repaired". A mistake fixed in Learn still shows open in Review, where the repair is a paid flow. This needs the
  owner's call (D3).
- **R8, medium.** LK15 is built nowhere: the preview counts feeds only, has no 10-minute cap, and its end options for chapter
  runs offer runs Free cannot start. Built by T4; the counted kinds and the length cap need the owner (D1, D2).
- **R9, low.** Cover and chapter counts come from a presumed-eligible pool. A start that verifies managed rows can come out
  slightly shorter, which shrink says honestly.
- **R10, low.** Leaving out passage-linked questions thins English questions. Cards still play.
- **R11, low.** Preview-only data must not be copied: `flow_context` on progress rows, and the seeded "Mock 3" labels.
- **R12, low.** Production migrations need the owner's hand, because auto mode blocks production writes. Prepare the SQL,
  the undo and the checks for him.

## 13. What the owner decides

- **D1.** Does LK15 count chapter runs and feeds only (`cards`, `recap` and the 6-question level check free of the daily
  limit)?
- **D2.** For Free at 20 minutes: clamp to 10 with a line (proposed), or refuse with 402?
- **D3.** Should a right answer in Learn close the mistake on Review too? Or should Review show "Answered right in Learn on
  1 Nov" (additive)?
- **D4.** When the place of a mistake is unknown, may the label read "You missed this on 16 Oct" (proposed copy)?
- **D5.** Is the line you needed inside a run free (the preview's rule), or should it count toward Free's 3 a day?
- **D6.** Keep run logs for 30 days (proposed)?
