"""Deck 24 Jeleva, Nephalia's Scourge M7 research candidate: structural checks only, not approval.

The packet is RESEARCH_ONLY_WITHDRAWN_NOT_OWNER_PRESENTABLE: zero genuine swaps. Pass C's requested Intuition and
Galvanic Iteration tests measured worse; the closest call (+Snap -Gitaxian Probe) is staged as an owner decision and
not counted. Nothing is padded."""
from __future__ import annotations
import hashlib
import json
import unittest
from collections import Counter
from pathlib import Path

from scripts import grixis_m7_decision_gate as gate

ROOT = Path(__file__).resolve().parents[1]
D = "Jeleva__Nephalia_s_Scourge"
J = "Jeleva, Nephalia's Scourge"
PACKET = ROOT / f"data/grixis/m7/decision_reviews/{D}.json"
BASE = ROOT / f"data/grixis/m7/baseline_sources/{D}_approved_source_2026-10-14.txt"
RAW = "00e3f52118f5944684ebc49a5398acf8184f7ca878e861221e4c99931191bc2f"
CAND_RAW = "4818b32a8f8bcbbadef7c4a46bead2b089d1e104d2faa68c4c1c14cd65ce6df1"
LH = "lh1:21c3ebbd08ef90b8499cb9087e5ea26440e3b33615be0a60b8c246ab3b045c4c"
RC = ROOT / "data/grixis/m7/research_challengers"


class JelevaNephaliasScourgeM7Tests(unittest.TestCase):
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
        self.assertEqual(lines[0], f"1x {J} [Commander]")
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
        self.assertIn("Commander-first to Jeleva's Oracle", note)
        for s in ("Kess, Dissident Mage 78", "Kefka, Court Mage 77", "Inalla, Archmage Ritualist 68",
                  "Evelyn, the Covetous 67"):
            self.assertIn(s, note)
        self.assertIn("Owner-removed or rejected cards and classes", note)
        plan = self.packet["commander_identity"]["mechanical_plan"]
        self.assertIn("exiles the top X cards", plan)
        self.assertIn("without paying its mana cost", plan)

    def test_owner_direction_removed_not_readded_and_alternative_staged(self):
        cand = Counter(gate.parse_list(ROOT / self.packet["final_candidate"]["path"])[0])
        for card in ("Mana Drain", "Cyclonic Rift", "Mizzix's Mastery", "Time Stretch", "Nexus of Fate", "Swiftfoot Boots",
                     "Frantic Search", "The One Ring", "Beseech the Mirror", "Praetor's Grasp", "Notion Thief",
                     "Dauthi Voidwalker", "Orcish Bowmasters", "Valley Floodcaller", "Roaming Throne",
                     "Strionic Resonator", "Burnt Offering", "Rain of Filth", "Mountain"):
            self.assertNotIn(card, cand)
        for keep in ("Long-Term Plans", "Scroll Rack", "Opposition Agent", "Hexing Squelcher"):
            self.assertEqual(cand[keep], 1, keep)
        self.assertEqual(self.judged["Snap"]["judgment"], "RETAIN_ALTERNATIVE")
        for rej in ("Intuition", "Galvanic Iteration", "Spellseeker", "Forbidden Orchard", "Hanweir Battlements",
                    "Dramatic Reversal", "Isochron Scepter", "Reanimate", "Merchant Scroll", "Mox Amber",
                    "Starting Town", "Hall of the Bandit Lord", "Goblin Bushwhacker", "Snapback", "Twinflame",
                    "Conjurer's Closet", "Insidious Dreams", "Cruel Tutor", "Savage Beating"):
            self.assertEqual(self.judged[rej]["judgment"], "REJECT", rej)
        for inv in ("Dockside Extortionist", "Manamorphose"):
            self.assertEqual(self.judged[inv]["judgment"], "EXCLUDE_INVALID", inv)
        self.assertGreaterEqual(len(self.judged), 10)
        self.assertNotIn("SELECT_ADD", {c["judgment"] for c in self.judged.values()})
        self.assertEqual(sorted(self.judged["Intuition"]["named_cuts"]), ["Long-Term Plans", "Scheming Symmetry"])
        audit = self.packet["low_swap_heightened_audit"]
        weak = {x["card"] for x in audit["weakest_slot_challenge"]}
        self.assertGreaterEqual(len(weak), 8)
        for card in ("Long-Term Plans", "Scheming Symmetry", "Borne Upon a Wind", "Gitaxian Probe", "Scroll Rack",
                     "Personal Tutor", "Arena of Glory", "Mox Opal"):
            self.assertIn(card, weak)
        pk = [(sorted(p["adds"]), sorted(p["cuts"])) for p in audit["multi_slot_packages"]]
        self.assertEqual(pk, [(["Dramatic Reversal", "Isochron Scepter"], ["Personal Tutor", "Scroll Rack"])])
        self.assertIn("Only one credible multi-slot package exists", audit["no_two_package_reason"])

    def test_power_bracket_tags_game_changers(self):
        v = self.packet["verification"]
        self.assertEqual(v["power_bracket"], 5)
        self.assertEqual(v["archidekt_tags"], ["cEDH", "Spellslinger", "Combo"])
        self.assertIn("Game Changers: 20 in both baseline and candidate", self.packet["commander_identity"]["natural_ceiling"])

    def test_alternatives_staged_as_complete_hundreds(self):
        def load(name):
            return Counter(gate.parse_list(RC / f"{D}_{name}_20261023.txt")[0])
        cases = {
            "PassC_plus_Intuition_minus_LongTermPlans": (["Intuition"], ["Long-Term Plans"]),
            "PassC_plus_Intuition_minus_SchemingSymmetry": (["Intuition"], ["Scheming Symmetry"]),
            "PassC_plus_GalvanicIteration_minus_BorneUponAWind": (["Galvanic Iteration"], ["Borne Upon a Wind"]),
            "one_Snap_over_GitaxianProbe": (["Snap"], ["Gitaxian Probe"]),
            "one_Spellseeker_over_MentalMisstep": (["Spellseeker"], ["Mental Misstep"]),
            "one_ForbiddenOrchard_over_ExoticOrchard": (["Forbidden Orchard"], ["Exotic Orchard"]),
            "one_HanweirBattlements_over_ArenaOfGlory": (["Hanweir Battlements"], ["Arena of Glory"]),
            "two_DramaticReversal_IsochronScepter_over_ScrollRack_PersonalTutor":
                (["Dramatic Reversal", "Isochron Scepter"], ["Scroll Rack", "Personal Tutor"]),
        }
        base = Counter(gate.parse_list(BASE)[0])
        for name, (adds, cuts) in cases.items():
            a = load(name)
            self.assertEqual(sum(a.values()), 100, name)
            self.assertEqual(sorted((a - base).elements()), sorted(adds), name)
            self.assertEqual(sorted((base - a).elements()), sorted(cuts), name)

    def test_commander_legal_released_no_exception(self):
        snap = json.loads((ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json").read_text())
        g = [c for c in snap["cards"] if c["name"] == J][0]
        self.assertEqual(g["commander_legality"], "legal")
        self.assertIs(g["game_changer"], False)
        self.assertEqual((g["set"], g["released_at"]), ("c13", "2013-11-01"))
        self.assertEqual(snap["project_exceptions"], "0")
        cand = set(gate.parse_list(ROOT / self.packet["final_candidate"]["path"])[0])
        gc = sorted(c["name"] for c in snap["cards"] if c["name"] in cand | {J} and c["game_changer"])
        self.assertEqual(len(gc), 20)
        for n in gc:
            self.assertIn(n, snap["game_changers_in_candidate"])

    def test_no_approval_or_lock_markers_in_new_artifacts(self):
        for p in [PACKET, ROOT / self.packet["final_candidate"]["path"]]:
            text = p.read_text()
            self.assertNotIn("CANONICAL_LOCKED", text)
            self.assertNotIn('"APPROVED"', text)


if __name__ == "__main__":
    unittest.main()
