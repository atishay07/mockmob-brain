# Wave 2 independent spot-check, 14 Oct 2026

**Who and how.** This is an independent check by a senior CUET UG examiner, written by an agent. I sampled 60 of the 390 accepted wave-2 questions (`accepted: true` in `wave2-acceptance-2026-10-14.json`). I read the current text of each one in `tmp/authored-w2/<subject>/<batch>.json`, which already includes any expert-pass repairs and the applied rewords. I solved each question myself before reading its key or the expert verdict. I edited no question files.

**Sampling.** I used Python `random.Random(20261014)` and sampled each subject from its accepted ids, sorted. The script is `scratchpad/sample.py`; its output, with the full text of every picked item, is `scratchpad/picked.json`. Neither file is in the repo. The split is proportional, with at least 5 per subject:

| Subject | Accepted | Sampled |
|---|---|---|
| Computer Science | 78 | 11 |
| General Test | 72 | 10 |
| Mathematics | 69 | 10 |
| Biology | 56 | 8 |
| English | 55 | 8 |
| Geography | 51 | 8 |
| Political Science | 9 | 5 (the 5 minimum, which is more than its proportional share) |

**Verdicts.**
- **NTA-ready:** fit to appear in a CUET-pattern paper as written.
- **Practice-grade:** the key is correct, but a syllabus-fit or wording issue means it should stay out of the NTA-pattern paper until it is fixed.
- **Reject:** the key is wrong or not unique, or the item is broken.

## Results

| # | Subject | Batch | Id | Type | My answer / key | Expert | Verdict | Reason |
|---|---|---|---|---|---|---|---|---|
| 1 | CS | b4 | e056011f-1958-4eda-8fe0-0f40fe290aea | single_mcq | B / B | ready | NTA-ready | LIKE 'R%' is the only prefix match. Clean distractors. |
| 2 | CS | b3 | 3860696b-f94c-42b9-a539-1b897716322e | single_mcq | C / C | ready | NTA-ready | The fixed-column table is the only structured-data option. |
| 3 | CS | b1 | 34abbb63-2fda-4850-a491-50ba1e837976 | single_mcq | C / C | ready | NTA-ready | DESCRIBE shows the column names and types. The other options are distinct commands. |
| 4 | CS | b1 | cb5101b5-3bdd-4d79-8337-30667d59a867 | single_mcq | A / A | repaired | NTA-ready | Both calls run `finally` (prints done twice) before print shows "-1 2". The new comma convention makes the options unambiguous. |
| 5 | CS | b4 | d1d56cc5-c272-4be5-9f63-4702d5983de0 | single_mcq | B / B | ready | NTA-ready | HAVING filters groups. Same concept as #9 (see patterns). |
| 6 | CS | b4 | 820e86a4-8e21-49cb-b70b-4c1c451f225b | single_mcq | C / C | ready | NTA-ready | Firewall definition. Labelled medium but plays as easy. |
| 7 | CS | b1 | 8cfc8e96-89de-4cc0-9ac4-707e27e37561 | single_mcq | C / C | ready | NTA-ready | Append mode gives HelloWorld. The stem rules out a newline. |
| 8 | CS | b2 | 6d13d4fd-4412-4469-b16b-409ef1b79ca0 | single_mcq | D / D | ready | NTA-ready | The queue ends as [9, 7], so the front is 9. Trace checked. |
| 9 | CS | b1 | d7ea058b-6475-4c93-b139-16a3f96c04ce | single_mcq | D / D | ready | NTA-ready | Correct WHERE-before / HAVING-after contrast. Overlaps #5. |
| 10 | CS | b2 | e8e00542-0cee-4b85-b5be-b0e3ba1a47c1 | single_mcq | B / B | ready | NTA-ready | floor(log2 100) + 1 = 7. The 6 off-by-one trap is fair. |
| 11 | CS | b1 | f9debc0f-c921-4e41-b0ab-1816fdd7b143 | single_mcq | B / B | ready | NTA-ready | SHOW TABLES after USE school lists that database's tables. |
| 12 | GT | b3 | f23ad1d3-882c-4dc2-8060-e13af4fe2b1a | single_mcq | D / D | ready | NTA-ready | Unique arrangement T Q R P S puts R in the middle. Labelled hard but is easy. |
| 13 | GT | b2 | cd7595ed-0ad7-4971-b751-620d04f3a27d | statement_based | A / A | ready | NTA-ready | Statements A, B and D are true. C is false (0.01). |
| 14 | GT | b1 | 72d7dce3-33a7-4592-be70-e2955f4b8477 | single_mcq | B / B | ready | NTA-ready | 800 x 0.85 = 680. |
| 15 | GT | b4 | ceb5b49c-70f4-4470-968b-469c49e4293f | single_mcq | D / D | ready | NTA-ready | Ravi is 19th from the left, so 22nd from the right. The 18 trap (wrong person) is good. |
| 16 | GT | b2 | f4cbe5ec-4495-460b-9751-9f9a1bf9403d | match_the_following | B / B | ready | NTA-ready | Fraction, decimal and percent pairs are all unique. Easy for medium. |
| 17 | GT | b1 | 62964f0b-dff3-4d75-bc39-9f1633f7c220 | match_the_following | C / C | ready | NTA-ready | Nehru, Tagore, Kalam, Premchand. Each distractor breaks at least one pair. |
| 18 | GT | b4 | 505a5821-7f27-45da-bb31-1edb9fa1ee24 | single_mcq | D / D | ready | NTA-ready | 334 days, 334 mod 7 = 5, Monday + 5 = Saturday. |
| 19 | GT | b2 | 0c58063b-c5ec-4c3d-a70d-40ffd57a09f1 | single_mcq | B / B | ready | NTA-ready | The mother is the husband's sister, so the speaker is the aunt. No alternative reading. |
| 20 | GT | b2 | d2d1e440-1447-4fc4-be52-6f03764331e4 | assertion_reason | D / D | ready | NTA-ready | R (the form 2k+1) is what proves A. This is the standard NTA reading. Labelled hard but is easy. |
| 21 | GT | b2 | 92d3d84e-a352-4dc2-9bfc-43619398b020 | single_mcq | C / C | ready | NTA-ready | Rule x2+2, and the doubling differences agree on 94. |
| 22 | Maths | b1 | a443b790-5883-4a86-97ff-a79fb504593d | match_the_following | A / A | ready | NTA-ready | All four antiderivatives checked. The pairing is unique. |
| 23 | Maths | b1 | e8e39a8f-434c-40c0-9e8f-2efec7c08d76 | single_mcq | B / B | ready | NTA-ready | Principal value π/4. 3π/4 is the out-of-range trap. |
| 24 | Maths | b2 | c692e563-f533-44b8-b390-dbbfc1fdaf18 | single_mcq | A / A | ready | NTA-ready | 8πr·dr/dt = 16π. |
| 25 | Maths | b1 | fb49ae9d-67bf-43c2-a22c-892e32b2e08d | single_mcq | D / D | ready | NTA-ready | Corners (0,0), (4,0), (3,1), (0,2) give a maximum of 13. |
| 26 | Maths | b1 | 87c9264b-613d-4c51-bb97-9de06bbe6fe8 | single_mcq | D / D | ready | NTA-ready | Reworded rows form is now in the file. A³ has rows (1,6), (0,1). Distractors are good. |
| 27 | Maths | b3 | ceb71d00-66ab-4ee7-9cad-74250d408a2f | statement_based | A / A | ready | NTA-ready | IF x², y = x³/5 + C/x², degree 1. A, B and D are true. |
| 28 | Maths | b3 | 8ee1a4be-30ab-4a3b-a98d-87294334ec60 | single_mcq | D / D | ready | NTA-ready | (e−1)/2. Now distinct from (e+1)/2 under the r5.2 option compare. |
| 29 | Maths | b2 | 2b6807ae-c16c-4267-b420-5722c0ed952d | single_mcq | C / C | ready | NTA-ready | The integrand is d/dx(eˣ/x). Option D is the integrand itself, a fair trap. |
| 30 | Maths | b2 | 12731fb4-c956-4aca-bb97-1a5ef2813c42 | single_mcq | A / A | ready | NTA-ready | tan(x/2) from 0 to π/2 = 1. |
| 31 | Maths | b3 | b0307bb2-96a1-4232-ae87-58d0742d49f2 | single_mcq | D / D | ready | NTA-ready | y'' = 4y. Unique. |
| 32 | Bio | b1 | 4b3919e1-b58b-44eb-a11c-42cca7d43ca7 | single_mcq | D / D | ready | NTA-ready | 20 = 12 + 8, so Q is in the middle. R–Q–P is the only option equivalent to P–Q–R. |
| 33 | Bio | b3 | 2886c110-f067-4b1c-b08d-c106f8bc63ab | match_the_following | B / B | ready | NTA-ready | Restriction enzyme, ligase, Taq, lysozyme roles all match NCERT. |
| 34 | Bio | b2 | 2148930a-60be-48b5-9e39-fec0472bdc02 | statement_based | B / B | ready | NTA-ready | 47,XXY and 45,XO are true. C and D are false. |
| 35 | Bio | b2 | 5b628f6b-b0f6-40ff-b175-dcea08d69b3f | single_mcq | D / D | ready | NTA-ready | The O child fixes IAi × IBi, so P(AB) = 1/4. |
| 36 | Bio | b1 | 1f51f8e3-79a9-4f4e-8fc2-a2359d0dd3f6 | sequence_ordering | D / D | ready | NTA-ready | Primordial, primary, secondary, Graafian. |
| 37 | Bio | b1 | 009cdde5-c914-475a-b773-c30818aa0ff8 | single_mcq | A / A | ready | NTA-ready | Grasshopper is XX–XO. NCERT example. |
| 38 | Bio | b1 | dbbeb54a-2a90-448d-bc03-d52a07078ded | match_the_following | D / D | ready | NTA-ready | The orphan-passage issue is gone (passage null in the current file). Contraceptive pairs are correct, including Saheli as once a week and non-steroidal. |
| 39 | Bio | b1 | 15342484-fa9f-4b7d-8caf-a7bb1d1ab98e | single_mcq | A / A | ready | NTA-ready | Tapetum nourishes the microspores. |
| 40 | Eng | v2 | 5c0c8364-d8a8-4b8e-9e93-a6a9406ead6a | sentence_rearrangement | A / A | ready | NTA-ready | B C A D is the only grammatical order. |
| 41 | Eng | v2 | 4891081e-8c50-4590-ba65-99b1892ab2be | fill_in_blank | A / A | ready | NTA-ready | "Rejected" is cued by "could not afford them". The distractors are weak but wrong. |
| 42 | Eng | v3 | 6277710e-49ef-44b3-8b99-c9b740be056f | antonym | C / C | ready | NTA-ready | Perpetual. The other three are synonyms. |
| 43 | Eng | v1 | 16986c98-200e-4c90-99d8-10ce90fb318f | match_the_following | C / C | ready | NTA-ready | All phrasal-verb pairs are standard and unique. |
| 44 | Eng | v2 | 6c570fed-0a98-484c-862e-addceb5286a0 | fill_in_blank | D / D | ready | NTA-ready | Present perfect backshifts to "had finished". |
| 45 | Eng | v2 | 5c265510-b0ba-4422-828f-8d95a00c6149 | synonym | C / C | ready | NTA-ready | Laconic means concise. |
| 46 | Eng | v1 | 1181c7a2-584e-49f2-a34f-0b83dbdbc068 | sentence_rearrangement | C / C | ready | NTA-ready | A C B D is unique. Very easy for its medium label. |
| 47 | Eng | v1 | 19453319-eb6d-49c8-b282-86d1e025724b | one_word_substitution | B / B | ready | NTA-ready | Polyglot. |
| 48 | Geo | b2 | 42295a2f-5388-48dd-8f5c-021b3fd9a57f | statement_based | D / D | ready | NTA-ready | A, B and D are true. Ranching is not nomadic. Matches NCERT Primary Activities. |
| 49 | Geo | b1 | f5ceaadd-0e02-4556-978e-5690c51b638b | sequence_ordering | D / D | ready | NTA-ready | Primary, secondary, tertiary, quaternary. Labelled hard but is easy. |
| 50 | Geo | b1 | f92f3699-2f61-4c22-a11e-cf947bc020c9 | single_mcq | A / A | ready | NTA-ready | 480/120 means arable land is a quarter of the area. Physiological density is in NCERT India: People and Economy, ch 1. |
| 51 | Geo | b1 | 694a21d0-314c-4fa4-a036-b52baef85d12 | statement_based | A / A | ready | NTA-ready | Shifting cultivation is subsistence farming. Minor: "(A), (B) and (C) only" is odd wording for all three. |
| 52 | Geo | b4 | 8c3a70dc-ec40-4a53-9c71-eec4dba19e09 | single_mcq | B / B | ready | NTA-ready | 62 − 79 = 17 deficit. "Merchandise" avoids the goods-or-services question. |
| 53 | Geo | b4 | 1445658c-c847-43d9-a6f3-474f23ee0894 | sequence_ordering | C / C | ready | **Practice-grade** | The dates are right (1987, 1992, 1997, 2015). Montreal, Kyoto and Paris dates are not in Class 12 Geography; this is Political Science or general-knowledge content. |
| 54 | Geo | b1 | fdbdd72a-aa89-4f36-b2ff-bd69aae539af | single_mcq | C / C | repaired | **Practice-grade** | 52.5 is correct and the stem gives everything needed. NCERT Geography does not teach the HDI index formula, so a computation item is off-pattern for CUET Geography. |
| 55 | Geo | b2 | 3fcbe4d0-8a61-48c8-9492-803679c7555d | single_mcq | B / B | ready | **Practice-grade** | B is still the best option. NCERT Class 12 Geography (International Trade) defines balance of trade as covering goods *and services*, but option B says "goods" only and the explanation states that services are excluded. A student taught from NCERT would see a conflict. Fix: make B "Value of exports minus value of imports" and remove the services sentence from the explanation. |
| 56 | PolSci | glob | 2785926b-24a5-40f2-8c49-f9cf4ecf6a67 | single_mcq | B / B | ready | NTA-ready | The NOT item is clear. The other three are recognised dimensions. |
| 57 | PolSci | glob | 7ed82615-4905-4767-a7e8-b4104ea206fd | single_mcq | A / A | repaired | NTA-ready | The 1991 balance of payments crisis is the trigger. The repaired distractors are plausible and false. |
| 58 | PolSci | glob | ee4e7379-b61d-481c-95b8-bbc665cc9bf9 | single_mcq | A / A | repaired | NTA-ready | Definition item. Option lengths are now balanced. |
| 59 | PolSci | glob | 673cda86-7ab4-40a6-8d5c-f38075d00c6c | statement_based | D / D | ready | NTA-ready | B and D are true. A and C are clearly false, so the key is unique even under the strict reading that the IMF dates from 1945. |
| 60 | PolSci | glob | 8eedfa08-6c44-41d8-9c93-794135a8aa52 | single_mcq | D / D | ready | NTA-ready | WTO 1995. Every distractor is a real, related year. |

## Summary

**Counts (60 sampled):**
- **NTA-ready:** 57 (95%).
- **Practice-grade:** 3 (5%), all Geography: #53, #54, #55.
- **Reject:** 0.

**Key check.** My own answer matched the stored key on all 60. Each key was the only correct option. I found no wrong key, no second correct option and no broken rendering. The expert-pass repairs I saw (#4, #54, #57, #58) are applied in the current files and are sound. The applied rewords (#26 matrix rows form, #32, #38) are also present and clean.

**Agreement with the expert pass.** I agree with the expert pass on 57 of 60. The 3 disagreements are all Geography, and in each one the expert marked "ready" (or "repaired") on key correctness alone, without checking syllabus fit against NCERT wording.

### Patterns

1. **Geography diverges from NCERT and the syllabus.**
   - **The definition:** wave 2 uses the economics definition of balance of trade (visible goods only). NCERT Class 12 Geography says it records "goods and services".
   - **Outside the sample:** `f6ef948f` keys statement (B), "balance of trade includes invisible items such as banking and insurance services", as false. Under NCERT Geography wording that statement is true, which leaves no correct option. Treat it as a probable reject. It also tests balance of payments and current-account content, which is Economics, not Geography.
   - **Off-syllabus content:** the HDI items include an arithmetic one (#54). #53 tests environmental-treaty dates.
2. **Difficulty labels run high.** Several items labelled hard are easy for a CUET candidate: #12, #20, #49, and arguably #19 and #21. Several labelled medium are easy: #6, #16, #46. Only 43 of 390 accepted items are labelled hard (11%), so the true hard share is lower still. This does not affect correctness, but it will skew any difficulty-balanced paper built from these labels.
3. **Concepts repeat across batches.** The duplicate screen catches near-identical stems but not the same concept:
   - WHERE versus HAVING: #5 and #9, plus 3 more HAVING table items. That is 5 HAVING items in CS.
   - Binary search worst case: 6 items.
   - Balance of trade: 3 Geography items plus #52.
   - HDI: 4 Geography items.

   A mock paper that draws randomly may put two of these together. Limit each concept to one per paper when assembling.
4. **Some distractors are weak.** In English vocabulary and fill-in-the-blank items (#41, #46), the wrong options are easy to eliminate. These are NTA-ready but sit at the easy end.

### Subjects needing a broader re-check

- **Geography: yes.** 3 of 8 sampled are practice-grade, and one more probable key conflict turned up outside the sample (`f6ef948f`). Before Geography goes into the NTA-pattern paper, re-check all 51 accepted Geography items against NCERT Class 12 wording. Look for three things:
  - balance of trade, balance of payments, and visible and invisible trade definitions;
  - HDI computation and banding items (`fdbdd72a`, `e32b79ff`, `ad34719d`, `8b40da05`);
  - dates of international events or treaties.
- **Political Science: no.** Only 9 items are accepted and the sample covered 5. All are clean, but the pool is too thin to fill a section on its own.
- **Computer Science, General Test, Mathematics, Biology, English: no.** I found no correctness or fit problem in the sample. The only actions are relabelling difficulty and limiting repeated concepts per paper.

**Limits.** This is a 60-item sample (15% of 390). With 0 rejects observed, the reject rate in the remaining 330 is probably low, but a few cannot be ruled out. Geography is the subject where problems concentrate.
