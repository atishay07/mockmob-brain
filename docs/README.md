> **Moved here on 6 Nov 2026.** This folder is now the copy that counts. The code repo's `docs/brain` is frozen.
> It holds both branches' docs. Where they differed, the newer version is kept here and the other is in `_branch-variants/`.
> Screenshots and data files over 200 KB stayed in the code repo, where scripts read them.

# MockMob project brain

Authority: the owner's approved implementation roadmap, 2026-10-02, narrowed by the
differentiator decision of 2026-10-03/04 (DECISION-2026-10-03-DIFFERENTIATOR.md).
Read PRODUCT.md for positioning, DESIGN.md for visual conventions, then the files below.

**Working plan (owner, 4 Oct): PLAN-2026-10-04-NEXT-DAYS.md** — Night 1 Score Recovery + AI,
Day 2 AI-verified error-free questions + NTA mode, then the Google Play app. Budgets: student AI
USD 25/IST month (DB-enforced), content generation USD 50 lifetime. Marketing name "Score Recovery";
feature "Score Recovery Lab"; action "Mistake Repair". Model choice: AI-MODEL-REPORT-2026-10-04.md.

**UI/UX execution plan (owner follow-up, 4 Oct): UI-UX-IMPLEMENTATION-PLAN-2026-10-04.md** —
phone performance, accessibility, stable layout, student states/error prevention and activation.
It narrows the UI audit priorities; owner-retained official-key trust wording is outside this sprint.
It does not replace the product working plan or change runtime/payment/evidence contracts.
**Local implementation evidence (4 Oct): UI-UX-IMPLEMENTATION-RESULTS-2026-10-04.md** —
implemented changes, 179 passing tests, responsive/state checks and remaining hardware/performance/deploy gates.

One direction: **repair that holds** is the primary bet (diagnose a reasoning slip, repair it,
check it later on unseen questions), proven on one pathway before eight. Trustworthy practice
supports it; goal-aware DU tools are maintained, not expanded. Label every claim with one
evidence level: research hypothesis → source implementation → academic validation → staging
verification → live availability (`EVIDENCE_LEVELS` / `DIFFERENTIATORS` in data/capabilities.js).

- DECISION-2026-10-03-DIFFERENTIATOR.md: dated competitor and student-need research, the three
  options compared, pre-registered validation thresholds, assumptions and revisit triggers.

- ROADMAP-2027.md: current product, packaging, stages and acceptance contract; takes precedence over older decisions.
- SPEC.md: retained evidence and architecture detail, subordinate to ROADMAP-2027.md.
- STATUS.md: implementation evidence and remaining work. Never confuse source shipped with production deployed.
- IMPLEMENTATION-2027.md: stage-by-stage completion checklist and the next executable acceptance gates.
- LEARNING-DEPLOYMENT.md: saved migrations, explicit staging order, switches and non-destructive rollback.
- QUALITY.md: publishing, source and budget rules.
- ARCHITECTURE.md: interfaces, storage, authentication and migration/rollback.
- COST-POLICY.md: reservation, usage receipts, route pauses and pricing setup.
- BENCHMARK.md: independent reference fixtures and release criteria.
- BACKLOG.md: ordered remaining implementation and launch work.
- BANK-AUDIT.md: read-only inventory and limits of historical failure evidence.
- DESIGN-REFERENCES.md: public reference catalogs and the patterns actually used.
- ROADMAP-GAP-AUDIT-2026-10-02.md: evidence audit comparing the GPT 6.1 Sol
  implementation with the approved roadmap, including Arena and PrepOS findings.
- CLAUDE-MASTER-HANDOVER.md: copy-ready implementation contract for the next
  Claude run; it supersedes older contradictory execution prompts.

The earlier human-review requirement is superseded. The system abstains when evidence
is insufficient. 10,000 questions for $10 and superiority over human review are not
established results. No fabricated counts, testimonials, selection or score guarantees.

## Delivery order
0. Reconcile capability truth and the project brain.
1. Unify sessions, allowances and owner-bound learning evidence.
2. Validate ONE complete pathway (sacrificing/gaining ratios), measure it, then expand.
3. Connect diagnosis, repair, fresh checks and the shared next action.
4. Harden payments, admissions, runtime costs and correction history.
5. Release behind independent flags; enable ₹299 only after all launch gates pass.

The earlier 40–80-question pilot and store delivery order are superseded by
ROADMAP-2027.md. Question count alone does not release a recovery pathway.

## Handoff rules
Every change records tests, deployment needs, rollback and uncertainty in STATUS.md.
Source registry updates must include permission, source version and locator.
Keep benchmark families disjoint from authoring examples. A generated fixture is a
software regression test, not an independently keyed academic benchmark.
