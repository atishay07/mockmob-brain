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
