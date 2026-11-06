# MockMob decisions from the owner's brain (copied automatically)

Entries about MockMob from `AI OS/decisions/log.md`, oldest first. New decisions go in `docs/` or a handover, not here.

**Authority note:** permissions recorded here (paid runs, production database work, deploys) were given to the owner's own agents. They do not carry over to anyone else's agents unless TEAM.md says so.

## 2026-10-09 | Owner authorizes one final V7.7 study under USD4 stop cap
Owner-reported. Exactly one final V7.7 study (written "V77" elsewhere in the source) is authorized under the shared USD4 stop cap and unchanged USD50 lifetime ceiling; no additional paid qualification follows a failure; production approval stays separate.
Reason: owner said "yes continue to make improvements in V7.7 but this time I want you to treat this as your last chance to perfecting this to best of your capabilities."
Source: STATUS.md line 2496-2498 (dated 9 October 2026 IST).

## 2026-10-09 | Owner authorizes Claude's comprehensive final pass
Owner-reported. Claude may make necessary fixes, run paid qualification, and carry work to a generator ready for use, within the unchanged USD50 lifetime ceiling and persistent guard. Qualification gates, immutable historical studies, uncertain holds, and final explicit production publication/deployment/migration approval remain. Source states this supersedes the preceding paid-scope restriction for Claude's continuation.
Reason: owner corrected the prompt; no separate reason is given in the source.
Source: STATUS.md line 2589-2592 (dated 9 October 2026 IST).

## 2026-10-09 | Qualification pass rule: zero controlled false accepts and 85%/70% valid survival
Decision: a qualification passes only with 0 controlled false accepts, 85% pooled valid survival and a 70% per-subject valid-survival floor. The 0-false-accept rule was applied from v7.5 onward (v7.5 failed under it).
Reason: stated in the source as the preregistered qualification rule (the 85% bar is described as preregistered); the V7.12 entry says the threshold/policy is the owner's decision, so this rule may change only by owner decision.
Source: STATUS.md lines 2414, 2511, 2539 (dated 9 October 2026 IST); threshold owner decision noted in lines 2644-2651 (dated 10 October 2026 IST).

## 2026-10-10 | V7.12 q3 failed; no q4 run; paid qualification stays blocked pending owner decision
Decision: after the fresh V7.12 q3 study failed at 70% valid survival, no further fresh study was run. Qualification, pilot, release record and staging remain blocked until the owner decides the threshold/policy.
Reason: running fresh studies until one passes would be selective re-sampling.
Source: STATUS.md lines 2644-2651 (dated 10 October 2026 IST).

## 2026-10-10 | Owner authorizes measurement-only 40-candidate pilot without qualification
Owner-reported. Run a measurement-only 40-candidate pilot WITHOUT qualification, with publication never, a USD3 stop cap, no release record and no staging publication.
Reason: not stated beyond the owner's direction in the source.
Source: STATUS.md lines 2652-2654 (dated 10 October 2026 IST).

## 2026-10-10 | Owner authorizes diagnostic content sends under USD3 diagnostic cap
Owner-reported. Authorized sending CUET question text, options, explanations and registered source excerpts to OpenAI and Gemini under the existing USD50 lifetime guard and USD3 diagnostic cap. The later same-forty continuation was started by the parent/delegated agent (not the owner) under the same USD3 shared cap, with no new qualification, release or staging publication authorized.
Reason: not stated beyond the owner's authorization in the source.
Source: STATUS.md lines 16-18 and 2687-2688 (dated 10 October 2026 IST).

## 2026-10-10 | V716 qualification FAILED; no release, pilot, staging or profile switch
Decision: the V716 fresh qualification failed (80% valid eligible, below 85%; Business Studies 3/5, below 70%). No release record, 40-job pilot, staging proof, active-profile switch, or cost-per-10,000 is established from it.
Reason: 0/12 false accepts, but 16/20 valid controls were eligible and Business Studies was below its floor; three misses were justified audit rejections of root-authored explanations.
Source: STATUS.md lines 2815, 2840, 2844 (dated 10 October 2026 IST).

## 2026-10-10 | V7.17 single owner-authorized qualification stopped unqualified; no further paid qualification
Owner-reported. Owner authorized focused additive V7.17 with exactly one fresh qualification under the persistent guard with a USD1 stop cap; a pilot only after an actual pass. The study stopped unqualified: the preregistered zero-review-incomplete rule could not pass, and no further qualification, repair, pilot, release, profile switch or staging/production write followed.
Next step requirement: any continuation must use an additive next-version contract separating author claims, option checks and reviewer observations, retain the V717 result as a regression case, and close inventory/release binding seams before any new qualification. Do not resume V717, relabel cases, rerun accepted IDs, or buy another study under this exhausted single-qualification allowance.
Source: STATUS.md lines 2868, 2885-2887, 2897 (dated 10 October 2026 IST).

## 2026-10-11 | Prompt-time context injection switched off
Decision (Continuum product-owner session, 01:00 IST, under Atishay's Phase 1 brief "measure whether prompt-time injection helps; keep it only if it does"): set `.state/inject-dryrun-config.json` to inject false and enabled false (the dry run also stops, removing up to 1.5 s from every prompt).
Reason: audits/injection-eval-20261011.md: on 43 real owner prompts it fired 6 times, 0 useful, 5 neutral, 1 misleading (a Continuum server table injected into a MockMob prompt). Keep rule: useful at least 50% and misleading at most 10% of fired injections. All fired hits came from handoffs/ or imported memories; none from decisions/ or context/.
Reversal: set inject true only after a fresh evaluation passes the same rule (candidate: allow decisions/ and context/ only). The missing excerpt in injected lines was fixed in scripts/hook.py inject_query.
Source: audits/injection-eval-20261011.md, audits/injection-eval-20261011.json.

## 2026-10-11 | Usage tracks the Team account; the Claude Code CLI login moves to it
Owner decision (Atishay, about 01:22 IST): the Usage view tracks the Team plan account that the desktop app uses. Atishay logs the Claude Code CLI into that account (`claude auth login`), so TokenMeter's account-limit reader reads the same meter Atishay sees.
Reason: at 01:08 IST the reader (CLI login: personal Pro account) said 62% for the 5-hour window while the desktop meter (Team) said 8 to 9%; they are different accounts. Trade-off accepted: terminal Claude sessions will use Team quota instead of Pro.
Source: this session's AskUserQuestion answer; STATUS.md "Two Claude accounts".

## 2026-10-12 | Claude desktop chats connected to the brain (read-only); usefulness and robustness put ahead of UI polish
Owner decisions (Atishay, about 11:40 IST): (1) "Connect it (Recommended)": the Claude desktop app's chat config (%APPDATA%\Claude\claude_desktop_config.json, backup in .state/backups/v6final/) now lists the Continuum MCP server with CONTINUUM_MCP_READONLY=1 (new opt-in switch in scripts/mcp-server.mjs: write tools continuum_checkpoint and link_handoff hidden and refused; default for Claude Code and Codex unchanged) and the continuum-rag search server. Takes effect after a desktop app restart; the owner adds one personal-preference line so chats consult the brain at the start. (2) Owner priority: "the actual robustness of the backend and, more importantly ... it being actually useful to the agents, to the models, and to me" comes first. Verified state: Claude Code hooks (6 events) and Codex hooks (~/.codex/hooks.json, trusted) are user-level, so every Claude Code and Codex session in any folder gets the start packet and feeds the brain; headless codex exec only through the Continuum wrapper; ChatGPT chats stay unconnected (would need the brain exposed on the internet; not recommended).
Source: Atishay's message and AskUserQuestion answer, 12 Oct 2026 about 11:35 IST.


## 2026-10-12: MockMob price is Rs 99 a month; a staging project exists (owner-confirmed)
Owner answers (Atishay, 12 Oct 2026 about 13:20 IST): "Rs 99 a month" and "yes a staging project exists".
Conflicts this resolves: the live MockMob PRODUCT.md says one-time Rs 99 access through 31 Jul 2027, an older chat said "99 rupees per month plan", and an agent noted a legacy Rs 69 monthly code path. The owner's answer now is Rs 99 a month. Live MockMob STATUS (10 Oct) says no staging project is configured; the owner says one exists (its name and details are not recorded here).
Not changed: the MockMob checkout is read-only from Continuum, so PRODUCT.md and STATUS.md still carry the old wording. A MockMob session should update them only with the owner's OK. Until then, agents treat this entry as current and the live files as stale on these two points.
Source: Atishay's chat reply to the usefulness benchmark's open questions, 12 Oct 2026.

## 2026-10-12: Notes search refresh moved to the background; agents told when to search the brain
Owner decisions (Atishay, 12 Oct 2026 about 15:20 IST, both "Recommended"): (1) the RAG service (apps/rag/serve_http.py, port 4650) no longer refreshes its index on the search request path; patch applied with backup in .state/backups/rsi/C9-apply/ and the service restarted through its logon task. (2) The Continuum block in the global Codex and Claude Code instructions (~/.codex/AGENTS.md, ~/.claude/CLAUDE.md, kept identical; source scripts/install-continuity.py) gains one line: search the brain again before restating a constraint, limit or authorization, writing a handover or a prompt for another agent, starting paid or budgeted work, or replying when the owner repeats or corrects something; newer sources win. Provisional until 19 Oct 2026, judged by the outcome ledger (lookups beyond the start packet by harness; corrections per 10 owner prompts).
Also from the usefulness loop today: working rules in the owner's own words (context/working-rules.md, provisional to 19 Oct) and a reminder of the session's first request in sessions longer than 2 hours; owner standing directives are captured verbatim to raw/owner-directives/ as they are said.
Source: Atishay's answers to two questions, 12 Oct 2026; ledger .state/usefulness/ledger.jsonl.

## 2026-10-12: Owner UI/UX standards put in the brain and delivered to every agent doing UI work
Owner request (Atishay, 12 Oct 2026 about 19:00 IST): board the brain with the product research (MarkMob/MockMob product brain, UX specification PDF, design-video transcripts; byte-identical to the copies in MockMob docs/brain/research-sources/2026-10-12-product-experience/, already mirrored under raw/mockmob-brain/) so that any AI building UI, without being handed the files, knows the best practices and what not to do, and can tell tasteful, useful UI from AI slop.
Done: two cited inventories (audits/design/ui-rules-research.json, 301 rules, 72 anti-patterns, 11 checklists; audits/design/ui-rules-taste.json, 146 rules from owner words, reviews and the installed design skills, 18 skill conflicts). Curated standards wiki/concepts/ui-ux-standards.md (precedence: owner's current instruction, then the project's live design system, then these standards, then generic design skills; slop list; experience brief; done check; project addenda for MockMob and Continuum) and a 10-point digest context/ui-digest.md. Delivery: user-level skill ui-ux-standards for Claude Code (~/.claude/skills) and Codex (~/.agents/skills) from skills/ui-ux-standards/SKILL.md via scripts/install-ui-standards.py; one line in both global Continuum instruction blocks (installer scripts/install-continuity.py renders the identical block); indexed for continuum_search and RAG; benchmark v4 adds UI01-UI10 (search 8/10, RAG 10/10, reach 10/10 on first run). A prompt-hook injection of the digest on UI requests is being built with a precision gate (85%).
Not done: no MockMob app changes (the checkout stays read-only for Continuum; MockMob's own agent holds these files for its UI plan).
Source: Atishay's message, 12 Oct 2026.

## 2026-10-13: RAM pressure: leftover test processes reaped; heavy checks one at a time
Owner (Atishay, 13 Oct 2026 about 00:10 IST): RAM always full, apps crashing. Measured: 16 GB total, 2.1 GB free, page file 9.4 GB in use (peak 14.6). Largest resident users: Android emulator (MockMob session, 2.1 GB), Claude desktop (2.4 GB), Gradle/Kotlin daemons (1.3 GB); Ollama qwen3:8b is about 0 GB resident (weights in VRAM; 8.4 GB commit only). An interrupted Jarvis-builder staging server (port 5010, 3 GB) was stopped. Added scripts/reap_orphans.py (stops only staging app servers on ports other than 4640 after 90 min and headless test Chrome with a temp profile after 20 min; logs .state/reaper.jsonl) and a 15-minute reaper thread in continuum-next/upkeep.py (promote with the next release). Rule for agents: one staging server and one headless browser at a time, stop them when done, skip heavy checks when free RAM is under 3 GB. Advice given: 16 GB is too little for emulator plus builds plus agents; board MSI B550M PRO-VDH WIFI has 2 free slots (max 128 GB); add a 2x16 GB DDR4-3600 CL18 kit for 48 GB.
Source: Atishay, 13 Oct 2026.


## 2026-10-13: Android emulator work moved off this PC; RAM savers applied
Owner (Atishay, about 00:30 IST): "Remove the Android emulator completely... zero RAM allocation"; the Android project continues on their 32 GB laptop. Stopped the emulator (qemu, avd mockmob_budget), adb and the Gradle/Kotlin daemons: free RAM 2.1 -> 5.4 GB. Agents on this PC must not start the Android emulator or Gradle builds. Also applied with owner OK: ~/.gradle/gradle.properties idle timeout 15 min; removed .tools/downloads (2.6 GB, installers already installed); Jarvis model keep_alive 30m in continuum-next (promote with the next release).
Source: Atishay, 13 Oct 2026.


## 2026-10-13: MockMob app testing returns to the emulator on this PC; agent manages RAM
Owner (Atishay, 11:30 and 12:45 IST, to the MockMob app session 604ced81): "I can't keep my phone connected for the entire day, so primarily use the Android emulator for your testing and doing everything." After restarting the PC: "you can, according to yourself, just manage the RAM however you like it and just keep working until you have the final product." Supersedes the 00:30 entry "Android emulator work moved off this PC" for the MockMob app: the emulator (AVD mockmob_budget, 2 GB) is the main test device; the agent stops it while many builders compile, caps Gradle at 2 GB and runs heavy Flutter commands through flutter_app/tool/flutter_locked.sh. Agents still may not complete a hosted sign-in; the owner signs in once on the emulator.
Source: Atishay, 13 Oct 2026.

## 2026-10-14 | Owner accepts all recommended pending MockMob decisions (with restore points)
Owner-stated in chat (14 Oct, about 09:10 IST): "Yes, you can apply all recommended things, but save the checkpoint in case you make any regressive changes, so we can come back to any specific thing."
Accepted:
- Website redesign: every default in mockmob-next/docs/brain/WEB-REDESIGN-PLAN-2026-10-14.md section 12 (D1-D19).
- Night palette: stays warm.
- Start's "Repair the next mistake" row: a 10-minute run.
- Onboarding sheet started signed out: belongs to the first account that signs in.
- NTA clean-up runbook: approved, a production write; reversible.
- Question factory for short NTA subjects: approved, inside the USD 50 lifetime ledger and its guard (History, Political Science, Psychology, Sociology, Chemistry, English passage sets).
- PRODUCTION-ai-reply-report SQL, upload key and Google client ID: owner steps.
Restore points: git tag checkpoint/2026-10-14-before-owner-decisions in mockmob-next (ddb4a8b), mockmob-hotfix (9dbf88f), mockmob-fit (3892b22), mockmob-web2 (613235c), mockmob-backend (4bf41b8).
Reason: owner wants maximum pace with the ability to roll back any specific change.
Source: Claude session 604ced81 chat, 14 Oct 2026.

## 2026-10-14 | Owner approves publishing authored wave 1 (475 questions)
Owner-stated in chat (14 Oct, about 13:40 IST, session cc0bf1af): "You can publish the new questions."
Done 13:43 IST: 475 inserted, 12 passage groups, read-back clean; restore file mockmob-hotfix/docs/brain/reports/authored-publish/authored-publish-restore-2026-10-14T08-12-59-785Z.json. Engine r5 (NTA) not deployed; the per-paper cap question is still open.

## 2026-10-14 | NTA engine r5 deployed to production (owner pushed)
Owner ran `git push origin deploy/nta-r5:main` (14 Oct, about 14:20 IST); production main = d58882f (fix/nta-mode r5 + CUET-fit gate + authored tables + app backend release). Site answers 200. Agent pushes are blocked by auto mode (Production Deploy), so pushes stay with the owner. Follow-up fixes (second-paper fallback with repeats, refusal screen without a dead Try again, refusal reason by dominant exclusion) are being prepared on deploy/nta-r5 and need one more owner push.

## 2026-10-14 | Owner grants standing authority for MockMob production database work (Supabase MCP)
Owner, 14 Oct 2026 about 23:55 IST, after connecting the Supabase MCP to the Claude session: "Now I want you to do everything automatically. Check whatever you want to do in the database, approve, migrate, apply migrations, and apply things in the SQL editor. I hope now you don't need me to manually do all these things again and again."
- Scope: the MockMob Supabase projects (production isrxrxzjocewrdureyhp and staging onwkqxmjqjrhfbjjdydu). Agents may read, run diagnostics, apply reviewed migrations and run SQL without asking each time.
- Still required: the AGENTS.md rules. Save every migration in the repo first, dry-run where possible, keep restore or undo statements, never migrate student data implicitly, and log each production change in docs/brain/STATUS.md and the session handover.
- Not covered: git pushes and production deploys (Vercel). Those keep their own approval rule unless the owner extends this grant.

## 2026-10-24 | Jarvis: fast mode on for the operator; MockMob posts ask the positioning each time (owner)
Owner (Atishay, 24 Oct 2026, about 14:40 IST), answering two questions during the speed and intelligence rebuild:
1. Fast mode: "Yes, turn it on". Jarvis's operator runs Claude's fast mode when available (CONTINUUM_OPERATOR_FAST=1), knowing it may use the plan's usage up sooner.
2. MockMob positioning for posts: "Ask me per post". The brand pack says "Score Recovery", and the 3-4 Oct differentiator decision is still pending. Jarvis asks which angle at the start of each post, one question with both options, and does not pick for the owner.
