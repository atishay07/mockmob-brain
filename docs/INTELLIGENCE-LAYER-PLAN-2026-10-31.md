# Intelligence layer plan (31 Oct 2026)

**What you asked for (31 Oct, dictated):** a more refined intelligence layer across the platform.

The core feature is each chapter's highlight material (key terms, definitions, very important lines) as flashcards. They serve book revision, fixing mistakes and learning.

Behind the cards sits a read of every student's weak and strong chapters, with accuracy mapped chapter by chapter to the questions.

Alongside that:
- check that all 15 subjects have enough questions, cards and practice in every chapter
- check that the syllabus map is right for both CUET and Class 12 boards
- group chapters into sensible units
- see how other platforms do it

Plan first, then build.

**What this plan rests on.** A read-only check of production on 31 Oct, the code, the CUET 2026 syllabus PDFs in `data/CUET 2026/`, and a scan of rival platforms. Nothing was changed or generated. The detailed reports are linked in section 9.

---

## 0. The short version

1. **Fix the base before building on it.**
   - **The syllabus map has real errors.** 217 live questions sit in chapters NCERT has dropped. Several chapters are split across two names. "Existing ... Coverage" placeholder units are shown to students.
   - **Half the core chapters are thin.** 97 of the 221 chapters with questions have fewer than 20 live questions.
   - **"Weak chapter" is computed in four different ways.** The places that show it can disagree with each other.
2. **Build one spine:** Subject > Unit > Chapter > Concept, with stable IDs. Every question, card and student record points at it.
3. **Build Key cards on that spine.** Each chapter gets a deck of key terms, definitions, key lines, formulas and facts, tied to an NCERT page and weighted by how often CUET asks it.
   - Cards are scheduled with the FSRS memory model the Learn suite already uses.
   - Cards are reachable from book order, from your mistakes, from the daily queue and as a last look before a paper.
4. **Build one student model:** a chapter state for each student, read on two axes. *Answering* is how well you solve questions. *Remembering* is how well you recall the cards. Every label shows its reason and needs a minimum of evidence before it changes.
5. **Build loops that use it.**
   - A wrong answer shows the card you needed.
   - A paper's result opens a "Fix it" set from your weakest chapters.
   - The daily Revise queue mixes due cards with due mistakes.
   - Ask Mobi reads the chapter state, not raw history.
6. **Fill content to a written target** of at least 40 live questions and about 30 cards in every core chapter, gated by quality checks and your go per wave.

---

## 1. What we have today (production, 31 Oct)

### 1a. Questions
- **8,549 live, 1,501 pending, 1,068 rejected.**
- **The 15 core subjects:** 221 chapter names carry live questions. The median chapter has 20.
  - 97 chapters have fewer than 20.
  - 100 have 20-39.
  - 8 have 40-59.
  - 16 have 60 or more.
- **Accountancy is 1,405 questions, three times any other subject**, and lopsided inside: Share Capital 225, Debentures 216, Retirement & Death of Partner 16, Financial Statements of Company 10.
- **Thinnest real chapters:**
  - Inverse Trigonometric Functions 6
  - Interface Python with MySQL 6
  - Geography's "Geographical Perspective on Selected Issues and Problems" 5
  - Manufacturing Industries 7
  - Plotting Data using Matplotlib 7
  - Stack 8
  - Cold War Era 8
  - Rise of Popular Movements 8
  - Democratic Upsurge and Coalition Politics 9
- **Little below chapter level.** Concept tags exist on 0 Biology, History and Geography questions, and on 4 Chemistry questions. Generated questions have one concept per chapter. The `question_concepts` table has 0 rows. So accuracy below chapter level is not possible today.
- **Few links to past CUET papers.** Only 80 live core questions point at a past-paper anchor. Biology, History, Geography and GAT have none.
- **Weak explanations** (missing or under 40 characters): 525 live questions in the core subjects. The worst are Economics 67, Sociology 68, Computer Science 67 and Physics 60.
- **Rough fill needed** (before the syllabus fixes): about 4,270 questions to reach 40 per chapter, about 8,500 to reach 60.

### 1b. Cards and revision
- **Learn suite:** 24 study units and 112 cards, in English, Accountancy, Business Studies and Economics only. 16 units are published and 3 quarantined. The other 11 subjects have no cards at all.
- **The Learn suite already has the right scheduler.** It runs FSRS (`ts-fsrs` 5.4.2, 90% target retention, 5 new cards a day, new cards paused when more than 20 are overdue). It also has a packet compiler (`data/study/authored/packetCompiler.mjs`) that turns a fact list into a lesson, cards and a summary.
- **Revise on the live site** (`data/revise.js` on main) brings your own wrong questions back on a 1/3/7/21-day box schedule, 10 a day.
- **Two queues, never shown together.** Revise has its own state table (`revise_cards`, 84 rows) and Learn has `study_card_states` (15 rows).
- **Trap atlas:** 8 rows.

### 1c. Students and analytics
- **791 students have some progress; 12 were active in the last 30 days.** Any model must work on very little data, both per student and across students. That rules out anything trained on our own population for now.
- **"Weak chapter" is computed in four different places with four different rules:**
  - `prepos_insights.js`: Wilson interval, at least 4 questions
  - `api/analytics`: plain accuracy, at least 3 questions
  - `getStudentAIContext.js`: under 60% is weak and 80% or more is strong; the row read is capped at 500 with no ordering, so it can silently drop data
  - `learning_weak.js`: wrong answers in the last 10 papers
- **The app also computes its own mistake map on the phone.** Two screens can therefore disagree about the same student.
- **Chapter is free text everywhere.** A rename in 2026 ("Computerised" to "Computerized") split Accountancy history in two. There is no per-chapter aggregate table and no index for it, so every request recomputes from all attempts.
- **`best_dwell_ms` is never written by paper attempts.** Pace analysis therefore has almost no data.

### 1d. Code base warning
- This worktree (`feat/app-and-web`) is 917 commits behind `origin/main` and 530 ahead of it.
- The live site and the Flutter app use files that exist only on main: `data/revise.js`, `trap_atlas.js`, `mock_swot.js`, `review_chapters.mjs`, `mobi_standing.js` and others.
- **All build work in this plan starts from `origin/main`.**

---

## 2. Syllabus truth: what is wrong and how we fix it

Verified (audit + two-sided check of every HIGH defect): **`intel-1031/syllabus-verified.md`** is the ruling.
- **Reference: CUET 2026 units, with NCERT chapters under them** (owner D200).
- **Sections are now first-class:**
  - Maths A1 + B1/B2
  - CS Section A + B1/B2
  - Accountancy AFS/CAS
- **About 340 live questions in 25 off-syllabus chapters leave every student surface.** They are stored, never served,
  and there is no "older syllabus" shelf (D201).
- **The two-sided check overturned some audit claims:**
  - Political Science keeps "Alternative Centres of Power", "Democratic Upsurge and Coalition Politics", "Recent Issues
    and Challenges" and "Era of One-Party Dominance", because CUET 2026 lists them.
  - World manufacturing stays under Secondary Activities.
- **Duplicates and orphans merge under one name:**
  - Vector Algebra / Vectors
  - Semiconductor / Electronic Devices
  - the d/f block pair
  - the National Income pair
  - Income Determination
  - Financial Management / Business Finance
  - Marketing
  - Dissolution
  - Computerised Accounting
  - the CS duplicates

---

## 3. The spine: one taxonomy with IDs

**What exists.** `data/canonical_syllabus.js` is the source of truth, mirrored to the `units` and `chapters` tables. Questions, attempt snapshots, progress rows and study units all point at chapters by name. That is the root of the duplicate and orphan problems.

**Target (Syllabus v2):**

| Level | ID example | Holds |
|---|---|---|
| Subject | `chemistry` | CUET subject code, paper pattern |
| Unit | `chemistry.u.organic-2` | Display name, CUET unit name, NCERT book part, order |
| Chapter | `chemistry.ch.electrochemistry` | NCERT title, book and chapter number, CUET unit, `in_cuet_2026`, `in_ncert_current`, class 12 only, weight |
| Concept | `chemistry.ch.electrochemistry.c.nernst-equation` | Name, NCERT section, 6-15 per chapter |
| Alias | `"d- and f-Block Elements" -> chemistry.ch.d-f-block` | Every old or variant name ever used |

**Rules:**
- **IDs never change; names can.** A rename becomes a one-line display change plus an alias.
- **Every question gets `chapter_id` and `concept_id`** (new columns, backfilled through the alias map).
  - The old `chapter` text stays for one release as a fallback, then becomes read-only.
  - Old attempt snapshots resolve through the alias map at read time, so history never splits again.
- **Weight per chapter:** past-paper frequency where we have real anchors (`nta_question_index`, 653 rows), otherwise CUET's unit share. "Appeared in N papers" is shown only where the count is real.
- **Concept lists come from the NCERT section headings of each chapter**, written once by agents and checked against the book. They are the unit that cards, questions and the student model share. The three concept-ID namespaces in use today get a crosswalk into this one: generated (`subject::slug`), recovery (`sacrificing_gaining`) and study (`vocabulary_context`).
- **Rival pattern (PW, Testbook):**
  - NCERT chapters for Physics, Chemistry, History, Psychology and Sociology.
  - NTA units for Accountancy, Business Studies, Economics, Political Science, Geography and Biology.
  - English and GAT by topic area.
  - **We do both:** the NCERT chapter is the thing you study, and the CUET unit is the group it sits in. Where NTA gives no units, we use 2-4 plain groups labelled as ours.
  - **No Class 11 chapters in the CUET map.** At most a "builds on Class 11: ..." hint on a concept.

---

## 4. Key cards (the core feature)

### 4a. Card types

| Type | Front | Back | Best for |
|---|---|---|---|
| Term | "Opportunity cost" | One-line definition in NCERT's sense | Economics, Business Studies, Psychology, Sociology |
| Key line | A short NCERT statement with the key word blanked | The word, plus the line and page | Biology, Political Science, History, Geography |
| Formula / reaction | "Nernst equation" or "Reimer-Tiemann: phenol + ?" | The formula, its terms and units / the product | Physics, Chemistry, Maths |
| Fact | "Year the Planning Commission was set up" | 1950, with one line of context | History, Political Science, Economics, GAT |
| Contrast | "Fiscal deficit vs Primary deficit" | The one difference that exams test | All subjects |
| Trap | The wrong option you once picked | Why it is wrong, with a link to the question | Built from your own mistakes and the trap atlas |

**English and GAT get their own decks:**
- **English:** vocabulary (already partly built from WordNet), idioms, one-word substitutions, grammar rules with a wrong/right pair.
- **GAT:**
  - static GK and science facts
  - quant formulas and shortcuts
  - reasoning patterns
  - a monthly current-affairs deck, dated and expiring

### 4b. What every card carries
- the chapter ID and concept ID
- its type
- front and back, short: front at most about 110 characters, back at most about 220
- **source:** NCERT book, chapter, section and page, plus a hash of the source passage
- **importance:** *Must know* (asked in past papers, or a core NCERT definition) or *Good to know*
- a version, a status (draft, published or quarantined) and its family ID (so a card and a question on the same fact are known to be related)

### 4c. How cards are made
**No paid API is needed.** The cards follow the same route as authored wave 1:
1. **Read** the NCERT chapter PDF. We collect the bold terms, boxed definitions, summary points, tables, formulas and dates, plus the concepts behind our questions and the past-paper anchors.
2. **Draft** 25-40 cards per chapter with Claude agents (Opus for sciences, Sonnet where the spec is mechanical), each card tied to its source span.
3. **Check automatically.** Uncertainty means quarantine, never forced publication (AGENTS.md).
   - **Grounding:** the answer is supported by the cited span; numbers, dates and names match the source exactly.
   - **One fact per card,** within length limits, and no duplicate of another card.
   - **The key word is unambiguous** for cloze cards, and the card does not give away its own answer.
   - **No chapter outside CUET 2026 or the current NCERT** (from the spine flags).
   - **Language suits a 16-year-old;** no NCERT paragraph copied wholesale.
4. **Release** as a versioned deck through the existing digest-bound import (`study:prepare`). Published decks are also served as static versioned JSON from the website. Students' devices then fetch card content from the CDN, and only each student's state touches Supabase (the October egress lesson).

**Volume:**
- About 190 chapters across the 13 book subjects at about 30 cards each, plus the English and GAT decks: about 6,000-7,000 cards.
- **Pilot first:** 3 subjects. My pick is Business Studies, Economics and Biology: memory-heavy, commerce first (current product direction), and Biology to prove the science format.

### 4d. How students use them
- **Book order (revise the book):** Subject > Unit > Chapter > deck. Go through cards in NCERT order, or open the one-page chapter sheet (all *Must know* cards, printable). This is "book revision".
- **Daily Revise queue:**
  - Due Key cards (FSRS) and due mistake questions (the existing box schedule) appear in one queue: about 20 items or about 5 minutes, with the cap you choose.
  - Three buttons: *Missed*, *Got it*, *Easy*.
  - New cards come only from chapters you have started or chosen, so the queue never floods.
- **From a mistake:** after a wrong answer, "The line you needed" shows 1-3 cards behind that concept, with one tap to add them to your queue.
- **Last look:** before a mock, or the night before the exam, run through the *Must know* cards of chosen chapters only, without scheduling.
- **In the Mob (later):** a card duel or relay is a natural Mob game format.
- **In Ask Mobi:** Mobi's answers cite the chapter's cards. They are cheap, short, checked context, so replies are more grounded and the model calls cost less.

---

## 5. The student model (chapter state)

**One pure module** (`data/chapter_state.js`, shared rules and fixtures) plus **one table** (`student_chapter_state`, updated when an attempt or a card review is written). This replaces the four weak-chapter rules, and the app reads it from the API instead of computing its own.

**Two axes per student per chapter (and per concept where tagged):**
- **Answering.** Accuracy on server-scored questions, adjusted for difficulty: a hard question right counts more, an easy one wrong counts more. Recent answers weigh more (half-life about 3 weeks). We store an estimate and how sure we are of it, a Wilson-style interval, which `prepos_insights` already uses.
- **Remembering.** The share of the chapter's *Must know* cards with recall chance at or above 90% today (FSRS retrievability). Forgetting therefore shows up even without new answers.

**Level shown to the student** (from Khan's mastery levels, kept honest):

| Level | Rule (first cut, tuned on real data) |
|---|---|
| Not started | Fewer than 5 answers and no cards reviewed |
| Learning | Some evidence, interval still wide |
| Shaky | Answering estimate below 60%, or Remembering below 50% |
| Solid | Answering at least 70% with at least 10 answers, and Remembering at least 70% |
| Mastered | Solid, plus at least 5 hard questions right, sustained over 2 or more weeks |
| Fading | Was Solid or Mastered, but Remembering has dropped or no practice for 3 weeks or more |

- **No percent from a handful of questions.** Below the evidence floor the screen says what it needs ("5 more questions to read this chapter").
- **Every label has a reason line:** "4 of 11 right in the last 2 weeks, mostly on Nernst equation".
- **Marks at stake = chapter weight x (1 - Answering estimate).** This orders "Fix next" and the Compass gap by chapter.
- **Pace and behaviour** (later, once `best_dwell_ms` is written for papers): a plain read after each mock, using the five labels *Careless*, *Rushing*, *Too slow*, *Guessing* and *In control*. This comes from Embibe's idea, with fewer labels and each one shown with its numbers.
- **Cold start with no onboarding quiz**, because you rejected the 5-question app onboarding:
  - the first paper or practice seeds the map
  - chapters can be marked "studied in school" to seed Learning
  - an optional 10-question check per subject is offered from the subject page, never forced

**Population level** (when there are enough students): per-question difficulty from `question_option_stats` and the trap atlas. Until then, authored difficulty plus past-paper anchors. We will not train anything on 12 active students.

---

## 6. Where it shows (refine existing screens, no new tab)

| Surface | What changes |
|---|---|
| Subject page | Unit groups, then chapters, each with level, live question count, card count and marks at stake |
| Review | Leads with weak chapters (your D18 idea), now from the single chapter state; "Fix it" per chapter = 10 questions + its due cards |
| Learn | Book-order decks and chapter sheets beside the existing lessons |
| Today | One Revise line: "14 due, about 5 minutes"; Fading chapters nudge once a week, not daily |
| Paper result | "Fix it" from the 2-3 chapters that cost the most marks; "The line you needed" under each wrong answer |
| Ask Mobi | Reads chapter state and cards; "What should I revise tonight?" answers from the model, free |
| Parents / college view (later) | Chapter map snapshot to share |

**Rules:**
- **Mock-up first** (a real-render preview at 390 and 1440, Night and Day) before any screen is built, as you asked on 15-18 Oct.
- Follow the UI standards, and refine rather than rebuild.
- **Plan split (your call, see section 8):** my default is that cards, the chapter map and Fix it are free. Pro gets custom decks, Mobi's week plan by chapter and the pace coach.

---

## 7. Build order and time (with parallel agents)

| Phase | What | Rough time | Gate |
|---|---|---|---|
| 0. Truth pass | Fix the syllabus map; alias every orphan name; set `in_cuet_2026` / `in_ncert_current` on every chapter and backfill the null `is_cuet_syllabus` flags; take off-syllabus chapters out of mocks and practice; drop placeholder units | About half a day after your decisions in section 8 | Production migration with dry-run and undo; question counts unchanged; mocks draw zero off-syllabus questions |
| 1. Spine | `chapter_id` / `concept_id` columns and backfill; concept lists for the 15 subjects; `chapter_state` module, table and index; the four weak-chapter rules replaced; app reads the API | 1-2 days | Fixtures pin every rule; web and app show the same levels for a test student |
| 2. Cards pilot | Card format in the study tables; pipeline and checks; 3 pilot subjects (about 1,300 cards); unified Revise queue; "The line you needed"; Last look; web and app | 2-3 days, mock-ups first | Zero failed grounding checks published; emulator walk with screenshots; your look at the mock-ups |
| 3. Map and loops | Chapter map on subject pages and Review; Fix it after papers; marks at stake; Mobi grounding | 1-2 days | Device walk against your feedback ledger |
| 4. Scale | Cards for the other 12 subjects; question fill to the floor, in waves you approve | Several days of agent waves | Per-wave quality report |
| 5. Measure | Do students who review a concept's cards answer later questions on it better than before? Recall rates, queue completion, retention | Ongoing | Read honestly; no claims before the numbers |

**Content fill and money:**
- Reaching 40 live questions per core chapter needs roughly 3,500-4,300 new questions after the syllabus fix.
- **The paid pipeline cannot do this inside the USD 50 lifetime ceiling.** The last ledger figure is about USD 13 spent, unreconciled since 7 Oct, and the observed cost is USD 0.014-0.03 per kept question, so the fill would cost about USD 60-130.
- **Options:** agent-authored waves on the subscription (as with wave 1, 475 questions), or a raised ceiling (your call).
- **First, triage the 1,501 pending questions:** some may already fill gaps.

---

## 8. Decisions (answered by the owner 31 Oct: D200-D206 in OWNER-MASTER-LEDGER.md)

Build specs: `intel-1031/KEYCARDS-BUILD-SPEC.md` and `intel-1031/KEYCARDS-CONTENT-SPEC.md`. The completeness critic's 20 points are folded into those specs: evidence states instead of mastery, Must-know-only scheduling with a horizon cap, separate tables from the Learn suite, stream fields, and read-time decay.

Original questions:

1. **Dropped chapters** (Solid State, Polymers, Reproduction in Organisms and others; full list in section 2):
   - (a) take them out of mocks and practice and keep them in an "Older syllabus" shelf, or
   - (b) delete them.
   - My pick is (a).
2. **NCERT wording on cards.** Key-line cards quote at most one short NCERT line with its page, and everything else is paraphrased. My pick is to proceed that way.
3. **Pilot subjects:** Business Studies, Economics, Biology?
4. **Content fill route:** agent-authored waves (no API spend), or raise the USD 50 ceiling?
5. **Free vs Pro:** cards, the chapter map and Fix it free?

---

## 9. Evidence
- **Production counts:** read-only SQL on `isrxrxzjocewrdureyhp`, 31 Oct, run in session 3b7877eb.
- **Syllabus audit:** `syllabus-audit.md`. **Rival scan:** `rival-research.md`. Both are in this session's scratchpad and are copied to `docs/brain/intel-1031/` with this plan.
- **Code survey:** subagent report, summarised in sections 1b-1d.
