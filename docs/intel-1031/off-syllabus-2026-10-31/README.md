# Off-syllabus pull (31 Oct 2026, applied on production)

**Owner:** "Pull them all", about the 218 questions the pool audit found outside the CUET 2026 syllabus
(`../POOL-AUDIT-2026-10-31.md`, finding 3).

## What changed
- **The 218** (`list.json` has each id, chapter and reason):
  - Set to `is_cuet_syllabus = false`, `status = 'pending'` and `exploration_state = 'frozen'`.
  - `verification_state` stays `verified`: the content is correct, only outside the syllabus.
- **Why all three fields:** a question is served when it is live, or when it is verified and active
  (`data/practice_source.js` VISIBLE_QUESTION_FILTER, also the feed, repair check and inventory). Setting status alone
  leaves a verified, active row visible.
- **The 25 answer-key pulls from this morning:**
  - They had exactly that gap: `pending` but still verified and active, so practice and the feed could still serve
    them.
  - They are now `frozen` as well.
- **Freezes stick:** the vote function only ever freezes a question, never unfreezes it. Approving one by hand in
  moderation would bring it back, but the off-syllabus flag still keeps the 218 out of the pickers.

## Evidence
- **Before:** all 218 were live, verified, active, `is_cuet_syllabus` null and not deleted. None was in
  `syllabus_v2_changes`.
- **Dry run** (rolled back with RAISE): pulled 218, froze 25, invalidated 0 learning episodes, visible questions
  8,571 to 8,328.
- **Applied** with `pull.sql` (one transaction). **Check after:** 218 off-syllabus rows, 25 frozen, 8,328 visible.
- **Undo:** `undo.sql` restores every field to the values read before the pull.

## Effects
- **Thin chapters after the pull** (servable questions, before to after):
  - Accountancy, Financial Statements of Company: 10 to 1.
  - Political Science, Recent Issues and Challenges: 13 to 4.
  - Political Science, Environment & Natural Resources: 13 to 10.
  - Every other touched chapter keeps 11 or more. Debentures and Share Capital lose about 30 each but keep 181.
- **New questions** for the thin chapters only on the owner's ask.
- **Worth a second look:** a few verdicts touch topics NCERT itself covers. Left out for now (uncertainty means
  quarantine); bring them back with `undo.sql` rows if the CUET 2026 unit text includes them.
  - Economics: CPI and price index, paradox of thrift.
  - Business Studies: single-use and standing plans.
- **Left alone:** 22 older rows (12 Mathematics, 8 Hindi, 2 English, last changed in April) are also pending, verified
  and active, so they are still served. They are outside the pilot and this pull.
