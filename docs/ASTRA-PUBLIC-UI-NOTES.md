# Astra public subpage review — 3 October 2026

Scope: login, signup, onboarding, pricing, about/contact/features, CUET guide and
SEO pages, legal-page typography, and a read-only audit of `ToastProvider`. The
homepage, calculator, social surfaces, shared navigation/footer, layout, and global
stylesheet were outside this pass. The checkout and legal terms were not changed.

## Route checklist

| Route | Review result |
| --- | --- |
| `/login` | Inspected; existing daylight auth shell and form hierarchy retained. |
| `/signup` | Inspected; shares the auth shell and usable form layout. |
| `/onboarding` | Inspected; subject selection and fixed continue action retained. |
| `/pricing` | Inspected; offer content remains driven by `publicOffer()`. No price or term edits. |
| `/pricing/prepos` | Inspected; wallet and paused-purchase state retained. |
| `/about` | Replaced unsupported comparisons and overbroad content-certainty claims with product-specific, qualified language. |
| `/contact` | Removed unverified response-time/service promises; clarified reporting and partnership requests. |
| `/features` | Updated stale score-outcome, AI Compass, and community-quality claims. Removed decorative repeating motion and shortened the desktop hover response. |
| `/cuet/[subject]` (six published hubs) | Corrected chapter headings to describe syllabus lists rather than bank coverage; clarified variable inventory and provisional 2027 rules. |
| `/cuet-2027` | Marked 2027 rules as pending; removed unverified paper counts, time, marking, and date-based study claims. |
| `/cuet-mock-test-free` | Replaced an unsupported speed-of-improvement claim with a specific review action. |
| `/cuet-previous-year-questions` | Reframed as a practice/review guide and stated that MockMob does not claim a verified historical question inventory. |
| `/cuet-practice-tests-online` | Inspected; no focused presentation fix identified in this pass. |
| `/terms`, `/privacy`, `/refunds` | Inspected typography and layout; existing 70ch measure and generous line-height are readable in source. No legal substance or typography change warranted. |
| Shared `ToastProvider` | Read-only assessment; no changes. See library and motion notes. |

The checkout already contained numerous user-authored tracked and untracked edits.
They were preserved. The `features/page.js` working-tree diff also contains earlier
in-progress changes outside this pass; this note describes only the focused edits
made here.

## Focused implementation

`src/app/public-polish.css` is imported by the Features page and scopes its rules to
`.mm.public-features`. Feature-card decoration now appears only on hover-capable
fine pointers. Icon feedback is limited to a 1.04 scale over 150ms; the dot layer
fades over 160ms. Reduced-motion users get no transform or opacity transition.
Removed the 4.2-second repeating step pulse and the repeating dot animation on
touch devices. These loops added continuous decoration to a one-time information
page without explaining product behavior.

Copy fixes align the owned public pages with the current product contract: practice
outcomes are not presented as guaranteed, historical DU thresholds are separate
from practice marks, recovery and AI are not described as universally live, and
subject hubs do not imply that the entire published syllabus has question
inventory. Legal and pricing terms remain untouched.

## Library and toast assessment

`package.json` includes `motion` v12, Tailwind, `clsx`, and `class-variance-authority`;
Sonner and a general component library are not installed. The simple card hover
needed no new dependency or Motion runtime. `pick-ui-library` therefore led to no
library change.

`ToastProvider` is mounted through the app provider and exposes success/error
messages with `status`/`alert` roles, a close control, optional link, and 3.2-second
auto-dismiss. It is a small existing system used by account, upload, and moderation
flows. Sonner could add queue/swipe behavior, but there is no concrete benefit in
this public-subpage task that justifies replacing it or changing the shared app
surface. The Sonner API skill was read for comparison; no Sonner behavior was
implemented.

Motion review was source-based; no browser feel claim is made here. The Features
page contained 500ms icon scaling, 700ms hover fades, and multiple infinite
4.2-second decoration loops. The hover effect is now short and capability-gated;
the loops were removed. Auth, onboarding, articles, legal pages, and pricing do not
need additional motion. Toasts enter immediately; leaving that high-frequency
shared feedback path untouched was appropriate for this scope.

## Shared navigation and mobile dock review

`NavBar.jsx` has a labelled menu toggle, `aria-expanded`, Escape-to-close, outside
pointer dismissal, link-close handlers, visible focus styling from the global
`:focus-visible` rules, 48px toggle target, and passive scroll tracking. I found no
confirmed keyboard-navigation failure in source. One markup issue to check: while
closed, the toggle still references `mm-nav-sheet` with `aria-controls`, but the
conditionally rendered sheet and ID are absent. Keeping the target mounted with
`hidden`, or dropping `aria-controls`, would remove that dangling reference.

`MobileDock.jsx` uses the safe-area inset and a fixed 48px action target. Its spacer
is a fixed 78px even though dock height can grow with wrapped copy and the safe
area. The public menu can also expand below the sticky header while the dock stays
fixed. These are source-based edge cases, not reproduced failures; the parent
should check 320px width, short landscape, long dock notes, and an open menu against
the dock in the browser.

## Skill-use matrix

| Skill | Applicability | Phase | Concrete artifact or check |
| --- | --- | --- | --- |
| `pick-ui-library` | Applicable | Assessment | Checked installed dependencies; retained CSS and current toast provider. |
| `ask-sonner` and `API.md` | Applicable to the toast audit | Assessment | Read setup, styling, positioning, and API guidance; no provider replacement. |
| `improve-animations`, `AUDIT.md`, `PLAN-TEMPLATE.md` | Applicable | Read-only audit | Audited purpose, frequency, duration, capability gating, and reduced motion; identified unnecessary repeated feature-card motion. |
| `find-animation-opportunities` | Applicable | Read-only audit | Evaluated public-page motion seams and rejected additional entrances or article/pricing animation. |
| `animate-expo` | Not applicable | Full read | Website is Next.js; no native animation changes. |
| `write-swift` | Not applicable | Full read | No Swift files or native app scope. |

The audit-only skills were kept read-only. The feature motion edits were made under
the parent task's direct implementation authority, not as an extension of those
audit skills.

## Verification and remaining checks

`npm.cmd run build` passed on 3 October 2026 with Next.js 16.2.4. TypeScript and
static page generation completed for all 55 generated pages; the build reported
the existing Edge Runtime warning that disables static generation for that page.
No test suite or browser checks were run in this subtask. The parent agent owns
browser verification and project-level test execution. This pass used source
review only; rendered states and the navigation/dock edge cases remain to be
checked there. No `STATUS.md` change was made.
