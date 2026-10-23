"""Deck 27 Grixistax___October_2026 (Kraum, Ludevic's Opus + Tevesh Szat, Doom of Fools) M7 research candidate:
structural checks only, not approval.

The packet is RESEARCH_ONLY_WITHDRAWN_NOT_OWNER_PRESENTABLE: two genuine swaps (+Arcane Signet -Mox Amber,
+Bitterblossom -Windfall), below the five-swap floor. Neither cut is an owner addition or explicit keep. Opposition is
staged (not counted); Talisman of Indulgence (Pass C challenger) is dominated by Arcane Signet. Nothing is padded."""
from __future__ import annotations
import hashlib
import json
import unittest
from collections import Counter
from pathlib import Path

from scripts import grixis_m7_decision_gate as gate

ROOT = Path(__file__).resolve().parents[1]
D = "Grixistax___October_2026"
KRAUM = "Kraum, Ludevic's Opus"
TEVESH = "Tevesh Szat, Doom of Fools"
PACKET = ROOT / f"data/grixis/m7/decision_reviews/{D}.json"
BASE = ROOT / f"data/grixis/m7/baseline_sources/{D}_approved_source_2026-10-14.txt"
RAW = "f36346d4ba965db1e098b0aa92d27a968ee3a14c74a2b9401c1a5357f83c025c"
CAND_RAW = "a04f16ba3a75bd53963866fd0b18c0390af54930b5526e6893ac6c6a6503b858"
LH = "lh1:f56e9d1dfe623d6a80dc00e5563e8e3895f739559d334afe04bca64eb56a0e89"
CAND_LH = "lh1:81656e61ce5b299509c70da8d8d39aaa41d6ecfbf4281f05857a936575207baf"
RC = ROOT / "data/grixis/m7/research_challengers"


class GrixistaxM7Tests(unittest.TestCase):
    def setUp(self):
        self.packet = json.loads(PACKET.read_text())
        self.registry = json.loads((ROOT / "data/grixis/registry.json").read_text())
        self.judged = {c["card"]: c for c in self.packet["material_candidates"]}

    def cand(self):
        return Counter(gate.parse_list(ROOT / self.packet["final_candidate"]["path"])[0])

    def test_gate_passes_as_withdrawn_research_only_not_approval(self):
        result = gate.verify_packet(self.packet, root=ROOT, registry=self.registry)
        self.assertFalse(result["owner_presentable"])
        self.assertEqual(result["new_swaps"], 2)
        self.assertEqual(result["status"], "M7_WITHDRAWN_RESEARCH_ONLY_NOT_OWNER_PRESENTABLE")
        self.assertEqual(self.packet["readiness"], "RESEARCH_ONLY_WITHDRAWN_NOT_OWNER_PRESENTABLE")
        reason = self.packet["withdrawal_reason"]
        self.assertIn("two genuine swaps (+Arcane Signet -Mox Amber, +Bitterblossom -Windfall)", reason)
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
        self.assertEqual(self.registry["decks"][D]["commanders"], [KRAUM, TEVESH])

    def test_exactly_two_swaps_against_vendored_and_canonical_source(self):
        cand = self.cand()
        path, md = gate.canonical_source(ROOT, self.registry["decks"][D])
        for base in (Counter(gate.parse_list(BASE)[0]), Counter(gate.parse_list(path, source_markdown=md)[0])):
            self.assertEqual(sorted((cand - base).elements()), ["Arcane Signet", "Bitterblossom"])
            self.assertEqual(sorted((base - cand).elements()), ["Mox Amber", "Windfall"])
        self.assertEqual(self.packet["final_changes"]["adds"], ["Arcane Signet", "Bitterblossom"])
        self.assertEqual(self.packet["final_changes"]["cuts"], ["Mox Amber", "Windfall"])

    def test_two_partner_commanders_first_and_100_physical_with_basics(self):
        lines = [x for x in (ROOT / self.packet["final_candidate"]["path"]).read_text().splitlines() if x.strip()]
        self.assertEqual(lines[:2], [f"1x {KRAUM} [Commander]", f"1x {TEVESH} [Commander]"])
        self.assertEqual(sum(1 for x in lines if x.endswith("[Commander]")), 2)
        self.assertFalse(any("[Companion]" in x for x in lines))
        self.assertEqual(sum(int(x.split("x ", 1)[0]) for x in lines), 100)
        self.assertEqual([x for x in lines if not x.startswith("1x ")], [])
        for basic in ("Island", "Swamp", "Mountain"):
            self.assertIn(f"1x {basic}", lines)
        rest = [x.split("x ", 1)[1] for x in lines[2:]]
        self.assertEqual(rest, sorted(rest, key=str.lower))
        self.assertEqual(len(set(rest)), 98)

    def test_naming_discrepancy_distinctness_and_commander_first_identity(self):
        plan = self.packet["commander_identity"]["mechanical_plan"]
        self.assertIn("The deck ID Grixistax___October_2026 is not a commander name", plan)
        self.assertIn("' // ' only as a pair separator", plan)
        self.assertIn("Commander 2016, c16, released 2016-11-11", plan)
        self.assertIn("Commander Legends, cmr, released 2020-11-20", plan)
        self.assertIn("draw two cards, then draw another card if the sacrificed permanent was a commander", plan)
        note = self.packet["commander_identity"]["anti_homogenization"]
        self.assertIn("Commander-first to Tevesh's sacrifice/draw Oracle and the stax plan", note)
        for s in ("Kefka, Court Mage 68/67", "Rograkh, Son of Rohgahh + Silas Renn 65/66",
                  "Kess, Dissident Mage 65/65", "Jeleva, Nephalia's Scourge 64/64",
                  "Bitterblossom is in none of the four"):
            self.assertIn(s, note)
        self.assertIn("Owner-removed or rejected cards and classes", note)

    def test_owner_direction_removed_not_readded_core_kept_and_judgments(self):
        cand = self.cand()
        for card in ("Arcane Laboratory", "Black Market Connections", "Defense Grid", "Grafdigger's Cage",
                     "Kederekt Parasite", "Nekusar, the Mindrazer", "Phyrexian Tyranny", "Psychosis Crawler",
                     "Exotic Orchard", "Luxury Suite", "Training Center", "Urborg, Tomb of Yawgmoth",
                     "Thassa's Oracle", "Demonic Consultation", "Ad Nauseam", "Rite of Flame", "Cabal Ritual",
                     "Simian Spirit Guide", "Final Fortune", "Borne Upon a Wind", "Gilded Drake", "Dress Down",
                     "Mnemonic Betrayal", "The One Ring", "Hullbreaker Horror", "Stranglehold", "Vexing Bauble",
                     "Chains of Mephistopheles", "Nether Void", "Smokestack", "Sphere of Resistance",
                     "Mox Amber", "Windfall", "Opposition", "Talisman of Indulgence"):
            self.assertNotIn(card, cand)
        for keep in self.packet["commander_identity"]["protected_core"]:
            self.assertEqual(cand[keep], 1, keep)
        for owner in ("Damping Sphere", "Necropotence", "An Offer You Can't Refuse", "Contamination", "Dark Ritual",
                      "Force of Negation", "Mindbreak Trap", "Skullclamp", "Flooded Strand", "Marsh Flats",
                      "Arid Mesa", "Phyrexian Tower", "Trinisphere", "Chalice of the Void", "Blood Moon",
                      "Back to Basics", "Overburden", "Tangle Wire", "Karn, the Great Creator"):
            self.assertEqual(cand[owner], 1, owner)
        self.assertEqual([c for c, v in self.judged.items() if v["judgment"] == "SELECT_ADD"],
                         ["Arcane Signet", "Bitterblossom"])
        self.assertEqual(self.judged["Arcane Signet"]["named_cuts"], ["Mox Amber", "Overburden"])
        self.assertEqual(self.judged["Bitterblossom"]["named_cuts"], ["Windfall", "Cyclonic Rift", "Magus of the Moon"])
        self.assertEqual(self.judged["Opposition"]["judgment"], "RETAIN_ALTERNATIVE")
        for rej in ("Talisman of Indulgence", "Fellwar Stone", "Frozen Aether", "Braids, Cabal Minion", "Strip Mine",
                    "City of Traitors", "Praetor's Grasp", "Snuff Out", "Spell Pierce", "Dispel", "Null Rod",
                    "Urza's Saga", "Sphere of Resistance", "Stasis", "Valley Floodcaller", "Undercity Sewers"):
            self.assertEqual(self.judged[rej]["judgment"], "REJECT", rej)
        self.assertEqual(self.judged["Archon of Emeria"]["judgment"], "EXCLUDE_INVALID")
        self.assertEqual(len(self.judged), 20)
        audit = self.packet["low_swap_heightened_audit"]
        weak = {x["card"] for x in audit["weakest_slot_challenge"]}
        self.assertEqual(len(weak), 17)
        for card in ("Mox Amber", "Windfall", "Static Orb", "Magus of the Moon", "Cyclonic Rift", "Cursed Totem",
                     "Torpor Orb", "Overburden", "Karn, the Great Creator", "Tangle Wire"):
            self.assertIn(card, weak)
        pk = [(sorted(p["adds"]), sorted(p["cuts"])) for p in audit["multi_slot_packages"]]
        self.assertEqual(pk, [(["Arcane Signet", "Bitterblossom"], ["Mox Amber", "Windfall"]),
                              (["Arcane Signet", "Bitterblossom", "Opposition"], ["Mox Amber", "Static Orb", "Windfall"])])

    def test_power_bracket_tags_game_changers(self):
        v = self.packet["verification"]
        self.assertEqual(v["power_bracket"], 5)
        self.assertEqual(v["archidekt_tags"], ["cEDH", "Stax", "Partner"])
        self.assertIn("Game Changers: 22 in both baseline and candidate", self.packet["commander_identity"]["natural_ceiling"])

    def test_alternatives_staged_as_complete_hundreds(self):
        def load(name):
            return Counter(gate.parse_list(RC / f"{D}_{name}_20261023.txt")[0])
        cases = {
            "PassC_plus_TalismanOfIndulgence_minus_MoxAmber": (["Bitterblossom", "Talisman of Indulgence"], ["Mox Amber", "Windfall"]),
            "PassC_plus_ArcaneSignet_minus_Overburden_keep_MoxAmber": (["Arcane Signet", "Bitterblossom"], ["Overburden", "Windfall"]),
            "PassC_plus_ArcaneSignet_minus_MoxAmber_only": (["Arcane Signet"], ["Mox Amber"]),
            "alt_Bitterblossom_over_CyclonicRift_keep_Windfall": (["Arcane Signet", "Bitterblossom"], ["Cyclonic Rift", "Mox Amber"]),
            "alt_Bitterblossom_over_MagusOfTheMoon_keep_Windfall": (["Arcane Signet", "Bitterblossom"], ["Magus of the Moon", "Mox Amber"]),
            "staged_plus_Opposition_minus_StaticOrb": (["Arcane Signet", "Bitterblossom", "Opposition"], ["Mox Amber", "Static Orb", "Windfall"]),
            "staged_plus_Opposition_minus_MagusOfTheMoon": (["Arcane Signet", "Bitterblossom", "Opposition"], ["Magus of the Moon", "Mox Amber", "Windfall"]),
            "rejected_plus_FrozenAether_minus_StaticOrb": (["Arcane Signet", "Bitterblossom", "Frozen Aether"], ["Mox Amber", "Static Orb", "Windfall"]),
            "rejected_plus_StripMine_minus_GemstoneCaverns": (["Arcane Signet", "Bitterblossom", "Strip Mine"], ["Gemstone Caverns", "Mox Amber", "Windfall"]),
        }
        base = Counter(gate.parse_list(BASE)[0])
        for name, (adds, cuts) in cases.items():
            a = load(name)
            self.assertEqual(sum(a.values()), 100, name)
            self.assertEqual(sorted((a - base).elements()), sorted(adds), name)
            self.assertEqual(sorted((base - a).elements()), sorted(cuts), name)

    def test_commanders_legal_released_no_exception(self):
        snap = json.loads((ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json").read_text())
        cards = {c["name"]: c for c in snap["cards"]}
        for name, st, rel in ((KRAUM, "c16", "2016-11-11"), (TEVESH, "cmr", "2020-11-20")):
            g = cards[name]
            self.assertEqual(g["commander_legality"], "legal")
            self.assertIs(g["game_changer"], False)
            self.assertEqual((g["set"], g["released_at"]), (st, rel))
            self.assertIn("Partner", g["oracle_text"])
        self.assertIn("can be your commander", cards[TEVESH]["oracle_text"])
        self.assertEqual(snap["project_exceptions"], "0")
        cand = set(gate.parse_list(ROOT / self.packet["final_candidate"]["path"])[0])
        gc = sorted(c["name"] for c in snap["cards"] if c["name"] in cand | {KRAUM, TEVESH} and c["game_changer"])
        self.assertEqual(len(gc), 22)
        for n in gc:
            self.assertIn(n, snap["game_changers_in_candidate"])

    def test_no_approval_or_lock_markers_in_new_artifacts(self):
        for p in [PACKET, ROOT / self.packet["final_candidate"]["path"]]:
            text = p.read_text()
            self.assertNotIn("CANONICAL_LOCKED", text)
            self.assertNotIn('"APPROVED"', text)


if __name__ == "__main__":
    unittest.main()
