# Conversion pass, 10 Nov 2026: what was found, what changed, how to measure it

Branch `web/1110-conversion` (worktree `wt-1110-convert`, from main `5dbcea349`). Local only: not pushed, not deployed.
Owner brief (pasted in chat, 10 Nov about 1:40 am IST): walk the website as a first-time CUET student, choose and
implement the most valuable polish and conversion improvements, define the conversion event, audience and baseline for
the "10x conversion and a 50%+ rate" ambition, verify on phone and desktop, show what changed and how to measure it.
Research used: the four UI Craft and Conversion mini-skills and the three video notes (AI OS handoffs
`20261109T200417.205367Z-36b2f102`, `...200416.966562Z-c66067d4`, `...200416.719155Z-88c6270b`, `20261109T163649.986015Z-fdf9f6c7`,
`20261107T201947.797018Z-c242d906`).

## 1. The funnel evidence that exists (read 10 Nov 2026, production, read-only)

| Stage | Number | Source |
|---|---|---|
| Home page visits | none recorded | Vercel Web Analytics is not enabled; `funnel_daily` holds 0 rows; no browser code called the counter before this branch |
| Sign-ups, Apr to May 2026 (CUET 2026 season) | 1,493 (63 in April, 1,430 in May) | `users.created_at` |
| Sign-ups, June 2026 to 9 Nov 2026 | 61 (8, 15, 11, 10, 16, 1 by month) | same; some are our own test accounts |
| Finished a first set within 24 hours of signing up | 715 of 1,493 (48%) last season; 22 of 61 (36%) since June | `attempts.completed_at` against `users.created_at` |
| Ever finished a set | 778 of 1,493 (52%); 22 of 61 | same |
| Paid (captured) in May 2026 | 96 students, 6.7% of May's 1,430 sign-ups; 132 students opened an order, 57 had a failed payment | `payments` |

So the only measured rates are after sign-up. The visitor stage, where "10x" would be judged, has no baseline at all.

## 2. Definitions (so the two goals can be compared with anything)

- **Event:** a finished sign-up (`signup_complete`, counted on the server when the account row is first created).
- **Eligible audience:** signed-out visitors opening the home page in a browser, not bots, not browsers that send Do Not
  Track or Global Privacy Control (`landing_view`).
- **Unit and window:** page loads per IST day, split by device kind (Android browser, iPhone browser, desktop); the admin
  page reads 14 days. It counts loads, not people: the counter keeps no id by design, so one student who opens the page
  twice counts twice.
- **Rate for the 10x goal:** `signup_complete / landing_view`, web device kinds only, same window. Baseline: unknown until
  the counter is on. Ten times a rate only means something once two weeks of the baseline exist.
- **Where a 50%+ rate is a fair reading:** not home page loads to sign-ups (no consumer site does that with cold visitors).
  The two stage rates that already sit near it: sign-ups who finish a first set within 24 hours (48% last season, 36% since
  June), and sample finishers who then choose sign-up (`signup_click / sample_done`, unmeasured).
- **Guard rails (a lift on the event must not hide a loss here):** `first_practice_started / signup_complete`, payments, page
  errors, load time.
- **Volume:** about 12 sign-ups a month now. No controlled test can read out at this volume; until creator posts or the
  season bring traffic, every comparison is before and after, and is a hypothesis.

## 3. The one switch that makes this measurable (owner decision, open since 16 Oct)

The aggregate funnel was built on 15-16 Oct (`funnel_daily`, `/api/funnel`, `src/lib/funnel.js`, `/admin/funnel`): step names
only, no cookie, no id, nothing under Do Not Track. Both migrations are applied on production (checked 10 Nov:
`funnel_increment`, `funnel_count_once`, `users.funnel_seen`, all 14 steps in the check). It has counted nothing because
`FUNNEL_ENABLED` is off and because the home page never sent its steps (the landing was on another branch on 16 Oct).
This branch sends them. After it ships: set `FUNNEL_ENABLED=true` in Vercel (production), redeploy, open the home page
once, and check `/admin/funnel`. Off again = unset it and redeploy.

## 4. What the walk found (live site, 390 and 1440, Day and Night, 10 Nov)

Kept as it is, because it already works: the hero reads in under a second and says who it is for, what it does and the
next action; the five-question sample is a real, ungated result; the film, the Lab, the tour and the DU tools are the
product's own; hero key to a usable sign-up form takes about 0.85 s.

Where a willing student lost momentum:
1. **The sample's result did not survive the click.** The card says "3/5 ... Q2 Accounting equation, Q4 Partnership ...
   Sign up free, then choose chapters like this one in Practice." The next screen said "Start your CUET 2027 practice.
   Keep your recorded mocks ... together." to everyone. The warmest visitors on the page were greeted as strangers.
2. **A floating note covered the headline.** On a first visit on a phone, "Light or dark? Your call" hung over
   "CUET 2027." from 1.4 s to 9 s, and over Mobi's desk after "Try 5 questions first".
3. **Nothing was being counted** (section 3).

## 5. What changed on the branch

| Change | Files | Why |
|---|---|---|
| The sample's score and missed chapters go with the reader to `/signup`: "You got 3 of 5. Keep going." and "Sign up free, then choose chapters like Accounting equation and Partnership: admission of a partner in Practice." Five of five is pointed at the full mock; none or one never puts the score in the headline. Kept in the browser only for a day, never sent, cleared once the account exists; a Mob or friend invite keeps its own words. | `sampleCarry.mjs` (new), `DemoDrill.jsx`, `SignupPageClient.jsx` | The promise now survives the click (finding 1) |
| On phones the first-visit theme note is no longer drawn; the switch's own soft pulse is the prompt. From 960 px it is unchanged. | `marketing-theme.css` | Nothing floats over the page's first words (finding 2) |
| The home page sends its funnel steps: `landing_view` (guests only), `sample_started`, `sample_subject_chosen`, `sample_done`, `signup_click`, `login_click`. Each once per page load, the step's name only. | `FunnelBeacon.jsx` (new), `DemoDrill.jsx`, `page.js` | Makes the baseline and any lift readable (finding 3) |
| Tests | `sampleCarry.test.mjs` (6 tests, in `test:app`) | Locks the three changes |

## 6. Hypotheses and how each would be read

| Change | Expected to move | Counter-signal |
|---|---|---|
| Result carried to sign-up | `signup_complete / signup_click` (it acts after the click) | `first_practice_started / signup_complete` falls: the greeting promised more than Practice gave |
| Theme note off phone headline | `signup_click / landing_view` and `sample_started / landing_view` on Android and iPhone browsers | none expected |
| Funnel steps | nothing; it is the instrument | a non-zero error rate on `/api/funnel` |

A fair attribution test (half of sample finishers see the carried greeting) needs a variant column the counter does not
have, and more traffic than today; propose it when a week brings a few hundred sample finishers.

## 7. Not done, and why

- **After sign-up** is where the measured drop is (about half never finish a set). Three first-run steps sit between the
  account and the first question. Carrying the sample's subject into the first run, or starting a first set straight after
  subjects, is the next lever. Not touched: it needs a signed-in walk on production (agents do not sign in there) and it
  changes onboarding and Today, which are the owner's to see first.
- **Proof beside the hero key.** True numbers exist (1,493 sign-ups last season; the creators' reels), but a public claim
  is the owner's copy decision, and he removed the hero's fact line on 5 Nov (LK121).
- **The free first full mock** appears to be off in production (the live page never says it). If it is turned on, it is the
  strongest true offer to say beside "Sign up free" and on the sample's result.
- **A finished sample is not restored** when a student comes back from `/signup` to the home page.
- **Phone scroll** (LK179 prototype) is still his decision; not part of this pass.
