"""safety.py: allowlist, path sanity, secret scan, size and binary checks.

Secret-looking samples are assembled at run time so this file itself never trips the scan.
"""
from __future__ import annotations

import unittest
from pathlib import Path

import _gitfixture  # noqa: F401  (puts .brain on sys.path)
from brainlib import safety

BRAIN_DOT = Path(__file__).resolve().parents[1]


def s(*parts) -> str:
    return "".join(parts)


class AllowlistTests(unittest.TestCase):
    def test_allowed(self):
        for p in (
            "docs/NOW.md", "docs/sub/dir/x.md", "context/a.md", "handoffs/mockmob/x.json",
            "playbook/memory/alice/MEMORY.md", "claims/alice/abc12345.json", "conflicts/20261106-alice/docs/x.json",
            ".brain/brain.py", ".brain/brainlib/sync.py", ".brain/team.json", ".brain/tests/test_sync.py",
            "TEAM.md", "README.md", "AGENTS.md", "CLAUDE.md", ".gitattributes", ".gitignore",
            "docs\\win\\path.md", "./docs/NOW.md",
        ):
            self.assertTrue(safety.is_allowed(p), p)

    def test_not_allowed(self):
        for p in (
            "", "src/app.py", "package.json", "docs", ".brain/cache/rag.sqlite", ".brain/cache/x/y",
            "node_modules/x.js", "../docs/x.md", "docs/../../etc/passwd", "/etc/passwd", "C:/docs/x.md",
            "NOTES.md", "secrets.env", ".env", ".git/config", "docs/__pycache__/x.pyc", ".brain/brainlib/__pycache__/a.cpython-312.pyc",
            "other/docs/x.md", ".brainx/file", "TEAM.md/x",
        ):
            self.assertFalse(safety.is_allowed(p), p)


class PathTests(unittest.TestCase):
    def test_reserved_windows_names(self):
        for p in ("docs/CON.md", "docs/con", "docs/NUL.txt", "docs/aux.md", "docs/prn.md", "docs/COM1.md",
                  "docs/com9.txt", "docs/LPT1", "docs/lpt9.x", "docs/CON/inside.md", "CON", "docs/con.tar.gz"):
            self.assertTrue(safety.check_path(p, tracked=[]), p)
        for p in ("docs/console.md", "docs/com10.md", "docs/COM0.md", "docs/conf.md", "docs/aux-notes.md", "docs/lpt.md"):
            self.assertEqual(safety.check_path(p, tracked=[]), [], p)

    def test_forbidden_characters(self):
        for p in ('docs/a:b.md', 'docs/a<b.md', 'docs/a>b.md', 'docs/a"b.md', 'docs/a|b.md', 'docs/a?b.md',
                  'docs/a*b.md', "docs/a\x01b.md", "docs/a\tb.md", "docs/a\x7fb.md"):
            self.assertTrue(safety.check_path(p, tracked=[]), repr(p))
        self.assertEqual(safety.check_path("docs/ok name (1) - é.md", tracked=[]), [])

    def test_trailing_dot_or_space(self):
        for p in ("docs/a.", "docs/a ", "docs/dir./a.md", "docs/dir /a.md", "docs/a.md."):
            self.assertTrue(safety.check_path(p, tracked=[]), repr(p))
        self.assertEqual(safety.check_path("docs/.hidden", tracked=[]), [])

    def test_length_limit(self):
        ok = "docs/" + "a" * (180 - 5)
        too_long = ok + "b"
        self.assertEqual(len(ok), 180)
        self.assertEqual(safety.check_path(ok, tracked=[]), [])
        reasons = safety.check_path(too_long, tracked=[])
        self.assertTrue(any("too long" in r for r in reasons), reasons)

    def test_case_only_collision(self):
        tracked = ["docs/NOW.md", "docs/Specs/a.md", "README.md"]
        self.assertTrue(any("case-only" in r for r in safety.check_path("docs/now.md", tracked=tracked)))
        self.assertTrue(any("case-only" in r for r in safety.check_path("docs/specs/b.md", tracked=tracked)))
        self.assertTrue(any("case-only" in r for r in safety.check_path("Readme.md", tracked=tracked)))
        self.assertEqual(safety.check_path("docs/NOW.md", tracked=tracked), [])  # itself is not a collision
        self.assertEqual(safety.check_path("docs/Specs/c.md", tracked=tracked), [])
        self.assertEqual(safety.check_path("docs/other.md", tracked=tracked), [])

    def test_tracked_paths_come_from_the_repo_when_not_given(self):
        fx = _gitfixture.make_fixture(1)
        self.addCleanup(fx.cleanup)
        clone = fx.clones[0]
        self.assertIn("docs/NOW.md", safety.tracked_paths(clone.path))
        self.assertTrue(safety.check_path("docs/now.md", repo=clone.path))
        self.assertEqual(safety.check_path("docs/brand-new.md", repo=clone.path), [])


class SecretScanTests(unittest.TestCase):
    def kinds(self, text):
        return [f.kind for f in safety.scan_text(text)]

    def test_each_pattern(self):
        samples = {
            "anthropic-key": s("sk-", "ant-", "api03-", "A1b2C3d4E5f6G7h8I9j0K1l2"),
            "openai-key": s("sk-", "proj-", "abcdEFGH1234abcdEFGH1234abcd"),
            "secret-key": s("sk-", "abcdEFGH1234abcdEFGH1234"),
            "github-token": s("gh", "p_", "A1b2C3d4E5f6G7h8I9j0K1l2M3n4O5p6Q7r8"),
            "github-token ": s("gh", "o_", "A1b2C3d4E5f6G7h8I9j0K1l2M3n4O5p6Q7r8"),
            "github-token  ": s("github", "_pat_", "11ABCDEFG0abcdefghijkl_mnopqrstuvwxyz0123456789"),
            "aws-key": s("AK", "IA", "ABCDEFGHIJKLMNOP"),
            "slack-token": s("xo", "xb-", "1234567890-abcdefghij"),
            "razorpay-key": s("rzp", "_live_", "AbCdEf123456"),
            "razorpay-key ": s("rzp", "_test_", "AbCdEf123456"),
            "jwt": s("ey", "J", "h" * 30, ".", "b" * 40, ".", "c" * 40),
            "supabase-token": s("sb", "p_", "0123456789abcdef0123456789abcdef"),
            "google-api-key": s("AI", "za", "SyA-1234567890abcdefghijklmnopqrstuv"),
            "private-key": s("-----", "BEGIN RSA PRIVATE KEY", "-----\nMIIEow\n-----", "END RSA PRIVATE KEY", "-----"),
            "pem-header": s("-----", "BEGIN CERTIFICATE", "-----"),
            "generic-secret": s("api", "_key", " = ", "Zq8f3Lm92XvTn40Pa7", "BcD"),
        }
        for kind, text in samples.items():
            found = self.kinds("some context\n" + text + "\nmore")
            self.assertTrue(found, f"{kind}: {text!r} was not detected")
            self.assertEqual(found[0], kind.strip(), f"{kind}: got {found}")

    def test_generic_secret_variants(self):
        value = "Zq8f3Lm92XvTn40P"  # exactly 16 chars
        self.assertEqual(len(value), 16)
        for key in ("api_key", "API-KEY", "secret", "password", "token", "service_role", "apikey"):
            for sep in ("=", ":", " = ", ": "):
                self.assertTrue(self.kinds(f"{key}{sep}{value}"), f"{key}{sep}")
        self.assertTrue(self.kinds(f'"password": "{value}"'))
        self.assertEqual(self.kinds("password = " + value[:15]), [])  # 15 chars: too short
        self.assertEqual(self.kinds("the password is unchanged"), [])
        self.assertEqual(self.kinds("token: short"), [])

    def test_jwt_any_length_but_segments_need_10_chars(self):
        head = s("ey", "J", "hbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9")
        service_role = s(head, ".", "ey", "Jyb2xlIjoic2VydmljZV9yb2xlIn0", ".", "a" * 30)
        self.assertEqual(len(service_role), 99)  # the real-life gap: just under the old 100-char rule
        self.assertEqual(self.kinds(service_role), ["jwt"])
        self.assertEqual(self.kinds(s("ey", "J", "a" * 10, ".", "b" * 10, ".", "c" * 10)), ["jwt"])
        self.assertEqual(self.kinds(s("ey", "J", "a" * 10, ".", "b" * 9, ".", "c" * 10)), [])
        self.assertEqual(self.kinds(s("ey", "J", "a" * 10, ".", "b" * 10, ".", "c" * 9)), [])
        self.assertEqual(self.kinds(s("ey", "J", "a" * 40, ".", "b" * 40, ".", "c" * 30)), ["jwt"])

    def test_the_service_role_env_line_that_slipped_through(self):
        jwt = s("ey", "JhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9", ".", "ey", "Jyb2xlIjoic2VydmljZV9yb2xlIn0", ".", "a" * 30)
        line = s("SUPABASE_SERVICE", "_ROLE_", "KEY", "=", jwt)
        (f,) = safety.scan_text("# env" + chr(10) + line + chr(10))
        self.assertEqual(f.line, 2)
        self.assertNotIn(jwt, f.excerpt)
        self.assertNotIn(jwt, safety.redact(line))
        self.assertTrue(safety.redact(line).startswith("SUPABASE_SERVICE_ROLE_KEY="))
        self.assertTrue(safety.check_bytes("docs/env.md", line.encode()))

    def test_env_style_names_with_a_secret_word(self):
        value = "Zq8f3Lm92XvTn40P" + "aBcD"
        names = (
            "SUPABASE_SERVICE_ROLE_KEY", "RAZORPAY_KEY_SECRET", "apiKey", "clientSecret", "DB-PASSWORD", "GITHUB_TOKEN",
            "my_token", "Token", "PRIVATE_KEY", "AWS_CREDENTIAL", "STRIPE_CREDENTIALS", "dbPasswd", "accessToken",
            "authtoken", "x-api-key", "OPENAI_API_KEY", "SECRET", "service_role", "SERVICE-ROLE",
        )
        for name in names:
            for text in (f"{name}={value}", f"{name}: {value}", f'{name} = "{value}"', f'"{name}": "{value}"',
                         f"export {name}='{value}'"):
                self.assertEqual([f.kind for f in safety.scan_text(text)], ["generic-secret"], text)
        self.assertNotIn(value, safety.redact(f"RAZORPAY_KEY_SECRET={value}"))
        self.assertIn("RAZORPAY_KEY_SECRET=[REDACTED]", safety.redact(f"RAZORPAY_KEY_SECRET={value}"))

    def test_env_style_needs_16_chars_and_a_secret_word(self):
        value = "Zq8f3Lm92XvTn40P"
        self.assertEqual(self.kinds("OPENAI_API_KEY=" + value[:15]), [])
        self.assertEqual(self.kinds("OPENAI_API_KEY=" + value), ["generic-secret"])
        for text in (
            f"monkey={value}", f"turkey: {value}", f"keyboard_layout={value}", f"max_tokens={value}", f"PASSWORDLESS_MODE={value}",
            f"SUPABASE_URL={value}", f"user_name={value}", f"hotkey = {value}",
            "TOKEN_PATH=/home/user/some/long/path/to/file", "SECRET_FILE=./keys/some/long/path.txt",
            "secret_name = request.headers.authorization", "api_key = some_long_variable_name_here",
            "token_type: " + value, "token = process.env.SOME_LONG_TOKEN_NAME",
            "SECRET=" + chr(10) + value,  # the value is on the next line: not an assignment
            "password:" + chr(10) + "- " + value,
        ):
            self.assertEqual(self.kinds(text), [], text)

    def test_env_style_placeholders_do_not_count(self):
        for text in (
            "OPENAI_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxx", "OPENAI_API_KEY=your-key-goes-here-1234", "STRIPE_SECRET=example-example-example",
            "GITHUB_TOKEN=REDACTED-REDACTED-REDACTED", "DB_PASSWORD=changeme-changeme-123", "API_KEY=<paste-your-key-here-now>",
            "apiKey: process.env.SOME_LONG_VARIABLE", "SECRET=...................",
        ):
            self.assertEqual(self.kinds(text), [], text)

    def test_short_or_prefix_only_text_is_clean(self):
        for t in (
            "keys start with " + s("sk-", "ant-") + " and look like that",
            s("sk-", "short"),
            "ask-me-anything-about-the-new-feature-today",
            "task-management-and-scheduling-done-right",
            "risk-adjusted-return-calculation-methodology",
            s("gh", "p_"), s("rzp", "_live_"), s("AK", "IA"), s("-----", "BEGIN") + " alone",
        ):
            self.assertEqual(self.kinds(t), [], t)

    def test_placeholders_do_not_count(self):
        for t in (
            s("sk-", "ant-", "xxxxxxxxxxxxxxxxxxxxxxxx"),
            s("sk-", "your-key-goes-here-1234567890"),
            s("sk-", "example", "-example-example-example"),
            s("sk-", "ant-", "REDACTED", "-REDACTED-REDACTED"),
            "password = <your-password-here-please>",
            "token: your-token-goes-here-now",
            "api_key = process.env.SOME_LONG_VARIABLE_NAME",
            s("api", "_key", ": ", "example-example-example"),
        ):
            self.assertEqual(self.kinds(t), [], t)

    def test_line_numbers_and_redacted_excerpt(self):
        secret = s("sk-", "ant-", "api03-", "A1b2C3d4E5f6G7h8I9j0K1l2")
        text = "one\ntwo\nkey is " + secret + " ok\nfour\n"
        (f,) = safety.scan_text(text)
        self.assertEqual(f.line, 3)
        self.assertNotIn(secret, f.excerpt)
        self.assertNotIn("A1b2C3d4", f.excerpt)
        self.assertIn("[REDACTED]", f.excerpt)
        self.assertIn("key is", f.excerpt)

    def test_multiple_findings_in_order(self):
        a = s("gh", "p_", "A1b2C3d4E5f6G7h8I9j0K1l2M3n4O5p6Q7r8")
        b = s("AK", "IA", "ABCDEFGHIJKLMNOP")
        found = safety.scan_text(f"x\n{a}\ny\nz {b}\n")
        self.assertEqual([(f.kind, f.line) for f in found], [("github-token", 2), ("aws-key", 4)])

    def test_redact_replaces_every_match(self):
        a = s("sk-", "ant-", "api03-", "A1b2C3d4E5f6G7h8I9j0K1l2")
        b = s("password", ": ", "Zq8f3Lm92XvTn40PaBcD")
        out = safety.redact(f"first {a} then\n{b}\nend")
        self.assertNotIn(a, out)
        self.assertNotIn("Zq8f3Lm9", out)
        self.assertEqual(out.count("[REDACTED]"), 2)
        self.assertIn("password: [REDACTED]", out)
        self.assertEqual(safety.redact(out), out)
        self.assertEqual(safety.redact("nothing here"), "nothing here")

    def test_private_key_block_is_fully_redacted(self):
        block = s("-----", "BEGIN PRIVATE KEY", "-----\nAAAA1111BBBB2222\nCCCC3333DDDD4444\n-----", "END PRIVATE KEY", "-----")
        out = safety.redact("before\n" + block + "\nafter")
        self.assertNotIn("AAAA1111", out)
        self.assertNotIn("CCCC3333", out)
        self.assertTrue(out.startswith("before\n"))
        self.assertTrue(out.endswith("\nafter"))

    def test_repo_prose_and_our_own_sources_are_clean(self):
        files = [BRAIN_DOT / "DESIGN.md"]
        files += [BRAIN_DOT / "brainlib" / n for n in ("config.py", "lock.py", "gitops.py", "safety.py", "state.py", "sync.py")]
        files += [Path(__file__).resolve().parent / n for n in ("test_safety.py", "test_lock.py", "test_sync.py", "_gitfixture.py")]
        for f in files:
            if f.exists():
                self.assertEqual(safety.scan_text(f.read_text(encoding="utf-8")), [], str(f))


class ContentTests(unittest.TestCase):
    def test_clean_text_passes(self):
        self.assertEqual(safety.check_bytes("docs/a.md", "# hello\n\nplain text é\n".encode("utf-8")), [])

    def test_too_large(self):
        data = b"a" * (2 * 1024 * 1024 + 1)
        (p,) = safety.check_bytes("docs/big.md", data)
        self.assertIn("too large", p["reason"])
        self.assertEqual(safety.check_bytes("docs/ok.md", b"a" * (2 * 1024 * 1024)), [])
        self.assertTrue(safety.check_bytes("docs/huge.png", b"\x89PNG\r\n\x1a\n" + b"\0" * (3 * 1024 * 1024)))

    def test_binary_and_invalid_utf8(self):
        (p,) = safety.check_bytes("docs/x.bin", b"abc\0def")
        self.assertIn("binary", p["reason"])
        (p,) = safety.check_bytes("docs/x.md", b"caf\xe9 latin-1 only")
        self.assertIn("UTF-8", p["reason"])

    def test_images_only_under_docs(self):
        png = b"\x89PNG\r\n\x1a\n\0\0\0\rIHDR" + b"\0" * 64
        for ext in (".png", ".jpg", ".webp"):
            self.assertEqual(safety.check_bytes(f"docs/img/a{ext}", png), [], ext)
            self.assertTrue(safety.check_bytes(f"context/a{ext}", png), ext)
            self.assertTrue(safety.check_bytes(f"playbook/a{ext}", png), ext)
        self.assertTrue(safety.check_bytes("docs/a.gif", png))

    def test_secret_blocks_with_line(self):
        secret = s("sk-", "ant-", "api03-", "A1b2C3d4E5f6G7h8I9j0K1l2")
        (p,) = safety.check_bytes("docs/n.md", f"a\nb\n{secret}\n".encode())
        self.assertIn("secret", p["reason"])
        self.assertEqual(p["line"], 3)
        self.assertNotIn(secret, str(p))

    def test_check_file_reads_from_disk(self):
        import tempfile, os

        d = tempfile.mkdtemp(prefix="mmb-safety-")
        self.addCleanup(__import__("shutil").rmtree, d, True)
        f = Path(d) / "x.md"
        f.write_bytes(b"fine\n")
        self.assertEqual(safety.check_file(f, "docs/x.md"), [])
        f.write_bytes(b"a" * (3 * 1024 * 1024))
        self.assertIn("too large", safety.check_file(f, "docs/x.md")[0]["reason"])
        self.assertIn("cannot read", safety.check_file(Path(d) / "missing.md", "docs/missing.md")[0]["reason"])


if __name__ == "__main__":
    unittest.main()
