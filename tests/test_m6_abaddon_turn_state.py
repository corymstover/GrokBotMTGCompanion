"""Adversarial tests for Cycle 96's deliberately limited real-effect micro-engine."""
import sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from grixis_m6_abaddon_turn_state import TurnState,Unsupported,scenarios,build

class AbaddonStateTests(unittest.TestCase):
 def test_trigger_timing_cannot_retroactively_cascade(self):
  s=TurnState(hand=["Test Spark","Test Spark"],mana={"C":2})
  s.place("Abaddon the Despoiler");s.place("Kessig Flamebreather")
  self.assertEqual(s.cast("Test Spark"),0)
  self.assertEqual(s.lost,0)
  s.resolve_all()
  self.assertEqual(s.lost,3)
  self.assertEqual(s.cast("Test Spark"),1)
  s.resolve_all()
  self.assertEqual(s.lost,6)
 def test_birgi_post_cast_mana_and_no_free_spell(self):
  s=TurnState(hand=["Boltwave","Boltwave"],mana={"R":1})
  s.place("Birgi, God of Storytelling")
  s.cast("Boltwave")
  self.assertEqual(s.mana["R"],0)
  with self.assertRaises(ValueError):s.cast("Boltwave")
  s.resolve_top()
  self.assertEqual(s.mana["R"],1)
  self.assertEqual(s.cast("Boltwave"),0)
  s.resolve_all()
  self.assertEqual(s.lost,18)
 def test_heartless_source_after_activation_lki(self):
  s=TurnState(turn=6)
  s.place("Heartless Hidetsugu",entered=5)
  s.tap_activate("Heartless Hidetsugu");s.remove("Heartless Hidetsugu")
  s.resolve_all()
  self.assertEqual(s.opponents,[20,20,16])
  self.assertEqual(s.pilot,20)
  self.assertEqual(s.lost,54)
 def test_tree_source_gone_fails_not_damaging(self):
  s=TurnState(turn=6)
  s.place("Tree of Perdition",entered=5)
  s.tap_activate("Tree of Perdition",target=0)
  s.remove("Tree of Perdition");s.resolve_all()
  self.assertEqual(s.opponents,[40,39,31]);self.assertEqual(s.lost,0)
 def test_summoning_sickness_and_next_turn_reset(self):
  s=TurnState()
  s.place("Tree of Perdition",entered=1)
  with self.assertRaises(ValueError):s.tap_activate("Tree of Perdition")
  s.lost=27
  s.next_turn()
  self.assertEqual(s.lost,0)
  s.tap_activate("Tree of Perdition")
  s.resolve_all();self.assertEqual(s.lost,27)
 def test_printed_cascade_survives_commander_absence(self):
  a=TurnState(hand=["Bituminous Blast"],mana={"B":1,"R":1,"C":3},
              library=["Test Echo"])
  self.assertEqual(a.cast("Bituminous Blast"),1)
  a.resolve_all()
  self.assertEqual(len([e for e in a.events if e["event"]=="cascade_hit"]),1)
 def test_double_cascade_and_exile_not_regranted(self):
  s=TurnState(hand=["Bituminous Blast"],mana={"B":1,"R":1,"C":3},
              library=["Test Echo","Test Land","Test Spark"])
  s.place("Abaddon the Despoiler")
  s.lost=5
  self.assertEqual(s.cast("Bituminous Blast"),2)
  s.resolve_all()
  c=[e for e in s.events if e["event"]=="cast"]
  self.assertEqual(len(c),3)
  self.assertEqual(sum(e["granted_cascade"] for e in c),1)
  self.assertTrue(all(e["granted_cascade"]==0 for e in c[1:]))
 def test_no_targets_and_no_cast_from_graveyard(self):
  s=TurnState(hand=["Bituminous Blast"],mana={"B":1,"R":1,"C":3},target_creature=False)
  with self.assertRaises(ValueError):s.cast("Bituminous Blast")
  with self.assertRaises(ValueError):s.cast("Test Echo","graveyard",free=True)
  self.assertEqual(len(s.hand),1)
 def test_commander_tax_and_color_requires_actual_payment(self):
  s=TurnState(mana={"U":1,"B":1,"R":1,"C":2})
  self.assertEqual(s.cast("Abaddon the Despoiler",origin="command"),0)
  s.resolve_all()
  self.assertIn("Abaddon the Despoiler",s.board)
  s.remove("Abaddon the Despoiler")
  s.mana={"U":1,"B":1,"R":1,"C":2}
  with self.assertRaises(ValueError):s.cast("Abaddon the Despoiler",origin="command")
  s.mana={"U":1,"B":1,"R":1,"C":4}
  s.cast("Abaddon the Despoiler",origin="command");s.resolve_all()
  self.assertEqual(s.command_casts,2)
 def test_support_removed_response_changes_damage(self):
  s=TurnState(turn=6)
  s.place("Heartless Hidetsugu",entered=5)
  s.place("Solphim, Mayhem Dominus")
  s.place("Bloodletter of Aclazotz")
  s.tap_activate("Heartless Hidetsugu")
  s.remove("Solphim, Mayhem Dominus")
  s.resolve_all()
  self.assertEqual(s.lost,108)
  self.assertEqual(s.pilot,20)
 def test_prevention_and_game_end(self):
  s=TurnState(hand=["Test Spark"],mana={"C":1})
  s.place("Kessig Flamebreather")
  s.prevent={0,1,2}
  s.cast("Test Spark");s.resolve_all()
  self.assertEqual(s.lost,0)
  h=TurnState(turn=6)
  h.place("Heartless Hidetsugu",entered=5)
  h.place("Solphim, Mayhem Dominus")
  h.place("Bloodletter of Aclazotz")
  h.tap_activate("Heartless Hidetsugu");h.resolve_all()
  self.assertTrue(h.over)
  with self.assertRaises(ValueError):h.cast("Test Spark")
 def test_fail_closed_on_unmodelled_effect(self):
  with self.assertRaises(Unsupported):TurnState(hand=["Force of Will"])
  s=TurnState(hand=["Test Echo"])
  with self.assertRaises(ValueError):s.cast("Test Echo",free=True)
 def test_evidence_reproducible_and_unauthorized(self):
  a=scenarios();b=scenarios()
  self.assertEqual(a,b)
  d=build()
  self.assertEqual(d["scenario_count"],7)
  self.assertFalse(d["full_deck_paired_effect_simulator"])
  self.assertFalse(d["full_phase_b_complete"])
  self.assertFalse(d["supports_improvement_claim"])
  self.assertFalse(any(d["authority"].values()))

if __name__=="__main__":unittest.main()
