# Home, next version: clarity first (spec, 20 Nov 2026, about 7:15 pm)

Written by the main session (Fable) for whoever builds it. The owner's words are in the ledger, LK360. Status: SPEC, being
built at a separate address; the live home page is NOT changed until he says so.

## Why (his words, LK360, after looking at Preparoo's site)
"as a newcomer, if I see their site, I still get a lot more clarity than we get from our side"; "we can improvise this by
maybe using an autoplay animation to explain everything automatically. How we do it on scroll, they do it automatically";
"these cards and explainer cards ... Start from the beginning instead of improvising them"; "this coverage thing: if we
could add something like this, reduce some other things from the site, and make the UI clean and polished"; "Every feature
has a different screen, so maybe we can somehow unify it"; "there is still an overload of information and not much
clarity. I think especially the weak part is the mistake lab thing"; "Just make what you feel could be best, and then
let's see what you come up with."

## What Preparoo does that we do not (from his two screenshots)
1. Every section is one plain question or promise in a few words, one sentence under it, then ONE picture.
2. One product frame for every feature (a browser window in the product's own light UI). A short list beside it names four
   things; the list advances by itself and the picture changes. A newcomer learns the whole product without scrolling a
   long pinned story or reading dense panels.
3. Proof by coverage: one large true figure ("73% of CUET 2026 questions tested concepts already covered") with the real
   questions under it, each mapped to the material that covers it.
4. One calm surface. No section has its own colour world.

## Where ours loses a newcomer today
- Sixteen sections; five tour tools each in a different dark screen; the Mistake Lab is a long pinned story of panels,
  figures and labels (he calls it the weak part); Key cards, the exam screen, Bring a mistake and the tour each explain
  one tool in their own visual language.
- Nothing says in one frame "this is what MockMob is and these are its four parts".
- No coverage proof, though the bank is the product's strongest fact (unlimited mocks from one central bank).

## The design: nine sections, one frame, phone first
Rules for every section: a heading of at most seven words that a 16-year-old new to CUET apps understands; at most one
sentence under it; one picture or one interaction; one action at most. Sentence case, no em dashes, no exclamation marks.
Every figure true to the code and data (use the page's existing constants and counts; never invent a number). Day and
Night. Phone (390 px) is designed first; 1440 follows. Reuse the existing tokens, type, buttons, Doodle marks (sparingly:
at most one mark a heading), Mobi art and real product components. No drawing tools, no decorative glow.

1. **Hero**: keep as it is (headline, the film, Sign up free, Try 5 questions, the price hook). No change.
2. **Colleges strip**: keep, thin.
3. **"Your whole CUET prep, in one place."** (NEW, replaces the tour deck, the Key cards section, the exam screen section
   and Bring a mistake as separate sections.) ONE product frame in the app's own light surface (a window with a plain
   title bar; the same frame is reused in section 5). Beside it (under it on a phone) a list of four rows, each an icon,
   three or four words and one line:
   - Practise: "Unlimited mocks, on the exam's own screen."
   - See: "Every lost mark traced to its chapter." (Mistake Lab)
   - Fix: "Revise what you got wrong, ask Mobi why." (Revise, Key cards, Ask Mobi)
   - Aim: "Your score against real DU cutoffs." (DU Compass)
   The list advances BY ITSELF about every 5 seconds while the section is on screen (a thin line fills on the active
   row); the frame cross-fades to that part's screen, which plays one short, calm demo (reuse the existing TourScreens /
   ExamScreen / KeyCards / Compass pieces restyled into the one light frame, or simple faithful recreations of the real
   app screens). A tap or click on a row jumps to it and pauses the autoplay until the pointer or finger leaves; it never
   runs under reduced motion (rows are then a plain list, the first shown, all tappable) or while the tab is hidden or the
   section is off screen. No scroll pinning. On a phone the rows are a horizontal set of four chips above the frame.
4. **"Try five CUET questions."**: keep the working sample as it is (it is proof by doing).
5. **"See exactly where your marks went."** (the Mistake Lab, rebuilt for clarity; replaces the pinned Lab story.) One
   example paper, three beats that advance by themselves in the same frame (same autoplay rules), each ONE large figure
   and one sentence:
   - "You scored 138 of 250."
   - "30 of the lost marks sit in one chapter: Partnership."
   - "Fix it in 10 questions, about 10 minutes."
   Use the figures the current Lab example already uses if they differ (they must agree with the product's sample); mark
   the example as an example in one quiet word. Then one line: "MockMob does this after every mock." and the action "Try
   it on a free mock". No panels of sub-figures, no legends.
6. **"How much of CUET does MockMob cover?"** (NEW, the coverage proof.) Subject pills; for the chosen subject, the
   syllabus chapters as a row of numbered dots (filled = the bank has questions for it) with the true count of questions
   beside the subject, and one headline figure that is TRUE: prefer "N of N chapters of the CUET syllabus covered, Q
   questions" from the real bank and syllabus data the site already holds (find where the page gets "5,117 questions in
   one live bank" and "15 CUET subjects", and the syllabus chapter lists used by Marks trend and Practice). If and only if
   the repo holds a real mapping of previous-year CUET questions to bank concepts, show a PYQ coverage figure as well.
   Never invent a percentage; if a figure cannot be computed from data, do not show it and say so in the report. Tapping a
   chapter dot shows its name and question count. Link: "See the syllabus".
7. **DU Compass**: keep, in its current compact form.
8. **Pricing**: keep as it is.
9. **Proof, FAQ, close**: creators and the wall of love as ONE section ("Students and creators on MockMob"), then FAQ,
   then the close band. The statement section and the Daily Five and Sunday section leave the home page (Daily Five keeps
   its own page and its nav link; say so in the report).

## How it ships
- Build it at a NEW address, `/home-next` (noindex, not linked from anywhere, not in the sitemap), using the same layout
  shell, nav and footer as `/`. The live home page (`src/app/page.js`) is not edited. He will open the address on his
  phone and decide; switching the real home is a later, separate step.
- Speed rules of 20 Nov apply (AGENT-COMMON.md, last section): no per-frame layout reads, transform and opacity only,
  no `:has()` on large ancestors, no blur outside a small opened surface, solid under `html[data-lite]`.
- Autoplay is his own new ask and overrides the 16 Nov "nothing self-moving" rule for these two frames only.
