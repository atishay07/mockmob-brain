# Owner feedback, 17 Oct 2026 about 12:45 am IST (app seen on the emulator during the v12 walk, website used live)

The owner asked for this to be read carefully, noted completely, and used as context in every future session. His words are kept as he wrote them (voice-typed; light obvious-typo notes in brackets), then turned into a ledger with ids. Newest owner words win over older ones.

## His words

**App (seen while the emulator tests ran):**
> Some UI elements are looking really nice, really good, though some still need refinement.
> One of the things that was previously really good was stated as a rule: it's like a 4-to-5 or 6-system. Right now, we are at 6, but it is not aligned properly at all. Should we have to think? In some sense, less, more also.
> Maybe because I told you to integrate colleges properly, I have done this, but I don't know what exactly the solution to this is. One thing is for sure: this right now is not good. You have to figure out some way. Just do the research on the UI/UX report site. They have many things about the nav and how perfect nav files popular apps have been built.
> And I would really like it if you could somewhat follow. I know it's difficult in Android because it stretches instead of bouncing, but the liquid glass design and how it interacts with everything, I really love it in the Apple system. I just want some of that taste to be carried forward in the app also, on the app level, not the Android UI. Obviously, we can't do anything about that, but we can control the app UI, so that would be something really cool.

**Website:**
> Firstly, some places still lack some of the design language. It feels somewhat like this full mock in the start menu is better incorporated in the mobile app than on the website.
> The issue is that, on the start menu, when I go on to select any of the things, the quick practice is theoretically working, but it's not giving the feel of a button that does something. I don't know why these feel like cards depicting information rather than buttons that I click and an action happens. On the top, subject selection is clearly being figured out as a button.
> Also, with these subjects, a bit of refinement is needed in the area where the logos are placed. Maybe the logos can be made a bit bigger, like in the top card of "Finish your recall session". There also, when the subject is changing actively in the card, the subject name can be changed or something like that.
> Right now, I'll do a quick practice of 10 questions. Maybe this fine-tune option should be given above the start quick practice so that everyone can see and customize it properly. I think this is something that people will skip through, and the UI of this fine-tune thing can be improved. Chapters are cluttered, and it's difficult to find exactly what we are looking for.
> Overall, the UI of attempting the mocks is really fluid, but there is some kind of thing which moves when I'm selecting it, top to down. When I move to an option, there are two boxes: one box is confirming my selection, and there's another box which is coming out of it as an animation. There are these small finish things which have to be taken care of.

**Result screen:**
> Mobby [Mobi] sleeping here feels a bit weird to me and is very confusing to me. I don't know how to even enter this or what exactly it is trying to do. I would just say that over here is a bit confusing. I'm still not sure if "repair the mistake" is what it is adding as a useful thing. Submission is there, and the add submission is there.
> This one is okay: the "check it" hold [Check it held] that you write. Just one thing: I don't know how to fix this. I had only requested all these features, but the UI is just too cluttered on the result screen. The spot [SWOT] analysis repair thing is just too much and too confusing. This is coming from a person like me who already understands everything on the site. If I see it from the student's point of view, they won't be able to figure out anything in this UI. What is going on, and what do they have to do? This requires a lot of thinking. I know it's very hard to exactly fix this, but we have to do something about this.

**More website:**
> In the subject selection on top, out of the five subjects, when we are selecting one subject, the others get blurred. That is good. I am not picking here, but just increase the blur of the other subjects a bit more so that the current section is a bit more clear. Also increase the size of the logos, as I had said before.
> The fine-tune mode should be disabled automatically in the NTA mode or in the full mock mode because full mock mode can have the difficulty slider but not the chapter option. Even in the smart mode I think we should not give that because we are weighing all this ourselves and using the intelligence to analyze. That's what we are advertising at least. The entire fine-tune should be in the quick practice only.
> There are a lot of things to think about, like the bottom navbar and all. I had already given a lot of feedback related to all this previously and I don't think that all that has been taken into account.
> Another bug kind of thing is this quick practice thing: when I am scrolling down, the start button gets white and then a pop-up comes up for practice (15 questions, 15 minutes included). As I scroll down it disappears and then as I scroll down it again appears. What state is it really following? That is the confusion. I think it's hiding itself for some button or something, but just see if there is any bug or if this is intended behavior.
> The bottom half, again, I had given the feedback here: it looks kind of weird to me, the placement of the start button at least. This today section I never really liked: very cluttered, very confusing. The learn and review section I'm not even going to look at. I know there are many things which need refinement there, so I just don't want to get disappointed right now.
> I think I have given you some direction of what I like and what I don't, so you can now act with it as the CTO. Define it.

## Ledger (ids for tracking; all open)

| Id | Surface | Item | Owner's rule or ask |
|---|---|---|---|
| F1 | App | Bottom nav | His earlier rule was a 4-to-6 slot bar, and he praised it when it worked. Today's 6-slot bar is "not aligned properly at all". Rethink the count: fewer may be better. |
| F2 | App and web | Where Colleges lives | The current integration "is not good". Research how popular apps structure navigation (his UI/UX research, Mobbin-style references), then decide. |
| F3 | App | Liquid-glass taste at the app level | Apple's Liquid Glass, interactive and responsive material. App UI only. Bounce instead of Android's stretch where the app controls scrolling. |
| F4 | Web | Design language gaps | The Start menu's full mock is better in the app than on the web. Bring the web up to the app. |
| F5 | Web | Start menu affordance | Quick practice and the other modes read as information cards, not buttons. They must feel pressable and do something. Subject selection already reads as buttons. |
| F6 | Web | Subject logos | Bigger, like the "Finish your recall session" card. When the subject changes, the card's subject name changes with it. |
| F7 | Web | Subject chip row | Keep the blur on unselected subjects, and blur them more. Bigger logos. |
| F8 | Web | Fine-tune placement and UI | Put it above "Start quick practice" so people see it. Improve its UI. Chapters are cluttered and hard to find: group them and add search. |
| F9 | Web and app | Fine-tune scope | Quick practice only. Full mock: difficulty only, no chapters. NTA mode and Smart practice: no fine-tune (we choose; that is what we advertise). |
| F10 | Web | Runner option animation | Picking an option shows two boxes: the confirm box plus a second box animating out of it, moving top to bottom. Make it one clean state change. |
| F11 | Web and app | Result screen | Too cluttered and confusing. Remove the sleeping Mobi (it is confusing). It is unclear what Repair adds. The submission is shown twice. The SWOT, analysis and repair stack is too much. A student must see at once what happened and what to do next. Check it held is fine. Needs real rethinking. |
| F12 | Web | Quick practice Start button state | On scroll the Start button turns white, a "15 questions, 15 minutes" pop-up appears, hides, then appears again. Find the rule. It is either a bug or a confusing intended behaviour; fix it either way. |
| F13 | Web | Bottom dock and Start placement | The Start button's placement looks weird. His earlier dock feedback was not fully applied: re-read it. |
| F14 | Web and app | Today | "Never really liked: very cluttered, very confusing." Redesign for one clear answer and one next move. |
| F15 | Web | Learn and Review | Need refinement; he did not look at them on purpose. |
| F16 | Both | Overall | Some UI elements are "really nice". Keep what works. Never simplify by cutting features. Act as CTO, define and execute. |

## How to use this

- Every design agent reads this file with the 16 Oct ledger (APP-OWNER-LEDGER-2026-10-16.md), his research brain (docs/research/premium-ux-ui-2026-10/AGENT_RULES.md) and the ui-ux-standards skill.
- Work is not done until an emulator walk (app) or a visual gate at 390 and 1440, Night and Day (web) shows the item fixed. Tick items here with the proof path.

## Added about 1:20 am IST (his words, then ledger rows)

> In the review, when I go to review any wrong answer which I had just attempted, the things which I had already repaired... are getting lost. I have to repair it again and spend another credit. That should not happen, and it should show the mock time and date when that was attempted in the review section. ... Okay, now it's working, so maybe it was not a bug.
> Overall, the UI/UX choices are still very confusing, even to me. ... Even last year, students were confused, and they didn't use 90% of the features because they didn't actually know what they were to do with this. We have to learn this from the top edtech platforms: how they make students utilize all the features, which gives them the feeling that what they're paying for is offering them value.

| Id | Surface | Item | Owner's rule or ask |
|---|---|---|---|
| F17 | Web and app | Review shows past repairs and when the mistake happened | A mistake already repaired must open its saved repair, never offer a paid repair again. Each mistake shows the mock and the date and time it was attempted. The data on 17 Oct showed 3 repairs on 3 different questions and no double charge, so the problem is visibility, not billing. |
| F18 | Both | Feature adoption and perceived value | Students did not use 90% of features last year because they did not know what to do. Learn from top edtech platforms how they lead students to each feature and make paid value felt. Research ran 17 Oct; it feeds the build round. |
