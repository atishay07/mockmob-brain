# Explore feed v2: a phone-first live prototype (CTO spec, 1 Nov 2026, about 12 am)

**Owner, 31 Oct, 11:50 pm (LK18):**
- The current navigation stays. Learn is already its own door in Practice.
- He wants "to keep the Explore feed and make it a very cool feature on the mobile app".
- He will judge only "an actual live prototype". This builds that on the website preview at phone size, opened on his own
  phone over the home Wi-Fi.
- App parity comes after he approves it.

The feed today (`src/components/learn2/feed/ChapterFeed.jsx`) is the run player with a different label: a card in a box, a
grey hint paragraph and a volt "Show answer" key. It does not feel like a feed. v2 is a full-screen vertical feed, one item per
screen, swiped up like Reels. It stays a study tool: honest, calm Night, nothing childish (his promo-film verdict). It keeps
the brand: volt on charcoal, Bricolage display type and the lamp-lit subject objects.

## 1. The feed screen (390 px; it must also work at 360 and 430)
- **Full screen, no bar, no top bar.** The feed is a focus place.
- **Top, 12 px from the safe area:**
  - Segmented progress ticks, one per item, like stories: 2 px tall with 3 px gaps. Done items are ink-2, the current item
    fills volt from left to right, and later items are a hairline.
  - Under the ticks: the close X (44 px target) on the left; the chapter title on the right, 13 px, one line, truncated.
    The title is the real chapter title, never "Partnership Fundamentals" (R9).
- **Paging:** vertical scroll-snap (`scroll-snap-type: y mandatory`). Each item is 100dvh. Swipe up for the next item and
  down for the previous one. On the desktop, Arrow keys and Space work too.
- **Behind each item:**
  - The chapter's subject object (the existing SubjectObject art), 220 px, at 18% opacity, softly blurred (6 px), anchored
    bottom-right and bleeding off the edge.
  - It drifts 8 px up as the item comes into view, in 600 ms, ease-out.
  - This is the only decoration. No gradients and no glow.

## 2. A Key card item
- **The kind line:** `Definition`, with `Must-know` in volt text when the card is Must-know.
- **The front:** centred in the upper two thirds, display type, 30 px, tight leading. Nothing else, so the screen is calm.
- **Tap anywhere on the card** to turn it over:
  - The card does a 3D rotateY flip, 420 ms, cubic-bezier(0.32, 0.72, 0, 1), with backface hidden.
  - The back shows NCERT's line at 20 px, then the source in text-3: "NCERT Class 12, Accountancy Part 1, Ch 2".
  - Before the first flip, one quiet line sits at the bottom: "Tap to turn it over". It shows only on the first card of a
    student's first feed.
- **Right rail, 16 px from the edge, at about two thirds down,** in the Reels position. Each icon is 44 px with a 12 px label
  under it:
  - **Keep** (a bookmark glyph) adds the card to Revise. On tap the glyph fills volt with a 1.15 pop over 180 ms, and a small
    copy of the card flies to the rail's foot (320 ms). The label becomes "Kept".
  - **Chapter** (a book glyph) opens the chapter page.
- **A swipe up without Keep schedules nothing.**
- **Free:** Keep works within the 5 open cards; after that the label reads "Pro".

## 3. A question item
- **The head:** `Question` or `You missed this in Mock 4 on 24 Oct`, in text-3. Then the stem at 22 px.
- **The options:** four big rows, at least 56 px tall, full width, with the key letter and the text.
- **On a tap the server grades it** (no key on the client before the answer).
  - **Right:** the row fills volt with ink text, and a 1.04 settle over 200 ms. A short haptic: `navigator.vibrate(12)`
    where supported. The top-right streak chip shows `4 in a row` when the run reaches 3 or more right answers. The chip
    counts up in place, with no confetti.
  - **Wrong:** the row shakes 4 px twice (240 ms) and turns to the bad colour. The right row outlines volt. A sheet rises
    from the bottom (280 ms) titled "The line you needed", holding the card's NCERT line and the source. The haptic is
    `navigator.vibrate([8, 40, 8])`.
  - **Either way:** "Swipe up for the next one" fades in at the foot after 600 ms, the first time only.
- **Rail:** Save (the question goes to Saved) and Chapter.

## 4. Rhythm
- **Item order:** a Key card first, then roughly two cards per question. A question that links to a card comes 3 to 6 items
  after it (A3).
- **Checkpoint every 8 items:** one interstitial screen, the only one.
  - It shows a large tabular number: `5 of 6 right` or `6 cards seen, 2 kept`.
  - Under it, one line: "Keep going, or stop here and save what you kept."
  - It has two keys: `Keep going` (volt) and `Stop here`.
  - It auto-advances only on a swipe.

## 5. The end screen
- **Title:** "10 minutes on Admission of a Partner".
- **The kept cards** fan open as a pile of small cards, with the count. The return day comes from the real stamp
  ("Back Tue").
- **Lines:** "Questions: 5 of 6 right" and "Fixed: 1 old mistake".
- **Keys:** the lead, `Another 10 minutes` (volt), then `Next chapter: Retirement of a Partner` and `Back to Explore`.
- **Free, the second feed of the day:** the end screen's lead is replaced by "Your free feed for today is done. Pro has as many
  as you like." with a `See Pro` text button. There is no modal (LK15).

## 6. The way in, on the Explore page (phone)
- **Above the question list:** a horizontal row of chapter covers that snap one per swipe. Each cover is 280 x 360 px.
  - At the top of each cover sits the subject object, lamp-lit, 140 px. Under it: the chapter title at 22 px, then "10
    minutes, 16 Key cards and 5 questions" in text-2.
  - At the foot of each cover: a volt `Play` key.
  - The first cover is the student's suggested chapter (due cards or open mistakes first), marked "For you" in text-2.
- **Length:** a small `5 | 10 | 20 min` segmented control above the row, applying to all covers.
- **The question list below stays as it is.**

## 7. Find inside Learn (the same prototype)
- **Learn home drops its Chapters | Find toggle.** In its place is a search field under the subject row: "Search 868 Key
  cards".
- **Focusing the field opens Find in place:** the shelves (Due today, Missed lately, In Revise, Must-know) show until the
  student types, and then the results show. Cancel returns to the chapters.

## 8. Motion and accessibility
- **Reduced motion:** no flips (cross-fade 120 ms), no drift, no shake (the colour change only), and no card flight.
- **Touch targets:** at least 44 px. Focus is visible.
- **Screen readers:** the feed is a list with aria-roledescription "feed". Each item announces "Card 3 of 21".
- **Layout:** no layout shift, and no horizontal page scroll at 360.

## 9. Prototype routes (dev preview)
- `/preview/arena?view=learn2-feed&decks=real&plan=pro&student=commerce&chapter=<key>&min=10` opens the feed.
- `view=explore` (or the existing Explore preview view) opens the covers.
- `view=learn2` opens Learn home with the search field.
- `plan=free` shows the Free limits.
- Answers are graded through the existing in-memory `/api/learn/*` preview routes. Nothing reaches production.
