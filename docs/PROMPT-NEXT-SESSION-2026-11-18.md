# Prompt for the next session (written 18 Nov 2026, about 3:00 pm IST, by the main Claude session)

Paste everything below the line into the new session.

---

You are continuing MockMob's website rebuild for the owner (Atishay). Start with `continuum_start` for project `mockmob`, then read, in `C:\Users\atish\mockmob-brain\docs\`: `NOW.md` (top section, 18 Nov), `OWNER-MASTER-LEDGER.md` items LK302 to LK315 (his words, whole), `DESIGN-DECISIONS-2026-11-18.md`, and `UI-AUDIT-LOG.md` sections 1 and 2f (how to capture screens fast, and today's traps). Do not re-walk what those mark as seen. Follow his UI standards (`AI OS\wiki\concepts\ui-ux-standards.md`).

## Where things stand
- Live: www.mockmob.in is `main 747d26f3e`. Code: `C:\Users\atish\Desktop\mockmob copy\wt-1110-convert`, branch `web/1118-prod` (same commit). Dev server: port 3571 (`.claude/launch.json`, name `convert-1110`). Release gate: `wt-1116-next/tmp/gate2.sh` (check out the commit there detached; start it ONCE, in background mode). Deploy is a fast-forward push of the gated commit to `main`; then check the live pages.
- Shipped today: "More inside MockMob" as a deck the scroll deals (`src/components/landing/TourDeck.jsx`, `deckMotion.mjs`, `src/app/r18-tour-deck.css`); the pen and highlighter (`src/components/doodle`: `Doodle`, `Marked`, `doodlePaths.mjs`); the streak block on Today; Search; test-screen keys and Cross out; Marks trend as an analysis desk; pen marks on 17 public pages.
- His verdict (18 Nov, about 2:55 pm): the doodles "look good"; the sliding-up animation is good; what he mainly sees is doodles and some animation. So the visible change is still too small.

## What to do now, in this order
1. **Use the phone's screen (his first point, LK313).** In "More inside MockMob" on a phone the product mock-up screen inside each card is small and there is blank space around it. Make the screen and its animation the largest thing on the card: shrink or drop what competes with it (the words above take about 190 px; the well's padding; the peek room), let the screen run close to the card's edges, and raise its fit floor so it is not scaled down to 0.73. Measure before and after at 390x844 and 360x740 (`tmp/1118/tools/deck.mjs`). Then apply the same test to every other phone section: wherever a graphic or animation sits small inside blank space (the Mistake Lab's screens, the exam screen's monitor, Key cards, the Compass), make it larger. Keep the scroll-dealt motion as it is.
2. **More life in the doodles (LK314).** Some marks should do more than draw once: think it through and build a few. Directions that fit the existing component: a mark that follows the scroll itself (drawn in step with the reader's scroll, as the deck's cards are), a mark that answers a tap or a correct answer, a highlighter that re-inks when a figure changes (the Compass score, the pricing pace). Keep the rules that keep it professional (one mark per heading, short phrases, red only for mistakes); nothing loops or pulses.
3. **The older sections (LK302, not done).** Home: exam screen, DU Compass, DU courses, creators, pricing, FAQ, footer. Signed-in: Practice, Your papers, Learn, Wallet, You, Progress, Your standing. Refine with the existing elements; lead each with one visible idea, not spacing changes.
4. **Bars and icons beyond the streak (LK309, part done)**, taking Duolingo as the bar for "readable in one look", in MockMob's own identity.

## Rules that matter most
- Phone first: he judges on his phone. Check every change at 390 and 360 wide, Day and Night, then 1440.
- No subpar art. Do not hand-model 3D. For Mobi or object art use the existing stills or the image generator.
- Tangible over minor: a change he cannot see in ten seconds does not count.
- Every release: the full gate, a look at each change in a real browser, then live checks. Say plainly what was not checked.
- Write a short brain checkpoint at natural points; update `NOW.md`, the ledger and the UI audit log at the end.

## Open decisions that are his (do not decide for him)
- Marks trend: Free students see each chapter's right-of-answered count; Key cards treats that line as Pro.
- Today shows two week rows (the streak's last seven days and "This week's goal").
