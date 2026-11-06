# NTA data audit, 13 October 2026

Read-only research for branch `fix/nta-mode`. Nothing in production or staging was written: every query was a `select` with the service role, no session was created, and no model API was called. The audit script is `scripts/nta-data-audit.mjs`; its raw output is `docs/brain/reports/nta-data-audit-2026-10-13.json`. The data is the production project named in `.env.local`, read on 13 October 2026 (the newest live question was created 7 October 2026).

## Bottom line

1. **Only 662 live questions have a real quality score, and all 662 are in four subjects** (English 173, Accountancy 141, Business Studies 183, Economics 165). The other 4,677 live questions in the 15 NTA-supported subjects (87.6%) have no score at all, and 11 subjects have none. `questions.quality_score` is `0` on every one of the 7,603 live rows; the real scores exist only inside the signed `evidence` JSON of the factory-published rows.
2. **The score is a 0 to 10 integer, given twice.** Every factory record carries a Luna score (`evidence.record.checks.exam_fit.item_quality_score`) and a Gemini score (`checks.independent_evaluation.item_quality_score`). Publication required both to be at least 7, so no live question is below 7. The two judges agree exactly on only 67 of 662 (10%); Gemini scores high (515 nines), Luna low (400 eights, one nine).
3. **The owner's "8 or 8.5" fits the mean of the two judges**, the only reading in which 8.5 exists. At mean 8 or more: **564** questions; at mean 8.5 or more: **340**. Luna alone at 8 or more: 401 (at 8.5: 1). Lower of the two at 8 or more: 389.
4. **Enough for one paper in four subjects, for five or ten in none.** On the repo's current paper pattern and mean 8 or more, one paper can be built in English and two each in Accountancy, Business Studies and Economics; at mean 8.5 or more, none in English and one each in the three commerce subjects. The other 11 subjects have no scored questions, so none.
5. **Even those papers do not match the authentic CUET shape.** In the registered CUET UG 2024 Booklet A, English is 4 passages of 6 questions plus 26 verbal items, and Accountancy, Business Studies and Economics each have 2 case sets of 5. Production has no English passage set of 6 (largest 5; only 5 sets have 3 or more questions) and no case set of any size in the commerce subjects. Against that shape the answer is 0 papers in all four subjects at any threshold.
6. **All 662 evidence records expire between 5 November 2026 22:41 UTC and 6 November 2026 14:57 UTC** (30 days after verification). After that the current evidence rule returns zero eligible questions in every subject, including the four that work today.
7. **The pipeline cannot be re-run on just the unscored questions as it stands.** The factory evaluation needs registered source packs and a calibrated route, which exist only for the same four subjects. Remaining lifetime budget on the ledger is USD 10.04, enough for roughly 1,070 to 1,570 questions at observed per-question cost, against 4,670 readable unscored questions (about USD 30 to 44). A no-API route with Claude agents in batches is feasible and is described in section 5.
8. **The 30-second limit is not at risk.** Measured on production data: database read 0.8 to 1.8 s, evidence checks 6 to 244 ms, paper selection 56 to 295 ms.

## 1. Score fields and their scales

| Field | Where | Scale and meaning | State in production | Owner's "8 / 8.5" maps to |
|---|---|---|---|---|
| `evidence.record.checks.exam_fit.item_quality_score` (Luna, `gpt-6-luna`, high effort) | signed JSON on factory rows | integer 0 to 10 from the exam-fit judge; publication gate is 7 (`MIN_ITEM_QUALITY`, `scripts/pipeline/lib/factoryEvidence.mjs:68`) | 662 live rows; 7: 261, 8: 400, 9: 1 | 8 / 9 (only integers exist) |
| `evidence.record.checks.independent_evaluation.item_quality_score` (Gemini, `gemini-3.8-flash`, medium) | same | integer 0 to 10, independent second judge, also gated at 7 | 662 live rows; 7: 29, 8: 118, 9: 515 | 8 / 9 |
| mean of the two judges (derived in this audit) | computed | 7 to 10 in half points | 7: 17, 7.5: 81, 8: 224, 8.5: 339, 9: 1 | 8 / 8.5 |
| `evidence.record.criteria` craft entries and `exam_fit.craft_scores` (`language_clarity`, `difficulty_suitability`, `distractor_plausibility`) | same | integers 1 to 10, craft detail behind the overall | 662 rows; craft mean at 8.5 or more: 2 rows | not a usable gate |
| `questions.quality_score` | column, `NUMERIC(8,4)`, default 0 | schema allows any value; consumers treat it as 0 to 1 (`data/answer_integrity.js:393` penalises below 0.8; `data/nta_question_selector.js:416` and `:462` use a 0.12 weight and a 0.6 floor) | `0` on all 7,603 live rows; the publisher hard-codes 0 (`scripts/pipeline/lib/publish.mjs:191`) | 0.80 / 0.85 if ever filled with score divided by 10 |
| `question_scores.quality_score` | table, 8,082 rows | community-ranking table | 0 on every row (also `rank_score` 0) | 0.80 / 0.85 |
| `questions.ai_score`, `ai_moderation_reviews.ai_score` | column and table | 0 to 1 weighted moderation score (`src/lib/moderation/tiering.js`) | 886 live rows, all Accountancy, all exactly 0.85; all 1,913 review rows (957 questions, 22 April 2026) are `model_used = 'mock'`, tier B | 0.80 / 0.85, but **0.85 is the mock constant**: a rule "ai_score at least 0.85" would pass those 886 rows with no real review |
| moderation `score` (`src/lib/moderation/ai.js`) and legacy validator `score`, `exam_quality`, `distractor_quality`, `conceptual_depth` (`scripts/pipeline/lib/llm.mjs`, accept only if all at least 7) | model output | float 0 to 10 | never persisted | 8 / 8.5 |
| `questions.validation_confidence`, `validated_at`, `is_cuet_syllabus`, `is_ncert_relevant` | written only by `scripts/pipeline/validate-existing.mjs` | 0 to 1 classification confidence | null on every live row: the script has never been applied | 0.80 / 0.85, no data |
| `questions.score`, `upvotes`, `downvotes` | columns | net community votes, integer | values from -3 to 4; the practice reader drops rows below -2 (4 live rows: 2 English, 2 Biology) | not a quality score |
| `quality_band` ('strong'), `ai_tier` ('A'), `verification_state` ('verified'), `exploration_state` ('active') | columns | labels | fixed strings written by every publisher; 8,104 rows 'strong', 8,119 tier 'A' | none; the selector adds ranking points for them (`scoreMetadata`), so its internal 0 to 1 value is a ranking heuristic, not quality |
| `momentum_score`, `exposure_*` | columns | engagement | 0 everywhere | none |
| CUET-fit rubric (five criteria 0 to 3, derived overall out of 10, pass at 7) and V716 composite (6 for practice, 7 for NTA) | `data/cuet_fit_rubric.mjs` and `docs/brain/GENERATOR-OPERATING-RULES-V716.md` in the main checkout `mockmob copy\mockmob copy`; not on this branch or in production | 0 to 10 | no production row carries it; V717 qualification stopped unqualified on 10 October | 8 / 8.5 |

Two consequences for the selector work. Any filter on `quality_score` or `ai_score` today selects nothing real. If scores are ever written to `quality_score`, write them divided by 10, or `answer_integrity` and the tier logic will misread them. The 7 / 8 / 9 gradations are one model call each, not measured item statistics, and QUALITY.md states that model agreement is not proof of correctness: the score is a CUET-fit label, and the mandatory correctness gates are separate.

## 2. Production inventory

Production holds 9,908 question rows: 7,603 live, 1,237 pending (draft or held), 1,068 rejected and soft-deleted. The live rows span 41 subjects; the 15 NTA-supported subjects hold 5,339. Subjects use internal ids (`general_test` is stored as `gat`).

### 2.1 Totals, scores and thresholds (live questions)

"Eligible now" is what `readablePracticeQuestions({ requireEvidence: true })` returns, using the signing key from `.env.local` and the source registry and calibration manifest in this branch (all 662 scored rows pass). Four further English rows with evidence are pending and withheld; four open key disputes exist. Threshold columns are counts among scored questions.

| Subject | Live | With factory record (scored) | Unscored | Scored, unreadable/ineligible | Eligible now | Mean >=7.5 | Mean >=8 | Mean >=8.5 | Luna >=8 | Gemini >=8 | Min of both >=8 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| english | 277 | 173 | 104 | 0 | 173 | 168 | 152 | 81 | 98 | 166 | 96 |
| general test | 157 | 0 | 157 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| accountancy | 1490 | 141 | 1349 | 0 | 141 | 139 | 128 | 85 | 91 | 139 | 91 |
| business studies | 438 | 183 | 255 | 0 | 183 | 177 | 148 | 92 | 112 | 170 | 105 |
| economics | 486 | 165 | 321 | 0 | 165 | 161 | 136 | 82 | 100 | 158 | 97 |
| mathematics | 285 | 0 | 285 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| physics | 320 | 0 | 320 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| chemistry | 300 | 0 | 300 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| biology | 379 | 0 | 379 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| history | 197 | 0 | 197 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| political science | 198 | 0 | 198 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| geography | 182 | 0 | 182 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| psychology | 87 | 0 | 87 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| sociology | 212 | 0 | 212 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| computer science | 331 | 0 | 331 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Total (15 subjects)** | 5339 | 662 | 4677 | 0 | 662 | 645 | 564 | 340 | 401 | 633 | 389 |

Why the rest are unscored. The 4,677 unscored live questions (6,941 across all 41 subjects) were published in April (6,455) and May (486) 2026 by the legacy generator and moderation path, before the evidence factory existed (7 October 2026). That path (a) kept only the validator's accept or reject decision and dropped its 0 to 10 numbers, (b) wrote fixed labels (`quality_band` 'strong', `ai_tier` 'A', `verification_state` 'verified'), (c) ran its moderation worker only once, in mock mode (957 questions, constant 0.85), and (d) never ran the bank-wide re-validation (`validate-existing.mjs`; `validated_at` is null on all rows). The evidence factory scored only its own 900 jobs (662 published, 238 quarantined, all four subjects); it is paused (`question_factory_control.paused = true`, `publication_enabled = false`). Staging holds the same 666 evidence rows (535 live) and no other scored questions.

Readable and gate-passing counts. 5,332 of the 5,339 live questions in the 15 subjects pass the practice reader's structural filter (the 7 that fail are 3 Accountancy rows whose explanation contradicts the key and 4 rows voted below -2), and 5,176 pass the NTA content gate. The rest fail for malformed text (17 Mathematics, 1 Physics), orphan passage questions (134 in total: 58 English, 11 History, 10 Business Studies, 10 Psychology, and smaller counts elsewhere; these are reading-style questions with no passage text), generic assertion-reason items with no English context (9 English) and invalid options (2 Economics). Of the 662 scored rows, 14 fail the selector's content gate (12 orphan passage, 2 invalid options).

### 2.2 Question types (live)

Types come from `question_type` where present (column or tag; the factory sets it) and otherwise from body wording (heuristic on "Assertion ... Reason", "Match List-I", "Statement I", "arrange"; used for 3,869 of the 5,339 live rows in these subjects). Read heuristic counts as estimates.

| Subject | Live | Single MCQ (direct or one-step) | Assertion-reason | Statement based | Match the following | Sequence / para jumble | Numerical | Case based (stand-alone) | Vocabulary / language | Reading-type stand-alone | Passage-set questions |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| english | 277 | 31 | 22 | 1 | 43 | 38 | 0 | 0 | 86 | 13 | 43 |
| general test | 157 | 110 | 25 | 1 | 21 | 0 | 0 | 0 | 0 | 0 | 0 |
| accountancy | 1490 | 1238 | 74 | 30 | 81 | 23 | 17 | 27 | 0 | 0 | 0 |
| business studies | 438 | 193 | 75 | 47 | 55 | 32 | 0 | 36 | 0 | 0 | 0 |
| economics | 486 | 231 | 61 | 59 | 54 | 20 | 26 | 35 | 0 | 0 | 0 |
| mathematics | 285 | 192 | 46 | 15 | 28 | 0 | 2 | 2 | 0 | 0 | 0 |
| physics | 320 | 185 | 81 | 34 | 19 | 0 | 0 | 1 | 0 | 0 | 0 |
| chemistry | 300 | 167 | 60 | 50 | 23 | 0 | 0 | 0 | 0 | 0 | 0 |
| biology | 379 | 246 | 67 | 30 | 34 | 0 | 1 | 1 | 0 | 0 | 0 |
| history | 197 | 131 | 40 | 2 | 24 | 0 | 0 | 0 | 0 | 0 | 0 |
| political science | 198 | 119 | 31 | 20 | 26 | 0 | 0 | 1 | 0 | 1 | 0 |
| geography | 182 | 127 | 29 | 2 | 24 | 0 | 0 | 0 | 0 | 0 | 0 |
| psychology | 87 | 55 | 20 | 9 | 2 | 0 | 0 | 1 | 0 | 0 | 0 |
| sociology | 212 | 114 | 32 | 41 | 24 | 0 | 0 | 1 | 0 | 0 | 0 |
| computer science | 331 | 190 | 61 | 45 | 35 | 0 | 0 | 0 | 0 | 0 | 0 |

Scored questions only:

| Subject | Scored | Single MCQ | Assertion-reason | Statement | Match | Sequence | Numerical | Case | Vocabulary | Reading-type | Passage |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| english | 173 | 0 | 0 | 0 | 28 | 27 | 0 | 0 | 86 | 0 | 32 |
| accountancy | 141 | 32 | 0 | 22 | 24 | 20 | 16 | 27 | 0 | 0 | 0 |
| business studies | 183 | 45 | 0 | 32 | 39 | 32 | 0 | 35 | 0 | 0 | 0 |
| economics | 165 | 36 | 0 | 23 | 26 | 20 | 25 | 35 | 0 | 0 | 0 |

The scored pool has no assertion-reason questions (the legacy bank has 74 in Accountancy alone). The legacy bank is mostly single MCQ (Accountancy: 1,238 of 1,490, 83%). Passage and case sets:

| Subject | Live passage sets (sizes) | Live questions in sets | Eligible scored sets (sizes) | Needed per authentic paper |
|---|---|---:|---|---|
| english | 18 (3x1, 9x2, 3x3, 2x4, 1x5) | 43 | 13 (2x1, 6x2, 3x3, 1x4, 1x5) | 4 sets x 6 |
| accountancy | 0 (none) | 0 | 0 (none) | 2 case sets x 5 |
| business studies | 0 (none) | 0 | 0 (none) | 2 case sets x 5 |
| economics | 0 (none) | 0 | 0 (none) | 2 case sets x 5 |

English also has 18 live passage groups, but 12 of them have 1 or 2 children. Every commerce subject stores its case questions stand-alone (27 Accountancy, 36 Business Studies, 35 Economics live), so a case set cannot be assembled from them.

### 2.3 Syllabus coverage against the official map

The map is `data/canonical_syllabus.js` (CUET UG 2026 PDFs in `data/CUET 2026`; registry version `nta-cuet-ug-2026@2026-09-02`, provisional for 2027). All live questions in the 15 subjects carry a chapter that exists in the map, except 3 Economics rows labelled "National Income and Related Aggregates" (the map says "National Income & Related Aggregates"). Chapter detail for the four scored subjects is in the appendix.

| Subject | Units | Chapters (official map) | Chapters with live questions | Chapters with a scored+eligible question | Chapters with mean >=8 | Chapters with none at mean >=8 |
|---|---:|---:|---:|---:|---:|---|
| english | 2 | 7 | 7 | 7 | 7 | - |
| general test | 6 | 9 | 9 | 0 | 0 | all |
| accountancy | 6 | 16 | 16 | 13 | 13 | Dissolution of Partnership; Financial Statements of Company; Computerized Accounting System |
| business studies | 13 | 13 | 13 | 12 | 12 | Entrepreneurship Development |
| economics | 3 | 18 | 18 | 17 | 17 | Infrastructure |
| mathematics | 7 | 18 | 18 | 0 | 0 | all |
| physics | 10 | 15 | 15 | 0 | 0 | all |
| chemistry | 11 | 16 | 16 | 0 | 0 | all |
| biology | 5 | 15 | 15 | 0 | 0 | all |
| history | 3 | 14 | 14 | 0 | 0 | all |
| political science | 2 | 19 | 19 | 0 | 0 | all |
| geography | 7 | 15 | 15 | 0 | 0 | all |
| psychology | 8 | 9 | 9 | 0 | 0 | all |
| sociology | 2 | 14 | 14 | 0 | 0 | all |
| computer science | 3 | 23 | 23 | 0 | 0 | all |

Gaps in scored coverage. Accountancy has no scored question in Dissolution of Partnership (13 live), Financial Statements of Company (14 live) or Computerized Accounting System (128 live). Business Studies has none in Entrepreneurship Development (12 live; not an official CUET unit, filed as "Existing coverage"). Economics has none in Infrastructure (13 live). The official sections of Mathematics (A1, B1, B2) and Computer Science (A, B1, B2) are flattened into one list in the canonical map, and no unit weighting is stored anywhere for any subject.

### 2.4 Difficulty labels

Every live question has an easy, medium or hard label written by the authoring model; none is measured from candidate responses. The V716 rule in the main checkout asks NTA to prefer medium and easy over hard.

| Subject | Live easy / medium / hard | Scored easy / medium / hard |
|---|---|---|
| english | 114 / 120 / 43 | 69 / 87 / 17 |
| general test | 81 / 35 / 41 | - |
| accountancy | 788 / 602 / 100 | 56 / 64 / 21 |
| business studies | 114 / 176 / 148 | 69 / 85 / 29 |
| economics | 197 / 188 / 101 | 59 / 76 / 30 |
| mathematics | 139 / 84 / 62 | - |
| physics | 132 / 102 / 86 | - |
| chemistry | 71 / 129 / 100 | - |
| biology | 161 / 114 / 104 | - |
| history | 98 / 50 / 49 | - |
| political science | 121 / 58 / 19 | - |
| geography | 120 / 35 / 27 | - |
| psychology | 33 / 35 / 19 | - |
| sociology | 107 / 82 / 23 | - |
| computer science | 125 / 98 / 108 | - |

## 3. Can N full NTA papers be built without repeats?

Method. The real `selectNtaQuestionSet` from this branch, run up to 10 times in sequence on a pool, removing each paper's questions before the next, with `excludeRepeatedFamilies` applied. A paper counts only if it has 50 questions and the repo's own pattern reports no shortfall (`data/nta_paper_pattern.js`). `+` means the cap of 10 was reached. Each cell is pool size / papers. Columns 1 to 3 use only scored questions. Columns 4 to 6 are hypotheticals: all readable unscored questions that pass the selector's content gate, at the stated share reaching 8 or more (a deterministic hash subsample; the factory's own live yield is 85% at mean 8 or more and 61% at Luna 8 or more), plus scored questions at mean 8 or more.

| Subject | Scored (any) (pool / papers) | Mean >=8 (pool / papers) | Mean >=8.5 (pool / papers) | If 60% of unscored reach 8 (pool / papers) | If 40% reach 8 (pool / papers) | If 100% reach 8 (ceiling) (pool / papers) |
|---|---:|---:|---:|---:|---:|---:|
| english | 173 / 1 | 152 / 1 | 81 / 0 | 213 / 1 | 197 / 1 | 275 / 1 |
| general test | 0 / 0 | 0 / 0 | 0 / 0 | 95 / 1 | 66 / 1 | 157 / 3 |
| accountancy | 141 / 2 | 128 / 2 | 85 / 1 | 973 / 10+ | 713 / 10+ | 1487 / 10+ |
| business studies | 183 / 3 | 148 / 2 | 92 / 1 | 305 / 5 | 243 / 4 | 438 / 8 |
| economics | 165 / 3 | 136 / 2 | 82 / 1 | 331 / 6 | 262 / 5 | 486 / 9 |
| mathematics | 0 / 0 | 0 / 0 | 0 / 0 | 170 / 3 | 117 / 2 | 285 / 5 |
| physics | 0 / 0 | 0 / 0 | 0 / 0 | 197 / 3 | 134 / 2 | 320 / 6 |
| chemistry | 0 / 0 | 0 / 0 | 0 / 0 | 191 / 3 | 138 / 2 | 300 / 5 |
| biology | 0 / 0 | 0 / 0 | 0 / 0 | 231 / 4 | 152 / 3 | 377 / 7 |
| history | 0 / 0 | 0 / 0 | 0 / 0 | 126 / 2 | 92 / 1 | 197 / 3 |
| political science | 0 / 0 | 0 / 0 | 0 / 0 | 120 / 2 | 77 / 1 | 198 / 3 |
| geography | 0 / 0 | 0 / 0 | 0 / 0 | 105 / 2 | 65 / 1 | 182 / 3 |
| psychology | 0 / 0 | 0 / 0 | 0 / 0 | 54 / 0 | 39 / 0 | 87 / 1 |
| sociology | 0 / 0 | 0 / 0 | 0 / 0 | 122 / 2 | 80 / 1 | 212 / 4 |
| computer science | 0 / 0 | 0 / 0 | 0 / 0 | 199 / 3 | 137 / 2 | 331 / 6 |

Plain answers per subject, scored questions only, at the owner's floor (mean 8 or more) and strict (8.5 or more). "Current" is the repo's pattern; "authentic" is the 2024 booklet shape described below.

| Subject | N=1 (50 questions) | N=5 (250) | N=10 (500) | What is missing |
|---|---|---|---|---|
| English | current: yes at 8 (1 paper), no at 8.5; authentic: no | no | no | 152 qualify at 8 and 81 at 8.5. No passage set of 6; sets of 3 or more: 5. Verbal chapters at mean 8: Para Jumbles 26, Match 22, Vocabulary 52, Correct Word Usage 23, enough for about 3 authentic papers. Needs 4, 20, 40 complete 6-question passage sets for N=1, 5, 10 |
| Accountancy | current: yes (2 papers at 8, 1 at 8.5); authentic: no | no (128 / 85 qualify; 250 needed) | no | 2 case sets of 5 per paper; 3 chapters with no scored question; Computerized Accounting System has 128 live, 0 scored |
| Business Studies | current: yes (2 at 8, 1 at 8.5); authentic: no | no (148 / 92) | no | 2 case sets of 5 per paper; Entrepreneurship Development unscored |
| Economics | current: yes (2 at 8, 1 at 8.5); authentic: no | no (136 / 82) | no | 2 case sets of 5 per paper; Infrastructure unscored |
| General Test, Mathematics, Physics, Chemistry, Biology, History, Political Science, Geography, Psychology, Sociology, Computer Science | no | no | no | no score at all; no authenticated paper or registered source pack; live banks of 87 (Psychology) to 379 (Biology) questions |

Ceiling if every readable unscored question reached the bar (last column of the table above): Accountancy 10 or more, Economics 9, Business Studies 8, Biology 7, Physics 6, Computer Science 6, Mathematics 5, Chemistry 5, Sociology 4, three each in General Test, History, Political Science and Geography, one each in English and Psychology. A perfect scoring pass would still leave English at 1 paper (passage sets), and 10 papers out of reach in 14 of 15 subjects. If only 40% of the unscored bank reached 8, the legacy subjects fall to 1 to 3 papers (Psychology 0).

### What the real CUET pattern looks like in the data

`data/source_registry.json` registers authenticated CUET UG 2024 Booklet A papers, with final keys, for four subjects only: English, Accountancy, Business Studies and Economics. Its `exam_specs` also exist only for these four (`pattern_version cuet-2024-authenticated-bookA-v1`). From them:

- English, 50 questions: Q1 to 16 verbal, Q17 to 22 passage 1, Q23 to 28 passage 2, Q29 to 34 passage 3, Q35 to 40 passage 4 (six questions each), Q41 to 50 verbal. The 26 verbal items are 6 rearrange, 6 fill the blank, 6 match and 8 synonym or antonym.
- Accountancy and Business Studies, 50 questions each: two complete case sets of five (Q41 to 45 and Q46 to 50). Economics: two complete case sets of five (Q28 to 32 and Q33 to 37). These are the complete sets the registry kept; sets with dropped items are not listed.

The current `nta_paper_pattern.js` uses 2 to 4 English passage sets of 3 or more questions (target 15 passage questions) and treats case or passage sets in domain subjects as optional (at most 2 sets, 10 questions). It therefore reports papers that do not resemble the 2024 booklet. Nothing in the repo describes the exact pattern of the other 11 subjects (no authenticated paper, no unit weighting); only their chapters, from the 2026 syllabus, are known. This is one year and one booklet code, and the registry notes that historical timing and attempt rules do not establish 2027 rules.

### Timing against the 30-second limit

Measured on production rows from this machine: reading a subject's live rows with the production query 0.8 s (Physics, 320 rows) to 1.8 s (English, 279 rows with heavy evidence JSON; Accountancy, 1,490 rows, 1.7 s); answer-integrity plus evidence eligibility 6 to 244 ms per subject; selection of the first paper 56 to 295 ms even on the largest legacy pools. End to end about 2 to 3 seconds, an order of magnitude inside 30 s. The earlier inventory timeout came from re-reading the 4.85 MB registry for every question; the snapshot fix (52de7fe) removed it.

## 4. Expiry risk

Every record's `expires_at` is `verified_at` plus 30 days. `evaluateEvidence` (`data/content_evidence.js:36`) then reports `stale_verification` and the question leaves the NTA pool. Earliest expiry 5 November 2026 22:41 UTC, latest 6 November 2026 14:57 UTC, all four subjects. The signature covers `expires_at`, so extending it needs either a paid re-verification or an owner-approved re-signing with the signing key; neither has been done, and the pipeline policy says only backend verification jobs create records. This is an owner decision with a 23-day clock.

## 5. Scoring the unscored questions

### How scoring works today

1. **Evidence factory** (`scripts/pipeline/factory.mjs`, `lib/factoryEvidence.mjs`, `lib/factoryCore.mjs`). A candidate is authored by Luna from registered source packs, then passes dedupe, schema, a Luna blind solve (high effort), a Gemini independent evaluation (medium), alternatives, source support, syllabus mapping, an explanation audit, presentation, exam fit (the 0 to 10 score) and, where needed, numeric or passage checks. Each check records its score and the record is signed with `CUET_EVIDENCE_SIGNING_KEY` (HMAC). Publication copies the signed record into `questions.evidence` and fixes `quality_score` at 0.
2. **Legacy generator.** `normalizeValidationResult` in `scripts/pipeline/lib/llm.mjs` produces 0 to 10 numbers and accepts only when all are at least 7, then discards them.
3. **Moderation worker** (`src/app/api/internal/moderation/process`). Tier, 0 to 10 `score`, 0 to 1 `ai_score`; in production it ran once, in mock mode.
4. **Bank re-validation** `scripts/pipeline/validate-existing.mjs`. Classification confidence only; never run. It calls Gemini through the SDK with no budget ledger, so it must not be run as is, and its `apply` mode soft-deletes rows and re-shuffles options.
5. **Main checkout only** (unmerged, not production). V716 and V717 CUET-fit scorecards; `reassessApprovals.mjs` re-judges factory approvals only (718 questions, USD 6.76 settled).

### Can it be re-run on just the unscored questions?

Not as it stands. The factory evaluation is built around factory jobs with source references: its mandatory `source_support` check needs registered, hash-verified source excerpts, and the registry has source packs for English, Accountancy, Business Studies and Economics only (eight packs). Legacy rows carry no `source_refs`, so they would quarantine at `source_support`. The one tool that touches existing rows without sources, `validate-existing.mjs`, runs outside the ledger. A score-only tool would be new work: select unscored live rows (read-only), send them through `BudgetLedger` and the existing transport (as `reassessApprovals.mjs` does) for a Luna blind solve plus a Gemini independent evaluation, and store the result outside the signed evidence, in a new table created by a saved migration the owner approves first.

### Cost under the budget ledger

The ledger file is `data/pipeline-budget.sqlite` in the main checkout (this worktree has none). A read-only copy was queried; its last request is 10 October 2026 05:58 UTC and its totals match STATUS: limit USD 50.00; settled USD 39.139769 across 14,993 requests; 65 unresolved holds USD 0.821324; committed USD 39.961093; **remaining USD 10.038907**. Spend by purpose: calibration USD 20.27, candidate generation USD 12.10 (1,618 candidates), reassessment USD 6.76 (718 questions).

Observed unit cost from receipts: reassessment (the closest thing to scoring an existing question) is about **USD 0.0094 per question** (USD 6.765 for 718). Summing per-request averages for candidate-time evaluation (Gemini independent 0.0043, Luna blind solve 0.0015, explanation audit 0.0006) gives about **USD 0.0064**. The 4,670 readable unscored questions in the 15 subjects would cost about USD 30 to 44 (the 2,646 in the 11 subjects with no scores: USD 17 to 25), against USD 10.04 remaining. That buys roughly 1,070 to 1,570 questions at realtime prices, perhaps double with native batch pricing if receipts confirm it. The USD 50 ceiling is the owner's; raising it is the owner's call. V717 qualification is closed unqualified, so no scorecard version is cleared for new paid use, and any new run needs the owner's preregistration and approval.

### Alternative: Claude agents in batches, no API cost

Feasible, and cheap in dollars. Suggested shape (not built): a read-only export of unscored live rows, 20 to 25 per batch (about 190 to 235 batches for 4,670), each agent scoring against a fixed rubric (blind solve with the key hidden, syllabus and chapter fit, CUET format and difficulty fit, distractor quality, clarity) and returning a half-point score plus its blind key. About 500 tokens per question, roughly 3 million tokens including the rubric. To make it comparable to the two-judge mean, run two independent passes, one per model tier, and take the mean; a blind-key mismatch or a defect flag excludes the question whatever its score. Limits: agent scoring is a judge-dependent label, not evidence, and cannot create a signed `evidence` record (that would need the signing key and breaks the "only backend verification jobs create records" policy). It would have to live in a separate score table, the NTA rule would read it explicitly, and the owner would have to accept it as qualifying. It also does not supply the missing 6-question passage sets or 5-question case sets; those need authoring.

## 6. Open points for the owner and the next builder

- Pick the score definition (the mean of the two judges is the only one with an 8.5) and the floor (8: 564 questions; 8.5: 340). Say whether NTA keeps requiring a valid, signed, unexpired record.
- Decide before 5 November whether to renew or re-sign the 662 records.
- Decide the pattern. The 2024 booklet shape (4 x 6 English passages; 2 x 5 case sets) needs newly authored sets, none of which exist. The current looser pattern can run now in four subjects, once or twice each.
- Decide how to score the legacy bank: the ledger route (USD 10 reaches about a quarter of it), the Claude-agent route, or neither.
- Data defects this audit found: 14 scored rows fail the selector's own content gate; 3 Economics rows use a chapter label that is not in the map; 134 live questions are orphan passage questions with no passage text.
- Not verified here: academic correctness of any question (the score is a fit label, not truth), real student sessions, the 2025 and 2026 paper structures, the official pattern of the other 11 subjects, and whether the ledger copy has moved since 10 October.

## Reproduce

```
node --use-system-ca scripts/nta-data-audit.mjs <out.json>
```

It needs `.env.local` (service role and the evidence signing key; it deliberately does not load `MOCK_AI=true`) and takes about 35 seconds.

## Appendix: chapter detail, scored subjects

Counts are scored questions per official chapter.


**english**

| Unit | Chapter | Live | Scored | Mean >=8 | Mean >=8.5 |
|---|---|---:|---:|---:|---:|
| Reading Comprehension | Factual Passage | 49 | 8 | 6 | 5 |
| Reading Comprehension | Narrative Passage | 17 | 9 | 9 | 4 |
| Reading Comprehension | Literary Passage | 30 | 15 | 14 | 8 |
| Verbal Ability | Para Jumbles | 40 | 27 | 26 | 6 |
| Verbal Ability | Match the Following | 43 | 28 | 22 | 19 |
| Verbal Ability | Vocabulary | 63 | 58 | 52 | 23 |
| Verbal Ability | Correct Word Usage | 35 | 28 | 23 | 16 |

**accountancy**

| Unit | Chapter | Live | Scored | Mean >=8 | Mean >=8.5 |
|---|---|---:|---:|---:|---:|
| Accounting for Partnership | Partnership Fundamentals | 156 | 11 | 8 | 4 |
| Accounting for Partnership | Profit & Loss Appropriation Account | 40 | 9 | 7 | 6 |
| Reconstitution of a Partnership firm | Change in Profit Sharing Ratio | 30 | 10 | 10 | 7 |
| Reconstitution of a Partnership firm | Goodwill Valuation | 33 | 5 | 4 | 2 |
| Reconstitution of a Partnership firm | Admission of Partner | 189 | 16 | 14 | 11 |
| Reconstitution of a Partnership firm | Retirement & Death of Partner | 24 | 10 | 9 | 7 |
| Dissolution of Partnership Firm | Dissolution of Partnership | 13 | 0 | 0 | 0 |
| Dissolution of Partnership Firm | Dissolution of Partnership Firm | 33 | 8 | 8 | 5 |
| Company Accounts: Accounting for Share and Debenture Capital | Share Capital | 234 | 25 | 23 | 16 |
| Company Accounts: Accounting for Share and Debenture Capital | Debentures | 222 | 7 | 6 | 4 |
| Analysis of Financial Statements | Financial Statements of Company | 14 | 0 | 0 | 0 |
| Analysis of Financial Statements | Analysis of Financial Statements | 144 | 3 | 2 | 1 |
| Analysis of Financial Statements | Comparative & Common Size Statements | 38 | 15 | 15 | 9 |
| Analysis of Financial Statements | Accounting Ratios | 33 | 10 | 10 | 7 |
| Analysis of Financial Statements | Cash Flow Statement | 159 | 12 | 12 | 6 |
| Computerized Accounting System | Computerized Accounting System | 128 | 0 | 0 | 0 |

**business studies**

| Unit | Chapter | Live | Scored | Mean >=8 | Mean >=8.5 |
|---|---|---:|---:|---:|---:|
| Nature and Significance of Management | Nature & Significance of Management | 106 | 13 | 12 | 7 |
| Principles of Management | Principles of Management | 46 | 14 | 12 | 7 |
| Business Environment | Business Environment | 27 | 17 | 13 | 12 |
| Planning | Planning | 20 | 11 | 9 | 4 |
| Organising | Organising | 20 | 11 | 10 | 7 |
| Staffing | Staffing | 35 | 18 | 16 | 10 |
| Directing | Directing | 34 | 13 | 10 | 5 |
| Controlling | Controlling | 28 | 17 | 17 | 10 |
| Business Finance | Financial Management | 29 | 17 | 14 | 9 |
| Financial Markets | Financial Markets | 28 | 22 | 10 | 7 |
| Marketing | Marketing Management | 22 | 15 | 12 | 7 |
| Consumer Protection | Consumer Protection | 31 | 15 | 13 | 7 |
| Existing Business Studies Coverage | Entrepreneurship Development | 12 | 0 | 0 | 0 |

**economics**

| Unit | Chapter | Live | Scored | Mean >=8 | Mean >=8.5 |
|---|---|---:|---:|---:|---:|
| Introductory Microeconomics | Introduction & Theory of Consumer Behaviour | 55 | 8 | 8 | 5 |
| Introductory Microeconomics | Production & Costs | 44 | 8 | 8 | 7 |
| Introductory Microeconomics | Theory of Firms under Perfect Competition | 20 | 8 | 8 | 5 |
| Introductory Microeconomics | Market Equilibrium & Simple Applications | 21 | 8 | 6 | 3 |
| Introductory Macroeconomics | National Income & Related Aggregates | 13 | 7 | 7 | 5 |
| Introductory Macroeconomics | Money & Banking | 32 | 7 | 6 | 5 |
| Introductory Macroeconomics | Income Determination | 24 | 9 | 8 | 7 |
| Introductory Macroeconomics | Government Budget & the Economy | 32 | 9 | 9 | 7 |
| Introductory Macroeconomics | Balance of Payments | 29 | 11 | 10 | 6 |
| Indian Economic Development | Indian Economy on the Eve of Independence | 36 | 8 | 5 | 2 |
| Indian Economic Development | Indian Economic Development 1950â€“1990 | 22 | 11 | 10 | 5 |
| Indian Economic Development | Economic Reforms Since 1991 | 19 | 8 | 5 | 1 |
| Indian Economic Development | Human Capital Formation | 22 | 13 | 8 | 4 |
| Indian Economic Development | Rural Development | 23 | 13 | 9 | 4 |
| Indian Economic Development | Employment | 25 | 12 | 10 | 4 |
| Indian Economic Development | Infrastructure | 13 | 0 | 0 | 0 |
| Indian Economic Development | Environment & Sustainable Development | 27 | 12 | 7 | 6 |
| Indian Economic Development | Development Experiences of India | 26 | 13 | 12 | 6 |
