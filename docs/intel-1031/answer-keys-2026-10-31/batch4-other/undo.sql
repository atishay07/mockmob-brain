-- kc-anskeys4b undo. One transaction. Not yet run.
BEGIN;

UPDATE questions SET status='live' WHERE status='pending' AND id::text IN ('2fa1db32-6452-43d9-9029-f38760ea1675','7f42972b-b2af-463e-8325-fcf02976a267','25fc5353-75cb-4e8f-856d-884ef5e025e4','6aa9c6ab-95f1-455e-80e9-26d15944015d','ebdc364c-b92e-41e7-a5f3-269d4196c197','1b50b4d1-51af-4cd9-9329-1042fb2b289f','6b103633-584a-4563-bd0b-9ea2782c67be');

UPDATE questions SET options=$q$[{"key":"A","text":"A 1-B, 2-C, 3-A, 4-D"},{"key":"B","text":"B 1-B, 2-C, 3-D, 4-A"},{"key":"C","text":"C 1-B, 2-C, 3-A, 4-D"},{"key":"D","text":"D 1-B, 2-C, 3-A, 4-D"}]$q$::jsonb
WHERE id::text='a88cf495-203f-4641-9c1b-1de126cd8a11';

UPDATE questions SET body=$q$Which of Taylor's principles emphasizes the need for management and workers to work together with full mutual understanding, sharing information and responsibility?$q$
WHERE id::text='17ce534e-0dcb-41e3-8eac-32f1e6804c96';

UPDATE questions SET options=$q$[{"key":"A","text":"A They face diseconomies of scale due to limited access to markets and inputs, raising per-unit costs"},{"key":"B","text":"B They face lower labour costs so long-run average cost is always lower"},{"key":"C","text":"C Government grants eliminate long-run costs differences"},{"key":"D","text":"D Small firms have inherently higher fixed costs per unit because they use more capital"}]$q$::jsonb,
 explanation=$q$Limited market access and input constraints often prevent rural small firms from exploiting economies of scale, raising LRAC.$q$
WHERE id::text='37b98d1f-88b8-4e04-bac2-f48c1e27885c';

UPDATE questions SET options=$q$[{"key":"A","text":"A APC = C/Y will eventually fall and can become negative while MPC = dC/dY remains constant at 0.8"},{"key":"B","text":"B MPC will eventually fall and can become negative, while APC also falls but not necessarily at the same rate"},{"key":"C","text":"C APC will always exceed MPC for all positive Y because of the autonomous term 100"},{"key":"D","text":"D MPC stays above APC for all Y because marginal propensity reflects immediate change"}]$q$::jsonb,
 explanation=$q$MPC = 0.8 - 0.02Y falls with Y and can become negative; APC = 100/Y + 0.8 - 0.01Y also falls, but their rates differ so both decline without a fixed ordering for all Y.$q$
WHERE id::text='44de535d-da3a-4631-bc30-e03ffbe97583';

UPDATE questions SET body=$q$Assertion: A paragraph that begins with a clear topic sentence is always more coherent than one that places the topic sentence at the end. Reason: End placement is used only in paragraphs that are inductive. Choose the correct option.$q$
WHERE id::text='8033d9d6-9ebf-47cd-b5b3-0aba1436b02d';

UPDATE questions SET body=$q$Assertion: In a paragraph the central idea and the topic sentence are interchangeable labels. Reason: A topic sentence always states the paragraph's central idea in one sentence. Choose the correct option.$q$
WHERE id::text='6d92334f-2cce-407e-b9b5-9f5e6c21d69d';

COMMIT;
