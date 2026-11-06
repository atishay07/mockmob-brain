# MockMob team brain

The shared memory for everyone building MockMob and for every agent they run: project docs, decisions, owner feedback, handovers between sessions, team lessons and who is working on what.

Each person keeps a copy on their own computer, and agents search that copy locally, so it's as fast as a brain that lives on one PC. Syncing with GitHub is automatic:

- **Session start:** the latest changes are pulled in before the agent starts.
- **During a session:** new handovers from teammates arrive in the background, at most every 5 minutes.
- **Writing:** every handover, note or claim the agent writes is shared within seconds.
- **Offline:** you keep working on your copy, and everything is shared at the next sync.

Nobody runs git here by hand.

## Install (once per computer, about 10 minutes)

1. Accept the GitHub invite to `atishay07/mockmob-brain`.
2. Install Git and Python 3.10 or newer:
   - **Windows:** Git for Windows (it includes Git Credential Manager, which signs you in through the browser) and Python from python.org.
   - **Mac:** `brew install git python gh`, then `gh auth login` and `gh auth setup-git`, so git signs in through the browser.
3. Clone the repo into your home folder:
   ```bash
   git clone https://github.com/atishay07/mockmob-brain.git ~/mockmob-brain
   ```
4. Run the installer and answer its questions (name, role, email, where your MockMob code checkout is):
   ```bash
   python ~/mockmob-brain/.brain/install.py
   ```
   It sets up search, connects Claude Code (and Codex, if you use it), runs a self-test and prints a summary.
5. Restart Claude Code. Open it in your MockMob code folder and ask: *"What's the current state of MockMob?"*

## How it works

- **Agents:** Claude Code and Codex get the same tools on every machine: `continuum_start`, `continuum_search`, `continuum_read`, `continuum_checkpoint` and `rag_search`. Agent instructions are therefore the same for everyone.
- **Search:** keyword plus meaning search over a local index (`~/.mockmob-brain/index`). The index refreshes itself after every pull, so a teammate's handover is searchable seconds after it arrives.
- **No clashes:**
  - Every handover is its own new file, so two people can never overwrite each other.
  - Edits to shared docs merge line by line.
  - If two edits truly clash, both versions are kept (the second goes in `conflicts/`) and the next agent is asked to tidy up.
- **Privacy:** the sync only shares the folders listed in `.brain/DESIGN.md`. It refuses files that look like they hold a key, token or password, files over 2 MB, and binaries. Your own Claude memory is copied into `playbook/memory/<you>/`, except entries marked as personal (`type: user`).

## Troubleshooting

| What you see | What to do |
|---|---|
| Packet says "sign-in needed" | `python ~/mockmob-brain/.brain/brain.py login` |
| Packet says "offline" | Nothing; it syncs when you're back online |
| A file "not shared" | Remove the key or password from that file; it syncs next time |
| Anything else | `python ~/mockmob-brain/.brain/brain.py doctor` |

Design and edge cases: `.brain/DESIGN.md`. Team roles: `TEAM.md`. Agent rules: `AGENTS.md`.
