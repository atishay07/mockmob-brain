# MockMob: full handoff, 15 Oct 2026, 02:45 IST

From session cc0bf1af (Claude Opus 5.5, account support@mockmob.in), stopped by the owner at about 95% usage. Everything is stopped and committed, and no process is running. This file replaces nothing: it gathers everything in one place. Older detail is in HANDOVER-2026-10-15-NIGHT.md (same folder).

---

## 1. Who the owner is and how he works (read first)

- **Who:** Atishay, founder of MockMob, a CUET UG 2027 prep product. It is "Score Recovery" for Commerce and more subjects, with a Flutter Android app plus a Next.js website at www.mockmob.in.
- **Expectations:** he expects speed and parallelism.
  - Tonight he asked for "a 1-hour task in 10 minutes" and for many agents at once.
  - Do not wait on full test suites before building.
  - Fan out agents on disjoint file ownership.
- **Honest progress:** give real percentages and real ETAs. Never repeat an estimate without new evidence.
- **No regressive changes.** Show taste changes as previews (side by side) before shipping. He trusts your judgment once he has seen direction; for example: "I won't approve every single subject... I'll leave you to it."
- **Parity:** every feature must work the same on the app and the website.
- **Quality bar** (memory files quality-bar-and-stop-rule.md and mockmob-design-direction.md):
  - premium, alive, and judged IN USE (motion, interactivity, robustness), not static;
  - references: HIGH (high.live), Revolut, FamApp; Duolingo-level character acting;
  - balanced: neither sparse nor cluttered or childish;
  - plain sentence-case copy, no filler, no exclamation marks;
  - Night and Day parity;
  - never cover text.
- **His newest creative direction (15 Oct 01:00):** "insane motion graphics... high-quality SVGs, generated images that are animated. The mob [Mobi, the mascot] should be everywhere with different actions and emotions, like Duolingo, real emotions, reacting to different things. Every element interactive, fluid, animated. Every part thoughtful in design. The website and already-built features taken a step further, refined, more finesse and usability."
- **Subject art:** the photo-real lamp-lit 3D subject objects (assets/art/obj-*.webp) are the look he loves ("10/10 quality"). Flat code-drawn emblems read as "basic and childish".
- **Bar icons:** Material Rounded/Outlined pairs (home, quiz, fact_check, initial avatar); the custom ones looked "extremely weird".
- **Stop rule:** work until usage is about 97%. If the reset is more than 30 minutes away, write a proper handoff and stop safely, with no agent left mid-task.
- **Disk:** C: filled to 0 GB once from agent leftovers (memory disk-hygiene.md). flutter_locked.sh now sweeps temp leftovers older than 6 hours. Clean up after builds and recordings, remove finished worktrees, and never touch his Downloads or the AI OS folder.

## 2. Permissions and access granted tonight

- **Production database:** standing authority over the Supabase production database via the Supabase MCP (project isrxrxzjocewrdureyhp; staging onwkqxmjqjrhfbjjdydu). It is recorded in AI OS/decisions/log.md.
  - Rules: save every migration in the repo first, dry-run, keep undo statements, log each production change in docs/brain/STATUS.md, and never change student data implicitly.
- **Bypass permissions** are on in Claude Code.
- **Vercel MCP** is connected: team team_V5PhMz9hqV42vblUMcvhYqoN (slug atishay07s-projects), production project `mockmob` prj_uSolddribHQDl1mM5AKxg3O9qCIu, which serves www.mockmob.in.
- **Deploys:** the owner allowed deploys of tonight's work (repair fixes, wave 2, website improvements).
- **Never paste secret keys into services.** The owner adds keys himself.
- **Agents never sign in to his real accounts.** He tests signed-in flows himself.
- **Fast mode** (Opus) was turned on for this session.

## 3. What shipped tonight (live or delivered)

### Website, production (origin/main = e1773d6a, plus the empty redeploy 6e4b64ed before it)

**Mistake Repair reliability** (audit: docs/brain/REPAIR-LAB-AUDIT-2026-10-14.md):
- the passage is sent to the model (passage_text vs passageText);
- NTA shuffled options are compared by identity (this also fixed hidden keys on NTA result pages);
- maxDuration 90 with per-call timeouts (OpenAI 45 s default);
- credits are never kept on a failure, and stuck reservations are released (plus a daily sweep in /api/internal/finalise-sessions);
- honest codes: provider_timeout, provider_unavailable, budget_reached, wallet_unavailable, paused;
- one log line per failure;
- the word filter is narrowed;
- a fallback to Claude Haiku 5.5.

**Web repair client:** a fresh requestId after a charged-0 failure, a 95 s abort, server messages shown, and the "Â·" mojibake fixed.

**ROOT CAUSE of repairs failing since 5 Oct:** Vercel Production had no OPENAI_API_KEY. The owner added it at about 00:30 and a redeploy was pushed.
- NOT YET VERIFIED by a live repair: no runtime_ai_requests rows yet.
- The owner must do one signed-in repair; then check runtime_ai_requests for an openai gpt-6-luna row.

### Database (production)

- **Migration 20261014183050 runtime_ai_price_claude_haiku_5_5:** the price row for the fallback ($0.10/$0.50 per M).
  - Undo: `delete from public.runtime_ai_prices where provider='anthropic' and model='claude-haiku-5-5';`
- **Authored wave 2 published:** 382 questions plus 1 case set, plan 73b63070, source claude-authored-2026-10-14-w2.
  - Restore file: mockmob-hotfix/docs/brain/reports/authored-publish/authored-publish-restore-2026-10-14T18-48-05-150Z.json.
  - Live counts after: biology 416, computer_science 387, english 382, gat 227, geography 223, mathematics 332, political_science 281.
- **Diagnosis facts:**
  - only 11 repairs in 14 days, from 2 accounts;
  - $0.011 of the $25 monthly cap spent;
  - no stuck credits;
  - the guard accepts gpt-6-luna (tested with a rollback).

### Vercel

- Five duplicate projects (mockmob-1uhb, -mmzs, -pf37, -nxud, -sjsj, each with only a *.vercel.app domain) were PAUSED. The owner approved removal; deletion needs his click. Links were given in chat. The path is vercel.com/atishay07s-projects/<name>/settings/general#delete-project.
- MOCK_AI in Production is "false", which is correct. It is a test switch: when true, moderation AI is faked and question publication is disabled. Leave it.
- Hobby plan: Fluid compute is on, and max duration is 300 s. The owner says Fluid usage was exhausted, and Hobby pauses projects that exceed the free tier; he plans to upgrade to Pro.

### App

- **Release APK v2 delivered** to his phone as mockmob-next/tmp/apk/MockMob-v2-release.zip. It contains MockMob-v2-156ab495.apk: in.mockmob.app, 31.6 MB, obfuscated, arm64, built from feat/app-and-web 156ab495.
  - The phone upload limit is 30 MB, so always zip the APK.
  - v1 (MockMob-phase2-release.zip) is superseded.
- **Contents of v2** (phase 2 rounds 1 and 2):
  - the new bar (Today, Practice, [Start], Review, You), with a live capsule (resume, sending, marked, offline, tonight's move);
  - the Start sheet;
  - a directional tab switch, the bar stepping aside for pushed pages, and container transforms;
  - pull to refresh;
  - Today hero art on the band, the 3D subject objects, Material bar icons;
  - spacing and Night/Day fixes, plus robustness fixes;
  - round-2 in-use fixes:
    - the runner Previous/Next tapLock is 0;
    - no blank frame between questions;
    - the practice title;
    - one paper name throughout;
    - the repair count is truthful;
    - moment layouts;
    - the welcome overflow;
    - the milestone crop.
  - analyze was clean, and 2,866 unit tests passed.
- **Recording v2:** mockmob-next/tmp/rec-1015/v2-journey-small.mp4 was sent. In-use findings are in mockmob-next/tmp/rec-1014/FINDINGS.md (findings 1 to 29).
- **Subject art regenerated** at the old quality and IN the app (wt-phase2): obj-accountancy.webp (calculator on a Debit/Credit ledger) and obj-computerscience.webp (brushed-brass laptop with code). object_art.dart bounds were updated.
  - Business Studies (brass stamp) and Languages (book) KEEP the old renders, by the owner's choice.
  - Candidates and the backup of the old files are in mockmob-next/tmp/subject-art-v2/.
  - The owner says the old set is 8/10 for depicting the subject and 10/10 for quality: only replace a render if it matches that quality.

## 4. State at stop (exact)

### App worktree `C:\Users\atish\Desktop\mockmob copy\wt-phase2`, branch ui/phase2, HEAD fc545b12 (WIP, not analyzed)

This commit holds the partial edits of agents stopped mid-work, plus finished ones. 357 files changed after 5a5e7852.
- **Finished app builders** (run wf_ede58103-677):
  - app-mobi-emotions (the Mobi emotion system in lib/core/mascot);
  - app-review;
  - app-insights-learn.
- **Cut mid-work (partial):** app-today, app-practice, app-result, app-you-notifications, app-rhythm-onboarding, app-bar-tools, app-motion-kit, app-runner. Their item lists come from the planner (see the journal below).
- **Round 3 (run wf_1fb2ccb3-a45):**
  - finished: unit-rest, today-mobi (Mobi bubble over the greeting), onboarding-deeplink (onboarding-05 and -01);
  - cut: cold-start (the 3.3 s logo hold, not done), goldens (the stale goldens refresh, partial).
- **Journals with every agent's return value and the planner's packets:**
  - C:\Users\atish\.claude\projects\C--Users-atish-Desktop-mockmob-copy\cc0bf1af-4c1f-4097-81a5-97ba84470f41\subagents\workflows\wf_ede58103-677\journal.jsonl (25 ideation reports, the planner's 16 packets and the builders' results);
  - ...\wf_1fb2ccb3-a45\journal.jsonl.
- **Workflow scripts:** ...\cc0bf1af-...\workflows\scripts\ (mockmob-alive-and-refined-wf_ede58103-677.js, mockmob-app-phase-2-round3-wf_1fb2ccb3-a45.js); copies of earlier scripts are in mockmob-next/tmp/workflows.
- Resume works only in the same session, so a new session should READ the journals and hand-author a continuation.

### Main app branch `mockmob-next`, feat/app-and-web

- HEAD b5c8a149 plus the doc commits. It has merged ui/phase2 up to 5a5e7852 (156ab495). fc545b12 is NOT merged yet.
- dart_defines/prod.json is here (git-ignored, public values only).

### Website worktree `C:\Users\atish\Desktop\mockmob copy\wt-web-refine`, branch web/alive-1015, HEAD 41f6d53e

- 11 commits on origin/main e1773d6a; NOT pushed; check:web did NOT run.
- node_modules is a junction to mockmob-hotfix/node_modules, which was restored tonight with npm ci after the full disk emptied it.
- **Commits:**
  - Mistake Repair v2 on the web: trap name, another way with contrast, a rule card with Copy, a folded question with key reveal, a marks line, Mobi reacting to the outcome;
  - the MobiReact kit and motion kit, Look and feel prefs (0a7b8ff0);
  - runner and result (d97e0a41, 32af1245);
  - review changes since the last look (a7edefad);
  - Saved and Radar (58fd76e3);
  - rhythm card, Progress and Today (aedfc5d5);
  - arena preview fixtures (e6afd38c);
  - Learn and study (853b048d);
  - nav and dock motion (0d1d486a);
  - Compass (41f6d53e).

### Other repos

- **mockmob-hotfix (deploy/nta-r5 = production):** clean except untouched old modified log files under logs/audit.
- **wt-repair (fix/repair-reliability):** merged into main; it can be removed.
- **mockmob-web2:** the unreleased website redesign (feat/web-redesign-p2); the owner gate is pending. Not touched tonight.

## 5. The plan for the next 5 to 6 hours (the vision, in order)

**Vision:** an app and website that feel alive and premium in use.
- Mobi is a real character with emotions, reacting to real events everywhere it fits. He is never in the timed NTA exam and never over text.
- Motion and micro-interactions on every control.
- Photo-real 3D art and generated, animated scenes.
- Every existing feature refined for usability.
- Identical on web and app.
- Truthful data only.

**Phase A: stabilise and ship what exists (first 60 to 90 minutes)**
1. **App, wt-phase2:** run `bash tool/flutter_locked.sh analyze` from flutter_app. Fix errors from the cut builders: finish or revert half-done edits, using each builder's packet items from the journal.
2. **Finish the cut packets** in parallel (8 app builders, disjoint paths as the planner defined them; re-read the packets from the journal): today, practice, result, you-notifications, rhythm-onboarding, bar-tools, motion-kit, runner. They should call the Mobi emotion API from the finished app-mobi-emotions packet; read lib/core/mascot to learn it.
3. **Round 3 leftovers:**
   - The cold-start 3.3 s logo hold (spec: unfold by 1.0 s). The brand must not wait on data.
   - Regenerate the stale goldens (test/golden/art, practice, core, and any area changed), and OPEN the images.
   - Finding 28: the demo resume card says "0 of 10 answered" while the capsule says 10.
4. **Unit tests** in 3 batches: (core_ui, today, demo, a11y), then (practice, runner, result, review, core_widgets), then the rest. Commit, and merge into feat/app-and-web.
5. **APK v3:**
   - Build in mockmob-next/flutter_app: `MOCKMOB_FLUTTER_SLOTS=3 bash tool/flutter_locked.sh build apk --release --target-platform android-arm64 --obfuscate --split-debug-info=build/symbols --dart-define-from-file=dart_defines/prod.json`.
   - If CMake says "Permission denied" (the antivirus), delete build/.cxx and retry.
   - Zip it and send it to the owner (SendUserFile).
6. **Web, wt-web-refine:**
   - Run eslint on the changed files and the suites test:recovery, test:learning, test:app, test:nta, test:auth, test:answer-integrity. Fix failures.
   - Push to main (`git push origin web/alive-1015:main`, fast-forward from e1773d6a).
   - Check the Vercel deployment and the live site pages.
7. **Verify Mistake Repair:** ask the owner to do one repair in the app, then query runtime_ai_requests via the Supabase MCP.

**Phase B: parity and depth (next 2 to 3 hours)**
8. **App repair v2** to match the web (audit section 5): trap name, another way, rule card, the folded question, a marks line that obeys the truth rules, 2 fresh "checked" questions, holds at +2 and +7 days, one "explain another way" per credit, Mobi reactions. The server side is shared, so check what the web branch added server-side and reuse it.
9. **Mobi everywhere,** done properly:
   - an audit of every screen for where Mobi reacts (wins, empathy after mistakes, waiting, loading, errors, idle, late night);
   - one Mobi per screen;
   - acts land after the state;
   - reduced motion gives still poses.
   - Match the web MobiReact kit, so both platforms use the same moods and triggers.
10. **Motion pass:** every control gets press, release and state motion. Shared-element transitions between list and detail. Number rolls. Sheet physics. Scroll-linked header effects. Profile build on the emulator, and check frames.
11. **Generated animated imagery:**
    - Codex CLI image generation works on the owner's ChatGPT login. Use old renders as style references, demand lamp falloff and chiaroscuro, generate at 1536 and downscale with LANCZOS, matte on pure black.
    - Animate in code: parallax layers, light sweeps, a subtle idle.
    - Candidates: moment scenes (repair recorded, week met, first mock), empty states, welcome.
    - Preview side by side; ship only what matches the 10/10 quality.

**Phase C: prove it (continuous)**
12. **Record the emulator** after each APK and send compressed clips.
    - Setup: AVD mockmob_budget with -memory 2048. Stop the Gradle and Kotlin daemons first. Use the profile demo build (`build apk --profile --target-platform android-x64 -t test/device_demo/demo_main.dart`) and install the app-profile.apk.
    - Tools: tool/emu_rec.sh (`rec_start`, `tapd "^label"`, `rec_stop`, `shot`, `labels`) and tool/frame_sheet.py.
    - Use `tapd "^Submit practice"`, not "^Submit".
    - Git Bash needs MSYS_NO_PATHCONV=1 for adb.
    - ffmpeg comes from imageio-ffmpeg (pip with `--use-feature=truststore`, because the antivirus intercepts TLS).
13. **Commit WIP often.** Keep the handoff current, write a continuum checkpoint after each phase, and stop at about 97% usage with a handoff.

## 6. Open items for the owner

- Click delete on the 5 paused duplicate Vercel projects.
- Do one Mistake Repair in v2 while signed in, so its result can be verified.
- Upgrade Vercel to Pro: Hobby pauses projects over the free tier, and its terms say non-commercial use only.
- Owner-only: the upload key (key.properties) for a signed Play release, the Google client ID in prod.json, Play Console setup, and the AI-reply report SQL (PRODUCTION-ai-reply-report-2026-10-14.sql, which creates the ai_reply_reports table; it can now be run via the Supabase MCP under the database grant).
- Keys he should look at: DeepSeek is at a balance of −$0.03, and the Kimi key is invalid (401). Both are used only by question tooling, not by the app or site.

## 7. Useful facts and gotchas

- **Flutter:** run it only via `bash tool/flutter_locked.sh` (2 slots, `MOCKMOB_FLUTTER_SLOTS` to raise). Run one command per agent, and agents must never return while their own command runs. "failed to delete sqlite3.dll" means wait 60 s and retry.
- **Golden tests and art:** golden tests keep SubjectEmblem.objectArt false. main() and demo_main() set it true, along with SubjectEmblem.idleEnabled true.
- **Demo app:** test/device_demo/demo_main.dart. It is signed in as the fixture student Asha, and liveAppOverrides() in lib/app_overrides.dart is shared with main.dart. It installs as in.mockmob.app.demo (profile) or .demo.debug.
- **Worktrees:** many repos share one git store under "mockmob copy/mockmob copy". Agent worktrees live in .claude/worktrees; remove finished ones.
- **Web tests:** run node --test suites via npm scripts. Use `node --use-system-ca` for network scripts (the antivirus intercepts TLS).
- **Vercel Hobby logs** are kept for 1 hour only. Use the database (runtime_ai_requests, ai_credit_reservations) as the source of truth for AI calls.
- **Routing for subagents** (owner): Opus orchestrates and takes the hardest design work, Sonnet does the heavy code and UI building, and Haiku does small bounded tasks.
