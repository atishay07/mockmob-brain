> Current authority: [ROADMAP-2027.md](ROADMAP-2027.md). Older rollout and packaging decisions below are superseded where they conflict; evidence and budget safeguards remain binding.

# Score Recovery Lab specification

Promise: Discover where you lose marks—and practise the changes that could recover them.
Audience: CUET UG 2027 Commerce: English, Accountancy, Business Studies, Economics.
Keep MockMob, volt green, Rs 99 one-time web access through July 31, 2027.
Initial diagnostic/pilot is free. Preserve existing paid access. Mentors are later.

## Experience
Five-question diagnostic -> observed answer/time history -> proposed intervention ->
fresh-question follow-up -> personal playbook. Correct-to-wrong answer changes have
an observed mark effect; knowledge gaps and time inefficiency are hypotheses.
Never display invented recoverable marks, causal improvement, rank or admission promises.
Browser events are self-reported telemetry, not proof of cheating or exact attention.
Delayed improvement requires two distinct, unassisted checks at least 24h apart;
repeat questions/family variants do not qualify. Failures reopen the concept.

Navigation: Today, Practice, Review, Progress, Account. Secondary: community, ranks,
contributions, AI. Homepage: promise, playable demo, recovery loop, evidence, price.
Preserve bright surfaces, slate test panels, volt actions, readable mobile-first type,
keyboard access, reduced motion and explicit unavailable/empty/error/offline states.

## Architecture
Keep Next.js/Supabase and Razorpay. Server stores selected question snapshots, expiry,
session owner and authoritative scores. Submission is idempotent by session ID.
Each answer event has a sequence, question ID, elapsed milliseconds and selected index.
All user reads are owner-scoped. Never trust client scores or answer keys.
Legacy attempts remain readable but cannot establish new evidence-based progress.
Version evidence by answer-bearing content hash, source and verifier versions.
Unresolved corrections quarantine questions; do not silently alter historical snapshots.

## Mobile
React/Vite/Capacitor bundled client, hosted backend, email OTP, validated bearer tokens,
secure platform token storage, free beta, no purchase links. Online scored sessions;
downloaded review is not an authoritative scored attempt. iOS needs macOS signing CI.
Stores require owner enrollment, signing, device QA and review; public Oct 8 launch
is not promised. Before paid app release add store billing, restoration, server receipt
checks/refunds, account deletion and privacy disclosures. Store costs are separate.

## Milestones and acceptance
Oct 8 target: focused web pilot and beta builds subject to account/device prerequisites.
Quality/access gates outrank deadlines. Full mocks require 50 eligible questions and
subject blueprint coverage; lack of content must not spend credits.
Verify wrong keys, ambiguity, false references, missing verdicts, duplicate candidates,
budget restart/concurrency, zero yield, ownership, forged scores and retry idempotency.
Track diagnostic completion, review return, fresh accuracy and confirmed defects.

## Research (observed 2026-10-01; reverify changing rules)
- https://ug.preparoo.app/ — planning, analytics and question explanations already exist.
- https://www.prepium.in/ — custom practice and eligibility already exist.
- https://cuet.nta.nic.in/cuetug-2026-syllabus/ — baseline until 2027 is verified.
- https://capacitorjs.com/docs/config — server.url is for development/live reload.
- https://support.google.com/googleplay/android-developer/answer/14151465 — account testing.
- https://developer.apple.com/app-store/review/guidelines/ — app release prerequisites.
