# Night refinement, 5 Nov 2026 (owner LK81-LK98): the orchestrator's spec

Source of truth for every packet tonight. The owner's words are verbatim in `docs/brain/OWNER-FEEDBACK-2026-10-31-LEARN.md` on
branch feat/app-and-web (section "5 Nov 2026, about 2:40 am IST"); the ledger rows are LK81-LK98 in `OWNER-MASTER-LEDGER.md`
there. His standing rules: refine, never rebuild or cut; Night stays subtle; keep the logo and the fonts (LK73); no AI slop
(no kickers, no middle-dot lists, no text walls, no fake numbers); he judges the live site on his phone, so everything ships
finished. Audience: 16-17-year-olds, many new to CBT. UI standards: the ui-ux-standards skill (or
`C:\Users\atish\Desktop\AI OS\wiki\concepts\ui-ux-standards.md`) and `docs/research/premium-ux-ui-2026-10/AGENT_RULES.md` if
present in your worktree; run their done check before reporting.

Base: branch web/1105-perf at 0c21de817 (main 09a5bbe39 + the LK81 perf fix: held stories drawn while idle, the tour keeps its
screens mounted). Every packet works on its own branch and worktree and touches only the files it owns.

## Decisions (mine; the packets implement them)

### D1 CTAs: sign up and log in lead; the five questions are the sample (LK83, LK88)
- Hero, guest: the volt key is **"Sign up free"** (to `/signup`, or `/signup?next=%2Frecovery` when recoveryReleased()). Under it,
  one secondary key **"Try 5 questions first"** that brings the demo card (#try-practice) into view. Then one quiet line
  **"Have an account? Log in"** (Log in is a link to `/login`). Signed-in: one key "Go to Practice" (or "Find my first gap" when
  released); no secondary.
- Phone dock (LandingDock/MobileDock), guest: two keys side by side, ghost **"Log in"** and volt **"Sign up free"**, the same
  from the hero to the footer; it never changes label while the reader scrolls (no swap after the demo's five, no
  "Try a CUET question" in the dock). Signed-in: one key "Go to Practice". It still leaves at the footer (hideAtFooter) and
  stays hidden while the hero's own keys are on screen (HeroDockGate).
- Closing band (CloseActions): guest: "Sign up free" + "Log in"; signed-in: "Go to Practice". No "Try a CUET question" there.
- The demo card's note becomes one even line: **"No sign-up for these five."** (no inline link that wraps on its own line). After the
  fifth answer, the card's own end state offers "Sign up free" (keep whatever it does today if it already does).
- The checklist tests L-006/L-008/L-009/L-010/L-013 change with this (owner decision LK83/LK88, 5 Nov, supersedes the 4 Nov
  wording): update them to the new rules, do not delete them.

### D2 The hero's "CUET 2027." line (LK82) and the hero (LK85)
- He finds its font and colours weird. The muddy lamp-lit lime (#CDDD5A Night, #526700 Day) goes. Keep the display font (LK73)
  and the three-line h1. Render three variants at 390x844 Night and Day and 1440x900 Night, pick by these criteria, ship the pick:
  (a) the brand line reads as MockMob's own brand mark, not a coloured word; (b) its green is exactly the brand volt family
  (#D2F000 fill or text in Night; in Day a fill of #D2F000 with ink #0B1000, or a deep olive text #3F5200 that passes AA);
  (c) the numerals "2027" look deliberate (lining, tabular, tracking tuned, not the display font's odd figures if they are odd);
  (d) it holds at 360 px without wrapping. Candidates: a volt tag (fill, ink text, small radius, the line set a step smaller and
  heavier), true-volt text with tuned tracking, an ink line with a short volt underline bar. Write the three renders and why the
  pick won into `docs/design-decisions/web-1105-hero.md`.
- Tidy the hero's rhythm at 360/375/390/412 and 1440: one clear ladder (h1, the one-sentence lead, keys, the two fact lines);
  no ragged lines (D3); the two hero links ("Free DU eligibility and cutoff calculator", "Try the exam-day screen") stay.

### D3 Even lines everywhere on the home page (LK84)
- Every paragraph on the landing gets `text-wrap: pretty`; headings, card notes, captions and one-line subs get
  `text-wrap: balance`. No inline link that falls onto a line of its own at 360-412 px; no single-word last lines in leads.
  Check at 360, 375, 390, 412 and 1440, Night and Day. The hero lead "MockMob is CUET UG mock tests with a review that finds the
  chapter behind every mark you lose." must break evenly.

### D4 The statement's green words come back (LK86)
- The statement's accent words (marked * in homeCopy STATEMENT) are drawn in the brand green again: true volt #D2F000 in Night,
  a deep olive that passes AA on paper in Day (about #3F5200), the other words in ink. As the scrub brings each clause in,
  its accent words arrive dim like the rest and then light up green (colour, not a highlighter). This reverses the 4 Nov
  "accent is weight, not colour" rule for the statement only (owner decision LK86).

### D5 The newer parts get more thought (LK87)
- "the part that you have added, like the preparo side" most likely means the Preparoo-inspired opening ("mo" opening, LK74)
  and the typed hero line; also look at the tour's PrepOS / Ask Mobi slide. Watch each at real speed on a phone-size viewport
  (frame captures every 50 ms), compare with ug.preparoo.app's opening and typing if you can reach it, and refine timing,
  easing, caret, the hand-off to the hero and the PrepOS slide's build so each reads as finished and expensive. No new effects
  for their own sake; nothing longer than today (opening 1.28 s first visit, 1.6 s cap; skippable).

### D6 The exam section (LK91, LK92)
- He liked the previous exam screen better: it showed the real URL, and the current NTA mode is not accurate. Study the retired
  `ExamComparator` (`git show 0b63fd9b7^:src/components/landing/ExamComparator.jsx` and its CSS) and the current ExamScreen.
  Keep one component with the MockMob / NTA switch, but make NTA mode faithful to the real NTA CBT screen (layout, colours,
  palette legend, buttons, the real exam URL in a browser address bar as the old one had it) and MockMob mode our own screen.
- Put the screen inside a desktop device mock-up (a monitor with a stand, or a laptop) drawn in CSS/SVG in the Desk Light palette,
  crisp at every width; on phones it scales down as a whole. No stock photos; nothing that looks fake.

### D7 Scroll (LK89, LK90) and a slow section (LK93)
Diagnosis (read-only scout, 5 Nov ~3:30 am; verify before relying on it):
- The loop: scrollBus.run() calls jumpFrame(y) (scrollBus.mjs ~35) before the subscribers (~40), so an instant jump that lands on
  its first frame clears `jumping()` before storyController.onFrame runs (~280). `flinging()` is true for 3 s after any touchend
  (~186-188, ~276-277), including the tap on the link, so a story within one screen that the jump crosses upward is clamped to its
  last rest (keepY, ~285-289); DemoJump's two-frame correction jumps again and onFrame puts it back (keepY clears only in settle(),
  ~297-299). The page ends on the story's last step with the dock hidden. Also afterNativeTouch() (~213-216) can set keepY at the
  tap's touchend and bus.jump() never resets it.
- Fix: in storyController's onClick and onHashChange (and on any bus.jump), clear keepY/keepStory and set lastRelease = -Infinity
  (a tap that follows a link is not a fling); run the subscribers before jumpFrame(y) in scrollBus.run() so jumping() is still
  true on the landing frame (the next frame carries `landed`). Add a bench/integration test: a touch tap (with touchend) on a
  jump link followed by the jump across a near story, from just below the statement, from below the tour and from Compass; the
  page must land on the demo card and stay there.
- The arrival: target `.lp-desk__card` (the question card), not the whole `.lp-desk` (the room arrived first). Remove the
  near-white 2 px outline ring on `.mm-drill` (landing-close.css ~57-73). Arrival is quiet: the card's own rounded shell lifts
  (a short shadow and its border brightening to --line-strong, then settling over about 600 ms). Focus the card itself
  (tabIndex -1, no visible focus ring for this programmatic focus), not answer A. DemoDrill's scrollIntoView uses
  behavior 'instant' (html has scroll-behavior: smooth). If the teleport still feels abrupt, a short view-transition
  cross-fade is allowed; never a programmatic glide.
- Fast scrolling glitches (LK90): run the bench's flick matrix at high speeds (dist 600-1600 px, speed 2500-8000 px/s, both
  directions, entering and leaving each held story, also wheel bursts at 1440) and look for visible faults: a reversal, an
  overshoot that snaps back, a re-entry loop, a frame where the stage jumps, a step skipped or repeated. Fix the controller's
  rules where they misfire; keep one gesture, one step (L-027/L-028) and the no-glide rule.
- DU Eligibility ("Energy", LK93): take EligibilityTeaser out of `<Reveal>` (page.js ~265-267) or give it threshold 0; on
  phones drop the 6 px blur on `.rv` for large blocks (feature-tour.css ~109-110) and shorten big-block fades to about 300 ms;
  predraw `#du-eligibility` while the page is idle (storyPredraw.mjs `predraw(section)` works for any content-visibility
  section of `main`).

### D8 Web account pop-up (LK97) and the app's words (LK95)
- In the logged-in web app, the top bar's account door (AppLayoutClient `.arena-acct`, the avatar + name link to /profile) opens a
  small pop-over modelled on the app's Account sheet (`flutter_app/lib/features/account_sheet/`): name and plan ("Free" or
  "Pro, until 12 Nov"), credits, Appearance (Night / Day / Match device, instant), links "Name, sign-in and plan" (/profile),
  Notifications, Help, "Write to us", and a quiet "Sign out". Esc and outside click close it; focus is trapped and returns to the
  door; it is a real button with aria-expanded. The credits door stays a link to /wallet. Phones keep the dock's You sheet.
- The web's Upgrade sheet titles and include-lines follow the app's words (BillingCopy.proIncludes, the app's sheet titles), money
  terms stay web-true (rupee price, cancel in Account).

### D9 Learn subject options at onboarding (LK94)
- The options already exist (data/cuet_syllabus.js SUBJECT_OPTIONS: mathematics B1/B2, computer_science B1/B2, accountancy AFS/CAS;
  table student_subject_options; PUT /api/me/subject-options; Learn's "Your school teaches" picker). Missing: onboarding asks.
  Web: in OnboardingPageClient, right after a subject with options is picked, ask its option inline (two clear choices with a
  one-line explanation each, "You can change this later in Learn"), save with the existing API after the subjects save; the
  edit-subjects flow asks too. App: the same in the app's onboarding and You > Subjects. Learn's picker states the current choice
  plainly (no "Both parts show until you choose" limbo once a choice is saved at onboarding).

### D10 Key card turn-over (LK95) and the app build (LK96)
- Refine the turn on both: the card lifts a little as it turns (scale peaking about 1.03 at 90 degrees, shadow deepening, then
  settling), same 340 ms and curve; reduced motion unchanged. App: also at 90 degrees a soft light sweep on the incoming face.
- App build 19 (1.0.21+19) after the app packet and an emulator walk; the owner uploads it.
