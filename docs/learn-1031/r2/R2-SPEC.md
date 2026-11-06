# Round 2 build spec (1 Nov 2026, about 5 pm IST): owner items LK24-LK35

**Sources:**
- Owner's words verbatim: `OWNER-FEEDBACK-2026-10-31-LEARN.md`, section "1 Nov 2026, about 4:05 pm", in the mockmob-next docs.
- Audit, in this folder: `phone-clarity.md`, `screens.md`, `usefulness.md`, `speed.md`, `hero.md`.
- Screenshots of today's state: `tmp/learn-1101/r2-before/INDEX.md`.

**How the rulings work:** each packet implements every item in the audit files that touches the files it owns. The rulings below win wherever an audit file disagrees with them.

## 0. Rulings (binding, every packet)
1. **Learn leads with one start offer, never zeros (LK27).**
   - A count that is 0 is never shown. Drop it; never print "0 due", "0 kept", "0 of 2 fixed" or "Nothing in Revise yet".
   - The start offer's copy follows the student's state. Use exactly these lines:

     | State | Headline | Key |
     |---|---|---|
     | New to the subject | **Start learning Accountancy** | "Start chapter 1 · 10 min" |
     | Unfinished run | **Pick up Admission of a Partner** | "Continue · 6 min" |
     | Returning, otherwise | **Today's 10 minutes in Accountancy** | "Start · 10 min" |
     | Free after the day's session | **That was today's free session.** | "See Pro" (main key); "Answer single questions" (quiet; questions in Explore stay free) |

   - "Today's 10 minutes" is due cards from any chapter, at most 40% of the time, then the roadmap chapter's new cards and questions, plus one open mistake if there is one.
   - Below the offer: at most two quiet "Or" rows (for example "Find your level", "Play this chapter as a feed"), then search.
2. **"Your roadmap" replaces the chapter ledger (LK10, LK24).**
   - Chapters in book order, grouped under their CUET unit.
   - Each row shows the title, "31 of 46 cards seen · 4 of 10 questions tried" and a thin 3 px bar.
   - The only verdict word is "Needs work", shown when the chapter state is weak above its evidence floor.
   - Drop "Getting there", "Holding", "Too few answers" and "Fading" from Learn lists.
   - No %, never "mastered".
3. **Roadmap logic** (`usefulness.md` items 1, 2, 4, 5, 7):
   - New pure `data/learn/roadmap.js`, which returns where the student is in the subject.
   - A student stays in a chapter until its cards have been seen once. Offer "30 new cards left here · Next 10 minutes here".
   - Cards turned in the Explore feed count as seen.
   - Final-weeks mode (`usefulness.md` item 6) is DEFERRED: CUET is in May 2027. Note it in the backlog only.
4. **Words.**
   - "Keep" becomes "Revise later" for cards and questions alike. Their only meaning is "add to Revise".
   - One word for each thing everywhere.
   - Sentence case. No exclamation marks, emoji or arrows on buttons. 12-hour time.
5. **End screens (LK31):**
   - Layout, top to bottom:
     - the chapter name as a quiet line
     - a headline
     - one row of up to 3 numbers, with every zero dropped
     - the chapter's progress bar growing (600 ms, ease-out)
     - one main key and at most one quiet text link
   - The X is the only other way out.
   - At 1440, one centred column of at most 560 px.
   - Free never sees a key that the server will then refuse.
6. **Stop sheet:** "5 of 20 done. It's all saved." A main key "Stop here" and a quiet "Keep going".
   - Remove "Leave for now" only after checking in `src/lib/server/learn.js` that a stopped run can still be resumed the same day. If it cannot, keep that path and say so in the report.
7. **First-time cues (LK29):**
   - **Explore feed, first visit only:**
     - The next item's top 40 px always peeks above the action row.
     - A chip with Mobi's head says "Swipe up for the next one". On desktop: "Scroll or press ↓ for the next one".
     - The chip bobs 3 times (420 ms up, 380 ms back, ease-out).
     - It is marked seen only after the student actually moves.
     - Reduced motion: a static chip.
   - **Also:** "Tap the card to turn it" on the first card of a student's first run, and the chapter page's "First up" row (rule 9). Use the cue table in `phone-clarity.md` for any other place it lists; each cue shows once per student.
8. **Space (LK30):**
   - On a phone, the run and feed cards fill the height from the progress bar to the action row, with the text at the top.
   - Skip sits under the last option.
   - The top bar is one row with a labelled counter ("4 of 20").
   - At 1440, no side column of zeros, and no jumping between items.
9. **Chapter page:**
   - Title at 32 px, at most 2 lines.
   - Delete the first-visit line and "No lesson yet. No open mistakes."
   - A "First up" row shows 3 real card fronts.
   - One main key.
10. **The Practice tab row on phones (LK26):** four equal tabs that never scroll: "Practice · Learn · Explore · Papers".
    - Saved moves into Explore's header as "Saved 2" (moved, not removed).
    - The revise count shows as a dot, not text.
    - The navigation structure otherwise stays as it is (LK16 is closed).
11. **Explore page:**
    - The covers start near the top and the slogan goes.
    - Show 3 short single questions under the covers, not 12.
    - Delete the dead `/api/learning/summary` call and its line (`speed.md` item 2: the field never arrives, so the line never shows).
12. **Product rules:**
    - Never "mastered", no mastery %, no "marks to recover" and no claim of marks a student could gain.
    - Zero paid model calls for scheduling or diagnosis.
    - Today's "marks they cost you" stays only if it is the real marks-lost figure from `data/review_chapters.mjs`. Check `phone-clarity.md` item 19: whether a brand-new student is shown history they do not have. Fix it if real.

## 1. Packets and the files each one owns
Each packet works in its own worktree, branched from `web/1031-learn-v2` at 584542985. It never edits another packet's files. If a change needs another packet's file, write the request into `docs/brain/learn-1031/r2/NOTES.md` (append only), and the orchestrator merges.

| Packet | Worktree / branch | Owns |
|---|---|---|
| P1 Learn home and roadmap | `wt-1101-r2-home` / `web/1101-r2-home` | `data/learn/roadmap.js` (new) and any `data/learn/*` rules for suggestions and the start offer; in `src/lib/server/learn.js`, the subject, home, suggest, start and search functions; the `/api/learn` subject and home routes and a new combined `/api/learn/home` that the sidebar badge shares (`speed.md` item 3); the learn.js speed items (`speed.md` items 5 and 6); `src/components/learn2/home/**`; Find. Tests: `test:learn` (add roadmap tests). |
| P2 Run, feed and ends | `wt-1101-r2-run` / `web/1101-r2-run` | `src/components/learn2/run/**`, `feed/**`, `stage/**`; in `learn.js`, the run-end, feed-end, stop and Free-end functions only. Rulings 5, 6, 7 (feed and run cues), 8, and "Revise later" inside run and feed. `screens.md` items on the run, feed, stop sheet, wrong answer and ends. |
| P3 Chapter, Explore and tabs | `wt-1101-r2-explore` / `web/1101-r2-explore` | `src/components/learn2/chapter/**`; the Explore page and covers (including `DiscoveryFeed.jsx`); the phone Practice tab row component; "Revise later" outside run and feed; rulings 9, 10, 11. |
| P4 Speed | `wt-1101-r2-speed` / `web/1101-r2-speed` | `AuthProvider.jsx`, `/api/auth/me`, `/api/questions/feed`, `/api/stats`, the Today data path (a combined `/api/today` per `speed.md` item 4, plus `useToday`), the CSS loading in the app layouts (`speed.md` item 8), and cache headers. Ruling 12's Today check. Every `speed.md` item not owned by P1. |
| P5 Home hero | `wt-1101-r2-hero` / `web/1101-r2-hero` | `src/components/landing/**` hero parts, `src/app/page.js` hero section, and new public images. Build `hero.md` as written: the painted rooms, the MobiReact tap cycle with the exact bubble lines, text cut by 20-27%, desktop Mobi beside the demo card, no sound, and its speed budget. |

## 2. How every packet works
- **Read first:** AGENTS.md, then `node_modules/next/dist/docs/` before writing Next code; DESIGN.md; the owner's UI standards at `C:\Users\atish\Desktop\AI OS\wiki\concepts\ui-ux-standards.md`; your audit file(s); the shots in `r2-before`.
- **Tests:**
  - Keep and extend: `test:learn`, `test:keycards`, `test:today`, `test:app`, `test:auth`, `test:egress` and lint, whichever touch your files.
  - Write unit tests for every new pure rule. In particular, pin "no zero is ever rendered as a lead" and the end-screen formula.
- **Look (RAM rule):**
  - At most 2 dev servers on this PC at once. Take a slot with `mkdir "C:\Users\atish\Desktop\mockmob copy\tmp-devslots\slot-1"` (or slot-2); if both exist, wait and retry every 60 s. Run `npx next dev --webpack -p <your port>` (P1 3481, P2 3482, P3 3483, P4 3484, P5 3485). Stop it and `rmdir` the slot when done.
  - Hold the browser lock `tmp/learn-1101/browser.lock` (a mkdir lock; see `scripts/design-audit/learn-1101-final-capture.mjs`) for every headless browser.
  - Capture your surfaces at 390x844 and 1440x900, Night and Day, into `tmp/learn-1101/r2-after/<packet>/`. Use the `/preview/arena` views and params listed in `r2-before/INDEX.md`; P5 uses `/` locally.
  - Look at every shot against the rulings and the UI standards' done check, fix, and capture again: at most 2 rounds.
- **Finish:** commit on your branch. Kill every process you started (dev server, browsers, node). Return what changed, the test counts, the shot folder and anything left.
- **Never** push, deploy, sign in to production, or write to a database.
