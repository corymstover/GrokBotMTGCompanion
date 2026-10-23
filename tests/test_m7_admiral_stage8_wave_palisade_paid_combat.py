"""Finite source-bound Admiral M7 stage8 decision: Wave/Palisade/Cannonade.

These fixtures intentionally assume exactly three pre-existing legal Pirate
attackers, legally-blockable paths, no extra static modifiers and spells
resolving. They are bounded counterfactuals, NOT a rules engine, win rate,
M6 I/J certificate, or any owner's M7 approval.
"""
from dataclasses import dataclass
from collections import Counter
import json
from pathlib import Path
import re
import unittest

ROOT=Path(__file__).resolve().parents[1]
RESEARCH=ROOT/"data/grixis/m7/research_challengers"
CANONICAL=ROOT/"data/grixis/m6/authority_snapshots/Admiral_Beckett_Brass_Canonical_Approved_20261022.txt"
FULL=RESEARCH/"Admiral_Beckett_Brass_Full_Source_Oracle_20261022.json"
POST=RESEARCH/"Admiral_Beckett_Brass_eleven_card_live_Scryfall_20261022.json"
WAVE_CANNON=RESEARCH/"Admiral_Beckett_Brass_six_Cosmotronic_Wave_20261022.txt"
WAVE_PALISADE=RESEARCH/"Admiral_Beckett_Brass_six_Wave_Palisade_draw_resilient_20261022.txt"
WAVE_PALISADE_AERIALIST=RESEARCH/"Admiral_Beckett_Brass_seven_Aerialist_Wave_Palisade_draw_resilient_20261022.txt"

@dataclass(frozen=True)
class Blocker:
    pirate: bool
    toughness: int

def eligible_remaining(blockers, spell):
    """Only defensive eligibility after the listed spell has resolved.

    No opposing instant response, protection, damage modification, or other
    blockers modeled. The three Pirate attackers share one defending player.
    """
    if spell=="WAVE":
        return []
    if spell=="PALISADE_CHOOSE_PIRATE":
        return [b for b in blockers if b.pirate]
    if spell=="CANNONADE":
        return [b for b in blockers if b.pirate or b.toughness>2]
    if spell=="NONE":
        return list(blockers)
    raise ValueError(spell)

def possible_pirate_hits(blockers, spell, attackers=3):
    """Conservative bound assuming each remaining blocker can stop one attacker."""
    return max(0, attackers-len(eligible_remaining(blockers,spell)))

def pays(pool, mana_cost):
    """Finite source-count proof for one spell only; cannot pay same sources twice."""
    pool=Counter(pool)
    symbols=re.findall(r"\{([^}]+)\}",mana_cost)
    generic=sum(int(x) for x in symbols if x.isdigit())
    for color in (x for x in symbols if x in {"W","U","B","R","G"}):
        if pool[color]<=0:
            return False
        pool[color]-=1
    return sum(pool.values())>=generic

def names_in(path):
    names=[]
    for line in path.read_text().splitlines():
        if line:
            raw,n=line.split("x ",1)
            names.extend([n.removesuffix(" [Commander]")]*int(raw))
    return names

class AdmiralStage8PayableBlockers(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.full={x["name"]:x for x in json.loads(FULL.read_text())["cards"]}
        cls.post={x["name"]:x for x in json.loads(POST.read_text())["verified_cards"]}

    def test_sources_bound_and_no_borrowed_legality_cert(self):
        wave=self.post["Cosmotronic Wave"]
        palisade=self.full["Raise the Palisade"]
        cannon=self.post["Fiery Cannonade"]
        self.assertEqual((wave["mana_cost"],wave["type_line"]),("{3}{R}","Sorcery"))
        self.assertEqual((palisade["mana_cost"],palisade["type_line"]),("{4}{U}","Sorcery"))
        self.assertEqual((cannon["mana_cost"],cannon["type_line"]),("{2}{R}","Instant"))
        self.assertIn("can't block this turn",wave["oracle_text"])
        self.assertIn("Return all creatures that aren't of the chosen type",palisade["oracle_text"])
        self.assertIn("2 damage to each non-Pirate creature",cannon["oracle_text"])
        self.assertEqual(wave["commander_legality"],"legal")
        self.assertEqual(palisade["legalities"]["commander"],"legal")
        self.assertEqual(cannon["commander_legality"],"legal")

    def test_complete_100_card_packages_preserve_actual_engine_roles(self):
        canon=names_in(CANONICAL)
        self.assertEqual(len(canon),100)
        p=names_in(WAVE_PALISADE)
        q=names_in(WAVE_CANNON)
        a=names_in(WAVE_PALISADE_AERIALIST)
        for names in (p,q,a):
            self.assertEqual(len(names),100)
            self.assertEqual(names[0],"Admiral Beckett Brass")
            self.assertTrue(all(v==1 or n in {"Island","Mountain","Swamp"}
                                for n,v in Counter(names).items()))
        self.assertEqual(sum((Counter(p)-Counter(canon)).values()),6)
        self.assertEqual(sum((Counter(q)-Counter(canon)).values()),6)
        self.assertEqual(sum((Counter(a)-Counter(canon)).values()),7)
        for name in ("Bident of Thassa","The Indomitable","Kindred Discovery",
                     "March of the Drowned","Open into Wonder","Path of Ancestry",
                     "Fiery Cannonade"):
            self.assertIn(name,p)
            self.assertIn(name,a)
        self.assertNotIn("Fiery Cannonade",q)
        self.assertIn("Raise the Palisade",q)
        self.assertNotIn("Raise the Palisade",p)

    def test_payable_four_mana_offensive_window_versus_five(self):
        pool=Counter({"U":1,"B":1,"R":1,"C":1})
        self.assertTrue(pays(pool,self.post["Cosmotronic Wave"]["mana_cost"]))
        self.assertFalse(pays(pool,self.full["Raise the Palisade"]["mana_cost"]))
        self.assertFalse(pays(pool,self.post["Open into Wonder"]["mana_cost"].replace("{X}","{3}")))
        # With a fifth real mana, X=3 Open is payable; its colors require UU.
        pool5=Counter({"U":2,"B":1,"R":1,"C":1})
        self.assertTrue(pays(pool5,"{3}{U}{U}"))
        self.assertTrue(pays(pool5,"{4}{U}"))

    def test_three_nontype_blockers_all_three_offensive_routes_enable_theft(self):
        b=[Blocker(False,4),Blocker(False,4),Blocker(False,4)]
        self.assertEqual(possible_pirate_hits(b,"NONE"),0)
        self.assertEqual(possible_pirate_hits(b,"WAVE"),3)
        self.assertEqual(possible_pirate_hits(b,"PALISADE_CHOOSE_PIRATE"),3)
        self.assertEqual(possible_pirate_hits(b,"CANNONADE"),0)

    def test_pirate_mirror_is_real_difference_waves_cannot_block(self):
        b=[Blocker(True,3),Blocker(True,4),Blocker(True,5)]
        self.assertEqual(possible_pirate_hits(b,"WAVE"),3)
        self.assertEqual(possible_pirate_hits(b,"PALISADE_CHOOSE_PIRATE"),0)
        self.assertEqual(possible_pirate_hits(b,"CANNONADE"),0)
        # Choosing some type other than Pirate to bounce opposing Pirates
        # would also bounce our three Pirate attackers: not a free solution.

    def test_mixed_thick_blockers_one_pirate_remains_after_palisade(self):
        b=[Blocker(False,5),Blocker(False,4),Blocker(True,4),Blocker(True,3)]
        self.assertEqual(possible_pirate_hits(b,"WAVE"),3)
        self.assertEqual(possible_pirate_hits(b,"PALISADE_CHOOSE_PIRATE"),1)
        self.assertEqual(possible_pirate_hits(b,"CANNONADE"),0)

    def test_retained_cannonade_defends_opponent_turn_versus_two_toughness(self):
        b=[Blocker(False,2),Blocker(False,2),Blocker(False,2)]
        self.assertEqual(len(eligible_remaining(b,"CANNONADE")),0)
        self.assertEqual(len(eligible_remaining(b,"WAVE")),0)
        self.assertEqual(self.post["Fiery Cannonade"]["type_line"],"Instant")
        self.assertEqual(self.post["Cosmotronic Wave"]["type_line"],"Sorcery")
        # Above equality is for after resolution ONLY: casting Wave during an
        # opponent's ordinary combat cannot replace Cannonade's instant job.

    def test_longer_term_board_reset_has_opposite_opportunity_cost(self):
        b=[Blocker(False,5)]*3
        self.assertEqual(eligible_remaining(b,"PALISADE_CHOOSE_PIRATE"),[])
        self.assertEqual(eligible_remaining(b,"WAVE"),[])
        # On NEXT turn with no creature recasts: Palisade's bounced creatures
        # still absent; Wave's three defenders remain in place.
        self.assertEqual(possible_pirate_hits([],"NONE"),3)
        self.assertEqual(possible_pirate_hits(b,"NONE"),0)
        # This fixture does not claim opponents cannot recast bounced creatures.

    def test_threshold_is_same_player_and_commander_end_step_survival(self):
        damage_sources_by_player={"A":["pirate1","pirate2"],"B":["pirate3"]}
        self.assertFalse(any(len(set(v))>=3 for v in damage_sources_by_player.values()))
        damage_sources_by_player={"A":["pirate1","pirate2","pirate3"],"B":[]}
        self.assertTrue(any(len(set(v))>=3 for v in damage_sources_by_player.values()))
        commander_present_at_end_step=False
        self.assertFalse(commander_present_at_end_step)
        # It is erroneous to treat a disappeared commander as a theft trigger.

if __name__=="__main__":
    unittest.main()
