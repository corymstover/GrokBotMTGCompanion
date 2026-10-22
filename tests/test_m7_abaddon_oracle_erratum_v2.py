"""Regression for two factual Oracle errors and full physical Abaddon V2 alternatives.

These are source-cited deterministic assertions and physical decklist validation;
they do NOT substitute for a live all-100 Scryfall audit or M6/J certification.
"""
from __future__ import annotations

from collections import Counter
import json
from pathlib import Path
import unittest

from scripts.grixis_m7_decision_gate import parse_list

ROOT = Path(__file__).resolve().parents[1]
FOLDER = ROOT / "data/grixis/m7/research_challengers"
ORACLE = FOLDER / "Abaddon_the_Despoiler_v2_oracle_erratum.json"
PORTFOLIO = FOLDER / "Abaddon_the_Despoiler_portfolio_v2.json"
BASICS = {"Island", "Mountain", "Swamp"}
PROTECTED = {
    "The Lost and the Damned", "Call Forth the Tempest", "The Ruinous Powers",
    "Birgi, God of Storytelling // Harnfel, Horn of Bounty", "Neheb, the Eternal",
    "Loyal Subordinate", "Underworld Breach", "Lion's Eye Diamond", "Brain Freeze"
}
LANDS = set("""Ancient Tomb|Badlands|Blood Crypt|Bloodstained Mire|City of Brass|Command Tower|Exotic Orchard|Flooded Strand|Island|Luxury Suite|Mana Confluence|Marsh Flats|Misty Rainforest|Morphic Pool|Mountain|Otawara, Soaring City|Polluted Delta|Scalding Tarn|Steam Vents|Swamp|Takenuma, Abandoned Mire|Training Center|Underground Sea|Urborg, Tomb of Yawgmoth|Verdant Catacombs|Volcanic Island|Watery Grave|Xander's Lounge""".split("|"))


def mana_value_from_cost(cost: str) -> int:
    if not cost:
        return 0
    import re
    tokens = re.findall(r"\{([^{}]+)\}", cost)
    if "{" + "}{".join(tokens) + "}" != cost:
        raise ValueError("invalid mana cost")
    return sum(int(s) if s.isdecimal() else 1 for s in tokens)


def abaddon_granted_cascade(*, own_turn: bool, cast_from_hand: bool, life_lost: int, mv: int) -> int:
    if life_lost < 0:
        raise ValueError("life loss cannot be negative")
    return int(own_turn and cast_from_hand and mv <= life_lost)


def call_forth_total_cascades(*, own_turn: bool, cast_from_hand: bool, life_lost: int) -> int:
    # Printed DOUBLE cascade applies to casts from any zone; Abaddon adds one iff qualified.
    return 2 + abaddon_granted_cascade(
        own_turn=own_turn, cast_from_hand=cast_from_hand, life_lost=life_lost, mv=8
    )


def lost_spawn_triggers(*, enchantment_controlled: bool, spells_cast_outside_hand: int,
                        lands_entered_outside_hand: int) -> int:
    if min(spells_cast_outside_hand, lands_entered_outside_hand) < 0:
        raise ValueError("negative event count")
    return int(enchantment_controlled) * (spells_cast_outside_hand + lands_entered_outside_hand)


class AbaddonOracleErratumV2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.oracle = json.loads(ORACLE.read_text(encoding="utf-8"))
        cls.portfolio = json.loads(PORTFOLIO.read_text(encoding="utf-8"))
        cls.facts = {c["card"]: c for c in cls.oracle["cards"]}
        cls.baseline, cls.commanders, cls.companions = parse_list(
            ROOT / cls.portfolio["baseline_source_path"]
        )
        cls.baseline_counts = Counter(cls.baseline)

    def test_exact_mana_value_accounting_and_source_links(self):
        self.assertEqual(len(self.facts), 10)
        for name, fact in self.facts.items():
            with self.subTest(card=name):
                self.assertEqual(mana_value_from_cost(fact["mana_cost"]), fact["mana_value"])
                self.assertIn(fact["mana_value"], range(0, 12))
                self.assertTrue(fact["oracle_source"].startswith("https://"))
                self.assertTrue(fact["oracle_signature"])
                self.assertTrue(set(fact["color_identity"]) <= {"B", "R", "U"})
        self.assertEqual(self.facts["The Lost and the Damned"]["mana_cost"], "{1}{U}{R}")
        self.assertEqual(self.facts["The Lost and the Damned"]["mana_value"], 3)
        self.assertEqual(self.facts["Call Forth the Tempest"]["mana_cost"], "{5}{R}{R}{R}")
        self.assertEqual(self.facts["Call Forth the Tempest"]["mana_value"], 8)
        self.assertEqual(self.facts["Keeper of Secrets"]["mana_value"], 6)
        self.assertEqual(self.facts["Inevitable Betrayal"]["mana_value"], 0)
        self.assertEqual({c["card"] for c in self.oracle["corrections"]},
                         {"The Lost and the Damned", "Call Forth the Tempest"})

    def test_double_printed_cascade_and_only_qualified_abaddon_third(self):
        self.assertEqual(call_forth_total_cascades(own_turn=True, cast_from_hand=True, life_lost=7), 2)
        self.assertEqual(call_forth_total_cascades(own_turn=True, cast_from_hand=True, life_lost=8), 3)
        self.assertEqual(call_forth_total_cascades(own_turn=False, cast_from_hand=True, life_lost=40), 2)
        self.assertEqual(call_forth_total_cascades(own_turn=True, cast_from_hand=False, life_lost=40), 2)
        self.assertEqual(abaddon_granted_cascade(own_turn=True, cast_from_hand=True, life_lost=3, mv=3), 1)
        self.assertEqual(abaddon_granted_cascade(own_turn=True, cast_from_hand=True, life_lost=2, mv=3), 0)

    def test_lost_triggers_on_actual_nonhand_cast_not_cascade_trigger_alone(self):
        self.assertEqual(lost_spawn_triggers(enchantment_controlled=True,
                         spells_cast_outside_hand=0, lands_entered_outside_hand=0), 0)
        self.assertEqual(lost_spawn_triggers(enchantment_controlled=True,
                         spells_cast_outside_hand=1, lands_entered_outside_hand=0), 1)
        self.assertEqual(lost_spawn_triggers(enchantment_controlled=True,
                         spells_cast_outside_hand=0, lands_entered_outside_hand=1), 1)
        self.assertEqual(lost_spawn_triggers(enchantment_controlled=True,
                         spells_cast_outside_hand=2, lands_entered_outside_hand=1), 3)
        self.assertEqual(lost_spawn_triggers(enchantment_controlled=False,
                         spells_cast_outside_hand=2, lands_entered_outside_hand=1), 0)
        # Suppressed cascade casting (e.g. Rule of Law) supplies zero nonhand casts.
        self.assertEqual(lost_spawn_triggers(enchantment_controlled=True,
                         spells_cast_outside_hand=0, lands_entered_outside_hand=0), 0)

    def test_four_exact_100_card_v2_staged_variants(self):
        self.assertEqual(len(self.baseline), 100)
        self.assertEqual(self.companions, [])
        self.assertEqual(len(self.commanders), 1)
        self.assertEqual(sum(n in LANDS for n in self.baseline), 34)
        p = self.portfolio
        self.assertEqual(p["stage"], "M7_SOURCE_CORRECTED_RESEARCH_NOT_OWNER_READY")
        self.assertEqual(p["current_preliminary_choice"], "engine_answer_keeper")
        self.assertEqual(p["new_full_list_owner_approvals"], 0)
        self.assertEqual(p["formal_m6_certifications"], 0)
        self.assertEqual(p["canonical_decks_modified"], 0)
        self.assertFalse(p["owner_approved"])
        self.assertFalse(p["stage_m7_final_packet_created"])
        variants=p["candidate_variants"]
        self.assertEqual({v["id"] for v in variants},
                         {"engine_only", "engine_answer_keeper", "engine_answer_betrayal",
                          "combat_answer_keeper"})
        for v in variants:
            with self.subTest(id=v["id"]):
                cards, command, companions = parse_list(ROOT / v["path"])
                self.assertEqual(len(cards), 100)
                self.assertEqual(command, self.commanders)
                self.assertEqual(companions, [])
                self.assertEqual(len(set(cards)), 94)
                self.assertTrue(PROTECTED <= set(cards))
                self.assertEqual(sum(name in LANDS for name in cards), 34)
                self.assertEqual(Counter(cards) - self.baseline_counts, Counter(v["adds"]))
                self.assertEqual(self.baseline_counts - Counter(cards), Counter(v["cuts"]))
                self.assertEqual(len(v["adds"]), len(v["cuts"]))
                self.assertNotIn("The Lost and the Damned", v["cuts"])
                self.assertNotIn("Call Forth the Tempest", v["cuts"])

    def test_historical_v1_identified_and_source_gap_still_open(self):
        p = self.portfolio
        self.assertEqual(p["supersedes"].split("/")[-1],
                         "Abaddon_the_Despoiler_portfolio.json")
        self.assertEqual(p["correction_receipt"].split("/")[-1],
                         ORACLE.name)
        self.assertFalse(self.oracle["claim_complete_100_card_oracle"])
        self.assertFalse(self.oracle["claim_m6_certified"])
        self.assertFalse(self.oracle["claim_m7_ready"])


if __name__ == "__main__":
    unittest.main()
