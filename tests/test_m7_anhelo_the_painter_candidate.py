"""Deck #4 Anhelo, the Painter M7 review candidate: structural, not approval."""
from __future__ import annotations
import hashlib
import json
import unittest
from collections import Counter
from pathlib import Path

from scripts import grixis_m7_decision_gate as gate

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "data/grixis/m7/decision_reviews/Anhelo__the_Painter.json"
RAW = "8d5f8a9bd4fcdcd164aab63150c14dc69a814a4d9fd764876de3214d3adf9972"
HISTORICAL = "d19d94b8a96fb27a760c7b7d9181221f74bd61642d1d1dd7644fc1c59c09839e"


class AnheloThePainterM7Tests(unittest.TestCase):
    def setUp(self):
        self.packet = json.loads(PACKET.read_text())
        self.registry = json.loads((ROOT / "data/grixis/registry.json").read_text())

    def test_gate_passes_as_review_candidate_not_approval(self):
        result = gate.verify_packet(self.packet, root=ROOT, registry=self.registry)
        self.assertTrue(result["owner_presentable"])
        self.assertEqual(result["new_swaps"], 5)
        self.assertEqual(self.packet["readiness"], "READY_FOR_EXACT_OWNER_APPROVAL_NOT_YET_APPROVED")
        self.assertFalse(self.packet["owner_authority"]["exact_candidate_owner_approved"])
        self.assertFalse(self.packet["owner_authority"]["canonical_deck_changed"])

    def test_registry_and_hashes_untouched_and_bound_separately(self):
        src = self.registry["decks"]["Anhelo__the_Painter"]["source"]
        self.assertEqual(src["recorded_sha256"], HISTORICAL)
        self.assertEqual(src["raw_sha256"], "sha256:" + RAW)
        self.assertIs(src["recorded_matches_raw"], False)
        self.assertEqual(self.packet["canonical_baseline_sha256"], RAW)
        exc = self.packet["baseline_provenance_exception"]
        self.assertEqual(hashlib.sha256((ROOT / exc["vendored_source_copy"]).read_bytes()).hexdigest(), RAW)

    def test_exact_five_physical_swaps(self):
        base = Counter(n.split(" // ")[0] for n in gate.parse_list(
            ROOT / self.packet["baseline_provenance_exception"]["vendored_source_copy"])[0])
        cand = Counter(n.split(" // ")[0] for n in gate.parse_list(
            ROOT / self.packet["final_candidate"]["path"])[0])
        self.assertEqual(sorted((cand - base).elements()), sorted(self.packet["final_changes"]["adds"]))
        self.assertEqual(sorted((base - cand).elements()), sorted(self.packet["final_changes"]["cuts"]))

    def test_no_approval_or_lock_markers_in_new_artifacts(self):
        for p in [PACKET, ROOT / self.packet["final_candidate"]["path"]]:
            text = p.read_text()
            self.assertNotIn("CANONICAL_LOCKED", text)
            self.assertNotIn('"APPROVED"', text)


if __name__ == "__main__":
    unittest.main()
