# MockMob round 4 — restore craft, then build a real mascot-guided journey

You are continuing MockMob in C:\Users\atish\Desktop\mockmob copy\mockmob copy. Act as a senior product designer, motion designer and frontend engineer. This is an implementation assignment, not just an audit. I am the owner and give you creative delegation: explore, choose, implement and verify without asking me to choose routine variants. Use your strongest available reasoning/model setting; this prompt is portable across Claude and a larger OpenAI model.

## Owner's latest feedback

The mascot and overall work are good, but Pip has not been integrated properly using Scroll Craft as an animated guide throughout the website. Make the character feel connected to the journey, rather than separate stickers with slight drift.

Some previously excellent animation, optimization and small UI refinements regressed. The homepage MockMob/NTA-style comparison now has boxes behaving strangely. Arena entry animation is missing. Practice lost some motion, including the exam-day/NTA card and its animated clock treatment. Restore what worked before and then improve it. These corrections are the foundation; also make the larger, high-value improvements in the five priorities below.

## Read and protect the existing work

Read AGENTS.md, PRODUCT.md, DESIGN.md, docs/brain/README.md, ROADMAP-2027.md and the latest STATUS.md entries. Then read ROUND3-NOTES.md and BRAND-MASCOT.md. The original round-3 request remains in ASTRA-ROUND3-PROMPT-2026-10-03.md; use it for unfinished scope, subject to this newer feedback.

Inspect git status and current diffs. This checkout contains extensive user/Claude changes and untracked features. Preserve them. Never git reset, clean or bulk-restore. HEAD is not the previous polished working-tree baseline. Selected pre-edit snapshots are in artifacts/round3/before-source; their coverage is incomplete. Restore targeted behavior, not entire files.

Read relevant installed Next.js 16.2.4 guides in node_modules/next/dist/docs before framework code. Use npm.cmd in PowerShell. Last known local dev URL was http://127.0.0.1:3000; verify it rather than assuming a server/PID is unchanged.

## Skills are mandatory working methods

Read fully and apply Scroll Craft at:
C:\Users\atish\Desktop\mockmob copy\scroll-craft-main\plugins\nateherk-design\skills\scroll-craft\SKILL.md

Also read its references/hero-depth.md, feel.md, devices.md, uniqueness.md, approved-collection.md, taste.md and verify.md. Follow the feeling curve, grammar selection, engineered peak, signature move, intermediate-position verification and device floor. Extend the existing self-authored brief in scrollcraft/builds/mockmob-round3/BRIEF.md or write a round-4 brief marked "Self-authored under explicit creative delegation".

Read and genuinely use every relevant Emil Kowalski skill under .agents/skills:
emil-design-eng, animate, improve-animations, review-animations, find-animation-opportunities, animation-vocabulary, apple-design, mobile-native, break-ui, prototype, pick-ui-library and ask-sonner.
Read their applicable referenced recipes, standards and picker files. animate-expo/write-swift do not apply.

Use prototype for the biggest open question: build three structurally different mascot-guide/choreography directions, not color variants. Choose the winner yourself, as authorized, after comparing desktop/mobile clarity, interaction cost and performance. Keep screenshots and decision rationale. Use improve-animations before changing motion and review-animations after. Keep a short matrix: skill → applied decision → actual artifact/browser evidence. Do not merely name the skills.

## Five implementation priorities, in order

### 1. Recover the animation and layout baseline

Inventory what was good before round 3 using the working-tree snapshots, screenshots, current source and owner feedback. Restore the Arena entry sequence and purposeful Practice selection/NTA preview/clock details. Check the full chain of theme, hover, focus, navigation, resize and remount.

Start at src/app/(app)/arena-support.css. It currently suppresses .view entry animations, .pr-nta__console transforms/transitions and .pr-nta__palette em animation outside reduced motion. The original effects still exist in arena.css/globals.css. These are confirmed suppression sources; replace broad overrides with narrowly justified rules. Inspect the timer/countdown components too: the owner's exact clock regression has not yet been isolated. Keep the actual timed answering surface calm while retaining crafted selection, entry and marketing motion.

Repair ExamComparator.jsx with home-refinements.css and brand-pip.css. New 44px targets, eight-column palettes, mobile span-two buttons and decorative placeholder spans may conflict. Reproduce both MockMob and NTA skins at narrow/tablet/desktop sizes, then fix track sizing and hit-area strategy. Preserve the NTA visual grammar and real state transitions; decorative cells need not be interactive. No stretched boxes, clipped rings, palette overflow or layout jumps when switching skin.

Acceptance: matched before/after screenshots plus actual pointer and keyboard checks of both skins, Arena entry and Practice card. No blanket "animation:none" cure and no undoing unrelated round-3 improvements.

### 2. Turn Pip into a coherent Scroll Craft guide

Use the existing original character and all seven source PNGs. Build one recognizable narrative: greeting at the hero → thinking at Mistake Lab → pointing at the Compass numbers → celebration/resolution at the close. Engineer the strongest moment around turning one illustrative mistake into a useful next practice step.

Prototype three approaches such as a continuous desktop travel lane, pose handoffs anchored to sections, and a compact phone guide. Pick a coherent system, adapting it across devices rather than forcing desktop pinning onto phones. The character should acknowledge entrances, react to the current section and guide attention. Use small, intentional blink/lean/gesture/settle accents where appropriate; do not stretch whole raster poses unnaturally or promise animation a static image cannot express.

Make the same voice appear selectively in onboarding, first-run help, empty/loading/error states and completed sessions. Static guidance on study pages is fine; no hovering/looping character while answering. Never obscure copy, charts, buttons, focus or the mobile dock. No mandatory scroll hijack or long empty spacers.

Reuse semantic React, existing CSS/Motion and progressive scroll capabilities. Prefer transform/opacity with reserved dimensions, lightweight assets and a clear reduced-motion fallback. Add a new runtime only with a concrete measured need. Validate intermediate scroll positions and reverse scrolling, not only section endpoints.

### 3. Establish a consistent motion system across the product

Build a small documented vocabulary for entrances, section reveals, active navigation, disclosure, hover/focus, loading and completion. Preserve the existing signature depth and playful details that earn attention. Distinguish landing storytelling, Practice selection and high-frequency exam answering.

Audit homepage, Explore, Today, Review, Progress, Radar, Compass, Saved, Ranks, Account, Contribute, My uploads, PrepOS, Result, Rival, onboarding and auth. Improve timing, easing, interruption behavior, content resizing and focus continuity. Respect reduced motion without disabling crafted motion for everyone.

Consolidate competing CSS only after tracing specificity and imports. Avoid transition:all, unnecessary layout animation, long per-item delays, excessive will-change and continuous offscreen loops. Keep fonts, both themes, campus illustrations and volt identity.

Acceptance: a concise motion decision table and regression evidence, including transitions back to a page, theme changes, long text and narrow/short screens.

### 4. Make the practice-to-review journey feel like one product

The major product improvement is continuity: Practice → recorded Result → Review/Saved → one honest next action. Use existing server-backed facts and stable routes, without inventing diagnosis, mastery, streaks or score gains. Make the next action and return path obvious.

Finish Explore's study ergonomics: native subject/chapter/difficulty filters, grouped/flat chapters, keyboard solving, locked feedback, explanations, server-confirmed saves/votes, held-row pagination, recoverable errors and end states. Preserve eight existing logic tests and add only meaningful tests for changed behavior.

Verify the latest safeguards for summary ordering, pagination focus, drawer focus, More navigation, Result ID changes and onboarding failure recovery. Test free/Pro/expired, 402 save limits, vote rollback, failed catalog/chapter/feed loads, no-history, long names, retained upload drafts and stale subject selections. The development fixture blocks real writes; do not treat it as proof of live persistence.

Use Pip as occasional contextual guidance rather than replacing useful data or generating fake personalized advice. Keep one clear action, truthful limitations and visible recovery/edit paths.

### 5. Finish responsive, accessibility and performance acceptance

Maintain a source-derived route checklist. Test all public and student-facing Arena routes at 320, 360, 390, 768, 820, 1024, 1280, 1440, 1920 and short landscape, both themes, 200% text, reduced motion, keyboard and genuine touch emulation. Use real pointer/hit-testing, not programmatic DOM click shortcuts.

Check long subject/college names, target hit areas ≥44px, focus visibility, contrast ≥4.5:1, clipping beyond root overflow, sticky/footer/dock occlusion, safe areas, loading/error/empty states and scroll restoration. Measure budget-Android costs: optimized images, lazy loading, animation work while offscreen, layout shifts and actual loading behavior under throttled conditions. State when the tool cannot emulate a condition; never substitute source inspection for a real-device test without labelling it.

Fresh lint/build and 158 tests passed at the handoff, but final visual/interaction acceptance is incomplete. Initial raw measurements and screenshots in artifacts/round3 are checkpoints, not certification. Complete the test runner's actual start/resume/interface-switch/key handling and failure recovery with fixture-safe data; never start a real paid checkout.

## Mascot source package

Original transparent PNGs:
artifacts/round3/mascot-high-resolution-png/

Files: pip-character-sheet.png, pip-greeting.png, pip-thinking.png, pip-pointing.png, pip-celebrating.png, pip-idle.png, pip-encouraging.png.
These are unchanged lossless originals, approximately 1.2–1.3K pixels, not enlarged WebP exports. manifest.json records dimensions, alpha range, bytes and hashes. Zip: artifacts/round3/MockMob-Pip-original-PNGs.zip.

Use public/brand/mascot/*.webp for ordinary website delivery; explicit dimensions and loading rules are already in src/components/brand/Mascot.jsx. Keep the PNGs as design masters. Prompts/source receipts: artifacts/round3/mascot-generation.json and docs/brain/BRAND-MASCOT.md. Do not regenerate the character unnecessarily. If genuinely needed, use available built-in image generation with the character sheet as identity authority; no paid API or Kie.

## Non-negotiables

Current product direction: Score Recovery Lab for CUET UG 2027 Commerce. Preserve server scoring, resumable sessions, atomic credits, AI-wallet reservations, entitlements, quarantine and release flags. No forced publication or claim that model agreement proves truth.

No deployment, production migrations, bank mutation, external messages, paid model calls, Razorpay plan creation or checkout. Keep publicOffer() as pricing authority; monthly ₹99 only opens when RAZORPAY_PLAN_ID_PRO_MONTHLY_99 is configured. Keep voices.js empty, truthful dated creator attribution/partnership markers, independent NTA/DU disclaimer, Compass "projection, not prediction" and eligibility ≠ admission.

## Verify and deliver

Run npm.cmd run lint, npm.cmd run build, test:recovery, test:du, test:learning, test:nta, test:answer-integrity, node --test data/tests/payment_entitlements.test.mjs and the Explore/contribution tests after relevant changes.

Update STATUS.md with exact checks, remaining gaps and targeted rollback boundary. Deliver before/after screenshots, intermediate mascot journey states, both exam skins, the five implemented priorities, skill-use matrix and honest limitations. Do not stop at a plan, one attractive screenshot or a generic redesign. Restore the earlier craft, make the mascot journey intentional, and complete the work you can actually verify.
