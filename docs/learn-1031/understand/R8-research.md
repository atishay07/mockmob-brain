# R8 research: owner UX rules for a learning area, and rival patterns (31 Oct 2026)

Scope: reading and web research only. No code changed. Written for the main session that will redesign Learn. Owner feedback (LK1 to LK14) is in `docs/brain/OWNER-FEEDBACK-2026-10-31-LEARN.md`.

How to read the tags:
- Rule numbers (R1 to R40) are the numbered rules in `docs/research/premium-ux-ui-2026-10/AGENT_RULES.md`.
- Evidence IDs (T001 to T009, S010 to S018) are from `source-ledger/EVIDENCE_INDEX.csv`. Only some rules carry an ID. Where a rule has none, I cite the rule number and say so.
- AS1 to AS12 are the 12 parts of the anti-slop acceptance test in `papers/ai-slop-independent.md`.
- RUB is the 12-dimension 0/1/2 rubric in the same file.
- Rival facts carry a URL. "Self-reported" means vendor marketing. "Unverified" means I could not confirm it from a first-party page.

Important limits of the owner's research brain (it says so itself in README.md): it is PARTIAL. Four of the five direct videos (8EAYZe6y3I8, qJ4qYhTqAz0, soZgjJi7xNw, XKDfs9xTzfw) were never retrieved. No video frames exist. Every rule is labelled "[I]" (our independent recommendation, informed by papers), not a creator order. The creators' numbers (jam study, 70-90% defaults, 2x loss aversion, completion "nearly doubled") are marked unverified and must not be quoted as facts. The research brain contains nothing specific about flashcards, libraries, search, feeds or print. Those topics are covered below only through its general rules.

---

## Part 1. The owner's UX research brain, rule by rule

### 1.1 Files that exist

| Path | What it is |
|---|---|
| `docs/research/premium-ux-ui-2026-10/README.md` | Edition note, evidence tags T/V/S/I, what is and is not verified. |
| `.../AGENT_RULES.md` | 40 numbered rules, MockMob overlay, 7 PR review questions. The main file. |
| `.../papers/uxpeak-2TlIg3VokY8.md` | "UX psychology behind apps people can't stop using": defaults, progress, value before signup, customisation, loss framing, price contrast (T001 to T006). |
| `.../papers/uxpeak-zr37ibqXl1U.md` | Three redesigns: trial, ride fares, villa booking (T007 to T009). Cross-case lessons. |
| `.../papers/uxpeak-03Xw8UyC6uo.md` | Foundations: UX vs UI, build a state machine before polish. |
| `.../papers/uxpeak-GGg61sdEjeI.md` | Description only (S010): product page hierarchy, sticky CTA. A research plan, not findings. |
| `.../papers/ai-slop-independent.md` | The 12-part anti-slop acceptance test, the diagnostic matrix and the 0/1/2 rubric. Not a summary of the unretrieved video XKDfs9xTzfw. |
| `.../papers/TimGabe-channel-context.md` | Motion rules context, no video analysed. |
| `.../papers/PENDING_*.md` | Placeholders only. Ignore. |
| `.../methodology/CAPTURE_AND_QA.md`, `visual-evidence/README.md` | Process notes. Visual evidence folder is intentionally empty. |
| `.../source-ledger/EVIDENCE_INDEX.csv`, `SOURCE_MANIFEST.csv` | Evidence IDs and source states. |
| `.../Premium_UX_UI_Research_Brain_Edition_01.pdf` | Not read (the markdown files are the same package). |

Rule 1 to 6 (source discipline) apply to our own design notes: name the user, task, data, state and success criterion; cite evidence IDs; never say a creator recommended something unless a timestamped transcript supports it; never invent test results or metrics; treat behavioural numbers as claims.

### 1.2 Rules that bear on the Learn area, grouped by the owner's themes

**A. Learn home and hub layout, hierarchy, information density (LK3, LK8, LK11)**

| Rule | Text in short | Evidence | What it means for Learn |
|---|---|---|---|
| R7 | One clear main action per task screen. Several equal calls to action need a written reason. | none (rule); AS2 | The Learn home needs one dominant "do this next" item. Equal tiles for Read, Study, Last look, Fix it fail this unless justified. But see LK11: the owner also wants options, so the single action must sit with a short row of alternates that are visibly secondary. |
| R8 | Rank content by what helps the user decide next, not by back-end entity or ease of development. | none | Do not show the data model (chapter, deck, unit, Key card, mode) as the structure. Show decisions: "What do you want to do, how long have you got?" |
| R9 | Essential data scan-friendly: value before label, clear units, meaningful status and dates. | none | Counts with units ("12 cards due", "about 10 min"), not walls of text. |
| R10 | Progressive disclosure for secondary functions; do not hide frequent or important controls to look minimal. | S014 (NN/g Progressive Disclosure) | Tension with LK11 and LK1. Hide the rare (print, settings, card-type filters). Do not hide the Key cards entry; the owner says it is already too small and badly placed. |
| R11 | Navigation consistency, accessible labels, selected state. | S016 (WCAG 2.2: consistent navigation, consistent identification) | Same names for the same thing everywhere. Read vs Last look confusion (LK7) is a naming-consistency failure. |
| R12 | Simple vertical rhythm for dense consumer mobile screens; grid only when comparison helps. | none | Learn on phone = a vertical list of decisions. A tile grid only for subject choice. |
| R28 | Whitespace separates concepts; do not enlarge everything. | none | |
| R33 | Cards group meaningful items; no cards for every label. | none | Warning: a screen of nested cards is slop. |
| AS2 | "Is the next useful action visually and verbally clear?" | ai-slop paper | Direct test of LK11. |
| AS4 | Can users identify the most relevant content in a short first scan? Test with real users, do not claim a fixed duration. | ai-slop paper | |
| Diagnostic row "Information architecture" | Generic symptom: identical 3-card summary everywhere. Deliberate: structure matches the next decision. Test: can the user find the target action without hunting? | ai-slop paper | Matches the owner's "confusing to find things" (LK9). |
| Example "Purposeful" CUET home | One current exam state, one last-result diagnosis, one next-best-move grounded in real history, why it was suggested, direct entry. Weak version: four glowing KPI cards, equal CTA tiles. | ai-slop paper | The owner's research already says what a MockMob home should be. Learn should follow the same grammar with 2 to 3 labelled alternates. |

**B. Choosers: subject, chapter, time; session setup (LK10)**

| Rule | Text in short | Evidence | What it means |
|---|---|---|---|
| R13 | Visible editable defaults only when backed by real context or safe assumptions. | T001, S015 | Pre-select the student's current subject, last chapter, and a 10-minute session only if that is their real last choice, and say so ("last time you did 10 min"). Always editable. |
| R14 | Never preselect consent, paid upgrades, data sharing. | none | |
| R18 | Say what happens next (count, time, task) when accurate. Use generic wording when dynamic facts are unknown. | none | A time chooser must show truthful consequences: "10 min: about 12 cards and 6 questions" only if computed from real pool sizes. |
| T001 note (paper 1) | Booking form with five empty fields vs prefilled sensible values plus a result-aware button ("12 results"). The paper's MockMob application: CTA reads "Start 10 Accountancy questions", never a fabricated count. Test: time to first question, % defaults edited, incorrect-start reversals, completion. | T001 | This is the closest thing in the brain to the owner's subject, chapter, time, go flow. Make the final button name the session. |
| Paper 1, section 2 | Prefer a labelled step sequence to an arbitrary percent when duration varies. | T002 | A three-step chooser ("Subject, Chapter, Time") is fine; a fake progress bar is not. |
| R17 | Progress must be truthful; never count steps not completed. | T002, S015 | No "20% done" for opening the page. |
| T004 | Give authorship over something useful (a goal, a path) and preserve it through auth. | T004 | Remember the student's chosen chapters and time across sessions and across guest to account. |
| R16 | Persist user-entered work through authentication. | T004 | |
| R35 and AS7 | Test empty, error, timeout, partial, no-data states. | none | Chapter with 0 cards, subject with a thin pool, offline. The chooser must say honestly what is available. |

**C. Next-best-move with options (LK9, LK11)**

| Rule | Text in short | Evidence |
|---|---|---|
| MockMob overlay, rule 1 | Every "next best move" must explain the supporting history, confidence and actionable subject or problem. If history is too thin, say so and suggest the first diagnostic action. | none (overlay) |
| R24 | "AI mentor" and "personalisation" claims must match logic that really runs, with known limits. | none |
| AS9 | No pseudo-evidence: invented counts, progress, urgency. | none |
| Example in ai-slop paper | Honest fallback when data is sparse: "take a baseline mock", not a made-up recommendation. | none |
| R22, T005 | No shame-based dismissal, fake countdowns, coercive loss prompts. | T005 |

Reading across: the brain wants a recommendation with its reason and confidence, and it also wants one main action (R7). It does not forbid showing alternates. The owner's complaint "it is just one thing, no more options" (LK11) is compatible with R7 if the alternates are clearly subordinate and each carries its own reason. Suggested reading: one primary (with reason), two to three secondary options, each specific ("Fix 3 weak cards", "Quick 5 min"), and a visible "pick your own" path.

**D. Flashcard study, mixed sessions, feeds, libraries, search**

The brain has no rule written for these. Rules that carry over by analogy:

- R24, AS9: any scheduling or "weak spots" claim must reflect real logic. The product rules in `KEYCARDS-BUILD-SPEC.md` already bind this build: no mastery percentage, never the word "mastered", a wrong answer is a hypothesis not a label, zero paid model calls for scheduling, uncertainty means quarantine or "not enough yet".
- R13, R18: labelled defaults, concrete next step.
- AS3 (true content), AS9: any badge such as "Must-know" is a claim. By AS9 it needs a sourced basis (for example "appeared in N previous papers", as `rival-research.md` item 12 already proposed). A badge on many cards fails AS12 ("what would be better without this?") and the diagnostic row "Content: placeholder stats, artificial testimonials". This directly supports LK13.
- Diagnostic row "Navigation: same sidebar whether mobile or consumer" and R12: library and search on mobile should be a vertical, scannable list.
- Circuit overlay (not MockMob, but the same principle): separate Today (urgent), Discover (broader), Listings, Inbox by task and state, "not a noisy equal-weight mosaic"; "favor list scanning on mobile; distinguish immediate action from exploration". Learn's three jobs map to this: Today (what to do now), Explore/Discover (feed), Library (find and revise specific things). That is the owner's LK10 ("a separate section") restated.

**E. Motion (LK5)**

| Rule | Text in short | Evidence |
|---|---|---|
| R31 | Motion needs a purpose (state change, continuity, feedback), reduced-motion behaviour, and no essential information conveyed only by animation. | none |
| AS10 | Each transition explains state or orientation; reduce motion when requested. | none |
| Diagnostic row "Motion" | Generic: unmotivated fades, decorative parallax. Deliberate: motion communicates cause, continuity, feedback. Test: what comprehension does the animation improve? | none |
| TimGabe context paper | Motion helps users understand state changes. Result-card transitions and onboarding steps benefit from continuity. Continuous hero animation and heavy scroll effects are rarely right in a timed exam. Contextual only; no video analysed. | none |

For "Got it": the animation must show the card leaving today's pile or moving to its next-review slot (cause and continuity), not confetti. Provide the reduced-motion version.

**F. Print and export (LK6)**

Nothing in the research brain. Closest: R5/R6 (no invented claims) and the general privacy rules in the system. Rival and vendor facts are in Part 2, section 2.9.

**G. Verification and review (applies to the redesign PR)**

- R34: verify on real small and large viewports. R36: keyboard, screen reader, focus order, text zoom, contrast, reduced motion, WCAG 2.2 (S016). R37: define the metric and a guardrail before claiming a pattern wins. R38: "feels premium" is not proof. R39: ship a `DESIGN_DECISIONS.md` with user task, screen alternatives, reason, evidence IDs, tradeoffs, unresolved assumptions, screenshot comparisons. R40: run the anti-slop rubric.
- The 7 PR review questions: what decision does the page help with; what can be removed without losing information; what does the primary action do exactly; which evidence IDs justify non-obvious choices; what could mislead (progress, price, data, personalisation, urgency); behaviour in loading, error, no-data, permission, slow-device states; how will we know it is better, not just different.

### 1.3 The 12-part anti-slop acceptance test (AS1 to AS12), written out

1. Product identity: recognisable as this product with the logo hidden.
2. One primary action: next useful action visually and verbally clear.
3. True content: metrics real, placeholders labelled, dates valid, testimonials sourced.
4. Hierarchy: the relevant content found in a short first scan (test with real users; no fixed seconds claimed).
5. Composition: margins, alignment, text measure follow intentional responsive rules.
6. Meaningful typography: roles (display, title, body, label, data), readable under zoom.
7. Statefulness: loading, error, retry, empty, partial, disabled, success.
8. Accessible interaction: focus, target size, semantics, contrast, reduced motion.
9. No pseudo-evidence: no invented counts, progress, urgency, reviews, uplifts, availability, endorsements.
10. Motion rationale: each transition explains state or orientation.
11. Measured usability: one leading metric and one guardrail (example given: activation plus wrong-choice corrections).
12. Human critique: ask "what would be better without this?" for every decorative block.

### 1.4 The 12-dimension 0/1/2 rubric (RUB)

Score each 0 (missing), 1 (partial), 2 (validated): task fit, information architecture, content truth, readable hierarchy, visual specificity, accessibility, functional states, trust, intentional motion, performance, responsive integrity, instrumentation. The paper says the score is an internal checklist, not proof of quality, and a human owner must sign off.

### 1.5 Where the owner's own research already contradicts the current Learn build

Based on the owner feedback (not on code I read):
- R7/AS2: a single suggestion with no alternates, or several equal tiles, both break the spirit. The brain asks for one primary plus reasons.
- R8: structure by back-end entity (chapter, card, mode) rather than by decision.
- R11: Read vs Last look are two names for similar-looking things.
- R12/R33: "lines and lines of text" and card-in-card layouts.
- AS9/AS3: "Must-know" on many cards is an unsourced claim.
- R10: the way into Key cards is hidden or too small (LK1). Frequent controls must not be hidden.
- R31/AS10: Study mode has no motion on Got it (LK5).

---

## Part 2. Rival and reference patterns

Method: WebSearch and WebFetch only. Where a site returned 403 (Quizlet help centre and blog, Khan Academy support) I did not work around it; I used search-result summaries and say so. Third-party blogs are flagged. Several rivals do not document a feature at all; I say "not documented" rather than guess.

### 2.1 What `intel-1031/rival-research.md` already covers (do not redo)

File: `C:/Users/atish/Desktop/mockmob copy/wt-1031-keycards-web/docs/brain/intel-1031/rival-research.md` (13 KB, 31 Oct 2026). It covers taxonomy, memory, analytics and retention, not session setup. Already known there:
- CUET rivals: PW (per-subject series, chapter and unit tests, unlimited re-attempts, printed Mind Maps per chapter), Testbook (739 tests with Chapter, Unit, NCERT Exemplar, Question Type axes; analysis "locked after pass expiry"), Easetolearn "Gap Fixer Sessions", Embibe (concept mastery, Sincerity Score, 10 behaviours, Achieve diagnostic-first), MARKS (PYQs, custom tests, quiz mode, formula cards).
- Memory: FSRS vs SM-2 (docs.ankiweb.net), Brainscape 1 to 5 confidence, Quizlet adaptive Learn (scheduling only in paid), RemNote cloze in notes, Duolingo half-life regression (+9.5% daily retention for practice sessions, vendor blog), Khan Academy levels (Attempted, Familiar, Proficient, Mastered).
- Its ranked ideas include: 4-level chapter state, weak-chapter "Fix it" session, FSRS defaults, 3-button card rating, typed NCERT-line cards (cloze, true/false), wrong answer to "add these cards", daily revision queue with cap, diagnostic first, importance badge from PYQ frequency ("appeared in N papers").
- Its "avoid" list: raw % on 3 to 5 questions, 10-label behaviour taxonomies and black-box scores, copying rivals' vague counts, Class 11 chapters, per-user FSRS optimisation or knowledge graphs at launch, paywalled spaced repetition.

Conflict to flag: `rival-research.md` idea 1 suggests levels "Untouched / Learning / Solid / Mastered". The build spec product rules say never use the word "mastered" and no mastery percentage. Use other names (for example Not started, Shaky, Getting there, Solid) if levels are kept.

New in this report: session setup, session length, mixing cards with questions, end-of-session options, libraries, cram, feeds, print.

### 2.2 Per-platform findings

#### Anki (desktop, AnkiDroid, AnkiMobile)
- Deck overview screen: a deck click opens an overview with three due counts, New, Learning, To Review, and a Study Now button. Source: https://docs.ankiweb.net/studying.html (official).
- Sessions run until the day's cards run out. During study there are four answer buttons (Again, Hard, Good, Easy) and each button shows when the card will next appear. Same source.
- Custom Study sits at the bottom of the overview. Presets: increase today's new-card limit, increase today's review limit, review forgotten cards (failed in the last N days), review ahead (due in the next N days), preview new cards, study by card state or tag. Source: https://docs.ankiweb.net/filtered-decks.html (official).
- Cram: the manual does not use the word "cram"; the nearest is Study by card state or tag with the card count set above the deck size. The manual warns review ahead is "not appropriate for repeated use" and that rescheduling during cramming changes real intervals (turn rescheduling off to leave schedules alone). Same source.
- Problem users hit: after the day's cards are done, Anki stops offering cards, and a user asked for a "cram" toggle because Custom Study needs several steps. Source: https://forums.ankiweb.net/t/quick-study-button-feature-request/45203 (forum, user report).
- Lesson: Anki is powerful and has no time chooser and no mixed question types. Its extra-session path is hidden and technical; MockMob should make "I want more, or I want something different" a visible first-class option.

#### Quizlet (Learn, Flashcards, Test)
First-party help pages returned 403, so this section rests on search summaries and one help-centre snippet.
- Learn adapts within a session and retests what you missed at the end of each round. Older guides say it ends when every term is answered correctly twice in a row; this is from older third-party guides and is unverified for the current app. Sources: https://www.slideshare.net/slideshow/using-quizlet/15162607 (old guide), https://help.quizlet.com/hc/articles/360048803491 (help centre, via search snippet).
- In a set you can pick Not Studied, Still Learning or Mastered to study only that group. "Study paths" are a paid (Plus) feature and can be switched off to use standard Learn. Same help article (search snippet).
- Learn options include question types and prompting with term or definition. Learn has a Start Over under Reset Progress (help snippet).
- Test mode: simulated exam. Per-test question-count and type options exist in Quizlet generally, but I could not confirm current wording. Unverified.
- Quizlet does not publish scheduling details (analysis blog, https://www.notelyn.com/blog/quizlet-spaced-repetition, third party).
- I found no confirmed session-length (5/10/20 minute) setting. Unverified.
- Lesson: group-by-state in the library (Not studied, Still learning, Mastered) is a clean self-control pattern. Avoid the word "Mastered" per MockMob's rules.

#### Duolingo
- Home is a linear path of circles; the path sets the order. Practice sessions are built into the path ("Practice is also forward progress"). Free users start a practice session from the heart icon; subscribers get a Practice Hub with several sets. Source: https://blog.duolingo.com/new-duolingo-home-screen-design (official).
- The stated rationale: many learners were unsure they were using the app the right way, so the path gives a clear sequence, and review is ordered with spaced repetition. Same source.
- Daily goal vs streak split. A 1-lesson action extends the streak and daily-goal progress is shown separately. Reported A/B result: +10.5% of daily learners on a streak overall, +19% for new learners; the highest-goal tier ("intense") had the lowest streak rate; fewer learners hit their goals afterwards. Source: https://blog.duolingo.com/improving-the-streak/ (official, vendor-reported).
- Goal tiers as 5, 10, 15, 20 minutes: only from third-party guides (https://duolingoguides.com/how-to-set-goal-of-15-minutes-in-duolingo/), and the official post above describes the goal as lessons per day. Unverified; do not cite as fact.
- Duolingo decides what to study and when to review so learners do not plan themselves (Japanese-language help page via https://blog.duolingo.com/how-to-use-duolingo/). Learners can take a level test to start at a matching unit.
- End-of-lesson summary details: no reliable first-party description found. Third-party mockups only. Unverified.
- Lesson: single path suits beginners. MockMob's owner explicitly wants control, so copy Duolingo's "streak is cheap, goal is separate" and "practice counts as progress", not its fully prescribed path.

#### Brilliant
- Courses are chosen by subject; lessons are short, hands-on problems with instant feedback. Third-party sources say about 15 minutes; no source says 5. The App Store listing mentions a personalising tutor and monthly new courses but no lesson length, daily goal or review feature. Sources: https://apps.apple.com/ec/app/brilliant-learn-by-doing/id913335252?l=en-GB (store listing), https://edwize.org/brilliant-review (third-party review).
- Lesson: one fixed lesson length per course; no student-chosen length. Little to copy for session setup.

#### Khan Academy
First-party support pages returned 403; below is from search results of those pages.
- Skill levels Not started/Attempted, Familiar, Proficient, Mastered; unit tests and course challenge sample skills across a unit or whole course; quizzes and unit tests can move a skill up several levels so a learner who already knows content can "prove it" and jump ahead. Source: https://support.khanacademy.org/hc/en-us/articles/115002552631 (via search summary); the "jump ahead" wording is from a 2018 beta post, may be out of date.
- Learners can work on any skill from the course page after the initial challenges.
- Lesson: "test out" is a respectful control for confident students. Do not copy the "Mastered" label or percentage.

#### Seneca (UK exam revision; closest functional match found)
First-party help pages were readable.
- Courses are exam-board specific; each course is split into small sections; a session = read a short explanation, answer questions, get instant feedback, practise again. Source: https://help.senecalearning.com/en/articles/2483292-what-is-seneca-learning
- Cram Mode (Multi Section Session): quiz-only. You choose the topics or tap Random. Each topic shows up to 4 random questions; a topic completes once 4 are studied; the session ends when all chosen topics are covered; you can tap Finish early and see topics you did well in and those needing work. Free sessions are limited to 20 questions. Source: https://help.senecalearning.com/en/articles/9203749-multi-section-session-aka-cram-mode
- Smart Learning mode models your forgetting curve per topic and returns a prioritised list of sections ("tells you what to learn and when"); available once enough data exists. Source: https://help.senecalearning.com/en/articles/2512816-what-is-the-smart-learning-mode
- Wrong Answers mode: open a course Overview, find it under a "For you" section, choose a topic, retry questions you got wrong. Free students can spend tokens (earned by finishing sessions) on a multi-topic version of up to 20 questions. Source: https://help.senecalearning.com/en/articles/3568906-what-is-wrong-answers-mode
- The Daily XP goal was hidden in February 2026 and replaced by a "Revision Planner" (an AI study plan; the help page gives no detail). Source: https://help.senecalearning.com/en/articles/7878107-what-happened-to-my-daily-xp-goal
- Teachers can set homework and revision on any topic; parents see time spent and scores. Same what-is page.
- Lesson: Overview has a "For you" band with distinct labelled options (smart list, wrong answers), and a separate topic-picked cram. Strong template for LK9, LK10, LK11. Note they cap items per topic, which keeps a mixed session from being dominated by one chapter.

#### Knowt
- Study modes on a set: flashcards, Learn, Test, Spaced Repetition, Matching. Learn: customisable question types, brings back what you struggle with. Spaced repetition: you rate difficulty and choose which question types appear (flashcard, multiple choice, true/false, written). Sources: https://knowt.com/teachers/independent-learning-study-skills, https://intercom.help/knowt/en/articles/10298067-how-do-i-use-the-spaced-repitition-mode (search snippet; the page itself returned 404 on fetch).
- Knowt's help recommends Learn rather than Spaced Repetition when the exam is within about 30 days; a third-party FAQ says about a week. The timeframes conflict.
- Teacher page says MCQ practice has customisable difficulty, time and quantity. No study-plan or session-length setting described.
- Lesson: naming modes by when to use them ("exam soon", "long term") is a good answer to LK7, but vendors disagree on thresholds; define ours from our own scheduler.

#### StudySmarter
- Three modes on a flashcard set: Spaced Repetition (Learn), Flashcards, Test. In Learn: question first, tap Show answer, rate Bad, OK, Good (swipe right Good, left Bad on mobile). Source: https://studysmarter.zendesk.com/hc/en-gb/articles/360010134119-Learn-your-flashcards
- App listings mention a study plan with exam dates and a calendar; a third-party review reports problems with exam-date setting. No official how-to found. Unverified. Source for search listing: https://apps.apple.com/in/app/id1439949520
- Lesson: 3-point rating is the norm; a study plan keyed to an exam date is claimed but unproven.

#### Gizmo
- Turns notes, PDFs, slides, web pages, YouTube into flashcards, then builds multiple-choice quizzes from the deck; says it uses active recall and spaced repetition. Gamification: daily streak (answer a set number daily), leaderboard, 15 lives per day, wait 10 minutes or pay for unlimited. A subscription removes the 10-quiz daily limit on AI quizzes. Source: https://techcrunch.com/2023/09/21/ai-startup-gizmo-funding-gamified-quizzes-flashcards-make-learning-fun/ (2023 news; may be dated).
- Testers in a Save My Exams review switched between flashcards, Learn mode, tests, matching, multiple choice and written questions (https://www.savemyexams.com/learning-hub/useful-resources/best-ai-flashcard-generator/, listing only; article body not read).
- Session length and card ordering are not documented.
- Lesson: flashcards and MCQs live in the same product but as separate modes, not one blended session. Lives and paywalled limits would clash with the "unlimited" USP.

#### Indian exam apps
- Physics Wallah: DPPs, notes, test series sit in the Batch section; chapter-wise tests; separate PW Pi "Pocket Course" and "One Shot" chapter revision, Quiz of the Day. Flashcards exist only in the separate PW Books app. Sources: https://www.pw.live/neet/dropper/batches/rapid-revision-series--neet--2025-571362, https://www.pw.live/news/pw-books-app-launch-digital-study-books-ai-doubt-solving (search summaries).
- Embibe: Achieve (diagnostic, knowledge graph, learn then practice). Practice flow: choose subject, then chapter, optionally topics, then source (book, syllabus, Big Book) and press "Practice Now"; "Important", "Difficulty", "Lengthiness" tags on chapters guide priority; per-question hints and step-wise micro-hints; revision list filter (questions to revise, all subjects, units, chapters); students cannot set question count or timer (timers are platform-set); custom tests are premium. Sources: https://embibe.com/in-en/best-education-content/dynamic-and-adaptive-practice-to-increase-competency-levels, https://www.embibe.com/in-en/helpdesk (partial read, first 100,000 characters only).
- Testbook: tap a subject to see "Chapter wise practice sets"; website has a "search chapters" box; Testbook Pass has unlimited practice and reattempts; notes and doubt support only in the app. Source: https://intercom.help/testbook-da1e94f5d0c5/en/articles/6655211-where-can-i-get-practice-sets-for-my-exams (search result).
- MARKS: official page lists PYQs, custom tests, quiz mode, formula cards; chapter-wise organisation and bookmarks are only on third-party listings. Source: https://getmarks.app. The page names no time or session-length options.
- Unacademy: listings say mock tests, quizzes, courses and flashcards/study guides; no details found. Toppr: practice questions and live doubts, no flashcards found. Exam Gyani: nothing found. All three are weak or unverified.
- Lesson: the Indian apps are test-and-video led. Nothing found offers "pick a time, get a mix of cards and questions". That is open space for MockMob. Embibe's subject, chapter, optional topics, Practice Now ladder is the nearest Indian precedent for the owner's chooser flow; its tags are worth studying but its non-editable question count is the opposite of what the owner wants.

#### Adjacent builder with the owner's exact setup flow
- ePrepare quiz builder: choose subject, chapter(s) or sub-topics, MCQ limit, timer (or untimed), feedback mode (after each question or at the end), then Generate; pause and resume; attempt history. Source: https://eprepare.org/quiz-builder (vendor page). Small player, but it is the clearest documented chooser with count and timer.

#### Feed-style learning (new, small players, all vendor pages)
- EduSwipe (PDF to swipeable flashcards with quiz and spaced repetition), BesserStudy (quiz feed with streaks and XP), Scroller (create subjects, scroll questions), Studii (2-minute AI lessons in vertical format), ScrollEd (pre-launch; a reviewer notes no independent evidence of learning outcomes or accuracy), WikiTok and Wiki-Tik (articles, no quizzes). A developer guide argues the feed needs quizzes or users feel entertained but not smarter. Sources: https://propakistani.pk/2026/09/21/this-app-turns-your-study-material-into-a-tiktok-style-learning-feed/, https://apps.apple.com/ca/app/studii-doomscroll-learn/id6755154363, https://fastpix.com/blog/how-to-build-a-tiktok-style-microlearning-app (search results).
- No evidence of learning outcomes for any of them. Treat as pattern inspiration only.

### 2.3 Evidence on mixing question types (retrieval practice and interleaving)
- Mixed practice (interleaving) has randomised classroom evidence in maths: Rohrer et al. 2020 (787 students, 54 classes, 5 schools; test at least a month later; summary figures 61% interleaved vs 37% blocked) and Brunmair and Richter 2019 (meta-analysis; small positive effect, strong variation). Sources: https://ies.ed.gov/ncee/WWC/Study/80702, https://www.frontiersin.org/articles/10.3389/fpsyg.2019.02296/full, https://Www.Gwern.net/doc/psychology/spaced-repetition/2019-rohrer.pdf (via search). The headline percentages appeared in a secondary summary; read the primary papers before citing numbers.
- Blocked practice feels better in the moment ("fluency illusion"); mixed practice feels harder. This supports a short note that explains why a mixed session feels harder, and argues against showing live "accuracy %" mid-session. Source: same search results, one secondary page; moderate confidence.
- This studies interleaving of problem types, not flashcard-plus-MCQ blending. Say so in any design note (R5, R38).

### 2.4 Print, watermark and download (LK6)
- Per-viewer ("dynamic") watermarks are the standard for course PDFs: name, email, date or IP stamped on every page, plus a static line such as "do not distribute". Vendors say it deters sharing and lets owners trace a leak. Sources: https://www.locklizard.com/document-security-blog/dynamic-watermarking/, https://www.verydoc.com/blog/how-to-automatically-watermark-pdfs-with-user-information-to-prevent-sharing.html (all vendor marketing).
- Limits stated in the same sources: a watermark is a deterrent, not a lock; it does not stop screenshots, photos or retyping. Claims of screenshot blocking could not be verified.
- Design note (mine): name plus a short ID is enough to trace; adding a phone number puts personal data on every copy. Tile it diagonally with low contrast so it does not hurt reading, repeat it across the whole page, and put it on the printed output and any PDF export. A visible MockMob mark on every page also serves the owner's "our watermark all over" ask without implying false security. Confirm privacy position before putting email or phone on printed sheets.

---

## Part 3. Ten patterns worth copying for MockMob

Each pattern lists the source, the owner item it solves, and the research rule it satisfies.

1. **One chooser ladder: subject, then chapters (one or several), then time, then a named Start button.** Sources: Embibe Practice Now ladder, ePrepare builder, Seneca cram topic-picker (URLs above). Solves LK10. Rules: R13 (editable, evidence-backed defaults), R18 and T001 (button names the session, for example "Start 10 min: Partnership, 12 cards and 6 questions", only with counts really computed), T002 (labelled steps, not fake percent). Keep topics optional ("Whole chapter" default, "Pick topics" secondary).

2. **Time as the unit of choice (5, 10, 20 minutes), converted by us into a mix.** No major rival documents a student-chosen time for card-plus-question sessions; Embibe even locks the timer; Duolingo's minute-tier goals are third-party only. So this is a differentiator, and also unproven. Solves LK10, LK12. Rules: R18, R37 (define a metric and guardrail first: time to first card, session completion, edits to the default). Show the plan in plain words before starting ("about 8 cards, 4 questions") and let the student drag it.

3. **A Learn "Today" band: one primary with its reason, plus 2 to 3 labelled alternates, plus "Choose your own".** Source: Seneca "For you" band (Smart Learning, Wrong Answers), Duolingo practice-as-progress. Solves LK9, LK11. Rules: R7 and AS2 (single primary), MockMob overlay (reason, confidence, honest sparse-data fallback), AS9. Typical alternates: "Fix 3 weak cards", "Quick 5 min", "Pick up Partnership: Basic concepts". When history is thin say so and offer a first diagnostic.

4. **An Anki-style chapter overview with three honest counts and one primary button.** Source: https://docs.ankiweb.net/studying.html. Solves LK4, LK7, LK3. Rules: R9 (value before label, units), R12, R33 (no cards inside cards). Counts: "To revise today / New / Shaky" in MockMob's own words. This replaces a wall of text with three numbers and a button, and replaces the Read/Study/Last look trio with a decision.

5. **A Library by state, with search and filters, as a separate tab from the daily flow.** Sources: Quizlet group-by-state (Not studied, Still learning, Mastered), Testbook "search chapters", Embibe revision-list filters, Anki Browse. Solves LK10 ("separate section ... revise specific cards"). Rules: R8 (organise by the student's decision), R12 (vertical list). Use MockMob-safe names (not "Mastered"). Allow "Revise just these" from any filter result.

6. **Name modes by situation, not by function, and explain the difference in one line.** Sources: Knowt (Learn for exam-soon, Spaced for long-term), Anki custom-study presets named by task ("Review forgotten cards", "Review ahead"). Solves LK7 (Read vs Last look). Rules: R11 and S016 (consistent identification), AS1. For example "Learn it" (first pass), "Check it" (cards and questions), "Before the exam" (fast scan). Do not keep two modes whose difference needs explaining.

7. **Finish early, and a summary that shows what went well, what needs work, and the next options.** Sources: Seneca cram Finish button; Anki per-button next-review times. Solves LK5, LK11. Rules: R31 and AS10 (animate the card moving to its next slot), R17 (only real progress), MockMob overlay (a wrong answer is a hypothesis). Summary ends with 2 to 3 next moves (for example "Fix 3 cards", "Another 5 min", "Next chapter"), the same grammar as pattern 3. Let Got it show "see again in 2 days" (or the like) as the motion's payoff.

8. **Separate the streak from the goal; make a tiny action count.** Source: Duolingo streak change (vendor A/B: +10.5% daily learners on a streak, +19% new learners). Solves retention without pressure. Rules: R22 and T005 (no coercive loss framing), R17 (truthful progress). Count a 5-minute session or ten cards as a day. No lives or paywalled limits (Gizmo-style) given the unlimited-mocks USP.

9. **Cram as a capped, multi-chapter session with an item cap per chapter.** Source: Seneca Cram Mode (up to 4 questions per chosen topic, Random option, ends when all covered). Solves LK12 and exam-eve use. Rules: R13, R18. Add Anki's warning in our own design: cramming should not silently reshuffle the long-term schedule (offer "count this towards my schedule" off by default for last-minute runs).

10. **Mixed card-and-question sessions, with a feed version in Explore, capped and ended.** Sources: interleaving evidence (Rohrer 2020; Brunmair and Richter 2019), feed apps that pair a vertical feed with quizzes (EduSwipe, BesserStudy, Scroller; vendor claims only), Duolingo (practice inside progress). Solves LK12. Rules: R31 (motion with purpose), R13 and R18 (a chosen chapter and "10 minute lesson" as an editable default), AS9 (do not claim learning gains). Build it as a bounded 10-minute run that ends with the pattern-7 summary, not an endless scroll. Explain once that mixed practice feels harder on purpose.

Also worth taking even though not in the ten: a watermark that tiles diagonally with name plus short ID on every page of the print sheet (Part 2.4), and replace "Must-know" with a sourced signal such as "appeared in N papers" shown only on the cards where it is true (R5/AS9, `rival-research.md` item 12).

## Part 4. Five things to avoid

1. **A single prescribed path with no way out (Duolingo-style) or a single suggestion (what the owner just rejected).** Violates LK9 and LK11, and R7 read together with the overlay (one primary plus reasons plus alternates). Evidence: Duolingo's home is a fixed path; Embibe fixes counts and timers, which the owner dislikes.
2. **Mastery language and numbers: "Mastered", mastery percentages, 10-label behaviour taxonomies.** Khan and Quizlet use "Mastered"; Embibe uses a Score Quotient and ten behaviour labels. MockMob rules forbid the word and the percentage; AS9 forbids unbacked precision; `rival-research.md` already warns against noisy per-chapter accuracy.
3. **Gating, lives and daily limits on core practice (Gizmo lives, 10-quiz cap; Quizlet paid study paths; Seneca free cram caps at 20; Testbook locking analysis after pass expiry).** Clashes with the unlimited-mocks USP and with R14/R22 spirit (no pressure to pay). Seneca's cap is the one to watch because it is otherwise the best template.
4. **Endless-feed mechanics and engagement mimicry (infinite scroll, brainrot modes, leaderboards used as pressure).** The feed apps cite no learning evidence; AS9 and R22 apply. A bounded 10-minute run avoids this.
5. **Hidden or power-user-only extra sessions and too many near-duplicate modes (Anki Custom Study buried under the overview; Quizlet and Knowt each with 5 or more modes; Gizmo's mode names differ by listing).** This is the exact "Read vs Last look" confusion (LK7) and a breach of R10/R11. Fewer, situation-named modes, with the alternative paths visible.

Also do not repeat: badges that appear on most items ("Must-know" on many cards, LK13). Fails AS12 and the ai-slop diagnostic "Content" row.

---

## Part 5. Open questions and unverified items

- Quizlet help centre and blog pages, Khan Academy support pages: 403 on fetch; findings come from search summaries. Re-verify Learn options, Test options and Khan thresholds from the app itself if they matter to a decision.
- Duolingo: no first-party description of the end-of-lesson summary or minute-tiered goals found. Third-party only.
- StudySmarter study plan and exam-date flow: no official how-to; a third-party review reports bugs.
- Gizmo: 2023 article; modes may have changed.
- Unacademy, Toppr, Exam Gyani, Brilliant lesson length: little or nothing first-party.
- Embibe helpdesk read only for its first 100,000 of about 313,000 characters. Auto-generated tests and quick tests might be documented later in that page.
- The interleaving percentages (61% vs 37%) came from a secondary summary; read Rohrer et al. 2020 before quoting.
- Does a student-chosen 5/10/20 minute mix of cards and questions improve outcomes? No rival evidence; needs our own metric (R37).
- Four of the owner's five research videos were never retrieved; the brain may gain rules about motion or AI slop later. Check `SOURCE_MANIFEST.csv` for updates before final sign-off.
- Transcription guess in the feedback file ("Fitzmeen downloading") is still unconfirmed; it changes whether print should be allowed at all or only watermarked.

## Sources (all fetched or returned by search in this session)
- https://docs.ankiweb.net/studying.html
- https://docs.ankiweb.net/filtered-decks.html
- https://forums.ankiweb.net/t/quick-study-button-feature-request/45203
- https://www.slideshare.net/slideshow/using-quizlet/15162607
- https://help.quizlet.com/hc/articles/360048803491
- https://www.notelyn.com/blog/quizlet-spaced-repetition
- https://blog.duolingo.com/new-duolingo-home-screen-design
- https://blog.duolingo.com/improving-the-streak/
- https://blog.duolingo.com/how-to-use-duolingo/
- https://duolingoguides.com/how-to-set-goal-of-15-minutes-in-duolingo/
- https://apps.apple.com/ec/app/brilliant-learn-by-doing/id913335252?l=en-GB
- https://edwize.org/brilliant-review
- https://support.khanacademy.org/hc/en-us/articles/115002552631
- https://help.senecalearning.com/en/articles/2483292-what-is-seneca-learning
- https://help.senecalearning.com/en/articles/9203749-multi-section-session-aka-cram-mode
- https://help.senecalearning.com/en/articles/2512816-what-is-the-smart-learning-mode
- https://help.senecalearning.com/en/articles/3568906-what-is-wrong-answers-mode
- https://help.senecalearning.com/en/articles/7878107-what-happened-to-my-daily-xp-goal
- https://knowt.com/teachers/independent-learning-study-skills
- https://intercom.help/knowt/en/articles/10298067-how-do-i-use-the-spaced-repitition-mode
- https://studysmarter.zendesk.com/hc/en-gb/articles/360010134119-Learn-your-flashcards
- https://apps.apple.com/in/app/id1439949520
- https://techcrunch.com/2023/09/21/ai-startup-gizmo-funding-gamified-quizzes-flashcards-make-learning-fun/
- https://www.savemyexams.com/learning-hub/useful-resources/best-ai-flashcard-generator/
- https://www.pw.live/neet/dropper/batches/rapid-revision-series--neet--2025-571362
- https://www.pw.live/news/pw-books-app-launch-digital-study-books-ai-doubt-solving
- https://embibe.com/in-en/best-education-content/dynamic-and-adaptive-practice-to-increase-competency-levels
- https://www.embibe.com/in-en/helpdesk
- https://intercom.help/testbook-da1e94f5d0c5/en/articles/6655211-where-can-i-get-practice-sets-for-my-exams
- https://getmarks.app
- https://eprepare.org/quiz-builder
- https://propakistani.pk/2026/09/21/this-app-turns-your-study-material-into-a-tiktok-style-learning-feed/
- https://apps.apple.com/ca/app/studii-doomscroll-learn/id6755154363
- https://fastpix.com/blog/how-to-build-a-tiktok-style-microlearning-app
- https://ies.ed.gov/ncee/WWC/Study/80702
- https://www.frontiersin.org/articles/10.3389/fpsyg.2019.02296/full
- https://Www.Gwern.net/doc/psychology/spaced-repetition/2019-rohrer.pdf
- https://www.locklizard.com/document-security-blog/dynamic-watermarking/
- https://www.verydoc.com/blog/how-to-automatically-watermark-pdfs-with-user-information-to-prevent-sharing.html
- Internal: `docs/research/premium-ux-ui-2026-10/*`, `wt-1031-keycards-web/docs/brain/intel-1031/rival-research.md`, `KEYCARDS-BUILD-SPEC.md` (product rules), `docs/brain/OWNER-FEEDBACK-2026-10-31-LEARN.md`.
