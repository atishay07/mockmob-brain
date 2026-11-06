---
name: vercel-font-fetch-flake
description: "2-3 Nov: Vercel production builds fail intermittently in Turbopack's next/font/google loader (Vercel runs `next build` = Turbopack; our gates use --webpack); redeploy the failed id; durable fix = self-host every Google face"
metadata:
  node_type: memory
  type: project
  originSessionId: ddd9a45c-465a-4aca-a19a-3798d499db2b
  modified: 2026-11-01T23:05:54.237Z
---

On 2 Nov 2026, 2 of 4 Vercel builds of main (iad1 builders) failed with `Command "npm run build" exited with 1` and a list of
`module-not-found` lines at `[next]/internal/font/google/geist_mono_b9dbf963.module.css`. The same commit built fine locally
and on a preview build that restored the same build cache, so the cause is the build-time Google Fonts fetch, not the cache
and not the code. Geist Mono is the only `preload: false` face in `src/app/layout.js`.

**Why:** a failed production build leaves the site on the previous deployment silently; a release looks pushed but is not live.

**How to apply:**
- After every push to main, read the deployment state (`get_deployment`), never assume READY.
- On this error, redeploy the same deployment: Vercel `create_deployment` with `requestBody.deploymentId` = the failed id,
  `target: "production"`, `forceNew: "1"`, slug `atishay07s-projects`, project `prj_uSolddribHQDl1mM5AKxg3O9qCIu`. It passed
  each time on 2 Nov.
- A pushed branch also builds a preview, which queues ahead of a production redeploy; wait for it.
- Durable fix (proposed to the owner, not done): serve Geist Mono with `next/font/local` from the repo so builds never fetch it.

Related: [[time-and-estimates-format]].

**3 Nov update:** after Geist Mono was self-hosted (620d65a2e), the same failure hit Gabarito ("Error while looking up
import map: next/font/google queries have exactly one entry", module-not-found in gabarito_*.module.css). It is
Turbopack's Google-font file replacer: Vercel's build command is plain `next build` (Turbopack in Next 16), while every
local gate here runs `next build --webpack`, so local builds never show it. Fix in progress: self-host Bricolage,
Gabarito and Hanken too (Fontsource woff2 + OFL in src/app/fonts), and gate releases with BOTH `next build` and
`next build --webpack`.
