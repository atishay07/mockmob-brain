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
| PROTOTYPE 9 Nov (branch proto/phone-free-scroll 27b8da7ac, Vercel preview; NOT live) | **LK179** "Can you make a hero section with a revised scroll function? We don't like forcefully forcing people to scroll through the entire section. They can see if they want to ... what we have implemented right now would be irritating on a mobile phone. It could be okay on a desktop, but on a mobile phone, that full functionality stopping deliberately in some places would be frustrating or maybe lower the conversion rate ... let me know which is the best approach, and then make a prototype link which I can see on my phone." This reverses L-029 / LK69 / LK103 (held stories, one gesture one step) on phones. Prototype: nothing holds on phones or touch screens; Mistake Lab is a sideways row of four scene cards with its tabs; the statement scrubs with the scroll; the tour and Recovery Lab use their swipe/tap modes. Desktop with a mouse keeps the holds. Waits for his look on the phone. |

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
| LOCAL, awaits his review (web/1109-demo-result 5dbcea349; not live) | **LK184** "Make a small, visible polish pass on the public MockMob homepage, centred on the existing five-question demo ... try real CUET-style practice, understand an actual mistake and see what a full mock would add ... Stop with a local diff for review. Production release is a separate owner decision." Done: misses named Q2/Q4 + chapter, your answer beside the correct one, honest heading and next step, one line on what a full mock adds. Packet B (dock over the arrival) did not reproduce, so no change. Report: wt-1109-demo-result/tmp/1109-demo/report/index.html. |
