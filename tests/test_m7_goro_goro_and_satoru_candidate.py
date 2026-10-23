"""Deck 21 Goro-Goro and Satoru M7 research candidate: structural checks only, not approval.

The packet is RESEARCH_ONLY_WITHDRAWN_NOT_OWNER_PRESENTABLE: one genuine swap (+Bitterblossom / -Mist-Syndicate Naga),
far below the five-swap floor, which is not padded."""
from __future__ import annotations
import hashlib
import json
import unittest
from collections import Counter
from pathlib import Path

from scripts import grixis_m7_decision_gate as gate

ROOT = Path(__file__).resolve().parents[1]
D = "Goro_Goro_and_Satoru"
PACKET = ROOT / f"data/grixis/m7/decision_reviews/{D}.json"
BASE = ROOT / f"data/grixis/m7/baseline_sources/{D}_approved_source_2026-10-14.txt"
RAW = "2fd39e3b39afaeb1bf394a59b392d8a29f28645776fa0b13c5754df67ab85fdf"
CAND_RAW = "38e02f9766783ad5194d569329f54603a47829a162d1bc3ea041898e1f4f5e5b"
RC = ROOT / "data/grixis/m7/research_challengers"


class GoroGoroAndSatoruM7Tests(unittest.TestCase):
    def setUp(self):
        self.packet = json.loads(PACKET.read_text())
        self.registry = json.loads((ROOT / "data/grixis/registry.json").read_text())
        self.judged = {c["card"]: c for c in self.packet["material_candidates"]}

    def test_gate_passes_as_withdrawn_research_only_not_approval(self):
        result = gate.verify_packet(self.packet, root=ROOT, registry=self.registry)
        self.assertFalse(result["owner_presentable"])
        self.assertEqual(result["new_swaps"], 1)
        self.assertEqual(result["status"], "M7_WITHDRAWN_RESEARCH_ONLY_NOT_OWNER_PRESENTABLE")
        self.assertEqual(self.packet["readiness"], "RESEARCH_ONLY_WITHDRAWN_NOT_OWNER_PRESENTABLE")
        reason = self.packet["withdrawal_reason"]
        self.assertIn("only one genuine swap was found", reason)
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

    def test_exact_single_physical_swap_against_vendored_and_canonical_source(self):
        cand = Counter(gate.parse_list(ROOT / self.packet["final_candidate"]["path"])[0])
        path, md = gate.canonical_source(ROOT, self.registry["decks"][D])
        for base in (Counter(gate.parse_list(BASE)[0]), Counter(gate.parse_list(path, source_markdown=md)[0])):
            self.assertEqual(sorted((cand - base).elements()), sorted(self.packet["final_changes"]["adds"]))
            self.assertEqual(sorted((base - cand).elements()), sorted(self.packet["final_changes"]["cuts"]))
        self.assertEqual(self.packet["final_changes"]["adds"], ["Bitterblossom"])
        self.assertEqual(self.packet["final_changes"]["cuts"], ["Mist-Syndicate Naga"])

    def test_single_commander_first_and_100_physical_singleton_except_basics(self):
        lines = [x for x in (ROOT / self.packet["final_candidate"]["path"]).read_text().splitlines() if x.strip()]
        self.assertEqual(lines[0], "1x Goro-Goro and Satoru [Commander]")
        self.assertEqual(sum(1 for x in lines if x.endswith("[Commander]")), 1)
        self.assertFalse(any("[Companion]" in x for x in lines))
        self.assertEqual(sum(int(x.split("x ", 1)[0]) for x in lines), 100)
        multi = [x for x in lines if not x.startswith("1x ")]
        self.assertEqual(multi, ["2x Island"])
        rest = [x.split("x ", 1)[1] for x in lines[1:]]
        self.assertEqual(rest, sorted(rest, key=str.lower))
        self.assertEqual(len(set(rest)), 98)

    def test_distinctness_note_and_commander_first_identity_recorded(self):
        note = self.packet["commander_identity"]["anti_homogenization"]
        self.assertIn("Commander-first", note)
        for s in ("Admiral Beckett Brass 45 -> 45", "Garza Zol, Plague Queen 43 -> 43", "Admiral Brass, Unsinkable 42 -> 42",
                  "Don Andres, the Renegade 41 -> 41", "Doctor Doom, King of Latveria 41 -> 41"):
            self.assertIn(s, note)
        self.assertIn("Owner-removed or rejected cards and classes", note)

    def test_owner_direction_no_owner_keep_or_addition_cut_and_removed_not_readded(self):
        adds = set(self.packet["final_changes"]["adds"])
        cuts = set(self.packet["final_changes"]["cuts"])
        removed = ("Reinforced Ronin", "Rising of the Day", "Feed the Swarm", "Combat Research", "Impact Tremors",
                   "Kaito, Dancing Shadow", "Kaito, Cunning Infiltrator", "Invisible Stalker", "Tormented Soul",
                   "Higure, the Still Wind", "Enduring Courage", "Sokenzan, Crucible of Defiance")
        for card in removed:
            self.assertNotIn(card, adds)
        owner_kept = ("Bident of Thassa", "Enduring Curiosity", "Daring Piracy", "Loyal Apprentice", "Urabrask's Forge",
                      "Determined Iteration", "Dragon Tempest", "Terror of the Peaks", "Rogue's Passage",
                      "Phoenix Chick", "Samut, Hazoret's Champion", "Withering Torment", "Waterbender Ascension",
                      "Raphael, the Nightwatcher", "Fire Navy Trebuchet", "Yuriko, the Tiger's Shadow",
                      "Satoru Umezawa", "Silver-Fur Master")
        for keep in owner_kept:
            self.assertNotIn(keep, cuts)
        self.assertIn("No owner keep or owner addition is cut", self.packet["final_changes"]["coherent_package_tradeoff"])
        for rej in ("Redoubled Stormsinger", "Dragonskull Summit", "Goblin Rabblemaster", "Kari Zev, Skyship Raider",
                    "Gurmag Swiftwing", "Sneak Attack"):
            self.assertEqual(self.judged[rej]["judgment"], "REJECT", rej)
        self.assertEqual(self.judged["Rapid Hybridization"]["judgment"], "RETAIN_ALTERNATIVE")
        self.assertEqual(self.judged["Jeweled Lotus"]["judgment"], "EXCLUDE_INVALID")
        self.assertEqual(self.judged["Bitterblossom"]["judgment"], "SELECT_ADD")

    def test_power_bracket_tags_game_changers_and_combo_disclosure(self):
        v = self.packet["verification"]
        self.assertEqual(v["power_bracket"], 4)
        self.assertEqual(v["archidekt_tags"], ["Ninjas", "Dragons", "Extra Combats"])
        ceiling = self.packet["commander_identity"]["natural_ceiling"]
        self.assertIn("Game Changers: 6 in baseline and candidate", ceiling)
        self.assertIn("5 -> 5 complete combos", ceiling)
        self.assertIn("142 -> 138", ceiling)
        csb = json.dumps(json.loads((RC / f"{D}_CommanderSpellbook_20261023.json").read_text()))
        for cid in ("33-3259", "1347-3259", "2237-3259", "3259-3934", "1674-3259"):
            self.assertIn(cid, csb)

    def test_alternatives_staged_as_complete_hundreds(self):
        def load(name):
            return Counter(gate.parse_list(RC / f"{D}_{name}_20261023.txt")[0])
        a = load("PassC_plus_Bitterblossom_minus_BidentOfThassa")
        self.assertEqual((a["Bitterblossom"], a["Bident of Thassa"], a["Mist-Syndicate Naga"], sum(a.values())), (1, 0, 1, 100))
        b = load("PassC_plus_Bitterblossom_minus_GrazilaxxIllithidScholar")
        self.assertEqual((b["Bitterblossom"], b["Grazilaxx, Illithid Scholar"], b["Mist-Syndicate Naga"], sum(b.values())),
                         (1, 0, 1, 100))
        c = load("PassC_plus_Bitterblossom_minus_FrostcliffSiege")
        self.assertEqual((c["Bitterblossom"], c["Frostcliff Siege"], sum(c.values())), (1, 0, 100))
        s = load("two_RedoubledStormsinger_over_FrostcliffSiege")
        self.assertEqual((s["Redoubled Stormsinger"], s["Frostcliff Siege"], s["Mist-Syndicate Naga"], sum(s.values())),
                         (1, 0, 0, 100))
        r = load("two_RapidHybridization_over_Vandalblast")
        self.assertEqual((r["Rapid Hybridization"], r["Vandalblast"], sum(r.values())), (1, 0, 100))
        k = load("two_DragonskullSummit_over_CrumblingNecropolis")
        self.assertEqual((k["Dragonskull Summit"], k["Crumbling Necropolis"], sum(k.values())), (1, 0, 100))

    def test_commander_legal_released_no_exception(self):
        snap = json.loads((ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json").read_text())
        g = [c for c in snap["cards"] if c["name"] == "Goro-Goro and Satoru"][0]
        self.assertEqual(g["commander_legality"], "legal")
        self.assertIs(g["game_changer"], False)
        self.assertEqual((g["set"], g["released_at"]), ("moc", "2023-04-21"))
        self.assertEqual(snap["project_exceptions"], "0")

    def test_no_approval_or_lock_markers_in_new_artifacts(self):
        for p in [PACKET, ROOT / self.packet["final_candidate"]["path"]]:
            text = p.read_text()
            self.assertNotIn("CANONICAL_LOCKED", text)
            self.assertNotIn('"APPROVED"', text)


if __name__ == "__main__":
    unittest.main()
