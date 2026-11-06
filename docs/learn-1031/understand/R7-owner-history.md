# R7 Owner history: everything the owner has said or decided about Learn, Key cards, Revise, Explore, the swipe stack, next-move UI, session choosers, navigation and the Start sheet

Written 31 Oct 2026 by a read-only subagent. Nothing was changed, built, committed or run. The text below quotes the owner exactly as the brain files record it (dictated, so some words are transcription guesses). Where a file records only a paraphrase, it says so.

## 0. How to read this

**Status tags**
- **BINDING**: his newest word on that point, or an earlier word nothing newer overrides.
- **SUPERSEDED**: a newer word of his replaced it (the newer one is named).
- **CONTEXT**: background or a precedent, not an instruction for Learn.
- **PLAN-TEXT (not his)**: written by an agent. It never counts as his word, and it is listed only where it conflicts with something he said.

**Rule used for conflicts:** the newest owner word wins, then his rejections and praise, then his research brain, then agent plans (OWNER-TASTE-PROFILE section 0, ledger "Sources").

**File abbreviations** (all under `C:/Users/atish/Desktop/mockmob copy/mockmob-next/docs/`)
- `LEARN` = brain/OWNER-FEEDBACK-2026-10-31-LEARN.md
- `LEDGER` = brain/OWNER-MASTER-LEDGER.md
- `DAWN` = brain/OWNER-FEEDBACK-2026-10-18-DAWN.md
- `F1019` = brain/OWNER-FEEDBACK-2026-10-19.md (it covers 19 to 21 Oct)
- `F17`, `F17N` = brain/OWNER-FEEDBACK-2026-10-17.md and ...-17-NIGHT.md
- `TASTE` = brain/OWNER-TASTE-PROFILE.md
- `PLAN` = brain/INTELLIGENCE-LAYER-PLAN-2026-10-31.md
- `BSPEC` = brain/intel-1031/KEYCARDS-BUILD-SPEC.md
- `UXS` = C:/Users/atish/Desktop/AI OS/wiki/concepts/ui-ux-standards.md
- `DD` = design-decisions/

---

## 1. The ten things to know first

1. **On 31 Oct, about 5:20 pm, he used Key cards live for the first time and said the Learn area as a whole is "far from what we are looking to do".** The only part he praised is Study mode ("exactly what we wanted"). Everything else (entry, Learn shell, Read mode, Last look, next-action card, the "Must know" label) he found small, confusing or weird (LEARN, LK1-LK14).
2. **He has never before given a verdict on the Learn area, the Concepts lessons or Revise.** His earlier Learn words are only three: 17 Oct "I'm not even going to look at" it (F15), 18 Oct "Learn ... needs refinement" and "no clear Learn tab" (D20), and 19 Oct "Your paper and learn section should not be hidden ... It seems like something extra" (H7). There is no recorded owner sign-off of the 17 Oct Learn design (DD/pass-1017/LEARN-REVIEW-1017.md says "owner sign-off pending").
3. **He gave a flow for Learn (LK10):** pick a subject, pick the concept or chapter, see what is lined up, pick a time, get a mix of cards and questions. Plus a separate place that shows what is where and lets the student revise chosen cards.
4. **He wants student control, not weakness-led steering (LK9), and a next action that is "dynamic" with options, not one fixed suggestion (LK11).** His own approved precedent for "one lead plus alternatives" is the swipe stack (D51, D90, D94) and the Today lead card with "Something else".
5. **Cards are "the core area" of Learn, and they should also feed Explore as a custom chapter feed (a 10-minute run of practice cards and MCQs) (LK12).**
6. **The bottom bar is a KEEP.** 19 Oct: "the bottom navbar is just awesome ... so it's perfect" (H5). The app bar is Today, Practice, Start, Mob, You (D105). He never asked for a Learn tab in it. LK1 says only that the way to Key cards is "badly placed and very small". A dock change is therefore a decision to put to him, not to assume.
7. **He has repeatedly rejected rebuilding screens he approved, and cutting richness to simplify (three times: 15 Oct web, 17 Oct result, 18 Oct Today).** Any replacement layout goes to him as a mock-up, in real renders, before it ships (Never again 1; memory real-renders-not-sketches, 23 Oct). On 31 Oct he has asked for new Learn structure himself (LK10), so the Learn shell is open to redesign. What he praised must stay.
8. **No walls of text.** 20 Oct (D185): "there should not be too much bombardment with text, like this text, big text, small text, bold text, and text inside a card." LK11 repeats it for Learn.
9. **The audience is 16 and 17-year-olds, many new to apps and to CBT (G23, 19 Oct).** If he finds a screen confusing, students will. Every control must explain itself the first time.
10. **"Must know" is on about two thirds of cards.** Counted from `wt-1031-keycards-web/data/keycards/decks/*.json`: 3,916 of 5,800 published cards (67.5%) carry `importance: "must"`, and no card has an `asked` value. That matches his complaint. See section 8.

---

## 2. His words about Learn and Key cards, newest first

### 2.1 31 Oct 2026, about 5:20 pm IST: live review of Key cards and Learn (LEARN) , BINDING (all of it)

He checked Key cards himself on www.mockmob.in after the flag went on at 1:35 pm. Verbatim, in full:

> Some parts are good and some are very confusing.
>
> * The journey to reach the keycard section is itself not very well placed and very small.
> * Just like in accountancy, when I select your part, it glitches sometimes and shuffles it. It's a bit buggy.
> * The interface regarding all of the things that you have built in the Learn section is itself not very good or easy to use.
> * Once we even get into a specific card or chapter (or whatever this is, like Accounting Partnership, Accounting Partnership Basic Concepts), in the Read section it's a very weird layout.
> * The Study section is the only part I like. It's exactly what we wanted but that also should maybe have some animation or something. When I press Got It and when there is that Print That Chapter Sheet, it's maybe a good idea but it should have our watermark all over the place so that no one can copy it. This is not watermark content but still we are Fitzmeen downloading.
> * This last Look, I really didn't understand. What's the difference between this and the Read section? It's a bit confusing.
> * All this should be integrated better, more tastefully, and more in the flow.
> * This overall Learn section needs easier self-control rather than just being based on focusing upon the weaknesses and all. If someone is trying to figure out things there, it's very confusing.
> * The Learn section should be according to this flow I am giving you as an example: someone comes in, they select a subject, they select the concept that they have to practice, and then there are many things lined up there. They select the time for which they want to practice and there are some combinations of cards and questions lined up for them. There is also a separate section that easily shows them what exactly to find where or, if they want to, separately revise something, some specific cards, and something else.
> * All of this, you have to think about how to integrate everything properly and make a good UI/UX. There should not be just lines and lines of text and stuff like that everywhere, an overload of information with no clear next action. Even the next clear action that you have is not dynamic. It's just one thing that it is showing, with no more options.
> * This is not a poor requirement but still this is far from what we are looking to do. These cards and everything are the core area for the Learn thing, the entire Learn area, so it should be better, as I said. Then you can integrate it in the Explore section also, maybe creating a customized feed for practicing a chapter, like starting a 10-minute lesson. It just shows randomly some practice cards, MCQ stuff like that, so everything has to be thoughtful. You have to think it through, which you are not doing right now.
>
> Pick up this direction and start working on this and making better progress. Honestly, I have not seen the quality of the overall cards. They seem decent to me, but everything just has a "must know" mark to it, which makes it kind of weird. Okay, not everything has it, but multiple things have it. These can be changed or something. For many of these things, you have to spend longer time thinking these through. And I'm giving you the basic direction, so ideate better on all of this.

**Transcription guesses recorded in LEARN (confirm with him):** "Fitzmeen downloading" probably means "preventing downloading", or "we are fine with them downloading, but it must carry our mark". "Accounting Partnership Basic Concepts" is the chapter "Accounting for Partnership: Basic Concepts".

**Reading notes for the designer (from the text itself, not invented):**
- "Your part" in the second bullet is the option picker for subjects with optional parts (Accountancy has AFS or CAS). The picker is `Option picker (one tap) for Mathematics, Computer Science and Accountancy` in BSPEC section 3. LK2 says the options reorder or "shuffle" on selection.
- "Read", "Study" and "Last look" are the three modes of the chapter deck (BSPEC section 3: "Three modes in one segmented control").
- "Print that chapter sheet" is the Pro button "Print chapter sheet" (BSPEC section 3). His reaction is to keep it and watermark it.
- "The next clear action ... is not dynamic. It's just one thing" refers to the single "Revise now" or lead action. The words "with no more options" are what he wants fixed.
- He calls the cards "decent". The complaint about "must know" is about the label, not the card text.

The LEDGER section "Learn and Key cards, 31 Oct evening" (lines 601-616) holds the same items as LK1-LK14 (all OPEN). LK14 reads: "Think longer; ideate better. Any replacement layout is shown to him as real renders before it ships (Never again 1)."

### 2.2 31 Oct 2026, earlier the same day (D200-D207), BINDING

Source: LEDGER lines 574-599, from his dictated words; INTELLIGENCE plan section 8.

- **Priority, dictated:** "The main thing that I really care about and focus upon is the card and the feature that we have to build. Other things, you can see yourself and improvise all of that."
- **About 10:40 am:** "Good going I'll do all the things you said soon but for now keep going keep building and perfecting more and more things and if you feel like everything is done then lmk". CONTEXT.
- **D200 Syllabus:** one reference, the real CUET syllabus (units), with NCERT chapters as the study unit and a clear unit for each. Build in every CUET intricacy (options between units, sections such as Maths core and Applied, CS and IP, optional parts). His goal: "the most precise and focused approach towards what is actually coming in the syllabus and what will be asked in the exam."
- **D201** No "Older syllabus" shelf unless it clearly reduces confusion (he expects it adds confusion). Off-syllabus chapters leave every student surface. **D207 (4:40 pm: "Pull them all")**: all 218 outside-syllabus questions leave every pool. LEDGER lines 596-599.
- **D202 Cards keep NCERT's exact language, with the reference (book, chapter, page).** "That language is what fetches them marks." Paraphrase only for explanations. This **supersedes the plan's own pick** (PLAN section 8 question 2: "quote at most one short NCERT line ... everything else is paraphrased"; PLAN-TEXT, not his).
- **D203** Card categories: the proposed types are good; add and label more as needed. Both halves must be done: the backend with every needed card and question type, and a "good-looking, well-integrated frontend".
- **D204** Pilot: at least the 5 to 6 most popular subjects. (Six are built: Accountancy, Business Studies, Economics, Biology, Political Science, English.)
- **D205** The USD 50 content ceiling "has been long exceeded and is no longer valid": removed.
- **D206 Free vs Pro:** Free is a taste ("have a feel for everything, and make people believe that it's useful, but not exactly provide them with actual value"). The real value of cards and the intelligence layer is Pro. This **supersedes the plan's default** that cards and Fix it are free (PLAN section 6; PLAN-TEXT).
- **1:20 pm and 1:35 pm:** "Yes, run them" (production steps) and "Turn it on" (the flag). CONTEXT.

### 2.3 20 Oct 2026 (F1019 lines 773-1031), mostly BINDING as principles

| Time | His words (exact) | Status |
|---|---|---|
| 6:51 pm | "In any screen, as I have mentioned many times previously, there should not be too much bombardment with text, like this text, big text, small text, bold text, and text inside a card. So just fully text-based so that should not be the case. There should be good UI/UX everywhere. Not like this." (D185) Also: "the screen and all four screens for four different things that you have built look very basic. Try to make them better and more aligned with the app." | BINDING. This is the rule behind LK11. |
| 6:57 pm | "All looks good, and don't make any regressive changes anywhere. Make sure that if you lack clarity on anything, call the continuum and check the previous context." (D186) | BINDING |
| 2:51 pm | "The decision to build the minimal version of mob, reducing the number of screens and fitting everything in a scroll, is also not a very good direction. ... By a clean UI, I just meant that things should not be hard to find or be overwhelming. If the screens are the same, whether they are just a single scroll with too much information or a single scroll, that is also not good. What happens on the result page is that previously too much was going on, and now too little is going on." (D173, from the Mob; it states a general principle) | BINDING as a principle: not one long scroll, not too little; a short sequence of focused screens is fine. |
| earlier, ledger D170 | "By simplicity, I didn't mean to cut too many features. ... these can just be added as a specific mode". D170 reads "CLI" as "clean UI": simplicity is clean presentation, never cutting approved features. | BINDING |
| 2:18 pm | A study-time app his class used (focus lock, tracked or logged study time, healthy competition): "This is just an example. I am not telling you to incorporate this feature." (K10) | CONTEXT only. It signals he likes simple, self-driven study tools. |
| 1:49 am | Wallet and Pro: "The screen where everything Pro unlocks is rudimentary, but the direction that you have taken could be built into something good." Ask Mobi: "Why would someone use Mobie over ChatGPT or any AI chatbot which they can use for free?" | CONTEXT (Pro value must be felt) |
| 5:45 pm | First Pro ask: "Wait for a real limit (Recommended)" (D181). No Pro ask on a first result; a dismissible sheet only at a real limit or on the second return to Today. | BINDING for Free-to-Pro prompts inside Learn |
| 3:25 pm | Free first full mock per subject: "Switch it off" (D175). | CONTEXT |

### 2.4 19 Oct 2026 (F1019 lines 1-560), BINDING unless noted

**1:15 am, after installing v15.2** (lines 3-50). Relevant words:
- Review, mobile: "The review segment is not showing exactly what we need to see, like the option to choose subjects and all." "Even the review section is very cluttered and doesn't show the recent mocks. ... There should be a clear path through the history and all."
- Audience (G23): "remember this app is for students who are literally 17 years old right now. Many of them might be new to using mobile ... If I'm finding the UI confusing and overwhelming, then for sure everything needs to be thought through. ... CBT is the first time they are attempting CBT mocks."
- Fresh account (G12, G16): a "Suggested for you" deck showed one option, English full mock. "It can show at least 3 or 4 cards before showing nothing else." The new account felt incomplete; "this is the bare minimum. Without this, we can't even put the app into testing."
- The accepted-card animation: "The animation when something gets accepted, like 'Do this next,' comes on top. Maybe, if you can, make it a bit better." (G13)
- Praise (KEEP): G2 first onboarding screen, G9 common sets and picks, G10 the bigger bar and animation, G14 the Today page ("the today page is good").
- Web: "Even in the subject selector, instead of showing the mode on top whenever I select a subject, in the practice mode, it's showing 5 questions to the pen in biology. ... I am seeing very weird UI choices." (G26) And "in the start section, you can add some kind of leading horizontal scroll or something in the subject selector so that people know that they have to horizontally scroll." (G27)
- Web IA (G24): "Your mob is placed inside Study only, and everything is inside Study, and Planning is in Marks Trends. That is also a bit weird."

**About 1:40 to 2:55 am, his choices** (lines 107-205)
- D105: the app bar becomes Today, Practice, Start, Mob, You; Review moves inside Practice as "Your papers". His pick: "Its own tab in the bar (Recommended)".
- D106: "Papers first, then mistakes (Recommended)".
- D107: web navigation: "Mock-up 2-3 options". D112: if he is away the CTO picks. **C-pick 1 (CTO, not his word): web nav A, the same five places as the app**: Today, Practice (with Your papers, Learn, Explore, Saved), Start, Mob (with Your standing), You (with Progress, Marks trend, Colleges, Wallet, Guide, Show me around). D114 lists "nav A" as LIVE from 19 Oct 1:44 pm. BINDING unless he overrides (he said "I can change it later"; nothing later changes it).

**3:05 pm, after v15.3 on a new account** (lines 237-277). His words:
> "Also, the bottom navbar is just awesome. It's amazing. It's as good as it can be. Exactly what I wanted, so it's perfect."
>
> The practice section needs not exactly a revamp, but what is important should be shown on top:
> * Ways to practice should be on top of Next Chapter or whatever you are showing on top. That's higher priority.
> * Your paper and learn section should not be hidden as it is in this UI right now. It seems like something extra. It should have some proper implementation in the UI.
> * Questions in stream: what is this? Don't understand. Admission compass: okay, looks good, but where is that college section now? I am unable to find it in the app. It's really important, and there is no clear-cut access to it or understanding how to access it.

Ledger rows: H5 "The bottom bar is perfect. KEEP." H6 "Ways to practise" goes above the next-chapter card. H7 "Your papers and Learn must not look hidden or extra; give them a proper place." H9 colleges need obvious access. Also at 3:05 pm: "I wanted you to build an experience like that [Duolingo], which has such clarity and is so amazing." (CONTEXT, Mob)

**4:15 pm, his picks** (lines 316-321): Practice: **"C: three doors"** (a Practise / Your papers / Learn switch under the title, D126). Colleges: "A + B: You card and Today strip (Recommended)". Daily goal: "A: a fourth 'More' bubble (Recommended)". "Question stream": "Rename to 'Untimed questions' (Recommended)". BINDING. Note the design doc recommended B and he chose the bolder C (DD/pass-1019pm/PRACTICE-COLLEGES-GOAL-1019PM.md line 36).

**H1 (daily goal, onboarding step 6 of 7)**: "For example if someone wants to attempt at least 1 mock per day, which is like 1 hour, or even more than that, why are we stopping them? ... it should be included tastefully. The entire smart layer around it should actually be smart, analyzing the entire patterns of the user: what they want, what they don't want. It should actually feel intelligent." And "10, 20, 30 minutes is fine, and it perfectly goes with the UI also, but tastefully." BINDING for any time chooser (see 5.3).

**11:42 pm, after installing version 11** (lines 507-560). He had installed a rival, "CUET Market", and said:
> "in that app, immediately when I went to attempt the first accountancy mock, they asked me if I want to attempt part A or part B. ... CUET has many caveats like this, which we have to go really in depth on. One of my reasons to go from 40, 50 subjects last year to just 15 this year is so that we have extreme depth and clarity, which no other platform has for CUET especially. The kind of confidence that that app ... gave me, we should be able to give the same from the first time."
> "Overall, they have a very professional, clean UI and all that."

BINDING context for LK2 (the part picker is where he expects CUET depth to show). He also wrote that gamified UI is "two-edged": casual users like it and "For the serious users, it becomes friction" (I16, CONTEXT).

### 2.5 18 Oct 2026 (DAWN), BINDING unless noted

**About 1:45 am, on R4** (lines 9-40). Learn and nav words:
- D20: "The progress thing is leading to some question, like to learn, but there is no separate learn tab in here, and learn as a whole is, I think, gone from there. Okay, no, it's there: Learn, but again, needs refinement. I don't know how much I have to nudge in everything for the website. ... most of the UI part as a whole (if I could explain it on the macro level) is fixed, but on the micro level, a lot of work is needed."
- D5: "What I'm noticing is the Repo S [Repairs?] or Mobi, everything is missing from the Practice section. The way you have placed it, no one will be able to see it ever. The placement is really bad." (This is his own wording for LK1's problem: a feature that exists but cannot be found.)
- D1-D3 Today: "Firstly today is honestly a huge regression in my opinion. ... There should be something interactive on the float [?] today and this Today section should lead and do more things not just start every 10 minutes or something else better like that." And: "Anywhere it should never look like just a basic form or filling something like a form. They should always be leading and interactive UI which leads you to the next thing."
- D13: "the bottom nav bar, like the round pulse which is around it, today it's looking fine. In practice, it's a bit weird, like text and line. These are small things which I'm mentioning, but they matter."
- D18: "We have tried so many times to fix this stuff, but no result. Maybe, rather than review, in the review section, we can integrate the weak chapters somehow, because that's actually more useful." (applies to Review, see conflict C2).
- D4 praise: "Coming on the Practice section, Subjects Loop. Perfect now. Overall the UI part and everything in the Practice is really refined and looks really good."
- Verdict on the whole: "Honestly, the mobile UI feels better".

**About 12:15 pm, on v15 on his phone** (DAWN line 192 and ledger lines 200-211), D40-D57 (app). Relevant:
- D43 "a clear cut button to go back, rather than just that small back icon on the top". Needed on every nested Learn page.
- D40/D44 layout: content too high, "almost into the notification bar and there's a lot of space in bottom".
- D46 (session length 10/20/30): "You be the judge" (CTO kept 10/20/30 plus one quiet line that full mocks exist) and D47: study days "not a clear or obvious UI choice that someone would alter it"; make it clearly interactive with a live readout.
- D50: "5, 10, 20 only. No direction until you do a full mock". The CTO read: "How many questions?" offers 5, 10, 15, 20 and a full mock.
- D51: suggested cards you swipe left and right in place of the "More ways to practice" row ("not sure, random ideas"). D52: Today richer.
- D53 "We don't want this friction... It should be instantaneous."
- D56 "feeling very basic now ... it used to feel something else and unique".

**About 12:50 pm:** "Yes, build both the richer Today (D52) and the swipe card stack (D51) as v15.1." BINDING (approved design: DD/pass-1018/TODAY-SWIPE-1018.md).

**About 7:40 pm** (DAWN lines 345-352), D90, on the swipe stack:
> "I think there were some issues with the swipe left and right thing, so you can take UI experience inspiration from apps like Tinder, not just swipe-left, swipe-right dating kind of apps. Many other apps have also integrated these kinds of things to understand user taste or adapt to this and many things, and the UI should also be like that. When a first-time user is entering, it won't know what cards actually do or what swipe left and swipe right mean, so you have to build the entire process into this."

**About 7:50 pm** (D92): taste is not only his preferences. It is "knowledge of what UI/UX taste is, through independent knowledge, the model, and so many research and records that I have added to the brain itself." BINDING (the way every critic judges).

**About 8:15 pm** (D94): "Yes, build swipe v2 as drawn: Up next / Not now with the buttons under the deck and the first-time demo." BINDING. D97: "Keep swipe v2 in the final build".

**About 11:21 am to 12:30 pm** (D59): the final v15 must include "Learn and Review beyond D18" (his list). SUPERSEDED in practice by later builds, but shows Learn was meant to be a finished part of the app.

### 2.6 17 Oct 2026 (F17, F17N)

**About 12:45 am and 1:20 am (F17)** , mostly BINDING:
- **F15 (SUPERSEDED by D20 on 18 Oct and by LK on 31 Oct):** "The learn and review section I'm not even going to look at. I know there are many things which need refinement there, so I just don't want to get disappointed right now."
- **F5, BINDING:** "I don't know why these feel like cards depicting information rather than buttons that I click and an action happens." (rows must look pressable.)
- **F8, BINDING (applies to chapter pickers):** "Chapters are cluttered, and it's difficult to find exactly what we are looking for." His ledger fix: group them and add search.
- **F6, F7:** subject logos bigger; unselected subject chips blurred, then N2: "This much blur is giving the feeling that it's logged [locked]." Use the earlier, lighter blur.
- **F9:** fine-tune is for Quick practice only; full mock: difficulty only; NTA and Smart: none ("we are weighing all this ourselves and using the intelligence ... That's what we are advertising").
- **F11:** result screen: "If I see it from the student's point of view, they won't be able to figure out anything in this UI. What is going on, and what do they have to do?"
- **F12, F13:** Start button state flicker on scroll; Start placement "looks kind of weird".
- **F18, BINDING:** "Even last year, students were confused, and they didn't use 90% of the features because they didn't actually know what they were to do with this. We have to learn this from the top edtech platforms: how they make students utilize all the features, which gives them the feeling that what they're paying for is offering them value."
- **F1:** "Right now, we are at 6, but it is not aligned properly at all. Should we have to think? In some sense, less, more also." (then A1: nav A with a separate Start key; later praised 19 Oct.)
- **F3:** "the liquid glass design and how it interacts with everything, I really love it in the Apple system." App-level only. Glass on chrome, never on content (TASTE).

**About 11 pm (F17N)**, the N list. BINDING unless noted:
- N5: segmented controls: "the first box arrives before the second box and then the second box overlaps it." Wants one indicator that slides cleanly. **Applies to the Read / Study / Last look switch.**
- N11: Start session sheet: "Really love the UI of the start session thing. Everything is super refined." Only the spacing between Quick practice and the other modes needs fixing.
- N12: result and review: "This is not acceptable at all. You have just made it more basic and removed the good stuff. ... I like the old UI better even though it was more complicated. At least it was intuitive."
- N13/N14/N16 praise: the weak chapters part, "scores by session ... very intuitive", "your answer sheet is good". N15: "Chapters by marks left open is not exactly good."
- N17: "This guide session on the bottom needs to be made more intuitive and easy when someone is figuring out they need a guide."
- N9: Ask Mobi orb looks old; "Either we stick to the mascot only, or I also really like the orb."
- N1 (Today): "this calendar type of thing needs a better UI ... very confusing and very cluttered ... when too many days are remaining, a few are focused". And the slider "is not exactly doing anything". (A lesson for any time slider in Learn: it must visibly do something.)

### 2.7 13 to 16 Oct 2026 (older, mostly CONTEXT but several still BINDING)

- **15 Oct 13:15, web restructure rejected** (memory web-restructure-rejected; HANDOFF-2026-10-15-AFTERNOON): "a huge regression", "so basic compared to what we had before". On navigation: "Cluttering each page with more information is not the solution." Practice: "previously it was such a beautiful UI". The Start sheet: "good", needs graphics, spacing and typography. **BINDING lessons:** never cut richness to simplify; regroup navigation but never merge pages into denser ones (DD/pass-1019/WEB-NAV-1019.md states this as a hard constraint).
- **15 Oct 16:30 (OWNER-VISION-2026-10-15-PM):** "This start thing that you have included, I really love it. What you have done with it is really thoughtful." "When many details together are improved and you keep on improving and improving, finally we have a product which is so refined, so finished, so good that it actually makes sense." Landing is mobile-first; the arena is desktop-first but phone-ready; the app is mobile only.
- **16 Oct about 00:45 to 01:00 (memory mockmob-design-direction):** a glow hero "really amplifies the AI slop look"; an eyebrow pill with a pulsing dot is "a pure giveaway that this is an AI-generated website". He wants real typographic hierarchy, not cards, pills and badges. BINDING (UXS section 10 is his slop list).
- **16 Oct 10:32, Practice order (APP-OWNER-LEDGER L08):** "The issue is the placement of things, like first in the top English subject, then a few modes, then subject selection, and then ... it's not exactly ideal." Subject first, then modes. BINDING.
- **14 Oct 18:30:** "less is not good. Balanced is the highest favorability. Crowded is better than less, then over-gamified at the same level as less." BINDING (the balance rule).
- **13 Oct 11:10 and the Mobi note:** Mobi should be alive like Duolingo's Duo; "no pasted AI pictures". "We wanted this to be an extension of the website, having more than it." BINDING for Mobi usage; Learn should use Mobi tastefully, one per screen (G-set L35).

---

## 3. Where Learn, Concepts, Key cards, Revise and Explore sit in the structure he approved

| Item | What he approved or said | Source | Status |
|---|---|---|---|
| App bottom bar | Today, Practice, Start, Mob, You. Review moves into Practice as "Your papers". The bar is "perfect". | D105 (19 Oct 1:40 am), H5 (3:05 pm) | BINDING |
| Learn in the app | "Practice C: three doors": a Practise / Your papers / Learn switch under the Practice title. Learn and Your papers are "in-place views". | D126 (19 Oct 4:15 pm); DD/pass-1019pm/PRACTICE-COLLEGES-GOAL-1019PM.md lines 31-36 | BINDING. Whether it shipped as drawn is for the code maps (LEDGER says built and merged in ui/v15.4-1019pm). |
| Learn on the web | Practice's own pages sit in a sideways tab row under the top bar: Practise, Your papers, Learn, Explore, Saved. "Explore" starts off-screen at 390 px as the scroll cue. | C-pick 1 under D112 (CTO), D114 live 19 Oct | BINDING by default (he never reversed it). |
| Phone web dock | Today, Practice, Start, Mob, You. The phone sheet is called "You" under option A, and it has no scroll. | WEB-NAV-1019.md lines 73-75, 165, 183 | BINDING by default |
| Learn must have "a clear place" | "there is no separate learn tab ... needs refinement" (D20); "should not be hidden ... seems like something extra" (H7) | DAWN D20; F1019 lines 248, 272 | BINDING. LEDGER lines 360 and 106 still list D20 as open: "Learn one tap on phones is a dock change". |
| Concepts (lesson library) | The app already calls it Concepts. The 17 Oct design made it "Concepts at the moment of need" (offered on a mistake, a chapter, a Practice panel, Today). No owner verdict on it exists. | DD/pass-1017/LEARN-REVIEW-1017.md sections 4.2, 5.9-5.11 | PLAN-TEXT, unverified by him. Note H7 and D126 later asked for a visible Learn door, which adds to it. |
| Revise | Only owner words: the F17 and F18 principles, and a bug note on 18 Oct 4 am ("Day 3 of your first week / Start Revise row half under the bottom bar"). No taste verdict on Revise. The Today line "Revise" is also in LK11's "Revise now" action. | DAWN lines 126-127; BSPEC section 3 | CONTEXT |
| Explore (web) | The untimed question feed (`/explore`, DiscoveryFeed). It stays after the community decision: "keep Explore, the Mob, Your standing and the creator programme". | DAWN line 121 (D21), DD/pass-1018/COMMUNITY-1018.md lines 9 and 47 | BINDING |
| Explore (app) | The Explore twin was called "Question stream"; he asked what it was; renamed "Untimed questions" (D126). | F1019 lines 248, 279-293, 321 | BINDING |
| Key cards, in the 17-25 Oct design | "No new top-level nav tab." Entry points: a "Key cards" link in the Learn hub and per chapter row, plus one Today Revise line. | BSPEC section 3 (agent spec, not his word) | PLAN-TEXT. His LK1 says this entry is "badly placed and very small". |
| Key cards, from LK12 | Also a feed inside Explore: "a customized feed for practicing a chapter, like starting a 10-minute lesson ... randomly some practice cards, MCQ stuff". | LEARN | BINDING |

---

## 4. Next-best-move, lead-card, swipe-stack and "what next" decisions

| Date | His word or choice | Status |
|---|---|---|
| 31 Oct (LK11) | "Even the next clear action that you have is not dynamic. It's just one thing that it is showing, with no more options." | BINDING, newest |
| 20 Oct (D185) | Screens must not bombard with text; make them better and "more aligned with the app". | BINDING |
| 19 Oct (G12) | A fresh account must see at least 3 or 4 suggestion cards, never a single one. | BINDING |
| 19 Oct (G13) | The accept animation of "Do this next" should be better. | BINDING (Today) |
| 18 Oct 8:15 pm (D94) | Approved swipe v2 as drawn: Up next / Not now, buttons under the deck (so the controls stay and mirror the drag), a first-time demo, undo, honest learning. | BINDING |
| 18 Oct 7:40 pm (D90) | A first-time user "won't know what cards actually do or what swipe left and swipe right mean, so you have to build the entire process into this." | BINDING |
| 18 Oct 12:50 pm (D51 approved) | A right swipe makes the card the lead; it never starts or spends. "Skip" and "Do this instead" buttons stay as the visible path. | BINDING |
| 18 Oct 1:45 am (D1, D2, D3) | Today must lead, be interactive, "do more things not just start every 10 minutes", never look like a form. | BINDING |
| 18 Oct (D35, 8:40 am) | The R3-based web Today is "better now". | BINDING (KEEP) |
| 17 Oct (F11, F14) | "A student must see at once what happened and what to do next." | CONTEXT. LK11 sharpens it: one leading action, but with real alternatives. |
| 17 Oct (F18) | The product should lead students to each feature at its moment and show value. | BINDING |
| Agent research (FEATURE-ADOPTION-2026-10-17.md rule 2, "Today is one hero card ... 'Choose something else' is a small link") | PLAN-TEXT. It is the origin of the single-card pattern that LK11 now rejects as too thin. | Superseded by LK11 where they differ |

The existing precedent for "one lead plus alternatives" is the Today lead card, the "Something else" link and the swipe stack. A Learn "what next" panel can reuse that vocabulary instead of inventing a new one.

---

## 5. Study sessions, time choosers, the Start sheet and navigation

### 5.1 The Start sheet (he praised it repeatedly), BINDING keep

- 15 Oct: "This start thing ... I really love it. What you have done with it is really thoughtful." The horizontal subject row must scroll on desktop.
- 17 Oct 11 pm (N11): "Really love the UI of the start session thing. Everything is super refined." Only the spacing between Quick practice and the other modes remains.
- Ledger Keep list: "the Start session sheet ('loved', N11)".
- Rules that came with it: modes read as buttons (F5); subject logos large (F6); unselected chips lightly blurred (N2); fine-tune for Quick practice only (F9); a leading cue that the subject row scrolls sideways (G27); show the mode, not "5 questions Biology", at the top (G26); no flicker of the Start button on scroll (F12).

### 5.2 Subjects loop and Practice, BINDING keep

- "Subjects Loop. Perfect now. Overall the UI part and everything in the Practice is really refined and looks really good." (18 Oct, D4)
- Ledger Keep: "the Practice UI", "the subjects loop".

### 5.3 Time and length choosers, BINDING

- **Minutes (Today and onboarding):** keep 10 / 20 / 30 (D46, "you be the judge", CTO kept it), and add a tasteful custom option: 1 hour = a mock a day, 2 hours = two mocks, "never cap a motivated student" (H1, D126 "More" bubble, no cap). The smart layer should learn real patterns and feel intelligent.
- **Questions:** 5, 10, 15, 20 and a full mock (D50, CTO reading of "5, 10, 20 only"). **Credits equal questions** (D65: "5 questions, then 5 credits only"); a full mock is 50. Free first full mock per subject is OFF (D175).
- **Controls must look controllable:** study days "not a clear or obvious UI choice" (D47) and a mock-count slider "not exactly doing anything" (N1). Any time or count control in Learn needs a live readout that shows what changes.
- **No long single scroll or tiny sliders without effect (D173, N1).**
- LK10 and LK12 mention a time ("They select the time for which they want to practice", "a 10-minute lesson"). That is the same family as these choosers. There is no recorded rule that Learn time must be 10/20/30, so the set is open, but the custom-time rule (never cap) and the readout rule apply.

### 5.4 Navigation, dock and the More sheet, BINDING

- **Bar:** praised: "just awesome ... perfect" (H5, 19 Oct). Do not change it without his yes.
- **Earlier dock rules still in force:** active indicator right on every tab (D13); a pill evenly round (G11); one sliding indicator (N5); glass on chrome, "I really love it in the Apple system" (F3); icons readable, no odd glyphs (14 Oct, W-069); 4 to 6 slots, aligned (F1, W-066).
- **No denser navigation (15 Oct):** "Cluttering each page with more information is not the solution." Regroup, never merge pages.
- **Back (D43):** a clear Back button, not only a small icon.
- **Discoverability (D5, D20, H7, H9, LK1):** "no one will be able to see it ever", "not hidden ... something extra", "no clear-cut access". The same complaint has now been made about Practice's repair and Mobi entries, Learn, Colleges, and Key cards. The pattern is clear: what he cannot find at a glance counts as missing.
- **Sidebar and guide:** "Help" is the wrong word and place (D11, answered by a Guide page); the Guide section must be intuitive (N17); "Show me around" stays visible.
- **Ask Mobi:** never below the theme control (D6); entry points in Today, Practice and Mob headers; not a stranded orb.

---

## 6. His taste and rules that bear on a Learn redesign (BINDING, from TASTE and the ledger)

- **What he loves** (TASTE section 1): premium glass and motion on chrome (HIGH, Revolut, Fampay, Apple); Mobi alive and adaptive; rich lamp-lit 3D subject art; bold persuasive true copy; one clear action that leads; unique and not basic; tangible, interactive and refined; a subtle Night.
- **What he rejects** (TASTE section 2): rebuilding approved screens; cutting good stuff; generic basic layouts; clutter ("too much information at once"); strips and bars a student must decode; forms; disclaimers and filler; neon, glow and AI-slop tells; things a first-time user must work out alone; friction; clunky or worse motion; mixed labels on one screen ("Repair first", "Repair in 1", "check it here": "a very confusing UI"); rows that do not look pressable; over-gamified (as bad as sparse); change he cannot see.
- **The 15-point taste checklist** (TASTE section 3) is the done check: unique, premium reference, one leading action, self-explaining first run, no form, rich not cut, calm structure, Mobi alive and adaptive, bold copy, consistency, layout safety (real gap under the status bar, Back button, 44 px), motion, Night subtle and Day equal, instant, visible.
- **How he judges:** he uses the real thing on a phone, screen by screen, verdict first, with what he physically sees. He compares to HIGH, Revolut, Fampay, Apple, Duolingo, Tinder, Opal and "most apps".
- **Standards that win ties after his words:** UXS (sentence-case labels; no middle-dot strings [T-124]; no arrows on button text; no emoji icons; one dominant action; no nested cards; no decorative gradient or glow; hairlines or spacing instead of boxes; 12-hour times; real numbers only).
- **Process rules from him:** end every update with "Things needed from you right now:" or "Nothing needed from your side." (M-018). Message only for something to see, a decision, an action for him, or a real risk (memory fewer-messages). Use relative times and the 12-hour clock (memory). Show real renders early, not pasted sketches (23 Oct).

---

## 7. Conflicts, tensions and how the newest word resolves them

| # | Tension | Resolution |
|---|---|---|
| C1 | "One clear next move" (F11, D1, D3, agent research FA-2) versus "not dynamic ... one thing ... no more options" (LK11) | LK11 wins. One leading action stays, but it is chosen dynamically and sits beside real alternatives (what is due, what is next in book order, what the student picked). Precedent: the Today lead card and the swipe stack (D94). |
| C2 | "Review leads with weak chapters" (D18, N13) and the plan's "marks at stake / Fix next" spine versus "easier self-control rather than just ... focusing upon the weaknesses" (LK9) | Both stand in their own place. Review keeps D18. Learn is student-led. Weakness becomes a lens or a suggestion, not the organising idea. |
| C3 | "No new top-level nav tab" (BSPEC) and "the bottom bar is perfect" (H5) versus "badly placed and very small" (LK1) | LK1 is about placement and size, not about a tab. The bar is frozen by H5 and D105. Fix the entry in Practice (the Learn door and the web tab row), Today, Explore and the chapter pages. A dock slot for Learn is a decision to put to him (LEDGER line 360 notes "Learn one tap on phones is a dock change"). |
| C4 | Learn "at the moment of need, no tab" (17 Oct design, PLAN-TEXT) versus "should not be hidden ... seems like something extra" (H7) and "C: three doors" (D126) | Owner words win. Learn is a visible door beside Practise and Your papers, and the moment-of-need links stay in addition. |
| C5 | "Refine, don't rebuild" (Never again 1) versus the new flow in LK10 | He himself asked for a new Learn flow and said the area is "far from what we are looking to do". The Learn shell may be redesigned. Keep what he praised (Study mode, the cards, Start sheet, Practice, swipe stack, Today, bottom bar). Mock-up first, in real renders. |
| C6 | Free taste versus open flow (D206) versus LK10 "many things lined up" | Free sees a taste of everything; the flow, the time chooser and the mixed set must work on Free, with the locked parts showing quietly (D101: Pro-only modes "visible but locked", never hidden). First Pro prompt only at a real limit (D181). |
| C7 | Cards "exact NCERT language" (D202) versus "no walls of text" (LK11, D185) | Both apply. Cards keep NCERT wording (short, with the reference). Everything around them stays minimal: one idea per screen, a short sequence of focused screens rather than one long scroll (D173). |
| C8 | Plan paraphrase "(a) older-syllabus shelf" and "paraphrase except one line" versus D201 and D202 | The owner words (D201, D202) win. |
| C9 | One long scroll versus many screens (D173) | Neither extreme. "Clean means easy to find and not overwhelming." |

---

## 8. The "Must know" mark

- **His words:** "everything just has a 'must know' mark to it, which makes it kind of weird. Okay, not everything has it, but multiple things have it. These can be changed or something." (LK13: "Too many cards carry 'Must-know'; change it.")
- **What the system does with it today:**
  - PLAN section 4b defines it as "*Must know* (asked in past papers, or a core NCERT definition) or *Good to know*".
  - In the published decks: 3,916 of 5,800 cards (67.5%) are `must`; 1,884 are `good`. Per deck: Accountancy 618 of 868, Biology 916 of 1,394, Business Studies 629 of 900, Economics 832 of 1,193, English 193 of 349, Political Science 728 of 1,096. No card has a value in `asked`. Source: `wt-1031-keycards-web/data/keycards/decks/*.json` (counted in this read-only pass; another worktree, `wt-1031-lk-mustknow`, exists and was not inspected).
  - BSPEC makes Must-know the engine's key: Free taste cards "Must-know first among ties", the due queue "Must-know first", "Add chapter to Revise" adds the Must-know set, Last look is "Must-know only", Print chapter sheet is the Must-know cards, and `memoryShare` counts only Must-know cards (BSPEC lines 203-224, 335-337).
  - The UI shows "{n} Must-know in all" and "Adds the N Must-know cards" in `src/components/keycards/ChapterDeck.jsx` (lines 282, 337, 369).
- **What this means for the redesign:** the label is shown on too many cards, and several features (Last look, print sheet, add set) depend on it. The owner asked only to change what he sees ("These can be changed or something"). He gave no replacement rule.

---

## 9. What a Learn redesign must obey (numbered, each with its source)

1. **Show him a mock-up in real renders (390 and 1440, Night and Day) before anything ships.** Never ship a replacement of something he has seen without it. (Never again 1; LK14; D91; memory real-renders-not-sketches; BSPEC "mock-up first".)
2. **Follow his LK10 flow:** subject, concept or chapter, what is lined up, time, a mix of cards and questions. Plus a separate "find what is where / revise chosen cards" place. (LK10)
3. **Give the student control.** Weakness is a suggestion, never the only door. (LK9)
4. **One leading action that is dynamic, with real alternatives next to it.** Never a single fixed suggestion. (LK11; D94; D1)
5. **No walls of text, no information overload, no text inside cards upon text.** A short sequence of focused screens beats one long scroll, and too little is as bad as too much. (LK11; D185; D173; 14 Oct balance ranking)
6. **Bring Key cards into Explore** as a custom chapter feed, such as a 10-minute run mixing practice cards and MCQs. (LK12)
7. **Make the way in findable and big.** Fix the entry points; do not add a dock tab without asking. Learn is a visible door in Practice (D126), not "something extra". (LK1; H7; D5; H5; D105)
8. **Keep the bottom bar as it is.** (H5; D105)
9. **Keep Study mode's structure** and add motion on "Got it" (and across the card flow). (LK5)
10. **Print chapter sheet stays, with the MockMob watermark all over it.** The exact watermark wording or design is not given. (LK6)
11. **Explain Read versus Last look, or merge them,** so a student never wonders what the difference is. He asked only that it be unambiguous. (LK7; N5 for the switch animation)
12. **Fix the option picker for Accountancy, Maths and CS.** Selecting must not reorder or shuffle. (LK2; D200 CUET intricacies)
13. **Change how "Must know" shows, and do not stamp it on most cards.** (LK13; section 8)
14. **Cards keep NCERT's exact words with the reference.** (D202)
15. **Free is a taste; the full value is Pro.** The locked parts are visible and quiet, with no modal on entry and no Pro ask before a real limit. (D206; D101; D181)
16. **Self-explaining for a 16 or 17-year-old new to CBT.** Gestures and controls are shown and coached the first time. A fresh account must be complete and never show a single card. (G23; D90; G12; F18)
17. **Rows and cards must look pressable;** a clear Back button on every nested page; targets of 44 px or more; one sliding indicator for any segmented control. (F5; D43; N5; W-079)
18. **Chapter lists are grouped and searchable.** (F8)
19. **Rich, not cut.** Reduce clutter by structure (layers, grouping, progressive disclosure), not by deleting the good stuff, the mascot moments or rich cards. (Never again 2; N12)
20. **Mobi, tastefully and adaptive, one per screen.** (13 Oct, D48, L35)
21. **Premium motion that explains state:** glass on chrome only, subtle Night, springy interruptible motion, haptics in the app, and nothing that is worse than the version it replaces. (F3; D7; D10; N5; TASTE section 3)
22. **Copy:** bold, specific and true; no filler, disclaimers, build jargon, middle-dot meta strings or exclamation marks on success. (M-006; W-093; UXS section 7)
23. **Web and app together.** Any new feature is built for both, and the website is the main product. (14 Oct rule; D157)
24. **Make the change visible and say where to look.** (D33)
25. **Verify as him:** a real device or live walk with screenshots, first-time student path, then his ledger. DONE means live or on a walked APK. (device-truth memory; ledger "When something ships")
26. **End each update with "Things needed from you right now:" or "Nothing needed from your side."** (M-018)

## 10. What he praised and must be kept

From LEARN: **Study mode** ("exactly what we wanted"), and the card quality ("They seem decent to me"). The watermarked print sheet idea ("maybe a good idea").
From the ledger Keep list and his words:
- Start session sheet (N11, 15 Oct).
- Practice UI and the subjects loop (D4).
- The swipe stack v2 (D94, D97) and Today's lead card with Road to CUET (D14, D35, D1 "clean").
- The bottom bar and its animation (H5, G10), and the Today page (G14).
- The result's front, answer sheet and overall summary; scores by session; weak chapters content (N13, N14, N16, D16).
- The Progress phone page (D19), the mobile web UI overall (D14), Day mode (N10).
- The onboarding first screen (G2), common course sets and picks (G9).
- The truthful Play-it-back reel concept (D29: "the concept is really good").
- Badges (D19: "they look cool so keep them").
- Explore (D21), the Mob, Your standing.
- Real subject objects (lamp-lit 3D art: "really premium"), and the logo B.

## 11. What he rejected and must not come back

- **The Learn area as built on 31 Oct:** entry too small and badly placed; Learn shell "not very good or easy to use"; Read layout "very weird"; Last look unclear versus Read; the lone next action; "Must know" on many cards.
- **Rebuilding an approved screen** (web restructure 15 Oct; result 17 Oct, "not acceptable at all"; Today R4 18 Oct, "a huge regression").
- **Cutting for simplicity** ("removed the good stuff").
- **Weakness-only steering** for Learn (LK9).
- **Walls of text and text bombardment** (D185, LK11).
- **Single fixed suggestion** (LK11); a single card for a fresh account (G12).
- **Tiny or hidden entry points** (D5, D20, H7, H9, LK1).
- **Forms and settings that look like forms** (D3).
- **A tiny back icon as the only way back** (D43).
- **Segmented controls with two boxes** (N5), and any motion that is worse than before (D10).
- **A heavy blur that feels locked** (N2). **Neon, glow and gradient AI-slop tells** (TASTE).
- **Over-gamification** as bad as sparse (14 Oct); an "aura farmers" style (D22).
- **A long single scroll for everything** (D173).
- **Defensive disclaimers and filler lines** (W-093); "Older syllabus" shelf by default (D201); paraphrasing NCERT on cards (D202).
- **Agent notions he never approved:** a Learn "at the moment of need only" with no visible door (see C4); "no new surface at all" for Key cards (see C3).

## 12. Open questions the record cannot answer (for the main session to put to him or decide as CTO)

1. What is "Fitzmeen downloading"? Likely "preventing" (the transcription guess in LEARN). Is the print sheet Pro only, and should the watermark carry the student's name?
2. Last look versus Read: does he want them merged or only explained?
3. Does he accept a Learn dock slot on the web phone dock or in the app bar, or should it stay a Practice door? (H5 and D105 say the bar is done.)
4. Is the Explore custom feed the existing web `/explore` (and the app's "Untimed questions"), or a new surface?
5. What replaces "Must know"? His wording is "can be changed or something".
6. Should the time chooser be 10/20/30 plus custom, or minutes for Learn specifically? (H1 says never cap.)
7. Free taste size for the new flow (the build uses `tastePerChapter`).
8. Whether D126's "Learn" door in the app has ever been walked by him: LEDGER says built in v15.4, not on his phone at the time.

## 13. Problems seen in the records themselves

- LEDGER lines 360 and 106 still list D20 as open with "Learn one tap on phones is a dock change" while H5 and D105 freeze the bar. The two statements are not reconciled anywhere.
- `asked` is empty on all 5,800 published cards although PLAN section 4b defines Must-know partly by past-paper asks; the label's meaning in the product is therefore not what the plan says.
- BSPEC (an agent spec) says "No new top-level nav tab" and puts Key cards one link deep in the Learn hub; the owner's LK1 shows that was too small. Nothing in the record has him approving that entry design.
- BSPEC uses a middle-dot string for the NCERT reference ("Business Studies Part 1 · Ch 1 · p. 3") while HANDOFF-2026-10-31-KEYCARDS-2.md says no middle-dot strings per his rule T-124. The live screens may differ; check.
- The "Never again" list in LEDGER is numbered 1 to 6, 8, 7 (out of order), which is only a numbering slip.
- The ledger says the LEARN items are folded in as LK1-LK14 but several decisions about Learn (D126 Practice C, C-pick 1 web nav A) were made by the CTO or by choosing among mock-ups, not dictated, so the "his words" for those are option labels, not prose.

## 14. Source index (files read for this report)

- brain/OWNER-FEEDBACK-2026-10-31-LEARN.md (all)
- brain/OWNER-MASTER-LEDGER.md (all, 617 lines; the LK block is lines 601-616, D200-D207 lines 574-599, Never again 38-52, Keep 54-68)
- brain/OWNER-TASTE-PROFILE.md (all)
- brain/OWNER-VISION-2026-10-15-PM.md (all)
- brain/OWNER-FEEDBACK-2026-10-17.md and -17-NIGHT.md (all)
- brain/OWNER-FEEDBACK-2026-10-18-DAWN.md (his words and ledger, lines 9-130, 185-260, 345-420)
- brain/OWNER-FEEDBACK-2026-10-19.md (lines 1-330, 507-560, 618-634, 773-806, 859-906, 951-978; searched the rest)
- brain/design-2026-10-13/OWNER-FEEDBACK-1014-1830.md and OWNER-FEEDBACK-1110.md (all); owner-materials.md and directions-final.md (searched)
- brain/INTELLIGENCE-LAYER-PLAN-2026-10-31.md (all)
- brain/intel-1031/KEYCARDS-BUILD-SPEC.md (lines 195-230, 303-366; searched the rest)
- brain/HANDOFF-2026-10-31-KEYCARDS-3.md (all), HANDOFF-...-KEYCARDS.md and -2.md, PROMPT-NEXT-SESSION-2026-10-31.md (searched), NOW.md (top 60 lines and headings, as data)
- brain/FEATURE-ADOPTION-2026-10-17.md, WEB-OWNER-LEDGER-2026-10-17.md, APP-OWNER-LEDGER-2026-10-16.md, MISSED-ASKS-2026-10-18.md (searched for Learn, Explore, nav, Start, session)
- design-decisions/pass-1017/LEARN-REVIEW-1017.md (sections 1, 2.3, 4, 5.8-5.12, 11), pass-1017/NAV-1017.md, pass-1018/SWIPE-V2-1018.md and TODAY-SWIPE-1018.md (headers and the owner lines), pass-1018/COMMUNITY-1018.md, pass-1019/WEB-NAV-1019.md, pass-1019pm/PRACTICE-COLLEGES-GOAL-1019PM.md
- AI OS/wiki/concepts/ui-ux-standards.md (all)
- Memory notes: web-restructure-rejected, audience-teens-new-to-cbt, real-renders-not-sketches, mockmob-design-direction
- Deck counts: wt-1031-keycards-web/data/keycards/decks/*.json (read-only, counted in this pass)

Not inspected (outside this task, existence only): worktrees `wt-1031-learn-v2`, `wt-1031-lk-fixes`, `wt-1031-lk-motion`, `wt-1031-lk-mustknow`, which may already hold work on these items.
