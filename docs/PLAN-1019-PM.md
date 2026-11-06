# PLAN 19 Oct PM: the owner's 3:05 pm feedback (H1-H12, verbatim in OWNER-FEEDBACK-2026-10-19.md)

Rules R1-R8 (PLAN-1019 section 0) bind every piece. Base: app `ui/v15.3-1019` at 4472b373 (build 9, wt-v15-3); web main 4af47969 (wt-rel11). H3 is resolved (an old account's real data). H5: the bottom bar is perfect, do not touch it. H10 is fixed in build 9.

## Order (his words: "First of all, I want to focus on that billing part")
1. **A. Play billing live for testing (H2)**: starts now; most steps are his, in Play Console.
2. **B. The Mob, 10/10 (H11)**: his main point; mock-ups first (R8), Opus for taste.
3. **C. Practice, Colleges and the daily goal (H1, H4, H6-H9).**
A, B and C touch different files and can run in parallel, each in a fresh session.

## A. Google Play billing, so he can see the whole flow (H2)
**Already built:** server routes `/api/billing/play/verify` and `/rtdn` (release 10, behind PLAY_BILLING_ENABLED, 404 when off), migration `20261018190000_play_purchases` (staging dry-run done, NOT on production), the app purchase flow (`flutter_app/lib/features/billing`, behind `--dart-define PLAY_BILLING=true`), the product map (`docs/brain/PLAY-BILLING-PLAN-1018.md`: `pro_cuet_2027` Rs 150; `credits_10_50`, `credits_29_150`, `credits_49_300` proposed Rs 15/45/75).
**His steps (Play Console and Google Cloud; agents never sign in as him):** payments profile; 15% fee tier; create the 4 in-app products with those exact ids; a Google Cloud service account with the Play Android Developer API and a JSON key, invited in Play Console; Pub/Sub topic + push subscription for RTDN; licence testers (his test Google accounts); upload build 9+ with billing ON to the Internal testing track. He also creates the **upload keystore** (one `keytool` command we give him, kept by him) or tells us to generate it and where to store it.
**Our steps:** (1) a one-page checklist for him with exact clicks and values; (2) the production migration under his standing grant (save, dry-run on staging when it answers, undo file, STATUS); (3) Vercel env vars are his (secrets): GOOGLE_PLAY_SERVICE_ACCOUNT_JSON, PLAY_RTDN_TOKEN (we generate the random token for him), then PLAY_BILLING_ENABLED=true; (4) a signed AAB of v15.3 with `PLAY_BILLING=true` and versionCode 10 (`tool/build_release_aab.sh`), plus a sideloadable APK for his phone; (5) walk the full flow with his licence tester: buy Pro, buy a pack, see Pro modes unlock, credits land, refund via Play Console revokes. **Done when:** he has bought Pro and a credit pack as a licence tester and seen Pro modes and the balance change in the app.
Open for him: web Razorpay (WALLET_COMMERCE_OPEN) stays separate unless he says to open it too.

## B. The Mob, a 10/10 social game (H11)
**His bar:** "an absolute 10/10", Duolingo-level clarity and delight (he started German today and is hooked), "extremely easy to use, fun", "think more than this". The rest of the app stays calm enough for serious students; the Mob is where we go all out.
**Must have:** a Mob of 2 to 5 friends; preset avatar characters (a set of about 20 to 24 original characters in Mobi's family, chosen in the profile, no photos); flexible Mob play beyond the weekly paper (a 5-question sprint, a 5- or 10-minute race, a custom length, a full mock together); join with a code that is effortless (fixed keyboard in build 9).
**Think beyond (proposals for the mock-ups, to be judged against the research brain's anti-slop test, not shipped blindly):** a Mob home that reads like a game lobby (everyone's avatar, who has played today, the Mob's shared streak); Mob quests (a weekly shared target: "Together: 200 questions this week"); head-to-head rematches; reactions after a paper (preset stickers, no free text for minors); a Mob league table that resets weekly with promotion; celebrations with Mobi and the avatars (frame-checked, R5); nudges to a friend who has not played ("Riya is waiting for you"), with a calm daily cap; every number true (no fake activity).
**Process:** R8 mock-ups first: 2-3 directions (lobby, sprint flow, results with avatars, avatar picker) at 360 dp, Night and Day, as images and a short motion study, for him to pick. Opus for design and copy, Sonnet to build after his pick. Web Mob follows the app's pick.

## C. Practice, Colleges and the daily goal (H1, H4, H6-H9)
- **H6:** Practice puts "Ways to practise" (the modes) at the top, above the next-chapter card.
- **H7:** Your papers and Learn get a proper, visible place in Practice (not a row that looks extra): mock-up the Practice page order first (R8): modes, then Your papers, then Learn, then the next chapter.
- **H8:** "Questions in stream" (find the exact label): rename it in plain words or remove the jargon (R6), with what it means.
- **H9:** Colleges: a clear, permanent way in (his words: "really important"). Options for the mock-up: a Colleges card at the top of You, a "Your colleges" row on Today that opens the full list, and Admission Compass from there. Never hide it behind "Aim".
- **H1:** the daily goal step (onboarding 6 of 7) keeps 10/20/30 min and adds a tasteful "More" path: 1 hour (a full mock a day), 2 hours (two mocks), or a custom amount, with no cap. The smart layer learns the student's real pattern (session lengths, time of day, modes chosen, skipped cards) and adjusts the deck and the goal suggestion, saying why ("You usually practise 40 minutes after 9 pm, so..."). Every claim must be true from data.
- **H4:** the clock animation on the full-mock card (two hands): confirm with him whether it stays; G12 asked to remove the odd clock animation.
**Done when:** walked on the emulator on a fresh and a heavy account, R2 lines, R4 against build 9, then on his phone.

## His answers (19 Oct 3:25 pm, D121)
1. Play prices confirmed: Pro Rs 150; packs Rs 15 / 45 / 75. Razorpay on the web is not part of this ask.
2. Upload key: he did not know the term (explained). Offer to generate it, tell him exactly where it is saved and that he must back it up.
3. He buys as the licence tester from his own Google account: ask him for that email.
4. H4: KEEP the clock animation on the full-mock card; just fix it (find what looks wrong and make it calm and correct).
5. H8 is dropped: "Questions in stream" was a dictation garble.
6. Avatars and the Mob: full creative freedom with our taste; make it unique and interesting.
