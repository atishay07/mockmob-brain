---
name: mockmob-landing-feedback-oct-2026
description: Owner's 5 Oct 2026 landing-page feedback — keep section placement literal, don't cut features, market every feature; Preparoo as mobile reference
metadata:
  type: feedback
---

Owner asked to remove the "subjects that carry your score" block and move Instagram "where it was" (bottom, in the Subjects slot). I moved it to the top and also cut Compass Pro, college destinations and the stats band; he said the page then felt "filled with more useless things" and that important content (DU Compass) had been lost.

**Why:** he reads placement and deletions literally; trimming for length without asking cost a round. He wants the landing page self-sufficient: every current feature clearly marketed, with high-quality motion (scroll reveals, subtle glass, progressive blur) and descriptive videos, modelled on ug.preparoo.app's mobile (one feature carousel, product mocks, sticky CTA, 7k px page).

**How to apply:** change only what is named; when shortening, collapse or ask rather than delete a feature. Prefer an overview (FeatureTour) over repeating sections. Real screen-recording videos need the owner's footage; slides take `video` paths. See [[mockmob-owner-round2-oct-2026]].

Later the same day: the owner rejected a tour built from cropped static stills ("no animation visible"). Every illustrative screen must visibly animate when it is the one being looked at, not once on first scroll. Verify motion frame by frame in a foreground browser (chrome-devtools MCP with mobile emulation) before reporting: the desktop app's Browser pane throttles timers and IntersectionObserver while hidden, which made reveals look stuck and hid real problems.
