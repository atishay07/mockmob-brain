# Higgsfield ideas brief: where real video beats SVG and code (16 Oct 2026, living document)

Read with HIGGSFIELD-PLAN-2026-10-16.md (budget, models, rules) and HIGGSFIELD-RESEARCH-2026-10-16.md (verified prices and features). This file collects ideas. Nothing here is approved for spend until the owner picks it at the storyboard step.

## The owner's direction (16 Oct about 11:15 pm, his words in substance)
- "I don't think that it is necessary to add animation in the subjects... Maybe it is more useful to use it somewhere on the website landing page or in app onboarding."
- "I was thinking in the direction of some scroll animations. Although we already have it... with Mobi, with SVG images... Sometimes we need some proper animation. This is just one of the examples. There can be many others."
- "Compile your ideas, put it in context, and include instructions to keep iterating on it... fire up some Haiku/Sonnet agents to give ideas. When we have multiple ideas... we can implement something which we like the most."

So the subject-object one-shots (U1 in the plan) are **deprioritised**. The focus is the **landing page (including scroll storytelling)** and **app onboarding**, plus any other place where "proper animation" beats SVG and code.

## Seed ideas (from the main session; to be extended by the idea agents)

| ID | Surface | Idea | Why video beats code here | Rough shape and cost |
|---|---|---|---|---|
| I1 | Landing, the "One question bank. As many mocks as you want with Pro." section | **The bank deals a fresh paper**: a lamp-lit vault or library of question cards; on scroll, cards lift and assemble into a new paper, and every scroll pass shows a different combination. It makes the headline differentiator (unlimited mocks from one central bank) visible. | Depth, light, paper and many small moving parts look cheap in SVG | Scroll-scrubbed 6-8 s sequence; drafts on Wan 480p, final on Seedance 2.5 at 720p or Wan at 1080p; about USD 2-3 |
| I2 | App onboarding, first launch | **The room wakes up**: the existing Night/Day welcome room art; the lamp clicks on, light spreads, and it settles exactly on the welcome still. Once, skippable, never again. | Real light falloff and atmosphere | 3-4 s portrait 720p, Wan or Kling, last frame = the welcome still; about USD 0.5-1 |
| I3 | Landing hero (optional, only if I1 and I2 work) | The same room moment in wide format beside the hero text; the still loads first (the LCP element) and the video plays after load | First impression; the brand world | 4-5 s 16:9; about USD 1-2 |
| I4 | Landing held stories (Mistake Lab, tour, Score Recovery Lab) | **A paper's journey as a scrubbed sequence**: a mock paper lands on the desk, the wrong answers lift out and settle into a repair notebook. It is a cinematic bridge between the real-UI scenes, never a replacement for them. | Continuity and camera movement that the UI mock-ups cannot do | 5-6 s scrub; about USD 1-2 |
| I5 | App first timed mock finished (once) | A short "first paper filed" moment: the paper slides into a lit folder | An emotional reward for a true event | 3 s; about USD 0.4 |
| I6 | Play listing (later, January) | 2-3 mood shots framing real screen recordings | Marketing; deferred by the owner's January rule | See the plan, U2 |

## Rules any idea must pass (from the owner's research and standards)
- **Real UI stays real.** Video is metaphor and mood, never an AI-generated product screen or fake result (T007, T009).
- **No AI Mobi.** Mobi stays the code rig; he may sit next to a video, never inside it.
- **Motion answers something.** Scroll position, a first launch or a real event. Never an endless ambient loop on a resting screen.
- **Performance:**
  - the still poster renders first;
  - mobile LCP must not get worse (the landing is about 4.7 s on mobile already);
  - about 1 MB or less per clip;
  - no autoplay under Save-Data or reduced motion: show the still;
  - pause when offscreen.
- **Scroll-scrubbed video technique:**
  - encode with every frame a keyframe (GOP 1) so seeking is smooth;
  - or use a canvas image sequence (WebP frames, about 60-90 frames, lazy-loaded) driven by scroll position;
  - pick per clip by weight;
  - test on a budget Android phone in Chrome.
- **Night and Day:** either a version for each theme or a neutral scene that sits well on both.
- **Every claim true.** The bank scene must not imply "never repeats". The landing already says an answered question can come back.

## References the owner admires
- **Opal (iOS) onboarding, via Mobbin**, shared by the owner 16 Oct about 11:40 pm: https://mobbin.com/flows/be4b5aa1-ba9d-494c-acbb-9ce8faa0d6f5 . A dark, cinematic 3D scene: a glowing opal crystal breaks out of rock with the line "Closer..." and a tap to continue. It is almost certainly pre-rendered 3D video or real-time 3D, not SVG. Use it as the bar for I2 (onboarding opening) and I1 (the bank scene), e.g. our central question bank or vault opening to reveal a fresh paper. Adapt the craft and pacing, never copy: our standards ban ALL-CAPS labels ("TAP TO CONTINUE"), keep it skippable, respect reduced motion, and load the still first.
- **iOS-only references are fine for taste.** MockMob's Flutter app has its own design system, so iOS screens are taste and flow references, not component specs. Translate only the Android conventions: system back, Android 13+ notification permission, share sheet, pickers, stretch rather than bounce scrolling, gesture bar, haptics.

## How to keep iterating (the loop future agents follow)
1. **Ideate.** Spawn 5-7 idea agents (mix of Haiku for breadth and Sonnet for depth), each with one lens and read access to this file, the plan, the research file, the landing source (src/app/page.js and src/components/landing on web/land2-1015), the app onboarding code (flutter_app/lib/features/onboarding), and AGENT_RULES.md. Suggested lenses:
   - A: landing scroll storytelling;
   - B: app onboarding and first run;
   - C: making the unlimited-mocks bank visible;
   - D: emotional moments tied to true events;
   - E: technical feasibility and performance (scrubbed video, canvas sequences, Flutter video, bandwidth);
   - F: a contrarian, "where video would be slop or waste money";
   - G: what premium apps do (HIGH, Revolut, Fampay, Duolingo, Apple product pages), described not copied.

   Each returns ideas in the table shape above, plus evidence IDs and risks.
2. **Synthesize.** One Sonnet agent dedupes and scores each idea 0-2 on impact for a student, truthfulness, fit with the owner's taste, performance risk (inverted) and cost. It ranks the top 8 and appends them to this file under "Round N".
3. **Storyboard (free).** For the owner's top picks, make the start and end frames (and 2-3 middle frames) with the owner's GPT image account in our art style. Show them in place, as mock-ups on the landing or onboarding screen.
4. **Owner picks.** No video spend before this.
5. **Draft cheaply.** Wan 3.0 480p, 2-3 variants, seed fixed. Log every call in tmp/higgsfield/LEDGER.csv after an /estimate.
6. **Final.** On the model the research file recommends for that shot (Seedance 2.5 at 720p only where its accuracy is needed). Show it in place on the real page or app (390 and 1440, Night and Day, the emulator for the app), then the owner signs off.
7. **Ship** through the normal gate (tests, visual critique, verifier).
8. **Record what was learned** under "Lessons", with what each model did well or badly on our kind of shot.

## Round 1 (to run after the 16 Oct 12:30 am usage reset)
Not run yet: at 11:15 pm the 5-hour usage window was at 87% with seven build agents mid-work, and a new wave would have risked killing them. The next session (or this one after the reset) runs step 1 and step 2 and appends the results here.

## Lessons
(None yet. No video has been generated.)
