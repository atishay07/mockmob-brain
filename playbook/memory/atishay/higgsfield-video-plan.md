---
name: higgsfield-video-plan
description: 16 Oct 2026 - owner funded USD 15 Higgsfield API; video only for subject-object one-shots and Play promo shots; researched: Wan 3.0 primary (480p drafts, 720p finals), Kling 3.0 Std A/B, Seedance 2.5 only at 720p for one owner-picked promo shot; /estimate before every call; 15% reserve
metadata:
  type: project
---

On 16 Oct 2026 the owner added USD 15 of Higgsfield API credit and asked for a judicious plan that future agents can follow ("not because I have put $15 in it that you have to just waste it"). He rates Seedance 2.5 far above Kling 3.0 on quality and prompt-following, but it is expensive (about USD 0.144/s against 0.042/s for Kling 3.0 and 0.020/s for Wan 3.0, with discounts that end 31 Oct).

**Direction update, 16 Oct about 11:15 pm (owner):** the subject-object animations are deprioritised. Focus on the landing page (scroll storytelling) and app onboarding, where "proper animation" beats SVG. Ideas and the iteration loop (idea agents, then synthesis, then free storyboard stills, then owner pick, then Wan drafts, then the final) are in `mockmob-next/docs/brain/HIGGSFIELD-IDEAS-2026-10-16.md`. Round 1 of idea agents is pending.

**The plan lives in** `mockmob-next/docs/brain/HIGGSFIELD-PLAN-2026-10-16.md`. Read it before any video work.

**Why:** UI motion and Mobi stay code-native (themeable, crisp, interactive, small). The research brain bans ambient loops on resting screens and fake product UI (T007, T009).

**How to apply:**
- Video only for: one-shot "object comes alive" clips when a subject is picked (U1); 2-4 cinematic shots around real screen recordings in the Play promo (U2); one milestone moment (U3).
- Researched 16 Oct, about 11 pm (HIGGSFIELD-RESEARCH-2026-10-16.md): the screenshot's prices are 480p rates, and Seedance 2.5 1080p is about USD 0.80/s. Wan 3.0 is the primary model (last frame, 1:1, seed; arena rank 4 against Seedance's 2): drafts at 480p, finals at 720p. A/B it against Kling 3.0 Std. Seedance only at 720p, for one promo shot the owner picks. Failed or moderated runs are not charged, but rejected renders are. Call /estimate before each run.
- Image-to-video from our approved stills only.
- Keep a ledger in `tmp/higgsfield/LEDGER.csv` with a hard cap of USD 15. The key stays in env only.
- The owner approves 3 test clips in place before any batch.

Status 16 Oct: not connected. See [[usp-unlimited-mocks]], [[owner-ux-research-brain]].

**22 Nov 2026 update (ledger LK371).** He started Higgsfield's 3-day unlimited trial (ends 25 Nov 2026; his card is charged USD 93.22 for a month of Ultra on 25 Nov unless he cancels: remind him on 24 Nov). His words: "Utilize it to its fullest", video, image and audio. Trial limits from the mail: 1 image and 1 video at a time; video Seedance 2.5 (480p, up to 30 s) and Seedance 2.0 (720p, up to 15 s); images Nano Banana Pro / 2.1 / 2, Seedream 5.0 Pro, GPT Image 2 / 2.5 / 2.6; audio Seed Audio 1.0, Eleven v3, Minimax Speech 2.8 HD, VibeVoice, Seed Speech. The USD 15 budget rule above does not apply while the trial runs.

In the Claude Code session of 22 Nov the "Higgsfield AI" connector had only 7 read tools (balance, models_list, models_get, list_workspaces, workspace_select, show_generations, import-claude-motion-from-url): no generate tool, so nothing could be generated from there. Check `session_connectors_status` and the tool list first; if still read-only, write the prompts and have him run them in the Claude chat app, then read results with show_generations. "Fish audio" (199ad0d7) and ElevenLabs (2de647b7) are different connectors that spend their own credits.

22 Nov 2026, 5 pm (new account): the trial is refused from Claude Code on both accounts ("unlimited generations are not available" there) and works only in Claude Cowork, Claude chat or ChatGPT. Working route: a standing Cowork worker pasted once (MockMob-promo-film/gen-queue/COWORK-WORKER.txt) that does gen-queue/requests/NN-*.txt in order, writes gen-queue/status and saves to gen-queue/done; the Code session only writes request files and places results (scripts/launch-place.py). A Claude Code session cannot start or drive Cowork.

23 Nov 2026, 2:02 am: confirmed again with the FULL Higgsfield connector in Claude Code (it lists generate_image / generate_video): use_unlim is refused with the same message. Do not try from Claude Code; the Cowork worker is the only free route. Free-trial facts found 23 Nov: GPT Image 2.6 only up to quality "medium" and one picture per job (batch_size ignored); Seedance 2.5 says supports_unlim (untested at 1080p).
