# E: the English in Learn v2, Explore and Key cards (LK61)

Packet E of `R7-SPEC.md` (3 Nov 2026, evening). This is a proposal only: no code is changed. The changes land after the W and I branches.

He said (3 Nov, about 3:15 pm): "Overall, the English that you write for everything, for sure, as I said, we want it to be improved." On 2 Nov he
also said: "Genuinely people should be able to understand what these three options do. Missed it, Got it, Easy. Even I have attempted so many and
I am unable to understand." Rows 1 to 6 answer that.

**What was read.** Web `wt-1103-web-cards` (branch web/1103-proto): `data/learn/{words,allowance,compose,suggest,roadmap,feed,stamps}.js`,
`src/components/learn2/**`, `src/components/keycards/**` and `src/components/feed/**`. App `wt-1103-app-r5-port`: `flutter_app/lib/features/learn2/**`
(the six `*_copy.dart` files, `data/learn_words.dart` and the model files that build lines) and `features/keycards/**`.
Skipped: card and question content, `fixtures.js`, chemistry symbols, routes, storage keys and CSS. That left about 1,080 distinct strings: about 660
on the web and about 420 in the app, many of them the same line on both.

**Before anyone edits.** `WORDS` (web `data/learn/words.js`) and `LearnWords` (app `data/learn_words.dart`) are held together by
`test/unit/learn2/data/learn_words_parity_test.dart` (cases from `tool/learn2_parity/words.mjs`), and the copy tests pin many of these lines. If a
row changes a shared word, change it on both sides and in those tests in the same commit. "Web" and "App" in the Where column mean the same line on
both platforms unless a row says otherwise.

## The table (most-seen first)

| # | Where | Before | After | Why |
|---|---|---|---|---|
| 1 | Web `words.js` `coachRatings`; App `LearnWords.coachRatings` (the coach line under the rating keys) | Missed it brings a card back soonest. Easy sends it furthest away. | How well did you know it? Missed it brings the card back soon. Got it, in a few days. Easy, much later. | He could not tell the three keys apart. One line now covers all three, in the order they appear on screen. The facts stay the same: the soonest return and the furthest return. |
| 2 | Web `RunPlayer.jsx:729`, `KeyCard.jsx:329` (`How well did you recall it?`); App `RunCopy.ratingGroup`, `KeyCardsCopy.howDidItGo` (`How did it go`) | How well did you recall it? / How did it go | How well did you know it? | One question for the same three keys on both screens. "Recall" is exam-book English. The app's version had no question mark. |
| 3 | Web `keycards/kinds.js:54` (`RATINGS`); App `KeyCardsCopy.missed` | Missed | Missed it | Learn already says "Missed it" (round 5, LK38). The Key cards screen said "Missed" for the same key. |
| 4 | Web `KeyCard.jsx:326` (`Show answer`); App `KeyCardsCopy.tapToReveal` (`Show the answer`) | Show answer / Show the answer | Turn over | One action had three names: Learn says "Turn over", the website's Key cards said "Show answer" and the app said "Show the answer". `WORDS.turnOver` is the shared word. |
| 5 | Web `ChapterDeck.jsx:191` | Each card you rate joins Revise: Missed brings it back soon, Got it and Easy space it out. | Each card you rate goes into Revise. Missed it brings it back soon. Got it and Easy bring it back later. | Uses the key's real name, and says "bring it back later" instead of the idiom "space it out". |
| 6 | Web `compose.js:55` `NOTE_FIRST`; `compose.js:54` `NOTE` (the chapter page's note under the keys) | Ratings join Revise, so cards come back when they are due. / Ratings join Revise. Questions are free. | Cards you rate go into Revise and come back when they're due. / Cards you rate go into Revise. Questions are free. | A rating does not join anything; the card does. |
| 7 | Every student-facing "run": Web `RunPlayer.jsx:157`, `:635`, `:649–650`, `RunEnd.jsx:39`, `RunParts.jsx:213`, `:249`, `ChapterPage.jsx:449`, `chapterModel.mjs:65`, `compose.js:399–400`; App `RunCopy.loadingLabel`, `errorTitle`, `emptyTitle`, `emptyLine`, `endErrorTitle`, `lessonLine`, `ChapterCopy.listLabel`, `chapter_model.dart:175` | run (for example "Lining up your run", "This run did not start", "Cards in this run…") | session ("Getting your session ready", "This session didn't start", "Cards in this session…") | The product already says "session" to students: Free's "today's free session" and the run's own "This session" header. "Run" is our internal word. Use one word everywhere. |
| 8 | Web `RunPlayer.jsx:157`; App `RunCopy.loadingLabel` | Lining up your run | Getting your session ready | "Lining up" is an idiom. Many first-time CBT students will not read it at a glance. |
| 9 | Web `roadmap.js:225`, `:212` (the hero's line); App: drawn from the server | Chapter 3 of 14 · Admission of a Partner | Chapter 3 of 14: Admission of a Partner | The owner's standard bans middle-dot strings. The dot is allowed only before a length (" · N min"). |
| 10 | Web `roadmap.js:220` (the hero's sub line) | 2 due cards first, then new ones here | 2 due cards first, then new cards from this chapter | Says what "ones" means and where "here" is. |
| 11 | Web `roadmap.js:180` | 3 steps lined up | 3 cards and questions to go | "Steps" and "lined up" are build talk. If the items are not all cards and questions, use "3 left". |
| 12 | Web `runView.mjs:183` `leadView` (the end's lead key) | Start 10 minutes | Start · 10 min | Every other key with a length uses " · N min" (ruling W). This one key spelled the length out. |
| 13 | Web `allowance.js` `FREE_CAPPED`; App `LearnFreeWords.capped`, `ExploreCopy.freeCapped` | Free sessions are up to 10 minutes. Pro has any length. | On Free, a session is up to 10 minutes. With Pro, pick any length. | "Pro has any length" is not natural English. Same facts. |
| 14 | App `FeedCopy.freeDoneShort` | Your free Learn session for today is done. | That was today's free session. | Ruling F says one sentence everywhere. The app's feed had its own version. |
| 15 | Web `endModel.mjs` `progressLabel` / `FREE_REST_PRO`; App `stage_end_model.dart:127` | 5 of 45 cards seen · the rest open with Pro | 5 of 45 cards seen. The rest open with Pro. | Removes the middle dot. Two short sentences read more easily. |
| 16 | Web `homeModel.mjs:280`; App `home_model.dart:315` | Needs work · from your papers | Needs work, from your papers | Removes the middle dot. The owner called these recommendation lines "not good" (LK59). |
| 17 | Web `homeModel.mjs:150`; App `home_model.dart:231` (sort) | Marks open | Most marks left | "Marks open" does not say what the sort does. The figure is the marks a chapter still has open. Never "marks to recover" (Key cards rule). |
| 18 | Web `homeModel.mjs:203` (spoken), and the row's `−35` figure | 35 marks open / −35 | 35 marks left in this chapter / +35 marks left (or "35 marks" beside the sort) | A bare minus sign reads as a penalty. Give the figure a word. |
| 19 | Web `Question.jsx:116` (`Not quite. It's B.`); `RunPlayer.jsx:485`; App `question_view.dart:754`, `run_controller.dart:687` | Not quite. It's B. / Not quite. The answer is B. | Not quite. The answer is B. | The same verdict was worded two ways. The feed's longer form ("Not quite. The answer is B, text.") stays for screen readers. |
| 20 | Web `RunPlayer.jsx:46`, `ChapterFeed.jsx:48`; App `RunCopy.questionChanged`, `FeedCopy.questionChanged` | This question was updated, so it was skipped. / This question changed a moment ago, so it is left out. | This question was just updated, so we skipped it. | The run and the feed said the same thing two ways. Unified. |
| 21 | Web `RunPlayer.jsx:47`, `ChapterFeed.jsx:49`; App `RunCopy.questionHeld`, `FeedCopy.questionHeld` | This question is in a paper that is still open, so it was skipped. / This question is in an open Mob paper, so it is left out for now. | This question is in a Mob paper that's still open, so we skipped it for now. | Unified. Keeps the more exact "Mob paper". |
| 22 | Web `ChapterFeed.jsx:51`; App `FeedCopy.closedLine` | This feed is finished, so this one is not counted. | This feed has ended, so this answer wasn't counted. | "This one" did not say what was not counted. |
| 23 | Web `feed.js:26` `CHECKPOINT_LINE`; App `feed_model.dart:215` | Keep going, or end here. What you kept is already in Revise. | Keep going, or stop here. The cards you kept are already in Revise. | The key below says "Stop here", so the line uses the same verb. "What you kept" is vague. |
| 24 | Web `feed.js:133` `keptLine`; App `feed_model.dart:241` | 3 kept. They are first in Revise. | 3 cards kept. They'll come first in Revise. | Says what was kept, and uses the future tense ("they'll come first"). |
| 25 | Web `ChapterFeed.jsx:134`; App `FeedCopy.pickedUp` | Picked up at 5 of 21 | Carrying on from 5 of 21 | "Picked up" can be read as "picked up a card". |
| 26 | Web `coverModel.js:89`; App `cover_model.dart:185` (a cover's key) | Play | Start | Learn says "Start" for the same act. "Play" makes studying sound like a game. |
| 27 | Web `ChapterFeed.jsx:494`; App `FeedCopy.emptyTitle` | Nothing to play here yet | Nothing here yet | Same reason as row 26. |
| 28 | Web `coverModel.js:79` | Cards and questions, all it has today | Cards and questions, that's all for today | The original was missing a word. |
| 29 | Web `ExploreCovers.jsx:291`; App `ExploreCopy.showing` | Showing 10 minute feeds. | Showing 10-minute feeds. | A length used before a noun takes a hyphen. |
| 30 | App `ExploreCopy.none` | No chapter feeds for Physics yet. The questions below still work. | No chapter feeds for Physics yet. You can still answer the questions below. | "Still work" sounds like a bug note. |
| 31 | Web `DiscoveryFeed.jsx:252`, `:284` | Community votes help organise the feed. They do not certify an answer. | Votes from other students sort this feed. They don't prove an answer is right. | "Certify" is legal English. Same facts, plain words. |
| 32 | Web `DiscoveryFeed.jsx:260` | Explore · untimed practice | Explore: practice without a timer | Removes the middle dot, and "untimed" is an odd word. |
| 33 | Web `DiscoveryFeed.jsx:251`, `:279` | That is every question for these filters. / You're up to date for these filters. Saved questions are ready for your next round. | That's every question for these filters. Your saved questions are ready when you want them. | Two endings for the same state. "Next round" is undefined here. |
| 34 | Web `DiscoveryFeed.jsx:282` | Tonight's rule | One habit that helps | It may not be night when they read it. |
| 35 | Web `QuestionCard.jsx:114` | Feedback is shown, but this activity could not be recorded. | Here's the answer, but this attempt wasn't saved. | "Activity" and "recorded" are system words. |
| 36 | Web `QuestionCard.jsx:115` | This question has no usable answer key. Try the next one. | This question's answer is missing, so we can't check it. Try the next one. | "Usable answer key" is build talk. |
| 37 | Web `QuestionCard.jsx:103`, `:105` | Question unavailable | This question didn't load | Says what happened. |
| 38 | Web `QuestionCard.jsx:99` | Unlabelled | No chapter | Says which label is missing. |
| 39 | App `KeyCardsCopy.questionsWaitServer` | Your questions could not be read just now. The Key cards can. | Your questions didn't load just now, but your Key cards are here. | "The Key cards can [be read]" was a broken sentence. |
| 40 | App `KeyCardsCopy.questionsWaitOffline` | You are offline. Your questions come back here when you are online. | You're offline. Your questions will show here when you're back online. | Contractions and the future tense. |
| 41 | Web `RunPlayer.jsx` `coachRecap`; App `RunCopy.coachRecap` | Answers are showing. Nothing is scheduled. | Answers are shown. This won't change when your cards come back. | "Nothing is scheduled" is opaque. The fact is that a recap does not touch the Revise schedule. |
| 42 | Web `ChapterDeck.jsx:245`; App `KeyCardsCopy.lastLookNote` | Must-know only, and nothing is scheduled. Swipe to move on / Must-know cards only. Nothing is scheduled. | Must-know cards only. This won't change when your cards come back. | Same as row 41. Web and app now say it the same way. Keep "Swipe to move on" on the web where it shows. |
| 43 | Web `kinds.js:66` `PRO_LINE`; App `KeyCardsCopy.proLine` | Pro opens every card in every chapter and keeps them on a schedule. | Pro opens every card in every chapter and brings each one back when it's due. | "Keeps them on a schedule" is abstract. This is the line Free students see most. |
| 44 | Web `FindView.jsx:197`; App `CardsCopy.lockedMatches` | 3 more cards match in cards Pro opens. | 3 more matching cards are part of Pro. | "In cards Pro opens" is clumsy. "Part of Pro" is already used (Save, part of Pro). |
| 45 | App `FeedCopy.keepProStamp`, `saveOnPro` | This card is on Pro. / Saving more questions is on Pro. | This card is part of Pro. / Saving more questions is part of Pro. | One phrase for Pro things. |
| 46 | Free review limits: Web `kinds.js:431–432`, `ChapterDeck.jsx:357`; App `KeyCardsCopy.reviewCapTitle`, `reviewsLeft`; Learn `chapterModel.mjs:65`, `compose.js:56` | card reviews (Key cards) / card ratings (Learn) | card ratings, everywhere | One daily limit with two names. Confirm with the server that it is the same 10 a day before merging the wording. |
| 47 | Web `chapterModel.mjs:65` `RATINGS_USED_LINE`; App `chapter_model.dart:175` | You've used today's 10 free card ratings. Cards in this run show their answers but won't be added to Revise. | You've used today's 10 free card ratings. In this session, cards show their answers but won't go into Revise. | "Run" becomes "session" (row 7), and "added to" becomes "go into". |
| 48 | Web `compose.js:56` `RATINGS_USED` | Today's 10 free card ratings are used. Your cards show without ratings; questions are free. | You've used today's 10 free card ratings. Cards show without rating keys; questions are still free. | Matches row 47, and says what is actually missing (the keys). |
| 49 | Web `kinds.js:428` | That is today's 5 new cards on Free. / Reading the cards stays open, and new cards come back tomorrow. | You've studied today's 5 new cards on Free. / You can still read every card. New cards open again tomorrow. | Plain subject and verb. "Reading stays open" is stiff. |
| 50 | Web `kinds.js:431` | Free includes 10 card reviews a day. Reading the cards stays open, and the reviews come back tomorrow. | Free has 10 card ratings a day. You can still read every card; ratings open again tomorrow. | Same as row 49, using the word from row 46. |
| 51 | Web `compose.js:399` | Revise first: 9 due. Until then a run takes at most 10 new cards, about 5 min. | Revise your 9 due cards first. Until then, a session adds at most 10 new cards (about 5 min). | "9 due" was a bare count ("never a bare 9 due" is our own rule). "Run takes" becomes "session adds". |
| 52 | Web `compose.js:400` | One run takes at most 10 new cards, about 5 min. | A session adds at most 10 new cards, about 5 min. | Same as row 51. |
| 53 | Web `compose.js:402` | This chapter has about 6 min of new things today. | This chapter has about 6 min of new work for today. | "New things" is vague. |
| 54 | Web `chapterModel.mjs:62`; App `chapter_model.dart:172` | Cards and questions, one at a time. Stop whenever you like; what you do is saved. | Cards and questions, one at a time. Stop whenever you like; everything you do is saved. | Reads more naturally. |
| 55 | Web `ChapterPage.jsx:461`; App `ChapterCopy.stale` | We could not update this. The last lined-up run is shown. | We couldn't change the length. You're seeing the last plan. | Says what "this" is, and drops "lined-up run". |
| 56 | Web `ChapterPage.jsx:443`; App `ChapterCopy.failed` | We could not line this up. | We couldn't set up this session. | Removes the idiom. |
| 57 | App `ChapterCopy.offline` | You are offline. This chapter needs a connection to line up. | You're offline. Connect to the internet to start this chapter. | Gives a clear next step. |
| 58 | Web `ChapterPage.jsx:449`; App `ChapterCopy.listLabel` | What's in this run / Lined up for this run | What's in this session | One label on both platforms. |
| 59 | Web `ChapterPage.jsx:164`; App `chapter_piles.dart:513` | Fills | Fills your time | A single "Fills" did not say what it fills. |
| 60 | Web `chapterModel.mjs:40`; App `chapter_model.dart:242` | Tap to put back / …left out. Tap to put it back | Tap to add it back / …left out. Tap to add it back | Simpler verb. |
| 61 | Web `chapterModel.mjs:120`; App `chapter_model.dart:320–321` | Print sheet / 12 Must-know lines, with your name | Chapter sheet / 12 Must-know lines, with your name on it | Names the thing, not the verb ("fix 3" of 2 Nov: name a row for what it opens). The app shares and the web prints, and "Chapter sheet" fits both. |
| 62 | App `KeyCardsCopy.shareSheet`; Web `ChapterDeck.jsx:398` | Share chapter sheet / Print chapter sheet | (keep both) | Keep: each verb is true on its own platform, and the noun "chapter sheet" is now shared (row 61). |
| 63 | Web `RunEnd.jsx` `endErrorLine`; App `RunCopy.endErrorTitle/Line` | Your run is saved / Its summary did not load. Every rating and answer is already in. | Your session is saved / The summary didn't load, but every rating and answer is saved. | "Already in" is vague. Uses the word from row 7. |
| 64 | App `FeedCopy.endErrorLine` | Its summary did not load. | The summary didn't load, but everything you did is saved. | The feed's version said nothing about whether the work was safe. Now it matches row 63. |
| 65 | Web `RunParts.jsx:213`; App `RunCopy.lessonLine` | Read this first. Its cards come next in this run. | Read this first. Its cards come next. | Shorter, and drops "run". |
| 66 | Web `RunParts.jsx:249` | You'll see this card again later in this run. | You'll see this card again later in this session. | Row 7. |
| 67 | App `RunCopy.roundLine` | 5 more are lined up. | 5 more to go. | Removes the idiom. |
| 68 | App `RunCopy.reviseLabel` (spoken) | In Revise 4 | 4 cards in Revise | The screen reader heard it as a broken phrase. |
| 69 | Web `RunEnd.jsx:65`; App `RunCopy.levelSub` | Your lowest score: 3 of 6 right | Your score: 3 of 6 right | "Lowest" puzzles a student after one check. Check first what "lowest" means in `learn.js` (several parts?). If it is the weakest part, say "Your weakest part: 3 of 6 right". |
| 70 | App `HomeCopy.offerLoading` | Loading your start | Getting today's plan | "Your start" is not a noun a student uses. |
| 71 | App `HomeCopy.setEmpty`, Web `FindView` / `homeModel` set lines | Cards you rate in a run come back here on the day they are due. / Rate a card in a run and it joins Revise. / A card you miss in a run shows here until you get it right. | Cards you rate come back here on the day they're due. / Rate a card and it goes into Revise. / A card you miss shows here until you get it right. | "In a run" adds nothing. |
| 72 | Web `CardsView.jsx:29`; App `CardsCopy.empty['must']` | Every card here is a good one to know; none is marked Must-know yet. | None of this chapter's cards is marked Must-know yet. | The first half sounded like an excuse. |
| 73 | Web `FindView` (over); App `CardsCopy.over` | 45 cards match. Pick up to 30 to study them, or add a word. | 45 cards match. Pick up to 30 to study, or type another word to narrow it. | "Add a word" is unclear: add it where? |
| 74 | Web `cardsShared.js:85`, `kinds.js:444` | …The other was already there or is part of Pro. | …The other was already in Revise or is part of Pro. | Says where "there" is. |
| 75 | App `KeyCardsCopy.added` | Added to Revise. 12 cards. | 12 cards added to Revise. | One sentence, with the count first, like the web's `cardsShared.js:85`. |
| 76 | App `KeyCardsCopy.offlineCached` | Offline. Showing what this phone kept. | You're offline. Showing what's saved on this phone. | A phone does not "keep". |
| 77 | App `KeyCardsCopy.nothingDueNote` | Add a chapter to Revise and its cards come back on a schedule. | Add a chapter to Revise and its cards come back when they're due. | Matches row 43. |
| 78 | App `KeyCardsCopy.savedOnPhone`, `reportWaiting` | Saved on this phone. It is sent when you are back online. | Saved on this phone. It'll be sent when you're back online. | Tense, and contractions. |
| 79 | App `KeyCardsCopy.studyAgain`; Web `ChapterDeck.jsx:180` | Go through again / Study again | Study again | Shared word. |
| 80 | Report title: Web `KeyCard.jsx:189`; App `KeyCardsCopy.reportTitle` | What looks wrong with this card? / What is wrong with this card | What's wrong with this card? | Unified. The app's version had no question mark. |
| 81 | Report sent: Web `KeyCard.jsx:186`; App `KeyCardsCopy.reportSent` | Thank you. Your report is saved, and reported cards are checked against the book. / Reported. The card is checked before it comes back. | Thanks. We'll check this card against the book before it comes back. | One warm line on both platforms. Keeps both facts. |
| 82 | Web `KeyCard.jsx:196` | The report was not sent. Your words are still here. Try again. | The report didn't send. Your words are still here; try again. | Contraction, one fewer sentence. |
| 83 | Web `LineYouNeeded.jsx:16`; App `KeyCardsCopy.lineMatched` | Matched by its words | Matched by the question's words | "Its" had no clear owner. |
| 84 | Web `ChapterDeck.jsx:356` | Adds the 12 Must-know cards. Good-to-know cards you add one at a time. | Adds the 12 Must-know cards. You can add the other cards one at a time. | The inverted sentence order was hard to read. "Good-to-know" is not used anywhere else. |
| 85 | Web `ChapterDeck.jsx:357` | Adds the 5 open cards. Free reviews 10 cards a day. | Adds the 5 free cards. On Free, you can rate 10 cards a day. | "Free reviews" reads as a verb ("Free reviews…"). Uses the word from row 46. |
| 86 | Web `ChapterDeck.jsx:381` | This chapter has no book chapter to take cards from, so it is practised with questions. Your other chapters have cards. | This chapter isn't in an NCERT book, so it's practised with questions only. Your other chapters have cards. | Plainer, same fact. "Practised" keeps the product's spelling. |
| 87 | Web `KeycardsHome.jsx:205` | They open here once the first chapters are checked against the book. Lessons and practice are all still open. | They'll show here once the first chapters are checked against the book. Lessons and practice are open as usual. | "All still open" is odd. |
| 88 | Web `optionChoice.js:49` | Choose your option and only its chapters show here and in your practice. Until then, both options show. | Pick your option to see only its chapters here and in practice. Until then, both show. | Shorter, and a clear cause and effect. |
| 89 | Key cards state: Web `kinds.js:372`; App `KeyCardsCopy.stateStrong`, `fadingWord` | Holding / Holding, fading | Going well / Going well, but fading | "Holding" does not tell a student it means good. These labels are pinned by KEYCARDS-BUILD-SPEC, so the owner should OK the change first. |
| 90 | Web `suggest.js:190` | 1,240 Accountancy cards, by term or line. | Search 1,240 Accountancy cards by a word or a line. | Clearer. "Term" means something else in Indian schools (a semester). |
| 91 | Web `suggest.js:260` | Its 12 Must-know lines, answers showing. | Its 12 Must-know lines, with answers shown. | Grammar. |
| 92 | Web `roadmap.js:68` `FEED_ROW_LINE` | Scroll through the chapter, stop any time | Scroll through the chapter and stop any time. | Joins the two parts and ends the sentence with a full stop. |
| 93 | Web `roadmap.js:207`, `suggest.js:172` | 6 questions · about 6 min | 6 questions, about 6 min | The dot is only for a key's length (rule 2). Use a comma in a line. |
| 94 | Web `words.js` `reviseQuestions`; App `LearnWords.reviseQuestions` | Revise · 5 questions | Revise 5 questions | The dot is reserved for a length (" · N min"), and this is not one. |
| 95 | Web `homeModel.mjs:221` (`KIND_WORD.level`) | Level | Skip ahead | A lone "Level" above the "Skip what you already know" row does not say what it is. |
| 96 | Web `UploadForm.jsx:93` | No credit reward is promised for a submission. | You don't earn credits for sending a question. | Legal register to plain English. Same fact. |
| 97 | Web `UploadForm.jsx:107` | Uncertain questions stay held. Submission does not mean publication. | We check every question first. If we're not sure it's right, it isn't published. | Same two facts, in words a 16-year-old uses. |
| 98 | Web `UploadForm.jsx:79` | Saved, but checks could not start yet. Track it in My uploads. | Saved. The checks haven't started yet; you can follow it in My uploads. | Clearer. |
| 99 | Web `UploadForm.jsx:102` | Options · tap a letter to mark the correct answer | Options: tap a letter to mark the right answer | Removes the middle dot. |
| 100 | Web `UploadForm.jsx:106`, `:104` | Submit for checks / Reasoning (recommended) | Send for checking / Why this is the answer (recommended) | Plainer labels. |
| 101 | Every "did not load / could not / was not saved" line (about 54 places, for example `Learn did not load`, `Key cards did not load`, `That rating was not saved. Try again.`, `Chapter feeds did not load.`) | X did not load. / X was not saved. | X didn't load. / X wasn't saved. | Contractions read warmer and faster, and the product already mixes them ("You've", "won't", "It's all saved"). Use one style. |

## Rules applied

1. **One word for one thing, on web and app.** "Session" for a student's sitting, never "run". Learn and Key cards share "Turn over",
   "Missed it / Got it / Easy", "How well did you know it?", "card ratings", "Study again", "part of Pro", "chapter sheet" and "That was today's free
   session." When a word changes, it changes in `words.js` and `learn_words.dart` together, with the parity test.
2. **The middle dot means a length and nothing else.** "Continue · 6 min" stays. Every other "A · B" becomes a comma, a colon or two sentences
   (owner standard 7, T-124).
3. **No idioms or build words a first-time CBT student must decode.** Out go "lined up", "lining up", "run", "steps", "activity recorded",
   "usable answer key", "certify", "submission/publication", "nothing is scheduled", "keeps them on a schedule" and "marks open". Each becomes what
   the student sees or gets.
4. **Say who and what.** Replace a vague "this", "it", "there", "ones", "things" or "what you kept" with the noun ("the cards you kept", "in
   Revise", "the length").
5. **Warm, short and natural.** Use contractions (didn't, you're, it'll, that's). Give the subject and verb first. Use one idea per sentence. Keep
   it to 2 sentences at most on a line under a key.
6. **Every fact stays.** Counts, limits (10 ratings, 5 new cards, 10-minute Free sessions), the order of returns (Missed it soonest, Easy
   furthest), what is saved and what Pro opens are all unchanged. Where a rewording would need a fact confirmed, the row says so (rows 46, 69, 89).
7. **The product's spelling and house style.** Indian/British spelling (practise as the verb, organise, colour). Sentence case. No exclamation marks,
   no hype, no arrows on keys. "Key cards", "Must-know", "Revise", "Pro" and "Free" keep their capitals. Times stay "N min" after a key.
8. **Errors name the next step** ("Connect to the internet to start this chapter", "Try the next one"), and they say the work is safe when it is.
