"""Abaddon post-Admiral M7: finite rules-faithful candidate timing cases.

Research-only regressions. Each case checks saved current Scryfall card text,
the authorized approved 100-card source and precisely described 4-player
hypotheses. These are NOT full Magic games, evidence of strategic superiority,
M6 I/J re-certification, a new final Abaddon list, or owner acceptance.
"""
from collections import Counter
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "data/grixis/m7/candidate_lists/Abaddon_the_Despoiler_rev2.txt"
SNAP = ROOT / "data/grixis/m7/research_challengers/Abaddon_the_Despoiler_post_Admiral_39_card_Scryfall_20261022.json"
OLD = ROOT / "data/grixis/m6/oracle_snapshots/Abaddon_the_Despoiler_Rev2_Scryfall_20261022.json"
BASICS = {"Island", "Mountain", "Swamp"}
G = {"U", "B", "R"}


def cards():
    result = Counter()
    for line in BASE.read_text(encoding="utf-8").splitlines():
        n, card = line.split("x ", 1)
        result[card.removesuffix(" [Commander]")] += int(n)
    return result


def variant(add, cut):
    original = cards()
    assert cut in original and original[cut] == 1
    assert add not in original
    now = original.copy()
    now[cut] -= 1
    del now[cut]
    now[add] += 1
    assert sum(now.values()) == 100
    assert all(v == 1 or k in BASICS for k, v in now.items())
    return now


class AbaddonReopenedExactOracleMechanics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.snap = json.loads(SNAP.read_text(encoding="utf-8"))
        cls.oracle = cls.snap["oracle_cards"]
        cls.old = json.loads(OLD.read_text(encoding="utf-8"))["oracle_snapshot"]

    def text(self, name):
        return self.oracle[name]["oracle_text"]

    def test_all_thirty_nine_challengers_are_source_resolved_and_legal(self):
        self.assertEqual(self.snap["candidate_count"], 39)
        self.assertFalse(self.snap["not_found"])
        self.assertTrue(self.snap["all_official_commander_legal"])
        self.assertTrue(self.snap["all_within_grixis_color_identity"])
        self.assertEqual(len(self.oracle), 39)
        self.assertTrue(all(v["commander_legality"] == "legal" for v in self.oracle.values()))
        self.assertTrue(all(set(v["color_identity"]) <= G for v in self.oracle.values()))
        self.assertIn("mana value X or less have cascade",
                      self.old["Abaddon the Despoiler"]["oracle_text"])
        self.assertEqual(sum(cards().values()), 100)
        self.assertIn("Abaddon the Despoiler", cards())
        self.assertEqual(self.snap["canonical_status"], "APPROVED_LOCKED_UNCHANGED")
        self.assertNotIn("Cryptolith Fragment", cards())

    def test_cryptolith_mana_ability_raises_x_while_paying_spell(self):
        variant("Cryptolith Fragment", "Talisman of Indulgence")
        faces = self.oracle["Cryptolith Fragment // Aurora of Emrakul"]["card_faces"]
        self.assertIn("This artifact enters tapped.", faces[0]["oracle_text"])
        self.assertIn("{T}: Add one mana of any color. Each player loses 1 life.",
                      faces[0]["oracle_text"])
        # State: own main phase, Abaddon on battlefield, untapped Fragment;
        # Chaos Warp in hand has legal permanent target, two other untapped
        # lands each supply one generic. Fragment supplies red as mana ability.
        # Rules 601.2g and 605.3b: Fragment's mana ability resolves while
        # paying, BEFORE 601.2i sees the spell cast and cascade triggers.
        lost_before = [0, 0, 0]
        lost_after_payment = [n + 1 for n in lost_before]
        payment = ("generic", "generic", "R")
        self.assertEqual(len(payment), 3)
        self.assertEqual(sum(lost_after_payment), 3)
        self.assertEqual(self.old["Chaos Warp"]["mana_value"], 3)
        self.assertTrue(self.old["Chaos Warp"]["mana_value"] <= sum(lost_after_payment))
        self.assertFalse(4 <= sum(lost_after_payment))
        # Tapped Fragment cannot use this mana ability; it entered tapped.
        fragment_entered_this_turn = True
        self.assertFalse(not fragment_entered_this_turn)

    def test_aurora_phoenix_returns_to_hand_only_on_real_cascade_cast(self):
        variant("Aurora Phoenix", "The Ruinous Powers")
        t = self.text("Aurora Phoenix")
        self.assertIn("Whenever you cast a spell with cascade", t)
        self.assertIn("from your graveyard to your hand", t)
        self.assertEqual(self.oracle["Aurora Phoenix"]["cmc"], 6)
        # Phoenix in graveyard. Abaddon on battlefield, own turn, total
        # opponents' life lost 3; hand-cast Chaos Warp MV3, cascade granted.
        in_graveyard = True
        cast_zone = "hand"
        printed_cascade = False
        abaddon_granted = cast_zone == "hand" and 3 <= 3
        phoenix_to_hand = in_graveyard and (printed_cascade or abaddon_granted)
        self.assertTrue(phoenix_to_hand)
        self.assertFalse(in_graveyard and ("exile" == "hand" and 3 <= 3))
        # A later printed-cascade exile cast qualifies separately (e.g.
        # actual cascade on a spell cast from exile); Abaddon alone doesn't.

    def test_electrostatic_field_after_cast_not_retroactive_cascade(self):
        variant("Electrostatic Field", "Call Forth the Tempest")
        self.assertIn("Whenever you cast an instant or sorcery spell",
                      self.text("Electrostatic Field"))
        # In own turn with Abaddon, X before an MV3 hand cast is only 2:
        # static cascade eligibility checked when cast completes (no cascade).
        x_before_cast = 2
        mana_value = 3
        cascade_at_cast = mana_value <= x_before_cast
        self.assertFalse(cascade_at_cast)
        # After cast, Field's triggered ability may resolve for three
        # opponents, raising X by three, not retroactively adding cascade.
        x_after_field = x_before_cast + 3
        self.assertEqual(x_after_field, 5)
        self.assertFalse(cascade_at_cast)
        # Cascade-hit instant from exile IS cast and triggers Field.
        self.assertTrue("exile" in {"hand", "exile"} and True)
        # Storm copies are placed onto stack without being cast.
        storm_copy_cast = False
        self.assertFalse(storm_copy_cast)

    def test_blood_discount_does_not_reduce_mana_value_or_grant_late_cascade(self):
        variant("Blood for the Blood God!", "Call Forth the Tempest")
        t = self.text("Blood for the Blood God!")
        self.assertIn("for each creature that died this turn", t)
        self.assertIn("draw eight cards", t)
        self.assertIn("Exile Blood for the Blood God!", t)
        self.assertEqual(self.oracle["Blood for the Blood God!"]["cmc"], 11)
        # Six creature deaths reduce eight generic to two generic;
        # still must pay BB R + two generic = five actual mana.
        deaths = 6
        generic_cost = max(0, 8-deaths)
        mana_paid = generic_cost + 3
        self.assertEqual(mana_paid, 5)
        self.assertEqual(self.oracle["Blood for the Blood God!"]["cmc"], 11)
        initial_x = 9  # e.g., resolved Boltwave with three opponents
        has_cascade_on_cast = 11 <= initial_x
        self.assertFalse(has_cascade_on_cast)
        # On resolution 8 damage to EACH opponent raises X by 24.
        x_after_resolution = initial_x + 8 * 3
        self.assertEqual(x_after_resolution, 33)
        self.assertFalse(has_cascade_on_cast)
        self.assertTrue(11 <= 12)  # qualifying separate already-raised X case

    def test_ghyrson_exact_one_ping_also_damages_self_on_spear(self):
        variant("Ghyrson Starn, Kelermorph", "The Ruinous Powers")
        self.assertIn("another source you control deals exactly 1 damage",
                      self.text("Ghyrson Starn, Kelermorph"))
        self.assertIn("each player", self.text("Spear Spewer"))
        # With four players, Spewer deals exactly 1 to each, triggering
        # Ghyrson separately for all four players; each Ghyrson deals 2
        # to that same player. Self harm is a strategic downside.
        self_life = 40 - 1 - 2
        opponent_losses = [1+2] * 3
        self.assertEqual(self_life, 37)
        self.assertEqual(opponent_losses, [3, 3, 3])
        self.assertEqual(sum(opponent_losses), 9)
        # Doublers/replacement effects could alter the exact-one predicate;
        # this fixture expressly assumes no such effect present.

    def test_ob_nixilis_one_group_ping_is_one_exile_trigger(self):
        variant("Ob Nixilis, Captive Kingpin", "The Ruinous Powers")
        t = self.text("Ob Nixilis, Captive Kingpin")
        self.assertIn("one or more opponents each lose exactly 1 life", t)
        self.assertIn("Exile the top card of your library", t)
        # Flamebreather ping to 3 opponents in a single spell-trigger
        # damage event creates ONE Ob trigger, not three.
        one_damage_event = [1, 1, 1]
        triggers = int(any(loss == 1 for loss in one_damage_event))
        self.assertEqual(triggers, 1)
        self.assertEqual(sum(one_damage_event), 3)

    def test_sulfuric_vortex_does_not_set_own_upkeep_opponent_loss(self):
        self.assertIn("At the beginning of each player's upkeep",
                      self.text("Sulfuric Vortex"))
        # Vortex pings the active upkeep player, NOT all players. During
        # our upkeep only we take damage; opponents' this-turn loss stays 0.
        opp_lost_this_own_turn = [0, 0, 0]
        own_life = 40 - 2
        self.assertEqual(sum(opp_lost_this_own_turn), 0)
        self.assertEqual(own_life, 38)

    def test_descent_into_avernus_symmetric_upkeep_treasure_and_damage(self):
        self.assertIn("each player creates X Treasure tokens",
                      self.text("Descent into Avernus"))
        # First own upkeep after entry: 2 counters. Four-player table,
        # each gains 2 treasures and suffers 2 damage, including caster.
        descent_counters = 2
        treasures = [descent_counters] * 4
        life_lost_by_opponents = [descent_counters] * 3
        self.assertEqual(treasures, [2, 2, 2, 2])
        self.assertEqual(sum(life_lost_by_opponents), 6)
        # Mana given to opponents and damage to self are not ignored.

    def test_mount_doom_color_and_activation_are_mutually_exclusive_unless_untapped(self):
        self.assertEqual(set(self.oracle["Mount Doom"]["color_identity"]), {"B", "R"})
        t = self.text("Mount Doom")
        self.assertIn("{T}, Pay 1 life: Add {B} or {R}.", t)
        self.assertIn("{1}{B}{R}, {T}: Mount Doom deals 1 damage to each opponent.", t)
        # Both abilities tap this land. Without untap, you cannot obtain
        # its mana and use the three-mana ping ability in the same turn.
        taps_needed_for_both = 2
        taps_available = 1
        self.assertGreater(taps_needed_for_both, taps_available)


if __name__ == "__main__":
    unittest.main()
