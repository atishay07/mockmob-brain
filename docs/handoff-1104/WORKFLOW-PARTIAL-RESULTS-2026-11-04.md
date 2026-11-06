# Partial results of the two workflows stopped at about 2:30 am IST, 4 Nov 2026 (account switch)

Extracted from their journals. A completed agent shows its full returned value; a started agent with no result was stopped mid-work.

## Workflow wf_24f47ca0-fd6

### launched (launched)

```json
{
 "type": "launched"
}
```

### review: release-safety (result)

```json
{
 "findings": [
  {
   "id": "release-safety-1",
   "title": "Release commit still declares version 1.0.19+17, so the versionCode is the one Play already holds",
   "severity": "medium",
   "file": "flutter_app/pubspec.yaml",
   "line": 19,
   "claim": "At 6079162d5 the pubspec still says `version: 1.0.19+17`. That is the versionCode of the previous release, cut in 06b65ff46 \"Version 1.0.19+17\". No commit in 06b65ff46..6079162d5 bumps it: the range's only pubspec change is the new `- assets/art/icons/` line. android/app/build.gradle.kts reads `versionCode = flutter.versionCode`, so a bundle built from this commit carries versionCode 17 and versionName 1.0.19, not the planned 1.0.20+18.",
   "failureScenario": "There are two ways this goes wrong. (1) The owner builds 6079162d5 as committed, with `bash tool/build_release_aab.sh` and no `--bump`, or with `flutter build appbundle` and no `--build-number`. The AAB has versionCode 17 and Play Console refuses the upload because version code 17 is already used. (2) He uses the script's `--bump` alone. tool/bump_version.py keeps the name unless `--name` is given, so the build becomes 1.0.19+18. The planned 1.0.20 name is lost: You > Help and the hub show \"1.0.19 (18)\", the Play release is named 1.0.19, and analytics and error reports tag this new build with app_version 1.0.19, the same as the previous release. No student gets a broken build, but the upload is blocked or ships with the wrong version name.",
   "evidence": "`git show 6079162d5:flutter_app/pubspec.yaml` line 19 is `version: 1.0.19+17`, the same as at 06b65ff46. `git log -- flutter_app/pubspec.yaml` shows the last version change is 06b65ff46 \"Version 1.0.19+17\"; 8a3b30cdd only adds the icons asset line. Earlier releases each had their own version commit (f72207c27 \"Version 1.0.18+16\", 06b65ff46). In tool/bump_version.py, without --name the code goes up by one and the name is kept (`name = f\"{major}.{minor}.{patch}\"`). tool/build_release_aab.sh only bumps when passed `--bump`, and only renames with `--name`. android/app/build.gradle.kts:47 has `versionCode = flutter.versionCode`. Nothing else in my area turned up a defect: no android/ or pubspec.lock changes and no new packages; all 9 BrandIconName files exist under the newly declared assets/art/icons/; no added debugPrint, assert, kDebugMode, localhost, LAN or preview URLs, analytics calls, or imports of test/ or device_demo code in lib/; the PLAY_BILLING gating is unchanged (plan strip still checks playBillingEnabledProvider before showGetProSheet).",
   "suggestedFix": "Before building, make the release's version commit with `python -I tool/bump_version.py --name 1.0.20` (1.0.19+17 becomes 1.0.20+18), or build with `bash tool/build_release_aab.sh --bump --name 1.0.20`. Then confirm the script prints \"Building MockMob 1.0.20+18 (versionCode 18)\"."
  }
 ]
}
```

### verify(trace): release-safety-1 (result)

```json
{
 "real": true,
 "severity": "low",
 "reasoning": "I checked every factual claim in the report against the code, and each one holds.\n- `git show 6079162d5:flutter_app/pubspec.yaml` has `version: 1.0.19+17`.\n- `git log 06b65ff46..6079162d5 -- flutter_app/pubspec.yaml` lists only 8a3b30cdd, the LK60 icons commit. The last version change is 06b65ff46 \"Version 1.0.19+17\". Earlier releases each had their own version commit (f72207c27, 06b65ff46).\n- `android/app/build.gradle.kts` lines 47-48 read `versionCode = flutter.versionCode` and `versionName = flutter.versionName`.\n- `tool/build_release_aab.sh` calls `bump_version.py` only with `--bump`. Without it, the build uses the version in pubspec as committed and prints \"Building MockMob 1.0.19+17 (versionCode 17)\".\n- `bump_version.py` without `--name` keeps the name (`name = f\"{major}.{minor}.{patch}\"`) and adds one to the code. So `--bump` alone gives 1.0.19+18, not the planned 1.0.20+18.\n- HEAD of the worktree is 6079162d5, so no later version commit exists.\n\nWhy low rather than medium: nothing reaches students. In case (1), Play Console refuses versionCode 17 at upload time with a clear duplicate-version error, and the fix takes seconds. In case (2), the build installs and works, but You > Help, the Play release name and analytics show 1.0.19 instead of 1.0.20, so the new build is mixed up with 1.0.19 in reports. This is a missing step before release, not a code defect. The script's own header says \"--bump ... (every upload needs this)\", and earlier releases made the version bump a separate last commit. It is still worth fixing before the owner builds, because the brief says he uploads this branch straight to Play.\n\nWhat would make it moot: a version commit to 1.0.20+18 made after 6079162d5, or the owner building with `--bump --name 1.0.20`.",
 "fixHint": "In C:/Users/atish/Desktop/mockmob copy/wt-1103-app-rel/flutter_app run `python -I tool/bump_version.py --name 1.0.20`, which changes 1.0.19+17 to 1.0.20+18. Commit it as \"Version 1.0.20+18\", following f72207c27 and 06b65ff46. Then run `bash tool/build_release_aab.sh` with no `--bump`, so the code does not go up again to 19. Check that it prints \"Building MockMob 1.0.20+18 (versionCode 18)\". The one-step alternative is to build with `bash tool/build_release_aab.sh --bump --name 1.0.20` and commit the pubspec change it leaves behind."
}
```

### review: topbar-icons (result)

```json
{
 "findings": []
}
```

### review: english-parity (result)

```json
{
 "findings": [
  {
   "id": "english-parity-1",
   "title": "The ratings coach line says \"Got it, in a few days\" right under a Got it key that says \"back in 3 weeks\"",
   "severity": "medium",
   "file": "flutter_app/lib/features/learn2/data/learn_words.dart",
   "line": 33,
   "claim": "The English pass rewrote LearnWords.coachRatings. The round-5 line only compared the keys (\"Missed it brings a card back soonest. Easy sends it furthest away.\"), which is true for every card. The new line gives fixed times: \"How well did you know it? Missed it brings the card back soon. Got it, in a few days. Easy, much later.\" The server works out each key's words from the card's stored FSRS state (learn.js returnsOf: schedule(state, rating)). For any card that already has a schedule, which is any due card, Got it is weeks away, not a few days. RunController shows this line through RunCopy.coachRate (run_copy.dart:65, run_controller.dart:350) under the three keys that print the server's words, so the screen contradicts itself. The coach id is new in this release ('ratings3'; 1.0.19 used 'rate2'/'rate2b'), so every existing student sees it once after updating.",
   "failureScenario": "A returning student updates to 1.0.20+18 and taps Start · 10 min on Learn home (the server puts due cards first), or starts a Revise due-cards session. On the first card they Turn over, the keys read \"Got it / back in 3 weeks\" and \"Easy / back in 5 weeks\" (the recorded server answer run_start_mix_pf_pro.json, item 1, stage due). Directly under them the coach says \"Got it, in a few days. Easy, much later.\" This is the one line that explains the keys, it shows once, and it is wrong. A brand-new student's first card is new (got 'in 3 days'), so the problem hits existing and returning students.",
   "evidence": "Checked at 6079162d5 (worktree clean; I edited nothing). I pumped the real LearnRunScreen with the harness (pumpRun with FixtureLearnApi, 360x800, light theme, first card turned) from a scratch test outside the repo: C:\\Users\\atish\\AppData\\Local\\Temp\\claude\\C--Users-atish-Desktop-mockmob-copy\\c5a8da45-5c74-46ba-abca-73f6160b75cd\\scratchpad\\fluttercheck\\run_screen_probe_test.dart. Screenshot at text 1.0: ...\\scratchpad\\fluttercheck\\run_session_100.png shows 'Got it back in 3 weeks', 'Easy back in 5 weeks' and under them 'How well did you know it? Missed it brings the card back soon. Got it, in a few days. Easy, much later.' In the recorded answers, due cards carry got 'in 3 weeks' / easy 'in 5 weeks' and new cards carry got 'in 3 days' / easy 'in 8 days'. The web's WORDS.coachRatings (data/learn/words.js on origin/main) has the same text, so the website has the same contradiction.",
   "suggestedFix": "Go back to a relative line that is true for every card (for example \"How well did you know it? Missed it brings the card back soonest, Easy furthest away. Each key says when.\"). Change data/learn/words.js and LearnWords.coachRatings together and regenerate words.json."
  },
  {
   "id": "english-parity-2",
   "title": "The Missed it key's second line is cut to \"back in this session, then tomo…\" at 360 dp with text 1.3",
   "severity": "low",
   "file": "flutter_app/lib/features/learn2/run/run_parts.dart",
   "line": 364,
   "claim": "The English pass changed missedWords from \"in this run, then …\" to \"in this session, then …\". That web change is in production (origin/main, learn.js returnsOf). The server sends it as returns.missed for nearly every rateable card on its first showing. RunRateKeys lays each key's second line in (width-16)/3-16 dp (88 dp on a 360 dp phone) and caps it at _subLines = 3 with an ellipsis (stage_keys.dart:510). At text scale 1.3, \"session, then\" (about 90.7 dp) no longer fits next to the word before it, so the text needs 4 lines and the return day is cut. The old words fit in 3 lines. The golden that holds this case (run_card_revealed_text13, whose comment says \"no label cut\") still plays the recorded pre-pass answers (\"in this run, then tomorrow\"), so it cannot see the problem.",
   "failureScenario": "A student has a 360 dp phone (a common 720p budget phone) with Android font size set to 1.3. They start any chapter or Revise session and Turn over a card. The Missed it key reads \"back in this / session, / then tomo…\", so the key no longer says when the card comes back, on almost every card. Phones 390 dp and wider and text 1.0/1.15 are not affected.",
   "evidence": "Flutter probes from the scratchpad (repo untouched). The probe C:\\Users\\atish\\AppData\\Local\\Temp\\claude\\C--Users-atish-Desktop-mockmob-copy\\c5a8da45-5c74-46ba-abca-73f6160b75cd\\scratchpad\\fluttercheck\\rate_keys_probe_test.dart lays out RunActionBar(RunRateKeys) with the app fonts. At 360 dp and 1.3, 'back in this session, then tomorrow' has paraWidth 88 and didExceedMaxLines=true; 'back in this run, then tomorrow' gives false; at 390 dp both give false. The probe run_screen_probe_test.dart on the real run screen with the recorded run rewritten to the live words gives the same result (exceeded=true only for session at 1.3). Screenshot: ...\\scratchpad\\fluttercheck\\run_session_130.png shows 'back in this / session, / then tomo…'. Font-metric check (HankenGrotesk-Medium 12sp, GPOS kerning, x1.3): 'session, then' = 90.67 dp > 88. Side note: the 1-line stamp 'Back in this session, then tomorrow' still fits at 1.3 but is cut at 1.5 on 360 dp, where the old wording fit.",
   "suggestedFix": "Raise RunRateKeys._subLines to 4 (keyHeight already measures with the same constant), or shorten the server's Missed words. Re-record the run fixtures from the live server so the text-1.3 golden covers the real words."
  },
  {
   "id": "english-parity-3",
   "title": "The Last look end key now says \"Study again\" but restarts Last look, not Study",
   "severity": "low",
   "file": "flutter_app/lib/features/keycards/widgets/key_card_run.dart",
   "line": 265,
   "claim": "Row 79 of the English pass renamed the shared KeyCardsCopy.studyAgain from 'Go through again' to 'Study again' (keycards_copy.dart:93). KcLastLook's end reuses that constant for its own restart key: KeyButton.secondary(label: KeyCardsCopy.studyAgain, onPressed: () => setState(() => _at = 0)). That key only replays the Must-know cards in Last look, with no ratings and nothing scheduled. On the same screen, 'Study' is a different mode in the segmented control (Read / Study / Last look). The label now names the wrong mode. The website's Last look end says 'Look again' (ChapterDeck.jsx LastLookMode on origin/main).",
   "failureScenario": "A student opens a chapter's Key cards, picks Last look and swipes to the end: 'That was every Must-know card in this chapter.' with the key 'Study again'. They tap it expecting a Study session (rating the cards toward Revise). Instead they get Last look card 1 again, with 'Must-know cards only. This won't change when your cards come back.', and the segmented control still on Last look. No cards are rated.",
   "evidence": "key_card_run.dart:265 in KcLastLook uses KeyCardsCopy.studyAgain; keycards_copy.dart:93 has studyAgain = 'Study again' (was 'Go through again' at 06b65ff46). keycards_deck_screen.dart:295/316 shows Last look as its own mode next to Study. Web origin/main src/components/keycards/ChapterDeck.jsx LastLookMode end key: 'Look again'.",
   "suggestedFix": "Give Last look its own label (for example KeyCardsCopy.lookAgain = 'Look again', the web's word) and keep studyAgain for the Study end."
  }
 ]
}
```

### verify(trace): english-parity-3 (result)

```json
{
 "real": true,
 "severity": "low",
 "reasoning": "I traced this at 6079162d5 and the report holds. In keycards_copy.dart line 93, studyAgain is now 'Study again'. At 06b65ff46 it was 'Go through again'. KcLastLook's end state in key_card_run.dart lines 259-266 shows lastLookDone and then KeyButton.secondary(label: KeyCardsCopy.studyAgain, onPressed: () => setState(() => _at = 0)). That only sets the Last look index back to 0. It doesn't switch KcMode, rate anything or schedule anything. keycards_deck_screen.dart line 316 mounts KcLastLook for KcMode.lastLook. The deck's mode labels are Read / Study / Last look (keycards_copy lines 57-59). So the key names the Study mode but replays Last look, and the selector stays on Last look. Nothing is server-driven here: the label is a compile-time const, so a release build with real data shows the same thing. The KeyCardRun and study-end defaults (lines 32 and 187) do belong to Study, so 'Study again' is right there; Revise passes againLabel: null. Only the Last look end is wrong. Severity is low. It's a misleading label at the end of one mode. The action itself is harmless: no data loss, no crash, and it doesn't break Study, which the student can still pick from the selector. It matters only because the new English pass created the confusion and the web says 'Look again'. english_pass_test.dart line 58 checks only the constant's value, so the test suite won't catch the misuse.",
 "fixHint": "In flutter_app/lib/features/keycards/keycards_copy.dart, add `static const String lookAgain = 'Look again';` (the web's LastLookMode word). In key_card_run.dart line 265, change the KcLastLook end key to `KeyButton.secondary(label: KeyCardsCopy.lookAgain, ...)`. Keep studyAgain as the default for KeyCardRun and the Study end. In english_pass_test.dart, add `expect(KeyCardsCopy.lookAgain, 'Look again')`, plus a widget check that a finished KcLastLook shows 'Look again' and not 'Study again'."
}
```

### verify(trace): english-parity-2 (result)

```json
{
 "real": true,
 "severity": "low",
 "reasoning": "I could not refute this one. I traced it at 6079162d5 and checked the server on origin/main.\n\n**Where the words come from**\n- The server (origin/main `src/lib/server/learn.js:649`, `returnsOf`) sets `returns.missed = missedWords(words(1), !shown.has(item.cardId))`.\n- `data/learn/words.js:95` makes that `in this session, then ${scheduled}`.\n- So nearly every rateable card gets \"in this session, then tomorrow\" on its first showing.\n- The app takes these words as they are: `LearnReturns.tryParse` and `forRating(1)` in `learn_models.dart`, with the \"back \" prefix added by `LearnWords.backLine`. The client's own `missedWords` is not what feeds the key.\n\n**How the key lays out**\n- `RunRateKeys` (`run_screen.dart:617` sets `returns: it.returns`) lives in `RunActionBar`. Its padding is `MmSpace.gutter` on both sides, so the row is 328 dp wide on a 360 dp phone.\n- `keyHeight` and `StageStepKey` both use a slot of (328 - 2*8)/3 - 2*8 = 88 dp.\n- The second line is a `Text` with `maxLines: _subLines` (3), `softWrap: true` and `overflow: TextOverflow.ellipsis` (`stage_keys.dart:508-512`).\n\n**Text scaling**\n- The app does not cap text scale anywhere on this path. `withClampedTextScaling(maxScaleFactor: 1.2)` appears only in the bar, the live capsule and the start key, not the run screen.\n- So an Android font size of 1.3 reaches the 12 sp second line in full.\n- At that scale \"session, then\" (about 90.7 dp in HankenGrotesk Medium) is wider than the 88 dp slot. The text needs 4 lines, and the third is cut with an ellipsis.\n\n**Evidence**\n- The reporter's real-screen probe picture (`scratchpad/fluttercheck/run_session_130.png`) shows the Missed it key reading \"back in this / session, / then tomo…\".\n- The Got it and Easy keys are fine.\n- Flutter shapes text the same way in tests and on a device, and the font is bundled, so the 2.7 dp overflow will look the same on a real phone.\n- The text-1.3 golden still plays recorded \"in this run\" answers, so it cannot catch this.\n\n**Why low**\n- Nothing crashes and no data is lost.\n- It only happens on phones about 360 dp wide with a font size of 1.3 or more.\n- The full words are still in the key's screen-reader label (`semanticsLabel`), and the hint under the keys still says Missed it brings the card back soon.\n- But on that common budget-phone setup it hits almost every card on its first showing.",
 "fixHint": "In `flutter_app/lib/features/learn2/run/run_parts.dart`, change `RunRateKeys._subLines` from 3 to 4. `keyHeight` lays out its `TextPainter` with the same `_subLines`, so all three keys grow to the same height together. After that:\n- Check the run screen's key area at 360 dp with text 1.3 and 1.5 so the taller keys don't crowd the card.\n- Re-record the run fixtures from the live server, or rewrite their `returns.missed` to \"in this session, then …\", so the `run_card_revealed_text13` golden covers the real words.\n\nThe other way out is shorter server words, such as \"this session, then tomorrow\". But `learn.js` and `words.js` would have to change, and those are in production."
}
```

### review: explore-learn-calm (result)

```json
{
 "findings": [
  {
   "id": "explore-learn-calm-1",
   "title": "The Explore door stays on the subject of the first link that opened it, for the whole session",
   "severity": "medium",
   "file": "flutter_app/lib/features/learn2/explore/explore_screen.dart",
   "line": 114,
   "claim": "ExploreScreen reads the link's ?subject= into _linked only once, in initState (lines 72-79). It never revisits or clears it: there is no didUpdateWidget, and only a tap on a chip inside Explore clears it. Line 114 (`_linked ?? ref.watch(practiceSubjectProvider)`) short-circuits, so once _linked is set the shared subject is not even watched. In this release Explore became an embedded Practice door (practice_screen.dart:613). PracticeDoorStage (door_stage.dart:68-79) keeps every door it has built alive offstage, and /practice and /practice?door=explore&subject=... share one page key. So one ExploreScreen state now lives for the whole app session, and the first link's subject overrides every later subject change and every later link's subject.",
   "failureScenario": "A student takes Accountancy and Economics, with Accountancy as the current subject. On Practise > More ways in they tap \"Chapter feeds\". learn2_door.dart:74 goes to /practice?door=explore&subject=accountancy, the door is built for the first time, and _linked becomes 'accountancy'. They switch to the Practise door, pick the Economics chip, then tap \"Chapter feeds\" again (/practice?door=explore&subject=economics) or the Explore door in the switch. Explore still shows the Accountancy chip selected, \"Accountancy chapter feeds\" covers, and a Questions entry that opens Accountancy questions. Pulling to refresh reloads the Economics covers (practice_screen.dart:186), not the ones on screen. The same happens after Learn home's \"Answer single questions\" row (learn_home.dart:248, which passes the subject) followed by Learn's subject picker. An App Link or reminder for /explore?subject=x is also ignored once the door has been built.",
   "evidence": "explore_screen.dart:72-79 handles widget.subject only in initState, and line 114 prefers _linked. door_stage.dart:68-79 keeps built doors in an Offstage/TickerMode subtree with a constant key per door. go_router 17.5 builds pageKey from the matched path (match.dart:231), so the PracticeScreen state survives query changes. FadingBranchContainer keeps every tab branch alive. In 1.0.19, /explore was a pushed standalone page, created fresh on each open, so the link's subject always applied. practice_explore_door_test.dart has no test that changes the subject.",
   "suggestedFix": "Treat the link as a one-shot handoff. After the post-frame select(linked), set _linked = null (or clear it as soon as practiceSubjectProvider equals it), and add didUpdateWidget so that a new non-null widget.subject is selected the same way. The Explore door then always follows the shared subject, and every link with ?subject= takes effect."
  },
  {
   "id": "explore-learn-calm-2",
   "title": "Feed checkpoint says \"8 of 16 done\"; its Stop here leads to an end saying \"1 of 16 done\" (or no done line)",
   "severity": "medium",
   "file": "flutter_app/lib/features/learn2/feed/feed_screen.dart",
   "line": 695,
   "claim": "The round-5 change (LK45 fix 2) moved the stopped feed end to the server's count: `stopped ? math.min(of, c.itemsDone)`, which is the place of the last kept card or answered question. The checkpoint page, whose \"Stop here\" key (line 433) leads straight to that end, still counts by position (`done: c.base + after`, line 534). So a single stop shows two different numbers one tap apart. In 1.0.19 the stopped end used `c.base + c.furthest`, which matched the checkpoint.",
   "failureScenario": "Take the 16-item feed from FixtureLearnApi (as in feed_screen_test). Keep card 1 (\"Revise later\"), turn cards 2-8 without keeping, and reach the checkpoint after item 8. It shows \"1 for Revise\" and \"8 of 16 done, about N min left.\" Tap \"Stop here\": the end's headline reads \"1 of 16 done\". If the student kept nothing and answered nothing, the end shows no done headline at all, because endHeadline returns null for 0, right after the checkpoint said \"8 of 16 done\". This happens in every feed long enough for a checkpoint (8 items with at least 4 after).",
   "evidence": "feed_screen.dart:534 uses `checkpointText(n, done: c.base + after, ...)`. feed_screen.dart:695 uses `reached = ... stopped ? math.min(of, c.itemsDone) : of`. FeedModel.itemsDone (feed_model.dart:395) counts only kept cards and answered questions, so turned cards count for nothing. feed_screen_test.dart:211-218 asserts \"8 of 16 done\" at the checkpoint with one card kept, and 229-238 never checks the end's headline. The web's ChapterFeed.jsx:684 has the same split.",
   "suggestedFix": "Use one rule for both screens. Either pass `done: c.itemsDone` (capped at of) into the checkpoint line, which matches the server and the stop sheet, or word the checkpoint's line so it is not a done count. Add a test that taps the checkpoint's Stop here and checks the end's headline."
  },
  {
   "id": "explore-learn-calm-3",
   "title": "After resuming a run, the stop sheet undercounts compared with the end (\"4 of 12 done\" vs \"5 of 12 done\")",
   "severity": "low",
   "file": "flutter_app/lib/features/learn2/run/run_controller.dart",
   "line": 299,
   "claim": "doneCount now uses StageEndModel.reachedPlace(_items, held, offset), which treats offset as a prefix of finished items (its own doc says \"a resumed run's prefix\"). On resume, offset comes from resumed.done (line 485). The server sets that to the number of items holding events, and it re-serves the items without events, including a question skipped before a later answered item. So the done items are not a prefix. The end screen uses the server's done.reached, the highest place of any event (run_end.dart:79), so the two disagree. The LK45 fix 2 rewrite was meant to make them equal, but it does not hold for resumed runs.",
   "failureScenario": "In a 12-item run: rate card 1, rate card 2, Skip question 3, answer question 4, rate card 5, then Close and Stop here. The end says \"5 of 12 done\" and the two agree. Later the student taps \"Continue\". The server returns items [Q3, 6..12] with resumed.done = 4, so offset = 4. The student presses Close at once, or skips Q3 again. The stop sheet says \"4 of 12 done. It's all saved.\"; after Stop here the end headline says \"5 of 12 done\".",
   "evidence": "run_controller.dart:297-304 computes doneCount as reachedPlace(..., offset), and line 485 sets `offset = r.resumed?.done ?? 0`. run_screen.dart:354 passes that to the stop sheet. Server learn.js (web 4b5f67e34) runBody filters row.items by event item ids and sets resumed.done = row.items.length - items.length. runDone sets reached = max(places.indexOf(e.item_id)+1) over all events. run_end.dart:79 prefers d.done.reached. The previous `offset + finished` had the same gap.",
   "suggestedFix": "On resume, keep the server's reached place: have the run body send resumed.reached, or keep each remaining item's original place. Then use max(priorReached, place of the last held item) for doneCount, so the sheet always reads what the end will."
  }
 ]
}
```

### verify(trace): english-parity-1 (result)

```json
{
 "real": true,
 "severity": "medium",
 "reasoning": "I couldn't refute it. The coach line contradicts the keys above it for any card that already has a schedule.\n\n1. **The line.** At 6079162d5, `LearnWords.coachRatings` (learn_words.dart:33) reads \"How well did you know it? Missed it brings the card back soon. Got it, in a few days. Easy, much later.\" `RunCopy.coachRate` points to it (run_copy.dart:65). `RunController.statusLine` (run_controller.dart:350) shows it when `_coachShow('ratings3')` is true.\n\n2. **When it shows.** `_coachWanted('ratings3')` is true on any turned, non-look card whose `returns` is not null. It is not limited to new cards, and it shows once per student.\n\n3. **The id is new.** `_coachIds` is `['front2', 'ratings3', 'pick', 'recap']`. The comment says `ratings3` replaces R2's `rate2`/`rate2b`, so every existing student sees it once after updating.\n\n4. **What the keys say.** The key words come from the server. In origin/main src/lib/server/learn.js, `returnsOf` reads each card's stored state. It uses that state only when `reps > 0` and a schedule exists, then computes `got: returnWords(schedule(state, 3, at).interval_days)` and `easy` the same way with rating 4.\n   - The scheduler (data/keycards.js) is ts-fsrs with retention 0.9 and no fuzz.\n   - `returnWords` (data/learn/words.js) prints \"in N days\" up to 13 days, then weeks, then months.\n\n5. **New card versus due card.** A new card gets about 3 days for Got it (\"in 3 days\"), so the line is true there. A due card already has stability, so its Got it interval is several times that.\n   - My own rough FSRS estimate for a second review is about 10 to 11 days. Later reviews run to weeks.\n   - The recorded fixture flutter_app/test/fixtures/learn2/run_start_mix_pf_pro.json has a due item with got \"in 3 weeks\" and easy \"in 5 weeks\". Its new items have \"in 3 days\" and \"in 8 days\".\n\n6. **Result.** A returning student whose first rated card is due sees \"Got it / in 3 weeks\" with \"Got it, in a few days\" under it. This applies to any Revise due-cards run, and to a mixed run that starts with a due card.\n\n**Limit.** The only thing that would make it unreachable is if no rateable due card ever comes first in a run. Revise due-card runs rule that out, because every card in them is due.\n\n**Severity: medium.** It is a visible, factually wrong sentence on a common path for returning students. It shows only once, the keys themselves are correct, and nothing breaks or is lost. So it is not high.",
 "fixHint": "Replace `LearnWords.coachRatings` (flutter_app/lib/features/learn2/data/learn_words.dart:33) and the web's `WORDS.coachRatings` (data/learn/words.js) with a line that compares the keys and is true for every card. For example: \"How well did you know it? Missed it brings the card back soonest, Easy furthest away. Each key says when.\" Change both together, regenerate words.json so the app-web parity test passes, and update any test or golden that pins the old text. The coach id `ratings3` does not need a bump, because it is not in any released build yet."
}
```

### review: sending-strip (result)

```json
{
 "findings": [
  {
   "id": "sending-strip-1",
   "title": "The settler settles an owed paper and cancels its backup job, but the pinned \"Sending Mock N\" notification is never cleared",
   "severity": "medium",
   "file": "flutter_app/lib/core/sync/session/stale_submit_settler.dart",
   "line": 127,
   "claim": "When StaleSubmitSettler resolves an owed draft (SubmitReceived, SubmitWindowClosed or SubmitRejected at lines 96 and 119), `_settled` cancels the WorkManager submit job (line 127). Nothing in the settler touches the shared `mock_in_progress` status notification. Only two things ever replaced or cleared the pinned \"Sending\" status: a live engine (onResumed/submit outcome) or that backup job (postResultReady/postSendEnded). After a process death, the LK50 settler takes the job's place and leaves the pinned \"Sending\" notification up for good, which is the LK50 symptom moved into the notification shade.",
   "failureScenario": "1. A student taps Submit on Mock 3. The POST fails on a dropped signal and the submit goes pending. 2. The student presses Home on the submit page. SessionEngine.onPaused posts the ongoing notification \"Sending Mock 3 / Your answers are on this phone and are being sent.\" (ongoing:true, autoCancel:false) and queues the job. 3. Android kills the process, or the student swipes the app away. 4. Later the student reconnects and opens the app before WorkManager has run the job. 5. On start the settler either POSTs (window open), gets SubmitReceived and deletes the draft, or GETs /api/attempts/{id} (past the window) and marks the draft received or windowClosed. In every case `_settled` then cancels the job. 6. No engine exists to call status.clear(). The cancelled job never posts \"Result ready\" or \"Mock 3 not recorded\". A job that still ran would return at `draft == null` without touching the notification. Result: the shade keeps saying the answers are being sent while the app shows the result or the not-recorded copy. On Android 13 and below the notification cannot be swiped away. It stays until another mock's runner reuses the id or the student signs out. Before LK50 the job would have run and replaced it.",
   "evidence": "stale_submit_settler.dart:87-131: no status or notification handling, and `_settled` calls scheduler.cancelSubmit. session_engine.dart:625-626 posts showSending on pause while a submit is unreceived. session_engine.dart:639/720/731 are the engine's only clears. background_tasks.dart:113 returns true when the draft is gone, without touching the status. background_tasks.dart:116/146/153/156/161: the job settles the status (cancel, postResultReady, postSendEnded). session_notifications.dart:27-36 and 72-80. notification_gateway.dart:162-163 sets `ongoing: ongoing, autoCancel: !ongoing`. grep finds no other code that cancels mockInProgressTaskId at startup.",
   "suggestedFix": "After a non-pending outcome in `_settleOne`, settle the status as runSubmitSessionTask does. Unless SessionHeartbeat.anotherIsLive(sessionId) is true, cancel mockInProgressTaskId on SubmitReceived and call postSendEnded(windowClosed or rejected) for the other outcomes. Inject the NotificationService or SessionStatusNotifier from sessionEngineServicesProvider."
  },
  {
   "id": "sending-strip-2",
   "title": "The past-window branch trusts the phone's wall clock and closes a paper the server would still accept, without ever POSTing it",
   "severity": "low",
   "file": "flutter_app/lib/core/sync/session/stale_submit_settler.dart",
   "line": 89,
   "claim": "`_settleOne` decides the window is closed by comparing `_now()` with `draft.endsAtWallMs + 120 s`. endsAtWallMs is a wall-clock estimate fixed when the session view arrived (session_clock.dart:46). The branch then only GETs the attempt. A 404 makes `_afterExpiry` save `windowClosed: true, pendingSubmission: false` (session_submitter.dart:193), and `_settled` cancels the backup job. That job would have POSTed regardless of the local clock (background_tasks.dart:137) and let the server decide. A forward wall-clock correction after the paper started therefore drops a submit that the server would still accept.",
   "failureScenario": "1. The phone's clock is 5 minutes slow when an Economics practice set (ticket mode, so the server holds no answers) starts. 2. The student submits with 10 minutes left while offline, and the submit goes pending. 3. The phone then syncs network time, and the clock jumps forward 5 minutes. 4. The student reopens the app online with 2 minutes left on the server's clock. 5. Local now is past endsAtWallMs + 120 s (that point is 3 minutes before the true deadline), so the settler takes the past-window branch. 6. GET /api/attempts/{id} returns 404. The draft is set windowClosed and the job is cancelled (it would also stop on windowClosed at background_tasks.dart:115). The runner loader refuses windowClosed drafts (runner_loader.dart:87). Result: the server would have accepted a POST for about 4 more minutes, but every answer of the set is never sent. For a durable mock, every unacknowledged answer is lost. Before LK50 the job POSTed and the server accepted it.",
   "evidence": "stale_submit_settler.dart:88-97 makes the window decision from the local clock and goes straight to settleAfterWindow. session_submitter.dart:179-194: settleAfterWindow is GET-only, and a 404 sets windowClosed. session_clock.dart:38-47: endsAtWall = receivedWall + remaining, so it carries the wall clock as it was at anchor time. background_tasks.dart:115 and 137: the job POSTs without a local window check, and stops once windowClosed is set. The server judges its own clock: practiceSessions.js finishPractice and recoverySessions.js:113 check `Date.now() > expires_at + 120000`.",
   "suggestedFix": "In the past-window branch, call submitter.submit first. It already falls back to GET on SESSION_EXPIRED, so only the server's SESSION_EXPIRED plus a 404 closes the paper. Alternatively, do not cancel the job and do not mark the draft windowClosed from a local-clock verdict alone."
  },
  {
   "id": "sending-strip-3",
   "title": "Settling a stale draft rewrites it as the newest draft, which hides a newer unfinished paper's Resume",
   "severity": "low",
   "file": "flutter_app/lib/core/sync/session/stale_submit_settler.dart",
   "line": 92,
   "claim": "The settler's window-closed write goes through `_tryDraftSave`, `saveIfOwned` and `save`. For a row that is not an archive row, `save` stamps `updatedAtMs = now` (session_draft_repository.dart:39). latestSessionDraftProvider and watchLatest order drafts by updatedAtMs (session_draft_repository.dart:173-180). An old stale paper settled by LK50 therefore jumps ahead of a newer running paper. Today's resume hero and the bar's Resume capsule both read only that latest draft.",
   "failureScenario": "1. A student carries the LK50 state: Accountancy mock M, pending, ended yesterday, in its own selection row. 2. The student also has an Economics practice P half done with 15 minutes left. P is the latest draft, so Today shows Resume for P and the bar shows the Resume capsule. 3. On the next start or resume, the settler GETs M and gets 404. M is saved windowClosed with updatedAt = now and becomes the latest draft. 4. todayDraftProvider, _resumeOrEnded (today_builder.dart:276-299) and resumeDraftProvider (quick_start.dart:50-53) now read M, which has ended and cannot resume. 5. P's Resume hero and Resume capsule disappear. OpenPaperResolver.offer returns null because P is a running draft (open_paper.dart:69). 6. P stays on the phone unoffered until its backup job submits the partly answered paper about 90 s before its deadline. Before LK50 nothing wrote M after its job stopped, so P stayed the latest draft.",
   "evidence": "stale_submit_settler.dart:92 calls settleAfterWindow. session_submitter.dart:193 calls _tryDraftSave(copyWith(windowClosed)). session_draft_repository.dart:39: `updated = isArchiveKey(...) ? draft.updatedAtMs : now`. session_draft_repository.dart:160-181: latest is ordered by updatedAtMs desc. today_builder.dart:276-278 builds ResumeHero only from i.draft. quick_start.dart:50-53: resumeDraftProvider reads the latest draft only.",
   "suggestedFix": "When the settler marks a past-window draft windowClosed, keep its stored updatedAtMs, for example by archiving it or by giving `save` an option to keep the timestamp. A settle should never make an old paper the latest draft."
  }
 ]
}
```

### verify(trace): explore-learn-calm-2 (result)

```json
{
 "real": true,
 "severity": "medium",
 "reasoning": "I traced the code at 6079162d5 and the report holds.\n\n**Checkpoint count.** `feed_screen.dart:534` builds the checkpoint with `checkpointText(n, done: c.base + after, ...)`. `StageEndModel.checkpointLines` turns that into \"${done} of ${of} done, about N min left.\", so it counts by position. For cp-8 in a 16-item feed with base 0 it reads \"8 of 16 done\", whatever the student did.\n\n**Stop here.** The checkpoint's \"Stop here\" key (line 433) calls `c.stopHere()` directly. That sets `_stopping` and `stoppedHere`, then `go(endAt)`. There is no stop sheet on this path.\n\n**End count.** The end is not end-only here (`onlyEnd` is false), so line 695 takes `reached = stopped ? math.min(of, c.itemsDone) : of`. `c.itemsDone` is `FeedModel.itemsDone`, which is `StageEndModel.reachedPlace` with `held = card ? st.kept : st.res != null`. It returns base + (index of the last kept card or answered question) + 1. A card that was only turned over counts for nothing. The server's reply does not change this number for a feed in progress.\n\n**The reported case.** Card 1 kept and cards 2-8 only turned: the checkpoint shows \"1 for Revise\" / \"8 of 16 done...\". After Stop here, `endHeadline(reached: 1, of: 16, stopped: true)` gives \"1 of 16 done\". With nothing kept or answered, `itemsDone` is 0 and `endHeadline` returns null because `r == 0`, so there is no done line at all, one tap after \"8 of 16 done\".\n\n**Regression.** At 06b65ff46 (1.0.19), line 688 used `math.min(of, c.base + c.furthest)`, which matched the checkpoint's position count. The round-5 LK45 change moved the end and the Close stop sheet (line 265, `math.min(c.itemsDone, c.of)`) to the server's rule but not the checkpoint. The doc comment on `reachedPlace` says one moment should never read two numbers, and this path breaks that.\n\n**Severity: medium.** Nothing crashes and no data is lost. The server holds the right state. But it is a visible contradiction on a common path: any feed with 12 or more items reaches a checkpoint, and Stop here is one of its two main keys. It is worst for students who mostly turn cards, which is what a feed is mostly for.",
 "fixHint": "Use one count for both screens.\n\n1. **Change.** In `feed_screen.dart` `_page`, `FeedCheckpointSlot` case, replace `done: c.base + after` with `done: math.min(of, c.itemsDone)`, the same count the Close stop sheet and the stopped end use. That makes all three agree. With nothing held, the line reads \"0 of 16 done\". The big number still leads with \"N cards seen\" because turned cards are `seen`, so the screen never leads with a zero. Keep `FeedCopy.checkpointLabel(c.base + after, of)` as it is. It is a place label, not a done count.\n2. **Alternative.** Reword the checkpoint line so it is not a done count, for example \"Item 8 of 16, about N min left.\"\n3. **Test.** Extend `feed_screen_test` to tap `end-cp-8` (the checkpoint's Stop here) and check that the end's headline matches the checkpoint's done count. Cover both the case with one card kept and the case with nothing held.\n4. **Web.** Make the same change in `ChapterFeed.jsx` (around line 684), and in the parity fixture if it asserts the checkpoint `done`, so the parity test still passes."
}
```

### verify(trace): explore-learn-calm-3 (result)

```json
{
 "real": true,
 "severity": "low",
 "reasoning": "I traced it at 6079162d5 and the bug is real. It is an edge case and only affects a number shown on screen.\n\nClient side:\n- run_controller.dart:296-304: while playing, doneCount returns StageEndModel.reachedPlace(_items, held, offset). That function (stage_end_model.dart:174) returns base + lastHeldIndex + 1, so it assumes the items done before resuming are a prefix of the run.\n- _adopt (line 485) sets offset = r.resumed?.done ?? 0.\n- RunView.itemHeld treats a question as held only when answered. skip() (line ~712) writes nothing to the server.\n\nServer side (src/lib/server/learn.js at 4b5f67e34):\n- runBody (670-690) drops every item that has an event and sets resumed.done = row.items.length - items.length, which is the number of items with events.\n- A skipped question that sits before a later answered or rated item is served again at index 0, so the done items are not a prefix.\n- runDone (1446-1451) sets reached = max over all events of (place + 1).\n- run_end.dart:79 prefers d.done.reached whenever raw['done'] is present.\n\nThe reported scenario, worked through: 12 items. Events exist for 1, 2, 4 and 5 (Q3 was skipped, so it has none). reached = 5. On resume the server serves [Q3, 6..12] with done = 4, so offset = 4.\n- asksToStop is true because doneCount = 4 + (-1) + 1 = 4, which is above 0.\n- Close shows the stop sheet with \"4 of 12 done\" (run_screen.dart:354 passes min(doneCount, total) = 4).\n- Stop here calls finish(4). The end then shows reached = 5 from the server.\n\nWhen the numbers disagree: only while every held item in the resumed list is one of the re-served gap items, or nothing is held yet. Any item held past the gap maps to the correct place (index i gives offset + i + 1, which equals its original place). Skipping Q3 again, or answering only gap questions, keeps the undercount.\n\nSide effect: `position` (offset + at + 1) also labels the re-served Q3 as item 5 of 12.\n\nSeverity is low. It needs a question skipped before a later held item, then Stop, then Continue, then Close before passing the gap. Nothing is lost or crashes, and the sheet is off by the size of the gap. The older offset + finished had the same gap, so this is not a regression in 1.0.20.",
 "fixHint": "The client alone cannot know where the gap items sat in the original run, so the server has to send that. In runBody, add `reached` to the resumed object, computed with runDone's rule: max over events of (places.indexOf(e.item_id) + 1).\n\nIn the app:\n1. Parse resumed.reached into a field such as priorReached, falling back to offset when it is absent, so older servers keep today's behaviour.\n2. In doneCount while playing, return max(priorReached, reachedPlace(_items, held, offset)). This is exact because any held item past the gap already maps to its true place, and a held gap item is at most priorReached.\n3. Use the same max in feed_model.itemsDone if feeds can resume with gaps.\n\nOptional, for `position`: have publicItem carry each item's original place."
}
```

### verify(trace): explore-learn-calm-1 (result)

```json
{
 "real": true,
 "severity": "medium",
 "reasoning": "I traced this at 6079162d5 and the bug is real.\n\n1. explore_screen.dart sets `_linked` only in initState, from a valid `widget.subject`, plus a post-frame `select(linked)`. Only `_pickSubject` clears it, on a chip tap inside Explore. There is no didUpdateWidget. build() runs `final String practiceId = _linked ?? ref.watch(practiceSubjectProvider);`, so while `_linked` is set the provider is not even watched. The chips' `selected`, the \"X chapter feeds\" label, `learnCoversProvider(subject)`, cover taps and `StreamEntry(subject: practiceId)` all follow `_linked`.\n2. practice_screen.dart:613 builds `ExploreScreen(embedded: true, subject: GoRouterState.of(context).uri.queryParameters['subject'])` with no key. PracticeDoorStage keeps every door it has built in `_built` under a constant `KeyedSubtree(ValueKey('practice-door-body-explore'))`, inside Offstage/TickerMode. So the same `_ExploreScreenState` is reused and only receives a new widget.\n3. /practice is a `tabRoot` in a StatefulShellBranch, and `mmTabRootPage` uses `key: state.pageKey`. In go_router 17.5.0, match.dart:231 builds `pageKey: ValueKey<String>(newMatchedPath)`, which leaves out the query. So /practice, /practice?door=explore and /practice?door=explore&subject=economics share one page and one PracticeScreen state.\n4. Entry points: ChapterFeedsRow (learn2_door.dart) calls `context.go(Learn2Links.explore(subject: subject))`, which leads to `/practice?door=explore&subject=<current>`. Learn home's offer does the same with `learnSubjectIdProvider`. `/explore?subject=` redirects there too.\n\nThe failing path: the first visit to Explore through \"Chapter feeds\" sets `_linked` to the current subject (say accountancy). The student then picks Economics on the Practise door (the provider becomes economics) and opens Explore again, either from Chapter feeds with `subject=economics` or from the door switch. They get the old state, and `_linked` is still accountancy. Explore shows the Accountancy chip, the Accountancy covers and an Accountancy Questions entry. Pull to refresh on that door (practice_screen.dart:186) invalidates the provider's subject (economics), not the one on screen. This lasts until the student taps a chip inside Explore or the app restarts.\n\nThis needs no unusual data. It only needs a student with more than one subject (normal for CUET) who first enters Explore through a link that names a subject, which \"Chapter feeds\" always does, and who later changes subject elsewhere. It does not crash or lose data, but the wrong subject is shown on a common path. Medium is right.\n\nSettling test: a widget test that opens /practice?door=explore&subject=accountancy, goes to the Practise door, selects economics, opens /practice?door=explore&subject=economics, and expects the Economics chip to be selected. It would fail today.",
 "fixHint": "In explore_screen.dart, treat the link's subject as a one-shot handoff, not a lasting override.\n(a) In initState's post-frame callback, after `select(linked)`, do `if (mounted) setState(() => _linked = null);`. From then on build follows `ref.watch(practiceSubjectProvider)`. Better still, always call ref.watch(practiceSubjectProvider) in build and use `_linked` only as the first-frame fallback.\n(b) Add `didUpdateWidget(ExploreScreen old)`: when `widget.subject != old.subject` and the new subject matches `storedSubjectId`, run the same canonicalSubject plus post-frame `select()` path (set `_linked` for one frame if you want no flash, then clear it).\n(c) Add a test to practice_explore_door_test.dart for: link with subject A, change to subject B on Practise, open Explore again with subject=B and through the door switch; expect B selected and B's covers requested."
}
```

### review: cards-stage-run (result)

```json
{
 "findings": [
  {
   "id": "cards-stage-run-1",
   "title": "A Key card's front can't be scrolled, and the new band, foot and deck push more prompts under its fade",
   "severity": "low",
   "file": "flutter_app/lib/features/learn2/stage/card_face.dart",
   "line": 264,
   "claim": "The front's 'Turn over' tap target is an opaque GestureDetector inside a Positioned.fill that sits above the front face (card_face.dart:259-266). RenderStack stops hit-testing at the first child that reports a hit. So the front's own SingleChildScrollView (_FaceState, line 343) never gets a touch, and a front taller than the card is cut off at its foot under the 44 dp fade. The back avoids this because it puts a translucent GestureDetector around its scroll view (line 357). The block itself is already in 1.0.19. What this release adds is more chrome: about 10 dp above the prompt (the 48 dp band replaces the 18 dp kind line and 20 dp padding) and about 32 dp below it (34 dp under the prompt plus a 48 dp source foot). RunDeck also takes 14 dp off a run's card (run_parts.dart:577). As a result, more fronts now spill past the card.",
   "failureScenario": "(a) Phone at 360x640 dp with a 28 dp status bar and a 24 dp gesture bar, Android font size 1.3, a Learn run, on the key_line card 'If the revaluation account finally shows a ____ then it indicates net gain and if there is a debit balance then it indicates ____.' (fixture cards_aop_all_pro.json). The prompt is 8 lines of 33.8 sp at 38.9 dp each. Its last line, which holds the second blank, now ends about 373 dp down a card about 383 dp tall, so it sits mostly under the paper-coloured fade (77% opaque at its foot). In 1.0.19 it ended at about 367 dp on a 397 dp card and was readable. A swipe on the front does nothing in a run because the pager is disabled; in the feed it moves to the next card. The back repeats the prompt in only 2 lines with an ellipsis, so the student never sees the whole question. On that phone 7 of the 270 fixture fronts newly reach this state. (b) At text scale 2.0, the app's supported maximum ('layouts must reflow, not clip', app.dart:109), about 100 of the 270 fixture fronts end under or below the fade on a 360x800 phone, in both releases, and none can be scrolled.",
   "evidence": "card_face.dart:254-267 at 6079162d5: Stack(fit: passthrough) holds [front _Face, Positioned.fill(Semantics(button: true, child: GestureDetector(behavior: HitTestBehavior.opaque, onTap: onTurn)))]. A childless opaque RenderPointerListener returns true from hitTest, and defaultHitTestChildren returns at the first child it hits, so the front _Face's Scrollable never enters the hit-test path. The drag goes to the pager's _CardScroll instead, which by design never scrolls (stage_pager.dart:516-539). Heights come from the code: new front chrome = band max(48, 18.75s+13) + 14 + 34 + foot (12 + max(18, 17.5s) + 18); old chrome = 20 + max(18, 16.9s) + 28 + max(18, 17.5s) + 18; a run card loses RunDeck.depth = 14. Line counts come from BricolageTitle-SemiBold advance widths at the prompt sizes in stage_sizes.dart:20-27 (wordSpacing 0, tracking from promptStyle), applied over the 270 Key cards in test/fixtures/learn2.",
   "suggestedFix": "Give the front the back's pattern: set the overlay to HitTestBehavior.translucent, or drop it and wrap the front's content in a translucent GestureDetector inside _Face, keeping the Semantics button and its 'Turn over: ...' label. A drag on a long front then scrolls it under the pager's edge rule and a tap still turns it. Add a test at text scale 2.0 that drags a long front and checks that its scroll position moves."
  },
  {
   "id": "cards-stage-run-2",
   "title": "The run's deck edges are 48 dp slabs whose flat tops show behind the card on every flip and after every rating",
   "severity": "low",
   "file": "flutter_app/lib/features/learn2/run/run_parts.dart",
   "line": 582,
   "claim": "RunDeck draws each edge as a 48 dp tall superellipse with square top corners, a hairline on all four sides and the paper shadow (lines 567-583). Only its bottom 7 or 14 dp are meant to show under the card; the card, the Stack's last child, is the only thing covering the upper 34-41 dp. Anything that stops the card covering them exposes those flat tops: (1) the flip rotates the card about its centre (card_face.dart:237-241), so from roughly 20 to 160 degrees it is narrower than the deck; (2) after a rating the real card is hidden at once (run_screen.dart:529, Duration.zero) while the ghost shrinks away, and the next card only starts fading in 220 + 60 ms later, over 240 ms (run_controller.dart:630, run_screen.dart:505); (3) a recap swipe (RunSwipe) slides the card sideways.",
   "failureScenario": "Any Learn run. Tap Turn over: for most of the 340 ms flip, two flat-topped, outlined slabs (near one 41 dp, far one 34 dp above the card's foot) show on both sides of the turning card. In Night they are #1B1C19 on the #12110E ground with a 7.5% white hairline across the top and a shadow; in Day they show as the #E2DBC9 hairline outline and shadow. Tap Got it: for about 0.2-0.5 s the empty item area shows the two cut-off slabs at its foot, and the next card then fades in over them. This repeats for every card in a run.",
   "evidence": "run_parts.dart:567-586 at 6079162d5: edge() = IgnorePointer(DecoratedBox(ShapeDecoration(color: fill, shape: mmShapeBorder(BorderRadius.vertical(bottom: Radius.circular(22)), side: BorderSide(color: paper.line)), shadows: paper.shadow))); Positioned(left: 20, right: 20, bottom: -depth, height: 48) and Positioned(left: 10, right: 10, bottom: -depth / 2, height: 48), then child. mmShapeBorder (shape.dart:7-8) is a RoundedSuperellipseBorder, so the zero top radii are square corners and the side is stroked on the top edge too. The web's run.css R8 (20762eb34) uses the same 48 px ::before and ::after edges, so the web shares this look.",
   "suggestedFix": "Draw each edge as a full card-sized sheet offset 7 or 14 dp down and inset 10 or 20 dp, so an exposed edge reads as the next card in the deck. Alternatively, fade the deck out together with the card while it leaves, and keep the stubs from being exposed during a flip, for example by showing only the strip under the card plus the corner overlap."
  }
 ]
}
```

### verify(trace): sending-strip-2 (result)

```json
{
 "real": true,
 "severity": "low",
 "reasoning": "I traced this at 6079162d5 and could not refute it. The mechanism happens as described, but only in a narrow edge case.\n\nHow it happens:\n1. session_clock.dart:46 sets `_endsAtWall = receivedWall + remaining`. If the phone's clock is wrong when the session view arrives, the saved `draft.endsAtWallMs` is off by the same amount. A later network-time correction does not change it. Only the engine's `_reanchorFromServer` re-anchors, and it returns early once `_submitStarted` is set and in ticket mode, so a draft that is already pending keeps the wrong deadline.\n2. stale_submit_settler.dart:88-97 decides \"window closed\" from `_now()` against `endsAtWallMs + 120 s`. It then calls `submitter.settleAfterWindow` and never POSTs.\n3. session_submitter.dart:179-194: `settleAfterWindow` is `_afterExpiry`, which is GET only. A null attempt (404) saves `pendingSubmission: false, windowClosed: true` and returns `SubmitWindowClosed`. The settler then calls `_settled`, which calls `scheduler.cancelSubmit`.\n4. The backup job would have POSTed with no local window check (background_tasks.dart:127-137). After the settler runs, it stops early at line 115 on `windowClosed`, and runner_loader refuses the draft.\n\nSo with a clock that ran slow at anchor time and was corrected later, the settler can close a paper inside the gap [local endsAt + 120 s, true endsAt + 120 s] while the server would still accept a POST.\n\nWhy the severity is low:\n- After an offline pending submit, the engine queues the job with `runAt: now` and a `NetworkType.connected` constraint (session_engine.dart:725, background_tasks.dart:259-262). When the network comes back, WorkManager usually runs that job and POSTs before the student reopens the app. The settler only wins this race when the job is deferred (Doze or a restricted standby bucket), or when the settler's own network-restored trigger fires first in a live process.\n- It also needs all of these at once: a wall clock off by minutes at anchor time (most Android phones use automatic network time), a correction afterwards, an offline submit, and a settle that lands inside a gap no wider than the clock error.\n- The same local-clock trust already exists in the engine's `onConnectivityRestored` (session_engine.dart:675) and in the job's retry decision (background_tasks.dart:160). LK50 adds one more place where it matters, and this place ends with a definite `windowClosed` instead of a skipped retry.\n\nThe result is a lost paper (ticket mode) or lost unacknowledged answers, so the impact is high. The trigger is rare, so overall it is an edge case: low.\n\nWhat would settle it for certain: a device test that anchors a ticket-mode set with the system clock 5 minutes slow, submits offline, sets automatic time on, keeps the job deferred (adb shell cmd jobscheduler, or a restricted bucket), then opens the app online inside the gap. Check whether `windowClosed` is set and no POST appears in the server logs.",
 "fixHint": "In `StaleSubmitSettler._settleOne`, do not let the local clock alone close a paper. In the past-window branch, run the same POST path as the open branch: open the journal, restore the `SessionClock`, and call `submitter.submit(draft:, journal:, durationMs: clock.durationMs)`. `submit` already sends `SESSION_EXPIRED` and `SESSION_ALREADY_SUBMITTED` to `_afterExpiry` (GET first, and only a 404 sets windowClosed). It also returns `SubmitReceived` when the server still accepts the paper, and `SubmitPending` when offline. Keep `if (outcome is! SubmitPending) await _settled(...)`, and do not reschedule the job in this branch. Optionally, POST only when the local verdict is within a bounded skew (for example `nowMs <= endsAtWallMs + submissionGraceMs + 30 min`) and fall back to `settleAfterWindow` for older drafts. That avoids POSTing papers that are days old, though an extra POST is harmless because the submit is idempotent. Add a test where the clock is past the local window, the fake api.submit returns 200, and the expected outcome is `SubmitReceived` with no windowClosed set."
}
```

### verify(trace): sending-strip-1 (result)

```json
{
 "real": true,
 "severity": "medium",
 "reasoning": "I traced this at 6079162d5 and could not refute it.\n\n1. **The settler never touches the notification.** `StaleSubmitSettler` (stale_submit_settler.dart) has no notification dependency. On any non-pending outcome, from either `settleAfterWindow` or `submit`, it calls `_settled`, and `_settled` only runs `scheduler.cancelSubmit(sessionId)`.\n2. **The provider does not add one.** `staleSubmitSettlerProvider` (sync_providers.dart:173-210) builds the settler from `services.db/drafts/submitter/scheduler`. It passes no `NotificationService` or `SessionStatusNotifier`. It runs on startup through a microtask, on resume and on reconnect.\n3. **The notification it leaves behind.** `SessionEngine.onPaused` (session_engine.dart:625-626) posts `showSending` when the submit was started but not received. That is `showOngoing` with `ongoing:true` (notification_service.dart:205), and the gateway sets `autoCancel: !ongoing`.\n4. **Only two places replace it.**\n   - A live engine: `onResumed` calls `status.clear()`, and `submit()` clears on received or windowClosed.\n   - The backup job `runSubmitSessionTask`: `postResultReady`, `postSendEnded`, or a cancel when the draft is already windowClosed or rejected.\n5. **Nothing sweeps it on start.** No code cancels `mock_in_progress` at startup or reconciles active notifications. A grep for ongoing, `activeNotifications` and `cancelAll` turns up only the sign-out `cancelAll` (auth_controller.dart:310, 542, 568).\n6. **No live engine exists after a restart.** After a process death, an engine is rebuilt only if the student opens that runner. Even then `onResumed` is not called on a fresh engine; only `onPaused` and `onResumed` touch the status.\n7. **The job cannot clean up either.** Once the settler cancels the WorkManager job, nothing posts \"Result ready\" or \"not recorded\". If the job had already started, it hits `draft == null` and returns true. Its own comment says \"whoever removed it cleared the status\", and the settler breaks that contract.\n\n**Result:** the pinned \"Sending Mock N / Your answers are … being sent\" stays up while the app shows the result or the not-recorded copy. On Android 13 and below the student cannot swipe it away. It goes only when another paper reuses the id or the student signs out.\n\n**This is new in this release.** Before LK50 the job would have run and replaced the notification.\n\n**Why medium:** this release is meant to stop false \"Sending\" claims (LK50), and a dropped signal at submit on budget phones is a path the app is built for. It is not high because it needs a pending submit, then a process death or swipe-away, then the app opening before WorkManager runs. It is cosmetic: no answers or data are lost.\n\n**What I did not settle:** how often the app beats WorkManager after a reconnect. Opening the app right after turning data back on, or during job backoff, makes it likely.",
 "fixHint": "In stale_submit_settler.dart, add an optional `NotificationService? notifications` to `StaleSubmitSettler`. In `staleSubmitSettlerProvider`, pass `ref.watch(notificationServiceProvider)` to it.\n\nAfter any non-pending outcome in `_settleOne`, settle the status the way `background_tasks._settleStatus` does: wrap it in try/catch, and skip it when `await SessionHeartbeat(db, userId: userId, now: _now).anotherIsLive(draft.sessionId)` is true.\n- **SubmitReceived:** `notifications.cancel(mockInProgressTaskId)`. The app is in the foreground, so no \"Result ready\" post is needed.\n- **SubmitWindowClosed:** `postSendEnded(n, draft: draft, end: UnrecordedEnd.windowClosed)`, or a plain cancel.\n- **SubmitRejected:** `postSendEnded(n, draft: draft, end: UnrecordedEnd.rejected)`.\n\nAlso cancel it, or post `notSent`, in the branch where the pending outcome failed to queue a job: there, too, no retry is running, so \"Sending\" would be false.\n\nAdd a unit test with a fake gateway. Post `showSending`, run `settle()` with a received outcome and with a window-closed outcome, and assert the `mock_in_progress` id was cancelled or replaced."
}
```

### verify(trace): sending-strip-3 (result)

```json
{
 "real": true,
 "severity": "low",
 "reasoning": "I traced it at 6079162d5 and the mechanism is real.\n\n1. Where the timestamp comes from. On a past-window draft that no engine owns, StaleSubmitSettler._settleOne (stale_submit_settler.dart:89-92) calls submitter.settleAfterWindow, which is _afterExpiry. When GET /api/attempts/{id} returns 404 (fetchAttempt returns null), session_submitter.dart:193 calls _tryDraftSave(draft.copyWith(pendingSubmission:false, windowClosed:true)). That goes through _saveOwned, then saveIfOwned (the row is still M's), then save. For a non-archive key, save stamps updatedAtMs = now (session_draft_repository.dart:39). Only archive keys keep the old time.\n\n2. Why M jumps ahead. latest() and watchLatest() order by updatedAtMs desc, limit 1 (lines 160-181). So M becomes the latest draft. latestSessionDraftProvider feeds these:\n- resumeDraftProvider (quick_start.dart:50-53): resumableDraft(M) is false, so it returns null and the Resume capsule disappears.\n- todayDraftProvider (today_providers.dart:194-221): it now describes M, ended, not resumable.\n- suggestion.dart:114 and suggestion_hero.dart:64.\nOpenPaperResolver.offer returns null because P is in runningDrafts (open_paper.dart:69). Nothing on Today or the bar offers P any more.\n\n3. Why M can sit in its own row next to P. The engine archives an earlier draft only when the new session uses the same selection (session_engine.dart:272-288). An Accountancy M and an Economics P therefore keep separate rows.\n\nWhy this is low and not medium:\n(a) It needs M owed and past its window, with no settle, while a newer P is still running. In this build the settler runs on start, on resume and when the network returns (sync_providers.dart:183-205). Starting P needs the network, so normally M is settled before P exists. The realistic paths are narrow:\n   - a user upgrading from 1.0.19 who already had a stale owed M and then started P. If M had been the latest draft, as in the owner's LK50 state where the strip read the latest draft, nothing is hidden.\n   - an earlier settle got SubmitPending (server error or timeout), the student started P, and a later resume got the 404.\n(b) It needs the 404 branch. A 200 deletes M.\n(c) P is not lost. OpenPaperResolver.blocker still returns P (open_paper.dart:79-81) on any credit-spending start. Once P is back on screen, its engine's saves restamp it as latest. If P is never reopened, its backup job still submits it.\nSo this is a visible defect on an edge path: no data loss, no crash.\n\nNot checked: whether the server finalises expired sessions, which would make the 404 branch rarer still.",
 "fixHint": "Make the window-closed write in settleAfterWindow keep M's stored updatedAtMs:\n1. Add an optional flag to SessionDraftRepository.save and saveIfOwned, for example `{bool keepUpdatedAt = false}`. When it is set and draft.updatedAtMs > 0, write that value instead of now (the same rule the archive branch uses at line 39).\n2. In session_submitter.dart, give _afterExpiry (and through it _saveOwned and _tryDraftSave) a parameter that passes keepUpdatedAt: true, and set it only from settleAfterWindow. The engine's own live SESSION_EXPIRED path stays as it is.\nSimpler alternative: in settleAfterWindow, drafts.archive(draft) first and then save the windowClosed copy under the archive key. archive() keeps updatedAtMs, and save() keeps it for archive keys. Note: archived drafts are excluded from runningDrafts, so check that Today's ended or missed notice for M still reads the way you want.\nAdd a test: M is owed, past its window, in its own selection row and older than a running P, and the GET returns 404. After settle(), latest() must still return P, and resumeDraftProvider must be non-null."
}
```

### verify(trace): cards-stage-run-1 (result)

```json
{
 "real": true,
 "severity": "low",
 "reasoning": "I traced the code at 6079162d5 and the mechanism holds. In card_face.dart (around lines 254-267) the front side is a Stack(fit: passthrough) holding [front _Face, Positioned.fill(Semantics(button) -> GestureDetector(behavior: HitTestBehavior.opaque, onTap: onTurn))]. The GestureDetector has no child, so it builds a childless RenderPointerListener. With opaque behaviour its hitTestSelf returns true, so it reports a hit wherever it covers the card. RenderStack hit-tests its children from last to first, and defaultHitTestChildren stops at the first child that reports a hit. So the overlay always wins, and the front _Face's SingleChildScrollView (_FaceState, built with StagePager.physicsOf) never enters the hit-test path.\n\nA vertical drag therefore reaches only the pager's _CardScroll. That view is exactly as tall as its page and, by its own doc comment, never scrolls. Its _PagePhysics sees the first movement, the gate cannot scroll, so the pager takes the gesture. The front never scrolls.\n\nThis contradicts the file's own contract: the header says \"A face taller than that scrolls inside, top-aligned, with a 44 dp fade\", and _FrontBody's doc says \"a face that does not fit is top-aligned and scrolls inside the card\". The back does not have the problem because _Face wraps its content in a translucent GestureDetector (line 347), and a test covers that (\"a long back ... scrolls inside\", card_face_test.dart:354). No test drags a long front. The opaque overlay is the same in 06b65ff46 (1.0.19), so the defect is not new, but the new band, foot and RunDeck depth do take the vertical room the report describes.\n\nVisible effect: when a front is taller than its card, the bottom of the column is clipped. Once the overflow is more than about 38 dp (the prompt's 34 dp bottom padding plus the 48 dp foot, minus the 44 dp fade), the last prompt lines sit under the paper-coloured fade and cannot be reached. The back repeats the prompt in only 2 lines (maxLines: 2, ellipsis), so the student never sees the full question.\n\nWhy low: it needs a long prompt plus a small screen or a large text scale (about 1.3 or more on a 360 dp phone, or 2.0). It is a real visible defect, but on an edge-case path, with no crash, no data loss and no Play risk. I did not re-check the exact counts in the report (7 of 270 fronts at 1.3, about 100 at 2.0). A golden or widget test at textScaler 1.3 and 2.0 on 360x640, using the fixture card, would settle the numbers. The core defect (an unscrollable front) is certain from the hit-test semantics alone.",
 "fixHint": "In flutter_app/lib/features/learn2/stage/card_face.dart (around line 263 at 6079162d5), change the front overlay to `GestureDetector(behavior: HitTestBehavior.translucent, onTap: widget.onTurn)`, keeping the Semantics(button: true, label: speak, onTap: widget.onTurn) wrapper. A childless translucent listener adds itself to the hit path but returns false, so RenderStack goes on to hit-test the front _Face and its Scrollable. A drag then scrolls the front under the pager's _PagePhysics edge rule, and a tap still turns the card, since the tap recognizer wins the arena when the finger does not move. The other option is the back's pattern: pass onTap: widget.onTurn and scrollable: true to the front _Face and drop the overlay, but the Semantics button label must then move onto the face. Add a widget test at textScaler 2.0 on a 360x640 surface with a long key_line fixture front. It should drag up on the front and expect the inner SingleChildScrollView's position.pixels to be above 0, and expect a tap to still call onTurn."
}
```

### verify(trace): cards-stage-run-2 (result)

```json
{
 "real": true,
 "severity": "medium",
 "reasoning": "I traced the code at 6079162d5 and the report is correct.\n\n1. **The edges are short slabs.** In run_parts.dart:567-586, `RunDeck` draws each edge as `Positioned(bottom: -14 or -7, height: 48)`. The decoration is `mmShapeBorder(BorderRadius.vertical(bottom: 22), side: paper.line)`, which is a `RoundedSuperellipseBorder` (shape.dart:7-8). So the top corners are square and the hairline is stroked on all four sides, including the top. The `Stack` uses `clipBehavior: Clip.none`, and the only thing covering the upper 34 and 41 dp of the slabs is `child`, the card.\n\n2. **The flip exposes them.** card_face.dart:224-242 rotates each face with `Transform(alignment: center, rotateY(angle))` and perspective 1/1200 over 340 ms on `Motion.drawer`. As the angle nears 90 degrees the card's projected width goes towards zero. The deck is a sibling outside the transform and does not move, so the full 48 dp slabs, flat tops and top hairlines included, show on both sides of the turning card. This happens on every Turn over and every Turn back.\n\n3. **A rating exposes them.** On a rating, run_controller.dart sets `leaving = true` and notifies. run_screen.dart:529 then hides the real face with `AnimatedOpacity(..., Duration.zero)`. The ghost in run_flight.dart is a separate root-overlay entry. It either shrinks (0.96, then 0.52, then 0.18) or, for a missed or look drop, falls 64 dp while fading out. The deck is not inside that fade and stays fully drawn. `advance()` then runs, and the next card is wrapped in `StageIn` (60 ms delay, 240 ms fade). That wrapper covers only the face, not `RunDeck`. So for a moment the empty card area shows only the two cut-off slabs, and the next card fades in over them, with their top hairlines showing through while it is semi-transparent.\n\n4. **The recap swipe exposes them too.** `RunSwipe` wraps the face inside `RunDeck`, so a sideways drag uncovers one end of each slab.\n\nThe colours are real: Night edges are #1B1C19 and #191917 (card_paper.dart:80-81), and Day edges are #F3EEE3 and #ECE6D9, each with the paper hairline and shadow. Nothing depends on server data, and it is not specific to debug builds. It happens for every Key card in every Learn run (reduced motion still applies the 0-to-1 opacity fades). It is transient and nothing breaks, but it is a visible defect on the most common Learn path. Under the rubric (\"visible defect on a common path\") that makes it medium, not low.",
 "fixHint": "In RunDeck (run_parts.dart:567-584), draw each edge as a whole card sheet instead of a 48 dp stub, so whatever is exposed looks like the next card in the deck:\n- Far edge: `Positioned(left: 20, right: 20, top: 14, bottom: -14, ...)`\n- Near edge: `Positioned(left: 10, right: 10, top: 7, bottom: -7, ...)`\n- Give each one the card's full radius on all four corners, e.g. `mmShapeBorder(BorderRadius.circular(22), side: BorderSide(color: paper.line))`, so no flat top or straight top hairline can ever show.\n\nOptionally, during `c.leaving`, also fade or drop the near edge so the stack reads as one card leaving.\n\nKeep the web's run.css R8 `::before`/`::after` edges in step (also 48 px), or the two platforms will look different.\n\nCheck the result with a widget or golden test that pumps the flip at about v=0.5 and the frame just after a rating, in both Night and Day."
}
```

Stopped before finishing: settle: goldens + full suite

## Workflow wf_5f4c151f-e76

### launched (launched)

```json
{
 "type": "launched"
}
```

### reference: ug.preparoo.app (result)

```json
{
 "summary": "I measured ug.preparoo.app on 4 Nov 2026 with two Browserbase cloud sessions (ap-southeast-1, Chrome 156, about 3 minutes in total). No local browser was used, so the lock was never needed. I ran 5 jobs: phone 390x844 with a cold load, a repeat visit and touch swipes; desktop 1280x800 cold; phone on Slow 4G with 4x CPU throttling; and phone with reduced motion. The evidence is CDP screencast frames (named by ms since navigation start), an in-page sampler recording every animation frame, and the site's own code (saved as line-numbered excerpts). Everything is in C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo, with index.json as the map. I signed in nowhere and edited no MockMob code.\n\nLOADER: A black full-screen panel is painted at first paint by inline CSS. The wordmark plus kangaroo lockup then zooms in: scale 0.85 to 1 and opacity 0 to 1, 800 ms, cubic-bezier(0.16,1,0.3,1). The zoom waits for the brand font and logo, with a 300 ms fallback. Next, Webflow IX2 action list a-60 \"Brand fade\" (from the Alture Webflow template) lifts the panel 600 ms after IX2 starts: height 100vh to 0 and translateY to -20vh, 750 ms in-out-cubic. A striped 20vh image rides the bottom edge. The hero underneath is already static and is revealed bottom first. Measured on screen: 0.78 to 2.47 s on a cold phone load, 0.32 to 1.90 s on a warm repeat visit. The end depends on page load, not a fixed time: on Slow 4G with 4x CPU it is plain black from 1.8 to 7.9 s and is gone only at 9.0 s. It plays on every visit and ignores reduced motion.\n\nTYPING: \"Ace the [CUET|IPMAT]\". It types at 150 ms per character (6.7 per second) and deletes at 100 ms per character (10 per second). Each full word holds for 2.2 s and the empty slot lasts 0.65 s; one two-word cycle takes 7.45 s. The caret is a '|' at weight 100 squeezed to 0.3 width, blinking on/off every 0.7 s. Reduced motion is ignored.\n\nHERO: The exam name is a 39 px headline at y=80 on the phone (141 px on desktop). One navy illustration card covers 69% of the phone screen and 67% of the desktop screen, and the benefit line and call to action sit inside it. Phone and desktop have the same parts and motion.\n\nSCROLL: Free native scroll with no snapping and no scroll library. A 300 px flick travels 2,817 px; a slow 300 px drag travels 285 px. The page is 11.6 phone screens long.\n\nFor MockMob: copy the structure, not the look, and fix Preparoo's flaws. The loader should show the mark from first paint, have a hard time cap, play once per session and respect reduced motion. Hero motion should start only after the reveal. The exam name should come first, with Mobi inside one card on both widths. The scroll story needs stepping that ignores swipe speed. One decision is open: MockMob's headline was ruled static on 1 Nov, and LK74 now points to a typed word.",
 "findings": [
  {
   "topic": "Entry loader: what appears and in what order (fast cold load)",
   "observation": "1) First paint is a solid black screen. The style tag 'preloader-fix' forces .brand_wrap{display:flex!important} and hides its children; the panel is fixed, full screen, z-index 102, 100vh, black, and the theme-color meta is #000 so the phone status bar matches. 2) The lockup ('Preparoo' in BDO Grotesk VF 600, 3.5rem, -0.03em, followed by a 4.2rem white kangaroo PNG) zoom-fades in. This is the CSS animation brand-zoom-in: 0.8 s, cubic-bezier(0.16,1,0.3,1), scale 0.85 to 1, opacity 0 to 1. It is opacity 0.95 after 300 ms and about 1.0 after 520 ms. 3) The lockup is fully visible for only about 0 to 250 ms. 4) The curtain: IX2 a-60 'Brand fade' waits 600 ms after IX2 starts, then animates panel height 100vh to 0vh and translateY 0 to -20vh together, 750 ms, inOutCubic. The lockup stays centred in the shrinking panel, so it rides up and off the top. A 1918x246 'mask.png' of horizontal black stripes (20vh tall, top:100%) trails the bottom edge, giving a venetian-blind wipe. 5) The panel is set to display:none and theme-color resets to #ffffff (2.5 s fallback). IX2's own .brand_logo scale steps do nothing because no element has that class.",
   "evidence": "Phone cold, in ms from navigation start: first paint (black) 776; IX2 start 1074; DOMContentLoaded 1126; fonts loaded 1142; is-ready (zoom starts) 1203; preloader-fix removed and curtain starts 1721; height 0 at 2438; display:none at 2472. Desktop cold: first paint 680, IX2 963, zoom 1065, curtain 1831, gone 2409. Code: source/splash.txt:5 (preloader-fix), :14-25 (keyframes, 0.8 s cubic-bezier(0.16,1,0.3,1)), :30 (theme-color #000000), :33-50 (markup), :53-73 (CSS: fixed, 100vh, lines 20vh at top:100%), :76-89 (event e-100 PAGE_START, loop off), :141-149 (delay 600, inOutCubic, 750 ms, heightValue 0, yValue -20vh), :154-157 (display none), :214 (fonts.load gate), :249 (setTimeout(revealBrand,300)). Frames: frames/m390/m390-f00788.jpg (black), m390-f01288.jpg (zoom mid-way), m390-f01705.jpg (lockup full), m390-f02055.jpg and m390-f02155.jpg (curtain with striped edge), m390-f02521.jpg (settled).",
   "files": [
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/filmstrip-m390.png",
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/filmstrip-d1280.png",
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/source/splash.txt",
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/m390.json",
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/d1280.json"
   ],
   "implication": "What makes it read as refined: one lockup, one easing in, one wipe out, no spinner or text, and no white flash because the splash is the very first paint. The hero is already in place underneath, so the wipe is the hero's entrance and nothing animates in again."
  },
  {
   "topic": "Entry loader: what ends it, slow networks, repeat visits, reduced motion",
   "observation": "The end is not a fixed time. The curtain is chained to Webflow IX2 starting, which happens at DOMContentLoaded after the 1.1 MB HTML (144 KB transferred), jQuery, the Webflow chunks and GSAP have run. The zoom is gated on the brand font and logo, but its 300 ms fallback timer lives in the tail script, so it only runs after the HTML has parsed. On Slow 4G with 4x CPU the screen is plain black with no logo from 1.78 s to about 7.9 s. The lockup zooms at 7.85 s, before the brand font finishes at 8.17 s, so the 'weird zoom' they tried to prevent can still happen. The curtain skips frames: its first rendered frame is already at 548/844 px height at 8.69 s, and it is gone at 8.96 s. The revealed headline reads 'Ace the |' because the typing loop started at 1.65 s under the splash and had deleted the word. The hero illustration finishes loading only at 15.2 s. On a second visit in the same context (warm cache) the splash plays again: first paint 320 ms, zoom 550 ms, curtain 1152 to 1835 ms, gone 1902 ms. Storage holds only attribution and Razorpay keys, with no 'seen splash' flag. With prefers-reduced-motion: reduce, the zoom (18 intermediate frames) and the curtain (32 frames) play unchanged.",
   "evidence": "m390slow.json: first paint 1776, HTML responseEnd 3782, IX2 7507, is-ready 7854, BDO font responseEnd 8166, curtain 8686 to 8955, image responseEnd 15226, 8 long tasks (1424 ms in total, longest 264 ms). Frames: frames/m390slow/m390slow-f08487.jpg (lockup at 8.5 s) and m390slow-f09003.jpg ('Ace the |' with half-loaded art). m390.json repeatPrp, plus frames/m390-repeat/m390-repeat-f00835.jpg (splash replayed). m390rm.json: zoom 1176 to 1730, curtain 1813 to 2546. A comment in the page source calls the splash 'exactly as the alture template does', i.e. it comes from a purchased Webflow template.",
   "files": [
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/filmstrip-m390slow.png",
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/m390slow.json",
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/m390rm.json",
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/frames/m390slow/m390slow-f09003.jpg"
   ],
   "implication": "Do not copy the gating. On budget Indian phones on 4G, Preparoo's loader becomes 6 s of black. MockMob's loader should draw its mark at first paint, have a hard time cap, play once per session, respect reduced motion, and start the hero's motion only after the reveal."
  },
  {
   "topic": "Hero typing animation (LK74)",
   "observation": "Markup: h1 'Ace ' plus h2 'the <span id=rotating-exam>CUET</span>'. Only the last word changes; 'Ace the' never moves because the slot sits at the end of the line. Two words: CUET and IPMAT. 'CUET' is in the HTML already complete, and the loop starts in the 'about to delete' state, 500 ms after the inline script runs. Code values: typingSpeed 150, deletingSpeed 100, pauseAfterWord 2000, pauseAfterDelete 500, driven by setTimeout at a constant cadence with no jitter. Measured: each typed character 149-151 ms (6.7 per second); each deleted character 99-100 ms (10 per second); the full word stays for 2.20-2.22 s (2000 ms plus two do-nothing steps); the empty slot shows only the caret for 650 ms; one two-word cycle takes 7.45-7.47 s. The first delete starts 3.39 s after navigation on desktop and about 3.5 s on the phone, only about 1.0 s after the curtain clears. Caret: an ::after '|' glyph in the text colour, weight 100, scaleX(0.3), margin-left 0.06em. That is about 0.5 px wide at 39 px type and about 1.7 px at 141 px type. The glyph runs from ascender to descender, so at 1280 it hangs into the top edge of the art card. Blink: keyframes 0-49% visible and 50-100% hidden over 0.7 s, so a hard 350 ms on / 350 ms off that never stops, even while typing. Reduced motion: the same cycle runs (m390rm typing log). Screen readers get a split h1 'Ace' and h2 'the CUET' with text that keeps changing, and nothing is marked aria-live or aria-hidden.",
   "evidence": "source/typing.txt:5-6 (markup), :9-24 (caret CSS and rex-blink), :25-66 (script: :28 words, :30 starts complete, :34-37 speeds, :66 500 ms start). m390.json prp.typing (e.g. C 8272, CU 8422, CUE 8572, CUET 8721, CUE 10922, CU 11022, C 11121, empty 11221, I 11871 ... IPMAT 12471; CUET complete at 8721, 16188, 23638, 31087). d1280.json typing (first CUE at 3386). Screenshots: m390-hero-at04787ms.png ('Ace the CU', caret in its off phase), m390-hero-at07229ms.png ('Ace the IPMAT|'), d1280-hero-at03911ms.png (caret crossing into the card).",
   "files": [
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/source/typing.txt",
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/m390-hero-at07229ms.png",
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/d1280-hero-at03911ms.png"
   ],
   "implication": "Worth adopting: one changing word at the end of a fixed line, rendered complete at first paint, slow deliberate typing (about 150 ms per character), faster deletion (100 ms), a long hold (2.2 s) and a hairline caret. Worth improving: start the first delete 2.5 s or more after the reveal; keep the caret solid while typing and blink only while holding; stop on the main word after 2-3 cycles or when the hero is off screen; show a static word with reduced motion; keep one stable h1 sentence for screen readers."
  },
  {
   "topic": "Other hero motion running at the same time",
   "observation": "The hero has three loops on separate clocks. (1) The typing, a 7.45 s cycle. (2) A value line (five lines: 'Mocks that represent past year patterns', 'Simple solutions which make sense', 'Topic tests for targeted practice', 'Flashcards with spaced repetition for retention', 'Analytics which help you prioritize') slides up one 3-line block every 3000 ms. The slide is translate3d, 0.6 s, cubic-bezier(0.25,0.1,0.25,1), 152 px at 390. A clone of the first line makes the loop seamless, with a hard reset 650 ms after the 5th slide. The first slide comes at 4.6 s. (3) The call-to-action dot pulses: IX2 a-21 scales 0 to 1 while fading 1 to 0, 1000 ms outCubic after a 750 ms delay, looping. None of the three checks reduced motion.",
   "evidence": "source/typing.txt:86-94 (box height calc(2.75rem*1.15*3)), :128-148 (setInterval 3000, transition 0.6 s, 650 ms reset); :155-200 (IX2 e-29 loop on, a-21 delay 750 and 1e3 outCubic). m390.json prp.words: slides at 4605, 7605, 10605, 13605, 16605 ms, reset at 17255. m390rm.json: a slide still happens at 4646 with reduced motion. m390rm-hero-at06640ms.png shows the pulse ring.",
   "files": [
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/m390.json",
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/m390rm-hero-at06640ms.png"
   ],
   "implication": "Three unsynchronised loops is a weakness, not something to copy. MockMob's hero should have at most one moving thing at a time (the typed word, or a Mobi reaction), with everything else still."
  },
  {
   "topic": "Typing inside the product demo ('Ask Preparoo')",
   "observation": "The AI section is a scripted demo. A fake pointer moves to the input in 400 ms, a tap ring plays (apTapPulse 0.6 s ease-out), and questions type themselves. 'Good evening, Arya' types at 55 ms per character, 'How did I do on Mock 1?' at 45 ms, 'Am I on track?' at 55 ms and 'What should I prioritize this week?' at 40 ms, i.e. 18-25 characters per second. That is about 3x faster than the hero's 150 ms. On touch devices delays are multiplied by 1.4 (mt=hasMouse?1:1.4). The caret is a 2 px x 1em bar in #0d2442 blinking with a 0.6 s step-end, and it hides 400 ms after the line finishes. Answers stream in. The demo ends on a navy brand card: the splash lockup again, fading in over 0.8 s.",
   "evidence": "source/demo-typing.txt:6 (mt 1.4), :8-30 (typeText helper), :70-72 (typed lines and speeds), :75-76 (caret and apCursorBlink), :78-89 (apBrandScreen with a 0.8 s opacity transition). The greeting call is at index.html char 882557 (typeText(greeting,greetCursor,'Good evening, Arya',55,400)).",
   "files": [
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/source/demo-typing.txt"
   ],
   "implication": "Two typing speeds for two jobs: a slow display word in the hero, realistic fast input in product demos. Reusing the opening lockup as the demo's end card is a cheap way to make the brand feel consistent. MockMob could end its exam or AI demos on its own wordmark-with-Mobi card."
  },
  {
   "topic": "Hero composition at 390x844 (LK70)",
   "observation": "Top to bottom: a 57 px white nav (lockup 123x28; 'Pricing' pill 69x27 in #c3d1e3 at 12.16 px/600; hamburger). Then the headline 'Ace the CUET': 39 px (10vw), Inter VF 600, line-height 0.9, letter-spacing -0.03em, black on #f5f6f8, at y=80. Then one art card, 366x620 at y=131 with 12 px side margins, radius 32 px, navy #0a1628, using a portrait illustration made for phones (v2_dark_bg_mobile.webp, 1536x2752, 428 KB, object-position center 70%). The words sit inside the card: the kicker 'ACE THE EXAM' (Roboto Mono VF 14 px, +0.7 px, 70% white, y=163); the value line (BDO Grotesk VF 28 px/500, line-height 1.15, -0.02em, white, 2 lines, y=191); and at the bottom right a glass call-to-action panel 'Ready to hop in? / Get started today!' (288x66, rgba(255,255,255,.08) with blur(12px), radius 12; title 14 px/600, subline 10.4 px at 50% white, 6 px pulsing dot). The card covers 226,920 of 329,160 px² (68.9%). The headline block is 3.6% of the screen. There are 19 words outside the nav. The next section's 'Make the CUET...' heading peeks in at y=836. The six product links are hidden on phones (0x0) and live in the menu.",
   "evidence": "m390.json metrics (heading1/heading2/image/label/wordItem/cta/coverage/visibleText). Screenshots m390-hero-at07229ms.png and m390-hero-at10546ms.png; frame frames/m390/m390-f02521.jpg.",
   "files": [
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/m390-hero-at07229ms.png",
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/m390.json"
   ],
   "implication": "A large art block is fine (Preparoo's is 69% of the phone screen) as long as the exam name comes first, above the art, and the benefit line and call to action sit inside the art. MockMob's phone hero currently places the painted room and Mobi before the h1 (wt-1104-web-polish/src/app/page.js:183, with the h1 at :184), which is the reverse order. Put the CUET line first, then one card with Mobi, one benefit line and the call to action."
  },
  {
   "topic": "Hero composition at 1280x800 and phone/desktop parity (LK67)",
   "observation": "Desktop uses the same parts in the same order. The headline is 140.8 px (11vw; clamp(4rem,11vw,14rem)) and spans 1137 px wide from y=96 to 223. The art card is 1241x549 at y=239, using a separate landscape illustration (v2_dark_bg.webp, 1824x576) and covering 66.6% of the screen. A row of six product links (Mocks, PYQs, Sectionals, Topic Tests, Notes, Flashcards; each 181x39, 16 px/600, white, with dotted underlines) sits at the top of the card. Kicker plus 44 px value line sit bottom left; the glass call-to-action (288x71, rgba(255,255,255,.2) with blur(20px), radius 18) sits bottom right. The nav has 8 links plus a 'Pricing' pill and a navy 'Log in' pill. The only phone/desktop differences are the illustration crop, the type scale (10vw against 11vw), the link row and the strength of the glass. The motion is identical. The one weakness: the 44 px value line sits over the drawn answer sheet, so text and line art touch.",
   "evidence": "d1280.json metrics; source/typing.txt:71-75 (10vw and 11vw rules); d1280-hero-at06634ms.png and d1280-hero-at09398ms.png.",
   "files": [
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/d1280-hero-at06634ms.png",
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/d1280.json"
   ],
   "implication": "Parity rule for LK67: one hero with identical motion and interaction on both widths, varying only the art crop and type scale. Preparoo has no tappable mascot at all; its only hero interaction (the call-to-action panel, which scrolls to #pricing over 850 ms with easeInOutCubic) works the same on both widths. MockMob's Mobi tap and bubble should exist on both widths or on neither."
  },
  {
   "topic": "Brand consistency: colour, type roles, illustration, mascot (LK68, LK73)",
   "observation": "Colour: one navy family (#0d2442 for interface, #0a1628 for the hero card), a page background of #f5f6f8, white type on navy, a black headline, and one saturated blue used only in about 3 small spots of the illustration. There is no glow, no neon edge and no gradient text; depth comes from one soft shadow under the card and one glass panel. Preparoo has no dark theme at all (no prefers-color-scheme or data-theme anywhere). Type has three fixed roles: Inter VF for body and headline (one of the fonts the owner listed as AI-common, so do not copy it), BDO Grotesk VF for the wordmark, value lines and call-to-action titles, and Roboto Mono VF only for kickers. The illustration is one monoline isometric style (white strokes on navy) of exam objects: open book, laptop with a chart, calculator, ticked answer sheet, flashcard stack, mug, book stack. The kangaroo mark never animates and is never a hero character. It works as a fixed signature in four places: the splash lockup, the nav lockup, the 'Ask Preparoo' demo end card, and a 24 px assistant avatar.",
   "evidence": "CSS tokens --_typography---font-family--primary 'Inter VF', --secondary 'BDO Grotesk VF', --detail 'Roboto Mono VF' (css/preparoo.ef0833b7b.css). The logo PNG appears at index.html chars 68595 (splash), 69543 (nav), 603446 (demo end card), 831669 and 910373 (avatar). A curl check of index.html and the CSS found 0 matches for prefers-color-scheme and data-theme. Screenshots m390-screen2.png, m390-screen3.png, d1280-screen2.png, d1280-screen3.png.",
   "files": [
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/m390-screen3.png",
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/d1280-screen2.png"
   ],
   "implication": "For Night (LK68), the navy card shows a dark surface can be calm: texture comes from line work, not glowing edges. Keep volt for the main action fill plus at most 1-2 small accents per screen. For LK73, keep MockMob's fonts (Bricolage display, Hanken body, Literata reading) with fixed jobs like Preparoo's; a kicker can be Hanken caps at 13-14 px, +0.05em, 70% opacity. Use Mobi as one consistent signature (the second 'o' of the wordmark, the loader, the AI avatar, end cards) and draw illustrations in one style showing MockMob's own exam objects."
  },
  {
   "topic": "Phone scroll behaviour and page length (LK69, LK71)",
   "observation": "Plain native scroll. There is no scroll-snap on html or body, no Lenis, Locomotive or ScrollTrigger (only leftover data-lenis-prevent attributes), overscroll-behavior:none, and history.scrollRestoration='manual' with a guard that undoes any scroll the browser restores until the user acts. Touch swipes measured from the top at 390: slow 300 px drag over 1.2 s gives 285 px (0.95x); 300 px in 250 ms gives 464 px (1.55x); 300 px in 80 ms gives 2,817 px (9.4x, 3.3 screens, settled in about 1.2 s); 150 px in 50 ms gives 1,836 px (12.2x). Desktop wheel: 1 notch gives 100 px, 5 notches give 500 px. So a fast flick skips several sections here too. Preparoo avoids the problem by having no pinned, stepped story; step-by-step movement happens only inside components. On phones the feature tabs become an accordion: a tapped tab gets smooth scrollIntoView 60 ms later with scroll-margin-top 84 px. There are prev/next arrows on the previews, CUET/IPMAT toggles, and the blog carousel is the only snap (scroll-snap-type:x proximity). Length: 9,817 px = 11.6 screens at 390x844 and 8,542 px = 10.7 screens at 1280x800, across 9 sections (hero, try-features, ask-preparoo, overlap, pricing, faq, newsletter, blog, cta). The overlap and pricing sections are 1,296 and 2,449 px tall on the phone.",
   "evidence": "m390scroll.json tests (scroll position over time, e.g. fast flick 1424, 2174, 2635, 2813, 2817). d1280.json scrollTests. m390.json metrics.scroll {snapHtml:none, behavior:auto, overscroll:none, lenis:undefined, restoration:manual}. source/scroll.txt:5-32 (guard), :37 (overscroll), :41 (scroll-margin-top 84px), :45-46 (blog snap), :55 (850 ms call-to-action scroll).",
   "files": [
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/m390scroll.json",
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/source/scroll.txt"
   ],
   "implication": "'One gesture = one step' cannot be borrowed from Preparoo; MockMob has to build it into its own scroll story (which must stay, per the owner's rule). Option 1: scroll-snap-type: y mandatory on the story with scroll-snap-stop: always on each step, so a fling cannot pass a step and a half drag settles to the nearest one. Option 2: a gesture controller that moves exactly one step per touch-end when the drag is 40 px or more, ignoring speed, and locks input during the 450-600 ms transition. Everywhere else, use plain native scroll like Preparoo, with no inertia library."
  },
  {
   "topic": "Section rhythm and text density (LK71, LK72)",
   "observation": "Each section follows the same pattern: a 3-5 word heading at 48 px on the phone and 96 px on desktop ('Make the CUET feel simple', 'Ask Preparoo', 'Answered questions.'), one sub-line of about 6-9 words ('Simple explanations. Structured practice. Only what matters.'), a CUET/IPMAT toggle, then a hands-on demo in a neutral browser frame (traffic-light dots, 'ug.preparoo.app' address bar). Tab descriptions are 4-7 words ('Stuff you actually need to remember'). The demos show Preparoo's own interface: a flip card ('cerebral — Tap to reveal', 1/10), a mock question with right and wrong states, notes, and a SWOT view. They do not copy NTA. The desktop preview frame is fixed at clamp(560px,50vw,660px) tall.",
   "evidence": "d1280.json and m390.json metrics.headingsAll (phone: 48 px at y=843, 2008, 7051, 9296; desktop: 96 px). Screenshots m390-screen2.png, m390-screen3.png, d1280-screen2.png. index.html char about 88000 (tryFeaturesWrap preview fixed at clamp(560px,50vw,660px)).",
   "files": [
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/m390-screen2.png",
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/d1280-screen2.png"
   ],
   "implication": "For the exam-screen section (LK72): show MockMob's real exam interface inside a neutral frame of fixed height (about one phone screen), introduced by one short heading and one sub-line. Let the demo do the explaining instead of paragraphs."
  },
  {
   "topic": "Earlier study notes: what still holds (MOBILE-REFINEMENT-PLAN-2026-10-04, HOMEPAGE-REFINEMENT-2026-10-02)",
   "observation": "Still true: the phone hero uses its own illustration, v2_dark_bg_mobile.webp, rendered 366x620 (natural size now measured at 1536x2752, 428 KB). The header is compact (57 px). Short, large headings are each followed by a highlighted feature row and then a browser-frame preview. Backdrop blur is used: the call-to-action glass is 12 px on phones and 20 px on desktop, and progressive-blur panels are still in the markup. From the 2 Oct note: hands-on demos and clearly selectable modes (CUET/IPMAT toggles; Flashcards/Notes/Mocks tabs) are still the pattern. No longer true: 'a floating free-mock prompt overlays preview content' — the 4 Nov markup has no fixed or floating prompt (only modals use position:fixed) and none appeared in screens 1-3 at 390. Superseded: the 4 Oct note said the animation code's authorship could not be established. The code is now read: Webflow IX2 action lists, CSS keyframes and a setTimeout typewriter; GSAP is used once, for a desktop mouse-trail effect; the splash comes from the Alture Webflow template. Neither earlier note covered the loader, typing cadence, flick distances or reduced-motion behaviour; those are new here.",
   "evidence": "m390.json metrics.image (366x620 at y=131) and imgNatural [1536,2752]; resources (v2_dark_bg_mobile.webp, 428,026 bytes). Grep of index.html for position:fixed found 5 rules, all modals or the splash. m390-screen2.png and m390-screen3.png show no floating prompt.",
   "files": [
    "C:/Users/atish/Desktop/mockmob copy/mockmob-next/docs/brain/MOBILE-REFINEMENT-PLAN-2026-10-04.md",
    "C:/Users/atish/Desktop/mockmob copy/mockmob-next/docs/brain/HOMEPAGE-REFINEMENT-2026-10-02.md"
   ],
   "implication": "The 4 Oct note's composition lessons still apply. Drop its floating-prompt warning as a description of today's Preparoo, but keep the rule it implied: MockMob's dock must not cover previews."
  },
  {
   "topic": "Principles for MockMob's own loader (LK74)",
   "observation": "Recommended spec, in MockMob's own idiom rather than Preparoo's striped template curtain. 1) Paint the splash in critical CSS at first paint in the theme's ground colour (Night ground on Night, paper on Day; Preparoo uses black over a light site), with a matching theme-color. 2) Draw logo B ('mockmob' with Mobi as the second o, plus the volt dot) as inline SVG in the server HTML, so it needs no font or image and is visible from the first frame. Preparoo hides its mark at opacity 0 until font, logo and scripts are ready, which became 6.1 s of black on Slow 4G. 3) Choreography sized to Preparoo's: mark rises in (scale 0.94-0.96 to 1 plus opacity, 450-520 ms, cubic-bezier(0.16,1,0.3,1); Preparoo uses 0.85 to 1 over 800 ms with the same curve), Mobi blinks once at about 500 ms (about 160 ms), the volt dot lands, then the panel lifts (translateY 0 to -100%, 600-700 ms, cubic-bezier(0.65,0,0.35,1); Preparoo uses 750 ms in-out-cubic after a 600 ms delay). Target about 1.2 s from first paint on a fast connection, with a hard cap of about 2.0 s whatever the load state; never wait on DOMContentLoaded or the full page. 4) Play once per session (sessionStorage); skip it on back/forward, on hash links and when the visitor arrives already scrolled. Preparoo replays it on every visit, a 1.6 s cost each time. 5) Reduced motion: no scale and no wipe, either no splash or a 150 ms cross-fade. 6) The lift is the hero's entrance: do not add a second hero entrance, and start the typed word and any Mobi reaction only after the panel is gone. No glow, sheen or edge light, per the owner's 16 Oct verdict.",
   "evidence": "Derived from the numbers in the loader findings (m390.json, m390slow.json, source/splash.txt:14-25 and :141-149).",
   "files": [
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/source/splash.txt"
   ],
   "implication": "This gives the owner's 'refined loading animation on entry' without Preparoo's slow-network black screen, its replay on every visit, and its disregard for reduced motion."
  },
  {
   "topic": "Decision for the parent: headline typing conflicts with the 1 Nov ruling",
   "observation": "MockMob's current headline is static on purpose. wt-1104-web-polish/src/components/landing/heroLines.mjs:1-6 records the R3 ruling H1 (1 Nov 2026): 'CUET 2027. One mock. Know what to fix.', with no typing, no caret and no cycling line, and Mobi's taps carrying the reactions. LK74 (4 Nov) asks for Preparoo-style typing, and the task's standing rules allow 'a typed line or a crisp per-letter morph'. If typing returns, follow Preparoo's sound parts: the word is complete at first paint, sits at the end of a line with min-width reserved for the longest word so phone line breaks never change, about 150 ms per character typed and 100 ms deleted, a 2.2-2.5 s hold, and a hairline caret in the text colour. Add what Preparoo lacks: start after the reveal, stop after 2-3 cycles, pause when off screen or when the tab is hidden, keep it static with reduced motion, mark the slot aria-hidden under a stable HERO_SENTENCE, and make every cycled word a true product fact.",
   "evidence": "wt-1104-web-polish/src/components/landing/heroLines.mjs:1-13; wt-1104-web-polish/src/app/page.js:183-191 (phone room plus Mobi, then the h1 lines).",
   "files": [
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/src/components/landing/heroLines.mjs",
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/src/app/page.js"
   ],
   "implication": "Reintroducing typing reverses a recorded ruling. The orchestrator should state that it follows LK74 (4 Nov, newer) and update the tests that hold the static headline (heroLines.test.mjs)."
  }
 ],
 "numbers": [
  {
   "metric": "Splash first paint (black), phone cold / desktop cold / phone warm repeat / phone Slow 4G + 4x CPU",
   "value": "776 / 680 / 320 / 1776 ms"
  },
  {
   "metric": "Webflow IX2 start (begins the 600 ms countdown to the curtain)",
   "value": "1074 / 963 / 500 / 7507 ms"
  },
  {
   "metric": "Lockup zoom start (font and logo ready, or 300 ms fallback)",
   "value": "1203 / 1065 / 550 / 7854 ms"
  },
  {
   "metric": "Lockup zoom",
   "value": "800 ms, cubic-bezier(0.16,1,0.3,1), scale 0.85 to 1, opacity 0 to 1 (opacity 0.95 at +300 ms)"
  },
  {
   "metric": "Curtain",
   "value": "starts 600 ms after IX2 start; height 100vh to 0 and translateY 0 to -20vh, 750 ms inOutCubic; measured 1721-2438 ms phone cold, 1831-2409 desktop, 1152-1835 warm, 8686-8955 slow (frames dropped)"
  },
  {
   "metric": "Splash gone (display:none), phone cold / desktop / warm / slow",
   "value": "2472 / 2409 / 1902 / 8955 ms"
  },
  {
   "metric": "Plain black with no logo on Slow 4G + 4x CPU",
   "value": "about 6.1 s (1.78 to 7.85 s)"
  },
  {
   "metric": "Hero illustration loaded on Slow 4G + 4x CPU",
   "value": "15.2 s (428,026-byte webp)"
  },
  {
   "metric": "Hero typing speed (type / delete)",
   "value": "150 ms per char = 6.7 chars/s / 100 ms per char = 10 chars/s"
  },
  {
   "metric": "Typing hold on full word / empty slot / two-word cycle",
   "value": "2.20-2.22 s / 0.65 s / 7.45 s"
  },
  {
   "metric": "First delete after navigation (fast load)",
   "value": "3.39 s desktop, about 3.5 s phone (about 1.0 s after the curtain clears)"
  },
  {
   "metric": "Caret",
   "value": "'|' via ::after, weight 100, scaleX 0.3 (about 0.5 px at 39 px type, 1.7 px at 141 px), 0.7 s hard blink (350 on / 350 off), always blinking"
  },
  {
   "metric": "Value-line slider",
   "value": "5 lines, every 3000 ms, 600 ms slide with cubic-bezier(0.25,0.1,0.25,1), 152 px step at 390"
  },
  {
   "metric": "Call-to-action dot pulse",
   "value": "scale 0 to 1 and fade 1 to 0, 1000 ms outCubic after 750 ms delay, looping"
  },
  {
   "metric": "Demo typing (Ask Preparoo)",
   "value": "40-55 ms per char (18-25 chars/s); touch delays x1.4; caret 2 px x 1em with 0.6 s step-end blink"
  },
  {
   "metric": "Phone hero: nav / headline / art card",
   "value": "57 px / 39 px Inter VF 600, line-height 0.9, -0.03em at y=80 / 366x620 at y=131, radius 32 px, 68.9% of the screen"
  },
  {
   "metric": "Phone hero: kicker / value line / call to action",
   "value": "Roboto Mono 14 px, +0.7 px, 70% white / BDO Grotesk 28 px/500, line-height 1.15 / 288x66 glass, blur 12 px, title 14 px, subline 10.4 px"
  },
  {
   "metric": "Desktop hero: headline / art card / value line",
   "value": "140.8 px (11vw), 1137 px wide / 1241x549, 66.6% of the screen / 44 px"
  },
  {
   "metric": "Words in the first phone screen outside the nav",
   "value": "19"
  },
  {
   "metric": "Page length",
   "value": "9,817 px = 11.6 screens at 390x844; 8,542 px = 10.7 screens at 1280x800; 9 sections"
  },
  {
   "metric": "Section heading size",
   "value": "48 px phone / 96 px desktop (Pricing 78 / 140.8 px)"
  },
  {
   "metric": "Phone touch swipes (finger distance, time, travel)",
   "value": "300 px slow drag gives 285 px; 300 px in 250 ms gives 464 px; 300 px in 80 ms gives 2,817 px; 150 px in 50 ms gives 1,836 px"
  },
  {
   "metric": "Desktop wheel",
   "value": "1 notch = 100 px; 5 notches = 500 px; no smoothing library"
  },
  {
   "metric": "HTML weight",
   "value": "1,111,207 bytes decoded, 144 KB transferred"
  },
  {
   "metric": "Browserbase time used",
   "value": "2 sessions, 71 s + 105 s"
  }
 ],
 "shots": [
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/filmstrip-m390.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/filmstrip-d1280.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/filmstrip-m390slow.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/frames/m390/m390-f00788.jpg",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/frames/m390/m390-f01288.jpg",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/frames/m390/m390-f01705.jpg",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/frames/m390/m390-f02055.jpg",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/frames/m390/m390-f02155.jpg",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/frames/m390/m390-f02521.jpg",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/frames/d1280/d1280-f02069.jpg",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/frames/m390slow/m390slow-f08487.jpg",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/frames/m390slow/m390slow-f09003.jpg",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/frames/m390-repeat/m390-repeat-f00835.jpg",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/m390-hero-at04787ms.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/m390-hero-at07229ms.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/m390-hero-at10546ms.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/m390-screen2.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/m390-screen3.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/d1280-hero-at03911ms.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/d1280-hero-at06634ms.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/d1280-hero-at09398ms.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/d1280-screen2.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/d1280-screen3.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/m390slow-hero-at15785ms.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/m390slow-hero-at19864ms.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/m390rm-hero-at03919ms.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/preparoo/m390rm-hero-at06640ms.png"
 ]
}
```

### research: what AI slop looks like (result)

```json
{
 "summary": "I built the AI-slop checklist. It is at C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/slop/slop-checklist.md and has three parts:\n- (a) 40 checkable tells in six groups: colour and light C1-C12, type T1-T6, layout L1-L7, imagery and mascot I1-I3, motion M1-M7, copy W1-W5. Each tell has a code check, a screenshot check, a pass bar for MockMob, the live page's current state with file:line evidence, and sources.\n- (b) What owned brands do in dark mode instead, measured where possible.\n- (c) The traps of a lime accent on near-black, with MockMob's own numbers.\n\nSources, in order: the owner's ui-ux-standards (sections 4, 5, 7, 8, 10 and 13), the research brain (AGENT_RULES.md, the 12-part test and rubric in ai-slop-independent.md, case T007), then web research. The web sources were impeccable.style/slop, the pixelslop detector thresholds, Fountain Institute's 7 tells, aismells, 925studios, prg.sh, devtake, Built In, RAXXO, 'The Linear effect', Linear's 2024 redesign post, Android/Material dark-theme guidance, the Robinhood 2024 identity, Nike's Volt guidance, Duolingo's character and shape posts, NN/g on the sparkles icon, typewriter accessibility notes, and the Aceternity and Magic UI component lists.\n\nI measured live production (www.mockmob.in) at 390 and 1440, Night and Day: 66 viewports, plus linear.app, raycast.com, duolingo.com and arc.net. I waited for the browser lock, took it, and released it. I opened every screenshot I drew a conclusion from. No code was edited, and the Cloudflare human check on Revolut was not bypassed.\n\nThe main finding: Night reads as neon because the same tokens become pure volt in Night and olive in Day. Night has 2.3 times Day's volt text at 390 (21 against 9) and 3.7 times at 1440 (26 against 7), and 2.5 to 4.2 times the lime-tint pixels. Four radial lime glows, two coloured glow shadows, a lime-lit top edge on the hero demo card, four glass panels on content and a pointer-lit volt dot grid are all still live. Night surfaces also barely separate (1.03 to 1.16:1), so containers rely on edges, and the system's 'active' edge token is 50% volt.\n\nThe checklist sets MockMob pass bars that are stricter than the generic detectors, following the owner's rules: one volt primary per viewport (W-075) and no glow (L-019). It keeps his two requested accents: 'CUET 2027.' (L-017) and 'MockMob' in the tour heading (L-030).\n\nTo re-measure, run `node capture.mjs`, then `node summarize.mjs`, in the same folder. Set `BASE=http://localhost:3452/` to measure a local build instead of production.",
 "findings": [
  {
   "topic": "Night neon: where it comes from",
   "observation": "Night maps the accent text and accent edge tokens to pure volt, while Day maps the same roles to quiet olive. So every kicker, link, badge, number and active border lights up in Night only.",
   "evidence": "marketing-theme.css:8 sets --accent-text #d2f000 and --accent-line rgba(210,240,0,.5) for Night. marketing-theme.css:20 sets #526700 and #9caf5d for Day; landing.css:32-34 sets the same Night values. A 50% volt line composites to #6f8007, hsl(68,90%,26%), at 4.35:1 against the ground; the page's neutral hairline is 1.23:1, so the volt edge is 3.5 times louder than the page's own structure. Measured volt text runs per pass, Night against Day: 390: 21 vs 9; 1440: 26 vs 7. Volt edges: 37 vs 23 at 390, 35 vs 24 at 1440. Mean lime-tint pixels: 3.70% vs 0.88% at 390, 1.95% vs 0.79% at 1440.",
   "files": [
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/src/app/marketing-theme.css",
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/src/app/landing.css",
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/slop/summary.json"
   ],
   "implication": "Fixing tokens and roles (volt only as a fill with dark ink in Night, neutral edges) removes most of the neon effect without cutting any section. This is checklist items C1, C2, C10 and C12."
  },
  {
   "topic": "Glow blobs and coloured glows are still live",
   "observation": "Four radial lime glows and two coloured glow shadows remain, even though a code comment says the hero aurora was removed as the glow that L-019 rules out.",
   "evidence": "Radial glows: home-refinements.css:16 (.085, behind the hero demo bay), compass-ladder.css:53 (.16) and :70 (.14), social-proof.css:37 (.22). The comment at social-proof.css:35 reads 'Apple-style glass over a soft volt glow'. The note about the removed aurora is at landing.css:221. Glow shadows: tour-screens.css:41 '0 0 20px -6px rgba(210,240,0,.45)' on the picked option, and tour-screens.css:14, a lime under-glow on every tour screen. On near-black these composite to olive fog from #1c230d to #37410b, which gives tint peaks of 13.76% (390 Night, Combo Planner), 11.8% (390 Night, Compass Pro) and 10.27% (1440 Night, Compass Pro).",
   "files": [
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/src/app/home-refinements.css",
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/src/app/compass-ladder.css",
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/src/app/social-proof.css",
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/src/app/tour-screens.css"
   ],
   "implication": "These break L-019 directly and are the clearest neon tells in screenshots (checklist C3 and C4). Day has its own versions (home-refinements.css:36, compass-ladder.css:65, social-proof.css:48), so remove them in both themes."
  },
  {
   "topic": "Hero lit edge and ambient tech patterns",
   "observation": "Three effects are still in the live hero: a volt hairline lighting the demo card's top edge, a hairline grid and dot matrix with radial fade masks, and a volt dot spotlight that follows the pointer on desktop. The close band also has the grid and dots. All of these were removed as slop in 'Hero v4' on 16 Oct, but that commit never reached main.",
   "evidence": "home-refinements.css:32-35 draws a linear-gradient of rgb(210 240 0 / .55) on .mm-screen::before; it composites to #7e930a at 4.78:1. HeroBackdrop.jsx with landing.css:234-262 draws the 4.5rem grid, the 1.5rem dots and the 13rem volt spot; the close band's layers are at page.js:441-444. Commit b6c40be4 ('Hero v4: type first, nothing ambient', 16 Oct, 1:29 am) removed 'the dot matrix and pointer-lit dots' and the 'stage-heading pulsing dot', and flagged 'the close band's aurora, grid and dots'. git branch --contains shows it only on web/land2-1015 and archive branches. Screenshot: shots/mm-1440-night-01-hero-pointer.png.",
   "files": [
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/src/components/landing/HeroBackdrop.jsx",
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/src/app/landing.css",
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/src/app/home-refinements.css",
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/src/app/page.js"
   ],
   "implication": "The owner-side process already ruled these out once (checklist C5 and C6). Re-applying that ruling is a refinement, not a cut."
  },
  {
   "topic": "Glass on content panels and flat Night surfaces",
   "observation": "Four content panels use glass (backdrop-filter), and three of them sit over lime glows. Night surfaces are a green-tinted near-black with almost no separation between levels, so containers depend on edges.",
   "evidence": "Glass: .lp-proof (hero-depth.css:35-48, blur 24px, saturate 170%), .lp-cpro (compass-ladder.css:52), .lp-combo (compass-ladder.css:69), .rl__summary (social-proof.css:36). Surfaces: the ground #0b100e is hue 156° with luminance 0.005; paper-raised #131a16 is only 1.08:1 above it. The demo screen gradient is 1.16:1 at its top and about 1.03:1 at its bottom, against about 15:1 for the same dark screen on Day paper. linear.app's body is #08090a with neutral border alpha 0.05 to 0.12 (median 0.08). The owner's standard is about #181818 ground and #212121 raised, neutral (ui-ux-standards.md:83).",
   "files": [
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/src/app/hero-depth.css",
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/src/app/compass-ladder.css",
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/src/app/marketing-theme.css"
   ],
   "implication": "Night needs designed surface steps and neutral edges; otherwise edges drift to lime again (checklist C7 and C11). Glass belongs on chrome only (W-071; ui-ux-standards.md:82)."
  },
  {
   "topic": "Volt does every job",
   "observation": "Volt carries 12 or more roles. The disciplined bar is 3: the brand marks (logo dot and Mobi), the one primary key fill, and the selected state as a fill.",
   "evidence": "Roles: kickers (home.css:43), 'CUET 2027.' (hero-scene.css:18), statement words (hero-depth.css:97), links (hero-scene.css:35), the Compass Pro and Combo Planner badges (compass-ladder.css:58), the correct tile (mistake-lab.css:58), the right count (:50), chart bars (mistake-lab.css:79, compass-ladder.css:40), the avatar (social-proof.css:90), the play button (:53), the focus ring (marketing-theme.css:7), the New badge (NavBar.jsx:26), plus numbers and timers ('780', '161K', '38:11'). Volt #d2f000 is hsl(68,100%,47%) with luminance 0.760, which is 85% of the body ink's luminance, at 14.8:1. The system's own rule says the opposite: marketing.css:25, 'Volt is a fill that carries dark ink, never a glow'.",
   "files": [
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/src/app/marketing.css",
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/src/app/mistake-lab.css",
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/src/app/home.css"
   ],
   "implication": "This is checklist C9 and C10 and trap (c)7: when volt is also the colour for 'correct', every lime word reads as a correct-answer signal."
  },
  {
   "topic": "Phone hero geometry and parity (LK70, LK67)",
   "observation": "On a 390x844 phone, the nav and the painted room take the top 45% of the screen. The only words in that band are Mobi's 'Tap me' line, and the headline starts at 47%. The phone hero (room plus a Mobi you tap) and the desktop hero (host Mobi plus pointer spotlight) tell different stories.",
   "evidence": "From the DOM audit: room 61-381px, h1 top 393px. The room height comes from --room-h: clamp(17rem,38svh,20rem) at hero-scene.css:165. The bubble's load line is heroTaps.mjs:8, 'Hi, I'm Mobi. Tap me.' Phone-only rules: hero-scene.css:150-246. Desktop-only: :285-307 and landing.css:272-276. Duolingo's phone hero fits its cast, the sentence saying what it is, and one key into one screen (shots/ref-duolingo-390-00-top.png).",
   "files": [
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/src/app/hero-scene.css",
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/src/components/landing/heroTaps.mjs"
   ],
   "implication": "This is checklist L1 and L2 and I3. With browser bars, the visible height is about 700 to 750px (an estimate), so the room takes more than half of what shows, which matches the owner's 'more than half' observation."
  },
  {
   "topic": "Type tells",
   "observation": "The fonts pass, apart from one leftover family. The type tells are: a kicker above each section heading, highlighter words, mono numbered counters, the Geist Mono family on figures and prices, a middle-dot meta line, and hero-metric number strips.",
   "evidence": "Kickers: page.js:269, 292, 307 and 372 render (385 does not in production). Statement accents: page.js:91. Counter '01 / 10': FeatureTour.jsx:190 and feature-tour.css:20. Geist Mono on .mm-measure: marketing.css:199-205 ('₹0', '73', '924.3'); impeccable lists Geist as an overused font. Trust line 'Free to start · Pro ₹99 a month · Cancel anytime': page.js:203 and heroTaps.mjs:51; ui-ux-standards.md:109 (T-124) bans middle-dot strings. Number strips: page.js:228-233, LiveStatsBand.jsx:9-34 (count-up) and the Instagram '199K+ / 100K+ / 690+'.",
   "files": [
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/src/app/page.js",
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/src/components/landing/FeatureTour.jsx",
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/src/components/landing/LiveStatsBand.jsx"
   ],
   "implication": "Checklist T1 to T6. Bricolage Grotesque, Hanken Grotesk and Literata pass, as the owner said."
  },
  {
   "topic": "Scroll steps depend on speed (LK69)",
   "observation": "A held story picks its step from where the page has scrolled, and the scroll itself is left at the browser's speed. So a fast flick crosses several steps and a slow drag can stop between two.",
   "evidence": "ScrollStory.jsx:8-14: an IntersectionObserver on 'beats' crossing the middle of the window, with 'wheel, trackpad, touch and keys … never caught' (the LK47 fix of 2 Nov). The tour's non-pinned track has scroll-snap-type: x mandatory with scroll-snap-stop: always (feature-tour.css:30-31), but the pinned tour turns it off (feature-tour.css:126).",
   "files": [
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/src/components/landing/ScrollStory.jsx",
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/src/app/feature-tour.css"
   ],
   "implication": "This is checklist M4. A fix must meet both L-027/LK69 (one gesture, one step) and LK47 (a single notch must not feel like a whole screen)."
  },
  {
   "topic": "Copy tells",
   "observation": "The copy has three instances of negative parallelism, about five clusters of staccato fragment tricolons, text walls in the tour slides, and a sparkles icon on 'Ask Mobi'. There are no hype clichés and no exclamation marks.",
   "evidence": "Negative parallelism: page.js:127 ('Fix why you got it wrong, not just the answer' and 'Fix why you missed it. Not just the answer.') and LabCinema.jsx:35. Tricolons: heroLines.mjs:11 and page.js:195, 282, 293 and 447. Tour bodies run 23 to 45 words, and one bullet at page.js:141 is 27 words. Sparkles: page.js:6 and 139. A grep for elevate, seamless, unleash, supercharge, world-class, delve and '!' found 0 hits.",
   "files": [
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/src/app/page.js",
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/src/components/landing/LabCinema.jsx",
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/src/components/landing/heroLines.mjs"
   ],
   "implication": "Checklist W1 to W3, I2 and W5. Treat these as a density problem: keep at most one such construction on the page."
  },
  {
   "topic": "Dead CSS that still carries slop",
   "observation": "Several slop devices sit in the stylesheets but are not rendered by any JSX. A future merge could bring them back.",
   "evidence": "The .lp-pill__dot infinite ping (landing.css:355-363), .lp-stage__live with 3 pings (home-refinements.css:41-42), the .lp-stage__path gradient hairline (home-refinements.css:49) and .lp-marquee (landing.css:540-553). A grep of components and app found no JSX use of these classes.",
   "files": [
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/src/app/landing.css",
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/src/app/home-refinements.css"
   ],
   "implication": "Deleting them stops a regression, the same way the 16 Oct Hero v4 cleanup was lost."
  },
  {
   "topic": "What owned dark brands do",
   "observation": "Linear uses a neutral near-black, neutral hairlines, almost no accent text, the real product UI and no glows. Raycast and Arc keep colour in one owned brand graphic. Robinhood, in volt's own colour family, uses its neon as 'purposeful pops' on black and neutrals, paired as black on neon. Nike limits Volt to small accents. Duolingo pairs its characters with a plain statement and gets depth from a solid keycap edge, not a glow.",
   "evidence": "Measured: Linear body #08090a, border alpha 0.05 to 0.12, 0 glows, saturated pixels 0.03 to 0.76%. Raycast body #07080a with one red key-art (18 to 23% saturated pixels in the hero). Arc #0b0b0b, with colour only in the logo. Sources: linear.app/now/how-we-redesigned-the-linear-ui ('reduce visual noise', 'a more neutral and timeless appearance'); robinhood.com newsroom 2024 ('purposeful pops of Robin Neon'; Robin Neon #ccff00 is hsl(72,100%,50%) against volt's hsl(68,100%,47%)); docs.robinhood.com/chain/brand-guidelines (black on neon; no gradients or shadows on the mark); gps.standards.nike.com/Brand/color-theory ('limit the use of Volt to accents that do not cover a large amount of space'); blog.duolingo.com/building-character and shape-language. Revolut returned a Cloudflare human check, which was not bypassed. HIGH (high.live) was not captured.",
   "files": [
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/slop/shots/ref-linear-1440-00-top.png",
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/slop/shots/ref-raycast-1440-00-top.png",
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/slop/shots/ref-duolingo-390-00-top.png",
    "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/slop/shots/ref-arc-1440-00-top.png"
   ],
   "implication": "MockMob already has an owned light source: the warm lamp light of the painted rooms, the lamp-lit subject objects and the shelf glow (home.css:68). Night atmosphere should use that amber light, not lime. Volt stays a fill (the key, the selected chip, Mobi)."
  },
  {
   "topic": "Generic detectors miss what the owner sees",
   "observation": "By generic thresholds MockMob is borderline, not flagged. The owner's own rules are stricter and do flag it, so the checklist uses those as its pass bars.",
   "evidence": "pixelslop flags neon text above 3 per page (#22), glows above 2 on a dark body (#3) and glass at 3 or more uses (#2). MockMob's worst viewports have 3 volt text runs and 2 glows, and the page has 4 content glass panels. The owner's rules: W-075, one volt primary per viewport; L-019, no glow. impeccable new-work.md:65 names the cluster: 'near-black with one neon accent and glowing edges'.",
   "files": [
    "C:/Users/atish/.claude/skills/impeccable/reference/new-work.md",
    "C:/Users/atish/Desktop/mockmob copy/mockmob-next/docs/brain/WEB-OWNER-LEDGER-2026-10-17.md"
   ],
   "implication": "Judge the page against the checklist's MockMob pass bars, not against generic detector scores."
  }
 ],
 "numbers": [
  {
   "metric": "Volt text runs per pass, Night vs Day, 390",
   "value": "21 vs 9 (2.3x)"
  },
  {
   "metric": "Volt text runs per pass, Night vs Day, 1440",
   "value": "26 vs 7 (3.7x)"
  },
  {
   "metric": "Volt edges per pass, Night vs Day",
   "value": "390: 37 vs 23; 1440: 35 vs 24 (includes one keycap bottom edge per primary key)"
  },
  {
   "metric": "Mean lime-tint pixel share, Night vs Day",
   "value": "390: 3.70% vs 0.88%; 1440: 1.95% vs 0.79%; peaks 13.76% (390 Combo Planner), 11.8% and 10.27% (Compass Pro)"
  },
  {
   "metric": "Volt luminance and contrast",
   "value": "0.760 (85% of ink 0.896); 14.8:1 on #0b100e; hsl(68,100%,47%)"
  },
  {
   "metric": "50% volt edge vs neutral hairline",
   "value": "#6f8007 at 4.35:1 vs #202522 at 1.23:1 (3.5x louder)"
  },
  {
   "metric": "Lime glow composites on Night",
   "value": ".085 → #1c230d; .16 → #2b340c; .22 → #37410b (olive fog)"
  },
  {
   "metric": "Night surface separation",
   "value": "raised 1.08:1; demo screen 1.03 to 1.16:1; same screen on Day about 15:1"
  },
  {
   "metric": "Statement dim words (opacity .18)",
   "value": "1.64:1 against the ground"
  },
  {
   "metric": "Phone hero geometry, 390x844",
   "value": "nav + room 0-381px (45%); h1 top 393px (47%)"
  },
  {
   "metric": "Content glass panels / lime radial glows / glow-shadow rules",
   "value": "4 / 4 / 2"
  },
  {
   "metric": "Infinite animations in view, 1440",
   "value": "55 across 17 viewports (mostly Mobi idle loops)"
  },
  {
   "metric": "Linear reference",
   "value": "body #08090a; border alpha 0.05-0.12 (median 0.08); 0 glows; saturated pixels 0.03-0.76%"
  },
  {
   "metric": "Checklist size",
   "value": "40 tells: C12, T6, L7, I3, M7, W5"
  },
  {
   "metric": "Viewports captured",
   "value": "66 MockMob (390 and 1440, Night and Day) + 20 reference shots; capture 2:26-2:30 am IST, 4 Nov 2026"
  }
 ],
 "shots": [
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/slop/shots/mm-390-night-00-hero.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/slop/shots/mm-390-day-00-hero.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/slop/shots/mm-1440-night-00-hero.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/slop/shots/mm-1440-night-01-hero-pointer.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/slop/shots/mm-390-night-05-tour.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/slop/shots/mm-1440-night-06-tour-mid.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/slop/shots/mm-390-night-04-lab-mid.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/slop/shots/mm-390-night-09-cpro.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/slop/shots/mm-390-night-14-insta.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/slop/shots/contact-390-night.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/slop/shots/contact-1440-night.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/slop/shots/contact-1440-day.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/slop/shots/contact-390-day.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/slop/shots/ref-linear-1440-00-top.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/slop/shots/ref-raycast-1440-00-top.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/slop/shots/ref-duolingo-390-00-top.png",
  "C:/Users/atish/Desktop/mockmob copy/wt-1104-web-polish/tmp/home-1104/slop/shots/ref-arc-1440-00-top.png"
 ]
}
```

Stopped before finishing: audit: live home page; scroll forensics (phone); inventory: Mobi and brand assets
