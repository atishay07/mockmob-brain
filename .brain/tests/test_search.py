"""Tests for brainlib/search/rag.py: sources, incremental refresh, filters, keyword search, optional vectors."""
from __future__ import annotations

import os
import shutil
import sys
import tempfile
import time
import unittest
from pathlib import Path
from unittest import mock

BRAIN_TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BRAIN_TOOLS))
from brainlib.search import rag  # noqa: E402

SCRATCH_MODELS = (r"C:\Users\atish\AppData\Local\Temp\claude\dc2af5953cc5fcb1\204dccba-6bad-4e60-8bb6-73166cbdb15c"
                  r"\scratchpad\models")


def write(path: Path, text: str, mtime: float | None = None) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    if mtime is not None:
        os.utime(path, (mtime, mtime))
    return path


class FakeBrain:
    """A small brain repo plus a code dir under one temp root."""

    def __init__(self):
        self.root = Path(tempfile.mkdtemp(prefix="mmbrain-search-"))
        self.brain = self.root / "brain"
        self.code = self.root / "code"
        self.state = self.root / "state"
        b = self.brain
        write(b / "TEAM.md", "# Team\n\nAtishay owns product. The CTO owns infrastructure and releases.\n")
        write(b / "AGENTS.md", "# Agent rules\n\nSave a handover before you stop.\n")
        write(b / "README.md", "# MockMob brain\n\nHumans read this first.\n")
        write(b / "CLAUDE.md", "# Same rules\n\nzebrafinch marker not indexed.\n")  # not a brain source
        write(b / "docs" / "NOW.md", "# Now\n\nWe are shipping the quiz arena redesign. Blocked on emulator walk.\n")
        write(b / "docs" / "STATUS.md", "# Status\n\nUpdated: 2026-09-01\n\nOld status text about onboarding.\n")
        write(b / "docs" / "specs" / "payments.md",
              "# Payments spec\n\nRazorpay handles refunds and chargebacks. Build tag v2.14.7 shipped to Play.\n")
        write(b / "context" / "priorities.md", "# Priorities\n\nUnlimited mocks is the headline feature.\n")
        write(b / "handoffs" / "mockmob" / "20261101T090000.000000Z-aaaaaaaa.md",
              "---\ntitle: Early handover\ntype: checkpoint\n---\n\n## task\n\nwalrus migration of the question bank\n")
        write(b / "handoffs" / "mockmob" / "20261105T090000.000000Z-bbbbbbbb.md",
              "---\ntitle: Late handover\ntype: checkpoint\n---\n\n## task\n\nwalrus cleanup of the arena screens\n")
        write(b / "handoffs" / "mockmob" / "20261105T090000.000000Z-bbbbbbbb.json", '{"task": "jsononlymarker"}')
        write(b / "handoffs" / "campusos" / "20261105T090000.000000Z-cccccccc.md", "# other project aardvark\n")
        write(b / "playbook" / "memory" / "cto" / "MEMORY.md", "- [Deploy rule](deploy.md): quokka deploy checklist\n")
        write(b / "random" / "notes.md", "# stray\n\nokapi stray folder not indexed\n")
        c = self.code
        for name in rag.CODE_TOP_FILES:
            write(c / name, f"# {name} of the code repo\n\nThe app uses Next.js and Supabase. {name}\n")
        write(c / "OTHER.md", "# other root file\n\nibexmarker\n")
        write(c / "docs" / "guide.md", "# Guide\n\nHow the question pipeline verifies each item.\n")
        write(c / "docs" / "deep" / "arch.md", "# Architecture\n\nThe pipeline writes to Postgres.\n")
        write(c / "docs" / "brain" / "hidden.md", "# Hidden\n\ncapybaramarker moved to the brain repo.\n")
        write(c / "docs" / "node_modules" / "x.md", "# dep\n\npangolinmarker\n")
        write(c / "src" / "readme.md", "# src\n\nsrcmarker\n")

    def cleanup(self):
        shutil.rmtree(self.root, ignore_errors=True)


class SearchTestBase(unittest.TestCase):
    use_vectors = False

    def setUp(self):
        self.fb = FakeBrain()
        env = {
            "MOCKMOB_BRAIN_STATE": str(self.fb.state),
            "MOCKMOB_BRAIN": str(self.fb.brain),
            "MOCKMOB_BRAIN_CODE_DIRS": str(self.fb.code),
            "RAG_TODAY": "2026-11-06",
        }
        if not self.use_vectors:
            env["MOCKMOB_BRAIN_NO_VECTORS"] = "1"
        patcher = mock.patch.dict(os.environ, env)
        patcher.start()
        self.addCleanup(patcher.stop)
        if self.use_vectors:
            os.environ.pop("MOCKMOB_BRAIN_NO_VECTORS", None)
        self.addCleanup(self.fb.cleanup)

    def docs(self) -> set[str]:
        con = rag.connect()
        try:
            return {r["id"] for r in con.execute("SELECT id FROM docs WHERE skipped=''")}
        finally:
            con.close()

    def files(self, query, **kw) -> list[str]:
        return [r["file"] for r in rag.search(query, **kw)]


class TestSources(SearchTestBase):
    def test_source_ids(self):
        got = {doc_id for _, doc_id, _ in rag.build_sources()}
        expected = {
            "brain/TEAM.md", "brain/AGENTS.md", "brain/README.md",
            "brain/docs/NOW.md", "brain/docs/STATUS.md", "brain/docs/specs/payments.md",
            "brain/context/priorities.md",
            "brain/handoffs/mockmob/20261101T090000.000000Z-aaaaaaaa.md",
            "brain/handoffs/mockmob/20261105T090000.000000Z-bbbbbbbb.md",
            "brain/playbook/memory/cto/MEMORY.md",
            "mockmob/AGENTS.md", "mockmob/CLAUDE.md", "mockmob/DESIGN.md", "mockmob/PRODUCT.md", "mockmob/README.md",
            "mockmob/docs/guide.md", "mockmob/docs/deep/arch.md",
        }
        self.assertEqual(got, expected)

    def test_all_sources_are_project_mockmob(self):
        self.assertEqual({p for p, _, _ in rag.build_sources()}, {"mockmob"})

    def test_two_code_dirs_first_doc_id_wins(self):
        second = self.fb.root / "code2"
        write(second / "README.md", "# second readme\n")
        write(second / "docs" / "extra.md", "# extra\n")
        got = [d for _, d, _ in rag.build_sources(code_dirs=[self.fb.code, second])]
        self.assertEqual(got.count("mockmob/README.md"), 1)
        self.assertIn("mockmob/docs/extra.md", got)

    def test_missing_code_dir_is_fine(self):
        got = [d for _, d, _ in rag.build_sources(code_dirs=[self.fb.root / "nope"])]
        self.assertIn("brain/TEAM.md", got)
        self.assertFalse([d for d in got if d.startswith("mockmob/")])

    def test_db_and_models_live_under_state_dir(self):
        self.assertEqual(rag.default_db_path(), self.fb.state / "index" / "rag.sqlite")
        with mock.patch.dict(os.environ, {"MOCKMOB_BRAIN_MODELS": str(self.fb.root / "m")}):
            self.assertEqual(rag.models_dir(), self.fb.root / "m")
        self.assertEqual(rag.models_dir(), self.fb.state / "models")

    def test_resolve_brain_dir_order(self):
        self.assertEqual(rag.resolve_brain_dir(), self.fb.brain)
        with mock.patch.dict(os.environ):
            os.environ.pop("MOCKMOB_BRAIN")
            write(self.fb.state / "config.json", '{"brain_dir": "%s"}' % str(self.fb.root / "cfgbrain").replace("\\", "/"))
            self.assertEqual(rag.resolve_brain_dir(), self.fb.root / "cfgbrain")


class TestIndexAndKeyword(SearchTestBase):
    def test_index_then_search(self):
        stats = rag.build_index()
        self.assertTrue(stats["complete"])
        self.assertEqual(stats["docs"], 17)
        self.assertEqual(stats["by_project"], {"mockmob": 17})
        self.assertIn("brain/docs/specs/payments.md", self.files("razorpay refunds chargebacks"))
        self.assertEqual(self.files("razorpay refunds")[0], "brain/docs/specs/payments.md")
        self.assertEqual(self.files("quokka")[0], "brain/playbook/memory/cto/MEMORY.md")
        self.assertEqual(self.files("pipeline verifies")[0], "mockmob/docs/guide.md")

    def test_excluded_files_are_not_found(self):
        rag.build_index()
        for word in ("zebrafinch", "jsononlymarker", "aardvark", "okapi", "ibexmarker", "capybaramarker",
                     "pangolinmarker", "srcmarker"):
            self.assertEqual(self.files(word), [], word)

    def test_result_shape(self):
        rag.build_index()
        r = rag.search("quiz arena redesign", limit=3)[0]
        for key in ("rank", "file", "title", "project", "line", "modified", "score", "matched_terms", "excerpt"):
            self.assertIn(key, r)
        self.assertEqual(r["file"], "brain/docs/NOW.md")
        self.assertEqual(r["title"], "Now")
        self.assertEqual(r["project"], "mockmob")

    def test_front_matter_title_for_handovers(self):
        rag.build_index()
        hits = {r["file"]: r["title"] for r in rag.search("walrus", limit=5)}
        self.assertEqual(hits["brain/handoffs/mockmob/20261105T090000.000000Z-bbbbbbbb.md"], "Late handover")

    def test_keyword_search_for_continuum_search(self):
        out = rag.keyword_search("walrus cleanup", limit=5)
        self.assertTrue(out)
        self.assertEqual(set(out[0]), {"score", "file", "line", "title", "excerpt"})
        # brain files are relative to the brain repo (no "brain/" prefix), code files carry "mockmob/"
        self.assertEqual(out[0]["file"], "handoffs/mockmob/20261105T090000.000000Z-bbbbbbbb.md")
        self.assertTrue((self.fb.brain / out[0]["file"]).is_file())
        code = rag.keyword_search("question pipeline verifies", limit=5)
        self.assertEqual(code[0]["file"], "mockmob/docs/guide.md")
        self.assertLessEqual(len(rag.keyword_search("brain", limit=50)), 20)

    def test_keyword_search_empty_query_terms(self):
        rag.build_index()
        self.assertEqual(rag.keyword_search("the and of"), [])

    def test_secret_like_file_is_skipped_and_stays_skipped(self):
        write(self.fb.brain / "docs" / "leak.md", "# Leak\n\napi_" + "key = " + "abcdefghijklmnop1234567890\nflamingomarker\n")
        stats = rag.build_index()
        self.assertEqual(stats["docs_skipped_secret"], 1)
        self.assertEqual(self.files("flamingomarker"), [])
        self.assertNotIn("brain/docs/leak.md", self.docs())
        again = rag.ensure_fresh(db_path=None, background=False)
        self.assertFalse(again["refreshed"])  # remembered: not re-read on every search
        # once the secret is removed the doc is indexed
        write(self.fb.brain / "docs" / "leak.md", "# Leak\n\nflamingomarker without the key\n", mtime=time.time() + 5)
        rag.ensure_fresh(background=False)
        self.assertIn("brain/docs/leak.md", self.files("flamingomarker"))

    def test_vectors_status_keyword_only_without_vectors(self):
        self.assertFalse(rag.vectors_available())
        self.assertEqual(rag.vectors_status(), "keyword only")
        info = rag.ensure_fresh(background=True)
        self.assertEqual(info["vectors_status"], "keyword only")
        self.assertFalse(info["vectors_refreshing"])
        self.assertFalse(info["worker_started"])

    def test_hybrid_falls_back_to_keyword(self):
        rag.build_index()
        out = rag.search_ex("razorpay refunds", mode="hybrid")
        self.assertEqual(out["mode_used"], "keyword")
        self.assertIn("keyword only", out["note"])
        self.assertEqual(out["results"][0]["file"], "brain/docs/specs/payments.md")

    def test_bad_mode_raises(self):
        rag.build_index()
        with self.assertRaises(ValueError):
            rag.search("x", mode="semantic")


class TestIncrementalRefresh(SearchTestBase):
    """Spec item 14: a pulled file is found on the next search without a full rebuild."""

    def chunk_ids(self, doc_id):
        con = rag.connect()
        try:
            return [r[0] for r in con.execute("SELECT id FROM chunks WHERE doc_id=? ORDER BY id", (doc_id,))]
        finally:
            con.close()

    def test_first_refresh_builds_then_unchanged_is_noop(self):
        first = rag.ensure_fresh(background=False)
        self.assertTrue(first["refreshed"])
        self.assertEqual(first["keyword_refresh"], "complete")
        self.assertEqual(first["docs"], 17)
        second = rag.ensure_fresh(background=False)
        self.assertFalse(second["refreshed"])

    def test_added_changed_deleted_file(self):
        rag.ensure_fresh(background=False)
        keep_before = self.chunk_ids("brain/docs/specs/payments.md")
        self.assertTrue(keep_before)

        # add (a file that arrived with a pull)
        pulled = write(self.fb.brain / "docs" / "decisions" / "arrival.md", "# Arrival\n\nThe narwhal decision was taken today.\n")
        info = rag.ensure_fresh(background=False)
        self.assertTrue(info["refreshed"])
        self.assertEqual(info["docs_changed"], 1)
        self.assertEqual(self.files("narwhal")[0], "brain/docs/decisions/arrival.md")
        self.assertEqual(self.chunk_ids("brain/docs/specs/payments.md"), keep_before)  # no full rebuild

        # change (new bytes, later mtime)
        write(pulled, "# Arrival\n\nThe manatee decision replaced it.\n", mtime=time.time() + 10)
        info = rag.ensure_fresh(background=False)
        self.assertTrue(info["refreshed"])
        self.assertEqual(info["docs_changed"], 1)
        self.assertEqual(self.files("narwhal"), [])
        self.assertEqual(self.files("manatee")[0], "brain/docs/decisions/arrival.md")
        self.assertEqual(self.chunk_ids("brain/docs/specs/payments.md"), keep_before)

        # delete
        pulled.unlink()
        info = rag.ensure_fresh(background=False)
        self.assertTrue(info["refreshed"])
        self.assertEqual(info["docs_removed"], 1)
        self.assertEqual(self.files("manatee"), [])
        self.assertNotIn("brain/docs/decisions/arrival.md", self.docs())
        con = rag.connect()
        try:  # nothing left behind in any table
            self.assertEqual(con.execute("SELECT COUNT(*) FROM chunks WHERE doc_id='brain/docs/decisions/arrival.md'").fetchone()[0], 0)
            self.assertEqual(con.execute("SELECT COUNT(*) FROM chunks_fts").fetchone()[0],
                             con.execute("SELECT COUNT(*) FROM chunks").fetchone()[0])
        finally:
            con.close()

    def test_touch_without_change_is_metadata_only(self):
        rag.ensure_fresh(background=False)
        target = self.fb.brain / "docs" / "NOW.md"
        before = self.chunk_ids("brain/docs/NOW.md")
        os.utime(target, (time.time() + 20, time.time() + 20))
        self.assertTrue(rag.changed_on_disk())
        stats = rag.index()
        self.assertEqual(stats["docs_metadata_only"], 1)
        self.assertEqual(stats["docs_changed"], 0)
        self.assertEqual(self.chunk_ids("brain/docs/NOW.md"), before)

    def test_code_repo_docs_are_picked_up_too(self):
        rag.ensure_fresh(background=False)
        write(self.fb.code / "docs" / "new-spec.md", "# New spec\n\nThe pelican feature flag.\n")
        rag.ensure_fresh(background=False)
        self.assertEqual(self.files("pelican")[0], "mockmob/docs/new-spec.md")

    def test_budget_cut_is_partial_and_next_call_continues(self):
        rag.ensure_fresh(background=False, budget_s=0.0)  # budget already spent: nothing is indexed
        info = rag.freshness()
        self.assertIsNone(info["last_indexed_at"])  # a partial run leaves the index stale
        done = rag.ensure_fresh(background=False)
        self.assertTrue(done["refreshed"])
        self.assertEqual(done["docs"], 17)

    def test_index_lock_held_skips_refresh(self):
        lock = rag._lock_path(None, "index")
        lock.parent.mkdir(parents=True, exist_ok=True)
        self.assertTrue(rag._acquire(lock))
        try:
            info = rag.ensure_fresh(background=False)
            self.assertFalse(info["refreshed"])
            self.assertEqual(info["reason"], "refresh already running")
        finally:
            rag._release(lock)

    def test_embed_lock_is_separate_from_index_lock(self):
        lock = rag._lock_path(None, "embed")
        lock.parent.mkdir(parents=True, exist_ok=True)
        self.assertTrue(rag._acquire(lock))
        try:
            self.assertTrue(rag.embedding_running())
            self.assertEqual(rag.embed_in_background()["reason"], "embedding already running")
            self.assertTrue(rag.ensure_fresh(background=False)["refreshed"])  # keyword refresh is not blocked
        finally:
            rag._release(lock)
        self.assertFalse(rag.embedding_running())

    def test_stale_lock_is_broken(self):
        lock = rag._lock_path(None, "embed")
        lock.parent.mkdir(parents=True, exist_ok=True)
        lock.write_text("999999")
        old = time.time() - rag.LOCK_STALE_SECONDS - 60
        os.utime(lock, (old, old))
        self.assertFalse(rag.embedding_running())
        self.assertTrue(rag._acquire(lock))
        rag._release(lock)


class TestFiltersAndMetadata(SearchTestBase):
    def setUp(self):
        super().setUp()
        rag.build_index()

    def test_project_filter(self):
        self.assertTrue(self.files("walrus", project="mockmob"))
        self.assertTrue(self.files("walrus", project="all"))
        self.assertEqual(self.files("walrus", project="continuum"), [])

    def test_since_until_use_the_handover_stamp_not_clone_time(self):
        both = set(self.files("walrus", limit=5))
        self.assertEqual(len(both), 2)
        late = self.files("walrus", since="2026-11-03", limit=5)
        self.assertEqual(late, ["brain/handoffs/mockmob/20261105T090000.000000Z-bbbbbbbb.md"])
        early = self.files("walrus", until="2026-11-03", limit=5)
        self.assertEqual(early, ["brain/handoffs/mockmob/20261101T090000.000000Z-aaaaaaaa.md"])
        self.assertEqual(self.files("walrus", since="2026-11-02", until="2026-11-04", limit=5), [])

    def test_since_filters_by_mtime_for_undated_names(self):
        old = time.mktime((2026, 1, 5, 12, 0, 0, 0, 0, -1))
        write(self.fb.brain / "docs" / "ancient.md", "# Ancient\n\nmammothnote lives here\n", mtime=old)
        rag.ensure_fresh(background=False)
        self.assertEqual(self.files("mammothnote", until="2026-02-01"), ["brain/docs/ancient.md"])
        self.assertEqual(self.files("mammothnote", since="2026-02-01"), [])

    def test_freshness_metadata(self):
        res = {r["file"]: r for r in rag.search("old status onboarding", meta=True, limit=5)}
        status = res["brain/docs/STATUS.md"]
        self.assertEqual(status["source_date"], "2026-09-01")
        self.assertEqual(status["source_date_basis"], "header")
        self.assertTrue(status["state_doc"])
        self.assertTrue(status["stale"])
        self.assertEqual(status["freshness"], "stale, verify")
        self.assertEqual(status["age_days"], 66)
        now = rag.search("quiz arena redesign", meta=True)[0]
        self.assertEqual(now["file"], "brain/docs/NOW.md")
        self.assertEqual(now["freshness"], "current")
        handover = rag.search("walrus cleanup", meta=True)[0]
        self.assertEqual(handover["source_date"], "2026-11-05")
        self.assertEqual(handover["source_date_basis"], "filename")

    def test_meta_off_removes_metadata_fields(self):
        r = rag.search("quiz arena redesign", meta=False)[0]
        self.assertNotIn("freshness", r)
        self.assertNotIn("exact_match", r)

    def test_exact_literal_route(self):
        res = rag.search("which build went out as v2.14.7", meta=True, limit=3)
        self.assertEqual(res[0]["file"], "brain/docs/specs/payments.md")
        self.assertEqual(res[0]["exact_match"], ["v2.14.7"])
        res = rag.search("what is in docs/specs/payments.md", meta=True, limit=3)
        self.assertEqual(res[0]["file"], "brain/docs/specs/payments.md")

    def test_name_route_pulls_the_state_doc(self):
        res = rag.search("current project status", meta=True, limit=3)
        self.assertIn("brain/docs/STATUS.md", [r["file"] for r in res])

    def test_current_query_prefers_newer_state(self):
        res = rag.search("latest status of onboarding and arena redesign", meta=True, limit=5)
        self.assertEqual(res[0]["query_mode"], "current")

    def test_supersedes(self):
        write(self.fb.brain / "docs" / "plan-v2.md", "# Plan v2\n\nSupersedes: docs/specs/payments.md\n\ndolphin plan\n")
        rag.ensure_fresh(background=False)
        res = {r["file"]: r for r in rag.search("razorpay refunds chargebacks", meta=True, limit=5)}
        self.assertEqual(res["brain/docs/specs/payments.md"]["freshness"], "superseded")
        self.assertEqual(res["brain/docs/specs/payments.md"]["superseded_by"], ["brain/docs/plan-v2.md"])

    def test_extract_literals(self):
        kinds = {l["text"]: l["kind"] for l in rag.extract_literals('see `foo bar` in docs/x.md at v1.2.3 for ABC-123')}
        self.assertEqual(kinds["foo bar"], "quoted")
        self.assertEqual(kinds["docs/x.md"], "path")
        self.assertEqual(kinds["v1.2.3"], "version")
        self.assertEqual(kinds["ABC-123"], "request_id")

    def test_chunking_keeps_line_numbers(self):
        long_doc = "# Big\n\n" + "\n".join(f"line {i} filler text here" for i in range(400)) + "\n\n## Tail\n\nzirconiummarker at the end\n"
        write(self.fb.brain / "docs" / "big.md", long_doc)
        rag.ensure_fresh(background=False)
        r = rag.search("zirconiummarker")[0]
        self.assertEqual(r["file"], "brain/docs/big.md")
        self.assertGreater(r["line"], 1)
        lines = long_doc.splitlines()
        self.assertIn("zirconiummarker", "\n".join(lines[r["line"] - 1:r["line"] + 60]))


class TestCli(SearchTestBase):
    def test_main_index_and_search(self):
        import io
        from contextlib import redirect_stdout
        buf = io.StringIO()
        with redirect_stdout(buf):
            self.assertEqual(rag.main(["index"]), 0)
            self.assertEqual(rag.main(["stats"]), 0)
            self.assertEqual(rag.main(["search", "razorpay refunds"]), 0)
        self.assertIn("brain/docs/specs/payments.md", buf.getvalue())

    def test_script_entry_runs_embed_pending_without_package_context(self):
        """The detached worker runs rag.py as a plain script; with no fastembed it must report, not crash."""
        import subprocess
        rag.build_index()
        env = dict(os.environ)
        proc = subprocess.run([sys.executable, str(Path(rag.__file__).resolve()), "embed-pending"],
                              capture_output=True, text=True, env=env, timeout=60)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("embedded", proc.stdout)


@unittest.skipUnless(rag.importlib.util.find_spec("fastembed") is not None and rag.importlib.util.find_spec("numpy") is not None,
                     "fastembed not installed")
class TestVectors(SearchTestBase):
    use_vectors = True

    def setUp(self):
        super().setUp()
        Path(SCRATCH_MODELS).mkdir(parents=True, exist_ok=True)
        patcher = mock.patch.dict(os.environ, {"MOCKMOB_BRAIN_MODELS": SCRATCH_MODELS})
        patcher.start()
        self.addCleanup(patcher.stop)
        rag._MODEL.clear()
        self.addCleanup(rag._MODEL.clear)

    def test_embed_then_hybrid_search(self):
        write(self.fb.brain / "docs" / "refunds.md", "# Refund policy\n\nWhen a customer asks for their money back we return the payment within seven days.\n")
        write(self.fb.brain / "docs" / "emulator.md", "# Emulator\n\nThe Android emulator gets at most three gigabytes of memory.\n")
        rag.build_index()
        self.assertGreater(rag.pending_embeddings(), 0)
        result = rag.embed_in_background()
        self.assertGreater(result.get("embedded", 0), 0, result)
        self.assertEqual(rag.pending_embeddings(), 0)
        self.assertEqual(rag.vectors_status(), "vectors current")
        out = rag.search_ex("how much RAM can the virtual phone use", mode="hybrid", meta=False)
        self.assertEqual(out["mode_used"], "hybrid")
        self.assertEqual(out["results"][0]["file"], "brain/docs/emulator.md")
        # a vector search is also incremental: a new file leaves pending chunks and no vectors are lost
        write(self.fb.brain / "docs" / "late.md", "# Late\n\nA late file about giraffes.\n")
        info = rag.ensure_fresh(background=False)
        self.assertGreater(info["pending_embeddings"], 0)
        self.assertEqual(info["vectors_status"], "vectors refreshing")
        self.assertGreater(rag.stats()["vectors"], 0)

    def test_detached_worker_embeds_in_background(self):
        rag.build_index()
        rag._spawn_embed_worker(None)
        deadline = time.time() + 180
        while time.time() < deadline and rag.pending_embeddings() > 0:
            time.sleep(1.0)
        self.assertEqual(rag.pending_embeddings(), 0, "detached worker did not finish")
        deadline = time.time() + 10
        while time.time() < deadline and rag.embedding_running():
            time.sleep(0.2)
        self.assertFalse(rag.embedding_running())


if __name__ == "__main__":
    unittest.main()
