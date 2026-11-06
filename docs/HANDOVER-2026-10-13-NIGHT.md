# MockMob handover, 13 Oct 2026 night (22:50 IST)

Everything is stopped. No agents or workflows are running. The relay watcher (`AI OS/scripts/relay.py watch`) was stopped. It starts again at the next logon through the "Continuum Relay Logon" task. Nothing has been pushed or deployed except where noted under "Live in production".

## Repos and branches (all local, not pushed)

| Repo | Branch | Head | State |
|---|---|---|---|
| `mockmob-next` (Flutter app in `flutter_app/`) | `feat/app-and-web` | `5beb81c` WIP | App round 3 builds plus logo B device fixes, committed as WIP. `flutter analyze` shows no errors (7 lint notes in tests). The full test suite, emulator check and review were **not run**. |
| `mockmob-hotfix` (website, NTA mode) | `fix/nta-mode` | `ad2023c` | NTA engine r4.1 (all expert-review fixes) plus session fixes. Tests pass on this branch. |
| `mockmob-hotfix` | `wip/cuet-fit` | `7848577` | Partial CUET-fit gate. 509 of 879 judge files are done, and NTA tests fail until the fixtures carry fit scores. **Not merged.** |
| `mockmob-web2` | `fix/web-state-home` | `1dc44b9` | State-aware home page and test-screen notices, reviewed and fixed. Not deployed; it was never checked in a browser at 375 px and 1024 px. |

## Live in production (done tonight, owner-approved)
- **325 questions withheld from practice** (`c1fc654`, `scripts/question-hold.mjs`, hold = status pending / disputed / pending_review). That is 279 from the suspect-key recheck, 34 with "only" corrupted to "mainly", and 15 demo seed rows.
- **76 repaired questions put back** (`96ff500`, `scripts/question-republish.mjs`). Each got a new key, explanation and wording, 4 of 5 blind solvers agreed, and both quality judges scored it 7 or more.
- Records and restore files: `mockmob-hotfix/docs/brain/reports/question-holds/`. Undo with `node --use-system-ca scripts/question-hold.mjs --mode=restore --restore=<file>`.
- 249 questions are still withheld: 25 repaired but below 7, 13 that could not be repaired, and 211 others.

## App (mockmob-next) — what's done, what's left
- Done earlier and committed as `49f4100`: pass 2 after the owner's 11:10 feedback, logo B geometry, brand logo widget, launcher icon, system splash and the "mo" to "mockmob" opening animation.
- In the `5beb81c` WIP, round 3 built 10 packages from 143 audited findings: practice, account safety and Play policy, Today, runner and NTA, result and review, onboarding, design system and dock, rhythm and notifications, insights and learn, tools, demo data and docs. It also holds the logo B fixes from the emulator check (hand-off dip to black, and others).
- **Left:**
  1. Full test suite (`bash tool/flutter_locked.sh test -j 1`) and fixes.
  2. Emulator walk-through of every changed screen: AVD `mockmob_budget`, `-memory 2048`, about 3 GB free RAM needed.
  3. Review the 10 packages.
  4. The deferred items listed in the round-3 plan: warm-up questions for 10 subjects, the text-scale and copy sweep, the deep-link lines in AndroidManifest.
  5. Build the **real** app (not the demo) for the owner's phone.
- Owner decisions flagged by round 3:
  - registration window February to March 2027;
  - NTA inactive grace of 1.5 s or 3 s;
  - recap back-button target;
  - the line "Nothing goes to ad or analytics companies";
  - the "NTA mode, with Pro" label.
- Owner's phone: delete all three old MockMob apps before installing a new build.
- The emulator can't reach www.mockmob.in over HTTPS because a certificate is intercepted on this PC. Test against the local staging site.

## Logo
Logo B (Cabinet Grotesk Black, Mobi as the second o, "mo" icon). Final files are in `mockmob-next/tmp/logo/final-B` (svg, png, play, web, social). The owner may still switch to A; regenerate with `python make_dart.py --which 1`. The web favicon and header files were made but not put into the website.

## NTA mode (mockmob-hotfix)
- **Quality pass:** 5,319 questions scored by two Haiku judges (`docs/brain/NTA-AGENT-RUBRIC.md`). Bar: each judge 7 or more, no flag, and both blind solves match the key.
- **Engine r4.1** (`fix/nta-mode`):
  - options are shuffled per session;
  - a blocking flag vetoes the question;
  - demo rows, corrupted text and keys in listed order are excluded;
  - a concept-repeat guard;
  - the difficulty policy;
  - non-repeat across a student's papers;
  - mark for review saved with the session, and the clock no longer restarts.
- **CUET-fit pass** (`wip/cuet-fit`):
  - The rubric is `docs/brain/NTA-CUET-FIT-RUBRIC.md`. It covers the factory fit dimensions and the owner's definition of a 10.
  - Three Haiku judges per question. On calibration, the Haiku majority agreed with the reference on question type 98% of the time.
  - 509 of 879 judge files are done, in `tmp/nta-pass/fit/results`. The missing pairs are in `tmp/nta-pass/fit/missing-pairs.json`.
  - Left: finish the scoring, merge, put the stored-type, fit-gate and recency rules in the engine, fix the test fixtures, and do the production engine run.
- **Last engine run** (`e1dbfe8`, before r4 and fit): 6 of 15 subjects can build a paper. The expert's verdict: not ready yet. 9 subjects lack enough good questions; the long-term fix is the question factory.
- Subagents are blocked from reading production. Run `node --use-system-ca scripts/nta-engine-run.mjs` from the main session.
- **Owner decision pending:**
  - hold 12 more corrupted-connective questions and 63 keys in listed order;
  - list in `tmp/nta-review-cleanup/CLEANUP-2026-10-13.md`.
- **Not deployed:** keep NTA undeployed until the fit merge is done and an expert re-reads the papers.

## Owner's standing instructions from today
- Use many Haiku agents on low or medium effort for checking and tagging. Use Opus only for real engineering or signature motion.
- App UI/UX improvement and new features should run continuously.
- A 10 is a PYQ changed by under 10% and made slightly harder, a CBSE board question, a highly predictable CBT staple, or a question testing a key aspect of a chapter. A very hard question is not a 10.
- NTA prefers the newest questions; a newer 8 beats an older 9.
- Ask before any production data write. Owner-proxy and relay decisions are in `AI OS/decisions/log.md`.

## Workflow scripts (for resuming)
They are in `mockmob-next/tmp/workflows/`: `app-round-3.js`, `logo-b-into-app.js`, `nta-engine-fixes.js`, `nta-cuet-fit-score.js` and others. The journals of the last live run are under `C:/Users/atish/.claude/projects/C--Users-atish-Desktop-mockmob-copy/782f4b0d-7661-4ff4-baf5-4cb5ba4dce77/subagents/workflows/`. Resuming is easier as a fresh, smaller run from this document than from those journals.
