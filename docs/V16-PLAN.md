# Version 16 plan (20 Oct 2026, 11:55 pm, session b7e1b5da on Fable 5.1)

Goal (D191): app 1.0.18+16, the final closed-testing build, signed in Desktop\MockMob-build-16, plus the phone-first website pass, both deployed and checked, in one pass tonight. Owner rules: D180 quality first; D185 Get Pro, no text bombardment; D186 no regressions; D188 model per task; D192 Fable plans and orchestrates, Opus only for taste and motion.

## What I verified in the code before planning
- A1: nothing shows after sign-up except the `/before-you-start` sheet (age, usage data, "Have a friend's code?" row, first move). No welcome-credits pop-up exists. ReferralCopy (features/referrals/referral_copy.dart) is the "boring" copy.
- A2: the Wallet invite section draws only when GET /api/referrals answers live:true; the "Have a friend's code?" row hides only when the student already joined with an invite. The server refuses a code for an account that has practised (`existing_account`). A pending deletion is invisible after sign-in: /api/me carries no deletion field.
- A3: the explainer is wired to Start a Mob, Join with a code, an invite link and "See how it works" only (mob_v3_nav.dart startMob/joinMob/howItWorks). Nothing plays on the first Mob tab visit. The Mob tab root for a student in no Mob is DenStartScreen (den_start_screen.dart).
- A4: the pro_nudge system covers only the first-session Pro sheet (D181) and inline Pro rows. No general nudges exist.
- A5: MOB_LIVE_ENABLED is not set on Vercel. App (mob_room_channel.dart) and web (components/mob/v3/live/liveChannel.js) both join PRIVATE channels, so turning "Allow public access to channels" off is safe for live rooms.
- A6: "lost"/"last" live mostly in features/insights (ask doors, suggestions, readout), Today's lead copy and the result read.
- W1/W2/W8: the web sells the one-time ₹99 access because `RAZORPAY_PLAN_ID_PRO_MONTHLY_99` is not set; `publicOffer()` flips to monthly the moment it is. The 19 Oct decision (D135/D136) keeps the website at ₹99 a month (Play ₹149).
- W4: web onboarding already starts on the subjects step; no preset or big accept key.
- W5: the scroll statement ("Your lost marks went somewhere...") is a held scroll story on phones only at min-height 780 px; words and objects are small.
- W6: Mistake Lab's Time step reveals are driven by a clock that stops at the step's end and never restarts; in held mode `if (pinned) return` freezes it.
- W7: tour screens (.ts) sit on a near-black gradient with a faint border; in dark mode they merge with the page.

## Waves
Wave 1 (now, 7 agents, one writer per worktree):
- A3 Mob first visit: welcome animation + explainer autoplay (Opus) in wt-1020-v16-mobwelcome.
- A1 welcome-credits pop-up + warmer invite copy (Opus) in wt-1020-v16-welcome.
- A2 + A6 invite correctness, deletion clarity, copy sweep, studying chip (Sonnet) in wt-1020-v16-sweep.
- W1/W2 pricing revamp like the app Pro page (Opus) in wt-1020-web16-pricing.
- W3 phone hero like the app welcome (Opus) in wt-1020-web16-hero.
- W5/W6/W7 statement, Mistake Lab timer, tour screen surfaces (Sonnet) in wt-1020-web16-landing.
- W4 subjects first with Commerce preselected (Sonnet) in wt-1020-web16-onboard.
Wave 2: A4 nudges (rules by Fable, card by Opus), A5 live (owner's Realtime switch, then MOB_LIVE_ENABLED), /api/me deletion field, web referral copy sync, W8 Razorpay guidance.
Wave 3: integrate app branches into ui/1020-v16, analyze + full suite, demo walks Night and Day, signed 1.0.18+16; integrate web branches, suites, build, deploy, smoke.

## A4 nudges: design (built in wave 2)
One surface: a "Mobi note" card near the top of Today (under the greeting), plus at most ONE sheet per app run for the two moments that deserve it (a friend joined or paid out; a Mob game waiting). Rules: at most one nudge per run; never during onboarding, a run, a result or over a sheet; never on the first session (D181 covers money); each nudge dismissible with X; a dismissed nudge stays quiet 7 days (InlineRules.quietFor); celebrations once per event id; money nudges obey D181.
| Key | When (all true) | Card line | Key |
|---|---|---|---|
| practice_today | after 6 pm, a daily goal exists, no practice today | "Ten minutes keeps today on your chain." | Practise 10 |
| repair_open | 1+ open repairs, none started in 2 days | "{n} marks are waiting to be fixed." | Fix them |
| mob_game | den Now card step 4 (a friend's game open), not played | "{Name} opened a {sprint}. Race it before {time}." | Open the Mob |
| credits_low | Free, credits <= 10, invites live | "{n} credits left. A friend brings 100 more." | Invite a friend |
| friend_joined | referral status: a friend joined, not yet practised | "{A friend} joined with your link. Their first practice pays you both 100." | See invites |
| friend_paid | referral status: rewarded since last seen | "100 credits landed. Your friend practised." (celebration) | Nice |
| chain_risk | chain alive, nothing today, after 8 pm | "Your {n}-day chain ends at midnight. One set keeps it." | Keep it |
| good_result | result >= 80% or a best, invites live, no money nudge shown today | "Good run. Race a friend next: you both get 100 credits." | Invite |
