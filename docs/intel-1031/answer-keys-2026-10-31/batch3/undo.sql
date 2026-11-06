-- NOT RUN. Restores every field touched by fix.sql.
BEGIN;

UPDATE questions
SET correct_answer = 'B',
    explanation = $kc$The retiring partner's capital is debited and continuing partners' capitals credited in the agreed payment amounts; bank is not directly credited because payment was to C capital accounts.$kc$
WHERE id::text = '3452e48e-430c-4700-b342-1e448ffafc36';

UPDATE questions SET status = 'live'
WHERE status = 'pending' AND id::text IN (
  '788a636d-64ff-468e-9615-417637064fd5',
  'c4d0b40b-25dd-4c0b-87a0-54bf4bbaa7f1',
  '3d7dbd43-fed8-417c-ae51-f821a958daf5',
  'e05ecfbb-6294-4dbf-88d3-4bcaef7ad9a3',
  'd0e86513-a195-4418-9c73-ca0c1176e4e7');

COMMIT;
