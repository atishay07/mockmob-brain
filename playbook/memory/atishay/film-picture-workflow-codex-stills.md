---
name: film-picture-workflow-codex-stills
description: "23 Nov 2026 (owner, LK420) - film people pictures: stills from our own Codex image_gen, uploaded to Higgsfield from Claude Code, Cowork makes only Seedance clips; blind judge picked our stills 3 of 3"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 6d1dadb4-a2d6-4fc2-b045-0fdac0227ba2
  modified: 2026-11-22T21:38:25.212Z
---

On 23 Nov 2026 at 2:33 am (ledger LK420) the owner changed how the launch film gets its people pictures: "You yourself generate the images in the ChatGPT image gen, connected here. You give those images to that agent... It can just take those images as references... and then just generate videos from them." His reasons: Higgsfield's GPT Image 2.6 on the free trial was exceptionally slow, the Cowork worker's results did not match the tasks, and the people were "not very good-looking" and "too overexpressive".

**Why:** tested the same night. Codex image_gen (lean second account, gpt-6-luna high) made a room picture in about 2 minutes against 5 to 6 minutes on Higgsfield, and a blind Opus judge picked the Codex picture in all three pairs ("clear overall and large on the over-expressive faces"). Caveat: the Codex prompts were also rewritten (calm, closed-mouth smiles), so part of the win is the prompt.

**How to apply:**
- Stills: Codex image_gen (MockMob-promo-film/out/gen-codex/rooms/run_rooms.sh pattern, one call at a time, copy the newest PNG yourself). Prompt for good-looking, well-groomed people with calm, natural expressions; plain positive description of one real photograph.
- Face-check every still and clip at full size (eyes, upper lip, teeth, hands) before it goes near a cut.
- Upload picked stills to the Higgsfield library from Claude Code: media_upload, then curl PUT with headers Content-Type and "If-None-Match: *", then media_confirm. Upload works here; free-trial generation does not.
- The Cowork worker makes only the clips from those media ids (Seedance 2.5, 720p on the free trial). It sometimes logs a job without writing its results line: get the URL with the higgs connector's jobs_wait(job_id) and download it yourself.
- The judge said even the winners lean stock-photo (smooth skin, centred framing); film grain and off-centre framing would help.
Related: [[image-gen-prompting-and-settings]], [[higgsfield-video-plan]], [[codex-image-gen-cheap]].
