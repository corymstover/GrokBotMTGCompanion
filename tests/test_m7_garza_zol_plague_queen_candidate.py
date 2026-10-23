"""Deck 20 Garza Zol, Plague Queen M7 research candidate: structural checks only, not approval.

The packet is RESEARCH_ONLY_WITHDRAWN_NOT_OWNER_PRESENTABLE: four genuine swaps, below the five-swap floor, which is
not padded."""
from __future__ import annotations
import hashlib
import json
import unittest
from collections import Counter
from pathlib import Path

from scripts import grixis_m7_decision_gate as gate

ROOT = Path(__file__).resolve().parents[1]
D = "Garza_Zol__Plague_Queen"
PACKET = ROOT / f"data/grixis/m7/decision_reviews/{D}.json"
BASE = ROOT / f"data/grixis/m7/baseline_sources/{D}_approved_source_2026-10-14.txt"
RAW = "32c0e8049a9c8a5d238048b4f774f0457908d724f23d4597b7da93a6cba0c16f"
CAND_RAW = "48b6a7dbdb2dac5d591d93cb6f7f7efea634c0663acab9b6a1812661e559317f"
RC = ROOT / "data/grixis/m7/research_challengers"
SINK = "Sink into Stupor // Soporific Springs"
FELL = "Fell the Profane // Fell Mire"


class GarzaZolM7Tests(unittest.TestCase):
    def setUp(self):
        self.packet = json.loads(PACKET.read_text())
        self.registry = json.loads((ROOT / "data/grixis/registry.json").read_text())
        self.judged = {c["card"]: c for c in self.packet["material_candidates"]}

    def test_gate_passes_as_withdrawn_research_only_not_approval(self):
        result = gate.verify_packet(self.packet, root=ROOT, registry=self.registry)
        self.assertFalse(result["owner_presentable"])
        self.assertEqual(result["new_swaps"], 4)
        self.assertEqual(result["status"], "M7_WITHDRAWN_RESEARCH_ONLY_NOT_OWNER_PRESENTABLE")
        self.assertEqual(self.packet["readiness"], "RESEARCH_ONLY_WITHDRAWN_NOT_OWNER_PRESENTABLE")
        reason = self.packet["withdrawal_reason"]
        self.assertIn("only four genuine swaps", reason)
        self.assertIn("not met without padding", reason)
        self.assertIn("NOT owner approved", reason)
        self.assertFalse(self.packet["owner_authority"]["exact_candidate_owner_approved"])
        self.assertFalse(self.packet["owner_authority"]["canonical_deck_changed"])
        self.assertNotIn("baseline_provenance_exception", self.packet)
        self.assertEqual(self.packet["verification"]["known_hard_blockers"], [])

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

    def test_exact_four_physical_swaps_against_vendored_and_canonical_md(self):
        cand = Counter(gate.parse_list(ROOT / self.packet["final_candidate"]["path"])[0])
        path, md = gate.canonical_source(ROOT, self.registry["decks"][D])
        for base in (Counter(gate.parse_list(BASE)[0]), Counter(gate.parse_list(path, source_markdown=md)[0])):
            self.assertEqual(sorted((cand - base).elements()), sorted(self.packet["final_changes"]["adds"]))
            self.assertEqual(sorted((base - cand).elements()), sorted(self.packet["final_changes"]["cuts"]))
        self.assertEqual(sorted(self.packet["final_changes"]["adds"]),
                         sorted(["Lizard Blades", "Giantfall", SINK, FELL]))
        self.assertEqual(sorted(self.packet["final_changes"]["cuts"]),
                         sorted(["Fellwar Stone", "Rapid Hybridization", "Exotic Orchard",
                                 "Takenuma, Abandoned Mire"]))

    def test_single_commander_first_and_100_physical_all_singletons(self):
        lines = [x for x in (ROOT / self.packet["final_candidate"]["path"]).read_text().splitlines() if x.strip()]
        self.assertEqual(lines[0], "1x Garza Zol, Plague Queen [Commander]")
        self.assertEqual(sum(1 for x in lines if x.endswith("[Commander]")), 1)
        self.assertFalse(any("[Companion]" in x for x in lines))
        self.assertEqual(len(lines), 100)
        self.assertTrue(all(x.startswith("1x ") for x in lines))
        rest = [x.split("x ", 1)[1] for x in lines[1:]]
        self.assertEqual(rest, sorted(rest, key=str.lower))
        self.assertEqual(len(set(rest)), 99)

    def test_distinctness_note_and_commander_first_identity_recorded(self):
        note = self.packet["commander_identity"]["anti_homogenization"]
        self.assertIn("Commander-first", note)
        for s in ("Nicol Bolas 61 -> 58", "Lord of Tresserhorn 50 -> 47", "Obeka, Brute Chronologist 48 -> 46",
                  "Nicol Bolas, the Ravager 46 -> 44", "Edward Kenway 46 -> 44"):
            self.assertIn(s, note)
        self.assertIn("Owner-removed or rejected cards and classes", note)

    def test_owner_direction_no_owner_keep_or_addition_cut_and_removed_not_readded(self):
        adds = set(self.packet["final_changes"]["adds"])
        cuts = set(self.packet["final_changes"]["cuts"])
        removed = ("Lightning Greaves", "Embercleave", "Bident of Thassa", "Ophidian Eye", "Frantic Search",
                   "Waltz of Rage", "Go for the Throat", "Soul Shatter", "Sword of Truth and Justice",
                   "Viridian Longbow", "Gorgon's Head", "Fire Whip")
        for card in removed:
            self.assertNotIn(card, adds)
        owner_kept = ("Blade of the Bloodchief", "Brotherhood Regalia", "Chandra's Ignition", "Curiosity",
                      "Grafted Exoskeleton", "Mask of Memory", "Quietus Spike", "Shadowspear", "Swiftfoot Boots",
                      "Sword of Feast and Famine", "Sword of Fire and Ice", "Trailblazer's Boots",
                      "Rogue's Passage", "Nova Flame", "Toxic Deluge", "Inquisitor's Flail")
        for keep in owner_kept:
            self.assertNotIn(keep, cuts)
        self.assertIn("No owner keep or owner addition is cut", self.packet["final_changes"]["coherent_package_tradeoff"])
        for rej in ("Nibelheim Aflame", "Fire Whip", "Hammer of Nazahn"):
            self.assertEqual(self.judged[rej]["judgment"], "REJECT", rej)
        self.assertEqual(self.judged["Fireshrieker"]["judgment"], "RETAIN_ALTERNATIVE")
        self.assertEqual(self.judged["Jeweled Lotus"]["judgment"], "EXCLUDE_INVALID")
        for add in self.packet["final_changes"]["adds"]:
            self.assertEqual(self.judged[add]["judgment"], "SELECT_ADD", add)

    def test_power_bracket_tags_game_changers_and_combo_disclosure(self):
        v = self.packet["verification"]
        self.assertEqual(v["power_bracket"], 4)
        self.assertEqual(v["archidekt_tags"], ["Voltron", "Commander Damage", "Deathtouch-Control"])
        ceiling = self.packet["commander_identity"]["natural_ceiling"]
        self.assertIn("Game Changers: 9 in baseline and candidate", ceiling)
        self.assertIn("3 -> 3 complete combos", ceiling)
        self.assertIn("86 -> 86", ceiling)
        csb = json.dumps(json.loads((RC / f"{D}_CommanderSpellbook_20261023.json").read_text()))
        for cid in ("3750-5039", "900-3750", "2822-3681"):
            self.assertIn(cid, csb)

    def test_alternatives_staged_as_complete_hundreds(self):
        def load(name):
            return Counter(gate.parse_list(RC / f"{D}_{name}_20261023.txt")[0])
        fs = load("four_Fireshrieker_instead_of_LizardBlades")
        self.assertEqual((fs["Fireshrieker"], fs["Lizard Blades"], fs["Fellwar Stone"], sum(fs.values())), (1, 0, 0, 100))
        kf = load("four_LizardBlades_cut_InquisitorsFlail_keep_FellwarStone")
        self.assertEqual((kf["Lizard Blades"], kf["Inquisitor's Flail"], kf["Fellwar Stone"], sum(kf.values())),
                         (1, 0, 1, 100))
        nn = load("five_NibelheimAflame_over_NovaFlame")
        self.assertEqual((nn["Nibelheim Aflame"], nn["Nova Flame"], sum(nn.values())), (1, 0, 100))
        nt = load("five_NibelheimAflame_over_ToxicDeluge")
        self.assertEqual((nt["Nibelheim Aflame"], nt["Toxic Deluge"], sum(nt.values())), (1, 0, 100))
        fw = load("five_FireWhip_over_Pongify")
        self.assertEqual((fw["Fire Whip"], fw["Pongify"], sum(fw.values())), (1, 0, 100))
        hn = load("five_HammerOfNazahn_over_TalismanOfIndulgence")
        self.assertEqual((hn["Hammer of Nazahn"], hn["Talisman of Indulgence"], sum(hn.values())), (1, 0, 100))
        pc = load("PassC_baseline_plus_Fireshrieker_minus_InquisitorsFlail")
        self.assertEqual((pc["Fireshrieker"], pc["Inquisitor's Flail"], pc["Fellwar Stone"], sum(pc.values())),
                         (1, 0, 1, 100))

    def test_commander_legal_released_no_exception(self):
        snap = json.loads((ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json").read_text())
        g = [c for c in snap["cards"] if c["name"] == "Garza Zol, Plague Queen"][0]
        self.assertEqual(g["commander_legality"], "legal")
        self.assertIs(g["game_changer"], False)
        self.assertEqual((g["set"], g["released_at"]), ("csp", "2006-07-21"))
        self.assertEqual(snap["project_exceptions"], "0")

    def test_no_approval_or_lock_markers_in_new_artifacts(self):
        for p in [PACKET, ROOT / self.packet["final_candidate"]["path"]]:
            text = p.read_text()
            self.assertNotIn("CANONICAL_LOCKED", text)
            self.assertNotIn('"APPROVED"', text)


if __name__ == "__main__":
    unittest.main()
