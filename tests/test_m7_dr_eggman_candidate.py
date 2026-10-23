"""Deck 15 Dr. Eggman M7 review candidate: structural checks only, not approval."""
from __future__ import annotations
import hashlib
import json
import unittest
from collections import Counter
from pathlib import Path

from scripts import grixis_m7_decision_gate as gate

ROOT = Path(__file__).resolve().parents[1]
D = "Dr__Eggman"
PACKET = ROOT / f"data/grixis/m7/decision_reviews/{D}.json"
BASE = ROOT / f"data/grixis/m7/baseline_sources/{D}_approved_source_2026-10-14.txt"
RAW = "ef34986253f71043e10c852b5f9f3ce79594fdfc1086b105f6744c3f639199c3"
CAND_RAW = "85bcd5a250c097a8b94322416c85272a8550728a43edc9a257b7fbd39823f792"


class DrEggmanM7Tests(unittest.TestCase):
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

    def test_exact_five_physical_swaps_against_vendored_and_canonical_md(self):
        cand = Counter(gate.parse_list(ROOT / self.packet["final_candidate"]["path"])[0])
        path, md = gate.canonical_source(ROOT, self.registry["decks"][D])
        for base in (Counter(gate.parse_list(BASE)[0]), Counter(gate.parse_list(path, source_markdown=md)[0])):
            self.assertEqual(sorted((cand - base).elements()), sorted(self.packet["final_changes"]["adds"]))
            self.assertEqual(sorted((base - cand).elements()), sorted(self.packet["final_changes"]["cuts"]))
            self.assertEqual(len(self.packet["final_changes"]["adds"]), 5)

    def test_single_commander_first_and_100_physical(self):
        lines = [x for x in (ROOT / self.packet["final_candidate"]["path"]).read_text().splitlines() if x.strip()]
        self.assertEqual(lines[0], "1x Dr. Eggman [Commander]")
        self.assertEqual(sum(1 for x in lines if x.endswith("[Commander]")), 1)
        self.assertFalse(any("[Companion]" in x for x in lines))
        self.assertEqual(sum(int(x.split("x ", 1)[0]) for x in lines), 100)
        self.assertEqual([x for x in lines if not x.startswith("1x ")], ["2x Island", "2x Mountain", "2x Swamp"])
        rest = [x.split("x ", 1)[1] for x in lines[1:]]
        self.assertEqual(rest, sorted(rest, key=str.lower))

    def test_distinctness_note_and_commander_first_identity_recorded(self):
        # The closed M7 schema has no distinctness key; the overlap note lives in
        # commander_identity.anti_homogenization and is disclosed honestly.
        note = self.packet["commander_identity"]["anti_homogenization"]
        self.assertIn("Commander-first", note)
        self.assertIn("Davros, Dalek Creator 45 -> 43", note)
        self.assertIn("Mishra, Eminent One 41 -> 41", note)
        self.assertIn("Mishra, Artificer Prodigy 40 -> 39", note)
        self.assertIn("The Valeyard 35 -> 34", note)
        self.assertIn("Blasphemous Act, Foundry Inspector", note)
        self.assertIn("Owner-removed classes", note)

    def test_owner_removed_class_not_readded_and_flagged(self):
        adds = set(self.packet["final_changes"]["adds"])
        removed = ("Megrim", "Steel Overseer", "Etherium Sculptor", "Mirrorworks", "Torrential Gearhulk",
                   "Imposter Mech", "Scrawling Crawler", "Damocles Base, Sword of Kang", "Chief of the Foundry",
                   "Raiders' Wake", "Tri-Sentinel")
        for card in removed:
            self.assertNotIn(card, adds)
        judged = {c["card"]: c for c in self.packet["material_candidates"]}
        for card in ("Steel Overseer", "Chief of the Foundry", "Imposter Mech", "Torrential Gearhulk", "Scrawling Crawler",
                     "Raiders' Wake"):
            self.assertEqual(judged[card]["judgment"], "REJECT")
            self.assertIn("OWNER-REMOVED", judged[card]["source"])

    def test_power_bracket_tags_and_game_changers(self):
        v = self.packet["verification"]
        self.assertEqual(v["power_bracket"], 4)
        self.assertEqual(v["archidekt_tags"], ["Villainous Choice", "Robots", "Artifact Cheat"])
        self.assertIn("Game Changers: 3 in baseline and candidate", self.packet["commander_identity"]["natural_ceiling"])
        self.assertIn("No infinite is claimed", self.packet["commander_identity"]["natural_ceiling"])

    def test_owner_retention_conflicts_flagged_with_staged_alternatives(self):
        judged = {c["card"]: c for c in self.packet["material_candidates"]}
        for card in ("Possession Engine", "Behemoth of Vault 0"):
            self.assertEqual(judged[card]["judgment"], "SELECT_ADD")
            self.assertIn("FLAG", " ".join(judged[card][k] for k in ("incumbent_opportunity_cost", "adversarial_downside")))
        rc = ROOT / "data/grixis/m7/research_challengers"
        for name, cut in (("four_keep_BlasphemousAct_no_PossessionEngine", "Blasphemous Act"),
                          ("five_keep_FoundryInspector_cut_WeaponsManufacturing", "Foundry Inspector")):
            alt = Counter(gate.parse_list(rc / f"{D}_{name}_20261023.txt")[0])
            self.assertEqual(alt[cut], 1)
            self.assertEqual(sum(alt.values()), 100)

    def test_no_approval_or_lock_markers_in_new_artifacts(self):
        for p in [PACKET, ROOT / self.packet["final_candidate"]["path"]]:
            text = p.read_text()
            self.assertNotIn("CANONICAL_LOCKED", text)
            self.assertNotIn('"APPROVED"', text)


if __name__ == "__main__":
    unittest.main()
