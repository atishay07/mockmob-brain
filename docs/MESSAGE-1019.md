# Release 11 and app v15.3: what changed for every point you raised (19 Oct)

**Website release 11 is live** on www.mockmob.in since 1:44 pm (main a0eb6abe, then the hero previews at 37935066). Two verifier rounds and a browser walk were done before the push, with no runtime errors since. **App v15.3** was walked on the emulator (a brand-new account, then a heavy one). Build 8 (818f594b) has been on your phone since 2:45 pm. Build 9 (4472b373) adds the walk's fixes and goes on the next time you connect.

## Your picks, as built
- **Web navigation A:** the same five places as the app: Today, Practice, Start, Mob, You. Mobi's door sits at the foot of the sidebar. (You leaned towards B's clarity too; we can revisit it.)
- **Ask Mobi B:** its own screen with two big doors, **Ask now** and **Ask your record**, in the app and at www.mockmob.in/mentor.
- **Homepage motion C:** you said it was good but slow, so I made it faster and also brought back last year's melt (April's "Rank up with the mob. / best. / top 1%.") as a second preview. You chose the faster typing version, and **it is live for everyone** on www.mockmob.in: the first change comes 1.6 s after the page appears, then a new line every 2.3 s, looping. It pauses while you scroll; phones set to reduce motion show "No more guessing." The melt stays at ?hero=v3 if you ever want to compare.

## The free first full mock (my decision as CTO)
**Every student's first full mock in each subject is free** (one per subject, ever; a started one counts). Without it, a free student (about 90 credits, with a full mock costing 50) could never finish "I don't know my range", which needs one full mock per subject. It costs no AI money (the questions come from the bank). You can turn it off with one setting (FIRST_FULL_MOCK_ENABLED=false), and every "free" line disappears with it.

## Every point, what changed, and where to look
**App, first open and onboarding**
- **G1** The first-open lines are full sentences now: "Find the marks you are losing. Win them back before CUET." Look: the first screen after install.
- **G2** Kept as it was.
- **G3** College search keeps the keyboard up while you type; "hans" finds Hansraj on the emulator. Please confirm on your phone.
- **G4** Courses lead with what commerce students target most: B.Com (Hons), BA (Hons) Economics, B.Com, BMS, BBA (FIA), then BA (Hons) Business Economics.
- **G5** One target course for now; change it any time in You > Plan.
- **G6** Colleges are ordered by last year's real closing marks for your course and category, with the number shown. For B.Com (Hons), unreserved, the 2026 data puts **LSR (912.5) above Hansraj (907.5)**, so that is the order you will see. For BA (Hons) Economics, OBC, Hansraj (712.8) is above LSR (707.8): the order follows the category.
- **G7** Today shows "Your top 3 of N" plus "See all N". Colleges 4 and 5 were never lost; You only displayed 3 (now up to 8).
- **G9** The course's rule ("B.Com (Hons) needs a language, usually English, plus 3 subjects...") shows before the first pick, with the common sets as one-tap chips.

**App, shell and Today**
- **G10, G14** Kept: the bigger bar, its animation and Today.
- **G11** The Today pill is an even stadium at every text size.
- **G12** A new account gets at least 4 real cards (a quick 10 in your weakest subject, a full mock, English, the Mob, and another subject when there is room). The broken lines are rewritten, and the odd clock animation is gone.
- **G13** The accept animation is one spring now (lift, travel, settle). The walk caught it also scrolling the page under the card; in build 9 the page holds still while the card moves.

**App, Practice, Mob, results, Your papers, Ask Mobi**
- **G15** Practice lists every mode again: Quick practice, Smart practice, Full mock and NTA mode. The Pro ones show a quiet Pro tag and a calm sheet ("Pro is coming to the app soon"), no price, no web link. The walk caught NTA mode losing its Pro tag after a subject change on the Start sheet; fixed in build 9.
- **G16** A brand-new account was walked end to end on the emulator against a release 11 staging site; the gaps it found are fixed (starter cards, the free first full mock, no dead ends).
- **G17** The bar is **Today, Practice, Start, Mob, You**. The Mob has its own tab with "Start a Mob / Join with a code". The walk caught the keyboard covering "Join with a code"; in build 9 the sheet rises above the keyboard.
- **G18** "Type your own range" accepts 900-920, "900 to 920" and reversed ranges, and refuses a gap over 200 in plain words. Every screen, Compass included, uses the same two words: **safe** (the low end clears it) and **in reach** (only the high end does).
- **G19** "I don't know my range yet": sit one full mock in each subject (progress shown per subject, and the first one in each is free), then you get an estimated range with its spread and the colleges it reaches. The estimate itself could not be run end to end on the emulator: the staging database stopped answering at about 1:45 pm. Unit tests cover it, and I will walk it once staging is back.
- **G20** Review is now **Practice > Your papers**: a stats strip, a subject filter, papers newest first (a tap opens that paper), then Mistakes to repair by chapter.
- **G21** Ask Mobi B, as above.
- **G22** The moment after Submit is back: the finish animation from before, a completion line, the marks counting up, one next move and "See this paper". Walked on a 10-question paper: the finish moment matches the approved timing. On a full mock, the result did not load on the slow staging site and "Try again" did not retry; the retry is fixed in build 9, and the full-mock reveal still needs one walk on a device. The practice result's "Repair Q9" key from v15.2 is back (build 9).
- **G23** Every screen got the "what does a first-time 17-year-old think this wants?" check; the lines are in tmp/walk-1019/APP-ACCEPTANCE-V153.md.

**Website**
- **G24** Navigation A (above). Every old address still works.
- **G25** Your papers has the stats strip back on top, then papers newest first, then mistakes. Look: Practice > Your papers.
- **G26** The Practice ticket leads with the mode, and the Start key says what it does ("Start 10 questions in Accountancy").
- **G27** The subject row in Start shows a cut-off chip, nudges once and has a chevron, so it is clear it scrolls.
- **G28** The gradients and textures are back where they were: the NTA mode button-card, the volt keycap keys, card edge lights, and the washes on Today, Colleges, the result and Features. No page-wide glow.
- **G29** Sign out is on the first screen of Account, in the top bar and in the You sheet, with one confirm ("Stay signed in" is the safe default).
- **G30** The homepage motion: the two previews above.
- **G31** One motion file is shared by the app and the web again: the count-up takes 720 ms and the springs are calmer.

**G32, G33 (how we work):** every change now follows eight rules: a fresh account first, the 17-year-old check on every screen, never hiding a feature to fix it, a side-by-side with the previous release, motion checked frame by frame, copy in your voice, one owner per surface, and mock-ups first. Two independent verifiers checked the website before the push; the second one blocked it once (a badge that broke the sidebar and a "Free" Ask Mobi question that could be charged 1 credit), and both were fixed before it went live.

## The Autopilot usage spike you asked about (D118)
Autopilot's "Continue a session" copied the whole night's conversation (600-800k tokens) and re-read it on every step: 138 steps in 40 minutes, about 100 million cached tokens, plus 88 million from its 5 helpers. It did merge real work, but a fresh session does the same for a fraction of the cost, which is how today ran.

## What is left
1. **Build 9 on your phone** (the walk's fixes): under a minute, the next time you connect it.
2. **One more device walk,** once the staging database answers again (it has refused connections since about 1:45 pm while Supabase reports it healthy): build 9's fixed screens, a full mock's reveal, and the range estimate end to end.
3. **Ask Mobi's credits footer** takes about a fifth of a small phone's screen. It does not hide anything, but a slimmer footer is a layout change, so it gets a mock-up first.
4. **Known small items** (in STATUS): a Free-mock race that only exists if durable sessions are switched on (they are off in production), and two lit cards back to back at the foot of Colleges.
5. **Older, waiting on you:** the Razorpay test-card run, then WALLET_COMMERCE_OPEN; the Play Console setup, then PLAY_BILLING_ENABLED; the PERSISTENT_LIMITS_ENABLED decision; a staging RESEND_API_KEY (staging sign-in mail).

## Things needed from you right now
1. **Your phone:** connect it (USB debugging on) whenever it suits you, and I install build 9.
2. **When you have a minute:** confirm G3 (college search) on your phone; on Ask Mobi, keep or drop the small line "An AI service writes Mobi's replies" under the Ask now box (one checker thought it reads like a disclaimer); and delete the 5 GB of old agent scratch folders listed in NOW.md (C: is at about 93 GB free, under your 100 GB rule).
