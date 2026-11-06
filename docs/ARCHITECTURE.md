> Current authority: [ROADMAP-2027.md](ROADMAP-2027.md). Older rollout and packaging decisions below are superseded where they conflict; evidence and budget safeguards remain binding.

# Runtime and interfaces

The authoritative checkout is this nested repository. Desktop/mockmob-clean is
comparison material. Next.js 16.2.4 and Supabase remain the backend; Razorpay remains
web billing. No new independent question generator is introduced.

## Practice and recovery

- POST /api/sessions: validated owner, launch subject, mode and request key. Select
  eligible questions before charging; a five-question quick diagnostic is free.
  Existing request keys return their original session, never a second charge.
- PUT /api/sessions: ordered visit/answer events. Sequence numbers start at one;
  identical retries are accepted, conflicting payloads and gaps are rejected.
- PATCH /api/sessions: score recorded events against the server snapshot. Ignore
  client scores, keys and submitted answer maps. A two-minute upload grace allows
  finishing from already recorded events, not late answering.
- GET /api/attempts and /api/attempts/:id: owner-scoped. Legacy POST delegates to
  the server-session submission handler; historical client scores stay historical.
- GET /api/recovery: delayed review, playbook and fresh concept checks. Exclude
  repeated IDs/families, missing concept mappings and changed/quarantined/currently
  unavailable verification. Historical snapshots remain immutable.
- POST /api/recovery: owner-authorized strategy/reflection, stored idempotently.

Shared public contract: shared/recoveryContract.js. Pre-submit question responses
whitelist stem, option text, passage and safe metadata; no answer/explanation keys.
Scoring logic: data/recovery.js. Scores use +5/-1; percentage display is clamped at
zero, raw marks remain available. Events are self-reported, not precise attention
or proof of cheating. Replay distinguishes observation from inferred intervention.

## Content

data/content_evidence.js canonicalizes answer-bearing content, checks HMAC records,
candidate identity, family/version, source support hashes, stage evidence and expiry.
data/evidence_registry.js additionally requires a released calibration route.
Generation workers and the existing offline importer both enter the same evidence
pipeline and publisher. Legacy heuristic sample approvals cannot bypass it.

scripts/pipeline/lib/configuredEvidenceAdapters.mjs is a configurable budgeted
source-grounded model adapter. sourceAdapters.mjs verifies source excerpt hashes,
quote existence, exact result matching and authenticated exam-example prerequisites.
Numerical families require separately implemented solvers; no model substitution.
Model judgment and exact quote existence do not by themselves prove entailment.

The old internal single-model moderation endpoint is paused without claiming jobs
or making paid requests. Manual approval cannot bypass publication evidence.
Saved evidence state is the product authority; old database tier/verified columns
are compatibility fields, not an independent accuracy guarantee.

## Saved migration and rollback

supabase/migrations/20261001105920_score_recovery_foundations.sql is saved and
tested in local Postgres (PGlite), NOT applied to production. It adds service-only
sessions, playbooks, delayed reviews, version history, question evidence/family/text,
atomic credit/session creation, event recording, exactly-once scoring/progress,
reversible quarantine and transactional passage-plus-children publication.

Before deployment: back up the target, inspect the migration against its schema,
apply in staging, exercise real authentication/credits and verify RLS. Install the
migration before enabling the web client. No production SQL was executed here.

Quarantine tool defaults to a dry-run plan. Applying it checks saved answer-bearing
fields, archives previous rows and holds family dependents without deleting IDs or
attempts. Restore each affected history row with restore_recovery_question; restored
evidence still must match content/current sources. Never revert changed answer keys
by blindly copying an old whole row. Keep new tables/history on application rollback.
Family registry holds must also be reconciled before any future variant is released.
Quarantine persists recovery_family_holds in the same transaction. Selection, worker
preflight and publication consult this service-only table; restoring one question
does not reopen its family. Release a held family only after fresh family evidence.

## Mobile

mobile/ is a separate React/Vite/Capacitor client with bundled dist, bundled fonts,
secure native storage, email OTP, bearer validation, local review/draft cache and
user-requested reminders. The Android source project is generated; iOS requires
macOS/Xcode. Backend CORS allows native localhost origins; service keys never enter
the client. Browser preview stores login in memory only. Beta has no purchases.
Online scored events must reach the server before expiry; offline review is a saved
historical snapshot. Real-device behavior remains unverified.
