---
name: mockmob-design-direction
description: "Owner wants a premium, expressive MockMob app (glass, rich motion, generated imagery, possible brand redesign) modelled on HIGH (high.live), Revolut and Fampay; no obvious disclaimers; onboarding must not be the 5-question sample"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 604ced81-3aa7-4deb-b42c-f324ca5f51e2
  modified: 2026-10-15T19:17:41.971Z
---

On 13 Oct 2026 the owner rejected the first MockMob app build as "really basic", "rudimentary" and lacking taste. Points, in his words where possible:
- The 5-question sample onboarding is "not correct for the app" (it suits the website); the app needs a polished onboarding that connects many things.
- Remove obvious defensive taglines ("MockMob is not affiliated with Delhi University", "This is just a diagnostic"); use "important stuff, exciting copy, captions" instead.
- The tab bar is plain; he wants glassmorphism and interactive navigation.
- References: HIGH (https://high.live, site and app: "it is just crazy, we want the vibe to be something like that"), Revolut, and FamApp by Fampay (same generation). He is open to redesigning the whole brand.
- Generate imagery: SVG, and raster via Codex `$imagegen` on his ChatGPT login (codex CLI is installed and logged in; no API key). He can find video generation if needed.
- "I expect nothing but perfection."

**Why:** he gave rich research and UI/UX material and felt it was not applied; his other projects (CampusOS briefs in Continuum) show the same taste: dark, cinematic, editorial, liquid glass used physically, motion and haptics on every meaningful interaction.

**Brand DNA is fixed (13 Oct logo rounds):** volt/lime green on a dark ground and the lowercase "mockmob" wordmark. A logo round that swapped to cobalt, vermilion and navy palettes with generic symbols made him furious ("don't align at all with our brand identity... Why is this such a regression?"). "Colour or mood is off" meant refine the treatment, not replace the palette. He then chose a wordmark-led logo (lettering is the logo, one ownable detail, icon cropped from it); a mascot-face mark was "too cute". Refine within the DNA; ask before departing from it.

**Logo, 13 Oct evening:** the owner chose round 4 finalist B for now: Cabinet Grotesk Black "mockmob" with Mobi's face (volt diamond, visor, oval answer-bubble eyes) as the SECOND o, icon "mo" (start of "mob"). He liked A (first o) visually but B "makes more sense" (mock + mob); C (Clash) is out. He is consulting people and may switch to A, so keep "which o" parametric. The app opens on "mo" and expands into the full word. Files: mockmob-next/tmp/logo/final-B.

**14 Oct evening, in-use verdict:**
- **Subject art:** he wants the photo-real, lamp-lit 3D subject objects back (`assets/art/obj-*.webp`: a red ledger, a brass stamp, a scale with an onion, a cube and compass). Phase 1A had replaced them with flat code-drawn emblems, which read "basic and very childish". He said the vibe was lost.
- **Bar icons:** the custom-drawn bar icons (a sun on a line, a pencil with a dot) look "extremely weird".
- **Clipping:** some logos and icons are not fully visible.
- **Rule:** prefer rich generated imagery over flat vector stand-ins, and never crop an object.
- **22:15 follow-up:** the restored 3D objects look "really premium". He still wants each object to say its subject.
  - Weak: Accountancy (a red ledger; the flat calculator plus balance sheet made more sense), Computer Science (a circuit board he could not read), Business Studies (a brass stamp), Languages (a blank notebook).
  - Plan agreed in principle: regenerate only those, in the same lamp-lit style, and show old next to new before shipping.
  - He said he is "afraid to tell you to make any changes because most of the time it doesn't happen the way that I expect". So never make regressive changes, and offer reversible, previewed options.
  - Any new feature must be built for the app and the website together.

**15 Oct morning:** the live Mistake Repair worked (gpt-6-luna) but he wants it "a bit more useful, more insights". He also asked for a SWOT after each mock, with one-tap recommendations of specific topic mocks. Bigger point: "everything is very confusing for a new student coming to the site. App is good in this term but website needs fixing or even a redesign." So the website should take the app's structure and first-run clarity, and new features must be integrated into the flow, not bolted on. Keep adding useful features.

**16 Oct about 00:45 IST, hero verdict:** a hero with glowing keys (a sheen sweep, a light running round the edge), drifting glow blobs and gradient text "doesn't look very impressive... really amplifies the AI slop look... a regression".
- **His slop reference** is section 10 of `C:\Users\atish\Desktop\AI OS\wiki\concepts\ui-ux-standards.md`. Check every visual change against it.
- **Changing headline line:** he remembers the old morphing text (`morphing-text.jsx`, April to 4 Oct). A typed line or a crisp per-letter morph is fine. Glass is not needed.
- **What "impressive" means:** typographic confidence, composition and real product moments. Never glow or ambient loops.

**16 Oct about 01:00 IST, slop defined further:**
- The Repair scene "Repair the reason, not just the answer" had a green eyebrow pill with a pulsing dot above it and four subject icons below it. He called that "a pure giveaway that this is an AI-generated website".
- He wants real typographic hierarchy, the way professional sites do it, instead of cards, pills and badges.
- He rates the site 50-60, and the target is 90.
- His design skills are now installed in `~/.claude/skills`, copied from the repo's `.claude/skills` and from AI OS: emil-design-eng, high-end-visual-design, redesign-existing-projects, design-taste-frontend, minimalist-ui, apple-design, gpt-taste, stitch-design-taste, animate, improve-animations, review-animations and find-animation-opportunities.
- Use them alongside ui-ux-standards (which wins conflicts) and impeccable.

**How to apply:** for MockMob UI, his newer direction overrides the generic "no glass, no gradient" lines in the UI standards digest; keep legibility, accessibility, M06 performance and the truth rules (no success before acknowledgment, no fake numbers). For big redesigns, research the references, show visual concepts and interview him in batches before building, then implement without another long document. See [[subagent-model-choice]] and [[emulator-ram-rule]].

**18 Oct 2026, about 3:50 am, the owner's choices:**
- **Copy tone:** exciting and bolder. Use punchy, energetic lines in place of disclaimers, on the landing and in onboarding. It is still never false: real numbers, no unprovable claims.
- **Badges:** keep them ("they look cool"). Refine how they are presented and what they do; never remove them.
- **The social side** is called **Mob**. The word "community" is retired.
- **The app's logo B opening** runs 3 s on the first launch after install only; later launches stay short.
