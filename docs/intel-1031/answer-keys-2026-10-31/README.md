# Flawed live questions: fixes ready to apply (31 Oct 2026)

**Status:** all five batches were applied on production on 31 Oct after the owner's "Yes, run them".
- **Gap found the same afternoon:** the 25 pull-outs set only `status = 'pending'`. They stayed verified and active,
  so they were still served.
- **Fixed:** `../off-syllabus-2026-10-31/pull.sql` froze them; its `undo.sql` reverses that.

**What each folder holds:**
- `VERDICTS.md`: the evidence, from the NCERT page or the working.
- `fix.sql`: one transaction. Every UPDATE is guarded on the current key, and the pull-outs also on
  `status = 'live'`.
- `undo.sql`: restores every touched field to the value read on 31 Oct.

| Batch | Found by | Questions | Key fixed | Reworded (key kept) | Out of the pool (`pending`) |
|---|---|---|---|---|---|
| `.` (batch 1) | Key cards links pass | 4 of 5 checked (1 was fine) | 2 (b29a66fb A to C, 01dc09dc A to D) | 2 (2370d28b, 577f9005) | 0 |
| `batch2` | gap pass | 8 | 0 | 5 | 3 |
| `batch3` | Accountancy gap pass | 6 | 1 (3452e48e B to C) | 0 | 5 (NCERT contradicts itself on writing off debenture discount, p. 81 vs p. 106) |
| `batch4-accountancy` | pool audit | 28 of 29 checked (1 was fine) | 0 | 18 (10 are one share-capital template bug) | 10 |
| `batch4-other` | pool audit | 13 | 0 | 6 | 7 |
| **All** | | **59** | **3** | **31** | **25** |

## How to apply (each batch on its own)
1. **Dry run.** Wrap the file's statements in `begin; ... rollback;`. Check that each UPDATE touched exactly one row, or
   the 10 template rows. A 0 means the row changed since 31 Oct: re-read it, do not force it.
2. **Apply** `fix.sql`.
3. **Spot-check** two rows per batch with SELECT.

## Effects to expect
- **Learning episodes:** the `learning_evidence_change` trigger marks any learning episode built on a changed
  question as invalidated. This is intended.
- **NTA papers:**
  - A reworded or re-keyed question no longer matches its signed evidence hash, so it leaves NTA papers until it is
    verified again.
  - Practice and Revise keep serving it.
  - These rows mostly have no signed evidence anyway.
- **The 10 template rewords:** `batch4-accountancy/undo.sql` restores them with the exact inverse `replace()`. Check
  one of them in the dry run.
