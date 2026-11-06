# Differentiator research and decision — 3–4 October 2026

Status: **recommendation, pending owner approval of the naming change in §8.** Everything else
here is consistent with ROADMAP-2027.md and narrows it; it does not loosen any evidence, budget,
entitlement or migration rule. Researched 3–4 October 2026 by Claude from public pages only.

## 0. How to read evidence labels

Every capability claim in the brain uses one of five levels, mirrored in code as
`EVIDENCE_LEVELS` / `DIFFERENTIATORS` in `data/capabilities.js`:

| Level | Meaning | Who can establish it |
| --- | --- | --- |
| Research hypothesis | We believe it would help students; no product evidence yet. | This record |
| Source implementation | Code/content exists locally and passes automated tests. | Tests, validators |
| Academic validation | An independent subject reviewer, or a calibrated cohort, confirms the content and mappings. | Not the author; not a model |
| Staging verification | Exercised against a named staging database and real authenticated accounts. | Saved staging report |
| Live availability | Deployed, switched on, and reachable by students. | Production check |

A later level never implies an earlier one. "Unverified" means this checkout cannot see it.

## 1. Question

Is Score Recovery Lab the right main differentiator before we invest further? Compare
**repair that holds**, **trustworthy practice** and **goal-aware preparation**, recommend one
primary advantage and at most two supporting capabilities, and define what would prove us wrong.

**Answer in one line:** keep the *mechanism* (diagnose → repair → fresh delayed checks) as the
primary bet, renamed and narrowed to "repair that holds", proven on one pathway before eight.
Trustworthy practice is its precondition and the first supporting capability; goal-aware
preparation is the second, in maintenance only. The "score recovery" framing should go.

## 2. Competitors: advertised, observed, unknown

Retrieved 3 October 2026. "Advertised" = the company's own page or listing says it. "Not
advertised" means only that the page did not say so — **not** that the feature is missing.

| Product | Advertised (primary source) | Observed / third-party | Unknown |
| --- | --- | --- | --- |
| [Preparoo](https://ug.preparoo.app/) | ₹2,499/subject, ₹5,499 all access; 100+ full mocks; 7,800+ topic questions; PYQs 2023–26; 7,300+ NCERT flashcards "with spaced repetition"; SWOT and chapter breakdowns; study-plan builder; "Ask Preparoo" AI copilot that explains answers and "where you went wrong" | — | How mistakes are diagnosed; whether any later check uses unseen questions; answer-key correction process |
| [AfterBoards](https://www.afterboards.in/cuet) | ₹249/subject (10 mocks + topic tests; English 25); "Deep Analytics" across multiple mocks; SWOT; adaptive topic tests; spaced-repetition vocabulary flashcards; "error-free" past papers; forums; DU course/cutoff eligibility | [Play listing](https://play.google.com/store/apps/details?id=in.afterboards.in) | Concept-level remediation; how "error-free" is verified |
| [CUETMOCK](https://cuetmock.com/) | Chapter/full mocks, PYQs, All India tests; "AI Assisted Mock Platform"; SWOT; DU Preference List with cutoff checking; mentorship with toppers; "Completely Original questions strictly based on NCERT" | — | Prices (on /plans); correction process |
| [Prepium](https://www.prepium.in/) | Page title: free CUET 2027 mocks, PYQs, daily practice. Page is script-rendered; little else was readable | SPEC.md (1 Oct) recorded custom practice and eligibility on this site | Nearly everything else: treat as unknown, not absent |
| SuperGrads (Toprankers) | Owner's own blog: AI doubt solver "bhAIya", AI performance dashboard incl. rank prediction, 20+ free / 200+ mocks, theory and 2,000+ questions per subject, small live batches ([Toprankers](https://www.toprankers.com/is-supergrads-good-for-cuet-preparation)) | Third-party review lists ₹5,000–₹42,197 courses ([AcademyCheck](https://academycheck.com/blog/supergrads-by-toprankers-cuet-coaching-complete-review-fees-success-rate)). supergrads.in did not resolve from this environment | Product behaviour behind the AI claims |
| [Career Launcher](https://www.careerlauncher.com/cuet/) | Online/classroom/self-paced coaching; free mocks and PYQs; free expert counselling; "Program Recommender"; DU CSAS guidance; "3000+ 100 percentiles since 2022" | — | Prices; analytics; remediation |
| Testbook | — | Both candidate CUET pages returned HTTP 500/404 on 3 Oct | **Everything.** No claim about Testbook is made here; re-fetch before relying on it |
| [DUBuddy](https://apps.apple.com/in/app/dubuddy-cuet-du-help-desk/id1634947249) | DU admission information; paid mock packages "aligned to the original NTA one"; "Connect with senior"; streaks; PYQs | 4.2★ / 245 ratings; a review complains of "too many errors in the answers" (one review, not a rate) | Content QA process |

**What the landscape shows.** Mocks, PYQs, chapter analytics/SWOT, AI explainers and DU
eligibility tools are table stakes: at least three competitors advertise each. Spaced repetition
is advertised for flashcards (Preparoo, AfterBoards), not for checking whether a repaired
*reasoning error* holds on unseen questions. Nobody we read advertises inspectable answer
provenance or correction history; several advertise "error-free" or "original" as an assertion.
Because absence of documentation proves nothing, the defensible reading is: **no competitor
publicly claims delayed, fresh-question verification of a specific reasoning repair.**

## 3. Student problems (evidence and its limits)

- **Repeated mistakes.** Coaching blogs prescribe manual "error logs", re-attempting wrong
  questions and tagging error types ([iQuanta](https://www.iquanta.in/blog/cuet-mock-analysis),
  [Drishti](https://www.drishticuet.com/strategy/top-10-mistakes-to-avoid-if-youre-reattempting-cuet-ug)).
  The problem is recognised; today's remedy is manual and repeats the *same* questions.
- **Unreliable answers.** NTA dropped 27, then one more, question from the CUET UG 2025 final key
  after expert review, and charges ₹200 per challenged question ([Careers360](https://news.careers360.com/cuet-ug-final-answer-key-2025-revised-nta-drops-28-questions-after-candidates-allege-errors-response-sheet-cuet-nta-nic-in/amp),
  [Scroll](https://scroll.in/announcements/1083612/cuet-ug-2025-provisional-answer-key-released-objection-window-open-till-june-20)).
  Students have complained about key errors since 2022. If the official key can be wrong,
  third-party mock keys can be too, and students have no way to inspect them.
- **Wasted revision time.** Rereading, highlighting and summarising rate low utility; practice
  testing and distributed practice rate high ([Dunlosky et al., 2013](https://www.psychologicalscience.org/news/releases/which-study-strategies-make-the-grade.html)).
  Refutation-style explanations show a moderate advantage against misconceptions (g ≈ 0.41 in one
  meta-analysis; [NSF PAR](https://par.nsf.gov/biblio/10629626)) — but in science topics;
  transfer to CUET Commerce is an **assumption** (A3).
- **Admission decisions.** Subject choice and DU eligibility matter, but the market is crowded
  and the data (DU Bulletin, CSAS cutoffs) is public.

**Research gap:** no student interviews or usage data were collected for this decision. Every
student-need statement above is a hypothesis about MockMob's users until the cohort data in §7.

## 4. The three advantages compared

| | Repair that holds | Trustworthy practice | Goal-aware preparation |
| --- | --- | --- | --- |
| Student benefit | Knows whether revision of a specific slip actually worked, on questions they have not seen | Can inspect where a key came from and see corrections; affected results are fixed automatically | Effort goes to subjects that matter for a realistic DU target |
| Existing alternatives | Manual error logs; flashcard spaced repetition; AI "where you went wrong" explainers | "Error-free"/"original" assertions; NTA challenge window | CUETMOCK preference list, AfterBoards eligibility, CL Program Recommender, DUBuddy, DU's own bulletin |
| Copying difficulty | Claim: easy. Working version: hard — needs validated misconception maps, reserved fresh families per concept, timing rules and outcome data accumulated over seasons | Hard to fake retroactively: history must exist from the start; a copy starts with no versioned record | Easy: public data, a weekend of work |
| Required assets | Permitted original content (≥6 families/concept), independent academic review, durable sessions, return behaviour | Versioned content hashes, correction log, recalculation queue (all saved locally), student-facing provenance UI (missing) | Parsed DU data (have), Combo Planner/Compass (have) |
| Costs | Authoring + review per concept (largest); zero runtime model cost | Mostly engineering; ongoing re-verification | Annual data refresh |
| Invalidating evidence | Students do not return for delayed checks; probe concordance low; delayed pass rates no better than first attempts; reviewers reject mappings | Students never open provenance; key errors are rare enough not to matter; trust does not move retention or conversion | Students choose subjects before arriving; tool use does not change practice behaviour |

**Useful feature vs defensible advantage.** Goal-aware preparation is *useful* and already built;
it is not defensible. Trustworthy practice is *defensible* (history compounds, copies start at zero)
but weak as a headline: every competitor already asserts accuracy, and students cannot tell the
difference before something goes wrong. Repair that holds is the only one that is both a reason to
choose MockMob *and* gets harder to copy with use — **if** students return for the checks.

## 5. Compounding, and its privacy limits

Three assets compound if collected lawfully:
1. **Permitted content** — original pathways with reserved fresh families. Each season adds families.
2. **Validated misconception mappings** — probe concordance (does the second probe agree with the
   first?) and delayed-check outcomes per hypothesis show which mappings are real.
   `data/recovery_metrics.js` computes concordance per pathway version.
3. **Intervention outcomes** — which repair version precedes held delayed checks.

**Privacy constraint (material, not legal advice).** Most CUET candidates are under 18. The DPDP
Act treats them as children: verifiable parental consent, and a prohibition on tracking or
behavioural monitoring of children, with exemptions limited to classes such as educational
institutions ([PIB explainer](https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251117695301.pdf)).
Most DPDP Rules obligations apply 18 months after the 13–14 November 2025 notification, i.e. from
about **13 May 2027 — inside the CUET 2027 season**. Whether a commercial test-prep service
qualifies for any exemption is unresolved (A6). Design consequences, adopted now:
- Outcome data serves the student's own learning first; cohort metrics are aggregates with groups
  under 5 suppressed (`MIN_REPORTABLE`), no advertising use, no sale.
- Prefer explicit, student-initiated checks over passive telemetry. Existing dwell/answer-change
  telemetry needs legal review before May 2027.
- Age and parental-consent onboarding is a launch prerequisite for 2027, not an afterthought.

## 6. Recommendation

- **Primary: Repair that holds.** One validated pathway first; expand only on evidence.
- **Supporting 1: Trustworthy practice**, scoped to what repair needs: versioned content hashes,
  automatic invalidation, correction history (all saved locally), then one student-facing
  "where this answer comes from" view. Without it a delayed check on a wrong key is meaningless.
- **Supporting 2: Goal-aware preparation**, maintenance only: Combo Planner and Compass stay; they
  may set which subject comes first in the shared plan; no new investment.

## 7. Validation plan (pre-registered)

Cohort: internal, then opted-in learners, one pathway (`sacrificing_gaining`), behind the existing
release gates. No decision below 30 started episodes (`MIN_DECISION_SAMPLE`). All rates are
descriptive with Wilson intervals; none is a causal effect.

| Metric (from `scripts/learning/recovery-metrics.mjs`) | Continue | Revisit | Stop / invalidate |
| --- | --- | --- | --- |
| Offer uptake: eligible learners who start | ≥ 25% | 15–25% | < 15% → demand hypothesis fails |
| Finished repair / started | ≥ 60% | 40–60% | < 40% → too long or unclear |
| Took delayed check 1 within 3 days of due / passed immediate | ≥ 50% | 30–50% | < 30% → "holds" cannot be shown; demote to supporting |
| Delayed check 2 pass rate (n ≥ 20) | ≥ 60% | 40–60% | < 40% → repair does not hold; rewrite before expanding |
| Probe concordance (n ≥ 30) | ≥ 70% | 50–70% | < 50% → mapping invalid; do not scale the matrix approach |
| Confirmed content defects | 0 | — | Any → automatic quarantine/invalidation, pause expansion until root-caused |
| Paid model calls in the core flow | 0 | — | Any → bug |

A causal claim ("repair improves marks") needs a randomised comparison (repair vs explanation-only),
designed and approved separately. Until then, copy may say only "passed two fresh checks".

**Expansion rule.** Pathway 2 starts only after pathway 1 has academic sign-off and meets "continue"
on uptake, return and concordance. Next candidate: Economics nominal/real values (solver-checkable),
before the conceptual and English evidence-span pathways.

## 8. Challenging Score Recovery Lab

Kept: diagnosis from wrong options, at most three probes, two-family support, abstention on
conflict, repair, unassisted fresh checks at ≥24h and ≥72h, failure reopening, invalidation.

Changed:
1. **Name and framing — decided by the owner on 4 October:** marketing "Score Recovery", feature
   "Score Recovery Lab", action "Mistake Repair" (PLAN-2026-10-04-NEXT-DAYS.md). Original proposal: "Score recovery" implies recovered marks, which
   the evidence rules forbid us to claim. Proposed user-facing name: **"Mistake Repair"**, promise
   "Fix the reasoning behind a repeated mistake — then prove it held on fresh questions." Internal
   module names stay. No public copy was changed in this round.
2. **One pathway before eight.** Eight parallel pathways spread authoring, review and cohort data
   too thin to learn anything. Stage 2 is now "one validated pathway, measured".
3. **Decision coaching** (time/answer-change analysis) is a useful feature inside results, not a
   differentiator: answer-change counts are easy to copy. Stays `not_released`.

Rejected ideas: positioning on question count; percentile/rank prediction; an AI copilot as the
differentiator (Preparoo and SuperGrads already advertise one, and model agreement is not truth);
admission probabilities; building all eight pathways before any cohort evidence; adding the
syllabus to `source_registry.json` (the paid worker treats an empty registry as a pause signal).

## 9. Assumptions

- A1 Students will return for a check 1–3 days later if the plan surfaces it (tested by §7 return).
- A2 Wrong options reveal stable reasoning patterns (tested by concordance).
- A3 Refutation-style repair transfers from science studies to Commerce concepts (needs cohort data).
- A4 An independent Accountancy reviewer can be engaged for a one-time pathway review; this is
  calibration, not routine per-question review, so it is consistent with "no routine human review".
- A5 The CUET 2027 Accountancy syllabus keeps sacrificing/gaining ratios (2026 syllabus verified).
- A6 DPDP obligations for under-18 learners apply to MockMob without an exemption (legal review).
- A7 Trust becomes visible to students only through an inspectable correction; we have no data yet.

## 10. Revisit triggers

A competitor advertises fresh-question verification of misconception repair; NTA publishes the
2027 syllabus (re-hash locator) or changes the pattern; legal review on DPDP; any "stop" threshold
in §7; academic reviewer rejects the mapping; owner changes pricing or audience; 1 March 2027 at the
latest (time to change course before the exam window).

## 11. What was implemented for this decision (4 October 2026)

| Item | Level reached |
| --- | --- |
| Candidate pathway `data/recovery_candidates/sacrificing_gaining.source.json` (3 probes, 5 repair steps, 6 checks, 14 families, 4 hypotheses) | Source implementation; academic validation **pending** |
| Validator `data/pathway_validation.js`, `npm run recovery:validate` — recomputes every key and matrix cell with exact fractions; 97/97 checks | Source implementation |
| Shared-plan facts (`learningPlan` → `primary.facts`), shown in PrepOS and the free record reply; model prompt told facts are authoritative | Source implementation |
| Metrics `data/recovery_metrics.js`, `scripts/learning/recovery-metrics.mjs` | Source implementation; configured database lacks `learning_episodes` (PGRST205) → **n = 0** |
| Evidence ladder + differentiators in `data/capabilities.js` | Source implementation |
| Staging seeding, signed evidence, registered digest, cohort | Not started |

Reports: `docs/brain/reports/pathway-sacrificing_gaining-validation.json`,
`recovery-metrics.json` (real, n = 0), `recovery-metrics-fixture.json` (simulated, labelled).

## Sources

Competitors: links in §2. Student problems and learning science: links in §3. Syllabus:
[NTA CUET UG 2026 syllabus index](https://cuet.nta.nic.in/cuetug-2026-syllabus/), Accountancy
(301) PDF SHA-256 `f67df11b2ba878944061e63169e075819a525535edb184508a093c230b9b72e7`, Unit II.
Privacy: [PIB DPDP explainer](https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251117695301.pdf),
[KS&K summary](https://ksandk.com/data-protection-and-data-privacy/childrens-data-protection-under-indias-dpdp-rules/).
