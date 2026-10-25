"""Deck 30 Lord_Xander__the_Collector (Lord Xander, the Collector) M7 research candidate: structural checks only, not
approval.

The packet is RESEARCH_ONLY_WITHDRAWN_NOT_OWNER_PRESENTABLE and BLOCKED: the existing M6 Pass C Stage A seal does not match
its committed stage_a.md (so no J bundle can pass the shared checker), and only three genuine swaps were found
(+Necromancy -Persist, FLAGGED explicit owner keep; +Swiftfoot Boots -Lightning Greaves; +Malakir Rebirth // Malakir Mire
-Bojuka Bog), below the five-swap floor. Owner-keeping alternatives A and B are staged as complete 100s. Nothing is
padded."""
from __future__ import annotations
import ast
import hashlib
import json
import unittest
from collections import Counter
from pathlib import Path

from scripts import grixis_m7_decision_gate as gate

ROOT = Path(__file__).resolve().parents[1]
D = "Lord_Xander__the_Collector"
XANDER = "Lord Xander, the Collector"
PACKET = ROOT / f"data/grixis/m7/decision_reviews/{D}.json"
BASE = ROOT / f"data/grixis/m7/baseline_sources/{D}_approved_source_2026-10-14.txt"
RAW = "92cdc2f9c1a3583ccf6a311679db66bef825dac2902761859e929f268b6b4787"
CAND_RAW = "8dc209682c00608e1d903b41988ac7bcec540005624ef7938593ee520f1a28c8"
LH = "lh1:84233c9153b8b1c86c521ce4734dab8515e49f448776f66e6c2a450772db773a"
CAND_LH = "lh1:51caa7ea583ad70417bbdf4e1c896e2db3a87021e87fe0425d452bd911fe3620"
RC = ROOT / "data/grixis/m7/research_challengers"
NEC, BOOTS, MAL = "Necromancy", "Swiftfoot Boots", "Malakir Rebirth // Malakir Mire"
PER, GRE, BOG = "Persist", "Lightning Greaves", "Bojuka Bog"
KAR, OFFER = "Karlach, Fury of Avernus", "An Offer You Can't Refuse"


class LordXanderM7Tests(unittest.TestCase):
    def setUp(self):
        self.packet = json.loads(PACKET.read_text())
        self.registry = json.loads((ROOT / "data/grixis/registry.json").read_text())
        self.judged = {c["card"]: c for c in self.packet["material_candidates"]}

    def cand(self):
        return Counter(gate.parse_list(ROOT / self.packet["final_candidate"]["path"])[0])

    def test_gate_passes_as_withdrawn_research_only_with_seal_blocker(self):
        result = gate.verify_packet(self.packet, root=ROOT, registry=self.registry)
        self.assertFalse(result["owner_presentable"])
        self.assertEqual(result["new_swaps"], 3)
        self.assertEqual(result["status"], "M7_WITHDRAWN_RESEARCH_ONLY_NOT_OWNER_PRESENTABLE")
        self.assertEqual(self.packet["readiness"], "RESEARCH_ONLY_WITHDRAWN_NOT_OWNER_PRESENTABLE")
        reason = self.packet["withdrawal_reason"]
        for s in ("RESEARCH_ONLY and BLOCKED", "Seal blocker", "commit bca97b98",
                  "89a78d803b5cb5ea886b2402828aaff00b78497db0b3c0fe569c6c0ee5a879d1",
                  "826f07707a6fdd1583b815ba6b80ad99bd8a71d57d03ac05766ed2a0a4cd0322",
                  "Stage A source diverged from separately sealed byte commitment",
                  "The sealed evidence and the checker are not edited", "Only three genuine swaps",
                  "FLAGGED owner-keep override", "NOT owner approved"):
            self.assertIn(s, reason)
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
        self.assertEqual(self.registry["decks"][D]["commanders"], [XANDER])

    def test_exactly_three_swaps_against_vendored_and_canonical_source(self):
        cand = self.cand()
        path, md = gate.canonical_source(ROOT, self.registry["decks"][D])
        for base in (Counter(gate.parse_list(BASE)[0]), Counter(gate.parse_list(path, source_markdown=md)[0])):
            self.assertEqual(sorted((cand - base).elements()), sorted([NEC, BOOTS, MAL]))
            self.assertEqual(sorted((base - cand).elements()), sorted([PER, GRE, BOG]))
        self.assertEqual(self.packet["final_changes"]["adds"], [NEC, BOOTS, MAL])
        self.assertEqual(self.packet["final_changes"]["cuts"], [PER, GRE, BOG])

    def test_commander_first_100_physical_with_basics_alphabetical(self):
        lines = [x for x in (ROOT / self.packet["final_candidate"]["path"]).read_text().splitlines() if x.strip()]
        self.assertEqual(lines[0], f"1x {XANDER} [Commander]")
        self.assertEqual(sum(1 for x in lines if x.endswith("[Commander]")), 1)
        self.assertFalse(any("[Companion]" in x for x in lines))
        self.assertEqual(sum(int(x.split("x ", 1)[0]) for x in lines), 100)
        self.assertEqual(sorted(x for x in lines if not x.startswith("1x ")), ["2x Island", "2x Mountain", "2x Swamp"])
        rest = [x.split("x ", 1)[1] for x in lines[1:]]
        self.assertEqual(rest, sorted(rest, key=str.lower))
        self.assertEqual(len(set(rest)), 96)

    def test_commander_first_identity_and_distinctness(self):
        plan = self.packet["commander_identity"]["mechanical_plan"]
        for s in ("snc, released 2022-04-29", "not a Game Changer", "no project exception", "discards half their hand",
                  "mills half their library", "sacrifices half their nonland permanents"):
            self.assertIn(s, plan)
        note = self.packet["commander_identity"]["anti_homogenization"]
        self.assertIn("Commander-first to Xander's Oracle", note)
        for s in ("Cormela, Glamour Thief 52/52", "Kess, Dissident Mage 52/52", "Kefka, Court Mage 51/51",
                  "Mai and Zuko 49/51", "Gwendlyn Di Corci 48/50", "Malakir Rebirth in none"):
            self.assertIn(s, note)

    def test_owner_direction_removed_not_readded_owner_cards_kept_and_judgments(self):
        cand = self.cand()
        for card in ("Grindstone", "Painter's Servant", "Narset, Parter of Veils", "Reliquary Tower", "Fractured Sanity",
                     "Ruin Crab", "Hedron Crab", "Consuming Aberration", "Syr Konrad, the Grim", "The Mindskinner",
                     "Fleet Swallower", "Traumatize", "The Master of Lake-town", "Irenicus's Vile Duplication",
                     "Phyrexian Metamorph", "Panharmonicon", "Displacer Kitten", "Deadeye Navigator",
                     "Kitsune's Technique", "Thassa's Oracle", "Demonic Consultation", "Glasspool Mimic // Glasspool Shore",
                     PER, GRE, BOG, "Goryo's Vengeance", "Kiki-Jiki, Mirror Breaker", "Seize the Day"):
            self.assertNotIn(card, cand)
        core = self.packet["commander_identity"]["protected_core"]
        self.assertIn(PER, core)  # explicit owner keep, cut and FLAGGED
        for keep in core:
            self.assertEqual(cand[keep], 0 if keep == PER else 1, keep)
        for owner in ("Auton Soldier", "Phantasmal Image", "Cruel Calculations", "Hall of Echoes"):
            self.assertEqual(cand[owner], 1, owner)
        self.assertEqual([c for c, v in self.judged.items() if v["judgment"] == "SELECT_ADD"], [NEC, BOOTS, MAL])
        self.assertEqual(self.judged[NEC]["named_cuts"], [PER, KAR, OFFER])
        for alt in ("Goryo's Vengeance", "Kiki-Jiki, Mirror Breaker"):
            self.assertEqual(self.judged[alt]["judgment"], "RETAIN_ALTERNATIVE", alt)
        for rej in ("Seize the Day", "Glasspool Mimic // Glasspool Shore", "Chrome Mox", "Command Beacon",
                    "Dualcaster Mage", "Mirror-Mad Phantasm", "Dauthi Voidwalker", "Counterspell", "Mental Misstep",
                    "Waste Not", "Twinflame", "Splinter Twin", "Supernatural Stamina", "Undying Evil",
                    "Fake Your Own Death", "Victimize", "Mox Diamond", "The Master of Lake-town", "Phyrexian Metamorph"):
            self.assertEqual(self.judged[rej]["judgment"], "REJECT", rej)
        self.assertEqual(self.judged["Sorin of House Markov // Sorin, Ravenous Neonate"]["judgment"], "EXCLUDE_INVALID")
        self.assertEqual(len(self.judged), 25)
        audit = self.packet["low_swap_heightened_audit"]
        weak = [x["card"] for x in audit["weakest_slot_challenge"]]
        self.assertEqual(len(weak), 13)
        for card in (PER, GRE, BOG, KAR, OFFER, "Training Center", "Gamble"):
            self.assertIn(card, weak)
        pk = [(sorted(p["adds"]), sorted(p["cuts"])) for p in audit["multi_slot_packages"]]
        self.assertEqual(pk[0], (sorted([NEC, BOOTS, MAL]), sorted([PER, GRE, BOG])))
        self.assertEqual(len(pk), 5)

    def test_power_bracket_tags_game_changers(self):
        v = self.packet["verification"]
        self.assertEqual(v["power_bracket"], 4)
        self.assertEqual(v["archidekt_tags"], ["Mill", "Clones", "Optimized"])
        self.assertIn("Game Changers: 20 in both baseline and candidate", self.packet["commander_identity"]["natural_ceiling"])

    def test_alternatives_staged_as_complete_hundreds(self):
        def load(name):
            return Counter(gate.parse_list(RC / f"{D}_{name}_20261023.txt")[0])
        a3, c3 = [NEC, BOOTS, MAL], [PER, GRE, BOG]
        cases = {
            "alt_A_owner_keeps_Necromancy_minus_Karlach": (a3, [KAR, GRE, BOG]),
            "alt_B_owner_keeps_Necromancy_minus_AnOfferYouCantRefuse": (a3, [OFFER, GRE, BOG]),
            "PassC_plus_GoryosVengeance_minus_Persist": (["Goryo's Vengeance", BOOTS, MAL], c3),
            "PassC_plus_SeizeTheDay_minus_Karlach": (a3 + ["Seize the Day"], c3 + [KAR]),
            "staged_plus_KikiJiki_minus_Karlach": (a3 + ["Kiki-Jiki, Mirror Breaker"], c3 + [KAR]),
            "rejected_plus_GlasspoolMimic_minus_TrainingCenter": (a3 + ["Glasspool Mimic // Glasspool Shore"], c3 + ["Training Center"]),
            "rejected_plus_ChromeMox_minus_TalismanOfCreativity": (a3 + ["Chrome Mox"], c3 + ["Talisman of Creativity"]),
            "rejected_plus_CommandBeacon_minus_XandersLounge": (a3 + ["Command Beacon"], c3 + ["Xander's Lounge"]),
        }
        base = Counter(gate.parse_list(BASE)[0])
        owner = ("Auton Soldier", "Phantasmal Image", "Cruel Calculations", "Hall of Echoes")
        for name, (adds, cuts) in cases.items():
            a = load(name)
            self.assertEqual(sum(a.values()), 100, name)
            self.assertEqual(sorted((a - base).elements()), sorted(adds), name)
            self.assertEqual(sorted((base - a).elements()), sorted(cuts), name)
            for o in owner:
                self.assertEqual(a[o], 1, (name, o))
        for name in ("alt_A_owner_keeps_Necromancy_minus_Karlach", "alt_B_owner_keeps_Necromancy_minus_AnOfferYouCantRefuse"):
            a = load(name)
            for keep in self.packet["commander_identity"]["protected_core"]:
                self.assertEqual(a[keep], 1, (name, keep))

    def test_commander_legal_released_no_exception(self):
        snap = json.loads((ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json").read_text())
        cards = {c["name"]: c for c in snap["cards"]}
        g = cards[XANDER]
        self.assertEqual(g["commander_legality"], "legal")
        self.assertIs(g["game_changer"], False)
        self.assertEqual((g["set"], g["released_at"]), ("snc", "2022-04-29"))
        self.assertEqual(snap["project_exceptions"], "0")
        cand = set(gate.parse_list(ROOT / self.packet["final_candidate"]["path"])[0])
        gc = sorted(c["name"].split(" // ")[0] for c in snap["cards"] if c["name"] in cand | {XANDER} and c["game_changer"])
        self.assertEqual(gc, sorted(ast.literal_eval(snap["game_changers_in_candidate"])))
        self.assertEqual(len(gc), 20)

    def test_no_approval_or_lock_markers_in_new_artifacts(self):
        for p in [PACKET, ROOT / self.packet["final_candidate"]["path"]]:
            text = p.read_text()
            self.assertNotIn("CANONICAL_LOCKED", text)
            self.assertNotIn('"APPROVED"', text)


if __name__ == "__main__":
    unittest.main()
