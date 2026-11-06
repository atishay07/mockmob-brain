# Pro nudge copy, web (18 Oct 2026)

For the owner (D79-D81, D84). The words live in `src/lib/proNudge.mjs`; `data/tests/pro_nudge_1018.test.mjs` checks them.
To switch an option, reorder `HEADLINE_OPTIONS` or `KEY_LABEL_OPTIONS`; whichever is first is the one in use.

Every line below is true for what Pro includes in the code today:
- unlimited Quick practice and Full mocks, each paper built fresh from one central bank (`src/lib/paperCopy.mjs`);
- no credits needed for practice;
- NTA mode (50 questions, 60 minutes);
- Smart practice;
- full chapter review;
- Compass Pro;
- a set difficulty;
- unlimited saves (Free keeps 25);
- the full Mob.

Ask Mobi replies still use credits on Pro. So the copy never says "no credits" without "for practice" beside it.
The rules: no "!", no emoji, no countdowns, no fake scarcity, and no numbers the student's record does not hold.

## The Upgrade sheet headline (generic sheet: the credits chip, the Start sheet, any See Pro)

| # | Headline | Why |
|---|---|---|
| 1 (my pick) | **Unlimited mocks. No credits needed.** | Your own words (D79), and it is the USP. Two short claims a student can repeat. |
| 2 | Practise until exam day feels familiar | Warmer, and about the result rather than the feature. It is softer on the offer. |
| 3 | Every mock you need, from one central bank | It names the bank, the reason the mocks never run out. It is a little long for a phone headline. |

The lede under it: "Every paper is built fresh from one central question bank, so there is no fixed set of mocks to run out of. Pro adds NTA mode, Smart practice and full chapter review, all for one price."

## The key (the one lime button)

| # | Key | Why |
|---|---|---|
| 1 (my pick) | **Get Pro for ₹99** | The price sits on the key, so nothing is hidden. "Pro" is right whichever feature opened the sheet (NTA, Smart, the Mob, saves). |
| 2 | Get unlimited mocks for ₹99 | It sells harder on the generic sheet, but it reads oddly when the student tapped NTA mode or the Mob. |
| 3 | Unlock Pro for ₹99 | The plain choice. "Unlock" frames Free as locked, which goes against the calm tone. |

When monthly Pro is on sale, the key follows `offer.js`: "Start Pro for ₹99/month". The web sheet never shows the Play price, and the app never shows the web price.

## Per-feature headlines (when a Free student taps a Pro feature)

| Tapped | Headline |
|---|---|
| NTA mode | Sit CUET before CUET |
| Smart practice | Practise what is costing you marks |
| Difficulty | Choose how hard it gets |
| Full chapter review | See every chapter that costs you marks |
| Compass Pro | Know what your practice is worth |
| Saves full (the 26th save) | Your 25 free saves are full |
| Credits chip, or short of credits for a set | Stop rationing your practice |
| The Mob | See your whole Mob, every week |
| After a result | Keep the momentum going |
| First-session pop-up | Paper done. Now take the limits off. (never counts papers: the sheet can open on a later paper in the first session) |

## Inline lines (one quiet line, one action)

| Where | Line | Action |
|---|---|---|
| Practice, under a set's cost | No credits needed for practice with Pro. Every set and every Full mock, included. | Get unlimited mocks |
| Account > Credits, under 50 credits | 40 credits left, short of a 50-credit Full mock. With Pro, practice needs no credits at all. | Get unlimited mocks |
| After a result | Keep the momentum. With Pro, your next paper and every one after it need no credits. | Get unlimited mocks |
| Review, an open chapter | Smart practice in Pro weights every set toward chapters like this one. | See Smart practice |
| Start sheet | Unlimited mocks, NTA mode and Smart practice. One Pro price, no credits needed for practice. | See Pro |

## Personal lines (D81: shown only when the fact is real)

- "You have sat 3 full mocks. With Pro, sit as many as it takes."
- "You spent 42 credits on practice this week. With Pro, that would be 0."
- "NTA mode in all 4 of your subjects..." This shows only when every one of the student's subjects has an NTA blueprint; otherwise it names one subject, or falls back to the plain line.
- "Partnership Fundamentals had the most mistakes on your paper..." This shows only when one chapter clearly leads, with at least 2 mistakes and no tie.

## When it shows (frequency caps)

- **The first-session pop-up:**
  - It shows once ever, after the first scored paper in the browser session that finished onboarding (within 6 hours).
  - It never shows on onboarding or in the 2 minutes after it.
  - It never shows over a paper or over another open sheet.
  - It is marked as shown only when it actually opens.
- **Inline lines:**
  - At most one per screen. The Start sheet shares the page's claim.
  - None on a paper.
  - A dismissed line stays quiet for 7 days.
  - Any "Not now" on the sheet quiets every inline line for a day.
  - Pro students see none of it.
