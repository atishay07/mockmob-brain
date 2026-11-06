# Verdicts: 29 flagged Accountancy questions

Counts: KEY_OK 1, KEY_WRONG 0, reworded 18, pending 10. (Verdicts below are my own reading of the full rows, from accounting principles; the NCERT PDFs were not needed because no question hinges on the debenture-discount point.)

| # | id (prefix) | Question | Key | Verdict | Evidence | Action |
|---|---|---|---|---|---|---|
| 1 | 4758fddf | Purchased goodwill, which items definitely change | A | FLAWED | If paid in cash, total assets are unchanged; audit right | Reword stem: "recorded on credit (payment still due)"; explanation updated. Key A holds |
| 2 | c2b4dbcb | Realised goodwill 36,000 vs "prior notional write-off" in CAS | A | FLAWED | Stem is incoherent (realised goodwill goes via Realisation A/c, no notional write-off to reverse) | pending |
| 3 | d9c47b1c | Reserve transferred to capitals | A | FLAWED | Transfer within equity changes no cash; "increase distributable cash" false | Reword option A to "no change in cash"; explanation updated. Key A holds |
| 4 | e36eecbb | Data processing cycle sequence | C | FLAWED | A (Entry, Processing, Storage, Output) and B are both standard; C omits output | pending |
| 5 | 02948971 | Forfeiture of 200 shares, effect on paid-up capital | A | FLAWED | Paid-up falls by the amount actually received, not nominal value; stem gives no called-up amount | pending |
| 6-16 | 04219368, 0b2f66a0, 1b09a38c, 248464f4, 72adc20a, 86a2aa10, bd6df01d, e4ea3760, f288d7f5, f9a72c4b (10) | Premium Rs4 vs allotment Rs3 "including premium" | A | FLAWED (generator bug) | Premium 4 > allotment 3 is impossible. Premium transferred = shares x 4 only if whole premium falls due on allotment | One consistent reword for all 10: "is ₹3 (including premium)" becomes "is ₹3 plus the entire premium". Key A, options and explanation stay correct |
| 10 | 63b4ad47 | Called-up vs paid-up, "final call pending" | B | FLAWED | 6 paid + 2 final call = 8, not 10; key B needs a made-but-unpaid first call | Reword stem (first call 2 made, unpaid; final call 2 not made); explanation updated. Key B holds |
| 17 | 02ad0c82 | Base for common-size appropriation items | B | FLAWED | Common-size P&L base is normally revenue/net sales; for an appropriation statement net profit is also defensible; no authority settles it | pending |
| 18 | 06dfac31 | Three statements on change in PSR | C | KEY_OK, wording loose | I is false (reserves go in old ratio), II true, III true once worded as gaining partner compensating sacrificing partner | Reword statement III; add explanation. Key C holds |
| 19 | 212dadfc | Death of R, amount payable | A | FLAWED (duplicate) | A and C identical; working 100,000 + 6,000 + 7,500 = 113,500 is right | Change C to "100,000 + 6,000 + 30,000 = 136,000". Key A holds |
| 20 | 2cb64d6f | Unrecorded debtors realised | D | FLAWED (duplicate) | A and D are the same entry (Dr Cash, Cr Realisation) | Change A to "Debit Cash/Bank and credit Debtors Account". Key D holds |
| 21 | 3ab58e08 | Match appropriation items | A | FLAWED | Interest on capital and salary have identical effect, so List II A and D both fit them; matching arbitrary | pending |
| 22 | 59025cc1 | Revaluation profit on retirement, repost in sacrificing ratio | A | FLAWED | Revaluation profit goes to old partners in the old ratio, so A is wrong accounting; C is arguably right but the stem invokes an "agreement" that muddles it | pending |
| 23 | 704ae886 | Loan 30,000 repaid with interest 3,000 | A | FLAWED | Interest is a charge that reduces profit/capitals; A and C both defensible; B/D wrong | pending |
| 24 | 941f38c8 | Admission, revaluation surplus among P, Q, R (2:1:1) | A | FLAWED | Surplus goes to P, Q, R in 2:1:1; option said 2:1 (R omitted) | Option A text "2:1" becomes "2:1:1"; explanation updated. Key A holds |
| 25 | a29d2b33 | Z buys from X yet brings 70,000 capital; retained earnings | C | FLAWED | Stem contradictory; debit P&L and reserve are distributed to old partners, net retained earnings change is not "none" | pending |
| 26 | b5298bc6 | Usual order of settlement on dissolution | A | FLAWED | A and D are both accepted orders | pending |
| 27 | c674cdb3 | Assertion/Reason: gaining partner compensates sacrificing | B | KEY_OK | A true; R true and explains A. Option B text is "Reason explains Assertion", so the audit misread the key. (Its twin ea840ec7 was not checked here.) | none |
| 28 | cfab4918 | Sequence of dissolution accounts | A | FLAWED | Standard order is Realisation, Capital, Bank; option A had Bank before Capital | Reorder option A to "Realisation, Partners' Capital, Cash/Bank"; explanation updated. Key A holds |
| 29 | f2e2c85c | Retirement, auto reallocation of accumulated profits | A | FLAWED | Accumulated profits go in old ratio; keyed sacrificing ratio is wrong; stem convoluted | pending |

Notes: the audit list's item numbers 6-16 contain 11 ids (10 template + 63b4ad47); the table numbers 63b4ad47 as 10 per the IDS file. Every UPDATE in `fix.sql` is guarded on the current correct_answer (pending ones also on status = 'live'). Undo restores exact original bodies, options (full arrays) and explanations.
