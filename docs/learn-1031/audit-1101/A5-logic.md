# A5: the logic of Learn v2 and the Explore feed (audit, 1 Nov 2026)

**Scope:** the composer, the chapter page's dry run, the run, the Explore feed, suggestions, Find (search and shelves), stamps,
chapter states, the Key cards scheduler as Learn uses it, and the LK15 Free rule. Read-only audit: nothing in the repo was
changed. Owner input read: OWNER-FEEDBACK-2026-10-31-LEARN.md (LK1-LK23), DESIGN-SPEC.md, API-CONTRACT.md, CRITIQUE-1.md,
FEED-2.md, maps R3 and R4.

**What I ran:**
- `test:learn` 51 of 51 pass, `test:keycards` 76 of 76 pass, `runMath.test.mjs` 10 of 10 pass.
- Scratch simulations through the real handlers (`previewAnswer` in `src/lib/server/keycardsPreview.js`), with the
  in-memory preview student (Pro and Free, `commerce` returning and `new`), every Accountancy chapter, a Business Studies,
  an Economics and two English chapters, at 5, 10, 20, 30, 45, 60 and 120 minutes. No database, no network.
  The scripts are in this session's scratchpad (`stats.mjs`, `words.mjs`, `sim1.mjs` to `sim11.mjs`, `sim7b.mjs`,
  `order_proto2.mjs`); every number below is copied from their output.

**Data caveat (read this first):** the preview's question fixture (`data/fixtures/learn-preview-questions.json`) holds
53 questions in 7 chapters. Accountancy has questions only in Partnership Fundamentals (10), Admission (10), Change in
Profit Sharing Ratio (7) and Profit and Loss Appropriation (1). Economics has one chapter (12). Business Studies has none.
So most preview runs are cards only. I separate what is a fixture artefact from what the rules themselves do; where it
matters I re-ran the real composer with a production-like pool of 60 questions per chapter (`sim10.mjs`).

The existing tests pass because they check the seeded chapters, mostly at 10 minutes. Every finding below is outside
what they assert. Section 4 lists the tests that would have caught them.

---

## 1. Short answers to the brief's questions

**Why do the covers say "16 Key cards and 5 questions", "32 Key cards and 1 question" and "8 Key cards and 7 questions"
for the same 10 minutes?** The composer gives 45% of the time to cards (15 s each) and 55% to questions (60 s each):
545 s of budget is 16 cards and 5 questions (`data/learn/compose.js:351-356`). Time one pile cannot use flows to the
other (`:358-367`).
- Profit and Loss Appropriation has 1 question in the fixture, so its question time becomes 32 cards. This is a fixture
  artefact. Production banks will remove it for chapters that have questions.
- Change in Profit Sharing Ratio has only 8 Key cards in the deck (real data), so its card time becomes 7 questions.
  That stays true in production.
- Is it right? The minutes are honest. Two things are wrong around it:
  - the order, which puts all 32 cards before the one question (finding F3);
  - the feed's own shape rule ("about two cards per question"), which breaks on every Pro 5-minute feed (4 to 14 cards
    per question), for Free at 10 and 20 minutes (0.7 and 0.3), and whenever one pile is thin.

**Is 15 s a card and 60 s a question realistic for a 16-year-old?**
- **Cards: 15 s is short for a new card.** The median card is 35 words of front plus NCERT line (p90 60 words, max 547),
  per `stats.mjs` and `words.mjs`. Careful reading at 150 words a minute, plus thinking and rating, gives 16 to 33 s per
  card on the real runs (`sim9.mjs`, a reading model, not a measurement).
- **Questions: 60 s is about right on average.** The model gives 46 to 74 s (stem plus options median 70 words, p90 117).
  It is short for numericals and for the long ordering stems.
- **The effect:** a Pro new student's "10 minutes" models at 12.7 minutes (Partnership Fundamentals) and 12.2 minutes
  (Admission). That trips the 125% guardrail of A12.
- **The fix:** R8 (seconds per item kind, carried on each item, then recalibrated from A12 timings).

**Are due cards, open mistakes, Must-know and new cards balanced?** In a run (mix), mostly yes:
- due cards first (Must-know, then oldest due);
- then new cards (Must-know first, then book order, at most 40);
- 1, 2 or 3 open mistakes at 5, 10 and 20 minutes, retried before their card.

The problems are around the edges:
- A new run on a chapter with many due cards is all due cards. That is acceptable: due first is the right priority.
- Learn ignores Key cards' "pause new cards past 40 overdue" (low priority, R15).
- Mistakes made earlier today are retried at once, so there is no spacing (F12).
- The feed serves due cards it cannot rate (F5).

**Is the feed adaptive at all?** Barely. Only two things adapt:
- A wrong answer brings the line's card back 3 items later.
- Answered questions count as "seen", so the next feed picks unseen questions first.

Cards do not move: nothing records that a card was shown. So "Another 10 minutes" replays 14 of the same 16 cards for a
new student and 16 of 16 for a returning one (`sim3.mjs`).

**Should a missed question bring its card back later?** Yes, and it already does, 3 items later. Two changes:
- It must not create a double showing (F8).
- The missed question itself should come back the next day, not in the very next feed (F12).

**Should a card the student flips quickly be skipped next time?** No.
- A fast flip is ambiguous: it could mean "I know it", "not now" or a mis-tap.
- Instead, a card that was shown goes behind the unshown cards for 3 days, and Keep stays the only explicit signal (R1).

**Should due cards from Revise join the feed?** No.
- A feed card cannot be rated, so a due card shown there stays due and comes back in every feed.
- The feed should serve cards the student does not hold yet. Only when those run out, it may show held cards that are
  not due, as looks. It never shows a due card.
- The end screen should offer "Revise 3 due cards, about 1 min" when the chapter has due cards (R1).

---

## 2. Findings

Severity: **blocker** (must be fixed before production or before the owner sees the next build), **high**, **medium**,
**low**.

### A. The run and the chapter page's dry run

**F1 (high). False "shrink": every Free 10-minute run says "Start 9 minutes" and "This chapter has enough for about 9
minutes today", even with a full question bank.**
- **Cause:** questions come in 60 s steps, and the leftover is dropped. Free has 5 open cards (75 s); 470 s are left
  for questions, which fits 7 (420 s) and leaves 50 s unused. The run totals 495 s, times 1.1 is 9.1, so 9 minutes, and
  `shrunk = realMinutes < length` (`compose.js:390-393`).
- **Evidence:**
  - Production-like pool of 60 questions: Free is 9 minutes at 10 and 19 minutes at 20 on all four chapters tried
    (`sim10.mjs`). The arithmetic holds for any chapter where Free has its 5 open cards to play, which is every chapter
    with Key cards for a new Free student.
  - Pro Change in Profit Sharing Ratio at 5 minutes reads "4 minutes" for the same reason.
  - The preview shows it on Partnership Fundamentals, Admission and Economics for Free (`sim1.mjs`), and CRITIQUE-1 C3
    saw the symptom.
- **Knock-on effects:**
  - The Free 'start' suggestion says "Start 10 minutes" and the chapter page says "Start 9 minutes".
  - The covers read "9 minutes, 5 Key cards and 7 questions" under a "10 min" switch.
  - The run is stored as 9 minutes (`learnPreview.js:339`), so the end title says "9 minutes on ...".
  - The next-chapter option offers "9 minutes" (`learnPreview.js:673`).
- **Fix:** R4.

**F2 (medium). The shrink text names the wrong cause.**
- "This chapter has enough for about N minutes today" (`compose.js:448-456`) is said in three cases:
  - when the 40-new-card cap is the limit: at 20 minutes, Accounting Ratios (164 cards) reads "about 17 minutes" and
    Nature and Significance of Management (67 cards) "about 12" (`sim1.mjs`, Pro);
  - when only the Your mistakes pile is left in (the other piles tapped out), where the page says the chapter has
    3 minutes;
  - when the granularity of F1 bites.
- **Fix:** R4 (a reason per case).

**F3 (high). The order clusters questions and leaves long runs of cards.**
- **Evidence:**
  - Pro new, Partnership Fundamentals, 20 minutes: `ccccccLccLLLLcLcccccLcLcccccccccccccccccLL`. Four linked questions
    are back to back, then 17 cards in a row.
  - Admission at 20 minutes: `ccccLcccLccccLccLcLcLLLLcccccccccccccccccL`.
  - 5-minute runs are `cccccccccLcL` (9 cards, then 2 questions in the last 3 items).
  - The feed's own check `feedOrderProblems` fails on the 20-minute feeds of new students ('adjacent' 3 times) and on
    every Pro 5-minute feed ('ratio' 4 to 14), per `sim2.mjs`.
  - A3 is not always kept either: `orderProblems` finds 1 to 2 problems on Partnership Fundamentals 20, Admission 5 and
    20, Change in Profit Sharing Ratio 10 and 20, and Biology 5, 10 and 20 (`order_proto2.mjs`).
- **Cause:** `buildOrder` places cards first and fits each linked question into its 3-to-6 window after its card
  (`compose.js:162-216`). When the linked cards are all early (Must-know first), all their questions land early.
  "Easiest last" then leaves the tail as cards only.
- **Fix:** R3. A scratch prototype of the slot-first order cut the worst card streak from 17 to 8 (4 at 10 minutes),
  back-to-back questions from 3 to 0, and A3 problems from 2 to 1 on the same chapters (`order_proto2.mjs`).

**F4 (medium). The minutes for the same thing disagree between screens.** Four rounding rules are in use:
- `compose.minutesFor` rounds, with the 10 percent (`compose.js:62`);
- `suggest.cardRunMinutes` and `recapMinutes` round up, with the 10 percent (`suggest.js:16,20`);
- `keycards.cardMinutes` rounds up, without it (`data/keycards.js:209`);
- `pileMinutes` rounds, without it (`compose.js:415`).

Seen:
- The Principles of Management recap reads "about 5 minutes" on Learn home and "about 4 min" on the chapter page
  (`sim8.mjs`).
- Find says "Due today 9, about 3 min" where the run would say 2.
- The piles of a 10-minute run add up to 9 (4 + 3 + 2) under "Start 10 minutes".

Fix: R9.5 (one function).

### B. The Explore feed

**F5 (high). The feed does not move forward through a chapter, and it serves due cards it cannot rate.**
- Nothing records which cards were shown. Only Keep changes a card's stage. So "Another 10 minutes" composes the same
  cards: 14 of 16 repeat for a new Pro student and 16 of 16 for the returning one (`sim3.mjs`).
- Due cards come first in the feed (`DDMD...`), are shown without a rating, stay due, and return in every feed and in
  Revise.
- Fix: R1.

**F6 (high). Keep writes a fake "Got it" review.**
- Keep calls the Key cards review with rating 3 (`learnPreview.js:586-598`, `:590`). The consequences:
  1. A recall that did not happen is logged in `key_card_reviews`.
  2. FSRS starts the card at the "Good" stability: it is due in 3 days, "Back Wed".
  3. Until then it counts as "holding" in `memoryShare`, which feeds the Pro reason line and the fading test.
  4. On Free it spends one of the day's 10 ratings and one of the 5 new-card slots, so 5 Keeps leave no new cards for
     Revise or a run that day.
  5. Keep on a card already due returns its old date, which is in the past, so the stamp reads "Back later today"
     (`stamps.js:24` clamps negative days to 0). Seen in `sim3.mjs`.
  6. A Free 402 after the day's new cards turns the rail label into "Pro" (`ChapterFeed.jsx:69,394`). That limit resets
     tomorrow, so "Pro" is not honest.
- Fix: R1 (Keep adds the card to Revise as a new card, with no rating).

**F7 (high). Leaving the feed starts a new run, and on Free that locks the student out for the day.**
- The feed starts a run on every mount (`ChapterFeed.jsx:249-270`), and the server resumes only mix and cards runs
  (`learnPreview.js:258-267,501-503`).
- The Chapter key on the rail, the browser back key, a refresh, or Android reloading the tab all remount the feed.
  - Pro loses their place and gets a fresh run.
  - Free gets the 402 "One feed a day" screen, because the feed was counted at its start (`learnPreview.js:496-499,511`).
- Fix: R2.

**F8 (medium). A card can show twice in a few items.**
- A wrong answer re-inserts the line's card 3 items later (`learnPreview.js:379-389,555`). This happens even when that
  card is still ahead in the run.
- That is always the case for an open mistake, because A3 retries a mistake before its card.
- **Evidence:**
  - Free: `Mx->re kl-act-no-writ | ... | A:kl-act-no-writ | c:kl-act-no-writ`, the same card twice in a row.
  - Pro: Partnership Fundamentals and Admission.
  - Both from `sim7b.mjs`.
- The re-inserted copy is labelled "Back from earlier" (`RunPlayer.jsx:143`) even when it was never shown earlier.
- Fix: R7.

**F9 (low). A checkpoint can come 1 or 2 items before the end.**
- `feedSlots` puts one after every 8th item that is not the last (`feed.js:34`): after item 32 of 33 (P&L
  Appropriation at 10 minutes) and after 40 of 42 (20-minute feeds), per `sim2.mjs`.
- The line "stop here and save what you kept" implies that stopping saves something. Kept cards are already saved.
- Fix: R3.4 and R16.

**F10 (low). Feed end-screen copy.**
- "Fixed: 0 of 1 old mistake" is a negative under a positive label (`learnPreview.js:704`).
- The title uses the shrunk minutes (F1).
- The run-end lead and options are computed for a feed and not used.
- Fix: R16.

### C. Suggestions, Find, stamps, states and the scheduler

**F11 (medium). Suggestions say one thing and run another.**
- **'due', "Revise these":** this is a minutes-based cards run (`suggest.js:74-83`), so 4 due cards become a 2-minute run
  of 7 cards, with 3 of them new. The same goes for 5, 8, 9 and 12 due (`sim8.mjs`).
- **'fix', "Fix them, 10 minutes":** 3 mistakes plus 24 cards to fill the time (`suggest.js:84-94` leaves cards in).
- **Two suggestions name the same chapter when another qualifies**, because `prefer()` uses used chapters only as a
  tiebreak (`suggest.js:61-62`). Due and fix are both Partnership Fundamentals, while Profit and Loss Appropriation and
  Accounting Ratios also have 3 due. Due and recap are both English "Choosing the Correct Word" (`sim5.mjs`).
- **'next' is "after the last studied chapter in book order"** (`suggest.js:95-107`). For example, one Explore answer in
  chapter 12 makes it jump to 13 and skip every unstarted chapter before it. The seeded Economics student is sent to
  chapter 8 of the second book while 4 earlier chapters are unstarted (`sim5.mjs`).
- Fix: R9.

**F12 (medium). Mistakes are retried with no spacing, and in production "fixed" would have two meanings.**
- A wrong answer in Learn opens a mistake now (`learnPreview.js:543`). The very next feed or run retries it as "You
  missed this in Learn on 1 Nov" (`sim3.mjs`, feed 2 retried feed 1's miss).
- One right answer marks it "Fixed".
- In production, Revise already owns the student's wrong answers (`data/revise.js`):
  - boxes 1 to 4, due 1, 3, 7 and 21 days apart;
  - retired only after the 4th right recall;
  - seeded from `user_question_progress` rows that have `last_selected_key`.
- If Learn keeps its own open-mistake list, the same question is "Fixed" in Learn and still due in Revise.
- Fix: R10.

**F13 (medium). Lessons.**
- Only the first lesson of a chapter is ever offered (`learnPreview.js:199`, `find`). Vocabulary has 6, so lessons 2 to
  6 never appear once lesson 1 is read.
- A chapter whose only content is a lesson says "Nothing to start yet. Nothing is lined up in this chapter yet." at 5
  and 10 minutes, while its shelf lists the unread 6-minute lesson. At 20 minutes it offers that lesson (`sim8.mjs`,
  English Factual Passage).
- Fix: R11.

**F14 (medium). Search drops results for natural queries.** Every word of the query must appear
(`search.js:14-19,40-55`), stopwords included:
- "goodwill" finds 70 cards;
- "what is goodwill" finds 12;
- "goodwill meaning" finds 0;
- "revalution" (a typo) finds 0;
- "IOC" finds 0.

Repeated common words also inflate scores. "interest on capital" ranks "Fixed vs Fluctuating capital: the difference on
items related to the deed (drawings, salary, interest on capital)" above the four cards that start "Interest on capital:",
because every extra "on" and "capital" adds to the score (`sim6.mjs`, `sim11.mjs`). Fix: R13.

**F15 (medium). "The line you needed" follows a different Free rule in Learn than in Key cards.**
- Key cards' `/api/keycards/line` gives Free 3 lines a day of any card (`lineNeededPerDay`).
- Learn shows a Free student the line only when it is one of the chapter's 5 taste cards, and otherwise "part of Pro"
  (`learnPreview.js:552-553`). With 5 open cards of about 46, that is most wrong answers.
- Fix: R14.

**F16 (medium). The in-run return of a Missed card erases the lapse, and on Free it costs two ratings.**
- Missed puts the card back in the run, and its FSRS state is due tomorrow (the end groups show "1 back tomorrow").
- Rating the re-inserted card Got it is a second FSRS review minutes later (`learnPreview.js:611,622`), which moves it to
  "Back Wed" (`sim4.mjs`). A card the student did not know comes back in 3 days, like a card they knew.
- The second rating also claims a second Free review slot.
- Fix: R6.1.

**F17 (medium). The end screen counts ratings, not cards.**
- `numbers.cards` and the Revise pile groups take every rating (`learnPreview.js:634,660`). After 16 cards with one
  Missed and its re-rating, the screen says 17 cards, "16 got it, 1 missed", and "1 back tomorrow, 16 back on Wed": 17
  return dates for 16 cards (`sim4.mjs`).
- "Another 5 minutes here" says "3 new ones" even when 30 are left (`fresh: Math.min(fresh, 3)`,
  `learnPreview.js:673`), and "1 missed card" after that card was re-rated Got it.
- Fix: R6.

**F18 (low). Stamps and rows.**
- An overdue card stamps "Back later today" (`stamps.js:24`).
- The row meta says "6 of 16 done today" for a run up to 24 hours old (`learnPreview.js:241,262`).
- The Pro "moved" line celebrates "from Not started to Too few answers" (`sim4.mjs`).
- "Find your level" ends without a level: it is 6 questions and a score.
- Fix: R16.

**F19 (medium). The covers row stops at 8 chapters and picks "For you" by due cards.**
- `maxCovers: 8` (`feed.js:15`) hides Accountancy chapters 9 to 14 (Debentures to Cash Flow Statement) from the feed.
  The only other way in is the "Next chapter" chain from the feed's end.
- "For you" weighs due cards plus mistakes (`feed.js:75`), but due cards are what the feed cannot serve usefully (F5).
- Every cover draws the subject object (`ExploreCovers.jsx:56`), which is LK21. That is a design matter; I add only the
  data field it needs (R12).

### D. The LK15 Free rule

**F20 (blocker). LK15 is a feed-only rule in the preview, and it does not exist for production.**
- **What exists:**
  - one Explore feed per IST day for Free (`feed.js:61-65`, `learnPreview.js:496-499,705,740`);
  - counted when the feed starts;
  - the end screen and covers say so only at the limit.
- **What is missing:**
  1. Chapter runs are unlimited for Free: a run and a feed are two separate allowances today, while LK15 says one
     session, either kind.
  2. Free can pick 20 minutes, "Your own" up to 120 (`ChapterPage.jsx:33-36`) and a 20-minute feed: there is no
     10-minute cap.
  3. Counting at start means a mis-tap or a refresh spends the day (F7).
  4. Nothing is stored outside process memory (`L.feeds`, `learnPreview.js:89`).
  5. No mid-run or midnight rule.
- Fix: R5 is the exact server rule.

### E. Production wiring (not visible in the preview)

**F21 (blocker for production). Run state and logging have no production home.**
1. **Run state:** runs, their items and their done map live in a `Map` in memory (`learnPreview.js:89`). The
   answer/rate/end routes need persistent run state on serverless.
2. **`flow_context 'learn'`:** A6 says feed answers log with `flow_context 'learn'`, but `question_interactions` allows
   only 'mock', 'review', 'explore' and 'shadow' (`supabase/migrations/0007_schema_fixes.sql:77-79`,
   `0010_phase1_compat.sql:106-107`).
3. **`user_question_progress`:** it has no `flow_context` column (`0028_learning_progress_bookmarks.sql:21-37`). Revise
   seeds a mistake only from rows with `last_selected_key` (`data/revise.js:107-128`). The preview writes neither
   `last_selected_key` nor `correct_count`.
4. **Keep's source:** `key_card_states.added_from` is CHECK-limited to 'chapter', 'taste', 'mistake' and 'manual'
   (`20261031140000_key_cards.sql:28`). So Keep must use 'manual' unless a migration adds 'feed'.

Fix: section 3.3 (P1 to P5).

**F22 (high for production). The question pool needs the practice filters.**
- The production bank has held Mob-paper questions, passage-linked questions (`passage_group_id`, R4 map section 3a),
  families and concepts. The paper selector filters them (`data/mob_chapter_counts.js` header, `data/practice_pick.js`).
- The composer's `pickQuestions` knows only difficulty and seen.
- Without these filters, Learn would serve an English passage question with no passage, or two questions of one family
  in a run.
- Fix: P3.

---

## 3. Proposed rules

Contract rule kept: fields are only added, nothing is renamed. New fields are marked **(add)**. "IST day" is always
`istDay(t)` from `data/keycards.js` (UTC plus 5:30, `YYYY-MM-DD`), taken on the server's clock.

### 3.1 Before the owner sees the next build (P0)

#### R1. The feed moves forward, and Keep is honest

```
FEED_RULES += { restDays: 3, cardShare: 0.35, questionsFirst: true }

// The feed's card pool: cards the student does not hold yet, cards not shown lately first. Never a due card.
feedCardPool(openCards, states, shownAt, now, slots):
  rested = c => !shownAt.has(c.id) || now - shownAt.get(c.id) >= 3 * DAY
  byRest = list => [...list.filter(rested).sort(mustFirst, bookOrder),
                    ...list.filter(c => !rested(c)).sort((a, b) => shownAt.get(a.id) - shownAt.get(b.id))]
  fresh  = byRest(openCards.filter(c => !c.locked && !states.has(c.id)))   // not in Revise
  if fresh.length >= slots: return fresh
  // Too few (a Free student whose 5 open cards are all in Revise): fill with cards in Revise that are NOT due, as looks
  // (shown, never rated; the rail reads "In Revise" with their real return day). Due cards stay Revise's.
  held   = byRest(openCards.filter(c => states.get(c.id)?.reps > 0 && !states.get(c.id).suspended
                                    && Date.parse(states.get(c.id).due_at) > now)).map(c => ({ ...c, look: true }))
  return [...fresh, ...held]

// "Shown" needs no new route. A card item of a feed run counts as shown at time t when either:
//   (a) the student answered, kept or saved any item after it in that run (t = that action), or
//   (b) GET /end was read and the card sits before the last slot the student reached (t = the end read).
// The server marks it: run.done.set(itemId, { shown: true, at: t }) (it schedules nothing).
// shownAt = the latest `at` per card over this student's feed runs of the last 3 days.

composeRun(kind 'feed'): cardPool = feedCardPool(...)    // no due cards
                         split: cardShare 0.35; in the flow passes, questions take the leftover before cards
                         (10 min: 12 cards and 6 questions; 5 min: 6 and 3; 20 min: 28 and 11, before R4's fill)

POST /api/learn/runs/:id/rate { itemId, keep: true }:
  state = key_card_states(user, cardId)
  if state && !state.suspended:
      // already in Revise: write nothing
      stamp = state.reps > 0 && due_at > now ? returnDay(due_at).stamp : 'In Revise'
  else:
      // the Key cards service's own add (the existing POST /api/keycards/add path, cardIds: [cardId]):
      // reps 0, due_at now, added_from 'manual'; no review row, no rating, no allowance claim
      res = kc.add(user, { cardIds: [cardId] })
      if res.http == 402 -> 402 { reason: 'keycards' }    // cannot happen in a Free feed: it serves only open cards
      stamp = 'In Revise'
  run.done.set(itemId, { kept: true, cardId, stamp })

dueQueue (data/keycards.js:200-202): among new cards, added_from 'manual' come first (the student's own picks),
  then the existing chapter order. A kept card is the first new card Revise shows. Free's 5 new a day still apply
  there, at the first rating.

Feed end:
  kept: "6 kept. They are first in Revise."  (no return day: none is scheduled yet)
  when the chapter has due cards: a second key "Revise 3 due cards, about 1 min"
                                  -> run { kind: 'cards', chapterKey, cardIds: dueIds }
```

Why: each feed now moves on through the chapter, and nothing is scheduled or claimed that the student did not do. Keep
gets one clear meaning: "put it in my Revise".

#### R2. A feed resumes, and Free is never locked out by a refresh or the back key

```
POST /api/learn/runs { kind: 'feed', chapterKey, minutes, fresh? (add) }:
  open = latest run where kind == 'feed' && chapterKey == body.chapterKey && !ended
         && istDay(createdAt) == istDay(now) && some item not done
  if open && body.fresh !== true -> 200 runBody(open, { resumed: true })   // same id; `resumed: { done, of }` exists
  else start a new run (subject to R5 on Free)
ChapterFeed: on mount call startRun as now. When body.resumed is set, the server has sent only the items not done; draw
  resumed.done ticks as done. "Another N minutes" sends fresh: true.
```

#### R3. One rhythm for runs and feeds: question slots first, cards around them

```
// Selection: at most one linked question per card. When a picked linked question's first run card is already
// covered by a picked question, skip it and take the next one in pickQuestions order.

order(items):                                    // a lesson, when there is one, stays first
  C = cards.length, Q = questions.length, N = C + Q
  if !C or !Q -> cards, then questions (as now)
  slots: for k in 0..Q-2: s[k] = max(k + 1, round((k + 1) * (N - 1) / Q)); s[Q-1] = N - 1
  questions to slots, in this order:
    short open mistakes (oldest first)
    -> linked questions by their card's display rank
    -> chapter questions
  the last slot = the easiest plain question (unlinked first), as A3 says
  a long mistake (over 60 words) = the second-last slot, never before item 5 (as now)
  cards:
    the card of each linked question goes 4 before its slot (else 3, 5, 6), never at or before a mistake that links to it
    the other cards fill the gaps in display order:
      due cards by oldest due date,
      then new cards in book order (chosen Must-know first, shown in book order)
  repair: if orderProblems(seq) is not empty, swap two non-tail questions' slots, re-place the cards, and keep a swap
          that lowers (A3 problems x 100 + back-to-back questions x 10 + longest card streak); at most 3 passes
// Result on the fixture chapters (order_proto2.mjs):
//   10 min: ccccLcccLcccLcccLcccL (was cccccccLccLcLccccLccL)
//   worst card streak 17 -> 8 (4 at 10 min); back-to-back questions 3 -> 0; A3 problems 2 -> 1

R3.4 checkpoints: one after item k (k = 8, 16, ...) only when (items after k) >= 4.
```

#### R4. Honest length: fill to the nearest item, and shrink only when the chapter has no more

```
after the flow passes (compose.js:358-367):
  // one more item of the kind that still has items, if at least half of it fits
  for kind in (feed ? [question, card] : [card, question]):
      if left >= seconds(kind) / 2 and pool(kind) has an unused item and the question cap allows:
          add one; break
  exhausted = (cards left out   || nC == cPool.length)
           && (questions out    || nQ == qPool.length || nM + nQ >= qCap)
           && (mistakes out     || nM == min(mPool.length, mCap))
  shrunk = exhausted && realMinutes < length
  shrink.reason (add):
    'mistakes' when only Your mistakes is in
    'cap'      when the cards pile hit the 40-new-card cap and the chapter has more new cards
    'pool'     otherwise
  shrink.text:
    pool:     "This chapter has about 7 minutes of new things today."
    cap:      "One run takes at most 40 new cards, about 11 minutes."
    mistakes: "Your 3 open mistakes take about 4 minutes."
run.asked (add) = the length the student chose; run.minutes stays the real length when shrunk
  - the end title and the next options use run.asked, unless shrunk
  - feed end "Another N minutes" uses run.asked
// Check: Free Partnership Fundamentals at 10 min, 60-question pool: 5 cards + 8 questions = 555 s x 1.1 = 10.2 min.
// The key reads "Start 10 minutes"; no shrink.
```

#### R5. LK15, the exact server rule

```
LEARN_FREE = Object.freeze({ sessionsPerDay: 1, maxMinutes: 10, counted: ['mix', 'feed'] })
FREE_SESSION_DONE = 'Your free Learn session for today is done. Explore questions stay free. Pro has as many as you like.'
FREE_CAPPED       = 'Free sessions are up to 10 minutes. Pro has any length.'
FREE_CARDS_ONLY   = 'Your free Learn session today is used, so this one is Key cards only. Questions come back tomorrow.'

Where it lives:
  learning_allowances (user_id, kind 'learn_session', period `${istDay(now)}:1`, reference = run id, created_at)
  The table exists, and its primary key (user_id, kind, period) is the lock: no migration.
  todaySession(user) = that row or null.

POST /api/learn/runs/preview and POST /api/learn/runs, plan Free, kind in counted:
  asked = minutes; minutes = min(asked, 10)
  capped (add) = asked > 10 ? { asked, text: FREE_CAPPED } : null
  s = todaySession(user)
  if s && s.reference != (the run being resumed):
      feed -> 402 { error: 'FREE_SESSION_USED', reason: 'learn_session', line: FREE_SESSION_DONE }
      mix  -> compose with leaveOut += ['questions', 'mistakes'] (Key cards only, within the card limits);
              free (existing field) = { text: FREE_CARDS_ONLY }

POST /api/learn/runs/:id/answer, plan Free, run.kind in counted:
  s = todaySession(user)
  if !s: insert row (on conflict do nothing); s = todaySession(user)    // the claim is at the FIRST ANSWERED QUESTION
  if s.reference != run.id -> 402 { error: 'FREE_SESSION_USED', line: FREE_SESSION_DONE }
                              // only a second tab racing; the player ends the run there with the line

Not counted:
  'cards' (Revise these, Study these: the card limits apply)
  'recap' (nothing scheduled, no questions)
  'level' (6 questions; Explore's questions are unlimited anyway)

Mid-run:
  - The claim covers the whole run: its re-inserted items, and a pick-up later the same IST day.
  - Nothing stops a run part-way on time.
  - A run claimed at 11:55 pm stays claimed by that day.
  - A run resumed on a later IST day claims that day's row with its own id, like a new run.

Free end screens after the claim:
  - no option that serves questions;
  - the lead is the FREE_SESSION_DONE line with a "See Pro" text key (no modal);
  - the options are:
      "Revise N due cards" (cards),
      "Quick recap of this chapter" (recap),
      "Questions on this chapter in Explore" (href: Explore's list filtered to the chapter).

Covers and the chapter page show a Free line only when todaySession exists and is not the open run (D181: only at the
limit). Pro: no row, no cap.
```

Why counting at the first answer: what LK15 gives away is free questions, and a question is free only once it is
answered. Opening a feed, looking at the first card and leaving costs nothing, so a refresh or a mis-tap never spends
the day.

#### R6. The end screen counts cards, and an in-run return is a learning step

```
R6.1 POST /rate on an item with stage 'again':
  kc.review(..., mode: 'last_look')      // logged; no FSRS move; no allowance
  stamp = the stamp from the card's first rating in this run ("Back tomorrow" after Missed)
R6.2 GET /end:
  perCard = cardId -> { first: its first saved rating in run order, last: its last saved rating with dueAt }
  numbers.cards = perCard.size
  detail.cards  = counts of FIRST ratings: "15 got it, 1 missed"
  revisePile    = revisePileGroups([...perCard.values()].map(x => x.last.dueAt))   // one return date per card
  missed (for endOptions) = cards whose first rating was Missed
  "Another 5 minutes here" evidence = the real 5-minute dry run of the chapter, e.g. "10 Key cards and 2 questions"
```

#### R7. A re-insert never shows a card twice

```
on a wrong answer at question index i, with line card X (open on the plan; once per card per run, as now):
  j = index of X's first item in the run
  if j > i:                                            // X is still ahead
      move it to i + 3 when j > i + 3; else leave it   // no copy
  else if X was shown and not rated Got it or Easy in this run:
      insert a copy at i + 3, stage 'again', reason (add) 'earlier'      // tag "Back from earlier"
  else if X is not in the run:
      insert at i + 3, stage 'again', reason (add) 'line'                // tag "The line you needed"
```

### 3.2 Next (P1)

#### R8. Seconds per item that a 16-year-old can keep to

```
LEARN_RULES += {
  cardSeconds:        { new: 18, due: 12, look: 10, recap: 10 },
  cardLongWords:      60,     // front + NCERT line over 60 words: +8 s
  questionSeconds:    { easy: 50, medium: 65, hard: 90 },
  questionLongWords:  60,     // stem over 60 words: +20 s
  mistakeSeconds:     60,
}
every run item carries seconds (add); the composer, the pile minutes, the pick-up minutes (learnPreview.js:269-270) and
  the player's "min left" (runMath.js:5-19) all sum item.seconds
A12: rate and answer bodies may carry ms (add, the time on screen)
  - with usage-data consent the server keeps it on the run;
  - after 200 runs, set each constant to the median of its kind;
  - the check is that no more than 10% of runs end over 125% of their length.
```

This makes a 10-minute run smaller: Partnership Fundamentals for a new student goes from 16 cards and 5 questions to
about 12 and 5. The owner must agree (section 5, D3).

#### R9. Suggestions do what they say

```
R9.1 prefer(): chapters not yet used by another suggestion first; a used chapter only when no other qualifies
R9.2 due:  run = { kind: 'cards', chapterKey, cardIds: the chapter's due ids (at most 100), minutes: minutesFor(due x 12) }
           (no new cards are added to a due run)
R9.3 fix:  run = { kind: 'mix', chapterKey, leaveOut: ['questions', 'cards', 'lesson'], minutes: minutesFor(n x 75) }
           label "Fix them, about N minutes": the mistakes, each with its line on the answer, its card re-inserted when
           wrong (R7). Count eligible mistakes only (R10.1).
R9.4 next: the first chapter in book order whose state is 'none', after the chapter of the student's latest Learn
           activity (a run, a card rating or a Learn answer); none after it -> the first 'none' chapter in book order
R9.5 one minutes function everywhere on Learn: compose.minutesFor(seconds) (round, with the 10 percent, at least 1);
     replace suggest.cardRunMinutes/recapMinutes and keycards.cardMinutes on Learn screens
R9.6 Free with today's session used (R5): a suggestion that would serve questions says "Key cards only today" in its
     evidence line; it still starts (R5 makes the run cards only)
```

#### R10. Mistakes are spaced, and there is one meaning of "fixed"

```
R10.1 a mistake is eligible for a retry in Learn only when made on an earlier IST day (istDay(m.at) < istDay(now))
      ("You missed this yesterday"); today's misses rest a day
R10.2 production: a chapter's open mistakes = the student's Revise question cards (state 'active', due_day <= today)
      for that chapter's questions
      - a Learn retry is gradeCard() (data/revise.js:64-70), the same write as /api/me/revise/answer;
      - it does not write user_question_progress (Revise's rule: retries move no accuracy);
      - new questions in Learn do write progress, with last_selected_key (so Revise seeds them).
R10.3 copy:
      - right:   "Right this time. Back on Wed to check it held." (from gradeCard's due_day)
      - "Fixed. You missed this in Mock 3 on 16 Oct." only when gradeCard returns 'done'
      - wrong:   as now
```

#### R11. Lessons

```
lesson = the chapter's first unread lesson in catalog order (replace c.lessons.find with "first not in lessonsRead")
lesson pile shows:
  - when length >= 20 and lesson.minutes <= length / 2, or
  - at any length when the chapter has no cards and no questions (startLabel "Start the 6-minute lesson")
```

#### R12. The covers

```
covers = every playable chapter (drop the cap of 8): For you first, then book order from the chapter after it, wrapping
For you, the first that applies:
  1. today's unfinished feed                                    reason "Pick up where you stopped"
  2. the most eligible open mistakes (R10.1)                    reason "2 old mistakes to fix"
  3. the chapter after the latest Learn activity, with new cards   reason "Next after Goodwill"
  4. the first chapter with cards                               reason "Chapter 1 of your book"
cover.art (add) = { object: <chapter object id> } when a chapter object exists, else null
  (the design team owns the drawing and the fallback, LK21)
Free: counts[20] = counts[10] with capped: true (R5)
```

#### R13. Find's search

```
queryWords: drop stopwords (isStopword, data/keycards.js:216) and the study words meaning, define, definition,
  explain, what, which; keep them only when the query is nothing else
spans and score: stopwords are neither required nor scored
abbreviations, expanded before matching, a small editable list:
  ioc -> interest on capital    iod -> interest on drawings    p&l / pl -> profit and loss
  cfs -> cash flow statement    bs -> balance sheet            fifo, lifo, gdp, gnp, nnp, ndp (as words)
one edit: a word of 6 or more letters with no exact hit matches a word within edit distance 1, at half weight
```

#### R14. "The line you needed" for Free follows Key cards' rule

```
Free, wrong answer, line card not open (not a taste card):
  claim keycard_line (reference = question id, the same rule as /api/keycards/line, 3 a day)
  if claimed: show the card's line (collapsed rules as now); no re-insert (the card is not open)
  else:       the locked line, as now
```

### 3.3 Production wiring (P1 to P5, before any /api/learn route ships)

- **P1. Run state.** A `learn_runs` table:
  - columns: `id` text primary key, `user_id`, `kind`, `chapter_key`, `asked_minutes`, `minutes`, `items` jsonb (ids,
    types, question ids, card ids, seconds; no answer keys), `done` jsonb, `created_at`, `ended_at`;
  - service-role only, with RLS like `learning_allowances`;
  - indexed on (user_id, created_at desc).
  - The migration is saved first; the owner applies it.
- **P2. Logging.** Either widen `chk_qi_flow_context` to add 'learn' (a migration), or log Learn answers as 'explore'
  with `metadata.source 'learn'` (no migration).
  - The answer route updates `user_question_progress` as the interact route does: seen_count, attempt_count,
    correct_count, last_selected_key, last_correct, last_attempted_at.
- **P3. The question pool.** A chapter's Learn pool = the practice eligibility:
  - live, not held, evidence-eligible;
  - no passage-linked questions until a passage set can be served whole;
  - one per family, at most 2 per concept (`data/practice_pick.js`).
  - Pass `family` and `concept` to the composer (add) and keep its one-per-card rule (R3).
- **P4. Mistakes** come from Revise (R10.2).
- **P5. Keep** uses `added_from 'manual'` (no migration; R1).
- **Note:** `/api/questions/feed` (Explore's list) still sends `correct_answer` (R4 map). Learn's "no key before an
  answer" holds for Learn's own routes. The same question's key is reachable through Explore, which is free and
  unlimited by design.

### 3.4 Later (P2)

- **R15.** When the student has more than 40 overdue Key cards (`KEYCARD_RULES.overduePauseNew`), a run's new cards are
  capped at 4 per 10 minutes. The Key cards pile says "Revise first: 46 due".
- **R16.** Small copy and number rules:
  - `returnDay` with due at or before now gives `{ stamp: 'Due now', group: 'due now' }`.
  - Row meta drops "today" unless the run is from today's IST day.
  - The checkpoint line: "Keep going, or stop here. What you kept is already in Revise."
  - The feed end, when fixed is 0: `{ label: 'Old mistakes', text: '1 still open' }`.
  - The "moved" line only between answer-based states (never from 'none').
  - The level run's end names the chapter to start: the lowest score among its question chapters.
  - The pile minutes are split from the run's total so they add up to it (largest remainder).

---

## 4. Tests that would have caught these (add before building)

1. `learn_feed`, two feeds in a row on one chapter (Pro, new): the second shares no card with the first while the
   chapter has unshown cards.
2. `learn_feed`, no due cards: a feed never serves a due card. It serves a card held in Revise (not due) only as a look,
   and only when the cards not in Revise run out.
3. `learn_feed`, Keep: writes no `key_card_reviews` row and no allowance row; the card is the first new card in
   `/api/keycards/due`.
4. `learn_feed`, resume: a second `POST /runs` for the same chapter on the same IST day, with no `fresh`, returns the
   same run id with `resumed`. On Free it is 200, not 402.
5. `learn_compose`, honest length: for every chapter, plan and length 5, 10 and 20 with a 60-question pool, `shrunk` is
   false and the key reads the chosen length. Free Partnership Fundamentals at 10 reads "Start 10 minutes".
6. `learn_compose`, rhythm: over every fixture chapter at 5, 10 and 20 minutes, mix and feed, Pro and Free, new and
   returning:
   - no two questions are back to back while cards remain;
   - the longest card streak is at most ceil(C / Q) + 2;
   - `orderProblems` finds no more problems than today.
7. `learn_feed`, checkpoints: none with fewer than 4 items after it.
8. `learn_preview`, end numbers: `numbers.cards` = distinct cards; the Revise pile total = distinct saved cards.
9. `learn_preview`, Missed then Got it on the re-inserted card: the card's due stays tomorrow, and Free used 1 rating.
10. `learn_preview`, no double show: a wrong answer on a mistake whose card is ahead leaves every card id appearing once,
    unless it was shown before that question.
11. LK15, Free:
    - a first answer in a mix run claims the day;
    - a feed start then is 402 FREE_SESSION_USED;
    - a second mix run is cards only, with the line;
    - 20 minutes is composed as 10 with `capped`;
    - a refresh resumes;
    - 11:50 pm and 12:10 am IST are two days;
    - Pro is never limited.
12. `learn_suggest`:
    - a due run holds only due cards;
    - a fix run holds only mistakes;
    - no chapter is named twice when another qualifies;
    - a recap of 24 cards says the same minutes on Learn home and the chapter page.
13. Lessons:
    - Vocabulary offers lesson 2 after lesson 1 is read;
    - Factual Passage at 10 minutes offers its 6-minute lesson.
14. `learn_search`:
    - "goodwill meaning" finds the goodwill cards;
    - "what is goodwill" returns the "goodwill" set;
    - "IOC" finds interest on capital;
    - "revalution" finds revaluation.

---

## 5. What the owner should decide (one line each, for the lead to put to him)

- **D1. Keep:** it puts the card in Revise as a new card, with no return day until he studies it (R1), not a pretend
  "Got it" with "Back Wed".
- **D2. "Fixed":** shown only when Revise retires the mistake; otherwise "Right this time. Back on Wed to check it held."
  (R10.3).
- **D3. Time per item:** realistic seconds per item (R8) make a 10-minute run about 12 cards and 5 questions instead of
  16 and 5.
- **D4. LK15:** the claim happens at the first answered question; a second run that day is Key cards only, and a second
  feed is refused with one line (R5).
- **D5. Migrations:** approve `learn_runs` (P1) and either the `flow_context` change or the 'explore' plus metadata
  route (P2).
