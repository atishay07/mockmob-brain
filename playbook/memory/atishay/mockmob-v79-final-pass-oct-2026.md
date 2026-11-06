---
name: mockmob-v79-final-pass-oct-2026
description: "V7.9 compact-resolution validator (9 Oct 2026): why V7.8 was replaced, the transport timeout bug, passage-scope and rival-condition lessons, fresh-benchmark construction via Claude subagents"
metadata:
  node_type: memory
  type: project
  originSessionId: 25c3edf2-b29c-4fc7-9e35-73be4428aee6
  modified: 2026-10-09T17:33:12.827Z
---

On 9 Oct 2026 Claude ran the owner-authorized final pass on the CUET generator. V7.8 (clause matrix + full re-audit) was measured natively and was too heavy: audits returned reasoning-only truncations, validation ~USD 0.02/item. Additive V7.9 (`contractV79`, `optionResolutionV79`, `factoryEvidenceV79`, `verifyV79`) keeps every gate but uses one row per option with an exact anchored premise; frozen r5 in `artifacts/question-factory/cuet-readiness-2026-10-09/v79-contract-freeze.json`.

**Why:** native regression on exposed V7.7 cases exposed concrete faults, each fixed only after evidence.

**How to apply:**
- Node fetch aborts responses whose headers take >300 s; OpenAI flex calls take 150–310 s. Always pass `fetchImpl: longFetch` (`scripts/pipeline/lib/longFetch.mjs`) to `createFactoryTransport`, or calls die as `fetch failed` and leave uncertain holds.
- In reading-comprehension the passage is the universe: "not stated or implied by the passage" refutes an option (`passage_scope`); subject-fact items keep "source silence is not contradiction".
- Validators sample-miss subtle missing conditions (bank item ea03: capital receipt = liability OR reduces assets). The r5 rival-condition check (`unexcluded_rival_conditions` must be empty) targets it; one clean pass on a stochastic miss proves little — repeat passes.
- Boolean schema field names can invert model meaning (`refutation_entailed` was read as "contradiction entailed"); name fields by the decision (`decisively_wrong`).
- Never wrap a paid run in a shell `timeout` — it kills in-flight requests (rule 12). Run in background and wait on the log.
- Contract files are re-read per candidate (`validationContractV79()` hashes files) — never edit V7.9 files while a run is live.
- Fresh benchmark recipe that worked: Sonnet authors per subject from main-registry hash-custodied facts, separate Sonnet blind custody with keys/labels stripped, sealed until the verifier freeze, then root adjudication. Related: [[mockmob-cuet-fit-generator-oct-2026]], [[delegation-workflow-orchestrator]].
- 10 Oct update (V7.12, frozen 557f43b3): never let quote anchoring merge space-separated tokens or drop in-line hyphens (reviewer showed "now here"→"nowhere", "re-sign"→"resign"); only a source line-end hyphen (NCERT encodes printed hyphens as U+00AD) may join. Scope labels (case_scope, passage_scope) are enforced by a deterministic detector (questionScopeV712.mjs).
- NCERT registry facts were ~half two-column spliced. Use the column-verified overlay `data/question-factory-runtime/source-registry-ncert-columns-v1.json` (ncertcol-<book>-v1, applied via lib/ncertColumnsRegistryV1.mjs) for studies AND pilot authoring; build kits only from the final overlay and check custody for every case, not just valid ones. pypdfium2 renders pages for visual audits (no pdftoppm).
- Before any pilot, size the VALIDATOR requests offline (recording transport + stub ledger with getCache) against `max_input_tokens` in data/pipeline-prices.json — it is a UTF-8 byte bound. V7.12's fixed instructions are ~20 KB, so subject candidates (33–37 KB) all failed `input_bound_exceeded` in the 9 Oct pilot while English fit. Raising that bound was refused by the auto-mode classifier; it needs the owner.
- Fresh q1/q2/q3 all failed the 85% valid rule (53/70/70%) with 0/47 defects accepted; independent adjudication showed ~3/6 q3 losses were validator false rejections (single-judge strictness). Don't keep re-running fresh studies hoping for a pass — that is re-sampling; the 85% threshold is the owner's decision.
