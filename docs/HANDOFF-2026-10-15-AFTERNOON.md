# MockMob handoff, 15 Oct 2026, about 14:00 IST

From session cc0bf1af (Opus 5.5), stopped safely at the owner's usage limit (98%). No workflow, dev server, build or test is running. Everything is committed; nothing new is pushed.

Also read: HANDOFF-2026-10-15-MIDDAY.md and HANDOFF-2026-10-15-FULL.md (same folder) for the owner's profile, rules and gotchas.

## 1. What the owner said today (newest first; these override older plans)

1. **Review on a local server, not HTML files.** "I hope you can show this to me on the local server instead of sending this HTML file." Run the website branch locally and give him the link. He signs in himself; agents never sign in.
2. **The website restructure was rejected** as "a huge regression". The full verdicts are in memory `web-restructure-rejected.md`. In short:
   - Never simplify by cutting. The landing must be "more advanced and better", with a feature showcase and scroll animation.
   - Revert to the old and improve: navigation ("cluttering each page with more information is not the solution"), Practice ("such a beautiful UI"), leaderboard, pricing typography, cutoff calculator (the "New" tag and green line).
   - Keep: onboarding, Study day (refine it), the guide, the Start sheet (add graphics, spacing and typography), the You account part with light/dark, and the brand switch (Bricolage plus the 3D subject objects).
   - Today is okay, but its drop boxes and controls are not designed.
   - **Logo:** remove the bolt mark and the old logo everywhere. Use only logo B, keeping the small dot.
3. **Depth over breadth; the Mistake Lab is the USP.** "implementation and perfection of one feature, and doubling down on each feature ... make it 10 times more useful".
   - He wants back what was lost: time spent on a question, how long it should take, and when an answer was changed.
   - He wants analysis "which no one is giving, and no one in the future is able to give, even with a Claude Max plan or with a team of 100 engineers". It must be easy to understand and reach.
4. **Features, motion and quality over recording and re-testing.** Light checks once per wave; record on the emulator only when he asks.

Memory files written today: `features-over-retesting.md`, `web-restructure-rejected.md`. `quality-bar-and-stop-rule.md` was updated: the usage hook can show the old account's figure after a switch.

## 2. State of every branch

| Branch | Worktree | Head | State |
| --- | --- | --- | --- |
| main (live) | | 11e30ec3 | Repair v3 and the SWOT. Vercel READY, 0 runtime errors at 11:38. No v3 repair yet in runtime_ai_requests. |
| web/alive-1015 | wt-web-refine | 0336dc43 | 8082a0ef: recording fixes (web). 0336dc43: time and decisions restored in the Lab's Find step (time per question against the paper's pace, every answer change with clock times, net marks effect). Both tested by their agents (eslint, test:learning, test:recovery). **Not pushed.** |
| web/v2-1015 | wt-web-v2 | cf51d4d8 | **The new website direction.** Built from web/alive-1015, so it is the live site plus 6 Opus packets (see 3). **Unchecked WIP.** `.env.local` is copied from wt-web-refine. node_modules is a junction to mockmob-hotfix. |
| web/ia-1015 | wt-web-ia | c44ecace | **Rejected. Never ship.** Salvage source only. |
| ui/phase2 (app) | wt-phase2 | 6e6db1aa | bd51ddce: recording fixes. 3feab035: time and decisions in the app result. 6e6db1aa: **unchecked WIP** of feature wave 1 (see 4). |
| feat/app-and-web | mockmob-next | d6bcf22c | Recording fixes merged. APK v5 (from 34046de9) was sent today. |

## 3. Website v2 (wt-web-v2): what the 6 builders did

All builders finished; the checker was stopped before it ran. Their structured results are in the journal of run wf_0d670f77-1fb (session cc0bf1af, subagents/workflows).

- **brand:**
  - Logo B everywhere, with the bolt mark removed and the small dot kept (`src/components/Logo.jsx`, manifest, opengraph).
  - The brand switch is on: Bricolage headings and 3D subject objects (`data/brand_flags.mjs`, `data/subject_art.mjs`, `src/components/brand/SubjectObject.jsx`, `src/app/brand.css`).
  - Preview: `/preview/brand-kit`.
- **you:** the account page he liked (`src/app/(app)/profile/**`, `src/components/profile/**`), with the live leaderboard kept.
- **onboarding:** 2 steps (subjects, then study days), with the days step refined (`src/app/onboarding/**`). Auth logic is unchanged.
- **start:** a Start key plus a premium Start sheet added to the live navigation (`src/components/start/**`, hook-in in `src/app/(app)/AppLayoutClient.jsx`).
- **controls:** one designed control set (`src/components/ui/controls/**`), swapped into the call sites the builder lists.
- **landing:** the live landing kept and made more advanced (`src/app/page.js`, `src/components/landing/**`, `src/app/home.css`).

**Next for v2:**
1. Run the check:
   - review against `web-restructure-rejected.md`: anything plainer or less animated than live is a defect;
   - `npx eslint --max-warnings 0` on the changed files;
   - `npm run test:app`, `test:learning`, `test:recovery`, `test:auth`, `test:nta`, `test:du`, one at a time;
   - `npm run build`: if the junction needs it, set the turbopack root to the parent folder and edit it back by hand. Never `git checkout` it.
2. Commit the fixes.
3. Start the local server for the owner with preview_start `web-v2-local` (`.claude/launch.json` in the "mockmob copy" folder; webpack dev on **http://localhost:3110**). Give him the link and the pages to look at. Signed-in demo views: `/preview/arena?view=...`. He can also sign in himself; email works, Google may bounce to production.
4. Push only on his OK.

## 4. App feature wave 1 (wt-phase2, commit 6e6db1aa, unchecked)

- **M1 motion language:**
  - shared tokens in `shared/motion-tokens.json`, generated into `lib/core/motion/motion_tokens.g.dart`;
  - springs, scrub, drag commit;
  - haptic grammar (Kotlin channel);
  - number memory (`count_up`, `monumental_number`).
- **M2 living objects:** the subject objects float, lean and catch the light, and the object flies into the next screen (`lib/core/art/object_life.dart`, `lib/core/motion/flight.dart`, `launch_rect.dart`).
- **I2:** 13 new subject objects plus sharper re-exports. Masters are in `mockmob-next/tmp/feature-wave-1015/masters/I2`.
- **I1:** sharp scenes plus 4 empty-state scenes. Masters are in `masters/I1`.
- **K0 contract:** added routes and screens for chapters, formats, leaks, revise, week_review and rulebook. **The owner has since cut chapters, formats and week_review.** Remove those, and keep revise, rulebook and leaks only if the Mistake Lab v4 spec uses them.

**Next:**
1. `bash tool/flutter_locked.sh analyze` and the tests of these areas, once.
2. Look at the changed goldens once.
3. Merge into feat/app-and-web.
4. Build APK v6 (command in HANDOFF-2026-10-15-FULL.md, section 5), zip it, and send it.

The web halves of M1, M2, I1 and I2 are not built. Each builder's webHandoff is in the journal of run wf_7f70b018-bc2. Port them into web/v2-1015, not web/ia-1015.

## 5. Mistake Lab v4 (the USP)

- **Restored today** on both platforms: time per question against the paper's pace, every answer change with clock times, and the net marks effect. Web 0336dc43; app 3feab035.
- **Root cause of the loss:** web commit 220e8d51 set `hideFind` on Full and NTA results whenever the SWOT was ready.
- **Data facts:**
  - attempts.details holds only qid, isCorrect and givenIndex;
  - timing and answer changes live in attempts.selection_meta.recovery (telemetry self_reported, timeline, observed.answerChanges);
  - also question_interactions.dwell_ms, user_question_progress.best_dwell_ms and recovery_sessions.events;
  - the full audit is in the journal of run wf_7a498cbc-116 (agent ground:data-audit).
- **Three visions are done:** marks engine, decision forensics ("your paper, replayed") and cohort trap science. Their full texts are in the same journal.
- **The synthesis wrote** `mockmob-next/tmp/mistake-lab-v4/SPEC.md` and `concept.html`. Read them and check they are complete; the run was stopped right after they were written. **Slice 1 is not built.**

**Next:**
1. Show the owner the concept, on the local server or as a short summary.
2. Build slice 1 on web/alive-1015 and the app together, Opus only, with a shared core module, fixtures and copy.json.
3. Merge into web/v2-1015.
4. Truthful numbers with denominators. NTA analysis only after submit. No new paid model calls outside the budget guard.

## 6. Open owner items

- One live Mistake Repair on the site, to verify the v3 cost (expect under USD 0.002 and under 1,400 output tokens in runtime_ai_requests).
- His OK to push:
  - web/alive-1015, the time and decisions restore (a lost feature coming back; recommended);
  - later, web/v2-1015.
- Supabase Confirm email ON; delete the 5 paused Vercel projects; upgrade Vercel to Pro; the upload key and the Google client ID.
- The fix 8 layout call: on a 360 px phone, the Practice options sit under the dock. Default: move the mode pair under the suggestion.

## 7. Gotchas learned today

- The Continuum usage line can show the other account's figure right after he switches accounts. Don't stop on it alone.
- Build every page he will look at with Opus. Sonnet-built pages read as basic to him.
- Never "simplify" by removing sections, animations or showcases. Compare against live before showing.
- Workflow agents must never use `git checkout` or `restore`, even to undo a temporary edit; edit the file back by hand.
- RAM: 16 GB, about 4 GB free with his apps open. Stop the Kotlin/Gradle daemon after an APK build (java.exe with --add-opens). Run one dev server at a time.
