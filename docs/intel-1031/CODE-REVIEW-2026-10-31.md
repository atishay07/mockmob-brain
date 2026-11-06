# Key cards integration: code review (31 Oct 2026, late morning)

**What was reviewed:** an independent read-only review of `web/1031-keycards` against base `0b7d6bc03`. Line numbers
refer to integration 90fddb40d.

**Results:**
- 4 high, 6 medium and 12 low findings.
- `test:keycards` passed, but no test covered the high findings.
- **Status:** H4 is fixed in 1ecb27667 (validate `sameContent`). The rest are open; see "Fix plan" at the end.

## HIGH
**H1. State reads cap at 1,000 rows** (CONFIRMED)
- **Where:** `src/lib/server/keycards.js:132` (used at :184, :226, :242, :273, :296, :341, :436). The query asks for
  5,000 rows with no order and no paging. PostgREST returns at most 1,000; see `data/practice_progress.js:83` and
  `data/db.js:1759`.
- **Failure:** a Commerce Pro student with 3 subjects added holds about 2,047 Must-know states. Every count and queue
  then comes from a random 1,000 rows.
- **Lost reviews:** `review()` misses the state of a card it just showed, inserts the review row (:327), then the state
  insert 409s (:339). The outbox retry hits the "seen" check (:306) and gets `{ok:true, replay:true}`, so the review is
  lost.
- **Fix:** `review()` reads only that card's row. Other reads page with `.order('card_id').range()`.

**H2. Older replay crashes the scheduler after the allowance is charged** (CONFIRMED by running it)
- **Where:** `keycards.js:321-326`, `data/keycards.js:113-119`.
- **Failure:** a client time on an earlier UTC day than `last_review_at` makes ts-fsrs throw `Invalid delta_t "-1"`. It
  throws after both allowance claims, so the route answers 503 forever and every retry burns a Free review.
- **Same UTC day:** `last_review_at` and `due_at` move backwards.
- **Fix:** compute the schedule before any claim. If the client time is before `last_review_at`, log the review like a
  last look and return ok, or use `max(at, last_review_at)`.

**H3. A Pro student who lapses to Free gets an unplayable queue** (CONFIRMED)
- **Where:**
  - `data/keycards.js:149-164`: `dueQueue` has no taste filter.
  - `keycards.js:271-282`, :292 and :437.
  - `ReviseRun.jsx` `KeyCardRun`.
- **Failure:** cards added while Pro stay in the queue and counts, but `review()` answers 402 `keycards` for any
  non-taste card. The player says "Today's free card reviews are used" with 0 used. Today, Review and Mobi keep
  counting them.
- **Fix:** for Free, filter the states through `canAdd` before `dueQueue` in `dueCards`, `today` and `dueCount`. Give
  the `keycards` reason its own copy.

**H4. The next validate run would quarantine 2,261 of 5,721 cards** (CONFIRMED; FIXED 1ecb27667)
- **Defect:** the id-reuse check compared the published copy, renamed to the syllabus chapter and unit, with the draft
  hash.

## MEDIUM
- **M1. The review row and the schedule update are separate writes** (`keycards.js:327-339`, "seen" check :305-307).
  - **Failure:** a lost state update is later acknowledged as `replay:true`.
  - **Fix:** one transactional RPC that does the replay check, the insert and the update with the expected `reps`. The
    table is not applied yet.
- **M2. The replay key is the clamped time** (`keycards.js:294`, :305-309; `data/keycards.js:221-226`).
  - **Failure:** a future time clamps to now and a time over 48 h old clamps to 48 h ago, both moving on every request.
    So a replay double-counts: `reps` goes up twice and two Free slots are used.
  - **Fix:** store the raw client value or a client review id in its own column (`client_key`) with the unique index on
    it. Use the clamped time only for scheduling.
- **M3. Web "Try again" sends a new timestamp** (`src/components/keycards/api.js:30`, `KeyCard.jsx:167`).
  - **Fix:** create `clientReviewedAt` once per card shown (`useRef`) and reuse it on retries.
- **M4. Every rating reads all the student's states twice** (`keycards.js:296`, :341; replay :300-302).
  - **Cost:** about 575 B per row, about 1.15 MB of egress per rating at 1,000 or more states.
  - **Fix:** read one row in `review()`. Compute `today` from slim columns without the `schedule` JSON.
- **M5. Chapter state reads at most 1,000 progress rows** (`keycards.js:175-180`, used at :184 and :389).
  - **Failure:** a read error makes every chapter "Not started".
  - **Fix:** page the read with the helper in `data/practice_progress.js`. Report unknown on error.
- **M6. The option picker shows the default as chosen when nothing is saved** (`KeycardsHome.jsx:84-88`, server
  `keycards.js:191`, :196).
  - **Failure:** tapping the checked default does nothing, so it can never be saved.
  - **Fix:** check nothing when `subject.option` is null, and let a tap on the default save it.

## LOW
- **L1.** A Free slot is claimed before a duplicate or conflicting write (`keycards.js:321`). Claim inside the M1
  transaction.
- **L2** (PLAUSIBLE). Free's 5 new cards a day is not enforced on direct reviews (`keycards.js:324`). Claim new cards
  with `newPerDay`, and answer 402 `keycard_new`.
- **L3.** Offline reviews from yesterday that sync after midnight use today's allowance (`keycards.js:295`). Use the
  IST day of the clamped client time.
- **L4** (PLAUSIBLE). Switching the AFS option to CAS leaves the AFS cards already added in Revise. Filter states by
  `sectionAllowed` in the queue.
- **L5** (PLAUSIBLE). The word-match score divides by the quote's length (`data/keycards.js:178-201`). English
  Must-know quotes have a median of 1 word, so one generic word can match. Require at least 3 shared words, or divide
  by the smaller count.
- **L6.** `LineYouNeeded.jsx:31-36`, :50 says "Both are in Revise" when the server added only the taste card. Use the
  response's `added`.
- **L7.** Card `order` restarts in each chapter, so new cards from different chapters interleave
  (`data/keycards.js:158-160`). Sort by chapter order, then card order.
- **L8.** The suspension check reads at most 1,000 reports (`keycards.js:112`). Use a view or RPC that returns only
  cards with 3 or more reports.
- **L9** (PLAUSIBLE, spec allows it). Three accounts can suspend any card for everyone. Add an account-age check and a
  daily report cap per user.
- **L10** (PLAUSIBLE). The taste is the 5 earliest Must-know cards, not the first 5 in book order, and the two differ in
  54 of 73 chapters (`data/keycards.js:51-66`). The app and the server may lock different cards. Pick one rule, pin it
  in the shared fixtures, and match the app.
- **L11.** `kinds.js:186-197` `findChapter` ignores old chapter names, so Review rows such as "Business Finance" lose
  the Key cards link. Use `resolveChapter(subject, name).key`.
- **L12** (PLAUSIBLE). The 85 re-tagged questions fail the content-hash check (`syllabus_v2.sql:504-534`,
  `content_evidence.js:25-30`), so they drop out of NTA papers instead of coming back. Re-score them, or accept a hash
  taken under the re-tag's old chapter.

## Checked and sound
- **Flag off:** every Key cards route and both `/api/me` routes answer 404 `KEY_CARDS_OFF`, and no UI entry shows.
- **Auth and Pro:** the user id comes from the session, and Pro is read fresh from the users row.
- **Database safety:** no SQL or RPC injection. RLS is on for all four new tables, with access for the service role
  only. The undo files reverse what their migrations add.
- **Content integrity:** deck sha256 matches the manifest, there are no duplicate ids, and every card is in a live
  chapter.
- **Migrations:** syllabus v2 can run twice safely.
- **Loading cost:** decks are parsed once per process (about 52 ms, 27 MB). The largest response is about 158 KB.
- **Product rules:** none broken (no mastery %, no "mastered", no "marks to recover", no paid model calls).

## Fix plan
- **Server and data:** H1, H2, H3, M1, M2, M4, M5, L1-L5, L7, L8, L10 and L12 go to one fix branch,
  `web/1031-kc-fixes`.
- **UI:** M3, M6, L6, L11 and the H3 copy are fixed after the real-deck UI branch merges, to avoid conflicts.
- **App:** L10 must match in the app, `ui/1031-keycards`.
