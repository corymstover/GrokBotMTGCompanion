"""P0-026: ten preregistered, bounded Passionate Archaeologist rules fixtures.

Exact chosen Abaddon 100-card source, 99 physical zone-conserved cards,
commander tracked separately, virtual copied spells/tokens not card sources.
All results conditional: never empirical meta-game likelihood or win rate.
"""
from __future__ import annotations
from collections import Counter
import hashlib
import json
from pathlib import Path
import unittest
from scripts.grixis_m7_decision_gate import parse_list

ROOT=Path(__file__).resolve().parents[1]
PLAN=json.loads((ROOT/"data/grixis/m6/phase_b_plans/abaddon_p0_archaeologist_20261022.json").read_text(encoding="utf-8"))
COMMANDER="Abaddon the Despoiler"
ARCH="Passionate Archaeologist"
CALL="Call Forth the Tempest"
LOYAL="Loyal Subordinate"
LOST="The Lost and the Damned"
KEEPER="Keeper of Secrets"
NALF="Nalfeshnee"
WILD="Wild-Magic Sorcerer"
MV={"Arcane Signet":2,"Sol Ring":1,"Boltwave":1,"Lotus Petal":0}
LANDS=("Mountain",)*3+("Island",)*3+("Swamp",)*2
ZONES=("library","hand","field","stack","graveyard","exile")
OPPONENTS=("A","B","C")


def census(s):
    return sum((Counter(s[k]) for k in ZONES),Counter())


def move(s,card,source,target):
    if card not in s[source]:
        raise AssertionError("Missing physical "+card+" from "+source)
    s[source].remove(card)
    s[target].append(card)


def conserved(s):
    if census(s)!=s["initial"]:
        raise AssertionError("Original physical 99 cards not conserved")
    if s["stack"] or s["exile"]:
        raise AssertionError("Original stack/exile zone unclean")


def stage(*,loss=9,commander_field=True,arch_field=True,nalf=False,
          wild=False,keeper=False,top=("Arcane Signet","Sol Ring","Boltwave")):
    path=ROOT/PLAN["physical_candidate_path"]
    if hashlib.sha256(path.read_bytes()).hexdigest()!=PLAN["physical_candidate_sha256"]:
        raise AssertionError("Full 100-card list hash changed")
    cards,cmd,companions=parse_list(path)
    if len(cards)!=100 or len(set(cards))!=94 or cmd!=[COMMANDER] or companions:
        raise AssertionError("Exact approved-family physical alternative invalid")
    s={z:[] for z in ZONES}
    s["library"]=list(cards[1:])
    s.update({"initial":Counter(cards[1:]),"commander_zone":"field" if commander_field else "command",
              "commander_owned":True,"arch_triggers":[],"arch_total_damage":Counter(),
              "lost_spawn":0,"keeper_damage":0,"life_lost_this_turn":loss,
              "cascade_count":None,"nonhand_casts":[],"cast_history":[],
              "nalf_virtual_copies":[],"nalf_boltwave_virtual_damage_each":0,
              "boltwave_actual_damage_each":0,"wild_extra_cascade_count":0,
              "tap_sources":[],"call_creature_sweep":None,"countered_nonhand":[],
              "virtual_permanent_copy_tokens":[],"timeline":[]})
    move(s,CALL,"library","hand")
    if arch_field: move(s,ARCH,"library","field")
    move(s,LOST,"library","field")
    if nalf: move(s,NALF,"library","field")
    if wild: move(s,WILD,"library","field")
    if keeper: move(s,KEEPER,"library","field")
    if loss==9: move(s,LOYAL,"library","field")
    elif loss!=0: raise AssertionError("Only declared loss X0/X9 states")
    for x in LANDS: move(s,x,"library","field")
    for x in reversed(top):
        if x not in MV or x not in s["library"]:
            raise AssertionError("Unregistered physical cascade hit: "+x)
        s["library"].remove(x)
        s["library"].insert(0,x)
    assert census(s)==s["initial"]
    return s


def paid_call(s):
    if s["tap_sources"] or any(Counter(s["field"])[x]<n for x,n in Counter(LANDS).items()):
        raise AssertionError("Cannot physically pay Call's {5}{R}{R}{R} or tap twice")
    s["tap_sources"].extend(LANDS)
    at_cast=s["life_lost_this_turn"]
    move(s,CALL,"hand","stack")
    s["cast_history"].append((CALL,8,"hand"))
    s["cascade_count"]=2+int(s["commander_zone"]=="field" and at_cast>=8)
    s["timeline"].append(("paid_hand_cast_Call",at_cast,s["cascade_count"]))


def exile_next(s,mv=8):
    if not s["library"]: raise AssertionError("No physical source to reveal")
    name=s["library"].pop(0)
    if name not in MV or MV[name]>=mv:
        raise AssertionError("Unmodeled cascade scan or invalid strictly-lower hit: "+name)
    s["exile"].append(name)
    s["timeline"].append(("cascade_physical_exile",name,mv))
    return name


def arch_trigger(s,card,*,protected=(),target=None,remove_after_trigger=False):
    # The granted ability belongs to a commander CREATURE on battlefield,
    # not to the enchantment itself or commander card in command zone.
    if not(s["commander_zone"]=="field" and s["commander_owned"] and ARCH in s["field"]):
        return
    protected=set(protected)
    requested=target or OPPONENTS[(len(s["nonhand_casts"])-1)%3]
    options=[p for p in OPPONENTS if p not in protected]
    if requested not in options:
        requested=next(iter(options),None)
    if requested is None:
        s["timeline"].append(("arch_no_legal_target_ability_not_on_stack",card))
        return
    # Capture granted trigger on physical *cast*, before countering source or
    # removal of Background; targeted ability uses last-known source.
    item={"card":card,"mv":MV[card],"target":requested,
          "commander_source":COMMANDER,"source_is_owned_commander":True}
    s["arch_triggers"].append(item)
    s["timeline"].append(("arch_triggered_at_cast",card,MV[card],requested))
    if remove_after_trigger:
        move(s,ARCH,"field","graveyard")
        s["timeline"].append(("arch_removed_after_trigger",))
    # A trigger already on stack resolves independently; zero damage still
    # requires a legal target. Damage is NONCOMBAT, never commander combat 21.
    s["arch_total_damage"][requested]+=MV[card]
    s["life_lost_this_turn"]+=MV[card]
    s["timeline"].append(("arch_trigger_resolved",card,requested,MV[card]))


def cast_exiled(s,card,*,target=None,protected=(),counter=False,
                remove_arch=False):
    if card not in s["exile"]: raise AssertionError("Card not actually exiled")
    first=len(s["nonhand_casts"])==0
    has_wild=first and WILD in s["field"]
    has_nalf=NALF in s["field"]
    move(s,card,"exile","stack")
    s["cast_history"].append((card,MV[card],"cast_from_cascade_exile"))
    s["nonhand_casts"].append(card)
    s["lost_spawn"]+=int(LOST in s["field"])
    if KEEPER in s["field"]: s["keeper_damage"]+=MV[card]
    arch_trigger(s,card,protected=protected,target=target,remove_after_trigger=remove_arch)
    # Copies are never cast; a physical card yields at most one Nalf copy
    # event, even when original gets a separate cascade.
    if has_nalf:
        s["nalf_virtual_copies"].append({"card":card,"cast":False,"physical":False})
        if card=="Boltwave":
            s["nalf_boltwave_virtual_damage_each"]+=3
            s["life_lost_this_turn"]+=9  # conditional 3 opponents with no prevention
        else:
            s["virtual_permanent_copy_tokens"].append({"card":card,"cast":False,"end_step_sacrifice":True})
    if counter:
        move(s,card,"stack","graveyard")
        s["countered_nonhand"].append(card)
        s["timeline"].append(("original_countered_after_cast_triggers_exist",card))
    if has_wild:
        s["wild_extra_cascade_count"]+=1
        nested=exile_next(s,MV[card])
        cast_exiled(s,nested)
    if card in s["stack"]:
        if card=="Boltwave":
            s["boltwave_actual_damage_each"]+=3
            s["life_lost_this_turn"]+=9
            move(s,card,"stack","graveyard")
        else:
            move(s,card,"stack","field")
    s["timeline"].append(("actual_spell_finished",card))


def resolve_call(s,*,drannith=False,rule_of_law=False,counter_first=False,
                 remove_arch_first=False,protected=(),targets=None):
    paid_call(s)
    for i in range(s["cascade_count"]):
        name=exile_next(s)
        if drannith or rule_of_law:
            move(s,name,"exile","library")
            s["timeline"].append(("cannot_cast_exiled_card_but_cascade_resolved",name))
        else:
            cast_exiled(s,name,
                        target=targets[i] if targets else None,
                        protected=protected,
                        counter=counter_first and i==0,
                        remove_arch=remove_arch_first and i==0)
    s["call_creature_sweep"]=sum(mv for n,mv,_ in s["cast_history"] if n!=CALL)
    move(s,CALL,"stack","graveyard")
    conserved(s)
    return s


class AbaddonPassionateArchaeologistP0026(unittest.TestCase):
    def test_arch_x9_three_cascades_target_split(self):
        s=resolve_call(stage(),targets=("A","B","A"))
        self.assertEqual(s["cascade_count"],3)
        self.assertEqual(s["nonhand_casts"],["Arcane Signet","Sol Ring","Boltwave"])
        self.assertEqual(s["arch_total_damage"],Counter({"A":3,"B":1}))
        self.assertEqual(len(s["arch_triggers"]),3)
        self.assertEqual(s["call_creature_sweep"],4)
        self.assertEqual(s["lost_spawn"],3)
        self.assertEqual(Counter(s["tap_sources"]),Counter(LANDS))

    def test_arch_x0_boltwave_no_retro_third(self):
        s=resolve_call(stage(loss=0,top=("Boltwave","Arcane Signet")),
                       targets=("B","C"))
        self.assertEqual(s["cascade_count"],2)
        self.assertEqual(s["nonhand_casts"],["Boltwave","Arcane Signet"])
        self.assertEqual(s["arch_total_damage"],Counter({"B":1,"C":2}))
        self.assertEqual(s["boltwave_actual_damage_each"],3)
        self.assertEqual(s["life_lost_this_turn"],9+3)
        self.assertEqual(s["call_creature_sweep"],3)

    def test_arch_mv0_trigger_deals_zero(self):
        s=resolve_call(stage(loss=0,top=("Lotus Petal","Arcane Signet")))
        self.assertEqual(len(s["arch_triggers"]),2)
        self.assertEqual(s["arch_triggers"][0]["mv"],0)
        self.assertEqual(s["arch_triggers"][0]["target"],"A")
        self.assertEqual(s["arch_total_damage"]["A"],0)
        self.assertEqual(s["lost_spawn"],2)

    def test_arch_original_exile_spell_countered(self):
        s=resolve_call(stage(loss=0,top=("Arcane Signet","Boltwave"),
                             keeper=True),counter_first=True)
        self.assertEqual(s["arch_total_damage"]["A"],2)
        self.assertEqual(s["countered_nonhand"],["Arcane Signet"])
        self.assertIn("Arcane Signet",s["graveyard"])
        self.assertNotIn("Arcane Signet",s["field"])
        self.assertEqual(s["lost_spawn"],2)
        self.assertEqual(s["keeper_damage"],3)

    def test_arch_commander_not_battlefield(self):
        s=resolve_call(stage(loss=9,commander_field=False))
        self.assertEqual(s["cascade_count"],2)
        self.assertEqual(s["nonhand_casts"],["Arcane Signet","Sol Ring"])
        self.assertEqual(s["arch_triggers"],[])
        self.assertEqual(s["arch_total_damage"],Counter())
        self.assertIn(ARCH,s["field"])

    def test_arch_background_removed_after_trigger(self):
        s=resolve_call(stage(loss=0,top=("Arcane Signet","Boltwave")),
                       remove_arch_first=True)
        self.assertEqual(s["arch_total_damage"],Counter({"A":2}))
        self.assertEqual(len(s["arch_triggers"]),1)
        self.assertIn(ARCH,s["graveyard"])
        self.assertEqual(s["lost_spawn"],2)

    def test_arch_drannith_and_rule_of_law(self):
        for stax in ("drannith","rule_of_law"):
            with self.subTest(stax=stax):
                s=resolve_call(stage(),**{stax:True})
                self.assertEqual(s["cascade_count"],3)
                self.assertEqual(s["nonhand_casts"],[])
                self.assertEqual(s["arch_triggers"],[])
                self.assertEqual(s["lost_spawn"],0)
                self.assertEqual(s["keeper_damage"],0)
                self.assertEqual(s["call_creature_sweep"],0)

    def test_arch_nalf_virtual_spell_copies_no_extra(self):
        s=resolve_call(stage(loss=0,nalf=True,top=("Boltwave","Arcane Signet")))
        self.assertEqual(s["cascade_count"],2)
        self.assertEqual(len(s["nalf_virtual_copies"]),2)
        self.assertTrue(all(not row["cast"] for row in s["nalf_virtual_copies"]))
        self.assertEqual(len(s["arch_triggers"]),2)
        self.assertEqual(sum(s["arch_total_damage"].values()),3)
        self.assertEqual(s["boltwave_actual_damage_each"],3)
        self.assertEqual(s["nalf_boltwave_virtual_damage_each"],3)
        self.assertEqual(s["call_creature_sweep"],3)

    def test_arch_wild_nested_separate_real_casts(self):
        s=resolve_call(stage(loss=0,wild=True,top=("Arcane Signet","Sol Ring","Boltwave")))
        self.assertEqual(s["wild_extra_cascade_count"],1)
        self.assertEqual(s["nonhand_casts"],["Arcane Signet","Sol Ring","Boltwave"])
        self.assertEqual(len(s["arch_triggers"]),3)
        self.assertEqual(sum(s["arch_total_damage"].values()),4)
        self.assertEqual(s["call_creature_sweep"],4)

    def test_arch_invalid_target_or_all_protected(self):
        s=resolve_call(stage(loss=0,top=("Arcane Signet","Boltwave")),
                       protected=("A",),targets=("A","A"))
        self.assertEqual([x["target"] for x in s["arch_triggers"]],["B","B"])
        self.assertEqual(s["arch_total_damage"],Counter({"B":3}))
        allblock=resolve_call(stage(loss=0,top=("Arcane Signet","Boltwave")),
                              protected=OPPONENTS)
        self.assertEqual(allblock["arch_triggers"],[])
        self.assertEqual(allblock["arch_total_damage"],Counter())
        self.assertEqual(len(allblock["nonhand_casts"]),2)


if __name__=="__main__":
    unittest.main()
