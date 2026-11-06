# NTA fullscreen and answer corrections: corrective audit

## Request and gaps

The owner requested fullscreen exam rehearsal with themed exit warnings and submission after
three warnings, and an apology plus the correct answer and corrective measures when MockMob's
key was wrong. The prior release implemented browser focus strikes and a suspected-key dispute
notice. It never requested fullscreen. Its in-app Exit shortcut could leave NTA mode. Its final
warning overlay hid the existing submission retry. It did not handle the `key_changed` response:
students saw the original option marked Correct beside a message that the key had changed.
Review outcomes were local React state and only returned when a repair was requested again.

## Implemented corrections

- NTA: user-gesture fullscreen entry for the test runner, blocking modal until entry; fullscreen
  exit, visibility and delayed blur monitoring; one strike per absence; two warnings and automatic
  submission on strike three. Return requires fullscreen re-entry when supported. Warnings are
  stored per session identity, survive reload and do not carry into a fresh generation. The timer
  retains its server-derived deadline, including while an entry/warning prompt is open.
- Native modal focus isolation; keyboard answering/navigation blocked during the prompt; no NTA
  in-app Exit shortcut. Failed fullscreen requests stay gated and offer retry without charging a
  strike. Unsupported browsers disclose a focus-only fallback. Terminal submission failure offers
  an accessible retry inside the modal. Successful submission stops monitoring before leaving
  fullscreen. Quick Practice is unaffected.
- Result API reads current question rows only after attempt-owner authorization and adds a display
  review for all changed/held/withdrawn questions, including originally correct and blank answers.
  Original snapshots, details, scores and entitlements are not overwritten. Retrieval errors are
  disclosed. Reading the result never calls a model or reserves an AI credit.
- Confirmed corrections show an apology, original key, corrected key, checked explanation/source
  when available, and a separately labelled marks adjustment. Unknown corrections are explicitly
  unverified and do not produce an adjustment. Changing the question/options/passage prevents
  comparison of old picks. Stale stored explanations are hidden. Option labels distinguish the
  key at submission from the corrected answer. Correction/held logs restore on reload.
- Mistake Repair receives the same review when its eligibility fails. Suspected disagreement
  remains quarantine, never proof. Blind-check indices must be in range; a failed dispute write
  no longer produces a claim that the question was successfully withheld.

## Owner's circular queue question

Read-only production queries matched question `dea6e298-269e-4b18-afd4-53c0b3be7cf5` exactly.
Current bank key is already D, status live, verification_state verified, correct_index null,
explanation null. The screenshot's original key was A. No version-history or dispute-report rows
were returned for this ID, so the provenance/timing of the historical change is not established.
No production data was changed.

A narrowly scoped source-backed display receipt matches this exact ID, stem, ordered options,
passage and current key. [Virginia Tech OpenDSA, sections 9.12.1.2–3](https://opendsa-server.cs.vt.edu/ODSA/Books/pubbook/odsa-all/fall-2019/Public_Instance/html/Queue.html)
uses modulo increments for front/rear to reuse the array cyclically. In the question's fixed-array
comparison, both statements are true and reuse explains better space utilisation: D. B is still
wrong and the owner's screenshot therefore has a zero marks adjustment. The receipt is not a
publication bypass for other questions. Other corrections require the existing trusted
publication-evidence gate before a corrected answer is claimed.

## Actual verification

- test:learning 91/91; test:recovery 35/35; answer-integrity/payment-entitlements 18/18. Eslint
  passed. Production Next.js 16.2.4/Turbopack build passed in the isolated normal checkout.
- Isolated headless Chrome used the real Fullscreen API for entry and exits. Warnings 1 and 2,
  reload persistence, third-strike submission, failed-submission retry and successful retry were
  exercised with local fixture submissions. Fullscreen denial stayed gated with zero strikes.
- Visibility/blur were injected into the actual browser hook and deduplicated. A real headless
  tab switch did not emit the required state, so genuine OS/window/tab-switch behavior is not
  claimed as verified. Browser-only enforcement is bypassable and is not a server proctoring record.
- Corrected result, reload, unverified key and unchanged Quick Practice were exercised. Desktop
  and 390x844 mobile preview compositions were inspected; modal centering and reduced motion
  were confirmed. Screenshots and JSON evidence: local `artifacts/corrective-checks/`.
- A second read-only query confirmed that the live question matches the exact receipt and gives D
  with zero adjustment for B. No paid model request, migration, payment opening or entitlement
  mutation was performed.

## Remaining gates and rollback

Deployment must be verified for the corrective commit. Signed-in production NTA/result flows,
physical phones, real app switching, screen-reader operation and live Luna compatibility remain
unverified. Browser security allows Escape/app switching; a web page cannot lock the operating
system. Fullscreen entry requires a user gesture (see [MDN Fullscreen API](https://developer.mozilla.org/en-US/docs/Web/API/Fullscreen_API)).
Leaderboard/account marks remain the original recorded values; adjustments are display-only
pending a separately evidenced revision workflow. No schema or production-data migration is
part of this release. Reverting the corrective code commit rolls it back without a DB rollback.
