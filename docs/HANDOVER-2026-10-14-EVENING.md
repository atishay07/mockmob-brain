# MockMob handover, 14 Oct 2026 about 19:30 IST

Session 604ced81 (Opus 5.5) stopped at the owner's request near the usage limit.

**Stopped and safe:**
- All workflows and agents are stopped.
- Every Flutter, Dart and Gradle process is killed and the Flutter lock slots are cleared.
- No emulator is running.
- Every repo is committed and clean apart from tmp and logs.
- Nothing is pushed by agents.

## Owner direction (newest first; his words in the linked files)

- **19:20.** "Focus on app working features and an app you can feel." NTA mode is done. The website shows few meaningful changes; the Weak chapters page was better before (now reverted, see below). He expects fast visible progress: motion, interactivity and feel are what matter.
- **18:30.** docs/brain/design-2026-10-13/OWNER-FEEDBACK-1014-1830.md:
  - Judge the app in use, not from static renders.
  - Spacing and alignment issues, for example Today's Accountancy card art floating at the top with dead space.
  - Light/dark inconsistencies.
  - Balance ranking: balanced, then crowded, then sparse and over-gamified (equally bad).
  - Robustness.
  - Rethink the bottom bar's design and structure.
  - "Looks pretty the same as ... 25 hours ago".
- **Memory:** quality-bar-and-stop-rule.md and mockmob-design-direction.md.

## Where the app is (mockmob-next repo; Flutter in flutter_app)

**Commit chain on feat/app-and-web:**

| Commit | What |
| --- | --- |
| 7e80faf | Phase 1A |
| 5ce16b8 | Phase 1B WIP |
| 18c831e | Phase 1C: 16 area fixers finished their review fixes (reviews in tmp/phase1b-reviews) |

The full test suite has NOT been run on 18c831e. The stabiliser was stopped to free build slots. The last fully green suite was fb510e5 (+3153) on this branch's history.

**Branch ui/phase2:** worktree `C:\Users\atish\Desktop\mockmob copy\wt-phase2`, HEAD 8fe30c4, which is WIP. 17 builders were cut off mid-work. 330 files changed, not analyzed, not tested.

The builders were implementing the four phase 2 specs in docs/brain/ui-phase2/ (in that worktree; also in mockmob-next):

- **DOCK.md:** the rethought bottom bar, Option A: Today, Practice, [Start], Review, You in one centred glass bar. Start opens a go-now sheet. A live capsule shows only when something is happening. Real counts only.
- **MOTION.md:** section 6 is the prioritised build list. Card-into-page transitions, directional tab switch, next-frame touch response, a pull-to-refresh replacing the stock spinner, and a celebration ladder (at most one burst per screen; honour the Celebrations setting).
- **SPACING.md and SPACING-AUDIT.md:** the system, and 80 findings by area with file and fix.
- **ROBUSTNESS.json:** 40 verified bugs (21 P1). Examples: a cached empty profile lets sheet sync overwrite a real plan; an unloaded consent state turns usage data off.

The builders' run journal (agent-by-agent results): `C:\Users\atish\.claude\projects\C--Users-atish-Desktop-mockmob-copy\604ced81-3aa7-4deb-b42c-f324ca5f51e2\subagents\workflows\wf_2b55182d-b37\journal.jsonl`. Results exist only for agents that finished. The run script is mockmob-next/tmp/workflows/app-phase-2-build.js.

**The final art set is approved and ready but NOT integrated:**
- Files: mockmob-next/tmp/art-explore/final/app/*.webp. Placement: tmp/art-explore/NOTES.md and final/anchors.json.
- What it covers: the welcome hero with live Mobi, the plan seal, the milestone backdrop, and the empty states.

**Release APK:** tmp/apk/mockmob-real-release-arm64-380c147.apk. It is older: it predates the blitz and phase 1. No newer APK exists.

## Next steps for the app (do these, fast, visible)

1. In wt-phase2 (ui/phase2), make it compile:
   - `cd flutter_app; bash tool/flutter_locked.sh pub get; bash tool/flutter_locked.sh analyze`
   - Finish each area's half-done items against the four specs. The DOCK first: it is the most visible change.
2. **Do not wait on full golden suites.** Build the demo APK early (`bash tool/flutter_locked.sh build apk --debug -t test/device_demo/demo_main.dart`) and put it on the emulator: AVD mockmob_budget, -memory 2048, about 2.5 GB free RAM needed. Record the opening, the dock, Today, practice to the finish, the result recap and repair (`adb shell screenrecord`), and send the owner clips or frames. He judges motion in use.
3. Integrate the art set with live Mobi (NOTES.md placement).
4. Merge ui/phase2 into feat/app-and-web. Run the full suite once at the end (`bash tool/flutter_locked.sh test -j 1 -r failures-only`; ONE flutter process at a time; a run takes 40 to 60 minutes). Build the real release APK (`--release --target-platform android-arm64 --dart-define-from-file=dart_defines/prod.json`). The owner installs and signs in himself.

**Process rules learned:**
- Agents must never return while their own long command is still running.
- A shared Flutter lock with 2 slots is the bottleneck: keep golden regeneration per area and rare.
- Commit WIP before any stop.
- Copy workflow scripts into mockmob-next/tmp/workflows so a later session can read them.

## NTA (mockmob-hotfix, branch deploy/nta-r5)

**Live in production (origin/main 57c4916, pushed by the owner):**
- engine r5 with the CUET-fit gate, r5.1 and r5.2;
- authored wave 1 (475 questions), published.

**Wave 2: 382 verified questions, publish-ready but NOT published.**
- Biology 56, Computer Science 76, English 55, General Test 77 (stored as `gat`), Geography 44, Maths 65, Political Science 9.
- Commits: 941f1cd, then b5f07fb, which fixes General Test being stored as `general_test`, the subject name the app never reads.
- The online dry run is clean: plan `docs/brain/reports/authored-publish/authored-publish-plan-2026-10-14T12-50-45-595Z.json`, plan hash 73b63070..., 0 blockers.

**Needs the owner:**
1. "publish wave 2". The apply command is in docs/brain/RUNBOOK-PUBLISH-AUTHORED-W2-2026-10-14.md.
2. A push of deploy/nta-r5 (b5f07fb), so production has the wave 2 score tables: `git -C "C:/Users/atish/Desktop/mockmob copy/mockmob-hotfix" push origin deploy/nta-r5:main`

The owner said NTA mode is done, so don't spend more time there unless he asks.

## Website (mockmob-web2, branch feat/web-redesign-p2, ea69c5d; nothing live)

- **Phase 1** (feat/web-redesign) and **Phase 2** are built and tested.
- The owner sees few meaningful changes. The Weak chapters page was reverted to its Phase 1 design (4957872).
- He said nothing more is needed on the website unless polished; the focus is the app.

## Owner actions still open
- Publish wave 2.
- Push deploy/nta-r5.
- Optional: the 59-row listed-order reorder command in hotfix docs.
- Upload key and Google client ID.
- AI-reply SQL.
