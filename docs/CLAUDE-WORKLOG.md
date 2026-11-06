# Claude worklog — CLAUDE-MASTER-HANDOVER execution

Started 2 October 2026. Binding contract: `CLAUDE-MASTER-HANDOVER.md`. Evidence:
`ROADMAP-GAP-AUDIT-2026-10-02.md`. Results of each stage are recorded in `STATUS.md`.

## Superseded promises (do not reintroduce)

These appear in older brain prose, PRODUCT.md or legacy UI and are no longer product
promises. Where they conflict with ROADMAP-2027.md and the handover, they lose.

| Old promise | Status | Replacement |
|---|---|---|
| 40–80 question pilot and store delivery order | Superseded | ROADMAP-2027 stages; question count never releases a pathway |
| "Fast lane" / fast-lane generation for Pro | Superseded, removed from Arena | Actual entitlement: Smart/NTA modes, no per-session credits |
| "Highest-quality selection" for premium | Superseded, removed | Selection/access benefit only; free bank is not academically inferior |
| Peer review / routine human question review | Superseded | Automated evidence; uncertainty → quarantine |
| Admission prediction, score-band estimate, chance bands | Superseded | Sourced historical DU eligibility/cutoffs with year, round, category |
| Invented or hard-coded counts (questions, students, subjects) | Superseded | Live `/api/stats` with truthful zero/unavailable states |
| PrepOS local missions, day plans, 20/45/60/90-minute setup planner | Superseded | Shared server plan (`/api/learning/plan`), 10/20/30 minutes |
| PrepOS benchmark entitlements and live AI credit packs | Superseded while paused | Wallet read-only; paused state message; no live pack buttons |
| Synthetic monthly AI balance when the wallet cannot be read | Removed | Explicit wallet `state` (`schema_unavailable`/`error`) with no balance |

## Dependency-ordered checklist

Stage A — Arena and capability truth
- [x] A0 Source inventory and call-graph trace (Arena, AppLayout, Today, PrepOS, wallet, registry)
- [x] A1 Capability registry: id/version, availability, official subject codes, entitlement,
      inventory policy, actionable unavailable reason
- [x] A2 Server launch quote (`GET /api/practice/quote`): entitlement, allowance, credit cost,
      duration, inventory, expiry, reason, idempotency token; dashboard renders it
- [x] A3 Arena light/dark semantic tokens, theme control in app shell, NTA console isolated
- [x] A4 Truthful Arena copy (Fast lane, highest-quality), subject normalization with
      unsupported/stale state that cannot launch
- [~] A5 Verify both themes at 320/375/768/1024/1280/wide; record in STATUS.md
      (dashboard, runners, PrepOS done via dev preview; other signed-in routes pending)

Stage B — PrepOS and wallet safety (before any paid AI)
- [x] B1 Wallet read is pure (no insert/reset), returns explicit state, single read in GET
- [x] B2 Remove direct read-modify-write consume fallback; RPC-only; fail closed when paused
- [x] B3 Stable operation key across retries; centralized effective-entitlement check
- [x] B4 PrepOS UI: paused message, no live pack buttons, failures never shown as zero
- [x] B5 PrepOS planner collapse: no local missions/day plans/setup planner; explains shared plan
- [x] B6 DU wording in PrepOS Tools: sourced historical comparison language
- [~] B7 Tests (done except provider timeout/fallback reversal, which need the
      not-yet-built student reservation path; real multi-session concurrency needs staging): expired entitlement, missing schema, stale cache, concurrent consume, retry
      same key, provider timeout, deterministic fallback, ledger failure, account switch;
      receipt/reconciliation report

Stage C onward (sessions/recovery integration, syllabus registry, pipeline, payments) follow
the handover order and are not started until A and B pass.
