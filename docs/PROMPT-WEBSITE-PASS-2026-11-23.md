You are taking over the MockMob website pass of 23 Nov 2026 (the owner's order, ledger LK427). The work is on the live home page at www.mockmob.in. The phone is the product: nearly every sign-up comes from a phone. Judge every change at 390x844 and 360x640 first, then at 1440x900.

START (read before you change anything)
1. Call continuum_start with project "mockmob" and the task "website pass LK427: CUET 2026 question by question, Daily Five, OnePlace and Lab notes, hero film".
2. Read these files in C:\Users\atish\mockmob-brain\docs:
   - NOW.md;
   - OWNER-MASTER-LEDGER.md, rows LK364 to LK368, LK370 to LK374 and LK427;
   - UI-AUDIT-LOG.md, its newest sections.
   Never run git in mockmob-brain.
3. The web repo is C:\Users\atish\Desktop\mockmob copy\wt-1110-convert, branch web/1118-prod (= origin/main). The live commit is 8c74cca7c (22 Nov, 12:28 pm).
   - Read the git log and status first: another session may have committed since.
   - The untracked files there are not yours. Leave them.
4. Load the ui-ux-standards skill, or read C:\Users\atish\Desktop\AI OS\wiki\concepts\ui-ux-standards.md. Run its done check before you report.
5. Read the memory index: C:\Users\atish\.claude\projects\C--Users-atish-Desktop-mockmob-copy\memory\MEMORY.md. Newer rules beat older ones.

THE OWNER'S WORDS (LK427, 23 Nov morning, dictated)
"Okay this is good only finally. What we have to do is take the good element from this and incorporate it into the hero section of the launch film as it is also important. This is good but this is not for the hero section. I don't know if we can incorporate it somewhere on the website or not. Let's see about that. For the hero section something like this will be created, incorporating the good elements from it. What I want you to do is build a prompt for me, firstly for around website redesign. The tasks will be:
1. Fix up the hero section of the hero section launch film, which it can see from here, and fix up the things.
2. Bring up the notes and things which we had left for our previous work in the animations of the 'Get all CUET prep in one place' and the mistake lab.
3. Come on to the daily 5, fixing the UI and explanation of that.
4. Most importantly, CUET 2026 checks, question by question, building its UI and checking it how Prepium does it, subject firstly for each stream and subject by subject, and in a concise, proper way only, not on a separate page if possible, on the home page only."

How to read it:
- "this" is the finished launch film, cut 5j.
- "Prepium" is Preparoo, the competitor.

ORDER: task 4 first (he called it the most important), then 3, then 2. Plan task 1 early, because film renders are slow and can run in the background while you work on the page.

TASK 4. CUET 2026, question by question, on the home page

What exists:
- Data: data/coverage/cuet2026/public/, which holds summary.json and one file per subject.
  - Nine papers, one 2026 shift each. Two independent checkers and a judge checked every question.
  - 382 of 416 counted questions are covered (92%):
    - 84 are the same question;
    - 21 are the same question with new numbers;
    - 277 are taught as a concept;
    - 34 are not in MockMob yet.
  - 39 reading-skill items are not counted.
  - Each question has: n, section, chapter, stem, passage, options, key, status, reason and match. The match is the MockMob question or Key card that teaches it, with its text.
- Coverage by stream (covered / counted):

  | Stream | Subject | Coverage |
  |---|---|---|
  | Commerce | Accountancy | 98% (54/55) |
  | Commerce | Business Studies | 90% (44/49) |
  | Commerce | Economics | 96% (43/45) |
  | Humanities | Geography | 81% (35/43) |
  | Humanities | History | 93% (39/42) |
  | Humanities | Political Science | 95% (39/41) |
  | Humanities | Psychology | 96% (48/50) |
  | Humanities | Sociology | 85% (35/41) |
  | Science | Biology | 90% (45/50) |

  Physics, Chemistry and Maths are not checked yet.
- The full pages: /cuet-2026-coverage and /cuet-2026-coverage/<subject>. Keep them: they hold the detail and serve search.
- The home teaser now (#cuet-2026; src/components/landing/coverage2026.mjs and CoverageProof.jsx):
  - a 92% card, "See every question", and six subject bars;
  - Political Science, Psychology and Sociology are missing;
  - no streams and no question level.
  He called the earlier version "very vague" (LK368).

His reference was a screenshot of a rival page headed "How much of CUET 2026 did Preparoo cover? 73%". In order, it shows:
- stream tabs (Commerce, Humanities, Science);
- a row of subject chips, each with its percent;
- a strip of question numbers, each marked covered or not;
- the chosen question beside the rival's own flashcard that covers it.
Take the idea, not their look. Make it better, and in MockMob's own identity.

Build it on the home page, in place of the teaser:
- Layout, top to bottom:
  - stream tabs;
  - subject chips with their percent;
  - the question strip for that subject: one cell per question, coloured by status; reading-skill items are shown but marked "not counted";
  - the chosen question: NTA's question (stem, options, the key) beside the MockMob question or Key card that covers it.
- Status in plain words: "Same question", "Same question, new numbers", "Taught: the concept", "Not in MockMob yet".
- It opens on Commerce, Accountancy, with a "Same question" cell chosen, so the side-by-side shows at once.
- One tap changes the stream, the subject or the question. No autoplay. If you add motion, the strip fills once as it comes into view.
- Concise: on a 390x844 phone, the tabs, chips, strip and the pair fit in about one and a half screens.
  - Long stems clamp, with "Show all".
  - A link to the subject's full page stays.
- Honest:
  - every number is computed from the data;
  - the Science tab shows Biology and says plainly that Physics, Chemistry and Maths are still being checked;
  - no "highest in the market" line and no comparison with Preparoo's 73% (their method differs; this limit is in LK368);
  - keep the method line: "A question counts only when two separate checks both found it in MockMob."
- Fast:
  - do not put all 416 questions in the first HTML;
  - load a subject's file when it is chosen, and preload Accountancy;
  - no layout shift when it loads.
- Headline: keep "CUET 2026, checked question by question." unless you have a clearly better one in plain words.
- Tests: extend coverage2026.test.mjs so that:
  - the numbers equal summary.json;
  - every subject can be reached;
  - every status maps to its words.

TASK 3. The Daily Five: its UI and its explanation

History:
- LK365: rethink it or remove it.
- LK366: "I'm unable to understand ... the overall explanation is really weak".
- LK367: "still a bit confusing for a newcomer".
- LK368: left undone.

What the product does today (src/lib/dailyFive.mjs and /daily):
- Five questions a day: two you missed, two from weak chapters and one new. Guests get a shared five.
- Finishing all five grows the streak.
- The Sunday Mock is one full paper on Sundays.

What a phone shows now:
- a run-on paragraph above the card;
- the card: "Daily Five", "Step 1 of 4", and five rows such as "You missed this on 14 Nov · Accountancy · Accounting Ratios";
- "Monday's five, 23 Nov. Open today, 11 h 28 min left.", then "Play today's five";
- a small "Example" chip;
- the demo cursor parked on top of row 5.

Goal: a newcomer gets it in about three seconds. Answer four things:
- what it is: five questions a day, picked from your own mistakes;
- why it helps: a mistake comes back until you get it right;
- what to do: play today's five (free, about 5 minutes);
- what the streak is.

Show it rather than write paragraphs. For example, a missed question drops from a mock into tomorrow's five, the five fill up, and the streak day lights. Make "Example" obvious to guests. Keep the Sunday Mock as the second card. Check every claim against the product.

TASK 2. OnePlace ("Your whole CUET prep, in one place.") and the Mistake Lab: the open notes

Read his notes LK364 to LK368 in the ledger.

What he approved:
- the captioned story direction;
- the Ask Mobi film;
- the Mob story;
- the Lab's stacked cards, at about 7 s a scene;
- Key cards as highlighted NCERT lines, with no pictures.

Still open:
- LK368: "there are some things which still need better maintenance of the whole CUET prep thing. I'll give feedback on that tomorrow." He never gave it, because the launch film took over.
- Learn is "a bit confusing still" (LK366).
- The combined Lab cards (LK368) were never seen on his phone.
- On desktop, the Lab cards keep 100 to 180 px empty under their content (UI-AUDIT-LOG, 22 Nov).
- Items 3 and 4 of the review below.

What to do:
- Film the six OnePlace rows and the Lab at 390x844 and 360x640.
- Fix whatever does not read in one look: pacing, empty space, cut text, the cursor over text.
- Where an older screen pictured it better, combine old and new (LK368).
- Do not rebuild these sections or cut a feature. He rejected a web restructure four times: refine in place.

TASK 1. The hero film, and a place for the launch film

What he means:
- The launch film (cut 5j: 82 s, narrated, real student clips) is "good finally", but it is not the hero film.
- The hero walkthrough film (v5, 53 s, nine chapters, live now) gets the launch film's good elements.
- Separately, find a place on the site for the launch film itself ("Let's see about that").
- The hero section around the film is in scope too.

His rules for the hero film (LK370, LK373, LK374):
- v5's voice take, script, captions, flow and 53 s length stay.
- No longer lines and no extra clauses.
- Never spell an abbreviation letter by letter.
- No screen recordings in a small window.
- Only the pictures, motion and sound change.
- Past versions:
  - v6 was "the worst";
  - v7, at 72 s, was dropped;
  - v8 (v5 plus three updated pictures; out/hero/web-v8, not live) was "very similar ... fine already". Build on v8.

Launch-film elements to bring in (choose what fits 53 s):
- the designed stage with depth: glass cards, a drifting 3D stage, the volt kicker "01 / 03";
- a hook in the first frame: familiar college crests from his folder, and the "CUET UG 2027" chip with the NTA mark;
- a live exam screen, with questions filling and the clock running;
- real student clips (Seedance 2.5, face-checked) in MockMob-promo-film/public/launch/v5/video: girl_laptop, morning_phone, college_gate, and the Mob's people (mob_riya, mob_kabir, mob_you);
- a hit on the first frame, and music from the first frame.

Also fix:
- On a phone, the 16:9 film plays at about 350x197 px and the screens inside it cannot be read (UI-AUDIT-LOG).
  - Make a phone cut (4:5 or 1:1, same voice and timing) for phones, and keep 16:9 for wider screens.
- In the film, chapter 02 is called "Mistake Repair", but the rest of the site says "Mistake Lab". Use the product's name.
- The "Sound on" key on the picture stays (owner, round 12).

Where things are:
- The film project is C:\Users\atish\Desktop\MockMob-promo-film (Remotion 4; local git only, never push).
  - Hero film: src/hero (v8 plan: docs/HERO-V8-PLAN.md; composition Hero16v8).
  - Launch film: src/launch/v4 (docs/LAUNCH-V4-STATE.md).
  - Cut 5j: out/launch/launch-v4-cut5j.mp4.
- The web player: src/components/landing/HeroFilm.jsx and heroFilmConfig.mjs. Its files are public/video/hero-v5-*.

The launch film on the site:
- Propose one place for it. One option: a "Watch the 80-second film" key near the hero or the close, opening a full-screen player. A 4:5 phone cut of at least its first 16 s would help most on phones.
- Build it behind a preview switch (like /?appnudge=1), and let him decide whether to switch it on.

Release:
- Send him the new hero film as a file first. The hero keeps v5 until he says to switch (LK370).
- Before you send it, watch it through and make a frame sheet for every chapter.
- Do the film work yourself in this main session, not in sub-agents or side sessions (his rule for the hero film).

THE REVIEW OF THE LIVE HOME (23 Nov, at 375x812 by the previous session; fold these in)
1. CUET 2026 teaser: 6 of 9 subjects, no streams, no question level (task 4).
2. Daily Five: a paragraph before the card, the cursor over row 5, and the "Example" chip too small (task 3).
3. The demo cursor rests on the words it is about to tap: in OnePlace, in the Lab (the SWOT tile "Costing you") and in the Daily Five. Park it beside its target until the tap.
4. Mistake Lab on a phone:
   - it takes about 3,500 px of scroll for five scenes;
   - at the end, its bottom rail ("Inside the Mistake Lab 1 of 5 / Skip") covers the first line of the next section;
   - check that its heading is seen before the stage pins.
5. The four generated subject objects under the Statement (an English book, an Accountancy calculator, a Business Studies briefcase, Economics scales) are the same family of generated art he called "AI slop" in LK367. Replace them with something real from the product, such as a real question, a Key card or a mock score, or remove them.
6. DU Compass: both times it was seen (the self-running score at 620 and at 680), every row read "0 of 10 cleared, short by 300". That is a bleak first read. Let the sweep spend its time on scores that clear a few colleges. It still never pauses by itself, only on Pause (his rule).
7. The page height changes while you scroll. Two reads of the heading positions differed by about 400 px, and a scripted jump to y 10,700 landed at 9,897. Measure layout shift during a phone scroll, and make #cuet-2026 and the other deep links land in the right place.
8. The hero film on a phone is too small to read (task 1).

Not looked at: a real phone, an iPhone, 1440 wide, and dark mode.

RULES (his standing rules)
- Refine the live page in place, with real product components only. Never cut a feature.
- Build first and make the change visible on a phone. Then run a critic pass against an 8/10 bar.
- On the phone:
  - one left edge, no walls of text, size by importance;
  - each section says what the feature is;
  - about 7 s for each story beat;
  - no outline boxes on real screens.
- Copy: plain words, no hype, no exclamation mark, no emoji, no em dash, and only true product facts.
- Deploying to www.mockmob.in:
  - He has given a standing OK to deploy landing work when you are satisfied.
  - First, all of these must pass:
    - npm run -s test:app;
    - the landing_checklist_1104 suite;
    - eslint;
    - both bundlers (webpack and Turbopack);
    - a filmed look at 390x844, 360x640 and 1440x900, in light and dark.
  - The hero film switch and the launch film's place wait for his word.
- Production database writes are blocked in auto mode. Ask him to reply "run it" in chat.
- Vercel Hobby allows 100 deploys a day. A Google-font fetch failure on Vercel is a flake: redeploy.
- Never print or commit anything from C:\Users\atish\MockMob-keys or from .env.local.
- Higgsfield:
  - The free trial charges USD 93.22 on 25 Nov unless he cancels. Remind him on 24 Nov.
  - Any new clip goes through the Cowork worker (MockMob-promo-film/gen-queue), never from Claude Code.
  - Reuse the face-checked launch clips first.
- Messages: send few. Only something to see, a decision that is his, an action for him, or a real risk. Give times on a 12-hour clock, read from the real clock.
- Brain:
  - Before any UI look, read UI-AUDIT-LOG.md, and add your findings to it after.
  - At the end, write:
    - outcome rows under LK427 in the ledger;
    - your own section in NOW.md;
    - a continuum_checkpoint, with no secrets (the CTO's agents read it).

DONE MEANS
- Task 4 is live on the home page, on phone and desktop. Its numbers equal summary.json, and the subject pages are kept.
- Task 3 is live: a newcomer gets the Daily Five in one look.
- Task 2: every open note above is fixed or answered, filmed at phone size, and live.
- Task 1: the new hero film (16:9 and a phone cut) is sent to him as files, with a frame sheet. The launch film's place is built behind a preview link he can open on his phone.
- Your final message lists every item in this prompt as done or not done, and says what you did not check.
