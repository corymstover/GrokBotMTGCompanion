"""Deck 16 Edea, Possessed Sorceress M7 review candidate: structural checks only, not approval."""
from __future__ import annotations
import hashlib
import json
import unittest
from collections import Counter
from pathlib import Path

from scripts import grixis_m7_decision_gate as gate

ROOT = Path(__file__).resolve().parents[1]
D = "Edea__Possessed_Sorceress"
PACKET = ROOT / f"data/grixis/m7/decision_reviews/{D}.json"
BASE = ROOT / f"data/grixis/m7/baseline_sources/{D}_approved_source_2026-10-14.txt"
RAW = "fd560a9b0777088b3ad1684ded030566c894faa206ddf6763b74d95d82c532e4"
CAND_RAW = "e8680cafc7b7500b6106677e1aaafce6d5035893ea9f0cd335cd1fa1ff5227a2"
RC = ROOT / "data/grixis/m7/research_challengers"


class EdeaM7Tests(unittest.TestCase):
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
        self.assertEqual(lines[0], "1x Edea, Possessed Sorceress [Commander]")
        self.assertEqual(sum(1 for x in lines if x.endswith("[Commander]")), 1)
        self.assertFalse(any("[Companion]" in x for x in lines))
        self.assertEqual(sum(int(x.split("x ", 1)[0]) for x in lines), 100)
        self.assertEqual([x for x in lines if not x.startswith("1x ")], ["3x Island", "3x Mountain", "3x Swamp"])
        rest = [x.split("x ", 1)[1] for x in lines[1:]]
        self.assertEqual(rest, sorted(rest, key=str.lower))

    def test_distinctness_note_and_commander_first_identity_recorded(self):
        note = self.packet["commander_identity"]["anti_homogenization"]
        self.assertIn("Commander-first", note)
        for s in ("Marchesa, the Black Rose 50 -> 49", "Missy 46 -> 46", "Wick, the Whorled Mind 45 -> 45",
                  "Tresserhorns 44 -> 43", "Thraximundar 43 -> 43", "Lord Xander 41 -> 43", "39 -> 38"):
            self.assertIn(s, note)
        self.assertIn("Owner-removed or rejected classes", note)

    def test_owner_removed_class_not_readded(self):
        adds = set(self.packet["final_changes"]["adds"])
        removed = ("Garland, Knight of Cornelia", "Coercive Recruiter", "Morbid Opportunist", "Reliquary Tower",
                   "Marchesa, the Black Rose", "Domineering Will", "Nasty End", "Cunning Rhetoric", "Conjurer's Closet",
                   "Phantasmal Image", "Helm of Possession", "Rhystic Study", "Vampiric Tutor", "Force of Will",
                   "The One Ring", "Breath of Fury", "Lithoform Engine")
        for card in removed:
            self.assertNotIn(card, adds)
        for card in ("Nasty End", "Rhystic Study", "Sakashima the Impostor"):
            self.assertEqual(self.judged[card]["judgment"], "REJECT")
            self.assertIn("OWNER", json.dumps(self.judged[card]))
        self.assertEqual(self.judged["Conjurer's Closet"]["judgment"], "RETAIN_ALTERNATIVE")
        self.assertEqual(self.judged["Lithoform Engine"]["judgment"], "RETAIN_ALTERNATIVE")

    def test_power_bracket_tags_and_game_changers(self):
        v = self.packet["verification"]
        self.assertEqual(v["power_bracket"], 4)
        self.assertEqual(v["archidekt_tags"], ["Theft", "Extra Combats", "Aristocrats"])
        ceiling = self.packet["commander_identity"]["natural_ceiling"]
        self.assertIn("Game Changers: 3 in baseline and candidate", ceiling)
        self.assertIn("No infinite is claimed", ceiling)
        self.assertIn("126 -> 167", ceiling)

    def test_owner_retention_conflicts_flagged_with_staged_alternative(self):
        for card in ("Aggravated Assault", "Hall of Echoes"):
            self.assertEqual(self.judged[card]["judgment"], "SELECT_ADD")
            self.assertIn("FLAG", " ".join(self.judged[card][k] for k in ("incumbent_opportunity_cost", "adversarial_downside")))
        alt = Counter(gate.parse_list(RC / f"{D}_four_keep_Evereth_Assault_over_Spotlight_no_Celebrant_20261023.txt")[0])
        self.assertEqual(alt["Evereth, Viceroy of Plunder"], 1)
        self.assertEqual(alt["Seize the Spotlight"], 0)
        self.assertEqual(alt["Combat Celebrant"], 0)
        self.assertEqual(sum(alt.values()), 100)
        litho = Counter(gate.parse_list(RC / f"{D}_five_LithoformEngine_instead_of_Dihada_20261023.txt")[0])
        self.assertEqual((litho["Lithoform Engine"], litho["Geyadrone Dihada"], sum(litho.values())), (1, 0, 100))

    def test_commander_legal_released_no_exception(self):
        snap = json.loads((ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json").read_text())
        edea = [c for c in snap["cards"] if c["name"] == "Edea, Possessed Sorceress"][0]
        self.assertEqual(edea["commander_legality"], "legal")
        self.assertIs(edea["game_changer"], False)
        self.assertEqual((edea["set"], edea["released_at"]), ("fic", "2025-12-05"))
        self.assertLessEqual(edea["released_at"], "2026-10-23")

    def test_no_approval_or_lock_markers_in_new_artifacts(self):
        for p in [PACKET, ROOT / self.packet["final_candidate"]["path"]]:
            text = p.read_text()
            self.assertNotIn("CANONICAL_LOCKED", text)
            self.assertNotIn('"APPROVED"', text)


if __name__ == "__main__":
    unittest.main()
