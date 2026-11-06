-- fix.sql: Accountancy 29 flagged questions. One transaction. NOT RUN.
begin;

-- ===== A. Template family (10): reword "(including premium)" -> "plus the entire premium" =====
update questions
set body = replace(body, 'is ₹3 (including premium)', 'is ₹3 plus the entire premium')
where id::text in (
 '04219368-5f33-4615-b0ca-1d588afb5187','0b2f66a0-7182-4b42-a31a-541380c32f0e','1b09a38c-495b-434e-8749-ea5005ad3563',
 '248464f4-8466-4be8-97a0-5c37e439a756','72adc20a-a695-455c-a3a0-80c5577b0d71','86a2aa10-b88d-4660-8354-9ca7e9597a1f',
 'bd6df01d-8ac2-45ee-916b-d290325701f7','e4ea3760-5317-4ae8-9ac7-98bc2ff1be70','f288d7f5-f384-4b03-b336-1a96ccfbb7c5',
 'f9a72c4b-7794-4e12-b98d-69690b2e999c')
  and correct_answer = 'A'
  and body like '%is ₹3 (including premium)%';

-- ===== B. Reworded singles =====
-- 4758fddf purchased goodwill: make the purchase on credit so total assets definitely rise
update questions set
 body = $f$When purchased goodwill is recorded on credit (payment still due) and shown in a comparative balance sheet, which items will definitely change in the vertical (common-size) presentation?$f$,
 explanation = $f$Recognised purchased goodwill increases intangible assets. Because the price is still owed, total assets and liabilities both rise, so their vertical percentages change.$f$
where id::text = '4758fddf-e094-4f70-aa8d-5afbfb770255' and correct_answer = 'A';

-- d9c47b1c reserve transfer changes no cash
update questions set
 options = $f$[{"key":"A","text":"A Increase both partners' capital balances in the profit-sharing ratio, with no change in the cash available for final settlement"},{"key":"B","text":"B Debit partners' capitals and credit revaluation reserve, reducing distributable cash"},{"key":"C","text":"C Move the reserve to a liability account thereby reducing net assets and available cash"},{"key":"D","text":"D Post the reserve as a creditor so partners must pay to receive final settlement"}]$f$::jsonb,
 explanation = $f$Transferring the reserve to capitals is a transfer within equity: partners' capitals rise according to the profit-sharing ratio, while cash and net assets stay the same.$f$
where id::text = 'd9c47b1c-338e-424a-af28-dfe37c5ca875' and correct_answer = 'A';

-- 63b4ad47 called-up vs paid-up stem contradiction
update questions set
 body = $f$Case: A company has issued 20,000 equity shares of Rs 10 each; holders have paid Rs 6 per share (application and allotment). The first call of Rs 2 per share has been made but not yet paid, and the final call of Rs 2 has not yet been made. How should called-up capital and paid-up capital be shown in the balance sheet?$f$,
 explanation = $f$Called-up capital = application + allotment + first call = Rs 8 per share = Rs 1,60,000. Paid-up capital is the Rs 6 actually received = Rs 1,20,000. The final call of Rs 2 is not yet called.$f$
where id::text = '63b4ad47-2fa5-4312-9e0a-48943a95502f' and correct_answer = 'B';

-- 06dfac31 statement III reworded (key C unchanged); explanation added
update questions set
 body = replace(body, 'Statement III: Goodwill premium brought by a partner on change is credited to the existing partners in their sacrificing ratio.', 'Statement III: Goodwill compensation paid by the gaining partner(s) is credited to the sacrificing partner(s) in their sacrificing ratio.'),
 explanation = $f$Statement I is wrong: reserves and surplus belong to the old partners and are shared in the old ratio. Statements II and III are correct.$f$
where id::text = '06dfac31-ad9b-475e-b9d2-201c12720b70' and correct_answer = 'C'
  and body like '%Statement III: Goodwill premium brought by a partner on change is credited to the existing partners in their sacrificing ratio.%'
  and explanation is null;

-- 212dadfc options A and C identical: make C a wrong value
update questions set
 options = $f$[{"key":"A","text":"A 100,000 + 6,000 + 7,500 = 113,500"},{"key":"B","text":"B 100,000 + 6,000 + 15,000 = 121,000"},{"key":"C","text":"C 100,000 + 6,000 + 30,000 = 136,000"},{"key":"D","text":"D 100,000 + 6,000 + 10,000 = 116,000"}]$f$::jsonb
where id::text = '212dadfc-fc2b-4bab-ada7-c83b36b7b717' and correct_answer = 'A';

-- 2cb64d6f options A and D identical: make A a wrong entry
update questions set
 options = $f$[{"key":"A","text":"A Debit Cash/Bank and credit Debtors Account for 6,000"},{"key":"B","text":"B Debit Realisation Account and credit Partner’s Capital for 6,000"},{"key":"C","text":"C Debit Realisation Account and credit Cash/Bank for 6,000"},{"key":"D","text":"D Debit Cash/Bank and credit Realisation Account for 6,000"}]$f$::jsonb
where id::text = '2cb64d6f-e3e7-40df-ba24-6041d0bb5347' and correct_answer = 'D';

-- 941f38c8 surplus shared by old partners P, Q, R in 2:1:1
update questions set
 options = $f$[{"key":"A","text":"A S gains 1/5; revaluation surplus to be shared among old partners in 2:1:1 ratio."},{"key":"B","text":"B S gains 1/5; revaluation surplus shared among all including S in new ratio."},{"key":"C","text":"C S neither gains nor sacrifices; revaluation surplus to old partners in old ratio."},{"key":"D","text":"D S gains weighted amount and surplus adjusted to compensate S directly."}]$f$::jsonb,
 explanation = $f$S acquires 1/5 from P and Q in the ratio 3:2, so S is a gainer. The revaluation surplus belongs to the old partners P, Q and R in their old ratio 2:1:1, before admission.$f$
where id::text = '941f38c8-7d4b-43b2-af75-9c595286d7fd' and correct_answer = 'A';

-- cfab4918 standard order Realisation, Capital, Bank
update questions set
 options = $f$[{"key":"A","text":"A Realisation Account → Partners’ Capital Accounts → Cash/Bank Account"},{"key":"B","text":"B Partners’ Capital Accounts → Realisation Account → Cash/Bank Account"},{"key":"C","text":"C Cash/Bank Account → Partners’ Capital Accounts → Realisation Account"},{"key":"D","text":"D Profit & Loss Appropriation → Realisation Account → Cash/Bank Account"}]$f$::jsonb,
 explanation = $f$Assets and liabilities are first dealt with through the Realisation Account, its profit or loss goes to the Partners’ Capital Accounts, and the Cash/Bank Account is closed last when the balance is paid to partners.$f$
where id::text = 'cfab4918-b523-4fc9-9115-5b7d744131b1' and correct_answer = 'A';

-- ===== C. Pull from live pool =====
update questions set status = 'pending'
where status = 'live' and (
  (id::text = 'c2b4dbcb-db48-43d6-b756-ca5fa98f395c' and correct_answer = 'A') or
  (id::text = 'e36eecbb-0a98-4478-bc04-0ff7cd33eaef' and correct_answer = 'C') or
  (id::text = '02948971-9988-4fe4-b995-56abfb3a02a5' and correct_answer = 'A') or
  (id::text = '02ad0c82-eb2d-44aa-b1b1-1dc6917c1b12' and correct_answer = 'B') or
  (id::text = '3ab58e08-6039-4be3-a633-e2147f54e39d' and correct_answer = 'A') or
  (id::text = '59025cc1-1ff3-4e2e-8aa2-29db643cca21' and correct_answer = 'A') or
  (id::text = '704ae886-958c-461c-b713-60fcae83a02b' and correct_answer = 'A') or
  (id::text = 'a29d2b33-618a-49aa-88f5-81e402313215' and correct_answer = 'C') or
  (id::text = 'b5298bc6-1606-4c27-b025-16c8558bf59f' and correct_answer = 'A') or
  (id::text = 'f2e2c85c-0b44-49ef-8cd2-a7bc48c3d1ec' and correct_answer = 'A')
);

commit;
