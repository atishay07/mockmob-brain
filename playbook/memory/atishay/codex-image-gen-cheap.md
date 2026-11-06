---
name: codex-image-gen-cheap
description: "How to generate images via Codex CLI on the owner's ChatGPT login without burning the limit (21 Oct 2026)"
metadata:
  node_type: memory
  type: reference
  originSessionId: 7a597d08-7687-4c4e-81b7-a9b6629feeb8
  modified: 2026-10-20T22:19:18.753Z
---

Images are generated with the Codex CLI built-in image_gen tool on the owner's ChatGPT plan (no API key): `codex exec -m gpt-6-luna -c model_reasoning_effort='"high"' --skip-git-repo-check -s workspace-write -C <dir> -i <ref> ... < prompt.txt`. The prompt MUST come on stdin because `-i` swallows following positional args.

Cost lesson (21 Oct): with the default config (GPT-6.1-Sol, high effort, service_tier priority, all MCP servers, plugins and hooks) each image call used 25k-71k tokens and ~30 images exhausted the main account's 5-hour allowance. A lean CODEX_HOME (`C:\Users\atish\.codex-alt`, second ChatGPT account, config = model gpt-6-luna + high effort only) uses ~13-15k tokens per image and 8-9 images cost about 2 percent. Under the lean home Codex's own file copy often fails; copy the newest PNG from `<CODEX_HOME>\generated_images\` yourself.

Owner's preference: Luna at high or xhigh (never compromise image quality). Full guide: C:\Users\atish\Desktop\MockMob-promo-film\docs\IMAGES.md. Related: [[promo-film-bar]].
