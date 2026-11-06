# R6: Must-know on Key cards (measured 31 Oct 2026)

**Definition today:** an author judgement, not evidence. The content spec says "must" = definitions, boxed or highlighted text, headed lists, summary points, anything a past CUET paper asked; "good" = the rest; aim for about 60%. Nothing enforces it. Reviewers only checked "importanceRight".

**Measured:** 5,800 cards in 73 chapters; 3,916 Must-know = 68% (per chapter: min 46%, median 69%, max 100%). By subject: accountancy 618/868 (71%), biology 916/1394 (66%), business studies 629/900 (70%), economics 832/1193 (70%), English 193/349 (55%), political science 728/1096 (66%). By kind: definitions 93% must, lists 90, types 91, steps 97, formulas 85, differences 87, entries 83, examples 9. The inflation is in facts (2,435 cards, 56% must) and key lines (784, 55%).

**Signals:** `asked` is 0 on every card; pyq_anchors holds 77 manual seeds, no real past papers; no NCERT emphasis field (only free-text source.section: Summary 106/118 must, Recap 24/28). The only exam signal is the question links: 2,144 questions to 1,210 cards (21%); 788 cards have 1 link, 422 have 2 or more. 262 linked cards are "good" while 76% of must cards have no link. Links are thin for political science (13% of cards) and biology (18%).

**Candidate rules** (score = 3 x min(links, 3) + kind weight (definition/formula 4, steps/difference/list 3, types/entry 2, key line/fact 1, example 0) + 1 for Summary/Recap sections):
- R1: core kind (definition/formula/steps) or linked, capped 40%, floor 5: 1,752 (30%).
- R2: top 25% of each chapter by score, min 6, max 40: 1,427 (25%); median chapter 18; about 4.5 minutes to read a chapter's core.
- R3 strict: 2+ links, or 1 link on definition/formula/steps/list/types/difference/entry, cap 30%, floor 6: 803 (14%; only 9% in biology and political science).

**Behaviour tied to the flag:** the tag (KeyCard.jsx:173), Last look (Must-know only), the print sheet (Must-know only), the Free taste (first 5 Must-know cards per chapter, so every chapter needs at least 5), Pro "Add chapter to Revise", due ordering, chapter state. App: key_card_parts.dart:90, keycards_rules.dart, keycards_copy.dart.

**Changing decks:** importance is inside cardHash (scripts/keycards/lib.mjs:35), so editing it quarantines cards as review:stale, and the deck sha256 must match manifest.json or the subject switches off in production. Cheapest safe route: a tier overlay file applied in loadDecks (no deck, hash or verdict change).

## Per-chapter tables
### accountancy (868 cards, 14 chapters)

| Chapter | Cards | Must now | Share | Linked cards | def | formula | list/types/steps/diff | fact | key_line/term | entry | example | R1 | R2 | R3 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Accounting Ratios | 164 | 113 | 69% | 22 | 41 | 37 | 16 | 46 | 10 | 3 | 11 | 66 (40%) | 40 (24%) | 20 (12%) |
| Admission of Partner | 53 | 41 | 77% | 16 | 3 | 2 | 5 | 13 | 14 | 16 | 0 | 16 (30%) | 13 (25%) | 16 (30%) |
| Analysis of Financial Statements | 16 | 11 | 69% | 1 | 4 | 0 | 8 | 3 | 1 | 0 | 0 | 5 (31%) | 6 (38%) | 6 (38%) |
| Cash Flow Statement | 81 | 50 | 62% | 24 | 13 | 1 | 14 | 27 | 18 | 3 | 5 | 32 (40%) | 20 (25%) | 16 (20%) |
| Change in Profit Sharing Ratio | 8 | 8 | 100% | 4 | 2 | 1 | 1 | 2 | 1 | 1 | 0 | 5 (63%) | 6 (75%) | 6 (75%) |
| Comparative & Common Size Statements | 18 | 15 | 83% | 13 | 4 | 1 | 3 | 8 | 2 | 0 | 0 | 7 (39%) | 6 (33%) | 6 (33%) |
| Debentures | 86 | 67 | 78% | 19 | 24 | 0 | 12 | 16 | 16 | 17 | 1 | 34 (40%) | 22 (26%) | 18 (21%) |
| Dissolution of Partnership Firm | 59 | 49 | 83% | 17 | 3 | 1 | 9 | 18 | 4 | 23 | 1 | 20 (34%) | 15 (25%) | 13 (22%) |
| Financial Statements of Company | 85 | 54 | 64% | 2 | 11 | 3 | 19 | 19 | 33 | 0 | 0 | 16 (19%) | 21 (25%) | 6 (7%) |
| Goodwill Valuation | 39 | 26 | 67% | 11 | 6 | 8 | 5 | 6 | 9 | 0 | 5 | 16 (41%) | 10 (26%) | 11 (28%) |
| Partnership Fundamentals | 46 | 33 | 72% | 9 | 5 | 0 | 10 | 21 | 10 | 0 | 0 | 12 (26%) | 12 (26%) | 6 (13%) |
| Profit & Loss Appropriation Account | 42 | 34 | 81% | 17 | 4 | 1 | 4 | 21 | 2 | 10 | 0 | 17 (40%) | 11 (26%) | 13 (31%) |
| Retirement & Death of Partner | 65 | 49 | 75% | 10 | 3 | 2 | 6 | 25 | 2 | 26 | 1 | 14 (22%) | 16 (25%) | 10 (15%) |
| Share Capital | 106 | 68 | 64% | 33 | 26 | 2 | 13 | 27 | 17 | 19 | 2 | 42 (40%) | 27 (25%) | 25 (24%) |
| **Subject total** | **868** | **618** | **71%** | 198 | | | | | | | | **302 (35%)** | **225 (26%)** | **172 (20%)** |

### biology (1394 cards, 13 chapters)

| Chapter | Cards | Must now | Share | Linked cards | def | formula | list/types/steps/diff | fact | key_line/term | entry | example | R1 | R2 | R3 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Biodiversity & Conservation | 71 | 43 | 61% | 14 | 13 | 1 | 9 | 45 | 3 | 0 | 0 | 23 (32%) | 18 (25%) | 12 (17%) |
| Biotechnology & its Applications | 70 | 58 | 83% | 14 | 11 | 0 | 7 | 43 | 9 | 0 | 0 | 23 (33%) | 18 (26%) | 6 (9%) |
| Biotechnology Principles & Processes | 81 | 48 | 59% | 17 | 15 | 0 | 11 | 50 | 5 | 0 | 0 | 30 (37%) | 20 (25%) | 10 (12%) |
| Ecosystem | 72 | 55 | 76% | 13 | 19 | 1 | 10 | 32 | 10 | 0 | 0 | 29 (40%) | 18 (25%) | 6 (8%) |
| Evolution | 120 | 86 | 72% | 15 | 12 | 1 | 9 | 92 | 6 | 0 | 0 | 23 (19%) | 30 (25%) | 10 (8%) |
| Human Health & Disease | 173 | 104 | 60% | 20 | 25 | 0 | 28 | 105 | 15 | 0 | 0 | 43 (25%) | 40 (23%) | 6 (3%) |
| Human Reproduction | 123 | 56 | 46% | 16 | 19 | 0 | 11 | 56 | 37 | 0 | 0 | 34 (28%) | 31 (25%) | 6 (5%) |
| Microbes in Human Welfare | 67 | 41 | 61% | 20 | 9 | 0 | 6 | 44 | 8 | 0 | 0 | 27 (40%) | 17 (25%) | 9 (13%) |
| Molecular Basis of Inheritance | 192 | 126 | 66% | 27 | 12 | 0 | 17 | 108 | 55 | 0 | 0 | 39 (20%) | 40 (21%) | 7 (4%) |
| Organisms & Populations | 86 | 54 | 63% | 19 | 24 | 4 | 9 | 41 | 8 | 0 | 0 | 34 (40%) | 22 (26%) | 11 (13%) |
| Principles of Inheritance & Variation | 114 | 72 | 63% | 28 | 32 | 2 | 7 | 63 | 10 | 0 | 0 | 46 (40%) | 29 (25%) | 13 (11%) |
| Reproductive Health | 76 | 60 | 79% | 13 | 17 | 0 | 7 | 47 | 5 | 0 | 0 | 25 (33%) | 19 (25%) | 7 (9%) |
| Sexual Reproduction in Flowering Plants | 149 | 113 | 76% | 41 | 28 | 0 | 17 | 67 | 37 | 0 | 0 | 55 (37%) | 37 (25%) | 26 (17%) |
| **Subject total** | **1394** | **916** | **66%** | 257 | | | | | | | | **431 (31%)** | **339 (24%)** | **129 (9%)** |

### business_studies (900 cards, 11 chapters)

| Chapter | Cards | Must now | Share | Linked cards | def | formula | list/types/steps/diff | fact | key_line/term | entry | example | R1 | R2 | R3 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Business Environment | 38 | 29 | 76% | 7 | 6 | 0 | 6 | 4 | 17 | 0 | 5 | 9 (24%) | 10 (26%) | 6 (16%) |
| Consumer Protection | 60 | 46 | 77% | 22 | 22 | 0 | 10 | 13 | 15 | 0 | 0 | 24 (40%) | 15 (25%) | 18 (30%) |
| Controlling | 48 | 34 | 71% | 22 | 5 | 0 | 9 | 14 | 18 | 0 | 2 | 19 (40%) | 12 (25%) | 12 (25%) |
| Directing | 112 | 67 | 60% | 12 | 28 | 0 | 30 | 9 | 39 | 0 | 6 | 35 (31%) | 28 (25%) | 11 (10%) |
| Financial Management | 127 | 82 | 65% | 23 | 23 | 4 | 20 | 10 | 69 | 0 | 1 | 45 (35%) | 32 (25%) | 11 (9%) |
| Marketing Management | 134 | 93 | 69% | 10 | 55 | 0 | 40 | 26 | 11 | 0 | 2 | 54 (40%) | 34 (25%) | 6 (4%) |
| Nature & Significance of Management | 67 | 45 | 67% | 29 | 24 | 0 | 14 | 13 | 10 | 0 | 6 | 27 (40%) | 17 (25%) | 20 (30%) |
| Organising | 69 | 60 | 87% | 22 | 22 | 0 | 26 | 11 | 10 | 0 | 0 | 28 (41%) | 17 (25%) | 19 (28%) |
| Planning | 51 | 37 | 73% | 17 | 17 | 1 | 11 | 7 | 12 | 0 | 3 | 20 (39%) | 13 (25%) | 12 (24%) |
| Principles of Management | 96 | 71 | 74% | 26 | 24 | 0 | 27 | 22 | 23 | 0 | 0 | 38 (40%) | 24 (25%) | 22 (23%) |
| Staffing | 98 | 65 | 66% | 30 | 33 | 0 | 32 | 9 | 24 | 0 | 0 | 39 (40%) | 25 (26%) | 24 (24%) |
| **Subject total** | **900** | **629** | **70%** | 220 | | | | | | | | **338 (38%)** | **227 (25%)** | **161 (18%)** |

### economics (1193 cards, 17 chapters)

| Chapter | Cards | Must now | Share | Linked cards | def | formula | list/types/steps/diff | fact | key_line/term | entry | example | R1 | R2 | R3 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Balance of Payments | 76 | 49 | 64% | 28 | 26 | 1 | 15 | 19 | 13 | 0 | 2 | 30 (39%) | 19 (25%) | 17 (22%) |
| Development Experiences of India | 83 | 49 | 59% | 12 | 6 | 0 | 17 | 32 | 28 | 0 | 0 | 18 (22%) | 21 (25%) | 6 (7%) |
| Economic Reforms Since 1991 | 89 | 54 | 61% | 13 | 11 | 0 | 15 | 45 | 14 | 0 | 4 | 20 (22%) | 22 (25%) | 8 (9%) |
| Employment | 58 | 45 | 78% | 16 | 13 | 1 | 5 | 26 | 12 | 0 | 1 | 20 (34%) | 15 (26%) | 11 (19%) |
| Environment & Sustainable Development | 59 | 35 | 59% | 10 | 9 | 0 | 11 | 30 | 9 | 0 | 0 | 17 (29%) | 15 (25%) | 6 (10%) |
| Government Budget & the Economy | 64 | 49 | 77% | 27 | 22 | 5 | 15 | 13 | 9 | 0 | 0 | 26 (41%) | 16 (25%) | 19 (30%) |
| Human Capital Formation | 51 | 30 | 59% | 14 | 3 | 0 | 18 | 15 | 14 | 0 | 1 | 14 (27%) | 13 (25%) | 6 (12%) |
| Income Determination | 78 | 51 | 65% | 17 | 25 | 7 | 5 | 15 | 21 | 0 | 5 | 31 (40%) | 20 (26%) | 8 (10%) |
| Indian Economic Development 1950–1990 | 92 | 59 | 64% | 20 | 14 | 0 | 14 | 37 | 27 | 0 | 0 | 28 (30%) | 23 (25%) | 10 (11%) |
| Indian Economy on the Eve of Independence | 50 | 39 | 78% | 23 | 4 | 0 | 8 | 21 | 17 | 0 | 0 | 20 (40%) | 13 (26%) | 11 (22%) |
| Introduction & Theory of Consumer Behaviour | 116 | 91 | 78% | 26 | 34 | 7 | 8 | 38 | 25 | 0 | 4 | 46 (40%) | 29 (25%) | 17 (15%) |
| Market Equilibrium & Simple Applications | 24 | 19 | 79% | 11 | 4 | 1 | 1 | 10 | 8 | 0 | 0 | 10 (42%) | 6 (25%) | 7 (29%) |
| Money & Banking | 70 | 55 | 79% | 23 | 23 | 6 | 7 | 27 | 6 | 0 | 1 | 28 (40%) | 18 (26%) | 13 (19%) |
| National Income & Related Aggregates | 90 | 64 | 71% | 18 | 30 | 27 | 8 | 15 | 7 | 0 | 3 | 36 (40%) | 23 (26%) | 14 (16%) |
| Production & Costs | 79 | 66 | 84% | 27 | 27 | 12 | 0 | 12 | 27 | 0 | 1 | 32 (41%) | 20 (25%) | 21 (27%) |
| Rural Development | 48 | 27 | 56% | 9 | 4 | 0 | 22 | 14 | 8 | 0 | 0 | 13 (27%) | 12 (25%) | 6 (13%) |
| Theory of Firms under Perfect Competition | 66 | 50 | 76% | 24 | 13 | 5 | 8 | 23 | 10 | 0 | 7 | 26 (39%) | 17 (26%) | 19 (29%) |
| **Subject total** | **1193** | **832** | **70%** | 318 | | | | | | | | **415 (35%)** | **302 (25%)** | **199 (17%)** |

### english (349 cards, 2 chapters)

| Chapter | Cards | Must now | Share | Linked cards | def | formula | list/types/steps/diff | fact | key_line/term | entry | example | R1 | R2 | R3 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Correct Word Usage | 66 | 39 | 59% | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 (12%) | 17 (26%) | 6 (9%) |
| Vocabulary | 283 | 154 | 54% | 68 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 68 (24%) | 40 (14%) | 37 (13%) |
| **Subject total** | **349** | **193** | **55%** | 76 | | | | | | | | **76 (22%)** | **57 (16%)** | **43 (12%)** |

### political_science (1096 cards, 16 chapters)

| Chapter | Cards | Must now | Share | Linked cards | def | formula | list/types/steps/diff | fact | key_line/term | entry | example | R1 | R2 | R3 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Alternative Centres of Power | 85 | 48 | 56% | 6 | 1 | 0 | 7 | 68 | 9 | 0 | 0 | 6 (7%) | 21 (25%) | 6 (7%) |
| Challenges of Nation Building | 75 | 59 | 79% | 10 | 4 | 0 | 3 | 59 | 5 | 0 | 0 | 13 (17%) | 19 (25%) | 6 (8%) |
| Challenges to & Restoration of the Congress System | 78 | 61 | 78% | 12 | 5 | 0 | 8 | 61 | 4 | 0 | 0 | 15 (19%) | 20 (26%) | 6 (8%) |
| Contemporary South Asia | 70 | 38 | 54% | 9 | 2 | 0 | 4 | 60 | 4 | 0 | 0 | 11 (16%) | 18 (26%) | 6 (9%) |
| Crisis of the Democratic Order | 52 | 29 | 56% | 13 | 2 | 0 | 3 | 38 | 7 | 0 | 0 | 13 (25%) | 13 (25%) | 6 (12%) |
| Democratic Upsurge and Coalition Politics | 35 | 27 | 77% | 3 | 0 | 0 | 1 | 33 | 1 | 0 | 0 | 5 (14%) | 9 (26%) | 6 (17%) |
| End of Bipolarity | 90 | 67 | 74% | 10 | 3 | 0 | 9 | 72 | 6 | 0 | 0 | 12 (13%) | 23 (26%) | 6 (7%) |
| Environment & Natural Resources | 65 | 44 | 68% | 8 | 10 | 0 | 8 | 44 | 2 | 0 | 0 | 17 (26%) | 16 (25%) | 6 (9%) |
| Era of One-Party Dominance | 78 | 53 | 68% | 9 | 4 | 0 | 4 | 61 | 9 | 0 | 0 | 13 (17%) | 20 (26%) | 6 (8%) |
| Globalisation | 59 | 43 | 73% | 7 | 4 | 0 | 4 | 38 | 13 | 0 | 0 | 10 (17%) | 15 (25%) | 6 (10%) |
| India's External Relations | 70 | 44 | 63% | 13 | 2 | 0 | 5 | 56 | 7 | 0 | 0 | 15 (21%) | 18 (26%) | 6 (9%) |
| International Organisations | 81 | 54 | 67% | 13 | 5 | 0 | 8 | 62 | 5 | 0 | 0 | 17 (21%) | 20 (25%) | 9 (11%) |
| Politics of Planned Development | 36 | 25 | 69% | 7 | 4 | 0 | 2 | 28 | 2 | 0 | 0 | 10 (28%) | 9 (25%) | 6 (17%) |
| Recent Issues and Challenges | 46 | 32 | 70% | 5 | 3 | 0 | 0 | 40 | 3 | 0 | 0 | 8 (17%) | 12 (26%) | 6 (13%) |
| Regional Aspirations | 105 | 57 | 54% | 11 | 0 | 0 | 5 | 95 | 4 | 0 | 0 | 12 (11%) | 26 (25%) | 6 (6%) |
| Security in the Contemporary World | 71 | 47 | 66% | 5 | 11 | 0 | 10 | 45 | 5 | 0 | 0 | 13 (18%) | 18 (25%) | 6 (8%) |
| **Subject total** | **1096** | **728** | **66%** | 141 | | | | | | | | **190 (17%)** | **277 (25%)** | **99 (9%)** |

