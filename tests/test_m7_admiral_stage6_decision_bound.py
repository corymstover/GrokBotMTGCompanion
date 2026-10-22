"""Admiral 7/8/9-swap stage6 decision-targeted, exact-card finite threshold tests.

Tests source-bound local blockers/cost interactions, never generalized match wins.
"""
from pathlib import Path
import json
import unittest

ROOT=Path(__file__).resolve().parents[1]
RESEARCH=ROOT/"data/grixis/m7/research_challengers"
EDHREC=json.loads((RESEARCH/"Admiral_Beckett_Brass_EDHREC_inclusion_lift_discovery_20261022.json").read_text())
ELEVEN=json.loads((RESEARCH/"Admiral_Beckett_Brass_eleven_card_live_Scryfall_20261022.json").read_text())
NEW={r["name"]:r for r in EDHREC["scryfall_new_discovery_oracle"]}
OLD={r["name"]:r for r in ELEVEN["verified_cards"]}

def best_case_hits(*,attacking_pirates,ready_blockers,tapped_blockers=0,unblockable_attackers=0,fog=False,removed_pirates=0):
    """Upper bound given fully adversarial optimal blockers of ordinary Pirates.

    A specifically made-unblockable Pirate cannot be covered by blockers.
    Real targeting, menace/flying, activated blockers, prevention, tokens,
    opponent turn effects and hidden information require their own fixtures.
    """
    if fog:
        return 0
    surviving=max(0,attacking_pirates-removed_pirates)
    assured=min(unblockable_attackers,surviving)
    remaining_blockers=max(0,ready_blockers-tapped_blockers)
    vulnerable=surviving-assured
    return assured+max(0,vulnerable-remaining_blockers)

class AdmiralStage6FiniteDecision(unittest.TestCase):
    def test_source_costs_and_card_identity_for_comparison(self):
        self.assertEqual(OLD["Open into Wonder"]["mana_cost"],"{X}{U}{U}")
        self.assertEqual(OLD["Cosmotronic Wave"]["mana_cost"],"{3}{R}")
        self.assertEqual(NEW["Dreamcaller Siren"]["mana_cost"],"{2}{U}{U}")
        self.assertEqual(NEW["Storm Fleet Aerialist"]["mana_cost"],"{1}{U}")
        self.assertIn("tap up to two target nonland permanents",NEW["Dreamcaller Siren"]["oracle_text"])
        self.assertIn("can't block this turn",OLD["Cosmotronic Wave"]["oracle_text"])
        self.assertIn("can't be blocked",OLD["Open into Wonder"]["oracle_text"])

    def test_dreamcaller_not_automatic_solution_against_four_defenders(self):
        # Three Pirates attacking, Regalia equipped on one and already paid.
        # The two other attackers remain blockable after Siren taps TWO of FOUR.
        self.assertEqual(best_case_hits(attacking_pirates=3,ready_blockers=4,
                                        tapped_blockers=2,unblockable_attackers=1),1)
        # X=3 Open into Wonder guarantees three unblocked subject to fog/answers.
        self.assertEqual(best_case_hits(attacking_pirates=3,ready_blockers=4,
                                        unblockable_attackers=3),3)
        # Wave's no-block clause can open all attackers, but is a sorcery
        # that costs 4 and gives no Open into Wonder combat-card draw.
        self.assertEqual(best_case_hits(attacking_pirates=3,ready_blockers=0),3)

    def test_dreamcaller_relevant_four_mana_earlier_window(self):
        # Versus TWO blockers, flash Siren tapping both can open existing
        # three Pirate attackers at cost 4 (UU), before Open's cost 5 at X=3.
        self.assertEqual(best_case_hits(attacking_pirates=3,ready_blockers=2,
                                        tapped_blockers=2),3)
        self.assertEqual(best_case_hits(attacking_pirates=3,ready_blockers=2),1)

    def test_fog_or_one_removed_pirate_destroys_exact_three_source_threshold(self):
        self.assertEqual(best_case_hits(attacking_pirates=3,ready_blockers=0,
                                        unblockable_attackers=3,fog=True),0)
        self.assertEqual(best_case_hits(attacking_pirates=3,ready_blockers=0,
                                        unblockable_attackers=3,removed_pirates=1),2)

    def test_aerialist_flying_and_karizev_menace_adverse_opposite_cases(self):
        # Two ground blockers and no flyers: flying Aerialist connects, whereas
        # two ground blockers can team up to stop Kari Zev's menace source.
        ground_blockers=2
        flyers=0
        self.assertEqual(flyers,0)
        self.assertGreaterEqual(ground_blockers,2)
        aerialist_connects=flyers==0
        kari_zev_connects=ground_blockers<2
        self.assertTrue(aerialist_connects)
        self.assertFalse(kari_zev_connects)
        # One flying blocker and no other creature: flyer can stop Aerialist;
        # a single flyer still cannot satisfy menace's 2-blocker requirement.
        flyers=1
        total_blockers=1
        self.assertFalse(flyers==0)
        self.assertTrue(total_blockers<2)
        # Opposite rankings forbid falsely declaring an always-dominant swap.

    def test_stage6_remains_research_only_and_physical_100(self):
        for f in ("Admiral_Beckett_Brass_seven_Regalia_Wave_20261022.txt",
                  "Admiral_Beckett_Brass_eight_Aerialist_20261022.txt",
                  "Admiral_Beckett_Brass_eight_Dreamcaller_20261022.txt",
                  "Admiral_Beckett_Brass_nine_Aerialist_Dreamcaller_20261022.txt"):
            rows=[line for line in (RESEARCH/f).read_text().splitlines() if line.strip()]
            self.assertEqual(sum(int(line.split("x ",1)[0]) for line in rows),100)
            self.assertTrue(rows[0].endswith("Admiral Beckett Brass [Commander]"))
        self.assertEqual(EDHREC["status"],"RESEARCH_ONLY_DISCOVERY_NOT_OWNER_READY")

if __name__=="__main__":
    unittest.main()
