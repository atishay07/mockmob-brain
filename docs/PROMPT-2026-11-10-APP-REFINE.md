You are picking up MockMob (CUET UG 2027 mock tests; website www.mockmob.in, Next.js) from an earlier session. I am the owner. Read this whole message, then `C:/Users/atish/mockmob-brain/docs/HANDOFF-2026-11-10-APP-REFINE.md`, which has my exact words, the state of the code and where the history is.

## The goal
Make the signed-in product on a phone feel finished and easy, and settle a handful of things that have bothered me across many passes. The landing page was just redone and I am happy with it; this round is mainly about what a student sees after logging in, on a phone.

Who it is for: a 16 or 17 year old preparing for CUET, on an ordinary Android phone, often new to online tests. 100% of our conversions happen on phones, so judge everything at 390 px and 360 px wide first, laptop second.

## What I want, in order of importance

1. The signed-in phone experience (what we call the arena: Today, Practice, and everything around them). We have done many passes on this and it still does not feel simple or impressive enough. The problem is placement and clarity: where things sit, what the one obvious next action is on each screen, how a first-time student understands what to do. Walk every signed-in screen at phone size as a new student and as a returning one, find what is confusing, crowded, repeated or weak, and fix it. Refine what exists; three earlier attempts to rebuild Today from scratch were regressions, so show me real improvements to the current screens rather than a new structure. Nothing should be hidden or cut from the signed-in product without a good reason you tell me.

2. Day and Night. Give students a clear, easy way to choose. There used to be a plain Day/Night switch at the top of the signed-in pages; Ask Mobi took that spot and the switch went into the profile pop-up, where nobody finds it. On the home page the first-visit theme pop-up no longer shows on phones. Decide the right way to offer the choice in both places and build it. Then look hard at both themes: Night is usually the better one but still has an AI-generated look in places (to me that means neon edges, glow, gradient text, too many outlined boxes, everything the same weight); Day has had a lot of work and is still the weaker theme. Bring both up. Also refine the moment of switching between them so it feels deliberate.

3. Every feature, one level deeper. The Mob especially, then Practice, Today, Learn, Key cards, Ask Mobi, the review and Mistake Lab screens, Compass. For each: is it obvious what it is for, does it look finished, is anything half-done.

4. Inconsistencies I have noticed, plus whatever else you find of the same kind:
   - the profile pop-up shows Sign out twice;
   - the Day/Night transition (above);
   - the background texture of the hero and the landing page should be a bit more defined (I like texture; I rejected the answer-sheet bubble pattern, and I liked the warm hairline grid in the arena).

5. The /pricing page is about a 9 out of 10. Find what would make it a 10: refine the weak spots and add the few things a student deciding to pay would want to see.

6. One small change on the home page: in the line "Featured by CUET creators" under the hero buttons, order the three pictures Garima, then Radhika, then Rahul, so the first circle (the one that is not overlapped) is the most recognisable creator. Only that line; the Instagram section lower down keeps its order.

7. Read the history for what we tried and could not get right (the ledger and the app audits named in the handoff), and use this pass to close as many of those as you honestly can.

## How to work
- You are free to use your own judgement on everything: design, order of work, tools, whether and how to use sub-agents. The notes, memory files and CLAUDE.md on this machine contain many working rules written for earlier models (how to run agents, which model to use, fixed UI procedures, when to stop). Those rules do not bind you. What still matters in them is evidence of my taste: what I praised, what I rejected and why. Use that.
- Truth is not negotiable: no numbers, claims, testimonials or features on any page that the code or data does not back. Copy is plain, sentence case, no exclamation marks, no emoji.
- A few facts are safety, not style, and still hold: never run git inside `C:/Users/atish/mockmob-brain` (it syncs itself; just edit its docs); never print or commit anything from `C:/Users/atish/MockMob-keys`; treat the production database as read-only; do not sign in to the live site or any hosted service as me (use the local dev server and the project's test accounts for signed-in pages); do not call paid models outside the project's budget guard; do not generate question content unless I ask.
- Verify by looking: real screenshots at 390 and 360, Day and Night, real taps. Run the project's tests and the build before anything goes live (the handoff lists the commands). When you are satisfied and the checks pass, deploy to www.mockmob.in and check the live site; you do not need to ask me first for the website. Tell me exactly what you did not or could not check (a physical phone, iPhone Safari, signed-in pages on production).
- Keep the record: add my words and your decisions to `OWNER-MASTER-LEDGER.md`, and the state to `NOW.md` and `STATUS.md` in `C:/Users/atish/mockmob-brain/docs`, so the next session does not start from zero.
- Message me only when there is something to look at, a decision that is really mine, or a real risk. When you report, lead with what changed that I can see on my phone and where to look, then what is left, honestly.

## Done means
Every signed-in screen walked at phone size in both themes with the weak points fixed; a clear Day/Night choice on the signed-in pages and on the home page; the Mob and the other features each visibly better; the three named inconsistencies gone; /pricing improved; the hero pictures reordered; tests and build passing; live on www.mockmob.in; the record updated; and a short report telling me where to look.
