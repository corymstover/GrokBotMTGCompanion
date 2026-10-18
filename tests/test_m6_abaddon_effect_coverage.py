"""Cycle 98: fail-closed mana and draw behaviors; frozen Oracle integration in CI."""
import sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_m6_abaddon_effect_coverage as m

def obj(hand,lib,extra_md=None):
 md={name:{"mv":0,"land":False,"front":name} for name in lib+hand}
 md.update(extra_md or {})
 t=m.ExpandedCascade(lib,md,"Bituminous Blast",[40,39,31],
     {"B":3,"R":3,"U":3,"C":5},6)
 # The Cycle-97 constructor intentionally fixes a three-card hand; these
 # isolated effect tests replace it with the explicitly named test hand.
 t.hand=list(hand)
 return t

class TestCycle98Coverage(unittest.TestCase):
 def test_preregistration_scope(self):
  p=m.read(m.PLAN)
  self.assertEqual(len(p["frozen_oracle_assertions"]),10)
  self.assertEqual(p["samples"],240)
  self.assertEqual(len(p["hypotheses"]),2)
  self.assertFalse(any(p["authority"].values()))
  self.assertEqual(set(p["frozen_oracle_assertions"]),set(m.EXTRA_CARDS))

 def test_sol_ring_and_signet_activation(self):
  t=obj(["Boltwave","Bituminous Blast","Flame Rift"],[])
  t.place("Sol Ring",entered=6)
  t.tap_mana("Sol Ring","C")
  self.assertEqual(t.mana["C"],7)
  with self.assertRaises(ValueError):t.tap_mana("Sol Ring","C")
  t.place("Arcane Signet",entered=6)
  t.tap_mana("Arcane Signet","U")
  self.assertEqual(t.mana["U"],4)
  with self.assertRaises(ValueError):t.tap_mana("Arcane Signet","G")

 def test_lotus_petal_must_sacrifice(self):
  t=obj(["Boltwave","Bituminous Blast","Flame Rift"],[])
  t.place("Lotus Petal",entered=6)
  t.tap_mana("Lotus Petal","B")
  self.assertNotIn("Lotus Petal",t.board)
  self.assertIn("Lotus Petal",t.graveyard)
  self.assertEqual(t.mana["B"],4)
  with self.assertRaises(ValueError):t.tap_mana("Lotus Petal","B")

 def test_talisman_damage_not_opponent_life_loss(self):
  t=obj(["Boltwave","Bituminous Blast","Flame Rift"],[])
  t.place("Abaddon the Despoiler",entered=5)
  t.place("Talisman of Dominance",entered=6)
  t.tap_mana("Talisman of Dominance","U")
  self.assertEqual(t.pilot,39)
  self.assertEqual(t.lost,0)
  self.assertEqual(t.opponents,[40,39,31])
  t.next_turn()
  t.tap_mana("Talisman of Dominance","C")
  self.assertEqual(t.pilot,39)

 def test_dark_ritual_and_rite_of_flame(self):
  t=obj(["Dark Ritual","Rite of Flame","Bituminous Blast"],[])
  t.cast("Dark Ritual");t.resolve_all()
  self.assertEqual(t.mana["B"],5) # paid B then gained BBB
  t.cast("Rite of Flame");t.resolve_all()
  self.assertEqual(t.mana["R"],4) # paid R then gained RR
  self.assertIn("Dark Ritual",t.graveyard)
  self.assertIn("Rite of Flame",t.graveyard)

 def test_brainstorm_draw_three_put_two_on_top(self):
  md={"Alpha":{"mv":2,"land":False,"front":"Alpha"},
      "Beta":{"mv":4,"land":False,"front":"Beta"},
      "Gamma":{"mv":1,"land":False,"front":"Gamma"},
      "Flame Rift":{"mv":2,"land":False,"front":"Flame Rift"},
      "Bituminous Blast":{"mv":5,"land":False,"front":"Bituminous Blast"}}
  t=obj(["Brainstorm","Bituminous Blast","Flame Rift"],["Alpha","Beta","Gamma"],md)
  self.assertEqual(t.cast("Brainstorm"),0)
  t.resolve_all()
  self.assertEqual(t.library,["Bituminous Blast","Beta"])
  self.assertEqual(sorted(t.hand),sorted(["Flame Rift","Alpha","Gamma"]))
  e=[x for x in t.events if x["event"]=="expanded_brainstorm"]
  self.assertEqual(e[0]["drawn"],["Alpha","Beta","Gamma"])

 def test_ponder_fixed_policy_keep_order_draw_one(self):
  md={"A":{"mv":2,"land":False,"front":"A"},"B":{"mv":4,"land":False,"front":"B"},
      "C":{"mv":3,"land":False,"front":"C"}}
  t=obj(["Ponder","Bituminous Blast","Flame Rift"],["A","B","C"],md)
  t.cast("Ponder");t.resolve_all()
  self.assertEqual(t.library,["B","C"])
  self.assertIn("A",t.hand)
  self.assertEqual(len([x for x in t.events if x["event"]=="expanded_ponder"]),1)

 def test_unknown_effects_remain_declined(self):
  md={"Demonic Tutor":{"mv":2,"land":False,"front":"Demonic Tutor"}}
  t=obj(["Bituminous Blast","Boltwave","Flame Rift"],["Demonic Tutor"],md)
  t.cast("Bituminous Blast");t.resolve_all()
  o=[x for x in t.events if x["event"]=="real_cascade_offer"]
  self.assertEqual(o[0]["outcome"],"declined_unmodeled")

 def test_ritual_from_cascade_has_no_granted_second_cascade(self):
  md={"Dark Ritual":{"mv":1,"land":False,"front":"Dark Ritual"}}
  t=obj(["Bituminous Blast","Boltwave","Flame Rift"],["Dark Ritual"],md)
  t.place("Abaddon the Despoiler",entered=5)
  t.lost=5
  t.cast("Bituminous Blast");t.resolve_all()
  c=[x for x in t.events if x["event"]=="cast" and x["origin"]=="cascade_exile"]
  self.assertEqual(len(c),1)
  self.assertEqual(c[0]["granted_cascade"],0)
  self.assertTrue(any(x["event"]=="expanded_ritual" for x in t.events))

if __name__=="__main__":unittest.main()
