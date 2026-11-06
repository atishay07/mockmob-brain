# Handoff, 2 Nov 2026, about 4:20 am IST: Learn v2 rounds 2 to 4 live; Key cards for 7 new subjects live; Computer Science half written

**Written by:** session 3b7877eb (Opus 5.5), the orchestrator for the owner's 1 Nov feedback (LK24-LK35).

**Why now:** the owner continues in a fresh account. The next session's prompt is `PROMPT-NEXT-SESSION-2026-11-02.md` in this folder.

## 1. What is live (production, www.mockmob.in)
| Release | main | Deployment | What |
|---|---|---|---|
| Learn v2 rounds 2 to 4 | 668341aea | dpl_kmM3Rym59riGDcmQ1MVgRzs9RbGa | Owner items LK24 to LK33. |
| Cards 1 | 90679d8c0 | dpl_Bb2sB56bG5wADahBaBkiQvzAQEyh | Chemistry 1,257 and History 1,418 Key cards; science notation. |
| Cards 2 | 26e5f359a | dpl_6hhcRyXQwLwtknmeVNiL1aDbyuqQ | Geography 1,162, Psychology 726, Sociology 983. |
| Cards 3 (current) | 7f1b204a7 | dpl_8B5HtwbPkxUfDXTKa5UeBzyTdd8F | Physics 932, Mathematics 260. |

- **Checks after every release:** there were no runtime errors (`get_runtime_errors`), and the pages answered 200.
- **Rollback:** Vercel instant rollback to the deployment above it.
- **The pre-Learn-v2-round-2 production:** dpl_DoGHp6AAWaCKngaFxKAckyhq7vAy (main 978edc236).
- **Not verified by anyone yet:** a real phone, a trackpad, or a screen reader. The owner should look on his phone.

## 2. Learn v2 rounds 2 to 4 (what shipped, where the specs are)
**Specs and evidence** are in the web repo:
- `docs/brain/learn-1031/r2/R2-SPEC.md`
- `docs/brain/learn-1031/r3/R3-SPEC.md` (the round-2 critics' findings as rulings)
- `docs/brain/learn-1031/r4/R4-SPEC.md` and `R3-REVIEW-FINDINGS.md`. These are 5 review lenses on round 3, and every serious finding was checked by 1 to 3 skeptics: 34 confirmed, 14 refuted.
- `docs/brain/STATUS.md` has an entry per release.

**Shared words:** `data/learn/words.js` holds one word per thing ("Turn over", "Continue · 6 min", "Keep going · 10 min", "Revise later", "open mistakes", `chapterPlace` "Chapter 5 of 14"). The Free after-session headline and line are in `data/learn/allowance.js` (`FREE_DONE_HEADLINE`, `FREE_DONE_LINE`).

**What students see:**
- **Learn:**
  - a start offer with no zeros, and a subject picker on phones
  - roadmap rows with the real chapter size ("45 cards · 10 questions")
  - chapters named by roadmap place
  - "Needs work · from your papers"
- **Cards:** flashcard layout with the next card's edge peeking and a one-time swipe chip.
- **Ends:** headline, up to 3 numbers, the bar, one key and one link.
- **Free's rule:** questions come back tomorrow; Key cards stay open. The server never offers Free a key it would refuse.
- **Today:** a new student sees no false history and no zeros.
- **Practice and Learn agree** on 14 chapters.
- **The address follows the run.**
- **Home hero:** a static headline, and Mobi reacts to taps.

**Open:**
- The Day hero poster needs a repaint (an image job).
- Practice says 15 Accountancy chapters on the live site where Learn says 14. The live `chapters` table holds an active "Computerized Accounting System" (CAS) row, and Learn hides chapters with no cards. Reconcile only if the owner wants it.
- Fluid compute could not be read through the API.

## 3. Key cards content (LK34; the owner chose "Use subscription", not the API)
| Subject | Published | Chapters | Held back | Live |
|---|---|---|---|---|
| Chemistry | 1,257 | 10 | 298 | yes |
| History | 1,418 | 12 | 337 | yes |
| Geography | 1,162 | 17 | 444 | yes |
| Psychology | 726 | 7 | 150 | yes |
| Sociology | 983 | 14 | 441 | yes (Structural Change 8 and Cultural Change 32: short NCERT chapters) |
| Physics | 932 | 14 | 397 | yes |
| Mathematics | 260 | 14 | 234 | yes, but THIN: about 2 h of study, below the owner's 3 h bar |
| Computer Science | not yet | 0 of 20 PDFs published | n/a | no; see section 4 |

The earlier decks are unchanged: Accountancy 866, Biology 1,394, Business Studies 901, Economics 1,195, English 350, Political Science 1,096. Tiers: 3,165 of 12,540 cards are Must-know.

**How the pipeline works:**
1. **Write and review.** The workflow `handoff-1102/content-wave2.js` runs one Sonnet author per NCERT chapter PDF, then one independent Sonnet reviewer. It runs K PDFs at a time.
   - Authors write `ncert-books/drafts/<code>.json`; reviewers write `ncert-books/reviews/<code>.json`.
   - Both skip a file that already exists, so a stopped run resumes cleanly.
   - It has a NOTATION rule for physics and mathematics: no formula whose meaning a flattened line would lose.
2. **Publish** in the web repo, worktree `wt-1101-content`, branch `web/1101-content` (= main 7f1b204a7):
   1. `node scripts/keycards/review-merge.mjs`
   2. `node scripts/keycards/validate.mjs --subject=<s>`, one subject at a time. A full run would also rebuild the older decks; it is idempotent, but slower.
   3. `node scripts/keycards/tier.mjs`
   4. `test:keycards` and `test:learn`
   5. Commit only `data/keycards`, then `git checkout -- logs/`.
3. **Rule change on 1 Nov:** `importanceRight` is advice only in review-merge, because tiers.json decides Must-know. exact, important and unambiguous still decide publication.
4. **Look before shipping** with the preview: start `content-look` from `.claude/launch.json` (port 3492, `wt-1101-content`), then run `node handoff-1102/content-look.mjs http://localhost:3492 <out> "<chapterKey>,<chapterKey>"`.
   - The preview student `sciences` takes the new subjects.
   - URLs need `decks=real`.
   - A seeded student with 42 due cards gets 4-card feeds. That is the backlog rule, not a bug.
5. **Chemistry notation** is drawn by `src/components/learn2/stage/sciText.mjs` (chemistry cards only), tested in `pagerModel.test.mjs`. It covers formulas, ion charges, complex-ion charges, NCERT's en-dash minus, electron configurations and monatomic ions.
6. **Accountancy chapter 1** now defines partnership by Section 4 (Ch 1, p. 2). The Ch 2 restatement is held as its duplicate. Both are recorded in the review files, so they survive any publish run.

## 4. Computer Science: exact state and how to finish it
**On disk** (`C:\Users\atish\Desktop\mockmob copy\ncert-books`):
- Drafts lecs101 to lecs110 are written (all valid JSON).
- Reviews lecs101 to lecs108 are written.
- Still missing:
  - reviews for lecs109 and lecs110
  - drafts and reviews for lecs111 to lecs113 and leip101 to leip107
- The wave was stopped on purpose at the handoff.

**Steps:**
1. **Resume** with the Workflow tool, `scriptPath` = `C:\Users\atish\Desktop\mockmob copy\handoff-1102\content-wave2.js`, and args = `{"subjects": ["computer_science"], "k": 3, "chapters": {"computer_science_B1": [...], "computer_science_B2": [...]}}`.
   - Take the two lists from `handoff-1102/wave3-chapters.json` exactly.
   - Read them from the file and compare before launching. A retyped em dash nearly mislabelled a History chapter.
   - Finished PDFs are skipped.
2. **Cost:** about 1.2% of the 5-hour window per PDF; about 12 PDFs are left.
3. **Publish** as in section 3, then look at 1 to 2 cards, run `next build --webpack`, add a STATUS entry and fast-forward main.
   - The build may flake once in next/font while fetching Google Fonts; retry once.
4. **Check the deploy** with `list_deployments` and `get_runtime_errors`.

## 5. The next real piece of work: Maths formula cards (proposed, not started)
- **The problem:** pdftotext flattens powers, fractions, integrals and matrices, so Maths cards hold only words (260 cards). Some chapters are thin: Three Dimensional Geometry has 1 card; Inverse Trigonometric Functions and Vector Algebra have 5 each.
- **The plan:**
  1. Render the NCERT pages to images (`pdftoppm`).
  2. Authors transcribe formulas from the image into LaTeX, keeping NCERT's exact words around them.
  3. An independent reviewer compares the rendered LaTeX with the page image.
  4. `validate.mjs` learns the new field.
  5. KaTeX draws the formulas for maths and physics cards only. Check the version, licence and bundle size.
- **Target:** Maths at least 400 cards, at least 15 per chapter, looked at on screen, tests green.
- **Note:** the proposal card was made in the old account only. Start it as a session in the new account if the owner agrees, or ask him first. It is a sizeable job.

## 6. Other open items, most useful first
1. **The owner's look at the live site:** record his words verbatim first (`OWNER-FEEDBACK-2026-10-31-LEARN.md`, ledger, NOW), then fix in one round.
2. **LK25, a fresh Play release:** waits on the app port session (worktree `wt-1101-learn-app`, branch `ui/1101-learn-app`; its emulator walk). Check that session's state; the owner uploads the AAB.
3. **English top-up:** about 300 more cards; English is about 1.7 h now. Also Accountancy's thin chapters. GAT has no NCERT book.
4. **Quarantine recovery round:** many held-back cards fail only on `front_dangling` or `front_too_long`. A fix pass plus an independent re-review could recover hundreds, the same way the earlier "fix round 2" recovered 88.
5. **Pre-existing failing suites:** test:authored-publish 13, test:factory 5, test:mob 7 and test:study 1 (the WordNet licence). They also fail on main 978edc236, so they come from earlier work.

## 7. Worktrees, tools and locks (all under `C:\Users\atish\Desktop\mockmob copy`)
- **Worktrees:**
  - `wt-1101-content`: `web/1101-content` = main. The place for content.
  - `wt-1031-learn-v2`: `web/1031-learn-v2` at 668341aea. Learn v2 code history; main has moved past it.
  - `wt-1101-r2-home|run|explore|speed|hero`: round-4 packet branches, all merged. Reuse them for fix packets (`git checkout -B <new> <base>`).
- **`handoff-1102/`** holds this session's scripts:
  - `content-wave2.js`: the card wave
  - `r3-fix.js`, `r4-fix.js`: five-packet fix-round templates
  - `r3-look.js`: capture plus 5 review lenses plus skeptic verification. It is expensive, so prefer a local capture and your own look.
  - `content-look.mjs`
  - `chapters-9.json`, `wave3-chapters.json`
  - `run_suites.sh`: per-suite pass/fail counts
  - `resolve_union.py`: NOTES.md merge conflicts
- **Locks:**
  - Dev slots: `tmp-devslots\slot-1|slot-2`, at most 2 dev servers.
  - Browser lock: `tmp-devslots\browser.lock`, one headless browser at a time.
  - All were empty at handoff.
- **`.claude/launch.json` configs:** `content-look` (3492) and `learn-r4-look` (3491). Use `preview_start`, never Bash, for dev servers.

## 8. What this session learned (in memory too: subagent-wave-pacing, workflow-agent-stalls)
- **Usage:**
  - Card waves cost about 1.2% of the 5-hour window per PDF.
  - A 73-agent review round (Opus critics reading 180 screenshots) cost about half a window.
  - A five-packet fix round costs about 15-18%.
  - The orchestrator's own turns get expensive once its context is large.
- **A workflow agent can stop** while waiting on its own Monitor and return one line. Check every packet worktree's `git log` and `git status` before trusting reports. R4-server had to be finished by hand: its suites were run, then it was committed.
- **Never `rm -rf logs/...`:** tracked files live there. Use `git checkout -- logs/`.
- **In Git Bash, never `find /c`:** it walks the whole drive. Count processes in PowerShell.
