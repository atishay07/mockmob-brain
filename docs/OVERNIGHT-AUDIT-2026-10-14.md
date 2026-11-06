# Overnight audit, 14 Oct 2026

Range audited: 7f14970..2209123 on feat/app-and-web (19 commits by git count; the handover says 20). Read-only audit: git history and files only, no Flutter runs, no edits. Evidence is at commit 2209123 unless stated.

## Summary verdict

1. The night helped. The data-safety work is real progress: a student's draft is no longer deleted on an unusable 2xx reply, only clear refusals mark a submit rejected, a new paper no longer blocks on an earlier unsent one, sign-out clears tokens first, and the cross-account guard now covers profile, goal, prefs, consent, onboarding and deletion writes.
2. It also left one P1 gap and a handful of P2 items. 47 findings were reported by 8 category checks. 15 were verified, 14 after merging one duplicate. The other 32 were refuted or not shown to be harmful (appendix).
3. Verified by severity: 1 P1, 6 P2, 7 P3. Six are regressions or harm; the rest are copy, scope or hygiene items.
4. The P1 and two of the P2 items share one cause: the expected-user guard added in 2209123 was not passed on the session submit, the events PUT or the outbox replay. That commit says it is untested, so the guard has no green run yet.
5. Recommendation: do not release 2209123 as is. Fix the guard gap, drop the parked onboarding sheet on account deletion, then run the full suite and goldens. Nothing found shows a student losing answers outright; the worst case is a paper wrongly shown as not recorded while the answers stay on the phone.

## Progress confirmed

### Data safety (846043f, 2209123)
- An unusable 2xx reply (no attempt id, 204, proxy page) no longer deletes the draft and journal. The submit stays pending (session_api.dart:84, session_submitter.dart:152).
- Only a clear refusal (400, 422, 402, 403, 404, 409, 413) marks a submit rejected or drops an outbox item. 408, 425, unknown statuses and no-response failures retry (api_error.dart:100). The submit body check matches the server: /api/attempts returns a flat attempt whose id is the session id, so the new id requirement is sound.
- A submit that finishes after an account switch no longer writes the attempts cache or result note into the new account, and the draft delete is pinned to its owner (session_submitter.dart:156-185).
- Starting a new paper no longer blocks on an earlier unsent paper. The earlier draft is archived under its own session id with a backup job queued, and it keeps its last-worked time (session_engine.dart, session_draft_repository.dart:36). The backup job submits the archived draft and retries with backoff on a pending result.
- The outbox flush is single-flight with a rerun flag (sync_providers.dart).
- ApiClient refuses writes whose expected user differs from the token's account, including after a 401 refresh (api_client.dart:233-300). Profile, goal, prefs, consent, onboarding sync and deletion pass it.
- Onboarding sheets are owned per account, parked 30 days on deliberate sign-out and never written to another account.
- Sign-out clears stored tokens before any network call and again under the lock. Sign-out and delete sheets warn when the unsent-work read fails.
- Runner close and reopen of the same session serialise, so a stale engine cannot overwrite the new engine's draft. A fresh open sends unacknowledged answers at once.
- The home-screen widget is overwritten at once on sign-out. SessionSyncer.flushNow loops until the journal is fully sent.

### Security surface (975f270, 5098239)
- Widget provider receiver is exported=false, the redraw broadcast uses FLAG_IMMUTABLE, and the tap href is accepted only under https://www.mockmob.in/ and re-resolved through ActionRouter.
- Launcher shortcuts are cleared on sign-out, never run while signed out, expire after 10 minutes, and resolve through ActionRouter.
- ActionRouter whitelists per-route query params and drops the rest. /practice/start is not an App Link path, so an external link cannot start a session.
- allowBackup stays false, reminder receivers are exported=false, and the login callback filter is unchanged.
- IntendedRoute carries an owner, so account B never lands on account A's remembered screen.
- The share card is private by default (count and date only), subject is opt-in, and nothing leaves the phone until Share is tapped.

### Tests
- Real, tighter tests, not padding: connectivity ping split, archive-and-keep-owed tests that assert the draft is kept, still pending and later submittable, a rejected 422 queues no backup job, NTA 3 s inactive grace on a fake clock, 48x48 tap target, brand opening safety cap and reduce-motion cases, a typed BrokenPrefs fake, and delete-account gating on typing DELETE.
- Edge cases added for repair, scheduler, reminder plan and today builder (late-night boundaries at 4:59, 5:00, 22:59, 23:00). A source-grep test proves no road copy names CSAS.
- Removed scratch probes (zz_band_probe_test, zz_probe goldens) are correctly gone.

### Copy
- No em dashes, en dashes, exclamation marks or emoji in any added copy line. Warm-up answer keys sampled (benzaldehyde, adjoint, growth rate, dependency ratio, Golaknath, Article 352 vs 356) are correct.
- Greeting and Mobi late-night line now change in the same minute. Portal code UR reads as "unreserved" in the ladder caption. First-paper result line names the subject. Defensive filler ("Your sheet is safe here") was dropped from onboarding offline lines. Blocked-channel and prompt-blocked notices state the cause plainly. Insights strategy ids are humanised.
- The notification re-ask cadence matches the owner decision of 14 Oct (docs/brain/HANDOVER-2026-10-14-MORNING.md:54).

### Brand and native
- No logo geometry, mark, wordmark or icon files changed. MainActivity splash lift is guarded against double removal. The opening clock can no longer run out under a slow splash. Reduced motion is re-read after the first frame. Tap-to-skip is never dead. Widget colours match the app palette tokens exactly. Shortcut icons are kept from resource shrinking via raw/keep.xml.
- New native touches are gated: review never in NTA, never in the first 3 days, at most once per 60 days; update only on Play installs and never restarts a live session.

### Churn
- No renames, no CRLF or blank-line churn, no generated or build output, no stray probe files. pubspec and lockfile changes match. Whitespace-only lines are 855 of 26189 added, almost all from real widget wraps.

## Regressions or harm found

### R1. P1. Session writes skip the expected-user guard
- Where: flutter_app/lib/core/sync/session/session_api.dart:35, 45, 56, 74 (putEvents, resume, submit, fetchAttempt); session_submitter.dart:99, 112-116, 137-145; session_engine.dart:584-592. Introduced by 846043f and 2209123.
- Evidence: grep for expectUserId finds nothing in session_api.dart or session_submitter.dart. Other callers pass it (consent_repository.dart:104, goal_repository.dart:25, notification_prefs_repository.dart:41). The submit path awaits journal idle and flushNow before submitting (session_engine.dart:584-592). If the account switches during those awaits, the submit starts with the new account's token. The server refuses with 403 or 404, which isDefinitiveRefusal treats as final (api_error.dart:100-110). The draft is saved rejected=true (session_submitter.dart:112-116), or windowClosed=true on a fetchAttempt 404 (:145), and the student sees "not recorded".
- Correction to the first reading: a request already in flight keeps its own token. The real window is a call that starts after the switch. The answers are kept locally, so they are not deleted, but a paper that is still owed to account A is shown as permanently rejected. A second verifier rated this P2 for that reason; it is kept at P1 here because it breaks the "owed submit stays owed" promise the commit makes.
- Fix: pass expectUserId: draft.userId on putEvents, resume, submit and fetchAttempt. accountChanged has no status and kind unauthorized, so it already maps to SubmitPending and keeps the draft.
- Why: this is the one change that makes the overnight "no cross-account writes" claim true for the data that matters most.

### R2. P2. Outbox replay skips the guard
- Where: flutter_app/lib/core/sync/outbox_repository.dart:187-192 (OutboxFlusher.flush), with due() read at :130-137. Gap present since before 7f14970; 2209123 added the guard but left this caller unwired.
- Evidence: api.request(item.method, item.path, body: item.body, options: ...) has no expectUserId, and _forExpectedUser returns true when none is named. due() is read once for the user signed in at the start, so a sign-out and different sign-in mid-flush sends A's queued writes with B's token.
- Corrections: OutboxItem has no userId field (outbox_repository.dart:15-43), so the fix needs one added or the flusher's scope user passed in. accountChanged is not isUnauthorized, so it falls to the retryLater branch (:205-209) and the flush continues; the item is kept. Harm is the cross-account send, not data loss. This is an incomplete fix more than a regression.
- Fix: carry the scope user id into flush and pass it as expectUserId. Stop the flush on isAccountChanged.

### R3. P2. Account deletion leaves the onboarding sheet parked on the phone
- Where: flutter_app/lib/features/onboarding/state/answers_controller.dart:229-241 (leave, _putAway), answers_store.dart:95-108 (park), sheet_sync.dart ~104-108, delete_screen.dart:137. Introduced by 846043f.
- Evidence: delete calls performSignOut(ref, keepQueuedWork: false), which sets signedOut with sessionExpired false. The sheet_sync listener then calls leave(), which parks any unsynced, non-blank sheet under onboarding_sheet.parked for 30 days. SignOutHooks has no registrations, clearUserData touches only the database, and dropParked runs only from takeFor. The copy in features/you/copy.dart:195-198 says unsent answers "will be removed when you are signed out". Age band, subjects, target colleges and worries stay on the device after a deletion request.
- Fix: when signing out with keepQueuedWork false, drop the parked entry and clear the sheet instead of parking it (a flag the listener checks, or a SignOutHooks entry).

### R4. P2. Opening hand-off can leave a splash ghost after a stalled release
- Where: flutter_app/lib/core/widgets/brand/brand_opening.dart:31-37 (OpeningGlass.release), :139-146 (_markSeen), :179-190 (_handOff). Introduced by 846043f and 352f3f3.
- Evidence: release() swallows the 4 s timeout and returns normally, so wait() looks answered. _markSeen sets _confirmed = true with no check that Android answered. _handOff then skips liftNow(). If Android had stalled, the Flutter mo fades over the first screen for about 150 ms, the ghost frame this code set out to prevent. MainActivity.kt answers within about 150 ms normally, so this is a rare path.
- Fix: have release() return whether Android answered and set _confirmed only on true. Call liftNow() at hand-off otherwise. Add a test where the channel never answers.

### R5. P2. Sign-out expiry line swapped a concrete fact for filler
- Where: flutter_app/lib/features/auth/copy.dart:22, introduced by c204c83.
- Evidence: was "Please sign in again. Your work is still on this phone." Now "Please sign in again. Your work is safe." "Please" is filler and "safe" claims more than the app shows. The same file keeps the concrete "Your work is still on this phone." for loadFailedBody.
- Fix: "Sign in again. Your work is still on this phone."

### R6. P3. One late-night definition became three, and the shared one moved
- Where: flutter_app/lib/core/domain/next_move.dart:88-95 and :101, flutter_app/lib/features/today/logic/move_builder.dart:123, introduced by 8bf1bfb. Still different: features/rhythm/logic/late_night.dart:8 (11 PM to 7 AM) and features/onboarding/screens/onboarding_flow.dart:301 (11 PM to 4 AM).
- Evidence: the old shared rule was hour >= 23 or < 7, the new one is < 5. From 5 to 7 AM the default repair length is no longer the short one and Mobi drops the sleepy art and line. The commit message says "One late-night definition", which is not true, and the handover admits "Not aligned yet".
- Fix: either align late_night.dart and onboarding to the shared constants, or restore the 7 AM end if the 5 to 7 AM behaviour change was not intended. Ask the owner which hours they want.

## Useless or unwanted changes

### U1. P2. CSAS source label stripped, and Round 1 minimums called "closing scores"
- Where: flutter_app/lib/features/onboarding/copy.dart:67, 73, 85; flutter_app/lib/features/you/copy.dart:239. Introduced by 5098239.
- Evidence: "CSAS 2026, Round 1" became "Last year's DU closing scores, out of 1000" and "University of Delhi, 2026 admissions". The figures are Round 1 minimum allocation scores (du_catalog.dart:46-54, du_2026_data.dart:3), so "closing" is less accurate. The owner asked only to drop the road stop. BUILD-BRIEF.md:86 asks for the label on DU numbers. Tools (features/tools/copy.dart:98) still says CSAS 2026 Round 1, so the app now names the same numbers two ways.
- Recommendation: restore a plain "Round 1 minimum, 2026" source line in onboarding and You, or get an owner decision that the label goes. Do not say "closing score".

### U2. P2. Plan "Aim" line still prints the raw portal category code
- Where: flutter_app/lib/features/onboarding/model/plan.dart:173, used via PlanSummary.of by plan_step.dart:137. Missed spot, not a regression: c204c83 only added parentheses around the existing code.
- Evidence: "(UR, out of 1000)" or "ORPHAN-FEMALE" shows to students while the ladder caption uses TodayCopy.categoryWords (today/copy.dart:214-225).
- Recommendation: route the line through categoryWords or a shared copy helper. student_sheet.dart:45 has the same pattern but no references, so it is dead code to delete or ignore.

### U3. P3. Warm-up header comment names the wrong source
- Not in the verified list as a defect; see appendix for the pool approval question.

### U4. P3. Widget picker preview shows sample numbers
- Where: flutter_app/android/app/src/main/res/values/widget_strings.xml:18-25, used by layout/widget_today_preview.xml and xml/today_widget_info.xml:13. Introduced by 5098239.
- Evidence: "Repair 4 mistakes from Mock 7", "2/4", "199", "Updated 9:40 PM" are static and marked as an example in the layout, but design-2026-10-13/owner-materials.md:313 says nothing illustrative is shown as real.
- Recommendation: use neutral text ("Next move", "--") or get the owner to accept samples in the picker.

### U5. P3. Shortcut set differs from the spec
- Where: flutter_app/lib/core/platform/app_shortcuts.dart (shortcutItems, ~56-63). Introduced by 5098239.
- Evidence: ships Resume, 10-min repair and "Practice 10". APP-DESIGN-SPEC.md section 9 (line 623) lists Resume mock, 10-minute repair, Saved mistakes and Fresh check (gated). Fresh check is correctly hidden while the content gate is closed, but "Practice 10" was not asked for and "Saved mistakes" is missing. The handover gives no reason for the swap.
- Recommendation: swap in Saved mistakes, or record the reason for Practice 10 in PENDING.

### U6. P3. Widget keeps the last student's next move when the session ends while the app is closed
- Where: TodayWidgetProvider.kt:510-532 (WidgetModel.read), home_widget_sync.dart:67-69. Introduced by 5098239 and 846043f.
- Evidence: the widget checks only the stored signedIn flag, never the live session. The signed-out write comes from a Dart provider that runs only while the app process is alive. A revoked refresh token or removed session leaves the move title on the home screen of a shared phone until the app next opens. Explicit sign-out is handled.
- Recommendation: accept as a known limit, or keep the move title behind the tap and show only "Open MockMob" plus the countdown.

### U7. P3. Warm-up and picker copy grammar: "Ten questions shows"
- Where: flutter_app/lib/features/practice/copy.dart:54 (53d676d).
- Recommendation: "Ten questions show where you stand."

### U8. P3. Brand warm-up pass does no work
- Where: flutter_app/lib/core/widgets/brand/brand_opening.dart:430-447 (_warmUp).
- Evidence: records paintPose into a PictureRecorder and disposes the picture without drawing it, so no shader or raster cost is paid, and nothing is primed for later frames. The comment at :432-433 claims otherwise.
- Recommendation: rasterise the six poses into a small offscreen image under the splash, or remove _warmUp and the comment. If kept, show a trace.

### U9. P3. Delete-account test is misnamed and lost an assertion
- Where: flutter_app/test/unit/you/account_test.dart:179-197 (2209123).
- Evidence: the test is named "success shows the returned message" but now checks only fixed client copy. DeletionReceipt (delete_screen.dart:16-24) carries no message. The 30-day statement still reaches the student on the ask screen (delete_screen.dart:169, copy.dart:191), so the disclosure is not lost, but the post-request repetition that 7f14970 tested is gone.
- Recommendation: rename the test, or assert the 30-day line on the ask screen.

## Appendix: unverified or refuted claims

These were reported but not confirmed as real, harmful defects. Notes are from the verifiers.

- tests-01, churn-03: bulk golden regeneration. The commit spread is wider than the claim (eight commits, e0ecd97 alone 317 PNGs). It follows listed visual work, so it is a re-baseline, not an unexplained overwrite. Pixel-level review was not possible read-only. A spot check against 7f14970 per area is still sensible; scratch before and after copies are in the session scratchpad under g/a and g/b.
- tests-03, scope-05: the "never returns" removal and the 2, 4, 7, 10 day re-ask follow the owner decision of 14 Oct. Only a stale doc remains: APP-DESIGN-SPEC.md:611 still says "returns after 14 days at most once". Update it. The cadence itself is not owner-confirmed in detail.
- tests-04: the title assertion went because ToolsCopy.noneOpenTitle no longer exists. The cited edit is in 2be7a88 and c204c83, not 2209123.
- tests-05: 2209123 says "NOT tested; full suite not run". The last green run is a817371 (2990 passed). This is a release gate: run the full suite and goldens on 2209123 before shipping. Not a code defect.
- data-safety-04: archiving an unsent paper is an improvement over 7f14970, which overwrote it. The backup job retries with backoff and a network constraint. Residual gap is only if scheduleSubmit itself throws (swallowed at session_engine.dart:68-70).
- data-safety-05: refuted, the server returns a flat attempt with a string id.
- data-safety-06, security-03: refuted, no realistic interleaving between accessToken() and the session read in one isolate; the profile reload keeps the session user.
- data-safety-07: account switch clears the earlier account's outbox by design and tokens are already gone; a missing notice is a UX follow-up, not a regression from this range.
- security-02: the same gap as R2. Verifier noted the flush code is identical in 7f14970, so incomplete fix rather than regression.
- security-04: debugPrint of unhandled errors reaches logcat in release (error_fallback.dart:113-114). Accurate but low exposure. Optional hardening: guard the full text with kDebugMode.
- security-05: share image stays in app cache under a fixed name. Private directory, overwritten on next share. Deleting immediately after share could break the receiving app. Hygiene only.
- security-07: proguard-rules.pro comment at :38-39 is stale (says Play Core is not shipped). No keep rule gap shown. Update the comment and do a release build check anyway.
- copy-a-02: the "Nothing goes to ad or analytics companies" sentence was removed in 2be7a88 (not 4d581a1). The remaining text is accurate and matches PLAY-RELEASE.md. Owner may want it back as a plain fact.
- copy-a-04, copy-a-05, copy-b-01, copy-b-03, copy-b-04, copy-b-05, copy-b-06: style preferences or minor wording. Examples: "free" in altReviewLine, identical great and good finish lines (the enum is used elsewhere), "Your email is still here." removed from the unknown sign-in failure, "Your first lands with a scored set." (threshold still shown by condFirstSet), "share right", generic "Something went wrong" fallback, repeated "any time". None break an owner rule.
- churn-01, churn-02, churn-04: whitespace churn from widget wraps, one pure-whitespace hunk in quick_start.dart (975f270), one trailing-space line in native_touches_test.dart:101. Review 975f270 and 352f3f3 with git diff -w.
- brand-04: turning reduced motion off during the hold window keeps the short opening. Sub-second, cosmetic, not a regression.
- scope-03: the widget day count is labelled "expected CUET" and matches directions-final.md:393. APP-DESIGN-SPEC.md:622 conflicts and should be reconciled.
- scope-04: warm-up pool of 30 comes from the approved bank per STATUS.md:111, but the header at warmup_pool.dart:2-3 still says written for this pool. Fix the comment and record D6 approval.
- scope-07: the "then sleep" late-night lines predate this range.
- scope-08: the reminders prompt sheet rewrite is the pinned footer fix, and the cadence doc comment moved to the new class. Untested, so run the notification goldens.
- scope-09: the pinned start bar answers the short-phone reach problem. Owner may want to confirm.
