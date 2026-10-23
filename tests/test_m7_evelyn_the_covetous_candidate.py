"""Deck 18 Evelyn, the Covetous M7 review candidate: structural checks only, not approval."""
from __future__ import annotations
import hashlib
import json
import unittest
from collections import Counter
from pathlib import Path

from scripts import grixis_m7_decision_gate as gate

ROOT = Path(__file__).resolve().parents[1]
D = "Evelyn__the_Covetous"
PACKET = ROOT / f"data/grixis/m7/decision_reviews/{D}.json"
BASE = ROOT / f"data/grixis/m7/baseline_sources/{D}_approved_source_2026-10-14.txt"
RAW = "1d602b5d9b2a370d3448816f593198212b2b83da74e92ccc3232798641b2588a"
CAND_RAW = "c3f6862c6f4498778069f45e7a5e5bc7efe92d70158b5e9b3f438c8c861b89ac"
RC = ROOT / "data/grixis/m7/research_challengers"


class EvelynTheCovetousM7Tests(unittest.TestCase):
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

    def test_single_commander_first_and_100_physical_all_singletons(self):
        lines = [x for x in (ROOT / self.packet["final_candidate"]["path"]).read_text().splitlines() if x.strip()]
        self.assertEqual(lines[0], "1x Evelyn, the Covetous [Commander]")
        self.assertEqual(sum(1 for x in lines if x.endswith("[Commander]")), 1)
        self.assertFalse(any("[Companion]" in x for x in lines))
        self.assertEqual(len(lines), 100)
        self.assertTrue(all(x.startswith("1x ") for x in lines))
        rest = [x.split("x ", 1)[1] for x in lines[1:]]
        self.assertEqual(rest, sorted(rest, key=str.lower))

    def test_distinctness_note_and_commander_first_identity_recorded(self):
        note = self.packet["commander_identity"]["anti_homogenization"]
        self.assertIn("Commander-first", note)
        for s in ("Don Andres, the Renegade (#14) 27 -> 29", "Cormela, Glamour Thief (#9) 67 -> 69",
                  "No Gonti deck is in the Grixis registry"):
            self.assertIn(s, note)
        self.assertIn("Owner-removed or rejected cards and classes", note)

    def test_owner_removed_class_not_readded_and_no_owner_keep_cut(self):
        adds = set(self.packet["final_changes"]["adds"])
        cuts = set(self.packet["final_changes"]["cuts"])
        removed = ("Displacer Kitten", "Otawara, Soaring City", "Morphic Pool", "Talisman of Creativity",
                   "Wheel of Fortune", "The One Ring", "Dragon's Rage Channeler", "Cyclonic Rift",
                   "Deflecting Swat", "Into the Flood Maw", "Hoarding Broodlord", "Beseech the Mirror")
        for card in removed:
            self.assertNotIn(card, adds)
        for keep in ("Vexing Bauble", "Ripples of Undeath", "Saw in Half", "Windfall", "Notion Thief",
                     "Stifle", "Mistrise Village"):
            self.assertNotIn(keep, cuts)
        self.assertEqual(self.judged["Displacer Kitten"]["judgment"], "REJECT")
        self.assertEqual(self.judged["Otawara, Soaring City"]["judgment"], "REJECT")
        self.assertEqual(self.judged["Spell Pierce"]["judgment"], "RETAIN_ALTERNATIVE")
        self.assertEqual(self.judged["Grim Monolith"]["judgment"], "RETAIN_ALTERNATIVE")
        self.assertEqual(self.judged["Wan Shi Tong, Librarian"]["judgment"], "RETAIN_ALTERNATIVE")

    def test_power_bracket_tags_game_changers_and_combo_disclosure(self):
        v = self.packet["verification"]
        self.assertEqual(v["power_bracket"], 5)
        self.assertEqual(v["archidekt_tags"], ["cEDH", "Worldgorger Combo", "Thassa's Oracle"])
        ceiling = self.packet["commander_identity"]["natural_ceiling"]
        self.assertIn("Game Changers: 19 in baseline and candidate", ceiling)
        self.assertIn("the same 7 complete combos in both lists", ceiling)
        self.assertIn("103 -> 117", ceiling)
        self.assertIn("No new combo is claimed", ceiling)

    def test_alternatives_staged_as_complete_hundreds(self):
        def load(name):
            return Counter(gate.parse_list(RC / f"{D}_{name}_20261023.txt")[0])
        pc = load("PassC_baseline_plus_Brainstorm_minus_RipplesOfUndeath")
        self.assertEqual((pc["Brainstorm"], pc["Ripples of Undeath"], pc["Spellskite"], sum(pc.values())), (1, 0, 1, 100))
        four = load("four_keep_BlazemireVerge")
        self.assertEqual((four["Blazemire Verge"], four["Verdant Catacombs"], sum(four.values())), (1, 0, 100))
        grim = load("five_GrimMonolith_instead_of_BurntOffering")
        self.assertEqual((grim["Grim Monolith"], grim["Burnt Offering"], sum(grim.values())), (1, 0, 100))
        wst = load("five_keep_WanShiTong_cut_NotionThief")
        self.assertEqual((wst["Wan Shi Tong, Librarian"], wst["Notion Thief"], sum(wst.values())), (1, 0, 100))
        six = load("six_SpellPierce_over_RipplesOfUndeath")
        self.assertEqual((six["Spell Pierce"], six["Ripples of Undeath"], sum(six.values())), (1, 0, 100))

    def test_commander_legal_released_no_exception(self):
        snap = json.loads((ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json").read_text())
        ev = [c for c in snap["cards"] if c["name"] == "Evelyn, the Covetous"][0]
        self.assertEqual(ev["commander_legality"], "legal")
        self.assertIs(ev["game_changer"], False)
        self.assertEqual((ev["set"], ev["released_at"]), ("snc", "2022-04-29"))
        self.assertLessEqual(ev["released_at"], "2026-10-23")

    def test_no_approval_or_lock_markers_in_new_artifacts(self):
        for p in [PACKET, ROOT / self.packet["final_candidate"]["path"]]:
            text = p.read_text()
            self.assertNotIn("CANONICAL_LOCKED", text)
            self.assertNotIn('"APPROVED"', text)


if __name__ == "__main__":
    unittest.main()
