# A2. The Explore page and its chapter covers: audit and proposal (1 Nov 2026)

Scope: the Explore page (`src/components/feed/DiscoveryFeed.jsx`, `src/app/(app)/explore/explore.css`) and its row of chapter
covers (`src/components/learn2/feed/ExploreCovers.jsx`, `covers.css`, `GET /api/learn/covers`, which is `covers()` in
`src/lib/server/learn.js:1095`, answered in the preview through `src/lib/server/learnPreview.js:195`).

Owner items this answers: **LK21** first (every Accountancy cover shows the same object), then **LK20** and **LK22** (blank
space, refinement), **LK23** (build it completely, test everything, make it more useful), within LK11, LK12, LK13, LK15, LK18.

What I looked at:
- Screenshots in `tmp/learn-1101/audit/`: `01-explore-covers-{1440-night,1440-day,1366-night,390-night,390-day,360-night}`,
  `02-explore-list-{1440,390}-night`, `03-explore-free-{1440,390}-night`, `04-explore-new-{1440,390}-night`,
  `05-explore-full-{1440,390}-night` (cropped to read), and for continuity `11-feed-card-front-{1440,390}-night`,
  `19-feed-free-end-390-night`, `20-feed-free-second-1440-night`, `30-home-top-390-night`, `40-chapter-10min-1440-night`.
- Code: the files above, plus `chapterInfo()` (learn.js:304), `data/learn/feed.js`, `src/components/learn2/links.js`,
  the one-volt mechanism in `src/app/(app)/AppLayoutClient.jsx:211-241`, `keycards.css`, `feed.css`, the arena tokens
  (`arena.css:16-88`), the shared `src/components/ui/controls/SegmentedControl.jsx`.
- Real data: I ran the production covers handler in-process over the preview students (`keycardsPreview.previewAnswer`,
  no server, no browser) for Accountancy, Business Studies, Economics and English; Pro and Free; `commerce` and `new`.
  Section 3 is that output, not a guess.
- Rules: `OWNER-FEEDBACK-2026-10-31-LEARN.md` (all of it), `AI OS/wiki/concepts/ui-ux-standards.md`, the research brain
  (`AGENT_RULES.md`, `EVIDENCE_INDEX.csv`, `papers/uxpeak-zr37ibqXl1U.md`, `papers/ai-slop-independent.md`), `DESIGN.md`,
  `PRODUCT.md`, `FEED-2.md`, `BUILD-1101.md` (1.2, 1.3, 1.6, 1.8 R12, 1.9, Part 3), `CRITIQUE-1.md` R9.

---

## 1. What works and must be kept

The owner: "I really love the things you have built and the direction that you are taking." So this is a refinement of
the same idea, not a new layout.

1. **A row of chapter covers above Explore's questions,** one cover per chapter, snapping one per swipe on a phone, with
   the row running to the screen's edges (`covers.css:18-22`). This is the "way in" of FEED-2 section 6 and stays.
2. **One length control for every cover** (5, 10 or 20 minutes) and covers whose numbers come from the composer's own dry
   run at each length (`learn.js:1123-1127`). Switching the length never waits and never moves the layout. Keep this
   contract exactly.
3. **The big chapter title in Bricolage** on each cover, and a single key per cover that names the action. The key's
   accessible name is already good: "Play Accounting for Partnership: Basic Concepts, 10 minutes" (`ExploreCovers.jsx:60`).
4. **The suggested chapter first** (the server's R12 order: today's unfinished feed, then old mistakes, then the chapter
   after the latest activity, then book order), followed by book order, wrapping. Keep the order; show its reason (4.6).
5. **Free's counts are the real Free composition** (5 open cards a chapter), so a cover never promises more than Free
   plays. Keep it.
6. **No layout shift:** the row's height is held from the first paint (CLS 0 at desktop, 0.003 on phones in the capture
   index). Keep a fixed cover height per breakpoint.
7. **The server contract of BUILD-1101 1.9 already carries most of what a distinct cover needs** (hook, ref, part, reason,
   student line, state). The fix is mostly in the client. Fields are only added, never renamed.
8. **The question list below stays as it is** (FEED-2 section 6), with Save and Show answer.
9. **The lamp-lit subject object stays, once per page,** where it means "this page is in Accountancy" (4.10). The Learn
   home's subject row (`30-home-top-390-night.png`) is the model: there the object names a subject, which is meaningful.

---

## 2. Findings, by severity

Severity: **blocker** = the owner will not accept the screen with it; **high** = breaks a product rule or a promise, or
blocks a task; **medium** = clear defect in clarity, states or layout; **low** = polish or a follow-up.

### Blocker

**F1. Every cover shows the same subject object, and so does the list head (LK21).**
- See: at 1440 the three visible covers (Accounting for Partnership: Basic Concepts, Profit and Loss Appropriation Account,
  Change in Profit Sharing Ratio) each carry the same 140 px calculator-and-ledger, and the "Accountancy" list head shows it
  a fourth time at 96 px (`01-explore-covers-1440-night.png`, `-1440-day`, `-1366-night`, `-390-night`, `-360-night`;
  `05-explore-full-1440-night.png`).
- Code: `ExploreCovers.jsx:56` draws `<SubjectObject id={subject} size={140}>` on every cover; `DiscoveryFeed.jsx:124`
  draws it again at 96 px.
- Why it fails: the object tells the student nothing about the chapter. It takes 140 of 360 px of every cover (39 percent)
  and is part of the "too much blank space" (LK22). The research brain: a real product preview beats an unrelated image when
  the user must judge what is offered (T007, T009; `papers/uxpeak-zr37ibqXl1U.md` line 48). Slop test #12: the screen is
  better without the repeated object.

### High

**F2. Three or four volt keys in one viewport.**
- At 1440 there are three volt Play keys side by side, and the sidebar's "Start a session" stays volt beside them: four
  lime fills (`01-explore-covers-1440-night.png`). On the phone the first cover's volt Play, the second cover's volt Play
  peeking at the right edge, and the dock's volt Start make three (`01-explore-covers-390-night.png`).
- Code: the Play links carry no `data-page-primary` (`ExploreCovers.jsx:60`), so the shell's one-volt mechanism
  (`AppLayoutClient.jsx:211-241`, W-075) never quiets the sidebar or the dock here. Compare the chapter page, where the
  sidebar Start is outlined (`40-chapter-10min-1440-night.png`), and Learn home on the phone, where the dock Start steps back
  (`30-home-top-390-night.png`).
- Rule: one volt action per viewport (ui-ux-standards 3 and 5; AGENT_RULES 7; CRITIQUE-1 R9 asked for this already).

**F3. The row cannot be moved on a computer, and only by a gesture on a phone.**
- At 1440 the row shows exactly three covers (3 x 280 + 2 x 12 = 864 px of an 866 px column): no peek, no arrows, no count,
  and the scrollbar is hidden (`covers.css:18-19`, `scrollbar-width: none`). The data has **14** Accountancy covers, so 11
  chapters are invisible with no hint that they exist. At 1366 the third cover is simply cut at the column edge (209 of
  280 px), which looks like a bug rather than a row.
- A vertical mouse wheel scrolls the page, not the row (correct), so a mouse user with no trackpad has only Tab, which walks
  through up to 14 links one by one.
- On the phone, a swipe is the only way to the next cover: a feature behind a gesture alone (the owner's audience rule).
- Same root as LK20 for the feed ("on PC there is no way to go on to the next thing").

**F4. The data that would make each cover distinct is already sent, and thrown away.**
- `covers()` returns per cover: `ref` ('Ch 2'), `number`, `partTitle`, `unitTitle`, `reason`, `forYou`, `hook` (the
  chapter's opening card: `front`, `kind`, `mustKnow`), `state`, `studentLine`, `counts`, `kept`, `due`, `mistakes`
  (`learn.js:1132-1138`, BUILD-1101 1.9).
- The client reads only `key`, `title`, `forYou` and `counts` (`ExploreCovers.jsx:52-62`).

**F5. On Free, once the day's session is used, every cover still invites a feed that will be refused.**
- When `data.free` is set, the client prints the line above the row (`ExploreCovers.jsx:49`) but leaves every volt Play key
  as it was (`:60`). A tap opens the "One feed a day on Free" screen (`20-feed-free-second-1440-night.png`), a dead end
  reached through the page's own primary action.
- Rule: LK15, limit lines only at the real limit and never a dead end; ui-ux-standards 6 (a disabled or limited state
  explains itself); T005 (no threat or wall); T003 (value before the gate).

**F6. "Questions on this chapter in Explore" does not open that chapter's questions.**
- The Free end screen and the 402 options link to `/explore?subject=accountancy&chapter=<name>` (`learn.js:422`, `:1053`),
  but `links.explore()` drops the query (`links.js:49`, `:64`) and `DiscoveryFeed.jsx` never reads URL parameters (it
  defaults to Accountancy, `:41`). The student lands on all chapters. A promise in copy that the page does not keep.

### Medium

**F7. The page's parts compete and sit apart from what they control.**
- Order today (`05-explore-full-1440-night.png`, `DiscoveryFeed.jsx:113-139`): the H1 "One question. One useful step." and
  lede, then the three filters (Subject, Chapter, Difficulty), then the covers, then a list head with the object and
  "Accountancy", then the questions. Chapter and Difficulty filter only the list, yet the covers sit between them and the
  list; the Subject filter controls both but reads as a list filter.
- The right column's "Answer first. Then ask why." is a 30 px display headline (`explore.css:42`) beside the covers, a second
  hero competing with the H1 and the cover titles; above it sits the kicker "Tonight's rule" (`DiscoveryFeed.jsx:135`), which
  the standards ban (no kickers above headings) and which is wrong at 10 am.
- The subject is named three times on one screen (filter, list head, object).

**F8. The cover line reads as random, and on Free the length control mostly does nothing.**
- Pro, 10 minutes: "16 Key cards and 5 questions", "32 Key cards and 1 question", "8 Key cards and 7 questions", "36 Key
  cards", and two covers that silently drop to "4 minutes, 16 Key cards" and "5 minutes, 18 Key cards" with no reason.
- Free, 10 minutes: 10 of 14 Accountancy covers read "1 minute, 5 Key cards" whatever length is picked; the control changes
  nothing there. The covers with questions read "9 minutes, 5 Key cards and 7 questions", which inverts the feed's own shape
  (about two cards per question, `feed.js:95-110` flags a ratio under 1).
- Cause, honestly stated: mostly the preview fixture. It has questions for only four Accountancy chapters (Partnership
  Fundamentals 10, Admission of Partner 10, Change in Profit Sharing Ratio 7, Profit and Loss Appropriation 1); production
  links 1,072 Accountancy questions (R4-explore: P&L 165, Change in PSR 136, Admission 159). But the cover must read well with
  any mix, including zero questions and a shortened length, and the Free card-to-question ratio is a real composer question
  for the logic owner (S1).

**F9. "For you" gives no reason, and claims personal choice where there is none.**
- The server sends the reason ("3 old mistakes to fix", "Pick up where you stopped", "Next after Goodwill: Nature and
  Valuation", "Chapter 1 of your book", `learn.js:1103-1118`); the cover shows only "For you".
- A first-time student (`student=new`) sees "For you" on chapter 1 (`04-explore-new-1440-night.png`), which is plain book
  order. ui-ux-standards 13: say "personalised" only where the logic truly is; AGENT_RULES MockMob overlay: a next move
  names its evidence, and says so when the history is too thin.

**F10. Free at 20 minutes: the cap is silent.**
- Free composes 20 as 10 (`counts[20].capped` is set, `learn.js:1126`), so the covers read "9 minutes" under a selected
  "20 min" and nothing says why. BUILD-1101 1.6 requires one line under the control: "Free sessions are up to 10 minutes.
  Pro has any length." The client ignores `capped`.

**F11. Silent, placeholder and mismatched states.**
- Error and empty return `null` (`ExploreCovers.jsx:40`): the section just vanishes, with no way to retry.
- While subjects load, the list head reads "your subject" in lower case (`DiscoveryFeed.jsx:106`, `:124`): placeholder copy
  on screen.
- The skeleton draws a 120 px circle where the object was (`covers.css:32`), so it will not match a cover without the
  object.

**F12. On the phone the feeds start below the first screen, and the head row is cramped.**
- At 390x844 the covers start at about y 560 css px after the place tabs, a two-line H1, a three-line lede, and three
  labelled filters (`05-explore-full-390-night.png` cropped); the first Play key is below the fold (capture index section 3,
  "Explore cover play key was below the first screen"). LK18 wants the feed to be a standout phone feature.
- At 360 the "Chapter feeds" title and the 5/10/20 control are 13 px apart (`01-explore-covers-360-night.png`).

**F13. One chapter, two names, on one screen.**
- The cover says "Accounting for Partnership: Basic Concepts"; the first question under it says "Partnership Fundamentals"
  (`01-explore-covers-1440-night.png`, `QuestionCard.jsx:94` prints the syllabus name), and the Chapter filter lists the
  syllabus names. CRITIQUE-1 R9 asked for the chapter title in Explore; still open.

**F14. The length control is a different control from the rest of the product, and forgets the choice.**
- Selected = a solid ink pill (white on Night, near-black on Day, `covers.css:13`): the brightest thing on the row after the
  volt keys. The chapter page uses a calm raised thumb (`40-chapter-10min-1440-night.png`) and the site has a shared
  `SegmentedControl` (radio group, roving focus, arrows, Home, End) used by "Time for practice". The covers' buttons are
  `aria-pressed` toggles without arrow-key behaviour, and the choice resets to 10 on every visit (`ExploreCovers.jsx:36`).

### Low

**F15. Long chapter names would be cut.** `.fxc-name` clamps at 3 lines (`covers.css:27`). At 22 px in a 244 px measure,
Economics' "Development Experiences of India: A Comparison with Neighbours" (61 characters) needs 4 lines and would end in an
ellipsis. Names are never truncated (ui-ux-standards 2).

**F16. The default subject ignores the student.** Explore opens on Accountancy for everyone (`DiscoveryFeed.jsx:41`), and
`pickSubject` serves covers for any subject with a deck (`learn.js:166-170`), so a student without Accountancy is shown
Accountancy covers. T001: defaults only from real context.

**F17. The student line describes things the feed will not do, and resume is invisible.**
- The server's `studentLine` leads with "3 due" (`learn.js:1130`), but a feed never serves a due card (BUILD-1101 1.2).
  On a feed cover, "3 due" suggests Play revises them.
- When the chapter has an unfinished feed today, Play resumes it (BUILD-1101 1.3), yet the key still reads as a new
  "Play" for the picked length.

**F18. Dead copy.** `ArenaHead eyebrow="Explore · untimed practice"` (`DiscoveryFeed.jsx:113`) carries a middle dot; ArenaHead
ignores the prop, but it is still copy in the source.

**F19. No way to know whether covers work.** Nothing records that a feed came from a cover, from the For you cover, or at
which position. Slop test #11 (one leading metric and one guardrail) cannot be answered.

---

## 3. The real data per chapter (inventory)

### 3.1 What exists per chapter on the server

From `chapterInfo()` (`learn.js:304-337`), all real, read once per request:
- **Identity:** `key`, `title` (the NCERT title, cleaned), `name` (the syllabus name the questions and filters use),
  `unit`, `section`, `ref` ('Ch 2'), `chapterNo`, `book` (mapped to `partTitle`: 'Part 1, Partnership Accounts',
  'Business Studies Part 1', 'Introductory Microeconomics', ...).
- **Content:** every card in book order with `front`, `kind`, `importance` (Must-know), `source` (book, chapter, page,
  section); the Free taste set (5 open cards); the servable questions (difficulty, linked cards); the first unread lesson.
- **The student:** card states (in Revise, due, kept = `added_from 'manual'`), open mistakes with their place and day
  ("You missed this in Mock 3 on 16 Oct"), the chapter state (`Getting there`, `Needs work`, `Holding`, `Too few
  answers`, `Not started`), `studied`, `lastActivityAt`, the answered tally, an unfinished run.
- **Counts:** cards, open, Must-know, open Must-know, due, in Revise, kept, linked questions.

### 3.2 What a cover receives today (BUILD-1101 1.9)

`{ key, title, ref, number, partTitle, unitTitle, reason|null, forYou, hook: { front, kind, mustKnow } | { locked } | null,
state: { key, label }, studentLine, counts: { 5|10|20: { cards, questions, minutes, capped? } }, kept, due, mistakes,
art: null }`, plus top-level `subject`, `lengths`, `free`.

### 3.3 Accountancy, the commerce preview student (Pro unless noted), in the order the row shows them

| # | Ref | Chapter | Hook (opening card front), characters | Student line now | 10 min, Pro | 10 min, Free |
|---|---|---|---|---|---|---|
| 1 | Part 1, Ch 1 | Accounting for Partnership: Basic Concepts (For you: "3 old mistakes to fix") | Define partnership. (19) | 3 due, 3 old mistakes | 10 min, 16 cards, 5 questions | 9 min, 5 cards, 7 questions |
| 2 | Part 1, Ch 1 | Profit and Loss Appropriation Account | What is the Profit and Loss Appropriation Account? (50) | 3 due | 10 min, 32 cards, 1 question | 2 min, 4 cards, 1 question |
| 3 | Part 1, Ch 2 | Change in Profit Sharing Ratio | What is the gaining ratio? (26) | Needs work | 10 min, 8 cards, 7 questions | 9 min, 5 cards, 7 questions |
| 4 | Part 1, Ch 2 | Goodwill: Nature and Valuation | What is goodwill? (17) | Holding | 10 min, 36 cards | 1 min, 5 cards |
| 5 | Part 1, Ch 2 | Admission of a Partner | What is reconstitution of a partnership firm? (45) | 2 old mistakes | 10 min, 16 cards, 5 questions | 9 min, 5 cards, 7 questions |
| 6 | Part 1, Ch 3 | Retirement and Death of a Partner | Sum due to a retiring/deceased partner includes: name items (i) to (v). (71) | Getting there | 10 min, 36 cards | 1 min, 5 cards |
| 7 | Part 1, Ch 4 | Dissolution of Partnership Firm | Define the dissolution of the firm (Section 39 of the Partnership Act 1932). (76) | New to you | 10 min, 36 cards | 1 min, 5 cards |
| 8 | Part 2, Ch 1 | Accounting for Share Capital | Define authorised capital. (26) | Too few answers | 10 min, 36 cards | 1 min, 5 cards |
| 9 | Part 2, Ch 2 | Issue and Redemption of Debentures | What is a debenture? (20) | New to you | 10 min, 36 cards | 1 min, 5 cards |
| 10 | Part 2, Ch 3 | Financial Statements of a Company | What are financial statements of a company? (43) | Needs work | 10 min, 36 cards | 1 min, 5 cards |
| 11 | Part 2, Ch 4 | Analysis of Financial Statements | What is 'Financial Statement Analysis'? (39) | New to you | 4 min, 16 cards (shrunk) | 1 min, 5 cards |
| 12 | Part 2, Ch 4 | Comparative and Common Size Statements | When is financial data comparative, and how is a deviation in accounting principles shown? (90) | Holding | 5 min, 18 cards (shrunk) | 1 min, 5 cards |
| 13 | Part 2, Ch 5 | Accounting Ratios | What is a ratio? (16) | 3 due | 10 min, 36 cards | 1 min, 5 cards |
| 14 | Part 2, Ch 6 | Cash Flow Statement | What is a Cash flow statement? (30) | Too few answers | 10 min, 36 cards | 1 min, 5 cards |

Computerised Accounting System has no cards and no questions and is correctly left out. Every hook is Must-know (12
definitions, 1 list, 1 fact), every hook is different, and the Admission hook is exactly the first card its feed shows
(`11-feed-card-front-1440-night.png`: "What is reconstitution of a partnership firm?").

For the new student (`student=new`, Free) the row and hooks are the same, every student line is "New to you", and the For
you reason is "Chapter 1 of your book".

### 3.4 The other Commerce subjects

- **Business Studies (11 covers):** refs Ch 1 to Ch 11 across Part 1 and Part 2, unique. Hooks 16 to 66 characters ("Define
  planning.", "What is directing in the context of management of an organisation?"); one carries a source note
  ("What is controlling? (NCERT, Meaning of Controlling)").
- **Economics (17 covers):** "Ch 2" appears in three different books (Introductory Microeconomics, Introductory
  Macroeconomics, Indian Economic Development); Ch 3 to Ch 6 appear twice each. Hooks 14 to 114 characters; the longest is
  "Which Article requires the government to present its estimated receipts and expenditures to Parliament every year?".
  Longest title: "Development Experiences of India: A Comparison with Neighbours" (61 characters).
- **English (2 covers):** no NCERT ref (the cards are written for MockMob), unit "Verbal Ability". Hooks "What does 'concise'
  mean?" and "Choose the correct word: The new rule will ____ every student. (affect / effect)".

### 3.5 What the inventory decides

- **A chapter number cannot be the cover's hero.** It repeats on neighbouring covers (Part 1 "Ch 2" three times in a row,
  "Ch 1" in both parts, Economics "Ch 2" in three books) and English has none. As the big display numeral it would make
  covers look the same, the opposite of LK21. It stays as small meta ("Part 1, Ch 2").
- **The opening card is unique per chapter, true, and is what Play opens.** It is the natural cover art.
- **"Due" is not a feed fact** (feeds never serve due cards), so it leaves the cover line.

---

## 4. Proposal

### 4.1 Decision: what a cover shows instead of the object

**The cover shows the first Key card its feed will open with,** set in display type on the lit card surface the Key cards
and the feed already use (owner W-013: "some blue light and texture on the cards"). The cover becomes a preview of the real
thing: tap Play and the same words open full screen. Every cover is distinct by content, not by decoration. No new artwork.

Alternatives considered:

| Option | What | Why not, or why |
|---|---|---|
| **A. The opening card (chosen)** | the feed's first card front as the cover's art, ref as small meta | Distinct on all 44 covers in the inventory (14 + 11 + 17 + 2); true; continuous with the feed (same words, same surface); value before Play (T003, T007, T009). |
| B. Display chapter numeral | a big "2" per cover | Repeats on neighbours, absent for English, decoration that looks like data (3.5). |
| C. The object, varied | different crops or angles of the same object | Still the same object (the owner's complaint). |
| D. Mix ticks | a strip of the feed's items, cards and questions | True only with the exact order from the server; adds texture, not choice. Possible later, not now. |
| E. Keep the object once | on the subject control in the page head | Kept (4.10): there it names the subject. |

Evidence: T007 and T009 (real preview over generic imagery; `uxpeak-zr37ibqXl1U.md` lines 13, 17, 48), T003 (value before
gate), S017 and S018 (slop is missing intent and repetition, not a colour), ui-ux-standards 3 ("one visual anchor that carries
real information"), AGENT_RULES 27.

### 4.2 The cover: anatomy and copy

```
+-----------------------------------+  one surface: radius 24, 1px line-strong, lit (cool light over the top 90 px, grain)
| Part 1, Ch 2                      |  MEDIA  ref line
|                                   |
|  What is reconstitution           |         hook: the feed's first card front, display 650,
|  of a partnership firm?           |         size by length, centred in the media below the ref line
|                                   |
+-----------------------------------+  1px line, full bleed
| Admission of a Partner            |  BODY   title, display 700
| For you: 2 old mistakes to fix    |         student line ("For you:" in accent text, 700)
|                                   |         (flexible space)
| 16 Key cards, 5 questions         |         mix line, tabular
| [ > Play 10 minutes             ] |         the key: volt on the lead cover only, line style on the rest
+-----------------------------------+
```

One surface, not a card inside a card (ui-ux-standards 3: never nest cards): the media is the top of the cover, full bleed,
separated from the body by a hairline, exactly where the object sat. The whole cover is one link (4.5).

**The parts, with exact copy:**

| Part | Rule | Copy |
|---|---|---|
| Ref line | `refLine` from the server (4.11); else derived: partTitle "Part N, ..." or "... Part N" gives "Part N, Ch X"; a book title drops "Introductory " ("Microeconomics, Ch 2"); no ref gives `unitTitle` ("Verbal Ability"); nothing gives no line. One line, ellipsis allowed (low-value meta). | "Part 1, Ch 2", "Microeconomics, Ch 2", "Indian Economic Development, Ch 5", "Verbal Ability" |
| Hook | `hook.front` exactly as stored. No kind label, no Must-know tag on covers (LK13). Locked or null hook: the questions-only fallback below. | "What is goodwill?" |
| Hook fallback, no cards | The mix in display type plus one line. | "8 questions" + "No Key cards here yet." |
| Title | `title`, never truncated. | "Admission of a Partner" |
| Student line, lead cover | Prefix plus the server's `reason`. Prefix "For you:" when the reason comes from the student's own history; "Start here:" when it is book order for a student with no history. Up to 2 lines. | "For you: 3 old mistakes to fix", "For you: pick up where you stopped", "For you: next after Goodwill: Nature and Valuation", "Start here: first in the syllabus" |
| Student line, other covers | `studentLine` without due counts (4.11): resume, else mistakes, else the state label, else "New to you". When every cover would say "New to you" (no history in the subject), the line is left out on the non-lead covers. 1 line. | "You stopped at 6 of 16", "2 old mistakes to fix", "Getting there", "New to you" |
| Mix line | Cards and questions of the picked length (`counts[m]`; questions include old mistakes). Either part dropped at 0. When `counts[m].minutes < m` and not capped, add ", all it has today". | "16 Key cards, 5 questions", "36 Key cards", "8 questions", "16 Key cards, all it has today" |
| Key | "Play {n} minutes", n = `counts[m].minutes` ("1 minute"). Resume: "Pick up, {left} minutes". Free at the day's limit: "Questions on this chapter". A 16 px play glyph inside the key, before the label; no trailing arrow. | "Play 10 minutes", "Pick up, 4 minutes" |

No middle dots, sentence case, no "mastered", no percentages, no "marks to recover".

### 4.3 Sizes per breakpoint

Width is fluid from the row's own width (CSS container queries on `.fxc`, `container-type: inline-size`), so there is always
a visible peek of the next cover and never a cut-off cover.

```css
.fxc { container: fxc / inline-size; }
.fxc-row { --g: 16px; --peek: 40px; display: grid; grid-auto-flow: column; grid-auto-columns: var(--w); gap: var(--g); }
@container fxc (min-width: 1040px)                         { .fxc-row { --w: calc((100cqw - 3 * var(--g) - var(--peek)) / 4); } }
@container fxc (min-width: 740px) and (max-width: 1039.98px) { .fxc-row { --w: calc((100cqw - 2 * var(--g) - var(--peek)) / 3); } }
@container fxc (min-width: 560px) and (max-width: 739.98px)  { .fxc-row { --w: calc((100cqw - var(--g) - var(--peek)) / 2); } }
@container fxc (max-width: 559.98px)                       { .fxc-row { --g: 12px; --w: min(320px, calc(100cqw - 56px)); } }
```

| | 1440x900 | 1366x768 | 1024x768 | 430 wide | 390x844 | 360x780 |
|---|---|---|---|---|---|---|
| Row width (Option A, full width, 4.10) | 1168 | 1094 | 752 | 398 | 358 | 328 |
| Covers in view | 4 and a 40 px peek | 4 and 40 | 3 and 40 | 1 and 82 | 1 and 60 | 1 and 60 |
| Cover width | 270 | 251.5 | 226.7 | 320 | 302 | 272 |
| Gap | 16 | 16 | 16 | 12 | 12 | 12 |
| Cover height | 356 | 356 | 368 | 332 | 332 | 332 |
| Media height (fixed) | 140 | 140 | 140 | 128 | 128 | 128 |
| Padding, inline | 18 | 18 | 16 | 16 | 16 | 16 |
| Media padding-top / ref line / gap | 16 / 16 / 10 | same | same | 14 / 16 / 8 | same | same |
| Hook size by length (up to 24 / 48 / 80 / over 80 characters), line-height | 26/1.1, 22/1.15, 19/1.2, 16/1.25 | same | 24, 20, 17.5, 15 | 24, 21, 18, 15.5 | same | same |
| Title (over 48 characters) | 18/1.18 (16/1.2) | same | 17/1.18 (15.5/1.2) | 17/1.18 (15.5/1.2) | same | same |
| Body padding top / bottom | 14 / 16 | same | same | 12 / 14 | same | same |
| Student line / mix line | 13.5/1.35 600 / 13/1.35 500 | same | same | 13/1.35 / 12.5/1.35 | same | same |
| Key height, radius, label | 46, 14, 650 15 px | same | same | 46, 14, 650 15 px | same | same |
| Paging | arrows in the head | arrows | arrows | pager under the row | pager | pager |

With Option B (row stays inside the main column) the same rules give 3 covers of 264.7 px at 1440 and 3 of 240 px at 1366.

Type details: hook `font: 650 <size>/<lh> var(--font-display); letter-spacing: -0.02em` (-0.01em at 16 px and under);
`text-wrap: balance; overflow-wrap: anywhere`; centred vertically in the media below the ref line
(`align-content: center`); 4 lines at most, with `-webkit-line-clamp: 4` only as a last resort (the full front is in the
link's description). Title `font: 700 ... var(--font-display); letter-spacing: -0.015em; text-wrap: balance`, no clamp.
Mix line `font-variant-numeric: tabular-nums`. Body grid rows: `auto auto 1fr auto auto`, gaps 6 (title to line) and 8
(mix to key), so every key sits on the same baseline across the row.

Estimated fit (average glyph widths of Bricolage at these weights, not yet rendered; the builder confirms with screenshots):
every Accountancy hook fits its tier in 3 lines at 302 px; the 114-character Economics hook needs 4 lines at 16 px in a
234 px measure. Every title fits in 3 lines at 18 px at 1440 and 1366, and the 61-character Economics title may need 4 lines
at 15.5 px at 1024 (hence the 368 px cover there).

### 4.4 Night and Day

Arena tokens only; both themes come from the tokens.

| Element | Night | Day |
|---|---|---|
| Cover surface | `--kc-surface`: `radial-gradient(120% 90px at 30% 0%, rgb(118 168 255 / .13), transparent 100%)`, grain, `--a-raised` #131a16 | same recipe, `rgb(70 120 220 / .09)`, light grain, #ffffff |
| Cover border, shadow | 1px `--a-line-strong` #384736, `--a-shadow-1` | #bcc5b0, light `--a-shadow-1` |
| Media and body divider | 1px `--a-line` #253026 | #dce1d4 |
| Ref line, mix line | `--a-ink-3` #93a08f | #56624f |
| Hook, title | `--a-ink` #f2f4ec | #172016 |
| Student line | `--a-ink-2` #bcc5b9 | #3d4a39 |
| "For you:" / "Start here:" | `--a-accent-text` #d2f000 | #4f6400 |
| Lead key | `.kc-btn--volt` (#d2f000, ink #10140e, edge #8ba000) | same |
| Other keys | `.kc-btn--line` (`--a-raised`, 1px `--a-line-strong`, ink) | same tokens |
| Focus ring | 2px `--a-focus`, offset 3px, follows radius 24 | #4f6400 |

The lit surface is the project's accepted Key cards material (W-013; precedence 2 of ui-ux-standards), not a new gradient.
`.fxc` is not inside `.kc`, so its tokens must exist there: either widen `keycards.css:14-21` to `.kc, .kc-line, .fxc`
(preferred, one selector) or copy the three variables into `covers.css` for `.fxc` and `html[data-theme='light'] .fxc`.
Contrast to check when built: `--a-ink-3` on the lit top of the media in both themes (it is 6.6:1 on plain #131a16 and 6.4:1
on #ffffff).

### 4.5 The row: paging on a computer and a phone, keyboard, semantics

- **Desktop and tablet (row width 560 px and up): two arrow buttons in the section head,** right of the length control,
  8 px apart. 44x44 circles, 1px `--a-line-strong`, `--a-raised`, a 18 px ChevronLeft or ChevronRight in `--a-ink-2`;
  hover (inside `@media (hover: hover)`): `--a-hover` fill, `--a-line-hover` border, ink icon; focus-visible: 2px
  `--a-focus`, offset 2px. Names: "Previous chapters", "Next chapters". At either end the arrow is `disabled`, opacity 0.38;
  if focus was on it, focus moves to the other arrow.
- **A click pages by the covers in view:** `scrollBy({ left: ±perView * (w + g), behavior })` with `behavior: 'smooth'`, or
  `'auto'` under reduced motion. With `scroll-snap-type: x mandatory` and `scroll-snap-align: start` it lands on a cover's
  start. The vertical wheel keeps scrolling the page; a trackpad or Shift and wheel scroll the row natively.
- **The count:** right of the title, `--a-ink-3` 13 px tabular: "14 chapters".
- **Phone (row under 560 px): a pager under the row,** centred, 10 px below it: `[<] 1 of 14 [>]`. Buttons 44x44 as above;
  the middle text 13.5 px 600 `--a-ink-2`, tabular, at least 64 px wide. It updates from the snapped cover (an
  `IntersectionObserver` on covers with threshold 0.6 inside the row). Names: "Previous chapter", "Next chapter". This is
  what makes the row usable without a swipe (the owner's rule: never a feature behind a gesture alone).
- **Keyboard:** one tab stop for the whole row (roving `tabindex`: the first cover in view, or the last focused). Left and
  Right move focus to the previous or next cover and bring it into view (`scrollIntoView({ inline: 'nearest', block:
  'nearest' })`); Home and End go to the first and last; Enter opens the feed. Tab order in the section: length control (one
  stop, radio group), Previous, Next, the row, then the pager on phones.
- **Semantics:** `<section aria-labelledby>` with the `h2`; `<ul aria-label="Accountancy chapter feeds">`, one `<li>` per
  cover; each cover is one `<a>` with `aria-labelledby="<title id> <key id>"` (name: "Admission of a Partner, Play 10
  minutes") and `aria-describedby="<line id> <mix id> <hook id>"`. The key inside is a styled `span`, not a second control.
- **Scrolling details kept:** `overscroll-behavior-x: contain`; on phones the row bleeds to the edges
  (`margin-inline: -16px; padding-inline: 16px; scroll-padding-inline: 16px`), as today.

### 4.6 For you

- **The pick stays the server's R12:** today's unfinished feed, then the chapter with the most old mistakes, then the chapter
  after the latest Learn activity that still has new cards, then the first chapter with cards. Two refinements for S2a:
  (a) skip a chapter whose feed was finished today when another one qualifies (a lead never repeats what was just done; same
  spirit as R9); (b) the book-order reason reads "First in the syllabus", not "Chapter 1 of your book" (for Economics the
  first syllabus chapter is "Ch 2" of a book, so the old copy is wrong there).
- **The lead cover is the only volt key on the row,** marked `data-page-primary` so the sidebar Start is outlined on desktop
  and the dock Start steps back while the key is on screen (W-075). The volt never moves to whichever cover is snapped: a key
  that changes with scroll is the bug the owner saw on Practice (F12 of 17 Oct).
- **The reason is on the cover** ("For you: 3 old mistakes to fix"), so the suggestion carries its evidence (AGENT_RULES
  MockMob overlay). A student with no history sees "Start here: first in the syllabus", never "For you".
- **The default stays editable:** any cover can be played, at any length (T001).

### 4.7 The 5, 10 and 20 control

- Use the site's `SegmentedControl` (`src/components/ui/controls/SegmentedControl.jsx`), `size="sm"`, `label="Feed
  length"`, options "5 min", "10 min", "20 min". It is a WAI-ARIA radio group with a roving tab stop, arrows, Home and End,
  and the sliding lens already used by "Time for practice". It replaces the ink-filled pill (F14). Ask U4 to use the same
  control on the chapter page, so Learn has one length control.
- Default 10. Remember the last choice per viewer in `localStorage` key `mm:explore:feedMinutes` (read and write inside
  try/catch; a failed read means 10).
- Free with 20 picked: the section's sub line becomes "Free sessions are up to 10 minutes. Pro has any length." (BUILD-1101
  1.6; it shows only then). The keys read what is really composed ("Play 10 minutes" or less). The control is never hidden
  or disabled on Free.
- Changing the length changes only numbers: each cover's mix line and key label (4.9). Nothing else moves.

### 4.8 Every state

| State | Section head | Covers | Keys |
|---|---|---|---|
| Loading | Title, control (usable), arrows disabled; screen-reader status "Loading chapter feeds" | Skeleton covers at the real size, as many as fit plus the peek: media with a 72x12 ref bar and two hook bars (85 and 60 percent, 20 px tall, 10 px apart, centred); hairline; title bars 80 and 55 percent x 16 px; line bar 45 percent x 12; mix bar 38 percent x 12; a 46 px key block, radius 14. Border `--a-line`, no shadow, existing `.skeleton` shimmer (static under reduced motion). | none |
| Pro, ready | Title, sub line "Key cards and questions, one at a time." (desktop only), "14 chapters", control, arrows | as 4.2 | lead volt, others line |
| Free, under the day's limit | same; with 20 picked, the sub line is the capped line (4.7) | Free counts | same |
| Free, day's session used (`data.free`) | Sub line: "Your free Learn session for today is done. Explore questions stay free." and a "See Pro" text key (accent underline, 44 px target), no modal | hooks, titles and student lines stay (value before the gate, T003); the mix line is left out | "Questions on this chapter" (lead volt, others line): sets the Chapter filter to this chapter, scrolls to the Questions section and focuses its heading. No call to `POST /api/learn/runs`. |
| First-time student | as Pro or Free | lead line "Start here: first in the syllabus"; other covers have no student line | lead volt |
| Unfinished feed today | | that cover: line "You stopped at 6 of 16", mix "About 4 minutes left"; the length does not change it | "Pick up, 4 minutes" |
| Shorter than the length | | mix "16 Key cards, all it has today" | "Play 4 minutes" |
| Chapter with questions only | | media: "8 questions" (display 650, 22 px) and "No Key cards here yet." (13 px `--a-ink-3`) | "Play n minutes" |
| Error | Title, control | One line in place of the row: "Chapter feeds did not load." and a "Try again" text key (44 px) that refetches | none |
| Empty (no playable chapter) | Title only | One line: "No chapter feeds for {Subject} yet. The questions below still work." | none |
| Subject changed | unchanged | skeleton, row scrolled back to 0, pager "1 of n" | none |

Nothing returns `null` any more, except the whole section while Learn v2 is off (the existing `NEXT_PUBLIC_LEARN2` gate).

### 4.9 Motion

Every movement answers an action; nothing loops; the page head's existing rise is the one load moment, so covers get no
entrance stagger. Easing `var(--ease-out, cubic-bezier(0.23, 1, 0.32, 1))`; transform and opacity only; never `all`.

| What | Trigger | Change | Duration | Reduced motion |
|---|---|---|---|---|
| Cover hover | pointer enters, `@media (hover: hover)` only | translateY(-2px); border to `--a-line-hover`; shadow to `--a-shadow-2` | 180 ms | border colour only |
| Cover press | `:active` | scale(0.985); the inner key's edge collapses as `.kc-btn--volt:active` does | 100 ms in, 160 ms out | edge collapse only |
| Length change | radio choice | the control's lens slides (its own 240 ms); in each cover only the text that changed fades in from translateY(3px), opacity 0 | 180 ms | instant |
| Paging | arrow or pager | smooth `scrollBy` (the browser's own, about 300 to 450 ms) | browser | `behavior: 'auto'` |
| Data arrives | skeleton to covers | the row's opacity 0 to 1 | 160 ms | instant |
| Subject change | listbox | the one subject object keeps its existing `mk-pop`; the row goes to the skeleton | existing | static |
| An arrow reaches the end | scroll position | opacity to 0.38 | 150 ms | instant |

Not now: a shared-element move of the hook into the feed's first card. Navigations into focus routes are deliberately not
transitions (`src/lib/motion/placeTransition.js`, FOCUS_PATHS: the owner saw the shell flash when opening a feed from a
cover). Try it later only with React's `ViewTransition` on the hook alone and no shell in the snapshot.

### 4.10 How the covers sit on the Explore page

**Option A (recommended): put things next to what they control, and give the covers the full width.**

```
Desktop 1440                                                            Phone 390
---------------------------------------------------------------------   ------------------------------
One question. One useful step.                  [obj 64] Subject [v]    One question. One useful step.
Untimed practice, separate from your timed mock score.                  Untimed practice, separate from
Play a short chapter feed, or take one question at a time.              your timed mock score.
                                                                        [obj 40] Subject [Accountancy v]
Chapter feeds        14 chapters        [5 min|10 min|20 min]  (<) (>)  Chapter feeds    [5|10|20 min]
Key cards and questions, one at a time.                                 [ lead cover ][ next
[ lead ][ cover ][ cover ][ cover ][ peek                                     (<)  1 of 14  (>)
---------------------------------------------------------------------   Questions
Questions   [Chapter v] [Difficulty v] Clear filters  |  Answer first.  [Chapter v] [Difficulty v]
[question card]                                       |  Then ask why.  [question card] ...
[question card]                                       |  Open saved ...  (the right column follows the list)
```

1. **Page head** (`ArenaHead`): keep the H1 "One question. One useful step." Lede: "Untimed practice, separate from your
   timed mock score. Play a short chapter feed, or take one question at a time." (phones show the first sentence only). The
   head's `aside` holds the subject: the lamp-lit `SubjectObject` (64 px from 900 px wide, 40 px on phones; `framed={false}
   lit`, keeping its `mk-pop` on change) and the Subject `Listbox`, label "Subject" visible (above it on desktop; to its left
   on one 48 px row on phones). This is the one object on the page.
2. **Chapter feeds,** right under the head, spanning the full content width (above the two-column area): 28 px above the
   section head, 16 px from the head to the row, 40 px below the row (or below the phone pager).
3. **Questions:** an `h2` "Questions" (display 700, 20 px) with the Chapter and Difficulty filters beside it from 900 px
   (grid `auto 1.5fr 0.8fr auto`, gap 12, the last cell "Clear filters") and under it on phones (the current two-column
   grid). The old list head with the 96 px object and the subject name is removed (the subject is in the page head). While
   subjects load, nothing says "your subject": the heading is "Questions" from the first paint.
4. **The right column follows the questions,** beside the list only (it is about answering questions): remove the
   "Tonight's rule" kicker; the heading "Answer first. Then ask why." drops from 30 px to 20/1.2 display 700, so the page has
   one hero. Its links and the solved count stay.
5. **Names:** the question meta and the Chapter filter show the chapter title ("Accounting for Partnership: Basic Concepts"),
   keeping the syllabus name as the filter's value (F13).
6. **URL:** `/explore?subject=&chapter=` preselects both and scrolls to Questions (F6). `links.explore()` keeps the query.
7. **Default subject:** the student's first subject (the covers API's own default), else the first available (F16).

Phone fold check for Option A (an acceptance check; the positions are estimates from the current captures, so a screenshot
decides): the lead cover's key must be fully visible above the dock without scrolling.
- 390x844: place tabs to y 142, H1 to about 205, a two-line lede to about 256, the subject row to about 320, the section head
  to about 392, the row from about 408, the cover's bottom about 740, the key's bottom about 726; the dock's top is about
  769. Visible.
- 360x780: the same head puts the key's bottom near 726 while the dock's top is about 705, so on phones under 380 px wide
  apply, in this order, until the key clears: (1) the lede as one line at 13.5/1.4, "Untimed practice, separate from your
  mock score." (2) the section's top margin 20 px instead of 28; (3) the H1 at 26 px. With (1) and (2) the key's bottom lands
  near 696.

**Option B (fallback if the page structure cannot change in this round):** covers stay inside the main column (3 per view by
4.3); move them above the filters, give the filters a "Questions" heading, remove the list-head object, and demote the right
column's heading. Everything inside the cover (4.2 to 4.9) is the same.

Option A is a reorder, not a rebuild: nothing is cut. The owner judges live prototypes (LK19) and has rejected rebuilds
before, so it is built in the preview behind the existing flag and shown to him, with B as the fallback.

### 4.11 Work split (BUILD-1101 Part 3 ownership) and contract additions

**S2a (`learn.js`, add-only fields, API-CONTRACT.md):**
1. `hook` = the first `card` item of the 10-minute dry run (the feed's real first card now); fall back to today's rule. Add
   `hook.id`. Test: a feed started right after reading the covers has `items[0].cardId === hook.id`.
2. `refLine` (4.2 rules: "Part 1, Ch 2", "Microeconomics, Ch 2", "Verbal Ability").
3. `name` (the syllabus name), for the Free-limit action, the filter and the chapter labels.
4. `resume: null | { done, of, minutesLeft }` for an unfinished feed today in that chapter; on such a cover `hook` is the
   next card item of that run when one is left (Play resumes it, so the preview stays true).
5. `studentLine` without due: resume, else "N old mistake(s) to fix", else the state label, else "New to you"; and top-level
   `history: boolean` (any chapter studied in the subject).
6. R12 refinements of 4.6 (skip a feed finished today; "First in the syllabus").
7. Starts from a cover send `source: 'explore_cover'`, `forYou`, `position`; the server keeps them in `start_state`.

**U2 (`ExploreCovers.jsx`, `covers.css`, `DiscoveryFeed.jsx`):** sections 4.2 to 4.9, the Free-limit action, the URL
parameters, the chapter labels, the default subject. Option A also moves the Subject control into the page head and the
Chapter and Difficulty filters to the Questions section: this goes past "covers area and chapter label only", so the CTO
widens U2's scope or takes Option B.

**P (`src/app/(app)/explore/**`, `links.js`):** `explore.css` for Option A (the full-width covers row above `.ex-layout`,
the Questions head grid, the right column's heading size and kicker); `links.explore({ subject, chapter })` keeping the
query.

**Not ours, noted:** U4 uses the same `SegmentedControl` on the chapter page; S1 looks at Free's card-to-question ratio
(5 cards to 7 questions, F8); `keycards.css` widens its surface tokens to `.fxc` (4.4).

### 4.12 Acceptance checks (to run on the built preview, with screenshots looked at)

Sizes: 1440x900, 1366x768, 1024x768, 390x844, 360x780, plus 430 wide; Night and Day; real pointer clicks.
1. **Distinct:** no `SubjectObject` inside `.fxc-row`; at most one on the page; the 14 Accountancy hooks are all different.
2. **One volt:** exactly one volt fill in every viewport at every size (the lead key); the sidebar Start is outlined on
   Explore; the dock Start is quiet while the lead key is on screen.
3. **Paging:** at 1440 and 1366, four covers and a 40 px peek; Next moves exactly four, Previous is disabled at the start,
   Next at the end; at 1024 three and a peek; on phones the pager reads "1 of 14" and its buttons move one cover; no
   horizontal page scroll at 360.
4. **Keyboard:** Tab reaches the control, Previous, Next, then one cover; Left and Right move between covers and bring them
   into view; Home and End work; Enter opens the feed; focus is always visible.
5. **Continuity:** opening a feed from a cover shows the cover's hook as its first card (`hook.id`).
6. **Free:** with the day claimed, the head line and "See Pro" show, every key reads "Questions on this chapter", a click
   sets the Chapter filter and scrolls to Questions, and no `POST /api/learn/runs` is sent. With 20 picked under the limit,
   the capped line shows.
7. **New student:** the lead reads "Start here: first in the syllabus"; no other cover says "New to you"; no "For you"
   anywhere.
8. **States:** blocked `/api/learn/covers` shows the error line, and Try again recovers; an empty subject shows its line;
   the skeleton matches the cover; "your subject" never appears; CLS stays at or under 0.01 on load.
9. **Fold:** 4.10's phone check.
10. **Names:** the Economics 61-character title is whole at 1024 and 360; the question meta shows chapter titles; the URL
    `/explore?subject=accountancy&chapter=Admission%20of%20Partner` preselects the filter.
11. **Reduced motion:** no transforms on hover, press or length change; paging jumps.
12. **Hit test:** `document.elementFromPoint` at each key's centre returns the cover link; at each arrow's centre, the
    arrow.

### 4.13 For the app later (A7, Flutter)

The same cover ports to a `PageView` with `viewportFraction` about 0.82 (302 of 390), the pager row under it, the lead's
key as the only filled lime, the hook in the display face on the lit card surface, and the length as the app's segmented
control. The data is the same `GET /api/learn/covers`.

---

## 5. Anti-slop test and rubric

### 5.1 The 12-part anti-slop acceptance test

| # | Test | Now | As proposed (to verify when built) |
|---|---|---|---|
| 1 | Identity with the logo hidden | Partial: volt keys and lamp-lit art are MockMob's, but repeated art reads as a template | Pass: the product's own Key cards, lit surface and keycap |
| 2 | One primary action | Fail: 3 to 4 volt fills (F2) | Pass: one volt key, the lead cover's |
| 3 | True content | Partial: counts are real, but "For you" without reason, a silent Free cap, a Play that is refused | Pass: reasons shown, caps and limits stated where they bite, resume named |
| 4 | Hierarchy at first scan | Partial: H1, a second display heading and covers compete; the object is the anchor and carries nothing | Pass: head, then feeds, then questions; the hook and title carry the chapter |
| 5 | Intentional composition | Fail: 3 covers with no peek at 1440, a cut cover at 1366, Play below the fold on phones | Pass: fluid widths with a fixed peek, fold checked |
| 6 | Typography by role | Partial: roles are right, long names would be clamped | Pass: hook, title, line, mix and key each have a role and size; no name is cut |
| 7 | Every state | Fail: error and empty vanish, "your subject" placeholder, Free-limit dead end | Pass: section 4.8 |
| 8 | Accessible interaction | Partial: good link names; no paging controls, 14 tab stops, swipe-only on phones | Pass: arrows, pager, roving focus, radio group, 44 px targets |
| 9 | No pseudo-evidence | Partial: "For you" implies personal choice for a new student | Pass: "Start here" when it is only book order |
| 10 | Motion with a reason | Pass, thinly: nothing moves without cause, but nothing answers the length switch | Pass: hover, press, number change and paging answer actions; reduced motion handled |
| 11 | One leading metric and one guardrail | Fail: none | Pass once 4.11 item 7 ships: leading, feeds started from covers per active Learn student per week and their completion rate (`learn_runs`); guardrail, Explore question answers per student per week do not fall, and zero 402 refusals start from a cover |
| 12 | What would be better without this? | Fail: the repeated object, the kicker, the second hero | Pass: each part answers a decision |

### 5.2 The 0/1/2 rubric (0 missing, 1 partial, 2 validated)

| Dimension | Now | As proposed | Note |
|---|---|---|---|
| Task fit | 1 | 2 | Pick a chapter and a length, then play; at the Free limit, practise questions instead |
| Information architecture | 1 | 2 | Filters next to the list; subject once, in the head |
| Content truth | 1 | 2 | Reasons, caps, shrink and resume all stated |
| Readable hierarchy | 1 | 2 | One hero; hook, title, line, key |
| Visual specificity | 0 | 2 | Every cover distinct by its own first card |
| Accessibility | 1 | 2 | Paging without a gesture, keyboard, names |
| Functional states | 0 | 2 | Section 4.8 |
| Trust | 1 | 2 | No refused primary action, no unearned "For you" |
| Intentional motion | 1 | 1 | Specified; becomes 2 only after it is seen on a real phone and a PC |
| Performance | 1 | 1 | Warm development timings only (covers in 1.3 to 2.0 s); the covers lose their 140 px images; production unmeasured |
| Responsive integrity | 1 | 2 | Container-query widths, phone fold check |
| Instrumentation | 0 | 1 | Needs 4.11 item 7 shipped and read |
| **Total (of 24)** | **9** | **21** | The proposed column is a target until the acceptance checks in 4.12 pass and the owner has seen it live |

A high visual score never cancels a correctness failure: F5 (a refused primary action) and F6 (a link that does not keep
its promise) must be fixed before any polish counts.

---

## 6. For the owner

Nothing needs his decision before building. What he should see on the live preview, at phone size and on his computer:
the covers with each chapter's own first card, the one lime key, the arrows on a computer and the pager on the phone, and
Option A's page order. He judges it there (LK19); Option B is ready if he prefers the old order.
