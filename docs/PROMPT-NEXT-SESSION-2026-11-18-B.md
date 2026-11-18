# Prompt for the next session (written 18 Nov 2026, about 10:15 pm IST, by the Claude session that did today's rebuild)

Paste everything below the line into the next model.

---

You are continuing MockMob's website work (www.mockmob.in: CUET practice for Indian students aged 16 to 17; Next.js 16 and Supabase). The owner, Atishay, looked at the live site on his phone on 18 Nov at about 10 pm and gave the feedback below. Your job is to act on it, build, check it in a real browser, pass the release gate, deploy, and report honestly. He judges on his phone first.

## Read first (15 minutes)
1. `C:\Users\atish\mockmob-brain\docs\NOW.md` (top section: what is live, what is held, the exact commits).
2. `C:\Users\atish\mockmob-brain\docs\OWNER-MASTER-LEDGER.md`, rows LK317 to LK330 (his words tonight, verbatim, with a reading of each), then LK302 to LK316 (the day's brief).
3. `C:\Users\atish\mockmob-brain\docs\UI-AUDIT-LOG.md` sections 1, 2f, 2g and 3 (how to look at pages, the capture tools, the traps).
4. `C:\Users\atish\Desktop\AI OS\wiki\concepts\ui-ux-standards.md` (his UI standards).
Never run git inside `C:\Users\atish\mockmob-brain`; it syncs by itself.

## Where things are
- Code: `C:\Users\atish\Desktop\mockmob copy\wt-1110-convert`, release branch `web/1118-prod`. Deploy = fast-forward push of a gated commit to `main` (Vercel builds it). Never push an ungated commit, never push lane branches.
- Gate: in `C:\Users\atish\Desktop\mockmob copy\wt-1116-next`: `git checkout --detach web/1118-prod`, confirm no `gate2.sh` is running, then `bash tmp/gate2.sh` once (about 15 minutes; result in `tmp/gate2.log`, must end `DONE` with every suite at fail 0, empty eslint, both builds exit 0; `test:recovery` always prints a "failing tests" line for a known todo: that is not a failure). Before the gate run `npm run test:app` and `node --test data/tests/landing_checklist_1104.test.mjs` in the release worktree.
- `.env.local` is the PRODUCTION database: no writes, no sign-ins, no payments, no paid model calls. Signed-in pages are seen only through fixtures at `/preview/arena?view=...`.
- Held, not live: `web/1118-prod` carries a rebuilt Colleges page and Saved page (merge 83fb1a8ed). He has not seen them. Look at them against item 9 below before they ship.
- Rollback points for comparing "before": home sections before today's evening rebuild = commit `219551a16`; Practice, Learn and You before their rebuild = commit `c2f12abcd`. Use `git show <commit>:<path>` or a temporary worktree to see the old version side by side.

## His feedback, in the order to do it (his words are in the ledger; this is the work)
1. **Doodles.** The pencils, markers and sparks that drew the marks are already removed everywhere ("highly unprofessional"); never bring a drawing tool back. The plain pen marks and highlights stay. Make them "a bit slower, more refined and more accurate with when they are showing up in the scroll": each mark should start when its words reach a comfortable reading position (not at the screen's foot, not after they have passed), take about a second with a gentle ease, and never replay. Files: `src/components/doodle/`.
2. **Smoothness (the biggest item).** "The screen stutters in the first five [seconds]"; "it doesn't feel like 120 FPS fluid. It feels like maybe 40, 50"; the first loading animation "is a bit too short". Record a performance trace of the home page on a throttled phone profile (first 6 seconds, then a full scroll), find what drops frames (hydration of the large home components, the hero film starting, font and image decoding, scroll handlers, layout work in the doodles' measuring), and fix causes, not symptoms. Let the opening animation run long enough to cover the page settling. Give before and after numbers (long frames, worst frame) in your report. Do not benchmark while builds or test suites run on this PC.
3. **The story progress bar** (the bar pinned at the bottom of the screen during the Mistake Lab and "More inside MockMob", with "1 of 5" and the moving marker) "is a bit jumpy ... it's not moving properly". Make it follow the scroll continuously. Also check the hero film's own segment bar. This reading is mine: confirm on a phone-size screen which bar jumps.
4. **The exam screen section** ("MockMob / NTA style Pro") is "a bit of a regression ... that desktop UI was better than this mobile approach". Bring back the desktop-monitor presentation from `219551a16` on phones too. Say clearly that NTA style is an exact copy of the real NTA exam screen. Keep today's phone-size readable version only for what opens on "Try it full screen".
5. **A first-visit note on phones**: a small static pop-up saying the site works best on a laptop or desktop, with a small cross, shown once per device, never blocking the page. He says he asked for this before (search the ledger for the earlier wording) and named "Clay Prep" as doing it; he may mean another prep site, so ask him or look it up before copying a pattern.
6. **Daily Five, "Play for your college."** He doubts using college names (legal risk, and whether it works) and wants "something more simpler". Build the simpler version without college names, keep the old one behind a flag, and show him both.
7. **DU Compass block on the home page**: it should play by itself when it comes into view, then pause after 10 to 15 seconds or when it leaves the screen. He is fine with either the old or the new look.
8. **"Which DU courses are open to you?"** on the home page: "either remove it or make it" better; the quick-start presets (Commerce, Science PCM, PCB) are too generic. My recommendation: remove the section from the home page and keep the calculator one tap away (hero link, footer, DU Compass block).
9. **Order and pricing.** Move pricing above the Instagram creators section. On the pricing card, "₹3,750 the usual way" has its working hidden in a disclosure far below: put the working right beside the figure (a small key next to the amount that opens the sum in place). He is unsure whether the old or new card is better: put `219551a16`'s card and today's side by side, keep the best of each, and make the card look better as a whole.
10. **Signed-in site**: "nothing really impressive", "too much blank space in some places", and Practice "is feeling like a regression" against the previous one. Compare Practice at `c2f12abcd` and now, at 1440 and 390, and restore what was better (the mode stays the ticket's heading: owner note G26). Then go through Today, Practice, Learn, Progress, You, Colleges and Saved at 390 and 1440 and close the empty space: size things by importance, no page should end in a blank half screen.

## Creative headroom
After items 1 to 10, you may propose and build ONE thing per area that makes the site feel more advanced than any mock platform, in MockMob's own identity (paper, ink, volt, the lamp-lit desk objects, Mobi): for example a more satisfying result moment, or a better streak moment. Show it to him before it replaces anything. If a section lacks a picture, you may generate art with the image generator (the hand-built 3D Mobi was dropped as "very bad"; only ship art that beats the existing stills).

## Rules that bind
- Visible change, phone first (390 and 360), then 1440; Day and Night. Capture before and after side by side and look at them yourself; if a stranger cannot tell which is new, it is not done.
- Nothing moves by itself except where he asked (item 7). Reduced motion respected. No nested cards, one left edge, no walls of text, 44 px touch targets, plain words a 16-year-old reads once, no new claims the code cannot back.
- Do not remove anything a student can use today unless an item above says so.
- Refine, do not rebuild from zero; when unsure whether old or new is better, compare both on screen and decide.
- Update `NOW.md`, the ledger (an outcome row per LK item) and `UI-AUDIT-LOG.md` when you ship; save a continuum checkpoint. Report to him in plain language: what is live, what percent is done, what is left, what you could not check (a real phone, Safari, signed-in pages on production).
