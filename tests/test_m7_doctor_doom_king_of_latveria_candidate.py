"""Deck 13 Doctor Doom, King of Latveria M7 review candidate: structural checks only, not approval."""
from __future__ import annotations
import hashlib
import json
import unittest
from collections import Counter
from pathlib import Path

from scripts import grixis_m7_decision_gate as gate

ROOT = Path(__file__).resolve().parents[1]
D = "Doctor_Doom__King_of_Latveria"
PACKET = ROOT / f"data/grixis/m7/decision_reviews/{D}.json"
BASE = ROOT / f"data/grixis/m7/baseline_sources/{D}_approved_source_2026-10-14.txt"
RAW = "c97bd448aa4b18d2f7ed15e5d67006ab320ed67ad3ed267e44150de472e1dc58"
CAND_RAW = "21d5ebd66352c34e9f7b786e71d121e9e0101f2426049741c2ddb1d95d1ab3fb"


class DoctorDoomKingOfLatveriaM7Tests(unittest.TestCase):
    def setUp(self):
        self.packet = json.loads(PACKET.read_text())
        self.registry = json.loads((ROOT / "data/grixis/registry.json").read_text())

    def test_gate_passes_as_review_candidate_not_approval(self):
        result = gate.verify_packet(self.packet, root=ROOT, registry=self.registry)
        self.assertTrue(result["owner_presentable"])
        self.assertEqual(result["new_swaps"], 6)
        self.assertEqual(self.packet["readiness"], "READY_FOR_EXACT_OWNER_APPROVAL_NOT_YET_APPROVED")
        self.assertFalse(self.packet["owner_authority"]["exact_candidate_owner_approved"])
        self.assertFalse(self.packet["owner_authority"]["canonical_deck_changed"])
        self.assertNotIn("baseline_provenance_exception", self.packet)

    def test_registry_matches_raw_and_vendored_copy_is_byte_identical(self):
        src = self.registry["decks"][D]["source"]
        self.assertEqual(src["recorded_sha256"], RAW)
        self.assertEqual(src["raw_sha256"], "sha256:" + RAW)
        self.assertIs(src["recorded_matches_raw"], True)
        self.assertEqual(self.packet["canonical_baseline_sha256"], RAW)
        self.assertEqual(hashlib.sha256(BASE.read_bytes()).hexdigest(), RAW)
        cand = ROOT / self.packet["final_candidate"]["path"]
        self.assertEqual(hashlib.sha256(cand.read_bytes()).hexdigest(), self.packet["final_candidate"]["sha256"])
        self.assertEqual(self.packet["final_candidate"]["sha256"], CAND_RAW)

    def test_exact_six_physical_swaps_against_vendored_and_canonical_md(self):
        cand = Counter(gate.parse_list(ROOT / self.packet["final_candidate"]["path"])[0])
        path, md = gate.canonical_source(ROOT, self.registry["decks"][D])
        for base in (Counter(gate.parse_list(BASE)[0]), Counter(gate.parse_list(path, source_markdown=md)[0])):
            self.assertEqual(sorted((cand - base).elements()), sorted(self.packet["final_changes"]["adds"]))
            self.assertEqual(sorted((base - cand).elements()), sorted(self.packet["final_changes"]["cuts"]))
            self.assertEqual(len(self.packet["final_changes"]["adds"]), 6)

    def test_single_commander_first_and_100_physical(self):
        lines = [x for x in (ROOT / self.packet["final_candidate"]["path"]).read_text().splitlines() if x.strip()]
        self.assertEqual(lines[0], "1x Doctor Doom, King of Latveria [Commander]")
        self.assertEqual(sum(1 for x in lines if x.endswith("[Commander]")), 1)
        self.assertFalse(any("[Companion]" in x for x in lines))
        self.assertEqual(sum(int(x.split("x ", 1)[0]) for x in lines), 100)
        rest = [x.split("x ", 1)[1] for x in lines[1:]]
        self.assertEqual(rest, sorted(rest, key=str.lower))

    def test_distinctness_note_and_commander_first_identity_recorded(self):
        # The closed M7 schema has no distinctness key; the overlap note lives in
        # commander_identity.anti_homogenization and is disclosed honestly.
        note = self.packet["commander_identity"]["anti_homogenization"]
        self.assertIn("commander-first", note)
        self.assertIn("the baseline shares 53 nonbasic names and the candidate also 53", note)
        self.assertIn("this candidate does not reduce that overlap", note)
        self.assertIn("Deck #12 Davros", note)
        self.assertIn("Owner-removed classes", note)

    def test_owner_removed_class_not_readded_and_flagged(self):
        adds = set(self.packet["final_changes"]["adds"])
        for card in ("Kefka, Court Mage", "Syphon Mind", "Dark Deal", "Tinybones, Trinket Thief"):
            self.assertNotIn(card, adds)
        judged = {c["card"]: c for c in self.packet["material_candidates"]}
        for card in ("Kefka, Court Mage", "Syphon Mind"):
            self.assertEqual(judged[card]["judgment"], "REJECT")
            self.assertIn("OWNER-REMOVED CLASS", judged[card]["source"])

    def test_power_bracket_tags_and_game_changers(self):
        v = self.packet["verification"]
        self.assertEqual(v["power_bracket"], 4)
        self.assertEqual(v["archidekt_tags"], ["Land Discard", "Villains", "Connive"])
        self.assertIn("candidate 7 (+Mox Diamond)", self.packet["commander_identity"]["natural_ceiling"])
        self.assertIn("No infinite is claimed", self.packet["commander_identity"]["natural_ceiling"])

    def test_no_approval_or_lock_markers_in_new_artifacts(self):
        for p in [PACKET, ROOT / self.packet["final_candidate"]["path"]]:
            text = p.read_text()
            self.assertNotIn("CANONICAL_LOCKED", text)
            self.assertNotIn('"APPROVED"', text)


if __name__ == "__main__":
    unittest.main()
