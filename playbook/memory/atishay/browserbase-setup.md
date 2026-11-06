---
name: browserbase-setup
description: "Browserbase cloud browser/search is set up for agents (21 Oct 2026): browse CLI, key file location, free-plan limits"
metadata:
  node_type: memory
  type: reference
  originSessionId: 7a597d08-7687-4c4e-81b7-a9b6629feeb8
  modified: 2026-10-21T07:56:03.644Z
---

On 21 Oct 2026 the owner gave a Browserbase key, saved in `C:\Users\atish\MockMob-keys\browserbase.txt`. Never print it; load it with `export BROWSERBASE_API_KEY="$(cat /c/Users/atish/MockMob-keys/browserbase.txt)"`.

The CLI is `browse`, installed globally with npm (0.11.3).
- Web search: `browse cloud search "<q>" --num-results N --json`.
- Page text: `browse cloud fetch <url> --format markdown`.
- Real cloud browser sessions are also available.

It's on the free plan, so proxies, Verified mode and CAPTCHA solving are not included, and Model Gateway is capped at $5. The owner wants it used for research, taste and references.

Agent guide: `C:\Users\atish\Desktop\MockMob-promo-film\docs\BROWSERBASE.md`.
