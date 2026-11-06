# Syllabus rulings, verified (31 Oct 2026)

**Basis:**
- The audit (`syllabus-audit.md`).
- A two-sided check of every HIGH defect, run as workflow `wf_c1916fd5-105` (24 verdict sets; the raw verdicts are in
  `verify.json` in this session's scratchpad). One side read the CUET 2026 PDF; the other read the NCERT Reprint
  2026-27 books and the CBSE 2026-27 curriculum.
- The owner's rule (D200): **one reference, the real CUET syllabus**. NCERT chapters are the unit of study, and each one
  sits clearly under its CUET unit.
- The owner's rule (D201): no "older syllabus" shelf.

## 1. The frame
- **Subject, then CUET unit (the exact CUET 2026 title), then NCERT chapter (the exact current NCERT title, book code
  and chapter number), then CUET sub-topics.**
- Where a CUET unit is a single NCERT chapter, the unit and the chapter share the title.
- Where CUET lists a topic that has no NCERT chapter, the chapter is the CUET unit itself. This covers Applied Maths B2,
  English and GAT.
- **Where CUET and NCERT titles differ, the CUET title leads** (it is the exam), and the NCERT title is shown as the book
  reference. Example: Political Science "Alternative Centres of Power" (CUET), with NCERT Ch 2 "Contemporary Centres of
  Power" as the reference.
- **Flags are keyed by exam year** (`cuet: { 2026: true }`). CUET 2027 has not been published. When NTA publishes it,
  re-run the audit and this check.

## 2. Sections and options (each student chooses; the choice filters questions, cards, chapter state and mocks)
- **Mathematics (319):**
  - A1 is common to everyone.
  - Then a choice of B1 Mathematics (NCERT core) or B2 Applied Mathematics.
  - These four chapters are B2 only: Numbers, Quantification and Numerical Applications; Time Based Data; Inferential
    Statistics; Financial Mathematics.
  - Probability Distributions: place it as the PDF does.
  - Default when the student has not chosen: B1.
- **Computer Science / Informatics Practices (308):**
  - Section A is common. Then a choice of B1 Computer Science or B2 Informatics Practices.
  - The PDF splits the sections but does not spell out the choice rule. Present it as "Pick B1 if you study Computer
    Science, B2 if Informatics Practices".
  - Default: B1.
- **Accountancy (301):** Computerised Accounting is CUET's alternative to Analysis of Financial Statements. The option is
  AFS (default) or CAS.
- The student picks once, on the subject page (one tap), and can change it later. There is no onboarding question.

## 3. Off-syllabus: leaves every student surface (stored, never served; `is_cuet_syllabus=false`)
All of these were confirmed absent from CUET 2026 by the CUET side of the check, and NCERT or CBSE agreed:

| Subject | Chapter | Live Qs | Re-tag first |
|---|---|---|---|
| Economics | Infrastructure | 12 | Colonial-infrastructure items go to Indian Economy on the Eve of Independence |
| Business Studies | Entrepreneurship Development | 11 | no |
| Physics | Communication Systems | 12 | no |
| Chemistry | Solid State, Surface Chemistry, Isolation of Elements, p-Block Elements, Polymers, Chemistry in Everyday Life | 75 | no |
| Biology | Reproduction in Organisms, Environmental Issues | 97 | Flowering-plant items go to Sexual Reproduction in Flowering Plants (the agent decides each item) |
| History | Kings and Chronicles, Partition | 20 | no |
| Political Science | Cold War Era, US Hegemony in World Politics, Rise of Popular Movements | 30 | Soviet-collapse items go to End of Bipolarity |
| Geography | Manufacturing Industries (India), Migration | 18 | World manufacturing goes to Secondary Activities; rural-urban migration goes to Geographical Perspective on Selected Issues and Problems |
| Psychology | Psychology and Life, Developing Psychological Skills | 22 | no |
| Computer Science | Boolean Algebra, Python Revision, Functions, Interface Python with MySQL | 40 | Items on functions or file handling that also fit a B1 chapter go to that chapter |

About 340 live questions in total. **Check every subject's mock pool after retiring them** (the unlimited-mocks
promise).

## 4. Kept: the audit was wrong here (CUET 2026 has them)
- **Political Science:**
  - "Alternative Centres of Power"
  - "Democratic Upsurge and Coalition Politics" and "Recent Issues and Challenges": CUET lists them separately, even
    though both read from NCERT "Recent Developments in Indian Politics"
  - "Era of One-Party Dominance"
- **Economics:** "Indian Economy on the Eve of Independence" stays. It is NCERT IED Ch 1 and a light CUET sub-topic.
- **Geography:** "Resources and Development" stays the CUET unit. It holds four NCERT chapters: Land Resources and
  Agriculture; Water Resources; Mineral and Energy Resources; Planning and Sustainable Development in Indian Context.
  Existing "Resources & Development" questions are re-tagged into these four. Where the agent is unsure of a
  question, it stays untagged and counts toward no chapter.

## 5. Merges and renames (old name becomes the alias)
- **Accountancy:**
  - "Dissolution of Partnership" goes to "Dissolution of Partnership Firm".
  - "Computerized" and "Computerised" become one chapter, "Computerised Accounting System".
- **Economics:**
  - "National Income & Related Aggregates" and "National Income Accounting" become one chapter.
  - "Income Determination" goes to "Determination of Income and Employment".
  - Use the CUET unit titles where they exist.
- **Business Studies:**
  - CUET unit "Business Finance", NCERT chapter "Financial Management". The empty "Business Finance" chapter row merges
    into it.
  - CUET unit "Marketing", NCERT chapter "Marketing". "Marketing Management" becomes the alias.
- **Mathematics:** "Vector Algebra" and "Vectors" become one chapter, "Vector Algebra" (NCERT).
- **Physics:** "Semiconductor Electronics" and "Electronic Devices" become one chapter, "Semiconductor Electronics:
  Materials, Devices and Simple Circuits".
- **Chemistry:** "d- and f-Block Elements" and "d and f Block Elements" become one chapter, "The d- and f-Block
  Elements".
- **Computer Science:**
  - "File Handling" goes to "File Handling in Python".
  - "MySQL" goes to "Structured Query Language (SQL)".
  - "Data Structures" is split into "Stack" and "Queue" (re-tag each item).
  - "Communication Technologies" goes to "Data Communication" (after review).
  - Use the NCERT CS XII titles: 1 Exception Handling in Python, 2 File Handling in Python, 3 Stack, 4 Queue, 5 Sorting,
    6 Searching, 7 Understanding Data, 8 Database Concepts, 9 Structured Query Language (SQL), 10 Computer Networks,
    11 Data Communication, 12 Security Aspects, 13 Project Based Learning.
- **Sociology:**
  - "Story of Indian Democracy" becomes NCERT "The Constitution and Social Change", under the CUET unit "Social Change
    and the Polity".
  - "The Market as a Social Institution" moves to the Indian Society book, as Ch 4.
  - "Mass Media & Communications" sits under the CUET topic "Media and Social Change".
- **Cosmetic "&" vs "and": change only the display title.** The stored chapter key stays, so app version 16 keeps
  working.
- `cuet_chapter_priorities.json` is rewritten with canonical names. 8 of its 10 subjects use names that do not exist
  today.

## 6. Labels (only where they reduce confusion; at most one chip per chapter)
- **"CUET only":** in CUET 2026, but not in the CBSE 2026-27 board exam. This covers the four Sociology chapters, and the
  CS B1 chapters that are not in CBSE 083.
- **"Class 11 book":** Economics Introductory Microeconomics is examined by CBSE in Class 11, but CUET tests it. (NCERT
  prints the book as Class XII, so the chip text reads "CBSE teaches this in Class 11".)
- Nothing else, and no shelf of old chapters.
