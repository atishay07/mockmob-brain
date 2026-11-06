---
name: quality-bar-and-stop-rule
description: Owner 14 Oct 2026 ~14:05 IST - app must feel next-level (beyond Duolingo-level motion); save brain checkpoints with findings continuously; stop with a clean handover at ~95% context or ~95% session usage
metadata:
  node_type: memory
  type: feedback
  originSessionId: cc0bf1af-4c1f-4097-81a5-97ba84470f41
  modified: 2026-10-15T06:17:47.597Z
---

Owner (14 Oct 2026, ~14:05 IST), after seeing the last two builds and the UI blitz: the motion and premium feel were "still not very good or premium, like a Duolingo level" that he expects. He wants "absolute perfection": the app "should truly feel like a next-level app and beyond anyone's expectations". Use any image or video generator available (Codex image_gen on his ChatGPT login works; no ffmpeg or video model on this PC), vector images, animated vectors, motion graphics and motion design.

He also wants: keep saving checkpoints in the brain, and add useful information found or done (not only status) to the brain.

Stop rule: at the next major limit (about 95% of the context window before auto-compact, or about 95% of the session usage limit), make the last checkpoint and stop there, even if some usage remains (stopping at 90%+ is fine; do not squeeze the last percent). The stop must be safe: no task left half-running, everything committed, a proper handover.

**Usage readings after an account switch (15 Oct ~11:45 IST):** the owner moves sessions to another account when one runs low. The Continuum hook's "5-hour usage is at N%" line can still be the OLD account's figure. A session stopped at "96%" right after a switch, and he was annoyed: "The 95% was for another account. That's why I had shifted here. Why aren't you continuing?" Don't stop on that hook number alone right after a resume or switch. If a handoff says the last session stopped at about 95%, assume it was a different account unless the reading clearly rises from this session's own work.

**Balance rule (14 Oct ~18:30 IST):** judge the app in use (motion, interactivity, robustness), not static renders. His ranking, best first: balanced, then crowded, then sparse and over-gamified (equally bad). Over-gamified is as bad as sparse. One spacing system everywhere, light/dark parity on every screen, and a rethought bottom navbar (structure, not just polish). He said the app "looks pretty the same as ... 25 hours ago", so visible change must be large. Full words: mockmob-next/docs/brain/design-2026-10-13/OWNER-FEEDBACK-1014-1830.md.

**Why:** he has seen two builds without the premium motion he asked for, and he loses work when sessions die mid-task.

**How to apply:** judge every screen and motion against HIGH, Revolut, Fampay and Duolingo-level character animation; verify motion on the emulator with rapid frame captures, not only static goldens; checkpoint after each phase with findings; watch context and usage and stop cleanly with a handover. See [[mockmob-design-direction]], [[overnight-autonomy-relay]], [[emulator-ram-rule]].
