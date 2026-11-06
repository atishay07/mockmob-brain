# Release 5: where to look

Written 18 Oct 2026 for the owner, after he said release 5 "seems the same" (D33). For each item: his words, where to look, what changed, and whether you can see it. Where a change is small or not visible, it says so.

Run it yourself: the dev server for this branch is at `http://localhost:3205` (phone on the same wifi: `http://192.168.1.8:3205`). The signed-in pages below need no sign-in. They are fixture pages with made-up data and a white "Development preview" box at the top (that box is not part of the app).

- Practice: `/preview/arena?view=dashboard&plan=pro`
- Ask Mobi: `/preview/arena?view=prepos&plan=pro`
- Help and FAQ: `/preview/arena?view=help&plan=pro`
- Result, your 10-question 58-second paper: `/preview/arena?view=result&paper=practice10&plan=pro`
- Review: `/preview/arena?view=review&plan=pro`
- Revise: `/preview/arena?view=revise&plan=pro`
- Concepts (was Learn): `/preview/study`
- The theme switch: any page. On the app it is in the top bar from tablet width up. On the landing it is in the top bar at every width. Click it.

Do not sign in on this dev server. It is wired to the production database.

## What release 5 does not contain

If you look for these you will see no change, and that is expected:

- Today (D1 to D3, D25 to D27). Not touched.
- The Ask Mobi redesign (D6, D12). Only the Night colour was fixed (item D7). The layout is the same.
- Icons (D8), badges (D19), Colleges and community changes. Not touched.

## Pictures: how they were made

Headless Chrome at 390 x 844 and 1440 x 900, Day and Night (Night = `localStorage['mm:theme:v1']='dark'`), saved in `docs/brain/r5-where-to-look/`. File names read `<item>-<390 or 1440>-<day or night>-<before or after>.jpg`.

- **before** = release 4 (main 9578ee66) run on a spare port, with the same fixture pages. For the result page the new 10-question fixture data was copied into release 4 so both sides show the same paper. The two landing-page items use the live www.mockmob.in.
- **after** = this branch on port 3205.
- `pixel-diff.json` holds, for every pair, the share of changed pixels and the share of lime pixels before and after.

## D5: Repairs and Ask Mobi are missing from Practice

His words: "no one will be able to see it ever. The placement is really bad."

Verdict: **visible.**

Where: Practice. One new line under the subject row (Accountancy, Economics...): "3 questions to repair in Accountancy", with "From your one session, and 5 more in other subjects", and two keys, **Review and repair** and **Ask Mobi**. It follows the subject you pick. The Review tab also now carries a count badge (8). The mode tiles, Fine-tune and session card are unchanged on purpose (D4).

On a phone the line is on the first screen once the preview box is out of the way (that is the `x-d5-practice-nobanner` picture). With the preview box it sits at the bottom edge.

Pictures:
- `d5-practice-1440-night-before.jpg` and `-after.jpg` (and `-day-`)
- `x-d5-practice-nobanner-390-night-before.jpg` and `-after.jpg` (and `-day-`)
- `d5-practice-full-390-day-before.jpg` and `-after.jpg` (the whole page; the dock is drawn over it, that is a screenshot effect)
- Ask Mobi opened in place, from the first agent: `docs/design-decisions/captures-practice-repairs-1018/practice-ask-mobi-open-390-day.png`

## D7: Night is "in-your-face" now, it was subtle

His words: "It was very subtle previously, the night mode. Now it is very in-your-face."

Verdict: **visible on Ask Mobi only. Not a general Night change.**

What was found: compared with the last production before release 2, the Night colours, accents and glows are unchanged everywhere except two places. Those two were fixed.
1. Ask Mobi, "Next step" card: the key "Start 10 practice questions" had become a full-width solid lime bar. In Night it is now an outline again (dark ground, strong line, light text).
2. The glowing Mobi orb that sat in the sidebar's Help door. The door is gone (see D11), so the orb is gone from the sidebar. The orb's lime glow is also dimmed in Night where it still appears.

Everything else in Night looks the same as release 4: Practice's "Start Quick practice" key, the Start key in the phone dock and lime links are still lime. If those are what feel loud, release 5 did not touch them.

Where: Ask Mobi page, Night, "Next step" tab. Lime pixels on the first screen at 1440: 2.83% before, 0.07% after. Whole page at 390: 3.14% before, 0.75% after. Day is unchanged.

Pictures: `d7-ask-mobi-1440-night-before.jpg` and `-after.jpg`; `d7-ask-mobi-full-390-night-before.jpg` and `-after.jpg` (the key is below the first screen on a phone).

## D10: the light/dark switch animation is worse than before

His words: "The animation is not as good quality as it used to be so change that."

Verdict: **visible, clearly. Best item to try yourself: click it.**

Before (release 2 to 4): a white disc with a small sun icon that cross-fades to a moon icon. After: the old version is back. The thumb is the sun itself, with a glow. A cloud sits beside it. When you switch to Night the sun is eclipsed into a crescent while it slides across, the cloud sinks and the stars land. It also stands still when Reduce motion is on in the app's own setting, not only when the phone asks.

Where: the switch in the top bar (app at tablet width and up; landing at every width). Frame-by-frame strips, 0 to 760 ms, Day to Night and Night to Day:
- `d10-frames-before-release4.jpg` and `d10-frames-after-release5.jpg`
- Resting state, big: `d10-switch-landing-1440-day-before.jpg` and `-after.jpg` (and `-night-`), same for `d10-switch-app-1440-`.
- The landing page around it is the same: `d10-landing-top-*` differ by 1 to 3% of pixels, which is only the switch.
- The "before" landing pictures are the live site. The frame strips were made earlier by the theme agent (`artifacts/r5-theme-1018/`).

## D11: Help is the wrong word and the wrong place

His words: "If you want to put it you can create a separate standing doc [a standalone page] instead of a scroll."

Verdict: **partly visible.** Help was already a page of its own in release 4. What changed around it is visible.

What changed:
- The page title is now "Help and FAQ" (it said "Help").
- The sidebar no longer has the Help door with the orb and its pop-up menu. "Help and FAQ" is a plain link in the Account group, next to Account.
- The foot of the sidebar is now only the Night / Daylight / Match device row.
- At 1440 x 900 the whole sidebar now fits. In release 4 the list ran past the bottom of the window after "Account", so Help and the theme row were below the edge.
- On a phone, More no longer has the "Help" chip. "Help and FAQ" is a row inside the account card at the top of the sheet.

Pictures:
- `d11-sidebar-1440-night-before.jpg` and `-after.jpg`
- `d11-help-page-1440-day-before.jpg` and `-after.jpg`
- `d11-more-sheet-390-night-before.jpg` and `-after.jpg`

## D13: the round pulse on the phone nav looks weird on Practice

His words: "In practice, it's a bit weird, like text and line."

Verdict: **visible, but subtle.** The round pulse itself is the same shape. What changed is what sits under the bar.

On Practice the lime-edged mode tile ran right under the capsule, so its edge and the word "Included" showed next to the pulse, which read as "text and a line". The dock now stands on a floor in the page colour, so whatever scrolls under the bar fades out. On phones under 380 px wide the labels are 10 px so the pulse never touches a letter. The only other change on Today's bar is the new count badge on Review.

Where: Practice at 390 wide, look at the bar with the tiles scrolled under it. The `x-d13` picture holds the same content under the bar in the after picture. Today's bar is nearly identical (2%) before and after, as he said it was fine there.

Pictures:
- `d13-nav-practice-390-day-before.jpg` next to `x-d13-nav-practice-same-place-390-day-after.jpg` (and `-night-`)
- `d13-nav-today-390-day-before.jpg` and `-after.jpg`

## D15: result, "Repair first", "Repair in 1", "Check it here"

His words: "In 1 and 3 it is showing repair first, and then it is just showing repair in 1 ... a very confusing UI."

Verdict: **visible, but small.** The wording changed, not the layout.

What changed, in "Your 5 mistakes": the volt "Repair first" key is now "Repair", with the same volt outline marking the one that comes first, so one label is used on every row. The lines under the heading say the two steps once: "Each mistake has one next step: Repair, then Check it held on a new question." Out-of-credit rows also say Repair. The opened row's key says "Repair Q6", matching the "Do this next" card. The "Do this next" card above is unchanged (0%).

Where: result page, "Your 5 mistakes". With one mistake already repaired (`&return=1`), release 4 showed "Check it held", "Repair first" and "Repair" together. Release 5 shows "Check it held" and "Repair".

Pictures:
- `d15-next-and-mistakes-1440-night-before.jpg` and `-after.jpg`
- `x-d15-mistakes-one-repaired-390-day-before.jpg` and `-after.jpg`

## D17: the answer bar is too compact, the replay shows only grey boxes

His words: "If there are just 10 questions, then show it according to 10 questions only."

Verdict: **visible for a short paper. Not different for a 50-question paper.**

What changed, on your 10-question, 58-second paper:
- The answer bar (the numbered boxes in the result's summary card; on a phone it is just under the first screen, scroll down) is now sized to the paper. Ten boxes fill one line on a desktop, or two even lines of five on a phone, up to 20 questions. In release 4 they were small and left-packed, with a gap on the right.
- The Replay (open "See every change", press Play): the old version was a thin strip of grey cells. Now each question has its own slot with its number and time on it, a clock runs (0:17), and one line says what is happening ("Q4 opened"), one event about every half second. A dot marks a changed answer.
- The Replay's own map has one slot per question. Up to 20 questions it stays open; above that it folds, with Expand and Collapse (not captured here, the 58-second paper has 10).
- The summary bar of a 50-question paper (`paper=avg`) looks exactly the same as before. That is by design: longer papers keep the wrapping layout.

Pictures:
- `x-d17-bar-10q-1440-day-before.jpg` and `-after.jpg`; the same at 390
- `d17-replay-playing-390-day-before.jpg` and `-after.jpg`; `d17-replay-open-1440-night-before.jpg` and `-after.jpg`
- `x-d17-bar-50q-*` pairs: identical

## F15: Learn and Review

His words (D18): "In the review section, we can integrate the weak chapters somehow, because that's actually more useful." (D20): "there is no separate learn tab ... Learn, but again, needs refinement."

Verdict: **visible.** Review is a different page. Revise and Concepts are new or rebuilt.

- **Review** (sidebar, phone dock): was a long page: a count, one lime key ("Open Accountancy, 17 Oct"), Revise and Your rules rows, and a chart of your last papers. Now two tabs, Mistakes and Papers. Mistakes opens on your costliest chapter ("Admission of a partner, 35 marks lost"), one key "Repair Q42", then the open mistakes grouped by chapter with marks lost, Revise and your repairs on the right. The Review tab carries a count badge. Pictures: `f15-review-1440-day-before.jpg` and `-after.jpg`, also 390 and Night.
- **Revise** (from Review): one run over questions you got wrong, repair checks and concept cards, with a progress bar. Pictures: `f15-revise-1440-day-before.jpg` and `-after.jpg`. Part of the difference is richer fixture data in release 5's preview, so judge the layout, not the wording.
- **Result page, new line:** under "Your 5 mistakes", "Learn the idea first" links the lesson for the chapter you lost most in (see `d15-next-and-mistakes-1440-night-after.jpg`, bottom). It has no "before"; release 4 had nothing there.
- **Concepts**: the page that used to be called Learn. It now leads with the lesson to read next, then "Where you lose marks" by chapter, with search and subject chips. Pictures: `f15-learn-1440-day-before.jpg` and `-after.jpg`.
- **Note on naming:** the sidebar item and the page title now say **Concepts**, not Learn. D20 asked for a clear place for Learn. If you wanted the name Learn kept, that is one word to change.

## Checks for this release

See the STATUS entry for the 18 Oct 2026 release 5 check. In short: eslint clean on the 66 changed files, the app, recovery, learning, auth, billing, nta, today, mob, subjects, du and dock suites pass with no failure, and `next build --webpack` passes. No test was changed.
