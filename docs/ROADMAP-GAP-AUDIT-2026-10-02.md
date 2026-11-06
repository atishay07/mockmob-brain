# Roadmap to GPT 6.1 Sol handoff audit

Date: 2 October 2026. This is a read-only audit of the implementation left by
GPT 6.1 Sol, followed by a handoff to Claude. It does not change product code,
run a migration, create a purchase, spend AI budget, or publish content.

## Executive finding

The implementation has a substantial server-side learning foundation: owner-bound
episodes, bounded diagnosis, response validation, family holds, delayed-check
states, shared-plan APIs, entitlement preservation, and a good set of software
tests. The product is still release-gated. The student-facing shell has not yet
become one coherent recovery product, and the Arena/PrepOS layers still expose
older assumptions.

The most urgent work is integration and truthfulness, in this order:

1. Make capability, inventory, quota, and wallet state server-owned and visible
   through one contract. A missing wallet schema must never look like a full
   balance, and an unavailable paid AI route must never look purchasable.
2. Finish Arena as a real product surface: theme tokens for the app shell,
   accessible states, truthful mode availability, subject-code handling, and one
   next action. Keep the conventional NTA exam skin separate from the user's
   Arena theme preference.
3. Remove the competing PrepOS planner and make it explain the shared learning
   plan. Fix the 10/20/30 minute contract and stop old mission/benchmark copy
   from creating parallel entitlements.
4. Establish the authoritative CUET subject/syllabus registry and audit the
   existing bank before generating anything. Only then build independently
   keyed, source-backed families for the eight recovery concepts.
5. Run the real staging journeys, content calibration, payment reconciliation,
   accessibility/device checks, and economics gates before enabling the ₹299
   offer.

| Original roadmap area | GPT 6.1 Sol handoff | Audit disposition |
|---|---|---|
| Recovery data model and bounded diagnosis | Local source implemented and software-tested | Keep; prove with authenticated staging content |
| Shared next action | API and page wiring present; Arena/PrepOS still carry older client assumptions | Finish one server quote/action contract |
| Arena light/dark experience | Marketing theme refined; app shell remains fixed dark in live DOM | Release blocker for app-shell theme work |
| PrepOS | Deterministic shared API exists, but local missions, old time choices and stale copy remain | Collapse to explanation layer |
| AI wallet | Atomic RPC/guard exists, but degraded synthetic balance and direct fallback remain | Fail closed; test durable reservation/receipts |
| Syllabus and eight pathways | Blueprints and software fixtures exist; source registry/calibration/pathways are empty | Read-only audit and authoritative mapping first |
| DU Compass | Source-backed implementation reported | Verify staging and keep historical/provisional language |
| ₹299 offer | Versioned and gated in source | Keep disabled until all content, journey, payment and margin gates pass |

## What was implemented, and what that proves

The status files report local source implementation of the following: a versioned
future ₹299 plan while preserving old ₹99 entitlements; bounded diagnosis with a
three-probe limit; numeric and evidence-span repair responses; fresh-family
reservation and delayed checks; ordinary session migration behind a flag; a
shared next-action API; sourced DU eligibility/cutoffs; persistent runtime-AI
reservation tables; guarded rate limits; Rival ownership/duplicate checks; and
versioned answer correction handling. These are useful foundations.

The recorded checks are software checks, not a learning or production claim:

- recovery 17/17, learning 12/12, and a combined offline suite 101/101;
- lint and build passed in the prior handoff;
- the learning HTTP check recorded 9/9 expected authentication/unavailable
  responses;
- a local browser run checked the landing page, an unavailable recovery state,
  selected Arena runner behavior in a development preview, and some responsive
  theme behavior.

This audit did not rerun those suites. It treats them as prior-run evidence and
does not upgrade them to proof of a live authenticated recovery journey, an
academic answer key, successful payment, wallet atomicity in production, real
device accessibility, or field performance. The next model must rerun relevant
checks after each change and add the missing staging evidence.

## Confirmed current gaps

### Arena is still a dark-only application shell

The live local `/dashboard`/Arena DOM reported `data-theme="light"`, but the
computed `.app-shell` background was the dark Arena token (`rgb(11, 16, 14)`)
and its text was the dark token (`rgb(242, 244, 236)`). There was no theme switch
in the app navigation. `src/app/(app)/arena.css` defines fixed night tokens and
does not branch on `data-theme`; `src/app/marketing-theme.css` scopes the actual
light/dark roles to `.mm`; `src/components/ThemeToggle.jsx` only helps surfaces
that render it; and `src/app/(app)/AppLayoutClient.jsx` does not render it.

The fix is a semantic app token layer and a single app-level theme control. Audit
all app routes at 320, 375, 768, 1024, 1280 and a wide desktop in both themes.
Do not recolor the NTA console into a marketing theme: the strict exam skin is a
separate, deliberate preference. Test focus, pressed, disabled, selected, error,
modal and chart states, not just the page background.

The static Impeccable detector found 95 heuristic advisories in Arena/dashboard
and PrepOS files (49 font-size, 28 color, 15 radius, plus one grid, one layout
transition and one easing advisory). These are leads, not 95 confirmed defects.
The JSON is saved at `docs/brain/reports/claude-handover-static-audit.json`.
Review intentional Night Arena treatments rather than mechanically normalizing
the design.

### Arena exposes mixed availability and legacy copy

The dashboard currently shows Quick, Full, Smart and NTA modes with different
labels and a “highest-quality” premium-selection message. It also showed the
legacy “Fast lane active” phrase. A mode label must come from the capability
registry, state whether it is free, included, unavailable, or sample-only, and
give a useful reason. Premium selection may improve selection or access; it must
not imply that the free bank is academically inferior.

The dashboard still has a static subject list and can display a stored Hindi
selection even though `CUET_PUBLIC_ALLOWED_SUBJECTS` does not include Hindi.
Do not delete historic preferences. Normalize them to stable official subject
codes, mark unsupported/stale choices clearly, and prevent a new launch from
falling through to `SUBJECT_NOT_SUPPORTED`.

Inventory counts aggregate multiple purposes. A count in the dashboard does not
prove that a complete Quick, NTA, recovery, or fresh-family blueprint is
available. Stats and selection must consume the same policy and expose genuine
zero or unavailable states.

### Today is better connected, but its contract must stay server-owned

At 320px, `/today` correctly showed “Your next useful step,” 10/20/30-minute
choices, an ordinary-practice fallback, and a recovery-source disclosure. That is
the right direction. The action currently needs a verified server action contract:
the chosen duration must affect the session or plan, the allowance/entitlement
must be checked at creation, and the UI must not infer access from a client credit
number. Keep one primary action and at most two alternatives.

### PrepOS still looks like a second planner and wallet store

`src/components/ai/MockMobAIHub.jsx` still builds local missions and day plans
(`buildMission`, `buildDailyPlan`, `buildSetupPlanResponse`) and persists setup
profile data. Its setup overlay asks for 20/45/60/90 minutes, while Today uses
10/20/30. That creates a competing plan and a contradictory time contract.
PrepOS should explain the server-generated plan and link to its action; it should
not create another schedule, benchmark entitlement, or mastery interpretation.

The Tools view still describes DU Compass as giving “college and course
direction,” which is broader than the sourced historical eligibility/cutoff
engine. Replace it with the exact sourced comparison language and year/round/
category context.

The older `MockMobAssistant.jsx` and current `MockMobAIHub.jsx` both contain
similar credit/plan vocabulary. Trace the call graph before deleting anything,
then retire or isolate dead legacy code so copy and access rules cannot diverge.

### PrepOS wallet has unsafe degraded paths

`src/services/credits/aiCreditWallet.js` is the highest-risk concrete review item.

- `getAIWallet` can insert or reset state while it is being read. The credits GET
  route also calls it indirectly twice through the usage snapshot.
- A missing table/error returns `emptyWallet` with a synthetic monthly allowance
  and an apparent total. A degraded schema must be `unknown/unavailable`, not a
  spendable 50 or a fake zero that silently makes the UI appear empty.
- The direct `consumeDirectly` fallback reads, calculates, updates, and then
  inserts a ledger row without compare-and-swap or one transaction. Ledger errors
  are logged and swallowed. This is not an acceptable paid-wallet path.
- `consumeAIAllowance.js` uses `Date.now()` as an idempotency reference, so a
  retry may receive a new key. Every retry needs the same stable operation key.
- `isPaidUser` relies on subscription fields that need to be checked against the
  centralized effective-entitlement/expiry rule.
- The client maps failed credit responses to zeros and still renders active pack
  buttons; the API returns `ok: true` without an explicit availability state.

Keep the existing atomic credit RPC and historical balances. For any paid AI
reactivation, require durable `reserved → executing → committed/released`
records, one operation id across retries, provider receipts separated from the
student ledger, and an unknown-price/funding fail-closed result. Until that is
staged and tested, render “PrepOS paid features are temporarily unavailable. Your
credits have not been used.” Keep purchased wallets readable and do not invent a
refund or grant in a fallback.

The current local wallet response showed 50 included credits. That is an observed
UI value, not proof that the wallet ledger is correct; the degraded fallback can
produce a similar value. The next implementation must prove this through a real
schema-backed staging test.

### Practice, recovery, and freshness still need boundary tests

The dashboard client has a credit-based launch gate while server practice policy
also has daily/baseline/sample allowances. Replace client guesses with a server
eligibility quote and consume only after successful idempotent creation. Preserve
ordinary credits and their existing RPC.

The session service has a legacy ticket compatibility path with a two-minute
receipt grace. Confirm that it cannot turn into extra answer time and that server
acknowledgement is authoritative. Confirm that saved/explore/ordinary exposure
cannot contaminate a reserved delayed-check family. The source has strong
reservation code, but this cross-surface exposure audit is still a release task.

The five-question baseline is a signal, not a full subject diagnosis. The
diagnostic blueprint must state sample size and ask for more evidence when it
cannot support a hypothesis. Do not display mastery, recovered marks, or causal
improvement.

## Content and syllabus agenda

Do not generate a large question volume next. The first deliverable is a read-only
content audit and authoritative curriculum registry.

`data/canonical_syllabus.js` is labelled as a CUET 2026 map and retains legacy
coverage. `data/cuet_controls.js` contains several different subject populations:
the public allowlist, the broader data catalog, launch subjects, and stored user
choices. These are not interchangeable. Assign stable official subject codes,
versioned syllabus/unit/topic/concept IDs, label aliases, and a crosswalk for old
attempts. Keep ambiguous or unmapped material quarantined.

The official NTA 2026 syllabus page located during this audit lists subject rows
and official codes, but a 2027 specification was not verified in this bounded
check. Claude must fetch and cite the official publication actually used, keep
the 2027 rules provisional until verified, and store source version/locator.
See [NTA CUET UG 2026 syllabus](https://cuet.nta.nic.in/cuetug-2026-syllabus/)
for the baseline inspected on 2 October 2026.

Generation must proceed as: authoritative registry → read-only bank audit → dry-run
mapping report → coverage by usable independent families and mode → independent
academic fixtures → budgeted calibration → eight initial pathways → only then
careful bank expansion. Preserve original source hashes, answer keys,
explanations, mapping decisions and quarantine reasons. Classify wrong keys,
mislabels, duplicates, near variants, incomplete passages, tax/version drift and
unofficial PYQs. Never use model agreement as truth and never call generated
fixtures independent benchmarks.

The initial pathway candidates remain the eight roadmap concepts: Accountancy
sacrificing/gaining ratios and revaluation treatment; Economics national-income
inclusions/exclusions and nominal versus real values; Business Studies delegation
versus decentralisation and planning versus controlling; English explicit
statement versus inference and main idea versus supporting detail. Verify each
against the authoritative syllabus first. Each enabled concept needs at least six
independent families plus diagnosis, repair, immediate, two delayed, and
maintenance inventory. Cosmetic numerical changes do not count as transfer.

## Release posture

The old ₹99 product remains the current offer and historical access remains
valid. The future ₹299 one-time plan through 31 July 2027 stays disabled until
content, authenticated journey, payment, wallet, accessibility, device, support,
receipts and ≥70% contribution-margin gates pass. No capability should appear in
the paid comparison while its release state is unavailable or gated.

## Verification record for this audit

- Read `AGENTS.md`, `PRODUCT.md`, `DESIGN.md`, and the project brain before this
  review; used Impeccable audit guidance and Supabase guidance.
- Inspected local `/dashboard`, `/today`, and `/mentor` in the existing signed-in
  development browser without starting a mock, purchase, paid call, or migration.
- Verified the Arena light-mode mismatch by DOM/computed state and inspected the
  small-screen Today state at 320px.
- Ran the Impeccable static detector against Arena/dashboard/PrepOS files. It
  returned 95 advisories; the full JSON is retained for Claude, and the findings
  are treated as heuristic review leads.
- Did not rerun the prior 17/17, 12/12, 101/101, lint, build, or 9/9 HTTP checks.

This document does not claim that a production deployment or academic validation
exists. It is the evidence layer for `CLAUDE-MASTER-HANDOVER.md`.
