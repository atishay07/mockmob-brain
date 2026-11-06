# Learn v2 data contract (slice, 31 Oct 2026)

All routes are under `/api/learn/`. In the slice they run through the development preview's real-deck source
(`/preview/arena/realdeck`, `src/lib/server/keycardsPreview.js` memory db, `?decks=real`), with the real decks, the Must-know
overlay (`data/keycards/tiers.json` when present) and real questions from `data/fixtures/learn-preview-questions.json`.
Production wiring (Supabase reads and writes) comes after the owner approves the renders. No answer key is ever sent before
an answer. Client wrappers: `src/components/learn2/api.js`. Shapes below are exact; add fields only, never rename.

```
GET /api/learn/subject?subject=accountancy
{ plan: 'free'|'pro', student: { isNew: bool },
  subjects: [{ id, name }],                       // the student's own subjects, their order
  subject: { id, name, cards, chapters, lessons },
  freeNote: string|null,                          // Free: "Free opens 5 cards in every chapter. Pro opens all 868."
  suggestions: [ Suggestion x3 ],                 // always 3, three different kinds
  parts: [{ id, title,                            // "Part 1, Partnership Accounts"
            option: null | { label: 'Your part', choices: [{ id, label }], chosen: id|null, hint },
            units: [{ title, optionId: id|null, chapters: [ChapterRow] }] }] }

Suggestion = { kind: 'pickup'|'due'|'fix'|'next'|'start'|'level'|'recap'|'search',
               title, evidence,                   // one line each
               action: { label, run?: { chapterKey, minutes, leaveOut: [] , kind: 'mix'|'recap' }, href?: string } }

ChapterRow = { key, title, ref,                   // "Ch 1"
               cards, mustKnow, due, mistakes, questions,
               lesson: null | { id, title, minutes, read: bool },
               state: { key: 'none'|'thin'|'needs_work'|'getting_there'|'holding'|'unknown', label },
               meta,                              // one true line: "3 due, no lesson yet"
               marksOpen: number|null }

POST /api/learn/runs/preview   { chapterKey, minutes, leaveOut: ['questions'|'cards'|'mistakes'|'lesson'] }
{ chapter: { key, title, ref, partTitle, unitTitle, state },
  minutes, startLabel,                            // "Start 10 minutes"
  piles: [{ id: 'cards'|'questions'|'mistakes'|'lesson', count, minutes, label, left: bool }],
  note,                                           // "Ratings join Revise. Questions are free."
  recap: { count, minutes, label },               // "Or a quick recap: the 12 Must-know lines, about 3 min"
  shrink: null | { minutes, text, addNext: null | { key, title } },
  free: null | { text },
  shelf: { cards: { count, mustKnow, inRevise }, questions: { linked, total }, mistakes: { open },
           lesson: null | { id, title, minutes, read }, print: { mustKnow, locked: bool } } }

POST /api/learn/runs   { chapterKey?, cardIds?, minutes, leaveOut, kind: 'mix'|'recap'|'cards'|'feed' }
{ id, kind, chapter: { key, title, ref }, minutes,
  items: [ { id, type: 'card', stage: 'new'|'due'|'again', card: KeyCard }
         | { id, type: 'question', origin: 'mistake'|'linked'|'chapter',
             question: { id, body, options: [{ key, text }] },
             mistake: null | { where, when } }      // "Mock 3", "16 Oct"
         | { id, type: 'lesson', lesson: { id, title, minutes } } ],
  revisePile: { count } }

POST /api/learn/runs/:id/answer  { itemId, choice }
{ correct, key, explanation, fixed: bool,           // fixed: an open mistake answered right
  line: null | { card: KeyCard }, reinsert: null | { itemId, at } }

POST /api/learn/runs/:id/rate    { itemId, rating: 1|3|4 }
{ ok, stamp,                                        // "Back Tue" | "Back in 12 days" | "Back later in this run"
  revisePile: { count }, limit: null | { text } }   // Free's 11th rating: cards continue as looks

GET  /api/learn/runs/:id/end
{ title,                                            // "10 minutes on Accounting for Partnership: Basic Concepts"
  numbers: { cards, questions, fixed },
  lines: [{ label, text }],                         // "Cards" / "9 got it, 2 easy, 2 missed"
  revisePile: [{ label, count }],                   // "back on Tue" 6
  moved: null | string, free: null | { text },
  lead: { label, evidence, run|href }, options: [{ label, evidence, run|href }] x3 }

GET  /api/learn/cards?chapter=&filter=all|must|revise|missed
{ chapter: { key, title, ref }, plan, counts: { all, must, revise, missed },
  sections: [{ title, cards: [KeyCard & { inRevise: bool, missedLately: bool, locked: bool }] }],
  lockedLine: null | string }

GET  /api/learn/shelves?subject=
{ due: { count, minutes }, missed: { count }, revise: { count, chapters }, must: { count, chapters } }

GET  /api/learn/search?subject=&q=
{ chapters: [{ key, title, cards }], lessons: [{ id, title, chapterKey }],
  cards: [{ card: KeyCard, chapterKey, chapterTitle }] }
```

KeyCard is the existing Key card shape the current UI renders (`src/components/keycards/KeyCard.jsx`), with `importance`
already overlaid by the Must-know tiers.

---

## Production and BUILD-1101 additions (1 Nov 2026)

Everything above stays. The routes are now real (`src/app/api/learn/**`, one service `src/lib/server/learn.js` over
Supabase through `learnHttp.js`); the development preview runs the same service over the in-memory client. Fields below are
ADDED; nothing above is renamed. The one exception is the preview-only 402 code `FREE_FEED_USED` (`reason: 'learn_feed'`),
replaced by `FREE_SESSION_USED` (`reason: 'learn_session'`); clients read only the status and `line`.

### Every route
- Off: 404 `{ error: 'LEARN_OFF' }` unless `LEARN2_ENABLED=true` and Key cards are on (the client flag is `NEXT_PUBLIC_LEARN2`).
- Auth: bearer token (the app) or cookie (the website); 401 `{ error: 'Unauthorized' }`. Rate limit 120 a minute: 429.
- Writes: a JSON object body of at most 16,000 characters (413 `BODY_TOO_LARGE`, 422 `INVALID_BODY`); the 100 longest real card ids make a 10,016-character start body.
- `Cache-Control: no-store`. Anything that could not be read: 503 `{ error: 'LEARN_UNAVAILABLE', message }` (never a zero for
  "could not look").

### GET /api/learn/subject
```
+ free: null | { text, maxMinutes: 10 }      // Free, only when today's session is used (the real limit)
+ roadmap: null | {                           // R2 rulings 1 to 3 (data/learn/roadmap.js); Learn home leads with it
    mode: 'pickup' | 'freeDone' | 'new' | 'today',
    headline, line, sub: string|null,         // "Start learning Accountancy" / "Pick up Admission of a Partner" /
                                              // "Today's 10 minutes in Accountancy" / "That was today's free session."
    progress: null | { done, of },            // pickup only
    key: { label, run? | href?, go? },        // "Start chapter 1 · 10 min" / "Continue · 6 min" / "Start · 10 min" / "See Pro"
    quiet: null | { label, href, go },        // freeDone: "Answer single questions" -> /explore
    or: [{ kind: 'level'|'feed'|'fix', label, line, run? | href? }] (at most 2),
    position: null | { chapterKey, index, of }, chapter: null | { key, title, seen, of, unseen } }
  today's key.run is a mix on the position chapter with cardIds = due cards (at most 40 percent of the minutes)
parts[].units[].chapters[] + progress: { of, seen, unseen, questions, tried }   // coverage, never mastery; feed cards count as seen
                           + verdict: 'Needs work' | null   + unit
```

### GET /api/learn/home?subject= (new, R2 speed.md item 3)
```
the /subject body + shelves (the /shelves body) from ONE snapshot; shelves.due.all is the sum of shelves.due.bySubject.
The shell's due badge shares this answer (learn2/api.js, a 30 s module cache cleared by every write and a run's end).
/subject and /shelves stay for the app.
```

### POST /api/learn/runs/preview
```
body: minutes over 10 on Free are composed at 10
+ asked: number                               // the length the student chose
+ capped: null | { asked, text }              // Free past 10: "Free sessions are up to 10 minutes. Pro has any length."
+ freeSession: null | { used: bool, maxMinutes: 10, line: string|null }   // null on Pro
  free: { text } is "Your free Learn session today is used, so this one is Key cards only. Questions come back tomorrow."
        when another run used today's session (the piles are then Key cards only)
  shrink + reason: 'pool'|'cap'|'mistakes' (from the composer, packet S1)
```

### POST /api/learn/runs (start, feed start, resume)
```
body + requestKey: 8-100 of [A-Za-z0-9_-]     // one id per start tap; a retried start returns the same run (else 422 INVALID_REQUEST_KEY)
     + resume?: run id                        // the student's own unfinished run under 24 hours: answered resumed
     + fresh?: true                           // "Another 10 minutes": never resume
     + kind: + 'level'
     A start of the same chapter and kind (mix or feed) on the same India day, with that run unfinished, resumes it.
     A mix with chapterKey AND cardIds is "Today's 10 minutes" (R2): the cards that are due, open and in the subject play first
     (oldest due first, at most 40 percent of the minutes), then the chapter's new cards and questions, and one open mistake
     second-last. start_state.today = { due }.
answer + asked: number                        // the length chosen (Free: at most 10)
       + resumed: null | { done, of }         // a resume sends only the items not done
       + added: null | { key, title }   + looks: null | { text }
       + free: null | { text }                // Key cards only, see above
       + capped: null | { asked, text }
       + shrink: null | { reason, text }
items  + every item: seconds
       + card: look: bool, recap: bool, reason?: 'earlier' | 'line'   // a copy "Back from earlier" / "The line you needed"
       + question: mistake: null | { where, when, label }             // "You missed this in Mock 4 on 24 Oct", "You missed this yesterday"
402 { error: 'FREE_SESSION_USED', reason: 'learn_session',
      line: 'Your free Learn session for today is done. Explore questions stay free. Pro has as many as you like.',
      options: [{ label, run|href }],        // Revise N due cards, Quick recap of this chapter, Questions on this chapter in Explore
      resume: null | { id, chapterKey, title, done, of, minutesLeft, kind } }   // a feed start on Free after the day is used
409 { error: 'IDEMPOTENCY_CONFLICT' }         // the same requestKey for another chapter or kind
```
LK15: Free's one Learn session a day counts `mix` and `feed`; `cards`, `recap` and `level` are free of it. The day is claimed
at the first answered question of such a run, not at the start.

### GET /api/learn/runs/:id (new)
```
200 the start answer of that run, resumed: { done, of }, only the items not done
404 RUN_NOT_FOUND (also another student's run)
409 { error: 'RUN_ENDED', endHref } | { error: 'RUN_EXPIRED', endHref }   // a run takes answers for 48 hours
```

### POST /api/learn/runs/:id/answer
```
+ retired?: bool                 // a retried mistake that Revise now retires
  fixed: true for a mistake answered right; fixedText:
         "Right this time. Back on Wed to check it held."  (still in Revise)
         "Fixed. You missed this in Mock 3 on 16 Oct."      (retired)
  line: null | { card, source, collapsed } | { card: locked stub, locked: true, text }
        Free: a line whose card is not open takes one of Key cards' 3 lines a day; past them, the locked line
  reinsert: null | { itemId, at, item, moved?: true }   // moved: the card was ahead and came closer (no copy)
402 FREE_SESSION_USED (as above, options [])            // an answer in a second tab's run after the day is used
409 QUESTION_CHANGED | QUESTION_HELD | RUN_ENDED | RUN_EXPIRED   // nothing written
422 ITEM_NOT_A_QUESTION | INVALID_CHOICE
```
A retried mistake is graded as Revise grades it (its card moves) and moves no accuracy; a new question records progress
with the key chosen, so a wrong one becomes a Revise question card the next day.

### POST /api/learn/runs/:id/rate
```
{ itemId, rating: 1|3|4 }
+ replay?: true                   // the same item again: the first answer, nothing rated twice
+ again?: true                    // a card rated earlier in this run, back again: a last look; stamp = its first stamp
+ saved?: false, look?: true      // a look (Free past its ratings)
+ reinsert: null | { itemId, at, item }   // Missed: "Back later in this run"
{ itemId, keep: true }            // the feed's Keep
-> { ok, kept: true, stamp, line, revisePile, limit: null }
   a card not in Revise joins it as a new card (Key cards' add, added_from 'manual'; no rating, no allowance):
     stamp 'In Revise', line 'In Revise'
   a card already in Revise: nothing written; stamp 'Back Wed' | 'Due now', line 'In Revise, back Wed' | 'In Revise, due now'
   402 { error: 'PRO_REQUIRED', reason } only for a locked card
409 RUN_ENDED | RUN_EXPIRED; 422 ITEM_NOT_A_CARD | INVALID_RATING
```

### GET /api/learn/runs/:id/end
```
+ numbers.mistakes, numbers.detail { cards, questions, fixed }
  numbers.cards counts distinct cards; detail.cards counts first ratings; the Revise pile has one return date per card
  title uses the length chosen unless the run was shrunk
  Free after today's session: lead = { line, label: 'See Pro', href: '/pricing', go: 'pro' }; options never serve questions
+ feed: null | { title,
          kept: { count, cards, groups, stamp, line },   // line: "6 kept. They are first in Revise."
          lines: [{ label, text }],                      // "Old mistakes" / "1 still open" when none was fixed
          lead: null | { label: 'Another 10 minutes', run: { kind: 'feed', chapterKey, minutes, fresh: true } },
          free: null | { text },
          next: null | { label, key, run: null | {...} },
          dueOffer: null | { count, minutes, label, run: { kind: 'cards', chapterKey, cardIds, minutes } } }
```
Ending is idempotent: a second read returns the same numbers.

### GET /api/learn/cards
```
?chapter=&filter=          as above, + counts.total, + lockedCount
?subject=&filter=          (new) Find's shelf in one request:
{ plan, filter, lockedCount, chapters: [{ key, title, ref, counts, cards: [...] }] }
```

### GET /api/learn/shelves
```
+ due.all (every subject, the Key cards service's own due count), due.subjects, missed.days
```

### GET /api/learn/covers?subject= (new)
```
{ subject: { id, name }, lengths: [5, 10, 20],
  covers: [{ key, title, ref: 'Ch 2'|null, number: 2|null, partTitle, unitTitle,
             reason: string|null,          // For you only: "Pick up where you stopped" | "2 old mistakes to fix" |
                                           //   "Next after Goodwill" | "Chapter 1 of your book"
             forYou: bool,
             hook: null | { id, front, kind, mustKnow },   // = counts[10].hook (F4 below): the first card of the 10-minute feed
             state: { key, label },
             studentLine,                  // one true line: "3 due, 2 old mistakes" | "You stopped at 6 of 16" | "New to you"
             counts: { 5: { cards, questions, minutes, hook, shrink?, capped? }, 10: {...}, 20: {...} },   // Free: 20 is composed as 10 (see F4)
             kept, due, mistakes, art: null }],
  free: null | { text, maxMinutes: 10 } }  // Free, only once today's session is used
```
Every playable chapter is a cover (no cap of 8): For you first, then book order from the chapter after it, wrapping.

---

## BUILD-1101 B7: fields the UI needs (packet S3, 1 Nov 2026)

Added only; nothing above is renamed. Production and the preview return the same shapes (the preview runs the same service).

### POST /api/learn/runs (and GET /api/learn/runs/:id)
```
+ chapter: { key, title, ref, partTitle, number }   // ref 'Ch 2'|null, partTitle 'Part 1, Partnership Accounts'|null, number 2|null
body + source?: 'explore_cover'                      // a start from an Explore cover; anything else is dropped
     + forYou?: bool, position?: 0-500               // kept (with source) in the run's start_state
404 { error: 'CHAPTER_NOT_FOUND' }                   // a chapter that is not there; api.js: kind 'chapter_not_found', isChapterMissing(error)
```

### POST /api/learn/runs/:id/answer
```
+ choice: 'A'..'D'          // the key the student sent (upper case); a replay echoes the first answer's
  reinsert.moved: true      // the card already in the list moved closer; never a copy (a copy has no `moved`)
```

### GET /api/learn/runs/:id/end
```
+ feed.done: { reached, of, minutes }      // reached: the place of the last item the student acted on (answer or Keep), of: the
                                           // feed's items, minutes: first event to last, rounded, at least 1 (0 reached: minutes 1)
+ reviseCards: [{ id, kind, front, mustKnow }]   // the cards this run rated Got it or Easy, in run order, at most 4
+ lead / options[]: + kind: 'next'|'here'|'fix'|'revise'|'recap'|'mock'|'explore',
                    + title   // the heading that names it: "Next: Goodwill", "Another 5 minutes here", "Fix 2 open mistakes"
                    + minutes // the length the key says ("Start 10 minutes"); null when it is not a timed run (mock, explore)
                    // `label` (the older whole line) stays. The Free "See Pro" lead has no kind.
```

### POST /api/learn/runs/preview
```
+ shrink.addNext.ref: 'Ch 3'|null      // and added.ref
+ piles[].held: 'free' | null          // 'free': Free's session is used today, so Questions and Mistakes wait until tomorrow
+ resume: null | { runId, done, of, minutesLeft, kind }    // the chapter's unfinished mix or cards run (24 hours)
+ firstVisit: bool                     // the student has not studied this chapter
```

### GET /api/learn/covers?subject=
```
top level  + history: bool             // any chapter studied in the subject
each cover + name                      // the syllabus name ("Admission of Partner"), for filters and the Free-limit action
           + refLine                   // "Part 1, Ch 2" | "Microeconomics, Ch 2" | "Verbal Ability" (the unit when the chapter has no number) | null
           + resume: null | { runId, done, of, minutesLeft }   // today's unfinished feed of this chapter with something done
           hook: null | { id, front, kind, mustKnow }
                 // = counts[10].hook (F4 below): the first card of the 10-minute feed a start would serve (what Play opens with);
                 // on a cover with an unfinished feed, the next card that feed has left; null when the feed has no card
           studentLine: the stop ("You stopped at 6 of 16"), else "2 old mistakes to fix", else the chapter's state label, else
                 "New to you"  (never a due count)
           reason: for the For you cover; the book-order reason now reads 'First in the syllabus'
                 ('Chapter 1 of your book' is gone); a chapter whose feed was finished today is not For you while another qualifies
                 ("Next after <that chapter>" when book order would have picked it)
```

### GET /api/learn/cards
```
?subject=|?chapter=  &filter=due     // the open cards that are due today (the rule of shelves.due); counts.due on every read
```

### GET /api/learn/subject (suggestions)
```
Suggestion.kind + 'feed'   // a student with no history: the third suggestion is the first chapter as a feed:
  { kind: 'feed', title: 'Chapter 1 as a feed', headline: 'As a feed', chapterTitle, chapterKey,
    evidence: 'One card or question at a time, 10 minutes.',
    action: { label: 'Open the feed', href: '/explore/run?chapter=<key>&min=10', go: 'feed' } }   // links.resolve() maps it in the preview
```
Suggestion also carries `headline` and `chapterTitle` (its two parts, for a card that sets the chapter on its own line) and `chapterKey`.

---

## Learn v2 fix round, packet F4: the server tells the truth (1 Nov 2026)

Added or tightened only; nothing above is renamed. Production and the preview service answer the same shapes.

### GET /api/learn/covers?subject=
```
counts[m] (m = 5, 10, 20): { cards, questions, minutes, capped?, shrink?, hook }
  + hook: null | { id, front, kind, mustKnow }
        // the first CARD item of the feed a start at length m serves right after this read; null when that feed has no card
        // (the cover then says its questions; never a card the feed will not show). On a chapter with an unfinished feed
        // today, any start resumes it, so every length's hook is that feed's next card (null when only questions are left).
        // The older `{ front: null, locked: true }` shape is no longer produced for a feed card (a feed serves open cards only).
  + shrink?: { reason: 'pool' | 'cap' | 'mistakes' }
        // present only when that length was cut: 'pool' the chapter has no more, 'cap' the 40 new-card cap (or the overdue
        // cap), 'mistakes' only open mistakes fit. Absent: the run is as long as asked. Free at 20 is judged on the 10-minute run
  capped?: true   // Free only: present only when the 10-minute clamp actually cut the run (the same feed at the asked length
                  // would have held more items). Never on 5 or 10, never when 20 and 10 compose the same
each cover  hook: counts[10].hook      // the top-level hook is always the 10-minute length's
```
The cover's older `hook` rule ("the chapter's first Must-know card when the feed has no card") is gone: no card in the feed, no hook.

### GET /api/learn/runs/:id/end
```
+ done: { reached, of, minutes }    // EVERY run kind (mix, cards, recap, feed, level); feed.done is the same object
      // reached: the place of the last item the student acted on (0 = none), of: the run's items,
      // minutes: first event to last, rounded, at least 1.  "You stopped at 8 of 21." / "All 21 done in 9 min."
```

### POST /api/learn/runs (a Free feed)
```
A Free student's feed whose chapter has no fresh open card (the open taste cards are all in Revise, due or not) holds those
open cards again as looks: item.look: true, stage 'later'. A look schedules nothing and writes no review, rating or allowance
(rate answers { look: true, saved: false }; Keep on a card already in Revise writes nothing). Never more than the chapter's
open cards. Pro is unchanged: a feed never serves a due card. A Free feed with at least one fresh open card is unchanged.
```

### Every route
```
Writes: body cap 16,000 characters (was 8,000): "Study these 100" no longer answers 413.
```

---

## Learn v2 round 2, packet P3 (1 Nov 2026)

Added only; nothing above is renamed.

### POST /api/learn/runs/preview
```
+ firstUp: [{ id, front, kind, mustKnow }]   // the chapter page's "First up" row (R2 ruling 9): the first 3 Key cards this run serves
                                             // (the composer is deterministic), only cards the student may open; [] when none
```

### GET /api/bookmarks?count=1
```
{ count }    // Explore's "Saved 2" (R2 ruling 10): one head count, no rows, no question reads. Without ?count=1 the route is unchanged.
```
