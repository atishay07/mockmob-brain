# Owner feedback, 13 October 2026, about 11:10 AM (verbatim)

Context: he used the app on his Vivo. Note that two apps were installed: the real app (signed out, onboarding only) and a demo build (`test/device_demo`, signed in as "Asha" with canned test data). Some bugs below come from the demo's canned data; the requirements stand regardless.

> From the things that I have noticed, the onboarding flow as such looks fine. I would not say it's more than 60% right now.
>
> One thing is the UI in general: the bottom navbar is very fluent and snappy right now, but the UI choices that you have made, like putting the green-by-green dot snapping in, are good. They require a lot of finish right now. They are working, but that finish is still not there.
>
> Some spacing, like on the first page only: 2 days, move accountancy, 3 mistakes. There is a book there, but the spacing overall can be improved. The road to make all these features can also be improved a bit.
>
> The subject icons are good, but around C, it makes a bit of sense. I don't know if everyone makes as much sense. Will you be able to map these for all the subjects is the question.
>
> The exam day layout needs to be changed. It's called the NTA mode, and all the features that we have on the website have to be there. Overall, the UI choices that you have in general, in some places like these dots depicted to show stuff, look cool for sure, but how useful are they is the question. I'm not saying to remove it, but thinking through these kinds of things and integrating the repos also, maybe with this.
>
> I think other things are also left, like subject: there is no option to edit subject, I think. Then there are these milestones. That thing should be improved. Weekly, some things require a bit more thinking over. Every feature is not thought through enough, and there's a major bug in whatever account you have signed in with. You might have tested a paper, and 10 questions were attempted: 7 out of 10, 2 were wrong, and 1 was not attempted.
>
> Whenever I am trying to start a quick practice of 5 questions, I am able to start a new practice. It's just loading the score. What is this? Even after we finish it, there's no such animation or something we talked about. Even when I'm starting from business studies or anything else, it's just redirecting me to the accounting page and all.
>
> Overall, the UI is also not as good as what we have on the website for this section. I would not say that this is 60% work done. This is like a good base, which we have to work upon a lot, not even a little. This is not a complete app. We wanted this to be an extension of the website, having more than it. It doesn't even have all those things, and the things which it even has require a lot of finesse. Some are straight up buggy, which require multiple passes to fix. Not multiple passes: you can fix it in one pass, but from the speed you are going through, I doubt it. We really need to pick up the pace with everything.
>
> Also, while onboarding and in some places, I was noticing that, in general, there is no animation in the images that you generated. Maybe the NR mascot also should be there in the app clearly, and it should have the animation and all. Either you can do it by SVG, creating a very extremely high-quality SVG, or by rendering its graphics, or by generating video. Generating a video animation for every single thing is not really feasible, so let me know how you want to do it.
>
> We want it to act like the Duolingo kind of thing: the Duo mascot of Duolingo, how it is animated everywhere, and also the onboarding. While onboarding, I was noticing that many pictures were just pasted there, just to be there. On the first page itself, there's an AI-generated picture that doesn't look good at all. There should be either some animation by the mascot saying hi or something else, but not just an AI-generated random picture.

## What this means (orchestrator's reading)

1. **Mobi becomes a living, animated character everywhere** (Duolingo's Duo is the reference): a code-rigged vector Mobi (layered parts: folded-diamond body, visor, eyes, antenna, arms, boots) animated in Flutter with a state machine (idle breathing, blink, look, wave hello, talk, cheer, think, point, sleepy, sad or oops, celebrate), reacting to events. The 3D renders may remain only where a still is clearly better; the welcome photo goes.
2. **No pasted AI pictures.** Welcome opens with Mobi saying hi. Every image must earn its place; prefer Mobi and purposeful code-drawn visuals.
3. **NTA mode** (the exam-day layout) must have every feature the website's NTA mode has.
4. **Website parity and beyond.** The app is an extension of mockmob.in with more than it. Every student-facing website feature must exist in the app (or be deliberately linked), with better finish.
5. **Practice must be correct and satisfying:** the chosen subject and length are honoured; finishing a practice gets a real moment (animation, Mobi, the result).
6. **Finish everywhere:** spacing (Today first screen), the road to May, milestones, weekly rhythm, edit subjects, every bubble or dot motif justified by usefulness or removed.
7. **Subject art for every subject** offered, not five.
8. **Pace.** One decisive pass with parallel builders, not slow loops.
