# Higgsfield (AI video) plan, 16 Oct 2026

> **Direction update, 16 Oct about 11:15 pm (owner):** subject-object animations (U1) are deprioritised. Use the budget where "proper animation" beats SVG and code: the **landing page (including scroll storytelling)** and **app onboarding** first, then other places. Ideas, rules and the iteration loop are in **HIGGSFIELD-IDEAS-2026-10-16.md**. The budget rules, models and ledger below still apply. Re-plan the step amounts for the picked ideas after the storyboard step.


The owner's question (16 Oct, about 10:40 pm): is Higgsfield video useful for MockMob's website and app, where are we lacking motion, and how should a USD 15 API budget be spent, with a plan future agents can follow. Prices are the owner's screenshot of the Higgsfield API page on 16 Oct. They are "from" prices for each model's cheapest mode, so 1080p costs more. Confirm the mode price in the API before every run.

## 1. Verdict: useful, but only for a narrow set of jobs

**Video is NOT for UI motion.** Screen transitions, sheets, count-ups, the result reveal, the clock turn, press feedback and Mobi all stay code-native (Flutter animations, CSS and the Web Animations API, SVG), for five reasons:
- **Themes:** code motion follows Night and Day. A video does not.
- **Crispness:** code motion is sharp at every size. Video blurs and bands on text and edges.
- **Interaction:** code motion is interruptible and follows the finger. Video only plays.
- **Reduced motion:** code motion honours it per element.
- **Cost:** code motion weighs almost nothing. Video adds MB to the APK and to bandwidth.

The owner's research brain agrees: motion must answer an action or show state (AGENT_RULES; the app pass removes loops on resting screens, M05). It also says to use real product screens, never fake dashboards or fake results (T007, T009). So an AI video of our own UI is not allowed.

**Mobi stays a code rig** (rig v2, 31 acts, one character on both surfaces). An AI video of Mobi would be a second, off-model Mobi. Do not do it.

**SVG versus video:** SVG and code cover flat shapes, icons, lines, numbers and the mascot. They cannot convincingly do lamp light, paper, texture, depth or camera moves on our lamp-lit subject objects. That is exactly where video earns its place.

## 2. Where video adds something we cannot get otherwise

| # | Use | Where it shows | Why it is not slop | Size limit |
|---|---|---|---|---|
| U1 | **Subject objects come alive, once**: a 1.5-3 s one-shot when a student picks a subject. The ledger book opens, the briefcase unlatches, the economics chart rises. Never a loop. | App Practice subject pick and subject hub hero; website Practice subject pick and the landing subject shelf on select | It answers an action (the pick). It ends on the existing still, so the still stays the canonical art. Reduced motion shows only the still. | 512x512, H.264 MP4 and VP9 WebM, about 150-250 KB each. App: stream from the CDN with the still as the poster; never bundle all 15. |
| U2 | **Play Store and launch promo**: 2-4 cinematic shots (lamp-lit desk, the subject objects, night-to-morning) that open and close a 30 s promo. **The middle of the promo is real screen recordings of the app.** | Play listing promo video (YouTube), the landing "see it" link later | The real product is shown as real recordings. AI covers only mood shots of our own art world. | 1080p source; YouTube hosts it |
| U3 | **One milestone moment**: a short object-based celebration for a true event (first timed mock, a badge), shown once | App result after the event, website Progress | It is tied to a real event and plays once. | Same as U1 |

**Not planned:** hero background video, ambient loops, fake product demos, AI Mobi, talking heads, any marketing campaign video. Marketing waits until January, per the owner.

## 3. Which model for which job (revised after research, 16 Oct about 11 pm; sources and caveats in HIGGSFIELD-RESEARCH-2026-10-16.md)

**Correction:** the screenshot's "from" prices are 480p (cheapest) rates. The first draft of this plan underpriced 1080p badly.

| Model | 480p | 720p | 1080p | Verified features | Use |
|---|---|---|---|---|---|
| **Wan 3.0** | USD 0.020/s | about 0.04/s | about 0.08/s | last-frame control, 1:1, fixed seed, 2-30 s; arena rank 4, close to Seedance | **Primary for U1/U3** (drafts at 480p, finals at 720p), and a U2 candidate at 1080p |
| **Kling 3.0 Standard** | 0.042-0.063/s (the reason for the split is unverified) | n/a (no resolution field) | Pro and 4K are separate endpoints | last frame (not Turbo), 3-15 s, no seed or negative prompt documented; arena rank 18 | **A/B against Wan** on the 3 test subjects; U2 candidate (Pro) |
| **Seedance 2.5** | 0.144/s | about 0.32/s | about 0.80/s | last frame, 4-30 s (minimum 4 s); arena rank 2 | **Only** for a U2 shot the owner picks that Wan and Kling cannot hold, at **720p** (about USD 1.3-1.6 per 4-5 s shot). Never at 1080p on this budget. |
| Wan 3.0 Prime | 0.027/s | 0.056/s | 0.112/s | speed tier, no quality gain | Skip |

**Facts that shape spending:** failed, moderated and timed-out requests are not charged, and a queued cancel is refunded. A clip that renders but that we reject IS charged. There is a `/estimate/` endpoint: call it before every generation. Credits expire after a year. The Wan 60% discount ends 31 Oct. The Kling and Seedance promo end dates are not published: if Kling's discount ends, use Wan at 720p for the rollout.

**Stills (keyframes, Play graphics):** the owner's GPT Image account first, since its cost is already paid.

## 4. The USD 15 budget (revised)

| Step | Model and mode | Plan | Cost |
|---|---|---|---|
| 0 | none | Keyframes from approved object art (the canonical still as the LAST frame); prompt sheet per use; owner picks the 3 test subjects | 0 |
| 1 | Wan 3.0 480p, 1:1, fixed seed, audio off | 3 subjects x 3 prompt variants x 3 s (27 s) | about 0.55 |
| 2 | A/B at production quality: Wan 3.0 720p vs Kling 3.0 Std | 3 subjects x 3 s on each (18 s) | about 1.5 |
| 3 | Owner review in place (app and site) | **STOP unless he approves**; he also picks the winning model | 0 |
| 4 | U1 rollout on the winner | 12 subjects x 3 s + 1 retry each (about 72 s at Wan 720p) | about 3.0-4.5 |
| 5 | U2 promo, 3 shots of 5 s | Wan 3.0 1080p or Kling Pro first (about 0.8 per shot); Seedance 2.5 720p only for one shot the owner picks | about 2.5-4.0 |
| 6 | U3 | 1 clip of 3 s on the U1 winner | about 0.4 |
| 7 | **Reserve** | Rejected clips we must pay for, retries, price changes | **at least 2.2 (15%)** |
| | | **Planned total about 12.8, hard cap 15.0** | |

## 5. Rules every agent follows

1. **Estimate, then ledger.** Call the `/estimate/` endpoint before every generation. **Ledger first.** Log every generation in `mockmob-next/tmp/higgsfield/LEDGER.csv`: time, model, mode, seconds, resolution, estimated and actual cost, purpose, result file, kept or rejected. Before each call, sum the actuals. If the call would pass USD 15, do not make it.
2. **The key never appears in chat or a commit.** The owner puts `HIGGSFIELD_API_KEY` in a git-ignored local env file. Agents read it from the environment only.
3. **Image-to-video from our own approved stills.** No text-to-video of the product, no AI Mobi, no AI UI.
4. **Owner approval at step 3** before any batch run. Show the clips in place, in the app and on the site, not as files.
5. **Ship rules:**
   - one-shot only, never a loop on a resting screen;
   - the poster still renders first;
   - reduced motion shows the still only;
   - stay under the size limits in section 2;
   - Night and Day both checked;
   - the clip ends on the canonical still, so there is no jump.
6. **Done means seen in use:** captured at 390 and 1440 on the website and on the emulator for the app, with screenshots and a recording looked at. A file in a folder is not done.

## 6. Status

The account is not connected yet. Next step when the owner says go: he adds the key to a local env file, and an agent runs steps 0-2. That is about USD 2.5 at most, with the 3 test clips shown to him in place.
