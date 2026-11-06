-- Answer-key fix (31 Oct 2026), evidence in VERDICTS.md (NCERT Accountancy Part I/II, Reprint 2026-27). Undo: undo.sql.
-- Two wrong keys corrected; two questions with no correct option get option A reworded to the NCERT answer (key stays A).
begin;
-- b29a66fb: NCERT leac201 p. 38: on forfeiture every entry is reversed "except the entry relating to share premium received".
update public.questions set correct_answer = 'C', explanation = $f$When shares are forfeited, all entries relating to them are reversed except the entry for share premium already received, so Securities Premium Reserve is not debited. Reversing it would wrongly remove a premium the company has actually received.$f$
 where id::text = 'b29a66fb56b078260537399fe3a3fcf1' and correct_answer = 'A';
-- 01dc09dc: NCERT leac201 p. 38: the share forfeiture balance is added to paid-up capital under Share Capital until reissue.
update public.questions set correct_answer = 'D', explanation = $f$The balance of the Share Forfeiture account is shown as an addition to paid-up capital under Share Capital until the shares are reissued; only the profit on reissue goes to capital reserve. So the assertion is false, while the reason is true.$f$
 where id::text = '01dc09dc-7b8d-49f7-80ca-9619ee54aae2' and correct_answer = 'A';
-- 2370d28b: NCERT leac206 p. 247: for a non-financial enterprise, interest received is an investing activity.
update public.questions set options = $f$[{"key":"A","text":"A 1-B,2-B,3-C,4-C"},{"key":"B","text":"B 1-B,2-A,3-C,4-A"},{"key":"C","text":"C 1-A,2-C,3-B,4-C"},{"key":"D","text":"D 1-C,2-B,3-A,4-B"}]$f$::jsonb,
 explanation = $f$For a non-financial company, interest received and purchase of investments are investing activities, while proceeds from a term loan and dividend paid are financing activities.$f$
 where id::text = '2370d28b-6067-421e-b47b-f79562498f34' and correct_answer = 'A';
-- 577f9005: NCERT leac202 p. 82: premium on issue of debentures is credited to Securities Premium Reserve.
update public.questions set options = $f$[{"key":"A","text":"A Securities Premium Reserve account"},{"key":"B","text":"B Profit and Loss Account as immediate income"},{"key":"C","text":"C Discount on Issue of Debentures account"},{"key":"D","text":"D Debentureholders' suspense account"}]$f$::jsonb,
 explanation = $f$Premium on the issue of debentures is not revenue. It is credited to Securities Premium Reserve and shown under Reserves and Surplus.$f$
 where id::text = '577f9005-e078-45e5-ae63-cbd4eb8108c9' and correct_answer = 'A';
commit;
