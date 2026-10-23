"""Deck 25 Kefka, Court Mage M7 research candidate: structural checks only, not approval.

The packet is RESEARCH_ONLY_WITHDRAWN_NOT_OWNER_PRESENTABLE: one genuine swap (+Dualcaster Mage -Culling the Weak),
below the five-swap floor. Pass C's requested Entomb tests measured only a small gain; the Talisman of Indulgence
fallback and the Diabolic Intent alternative cut are staged and not counted. Nothing is padded."""
from __future__ import annotations
import hashlib
import json
import unittest
from collections import Counter
from pathlib import Path

from scripts import grixis_m7_decision_gate as gate

ROOT = Path(__file__).resolve().parents[1]
D = "Kefka__Court_Mage"
K = "Kefka, Court Mage // Kefka, Ruler of Ruin"
PACKET = ROOT / f"data/grixis/m7/decision_reviews/{D}.json"
BASE = ROOT / f"data/grixis/m7/baseline_sources/{D}_approved_source_2026-10-14.txt"
RAW = "cd36192fedda7a4f54570fb8b8e4605147b40f9254e6985729097fc998f17b03"
CAND_RAW = "4adf02f9a72586b541e980218257f296a3b42bd22318bc9b59dc3dac967d210c"
LH = "lh1:a858b67801ed8c4703527bd43954e7263653c7b64b1cd1953db9a945d55bbd2e"
CAND_LH = "lh1:ba340792b7383533f17207ac48228ad283d13ad513b0b52d310e6f964f964b01"
RC = ROOT / "data/grixis/m7/research_challengers"


class KefkaCourtMageM7Tests(unittest.TestCase):
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
        self.assertIn("one genuine swap (+Dualcaster Mage -Culling the Weak)", reason)
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
        self.assertIn(CAND_LH, self.packet["final_candidate"]["deckwide_reconciliation"])

    def test_exactly_one_swap_against_vendored_and_canonical_source(self):
        cand = Counter(gate.parse_list(ROOT / self.packet["final_candidate"]["path"])[0])
        path, md = gate.canonical_source(ROOT, self.registry["decks"][D])
        for base in (Counter(gate.parse_list(BASE)[0]), Counter(gate.parse_list(path, source_markdown=md)[0])):
            self.assertEqual(sorted((cand - base).elements()), ["Dualcaster Mage"])
            self.assertEqual(sorted((base - cand).elements()), ["Culling the Weak"])
        self.assertEqual(self.packet["final_changes"]["adds"], ["Dualcaster Mage"])
        self.assertEqual(self.packet["final_changes"]["cuts"], ["Culling the Weak"])

    def test_single_commander_first_and_100_physical_singleton(self):
        lines = [x for x in (ROOT / self.packet["final_candidate"]["path"]).read_text().splitlines() if x.strip()]
        self.assertEqual(lines[0], f"1x {K} [Commander]")
        self.assertEqual(sum(1 for x in lines if x.endswith("[Commander]")), 1)
        self.assertFalse(any("[Companion]" in x for x in lines))
        self.assertEqual(sum(int(x.split("x ", 1)[0]) for x in lines), 100)
        self.assertEqual([x for x in lines if not x.startswith("1x ")], [])
        self.assertIn("1x Island", lines)
        for basic in ("Swamp", "Mountain"):
            self.assertNotIn(f"1x {basic}", lines)
        rest = [x.split("x ", 1)[1] for x in lines[1:]]
        self.assertEqual(rest, sorted(rest, key=str.lower))
        self.assertEqual(len(set(rest)), 99)

    def test_distinctness_note_and_commander_first_identity_recorded(self):
        note = self.packet["commander_identity"]["anti_homogenization"]
        self.assertIn("Commander-first to Kefka's Oracle", note)
        for s in ("Kess, Dissident Mage 80/80", "Jeleva, Nephalia's Scourge 78/78", "Inalla, Archmage Ritualist 72/73",
                  "Evelyn, the Covetous 67/68", "Inalla runs Kefka itself"):
            self.assertIn(s, note)
        self.assertIn("Owner-removed or rejected cards and classes", note)
        self.assertIn("Owner-direction flag", note)
        plan = self.packet["commander_identity"]["mechanical_plan"]
        self.assertIn("each player discards a card", plan)
        self.assertIn("Harmonic Prodigy doubles it", plan)

    def test_owner_direction_removed_not_readded_keeps_retained_and_alternatives_staged(self):
        cand = Counter(gate.parse_list(ROOT / self.packet["final_candidate"]["path"])[0])
        for card in ("Animate Dead", "Dauthi Voidwalker", "Geth's Grimoire", "Kroxa, Titan of Death's Hunger",
                     "Laughing Mad", "Liliana's Caress", "Megrim", "Monument to Endurance", "Nightscape Familiar",
                     "Sheoldred, the Apocalypse", "Strionic Resonator", "Windfall", "Mountain", "Swamp",
                     "Xander's Lounge", "Exotic Orchard", "Cyclonic Rift", "Opposition Agent", "Psychosis Crawler",
                     "Cursed Totem", "Samut, Tyrant of Naktamun", "Banishing Knack", "Retraction Helix",
                     "The One Ring", "Birgi, God of Storytelling // Harnfel, Horn of Bounty", "Faerie Mastermind"):
            self.assertNotIn(card, cand)
        for keep in ("Gogo, Mysterious Mime", "Hexing Squelcher", "Phyrexian Metamorph", "Tinybones, Bauble Burglar",
                     "Waste Not", "Harmonic Prodigy", "Essence Flux", "Displacer Kitten", "Anger", "Arena of Glory",
                     "Phantasmal Image", "Saw in Half", "Molten Duplication", "Demonic Counsel", "Valley Floodcaller"):
            self.assertEqual(cand[keep], 1, keep)
        dc = self.judged["Dualcaster Mage"]
        self.assertEqual(dc["judgment"], "SELECT_ADD")
        self.assertEqual(dc["confidence"], "MODERATE")
        self.assertEqual(dc["named_cuts"], ["Culling the Weak", "Diabolic Intent"])
        for s in ("0.1706", "0.1867", "497/2232", "861/2232", "Owner-direction flag", "does not require Kefka"):
            self.assertIn(s, dc["adversarial_downside"])
        self.assertEqual(self.judged["Talisman of Indulgence"]["judgment"], "RETAIN_ALTERNATIVE")
        for rej in ("Entomb", "Dragon's Rage Channeler", "Mockingbird", "Vivi Ornitier", "Mistrise Village",
                    "Spark Double", "Vexing Bauble", "Defense Grid", "Praetor's Grasp", "Grinding Station",
                    "Strix Serenade", "Flesh Duplicate", "Twinflame", "Snapcaster Mage", "Mox Amber", "Urza's Saga",
                    "Generator Servant"):
            self.assertEqual(self.judged[rej]["judgment"], "REJECT", rej)
        for inv in ("Dockside Extortionist", "Manamorphose"):
            self.assertEqual(self.judged[inv]["judgment"], "EXCLUDE_INVALID", inv)
        self.assertGreaterEqual(len(self.judged), 10)
        self.assertEqual([c for c, v in self.judged.items() if v["judgment"] == "SELECT_ADD"], ["Dualcaster Mage"])
        self.assertEqual(sorted(self.judged["Entomb"]["named_cuts"]), ["Borne Upon a Wind", "Demonic Counsel"])
        audit = self.packet["low_swap_heightened_audit"]
        weak = {x["card"] for x in audit["weakest_slot_challenge"]}
        self.assertGreaterEqual(len(weak), 10)
        for card in ("Culling the Weak", "Diabolic Intent", "Demonic Counsel", "Borne Upon a Wind",
                     "Tinybones, Bauble Burglar", "Molten Duplication", "Talisman of Creativity", "Island",
                     "Gogo, Mysterious Mime", "Anger"):
            self.assertIn(card, weak)
        pk = [(sorted(p["adds"]), sorted(p["cuts"])) for p in audit["multi_slot_packages"]]
        self.assertEqual(pk, [(["Dragon's Rage Channeler", "Entomb"], ["Demonic Counsel", "Tinybones, Bauble Burglar"])])
        self.assertIn("Only one credible multi-slot package exists", audit["no_two_package_reason"])

    def test_power_bracket_tags_game_changers(self):
        v = self.packet["verification"]
        self.assertEqual(v["power_bracket"], 5)
        self.assertEqual(v["archidekt_tags"], ["cEDH", "Discard", "Clones"])
        self.assertIn("Game Changers: 20 in both baseline and candidate", self.packet["commander_identity"]["natural_ceiling"])

    def test_alternatives_staged_as_complete_hundreds(self):
        def load(name):
            return Counter(gate.parse_list(RC / f"{D}_{name}_20261023.txt")[0])
        cases = {
            "PassC_plus_Entomb_minus_DemonicCounsel": (["Entomb"], ["Demonic Counsel"]),
            "PassC_plus_Entomb_minus_BorneUponAWind": (["Entomb"], ["Borne Upon a Wind"]),
            "PassC_plus_DragonsRageChanneler_minus_TinybonesBaubleBurglar":
                (["Dragon's Rage Channeler"], ["Tinybones, Bauble Burglar"]),
            "PassC_plus_TalismanOfIndulgence_minus_CullingTheWeak": (["Talisman of Indulgence"], ["Culling the Weak"]),
            "one_Mockingbird_over_MoltenDuplication": (["Mockingbird"], ["Molten Duplication"]),
            "one_ViviOrnitier_over_TalismanOfCreativity": (["Vivi Ornitier"], ["Talisman of Creativity"]),
            "one_MistriseVillage_over_Island": (["Mistrise Village"], ["Island"]),
            "one_DualcasterMage_over_DiabolicIntent": (["Dualcaster Mage"], ["Diabolic Intent"]),
            "one_SparkDouble_over_GogoMysteriousMime": (["Spark Double"], ["Gogo, Mysterious Mime"]),
        }
        base = Counter(gate.parse_list(BASE)[0])
        for name, (adds, cuts) in cases.items():
            a = load(name)
            self.assertEqual(sum(a.values()), 100, name)
            self.assertEqual(sorted((a - base).elements()), sorted(adds), name)
            self.assertEqual(sorted((base - a).elements()), sorted(cuts), name)

    def test_commander_legal_released_no_exception(self):
        snap = json.loads((ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json").read_text())
        g = [c for c in snap["cards"] if c["name"] == K][0]
        self.assertEqual(g["commander_legality"], "legal")
        self.assertIs(g["game_changer"], False)
        self.assertEqual((g["set"], g["released_at"]), ("fin", "2025-06-13"))
        self.assertEqual(snap["project_exceptions"], "0")
        cand = set(gate.parse_list(ROOT / self.packet["final_candidate"]["path"])[0])
        gc = sorted(c["name"] for c in snap["cards"] if c["name"] in cand | {K} and c["game_changer"])
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
