# Missed owner asks, 18 Oct 2026 (to fold into OWNER-MASTER-LEDGER.md)

**What this is.** These are owner asks that no ledger held, from his whole message corpus (`tmp/owner-corpus`, 12 to 17 Oct).

**How it was built:**
- **Sources.** Ten of the twelve sweeps finished (`tmp/resume-1017e/corpus-sweep-results.json`). They found 54 asks marked missing. The synthesizer redid sweeps 3 and 9 (chunk-03 and chunk-09) by hand.
- **Filtering.** An ask was dropped when the master ledger already holds it, or when a newer message reverses it. The newest owner words are `OWNER-FEEDBACK-2026-10-18-DAWN.md`, up to about 4:10 am.
- **Code check.** The rest were checked against live main (origin/main 9578ee66, read through wt-ship17) and the app (wt-v15, ui/v15-1018 at 6ffc3e59).

**Status words** are as in the master ledger: OPEN, DECIDE, DONE, RULE (a standing process rule, nothing to build).

The "In code?" column records what the code does today.

---

## Product asks

| ID | Surface | His words (date, IST unless marked) | What done looks like | Owner area | In code? |
|---|---|---|---|---|---|
| M-001 | App, brand opening | "why is the 3-second logo not up? All that is not done right now." (14 Oct 19:32Z) | **His call:** does he want a longer opening (about 3 s), or was the ask only that the logo B opening be present? Build to his answer. Do not lengthen cold start without his word. | App: brand, motion | **Partly.** Logo B opening exists, but it is about 1.3 s (`core/widgets/brand/brand_opening.dart` timeline 0-1280 ms), not 3 s. **DECIDE.** |
| M-002 | App, copy (USP) | "one of our main USPs is that we have a centralized question bank, and from that, anyone can do unlimited mocks... It should not be in the face... but everyone should know" (16 Oct about 4:50 pm). The W-095 subject claim was to be added to the app (16 Oct 22:31Z). | The app says, truthfully and quietly, that Pro gives unlimited mocks from one central bank (onboarding, credits/plan and the Start sheet). The same wording as the web (W-095), with no "41 subjects". | App: copy, credits | **Partly.** The app says only "Pro includes unlimited practice" (`features/credits/credits_copy.dart:19`). No mention of a central bank or unlimited mocks; no W-095 subject claim. The web landing has it (`src/components/landing/QuestionBankLine.jsx`). **OPEN.** |
| M-003 | App and web, NTA mode | "If someone is pulling down the notification sheet... then 3 seconds. Other than that, if someone is deliberately switching to another app, then normal... we are already giving 3 warnings... No need to give any grace" (13 Oct 18:53Z and 18:58Z) | A brief interruption (3 s or less, such as the notification shade) is forgiven. A deliberate app or tab switch counts at once. Three warnings end the paper. No other grace. | NTA runner (web and app) | **Web: DONE** (`data/exam_integrity.mjs`: BRIEF_INTERRUPTION_MS = 3000, INTEGRITY_STRIKES = 3; `ExamIntegrityGuard.jsx`). **App: not found.** The engine only records time away (`core/sync/session/session_engine.dart` onPaused/onResumed). `nta_strikes` exists only as an end reason (`core/models/session.dart:39`). Confirm whether the app's NTA mode should enforce this. **OPEN (app).** |
| M-004 | App and web, whole product | "I'm not sure how you have incorporated... so does the overall robustness of using all the features and everything" (14 Oct 12:29Z) | A feature-by-feature walk on the emulator and on live: every feature works end to end, with no crash, dead button or lost state. `docs/brain/ui-phase2/ROBUSTNESS.json` items are tracked to closed. | QA (device-truth walk) | No single check exists. W-088 covers states and W-091 covers the live audit. Neither says "every feature works end to end". **OPEN.** |
| M-005 | App, decorative dots | "these dots depicted to show stuff, look cool for sure, but how useful are they is the question... thinking through these kinds of things" (13 Oct 05:46Z) | Every dot or indicator in the app either carries real information or is reworked so that it does. Do not cut anything that is useful (Never again 2). | App: UI polish | Not audited. W-076 and L-020 cover web eyebrow dots only. **OPEN.** |
| M-006 | Web and app, copy | "Important stuff, exciting copy, captions, and many things can be written" in place of the disclaimers (12 Oct 20:59Z) | **His call** on how this fits W-093 ("plain and concrete, no hype"). Proposed: wherever a disclaimer was removed, write motivating, concrete captions that say what the student gets, with no hype words. | Copy | W-093 and W-076 push the other way. **DECIDE.** |
| M-007 | Colleges and Compass, data | "the detail that you have put in just seems a bit wrong to me. Maybe it's right" (15 Oct 14:51Z) | One verification pass of Compass programmes, counts and cutoffs against the CSAS and DU sources. Mismatches are fixed, and the source and date are recorded. | Colleges data | Not verified. W-050 and app L23/L26 cover the UI, not data accuracy. **OPEN.** |
| M-008 | Content, question quality bar | "What a 10 means to me... directly taken from the PYQ... less than 10% deviation... a bit more difficult... not extremely hard to solve" (13 Oct 14:41Z) | His 10/10 definition is written into the judge rubric and the factory brief. **Content runs only when he asks** (memory rule, 17 Oct). | Question pipeline | **Partly.** PYQ anchoring exists (`scripts/pipeline/autonomous/worker.mjs:93` anchor tiers 1-4; `pyq_anchor_id` required at line 610). No "<10% deviation" rule found. **OPEN (rubric text only).** |
| M-009 | Landing and app onboarding, video | "Maybe it is more useful to use it somewhere on the website landing page or in app onboarding... scroll animations... compile your ideas... fire up some Haiku Sonnet agents to give ideas... then we can implement something which we like the most" (16 Oct 11:07 to 11:10 pm) | The idea agents extend the list. Storyboards for the top two are shown to him. He picks. Only then is any of the USD 15 spent (with a 15% reserve). | Brand, motion | **Partly.** `docs/brain/HIGGSFIELD-IDEAS-2026-10-16.md` has seed ideas I1-I6 (landing bank-deals-a-paper scroll, onboarding room wakes up). No storyboard has been shown to him. Not in the master ledger. **OPEN.** |
| M-010 | Backend, AI spend ceiling | "remove the Rs 2,200 ceiling... until my API credits don't run out" (16 Oct 20:06Z) | A migration makes the repo match production: the global `student_ai` row is set to the removed-ceiling value. A fresh database rebuild must not bring the USD 25 cap back. | Backend, DB | **No.** `supabase/migrations/20261004120000_runtime_ai_monthly_cap.sql` still seeds USD 25. `20261017120000_runtime_ai_user_cap.sql:33-34` notes that production was raised to 1000000 by hand. **OPEN** (belongs beside W-098). |
| M-011 | Ops, Vercel | "Yes, you can remove the six duplicate virtual projects." (14 Oct 20:45Z) | The duplicate Vercel projects are gone. The records name five paused ones: mockmob-1uhb, -mmzs, -nxud, -pf37 and -sjsj. Check the count (he said six) before deleting. Deletion is permanent: he clicks it, or he gives a fresh go-ahead in the session. | Ops | Not checked in this pass. Earlier handoffs list them as awaiting deletion. **OPEN.** |
| M-012 | App, notification permission | "Notification prompt can be sent again and again with some unique way of asking to approve it" (13 Oct 18:53Z) | The prompt comes back on a cadence. Its wording varies each time. It never asks during a session or in NTA mode. | App: notifications | **Mostly DONE.** The cadence is built in `features/notifications/logic/pre_prompt_policy.dart`: gaps of 2, 4 and 7 days, then 10 days; only after a result; never during a session or in NTA mode. Varied wording per ask is not verified. |
| M-013 | App, study days | "Study days can be saved on the phone." (13 Oct 18:53Z) | Study days stay readable offline on the phone, and the home widget shows them. | App: rhythm | **Partly.** `RhythmWeek.studyDays` comes from the server model (`core/models/rhythm.dart`) and feeds the home widget (`core/home_widget/home_widget_data.dart:231`). Local persistence is not verified. Low priority. |
| M-014 | Business, iOS | "avoid launching any iOS app unless people explicitly start asking... $100 per year... is my decision" (15 Oct 18:13Z) | No iOS work, and no App Store promise in any copy, until students ask. | Business | **DONE / RULE.** The landing has no App Store mention (grep of origin/main). |
| M-015 | NTA papers, question mix | "Okay, no cap, only deploy them. These new versions are actually better in quality" (14 Oct 08:14Z) | No cap on agent-written questions per paper. Newest-first selection stands. | NTA engine | **DONE / RULE.** No such cap was found in origin/main. |
| M-016 | Brand, mascot and art | "doesn't give me a proper edtech vibe, maybe a bit too gamified... not willing to accept any random generic mascot... only if it's something really legal" (13 Oct 09:28Z) | Any new mascot, logo or art reads as edtech (not over-gamified), is original and is legally safe. Logo B stands (memory: "may switch to A"). | Brand | **RULE.** Logo B was chosen (W-081); Mobi is the in-house code rig. |

## Process asks (standing rules; not in any ledger, only in memory or handoffs)

| ID | His words (date) | Rule | Held where today |
|---|---|---|---|
| M-017 | "If you ever find any such [crucial security concerns], fix it immediately and deploy it." (12 Oct 16:39Z) | Crucial security fixes are hotfixed and deployed without asking. Gates and verifiers still apply. | Memory only (security-fixes-deploy-immediately). |
| M-018 | "explicitly mention it in bold: 'Things needed from you right now.' Otherwise, in every update, just mention 'Nothing needed from your side.'" (12 Oct 20:07Z). Repeated on 13 Oct 18:53Z. | Every update to him ends with one of those two lines. | Nowhere. **Add to the master ledger's rules.** |
| M-019 | "I'm going to sleep now so don't ask me for anything. You have to find workarounds... Optimize the RAM yourself" (12 Oct 21:54Z; 13 Oct 19:46Z). "RAM should not be the deciding factor" (16 Oct 11:23Z), but "The app crashed because of low RAM" (16 Oct 14:49Z). | While he sleeps, never block on a question; find a workaround. Size agent counts for maximum throughput, but reap leftovers (Gradle, headless Chrome, dev servers) so that his apps don't crash. | Memory (overnight-autonomy-relay, agent-swarm-resource-hygiene). |
| M-020 | Newest first: the live request ("go all out in next 15-20 mins and i take over the progress to another account before i go to sleep", 18 Oct about 3 am). Then: "your usage is at 90%, so no need to stop... start preparing a proper handoff" (18 Oct 1:45 am). "I'll switch the account when usage is hit" (17 Oct 01:22Z). "The last agent stopped abruptly because I forgot to tell it to prepare the handoff" (17 Oct 06:59Z). "at 97% or 98%, you can stop" (14 Oct 19:32Z). "The 95% was for another account" (15 Oct 06:13Z). | Prepare the handoff and the next prompt early, without being told, so that a hard stop loses nothing. Don't stop for usage before about 97-98% unless he says. A usage figure from another account doesn't count. The handoff note that said "stop at 87-90%" is not his rule. | Memory (quality-bar-and-stop-rule) and mixed handoff text; it conflicts with HANDOFF-2026-10-17-EVENING section 10. |
| M-021 | "Just go all out in the next 30 minutes" when the window is about to reset (13 Oct 19:46Z; 14 Oct 03:26Z; 14 Oct 17:27Z; 16 Oct 07:37Z). "Keep a check on the stalled agents" (16 Oct 07:55Z). | Near a usage reset with quota left, run maximum parallel work. Watch for stalled agents throughout. | Memory only. |
| M-022 | "Opus as orchestrator... Sonnet is the main heavy lifter... Haiku for the smaller tasks" and "Using so many Sonnet agents just to generate questions is a bit too much" (14 Oct 08:39Z). Older: "100 Haiku agents... cheaper than 1 to 5 Opus agents" (13 Oct 14:45Z). | Newest memory (15 Oct 21:30) wins: Sonnet does the heavy lifting, Haiku the quick tasks, and Opus only complex UI, motion and polish. Planning stays in the main session. Set effort explicitly. | Memory (subagent-model-choice). |
| M-023 | "don't overcomplicate the prompt... one single goal... context in the handoff" (16 Oct 18:13Z; again 20:31Z and 20:41Z) | Every next-session prompt has one goal and points to the handoff, NOW.md and the master ledger for context. | Nowhere. **Add to the master ledger's rules.** |
| M-024 | "say time in 12-hour format... 'in the next 30 minutes'... achievable in 2 hours" (16 Oct 11:19Z) | Use relative times on a 12-hour clock. Size estimates for parallel agents, not one human. | Memory (time-and-estimates-format). |
| M-025 | "You have been doing the same thing since like 3-4 hours now... focus on other things also" (15 Oct 13:39Z). "The app should go side by side with continuous UI/UX improvements" (13 Oct 14:45Z). | Never let one track eat hours while other open asks sit untouched. App improvement keeps running in parallel. | Nowhere. |
| M-026 | "You can use ChatGPT Codex to generate images... access the Continuum brain" (12 Oct 20:59Z). "I have already given you access to a GPT account... GPT Image 2.5" (16 Oct 17:14Z). | Image generation through his GPT account is allowed when it is available (it is not always open). | Memory only. |
| M-027 | "it's a bit too low quality... because of the low resolution of the Android emulator or because it's a too-cheap budget build... let me know" (14 Oct 15:21Z) | Answer him once with evidence: the same screen on a higher-resolution AVD (within the 2-3 GB RAM rule) or on his phone when he connects it. Say whether the quality loss is the emulator or the build. | Not answered in any record. **OPEN.** |

---

## Dropped, with the reason

**Already held by the master ledger or other live files:**
- The count mismatch bug "7 of 10 attempted, 2 wrong, 1 not attempted" (13 Oct). Held by D15 (counts that agree) and the v15 walk findings.
- Mistake Lab v4 on the app (15 Oct). Held by W-034/W-035, D18, "D-items carry over to the app" and W-085.
- The Play closed test: a new app, a 14-day test with 12 or more testers, and he gathers the testers (13 Oct). Held by `PLAY-READINESS-V15.md` and the master ledger's Play row. The newer decision A2 holds v15 until the new Today is built.
- A clear social aspect on app and web (16 Oct 11:44Z). Held by D22, the Mob row and COMMUNITY-1018.
- Remove the NTA privacy line (13 Oct). Held by W-017/W-018.
- Premium motion, generated graphics and vector animation (14 Oct). Held by W-073, W-086 and app L34.

**Reversed by newer words:**
- "Relay can be kept off" (13 Oct 18:53Z). He turned the relay on for overnight on 14 Oct (memory overnight-autonomy-relay).
- "Pick up the pace / stage waves / stop at 87-90%". Superseded by M-020 and M-021 and the live "go all out" request.
- "so much usage limit consumed... 20x max plan" (17 Oct 04:45Z). Superseded by his later "unlimited usage" and the live request.
- "make a plan which we can work upon" (12 Oct). Approved the same day and replaced by later plans.

**Not asks:**
- Information questions: 1000+ accounts, lifetime paid users, the CU2026 loss figure (15k+ spent for 8-9k revenue).
- The fast-mode question.
- "Ignore the old second videos file".
- The Mobbin purchase question.
- The Opal reference (inspiration only).
- Image-only messages with no words (14 Oct 12:24Z, 12:56Z, 14:35Z and 14:38Z; 14 Oct 21:27Z "Looks good till this point", where the screen is not recoverable).

**Too old or ambiguous to act on without him:**
- "Brands... This looks good" (15 Oct 07:47Z). Read as "leave unchanged".
- The CSAS admission portal remark (13 Oct). Superseded by the Compass work.
- "Recap back button: read the logs of why it was built" (13 Oct). The result and recap have been rebuilt several times since.
