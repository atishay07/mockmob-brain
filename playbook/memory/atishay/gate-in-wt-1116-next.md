---
name: gate-in-wt-1116-next
description: "16 Nov 2026: where the MockMob web release gate must run and two launch traps (lint rule not found, Turbopack with --use-system-ca)"
metadata:
  node_type: memory
  type: reference
  originSessionId: ec03baf1-09ed-4ab6-80be-4f81fc956a95
  modified: 2026-11-16T14:20:38.946Z
---

The MockMob web release gate (24 suites, lint, a webpack build and a Turbopack build) runs in `C:\Users\atish\Desktop\mockmob copy\wt-1116-next`, the only worktree with the real Next 16.3.8 and eslint-config-next 16.3.8 packages. Check the commit out there detached (`git checkout --detach <sha>`) and run `bash tmp/gate2.sh`; read every line of `tmp/gate2.log`.

- In any worktree whose `node_modules` is the junction to `wt-1103-web-cards` (16.2.4), `npx eslint src` prints five "Definition for rule '@next/next/no-location-assign-relative-destination' was not found" errors. They are the old packages, not the code.
- A Turbopack build started as `node --use-system-ca node_modules/next/dist/bin/next build` fails with "--use-system-ca is not allowed in NODE_OPTIONS". Use `npx next build`. The webpack build accepts the flag.
- A push to both `web/1115-prod` and `main` queues a preview build ahead of the production one on Vercel Hobby (one build at a time): production can sit QUEUED for several minutes.
- After the home page gains or loses markup, recapture `data/tests/fixtures/home-elements.json` (`scripts/capture-home-elements.mjs <base>`, with PLAYWRIGHT_CORE and CHROME set) or `home_cascade_order.test.mjs` judges the old tree.
- Remove a lane worktree only after `cmd /c rmdir` on its `node_modules` junction (see [[worktree-remove-follows-junctions]]).

See [[vercel-hobby-and-turbopack-junction]], [[release-build-own-worktree]].
