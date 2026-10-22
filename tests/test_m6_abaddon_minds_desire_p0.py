"""Abaddon P0-029: exact-100 source-paid Mind's Desire storm/impulse cases.

Every resolving Mind's Desire copy shuffles, then exiles one real card.
Fixture chooses ONE POSSIBLE resulting shuffle order before each exile.
Unplayed cards stay exiled after end of turn; nothing is automatically cast.
Virtual storm/Nalf spell copies do not enter the 99 physical card census.
"""
from __future__ import annotations
from collections import Counter
import hashlib
import json
from pathlib import Path
import unittest
from scripts.grixis_m7_decision_gate import parse_list

ROOT=Path(__file__).resolve().parents[1]
PLAN=json.loads((ROOT/"data/grixis/m6/phase_b_plans/abaddon_p0_minds_desire_20261022.json").read_text(encoding="utf-8"))
MIND="Mind's Desire"
NALF="Nalfeshnee"
KILN="Storm-Kiln Artist"
PROSPER="Prosper, Tome-Bound"
LOST="The Lost and the Damned"
KEEPER="Keeper of Secrets"
ARCH="Passionate Archaeologist"
CALL="Call Forth the Tempest"
RITE="Rite of Flame"
DARK="Dark Ritual"
BOLT="Boltwave"
VISION="Ancestral Vision"
ZONES=("library","hand","battlefield","stack","exile","graveyard")
HAND_LANDS=("Mountain",)*3+("Swamp",)*2+("Island",)*2+("Command Tower",)
CALL_LANDS=("Mountain",)*3+("Island",)*3+("Swamp",)*2
PERMANENTS={"Sol Ring","Arcane Signet"}
INSTANT_SORCERY={MIND,RITE,DARK,BOLT,VISION,CALL}
MANA_VALUES={MIND:6,BOLT:1,"Arcane Signet":2,"Sol Ring":1,VISION:0}


def physically(s):
    return sum((Counter(s[x]) for x in ZONES),Counter())


def move(s,card,a,b):
    if card not in s[a]:raise AssertionError("Physical "+card+" missing from "+a)
    s[a].remove(card)
    s[b].append(card)


def conserved(s):
    if physically(s)!=s["initial"]:
        raise AssertionError("Exactly 99 physical source-card multiset changed")


def stage(*,nalf=False,kiln=True,prosper=False,lost=False,keeper=False,arch=False,
          call=False):
    path=ROOT/PLAN["physical_challenger_path"]
    if hashlib.sha256(path.read_bytes()).hexdigest()!=PLAN["physical_challenger_raw_sha256"]:
        raise AssertionError("Preregistered exact physical 100 source SHA drift")
    cards,commanders,comp=parse_list(path)
    if len(cards)!=100 or len(set(cards))!=94 or commanders!=["Abaddon the Despoiler"] or comp:
        raise AssertionError("Invalid real Abaddon 100 card pool")
    s={k:[] for k in ZONES}
    s["library"]=list(cards[1:])
    s.update({"initial":Counter(cards[1:]),"active_turn":10,"plays":[],
      "stack_history":[],"cast_history":[],"virtual_spell_copies":[],
      "impulses":[],"free_casts":[],"storm_count":0,"magecraft_treasure":0,
      "prosper_treasure":0,"lost_spawns":0,"keeper_damage":0,"arch_damage":0,
      "nalf_spell_copies":[],"virtual_permanent_tokens":[],"boltwave_damage_each":0,
      "drawn_by_vision":[],"land_drop_available":True,"land_plays":0,
      "tapped_lands":[],"mana_proof":[],"abaddon_field":True,"abaddon_cascade":0,
      "call_printed_cascades":0,"mind_storm_copies":0,"mind_nalf_copies":0,
      "physical_impulse_resolutions":0,"copies_made":0})
    for card,enabled in ((NALF,nalf),(KILN,kiln),(PROSPER,prosper),
                        (LOST,lost),(KEEPER,keeper),(ARCH,arch)):
        if enabled:move(s,card,"library","battlefield")
    for card in CALL_LANDS if call else HAND_LANDS:
        move(s,card,"library","battlefield")
    conserved(s)
    return s


def pay_lands(s,land_names,spell):
    for card in land_names:
        if Counter(s["battlefield"])[card]<=Counter(s["tapped_lands"])[card]:
            raise AssertionError("Physical untapped source missing: "+card)
        s["tapped_lands"].append(card)
    s["mana_proof"].append((spell,tuple(land_names)))


def on_actual_cast(s,card,zone):
    s["cast_history"].append((card,zone))
    if card in INSTANT_SORCERY and KILN in s["battlefield"]:
        s["magecraft_treasure"]+=1
    if zone=="exile":
        if PROSPER in s["battlefield"]:s["prosper_treasure"]+=1
        if LOST in s["battlefield"]:s["lost_spawns"]+=1
        mv=MANA_VALUES.get(card)
        if mv is not None:
            if KEEPER in s["battlefield"]:s["keeper_damage"]+=mv
            if ARCH in s["battlefield"] and s["abaddon_field"]:s["arch_damage"]+=mv


def make_copy(s,card,kind):
    s["virtual_spell_copies"].append((card,kind,"NOT_CAST"))
    s["copies_made"]+=1
    if card in INSTANT_SORCERY and KILN in s["battlefield"]:
        s["magecraft_treasure"]+=1
    if kind=="nalf":s["nalf_spell_copies"].append(card)
    if card in PERMANENTS:
        s["virtual_permanent_tokens"].append((card,"haste","sacrifice_at_end_step"))
    if card==BOLT:s["boltwave_damage_each"]+=3


def cast_prior(s,card):
    if card not in (RITE,DARK,BOLT):raise AssertionError("Unregistered prior spell")
    pay_lands(s,("Swamp",) if card==DARK else ("Mountain",),card)
    move(s,card,"library","hand")
    move(s,card,"hand","stack")
    on_actual_cast(s,card,"hand")
    move(s,card,"stack","graveyard")
    if card==BOLT:s["boltwave_damage_each"]+=3


def cast_mind_from_hand(s):
    # Physically pay 4UU with the six remaining original untapped lands.
    available=[]
    selected=["Island","Island"]
    selected += ["Mountain"]*max(0,Counter(s["battlefield"])["Mountain"]-Counter(s["tapped_lands"])["Mountain"])
    selected += ["Swamp"]*max(0,Counter(s["battlefield"])["Swamp"]-Counter(s["tapped_lands"])["Swamp"])
    selected += ["Command Tower"]
    selected=selected[:6]
    if len(selected)!=6 or Counter(selected)["Island"]!=2:
        raise AssertionError("4UU cannot be sourced from six distinct untapped originals")
    pay_lands(s,selected,MIND)
    move(s,MIND,"library","hand")
    move(s,MIND,"hand","stack")
    earlier=len(s["cast_history"])
    on_actual_cast(s,MIND,"hand")
    return earlier


def resolve_impulse(s,which,card):
    """Choose one actually available card as the top of a possible shuffle."""
    if card not in s["library"]:raise AssertionError("Requested impulse source not in real library: "+card)
    # Each resolving virtual/original Desire instructs a physical shuffle;
    # this conditional arrangement has nonzero probability but is not sampled.
    s["library"].remove(card)
    s["library"].insert(0,card)
    hit=s["library"].pop(0)
    s["exile"].append(hit)
    s["impulses"].append({"card":hit,"source":which,"expires":s["active_turn"]})
    s["physical_impulse_resolutions"]+=1
    s["stack_history"].append(("mind_resolved_one_exile",which,hit))
    conserved(s)


def resolve_mind(s,staged_hits,*,storm_count,counter_original=False,zone="hand"):
    """Trigger storm and/or Nalf separately and resolve copies then original."""
    if MIND not in s["stack"]:raise AssertionError("No actual Mind spell on stack")
    if len(staged_hits) != storm_count + int(zone=="exile" and NALF in s["battlefield"]) + int(not counter_original):
        raise AssertionError("Number of staged physical impulse resolutions cannot be invented")
    for _ in range(storm_count):
        make_copy(s,MIND,"storm")
        s["mind_storm_copies"]+=1
    if zone=="exile" and NALF in s["battlefield"]:
        make_copy(s,MIND,"nalf")
        s["mind_nalf_copies"]+=1
    if counter_original:
        move(s,MIND,"stack","graveyard")
        s["stack_history"].append(("original_mind_countered",))
    # Nalf copy and storm copies resolve independently before original.
    for i,card in enumerate(staged_hits):
        resolve_impulse(s,"copy" if i<storm_count+s["mind_nalf_copies"] else "original",card)
    if MIND in s["stack"]:move(s,MIND,"stack","graveyard")
    conserved(s)


def cascade_actual(s,card):
    if card not in s["library"]:raise AssertionError("Source cascade hit absent")
    s["library"].remove(card)
    s["exile"].append(card)
    move(s,card,"exile","stack")
    on_actual_cast(s,card,"exile")
    if NALF in s["battlefield"]:
        make_copy(s,card,"nalf")
    move(s,card,"stack","battlefield" if card in PERMANENTS else "graveyard")
    s["free_casts"].append(card)
    conserved(s)


def play_impulse(s,card,*,turn=10,phase="main",empty_stack=True,
                 land_drop_available=True):
    permission=next((p for p in s["impulses"] if p["card"]==card),None)
    if permission is None or card not in s["exile"] or turn!=permission["expires"]:
        raise ValueError("Mind's Desire permission expired or card unavailable")
    if phase!="main" or not empty_stack or s["stack"]:
        raise ValueError("Normal sorcery/land timing, own main phase and empty stack required")
    if card in ("Swamp","Mountain","Island","Command Tower"):
        if not (land_drop_available and s["land_drop_available"]):
            raise ValueError("Normal land drop restriction")
        move(s,card,"exile","battlefield")
        s["land_drop_available"]=False
        s["land_plays"]+=1
        if PROSPER in s["battlefield"]:s["prosper_treasure"]+=1
        if LOST in s["battlefield"]:s["lost_spawns"]+=1 # actual land from exile
        s["plays"].append((card,"land_not_spell"))
    else:
        move(s,card,"exile","stack")
        on_actual_cast(s,card,"exile")
        if NALF in s["battlefield"]:make_copy(s,card,"nalf")
        if card==BOLT:
            s["boltwave_damage_each"]+=3
        if card==VISION:
            # Resolving original ancestral draw 3 from real library, not fake cards
            for _ in range(3):
                if not s["library"]:raise AssertionError("Ancestral draw from empty source")
                drawn=s["library"].pop(0)
                s["hand"].append(drawn)
                s["drawn_by_vision"].append(drawn)
        move(s,card,"stack","battlefield" if card in PERMANENTS else "graveyard")
        s["plays"].append((card,"free_spell_cast_from_exile"))
    conserved(s)


class AbaddonMindsDesireP0029(unittest.TestCase):
    def test_desire_hand_two_paid_spells_storm2_magecraft(self):
        s=stage()
        cast_prior(s,RITE)
        cast_prior(s,DARK)
        count=cast_mind_from_hand(s)
        self.assertEqual(count,2)
        resolve_mind(s,(BOLT,"Arcane Signet","Swamp"),storm_count=count)
        self.assertEqual(s["mind_storm_copies"],2)
        self.assertEqual(s["physical_impulse_resolutions"],3)
        self.assertEqual(s["magecraft_treasure"],5) # Rite/Dark/Mind casts; 2 Mind copies
        self.assertEqual(s["free_casts"],[])
        self.assertEqual(s["plays"],[])
        self.assertEqual(len(s["impulses"]),3)
        self.assertTrue(all(qty<=Counter(s["battlefield"])[name] for name,qty in Counter(s["tapped_lands"]).items()))
        self.assertEqual(len(s["tapped_lands"]),8)
        conserved(s)

    def test_desire_deferred_spells_land_prosper_and_lost(self):
        s=stage(nalf=True,kiln=True,prosper=True,lost=True,keeper=True,arch=True)
        cast_prior(s,RITE);cast_prior(s,DARK)
        count=cast_mind_from_hand(s)
        resolve_mind(s,(BOLT,"Arcane Signet","Swamp"),storm_count=count)
        self.assertEqual(s["prosper_treasure"],0)
        self.assertEqual(s["lost_spawns"],0)
        play_impulse(s,BOLT);play_impulse(s,"Arcane Signet");play_impulse(s,"Swamp")
        self.assertEqual(s["prosper_treasure"],3)
        self.assertEqual(s["lost_spawns"],3)
        self.assertEqual(s["keeper_damage"],3)
        self.assertEqual(s["arch_damage"],3)
        self.assertEqual(s["nalf_spell_copies"],[BOLT,"Arcane Signet"])
        self.assertEqual(s["boltwave_damage_each"],6)
        self.assertEqual(s["land_plays"],1)
        self.assertEqual(len(s["plays"]),3)
        self.assertEqual(len([z for z in s["cast_history"] if z[1]=="exile"]),2)
        conserved(s)

    def test_desire_no_automatic_play_and_permission_expiry(self):
        s=stage(prosper=True,lost=True)
        cast_mind_from_hand(s)
        resolve_mind(s,("Swamp",),storm_count=0)
        self.assertEqual(s["prosper_treasure"],0)
        self.assertEqual(s["lost_spawns"],0)
        with self.assertRaises(ValueError):play_impulse(s,"Swamp",empty_stack=False)
        with self.assertRaises(ValueError):play_impulse(s,"Swamp",land_drop_available=False)
        with self.assertRaises(ValueError):play_impulse(s,"Swamp",turn=11)
        self.assertIn("Swamp",s["exile"])
        self.assertEqual(s["land_plays"],0)
        conserved(s)

    def test_desire_counter_original_storm_copies_survive(self):
        s=stage()
        cast_prior(s,RITE);cast_prior(s,DARK)
        count=cast_mind_from_hand(s)
        resolve_mind(s,(BOLT,"Swamp"),storm_count=count,counter_original=True)
        self.assertIn(MIND,s["graveyard"])
        self.assertEqual(s["physical_impulse_resolutions"],2)
        self.assertEqual(s["mind_storm_copies"],2)
        self.assertEqual(s["magecraft_treasure"],5)
        self.assertEqual(len(s["impulses"]),2)
        conserved(s)

    def test_desire_x9_hand_abaddon_granted_independent(self):
        s=stage(lost=True,prosper=True)
        cast_prior(s,BOLT);cast_prior(s,RITE)
        self.assertEqual(s["boltwave_damage_each"],3)
        count=cast_mind_from_hand(s)
        self.assertEqual(count,2)
        if s["abaddon_field"] and s["boltwave_damage_each"]*3>=6:
            s["abaddon_cascade"]+=1
            cascade_actual(s,"Sol Ring")
        resolve_mind(s,("Arcane Signet","Swamp","Ancestral Vision"),storm_count=count)
        self.assertEqual(s["abaddon_cascade"],1)
        self.assertEqual(s["free_casts"],["Sol Ring"])
        self.assertEqual(len(s["cast_history"]),4) # two prior + Mind + cascade Sol Ring
        self.assertEqual(s["mind_storm_copies"],2)
        self.assertEqual(s["physical_impulse_resolutions"],3)
        self.assertEqual(s["prosper_treasure"],1)
        self.assertEqual(s["lost_spawns"],1)
        conserved(s)

    def test_desire_cast_from_call_exile_nalf_plus_storm(self):
        s=stage(nalf=True,prosper=True,lost=True,call=True)
        pay_lands(s,CALL_LANDS,CALL)
        move(s,CALL,"library","hand")
        move(s,CALL,"hand","stack")
        on_actual_cast(s,CALL,"hand")
        s["call_printed_cascades"]=2
        # First printed Call cascade legally hits MV6 Mind from library.
        move(s,MIND,"library","exile")
        move(s,MIND,"exile","stack")
        prior=len(s["cast_history"]) # paid Call is earlier actual spell
        on_actual_cast(s,MIND,"exile")
        self.assertEqual(prior,1)
        resolve_mind(s,(BOLT,"Arcane Signet","Swamp"),storm_count=prior,zone="exile")
        cascade_actual(s,"Sol Ring") # second printed Call cascade, not Abaddon
        move(s,CALL,"stack","graveyard")
        self.assertEqual(s["mind_storm_copies"],1)
        self.assertEqual(s["mind_nalf_copies"],1)
        self.assertEqual(s["physical_impulse_resolutions"],3)
        self.assertEqual(s["prosper_treasure"],2) # Mind and Sol Ring; copies not cast
        self.assertEqual(s["lost_spawns"],2)
        self.assertEqual(s["abaddon_cascade"],0)
        self.assertEqual(len([x for x in s["cast_history"] if x[1]=="exile"]),2)
        conserved(s)

    def test_desire_zero_cost_ancestral_vision_free_cast(self):
        s=stage(prosper=True,lost=True,keeper=True,arch=True)
        count=cast_mind_from_hand(s)
        self.assertEqual(count,0)
        resolve_mind(s,(VISION,),storm_count=0)
        play_impulse(s,VISION)
        self.assertEqual(s["prosper_treasure"],1)
        self.assertEqual(s["lost_spawns"],1)
        self.assertEqual(s["keeper_damage"],0)
        self.assertEqual(s["arch_damage"],0)
        self.assertEqual(len(s["drawn_by_vision"]),3)
        self.assertIn(VISION,s["graveyard"])
        conserved(s)


if __name__=="__main__":
    unittest.main()
