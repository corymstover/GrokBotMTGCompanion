"""Deck 23 Inalla, Archmage Ritualist M7 research candidate: structural checks only, not approval.

The packet is RESEARCH_ONLY_WITHDRAWN_NOT_OWNER_PRESENTABLE: zero genuine swaps. The strongest change (+Dualcaster Mage
-Kefka) re-adds an owner-removed card, so it is staged as an owner decision and not counted. Nothing is padded."""
from __future__ import annotations
import hashlib
import json
import unittest
from collections import Counter
from pathlib import Path

from scripts import grixis_m7_decision_gate as gate

ROOT = Path(__file__).resolve().parents[1]
D = "Inalla__Archmage_Ritualist"
PACKET = ROOT / f"data/grixis/m7/decision_reviews/{D}.json"
BASE = ROOT / f"data/grixis/m7/baseline_sources/{D}_approved_source_2026-10-14.txt"
RAW = "81333ac71d483b667af968bf2ab221e1fa0de6edd7c2395170d15786e5b15fa3"
CAND_RAW = "916e056ba387fc7e162a359069f11a1b59e91ffb358931742d2a0b912c6c4ed1"
LH = "lh1:c3f633472c2acd8e07b82551fc781d5cc5dd5a56f1b6388a728fa9ef0c855ccd"
RC = ROOT / "data/grixis/m7/research_challengers"
KEFKA = "Kefka, Court Mage // Kefka, Ruler of Ruin"


class InallaArchmageRitualistM7Tests(unittest.TestCase):
    def setUp(self):
        self.packet = json.loads(PACKET.read_text())
        self.registry = json.loads((ROOT / "data/grixis/registry.json").read_text())
        self.judged = {c["card"]: c for c in self.packet["material_candidates"]}

    def test_gate_passes_as_withdrawn_research_only_not_approval(self):
        result = gate.verify_packet(self.packet, root=ROOT, registry=self.registry)
        self.assertFalse(result["owner_presentable"])
        self.assertEqual(result["new_swaps"], 0)
        self.assertEqual(result["status"], "M7_WITHDRAWN_RESEARCH_ONLY_NOT_OWNER_PRESENTABLE")
        self.assertEqual(self.packet["readiness"], "RESEARCH_ONLY_WITHDRAWN_NOT_OWNER_PRESENTABLE")
        reason = self.packet["withdrawal_reason"]
        self.assertIn("zero genuine swaps were found", reason)
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
        self.assertEqual(hashlib.sha256(cand.read_bytes()).hexdigest(), CAND_RAW)
        self.assertEqual(self.packet["final_candidate"]["sha256"], CAND_RAW)
        self.assertEqual(self.packet["canonical_baseline_logical_hash"], LH)
        self.assertEqual(self.registry["decks"][D]["current_canonical_hash"], LH)

    def test_zero_swaps_against_vendored_and_canonical_source(self):
        cand = Counter(gate.parse_list(ROOT / self.packet["final_candidate"]["path"])[0])
        path, md = gate.canonical_source(ROOT, self.registry["decks"][D])
        for base in (Counter(gate.parse_list(BASE)[0]), Counter(gate.parse_list(path, source_markdown=md)[0])):
            self.assertEqual(cand, base)
        self.assertEqual(self.packet["final_changes"]["adds"], [])
        self.assertEqual(self.packet["final_changes"]["cuts"], [])

    def test_single_commander_first_and_100_physical_singleton(self):
        lines = [x for x in (ROOT / self.packet["final_candidate"]["path"]).read_text().splitlines() if x.strip()]
        self.assertEqual(lines[0], "1x Inalla, Archmage Ritualist [Commander]")
        self.assertEqual(sum(1 for x in lines if x.endswith("[Commander]")), 1)
        self.assertFalse(any("[Companion]" in x for x in lines))
        self.assertEqual(sum(int(x.split("x ", 1)[0]) for x in lines), 100)
        self.assertEqual([x for x in lines if not x.startswith("1x ")], [])
        self.assertIn("1x Island", lines)
        self.assertIn("1x Swamp", lines)
        rest = [x.split("x ", 1)[1] for x in lines[1:]]
        self.assertEqual(rest, sorted(rest, key=str.lower))
        self.assertEqual(len(set(rest)), 99)

    def test_distinctness_note_and_commander_first_identity_recorded(self):
        note = self.packet["commander_identity"]["anti_homogenization"]
        self.assertIn("Commander-first to Inalla's Oracle", note)
        for s in ("Kefka, Court Mage 72", "Kess, Dissident Mage 71", "Jeleva, Nephalia's Scourge 68",
                  "Evelyn, the Covetous 68", "Fire Lord Azula 67"):
            self.assertIn(s, note)
        self.assertIn("Owner-removed or rejected cards and classes", note)
        self.assertIn("Eminence", self.packet["commander_identity"]["mechanical_plan"])

    def test_owner_direction_removed_not_readded_and_owner_decision_staged(self):
        removed = ("Dualcaster Mage", "Snapcaster Mage", "Micromancer", "Samut, Tyrant of Naktamun", "Spectral Arcanist")
        cand = Counter(gate.parse_list(ROOT / self.packet["final_candidate"]["path"])[0])
        for card in removed:
            self.assertNotIn(card, cand)
        self.assertEqual(self.judged["Dualcaster Mage"]["judgment"], "RETAIN_ALTERNATIVE")
        for rej in ("Micromancer", "Snapcaster Mage", "Samut, Tyrant of Naktamun", "Twinflame", "Defense Grid",
                    "Gifts Ungiven", "Tishana's Tidebinder", "Crystal Vein", "Tarnished Citadel", "Jeweled Amulet",
                    "The One Ring", "Mindbreak Trap", "Phantasmal Image", "Buried Alive", "Grim Tutor",
                    "Spectral Arcanist"):
            self.assertEqual(self.judged[rej]["judgment"], "REJECT", rej)
        for inv in ("Dockside Extortionist", "Culling Ritual"):
            self.assertEqual(self.judged[inv]["judgment"], "EXCLUDE_INVALID", inv)
        self.assertGreaterEqual(len(self.judged), 10)
        self.assertNotIn("SELECT_ADD", {c["judgment"] for c in self.judged.values()})
        audit = self.packet["low_swap_heightened_audit"]
        weak = {x["card"] for x in audit["weakest_slot_challenge"]}
        self.assertGreaterEqual(len(weak), 10)
        for card in (KEFKA, "Thundertrap Trainer", "Blood Pet", "Wheel of Fortune", "Hoarding Broodlord"):
            self.assertIn(card, weak)
        pk = [(sorted(p["adds"]), sorted(p["cuts"])) for p in audit["multi_slot_packages"]]
        self.assertIn((["Dualcaster Mage", "Snapcaster Mage"], sorted([KEFKA, "Thundertrap Trainer"])), pk)
        self.assertIn((["Defense Grid", "Gifts Ungiven"], sorted([KEFKA, "Blood Pet"])), pk)

    def test_power_bracket_tags_game_changers(self):
        v = self.packet["verification"]
        self.assertEqual(v["power_bracket"], 5)
        self.assertEqual(v["archidekt_tags"], ["cEDH", "Wizards", "Combo"])
        self.assertIn("Game Changers: 18 in both baseline and candidate", self.packet["commander_identity"]["natural_ceiling"])

    def test_alternatives_staged_as_complete_hundreds(self):
        def load(name):
            return Counter(gate.parse_list(RC / f"{D}_{name}_20261023.txt")[0])
        a = load("PassC_plus_DualcasterMage_minus_Kefka")
        self.assertEqual((a["Dualcaster Mage"], a[KEFKA], sum(a.values())), (1, 0, 100))
        m = load("PassC_plus_Micromancer_minus_Kefka")
        self.assertEqual((m["Micromancer"], m[KEFKA], sum(m.values())), (1, 0, 100))
        s = load("PassC_plus_SnapcasterMage_minus_ThundertrapTrainer")
        self.assertEqual((s["Snapcaster Mage"], s["Thundertrap Trainer"], sum(s.values())), (1, 0, 100))
        u = load("two_PassC_Dualcaster_Snapcaster_over_Kefka_Trainer")
        self.assertEqual((u["Dualcaster Mage"], u["Snapcaster Mage"], u[KEFKA], u["Thundertrap Trainer"], sum(u.values())),
                         (1, 1, 0, 0, 100))
        g = load("two_DefenseGrid_GiftsUngiven_over_Kefka_BloodPet")
        self.assertEqual((g["Defense Grid"], g["Gifts Ungiven"], g["Blood Pet"], sum(g.values())), (1, 1, 0, 100))
        t = load("one_TishanasTidebinder_over_ThundertrapTrainer")
        self.assertEqual((t["Tishana's Tidebinder"], t["Thundertrap Trainer"], sum(t.values())), (1, 0, 100))

    def test_commander_legal_released_no_exception(self):
        snap = json.loads((ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json").read_text())
        g = [c for c in snap["cards"] if c["name"] == "Inalla, Archmage Ritualist"][0]
        self.assertEqual(g["commander_legality"], "legal")
        self.assertIs(g["game_changer"], False)
        self.assertEqual((g["set"], g["released_at"]), ("c17", "2017-08-25"))
        self.assertEqual(snap["project_exceptions"], "0")

    def test_no_approval_or_lock_markers_in_new_artifacts(self):
        for p in [PACKET, ROOT / self.packet["final_candidate"]["path"]]:
            text = p.read_text()
            self.assertNotIn("CANONICAL_LOCKED", text)
            self.assertNotIn('"APPROVED"', text)


if __name__ == "__main__":
    unittest.main()
