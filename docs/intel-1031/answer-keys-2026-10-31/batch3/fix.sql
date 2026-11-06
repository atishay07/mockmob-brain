-- NOT RUN. Review first. Guarded: each UPDATE only fires if the row still has the audited values.
BEGIN;

-- 3452e48e: KEY_WRONG, B -> C (gaining partners debited, retiring partner credited)
UPDATE questions
SET correct_answer = 'C',
    explanation = $kc$When continuing (gaining) partners compensate the retiring partner for his share of goodwill, the gaining partners' capital accounts are debited and the retiring partner's capital account is credited (NCERT Part I, p. 114: Gaining Partners Capital A/c Dr., To Retiring Partner's Capital A/c). So: Dr A Capital 28,800 and B Capital 19,200; Cr C Capital 48,000. The bank transfers are between the partners personally, so the firm's bank account is not credited.$kc$
WHERE id::text = '3452e48e-430c-4700-b342-1e448ffafc36'
  AND status = 'live' AND correct_answer = 'B';

-- FLAWED (NCERT p. 81 vs p. 106 conflict, or no option matches): take out of the pool
UPDATE questions SET status = 'pending'
WHERE status = 'live' AND id::text IN (
  '788a636d-64ff-468e-9615-417637064fd5',
  'c4d0b40b-25dd-4c0b-87a0-54bf4bbaa7f1',
  '3d7dbd43-fed8-417c-ae51-f821a958daf5',
  'e05ecfbb-6294-4dbf-88d3-4bcaef7ad9a3',
  'd0e86513-a195-4418-9c73-ca0c1176e4e7');

COMMIT;
