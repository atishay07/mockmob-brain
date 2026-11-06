# Live question pools: syllabus-fit audit (31 Oct 2026)

A read-only audit of every live question in the five NCERT pilot subjects, against the CUET 2026 unit lists and the
NCERT text. Questions in retired chapters were skipped; the syllabus v2 migration handles them.

**Status:** nothing in production has changed. Every list here needs the owner's decision.
- **Per-question verdicts:** `pool-audit-2026-10-31/fit-*.json` (non-ok items only, each with a one-line why).
- **Brief:** `pool-audit-2026-10-31/FIT-AUDIT-BRIEF-2026-10-31.md`.

## Totals

| Subject (scope) | Examined | OK | Wrong chapter | Outside CUET 2026 | Not in NCERT | Flawed |
|---|---|---|---|---|---|---|
| Accountancy, partnership chapters | 460 | 282 | 161 | 2 | 1 | 14 |
| Accountancy, company accounts | 451 | 342 | 27 | 63 | 1 | 18 |
| Accountancy, analysis, cash flow and CAS | 494 | 324 | 147 | 10 | 8 | 5 |
| Business Studies | 411 | 291 | 85 | 27 | 5 | 3 |
| Economics | 454 | 350 | 35 | 53 | 11 | 5 |
| Biology (live chapters) | 354 | 268 | 28 | 39 | 17 | 2 |
| Political Science (live chapters) | 251 | 140 | 32 | 24 | 52 | 3 |
| **All** | **2,875** | **1,997 (69%)** | **515 (18%)** | **218 (8%)** | **95** | **50** |

## What stands out
1. **Accountancy is mostly a handful of templates.** Each of these is the same question again and again with new
   numbers or names, and every key checked correct:

   | Template | Copies |
   |---|---|
   | "Deed provides interest on capital @ x%" | 138 |
   | "Change the ratio to equal, goodwill X, sacrifice Y" (filed under Admission) | 114 |
   | Debenture "amount credited" | 131 |
   | Share Capital "securities premium" | 83 |
   | Quick Ratio sums (filed under Analysis of Financial Statements) | 130 |
   | Cash flow "operating profit before working capital changes" | 134 |
   | One cash-purchase voucher question with 5 software names (Computerised Accounting) | 119 |
   | **Total, about** | **849 of 1,405 live Accountancy questions** |

   This undercuts the "unlimited mocks" promise for Accountancy more than any other finding. A student meets the
   same question shape many times in one mock.
2. **Wrong chapter (515).** Most are template blocks filed under the wrong chapter: 130 Quick Ratio, 114 ratio-change,
   and 64 Business Studies items under "Nature & Significance of Management". They skew chapter state ("Needs work"
   on a chapter the student never practised) and practice by chapter.
   - **Caveat:** some agents judged from shortened stems. Check every move with the full text before applying it.
3. **Outside the CUET 2026 syllabus (218).**
   - **Accountancy:** debenture redemption, DRR and sinking fund (about 24), bonus and rights (13), conversion (6+9),
     buy-back (7).
   - **Economics:** externalities and policy tools (about 14), money-demand motives (about 9), preference theory
     (about 7).
   - **Biology:** plant tissue culture and breeding techniques (11).
   - **Political Science:** percentage arithmetic (12).
   - **Business Studies:** plan types (6) and span of management (5).
   - These stay in mocks today, although CUET 2026 will not ask them.
4. **Not decidable from NCERT (95).** Political Science has 52 of the 251, mostly Neighbourhood First, Look East,
   SAARC and generic environment items.
5. **Flawed (50).** Identical options, two right options, keys that contradict NCERT, a "1+1" test question. They
   overlap with the answer-key batches 1-3 (`answer-keys-2026-10-31/`), which hold fixes and exact undos for 19 of
   them.

## Suggested owner decisions (in order)
1. **Apply answer-key batches 1-3.** 19 questions: 4 key fixes, 7 rewords and 8 out of the pool. Each batch has
   `fix.sql` and `undo.sql`.
2. **Take the other flawed questions (about 31) out of the pools** (status `pending`), after a short fix-or-pull pass
   like batches 1-3.
3. **Outside-syllabus (218):** take them out of the pools, or keep them only outside NTA-pattern mocks.
   **Done 31 Oct (owner: "Pull them all"):** all 218 pulled on production, see `off-syllabus-2026-10-31/`.
4. **Wrong chapter (515):**
   - Check each move with the full text, then re-tag with the same mechanism as the syllabus v2 re-tag (code review
     L12 already keeps re-tagged questions eligible).
   - The 244 template moves (Quick Ratio, ratio change) are safe in bulk.
5. **Templates:**
   - **Done in code (eb70694c5):** the practice and mock picker takes at most 2 copies of one template stem per paper.
     It folds names, amounts and rates, and fills with more copies only when the pool has nothing else. NTA mocks use
     their own engine and need signed evidence, which these template rows do not have.
   - The real cure is more distinct Accountancy questions. Write them only when the owner asks.
