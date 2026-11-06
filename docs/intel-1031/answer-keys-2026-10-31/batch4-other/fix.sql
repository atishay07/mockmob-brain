-- kc-anskeys4b fix. One transaction. Not yet run.
BEGIN;

-- 7 pulled to pending (out of live pool)
UPDATE questions SET status='pending' WHERE status='live' AND correct_answer='C' AND id::text='2fa1db32-6452-43d9-9029-f38760ea1675';
UPDATE questions SET status='pending' WHERE status='live' AND correct_answer='B' AND id::text='7f42972b-b2af-463e-8325-fcf02976a267';
UPDATE questions SET status='pending' WHERE status='live' AND correct_answer='B' AND id::text='25fc5353-75cb-4e8f-856d-884ef5e025e4';
UPDATE questions SET status='pending' WHERE status='live' AND correct_answer='C' AND id::text='6aa9c6ab-95f1-455e-80e9-26d15944015d';
UPDATE questions SET status='pending' WHERE status='live' AND correct_answer='B' AND id::text='ebdc364c-b92e-41e7-a5f3-269d4196c197';
UPDATE questions SET status='pending' WHERE status='live' AND correct_answer='A' AND id::text='1b50b4d1-51af-4cd9-9329-1042fb2b289f';
UPDATE questions SET status='pending' WHERE status='live' AND correct_answer='B' AND id::text='6b103633-584a-4563-bd0b-9ea2782c67be';

-- a88cf495 placentation: make C and D distinct wrong sets, key A unchanged
UPDATE questions SET options=$q$[{"key":"A","text":"A 1-B, 2-C, 3-A, 4-D"},{"key":"B","text":"B 1-B, 2-C, 3-D, 4-A"},{"key":"C","text":"C 1-A, 2-C, 3-B, 4-D"},{"key":"D","text":"D 1-B, 2-D, 3-A, 4-C"}]$q$::jsonb
WHERE status='live' AND correct_answer='A' AND id::text='a88cf495-203f-4641-9c1b-1de126cd8a11';

-- 17ce534e Taylor: stem points to cooperation vs individualism only
UPDATE questions SET body=$q$Which of Taylor's principles calls for genuine cooperation between management and workers, in place of individualism and unhealthy competition?$q$
WHERE status='live' AND correct_answer='B' AND id::text='17ce534e-0dcb-41e3-8eac-32f1e6804c96';

-- 37b98d1f: option A no longer misuses diseconomies of scale
UPDATE questions SET options=$q$[{"key":"A","text":"A They cannot exploit economies of scale because of limited access to markets and inputs, raising per-unit costs"},{"key":"B","text":"B They face lower labour costs so long-run average cost is always lower"},{"key":"C","text":"C Government grants eliminate long-run costs differences"},{"key":"D","text":"D Small firms have inherently higher fixed costs per unit because they use more capital"}]$q$::jsonb,
 explanation=$q$Limited market access and input constraints stop rural small firms from exploiting economies of scale, so their long-run average cost stays higher.$q$
WHERE status='live' AND correct_answer='A' AND id::text='37b98d1f-88b8-4e04-bac2-f48c1e27885c';

-- 44de535d: C was also true (APC-MPC = 100/Y + 0.01Y > 0); flip C to a false statement
UPDATE questions SET options=$q$[{"key":"A","text":"A APC = C/Y will eventually fall and can become negative while MPC = dC/dY remains constant at 0.8"},{"key":"B","text":"B MPC will eventually fall and can become negative, while APC also falls but not necessarily at the same rate"},{"key":"C","text":"C APC will always be below MPC for all positive Y because of the autonomous term 100"},{"key":"D","text":"D MPC stays above APC for all Y because marginal propensity reflects immediate change"}]$q$::jsonb,
 explanation=$q$MPC = 0.8 - 0.02Y falls with Y and turns negative beyond Y = 40; APC = 100/Y + 0.8 - 0.01Y also falls, at a different rate. APC - MPC = 100/Y + 0.01Y is always positive, so APC stays above MPC (C and D are false), and MPC is not constant (A is false).$q$
WHERE status='live' AND correct_answer='B' AND id::text='44de535d-da3a-4631-bc30-e03ffbe97583';

-- 8033d9d6: Reason softened from 'only' to 'typical', so R is true and A ('always') is false
UPDATE questions SET body=$q$Assertion: A paragraph that begins with a clear topic sentence is always more coherent than one that places the topic sentence at the end. Reason: End placement is typical of paragraphs that are inductive. Choose the correct option.$q$
WHERE status='live' AND correct_answer='D' AND id::text='8033d9d6-9ebf-47cd-b5b3-0aba1436b02d';

-- 6d92334f: Reason 'always' replaced with 'when present'
UPDATE questions SET body=$q$Assertion: In a paragraph the central idea and the topic sentence are interchangeable labels. Reason: A topic sentence, when present, states the paragraph's central idea in one sentence. Choose the correct option.$q$
WHERE status='live' AND correct_answer='D' AND id::text='6d92334f-2cce-407e-b9b5-9f5e6c21d69d';

COMMIT;
