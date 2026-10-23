"""Deck 19 Fire Lord Azula M7 review candidate: structural checks only, not approval."""
from __future__ import annotations
import hashlib
import json
import unittest
from collections import Counter
from pathlib import Path

from scripts import grixis_m7_decision_gate as gate

ROOT = Path(__file__).resolve().parents[1]
D = "Fire_Lord_Azula"
PACKET = ROOT / f"data/grixis/m7/decision_reviews/{D}.json"
BASE = ROOT / f"data/grixis/m7/baseline_sources/{D}_approved_source_2026-10-14.txt"
RAW = "b6ef396641f2b5cfac0eb81fb494f21f3745e2a3fd47fa75d2eaadbdc34ddee5"
CAND_RAW = "f4136ea0028ee787dddad379e12a7e34ccdaa6578a52d1c63ae953734e5806f2"
RC = ROOT / "data/grixis/m7/research_challengers"


class FireLordAzulaM7Tests(unittest.TestCase):
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
        self.assertEqual(lines[0], "1x Fire Lord Azula [Commander]")
        self.assertEqual(sum(1 for x in lines if x.endswith("[Commander]")), 1)
        self.assertFalse(any("[Companion]" in x for x in lines))
        self.assertEqual(len(lines), 100)
        self.assertTrue(all(x.startswith("1x ") for x in lines))
        rest = [x.split("x ", 1)[1] for x in lines[1:]]
        self.assertEqual(rest, sorted(rest, key=str.lower))
        self.assertEqual(len(set(rest)), 99)  # Tainted Pact: distinct names

    def test_distinctness_note_and_commander_first_identity_recorded(self):
        note = self.packet["commander_identity"]["anti_homogenization"]
        self.assertIn("Commander-first", note)
        for s in ("Norman Osborn 76 -> 74", "Kefka, Court Mage 76 -> 74", "Kess, Dissident Mage 74 -> 73",
                  "Rograkh/Silas Renn 74 -> 71", "Jeleva, Nephalia's Scourge 73 -> 70",
                  "Evelyn, the Covetous 68 -> 66", "Turnabout and Flashback appear in no other Grixis export"):
            self.assertIn(s, note)
        self.assertIn("Owner-removed or rejected cards and classes", note)

    def test_owner_removed_class_not_readded_and_samut_override_flagged(self):
        adds = set(self.packet["final_changes"]["adds"])
        cuts = set(self.packet["final_changes"]["cuts"])
        removed = ("Storm-Kiln Artist", "Spellseeker", "Dualcaster Mage", "Twinflame", "Twinning Staff",
                   "Lightning Greaves", "Seething Song", "Snapcaster Mage", "Brainstorm", "Gitaxian Probe",
                   "Leyline of Anticipation", "Veyran, Voice of Duality", "Archmage Emeritus",
                   "The Last Agni Kai", "Training Center", "Final Fortune")
        for card in removed:
            self.assertNotIn(card, adds)
        # The only owner addition cut is Samut, and the override is flagged with a keep-Samut alternative.
        owner_adds_kept = ("Geist of Saint Thalia", "Strix Serenade", "Repeal", "Quicken", "Crimson Wisps",
                           "Expedite", "Grinding Station", "Beseech the Mirror", "Mox Opal",
                           "Wan Shi Tong, Librarian", "Starting Town", "Arena of Glory", "Cavern of Souls")
        for keep in owner_adds_kept:
            self.assertNotIn(keep, cuts)
        self.assertIn("Samut, Tyrant of Naktamun", cuts)
        self.assertIn("FLAGGED", self.packet["final_changes"]["coherent_package_tradeoff"])
        self.assertEqual(self.judged["Lightning Greaves"]["judgment"], "REJECT")
        self.assertEqual(self.judged["Brainstorm"]["judgment"], "REJECT")
        for alt in ("Mox Amber", "Spellseeker", "Storm-Kiln Artist"):
            self.assertEqual(self.judged[alt]["judgment"], "RETAIN_ALTERNATIVE")

    def test_power_bracket_tags_game_changers_and_combo_disclosure(self):
        v = self.packet["verification"]
        self.assertEqual(v["power_bracket"], 5)
        self.assertEqual(v["archidekt_tags"], ["Combat-Flash", "Spell Copy", "Combo"])
        ceiling = self.packet["commander_identity"]["natural_ceiling"]
        self.assertIn("Game Changers: 20 in baseline and candidate", ceiling)
        self.assertIn("9 -> 10 complete combos", ceiling)
        self.assertIn("11-4276-7089", ceiling)
        self.assertIn("98 -> 105", ceiling)
        csb = json.loads((RC / f"{D}_CommanderSpellbook_20261023.json").read_text())
        self.assertIn("11-4276-7089", json.dumps(csb))

    def test_alternatives_staged_as_complete_hundreds(self):
        def load(name):
            return Counter(gate.parse_list(RC / f"{D}_{name}_20261023.txt")[0])
        samut = load("four_keep_Samut_no_Turnabout")
        self.assertEqual((samut["Samut, Tyrant of Naktamun"], samut["Turnabout"], sum(samut.values())), (1, 0, 100))
        swan = load("four_keep_SwanSong_no_Flashback")
        self.assertEqual((swan["Swan Song"], swan["Flashback"], sum(swan.values())), (1, 0, 100))
        gem = load("five_keep_GemstoneCaverns_cut_WoodedFoothills")
        self.assertEqual((gem["Gemstone Caverns"], gem["Wooded Foothills"], gem["Mistrise Village"], sum(gem.values())),
                         (1, 0, 1, 100))
        six = load("six_MoxAmber_over_FellwarStone")
        self.assertEqual((six["Mox Amber"], six["Fellwar Stone"], six["Turnabout"], sum(six.values())), (1, 0, 1, 100))
        ss = load("PassC_baseline_plus_Spellseeker_minus_Samut")
        self.assertEqual((ss["Spellseeker"], ss["Samut, Tyrant of Naktamun"], ss["Swan Song"], sum(ss.values())), (1, 0, 1, 100))
        bs = load("PassC_baseline_plus_StormKilnArtist_minus_BigScore")
        self.assertEqual((bs["Storm-Kiln Artist"], bs["Big Score"], sum(bs.values())), (1, 0, 100))
        wst = load("PassC_baseline_plus_StormKilnArtist_minus_WanShiTong")
        self.assertEqual((wst["Storm-Kiln Artist"], wst["Wan Shi Tong, Librarian"], sum(wst.values())), (1, 0, 100))

    def test_commander_legal_released_no_exception(self):
        snap = json.loads((ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json").read_text())
        az = [c for c in snap["cards"] if c["name"] == "Fire Lord Azula"][0]
        self.assertEqual(az["commander_legality"], "legal")
        self.assertIs(az["game_changer"], False)
        self.assertEqual((az["set"], az["released_at"]), ("tla", "2025-11-21"))
        self.assertLessEqual(az["released_at"], "2026-10-23")

    def test_no_approval_or_lock_markers_in_new_artifacts(self):
        for p in [PACKET, ROOT / self.packet["final_candidate"]["path"]]:
            text = p.read_text()
            self.assertNotIn("CANONICAL_LOCKED", text)
            self.assertNotIn('"APPROVED"', text)


if __name__ == "__main__":
    unittest.main()
