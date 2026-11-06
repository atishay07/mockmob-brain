# NTA pattern spec: CUET UG paper blueprints (15 subjects)

Written 13 Oct 2026 on `fix/nta-mode`. This is the reference for the NTA-mode engine: what a real
CUET UG paper looks like for each subject MockMob supports, how sure we are, and where it came from.
The machine-readable form is `data/nta_blueprints/<subject>.json`. Shape: `_schema.json`. Type
detection: `_types.json`. Sources: `_sources.json`. Consistency test: `data/tests/nta_blueprints.test.mjs`
(`node --test data/tests/nta_blueprints.test.mjs`, 18 tests).

This spec covers only the paper pattern. Which questions are allowed into NTA mode (the score
threshold) is decided elsewhere.

## 1. Official rules (certain)

From the NTA CUET(UG)-2026 Information Bulletin (S1: para 4, 2.3, 2.4, 12.1). The 2025 bulletin (S2)
has the same scheme. It applies to every subject.

| Rule | Value |
|---|---|
| Questions per paper | 50, **all compulsory** (no internal choice since 2025) |
| Duration | 60 minutes per paper (PwBD: +20 min per hour) |
| Format | Objective MCQ, 4 options, one correct, CBT |
| Marking | +5 correct, -1 incorrect, 0 unanswered; maximum 250 |
| Key anomalies | More than one correct option: +5 only to those who marked a correct one. No correct option or dropped question: +5 to everyone |
| Medium | Bilingual (English plus the chosen language); English prevails |

**Sectioned papers.** Mathematics/Applied Mathematics (319) and Computer Science/Informatics Practices
(308) have a common Section A (15 questions) plus a choice of B1 or B2 (35 questions). The candidate
answers 50. Source: the 2026 syllabi (S3) and the 2025 Mathematics paper instructions (S4): "Section A
consist of 15 questions (Q. 1 to Q. 15), all are compulsory", B1 Core Q16-50 and B2 Applied Q16-50
in the candidate's view. The 2025 Informatics Practices paper has Section A at Q1-15 and B2 at Q16-50.

## 2. What real papers look like (2025 papers, one shift per subject)

I read every question of 11 real CUET UG 2025 papers (Oswaal solved reprints, S4): English,
Mathematics/Applied Mathematics, Physics, Chemistry, Biology, Economics, Accountancy, Business
Studies, History, Geography and Informatics Practices (Section A + B2). I classified each question by
chapter and type. Counts are in each blueprint's `evidence.observed`. I could not find full 2025 or 2026
papers for General Test, Political Science, Psychology, Sociology or Computer Science (B1); those
blueprints rest on shift reports and the common template below, and are marked low confidence.

Findings that hold across the papers:

1. **Domain papers share one template.** Most theory papers have about 25 single MCQs, 5 match List-I
   with List-II, 5 arrange-in-sequence, 5 multi-statement ("(A), (B) and (C) only") items, then **two
   passage sets of 5 questions at Q41-45 and Q46-50**. Two sets at the end appeared in Chemistry, Biology,
   Economics, History, Geography and Business Studies (6 of 9 domain papers). Physics, Accountancy,
   Mathematics and Informatics Practices had no sets.
2. **Questions are not grouped by chapter.** Q1-40 jump between chapters and units, and the special types
   are scattered. Each passage set stays inside one chapter (for example Bt toxins, immunity,
   Vijayanagara, Rowlatt Satyagraha, price ceilings, Bharmaur case study).
3. **Assertion-reason did not appear in any 2025 paper read.** 2026 shift reports mention it for History,
   Political Science and the General Test, so the blueprints allow 0-2 (0-3 for Political Science),
   with a target of 0.
4. **Coverage is broad and fairly even.** Chemistry was almost exactly 5 per unit. Biology was 9-11 per
   unit. Physics was 3-8 per unit. Every syllabus unit appeared except IED in Economics (0 in that shift)
   and Computerised Accounting (0; it is "Optional to Unit V" in the syllabus).
5. **English opens with its passages.** 2025: three passages of 4 questions at Q1-12 (reflective or
   factual, narrative, factual), then 38 verbal-ability items **interleaved by type**: 10 match the
   following (idioms, proverbs, phrasal verbs, words, figures of speech, homonyms, sentence fill-ins),
   5 synonyms, 5 antonyms, 10 fill-in-the-blank and 8 sentence rearrangements. A rearrangement is four
   parts (A)-(D) of **one sentence**, not a jumbled paragraph. 2026 shift reports (S5): usually 2 passages
   of about 5 questions, sometimes a third short unseen passage (one shift placed it at the end). Other
   items reported: idioms, one-word substitution and 1-2 error-detection items. Syllabus: factual,
   narrative and literary passages, at most 300 words.
6. **Difficulty is mostly direct NCERT recall** with one-step numericals. NTA publishes no difficulty
   mix. The blueprint targets (easy/medium/hard, as MockMob labels them) are inferred.

## 3. Per-subject summary

Units are listed as "target (min-max)". The full chapter ranges are in the JSON files. Types are
standalone questions: S = single, M = match, Q = sequence, St = multi-statement, AR = assertion-reason.
Sets = passage sets × size.

| Subject (code) | Structure | Unit targets | Types S/M/Q/St/AR + sets | Confidence (structure / units / types) | Main inferences |
|---|---|---|---|---|---|
| English (101) | 50; passages first, then mixed verbal ability | RC 10 (8-15); Vocabulary 13; Correct Word Usage 11; Para Jumbles (sentence rearrangement) 7; Match 9 | Syn 4, Ant 4, Idiom 3, One-word 2, Fill 10, Error 1, M 9, Rearr 7 + 2×5 (2-3 sets of 4-5) | high / medium / medium | Difficulty; subtype ranges merge the 2025 paper with 2026 recall |
| General Test (501) | 50; mixed areas | GK 12, Current affairs 6, Mental ability 5, Numerical 5, Quant reasoning 11, Logical reasoning 10, Science 1 | 44/2/2/1/1, optional DI set | high / low / low | All area targets come from 2025 shift recall (quant 14-20, reasoning 10-16, GK 15-20) |
| Accountancy (301) | 50 | Partnership 8; Reconstitution 13; Dissolution 8; Company accounts 14; Analysis of FS 7; CAS 0 | 35/4/6/5/0, no sets; about 25% numerical | high / medium / medium | Chapter splits; CAS excluded |
| Business Studies (305) | 50; sets at 41-50 | 12 units, 3-6 each (Directing 6, Principles 5, Finance 5, Marketing 5) | 26/5/4/5/0 + 2×5 cases | high / medium / medium | Financial Markets 3 (0 in the paper read) |
| Economics (309) | 50; sets at 41-50 | Micro 20 (16-24); Macro 26 (22-30); IED 4 (0-8) | 25/5/5/5/0 + 2×5; about 20% numerical | high / medium (IED low) / medium | IED share (0 in the paper read) |
| Mathematics (319) | A 15 + B1 35 (core) or A 15 + B2 35 (applied) | A: matrices/determinants 4, calculus 8, LPP 2, probability distributions 1. B1: calculus 16, vectors and 3D 6, algebra 5, R&F 3, probability 3, LPP 2. B2: applied units 24 (numbers 7, financial maths 6, probability distributions 5, time-based data 3, inferential statistics 3), calculus 5, algebra 3, LPP 3 | 42/5/0/3/0, no sets; about 80% computational | high / medium / medium | 7 B1 and 6 B2 questions could not be mapped from the extracted text |
| Physics (322) | 50 | Electrostatics 8, Current 6, Magnetism 7, EMI and AC 7, EM waves 3, Optics 8, Dual nature 3, Atoms and nuclei 4, Semiconductors 4 | 44/4/1/1/0, no sets; about 50% numerical | high / medium / medium | Difficulty |
| Chemistry (306) | 50; sets at 41-50 | 10 units × 5 (3-7) | 25/5/5/5/0 + 2×5 | high / medium-high / medium | Difficulty |
| Biology (304) | 50; sets at 41-50 | Reproduction 10, Genetics and evolution 11, Human welfare 9, Biotechnology 10, Ecology 10 | 24/5/6/5/0 + 2×5 | high / medium-high / medium | Chapter splits |
| History (314) | 50; sets at 41-50 | Part I 15, Part II 17, Part III 18 (12 themes, 3-6 each, Gandhi 6) | 30/4/2/4/0 + 2×5 source passages | high / medium / medium | AR allowance (2026 recall only) |
| Political Science (323) | 50; sets at 41-50 | Politics in India 27 (9 topics × 3); World politics 23 | 30/4/2/4/0 + 2×5 | medium / low / low | Everything except the exam rules; passage sets are confirmed by 2025 recall (LTTE, Nepal, Partition, princely states) |
| Geography (313) | 50; sets at 41-50 | Transport and trade 12, People 10, Human activities 10, Resources and planning 10, Settlements 3, Issues 3, Nature and scope 2 (2025 paper: 25 per NCERT book) | 25/5/5/5/0 + 2×5 case studies | high / medium / medium | Mapping between canonical chapters and the two books |
| Psychology (324) | 50; sets assumed | 7 units: Disorders 9, Self 8, the rest 5-7 | 26/5/4/5/0 + 2×5 vignettes | medium / low / low | Unit targets from 2025 shift reports; sets assumed |
| Sociology (326) | 50; sets assumed | Indian Society 23, Change and Development 27 | 30/4/2/4/0 + 2×5 | medium / low / low | Everything except the exam rules |
| Computer Science (308) | A 15 + B1 35 (CS) or A 15 + B2 35 (IP) | A: SQL 7, database concepts 4, networks 4. B1: 11 syllabus units, 2-5 each. B2: Pandas 12, SQL 7, Matplotlib 6, societal impacts 6, networks 4 | 34/5/5/6/0, no sets; about 8 code or query output items | high / medium (B1 low) / medium | B1 targets (no B1 paper read) |

Difficulty targets (easy/medium/hard): standard theory 0.40/0.45/0.15; Chemistry, Biology and Computer
Science 0.35/0.50/0.15; Physics and Mathematics 0.30/0.50/0.20; English 0.35/0.50/0.15; General Test
0.35/0.45/0.20. All are **inferred**, with ±0.10 ranges. Reported 2026 difficulty (S9): Physics and
Mathematics were the hardest (moderate to hard), the General Test moderate to challenging, and most
others easy to moderate or moderate.

## 4. Chapters that must never enter an NTA paper

These chapters are not in the 2026 syllabus but still hold live questions (production, read-only count
on 13 Oct 2026). Each blueprint lists them in `excludedChapters`.

| Subject | Chapters (live rows) |
|---|---|
| Biology | Reproduction in Organisms (79), Environmental Issues (23) |
| Chemistry | Isolation of Elements (21), p-Block Elements (17), Solid State (13), Chemistry in Everyday Life (12), Surface Chemistry (11), Polymers (10) |
| Accountancy | Computerized Accounting System (128): optional in the syllabus, 0 in the 2025 paper |
| Computer Science | Boolean Algebra (15), Python Revision (13), Functions (11), Interface Python with MySQL (6) |
| Political Science | US Hegemony in World Politics (14), Cold War Era (9), Rise of Popular Movements (8) |
| History | Kings & Chronicles (10), Partition (10) |
| Psychology | Developing Psychological Skills (12), Psychology & Life (11) |
| Physics | Communication Systems (12) |
| Business Studies | Entrepreneurship Development (12) |

## 5. What this means for the current engine (`data/nta_paper_pattern.js`)

The layout in commit 4026a29 differs from the real papers in four ways:

- **English.** The engine alternates verbal blocks with passages and keeps each verbal type in a block. Real
  papers put the 2-3 passages first (Q1-10 or Q1-12) and interleave the verbal types. A run of 10-12
  passage questions at the start is authentic. What is not authentic is fragments of 1-3 questions,
  more than 3 passages, or passages above 300 words.
- **Domain papers.** The engine lays chapters out in syllabus order, with up to two sets anywhere. Real
  papers mix chapters in Q1-40 and put the two 5-question sets at Q41-50.
- **Types.** The engine has no type quotas for domain subjects. Real papers hold about 5 match, 5 sequence and
  5 multi-statement items. `questions.question_type` is null for most live rows, so the engine must
  classify from the stem. `_types.json` holds patterns built from the 2025 NTA wording. Run over the 10
  extracted papers, they reproduce the manual type counts to within ±1 per type when English-only types
  are restricted to English.
- **Passage sets.** Production has passage rows only for English (41 live rows). No domain subject has
  sets, so domain papers need the blueprint's `ifUnavailable` rule (standalone questions from the same
  chapters at the end) until case sets are generated.

Live bank against one paper's chapter targets (all live rows, before any score filter): every subject
can fill one paper except **Psychology: Psychological Disorders has 3 live questions against a target of 9**
(87 live questions in total, 23 of them out of syllabus).

## 6. Method and limits

- Rules: the 2026 and 2025 bulletins were read in full text (`pdftotext`).
- Syllabi: `data/CUET 2026/*.pdf`. The repo's `data/pyq_anchors` files are manual seeds, not real PYQs,
  so they were not used as evidence.
- Papers: one shift per subject, from a publisher's solved reprint. Shift dates are not printed. A
  reprint can drop passage headers. The Physics and Accountancy reprints show no "read the passage"
  text, so those papers may have had sets that the reprint lost.
- 2026: no full 2026 papers were available. 2026 evidence is shift recall and qualitative analysis (S5,
  S9), which conflict between shifts.
- Inferred items are listed per blueprint in `evidence.inferred`. Confidence is given per aspect in
  `evidence.confidence`.
- To raise confidence: read more 2025 and 2026 shifts per subject (NTA shows each candidate their own
  paper during answer-key challenges), especially for General Test, Political Science, Psychology,
  Sociology and Computer Science B1, then bump `blueprintVersion`.

## Sources

S1 NTA CUET(UG)-2026 Information Bulletin. S2 NTA CUET(UG)-2025 Information Bulletin. S3 NTA CUET(UG)-2026
syllabi (cuet.nta.nic.in/cuetug-2026-syllabus; local copies in `data/CUET 2026`). S4 Oswaal solved
reprints of the CUET(UG) 2025 papers (11 subjects). S5 Careers360 CUET English 2026 shift recall. S6
Careers360 CUET 2025 GAT analysis. S7 Careers360 CUET Political Science 2025 paper. S8 Careers360 CUET
Psychology 2025 analysis. S9 Hitbullseye CUET 2026 analysis. Full titles, URLs and what each source was
used for are in `data/nta_blueprints/_sources.json`.
