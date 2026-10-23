"""Deck 22 Gwendlyn Di Corci M7 research candidate: structural checks only, not approval.

The packet is RESEARCH_ONLY_WITHDRAWN_NOT_OWNER_PRESENTABLE: one genuine swap (+Hymn to Tourach / -Dauthi Voidwalker,
a flagged override of a card named in the owner's blueprint), far below the five-swap floor, which is not padded."""
from __future__ import annotations
import hashlib
import json
import unittest
from collections import Counter
from pathlib import Path

from scripts import grixis_m7_decision_gate as gate

ROOT = Path(__file__).resolve().parents[1]
D = "Gwendlyn_Di_Corci"
PACKET = ROOT / f"data/grixis/m7/decision_reviews/{D}.json"
BASE = ROOT / f"data/grixis/m7/baseline_sources/{D}_approved_source_2026-10-14.txt"
RAW = "9a393cb7edf40f9bfb388d37dd657839cad851dc6a021440c7d1b239c1fd20a9"
CAND_RAW = "f5f26b78a09f9247be2e311dd76b6e1ff3ed012cd2eaa66692cb33b68fc38197"
RC = ROOT / "data/grixis/m7/research_challengers"


class GwendlynDiCorciM7Tests(unittest.TestCase):
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
        self.assertEqual(self.packet["final_changes"]["adds"], ["Hymn to Tourach"])
        self.assertEqual(self.packet["final_changes"]["cuts"], ["Dauthi Voidwalker"])

    def test_single_commander_first_and_100_physical_singleton_except_basics(self):
        lines = [x for x in (ROOT / self.packet["final_candidate"]["path"]).read_text().splitlines() if x.strip()]
        self.assertEqual(lines[0], "1x Gwendlyn Di Corci [Commander]")
        self.assertEqual(sum(1 for x in lines if x.endswith("[Commander]")), 1)
        self.assertFalse(any("[Companion]" in x for x in lines))
        self.assertEqual(sum(int(x.split("x ", 1)[0]) for x in lines), 100)
        multi = [x for x in lines if not x.startswith("1x ")]
        self.assertEqual(multi, ["2x Island", "2x Mountain", "5x Swamp"])
        rest = [x.split("x ", 1)[1] for x in lines[1:]]
        self.assertEqual(rest, sorted(rest, key=str.lower))
        self.assertEqual(len(set(rest)), 93)

    def test_distinctness_note_and_commander_first_identity_recorded(self):
        note = self.packet["commander_identity"]["anti_homogenization"]
        self.assertIn("Commander-first", note)
        for s in ("Crosis, the Purger 55 -> 56", "Nekusar, the Mindrazer 54 -> 54", "Lord Xander, the Collector 50 -> 50",
                  "Nicol Bolas 46 -> 46", "The Madcap Jester 45 -> 44", "Grixistax October 2026 45 -> 44"):
            self.assertIn(s, note)
        self.assertIn("Owner-removed or rejected cards and classes", note)

    def test_owner_direction_flagged_override_and_removed_not_readded(self):
        adds = set(self.packet["final_changes"]["adds"])
        cuts = set(self.packet["final_changes"]["cuts"])
        removed = ("Bone Miser", "Fell Specter", "Hypnotic Specter", "Sangromancer", "Feed the Swarm", "Megrim",
                   "Counterspell", "Burning Inquiry", "Winds of Change", "The Locust God")
        for card in removed:
            self.assertNotIn(card, adds)
        owner_kept = ("Lightning Greaves", "Thousand-Year Elixir", "Magewright's Stone", "Patriar's Seal", "Bottomless Pit",
                      "Oppression", "Chains of Mephistopheles", "Notion Thief", "Waste Not", "Geth's Grimoire",
                      "Liliana's Caress", "Tinybones, Trinket Thief", "Tinybones, Bauble Burglar",
                      "Tergrid, God of Fright // Tergrid's Lantern", "Underworld Breach", "Kess, Dissident Mage",
                      "Mind Twist", "Illusionist's Bracers", "Pemmin's Aura", "Tinybones, Pocket Nuisance",
                      "Withering Torment", "Minamo, School at Water's Edge")
        for keep in owner_kept:
            self.assertNotIn(keep, cuts)
        # The one cut is a blueprint-named card, so the override is flagged rather than hidden.
        self.assertIn("Flagged: Dauthi is named in the owner's blueprint", self.packet["final_changes"]["coherent_package_tradeoff"])
        for rej in ("Whispering Madness", "Swiftfoot Boots", "Drown in the Loch", "Kederekt Parasite", "Lavaborn Muse",
                    "Rankle, Master of Pranks", "Tinybones, the Pickpocket", "Davriel, Rogue Shadowmage",
                    "Vizier of Tumbling Sands", "Retreat to Coralhelm", "Sulfurous Springs", "Mana Vault"):
            self.assertEqual(self.judged[rej]["judgment"], "REJECT", rej)
        for alt in ("Aphetto Alchemist", "Rings of Brighthearth"):
            self.assertEqual(self.judged[alt]["judgment"], "RETAIN_ALTERNATIVE", alt)
        self.assertEqual(self.judged["Jeweled Lotus"]["judgment"], "EXCLUDE_INVALID")
        self.assertEqual(self.judged["Megrim"]["judgment"], "EXCLUDE_INVALID")
        self.assertEqual(self.judged["Hymn to Tourach"]["judgment"], "SELECT_ADD")
        self.assertGreaterEqual(len(self.judged), 10)
        self.assertGreaterEqual(len(self.packet["whole_deck_audit"]["weakest_slots"]), 8)

    def test_power_bracket_tags_game_changers_and_combo_disclosure(self):
        v = self.packet["verification"]
        self.assertEqual(v["power_bracket"], 4)
        self.assertEqual(v["archidekt_tags"], ["Discard", "Wheels", "Untap"])
        ceiling = self.packet["commander_identity"]["natural_ceiling"]
        self.assertIn("Game Changers: 17 in both baseline and candidate", ceiling)
        self.assertIn("1 -> 1 complete combo (1368-2706-3518", ceiling)
        self.assertIn("almost-included 52 -> 50", ceiling)
        csb = json.dumps(json.loads((RC / f"{D}_CommanderSpellbook_20261023.json").read_text()))
        for cid in ("1368-2706-3518", "283-4091"):
            self.assertIn(cid, csb)

    def test_alternatives_staged_as_complete_hundreds(self):
        def load(name):
            return Counter(gate.parse_list(RC / f"{D}_{name}_20261023.txt")[0])
        a = load("PassC_plus_AphettoAlchemist_minus_MagewrightsStone")
        self.assertEqual((a["Aphetto Alchemist"], a["Magewright's Stone"], a["Dauthi Voidwalker"], sum(a.values())), (1, 0, 1, 100))
        b = load("PassC_plus_RingsOfBrighthearth_minus_MindTwist")
        self.assertEqual((b["Rings of Brighthearth"], b["Mind Twist"], b["Dauthi Voidwalker"], sum(b.values())), (1, 0, 1, 100))
        c = load("one_RingsOfBrighthearth_over_DauthiVoidwalker")
        self.assertEqual((c["Rings of Brighthearth"], c["Dauthi Voidwalker"], c["Hymn to Tourach"], sum(c.values())), (1, 0, 0, 100))
        d = load("two_HymnToTourach_AphettoAlchemist_over_Dauthi_MagewrightsStone")
        self.assertEqual((d["Hymn to Tourach"], d["Aphetto Alchemist"], d["Dauthi Voidwalker"], d["Magewright's Stone"],
                          sum(d.values())), (1, 1, 0, 0, 100))
        w = load("two_WhisperingMadness_over_ReforgeTheSoul")
        self.assertEqual((w["Whispering Madness"], w["Reforge the Soul"], w["Hymn to Tourach"], sum(w.values())), (1, 0, 1, 100))
        s = load("challenge_SulfurousSprings_over_CrumblingNecropolis")
        self.assertEqual((s["Sulfurous Springs"], s["Crumbling Necropolis"], sum(s.values())), (1, 0, 100))

    def test_commander_legal_released_no_exception(self):
        snap = json.loads((ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json").read_text())
        g = [c for c in snap["cards"] if c["name"] == "Gwendlyn Di Corci"][0]
        self.assertEqual(g["commander_legality"], "legal")
        self.assertIs(g["game_changer"], False)
        self.assertEqual((g["set"], g["released_at"]), ("me3", "2009-09-07"))
        self.assertEqual(snap["project_exceptions"], "0")

    def test_no_approval_or_lock_markers_in_new_artifacts(self):
        for p in [PACKET, ROOT / self.packet["final_candidate"]["path"]]:
            text = p.read_text()
            self.assertNotIn("CANONICAL_LOCKED", text)
            self.assertNotIn('"APPROVED"', text)


if __name__ == "__main__":
    unittest.main()
