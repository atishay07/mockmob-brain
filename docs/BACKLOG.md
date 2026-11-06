> Current authority: [ROADMAP-2027.md](ROADMAP-2027.md). Older rollout and packaging decisions below are superseded where they conflict; evidence and budget safeguards remain binding.

# Ordered implementation backlog

Current executable checklist: [IMPLEMENTATION-2027.md](IMPLEMENTATION-2027.md).

## Now (owner plan, 4 Oct evening): see PLAN-2026-10-04-NEXT-DAYS.md — it supersedes the list below.

## Next, in order (4 October 2026 decision)

1. Owner: approve or reject the "Mistake Repair" rename; engage one independent Accountancy
   reviewer for `data/recovery_candidates/sacrificing_gaining.source.json` (see review items in
   docs/brain/reports/pathway-sacrificing_gaining-validation.json).
2. Named staging: apply the saved learning migrations (configured DB lacks learning_episodes).
3. Backend verification job signs the 14 candidate items; seed staging; register the digest.
4. Pilot gate: allow the candidate for an opted-in cohort only (new flag; not built yet).
5. Run `scripts/learning/recovery-metrics.mjs` weekly; decide at ≥30 episodes per thresholds.
6. Trustworthy practice: one student-facing "where this answer comes from" view.
7. Legal review of DPDP duties for under-18 learners and existing telemetry before May 2027.
8. Only then: pathway 2 (Economics nominal/real values).
The sections below preserve earlier technical context; their stage order, pilot
count and launch dates are historical and no longer control implementation.

Preserve the approved USP, launch scope, one-time pricing, entitlements and budget.
No routine human question review. Do not bypass a gate to meet the October 8 target.

## 1. Establish reference inputs and calibration

Register versioned permitted excerpts, document identities/extraction checks and
official exam specs in source_registry.json. facts[locator].text must SHA256-match
supports[locator] and each source_ref.support_hash. Authentic examples require
source_kind=authentic_pyq and independently checked final_key_matched. Manual seeds
never receive those flags merely because an agent knows their likely answer.

Build development/held-out fixtures described in BENCHMARK.md. Supply numerical
solver/boundary modules keyed by exact family ID to createEvidenceAdapters. Compare
independent results, including wording/assumptions and alternative-answer challenges.
Authenticate source/key extraction before running paid models. Add benchmark-run
CLI persistence and route-release checks; never hand-set a released manifest.

Configure exact verified model prices/host/full limits and a durable shared ledger.
Use configuredEvidenceAdapters only for approved model stages. Measure the initial
calibration within $2. Route failures pause automatically; publish nothing uncertain.

## 2. Stage the backend and pilot content

Inspect saved migration against production schema in a backup/staging clone. Exercise
atomic passage publication, rollback, existing Razorpay entitlements and real owner
authentication. Set CUET_CONTENT_AUTHOR_ID to an actual system author. Save a staging
audit and quarantine dry run, then apply only the reversible approved changes.

Recheck local Economics candidates through item-level evidence_results.json. Existing
offline importer uses these results and current publication eligibility, not sample
approval. Author bounded original batches across English/Accountancy/Business Studies/
Economics. Do not promise 40–80 until yield and concept coverage are measured.

Generation jobs require active registered source families for their subject/chapter.
Use the worker's existing pipeline and evidence integration. Add compatible-stage
batch dispatch with strict complete candidate-ID matching as a measured optimization;
current evidence verification is sequential. Add within-tested-bound family reuse
for numerical variants only after independent solver/boundary/wording calibration.

## 3. Complete correction and recovery behavior

Implement automated report-triggered re-evaluation, versioned answer correction and
auditable score/progress recomputation. Current code safely excludes changed or held
evidence from improvement claims; it does not yet recompute historic raw scores.
Implement evidence-backed family release and registry synchronization; durable
database family holds already block future publication and scored selection.
Add whole-bank near-semantic duplicate
matching before paid calls; current audit finds exact/stem/number-normalized families.

Add measured per-question dwell/revisit breakdown with uncertainty, optional confidence
outside strict exam flow and guessed-correct delayed review. Queue completion and
due-review transitions still need implementing. Today currently connects diagnosis
to the latest intervention; combine concept repair/timing/delayed review in one plan.
Do not overstate a chapter from two checks; use actual concept mappings.

## 4. Complete app surfaces and real-device beta

Homepage, result lab, Today, Review and Progress use the new recovery direction.
Reconcile remaining legacy dashboard, subject/SEO, onboarding, saved/upload, community
and account screens in the same design world. Preserve five primary tabs and keep
advanced AI/community secondary. Do not infer that the whole website was redesigned.

Set mobile public backend configuration; sync bundled assets to Android. JDK/SDK,
signing and real devices are absent in this shell. Test email delivery/codes, token
refresh, secure storage failures, user-switch cache isolation, offline/online,
background/resume, expiry, interrupted submit and retries. On macOS generate/sign iOS
and verify safe areas, OTP, Keychain and reminders. Desktop web-assets compilation is
not device QA. Store enrollment/test/review remain external release gates.

Free beta has no purchases. Before production digital purchases add compliant store
billing/receipt verification, restoration/refunds, account deletion/privacy disclosures.
Store/infrastructure fees remain outside the $10 content budget. Mentoring/admission
tools and broad syllabus coverage come after evidenced pilot results.
