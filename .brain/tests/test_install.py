"""Tests for .brain/install.py. Every test runs against a temp HOME; the real ~/.claude, ~/.codex and
~/.mockmob-brain are never touched."""
from __future__ import annotations

import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock

BRAIN_TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BRAIN_TOOLS))
import install  # noqa: E402

REAL_REPO = BRAIN_TOOLS.parent

FOREIGN_HOOK = {"type": "command", "command": '"C:/Python/python.exe" -B "C:/other/scripts/hook.py" claude SessionStart', "timeout": 15}
SETTINGS = {
    "env": {"FOO": "bar"},
    "permissions": {"allow": ["Bash(ls:*)"]},
    "hooks": {
        "SessionStart": [{"hooks": [FOREIGN_HOOK]}],
        "PostToolUse": [{"matcher": "Edit|Write|Skill", "hooks": [{"type": "command", "command": "other-tool post", "timeout": 5}]}],
        "PreToolUse": [{"matcher": "*", "hooks": [{"type": "command", "command": "guard", "timeout": 3}]}],
    },
    "theme": "dark",
}
CLAUDE_JSON = {
    "numStartups": 42,
    "mcpServers": {"context7": {"type": "stdio", "command": "npx", "args": ["-y", "ctx7"], "env": {}}},
    "projects": {"C:/x": {"allowedTools": []}},
}
CLAUDE_MD = "# My global rules\n\nBe brief.\n"
CODEX_TOML = (
    '[features]\nhooks = true\n\n[mcp_servers.supabase]\nurl = "https://example.invalid/mcp"\n\n'
    '[mcp_servers.node_repl]\ncommand = "node"\nargs = ["repl.js"]\n'
)
CODEX_HOOKS = {"hooks": {"Stop": [{"hooks": [{"type": "command", "command": "other-codex-hook", "timeout": 10}]}]}}
CODEX_AGENTS = "# Codex rules\n\nAnswer in English.\n"
TEAM_MD = """# Team

| Person | Role | Final say on |
|---|---|---|
| Atishay | Founder (owner) | Product |
| CTO (name added at install) | CTO | Architecture |

## How disagreements are settled
"""


def write_json(path: Path, doc) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(doc, indent=2) + "\n"
    path.write_text(text, encoding="utf-8", newline="\n")
    return text


def git_init(path: Path, origin: str | None = None):
    path.mkdir(parents=True, exist_ok=True)
    subprocess.run(["git", "init", "-q", "-b", "main", str(path)], check=True)
    if origin:
        subprocess.run(["git", "-C", str(path), "remote", "add", "origin", origin], check=True)


class InstallBase(unittest.TestCase):
    with_codex = True

    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix="mmbrain-install-"))
        self.addCleanup(shutil.rmtree, self.root, ignore_errors=True)
        self.home = self.root / "home"
        self.home.mkdir()
        self.state = self.root / "state"
        self.work = self.root / "work"
        self.brain = self.work / "mockmob-brain"
        self.code = self.work / "mockmob"
        shutil.copytree(BRAIN_TOOLS, self.brain / ".brain",
                        ignore=shutil.ignore_patterns("tests", "__pycache__", "cache", "*.bak-*", "team.json"))
        (self.brain / "TEAM.md").write_text(TEAM_MD, encoding="utf-8")
        (self.brain / "README.md").write_text("# MockMob brain\n\nHello team.\n", encoding="utf-8")
        (self.brain / "docs").mkdir()
        (self.brain / "docs" / "NOW.md").write_text("# Now\n\nShipping.\n", encoding="utf-8")
        git_init(self.brain, "https://example.invalid/atishay07/mockmob-brain.git")
        git_init(self.code, "https://example.invalid/atishay07/mockmob.git")
        (self.code / "AGENTS.md").write_text("# Code agents\n\nBudget rules here.\n", encoding="utf-8")

        self.settings_text = write_json(self.home / ".claude" / "settings.json", SETTINGS)
        self.claude_md_text = CLAUDE_MD
        (self.home / ".claude" / "CLAUDE.md").write_text(CLAUDE_MD, encoding="utf-8", newline="\n")
        self.claude_json_text = write_json(self.home / ".claude.json", CLAUDE_JSON)
        mem = self.home / ".claude" / "projects" / "C--Users-dev-Desktop-mockmob" / "memory"
        mem.mkdir(parents=True)
        (mem / "MEMORY.md").write_text("- [x](x.md)\n", encoding="utf-8")
        other = self.home / ".claude" / "projects" / "C--Users-dev-Desktop-unrelated" / "memory"
        other.mkdir(parents=True)
        if self.with_codex:
            cdir = self.home / ".codex"
            cdir.mkdir()
            (cdir / "config.toml").write_text(CODEX_TOML, encoding="utf-8", newline="\n")
            self.codex_hooks_text = write_json(cdir / "hooks.json", CODEX_HOOKS)
            (cdir / "AGENTS.md").write_text(CODEX_AGENTS, encoding="utf-8", newline="\n")

        env = {"HOME": str(self.home), "USERPROFILE": str(self.home), "MOCKMOB_BRAIN_STATE": str(self.state),
               "MOCKMOB_BRAIN_NO_CLI": "1", "MOCKMOB_BRAIN_NO_VENV": "1", "MOCKMOB_BRAIN_NO_VECTORS": "1"}
        patcher = mock.patch.dict(os.environ, env)
        patcher.start()
        self.addCleanup(patcher.stop)
        for key in ("CLAUDE_CONFIG_DIR", "CODEX_HOME", "MOCKMOB_BRAIN", "MOCKMOB_BRAIN_CODE_DIRS", "MOCKMOB_BRAIN_MODELS"):
            os.environ.pop(key, None)

    # -- helpers
    def run_install(self, *extra, expect=0, with_code=True):
        argv = ["--yes", "--quiet", "--skip-selftest", "--brain-dir", str(self.brain),
                "--name", "Dev Person", "--role", "cto", "--email", "dev@example.com", *extra]
        if with_code and "--code-dir" not in extra:
            argv += ["--code-dir", str(self.code)]
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = install.main(argv)
        self.assertEqual(code, expect, buf.getvalue())
        return buf.getvalue()

    def uninstall(self):
        with redirect_stdout(io.StringIO()):
            self.assertEqual(install.main(["--uninstall", "--quiet", "--brain-dir", str(self.brain)]), 0)

    def snapshot(self) -> dict:
        out = {}
        for base in (self.home, self.state, self.brain / "TEAM.md", self.brain / ".brain" / "team.json"):
            files = [base] if base.is_file() else (sorted(p for p in base.rglob("*") if p.is_file()) if base.is_dir() else [])
            for p in files:
                if ".bak-mockmob" in p.name or p.suffix in (".sqlite", ".lock") or "-wal" in p.name or "-shm" in p.name:
                    continue
                if "index" in p.parts and p.parent.name == "index":
                    continue
                out[str(p)] = p.read_bytes()
        return out

    def load(self, path: Path):
        return json.loads(path.read_text(encoding="utf-8"))

    def ours(self, doc, event, harness="claude"):
        found = []
        for group in doc.get("hooks", {}).get(event, []):
            for h in group.get("hooks", []):
                if ".brain/hook.py" in h["command"] and f" {harness} {event}" in h["command"]:
                    found.append((group, h))
        return found

    def backups(self, path: Path):
        return sorted(path.parent.glob(path.name + ".bak-mockmob-*"))


class TestStandaloneInstall(InstallBase):
    def test_full_install(self):
        self.run_install()
        py = sys.executable.replace("\\", "/")
        hook = (self.brain / ".brain" / "hook.py").as_posix()

        cfg = self.load(self.state / "config.json")
        self.assertEqual(cfg["person"], "dev-person")
        self.assertEqual(cfg["display_name"], "Dev Person")
        self.assertEqual(cfg["role"], "cto")
        self.assertEqual(cfg["email"], "dev@example.com")
        self.assertEqual(cfg["mode"], "standalone")
        self.assertEqual(cfg["python"], sys.executable)
        self.assertFalse(cfg["vectors"])
        self.assertEqual(Path(cfg["brain_dir"]), self.brain.resolve())
        self.assertEqual([Path(p) for p in cfg["code_dirs"]], [self.code])
        self.assertEqual([Path(p).parent.name for p in cfg["memory_dirs"]], ["C--Users-dev-Desktop-mockmob"])

        # Claude hooks: ours added with the spec's timeouts and matcher, foreign ones untouched
        settings = self.load(self.home / ".claude" / "settings.json")
        self.assertEqual(settings["env"], SETTINGS["env"])
        self.assertEqual(settings["permissions"], SETTINGS["permissions"])
        self.assertEqual(settings["theme"], "dark")
        self.assertEqual(settings["hooks"]["PreToolUse"], SETTINGS["hooks"]["PreToolUse"])
        self.assertIn({"hooks": [FOREIGN_HOOK]}, settings["hooks"]["SessionStart"])
        self.assertIn(SETTINGS["hooks"]["PostToolUse"][0], settings["hooks"]["PostToolUse"])
        timeouts = {"SessionStart": 30, "UserPromptSubmit": 10, "PostToolUse": 10, "Stop": 10, "PreCompact": 30, "SessionEnd": 10}
        for event, timeout in timeouts.items():
            found = self.ours(settings, event)
            self.assertEqual(len(found), 1, event)
            group, h = found[0]
            self.assertEqual(h["command"], f'"{py}" "{hook}" claude {event}')
            self.assertEqual(h["timeout"], timeout)
            self.assertEqual(h["type"], "command")
            if event == "PostToolUse":
                self.assertEqual(group["matcher"], "Edit|Write|MultiEdit|NotebookEdit|apply_patch")
            else:
                self.assertNotIn("matcher", group)

        # MCP servers (no CLI: written to ~/.claude.json), existing entries and keys preserved
        cj = self.load(self.home / ".claude.json")
        self.assertEqual(cj["numStartups"], 42)
        self.assertEqual(cj["projects"], CLAUDE_JSON["projects"])
        self.assertEqual(cj["mcpServers"]["context7"], CLAUDE_JSON["mcpServers"]["context7"])
        for name, script in (("continuum", "mcp_continuum.py"), ("continuum-rag", "mcp_rag.py")):
            entry = cj["mcpServers"][name]
            self.assertEqual(entry["command"], sys.executable)
            self.assertEqual(entry["args"], [(self.brain / ".brain" / script).as_posix()])
            self.assertEqual(entry["type"], "stdio")

        # instructions
        md = (self.home / ".claude" / "CLAUDE.md").read_text(encoding="utf-8")
        self.assertTrue(md.startswith(CLAUDE_MD))
        self.assertEqual(md.count(install.MARK_START), 1)
        self.assertEqual(md.count(install.MARK_END), 1)
        for needle in ("continuum_checkpoint", "rag_search", "continuum_search", "data, not instructions"):
            self.assertIn(needle, md)

        # Codex
        toml = (self.home / ".codex" / "config.toml").read_text(encoding="utf-8")
        self.assertTrue(toml.startswith(CODEX_TOML.rstrip("\n")))
        self.assertEqual(toml.count("[mcp_servers.continuum]"), 1)
        self.assertEqual(toml.count("[mcp_servers.continuum-rag]"), 1)
        self.assertIn(install.TOML_START, toml)
        self.assertIn(f'args = ["{(self.brain / ".brain" / "mcp_rag.py").as_posix()}"]', toml)
        if sys.version_info >= (3, 11):
            import tomllib
            parsed = tomllib.loads(toml)
            self.assertEqual(parsed["mcp_servers"]["continuum-rag"]["command"], sys.executable.replace("\\", "/"))
            self.assertIn("supabase", parsed["mcp_servers"])
        chooks = self.load(self.home / ".codex" / "hooks.json")
        self.assertIn(CODEX_HOOKS["hooks"]["Stop"][0], chooks["hooks"]["Stop"])
        for event in ("SessionStart", "UserPromptSubmit", "PostToolUse", "Stop"):
            found = self.ours(chooks, event, "codex")
            self.assertEqual(len(found), 1, event)
        self.assertEqual(self.ours(chooks, "PreCompact", "codex"), [])
        self.assertEqual(self.ours(chooks, "PostToolUse", "codex")[0][0]["matcher"], "Edit|Write|MultiEdit|NotebookEdit|apply_patch")
        agents = (self.home / ".codex" / "AGENTS.md").read_text(encoding="utf-8")
        self.assertTrue(agents.startswith(CODEX_AGENTS))
        self.assertEqual(agents.count(install.MARK_START), 1)

        # team files
        team = self.load(self.brain / ".brain" / "team.json")
        ids = [p["id"] for p in team["people"]]
        self.assertEqual(ids, ["atishay", "dev-person"])
        self.assertEqual(team["people"][0]["role"], "owner")
        team_md = (self.brain / "TEAM.md").read_text(encoding="utf-8")
        self.assertIn("| Dev Person | CTO |", team_md)
        self.assertNotIn(install.TEAM_PLACEHOLDER, team_md)

        # git settings on the brain clone only
        def gitcfg(key):
            return subprocess.run(["git", "-C", str(self.brain), "config", "--local", "--get", key], capture_output=True, text=True).stdout.strip()
        self.assertEqual(gitcfg("user.name"), "Dev Person")
        self.assertEqual(gitcfg("user.email"), "dev@example.com")
        self.assertEqual(gitcfg("pull.rebase"), "true")
        self.assertEqual(gitcfg("rebase.autoStash"), "true")
        self.assertEqual(gitcfg("core.autocrlf"), "false")
        self.assertEqual(gitcfg("fetch.prune"), "true")
        self.assertEqual(gitcfg("core.longpaths"), "true" if os.name == "nt" else "")

        # keyword index built inline
        self.assertTrue((self.state / "index" / "rag.sqlite").is_file())

        # every edited file was backed up
        for path in (self.home / ".claude" / "settings.json", self.home / ".claude" / "CLAUDE.md", self.home / ".claude.json",
                     self.home / ".codex" / "config.toml", self.home / ".codex" / "hooks.json", self.home / ".codex" / "AGENTS.md"):
            baks = self.backups(path)
            self.assertEqual(len(baks), 1, path)
        original = self.backups(self.home / ".claude" / "settings.json")[0].read_text(encoding="utf-8")
        self.assertEqual(original, self.settings_text)

    def test_idempotent(self):
        self.run_install()
        first = self.snapshot()
        baks = {p.name for p in self.home.rglob("*") if ".bak-mockmob" in p.name}
        self.run_install()
        second = self.snapshot()
        self.assertEqual(first, second)
        self.assertEqual({p.name for p in self.home.rglob("*") if ".bak-mockmob" in p.name}, baks)  # no new backups
        settings = self.load(self.home / ".claude" / "settings.json")
        for event in ("SessionStart", "UserPromptSubmit", "PostToolUse", "Stop", "PreCompact", "SessionEnd"):
            self.assertEqual(len(self.ours(settings, event)), 1)
        md = (self.home / ".claude" / "CLAUDE.md").read_text(encoding="utf-8")
        self.assertEqual(md.count(install.MARK_START), 1)
        team = self.load(self.brain / ".brain" / "team.json")
        self.assertEqual(len(team["people"]), 2)
        self.assertEqual((self.brain / "TEAM.md").read_text(encoding="utf-8").count("Dev Person"), 1)

    def test_rerun_replaces_our_hooks_when_python_changes(self):
        self.run_install()
        settings_path = self.home / ".claude" / "settings.json"
        doc = self.load(settings_path)
        for group, h in self.ours(doc, "Stop"):
            h["command"] = h["command"].replace(sys.executable.replace("\\", "/"), "C:/old/python.exe")
        write_json(settings_path, doc)
        self.run_install()
        doc = self.load(settings_path)
        found = self.ours(doc, "Stop")
        self.assertEqual(len(found), 1)
        self.assertNotIn("old/python", found[0][1]["command"])

    def test_uninstall_restores_clean_state(self):
        before = self.snapshot()
        self.run_install()
        self.assertNotEqual(self.snapshot(), before)
        self.uninstall()
        home = self.home
        self.assertEqual((home / ".claude" / "settings.json").read_text(encoding="utf-8"), self.settings_text)
        self.assertEqual((home / ".claude" / "CLAUDE.md").read_text(encoding="utf-8"), CLAUDE_MD)
        self.assertEqual(self.load(home / ".claude.json"), CLAUDE_JSON)
        self.assertEqual((home / ".codex" / "config.toml").read_text(encoding="utf-8"), CODEX_TOML)
        self.assertEqual(self.load(home / ".codex" / "hooks.json"), CODEX_HOOKS)
        self.assertEqual((home / ".codex" / "AGENTS.md").read_text(encoding="utf-8"), CODEX_AGENTS)
        # our config and the brain's team files stay (uninstall only removes the agent wiring)
        self.assertTrue((self.state / "config.json").is_file())
        # a second uninstall is a no-op
        snap = self.snapshot()
        self.uninstall()
        self.assertEqual(self.snapshot(), snap)

    def test_uninstall_without_install_touches_nothing(self):
        before = self.snapshot()
        self.uninstall()
        self.assertEqual(self.snapshot(), before)
        self.assertEqual([p for p in self.home.rglob("*") if ".bak-mockmob" in p.name], [])

    def test_uninstall_keeps_foreign_entries_with_similar_names(self):
        self.run_install()
        cj_path = self.home / ".claude.json"
        doc = self.load(cj_path)
        doc["mcpServers"]["continuum"] = {"type": "stdio", "command": "node", "args": ["C:/AI OS/scripts/mcp-server.mjs"], "env": {}}
        write_json(cj_path, doc)
        self.uninstall()
        after = self.load(cj_path)
        self.assertIn("continuum", after["mcpServers"])  # not ours: left alone
        self.assertNotIn("continuum-rag", after["mcpServers"])

    def test_existing_mcp_name_pointing_elsewhere_is_skipped_with_warning(self):
        foreign = {"type": "stdio", "command": "node", "args": ["C:/AI OS/scripts/mcp-server.mjs"], "env": {}}
        doc = dict(CLAUDE_JSON)
        doc["mcpServers"] = {**CLAUDE_JSON["mcpServers"], "continuum": foreign}
        write_json(self.home / ".claude.json", doc)
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = install.main(["--yes", "--skip-selftest", "--brain-dir", str(self.brain), "--name", "Dev Person",
                                 "--role", "cto", "--email", "dev@example.com", "--code-dir", str(self.code)])
        self.assertEqual(code, 0)
        self.assertIn("'continuum' already exists", buf.getvalue())
        cj = self.load(self.home / ".claude.json")
        self.assertEqual(cj["mcpServers"]["continuum"], foreign)
        self.assertIn("continuum-rag", cj["mcpServers"])

    def test_our_mcp_entry_with_other_python_is_updated(self):
        self.run_install()
        cj_path = self.home / ".claude.json"
        doc = self.load(cj_path)
        doc["mcpServers"]["continuum-rag"]["command"] = "C:/old/python.exe"
        write_json(cj_path, doc)
        self.run_install()
        self.assertEqual(self.load(cj_path)["mcpServers"]["continuum-rag"]["command"], sys.executable)

    def test_invalid_settings_json_is_not_clobbered(self):
        bad = self.home / ".claude" / "settings.json"
        bad.write_text("{ not json", encoding="utf-8")
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = install.main(["--yes", "--quiet", "--skip-selftest", "--brain-dir", str(self.brain), "--name", "Dev Person",
                                 "--role", "cto", "--email", "dev@example.com", "--code-dir", str(self.code)])
        self.assertEqual(code, 1)
        self.assertEqual(bad.read_text(encoding="utf-8"), "{ not json")
        self.assertEqual(self.backups(bad), [])
        # the rest still went in
        self.assertIn(install.MARK_START, (self.home / ".claude" / "CLAUDE.md").read_text(encoding="utf-8"))

    def test_four_space_indent_is_kept(self):
        path = self.home / ".claude" / "settings.json"
        path.write_text(json.dumps(SETTINGS, indent=4) + "\n", encoding="utf-8")
        self.run_install()
        text = path.read_text(encoding="utf-8")
        self.assertRegex(text, r'\n    "env"')
        self.uninstall()
        self.assertEqual(path.read_text(encoding="utf-8"), json.dumps(SETTINGS, indent=4) + "\n")

    def test_codex_server_defined_elsewhere_is_not_duplicated(self):
        cfg = self.home / ".codex" / "config.toml"
        cfg.write_text(CODEX_TOML + '\n[mcp_servers.continuum]\ncommand = "node"\nargs = ["x.mjs"]\n', encoding="utf-8", newline="\n")
        self.run_install()
        toml = cfg.read_text(encoding="utf-8")
        self.assertEqual(len(re.findall(r"^\[mcp_servers\.continuum\]", toml, re.M)), 1)
        self.assertEqual(len(re.findall(r"^\[mcp_servers\.continuum-rag\]", toml, re.M)), 1)
        self.uninstall()
        self.assertEqual(cfg.read_text(encoding="utf-8"), CODEX_TOML + '\n[mcp_servers.continuum]\ncommand = "node"\nargs = ["x.mjs"]\n')

    def test_cli_is_used_when_present(self):
        fake_dir = self.root / "bin"
        fake_dir.mkdir()
        log = self.root / "cli.log"
        if os.name == "nt":
            (fake_dir / "claude.cmd").write_text(f'@echo %* >> "{log}"\r\n@exit /b 0\r\n', encoding="utf-8")
        else:
            exe = fake_dir / "claude"
            exe.write_text(f'#!/bin/sh\necho "$@" >> "{log}"\nexit 0\n', encoding="utf-8")
            exe.chmod(0o755)
        env = {"PATH": str(fake_dir) + os.pathsep + os.environ["PATH"]}
        with mock.patch.dict(os.environ, env):
            os.environ.pop("MOCKMOB_BRAIN_NO_CLI")
            self.run_install()
        lines = [l.strip() for l in log.read_text(encoding="utf-8").splitlines() if l.strip()]
        add_lines = [l for l in lines if l.startswith("mcp add")]
        self.assertEqual(len(add_lines), 2, lines)
        self.assertIn("mcp add --scope user continuum -- ", add_lines[0])
        self.assertTrue(add_lines[0].endswith("mcp_continuum.py"), add_lines[0])
        self.assertIn("mcp add --scope user continuum-rag -- ", add_lines[1])
        # the fake CLI wrote nothing, so the installer fell back to editing ~/.claude.json
        self.assertIn("continuum-rag", self.load(self.home / ".claude.json")["mcpServers"])


class TestOtherModes(InstallBase):
    def test_bridge_mode_changes_no_agent_files(self):
        before = self.snapshot()
        self.run_install("--mode", "bridge")
        after = self.snapshot()
        agent_files = {k for k in before if ".claude" in k or ".codex" in k}
        for key in agent_files:
            self.assertEqual(before[key], after[key], key)
        self.assertEqual([p for p in self.home.rglob("*") if ".bak-mockmob" in p.name], [])
        self.assertFalse((self.state / "index" / "rag.sqlite").exists())
        cfg = self.load(self.state / "config.json")
        self.assertEqual(cfg["mode"], "bridge")
        self.assertEqual(
            subprocess.run(["git", "-C", str(self.brain), "config", "--local", "--get", "pull.rebase"], capture_output=True, text=True).stdout.strip(),
            "true")

    def test_no_codex_folder_means_no_codex_files(self):
        shutil.rmtree(self.home / ".codex")
        self.run_install()
        self.assertFalse((self.home / ".codex").exists())

    def test_duplicate_person_id_with_different_email_is_refused(self):
        write_json(self.brain / ".brain" / "team.json",
                   {"people": [{"id": "dev-person", "name": "Dev Person", "role": "cto", "email": "someone-else@example.com"}]})
        self.run_install(expect=2)
        self.assertFalse((self.state / "config.json").exists())
        self.assertFalse((self.home / ".claude" / "CLAUDE.md").read_text(encoding="utf-8").count(install.MARK_START))

    def test_same_person_same_email_is_fine(self):
        write_json(self.brain / ".brain" / "team.json",
                   {"people": [{"id": "dev-person", "name": "Dev Person", "role": "cto", "email": "DEV@example.com"}]})
        self.run_install()
        self.assertEqual(len(self.load(self.brain / ".brain" / "team.json")["people"]), 1)

    def test_owner_install_does_not_seed_an_extra_owner(self):
        argv = ["--yes", "--quiet", "--skip-selftest", "--brain-dir", str(self.brain), "--name", "Atishay", "--role", "owner",
                "--email", "a@example.com", "--code-dir", str(self.code), "--mode", "bridge"]
        with redirect_stdout(io.StringIO()):
            self.assertEqual(install.main(argv), 0)
        team = self.load(self.brain / ".brain" / "team.json")
        self.assertEqual([p["id"] for p in team["people"]], ["atishay"])
        self.assertEqual(team["people"][0]["email"], "a@example.com")
        self.assertEqual((self.brain / "TEAM.md").read_text(encoding="utf-8"), TEAM_MD)  # his row already exists

    def test_missing_name_is_an_error(self):
        buf = io.StringIO()
        with mock.patch.dict(os.environ, {"GIT_CONFIG_GLOBAL": str(self.root / "nogit"), "GIT_CONFIG_NOSYSTEM": "1"}):
            with redirect_stdout(buf):
                code = install.main(["--yes", "--quiet", "--skip-selftest", "--brain-dir", str(self.brain), "--mode", "bridge"])
        self.assertEqual(code, 2)
        self.assertIn("--name", buf.getvalue())


class TestDetection(InstallBase):
    def test_code_repo_found_next_to_brain(self):
        decoy = self.work / "decoy"
        git_init(decoy, "https://github.com/someone/else.git")
        found = install.detect_code_dirs(self.brain)
        self.assertEqual(found, [self.code])

    def test_brain_clone_is_never_taken_as_code_repo(self):
        shutil.rmtree(self.code, ignore_errors=True)
        self.assertEqual(install.detect_code_dirs(self.brain), [])

    def test_code_repo_found_on_desktop(self):
        shutil.rmtree(self.code)
        nested = self.home / "Desktop" / "mockmob copy" / "mockmob copy"
        git_init(nested, "git@github.com:atishay07/mockmob.git")
        self.assertEqual(install.detect_code_dirs(self.brain), [nested])

    def test_autodetect_used_by_installer(self):
        self.run_install(with_code=False)
        cfg = self.load(self.state / "config.json")
        self.assertEqual([Path(p) for p in cfg["code_dirs"]], [self.code])

    def test_memory_dirs_match_code_dir_key_or_mockmob(self):
        got = install.detect_memory_dirs([Path("C:/Users/dev/Desktop/mockmob")])
        self.assertEqual([p.parent.name for p in got], ["C--Users-dev-Desktop-mockmob"])
        extra = self.home / ".claude" / "projects" / "D--stuff-app" / "memory"
        extra.mkdir(parents=True)
        got = install.detect_memory_dirs([Path("D:/stuff/app")])
        self.assertIn("D--stuff-app", [p.parent.name for p in got])

    def test_prerequisites_ok_here(self):
        self.assertEqual(install.check_prerequisites(), [])


class TestPureHelpers(unittest.TestCase):
    def test_block_roundtrip(self):
        for original in ("", "x\n", "x\n\ny\n", "# T\n\nbody\n"):
            added = install.add_block(original, install.INSTRUCTION_BLOCK)
            self.assertEqual(added.count(install.MARK_START), 1)
            self.assertEqual(install.add_block(added, install.INSTRUCTION_BLOCK), added)
            self.assertEqual(install.remove_block(added), original)

    def test_block_in_the_middle_keeps_text_after(self):
        text = "head\n\n" + install.INSTRUCTION_BLOCK + "\n\ntail\n"
        self.assertEqual(install.remove_block(text), "head\n\ntail\n")

    def test_add_team_row(self):
        text = install.add_team_row(TEAM_MD, "Sam Lee", "member")
        self.assertIn("| Sam Lee | member |", text)
        self.assertEqual(install.add_team_row(text, "Sam Lee", "member"), text)
        self.assertIn("| Priya | CTO | Architecture |", install.add_team_row(TEAM_MD, "Priya", "cto"))

    def test_strip_ours_keeps_mixed_groups(self):
        groups = [{"hooks": [{"type": "command", "command": '"p" "C:/x/.brain/hook.py" claude Stop'},
                             {"type": "command", "command": "other"}]},
                  {"hooks": [{"type": "command", "command": '"p" "C:\\y\\.brain\\hook.py" claude Stop'}]}]
        self.assertEqual(install.strip_ours(groups), [{"hooks": [{"type": "command", "command": "other"}]}])

    def test_hook_command_exec_form(self):
        cmd = install.hook_command("C:\\Py\\python.exe", Path("C:/brain/.brain"), "codex", "Stop")
        self.assertEqual(cmd, '"C:/Py/python.exe" "C:/brain/.brain/hook.py" codex Stop')


class TestSelfTest(InstallBase):
    def test_rag_server_round_trip(self):
        self.run_install()
        ok, detail, replies = install.mcp_roundtrip(sys.executable, self.brain / ".brain" / "mcp_rag.py",
                                                    {"name": "rag_search", "arguments": {"query": "Shipping", "mode": "keyword"}})
        self.assertTrue(ok, detail)
        body = json.loads(replies[3]["result"]["content"][0]["text"])
        self.assertEqual(body["results"][0]["file"], "brain/docs/NOW.md")

    def test_missing_server_script_fails_cleanly(self):
        ok, detail, _ = install.mcp_roundtrip(sys.executable, self.root / "nope.py", timeout=30)
        self.assertFalse(ok)

    def test_full_selftest_when_all_modules_exist(self):
        needed = ["hook.py", "mcp_continuum.py", "mcp_rag.py", "brainlib/sync.py", "brainlib/packet.py", "brainlib/config.py"]
        if not all((self.brain / ".brain" / n).is_file() for n in needed):
            self.skipTest("other modules are not written yet")
        self.run_install()
        report = install.Report(quiet=True)
        cfg = self.load(self.state / "config.json")
        results = install.selftest(cfg, self.brain, True, report)
        by_name = {name: (ok, detail) for name, ok, detail in results}
        self.assertTrue(by_name["MCP continuum-rag round trip"][0], by_name)
        self.assertTrue(by_name["MCP continuum round trip"][0], by_name)
        self.assertTrue(by_name["SessionStart hook prints a packet"][0], by_name)
        self.assertTrue(by_name["rag_search returns hits"][0], by_name)
        self.assertIn("cannot reach", by_name["git remote"][1])  # the fake origin is an .invalid host: no real network
        # the self-test must not leave claims or handovers in the real brain
        self.assertFalse((self.brain / "claims").exists())
        self.assertEqual(list((self.brain / "handoffs").glob("**/*")) if (self.brain / "handoffs").exists() else [], [])

    def test_doctor_runs_without_changing_files(self):
        self.run_install()
        before = self.snapshot()
        with redirect_stdout(io.StringIO()):
            install.main(["--doctor", "--quiet"])
        self.assertEqual(self.snapshot(), before)


if __name__ == "__main__":
    unittest.main()
