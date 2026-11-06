# Model trial, 6-8 Nov 2026 (owner's research; temporary; changes no rule)

The owner is comparing models on MockMob's existing workflow: GPT-6 Terra on a ChatGPT $20 plan against Claude Opus 5.5 on a
team premium plan (about 6-7x the usage). Opus 5.5 stays the primary model. This file is a side log only.

## Baseline: Opus 5.5, session 34abe724, 4 Nov ~3 am to 6 Nov ~12:40 am IST (about 45 hours, about 49% of a weekly allowance)
Shipped and verified (each through the full gate: suites, eslint, both builds, scroll/speed benches, visual pass):
- App 1.0.20+18 and 1.0.21+19 (signed AABs; emulator walks; 12,4xx tests passing each).
- Website, five production releases: Desk Light home page (LK67-LK75); night round 1 (LK81-LK97: perf predraw, CTAs, brand
  line, statement colours, exam monitor + faithful NTA runner, jump loop, fast-scroll, DU, account pop-over, onboarding options);
  round 2 (app motion on the web, public pages, logged-in layout scan of 25 views x 6 sizes); round 3 (LK99-LK115: Day palette,
  brand back, hero, bottom bar, tour fix, phone exam, pricing value framing, Key cards section).
- Content: 438 Key cards (Computerised Accounting 207, English reading 231) via author + reviewer agents.
- Round 4 (LK117-LK147): 7 packets built, 6 reviewed, 3 fixed; stopped at the limit (see HANDOFF-2026-11-06.md).
Orchestration: Opus planned, specced, reviewed and merged; Opus/Sonnet subagents built in parallel worktrees.

## What the trial session should log (fill in as you go)
| Time | Task (from the handoff) | Result (done / partly / not) | Tests and gate | Mistakes found and fixed | Where unsure |
|---|---|---|---|---|---|

## Comparison to compute afterwards (by the primary engineer)
Tasks finished vs attempted; gate pass rate; defects found later in review; rework needed; owner-visible quality of the
screenshots; usage consumed (share of the plan). Note the different plans and models when reading the numbers.

## Result, written 6 Nov 2026 ~2:30 pm IST by Claude Opus 5.5 (session c7c9ed83), from git and the handoffs
The table above was never filled (LK149 turned the run into a normal session), so this reads the record instead.

| | Claude Opus 5.5 (34abe724), round 4 part | ChatGPT / Codex (01a1ad66) |
|---|---|---|
| Window | 5 Nov ~11:40 pm to 6 Nov ~12:40 am (~1 h) | 6 Nov ~1:52 am to 3:19 am (~1.5 h) |
| Job | Plan and spec 7 packets, build them in parallel worktrees | Finish 4 unfinished packets, integrate 6, run the release gate |
| Done | 7 built, 6 reviewed, 3 fixed (demo, pricing, app); hero, learn, nav, sections left as WIP at the limit | 4 packet fixes, 6 merges (1 conflict), lint fixes, 3 real speed fixes (predraw start, tour-rail layout read, touch entry), 1 truth fix (Key cards zero before the roll), suites, both builds 115/115, 72 shots viewed, Vercel access checked, precise handoff |
| Left or wrong | Unfinished WIP; the wheel/clamp code it wrote on 4-5 Nov had the mouse-wheel scroll bug the owner hit on 6 Nov (LK154) | One source test it broke with its own change and did not update; final speed/gesture/visual runs not finished at the stop; trial log not filled |
| Checked later | Fixed in round 5 (this session) | Its runtime passed the full gate unchanged on 6 Nov: 0 frames over 100 ms cold and warm, 128/128, 72 shots clean; shipped as main 068a7a061 |
| Usage | ~12% of a weekly Team allowance in that hour (78% to ~90%) | Stopped at the owner's request at "5% usage" (LK152); the log does not say whether used or left |

Reading: both produced gate-quality work. The ChatGPT session was careful and evidence-led in integration and debugging, with one small miss. One session each, on different jobs and plans (Team premium has about 6-7x the usage of the $20 plan), cannot rank the models; a fair test gives both the same packet and the same gate.
