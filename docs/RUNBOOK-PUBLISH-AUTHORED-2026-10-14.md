# Runbook: publish the agent-authored wave 1 and make it NTA-eligible (14 Oct 2026)

Status: **tooling only. Nothing here has been run against production or staging.** Every number below was produced offline, from the committed candidates, the committed score entries, the committed agent and CUET-fit tables and the 13 Oct local export of the bank (`tmp/nta-fixtures`). Publication needs the owner's approval (FACTORY-RUN-2026-10-14.md section 4, item 6).

Update, 14 Oct (later): `wip/cuet-fit` is merged into `fix/nta-mode` (merge `47e0880`, engine `nta-engine-2026.10.13-r5`: the CUET-fit gate, the judges' stored type and chapter first, newest questions preferred), and section 3's `merge` has been run and committed (`d593e84`): the agent **and** fit tables of the six subjects carry the 475 entries. Section 3's numbers below are from the r5 engine with those tables. Not pushed, not deployed.

What is being published: the **475 final candidates** of `docs/brain/reports/authored/wave1-candidates-final-2026-10-14.json` (source `claude-authored-2026-10-14`; AUTHORED-QUESTIONS-WAVE1-2026-10-14.md says how they were made and checked). They are the 479 wave-1 candidates, kept unchanged in `wave1-candidates-2026-10-14.json` for history, minus the 4 that failed the fresh judge pass and with the 19 that the engine refused reworded (same ids).

| Piece | File |
| --- | --- |
| Row mapping and plan (pure) | `scripts/lib/authored-wave.mjs` |
| Judge files to score entries (pure) | `scripts/lib/authored-scores.mjs` |
| Publish, with dry-run, apply, restore | `scripts/question-publish-authored.mjs` |
| Offline candidates, score merge and engine check | `scripts/authored-scores-merge.mjs` |
| Tests (no network, 55 tests) | `data/tests/authored_publish.test.mjs`, `npm run test:authored-publish` |
| Final candidates, and the 4 dropped with their reasons | `wave1-candidates-final-2026-10-14.json`, `wave1-dropped-2026-10-14.json` |
| Judge records, durable (the raw `tmp/authored` files are untracked) | `wave1-score-entries-final-2026-10-14.json` |
| Offline engine check of the final set | `wave1-score-check-final-2026-10-14.json` |
| As first built, kept for history | `wave1-candidates-2026-10-14.json`, `wave1-score-entries-2026-10-14.json`, `wave1-score-check-admit-...json`, `wave1-score-check-hold-...json` |

All under `docs/brain/reports/authored/`.

## 0. What changed after the first build, and what is settled

1. **Fresh judge pass on the 60 repaired-text questions** (batches fr-01 to fr-04: two quality judges and three fit judges each, claude-haiku-5-5, 14 Oct). 56 passed. 4 failed the wave's acceptance rule and are **dropped**:

   | Id | Subject | Why |
   | --- | --- | --- |
   | `5417fab7-c777-435a-851d-c06d92c7480a` | english, set `english__p1__set3` | fit judges 8/6/4 (median 6, bar 8) |
   | `2aeac152-79f9-4bc3-b24d-a4fe11c51c3b` | history | quality judges 7/3, flag `duplicate_options` |
   | `bfe02c5b-46a2-478e-a826-fc0392cdff7f` | political_science | quality judges 6/8 (bar 7 each) |
   | `7620ca67-81e1-4155-8b15-c0f56c847aff` | political_science | quality judges 6/7 |

   Consequences: the dropped English question leaves its set with **3 children**, below the engine's minimum of 4, so that set is published (practice and full mock show it) but **never served in NTA mode**. One Political Science chapter (Globalisation, which had a single authored question) now has none.
2. **The 19 engine-refused questions were reworded** (same ids, minimally; batch rw-01-final) and re-judged: 5 blind solvers each (all 19 were 5 of 5 on the key), two quality judges (7 or more, no flags), three fit judges (median 8 or more). The 15 "according to" stems, the one "mainly" stem and the three sign-only option sets are fixed; the engine now refuses none of the 475. Two of the 19 were also in the fresh-60 set; their fresh-60 results judged the older wording, so they are ignored (the builder only uses a fresh result whose batch text equals the final text).
3. **`--repaired-text=admit|hold` no longer changes anything.** Every question whose hashed text differs from what its first judges saw was re-judged on the final text, so no entry binds scores to text the judges did not see (`hashChangedByRepair: 0`; `hold` and `admit` give identical tables, a test checks it). The flag stays mandatory and the runbook uses `admit`. 74 entries still carry first-pass judges on a text that differs only in the difficulty label or the NCERT reference, which are not in the content hash.
4. **Judge model: claude-haiku-5-5 throughout** (confirmed by the orchestrator, including the original wave-1 judges), so the agent threshold (7 of 10 on each judge, calibrated 13 Oct on that model) applies.
5. **The build refuses an unaccepted question.** `--mode=entries` gives no entry, and exits with a problem, for any question whose records fail the rule (4 of 5 solvers on the key, both quality judges at 7 or more with no flag and the key as blind answer, fit median 8 or more, fewer than two fit flags). So a failing question has to be dropped before the tables can be built.

Offline engine check of the final set (`ntaEligibility` of engine r5 run on every planned row with the merged agent and fit tables, the same gates the website uses, the CUET-fit gate included): **475 of 475 admitted**, the builder's fit-gate mirror 475 of 475, no refusal reasons. The committed tables give the same through the engine's defaults (a test checks it). By subject (admitted of planned): Chemistry 95/95, English 58/58, History 81/81, Political Science 81/81, Psychology 79/79, Sociology 81/81. English passage sets servable: **11 of 12** (the 3-question set is not).

For history, the first build (479 candidates, original judges) gave 460 admitted under `admit` and 402 under `hold`, with 19 content refusals; its tests still run against the kept first-build files.

## 1. Tests

```
npm run test:authored-publish
```

Expected: 55 tests, 0 failures. They need no network and no `.env`. One test compares the builder's fit-gate mirror with this checkout's `data/nta_fit_scores.js` (`NTA_FIT_CHECKOUT` names another checkout); one checks that the committed tables admit all 475 through the engine's defaults, so it fails until section 3's `merge` is committed (it is, `d593e84`).

The other suites on this branch after the merge: `npm run test:nta` 134 tests, `test:recovery` 40, `test:question-reorder` 26, `test:nta-e2e` 418 (needs `tmp/nta-fixtures` and the signing key in `.env.local`, both local; no network). All pass.

## 2. Candidates and entries (already built and committed; rebuild only if `tmp/authored` changes)

```
node scripts/authored-scores-merge.mjs --mode=candidates-final --reword=tmp/authored/fresh/rw-01-final.json
node scripts/authored-scores-merge.mjs --mode=entries --quality-model=claude-haiku-5-5 --fit-model=claude-haiku-5-5 --solver-model=claude-haiku-5-5 --fresh=tmp/authored/fresh
```

`candidates-final` takes the wave-1 candidates (`--original-candidates`), removes the ids of `wave1-dropped-2026-10-14.json` and replaces the text of the reworded ids; it refuses a reword that changes a question's subject, chapter, type, set or passage, a drop without a reason, and a set left with fewer than 2 questions. Expected: 475 candidates, 4 dropped, 19 reworded, 12 passage groups (eleven of 5 children, one of 3).

`entries` expected: `ok: true`, 475 entries, 0 problems, 134 repaired, 73 judged on the final text by the fresh pass, 19 reworded after wave 1, 10 stale fresh results ignored (the five fr-batch judges of each of the two questions that were reworded afterwards). Each reworded entry records `reworded_after_wave1` (the fields), the engine reasons it was reworded for, `expert_reviewed_text: "earlier_text"` and the blind re-solve as `blind_resolve_on_earlier_text`.

## 3. Merge the score tables, then check (offline; done and committed in `d593e84`)

```
node scripts/authored-scores-merge.mjs --mode=merge --repaired-text=admit
git diff --stat data/nta_agent_scores data/nta_fit_scores
node scripts/authored-scores-merge.mjs --mode=check --repaired-text=admit --impact=tmp/nta-fixtures --report=docs/brain/reports/authored/wave1-score-check-final-2026-10-14.json
npm run test:nta
npm run test:authored-publish
```

`check` builds the merged tables in memory from the entries and the tables on disk and runs engine r5's `ntaEligibility` with them (`agentScores` and `fitScores`), so it gives the same answer before and after `merge`. Expected: `planned: 475`, `agentEntries: 475`, `engineEligible: 475`, `engineIneligible: 0`, `fitGate.pass: 475`, `fitGate.baseTablesMissing: []`, `qualityAndFitBoth: 475`, `hashChangedByRepair: 0`, `heldForFreshPass: 0`, `passageSets: 11 of 12 servable`. By subject: chemistry 95, english 58, history 81, political_science 81, psychology 79, sociology 81, all eligible.

Offline paper check (`--impact`, the 13 Oct export of the bank; the five short subjects carry no factory evidence, so the engine can score them without the signing key). Engine r5, so "before" is the bank under the quality AND fit gates with the committed tables, "after" adds the authored rows with the merged tables. Three papers in a row for one simulated student, each leaving out the earlier papers' questions:

| Subject | Eligible rows before, after | Papers before | Papers after (questions) |
| --- | --- | --- | --- |
| Chemistry | 57, 152 | refused x3 | 50, 50, 50 |
| History | 23, 104 | refused x3 | 50, 50, 50 |
| Political Science | 30, 111 | refused x3 | 50, 50, 50 |
| Psychology | 36, 115 | refused x3 | 50, 45, 50 |
| Sociology | 53, 134 | refused x3 | 50, 50, 50 |

(Under engine r4.1, before the fit gate, the "before" column was 107, 34, 42, 41, 63.) All "after" papers are `closest` (not `exact`): a paper of 45 to 50 questions that deviates from the blueprint somewhere (for example a difficulty or type minimum). This is an approximation: the export is from 13 Oct and ignores the 15 questions held since. English is not in this table: its pool carries factory evidence.

**Recency.** The planned rows have no `created_at` (the database sets it on insert), so in this check the engine treats them as undated and least new. Live, they are the newest rows, and r5 prefers the newest questions first (owner, 13 Oct). Re-run offline with `created_at` set on the authored rows, the three papers take this many authored questions out of 50: Chemistry 47, 40, 31; History 47, 37, 46; Political Science 47, 39, 41; Psychology 44, 38, 39; Sociology 47, 25, 40. So, once published, a student's first NTA paper in these subjects is about nine-tenths authored questions.

`merge` rewrites `data/nta_agent_scores/{chemistry,english,history,political_science,psychology,sociology}.json` and `data/nta_fit_scores/<the same six>.json` with the authored entries added; every other entry is untouched (checked table by table, and a test checks it). In the agent tables `merged_at` and `measures.admissible_before_row_checks` change and an `authored` block is added (`models` stays `claude-haiku-5-5`). Entries per agent table: Chemistry 300 to 395, English 277 to 335, History 197 to 278, Political Science 198 to 279, Psychology 87 to 166, Sociology 212 to 293 (475 added in all). `measures.admissible_before_row_checks` per table: 125 to 220, 96 to 154, 53 to 134, 59 to 140, 53 to 132, 82 to 163 (the other `measures` are left as the base merge wrote them).

In the fit tables only `merged_at` changes and an `authored` block is added; `measures` and `status` (`complete`) are left as `scripts/nta-fit-merge.mjs` wrote them. Entries per fit table: Chemistry 125 to 220, English 96 to 154, History 53 to 134, Political Science 59 to 140, Psychology 53 to 132, Sociology 82 to 163. Authored fit pass at 8: all 475; at 9: chemistry 77, english 41, history 58, political_science 51, psychology 56, sociology 53.

Re-running `merge` is safe: authored entries are replaced in place, any other entry with the same id makes it refuse, and with the same `--now` it reproduces all twelve files byte for byte (`engine_type_guess` is the engine's heuristic guess, `heuristicNtaType`, so a committed entry's stored type does not feed back into it). On a checkout without `data/nta_fit_scores` (a branch from before the CUET-fit merge) `merge` writes only the agent tables (`fitTablesWritten: false`); to write fit tables elsewhere pass `--fit-base=<dir> --fit-out=<dir>`.

## 4. Dry run (reads the target; writes no row)

The target is the project in `.env.local`. The 13 Oct export names project `isrxrxzjocewrdureyhp`; the script stops if the URL's project ref differs from `--expect-project`.

```
node --use-system-ca scripts/question-publish-authored.mjs --mode=dry-run --expect-project=isrxrxzjocewrdureyhp
```

It reads: that each column the insert writes exists in `questions` and `passage_groups`, which planned ids and group ids already exist, and the live count per subject. It writes `docs/brain/reports/authored-publish/authored-publish-plan-<stamp>.json` (every row and group that would be written, the plan hash, the checks). Exit code 2 when there are blockers.

Expected, with the agent and fit tables merged and committed (they are; the offline run below gave exactly these values on 14 Oct after `d593e84`):

| Field | Value |
| --- | --- |
| `summary.questions`, `passageGroups`, `chapters` | 475, 12, 61 |
| `summary.bySubject` | chemistry 95, english 58, history 81, political_science 81, psychology 79, sociology 81 |
| `summary.byType` | conceptual_mcq 260, statement_based 64, sequence_ordering 37, match_the_following 48, reading_comprehension 58, assertion_reason 8 |
| `summary.byDifficulty` | medium 269, easy 188, hard 18 |
| `summary.byExpertReview` | ready 341, repaired 134 (19 rows also carry the tag `authored_revision:reworded`) |
| passage sets | 12 sets: eleven of 5 children, `english__p1__set3` of 3 |
| `warnings` | one: `english__p1__set3` has 3 questions, below the NTA minimum of 4 (not a blocker) |
| `candidatesSha256` | `18b27c06748db793cfc30d13515b3aa6bb3190d03a93c0820c9402be4ed0b69e` |
| `planHash` | `39a4b051475df71b02778f5ad8dfdc7fb4c6c96e76d8e1fc82e019a024b3fca2` |
| `checks.questionColumnsMissing`, `passageGroupColumnsMissing` | 0, 0 |
| `checks.existingQuestionIds`, `existingGroupIds` | 0, 0 (the authored uuids are new; any other number is a blocker) |
| `checks.agentScores` | bound 475, missing 0, hashMismatch 0 |
| `checks.fitScores` | bound 475, missing 0, hashMismatch 0 (on a checkout without `data/nta_fit_scores`: "not checked") |
| `checks.bankLookalikes` | exact 0, nearStem 0 (against the local 13 Oct export; informational) |
| `blockers` | `[]` |

Run offline (no database, so no column, id or count check; it says so):

```
node scripts/question-publish-authored.mjs --mode=dry-run --offline
```

A different `planHash` means the row mapping or the candidates changed since this runbook was written; read the plan before approving it.

## 5. Apply

Only after the owner approves the dry-run file.

```
node --use-system-ca scripts/question-publish-authored.mjs --mode=apply --plan=docs/brain/reports/authored-publish/authored-publish-plan-<stamp>.json --reason="owner approved wave 1 publication <date>" --expect-project=isrxrxzjocewrdureyhp
```

What it does, in order: re-plans from the candidates file the dry run named (their sha256 and the plan hash must match, else it stops); checks the columns; **refuses if any planned question id or group id already exists** (it only ever inserts, never updates, so an existing row cannot be overwritten); refuses rows without score entries bound to their hash unless `--allow-unscored`; writes `authored-publish-restore-<stamp>.json` **before the first insert**; inserts the 12 passage groups, then the questions in chunks of 50; reads everything back.

Expected output: `inserted: 475`, `groupsInserted: 12`, `missing: []`, `notVisible: []`, `hashMismatch: []`, `groupsMissing: []`, and `liveAfter` equal to `liveBefore` plus 95, 58, 81, 81, 79, 81 for chemistry, english, history, political_science, psychology, sociology.

Each row is written as: `status live`, `verification_state verified`, `exploration_state active`, `exploration_lane none`, `ai_tier PENDING`, `quality_band unrated`, `source claude-authored-2026-10-14`, tags naming the run, wave, type, unit, expert review and NCERT reference, `live_at` set to the apply time. `provenance`, `evidence`, `legacy_screening` and the database `content_hash` stay NULL on purpose (see section 9). Commit the plan and restore files afterwards, as the earlier hold runs did.

Then: deploy the code that carries the merged tables if it is not already deployed (until it is, the rows are visible in practice and invisible to NTA mode). The NTA pool is cached in memory for 5 minutes (`NTA_POOL_CACHE_MS`), so a new paper picks the rows up within that time. To confirm, run the existing read-only `scripts/nta-engine-run.mjs`.

Deploying this branch also deploys engine r5 for **every** subject, not only these six: the CUET-fit gate, the judges' stored type and chapter, and newest-first selection (docs/brain/NTA-ENGINE-POLICIES.md section 10; the read-only production run is docs/brain/NTA-ENGINE-RUN-FIT.md). On the 13 Oct export (`npm run test:nta-e2e`), against r4.1: General Test serves 46 questions instead of 50 and can refuse a student's later paper; Mathematics goes from a 47-question paper to a refusal; Biology goes from a refusal to a 46-question paper; with synthetic scores (the e2e "promoted" mode) History, Political Science and Sociology go from served to refused (without the authored rows). The other served subjects keep 50-question papers.

## 6. Restore

```
node --use-system-ca scripts/question-publish-authored.mjs --mode=restore --restore=docs/brain/reports/authored-publish/authored-publish-restore-<stamp>.json --expect-project=isrxrxzjocewrdureyhp
```

Default **hide**: the 475 rows go to the withheld state of `scripts/question-hold.mjs` (`pending`, `disputed`, `pending_review`) and `is_deleted = true`, and the 12 groups to `hidden` / not discoverable. This keeps attempt history. Only ids named in the restore file, only rows still from this source. `--hard-delete` deletes the rows that are still exactly as written (skipping any edited since), then the groups no question points at; tables that reference questions with `ON DELETE CASCADE` lose their rows for these ids, so use it only before any student has seen them. The same command cleans up after a failed apply: the error message names the restore file, which already lists every intended id; ids that were never written are skipped.

## 7. A further fresh judge pass (another wording, or a question dropped and replaced)

`--mode=rejudge-list` lists the questions whose judged text differs from the final text in a way the content hash covers; on the final entries it lists none. To re-judge anything else, save the batch text the judges were given as `<batch>.json` (`{ "batch": ..., "questions": [...] }`) next to their results `<batch>__j1|j2|h1|h2|h3.json` (and `<batch>__s1..s5.json` for fresh blind solvers) in one directory, then:

```
node scripts/authored-scores-merge.mjs --mode=entries --quality-model=claude-haiku-5-5 --fit-model=claude-haiku-5-5 --solver-model=claude-haiku-5-5 --fresh=tmp/authored/fresh --fresh=<dir>
node scripts/authored-scores-merge.mjs --mode=merge --repaired-text=admit
```

A fresh result replaces the original of its role only where its batch text equals the candidate's text (a result on an older wording is counted as stale and ignored), all five judges of a question must be fresh together, and the question must pass the acceptance rule or the build refuses it. A reworded candidate changes the plan hash, so run the dry run again.

## 8. After publication

- Update `docs/brain/STATUS.md` with the dry-run counts, the apply read-back and the engine check.
- The Explore feed reads `question_scores` rows, which direct inserts do not create, so these questions do not appear in Explore. Practice, full mock and NTA mode read `questions` directly. Say so if the owner expects them in Explore.
- Select-only checks to run in the SQL editor: `select subject, count(*) from questions where source = 'claude-authored-2026-10-14' and not is_deleted group by 1;` (95, 58, 81, 81, 79, 81) and `select count(*) from passage_groups where source = 'claude-authored-2026-10-14';` (12).

## 9. Why the rows look the way they do

- `provenance` is NULL. `isEvidenceManaged` (`data/question_factory_policy.mjs`) treats any row with `provenance` as factory-managed, and `legacyPracticeVisible` (`data/practice_availability.js`) then hides it from practice unless it carries a full signed evidence record. Where the questions came from is in `source`, the tags, the score tables and the restore file. A test pins this.
- `evidence` is NULL: the engine's agent path reads only rows without evidence (`loadNtaAgentRows`), and these rows are scored by the agent tables, not by signed factory evidence.
- The database `content_hash` column is NULL, like all 5,339 live rows exported on 13 Oct. It is body plus key only and unique among undeleted rows, and many English passage questions share a generic stem and key.
- `question` and `correct_index` are NULL, as on 5,324 of the 5,339 live rows; the reader uses `body` and `correct_answer`.
- Passage children carry `passage_group_id`, `passage_id`, `passage_text` and a 1-based `order_index`; the group id is `pg_` plus 32 hex digits derived from the set id, so a re-run writes the same group. Group titles are the passage type ("Factual Passage" and so on), because the authored sets have no titles.
- `author_id` and `uploaded_by` are NULL (the 15 seed rows are the only other live rows without an author; the column is nullable since migration 0007).
- The NTA content hash in the score tables is `contentHash` of the planned row (`scripts/lib/authored-wave.mjs` `contentHashOf`); a test checks the hash of every planned row against the engine's.

## 10. Open questions for the owner

1. Publish now, after reading the dry-run file?
2. The English set `english__p1__set3` has 3 questions and will not be served in NTA mode. Publish it for practice as it is (the plan does), author one replacement question for it (one more question and a judge pass would make it servable), or drop its three questions from the publish set (add their ids to `wave1-dropped-2026-10-14.json` and rebuild)?
3. Political Science "Globalisation" has no authored question left. Cover it in wave 2?
4. ~~Merge `wip/cuet-fit` into `fix/nta-mode` before the fit entries are merged?~~ Done locally on 14 Oct (`47e0880`, tables `d593e84`); not pushed or deployed.
5. Should these appear in Explore (needs `question_scores` rows, a separate step)?
6. Deploying engine r5 changes NTA mode for every subject (section 5). Accept that together with this publication, or deploy and watch it separately first?
7. Under r5's newest-first rule a student's first NTA paper in Chemistry, History, Political Science, Psychology and Sociology would be about nine-tenths authored questions, all judged by claude-haiku-5-5 agents with no human reading (section 3, Recency). Is that acceptable, or should the authored share per paper be capped?
