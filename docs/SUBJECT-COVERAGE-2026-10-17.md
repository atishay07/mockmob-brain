# Subject coverage: decision, 17 Oct 2026

The owner asked whether the 15-20 subjects MockMob implements properly cover at least 80% of CUET UG students, and asked for a business decision. Research by a subagent (public NTA-derived data plus read-only production data); decision by the main session (Claude Opus 5.5, session cc0bf1af).

## Facts

**Public data.** Subject-wise registrations for 2026 come from Careers360 and Kollegeapply, 23-24 Jun 2026. Their row sums equal NTA's published totals.
- 15,68,867 candidates registered in 2026, for 67,56,327 paper registrations (about 4.3 papers each).
- Five papers dominate:

  | Paper | Share of candidates |
  |---|---|
  | English | 81% |
  | Chemistry | 61% |
  | GAT | 58% |
  | Physics | 58% |
  | Maths | 37% |

- Then:

  | Paper | Share of candidates |
  |---|---|
  | Biology | 35% |
  | Economics | 16% |
  | Business Studies | 15% |
  | Accountancy | 14% |
  | Political Science | 10% |
  | Hindi | 9.5% |

**Coverage by the 15 subjects we implement properly:**
- **Papers:** they cover 94.9% of all CUET paper registrations in 2026 (93.9% in 2025).
- **Candidates:** about 80% of candidates have every paper covered. The base-case range is 76-83%; the assumption-free bounds are 78-96%.

**Gaps by size:**
- Hindi: +8.7 points of candidate coverage. The bank has 10 questions.
- Physical Education: +4.2 points. 142 questions exist, but they are not verified.
- Agriculture: +2.3 points. 91 questions exist.

**Our list is out of date.** CUET removed Entrepreneurship, Teaching Aptitude, Legal Studies and Engineering Graphics in 2025, but our bank still holds them. 26 of our 41 subjects are bulk-published with no student evidence.

**Depth is the bigger risk:**
- Physics and Chemistry are 28% of all papers, yet their banks hold 301 and 376 questions: about 6-7 non-overlapping 50-question papers each.
- GAT (58% of candidates) has 227 questions, about 4 papers.
- Accountancy has 1,405 questions, about 28 papers.

**Our students skew commerce.** Accountancy, Business Studies and Economics are each chosen by 27-31% of our users, against 13-16% nationally. Science students choose Maths, Physics and Chemistry but rarely practise them:

| Subject | Chose it | Practised it |
|---|---|---|
| Maths | 284 | 27 |
| Physics | 345 | 28 |

## Decision

1. **Retire "41 subjects" everywhere.** The truthful claim is "full NTA-pattern mocks for the 15 subjects behind 19 of every 20 CUET papers (2026 NTA data)". Do not claim "80% of students" or "every subject".
2. **Stop offering the 4 subjects CUET dropped** in pickers and practice. Keep their rows; just don't show them. The other thin subjects stay reachable as practice but are never counted in claims. This is not a cut: they aren't CUET papers any more.
3. **Content investment order:**
   1. **Depth where the students are:** GAT, Physics, Chemistry, Maths and Biology, toward at least 600 verified questions each. That makes "as many mocks as you want" true for the largest audience, and fixes why science students choose us but don't practise.
   2. **Hindi** to at least 200 verified questions (+8.7 points).
   3. **Verify the Physical Education bank** (+4.2 points; mostly verification).
   4. **Agriculture** (+2.3 points).

   With Hindi and PE done, the claim becomes "the subjects behind 98 of every 100 CUET papers", and about 93% of candidates are fully covered.
4. **Do not build the long tail now.** The 16 other papers are each under 7,500 registrations, about 5% of papers in total.
5. **Funding:**
   - Authoring and verification run as Claude agents (Haiku authors and Sonnet verifies, the owner's routing). They follow the CUET-fit contract in docs/brain/QUALITY.md and never draw on the USD 50 content budget, of which USD 10.04 remains.
   - Publishing a new wave to production needs the owner's OK, as wave 1 did on 14 Oct.
   - The 542 missing explanations would cost about USD 0.72 at the measured authoring rate.

## Evidence

- The full research reply, with every source URL, was returned by the coverage-research subagent on 17 Oct around 12:55 am IST. The tables above are copied from it.
- The bank numbers come from production read-only SQL and from mockmob-next/tmp/wave-results/wf_1693fdcb-431-U-question-health.json.
