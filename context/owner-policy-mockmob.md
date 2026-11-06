# MockMob: the owner's standing answers for agents (approved 13 Oct 2026)

Source: Atishay's answers on 13 Oct 2026, about 21:15 IST (decisions/log.md, "Owner proxy"). Jarvis may answer an agent from these rules without disturbing the owner, and reports what it answered afterwards. Anything these rules don't clearly cover goes to the owner.

## Agents may do these without asking
1. **Tests, lint and local builds:** for example npm test, npm run lint, npm run build, flutter test and flutter analyze. Local only.
2. **Push feature branches:** any branch other than main. Never force-push, never push to main.
3. **Staging Supabase SQL:** on the staging project only. Never on production.
4. **Continue an approved plan:** "Shall I continue?" when the owner already approved that plan, and the next step stays inside it.

## Always the owner's (an agent asks; Jarvis never answers these from rules)
- **Push to main, or any production deploy:** a spoken yes each time, or a bedtime grant with a condition and an end time. Either one becomes a one-time permission rule.
- **Production SQL, migrations, data changes:** the owner runs them. Jarvis opens the page and copies the SQL.
- **Hosted sign-in, OTPs, passwords, secrets** (e.g. Vercel or Supabase keys): the owner only. Agents and Jarvis never handle them.
- **Deleting files or data, spending money, publishing, sending messages.**
- **Anything the auto-mode safety check blocked:** Jarvis reports it and never routes around it.
