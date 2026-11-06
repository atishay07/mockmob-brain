# Owner materials: what we were given, what it asks for, and where the app falls short

Date: 13 October 2026. Written after the owner rejected the current Android app's onboarding, copy and navigation ("really basic", "not even close to an onboarding flow of a polished app", "a good navbar wouldn't look like this").

Scope: this is a reading record and a gap analysis. It does not change code and does not authorise anything by itself. The owner's message of 13 October 2026 is the newest authority. Where it conflicts with an older document, section 4 says which way to resolve it and what still needs his confirmation.

## What was read

| Key | Material | How it was read |
| --- | --- | --- |
| O13 | Owner message, 13 Oct 2026 (relayed verbatim by the workflow harness) | In full |
| R | `mockmob copy/docs/brain/PRODUCT-EXPERIENCE-RESEARCH-2026-10-12.md` | Sections 1-16 (L1-707) in full. Appendices A-D (L709-5663) reproduce the source files below byte for byte, so they were read through those files. A script confirmed that every PDF text line from page 26 onward appears in product-brain.md. |
| PB | `research-sources/2026-10-12-product-experience/product-brain.md` (incl. Tim transcript L001-L201, cited PB-T) | In full, L1-1412 |
| V | `research-sources/.../dashboard-undertone-transcript.txt` (cited by file line, = C001-C164) | In full, L1-164 |
| N | `research-sources/.../user-request-and-notes.md` | In full, L1-109 |
| PDF | `research-sources/.../ux-specification-extracted.txt` (59 pages) + figure-15..20.png (PDF pp. 15-20) | Pages 1-25 read directly, the rest checked against PB by script; all six figures viewed |
| UXS | `AI OS/wiki/concepts/ui-ux-standards.md` | In full, L1-207 |
| IMP | `~/.claude/skills/impeccable/SKILL.md` + reference/onboard, delight, overdrive, animate, android, craft-floor, bolder, typeset, colorize | All in full |
| SPEC | `mockmob-next/docs/brain/APP-DESIGN-SPEC.md` | In full, L1-780 |
| DES | `mockmob-next/DESIGN.md` | In full, L1-622 |
| C1 | Continuum `raw/conversations/claude/37905d9d3e69-1.md` L280-560 (CampusOS deep-redesign brief, owner-written, 13 Jul 2026) | Read |
| C2 | Continuum `raw/conversations/codex/b5fbc02f2762-1.md` L440-700 (same brief as sent to Codex) | Read |
| C3 | Continuum `raw/conversations/codex/b5fbc02f2762-2.md` L3200-3460 (owner's refinement brief: dock stability, glass and colour) | Read |
| C4 | Continuum `raw/conversations/codex/76f6fd2cc78e-1.md` L60-350 (owner's earlier CampusOS brief: "Everything moves") | Read (found by searching for "liquid glass") |
| C5 | Continuum `raw/claude-memory-C--Users-atish-Desktop-CampusOS/marquee-design-system.md` (what the CampusOS interview concluded) | In full |
| OW | Continuum `raw/conversations/claude/01163b7e429f-1.md` L20-29: dated owner quotes taken from `AI OS/audits/v6/owner-words` | Design-taste rows extracted by script (the stored dump is truncated at about 199 of 362 rows) |
| LF | Continuum `raw/claude-memory-c--Users-atish-Desktop-mockmob-copy-mockmob-copy/mockmob-landing-feedback-oct-2026.md` | In full |
| Shots | `mockmob-next/tmp/app-shots/m06/*-s.png` (40 files, Galaxy M06) | Every file opened |

Searches run: continuum_search for "high.live", "liquid glass", "Revolut", "Fampay", "onboarding" and two follow-ups (owner design feedback; Mobi and glass decisions). The search for **Fampay** returns only the 13 October message, so there is no earlier Fampay direction. **high.live** appears only in CampusOS sessions (13 Jul 2026), where the owner said "take inspiration from high.live website… use gpt image generator". That site is canvas-rendered and its HTML exposes nothing (codex 70082c8c00c6-1 L1030-1061). **No live inspection of high.live, Fampay or Revolut was done in this pass.** A dedicated reference study is still owed (see the summary).

---

## 1. Every concrete recommendation in the owner's materials

Legend: "R L304" means research doc line 304, "PB L340" means product-brain line 340, "PB-T L047" means Tim transcript line L047 inside PB, and "V L109" means the Undertone file line 109. Items marked (claim) are video assertions, kept as they were supplied and not verified.

### 1.1 Onboarding and first run

| # | Recommendation | Source |
| --- | --- | --- |
| 1 | Onboarding's job is to reach the moment that proves the product is worth the time, not to teach the product. | IMP onboard L3, L26 |
| 2 | Value before commitment: give a short, useful guest experience before an account, a long questionnaire or payment. | PB L80; R L94 |
| 3 | Never throw away completed guest work. Merge it once, idempotently, when the account is created. | PB L82, L246 |
| 4 | Ask for the subject (and the goal) only when the answer changes what the student gets, and explain why you are asking. | PB L56, L243; IMP onboard L71-74 |
| 5 | Undertone lesson: high completion of a long onboarding measured how badly users needed the app, not how good the onboarding was. Watch whether people reach the first trustworthy outcome. | V L65-73; R L262, L270 |
| 6 | Move the core action into onboarding, where motivation is highest ("test your mic while you're still inside the flow"). | V L108-111 |
| 7 | Replace the dead end with a real result: "you get shown a real recap before you've even gotten into the app". | V L112-114 |
| 8 | By the time the user lands, two questions are answered: "does this work and what will it give me". | V L114 |
| 9 | A five-question demo that ends in a signup wall without explanation is the MockMob version of Undertone's microphone dead end. | R L272 |
| 10 | Show the real form of a result and the next step before demanding a full mock. Keep sample data labelled as sample performance. | R L274 |
| 11 | Revolut: "They don't just drop you into a boring signup flow… rich visuals, super smooth transitions… stepping into something premium." | PB-T L047-L048 |
| 12 | "Nail the first impression. Spend time to polish your onboarding, polish your welcome moments." | PB-T L053-L054 |
| 13 | Visceral layer: the first contact must look credible. The failure to avoid is a premium-looking shell with vague claims. | PB L158-164 |
| 14 | Show, don't tell. Use real functionality, not a separate tutorial mode, and teach one thing at a time. | IMP onboard L32-35, L218 |
| 15 | Give a skip path, an honest time estimate and progress ("step 1 of 3"). | IMP onboard L37-40, L64-68, L80 |
| 16 | Introduce one to three core concepts, interactively. | IMP onboard L76-80 |
| 17 | First success: guide the student to accomplish something real, celebrate it without overdoing it, and give clear next steps. | IMP onboard L82-86 |
| 18 | "Respect user intelligence. Don't patronize or over-explain." Never show "obvious explanations". | IMP onboard L53-56, L215 |
| 19 | Empty states are onboarding: say what will appear, why it matters and how to start, with visual interest (illustration, not bare text). | IMP onboard L50, L168-185 |
| 20 | Ask for notification permission only after value has been shown. A refusal never blocks study. | PB L396; R L604; SPEC L611 |
| 21 | Positioning to test: "Turn your last mock into your next improvement." It is a hypothesis, not a mandate. | PB L60-62 |
| 22 | First-visit sequence: landing, then subject, then a short practice, then answers with an explanation, then save, then a short next action. If a full mock is chosen first, allow it. | PB L240-249 |
| 23 | Speak-style lesson: pick efficacy over the tap-through game; question whether students need "more questions, more choices". | PB L102-104; PB-T L073-L074 |
| 24 | Owner's working rule for CampusOS onboarding, a parallel case: a branded cold open, then identity-building screens, with onboarding identity objects as the place for the strongest glass. | C5; C3 L3300-3460 |

### 1.2 Emotion during a task, after it, and on return

| # | Recommendation | Source |
| --- | --- | --- |
| 25 | The emotional job is calm agency: "I can see what happened, understand the next step, and trust that my work is preserved." | R L80; PB L46 |
| 26 | Design each transition. Before: uncertainty. During: concentration. After a poor result: alert to judgement. Repair: small enough to begin. Check: honest evidence. Return: remembered context. | R L110-112; PB L228 |
| 27 | After a poor mock, lead with "Here's the first thing to work on", not a red wall of weaknesses. | PB L230; R L112 |
| 28 | During a timed mock: concentration and control. No correctness, no mascot, near-zero motion, visible save state. | PB L259-261; SPEC L82, L398 |
| 29 | "Correct answers get concise feedback; mistakes get a specific explanation and a next step." | PB L86, L344-346 |
| 30 | Duolingo: answer feedback should make you "feel encouraged, corrected, and even cheered on" (claim). | PB-T L018 |
| 31 | A completed useful session gets an earned ending. No reward interaction between exam questions. | PB L172 |
| 32 | Every ending is designed. A score with no next step is a bug. | SPEC L73; R L314 |
| 33 | Give permission to stop: "Finish for now" as a real ending. | PB L130, L386; R L479 |
| 34 | Return after a gap: "Welcome back. Choose the time you have." No guilt countdown, no erased progress. | R L436; PB L350, L364; SPEC L589-591 |
| 35 | Cadence follows school and coaching, not a daily-open target. Study natural returns before adding reminders. | R L278-280 |
| 36 | Mobi responds to known context only. It never pretends to know feelings and never threatens. | R L332; PB L371 |
| 37 | "Performance is emotional design." Load key text and actions before optional animation, and keep timers stable. | PB L770-772 |
| 38 | Phantom: in an intimidating category, friendly visuals and warm, playful details make heavy topics lighter. | PB-T L031, L040; PB L178 |
| 39 | Warmth must not blur facts. "A calm failure message with saved work matters more than a mascot smiling during a lost attempt." | PB L178, L230 |
| 40 | Undertone's founder called the old app "very utilitarian… not much in the way of flair or panache". That was the diagnosis, and it matches the owner's 13 Oct complaint. | V L67 |

### 1.3 Recap reveal (the Undertone moment)

| # | Recommendation | Source |
| --- | --- | --- |
| 41 | Find the moment where users already come back on their own (Undertone: median about 10 minutes after the session, which is a claim). For MockMob that is opening the result after a mock. | V L89-93; R L419; SPEC L84 |
| 42 | "The best moment in the product was also the weakest screen in it": a block of text and a "see full recap" button. | V L94-95 |
| 43 | Brand and design system come first, so every fix feels like the same product. | V L97-106; R L284-286 |
| 44 | Seven interventions: (1) hold the thread while the user leaves, (2) notify when ready, (3) a surface worth opening with a subtle bounce, (4) the user performs the reveal, (5) payoff on two senses (confetti and a haptic), (6) frame what they got, (7) put the next ask inside the peak. | V L138-146; R L298-306 |
| 45 | The reveal is something the user performs, "like opening a gift", without being tacky. | V L140-142 |
| 46 | Peak-end rule: "You remember an experience by its biggest moment and by how it ends." Apple packaging was the reference. | V L132-136; R L312 |
| 47 | The brief had two edges, "Nothing clinical… Nothing cute". The ending must fit the person. | V L152-154 |
| 48 | Distinctive endings come from the product's own metaphor. Undertone used a record sleeve; MockMob's spec already has the folded answer sheet. | R L318-320; SPEC L13 |
| 49 | Show processing stages only when real state backs them. No invented "AI verified" stage. | R L292; UXS L101 |
| 50 | Decay the ritual and offer skip paths. The reveal is charming once and a burden on the twentieth time, so give direct access, skip and reduced-motion paths. | R L308, L611; SPEC L438-441 |
| 51 | The poor-result variant behaves differently: no confetti after a distressing result. | R L308; SPEC L467 |
| 52 | Card sequence for MockMob: the marks with the answer sheet, where the marks went, the first thing to fix, then what was recorded plus the next ask. | SPEC L451-456 |
| 53 | "UX, UI and branding are table stakes… What none of that gives you is connection, a personality, a thought-through, custom-made experience." | V L156-160 |
| 54 | "The small touches that we didn't expect… this feels cohesive, this has life, this has a personality." | V L161-162 |

### 1.4 Celebrations

| # | Recommendation | Source |
| --- | --- | --- |
| 55 | "Celebrate the small wins… they should feel intentional." (Duolingo) | PB-T L021-L022 |
| 56 | Micro-interactions for repeated behaviour: "A subtle bounce, a glow, a sparkle." | PB-T L020 |
| 57 | Match the response to effort and consequence: milestones can expand, routine saves should simply feel certain. | IMP delight L39 |
| 58 | Celebrate specifically ("7 of 10 fresh, earlier 4 of 10"), never "you are now stronger". | PB L138, L283, L365; R L438 |
| 59 | No fullscreen reward per question. | PB L345 |
| 60 | Never manufacture a celebration for an ordinary click. | IMP delight L23 |
| 61 | A celebration must be specific enough that a neighbouring product could not use it unchanged. | IMP delight L63 |
| 62 | Delight must never be "mandatory, unskippable, or exhausting on repeat". | IMP delight L50-57 |
| 63 | Variable presentation is allowed for occasional, non-essential acknowledgment. Never randomise access, scores or explanations. | R L385-387; PB L208 |

### 1.5 Streaks and gamification balance

| # | Recommendation | Source |
| --- | --- | --- |
| 64 | Use fewer mechanics well, and justify each one's attention cost (the S-curve claim, Habitica). | R L371-373; PB L118-122 |
| 65 | PBL fallacy: "PBL is the scoreboard of a game, not the game itself." Badges must certify real work. | PB-T L094; R L359-361 |
| 66 | Streak trap: streaks drift from "I want to" to "I can't miss today". Wrap them in agency (chosen goal, pause, rest). | PB-T L113-L120; R L377-379 |
| 67 | Default to a chosen weekly goal with rest days and a friendly restart. Nothing earned is lost. | PB L390-392; SPEC L541-552 |
| 68 | Completion drive (rings) works when the denominator is real work: "2 of 3 repair cycles", not "80 XP to unlock a chest". | PB L130; R L391 |
| 69 | Competence feedback beats recognition: "Build mechanics that signal you got better at the actual thing." | PB-T L141; R L393 |
| 70 | Strava lesson: winnable local competition. Optional comparable cohorts, personal bests by default, no global leaderboard. | PB-T L099-L105; R L365-367 |
| 71 | No craving machine, no infinite game, no forced scoreboard. "The goal is willing, useful return, not making an exam student unable to stop." | PB L218-224; R L399-405 |
| 72 | Community needs a purpose, norms and moderation. "A dormant chat tab is a feature, not a community." | PB L142-144; R L409 |
| 73 | Shareable output shows real completed work, is private by default and never exposes marks. | PB L428; R L446; SPEC L496 |

### 1.6 Motion

| # | Recommendation | Source |
| --- | --- | --- |
| 74 | Every interaction needs a response: four button states plus focus, input states and micro-interactions (the chip that slides up after "copy"). | V L49-54; R L230-242 |
| 75 | Motion communicates a state change. Budgets: press about 100 ms, state 150-220 ms, result 220-350 ms, milestone up to 500 ms. | PB L340; UXS L116-120 |
| 76 | "Polish builds trust. Treat visual details, motion, and transitions as core product features, not fluff." | PB-T L038-L039 |
| 77 | "What really sticks is how the product feels when someone taps, swipes, or waits." | PB-T L042 |
| 78 | Revolut: tactile charts ("drag your finger and the graph responds with a soft glow") and a 3D card that "flips, rotates, catches light". | PB-T L049-L051 |
| 79 | Use tactile interaction where it helps: inspect a point on score history, reveal evidence, move smoothly from result to repair. No 3D for its own sake. | PB L184 |
| 80 | One motion thesis with one focal moment drawn from the product, not "a generic fade-and-rise". | IMP animate L25-34; craft-floor L13 |
| 81 | Choose motion material by meaning: shared-element and FLIP for continuity, blur and backdrop for depth, masks for reveals. | IMP animate L36-46 |
| 82 | Exit faster than entrance, use natural deceleration `cubic-bezier(0.16, 1, 0.3, 1)`, and no reflexive bounce. | IMP animate L61 |
| 83 | Android: Material motion patterns (container transform, shared axis, fade through), predictive back, and honour Remove animations. | IMP android L15, L40 |
| 84 | Blur, layered shadows, 3D and large assets must earn their cost on budget Android. | R L248; UXS L125 |
| 85 | Owner, CampusOS: "Motion is not optional", using springs, shared elements, gestures, scroll-linked effects, parallax, staggered reveals, animated numbers, custom loading and empty states, and "subtle 3D or perspective". | C1 L283-517 (Motion section); C2 L570-600 |
| 86 | "Do not use the same fade-up animation everywhere. Animations should explain origin, hierarchy, state, and consequence." | C1; C2 L586-590 |
| 87 | "Everything moves. Nothing pops. Everything glides. Every interaction has weight." | C4 L60-350 (Motion Language) |
| 88 | Demos visibly animate when looked at, not once on first scroll ("no animation visible" was rejected). | LF |
| 89 | Reduced motion keeps the same information in text. | PB L352; R L556; UXS L124 |

### 1.7 Haptics

| # | Recommendation | Source |
| --- | --- | --- |
| 90 | Payoff on two sensory channels, visual plus a subtle haptic ("half a kit" in the transcript, likely "haptic"). | V L143; R L304, L664 |
| 91 | Owner, CampusOS: haptics on navigation, card presses, saves, confirmations, errors and state changes, "different haptic strengths based on the importance of the action". | C1; C2 L592-594; C5 ("graded CampusHaptics") |
| 92 | Never rely on haptics alone; respect the system setting and an in-app switch. | PB L352; SPEC L203 |
| 93 | Spec vocabulary: tick (tab, option, recap drag thresholds), settle (key commit), open (sheet opened, submission acknowledged), warn. None on wrong answers. | SPEC L202-212 |

### 1.8 Copy

| # | Recommendation | Source |
| --- | --- | --- |
| 94 | Use concrete verbs and evidence: "Try 8 fresh questions on inference" beats "Unlock your academic superpowers". | PB L356; UXS L106 |
| 95 | Copy table: first diagnosis, supported pattern, sparse content, return, verification success, ambiguous result, temporary error. | PB L358-367 |
| 96 | Keep a small shared vocabulary: mock, repair, fresh check, progress, goal. | PB L446 |
| 97 | Do not wrap a feature in AI voice; make the feature self-explanatory. Show intelligence through a good next action. | UXS L111; PB L196 |
| 98 | No build talk in the product: no routes, codes or service names. | UXS L110, L148 |
| 99 | No AI clichés, no exclamation-mark successes, no middle-dot strings. | UXS L107-109 |
| 100 | Copy must use the product's language. "Generic whimsy is worse than neutral clarity." | IMP delight L46 |
| 101 | Owner, 13 Oct: obvious disclaimers "don't need to be written. Important stuff, exciting copy, captions, and many things can be written." | O13 |
| 102 | Owner, 4 Oct: "improvise the English copies what you have written". | OW (2026-10-04) |
| 103 | Brand voice should be understandable, accurate, encouraging and recognisably MockMob across every touchpoint. | PB L446 |

### 1.9 Navigation and information architecture

| # | Recommendation | Source |
| --- | --- | --- |
| 104 | Test three task destinations (Practice / Improve / My Goal) against the current five. Use labelled tabs and "avoid icon-only navigation". | PB L234-238; R L442 |
| 105 | Home priority: an unfinished session, then the next best move, then due checks, the weekly goal, then optional practice. The hero fits the first viewport. | PB L253-255; PDF p15 (figure-15) |
| 106 | One useful default plus "Choose your own practice"; feature names should not all demand equal home-screen attention. | PB L66, L98; figure-15 |
| 107 | Progressive disclosure: frequent actions visible, rare ones behind a labelled popover or "More", never hidden for good. | V L12-14; R L178-182; UXS L66 |
| 108 | Android: a navigation bar with 3-5 destinations, system Back always works, edge-to-edge insets, 48 dp targets. | IMP android L13-20 |
| 109 | Owner, CampusOS: criticised a "visually dominant bottom navigation"; the target is a "compact and refined" navigation, a "compact floating glass dock, channel-lit per active tab, hides on scroll-down". | C1 (References and Definition of done); C5 |
| 110 | Dock stability: constant outer dimensions, no overflow during tab animation, safe areas, text scaling, and resilience to rapid switching. | C3 L3264-3300 |
| 111 | Floating UI must never cover text or controls; pad scroll areas for fixed bars. | UXS L64, L145 |

### 1.10 Premium feel, brand and visual craft

| # | Recommendation | Source |
| --- | --- | --- |
| 112 | "Just being useful isn't enough anymore. The real edge is in how your product makes people feel… smooth, delightful, playful, or even premium?" | PB-T L004-L005; N L66 |
| 113 | Revolut: premium comes from many quiet details: "None of these design details shout at you, but together they create something way more premium." | PB-T L052 |
| 114 | "Clean alone is table stakes and is not the goal… a product that feels intentional, alive and built around its own central idea." | UXS L25 |
| 115 | Slop item 16: "A clean-but-generic app with no point of view, shipped on the assumption that clean is enough." | UXS L165 |
| 116 | Let data decide the form; hierarchy from size, position and contrast; "an image always adds a great pop of color and makes scanning super easy". | V L5-9, L18-19 |
| 117 | Image overlays: a gradient scrim, with "progressive blur on top of the gradient for an even more modern look". | V L55-57; R L246 |
| 118 | Typography: tighten large headings by -2% to -3% with 110-120% line height. Use few sizes. | V L31-34; UXS L70-71 |
| 119 | Dark mode: depth from lighter raised layers, softer borders, desaturated chips. | V L40-44; R L218 |
| 120 | "Raised tactile buttons" from inner and outer shadows. This is the existing keycap signature. | V L44; DES L374; SPEC L151-159 |
| 121 | Delight thesis: one sentence saying what the user should feel and why it belongs to this product, then the smallest system that delivers it. | IMP delight L25-35 |
| 122 | Overdrive: what makes a user of this interface say "wow"? For functional UI, the wow is in how it feels (morphing dialogs, spring physics), and effects must not jank on mid-range devices. | IMP overdrive L10, L28-44, L113-118 |
| 123 | Bolder: commit fully to one decisive move and quiet everything around it. "If every element got louder, the section got flatter." | IMP bolder L15-18 |
| 124 | Colour: let the strongest colour own a deliberate region instead of scattering tiny accents. | IMP colorize L42-43 |
| 125 | Craft floor: no eyebrows, no same-size icon cards, no glass as decoration, and "when torn between refined and committed, commit". | IMP craft-floor L24-42 |
| 126 | Owner, CampusOS: "dark, cinematic, youthful, intelligent, tactile, socially alive, editorial, expressive"; "authored rather than assembled". | C1; C2 |
| 127 | Owner, CampusOS: selective physical glass ("not like a transparent rounded rectangle placed over a blurred background"), with "different glass behaviours" for navigation, controls, sheets, overlays, status and interactive cards; readable contrast; smooth on a normal Android device. | C1; C2 L541-566 |
| 128 | "Glass should remain selective… Content-heavy areas should usually retain stable dark or tonal surfaces for readability." Soften harsh flat colour with translucent layers, edge highlights and "restrained colour bloom". | C3 L3330-3460 |
| 129 | Use generated imagery, illustrations, custom icons and posters. When an asset is missing, build the rich layout with a deliberate placeholder; "Do not replace rich layouts with empty text cards." | C1; C2 (Visual composition); C4 L60-80 |
| 130 | Owner, 13 Oct: generate SVGs, use ChatGPT/Codex image generation, and ask for video if animations need it. A full brand redesign is on the table. Vibe references: high.live and its app, Revolut, Fampay. | O13 |

---

## 2. The owner's taste profile, in his own words

**What he is rejecting now (MockMob, 13 Oct):** "really basic right now"; "not even close to an onboarding flow of a polished app"; "a good navbar wouldn't look like this"; "not interactive at all"; "weird bottom taglines… obvious and don't need to be written"; "rudimentary".

**What he is asking for (MockMob, 13 Oct):** "be more thoughtful and have taste in your design direction"; "nothing but perfection"; "a really fancy UI: something premium, something which inspires people to use the app"; "exciting copy, captions"; glassmorphism; references high.live ("It's so good… it is just crazy"), Revolut and Fampay ("appeals to a similar kind of generation"); "redesign the entire brand".

**Recurring across projects (OW, dated):**
- "it looks very AI everywhere and doesn't give that this is an actual worth it feature feel" (3 Oct, MockMob).
- "they have to be placed very thoughtfully" (3 Oct, on animation and mascot placement).
- "use image gen… and apple glass morphism… along with the frontend skills extensively" (3 Oct).
- "It has lost the original touch" (1 Oct). "the app is a very basic app. The UI/UX is very basic" (12 Jul, CampusOS). These are the same words he used on 13 Oct.
- "make the current state at least ten times better" (9 Oct). "It should have that addictive feel that a good product has. The UI should feel premium… It should have taste" (10 Oct).
- "has a really nice UI, which makes it really fun to use. It is also useful" (9 Oct). Fun and useful go together for him.

**The other edge of his taste (he also punishes excess):**
- "too many cards, pills, chips, labels, borders, glows, gradients… Reduce rather than decorate. Use fewer, stronger ideas" (16 Jul).
- "Maybe you have overdone the lighting" (8 Oct).
- "filled with more useless things" (LF, 5 Oct, landing).
- "Glass should remain selective. Do not convert every card or background into frosted glass" (C3).
- CampusOS criticised "large empty spaces, oversized rounded cards, pill controls… repeated title-and-panel layouts, sparse content… visually dominant bottom navigation" (C1). That sentence describes the current MockMob app almost exactly.

**His CampusOS vocabulary (C1/C2/C4/C5):** "authored rather than assembled"; "premium cultural operating system"; "dark, cinematic, youthful… tactile… editorial, expressive"; "This looks expensive"; "Typography should carry the interface. Not boxes."; "Everything moves. Nothing pops. Everything glides."; "Never use flat colors… Subtle animated lighting… Noise. Depth."; "Glass should feel physical and interactive"; "navigation is compact and refined"; HIGH used for "emotion, lighting, branding, motion, premium feeling", not for layout (C4). The CampusOS interview settled on "HIGH-led/tempered, functional color family, selective physical glass, condensed editorial type, floating dock, cinematic-moment motion, medium density, procedural imagery… branded cold-open, adaptive quality" (C5).

**Durable working rules:** he reads placement and deletions literally and wants features kept, not cut (LF); motion must be visibly working when inspected (LF); real numbers only, so social proof must be real, dated and sourced (Atishay entity page); he wants design references to be used ("use taste and 1000+ design references", OW 1 Oct).

**Taste in one line:** dark, cinematic, editorial and tactile, with selective physical glass, purposeful and graded motion and haptics, generated imagery and big confident type. Premium means "looks expensive" and fun to use. It must never be cluttered, generic, decorated for its own sake or over-lit.

---

## 3. Screen-by-screen gap analysis (Galaxy M06 screenshots)

Common to every screen: a flat paper or charcoal ground with no depth, light or imagery. Every element is the same rounded white keycap or row. There is no brand moment, no visible motion or haptic story, and large dead voids. This is the "clean is enough" failure (UXS L165) and the "very utilitarian… not much flair or panache" diagnosis (V L67).

| Shot | What is on screen | Gap against the owner and the research |
| --- | --- | --- |
| 01-launch (Welcome) | A small Mobi sticker top left; "Find the marks you're losing. Repair the mistake."; "Start with five CUET-style questions. No account needed."; five empty squares with "Your answer sheet fills in as you go."; about 200 px of empty paper; volt "Try 5 questions"; "I already have an account"; footer **"MockMob is not affiliated with NTA or Delhi University."** | No cold open or "stepping into something premium" moment (items 11-12). The defensive footer is exactly what the owner named. "Try 5 questions" anchors the non-scalable sample. Mobi is a static sticker, not a guide. There is no reason to believe (no product preview or recap preview) and the void sits mid-screen. |
| 02-subject | "Back" text link; "Which paper first?"; four identical white keycap rows; "Other subjects" as bare bold text; three grey paragraphs: "We use this to set up your first mock. You can change this later in You.", "The five sample questions are the same for every paper.", **"Five original sample questions. No signup. Not an official PYQ or a scored diagnostic."** | A generic list with no subject identity (icon, colour or art). The copy admits the subject choice changes nothing for the sample ("the same for every paper"), so the question has no point (item 4). Repeated disclaimer, and half the screen is empty. |
| 03/05/07/08/09 (Q1-Q5) | Back plus an **"On this phone"** pill; "Question n of 5" with pips; caption **"Sample questions. This is not a diagnosis."** above every question; four identical options; a 250 px void; footer disclaimer repeated on all five screens | Disclaimers appear twice per screen, five times over (O13; IMP onboard L215). "On this phone" is system state shown to a guest who has no account yet, so it is build talk in effect. There is no momentum: the sheet does not visibly fill and there is no streak of right answers or mascot reaction before the choice. The voids are dead. |
| 04 / 10 (correct) | The chosen key goes ink with a check; a panel with a 40 dp Mobi, "Correct" and a one-line reason; "Next question" | The success moment is a flat grey box. There is no felt payoff on two channels (item 90) and no animated sheet cell. Mobi is a thumbnail. It does not yet "feel encouraged… cheered on" (item 30). |
| 06 (wrong) | Red-bordered option; pink panel "Not quite", "The answer is B, ₹50,000." with the working | Functionally right and kind in tone. Visually it is the loudest thing in the flow, louder than any success, so the emotional weighting is inverted. |
| 11/12 (sample result) | Big "4" with "of 5 correct"; a five-cell strip; "This is your answer sheet. After a mock, the same sheet shows every question."; **"Sample, not a diagnosis. Five questions can show how MockMob explains things. They cannot say where you stand."**; a dashed card **"Example, not your plan yet"** explaining what would appear later; "Save this and continue", "Try another subject" | This is the onboarding's peak and it is the weakest screen. It is Undertone's "block of text and a see full recap button" (V L94). No reveal, no celebration, no Mobi, no folded sheet, so the signature recap (SPEC A1) is absent at the moment that matters most. Half the copy explains what the app cannot do, and the "next move" is a dashed empty box (C1: "Do not replace rich layouts with empty text cards"). |
| 13-signin (sheet) | "Create a free account to keep your five answers and start a mock."; "Your five answers are on this phone. Not sent yet."; volt "Continue with Google", "Use an email code", "Not now" | Reasonable mechanics. The second line is system jargon at a persuasive moment. It is the generic bottom sheet over a dimmed screen, with no value framing (no picture of what the account unlocks). |
| 14-16 (email, code) | "Sign in"; "We email you an 8-digit code. No password to remember."; eight code boxes; "Not there? Check your spam folder."; error "Something went wrong on our side. Your email is still here. Try again." | Competent but stock. It uses a back arrow where earlier screens used a "Back" text link (inconsistent chrome). No brand presence. |
| 17 (offline) | Banner "You are offline. Connect to sign in." | Honest and fine. |
| 18-relaunch | A blank page reading **"Splash /splash"** | A raw route placeholder is visible to the user: build talk (UXS L110, slop list 4). There is no splash or cold-open brand moment. |
| 19, 36, 38 (Today) | A blank page reading **"Today /today"** above the tab bar, in light and dark | The most important screen in the app is not built. The user lands on a route label after onboarding, which is a dead end (R L272). Every Today recommendation (item 105, figure-15) is missing. |
| Tab bar (19-41) | A flat full-width bar, raised fill, 1 dp hairline, five Lucide outline icons (house, dumbbell, clipboard, book, person), labels, volt pill behind the active icon | This is what the owner called "a good navbar wouldn't look like this… not interactive". It is the stock Material bar: no glass, not floating, no spring or light response, permanently 72 dp tall, and it covers content (31: the "NTA-style mode" row is cut off; 20: "CUET tools" sits under it; 27: "Late-night lines" is cut). It is the "visually dominant bottom navigation" from C1. The dumbbell is a gym metaphor for study. |
| 20 / 29 (You) | "You"; "Signed in as app-e2e-student@example.com"; rows (Weekly goal and rhythm, Repair record, Milestones, Personal bests, Notifications, Appearance and feel, Privacy "Usage data is off", Account, Help); "CUET tools" header half hidden | A settings list, not an identity. There is no profile card or "pass", no progress shown inline, and settings dominate (C1 asked for the reverse on Profile). Ten identical rows with chevrons. |
| 21-23, 41 (Usage data) | The switch "Allow usage data to improve MockMob"; a long paragraph of what is and is not collected; "See every event we collect"; another paragraph about sessions and Google Play; "Change my answer"; confirmations "Usage data is off. We stopped collecting it. Earlier usage data was deleted." / "Usage data is on. Saved…" | Correct and honest, but a wall of legal text with no visual structure. "Change my answer" has no context (it re-asks the age question). It could be a structured two-column "We count / We never collect" layout. |
| 24-26, 40 (Notifications) | Offline strip "Showing settings from 1:51 AM. Changes need a connection."; card "Notifications are off" with volt "Turn on"; a "Your day" bar with quiet hours; toggles | The 24-hour "Your day" bar is the one genuinely designed idea in the app, but it is flat and inert (it is not draggable). Otherwise this is the generic card-plus-toggles pattern. |
| 27/28 (Appearance) | Theme rows (Match phone, Light "Paper colours.", Dark "Night colours."); toggles for Reduce motion, Touch feedback, Open results directly, Late-night lines (cut off by the tab bar) | Functional. No live preview of the theme and no sense of "feel". The tab bar hides the last row. |
| 30 (Learn) | Sleeping Mobi; **"Learning is not available right now."**; "Practice and Review are still open."; "Open Practice" | One of five tabs is a dead end that says it is unavailable. The IA spends a primary destination on nothing (item 104). |
| 31 (Practice) | Subject chips (Accountancy selected, English, "Other subjects" dropdown); a "Full mock" card with a decorative 50-square grid and "Uses 50 credits. You have 100."; Quick practice and Chapter practice rows, each with mini square grids, chevrons, costs and **"Practice, not proof"**; "NTA-style mode, Part of Pro. You can take a…" cut off | Cost-first copy ("Uses 10 credits") on every row instead of what you will get. A defensive tagline replaces a description. The decorative mini-grids repeat on every row (the same-ornament pattern). The tab bar covers content. Nothing invites the student; this is a catalogue (R L338, figure-15 "one useful default"). |
| 32 (Quick practice setup) | Subject chips; a stepper "- 10 +" with big boxes; a row of ten squares; "10 questions, about 10 minutes"; **"Uses 10 credits. You have 100."**; "Feedback comes after you finish."; "Start practice" | A big empty middle and a stock stepper. Again the cost is the most prominent line. No preview of the session or chapter coverage. |
| 33 (after Start) | A blank page reading **"Runner /run/:sessionId"** | The runner is not built. The primary action of the Practice tab leads to a route label: build talk and a dead end. |
| 34 (after back) | Android home screen | Back from the runner placeholder exited the app. This conflicts with "system Back always works" and with the leave guard (SPEC L276). Worth re-checking on device. |
| 35 | Camera app | A stray capture, not app content. |
| 37 (Account) | Name "app-e2e-student"; email; "Plan: Not on Pro. Pro bought on mockmob.in is honoured here."; "Sign out"; "Delete account" | Plain list. The Pro line is honest, but the plan has no presence. Fine for a settings page, but it reinforces the settings-heavy You tab. |

**Copy inventory to remove or rewrite** (from `flutter_app/lib`): `onboarding/copy.dart` L10 `notAffiliated`, L38 `sampleCaption`, L39 `sampleDisclaimer`, L58 `resultLine`, L60 `exampleLabel`; `you/copy.dart` L180 `helpNonAffiliation` (keep in Help only); `practice/copy.dart` L18 `chapterModeLine` "Practice, not proof" and L144 "This try is not recorded. It is practice, not proof."; `core/copy/state_words.dart` L22/L26 receipts ending "This is practice, not proof."; `rhythm/copy.dart` L136 "Fresh checks are not available yet." appended to a positive weekly ending. Also the router placeholders (`core/router/placeholder_screen.dart`), which show raw routes to users.

**Scorecard against the rubric (R L580-593), summarised:** data truth and continuity are strong (save-state honesty and the offline banners work). Visual craft, emotional fit, feedback and return value are weak to absent. The core loop screens (Today, runner, result and recap, Review) are placeholders, so action clarity cannot be judged.

---

## 4. Conflicts between older documents and the owner's new direction

Precedence is set by the documents themselves: "the owner's current instruction in the chat" comes first (UXS L14-16; SPEC L5). The resolutions below follow that order but keep every integrity rule in section 5.

| # | Older rule | New direction | Recommended resolution | Needs owner OK? |
| --- | --- | --- | --- | --- |
| 1 | **No glass or blur.** SPEC L53 rule 5 ("No decorative gradient, glow, glass or blur"); SPEC L190 and L667 (no `BackdropFilter`); DES L527 ("Don't reach for a translucent or blurred card"); PB L293 ("Avoid a dashboard filled with floating translucent tiles"); craft-floor L33 | Glassmorphism and liquid glass are wanted (O13; C1; C3) | Adopt **selective physical glass**, which is CampusOS's own rule (C3: "Glass should remain selective"). Use glass for floating chrome (dock, collapsing top bar, sheets, overlays, the recap tab, controls over imagery) and keep solid tonal surfaces for questions, explanations and evidence. This also satisfies UXS L82, which already allows blur on fixed chrome. On the M06: one shared backdrop layer, no blur inside scrolling lists, and a full/lite quality switch (C5 `GlassSettings`), profiled on the device. | Direction given; the device budget must be proven |
| 2 | **Five-question sample onboarding.** SPEC 5.1.1-5.1.4 (L287-293), A9 (L38, hardcoded `DemoDrill.jsx` questions "the same for every paper"); PB L60 "Try 5 questions"; PB L80 | "Not scalable… not correct for the app" (O13) | Replace it with an onboarding that (a) asks what changes the plan (target course or college, subject combination, exam year, time per day, how prepared the student feels), (b) runs a short, real, subject-specific diagnostic served from the question bank instead of five bundled questions, (c) **ends in the sealed-sheet recap reveal**, so the signature peak happens during onboarding as Undertone did (V L109-114), and (d) reveals a first personal plan ("your first thing to fix" with real evidence), then asks for the account at the moment of value with work carried over (PB L82). Keep value before commitment and a skip path. | Yes: the length, whether the account comes before or after the diagnostic, and the content source |
| 3 | **Disclaimers on screen.** SPEC L287 non-affiliation footer, L291 per-question disclaimer, L293 "Sample, not a diagnosis…", L56 "practice, not proof" on every fresh-check surface, L531 Help line | "These kinds of things are obvious and don't need to be written" (O13) | Keep truth by **not making the claim** instead of appending a denial (UXS L111; IMP onboard L215). Move non-affiliation to Help/About and the Play listing only. Delete per-screen sample captions. Replace "Practice, not proof" with positive, accurate framing that names what comes next (for example "Practice round. Your fresh check unlocks later."). Keep honest save-state words but show them as quiet glyphs and states, not sentences, on guest screens. | No for removal; wording in copy review |
| 4 | **Mobi limits.** SPEC L57 rule 9 (never speaks, never reacts to inactivity, never sad), L165 placement list, L566-578 matrix, no Rive or Lottie (L165, L707); DES L597-602 | Expressive, inspiring, "mascot actions with meaning" (OW 3 Oct); Duolingo "use the mascot to show expressions" (PB-T L023) | Keep the research-backed limits: never during timed answering (PB L352), no guilt or sad poses for inactivity, no claims. Relax presence: Mobi as a guide through onboarding, a reactive companion on the sample and diagnostic answers, the Today hero, the recap peak and celebration moments. Allow Rive or sprite animation if it measures within budget on the M06. Allow short, factual, non-evaluative lines in onboarding only. | Yes: whether Mobi may speak, and Rive |
| 5 | **Motion restraint.** SPEC 3.1 (opacity and transform only); UXS L115 (one authored page-load moment); DES L530-531; SPEC L564 ("No confetti, no particles, no sound anywhere in v1") | "Motion is not optional"; springs, shared elements, gestures, parallax (C1; C4); interactive feel (O13); Undertone confetti plus haptic payoff (V L143) | Build a full motion system: spring physics, shared-element continuity (card to detail, sheet to recap), gesture-driven reveal, scroll-linked headers and a responsive dock. Keep it fast (budgets in item 75), keep zero motion while answering a timed mock, keep reduced-motion parity, and make celebrations proportional, once per event id, and never after a poor result (R L308). Allow a restrained particle or confetti burst for genuine milestones only. | Confetti and sound: yes |
| 6 | **No gradients or glow.** UXS L81-82; DES L286 No-Halo | "Restrained colour bloom", "softened gradients", "Never use flat colors… Subtle animated lighting" (C3; C4); the web Night Arena already ships a "soft volt aurora" (DES L550) | Allow ambient light fields as environment behind hero, onboarding and recap surfaces, matching the website. Still ban gradient text, neon halos on controls and glow as decoration on cards. Watch for over-lighting ("Maybe you have overdone the lighting", OW 8 Oct). | Direction given |
| 7 | **Theme default.** SPEC L121 (Match phone, light fallback); shots show paper by default | The owner's taste is dark and cinematic (C1; C5; the web Night Arena defaults to dark, DES L573-575) | Make a designed dark "night" world the hero identity (the late-night use scene, SPEC L89, also fits craft-floor L40 "pick it from the use scene"). Keep light as a composed option. | Yes |
| 8 | **Tab bar.** SPEC L222 (flat 64 dp raised bar, hairline, volt pill); IMP android L13 (Material nav bar) | "a good navbar wouldn't look like this… not interactive" (O13); CampusOS floating glass dock (C5) | A floating glass dock with stable partition widths (C5 dock fix), a spring active indicator, a haptic tick, hide-on-scroll, labels kept (PB L238), 48 dp targets and predictive back preserved. Reconsider five tabs: Learn is a dead tab today, so test 3-4 destinations (R L442). | Tab count: yes |
| 9 | **Volt usage limits.** SPEC L60 rule 12 (volt only on primary keys and the active tab) | A vivid, exciting, Gen Z feel (Fampay, HIGH); possible brand redesign (O13) | Keep volt as the signature action colour, but let the brand own deliberate regions (onboarding, recap, Today hero) through light and material, per colorize L42. A brand redesign may add a functional secondary family (the CampusOS "Channel" idea, C5), for example one hue per subject. | Yes (brand redesign scope) |
| 10 | **Imagery.** SPEC A1 ("plain shapes, no images"); PB L418 (no imagined campus imagery as if real); R L194 | Generate images and SVGs; ChatGPT/Codex image generation; video if needed (O13; C1; C4) | Use generated illustration, 3D-style objects, subject art and SVG motion graphics freely when they read as illustration. Never fake a real DU campus photo or a real student. Budget asset weight for the M06 (WebP or vector, lazy loading). | No |
| 11 | **Copy tone.** SPEC copy is truth-first and flat ("On this phone", "Saved on the server"); UXS L105-112 | "exciting copy, captions" (O13) | Write with voice (energetic, Gen Z, specific to CUET and DU), still concrete and still without hype clichés or invented numbers. Excitement comes from stakes and specificity ("Your first mock becomes a map of where the marks went"), not from superlatives. | Copy review |
| 12 | **No Rive or Lottie, no sound.** SPEC L707; SPEC L212 | "Rive, or Lottie when appropriate" (C1) | Allow one animation runtime if the M06 profile is clean. Sound stays off by default and opt-in only (IMP overdrive L116). | Yes |
| 13 | **Practice / Improve / My Goal IA vs Today / Practice / Review / Learn / You** (PB L234 vs SPEC L222) | Navigation is under review anyway | Run the IA test the research asked for (R L442, L495) as part of the redesign, not after it. | Yes |
| 14 | **Spec authority.** SPEC calls itself "definitive" (L3) | Owner rejected its outputs | Treat SPEC's behaviour and state contracts (sections 5, 7, 8, 10) as binding product truth. Treat its visual and copy decisions (sections 0 rules 5 and 12, 2, 2.6, 3.1, 4.1, 5.1 copy) as superseded pending a new design spec. | Confirm via the new design spec |

---

## 5. What must stay true so a flashier design does not break trust

These are integrity rules, not decoration. Removing obvious disclaimers is allowed. Breaking any of these is not.

1. **Never show success before the server acknowledges it.** Local work is never called saved (SPEC L54; UXS L100; R L605). Glass, confetti and haptics fire only after acknowledgment (SPEC L208-209).
2. **No invented numbers.** No fake counts, testimonials, avatars or social proof, and nothing illustrative shown as real (UXS L55, L162; PB L428; Atishay entity page: real, dated and sourced counts only). Generated images must not pose as real students or real campus photos (PB L418).
3. **Practice is not proof.** Practice, repair, fresh check and retained check remain distinct states in data and UI (PB L136, L279, L716-732; R L607). This can be shown structurally (Found, Repaired, Checked) instead of with taglines.
4. **No recovered-marks, percentile, admission-chance or "mastered" claims** (PB L619-621; R L438; SPEC L56). Exciting copy must still pass this test.
5. **No correctness and no Mobi during a timed or exam-equivalent mock.** Zero decorative motion while answering (PB L261, L352; SPEC L57-58, L398).
6. **Celebration is proportional.** Never after a poor or held result. Never per question. Once per event id (R L308, L601; PB L345; SPEC L564).
7. **A reveal never withholds a result.** A button, a TalkBack action and skip always work, and the ritual decays on repeat (R L600, L611; SPEC L441, L477).
8. **Only real processing stages,** no simulated percentages (R L292, L602; UXS L101).
9. **Predictable rewards.** No variable-ratio or paid random rewards, and no randomised access to learning (R L387, L401).
10. **No punitive streaks.** Nothing earned is lost; there is rest, pause and a welcoming return; no guilt notifications (R L379; PB L126, L398; SPEC L549, L600).
11. **Notifications only after value,** with refusal never blocking study and quiet hours respected (PB L396; R L604; SPEC L611-616).
12. **Privacy:** sharing is opt-in and private by default; the usage-data consent stays exact (R L446; SPEC L523-529).
13. **Accessibility survives the glass:** AA contrast measured on the glass over its worst background, 44-48 dp targets, TalkBack names, reduced motion with the same information as text, nothing carried by colour, motion or haptics alone (UXS L127-136; R L556, L610; IMP android L20).
14. **Performance on the M06 is part of the design:** blur, 3D and large assets must earn their cost; measure in profile mode on the phone, not the emulator (R L248; PB L770-772; SPEC L655-667; C1 "smooth on a normal Android device").
15. **No build talk:** route placeholders such as "/today" and "/run/:sessionId" must never reach a user build (UXS L110).
16. **Server authority** over scoring, keys, credits, Pro and deadlines is unchanged by any visual work (SPEC L59).
