-- undo.sql: restores every field fix.sql touches to its pre-fix value. NOT RUN.
begin;

-- A. Template family: exact inverse of the replace
update questions
set body = replace(body, 'is ₹3 plus the entire premium', 'is ₹3 (including premium)')
where id::text in (
 '04219368-5f33-4615-b0ca-1d588afb5187','0b2f66a0-7182-4b42-a31a-541380c32f0e','1b09a38c-495b-434e-8749-ea5005ad3563',
 '248464f4-8466-4be8-97a0-5c37e439a756','72adc20a-a695-455c-a3a0-80c5577b0d71','86a2aa10-b88d-4660-8354-9ca7e9597a1f',
 'bd6df01d-8ac2-45ee-916b-d290325701f7','e4ea3760-5317-4ae8-9ac7-98bc2ff1be70','f288d7f5-f384-4b03-b336-1a96ccfbb7c5',
 'f9a72c4b-7794-4e12-b98d-69690b2e999c')
  and body like '%is ₹3 plus the entire premium%';

-- B. Singles
update questions set
 body = $f$When purchased goodwill is recorded and shown in a comparative balance sheet, which items will definitely change in the vertical (common-size) presentation?$f$,
 explanation = $f$Recognised purchased goodwill increases intangible assets and total assets, thereby changing their vertical percentages.$f$
where id::text = '4758fddf-e094-4f70-aa8d-5afbfb770255';

update questions set
 options = $f$[{"key":"A","text":"A Increase both partners' capital balances in the profit-sharing ratio and increase distributable cash available for final settlement"},{"key":"B","text":"B Debit partners' capitals and credit revaluation reserve, reducing distributable cash"},{"key":"C","text":"C Move the reserve to a liability account thereby reducing net assets and available cash"},{"key":"D","text":"D Post the reserve as a creditor so partners must pay to receive final settlement"}]$f$::jsonb,
 explanation = $f$Transferring reserve to capitals increases partners' capitals according to profit-sharing, raising amounts distributable at settlement.$f$
where id::text = 'd9c47b1c-338e-424a-af28-dfe37c5ca875';

update questions set
 body = $f$Case: A company has issued 20,000 equity shares of Rs 10 each; holders have paid Rs 6 per share (application and allotment) and final call of Rs 2 pending. How should called-up capital and paid-up capital be shown in the balance sheet?$f$,
 explanation = $f$If final call of Rs2 is pending, called-up includes amounts called (application+allotment+first call = Rs8) and paid-up is Rs6 actually received.$f$
where id::text = '63b4ad47-2fa5-4312-9e0a-48943a95502f';

update questions set
 body = replace(body, 'Statement III: Goodwill compensation paid by the gaining partner(s) is credited to the sacrificing partner(s) in their sacrificing ratio.', 'Statement III: Goodwill premium brought by a partner on change is credited to the existing partners in their sacrificing ratio.'),
 explanation = NULL
where id::text = '06dfac31-ad9b-475e-b9d2-201c12720b70';

update questions set
 options = $f$[{"key":"A","text":"A 100,000 + 6,000 + 7,500 = 113,500"},{"key":"B","text":"B 100,000 + 6,000 + 15,000 = 121,000"},{"key":"C","text":"C 100,000 + 6,000 + 7,500 = 113,500"},{"key":"D","text":"D 100,000 + 6,000 + 10,000 = 116,000"}]$f$::jsonb
where id::text = '212dadfc-fc2b-4bab-ada7-c83b36b7b717';

update questions set
 options = $f$[{"key":"A","text":"A Credit Realisation Account and debit Cash/Bank for 6,000"},{"key":"B","text":"B Debit Realisation Account and credit Partner’s Capital for 6,000"},{"key":"C","text":"C Debit Realisation Account and credit Cash/Bank for 6,000"},{"key":"D","text":"D Debit Cash/Bank and credit Realisation Account for 6,000"}]$f$::jsonb
where id::text = '2cb64d6f-e3e7-40df-ba24-6041d0bb5347';

update questions set
 options = $f$[{"key":"A","text":"A S gains 1/5; revaluation surplus to be shared among old partners in 2:1 ratio."},{"key":"B","text":"B S gains 1/5; revaluation surplus shared among all including S in new ratio."},{"key":"C","text":"C S neither gains nor sacrifices; revaluation surplus to old partners in old ratio."},{"key":"D","text":"D S gains weighted amount and surplus adjusted to compensate S directly."}]$f$::jsonb,
 explanation = $f$S acquires 1/5 by existing partners sacrificing in 3:2 ratio so S is a gainer and revaluation surplus belongs to old partners in their old ratio before admission.$f$
where id::text = '941f38c8-7d4b-43b2-af75-9c595286d7fd';

update questions set
 options = $f$[{"key":"A","text":"A Realisation Account → Cash/Bank Account → Partners’ Capital Accounts"},{"key":"B","text":"B Partners’ Capital Accounts → Realisation Account → Cash/Bank Account"},{"key":"C","text":"C Cash/Bank Account → Partners’ Capital Accounts → Realisation Account"},{"key":"D","text":"D Profit & Loss Appropriation → Realisation Account → Cash/Bank Account"}]$f$::jsonb,
 explanation = $f$Assets/liabilities are realised (Realisation Account), cash receipts/payments recorded (Cash/Bank), then partners’ capitals are settled.$f$
where id::text = 'cfab4918-b523-4fc9-9115-5b7d744131b1';

-- C. Back to live
update questions set status = 'live'
where status = 'pending' and id::text in (
 'c2b4dbcb-db48-43d6-b756-ca5fa98f395c','e36eecbb-0a98-4478-bc04-0ff7cd33eaef','02948971-9988-4fe4-b995-56abfb3a02a5',
 '02ad0c82-eb2d-44aa-b1b1-1dc6917c1b12','3ab58e08-6039-4be3-a633-e2147f54e39d','59025cc1-1ff3-4e2e-8aa2-29db643cca21',
 '704ae886-958c-461c-b713-60fcae83a02b','a29d2b33-618a-49aa-88f5-81e402313215','b5298bc6-1606-4c27-b025-16c8558bf59f',
 'f2e2c85c-0b44-49ef-8cd2-a7bc48c3d1ec');

commit;
