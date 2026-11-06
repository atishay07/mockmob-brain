---
name: security-fixes-deploy-immediately
description: "Owner's standing permission (12 Oct 2026) to fix and deploy crucial MockMob security issues immediately, without asking first"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 604ced81-3aa7-4deb-b42c-f324ca5f51e2
  modified: 2026-10-12T16:40:26.986Z
---

When a crucial security problem is found in MockMob (for example a student able to grant themselves Pro, or an unauthenticated route leaking data), fix it immediately and deploy it to production. Owner's words, 12 Oct 2026: "If you ever find any such, fix it immediately and deploy it."

**Why:** the owner judged the self-grant-Pro and open moderation-queue findings as crucial and does not want them waiting on a larger release.

**How to apply:** ship the security fix alone as a minimal hotfix from `origin/main` (not bundled with feature work), run the relevant tests and a production build first, follow the deploy lessons in [[mockmob-deploy-lessons]] (no www/apex redirect changes; probe redirects after deploy), verify on production, then tell the owner what shipped. This permission covers security fixes only, not feature deploys or production data migrations.
