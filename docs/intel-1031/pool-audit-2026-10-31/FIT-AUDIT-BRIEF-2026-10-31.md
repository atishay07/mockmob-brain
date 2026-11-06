# Live question pool: syllabus-fit audit brief (31 Oct 2026)

**Why:** MockMob's live practice questions decide a student's chapter state and their mocks. The Key cards passes found:
- many questions filed under the wrong chapter (for example environment items under Regional Aspirations, genetics
  under Human Health)
- many questions on topics the CUET 2026 syllabus dropped (money-demand motives, isoquants, open-economy multiplier,
  Sanger sequencing, DRR and sinking fund)

**Your job:** an exact, read-only list. Nobody changes a question from your list without the owner's decision, so be
precise and conservative.

## Inputs (read only)
- **Live questions:**
  - Supabase `execute_sql`, project `isrxrxzjocewrdureyhp`. SELECT only; never insert, update, delete or apply.
  - Filter: `status = 'live' and coalesce(is_deleted,false) = false and subject = '<subject>'`.
  - Columns: `id, chapter, body, options, correct_answer, explanation`.
  - Read in pages; never print more than you need.
- **The syllabus:** `C:\Users\atish\Desktop\mockmob copy\wt-1031-keycards-web\data\cuet_syllabus.js`. Its live chapters
  and `resolveChapter(subject, name)` (retired chapters resolve with `retired: true`; skip those questions, they are
  handled already).
- **The CUET 2026 unit lists:**
  `pdftotext "C:\Users\atish\Desktop\mockmob copy\mockmob-next\data\CUET 2026\<subject>.pdf" -`. These say which topics
  are in.
- **NCERT text when needed:** `C:\Users\atish\Desktop\mockmob copy\ncert-books\pdf\<code>.pdf`.

## For every live question in your scope, one verdict
- **ok:** it tests its stored chapter (after `resolveChapter`), and the topic is in the CUET 2026 unit list.
- **move:** it clearly tests a different live chapter of the same subject. Give that chapter's key. Use it only when a
  CUET student would say at once that the question belongs there.
- **outside_syllabus:** the topic is not in any CUET 2026 unit of the subject, even if an NCERT book mentions it. Name
  the topic.
- **outside_ncert:** in a unit, but the deciding fact is not in the NCERT text, and no NCERT line or rule settles it.
  Use it sparingly.
- **flawed:** a wrong key, no correct option, two correct options, or an ambiguous stem. Give the evidence in one line.

## Output
- **File:** `C:\Users\atish\Desktop\mockmob copy\ncert-books\audit\fit-<your task name>.json`:

  ```json
  { "subject": "...", "examined": n, "counts": { "ok": n, "move": n, "outside_syllabus": n, "outside_ncert": n, "flawed": n },
    "items": { "<questionId>": { "stored": "<chapter as stored>", "verdict": "move|outside_syllabus|outside_ncert|flawed", "to": "<chapterKey, for move>", "why": "one line" } } }
  ```

  List only non-ok items under `items`. Keys are sorted.
- **Scratch:** only in your own `kc-fit-<name>` folder inside your temp folder.
- Change nothing else.

## Return
Four lines:
1. Examined, and the counts.
2. The 3 stored chapters with the most moves.
3. The 3 biggest outside-syllabus topics with their counts.
4. The flawed ids.
