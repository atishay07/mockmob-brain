# BUILD-1101: Learn v2 and the Explore feed, built completely (CTO spec, 1 Nov 2026)

Binding for every builder in workflows learn-build-1101-*. The owner's words (LK20-LK23, verbatim in
mockmob-next/docs/brain/OWNER-FEEDBACK-2026-10-31-LEARN.md): the feed has no way to the next item on a computer and too
much blank space; every Accountancy cover shows the same object; the chapter run is "quite good" but needs a lot of
refinement; "build this feature completely and test out everything ... refine and think about the UI/UX of this entire
thing, the entire logic behind it, and making it more useful."

Sources this spec decides from (read the parts named in your packet; they are evidence, this file is the decision):
- `docs/brain/learn-1031/audit-1101/A5-logic.md` (rules R1-R16, tests 1-14),
- `A6-wiring.md` (production plan, migration draft, tests),
- `A7-app.md` (Flutter plan; not built in this round),
- `A1`-`A4`, `A8`, `00-critic.md` (UI audits; Part B of this file is decided from them).

Where this file and an audit disagree, this file wins. Where this file is silent, follow the audit for your area and write
what you chose into the shared notes file (below).

---

## Part 0. Ground rules for every builder

- **Worktree:** `C:/Users/atish/Desktop/mockmob copy/wt-1031-learn-v2`, branch `web/1031-learn-v2`. Next.js 16 with
  breaking changes: read `AGENTS.md` and the relevant `node_modules/next/dist/docs/` page before using a framework API
  (route `params` is a Promise).
- **Own only your packet's files** (Part 3). Never edit another packet's files. If you need a change there, write the request
  in the notes file and work around it.
- **Shared notes file:** `tmp/learn-1101/build-notes.md`. Append one line per milestone: `[S1 02:40] compose.js R3+R4 done;
  exports composeRun(..., { seconds }) unchanged signature; new item.seconds`. Read it before you integrate with another
  packet's work. Never send messages to other agents.
- **The dev server is already running** at http://localhost:3451 (hot reload). Do not start another server, emulator, Gradle
  or a second browser. Only packets whose brief says so may take screenshots, and only with ONE headless Chromium that they
  close at the end (RAM rule). Kill only processes you started.
- **No production writes of any kind, no deploy, no push.** Migrations are written and tested locally (PGlite) only.
- **Commit** your own files when your packet is green: `git add <your files>` then `git commit -m "<packet>: ..."`, ending
  the message with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. Never `git add -A`, never stash, never touch
  `logs/`, never amend or rebase. If a commit races another packet's commit, just retry.
- **Tests:** keep `npm run test:learn`, `npm run test:keycards` and `node --test src/components/learn2/run/runMath.test.mjs`
  green, plus the tests your packet adds. Run eslint on every file you changed (`npx eslint <files>`).
- **Copy rules:** plain words, sentence case, no exclamation marks, no emoji, no middle dots, no arrows appended to button
  text, 12-hour time, never "mastered", no mastery %, no "marks to recover", no build talk. One volt (accent) action per
  viewport.
- **Contract:** fields are only added, never renamed (API-CONTRACT.md). New fields are listed in Part 1.9.

---

## Part 1. Logic (decided)

The rules below are A5's R1-R16 with these decisions. "IST day" is `istDay(t)` from `data/keycards.js`.

### 1.1 Keep is honest (A5 R1, owner decision D1 taken by the CTO)
- Keep puts the card in Revise as a **new card**: the Key cards service's own add (`added_from 'manual'`, reps 0, due now).
  No review row, no rating, no Free allowance spent.
- A card already in Revise: write nothing. The stamp is its real return day (`Back Wed`), or `Due now` when it is due.
- Revise's due queue (`data/keycards.js dueQueue`): among new cards, `added_from 'manual'` come first (the student's own
  picks), then the existing chapter order. Free's 5 new a day still apply in Revise, at the first rating.
- Rail label after Keep: `Kept`. The stamp line under the card: `In Revise` (new) or `In Revise, back Wed` (held).
- The feed end: `6 kept. They are first in Revise.` (no return day: none is scheduled yet).
- On Free, Keep never shows "Pro" for a daily limit (it spends nothing). Keep shows "Pro" only for a card that is locked.

### 1.2 The feed moves forward (A5 R1)
- The feed's card pool: open cards the student does not hold yet; cards not shown in the last 3 days first (Must-know
  first, then book order); then the recently shown ones, oldest shown first. **Never a due card.** When the fresh pool runs
  out, held cards that are not due may join as looks (`look: true`, rail reads `In Revise`).
- "Shown" needs no new route: a card item counts as shown when any later item of the same run was answered, kept or saved,
  or when `GET /end` was read and the card sits before the last item reached.
- Split for feeds: cards take 35% of the time, questions the rest, with questions placed first in the flow passes.
- The feed end offers, when the chapter has due cards: `Revise 3 due cards, about 1 min` (a `cards` run of the due ids).

### 1.3 Resume (A5 R2 + A6 4.3/4.4)
- Every start sends `requestKey` (one id per start tap, kept in sessionStorage for that page). A retried start returns the
  same run.
- A feed or run start for the same chapter and kind on the same IST day, with an unfinished run, resumes it (same id,
  `resumed: { done, of }`), unless the body says `fresh: true` ("Another 10 minutes" sends it).
- After a start the page puts `?run=<id>` in its URL (`router.replace`); a reload reads `GET /api/learn/runs/:id`.

### 1.4 One rhythm (A5 R3, R3.4)
- Question slots first, cards around them (A5 R3 pseudo-code). At most one linked question per card. The last slot is the
  easiest plain question. Repair passes as specified.
- Checkpoints in feeds: after item 8, 16, ... only when 4 or more items follow.
- Tests: no two questions back to back while cards remain; longest card streak at most ceil(C/Q) + 2.

### 1.5 Honest length (A5 R4) and realistic seconds (A5 R8, owner decision D3 taken by the CTO)
- Seconds per item: cards new 18, due 12, look 10, recap 10, +8 when front plus NCERT line is over 60 words; questions
  easy 50, medium 65, hard 90, +20 when the stem is over 60 words; an open mistake 60. Every run item carries `seconds`.
- One minutes function everywhere on Learn (`compose.minutesFor`: round, with the 10 percent, at least 1).
- Fill to the nearest item; shrink only when the chapter has no more, with a reason: `pool` "This chapter has about 7
  minutes of new things today.", `cap` "One run takes at most 40 new cards, about 11 minutes.", `mistakes` "Your 3 open
  mistakes take about 4 minutes."
- `run.asked` is the length chosen; the end title and the next options use it unless shrunk.
- The pile minutes are split from the run's total so they add up to it (largest remainder).

### 1.6 LK15: Free's one Learn session a day (A5 R5; A6 D1, D2)
- Counted kinds: `mix` (a chapter run) and `feed`. Not counted: `cards` (Revise these, Study these), `recap`, `level`.
- Free lengths are clamped to 10 minutes. The 5 | 10 | 20 control stays visible (never hide features); picking 20 or
  "Your own" over 10 on Free composes 10 and shows one line under the control: `Free sessions are up to 10 minutes. Pro has
  any length.` (only then: the line is the real limit).
- **The claim happens at the first answered question**, not at the start: opening a feed, looking at cards and leaving costs
  nothing. Server row: `learning_allowances (user_id, kind 'learn_session', period '<IST day>:1', reference = run id)`.
- After the day is claimed by another run:
  - a new `mix` start is composed as Key cards only (questions and mistakes left out) with `free.text` = `Your free Learn
    session today is used, so this one is Key cards only. Questions come back tomorrow.`;
  - a new `feed` start answers 402 `{ error: 'FREE_SESSION_USED', reason: 'learn_session', line, options }`, line =
    `Your free Learn session for today is done. Explore questions stay free. Pro has as many as you like.`, options =
    Revise N due cards (if any), Quick recap of this chapter, Questions on this chapter in Explore;
  - an answer in a second tab's run answers 402 with the same line; the player ends that run calmly with the line.
- The claimed run itself (resumed later the same IST day) stays free to finish. A run claimed at 11:55 pm stays that day's.
- Free end screens after the claim never offer an option that serves questions; the lead is the line with a `See Pro` text
  key (no modal).
- Covers and the chapter page show the Free line only when the day is claimed by another run (only at the real limit).
- Pro: no row, no cap.

### 1.7 Runs count cards and never show a card twice (A5 R6, R7)
- `GET /end`: `numbers.cards` = distinct cards; the detail counts first ratings; one return date per card.
- A re-rated "again" card is logged as `last_look` (no second FSRS move, no second Free slot); its stamp stays the first
  rating's.
- A wrong answer: if the line's card is still ahead, move it to i+3 (no copy); if shown and not rated well, insert a copy at
  i+3 tagged `Back from earlier`; if not in the run, insert at i+3 tagged `The line you needed`.

### 1.8 Suggestions, mistakes, lessons, covers, search, the Free line (A5 R9-R16)
- **R9 suggestions:** no chapter named twice when another qualifies; `due` runs hold only due cards; `fix` runs hold only
  mistakes ("Fix them, about N minutes"); `next` = the first unstarted chapter in book order after the latest Learn
  activity.
- **R10 mistakes:** a mistake is retried in Learn only from an earlier IST day ("You missed this yesterday" / "in Mock 4 on
  24 Oct"); copy on a right retry: `Right this time. Back on Wed to check it held.`; `Fixed. You missed this in Mock 3 on
  16 Oct.` only when Revise retires it. In production the open mistakes are the student's Revise question cards (A5
  R10.2); in the preview keep the in-memory list but apply the IST-day rule and the copy.
- **R11 lessons:** the first unread lesson; lesson pile when length >= 20 and the lesson fits in half, or when the chapter has
  only a lesson ("Start the 6-minute lesson").
- **R12 covers:** every playable chapter (no cap of 8), For you first then book order from the next chapter (wrapping). For
  you = today's unfinished feed ("Pick up where you stopped"), else most eligible old mistakes ("2 old mistakes to fix"),
  else the chapter after the latest Learn activity with new cards ("Next after Goodwill"), else the first chapter with
  cards ("Chapter 1 of your book"). Cover data fields: Part 1.9.
- **R13 search:** drop stopwords and study words (meaning, define, definition, explain, what, which) unless nothing else is
  left; abbreviations (ioc, iod, p&l, pl, cfs, bs); one-edit fuzzy match for words of 6+ letters at half weight; stopwords
  are neither required nor scored.
- **R14 the line you needed on Free:** follows Key cards' rule (3 a day, `keycard_line` allowance) when the line's card is not
  open; otherwise the locked line.
- **R15:** over 40 overdue Key cards, a run's new cards are capped at 4 per 10 minutes and the pile says `Revise first: 46
  due`.
- **R16:** `Due now` stamp for overdue; row meta drops "today" unless from today's IST day; checkpoint line `Keep going, or
  stop here. What you kept is already in Revise.`; feed end with nothing fixed reads `Old mistakes: 1 still open`; the moved
  line never starts from "Not started"; the level run's end names the chapter to start.

### 1.9 New fields (add only; S2 writes them into API-CONTRACT.md)
- Run items: `seconds`; card items `look`, `reason` ('earlier' | 'line'); run: `asked`, `resumed`, `capped`, `free`.
- Starts: body `requestKey`, `resume`, `fresh`; 402 `FREE_SESSION_USED` `{ line, options, resume }`.
- `GET /api/learn/runs/:id` (new).
- Shrink: `reason`.
- Covers (`GET /api/learn/covers?subject=`), each cover:
  `{ key, title, ref ('Ch 2'), number (2), partTitle, unitTitle, reason|null, forYou: bool,
     hook: { front, kind, mustKnow } | null   // the chapter's opening card: its first Must-know card in book order, else its first card
     state: { key, label }, studentLine       // one true line: "3 due, 2 old mistakes" | "You stopped at 6 of 16" | "New to you"
     counts: { 5: {cards, questions, minutes}, 10: {...}, 20: {...} }, kept: n, due: n, mistakes: n, art: null }`
  plus top-level `free: null | { text, maxMinutes: 10 }`.
- The feed end: `kept: { count, line }`, `dueOffer: null | { count, minutes, run }`.

---

## Part 2. Production (decided; A6 with these changes)

- **The service:** refactor `src/lib/server/learnPreview.js` into `src/lib/server/learn.js` (`createLearn(deps)`, injectable,
  no `server-only`), `learnStore.js` (queries) and `learnHttp.js` (wrapper: flag `LEARN2_ENABLED === 'true'` and Key cards
  on, else 404 `LEARN_OFF`; `auth(request)` for cookie or bearer; persistent rate limit 120; JSON object body up to 8,000
  characters; `Cache-Control: no-store`; thrown errors 503 `LEARN_UNAVAILABLE`). The preview becomes the seed over
  `createLearn` with the memory client, and its tests become parity tests.
- **Routes** (`src/app/api/learn/`): `subject`, `runs` (POST), `runs/preview`, `runs/[id]` (GET), `runs/[id]/answer`,
  `runs/[id]/rate`, `runs/[id]/end`, `cards` (+ `?subject=&filter=`), `shelves`, `search`, `covers`. Form:
  `export const dynamic = 'force-dynamic'; export async function GET(request)` / `POST(request, { params })` with
  `const { id } = await params`. All join `data/tests/app_bearer_routes.test.mjs`.
- **Run state:** `learn_runs` + `learn_run_events` as in A6 section 7.1, with ONE change: `learn_start_run` claims nothing;
  `learn_record_event` takes `p_quota jsonb` (`{ kind: 'learn_session', day, limit: 1 }` only for Free and counted kinds and
  only for an answer event) and claims the slot in the same transaction before writing; a slot held by another run answers
  `{ status: 'used', reference }` and writes nothing. `learn_runs.session_claimed` is set when it claims.
- **Answers** record through `learn_record_event` (event, progress with `last_selected_key`, interaction with
  `flow_context 'learn'`); never `attempts`, `recovery_sessions`, credits.
- **Questions:** the shared light pool with practice eligibility (A6 4.3 step 6, A5 P3): live, not held, evidence-eligible,
  no passage-linked questions, one per family, at most 2 per concept; the key read from the live row only at answer time;
  open Mob paper questions never enter (fail closed).
- **Key cards review options:** `clientKey` (per-item replay key `'learn:' + sha256(runId:itemId).slice(0,40)`),
  `withToday: false`, `me`; the HTTP route's behaviour unchanged.
- **Account deletion:** `learn_run_events` then `learn_runs` in `DELETION_STEPS` (code ships before the tables).
- **Migration:** `supabase/migrations/20261101150000_learn_runs.sql` and `supabase/undo/20261101150000_learn_runs.undo.sql`,
  tested on PGlite (`data/tests/learn_db.test.mjs`), idempotent, functions SECURITY DEFINER with empty search_path,
  service_role only. **Saved, not applied.** The owner applies it after the rolled-back dry run (auto mode blocks production
  writes).
- **Tests:** `learn_routes`, `learn_db`, `learn_egress`, `learn_static` (no AI imports; no production route imports preview
  modules; every route calls learnHttp), bearer list, deletion order, keycards review options; all of A5 section 4.
- **Client:** `api.js` sends `requestKey`, `resume`, `fresh`; handles 402 `FREE_SESSION_USED` and 409
  `QUESTION_CHANGED|QUESTION_HELD|RUN_EXPIRED|RUN_ENDED`; `getRun(id)`.
- **Flags:** server `LEARN2_ENABLED`, client `NEXT_PUBLIC_LEARN2` (already gates the covers on the live Explore page). Both off
  in production until the owner turns them on.

### 2.1 The database interface (S2a codes against it, S2b implements it; both keep it exactly)
- `learn_start_run(p_row jsonb, p_question_ids text[]) returns jsonb` -> `{ status: 'ok' | 'replay' | 'key_conflict', id }`.
  Inserts the run (unique `(user_id, request_key)`) and the exposure rows. Claims nothing.
- `learn_record_event(p_user text, p_run text, p_item text, p_event jsonb, p_progress jsonb, p_interaction jsonb,
  p_reinsert jsonb, p_limit_line text, p_quota jsonb) returns jsonb` ->
  `{ status: 'ok' | 'replay' | 'not_found' | 'no_item' | 'used', body?, reinsert?: { item_id, at }, revise_pile?, reference?, claimed? }`.
  Order inside: lock the run `for update`; replay probe (an event for `(run, item)` returns `replay` with its body); then, when
  `p_quota` is `{ kind: 'learn_session', day: 'YYYY-MM-DD', limit: 1 }`: if a slot row of that day already references this
  run, go on; else insert the first free slot `(p_user, kind, day || ':' || slot, p_run)` `on conflict do nothing`; when no
  slot can be taken answer `{ status: 'used', reference: <the run holding it> }` and write nothing; when it claims, set
  `learn_runs.session_claimed = true` and answer `claimed: true`. Then the re-insert, the event, progress, interaction and
  counters exactly as A6 7.1.
- Key cards service: `review(userId, body, { clientKey, withToday, me })` (additive options, defaults keep today's
  behaviour); `add(userId, { cardIds, addedFrom: 'manual' })` for Keep (use the existing add path; widen nothing in the
  database: 'manual' is allowed by the check).
- The memory client (`keycardsMemoryDb.js`) mirrors both functions statement for statement, so the preview and the unit
  tests run the same rules.

## Part 3. Packets and file ownership

| Packet | Owns (only these) |
|---|---|
| **S1 engine** | `data/learn/{compose,feed,suggest,search,stamps}.js`, new `data/learn/{allowance,seconds}.js`, `src/components/learn2/run/runMath.js` (+ its test), tests `data/tests/learn_{compose,feed,suggest,search}.test.mjs` |
| **S2a service and routes** | `src/lib/server/{learnPreview,learn,learnStore,learnHttp,study}.js`, `src/app/api/learn/**`, `src/components/learn2/api.js`, tests `data/tests/learn_{preview,routes,egress,static}.test.mjs`, `data/tests/app_bearer_routes.test.mjs`, `docs/brain/learn-1031/API-CONTRACT.md` (copy it from mockmob-next first) |
| **S2b database and Key cards** | `supabase/migrations/20261101150000_learn_runs.sql`, `supabase/undo/20261101150000_learn_runs.undo.sql`, `data/tests/learn_db.test.mjs`, `src/lib/server/{keycards,keycardsMemoryDb,keycardsPreview,accountDeletion}.js`, `data/keycards.js`, `data/tests/keycards_routes.test.mjs`, `data/tests/keycards_db.test.mjs`, the deletion-order test |
| **P pages** | `src/app/(app)/learn/**` (new v2 routes behind the flag, keep lessons), `src/app/(app)/explore/**` (feed route), `src/components/learn2/links.js`, `src/app/preview/arena/**`, `src/app/(app)/AppLayoutClient.jsx` (Learn row href and focus routes only) |
| **U1 feed** | `src/components/learn2/feed/ChapterFeed.jsx`, `feed.css`, new files under `src/components/learn2/feed/` except covers, and the shared study parts in new `src/components/learn2/stage/**` |
| **U2 Explore** | `src/components/learn2/feed/ExploreCovers.jsx`, `covers.css`, `src/components/feed/DiscoveryFeed.jsx` and `src/app/(app)/explore/explore.css` (Option A behind the flag only; the live page unchanged with the flag off) |
| **S3 server fields** (after S1) | `src/lib/server/learn.js`, `src/lib/server/learnPreview.js`, `data/learn/suggest.js`, `src/components/learn2/api.js`, `docs/brain/learn-1031/API-CONTRACT.md`, their tests |
| **U3 Learn home** | `src/components/learn2/home/**`, `src/components/learn2/cards/**` |
| **U4 chapter and run** | `src/components/learn2/chapter/**`, `src/components/learn2/run/**` except `runMath.js` |

## Part B. The UI

Decided by the main session from its own look at the build (desktop 1440 in a real browser), the 139 captures in
`tmp/learn-1101/audit/` with their measurements (`index.md` section 2), and the UI audits A1-A4 and A8 in
`docs/brain/learn-1031/audit-1101/`. Where an audit proposes exact values for something this part does not fix, follow the
audit and note it in the notes file.

**What the measurements proved (index.md section 2):**
- Desktop: one mouse-wheel notch, a trackpad burst and three notches all leave the feed on the same item. Only a single
  wheel event of half the screen moves it. No visible control exists to go on. Keys work but are shown nowhere. The stage
  is 560 px of 1440 (39%), 440 px empty on each side; the card is 668 px tall for two lines of text.
- Phone: a slow 300 px swipe (36% of the screen) snaps back every time; only quick flicks advance, and not always. That is
  native scroll-snap: the nearest snap point wins. A student who drags gently is stuck too.

### B1. One study stage for the feed and the run (U1 builds the feed's, U4 the run's, from the same rules)
The feed and the run are the same kind of screen: one item at a time. They share these rules so they feel like one product.

**Layout per width (the item is never a tall empty box):**
- **Phone (under 768 px):** top bar (close, title, `3 of 21`), then the item, then a **bottom action bar** (safe-area aware)
  that holds the item's one primary key. Side padding 16 px. The card is the full content width.
- **Tablet and small laptop (768 to 1199 px):** one column 600 px wide, centred. The action bar sits right under the item,
  not at the screen's foot.
- **Desktop (1200 px and up):** three columns, centred as one group (max 1120 px): a **session panel** (240 px) on the left,
  the **stage** (640 px) in the middle, the **control column** (72 px) on the right. Gaps 40 px. Nothing else on screen.
  - The session panel holds only real numbers about this session, quiet (text-2, no boxes): the chapter title (display,
    20 px) and its ref (`Ch 2, Accountancy Part 1`), `Card 3 of 21`, `About 7 min left`, `Questions 2 of 3 right`,
    `Kept 2` with the tiny kept pile, and a `Stop here` text key (it goes to the end screen).
  - The control column holds the item's side keys (Keep or Save, Chapter) and, below them, the **pager**: two round 48 px
    keys, `Previous` (chevron up) and `Next` (chevron down), with tooltips that name the keys (`Previous (Up arrow)`,
    `Next (Down arrow)`). Disabled at the ends.
- **The card fits its content.** Both faces are measured and the card takes the taller face's height, at least 300 px on a
  phone and 360 px on desktop, at most the space between the top bar and the action bar. The item is centred vertically in
  that space. The front's type scales with its length: up to 60 characters 34 px (phone) / 44 px (desktop); up to 120
  characters 28 / 36 px; longer 22 / 28 px. Tight leading (1.12), balanced wrap.
- **The front carries more than the prompt:** the kind line (`Definition`, `Must-know` in volt text), the prompt, and at the
  foot of the face a quiet source chip (`NCERT, Accountancy Part 1, Ch 2, p. 70`) so the student knows where the answer will
  come from. The back repeats the prompt small (13 px, text-3) above NCERT's line, so turning the card never loses the
  question.

**Moving between items (a real pager, not native scroll-snap):**
- Items are laid out in a track moved with `transform: translateY` (GPU), one item per viewport height.
- **Touch:** the track follows the finger 1:1 (rubber band at the ends, 0.35 resistance). On release it goes on when the drag
  is past 18% of the height or the release velocity is over 0.35 px/ms in that direction; otherwise it springs back.
  Animation 320 ms `cubic-bezier(0.32, 0.72, 0, 1)`.
- **Wheel and trackpad:** add up deltaY within one gesture; at 60 px it moves one item and then ignores the rest of that
  gesture until the wheel has been quiet for 220 ms (so trackpad inertia moves one item, never three).
- **Keys:** Down, `j`, PageDown move on; Up, `k`, PageUp move back; Space and Enter turn an unturned card, otherwise move on;
  Home and End go to the first and the last item. Ignored while focus is in a text field.
- **Inner scroll:** an item whose content is taller than its space scrolls inside; the pager takes the gesture only at that
  scroll's top or bottom edge, in that direction.
- **The primary key** in the action bar is always visible and labelled, so no one has to know a gesture: a card shows
  `Turn over` until it is turned, then `Next`; a question shows nothing until answered, then `Next`; the checkpoint shows
  `Keep going` and `Stop here`. On the last item `Next` reads `See how it went`. It is the screen's one volt key.
- Reduced motion: no track animation (instant switch with a 120 ms cross-fade), no flip (cross-fade), no shake.
- Screen readers: the stage is a `feed` with `aria-roledescription`, each item `article` with `aria-setsize` and
  `aria-posinset`, and the live region says `Card 3 of 21` on each move.

**The card turn:** keep the 3D flip (it is the feed's signature) at 380 ms `cubic-bezier(0.32, 0.72, 0, 1)` with a light
haptic (`navigator.vibrate(8)`) where supported; the faces have the same measured height, so nothing jumps.

**A wrong answer, without covering the answers:** the other options fade to 40% (160 ms), the chosen row shakes 4 px twice
and turns the bad colour, the right row outlines volt, and **the line you needed opens in place below the options**
(height and opacity, 240 ms): its title, NCERT's line with the key words underlined, and the source. No bottom sheet over the
options. If the item now overflows, it scrolls inside (inner scroll rule above), and the primary key reads `Next`.
A right answer: the row fills volt (ink text), a 1.04 settle in 200 ms, `navigator.vibrate(12)`, and the streak chip
`4 in a row` from 3 in a row, in the top bar (phone) or the session panel (desktop).

**The subject object behind items is removed** from the feed and the run (it sat in a far corner on desktop and repeats the
same picture on every item; LK21). The chapter's identity comes from its title and number.

### B2. The run (U4) and the chapter page (U4)
- The run uses B1 completely: the session panel shows the run's piles instead of feed numbers (`Key cards 3 of 12`,
  `Questions 1 of 5`, `Your mistakes 0 of 2`, `In Revise 3` with its pile and the flight target), the card fits its
  content, and the action bar holds `Show answer`, then the three rating keys `Missed`, `Got it`, `Easy` (Got it is the volt
  one). On a phone the In Revise count sits in the top bar next to `3 of 21`.
- The chapter page is "quite good": keep its structure (title, state, `How long have you got?`, the piles, Start). Refine:
  - remove the line `Ratings join Revise. Questions are free.` (jargon, and not true on Free);
  - the piles get their minutes from the run's total (they add up to the Start key);
  - on desktop the right column `In this chapter` stays, aligned to the top of the title, with 40 px gap;
  - Free's line shows only at the real limit (Part 1.6).
- The run's end: on desktop two columns inside 880 px (left: title, the numbers, the moved line, the Revise pile; right: the
  next keys, the lead volt first). On a phone, stacked as today. Mobi stays only where he already is.

### B3. The feed (U1)
- B1 completely, plus: Keep and Chapter are the side keys of a card, Save and Chapter of a question (desktop control column;
  phone action bar: `Keep` icon key left of the primary key, `Chapter` icon key right of it, each 48 px with its label).
- Kept: the bookmark fills volt with a 1.15 pop (180 ms), a small copy of the card flies to the session panel's kept pile
  (desktop) or the top bar's kept count (phone) in 320 ms, the label becomes `Kept`, and the line under the card reads
  `In Revise` (or `In Revise, back Wed` for a held card). No "Pro" for daily limits (Part 1.1).
- Checkpoint and end per Part 1 copy; the end on desktop uses the two-column end of B2.
- Free: the feed start refused (Part 1.6) shows its line and the options as a calm full stage, no modal.
- Loading: the stage skeleton at final shape (top bar, a card of 360 px, the action bar), no spinner.

### B4. The Explore covers (U2)
- **No subject object on the covers** (LK21). Each cover is the chapter's own: a small fanned stack of three cards (the
  chapter page's pile language) with the chapter's **hook card front** on the top card (display type, up to 4 lines,
  ellipsis), the big chapter number (`2`, display 40 px, tabular) and the part (`Accountancy Part 1`) above it, then the
  title (22 px), the student's own line (`studentLine`: `3 due, 2 old mistakes` / `You stopped at 6 of 16` / `New to you`),
  and the counts line for the chosen length (`10 minutes: 12 Key cards and 5 questions`).
- One volt key in view: the `For you` cover's `Play` is volt; every other cover's `Play` is a neutral key. On a phone the
  cover that is snapped into view gets the volt key.
- Desktop: covers 280 x 380 in a row with visible previous/next arrow keys at the row's ends (48 px), keyboard arrows when
  the row has focus, and the row shows as many whole covers as fit. Phone: a snapping row, the cover 82% of the width.
- The `5 | 10 | 20 min` control stays above the row. Free: the 20 min choice shows the capped line only when chosen.
- Loading: skeleton covers at final shape; the lowercase `your subject` label while loading is gone (use the real subject
  name, or nothing).

### B5. Learn home, Find and the Key cards view (U3)
- Keep the structure (subject row, search field, three suggestions, chapters in book order). Refine density from A3: no empty
  bands inside tiles, the Pick up tile's key right under its text, tiles that align on one baseline on desktop, the subject
  row not taller than it needs to be. The search and shelves per A3. The Free note only at a real limit.

### B6. Everywhere
- Night and Day both checked. 44 px targets (48 px for the pager and action-bar keys). Visible focus. No horizontal scroll at
  360. No layout shift. Copy rules of Part 0.

### B7. Decisions on the UI audits (1 Nov, 3:15 am; these override B1-B5 where they differ)
**Feed (A1-feed.md): accepted in full, including its section 3.17 changes A to G:**
- A. No chevron pager in a control column. The action bar under the item holds a labelled `Previous` line key on the left
  (keycap `Up` on fine pointers) and the step slot on the right (the one volt key: `Turn over`, `Next`, `See how it went`,
  `Keep going`). Desktop layout is A1 3.2 exactly (panel, stage, rail; widths per band; no top bar on desktop, Close in the
  panel).
- B. Questions show a quiet `Skip` until answered. C. The turn is 340 ms. D. The streak lives in the verdict line
  (`Right. 4 in a row.`) and in the desktop panel, never as a floating chip. E. The end title is the chapter title plus the
  done line (`All 21 done in 9 min.` / `You stopped at 8 of 21.`). F. Cards are centred, questions top-aligned. G. One
  definition of "Questions" (plain questions; old mistakes on their own line) on the checkpoint, the panel and the end.
- A1's P2 items are in scope: the phone "This feed" sheet (it is the phone's visible Previous and overview) and the one-time
  nudge. Build P1 first.
- The card face on a phone: A1's rule (fits its content, min `clamp(300px, 46dvh, 380px)`, centred with a slight upward
  bias) for the feed AND the run. A4's "fill the stage" is not taken.
- A8's feed findings are part of the feed packet: F1 (the card is not a `role=button` with an aria-label that hides the
  NCERT line: the face content stays readable; `Turn over` is a real button), F2 (focus moves into the feed on mount; in
  the preview, where the feed is portalled over the shell, set `inert` on the shell while the feed is open; Escape never
  leaves the feed), F3 (solved by the line in place), F4 (a solid top bar, no content under Close), F5 (a long back fades at
  its foot and scrolls; arrows scroll it when it has focus), F7 (live regions exist before their text), F8 (every server
  error kind drawn; a 404 chapter is its own state), F9 (`reinsert.moved` never duplicates), F10 (a failed end read shows an
  error with Try again, never invented numbers; the end re-reads when revisited), F11 (resume with `?run=`, ticks filled to
  the resumed point), F14 (Day contrast: rest options by colour not opacity, upcoming ticks visible), F16, F17, F18 (a
  ref lock on answering).

**One set of study parts, owned by U1, used by U4.** U1 builds them first, in `src/components/learn2/stage/`: the stage
layout (panel, stage, rail, action bar per A1 3.2-3.6), the card face (fit type, source foot, prompt on the back), the
option row and verdict line, the line in place, the ticks, the end form (A1 3.9: title, done line, pile of real card faces,
lines, keys), and the stop sheet (A4). U1 writes a line in the notes file when each part is usable, with its import path
and props. U4 builds the chapter page first, then the run on these parts; until a part lands, U4 follows A1/A4 values.

**Covers and Explore (A2-explore-covers.md): accepted, with one condition.**
- The cover shows the feed's opening Key card (the hook) as its art, the small ref line (`Part 1, Ch 2`), the title, the
  student line, the mix line and `Play 10 minutes`; no big numeral (A2 3.5 is right: numerals repeat); no subject object on
  covers. One volt key: the For you cover's, and it does not move with scrolling. Arrows on desktop, a `1 of 14` pager on
  phones. The site's `SegmentedControl` for 5 | 10 | 20.
- Option A (covers full width under the page head, the Subject control in the head with the page's one object, a
  `Questions` heading with the filters, the right column demoted) is accepted **only behind the `NEXT_PUBLIC_LEARN2` flag
  (and always in the preview)**. With the flag off, the live Explore page must render exactly as it does today. U2 may
  edit `DiscoveryFeed.jsx` and `src/app/(app)/explore/explore.css` for this.

**Learn home, Find, cards (A3-learn-home.md): accepted in full** for U3.

**Chapter page, run, run end (A4-chapter-run.md): accepted, except:**
- the phone card does not fill the stage (see above);
- the chapter page keeps the subject object in its head (it appears once there, so it is the subject's identity, not a
  repeat); A4's numeral head is not taken.
- Accepted from A4 section 5: the end as lines (one form with the feed end), the length segment never rewrites the choice,
  questions on the page (no card face), "Everything in this chapter", the "Stop for now?" sheet, the resume row on the
  chapter page, and the Start key never under the dock (A8 F12).

**Server fields the UI needs (packet S3, after S1 is done; until then the UI codes against these names with fallbacks):**
1. Run body: `chapter: { key, title, ref, partTitle, number }`.
2. Feed end: `feed.done: { reached, of, minutes }` (minutes = first event to last, rounded, at least 1).
3. Answer body: echoes `choice`; `reinsert.moved: true` means "the card already in the list moved", never a copy.
4. Covers: `hook` = the first card item of the 10-minute feed dry run, with `hook.id`; `refLine`; `name`; `resume: null |
   { runId, done, of, minutesLeft }`; `studentLine` without due counts; top-level `history`; R12 refinements (skip a chapter
   whose feed finished today when another qualifies; "First in the syllabus"); starts from a cover send `source:
   'explore_cover'`, `forYou`, `position`, kept in `start_state`.
5. Runs preview: `shrink.addNext.ref`; `piles[].held: 'free' | null`; `resume: null | { runId, done, of, minutesLeft, kind }`;
   `firstVisit`.
6. Run end: `reviseCards: [{ id, kind, front, mustKnow }]` (at most 4); `lead.title`, `lead.minutes`, `lead.kind`.
7. Cards: `filter=due` on `GET /api/learn/cards?subject=`.
8. Suggestions: for a student with no history, the third suggestion is "Chapter 1 as a feed" (A3 3.10).
9. A missing chapter answers 404 `CHAPTER_NOT_FOUND`, and `api.js` maps it to the kind `chapter_not_found`.

**Screenshots while building (the build-and-look loop), one browser at a time:** take the lock by creating the directory
`tmp/learn-1101/browser.lock` (mkdir is atomic; if it exists, wait and retry; if it is older than 5 minutes, it is stale:
remove it and take it). Launch one headless Chromium, take your shots into `tmp/learn-1101/build/<packet>/`, close it,
remove the lock. Keep each session under 3 minutes. Look at every shot you take.
