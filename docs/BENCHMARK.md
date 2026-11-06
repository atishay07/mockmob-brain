# Calibration before content release

data/calibration_manifest.json is paused with empty development and held-out sets.
The regression suites test software defenses; they are not academic certification.

Register official syllabus/rules, authentic question documents and FINAL answer
keys with identity checksum, edition/version, permission and extraction evidence.
Match question numbers/options to final keys; detect missing/duplicate mappings and
document mismatches. Original/manual seeds retain that label, without invented PYQ
years or anchor IDs. 2027 rules remain provisional until officially verified.

Fixture format: id, category, valid, split, question, provenance with source_id,
key_locator and independently_keyed=true. Preserve reference answer provenance,
question family, source version and the applied defect. Development sources/families
must be disjoint from held-out sources/families, not only different question IDs.
Do not tune prompts against the held-out set after seeing failures; version a new
benchmark if it becomes development material.

Required categories: valid_easy, valid_medium, valid_difficult, wrong_key,
multiple_correct, missing_assumptions, out_of_syllabus, false_citation,
unsupported_explanation, orphan_passage, cosmetic_duplicate, option_collision,
solver_boundary. Include each launch subject and each enabled route. Numerical
boundaries include zero/negative inputs, rounding ties, invalid domains, units and
option collisions. Passage fixtures exercise parent/child integrity and answer spans.

calibrate in evidencePipeline.mjs reports valid/invalid sample sizes, category-level
results, split disjointness and critical false accepts. Release requires:

- Every deterministic corruption regression caught.
- No known invalid held-out critical item published.
- >=95% valid reference survival through correctness checks.
- Every required category, independent key provenance and disjoint source/family splits.

A small clean suite does not prove universal correctness or superiority to human
review. Model agreement remains correlated supporting evidence. Independent solvers
do not certify wording or syllabus fit. Route-specific calibration reports go under
manifest.routes[route]; report.verifier_version and source_registry_version must
match current inputs and split_disjoint must be true. Only released routes enter
scored practice. New source or verifier versions require recalibration.

Next calibration run must store fixture hashes, verifier/source/family versions,
full result IDs, failures and actual ledger usage. Pilot 40–80 questions is conditional
on these results. Do not publish the existing 100-question Economics batch based on
its heuristic score or a 20-item model sample.
