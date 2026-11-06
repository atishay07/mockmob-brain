# Expanding Learn without recurring generation costs

One authored packet in `data/study/authored/expansion.json` produces one concept lesson,
worked contrasts, a concept map, original teaching checks, recall variants and printable
chapter material. The compiler does not publish. Students reuse the released packet;
finishing a lesson unlocks its cards without a model call or AI credit charge.

## Author and prepare

1. Pick a gap from `npm run study:coverage`. Its 54-chapter map is provisional for CUET
   2027; a chapter containing a lesson is only partial coverage.
2. Use a permitted reference. Download the official NCERT PDF to
   `data/study/sources/ncert-<source>.pdf`. PDFs stay outside Git. A changed source digest
   requires a new registered identity/version; do not quietly replace the cited edition.
3. Author a narrowly scoped packet: stable ID, subject/chapter/concept, source ID, version,
   at least three distinct factual contrasts, exact PDF page/anchor for each, accurate
   memory cues and original scenarios. Paraphrase the facts; do not reproduce textbook
   pages. Add a typed calculation only if the independent validator supports its operation.
4. Run `node scripts/learning/register-study-packets.mjs`, then `npm run study:prepare`.
   This compiles, checks source digests and cited pages, independently recomputes arithmetic,
   checks keys/packet consistency, updates coverage, saves SQL and dry-runs the import in
   an isolated database. It makes no paid provider calls or production writes. Missing
   sources, inconsistent keys and unsupported material remain quarantined. `--skip-pdf`
   is test-only and cannot write a release proof.
5. Inspect the rendered lesson, its worked cases and recall tasks. PDF phrase matching
   and arithmetic checks are useful evidence, not independent academic calibration. A
   formal repair pathway still needs its separate source, calibration and exam-fit gates.
6. Save the current-project read-only plan, then insert the released versions through
   `apply-study-content-v2.mjs` with `--artifact-dir=artifacts/study-suite/v3`. This requires
   a matching content digest in the saved dry-run receipt and rejects changed existing
   versions before writing. No question bank or learner balance is changed by this importer.

Commands requiring a database connection run with the existing ignored environment file:

```powershell
node --use-system-ca --env-file=.env.local scripts/learning/apply-study-content-v2.mjs plan --artifact-dir=artifacts/study-suite/v3
node --use-system-ca --env-file=.env.local scripts/learning/apply-study-content-v2.mjs insert --artifact-dir=artifacts/study-suite/v3
node --use-system-ca --env-file=.env.local scripts/learning/apply-study-content-v2.mjs verify --artifact-dir=artifacts/study-suite/v3
```

## Corrections and release

An ID/version is immutable after publication. Bump a version for a correction, validate
again, insert the new version, deploy its release manifest, then quarantine superseded
versions through the existing correction mechanism. Saved runs receive replacement
navigation; withdrawn answers are not returned. Existing event history remains.

This expansion inserts seven new units and 21 cards; it does not retire or change any of
the preceding 14 lessons or 65 cards. The current total is 21 lessons, 86 cards and partial
lesson coverage in 15 of 54 chapters. The other 39 remain visible as gaps.

## AI is optional student support

The lesson tutor can simplify current published teaching or explain feedback after an
answer. It cannot see future items, publish curriculum or certify mastery. It uses the
existing PrepOS one-credit reservation and runtime AI budget ($25 per IST month), including
failure/retry accounting. Ordinary teaching, recall and summaries remain usable without
AI. Shared content is prepared once; it is not generated on every student visit. Future
paid content authoring must use the existing $50 lifetime content budget ledger.

Retain existing Android/offline work. Online API support and printable summaries do not
by themselves verify native downloadable-pack refresh, account isolation or real-device
offline behavior; those checks remain with the existing mobile release workflow.
