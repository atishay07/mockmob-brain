-- Undo for fix.sql (31 Oct 2026): restores the four rows exactly as they were before the fix (values read just before).
begin;
update public.questions set correct_answer = 'A', explanation = $u$On forfeiture, the premium received on shares issued at a premium is reversed with the other entries for the forfeited shares, so Securities Premium A/c is debited to the extent of the premium received. Leaving the entry unchanged would keep a premium on shares that have been cancelled.$u$
 where id::text = 'b29a66fb56b078260537399fe3a3fcf1';
update public.questions set correct_answer = 'A', explanation = $u$Forfeited share money is capital in nature and shown as a capital reserve under shareholders' funds, and the reason explains the presentation.$u$
 where id::text = '01dc09dc-7b8d-49f7-80ca-9619ee54aae2';
update public.questions set options = $u$[{"key":"A","text":"A 1-A,2-B,3-C,4-C"},{"key":"B","text":"B 1-B,2-A,3-C,4-A"},{"key":"C","text":"C 1-A,2-C,3-B,4-C"},{"key":"D","text":"D 1-C,2-B,3-A,4-B"}]$u$::jsonb,
 explanation = $u$Interest received is operating, purchase of investments is investing, proceeds from loan and dividend paid are financing activities.$u$
 where id::text = '2370d28b-6067-421e-b47b-f79562498f34';
update public.questions set options = $u$[{"key":"A","text":"A Premium on redemption of debentures account (or appropriate reserve for meeting redemption premium)"},{"key":"B","text":"B Profit and Loss Account as immediate income"},{"key":"C","text":"C Discount on Issue of Debentures account"},{"key":"D","text":"D Debentureholders' suspense account"}]$u$::jsonb,
 explanation = $u$Premium on issue is not treated as revenue but credited to a reserve (often 'Premium on redemption of debentures') to meet future liability.$u$
 where id::text = '577f9005-e078-45e5-ae63-cbd4eb8108c9';
commit;
