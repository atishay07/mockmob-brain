# Homepage refinement, October 2, 2026

## Direction and scope

Refine the current Night Arena homepage rather than replace it. Preserve the CUET
headline, Gabarito/Hanken typography, lime action colour, five-question demo,
course eligibility logic, pricing and existing sections. Give the hero a cleaner
framed practice surface; add college destinations and a hands-on exam comparison.
The correction in the owner's brief is CUET, Prepium, Preparoo and **no regressive
changes**.

Palette: dark ground #0b100e, raised #131a16, light ground #f4f5f0, ink #172016,
action #d2f000, accessible lime-family text on light #526700. The light page keeps
product demonstrations dark. NTA-style paper remains white in either theme.
Layout: existing split hero; subject picker followed by four campus cards;
full-width comparison with question pane and palette; existing sections follow.
The campus cards and active question are the visual content, without invented
testimonials, college rankings or score improvements.

## References actually used

- [Prepium](https://www.prepium.in/): opened the supplied live homepage, inspected
  its college carousel, cutoff links and interface preview. Borrowed the idea of
  visible college destinations and a demonstrable exam interface, not their
  artwork, testimonials or claims.
- [Preparoo](https://ug.preparoo.app/): opened the supplied live homepage and
  inspected its hero, product demonstrations and feature selectors. Borrowed
  the hands-on product explanation and clear selectable modes.
- [Awwwards Sites of the Day](https://www.awwwards.com/websites/sites_of_the_day/):
  searched five public catalog pages, deduplicating 120 website entries. The
  detail-page fetch pass returned 26 successful pages; remaining entries were
  only available through catalog listings. This is a breadth survey, **not 120
  individual visual audits**. Names, URLs and fetch status are recorded in
  `artifacts/homepage/reference-survey.json`.
- [Landbook](https://land-book.com/) and
  [CSS Design Awards](https://www.cssdesignawards.com/): public catalog scan for
  hierarchy, product demonstration and restrained motion. Godly and the web
  reader's paginated Awwwards requests were unavailable; public HTTP catalog
  requests supplied the breadth survey instead.
- User screenshots: blue/white CBT console, orange not-answered shapes, green
  answered shapes, purple review circles and green answer marker over purple.

## Implementation

- `ThemeToggle`: accessible switch, animated sun/moon track, local preference
  and cross-tab synchronization. A small pre-paint script restores the preference;
  default remains dark. Reduced motion disables toggle transitions.
- `CollegeDestinations`: four responsive campus illustration cards; links open
  the relevant programme filter in the existing free calculator. These are course
  exploration links, not promises of a college-specific admission result.
- `ExamComparator`: five original sample questions with answer selection,
  navigation, clearing, review flags and reset. Fifty palette positions show the
  full-mock structure; only the five sample positions are interactive. Switching
  views preserves the same state. The timer is explicitly a fixed demo display.
- Paid users get a setup link carrying mode/interface to the dashboard. Others
  reach the existing pricing page. The test runner offers the same presentation
  choice only within NTA mode, which retains its existing entitlement gate.
- `nta-classic.css` restyles the same runner rather than creating a second scoring
  or session implementation. Existing answers, timer, storage key, scoring,
  submission, credits and content gates remain authoritative. Classic mode adds
  Mark for Review & Next and Clear response controls beside existing navigation.

## Illustration provenance

Generated with the built-in ChatGPT image generator, not an API script. Generated
artwork is labelled campus-inspired illustration on the page, not photography or
an exact architectural record. Source: `artifacts/homepage/campus-source.png`.
Production asset: `public/images/campus-illustrations.webp`, 1200x800, 275,656 bytes.
Only format/size optimization was performed after generation.

Prompt: Create one premium editorial illustration sprite sheet for a Delhi
University exam preparation website. Exact 2x2 grid of four equal rectangular
illustrations, no gaps, borders, text, labels or logos. Top left: SRCC-inspired red
sandstone academic building with square clock tower and lawn. Top right:
Hindu-inspired red brick academic building, cream arched colonnade, trees and
lawn. Bottom left: Hansraj-inspired warm salmon brick academic facade and pale
arched entrance. Bottom right: St. Stephen's-inspired red brick colonial building,
cream trim and long arched verandah. Architectural gouache/travel editorial style,
sage foliage, dusty brick, pale pistachio sky, soft afternoon light, readable
silhouettes, serene mood, no people, no photorealism, no text. Landscape 1536x1024.
Central buildings and breathing room in each quadrant. Independent campus
illustration cards, not claimed as photos.

## Verification and limits

- Production build and ESLint pass.
- Existing suites: NTA 22/22; DU 16/16; recovery/evidence/database 15/15;
  answer-integrity 6/6; payment entitlements 11/11 (70 total).
- Browser: desktop at approximately 1073px and 1280px; mobile at 390px and 320px.
  No document overflow at 390px or 320px. Theme switch and comparator selectors
  have 44px-high targets; mobile interactive palette targets also have 44px height.
- Verified answer selection, review-and-next, selected-answer preservation when
  switching, clearing a reviewed answer, reset, mobile menu and theme switching.
  Confirmed Commerce preset produces 35/73 eligible programmes.
- Confirmed SRCC link reaches calculator with B.Com. (Hons.) selection logic;
  course input is validated against the dataset before filtering.
- Mechanical design scan saved to `artifacts/homepage/design-scan.json`.
  Palette/radius/type-scale advisories reflect the new theme and console skin;
  Arial warnings are intentional for the user-requested conventional CBT style.
- No real premium exam was started/submitted and no checkout was made. Live
  authenticated scoring with the classic skin remains an end-to-end release check.
  No real-device or screen-reader run. NTA-style means a reference-based practice
  interface; the official 2027 interface is not asserted to be identical.
- Local source change only: no deployment, production migration or data mutation.
  Rollback removes the new imports/components/styles and the narrow dashboard,
  runner and calculator additions, preserving all pre-existing user edits.
