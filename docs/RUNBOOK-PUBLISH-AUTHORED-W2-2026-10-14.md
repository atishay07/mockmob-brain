# Runbook: publish the agent-authored wave 2 and make it NTA-eligible (14 Oct 2026)

Status: **tooling and tables only. Nothing here has been run against production or staging.** (A first dry run on 14 Oct showed 77 General Test rows planned under the subject `general_test`; the bank stores that paper as `gat`. Fixed the same day, see section 1, item 9. **Any plan file written before that fix, plan hash `89e4b3c6...`, is void: do not apply it.**) Every number below was produced offline, from the committed final candidates, the committed score entries, the committed agent and fit tables and the 13 Oct local export of the bank (`tmp/nta-fixtures`). Publication needs the owner's approval, as for wave 1 (`RUNBOOK-PUBLISH-AUTHORED-2026-10-14.md`, which this mirrors; read it for the mechanics that are not repeated here).

What is published: the **382 final candidates** of `docs/brain/reports/authored-w2/wave2-candidates-final-2026-10-14.json` (source `claude-authored-2026-10-14-w2`, tag `authored_wave:2`). They come from 451 questions written in 7 subjects (Biology, Computer Science, English verbal, General Test, Geography, Mathematics and Political Science Globalisation, 60 to 80 each), checked by 5 blind solvers, 2 quality judges and 3 CUET-fit judges per question (all claude-haiku-5-5), then an expert pass, an independent spot-check of 60, a fresh judge and solver pass on the 10 questions the engine refused and that were reworded, a review in this pass, a blind re-solve of the 12 held repaired questions (all 12 came back), and a second-reviewer and Geography NCERT recheck that dropped 14.

| Piece | File |
| --- | --- |
| Row mapping and plan (pure, wave aware) | `scripts/lib/authored-wave.mjs` |
| Judge files to score entries, provenance per wave | `scripts/lib/authored-scores.mjs` |
| Acceptance, final assembly (`--mode=final`), engine check (`--mode=check --final`) | `scripts/authored-w2-accept.mjs` |
| Score merge and engine check (check, merge) | `scripts/authored-scores-merge.mjs` |
| Publish, with dry-run, apply, restore | `scripts/question-publish-authored.mjs` |
| Tests (no network): wave 1 (56) and wave 2 (26) | `data/tests/authored_publish.test.mjs`, `data/tests/authored_w2.test.mjs`, `npm run test:authored-publish` |
| Final candidates and score entries | `wave2-candidates-final-2026-10-14.json`, `wave2-score-entries-final-2026-10-14.json` |
| Every drop with its category and reason; the hand decisions behind some of them | `wave2-dropped-2026-10-14.json`, `wave2-drop-decisions-2026-10-14.json` |
| Acceptance of the raw files (per question, with the final outcome) | `wave2-acceptance-2026-10-14.json` |
| Offline checks of the final set | `wave2-engine-check-final-2026-10-14.json`, `wave2-score-check-final-2026-10-14.json` |
| Expert verdicts, the supplementary review of this pass, the spot-check | `expert/*.json`, `expert/supplement-2026-10-14.json`, `wave2-spotcheck-2026-10-14.md` |
| As first accepted, kept for history | `wave2-candidates-asjudged-2026-10-14.json`, `wave2-score-entries-asjudged-2026-10-14.json` (390 questions) |

All under `docs/brain/reports/authored-w2/`.

## 0. What is in, what is out

By subject (written, accepted by the rule after the re-run of the judge files, accepted at the first pass, **final**, dropped from the accepted ones):

| Subject | Written | Accepted by the rule | First pass | **Final** | Dropped |
| --- | --- | --- | --- | --- | --- |
| Biology | 60 | 56 | 56 | **56** | 0 |
| Computer Science | 80 | 78 | 78 | **76** | 2 |
| English (verbal items 54, one passage question) | 61 | 55 | 55 | **55** | 1 |
| General Test | 80 | 77 | 72 | **77** | 0 |
| Geography | 80 | 67 | 51 | **44** | 26 |
| Mathematics | 80 | 68 | 69 | **65** | 6 |
| Political Science (Globalisation) | 10 | 9 | 9 | **9** | 0 |
| Total | 451 | 410 | 390 | **382** | 35 (some were accepted only this time) |

Drops, 35 in all (`wave2-dropped-2026-10-14.json`, one entry each with its reason):

| Category | n | Why |
| --- | --- | --- |
| `held_key_correct_solvers_disagree` | 1 | `87c9264b`: held, not rejected, and kept out of NTA. The key D is right by explicit computation, but the fresh blind solvers did not reach 4 of 5 on it (0 of 5, all answered A) and the rule stands. See section 7. |
| `geography_ncert_recheck_practice` | 9 | Second-reviewer Geography NCERT recheck, verdict practice: `4e27ea47` (NCERT teaches three stages, not four), `a1a985d8` (rote state ranks beyond NCERT), `ff6a9f3a` (not NCERT wording), `47f514b2` (overlapping descriptions, telegraph detail not NCERT), `819e826f` (National Highway 44 by number not NCERT), `af69a573` (balance of trade over goods and services), `f3b33c2c` (Kiel Canal and Malacca not clearly NCERT), `bcfc7ea5` (mainly Class 10 content), `e4a0e47c` (terms and cited section not clearly NCERT). |
| `geography_ncert_recheck_reject` | 4 | Same recheck, verdict reject: `8b40da05` (keyed HDI component is not NCERT's), `f5ceaadd` (arbitrary ranking of tertiary above quaternary), `86fa69db` (soil types, Class 10 and 11), `0457ce26` (planning and NITI Aayog, economy or polity). |
| `second_reviewer_practice` | 1 | `75dc1722`: pipelines carrying ore slurry make the key railways not uniquely correct for lowest cost per tonne-km; practice, not graded NTA (the Geography recheck said the same). |
| `near_duplicate` | 4 | `be0982b3` `8ee1a4be` `0a894f70` `e8315021`, each a restatement of a kept question (the partner is named in the reason). |
| `identical_to_live_question` | 2 | `3860696b` and `524da815`: the stem equals a live question in the 13 Oct export. |
| `spot_check_practice_grade` | 3 | `1445658c` (treaty dates are not Class 12 Geography), `fdbdd72a` (HDI index arithmetic, not NCERT), `3fcbe4d0` (balance of trade defined over goods only against NCERT's goods and services). |
| `spot_check_probable_reject` | 1 | `f6ef948f`: the key marks "the balance of trade includes invisible items" as false, which the NCERT Geography wording makes true, so no option is correct. |
| `expert_verdict_not_publishable` | 3 | `ad34719d` (expert verdict practice: geometric-mean HDI is beyond NCERT), and two of this pass's own review, `1b79114f` (dates of technology milestones, off syllabus) and `dff435fd` (balance of trade over visible goods only). |
| `geography_ncert_recheck_hdi_banding` | 1 | `e32b79ff`: needs the UNDP cut-offs, which NCERT Class 12 Geography does not give. |
| `same_concept_repeat` | 3 | `9ddc9446` (Suez), `0ece0098` (Golden Quadrilateral), `812f00de` (west-coast ports): the same fact as a question that is kept. |
| `duplicate` | 3 | `26feae72` (a restatement of `3dc623cc`, accepted in this pass) and, since the 12 held questions came back, `06298513` (since 2015, against `8ea3affd`) and `66c40b7a` (sin 3x / x continuity, against `8e614805`): the screen keeps the first accepted copy. |

Not accepted by the rule (41 of the 451; a question can fail in more than one way; per question in the acceptance file): fit median below 8 (12), duplicate of an accepted question (16), quality score below 7 (9), too few solvers on the key (4, `87c9264b` among them), quality flag (4), expert verdict practice (3), fit flags (2), a judge's blind answer off the key (1).

## 1. What was done in this pass, and the rules it applied

1. **Acceptance re-run** with the re-run judge files (`general_test__b4` h1, `geography__b2` h1, `geography__b3` h2, `mathematics__b1` h1 and the rest): 451 questions, 240 of 240 result files present, 410 accepted by the rule once the 12 re-solves are in (400 before them; the first pass took 390). The `reword` folder of `tmp/authored-w2` is a fresh pass on later wording, not a subject: the script now skips it, and `expert` and `resolve`.
2. **The wave-1 fresh-pass rule for the 10 reworded questions**: a fresh result counts only when its batch text is the final text, all ten records (five solvers, two quality judges, three fit judges) are there, and the question then passes the rule on them alone. 9 of 10 pass (5 of 5 solvers on the key, quality 7 or more, fit median 8 or more). The tenth, `87c9264b`, fails (section 7; it is held with its reason in the ledger).
3. **A conflict found and settled.** The expert pass ran after the rewords and, for `a3eb6b10` (English, "He is ___ honest man"), set the reworded option A "a (before a consonant sound)" back to plain "a", the single-letter option the engine refuses. The final text is the reworded text that the fresh pass judged (the script reports it in `final_pass_inputs.text_set_to_the_fresh_pass`). The batch file in `tmp/authored-w2/english/english__v2.json` still has the expert's version.
4. **Expert verdicts** (`expert/*.json`, 390 questions: 350 ready, 39 repaired, 1 practice): practice and reject are dropped. Of the 39 repaired: 12 changed what blind solvers see (a stem or options) and came back through the blind re-solve of 14 Oct (section 6: 3 of 3 solvers on the key for each of the 12); 1 (`a3eb6b10`) was reworded afterwards and stands on its fresh five solvers; 1 (`fdbdd72a`) was dropped by the spot-check; the other 25 changed only the explanation, the difficulty label or the NCERT reference. For those 25 (and the 2 explanation repairs of this pass) the five original blind solvers saw the same stem and options, so their 4 or 5 of 5 on the key stands for the final text and no re-solve is asked for. This is the rule of this wave, not of wave 1 (which re-solved every repaired question); it is recorded per entry (`blind_solvers.on: "final"`, provenance `admitted_on_expert_verdict_blind_text_unchanged`).
5. **A supplementary review of 27 questions** that became accepted only after the re-run and so had no expert verdict (`expert/supplement-2026-10-14.json`): solved blind first, then key, explanation, distractors and NCERT reference checked. 23 ready, 2 repaired (explanation only: `75dc1722`, `c48dd176`), 2 practice (dropped). **One reviewer (Claude Sonnet 5.5, this session), not the 24 batch reviewers**; recorded in each entry as `supplementary_review`. 17 of the 27 are in the final set (the rest were practice, repeats of a question that came back from the hold, dropped by the rechecks of 14 Oct, or not accepted).
6. **Geography against NCERT wording**: this pass read all 55 Geography questions of the final set (the 14 that are new since the first pass solved blind first; the other 41 read with their keys and explanations) for balance of trade and payments, HDI and international dates. Result: the three practice-grade and the probable reject of the spot-check, `e32b79ff`, `ad34719d`, `1b79114f`, `dff435fd` were dropped; the three same-fact repeats from batch 3 were dropped. The 3 Geography questions that were held for a re-solve (`51db2fdf`, `c2a88140`, `d437d53e`, option lengths only) came back after this and were not part of that read. A second-reviewer Geography NCERT recheck followed (13 Geography items, solved blind first: 9 practice and 4 reject, all dropped, see section 0). NCERT itself was not available to this pass (no network), so "against NCERT wording" means against the wording the spot-check quotes and the reviewer's knowledge of Class 12 Fundamentals of Human Geography and India: People and Economy. The 44 final Geography items are the ones that survive both reads; a second reviewer over all of them is still not done (section 7).
7. **Sets.** `english__p1__set3` (3 children after wave 1's drop, so not served in NTA mode) gets its fourth child, `set3fix`, and becomes servable; it joins the wave-1 group (`_extends_set`), no group row is written. Geography batch 3 holds one case set (`geo-b3-settlement-set-1`, the Dhanaura settlement, 4 questions, 139 words, in the blueprint's range of 120 to 300): stored like a passage set (`passage_group_id`, `passage_text`, order 1 to 4, `question_type` `case_based`, passage kind null).
8. **Tooling extended, wave 1 untouched** (`npm run test:authored-publish`: the 55 earlier wave-1 tests are unchanged and green; one is added, item 9): `AUTHORED_SUBJECTS` gains the five subjects; a wave is its `source` (`WAVES`, `waveOf`); English verbal item types map to the live vocabulary (`fill_in_blank` to `correct_word_usage`, `sentence_rearrangement` to `para_jumble`, `idiom_phrase` to `idiom`, and the others as they are); case sets of Geography and a top-up child are mapped; provenance text and the `authored` block of the tables are per wave; `merge` writes only the subjects the candidates name; the publish script takes its source from the candidates and, for a top-up, checks that the wave-1 group is in the target.

9. **Subject id fix (14 Oct 2026, before any publish).** A candidate names its subject by the public id (`general_test`); the live bank stores General Test as `gat` (`data/cuet_controls.js`: `toInternalSubjectId` maps `general_test` to `gat`, `toPublicSubjectId` back). The plan wrote the public id into `questions.subject`, so the app's practice and NTA reads (which use `gat`) would never have seen the 77 General Test rows, and the dry run's `liveBefore` queried `general_test` and reported 0 (the lookalike check likewise compared General Test rows with no export rows at all). Now `toQuestionRow` and `toPassageGroupRow` store the internal id, so the rows, `summary.bySubject` (`gat` 77), the plan hash, the dry run's and apply's `liveBefore`/`liveAfter` reads, the lookalike check and the restore file's `subject` all use `gat`. The score tables and their files stay keyed by `general_test` (`data/nta_agent_scores.js` and `data/nta_fit_scores.js` map `gat` to it, the engine's `getNtaBlueprint` and `ntaEligibility` accept both); an entry is found by question id. **The content hash covers `subject`**, so the 77 General Test entries of both tables were bound to the `general_test` hash and the engine refused every row stored as `gat` (`question_changed_since_scored`, `fit_question_changed`). Both `general_test.json` tables were merged again (same command as section 3, same `--now`; only the `content_hash`, `scored_content_hash`, `judged_content_hash` and `final_content_hash` fields of those 77 entries changed, no score, flag, judge or other entry did, and no other subject's file changed). The 157 live General Test rows of the 13 Oct export are bound to their `gat` hashes in the same tables (agent 157 of 157, fit 101 entries, 0 mismatches), which is how the stored hash was confirmed. Wave 1 is unaffected: its six subjects have no alias (plan hash unchanged, `39a4b051...`). New: a warning in the dry run for a planned subject that has no live rows in the target (the symptom of a wrong id). Tests added: a planned `general_test` row has subject `gat`; the engine admits a `gat` row with the wave-2 entries and refuses the same row stored as `general_test`; the tables are bound to the `gat` hash; a General Test paper built from the export takes wave-2 rows only when they are stored as `gat`; the lookalike and live-count reads use `gat`; wave 1 has no alias.

## 2. Tests

```
npm run test:authored-publish
npm run test:nta
npm run test:nta-e2e
```

On this branch after the merge of the tables and the subject id fix: `test:authored-publish` 82 (56 of wave 1, 26 of wave 2; the last 3 of wave 2 read `tmp/authored-w2`, and the General Test paper test reads `tmp/nta-fixtures/gat.json`; they skip on a machine without them), `test:nta` 150, `test:nta-e2e` 418 (needs `tmp/nta-fixtures` and the signing key in `.env.local`, both local). All pass.

## 3. Rebuild (only on the machine that holds `tmp/authored-w2`; every output is committed)

```
node scripts/authored-w2-accept.mjs --mode=final --now=2026-10-14T12:10:00.000Z
node scripts/authored-w2-accept.mjs --mode=check --final --label=final --now=2026-10-14T12:10:00.000Z
node scripts/authored-scores-merge.mjs --mode=merge --repaired-text=admit --candidates=docs/brain/reports/authored-w2/wave2-candidates-final-2026-10-14.json --entries=docs/brain/reports/authored-w2/wave2-score-entries-final-2026-10-14.json --now=2026-10-14T12:10:00.000Z --impact=tmp/nta-fixtures --report=docs/brain/reports/authored-w2/wave2-score-check-final-2026-10-14.json
```

`--mode=accept` on its own (the command of the task) writes the acceptance, the rule-accepted candidates and their entries but not the `final` section of the acceptance file; `--mode=final` writes all of that and the final files. `final` reads the raw files, `expert/`, the as-judged candidates, the fresh pass (`tmp/authored-w2/reword`), the re-solves (`tmp/authored-w2/resolve`), the hand decisions and the spot-check, and writes the acceptance, the final candidates and entries and the ledger. `merge` rewrites `data/nta_agent_scores/` and `data/nta_fit_scores/` for the 7 subjects only (done and committed): 56, 76, 55, 77, 44, 65 and 9 entries added to Biology, Computer Science, English, General Test, Geography, Mathematics, Political Science; every existing entry is untouched (a test checks it); `merge` only adds, so after a drop the tables are reset to their pre-wave-2 state (`git checkout f72739f^ -- data/nta_agent_scores data/nta_fit_scores` for the 7 subjects) and merged again, otherwise an entry of a question that is no longer published stays behind (this pass did that); `merged_at`, `measures.admissible_before_row_checks` (agent) and an `authored["claude-authored-2026-10-14-w2"]` block change. Re-running with the same `--now` reproduces the files byte for byte (a test checks it).

Offline engine check of the final set (engine `nta-engine-2026.10.14-r5.2`, the same gates the website uses): `planned 382, engineEligible 382, engineIneligible 0`, fit gate 382, `hashChangedByRepair 25` (the explanation-only repairs, scored on the earlier explanation and admitted on the expert verdict), placement problems 0, passage sets servable 2 of 2.

Offline paper check (`--impact`, the 13 Oct export, three papers in a row for one simulated student; the six subjects have no factory evidence so the engine scores them without the signing key; approximation, as in wave 1):

| Subject | Eligible rows before, after | Papers before | Papers after (questions) |
| --- | --- | --- | --- |
| Biology | 125, 181 | closest 46, 45, 46 | closest 50, 50, 50 |
| Computer Science | 74, 150 | refused x3 | exact 50, closest 48, closest 50 |
| General Test | 75, 152 | closest 45, 45, 46 | exact 50, closest 50, closest 50 |
| Geography | 67, 111 | refused x3 | closest 50, 50, 50 |
| Mathematics | 99, 164 | refused x3 | closest 49, 47, 50 |
| Political Science | 30, 39 | refused x3 | refused x3 |

Political Science stays refused: 9 questions do not carry a section. English is not in the table (its pool carries factory evidence). Recency: the planned rows have no `created_at` here, so the engine counts them as least new; live they are the newest rows and r5 prefers the newest first, so a student's first paper in these subjects will draw many of them (wave 1's runbook, section 3, has the same caveat and the same open question 7).

## 4. Dry run (reads the target; writes no row)

The orchestrator runs it. The target is the project in `.env.local`; the script stops if the project ref differs from `--expect-project`.

```
node scripts/question-publish-authored.mjs --mode=dry-run --offline --candidates=docs/brain/reports/authored-w2/wave2-candidates-final-2026-10-14.json
node --use-system-ca scripts/question-publish-authored.mjs --mode=dry-run --candidates=docs/brain/reports/authored-w2/wave2-candidates-final-2026-10-14.json --expect-project=isrxrxzjocewrdureyhp
```

The first is offline (no column, id or count check). The second reads: that each column the insert writes exists, which planned ids and group ids already exist, that **the wave-1 group `pg_b1c0212d23fa9117786356ede1fc95f7` that the English top-up joins is in the target**, and the live count per subject. It writes `docs/brain/reports/authored-publish/authored-publish-plan-<stamp>.json`. Exit code 2 when there are blockers.

Expected (the offline run gave the plan values on 14 Oct):

| Field | Value |
| --- | --- |
| `source` | `claude-authored-2026-10-14-w2` |
| `summary.questions`, `passageGroups`, `chapters` | 382, 1, 65 |
| `summary.bySubject` | biology 56, computer_science 76, english 55, **gat 77** (General Test, the id the bank stores; not `general_test`), geography 44, mathematics 65, political_science 9 |
| `summary.byType` | conceptual_mcq 231, match_the_following 40, statement_based 33, sequence_ordering 23, correct_word_usage 12, para_jumble 9, synonym 7, antonym 7, assertion_reason 5, idiom 4, one_word_substitution 4, case_based 4, error_detection 2, reading_comprehension 1 |
| `summary.byDifficulty` | medium 202, easy 142, hard 38 |
| `summary.byExpertReview` | ready 345, repaired 37 (9 rows also carry the tag `authored_revision:reworded`) |
| passage sets | the Geography case set `geo-b3-settlement-set-1` (group `pg_ae0718e18ae74fd3aa519865ee34a569`, 4 children); `summary.topUpSets`: `english__p1__set3`, group `pg_b1c0212d23fa9117786356ede1fc95f7`, existing 3, added 1 |
| `warnings` | none (no set is below the NTA minimum of 4; online, none either: every planned subject has live rows, `gat` included) |
| `candidatesSha256` | `b0644cba44cd4de297c9ceeb562e757b92685fec60dab15870a4fed898071f4b` |
| `planHash` | `73b630705530e07588c6eef2ba9857927d8faed9cabf0d118da065af679207c4` (was `89e4b3c6...` before the subject id fix; only the subject of the 77 General Test rows differs) |
| `checks.questionColumnsMissing`, `passageGroupColumnsMissing` | 0, 0 |
| `checks.existingQuestionIds`, `existingGroupIds` | 0, 0 (any other number is a blocker) |
| `checks.topUpGroupsMissing` | 0 (online only; a missing wave-1 group is a blocker: wave 1 is not published in that target) |
| `checks.liveBefore` (online only) | keyed by the stored ids: biology, computer_science, english, **gat**, geography, mathematics, political_science. Every count is above 0; `gat` was the one that read 0 under `general_test`. |
| `checks.agentScores`, `checks.fitScores` | bound 382, missing 0, hashMismatch 0 |
| `checks.bankLookalikes` | exact 0, nearStem 0 (against the local 13 Oct export; informational; General Test rows are now compared with the export's `gat` rows, which they were not before) |
| `blockers` | `[]` |

A different `planHash` means the row mapping or the candidates changed since this runbook was written; read the plan before approving it. `candidatesSha256` is a sha of the file with line endings normalised.

## 5. Apply, restore

Only after the owner approves the dry-run file.

```
node --use-system-ca scripts/question-publish-authored.mjs --mode=apply --plan=docs/brain/reports/authored-publish/authored-publish-plan-<stamp>.json --reason="owner approved wave 2 publication <date>" --expect-project=isrxrxzjocewrdureyhp
node --use-system-ca scripts/question-publish-authored.mjs --mode=restore --restore=docs/brain/reports/authored-publish/authored-publish-restore-<stamp>.json --expect-project=isrxrxzjocewrdureyhp
```

Apply re-plans from the candidates file the dry run named (their sha256 and the plan hash must match), re-checks the columns and that the wave-1 group is in the target, **refuses if any planned question id or group id already exists** (insert only), refuses rows without score entries bound to their hash, writes `authored-publish-restore-<stamp>.json` before the first insert, inserts the 1 new group and then the 382 questions in chunks of 50, and reads everything back.

Expected: `inserted: 382`, `groupsInserted: 1`, `missing: []`, `notVisible: []`, `hashMismatch: []`, `groupsMissing: []`, and `liveAfter` equal to `liveBefore` plus 56, 76, 55, 77, 44, 65, 9 for biology, computer_science, english, gat, geography, mathematics, political_science (both keyed by the stored subject, General Test as `gat`).

Restore (default hide) works as in wave 1, with the source taken from the restore file (`claude-authored-2026-10-14-w2`). It never touches the wave-1 group the English top-up joined (that group is not in the restore file's `groupIds`; it is named in `topUpGroupIds`), and it touches only rows whose `source` is the wave-2 source, so wave 1 is unaffected. `--hard-delete` deletes rows still exactly as written and, of the groups, only the case-set group once no question points at it.

Then: deploy the code that carries the merged tables if it is not already deployed (until it is, the rows show in practice and not in NTA mode); the NTA pool is cached for 5 minutes. The rows are written as in wave 1 (`status live`, `verified`, `active`, `ai_tier PENDING`, `source claude-authored-2026-10-14-w2`, `provenance` and `evidence` NULL on purpose; wave 1's section 9 says why). They do not appear in Explore (that reads `question_scores`).

## 6. The 12 held questions: brought back (14 Oct 2026)

They were the expert-repaired questions whose stem or options changed after the blind solvers solved the old text: `234b88ee` `fdb74c4a` `b4a09c0e` (Biology, option lengths), `cb5101b5` `1aa2dc1c` (Computer Science, stem), `8ea3affd` (English, option C), `51db2fdf` `c2a88140` `d437d53e` (Geography, option lengths), `8e614805` (Mathematics, `sin(3x)`), `ee4e7379` `7ed82615` (Political Science, options). Their blind text, without key or explanation, is in `tmp/authored-w2/resolve/rv-w2-blind.json`.

Three fresh blind solvers wrote `rv-w2__s1.json`, `rv-w2__s2.json` and `rv-w2__s3.json`, and all three matched the key on all 12 (3 of 3). `node scripts/authored-w2-accept.mjs --mode=final` brought all 12 back (each entry carries `blind_resolve_on_final_text`). The duplicate screen, which keeps the first accepted copy, then dropped the two published questions that repeat held ones: `06298513` (since 2015, against `8ea3affd`) and `66c40b7a` (sin 3x / x continuity, against `8e614805`). That made 396; the 14 drops of the rechecks (section 0) took the final to 382.

The rule itself is still tested without the re-solve files: the raw-file tests of `authored_w2.test.mjs` run the final pass with an empty re-solve folder (the 12 are held again), then with a folder they build.

## 7. For the owner to decide or to know

1. **`87c9264b` (Mathematics, A³ of the matrix with rows (1, 2) and (0, 1)).** All five fresh solvers answered A; the key is D, (1, 6) and (0, 1), which is right by computation (A³ = (1, 6; 0, 1)), by the two quality judges and by the independent spot-check. Under the wave rule (4 of 5 on the key) it is out, and nothing was invented: the ledger records it as held (`held_key_correct_solvers_disagree`) with the reason, not as rejected. A hand check on 14 Oct redid the computation (A squared = (1, 4; 0, 1), A cubed = (1, 6; 0, 1), cross-checked as A times A squared; the distractors are a wrong result (A), 3A (B) and the cube-the-entry error 2 cubed = 8 (C)), so the key stands and the solvers' agreement on A stays unexplained. It stays out of NTA unless 4 of 5 fresh solvers agree on the key; the owner may still choose it for practice. The blind copy is `tmp/authored-w2/resolve/matrix-blind.json`.
2. **24 repaired questions are published without a new 3-solver re-solve**, on the original five solvers' result, because the repair touched only the explanation, the difficulty label or the NCERT reference. If the owner wants the wave-1 rule (a re-solve of every repaired question) applied here too, they are: `f3a654c3` `21b5b630` `845b0fb6` `f1e3b5d2` (Biology), `dd2c0a43` `af2c23fa` `cd8f0b68` (Computer Science), `5921f24b` `45e42f52` `b4463536` (English), `4791a3ed` `2b039f56` `337e86b5` `d4924246` `d7b0ee45` `93e3dc53` (General Test), `b3691bf1` `c48dd176` `8fa17c21` (Geography), `811b55a8` `303622fe` `1f21bc96` `12d9762a` (Mathematics), `d679ea00` (Political Science). `a3eb6b10` is repaired and reworded; it has the fresh five solvers on its final text.
3. **17 questions have only the single-reviewer supplementary review**, listed in `expert/supplement-2026-10-14.json`.
4. **Difficulty labels run high** (the spot-check): many "hard" items play as easy. It does not affect keys; it skews difficulty-balanced papers.
5. **Concepts repeat across batches** (HAVING in Computer Science, binary search, balance of trade, HDI): the duplicate screen catches near-identical stems, not the same concept. The Geography repeats of batch 3 were dropped; the others stay, so a paper may carry two items on one concept.
6. **Geography needs a second reviewer** for all 44 final items if the owner wants the NCERT re-check closed; this pass could not read NCERT. A second reviewer rechecked 13 Geography items on 14 Oct and all 13 were dropped as practice or reject (section 0); the other final items have not had a second Geography read.
7. Deploying this branch also deploys engine r5.2 for every subject (see the wave-1 runbook, section 5).

## 8. After publication

- Update `docs/brain/STATUS.md` with the dry-run counts, the apply read-back and the engine check.
- Select-only checks: `select subject, count(*) from questions where source = 'claude-authored-2026-10-14-w2' and not is_deleted group by 1;` (biology 56, computer_science 76, english 55, gat 77, geography 44, mathematics 65, political_science 9; no row may be under `general_test`), `select count(*) from passage_groups where source = 'claude-authored-2026-10-14-w2';` (1), `select count(*) from questions where passage_group_id = 'pg_b1c0212d23fa9117786356ede1fc95f7' and not is_deleted;` (4: three of wave 1 and one of wave 2).
