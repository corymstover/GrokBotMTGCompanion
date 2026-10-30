"""Phase 7 broader relation test set (Batch 5).

Data-driven: every claim-bearing, non-structural edge in the committed multiverse graph must be
retrievable through mv_ask.lore(subject, relation, "out") with its canon grade intact, and the
confidence envelope must never report VERIFIED when a qualifying (non-CONFIRMED) grade is present.
Plus natural-language questions answered from the Batch 5 Phase 5 claim packs (KLD/AER, XLN/RIX,
AKH/HOU). These packs are PRELIMINARY_RESEARCH; the tests check retrieval fidelity, not canon approval.
"""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import mv_ask as A  # noqa: E402

GRAPH = json.loads((ROOT / "data" / "multiverse_graph" / "multiverse_graph.json").read_text(encoding="utf-8"))
NODES = {n["id"]: n for n in GRAPH["nodes"]}
CLAIM_EDGES = [e for e in GRAPH["edges"] if e.get("claim") and e["relation"] not in A.STRUCTURAL]


def _rows(env):
    return [r for v in env["result"].get("relations_by_status", {}).values() for r in v]


class EveryClaimEdgeIsAnswerable(unittest.TestCase):
    def test_no_duplicate_named_entities(self):
        # Two lore nodes of one type with one name make A.lore(name) resolve to only one of them (Batch 6c).
        seen = {}
        for n in GRAPH["nodes"]:
            kind = n["id"].split(":", 1)[0]
            if kind in {"card", "claim", "curated", "source"}:
                continue
            key = (kind, n["name"].strip().lower())
            with self.subTest(node=n["id"]):
                self.assertNotIn(key, seen, f"{n['id']} duplicates {seen.get(key)}")
            seen.setdefault(key, n["id"])

    def test_claim_edge_set_is_substantial(self):
        self.assertGreaterEqual(len(CLAIM_EDGES), 250)

    def test_each_edge_round_trips_with_grade_and_source(self):
        for e in CLAIM_EDGES:
            with self.subTest(claim=e["claim"], relation=e["relation"]):
                env = A.lore(NODES[e["from"]]["name"], e["relation"], "out")
                hits = [r for r in _rows(env) if r["claim"] == e["claim"] and r["node"] == e["to"]]
                self.assertTrue(hits, f"{e['from']} {e['relation']} {e['to']} not returned")
                self.assertEqual(hits[0]["status"], e["grade"])
                self.assertTrue(hits[0]["source_urls"], "answer without a cited source")

    def test_confidence_never_overstates(self):
        for e in CLAIM_EDGES:
            env = A.lore(NODES[e["from"]]["name"], e["relation"], "out")
            statuses = {r["status"] for r in _rows(env)}
            with self.subTest(claim=e["claim"]):
                if statuses & A.QUALIFYING:
                    self.assertEqual(env["confidence"], "QUALIFIED")
                    for s in statuses & A.QUALIFYING:
                        self.assertIn(s + "_PRESENT", env["flags"])
                elif "TIMELINE_CONTEXT_REQUIRED" in env["flags"]:
                    # A confirmed claim may still be confined to an erased/revised timeline.
                    self.assertEqual(env["confidence"], "QUALIFIED")
                else:
                    self.assertEqual(env["confidence"], "VERIFIED")

    def test_qualified_claims_carry_limitations(self):
        for e in CLAIM_EDGES:
            if e["grade"] in {"CANON_IMPLIED", "CANON_DISPUTED", "OPEN_QUESTION"} and e["claim"][:3] in {"KLD", "AER", "XLN", "AKH"}:
                env = A.lore(NODES[e["from"]]["name"], e["relation"], "out")
                hit = [r for r in _rows(env) if r["claim"] == e["claim"]][0]
                with self.subTest(claim=e["claim"]):
                    self.assertTrue(hit["limitation"])


class Batch5NaturalLanguage(unittest.TestCase):
    def _ask(self, q, claim, other, confidence="VERIFIED"):
        env = A.ask(q)
        self.assertEqual(env["confidence"], confidence, q)
        hits = [r for r in _rows(env) if r["claim"] == claim]
        self.assertTrue(hits, f"{q}: {claim} missing")
        self.assertEqual(hits[0]["node"], other)
        self.assertTrue(all("magic.wizards.com" in u for u in hits[0]["source_urls"]))
        return env

    def test_who_killed_razaketh(self):
        self._ask("Who killed Razaketh?", "AKH006", "character:liliana_vess")

    def test_who_created_the_immortal_sun(self):
        self._ask("Who created the Immortal Sun?", "XLN008", "character:azor")

    def test_who_defeated_ugin_uses_defeated_fallback(self):
        env = self._ask("Who defeated Ugin?", "XLN010", "character:nicol_bolas")
        self.assertEqual(env["route"], "ask->lore:defeated")

    def test_who_created_heart_of_kiran_reports_designed(self):
        env = self._ask("Who created Heart of Kiran?", "AER004", "character:kiran_nalaar")
        self.assertEqual(env["route"], "ask->lore:designed")

    def test_unknown_still_not_found(self):
        self.assertEqual(A.ask("Who defeated Zzyzx the Unwritten?")["confidence"], "NOT_FOUND")


if __name__ == "__main__":
    unittest.main()
