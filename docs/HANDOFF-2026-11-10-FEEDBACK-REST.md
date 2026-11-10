# Handoff, 10 Nov 2026 about 10:30 pm IST: the rest of the owner's feedback on the app-refine pass

The prompt to start from is `PROMPT-2026-11-10-FEEDBACK-REST.md` in this folder. This file is the state behind it.

## State

- Live: `origin/main` = `7444fb291` (www.mockmob.in). Branch `web/1110-conversion` in the worktree `C:/Users/atish/Desktop/mockmob copy/wt-1110-convert` is the same commit. Working tree clean. Dev server stopped. Rollback for the whole evening: Vercel `dpl_jgpwQVt4eiE6Cm3iAh9ZJgMf4nq4` (main ca0991ae8).
- The evening's commits: `becb9055b` (the app-refine pass, LK199 to LK206), `a3f239194` and `7444fb291` (the first half of the feedback).
- The owner's feedback is in `OWNER-MASTER-LEDGER.md`, rows LK212 to LK224, with outcomes.

## Done and live from the feedback

- LK212 refund words on /pricing (support line) and /refunds; never a flat no.
- LK213 "What happens when you get Pro" as a timeline built from `paySteps()` in `src/components/pricing/payCopy.mjs`.
- LK214 a fourth "Also in Pro" tile.
- LK215 the Accountancy onboarding note, checked against `data/CUET 2026/accountancy.pdf` ("Optional to Unit V: Computerised Accounting System"). All 16 live subjects' 2026 syllabi were re-read: only Mathematics, Computer Science and Accountancy carry a choice.
- LK220 the Night/Day switch sits beside the mark on phones (`AppLayoutClient.jsx`, `nav-places.css`).
- LK222 locked difficulty levels open the Pro sheet (`SegmentedControl` has `onLockedPress`); the chosen practice tile's ring settles in whole (`practice.css`).
- LK217, first part: the Wallet's first screen and pack rows.

## Not done (the prompt lists them in order)

1. LK218 the Pro pop-up graphic. Not started. A plan is at the end of `tmp/1110-app/notes-pricing2.md`.
2. LK219 the You card, even subjects, a Mob profile. A helper was started and stopped within minutes; it changed no file.
3. LK223 the home sample's loading state and finest questions. A helper was started and stopped within minutes; it changed no file.
4. LK217 the rest of the Wallet. Selling is closed by `WALLET_COMMERCE_OPEN` (Vercel Production). The buying path reads complete in code and has never been run with a payment; refund clawback for packs is not built. Details: `tmp/1110-app/notes-wallet.md`. The owner decides when to test and open it.
5. LK221 the guide redesign with auto-start. Not started. The owner's condition: only if it reaches a very high standard.
6. LK216 web onboarding polish. Not started.

## Facts worth knowing

- Tests that fail with or without any of this work, outside the release gate: `npm run test:mob` (7 server-side tests in mob_v3 files), `npm run test:study` (1, the content gate).
- Last full gate (on becb9055b plus the two later commits' own runs): landing 570 (546 pass, 0 fail), app 1,034, dock 63, du 43, keycards-ui 40, auth 141, billing 453, today 146, subjects 62, recovery 642, learn 440; eslint clean; `next build --webpack` 115/115.
- The dev config keeps dev output in `.next-dev` and build output in `.next`, so a build can run while the dev server runs. Delete both after a session (about 2 GB).
- Walks can fail with "Execution context was destroyed" when a file is saved mid-walk (hot reload). Run them again.
- Playwright will not click a key marked `aria-disabled`; `tap.mjs` has `at=<selector>` for that.
- In Git Bash a lone `/` argument is rewritten to a Windows path: prefix the command with `MSYS_NO_PATHCONV=1`.
- Never checked this evening: a physical phone, iPhone Safari, signed-in pages on production.
