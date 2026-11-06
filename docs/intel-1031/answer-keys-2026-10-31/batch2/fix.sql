-- kc-anskeys2 fix. NOT run. Each UPDATE is guarded on the current correct_answer (and status where relevant).
begin;

-- 1. c36c7a90 Biology sewage/biogas: option A said "primary step" uses aerobic microbes. NCERT: primary = physical; secondary = aerobic. Reword option A.
update questions set
  options = jsonb_set(options, '{0,text}', to_jsonb($f$Both processes involve microbial breakdown of organic matter, but biogas production specifically uses methanogens under anaerobic conditions, while sewage treatment uses aerobic microbes in the secondary (biological) step.$f$::text)),
  explanation = $f$Biogas plants rely on methanogens working anaerobically on dung or plant waste. Sewage treatment shares the idea of microbial breakdown, but its primary step is only physical (filtration and sedimentation); aerobic microbes act in the secondary, biological step in aeration tanks. So the two are related, not unrelated, yet they are not identical.$f$
where id = 'c36c7a90-229e-4db4-83ee-f45cd6ba89ec' and correct_answer = 'A' and options->0->>'key' = 'A';

-- 2. c0acd8a3 Biology lac operon with glucose + lactose: outside NCERT (positive regulation/CAP is "beyond the scope" per NCERT p.101), and key C is wrong on the repressor (lactose inactivates it). Take out of live pool.
update questions set status = 'pending'
where id = 'c0acd8a3-4630-4231-a899-573790f1d095' and correct_answer = 'C' and status = 'live';

-- 3. 93fbdc79 Business controlling steps: "difference between actual and standards" is Step 3 (Comparing), not offered. Reword stem to describe Step 4.
update questions set
  body = $f$Determining the acceptable range of deviations and finding out their causes is known as which step in controlling?$f$
where id = '93fbdc79-d3d6-4957-abde-ee0ebe65de41' and correct_answer = 'C';

-- 4. 9ff559b9 Business control techniques: Network Analysis (PERT/CPM) and Management by Exception also appear as techniques in NCERT. Restrict stem to traditional techniques.
update questions set
  body = $f$Which of the following is a traditional technique used in controlling to ensure that activities are performed according to plans?$f$,
  explanation = $f$NCERT lists personal observation, statistical reports, breakeven analysis and budgetary control as the traditional techniques of managerial control. An organisation chart belongs to organising, and PERT/CPM (network analysis) is a modern technique. Management by exception is a principle applied with critical point control, not a traditional technique.$f$
where id = '9ff559b9-90cc-439a-9db6-bda5213ca40f' and correct_answer = 'A';

-- 5. 6a04cf27 Business reallocating resources: ambiguous (planning / co-ordination / controlling). Reword stem so the deviation and corrective action are explicit.
update questions set
  body = $f$A company experiences a sudden surge in demand, and production falls short of the targets set. The management team compares actual output with the targets, analyses the shortfall and takes corrective action by reallocating resources and adjusting production schedules. This demonstrates effective:$f$,
  explanation = $f$Comparing actual output with targets, analysing the deviation and then taking corrective action (for example, assigning additional workers and equipment when work is behind schedule) are steps of the controlling process.$f$
where id = '6a04cf27-e0c5-406b-9b76-e5594e504839' and correct_answer = 'C';

-- 6. 2cd3f1f7 Economics eve of independence: Statement III said modern industry "had made significant progress"; NCERT says its progress remained very slow. With the original text no option is correct (only I is true). Reword III so I and III are true (key A).
update questions set
  body = $f$Read the statements and choose the correct option.
Statement I: On the eve of independence, India's population was characterized by high birth and death rates, leading to a slow growth rate.
Statement II: The occupational structure was evenly distributed among agriculture, industry, and services.
Statement III: Modern industry, especially cotton textiles and jute, began to take root, but its progress remained very slow, and the traditional handicraft industry was in decline.$f$,
  explanation = $f$Statement II is false: agriculture employed 70-75 per cent of the workforce, manufacturing about 10 per cent and services 15-20 per cent. Statement III now matches NCERT: modern industry began with cotton and jute mills but progressed very slowly while handicrafts declined. Statements I and III hold.$f$
where id = '2cd3f1f7-08f9-4e77-b661-fb24498986a7' and correct_answer = 'A';

-- 7. cb58ae10 Political Science Neighbourhood First / Look East / SAARC: "Neighbourhood First" is not in NCERT, and List II B and C both describe SAARC, so the mapping cannot be settled from the book. Take out of live pool.
update questions set status = 'pending'
where id = 'cb58ae10-a547-483a-bbde-c826cc7b8229' and correct_answer = 'B' and status = 'live';

-- 8. 3254fe26 Political Science environmental mobilisation match: keyed option uses B twice and never C (not 1:1), and the tactics are not in NCERT. Take out of live pool.
update questions set status = 'pending'
where id = '3254fe26-4580-49ce-b51a-9d0e9157d98f' and correct_answer = 'C' and status = 'live';

commit;
