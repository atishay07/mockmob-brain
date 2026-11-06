# Read-only bank inventory, October 1 2026

Full inventory: artifacts/recovery/bank-audit.json. Reversible recommendations:
artifacts/recovery/quarantine-plan.json. Historical diagnosis:
artifacts/recovery/failure-classification.json. No bank rows were changed.

| Origin/state | Count |
|---|---:|
| Database records | 9,242 |
| Local Economics batch records | 100 |
| Total inventoried | 9,342 |
| Eligible under the new gate | 0 |
| Repairable/local quality signals | 2,055 |
| Uncertain/insufficient evidence | 7,228 |
| Structurally invalid | 59 |
| Exact content duplicates | 0 |
| Likely duplicate stems | 19 |

Each finding includes subject, chapter, source label, generator version, available
evidence, canonical content hash, proposed status and reasons. Coverage totals and
remaining eligible counts are grouped by subject/chapter. Number-normalized family
counts are candidates for follow-up similarity checks, not proof of semantic duplication.

Structural checks cover options/keys; passage text is resolved from parent groups.
Local answer/explanation warnings are repair signals, not independent proof of a
wrong key. Missing provenance and heuristic scores do not establish correctness.
Zero eligible content is an evidence gap, not a conclusion that all questions are bad.
Paid verification estimates remain unknown until official pricing and pilot yield.

The saved dry-run recommends quarantine for 59 structurally invalid database rows.
Missing evidence alone does not trigger bulk destructive filtering. Applying the
quarantine requires the saved migration and a matching current snapshot; IDs and
historical attempts are preserved. Inspect dry-run and staging behavior first.

The May 1 historical audit records ten routes with zero generated candidates and
zero validation submissions. The new classification is INSUFFICIENT_TELEMETRY.
The source was inspected for weak-generation claims and zero-cost defaults, but
no request-level billing receipts were found in the inspected repository logs.
The dominant cause of the owner's historical API bill therefore remains UNKNOWN.
Do not treat old estimated costs or failed-route labels as provider billing evidence.
