---
name: owner-feedback-1017
description: "Owner's 17 Oct 12:45 am feedback (app nav, liquid glass, web start menu, fine-tune scope, result screen clutter, Today, dock); full words and ledger F1-F16 in docs/brain/OWNER-FEEDBACK-2026-10-17.md; use in all future sessions"
metadata:
  node_type: memory
  type: feedback
  originSessionId: cc0bf1af-4c1f-4097-81a5-97ba84470f41
  modified: 2026-10-16T19:04:32.699Z
---

On 17 Oct 2026 the owner gave long feedback and asked that it be "read very carefully... context for all the future chats". The full words and the F1-F16 ledger are in `mockmob-next/docs/brain/OWNER-FEEDBACK-2026-10-17.md`; read that file before any UI work.

The rules in short:
- **App bottom nav (F1, F2):** his old rule was 4 to 6 slots. The current 6-slot bar is "not aligned properly at all", and fewer may be better. Where Colleges lives is unsolved ("not good"). Research how popular apps build their nav, then decide.
- **Liquid glass (F3):** he loves Apple's Liquid Glass and how it interacts. Carry that taste into the app UI (not Android system UI), and use bounce where the app owns scrolling.
- **Website Start menu (F4-F8, F12):**
  - The mode rows must feel like pressable buttons, not info cards.
  - Subject logos bigger, and the card's subject name follows the selected subject.
  - Stronger blur on unselected subject chips.
  - Fine-tune sits above "Start quick practice", with a better UI and searchable, grouped chapters.
  - The Start button's scroll state (it turns white and a "15 questions, 15 minutes" pop-up flips) is a bug to fix.
- **Fine-tune scope (F9):** quick practice only. Full mock gets difficulty only. NTA and Smart practice get none ("we weigh it ourselves").
- **Runner (F10):** picking an option must not show a second box animating out of the first.
- **Result screen (F11):** too cluttered and confusing even for him. Remove the sleeping Mobi. Repair's value is unclear. The SWOT, analysis and repair stack is too much. A student must see what happened and the one next thing. Check it held is fine.
- **Today (F14):** "never really liked: very cluttered, very confusing".
- **Learn and Review (F15):** need refinement.
- **Dock and Start placement (F13):** looks weird, and his earlier feedback was not applied.

**Why:** he judges in use, he has repeated nav and dock feedback for days, and he said "act with it as the CTO. Define it."

**How to apply:** treat F1-F16 as the acceptance list next to APP-OWNER-LEDGER-2026-10-16.md. Never simplify by cutting features ([[web-restructure-rejected]]). Prove fixes on the emulator ([[device-truth-testing]]) or with the web visual gate ([[features-over-retesting]]).

**Decisions later on 17 Oct (about 1:45 am):**
- **Mob D-S1:** open to everyone, final. He accepts the legal risk: no age gating and no consent flow for the Mob.
- **Mob D-S2:** neither all free nor Pro-only. Free and Pro must differ clearly, with a hook to try it once (not a trial). Decided split:
  - Free: weekly paper, ring and a teaser line.
  - Pro: the full side-by-side, history, extra papers, 3 Mobs.
  - The first Mob week shows the side-by-side once, free.
  - Details are in SOCIAL-SPEC section 15.
- **His Mob bar:** "10/10 only if execution is 10/10". A 5/10 execution makes it a 0/10 idea.
- **AI cost rule:** each paid user's API cost must stay at Rs 5-10. A per-user monthly cap in the guard is being built (docs/brain/AI-COST-PER-USER-2026-10-17.md). Still open: whether credits are 50 a month or 50 in total.
- **His time:** after 1-2 hours of answering, he expects substantial progress on every front of the app and website.
- **AI cap (2:15 am):** Rs 5 a month per paid user (50 credits a month), Rs 1 per free user. Only gpt-6-luna and claude-haiku-5-5 may be used anywhere. New questions must follow every wave 1-2 validation step (rubric, blind solve, review verdict, two-judge scores, fit scores, difficulty mix) before publish.
- **Global AI ceiling removed (3:10 am):** student_ai monthly_cap_usd set to 1000000 on production; per-student caps (Rs 5 paid, Rs 1 free) stay. **Nav:** A1 chosen (option A with a lime-filled Start key); refine the active-tab lens bubble, which looks weird where it overlaps. Never lose the Practice cards' blue light and texture. **Publish rule:** questions scored 8+ by the full wave 1-2 process get published; well-scored 5-7 ones may be kept for practice only. Hindi is a quality worry: extra validation needed.
- **Funding and plan (3:20 am):** the owner has a Claude startup grant: this Team plan plus USD 1,000 in Anthropic API credits that expire in the first week of April 2027; possibly USD 500 a month more across his 5 team accounts. Student traffic starts in May.
  - He set the billing alerts himself.
  - He will add the Anthropic API key soon. Then **switch all runtime AI to Anthropic (Haiku 5.5) until the credits run out.**
  - He is weighing whether to stop the paid-API question pipeline and author questions with subscription agents instead (he finds agent-written questions good). Undecided.
- **Hindi:** he is not fluent and cannot review it; he may ask someone. Hindi stays unpublished until a fluent human checks a sample.

**3:30 am, after watching the v12 walk on the emulator:** "it's just very bad right now. The homepage UI looks weird, the navbar changes, and many other things that I wanted to be implemented are not implemented." v12 (f5d848bf) predates every 17 Oct design. Decision (main session): v12 walk and release cancelled; v13 (NAV A1, GLASS, RESULT, TODAY, START, F17, Mob split, UX pass) is built straight away and is the only next APK. **How to apply:** never spend walks or releases on a build that lacks his newest decisions; when he may watch the emulator, show the newest build only.

**About 11 pm, after reviewing the live website on desktop (full words: docs/brain/OWNER-FEEDBACK-2026-10-17-NIGHT.md, N1-N19):**
- The Result and Review redesign is "not acceptable at all": it removed the mascot and the full screen of information that was "the good stuff". Restore the old richness, keeping only the clarity additions.
- Today is still confusing. The calendar/road strip and the mock slider must go, on web and app.
- Blur on the Practice chips is too strong now.
- Segmented-control animation is clunky (one box arrives before the other).
- Also: NTA bottom bar overflows on CS/IP and the timer is flaky; the Ask Mobi orb looks old; the guide needs to be more intuitive; check the CUET 2027 maximum subject count.
- He loves the Start session sheet.
