---
name: mockmob-cuet-fit-generator-oct-2026
description: "CUET-fit validator study state (7 Oct 2026): v7 pipeline built but unreleased, OpenAI credit exhausted and owner declined to add it, legacy contract hash locked while cohort 010 is pending"
metadata:
  node_type: memory
  type: project
  originSessionId: b3257bbd-baa2-4305-ac9a-a304a9632fae
  modified: 2026-10-07T17:06:09.105Z
---

On 7 Oct 2026 the question-generator work was split in two: a frozen legacy v6.2 contract (hash d80135b0…, hashed by compactBenchmark.mjs over factoryCore/factoryEvidence/evidencePipeline/focusedCoverage/focusedSources and four data files) that the retained collector still uses for cohort 010, and a new additive v7 CUET-fit contract in new files (data/cuet_fit_rubric.mjs, data/cuet_fit_evidence.mjs, scripts/pipeline/lib/factoryEvidenceV7.mjs, verifyV7.mjs, cuetFit.mjs, authorIntegrityV7.mjs, tools/cuetFitFactory.mjs). Full state in artifacts/question-factory/cuet-fit-2026-10-07/REPORT.md and RUNBOOK.md.

**Why:** editing any legacy-hashed file stops the running controller (it re-hashes from disk every loop) and strands cohort 010's 9 accepted OpenAI authoring requests. v7 records must keep policy_version `cuet-llm-v3` because the saved publication RPC accepts only that literal.

**How to apply:**
- Do not edit the hashed legacy files until cohort 010 is terminal; add behaviour in new files or in unhashed ones (evidence_registry.js, factoryTransport.mjs, factoryFailure.mjs, focusedFactory.mjs).
- Owner later topped up OpenAI (USD 10) and Anthropic (USD 5); Haiku 5.5 is wired as a measurement-only provider, Gemini and OpenAI stay. 8 Oct: dual_blind (effort-policy-v1) FAILED the fresh v3 release (1/47 defects accepted, valid survival 0.769 < 0.85, 26 calls left unresolved after a killed worker). No release in the manifest; v3 is spent. Ledger USD 20.05 of 50 committed.
- Never kill a worker mid-flight: unresolved realtime requests are never resubmitted and cost benchmark coverage.
- Gemini alone is not an adequate validator (lenient on source entailment, unstable at the margin); dual validation cost ~5x single Luna with no measured extra catch; single Luna approved 2 of 16 audited correctness defects under v7.0 and is unmeasured under v7.1.
- 662 approved questions are retrievable in staging and production (verified 7 Oct); 20.5% exceed the longest authentic PYQ reading load (132 words).
- Never run checkFactoryRestart.mjs while the collector is live (it kills the worker).
- 9 Oct: batch idea inspection is now v4 (repeated ordering task rule); saved v3 inspections must be re-run before publication. Para Jumbles has only 8 original stimuli and the bank holds ~24 surplus repeated ordering ideas; the planning-side fix in briefDiversity.mjs is still open. Haiku subagents were not used (task was small enough inline).
