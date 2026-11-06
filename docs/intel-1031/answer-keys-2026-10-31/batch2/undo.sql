-- kc-anskeys2 undo. NOT run. Restores every field fix.sql touches to its value as read on 2026-10-31.
begin;

update questions set
  options = $f$[{"key":"A","text":"Both processes involve microbial breakdown of organic matter, but biogas production specifically uses methanogens under anaerobic conditions, while sewage treatment uses aerobic microbes in the primary step."},{"key":"B","text":"Biogas production uses mainly plant waste, while sewage treatment uses mainly human waste."},{"key":"C","text":"Sewage treatment often produces biogas as a byproduct, whereas biogas plants rarely treat sewage."},{"key":"D","text":"Both processes are identical because they occur in the same type of digester."}]$f$::jsonb,
  explanation = null
where id = 'c36c7a90-229e-4db4-83ee-f45cd6ba89ec';

update questions set status = 'live' where id = 'c0acd8a3-4630-4231-a899-573790f1d095';

update questions set
  body = $f$Identifying the difference between actual performance and established standards is known as which step in controlling?$f$
where id = '93fbdc79-d3d6-4957-abde-ee0ebe65de41';

update questions set
  body = $f$Which of the following is a technique used in controlling to ensure that activities are performed according to plans?$f$,
  explanation = $f$Budgetary Control is a quantitative technique used to monitor and control performance against financial plans.$f$
where id = '9ff559b9-90cc-439a-9db6-bda5213ca40f';

update questions set
  body = $f$A company experiences a sudden surge in demand for its products, leading to production bottlenecks. The management team quickly reallocates resources and adjusts production schedules to meet the demand. This demonstrates effective:$f$,
  explanation = $f$Responding to unexpected changes in demand and production by adjusting resources and schedules is a critical aspect of controlling.$f$
where id = '6a04cf27-e0c5-406b-9b76-e5594e504839';

update questions set
  body = $f$Read the statements and choose the correct option.
Statement I: On the eve of independence, India's population was characterized by high birth and death rates, leading to a slow growth rate.
Statement II: The occupational structure was evenly distributed among agriculture, industry, and services.
Statement III: The modern industrial sector, especially cotton textiles and jute, had made significant progress, but the traditional handicraft industry was in decline.$f$,
  explanation = null
where id = '2cd3f1f7-08f9-4e77-b661-fb24498986a7';

update questions set status = 'live' where id = 'cb58ae10-a547-483a-bbde-c826cc7b8229';
update questions set status = 'live' where id = '3254fe26-4580-49ce-b51a-9d0e9157d98f';

commit;
