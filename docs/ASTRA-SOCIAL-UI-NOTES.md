# Social proof UI refinement · 3 October 2026

Scope: curated Instagram strip and consent-gated Wall of Love. No homepage section wiring, voice content, production data, or claims were added. `VOICES` remains empty, so the public wall remains hidden.

## What changed

- Instagram cards now use local type and a quiet grid/orbit pattern to make the existing creator and post attribution feel intentional when a permitted thumbnail is unavailable. These are authored graphic covers, not representations of the underlying posts. Cards preserve their 9:16 slot when activated.
- Instagram embeds are still created only after the selected card is activated. A live status identifies loading and delayed/error states; an always-visible link opens the original post so login walls and blocked embeds have a usable route out. The open profile action, canonical permalink, creator attribution and existing six curated items remain intact.
- Carousel arrows now work at phone and desktop widths, have 44px targets, and disable at the actual scroll ends. (Follow-up, Claude: they use `aria-disabled` so a focused arrow keeps focus at the end; activating a card moves focus to "Open original"; verified visible at 375/390.) Touch still uses native horizontal scrolling and snap points. Reduced motion selects an immediate scroll.
- Wall entries require explicit consent and non-empty student wording and names. Initials use grapheme clusters where supported; detail is omitted when missing. Long names and quotes wrap without squeezing the avatar or truncating student wording.
- Four or more wall entries use two slow opposing tracks with an explicit pause/resume button. (Follow-up, Claude: short lanes repeat hidden copies to at least four cards so the loop never shows an empty stretch; drift is ~16px/s per lane.) Visual loop copies use `aria-hidden` and `inert`. With reduced motion the layout becomes a static grid. Zero entries render nothing in the component; the development route explains this state.

## Prototype comparison and choice

The isolated `/preview/wall` exploration used the same clearly marked placeholder dataset and compared three layout answers:

| Direction | Layout axis | Tradeoff |
| --- | --- | --- |
| Quiet grid | Stable cards with no movement | Easiest to scan, but does not use the horizontal width well for larger collections. |
| Editorial feature | One large lead quote beside supporting cards | Gives one student more weight and uses more vertical space; risks implying a featured endorsement. |
| Twin tracks | Two opposing rows with a direct pause control | Shows a larger collection at once and retains control, with motion as the cost. |

Selected Twin tracks for four or more entries: every student quote keeps equal visual weight, and visitors can stop movement directly. The prototype picker and alternate compositions were removed after selection. The route remains as a development-only worst-case fixture for 0, 1, 3, 4 and 12 entries at `/preview/wall?count=...`; its placeholder text is labeled and is never imported by the landing page.

The separate Instagram cover exploration compared (1) a sparse dark identity cover, (2) a framed Instagram-like skeleton, and (3) an authored typographic cover with a small orbital graphic. Direction 3 was integrated: creator identity and the media type are prominent without implying a fabricated caption, photograph, like count or post topic.

## Skill-use matrix

| Skill | Phase | Applied decision or artifact |
| --- | --- | --- |
| `animate` | Implementation | Kept only the slow explanatory track motion; CSS linear transform loop, explicit pause, reduced-motion static grid. Did not animate frequent card activation. |
| `animation-vocabulary` | Design | Named the repeated track as a linear marquee; the preview alternatives varied layout and reading hierarchy instead of merely changing color. |
| `apple-design` | Interaction and type | Kept scrolling under direct user control, used native scroll rather than custom touch gestures, preserved legible line height, and omitted absent attribution instead of inserting a placeholder dash. |
| `prototype` and `prototype/PICKER.md` | Exploration | Built three distinct wall directions in the dev preview with the prescribed keyboard and URL picker, compared tradeoffs, integrated Twin tracks and removed the picker/alternates. |
| `break-ui` and `break-ui/CATALOG.md` | Fixture coverage | Added 0/1/3/4/12 cases, a one-letter name, missing detail, long plausible name, diacritics, long text and mixed metadata. The fixture control persists `count` in the URL. |
| `review-animations` and `review-animations/STANDARDS.md` | Final motion review | Confirmed linear marquee timing, transform-only loop, explicit pause state, reduced-motion fallback and hover-capability gating. No animation was added to carousel content changes. |
| `mobile-native` | Responsive implementation | Kept native touch scrolling, visible keyboard-operable arrows at every width, 44px controls, stable vertical media ratio, and pointer-capability-gated hover styling. Hardware feel remains unverified. |
| `pick-ui-library/PICKER.md` | Component choice | No dialog, menu, drag interaction or shared-state need was found; native buttons, links and CSS fit the component without adding a dependency. |
| Next.js local Server/Client, CSS, and Page/searchParams guides | Framework work | Kept browser state in narrowly scoped Client Components, kept the preview route server-gated in production, and used the current async `searchParams` page API. |

## Verification and remaining limits

- Targeted ESLint passed for `CreatorReels.jsx`, `WallOfLove.jsx`, `preview/wall/page.jsx` and `preview/wall/SocialWallPreview.jsx`.
- The parent task owns browser validation. Review `/` and `/preview/wall?count=0`, `1`, `3`, `4`, and `many` (12) for keyboard controls, carousel ends, embed activation/direct-link fallback, quote wrapping, pause/resume and reduced motion. No Instagram iframe was activated during this code pass.
- Real consented testimonials and permitted media covers were not supplied. The public Wall of Love remains hidden; the local CSS covers are not used as post imagery. No external image-generation or paid generation was used.
- Real phone hardware, embed login-wall behavior and Instagram's cross-origin blocked state remain unverified. The direct original-post link remains present because a cross-origin iframe cannot reveal its internal login/error content reliably.
