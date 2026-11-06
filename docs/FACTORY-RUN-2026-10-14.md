# Question factory run for short NTA subjects (14 Oct 2026)

**Result: not run. No paid call was made. The ledger is unchanged.**

The owner approved this run on 14 Oct (AI OS `decisions/log.md`, entry "Owner accepts all recommended pending MockMob decisions"): fill History, Political Science, Psychology, Sociology, Chemistry and the English passage sets, inside the USD 50 lifetime ledger and its guard. Before any spend I checked the factory against that request. It cannot do this work as it stands. Each item below names what is needed. None of it is an agent's call to make, because each one needs a code change in the dirty checkout, an owner decision the log still lists as open, or both.

## 1. Ledger (read 14 Oct 2026, read-only)

Source: `mockmob copy/data/pipeline-budget.sqlite`, the only persistent ledger on this PC. I opened it with a read-only SQLite connection, not through `BudgetLedger`, because its constructor writes.

| Item | USD |
|---|---:|
| Lifetime ceiling | 50.000000 |
| Settled (14,993 requests) | 39.139769 |
| Uncertain historical holds (65 unresolved, all bounded) | 0.821324 |
| **Committed** | **39.961093** |
| **Remaining** | **10.038907** |

Unbounded unresolved: 0, so the guard would allow a reservation. The last request is dated 10 Oct 05:58 UTC (V717). These figures match STATUS (10 Oct) and the owner's figure of about USD 39 spent. No factory worker is running. I checked the node processes.

## 2. Why the factory cannot run this request

1. **No qualified generator. This is an open owner decision.** V716 failed its qualification and V717 stopped unqualified (decision log, 10 Oct). The log also says "Qualification, pilot, release record and staging remain blocked until the owner decides the threshold/policy." It also says any continuation needs an additive next-version contract (V718) that separates author claims, option checks and reviewer observations, with the inventory and release seams closed, before any new qualification. The 14 Oct approval allows spending inside the ledger. It does not settle that policy. The V717 generation runner enforces this in code: `qualifiedPilotV717.mjs` throws `v717_pilot_requires_passed_current_qualification`. No V718 exists in any checkout.
2. **The factory only covers four subjects.** `FACTORY_SUBJECTS = ['english','accountancy','business_studies','economics']` in `data/question_factory_policy.mjs`, in both the dirty checkout and the committed one. Everything below is limited to those same four subjects:
   - the 8 registered source packs;
   - the authenticated PYQ exemplars (Accountancy 45, Business Studies 48, Economics 50, English 30);
   - the exam specs;
   - the released calibration (`luna-gemini-cuET-v6.2`, by_subject has the same four);
   - the V717 per-subject qualification floors.

   History, Political Science, Psychology, Sociology and Chemistry have none of these. Only their syllabus PDFs exist (`data/CUET 2026/<subject>.pdf`), and the catalog marks them `pending_extraction`. The factory's mandatory `source_support` gate needs registered, hash-checked source excerpts, so it would quarantine everything for these subjects. NTA-DATA-AUDIT reached the same conclusion on 13 Oct.
3. **No 200 to 300 word English passages exist to build on.** The factory consumes registered passage stimuli. It has no stage that authors a new passage. The registry holds 24 original passages of 92 to 132 words and one CUET 2024 passage of 335 words. That passage is over the 300-word limit and is an authentic paper passage whose reuse is not cleared.
4. **Prices expired.** `data/pipeline-prices.json` expired on 2026-10-12 21:37 UTC (verified 6 Oct). `budgetedFetch` and `factoryTransport` refuse every dispatch when prices have expired, and the V716/V717 sessions need at least 10 minutes of validity left. Refreshing prices means re-verifying the provider pricing pages and editing that file. In `mockmob copy` the file is tracked and already modified (` M data/pipeline-prices.json`), so editing it would touch a tracked file in the dirty checkout.
5. **The live factory exists only in the dirty checkout.** The V716/V717 code (220 lib files, uncommitted) and the ledger are only in `mockmob copy`. The committed checkouts (mockmob-hotfix and the others) hold the 7 Oct factory: 48 lib files, the same four subjects, the same expired prices, and no ledger. Adding subjects, a passage-authoring stage or a planner for these targets would be a code change in one of the two. Neither is allowed without the owner.

Credentials are not a blocker. The OpenAI, Gemini, signing-key and Supabase variable names are present in `.env.local`. Values were not read.

## 3. Plan and cost estimate (for once the blockers are cleared)

The target is three distinct 50-question papers per subject, which is 150 qualifying questions each. Chapter shares follow `data/nta_blueprints` targets. I split each subject's gap in proportion to the blueprint weights. The live per-chapter eligible counts were not re-read, so a read-only count should come before a run, because the current pool is uneven (History paper 1 had 0 questions from Kinship and from Thinkers).

**Generation should follow the owner's definition of a 10** (NTA-CUET-FIT-RUBRIC section 1). Prefer these, in order:
- a past CUET question changed by under 10% and made equal or slightly harder;
- a CBSE board or NCERT exercise item;
- a predictable CBT staple;
- an item that tests one key aspect of its chapter.

Never aim for "very hard". The difficulty mix follows the blueprint: History, Political Science, Psychology and Sociology about 40% Easy, 45% Medium and 15% Hard; Chemistry and English 35% Easy, 50% Medium and 15% Hard. Medium comes first. The first route needs authenticated CUET PYQs for these subjects, and none are registered yet.

**Cost basis:** about USD 0.0206 per candidate, measured on the commerce subjects (STATUS line 2649). That is authoring about 0.0012, full validation about 0.0148, and one repair on about 30% of items, adding about 0.0046 per candidate. The assumed yield at the NTA bar is 60% (the 7 Oct factory published 662 of 900, and 85% of those reach a mean of 8 or more). Yield for the new subjects is **unmeasured**.

| Subject | Eligible now | Needed for 3 papers | Candidates at 60% | Estimated USD |
|---|---:|---:|---:|---:|
| History | 23 | 127 | 212 | 4.37 |
| Political Science | 30 | 120 | 200 | 4.12 |
| Psychology | 36 | 114 | 190 | 3.91 |
| Sociology | 53 | 97 | 162 | 3.34 |
| Chemistry | 57 | 93 | 155 | 3.19 |
| English passage sets | 0 sets | 6 sets of 5 (30 items) | 12 sets (60 items) | 1.24 + passage authoring |
| **Total** | | **581** | **979** | **about 20.2** |

Chapter split of the "needed" column (3 × blueprint target in brackets):
- **History:** Bricks 10 (12), Kings 10 (12), Kinship 8 (9), Thinkers 10 (12), Travellers 13 (15), Bhakti-Sufi 10 (12), Vijayanagara 10 (12), Peasants 10 (12), Colonialism 10 (12), Rebels 10 (12), Gandhi 16 (18), Constitution 10 (12).
- **Political Science:** 7 to 8 for each of the 9 "Politics in India" chapters (9 each); End of Bipolarity, Alternative Centres and South Asia 10 each (12); International Organisations, Security and Environment 7 each (9); Globalisation 5 (6).
- **Psychology:** Variations 16 (21), Self 18 (24), Life Challenges 11 (15), Disorders 21 (27), Therapies 16 (21), Attitude 16 (21), Social Influence 16 (21).
- **Sociology:** Introducing 2 (3), Demographic 10 (15), Institutions 11 (18), Inequality 11 (18), Diversity 9 (15), Structural 6 (9), Cultural 8 (12), Democracy 6 (9), Rural 8 (12), Industrial 6 (9), Market 6 (9), Globalisation 6 (9), Mass Media 4 (6), Social Movements 4 (6).
- **Chemistry:** 9 to 10 for each of the 10 units (15 each).

**Type mix per paper (blueprint):**
- History, Political Science and Sociology: about 30 single MCQ, 4 match, 2 sequence, 4 statement, plus 2 source-based sets of 5.
- Psychology: 26 single, 5 match, 4 sequence, 5 statement, plus 2 case vignettes.
- Chemistry: 25 single, 5 match, 5 sequence, 5 statement, plus 2 concept-passage sets.

The current pool has 0 match and 0 sequence items at the bar for History.

**English also lacks verbal ability items, not just passages.** Each paper needs 40 verbal ability items. The 47 eligible today cover about one paper, so three papers need about 73 more (about 122 candidates, about USD 2.5). That would bring the full ask to about USD 22.7.

**What fits:** the full request (about USD 20 to 23) is about twice the USD 10.04 remaining. After the one-time setup work, the remaining budget buys about 360 to 410 candidates, or about 215 to 250 qualifying questions. That is roughly one more complete paper per subject, not three. The setup work is source packs, qualification for the new subjects (V716/V717 studies cost USD 0.06 to 0.26 actual) and a 40-candidate pilot (USD 3 cap, about USD 0.8 expected). Each candidate reserves up to USD 0.361 while it is in flight, so concurrency must stay low enough for the reservations to fit the remaining budget.

## 4. What needs the owner

In order:

1. **Qualification policy.** Decide the threshold/policy the 10 Oct log left open. Either authorize an additive V718 contract plus one fresh qualification, or authorize generation from an unqualified profile as quarantine-only output. That second option would be a new exception the record does not grant today.
2. **Subject expansion.** Authorize the code change to add the five subjects: subject lists, exam specs, calibration fixtures and per-subject floors. Say in which checkout: a clean branch from mockmob-hotfix, not the dirty `mockmob copy`. Also authorize registering source packs for these subjects:
   - NCERT text excerpts;
   - authenticated CUET 2022 to 2025 PYQs;
   - CBSE board items, with a permission basis.

   Without authenticated PYQs, the owner's first route to a 10 (a PYQ changed by under 10%) is not possible.
3. **English passages.** Authorize a passage-authoring stage, or a source of cleared 200 to 300 word passages (factual, narrative and literary), plus a planner that targets passage sets.
4. **Price refresh.** Approve re-verifying provider prices and updating `data/pipeline-prices.json` in the checkout the run will use.
5. **Budget scope.** Choose between about one more paper per subject within the USD 10.04 remaining, or a priority order (for example History and Political Science first). Raising the ceiling is the owner's call alone.
6. **Publication** stays a separate approval. Nothing here publishes. Separately, the factory evidence on the 662 scored live questions expires on 5 to 6 Nov 2026 (PENDING-2026-10-14 item 13).

## 5. What was not touched

No paid call, ledger write, price edit or code change. No file was edited in `mockmob copy`. No stash, reset or commit anywhere. No production or staging read or write. The only file written is this document, uncommitted.
