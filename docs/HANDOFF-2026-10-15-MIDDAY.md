# MockMob handoff, 15 Oct 2026, about 11:25 IST

From session 604ced81 (Opus 5.5), stopped at about 95% usage. Everything is committed and no workflow is running. Read HANDOFF-2026-10-15-FULL.md (same folder) for the owner's profile, standing rules and gotchas. This file covers what changed since 02:45.

## Owner direction today (his words in mockmob-next/tmp/resume-1015/OWNER-WORDS-1014.md and below)

- **Repair:** "It's working, but it should be a bit more useful, like giving more insights." Also: "after each mock, add a SWOT analysis... recommend the next specific topic mocks."
- **Website:** "Keep adding useful features like this and integrate them properly with the UI and website flow overall. Right now everything is very confusing for a new student coming to the site. App is good in this term but website needs fixing or even a redesign."
- **Browser:** never drive his browser. Agents' chrome-devtools starts its own Chrome and cannot see his session, and its windows annoyed him. Never sign in or create accounts, even with a demo email. Use /preview/arena fixtures on a local dev server, captured headlessly.

## Shipped (live)

| What | Where | State |
| --- | --- | --- |
| Website Phase A | origin/main c47a94cd | live |
| Website Phase B | 4d006fb9 | live |
| Repair v3 and the post-mock SWOT | **11e30ec3, pushed at about 11:22 IST** | Vercel deploy not yet checked |

The Phase B website commit 4d006fb9 contains Mobi parity with the app and the repair run you can step back through.

**APK v3 and v4** were sent to the owner (mockmob-next/tmp/apk/MockMob-v4-release.zip, built from 1356ac4f). **APK v5 is not built:** feat/app-and-web is now 34046de9, which includes Repair v3 and the SWOT.

**Production database:**
- **Migration 20261013150000 auth_unconfirmed_passwords applied.** This is the account takeover guard. It was tested on staging first, with a rolled-back test. Logged in STATUS.md, with the undo statements.
- **Mistake Repair verified live** at 08:47 IST: gpt-6-luna, 480 in and 196 out tokens, USD 0.00015.

## Repair v3 and SWOT

- **Spec:** mockmob-next/tmp/repair-v3/SPEC.md.
- **Repair v3, per repair (one model call, 1 credit, max_tokens 1400):**
  - the trap named;
  - why the pick tempted, and where it breaks;
  - why the key is right;
  - the other options;
  - a rule and a memory hook;
  - "Explain it another way", included.
- **Free "From your record" lines,** server-built from stored data.
- **The pattern line,** dated: "Since 15 Oct, 2 of your 3 repairs in X had this trap".
- **The post-mock SWOT** on Full and NTA results only: deterministic, no model, with "Do these next" giving up to 3 one-tap practice sets.
- **Rollback:** set the env REPAIR_PROMPT_VERSION=1 to get the v1 prompt back.
- **Verified:**
  - an adversarial truth review, then 8 fixes, then an independent verifier with every item confirmed;
  - web test:learning 272, recovery 40, app 147, nta 150, eslint clean, build OK earlier;
  - app analyze clean, unit tests about 3,835 green, review and result goldens green.
- **NOT yet verified:** a live v3 repair, meaning real tokens, cost and field drop rate. Ask the owner to do one repair on the site, then query runtime_ai_requests. The expected cost is about USD 0.0004 to 0.001, with output under 1,400 tokens.
- **Watch for 7 days:** spec D.3.

## Website restructure: IN PROGRESS, not live

- **Plan:** mockmob-next/tmp/web-ia/PLAN.md. **Findings:** FINDINGS.md. **Before screenshots:** shots/. **Audits:** audits.json.
- **Summary:** the website takes the app's structure, Today · Practice · Start · Review · You. A sample-first landing, a 2-step onboarding, one name per concept, and every "being prepared" line cut.
- **Owner decisions N1 to N9:** plan section 9.2, all using their defaults. Show them in the Gate A preview.
- **Worktree:** `C:\Users\atish\Desktop\mockmob copy\wt-web-ia`, branch web/ia-1015.
  - It holds WIP commit cdddb6c8, NOT checked.
  - node_modules is a junction to mockmob-hotfix.
- **Run wf_91b1d417-363** (script copy mockmob-next/tmp/workflows/web-ia-build-1015.js; journal at the session's subagents/workflows/wf_91b1d417-363/journal.jsonl):
  - finished: IA0 (contract), plus 4 of IA1 to IA4;
  - cut mid-work: IA5 to IA8, and Gate A.
- **Next steps:**
  1. Read the journal for each result.
  2. Rerun the cut packets (IA5 Practice, IA6 Review and Ask, IA7 You, IA8 pricing and public) on top of cdddb6c8.
  3. Run Gate A: suites, build, headless before and after captures, and the gate-a.html contact sheet sent to the owner.
  4. **IA9:** merge web/alive-1015, which now has Repair v3, into web/ia-1015, then integrate.
  5. Push ONLY after the owner OKs the previews (Gate B).

## Also open

- **v3 recording findings** not yet fixed (mockmob-next/tmp/rec-v3/FINDINGS-v3.md):
  - item 3: hero 3 vs tab 4 to repair;
  - item 4: "last 4" vs "last 6";
  - item 5: the repair run's Mobi row is sparse;
  - item 6: repair copy jargon;
  - item 7: the question swap overlap;
  - item 8: the Practice options under the dock.
- **Emulator recording of v4/v5,** which would also give the real cold-start time now that demo_main sets deferApp.
- **Owner steps:**
  - Supabase Confirm email ON;
  - delete the 5 paused Vercel projects;
  - upgrade Vercel to Pro;
  - the upload key and the Google client ID.
