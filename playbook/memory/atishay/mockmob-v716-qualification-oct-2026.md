---
name: mockmob-v716-qualification-oct-2026
description: "V716 integrated, frozen, fresh-qualified once and FAILED (0 false accepts, valid 16/20); key process lessons for paid runs"
metadata:
  node_type: memory
  type: project
  originSessionId: 3f0f3388-00fd-43e4-89e6-a3eea17f86a7
  modified: 2026-10-10T00:21:02.713Z
---

V716 (report-and-policy generator) was integrated, frozen (final-pass-v716/V716-FINAL-EXECUTION-FREEZE.json) and run on one fresh 32-case benchmark on 10 Oct 2026. It **failed**: 0/12 false accepts but valid 16/20, Business Studies 3/5. Three misses were root-authored valid-control explanations with unsupported claims; one was a validator option-status inversion on a NOT stem. Reviewers rate nearly everything Easy. Ledger after: USD10.100569 remains of USD50. No pilot or release followed; the next step needs an owner decision (see final-pass-v716/NEXT-STEPS.md).

**Why:** the owner asked for one bounded fresh study and honest failure reporting, not benchmark after benchmark.

**How to apply:** never edit freeze-closure files during a paid run, because the contract hash is derived live and re-keys requests. Launch paid runners with `node --use-system-ca`. Write benchmark explanations with excerpt-entailed claims only; a Haiku custody audit is weaker than the V716 audit. Relates to [[mockmob-v79-final-pass-oct-2026]] and [[mockmob-cuet-fit-generator-oct-2026]].
