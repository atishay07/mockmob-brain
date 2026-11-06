# Round-3 review findings (1 Nov 2026, about 10 pm IST)

Five lenses on the merged round 3 (shots: tmp/learn-1101/r3-merged/INDEX.md, 180 PNGs). Every blocker, high and medium finding was checked by 1-3 independent skeptics: SURVIVES = confirmed, refuted = not real or intended (header only here). LOW = not checked. IDs like ui-correctness#1 are what R4-SPEC.md cites. Evidence is the skeptics' own words, cut to 700 characters.

```text

##### LENS owner-eye | Ship after fixes. Round 3 answers LK27 (a clear "Start learning Accountancy" offer with no zero lines), LK29 (a first-visit swipe chip on a real peek edge) and LK31 (ends are down to a headline, at most 3 numbers and 2 keys). But LK32 (the hero) is visibly unchanged on the phone, LK30 (blank space) got worse on the end screens and the Free refusal, and two truth problems (mixed chapter numbering, a Part 2 option the student can't see) would mislead a student.
[owner-eye#1] refuted 0 of 3 | blocker | Home hero, phone and desktop (LK32)
[owner-eye#2] SURVIVES 2 of 2 | high | Run, feed, chapter page, Explore covers: chapter numbering
  P: Two numbering systems contradict each other on the same screen. The run's left column says "Part 1, Ch 1" while the card under it cites "NCERT, Accountancy Part 1, Ch 2, p. 48". Learn home says "Chapter 1 of 14". Change in Profit Sharing Ratio, Goodwill and Admission of a Partner are all labelled "Part 1, Ch 2", although the roadmap lists them as the 3rd, 4th and 5th chapters. The feed's desktop rail reverses the order again ("Ch 2, Part 1"). A student can't tell which chapter they are in, or whether the source line is right.
  F: Pick one student-facing label. Use the roadmap position ("Chapter 5 of 14") or the NCERT unit name ("Reconstitution, Unit 2"), never a bare "Ch 2" shared by three chapters. Keep the NCERT page reference only inside the source line, and make it say "NCERT book" so it doesn't read as the app's chapter number. Use one order everywhere ("Part 1, Ch N").
  I: r01-run-card-front-1440-day.png; c03-chapter-resume-390-night.png; x01-explore-top-1440-night.png; l01-learn-home-fresh-free-390-night.png
  Files: src/components/learn2/run/**, feed/**, chapter/**, Explore covers
  EV: CONFIRMED: I confirmed the contradiction in three of the four cited screenshots. I did not open the feed rail screenshot, so the "Ch 2, Part 1" reversed order is unchecked. (1) r01-run-card-front-1440-day.png: the left column under "Accounting for Partnership: Basic Concepts" says "Part 1, Ch 1". The card footer on the same screen says "NCERT, Accountancy Part 1, Ch 2, p. 48". (2) x01-explore-top-1440-night.png: the cards read "Part 1, Ch 1" (Basic Concepts), "Part 1, Ch 1" (Profit and Loss Appropriation Account), "Part 1, Ch 2" (Change in Profit Sharing Ratio) and "Part 1, Ch 2" (Goodwill). The numbers repeat and do not run 1, 2, 3, 4, and the strip reads as the 1st, 2nd, 3rd and 4th chapte
[owner-eye#3] refuted 0 of 2 | high | End screens and Free refusal, phone (LK30)
[owner-eye#4] SURVIVES 1 of 2 | high | Learn home roadmap, Part 2 options
  P: "Part 2 has two options. Pick the one your school teaches." sits above two pills, and neither looks selected. Yet the list below shows only the Analysis of Financial Statements chapters, because the Computerised Accounting chapters, which have no cards, are hidden silently. A Computerised Accounting student sees an apparently unchosen option and a list that is not theirs, with no 'coming' line. LK2 was already a complaint about this picker.
  F: With nothing picked, either show both groups or pre-select nothing and hide both until a pill is tapped. Give the pills a clear pressed state (aria-pressed and a filled style). When the picked or implied option has no cards, show "Cards for this option are coming."
  I: l01-learn-home-fresh-free-1440-night.png (pills at x 860-1300, y 635-675); l01-learn-home-fresh-free-full-390-night.png
  Files: src/components/learn2/home/ChapterMap.jsx (~L297-L320, PartSwitch/OptionGroup)
  EV: REFUTED: I checked the 1440 and 390 night screenshots and the code in ChapterMap.jsx, homeModel.mjs and learn-home.css.

What the screenshots show: Part 2 has the line "Part 2 has two options. Pick the one your school teaches." and two outline pills with neither filled. Below them sit the shared Company Accounts unit (Share Capital, Debentures) and the Analysis of Financial Statements unit. No Computerised Accounting chapters are drawn.

Why this is intended rather than a defect:
1. R3-SPEC R5 says chapters with no cards are hidden and the "Cards for this option are coming." line shows only "if the student's picked option has none at all". Nothing picked is not that case. The code comments s
[owner-eye#5] SURVIVES 2 of 2 | high | Today, brand-new student, phone
  P: The floating "Your week and road" glass pill now sits on the start card's swap row. It covers "Tap one to s[wap]…" and the tops of "A full mock" and "Start with…" on the first screen. This is new to the first screen in round 3, because T1 shortened the card. Floating UI over text and controls is No. 1 on the owner's slop list.
  F: Add the swap row ('.tm__alt' or its equivalent) to KEEP_CLEAR in TodayCue, or start the cue already folded to the 40 px circle when it would overlap the card. Never draw the 2.4 s label over card content.
  I: t01-today-new-free-390-night.png (y 1420-1520)
  Files: src/components/today/TodayCue.jsx:17 (KEEP_CLEAR)
  EV: CONFIRMED: I opened t01-today-new-free-390-night.png and t01-today-new-free-390-day.png. In the night shot, the "Your week and road" pill (about y 1418-1500, x 210-570 at 2x) sits on the swap row. It cuts "Tap one to swap it in as..." off at "Tap one to s". It also sits directly above the "A full mock" and "Start with" cards, which are already half-faded under the bottom nav. In the day shot the pill is folded to the circle with a chevron, about x 340-440. It still sits on the same row and hides the middle of the sentence, leaving "Tap one to swap it in as" and "ve" on either side. So the overlap shows in both themes, and in the full-label state the loss is worse. Neither R3-SPEC.md nor R2-S
[owner-eye#6] refuted 0 of 1 | medium | Free after the day's session: Learn home, refusal, Free ends
[owner-eye#7] SURVIVES 1 of 1 | medium | Practice page, phone (LK24, LK30)
  P: About 330 px of dead black band sits before "Your papers". The "Timed, marked +5/-1…" card above it ends with square, cut-off bottom corners and looks broken. This was already in round 2 (p3/80-practice-full-390-night.png), so X5's 'reserve the bar's height at the end' landed mid-page. The Pro page is still about 13 screens long, and the Free page adds a Pro banner plus a second Pro block. This is the clutter LK24 is about.
  F: Put the sticky bar's reserved space at the true end of the scroll area. Fix the summary card's radius/overflow. Fold the 'Timed, marked…' copy into the Quick practice card. On Free, keep one Pro mention, not two.
  I: p01-practice-pro-full-390-night.png (y 3150-3800); p02-practice-free-full-390-night.png
  Files: Practice dashboard components
  EV: CONFIRMED: I opened p01-practice-pro-full-390-night.png and p02-practice-free-full-390-night.png myself and the problem is there on both. The "Timed, marked +5 / -1, saved to your record" card has rounded top corners but a flat, square-cornered bottom edge with a visible border line. Below it is an empty black band before the "Your papers" card. On Pro the band is about 345 px in the 2x image, roughly 170 CSS px. The finding's "about 330 px" is image pixels, not CSS pixels, so the size is slightly overstated but the band is real. On Free it is about 130 to 170 CSS px. R3-SPEC X5 says to reserve the sticky Fine-tune bar's height "at the end of the scroll area". Here the reserved space sits mi
[owner-eye#8] refuted 0 of 1 | medium | Run question after a wrong answer, phone
[owner-eye#9] SURVIVES 1 of 1 | medium | Learn home and chapter page counts (LK11 clarity)
  P: Learn home's main offer says "9 due cards first, then new ones here", and the first Or row is again "Revise 9 due cards · 2 min". The student can't tell if Start already does that. On the chapter page the mistakes pile reads "2 of 3 · Your mistakes", while the list below says "Fix 3 open mistakes · 3 min" for the same chapter.
  F: When the offer already leads with due cards, drop the line or the Revise row (keep one). Make the pile show the count it will play, with the same number as the row, or say "2 fit in 10 min".
  I: l02-learn-home-returning-pro-390-night.png; c02-chapter-returning-pro-full-390-night.png
  Files: src/components/learn2/home/homeModel.mjs; src/components/learn2/chapter/**
  EV: CONFIRMED: Both mismatches are visible in the screenshots, and no spec ruling makes either one intended.

Learn home (l02-learn-home-returning-pro-390-night.png): the offer says "9 due cards first, then new ones here" and has a "Start · 10 min" key. The first Or row, directly under it, is "Revise 9 due cards · 2 min". A student can't tell whether Start already covers the due cards. The code does mean Start to include them: data/tests/learn_roadmap.test.mjs:95 asserts the line '2 due cards first, then new ones here'. So the Revise row repeats what the offer line says Start does. R3-SPEC R3 only says the Revise row appears when due > 0; it doesn't say to keep both. Nothing rules this overlap i
[owner-eye#10] SURVIVES 1 of 1 | medium | Explore chapter covers (LK21, unbranded)
  P: The covers now show the chapter's first card text on a flat dark panel. The first cover is a fill-in-the-blank with "'____'" placeholders that read like a broken template. There is no chapter-specific visual, and the only image left is the Accountancy object beside the picker. It solves 'same logo everywhere' by removing art, which looks cheap next to the owner-loved direction. Below "For you" sits a large empty gap.
  F: Use a short card front, never a cloze, as the cover line. Add one chapter motif per cover (from the brand illustration set or a generated chapter object). Tighten the empty middle of the card.
  I: x01-explore-top-390-night.png; x01-explore-top-1440-night.png
  Files: Explore page covers
  EV: CONFIRMED: PARTLY CONFIRMED, with the finding's strongest claim refuted by the spec. I opened x01-explore-top-390-night.png and x01-explore-top-1440-night.png.

CONFIRMED, cloze cover. Chapter 1's cover text reads "Persons who have entered into partnership with one another are individually called '____' and collectively called '____'." It sits on a flat dark panel at both widths. A student who hasn't opened the chapter sees an unfinished sentence as the headline. The other three covers at 1440 are clean questions ("What does the Profit and Loss Appropriation Account show?", "What is the gaining ratio?", "What is goodwill?"). The cloze is therefore the one cover that reads as a broken templat
[owner-eye#11] SURVIVES 1 of 1 | medium | Saved and Explore single questions (LK24 clutter)
  P: Each saved question carries three bordered buttons: a full-width lime-outline "Practise this chapter", "Try it again" and "Remove". Two saved items fill the whole screen with button walls. Singles repeat an "Answer it" + "Save" pair on every row. This is the repeated action trio from the slop list.
  F: Make the row itself open the question (tap the stem). Keep one quiet text action (Remove) and move "Practise this chapter" to a single key per chapter group.
  I: x03-saved-390-night.png; x02-explore-singles-390-night.png
  Files: Saved page, DiscoveryFeed.jsx
  EV: CONFIRMED: I opened x03-saved-390-night.png and x02-explore-singles-390-night.png. The finding holds for Saved and is only partly right for Explore.

Saved (x03): each of the 2 saved items carries three bordered buttons. These are a full-width lime-outline "Practise this chapter", then "Try it again" and "Remove" side by side. The stem is plain text, not tappable. Two items fill the 390x844 screen with button rows, and the rows are about as tall as the stems.

Explore singles (x02): each card has a right-aligned "Answer it" and "Save" pair. That is a pair, not a trio, and the buttons are small. It is repetitive across the cards but mild. The finding overstates this half.

Spec check: R3-SPEC
[owner-eye#12] SURVIVES 1 of 1 | medium | Explore singles / Saved: wrong chapter label
  P: "Goodwill brought in by an incoming partner is shared by old partners in:" is labelled "Accounting for Partnership: Basic Concepts". It is an Admission of a Partner (or Goodwill) question, so a student filtering by chapter gets the wrong content.
  F: Re-map this question's chapter tag at the source, and add a check that question stems mentioning 'incoming partner' or 'admission' are not tagged Basic Concepts.
  I: x02-explore-singles-390-night.png; x03-saved-390-night.png
  Files: question chapter mapping / preview fixture
  EV: CONFIRMED: I can see the mislabel in both cited screenshots. In x02-explore-singles-390-night.png, the first card reads "Accounting for Partnership: Basic Concepts / Easy / Goodwill brought in by an incoming partner is shared by old partners in:". The third card, "On admission of a new partner...", is labelled "Admission of a Partner". The x03-saved-390-night.png header for the same question is also "Accounting for Partnership: Basic Concepts", which fits R3 X3 (canonical syllabus titles). The label is wrong against the app's own syllabus. In data/cuet_syllabus.js, "Partnership Fundamentals" maps to Basic Concepts, which sits under the unit "Accounting for Partnership" alongside the Profit &
[owner-eye#13] refuted 0 of 1 | medium | Today, brand-new student: goal counters
[owner-eye#14] SURVIVES 1 of 1 | medium | End screens: card-fan minis
  P: text-wrap: balance on the narrow, rotated minis leaves orphan first words on their own line ("A / partnership / firm has n…", "The / sacrifice by / a partner."). Clamping cuts mid-word ("features o…"). It looks broken at the focal point of the end screen.
  F: Use text-wrap: pretty (not balance) on minis, a smaller mini font so 3 lines fit about 18 characters each, and truncate at a word boundary.
  I: r07-run-end-stopped-390-night.png; f07-feed-end-390-night.png; f05-feed-checkpoint-390-night.png; r06-run-end-390-night.png
  Files: src/components/learn2/stage/** (fan minis)
  EV: CONFIRMED: I opened all four cited screenshots and the defect is visible in each. r07-run-end-stopped-390-night shows "A" alone on the first line, then "partnership", then "firm has n…", so the first word is orphaned and the clamp cuts "n…" mid-word. f07-feed-end-390-night shows "The" alone on a line, then "sacrifice by", then "a partner." f05-feed-checkpoint-390-night shows the same "The / sacrifice by / a partner." in the smaller two-card fan. r06-run-end-390-night shows "Name the / 6 essential / features o…", with the same mid-word cut at "o…". The spec does not rule this behaviour as intended. R3-SPEC L6 (line 135) asks for `text-wrap: balance`, a 3-line clamp with an ellipsis, and no mi
[owner-eye#15] LOW-unchecked  | low | Run question hint
  P: "Pick the answer you think is right." shows on question 5 for a returning student who has answered questions before ("You missed this in Mock 3"). W says it shows once, on the first question a student ever sees.
  F: Gate the hint on a per-student 'seen first question' flag, not per run.
  I: r03-run-question-390-night.png; r03-run-question-1440-night.png
  Files: src/components/learn2/run/**
  EV: 
[owner-eye#16] LOW-unchecked  | low | Run and feed end consistency
  P: The labels and chrome differ between the two ends. The feed end says "3 in Revise" while the run end says "14 in Revise, back Wed" (L5 requires the same labels). The run end's phone X has no label, while the feed end shows "X Close".
  F: Share one end-numbers component and one close control for run and feed.
  I: r06-run-end-390-night.png vs f07-feed-end-390-night.png
  Files: src/components/learn2/stage/**
  EV: 
[owner-eye#17] LOW-unchecked  | low | Learn home roadmap 'Start here' pill, phone
  P: At 390 the lime "Start here" pill has a blurred glow halo. The desktop pill is crisp (l01-1440-night). Glow is on the owner's slop list.
  F: Remove the box-shadow/filter glow on the phone pill, and match desktop.
  I: l01-learn-home-fresh-free-390-night.png (y 1490-1530)
  Files: src/components/learn2/home/learn-home.css
  EV: 
[owner-eye#18] LOW-unchecked  | low | Desktop run rail pile label
  P: The rail shows "In Revise 4" with a stacked label and number. L4 specifies the visible label "4 to revise" (pileLabel). The rail also stacks four count rows (Key cards 4 of 14, 2 questions, 2 open mistakes, In Revise), which is busy for a side rail.
  F: Use pileLabel. Drop the rows that repeat the progress bar.
  I: r03-run-question-1440-night.png (x 205-310, y 540-585)
  Files: src/components/learn2/run/** (top bar / rail)
  EV: 

##### LENS ui-correctness | Ship after fixes. Night and Day hold at 390 and 1440, and the console is clean, l2=off included. But Free roadmap rows now say a chapter has "5 cards", and chapter, card and due counts disagree between Learn, Explore, Practice and the Free screens. Both would mislead a student.
[ui-correctness#1] SURVIVES 3 of 3 | blocker | Learn home roadmap (Free), all states
  P: This is a regression from round 2. R2 rows read "5 free cards"; R3 dropped "free" but kept the Free count, so every Free row now says the chapter itself has "5 cards" (Goodwill "5 cards", Share Capital "5 cards"). The same chapters show "45 cards. 5 open on Free." on the chapter page, "of 52 cards seen" on the feed end, and 39-106 cards for Pro. On the Free-done home the first row reads "5 of 5 cards seen" with a full bar, so the chapter looks finished. The library looks tiny (against LK34) and students are told they have done everything.
  F: Free rows show the real chapter size ("45 cards · 10 questions"), the same as Pro. Keep "5 free in each chapter" once in the header (R5). Progress on Free reads against the real total ("5 of 45 cards seen"). Add a copy test that a Free row's card count equals the chapter total.
  I: l01-learn-home-fresh-free-full-390-night.png, l01-learn-home-fresh-free-1440-day.png, l04-learn-home-free-done-390-day.png; compare r2-merged/extra/86-learn-home-fresh-free-1440-night.png, c01-chapter-fresh-free-full-390-night.png, f08-feed-end-free-390-day.png
  Files: src/components/learn2/home/** (roadmap row), data/learn/roadmap.js
  EV: CONFIRMED: Confirmed from the screenshots and the code. In l01-learn-home-fresh-free-full-390-night.png the Free roadmap rows read "5 cards · 1 question", "5 cards" (Goodwill), "5 cards" (Share Capital) and "5 cards · 10 questions". The chapter page c01-chapter-fresh-free-390-night.png shows the Key cards pile as 5 with the same chapter reading as a 45-card chapter elsewhere. In l04-learn-home-free-done-390-day.png the first row reads "5 of 5 cards seen · 3 of 10 questions tried", so the chapter looks finished on Free. The header line "5 free in each chapter" is present and correct (R5), but the rows contradict it by calling 5 the chapter's size.

Cause in code. ChapterMap.jsx line 54 calls 
[ui-correctness#2] SURVIVES 2 of 2 | high | Practice (Free and Pro), Fine-tune and Your papers
  P: Practice says Accountancy has "all 5 chapters" ("Questions from all 5 chapters", "Chapters All 5"), while Learn, Explore and the chapter page say 14. Your papers names the chapter "Partnership Fundamentals", which is not a syllabus title (C2 and T5/X3 canonical titles).
  F: Practice's chapter picker and the Your papers line read the same playable, canonical chapter list that Learn uses (14, "Accounting for Partnership: Basic Concepts"). Map the old 5-chapter question taxonomy onto the syllabus chapters.
  I: p02-practice-free-full-1440-day.png, p01-practice-pro-full-1440-night.png, p02-practice-free-full-390-day.png
  Files: Practice dashboard components (R3-explore), chapter mapping source
  EV: CONFIRMED: I saw it in the screenshots. p02-practice-free-full-1440-day.png shows the Fine-tune card with "Chapters ... All 5" and "Questions from all 5 chapters.". The sticky summary card shows "Chapters All 5". p01-practice-pro-full-1440-night.png shows the same two lines. In the p02 Your papers card, the line reads "Partnership Fundamentals: 6 wrong of 10 answered." On the Learn home (l01-learn-home-fresh-free-1440-day.png) the Accountancy tab says "14 chapters · 866 Key cards · 4 lessons". The offer says "Chapter 1 of 14 · Accounting for Partnership: Basic Concepts". The roadmap lists that canonical title and the other syllabus titles, none called "Partnership Fundamentals". So one subje
[ui-correctness#3] refuted 0 of 2 | high | Explore chapter feed covers
[ui-correctness#4] SURVIVES 2 of 2 | high | Explore single questions and Saved
  P: "Goodwill brought in by an incoming partner is shared by old partners in:" is labelled "Accounting for Partnership: Basic Concepts". It belongs to Admission of a Partner / Goodwill. It is the first single question, and on Saved its "Practise this chapter" key sends the student to the wrong chapter. The old taxonomy ("Partnership Fundamentals") is the likely cause.
  F: Re-map the question's chapter (and its 5-chapter-to-14-chapter mapping) to the syllabus chapter. Prefer singles whose mapping is exact. Add a check that the singles' chapter labels match their stems' syllabus topic.
  I: x02-explore-singles-1440-day.png, x01-explore-full-390-night.png, x03-saved-390-night.png, x04-explore-l2off-390-night.png
  Files: Explore singles source / question chapter map
  EV: CONFIRMED: I saw the problem in three of the four cited images. I did not open x04 or check the Practise link target.

- x02-explore-singles-1440-day.png: the first single question, "Goodwill brought in by an incoming partner is shared by old partners in:", is labelled "Accounting for Partnership: Basic Concepts". The other two cards are labelled correctly: "Goodwill: Nature and Valuation" and "Admission of a Partner". A goodwill-sharing stem under Basic Concepts is plainly the wrong chapter for a student.
- x01-explore-full-390-night.png: the same mislabelled card is first in the list at 390 wide.
- x03-saved-390-night.png: the same question again carries the Basic Concepts label. Its lime 
[ui-correctness#5] SURVIVES 2 of 2 | high | Explore feed, a question item (390)
  P: A floating pill "Options below" with a down chevron sits over the next item's peek card. All four options are already fully visible above it, so the cue is false. It covers the peek's type label ("Fact") and breaks L3 (the peek must be a clean card edge).
  F: Show "Options below" only when the options group is actually below the fold, and place it inside the stage, never on the peek strip. Otherwise render nothing there and keep the peek's type label.
  I: f03-feed-later-item-no-chip-390-night.png, f03-feed-later-item-no-chip-390-day.png
  Files: src/components/learn2/feed/**
  EV: CONFIRMED: I opened f03-feed-later-item-no-chip-390-night.png and the day version. In both, question 2 of 12 ("Admission of a Partner") shows all four options A to D in full, with D ending near y=1350 of 1688. A pill reading "Options below" with a down chevron sits just under D, centred over the next item's peek strip. The peek's "Fact" label is visible at the left edge of that strip. The pill covers the middle of the strip and sits on its top border. The cue is false because every option is already on screen. L3 in R3-SPEC.md says the peek is a real card edge with the next item's type label inside, and that the only chip allowed in that strip is the first-visit Mobi swipe cue. This is a dif
[ui-correctness#6] SURVIVES 1 of 2 | high | Free after the day's session: Learn home vs feed refusal
  P: F rules that both screens show the same block, but the due rows disagree: Learn home says "Revise 8 due cards · 2 min" and the refusal says "Revise 3 due cards · 1 min". If this is the same student, C1's single due source is not used by the refusal screen.
  F: Have the refusal screen read due.all from the C1 server function. If the capture used two fixtures, align them and re-shoot so the screens can be compared.
  I: l04-learn-home-free-done-390-day.png vs f09-feed-free-refused-390-night.png
  Files: feed refusal screen (R3-run), learn.js due function
  EV: REFUTED: The numbers differ (l04 shows "Revise 8 due cards · 2 min", f09 shows "Revise 3 due cards · 1 min"), but they are not the same student and not the same scope, so the finding's premise fails.

1. Different fixtures. In wt-1101-r2-hero/scripts/design-audit/learn-1101-r3-merged-capture.mjs, every shot gets its own `env.kcs` (`r3m-${shot.id}-...`). l04 comes from the 'home-free-done' shot: a fresh kcs, `useFreeSession`, then the Learn home for Accountancy. f09 comes from the 'feed-free-end' shot, a different kcs. That shot first runs `feedWalk` through the whole AOP chapter feed on that same kcs. The walk opens cards and keeps or revises them, which can lower the due count. It then open
[ui-correctness#7] SURVIVES 1 of 1 | medium | Run, wrong answer (390)
  P: After a wrong answer the stage scrolls so the stem's first line ("When the partners' capital accounts") and the context line ("You missed this in Mock 3 on 16 Oct") go under the top bar. The student sees a question that starts mid-sentence ("are fixed, on which side of which…").
  F: When the feedback opens, keep the stem in view: scroll only far enough to show "Not quite" and the line, or collapse the line card. Never clip the stem under the bar.
  I: r04-run-wrong-line-390-day.png, r04-run-wrong-line-390-night.png, r05-run-stop-sheet-390-day.png
  Files: src/components/learn2/run/**
  EV: CONFIRMED: I opened r04-run-wrong-line-390-day.png, r04-run-wrong-line-390-night.png and r05-run-stop-sheet-390-day.png, and the problem is there in all three. Under the chapter line ("Accounting for Partnership: Basic Concepts") the stem begins mid-sentence at "are fixed, on which side of which", with a fade over that line. The text before it ("When the partners' capital accounts") is not visible. The context line "You missed this in Mock 3 on 16 Oct" is not visible either. The student sees "…account are the drawings recorded?", and the question is missing its subject and its condition, which are the parts needed to answer it. Night and Day look the same. R3-SPEC L2 says only that when the 
[ui-correctness#8] SURVIVES 1 of 1 | medium | Today, Weak chapters and Last paper (returning Pro)
  P: Ruling W bans "missed" as a count of mistakes, but Today shows "6 of 10 missed", "5 of 9 missed", "3 of 7 missed" and "5 of your 20 misses (4 wrong, 1 blank)". T5 asks for canonical titles, but the third weak chapter is "Ratios" (the roadmap says "Accounting Ratios").
  F: Use canonical titles from the roadmap source. Reword the counts, for example "6 of 10 wrong or blank" or "6 open mistakes", in line with W.
  I: t02-today-returning-pro-full-390-night.png
  Files: Today components, todayReads.js
  EV: CONFIRMED: The finding holds. In t02-today-returning-pro-full-390-night.png the Weak chapters rows read "6 of 10 missed", "5 of 9 missed" and "3 of 7 missed". The Last paper block reads "5 of your 20 misses (4 wrong, 1 blank)". R3-SPEC Ruling W (section "W. Words: one word for each thing, everywhere") sets the question-mistakes term as "open mistakes". Its "Never" column bans "missed" as a count of mistakes. The ruling says "everywhere" and the spec does not exempt Today, so these strings are not intended. T5 requires canonical syllabus titles. The third weak-chapter row shows "Ratios", but the repo's canonical data (artifacts/study-suite/coverage.json and data/calibration_manifest.json) use
[ui-correctness#9] refuted 0 of 1 | medium | Run, stop sheet vs stopped end
[ui-correctness#10] refuted 0 of 1 | medium | Today, brand-new Free (390)
[ui-correctness#11] refuted 0 of 1 | medium | Shell sidebar on tall desktop pages
[ui-correctness#12] refuted 0 of 1 | medium | Run, wrong answer line
[ui-correctness#13] SURVIVES 1 of 1 | medium | Chapter numbering across Learn, Explore, chapter page and feed
  P: Learn says "Chapter 1 of 14", but Explore covers and chapter pages use the NCERT number. "Part 1, Ch 2" appears on Change in PSR, Goodwill and Admission (the 3rd to 5th chapters on the roadmap). The feed's desktop panel reverses the order ("Ch 2, Part 1, Partnership Accounts"). A student cannot match the numbers.
  F: Use one label, "Part 1 · Chapter 5 of 14", or drop "Ch N" where it clashes. One order everywhere.
  I: l07-sidebar-explore-1440-night.png, c03-chapter-resume-1440-day.png, f04-feed-card-front-1440-night.png, l02-learn-home-returning-pro-1440-night.png
  Files: chapter label helper (shared)
  EV: CONFIRMED: I opened the four cited screenshots. Explore (l07, 1440 night) labels the first four chapter covers "Part 1, Ch 1", "Part 1, Ch 1", "Part 1, Ch 2" and "Part 1, Ch 2", so two different chapters share each number. The chapter page for Admission of a Partner (c03, 1440 day) reads "Part 1, Ch 2". The Learn home roadmap (l02) lists the same chapters in order as Basic Concepts, P&L Appropriation, Change in PSR, Goodwill, and the offer line reads "Chapter 1 of 14 · Accounting for Partnership: Basic Concepts". That "Chapter N of 14" is a roadmap position out of 14 playable chapters. R3-SPEC R2 keeps it ("Chapter 1 of 14") and C2 defines the 14 as the playable-chapter count, so it is a pos
[ui-correctness#14] SURVIVES 1 of 1 | medium | Run, desktop side panel pile
  P: The desktop pile reads "In Revise 4" with a card icon. L4 asks for the visible label "4 to revise" (pileLabel), and W reserves "In Revise" for a card's server-confirmed state.
  F: Render pileLabel("4 to revise") with the card-stack icon and aria-label "4 cards to revise later". Show it only when the count is at least 1.
  I: r03-run-question-1440-night.png
  Files: src/components/learn2/stage/**
  EV: CONFIRMED: Seen directly in r03-run-question-1440-night.png. The left session panel shows a card-stack glyph with the small label "In Revise" and a large "4" under it. It does not read "4 to revise". R3-SPEC L4 (line 110) says the desktop pile (>=1024) is one card-stack icon with the visible label "4 to revise" (pileLabel) and aria-label "4 cards to revise later", shown only at 1 or more. R3-SPEC line 30 reserves "In Revise" for a card's server-confirmed state, and line 112 repeats that. In code, SessionPanel in src/components/learn2/run/RunParts.jsx (lines 128-133) hardcodes `<p className="lr-panel__rl">In Revise</p>` with the bare count `{pile}`. It never calls pileLabel and has no aria-la
[ui-correctness#15] LOW-unchecked  | low | Today, brand-new student week row
  P: The Today cell shows the rest-day dot (legend: "Dot: a rest day") while the hero says Day 1 and "Start now". The page tells a new student that today is both a rest day and day 1.
  F: For a student with no history, mark today as the planned first day (an empty ring or a dash), never as a rest day.
  I: t01-today-new-free-1440-night.png, t01-today-new-free-full-390-day.png
  Files: Today week strip
  EV: 
[ui-correctness#16] LOW-unchecked  | low | End screens, run vs feed
  P: L5 wants the same labels on both ends, but the feed end says "3 in Revise" and the run end says "14 in Revise, back Wed". The feed end also has an "X Close" label while the run end at 390 shows a bare X.
  F: Use the same numbers row component and the same close control on both ends.
  I: f07-feed-end-390-night.png vs r06-run-end-390-night.png
  Files: src/components/learn2/run/**, feed/**
  EV: 
[ui-correctness#17] LOW-unchecked  | low | Practice, Free (390)
  P: About 170 px of blank space sits mid-page between the summary card and Your papers (owner LK30: too much blank). The separate summary card ("Timed, marked +5 / -1…") is still there although X5 says to merge it into the sticky bar. In the full shot the sticky bar sits on top of the questions-count picker.
  F: Reserve the sticky bar's height only at the end of the scroll area. Merge the summary into the bar. Check that the count picker is never covered at 390x844.
  I: p02-practice-free-full-390-day.png
  Files: Practice dashboard components
  EV: 
[ui-correctness#18] LOW-unchecked  | low | Stop sheet vs end keys
  P: "Keep going" means two things: closing the stop sheet to continue this run, and on the ends starting a new 10 minutes ("Keep going · 10 min"). That breaks W's one word per thing.
  F: Label the sheet's quiet key "Back to it" or "Not now". Keep "Keep going · 10 min" for the end key only.
  I: r05-run-stop-sheet-390-day.png, f06-feed-stop-sheet-390-day.png vs r06-run-end-390-night.png, f07-feed-end-390-night.png
  Files: run/** and feed/** sheets
  EV: 
[ui-correctness#19] LOW-unchecked  | low | Chapter page, desktop resume
  P: "7-minute lesson, not read yet" breaks the W time format (" · N min").
  F: Write "Lesson · 7 min, not read yet" using withMinutes.
  I: c03-chapter-resume-1440-day.png
  Files: src/components/learn2/chapter/**
  EV: 
[ui-correctness#20] LOW-unchecked  | low | Run, Key card back
  P: On the back the source line ("NCERT, Accountancy Part 1, Ch 2, p. 48") sits under the answer text instead of pinned to the card's bottom, as on the front (L1). The answer block also leaves a big empty band above it.
  F: Pin the source line to the card's bottom on both faces, and centre the back's text block in the space between the label and the source line.
  I: r02-run-card-turned-390-day.png
  Files: src/components/learn2/stage/**
  EV: 

##### LENS first-timer | Ship after fixes. A first-time Free student can find and start Learn: the offer, the chapter page, the feed cue and the Free-done wording are clear and kind. Three things still mislead or look broken. The Free roadmap shows every chapter as "5 cards". Key cards give two different chapter numbers for the same NCERT chapter. On a brand-new student's first Today screen, a floating cue covers the alternatives.
[first-timer#1] SURVIVES 2 of 2 | high | Learn home roadmap and subject line (Free)
  P: On Free, every roadmap row reads "5 cards": Goodwill, Admission, Share Capital and so on. The same page's desktop tab line says "866 Key cards", the chapter page says "45 cards. 5 open on Free.", and Pro sees 39, 52 or 106 cards. A student reads the chapters as tiny and never learns that most of the content exists. The header "5 free in each chapter" doesn't say 5 of what. The Free limit is told inconsistently and makes the product look smaller than it is.
  F: Rows show the real chapter size ("45 cards · 10 questions"), as R5 asks for unstarted rows. Make the header say "5 Key cards free in each chapter". Keep the row count from row.cards, not progress.of (homeModel.mjs freeEach/roadmapRow).
  I: l01-learn-home-fresh-free-full-390-day.png, l01-learn-home-fresh-free-1440-night.png, l04-learn-home-free-done-full-390-night.png vs l02-learn-home-returning-pro-full-390-night.png and c01-chapter-fresh-free-full-390-night.png
  Files: src/components/learn2/home/homeModel.mjs, ChapterMap.jsx
  EV: CONFIRMED: I saw it in two screenshots. In l01-learn-home-fresh-free-full-390-day.png, every Free roadmap row reads "5 cards" (Goodwill, Admission of a Partner, Share Capital, Accounting Ratios, Cash Flow). Two rows add "· 7 questions" or "· 10 questions". The header says only "5 free in each chapter". In c01-chapter-fresh-free-full-390-night.png the same chapter says "45 cards. 5 open on Free." and "10 questions in this chapter", so the home row and the chapter page disagree. R3-SPEC R5 says unstarted rows show "45 cards · 10 questions" with no bar. The same spec says the "5 free in each chapter" line goes once in the header, never on rows. R6 gives the tab line as "866 Key cards". The Free
[first-timer#2] SURVIVES 2 of 2 | high | Key card and wrong-answer source lines
  P: Cards from the same chapter (Accounting for Partnership: Basic Concepts) cite two different NCERT chapters. data/keycards/decks/accountancy.json mixes code leac102/chapterNo 2/p.48 (def-partnership, about line 16650) with leac101/chapterNo 1/p.7 (about line 17786). The app calls the chapter "Ch 1". A student who opens the book to check "Ch 2, p. 48" lands in a different chapter. A wrong citation erodes trust in every card.
  F: Normalise each chapterKey's source.chapterNo and page to one book edition (the rationalised NCERT that the chapter page numbering uses). Add a deck test that all cards in one chapterKey share a chapterNo.
  I: r02-run-card-turned-390-night.png ("NCERT, Accountancy Part 1, Ch 2, p. 48") vs r04-run-wrong-line-390-day.png ("NCERT, Accountancy Part 1, Ch 1, p. 7") vs c01 header "Part 1, Ch 1"
  Files: data/keycards/decks/accountancy.json
  EV: CONFIRMED: The defect is real but narrower than described. In data/keycards/decks/accountancy.json, chapterKey accountancy.partnership-fundamentals (shown in the app as "Accounting for Partnership: Basic Concepts") has 45 cards. 44 cite code leac101, chapterNo 1, with pages 2 to 7 and 35 to 36. Exactly one card, kc.accountancy.partnership-fundamentals.def-partnership, cites code leac102, chapterNo 2, page 48, section "Introduction". I confirmed both citations on screen. r02-run-card-turned-390-night.png shows "NCERT, Accountancy Part 1, Ch 2, p. 48" as card 1 of 18 in that chapter. r04-run-wrong-line-390-day.png shows "NCERT, Accountancy Part 1, Ch 1, p. 7" in the same chapter. Neither R2-SP
[first-timer#3] SURVIVES 2 of 2 | high | Today, brand-new Free student, first screen
  P: The floating "Your week and road" cue (folded to a chevron circle in Day) sits on top of the coach line "Tap one to swap it in as your move" and the alternatives "A full mock" / "Start with…". The dock clips them too. The line reads "Tap one to s… ve", so the only cue that explains the alternatives is hidden, and the first screen looks broken. "Your move" and "road" are also unclear words for a new student.
  F: Anchor the TodayCue below the start card (or hide it while the alternatives row is in view), and keep the alternatives row clear of the dock. Reword the coach line, for example "Or start with one of these".
  I: t01-today-new-free-390-day.png, t01-today-new-free-full-390-night.png
  Files: src/components/today/TodayCue.jsx, TodayMove.jsx:276, today.css:286
  EV: CONFIRMED: I can see the problem myself in t01-today-new-free-390-day.png. At scroll 0 on 390x844, the 44px glass chevron circle sits at y~1455 (2x) on the coach line, so the line reads "Tap one to swap it in as [circle] ve". The alternatives row ("A full mock" / "Start with…") is faded and half under the dock. In t01-today-new-free-full-390-night.png the wide "Your week and road" pill (still in its first 2.4 s) sits in the same place and cuts the line to "Tap one to s". I checked the code. TodayCue is position:fixed, centred, 92px above the bottom (today.css ~L289). It steps away only for `.tm__key` and `.tm__why` (KEEP_CLEAR in TodayCue.jsx), after a 24px scroll, or once the week is seen. 
[first-timer#4] SURVIVES 1 of 1 | medium | Free run end
  P: The bar reads "5 of 45 cards seen", but this Free student has now seen all 5 free cards in the chapter. Nothing says the other 40 are Pro, so the student comes back tomorrow expecting new cards and finds none. The chapter page says it ("5 open on Free"); the end screen hides it.
  F: On Free, when seen = the free count, label the bar "5 of 45 cards seen · the rest open with Pro" (one line, no extra block). Or have the quiet See Pro link carry that reason.
  I: r08-run-end-free-390-night.png
  Files: src/components/learn2/run/** end screen
  EV: CONFIRMED: I opened r08-run-end-free-390-night.png and saw the gap myself. The bar label reads "5 of 45 cards seen" with a 5/45 sliver of progress. The only Free copy is "That was today's free session. Questions come back tomorrow." Under it sit the "Quick recap · 1 min" key and a quiet "See Pro" link. Nothing on the screen says the other 40 cards are Pro-only, so a student could read the bar as 40 cards still to come. The spec does not rule this as intended. R3-SPEC section F and L5 only prescribe the bar label ("20 of 45 cards seen") and the Free line plus keys. They say nothing about what the bar means once a Free student has seen all 5 open cards. So this is an unspecified gap, not a rul
[first-timer#5] refuted 0 of 1 | medium | Feed refused (Free) and Learn home Free-done
[first-timer#6] SURVIVES 1 of 1 | medium | Free-done due count
  P: Two screens of the same Free-after-session state show different due counts. If this is not only two fixtures, the student sees the number change between screens (C1, one source).
  F: Make the refusal screen read due.all from the same server function as /api/learn/home. Capture both from one fixture to confirm.
  I: l04-learn-home-free-done-390-night.png ("Revise 8 due cards · 2 min") vs f09-feed-free-refused-390-night.png ("Revise 3 due cards · 1 min")
  Files: src/lib/server/learn.js, feed refusal component
  EV: CONFIRMED: I opened both images. l04-learn-home-free-done-390-night.png shows "Revise 8 due cards · 2 min". f09-feed-free-refused-390-night.png shows "Revise 3 due cards · 1 min". The two screens are not just two fixtures. The cause is in the code.

- The Learn home row comes from data/learn/roadmap.js. It uses every due card of the subject (dueSorted, reviseDue.count).
- The feed refusal is built by sessionUsed() in src/lib/server/learn.js (about line 505). It uses info.counts.due and info.dueIds, which are for a single chapter, and the run it starts is limited to that chapter's key.
- The capture scripts show the f09 screen was opened on chapter C1 (accountancy.partnership-fundamentals) af
[first-timer#7] SURVIVES 1 of 1 | medium | Learn home Or rows
  P: "Start chapter 1 · 10 min" and "Play this chapter as a feed — One card or question at a time" sound the same: the chapter run is also one card or question at a time. A new student can't tell why they would pick the feed.
  F: Give the feed row a line that says what's different, for example "Swipe through cards and questions, no time set". Keep it to one line.
  I: l01-learn-home-fresh-free-390-night.png
  Files: src/components/learn2/home/**
  EV: CONFIRMED: In l01-learn-home-fresh-free-390-night.png the two rows read "Start chapter 1 · 10 min" and "Play this chapter as a feed / One card or question at a time". The run key card is itself one card or question at a time, so the feed row's only line does not say what is different. The specs name the row ("Play this chapter as a feed", R3 ruling R3 item 3, R2 "Or" rows) but give no subline, so this copy is not a spec-ruled behaviour. The line comes from an earlier API-contract draft ("One card or question at a time, 10 minutes"). A new student has no reason to choose the feed over the main key. This is a copy problem, not a layout bug. FIX: Change the feed row's line to one that names the
[first-timer#8] SURVIVES 1 of 1 | medium | Roadmap Part 2 option
  P: "Part 2 has two options. Pick the one your school teaches." sits over two identical outlined pills, with neither shown as picked. The list below silently shows the Analysis of Financial Statements chapters and "Chapter 1 of 14" counts them. A Computerised Accounting student doesn't know whether they are seeing their own syllabus.
  F: Until a choice is saved, add the line "Showing Analysis of Financial Statements until you pick". Once one is chosen, show it filled (aria-checked already exists; style the checked state).
  I: l01-learn-home-fresh-free-full-390-day.png (crop around y 2560-3020), l01-learn-home-fresh-free-1440-night.png
  Files: src/components/learn2/home/ChapterMap.jsx PartSwitch, learn-home.css .lh-opt__btn
  EV: CONFIRMED: I saw the problem in both cited screenshots. In l01-learn-home-fresh-free-full-390-day.png (around y 2560-3020 in original pixels), the line "Part 2 has two options. Pick the one your school teaches." sits over two identical outlined pills, "Analysis of Financial Statements" and "Computerised Accounting". Neither is filled or marked. Directly below, the list shows "Company Accounts..." and then an "Analysis of Financial Statements" group with Financial Statements of a Company, Ratios, Cash Flow and so on. Nothing says that is a default. The 1440 night image shows the same: two outlined pills, neither picked, and the Analysis chapters listed beneath. A Computerised Accounting stude
[first-timer#9] refuted 0 of 1 | medium | Run, wrong answer
[first-timer#10] SURVIVES 1 of 1 | medium | Explore singles and Saved (preview fixture)
  P: "Goodwill brought in by an incoming partner…" is labelled "Accounting for Partnership: Basic Concepts" (it is Admission/Goodwill), and Saved's "Practise this chapter" would send the student to the wrong chapter. It comes from previewFixtures.js:14 (chapter 'Partnership Fundamentals' mapped to Basic Concepts), but the owner judges the preview.
  F: Tag the fixture to Admission of a Partner (or Goodwill), and confirm that the real bank's chapter mapping for 'Partnership Fundamentals' rows is canonical.
  I: x02-explore-singles-390-day.png, x03-saved-390-day.png
  Files: src/app/preview/arena/previewFixtures.js:14, ArenaPreviewClient.jsx:81
  EV: CONFIRMED: I can see the problem in both cited screenshots, and the cause is as described. The fixture is the cause, and the real chapter mapping is correct.

- x02-explore-singles-390-day.png: the first single-question card has the header "Accounting for Partnership: Basic Concepts". Its body is "Goodwill brought in by an incoming partner is shared by old partners in:". The third card, "Admission of a Partner", is a separate chapter.
- x03-saved-390-day.png: the same question is saved with the same Basic Concepts label. Its "Practise this chapter" button would open Partnership Fundamentals, which is the wrong chapter for a goodwill or admission question.
- Cause: `src/app/preview/arena/prev
[first-timer#11] refuted 0 of 1 | medium | Key card rating keys
[first-timer#12] LOW-unchecked  | low | Run question hint
  P: "Pick the answer you think is right." shows on question 5 of a returning student who has mock history ("You missed this in Mock 3"). Ruling W says once, on the first question a student ever sees. It also sits below Skip at the very bottom, so it is read last.
  F: Gate it on the student's first-ever question (any surface), and place it above the options.
  I: r03-run-question-390-night.png
  Files: src/components/learn2/run/**
  EV: 
[first-timer#13] LOW-unchecked  | low | Roadmap verdict
  P: "Needs work" appears on Financial Statements of a Company, which has no cards seen and no questions tried in Learn. The student doesn't know where the verdict comes from.
  F: When the evidence is from papers, say so ("Needs work · from your papers"), or show the verdict only once Learn activity exists in that chapter.
  I: l04-learn-home-free-done-full-390-night.png, l02-learn-home-returning-pro-full-390-night.png
  Files: src/components/learn2/home/homeModel.mjs roadmapRow
  EV: 
[first-timer#14] LOW-unchecked  | low | Practice (Free)
  P: "Partnership Fundamentals: 6 wrong of 10 answered." uses the internal deck name, not the canonical title "Accounting for Partnership: Basic Concepts". A tall empty band (about 250 px) also follows the credits card before Your papers (LK30).
  F: Map chapter names through the canonical syllabus titles and remove the extra bottom spacing on that card.
  I: p02-practice-free-full-390-night.png
  Files: src/app/(app)/dashboard/DashboardPageClient.jsx
  EV: 
[first-timer#15] LOW-unchecked  | low | Today copy, brand-new student
  P: "This week" next to "4 study days this week" repeats itself. "Dot: a rest day. Dash: before your first session." is a legend a new student has to decode. "This set uses 10 credits. You have 108." appears with credits never explained.
  F: Header "This week" with the count "4 study days". Drop or simplify the legend. Credits: add one tap-to-explain, for example "What are credits?".
  I: t01-today-new-free-full-390-night.png
  Files: src/components/today/**
  EV: 
[first-timer#16] LOW-unchecked  | low | Saved page
  P: Each saved question carries three keys (a full-width "Practise this chapter", "Try it again" and "Remove"). On a phone this is cluttered (LK24), and "Try it again" is odd for a question never answered.
  F: Make the whole question open it to answer. Keep one quiet "Practise this chapter" link, and move Remove into a menu or a swipe.
  I: x03-saved-390-day.png
  Files: Saved page component
  EV: 
[first-timer#17] LOW-unchecked  | low | Run vs feed close control
  P: Feed screens show "X Close"; run screens show a bare X. The same action looks different between two parts of the same Learn flow.
  F: Use one treatment (X with the label "Close" is clearer for new users) on run, feed, ends and refusal.
  I: r08-run-end-free-390-night.png vs f08-feed-end-free-390-day.png and f09-feed-free-refused-390-night.png
  Files: src/components/learn2/run/**, feed/**
  EV: 

##### LENS server-security | Ship after fixes. I found no IDOR: every run read, resume, end, answer and rate is scoped by user_id, and a foreign run id gives 404 or a new run of the caller's own. I found no way past Free's one counted session either, because the answer-time claim check holds. Two high-severity problems remain. First, Free can be shown a "Continue" key that the server then refuses with a 402 in the middle of the run. Second, with a part option set, the one due count (C1) overcounts and disagrees with the run it starts and with the Key cards service. test:learn passes 316/316; the scenarios below are from a scratch node test, now removed from the repo.
[server-security#1] SURVIVES 2 of 2 | high | Run/feed end (stopped) and Learn home pickup, Free
  P: Free's session is claimed on the first answered question, not at the start. Reproduced: a Free student starts a mix, rates 1 card and taps Stop. The session is still unclaimed (sessionDone false), so the stopped end offers 'Continue · 10 min' plus 'Fix 2 open mistakes · 2 min'. The fix key now starts a NEW run (fresh), and its first answer claims the day for that run. Afterwards the end's main key, Learn home's pickup key ('Continue · 10 min', which resumes run A because roadmap pickup ignores who holds the session) and the suggestions pickup all reopen run A. Its first question returns 402 FREE_SESSION_USED, and RunPlayer ends the run. The student was offered a key the server refuses. The same happens with a feed stopped before its first answer. Before R3 the fix key resumed A, so this path was not reachable.
  F: On Free, treat an unfinished counted run of today as the pending holder. (a) In endOptions' stopped branch, drop the fix key when !isPro and isCounted(stopped.kind), even if S.session is null; or make the fix key resume nothing and refuse with the sessionUsed block. (b) In subjectBody/roadmap, when freeDone and runOut.id !== S.session.reference and runOut is counted, do not offer it as 'Continue'; offer the holder (freeRun) instead, or label the run cards only. Add a route test: Free stop after one card, take the fix key and answer, then every Continue the server offers must answer 200 on its first question.
  I: data/learn/suggest.js:271; src/lib/server/learn.js:1232; data/learn/roadmap.js:157; src/lib/server/learn.js:637-646
  Files: data/learn/suggest.js, src/lib/server/learn.js, data/learn/roadmap.js, data/tests/learn_routes.test.mjs
  EV: CONFIRMED: I traced this in wt-1031-learn-v2 at 98e03e8cb and the finding holds.

1. **The session is claimed on the first answer, not at the start.** In src/lib/server/learn.js around lines 1005-1048, the answer handler sends `quota: counted ? { kind: 'learn_session', ... }` to `store.recordEvent`. It returns `used()` (402 FREE_SESSION_USED) when `A.session && A.session.reference !== row.id`. Rating a card spends no quota, so a mix stopped after one rated card leaves `S.session` null.

2. **The stopped end offers both keys.** At learn.js:1232, `sessionDone = !S.isPro && Boolean(S.session)` is false. In data/learn/suggest.js:271, the stopped branch returns `options: fix && !freeSessionUsed ?
[server-security#2] SURVIVES 2 of 2 | high | Learn home Revise row, sidebar dot, /api/learn/home and /api/learn/shelves due (C1), part options
  P: dueNow and dueSummary count every due state in the subject without applying the student's part option (syllabus.sectionAllowed), and retired chapters are counted too. The roadmap's cardIds come only from allowed chapters. Reproduced with computer_science, option B2, and 6 due cards each in a B1 chapter and a B2 chapter. Pro sees 'Revise 12 due cards · 3 min', and the run serves 6 cards. home.due.all and shelves.due.all are both 12, while kc.dueCount (used by R15 overdue, Revise and Today) is 6. Free sees 'Revise 10 due cards · 2 min' and gets 5 cards. home and shelves agree with each other, but both are wrong for the student and contradict the Key cards service. The E2 test ('all equals kc.dueCount') still passes only because its fixture has no options.
  F: In dueNow and in each subject of dueSummary, keep only states whose chapter is allowed: syllabus.chapterByKey(state.chapter_key) not retired, and sectionAllowed(subject, section, option). Read options once from S.options for the other subjects. Take reviseRow's count from the same filtered list that supplies its cardIds. Add an options fixture to the C1 test and assert due.all === kc.dueCount and revise label count === cardIds.length.
  I: src/lib/server/learn.js:1503-1527; src/lib/server/learn.js:685; data/learn/roadmap.js:140-152
  Files: src/lib/server/learn.js, data/learn/roadmap.js, data/tests/learn_r3_home.test.mjs
  EV: CONFIRMED: At HEAD 98e03e8cb, dueNow (src/lib/server/learn.js:1503-1508) keeps a state when it is not suspended, S.isOpen(card_id) is true and S.pub.byId has the card. It never checks S.option or syllabus.sectionAllowed. S.isOpen (line 194) is `me.isPro || S.taste.has(id)`, so for Pro it is always true, and S.taste comes from tasteIds(S.cards) over the whole subject. dueSummary (lines 1517-1527) counts the other subjects the same way, with no options check. Learn home passes reviseDue: dueNow(S) at line 685 for the Revise label count and minutes. The `due` list that supplies cardIds is built at line 669 from `allowed`, which line 635 filters with syllabus.sectionAllowed(sid, i.section, S.opt
[server-security#3] SURVIVES 1 of 1 | medium | start() resume branch: same make check (C2-1)
  P: The make check compares only whether 'cards' is left out. A mistakes-only start (questions, cards and lesson left out) therefore still resumes a stopped questions-only run (cards and lesson left out), and the reverse also holds. Reproduced on Pro: stop a questions-only run of Planning after 1 answer. Home's or row 'Fix 1 open mistake · 1 min' (roadmap fixRow, sent without fresh) resumes that run and serves 1 mistake plus 7 new chapter questions. The key promised 1 minute of mistakes.
  F: Compare the full make: the sorted leave_out sets must be equal, or at least both 'cards' and 'questions'. Better still, give roadmap fixRow (and the suggestions fix action) fresh: true, as the end's fix key has. Add a test: stop a questions-only run, then home's fix row returns a new run whose items are all origin 'mistake'.
  I: src/lib/server/learn.js:834
  Files: src/lib/server/learn.js, data/learn/roadmap.js, data/learn/suggest.js
  EV: CONFIRMED: The finding holds. Lines 831-834 of src/lib/server/learn.js work out `cardsOut = cleanLeaveOut(body?.leaveOut).includes('cards')`. They then resume any same-day, unfinished run of the same kind and chapter where `(r.leave_out || []).includes('cards') === cardsOut`. No other pile is compared.

Two starts both pass that test:
- **Home's fix row:** data/learn/roadmap.js:134 builds `run: { chapterKey, minutes: m, leaveOut: ['questions','cards','lesson'], kind: 'mix' }`. It sends no `fresh` (only the end's lead at learn.js:1319 sends fresh: true).
- **The chapter page's questions-only start:** ChapterPage.jsx:330-333 builds `only('questions')`, which gives leaveOut ['cards','mistakes',
[server-security#4] SURVIVES 1 of 1 | medium | Free-done block: feed refusal (402) vs Learn home
  P: Ruling F says the feed refusal and Learn home's Free-done state show the same block. The refusal's 'Revise N due cards · M min' counts only the refused chapter (info.counts.due and info.dueIds). Home's row counts the whole subject (dueNow). One student at the same moment sees, for example, 'Revise 2 due cards · 1 min' on the refusal and 'Revise 9 due cards · 3 min' on home.
  F: Build the refusal's Revise option from the same subject-wide source as home: the filtered dueNow list, oldest first, capped at maxCardIds. Or factor roadmap's reviseRow into a helper that both call.
  I: src/lib/server/learn.js:510-512; src/lib/server/learn.js:685
  Files: src/lib/server/learn.js, data/learn/roadmap.js
  EV: CONFIRMED: I confirmed the problem in the code. The feed refusal comes from startRun at learn.js:839-843, where `info = chapterInfo(S, key)` is the chapter the student tapped. sessionUsed (learn.js:507-516) builds the Revise option only from `info.counts.due` and `info.dueIds`, so it covers that one chapter. Learn home's roadmap (learn.js:685) takes `reviseDue: dueNow(S)` (learn.js:1503-1508), which counts every live due card in the subject. The comment there (C1) says this is the same count the shelves and the due badge show.

The snapshot at line 824 already covers the whole subject (`key.split('.')[0]`), so dueNow(S) could be called at the refusal too. It isn't. Ruling F in R3-SPEC says "
[server-security#5] LOW-unchecked  | low | GET /api/learn/runs/:id/end?stop=1 on an ended run
  P: finished does not check row.ended_at. A stop end read after the run was ended (a retry via onRetry with stoppedAt, a second tab) answers stopped: true with 'Continue · 6 min' (resume: the ended run). The explicit resume rejects an ended run and falls through to a fresh composition, so 'Continue' starts a NEW full run. Reproduced. On Free's used day that new run is a 402 for a feed, or a cards-only run for a mix.
  F: Set finished = Boolean(row.ended_at) || !stop || recap || done >= item_count, so an ended run never gets the stopped keys.
  I: src/lib/server/learn.js:1218; src/lib/server/learn.js:1242; src/lib/server/learn.js:1265
  Files: src/lib/server/learn.js
  EV: 
[server-security#6] LOW-unchecked  | low | End of a stopped level run
  P: A level run stopped with ?stop=1 is not ended, and the body says stopped: true. But endOptions receives stopped: null for level, so the keys are Keep going / Next chapter, or 'Start with X', with no Continue. The UI draws the stopped layout ('5 of 6 done') without a way back, and the run stays open (answerable) for 48 h.
  F: For level, either end the run on stop (treat it as finished) or report stopped: false. Keep the body's stopped and the keys' stopped from the same expression.
  I: src/lib/server/learn.js:1242; src/lib/server/learn.js:1265
  Files: src/lib/server/learn.js
  EV: 
[server-security#7] LOW-unchecked  | low | Learn home Revise row, Pro with more than 100 due cards
  P: The count and minutes cover every due card ('Revise 150 due cards · 40 min'), but cardIds are capped at LEARN_RULES.maxCardIds (100), so the run serves 100 cards in about 27 min. The label overstates the run.
  F: When dueSorted was truncated, say the run's own count and minutes (min(count, 100), with minutes summed over the sliced list), or label it as the first 100.
  I: data/learn/roadmap.js:140-152
  Files: data/learn/roadmap.js
  EV: 

##### LENS client-code | Ship after fixes. The round-3 client code mostly waits for the server before it confirms anything and handles focus well, but the end keys now start runs without changing the address. A reload or Back after "Keep going", "Fix N open mistakes" or "Continue" can put a student in a different run or back on the old end screen. Today's new-student fix also moves the start card on load.
[client-code#1] SURVIVES 2 of 2 | high | Run and feed end screens: in-place Keep going, Next chapter, Fix N open mistakes, Continue, Quick recap
  P: End keys that start a chapter run now call onStart, which runs setParams and begin(), and the feed's Continue calls resumeFeed(). Neither updates the URL; there is no router.replace anywhere in RunPlayer, and Player reads its params from the URL only once. Example: a student stops, then taps "Fix 3 open mistakes" and gets a new fresh run, but the address still holds the original start URL (kind=mix, no fresh). A reload starts a mix, and the server's resume branch puts them back in the stopped run, which is the C2-1 confusion the spec set out to fix. Another case: a run opened from ?run=<id>&end=1, then "Keep going" in place, then a reload shows the old end screen again. Android often reloads a backgrounded tab on low-RAM phones, so students will hit this.
  F: When params change, router.replace the run URL to match the new run: once the server returns the run, rewrite to ?run=<newId> (plus chapter and kind), and drop end=1 and fresh. Do the same in the feed after adopt() in resumeFeed and again10. Add a test that the URL after onStart names the new run id.
  I: src/components/learn2/run/RunPlayer.jsx:619-623; src/components/learn2/run/RunEnd.jsx:69,73; src/components/learn2/feed/ChapterFeed.jsx:338-344,594
  Files: src/components/learn2/run/RunPlayer.jsx, src/components/learn2/run/RunEnd.jsx, src/components/learn2/feed/ChapterFeed.jsx
  EV: CONFIRMED: The RunPlayer half holds up. At 98e03e8cb, Player (RunPlayer.jsx:166-173) builds its params once in a useState initializer from its props and useSearchParams (fresh, next). The end screen's onStart (lines 619-623) only calls setParams({... runId: r.resume || null, fresh: Boolean(r.fresh), openEnd: false}), which runs begin(), and the recapEnd "Study these N" key does the same (line 634). RunPlayer contains no router.replace, history.replaceState or other URL write; the only router calls are push for the lesson and for close. RunEnd.keyTarget (RunEnd.jsx:21-29) sends every non-feed option to { run }, so onStart handles it in place (lines 69 and 73). After "Keep going", "Next chapte
[client-code#2] SURVIVES 1 of 1 | medium | Today, brand-new student at 390 (T3)
  P: dayOne is everSessions === 0, and everSessions is null until facts or rhythm load. While loading, the strip, as its .tcs--wait skeleton, renders straight into the header on phones, above the start card. When the facts arrive with 0 sessions, that strip is unmounted and a new one mounts below the start card. On the exact first screen T3 targets, the start card jumps up after landing, which is visible layout shift. For dayOne it also mounts two TodayCollegesStrip instances, one hidden by CSS, each with its own useCollegeCutoffs read.
  F: While everSessions is unknown, put nothing in the header on phones; for example, gate the header strip on everSessions !== null && !dayOne, or reserve the strip only in the 1100 px header. Then render one strip and place it with CSS order or a single slot instead of two mounted copies.
  I: src/app/(app)/today/page.jsx:150,297,308,325
  Files: src/app/(app)/today/page.jsx, src/components/today/today.css
  EV: CONFIRMED: The finding holds at 98e03e8cb. In page.jsx, line 250 sets everSessions to null until facts.sessions or rhythm.counts.sessions arrives, and line 297 sets dayOne = everSessions === 0, so dayOne is false while those reads load. Line 308 then renders the bare <TodayCollegesStrip> in the header. While it is held (hold=landing), TodayCollegesStrip.jsx:18 draws the .tcs--wait skeleton. No phone CSS hides a bare .tcs in the header; only .today__colleges-head is display:none below 1100 px (today.css:26). So on a 390 px phone the skeleton sits above the start card.

When the reads land with 0 sessions, dayOne turns true. Line 308 swaps to the <div className="today__colleges-head"> wrapper,
[client-code#3] SURVIVES 1 of 1 | medium | Explore single questions (X1)
  P: pickSingles re-chooses the first 3, preferring distinct chapters, from the whole question pool every time a page is appended. Example: page 1's eligible questions come from chapters A, A, B, so the first 3 are A1, B1, A2. After "More questions" (or the automatic top-up), page 2 brings C1, and the list re-picks as A1, B1, C1, A2. The question the student may have just answered moves down a slot under their thumb, and every card below shifts.
  F: Keep the order stable once questions are shown: compute the 3 distinct-chapter picks only for the first fill, then only append new eligible questions after the ones already shown, for example by remembering the shown ids in a ref and ordering by first-shown.
  I: src/components/feed/DiscoveryFeed.jsx:155-165,199-200; src/components/feed/exploreModel.mjs:56-68
  Files: src/components/feed/DiscoveryFeed.jsx, src/components/feed/exploreModel.mjs
  EV: CONFIRMED: I traced the code and the reported problem is real.

- **Pages are merged into one list.** In `src/components/feed/DiscoveryFeed.jsx:119`, `loadPage` adds each new page to the existing questions with `appendUniqueQuestions(current.questions, data.questions)`.
- **The picks are recomputed over that whole list.** `singles = useMemo(() => pickSingles(page.questions, ...))` at line 155 reruns every time `page.questions` changes.
- **The visible list is a slice of the recomputed result.** At line 199, `list = singles.slice(0, shown)`.
- **How `pickSingles` orders questions** (`exploreModel.mjs:56-68`): it walks every eligible question and fills the first `FIRST_SHOWN` (3) slots with on
[client-code#4] SURVIVES 1 of 1 | medium | Run top bar, desktop Revise-later pile (L4)
  P: The visible "4 to revise" is aria-hidden, and the spec's aria-label "4 cards to revise later" is placed on a <p>. A paragraph has no role that takes a name, so most screen readers ignore that aria-label. At 1024 px and up, a screen-reader user hears nothing about the pile. Stage.jsx's KeptCount does this correctly with role="img".
  F: Give the pile role="img" (or put the words in a visually hidden span) the same way KeptCount does in Stage.jsx:221.
  I: src/components/learn2/run/RunParts.jsx:80-83
  Files: src/components/learn2/run/RunParts.jsx
  EV: CONFIRMED: At 98e03e8cb, RunParts.jsx:80-83 (TopBar) renders the pile as `<p className="lr-top__pile" aria-label={pile ? `${pile} cards to revise later` : undefined}>`. It has no role. Everything inside it is hidden from screen readers. PileGlyph (RunParts.jsx:28) is a span with aria-hidden="true", and the visible `<b>` holding pileLabel ("4 to revise") also has aria-hidden="true". The only other child is the 1.6 s "In Revise" tip with role="status", and it appears only when the count goes from 0 to 1. A `<p>` has the paragraph role, and ARIA 1.2 does not allow an author-given name on that role. NVDA, JAWS and VoiceOver usually ignore aria-label on a plain p, so the paragraph is read as empt
[client-code#5] refuted 0 of 1 | medium | Learn home SubjectPicker sheet: focus trap and viewport change
[client-code#6] LOW-unchecked  | low | Learn home SubjectPicker sheet: keyboard model
  P: The <ul> is given role="radiogroup" with <li> children, and every row is a role="radio" button in the Tab order. Arrow keys do nothing, and Tab steps through all subjects. That does not match the radio pattern screen readers announce. ARIA also does not allow a radiogroup to own listitems.
  F: Either drop the radio roles and use plain buttons with aria-current or aria-pressed in a list, or implement a roving tabindex with Up and Down arrows and role="none" on the <li>.
  I: src/components/learn2/home/SubjectPicker.jsx:52-55
  Files: src/components/learn2/home/SubjectPicker.jsx
  EV: 
[client-code#7] LOW-unchecked  | low | Learn home SubjectPicker scrim (L7 motion)
  P: The sheet is portalled to <body>, but --lh-ease is defined only on .lh. The scrim's animation, `lh-fade 200ms var(--lh-ease) both`, references an undefined variable, so the whole declaration is invalid at computed-value time. The scrim pops in with no 200 ms fade, while the panel's literal cubic-bezier still animates.
  F: Use var(--mm-ease-out, cubic-bezier(0.23, 1, 0.32, 1)) directly in .lh-psheet__scrim, or define --lh-ease on .lh-psheet.
  I: src/components/learn2/home/learn-home.css:10,351
  Files: src/components/learn2/home/learn-home.css
  EV: 
[client-code#8] LOW-unchecked  | low | Explore top-up counter (X1)
  P: topUps is a ref that resets only when a page fills (singles.length >= shown) or when "More" is tapped. Suppose a subject's pages are mostly out of syllabus, so 5 top-ups run and give up. The student then switches subject or chapter. The counter stays at 5, so the new filter never auto-tops-up and can show 1 or 2 questions, or the "No ready questions on this page" empty state, while more pages exist.
  F: Reset topUps.current = 0 whenever filters.subject, filters.chapter or filters.difficulty change, or when loadPage is called with reset.
  I: src/components/feed/DiscoveryFeed.jsx:158-165
  Files: src/components/feed/DiscoveryFeed.jsx
  EV: 
[client-code#9] LOW-unchecked  | low | Practice dashboard for Pro: Start card and sticky bar (X5)
  P: For Pro, costLabel is 'Checking' while the quote loads and '' once it is ready. The Cost row draws, then disappears, and the card shrinks. The bar's text works the same way: barCost falls back to modeBadge(...).text || 'Checking', which shows "· Checking" and then drops the separator and the text. Pro students see the late content shift on every subject or mode change.
  F: For isPremium, never draw the Cost row or the bar's cost slot, including while loading (check isPremium before quoteStatus), so the layout matches the final state from the first paint.
  I: src/app/(app)/dashboard/DashboardPageClient.jsx:764,821 (barCost about 487)
  Files: src/app/(app)/dashboard/DashboardPageClient.jsx
  EV: 
[client-code#10] LOW-unchecked  | low | Run start race (begin without a stale guard)
  P: Now that end keys start runs in place, begin(params) runs more often, and it has no cancellation. If two begins overlap (onStart from the end, then "Try again" or a quick second key while the first startRun is slow), whichever response lands last wins. setRun and setItems can then show run B's items while run A was the one started last. On Free that orphans a counted run on the server.
  F: Keep a request token in a ref and ignore responses whose token is no longer current. Also disable the end keys (aria-busy) from tap until the new run loads.
  I: src/components/learn2/run/RunPlayer.jsx:219-259
  Files: src/components/learn2/run/RunPlayer.jsx
  EV: 
[client-code#11] LOW-unchecked  | low | Run top bar "In Revise" tip
  P: The 1.6 s tip is a role="status" span mounted together with its text, inside .lr-top__pile, which is display:none below 1024 px. Phones never see or hear it. On desktop, a live region inserted with its content already present is often not announced.
  F: Announce the first Revise through the player's existing polite live region (setAnnounce) and keep the visual tip for desktop only.
  I: src/components/learn2/run/RunParts.jsx:65-72,83; src/components/learn2/run/run.css:30
  Files: src/components/learn2/run/RunParts.jsx, src/components/learn2/run/run.css
  EV: 
[client-code#12] LOW-unchecked  | low | Study stage motion with the in-app reduced-motion setting
  P: The new feed chip bob (3 iterations), the peek cap's fade and the kept-count pop are switched off only under @media (prefers-reduced-motion). The app's own html[data-motion='reduced'] setting, which run.css:522-523 and nav-badge.css honour, is not checked. A student who chose reduced motion in the app still sees the chip bob.
  F: Mirror the reduced-motion block under html[data-motion='reduced'] .st ... in stage.css.
  I: src/components/learn2/stage/stage.css:553-565 (new .st-cue bob, .st-cap and .st-kept animations at 167-172)
  Files: src/components/learn2/stage/stage.css
  EV: ```
