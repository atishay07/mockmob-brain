---
name: image-gen-prompting-and-settings
description: "23 Nov 2026 - owner blamed \"AI slop\" people pictures on my prompts and settings, not the model; GPT Image 2.6 at high quality, batches of 4, Seedance 2.5; check every face"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 16f14db0-6d31-4a6e-9c82-29f414852a62
  modified: 2026-11-22T19:20:12.964Z
---

On 23 Nov 2026, about 12:50 am (ledger LK415), watching generated pictures for the launch film arrive, the owner said of a generated girl: "just look at the face: you have made it look so weird", and of a second take "there is some sort of a mustache or something, which shouldn't be there in a girl. In general, it's very AI-generated." His diagnosis, in his words: "GPT 2.6 is really good. I have used it multiple times, so if it's creating such outputs, it's mostly an issue with the prompting" and "For the video generations, it could be because you are using Seedance 2.0 instead of 2.5."

**Why:** he was right on each point when checked against Higgsfield's model list that night. I had GPT Image 2.6 on quality "medium" (it has high, xhigh, max), one image per shot (it can batch 4), with prompts that asked for golden evening light and listed many things NOT to show; and I used Seedance 2.0 from my own stale rule file although 2.5 was listed.

**How to apply:**
- Before any generation run, read the provider's current model list (`models_explore`) for the newest version and the top quality tier; never trust an older rule file of my own for model names or settings.
- Images of people: describe ONE real photograph in plain positive terms (who, where, what they are doing, expression, soft even light on the face from the front, lens and distance, true-to-life colour). No long "no this, no that" lists, no golden-hour glow. Ask for a batch of 4 and pick by eye.
- Look at every face at full size before it goes anywhere near a cut: upper lip, eyes, teeth, hands. A girl with a lip shadow or any "weird" face is rejected by me, not by him.
- My own reading (not his words): he watches generations as they land, so a bad picture costs trust even if it never reaches a cut.
- A film must not depend on generations: keep a designed stand-in so a cut can ship without them.
Related: [[launch-film-verdict-1122]], [[higgsfield-video-plan]], [[no-subpar-3d-use-image-gen]].
