---
name: mockmob-owner-audit-jul-2026
description: "MockMob owner audit (Jul 2026) + the Aug 2026 mobile-first redesign — what changed and where the authority now lives"
metadata: 
  node_type: memory
  type: project
  originSessionId: 31bfcdc8-ad4a-4322-be31-1ad40e3f740e
  modified: 2026-08-05T19:59:25.500Z
---

Full 18-section audit artifact: https://claude.ai/code/artifact/bb3db2b7-5d66-4259-b7e1-ffa17aa58a92 (published 2026-07-12).

**Authority moved into the repo (Aug 2026).** `PRODUCT.md` now holds durable product truth, confirmed brand commitments, and the owner's standing design preferences; `DESIGN.md` holds the visual system. Prefer both over this note.

Shipped 2026-07-12 (uncommitted): CUET 2027 relaunch (`pro_cuet_2027` live at ₹99, `pro_cuet_2026` legacy, accessUntil 2027-07-31), fake testimonials removed in favour of `LiveStatsBand` wired to `/api/stats`, `DemoDrill` (5-question no-signup drill), sitewide og:image via `src/app/opengraph-image.jsx` (note: `seoMetadata` must not pass an empty images array — it strips the file-convention og:image), www→apex 308 in `next.config.mjs`, `/about` `/contact` `/cuet-2027`, six subject hubs at `/cuet/[slug]` (`src/lib/subjectHubs.js`).

**Superseded by the Aug 2026 redesign:** the RadarField canvas hero, ArenaPreview, DotPattern decoration, glass cards, `.eyebrow` kickers, and the volt-on-near-black palette are all gone from marketing. `DecodeWord` survives and still carries the kinetic personality the owner asked to keep.

Still manual for the owner: Vercel domain-level redirect + `NEXT_PUBLIC_SITE_URL`, Search Console + analytics, abandoned-checkout email (needs a cron decision), Telegram/WhatsApp community, real beta testimonials.

Stale, do not trust: `PROJECT_CONTEXT.md` still describes MockMob as multi-exam (CUET/JEE/NEET/UPSC). The owner confirmed CUET-only, fully committed. See [[mockmob-redesign-aug-2026]].
