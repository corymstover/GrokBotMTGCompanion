"""P0-027: ten registered exact-100-card Prosper exile-play tests.

Prosper's Pact Boon triggers for PLAYING an actual CARD from exile,
including a land play, but not for merely exiling, spell-copy resolution,
or casting a card from hand. This is a bounded deterministic trace.
"""
from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path
import unittest
from scripts.grixis_m7_decision_gate import parse_list

ROOT=Path(__file__).resolve().parents[1]
PLAN=json.loads((ROOT/"data/grixis/m6/phase_b_plans/abaddon_p0_prosper_20261022.json").read_text(encoding="utf-8"))
CALL="Call Forth the Tempest"
PROSPER="Prosper, Tome-Bound"
WILD="Wild-Magic Sorcerer"
NALF="Nalfeshnee"
LOST="The Lost and the Damned"
ARCH="Passionate Archaeologist"
LOYAL="Loyal Subordinate"
MV={"Arcane Signet":2,"Sol Ring":1,"Boltwave":1,PROSPER:4}
LANDS=("Mountain",)*3+("Island",)*3+("Swamp",)*2
ZONES=("library","hand","field","stack","exile","graveyard")


def move(s,name,src,dst):
    if name not in s[src]:raise AssertionError("Physical "+name+" missing in "+src)
    s[src].remove(name);s[dst].append(name)


def conserved(s):
    physical=sum((Counter(s[z]) for z in ZONES),Counter())
    if physical!=s["original"] or s["stack"]:
        raise AssertionError("Wrong original 99-card physical multiset/stack")
    return True


def load_deck():
    p=ROOT/PLAN["candidate_path"]
    if hashlib.sha256(p.read_bytes()).hexdigest()!=PLAN["candidate_sha256"]:
        raise AssertionError("Full registered 100-card challenger SHA changed")
    cards,cmd,comp=parse_list(p)
    if len(cards)!=100 or len(set(cards))!=94 or cmd!=["Abaddon the Despoiler"] or comp:
        raise AssertionError("Source is not exact Grixis 100 singleton deck")
    return cards[1:]


def base():
    cards=load_deck()
    s={k:[] for k in ZONES}
    s["library"]=list(cards)
    s.update({"original":Counter(cards),"treasures":0,"spawns":0,"plays_from_exile":[],
              "casts_from_exile":[],"cast_history":[],"boltwave_damage_each":0,
              "virtual_copy_resolves":0,"wild_nested":0,"cascade_count":0,
              "actual_exile_spells_countered":[],"tap_sources":[],"arch_damage":0,
              "commander_zone":"field","current_turn":10,"impulse_permissions":{},
              "land_drop_available":True,"land_plays":0,"events":[]})
    move(s,LOST,"library","field")
    return s


def bring_top(s,names):
    for name in reversed(names):
        if name not in s["library"]:raise AssertionError("Expected exact source card unavailable: "+name)
        s["library"].remove(name)
        s["library"].insert(0,name)


def call_fixture(*,loss=9,prosper_prior=True,nalf=False,wild=False,
                 top=("Arcane Signet","Sol Ring","Boltwave")):
    s=base()
    s["loss"]=loss
    move(s,CALL,"library","hand")
    if prosper_prior:move(s,PROSPER,"library","field")
    if nalf:move(s,NALF,"library","field")
    if wild:move(s,WILD,"library","field")
    if loss==9:move(s,LOYAL,"library","field")
    elif loss!=0:raise AssertionError("Only X9 or X0 precommitted")
    for land in LANDS:move(s,land,"library","field")
    bring_top(s,top)
    conserved(s)
    return s


def cascade_hit(s,threshold):
    if not s["library"]:raise AssertionError("Empty source library")
    card=s["library"].pop(0)
    if card not in MV or MV[card]>=threshold:
        raise AssertionError("Physical source was not registered lower-MV cascade hit "+card)
    s["exile"].append(card)
    return card


def treasure_trigger(s,card,how):
    if PROSPER in s["field"]:
        s["treasures"]+=1
        s["plays_from_exile"].append((card,how))
        s["events"].append(("pact_boon_triggers_actual_exile_play",card,how))
    else:s["events"].append(("prosper_absent_no_pact_trigger",card))


def cast_hit(s,card,*,remove_prosper=False):
    if card not in s["exile"]:raise AssertionError("Not an actually exiled card")
    first=len(s["casts_from_exile"])==0
    nalf=NALF in s["field"]
    wild=first and WILD in s["field"]
    # Casting a spell is PLAYING a card; triggers happen before the original
    # spell resolves. Prosper cannot trigger on its own original cast if
    # not yet on battlefield.
    move(s,card,"exile","stack")
    s["casts_from_exile"].append(card)
    s["cast_history"].append((card,MV[card],"exile"))
    s["spawns"]+=int(LOST in s["field"])
    treasure_trigger(s,card,"cast_spell")
    if nalf:
        s["virtual_copy_resolves"]+=1
        if card=="Boltwave":s["boltwave_damage_each"]+=3
    if remove_prosper and first and PROSPER in s["field"]:
        move(s,PROSPER,"field","graveyard")
        s["events"].append(("removed_after_pact_trigger",))
    if wild:
        s["wild_nested"]+=1
        nested=cascade_hit(s,MV[card])
        cast_hit(s,nested)
    if card=="Boltwave":
        s["boltwave_damage_each"]+=3
        move(s,card,"stack","graveyard")
    else:
        move(s,card,"stack","field")


def resolve_call(s,*,drannith=False,rule_of_law=False,remove_prosper_first=False):
    if s["tap_sources"] or any(Counter(s["field"])[x]<n for x,n in Counter(LANDS).items()):
        raise AssertionError("Must source-pay 5RRR from eight untapped real basics")
    s["tap_sources"].extend(LANDS)
    before=s["loss"]
    move(s,CALL,"hand","stack")
    s["cast_history"].append((CALL,8,"hand"))
    count=2+int(s["commander_zone"]=="field" and before>=8)
    s["cascade_count"]=count
    for i in range(count):
        card=cascade_hit(s,8)
        if drannith or rule_of_law:
            move(s,card,"exile","library") # one physically possible bottom order
        else:
            cast_hit(s,card,remove_prosper=remove_prosper_first and i==0)
    move(s,CALL,"stack","graveyard")
    conserved(s)
    return s


def impulse_fixture(card="Swamp",*,arch=False):
    s=base()
    move(s,PROSPER,"library","field")
    # One actual untapped source Mountain is available on next main phase.
    move(s,"Mountain","library","field")
    if arch:move(s,ARCH,"library","field")
    bring_top(s,(card,))
    return s


def beginning_end_step_exile(s):
    # The ability TRIGGERS at the BEGINNING of the end step. Merely exiling
    # does not constitute playing a card, hence neither Pact nor Lost.
    if PROSPER not in s["field"] or not s["library"]:
        raise AssertionError("No live Prosper or top physical card")
    card=s["library"].pop(0)
    s["exile"].append(card)
    s["impulse_permissions"][card]=s["current_turn"]+1
    s["events"].append(("mystic_arcanum_begin_end_step_exile",card,s["current_turn"]+1))
    conserved(s)
    return card


def permission(s,card,*,turn,active_player="self"):
    if card not in s["exile"] or card not in s["impulse_permissions"]:
        raise ValueError("No physically exiled card with Mystic permission")
    if active_player!="self" or turn>s["impulse_permissions"][card]:
        raise ValueError("Mystic permission is not active on current self turn")


def play_impulse_land(s,card,*,turn,phase="main",stack_empty=True,
                      land_drop_available=True,active_player="self"):
    permission(s,card,turn=turn,active_player=active_player)
    if phase!="main" or not stack_empty or not land_drop_available or not s["land_drop_available"]:
        raise ValueError("Cannot play land outside own empty-stack main phase or used land drop")
    move(s,card,"exile","field")
    s["land_drop_available"]=False
    s["land_plays"]+=1
    treasure_trigger(s,card,"play_land_from_exile")
    s["spawns"]+=int(LOST in s["field"]) # Land ENTERS from exile, not from hand.
    s["events"].append(("land_ETB_from_exile_not_spell_cast",card))
    conserved(s)


def cast_impulse_sorcery(s,card,*,turn,phase="main",active_player="self"):
    permission(s,card,turn=turn,active_player=active_player)
    if phase!="main" or not s["field"].count("Mountain") or "Mountain" in s["tap_sources"]:
        raise ValueError("Sorcery timing or actual untapped red source unavailable")
    s["tap_sources"].append("Mountain")
    move(s,card,"exile","stack")
    s["cast_history"].append((card,MV[card],"exile"))
    s["casts_from_exile"].append(card)
    treasure_trigger(s,card,"cast_spell")
    s["spawns"]+=int(LOST in s["field"])
    if ARCH in s["field"] and s["commander_zone"]=="field":
        s["arch_damage"]+=MV[card]
    if card=="Boltwave":
        s["boltwave_damage_each"]+=3
    move(s,card,"stack","graveyard")
    conserved(s)


class AbaddonProsperP0027(unittest.TestCase):
    def test_prosper_x9_three_cascade_casts(self):
        s=resolve_call(call_fixture())
        self.assertEqual(s["cascade_count"],3)
        self.assertEqual(s["casts_from_exile"],["Arcane Signet","Sol Ring","Boltwave"])
        self.assertEqual(s["treasures"],3)
        self.assertEqual(s["spawns"],3)
        self.assertEqual(len(s["cast_history"]),4) # Call from hand + 3 actual
        self.assertEqual(Counter(s["tap_sources"]),Counter(LANDS))

    def test_prosper_boltwave_nalf_virtual_copy(self):
        s=resolve_call(call_fixture(loss=0,nalf=True,top=("Boltwave","Arcane Signet")))
        self.assertEqual(s["cascade_count"],2)
        self.assertEqual(s["virtual_copy_resolves"],2)
        self.assertEqual(s["boltwave_damage_each"],6)
        self.assertEqual(s["treasures"],2)
        self.assertEqual(s["spawns"],2)
        self.assertEqual(len(s["casts_from_exile"]),2)

    def test_prosper_wild_nested_independent_casts(self):
        s=resolve_call(call_fixture(loss=0,wild=True))
        self.assertEqual(s["cascade_count"],2)
        self.assertEqual(s["wild_nested"],1)
        self.assertEqual(s["casts_from_exile"],["Arcane Signet","Sol Ring","Boltwave"])
        self.assertEqual(s["treasures"],3)
        self.assertEqual(s["spawns"],3)

    def test_prosper_entering_from_first_cascade(self):
        s=resolve_call(call_fixture(loss=0,prosper_prior=False,top=(PROSPER,"Sol Ring")))
        self.assertEqual(s["casts_from_exile"],[PROSPER,"Sol Ring"])
        self.assertEqual(s["treasures"],1)
        self.assertEqual(s["spawns"],2)
        self.assertIn(PROSPER,s["field"])

    def test_prosper_removed_after_first_cast(self):
        s=resolve_call(call_fixture(loss=0,top=("Arcane Signet","Boltwave")),
                       remove_prosper_first=True)
        self.assertEqual(s["treasures"],1)
        self.assertEqual(s["casts_from_exile"],["Arcane Signet","Boltwave"])
        self.assertIn(PROSPER,s["graveyard"])

    def test_prosper_drannith_or_rule_of_law(self):
        for stax in ("drannith","rule_of_law"):
            with self.subTest(stax=stax):
                s=resolve_call(call_fixture(),**{stax:True})
                self.assertEqual(s["cascade_count"],3)
                self.assertEqual(s["casts_from_exile"],[])
                self.assertEqual(s["treasures"],0)
                self.assertEqual(s["spawns"],0)

    def test_prosper_end_step_exile_land_then_next_main_play(self):
        s=impulse_fixture("Swamp")
        self.assertEqual(beginning_end_step_exile(s),"Swamp")
        self.assertEqual(s["treasures"],0)
        with self.assertRaisesRegex(ValueError,"Cannot play land"):
            play_impulse_land(s,"Swamp",turn=10,phase="end")
        play_impulse_land(s,"Swamp",turn=11)
        self.assertEqual(s["treasures"],1)
        self.assertEqual(s["spawns"],1)
        self.assertEqual(s["casts_from_exile"],[])
        self.assertEqual(s["land_plays"],1)
        self.assertIn("Swamp",s["field"])
        conserved(s)

    def test_prosper_end_step_exile_sorcery_paid_next_main(self):
        s=impulse_fixture("Boltwave",arch=True)
        self.assertEqual(beginning_end_step_exile(s),"Boltwave")
        with self.assertRaisesRegex(ValueError,"Sorcery timing"):
            cast_impulse_sorcery(s,"Boltwave",turn=10,phase="end")
        cast_impulse_sorcery(s,"Boltwave",turn=11)
        self.assertEqual(s["treasures"],1)
        self.assertEqual(s["spawns"],1)
        self.assertEqual(s["arch_damage"],1)
        self.assertEqual(s["boltwave_damage_each"],3)
        self.assertEqual(s["casts_from_exile"],["Boltwave"])
        self.assertIn("Mountain",s["tap_sources"])

    def test_prosper_expired_permission_unplayed(self):
        s=impulse_fixture("Swamp")
        beginning_end_step_exile(s)
        with self.assertRaisesRegex(ValueError,"Mystic permission"):
            play_impulse_land(s,"Swamp",turn=12)
        self.assertEqual(s["treasures"],0)
        self.assertEqual(s["spawns"],0)
        self.assertIn("Swamp",s["exile"])
        conserved(s)

    def test_prosper_land_timing_and_land_drop_restrictions(self):
        for policy in ("opponent_turn","end_step","nonempty_stack","land_drop_used"):
            with self.subTest(policy=policy):
                s=impulse_fixture("Swamp")
                beginning_end_step_exile(s)
                args={"turn":11}
                if policy=="opponent_turn":args["active_player"]="opponent"
                if policy=="end_step":args["phase"]="end"
                if policy=="nonempty_stack":args["stack_empty"]=False
                if policy=="land_drop_used":args["land_drop_available"]=False
                with self.assertRaises(ValueError):
                    play_impulse_land(s,"Swamp",**args)
                self.assertEqual(s["treasures"],0)
                self.assertIn("Swamp",s["exile"])
                conserved(s)


if __name__=="__main__":
    unittest.main()
