---
name: platform-focus-mobile-first
description: "Owner 15 Oct 2026 ~16:30 IST - landing page is mobile-first (ads, promotion); arena is desktop-first but must work on phones; the app is mobile only; act as CTO and keep polishing small details"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 604ced81-3aa7-4deb-b42c-f324ca5f51e2
  modified: 2026-10-15T10:44:41.397Z
---

Owner, 15 Oct 2026, after reviewing website v2 on the local server (he called it "a step in the right direction", "maybe 30%", needing 2 or 3 more passes):

- **Landing page: mobile-first, always.** Ads and promotion bring people in on phones. Every landing section must be at least as impressive on a phone as on desktop. Example: the pinned "Every mark, traced back to a moment" scroll story worked on desktop but fell apart into stacked sections on mobile, which "should not happen".
- **Arena (signed-in website: Practice, Today, results): desktop-first,** but some students take tests and mocks on phones, so mobile must be good too. The arena on mobile "can still be a bit confusing"; bring the app's refinements across.
- **The app is mobile only.**
- **No sub-remarks on production pages,** such as "Illustrative example... not a prediction". He sees them as AI slop. The English must be refined.
- **He loves the Start sheet.** Scroll stories that hold a section while the content advances are wanted on more sections, because people scroll past them too fast.
- **Act as the CTO:** keep progressing on your own and keep fixing small details (small logos, easing, horizontal scroll that doesn't work on desktop) until it is truly refined. He authorised deploying the landing once I am satisfied with it myself.

**How to apply:** design and check every landing change at phone width first (390x844), then desktop. Check the arena at both sizes. Never leave a desktop-only effect that degrades on phones. See [[web-restructure-rejected]], [[features-over-retesting]], [[mockmob-design-direction]].
