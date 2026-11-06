---
name: features-over-retesting
description: "Owner 15 Oct 2026 ~12:00 IST - spend effort on new features, motion, high-res quality and web integration; minimal recording and repeated testing"
metadata:
  node_type: memory
  type: feedback
  originSessionId: cc0bf1af-4c1f-4097-81a5-97ba84470f41
  modified: 2026-10-15T18:46:32.177Z
---

On 15 Oct 2026 at about 12:00 IST, the owner said: "don't focus too much on recording things and testing over and over again. Mostly just focus on adding more and more new features, improving them, and making the app better: the motion animation, all that, making it more high-res, more high-quality, fluid, and integrating properly with the website also."

**Why:** sessions were spending large shares of time on emulator recordings, contact sheets and repeated suite runs, while he wants visible product progress.

**How to apply:**
- Default split: most agents build features, motion, imagery and web parity; checking is one lean pass per wave (analyze, the touched area's tests, a build), not repeated full suites or recordings.
- Record on the emulator only when he asks or a motion change can't be judged any other way.
- Still keep the safety rules: truthful data, no regressions, NTA exam-faithful, budget guards, and no push of the website restructure without his OK.

**Depth over breadth (same day, ~12:45 IST):** "try not to overload with useless features or just too many similar things. What is more important is implementation and perfection of one feature, and doubling down on each feature."
- The Mistake Lab (the result page's Score Recovery Lab, plus Mistake Repair and the SWOT) is the USP. Make it "10 times more useful".
- He noticed lost features: time spent on a question, how long it should take, and when an answer was changed. Commit 220e8d51 had hidden the Lab's Find step whenever the SWOT showed.
- He wants analysis "which no one is giving, and no one in the future is able to give, even with a Claude Max plan or with a team of 100 engineers". So build moats from our own data: the timing and answer-change telemetry from the NTA-faithful runner, what all students did on each question, and each student's history. It must be easy to understand and easy to reach.
- So a 14-packet feature list was cut back. Revise, Why marks leak and Rule book fold into the Lab only where they help; Your chapters, Paper formats and Week in review are cut for now.
- Never silently remove a feature a student could see. Merge it into the new flow instead.

**Quality gate before every deploy (16 Oct 2026, about 00:35 IST; this wins over "light checks"):** "remember to not compromise quality for speed... testing everything and the finish and furnishing and polish of everything before deploying anything to our standards... Every feature deployed, every small new change, is actually tested and critiqued properly, then deployed."
- **Light** means don't repeat checks needlessly. It never means skip the gate.
- **Before any website deploy:**
  - lint, the suites and a build;
  - a visual critique: a dev server, headless captures of every changed page at 390 and 1440 in Night and Day, looked at and clicked with a real pointer;
  - defects fixed and recaptured.
- **Before any APK:** analyze, the tests, and the changed goldens opened.
- A builder's "no browser" result is not a critique. Run a critic step before shipping.

See [[quality-bar-and-stop-rule]], [[mockmob-design-direction]].
