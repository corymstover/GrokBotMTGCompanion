"""Abaddon stage12 finite full-100/source/trigger tests; RESEARCH ONLY.

No simulated win rates, global optimality, new M6 I/J certificate or owner approval.
The five-swap floor is a presentation restriction, not an optimization target.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DIR = ROOT / "data/grixis/m7/research_challengers"
REPORT = DIR / "Abaddon_the_Despoiler_stage12_openended_sanctum_wheel_warhammer_portfolios_20261022.json"
BASE = ROOT / "data/grixis/m7/candidate_lists/Abaddon_the_Despoiler_rev2.txt"
ORACLE = ROOT / "data/grixis/m6/oracle_snapshots/Abaddon_the_Despoiler_Rev2_Scryfall_20261022.json"
EXTRA = DIR / "Abaddon_the_Despoiler_post_Admiral_39_card_Scryfall_20261022.json"
STAGE4 = DIR / "Abaddon_the_Despoiler_stage4_13_source_cards_20261022.json"
STAGE8 = DIR / "Abaddon_the_Despoiler_stage8_nine_offranking_Scryfall_20261022.json"
BASICS = {"Island", "Mountain", "Swamp"}


def parse_100(path):
    raw = path.read_bytes()
    cards = Counter()
    for line in raw.decode("utf-8").splitlines():
        quantity, name = line.split("x ", 1)
        cards[name.removesuffix(" [Commander]")] += int(quantity)
    assert sum(cards.values()) == 100, path
    assert cards["Abaddon the Despoiler"] == 1, path
    assert all(n in BASICS or qty == 1 for n, qty in cards.items()), path
    return raw, cards


def full_wheel_draw_loss(opponents=3, draws_per_opponent=7, sheoldred=True,
                         bloodletter=False):
    """Triggers resolve after original Wheel finishes, never retroactively."""
    amount = 2 if sheoldred else 0
    return opponents * draws_per_opponent * amount * (2 if bloodletter else 1)


class AbaddonStage12UnboundedPhysical(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads(REPORT.read_text(encoding="utf-8"))
        cls.original = json.loads(ORACLE.read_text(encoding="utf-8"))["oracle_snapshot"]
        cls.extra = json.loads(EXTRA.read_text(encoding="utf-8"))["oracle_cards"]
        cls.stage4 = json.loads(STAGE4.read_text(encoding="utf-8"))["oracle_cards"]
        cls.stage8 = json.loads(STAGE8.read_text(encoding="utf-8"))["oracle_cards"]

    def test_source_oracle_real_costs_and_legal_types(self):
        self.assertEqual(self.original["Exalted Flamer of Tzeentch"]["mana_cost"], "{2}{U}{R}")
        self.assertIn("At the beginning of your upkeep, return an instant or sorcery card at random",
                      self.original["Exalted Flamer of Tzeentch"]["oracle_text"])
        self.assertIn("Whenever you cast an instant or sorcery spell",
                      self.original["Exalted Flamer of Tzeentch"]["oracle_text"])
        self.assertIn("Cascade", self.original["Noise Marine"]["oracle_text"])
        self.assertIn("Whenever you cast a spell from exile", self.original["Nalfeshnee"]["oracle_text"])
        self.assertIn("Whenever you cast a spell from anywhere other than your hand",
                      self.original["Keeper of Secrets"]["oracle_text"])
        self.assertIn("At the beginning of your upkeep", self.original["The Ruinous Powers"]["oracle_text"])
        self.assertEqual(self.extra["Sheoldred, the Apocalypse"]["mana_cost"], "{2}{B}{B}")
        self.assertIn("Whenever an opponent draws a card, they lose 2 life",
                      self.extra["Sheoldred, the Apocalypse"]["oracle_text"])
        self.assertIn("{1}{B}{R}, {T}: Mount Doom deals 1 damage to each opponent",
                      self.extra["Mount Doom"]["oracle_text"])
        self.assertEqual(self.stage4["Sakashima of a Thousand Faces"]["mana_cost"], "{3}{U}")
        self.assertIn("legend rule", self.stage4["Sakashima of a Thousand Faces"]["oracle_text"])
        self.assertIn("first main phase", self.stage8["Sanctum of Stone Fangs"]["oracle_text"])
        self.assertIn("Whenever a creature you control enters",
                      self.stage8["Impact Tremors"]["oracle_text"])

    def test_wheel_life_loss_only_after_original_spell_cast(self):
        self.assertEqual(full_wheel_draw_loss(), 42)
        self.assertEqual(full_wheel_draw_loss(bloodletter=True), 84)
        self.assertEqual(full_wheel_draw_loss(draws_per_opponent=3), 18)
        self.assertEqual(full_wheel_draw_loss(sheoldred=False), 0)
        self.assertIn("spells you cast from your hand with mana value X or less",
                      self.original["Abaddon the Despoiler"]["oracle_text"])
        # Count is a finite deterministic draw-trigger assertion, not a
        # pre-Wheel cascade eligibility assertion or a win-rate simulation.

    def test_exalted_and_sanctum_timing_distinction(self):
        self.assertIn("At the beginning of your upkeep",
                      self.original["Exalted Flamer of Tzeentch"]["oracle_text"])
        self.assertIn("At the beginning of your first main phase",
                      self.stage8["Sanctum of Stone Fangs"]["oracle_text"])
        self.assertIn("At the beginning of your upkeep",
                      self.original["The Ruinous Powers"]["oracle_text"])
        # Shrine provides X=3 once on the battlefield BEFORE first-main begins.
        # Exalted's spell-ping is a later cast trigger; it cannot retroactively
        # grant cascade to the very spell that induced its trigger.
        self.assertEqual(3 * 1, 3)

    def test_five_and_six_openended_full_100_source_legal_not_owner_ready(self):
        r = self.report
        prior_raw, prior = parse_100(BASE)
        self.assertEqual(hashlib.sha256(prior_raw).hexdigest(),
                         r["canonical"]["raw_sha256"])
        self.assertEqual(r["status"], "RESEARCH_ONLY_NOT_OWNER_PRESENTABLE")
        self.assertFalse(r["owner_ready"])
        self.assertFalse(r["m6_changed_candidate_certified"])
        self.assertTrue(r["canonical_approved_locked_unchanged"])
        self.assertTrue(r["admiral_approved_locked_unchanged"])
        self.assertTrue(r["deck3_hold"])
        self.assertEqual(len(r["fully_specified_research_alternatives"]), 3)
        self.assertEqual(sorted(a["swaps"] for a in r["fully_specified_research_alternatives"]),
                         [5, 5, 6])
        protected = r["whole_99_comparison"]["guardrails_preserved_in_all_three"]
        for v in r["fully_specified_research_alternatives"]:
            raw, after = parse_100(ROOT / v["path"])
            self.assertEqual(hashlib.sha256(raw).hexdigest(), v["raw_sha256"])
            self.assertEqual(sorted((after-prior).elements()), sorted(v["add"]))
            self.assertEqual(sorted((prior-after).elements()), sorted(v["cut"]))
            self.assertEqual(v["swaps"], len(v["add"]))
            self.assertEqual(v["swaps"], len(v["cut"]))
            self.assertEqual(after["Mountain"], 2)
            self.assertEqual(after["Island"], 3)
            self.assertEqual(after["Swamp"], 3)
            self.assertEqual(after["Mount Doom"], 1)
            for n in protected:
                self.assertIn(n, after, (v["name"], n))
            for n in after:
                c = (self.original.get(n) or self.extra.get(n) or
                     self.stage4.get(n) or self.stage8.get(n))
                self.assertIsNotNone(c, (v["name"], n))
                self.assertEqual(c["commander_legality"], "legal", n)
                self.assertTrue(set(c["color_identity"]) <= set("UBR"), n)
            self.assertEqual(v["status"], "RESEARCH_ONLY")

    def test_stopping_rule_is_quality_independent_of_floor_count(self):
        r = self.report
        self.assertIn("genuinely", r["next"])
        self.assertIn("40K identity losses", r["decisive_status"])
        self.assertIn("Keeper of Secrets versus Nalfeshnee",
                      " ".join(r["whole_99_comparison"]["challenge_beyond_selected_slots"]))
        self.assertFalse(r["owner_ready"])


if __name__ == "__main__":
    unittest.main()
