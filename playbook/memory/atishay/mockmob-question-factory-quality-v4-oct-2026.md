---
name: mockmob-question-factory-quality-v4-oct-2026
description: "Question factory state (6 Oct 2026, quality-v5): 58/100 machine-eligible, 41 audit publish-ready, ~$0.019/eligible; 10k within $50 not met"
metadata:
  node_type: memory
  type: project
  originSessionId: c5be4860-3336-41a4-a4a4-10cb2484d656
  modified: 2026-10-06T15:36:41.222Z
---

The owner's goal is 10,000 unique published CUET questions within a $50 lifetime ceiling at the highest defensible quality. Pass rate is an optimisation metric only.

**State (6 Oct 2026, verifier v5.3, `qualityCampaign.mjs`):**
- Defect regression: 0 of 18 audited defects accepted.
- Calibration retention: 80.6%, below the 85% floor, so not released. The owner chose a measure-only cohort (`--measure-only`).
- Cohort: 58/100 machine-eligible; my audit rated 41 of them publish-ready.
- Cost: $0.0194 per eligible, so ≈$200 for 10k (≈$103 at unproven batch pricing). Bulk spending is paused.

**Why:** single LLM samples flip borderline verdicts. The fixes were dual Luna samples, source-backed chapters, missing-condition checks and deterministic lint. Calibration fixtures were previously observed, not unseen.

**How to apply:**
- Next levers: demonstrate batch execution, deduplicate ideas across anchors, plan more blueprints per call, and try a cheaper second Luna sample (it must pass the gates).
- Don't re-sample or relabel fixtures to win a release; archive every gate run.
- See [[mockmob-differentiator-decision-oct-2026]].
