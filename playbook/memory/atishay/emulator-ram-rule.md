---
name: emulator-ram-rule
description: "Owner's PC has 16 GB RAM; the Android emulator is the main MockMob test device (13 Oct), at most 2-3 GB assigned, and the agent manages memory itself"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 604ced81-3aa7-4deb-b42c-f324ca5f51e2
  modified: 2026-10-13T06:16:38.101Z
---

On the owner's Windows PC (16 GB RAM) the emulator plus parallel build agents once exhausted memory (12 to 13 Oct 2026). His rule then: start an emulator only with 5 to 6 GB free and assign at most 2 to 3 GB. On 13 Oct overnight he added "Optimize the RAM yourself", and at 11:30 AM: "I can't keep my phone connected for the entire day, so primarily use the Android emulator for your testing and doing everything."

**Why:** he needs his phones; the PC must stay usable; memory is shared with Chrome, the Continuum services and many Claude agents.

**How to apply:** test on the emulator (AVD mockmob_budget: 720x1600, 300 dpi like his Galaxy M06, hw.ramSize 2048, start with -memory 2048 -no-snapshot-save -no-boot-anim -gpu auto -no-audio). Check Available MBytes first; free memory by stopping your own leftovers (Gradle daemons with gradlew --stop, Gradle heap capped at 2G in flutter_app/android/gradle.properties, stray flutter_tester), never by closing his browser; stop the emulator while many builders compile and restart it for integration. Run heavy Flutter commands through flutter_app/tool/flutter_locked.sh (two slots). Use his phones (Galaxy M06 R9ZY9056DVF budget, Vivo V2413 10BF370PA6002XR) only when he connects them, and never leave a demo build that looks like the real app on them. Agents may not complete a hosted sign-in; ask him to sign in once on the emulator. See [[subagent-model-choice]] and [[security-fixes-deploy-immediately]].


Update 14 Oct 2026 ~01:10 IST (owner): testing is emulator only. Free RAM yourself (only Claude/Python services should be running; you may stop leftovers or use the agentic OS / Jarvis). Prefer 3 GB for the AVD; if 3 GB cannot be freed, a 2 GB emulator is acceptable (sluggish is fine). The app targets phones with at least 3 GB RAM; do not optimise below that.
