# MockMob chapter map audit: CUET 2026 and CBSE/NCERT Class 12

Read-only audit of `data/canonical_syllabus.js` for the 15 TOP_SUBJECTS. Also checked: `data/subjects.js`, `data/subject_registry.js`, `data/cuet_chapter_priorities.json`, `data/pyq_anchors.js` (legacy map), `scripts/pipeline/lib/factoryEvidence.mjs` (alias), `supabase/migrations/0026_cuet_2026_canonical_syllabus.sql` (header only). No repo file was changed. Supabase was not queried.

## Sources and how far they can be trusted

| Source | What it settles | Status |
|---|---|---|
| NTA CUET (UG) 2026 syllabus PDFs, `data/CUET 2026/*.pdf` (text extracted with pdftotext) | What CUET 2026 tests, unit by unit | Read in full for all 15 subjects |
| CBSE Senior Secondary Curriculum **2026-27**, `cbseacademic.nic.in/web_material/CurriculumMain27/SecPart2/<Subject>_SecP2_2026-27.pdf` (read 31 Oct 2026, parsed in memory) | Which NCERT chapters a current Class 12 student is examined on, with chapter titles for Physics, Chemistry, Biology, Geography, Political Science, History, Sociology, Psychology, Business Studies, CS, IP, Maths units, Applied Maths units, Economics units, Accountancy units | Read; this is the strongest board-side source |
| ncert.nic.in textbook pages | Exact NCERT tables of contents | **Not readable** (TLS errors and JS-rendered chapter lists). NCERT URL codes in the CBSE file confirm book sizes: Fundamentals of Human Geography `legy1=0-8` (8 chapters), India People and Economy `legy2=0-9` (9 chapters) |
| Web search (secondary sites) | CS Class 12 13-chapter list (Shaalaa, IndCareer); Pol Sci Part A Ch 2 = "Contemporary Centres of Power" (edzy, aglasem; CBSE 2026-27 agrees); IED Poverty and Infrastructure deleted (MTG blog, Vedantu); Sociology deletions (CBSE deleted-content list 2020-21, GetMyUni); Accountancy Part I = 4 chapters (Collegedunia, aglasem, Competishun) | Secondary; used only where they agree with each other or with CBSE |
| My own knowledge of NCERT titles | Exact NCERT titles not printed in the CBSE file (Maths chapters, Economics chapters, Accountancy Part II, IP book) | Marked **(unverified)** below |

Important context:
- Students in Class 12 now (2026-27) sit **CUET 2027**. NTA has not published a 2027 syllabus (the repo's `subject_registry.js` says the same). Everything below is against CUET 2026; re-run this audit when the 2027 PDFs appear.
- CBSE 2026-27 marks several old NCERT chapters as **"included in the syllabus but assessed only formatively"** (not in the board exam): Chemistry's Surface Chemistry, Isolation of Elements, Polymers, Chemistry in Everyday Life; Biology's Environmental Issues; Geography's Population Composition, Human Settlements (Fundamentals book), Migration. They are **not in CUET 2026** either. For a CUET product they count as deleted.
- Where CUET goes beyond the CBSE Class 12 board syllabus: Economics (all of Introductory Microeconomics is CBSE **Class 11**), Sociology (4 chapters CBSE no longer examines), CS Section B1 (Queue, Searching, Sorting, Understanding Data, Security Aspects come from the NCERT CS book, not CBSE 083), Maths Section A1. Students need a "CUET only" label on these, not a silent mix.

## Cross-cutting defects (not counted in the per-subject totals)

| ID | Severity | Defect |
|---|---|---|
| X1 | MEDIUM | `canonical_syllabus.js` header says it keeps "a stability bias toward preserving existing chapter names". This is the cause of the "Existing ... Coverage" placeholder units, which hold deleted or off-syllabus chapters (Chemistry 6, Physics 1, Psychology 2, Business Studies 1). |
| X2 | MEDIUM | The map has no fields for `ncert_ref`, `cuet_unit`, `in_cuet`, `in_board`, `class_level` or `stream` (Maths B1/B2, CS B1/B2, Accountancy CAS option). Without these the UI cannot tell a student "CUET only", "Class 11" or "only if you chose IP". |
| X3 | MEDIUM | `cuet_chapter_priorities.json` (used by onboarding "next chapter by name", the pipeline planner and the Flutter `chapter_order.dart`) uses names that are not canonical chapters in 8 of 10 subjects: `Grammar`, `Error Detection`, `Quantitative Aptitude`, `Logical Reasoning`, `Data Interpretation`, `Partnership`, `Company Accounts`, `Financial Statements`, `Dissolution`, `Marketing`, `National Income`, `Government Budget`, `Money and Banking`, `Demand/Supply`, and "and" spellings where the canonical name uses "&". Unless the consumers normalise, exact matching fails. Counted per subject below. |
| X4 | LOW | `subjects.js` still carries old hand-written chapter lists (with deleted chapters, e.g. English literature, Chemistry Solid State). They are overwritten at runtime from the canonical map for these 15 subjects, so they do no harm in the web app, but the comment says they seed the DB (`scripts/seed.mjs`, migration 0004). Migration 0026 is "upsert + map only; no deletes", so deleted chapters most likely still sit in `public.chapters` (DB state **unverified**, not queried). |
| X5 | LOW | Alias logic is scattered: `pyq_anchors.js` LEGACY_CHAPTER_MAP, `factoryEvidence.mjs` CHAPTER_ALIASES (only the Dissolution pair), `cuet_top_route_audit.json` chapter_aliases. One exported alias map should replace all three (see Migration). |

## Per-subject findings

Severity key: HIGH = student misled (deleted or off-syllabus chapter taught, real chapter missing); MEDIUM = name a student won't recognise, duplicate or merged chapter, wrong unit or grouping, priorities mismatch; LOW = cosmetic.

### 1. English (CUET 101) — H 0, M 1, L 3

CUET 2026: Reading Comprehension (factual, narrative, literary passages, max 300 words); Verbal Ability (rearranging the parts, match the following, choosing the correct word, synonyms and antonyms). CUET English is a language test; CBSE English Core literature (Flamingo, Vistas) is not tested, so leaving it out is correct.

| ID | Sev | Defect |
|---|---|---|
| EN-M1 | MEDIUM | Priorities list `Reading Comprehension` (a unit), `Grammar`, `Error Detection` (not in CUET 2026), `Para Jumbles`, `Vocabulary`. Onboarding can name a chapter that does not exist. |
| EN-L1 | LOW | `Vocabulary` → CUET wording "Synonyms and Antonyms". |
| EN-L2 | LOW | `Para Jumbles` → CUET "Rearranging the Parts" (keep "Para Jumbles" as the friendly subtitle). |
| EN-L3 | LOW | `Correct Word Usage` → CUET "Choosing the Correct Word". |

Target shape (no NCERT link; in-NCERT = n/a):

| Unit | Chapter | CUET | in CUET |
|---|---|---|---|
| Reading Comprehension | Factual Passage | 1a | yes |
| | Narrative Passage | 1b | yes |
| | Literary Passage | 1c | yes |
| Verbal Ability | Rearranging the Parts (Para Jumbles) | 2a | yes |
| | Match the Following | 2b | yes |
| | Choosing the Correct Word | 2c | yes |
| | Synonyms and Antonyms | 2d | yes |

### 2. General Aptitude Test (CUET 501, id `gat`) — H 0, M 2, L 2

CUET 2026: General Knowledge, Current Affairs, General Mental Ability, Numerical Ability, Reasoning ("simple application of basic mathematical concepts: arithmetic, algebra, geometry, mensuration, statistics"), Logical and Analytical Reasoning, General Science and Environment Literacy. No NCERT book.

| ID | Sev | Defect |
|---|---|---|
| GT-M1 | MEDIUM | Overlap: unit `Numerical Ability` and unit `Quantitative Reasoning` (with `Basic Mathematical Concepts` and `Statistical Data Analysis`). The last two are sub-points of CUET's quantitative reasoning line, not separate topics; questions will scatter across four near-identical tags. |
| GT-M2 | MEDIUM | Priorities use `Quantitative Aptitude`, `Logical Reasoning`, `Data Interpretation` (none canonical; "data interpretation" is not named in CUET 2026). |
| GT-L1 | LOW | Six units for nine chapters, most with one chapter. |
| GT-L2 | LOW | Display name "General Test"; NTA calls 501 "General Aptitude Test" (registry crosswalk `gat` → `general_test` already exists). |

Target shape:

| Unit | Chapter | in CUET |
|---|---|---|
| General Knowledge and Current Affairs | General Knowledge | yes |
| | Current Affairs | yes |
| Reasoning | General Mental Ability | yes |
| | Logical and Analytical Reasoning | yes |
| Quantitative Aptitude | Numerical Ability | yes |
| | Quantitative Reasoning (arithmetic, algebra, geometry, mensuration, statistics) | yes |
| General Science and Environment Literacy | General Science and Environment Literacy | yes |

### 3. Accountancy (CUET 301) — H 0, M 5, L 5

CUET 2026 Units: I Accounting for Partnership; II Reconstitution (change in PSR, revaluation, goodwill, admission, retirement/death); III Dissolution (excluding piecemeal distribution, sale to a company, insolvency); IV Company Accounts (share and debenture capital); V Analysis of Financial Statements (company FS, analysis, comparative and common-size, ratios, cash flow); **"Optional to Unit V": Computerised Accounting System**. CBSE 2026-27 Part B is likewise *either* Financial Statement Analysis *or* Computerised Accounting. NCERT: Accountancy Part I (4 chapters after rationalisation; Not-for-Profit Organisations removed) and Part II (company accounts and analysis), plus a separate NCERT book "Accountancy – Computerised Accounting System".

| ID | Sev | Defect |
|---|---|---|
| AC-M1 | MEDIUM | Duplicate: `Dissolution of Partnership` and `Dissolution of Partnership Firm` in the same unit (only the pipeline aliases them). Keep "Dissolution of Partnership Firm" (Part I Ch 4). |
| AC-M2 | MEDIUM | `Profit & Loss Appropriation Account` as its own chapter splits NCERT Part I Ch 1 into two tags; it is a topic of "Accounting for Partnership: Basic Concepts", not a CUET heading. |
| AC-M3 | MEDIUM | `Analysis of Financial Statements` and `Comparative & Common Size Statements` overlap: comparative and common-size statements are the tools section of NCERT Part II "Analysis of Financial Statements" (CUET's "Tools for Financial Analysis"). |
| AC-M4 | MEDIUM | CAS is modelled as an extra unit, not as the alternative to Unit V. A student who chose Analysis of FS gets CAS questions and vice versa. How NTA sets the optional part in a no-choice paper is **unverified**; at minimum let the student pick. |
| AC-M5 | MEDIUM | Priorities `Partnership`, `Company Accounts`, `Financial Statements`, `Dissolution` are not chapter names. |
| AC-L1 | LOW | `Partnership Fundamentals` → NCERT Part I Ch 1 "Accounting for Partnership: Basic Concepts" (the current name follows TS Grewal, also familiar). |
| AC-L2 | LOW | `Admission of Partner`, `Retirement & Death of Partner` → NCERT "Reconstitution of a Partnership Firm – Admission of a Partner" / "– Retirement/Death of a Partner" (Part I Ch 2, 3; exact dash wording **unverified**). |
| AC-L3 | LOW | `Change in Profit Sharing Ratio`, `Goodwill Valuation`: CUET bullets and TS Grewal chapters, but inside NCERT Part I Ch 2 (placement **unverified**). Keep, label "part of NCERT Ch 2". |
| AC-L4 | LOW | `Share Capital` → "Accounting for Share Capital" (Part II Ch 1); `Debentures` → "Issue and Redemption of Debentures" (Part II Ch 2) (**unverified** exact title); `Financial Statements of Company` → "Financial Statements of a Company". |
| AC-L5 | LOW | Unit name casing `Reconstitution of a Partnership firm`. |

Target shape:

| Unit | Chapter | NCERT | CUET | in CUET | in NCERT/board |
|---|---|---|---|---|---|
| Accounting for Partnership Firms | Accounting for Partnership: Basic Concepts (incl. P&L Appropriation, guarantee, past adjustments) | Part I Ch 1 | I | yes | yes |
| | Change in Profit Sharing Ratio | Part I Ch 2 topic (unverified) | II | yes | yes |
| | Goodwill: Nature and Valuation | Part I Ch 2 topic (unverified) | II | yes | yes |
| | Admission of a Partner | Part I Ch 2 | II | yes | yes |
| | Retirement and Death of a Partner | Part I Ch 3 | II | yes | yes |
| | Dissolution of Partnership Firm | Part I Ch 4 | III | yes | yes |
| Company Accounts | Accounting for Share Capital | Part II Ch 1 | IV | yes | yes |
| | Issue of Debentures | Part II Ch 2 | IV | yes | yes |
| Analysis of Financial Statements (option A) | Financial Statements of a Company | Part II Ch 3 | V | yes | yes |
| | Analysis of Financial Statements (incl. comparative, common-size) | Part II Ch 4 | V | yes | yes |
| | Accounting Ratios | Part II Ch 5 | V | yes | yes |
| | Cash Flow Statement | Part II Ch 6 | V | yes | yes |
| Computerised Accounting System (option B, instead of Analysis) | Computerised Accounting System (overview, structure, AIS) | NCERT CAS book (chapter numbers unverified) | V-opt | yes | yes (CBSE option) |
| | Accounting Applications of Electronic Spreadsheet | NCERT CAS book (unverified) | V-opt | yes | yes (CBSE option) |

Note: the canonical file spells "Computerized"; CUET and NCERT spell "Computerised". Migration 0026 already rewrote questions to the "-ized" spelling; keep one spelling and alias the other.

### 4. Economics (CUET 309) — H 1, M 5, L 5

CUET 2026: Course I Introductory Microeconomics (4 units), Course II Introductory Macroeconomics (5 units), Course III Indian Economic Development (Unit I Development Policies and Experience 1947-90; Unit II Economic Reforms since 1991; Unit III Current Challenges: human capital, rural development, employment, environment and sustainable development; Unit IV Development Experiences: comparison with neighbours). CBSE 2026-27: **Microeconomics is Class XI**; Class XII = Macroeconomics + Indian Economic Development (Units 6-8). NCERT prints "Introductory Microeconomics" as a Class XII book and "Indian Economic Development" as a Class XI book, the reverse of how CBSE teaches them.

| ID | Sev | Defect |
|---|---|---|
| EC-H1 | HIGH | `Infrastructure` is taught. Deleted from NCERT IED in rationalisation (MTG, Vedantu), absent from CBSE 2026-27 Unit 7 and from CUET 2026 Unit III. (Poverty, also deleted, is correctly absent.) |
| EC-M1 | MEDIUM | No class labels. Microeconomics is CBSE Class 11 but in CUET; IED is an NCERT "Class XI" book examined in CBSE Class 12. Students will think chapters are missing or extra. |
| EC-M2 | MEDIUM | IED is one flat unit of 9 chapters; CUET and CBSE group it into Development Experience 1947-90 and Reforms, Current Challenges, Comparison with Neighbours. |
| EC-M3 | MEDIUM | `Income Determination` → "Determination of Income and Employment" (NCERT Macro, CBSE and CUET all use this). |
| EC-M4 | MEDIUM | `Indian Economic Development 1950–1990` repeats the book title; NCERT chapter is "Indian Economy 1950–1990". |
| EC-M5 | MEDIUM | Priorities `Money and Banking`, `National Income`, `Government Budget`, `Balance of Payments`, `Demand/Supply` (the last is Class 11 micro and not a chapter). |
| EC-L1 | LOW | `National Income & Related Aggregates` matches CBSE and CUET; NCERT Macro chapter is "National Income Accounting" (**unverified** exact title). Show NCERT title as subtitle. |
| EC-L2 | LOW | `Balance of Payments` matches CBSE; CUET and NCERT call it "Open Economy Macroeconomics" (it includes exchange rates). |
| EC-L3 | LOW | `Economic Reforms Since 1991` matches CUET/CBSE; NCERT "Liberalisation, Privatisation and Globalisation: An Appraisal". CBSE 2026-27 adds demonetisation and GST concepts (not in CUET). |
| EC-L4 | LOW | Short titles: `Human Capital Formation` ("... in India"), `Employment` ("Employment: Growth, Informalisation and Other Issues"), `Development Experiences of India` ("Comparative Development Experiences of India and its Neighbours"). NCERT titles from memory, **unverified**. |
| EC-L5 | LOW | `Theory of Firms under Perfect Competition` → "The Theory of the Firm under Perfect Competition". |

Target shape (NCERT chapter numbers are **unverified** where marked *; the rationalised IED numbering after removing Poverty and Infrastructure is not confirmed):

| Unit | Chapter | NCERT | CUET | in CUET | in board |
|---|---|---|---|---|---|
| Introductory Microeconomics (CBSE Class 11) | Introduction and Theory of Consumer Behaviour | Micro Ch 1-2 | I-I | yes | Class 11 |
| | Production and Costs | Micro Ch 3 | I-II | yes | Class 11 |
| | The Theory of the Firm under Perfect Competition (incl. supply) | Micro Ch 4 | I-III | yes | Class 11 |
| | Market Equilibrium and Simple Applications | Micro Ch 5 | I-IV | yes | Class 11 |
| Introductory Macroeconomics | National Income and Related Aggregates | Macro Ch 1-2* | II-I | yes | yes |
| | Money and Banking | Macro Ch 3* | II-II | yes | yes |
| | Determination of Income and Employment | Macro Ch 4* | II-III | yes | yes |
| | Government Budget and the Economy | Macro Ch 5* | II-IV | yes | yes |
| | Open Economy Macroeconomics (Balance of Payments) | Macro Ch 6* | II-V | yes | yes |
| IED: Development Experience (1947-90) and Economic Reforms | Indian Economy on the Eve of Independence | IED Ch 1 | III-I | yes | yes |
| | Indian Economy 1950–1990 | IED Ch 2 | III-I | yes | yes |
| | Liberalisation, Privatisation and Globalisation: An Appraisal | IED Ch 3 | III-II | yes | yes |
| IED: Current Challenges facing the Indian Economy | Human Capital Formation in India | IED* | III-III | yes | yes |
| | Rural Development | IED* | III-III | yes | yes |
| | Employment: Growth, Informalisation and Other Issues | IED* | III-III | yes | yes |
| | Environment and Sustainable Development | IED* | III-III | yes | yes |
| IED: Development Experience of India | Comparative Development Experiences of India and its Neighbours | IED* | III-IV | yes | yes |
| (retired) | Infrastructure | deleted | — | no | no |

### 5. Business Studies (CUET 305) — H 1, M 3, L 2

CUET 2026 Units I-XII exactly match NCERT Business Studies Part I (Ch 1-8, Principles and Functions of Management) and Part II (Ch 9-12, Business Finance and Marketing). CBSE 2026-27 Class XII has the same 12 chapters; Entrepreneurship Development appears only in the CBSE Class XI course.

| ID | Sev | Defect |
|---|---|---|
| BS-H1 | HIGH | `Entrepreneurship Development` is taught (in placeholder unit). Not in CUET 2026, not a Class 12 NCERT/CBSE chapter (old Part II Ch 13 removed; now CBSE Class 11). |
| BS-M1 | MEDIUM | Placeholder unit `Existing Business Studies Coverage`. |
| BS-M2 | MEDIUM | 12 one-chapter units; NCERT and CBSE group into two parts. |
| BS-M3 | MEDIUM | Priorities `Marketing` (chapter is `Marketing Management`). |
| BS-L1 | LOW | Unit/chapter label pairs differ (`Business Finance` / `Financial Management`, `Marketing` / `Marketing Management`); fine once the unit is the NCERT part. NCERT Ch 11 exact title ("Marketing" vs "Marketing Management") **unverified**; CBSE uses "Marketing Management". |
| BS-L2 | LOW | `Nature & Significance of Management` "&" vs "and". Also: CUET cites the Consumer Protection Act 2019; check no 1986-Act questions remain (content check, not a map defect). |

Target shape:

| Unit | Chapter | NCERT | CUET | in CUET | in NCERT |
|---|---|---|---|---|---|
| Principles and Functions of Management | Nature and Significance of Management | Part I Ch 1 | I | yes | yes |
| | Principles of Management | Part I Ch 2 | II | yes | yes |
| | Business Environment | Part I Ch 3 | III | yes | yes |
| | Planning | Part I Ch 4 | IV | yes | yes |
| | Organising | Part I Ch 5 | V | yes | yes |
| | Staffing | Part I Ch 6 | VI | yes | yes |
| | Directing | Part I Ch 7 | VII | yes | yes |
| | Controlling | Part I Ch 8 | VIII | yes | yes |
| Business Finance and Marketing | Financial Management | Part II Ch 9 | IX Business Finance | yes | yes |
| | Financial Markets | Part II Ch 10 | X | yes | yes |
| | Marketing Management | Part II Ch 11 | XI Marketing | yes | yes |
| | Consumer Protection | Part II Ch 12 | XII | yes | yes |
| (retired) | Entrepreneurship Development | removed (CBSE Class 11) | — | no | no |

### 6. Mathematics (CUET 319) — H 1, M 2, L 3

CUET 2026: Section A1 (common: matrices and determinants, derivatives, maxima/minima, integration, area, differential equations, probability distributions, LP), then **either** Section B1 Mathematics (6 units = the 13 NCERT chapters) **or** Section B2 Applied Mathematics (8 units: Numbers/Quantification, Algebra, Calculus incl. marginal cost/revenue and consumer/producer surplus, Probability Distributions, Time-Based Data, Inferential Statistics, Financial Mathematics, Linear Programming). CBSE 2026-27 Maths units: I Relations and Functions, II Algebra, III Calculus, IV Vectors and 3-D Geometry, V LP, VI Probability (matches ours). CBSE Applied Mathematics (241) has the same 8 units as CUET B2; it has no NCERT textbook (**unverified**).

| ID | Sev | Defect |
|---|---|---|
| MA-H1 | HIGH | Applied Maths chapters (`Numbers, Quantification and Numerical Applications`, `Probability Distributions`, `Time Based Data`, `Inferential Statistics`, `Financial Mathematics`) sit as a 7th unit in the same chapter pool as B1. A B1 (NCERT Maths) student practising "Mathematics" can get t-tests, time series and EMI questions that are in neither their syllabus nor NCERT. Needs a `stream` field and filtering. |
| MA-M1 | MEDIUM | The Applied Maths unit is incomplete vs CUET B2: Algebra, Calculus (with economics applications) and Linear Programming are missing for B2, and would collide with the B1 chapter names if added unlabelled. |
| MA-M2 | MEDIUM | Section A1 (common to both streams) is not modelled, so a mock cannot reproduce the A1 + B1/B2 paper. |
| MA-L1 | LOW | "&" vs NCERT "and" (`Relations & Functions`, `Continuity & Differentiability`). |
| MA-L2 | LOW | Probability: CUET B1 lists conditional probability, multiplication theorem, independence, total probability, Bayes only. Random variables and binomial distribution questions belong to A1/B2 "Probability Distributions", not B1 Probability. Tag accordingly. |
| MA-L3 | LOW | Separate `applied_mathematics` subject duplicates the unit (registry crosswalks it to `mathematics`). Priorities for Maths are all valid canonical names. |

Target shape:

| Unit | Chapter | NCERT | CUET | in CUET | in NCERT |
|---|---|---|---|---|---|
| Relations and Functions | Relations and Functions | Part I Ch 1 | B1-I | yes | yes |
| | Inverse Trigonometric Functions | Part I Ch 2 | B1-I | yes | yes |
| Algebra | Matrices | Part I Ch 3 | A1, B1-II | yes | yes |
| | Determinants | Part I Ch 4 | A1, B1-II | yes | yes |
| Calculus | Continuity and Differentiability | Part I Ch 5 | B1-III | yes | yes |
| | Application of Derivatives | Part I Ch 6 | A1, B1-III | yes | yes |
| | Integrals | Part II Ch 7 | A1, B1-III | yes | yes |
| | Application of Integrals | Part II Ch 8 | A1, B1-III | yes | yes |
| | Differential Equations | Part II Ch 9 | A1, B1-III | yes | yes |
| Vectors and Three-Dimensional Geometry | Vector Algebra | Part II Ch 10 | B1-IV | yes | yes |
| | Three Dimensional Geometry | Part II Ch 11 | B1-IV | yes | yes |
| Linear Programming | Linear Programming | Part II Ch 12 | A1, B1-V | yes | yes |
| Probability | Probability | Part II Ch 13 | B1-VI | yes | yes |
| Applied Mathematics (stream B2 only) | Numbers, Quantification and Numerical Applications | CBSE 241 Unit 1 (no NCERT) | B2-I | yes | no (CBSE Applied Maths) |
| | Algebra (Applied) | CBSE 241 Unit 2 | B2-II | yes | no |
| | Calculus (Applied: marginal cost/revenue, CS/PS) | CBSE 241 Unit 3 | B2-III | yes | no |
| | Probability Distributions | CBSE 241 Unit 4 | A1, B2-IV | yes | no |
| | Inferential Statistics | CBSE 241 Unit 5 | B2-VI | yes | no |
| | Time-Based Data | CBSE 241 Unit 6 | B2-V | yes | no |
| | Financial Mathematics | CBSE 241 Unit 7 | B2-VII | yes | no |
| | Linear Programming (Applied) | CBSE 241 Unit 8 | B2-VIII | yes | no |

### 7. Physics (CUET 322) — H 1, M 1, L 2

CUET 2026 Units 1-9 match CBSE 2026-27 and NCERT Physics Part I (Ch 1-8) and Part II (Ch 9-14).

| ID | Sev | Defect |
|---|---|---|
| PH-H1 | HIGH | `Communication Systems` is taught. Removed from NCERT (book ends at Ch 14 Semiconductor Electronics), not in CBSE 2026-27, not in CUET 2026. |
| PH-M1 | MEDIUM | Placeholder unit `Existing Physics Coverage`. |
| PH-L1 | LOW | `Semiconductor Electronics` → "Semiconductor Electronics: Materials, Devices and Simple Circuits"; "&" vs "and" throughout. |
| PH-L2 | LOW | Priorities use "and" (`Moving Charges and Magnetism`, `Ray Optics and Optical Instruments`) where canonical uses "&". |

Target shape (all in CUET yes, in NCERT yes):

| Unit (CUET) | Chapter | NCERT |
|---|---|---|
| 1 Electrostatics | Electric Charges and Fields | Part I Ch 1 |
| | Electrostatic Potential and Capacitance | Part I Ch 2 |
| 2 Current Electricity | Current Electricity | Part I Ch 3 |
| 3 Magnetic Effects of Current and Magnetism | Moving Charges and Magnetism | Part I Ch 4 |
| | Magnetism and Matter | Part I Ch 5 |
| 4 Electromagnetic Induction and Alternating Currents | Electromagnetic Induction | Part I Ch 6 |
| | Alternating Current | Part I Ch 7 |
| 5 Electromagnetic Waves | Electromagnetic Waves | Part I Ch 8 |
| 6 Optics | Ray Optics and Optical Instruments | Part II Ch 9 |
| | Wave Optics | Part II Ch 10 |
| 7 Dual Nature of Matter and Radiation | Dual Nature of Radiation and Matter | Part II Ch 11 |
| 8 Atoms and Nuclei | Atoms | Part II Ch 12 |
| | Nuclei | Part II Ch 13 |
| 9 Electronic Devices | Semiconductor Electronics: Materials, Devices and Simple Circuits | Part II Ch 14 |
| (retired) | Communication Systems | deleted |

### 8. Chemistry (CUET 306) — H 6, M 2, L 3

CUET 2026 has exactly 10 units = the 10 rationalised NCERT chapters, same as CBSE 2026-27. CBSE marks Surface Chemistry, Isolation of Elements, Polymers and Chemistry in Everyday Life as formative-only (not examined). Solid State and Class 12 p-Block are gone (p-block groups 13-14 stay in Class 11; groups 15-18 were removed from Class 12).

| ID | Sev | Defect |
|---|---|---|
| CH-H1 | HIGH | `Solid State` taught: deleted from NCERT 12, not in CBSE or CUET. |
| CH-H2 | HIGH | `Surface Chemistry` taught: formative-only in CBSE, not in CUET. |
| CH-H3 | HIGH | `Isolation of Elements` taught: same. |
| CH-H4 | HIGH | `p-Block Elements` taught: removed from Class 12, not in CUET 2026. |
| CH-H5 | HIGH | `Polymers` taught: formative-only, not in CUET. |
| CH-H6 | HIGH | `Chemistry in Everyday Life` taught: formative-only, not in CUET. |
| CH-M1 | MEDIUM | Placeholder unit `Existing Chemistry Coverage`. |
| CH-M2 | MEDIUM | Ten one-chapter units; NCERT splits Part I (physical and inorganic, Ch 1-5) and Part II (organic, Ch 6-10). Students revise as Physical / Inorganic / Organic. |
| CH-L1 | LOW | "&" vs "and"; `d- and f-Block Elements` → NCERT "The d- and f-Block Elements". |
| CH-L2 | LOW | CUET Biomolecules lists hormones; whether the rationalised NCERT chapter keeps hormones is **unverified**. Keep hormone questions tagged but low priority. |
| CH-L3 | LOW | Priorities `Aldehydes Ketones and Carboxylic Acids` (no comma, "and") does not match `Aldehydes, Ketones & Carboxylic Acids`. |

Target shape (all in CUET yes, in NCERT yes):

| Unit | Chapter | NCERT | CUET |
|---|---|---|---|
| Physical Chemistry | Solutions | Part I Ch 1 | I |
| | Electrochemistry | Part I Ch 2 | II |
| | Chemical Kinetics | Part I Ch 3 | III |
| Inorganic Chemistry | The d- and f-Block Elements | Part I Ch 4 | IV |
| | Coordination Compounds | Part I Ch 5 | V |
| Organic Chemistry | Haloalkanes and Haloarenes | Part II Ch 6 | VI |
| | Alcohols, Phenols and Ethers | Part II Ch 7 | VII |
| | Aldehydes, Ketones and Carboxylic Acids | Part II Ch 8 | VIII |
| | Amines | Part II Ch 9 | IX |
| | Biomolecules | Part II Ch 10 | X |
| (retired) | Solid State, Surface Chemistry, Isolation of Elements, p-Block Elements, Polymers, Chemistry in Everyday Life | deleted / formative-only | no |

(Biomolecules can sit in its own "Biomolecules" unit if preferred; CBSE weight 7 marks.)

### 9. Biology (CUET 304) — H 2, M 0, L 2

CUET 2026 Units VI-X with 13 chapters = CBSE 2026-27 = NCERT 13 chapters. Our unit names already match.

| ID | Sev | Defect |
|---|---|---|
| BI-H1 | HIGH | `Reproduction in Organisms` taught: deleted from NCERT 12, not in CBSE or CUET. |
| BI-H2 | HIGH | `Environmental Issues` taught: CBSE formative-only (reading material), not in CUET 2026 Unit X. (Strategies for Enhancement in Food Production is correctly absent.) |
| BI-L1 | LOW | Titles: `Biotechnology Principles & Processes` → "Biotechnology: Principles and Processes"; `Human Health & Disease` → "Human Health and Disease"; `Biodiversity & Conservation` → "Biodiversity and Conservation" (CBSE prints "Biodiversity and its Conservation"; NCERT title **unverified** between the two). |
| BI-L2 | LOW | Priorities use "and" spellings. |

Target shape (all in CUET yes, in NCERT yes):

| Unit (CUET) | Chapter | NCERT |
|---|---|---|
| VI Reproduction | Sexual Reproduction in Flowering Plants | Ch 1 |
| | Human Reproduction | Ch 2 |
| | Reproductive Health | Ch 3 |
| VII Genetics and Evolution | Principles of Inheritance and Variation | Ch 4 |
| | Molecular Basis of Inheritance | Ch 5 |
| | Evolution | Ch 6 |
| VIII Biology and Human Welfare | Human Health and Disease | Ch 7 |
| | Microbes in Human Welfare | Ch 8 |
| IX Biotechnology and its Applications | Biotechnology: Principles and Processes | Ch 9 |
| | Biotechnology and its Applications | Ch 10 |
| X Ecology and Environment | Organisms and Populations | Ch 11 |
| | Ecosystem | Ch 12 |
| | Biodiversity and Conservation | Ch 13 |
| (retired) | Reproduction in Organisms; Environmental Issues | deleted / formative-only |

### 10. History (CUET 314) — H 2, M 0, L 2

CUET 2026 Themes I-XII = CBSE 2026-27 Themes 1-12 = NCERT Themes in Indian History Parts I-III (4 + 4 + 4). Kings and Chronicles (Mughal courts) and Understanding Partition were removed (also Colonial Cities, correctly absent).

| ID | Sev | Defect |
|---|---|---|
| HI-H1 | HIGH | `Kings & Chronicles` taught: removed from NCERT Part II, not in CBSE or CUET. |
| HI-H2 | HIGH | `Partition` taught: removed from NCERT Part III, not in CBSE or CUET. |
| HI-L1 | LOW | Names use "&" and drop NCERT subtitles. CUET uses different descriptors (e.g. "Harappan Civilisation and Archaeology", "Social Histories of Early Societies: Mahabharata", "Revolt of 1857: Patterns and Representations", "The Making of the Constitution"); show them as aliases/subtitles so a CUET-syllabus reader can match. |
| HI-L2 | LOW | Unit names (Parts I/II/III) are right; adding era tags (ancient / medieval / modern) helps. |

Target shape (all in CUET yes, in NCERT yes):

| Unit | Chapter (NCERT title) | NCERT | CUET theme |
|---|---|---|---|
| Themes in Indian History Part I | Bricks, Beads and Bones: The Harappan Civilisation | Theme 1 | I |
| | Kings, Farmers and Towns: Early States and Economies | Theme 2 | II |
| | Kinship, Caste and Class: Early Societies | Theme 3 | III |
| | Thinkers, Beliefs and Buildings: Cultural Developments | Theme 4 | IV |
| Themes in Indian History Part II | Through the Eyes of Travellers: Perceptions of Society | Theme 5 | V |
| | Bhakti-Sufi Traditions: Changes in Religious Beliefs and Devotional Texts | Theme 6 | VI |
| | An Imperial Capital: Vijayanagara | Theme 7 | VII |
| | Peasants, Zamindars and the State: Agrarian Society and the Mughal Empire | Theme 8 | VIII |
| Themes in Indian History Part III | Colonialism and the Countryside: Exploring Official Archives | Theme 9 | IX |
| | Rebels and the Raj: The Revolt of 1857 and its Representations | Theme 10 | X |
| | Mahatma Gandhi and the Nationalist Movement: Civil Disobedience and Beyond | Theme 11 | XI |
| | Framing the Constitution: The Beginning of a New Era | Theme 12 | XII |
| (retired) | Kings and Chronicles; Understanding Partition | removed | no |

(Subtitles follow CBSE 2026-27 wording; exact NCERT punctuation **unverified**.)

### 11. Political Science (CUET 323) — H 3, M 2, L 1

CBSE 2026-27: Part A Contemporary World Politics, 7 chapters (End of Bipolarity, Contemporary Centres of Power, Contemporary South Asia, International Organizations, Security in the Contemporary World, Environment and Natural Resources, Globalisation); Part B Politics in India since Independence, 8 chapters (Challenges of Nation-Building, Era of One-Party Dominance, Politics of Planned Development, India's External Relations, Challenges to and Restoration of the Congress System, The Crisis of Democratic Order, Regional Aspirations, Recent Developments in Indian Politics). CUET 2026 has 7 CWP topics (no Cold War, no US hegemony) and 9 PISI topics (no popular movements; the last NCERT chapter split into "Democratic Upsurge and Coalition Politics" and "Recent Issues and Challenges").

| ID | Sev | Defect |
|---|---|---|
| PS-H1 | HIGH | `Cold War Era` taught: removed from NCERT, not in CBSE or CUET. |
| PS-H2 | HIGH | `US Hegemony in World Politics` taught: removed, not in CBSE or CUET. |
| PS-H3 | HIGH | `Rise of Popular Movements` taught: removed, not in CBSE 2026-27 or CUET 2026. |
| PS-M1 | MEDIUM | `Democratic Upsurge and Coalition Politics` + `Recent Issues and Challenges`: two CUET topic names for one NCERT chapter, "Recent Developments in Indian Politics" (Part B Ch 8). Students won't find either in their book; merge, keep both as aliases. |
| PS-M2 | MEDIUM | `Alternative Centres of Power` → current title "Contemporary Centres of Power" (Part A Ch 2; old edition title was "Alternative Centres of Power"). |
| PS-L1 | LOW | `Crisis of the Democratic Order` → "The Crisis of Democratic Order"; `Challenges to & Restoration...` "&"; `International Organisations` (CBSE spells "Organizations"). |

Target shape (all in CUET yes, in NCERT yes):

| Unit | Chapter | NCERT | CUET topic |
|---|---|---|---|
| Contemporary World Politics | The End of Bipolarity | Part A Ch 1 | CWP 1 Disintegration of the Second World |
| | Contemporary Centres of Power | Part A Ch 2 | CWP 2 Alternative Centres of Power |
| | Contemporary South Asia | Part A Ch 3 | CWP 3 |
| | International Organisations | Part A Ch 4 | CWP 4 |
| | Security in the Contemporary World | Part A Ch 5 | CWP 5 |
| | Environment and Natural Resources | Part A Ch 6 | CWP 6 |
| | Globalisation | Part A Ch 7 | CWP 7 |
| Politics in India since Independence | Challenges of Nation Building | Part B Ch 1 | PISI 2 |
| | Era of One-Party Dominance | Part B Ch 2 | PISI 1 |
| | Politics of Planned Development | Part B Ch 3 | PISI 3 |
| | India's External Relations | Part B Ch 4 | PISI 4 |
| | Challenges to and Restoration of the Congress System | Part B Ch 5 | PISI 5 |
| | The Crisis of Democratic Order | Part B Ch 6 | PISI 6 |
| | Regional Aspirations | Part B Ch 7 | PISI 7 |
| | Recent Developments in Indian Politics | Part B Ch 8 | PISI 8 + 9 |
| (retired) | Cold War Era; US Hegemony in World Politics; Rise of Popular Movements | removed | no |

Order note: NCERT (and CBSE) put Contemporary World Politics as Part A; CUET lists Politics in India first. Either order is fine; pick the NCERT one to match textbooks.

### 12. Geography (CUET 313) — H 3, M 4, L 3

CBSE 2026-27 (and NCERT book sizes `legy1=0-8`, `legy2=0-9`): Fundamentals of Human Geography, 8 chapters (Human Geography; The World Population Distribution, Density and Growth; Human Development; Primary; Secondary; Tertiary and Quaternary Activities; Transport and Communication; International Trade). India: People and Economy, 9 chapters (Population Distribution, Density, Growth and Composition; Human Settlements; Land Resources and Agriculture; Water Resources; Mineral and Energy Resources; Planning and Sustainable Development in Indian Context; Transport and Communication; International Trade; Geographical Perspective on Selected Issues and Problems). Formative-only: Population Composition, Human Settlements (Fundamentals), Migration. CUET 2026 follows the same two books (A Units I-IV, B Units I-V).

| ID | Sev | Defect |
|---|---|---|
| GE-H1 | HIGH | `Manufacturing Industries` taught: removed from India P&E, not in CBSE or CUET. |
| GE-H2 | HIGH | `Migration` taught as a chapter: removed from India P&E (CBSE formative-only), not a CUET topic (CUET only mentions rural-urban migration under Issues and Problems). |
| GE-H3 | HIGH | Three real chapters missing: India P&E Ch 3 Land Resources and Agriculture, Ch 4 Water Resources, Ch 5 Mineral and Energy Resources are collapsed into `Resources & Development`. Students cannot practise them by chapter. |
| GE-M1 | MEDIUM | India P&E Ch 7 Transport and Communication and Ch 8 International Trade are not distinct from the world chapters of the same names (one `Transport & Communication`, one `International Trade`, in one unit). India-specific content (seaports and hinterland, India's trade pattern) has no home. |
| GE-M2 | MEDIUM | `India — People & Economy` is a book title used as a chapter; it is India P&E Ch 1 "Population: Distribution, Density, Growth and Composition". |
| GE-M3 | MEDIUM | `Human Settlements` sits in its own unit among Fundamentals units; in the current books it is only India P&E Ch 2 (the Fundamentals chapter is formative-only). |
| GE-M4 | MEDIUM | 7 units mix both books; NCERT and CUET use Book A (Units I-IV) and Book B (Units I-V). |
| GE-L1 | LOW | `Human Development` is ambiguous (was in both books; only Fundamentals Ch 3 remains). |
| GE-L2 | LOW | Titles: `Population — Distribution, Density, Growth` → "The World Population: Distribution, Density and Growth"; `Planning & Sustainable Development` → "... in Indian Context"; `Human Geography — Nature & Scope` → "Human Geography: Nature and Scope". |
| GE-L3 | LOW | Subject name "Geography / Geology" (official), but no Geology content exists; say so in the UI. |

Target shape (all in CUET yes, in NCERT yes):

| Unit | Chapter | NCERT | CUET |
|---|---|---|---|
| A. Fundamentals of Human Geography | Human Geography: Nature and Scope | FHG Ch 1 | A-I |
| | The World Population: Distribution, Density and Growth | FHG Ch 2 | A-II |
| | Human Development | FHG Ch 3 | A-II |
| | Primary Activities | FHG Ch 4 | A-III |
| | Secondary Activities | FHG Ch 5 | A-III |
| | Tertiary and Quaternary Activities | FHG Ch 6 | A-III |
| | Transport and Communication (World) | FHG Ch 7 | A-IV |
| | International Trade (World) | FHG Ch 8 | A-IV |
| B. India: People and Economy | Population: Distribution, Density, Growth and Composition | IPE Ch 1 | B-I |
| | Human Settlements | IPE Ch 2 | B-II |
| | Land Resources and Agriculture | IPE Ch 3 | B-III |
| | Water Resources | IPE Ch 4 | B-III |
| | Mineral and Energy Resources | IPE Ch 5 | B-III |
| | Planning and Sustainable Development in Indian Context | IPE Ch 6 | B-III |
| | Transport and Communication (India) | IPE Ch 7 | B-IV |
| | International Trade (India) | IPE Ch 8 | B-IV |
| | Geographical Perspective on Selected Issues and Problems | IPE Ch 9 | B-V |
| (retired) | Manufacturing Industries; Migration | removed | no |

If two units feel too coarse, use the CUET sub-units (A-I..A-IV, B-I..B-V) as the unit level; the NCERT book stays as a "part" label.

### 13. Psychology (CUET 324) — H 2, M 1, L 1

CUET 2026 Units 1-7 = CBSE 2026-27 Units I-VII = the 7 rationalised NCERT chapters. Chapters 8 and 9 of the old book are gone.

| ID | Sev | Defect |
|---|---|---|
| PY-H1 | HIGH | `Psychology & Life` taught: old Ch 8, not in CBSE 2026-27 or CUET. |
| PY-H2 | HIGH | `Developing Psychological Skills` taught: old Ch 9, not in CBSE or CUET. |
| PY-M1 | MEDIUM | Placeholder unit `Existing Psychology Coverage`. |
| PY-L1 | LOW | "&" vs "and"; seven one-chapter units match CUET and CBSE, so keep; an optional theme grouping is shown below. |

Target shape (all in CUET yes, in NCERT yes):

| Unit (optional theme) | Chapter | NCERT | CUET |
|---|---|---|---|
| Individual Differences and Self | Variations in Psychological Attributes | Ch 1 | 1 |
| | Self and Personality | Ch 2 | 2 |
| Stress, Disorders and Therapy | Meeting Life Challenges | Ch 3 | 3 |
| | Psychological Disorders | Ch 4 | 4 |
| | Therapeutic Approaches | Ch 5 | 5 |
| Social Psychology | Attitude and Social Cognition | Ch 6 | 6 |
| | Social Influence and Group Processes | Ch 7 | 7 |
| (retired) | Psychology and Life; Developing Psychological Skills | removed | no |

### 14. Sociology (CUET 326) — H 0, M 3, L 2

CBSE 2026-27 examines: Indian Society Ch 1 (non-evaluative), 2, 3, 5, 6 (7 = project, non-evaluative); Social Change and Development in India (CBSE numbering 8-15) Ch 8, 9, 11, 12, 15. It does **not** examine Ch 4 The Market as a Social Institution, Ch 10 The Story of Indian Democracy, Ch 13 Globalisation and Social Change, Ch 14 Mass Media and Communications. **CUET 2026 does test all four** (Indian Society Unit II "The Market as a Social Institution"; Change and Development Unit II "Social Change and the Polity" = constitution, parties, panchayati raj; Unit IV "Media and Social Change", "Globalisation and Social Change"). CUET keeps the old CBSE unit headings, which differ from the NCERT chapter titles. Whether NCERT still prints Ch 4, 10, 13, 14 is **unverified** (CBSE keeps the 1-15 numbering with gaps, which suggests they are still in the books).

| ID | Sev | Defect |
|---|---|---|
| SO-M1 | MEDIUM | No "CUET only, not in your board exam" label on Market, Story of Indian Democracy, Globalisation and Social Change, Mass Media and Communications. A student following the CBSE syllabus will have skipped them. Keep them, label them. |
| SO-M2 | MEDIUM | `Introducing Indian Society` is non-evaluative in CBSE and not a CUET topic. Keep as "background" or drop from mocks. |
| SO-M3 | MEDIUM | `Market as a Social Institution` is placed in the "Social Change and Development in India" unit; it is Indian Society Ch 4 (and CUET Indian Society Unit II). |
| SO-L1 | LOW | Short titles: `Demographic Structure` ("The Demographic Structure of the Indian Society"), `Social Institutions` ("... : Continuity and Change"), `Patterns of Social Inequality` ("... and Exclusion"), `Challenges of Cultural Diversity` ("The ..."), `Story of Indian Democracy` ("The ..."). |
| SO-L2 | LOW | No CUET-unit mapping (CUET topics such as "Rural-Urban Linkages", "Social Reform Movements and Laws", "Land Reforms, Green Revolution" need to point at chapters). |

Target shape:

| Unit | Chapter | NCERT | CUET unit | in CUET | in CBSE 2026-27 exam |
|---|---|---|---|---|---|
| Indian Society | Introducing Indian Society | IS Ch 1 | — | no | non-evaluative |
| | The Demographic Structure of the Indian Society | IS Ch 2 | IS-I | yes | yes |
| | Social Institutions: Continuity and Change | IS Ch 3 | IS-II | yes | yes |
| | The Market as a Social Institution | IS Ch 4 | IS-II | yes | no |
| | Patterns of Social Inequality and Exclusion | IS Ch 5 | IS-III | yes | yes |
| | The Challenges of Cultural Diversity | IS Ch 6 | IS-IV | yes | yes |
| Social Change and Development in India | Structural Change | SCDI Ch 1 (CBSE 8) | CD-I | yes | yes |
| | Cultural Change | SCDI Ch 2 (9) | CD-I | yes | yes |
| | The Story of Indian Democracy | SCDI Ch 3 (10) | CD-II | yes | no |
| | Change and Development in Rural Society | SCDI Ch 4 (11) | CD-III | yes | yes |
| | Change and Development in Industrial Society | SCDI Ch 5 (12) | CD-III | yes | yes |
| | Globalisation and Social Change | SCDI Ch 6 (13) | CD-IV | yes | no |
| | Mass Media and Communications | SCDI Ch 7 (14) | CD-IV | yes | no |
| | Social Movements | SCDI Ch 8 (15) | CD-V | yes | yes |

### 15. Computer Science / Informatics Practices (CUET 308) — H 2, M 6, L 2

CUET 2026: Section A (common: Database Concepts, SQL I, SQL II, Computer Networks), then **either** B1 Computer Science (Exception and File Handling in Python, Stack, Queue, Searching incl. hashing, Sorting, Understanding Data, Database Concepts, SQL, Computer Networks, Data Communication, Security Aspects) **or** B2 Informatics Practices (Database Query using SQL, Data Handling using Pandas I and II, Plotting with Matplotlib, Introduction to Computer Networks, Societal Impacts, Project Based Learning). B1 follows the NCERT Class 12 CS book (13 chapters: Exception Handling in Python, File Handling in Python, Stack, Queue, Sorting, Searching, Understanding Data, Database Concepts, Structured Query Language, Computer Networks, Data Communication, Security Aspects, Project Based Learning; source Shaalaa/IndCareer). CBSE 083 Class 12 (2026-27) differs: Python revision, functions, exception handling, text/binary/CSV files, stack, networks, SQL, Python-SQL interface; no queue, sorting, searching, understanding data. Boolean logic is CBSE CS **Class 11** Unit 1.

| ID | Sev | Defect |
|---|---|---|
| CS-H1 | HIGH | `Boolean Algebra` taught: not in CUET 2026, not in NCERT CS 12, not in CBSE 083 Class 12 (Class 11 only). |
| CS-H2 | HIGH | B1 (CS) and B2 (IP) chapters are in one pool with no stream field. A CS student gets Pandas, Matplotlib and Societal Impacts questions; an IP student gets Stack, Queue and Sorting. |
| CS-M1 | MEDIUM | `Communication Technologies`: not a CUET or NCERT title; near-duplicate of `Data Communication` (NCERT CS Ch 11). |
| CS-M2 | MEDIUM | Duplicate: `File Handling` vs `Exception and File Handling in Python`. |
| CS-M3 | MEDIUM | Duplicate: `Data Structures` vs `Stack` / `Queue`. |
| CS-M4 | MEDIUM | Duplicate: `MySQL` vs `Structured Query Language`. |
| CS-M5 | MEDIUM | `Python Revision`, `Functions`, `Interface Python with MySQL` are CBSE 083 board topics, not CUET 2026 topics. Keep only as "board only" or remove from CUET mocks. |
| CS-M6 | MEDIUM | IP chapters missing or merged: `Database Query using SQL` (NCERT IP Ch 1 "Querying and SQL Functions", **unverified** title), `Introduction to Computer Networks` (IP networks/web chapter, different from CS networks), and `Data Handling using Pandas` should be I and II (CUET lists them separately). |
| CS-L1 | LOW | NCERT order is Sorting (Ch 5) then Searching (Ch 6); ours is reversed. |
| CS-L2 | LOW | `Project Based Learning` is only under B2; it is also NCERT CS Ch 13 but not a CUET B1 topic, so B2-only is acceptable. Subject display name is long; consider "Computer Science / IP" with a stream picker. |

Target shape:

| Unit | Chapter | NCERT | CUET | in CUET | in NCERT |
|---|---|---|---|---|---|
| Section A: Databases and Networks (both streams) | Database Concepts | CS Ch 8 | A-1, B1-7 | yes | yes |
| | Structured Query Language (SQL I and II) | CS Ch 9; IP Ch 1 | A-2, A-3, B1-8 | yes | yes |
| | Computer Networks | CS Ch 10 | A-4, B1-9 | yes | yes |
| Section B1: Computer Science | Exception and File Handling in Python | CS Ch 1-2 | B1-1 | yes | yes |
| | Stack | CS Ch 3 | B1-2 | yes | yes |
| | Queue | CS Ch 4 | B1-3 | yes | yes |
| | Sorting | CS Ch 5 | B1-5 | yes | yes |
| | Searching | CS Ch 6 | B1-4 | yes | yes |
| | Understanding Data | CS Ch 7 | B1-6 | yes | yes |
| | Data Communication | CS Ch 11 | B1-10 | yes | yes |
| | Security Aspects | CS Ch 12 | B1-11 | yes | yes |
| Section B2: Informatics Practices | Database Query using SQL | IP Ch 1 (unverified) | B2-1 | yes | yes |
| | Data Handling using Pandas – I | IP Ch 2 (unverified) | B2-2 | yes | yes |
| | Data Handling using Pandas – II | IP Ch 3 (unverified) | B2-3 | yes | yes |
| | Plotting Data using Matplotlib | IP Ch 4 (unverified) | B2-4 | yes | yes |
| | Introduction to Computer Networks | IP Ch 5 (unverified) | B2-5 | yes | yes |
| | Societal Impacts | IP Ch 6 (unverified) | B2-6 | yes | yes |
| | Project Based Learning | IP Ch 7 (unverified) | B2-7 | yes | yes |
| (board only, not CUET) | Python Revision; Functions; Interface Python with MySQL | CBSE 083 | — | no | CBSE yes |
| (retired) | Boolean Algebra; Communication Technologies | — | — | no | no |

## Defect counts

| Subject | HIGH | MEDIUM | LOW |
|---|---|---|---|
| English | 0 | 1 | 3 |
| GAT | 0 | 2 | 2 |
| Accountancy | 0 | 5 | 5 |
| Economics | 1 | 5 | 5 |
| Business Studies | 1 | 3 | 2 |
| Mathematics | 1 | 2 | 3 |
| Physics | 1 | 1 | 2 |
| Chemistry | 6 | 2 | 3 |
| Biology | 2 | 0 | 2 |
| History | 2 | 0 | 2 |
| Political Science | 3 | 2 | 1 |
| Geography | 3 | 4 | 3 |
| Psychology | 2 | 1 | 1 |
| Sociology | 0 | 3 | 2 |
| Computer Science / IP | 2 | 6 | 2 |
| **Total** | **24** | **37** | **38** |

Plus cross-cutting X1-X5 (3 MEDIUM, 2 LOW).

## Migration: rename without breaking tagged questions

Chapter strings are load-bearing: `questions.chapter` is free text, `isValidTopSyllabusPair` / `getCanonicalUnitForChapter` gate the question upload API (`src/app/api/questions/*`), practice sessions, the NTA selector and ~20 pipeline scripts; the Flutter app and `cuet_chapter_priorities.json` carry names too. So:

1. **One alias source.** Export from `canonical_syllabus.js`:
   - `CHAPTER_ALIASES[subject][oldName] = newName` (renames and merges),
   - `RETIRED_CHAPTERS[subject][name] = { reason: 'deleted_from_ncert' | 'not_in_cuet' | 'board_only', since: '2026-27' }`,
   - `resolveChapter(subject, name)` returning `{ chapter, retired, reason }`.
   Make `isValidTopSyllabusPair`, the upload API and `factoryEvidence.sameChapter` call `resolveChapter`, so old names are accepted on read and written back as new names. Fold `pyq_anchors.js` LEGACY_CHAPTER_MAP and the factoryEvidence alias into it.
2. **Stable keys.** Give every chapter a slug id (`physics.ch14_semiconductor_electronics`) and keep the display title separate, so future NCERT renames are a label change.
3. **DB migration (no deletes).** New `chapter_aliases(subject_id, old_name, new_name, kind)` table seeded from the JS map; `update questions set chapter = new where (subject, chapter) in aliases and kind in ('rename','merge')`; rename `chapters` rows in place (keep ids); for retired chapters set a flag (e.g. `chapters.retired_reason`, `questions.syllabus_status = 'out_of_syllabus'`) and exclude them from practice, mocks and priorities. Keep attempts and stats; read them through the alias view so past performance follows the new name.
4. **Splits need review, not a blind rename.** `Resources & Development` → Land / Water / Mineral and Energy / Planning; `Transport & Communication` and `International Trade` → World vs India; `Data Handling using Pandas` → I / II; `Data Structures` → Stack / Queue; `Analysis of Financial Statements` + `Comparative & Common Size Statements` (merge). Default to one target with `needs_retag = true`, then re-tag by keyword or a cheap classifier pass (owner approval needed for any paid run).
5. **Retired questions: re-tag before hiding where content survives.** e.g. some `Manufacturing Industries` questions fit `Secondary Activities`; `Migration` questions on rural-urban migration fit `Geographical Perspective on Selected Issues and Problems`; `Cold War Era` items on Soviet collapse fit `The End of Bipolarity`. Everything else stays stored but unserved.
6. **Update every name consumer in the same change**: `cuet_chapter_priorities.json`, `subjects.js` legacy lists, `cuet_top_route_audit.json`, Flutter `chapter_order.dart` / `warmup_pool.dart`, migration seed for `units`.
7. **Add fields** per chapter: `ncert_ref` (book, chapter), `cuet_unit`, `in_cuet`, `in_board`, `class_level` (11/12), `stream` (Maths B1/B2, CS B1/B2, Accountancy AFS/CAS). Use them for "CUET only", "Class 11", "only if you chose IP" labels and for stream filtering in mock selection.

### Alias map (old → new)

Renames and merges (`kind: rename` unless noted):

| Subject | Old | New |
|---|---|---|
| english | Para Jumbles | Rearranging the Parts (Para Jumbles) |
| english | Correct Word Usage | Choosing the Correct Word |
| english | Vocabulary | Synonyms and Antonyms |
| english | Grammar (legacy) | Choosing the Correct Word |
| gat | Basic Mathematical Concepts | Quantitative Reasoning (merge) |
| gat | Statistical Data Analysis | Quantitative Reasoning (merge) |
| gat | Logical & Analytical Reasoning | Logical and Analytical Reasoning |
| gat | Quantitative Aptitude / Logical Reasoning / GK (legacy) | Quantitative Reasoning / Logical and Analytical Reasoning / General Knowledge |
| accountancy | Partnership Fundamentals, Partnership (legacy) | Accounting for Partnership: Basic Concepts |
| accountancy | Profit & Loss Appropriation Account | Accounting for Partnership: Basic Concepts (merge) |
| accountancy | Goodwill Valuation | Goodwill: Nature and Valuation |
| accountancy | Admission of Partner | Admission of a Partner |
| accountancy | Retirement & Death of Partner | Retirement and Death of a Partner |
| accountancy | Dissolution of Partnership | Dissolution of Partnership Firm (merge) |
| accountancy | Share Capital | Accounting for Share Capital |
| accountancy | Debentures | Issue of Debentures |
| accountancy | Financial Statements of Company | Financial Statements of a Company |
| accountancy | Comparative & Common Size Statements | Analysis of Financial Statements (merge) |
| accountancy | Computerised Accounting System / Computerized Accounting System | Computerised Accounting System (pick one spelling) |
| economics | Introduction & Theory of Consumer Behaviour | Introduction and Theory of Consumer Behaviour |
| economics | Production & Costs | Production and Costs |
| economics | Theory of Firms under Perfect Competition | The Theory of the Firm under Perfect Competition |
| economics | Market Equilibrium & Simple Applications | Market Equilibrium and Simple Applications |
| economics | National Income & Related Aggregates, National Income (legacy) | National Income and Related Aggregates |
| economics | Money & Banking | Money and Banking |
| economics | Income Determination | Determination of Income and Employment |
| economics | Government Budget & the Economy | Government Budget and the Economy |
| economics | Balance of Payments | Open Economy Macroeconomics (Balance of Payments) |
| economics | Indian Economic Development 1950–1990 | Indian Economy 1950–1990 |
| economics | Economic Reforms Since 1991 | Liberalisation, Privatisation and Globalisation: An Appraisal |
| economics | Human Capital Formation | Human Capital Formation in India |
| economics | Employment | Employment: Growth, Informalisation and Other Issues |
| economics | Environment & Sustainable Development | Environment and Sustainable Development |
| economics | Development Experiences of India | Comparative Development Experiences of India and its Neighbours |
| business_studies | Nature & Significance of Management, Management (legacy) | Nature and Significance of Management |
| mathematics | Relations & Functions | Relations and Functions |
| mathematics | Continuity & Differentiability | Continuity and Differentiability |
| physics | every "X & Y" chapter | "X and Y" (e.g. Moving Charges and Magnetism) |
| physics | Semiconductor Electronics | Semiconductor Electronics: Materials, Devices and Simple Circuits |
| chemistry | d- and f-Block Elements | The d- and f-Block Elements |
| chemistry | Haloalkanes & Haloarenes; Alcohols, Phenols & Ethers; Aldehydes, Ketones & Carboxylic Acids | "and" forms |
| biology | Principles of Inheritance & Variation; Human Health & Disease; Biotechnology Principles & Processes; Biotechnology & its Applications; Organisms & Populations; Biodiversity & Conservation | NCERT "and" forms; "Biotechnology: Principles and Processes" |
| history | Bricks, Beads & Bones … Framing the Constitution (12) | NCERT titles with subtitles (table above); "Mahatma Gandhi & the Nationalist Movement" → "Mahatma Gandhi and the Nationalist Movement"; "An Imperial Capital — Vijayanagara" → "An Imperial Capital: Vijayanagara" |
| political_science | Alternative Centres of Power | Contemporary Centres of Power |
| political_science | End of Bipolarity | The End of Bipolarity |
| political_science | Democratic Upsurge and Coalition Politics | Recent Developments in Indian Politics (merge) |
| political_science | Recent Issues and Challenges | Recent Developments in Indian Politics (merge) |
| political_science | Crisis of the Democratic Order | The Crisis of Democratic Order |
| political_science | Challenges to & Restoration of the Congress System | Challenges to and Restoration of the Congress System |
| political_science | Environment & Natural Resources | Environment and Natural Resources |
| geography | Human Geography — Nature & Scope | Human Geography: Nature and Scope |
| geography | Population — Distribution, Density, Growth | The World Population: Distribution, Density and Growth |
| geography | India — People & Economy | Population: Distribution, Density, Growth and Composition |
| geography | Tertiary & Quaternary Activities | Tertiary and Quaternary Activities |
| geography | Transport & Communication | Transport and Communication (World) **split** with (India) |
| geography | International Trade | International Trade (World) **split** with (India) |
| geography | Resources & Development | Land Resources and Agriculture / Water Resources / Mineral and Energy Resources **split** |
| geography | Planning & Sustainable Development | Planning and Sustainable Development in Indian Context |
| psychology | Self & Personality; Attitude & Social Cognition; Social Influence & Group Processes | "and" forms |
| sociology | Demographic Structure | The Demographic Structure of the Indian Society |
| sociology | Social Institutions | Social Institutions: Continuity and Change |
| sociology | Patterns of Social Inequality | Patterns of Social Inequality and Exclusion |
| sociology | Challenges of Cultural Diversity | The Challenges of Cultural Diversity |
| sociology | Market as a Social Institution | The Market as a Social Institution (also move unit) |
| sociology | Story of Indian Democracy | The Story of Indian Democracy |
| sociology | Change & Development in Rural/Industrial Society; Globalisation & Social Change; Mass Media & Communications | "and" forms |
| computer_science | File Handling | Exception and File Handling in Python (merge) |
| computer_science | Data Structures | Stack / Queue **split** |
| computer_science | MySQL | Structured Query Language (merge) |
| computer_science | Communication Technologies | Data Communication (merge, after review) |
| computer_science | Data Handling using Pandas | Data Handling using Pandas – I / – II **split** |

Retire (keep stored, do not serve; re-tag individual questions first where noted):

| Subject | Chapter | Reason |
|---|---|---|
| economics | Infrastructure | deleted from NCERT; not in CUET |
| business_studies | Entrepreneurship Development | not Class 12; not in CUET |
| physics | Communication Systems | deleted |
| chemistry | Solid State; p-Block Elements | deleted from Class 12 |
| chemistry | Surface Chemistry; Isolation of Elements; Polymers; Chemistry in Everyday Life | CBSE formative-only; not in CUET |
| biology | Reproduction in Organisms | deleted |
| biology | Environmental Issues | CBSE formative-only; not in CUET |
| history | Kings & Chronicles; Partition | deleted |
| political_science | Cold War Era; US Hegemony in World Politics; Rise of Popular Movements | deleted (re-tag Soviet-collapse items to The End of Bipolarity) |
| geography | Manufacturing Industries (re-tag some to Secondary Activities); Migration (re-tag rural-urban items to Issues and Problems) | deleted / formative-only |
| psychology | Psychology & Life; Developing Psychological Skills | deleted |
| computer_science | Boolean Algebra | Class 11 only; not in CUET |
| computer_science | Python Revision; Functions; Interface Python with MySQL | board only (`board_only`, hide from CUET mocks) |

## Things I could not verify

- Exact NCERT tables of contents (ncert.nic.in unreadable): Accountancy Part I chapter 2/3 exact titles and where goodwill / change in PSR sit; Accountancy Part II titles; the CAS book chapters; Economics (Micro, Macro, IED) exact titles and the rationalised IED numbering; Maths chapter titles (standard, from memory); IP book chapter titles and numbers; Business Studies Ch 11 "Marketing" vs "Marketing Management"; Biology Ch 13 "Biodiversity and Conservation" vs CBSE's "Biodiversity and its Conservation"; whether Sociology Ch 4, 10, 13, 14 are still printed in the NCERT books.
- Whether Chemistry Biomolecules still covers hormones in the NCERT book (CUET does).
- How NTA handles Accountancy's "Optional to Unit V" (CAS) inside a no-choice paper.
- Live DB state of `public.chapters` and how many questions carry each old name (Supabase not queried, by instruction).
- CUET 2027 syllabus (not yet published) and whether new NCF-SE Class 12 textbooks change titles for 2027-28.
