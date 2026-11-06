# Learn as its own section: navigation v2 (CTO spec, 31 Oct 2026, 11:30 pm) -- REJECTED by the owner, 31 Oct 11:50 pm

> He saw the renders (built as `&nav=n2`, commits d54f5bd8a and 998903ae2, both reverted) and said the current structure is cleaner. In the app,
> Practice | Learn | Your papers already gives Learn its own place, and a tab whose only extras are Find and Explore adds little.
> The current navigation stays. Find lives inside Learn, and Explore's feed is to become a standout phone feature, shown to him as a
> live prototype (LK18).


Owner, 31 Oct: Learn "has now expanded a lot, so we can make it into another part", but the app's bar cannot grow. This spec
answers both. It is drawn for him first (preview `&nav=n2`), not shipped.

## The split
- **Practice** is testing yourself: practice sets and mocks, Your papers, Saved.
- **Learn** is learning: chapters (Key cards, lessons, questions), Find and revise, and the Explore feed.
- Explore moves from Practice to Learn, because its feed now mixes Key cards and questions. Every old route keeps working.

## Website, desktop (1440)
The sidebar has five places, the same as the phone bar plus Learn:
```
Today
Practice
   Your papers
   Saved
Learn                      27      (Key cards due, all subjects, tabular)
   Find and revise
   Explore
Mob
   Your standing
You
   ...unchanged
```
The Start key, the Mobi door and Night and Day do not change.

## Phones (website at 390 and the app): the bar does not change
The bar stays Today, Practice, Start, Mob, You. The Practice tab gets two halves.
- **Title switch.** At the top of the Practice tab, in place of the page title, the words `Practice` and `Learn` sit side by
  side in display type, 28 px.
  - The active word is full ink. The other is muted (text-3).
  - A 2 px volt underline sits under the active word. It slides between the words in 220 ms (cubic-bezier(0.32, 0.72, 0, 1)).
  - Tap a word, or swipe sideways on the content, to switch.
  - Learn carries its due count as a small tabular number after the word: `Learn 27`.
  - With reduced motion, the underline jumps and the content cross-fades in 120 ms.
- **Each half has one row of doors** under the switch, in the existing tab row style. All of them fit, so no peek cue is
  needed.
  - Practice: `Practise | Your papers | Saved`.
  - Learn: `Chapters | Find | Explore`. This replaces the Chapters and Find toggle on Learn home.
- **Memory.** The tab opens on the half the student last used. A deep link chooses its half: `/learn*` and `/explore` open
  Learn, and everything else opens Practice.
- **Badge.** The bar's Practice badge keeps its open-mistakes count. The Learn due count lives on the switch, so the bar
  never shows two numbers.
- **Learn still has its own doors from elsewhere** (A8): the Start sheet row "Learn a chapter", the Learn move on Today, and
  "Open {chapter}" on results.

## Considered and not chosen
- **Swap Mob out of the bar for Learn.** This loses the social place he built (chains, games) and moves a daily habit to a
  sheet.
- **Long-press the Practice tab for Learn.** It is hidden, and a first-time student would never find it.
- **Rename the tab to "Study".** That clashes with Study mode on Key cards.
