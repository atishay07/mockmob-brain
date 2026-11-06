# Guided tour refinement — 4 October 2026

Owner feedback after the UI release: the feature demos stopped too easily, advances were unclear,
seven seconds was too long, and the phone dropdown disrupted the composition. The new direction
is an automatic, compact product story with a visible next chapter and a 3–5 second pace.

## Implementation

- `FeatureTour.jsx`: 4.8-second bounded advance with pausable visible time and matching transform
  progress. Explicit navigation and horizontal swipe selection start a fresh chapter without turning
  off autoplay. Removed the competing slide IntersectionObserver and seven-second interval.
- Vertical touch/wheel browsing does not disable rotation. Horizontal interaction holds playback
  briefly, releases after settling, and resumes automatically. Explicit Pause remains in force.
  Keyboard focus in chapter/content controls holds rotation; Play resumes. Hidden/offscreen demos
  stop without catching up; reduced motion retains static, selectable demonstrations.
- Actual demo visibility gates playback rather than a visible footer. Resizing aligns the selected
  phone panel. Chapter-strip scrolling and panel scrolling do not call document scrolling.
- Phone dropdown removed. Shared chapter strip, eight-segment progress, current chapter, explicit
  Pause and an "Up next" button replace the scattered controls. Only the active slide is accessible;
  seven inactive slides remain inert. Automatic changes are not announced as live-region chatter.
- `feature-tour.css`: one coherent frame, compact phone copy, stable screen area, contained product
  demos, and both themes. Product-screen spacing corrected after the first matrix found overhangs
  on narrow phones. The floating sample dock steps aside during the visible tour and returns when
  it is left; keyboard focus on the dock restores visibility.
- `page.js`: shorter tour heading/introduction. Original sample activation remains available.
- Phone supporting copy uses each tool's existing reassurance rather than repeating its headline.
- `MistakeLab.jsx`: nearby explanatory stages use 4.8 seconds instead of 5.6–6.2 seconds.
- Official-key demo wording retained. No product/scoring/model/credit/payment/entitlement changes.

## Verification

- Isolated application source tree `d545c2f75982320545a7307fa0db9da25e7c1f55` passed final
  production build. Nine UI-state/landing tests and full lint passed. Source whitespace check passed.
  Evidence: `artifacts/tour-refinement-2026-10-04/`.
- The local snapshot shares installed dependencies through a junction. Its temporary Turbopack root
  is the documented common ancestor of the snapshot and dependencies. Application source matches
  the staged release; this validation-only root setting is not part of the production commit.
- Final browser matrix: light/dark 320/390/768/1024/1440px; zero global horizontal overflow,
  all measured tour controls at least 44px tall, and no product-screen overhangs. All eight phone
  and tablet screens were measured; desktop renders the selected panel.
- Observed automatic progression across several chapters, last-to-first loop, pointer chapter selection
  with playback retained, normal scrolling with playback retained, and explicit Pause retaining its
  frame over later observations. Keyboard Tab into the active CTA held playback; returning to Play
  and Enter resumed it. Pointer Pause succeeded even though one native click reported a timeout;
  fresh UI state confirmed the result, so it was not blindly repeated.
- A native dynamic-selector wait did not capture an intermediate automatic state. Separate fresh
  observations confirmed progression and loopback. 4.8 seconds is the configured visible-time
  duration; no device wall-clock precision, frame-rate or performance improvement is claimed.
- Physical-phone swipe/momentum, actual reduced-motion browser setting, screen reader, and
  controlled CPU/network traces/CWV remain unverified. No paid calls or real student transactions.

## Publication and rollback

The owner-authorized live refinement follows the prior UI publication. Production readiness and
live smoke must be recorded in STATUS.md after Vercel completes. Existing unrelated AI/commerce,
pricing/payment and backend-test changes remain local. No database migration is needed.

Rollback this refinement's four UI source files to the preceding UI release. Preserve the earlier
mobile/result/dashboard/DU work and all unrelated owner edits. Pause still provides a user-controlled
fallback while investigating any hardware-specific autoplay issue.
