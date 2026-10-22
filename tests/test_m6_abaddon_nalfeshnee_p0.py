"""Abaddon P0-025: nine preregistered physical Nalfeshnee spell-copy tests.

The 99 physical source cards never include virtual copied spells or tokens.
Only bounded stack/cast effects are modeled, not a multiplayer engine.
"""
from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path
import unittest
from scripts.grixis_m7_decision_gate import parse_list

ROOT=Path(__file__).resolve().parents[1]
PLAN=json.loads((ROOT/"data/grixis/m6/phase_b_plans/abaddon_p0_nalfeshnee_20261022.json").read_text())
CALL="Call Forth the Tempest"
NALF="Nalfeshnee"
LOST="The Lost and the Damned"
KEEPER="Keeper of Secrets"
LOYAL="Loyal Subordinate"
WILD="Wild-Magic Sorcerer"
LANDS=("Mountain",)*3+("Island",)*3+("Swamp",)*2
MV={"Arcane Signet":2,"Sol Ring":1,"Boltwave":1,
    "Talisman of Creativity":2,NALF:6,"Lotus Petal":0}
NONPERMANENT={"Boltwave"}
ZONES=("library","hand","field","stack","exile","graveyard")


def census(s):
    return sum((Counter(s[z]) for z in ZONES),Counter())


def move(s,card,src,dst):
    if card not in s[src]:
        raise AssertionError(f"Cannot physically move {card!r} from {src}")
    s[src].remove(card)
    s[dst].append(card)


def stage(*,top=("Arcane Signet","Sol Ring","Boltwave"),loss=9,
          nalf_prior=True,wild_prior=False,keeper_prior=True):
    src=ROOT/PLAN["candidate_path"]
    if hashlib.sha256(src.read_bytes()).hexdigest()!=PLAN["candidate_sha256"]:
        raise AssertionError("Wrong exact 100-card research list")
    cards,commander,comp=parse_list(src)
    if len(cards)!=100 or len(set(cards))!=94 or commander!=["Abaddon the Despoiler"] or comp:
        raise AssertionError("Incorrect physically sourced singleton candidate")
    s={z:[] for z in ZONES}
    s["library"]=list(cards[1:])
    s.update({"original":Counter(cards[1:]),"land_taps":[],"loss":loss,
      "call_cascade_count":None,"cast_history":[],"exile_casts":[],
      "virtual_spell_copies":[],"virtual_permanent_copies":[],
      "sacrificed_copy_names":[],"nalf_copy_triggers":0,
      "copies_resolved":0,"boltwave_originals_resolved":0,
      "boltwave_copies_resolved":0,"boltwave_total_per_opponent":0,
      "lost_spawns":0,"keeper_targeted_damage":0,"nalf_removed":False,
      "wild_cascade_trigger_count":0,"source_countered_names":[],
      "source_call_damage":None,"call_countered":False,"timeline":[]})
    move(s,CALL,"library","hand")
    move(s,LOST,"library","field")
    if keeper_prior: move(s,KEEPER,"library","field")
    if nalf_prior: move(s,NALF,"library","field")
    if wild_prior: move(s,WILD,"library","field")
    if loss==9: move(s,LOYAL,"library","field")
    elif loss!=0: raise AssertionError("Only conditional X0 and X9 states preregistered")
    for x in LANDS: move(s,x,"library","field")
    for x in reversed(top):
        if x not in s["library"]: raise AssertionError("Hit not source-owned: "+x)
        s["library"].remove(x)
        s["library"].insert(0,x)
    if census(s)!=s["original"]: raise AssertionError("Initial source count drift")
    return s


def next_hit(s,threshold):
    """Prearranged possible physical cascade hit, strict less-than MV."""
    if not s["library"]: raise AssertionError("Empty library not preregistered")
    x=s["library"].pop(0)
    if x not in MV or MV[x]>=threshold:
        raise AssertionError("Unmodeled skipped/revealed cascade source: "+x)
    s["exile"].append(x)
    s["timeline"].append(("cascade_exile",x,threshold))
    return x


def copy_trigger(s,name,*,counter_source=False,remove_nalf=False):
    # Creation of this triggered ability occurred when the real spell was cast
    # FROM EXILE. The spell's last-known information is sufficient if original
    # has been countered before the trigger resolves.
    s["nalf_copy_triggers"]+=1
    s["timeline"].append(("nalf_trigger_pending",name))
    if remove_nalf:
        move(s,NALF,"field","graveyard")
        s["nalf_removed"]=True
    if counter_source:
        move(s,name,"stack","graveyard")
        s["source_countered_names"].append(name)
    s["virtual_spell_copies"].append({"name":name,"physical":False,"cast":False})
    s["timeline"].append(("virtual_copy_on_stack",name))
    s["copies_resolved"]+=1
    if name in NONPERMANENT:
        if name=="Boltwave":
            s["boltwave_copies_resolved"]+=1
            s["boltwave_total_per_opponent"]+=3
            s["loss"]+=9  # three opponents take 3 each; no prevention assumed
    else:
        s["virtual_permanent_copies"].append({
            "name":name,"haste":True,"sacrifice_next_end_step":True,
            "from_permanent_spell_copy":True,"token_created_event":False})
    s["timeline"].append(("resolve_virtual_copy",name))


def cast_hit(s,name,*,counter_first=False,remove_nalf_first=False):
    if name not in s["exile"]: raise AssertionError("Not exiled by genuine cascade")
    is_first=len(s["exile_casts"])==0
    nalf_trigger = NALF in s["field"]
    wild_trigger = is_first and WILD in s["field"]
    move(s,name,"exile","stack")
    s["exile_casts"].append(name)
    s["cast_history"].append((name,MV[name],"exile_actual_cast"))
    s["lost_spawns"]+=int(LOST in s["field"])
    if KEEPER in s["field"]:
        s["keeper_targeted_damage"]+=MV[name]
        s["loss"]+=MV[name] # one opponent targeted per Keeper ability
    s["timeline"].append(("actual_exile_cast",name,nalf_trigger,wild_trigger))
    if nalf_trigger:
        copy_trigger(s,name,counter_source=counter_first and is_first,
                     remove_nalf=remove_nalf_first and is_first)
    # Legal controller-chosen ordering: copy trigger resolves, then the
    # first-cast Sorcerer-granted cascade, then the original hit spell.
    if wild_trigger:
        s["wild_cascade_trigger_count"]+=1
        nested=next_hit(s,MV[name])
        cast_hit(s,nested)
    if name in s["stack"]:
        if name=="Boltwave":
            s["boltwave_originals_resolved"]+=1
            s["boltwave_total_per_opponent"]+=3
            s["loss"]+=9
            move(s,name,"stack","graveyard")
        else:
            move(s,name,"stack","field")
        s["timeline"].append(("resolve_original",name))
    else:
        s["timeline"].append(("countered_original_copy_independent",name))


def run(s,*,drannith=False,rule_of_law=False,counter_first=False,
        remove_nalf_first=False,counter_call=False):
    if s["land_taps"] or any(Counter(s["field"])[n]<v for n,v in Counter(LANDS).items()):
        raise AssertionError("Eight untapped source-paid Call lands absent")
    # 3 red and five off-color generic: no source can pay twice.
    s["land_taps"].extend(LANDS)
    threshold=s["loss"] # Abaddon grant is fixed at CALL cast, not later
    move(s,CALL,"hand","stack")
    s["cast_history"].append((CALL,8,"hand"))
    outer=2+int(threshold>=8)
    s["call_cascade_count"]=outer
    s["timeline"].append(("source_call_cast",threshold,outer))
    if counter_call:
        move(s,CALL,"stack","graveyard")
        s["call_countered"]=True
    for i in range(outer):
        hit=next_hit(s,8)
        if drannith or rule_of_law:
            move(s,hit,"exile","library") # a possible 1-card bottom placement
            s["timeline"].append(("prohibited_exile_cast_bottom",hit))
        else:
            cast_hit(s,hit,counter_first=counter_first and i==0,
                     remove_nalf_first=remove_nalf_first and i==0)
    if CALL in s["stack"]:
        s["source_call_damage"]=sum(mv for name,mv,_ in s["cast_history"] if name!=CALL)
        move(s,CALL,"stack","graveyard")
    if census(s)!=s["original"] or s["stack"] or s["exile"]:
        raise AssertionError("Physical 99 source cards drifted or physical spell unresolved")
    return s


def end_step(s):
    """Only permanent-spell copies, not genuine artifact cards, are sacrificed."""
    previous=[x["name"] for x in s["virtual_permanent_copies"]]
    for x in s["virtual_permanent_copies"]:
        if not (x["haste"] and x["sacrifice_next_end_step"]
                and x["from_permanent_spell_copy"] and not x["token_created_event"]):
            raise AssertionError("Copied permanent has wrong Nalf end-step effect")
        s["sacrificed_copy_names"].append(x["name"])
    s["virtual_permanent_copies"].clear()
    if census(s)!=s["original"]:
        raise AssertionError("Virtual spell-copy/token altered physical card census")
    return previous


class AbaddonNalfeshneeP0025(unittest.TestCase):
    def test_nalf_permanent_artifact_copy_eot_sac(self):
        s=run(stage())
        self.assertEqual(len(s["virtual_permanent_copies"]),2)
        self.assertEqual(s["lost_spawns"],3)
        self.assertEqual(s["keeper_targeted_damage"],4)
        self.assertEqual(s["nalf_copy_triggers"],3)
        self.assertTrue(all(not x["token_created_event"] for x in s["virtual_permanent_copies"]))
        self.assertEqual(end_step(s),["Arcane Signet","Sol Ring"])
        self.assertIn("Arcane Signet",s["field"])
        self.assertIn("Sol Ring",s["field"])
        self.assertEqual(s["virtual_permanent_copies"],[])

    def test_nalf_sorcery_boltwave_resolves_twice(self):
        s=run(stage(top=("Boltwave","Sol Ring","Arcane Signet")))
        self.assertEqual(s["boltwave_copies_resolved"],1)
        self.assertEqual(s["boltwave_originals_resolved"],1)
        self.assertEqual(s["boltwave_total_per_opponent"],6)
        self.assertEqual(s["lost_spawns"],3)
        self.assertEqual(s["keeper_targeted_damage"],4)
        self.assertEqual(s["nalf_copy_triggers"],3)
        self.assertIn("Boltwave",s["graveyard"])

    def test_nalf_three_independent_cascade_hits_x9(self):
        s=run(stage())
        self.assertEqual(s["call_cascade_count"],3)
        self.assertEqual(s["exile_casts"],["Arcane Signet","Sol Ring","Boltwave"])
        self.assertEqual(s["copies_resolved"],3)
        self.assertEqual(s["source_call_damage"],4)
        self.assertEqual(s["lost_spawns"],3)
        self.assertEqual(len(s["cast_history"]),4) # Call + 3 actual, not copies

    def test_nalf_no_retroactive_abaddon_from_boltwave(self):
        s=run(stage(loss=0,keeper_prior=False,top=("Boltwave","Arcane Signet")))
        self.assertEqual(s["call_cascade_count"],2)
        self.assertEqual(s["boltwave_total_per_opponent"],6)
        self.assertEqual(s["loss"],18)
        self.assertEqual(s["copies_resolved"],2)
        self.assertEqual(s["lost_spawns"],2)
        self.assertEqual(s["source_call_damage"],3)

    def test_nalf_original_boltwave_countered_copy_survives(self):
        s=run(stage(top=("Boltwave","Sol Ring","Arcane Signet")),counter_first=True)
        self.assertEqual(s["boltwave_copies_resolved"],1)
        self.assertEqual(s["boltwave_originals_resolved"],0)
        self.assertEqual(s["boltwave_total_per_opponent"],3)
        self.assertIn("Boltwave",s["source_countered_names"])
        self.assertIn("Boltwave",s["graveyard"])
        self.assertEqual(s["lost_spawns"],3)
        self.assertEqual(s["source_call_damage"],4) # countered spell WAS cast

    def test_nalf_removed_after_first_cast(self):
        s=run(stage(),remove_nalf_first=True)
        self.assertTrue(s["nalf_removed"])
        self.assertIn(NALF,s["graveyard"])
        self.assertEqual(s["exile_casts"],["Arcane Signet","Sol Ring","Boltwave"])
        self.assertEqual(s["copies_resolved"],1)
        self.assertEqual(len(s["virtual_permanent_copies"]),1)
        self.assertEqual(s["lost_spawns"],3)

    def test_nalf_drannith_rule_of_law(self):
        for policy in ("drannith","rule_of_law"):
            with self.subTest(policy=policy):
                s=run(stage(),**{policy:True})
                self.assertEqual(s["exile_casts"],[])
                self.assertEqual(s["nalf_copy_triggers"],0)
                self.assertEqual(s["lost_spawns"],0)
                self.assertEqual(s["source_call_damage"],0)
                self.assertEqual(s["call_cascade_count"],3)

    def test_nalf_entering_from_first_cascade_no_retro_copy(self):
        s=run(stage(nalf_prior=False,top=(NALF,"Arcane Signet","Sol Ring")))
        self.assertEqual(s["exile_casts"],[NALF,"Arcane Signet","Sol Ring"])
        self.assertEqual(s["nalf_copy_triggers"],2)
        self.assertEqual(s["lost_spawns"],3)
        self.assertIn(NALF,s["field"])
        self.assertEqual(len(s["virtual_permanent_copies"]),2)

    def test_nalf_wild_magic_nested_no_copy_recursion(self):
        s=run(stage(loss=0,wild_prior=True,
                    top=("Arcane Signet","Sol Ring","Boltwave")))
        self.assertEqual(s["call_cascade_count"],2)
        self.assertEqual(s["wild_cascade_trigger_count"],1)
        self.assertEqual(s["exile_casts"],["Arcane Signet","Sol Ring","Boltwave"])
        self.assertEqual(s["copies_resolved"],3)
        self.assertEqual(s["lost_spawns"],3)
        self.assertEqual(len(s["cast_history"]),4)
        self.assertEqual(s["source_call_damage"],4)


if __name__=="__main__":
    unittest.main()
