# Accountancy answer-key check

Read-only. Stored key = column `correct_answer` (a letter); `correct_index` is null; explanation is in `explanation`. NCERT text via pdftotext. None of the 5 ids appear in data/keycards/links/accountancy.json; related Key cards were found by topic in decks/accountancy.json and are cited.

## b29a66fb56b078260537399fe3a3fcf1 (Share Capital): KEY_WRONG, correct = C
Q: Shares issued at a premium are forfeited; the full premium was already received and recorded. Treatment of the premium entry?
Stored: A (reverse the premium entry); the explanation argues for A.
Correct: C (leave the entry unchanged).
Evidence: NCERT leac201 (Accountancy Part I), Ch 1 Accounting for Share Capital, printed p. 38: "when the shares are forfeited, all entries relating to the forfeited shares must be reversed except the entry relating to share premium received, if any." Printed p. 39: the securities premium account "is not to be debited at the time of forfeiture if the premium has been received". It is debited only for premium not received.
Key cards: kc.accountancy.share-capital.fact-forfeit-entries-reversed, fact-forfeit-premium-received-no-debit.
Note: the row's own evidence record has solved_key C, so A looks like a publish-time key error.

## 577f9005-e078-45e5-ae63-cbd4eb8108c9 (Debentures): FLAWED, no option correct
Q: Debentures issued at a premium: premium normally credited to which account?
Stored: A (Premium on redemption of debentures account / reserve).
Evidence: NCERT leac202, Ch 2 Issue and Redemption of Debentures, 2.4.3, printed p. 82: "The amount of premium is credited to Securities Premium Reserve account and is shown on the liabilities side of the balance sheet under the head 'Reserves and Surpluses'." Premium on redemption is a separate liability, not where issue premium goes. B, C, D are wrong too.
Suggestion (fix.sql, commented): reword option A to "Securities Premium Reserve account".
Key card: kc.accountancy.debentures.kl-premium-credited-spr.

## 2370d28b-6067-421e-b47b-f79562498f34 (Analysis of Financial Statements): FLAWED, no option correct
Q: Match 1 Interest received, 2 Purchase of investments, 3 Proceeds from term loan, 4 Dividend paid to A Operating, B Investing, C Financing. Stored: A (1-A,2-B,3-C,4-C).
Working: purchase of investments = investing (B); term loan proceeds = financing (C); dividend paid = financing (C); interest received = investing (B) for a non-financial company. Correct set 1-B,2-B,3-C,4-C is not offered (A has 1-A, B has 2-A, C and D are wrong on several).
Evidence: NCERT leac206 (Cash Flow Statement), 6.5.4, printed p. 247: "In case of a non-financial enterprise ... payment of interest and dividends are classified as financing activities whereas receipt of interest and dividends are classified as investing activities." Operating applies only to a financial enterprise, which the stem does not state.
Suggestion (fix.sql, commented): reword option A to "1-B,2-B,3-C,4-C".
Key cards: kc.accountancy.cash-flow-statement.list-investing-inflows, fact-interest-dividend-financial.

## 01dc09dc-7b8d-49f7-80ca-9619ee54aae2 (Share Capital): KEY_WRONG, correct = D
Q: Assertion: amounts in the Forfeited Shares Account are shown under Reserves and Surplus as capital reserve. Reason: forfeited amounts arise from receipts on share capital, so are capital in nature.
Stored: A. Correct: D (assertion false, reason true).
Evidence: NCERT leac201, printed p. 38: "The balance of shares forfeited account is shown as an addition to the total paid-up capital of the company under the head 'Share Capital' ... till the forfeited shares are reissued." Only the profit on reissue is transferred to capital reserve. The chapter's own exercise lists the answer to "Balance of share forfeiture account is shown in the balance sheet under" as share capital.
Caveat: if "Forfeited Shares Account" is read as the post-reissue gain, the assertion would be true. The stem says the account's amounts, so D is the NCERT-faithful reading. Medium confidence; a conservative alternative is to reword the assertion instead.
Key card: kc.accountancy.share-capital.entry-capres.

## d0e86513-a195-4418-9c73-ca0c1176e4e7 (Debentures): KEY_OK, A
Q: Assertion: discount on issue of debentures should be written off over the life of the debentures. Reason: it is a capital loss on raising long-term finance, so may be amortised over the period the debentures are outstanding. Stored A.
Evidence: NCERT leac202, 2.4.2, printed p. 81: the discount "can be written off either by debiting it to or out of Securities Premium Reserve, if any, during the life time of debentures." Both statements hold and the reason explains the practice. Minor wording point: "should" versus NCERT "can"; not enough to change the key.
Key cards: kc.accountancy.debentures.kl-discount-written-off-section-52, entry-write-off-entry.
