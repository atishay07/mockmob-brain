# Team

Who works on MockMob, and who has the final say on what. Agents read this at the start of every session.

| Person | Role | Final say on |
|---|---|---|
| Atishay | Founder (owner) | Product, design, copy, what ships to students, priorities, budgets, paid AI runs, content generation |
| CTO (name added at install) | CTO | Architecture, code, reviews, deploys, database, security, the agent workflow |

## How disagreements are settled

- **Inside one area,** the newest decision by the person who owns that area wins.
- **Across areas,** agents never settle it themselves. They raise it with the owner of the area that is affected, in a handover or in the chat.
- **Anything a student sees** needs Atishay's OK, even when the change is technical.
- **Product decisions by Atishay** stand until he changes them. The ledger (`docs/OWNER-MASTER-LEDGER.md`) records them.

## Who edits what in this brain

- **`handoffs/`:** everyone adds new handovers. Nobody edits someone else's.
- **`docs/`:** everyone. In `docs/NOW.md`, update your own section; add a `## <your name>` section if it is missing. In the ledger, add entries rather than rewriting old ones.
- **`context/`:** copied automatically from Atishay's private brain. Don't edit it here, because the next copy overwrites it. Propose a change in a handover instead.
- **`playbook/memory/<person>/`:** copied automatically from each person's Claude memory. Each person's folder is theirs.
- **`claims/`:** written by the tools. Each person's folder is theirs.

## Permissions

Permissions recorded in `context/` (paid runs, production database work, deploys) were given to Atishay's own agents. They apply to other people's agents only if they are listed here.

Permissions that apply to everyone's agents:
- None yet.
