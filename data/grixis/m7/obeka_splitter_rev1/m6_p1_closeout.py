"""Current-SHA Obeka Splitter P1 effect-level positive/adversarial checks.

This resolves bounded mechanics but does not prove multiplayer wins, formal M6
I/J zero-improvement, or that retired Darksteel Reactor scenarios passed.
"""

import unittest
from m6_p0_followup import DECK, SHA, ORACLE, extra_upkeeps, sha256


def granted_upkeeps(combat_damage, *, throne=False, staff=False, connected=True):
    if not connected:
        return 0
    # Separate 'additional time' effects each add one trigger, not multiply.
    return extra_upkeeps(unprevented_damage=combat_damage) * (1 + int(throne) + int(staff))


def upkeep_artifacts(upkeeps, *, thopter_network=False, controls_artifact=False,
                     smaug=False, court=False, monarch=False, legal_copy_target=False):
    thopters = upkeeps if thopter_network and controls_artifact else 0
    treasures = upkeeps if smaug else 0
    copies = upkeeps if court and monarch and legal_copy_target else 0
    return thopters + treasures + copies


def sieve_turn(*, sieve_untapped, other_artifacts, keep_sieve=True):
    # Paying the {T}, sacrifice-five-artifacts COST is atomic. Including Time
    # Sieve itself is legal but cannot sustain the same Time Sieve next turn.
    if not sieve_untapped:
        return False
    return other_artifacts >= (5 if keep_sieve else 4)


def mechanized_production_upkeeps(existing_same_name_artifacts, upkeeps,
                                 *, enchantment_attached=True):
    if not enchantment_attached or upkeeps <= 0:
        return False
    # At each upkeep, create one matching token THEN check eight same-name.
    return existing_same_name_artifacts + upkeeps >= 8


class ObekaCurrentP1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        assert sha256(DECK.read_bytes()).hexdigest() == SHA
        cls.names = {line.split("x ", 1)[1].split(" [")[0] for line in
                     DECK.read_text().splitlines() if line.strip()}

    def require(self, *names):
        for name in names:
            self.assertIn(name, self.names)
            self.assertEqual(ORACLE[name]["commander_legality"], "legal")

    def test_K4_throne_chooses_actual_ogre_or_warlock_type(self):
        self.require("Roaming Throne", "Obeka, Splitter of Seconds")
        self.assertIn("Ogre Warlock", ORACLE["Obeka, Splitter of Seconds"]["type_line"])
        self.assertIn("additional time", ORACLE["Roaming Throne"]["oracle_text"])
        self.assertEqual(granted_upkeeps(3, throne=True), 6)
        self.assertEqual(granted_upkeeps(3, throne=False), 3)
        self.assertEqual(granted_upkeeps(3, throne=True, connected=False), 0)

    def test_E2_two_independent_trigger_multipliers_add_not_exponentiate(self):
        self.require("Roaming Throne", "Wizard's Staff", "Mjölnir, Hammer of Thor")
        self.assertIn("additional time", ORACLE["Wizard's Staff"]["oracle_text"])
        self.assertEqual(granted_upkeeps(2, throne=True, staff=True), 6)
        self.assertNotEqual(granted_upkeeps(2, throne=True, staff=True), 8)
        self.assertEqual(granted_upkeeps(4, connected=False, throne=True, staff=True), 0)

    def test_K5_E1_upkeep_artifact_generation_requires_live_sources(self):
        self.require("Time Sieve", "Thopter Spy Network", "Smaug the Magnificent",
                     "Court of Vantress")
        self.assertIn("if you control an artifact", ORACLE["Thopter Spy Network"]["oracle_text"])
        self.assertIn("If you're the monarch", ORACLE["Court of Vantress"]["oracle_text"])
        self.assertEqual(upkeep_artifacts(4, thopter_network=True, controls_artifact=True), 4)
        self.assertEqual(upkeep_artifacts(4, thopter_network=True, controls_artifact=False), 0)
        self.assertEqual(upkeep_artifacts(4, smaug=True), 4)
        self.assertEqual(upkeep_artifacts(4, court=True, monarch=False,
                                          legal_copy_target=True), 0)
        self.assertEqual(upkeep_artifacts(4, court=True, monarch=True,
                                          legal_copy_target=True), 4)

    def test_W1_time_sieve_extra_turn_is_conditional_not_automatic_infinite(self):
        self.require("Time Sieve", "Thopter Spy Network", "Smaug the Magnificent")
        self.assertIn("Sacrifice five artifacts", ORACLE["Time Sieve"]["oracle_text"])
        produced = upkeep_artifacts(5, smaug=True)
        self.assertTrue(sieve_turn(sieve_untapped=True, other_artifacts=produced,
                                   keep_sieve=True))
        self.assertFalse(sieve_turn(sieve_untapped=True, other_artifacts=4,
                                    keep_sieve=True))
        self.assertTrue(sieve_turn(sieve_untapped=True, other_artifacts=4,
                                   keep_sieve=False))
        self.assertFalse(sieve_turn(sieve_untapped=False, other_artifacts=10))
        # A repeat requires connecting with Obeka AGAIN on the extra turn,
        # enough newly generated artifacts, surviving engines and legal attacks.

    def test_K6_W2_mechanized_wins_but_darksteel_source_was_removed(self):
        self.require("Mechanized Production")
        self.assertNotIn("Darksteel Reactor", self.names)
        self.assertIn("eight or more artifacts with the same name",
                      ORACLE["Mechanized Production"]["oracle_text"])
        self.assertTrue(mechanized_production_upkeeps(1, 7))
        self.assertFalse(mechanized_production_upkeeps(1, 6))
        self.assertFalse(mechanized_production_upkeeps(1, 7,
                                                      enchantment_attached=False))
        # Darksteel Reactor original-case branch needs inapplicable disposition.

    def test_W3_unblocked_combat_needed_to_gain_upkeep_value(self):
        self.require("Obeka, Splitter of Seconds", "Smaug the Magnificent")
        u = granted_upkeeps(3, connected=True)
        self.assertEqual(upkeep_artifacts(u, smaug=True), 3)
        self.assertEqual(upkeep_artifacts(granted_upkeeps(3, connected=False),
                                          smaug=True), 0)

    def test_F2_removal_timing_and_sieve_cost_paid_before_responses(self):
        self.require("Time Sieve")
        self.assertTrue(sieve_turn(sieve_untapped=True, other_artifacts=5))
        # If all 5 sacrifices were paid, removing Sieve in response to the
        # *activated ability* does not undo the already-paid cost or extra turn.
        self.assertFalse(sieve_turn(sieve_untapped=False, other_artifacts=5))

    def test_F3_setup_cost_and_false_mana_free_assumption(self):
        self.require("Obeka, Splitter of Seconds", "Time Sieve",
                     "Mechanized Production", "Thopter Spy Network")
        self.assertEqual(ORACLE["Time Sieve"]["mana_cost"], "{U}{B}")
        self.assertEqual(ORACLE["Mechanized Production"]["mana_cost"], "{2}{U}{U}")
        self.assertEqual(ORACLE["Thopter Spy Network"]["mana_cost"], "{2}{U}{U}")
        # On-turn engine setup is not free: Obeka also costs 1UBR to cast,
        # and each protection/attack enabler has its own mana/tempo demand.
        self.assertEqual(ORACLE["Obeka, Splitter of Seconds"]["mana_cost"], "{1}{U}{B}{R}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
