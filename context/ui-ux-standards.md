---
title: UI/UX standards (tasteful and useful, not AI slop)
type: concept
status: current
owner_confirmed: owner mandate 12 Oct 2026 (rules below carry their own evidence)
updated: 2026-10-12
---
# UI/UX standards: tasteful and useful, not AI slop

**Read this before building, changing or reviewing any interface, in any project, even when nobody asked you to.** The owner's words: "These are the kinds of things I want my models to always take care of whenever they are performing: the UI/UX, the experience, and how the entire app and the experience are being built around something... AI models usually lag on that." [O1]

## How to use this page
- **Scale the effort to the change.** A copy fix needs a one-line check. A new screen needs the brief in section 1, and a new journey needs a full brief and the done-check in section 11 [R§11, R-099].
- **Precedence, highest first:**
  1. the owner's current instruction in the chat;
  2. the project's live design system and contracts (its tokens, type roles, components and accepted decisions);
  3. this page;
  4. installed design skills (impeccable, design-taste, high-end-visual-design and the others).

  General rules explain intent; they do not override a project's accepted system [R-300]. Where skills disagree with this page (gradients, glow, eyebrows, monospace labels, trailing arrows), this page wins, because it records the owner's taste [T, skill_conflicts].
- **Project addenda** are in section 12: MockMob (product, learning and gamification rules) and Continuum (its own visual language).
- **Every rule carries a source.** The legend is at the bottom; the full cited inventories are in audits/design/ui-rules-research.json (R-ids, 301 rules) and audits/design/ui-rules-taste.json (T-ids, 146 rules).

## The bar in one paragraph
Tasteful and useful means the screen answers the user's question at a glance. Its numbers are true and explained. Every state of every control is designed, and it looks like one deliberate product with a point of view. AI slop is the opposite: a plausible-looking default assembled from habits. Typical slop is gradient washes, glowing purple, identical rounded cards and pills, all-caps eyebrows, fake progress, invented numbers, hype copy, and missing empty, error and loading states. Clean alone is table stakes and is not the goal. The lasting difference is a product that feels intentional, alive and built around its own central idea [R-287, R-216, O2, T-002, T-015]. Judge at three layers: the first impression looks credible, use is fast, clear and accurate, and afterwards the effort led somewhere [R-125].

## 1. Before you build: a short experience brief
For a new screen or journey, answer these in a few lines before writing UI code [R§11.2]. Skip a line only when it truly does not apply.
1. **Job:** what the user is trying to get done here, and what happened just before (entry and continuity).
2. **Outcome:** what useful work becomes possible, and what the one primary action is.
3. **Data truth:** which data is real, provisional, missing, corrected or illustrative.
4. **States:** loading, empty, sparse, error, success, held or pending, interrupted, and return-after-days.
5. **Persistence and cost:** when the work counts as saved or accepted, and what is retried or paid.
6. **Feel:** reassure, clarify, encourage, acknowledge or concentrate. Name the emotional intent and where motion may help.
7. **Acceptance:** which rendered interactions and checks will prove it works.

Then design the whole journey as one orchestration (inputs, history, loading, actions, time, outcome), not one screenshot state [R-001, R-002].

## 2. Let the data decide the form
- Choose the representation from the decision the user makes [R-003, R-240, V]:
  - chips for small fixed category sets only;
  - aligned columns for comparable numbers;
  - a timeline for events;
  - ordered bars for ranking.

  A uniform table with nothing driving its form reads as unbuilt [V].
- Right-align numbers and use tabular numerals, with consistent precision and signs [R-005]. Use `font-variant-numeric: tabular-nums`, not monospace labels [T-050, A-008].
- Put the unit and the denominator next to every count, and keep distinct denominators distinct ("6 of 15 answered" is not "6 of 16 in the set") [R-006, R-182].
- No false precision: no percentages or decimals more precise than the sample supports. Flag small samples instead of headlining them ("1 of 1, 100%" is filler) [R-007, R-185, P].
- **Zero, unknown, missing and withheld are four different things.** Show each one truthfully; never render unknown as 0, and never show raw null/undefined [R-008, T-135].
- Give every number context: compared with yesterday, a trend, its age or its source. Use one meaning per number on a screen, and one definition per count across all pages [T-129, T-130, T-134].
- Truncate only long, low-value text, with the full text reachable by touch and keyboard. Never truncate names, costs, questions, answer options or disclosures [R-009, R-010].
- Muted or inactive rows keep readable contrast and a written state [R-011].
- When a correction changes an earlier result, annotate it; never silently rewrite history [R-014].
- Show only real, sourced numbers: no placeholders, demo figures or test data in real views [T-011, T-132]. Label illustrative mock-ups as illustrative [R-152, R-301].

## 3. Hierarchy, layout and spacing
- The first thing seen answers the user's immediate question. Build hierarchy from size, position and contrast: result and status first, then the pattern, then the next task [R-023, R-250]. Within a few seconds the reader should know what matters and what to do [T-010].
- **One dominant useful action per screen.** Give secondary actions clearly lower prominence, but still a visible hover, focus and pressed state [R-093, R-039, T-077].
- Give each page one visual anchor that carries real information. Fix a bland page with hierarchy and data, not decoration [T-008, A-024].
- Spacing comes from a 4-point scale, and gaps express relationships: tight inside a label/value pair, about 32px between independent groups. Grouping is itself hierarchy [R-026, R-251, R-252].
- Prefer generous whitespace over boxes. Use a card only when elevation means something; otherwise group with spacing, hairlines or a background change. **Never nest cards** [R-253, T-074].
- Avoid the generic three-equal-cards row and the "hero metric" template (big number, small label, three stats). Vary shape and weight by role [T-076, T-085, A-003].
- Floating UI (assistant balls, bars, chips, toasts) must never cover figures, text or controls at the target sizes. Pad scroll areas for fixed bars [T-095, A-001]. This is the most frequent defect found in reviews.
- No dead bands or empty voids. Anchor content to the top; empty lanes collapse to one quiet line [T-097, T-131].
- Show frequent actions directly and put rare ones behind a labelled disclosure (a popover or a "More" button), never hidden for good [R-018, R-245]. Detail panels keep the parent's scroll and state, close clearly, and return focus to their trigger [R-019, R-151].

## 4. Typography
- Use one good, deliberately chosen sans-serif family per product, and treat type as a first-class decision with a real scale and visible weight steps [R-028, R-254, T-004]. Do not reach for Inter, Roboto or Arial out of habit [A-014].
- Large headings: tighten tracking (about -2% to -3%) and use 110-120% line height. Never tighten small text [R-028, R-255].
- Use few sizes, by semantic role. A landing page needs at most about six; dense dashboards rarely go above 24px except for one hero figure [R-029, R-256].
- Set titles and key figures in heavy, tight, high-contrast type against small, muted, sentence-case support text [T-032].
- **Write labels in sentence case.** No tracked ALL-CAPS eyebrows, kickers above headings, numbered section badges ("01 / 02"), or a single accented word in a headline [T-061, T-062, T-063, T-064, A-012].
- Check real line breaks with long real labels, numerals and symbols, and keep a stable fallback font so layout does not jump [R-030, R-032].
- Show times in 12-hour format ("11:42 PM") [T-022, A-015].

## 5. Colour, surfaces and depth
- **Colour comes from meaning, not decoration.** Start from one primary colour, derive a ramp (washes, borders, fills, text roles), and add semantic colour only where it means something. Red is for states the user can and should act on; a low value is not automatically danger [R-015, R-033, R-243, R-259].
- **Use exactly one soft accent,** reserved for the primary action, the active state and the product's signature element. Everything else is neutral. Categorical colours stay within the system, with no rainbows [T-031, T-072].
- **Never carry state by colour alone.** Pair colour with words or an icon. Green, amber and red go on a thin bar or small tag, never as decoration [R-016, T-071].
- **No decorative gradients:** no washes, no gradient text, no gradient glows. The only gradient allowed is a functional scrim that makes text readable over an image, checked for worst-case contrast and with an opaque fallback [T-003, T-081, R-046, R-267].
- **No glow or neon halos** on elements, except a deliberate functional glow on a product's signature visual [T-080, A-009]. **No glass blur on content cards**; blur only for fixed or sticky chrome [T-082].
- **Dark mode uses neutral charcoal** (about #181818 ground and #212121 raised), not pure #000 and not blue- or indigo-tinted near-black. Raised layers are slightly lighter, borders are restrained, and chip saturation is softened [T-005, T-069, R-035, R-260].
- **Shadows are soft:** low opacity and high blur, stronger for popovers than for cards. If the shadow is the first thing you notice, it is wrong. No coloured zero-offset halos [R-036, R-261, T-079].
- No coloured side borders thicker than 1px on cards, rows or alerts [T-083].
- Do not copy another product's palette or signature motif [R-054].

## 6. Icons, buttons and complete state contracts
- Size icons near the adjacent text's line height; most icons are too large. Keep one icon style, stroke and baseline. The visible size and the hit area are different things [R-037, R-263].
- Buttons: horizontal padding about twice the vertical. The primary is filled; secondaries are outlined or text. No repeated identical pill trio on every row [R-038, T-077].
- **Specify every state of every control,** keyboard focus included [R-040, R-265]:
  - buttons: rest, hover, focus, pressed, disabled and loading;
  - inputs: empty, filled, focus, invalid and valid;
  - toggles, tabs and rows: their own sets.
- A disabled control explains itself when the reason matters, and loading never erases context [R-042].
- No emoji as icons or in text, and no arrows or chevrons appended to button or link text; use a real icon inside the control if one is needed [T-087, T-125].
- Hover may reveal affordances, but everything hover reveals needs a touch and keyboard equivalent [R-020, R-246, R-092].

## 7. Feedback, truth and copy
- **Never show success before the system has acknowledged it.** Model the real states: pending, sending, accepted, failed, uncertain and held. Never label local pending work as saved [R-041, R-091, R-045].
- **Show processing stages only when real system state backs them.** No invented stages or simulated percentages to make waiting feel better [R-055, R-279].
- Errors name a recovery action and preserve the user's work. Destructive actions state their consequence and offer undo where feasible [R-043, R-021].
- Empty and loading states say what to do next. Never show a wall of "unknown" or "not recorded" [T-117, A-005].
- Validate input when the user can act on it, not while they are mid-word [R-044].
- **Write copy that is plain, concrete and honest:**
  - concrete verbs and real evidence ("You missed 4 of 9"), not hype ("Unlock your superpowers") [R-156, R-080];
  - none of the AI clichés: Elevate, Seamless, Unleash, Next-gen, Game-changer, Delve;
  - no exclamation marks on success messages [T-123];
  - no middle-dot meta strings ("A · B · C") [T-124].
- **No build talk in the product:** never internal codes, ports, file names, "staging" or service names in user-facing text [T-030, A-004].
- **Do not wrap a feature in AI voice.** Make the feature self-explanatory and cut the decorative explanation [T-007]. Show intelligence through a good next action, not an AI button or badge everywhere [R-129].
- Calm, specific copy after a poor result, with one next step. Never celebrate a bad outcome [R-081, R-127].

## 8. Motion
- **Every animation answers an action or shows a state.** At most one authored page-load moment. Do not stack identical fade-ups on every section or loop animations on every card [T-024, T-112, T-114].
- Durations by role [R-153]:
  - about 100ms for a press;
  - 150-220ms for a small state change;
  - 220-350ms for a result;
  - up to 500ms for an optional milestone.

  Never delay a usable control behind an animation.
- Use custom ease-out curves for entering and exiting, never ease-in on UI. Never `transition: all`, and never animate in from scale(0) (start at 0.95 with opacity 0) [T-103, T-105, A-006].
- Under reduced motion, replace movement with an instant change or a short fade, and keep the same information in text [R-155, R-058].
- Animation must never mask a slow or failing flow [R§ anti-patterns]. Heavy effects (blur, 3D, large assets) must earn their cost on low-end devices and slow networks [R-047, R-202].

## 9. Accessibility and performance (not optional)
- WCAG 2.2 AA throughout [R-201]:
  - every control reachable by keyboard, with visible focus;
  - every control named for screen readers;
  - correct headings;
  - AA contrast at the final size;
  - errors that do not rely on colour;
  - reduced motion respected.
- Required information and actions never depend on hover, colour, motion, haptics or sound alone [R-092].
- Touch targets: 44px is the product choice; 24px is the WCAG floor [R-100].
- Speed is part of the design:
  - aim for first content in about 1 s and data in about 1.5 s;
  - no layout shift (reserve space for content that arrives late);
  - no console errors [T-136, R-203].
- Field thresholds are LCP ≤ 2.5 s, INP ≤ 200 ms and CLS ≤ 0.1. Lab numbers are a diagnosis, not proof [R-101, R-203].

## 10. The AI-slop list: never ship these
Ordered by how often they appear across the owner's reviews, the research and the skills [A-, anti_patterns].
1. Floating UI, bars or hero visuals covering text, figures or controls.
2. Decorative gradients: washes, gradient text, rainbow or "AI purple" gradients.
3. Identical rounded cards, pills or tiles at the same weight; the same action trio on every row; a card that reads like a spreadsheet.
4. Internal jargon or build talk in UI copy.
5. Missing or dead empty, loading and error states; walls of "unknown".
6. `transition: all`, ease-in on UI, scale(0) entrances, slow UI motion, infinite loops on components.
7. Pure black, or blue- or indigo-tinted near-black, standing in for a designed dark theme.
8. Monospace used as a costume for labels and metadata.
9. Glow, neon halos, glass blur on content.
10. AI copy clichés, exclamation-mark successes, hype claims.
11. Arrows or chevrons appended to button text; emoji as icons.
12. ALL-CAPS tracked eyebrows, kickers above headings, numbered section badges.
13. Fake truth:
    - fabricated progress stages or percentages;
    - success shown before acknowledgment;
    - invented testimonials, counts or avatars;
    - false precision;
    - guessed scores shown as meters ("impact 2/5").
14. Hover-only essential controls; icon-only navigation; colour as the only signal.
15. Decoration standing in for structure: confetti or badges without a real outcome, a reward screen covering a weak ending, the generic three-card row, the hero-metric template.
16. A clean-but-generic app with no point of view, shipped on the assumption that clean is enough.
17. An invisible overlay (a transparent full-screen layer, a stuck modal backdrop, a mis-scoped `pointer-events`) that swallows clicks while screenshots look perfect. This shipped to the owner's live Continuum app on 12 Oct 2026, and every text, keyboard and screenshot check passed [P].

## 11. Before you call it done
- **Click it for real.** Click the primary controls and the navigation with a real pointer (or CDP mouse events), not `element.click()`, the keyboard or a screenshot. Hit-test the page so that nothing invisible covers it (`document.elementFromPoint` returns page content). Text, keyboard and screenshot checks all passed while an invisible layer blocked every click in the owner's live app [P, 12 Oct 2026].
- **Exercise the rendered journey in a real browser or device,** not just the code:
  - a small phone and the relevant desktop sizes (for the owner's desktop tools, 1366x650 and 1920x1080);
  - both themes if they are affected;
  - long real labels and real focus movement;
  - the primary and recovery actions;
  - reduced motion.

  Take screenshots and look at them [R-095, T-017].
- Inspect the computed layout, not just the JSX. For stateful work, test interrupting and returning [R§11.4, R-097].
- **Run the slop list in section 10 against the screen** and confirm none is present before reporting [T-001].
- Score it against the review rubric [R§12]: product fit, action clarity, data truth, continuity, agency, visual craft, feedback, emotional fit, accessibility, performance and return value. **A high visual score never cancels a correctness failure.**
- **Report precisely:** a fixture shows behaviour on supplied data, a screenshot shows a composition, and a build shows it builds. None of them alone proves real-device performance [R-096]. Say what you actually exercised.
- When the owner already sees a UI, show screenshots or a side preview and get their OK before replacing it. When they say a section is good, change only what they asked for [T-016, T-025].

## 12. Project addenda
- **MockMob** (CUET UG 2027 Commerce, Score Recovery):
  - Product and experience authority: the live MockMob docs/brain/PRODUCT-EXPERIENCE-RESEARCH-2026-10-12.md (brain mirror: raw/mockmob-brain/), sections 2-12. That covers the recap and return flow, recommendation card contracts, learning-proof rules and the gamification boundaries: no punitive streaks, no variable-ratio paid rewards, no global leaderboard most users cannot win, no fullscreen reward per question, and no correctness shown during an exam-equivalent mock.
  - MockMob's live design system (Night Arena tokens, its three-role type system) overrides the generic choices on this page [R-300].
  - Owner-confirmed price: Rs 99 a month (decisions/log.md, 12 Oct 2026).
- **Continuum** (the owner's local OS):
  - Desktop-first at 1366-1920px; phones only need to not break.
  - Manrope; neutral charcoal; one lilac accent. The owner chose lilac deliberately, which overrides the skills' "no purple" rule.
  - A live brain globe or orb as the hero: it keeps orbiting, sits high, and never covers text. Its glow is the one permitted glow.
  - A movable assistant ball with a dock card, a floating window and confirm cards ("or say yes").
  - A segmented Claude Code / Codex switch that re-themes the scene.
  - A 12-hour clock.
  - Sources: audits/v6/DESIGN-FINAL.md and audits/v6/REFERENCE-INVENTORY.md [T-013, T-014, T-021, T-023, T-026, T-027, T-031, T-035 to T-053].
- **CampusOS and new projects:** no addendum yet. Use this page, and write the project's own system (type, colour, components, states) before building flows [R-053, R-273].

## 13. Evidence-qualified rules from the owner's research (16 Oct 2026, MockMob first)
The owner compiled the **Premium UX/UI research brain, edition 01**: [premium-ux-research-2026-10](premium-ux-research-2026-10.md). The files are in `AI OS/research/Premium_UX_UI_Research_Brain/` and, for agents, in `mockmob-next/docs/research/premium-ux-ui-2026-10/`. Read its `AGENT_RULES.md` and the paper for the screen you are building. **Where it disagrees with an older rule on this page, the research wins** (it is newer and was written for MockMob), unless the owner's own chat instruction or the project system says otherwise.

- **Evidence discipline.** Tag reasoning by source: T (timestamped transcript), V (real frame), S (supporting source), I (interpretation). Cite IDs such as T003 or S014 in design notes. A creator's A/B "winners" and behavioural numbers are claims, never facts to reuse [RB-AGENT 1-6].
- **The next best move carries its evidence.** It names the supporting history, the confidence and the subject or problem. With sparse data it says so and offers a baseline mock instead of a made-up plan [RB-overlay].
- **Value before the account wall,** with guest work carried into the account (T003, T004). Specific CTAs ("Start 10 Accountancy questions"). Defaults only from real context, visible and editable (T001). Progress only for completed steps (T002).
- **Honest money.**
  - Real ₹ a month, renewal, included usage, credit expiry and total.
  - Never set monthly against one-time amounts as if they were the same.
  - No fake reference prices, countdowns or urgency, and no loss threats (T005, T006, T009).
  - Trials only with a real timeline and cancel path (T007).
- **Exams:** no upsells inside a paper; protect the timer, answer persistence, reconnection and submitted-state clarity; no heavy scroll effects or constant animation in a timed paper.
- **AI:** explain uncertainty and the credit cost before any irreversible model call. Say "personalised" only where the logic truly is.
- **Glass, gradients and grids** are slop when chosen by default and repeated without reason. They are allowed only where the design brief requires them (for MockMob, the app's glass dock). A minimal page with no hierarchy or task logic is also slop.
- **Done check additions** (section 11 still applies):
  - **The 12-part anti-slop acceptance test:**
    1. identity with the logo hidden;
    2. one primary action;
    3. true content;
    4. hierarchy at first scan;
    5. intentional composition;
    6. typography by role;
    7. every state;
    8. accessible interaction;
    9. no pseudo-evidence;
    10. motion with a reason;
    11. one leading metric plus one guardrail;
    12. "what would be better without this?".
  - **The 0/1/2 rubric** over 12 dimensions: task fit, information architecture, content truth, readable hierarchy, visual specificity, accessibility, functional states, trust, intentional motion, performance, responsive integrity and instrumentation. It is an internal checklist, not proof of quality, and the owner signs off before a launch.
  - **A DESIGN_DECISIONS note per feature:**
    - the user task;
    - the alternatives and the reason;
    - the evidence IDs;
    - the trade-offs and open assumptions;
    - before and after screenshots;
    - the verification.

## Sources (legend)
- **[O1]** owner request, 12 Oct 2026: raw/mockmob-brain/research-sources/2026-10-12-product-experience/user-request-and-notes.md.
- **[O2]** owner, 11 Oct 2026, "AI slop... gradients, the dark weird theme, the typography": audits/v6/DESIGN-BRIEF.md.
- **[R§n] / R-nnn** MockMob product experience research, section n: raw/mockmob-brain/PRODUCT-EXPERIENCE-RESEARCH-2026-10-12.md (rule ids in audits/design/ui-rules-research.json).
- **[V]** design videos transcript (dashboard fundamentals; Undertone case study): raw/mockmob-brain/research-sources/2026-10-12-product-experience/dashboard-undertone-transcript.txt. Video statistics are unverified source claims; do not reuse them in product UI [R-298].
- **T-nnn / A-nnn** owner taste, reviewer findings and skill rules, with evidence: audits/design/ui-rules-taste.json (owner words: audits/v6/OWNER-ASKS.md, DESIGN-BRIEF.md, REFERENCE-INVENTORY.md; reviews: audits/v6/polish/; skills: .claude/skills/).
- **[P]** Continuum UI review passes 0-11: audits/v6/polish/.

[Evidence-safe UX](evidence-safe-ux.md) · [MockMob](../entities/mockmob.md) · [source authority](source-authority.md)
