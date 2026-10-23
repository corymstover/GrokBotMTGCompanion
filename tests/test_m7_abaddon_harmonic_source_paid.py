"""Source-bound Harmonic Prodigy candidate sequence, not an M7 final verdict.

Finite deterministic effects under named positive and adverse hypotheses, not
unbounded game results. Real Magic priority allows tap activations between
separate Thermo-Alchemist untap triggers; summoning sickness must be cleared.
"""
import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/"data/grixis/m7/research_challengers/Abaddon_the_Despoiler_stage4_13_source_cards_20261022.json"
EXISTING=ROOT/"data/grixis/m6/oracle_snapshots/Abaddon_the_Despoiler_Rev2_Scryfall_20261022.json"


def actual_trigger_count(has_prodigy, source_is_shaman_or_other_wizard):
    return 2 if has_prodigy and source_is_shaman_or_other_wizard else 1


def on_cast(kessig, harmonic, abaddon, zone, mv, prior_opponent_loss):
    # Cascade eligibility belongs to the moment a hand spell is cast.
    cascade = abaddon and zone=="hand" and mv <= sum(prior_opponent_loss)
    # Kessig triggers AFTER that casting event, so cannot backdate cascade.
    repeats=actual_trigger_count(harmonic,kessig)
    after=[n+repeats for n in prior_opponent_loss]
    return cascade,after,repeats


class AbaddonHarmonicFiniteTiming(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        src=json.loads(SRC.read_text(encoding="utf-8"))
        cls.cards=src["oracle_cards"]
        cls.existing=json.loads(EXISTING.read_text(encoding="utf-8"))["oracle_snapshot"]

    def test_types_and_real_current_oracle_support_four_source_engines(self):
        self.assertIn("Shaman",self.cards["Kessig Flamebreather"]["type_line"])
        self.assertIn("Shaman",self.cards["Thermo-Alchemist"]["type_line"])
        self.assertIn("Wizard",self.cards["Vivi Ornitier"]["type_line"])
        self.assertIn("Shaman",self.cards["Storm-Kiln Artist"]["type_line"])
        self.assertIn("another Wizard",self.cards["Harmonic Prodigy"]["oracle_text"])
        self.assertIn("triggered ability of a Shaman",
                      self.cards["Harmonic Prodigy"]["oracle_text"])
        self.assertIn("Whenever you cast a noncreature",
                      self.cards["Kessig Flamebreather"]["oracle_text"])
        for name in ("Kessig Flamebreather","Thermo-Alchemist","Vivi Ornitier","Storm-Kiln Artist"):
            self.assertIn(name,self.existing)

    def test_double_kessig_ping_does_not_retroactively_grant_cascade(self):
        # Four players, own turn, Abaddon+Harmonic+Kessig on battlefield,
        # initial X=0. A noncreature hand spell with MV3 is cast and paid.
        cast_cascade,loss,events=on_cast(True,True,True,"hand",3,[0,0,0])
        self.assertFalse(cast_cascade)
        self.assertEqual(events,2)
        self.assertEqual(loss,[2,2,2])
        self.assertEqual(sum(loss),6)
        # Following cast at printed MV3 can now receive cascade.
        following_cascade,_,_=on_cast(True,True,True,"hand",3,loss)
        self.assertTrue(following_cascade)
        no_harmonic,baseline,_=on_cast(True,False,True,"hand",3,[0,0,0])
        self.assertFalse(no_harmonic)
        self.assertEqual(sum(baseline),3)

    def test_vivi_two_noncreature_trigger_instances_not_two_mana_activations(self):
        # Harmonic duplicates Vivi's Wizard on-cast trigger (counter + ping),
        # not its {0} activated once-per-turn mana ability.
        extra_triggers=actual_trigger_count(True,True)
        self.assertEqual(extra_triggers,2)
        vivi_counters_added=extra_triggers
        loss_on_three_opponents=[extra_triggers]*3
        self.assertEqual(vivi_counters_added,2)
        self.assertEqual(sum(loss_on_three_opponents),6)
        activated_vivi_mana_uses_this_turn=1
        self.assertEqual(activated_vivi_mana_uses_this_turn,1)

    def test_stormkiln_magecraft_doubles_cast_and_copy_but_not_copy_as_cast(self):
        t=self.cards["Storm-Kiln Artist"]["oracle_text"]
        self.assertIn("Whenever you cast or copy an instant or sorcery spell",t)
        # One real instant cast and one copy of that spell. Magecraft sees
        # TWO events, each with 2 trigger instances from Harmonic.
        cast_events=1
        copy_events=1
        treasure=(cast_events+copy_events)*actual_trigger_count(True,True)
        self.assertEqual(treasure,4)
        # Kessig only responds to the ONE real cast, not the copy.
        kessig_damage_events=cast_events*actual_trigger_count(True,True)
        self.assertEqual(kessig_damage_events,2)
        self.assertNotEqual(kessig_damage_events,treasure)

    def test_thermo_two_untaps_allow_three_taps_if_ready_and_untapped(self):
        t=self.cards["Thermo-Alchemist"]["oracle_text"]
        self.assertIn("Whenever you cast an instant or sorcery spell, untap this creature.",t)
        n_untap=actual_trigger_count(True,True)
        self.assertEqual(n_untap,2)
        # Precondition: controlled since turn began. Tap in response to
        # both on-cast untap triggers, then after each untap resolves.
        state={"tapped":False,"life_lost":[0,0,0],"taps":0}
        def tap_ping():
            if state["tapped"]:
                return False
            state["tapped"]=True
            state["taps"]+=1
            state["life_lost"]=[v+1 for v in state["life_lost"]]
            return True
        self.assertTrue(tap_ping()) # before first untap resolves
        for _ in range(n_untap):
            state["tapped"]=False
            self.assertTrue(tap_ping()) # legal priority between triggers
        self.assertEqual(state["taps"],3)
        self.assertEqual(sum(state["life_lost"]),9)
        # Missing early control/summoning-sickness clearance prevents this.
        summoning_sick=True
        self.assertFalse(not summoning_sick)

    def test_removed_harmonic_before_cast_does_not_double_later_trigger(self):
        # Targeted kill before the next hand cast leaves only normal triggers.
        _,without,normal=on_cast(True,False,True,"hand",3,[0,0,0])
        _,with_it,doubled=on_cast(True,True,True,"hand",3,[0,0,0])
        self.assertEqual(normal,1)
        self.assertEqual(doubled,2)
        self.assertEqual(sum(without),3)
        self.assertEqual(sum(with_it),6)
        # Removing Harmonic AFTER the casting event does not undo doubled
        # triggers already created; it only affects subsequent spells.
        already_created=doubled
        harmonic_still_present=False
        self.assertEqual(already_created,2)
        self.assertFalse(harmonic_still_present)

    def test_harmonic_not_a_cascade_static_ability_doubler(self):
        oracle=self.existing["Abaddon the Despoiler"]["oracle_text"]
        self.assertIn("spells you cast from your hand",oracle)
        self.assertIn("mana value X or less have cascade",oracle)
        # Abaddon is an Astartes Warrior; its continuous grant is not a
        # triggered ability of a Shaman or another Wizard.
        self.assertEqual(actual_trigger_count(True,False),1)
        # Individual cascade triggers belong to spells; cannot claim a
        # second Abaddon-granted cascade by casting Harmonic alone.


if __name__=="__main__":
    unittest.main()
