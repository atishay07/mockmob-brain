# Astra round 3: brand, mascot, copy, responsiveness and the Arena, with full creative delegation

You are continuing MockMob in `C:\Users\atish\Desktop\mockmob copy\mockmob copy`. Act as a senior product designer, brand designer, design engineer and frontend implementer at once. I am the owner. I like the current direction (the animation and styling are "really good"), and I want you to take it further with imagination: think like a studio given a brief, not a contractor given a ticket list. You have explicit creative delegation for visual, motion, copy and interaction decisions. Do not stop to ask me to choose between variants; explore, decide, explain briefly, ship.

## 1. Read first (authority and current state)

Read `AGENTS.md`, `PRODUCT.md`, `DESIGN.md`, `docs/brain/README.md`, `docs/brain/ROADMAP-2027.md`, and the top three entries of `docs/brain/STATUS.md` (they describe what Claude shipped on 3 October 2026: hero scroll depth, glass proof dock, scroll-scrubbed statement, creator reach section, Compass Pro, the CUET Subject Combo Planner at `/cuet-subject-combination`, rebuilt Today/Review/Progress, shared `ArenaHead`/`ArenaStats` in `src/components/arena/ArenaHead.jsx`). Inspect `git status` and diffs before editing; the tree has extensive uncommitted work. Preserve it. Never reset, clean or bulk-revert. Next.js 16.2.4 has breaking changes: read the relevant guide in `node_modules/next/dist/docs/` before framework code.

Use `npm.cmd` in PowerShell. The dev server is usually at `http://localhost:3000`. `/preview/arena?view=dashboard|test|prepos|compass|radar|saved|today|review|progress&plan=pro` is a development fixture with stubbed account APIs; it proves layout, never real auth, persistence, entitlements or billing.

## 2. Skills: use them deeply, not by name

Read in full before designing: Scroll Craft (`C:\Users\atish\Desktop\mockmob copy\scroll-craft-main\plugins\nateherk-design\skills\scroll-craft\SKILL.md` plus `references/hero-depth.md`, `feel.md`, `devices.md`, `uniqueness.md`, `approved-collection.md`, `taste.md`, `verify.md`), and every Emil Kowalski skill under `.agents/skills/` (`emil-design-eng`, `animate`, `improve-animations`, `review-animations`, `find-animation-opportunities`, `animation-vocabulary`, `apple-design`, `mobile-native`, `break-ui`, `prototype`, `pick-ui-library`, `ask-sonner`), with their referenced files when the workflow applies. Also use any other frontend design, branding or image skills available in your environment. Keep a short skill-use matrix (skill, where applied, concrete artifact or check) in your notes. `animate-expo` and `write-swift` do not apply: this is a Next.js website.

Write a Scroll Craft `BRIEF.md` marked "Self-authored under explicit creative delegation", with a feeling curve, one engineered peak, the tell-someone sentence and a signature move. Adapt its principles to semantic React plus the existing CSS/Motion system; do not replace the site with a standalone HTML page or add a second animation runtime without a strong reason.

## 3. What I want this round

### A. A brand with a character: design a MockMob mascot
Give MockMob a memorable identity beyond the volt colour. Design an original mascot with ChatGPT's built-in image generation (the image tool in your environment, not a paid API, not Kie). Before generating, write a short creative brief: who the character is (a CUET companion, a coach or a study buddy, your call), its personality matched to our voice (tech-superior, warm, a little cheeky, never childish), silhouette, palette built around volt `#D2F000` on Night Arena dark, and why it fits Indian Class 12 students at 11pm on a budget Android phone.

- Produce a consistent character sheet first, then a small set of poses or expressions tied to real moments: greeting (hero), thinking (Mistake Lab), pointing at a number (Compass), celebrating a correct answer (demo drill), sleeping or idle (empty states), and worried but encouraging (error states). Keep identity, proportions and palette identical across poses.
- Inspect every output at its real rendered size and on a 360px phone crop. Make genuine transparent cutouts (check the alpha), optimise to WebP/AVIF with explicit dimensions and alt text, and copy finals into `public/brand/mascot/`. Record prompts, chosen files and rejected attempts in `docs/brain/BRAND-MASCOT.md`.
- Make the mascot flow through the landing page with Scroll Craft: it should travel, react or change pose as the visitor moves through the journey (hero, then Mistake Lab, then Compass, then the close). That journey is a strong signature-move candidate. Use transform and opacity only, layered depth, and a static fallback under reduced motion. It must not cover copy, CTAs or the demo, and must stay light on a budget Android.
- Use the mascot sparingly in the Arena: empty states, first-run moments, a completed session, loading. Never on high-frequency study actions, never animated while a student is answering.
- The mascot is a brand character, never a student, testimonial, creator or endorsement. Do not generate student photos, creator thumbnails, testimonials or outcome imagery.
- Also refresh supporting brand touches where they earn their place: OG image, favicon or app icon treatment, loading moments. Keep Gabarito, Hanken Grotesk and mono, the volt signature, light and dark themes, and the existing campus illustrations.

### B. Copy: make every line earn its place
The visual polish is ahead of the copy. Rewrite marketing and in-app copy for clarity, confidence and a distinct MockMob voice, without breaking truth rules. Specific examples I noticed:

- The glass proof dock under the hero: "199K+" and "2 exam screens" work and "73 programmes" is fine, but "50 in 60" is unclear. Rewrite all four cells as instantly understandable facts: a sharp number or word plus a short human sub-line.
- The hero lede, section sub-heads, the scroll statement, the Compass Pro and Combo Planner promos, FAQ answers, empty and error states, buttons. Shorter, more specific, student-first. Read everything aloud at the 11pm-before-a-mock level.
- Keep claims honest: no invented counts, testimonials, rank or score guarantees; "projection, not prediction" on Compass Pro; subject eligibility is not admission.

### C. Creators section detail
For Garima Jain, lead with **@du__club (161K followers)** rather than @garima.again (25.2K). The reel `DX4Buebt9xI` appears to be a du__club post or collaboration. Verify on Instagram, then update `src/lib/social.js` (handle, attribution, ordering by reach) and the card so the bigger, posting account is the headline. Keep counts dated, sourced from public profiles, and keep paid partnerships marked.

### D. Explore ("The Mob's Feed") is broken: rebuild it properly
`src/app/(app)/explore` with `src/components/feed/DiscoveryFeed.jsx` (1,264 lines, an inline `<style>` block, about 41 inline styles, the old "// Discovery" eyebrow, the italic "The Mob's Feed" headline) and `QuestionCard.jsx` are broken in both UI and function. Audit what actually works against `/api/questions/feed`, `/api/questions/explore`, `/api/subjects`, `/api/chapters`, `/api/learning/summary`, bookmarks and votes. Then redesign Explore as a genuinely good study surface: fast filters (subject, chapter, difficulty), a solve-in-place card with clear answer feedback and explanation, save, vote, an infinite or paged list with real loading, empty, error and end states, streak or progress only if real data backs it, and a phone-first layout. Move styles into the Arena CSS system with the shared `ArenaHead`. Fix confirmed functional defects after tracing their API contracts; add tests where logic changes.

### E. Information architecture of the Arena
The sidebar groups are Study (Today, Practice, Review, Progress, Account) and Tools (Radar, Saved, Compass, PrepOS, Explore, Ranks, Contribute, My uploads). Rethink it: Explore belongs in Study, Account probably does not, and Saved and Review may belong together. Propose and implement a clearer grouping (desktop sidebar, mobile nav and moderator variant) with stable routes.

### F. Finish the Arena to the Practice standard
Practice, Today, Review, Progress, Radar and Compass now share one language. Bring the rest up to it with the same care: Leaderboard/Ranks, Account/Profile, Contribute/Upload, My uploads, PrepOS/mentor, Result, AI Rival, onboarding, login/signup, plus the NTA runner chrome (keep its intentional exam skin). Check free, Pro, expired, empty, loading, error and no-history states. Extend `/preview/arena` fixtures where needed (development only, clearly labelled).

### G. Responsiveness: make it really 100%
I am not convinced every section is fully responsive. Do a systematic `break-ui` plus `mobile-native` pass across every public and Arena route at 320, 360, 390, 768, 820, 1024, 1280, 1440, 1920 and short landscape, both themes, 200% text, reduced motion, keyboard and touch emulation. Fix overflow, clipped text, cramped controls, under-44px targets, sticky or dock occlusion, safe areas, and long subject or college names. Keep a route-by-width checklist in your notes.

### H. Your own ideas
Beyond this list, find the three to five highest-leverage improvements a world-class studio would make to MockMob's look, feel and story, and implement the ones you believe in. Use `prototype` for the biggest open design questions (three genuinely different directions, pick one yourself), and `find-animation-opportunities` to reject motion that does not earn its place.

## 4. Non-negotiables

- Truth: no fabricated testimonials, student counts, rank or score claims. The Wall of Love stays hidden: `src/lib/voices.js` is empty on purpose, and the live-site quotes are not verified (one is the founder's own). Creator numbers must be real and dated.
- Pricing follows `publicOffer()` in `src/lib/payments/offer.js`. ₹99/month opens only when `RAZORPAY_PLAN_ID_PRO_MONTHLY_99` is set; do not create Razorpay plans, run checkout or touch payment flows.
- No paid model calls; no Kie; respect the $2 calibration within $10 lifetime budget guard. Image work uses only the built-in ChatGPT image generation.
- No deployment, production migrations, bank mutation or external messages. Keep server scoring, session resume, atomic credits, AI-wallet reservations, entitlements, release flags, evidence quarantine and the NTA skin intact. MockMob is not affiliated with NTA or DU, and that disclaimer stays.
- Accessibility and the budget-Android/patchy-4G floor govern every decision: 44px targets, 4.5:1 contrast in both themes, reduced motion respected, no heavy WebGL by default, lazy and optimised assets.

## 5. Verify and deliver

Verify in a real browser as you go (real pointer, keyboard and touch input, not only DOM clicks): intermediate scroll positions, both themes, reduced motion, phone widths. Run `npm.cmd run lint`, `npm.cmd run build`, `test:recovery`, `test:du`, `test:learning`, `test:nta`, `test:answer-integrity` and `node --test data/tests/payment_entitlements.test.mjs` after relevant changes. Record actual verification, assets created, remaining gaps and the rollback boundary at the top of `docs/brain/STATUS.md`.

Final reply: what changed and why (with before and after screenshots of the key moments), the mascot and its journey, the copy changes, the Explore rebuild, the new IA, the responsive checklist, tests run, and anything you could not verify. Be candid.
