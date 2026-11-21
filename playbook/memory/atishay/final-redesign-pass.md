---
name: final-redesign-pass
description: "20-21 Nov 2026: the final website redesign; after a rejected rebuild, the live home was refined with real product screens worked by a cursor, and on 21 Nov 3:05 pm he had it switched live as the real home"
metadata:
  node_type: memory
  type: project
  originSessionId: 777be139-a000-4c98-9286-70590b597225
  modified: 2026-11-21T09:40:28.776Z
---

On 20 Nov 2026 (LK361) Atishay called this "the final on the website redesign". The first /home-next (a new 12-block page) scored "at max a 6/10" against the live home's 8/10 (LK363). It was then rebuilt on the live home. An independent Opus critic scored it after every release overnight (7.0, 8.0, 8.5, 8.7, 9.0 against 7.5 for the old home). After his LK364 notes he said "Switch it live" on 21 Nov, and since 3:05 pm (main 459b9dd3d) `/` is the new page. /home-next redirects (308) to `/`.

**Why:** he wants a newcomer to understand the product from its ACTUAL screens, worked live by a cursor, the way Preparoo's page does.

**How to apply:**
- The home is now `src/app/page.js` with OnePlace (six rows: Practise, Key cards, Ask Mobi, Learn, Benchmarks, the Mob) and `<LabCinema look="next" />`.
- On phones, Practise plays the real phone exam inline. The frame autoplays from its heading to the end. The Lab plays itself until a touch.
- Future home work refines this page in place ([[web-restructure-rejected]]). Run an independent critic round after big changes; it caught what screenshots missed.
- Phone first ([[platform-focus-mobile-first]]). Report with a counted list ([[percent-from-a-counted-list]]).
