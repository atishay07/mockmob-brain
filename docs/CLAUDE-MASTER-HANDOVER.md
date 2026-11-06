# MockMob → Claude master implementation handover

**Date:** 2 October 2026  
**Role:** You are the implementing Claude workhorse for MockMob.  
**Source of truth:** this handoff plus `AGENTS.md`, `PRODUCT.md`, `DESIGN.md`,
and `docs/brain/ROADMAP-2027.md`. The approved roadmap wins over older project
brain prose. The companion evidence audit is
`docs/brain/ROADMAP-GAP-AUDIT-2026-10-02.md`.

## Mission

Turn MockMob into a truthful CUET UG 2027 practice product whose flagship is
**Score Recovery Lab**:

> Find the mistaken reasoning, repair the missing step, and check whether it
> survives genuinely fresh questions later.

The student journey stays inside the existing product shell:

`practice → investigate a mistake → repair the reasoning → immediate fresh
application → delayed check after at least 24 hours → delayed check around 72
hours → maintenance check around 7 days`.

Keep the existing Night Arena identity, ordinary Quick/Full/Smart/NTA practice,
Review, Progress, Radar, DU tools, saved questions and purchased access. Connect
them to one server learning record. Do not add another dashboard or a second
planner. Do not ship a card carousel or a static demo in place of the workflow.

The future commercial target is **MockMob CUET 2027, ₹299 once through 31 July
2027**. This is a gated hypothesis. Existing ₹99 CUET 2027 customers keep their
rights and expiry. The new offer must remain disabled until the release gates
below pass.

## Non-negotiable rules

1. Read the named product/brain files and inspect current changes before editing.
   Preserve user edits and the existing Next.js/Supabase stack. Read the installed
   Next guide before framework changes and Supabase guidance before schema work.
2. Never run a production migration, publish/quarantine application, deployment,
   checkout, refund, purchase, or paid generation implicitly. Save migration,
   dry-run, and rollback artifacts first.
3. Preserve Razorpay plan IDs, captured-payment/signature/owner/amount checks,
   historical ₹99 orders, ordinary credit RPCs, existing balances and purchased
   AI wallets.
4. Core diagnosis, repair, scheduling and scoring require zero paid model calls.
   Keep content calibration at the authorized $2 allowance within the $10 lifetime
   ceiling. Runtime funding is separate and not authorized by this task.
5. Unknown evidence, source, price, inventory, schema or provider state means
   quarantine or a useful unavailable state. Never turn uncertainty into a number,
   a fake free balance, a chance band, a mastery percentage or a human-review
   promise.
6. An incorrect answer creates a hypothesis, not a psychological label. Use no
   more than three probes, choose the next probe with an explicit diagnostic
   matrix, require two supporting observations from distinct families, and abstain
   on conflicting evidence.
7. Assisted work, repeated questions, and explanations do not establish transfer.
   Only independent fresh families can pass an immediate or delayed check. Never
   claim “mastered,” “permanently fixed,” “recovered marks,” or causal improvement
   from this evidence.
8. Use append-only observations and versioned projections. Changed/quarantined
   evidence invalidates derived claims without overwriting historical attempts.
9. Keep a single server-generated next action for Today, Radar, results and
   PrepOS. Priority is active session, overdue fresh check, unfinished repair,
   repeated supported miss, baseline, then ordinary practice. Offer 10/20/30
   minutes and one primary action plus at most two alternatives.

## First response and working method

Before changing behavior:

1. Read `AGENTS.md`, root `PRODUCT.md`, root `DESIGN.md`, and every linked brain
   file. Read `docs/brain/ROADMAP-GAP-AUDIT-2026-10-02.md` and inspect current
   `git diff`; do not reset or discard existing work.
2. Run a source inventory of Arena, AppLayout, Today, Practice, Review, Progress,
   Radar, results, PrepOS, wallet/credit services, capability registry, syllabus,
   pipeline, payments and migrations. Trace the active component call graph before
   removing `MockMobAssistant.jsx` or any old path.
3. Save a dependency-ordered checklist in `docs/brain/CLAUDE-WORKLOG.md` or the
   project brain, explicitly marking older pilot, fast-lane, peer-review,
   admission-prediction, invented-count, and competing-planner promises as
   superseded. Do not merely add a new header while leaving contradictory active
   instructions.
4. Update `docs/brain/STATUS.md` after each stage with implemented behavior,
   commands/results, browser/device flows actually exercised, remaining content
   and deployment gates, migrations/rollback, and the next incomplete criterion.

Work in dependency order. A page that advertises an unimplemented pathway is not
progress toward the definition of done.

## Stage A — Arena and capability truth (do this immediately)

### 1. One capability contract

Create or finish the central capability registry consumed by public copy,
navigation, subject selectors, Today, Arena mode launchers, pricing and PrepOS.
Each entry has: stable capability ID/version, availability state, supported
official subject codes, entitlement requirement, inventory policy, and an
actionable unavailable reason. Distinguish ordinary inventory, recovery-eligible
inventory, original sample content and verified historical exam material.

The server returns a single eligibility/quote object for a launch: entitlement,
allowance, credit cost, duration, inventory, expiry, reason and idempotency token.
The client renders that object and never gates or enables a launch from a guessed
credit number. Genuine zero is zero; unknown is unavailable; stale data is
labelled stale.

### 2. Fix Arena themes and layout

Add semantic app-shell tokens for light and dark modes, render the theme control
where Arena users can reach it, and persist the existing preference without
flashing or breaking the marketing theme. Audit all Arena/dashboard/Practice/
Review/Progress/Account/Tools states in both themes. Fix hard-coded zinc/white
portals, modal surfaces, charts, forms and focus rings. Preserve the visual Night
Arena style in dark mode and make light mode intentional, readable and calm.

Keep the NTA strict exam console as its own conventional skin. Do not globally
apply marketing tokens to it. Test keyboard focus, selected/pressed/disabled,
error, loading, empty, unavailable and modal states at 320px, 375px, 768px,
1024px, 1280px and a wide desktop. Verify no horizontal overflow and no layout
shift on answer selection. Use the static detector report as a review list; do
not mechanically “fix” intentional grid, typography or radius choices.

### 3. Make Arena copy and subjects truthful

Remove “Fast lane active” and old internal development language. Use CUET UG 2027
and the supported launch subjects. Replace “highest-quality” or similar free-versus-
premium quality implications with the actual selection/entitlement benefit.

Keep historic stored subjects, but normalize labels to stable official codes with
an explicit version crosswalk. An unsupported stale selection must show a useful
edit/recheck state and cannot launch a broken session. Do not claim that an
aggregate question count supports every mode or recovery pathway.

Results must offer one supported investigation or a useful ordinary Review state.
Today must show the server reason and duration contract. PrepOS must consume this
same plan.

## Stage B — repair PrepOS and the wallet before any paid AI work

### 1. PrepOS is an explanation layer

Remove or isolate local mission/calendar generation in `MockMobAIHub.jsx` after
tracing its active callers. `buildMission`, `buildDailyPlan`, setup-profile
planning and benchmark/credit copy must not create a competing study schedule or
entitlement. PrepOS can explain evidence, summarize the server plan, and link to
the next action. Use the same 10/20/30-minute choices as Today. The initial setup
must be optional contextual guidance, not an interrupting planner.

Replace stale DU wording such as broad “college and course direction” with sourced
eligibility and historical cutoff comparison, including year, round and category.
Do not infer admission probability or convert uncalibrated mock marks into an
official score.

### 2. Define wallet state explicitly

The wallet API must return a state such as `available`, `empty`, `paused`,
`schema_unavailable` or `error`, plus a safe display message. A missing table or
read failure must never return a synthetic monthly balance and must never be
rendered as a spendable zero. Keep a student’s real stored balances visible when
the schema is healthy.

Make `GET /api/ai/credits` one coherent read. It must not call a read function
that inserts/reset state, and it must not read the wallet twice through usage
snapshot composition. Separate normal practice credits from the PrepOS AI wallet.
Use one centralized effective entitlement/expiry check.

Paid AI remains paused until staging proves all of this:

- reservation is durable and atomic (`reserved → executing → committed` or
  `released`);
- one stable operation/idempotency key survives every client/provider retry;
- provider request IDs and actual expenditure receipts are recorded separately
  from the student ledger;
- unknown model price or missing funding fails closed;
- unusable output/deterministic failure reverses the student reservation without
  erasing provider expenditure;
- concurrent requests cannot overspend included or bonus credits;
- ledger and balance changes commit in one transaction/RPC, with errors surfaced;
- a failed request never consumes student credits.

Do not reactivate the direct read-modify-write fallback. Preserve and use the
existing atomic credit RPC. The UI must say, “PrepOS paid features are temporarily
unavailable. Your credits have not been used,” when the route is paused or
degraded. Pack buttons must not look live when checkout is not wired. Preserve
historical purchased wallets and old plan IDs.

Add tests for expired entitlement, missing schema, stale cache, two concurrent
consumes, retry with the same key, provider timeout, deterministic fallback,
ledger insert failure, and account switching. Add a receipt/reconciliation report.

## Stage C — sessions, recovery and evidence integration

Extend the existing session infrastructure. Keep sealed ticket compatibility while
migrating new ordinary and recovery sessions to durable owner-bound records. Keep
scoring authority, content evidence and learning purpose separate.

Required API contracts:

- `GET /api/learning/plan`: primary action, alternatives, duration, availability,
  reason and evidence references.
- `POST /api/recovery/episodes`: owner-bound idempotent start/resume after
  entitlement and complete-inventory checks.
- `POST /api/recovery/episodes/:id/responses`: validated idempotent choice,
  numeric-step or evidence-span response; return only the next permitted step.
- Existing `/api/sessions`: scored practice and fresh-check submissions.
- Existing `/api/recovery`: ordinary mistake review separate from recovery claims.

The first baseline is a signal. It must seed a supported investigation without
pretending to diagnose a whole subject from five questions. Probe answers must not
leak matrices, hidden keys or future checks. Reserve full pathways before episode
creation. Exclude seen families before selection, including saved/explore/ordinary
exposure and author-owned content where policy requires. Missing inventory blocks
without charge or silent repeat.

Enforce episode states `investigating`, `repairing`, `immediate_check`,
`delayed_check_1`, `delayed_check_2`, `maintained`, `needs_repair`,
`blocked_content`, and `invalidated`. Immediate and delayed checks must be
unassisted, from fresh families, and idempotent. The first delayed check is at
least 24 hours after repair; the second is around 72 hours and at least 24 hours
after the first completed check. A failed check reopens the concept. Only two
passed delayed checks may show “Passed two fresh checks.”

Keep ordinary mistakes useful in Review even when they are not recovery evidence.
Record practice answer changes as event-level effects plus net first-to-final
effects, including beneficial changes; do not call a negative sum recoverable
marks. Defer the timed decision experiment until the core recovery gate passes.

## Stage D — authoritative syllabus and question pipeline

Begin this agenda in parallel with the Arena integration, but do not allow
unverified content into recovery.

1. Locate and cite the authoritative official CUET publication for the intended
   year. The 2026 NTA page is only the baseline checked on 2 October 2026; do not
   assume it is a 2027 specification. Record publication version, subject code,
   unit, topic, locator and permission/source identity.
2. Build one versioned registry: official subject codes and aliases, syllabus unit/
   topic/concept IDs, launch subjects, public catalog, ordinary inventory,
   historical exam material, and recovery coverage. Keep old IDs through a
   crosswalk; do not silently relabel old attempts.
3. Run a read-only audit of every question and produce a dry-run mapping report.
   Preserve source hash, original answer key, explanation, route, family, mapping
   decision, duplicate/near-duplicate signal, and quarantine reason. Classify
   wrong keys, mislabels, incomplete passages, tax/version drift, unofficial
   material and ambiguous mapping. Do not apply changes from the dry run.
4. Verify blueprint coverage by usable independent families, not row count. Fix
   the offline factory and validators so subject/chapter arguments cannot silently
   fall back to a default Economics route.
5. Author and independently key the eight initial pathways: Accountancy
   sacrificing/gaining ratios and revaluation; Economics national-income
   inclusions/exclusions and nominal/real values; Business Studies delegation/
   decentralisation and planning/controlling; English explicit statement/inference
   and main idea/supporting detail. Verify them against the registry first.
6. Each enabled concept needs at least six independent families plus diagnosis,
   repair, immediate, two delayed and maintenance inventory. Cosmetic numbers do
   not make a new transfer family. Use deterministic numerical solvers and
   approved text evidence spans; arbitrary free text must not receive confident
   academic grading.
7. Use independent held-out academic fixtures and boundary tests. Model agreement,
   software tests and generated examples do not establish truth. Keep uncertain
   candidates quarantined and preserve the existing $2/$10 budget ledger.

Empty source registry, paused calibration, empty pathways, or incomplete families
must keep the affected capability unavailable.

## Stage E — paid hardening and release

Keep Compass sourced and historical. Finish payment reconciliation, old pending
order verification, V2 offer mapping, captured-payment/signature/owner/amount
checks, webhook replay, refund/revocation and useful support references. Finish
correction-queue processing and automated report-triggered re-evaluation; edited or
quarantined content invalidates derived claims without rewriting attempt history.

Add persistent rate limits for authentication, paid AI and expensive endpoints.
Exercise account switching, network interruption, expiry, resume, concurrent
starts, duplicate completion, missing content, invalidated evidence and stale
inventory. Add keyboard, screen-reader, reduced-motion, both-theme and 320px
coverage plus a real budget Android constrained-connectivity check. Measure lab
performance before launch but do not call it field data; targets are p75 LCP ≤2.5s,
INP ≤200ms and CLS ≤0.1 once enough field data exists.

Use independent flags for session migration, recovery pathways, decision coaching
and new pricing. Rollback disables new starts/sales while retaining in-progress
completion, history and entitlements; never drop the new history tables.

Track baseline completion, investigation/repair and delayed-check completion,
fresh accuracy with sample sizes/attrition, blocked content and confirmed defects,
return after repair, free-workflow-to-purchase conversion, cost per completed
episode/student, payment failures and support. Describe cohorts; do not claim
causality from before/after scores.

## Required verification and handoff output

At each stage run the relevant existing suites, then add meaningful cases for
three-probe/conflicting diagnosis; numeric boundaries and text evidence;
repeated IDs/families; assisted answers; premature/failed delayed checks;
exhaustion without charge; correction invalidation; concurrent session/episode/
quota/payment/AI retries; old ₹99/new ₹299/pending orders/wallets; zero/stale/
unavailable inventory; expiry/network/account-switch/resume; and accessibility/
theme/mobile states. Use `npm.cmd` in PowerShell. Run at minimum, where relevant:

`npm.cmd run test:recovery`  
`npm.cmd run test:learning`  
existing NTA, answer-integrity, mock-selection, payment and DU suites  
`npm.cmd run lint`  
`npm.cmd run build`

Do not report a check as run unless it was actually run. Record browser routes and
states actually exercised. Update `docs/brain/STATUS.md` and the worklog with:
implemented behavior, exact commands/results, deployment/migration/rollback
requirements, content/source gates, and the next incomplete acceptance criterion.

## Definition of done

A new student can complete baseline → supported investigation → reasoning repair →
fresh application → two genuinely fresh delayed checks, restart safely, see why a
state is unavailable, and review ordinary mistakes. A returning student sees the
same next action in Today, Radar, results and PrepOS. A student can purchase the
clearly described product without broken access, hidden AI charges or unsupported
academic/admission claims. The system has source-backed, independently checked
content and a recoverable staging/payment trail.

A passing build, attractive homepage, populated feature list, or green software
fixture suite alone does not meet this definition.

## How to report back

When you finish a safe slice, report the files changed, behavior now real, tests
actually run, browser/device flows actually exercised, known limitations, and the
next gate. If blocked, disable the capability and record the exact missing source,
family, receipt, migration, budget or deployment prerequisite. Never bypass a gate
just to claim completion.
