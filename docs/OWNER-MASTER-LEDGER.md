# MockMob owner master ledger (living file: read it first, update it at every session end)

**Why this file exists.** The owner (18 Oct, 1:45 am): "I have to explain and give the same feedback again and again, so that should not happen."

His asks were spread over six dated ledgers, so agents missed items. This file is **the one list of what he has asked for that is not yet done**, grouped by surface, with his latest verdict.

**How to use it:**
- **Start of a session:** read this file. Then open the source files only for the rows you will work on.
- **New owner feedback:**
  1. Save his words verbatim in a dated `OWNER-FEEDBACK-<date>.md`, with a ledger and "(confirm)" flags on transcription guesses.
  2. Then fold every item into the rows here: update the row, or add one.
- **When something ships:** set its status, giving the release and sha. **DONE means verified on the live site or a walked APK**, not just merged.
- **When he rejects something:** set REJECTED, quote him, and add the lesson to "Never again" below.

**Status words:**
- **OPEN:** not started.
- **BUILT:** on a branch, not live.
- **LIVE-UNCHECKED:** live, but he has not looked.
- **DONE:** he accepted it, or it was verified live.
- **REJECTED:** he rejected what shipped; redo it.
- **DECIDE:** his decision is needed.

**Sources, newest first:**

| Prefix | File |
|---|---|
| D | `OWNER-FEEDBACK-2026-10-18-DAWN.md` (18 Oct 1:45 am, after R4) |
| N | `OWNER-FEEDBACK-2026-10-17-NIGHT.md` |
| F | `OWNER-FEEDBACK-2026-10-17.md` |
| W, L | `WEB-OWNER-LEDGER-2026-10-17.md` (web W-001-W-100, landing L-001-L-045) |
| App L | `APP-OWNER-LEDGER-2026-10-16.md` (L01-L39) |
| v15 | `V15-SPEC-2026-10-18.md` (the v13 walk findings) |

His full message history is in `tmp/owner-corpus` (286 messages).

---

## Never again (his rejections, each a rule)

1. **Refine, don't rebuild.**
   - 15 Oct: the web restructure was "a huge regression".
   - 17 Oct: the result redesign was "not acceptable at all".
   - 18 Oct: the Today redesign was "a huge regression".

   When he calls a screen confusing, keep its information and structure and refine the UI and interaction. Any replacement layout is shown to him as a mock-up before it ships.
2. **Never simplify by cutting.** Never remove "the good stuff" (mascot moments, the full analysis, rich cards) to reduce clutter. Reduce clutter by structure, not deletion.
3. **Nothing looks like a form.** Settings and plan surfaces are leading, interactive flows that take you to the next thing (D3).
4. **Night mode stays subtle.** No neon, no heavy glows or accents (D7). He loved the earlier Night.
5. **Motion must not degrade.** A changed animation is at least as good as the old one (D10 theme switcher, N5 segmented controls).
6. **No obvious disclaimers or filler lines** (W-093). No "41 subjects" (W-095). Copy tone is exciting and bold (M-006, 18 Oct), never false.
8. **Keep the badges** (D19, 18 Oct): refine them, never remove them.
7. **Only gpt-6-luna and Claude Haiku 5.5 run in the app or website** (W-098).

## Keep (he praised these; don't touch except for bugs)
- **Practice and Start:**
  - the Practice UI ("really refined, looks really good", D4);
  - the subjects loop ("perfect now");
  - the Start session sheet ("loved", N11).
- **Result:**
  - the answer sheet and overall summary (N16);
  - scores by session (N14);
  - the front of the result (marks, right/wrong, accuracy, blank; D16).
- **Elsewhere:**
  - the weak chapters content (N13);
  - Progress on phone (D19, except badges);
  - the R4 Today's cleanliness (D1; the layout itself is rejected);
  - the mobile web UI overall (D14);
  - Day mode (N10).

---

## Open items by surface (website unless marked)

### Today (web and app): **TOP PRIORITY, REJECTED in R4**

| Status | Item |
|---|---|
| REJECTED | **D1, D2:** R4 Today (main 9578ee66) is "a huge regression": clean, but not tangible, and it lacks the information. Go back to the R3 Today (5d0c46f2) information and structure and refine it. It must lead the student and be interactive, more than "start 10 minutes". Reorder; add more important things. **The main session designs it and shows the owner a mock-up first.** |
| OPEN | **N1 (still true for the R3 base):** the long road strip is hard to read (only a few weeks in focus), and the mock-count slider does nothing a student understands. Fix both inside the R3 structure. |
| OPEN | **D3:** the Change plan sheet is okay, but must never look like a form; it must be a leading, interactive flow. |
| OPEN | **W-042:** loads fast with no section arriving late; works for an account with history. |
| OPEN | **W-044:** a cue leads to the road below the fold. |
| BUILT, REJECTED design | **App v15 Today packet:** built the R4-style "Your road to CUET" card and Adjust plan sheet (V15-SPEC section 2) in wt-v15-today. **It follows the rejected design. Redo it per D1-D3 before v15 ships** (see NOW.md). |

### Result (web and app)

| Status | Item |
|---|---|
| LIVE-UNCHECKED, partly REJECTED | **N12:** R4 restored the reveal and the full analysis; he says it is "back and better" but not what he wanted (D15). |
| OPEN | **D15:** one clear action per mistake. Today one screen mixes "Repair first", "Repair in 1" and "Check it here" for 5 mistakes; use one label and counts that agree. |
| OPEN | **D16:** the depth layer is cluttered; give it one calm structure. |
| OPEN | **D17:** the answer bar fits the mock's length (10 questions, then 10 slots), with expand and collapse. Replay is useless today ("grey boxes going and going"): show real events (answers, changes, skips, time per question) or cut it. |
| OPEN | **N15:** "Chapters by marks left open" is not good. R4 replaced it with "Where your marks went"; check it. |
| OPEN | **W-026/029/030:** layers, the SWOT with one-tap recommendations, a memorable reveal. |
| OPEN | **F11:** what Repair adds must be obvious; nothing shown twice. |
| OPEN (app) | **v15 walk findings 1, 4, 5:** the stem shows twice; stale credits after a set (10 credits for both 5 and 10 questions); the Repair chip doesn't start a repair. |

### Review, Repair and Learn

| Status | Item |
|---|---|
| OPEN | **D18:** "We have tried so many times to fix this stuff, but no result." His idea: Review leads with the **weak chapters** (marks lost by chapter, Practise), with mistakes under each. |
| OPEN | **F17, W-038:** a repaired mistake opens its saved repair (never a paid repair again). Each mistake shows its mock and its date and time (12-hour). |
| OPEN | **W-032, W-033:** Repair lets the student try again before seeing the key; it completes on staging with no error. |
| OPEN | **W-034, W-035:** Mistake Lab timing and the v4 dashboard. |
| OPEN | **D20, F15, W-040:** Learn needs a clear place in navigation and a real refinement pass. F15 Learn/Review work: Revise and Concepts are BUILT in wt-lr2 and wt-lr3; the Review part (P-LR1) is ON HOLD until he accepts the result. |
| OPEN (app) | **v15 finding 7:** the Review notice is duplicated, covers content, and its counts disagree. |

### Practice, Start, runner and NTA

| Status | Item |
|---|---|
| OPEN | **D5:** the Repairs [confirm] and Mobi entry points are missing from Practice ("no one will be able to see it ever"). |
| LIVE-UNCHECKED | **N2:** the blur is lighter. |
| LIVE-UNCHECKED | **N3:** the fine-tune copy. |
| LIVE-UNCHECKED | **N5:** one sliding indicator. |
| LIVE-UNCHECKED | **N7:** "CS/IP". |
| LIVE-UNCHECKED | **N8:** the NTA bar is continuous and the timer works. |
| LIVE-UNCHECKED | **N11:** spacing. |
| LIVE-UNCHECKED | **N6:** the five-subject cap (the picker note lacks a 2026 qualifier). |
| OPEN | **N4:** fine-tune "something better can be done" (an open design question). |
| OPEN | **F12:** the Quick practice Start button state flicker on scroll. |
| OPEN | **W-002/003/005/008/012:** remaining Start menu affordance items. |
| OPEN | **W-013:** the Practice cards' blue light and texture. |
| OPEN | **W-017/018:** the runner's top notice; no privacy filler line. |
| OPEN | **W-023:** NTA strike guard. |

### Ask Mobi

| Status | Item |
|---|---|
| REJECTED | **D6, D12, N9:** the R4 orb and panel: "very old", "too much clutter", "neon", "weird UI"; "only Your Record works"; it should not sit below the theme selector. **Needs a redesign brief from the main session (purpose, entry points, contents, placement) before building.** Also the R4 caveat: the panel is dark in Day mode. |
| OPEN | **W-060:** the cost is shown before each call; the balance updates. |

### Night mode, theme and icons

| Status | Item |
|---|---|
| REJECTED | **D7:** Night is now too highlighted and neon. Find what changed in the Night tokens, accents and glows between pre-R2 production and R4, and restore the subtle Night. |
| REJECTED | **D10:** the new light/dark switcher animation is worse than the old one; restore it. |
| OPEN | **D8, W-069:** icons (a consistent family; no odd glyphs). |
| OPEN | **W-075, W-076:** one volt key per viewport; the slop list (no glow, no gradient text, no nested cards). |
| OPEN | **W-078, W-079:** Night and Day parity; 44 px targets. |

### Navigation, sidebar and dock

| Status | Item |
|---|---|
| OPEN | **D11:** the sidebar bottom (My Account, Help, theme): "Help" is the wrong word and the wrong place. If kept, it becomes its own page, not a scroll. |
| OPEN | **N17:** the guide section is more intuitive. |
| OPEN | **D13:** the phone bottom nav active pulse looks wrong on Practice ("text and line"). |
| OPEN | **F13, W-068:** the dock and Start placement. |
| OPEN | **W-070:** the "Arena" label is clear. |
| OPEN | **F2, W-067:** Colleges' home in navigation (researched; the same on web and app). |

### Progress, You and badges

| Status | Item |
|---|---|
| OPEN | **D9:** "Not much implemented". |
| OPEN | **D19 (clarified 3:50 am):** "badges are not incorporated properly but they look cool so keep them don't remove just refine the UI and functionality around them." Keep the badges; refine their presentation, placement and what earning one does. BADGES-ICONS-1018 option A (remove) is REJECTED. |
| OPEN | **W-053:** You leads with study days, badges, milestones and personal bests. |
| OPEN | **W-052:** the top-bar Profile shows name, email, credits and plan. |

### Colleges and Compass

| Status | Item |
|---|---|
| OPEN | **W-047, W-049:** colleges are picked inside onboarding. |
| OPEN | **W-050:** Compass is prominent. |
| OPEN | **W-051:** the cutoff calculator's "New" tag and green line. |

### Social: community, leaderboard and the Mob

| Status | Item |
|---|---|
| DECIDE | **D21:** maybe suspend the community idea and remove the community section (not final). Keep "Your standing". Don't delete anything until he decides. |
| OPEN | **D22 (name DECIDED 3:50 am: Mob; "community" retired):** a concept brief for a cooler, useful "social circle". Reference: an app he called "RPM" (leaderboard, aura, badges); he finds it cringe, so don't copy. |
| OPEN | **W-055:** the leaderboard is the richer earlier design. |
| BUILT | **The Mob:** web wt-mobfix c33d7f03 plus a fix round, 18 Oct; the app side is in v13/v15, off. **It switches on only at 10/10 after the gate** (the steps are in NOW.md). Square this with D21 first. |
| OPEN | **W-061, W-062:** the Mob on the main surfaces. |

### Pricing, auth, copy and whole-site items

| Status | Item |
|---|---|
| OPEN | **W-097:** the pricing visual upgrade. |
| OPEN | **W-057:** sign up and login improvement. |
| OPEN | **W-093/094/095:** copy truth and no filler. |
| OPEN | **W-064, F18:** guided entry points for every feature (adoption). |
| OPEN | **W-072/073/077/082/083/087:** the premium bar, motion, anti-slop, subject art, balance and detail sweeps. |
| OPEN | **W-085:** web and app parity. |
| DONE (audit) | **W-091:** re-audited on live R6 on 18 Oct (`W-REAUDIT-2026-10-18.md`): **71 PASS, 21 PARTIAL, 0 FAIL, 4 not testable, 4 superseded** (was 37/49/11). The open items are being fixed in R7/R8 (see the 9:50 am row below). |

### Landing

| Status | Item |
|---|---|
| BUILT, gate running | **L-003-L-045:** wf_b167ffb5-960, wt-land2. It ships on the fixed checklist: every L item passes, zero truth and zero high defects, each fix locked by a test. The score is advisory. |

### App (Flutter)

| Status | Item |
|---|---|
| BUILT, in progress | **v15 = the Play Store candidate** (`V15-SPEC-2026-10-18.md`). |
| OPEN | **F1:** the nav count and alignment. |
| OPEN | **F3:** the liquid-glass taste. |
| OPEN | **F9:** the fine-tune scope. |
| OPEN | **App L01-L39** (`APP-OWNER-LEDGER-2026-10-16.md`). |
| OPEN | **v15 walk findings 1-9.** |
| OPEN | **D-items carry over to the app:** Today D1-D3, result D15-D17, Review D18, Ask Mobi D6, Night D7. |
| OPEN | **Play Store readiness** (V15-SPEC section 7): the upload key and the Console are the owner's. |

---

### Added 18 Oct 2:30-4:10 am IST (session 25ef3d95; his words in OWNER-FEEDBACK-2026-10-18-DAWN.md, end sections)
| Id | Surface | Item | Status |
|---|---|---|---|
| A2 | App | Hold v15 for the new Today (decision A) | v15 waits for Today |
| D25 | Today (web, app) | Proceed with TODAY-1018 into v15 | building (web wt-today18, app wt-v15-today2) |
| D26 | Today | Road to CUET shows due today, due this week and the overall goal | building |
| D27 | Today | Must feel unique and premium in the final UI, not generic | building; critic checks |
| D5 | Practice | "Repo S" = Repairs (CTO decision; he could not confirm) | built in R5 (web/r5-practice-1018), not live |
| D6 | Ask Mobi | Confirmed = Ask Mobi; ASK-MOBI-1018 approved | web wt-r6-askmobi, app wt-v15-askmobi |
| D16-D18 | Review, result | REVIEW-RESULT-1018 approved | web wt-r6-review; app after v15-result |
| D21 | Community | Keep for now; hide contributions per COMMUNITY-1018 (approved) | web wt-r6-community (with D20) |
| D28 | Today (app) | "Back from marking": bugs seen on v13: greeting by hour ("Good evening" at 2:41 am), "Still refreshing" stuck, row under the bar | v15 integration |
| D29 | Today, result | Replace the fake "Back from marking" wait with a truthful reel: "Play your paper back, 20 s" (same engine as the D17 replay) | app widget wt-v15-reel; web in R6 replay |

### Added 18 Oct about 3:45-4 am IST (his words in OWNER-FEEDBACK-2026-10-18-DAWN.md, last sections)
| Id | Surface | Item | Status |
|---|---|---|---|
| D30 | Landing, big pages | He reviews the landing live himself before any ship (local dev server or preview); screenshots are not enough | rule |
| D31 | Landing | The landing does not follow his instructions; the next pass starts from his own landing words, not critic scores | open |
| D32 | Landing | The landing branch (wt-land2 48e7b057) is a "major regression": do NOT ship it. Keep only (a) the held-story position indicator at the top (Mistake Lab, What's inside) (confirm the element) and (b) the top light/dark toggle; port those two into the CURRENT live landing | open |
| D33 | Website | Release 5 changes were not visible to him ("seems the same"); every release must make his asks visibly obvious and say where to look | rule |
| D34 | Process | Work until about 80% usage, then stop safely with the handoff and the prompt | done this session |
| M-001..M-027 | All | Missed asks from the 12-17 Oct corpus: `MISSED-ASKS-2026-10-18.md` (M-001 logo 3 s and M-006 "exciting copy" need his decision; M-018: end every update with "Things needed from you right now" or "Nothing needed from your side"; M-020: his stop rule is about 97-98% usage) | fold in next session |
| D19, D8 | Progress, icons | `BADGES-ICONS-1018.md`: recommend removing badges for a dated record with real numbers; one Lucide icon family, phone bar fixed | show him |

### Missed asks folded in, 18 Oct about 3:45 am IST (from `MISSED-ASKS-2026-10-18.md`; his words and code checks are there)
| Id | Surface | Item | Status |
|---|---|---|---|
| M-001 | App, brand opening | DECIDED 3:50 am: the full 3 s logo B opening on the FIRST launch after install only; later launches keep the short one (about 1.3 s) | OPEN (v15) |
| M-002 | App, copy | Unlimited mocks from one central bank, said truthfully and quietly in the app (onboarding, plan, credits) | OPEN |
| M-003 | App and web, NTA | A brief interruption of 3 s or less (the notification shade) is forgiven; a deliberate switch counts at once; three warnings, no other grace | OPEN (with W-023) |
| M-004 | Both | A feature-by-feature robustness walk: no crash, dead button or lost state | OPEN (the v15 walk and the live W re-audit) |
| M-005 | App | Every decorative dot or indicator carries real information or is reworked so it does | OPEN |
| M-006 | Copy | DECIDED 3:50 am: **exciting, bolder copy** (punchier, energetic) where disclaimers were removed, on the landing and in onboarding. Relaxes W-093's no-hype for tone only; truth rules still hold (no false claims, real numbers) | OPEN (copy pass) |
| M-007 | Compass data | Verify programmes, counts and cutoffs against the CSAS and DU sources; record the source and date | OPEN |
| M-008 | Content | His 10/10 question definition goes into the judge rubric (content runs only when he asks) | OPEN |
| M-009 | Landing, onboarding | Video or scroll-animation ideas: storyboards for the top two, he picks | OPEN (with Higgsfield) |
| M-010 | Backend | A migration so the repo matches production's removed AI ceiling; a rebuild must not restore the USD 25 cap | OPEN |
| M-011 | Ops | Delete the duplicate paused Vercel projects (he said six; the records name five). He clicks, or gives a fresh go-ahead | OPEN, his click |
| M-012 | App | The notification prompt returns on a cadence with varied wording | mostly DONE |
| M-013 | App | Study days readable offline | OPEN, low |
| M-027 | App | Answer once with evidence: is the low quality the emulator or the build? | OPEN |
| M-014, M-015, M-016 | Rules | No iOS until students ask; no cap on agent-written questions per paper; any new mascot or art reads as edtech, is original and is legally safe | RULE |

**Process rules from the missed asks** (apply to every session):
- **M-018:** every update to him ends with either **"Things needed from you right now:"** followed by the items, or **"Nothing needed from your side."**
- **M-021:** near a usage reset, with quota left, run the most parallel work. Watch for stalled agents throughout; the main session monitors them continuously.
- **M-023:** every next-session prompt has one goal and points to NOW.md and this ledger.
- **M-025:** never let one track eat hours while other open asks sit; app work runs in parallel with web work.
- **M-019:** while he sleeps, never block on a question; find a workaround.


### Status update, 18 Oct about 6:45 am IST (session 604ced81)
| Items | Status |
|---|---|
| D7/D12 (Night on Ask Mobi), D10 theme switch, D11 Help and FAQ page, D13 nav floor, D5 Practice Review and repair + Ask Mobi, D15/D17 (first pass), F15 Learn and Review, D20 the "Learn" name | **LIVE-UNCHECKED** in R5 (main 58bc53f6). Where to look: docs/brain/R5-WHERE-TO-LOOK.md |
| D15/D16/D17/D18/D29/F17 (Review/result 1018), D6/D12 (Ask Mobi 1018), COMMUNITY-1018 + D20, D19 badges (web) | **LIVE-UNCHECKED** in R6 (main 70c4598c, about 7:25 am) |
| D1-D3, D25-D28 (web Today 1018) | **BUILT**, wt-today18 d0486c12; waits for his live review (port 3207) |
| D32 landing | **BUILT**, wt-land3 f64cffe5 (position band only; the toggle was already live); waits for his live review (port 3206) |
| App: Today 1018 (D1-D3, D26-D29), Ask Mobi (D6), Play it back (D29), M-001 logo, D19 badges | **BUILT** in v15 (wt-v15 fecc6a73 + ui/v15-badges a85f0e50); emulator walk running |
| Production migration revise_cards_mode | Applied at 4:50 am (grant); STATUS text pending in the R6 push |

### Owner at about 8:40 am, 18 Oct
| Id | Item | Status |
|---|---|---|
| D35 | The web Today is "better now". Ship it on top of release 6 | OPEN (R7) |
| D36 | Ask Mobi redesign not seen (the preview was built on R4). On R7, the Today lead card carries Ask Mobi "Why this?"; release notes say where Ask Mobi is | OPEN (R7) |
| D38 | Landing HERO refinement: the morphing/typed changing line under "CUET 2027" (L-016), CUET 2027 coloured (L-017), not a fake button (L-018), clean spacing (L-014), the Mobi animation (L-004), no glow (L-019) | OPEN (Opus, wt-land3) |
| D37 | Finish and perfect everything, publish the final web and app versions, then tell him; he reviews both and gives final feedback | RULE / in progress |

### Re-audit follow-ups, 18 Oct about 9:50 am (all being built for R8 unless marked)
| W | Item | Where |
|---|---|---|
| W-041/W-042/W-077 (Today) | The new Today replaces R4's | R7 (verifying) |
| W-078 | /mentor "Your record" unreadable in Day (contrast 1.01): a LIVE bug | wt-r8-fixes |
| W-026/W-075 | Two lime keys on phones: the dock Start goes quiet while a page's own primary is visible (the same rule the desktop sidebar already uses) | wt-r8-fixes |
| W-079 | Sub-44 px spots (Practice fine-tune row, "See Q14", the Mob icon buttons; desktop sidebar rows if the rail still fits) | wt-r8-fixes |
| W-093 | Help "Five stops" vs the 8-stop tour; two disclaimer-tone lines (Learn, Progress) | wt-r8-fixes |
| W-089 | Copy the pass-1018 design notes into the repo | wt-r8-fixes |
| W-064 | The first-week path; the "of the 6 you repaired, 5 did not come back" receipt | wt-r8-adopt |
| W-032 | "Try it again" before the key on the result page | wt-r8-retry |
| W-074 | The landing shows two Mobis at once at 1440 | the landing hero agent (wt-land3) |
| W-085 | App parity: Review leads with weak chapters in v15 | wt-v15-review |
| W-061/W-062 | The Mob is off in production | by decision (gate first) |
| W-049 | Colleges are also addable outside onboarding | kept as edit paths (never cut); his call if he wants them gone |
| W-099 | /mentor "Your record" and the Weak chapters page repeat the same record | **DECIDE** (merging cuts a page; ask him) |
| W-033/W-058 | A live repair and sign-in persistence need a real signed-in walk | not testable from fixtures |
| W-046 | "Study day / week chapters" meaning | **ask him** |

### Owner on v15 (79aaca6d) on his phone, 18 Oct about 12:15 pm (D40-D57; his words at the end of OWNER-FEEDBACK-2026-10-18-DAWN.md)
| D | Item | Status / where |
|---|---|---|
| D40, D43, D44, D48 | Onboarding layout: content too high, too much space below; a clear Back button; adaptive Mobi and a sharper Mobi graphic, bigger on the plan screen | Building: ui/v15-onboard-a |
| D41, D42, D45, D46, D47, D49 | Courses (most chosen first, Bulletin combinations, full list); no default subjects for "Not sure yet"; marks step up to 3; a full-mocks line under 10/20/30; an interactive study-days step; usage data ON by default | Building: ui/v15-onboard-b |
| D53 | Ask Mobi answers at once; no "goes to an AI service" sheet | Building: ui/v15-askinstant (web parity in R8 fixes) |
| D56, D57 (+ D8) | Restore the Start key's lost character; the bar's frosted glass visible; one icon family | Building: ui/v15-icons |
| D51, D52 | Swipe suggestion cards; a richer Today (earlier versions felt cooler) | APPROVED 12:50 pm as v15.1 (TODAY-SWIPE-1018.md); building ui/v15-today-rich and ui/v15-swipe |
| D55 | Audit every recorded app ask against the build, then fix the gaps | Audit plus fixer: ui/v15-ledger |
| D50 | "5, 10, 20 only. No direction until you do a full mock" | CTO decision: 5/10/15/20 + full mock in "How many questions?", day-one direction from marks at stake; ui/v15-length into the final v15 |
| D54 | 50 free credits for free users | DECIDED 12:28 pm: yes (see the 11:21 am-12:30 pm section) |

### Owner 11:21 am-12:30 pm, 18 Oct (D58-D62, D54 decided; his words at the end of OWNER-FEEDBACK-2026-10-18-DAWN.md)
| D | Item | Status / where |
|---|---|---|
| D58, D61 | APK of the walked v15, on his phone | DONE 11:34-11:40 (mockmob-v15-79aaca6d.apk, 1.0.15+3) |
| D59 | The whole "Not done yet" list in the final v15: Review D18, polish 2, icons D8, M-001/2/3, the Mob (switch off), Learn and Review beyond D18 | Building in v15-final-1218 (asks done, 4a1b9b98) |
| D54 | Free AI wallet 10 -> 50 a month: server, website, app together | Building: web/credits50-1018 (wt-credits50) and ui/v15-credits (merged into v15 before the integrator) |
| D60, D62 | Max parallel, nothing stalled; final app in 1-2 hours; scan for anything broken | 17 agents running; chain and times in NOW.md |

### Status at 3:35 pm, 18 Oct (session 25ef3d95 handoff)
- **DONE, live:** release 7 (fc9e1f6b).
- **Verified GO, waiting for his live look:** release 8 (00328e54), which carries W-078, W-075, W-079, W-093, W-089, W-064, W-032, D38, D53 web and D54 web. The migration is not applied yet.
- **App:** D40-D50, D53, D56, D57, D8, M-001 and M-002 passed the emulator walk at 628f3612. D18 is blocked by the Review "316 of 310" HIGH (the fix is partial in 77d51ba8). D49 and M-003 are proven by test only.
- **D51 and D52:** built and critic-checked, in v15.1 wt-v15-1 (88cc6c5d); not walked yet.
- None of the app items is DONE until a walked APK is in his hands.

### Owner at about 3:55 pm, 18 Oct (session 604ced81)
| D | Item | Status |
|---|---|---|
| D63 | "Ship it": release 8 (asked about 3:45 pm) | DONE: migration applied on production (pre/post md5 checked, dry spend rolled back); main 00328e54 READY, 0 runtime errors; STATUS eb5185ef |

### Owner at about 4 pm, 18 Oct (D64-D68; his words at the end of OWNER-FEEDBACK-2026-10-18-DAWN.md)
| D | Item | Status |
|---|---|---|
| D64 | W-099 and W-046: skip | CLOSED by the owner |
| D65 | Practice credits = number of questions (5/10/15/20 -> 5/10/15/20; full mock 50 stays 50) on server, website, app | OPEN: building (R9 web + final app) |
| D66 | The Mob fully built, ON, tested (web and app) | OPEN: staging gate, production switch-on |
| D67 | Ship the final v15 (all his v15 fixes) + the Mob + the website with all his feedback | OPEN: R9 + final app |
| D68 | Within 1-2 hours of 4 pm | target 5-6 pm |

### CEO/CTO decisions while the owner is away (18 Oct from about 4:10 pm, D69)
| # | Decision | Why |
|---|---|---|
| C1 | One FINAL app build instead of two APKs: the v15 walk fixes + per-question prices + the richer Today and swipe stack (v15.1), one integration (1.0.15+6), one emulator walk, one release APK. The old two-walk workflow was stopped at 4:15 pm (the fixer's edits saved as STOP POINT 17ccad0f). | D67 asks for one shipment; one walk saves about 45 minutes of emulator time |
| C2 | Per-question practice prices (D65): Quick 1 credit a question (5/10/15/20); a 50-question full mock stays 50; Pro unchanged; every free allowance unchanged (today's included 10-question set, free first sets, the free 5-question recovery set, Mob papers); old 'attempt' (10) and 'attempt_full' (50) kept for old app builds; new per-count actions in the database. | His words; keeps old builds correct and the credit RPCs atomic |
| C3 | The Mob ships ON (D66) when its real staging gate passes and an independent verifier says GO: production migrations 20261017100000_mob and 20261017190000_mob_fix_1017 under the standing grant, then MOB_ENABLED=true on Vercel Production. The app's Mob is server-driven, so it appears in the app at the same moment. | His words "fully built, switched on, everything tested" |
| C4 | Release 9 (the Mob, credits per question, the audited website fixes) ships on suites + independent verifier GO without waiting for his live look. | His 4 pm "should now be shipped" and D69 |
| C5 | His phone gets the final APK when he is back and plugs it in (only the main session installs). | Nothing touches his phone without him |

### Audit reconciliation: website release 8 (live 00328e54), 18 Oct about 4:45 pm (read-only, 5 surface auditors; evidence in tmp/ledger-audit-1018/results.json and screenshots)
**Totals:** DONE 83, PARTIAL 31, NEEDS_DECISION 7, NOT_TESTABLE 1.

- **DONE (verified on release 8):** D1, D10, D12, D13, D15, D16, D17, D19, D2, D21, D26, D29, D3, D32, D35, D38, D5, D53, D54, F12, F13, F15, F17, F2, L-004, L-014, L-016, L-017, L-018, L-019, M-002, N1, N11, N12, N15, N2, N3, N5, N7, N8, N9, W-002, W-003, W-005, W-008, W-012, W-013, W-017, W-018, W-023, W-026, W-029, W-030, W-032, W-034, W-035, W-038, W-040, W-041, W-047, W-050, W-051, W-052, W-055, W-057, W-060, W-061, W-062, W-064, W-067, W-068, W-069, W-070, W-074, W-076, W-078, W-082, W-083, W-093, W-094, W-095, W-097
- **PARTIAL -> fixed in release 9 (wt-rel9, verifying; DONE only once live):** D28, W-042, W-044, D27 nits, F18, D18 and LOST-X-OF-Y, D15, F11 (one stem, one Repair), D6, D11 (Help -> Guide), N17 (Show me around), W-075, W-079, N6, D8 glyph, D7 badges in Night, M-006 (web onboarding), the /pricing/ai-credits false claim, the onboarding no-cap line, landing 'leaderboard' -> 'Your standing', one price framing, L-013 footer Help for guests, L-019 aurora removed, W-087 details.
- **Still open after release 9:** D25 and W-085 app halves (the final app build), W-033 (needs a signed-in repair walk), W-042 real-account timing, D31 (his landing verdict), W-072/W-073/W-077 (broad premium sweeps), D9 and W-053 (Progress order), M-007 (Compass source check), D20 (Learn one tap on phones is a dock change), D22 (Mob mechanics beyond M1).
- **Closed by the owner (D64):** W-099, W-046. **Decided (D65):** FLAT-10 -> 1 credit a question. **Open design question:** N4 (fine-tune).

### Owner at about 6:10 pm, 18 Oct (D70-D71)
| D | Item | Status |
|---|---|---|
| D70 | Full progress update; anything needed from him | Answered 6:20 pm: R9 and the final app in progress (times in chat); needs: account switch near 95% usage, phone plugged in for the install |
| D71 | Pro, credits and pricing inside the Play app; does Google take 30%; can Play prices be higher; any grey area | Answered 6:20 pm from Google's own pages: India today = 15% on the first USD 1M a year (enrol in the 15% tier) and 15% on auto-renewing subscriptions; 30% only above USD 1M for one-time products; new 10% rates reach the rest of the world by 30 Sep 2027; India User Choice Billing = own checkout beside Play's, fee 4 points lower, different prices allowed. No grey area (app and account removal risk). Recommended: ship web-purchase + app-unlock first (no fee), then Play Billing + User Choice Billing at the same Rs 99. OPEN: his go-ahead on that plan |

### Owner at about 6:25 pm, 18 Oct (D72-D74)
| D | Item | Status |
|---|---|---|
| D72 | Play price about Rs 50 above the web (not 115, not 199) | CTO decision: Pro Rs 149 on Google Play, Rs 99 on the web; prices set in Play Console, never in code; the app never shows the web price (anti-steering) |
| D73 | A plan for selling Pro and credits in the Play app, and build it | BUILDING 6:30 pm: server (wt-play-server, web/play-billing-1018: verify + RTDN + play_purchases migration, flag PLAY_BILLING_ENABLED) and app (wt-play-app, ui/play-billing-1018: in_app_purchase, Get Pro sheet, flag PLAY_BILLING); plan doc docs/brain/PLAY-BILLING-PLAN-1018.md; a real purchase needs his Play Console setup |
| D74 | Everything by 10:30 pm, more parallel agents | Chain in chat: R9 live ~7:30, final app ~8, Play billing built and checked ~9:30, v15.2 APK ~10:15, final message 10:30 |

### Owner at about 6:38 pm, 18 Oct (D75-D77)
| D | Item | Status |
|---|---|---|
| D75 | Pro on Google Play: Rs 150 FINAL (web stays Rs 99) | Recorded; set in Play Console; play-server plan doc updated |
| D76 | One credits wallet on web AND app (practice + AI credits, reload packs); build now, he wires Razorpay today | BUILDING 6:42 pm: web wt-wallet-web (web/wallet-1018: /wallet, /api/wallet, /api/wallet/order + verify, flag WALLET_COMMERCE_OPEN, note WALLET-RAZORPAY.md); app Wallet screen added to the Play billing app agent. Packs (CEO proposal, constants): AI Rs 10/50, Rs 20/150, Rs 50/400 (existing ids, labels renamed); practice NEW Rs 19/100, Rs 49/300; Play prices about 1.5x (AI 15/30/75, practice 29/75) for him to confirm |
| D77 | "No agent is running / stalled": stay on top, more parallel | 6:38 pm check: all 4 agents wrote within 1-5 min; 2 more agents added (wallet web, wallet app scope) |

### Owner at about 6:50 pm, 18 Oct (D78-D81)
| D | Item | Status |
|---|---|---|
| D78 | ONE credits balance for everything (no separate practice and AI wallets) | BUILDING 6:58 pm: core (Opus, wt-credits-core, web/credits-core-1018): one balance = this month's free 50 + held (ai bonus + users.credit_balance); one spend order (free, bought, held) for practice and AI; spend_credits and the AI reserve/consume functions take through one wallet function; no data moved; migration 20261018210000_one_credits_balance + undo; packs credits_10_50 (Rs 10), credits_29_150 (Rs 29), credits_49_300 (Rs 49). Wallet web/app and Play map redirected to one balance |
| D79-D80 | Pro nudges everywhere ("Get unlimited mocks", "No credits needed for practice with Pro"); any Pro feature tap opens "Upgrade to Pro" | BUILDING: web (Opus, wt-pro-nudge), app (wt-pro-nudge-app; app nudges only with Play billing on, the store rule) |
| D81 | First-session pop-up after the first real action (never on or right after onboarding), benefits personalised and true; once ever | BUILDING with D79-D80 |

### Owner at about 7:05 pm, 18 Oct (D82-D83)
| D | Item | Status |
|---|---|---|
| D82 | Packs approved: 50 credits Rs 10, 150 Rs 29, 300 Rs 49 (web); Play Rs 15 / 45 / 75; Pro Rs 150 on Play | DECIDED |
| D83 | Worst-case cost and margin of a Rs 10 / 50-credit pack | ANSWERED 7:10 pm from production runtime_ai_requests (gpt-6-luna avg USD 0.000299, max 0.000479, guard ceiling 0.00237 per reply; a Haiku-class reply about 0.00127). Found: the per-user AI cap would refuse bought credits; fix sent to the credits core agent. Recommendation: a hard output cap per reply, the default on gpt-6-luna |

### Owner at about 7:12 pm, 18 Oct (D84-D85)
| D | Item | Status |
|---|---|---|
| D84 | Nudge, paywall, Pro and pack copy in persuasive marketing English (not generic or flat); truth kept | Sent to the web and app nudge agents 7:14 pm |
| D85 | He switches accounts himself near 95% | RULE for tonight |

### Status at 7:15 pm, 18 Oct (session 604ced81 handoff, stopped at 95% usage)
- **DONE, live:** release 8 (00328e54); production migrations free_ai_wallet_50, practice_credit_per_question, mob + mob_fix (code not yet live for the last three).
- **Built, final checks pending:** release 9 (wt-rel9b 31c4dd21: audit fixes, per-question credits, the Mob); final app 1.0.15+6 (wt-v15-1 01dd7770, walk r1 fixes in); Play billing server (DONE, 9b6cd30b).
- **Mid-build:** one credits balance core (5c553d3a + STOP POINT), web wallet (6237ada2), web Pro nudges (b281ea9a), app billing + wallet (STOP POINT 5ae50007), app Pro nudges (STOP POINT a00ddfe1).
- None of D65, D66, D76, D78-D81 is DONE until live (web) or on a walked APK in his hands (app). Next steps: NOW.md section 4.

### Owner at about 7:20 pm, 18 Oct (D86; new account, session 25ef3d95)
| D | Item | Status |
|---|---|---|
| D86 | Tonight by 10:30 pm, in order: R9 (verify, MOB_ENABLED, push, STATUS); final app 1.0.15+6 (walk, APK, Mob + per-question walk on 3103, install, send); tracks C-H with tests and independent checks; release 10 + production migrations play_purchases and one_credits_balance; v15.2 walked, APK, installed; then ONE message | BUILDING 7:25 pm |

### Owner at about 7:40 pm, 18 Oct (D87-D91)
| D | Item | Status |
|---|---|---|
| D87 | Many more agents in parallel; speed up | 7:45 pm: added the taste workflow (about 12 more agents) on top of the 3 running |
| D88 | Keep nudging agents; never let one stall | A stall monitor on every agent transcript (alert after 8 min silent) |
| D89 | Every check also a taste check with actionable improvements, in his taste; keep improving | OWNER-TASTE-PROFILE.md (synthesised from the ledger and his words) used by every critic; taste critics per surface feed improvement builders for v15.2 and release 10 |
| D90 | Swipe stack: Tinder and taste-learning swipe apps as inspiration; first-time users must learn what cards and left/right mean | Swipe v2: Opus design spec + mock, then build, then Opus taste critic; ships in v15.2 |
| D91 | Stay aligned on all tasks; show how things look early | Send him screenshots of each surface as critics finish |

### Owner at about 7:50 pm, 18 Oct (D92-D93)
| D | Item | Status |
|---|---|---|
| D92 | Taste = independent UI/UX knowledge + his research brain + his records, combined (not only his preferences) | OWNER-TASTE-PROFILE.md section 0 added 7:55 pm; it governs the build and re-check stages |
| D93 | The taste loop is an experiment: real results on usefulness, regressions and agent confusion; keep it only if clearly useful | A blind A/B evaluation after the taste workflow (before vs after, order hidden), plus regressions, skipped or confused items, merge conflicts and cost, in docs/brain/TASTE-LOOP-EVAL-1018.md with a keep/drop call |

### Owner at about 8:15 pm, 18 Oct (D94)
| D | Item | Status |
|---|---|---|
| D94 | Swipe v2 approved as drawn (Up next / Not now, buttons under the deck, first-time demo, undo, honest learning) | BUILDING: ui/v15-swipe2 (wt-v15-swipe2), Opus critic loop, ships in v15.2 |

### Owner at about 8:40 pm, 18 Oct (D95)
| D | Item | Status |
|---|---|---|
| D95 | Skip installing 1.0.15+6 on his phone; finish it and send the APK file; he connects once for v15.2 when the whole app is ready | Recorded; the 1.0.15+6 APK will be sent as a file; v15.2 is the install |

### Owner at about 8:45 pm, 18 Oct (D96)
| D | Item | Status |
|---|---|---|
| D96 | ONE goal: the final app with everything, in about 1 hour; skip the 1.0.15+6 file and everything else; merge everything, one final walk, one fix pass, APK, install | 8:48 pm: the web tracks C/D/E stopped (STOP POINTs: credits-core 6c23b11c, pro-nudge-app 69938fad); one workflow merges ui/v15.1-1018 + Play billing + Pro nudges + taste fixes + swipe v2 into ui/v15.2-1018, one walk, one fix pass, release APK. Release 9 is kept only because the app's Mob and per-question prices need it live |

### Status at about 10:25 pm, 18 Oct (session 25ef3d95)
- **DONE, live:** website release 9 (main 2e45a92c, then STATUS 9b3661e8). It carries D65 per-question credits, the D66 Mob ON (MOB_ENABLED=true on Vercel), and the audit fixes (the ledger PARTIAL list). Vercel is READY with 0 runtime errors; the live smoke test passed.
- **W-044** (the Today cue) is not claimed: it stays OPEN for a decision.
- **Final app** (ui/v15.2-1018 in wt-v15-2, with swipe v2): the one final walk said NO-GO, with 15 HIGH, 11 MEDIUM and 6 LOW (mostly numbers that disagree across screens; the Up next bar covering Start). The one fix pass is running, then the APK and the install (D96).
- **Tracks C/D/E (web wallet, credits core, web nudges):** paused at STOP POINTs for release 10 (D96).

### Status at about 10:35 pm, 18 Oct (session 25ef3d95 handoff, stopped at 96% usage)
- **DONE, live:** release 9 (2e45a92c, STATUS 9b3661e8); D65 (web and server); D66 the Mob ON (web, server); the release 8 audit PARTIAL items (except W-044).
- **Final app (ui/v15.2-1018, wt-v15-2 fae1d928):** everything is merged (v15 fixes, D52, swipe v2 D94, per-question prices, Play billing and nudges behind the flag, taste fixes).
  - The one final walk said NO-GO: 15 HIGH, 11 MEDIUM, 6 LOW (tmp/resume-1018-2230/FINAL-WALK-ISSUES.json).
  - The fix pass is partial: 5 fixed and committed, plus a STOP POINT.
  - Next: finish the fix pass, build the APK, then the install he connects for (D95-D96).
- **Release 10 tracks (C/D/E/F and web taste):** paused at their heads (NOW.md section 4).
- **Taste experiment (D93):** an interim positive result (the critics found real bugs that the walk confirmed). The blind evaluation was not run. Interim call: a lighter version (NOW.md section 5).

### Owner at about 10:40 pm, 18 Oct (D98; new account, session 604ced81 resumed)
| # | Ask | Status |
|---|---|---|
| D98 | Order: final app v15.2 first (review fae1d928, merge taste dec4e083 + c2e950ba, ONE fix pass on the remaining HIGH/MEDIUM + quick LOWs, analyze + unit tests of changes, release APK, one install), then release 10 (two production migrations, one Opus verifier capped at 2 rounds), then ONE message; fast and slow work in separate workflows | DONE 12:47 am: v15.2 installed on his phone (ab04b067) and sent; release 10 live (75ac3f23) with 3 production migrations; one verifier + fixes |

### Owner at about 11:30 pm, 18 Oct (D99)
| # | Ask | Status |
|---|---|---|
| D99 | The 10:30-10:45 pm promise was missed: finish the last bit now and say honestly what the holdup is | 11:32 pm: answered with the real chain; no new scope; APK next |

### Owner at about 11:45 pm, 18 Oct (D100)
| # | Ask | Status |
|---|---|---|
| D100 | Finish everything in THIS session (no 10th carry-over to another agent); speed up | DONE in this session, 12:50 am |

### Status at about 12:50 am, 19 Oct (session 604ced81)
- **Final app v15.2** (1.0.15+7, ab04b067): one fix pass over the final walk (all 15 HIGH and 11 MEDIUM fixed, analyze clean, 6,043 unit tests pass), release APK installed on his phone at 12:47 am and sent as a file. DONE pending his hand check (D96).
- **Release 10 live** (main 75ac3f23, STATUS 23a7c090): one credits balance (D78), wallet, web Pro nudges (D79-D81, D84), Play billing server (off), Today taste fixes, light attempts list. Production migrations play_purchases, one_credits_balance, attempts_list_summary_fn applied with pre/post md5 checks and undo files. Flags WALLET_COMMERCE_OPEN, PLAY_BILLING_ENABLED, PERSISTENT_LIMITS_ENABLED stay off (his steps).
- **Waiting on him:** Razorpay test-card run, Play Console setup, PERSISTENT_LIMITS_ENABLED, W-044 (glass-circle Today cue), his v15.2 hand check.

### Owner at about 1:15 am, 19 Oct: v15.2 and release 10 hand check (G1-G33, verbatim in OWNER-FEEDBACK-2026-10-19.md)
| # | Ask (short) | Status |
|---|---|---|
| G1 | First-open Mobi line and sub-line are broken English; rewrite in proper marketing English | BUILT in app v15.3 (ui/v15.3-1019 125755f4); walk + verifier pending |
| G3 | College search: keyboard keeps cutting off, cannot search | BUILT in app v15.3 (ui/v15.3-1019 125755f4); walk + verifier pending; owner confirms on his phone |
| G4 | Course list: BA (Hons) Business Economics listed as if a top DU course | BUILT in app v15.3 (ui/v15.3-1019 125755f4); walk + verifier pending |
| G5 | Question: target multiple courses? | ANSWER |
| G6 | College order: SRCC, Hindu, Hansraj, LSR (he says); we put LSR above Hansraj; check the data, show the basis | BUILT in app v15.3 (ui/v15.3-1019 125755f4); walk + verifier pending (data puts LSR 912.5 above Hansraj 907.5 for B.Com (Hons) UR) |
| G7 | Only the first 3 colleges show on Today; 4th+ show nothing | BUILT in app v15.3 (ui/v15.3-1019 125755f4); walk + verifier pending (picks 4-5 were a You display cap, never lost) |
| G9 | Show "BCom (Hons) needs English + 3" before a pick, with the course's common sets (nice to have) | BUILT in app v15.3 (ui/v15.3-1019 125755f4); walk + verifier pending |
| G11 | Bottom nav Today pill not evenly rounded | BUILT in app v15.3 (ui/v15.3-1019 125755f4); walk + verifier pending |
| G12 | Suggested deck: a fresh account gets 1 card; bad end copy; clock animation; need 3-4 real cards | BUILT in app v15.3 (ui/v15.3-1019 125755f4); walk + verifier pending |
| G13 | "Do this next" accepted animation: make it better | BUILT in app v15.3 (ui/v15.3-1019 125755f4); walk + verifier pending |
| G15 | Practice lacks Smart mock and NTA mock (v15.2 hid NTA with billing off) | BUILT in app v15.3 (ui/v15.3-1019 125755f4); walk + verifier pending (D101 visible but locked) |
| G16 | Fresh account is incomplete vs his old account: "bare minimum" for testing | BUILT in app v15.3 (ui/v15.3-1019 125755f4); walk + verifier pending |
| G17 | The Mob is hidden inside You | BUILT in app v15.3 (ui/v15.3-1019 125755f4); walk + verifier pending (Mob tab, D105) |
| G18 | Own range input: 900-920 fails, shows "0 of 4 clear" then "Within your range" | BUILT in app v15.3 (ui/v15.3-1019 125755f4); walk + verifier pending |
| G19 | "I don't know my range": estimate from about 5 NTA mocks | BUILT in app v15.3 (ui/v15.3-1019 125755f4); walk + verifier pending (D109 + C-dec 1 free first mock) |
| G20 | Review: no subject choice, cluttered, no recent mocks, no clear history path | BUILT in app v15.3 (ui/v15.3-1019 125755f4); walk + verifier pending (D106 Your papers) |
| G21 | Ask Mobi: "Ask now" and "Ask your record", big and useful | BUILT in app v15.3 (ui/v15.3-1019 125755f4); walk + verifier pending; web /mentor two doors building (C2-web) |
| G22 | No completion moment; weak result screen on mobile; reveal animation gone (regression) | BUILT in app v15.3 (ui/v15.3-1019 125755f4); walk + verifier pending (D108 finish moment restored) |
| G23 | PRINCIPLE: 16-17-year-olds, many new to apps and CBT; simple, obvious, guided | RULE |
| G24 | Web IA: Mob inside Study, everything in Study, Planning inside Marks trends | BUILT in web release 11 (deploy/web-1019-r11 3ae564a6, not pushed); verifier round 2 pending (nav A) |
| G25 | Web: core stats gone from the top; Review order weird; "something is broken" | BUILT in web release 11 (deploy/web-1019-r11 3ae564a6, not pushed); verifier round 2 pending |
| G26 | Web Practice: picking a subject shows "5 questions ... Biology" at the top instead of the mode | BUILT in web release 11 (deploy/web-1019-r11 3ae564a6, not pushed); verifier round 2 pending |
| G27 | Web Start: sideways-scroll cue for the subject selector (asked before) | BUILT in web release 11 (deploy/web-1019-r11 3ae564a6, not pushed); verifier round 2 pending |
| G28 | Web feels like an OLDER version: Full mock / NTA button gradient, textures and gradients gone | BUILT in web release 11 (deploy/web-1019-r11 3ae564a6, not pushed); verifier round 2 pending |
| G29 | Web: no visible "Sign out of this browser" | BUILT in web release 11 (deploy/web-1019-r11 3ae564a6, not pushed); verifier round 2 pending |
| G30 | Homepage morphing text: basic; start the timed change only after the first screen settles | BUILT in web release 11 (deploy/web-1019-r11 3ae564a6, not pushed); verifier round 2 pending (hero C OFF behind HERO_MOTION_V2; owner judges live) |
| G31 | All animations feel faster and less refined than before | BUILT in web release 11 (deploy/web-1019-r11 3ae564a6, not pushed); verifier round 2 pending |
| G32-G33 | Not satisfied; agents must think through every point, exceed it, and act, not loop | RULE |
| KEEP | G2 first onboarding screen, G9 common sets and picks, G10 the bigger bar and animation, G14 Today | KEEP |

### Owner decisions, 19 Oct about 1:35-1:45 am (D101-D110; verbatim in OWNER-FEEDBACK-2026-10-19.md; specs in PLAN-1019.md)
| # | Decision | Status |
|---|---|---|
| D101 | Pro-only modes (NTA mode, Smart practice) VISIBLE but locked in the app while PLAY_BILLING is off; never hidden | PLANNED (Wave A1) |
| D102 | Planning only tonight; a complete handoff with nothing unclear | DONE 2:10 am (PLAN-1019, NOW.md, NEXT-PROMPT-1019) |
| D103 | Colleges ordered by last year's real closing marks for the course and category, number shown | PLANNED (A2) |
| D104 | Today: "Your top 3 of N" plus "See all N" | PLANNED (A2) |
| D105 | App bar: Today, Practice, Start, Mob, You; Review moves into Practice as Your papers | PLANNED (A1) |
| D106 | Your papers: stats strip, subject filter, papers newest first (tap = result + answers), then Mistakes by chapter | PLANNED (A3) |
| D107 | Web navigation: 2-3 mock-ups, he picks before anything moves | PLANNED (Wave B) |
| D108 | After Submit (app): restore the approved finish moment (68f63c11), then completion line, count-up, one next move | PLANNED (A3) |
| D109 | "I don't know my range": estimate after one full mock per subject, progress per subject | PLANNED (A5) |
| D110 | Ask Mobi ("Ask now" / "Ask your record", big): mock-up first | PLANNED (Wave B) |

### Owner decisions, 19 Oct about 2 am to 3:20 am (D111-D117 and C-dec 1; verbatim in OWNER-FEEDBACK-2026-10-19.md)
| # | Decision | Status |
|---|---|---|
| D111 | Explain plainly, ask only what is needed, then run the plan autonomously beyond his expectation | IN EFFECT |
| D112 | If he is away when the mock-ups land, the CTO picks the recommendation and builds it | USED (C-pick 1-3) |
| D113 | No Autopilot "Continue a session" while a session has live agents (it forked and duplicated 10 agents) | RULE |
| D114 | Picks: web nav A, Ask Mobi B, homepage motion C judged live; the marketing copy matters most | LIVE (19 Oct 1:44 pm): nav A, Ask Mobi B on /mentor and in app v15.3, hero C (now ON, D120); copy passes on both |
| D115 | Push release 11 when it passes its verifier; the homepage motion ships OFF behind HERO_MOTION_V2, preview ?hero=v2 | DONE: release 11 live 1:44 pm (a0eb6abe) after verifier round 2 + fixes |
| D116 | Resume order (merge A4a first, relaunch owners, merge early, copy pass, acceptance walks, verifier per platform, ship, ONE message) | DONE 19 Oct about 3 pm (MESSAGE-1019.md); the device walk of build 9 waits on staging |
| D117 | Run the whole night autonomously; the phone install waits for him | DONE: v15.3 build 8 installed 2:45 pm; build 9 (walk fixes) at next connect |
| C-dec 1 | Every student's first full mock in each subject is free (one per subject, ever; a started one counts) | LIVE in release 11; kill switch FIRST_FULL_MOCK_ENABLED=false; app v15.3 sends firstFree and handles the race |
| D118 | Explain the Autopilot usage spike; report progress; continue safely in a fresh session | DONE: explained in MESSAGE-1019 (a forked 600-800k conversation re-read on every step) |
| D119 | Hero too slow: something new every 2-3 s; try last year's 'top 1%' melt | DONE: faster C (?hero=v2, a line every 2.3 s, looping) and the melt (?hero=v3) built and shown live |
| D120 | He chose the faster typing hero (v2): publish it; install v15.3 on his connected phone | DONE: hero v2 ON for everyone (9fd48201); build 8 installed 2:45 pm |

## Waiting on the owner (updated 19 Oct about 3 pm)
- Connect the phone for v15.3 build 9 (the walk fixes). Confirm G3 (college search keyboard) on his phone. Keep or drop "An AI service writes Mobi's replies" under Ask now. Delete ~5 GB of old agent scratch (C: ~93 GB free).
- Answered 3:50 am: M-001 first launch 3 s; M-006 bolder copy; D19 keep badges, refine; D22 Mob.
- D32: confirm the kept landing element when he reviews the port live (wt-land3, port 3206).
- The icons (D8): the proposal is in BADGES-ICONS-1018; it ships with the next app nav change, unless he objects.
- Play Console account and upload key; Anthropic key; Avast HTTPS-scanning exception; 112 held questions; a Hindi reviewer; free first Repair; M-011 Vercel duplicates (his click).

## C-dec 2 (CTO, 19 Oct 6:50 pm, under D111/D112 "designer's pick"): Mob v3 build-spec open points
1. The weekly Mob paper holds its answers and explanations until it closes (Sunday 11:59 PM), like every Mob game (fairness; no leaks to friends who have not sat it).
2. Free's weekly start covers one 24-hour Sprint or Your own round per Mob (no live rooms). 3. A passed mic allows a live room. 4. Live rooms open 6:00 AM to 11:00 PM (minors). 5. Quest size 15 questions per member. 6. Free starters: Dart, Dog-ear, Hexa, Kandil; Hop (redrawn) is the first quest prize. 7. Mob names from a fixed list of 24 (no "Night Owls"). 8. The 6-second podium tier and Mobi once per moment, as specified. 9. "Free members join and play everything" (D133) lifts the one-free-Mob-paper-a-week limit across Mobs.
Spec: docs/design-decisions/pass-1019pm/mob-v3/MOB-BUILD-SPEC-V3.md. Production migration, the Realtime public-access setting and the flags wait for his yes.

## 19 Oct PM decisions (D121-D137; verbatim in OWNER-FEEDBACK-2026-10-19.md; state in NOW.md)
- D121 Play prices; H4 keep and fix the clock (DONE, calm stopwatch, in v15.4); H8 dropped.
- D123/D124 upload key created (folder MockMob-keys in his user folder, backed up); tester atishay07jain@gmail.com. DONE.
- D126 Practice C, Colleges A+B, goal A, "Untimed questions": BUILT and merged in ui/v15.4-1019pm (not yet on his phone).
- D127-D129, D133, C-dec 2: Mob v3 (Den Arena + Live moments, Folds finish C, Free/Pro starts, two streaks): spec done; server Phase A built (staging); app parts built, merge pending; final character art pending.
- D131 reviewer account with Pro: DONE (STATUS has the undo).
- D135/D136 Play Pro = monthly pro_monthly Rs 149; packs Rs 15/45/75: products ACTIVE in Play Console; server and app subscription support at a STOP POINT; production migration and billing deploy need his yes.
- D134 store listing pack ready on his Desktop; closed test not started.
- D137 handoff at 98% usage.

## C-dec 3 (CTO, 20 Oct 2:15 am, under D156 "decide independently"): Ask Mobi's value (J4; proposal docs/design-decisions/pass-1020/ASK-MOBI-VALUE.md)
1. The rule: Mobi never charges for talking. One credit buys a finished job: a mistake fixed and checked to hold (why YOUR option looked right, then 2 fresh check questions), or a doubt settled and then tested (a thread of up to 5 follow-ups that ends with 2 real CUET questions on it). Everything Mobi works out from the record is free.
2. Free: "What should I revise tonight?", the debrief after every paper, the score range against the student's colleges, last look, Daily 5, check-ins. Pro: Mobi jobs use no credits (fair use 10 a day), the week plan, the college gap by chapter, the pace coach.
3. Crowd lines ("most students picked C") only at 30 or more answers on that question.
4. Build order for version 13: (a) the debrief = the finish screen's analysis in Mobi's voice with one "Fix these" key; (b) "Fix it for good" (Repair becomes Mobi's job, reachable from "Ask Mobi about Q7"); (c) "Where you stand" leads the Ask your record door (score range vs the student's colleges, from the projection the web already has), and the mentor context finally reads the student's colleges. The pricing page's "3 credits for a deeper analysis" line goes.

## C-dec 3b (CTO, 20 Oct, after D157): Mobi and AI credits, corrected
- Pro does not make Mobi free. Credits are bought mostly by Pro students; every Mobi job costs credits on every plan (free monthly credits still apply).
- Price each job from its real model cost with a wide margin (1 credit is about Rs 0.25 at the 300-pack price; a job's model cost must stay a small fraction of its credit price; measure it in the code's cost ledger).
- Depth over volume: a credit buys a deeper, more useful job, not more jobs. Repair (1 credit) becomes the flagship: why YOUR option looked right using our trap atlas and your own history, the rule to keep, check questions, and a held check later.
- What is computed from the record (no model call) stays free and is woven through the platform, not boxed in a chat. The website is the main product: every Mobi change lands on the web first or together.

## 31 Oct decisions (D200-D206): intelligence layer and Key cards (plan docs/brain/INTELLIGENCE-LAYER-PLAN-2026-10-31.md)
His words, 31 Oct (dictated): "The main thing that I really care about and focus upon is the card and the feature that we have to build. Other things, you can see yourself and improvise all of that."
- D200 Syllabus: one reference, the real CUET syllabus (units), with NCERT chapters as the study unit and a clear unit for each. Build in every CUET intricacy (options between units, sections such as Maths core/Applied and CS/IP, optional parts). Verify every dropped chapter against the real syllabus before acting. Goal: "the most precise and focused approach towards what is actually coming in the syllabus and what will be asked in the exam."
- D201 No "Older syllabus" shelf unless it clearly reduces confusion (he expects it adds confusion). Default: off-syllabus chapters leave every student surface.
- D202 Cards keep NCERT's exact language, with the reference (book, chapter, page). "That language is what fetches them marks." Paraphrase only for explanations. NCERT books are public; quoting is fine.
- D203 Card categories: the proposed types are good; add and label more as needed. Both halves must be done: backend and database with every needed question/card type and material in place, AND a good-looking, well-integrated frontend.
- D204 Pilot: at least the 5-6 most popular subjects.
- D205 The USD 50 lifetime content ceiling "has been long exceeded and is no longer valid": removed (web/1031-keycards 528fe5e18: budgetLedger, AGENTS.md, COST-POLICY). API credits available on request ($500, $1,000, ...) or use the subscription agent path, whichever fills content better.
- D206 Free vs Pro: Free is a taste ("have a feel for everything, and make people believe that it's useful, but not exactly provide them with actual value"); the real value of cards and the intelligence layer is Pro.

## 31 Oct, about 10:40 am: "keep building and perfecting"
His words, 31 Oct, after the morning handoff: "Good going I'll do all the things you said soon but for now keep going keep building and perfecting more and more things and if you feel like everything is done then lmk"

He will take the owner steps himself soon:
- look at the screens
- the flag
- the syllabus v2 migration and pool shrink
- the deploy
- the app build

The afternoon session built on, without writing to production; see HANDOFF-2026-10-31-KEYCARDS-3.md. The flawed-question fixes, the live re-tag and the pool-audit decisions were added to his list, each with its SQL and undo.

## 31 Oct, about 4:40 pm: the 218 outside-syllabus questions
His words: "Pull them all" (answering "What should happen to the 218 outside-syllabus questions?"; the other choice was
to keep them out of NTA-pattern mocks only).
- D207 All 218 leave every pool (done the same afternoon; docs/brain/intel-1031/off-syllabus-2026-10-31/).

## Learn and Key cards, 31 Oct evening (LK1-LK14; verbatim in OWNER-FEEDBACK-2026-10-31-LEARN.md)
His summary: "Some parts are good and some are very confusing." Study mode is "exactly what we wanted"; the rest of Learn is "far from what we are looking to do".

| Status | Item |
|---|---|
| RENDERS SENT 31 Oct 9:45 pm (preview, web/1031-learn-v2) | **LK1** The way to Key cards is badly placed and too small. |
| LIVE-UNCHECKED (main b7e68f8e2, 31 Oct 6:55 pm) | **LK2** Bug: choosing "Your part" (Accountancy) sometimes glitches and reorders the options. |
| RENDERS SENT 31 Oct 9:45 pm (preview, web/1031-learn-v2) | **LK3, LK8, LK9, LK11** Learn as a whole: hard to use, weakness-led only, walls of text, one fixed next step. He wants student control, clear dynamic next actions with options, tasteful integration in the flow. |
| RENDERS SENT 31 Oct 9:45 pm (preview, web/1031-learn-v2) | **LK4** Read mode layout is weird. |
| LIVE-UNCHECKED (main b7e68f8e2) | **LK5** Study mode is right; add motion (for example on Got it). Keep its structure. |
| LIVE-UNCHECKED (main b7e68f8e2; also the lesson and chapter summary prints) | **LK6** Print chapter sheet: MockMob watermark all over it. |
| RENDERS SENT 31 Oct 9:45 pm (preview, web/1031-learn-v2) | **LK7** Last look vs Read is unclear. |
| RENDERS SENT 31 Oct 9:45 pm (preview, web/1031-learn-v2) | **LK10** The flow: subject, then concept or chapter, then what is lined up, then a time, then a mix of cards and questions. Plus a separate place to find what is where and revise chosen cards. |
| RENDERS SENT 31 Oct 9:45 pm (preview, web/1031-learn-v2) | **LK12** Cards are the core of Learn; bring them to Explore as a custom chapter feed (for example a 10-minute run of cards and MCQs). |
| LIVE-UNCHECKED (main b7e68f8e2; 3,916 to 1,439 Must-know, 25%) | **LK13** Too many cards carry "Must-know". |
| OPEN | **LK14** Think longer; ideate better. Any replacement layout is shown to him as real renders before it ships (Never again 1). |
| BUILT behind flags (1 Nov, e8e6d3c0c; claimed at the first answer) | **LK15 (A9):** questions in the Explore feed and Learn sessions are free "up to a certain limit". CTO rule: Free gets one Learn session a day (a chapter run or the feed, up to 10 min); Explore swipe stays unlimited; Pro gets any number. |
| CLOSED: REJECTED 31 Oct 11:50 pm, current nav stays | **LK16 (N1):** Learn becomes its own section; the app bar cannot grow. Spec: learn-1031/NAV-2.md (web sidebar place; on phones, a Practice/Learn title switch in the Practice tab). |
| ANSWERED | **LK17:** he sees no change in Learn. Nothing is deployed; the local preview was opened in his browser pane. |
| BUILDING (live phone prototype) | **LK18:** keep the Explore feed and make it "a very cool feature on the mobile app"; Find inside Learn (search). Spec learn-1031/FEED-2.md. |
| RULE | **LK19:** he comments only on live prototypes he can use, not mock-ups. Give him a link that opens on his phone. |
| BUILT IN PREVIEW, AWAITING HIS LOOK (1 Nov 6:20 am) | **LK20:** the feed on a computer has no way to the next item ("stuck on one thing") and too much blank space everywhere. He likes the direction. |
| BUILT IN PREVIEW, AWAITING HIS LOOK (1 Nov 6:20 am) | **LK21:** he loves the Explore covers, but every Accountancy cover shows the same subject object. Make each cover chapter-specific. |
| BUILT IN PREVIEW, AWAITING HIS LOOK (1 Nov 6:20 am) | **LK22:** the chapter run (chapter, time, adjusted mix) is "quite good"; refine it a lot; too much blank space and UI refinement across Learn. |
| WEB BUILT AND TESTED behind flags (1 Nov 6:20 am); app port next | **LK23:** build the feature completely now, test everything, fix every issue, refine UI/UX and logic, make it more useful with the systems around it; then tell him what is needed from him. |


## Learn v2 live, 1 Nov afternoon (LK24-LK35; verbatim in OWNER-FEEDBACK-2026-10-31-LEARN.md, section "1 Nov 2026, about 4:05 pm")
His frame: "Keep going. You have a bit of a direction and a taste of what I have wanted initially. Now you have to double down on it."

| Status | Item |
|---|---|
| LIVE 1 Nov ~11:55 pm (main 668341aea): one subject picker on phones, no status line or ring dots, Saved grouped; check on his phone | **LK24** The phone website is too cluttered. |
| WAITING ON HIM (2 Nov ~9:20 am): 1.0.19+17 built and signed (upload key, same signer as 16), gated and walked on the emulator against the live web; file C:/Users/atish/Desktop/MockMob-build-17/mockmob-1.0.19+17-sells.aab with OWNER-STEPS.md. He uploads it to Play closed testing, then checks Learn on his phone. Branch ui/1101-learn-app not merged | **LK25** Ship a fresh Google Play release as soon as the app update is ready. |
| LIVE 1 Nov ~11:55 pm (main 668341aea): four equal tabs Practice · Learn · Explore · Papers; Saved moved into Explore | **LK26** The Explore / Saved / All top tabs confuse a first-time visitor. |
| LIVE 1 Nov ~11:55 pm (main 668341aea): "Start learning Accountancy" / "Start chapter 1 · 10 min", no zero anywhere (pinned by tests) | **LK27** Learn leads with a clear offer to start learning ("Start learning <subject>", "Your roadmap"), never a line of zeros. |
| LIVE 1 Nov ~11:55 pm (main 668341aea), partly: combined /api/today and /api/learn/home reads, auth chain in parallel, /api/stats CDN cache (MISS then HIT), CSS split; Fluid compute not readable through the API | **LK28** The phone website and the website are slow. |
| LIVE 1 Nov ~11:55 pm (main 668341aea): the next card peeks as a real card edge with a one-time Mobi chip; first-run turn and question hints once per student | **LK29** First-time cues: the Explore feed moves by swiping down, so show how. Think about cues everywhere. |
| LIVE 1 Nov ~11:55 pm (main 668341aea): cards are flashcards (text centred), question options in the thumb zone, end keys pinned at the bottom | **LK30** Too much blank space; use it. |
| LIVE 1 Nov ~11:55 pm (main 668341aea): one end screen: headline, up to 3 numbers, the bar, one key and one link | **LK31** End screens carry too many lines and walls of text. |
| LIVE 1 Nov ~11:55 pm (main 668341aea): the painted room, Mobi tap reactions with bubble lines, one still headline, desktop Mobi in the gutter. Left: a repainted Day poster (image job) | **LK32** Home hero: 10-20% less space for the details, more branded, reacts to taps (Mobi). Use the animation and promo-film assets. |
| STANDING GOAL | **LK33** Keep improving the feature and the whole UI/UX, plus the usefulness of every feature, until satisfied. |
| IN PROGRESS: 15,707 cards live. Every subject over 3 h except Mathematics (548 cards, ~2.9 h, 3 Nov ~2:40 pm, main 29b001d8e): all 13 NCERT chapters carry typeset formulas checked against the page images; NCERT 2026-27 supports about this much (two chapters cut by NCERT, four Applied Maths chapters have no NCERT book). His answer 2 Nov, verbatim: "Yes, start it" (formula pipeline) | **LK34** Populate every subject and chapter: at least 3 hours of study per subject, more is fine. |
| STANDING GOAL | **LK35** Keep going; double down on this direction. |
| DECIDED 1 Nov ~5:45 pm | **LK34 route:** asked for an Anthropic API key (about $500) for card batches, he chose "Use subscription". Cards are written by subscription agents, paced across the 5-hour windows. The API pipeline (scripts/keycards/api-batch.mjs, web/1101-content-api 3b0feaa05) stays ready, unused. |

## Learn v2 on the web, 2 Nov about 10 am (LK36-LK49; verbatim in OWNER-FEEDBACK-2026-10-31-LEARN.md, section "2 Nov 2026, about 10 am")
Owner of this round: the app port session (c4dbd3b5), coordinating with the Key cards session for main pushes.

| Status | Item |
|---|---|
| IN PROGRESS | **LK44** Every answer is A. Keys in the verified bank are skewed to A; options must be shuffled wherever they are served unshuffled, the key moving with them. |
| IN PROGRESS | **LK45** Do fixes 2, 3 and 4 (one count on the stop sheet and the end; the app's Print sheet row named for what it opens; a Revise run's head line says Revise). |
| IN PROGRESS | **LK38** Missed it / Got it / Easy: nobody can tell what they do; Missed it seems to do nothing; Got it and Easy look the same. |
| IN PROGRESS | **LK37** "Start 10 min" cannot be changed; let the student choose how many Key cards, questions and mistakes a run holds. |
| IN PROGRESS | **LK40** Scrolling over the question area does not scroll the page. |
| LIVE 4 Nov ~1 am (main 55a1d2f63): bigger stage and type from 1360 px | **LK41** Desktop is scaled down with too much blank space. |
| LIVE 4 Nov ~1 am (main 55a1d2f63): Key cards as index cards (paper, family band, ruled back; Night without a rim) | **LK39** Cards look boring in Light and Dark; make them more interesting. |
| LIVE 4 Nov ~1 am (main 55a1d2f63): Night cards with one quiet hairline, no rim; lime only on the primary key | **LK43** Dark mode: the neon glow around every card is too much; make it subtle. |
| LIVE 4 Nov ~1 am (main 55a1d2f63) on the web (one capsule); app BUILT 4 Nov ~8:15 pm in 1.0.20+18 (You plan strip), waiting for his upload | **LK42** Top bar: the Pro, credits and wallet marks look low quality; rethink the top bar (web and app). |
| IN PROGRESS | **LK46** Web tabs: four equal tabs are fine; order Practice, Papers, Learn, Explore. App tabs: he will look on the phone first. |
| IN PROGRESS | **LK47** The website's scroll feels too fast in its first section; slow it down. |
| TO ANSWER | **LK48** Has copying the app's UI to the web hidden options or made some unreachable? Confirm. |
| TO ANSWER | **LK36** English seems to list only Verbal Ability; are all subjects' chapters listed? |
| STANDING | **LK49** The small UI/UX fixes he gave long ago still have to be done. |

## The app on his phone, 3 Nov about 1:30 pm (LK50-LK54; verbatim in OWNER-FEEDBACK-2026-10-31-LEARN.md, section "3 Nov 2026, about 1:30 pm")

| Status | Item |
|---|---|
| BUILT 4 Nov ~8:15 pm in 1.0.20+18 (Desktop/MockMob-build-18, signed with the upload key; ui/1103-app-18 c93a34c95 pushed); waiting for his upload: the settler clears a stale owed paper and its pinned notification; only the server closes a paper  | **LK50** On his main account every app screen shows "Sending your answers · Computer Science mock". A glitch: a stale local draft keeps pendingSubmission after its submit window, so the strip never clears. |
| BUILT 4 Nov ~8:15 pm in 1.0.20+18 (Desktop/MockMob-build-18, signed with the upload key; ui/1103-app-18 c93a34c95 pushed); waiting for his upload: Explore is Practice's fourth door  | **LK51** The app has no Flow (Explore) feed; Practice, Papers and Learn are there. |
| BUILT 4 Nov ~8:15 pm in 1.0.20+18 (Desktop/MockMob-build-18, signed with the upload key; ui/1103-app-18 c93a34c95 pushed); waiting for his upload: the calm Learn  | **LK52** The app's Learn section is still a bit cluttered; its UI needs improving. |
| BUILT 4 Nov ~8:15 pm in 1.0.20+18 (Desktop/MockMob-build-18, signed with the upload key; ui/1103-app-18 c93a34c95 pushed); waiting for his upload; review + emulator walk fixes in it  | **LK53** The whole app: keep what is right, make it stronger and more premium, in the direction of Duolingo. |
| STANDING | **LK54** Keep a running list of what needs his feedback; he answers when back. Continue yesterday's work (Maths formula cards, the remaining chapters). |

## LAN preview look, 3 Nov about 3:15 pm (LK55-LK62; verbatim in OWNER-FEEDBACK-2026-10-31-LEARN.md, section "3 Nov 2026, about 3:15 pm"). He said: stop everything, record only; continue after his PC restart.

| Status | Item |
|---|---|
| OPEN | **LK55** The preview looks exactly the same as before. Top bar with credits and Pro is good if that is what it shows. |
| LIVE 4 Nov ~1 am (main 55a1d2f63): the preview tabs keep Learn v2 (a preview fault, not the live site) | **LK56** The bar shows Practice, Papers and Explore, but there is no way to reach Learn in that version. |
| LIVE 4 Nov ~1 am (main 55a1d2f63): preview fault fixed (tabs keep the real decks) | **LK57** "Chapter feeds did not load." shows on the preview. |
| LIVE 4 Nov ~1 am (main 55a1d2f63): the new card look, visible on phones | **LK58** The card look is exactly the same as before (LK39 not visible). |
| LIVE 4 Nov ~1 am (main 55a1d2f63): Up next as one module, one voice (Suggested) | **LK59** The intelligent recommendations that were added make the UI feel cluttered: the implementation in the UI is not good. |
| LIVE 4 Nov ~1 am (main 55a1d2f63) on the web; app BUILT 4 Nov ~8:15 pm in 1.0.20+18, waiting for his upload | **LK60** No vague icons: use proper branded icons, a generated image, or something better. |
| LIVE 4 Nov ~1 am (main 55a1d2f63) on the web (Learn, Explore, Key cards); app in 1.0.20+18; ~400 lines elsewhere still to do | **LK61** The English everywhere must be improved (repeat). |
| PARTLY LIVE 4 Nov ~1 am (main 55a1d2f63): Find's sets on Learn home; more in R7 W-WEB-FULL.md "Next" | **LK62** The mobile website is now nearly a copy of the app, but the website has more features and must be a full-fledged experience; plan how, especially Learn. |

## Ship for real, 3 Nov about 11:55 pm (LK63-LK66; verbatim in OWNER-FEEDBACK-2026-10-31-LEARN.md, section "3 Nov 2026, about 11:55 pm")

| Status | Item |
| --- | --- |
| IN PROGRESS (4 Nov ~3 am stop): web lanes done and live; app merged, review done, fixes/walk/build left | **LK63** Finish every open lane (Physics, app 1.0.20+18, web cards/top bar/icons/full website, English), then review the UI against all his past feedback and keep improving until satisfied. |
| DONE 5 Nov ~12:35 am: AAB 1.0.20+18 (Desktop/MockMob-build-18, his upload pending) and the web live at main 09a5bbe39 | **LK64** No prototype links or test builds: a final AAB he uploads straight to Google Play, and the final web changes deployed to www.mockmob.in so he sees them on every device. Supersedes "ship each web change only after his live look" for this round. |
| DONE 4 Nov ~3 am except the 610 MB snapshot push (his command in the handoff) | **LK65** Commit all uncommitted work; the project final and up to date today, recorded as a proper checkpoint, for handing over and onboarding other members. |
| ANSWERED 4 Nov ~12:10 am: "Push branches to GitHub" (his button answer) | **LK66** His message ends "Everything then should be sent to": where? Push every branch to GitHub, after the production web deploy so preview builds do not queue ahead of it. Vercel is on Hobby (100 deployments a day, one build at a time): 438 branch pushes would block production for up to a day, so the ~15 current branches go up as branches and the older ones as archive/<branch> tags (tags start no Vercel build; checked on one first). |

## Home page hero and brand, 4 Nov about 2:05 am (LK67-LK76; verbatim in OWNER-FEEDBACK-2026-10-31-LEARN.md, section "4 Nov 2026, about 2:05 am"). His scores: brand vs AI slop 7/10 overall, Night 6/10; logo and fonts are good.

| Status | Item |
| --- | --- |
| LIVE 5 Nov ~12:35 am (main 09a5bbe39, Desk Light home page; spec home-spec/SPEC-HOME-1104.md) | **LK67** Hero parity: the phone hero's Mobi tap animation and changing bubble feel weird on a phone, and the desktop hero has none of it. One hero idea on both. |
| LIVE 5 Nov ~12:35 am (main 09a5bbe39, Desk Light home page; spec home-spec/SPEC-HOME-1104.md) | **LK68** Night hero looks like AI slop: too much neon highlighting and neon edges. Research what AI slop looks like and remove it. |
| LIVE 5 Nov ~12:35 am (main 09a5bbe39, Desk Light home page; spec home-spec/SPEC-HOME-1104.md) | **LK69** Phone scroll on the home page is inconsistent and laggy: one gesture = one step, never speed-dependent (a fast flick must not skip several, a slow drag must not stop half way). |
| LIVE 5 Nov ~12:35 am (main 09a5bbe39, Desk Light home page; spec home-spec/SPEC-HOME-1104.md) | **LK70** Phone hero: over half the screen is Mobi and decoration, with no word of CUET, exams or what MockMob is. Keep Mobi, but the hero must say what we are. |
| LIVE 5 Nov ~12:35 am (main 09a5bbe39, Desk Light home page; spec home-spec/SPEC-HOME-1104.md) | **LK71** AI-slop traits and text walls on the home page; shorten. |
| LIVE 5 Nov ~12:35 am (main 09a5bbe39, Desk Light home page; spec home-spec/SPEC-HOME-1104.md) | **LK72** The exam screen on the home page is too tall, and must show the real MockMob exam screen (better and unique), not a copy of the NTA interface. |
| LIVE 5 Nov ~12:35 am (main 09a5bbe39, Desk Light home page; spec home-spec/SPEC-HOME-1104.md) | **LK73** A stronger brand identity of our own: illustrations, typography hierarchy, consistent use of Mobi. Keep the fonts and the logo (not the common AI fonts). |
| LIVE 5 Nov ~12:35 am (main 09a5bbe39, Desk Light home page; spec home-spec/SPEC-HOME-1104.md) | **LK74** Reference ug.preparoo.app: a refined loading animation on entry and a refined typing animation on the home page; that level of refinement. |
| STANDING | **LK75** Refine these small things automatically, ourselves; think it through. |
| DONE 4 Nov ~2:10 am | **LK76** The push command failed: it ran in the parent folder, which is not a git repository. Gave him a one-line command that names the repository. |
| ANSWERED 4 Nov ~6:35 pm: status, ETA (AAB about 9 pm, website about 11 pm IST), nothing blocking needed from him | **LK77** Continue where you left off; tell me what is done, what is left, by when it all completes, and whether anything is needed from me. |
| DONE (by him, 3-4 Nov night; verified 4 Nov ~6:45 pm: origin refs/archive/uncommitted-1104-main = 117408243) | **LK78** The 610 MB backup push is up to date; he did it yesterday. Do not ask again. |
| ANSWERED 4 Nov ~6:55 pm: live = main ced6f747f (Learn fixes only); the home page shown in screenshots is not deployed yet, ships after the gate | **LK79** Has anything been deployed? The live site looks unchanged and different from the screenshots in the chat. |
| DONE 5 Nov ~12:35 am: AAB 1.0.20+18 in Desktop/MockMob-build-18; home page live (main 09a5bbe39); reported to him | **LK80** Speed up: fix everything, deploy everything, then tell me; as perfect as it can be when I see it. |


## Live mobile site look and the night's refinement, 5 Nov about 2:40 am (LK81-LK98; verbatim in OWNER-FEEDBACK-2026-10-31-LEARN.md, sections "5 Nov 2026, about 2:25 am" and "about 2:40 am")

| Status | Item |
|---|---|
| LIVE 5 Nov ~5:50 am (main 7b47b4c90) | **LK81** Fix the slow-phone stutter on the Lab and tour sections (first draw at 4x CPU, the tour's per-step rebuild). |
| LIVE 5 Nov ~5:50 am (main 7b47b4c90) | **LK82** The hero's "CUET 2027." line: its font and colours look weird. |
| LIVE 5 Nov ~5:50 am (main 7b47b4c90) | **LK83** The main CTA is only "Try 5 questions"; the main CTA should be sign up / log in (or similar), not only the five questions. |
| LIVE 5 Nov ~5:50 am (main 7b47b4c90) | **LK84** Uneven text lines (for example "Pick yours free"): better typographic choices. |
| LIVE 5 Nov ~5:50 am (main 7b47b4c90) | **LK85** Improve the hero section and the rest a bit more. |
| LIVE 5 Nov ~5:50 am (main 7b47b4c90) | **LK86** The statement scroll lost its mix of white and green (volt) words, which was well branded; bring it back, better. |
| LIVE 5 Nov ~5:50 am (main 7b47b4c90) | **LK87** Scroll feel, blur and motion and the tour's desk-object icons are good; more thought for the newer parts, especially PrepOS / Ask Mobi. |
| LIVE 5 Nov ~5:50 am (main 7b47b4c90) | **LK88** Scrolling up shows one CTA after another (the dock changing); CTAs should be sign up, log in or similar, not only the five questions. |
| LIVE 5 Nov ~5:50 am (main 7b47b4c90) | **LK89** "Try a CUET question" sometimes gets stuck in a scroll loop; when not, the arrival is not clean (a white box, then a highlight). |
| LIVE 5 Nov ~5:50 am (main 7b47b4c90) | **LK90** Scroll still inconsistent: it glitches, especially when scrolling really fast. |
| LIVE 5 Nov ~5:50 am (main 7b47b4c90) | **LK91** The exam screen's MockMob / NTA switch: he liked the previous one better (it showed the real URL); the NTA mode is not accurate now. |
| LIVE 5 Nov ~5:50 am (main 7b47b4c90) | **LK92** Add desktop photos or a device mock-up in the exam (NTA) section; think of more like it. |
| LIVE 5 Nov ~5:50 am (main 7b47b4c90) | **LK93** A section (probably DU Eligibility, "Energy") loads a bit slowly. |
| LIVE 5 Nov ~5:50 am (main 7b47b4c90); app 1.0.21+19 built (Desktop/MockMob-build-19) | **LK94** Learn: subject options must be asked at onboarding and editable in Learn: Computer Science Section B1 (Computer Science) or B2 (Informatics Practices); Accountancy Part B Analysis of Financial Statements or Computerised Accounting; every subject with such a choice. App and web. |
| LIVE 5 Nov ~5:50 am (main 7b47b4c90) (web: Pro sheet words, card turn); app 19 card turn | **LK95** Key cards are really good (turn-over can be refined); Explore feed much better; MCQs improved. Carry the app's things to the web: the Pro plan descriptions, the app's UI exactly, its animations. |
| DONE 5 Nov ~5:50 am: web live; app 1.0.21+19 in Desktop/MockMob-build-19 for his upload | **LK96** After these fixes: send the final app (Play build) and deploy everything to the website. |
| LIVE 5 Nov ~5:50 am (main 7b47b4c90) | **LK97** Tapping the profile at the top should open a small pop-up with quick toggles (Day/Night and the like), not jump to the whole You page. |
| STANDING (round 1 live 5:50 am, round 2 live ~7:50 am: the app's motion on the web, public and app pages refined) | **LK98** Keep going until morning until satisfied with the app and the website: a proper overall refinement (UI/UX, brand, fonts, typography); keep doubling down on the brand. When all of it is done and he is away: add content (more questions, Learn and practice, Key cards). |

## His look at the live site after the night, 5 Nov about 10 am (LK99-LK114; verbatim in OWNER-FEEDBACK-2026-10-31-LEARN.md, section "5 Nov 2026, about 10 am")

| Status | Item |
|---|---|
| LIVE 5 Nov ~4:45 pm (main ce24dc682) | **LK99** The new CTAs are in, but the hero needs more refinement; Preparoo's landing is cleaner and better in some ways. |
| LIVE 5 Nov ~4:45 pm (main ce24dc682) | **LK100** Brand every element properly: the hero's second beat ("Five questions free", "73 DU programmes") must be shown properly, removed, or used better. |
| LIVE 5 Nov ~4:45 pm (main ce24dc682) | **LK101** Day mode: the green is everywhere, extremely light, and a very different colour from before and from the brand colour. Find why and fix. |
| LIVE 5 Nov ~4:45 pm (main ce24dc682) | **LK102** The statement: "MockMob" in "MockMob shows you where" must be green too. |
| LIVE 5 Nov ~4:45 pm (main ce24dc682) | **LK103** On phones the held stories' card fills the whole screen to the bottom; leave 10-20% at the bottom like Preparoo, with a blur and a progress/loading cue. A clear way to skip to the bottom or the top. |
| LIVE 5 Nov ~4:45 pm (main ce24dc682) | **LK104** The MockMob logo in the site bar takes you to the top (on the home page), and there is a way to the bottom too. |
| LIVE 5 Nov ~4:45 pm (main ce24dc682) | **LK105** "What's inside MockMob" (the tour) is still glitchy in its animation, sometimes. |
| LIVE 5 Nov ~4:45 pm (main ce24dc682) | **LK106** The exam screen: he likes the desktop version; on phones it is too small to see. A tasteful phone version. |
| LIVE 5 Nov ~4:45 pm (main ce24dc682) | **LK107** The numbers card under the exam section (5,765 questions, 15 subjects, ₹99) has little relevance; remove or use it well. |
| LIVE 5 Nov ~4:45 pm (main ce24dc682) | **LK108** Branding has been removed in many places and the landing became plainer ("Featured by CUET creators" and more); bring the brand back. |
| LIVE 5 Nov ~4:45 pm (main ce24dc682) | **LK109** The home page's pricing section: cleaner, like the pricing page: one plan, everything in it. |
| LIVE 5 Nov ~4:45 pm (main ce24dc682) | **LK110** The final card (with the referral code) needs thought; value framing like "₹22 a day": ask how many mocks a day or month, a toggle that shows the value per mock (₹1, ₹2 a mock). |
| LIVE 5 Nov ~4:45 pm (main ce24dc682) | **LK111** An honest comparison with other platforms ("on platform X you pay ₹5,500 for this; here this much"). |
| LIVE 5 Nov ~4:45 pm (main ce24dc682) | **LK112** Preparoo-level polish: loading animation everywhere, a very clean look; a Key cards (flashcards) section on the home page with the glass look the pricing cards have. |
| PARTLY DONE 5 Nov ~4:45 pm: CAS 207 + English reading 231 cards live; Financial Markets blocked (truncated archive) | **LK113** Content: his OK to download any NCERT book needed and to do anything else needed for content. |
| STANDING | **LK114** His feedback is a direction, not a full list: understand it and apply the same thinking everywhere on our own. |
| DECIDED 5 Nov ~11:10 am | **LK115** Accountancy Part B: keep both choices (AFS and CAS) at onboarding and in Learn; AFS default, with the 2025-paper line. |
| ANSWERED 5 Nov ~3:55 pm | **LK116** Why did you stop working? Tell me what is left, what is needed from me, and what is done. |

## The full website and app feedback, 5 Nov about 11:40 pm (LK117-LK147; verbatim in OWNER-FEEDBACK-2026-10-31-LEARN.md, section "5 Nov 2026, about 11:40 pm")

| Status | Item |
|---|---|
| LIVE 6 Nov (main 068a7a061) | **LK117** Desktop hero: too much white/blank space; massive and clearly visible like Preparoo, filling the screen (only small side margins); a background texture like before, especially in Night. |
| LIVE 6 Nov (main 068a7a061) | **LK118** Day green is still not exactly right. |
| LIVE 6 Nov (main 068a7a061) | **LK119** The whole site is not optimised for desktop (and tablet/laptop): formatting at every size. |
| LIVE 6 Nov (main 068a7a061) | **LK120** Mobile hero: no texture, no highlighting of CUET; the typed line is sometimes there, sometimes gone: find why and fix. |
| LIVE 6 Nov (main 068a7a061) | **LK121** Remove the fact line ("5,765 questions. Free to start, Pro ₹99 a month.") from the hero; keep "Have an account? Log in". |
| LIVE 6 Nov (main 068a7a061) | **LK122** The demo card's copy ("Hi, I'm Mobi. Your first question. Go." ...) is weak: rewrite from a marketing angle. |
| LIVE 6 Nov (main 068a7a061) | **LK123** "Not your subject?" on the demo: pick a subject, get 5 random questions from that subject's bank. |
| LIVE 6 Nov (main 068a7a061) | **LK124** The fact strip ("5 questions free", "73 DU programmes") is useless/unclear: show the main features or remove; "as low as ₹1 a mock" is a better hook. |
| LIVE 6 Nov (main 068a7a061) | **LK125** In the statement "MockMob" must be green from the start, not turn green on scroll. |
| LIVE 6 Nov (main 068a7a061) | **LK126** Mistake Lab: the Repair and SWOT scenes are cluttered on phones. |
| LIVE 6 Nov (main 068a7a061) | **LK127** Too much white space between items and sections on phones (Score Recovery Lab and others). |
| LIVE 6 Nov (main 068a7a061) | **LK128** Key cards section: refine more; less blank space. |
| LIVE 6 Nov (main 068a7a061) | **LK129** The exam section ("Practise calm, then rehearse exam day") degraded: revert to the previous version or do it properly. |
| LIVE 6 Nov (main 068a7a061) | **LK130** Pricing: the plan card covers too much of the big "Pro" word; move it lower; in Day the word is hard to see. |
| LIVE 6 Nov (main 068a7a061) | **LK131** Value slider: 2 a week is too low; start at 5-7 a week so even the lowest makes students feel they practise too little, under ₹10 a mock; a cool catch at the top end (under ₹1). |
| LIVE 6 Nov (main 068a7a061) | **LK132** Remove the "What each costs to May 2027" comparison completely (bad copy, weak UI, naming other platforms is legally risky). |
| LIVE 6 Nov (main 068a7a061) | **LK133** The nav's Pricing pill goes to the /pricing page, not #pricing. |
| LIVE 6 Nov (main 068a7a061) | **LK134** /pricing: the bottom plan card refined like the home page's; the final slide as "Free or Pro" or similar. |
| LIVE 6 Nov (main 068a7a061) | **LK135** The phone bottom bar (Log in / Sign up free): spacing and UI/UX issues; the CTA is weak. |
| LIVE 6 Nov (main 068a7a061) | **LK136** Learn Accountancy Part B (AFS vs CAS) affects only the last chapters (CUET Part 1/Part 2; three Class 12 books): cross-check the approach. |
| LIVE 6 Nov (main 068a7a061) | **LK137** Web Key cards: rating by swipe (right Got it, down Easy, left Missed) as well as keys. |
| STANDING | **LK138** Keep adding refinements like these on our own, without being told again. |
| LIVE 6 Nov (main 068a7a061) | **LK139** Learn search is cluttered; the Show answer toggle is broken; a chapter search shows chapters and cards instead of the chapter. |
| LIVE 6 Nov (main 068a7a061) | **LK140** Learn is clunky overall: refine. |
| LIVE 6 Nov (main 068a7a061) | **LK141** The You button does not open the full You section while the top profile icon does: the opposite of what it should do. |
| LIVE 6 Nov (main 068a7a061) | **LK142** Arena (Today, Practice, everything) still feels limited and not easy enough to use; not impressive. |
| LIVE 6 Nov (main 068a7a061) | **LK143** Ask Mobi (the AI layer) has disappeared from the UI: bring it back as a main feature, with a plan. |
| OPEN | **LK144** App: more haptics (for example the Mob tutorial); the Explore and Learn feeds are good: only a little greener/better. |
| STANDING | **LK145** Split the effort 80% website (desktop, laptop, tablet, phone) and 20% app. |
| LIVE 6 Nov (main 068a7a061) | **LK146** Arena desktop: the sidebar needs UI refinement (the feed's use of the screen is fine). |
| STANDING | **LK147** Do not worry about the weekly limit; keep going; when close to the limit, stop and prepare a handoff so he can continue on another account. |
| DONE 6 Nov ~12:40 am | **LK148** Stop at 90% usage and hand off; a temporary 2-3 day trial of GPT-6 Terra on our workflow, tracked in a side file only; no standing rules; Opus stays primary. |
| DONE 6 Nov ~2 am | **LK149** Not a trial: the next session is a normal one (ships through the gate); give the prompt inline. |
| LIVE 6 Nov (main 068a7a061) | **LK150** All six web branches integrated and released after the full gate. |
| DONE 6 Nov | **LK151** The owner restored Vercel team access. Deployment listing and private runtime error lookup succeeded. |
| PAUSED AT OWNER REQUEST 6 Nov | **LK152** Stop running work at 5% usage. Save an evidence-backed handoff and a next-session prompt. |
| DONE 6 Nov ~1 pm | **LK153** Resume Round 4: fix the stale gesture source assertion, pass the full gate (0 frames over 100 ms cold and warm, 128/128 at 390, every 390/1440 Night/Day capture looked at), then push main and verify Vercel, private errors and the live phone view. No sign-in, no production database writes. |
| LIVE 6 Nov (main d629a2939) | **LK154** "Something with the scroll animation and the entire scroll of the website is broken ... behaving very weirdly in this part ... scroll is completely broken in this pass." Found: a mouse wheel spun without a pause could not enter a held story (Mistake Lab first): the page shook 100 px at its edge for as long as the wheel turned (wheel/clamp code of 4-5 Nov; the 9-case wheel matrix never spun in from outside). |
| LIVE 6 Nov (main d629a2939) | **LK155** "The landing page: the texture ... behind it ... is kind of very weird. That thing needs to be replaced." (the R4 answer-sheet bubble field behind the hero) |
| LIVE 6 Nov (main d629a2939) | **LK156** "The icons ... for the card that you have built (Unlimited Mocks, Mistake Lab, Score Recovery, Ask Mobi ...) need improvement." (the hero feature strip) |
| LIVE 6 Nov (main d629a2939) | **LK157** "What a mock costs at your pace": "5, 1 per paper, what does that mean? ... it should not look like that ... There should be a slider for how many things a student can do (1 mock, then repairs, then key cards and other stuff). Make some marketing material around it ... so appealing that the cost is so low that someone thinks, 'How is this even possible?' ... So many features other than mocks ... which the Pro plan gives." |
| LIVE 6 Nov (main d629a2939) | **LK158** Small round: do all the fixes and report; also analyse what the Claude session did, what the ChatGPT session did, and the result of the model test. |
| LIVE 6 Nov (main d629a2939) | **LK159** Hero: "How you have highlighted CUET 2027, I don't mean that you have to straight up just run a highlighter over it. It looks very bad and is not tasteful at all." (keep CUET emphasised, LK120, but tastefully) |
| LIVE 6 Nov (main d629a2939) | **LK160** Strip icons: the drawn line icons "are honestly a regression even more ... look very weird rather than the 3D-generated icons." Go back to 3D icons, improved. |
| LIVE 6 Nov (main d629a2939) | **LK161** "The scroll thing is still not fixed. I'm scrolling once on the mobile, and it's registering many swipes inside ... what's inside MockMob ... In general, there are many scrolling inconsistencies on the mobile." (desktop: "scrolling on the desktop feels very natural") |
| LIVE 6 Nov (main d629a2939) | **LK162** /pricing on a phone: Pro sits below Free. "Free or Pro should be a slider or something like that, and Pro should be the first option. People can slide up to Free and do the create account thing." |
| LIVE 6 Nov (main d629a2939) | **LK163** Exam "full screen mode on mobile: it should detect that it's mobile, and it should not make it horizontal." |
| LIVE 6 Nov (main d629a2939) | **LK164** The value slider "is a good direction, but it's a bit weird ... see how many other websites do this." Full mocks 190, Mistake Lab 190, chapter reviews 190 read as the same number; maybe "How many key cards will you practice?"; improve it. People must scroll to the bottom, not leave at the top. |
| LIVE 6 Nov (main d629a2939) | **LK165** Desktop pricing: the Pro card and "Everything your ₹99 covers" sit side by side and "both should be equally visible. Maybe you bring it up." |
| ANSWERED 6 Nov | **LK166** "Have you removed those keycards ... I don't see it." No: the preview has no KEY_CARDS_ENABLED (production-only env var), so it hides Key cards; live keeps them. |
| STANDING 6 Nov | **LK167** "Overall, it looks good." Improve scrolling in other sections too, especially on mobile; carry on with yesterday's open feedback (web and app). |
| LIVE 6 Nov (main d629a2939) | **LK168** Value card, final pass: compare ₹99 a month with how students usually pay (mock series ~₹500/subject, revision cards or books), not with our own credits; never multiply ₹99 by months; quick, low information. Shipped: subject steps 1-5, the usual way (₹500 + ₹250 a subject, marked typical) vs ₹99 a month, proportional bars. Iterate later. |
| DONE 7 Nov (main c267858d1; deploy verified separately) | **LK169** Speed: catching a fling on a story's edge costs one long frame (100-170 ms at 4x CPU; the price of the no-skip fix); make it cheaper. Outcome: the catch now only stops the fling and the held-story mark is set at rest (settle), so the restyle is off the catch frame; 22-swipe bench 8-10 frames over 100 ms before, 0-3 after, none in the scroll code. The strict "zero over 100 ms" gate is not met consistently on this PC (Round 4 baseline also 0-6). Not tested on a real Android emulator on the final build. |
| LIVE 7 Nov (main f30bb1059) | **LK170** Pricing marketing pass (his four picks): "as low as ₹1.10": "why not just make it ₹1 ... doesn't matter, that 10 paisa" (now About ₹1); Pro card and table name Mistake Lab, Mistake Repair and Ask Mobi, Key cards; value card says 10 to 30 papers. He thought Pro had 100 credits: it is 50 a month, the same as Free, all for Mobi on Pro. |
| LIVE 7 Nov (main 548f8804c) | **LK171** "The main thing that we would be bringing back from yesterday is ... ₹3,000 the usual way: ₹99 a month here. That line was removed, and we should add it back." "You can follow a maximalist approach, adding more things." |
| LIVE 7 Nov (main 548f8804c) | **LK172** "For 'How many CUET subjects are you taking?', the default should be 5 only, because 99% of students are taking 5 subjects." |
| LIVE 7 Nov (main 548f8804c) | **LK173** /pricing: "after 'Also in Pro', move the Free or Pro pricing section above the Free and Pro side by side. Below that, keep a more detailed value indicator than the homepage one ... more features and more convincing ways, so if someone is coming to a pricing page, they should not leave in any case ... then the comparison table." |
| LIVE 7 Nov (main 548f8804c) | **LK174** Pro plan listings: "you have highlighted the questions and 15 CUET subjects, you can highlight unlimited also, and keywords like that." |
| LIVE 7 Nov (main 548f8804c) | **LK175** Home pricing head: "Start free, Go Pro for unlimited mocks": copy fine, "formatting should be better, like center-aligned ... because it's a headline". "₹99 is about ₹3.30 a day ... fine, but all this text should not be just lying around randomly. It should be properly made." The Mobi note "No rush. Free stays free.": "many texts are just lying around randomly ... you can do something better." |
| LIVE 7 Nov (main 548f8804c) | **LK176** Landing: things that take space "can be collapsed into collapsible things, like the domain subjects, [the subject planner] and 'Which DU courses are open to you'. The domain subjects can be collapsed because we already have Quick start and Language." |
| LIVE 7 Nov (main 548f8804c) | **LK177** "We have 73 programmes. That section can also be made more useful, and some parts are repeated above" (the college cutoff cards repeat Compass). Pricing stays at the bottom: "first show every feature, then show the pricing." |
| STANDING 7 Nov | **LK178** "Your call ... small refinements you can do yourself, then show me the final product overall. We are at 95% right now, so one final push ... revisit the older feedback and double down on anything still not done." |


## R8 visible-craft pass, 8 Nov 2026 (brief recorded verbatim in AI OS handoff 20261107T201947.797018Z-c242d906)

| Status | Item |
|---|---|
| LIVE 8 Nov evening (main a017c2555); app 20 built | **R8-1** The 8 Nov brief: refine the website and app (thoughtful, tactile, confident, fast, finished), not a rebrand; keep the Keep list; the missed question carries through diagnosis, explanation, repair and next action; walk phone, tablet, desktop and the app; verify; "This prompt authorises local improvement work, not automatic production deployment." |
| DONE 8 Nov | **R8-2** "I'm going to sleep right now so just continue working. Keep noting down and compiling every change that you are making before and after all that and update me in the morning once everything is completely done" (running log + before/after report). |
| DONE 8 Nov | **R8-3** After the usage limit reset: "Please continue from where you left off." |
| DONE 8 Nov | **R8-4** "What's the update on everything? ... The API spend is almost $500. I want an update on what all is done, what's left, and what took so long." |
| DONE 8 Nov | **R8-5** "We can finish everything that is left ... I just need proper tangible visuals of before, after, what was done, and what was not done. Get all the remaining stuff completed in the next 30 mins." (R8-BEFORE-AFTER.html) |
| OPEN (owner) | **R8-6** Decisions: keycap vs pill primary key; Score Recovery on sale or hidden; "Repair Q42" vs "Fix it for good"; Day samples dark or Day; app swipe ratings; APP-11/14/20; hero r7 walk. |
| DONE 8 Nov | **R8-7** Preview links: "Can you give me a preview link or something by which I can see what exactly was done? Did you do it in the new hero section or the old one?" Old/new LAN servers and a 140-item guide. |
| DONE 8 Nov evening | **R8-8** "The main hero section that we made yesterday had to be finalized with the college logo, promo video ... along with the changes you did today. Merge both ... make the final landing page when you deploy it." Merged web/r7-hero; live on a017c2555. |
| DONE 8 Nov evening | **R8-9** Arena: "you have removed the texture ... the previous one looked better. This looks a bit cleaner also ... the color and the warmth ... make it a bit better." Warm hairline grid restored with the warm palette. Sidebar unchanged by R8 apart from labels. |
| ANSWERED 8 Nov evening | **R8-10** "The key cards and all of that are gone ... The Learn section, I think, is entirely gone." The LAN preview hides Learn without &study=on; R8 did not change Learn's nav or flags. Owner to confirm signed in on www. |
| DONE 8 Nov evening; upload OPEN (owner) | **R8-11** "Firstly, deploy the website with all the changes live, and then give me the app ... Start ASAP." Website live; app 1.0.22+20 in Desktop/MockMob-build-20. |

## Home page scroll on phones, 9 Nov 2026 (owner, pasted in chat)

| Status | Item |
|---|---|
| SETTLED by LK190 (10 Nov: FLOW is live on main 7c28f3ea7; the free prototype proto/phone-free-scroll 27b8da7ac was not merged) | **LK179** "Can you make a hero section with a revised scroll function? We don't like forcefully forcing people to scroll through the entire section. They can see if they want to ... what we have implemented right now would be irritating on a mobile phone. It could be okay on a desktop, but on a mobile phone, that full functionality stopping deliberately in some places would be frustrating or maybe lower the conversion rate ... let me know which is the best approach, and then make a prototype link which I can see on my phone." This reverses L-029 / LK69 / LK103 (held stories, one gesture one step) on phones. Prototype: nothing holds on phones or touch screens; Mistake Lab is a sideways row of four scene cards with its tabs; the statement scrubs with the scroll; the tour and Recovery Lab use their swipe/tap modes. Desktop with a mouse keeps the holds. Waits for his look on the phone. |

## Hero walkthrough film, 9 Nov 2026 (owner, pasted in chat)

| Status | Item |
|---|---|
| LIVE 9 Nov: r1 main dd8c63a7a, r2 polish main be44eafca | **LK180** "Right now, you have to work on the main walkthrough video of the platform and what we have to place on the main hero section of the website ... not much attention to the promo video. Similar assets and all can be used, just reframing everything to be more fit for a website hero section rather than a promo video ... make sure it is relevant for the entire website. Being at the hero section, it should be a highly converting video. If you need to make some changes to the hero section video player embedder ... you have the discretion." Done: Hero16 (67 s, muted-first, reading-pace holds, ten chapters incl. new Learn, Key cards and What you get), player bar under the picture with chapter jumps. |
| Applied in r1 | **LK181** "Think about the funnel. If a student is coming and visiting your website, it's not necessary that they are seeing the promo ... they have some sort of basic trust or knowledge of the company but they don't fully trust us yet to give their money to us. We have to build that trust and establish that we are the best and what all we offer instead of focusing on our first-time promotion." Applied: the logo intro cut; the film shows the full study loop and ends on a trust chapter (15 subjects behind 19 of every 20 CUET papers; ₹3,750 the usual way vs ₹99 a month, all six Pro features) before Sign up free. |
| Applied in r4 | **LK182** (9 Nov ~10:40 am, on r3) "the first 20 seconds ... very slow. Some are very fast, and the voice is not very human-like. Even the background music is a bit too loud, and it's not always in sync ... remove that 142 and all that kind of weird hook. Just come straight to the point ... a short walkthrough, walk around, plus a first impression ... add some on-screen effects because it will be muted usually ... reference the klayprep website". Applied: r4 52 s, new voice (Yash, his pick), no hook, montage opening, numbered features with muted effects, bed 18 dB under voice. Before that (LK182a, 9 Nov morning: "it should have a voice") r3 added narration. |
| Applied in r5 | **LK183** (9 Nov ~12:30 pm, on r4) "The first 5 seconds ... 'Preparing for CUET 27, college logo,' and all that was better ... something more new can be made. From 5 seconds to 10 seconds ... half-cut. Screenshots are just placed together. Better graphics ... In other places, quality feels a bit of a compromise ... Overall, it's good enough. Other: sound design ... the last 3-4 seconds, by making it end with a pop ... using the previous MockMob ending screen". Applied: r5 53 s live (main 1184acb84): richer open with a new iris exit, a staged product tour of whole devices for 5-10 s, whole devices in 02-07, the previous end card, one pop ending. |

## Homepage sample result, 9 Nov 2026 night (owner, pasted research prompt)

| Status | Item |
|---|---|
| LIVE 9 Nov ~11:30 pm (main 5dbcea349) on his "Yes, deploy it" | **LK184** "Make a small, visible polish pass on the public MockMob homepage, centred on the existing five-question demo ... try real CUET-style practice, understand an actual mistake and see what a full mock would add ... Stop with a local diff for review. Production release is a separate owner decision." Done: misses named Q2/Q4 + chapter, your answer beside the correct one, honest heading and next step, one line on what a full mock adds. Packet B (dock over the arrival) did not reproduce, so no change. Report: wt-1109-demo-result/tmp/1109-demo/report/index.html. |

## Conversion pass, 10 Nov 2026 about 1:40 am (owner, pasted in chat)

| Status | Item |
|---|---|
| LIVE-UNCHECKED 10 Nov ~4:30 am (main 7c28f3ea7, with round 10) | **LK185** "Load the UI Craft and Conversion mini-skills and the three video research notes from the AI OS brain. In one pass, walk the current MockMob website as a first-time CUET student, from arrival through the next meaningful action. Use the live experience and available funnel evidence to judge what feels generic, what makes the offer hard to trust, and where a willing student loses momentum. Choose and implement the improvements you judge most valuable ... Apply the research selectively and build on what already gives MockMob its character. This is a polish and conversion pass on the existing experience." Built: the sample's result carried to /signup; the phone theme note off the headline; the home page's funnel steps. Write-up: CONVERSION-PASS-2026-11-10.md. Live with round 10 (LK189); verified on www: the sample's 3 of 5 opens /signup. |
| CLOSED by LK189 (10 Nov: a hypothetical bar, not a measurement; definitions kept in CONVERSION-PASS-2026-11-10.md) | **LK186** "Our ambition is 10× conversion and a 50%+ rate. Define the conversion event, eligible audience, and baseline so those goals are comparable. Treat lift as a hypothesis until measured. Verify your changes on phone and desktop, then show what you changed, why you chose it, and how you'd measure the result." Event: finished sign-up; audience: signed-out home page loads; rate: signup_complete / landing_view by device kind over 14 days. Known today: 1,493 sign-ups last season, 61 since June; first set within 24 h of sign-up 48% last season, 36% since June; 6.7% of May sign-ups paid; no visitor data. |
| PARKED by LK189 (10 Nov: he does not want measurement; the switch stays off, the home page's calls answer 204) | **LK187** Turn on the visit and sign-up counter: FUNNEL_ENABLED=true in Vercel, then redeploy. It keeps step names only (no cookie, no id). Without it neither goal can be measured. |
| LIVE-UNCHECKED 10 Nov ~4:30 am (main 7c28f3ea7, dpl_6cJqMnU6b1AwqjBNna1FX1KJTGdt): five groups of sections refined in place, each looked at before and after at 390 and 1440, Day and Night; write-up ROUND-10-LANDING-2026-11-10.md; he looks on his phone and laptop | **LK189** (10 Nov ~2:40 am, on the pass above) "First of all, let me clarify that you don't need to see historic signups or anything else, or measure how many people are going to sign up, or calculate conversion rate from that. By 10x the conversion rate and 50% conversion rate, we meant that, in a sense, you can estimate and say hypothetically: because this is so good, or if it is targeted to an actual student, how likely is it to convert, just hypothetically, based on improvisation to the landing page? I think you have made some small, meaningful changes, but I think you can take it deeper and improvise a lot more. I'm treating this more as a UI/UX refinement and design taste refinement rather than focusing on signups and conversion rates, and treating them more as a byproduct. When you are satisfied with the overall landing page and everything, then you can commit the site and deploy it live." So: LK186/LK187 are not asks (no measuring, no counter decision needed); a deeper, visible taste refinement of the whole landing page; deploy on our own judgement when satisfied. |
| LIVE-UNCHECKED 10 Nov ~4:30 am (main 7c28f3ea7): FLOW on touch screens: the stage still pins and shows every step, the scroll is always the browser's own, a gentle swipe is one step, a flick passes several, one landing per story on its first fling; a mouse is unchanged. From the top to the plans on a phone: 31 ordinary flicks before, 19 now; 23 quick flicks before, 10 now. Not checked on a physical phone | **LK190** (10 Nov ~2:55 am; settles LK179) "Also, just remember, while you are trying to treat this somewhat as an overall final UX pass, to merge some things and make them better (like the scroll decision, which was pending on our side). Over that, find the balance of what could be the best solution, because I am conflicted on it, and overall, there is no single correct way to it, maybe. The issue is that if we remove scroll, we aren't able to really show the features to the people. If we keep the scroll, then it feels very locked in. People will just not scroll to the end of the pricing page. The goal is to make people scroll through the entire page and force them to scroll through the entire page somehow, without making it so forceful and so irritating that they leave the page because of the forced scrolling. We have to strike some balance or find some sort of solution to this. Try to solve this issue also if you can do it in this pass." |
| DECIDE (owner) | **LK188** Next levers found in the pass, not built: the first run after sign-up (about half of sign-ups never finish a set); a proof line beside the hero key (1,493 sign-ups last season is true, but it is his copy call after LK121); the free first full mock appears off on production; restoring a finished sample when a student comes back from /signup. |

## His look at round 10 on his phone, 10 Nov 2026 about 5 am (LK191-LK198; verbatim in ROUND-11-SPEC-2026-11-10.md, which also holds the decisions and the build spec)

| Status | Item |
|---|---|
| NOTED | **LK191** The scroll is now "how it was in our first version of this scroll test ... maybe this is the right approach" (flow stays; held is not coming back). |
| LIVE 10 Nov (main 79b9c49cb) | **LK192** "very inconsistent scrolling ... Even in normal scrolling ... it skips too much or too little of the content and unevenly skips the slides or the sections. This is especially evident in the [What's inside MockMob] stuff. You have to make it somehow consistent by maybe increasing the time of each, making it less jumpy now, not making it properly held because that takes away the smoothness". Flicks running on is "expected behavior". Decision: a normal swipe is exactly one step, a flick is free; longer steps. |
| LIVE 10 Nov (main 79b9c49cb) | **LK193** "why do we have two slides for the mistake repair lab or [score] recovery lab? I think it's the same feature and we have two sections on the landing page for it ... both can be merged into one only." |
| LIVE 10 Nov (main 79b9c49cb) | **LK194** "your typography looks good. Just use your marketing brain a bit more to finish up the things and make the things better on the overall website." On the phone it "looks like 90% the same ... I can notice some meaningful changes." |
| STANDING | **LK197** "All this I have seen on the phone only because that's where 100% of our conversions will take place ... people will first visit the website and use the phone only. That is our primary product." Judge and verify the phone first, always. |
| LIVE 10 Nov (main 79b9c49cb) | **LK195** NTA mode's "0/3 warnings" on the home page is not interactive ("The counter doesn't increase by doing anything. Not sure if we should keep it or remove it."). Decision: remove the counter, say the rule in words if the runner really does it. |
| LIVE 10 Nov (main 79b9c49cb) | **LK196** "the autoplay and story-style inside [MockMob] slides have gone but there is still the play/pause button. Either remove it or, if we are keeping it, then bring back that old UI that we had." Decision: remove the key; demos play once per arrival. |
| STANDING | **LK198** "After that I need a very finished product in every sense ... You have the authority to add or remove anything on the landing page. The goal is to make it the best for conversion and converting students into paying customers". Newer than "never cut" for the landing page: remove repeats, keep each feature's best demo once. |

## Signed-in phone UI, themes and consistency, 10 Nov 2026 about 3 pm (LK199-LK206; verbatim in HANDOFF-2026-11-10-APP-REFINE.md; prompt in PROMPT-2026-11-10-APP-REFINE.md)

| Status | Item |
|---|---|
| LIVE 10 Nov (main becb9055b); checked on the dev preview, not on live signed-in pages | **LK199** "refine the mobile UI after logging in, basically the practice arena UI/UX": placement and clarity on a phone; many passes have not got there. **Outcome:** every signed-in screen walked at 390 and 360, Night and Day, as a new and a returning student; refined, nothing rebuilt. Review (what a repair is before the first Repair key; a new student's Start key on the first screen at 360 x 640), Result (the four end links are one ruled list), Rules, Repair, /recovery (one heading, one key), Learn (the chapter page's sticky Start no longer cuts the In/Out switches), Explore, Ask Mobi (no boxes in boxes, one paused notice), Progress (first-week bar; the next step's key is the page's main key), You (name and email as lines with a Change key; password behind "Set a password"; credit history folded), Wallet ("Top-ups open soon" said once, the three greyed keys gone), My uploads, Radar, Rival (Start key on the first screen), Upload, the Pro line (one quiet line with a text link, D79), the first-time note (no accent bar). Today and Practice already kept their main key above the dock at 360 x 672; they got the calmer edges and Practice's chosen mode wears one ring. |
| LIVE 10 Nov (main becb9055b) | **LK200** Day and Night: "how to properly give them to the user"; the top switch "has been replaced with Ask [Mobi]"; the home page pop-up is gone on phones; Night "still gives kind of an AI slop vibe"; Day is weaker. **Outcome:** the Night/Day switch is back in the signed-in top bar at every width (phones: the "mo" mark, Ask Mobi, the switch, credits and the person; fits at 390, 360 and 320; the full wordmark does not fit beside it, so the logo shortens to the app's mark below 640 px). Appearance (Night, Daylight, Match device) stays in the account sheet and on You. Home and /pricing: the first-visit note is back on phones as one line under the switch, gone on the first scroll or press. Night: the volt outline token is a tinted hairline (0.5 to 0.28), lit cards keep their wash (G28), boxed and volt-edged rows became hairline lists (Mob settings, Rules, Result links, Learn, Progress, Compass sources). Day: the same, plus the result's figures on raised paper and Progress week bars that read at a glance. Targeted fixes, not a repaint: his eye decides whether Night and Day are there. |
| LIVE 10 Nov (main becb9055b); the den was checked on the dev preview only | **LK201** "refine each and every feature more, like the mob feature." **Outcome:** the Mob says what it is in one sentence; the key is one line ("Sit this week's paper") with its cost under it; a Mob of one leads with "Invite a friend"; Members ends in the invite row; Settings are plain rows; no Mob: the Start form follows the seats picture; in the den the Play key is on the first screen at 390 x 844 (the page title that repeated the tab is kept for screen readers on phones, the runs line sits under the key). Compass: says what it is for first; ticked subjects fold into one card with Edit; View courses lands on a course; every cutoff says its year and what it is. Learn, Ask Mobi, Review, Mistake Lab screens, Key cards inside Learn: see LK199. Not walked after the change: the Mob explainer, live and play screens, Today's Mob card, the Practice chip. |
| LIVE 10 Nov (main becb9055b) | **LK202** "In the profile pop-up the sign-out button is repeated." **Outcome:** Sign out is shown once in the shell: a clear row with its icon in the account pop-up (G29: easy to see). The top bar's own key is gone; the sheet steps back while "Sign out here?" is asked. The You page keeps its own. |
| LIVE 10 Nov (main becb9055b); frames checked in headless Chrome, not on a phone | **LK203** "The light/dark mode transition can be refined." **Outcome:** the new theme spreads from where the sun or moon lands, 680 ms with a gentle start and landing (it was 560 ms and covered half the screen in the first tenth of a second). The sun and moon thumb is unchanged (D10). Knobs: REVEAL_MS, REVEAL_EASE in ThemeToggle.jsx. |
| LIVE 10 Nov (main becb9055b) | **LK204** "The texture of the background on the hero section and overall landing page can be made a bit more defined." **Outcome:** the Arena's warm hairline grid (48 px, fixed, fading down the screen) behind the whole home page, and the hero's paper grain a third stronger in Day and a seventh in Night. No bubbles, dots or spotlight. Knobs: brand-texture.css `.mm-grid --grid-ink`, `--grain-hi`, `--grain-lo`. |
| LIVE 10 Nov (main becb9055b); W-097 (the visual upgrade) stays open | **LK205** /pricing "is already like a 9/10 but some areas can be improvised and a few things can be added." **Outcome:** "What happens when you get Pro" under the plan cards (pay, Pro turns on, renewal or "Nothing renews", who to write to); "Can I get a refund?" third in the questions (restates /refunds, starts with "No."); the hero copy centred inside the gutters with the price on the first screen at 360 x 640; a signed-out student who taps Get Pro returns to the plan after sign-in. Every added sentence has its source in a test (pricing_pay_steps_1110). **His to confirm:** the refund question on this page; "we reply within a day" here too; whether a parent may pay; whether website Pro works in the Android app; whether Rs 99 includes taxes; "until you cancel" against Razorpay's 24-payment plan. |
| LIVE 10 Nov (main becb9055b) | **LK206** Hero creator pictures: Garima first, Radhika second, Rahul third (hero only): "the first circle one is the most recognizable and it's not cut out, you have to think about such things yourself." **Outcome:** that order in the hero line only, and the first picture is drawn whole, on top. The Instagram section keeps biggest audience first. |
| STANDING | **LK207** Work-style instructions written for older models (sub-agents, specific ways of working, UI/UX procedures) do not apply to the newest model: "You are free to use your own thinking ... the entire codebase is yours." Weekly usage is no reason to stop (same day). |

## The app-refine pass, 10 Nov 2026 evening (LK208-LK211; his brief is PROMPT-2026-11-10-APP-REFINE.md; live main becb9055b)

| Status | Item |
|---|---|
| STANDING | **LK208** What an AI-generated look means to him: "neon edges, glow, gradient text, too many outlined boxes, everything the same weight". Night "is usually the better one"; Day "has had a lot of work and is still the weaker theme". Texture: "I like texture; I rejected the answer-sheet bubble pattern, and I liked the warm hairline grid in the arena". |
| STANDING | **LK209** "Nothing should be hidden or cut from the signed-in product without a good reason you tell me." Told in this pass: Wallet's three greyed "Top-ups open soon" keys (the sentence stays, once); the den's page title on phones (it repeated the tab; kept for screen readers); Compass's subject chips while the subjects card is folded (the card names them; Edit brings everything back); the full wordmark in the phone top bar (the "mo" mark; the switch needed the room). |
| STANDING | **LK210** "Truth is not negotiable: no numbers, claims, testimonials or features on any page that the code or data does not back. Copy is plain, sentence case, no exclamation marks, no emoji." Also: "Message me only when there is something to look at, a decision that is really mine, or a real risk. When you report, lead with what changed that I can see on my phone and where to look, then what is left, honestly." |
| NOTE | **LK211** A usage limit cut this pass in two (about 3:50 pm; "Try again" at 7:55 pm). Nothing was lost: sub-agents resume by id after the reset. |

- **Old rows looked at on the dev preview in this pass (not on live signed-in pages, so they stay as they are until he sees them):** D3 the Change plan sheet is a sentence the student fills in step by step, not a form: holds. D5 Practice shows "Review and repair" and "Ask Mobi what to practise" under Your papers: holds. D15 one action per mistake ("Repair" / "See repair" / "Check it held"): holds. D17 the answer bar fits the paper and "Play your paper back" is present: holds. F17 a repaired mistake opens its saved repair with its mock and 12-hour time: holds. W-051 the calculator's "New" tag is on the public nav. W-050 Compass is clearer but still lives under You with no dock tab. W-053 unchanged (D126 A keeps colleges first; his call). D19 badges: kept, not refined. M-007: the page cites four DU documents with no retrieval date; no figure was checked against the PDFs.
- **Left open, honestly:** a physical phone and iPhone Safari were not used; signed-in pages on production were not opened (no sign-in as him); the Mob explainer, live and play screens; Compass Pro's "Your colleges" still reads as a form; Rival's Start key shows twice on a phone; Free students get two practice cards back to back at the end of Compass; "course" and "programme" are mixed in Compass; the Ask Mobi page lights "You" in the dock (the 19 Oct nav option A); `test:mob` has 7 failing server-side tests and `test:study` 1, both with or without this change.

## His feedback on the app-refine pass, 10 Nov 2026 about 9:45 pm (LK212-LK224; dictated, some words mis-heard by the dictation and read in context)

| Status | Item |
|---|---|
| LIVE 10 Nov (main 7444fb291) | **LK212** The refund question on /pricing: "you can remove [it], but we have to place it somewhere. I think in the pricing support section ... don't start it with a 'no' ... In very, very extreme edge cases, we might consider a refund, but usually it's a 'no.' ... once payment has gone through, then 99 out of 99, they won't get refunded. Still, we can't just straight up say, 'No, in any circumstance' ... Play around with the words." **Outcome:** out of the questions; said once in the support line under the Pro timeline ("A payment is normally not refunded once it has gone through. If you were charged twice ... we check it against Razorpay's records"), with a link to /refunds. /refunds reworded in the same spirit ("Refunds on the website"; dated 10 November 2026). |
| LIVE 10 Nov (main 7444fb291) | **LK213** "What happens when you get Pro": "Those are good. Many apps do it to build trust. The only issue is it's just a wall of text. Maybe you can replace it with some sort of a graphic ... expand it into a free trial step if we ever plan to do that in the future, not right now." **Outcome:** a drawn timeline (three marks on a rail, one short line each, the detail under "More"), vertical on phones, a rail on desktop; the steps come from data (paySteps), so a first step can be added later. No trial is named. |
| LIVE 10 Nov (main 7444fb291) | **LK214** "In the pro section, there are three right now ... there is space for one more ... key cards or even something else". **Outcome:** "Also in Pro" has a fourth tile (Key cards while KEY_CARDS_ENABLED is on, otherwise DU Compass), four even tiles at every width. |
| LIVE 10 Nov (main 7444fb291) | **LK215** Onboarding, Accountancy: "it's showing the 2025 CUET paper asked for an analysis of financial statements only. How's that possible? ... CUET gives the option between both parts, so confirm it, and all subjects need to be updated according to that only." (Computer Science and Maths are right.) **Outcome:** he is right. The CUET (UG) 2026 Accountancy syllabus prints "Optional to Unit V: Computerised Accounting System" (data/CUET 2026/accountancy.pdf); the old line rested on one shift's reprint. The note now reads "The CUET syllabus gives Unit V two ways. Pick the one your school teaches." All 16 live subjects' 2026 syllabi were read again: only Mathematics, Computer Science and Accountancy carry a choice, as the app models. |
| OPEN | **LK216** Onboarding on the web "is not as polished as the app". Not started. |
| UI LIVE, COMMERCE PENDING 11 Nov (main 97192a222) | **LK217** "Wallet and all is still broken. We need to finish it up. There is no way to purchase anything, and also, overall, the UI is just falling off text." **Outcome** Activity, loading, error, zero, low, Pro and confirmed-purchase states are live. Selling is closed. The owner decides after a Razorpay Test Mode purchase on an isolated preview. Refund clawback for packs is open. |
| LIVE 10 Nov (main da4555622) | **LK218** "When someone clicks on a premium feature which needs Pro, then also the pop-up that comes can be a bit refined by adding some graphic". **Outcome:** the sheet names the feature, uses an existing MockMob desk object and shows the same price, terms and Get Pro action in a footer that stays visible when details scroll. |
| LIVE 10 Nov (main 755dd31fe) | **LK219** "add the functionality to add ... some sort of setting, avatar, or profile for the mob feature, and to provide the overall social layer, which is important. Refine this card, like 'Hi Atishay' and 'Free plan' ... Right now, it's 5 subjects: 3 on the top row, 2 centered on the bottom row. Take care of these kinds of things on your own and overall improve the [You] section." **Outcome** The card shows the saved name and initial, plan, balance linked to Wallet, aligned subject rows and the current Mob identity with the shared name and colour editor. |
| LIVE 10 Nov (main 7444fb291) | **LK220** The Night/Day toggle "between the Ask Mobi, the credits, and the profile: doesn't it feel a bit weirdly placed?" **Outcome:** agreed. On phones it now sits on the left beside the mark; the right side is Ask Mobi and the account. Desktop unchanged. |
| DESIGN FOR REVIEW 11 Nov | **LK221** "the top bar and the guide feature are just so, so, so bad. It should automatically start when someone is first-time entering the platform. Only implement it if you can properly fix it up and make it up to a very high standard and quality." **Outcome** Prototype has three anchored stops for Start, Practice and Ask Mobi. Owner review and an account-level first-visit mechanism are pending. The live guide is unchanged. |
| LIVE 10 Nov (main 7444fb291) | **LK222** Ways to practise: the "360 green light which goes around" a chosen mode "feels a bit weird and incomplete". **Outcome:** the ring no longer travels round the card; it settles in as one piece (200 ms). Fine-tune: "even when tapping on the other modes, it should just show that pro pop-up." **Outcome:** a Free student tapping Easy, Medium or Hard gets the Pro sheet. |
| LIVE 10 Nov (main 4461487f5) | **LK223** The home page's sample: "when you ... select another subject, it takes like 5 seconds to load. Make sure there is a proper loading animation." The sample questions "should be the highest-quality questions ... the repeated [CUET] questions so that ... we can also show something like 'Was asked in [CUET 20xx]' or 'Previous year similar question'." Quality here means "relevance to [CUET] and the syllabus", not difficulty. Rule for the build: an "asked in" label only where a stored field says so for that exact question. **Outcome** The chosen subject and four answer placeholders show while loading. Accepted alternate sets are cached and the sample favours eligible, higher-quality questions across chapters. Exact and adapted past-paper labels require signed provenance and a verified source year. |
| STANDING | **LK224** "Overall, I want you to think outside the feedback that I'm giving and make good changes yourself. The codebase is yours, and you have the autonomy to make good, meaningful changes and then report it to me." |

## 11 Nov 2026, about 1:29 am IST: the guide and web onboarding (main 230de48e8); review of the other session's four releases

| Status | Item |
|---|---|
| LIVE 11 Nov (main 230de48e8); seen only on the dev preview | **LK221 outcome:** the guide is rebuilt: six short stops (Today, Practice, Start, Ask Mobi, Your Mob while it is on, You), one spotlight in the target's own shape, a card with Mobi that never covers its target, Back, Next, Skip, Escape. It starts by itself once for a student who finished onboarding on this device in the last 24 hours, on Today or Practice (onboarding ends on Practice), never over a paper, a sheet or the Pro sheet. The Learn, Your papers, Progress, Colleges and Guide stops left the tour (not the product). Not account-wide: a student who onboarded in the Android app or in a private window gets no auto-start. |
| LIVE 11 Nov (main 230de48e8); seen only on the dev preview | **LK216 outcome:** onboarding polish: the main key stays at the bottom edge on every step, picked subjects are a soft fill with a tick, no card inside a card, an odd last tile fills its row, the last key reads "Finish and open Practice". Open: the keyboard lift needs a look on a real phone; laptop width not walked; not compared screen by screen with the Android app. |
| NOTE | The other session's releases (LK218 Pro sheet, LK219 You card and Mob profile, LK223 home sample, LK217 Wallet states; main 97192a222) were looked at again at 390 and 360 in Night and Day and hold. The owner said the sample's loading state is fine. Still unmeasured: the sample's real response time and question quality per subject; no question has a verified past-paper label. Wallet selling stays closed (his decision after a test payment). |

## His brief for the final pass, 12 Nov 2026 about 7:15 pm (LK225-LK230; dictated, read in context)

| Status | Item |
|---|---|
| STANDING | **LK225** "run one final pass for both the website and the app, focusing on: improvising the hero section of the website and the overall landing page and experiences in the arena, wherever you can, on both mobile and desktop; the landing page: the priority should be more mobile ... You don't have to just go through everything and vaguely improvise it. See the side, and if you identify any weak points, then fix them. Points which are already liked by everyone and you think are good: no need to change that. This is not a 100% complete redesign of your whole website. This is an improvement on whatever can be improved to make it a more converting site". |
| LIVE 12 Nov (main 766eb6da9) | **LK226** Home page and hero. **Outcome:** walked top to bottom at 390 and 360 (Night and Day, the Day theme being what a first visit gets), at 1440, a first visit timed (the hero is up within 0.6 s on the local build), the sign-up page, and the film frame by frame against today's site (its "Pro ₹99 a month", "15 subjects, 19 of every 20 CUET papers" and "four friends" all match production). One real fault found and fixed: on a phone the last slide of "More inside MockMob" (the Mob) ran 43 px past the right edge and cut its text; its "Up next" now says "Key cards". The hero itself, the sample, the Lab, the plans and the close were left as they are: nothing there was weak enough to change for the sake of changing (LK121 keeps facts out of the hero; the "Sound on" key stays because the film is narrated). |
| LIVE 12 Nov (main 766eb6da9) | **LK227** "the inside platform (the arena practice, whatever you call it): for desktop, there should be variety, and this should be conveyed. I don't know if you have implemented this type of thing better on desktop, but those sorts of things should be implemented." (Read as: the signed-in product must be made for desktop too, not a phone layout stretched; "variety" may be a mis-heard "parity".) **Outcome:** every signed-in page seen at 1440, 1366 and 1920. Most already use two columns (Today, Practice, You, Your papers, Marks trend, Colleges, Ask Mobi). Fixed: Learn and Key cards sat 65 and 100 px right of every other page's left edge (now one edge); the Mob's roster and settings sit side by side from 1100 px (production runs the den, Mob v3); starting a practice set no longer fires a success toast over the Start key before any session exists. Not seen on desktop: the test-taking screen itself (the local preview cannot open a paper). |
| BUILT 12 Nov (1.0.23+21, c79dac51c) | **LK228** "For the app, it's already at a very good level, but ... from the onboarding to the inside experience ... it can take a bit more finish and refinement ... what you can improvise from a fresh perspective". **Outcome:** 117 fresh emulator shots of the signed-in app (Night and Day) read one by one, plus the onboarding reference renders. Five finishing touches: the band under the bottom bar now closes (a row scrolling past was readable there as a line cut in half, on every tab); the account sheet says "Credits" once, with the balance lined up under it and no empty band (the "Saved 9:14 PM" line now sits at the end of the caption's line); the opening screen's lamp light runs to the top edge (a flat dark strip behind the status bar ended in a hard edge); the welcome screen no longer ends in a black strip (it asked for an opaque black navigation bar; found on the release build); the Privacy row opens a page called Privacy (it was "Usage data"). The onboarding steps themselves were left as they are. Checked: flutter analyze clean; unit folders account_sheet, core/router, core_ui, credits, a11y, you, today (1,460), test/widget (365) and the welcome tests (74) pass; 130 reference images re-recorded and their suites pass (324); the bundle and the APK carry the upload key (SHA-256 62:AC:58:08...EC:47) and pass the 16 KB check; on the emulator, the signed-in screens in the demo build (Night and Day) and the release build itself, installed over version 16: opening screen, welcome, the class, course and college steps. Not checked: a physical phone; a sign-in in the release build; the first-run flow after the college step on a device; the whole unit and golden folders in one run (old drift remains in the credits, start sheet, art scenes, today_resume and share-card reference images; the credits ones fail without these changes too). |
| DONE (no change) | **LK229** "If you want, you can also make changes to the main video in the hero section ... they need to be done by Fable only. Don't spawn any subagents for it." **Outcome:** watched every two seconds of the 53 s film; its claims match the live site and its screens still match the product. No change made. A portrait cut for phones (the film is 350 px wide there) would be the one real gain; it is a re-layout of all its chapters, a job of its own, his to ask for. Asked the same evening; his answer: "Not now". Do not raise it again unless he does. |
| STANDING | **LK230** "In other places, if you are doing some bug fixes and minor adjustments here and there ... you can spawn cheaper Sonnet agents." Used so: one Sonnet helper took the emulator screenshots, one brought the app's tests and reference images in line; the design decisions and edits were the main session's. |
| STANDING | **LK231** (12 Nov, about 9:40 pm, after the final pass) "Did you make any major, meaningful changes, or just small things ... I don't see any major changes as such on the landing page, hero section, or anything." Answer given: no, small fixes only; most of the time went on looking. Then: "just log everything and your findings ... no other agent has to spend this kind of time looking and already finding the things which you have already found or which you think don't need to be changed ... Log all of this in the brain, keep it updated". **Outcome:** `UI-AUDIT-LOG.md` (what was looked at, verdict per surface, fixes, open candidates, the fast way to capture). Every agent reads it before UI work and adds to it. The open candidates for visible change are listed there, section 5; none is started. |

## His brief for the motion pass, 12 Nov 2026 about 11:25 pm (LK232-LK236; dictated, pasted as one note)

Verbatim: "What I want you to do right now is do a controlled pass on the entire animations and UX part of the landing page. You just have to focus on: improving the animations and the flows; reducing the ice block; integrating the mobi using scroll graph properly; maybe using him as a bot that we can build on the home page and include it as part of a free trial without signup. Something like that."

Transcription guesses, both to confirm with him: "ice block" was read as "AI slop"; "scroll graph" as "scroll-craft", the skill in `Desktop/mockmob copy/scroll-craft-main` (its ideas were used: the scroll as the timeline, depth from planes that move differently, one character threading the page; its build pipeline was not, because it is for new pages).

| Status | Item |
|---|---|
| LIVE 13 Nov (main a218cb9a4) | **LK232** "improving the animations and the flows". **Outcome:** a helper read every animation on the home page (26 findings, `wt-1110-convert/tmp/1113-motion/AUDIT.md`); the ones felt on a phone were fixed. Section headings no longer blur in over 0.8 s (a 10 px rise in 0.32 s); a block starts when its top edge is seen. Mistake Lab scenes no longer cross through each other on a swipe. On the sample: a press dips the option, the answer lands without the old 3 px hop, Mobi's bubble never shows two lines at once, and the next question arrives as the next of five. Press states for the tour chips, pricing steps, Compass keys, FAQ rows and shelf links; the Key card turns in 0.48 s; the phone menu's sign-up keys land by 0.41 s (were 0.64 s). Not changed: the step and gesture logic of the held stories, the hero film, the college strip's own motion (his design of 7 Nov), any section's content or order. |
| LIVE 13 Nov (main a218cb9a4) | **LK233** "reducing the ice block" (read as AI slop). **Outcome:** in motion, the generated-page tells were the blur-in headings, slow uniform fade-ups, hovers that stick on touch and taps with no answer; all fixed under LK232. No new gradient, glow, glass or floating element was added. Left as his own choices: the two college marquees, the one floating lit object, the Wall's drift. |
| LIVE 13 Nov (main a218cb9a4) | **LK234** "integrating the mobi using scroll graph properly" (read as scroll-craft). **Outcome:** (1) on phones the logo's Mobi stands on the current step of the bottom bar in the Mistake Lab and "More inside MockMob" and hops to the next step as the story moves; (2) in "Try five CUET questions" the painted room settles back while Mobi comes forward and his bubble arrives last, driven by the scroll (CSS view timeline; a plain scene on browsers without it and under Reduce motion). Considered and not built: Mobi inside the statement section (the phone layout there is full; he would cover text or the subject objects). The seats' hop-in and the desktop lane Mobi are as they were, except that the desktop one now fades instead of popping. |
| LIVE 13 Nov (main a218cb9a4) | **LK235** "maybe using him as a bot that we can build on the home page and include it as part of a free trial without signup". **Outcome:** after the five sample questions the result has "Ask Mobi what to do tonight": one clear step worked out from those five answers (the chapter with the most misses, or a full mock after five of five), with two follow-ups ("Why that one?", "And after that?"). It runs in the browser with no AI model, no network and no cost, and its last line says what it is ("That is Ask Mobi with five answers to go on. After a mock he reads your whole record."). The section's sub-line now reads "Get your score, with every miss explained. Then ask Mobi what to do tonight." |
| OPEN, his decision | **LK236** A Mobi that answers typed questions from visitors who have not signed up needs a paid model, and the rule is that no paid model runs outside its budget guard; the guard is per signed-in student (AGENTS.md). It needs his yes on a guest budget (a monthly cap for all guests together, a few questions per visitor) and a database change for the CTO. Not built. **Decided by him 13 Nov, see LK238.** |

## His look at round 13 and the round 14 brief, 13 Nov 2026 about 12:20 to 12:30 am (LK237-LK241; dictated)

Verbatim, first message: "I'm unable to see many of the things that you are saying that you did, because only one change out of the many that you are saying I can see: just this small Mobi icon hopping when I'm scrolling through sections. It's a small, nice touch, but Mobi is still not scrolling or interactive, and many inaccurate depictions are still there. I don't know what you have done for the AI flop check or look ... I don't see the Asmo feature anywhere on the home screen, sign-up screen, or anywhere ... Overall, the entire landing page looks the same to me." ("AI flop" = AI slop, "Asmo" = Ask Mobi; "inaccurate depictions" was asked about and not yet answered: confirm which.)

Verbatim, second message: "I saw what you have done with the Asmo. I don't know if this is a pre-trained algorithm. I don't think these are making real API calls after the five questions. What I want is the full version implemented. You are right to consider the budget part ... Maybe think like ₹1 per user or something like that, at max. That's the upper limit capping. Or even cap it to ₹0.5 per visitor and make it useful, or think how you could implement it better. I don't want you to think again and again. Right now, go on to the building part. You have only 2 hours to go all out on the landing page and improvise it however you can. Don't start looking again or reading stuff again. If you have found anything, then just take action on that. Nothing else. Whatever you are implementing, don't make it cluttered. Implement it tastefully only. Whether it's the ask movie at the front, the visuals flop pass, or the scroll companion on phone, it should be thoughtful and elegant. Start now. Only review once you have completed all the criteria that I mentioned, and you can score at least above an 8 on all these criteria."

| Status | Item |
|---|---|
| STANDING | **LK237** Round 13 read to him as "the entire landing page looks the same": timing changes are not visible change. A pass he asks for must show on his phone within the first screens. Build first, look at the end; do not spend the time reading and looking. |
| LIVE 13 Nov (main 38a09a4e7) | **LK238** The full Ask Mobi for visitors who have not signed up, with real model calls. **Budget, his words:** ₹1 a visitor is the upper limit; aim for ₹0.5 a visitor. |
| LIVE 13 Nov (main 38a09a4e7) | **LK239** Ask Mobi "at the front": reachable from the home page without answering the five questions. |
| LIVE 13 Nov (main 38a09a4e7) | **LK240** Mobi as a scroll companion on phones, "thoughtful and elegant", not cluttered. This lifts the earlier rule that the phone bar carries no Mobi (W-074 stays as "one Mobi in view"). |
| LIVE 13 Nov (main 38a09a4e7) | **LK241** The visual slop pass ("visuals flop pass"): the page must look visibly more deliberate; tasteful, no clutter. Self-review bar: 8 of 10 or more on each of his criteria before it is called done. |

## The production pass before marketing, 15 Nov 2026 (11:45 am and about 7:15 pm; record in PRODUCTION-PASS-2026-11-15.md, handoffs HANDOFF-2026-11-15-PRODUCTION-PASS.md and HANDOFF-2026-11-15-NIGHT.md)

Verbatim, about 7:15 pm: "Focus more on building and building more things, and thinking about just the ideas to build more. Rather than just doing an audit and thinking long on smaller things and refinements ... it is build-focused and production-focused. Keep building things and improvising them ... tangible, actual results, not small refinements." "You can think for yourself what's useful, what's not, and apply everything. Push it to live. Then we'll come back to the pending decisions."

| Status | Item |
|---|---|
| STANDING | **LK242** The final pass before marketing is a build pass: new, visible things, shipped live; no long audits; decide small product questions; one running list of what waits on him; every update lists every plan item with its status. |
| LIVE 15 Nov (main 79ff0d94e) | **LK243** The Daily Five as a habit (account record from server-checked answers, a study day, the Mob's rows, the public bar, how everyone did from 30). |
| LIVE 15 Nov (main 79ff0d94e) | **LK244** The Sunday Mock, free, one sitting a subject a week, no ranking line (his decision pending); first on 22 Nov. |
| LIVE 15 Nov (main 12516f20f) | **LK245** DU cutoff pages per course and college, checked against DU's PDFs. |
| BUILT, OFF (waits on him) | **LK246** Welcome and day-2 emails: his consent line, the migration, the privacy page, then the switch. |
| BUILT, HELD | **LK247** First paint (cascade check) and late upload with the durable start fix (no rewards for late papers first). |
| LIVE 16 Nov (main acc95ac67) | **LK247** First paint shipped, live page identical to the baseline; late papers shipped 15 Nov night (6858ccef5). |
| STANDING 16 Nov | **LK248** His words: "what you are building is still not up to the mark ... think in a unique brand identity direction ... this space is a bit low". A feature on the landing gets a large block in MockMob's own identity (paper, ink, volt, the desk), never a thin quiet row; do not copy a rival (Prepium shown as a reference only; he calls its UI and ours "AI sloppy"). |
| STANDING 16 Nov | **LK249** "A highly converting website is very important in every sense"; every feature thought through for how it is presented, how it works and its whole flow; "not always taking the safest approach, is usually the best approach". |
| STANDING 16 Nov | **LK250** "Make sure that it's very clearly depicted: what it is exactly and how we do it every time": each recurring thing states its rhythm in plain words (a new five every day at 12:00 am; the Sunday Mock every Sunday 10:00 am to 10:00 pm). "Keep going until you attain perfection." |
| LIVE 16 Nov (main 15286120f), he approved the direction ("Yes, that's what I want") | **LK251** The Daily Five as a calendar page on the home page, the Sunday Mock page under it, `/daily` rebuilt with the same day band. His first point of 16 Nov ("not placed correctly as a proper clock ... the entire UI and flow around it is very bad"). |
| LIVE 16 Nov (main 844e608fe) | **LK252** His second point: a top progress bar (built two ways: a route bar on every page, and a reading line on the home bar; he can drop either), the opening shorter and smaller, the shell and sign-in waits redrawn. |
| LIVE 16 Nov (main 844e608fe) | **LK253** Public Key card decks per chapter at `/key-cards` (the Free taste of 5 a chapter; 183 chapters). |
| LIVE 16 Nov (main 844e608fe), never run with a real model call | **LK254** Bring a mistake from any test, in Ask Mobi, 1 credit. His decision: the distress pre-check fires on real exam text about suicide in the pasted question. |
| LIVE 16 Nov (main 91f8f8aaf) | **LK256** Badges refined: one family of stamped marks, the earning moment, share, the collection in four rows; names and rules unchanged; the new "what it needs" lines are his to read. |
| LIVE 16 Nov (main e137d3575) | **LK255** Desktop two-column Wallet, Progress and result from 1100 px, with a tablet walk (phones unchanged). NOT STARTED: Mob class leagues, corrections log, durable-sessions SQL, Next 16.3.8. |
| LIVE 16 Nov (main aecaf31c5) | **LK257** Home Key cards: "Pick your subject and turn a real chapter's cards. No account.", 14 subjects. NEXT in his direction: the rest of the landing feature by feature (`HANDOFF-2026-11-16.md`). |
| LIVE 16 Nov (main 329e257ba), migration UNAPPLIED (CTO) | **LK258** The free first Full mock's release race for durable sessions, reviewed; two narrow cases left for the CTO before the switch. |
| STANDING 16 Nov, 10:20 am | **LK259** "No need to stop for handover or anything. You stopped 7 hours ago ... Continue everything ... only stop when you think everything has been finalized, and then report to me that everything is done now." Keep building through the usage window; handoff in passing. |
| LIVE 16 Nov (main 05510626d) | **LK260** Bring a mistake on the home page (a paper slip, Mobi's read on ink, a check answerable in place). |
| LIVE 16 Nov (main f5f6774c5) | **LK261** The Sunday Mock page's day band; a guest's Daily Five carried to the account on sign-up; the corrections log, UNLISTED until he reads it (his decision to list). |
| LIVE 16 Nov (main b42dd5bb4) | **LK262** The first minute after sign-up: a new student lands on the page they signed up for; the last race cases (migration 20261116130000 unapplied, CTO). |
| LIVE, OFF 16 Nov (main a6ab71edc) | **LK263** Mob class leagues behind `CLASS_LEAGUES_ENABLED`; SQL unapplied. His: turn on, and the floor of five against fake accounts. |
| DONE 16 Nov | **LK264** His words: "keep optimizing the PC side by side. The storage is running low ... terminals continuously popping in and out for about 1 minute ... makes the PC unusable". Fixed at the source (hidden console for six background jobs); 17 GB freed; two large folders wait on his yes. |
| LIVE 16 Nov (main 79672593c) | **LK265** Next.js 16.3.8, chart.js removed. The build list of 15-16 Nov is finished; what remains waits on him (decisions and SQL). |

## His look at the live site on his phone, 16 Nov 2026 about 5:45 pm (LK266-LK274; typed)

His words, whole:

> I have checked the new site live. Everything which is live right now on the landing page, particularly, looks good on the desktop page but falls short on the mobile page.
> * The Sunday mocks are consuming too much vertical space on the home page. I don't know if they should be just below the hero section as it is not a very important or useful feature.
> * "Number 2" is written on the Daily 5. What exactly does it mean? Overall I don't understand what you have built in Today's 5. You have mentioned English in general but when I click on Continue Today's 5, I think there are English and CAT questions only. Never mind. This is not a very useful feature. I don't think this is the way it is implemented but anyway if you want to keep it, you can keep it. It's nice to have but it should not be at the top. It can be somewhere else.
> * "Got 1 wrong" in another test: this section is broken both on desktop and mobile as the overall placement is very weird. I don't know if we properly have this functionality on our AskMobi chatbot: uploading pictures of any other paper, its capability of integrating it and providing some other value, simply uploading it to ChatGPT, how many credits it would cost, pricing it properly, and all that kind of stuff.
> * The scrolling of MockMob and its actions, what it is doing: it needs to be interactive and overall fixed in general.
> * It's fine. I would say up to the Practice Exam section, up to that section, is competent. After that, it's doing weird movements, and the overall scroll needs to be better.
> * These are some of the things which I have mentioned. Overall, I think there are many more improvements that you can introduce to this also, in all the aspects of the landing page. Do a final pass, and then let's see what you build. Don't use obviously AI slop elements like fonts or flashing, pulsing dots, that kind of stuff. You know what slop is and what good UI looks like, and it's different. Work it in that way, and each screen should be built with high effort and thoughtfully, like how the mocks work. It should have a proper explanation, not just walls of text, and that is also not properly lined.
>
> I don't know why I have this result. It is way below expectation, and I don't exactly know why this happened, but this won't cut it. We need major improvisations still. Remember, the codebase is yours. Feel free to make any changes that you like, so don't be hesitant on that part or keep asking me stuff.

How it was read (the readings are mine, not his): "CAT" is the General Test (GAT). "The scrolling of MockMob and its actions" is the phone scroll companion, Mobi (LK240), and the "More inside MockMob" tour. "Up to the Practice Exam section" is the tour's first tool (Practice, an exam screen); from its second tool on the held scroll swapped screens under a still page. "How the mocks work ... walls of text" is the Sunday Mock page's "How it works" (six headings over six paragraphs), reached from "See how the Sunday Mock works".

| Status | Item |
|---|---|
| STANDING | **LK266** Desktop is fine; the phone is where the landing falls short. A pass is judged on his phone. |
| LIVE 16 Nov (main 516bc9511) | **LK267** Daily Five and Sunday Mock: not under the hero, far smaller. Two short rows in their own section after the exam screen (about 535 px at 390, from about 1,500). |
| LIVE 16 Nov (main 516bc9511) | **LK268** "Number 2" removed everywhere (home, Today's row, /daily). /daily and the home row say the five come from English and the General Test, the same five for everyone. |
| LIVE 16 Nov (main 516bc9511) | **LK269** "Got one wrong in another test?" rebuilt: one card walked through in three steps (your question, Mobi's read, a check), words on one left edge, 956 px at 390 from about 1,700. |
| LIVE 16 Nov (main 67146f994), never run against a real model | **LK270** Ask Mobi reads a PHOTO of a question (until now typed text only), priced (a photo 2 credits, typed 1), names the chapter from MockMob's own list and opens practice on it. Never run against a real model by an agent: his to try once. |
| LIVE 16 Nov (main 516bc9511) | **LK271** The scrolling Mobi: stands only on the bottom bar, no lean, stretch or hop, and a tap opens Ask Mobi with a question about the section in view. |
| LIVE 16 Nov (main 516bc9511) | **LK272** The tour on phones: a plain stack of the five tools (no held scroll after Practice), and every screen answers a tap. |
| LIVE 16 Nov (main 516bc9511) | **LK273** Things that moved by themselves or by accident on a phone: the Compass score no longer runs by itself on touch; a thumb scrolling across a slider no longer sets it. Compass head starts on the page's left edge; Key cards shows six subject chips and a count. |
| LIVE 16 Nov (main 516bc9511) | **LK274** The Sunday Mock page's "How it works": the paper as three figures and the day as a timeline, from the rule's own constants. |
| STANDING | **LK275** "The codebase is yours. Feel free to make any changes that you like, so don't be hesitant on that part or keep asking me stuff." No pulsing or flashing dots, no slop fonts; explain a feature with a designed screen, never a wall of text, and line the words up. |
| OPEN, his decision | **LK276** Ask Mobi pricing on Free: a typed mistake costs 1 credit and a photo 2, but at expected model costs the Rs 2.50 monthly AI cap ends a Free month after about 31 typed or 22 photo asks, before the 50 credits are spent. Leave it, raise the Free cap, or price typed 2 and photo 3. |
| HIS TO DO | **LK277** Try one photo of a question in Ask Mobi from his own account (2 credits; a failed reply uses none). It is the first real photo call; the receipt then shows the true image cost against the reservation. |

## His second look on his phone, 16 Nov 2026 about 10:25 pm (LK278-LK289; part pasted dictation, part typed)

His words, whole. The first part came as pasted dictation:

> I'll give you feedback one by one on what works and what doesn't.
>
> 1. More inside MockMob: I have you spread everything into different sections vertically. The vertical space on mobile is already full, and it's just a wastage of vertical space. I think the older one was better, or I don't think this would work.
> 2. Keycard is fine, and this is also fine.
> 3. Pick your subject.
> 4. This Ask Mobi thing went wrong in another test. I think you had some older type version, and the copywriting on that was, I think, better. It had something like "in your other coaching school" or something like that, or another question was wrong. The student should feel that it is readable.
> 5. Your question, "Mobbies read," is right now doing a good job, but it's not good enough. It's rated 5 and 10 out of 10 right now. It could be more descriptive of what exactly is needed and what value we are providing them over any other thing. That should be clear.
> 6. This 5-day one paper on Sunday also needs to be improved. This is looking like a very small subsection, not something important or a major part of the platform, and it is also tucked away and hidden. If you understand what I'm saying, the visual hierarchy is not here completely, and the overall UI should be better. I'll just show you how ours look versus how Prepium's look. The Prepium one is also not perfect because it's consuming a bit too much vertical space on the phone, but it's still better than our implementation.
> 7. I would just say the Mobi image generations and animations can be improved. We can use the image generator to generate any new animations, or Blender, or whatever you like. Overall, some of that stuff also can be improved.
>
> Read this as one ultimate final pass of the landing page. Improve whatever you can on the site and anywhere else.
>
> Lastly, coming to the pricing question, if you could, just fit everything within our budget and price things according to it. I think the current 50 free credits that we give, for that, we had capped it to no more than ₹2.05 in monthly API usage.
>
> 1. Increase it to ₹3.5, incidental only.
> 2. Just see if, in all the use cases that we are thinking of, that budget in the 50 credits is sufficient or not, and apply things according to that.

Then typed:

> Then, coming on to the testing AskMobie, I don't see any way to upload a photo here. This is just such bad UI in the AskMobie thing. I'm not even going to try it, but let me just add a random image just for the sake of it, because I've never seen poor UI.
>
> Just then, this is an AI chatbot. It should feel like a proper AI agent with a ChatGPT or any Claude-like interface, but even better than that.
>
> But it should not be written that we are sending calls to. Not for the sake of hiding it, but any company who is making their own chatbot should mention this if they are using the API, right? We are not required to mention such kinds of things either.
>
> Keep the look professional, clean, and beautifully made, and it should feel like more than a chatbot and assistant, but still have all the functionality and UI of a proper chatbot.
> Now my question is: I uploaded a random photo, and it just showed that this doesn't look like a question from a test, so that's okay, not an issue. That's the correct intentional behavior, but again, it took away the bad user. Leaving that also, if someone keeps spamming random photos, I think this still counts as a call to the API route. I don't know if it costs us credits. It must cost something to create if it's doing a call. It's nigh worthless, but it's costing something, and I don't think we are deducting any credits. We are not deducting any credits, so I think this is kind of a loophole.
>
> Overall, this also needs to be thought through more in terms of how to build this properly. Also, make sure the Sunday mark on the top is not showing in the practice section. That should only be done if the date is Saturday, just the Sunday before, marked as a reminder of some sort.

How it was read (the readings are mine, not his). No picture arrived with the message, so "how ours look versus how Prepium's look" was read from Prepium's live page at phone size (its weekly-dose cards: a coloured band with LIVE NOW and a large date, then the name, three chips and a full-width key; about 390 px each). "The older one" for the tour is the one held stage of before 3891f2ace; its self-playing demos and moving chip row are taken as the "weird movements" of the 5:45 pm note, the held stage itself as what he liked. "₹2.05" is the Rs 2.50 Free cap. "Incidental only" is read as: raise it to Rs 3.50 and no further. "The Sunday mark on the top ... in the practice section" is the Sunday Mock line under Practice's heading (`SundayPracticeRow`); read as: show it on Saturday as a reminder, and on Sunday while the paper can still be started, on no other day. "It should not be written that we are sending calls to": no provider is named in the product's own screens; the privacy page keeps naming who processes a photo.

| Status | Item |
|---|---|
| LIVE 17 Nov about 1:03 am (main 3511f1fb3) | **LK278** The tour on phones: the vertical stack wastes the screen; "the older one was better". Back to one held stage, screens still answer a tap, nothing plays by itself. Outcome: one held stage on phones again, five still tabs, every screen answers a tap, the browser's own scroll; nothing plays by itself. In the 390 walk each ordinary swipe moved one tool. |
| NO CHANGE | **LK279** Key cards and "Pick your subject" are fine. |
| LIVE 17 Nov about 1:03 am (main 3511f1fb3) | **LK280** "Got one wrong in another test?": the older copy read better (it named the coaching sheet, the school paper, the book). A student should find it readable. Outcome: the older concrete copy is back ("a question from your coaching sheet, your school paper or a book"). |
| LIVE 17 Nov about 1:03 am (main 3511f1fb3) | **LK281** The three-step card (your question, Mobi's read, check) is "5 out of 10": say what the student has to bring and what MockMob gives that any other tool does not. Outcome: four steps (Question, Read, Check, Practise) and "What you leave with": the CUET chapter, your slip, 2 checks, 10 more from MockMob's bank on that chapter; the price line under the key. |
| LIVE 17 Nov about 1:03 am (main 3511f1fb3) | **LK282** "Five a day. One paper a Sunday." is too small, tucked away, no visual hierarchy; it must read as a major part of the platform. Prepium's cards are better but too tall. Outcome: a main block with its own stamp and a big head, a week rail, today's card on ink with its clock and key, the Sunday card; 811 px at 390 (Prepium-like weight without its height). |
| PART LIVE 17 Nov about 1:03 am (main 3511f1fb3) | **LK283** Mobi's pictures and animations can be better; the image generator, Blender, anything may be used. Outcome: in the app's Ask Mobi, seven clean Mobi poses, a six-frame wave on the chat's start, reading stills while he works. NOT done: the home page's Mobi (the vector figure, kept by the 4 Nov decision) has no new art or animation; the phone companion only got the rule that he never covers words. |
| STANDING | **LK284** "Read this as one ultimate final pass of the landing page. Improve whatever you can on the site and anywhere else." |
| LIVE 17 Nov about 1:03 am (main 3511f1fb3) | **LK285** Pricing: raise the Free monthly AI cap from Rs 2.50 to Rs 3.50, check every AI use fits the 50 credits inside it, and price accordingly. Closes LK276. Outcome: Free cap Rs 3.50 (USD 0.0398; the owner ran the SQL, read back). Every Mobi use fits inside a Free credit's Rs 0.07, so no price changes; the working is in src/services/mobi/mistakePrices.mjs. Closes LK276. |
| LIVE 17 Nov about 1:03 am (main 3511f1fb3) | **LK286** Ask Mobi: he could not find the photo upload; "such bad UI". It must feel like a proper AI agent, with a ChatGPT or Claude-like interface "but even better", professional and clean, "more than a chatbot" with every function of one. Outcome: /mentor is a chat: a pinned composer with a labelled Photo key, the thread, History, Your record as its own tab; the docked panel shares it. Not checked: a real phone keyboard, a real model reply. The Android app's Ask screen still has the old layout and no photo key. |
| LIVE 17 Nov about 1:03 am (main 3511f1fb3) | **LK287** The product's screens do not say where the calls go (no provider named). Outcome: no provider is named in the product's screens; the privacy page still says who processes a photo. |
| LIVE 17 Nov about 1:03 am (main 3511f1fb3) | **LK288** A refused random photo costs us a model call and the student no credits: a loophole; think the whole thing through. Outcome: an ask Mobi has to read but cannot use (not a test question, or an unreadable photo) costs 1 credit, once, and the rule shows beside the price before sending; refusals before the model and our own failures stay free. |
| LIVE 17 Nov about 1:03 am (main 3511f1fb3) | **LK289** Practice: the Sunday Mock line at the top shows only as a reminder the day before (Saturday). Outcome: Practice's Sunday Mock line shows only on Saturday (a reminder) and on Sunday until the last start. |


## His third look, 17 Nov 2026 about 1:15 am (LK290-LK301; part pasted dictation, part typed)

His words, whole. The first part came as pasted dictation:

> I'll tell you right now what works and what doesn't.
>
> * Coming onto the morning side, that section is still not good. From the ones that you have made, I would say that the previous version, in which you had just spread everything vertically, was the first. That old one was better than this. Though that was not perfect in any sense or good, it was better than this. You have to think about how you can better implement all this. I am just leaving it hanging.
> * Overall, in the above card of this, there's a weird shadow that got off, so just make it soft and diffused. Keep a focus on the overall visual hierarchy of everything and how the flow is working.
> * This Asmobi thing, I would say you have depicted all this quite perfectly. This daily 5 and Sunday mock is also depicted quite well. I would just say, if we could do something different, like what Prepium is doing, because this is exactly their version copied. If you see that they don't do it this way

Then typed:

> * What they do is they have all this in a daily challenges section, and they have stuff like English daily 017 number. If you see the website and try to attempt it, what they have done is identify yourself and choose your team to appear on the leaderboard. There are some athletes' names, jersey numbers, and all this.
>
> This is just gamification of stuff. I don't know if this is good or not, but it could be something useful in general. I'm thinking in that direction and building something unique from them. What I'm saying is, what works and what's good is the UI and how you have made it look and be understandable: that part is good.

Then pasted dictation again:

> And there were many new generations of Mobi and 3D assets and image generations in the last session but I don't see any changes to that. I don't know if it hasn't been committed or if there is some other issue.
>
> The working is good now. Overall, I like the look better. Dot canceling too, but it's good. It's directing the credit also as it should. You have added, I think, some kind of soft blur to the page, which I also really like and which feels good.
>
> Also after this, what you have to focus on is improvising the streak system and refining RNTA mode and stuff like that. Overall making the website just feel very fluid and smooth is also very important. It's pretty good right now but still just make it as good as we can.
>
> Just one thing: the loading animation while opening the website is still not good at all and needs to be improvised. It should be grand in the phase, with even some animation falling through it after loading the page. Once the page is loaded and the animation has gone up, you can merge it into the MockMob logo at the top and animate the logo a little bit, of some sort. Just think about it.

Then typed:

> Finally, coming onto the app: build everything in the app and send me the final version. Whatever you build, it should be up to date with all the progress that we have made and the most complete product possible. This is our final build for the app also.
>
> Just confirm one thing for me: if the web app feature is available on iOS, is it just an extension of the website that saves the information? Or is it a full-fledged, proper app experience, like the haptics and multiple other things that can be done only in the app? Does it do all of those things? If yes, we'll build that also.

How it was read (the readings are mine, not his): "the morning side" is "More inside MockMob" (the tour); "the previous version ... spread everything vertically" is the touch stack of 16 Nov evening (516bc9511), which he now ranks above the held stage he asked for back at 10:25 pm (LK278), while his complaint about the stack (it wastes vertical space) still stands; "I am just leaving it hanging" is read as: the form is mine to decide. "The above card of this" is read as a card in or just above the tour. "This Asmobi thing" is the bring-a-mistake block. "Exactly their version copied" is read as: Prepium's look is copied, and he wants a mechanic of MockMob's own in the direction of their daily challenge (an edition, an identity, a team, a leaderboard). "Dot canceling too" is unclear (possibly a remark on the chat's typing dots); "the working is good now ... directing the credit ... soft blur" is praise for the Ask Mobi chat. "RNTA mode" is "our NTA mode". "Grand in the phase" is read as "grand in its first phase". On the art: the night's generations are in `wt-1110-convert/tmp/1116-art`; the home page's seats already used the 3D poses and only got cleaner edges, and the new poses went into Ask Mobi only, so the home page looked the same.

| Status | Item |
|---|---|
| LIVE 17 Nov ~4:12 am (main 65797fd17): on touch a deck (five still tabs over cards the finger swipes sideways, next card peeking, never held; 969 px at 390); desktop keeps the held tour | **LK290** "More inside MockMob" on phones is still not good; the vertical stack was better than the held stage, though not good either. A better form is mine to find (it must not waste vertical space). |
| LIVE 17 Nov ~4:12 am (main 65797fd17): soft shadows; a sweep finds no shadow past its section at 360/390/1440 Day and 390 Night | **LK291** A "weird shadow" on the card above or in that section: make it soft and diffused; mind the visual hierarchy and the flow. |
| HOLDS 17 Nov | **LK292** The bring-a-mistake block ("depicted quite perfectly"). |
| LIVE 17 Nov ~4:12 am (main 65797fd17): a college game: "Play for your college" (DU college pick, once a week after the first change), an admit-card seat only its owner sees, a college board (colleges, never people; floors; average from 10 players to the nearest half), edition names ("Tuesday's five, 17 Nov"), yesterday's trap; app port in the final build | **LK293** Daily Five and Sunday Mock read well but look like Prepium's; build something of MockMob's own in the direction of their daily challenge (edition, identity, team, leaderboard), keeping our clear UI. |
| ANSWERED; LIVE 17 Nov ~4:12 am (main 65797fd17): the 3D Mobi in each seat's job pose (magnifier, camera, reading, pointing, attentive, calendar, wave) | **LK294** The night's Mobi generations are not visible. Answer: nothing was lost (tmp/1116-art); the new poses went into Ask Mobi only. Now: place them on the home page where they mean something. |
| HOLDS 17 Nov | **LK295** Ask Mobi chat: works, looks better, charges as it should, the soft blur is liked. |
| LIVE 17 Nov ~4:12 am (main 65797fd17): one daily streak for every student (Mob or not): Today's block, You, a sheet with 7 days, rest passes, milestones tied to questions answered, an exam pause; Daily Five and repairs count; the top-bar chip only from 640 px up | **LK296** Next focus: improve the streak system. |
| LIVE 17 Nov ~4:12 am (main 65797fd17): instructions before the clock, an answer saved only by Save & Next or Mark for Review & Next, "Saved" / "Not saved yet" by the question number, NTA's Exam Summary, NTA style by default, no warnings counter | **LK297** Next focus: refine NTA mode. |
| STANDING; 17 Nov: a late college-board answer could move the Sunday card (CLS 0.125, intermittent): fixed and live (04004f2b2), three production runs 0.000-0.002. Open: the first swipe below the hero holds one long frame (about 380 ms at 4x CPU, rendering only, no script), not yet traced | **LK298** Make the website feel as fluid and smooth as possible. |
| LIVE 17 Nov ~4:12 am (main 65797fd17): answer sheet rain on the page's own ground, the word rises onto the bar logo, the logo settles (dot drops, Mobi hops and blinks); never delays LCP | **LK299** The opening animation is "still not good at all": grand at first, something falling through it, then it rises and merges into the header logo, which animates a little. (Replaces the 16 Nov "smaller" rule pinned by L-043.) |
| BUILT 17 Nov ~6:35 am: version 22 (1.0.24+22) in Desktop/MockMob-build-22 (signed AAB that sells, arm64 APK, symbols, README, OWNER-STEPS with the Data safety photo step): Ask Mobi chat with the Photo key, Daily Five as the college game, Sunday Mock, badges, the one daily streak, NTA mode as the exam's twin, the 3D Mobi; each lane reviewed; emulator walk done (release first run, demo signed-in screens, NTA end to end) | **LK300** The app: build everything into it, up to date with all progress, the most complete product; this is the final app build; send him the final version. |
| ANSWERED 17 Nov | **LK301** iPhone: is the web app just the website or a full app with haptics? Answer: the website in its own window (full screen, offline, push once on the Home Screen), no haptics, no App Store, no widgets; a full iPhone app means compiling the Flutter app for iOS (Apple Developer account, a Mac or cloud Mac builds, Apple in-app purchase for Pro). His decision whether to build it. |


## His brief of 18 Nov 2026, about 12:45 pm, and his note about 2:05 pm (LK302-LK312; pasted dictation)

His words, whole. First, about 12:45 pm:

> Right now, your task is to redesign and rebuild the entire website, not from scratch using our element set, but to make it more premium and more refined.
>
> The reason we are doing this is that many sections of the site are rebuilt, but many are very old and were built using the tech from AI models of previous years, which lagged in many ways: UI/UX taste and other things. To take the website to a completely next level, that's our goal.
>
> You don't have to spend much time analyzing the website side or doing that kind of thing. Your main goal should be to build, build, and build. This is not just a UI/UX design. This is improvisation of features, adding new features, refining the overall flows, and making the website as good as you can in every aspect. You have to go all out on this.
>
> Just a few things to keep in mind that need correction. For example, more inside this section needs to be rethought. Firstly, we had a thing like the mistake lab, in which we had animated cards and scroll animation on them. Now we have these sliding cards, which are not good. They have no animation, or they are a bit weird. If they are touch-responsive, no one will be able to understand that they have to touch it or do something to interact with them. These kinds of things you have to think about.
>
> The end goal should be that this website, the main platform, should be more advanced than anything in ECVT or any mock platform out in the market. The end goal should be that if any student visits our website, they should be convinced within 30 seconds that this is the best and most advanced platform available in the market.
>
> You have all the instructions and rules set already from the brain. Just one thing to remember for this specific prompt: if you are doing any 3D, animation, or text-related work, then don't want a Fable subagent for it. Do it yourself in this chat only, in this context window, because your responsibility here for today is being the orchestrator plus 3D WebCL designer for all those kinds of tasks. For all the other things, you can follow the guidelines for subagents and stuff that we have, or do it yourself. Everything is up to you. The code basis is yours. Start right now and keep updating me on the progress.

Then, about 2:05 pm, while the work ran:

> Just a thing that I wanted to say: we want tangible output, and you can do smaller things even to make a large difference. After all, it's up to you, but I'll give you some examples.
>
> Overall, when people scroll through text, just circling the text in a fancy way, maybe drawing the line under it, and having that kind of a doodle vibe in some cases while keeping it professional also. That's a small example in which you can think of improvising things. There are many other ways, but I'm just giving you a bit of direction so that you don't give me minor improvements. And overall, just thinking through things like how to properly integrate streak features or some sort of bars or icons, whatever we are using. Everything should be refined, taking inspiration from popular apps like Duolingo and other things that we have stored as skills, accessing those, and going out of my way to create a better product. And whatever you are thinking or doing, override your thought processes. Keep noting it down in the brain at a few checkpoints in between so that it's easier to retrieve context, but don't spend too much time on it. This should take less than 5% of the time overall. I was just seeing some working screenshots while you were building the 3D and stuff. It was just very bad, so don't use any subpar outputs. I saw some that you had used previously also, which were mostly way better than what you are doing right now. Anyway, if there is any issue with not getting 3D perfect, then just switch to using the image generator. I think you have access to the GPT image generator, so use that.

How it was read (the readings are mine, not his): "more inside this section" is "More inside MockMob" (the tour); "sliding cards" is the sideways deck a finger got on 17 Nov; "ECVT" is unclear (possibly "ed-tech"); "3D WebCL designer" is 3D and WebGL. "Text-related work" is read as on-screen wording and type. The "working screenshots" he saw were my Blender reference renders of a hand-built real-time 3D Mobi; "some that you had used previously" are the generated 3D Mobi stills already on the site. "Override your thought processes" is read as: write down what I am thinking and doing as I go.

| Status | Item |
|---|---|
| STANDING 18 Nov; new features LIVE about 2:25 pm (main fe0dfe8a7): Search across the signed-in site, keys and a Cross out tool on the test screen; merged, not live: Marks trend as an analysis desk | **LK302** The whole website gets a premium, refined rebuild from the existing element set: not from scratch, and not minor improvements. Build, do not analyse. Features, new features and flows as well as the look. |
| STANDING 18 Nov | **LK303** The goal: more advanced than any mock platform; a student is convinced within 30 seconds that it is the best and most advanced one. |
| LIVE 18 Nov about 2:00 pm (main 3ee7bca5e) | **LK304** "More inside MockMob": the sideways cards are "not good" (no animation, nobody knows to touch them); the Mistake Lab's animated cards on scroll are the model. Built: one deck the scroll deals on every pointer (cards rise over each other with the scroll, each tool's demo plays as its card lands, the tabs' mark slides with the scroll). |
| STANDING 18 Nov | **LK305** Today the main session does all 3D, animation and on-screen wording itself; no Fable sub-agent for those. Other work may go to sub-agents by the usual guide. |
| STANDING 18 Nov | **LK306** "Keep updating me on the progress." |
| STANDING 18 Nov | **LK307** Tangible output: small things that make a large difference count; minor improvements do not. |
| LIVE 18 Nov about 2:00 pm (main 3ee7bca5e): the pen and the highlighter on the home page (15 marks) and the sample card's verdicts; the Lab's screens and the result page LIVE about 2:25 pm (main fe0dfe8a7); the other public pages built by a lane, not live | **LK308** A doodle vibe, kept professional: as people scroll through text, circle a word "in a fancy way", draw a line under it. One example of the direction, not the whole of it. |
| PART LIVE 18 Nov about 2:00 pm (main 3ee7bca5e): Today's streak block (Mobi as the streak's mark, the number, the week's bubbles, a bar for today). NOT done: other bars and icons across the arena | **LK309** Streak features, bars and icons: think through how they are integrated; everything refined, taking inspiration from Duolingo and from the stored skills. |
| STANDING 18 Nov | **LK310** Note thinking and progress in the brain at a few checkpoints; under 5% of the time. |
| DROPPED 18 Nov | **LK311** The real-time 3D Mobi built by hand (Blender script to a WebGL mesh): he saw the working renders and called them "very bad"; the generated Mobi art already on the site is "way better". Dropped before anything shipped; no subpar output is to be used. |
| STANDING 18 Nov | **LK312** Where 3D cannot be made perfect, use the image generator (GPT image generation through Codex) instead. |


## His look at the three live batches, 18 Nov 2026 about 2:55 pm (LK313-LK315; pasted dictation)

His words, whole:

> I have seen what you have done. Mainly, I can just see the doodles and all, and some animation changes, so it's fine.
>
> One thing is utilizing the vertical space. You already have to compact so much on the phone, with so much information in a little space. Still, there is blank space. Optimizing those kinds of things, especially in the WhatsApp-side mockup screen. Sliding-up animation and that all is good, but we can utilize the screen more. All that is very small, and we can make the actual portion size of the graphic and animation larger.
>
> Doodles look good. Some can be more animated, and some sort of those things can be thought about more. I hope you have now found out everything which needs to be done, everything that already works, and what needs to be touched.
>
> Just create a prompt along with the handoff, which I can now continue in ChatGPT on the side. Just focus upon the main important things and direct it for what we have to do right now. It also has access to brains and all the tools like you, so no need to go very deep into the history and that kind of stuff.

How it was read (mine, not his): "the WhatsApp-side mockup screen" is the "what's inside" mock-up screen, the product screen inside each card of "More inside MockMob" on a phone.

| Status | Item |
|---|---|
| OPEN 18 Nov | **LK313** On the phone there is still blank space; the mock-up screens in "More inside MockMob" are "very small". Make the graphic and its animation larger and use the screen. The sliding-up animation is good. |
| OPEN 18 Nov | **LK314** The doodles "look good"; some can be more animated; think that through further. |
| DONE 18 Nov | **LK315** A prompt and handoff for the next session (he continues in ChatGPT): `PROMPT-NEXT-SESSION-2026-11-18.md`. |
| LIVE 18 Nov about 6:27 pm (main 219551a16): the tour's screens fill the phone card; the rest of LK313 (other sections) is in the round 2 lanes | **LK313 outcome** |
| PART LIVE 18 Nov about 6:27 pm (main 219551a16): the Lab heading's pen follows the scroll; figures re-ink | **LK314 outcome** |
| STANDING 18 Nov about 6:15 pm | **LK316** His words: "Basically, ask me to implement all the changes. Whatever you see, write and get this all done, keep going until you match the requirements of my first prompt." Read as: implement everything that is left myself, without stopping, until the first prompt (LK302, LK303) is met. |
| LIVE 18 Nov about 7:42 pm (main c2f12abcd): the older sections rebuilt (home: exam screen, DU Compass, DU courses, creators, pricing, FAQ, close, footer; signed-in: Progress, Your standing, Your papers, Wallet). Practice, Learn and You in a lane, not live | **LK302 / LK313 / LK309 outcome** |
| LIVE 18 Nov, pushed 9:11 pm (main 9c7b563f2): Practice as a ticket always in view (mode as its heading, G26 kept), Learn's roadmap with chapter states, You as one card; a visible pencil, red pen and marker now make the lead doodles, with sparks on two circles. Features, About, footer and article pages in two lanes, not live | **LK302 / LK314 / LK316 outcome** |
| LIVE 18 Nov 9:42 pm (main 0c9099f0e): /features as a catalogue of real product screens, /about with live figures, the footer folded on phones everywhere, the four guide pages scannable with every word kept. Left: signed-in Colleges and Saved | **LK302 / LK316 outcome** |
| OPEN about 10:05 pm 18 Nov, after looking at the live site (main 0c9099f0e) on his phone | **LK317** His words: "Okay, so now I'll give you feedback on what works and what doesn't. Firstly, when I load onto the site, you have added some weird markers or pencils kind of thing, like looking highly unprofessional. Just subtle and dual animations, how we have on most places, and previously that was good enough. And revert back to that in every place. These Animations could be a bit slower, more refined and more accurate with when they are showing up in the scroll. But other than that, nothing." Read as: the pencil, red pen, marker and sparks added at 9:12 pm are rejected: remove them everywhere, keep the plain doodle marks ("dual" is dictation for doodle). The marks themselves should draw a bit slower, more refined, and timed exactly to when the words come into view. |
| OPEN 18 Nov about 10:05 pm | **LK318** His words: "As such, then the top progress bar is a bit jumpy in the bottom because it's not moving properly." Read as: my reading, not certain: the story progress bar pinned at the bottom of the screen (Mistake Lab and More inside: "1 of 5" with the moving marker) moves in jumps instead of following the scroll. Could also be the hero film's segment bar. Confirm on a phone-size screen. |
| OPEN 18 Nov about 10:05 pm | **LK319** His words: "Then there's MockMode and NTS Style Pro mode. This is also bit of a regression. And it should be clear that NTA mode has the exact real copy of the NTS screen. And overall that desktop UI was Only better than this mobile approach which you have taken. This can be implemented when someone clicks on try full screen, then it works, but not like this." Read as: the home page's exam screen section (the MockMob / NTA style Pro switch), rebuilt at 7:42 pm as a phone-scale question, is a regression. He wants the earlier desktop-monitor presentation back (commit 219551a16), a clear statement that NTA style is an exact copy of the real NTA screen, and the phone-scale version only inside "Try it full screen". |
| OPEN 18 Nov about 10:05 pm | **LK320** His words: "And from that I also forgot you. I don't know if you have implemented that works best on desktop. Small pop-up how Clay Prep does it when first time, like every time when someone, not every time, first time someone visit the website. There should be a static pop-up on switch to desktop or basically anything like that. I had told you this before also, and just a small cross to remove it." Read as: a small static first-visit pop-up on phones saying the site works best on desktop, with a small cross, shown once. He says he asked before. "Clay Prep" is as dictated; the site he means is not confirmed. |
| OPEN 18 Nov about 10:05 pm | **LK321** His words: "Then this five a day play for your college. I don't know if you should add like colleges names to like this. I don't know if it will work. Any issues legally, but I'm not very cool. And something more simpler can be done." Read as: Daily Five's "Play for your college" (the college board): he doubts using college names (legal risk, and whether it works) and wants something simpler. "not very cool" is likely dictation for "not very sure". |
| OPEN 18 Nov about 10:05 pm | **LK322** His words: "Then this, do you compass new style is, I'm not sure if this is better or old one was better, but both were fine. But it should autoplay only and, after logging out or playing for ten. second or fifteen or something like that, then it can pause." Read as: the home page's DU Compass block: either look is fine; it should play by itself and pause after 10 to 15 seconds or when it leaves the screen ("logging out" is likely dictation for scrolling out). This overrides "nothing self-moving" (16 Nov) for this block only. |
| OPEN 18 Nov about 10:05 pm | **LK323** His words: "Then you can remove this which two voices are open to you because I mean either remove it or make it But like this is very very common PCMB science everyone has like different subject but still um this is the bit we add like in terms of UI" Read as: the home section "Which DU courses are open to you?": remove it, or make it better; the quick-start presets (Science PCM, PCB) are too generic because everyone's subjects differ, and the UI is weak. ("two voices" is dictation for DU courses.) |
| OPEN 18 Nov about 10:05 pm | **LK324** His words: "then this pricing should be moved above above on Instagram" Read as: on the home page, pricing goes above the Instagram creators section. |
| OPEN 18 Nov about 10:05 pm | **LK325** His words: "then the main issue coming on to the pricing page I'm not sure of previous. Look was better or this is better. In some sorts previous was better, in some sorts this is better. I see how you have compared it everything, but the how usual price worked out. Either incorporate it as a some button near where you have written the amount, because you are just writing three thousand seven hundred fifty usual way. But firstly, if That is hidden under a dropbox, so it will be confusion of how it adds up. So you know, this is something you should usually think about. And overall pricing page card UI can be better." Read as: the pricing card: he is unsure whether the old or the new one is better (each has better parts). The working behind "Rs 3,750 the usual way" must sit right beside the figure (a small key near the amount), not in a disclosure elsewhere, or the sum is confusing. The card's UI as a whole can be better. Lesson he names: think about whether a figure's explanation is findable where the figure is. |
| OPEN 18 Nov about 10:05 pm | **LK326** His words: "And also I think that the first loading animation of the site is a bit too short. I don't know if this is because of that or something else, but the screen stutters in the first five. That should not be happening. If overall everything should be smooth and the site, though it's fluid, but it doesn't feel like 120 FPS fluid. It feels like maybe 40, 50 FPS fluid. It's a very vague way of telling how it feels, but I hope we can fix this also." Read as: performance: the opening animation is too short, the screen stutters in the first five seconds, and scrolling feels like 40 to 50 fps, not 120. Wants it fixed. |
| OPEN 18 Nov about 10:05 pm | **LK327** His words: "Then logging in mostly things feel similar. I see just change still nothing really impressive but works overall. There are some space issues having too much blank space in some spaces and unutilized space." Read as: signed-in site: changed but not impressive; blank and unused space in places. |
| OPEN 18 Nov about 10:05 pm | **LK328** His words: "I think at I don't know if you've done something different in the practice section, but I am getting a feeling that previous one looked better. And this one is feeling like a regression." Read as: Practice (the ticket redesign, live 9:12 pm) feels like a regression against the previous page (commit c2f12abcd). |
| STANDING 18 Nov about 10:05 pm | **LK329** His words: "This is the basic crux of my feedback. Just add to it, make a proper, well-detailed, well-scoped prompt with some creative headroom. But just write down whatever you want next model to do, and I'll be basing it into GPT. If you have some 3D work or image generation work left, then also it can do that. I don't think you can continue with these changes here, so just note everything down properly and give the prompt for next session." Read as: stop building here; note everything; write the next-session prompt for GPT (docs/PROMPT-NEXT-SESSION-2026-11-18-B.md), with creative headroom and any image work. |
| DONE 18 Nov (see NOW.md for the commit and time): the pencils, markers and sparks are off everywhere, pinned by a test; the slower, better-timed marks are in the next-session prompt | **LK317 outcome (part)** |
| LESSON 18 Nov | **LK330** (the session's own reading of tonight, not his words): three of today's rebuilds read to him as regressions (exam screen, Practice, the pencils) and two as "not sure which is better" (pricing card, DU Compass). Before replacing a section he has already accepted, put old and new side by side and keep the old where it wins; an added flourish (a drawing tool) is not refinement. See memories web-restructure-rejected and tangible-doodle-direction. |
| DONE 19 Nov 3:18 pm (main e8a2d917d) | **LK317 outcome** The marks are a plain stroke, no tool, no flick. Each takes a hand's time (a circle 0.96 s, an underline 0.64 s, a highlight 0.72 s) and starts a beat (0.18 s) after its words are wholly in view and clear of the lowest quarter of the screen. Component `Doodle.jsx`; pinned by `doodlePaths.test.mjs`. |
| DONE 19 Nov 3:18 pm | **LK318 outcome** The marker on the bottom story bar now follows the story's scroll progress continuously (no hop, no 320 ms catch-up). `SectionPosition.jsx`. |
| DONE 19 Nov 3:18 pm | **LK319 outcome** On phones the exam section is the monitor again (byte for byte the 219551a16 version); the phone runner opens only from "Try it full screen". The line reads "NTA style is an exact copy of the real NTA exam screen." |
| DONE 19 Nov 3:18 pm | **LK320 outcome** A strip above the hero on phones: "MockMob works best on a laptop or desktop." with a small cross; shown on a first visit (30 minutes) or until the cross. "Clay Prep" was not looked at: the reference is unverified. |
| DONE 19 Nov 3:18 pm, his to confirm | **LK321 outcome** College names are off the Daily Five by default (switch `NEXT_PUBLIC_DAILY_COLLEGE_BOARD`, off). The section reads "Five a day. Keep your streak." The college version is one switch away if he wants it back. |
| DONE 19 Nov 3:18 pm | **LK322 outcome** DU Compass plays one sweep by itself on phones too (about 11 s), then rests; it stops when it is off screen or the tab is hidden. |
| DONE 19 Nov 3:18 pm | **LK323 outcome** "Which DU courses are open to you" is removed from the home page (the calculator page itself stays, linked from the hero). |
| DONE 19 Nov 3:18 pm | **LK324 outcome** Pricing sits above the Instagram section. |
| PART 19 Nov 3:18 pm | **LK325 outcome** The two-price bars always show; on phones a key beside the figure ("See how ₹3,750 adds up") opens the sum under it; from 900 px the sum is open beside the card. NOT done: the pricing card's own look ("can be better"). |
| PART 19 Nov 3:18 pm | **LK326 outcome** The opening is 1.75 s on a first visit and 1.1 s after (was 1.2 and 0.8). Measured on a lab phone profile (CPU x4), first six seconds of home: 35 to 43 fps before, 76 to 78 fps live; worst frame 1.13 to 1.15 s before, 0.62 to 0.65 s live. Two more causes were found after the release and fixed in f86083631 (not live at the time of this row): the session provider forcing the whole page to hydrate in one task, and `> * + *` rules restyling the page on every insert. Not checked on a physical phone or in Safari. |
| PART 19 Nov 3:18 pm | **LK327 outcome** You at 1440 loses 435 px of blank; Colleges' four subjects sit in one row at 360; a doubled hairline on Marks trend is gone. NOT done: Today's two columns at 1440, the empty 230 px right of the 960 px column on signed-in pages, anything "impressive". |
| DONE 19 Nov 3:18 pm | **LK328 outcome** Practice is restored whole to the version he preferred (c2f12abcd): page, sheet and tests. |
| LESSON 19 Nov | **LK331** (the session's reading, not his words): a rule that makes the browser or React redo the WHOLE page for one small change cannot be seen in a screenshot or a test, only measured. Three were found today: `:has()` with a state inside, a context value that changes above parts of the page not yet hydrated, a bare `*` left of `+` or `~`. Measure a production build on a slowed CPU (`tmp/1119-phone/*.mjs`) before calling a page smooth. |
| DONE 19 Nov 4:15 pm (main 64efe70d8; rollback e8a2d917d) | **LK326 outcome, part 2** The session provider no longer forces the whole page to hydrate in one task, and no `> * + *` rule restyles the page on an insert. Live, lab phone profile CPU x4: the 577 to 689 ms freeze at about 2 s is gone; longest frame after the first second 96 ms. No runtime errors. |
| OPEN 19 Nov about 4:20 pm | **LK332** His words: "from what felt better, majorly on the phone: that you added that, how it works, and how the 3,050 is calculated." Read as: on the pricing card the adds-up working is what he likes; no further pricing ask. |
| OPEN 19 Nov about 4:20 pm | **LK333** His words: "We are saying desktop is our best experience but it's way more buggy on the mobile side. It should be way more impressive than the mobile side, which it is not yet. I know mobile is way more important in terms of the landing page, but still, on desktop, you can easily go way more all out than on mobile when adding even the cursor animations, animating cursors, scrolls, and clicks. Overall, everything can be way more than mobile." Read as (mine): the DESKTOP site is buggier and less impressive than the phone one; desktop should go further: cursor, scroll and click animation. |
| OPEN 19 Nov about 4:20 pm | **LK334** His words: "Some places, the scroll is even getting stuck or very jumpy and weird. That also, I think, you should treat mobile and desktop as separate optimizations." Read as: desktop scroll sticks or jumps in places; optimise desktop separately. |
| OPEN 19 Nov about 4:20 pm | **LK335** His words: "These tools are also a bit not perfect. They are not meant to be perfect, but they are overlapping a bit too much with the other letters and have too much white space in between stuff. That's also an issue on desktop." Read as (mine, not certain): "tools" = the doodle marks; on desktop they overlap neighbouring letters too much; and desktop has too much empty space between things. |
| STANDING 19 Nov about 4:20 pm | **LK336** His words: "Whatever you say, whenever you believe that this is now the perfect version, then let me know at that time. Until then, keep going. The only reason to stop is if fees are above 95%. When that happens, I'll let you know." |
| PART 19 Nov 5:08 pm (main 23432d0e7) | **LK333-LK335 outcome so far** Live: the mouse wheel scrolls the Mistake Lab and the tour like the rest of the page (was 24 of 40 notches swallowed and four 878 px jumps; now 0 and 0, measured on live); a step costs about six notches; circle marks clear the next word; the four widest gaps between desktop sections are down from 193-277 px to 142-157 px; a ring trails the mouse pointer, opens over keys and answers a click. NOT done: richer desktop scroll and hero effects, every other mark checked at 1440, the signed-in pages on desktop, a real-mouse look by him. |
| PART 19 Nov 7:45 pm (main c22456209) | **LK333-LK335 outcome, second batch** Live for a mouse or trackpad: a named cursor (Play, Pause, Turn, Drag, Watch, Open beside the arrow), primary keys that lean toward the arrow, the hero film and exam monitor turning to face it, a faint light on the paper, the ring stretching along a scroll; on scroll the pictures of three sections drift against their words. Marks at 1440: the comma after the circled "where" no longer starts a line alone; loops and the highlighter no longer touch the next word (each mark measured: 0 px into a neighbour). NOT done: signed-in pages at 1440; a real-mouse look by him; Safari and Firefox unchecked. |
| PART 19 Nov 7:57 pm (main ce131e9b7) | **LK327, LK333, LK335 outcome, third batch** Live: in Key cards and Ask Mobi the card rides beside its words on desktop (no blank paper under it); signed-in Today uses 1120 px on wide screens (about 210 px stood empty at 1440); the tour's and exam screen's keys answer a hovering mouse; reel cards tilt. Checked on live: wheel 0 stuck and 0 jumps, every mark clear of its neighbours, no error or overflow at 1440 in Day and Night. HIS TO DECIDE: keep or drop the faint light under the arrow (a decorative glow); spread the pointer layer to the other public pages. NOT done: his look with a real mouse; Safari and Firefox. |
| PART 19 Nov 8:31 pm (main ddecb3941) | **LK333-LK335 outcome, fourth batch** Live: the ring takes the state of what is under it after a scroll (it kept an old state when the page moved under a resting mouse); loop marks clear their own last letter and their neighbours at 1440, 390 and 360; the light under the arrow goes out over films and photographs. All four evening batches verified on live by script (wheel 0 stuck 0 jumps, marks clear, no error or overflow at 1440). STILL HIS: a look with a real mouse; keep or drop the light under the arrow; spread the pointer layer beyond the home page. |
| STANDING 19 Nov about 10:15 pm, after using the live site (main ddecb3941) with a mouse on a 27 inch OLED screen | **LK337** His words: "I really want you to always produce output and calculate a real percentage of how well the task has been completed. You have been saying that it's 85% done to me since I don't know how many times and through how many passes. It's just a very vague number. Other than that, I want actual stuff being done." Read as: a percent is counted from a written list (items done and verified over items asked), shown with the list; never a round feeling, never the same figure twice without new evidence. |
| OPEN 19 Nov about 10:15 pm | **LK338** His words: "The light really looks good and is overall diffused, both in the light mode and dark mode. I would just say that it's a bit too much in the dark mode. In the light mode, it's quite subtle and diffused, and it gets a bit too large and excessive in dark mode." Read as: the torch stays (his decision); smaller and fainter in Night. |
| OPEN 19 Nov about 10:15 pm | **LK339** His words: "Overall, I would say it's like 90%, or at a 9/10 quality. The only stuff left is making it more snappy and intuitive amongst everything, so that it automatically snaps onto things. For example, if hovering over or even taking it closer to a button, it automatically snaps onto that button. Many sites do it. If you know what I'm talking about, you have kind of done it in some places but that can be worked upon a bit." Read as: the ring snaps to a button's own shape, from near it, on every button. |
| OPEN 19 Nov about 10:15 pm | **LK340** His words: "The scroll slider on the top: there are two. If I am inside the mistake lab, one is its self-slider and one is the entire website one. The self-slider, I think, is green and the top one is black but this color difference is not visible to me. Why, even on an OLED and 27-inch screen? ... The solution to this could be making the main scroller on the top some sort of unique animation so that it's visible. Inside, one can be black or green, whatever is kept normal, and the main one can be more visible." |
| OPEN 19 Nov about 10:15 pm | **LK341** His words: "Overall, the scroll feels nice but you could do a bit more in the screens with desktop. For example, more inside mock mob, there, all those are reactive scenes so just having a pop box, 'Try them out,' is not very useful. You can think about it if it's implemented in some tasteful way but overall, it looks good to me." |
| OPEN 19 Nov about 10:15 pm | **LK342** His words: "These doodles and all can be, in some places, a bit unique and they are. These are doing the animation before the scrolling or very easily so that's why I scroll and most parts are not visible. Like, about ₹1 one: firstly, it could have that circle and three dots, how it had previously. Then most places, it's fine." Read as: marks draw too early to be seen on a big screen; the ₹1 circle gets its three flicks back (the flicks only; the pencils stay off, LK317). |
| OPEN 19 Nov about 10:15 pm | **LK343** His words: "you have removed the scroll animations and all that kind of stuff from Mobie. Then we have to bring interactivity in some way or the other. Many times it appears and many times it disappears. I don't know if I am weird to notice it or this is actually happening. Many interactive movie elements, I think, which previously existed, have now been replaced with static images, with no floating eyes or anything." ("Mobie", "movie" = Mobi.) |
| OPEN 19 Nov about 10:15 pm | **LK344** His words: "Honestly I'm nitpicking stuff here. It's fine only but just see if it is possible for you to improvise in any way because already everything is good enough. Just some final finish would make it a lot better and now it's truly looking like a proper desktop experience ... Overall I just feel like, in some way or other, scroll could be made a bit better, like using some kind of scroll craft if possible. Honestly overall, I'll say I'm really happy with most of the things so I wouldn't complain much." |
| OPEN 19 Nov about 10:15 pm | **LK345** His words: "you have added a search function, which is nice, but Control+K, I think, is the default Windows shortcut. Could be anything but can we replace it with Alt+Space or something like that? ... Like Control+K ... becomes very hard to use for most people ... I think Alt+Space would trigger something on the browser. Windows+Space is also triggering that language thing. I don't know if any key is actually free. You can think about it ... When someone first uses the search, a small introductory pop-up can come, like, 'This is your one place to search everything' or 'Search for anything, one place to search for everything. Central control.'" |
| OPEN 19 Nov about 10:15 pm | **LK346** His words: "the insight platform thing can be made a bit more interactive in some places and overall white space is still a lot more here. Optimizing it for proper use and making everything properly resizable for all screens: if I'm using it on a 27-inch screen, maybe this is because it has too much white space. It would be less on a laptop but it should not happen even in edge cases like these. It should be able to resize to every scene. That's what reactive UI is." |
| OPEN 19 Nov about 10:15 pm | **LK347** His words: "There are some cards, for example, in this quick practice and mocks cards, which come on the right-hand side. You have an edge light kind of thing in which there's a green border but it's not closing it properly. There is some weird UI bug. Platforms: I'll say the overall platform is in really good shape right now. Picking up from here you could just keep undermining more things which you identified as gaps or just improvising everything." |
| OPEN 19 Nov about 10:15 pm | **LK348** His words: "in the learn section: for 'Find a topic' you have used the slash key. This is not an issue but instead of doing this you could at least maybe use some easy-to-access key, like Shift or something else. If you have some logical reason behind it, if it's a familiar shortcut, or if it's a Windows shortcut, then fine but if not, then these kinds of UX things also matter." |
| OPEN 19 Nov about 10:15 pm | **LK349** His words: "Another bug I noticed in the progress section, the streak: I'm cutting onto the UI and it's not very proper. In general I didn't like the streak system that you have built. It's very basic. It's just existing for the sake of it. Streaks are only implemented if they are useful or integrated extremely well into the app. How Duolingo does it is only one example ... but if you copy Duolingo then it will be trash here only also. Because they made the streaks how it would be useful for their platform, for them ... Duolingo is a gold standard of how to think, how design thinking happens, and how to think through stuff to implement properly to our specific needs and business ... Streak is not itself a very important feature, but overall, I would say the platform and features, everything which are still on the backfoot or not as good, can be improvised in that way." Also: "I think the streak system can be redesigned and made more innovative. Some inspiration from Duolingo can be taken." |
| OPEN 19 Nov about 10:15 pm | **LK350** His words: "On desktop, we have a lot of space, so even the Asma, we can set as a quick-to-access chatbot on the right-hand side of the screen also. It's there already on easy access, on the left-hand side, just below the Start Session button. That's good, but it's an unusual situation, so people might not notice it." ("Asma" = Ask Mobi.) |
| STANDING for this pass, 19 Nov about 10:15 pm | **LK351** His words: "Coming on to the last point for this pass, just focus on website and app final passes for both of them. Right now, I have not mentioned to you anything very major. There are some parts which are a bit difficult to do, require thinking, or are not as well scored, but most of these are smaller refinements or easier tasks. You can mainly make this pass go quickly rather than also taking 3, 4 hours. Just assign these two smaller agents, like Sonnet or Opus, using the guide that we have in our brain for subagents if you require it. All this is up to you." Read as (the session's reading): "website" = the public home page, "app" = the signed-in web platform he had just used; the Flutter app was not in this feedback. |
| LIVE 19 Nov 11:30 pm (main ea1bdfa68) | **LK338 to LK343, LK345, LK348, LK349, LK350 outcome** Home, mouse only: Night's light smaller and fainter; the ring snaps onto a key from near it; Mobi rides the page's reading line (the Lab's rule stays plain); tour screens say "Try it"; a mark waits until the page has stopped, and the price figure has its three flicks; Mobi has stops again in the Lab, the tour and Key cards and his eyes move in every pose (he had been one still picture for half the page since the 17 to 19 Nov rebuilds). Signed-in: Search by Ctrl Space with a first-use line; type-to-find on Learn; an Ask Mobi key at the bottom right that docks on wide screens; the streak as one highlighter line with what the run has made, a pace line and a key. Seen in fixtures and by script; not with a real mouse or a real account. |
| LIVE 19 Nov 11:40 pm (main 2e7430340) | **LK346, LK347 outcome** Signed-in pages are centred and grow in steps to 2560 px (three columns on Today, Progress, Marks trend and You from 1800); the Practice card's edge closes all round (it was an inset shadow painted under the sticky Start row); Marks trend answers hover and focus. Not seen on a real 27 inch screen. |
| PART 19 Nov 11:40 pm | **LK344 outcome so far** Only the pricing backdrop word's drift was added as new scroll craft; the rest of what moved with the scroll tonight is the rider, Mobi's journey and the mark timing. Open for a next pass if he wants more. |
| OPEN 20 Nov about 1:55 am, after using main 2e7430340 (Opera GX, a high-end PC) | **LK352** His words: "some things I really like: how you have implemented some snapping-in features and with the cursor. The things that you have done, all that is, I would say, really good. I think when the things are snapping on, it should feel like it is just getting snapped onto the existing button rather than putting a bubble over it. That can work for something, but I think this needs a bit of refinement. In some places, it's really good and works, and in some places, it doesn't. Overall, I would rate it a 9/10, but it needs improvement." |
| OPEN 20 Nov about 1:55 am | **LK353** His words: "I'm feeling that the website has become a bit too slow and sometimes not loading things, maybe because it has become a bit too heavy. Just see to it and make sure it runs on even weaker systems, because if it is causing an issue on such a high-end system, then the target should be that it should easily work on a even a cheap ₹15,000 cromebook. The target should not be to check if it's working on a ₹1 lakh laptop or MacBook." And: "focus on the snappiness of the website and, as I said, making it look as smooth as possible. You can add more scroll but I don't exactly know what you would add as more scroll effects. That's not important. What is important is to refine and double down on this." Read as: speed and smoothness are the pass; the yardstick is a cheap Chromebook, measured, not a fast laptop; more scroll effects are dropped. |
| OPEN 20 Nov about 1:55 am | **LK354** His words: "many heavy sites ... use, what I have seen, some sort of a compulsory loading screen to load all the assets of the site or something in that way." Read as: his idea, mine to judge; a loading screen is worth it only if it really loads what the page then needs. |
| OPEN 20 Nov about 1:55 am | **LK355** His words: "some sort of a visual hierarchy in between the different sections is missing because some things are up and some are down. In the Home Today section only, when there's a line, 'Welcome back Atishay,' the front of it should be blank and everything should be below it, like some sort of headings. Having other sections in one place and having everything leveled properly, that is the kind of thing I'm talking about." Read as: on Today the greeting stands alone on its row; every column starts below it at the same level, each under a heading of the same kind. |
| OPEN 20 Nov about 1:55 am | **LK356** His words: "The Search Again issue is Control + Space. At least on my browser, I'm using Opera GX. It's been using it for the search stuff function so it's not working on the website ... Yes it's working on Chrome so I think it should work for most people ... Just see it. Wait if this is the best that we can do. If there is any other more available shortcut, that would be better for more browsers if you think. Search about this also and overall, making the UI of the search better. It's fine already. If you can make it a bit better and more intuitive, like how Apple has done it with their Spotlight." |
| OPEN 20 Nov about 1:55 am | **LK357** His words: "The Ask Mobi on the desktop also has to be improved. The Ask Mobi, both things: the Ask Mobi section itself, the UI there only, and especially where you have placed Ask Mobi on the left side, it's a bit weird. When I am clicking it in the practice section, for example, the entire other space is getting cropped into some sort of a placeholder box or something. Overall, this entire chatbot could just be, on the bottom, an opaque or glass-morphism kind of small chat box, which can then be expanded into a full page or window. Try then doing. You can just think whatever is the best approach for this, but definitely this is not it. Apart from this, I think most things feel good to me". Read as: the page-narrowing dock and the round key are rejected; a small chat box at the bottom that opens into a window, then a full page; the page under it is never cropped. |
| STANDING 20 Nov about 2:40 am | **LK358** His words: "even though I am right now testing and giving my feedback on the desktop only, it's not like our primary focus has not shifted to desktop. The primary focus is still on mobile because the majority of the audience will be on mobile. I'm not sure about the platform and how it will be used, mobile or desktop. That could be a majority desktop because of the app, but the landing page will be almost 100% mobile ... for the landing page, the entire video section, and everything like that, which will be the first impression, that is still related to mobile only ... I just wanted to tell you not to spend too much time on fixing very many [fine details] on the desktop. If some improvisations are to be made on desktop, that should be majorly based on the platform, inside-side of things." Read as: landing = phone first, measure and polish there; desktop effort goes to the signed-in platform. |
