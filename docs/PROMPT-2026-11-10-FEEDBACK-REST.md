You are picking up MockMob (CUET UG 2027 mock tests; website www.mockmob.in, Next.js) from an earlier session. I am the owner. Read this whole message, then `C:/Users/atish/mockmob-brain/docs/HANDOFF-2026-11-10-FEEDBACK-REST.md`, before you change anything. Work through the items in the order given. Finish and ship one item completely before starting the next.

## Where everything is

- Code: the git worktree `C:/Users/atish/Desktop/mockmob copy/wt-1110-convert`, branch `web/1110-conversion`. It equals `origin/main` at commit `7444fb291`, which is live. The working tree is clean. Run every command from this folder.
- Record (plain files, edit by absolute path): `C:/Users/atish/mockmob-brain/docs/OWNER-MASTER-LEDGER.md` (my words are rows LK212 to LK224 at the end), `NOW.md`, `STATUS.md`.
- Working notes and tools from the last session: `wt-1110-convert/tmp/1110-app/` (not committed). Read `BRIEF-COMMON.md` there first: audience, my taste, the design rules, the preview route.

## Rules that are not negotiable

1. Never run git inside `C:/Users/atish/mockmob-brain`. It syncs itself. Only edit its files.
2. Never read, print or commit anything from `C:/Users/atish/MockMob-keys`. Never print values from `.env.local`.
3. The production database is read-only. No migrations, no schema changes, no writes.
4. Do not sign in to the live site or any hosted service as me. Signed-in pages are seen only on the local dev server through the preview route (below).
5. Do not call paid AI models. Do not generate or rewrite question content.
6. Do not change any production setting on Vercel or Razorpay. In particular do not set `WALLET_COMMERCE_OPEN`.
7. Truth: no number, claim, label or feature on any page unless the code or data backs it. If you cannot prove it, leave it out and tell me.
8. Copy: plain words, sentence case, no exclamation marks, no emoji, no em dash.
9. Refine what exists. Do not rebuild a screen from scratch and do not remove anything from the signed-in product; if you move or fold something, tell me what and why.
10. Never use `git stash`. Never `git worktree remove`. `node_modules` in the worktree is a link to another folder: never delete through it.
11. This is not the Next.js you know: before using a Next API, read the matching guide in `node_modules/next/dist/docs/`.
12. Tests pin copy, class names and CSS. When your change is intended and a test fails, update that assertion to the new truth. Never delete an assertion.

## Design rules (my taste)

- Judge at phone size first: 390 x 844 and 360 x 740, then 1440 x 900. Always both themes, Night and Day.
- An AI-generated look, to me, is: neon edges, glow, gradient text, too many outlined boxes, everything the same weight. Avoid all of it.
- One volt (lime) filled key per screen, for the main action only. No volt border around a whole card. No box inside a box. A surface is either a raised fill or a hairline, not both stacked.
- Real hierarchy: one clear title, quieter labels, heavier numbers with their unit.
- The main action must be visible above the bottom bar (it covers about 90 px) on a 360 x 672 screen.
- In app CSS use only the existing tokens (`var(--a-*)`); no literal colours. Tap targets 44 px or more.
- Motion only on transform and opacity, 150 to 350 ms, and it must respect reduced motion.
- A little tasteful graphic is welcome (the project has Mobi art and subject objects in `public/`). Walls of text are not.

## How to see your work

- Start the dev server from the worktree: `npx next dev -p 3571` (leave it running in its own terminal; stop it when you finish).
- Signed-in screens, with test data and no sign-in: `http://127.0.0.1:3571/preview/arena?view=<view>&plan=<free|pro>&data=<ready|empty>&study=on&decks=real`. Views you need: `wallet`, `profile` (the You page), `dashboard` (Practice), `today`, `mob`, `onboarding`. The Mob room: `/preview/mob-den`. Public pages: `/` and `/pricing?offer=monthly`.
- Capture tools in `tmp/1110-app/` (run from that folder):
  - `node walk.mjs --label <name> --w 390 --h 844 --theme <dark|light> --data <ready|empty> --views <view> --max 4 [--plan pro]` saves `shots/<name>/<w>-<theme>-<data>/<view>-v0.jpg` and prints page errors and sideways overflow.
  - `node tap.mjs <name> "<view&params or /path>" <dark|light> <WxH> "text=<visible text>"` taps then saves a shot after each tap. Use `"at=<css selector>"` to tap a key marked aria-disabled.
  - `MSYS_NO_PATHCONV=1 node land.mjs <name> "/pricing?offer=monthly" ".css-selector" 390x844,1440x900` for public pages.
  - `python montage.py <out.jpg> <thumb width> <img> <img> ...` puts shots side by side.
- Look at every shot yourself before you call an item done. Take a before shot first.

## The work, in order

Each item starts with my words. "Done when" is the check you must pass.

### 1. The Pro pop-up
"When someone clicks on a premium feature which needs Pro, then also the pop-up that comes can be a bit refined by adding some graphic or some sort of thing."
- Files: `src/components/pro/UpgradeSheet.jsx`, `ProFacts.jsx`, `pro-nudge.css`; words in `src/lib/proNudge.mjs`. A plan from the last session is at the end of `tmp/1110-app/notes-pricing2.md`.
- Open it: Practice (`view=dashboard&plan=free`), tap "Set up" on Smart practice or NTA mode, or tap a locked difficulty level.
- Do: add one small brand graphic (existing art only) and a clearer order: what you tapped, what Pro gives for it, the price, one key. Change no price or claim.
- Done when: it reads well at 390 and 360 in Night and Day, nothing overflows, and `node --test data/tests/pro_nudge_1018.test.mjs` plus every test file that mentions `UpgradeSheet` or `proNudge` passes.

### 2. The You card, the subjects layout, and a profile for the Mob
"We need to add the functionality to add, overall, some sort of setting, avatar, or profile for the mob feature, and to provide the overall social layer, which is important. Refine this card, like 'Hi Atishay' and 'Free plan'. Right now, it's 5 subjects: 3 on the top row, 2 centered on the bottom row. Take care of these kinds of things on your own and overall improve the [You] section."
- Files: `src/app/(app)/profile/**`, `src/components/profile/**`. Read `tmp/1110-app/notes-you.md` and `notes-mob.md` first.
- Do, part A: make the first card a real profile card: the student's picture and name as the title, the plan as a designed mark (Free quiet, Pro distinct), credits as one figure linking to the Wallet, and subjects laid out evenly for 1, 2, 3, 4 and 5 subjects (check each count).
- Do, part B: add "How your Mob sees you" to that card: their Fold figure or coloured disc and their Mob name, with a key that opens the name and colour dialog that already exists in `src/components/mob/MobPage.jsx`. Show it truthfully for: in a Mob, in no Mob yet (a key to start or join), Mob switched off (absent). Use only fields and server actions that already exist. If something needs a new database column (one avatar across all Mobs, a bio, a public profile), do not build it: write down exactly what it would need.
- Tests that pin this page: `data/tests/web_fixb_1019.test.mjs` (keeps `<SignedInLine` after `<YourSheet` and before `<PlanCredits`), `data/tests/you_account.test.mjs`. Run `npm run test:mob` too (7 failures in mob_v3 server tests already exist and are not yours) and `npm run test:subjects`.
- Done when: the card is even at every subject count at 390 and 360, both themes, Free and Pro.

### 3. The home page's sample questions
"When you pick a subject, not your subject, and select another subject, it takes like 5 seconds to load. Make sure there is a proper loading animation." And: the sample questions "should be the highest-quality questions ... the repeated [CUET] questions so that ... we can also show something like 'Was asked in [CUET 20xx]' or 'Previous year similar question'." Quality means "relevance to [CUET] and the syllabus", not difficulty.
- Files: `src/components/landing/DemoDrill.jsx` and its styles, `src/lib/demoSample.mjs`, `src/app/api/sample/**`. Do not touch the landing scroll engine (`storyController.mjs`, `ScrollStory.jsx`, `storyGesture.mjs`).
- Do first: a designed loading state inside the card: the picked subject's name stays, a skeleton of the question and four options in the card's own shape, the card's height held, no layout shift, and the existing slow, offline and error states still take over. Then make the wait shorter where that is plainly safe (ask for less, cache each subject's answer for a while). No schema change.
- Then: find what the question records carry (source, previous-year flag, verification, quality, reports) and make the sample draw from the best existing set per subject, with a fallback for thin subjects.
- An "asked in CUET 20xx" or "similar to a previous year" label may be shown ONLY where a stored field says so for that exact question. If no reliable field exists, show no label and write down what data would be needed. A wrong label on the home page is worse than none.
- Never change a question's text, options, answer or explanation.
- Done when: the loading state shows on a slowed network at 390 and 360 in both themes, and `node --test src/components/landing/*.test.mjs $(cat tmp/1110-refine/gate-list.txt)` passes with 0 failures.

### 4. The Wallet, the rest
"Wallet and all is still broken. We need to finish it up. There is no way to purchase anything, and also, overall, the UI is just falling off text."
- Already done and live: the first screen and the pack rows. Read `tmp/1110-app/notes-wallet.md`.
- Do: history as scannable rows (tabular numbers, 12-hour times, signs, running balance) folded behind one key when long; the loading, error, zero, low-balance, Pro and after-payment states; check 360 wide and Day with selling open. Files: `src/app/(app)/wallet/**`, `src/components/wallet/**`.
- Do NOT turn selling on. Buying is closed by the production switch `WALLET_COMMERCE_OPEN`, and the buying path has never been run with a payment. That is my decision after a test-card purchase. Tell me exactly what such a test needs; do not run it.
- Done when: wallet and credit tests and `npm run test:billing` pass, and each state has a shot.

### 5. The guide
"The top bar and the guide feature are just so, so, so bad. It should automatically start when someone is first-time entering the platform. Only implement it if you can properly fix it up and make it up to a very high standard and quality."
- Files: the tour block at the end of `src/app/(app)/AppLayoutClient.jsx`, its stops in `src/lib/appTour.mjs`. Open it from the person's sheet in the top bar, "Show me around".
- Do: show me a design first. Build it only if you can make it clearly good: few stops, each pointing at one real thing, a calm card that never covers what it points at, Back, Next and Skip that always work, done once per account, and auto-start only on a first-time student's first visit to Today, never over onboarding or a test.
- If you cannot reach that standard, leave the current guide as it is, do not add auto-start, and tell me what you would need.

### 6. Web onboarding
"I was testing the onboarding flow in a new account. Firstly, it's not as polished as the app."
- Files: `src/app/onboarding/**`. Preview: `view=onboarding`.
- Do: walk all steps at 390 and 360 in both themes as a new student, list what is rough (spacing, hierarchy, uneven grids, weak states), and fix those. Keep the steps and their order.
- The Accountancy note is already corrected ("The CUET syllabus gives Unit V two ways. Pick the one your school teaches."). Do not change the subject choices: they match the official 2026 syllabus.

## Before anything goes live (every item)

Run from the worktree and read the results:
1. `node --test src/components/landing/*.test.mjs $(cat tmp/1110-refine/gate-list.txt)`
2. `npm run test:app`, `npm run test:dock`, `npm run test:du`, `npm run test:keycards-ui`, `npm run test:auth`, `npm run test:billing`, `npm run test:subjects`
3. `npx eslint <every script file you changed>`
4. `npx next build --webpack` (stop the dev server's port conflicts first if any; delete `.next` after)
Known failures that are not yours and not in this gate: `npm run test:mob` (7 server-side tests), `npm run test:study` (1). Anything else failing is yours to fix.

Then ship:
1. `git add -A -- src data/tests` and commit with a plain message; end it with the line `Co-Authored-By:` followed by your own model name.
2. `git push origin web/1110-conversion`. Vercel builds a preview. Wait until that preview is READY.
3. `git push origin HEAD:main` (a fast-forward only). That deploys www.mockmob.in.
4. Check the live public page you changed. Signed-in pages cannot be checked live; say so.
If a Vercel build fails on fetching a font, redeploy the same build; do not change code for it.

## Keep the record (every item)

- `OWNER-MASTER-LEDGER.md`: change the status of the matching row (LK216, LK217, LK218, LK219, LK221, LK223) and add one sentence of outcome.
- `NOW.md`: a new entry at the top with the date, a real clock time in 12-hour form (run `date`), what is live, what is not, what you did not check.
- `STATUS.md`: a new entry at the top with the commit, the test numbers and what is unresolved.

## How to report to me

Short. First what I can see on my phone and where to look. Then what is left. Then exactly what you did not check (a real phone, iPhone Safari, signed-in pages on production). Never say something is done or checked if you did not see it yourself. If you are unsure, stop and ask me one clear question.
