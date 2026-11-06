"""Tests for .brain/mcp_rag.py (server name continuum-rag)."""
from __future__ import annotations

import json
import os
import subprocess
import sys
import unittest
from pathlib import Path
from unittest import mock

BRAIN_TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BRAIN_TOOLS))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import mcp_rag  # noqa: E402
from brainlib.search import rag  # noqa: E402
from test_search import FakeBrain  # noqa: E402


class McpBase(unittest.TestCase):
    def setUp(self):
        self.fb = FakeBrain()
        patcher = mock.patch.dict(os.environ, {
            "MOCKMOB_BRAIN_STATE": str(self.fb.state), "MOCKMOB_BRAIN": str(self.fb.brain),
            "MOCKMOB_BRAIN_CODE_DIRS": str(self.fb.code), "MOCKMOB_BRAIN_NO_VECTORS": "1", "RAG_TODAY": "2026-11-06"})
        patcher.start()
        self.addCleanup(patcher.stop)
        self.addCleanup(self.fb.cleanup)

    def call(self, args, msg_id=7):
        reply = mcp_rag.handle({"jsonrpc": "2.0", "id": msg_id, "method": "tools/call",
                                "params": {"name": "rag_search", "arguments": args}})
        self.assertEqual(reply["id"], msg_id)
        return reply["result"]

    def payload(self, args):
        result = self.call(args)
        self.assertFalse(result["isError"], result)
        return json.loads(result["content"][0]["text"])


class TestProtocol(McpBase):
    def test_initialize_echoes_supported_versions(self):
        for version in ("2025-06-18", "2025-03-26", "2024-11-05"):
            r = mcp_rag.handle({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": version}})
            self.assertEqual(r["result"]["protocolVersion"], version)
            self.assertEqual(r["result"]["serverInfo"]["name"], "continuum-rag")
            self.assertIn("tools", r["result"]["capabilities"])
        r = mcp_rag.handle({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "1999-01-01"}})
        self.assertEqual(r["result"]["protocolVersion"], "2025-06-18")
        r = mcp_rag.handle({"jsonrpc": "2.0", "id": 1, "method": "initialize"})
        self.assertEqual(r["result"]["protocolVersion"], "2025-06-18")

    def test_notification_gets_no_reply_and_ping_works(self):
        self.assertIsNone(mcp_rag.handle({"jsonrpc": "2.0", "method": "notifications/initialized"}))
        self.assertEqual(mcp_rag.handle({"jsonrpc": "2.0", "id": 2, "method": "ping"})["result"], {})

    def test_tools_list_schema_matches_continuum(self):
        tools = mcp_rag.handle({"jsonrpc": "2.0", "id": 3, "method": "tools/list"})["result"]["tools"]
        self.assertEqual([t["name"] for t in tools], ["rag_search"])
        props = tools[0]["inputSchema"]["properties"]
        self.assertEqual(set(props), {"query", "project", "since", "until", "limit", "mode", "metadata", "confidence"})
        self.assertEqual(props["project"]["enum"], ["continuum", "mockmob", "all"])
        self.assertEqual(props["limit"]["maximum"], 5)
        self.assertEqual(props["mode"]["enum"], ["keyword", "hybrid"])
        self.assertEqual(tools[0]["inputSchema"]["required"], ["query"])

    def test_unknown_method_and_tool(self):
        self.assertEqual(mcp_rag.handle({"jsonrpc": "2.0", "id": 4, "method": "nope"})["error"]["code"], -32601)
        r = mcp_rag.handle({"jsonrpc": "2.0", "id": 5, "method": "tools/call", "params": {"name": "other", "arguments": {}}})
        self.assertEqual(r["error"]["code"], -32602)

    def test_serve_loop_survives_garbage_and_replies_in_order(self):
        import io
        lines = "\n".join([
            "not json",
            json.dumps({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2024-11-05"}}),
            json.dumps({"jsonrpc": "2.0", "method": "notifications/initialized"}),
            "",
            json.dumps({"jsonrpc": "2.0", "id": 2, "method": "tools/list"}),
        ]) + "\n"
        out = io.StringIO()
        mcp_rag.serve(io.StringIO(lines), out)
        replies = [json.loads(x) for x in out.getvalue().splitlines()]
        self.assertEqual(replies[0]["error"]["code"], -32700)
        self.assertEqual([r.get("id") for r in replies[1:]], [1, 2])


class TestRagSearchTool(McpBase):
    def test_returns_hits_with_continuum_response_shape(self):
        p = self.payload({"query": "razorpay refunds chargebacks"})
        for key in ("results", "index", "vectors_status", "confidence", "served_by"):
            self.assertIn(key, p)
        self.assertEqual(p["served_by"], "in-process")
        self.assertEqual(p["vectors_status"], "keyword only")
        self.assertEqual(p["results"][0]["file"], "brain/docs/specs/payments.md")
        self.assertEqual(p["confidence"]["scored"], False)
        self.assertTrue(p["index"]["refreshed"])  # first call builds the index
        self.assertEqual(p["index"]["keyword_refresh"], "complete")
        self.assertIn("index_age_minutes", p["index"])
        # metadata defaults on, as in the owner's Continuum
        self.assertIn("freshness", p["results"][0])

    def test_pulled_file_is_found_on_the_next_search(self):
        self.payload({"query": "razorpay"})
        (self.fb.brain / "docs" / "pulled.md").write_text("# Pulled\n\nThe axolotl plan arrived with the pull.\n", encoding="utf-8")
        p = self.payload({"query": "axolotl plan"})
        self.assertEqual(p["results"][0]["file"], "brain/docs/pulled.md")
        self.assertTrue(p["index"]["refreshed"])
        self.assertEqual(p["index"]["docs_changed"], 1)

    def test_limit_is_capped_at_five(self):
        p = self.payload({"query": "the code repo app next supabase", "limit": 50, "mode": "keyword"})
        self.assertLessEqual(len(p["results"]), 5)

    def test_filters_and_mode(self):
        p = self.payload({"query": "walrus", "since": "2026-11-03", "mode": "keyword"})
        self.assertEqual([r["file"] for r in p["results"]], ["brain/handoffs/mockmob/20261105T090000.000000Z-bbbbbbbb.md"])
        p = self.payload({"query": "walrus", "project": "continuum"})
        self.assertEqual(p["results"], [])
        self.assertIn("only the MockMob team brain", p["note"])
        p = self.payload({"query": "walrus", "project": "mockmob", "metadata": False})
        self.assertNotIn("freshness", p["results"][0])

    def test_hybrid_without_vectors_says_so(self):
        p = self.payload({"query": "razorpay refunds", "mode": "hybrid"})
        self.assertEqual(p["mode_used"], "keyword")
        self.assertIn("keyword only", p["note"])

    def test_confidence_without_vectors_is_unscored(self):
        p = self.payload({"query": "razorpay refunds", "confidence": True})
        self.assertFalse(p["confidence"]["scored"])
        self.assertTrue(p["results"])

    def test_errors_are_reported_not_raised(self):
        r = self.call({"query": "  "})
        self.assertTrue(r["isError"])
        self.assertIn("query is required", r["content"][0]["text"])
        r = self.call({"query": "x", "mode": "semantic"})
        self.assertTrue(r["isError"])
        self.assertIn("search failed", r["content"][0]["text"])
        r = self.call({})
        self.assertTrue(r["isError"])

    def test_refresh_failure_does_not_block_search(self):
        self.payload({"query": "razorpay"})
        with mock.patch.object(rag, "ensure_fresh", side_effect=RuntimeError("disk on fire")):
            p = self.payload({"query": "razorpay refunds"})
        self.assertEqual(p["index"]["error"], "disk on fire")
        self.assertTrue(p["results"])

    def test_empty_brain_returns_no_results_not_an_error(self):
        empty = self.fb.root / "empty"
        empty.mkdir()
        with mock.patch.dict(os.environ, {"MOCKMOB_BRAIN": str(empty), "MOCKMOB_BRAIN_CODE_DIRS": ""}):
            p = self.payload({"query": "anything at all"})
        self.assertEqual(p["results"], [])


class TestSubprocessRoundTrip(McpBase):
    def test_stdio_roundtrip(self):
        msgs = [
            {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2025-06-18"}},
            {"jsonrpc": "2.0", "method": "notifications/initialized"},
            {"jsonrpc": "2.0", "id": 2, "method": "tools/list"},
            {"jsonrpc": "2.0", "id": 3, "method": "tools/call",
             "params": {"name": "rag_search", "arguments": {"query": "quokka deploy checklist"}}},
        ]
        proc = subprocess.run([sys.executable, str(BRAIN_TOOLS / "mcp_rag.py")], input="\n".join(json.dumps(m) for m in msgs) + "\n",
                              capture_output=True, text=True, timeout=120, env=dict(os.environ))
        self.assertEqual(proc.returncode, 0, proc.stderr)
        replies = {r["id"]: r for r in (json.loads(x) for x in proc.stdout.splitlines())}
        self.assertEqual(sorted(replies), [1, 2, 3])
        self.assertEqual(replies[1]["result"]["serverInfo"]["name"], "continuum-rag")
        self.assertEqual(replies[2]["result"]["tools"][0]["name"], "rag_search")
        body = json.loads(replies[3]["result"]["content"][0]["text"])
        self.assertEqual(body["results"][0]["file"], "brain/playbook/memory/cto/MEMORY.md")


if __name__ == "__main__":
    unittest.main()
