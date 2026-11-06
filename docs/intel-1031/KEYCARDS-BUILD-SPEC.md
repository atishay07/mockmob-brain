# Key cards and chapter state: build spec (31 Oct 2026)

**Owner decisions:** D200-D206 (`docs/brain/OWNER-MASTER-LEDGER.md`, 31 Oct).

**Companion specs:**
- `KEYCARDS-CONTENT-SPEC.md` (card format and content checks)
- `syllabus-verified.md` (syllabus rulings)

**Code map:** the integration survey (the paths below were checked against `origin/main` 0b7d6bc03 and app
`ui/1020-v16` f72207c27).

**Product rules that bind this build** (`docs/brain/CLAUDE-MASTER-HANDOVER.md` rules 4-9, and `data/prepos_insights.js`
header):
- no mastery percentage
- never the word "mastered"
- never "marks you could recover"
- a wrong answer is a hypothesis, not a label
- zero paid model calls for scheduling or diagnosis
- uncertainty means quarantine or an honest "not enough yet"

**Copy:**
- plain, sentence case
- no exclamation marks, emoji, arrows on buttons, or build talk
- 12-hour clock

## 0. Branches and worktrees (all under `C:\Users\atish\Desktop\mockmob copy\`)

| Part | Branch | Worktree | Base |
|---|---|---|---|
| Web: syllabus v2 | `web/1031-syllabus` | `wt-1031-syllabus` | `web/1031-keycards` |
| Web: Key cards server + chapter state | `web/1031-kc-server` | `wt-1031-kc-server` | `web/1031-keycards` |
| Web: Key cards screens | `web/1031-kc-ui` | `wt-1031-kc-ui` | `web/1031-keycards` |
| App: Key cards + chapter state | `ui/1031-keycards` | `wt-1031-keycards-app` | `ui/1020-v16` |
| Content (decks) | `web/1031-keycards` | `wt-1031-keycards-web` | integration branch |

**Ownership:**
- The web parts share no files except where this spec names an owner.
- `web/1031-keycards` is the integration branch. The orchestrator merges the parts in this order: syllabus, server, UI,
  content.
- Never push, deploy, or touch production; the orchestrator does that.
- Commit often on your own branch.

**Resource rules:**
- Flutter commands only through `MOCKMOB_FLUTTER_SLOTS=2 bash tool/flutter_locked.sh <args>`.
- At most one Gradle or emulator job.
- Kill every dev server, headless Chrome and Gradle daemon you start before you finish.
- Never sign in to production from a local build. Use the demo mode / fixtures.

---

## 1. Syllabus v2 (owner: `web/1031-syllabus`)

**New module `data/cuet_syllabus.js`** (pure, no I/O). It is the single source for the 15 TOP_SUBJECTS:

```js
export const SYLLABUS_YEAR = 2026; // CUET 2027 not published yet
export const SUBJECT_OPTIONS = {
  mathematics: { label: 'Section', choices: [{ id: 'B1', label: 'B1 Mathematics' }, { id: 'B2', label: 'B2 Applied Mathematics' }], default: 'B1' },
  computer_science: { label: 'Section', choices: [{ id: 'B1', label: 'B1 Computer Science' }, { id: 'B2', label: 'B2 Informatics Practices' }], default: 'B1' },
  accountancy: { label: 'Part', choices: [{ id: 'AFS', label: 'Analysis of Financial Statements' }, { id: 'CAS', label: 'Computerised Accounting' }], default: 'AFS' },
};
// one entry per chapter, in NCERT order within each CUET unit
export const CHAPTERS = [
  { key: 'business_studies.financial-management', subject: 'business_studies', name: 'Financial Management',
    title: 'Financial Management', unit: 'Business Finance', unitOrder: 9, order: 1,
    ncert: { book: 'Business Studies Part 2', code: 'lebs201', chapter: 9 },
    section: null,            // or 'A1' | 'B1' | 'B2' | 'A' | 'AFS' | 'CAS'
    cuetOnly: false,          // in CUET 2026, not in the CBSE 2026-27 board exam
    cbseClass11: false,       // Economics micro: CBSE teaches it in Class 11
    lightWeight: false },     // e.g. Eve of Independence
  ...
];
export const CHAPTER_ALIASES = { business_studies: { 'Business Finance': 'Financial Management', ... }, ... };
export const RETIRED_CHAPTERS = { chemistry: { 'Solid State': 'not_in_cuet_2026', ... }, ... };
export function resolveChapter(subject, name) {}
// -> { key, name, title, unit, section, retired: false } | { retired: true, reason, name } | null (unknown)
export function chaptersFor(subject, { option } = {}) {} // live chapters for the student's option, NCERT order
export function unitsFor(subject, { option } = {}) {}    // [{ unit, chapters: [...] }]
```

**Rules:**
- **`name` is the stored chapter string that questions use today.** Keep it unchanged unless `syllabus-verified.md`
  section 5 merges or renames it, so the released app version 16 keeps working.
- **`title` is the display title** (the exact NCERT title; for CUET-led units, the CUET title). The UI shows `title`.
- **Rebuild `CANONICAL_SYLLABUS` in `data/canonical_syllabus.js` for the 15 top subjects from `CHAPTERS`.**
  - Each unit becomes the exact CUET unit title.
  - Chapters become `name`.
  - Retired chapters are removed.
  - "Existing ... Coverage" units are removed for these 15 subjects (keep the other subjects untouched).
- **Keep every existing export and signature** of `canonical_syllabus.js`.
- **`isValidTopSyllabusPair` accepts aliases** (it resolves them first). The upload API and pipeline validators then
  write back the new `name`.
- **Fold the alias logic** in `pyq_anchors.js` LEGACY_CHAPTER_MAP and `factoryEvidence.mjs` CHAPTER_ALIASES into
  `resolveChapter`. Keep their exports as thin wrappers.
- **Rewrite `data/cuet_chapter_priorities.json`** with canonical names, keeping its shape.
- **Practice, mock and Mob selection must never serve a retired-chapter question or a question with
  `is_cuet_syllabus === false`.** Apply this in the shared selectors:
  - `data/practice_pick.js`
  - `data/nta_question_selector.js`
  - `data/mock_question_selector.js`
  - `src/lib/server/mob/deps.js`
  - `practiceSessions.js`
  - `data/mob_chapter_counts.js`
  - `dashboard/chapterGroups.mjs`
- **Option filter:** when a student has an option saved (section 2's `student_subject_options`), practice by chapter and
  mocks for that subject draw only from `section in (null, common, chosen)`.
  - Mocks already have NTA blueprint variants (`resolveNtaVariant`, `data/nta_engine.js:153`). Map B1 to core/cs and
  B2 to applied/ip. Pass the saved option where the variant is chosen today.
  - Without a saved option, behaviour is unchanged.
- **Migration file (save only, do not apply):** `supabase/migrations/20261031130000_syllabus_v2.sql`, plus
  `supabase/undo/20261031130000_syllabus_v2.undo.sql`. It must:
  - upsert `units` and `chapters` for the 15 subjects to match `CHAPTERS`, keeping ids
  - add `chapters.retired_reason text`, `chapters.chapter_key text unique`, `chapters.title text` and
    `chapters.section text`
  - set `retired_reason` on retired rows (never delete)
  - `update questions set is_cuet_syllabus=false` where (subject, chapter) is retired
  - rename merged names in `questions.chapter` (section 5 merges only)
  - record every changed question id in a new table `syllabus_v2_changes(question_id, old_chapter, new_chapter,
    old_flag)` for the undo
- **Re-tags** (questions moving from a retired or split chapter into a live chapter): produce
  `data/syllabus/retag-2026-10-31.json` = `[{ id, subject, from, to, why }]`.
  - The orchestrator fills it from an agent pass. Leave the file with `[]` plus the migration hook that applies it.
- **Tests:** a new `data/tests/cuet_syllabus.test.mjs` that pins:
  - every ruling in `syllabus-verified.md`
  - that every `name` in `CHAPTERS` is unique per subject
  - aliases resolve
  - retired chapters are rejected by `isValidTopSyllabusPair`
  - the selectors drop retired/flagged questions
  - the option filter
  - Run `npm run test:nta`, `test:recovery`, `test:subjects`, `test:learning` and `lint`. Fix what you break.
- **Do not change the other 22 subjects.**

---

## 2. Key cards server and chapter state (owner: `web/1031-kc-server`)

### 2a. Content files (bundled with the site; no Supabase egress for content)
- `data/keycards/decks/<subject>.json` follows `KEYCARDS-CONTENT-SPEC.md` section 6.
- `data/keycards/manifest.json` = `{ "<subject>": { "version": n, "sha256": "...", "cards": n } }`.
- `data/keycards/links/<subject>.json` = `{ "<questionId>": ["<cardId>", ...] }` ("The line you needed").
- **Ship one small fixture deck** (`data/keycards/decks/_fixture.json`, 6 cards across 2 chapters of
  `business_studies`) for tests. The real decks arrive from the content stage.
- `scripts/keycards/validate.mjs`:
  - implements checks 1-5 of `KEYCARDS-CONTENT-SPEC.md` section 5
  - `pdftotext` is at `/mingw64/bin/pdftotext`; PDFs are in `../ncert-books/pdf` relative to the repo, overridable by
    `KEYCARDS_NCERT_DIR`
  - printed page = PDF page index + an offset, detected per PDF by majority vote over standalone integer lines on each
    page
  - takes draft files (`ncert-books/drafts/<code>.json` = `{ code, subject, cards: [...] }`) and writes:
    - `data/keycards/decks/<subject>.json` (pass)
    - `data/keycards/quarantine/<subject>.json` (fail, with `reasons`)
    - `data/keycards/coverage/<subject>.json`
    - `data/keycards/manifest.json`
  - exits non-zero on malformed input. Card failures do not fail the run; they quarantine.
- `scripts/keycards/review-merge.mjs` merges independent-review verdicts (`ncert-books/reviews/<code>.json` =
  `[{ id, exact, important, unambiguous, importanceRight, reason }]`): any `false` moves the card to quarantine.

### 2b. Tables (migration `supabase/migrations/20261031140000_key_cards.sql` + undo; save only)

```sql
create table key_card_states (
  user_id text not null, card_id text not null, subject text not null, chapter_key text not null,
  schedule jsonb not null, reps int not null default 0, lapses int not null default 0,
  due_at timestamptz not null, last_review_at timestamptz, last_rating smallint,
  added_from text not null check (added_from in ('chapter','taste','mistake','manual')),
  added_at timestamptz not null default now(), suspended boolean not null default false,
  primary key (user_id, card_id));
create index on key_card_states (user_id, due_at) where not suspended;
create table key_card_reviews (
  id bigint generated always as identity primary key, user_id text not null, card_id text not null, card_v int not null,
  rating smallint not null check (rating in (1,3,4)), mode text not null check (mode in ('revise','study','last_look')),
  reviewed_at timestamptz not null default now(), client_reviewed_at timestamptz, scheduled_days real, elapsed_days real);
create index on key_card_reviews (user_id, reviewed_at desc);
create table key_card_reports (user_id text not null, card_id text not null, reason text not null check (char_length(reason) <= 300),
  created_at timestamptz not null default now(), primary key (user_id, card_id));
create table student_subject_options (user_id text not null, subject text not null, option text not null,
  updated_at timestamptz not null default now(), primary key (user_id, subject));
```

- **Security:** RLS on, with no browser policies (service role only, like the study tables).
- Add all four tables to `src/lib/server/accountDeletion.js`.
- `last_look` reviews are logged but never change the schedule.

### 2c. Pure rules: `data/keycards.js` (no I/O; shared by web and app through fixtures)

**Constants:**

```js
export const KEYCARD_RULES = Object.freeze({
  retention: 0.9,
  examHorizon: '2027-05-15',          // longest interval never passes this date
  free: { tastePerChapter: 5, reviewsPerDay: 10, newPerDay: 5, lineNeededPerDay: 3 },
  pro:  { newPerDayChoices: [10, 15, 25], newPerDayDefault: 15 },
  overduePauseNew: 40,
  minutesPerCard: 0.25,               // 15 seconds per card
  ratings: { missed: 1, gotIt: 3, easy: 4 },
});
```

**Functions:**
- `deckView(cards, { isPro })`:
  - In book `order`.
  - Free: the first `tastePerChapter` cards of each chapter (Must-know first among ties) come back whole. The rest come
    back as `{ id, kind, label, locked: true }`.
  - Pro: everything comes back whole.
- `dueQueue(states, cardsById, { now, isPro, newAllowanceLeft, limit })`:
  1. Due cards (`due_at <= now`), Must-know first, then by `due_at`.
  2. Then new cards: added but never reviewed, in book order, up to `newAllowanceLeft`.
  - Pause new cards when the overdue count exceeds `overduePauseNew`.
  - Skip suspended cards and cards no longer published.
- `schedule(state, rating, now)`:
  - ts-fsrs with `request_retention 0.9` and `maximum_interval` = days from `now` to `examHorizon` (at least 1).
  - Map ratings Missed=Again(1), Got it=Good(3), Easy=Easy(4). Map `ts-fsrs` `Rating`.
- `chapterAddSet(cards, chapterKey, { isPro })`:
  - Pro: all Must-know cards of the chapter.
  - Free: only its taste cards.
  - Good-to-know cards are added only by explicit choice (Pro).
- `lineNeeded(questionId, links, cardsById, fallback)`:
  - Precomputed links first.
  - Otherwise lexical: score each Must-know card of the question's chapter by token overlap between the question text +
    explanation and the card's `quote`, ignoring stopwords. Return the top 2 when the score is at least 0.35.
  - Otherwise return `[]`.
- `memoryShare(states, chapterCards, now)`:
  - FSRS retrievability at least 0.9 among the chapter's added Must-know cards.
  - Returns `{ holding, added, mustKnow }`.

### 2d. Chapter state: `data/chapter_state.js` (pure)

**Input:**
- `user_question_progress` rows (one per question: `attempt_count`, `last_correct`, `last_attempted_at`, `chapter`)
- `resolveChapter`
- the student's options
- key card states

**Counting rules:**
- Each question counts once, by its latest answer, so repeats cannot inflate it.
- Retired chapters and unknown names are skipped.
- Aliases are resolved first.

**State per chapter:**
- `n` = distinct questions answered, `right` = latest answers that were correct.
- Use the existing Wilson helper (`data/prepos_insights.js`). Do not write a new one.
- State (labels exactly as in the `Label` column):

| state | rule | Label |
|---|---|---|
| `none` | n = 0 and no cards added | Not started |
| `thin` | 0 < n < 6 | Too few answers |
| `weak` | Wilson upper < 0.55 | Needs work |
| `mid` | otherwise | Getting there |
| `strong` | Wilson lower ≥ 0.65 | Holding |

- `fading: true` when the state is `strong` and either nothing in the chapter has been answered or reviewed for 21 days,
  or under half the added Must-know cards are holding today.
- **Reason line** (Pro): "7 of 12 right on the latest try at each question" + (if cards) "Cards: 14 of 20 holding".
- **No percent shown below n = 6. Never use "mastered", "mastery" or "marks to recover".**
- **Also return:**
  - `marksLost` from `data/review_chapters.mjs`, unchanged (reuse it; do not re-implement)
  - `available = { questions, cards }` for the chapter (live question count via the cached inventory, card count from
    the deck)
- **The other weak-chapter rules stay as they are in this release.** `prepos_insights`, `mock_swot`,
  `review_chapters`, `learning_weak` and the analytics route are all left alone. Chapter state is a new read for the new
  screens. Note in `docs/brain/intel-1031/` which surfaces should move to it later.

### 2e. Server and routes

- `src/lib/server/keycards.js` loads decks once per process (a `Map`) and checks each deck's sha256 against the
  manifest. A mismatch disables that subject and logs it.
- The env flag `KEY_CARDS_ENABLED` (default off) gates every route. Off means 404 with `{ error: 'KEY_CARDS_OFF' }`.
- Use the existing `learningHttp.js` wrapper pattern: auth, rate limit, body cap. Premium = `user.isPremium`.
- Free allowances use `learning_allowances` (kinds `keycard_review`, `keycard_new`, `keycard_line`; period = IST day).

| Method + path | Body / query | Response |
|---|---|---|
| GET `/api/keycards` | — | `{ enabled, isPro, subjects: [{ subject, title, option, options?, units: [{ unit, chapters: [{ key, title, ncert:{book,chapter}, chip: 'CUET only'\|'CBSE teaches this in Class 11'\|null, cards, mustKnow, unlocked, added, due, state: { state, label, fading } }] }] }], today: { due, newLeft, reviewsLeft, minutes } }` (student's subjects only; option-filtered) |
| GET `/api/keycards/deck?chapter=<key>` | — | `{ chapter: {key,title,unit,ncert,chip}, cards: [card \| locked stub], counts: {total, mustKnow, locked}, added: [cardId] }` |
| POST `/api/keycards/add` | `{ chapter }` or `{ cardIds: [] }` | `{ added: n, today }` (Free: taste cards only; Pro: anything published) |
| GET `/api/keycards/due?limit=20` | — | `{ cards: [card + {state:{reps,lapses,due}}], today }` |
| POST `/api/keycards/review` | `{ cardId, rating: 1\|3\|4, mode: 'revise'\|'study'\|'last_look', clientReviewedAt? }` | `{ ok, next: { due_at, interval_days }, today }`. Free over `reviewsPerDay` returns 402 `{ error: 'PRO_REQUIRED', reason: 'keycard_reviews' }`. Replays with the same (cardId, clientReviewedAt) are idempotent. `clientReviewedAt` is clamped to within 48 h before server now and never in the future. |
| GET `/api/keycards/line?questionId=` | — | `{ cards: [card], source: 'linked'\|'matched'\|'none', left? }` (Free: counts `lineNeededPerDay`) |
| POST `/api/keycards/report` | `{ cardId, reason }` | `{ ok }`. At 3 distinct reports a card is suspended for everyone via a server-side quarantine list (`key_card_reports` count) until the orchestrator reviews it. |
| GET `/api/me/chapters?subject=` | — | `{ subject, option, units: [{ unit, chapters: [{ key, title, state, label, fading, n?, right?, reason?, memory?, marksLost, available }] }] }` (`n`, `right`, `reason` and `memory` for Pro only) |
| PUT `/api/me/subject-options` | `{ subject, option }` | `{ subject, option }` |

**Revise integration** (server side, owner `kc-server`):
- `src/lib/server/revise.js` `composeQueue` and `src/app/api/me/revise/route.js` add due Key cards as a third source
  `keycards`, after the existing mistake questions and study cards.
- The cap rules in `data/revise.js` are unchanged. Key cards obey their own limits (2c).
- Today's due count (`useToday` / `review_input.mjs` `reviseDue`) includes due Key cards.
- `src/services/mobi/tonight.js` counts them too, with no model call.

**Tests:**
- `data/tests/keycards.test.mjs` (rules, gating, FSRS horizon, queue limits, lineNeeded)
- `data/tests/chapter_state.test.mjs` (states, thresholds, alias/retired handling, forbidden words)
- `data/tests/keycards_routes.test.mjs` (route handlers with a fake db, 402 paths, idempotent replay)
- A 180-day simulation: a 5-subject Pro student at 10 minutes a day must have a bounded queue (never more than 60 due),
  and new cards must keep flowing at least 3 days a week.
- `npm run test:recovery`, `test:study`, `test:today`, `test:egress`, `test:app`, `lint` and `next build --webpack` must
  pass.

---

## 3. Web screens (owner: `web/1031-kc-ui`)

**Build against fixtures that match section 2e exactly** (`src/components/keycards/fixtures.js`). Put a single fetch
layer in `src/components/keycards/api.js` so integration is one file. Follow DESIGN.md, the owner's UI standards
(`C:\Users\atish\Desktop\AI OS\wiki\concepts\ui-ux-standards.md`) and the existing tokens: paper, ink, volt, slate,
`--r-*`, `--ease-out`, `--dur-ui`.

**Motion:** transform and opacity only, 150-300 ms ease-out, reduced motion respected. Night and Day both work.

### Screens
- **`/cards` (Key cards home):**
  - Subject switcher (the student's subjects).
  - Option picker (one tap) for Mathematics, Computer Science and Accountancy.
  - CUET units, each with its chapters in NCERT order. Each chapter row shows:
    - title
    - NCERT book and chapter as small secondary text
    - the chip if any
    - state label as text (with a non-colour cue)
    - "18 cards · 6 due"
    - for Free, "5 of 38 open"
  - Top line: today's due count and minutes, with one primary action "Revise now" (goes to `/review/revise`).
- **`/cards/[chapter]` (chapter deck):**
  - Header: unit, then chapter title, then the NCERT reference.
  - Three modes in one segmented control:
    - **Read:** book order. Each card shows its kind label, front as a small prompt, and back as the exact NCERT text in
      a reading style with blanked words subtly marked. The NCERT reference "Business Studies Part 1 · Ch 1 · p. 3" is
      under it, plus the optional "In short" note. Locked cards show as a quiet stub row with the count and one upgrade
      line, not a wall of locks.
    - **Study:** a card session.
      - Front first; space or tap reveals.
      - Three buttons: Missed / Got it / Easy, with keyboard 1/2/3.
      - Progress shown as "4 of 20". The end screen shows counts only.
    - **Last look:** Must-know only, fast swipe or next, nothing scheduled.
  - "Add chapter to Revise" (adds the Must-know set).
  - Pro: "Print chapter sheet", a print stylesheet of the Must-know cards with their references.
  - "Report this card" in a small overflow menu on each card.
- **Revise (`/review/revise`):**
  - The queue now plays `keycards` items with a `KeyCardRun` player (the same card UI as Study).
  - Time estimate per item type: questions 40 s, cards 15 s.
- **"The line you needed":** on the paper result / review screen, under each wrong answer, show a compact block with the
  1-2 cards from `/api/keycards/line`, an "Add to Revise" action, and the source label. Hide the block when `source` is
  `'none'`.
- **Entry points:**
  - A "Key cards" link in the Learn hub (`/learn`) and in `ChapterRows` beside `LessonLink` (per chapter).
  - A Today line, "Revise · 14 due · about 6 minutes". It reuses the existing Revise line; do not add a second one.
  - **No new top-level nav tab.**
- **Free:**
  - Upsell through the existing `UpgradeSheet` / `InlineNudge` with a new reason `keycards`.
  - Copy, factual: "Pro opens every card in every chapter and keeps them on a schedule."
  - Show the gate once per screen, never as a modal on entry.
- **States:** loading (skeleton rows), empty ("No cards for this chapter yet"), error (retry), feature off (the Learn
  link hides), sparse.

**Proof:**
- Screenshots at 390 and 1440 px, Night and Day, of `/cards`, a chapter deck in each mode, a Free and a Pro view,
  Revise with cards, and the line-you-needed block.
- Saved to `tmp/walk-1031/web/`.
- Captured with the existing headless capture scripts against `next dev` using fixtures, never production data.
- Look at every shot, fix what is off, and repeat until clean.
- `npm run lint`, `next build --webpack` and any UI tests you add must pass.

---

## 4. App (owner: `ui/1031-keycards`, Flutter in `flutter_app/`)

Mirror section 3 in the app idiom. Use the same API (section 2e) with fakes in `test/unit/keycards/support` and the
existing theme tokens, motion tokens, `showMmSheet` and `KeyButton`.

**Navigation:**
- A "Key cards" entry in the Learn door (`routes.dart` `learnDoor`) and on chapter rows in Review.
- Due cards appear inside the existing Revise screen (a third item type with the same card UI).
- No new shell tab.

**Offline:**
- Cache each opened deck (cache key `keycards_deck_<chapterKey>`, with the deck sha) and the due queue.
- Reviews go through the existing `Outbox`, with a device timestamp sent as `clientReviewedAt`.
- Show "as of 9:40 PM" on cached chapter states.

**Free/Pro:** use `AuthSnapshot.isPro` and a new `ProReason.keycards`; the upgrade sheet stays behind `PLAY_BILLING` as
today.

**Line you needed:** on the result review screen, the same as on the web.

**Other requirements:**
- Demo mode (`test/device_demo/demo_main.dart`) gets a Pro and a Free fixture student with the fixture deck.
- Golden tests for every new screen in Night and Day, saved under `test/golden/keycards/goldens/`.
- Unit tests for the queue, the gating and the outbox replay.
- `MOCKMOB_FLUTTER_SLOTS=2 bash tool/flutter_locked.sh analyze` and the keycards/learn/review test folders must pass.
- Do not bump the version and do not build a release.

---

## 5. Content (orchestrator-run waves)

**Pilot (D204):**
- Accountancy, Business Studies and Economics now (their PDFs are on disk).
- Biology and Political Science when their PDFs arrive.
- English as an authored/WordNet deck.

**Stages:**
1. **Author:** one agent per NCERT PDF writes `ncert-books/drafts/<code>.json` to `KEYCARDS-CONTENT-SPEC.md`.
2. `node scripts/keycards/validate.mjs` runs the machine checks.
3. **Review:** one independent reviewer per PDF writes `ncert-books/reviews/<code>.json`.
4. `node scripts/keycards/review-merge.mjs`, then validate again.
5. **Link:** one agent per pilot chapter maps live questions to cards and writes `data/keycards/links/<subject>.json`.
   Uncertain links are omitted.

**Publish gate:** only cards with 0 failed checks are published. The coverage report is read before release.

---

## 6. Release (orchestrator)

1. Merge the parts into `web/1031-keycards`.
2. Run the full suites and `next build --webpack`.
3. Visual pass at 390/1440, Night/Day.
4. Production migrations, after a dry-run on a PGlite or schema copy, with the undo saved:
   - syllabus v2
   - key cards
5. Re-tag pass, then a pool check per subject.
6. Deploy with `KEY_CARDS_ENABLED=true` only after the owner has seen the screens, or under the standing CTO rule if he
   says so.
7. App: version 17 build after the device walk (emulator, demo mode, screenshots against the owner's ledger).
8. Write the `STATUS.md` entry with the undo.
