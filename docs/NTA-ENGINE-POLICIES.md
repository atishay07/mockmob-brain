# NTA engine policies after the expert review of 13 Oct 2026

The expert read whole NTA papers built by engine r3 and found nine defects. This file records how the
engine (data/nta_engine.js, data/nta_item_checks.js, data/nta_agent_scores.js, data/option_text.js,
scripts/nta-pass-merge.mjs) now handles each one, and what still needs the owner. Tests: the "finding N"
tests in data/tests/nta_review_fixes.test.mjs, the merge test in data/tests/nta_agent_scores.test.mjs and
data/tests/option_text.test.mjs.

## 1. Answer positions: options are shuffled per session

The bank stores most keys at A (79% of Mathematics, 71% of Physics and General Test). Every served row now
has its options in an order seeded by the session's key (the generation key, which also fixes the session
id) and the question id, so a resume, a replay and the review show the same order (ntaServedRow).

- The key is remapped: `correct_index` and `correct_answer` name the served position; the options are
  relabelled A-D in served order; `nta_option_order[i]` is the stored option shown at position i, and
  `nta_options_shuffled` says whether anything moved. The session stores these (src/lib/server/ntaPaper.js
  ntaOptionLayout) and refuses a paper whose key was not remapped.
- A letter stored in front of every option ("A  7/2", "B. Planning", "A 36") is removed first
  (data/option_text.js; a single space counts only when no option then reads as a reference such as "A and B").
- Explicit option references in the explanation ("option C", "options B and D", "the answer is (A)",
  "A is correct") are rewritten to the served letters in one pass.
- Options keep their stored order when they name other options ("All of the above", "Both A and B",
  "option 2"), are error-spotting part labels ("(A)", "(B)", "No error"), the stem names an option, or the
  explanation says "(C) is correct" about a statement the stem labels (C). Statement combinations
  ("(A) and (C) only", "I and III only") refer to the stem's statements and do move.

## 2. Blocking flags veto every source

A blocking flag (rubric section 3) from either agent judge keeps the question out whatever its score
source, factory evidence included (reason `agent_blocking_flag`). Factory evidence still decides the score;
it never overrules a judge who found a wrong fact, an answer in the stem or a broken layout.

## 3. Seed and demo rows

Only UUID ids are served (factory ids are the same 128 bits without hyphens). The 15 old seed rows
(a1-a3, b1-b3, e1-e3, g1-g3, m1-m3, source "PYQ 20xx") fail `id_not_uuid`; rows whose source, provenance
kind or tags say seed, demo, dummy, placeholder or fixture fail `seed_or_demo_row`.

## 4. Corrupted connectives

A text pass replaced "only" with "mainly". The wording gate (`wording_corrupted_connective`) catches the
forms that read wrongly in a stated condition: "I and III mainly", "Statement II mainly", "if and mainly if",
"the mainly ...", "mainly one/two/once", "mainly if", "mainly when", "mainly partially", "not mainly ... but
also", and "mainly" closing a clause. Ordinary use ("Acid rain is mainly caused by ...") passes. On the
13 Oct export it catches all 34 rows of the owner-approved hold plus 12 more; the ids for the clean-up are
in tmp/nta-review-cleanup/CLEANUP-2026-10-13.md (owner approval needed before any database change).

## 5. Chapters

Not changed by these fixes. Since engine r5 (the CUET-fit merge, section 10) the fit judges' majority chapter
and unit place a row before the database chapter (data/nta_engine.js placementOf); passage children keep the
database chapter while it maps to the paper, so one passage stays in one set.

## 6. One concept per paper, without matching tags

Two questions cannot share a paper when (in addition to the earlier same-stem, same-text, same-figures,
same-concept-name and headword rules):

- their stems are near-identical in wording: character 5-grams of the stem without instructions, each
  weighted by how rare it is in the pool, Jaccard 0.45 or more (`near_duplicate_stem_chars`; stems under 60
  characters and English vocabulary templates are left to the other rules);
- they have the same short correct answer, such as "Directing" (`same_key_answer`);
- either judge's objective tag shares a key concept phrase with either judge's tag of the other question:
  an order-free word pair of the tag's concept part ("law lenz", "meaning directing", "point percentage")
  that at most 5% of the subject's judged questions carry (`same_concept_words`). Single words are not used:
  even rare ones span several concepts, and with them most subjects could no longer fill a paper.

The stored objective tag (one per paper, or its cap) is the tag both judges gave alike; a tag only one judge
gave is no longer stored (scripts/nta-pass-merge.mjs), and both judges' tags stay in the score tables.

## 7. Difficulty: the stored label stands

The judges were told "when unsure between two levels, choose the lower", so their one-level disagreements
pushed 612 hard questions to medium and left almost nothing hard. Policy: the stored difficulty label is
used unless both judges agreed on one level AND that level is two levels from the label (easy labelled hard,
or the reverse). The merge writes only those corrections (80 after the re-judge, policy
`two_level_gap_only`; 1,267 one-level disagreements counted, not applied) and the engine applies nothing
else (data/nta_item_checks.js ntaDifficultyOf).

## 8. Listed-order keys

An arrange-in-sequence key that is the listed order ((A), (B), (C), (D)) and a match key that pairs the lists
in listed order ((A)-(I), (B)-(II), ...) give the answer away: `sequence_key_is_listed_order`,
`match_key_is_listed_order`. 63 live rows on the 13 Oct export (24 sequence, 39 match), listed for the
clean-up.

## 9. A student's next paper

`previousPaperIds` (data/nta_pool.js loadPreviousNtaPaperIds: submitted NTA attempts and NTA sessions kept on
the server) are left out of the pool whenever the rest still serves a paper. When it cannot, the paper is
built from the whole pool with them treated as seen (used only where nothing new fits) and
`structure.crossPaper` records `pool_too_small_without_previous_papers`, the paper that would have been
possible without them, and how many questions repeat. scripts/nta-engine-run.mjs builds papers 2 and 3 this
way and reports the repeats and the key positions.

A refusal is worked out once more with a fixed seed, so a student who retries reads the same sentence.

Repeats never refuse a paper (engine r5.1, 14 Oct). Seen questions (the student's practice answers, and earlier
papers in the fallback above) are first held back to fill only what new ones cannot ('seen_first'). Holding
them back can itself leave the paper short: on the 13 Oct export a second paper went from 46 to 44 for General
Test and from 45 to 44 for Economics, both refused. When the seen-first build is refused for too few questions
or passages, the paper is built again with repeats allowed, with every gate, quota and structure check
unchanged: first 'relaxed' (a seen question gives way only to an equally useful new one), then 'none' (built
as if nothing had been seen). The notice names the repeats ("N questions repeat from your earlier NTA papers:
there are not enough new questions that fit the pattern."); `structure.repeatFallback` records each build and
`crossPaper.repeatsAllowed` says a repeat-allowed build was used. Unsubmitted NTA sessions still count as
earlier papers: their whole paper was on screen, and the finaliser turns them into attempts after the deadline
and grace anyway.

When no question at all can be placed (`no_scored_questions`), the sentence names the gate that kept out the
most questions (`refusal.cause`): `quality` (no trusted score of 8 or more), `fit_not_judged` or `fit_below_bar`
(the CUET-fit judges), `veto` (key disputes, holds, blocking flags, answer, wording and format checks),
`syllabus` (questions pass every gate but sit in chapters the paper does not ask) or `unscored` (nothing carries
a score). `shortfall.excludedRows` counts rows per gate. A refused paper's notice items list only what the bank
is short of (types, units, chapters, numericals), never positions or layout of a paper nobody sees. The website
reads `detail.retryable` (false for the three bank refusals) and offers a Full Mock instead of "Try again".

## 10. CUET fit (engine r5, merged from wip/cuet-fit on 14 Oct)

Eligibility needs the quality gate above AND the CUET-fit gate (data/nta_fit_scores.js, rubric
docs/brain/NTA-CUET-FIT-RUBRIC.md): three fit judges scored the row's current content, fewer than two raised a
fit flag, and their median fit score is at least `NTA_MIN_FIT_SCORE` (8). Anything missing fails closed
(`fit_not_judged`, `fit_question_changed`, ...). The judges' majority type is the row's type before the
engine's heuristic (`classifyNtaType`; `heuristicNtaType` is the heuristic alone), and a type the subject's
paper never asks is refused (`fit_type_not_in_pattern`). Among eligible rows the newest (by creation day) is
preferred, then the higher score, then the higher fit median (owner, 13 Oct: "always pick the latest
questions"). Any text change, such as a listed-order reorder, unbinds the fit entry as it unbinds the agent
score: the row needs a fresh fit pass.
