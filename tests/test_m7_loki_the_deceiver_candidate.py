"""Deck 28 Loki__the_Deceiver (Loki, the Deceiver) M7 research candidate: structural checks only, not approval.

The packet is RESEARCH_ONLY_WITHDRAWN_NOT_OWNER_PRESENTABLE: two genuine swaps (+Ultimo, Civilization's End
-Crimson Cowl, Master of Evil; +Elektra, Daughter of the Hand -Killmonger, Ruthless Usurper), below the five-swap floor.
Neither cut is an owner addition or explicit keep. Strionic Resonator (Pass C) and Victor Timely, Wily Tycoon are staged
(not counted); Seize the Day (Pass C) is rejected. Nothing is padded."""
from __future__ import annotations
import ast
import hashlib
import json
import unittest
from collections import Counter
from pathlib import Path

from scripts import grixis_m7_decision_gate as gate

ROOT = Path(__file__).resolve().parents[1]
D = "Loki__the_Deceiver"
LOKI = "Loki, the Deceiver"
PACKET = ROOT / f"data/grixis/m7/decision_reviews/{D}.json"
BASE = ROOT / f"data/grixis/m7/baseline_sources/{D}_approved_source_2026-10-14.txt"
RAW = "5079291c08c5af212b3d90d63ac5b01849d45c7700b1d64100ef57fb13458062"
CAND_RAW = "ce64e22265467a7032cf7814bbbadb4c215f24e9c3a63f9217bcf2f4f47fcb5d"
LH = "lh1:1af6ee049bf73721081d3bed599d91b174e2487b42630b8b1c51827301e49c68"
CAND_LH = "lh1:d26a9eea1d9d69ecd6c8e029d446bb587ad5b71b75371d494035a1211c1b40d8"
RC = ROOT / "data/grixis/m7/research_challengers"
ULT, ELE = "Ultimo, Civilization's End", "Elektra, Daughter of the Hand"
COWL, KILL = "Crimson Cowl, Master of Evil", "Killmonger, Ruthless Usurper"


class LokiM7Tests(unittest.TestCase):
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
        self.assertIn(f"two genuine swaps (+{ULT} -{COWL}; +{ELE} -{KILL})", reason)
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
        self.assertEqual(self.registry["decks"][D]["commanders"], [LOKI])

    def test_exactly_two_swaps_against_vendored_and_canonical_source(self):
        cand = self.cand()
        path, md = gate.canonical_source(ROOT, self.registry["decks"][D])
        for base in (Counter(gate.parse_list(BASE)[0]), Counter(gate.parse_list(path, source_markdown=md)[0])):
            self.assertEqual(sorted((cand - base).elements()), sorted([ULT, ELE]))
            self.assertEqual(sorted((base - cand).elements()), sorted([COWL, KILL]))
        self.assertEqual(sorted(self.packet["final_changes"]["adds"]), sorted([ULT, ELE]))
        self.assertEqual(sorted(self.packet["final_changes"]["cuts"]), sorted([COWL, KILL]))

    def test_commander_first_100_physical_with_basics_alphabetical(self):
        lines = [x for x in (ROOT / self.packet["final_candidate"]["path"]).read_text().splitlines() if x.strip()]
        self.assertEqual(lines[0], f"1x {LOKI} [Commander]")
        self.assertEqual(sum(1 for x in lines if x.endswith("[Commander]")), 1)
        self.assertFalse(any("[Companion]" in x for x in lines))
        self.assertEqual(sum(int(x.split("x ", 1)[0]) for x in lines), 100)
        self.assertEqual(sorted(x for x in lines if not x.startswith("1x ")), ["2x Mountain", "3x Island", "3x Swamp"])
        rest = [x.split("x ", 1)[1] for x in lines[1:]]
        self.assertEqual(rest, sorted(rest, key=str.lower))
        self.assertEqual(len(set(rest)), 94)  # 95 distinct names including Loki

    def test_commander_first_identity_and_distinctness(self):
        plan = self.packet["commander_identity"]["mechanical_plan"]
        for s in ("Marvel Super Heroes Commander, msc, released 2026-06-26", "not a Game Changer",
                  "attack triggers do not fire on the copy, CR 508.4", "no project exception"):
            self.assertIn(s, plan)
        note = self.packet["commander_identity"]["anti_homogenization"]
        self.assertIn("Commander-first to Loki's Oracle", note)
        for s in ("Doctor Doom, King of Latveria 53/53", "Be'lakor, the Dark Master 42/42",
                  "Admiral Brass, Unsinkable 40/40", "Nathan Drake, Treasure Hunter 40/40",
                  "Construct a Cosmic Cube, The Masters of Evil, Reliquary Tower",
                  "Puppet Master, String Puller and Vulture, Scheming Scavenger", "no additional clone effect"):
            self.assertIn(s, note)

    def test_owner_direction_removed_not_readded_core_kept_and_judgments(self):
        cand = self.cand()
        for card in ("Construct a Cosmic Cube", "The Masters of Evil", "Reliquary Tower", "Kindred Dominance",
                     "Raise the Palisade", "Endless Ranks of HYDRA", "Puppet Master, String Puller",
                     "Vulture, Scheming Scavenger", "Thassa's Oracle", "Demonic Consultation", COWL, KILL,
                     "Strionic Resonator", "Seize the Day", "Victor Timely, Wily Tycoon", "Kindred Charge", "Twinflame",
                     "Helm of the Host", "Glorious Purpose"):
            self.assertNotIn(card, cand)
        for keep in self.packet["commander_identity"]["protected_core"]:
            self.assertEqual(cand[keep], 1, keep)
        for owner in ("Red Ghost, Intangible Genius", "Titan of Littjara", "Hall of Echoes", "Blasphemous Act",
                      "Swiftfoot Boots", "Lightning Greaves", "The Master, Multiplied", "Roaming Throne"):
            self.assertEqual(cand[owner], 1, owner)
        self.assertEqual([c for c, v in self.judged.items() if v["judgment"] == "SELECT_ADD"], [ULT, ELE])
        self.assertEqual(self.judged[ULT]["named_cuts"], [COWL, "Kang Prime"])
        self.assertEqual(self.judged[ELE]["named_cuts"], [KILL, "Iron Monger, Sadistic Tycoon"])
        for alt in ("Strionic Resonator", "Victor Timely, Wily Tycoon"):
            self.assertEqual(self.judged[alt]["judgment"], "RETAIN_ALTERNATIVE", alt)
        for rej in ("Seize the Day", "Kingpin, Wilson Fisk", "Secluded Courtyard", "Tri-Sentinel, Act of Vengeance",
                    "Lady Loki, Agent of Chaos", "Kindred Charge", "Twinflame", "Helm of the Host", "Archnemesis",
                    "Glorious Purpose", "Vampiric Tutor", "Ancient Tomb", "Terminate", "Hostage Taker"):
            self.assertEqual(self.judged[rej]["judgment"], "REJECT", rej)
        for inv in ("Hela, Mistress of Darkness // Dark Tutor", "Mirror Universe Intrusion", "Dockside Extortionist"):
            self.assertEqual(self.judged[inv]["judgment"], "EXCLUDE_INVALID", inv)
        self.assertEqual(len(self.judged), 21)
        audit = self.packet["low_swap_heightened_audit"]
        weak = {x["card"] for x in audit["weakest_slot_challenge"]}
        self.assertEqual(len(weak), 14)
        for card in (COWL, KILL, "Swiftfoot Boots", "Black Market Connections", "Kang Prime",
                     "Iron Monger, Sadistic Tycoon", "Red Ghost, Intangible Genius", "Titan of Littjara", "Hall of Echoes"):
            self.assertIn(card, weak)
        pk = [(sorted(p["adds"]), sorted(p["cuts"])) for p in audit["multi_slot_packages"]]
        self.assertEqual(pk[0], (sorted([ULT, ELE]), sorted([COWL, KILL])))
        self.assertEqual(len(pk), 3)

    def test_power_bracket_tags_game_changers(self):
        v = self.packet["verification"]
        self.assertEqual(v["power_bracket"], 4)
        self.assertEqual(v["archidekt_tags"], ["Villains", "Clones", "Optimized"])
        self.assertIn("Game Changers: 5 in both baseline and candidate", self.packet["commander_identity"]["natural_ceiling"])

    def test_alternatives_staged_as_complete_hundreds(self):
        def load(name):
            return Counter(gate.parse_list(RC / f"{D}_{name}_20261023.txt")[0])
        core_a, core_c = [ULT, ELE], [COWL, KILL]
        cases = {
            "PassC_plus_StrionicResonator_minus_SwiftfootBoots": (core_a + ["Strionic Resonator"], core_c + ["Swiftfoot Boots"]),
            "PassC_plus_SeizeTheDay_minus_BlackMarketConnections": (core_a + ["Seize the Day"], core_c + ["Black Market Connections"]),
            "PassC_plus_SeizeTheDay_minus_UrzasIncubator": (core_a + ["Seize the Day"], core_c + ["Urza's Incubator"]),
            "alt_Ultimo_over_KangPrime_keep_CrimsonCowl": (core_a, [KILL, "Kang Prime"]),
            "alt_Elektra_over_IronMonger_keep_Killmonger": (core_a, [COWL, "Iron Monger, Sadistic Tycoon"]),
            "staged_plus_VictorTimely_minus_KangPrime": (core_a + ["Victor Timely, Wily Tycoon"], core_c + ["Kang Prime"]),
            "rejected_plus_KingpinWilsonFisk_minus_MadameHydra": (core_a + ["Kingpin, Wilson Fisk"], core_c + ["Madame Hydra"]),
            "rejected_plus_SecludedCourtyard_minus_PathOfAncestry": (core_a + ["Secluded Courtyard"], core_c + ["Path of Ancestry"]),
        }
        base = Counter(gate.parse_list(BASE)[0])
        for name, (adds, cuts) in cases.items():
            a = load(name)
            self.assertEqual(sum(a.values()), 100, name)
            self.assertEqual(sorted((a - base).elements()), sorted(adds), name)
            self.assertEqual(sorted((base - a).elements()), sorted(cuts), name)

    def test_commander_legal_released_no_exception(self):
        snap = json.loads((ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json").read_text())
        cards = {c["name"]: c for c in snap["cards"]}
        g = cards[LOKI]
        self.assertEqual(g["commander_legality"], "legal")
        self.assertIs(g["game_changer"], False)
        self.assertEqual((g["set"], g["released_at"]), ("msc", "2026-06-26"))
        self.assertEqual(snap["project_exceptions"], "0")
        cand = set(gate.parse_list(ROOT / self.packet["final_candidate"]["path"])[0])
        gc = sorted(c["name"] for c in snap["cards"] if c["name"] in cand | {LOKI} and c["game_changer"])
        self.assertEqual(gc, sorted(ast.literal_eval(snap["game_changers_in_candidate"])))
        self.assertEqual(len(gc), 5)

    def test_no_approval_or_lock_markers_in_new_artifacts(self):
        for p in [PACKET, ROOT / self.packet["final_candidate"]["path"]]:
            text = p.read_text()
            self.assertNotIn("CANONICAL_LOCKED", text)
            self.assertNotIn('"APPROVED"', text)


if __name__ == "__main__":
    unittest.main()
