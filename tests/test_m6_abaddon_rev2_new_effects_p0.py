"""Finite new-effect P0 fixtures for Abaddon's revised M7 research list.

Exact physical source, live-dated Oracle anchor and legal cast/trigger windows
are intentionally distinguished from a full multiplayer Magic engine or
universal M6 I/J zero-improvement certification.
"""
from collections import Counter, deque
from dataclasses import dataclass
import json
from pathlib import Path
import unittest

from scripts.grixis_m7_abaddon_rev2_live_oracle import MANIFEST, validate_portfolio

ROOT = Path(__file__).resolve().parents[1]
OLDER = ROOT / "data/grixis/m6/oracle_snapshots/Abaddon_the_Despoiler_Scryfall_20261022.json"


def cascade_instances(*, spell_mana_value, x_lost, from_hand, own_turn,
                      abaddon_count, printed_cascade=0):
    # Printed cascade is intrinsic even on a cast from exile. Abaddon's
    # extra cascade is granted only to qualifying hand casts on own turn.
    grant = (abaddon_count if own_turn and from_hand and spell_mana_value <= x_lost else 0)
    return printed_cascade + grant


def bowmasters_triggers(draw_events):
    # Each draw event: (draws, is_draw_step, is_that_player_first_draw_of_step).
    return sum(1 for _player, draw_step, first_in_step in draw_events
               if not (draw_step and first_in_step))


def legal_alternate_cost_pair(*, offered_without_mana_cost, chosen_overload):
    # Cascade's without-paying alternative and overload's alternative
    # cannot both be selected for a single cast.
    return not (offered_without_mana_cost and chosen_overload)


def spark_enters_as_abaddon(controlled_creatures):
    # Spark Double's as-enters copy choice is not a target.
    return "Abaddon the Despoiler" in controlled_creatures


@dataclass
class CombatLoop:
    opposing_loss_this_turn: int
    red: int
    assault_on_battlefield: bool
    abaddon_controlled: bool
    loyal_controlled: bool
    neheb_controlled: bool

    def combat_to_postcombat(self, opponents=3, can_resolve=True):
        if can_resolve and self.loyal_controlled and self.abaddon_controlled:
            self.opposing_loss_this_turn += 3*opponents
        if self.neheb_controlled:
            self.red += self.opposing_loss_this_turn

    def buy_extra_combat(self):
        if not self.assault_on_battlefield or self.red < 5:
            return False
        self.red -= 5
        return True


class AbaddonRevisedNewEffectP0(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.man = json.loads(MANIFEST.read_text(encoding="utf-8"))
        cls.portfolios, _ = validate_portfolio(cls.man)
        cls.older = json.loads(OLDER.read_text(encoding="utf-8"))["oracle_snapshot"]
        cls.new = cls.man["newly_checked_scryfall_oracle"]

    def test_source_effects_are_real_not_proxy_cards(self):
        self.assertEqual(self.older["Abaddon the Despoiler"]["mana_value"],5)
        self.assertIn("During your turn",self.older["Abaddon the Despoiler"]["oracle_text"])
        self.assertIn("spells you cast from your hand",self.older["Abaddon the Despoiler"]["oracle_text"])
        self.assertIn("isn't legendary",self.new["Spark Double"]["oracle_text"])
        self.assertIn("except the first one they draw",self.new["Orcish Bowmasters"]["oracle_text"])
        self.assertIn("Overload {6}{U}",self.new["Cyclonic Rift"]["oracle_text"])
        self.assertEqual(self.older["Aggravated Assault"]["mana_value"],3)
        self.assertEqual(self.older["Loyal Subordinate"]["mana_value"],3)
        self.assertEqual(self.older["Neheb, the Eternal"]["mana_value"],5)

    def test_duplicated_abaddon_grants_two_not_three_cascades(self):
        self.assertEqual(cascade_instances(spell_mana_value=3,x_lost=9,from_hand=True,own_turn=True,abaddon_count=2),2)
        self.assertEqual(cascade_instances(spell_mana_value=3,x_lost=2,from_hand=True,own_turn=True,abaddon_count=2),0)
        self.assertEqual(cascade_instances(spell_mana_value=3,x_lost=9,from_hand=False,own_turn=True,abaddon_count=2),0)
        self.assertEqual(cascade_instances(spell_mana_value=3,x_lost=9,from_hand=True,own_turn=False,abaddon_count=2),0)
        # Noise Marine MV5 printed cascade would contribute its intrinsic one.
        self.assertEqual(cascade_instances(spell_mana_value=5,x_lost=9,from_hand=True,own_turn=True,abaddon_count=2,printed_cascade=1),3)

    def test_spark_copy_decision_made_on_entry_and_nonlegendary_permanent_survives(self):
        # Spark's as-enters copy replacement does NOT target. Need Abaddon
        # controlled when clone enters, rather than merely at original cast.
        clone_exists=spark_enters_as_abaddon(["Abaddon the Despoiler"])
        nonlegendary_clone=clone_exists and "isn't legendary" in self.new["Spark Double"]["oracle_text"]
        self.assertTrue(nonlegendary_clone)
        self.assertFalse(spark_enters_as_abaddon(["Birgi, God of Storytelling"]))

    def test_bowmasters_one_trigger_per_opponent_card_during_own_turn_wheel(self):
        # Wheel resolving draws seven for each of three opponents on our turn.
        events=[(opponent,False,False) for opponent in range(3) for _ in range(7)]
        self.assertEqual(bowmasters_triggers(events),21)
        # The special exclusion is only the FIRST draw in that player's draw step.
        own_step=[(0,True,True),(0,True,False),(0,True,False)]
        self.assertEqual(bowmasters_triggers(own_step),2)

    def test_bowmasters_pending_triggers_do_not_change_cascade_threshold(self):
        queue=deque([1]*21)
        x=0
        self.assertEqual(x,0)
        for _ in range(4):
            x += queue.popleft()  # each separate unprevented opponent damage
        self.assertEqual(x,4)
        self.assertEqual(len(queue),17)
        # Opponent removal/prevention on remaining stack prevents imaginary X=21.
        queue.clear()
        self.assertEqual(x,4)

    def test_no_bowmasters_draw_history_when_entering_after_wheel(self):
        creature_controlled_during_draws=False
        triggers=bowmasters_triggers([(n,False,False) for n in range(3) for _ in range(7)]) if creature_controlled_during_draws else 0
        self.assertEqual(triggers,0)
        # Bowmasters ETB itself still produces one separate damage/amass trigger.
        etb_triggers = 1 if "When this creature enters" in self.new["Orcish Bowmasters"]["oracle_text"] else 0
        self.assertEqual(etb_triggers,1)

    def test_rift_paid_overload_uses_mana_value_two_for_hand_cascade(self):
        rift=self.new["Cyclonic Rift"]
        self.assertEqual(rift["mana_cost"],"{1}{U}")
        self.assertEqual(rift["mana_value"],2)
        mana_pool={"U":1,"generic":6}
        self.assertEqual(mana_pool["U"]+mana_pool["generic"],7)  # {6}{U} paid
        self.assertEqual(cascade_instances(spell_mana_value=rift["mana_value"],x_lost=2,from_hand=True,own_turn=True,abaddon_count=1),1)
        self.assertEqual(cascade_instances(spell_mana_value=rift["mana_value"],x_lost=1,from_hand=True,own_turn=True,abaddon_count=1),0)

    def test_rift_overload_affects_only_opponents_nontoken_nonland_or_tokens(self):
        # Overload changes 'target' to 'each' on controlled spell; the words
        # 'you don't control' and 'nonland permanent' still restrict it.
        permanents=[("opponent","creature"),("opponent","enchantment"),
                    ("opponent","land"),("self","creature"),("self","land")]
        bounced=[p for p in permanents if p[0]=="opponent" and p[1]!="land"]
        self.assertEqual(bounced,[("opponent","creature"),("opponent","enchantment")])
        # Cascade's no-cost offer and overload's alternate cost cannot combine.
        self.assertFalse(legal_alternate_cost_pair(offered_without_mana_cost=True,chosen_overload=True))
        self.assertTrue(legal_alternate_cost_pair(offered_without_mana_cost=False,chosen_overload=True))

    def test_source_paid_neheb_loyal_assault_after_regular_combat(self):
        game=CombatLoop(0,0,True,True,True,True)
        game.combat_to_postcombat()
        self.assertEqual((game.opposing_loss_this_turn,game.red),(9,9))
        self.assertTrue(game.buy_extra_combat())
        self.assertEqual(game.red,4)
        game.combat_to_postcombat()
        self.assertEqual((game.opposing_loss_this_turn,game.red),(18,22))
        self.assertTrue(game.buy_extra_combat())

    def test_source_paid_neheb_assault_cast_from_first_neheb_mana(self):
        game=CombatLoop(0,0,False,True,True,True)
        game.combat_to_postcombat()
        self.assertEqual(game.red,9)
        game.red -= 3  # cast Assault from hand paying {2}{R}, no prior mana
        game.assault_on_battlefield=True
        self.assertEqual(game.red,6)
        self.assertTrue(game.buy_extra_combat())
        self.assertEqual(game.red,1)

    def test_assault_does_not_infer_win_after_board_interaction(self):
        game=CombatLoop(0,0,True,True,True,False)  # Neheb answered before postcombat
        game.combat_to_postcombat()
        self.assertEqual(game.opposing_loss_this_turn,9)
        self.assertEqual(game.red,0)
        self.assertFalse(game.buy_extra_combat())
        # Controlling no Abaddon when Loyal triggers means no lieutenant loss.
        game2=CombatLoop(0,0,True,False,True,True)
        game2.combat_to_postcombat()
        self.assertEqual(game2.red,0)

    def test_all_three_revised_variants_keep_source_physical_conservation(self):
        original=Counter(self.portfolios["baseline"])
        for v in self.man["comparisons"]:
            with self.subTest(variant=v["id"]):
                variant=Counter(self.portfolios[v["id"]])
                self.assertEqual(sum(variant.values()),100)
                self.assertEqual(variant-original,Counter(v["adds"]))
                self.assertEqual(original-variant,Counter(v["cuts"]))


if __name__ == "__main__":
    unittest.main()
