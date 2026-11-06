# Astra UI and motion refinement handoff

## Copy-ready execution prompt

You are continuing MockMob in this existing local workspace:
`C:\Users\atish\Desktop\mockmob copy\mockmob copy`.

Act as a senior product designer, design engineer and frontend implementer. Claude and I have spent substantial time improving this website. I consider the current homepage approximately 9/10. Your task is to push its craft toward 10/10 and bring every remaining student-facing page and section up to the same standard. That rating describes my ambition, not a measured acceptance result. Preserve the work that gives the site its identity. Study the current rendered product before deciding what to change.

This is an implementation request. Complete the design, code and verification in coherent stages. You have explicit creative delegation for routine visual and interaction decisions. Continue relevant unfinished UI work from the project brain. Do not stop at an audit, plan, first attractive screenshot or homepage-only pass. Keep a route checklist so scope survives context compaction. Do not expand this UI task into an unrelated backend rebuild or production rollout.

### 1. Establish current authority and protect the baseline

Read `AGENTS.md`, `PRODUCT.md`, `DESIGN.md`, then `docs/brain/README.md`. Read `ROADMAP-2027.md`, the newest entries at the TOP of `STATUS.md`, `CLAUDE-WORKLOG.md`, `IMPLEMENTATION-2027.md`, `LEARNING-DEPLOYMENT.md`, and `CLAUDE-MASTER-HANDOVER.md` as needed. Current roadmap and owner decisions override historical prose. DESIGN.md contains superseded descriptions followed by later Night Arena, daylight-theme and app-shell refinements; resolve those layers against the actual current code.

Inspect Git status and diffs first. This checkout contains extensive existing tracked edits and untracked implementation files. Preserve them. Never reset, clean, revert broad changes, overwrite Claude's working features, or treat every untracked file as disposable.

Use the existing dev server when available. During handoff preparation it was at `http://localhost:3000`, Next.js PID 19012; this is a snapshot, verify it now. Use `npm.cmd` in PowerShell. Read relevant installed guides under `node_modules/next/dist/docs/` before framework changes. The stack is Next.js 16.2.4, React 19, Motion v12, Tailwind v4, lucide-react and Chart.js. Prefer existing components, tokens and dependencies.

Capture the current homepage in both themes on phone and desktop, then key interactive states. Record what is already excellent and should stay. Make a page inventory from the source routes and actual navigation. Compare before and after at matching dimensions and states.

### 2. Explicitly use all 15 skills with depth and correct scope

Read the FULL SKILL.md of Scroll Craft:
`C:\Users\atish\Desktop\mockmob copy\scroll-craft-main\plugins\nateherk-design\skills\scroll-craft\SKILL.md`.

Read the FULL SKILL.md for EACH of these 14 skills under:
`C:\Users\atish\Desktop\mockmob copy\mockmob copy\.agents\skills\<name>\SKILL.md`:

1. `animate`
2. `animate-expo`
3. `animation-vocabulary`
4. `apple-design`
5. `ask-sonner`
6. `break-ui`
7. `emil-design-eng`
8. `find-animation-opportunities`
9. `improve-animations`
10. `mobile-native`
11. `pick-ui-library`
12. `prototype`
13. `review-animations`
14. `write-swift`

Read the relevant referenced documents fully when their workflow applies. For Scroll Craft, include hero-depth, approved-collection, uniqueness, feel, devices, taste and verify before design/implementation of the relevant marketing surface. For Emil's skills, load AUDIT.md, PLAN-TEMPLATE.md, STANDARDS.md, RECIPES.md, CATALOG.md, PICKER.md and Sonner API.md where needed. Avoid truncated reads: read large files in successive bounded chunks.

Create a skill-use matrix: name, applicability, phase, concrete artifact or check. Merely naming a skill is insufficient. Use this staged synthesis:

- `emil-design-eng`: overall craft, typography, layout, states and cohesion.
- `improve-animations`: deep read-only motion audit and precise plans; then switch to `animate` for implementation. Keep those roles distinct.
- `find-animation-opportunities`: identify the few highest-value missing transitions and explicitly reject distracting ones.
- `animation-vocabulary`: name the planned motion precisely.
- `animate`: implement purpose-driven, interruptible, token-based web motion.
- `apple-design`: direct feedback, momentum where relevant, spatial continuity and typography; preserve MockMob's visual identity.
- `mobile-native`: safe areas, viewport units, input size, touch feedback, keyboard and scroll behavior, capability-gated hover.
- `pick-ui-library`: assess component needs against installed dependencies. Avoid dependency churn or importing a library just to demonstrate use.
- `ask-sonner`: use for meaningful notification work if Sonner is selected; do not replace a sound existing toast system without a concrete benefit.
- `prototype`: explore three meaningfully different variants only for the highest-impact unresolved design choices, in an isolated development surface. I explicitly delegate selection of the best variant to you: compare them, choose, explain briefly and integrate. Do not stop to ask me to choose.
- `break-ui`: stress-test and fix all relevant confirmed UI failures. I explicitly authorize the fix phase and routine wrap/truncate/layout decisions. Keep fixture controls development-only.
- `review-animations`: review the final changed motion and repair confirmed findings before delivery.
- `animate-expo` and `write-swift`: read and assess, but mark direct implementation inapplicable unless actual authorized Expo/React Native or Swift work exists. This website task does not authorize creating a native app or changing the stack. Do not pretend native APIs apply to Next.js.

My explicit delegation supersedes optional interview/selection/stop checkpoints inside skills. Write Scroll Craft's brief as `Self-authored under explicit creative delegation`, distinguishing my stated preferences from your authored decisions. Use its journey, feeling curve, grammar, peak and signature-move discipline to improve this existing page. Its engine is designed for standalone HTML: adapt the design principles to semantic React and the current Motion/CSS system; do not replace the app with a disconnected HTML demo or add a second animation runtime without justification. Keep its external source folder unchanged. Keep build notes and any fingerprint registry inside this writable project if needed.

Do not use skill quotas to add filler, long pinned spans, compulsory video or decorative interactions to study screens. Marketing can be expressive; daily practice must feel fast, calm and legible. Accessibility, truthful content and the budget-Android/patchy-4G constraint govern every interpretation.

### 3. Refine the homepage and finish new sections

Preserve the volt identity, Gabarito/Hanken/mono typography, grid/dot depth, framed practice bay, keycap controls, theme toggle, original campus illustrations, five-question demo and NTA/MockMob comparison. Refine spacing, contrast, composition, responsive hierarchy, transitions and section-to-section pacing. Keep the primary next action obvious. Do not introduce variable-width headline/CTA jitter, moving hover hit targets or global overflow rules that break sticky positioning.

Audit every homepage section: hero, Mistake Lab, subject strip, DU Compass, eligibility teaser, campus destinations, exam comparison, live stats, product screens, steps, subject cards, Instagram, Wall of Love, pricing, FAQ, closing band, navigation and mobile dock. Give different sections appropriate treatments instead of identical reveal animations everywhere. Use the product's working interactive demonstrations as potential signature moments; invent another only when it earns its place.

**Instagram:** already implemented in `src/components/landing/CreatorReels.jsx`, `src/lib/social.js` and `src/app/social-proof.css`. There are three creator reels and three MockMob posts. It is a curated strip, not a live-synced feed. Improve card composition and browsing; real permitted covers are preferable to the current generic play-button covers. Preserve attribution, canonical links and click-to-load embeds, with no third-party requests before activation. Handle unavailable/private posts, blocked embeds and login walls with a clear direct link. Check switching active cards, keyboard use, touch scrolling, arrow end states and fixed media geometry. Never fabricate creator imagery, likes, captions or endorsements.

**Wall of Love:** already implemented in `WallOfLove.jsx` and `src/lib/voices.js`; `/preview/wall` is a development-only placeholder preview. VOICES is empty, so production correctly hides the section. Improve and stress-test the layout, including 0, 1, 3, 4 and many entries, long quotes/names, focus, reduced motion and pauses. Make duplicates in any loop inaccessible to assistive technology and provide an accessible way to pause automatic movement if needed. Publish only real supplied quotes with documented consent. Do not copy unverified quotes from the old live site or generate testimonials, student avatars, ranks or outcomes. If no real quotes are available, finish the reusable component and leave the public section hidden; this content dependency must not block other work.

**DU Compass:** the current interactive landing section is `CompassLadder.jsx`, `src/app/compass-ladder.css`, `src/lib/du/showcase.js`, using `public/du/2026`. Refine it together with `/admission-compass` and `/cuet-cutoff-calculator`. The score currently sweeps automatically until the visitor interacts. Evaluate whether this interferes with reading, causes unnecessary React work or distracts from the tool; make user control and pause behavior explicit, or use a short introductory demonstration followed by a stable state. Improve score entry/slider, controls, mobile result readability, legends and the relationship between the teaser and full tool.

Show explicit data year/cycle, programme, category, round and source. As of 3 October 2026, the 2026 dataset is not 'last year'; replace relative year wording with the exact historical cycle after checking sources. A missing cutoff does not prove 'no seats'; inspect that current label and distinguish missing data from validated seat information. Preserve exact eligibility rules, subject aliases, selected-subject persistence, share links and live results. Historical thresholds do not establish admission chances or convert mock marks into CUET scores. Review the showcase's score axis against the actual dataset rather than assuming it fits every programme.

### 4. Bring remaining pages to the same standard

Prioritize pages recorded as untouched/unverified, but inspect their CURRENT implementation before classifying them. Route checklist should include:

- Today, Practice/dashboard, branded runner, NTA runner, Result, Radar/analytics, PrepOS/mentor, Review, Recovery, Progress, Admission Compass and the cutoff calculator.
- Saved, Explore, Leaderboard/Ranks, AI Rival, Contribute/upload, My uploads, Profile/Account and onboarding.
- Login/signup, Pricing and PrepOS pricing, Features, About, Contact, CUET subject hubs, CUET 2027 guide and SEO entry pages.
- Legal pages: typography, readability, navigation and theme consistency; preserve substantive terms.
- Moderator/admin surfaces only where shared styling changes affect them or a concrete remaining UI issue is in scope; preserve role boundaries.

Use shared primitives to achieve consistency without flattening purpose-specific layouts. Preserve the intentional conventional NTA console skin. Check empty, loading, error, unavailable, no-history, free, Pro, expired and paused states. Use existing development previews and account API stubs for inaccessible signed-in views. Never claim a stubbed preview proves real authentication, persisted results, entitlement enforcement or billing.

Keep a focused list of behavioral defects discovered while doing UI work. Repair scope-relevant issues only after tracing their contracts; distinguish reproduced defects from hypotheses. Carry unrelated product, staging and content-release gates forward in the project brain rather than silently closing them.

### 5. Use the built-in ChatGPT image generator when it improves the result

You are explicitly encouraged to generate or edit purposeful visual assets when existing assets and code-native shapes cannot provide the needed quality. First read:
`C:\Users\atish\.codex\skills\.system\imagegen\SKILL.md`.

Use the built-in image-generation tool exposed in this environment as `image_gen.imagegen` (in code tools: `tools.image_gen__imagegen`). If it is deferred, discover the image-generation tool by name/description. Do not assume a prompt creates tool access. If it is unavailable, report that limitation and complete work using available assets; do not silently switch to a paid API or kie.ai.

For built-in generation, no OPENAI_API_KEY is required. Make a concise asset brief specifying its actual UI purpose, art direction, composition, aspect ratio, palette and constraints. For new images omit reference-image arguments. For local edits inspect the file with view_image, then provide referenced_image_paths; preserve identity and use a sibling versioned filename. For cutouts request transparent_background=true and inspect actual alpha.

Inspect every output at its intended rendered size and mobile crop. Copy selected outputs into this project's public assets, optimize to suitable WebP/AVIF/PNG, supply dimensions and appropriate alt text, and keep text and interactive UI as real markup. Respect the existing illustrated campus direction and clearly label illustrations. Generated artwork is never evidence of students, creators, admission outcomes or testimonials. Save the final prompts, selected filenames and generation method. Keep paid API generation outside this workflow unless explicitly authorized and routed through the existing persistent budget guard; never bypass the $2 calibration/$10 lifetime content ceiling.

### 6. Verification and delivery

Verify the rendered product throughout implementation, not just at the end. Use actual pointer interaction, keyboard navigation and touch emulation; programmatic DOM clicks can bypass overlays. Cover both themes and representative widths: 320, 375/390, 768/820, 900/1024, 1280/1440 and 1920/3440, plus short landscape and 200% text zoom. Exercise reduced motion in the browser, rather than claiming a CSS review is a test.

Inspect scroll entrances AND intermediate positions; interrupt/reverse toggles, drawers and carousels. Check no layout shift on demo answers, headline/CTA hover, media activation or results updates. Check menus, focus visibility/order, disabled states, overflow, sticky bars, bottom-dock occlusion, safe-area padding and reading contrast in hover/focus/pressed/selected states. Exercise the full five-question demo and comparator state preservation. Check Compass filters, missing-data states, subject aliases and share/edit/recheck behavior.

Run lint and production build, `npm.cmd run test:recovery`, relevant existing question/payment suites, `test:nta`, `test:answer-integrity`, `test:du` for admissions work, and `test:learning` for connected learning/social/offer changes. Run `node --test data/tests/payment_entitlements.test.mjs` when relevant. Do not run scripts that call paid models or mutate the bank as part of UI verification. Re-run appropriate checks after fixes; do not repeatedly run broad suites without a new reason.

Compare asset bytes, JavaScript impact and layout/performance before and after. Use Lighthouse and CPU/network emulation if available; label them as lab evidence. Real-device behavior remains unverified unless actual hardware was used. Do not promise 60fps or call a screenshot a functional test.

Keep server-authoritative scoring, session resume/idempotency, atomic practice credits, AI-wallet reservations, existing paid entitlements, release flags and Razorpay flows intact. Pricing follows `src/lib/payments/offer.js` and actual configuration: monthly ₹99 is gated; one-time buyers retain their term. Keep evidence rules, uncertainty quarantine and provisional CUET 2027 rules. No implicit production migrations or bank mutation. Deployment, purchases and production data actions are outside this local UI task.

Record actual verification, route completion, screenshots, unresolved gates and rollback boundaries in `docs/brain/STATUS.md`. Save a short before/after review with evidence and a skill-use matrix. Final response: what improved, pages completed, tests actually run, visual/functional checks, image assets, remaining content/access/deployment dependencies and local preview URL. Be concise and candid. Continue until the authorized UI scope is complete or a concrete dependency prevents a specific part; finish independent work and name the precise blocked part.

## Preparation evidence (3 October 2026)

This handoff was prepared from current source, the latest Stage R/R2 status, and a limited live local-browser inspection of the homepage at phone and desktop sizes, including the DU Compass and dark Instagram strip. The current homepage has the Mistake Lab, Compass ladder, calculator teaser, campus illustrations, comparator and curated social strip. Wall of Love is intentionally hidden by an empty consented-data list. The creator cards currently use generic local covers; embeds were not activated in this preparation pass. Signed-in routes, real checkout, real-device performance and all motion states were not verified here. Historical Claude test counts are historical evidence and were not rerun during prompt preparation. No application code was changed by this handoff preparation.
