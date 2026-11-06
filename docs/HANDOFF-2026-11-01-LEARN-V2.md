# Handoff: Learn v2 and the Explore feed (1 Nov 2026, about 1:45 pm IST)

## Where it stands
- **Website: LIVE for all students** on mockmob.in since about 1 pm (main 978edc236, Vercel dpl_DoGHp6AAWaCKngaFxKAckyhq7vAy).
  Switches LEARN2_ENABLED=true and NEXT_PUBLIC_LEARN2=on (Vercel production). Off = set both off and redeploy.
- **Migration** 20261101150000_learn_runs.sql applied by the owner in the SQL editor (dry run OK first); verified by a read
  (both tables, both SECURITY DEFINER functions, flow_context accepts 'learn', no anon read). Undo:
  `supabase/undo/20261101150000_learn_runs.undo.sql` (worktree wt-1031-learn-v2).
- **Code:** branch `web/1031-learn-v2` (worktree `C:\Users\atish\Desktop\mockmob copy\wt-1031-learn-v2`), fast-forwarded into
  main. Spec `docs/brain/learn-1031/BUILD-1101.md` (Part 1 logic, Part 2 production, Part B UI with B7). Audits A1-A8,
  00-critic, 09-final-critic in `docs/brain/learn-1031/audit-1101/`. Final screenshots `tmp/learn-1101/final/`,
  owner set `tmp/learn-1101/for-owner/`.
- **Verified before deploy:** test:learn 244, keycards 81, auth 137, recovery 637/640 (0 fail), billing 453, egress 101,
  today 120, dock 55; test:app 986/990 (2 landing hero tests that also fail on main). Live smoke: /api/learn/* 401 signed
  out, chapter pages render, no runtime errors. NOT verified: a signed-in session on production (agents never sign in),
  a real phone, a real trackpad, a screen reader.
- **Android app port:** linked session local_3c5cb01e ("Port Learn v2 and the Explore feed to the app"), branch
  `ui/1101-learn-app` in its own worktree, nothing pushed. Done: data layer, study stage, Learn home, Explore covers, feed,
  chapter page (each with tests and goldens). Building: the run, Find with the Cards view. Then entry points, the full
  test gate and the emulator walk. A hung `flutter test` (started 1:11 pm) holds a Flutter slot; its agent was refused a
  kill: the owner may end it.

## App port, at the stop (about 2:55 pm IST, usage 94%)
- All eight packets built on `ui/1101-learn-app` (worktree wt-1101-learn-app); combined gate green (about 3,800 tests, analyze clean).
  Stopped at a checkpoint; three demo builds, the emulator boot and first launch were left running in the background.
  Next for that session: the emulator walk with screenshots after the 4:40 pm IST reset. Nothing pushed.

## Owner, latest words
- "Ship it" and: he wants it live to test everything properly; he "mostly loved the direction"; "a bit of refinement and
  fixes" after deploy; it was "still a bit buggy in the local server". He has feedback to give after testing live.
- CTO decisions he can override: Keep = add to Revise (no fake rating); realistic seconds (about 12 cards and 5
  questions in 10 min); LK15 claimed at the first answered question, Free clamped to 10 min, a second Free run is Key
  cards only; no Must-know tag on feed and run cards; the chapter page keeps the subject object.
- Content calls waiting on him: near-duplicate cards "Define partnership." / "What is partnership?"; the card "If this
  amount is paid to the old partners..." reads oddly alone (feeds no longer open on it).

## Next
1. Get his live feedback (and the local bugs he saw); fix in one round on `web/1031-learn-v2`, suites, screenshots
   (390 and 1440, Night and Day), push to main. Watch Vercel runtime errors (`get_runtime_errors`) after each deploy.
2. Known small items: re-record the two films (they predate 1bfd86ee9); Day theme reshoots after the M-fixes; a real
   Ctrl+P margin check of the print sheet; the server's done count can read one higher than the stop sheet's.
3. App port: let session local_3c5cb01e finish (run, Find, entry points, test gate, emulator walk with screenshots for
   the owner). App release is version 17 with Key cards; the owner does Play steps.
4. Update NOW.md and OWNER-MASTER-LEDGER.md (LK20-LK23) with his verdict.
