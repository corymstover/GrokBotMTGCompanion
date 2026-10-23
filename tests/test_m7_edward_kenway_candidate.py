"""Deck 17 Edward Kenway M7 review candidate: structural checks only, not approval."""
from __future__ import annotations
import hashlib
import json
import unittest
from collections import Counter
from pathlib import Path

from scripts import grixis_m7_decision_gate as gate

ROOT = Path(__file__).resolve().parents[1]
D = "Edward_Kenway"
PACKET = ROOT / f"data/grixis/m7/decision_reviews/{D}.json"
BASE = ROOT / f"data/grixis/m7/baseline_sources/{D}_approved_source_2026-10-14.txt"
RAW = "a08d3bc9c283415f1579c493eccb3febd7d10dea3777bf3dc50cfbc0dbed4019"
CAND_RAW = "f3aad8e7da61996f27f423b6f0a2c7b33ea68acd9afbd57fb5e8a368b4a88aad"
RC = ROOT / "data/grixis/m7/research_challengers"


class EdwardKenwayM7Tests(unittest.TestCase):
    def setUp(self):
        self.packet = json.loads(PACKET.read_text())
        self.registry = json.loads((ROOT / "data/grixis/registry.json").read_text())
        self.judged = {c["card"]: c for c in self.packet["material_candidates"]}

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
        self.assertEqual(lines[0], "1x Edward Kenway [Commander]")
        self.assertEqual(sum(1 for x in lines if x.endswith("[Commander]")), 1)
        self.assertFalse(any("[Companion]" in x for x in lines))
        self.assertEqual(sum(int(x.split("x ", 1)[0]) for x in lines), 100)
        self.assertEqual([x for x in lines if not x.startswith("1x ")], ["2x Island", "2x Swamp"])
        self.assertIn("1x Mountain", lines)
        rest = [x.split("x ", 1)[1] for x in lines[1:]]
        self.assertEqual(rest, sorted(rest, key=str.lower))

    def test_distinctness_note_and_commander_first_identity_recorded(self):
        note = self.packet["commander_identity"]["anti_homogenization"]
        self.assertIn("Commander-first", note)
        for s in ("Admiral Beckett Brass 50 -> 49", "Admiral Brass, Unsinkable 48 -> 46",
                  "Don Andres, the Renegade 49 -> 47", "Nathan Drake, Treasure Hunter 47 -> 45"):
            self.assertIn(s, note)
        self.assertIn("Owner-removed or rejected cards and classes", note)

    def test_owner_removed_class_not_readded_and_no_owner_keep_cut(self):
        adds = set(self.packet["final_changes"]["adds"])
        cuts = set(self.packet["final_changes"]["cuts"])
        removed = ("Sulfur Falls", "Revel in Riches", "Setzer, Wandering Gambler", "Mechanized Production",
                   "Magmatic Galleon", "Reckoner Bankbuster", "Mobilizer Mech", "Malcolm, Alluring Scoundrel",
                   "Path of Ancestry", "Corsair Captain", "Fell Flagship", "Treasure Map", "Weatherlight")
        for card in removed:
            self.assertNotIn(card, adds)
        for keep in ("Fateful Discovery", "Imperial Seal", "Time Sieve", "Academy Manufactor"):
            self.assertNotIn(keep, cuts)
        self.assertEqual(self.judged["Path of Ancestry"]["judgment"], "REJECT")
        self.assertEqual(self.judged["Eagle Vision"]["judgment"], "RETAIN_ALTERNATIVE")
        self.assertEqual(self.judged["Chandra, Spark Hunter"]["judgment"], "RETAIN_ALTERNATIVE")
        self.assertEqual(self.judged["Dragon's Smile"]["judgment"], "EXCLUDE_INVALID")

    def test_power_bracket_tags_game_changers_and_combo_disclosure(self):
        v = self.packet["verification"]
        self.assertEqual(v["power_bracket"], 4)
        self.assertEqual(v["archidekt_tags"], ["Vehicles", "Pirates", "Treasure"])
        ceiling = self.packet["commander_identity"]["natural_ceiling"]
        self.assertIn("Game Changers: 10 in baseline and candidate", ceiling)
        self.assertIn("the same 6 complete combos in both lists", ceiling)
        self.assertIn("43 -> 45", ceiling)
        self.assertIn("no unconditional infinite is claimed", ceiling)

    def test_pass_c_alternatives_staged_as_complete_hundreds(self):
        fat = Counter(gate.parse_list(RC / f"{D}_PassC_MirkwoodBats_over_FatefulDiscovery_keep_Fellwar_20261023.txt")[0])
        self.assertEqual((fat["Mirkwood Bats"], fat["Fateful Discovery"], fat["Fellwar Stone"], sum(fat.values())), (1, 0, 1, 100))
        adr = Counter(gate.parse_list(RC / f"{D}_PassC_MirkwoodBats_over_Adrestia_keep_Fellwar_20261023.txt")[0])
        self.assertEqual((adr["Mirkwood Bats"], adr["Adrestia"], adr["Fateful Discovery"], sum(adr.values())), (1, 0, 1, 100))
        four = Counter(gate.parse_list(RC / f"{D}_four_no_MirkwoodBats_keep_Fellwar_20261023.txt")[0])
        self.assertEqual((four["Mirkwood Bats"], four["Fellwar Stone"], sum(four.values())), (0, 1, 100))
        six = Counter(gate.parse_list(RC / f"{D}_six_EagleVision_over_ImperialSeal_20261023.txt")[0])
        self.assertEqual((six["Eagle Vision"], six["Imperial Seal"], sum(six.values())), (1, 0, 100))
        ch = Counter(gate.parse_list(RC / f"{D}_five_ChandraSparkHunter_instead_of_MuYanling_20261023.txt")[0])
        self.assertEqual((ch["Chandra, Spark Hunter"], ch["Mu Yanling, Wind Rider"], sum(ch.values())), (1, 0, 100))

    def test_commander_legal_released_no_exception(self):
        snap = json.loads((ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json").read_text())
        ed = [c for c in snap["cards"] if c["name"] == "Edward Kenway"][0]
        self.assertEqual(ed["commander_legality"], "legal")
        self.assertIs(ed["game_changer"], False)
        self.assertEqual((ed["set"], ed["released_at"]), ("acr", "2024-07-05"))
        self.assertLessEqual(ed["released_at"], "2026-10-23")

    def test_no_approval_or_lock_markers_in_new_artifacts(self):
        for p in [PACKET, ROOT / self.packet["final_candidate"]["path"]]:
            text = p.read_text()
            self.assertNotIn("CANONICAL_LOCKED", text)
            self.assertNotIn('"APPROVED"', text)


if __name__ == "__main__":
    unittest.main()
