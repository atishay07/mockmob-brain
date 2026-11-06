---
name: device-truth-testing
description: "16 Oct 2026 - owner found the same app issues from v5/v6 still in v10; app work is done only when walked on the emulator with screenshots against his feedback ledger, never on goldens alone"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 604ced81-3aa7-4deb-b42c-f324ca5f51e2
  modified: 2026-10-16T05:11:03.123Z
---

On 16 Oct 2026 (about 10:45 IST) the owner installed APK v10 and found issues he had reported in v5 and v6 still present: Today showing "Could not reach MockMob" for every account, the Road to May clunky, the study-days ring stuck on 3, My colleges search failing ("BCOM") with results hidden under the keyboard, the Practice tab order, "Review again" broken, the You tab mixing account and study, Admission Compass tucked away, and the bottom nav bubble misaligned. His words: "I don't know what exactly changed after so many passes and builds. The basic issues ... are still the same issue." and "Even if you had tested this properly on the emulator, you could have caught all this."

**Why:** agents verified app work with analyzer, unit tests and golden images only. Goldens render fixtures at a fixed size and never exercise a real signed-in state, an upgrade from the previous build, the keyboard, or scrolling. So screens passed while staying broken in use.

**How to apply:**
- Keep one owner feedback ledger for the app (every item he has raised, newest wins). Every packet maps to ledger items.
- No app item is done until it has been walked on the emulator (2-3 GB, see [[emulator-ram-rule]]) against the local staging site with the project's test account, with screenshots looked at, including: upgrade over the previous APK, keyboard open, scroll, Night and Day.
- His phone is only for the final check of a release, and only when he says it is connected.
- Report per ledger item with the screenshot proof, not "tests pass".

Related: [[quality-bar-and-stop-rule]], [[features-over-retesting]], [[cto-mode-standing-goal]].
