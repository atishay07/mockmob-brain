# ACCEPTANCE-1019: the checklist that proves every item on the 19 Oct release candidates

Written 19 Oct 2026, about 2:35 am IST, by the brief-14 author (Opus 5.5) for session 25ef3d95. It changes no code. It is the sheet the final walk and the Opus verifier tick, item by item.

**Candidates under test**
- **App v15.3:** branch `ui/v15.3-1019` in `wt-v15-3` (from ab04b067), a PROFILE APK built with `dart_defines/phone-relay.json`.
- **Web release 11:** branch `deploy/web-1019-r11` in `wt-rel11` (from 23a7c090), served by a dev server for fixtures and by the staging launcher for signed-in checks.

**Read in full before writing:** OWNER-FEEDBACK-2026-10-19.md (G1-G33, D101-D113), PLAN-1019.md (R1-R8, every SPEC and DONE WHEN), tmp/feedback-1019/FORENSICS.md, AUTOPILOT-GOAL-1019.md, briefs 01-14, BRIEF-1019-COMMON.md, NOW.md. Exact strings, files and flags below were read from the v15.2 code (ab04b067) and live web main (23a7c090), so a verifier knows what "before" says.

**Count:** 46 blocks = 33 G items (G1-G33) + 13 decisions (D101-D113; D113 is read-only extra). Nine of the D blocks (D101, D103-D110) are short blocks that point at the G block that holds their steps.

---

## 0. How to use this sheet

1. **One block per item.** Each block has: his words, the decision, the DONE WHEN, the test steps, the proof to open, the R4 comparison, the R2 line, and "Fail if".
2. **An item is DONE only when** every "Proof to open" file exists and was opened by the verifier, the R4 pair shows no loss, the R2 answer matches the pass answer, and no "Fail if" line is true. Anything less is NOT DONE with the reason.
3. **No DONE WHEN exists for some items.** PLAN-1019 gives a SPEC and no DONE WHEN for G5, G21, G24-G31 and for the KEEP and rule items (G2, G8, G10, G14, G23, G32, G33). For those the block copies the SPEC's closing sentence (or AUTOPILOT-GOAL section 7 for KEEP items) and says so.
4. **Order of proof is fixed by R1:** the FRESH account is walked first, the HEAVY account second. Every app proof is at 360 dp in Night and in Day; every web proof is at 390 and 1440 in Night and in Day.
5. **OWNER tags.** Two proofs end on his phone and cannot be closed on the emulator: G3 (his keyboard) and G22 ("he sees the moment on his phone"). The verifier proves everything up to that point, marks the item "DONE on emulator, OWNER confirms on phone", and MESSAGE-1019.md says so.
6. **Common fail rules (true for every block, not repeated):**
   - broken English, a dropped article, a clipped label, or a fragment anywhere on a changed screen (R6);
   - a feature, tile, row, gradient, texture or motion that v15.2 or release 10 showed and the candidate does not, unless he asked for it (R3, R4; HIGH);
   - the same number shown with two values on two screens, unlabelled (the 18 Oct walk found repair counts 139 / 19 / 2);
   - the keyboard covering a focused field, or text clipped at 1.3x text;
   - a Pro-only thing shown with a price, a buy key or a web link while PLAY_BILLING is off (anti-steering, D101).

## 1. Shared setup, evidence names and the "before" sets

### 1.1 Accounts and devices
- **FRESH:** a NEW staging test student, created on this walk through the app's own sign-up (email code). Generate the code with `node --use-system-ca scripts/dev/staging-otp.mjs <email>` from `wt-batch` (RIG-READY.md). Never reuse an old test student, never use the owner's account.
- **HEAVY:** `app-e2e-student@example.com` (staging; free plan; subjects Accountancy and English; many papers, 390 credits when last walked).
- **Emulator:** `emulator-5554`, AVD `mockmob_budget`, 720 x 1600 at 320 dpi = **360 dp**. Hold the lock `C:\Users\atish\AppData\Local\Temp\mm-emu-lock`. Never touch device 10BF370PA6002XR.
- **Staging site for the walk:** `wt-rel11` served by the launcher pattern `tmp/rig-1016e/stagingLocalApp.r9-3103.mjs` copied to port 3104, then `adb -e reverse tcp:3101 tcp:3104`. Restore the reverse afterwards. Warm `/api/stats`, `/api/auth/me`, `/api/attempts/summary` first.

### 1.2 Phone switches (all through adb, all restored at the end)
| Need | Command |
|---|---|
| Night / Day (app on "Match phone") | `adb -e shell cmd uimode night yes` / `night no` (else You > Appearance) |
| Text 1.0 / 1.3 / 1.6 | `adb -e shell settings put system font_scale 1.0` / `1.3` / `1.6` |
| 412 dp width | `adb -e shell wm size 824x1830`, undo with `wm size reset` |
| Short screen (keyboard stress) | `adb -e shell wm size 720x1280`, undo with `wm size reset` |
| Reduced motion | `adb -e shell settings put global animator_duration_scale 0` (and window and transition scales), back to 1.0 |
| Offline | `adb -e reverse --remove tcp:3101` and `--remove tcp:3102`; online again with `adb -e reverse tcp:3101 tcp:3104` and `tcp:3102 tcp:3102`. Airplane mode does NOT cut the adb tunnel. |
| Late-night clock (G1) | `adb -e shell settings put global auto_time 0`, `adb -e root`, `adb -e shell date MMDDhhmm` for 1:30 AM; restore auto time. If the image is not rootable, use the pinned late-night widget test and say so. (At the time of writing the emulator clock is already past 2 AM, so the late-night line shows for real; after 5 AM it needs forcing.) |
| Keyboard state | `adb -e shell dumpsys input_method` and read `mInputShown` |

### 1.3 Evidence names (new folders are created by the walk; the two baseline folders already exist)
- Candidate app shots: `tmp/walk-1019/cand-app/<ID>_<screen>_<fresh|heavy>_<night|day>[_t130|_t160|_412].png`.
- Candidate web shots: `tmp/walk-1019/cand-web/<ID>_<page>-<state>_<390|1440>_<night|day>.png`.
- Frame sequences (app and web): `tmp/walk-1019/frames/<ID>/f-0000.png ...` plus `timing.md` (first moving frame, last moving frame, ms between, measured values). Frames come from `adb -e shell screenrecord --time-limit 8 --bit-rate 8000000` (app; as in tmp/rec-1014/FINDINGS.md, frames by the imageio-ffmpeg binary, read frame time from the video's own timestamps, not by counting frames) and from Playwright `recordVideo` (web). For numbers, web also injects a `requestAnimationFrame` sampler (`page.addInitScript`) that logs `performance.now()` against the value under test (counter text, `scrollLeft`, opacity, transform).
- R4 pairs: `tmp/walk-1019/r4/<ID>_<screen>_before-after_<night|day>.png` (before on the left, candidate on the right, labelled).
- R2 lines: one row per screen in `tmp/walk-1019/R2-LINES.md`: `screen | what a first-time student thinks it wants | matches the pass answer? | note`.
- Verdicts: the scoreboard in section 5, filled in `tmp/walk-1019/ACCEPTANCE-RESULTS.md`.
- Web Night = `localStorage['mm:theme:v1']='dark'` (set with `addInitScript` before load); Day = unset or `'light'`. Reduced motion = `localStorage['mm:motion:v1']='reduced'` or Playwright `reducedMotion:'reduce'`. Headless playwright-core only (the path in BRIEF-1019-COMMON.md), never a visible browser, never the chrome-devtools MCP.

### 1.4 The "before" sets (R4)
| Set | Folder | Naming | Status at about 2:30 am |
|---|---|---|---|
| App v15.2 baseline (the build on his phone) | `tmp/walk-1019/baseline-v15.2/` | `nNN-screen.png`, for example `n01-welcome.png`, `n02b-welcome-mobi-line.png`, `n07-onb-step2-colleges.png`, `n08-onb-college-search-hans.png` | filling in (13 shots so far, through the college search) |
| Web release 10 baseline (live main 23a7c090) | `tmp/walk-1019/baseline-web-r10/` | `<page>-<state>-<390 or 1440>-<dark or light>[-full].png`, for example `colleges-default-1440-dark.png`, `mob-alone-390-light-full.png` | filling in (206 files so far) |
| v15.2-era fallback shots | `tmp/app-walk-1018g/NN-name.png` (and `.s.png` small copies) | numbered | complete (224 files); used when a key is missing from the baseline |
| v15.1-era motion clips | `tmp/app-walk-1018/clip-*.mp4` (tab-switch, submit-reveal, mock-reveal, finish-to-today, reel-not-now, today-swap, start-sheet, askmobi-open, theme-switch) | named | complete; the nearest before-motion that exists |
| Web "before" for G26 and G27 and Review/Account | `tmp/feedback-1019/a4b/` (`g26-base-1440-dark-after-pick.png`, `g26-base-390-dark-after-pick.png`, `g27-base-390-dark-sheet.png`, `g27-base-1440-dark-sheet.png`, `explore-base-practice-*`, `explore-base-profile-*`, `explore-base-review-*`, `explore-base-review-one-*`) | named | complete |
| Web lit build (target look for G28, G31) | detached worktree `wt-1019-a4a-before` at 77713336 (`deploy/1016-batch`, 10-16 01:33), preview server on port 3502; springs only: `deploy/1015-night` 3fc0095b | n/a | agent A4a made it; re-use or recreate |
| Approved app finish moment (G22) | commit 68f63c11 (`flutter_app/lib/features/practice/widgets/finish_stage.dart` and `finish_ceremony.dart`, `flutter_app/lib/features/practice/practice_result_screen.dart`, goldens `test/golden/practice/goldens/finish_0ms_*.png`, `finish_400ms_*.png`, `finish_900ms_*.png` (day and night)) | git | complete |

**Baseline gate before E1:** every "before" key a block names must exist in `baseline-v15.2/` by eye (key = screen words in the file name) or in the fallback list. If not, install the v15.2 PROFILE APK (`wt-v15-2/flutter_app/build/app/outputs/flutter-apk/app-profile.apk`) and capture the gap in one short extra session. Also read `tmp/walk-1019/BASELINE-FINDINGS.md` and `BASELINE-WEB-FINDINGS.md` when they land: G16 uses them as its dead-end list.

### 1.5 App facts the verifier needs (read from v15.2, ab04b067)
- **Bar today:** Today, Practice, Review (with an open-repairs badge), Colleges, You, plus the round Start key beside the capsule (`lib/core/widgets/bar/bar_tabs.dart`).
- **Welcome strings (`lib/features/onboarding/copy.dart`):** headline "Every lost mark has a pattern."; support "MockMob finds yours, helps you repair it, and checks the repair holds. Two minutes to set up."; Mobi bubble "Hi, I'm Mobi. Let's find yours."; late-night line (11 PM to 5 AM) "Late one tonight. Two minutes, then sleep." That last line is what he heard as "1 light late 1 to 9, 2 minutes and sleep" at about 1 am. Other clipped Mobi lines in the same file: "About a second. Clean.", "Classic trap. Fix below.", "Now be harsh. Tap Shaky on any you'd dread.", "Still yours to seal."
- **First question step ("1 of 7"):** "Which colleges would you say yes to tomorrow?", "Lowest Round 1 score in 2026, out of 1000.", a course chip (B.Com (Hons)) with a pencil, a category menu ("Showing unreserved"), the "Find a college" search field (the college search), "0 of 8 picked", then the ladder with real numbers (SRCC 924.3, Hindu 919.9 in the v15.2 shot). The six most-chosen course tiles and "More courses" open from the chip. Up to 8 colleges. Data file: `lib/features/onboarding/data/du_2026_data.dart` (2026 Round 1 minimums, which is last year's data for CUET 2027).
- **Practice modes (`lib/features/practice/copy.dart`):** Quick practice, By chapter, Smart practice, Full mock, NTA mode. Gated lines today: "Comes with Pro" and "not part of your plan".
- **Type your own range:** Colleges screen > "Type your own" (also the programme screen) opens the estimate sheet (`lib/features/tools/estimate/`): From and To fields, "Out of 1000. A range is fine; most students aren't sure yet.", a source switch (From your latest full mocks / From your practice projection / Type your own), "Use as my estimate", and the headline "Your colleges: N of M clear". Row words today: "Clears by X", "Within your range", "Needs X more". The existing mocks line reads "Full mocks in N of the 4 papers DU counts."
- **Result flows:** quick, chapter and smart sets go to `practiceResult` (the regressed one). Full and NTA mocks go sealed sheet, then 4-card recap, then the full result (still alive).
- **Free starting balance:** RIG-READY.md recorded a fresh free test student starting at 90 practice credits; a quick 10 costs 10, a full mock 50. The walk records the real starting balance of the FRESH account (it matters for G19).

---

## 2. Item index (46 blocks)

| ID | Kind | Group | Session | Decision |
|---|---|---|---|---|
| G10 | KEEP | A1 | E1, E3 | KEEP |
| G11 | BUILD | A1 | E1, E2 | |
| G15 | BUILD | A1 | E2, E3 | D101 |
| D101 | decision | A1 | E2 | Visible but locked |
| G17 | BUILD | A1 | E1, E2, E3 | D105 |
| D105 | decision | A1 | E1, E2 | Own tab in the bar |
| G1 | BUILD | A2a | E1 | |
| G2 | KEEP | A2a | E1 | KEEP |
| G3 | BUILD (OWNER) | A2a | E1 | |
| G4 | BUILD | A2a | E1 | |
| G5 | ANSWER | A2a | E1, E2 | not now |
| G6 | BUILD | A2a | P, E1, E3 | D103 |
| D103 | decision | A2a | P, E1 | Real cutoff data, shown |
| G8 | ANSWER | A2a | E1 | no action |
| G9 | BUILD | A2a | E1 | |
| G7 | BUILD | A2b | E1, E3 | D104 |
| D104 | decision | A2b | E1 | Top 3 plus all N |
| G12 | BUILD | A2b | E1, E3 | |
| G13 | BUILD | A2b | E1, E3 | |
| G14 | KEEP | A2b | E1, E3 | KEEP |
| G20 | BUILD | A3 (and A1, A4b) | E2, E3, W1, W2 | D106 |
| D106 | decision | A3 | E2, E3, W1 | Papers first, then mistakes |
| G22 | BUILD (OWNER) | A3 | E2, E3 | D108 |
| D108 | decision | A3 | E2 | Restore the reveal, then refine |
| G18 | BUILD | A5 | E2, E3 | |
| G19 | BUILD | A5 | E2, E3 | D109 |
| D109 | decision | A5 | E2, E3 | One mock per subject |
| G28 | BUILD | A4a | W1 | |
| G31 | BUILD | A4a | W1 | |
| G25 | BUILD | A4b | W1, W2 | D106 (web) |
| G26 | BUILD | A4b | W1 (and app) | |
| G27 | BUILD | A4b | W1 | |
| G29 | BUILD | A4b | W1, W2 | |
| G24 | BUILD (mock-up first) | C1 | W1 | D107 |
| D107 | decision | C1 | W1 | Mock-up 2-3 options |
| G21 | BUILD (mock-up first) | C2 | E2, E3, W1 | D110 |
| D110 | decision | C2 | E2 | Mock-up first |
| G30 | BUILD (mock-up first) | C3 | W1 | |
| G16 | WALK | X | E1, E2 | |
| G23 | RULE | X | all | |
| G32 | PROCESS | X | end | |
| G33 | PROCESS | X | end | |
| D102 | process | X | end | Planning only |
| D111 | process | X | end | Explain, then deliver |
| D112 | process | X | W1, E2 | Pick the recommendation |
| D113 | process | X | end | No Autopilot tonight |

---

## 3. Blocks, grouped by surface owner

# GROUP A1: app shell and Practice (brief 01, branch ui/1019-a1-shell)

### G10 KEEP: the bigger base and its animation
- **His words:** "really love the bigger base. You can keep a really great UI and all. Really love the steamed animation." (G10; "bigger base" is read as the bottom bar and "steamed" as the stream/glide of its pill, both "(confirm)" in the ledger.)
- **Decision:** KEEP the UI direction. Because D105 re-lays the bar (five controls), this is a regression check on size, glass and the pill's glide.
- **DONE WHEN:** none in PLAN-1019 (KEEP). Rule used, AUTOPILOT-GOAL section 7: "Keep (he praised these; do not touch except for bugs): ... the bigger base and its animation".
- **Test (E1 FRESH, E3 HEAVY; Night and Day):**
  1. Today at 360 dp: crop the bar. Measure capsule height, width, corner radius, bottom inset and the glass (blur, edge light, shadow) in the candidate and in v15.2.
  2. Record 4 s of Today > Practice > Mob > You > Today (`screenrecord`). The selected pill must glide, not jump. Compare its duration and curve with `tmp/app-walk-1018/clip-tab-switch.mp4` (v15.1-era) and the v15.2 baseline.
  3. Press the Start key and release: the press feedback is unchanged.
  4. Repeat the bar crop at text 1.3.
- **Proof to open:** `cand-app/G10_bar-crop_*_{night,day}.png` (both accounts), `frames/G10/timing.md`.
- **R4:** before = `baseline-v15.2/` key `today` bar region (fallback `app-walk-1018c/14b-bar-crop.png`, `app-walk-1018g/28-today.png`). Any loss of height, blur, glow, or glide is HIGH.
- **R2:** "Bar": a first-time student thinks "five places; I am on Today; the big round key starts a paper."
- **Fail if:** bar shorter or narrower than v15.2 by more than 2 dp; glass or blur gone; the glide replaced by a jump; the Start key stops being the single dominant key.

### G11: the Today pill is not evenly rounded
- **His words:** "the bubble around "Today" is fine in others, but it's kind of not evenly rounded at the edges."
- **Decision:** the selected-tab pill is a perfect stadium on every tab.
- **DONE WHEN (verbatim):** a zoomed screenshot shows even ends.
- **Test (E1 and E2 FRESH; Night and Day):**
  1. For each selected state (Today, Practice, Mob, You): `screencap`, crop the pill, enlarge to at least 4x.
  2. Overlay two circle guides of radius h/2 on the pill's left and right ends. Record the left and right inset (pill edge to the first and last glyph of its icon and label) in px, and the pill centre against the icon-and-label centre.
  3. Repeat at 360 dp with text 1.0, 1.3 and 1.6; at 412 dp with 1.0 and 1.3 (`wm size 824x1830`); once in Day.
  4. Watch the end of the glide: the pill must not settle off-centre or flat on one side.
- **Proof to open:** `cand-app/G11_pill-zoom_<tab>_<theme>_<scale>.png` with the guides drawn, and a one-line table of the measured insets in `frames/G11/timing.md` (pass = ends match a half-height circle within 1 px at 720 px width, left inset = right inset within 1 px, centres within 1 px).
- **R4:** before = `baseline-v15.2/` key `bar` or `today` (the owner's own complaint is the Today pill). Make the before-and-after zoom pair side by side.
- **R2:** "Bar, selected tab": "the glowing shape tells me which place I am in."
- **Fail if:** any end is flatter than the other; insets differ by more than 1 px; the label clips at 1.6; the pill is not centred on its icon and label; any other tab pill differs from the Today pill.

### G15: Practice shows every mode (visible but locked)
- **His words:** "There is no option for smart mock or NTA mock. Why is that?" and "the UI feels incomplete to me, honestly."
- **Decision:** D101, "Visible but locked": every mode is always listed; Pro-only modes carry a quiet Pro tag; with billing off a tap opens a calm sheet with no price and no link.
- **DONE WHEN (verbatim):** on a fresh Free account, Practice shows all the modes.
- **Test (E2 FRESH, then E3 HEAVY; Night and Day):**
  1. Practice tab, scroll top to bottom. Expect five tiles: **Quick practice, By chapter, Smart practice, Full mock, NTA mode** (PLAN names four; By chapter is what he saw and must stay, so nothing that was visible disappears). The Pro-only ones (Smart, NTA) show a quiet "Pro" tag (a small text tag, not a coloured badge).
  2. Tap NTA mode, then Smart practice. Each opens a calm sheet. Expected NTA text: "NTA mode is part of Pro. Pro opens in the app soon." Read the whole sheet: no price, no rupee sign, no "Upgrade" or "Buy" key, no link, no web mention. Close works. Nothing starts.
  3. Repeat the locked entries in the Start sheet, Today's alternatives sheet, and the NTA instructions screen (v15.2 hid them in `alternatives_sheet.dart`, `quick_start.dart`, `nta_instructions_screen.dart`).
  4. With billing ON (PLAY_BILLING true): tap opens the Upgrade sheet; a Pro student opens and uses both modes. Prove this with the widget tests (Free and Pro, billing off and on, four cases) or a second PROFILE build with `--dart-define=PLAY_BILLING=true`.
  5. HEAVY: the same five tiles (v15.2 already showed Full mock and NTA mode with a Pro tag here).
- **Proof to open:** `cand-app/G15_practice-top_fresh_*`, `G15_practice-bottom_fresh_*`, `G15_locked-sheet-nta_fresh_*`, `G15_locked-sheet-smart_fresh_*`, `G15_start-sheet_fresh_*`; the four widget test names.
- **R4:** before = `baseline-v15.2/` key `practice` fresh (shows only Quick, By chapter and Full mock: this is his complaint) and heavy `75-practice-bottom.png` (fallback). The NTA tile keeps its exam-day art and "The exam-day screen." line.
- **R2:** "Practice": "pick a subject and a way to practise; the ones marked Pro are not open yet."
- **Fail if:** any mode is missing for a fresh Free account; a locked tile starts a paper; the Pro tag is loud; the sheet shows a price, a link or an upgrade key; the sheet text is the old "not part of your plan"; a tile's art is lost.

### D101: NTA mode (and any Pro-only mode) visible but locked
- **His words:** "Visible but locked" (his answer, 1:35 am, about NTA mode while Play billing is off).
- **Decision:** D101: visible but locked while PLAY_BILLING is off: a quiet Pro tag, no way to buy, no web link or price. Never hidden.
- **DONE WHEN (verbatim, G15):** on a fresh Free account, Practice shows all the modes.
- **Test:** steps 1-5 of G15. Extra: with billing off, tap every locked entry the app has (Practice tile, Start sheet, Today alternatives, a Pro-only deck card if any) and read each sheet for a rupee sign, "buy", "upgrade", or a URL.
- **Proof to open:** the G15 files plus `cand-app/D101_locked-entries-sweep.md` (one row per entry: where, text, clean y/n).
- **R4 / R2 / Fail if:** as G15.

### G17: the Mob gets its own tab
- **His words:** "I also don't see the mock. It's here, so I can't really test this out. It is hidden inside the use section, so that won't work." ("mock" read as Mob, "use" as You.)
- **Decision:** D105, "Its own tab in the bar (Recommended)": the bar becomes Today, Practice, Start, Mob, You; Review moves into Practice as "Your papers".
- **DONE WHEN (verbatim):** the bar shows the five, and the Mob is one tap away on a fresh account.
- **Test (E1 and E2 FRESH, E3 HEAVY; Night and Day):**
  1. After sign-in the bar shows exactly five controls, in this order: Today, Practice, Start, Mob, You. Start stays the one dominant round volt key. Review and Colleges are not bar items.
  2. Tap Mob on the FRESH account (no Mob). Expect a clear screen with "Start a Mob" and "Join with a code" (plain words, two keys, no study-week gate, no empty page). Open both: the code field is not hidden by the keyboard; create a Mob (a bad name shows a plain error, as in `91b-name-invalid.png`); the invite sheet works.
  3. After the Mob exists: the Mob tab shows your Mob, this week's paper and the invite. Today's Mob card is gone (it shows only while the student has no Mob: check before and after creating).
  4. You hub: the Mob row (the 6th row, `MobHubRow`) is gone.
  5. HEAVY (a Mob member): same Mob home; check the leave flow is still reachable.
  6. R3 sweeps (D105 names five items and does not say where Colleges goes): from a fresh Today, the Colleges screen is reachable (Today's colleges card "See all", and You). Review's open-repairs count survives somewhere on the Practice tab (the "Repairs: N open mistakes" row or a badge on Practice or "Your papers"). If either vanished it is a HIGH.
  7. Old entries still land: the `/you/mob` and `/mob` routes, notification and result deep links (route redirect tests by name).
- **Proof to open:** `cand-app/G17_bar_{fresh,heavy}_*`, `G17_mob-tab-nomob_fresh_*`, `G17_mob-home-member_heavy_*`, `G17_you-hub-no-mob-row_fresh_*`, `G17_colleges-reachable_fresh_*`, the route test names.
- **R4:** before = `baseline-v15.2/` keys `you-hub` (Mob 6th row), `bar`, `mob-start`; fallback `app-walk-1018g/66-you.png`, `89-mobcard.png`, `90-mobstart.png`, `91-mob-created.png`.
- **R2:** "Mob tab, no Mob": "I can start a small group of friends or join one with a code."
- **Fail if:** other than five controls; labels differ; Mob needs a prior study week; the You row remains; Colleges or the repair count became unreachable; a deep link lands on a removed screen.

### D105: the bar becomes Today, Practice, Start, Mob, You
- **His words:** "Its own tab in the bar (Recommended)" (the option read: the bottom bar becomes Today, Practice, Start, Mob, You; Review moves into Practice as 'Your papers').
- **Decision:** D105, as above.
- **DONE WHEN (verbatim, G17):** the bar shows the five, and the Mob is one tap away on a fresh account.
- **Test / Proof / R4 / R2 / Fail if:** G17 steps 1-7. Extra: the Review tab is gone from the bar but "Your papers" is one tap inside Practice (G20 steps 1-2).

---

# GROUP A2a: onboarding and colleges (brief 02, branch ui/1019-a2a-onboard)

### G1: the first-open copy is broken English
- **His words:** "the text that shows on the Mockmob mascot is "1 light late 1 to 9, 2 minutes and sleep."" and "I don't know what kind of English this is."
- **Decision:** rewrite as full, grammatical, persuasive sentences (D84), keeping his Mobi-speech pattern. His own words about the headline: "Every last Mockmob has a pattern and it's fine", so the headline "Every lost mark has a pattern." may stay (G2 keep); PLAN's direction "Find the marks you are losing. Win them back before CUET." is a direction, not a demand.
- **DONE WHEN (verbatim):** no fragment or telegram English appears on any onboarding screen. A copy test bans dropped articles in these strings (list them).
- **Test (E1 FRESH; the Day pass and the Night pass; text 1.0 and 1.3):**
  1. `pm clear`, launch at the normal hour. Read the Mobi bubble, the headline, the support line. Then force the late-night hour (section 1.2) and read the late-night line, including the asleep state (1 to 5 AM) and the line after a tap on Mobi.
  2. Walk EVERY onboarding step and write every Mobi line and every sentence into `tmp/walk-1019/G1-strings.md`: `screen | string | full grammatical sentence? y/n`. Include the "arrive" lines (`mobiArrive`), the answer reactions ("About a second. Clean.", "Classic trap. Fix below."), "Now be harsh...", "Still yours to seal.", "Sealed. It's yours.", "Keep it with you.", the save step and the age sheet.
  3. Open the copy test and list its string set; check it covers every string in the table, not only the welcome.
  4. Check the bubble and support line do not clip at 1.3.
- **Proof to open:** `cand-app/G1_welcome_fresh_{night,day}.png`, `G1_welcome-late_fresh_night.png`, `G1_welcome-asleep-woken_fresh_night.png`, `tmp/walk-1019/G1-strings.md`, the copy test name.
- **R4:** before = `baseline-v15.2/n01-welcome.png`, `n02-welcome-mobi-woken.png`, `n02b-welcome-mobi-line.png` (already on disk; the late-night line "Late one tonight. Two minutes, then sleep." is in `n02b`).
- **R2:** "Welcome": "this wants me to tap Build my plan; it will take about two minutes."
- **Fail if:** any line lacks a verb or an article ("Late one tonight." as a bare fragment, "Classic trap." as a bare fragment); "yours" with no antecedent ("Let's find yours."); "Two minutes, then sleep" survives as a fragment; a string on a later step is clipped English while only the welcome was fixed.

### G2 KEEP: the first onboarding screen is fine
- **His words:** "The first onboarding screen is fine."
- **Decision:** KEEP. G1 changes strings only.
- **DONE WHEN:** none in PLAN-1019 (KEEP). Rule used: AUTOPILOT-GOAL section 7 ("the first onboarding screen").
- **Test (E1 FRESH; Night and Day):** screenshot the welcome. Overlay on the v15.2 welcome with the text blocks masked. The desk, lamp, window, Mobi pose, headline size, key shape and "I already have an account" link are unchanged. Mobi's three acts still play (waves; yawns from 11 PM; asleep from 1 AM until a tap wakes him). Returning-student variant: "Pick up my sheet" still shows after a partial sheet.
- **Proof to open:** `cand-app/G2_welcome-diff_fresh_{night,day}.png` (masked overlay, changed pixels outside the text boxes listed).
- **R4:** before = `baseline-v15.2/n01-welcome.png`. Any visual change outside the text is HIGH.
- **R2:** "Welcome": as G1.
- **Fail if:** layout, art, Mobi or key changed beyond the strings.

### G3: the college search keyboard (OWNER confirms on his phone)
- **His words:** "in every repo there is a search code option. I'm unable to search it. My keyboard gets cut off again and again." ("Scene F9" read as the colleges step; "(confirm)" in the ledger.)
- **Decision:** fix the keyboard and the search field so typing works and stays visible.
- **DONE WHEN (verbatim):** on the emulator at 360 dp, typing "hans" keeps the keyboard up and shows Hansraj. A widget test asserts the field keeps focus across rebuilds.
- **Test (E1 FRESH; Day pass and Night pass):**
  1. On the colleges step ("Which colleges would you say yes to tomorrow?"), tap "Find a college". Type "hans" one letter at a time, 150 ms apart (`adb -e shell input text h`, and so on). After every letter run `dumpsys input_method` and confirm `mInputShown=true`. Screenshot with the keyboard up: the field is fully visible above the keyboard and a Hansraj row is visible without scrolling beneath it.
  2. Clear (the X), type "lady", then "sri", then paste a long string and clear it. The keyboard never dismisses by itself; the results filter as you type.
  3. Tap a result: it is picked, no flicker, "N of 8 picked" updates.
  4. STRESS (the default emulator may not reproduce his phone, which is a vivo V2413): repeat step 1 on the short screen (`wm size 720x1280`), at text 1.3 and 1.6, and with the keyboard's suggestion strip on. Repeat while the ladder is animating.
  5. Every other search field in the app: the course sheet ("More courses"), the "More subjects" sheet, You > Plan college picker, the Colleges screen. Same checks.
  6. Widget test: open it and confirm it rebuilds the field's parent and asserts the same `FocusNode` still has focus.
  7. Before-fix proof: re-run steps 1 and 4 on the v15.2 PROFILE APK (the walker's `n08-onb-college-search-hans.png` shows the keyboard up with Hansraj visible on v15.2 in the default emulator, so that one shot did not reproduce his failure; say so, and let the stress variants decide).
- **Proof to open:** `cand-app/G3_search-hans_fresh_{night,day}.png` (keyboard up), `G3_search-stress-short_fresh_night.png`, `G3_search-t160_fresh_night.png`, `tmp/walk-1019/G3-ime-log.md` (the `mInputShown` line after every key), the widget test name. OWNER step: he types "hans" on his phone after the v15.3 install.
- **R4:** before = `baseline-v15.2/n07-onb-step2-colleges.png`, `n08-onb-college-search-hans.png`, `n09-onb-college-search-keytaps.png`.
- **R2:** "Colleges step": "I type a college name and pick it; I can also skip."
- **Fail if:** the keyboard drops after any key; the field or the first result hides under the keyboard on any variant; focus is lost after a rebuild; another search field in the app still misbehaves.

### G4: course list order
- **His words:** "what is BA Honors Business Economics? Is this the top course in DU? I don't think so."
- **Decision:** lead with what aspirants choose most; never call a course "top".
- **DONE WHEN (verbatim):** the list shows that order, and a test pins the order.
- **Test (E1 FRESH; Night and Day):** from the course chip's pencil, read the six most-chosen course tiles top to bottom, then open "More courses". Expect: **B.Com (Hons), BA (Hons) Economics, B.Com, BMS, BBA (FIA), BA (Hons) Business Economics**, then the rest. No tile or row says "top", "best" or implies a rank. Same order in You > Plan's course picker and the Colleges course filter. Open the test: it pins these six.
- **Proof to open:** `cand-app/G4_course-tiles_fresh_{night,day}.png`, `G4_more-courses_fresh_night.png`, the test name.
- **R4:** before = `baseline-v15.2/n05-onb-step2-course.png`, `n06-onb-step2-course-scrolled.png` (fallback `app-walk-1018c/03a-ob-courses-s1.png`).
- **R2:** "Course picker": "I choose the course I am aiming for."
- **Fail if:** the order differs; a "top" or "best" label exists; the order differs between onboarding and You.

### G5 ANSWER: more than one target course
- **His words:** "What if someone wants to select multiple courses they are targeting? Not a necessary feature to add, but just a question."
- **Decision:** not now. One target course; changeable any time in You > Plan; colleges can span courses later.
- **DONE WHEN:** none in PLAN-1019 (an answer). Brief 02's rule: "make sure the course step and You > Plan say plainly that the course can be changed any time."
- **How to show the answer:**
  1. FRESH, course step: a plain line says the course can be changed any time (record its exact words).
  2. FRESH, You > Plan: change the course from B.Com (Hons) to BA (Hons) Economics and back. Colleges, numbers and Today follow the new course without a restart.
  3. Draft reply for MESSAGE-1019.md: "You can aim at one course for now, and you can change it any time in You, Plan. Picking colleges across several courses is a later feature."
- **Proof to open:** `cand-app/G5_course-note_fresh_*`, `G5_plan-change-course_fresh_*`, the draft reply line.
- **R4:** before = `baseline-v15.2/` key `plan` (fallback `app-walk-1018g/69-plan.png`).
- **R2:** "Course step note": "I am not stuck with this choice."
- **Fail if:** the note is missing; changing the course leaves stale colleges or numbers.

### G6: college order by real cutoff data, with the number shown
- **His words:** "Usually it is SICC, then Hindu, then Hansraj, then LSR." (SICC read as SRCC.) His choice: "Real cutoff data, shown (Recommended)".
- **Decision:** D103: order by last year's real closing marks for the course and category, number beside each row.
- **DONE WHEN (verbatim):** the order matches the data, and every row shows its number.
- **Test (P first, no emulator; then E1 FRESH):**
  1. P: A2a's report names the source file and its provenance (`du_2026_data.dart`, "Lowest Round 1 score in 2026, out of 1000"). Open it. For B.Com (Hons), unreserved, list SRCC, Hindu, Hansraj, LSR, Kirori Mal, Ramjas and any other college that is often picked, with numbers. Compute the expected descending order. Say plainly whether his belief (SRCC, Hindu, Hansraj, LSR) holds. Repeat for BA (Hons) Economics and one reserved category.
  2. E1: on the colleges step pick colleges in a scrambled order (LSR, Hansraj, SRCC, Hindu, Ramjas). The ladder and the picked list show the data's order and every row carries its number (a plain separator, no middle dot if the copy rules ban it). A college with no number for that course and category says so plainly and sorts last.
  3. Change the course chip and the category menu: order and numbers change with them.
  4. Same order and same numbers on every screen that lists the picks: onboarding, Today's card and its sheet, You > Plan, the Colleges screen.
  5. Year label: rows say "last year" only if the data is last year's admission cycle (the file says 2026); never "2025" over 2026 data.
- **Proof to open:** `tmp/walk-1019/G6-data-table.md` (college, number, source file and line, expected rank, shown rank), `cand-app/G6_ladder-scrambled-pick_fresh_*`, `G6_picked-list_fresh_*`.
- **Answer for MESSAGE-1019.md:** his order against the real numbers, in plain words ("For B.Com (Hons), unreserved, last year's lowest Round 1 scores were: SRCC x, Hindu y, Hansraj z, LSR w").
- **R4:** before = `baseline-v15.2/n07-onb-step2-colleges.png` (shows SRCC 924.3 above Hindu 919.9 and Hansraj 907.5).
- **R2:** "Colleges step": "the higher the number, the harder the college; I pick the ones I would say yes to."
- **Fail if:** any number cannot be traced to the source file and line; any row lacks a number; the order differs between screens; the order ignores the course or category; a hard-coded order is left in the code.

### D103: colleges ordered by last year's real closing marks, number shown
- **His words:** "Real cutoff data, shown (Recommended)".
- **Decision:** D103, as above.
- **DONE WHEN (verbatim, G6):** the order matches the data, and every row shows its number.
- **Test / Proof / R4 / R2 / Fail if:** G6 steps 1-5.

### G8 ANSWER: removing a chosen subject
- **His words:** "Once I have selected subjects, how do I remove? Never mind."
- **Decision:** no action; he found it.
- **DONE WHEN:** none (no action). Check it still works so the answer stays true.
- **How to show the answer (E1 FRESH):** on the subjects step tap a ticked subject (or a ticked common set's chip): it unticks and Mobi does not scold. Also remove a subject in You > Subjects and in Practice "Edit subjects".
- **Proof to open:** `cand-app/G8_untick_fresh_*`, `G8_you-remove-subject_fresh_*`.
- **R4:** before = `baseline-v15.2/` key `subjects` (fallback `app-walk-1018g/08-subjects.png`, `09-set.png`).
- **R2:** "Subjects step": "tap again to take one off."
- **Fail if:** removing a subject stopped working or loses other picks.

### G9: the subject rule up front, with the common sets
- **His words:** "BCom Honors also needs a language such as English and two other subjects ... Not a necessary feature at all, but just a better touch." and "You have also added common picks, that's great."
- **Decision:** show the course's rule as one line before the first pick, with the common sets as one-tap chips. KEEP the sets and picks.
- **DONE WHEN (verbatim):** the line shows before the first pick.
- **Test (E1 FRESH; Day pass and Night pass; 1.3 text):**
  1. Arrive on the subjects step and screenshot BEFORE touching anything: one line such as "B.Com (Hons) needs a language, usually English, plus 3 subjects such as Accountancy, Business Studies and Economics or Maths", and the course's common sets as chips.
  2. Go back, change the course to BA (Hons) Economics, return: the line changes with the course (it is not generic).
  3. Tap a set chip: the subjects tick, Mobi says the rating line ("Now be harsh. Tap Shaky...", unless reworded for G1), the picks work as before.
- **Proof to open:** `cand-app/G9_rule-before-pick_fresh_{night,day}.png`, `G9_rule-other-course_fresh_night.png`, `G9_set-chip-tapped_fresh_night.png`.
- **R4:** before = `baseline-v15.2/` key `subjects-before` (fallback `app-walk-1018g/08-subjects.png`, `10-set-top.png`).
- **R2:** "Subjects step": "I need a language plus three; I can tap a ready-made set."
- **Fail if:** the line appears only after a pick; it is the same for every course; it clips; the common sets or picks were removed.

---

# GROUP A2b: app Today and the deck (brief 03, branch ui/1019-a2b-today)

### G7: the colleges on Today
- **His words:** "the first three colleges that I select show on Today and the fourth college shows nothing." His choice: "Top 3, labelled, plus 'all 5' (Recommended)".
- **Decision:** D104: Today shows the 3 hardest-to-reach picked colleges labelled "Your top 3 of N", plus "See all N".
- **DONE WHEN (verbatim):** with 5 colleges, Today shows 3 plus "See all 5", and the sheet lists 5.
- **Test (E1 FRESH with 5 colleges picked; E3 HEAVY):**
  1. Pick 5 colleges in onboarding, reach Today (Night, then Day): the colleges card header reads "Your top 3 of 5", shows 3 rows (the 3 hardest by last year's closing marks, the same order as G6) and a "See all 5" row.
  2. Tap "See all 5": a sheet lists all 5 with the marks each needs and the gap. Recompute one gap by hand from the number shown and the student's current figure; it matches.
  3. Add and remove colleges in You > Plan to reach 2, 3 and 8 (max 8): the header and the "See all" row follow ("Your top 3 of 8" with "See all 8"; with 2 or 3 the wording stays true and no empty "see all"). Unit tests cover 2, 3, 5 and 8.
  4. Old copy: the line "The first 3 show on Today" (`colleges_copy.dart` lines 14 and 71) and the "On Today" marks on the first three rows of the onboarding ladder (`college_ladder.dart` line 19) are gone or rewritten to the new rule.
  5. At text 1.3 the sheet scrolls and no row is lost.
- **Proof to open:** `cand-app/G7_today-colleges-5_fresh_{night,day}.png`, `G7_see-all-sheet_fresh_*`, `G7_today-colleges-8_heavy_night.png`, `G7_onboarding-ladder-copy_fresh_night.png`, the unit test names.
- **Answer for MESSAGE-1019.md:** "Today showed three because the card was built for three. It now says Your top 3 of N and opens all N."
- **R4:** before = `baseline-v15.2/` key `today-colleges` (fallback `app-walk-1018g/36-today-loaded.png`).
- **R2:** "Today's colleges card": "these are my hardest colleges; tap to see all of them."
- **Fail if:** a college silently disappears; "of N" is wrong; stale "first three" copy remains; the sheet lacks the marks or the gap.

### D104: Today shows "Your top 3 of N" with "See all N"
- **His words:** "Top 3, labelled, plus 'all 5' (Recommended)".
- **Decision:** D104, as above.
- **DONE WHEN (verbatim, G7):** with 5 colleges, Today shows 3 plus "See all 5", and the sheet lists 5.
- **Test / Proof / R4 / R2 / Fail if:** G7 steps 1-5.

### G12: the Suggested deck on a fresh account
- **His words:** ""Suggested for you" in a fresh account with the mapped subjects is just showing one option, like English full mock." and "it can show at least 3 or 4 cards before showing nothing else."
- **Decision:** a fresh account with subjects always gets at least 4 real cards built from its subjects; honest copy; a calm card.
- **DONE WHEN (verbatim):** a fresh account's deck has at least 4 cards, every line is grammatical, and a test builds the deck from an empty history.
- **Test (E1 FRESH with 3 or more subjects; E3 HEAVY; Night and Day):**
  1. Today > "Suggested for you". Count the cards by pressing "Up next" or "Not now" one at a time. Expect at least 4 before the end card, in this order: (1) a quick 10 in the subject he rated weakest ("Shaky") in onboarding; (2) a full mock in his first domain subject; (3) an English quick 10 (or his language); (4) the Mob ("Sit the same paper as your friends"); (5) another subject when there is room. Each shows its cost and time truthfully. A Pro-only card, if any, is visible but locked, never priced.
  2. Pass a card (Not now): the line reads like "Moved to the back. You will see it again after the others." (or equal, grammatical and true). The old "You passed this one" and "it waits" lines are gone.
  3. Reach the end card: "You've seen all 4. Go through them again, or see every way to practise." The number in the line equals the deck's real size (v15.2 said "That's all three for today"). The "Go through them again" key and "See every way to practise" both work.
  4. The full-mock card: record 3 s. The stopwatch (`SuggestedArt.stopwatch`) does not tick or sweep; it is a calm static icon or gone. In reduced motion it is still.
  5. HEAVY: record-based cards (repair, revise, weakest chapter) still lead; total at least 4 or as many as exist.
  6. A one-subject account (unit test) still gets a sensible deck.
- **Proof to open:** `cand-app/G12_deck-card-1..N_fresh_{night,day}.png`, `G12_deck-pass-line_fresh_night.png`, `G12_deck-end_fresh_{night,day}.png`, `frames/G12/` (the clock card, 3 s), the deck-from-empty-history test name and its 1, 3, 5 subject cases.
- **R4:** before = `baseline-v15.2/` keys `today-deck-*` and `today-deck-end` (fallback `app-walk-1018g/37-deck.png`, `38-demo-1..3.png`, `42-deck2.png`, `43-notnow.png`, `55-end.png`).
- **R2:** "Suggested for you": "each card is a thing I can do next; I can do it or skip it."
- **Fail if:** fewer than 4 cards on a fresh account; a duplicate card; a card for a mode the student cannot start; any ungrammatical or false count; the clock still moves; swipe v2 (D94: Up next / Not now, buttons under the deck, first-time demo, undo) changed.

### G13: the "Do this next" accepted animation
- **His words:** "The animation when something gets accepted, like "Do this next," comes on top. Maybe, if you can, make it a bit better."
- **Decision:** one continuous, calm spring: lift, travel, settle.
- **DONE WHEN (verbatim):** the frame sequence shows a single continuous move.
- **Test (E1 FRESH, E3 HEAVY):**
  1. On the deck tap "Up next" on the second card (then once by swipe right). Record 6 s from just before the tap. Extract frames; take timestamps from the video.
  2. Measure: start frame (first movement) and end frame (settled) give 350 to 450 ms; the card lifts to scale 1.0 to 1.03 with a stronger shadow; it travels to the lead slot in ONE spring with overshoot of at most 4% of the travel distance (read the card's top edge in pixels per frame); the old lead card settles without a snap or blink; no frame shows a duplicate or a missing card; positions rise and settle with a single peak (no second bounce).
  3. Reduced motion (`animator_duration_scale 0`): a crossfade, no travel.
  4. Compare with v15.2's own timing (`suggested_stack.dart` drives a fly controller of 340 ms and an arrive controller of 360 ms; read the frames to see whether they run one after the other, which would read as two moves) and with the tokens in `lib/core/motion/motion.dart` and docs/brain/MOTION.md.
- **Proof to open:** `frames/G13/` (contact sheet, every frame opened) and `frames/G13/timing.md` (duration, peak scale, overshoot %, number of peaks), plus the reduced-motion clip frames.
- **R4:** before = `tmp/app-walk-1018/clip-today-swap.mp4` and `clip-reel-not-now.mp4` (v15.1-era), `baseline-v15.2/` accept stills (fallback `app-walk-1018g/39-drag-right.png`, `40-after-right.png`, `44-upnext-btn.png`).
- **R2:** "After tapping Up next": "the card I chose moved up to Do this next."
- **Fail if:** two phases; duration outside 350-450 ms; peak scale above 1.03; overshoot above 4%; a visible jump; reduced motion still travels.

### G14 KEEP: Today is good
- **His words:** "the today page is good, and some parts have been good."
- **Decision:** KEEP. Only the allowed changes touch Today: the colleges card (G7), the deck (G12, G13), A5's single progress card (G19), the Mob card condition (G17).
- **DONE WHEN:** none in PLAN-1019 (KEEP). Rule used: AUTOPILOT-GOAL section 7 ("the app's UI direction and Today").
- **Test (E1 FRESH, E3 HEAVY; Night and Day):** scroll Today top to bottom in steps and make a montage; do the same on v15.2. List every block in both. The week strip, the hero "Do this next", the milestones, the Start card, glass, spacing and type are unchanged apart from the four allowed changes.
- **Proof to open:** `cand-app/G14_today-scroll-1..N_{fresh,heavy}_{night,day}.png`, `r4/G14_today-montage_before-after_{night,day}.png`.
- **R4:** before = `baseline-v15.2/` key `today` (fallback `app-walk-1018g/28-today.png`, `36-today-loaded.png`, the `52-scroll-1..11.png` set).
- **R2:** "Today": "this is my plan for today; the big card is the next thing to do."
- **Fail if:** any block lost, reordered or restyled beyond the four allowed changes (HIGH).

---

# GROUP A3: result and "Your papers" (brief 04, branch ui/1019-a3-result)

### G20: Review becomes Practice > Your papers
- **His words:** "Even the review section is very cluttered and doesn't show the recent mocks. First, it's hard to check even after the mock is given. There should be a clear path through the history and all." His choice: "Papers first, then mistakes (Recommended)".
- **Decision:** D106: Review lives inside Practice as "Your papers": stats strip, subject filter, papers newest first (a tap opens the result and answers), then "Mistakes to repair" by chapter.
- **DONE WHEN (verbatim):** a fresh account after 1 paper sees it at the top, and a heavy account filters by subject.
- **Test (E2 FRESH, E3 HEAVY; Night and Day; HEAVY also at 1.3):**
  1. **Structure (A1):** the Practice tab has a clear "Your papers" entry; it opens the screen. Review is not a bar item. Old routes (the Review deep link, the result screen's "See this paper", notifications) land on it. The open-repairs count is still visible from the Practice tab.
  2. **FRESH, no papers:** the screen shows a friendly first step ("Sit your first paper", one key), never an empty page.
  3. **FRESH, after the 10-question paper (E2):** from the result tap "See this paper": it lands on Your papers with that paper's row at the top. Top to bottom: (a) stats strip: papers sat 1, latest marks with a trend (with one paper there is no trend arrow and no fake "0"), open repairs; (b) subject chips (with a scroll cue if they overflow); (c) "Your papers" newest first, each row = paper name, subject, marks out of the maximum, date and time in 12-hour form ("10:11 PM"); (d) "Mistakes to repair" by chapter.
  4. **HEAVY:** tap a subject chip: only that subject's rows remain; "All" resets. The strip says whether it shows all papers or the filter. Tap two rows (a quick set and a full mock): each opens its own result and answers (check marks and date against the row). Recent full mocks appear in the list.
  5. **Numbers agree:** fill `tmp/walk-1019/G20-numbers.md`: papers sat, full mocks, open repairs, as shown on Your papers (strip, rows, chapter list), Practice's repairs row, You ("N full mocks landed") and Today. They are equal, or each carries a label that says why they differ ("tonight" against "all").
  6. A chapter whose header would read "Nothing left to repair" is never the auto-opened one.
  7. Above the fold at 360 x 800 holds the strip, the chips and the first rows, nothing else.
- **Proof to open:** `cand-app/G20_papers-empty_fresh_*`, `G20_papers-1paper_fresh_*`, `G20_papers-heavy_heavy_*`, `G20_papers-filter-<subject>_heavy_*`, `G20_row-opens-result_heavy_*`, `G20_practice-entry_fresh_*`, `tmp/walk-1019/G20-numbers.md`.
- **R4:** before = `baseline-v15.2/` keys `review-fresh`, `review-heavy` (fallback `app-walk-1018g/59-review.png`, `60-repair.png`).
- **R2:** "Your papers": "this is the list of papers I have sat; tap one to see it."
- **Fail if:** not newest first; 24-hour time; marks without the maximum; a row opens the wrong paper; filter missing or wrong; clutter above the fold; numbers disagree unlabelled; the D18 "leads with weak chapters" value lost inside Mistakes.
- **Web twin:** the same order on the web is proved in G25 (A4b).

### D106: Your papers: stats strip, subject filter, papers newest first, then mistakes by chapter
- **His words:** "Papers first, then mistakes (Recommended)".
- **Decision:** D106, as above (app in A3, web in A4b).
- **DONE WHEN (verbatim, G20):** a fresh account after 1 paper sees it at the top, and a heavy account filters by subject.
- **Test / Proof / R4 / R2 / Fail if:** G20 (app) and G25 (web).

### G22: the moment after Submit (OWNER confirms on his phone)
- **His words:** "after completing, there is no message animation, and the overall result screen feels very weak on mobile." and "How has this result screen regressed so much?" His choice: "Restore the reveal, then refine (Recommended)".
- **Decision:** D108: restore the approved reveal exactly (68f63c11), then a completion line, marks counting up, one next move; then refine on a phone.
- **DONE WHEN (verbatim):** the frame sequence matches the approved reveal, and he sees the moment on his phone.
- **Test (E2 FRESH: a 10-question Quick; E3 HEAVY: a full mock; Night, plus Day for the end state):**
  1. FRESH: start a 10-question Quick practice (10 credits), answer all, tap Submit. Record from 1 s before Submit until 8 s after. Extract frames with video timestamps.
  2. The sequence must match the approved FinishStage (68f63c11): (a) the sheet inks in bubble by bubble, about 40 ms apart (10 bubbles take about 400 ms; the cap is 800 ms), then a 200 ms lead; (b) the figure counts up with each right answer and is stamped (it starts at scale 1.12 and holds until 80 ms, falls to 1.0 at the landing 240 ms into the 840 ms stamp, and has settled by 420 ms; the ring and shards of a good set run to 840 ms); (c) a good set gets one ring and 14 shards, a mixed set gets the stamp alone and Mobi's calm line, never sad; (d) Mobi reacts 160 ms after the landing; (e) a tap anywhere skips to the end state. Measure each against these numbers (tolerance 15%).
  3. Then the new layer: a completion line like "Paper saved. 7 of 10 right." (true numbers, matching the result); the marks counting up for 600 to 900 ms with an ease-out and tabular figures (no horizontal jitter of digits); ONE dominant next-move key; a "See this paper" link (G20).
  4. "Paper saved" is true: with the server unreachable at Submit (remove the 3101 reverse) the line must NOT say "Paper saved"; it says the paper is kept on the phone and will sync; after the reverse is back it flips to saved. (Use a 5-question paper for this second run.)
  5. Celebrations setting (You > Appearance): Full (ring, shards, Mobi), Quiet (ink, count and stamp only), Off (end state at once, with the words). Reduced motion: end state or a short fade.
  6. Above the fold at 360 x 800: back, the completion line, the big marks, one primary key, "See this paper". Nothing else.
  7. Goldens: the candidate's finish goldens at 0, 400 and 900 ms (Day and Night) equal 68f63c11's `finish_*` goldens, apart from the new layer below the stamp.
  8. HEAVY full mock (50 credits; answer 3, then Submit): sealed sheet, then the 4-card recap, then the full result with Mobi's reveal beside the score and the count-up on first open. All three still play. Record them.
- **Proof to open:** `frames/G22/practice/` and `timing.md` (each beat's measured time against the approved number), `frames/G22/mock/`, `cand-app/G22_result-abovefold_fresh_{night,day}.png`, `G22_offline-line_fresh_night.png`, the golden diff, the unit tests by name ("Paper saved" only after the save).
- **R4:** before = `tmp/app-walk-1018/clip-submit-reveal.mp4`, `clip-finish-to-today.mp4`, `clip-mock-reveal.mp4` (v15.1-era), `baseline-v15.2/` result shots (fallback `app-walk-1018g/83-submit.png`, `84-result.png`); approved = the 68f63c11 goldens and `finish_stage.dart`.
- **R2:** "Result": "I finished; here is my score and the one thing to do next."
- **Fail if:** `FinishStage` is not mounted; any beat deviates more than 15% from the approved timing; "Paper saved" appears before the save is confirmed; the count-up is not tabular or runs over 900 ms; two competing next moves; clutter above the fold; Celebrations ignored. OWNER step: he sees it on his phone after the v15.3 install.

### D108: restore the reveal, then refine
- **His words:** "Restore the reveal, then refine (Recommended)".
- **Decision:** D108, as above (approved reveal from 68f63c11; then a short completion line, marks counting up, one next move).
- **DONE WHEN (verbatim, G22):** the frame sequence matches the approved reveal, and he sees the moment on his phone.
- **Test / Proof / R4 / R2 / Fail if:** G22 steps 1-8.

---

# GROUP A5: the range (brief 05, branch ui/1019-a5-range)

### G18: "type your own range" and the goal check
- **His words:** "Even if I write 900 to 920, it shows "Your goal is 0 out of 4 clear," but then it shows "Within your range" after I exit."
- **Decision:** one rule everywhere. A college is **safe** when the range's LOW end clears it and **in reach** when only the HIGH end does. The headline and the rows use the same words ("2 safe, 2 in reach of 4").
- **DONE WHEN (verbatim):** unit tests cover 900-920, 910-920, "900 to 920", 920-900 and a gap of 250, and the onboarding screen and Today agree.
- **Test (E2 FRESH, E3 HEAVY; Night and Day):**
  1. Entry: Colleges screen (from Today's colleges card or You) > "Type your own" (also the programme screen). Enter From 900 and To 920 against the student's four colleges. Write the four cutoffs. Compute by hand: safe if low >= cutoff, in reach if high >= cutoff > low, otherwise "needs X more". The headline counts equal the rows' words exactly ("N safe, M in reach of 4").
  2. Repeat for 910 to 920, 912.5 to 920, 920 to 900 (swaps silently to 900 to 920), and a gap of 250 (for example 700 to 950): refused with a plain message that keeps the typed numbers. Out of 0 to 1000 (for example 990 to 1100) is refused plainly. If the sheet accepts a single text field, also "900 to 920", "900-920" and the en dash "900–920".
  3. Tap "Use as my estimate", exit, return: the Colleges screen, Today's colleges card, You > Plan's range row and the programme screen's line ("Your estimate clears ... within your range" in `programmeStands`) all read the same parsed value and the same words. No "0 of 4 clear" next to "Within your range".
  4. grep the strings: the old wording ("of N clear", "Within your range", "more are within the range") must not survive beside the new words anywhere in the app.
  5. The keyboard never hides the From and To fields (see G3).
- **Proof to open:** `cand-app/G18_900-920_{fresh,heavy}_{night,day}.png`, `G18_910-920_*`, `G18_reversed_*`, `G18_gap250-message_*`, `G18_today-agrees_*`, `G18_plan-agrees_*`, `tmp/walk-1019/G18-hand-calc.md` (cutoffs, expected words, shown words), the unit test names.
- **R4:** before = the v15.2 failure, captured on the v15.2 APK with the same keystrokes (900 and 920 give "0 of 4 clear" with "Within your range" rows); no baseline shot exists yet, so capture it (fallback key `baseline-v15.2/` `estimate-900-920`).
- **R2:** "Type your own range": "I tell it the marks I am aiming for; it shows which colleges that reaches."
- **Fail if:** any headline and row disagree; a wide range fails while a narrow one works; the error message blames the student ("Invalid input"); a screen after exit shows different words or counts.

### G19: "I don't know my range yet"
- **His words:** "There can be a feature like "I don't know my range," where we can test the range by giving 5 NTA mocks" and (his choice) "Your first direction is fine for estimating after 5 full mocks, but it should show 1 mock for each subject like that."
- **Decision:** D109: estimate after one full mock for EACH subject of the student's set, with progress per subject; then the estimated range with the colleges it reaches, which the student can accept.
- **DONE WHEN (verbatim):** the flow works on a fresh account with fixtures, and the copy is honest.
- **Test (E2 FRESH; E3 HEAVY; Night and Day):**
  1. In the estimate sheet's source switch and in You > Plan, find the choice "I don't know my range yet". Choose it on the FRESH account. Today shows ONE progress card: "Sit one full mock in each subject and we'll estimate your range: English done, Accountancy done, Economics next." Use the account's real subjects, in the order of its set; each subject reads done, next or to do.
  2. The key "Sit one" opens that subject's full mock start (do not run it; read the cost line, "Uses 50 of your N credits").
  3. Fixtures, no emulator time: top up the FRESH account's credits on STAGING only (service role; never production), then sit one full mock per subject through the rig (`take.mjs <subject> full 50` and `finish.mjs <view.json> <blanks>`), two subjects first. Reopen the app: the card shows the right done and next subjects. Then sit the rest: the card is replaced by the estimated range.
  4. The estimate: the range is the summed subject estimate with its spread, always a range, never a lone number, labelled "estimate from your N mocks" (N = the real count), with the colleges it reaches in the G18 words (safe and in reach), and two keys: accept it as my range, or keep going. Recompute by hand from the attempt marks (`node --use-system-ca tmp/rig-1016e/state.mjs`) with the formula in `estimate.dart` (`EstimateSource.mocks`; "Raw marks, out of 250 a paper. Your last 3 mocks in each paper set the range."). The shown figures equal the hand figures to the mark.
  5. Accept: You > Plan's range row, Today and the Colleges screen show the accepted range and agree (G18). Keep going: the card stays.
  6. Consistency: the existing line "Full mocks in N of the 4 papers DU counts." in the estimate sheet must not contradict the card (the card counts subjects of the student's set; DU counts four papers). Record both numbers and say which the student sees where.
  7. HEAVY: with a full mock in every subject the estimate shows at once; with one subject missing the card shows that subject as next.
  8. Honesty: no "your score will be", no "predicted"; the spread is visible. Cost honesty: a fresh Free student starts near 90 credits and a full mock costs 50, so five mocks cannot be sat on the free start; the card or the "Sit one" sheet must say what a mock costs, and this must be written up for the owner (MESSAGE-1019.md "what is left").
  9. Unit tests: 1, 3 and 5 subjects; partial progress; done.
- **Proof to open:** `cand-app/G19_choice_fresh_*`, `G19_card-0-of-N_fresh_{night,day}`, `G19_card-partial_fresh_*`, `G19_estimate-ready_fresh_*`, `G19_accepted-agree_fresh_*`, `G19_estimate-ready_heavy_*`, `tmp/walk-1019/G19-hand-calc.md`, the rig command log, the unit test names.
- **R4:** before = Today and the estimate sheet at v15.2 (baseline keys `today-top-fresh` and `estimate`); the new card must not disturb the rest of Today (G14).
- **R2:** "Progress card": "it wants me to sit one full mock in each subject, one at a time; it shows which is next."
- **Fail if:** the card shows for a student who typed a range; a quick set or a repeat of one subject counts as done; the estimate shows before every subject is done; the range has no spread or is worded as certain; "Sit one" starts the wrong subject; the card stays after accepting; the cost is hidden.

### D109: "I don't know my range": estimate after one full mock per subject
- **His words:** "Your first direction is fine for estimating after 5 full mocks, but it should show 1 mock for each subject like that."
- **Decision:** D109, as above.
- **DONE WHEN (verbatim, G19):** the flow works on a fresh account with fixtures, and the copy is honest.
- **Test / Proof / R4 / R2 / Fail if:** G19 steps 1-9.

---

# GROUP A4a: web polish restore (brief 06, branch web/1019-a4a-polish)

### G28: the website "feels like an older version" (gradients, textures, the NTA button)
- **His words:** "I honestly don't know what has happened on the website, like textures and gradients from many places. This feels like an older version to me." and "The full mockup NTA mode ... should be like a button, and the gradient and all are gone."
- **Decision:** restore exactly what FORENSICS finds removed, keeping later fixes; his taste note: Night glow stays subtle (restore the NTA gradient button-card, the volt keycap and the card edge lights and textures, not a page-wide glow).
- **DONE WHEN:** none in PLAN-1019 (SPEC only). SPEC, verbatim: "restore exactly what FORENSICS.md finds removed (the sha and files), including the Full mock / NTA mode gradient button and the textures. Then run R4 (side-by-side with the release that had them)."
- **Test (W1: dev server, 390 and 1440, Night and Day):**
  1. `/preview/arena?view=dashboard&plan=free&data=ready&catalog=full` (Practice). The NTA control is a button-card again (`pr-tile pr-nta mk-rim`, kicker "Closest to exam day", the console picture). Computed style check in the page: its `background-image` contains `linear-gradient(135deg` with `--a-volt-wash` to transparent at 55%; the selected-tile wash and the `.pr-nta__more` gradient are back (c9662f67^ `practice.css` lines 42, 125, 216, 249; `arena.css` line 1318). It reads as pressable (hover lift, press, focus ring).
  2. `btn-volt` keys have the edge, sheen and a subtle glow back; `.na__cta` has its lean-in and glow on hover (fine pointer only).
  3. Card and sheet edge lights are back; textures stay (`--pr-grain` on Practice).
  4. For each file FORENSICS names, list the gradient lines removed in c9662f67, 09421b29, 06285f1a, fb73dccd and 89ed9905 and mark each as restored or deliberately left with a reason: `arena.css`, `practice.css`, `features/page.js`, `pricing/prepos/page.js`, `start.css`, Account, Credits, Compass, Combo planner, Leaderboard, `PrepOSOrb.jsx`, `marketing-theme.css`, `AIRivalArena.jsx`, the theme toggle sky, `hero-depth.css`.
  5. Landing aurora (removed by 706b1fe9 under L-019): either restored in a way L-016 and L-019 allow (no drifting blob, no gradient text) or left with a stated reason. Run the landing L-item suite; it must still pass.
  6. No page-wide glow in Night.
  7. Count `gradient(` in CSS: release 10 has 168 (1015-night 165, 1016-batch 167). The candidate is not lower than 168 and the named lines are back. Report the number.
  8. Visit: Practice, Today, the Start sheet, Account (`view=profile`), Wallet, Compass (`view=compass`), Leaderboard (`view=ranks`), `/features`, the pricing page, `/`.
  9. Answer for MESSAGE-1019.md: which commit removed what and when (c9662f67, 16 Oct 3:25 am, "Arena de-slop A1"; 09421b29, 16 Oct 8:44 am; 706b1fe9, 18 Oct).
- **Proof to open:** `cand-web/G28_<page>-<state>_{390,1440}_{night,day}.png` for the pages in step 8, `r4/G28_*_three-way.png` (release 10, the lit build at 77713336, the candidate), `tmp/walk-1019/G28-restore-table.md` (one row per removed line: file, sha, restored y/n, reason), the computed-style log.
- **R4:** before = `baseline-web-r10/` Practice and Today (`dashboard`/`today` keys) AND the lit build at 77713336 (preview on 3502). The candidate must look at least as lit as the lit build on these screens without a page-wide glow. Any gradient, texture or key that the lit build had and the candidate lacks is HIGH.
- **R2:** "Practice (web)": "pick a subject, then a mode; the NTA button is the exam-day screen."
- **Fail if:** the NTA control is still a plain tile; keys are flat; a page-wide glow appears; a drifting aurora returns; a restored file undid a later fix.

### G31: animations feel faster and less refined
- **His words:** "I don't know why I feel like all the animations inside Mockmob have changed and feel, to me, faster... It doesn't feel to me as refined and polished as they were previously."
- **Decision:** restore the approved motion tokens where they were shortened (unless the ledger shows he asked): count-up, stagger, springs, keycap press.
- **DONE WHEN:** none in PLAN-1019 (SPEC only). SPEC, verbatim: "One motion token file is the single source."
- **Test (W1):**
  1. Tokens: read `src/app/motion-kit.css`. `--mm-dur-count-up` is 720 ms (release 10: 420 ms from 9d28148b). `grep -rn "dur-count-up" src` shows ONE definition. List every hard-coded duration in CSS that bypasses a token (count before and after).
  2. Count-up frames: on `view=result` and `view=progress`, sample a number's text with the rAF sampler through its count-up: total 720 ms (tolerance 40 ms). Release 10 is 420.
  3. Stagger: on a page open (`view=today`, `view=dashboard`) sample each child's opacity and transform: the children rise one after another about 45 ms apart (1015-night), not "one lead and the rest fade together at 160 ms" (release 10, dbb80d00).
  4. Springs: a key press and release, the dock pill, the sidebar pill: the livelier spring on keys, pills and the dock (`cubic-bezier(.34, 1.56, .64, 1)` over 420 ms, 1015-night) or an agreed calm value with a ledger line; measure the overshoot. The keycap press edge is back (c9662f67).
  5. Before each restored value the verifier reads `OWNER-MASTER-LEDGER.md` and the owner files for an instruction that asked for the change; at the time of writing a search of the master ledger, the taste profile and the 15-18 Oct owner files for "overshoot", "Q11" and "count-up" found no such instruction.
  6. Reduced motion (`mm:motion:v1=reduced`): entrances become a 160 ms fade; no tilt, blink or clock (docs/brain/MOTION.md).
  7. Page transitions (dbb80d00's ViewTransition): no motion that the owner could read as "faster"; compare a navigation Today to Practice in frames.
- **Proof to open:** `frames/G31/count-up/timing.md` (candidate, release 10, lit build), `frames/G31/stagger/`, `frames/G31/spring/`, `cand-web/G31_tokens.txt` (the grep output), the ledger-check note.
- **R4:** before = release 10 (live) and `deploy/1015-night` 3fc0095b (springs and count-up) / 77713336 (count-up and stagger). Table: token, release 10, restore-from, candidate.
- **R2:** "Any page on open": "it settles calmly; nothing looks rushed."
- **Fail if:** count-up is not 720 ms; stagger still lead-only; the press edge missing; a token is defined twice; reduced motion no longer honoured.

---

# GROUP A4b: web account, Review, Practice, Start (brief 07, branch web/1019-a4b-ux)

### G25: the web Review: core stats gone, weird order, "I can't even access this properly"
- **His words:** "At the top, it's not showing the core statistics like it used to show, even in the review section" and "I can't even access this properly."
- **Decision:** restore the stats strip and shape Review as D106: strip, subject chips, Your papers newest first, then Mistakes to repair.
- **DONE WHEN:** none in PLAN-1019 (SPEC only). SPEC closing line, verbatim: "Fix whatever is broken ("I can't even access this properly"); reproduce it on preview fixtures and a staging account."
- **Test (W1 fixtures, W2 staging; 390 and 1440, Night and Day):**
  1. `/preview/arena?view=review&review=one` (FRESH after 1 paper), `review=student1018` (HEAVY, the default), `review=empty` (no papers), `review=done`, `review=nothing`, `review=allwrong`, `review=down`, `review=slow`.
  2. Order top to bottom: (a) the stats strip: papers sat, latest marks with a trend, open repairs; (b) the subject filter chips with a scroll cue; (c) "Your papers" newest first, each row = paper name, subject, marks out of the maximum, date in 12-hour form, tap opens that paper's result and answers; (d) "Mistakes to repair" by chapter. A chapter whose header reads "Nothing left to repair" is never the one that opens first (`review=done`, `review=nothing`).
  3. `review=empty` shows a friendly first step with one key, not an empty page. `review=down` and `review=slow` show a calm retry and a skeleton.
  4. Numbers agree between the strip, the rows and the chapters (`tmp/walk-1019/G25-numbers.md`).
  5. Access ("something is broken"): reach Review from the 1440 sidebar, the 390 dock or More sheet, a result page's link to the paper, and a deep link (`?pane=papers` if kept). All land on the same page without a blank state, a redirect loop or a console error. Read the console on every load.
  6. W2: a NEW staging test student sits a quick paper through the rig; Review on the real data shows the paper at the top; the row opens its result; a heavy student filters by subject.
- **Proof to open:** `cand-web/G25_review-<fixture>_{390,1440}_{night,day}.png`, `G25_review-signedin_{390,1440}_*`, `tmp/walk-1019/G25-numbers.md`, the console logs.
- **R4:** before = `baseline-web-r10/review-*` (fallback `tmp/feedback-1019/a4b/explore-base-review-*` and `explore-base-review-one-*`, 390 and 1440 dark) and the old layout at ad381711 (`ReceiptStrip`, papers view).
- **R2:** "Review": "my papers, newest first; below them, the mistakes to fix."
- **Fail if:** the strip is absent; chapters come before papers; no filter; unlabelled disagreeing numbers; "Nothing left to repair" opens first; a route that blanks.

### G26: Practice selector shows "5 questions ... Biology" instead of the mode
- **His words:** "instead of showing the mode on top whenever I select a subject, in the practice mode, it's showing 5 questions to the pen in biology."
- **Decision:** the mode and length selection stay where the student is; the summary lives only in the start key ("Start 5 questions in Biology").
- **DONE WHEN:** none in PLAN-1019 (SPEC only). SPEC closing line, verbatim: "Show the summary only in the start key ("Start 5 questions in Biology")."
- **Surface is unconfirmed** (NOW.md asks him). Test every candidate surface; the pass rule applies to each: after picking a subject the top of the surface still names the MODE, and the count and subject appear only in the start key.
  1. Web Practice, `?view=dashboard&catalog=full` at 1440: pick Biology, Quick, 5. The right-hand ticket's lead line is the mode ("Quick practice"); `pr-ticket__what` no longer reads "5 Biology questions" at the top; the page does not jump (`scrollY` unchanged within 1 px after the pick).
  2. Web Practice at 390: the sticky bar's text and the start key: the key reads "Start 5 questions in Biology".
  3. Web Start sheet (open "Start a session"), pick Biology: the lead card at the top (the 390 shot shows "10 Accountancy questions" with "Set it up") names the MODE; the count and subject sit in its key.
  4. App Practice and Start sheet (E2): picking a subject keeps the mode first.
- **Proof to open:** `cand-web/G26_practice-after-pick_{390,1440}_{night,day}.png`, `G26_startsheet-after-pick_{390,1440}_*`, `cand-app/G26_start-after-pick_fresh_*`, the `scrollY` log.
- **R4:** before = `tmp/feedback-1019/a4b/g26-base-1440-dark-after-pick.png` and `g26-base-390-dark-after-pick.png`; web Start sheet `g27-base-390-dark-sheet.png`.
- **R2:** "Practice, after picking a subject": "I chose a subject and I can still see which kind of practice I am doing."
- **Fail if:** any surface leads with the count and subject; the layout jumps on pick; the key text is missing.

### G27: the Start sheet's subject chips need a sideways cue
- **His words:** "you can add some kind of leading horizontal scroll or something in the subject selector so that people know that they have to horizontally scroll."
- **Decision:** a peek, a one-time nudge, an edge fade and a chevron.
- **DONE WHEN:** none in PLAN-1019 (SPEC only). SPEC closing line, verbatim: "He asked for this before (it is in the ledger)."
- **Test (W1; clear the first-open flag before each run):**
  1. Open the Start sheet at 390 with an overflowing subject list (`catalog=full`): the last visible chip is cut at about 60% of its width (accept 50 to 70%; measure `visible width / chip width` in the DOM).
  2. The row nudges 24 px once on first open (sample `scrollLeft`: 0 to 24 and back, once, 24 px plus or minus 2). A second open does not nudge.
  3. A right-edge fade and a chevron are visible; the chevron does not overlap the last chip.
  4. Reduced motion: `scrollLeft` stays constant.
  5. A student with 3 subjects (no overflow): no peek and no chevron (nothing to scroll).
  6. The Practice page shelf (`practice.css` lines 65-66, a 64 px mask) has the same cue. At 1440 the mouse arrows remain.
- **Proof to open:** `cand-web/G27_startsheet-peek_{390,1440}_{night,day}.png`, `frames/G27/` (every 40 ms for the first 1.5 s) and the `scrollLeft` log.
- **R4:** before = `tmp/feedback-1019/a4b/g27-base-390-dark-sheet.png`, `g27-base-1440-dark-sheet.png`.
- **R2:** "Start sheet": "there are more subjects to the right."
- **Fail if:** no peek; the nudge repeats on each open or ignores reduced motion; the chevron covers a chip; a non-overflowing row shows a cue.

### G29: no way to sign out of this browser
- **His words:** "I seriously don't see "Sign out of this browser" finally."
- **Decision:** a plain, labelled "Sign out" row on the account page and a labelled button in the top bar and the phone More sheet, separate from "Sign out of other devices" and "Delete account".
- **DONE WHEN:** none in PLAN-1019 (SPEC only). SPEC closing line, verbatim: "visible at 390 and 1440, separate from "Sign out of other devices" and "Delete account"."
- **Test (W1 fixtures; W2 staging):**
  1. `?view=profile` at 390 and 1440: an "Account actions" group with the rows in this order: **Sign out, Sign out of other devices, Delete account**. Delete account is last and visually separated.
  2. `getByText('Sign out', {exact:true})` is visible at 1440 in the top bar (the word, not only the glyph at `AppLayoutClient.jsx:413`) and at 390 inside the More sheet (`:462`) within two taps from any page.
  3. At 390 the group is reachable without hunting (record how many screens of scrolling from the top; the order-7 placement `account.css` lines 213-222 is gone or the group is promoted).
  4. W2: with a NEW staging student, tap Sign out: the confirm "Stay signed in" appears first; confirm: the session ends, `/today` asks for sign-in, cookies cleared. Sign in again. Do NOT run Delete; check only that it asks for confirmation and is separate.
- **Proof to open:** `cand-web/G29_profile_{390,1440}_{night,day}.png`, `G29_topbar-signout_1440_*`, `G29_more-sheet-signout_390_*`, `G29_signed-out_{390,1440}_*` (W2).
- **R4:** before = `tmp/feedback-1019/a4b/explore-base-profile-390-dark.png`, `explore-base-profile-1440-dark.png` and `baseline-web-r10/profile-*`.
- **R2:** "Account": "I can sign out here."
- **Fail if:** the control is icon-only; it sits inside another card; Delete account sits next to Sign out without separation; the 390 More sheet lacks the word; signing out leaves a live session.

---

# GROUP C (Wave C, built after the mock-up picks: D112 applies if he is away)

### G24: web navigation (C1)
- **His words:** "Your mob is placed inside Study only, and everything is inside Study, and Planning is in Marks Trends." His choice: "Mock-up 2-3 options".
- **Decision:** D107: 2-3 mock-up options first; he picks; then build. If he is away, D112: the CTO picks the designer's recommendation, builds it, tells him.
- **DONE WHEN:** none in PLAN-1019 (SPEC only). SPEC, verbatim: "MOCK-UP FIRST: 2-3 options (A: the app's Today, Practice, Start, Mob, You; B: the current nav with the Mob and Planning pulled out; C: one more by the designer). Each at 390 and 1440. He picks; then build."
- **Test (W1; the build is checked against the recorded pick):**
  1. Mock-up evidence exists: `docs/design-decisions/pass-1019/WEB-NAV-1019.md` (each option's full map, R2 line, pros and cons, recommendation) and boards under `tmp/design-1019/web-nav/` (sidebar at 1440 and dock plus More sheet at 390, Night and Day, one comparison board per theme). The pick and its reason are recorded in the ledger and in MESSAGE-1019.md.
  2. The built nav's labels and grouping match the pick's map exactly (diff the labels).
  3. **R3 reachability crawl** (Playwright, `study=on&contribute=on`, then as a moderator): every current page is reachable from Today in at most 2 clicks at 1440 and at most 2 taps at 390: `/today`, `/dashboard` (Practice), `/learn`, `/review`, `/explore`, `/saved`, `/progress`, `/leaderboard` (Your standing), `/mob`, `/analytics` (Marks trend), `/admission-compass` (Colleges), `/mentor` (Ask Mobi), `/profile` (Account), `/wallet`, `/help` (Guide), plus `/upload`, `/my-uploads` (contribute on) and `/moderation`. Write the table: page, clicks at 1440, taps at 390, old URL still opens (200 or redirect, never 404), the nav item is highlighted on the page (and on its sub-pages, such as a result under Practice).
  4. His three complaints: the Mob is a first-level place (an item of its own at 1440 and one tap at 390, not only inside More); no group holds "everything" (no group above 6 items); Planning is no longer a label sitting over "Marks trend" (the group names make sense in plain student words).
  5. Badges: the Review open-repairs count is not lost.
  6. Focus order follows the visual order; the dock never covers content at 390.
- **Proof to open:** `cand-web/G24_nav_{390-dock,390-more,1440}_{night,day}.png`, `tmp/walk-1019/G24-reach-table.md`, the label diff, the WEB-NAV board images for the picked option.
- **R4:** before = `baseline-web-r10/` nav views (sidebar 1440, dock and More 390) for each page; every page that had a place still has one.
- **R2:** "Nav": "I can find where to take a mock, see my papers and join friends in one look."
- **Fail if:** any page unreachable or 404 on an old URL; the built nav differs from the recorded pick; the Mob is still buried; a group holds everything; the repair count lost.

### D107: web navigation: 2-3 mock-up options for him to pick
- **His words:** "Mock-up 2-3 options".
- **Decision:** D107: nothing moves until he picks; option A is the app's five.
- **DONE WHEN (verbatim, G24 SPEC):** He picks; then build.
- **Test / Proof / R4 / R2 / Fail if:** G24 steps 1-2 (evidence of the options, the pick, then the build) plus D112.

### G21: Ask Mobi, "Ask now" and "Ask your record" (C2)
- **His words:** "This "Ask Me" can also be integrated more properly and made more useful, in terms of "You can ask now" and "Ask your record," with a very big UI." His choice: "Mock-up first".
- **Decision:** D110: mock-up 2-3 options; then build the pick (the app first; the web only if the pick includes it). Instant answers with no consent sheet (D53) stay.
- **DONE WHEN:** none in PLAN-1019 (SPEC only). SPEC, verbatim: "MOCK-UP FIRST: 2-3 options for "Ask now" and "Ask your record", big (near-full-screen sheet vs its own screen vs a tab inside Mob/You). After his pick, build it."
- **Test (E2 FRESH, E3 HEAVY, W1 if the web is included; 360 dp Night and Day):**
  1. Mock-up evidence: `docs/design-decisions/pass-1019/ASK-MOBI-1019.md` and boards under `tmp/design-1019/ask-mobi/` (entry point, fresh empty state, heavy suggestions, a streaming answer, the credit line, an error and offline state; app at 360 x 800 and 412 x 915, Night and Day; web at 1440). The pick and reason are recorded.
  2. Entry: reachable in at most 2 taps from Today (per D105 the bar is Today, Practice, Start, Mob, You; note where the pick puts it). The existing entries still work (Today's "Ask Mobi what to practise", the result's "Ask Mobi about this set", the Practice row): R3.
  3. The screen shows two big, obvious ways in: **Ask now** (any CUET question, a concept, a doubt: type or tap a starter) and **Ask your record** (answers from his own papers: weakest chapter, what to revise tonight, why a mark was lost). Both are visible above the fold at 360 x 800 without scrolling, with large type and tap targets (guideline: tap targets 56 dp or more, titles 20 sp or more; his word is "very big").
  4. FRESH, no papers: "Ask your record" says plainly what it needs ("Sit one paper first and Mobi can answer from it") and offers ONE starter that works. "Ask now" works at once.
  5. Ask now: type or tap a starter; the answer streams; there is no consent sheet on the first ask (D53).
  6. The credit line is plain and true: check the rule in the server and the wallet. At the time of writing the web says "Opening Mobi is free; a written reply costs 1 credit" and the app marks entries "Free"; the brief for the mock-ups says one credit a reply and Free 50 a month. Take one reply and compare the balance before and after: it moves by exactly what the screen says.
  7. HEAVY: "Ask your record" suggestions come from the record; every figure and chapter named exists in Your papers and the numbers agree (G20).
  8. Error and offline: remove the 3101 reverse: a calm message with a retry, no endless spinner, and no credit taken. Restore and retry.
  9. Web twin if included: `/mentor` and `?view=prepos` at 390 and 1440, same checks.
- **Proof to open:** `cand-app/G21_ask-home_{fresh,heavy}_{night,day}.png`, `G21_ask-now-answer_fresh_*`, `G21_ask-record-empty_fresh_*`, `G21_ask-record-answer_heavy_*`, `G21_ask-offline_fresh_*`, the credit before and after, the board images of the pick.
- **R4:** before = `baseline-v15.2/` keys `ask-mobi` (fallback `app-walk-1018g/62-askmobi.png`, `63-askmobi.png`, `64-askmobi.png`, `65-ask-ans.png`, and `tmp/app-walk-1018/clip-askmobi-open.mp4`) and the web Ask Mobi panel in `baseline-web-r10/`.
- **R2:** "Ask Mobi": "ask anything, or ask about my own papers."
- **Fail if:** the screen is not the recorded pick; a way in is below the fold; the fresh "record" state is a dead end; a consent sheet appears; the credit line is false; an old entry broke.

### D110: Ask Mobi, "Ask now" and "Ask your record": mock-up first
- **His words:** "Mock-up first".
- **Decision:** D110: mock-ups before any build.
- **DONE WHEN (verbatim, G21 SPEC):** After his pick, build it.
- **Test / Proof / R4 / R2 / Fail if:** G21 steps 1-2 plus D112.

### G30: the homepage morphing text (C3)
- **His words:** "This morphing text on the homepage, firstly, is a very basic animation. Change it somehow. This timing animation should start after someone is done scrolling and the first screening gets attached."
- **Decision:** a refined transition that starts only after the hero settles; mock-up first (D112 applies).
- **DONE WHEN:** none in PLAN-1019 (SPEC only). SPEC closing line, verbatim: "Mock-up the motion as a short screen recording before shipping." Operative SPEC: "replace the basic morph with a refined text transition (for example a per-word blur-and-rise or a clip-reveal, 400-600 ms, ease-out). The cycling starts only after the hero has settled (first paint done, no scroll for 1.2 s) and pauses while the student scrolls; reduced motion shows the final line only."
- **Test (W1 landing `/`; 390 x 844 and 1440 x 900; Night and Day):**
  1. Mock-up evidence: `docs/design-decisions/pass-1019/HERO-MOTION-1019.md` (already present), the strips and videos under `tmp/design-1019/hero-motion/`; the pick is recorded.
  2. Timeline A (no scroll): log navigation start, first paint, hero entrance end, every text change (a MutationObserver on the changing line). The first change is at least 1.2 s after the later of "hero entrance ended" and "last scroll"; it is not on a timer from mount (release 10: `FIRST_MS` 3600 from mount, `heroPhrases.mjs`).
  3. Timeline B: scroll at 2 s for 1 s. No change fires during the scroll; the next change comes at least 1.2 s after the last scroll event.
  4. Timeline C: scroll the hero out of view: no cycling; scroll back: it resumes after 1.2 s of stillness. Timeline D: a hidden tab pauses.
  5. One change takes 400 to 600 ms with an ease-out (frames every 40 ms through one change: progress is monotone and decelerating). The hold between phrases is not shorter than release 10's 2600 ms (he finds things "faster").
  6. Frame strips at both widths in both themes through one full change; compare them with the picked option's strip in `tmp/design-1019/hero-motion/`.
  7. Reduced motion: only the final line shows and it never changes. The accessible name stays the stable sentence (`HERO_SENTENCE`: "CUET 2027. One mock. No more guessing."), not the cycle; nothing announces each change.
  8. L-016 and L-019: the changing word is a typed or crisp morph, not glass; no glow, sheen, drop shadow glow or gradient text on it (check computed styles).
  9. No layout shift: the headline box height is constant across phrases and each phrase fits on one line at 320 px.
- **Proof to open:** `frames/G30/` (strips, both widths, both themes), `frames/G30/timeline.md` (A to D with timestamps), `cand-web/G30_hero_{390,1440}_{night,day}.png`, the computed-style log.
- **R4:** before = `baseline-web-r10/` hero frame strip (the baseline walker records the hero over 8 s every 200 ms): the first change is at about 3.6 s from load regardless of scrolling.
- **R2:** "Hero": "the headline says CUET 2027. One mock. then a changing promise; nothing for me to do but read."
- **Fail if:** the first change keys off mount; a change fires during a scroll; duration outside 400-600 ms; hold shorter than 2600 ms; reduced motion still cycles; glow or gradient text; layout shift.

---

# GROUP X: cross-cutting, the principle and the process

### G16: a fresh account must be complete
- **His words:** "this is the bare minimum. Without this, we can't even put the app into testing."
- **Decision:** the new-student path must be complete without Pro or payment: no screen with nothing useful to do.
- **DONE WHEN (verbatim):** the fresh-account walk finds no screen with nothing useful to do.
- **Test (E1 and E2 FRESH; W1 empty fixtures):**
  1. Walk, in this order, writing one row each into `tmp/walk-1019/FRESH-SWEEP.md` (`screen | what is there | the one useful thing the student can do (a verb) | empty, single-item or dead end? | fixed?`): welcome; every onboarding step; sign-in; Today (every block; the deck through the end card); Practice (every tile and sheet); Start sheet; a 10-question Quick from start to submit; the moment after Submit; the result; Your papers; Revise (empty: it must say how to fill it, with a key); Learn; Ask Mobi (Ask now and Ask your record); the Mob (find it, create it, its empty states); You and every row; Credits and wallet; settings; offline and reconnect (remove the reverse; Today shows a calm offline state; reconnect recovers).
  2. Take `tmp/walk-1019/BASELINE-FINDINGS.md` (app) and `BASELINE-WEB-FINDINGS.md` (web) when they land. For every HIGH and MEDIUM finding write `finding id | candidate status (fixed with a shot, or explained and owner-flagged)`. A HIGH left unfixed without an owner decision is a fail.
  3. Web: `?view=today&data=empty` and `firstweek=1`, `review=empty`, `?view=mob&mob=notsat`, `?view=dashboard&data=empty`: every one has a useful key and no dead end.
- **Proof to open:** `tmp/walk-1019/FRESH-SWEEP.md`, the finding-by-finding status table, the empty-fixture shots.
- **R4:** before = the baseline findings files themselves plus `baseline-v15.2/` and `baseline-web-r10/` for each screen.
- **R2:** one line for every row of the sweep (G23).
- **Fail if:** any screen offers the student nothing to do, shows a single item where a set was promised, or ends in a dead end without an exit.

### G23 RULE: the users are 16- and 17-year-olds, many new to apps and CBT
- **His words:** "remember this app is for students who are literally 17 years old right now. Many of them might be new to using mobile" and "If I'm finding the UI confusing and overwhelming, then for sure everything needs to be thought through."
- **Decision:** a rule for everything: simple, obvious, guided (R2).
- **DONE WHEN:** none (a rule). How to show it:
  1. `tmp/walk-1019/R2-LINES.md` has a row for EVERY screen walked (E1, E2, E3, W1, W2), each answered in the first person of a first-time student and judged against the pass answer in its block. A screen whose answer is not obvious in 3 seconds is a finding.
  2. A cold read: one agent with no briefing walks the FRESH account from welcome to the first result using only what the screens say, and records taps taken, hesitations and dead ends.
  3. Jargon list, each explained at first sight in plain words: CBT, NTA, CSAS, cutoff or "lowest Round 1 score", Mob, repair, Pro, credits, reel. Record where each first appears and whether it is explained.
  4. Basics at 360 dp and 1.3 text: one primary key per screen; tap targets 48 dp or more; body text 14 sp or more; no clipping.
- **Proof to open:** `R2-LINES.md`, the cold-read log, the jargon table.
- **R4 / R2 / Fail if:** a screen with no R2 row; a jargon term unexplained at first sight; a screen with two competing primary keys.

### G32 PROCESS: "I am not satisfied ... even after spending so much time with multiple agents"
- **His words:** "Honestly, I am not satisfied with the result of all this at all, even after spending so much time with multiple agents." and "the core problem and the user experience are the same."
- **Decision:** a rule; the answer is evidence, not words.
- **DONE WHEN:** none (a rule). How to show it:
  1. MESSAGE-1019.md has one row per G item: what changed, where to look, the evidence path (block id from this sheet), and its verdict. No row says DONE without an evidence path the verifier opened.
  2. Things he said had gone and must be back: the reveal (G22), the NTA gradient button and textures (G28), the stats strip (G25), the animation feel (G31). Show each with its R4 pair.
  3. The first emulator session in the walk log is a FRESH account (R1), proved by the timestamps in `tmp/walk-1019/`.
- **Proof to open:** MESSAGE-1019.md table, `tmp/walk-1019/r4/` folder, the walk log.
- **Fail if:** any G row has no evidence; a restored item has no R4 pair.

### G33 PROCESS: "Why can't you see these kinds of things yourself?"
- **His words:** "Why can't you see these kinds of things yourself and analyze them as to how they should be?" and "actually nudge the entire flow so that it should take actual action on my feedback, rather than just being stuck in the loop."
- **Decision:** a rule: every agent thinks through every point and acts (R1-R8).
- **DONE WHEN:** none (a rule). How to show it:
  1. MESSAGE-1019.md answers him in plain words using PLAN-1019 section 0: checks ran on a heavy seeded account only; hiding was treated as a fix; no release was compared with the previous one; checks verified the list and not the experience; many branches merged late. And it says what changed: R1 to R8, a fresh account first, side-by-side diffs, motion as frames, one owner per surface, mock-up first.
  2. Evidence that the rules ran: `r4/` has a before-after for every BUILD item; frames exist for G13, G22, G27, G30, G31; `R2-LINES.md` is complete; the FRESH walk came first.
  3. Beyond his expectation: the NEW findings from the baseline walks that no G item named are fixed or listed (MESSAGE-1019.md "extras").
- **Proof to open:** MESSAGE-1019.md section on the loop, the `r4/` listing, the NEW-findings status table.
- **Fail if:** the message blames anyone or hides a cause; a rule has no artefact.

### D102: planning only tonight
- **His words:** "Do all the theoretical work right now, in this window only. Then prepare a handoff so that ... nothing is still not clear".
- **Decision:** D102: record everything, decide, write a handoff so complete the next session builds exactly what he expects.
- **DONE WHEN:** done at 2:10 am per the ledger. Evidence: PLAN-1019.md, NOW.md, NEXT-PROMPT-1019.md exist and say what they should; the ledger row reads DONE.
- **Test:** nothing runs on the candidates. The verifier opens the three files and the ledger row.
- **R4 / R2 / Fail if:** not applicable; fail only if a file is missing or contradicts the plan.

### D111: explain what happened, ask only what is needed, then deliver
- **His words:** "I want you to understand everything and have clarity of what all happened and why the successful result was not published, even after doing so much."
- **Decision:** D111: first explain plainly; ask only what is needed; then run the plan and deliver beyond his expectation.
- **DONE WHEN:** none in PLAN-1019. Check:
  1. MESSAGE-1019.md opens with the plain explanation: why the good result never reached him. It names the real causes from FORENSICS (the 16 Oct "de-slop" removed the gradients; v13 unmounted the finish moment; v15.2 hid NTA to hide Pro; Review was replaced by a design that dropped the strip) and the process causes (PLAN section 0).
  2. It asks only for what is genuinely needed: connect the phone for v15.3; say "push" for release 11 (or run the command); the G26 surface if still unclear; the Razorpay test card, Play Console, PERSISTENT_LIMITS_ENABLED and W-044. It ends with "Things needed from you right now" or "Nothing needed from your side".
  3. Plain English only (R6); jargon explained.
- **Proof to open:** MESSAGE-1019.md.
- **Fail if:** blame, hidden causes, a question that need not be asked, jargon.

### D112: if he is away, pick the recommendation and build it
- **His words:** "If I'm not around when the mock-ups arrive, pick your recommendation for web nav, Ask Mobi and the homepage motion and build it; I can change it later."
- **Decision:** D112: the CTO picks the designer's recommended option for web navigation, Ask Mobi and the homepage motion, builds it, and tells him. He can change it later.
- **DONE WHEN:** none in PLAN-1019. Check:
  1. Three ledger rows exist, each with the option name, the reason, a time, and "he can change it later".
  2. MESSAGE-1019.md lists the three picks with their board images.
  3. Each build equals its pick (G24, G21, G30 above).
  4. If he has replied since, his pick wins (the newest source wins): read the bottom of OWNER-FEEDBACK-2026-10-19.md before the walk.
- **Proof to open:** the three ledger rows, the message section, the board images.
- **Fail if:** a pick is unrecorded; a build differs from its pick; a newer owner pick was ignored.

### D113: no Autopilot tonight (extra, read from the owner file)
- **His words:** "Keep your 10 agents running in this session; no Autopilot tonight."
- **Decision:** D113: session 25ef3d95 keeps its 10 agents and runs the plan; at the limit make STOP POINTs and wait for the reset or for him.
- **DONE WHEN:** none. Check: `git worktree list` shows each owner worktree once; no second session wrote to a worktree after the Autopilot fork stopped (about 2:12 am); the one known fork write is the harmless STOP POINT 83ac6103 (A2a); NOW.md names the original ten agents.
- **Proof to open:** the worktree list and the `git log` per worktree.
- **Fail if:** two sessions touched one worktree.

---

## 4. Walk order (one page): every block in the fewest sessions

The order is R1: FRESH first, HEAVY second. Emulator sessions are about 15 minutes each (the shared-emulator lock rule); there are three, plus a short gap-fill only if the baseline is missing a key. Browser runs are two.

**P: Prep, no emulator time (about 20 minutes)**
- Build the v15.3 PROFILE APK from `wt-v15-3` with `dart_defines/phone-relay.json` (one Flutter build at a time; `./gradlew --stop` after).
- Start the staging site from `wt-rel11` on port 3104; reverse 3101 to 3104; warm routes. Install the APK.
- Baseline gate (section 1.4): every "before" key exists, or note the gaps.
- Data checks done at the desk: G6 data table and the year label; D103; G18 hand-calc expectations; G19 formula; the unit test names for G1, G3, G4, G7, G12, G15, G17, G18, G19, G20, G22.
- Read the bottom of OWNER-FEEDBACK-2026-10-19.md for any newer pick (D112).

**E1: FRESH, part 1 (onboarding to Today). Day first, then Night.**
1. `pm clear`; Day (`cmd uimode night no`); normal clock. Onboarding pass in Day, stopping at the save step with no sign-in: **G1** (welcome, every Mobi line), **G2** (diff), **G3** (hans, stress variants, other search fields), **G4**, **G5** (note), **G6** (scrambled picks, five colleges), **G7** (the five picks), **G8** (untick), **G9** (rule before the first pick, other course). Then `pm clear`.
2. Late-night clock: welcome asleep and woken (**G1** late-night). Restore the clock.
3. Night pass with the same inputs, sign up with the email code: this creates FRESH account A. Today: **G14** (montage), **G7** (top 3 of 5, See all 5), **G6** (order on Today), **G12** (every deck card, a pass, the end card, the clock card), **G13** (accept recording, then reduced motion), **G10** and **G11** (bar crops, zoom, text 1.0 / 1.3 / 1.6, 412 dp), **G17** (five controls, Mob tab present).
4. Flip to Day and re-shoot Today, the deck and the bar zoom.

**E2: FRESH, part 2 (account A, Night then Day, about 15 minutes)**
5. **G15** and **D101** (Practice tiles, locked sheets, Start sheet, alternatives), **G20** step 2 (empty Your papers), **G26** app side (pick a subject in Start).
6. The 10-question Quick, recorded from before Submit: **G22** and **D108** (frames, completion line, count-up, above the fold, Celebrations settings), **G20** step 3 ("See this paper", the top row, numbers), then a 5-question paper with the reverse removed at Submit (offline "Paper saved" check).
7. **G17** and **D105** (Mob tab with no Mob, create, Mob home, Today's Mob card gone, You has no Mob row), **G21** and **D110** (Ask Mobi: fresh empty state, Ask now with a credit before and after, offline).
8. You > Plan: **G5** (change the course and back), **G18** (type 900-920, 910-920, reversed, gap 250; Today and You agree), **G19** and **D109** (choose "I don't know my range yet", the card; while the app waits, run the rig scripts to sit two mocks, reopen, then the rest, then the estimate and Accept).
9. **G16** sweep items not yet seen (Revise, Learn, You rows, credits, offline and reconnect). Flip to Day; re-shoot Practice, Your papers, the result end state, the Mob tab, Ask Mobi.

**E3: HEAVY (`app-e2e-student@example.com`, about 15 minutes)**
10. Night: **G14** (diff against the baseline), **G12** heavy deck, **G7** with 8 colleges, **G15** tiles, **G20** (subject filter, rows open the right paper, numbers table), **G18** on You > Plan, **G19** estimate-ready or partial, **G17** member Mob home, **G21** "Ask your record" from the record, **G10** bar.
11. A full mock (50 credits; answer 3; Submit): **G22** sealed sheet, 4-card recap, reveal.
12. Text 1.3 and 1.6 sweep on Today, Practice, Your papers and the bar (**G11**, **G23**). Flip to Day and repeat the key screens. Kill the emulator, restore the reverses and settings, `./gradlew --stop`, release the lock.

**W1: browser run 1, anonymous, one script on the 3104 server (390 x 844 and 1440 x 900, Night and Day)**
13. Landing `/`: **G30** timelines A to D and strips, **G28** landing and aurora, **G31** hero, public pages `/features`, the pricing page.
14. Arena fixtures (`study=on&contribute=on`): Practice `view=dashboard&catalog=full` (**G28** NTA button, **G26** pick Biology, **G27** Start sheet first open and nudge), `view=today` (default, `data=empty`, `firstweek=1`), `view=review` (all `review=` fixtures: **G25**, **D106**), `view=profile` (**G29**), `view=mob`, `view=wallet`, `view=compass`, `view=ranks`, `view=prepos` (**G21** web), `view=result` and `view=progress` (**G31** count-up frames, stagger, key press, dock spring), the nav crawl (**G24**, **D107**).
15. Optional inside the same run: the lit build on port 3502 for the **G28** three-way pairs, if A4a's saved shots are missing.

**W2: browser run 2, signed in on staging (one script, a NEW test student)**
16. Sign in with the email code; sit a quick paper through the rig; **G25** Review on real data and the row opens its result; **G29** Sign out for real (confirm, session ends), sign in again; **G20** web twin; **G21** web `/mentor` if included. Sign out at the end.

**Close:** fill `tmp/walk-1019/ACCEPTANCE-RESULTS.md` from the scoreboard below; build `r4/` pairs for every BUILD block; verify **G32**, **G33**, **D102**, **D111**, **D112**, **D113** against MESSAGE-1019.md and the ledger. Two verifier rounds at most.

Coverage check: every block appears above. A1: G10, G11, G15, D101, G17, D105 (E1, E2, E3). A2a: G1-G6, D103, G8, G9 (P, E1). A2b: G7, D104, G12-G14 (E1, E3). A3: G20, D106, G22, D108 (E2, E3, W1, W2). A5: G18, G19, D109 (E2, E3). A4a: G28, G31 (W1). A4b: G25-G27, G29 (W1, W2). Wave C: G24, D107 (W1), G21, D110 (E2, E3, W1), G30 (W1). X: G16 (E1, E2), G23 (all), G32, G33, D102, D111, D112, D113 (close).

---

## 5. Scoreboard (copy to `tmp/walk-1019/ACCEPTANCE-RESULTS.md` and fill; one row per block)

Columns: `ID | verdict (DONE / DONE on emulator, OWNER confirms / NOT DONE) | evidence paths opened | R2 matches pass answer (y/n) | R4 pair shows no loss (y/n) | fail-if lines checked (y/n) | note`.

G1, G2, G3, G4, G5, G6, D103, G7, D104, G8, G9, G10, G11, G12, G13, G14, G15, D101, G16, G17, D105, G18, G19, D109, G20, D106, G21, D110, G22, D108, G23, G24, D107, G25, G26, G27, G28, G29, G30, G31, G32, G33, D102, D111, D112, D113.

That is 46 rows. A row with a blank column is NOT DONE.
