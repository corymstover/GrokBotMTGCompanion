"""P0-028: seven preregistered exact-100-source copy-sensitive magecraft cases.

Storm-Kiln Artist triggers on an instant/sorcery spell CAST *or COPIED*.
Copy events are virtual; copied permanent spells are not instants/sorceries.
Physical 99 noncommander cards remain in exactly one tracked zone.
"""
from __future__ import annotations
from collections import Counter
import hashlib
import json
from pathlib import Path
import unittest
from scripts.grixis_m7_decision_gate import parse_list

ROOT=Path(__file__).resolve().parents[1]
PLAN=json.loads((ROOT/"data/grixis/m6/phase_b_plans/abaddon_p0_storm_kiln_20261022.json").read_text(encoding="utf-8"))
KILN="Storm-Kiln Artist"
NALF="Nalfeshnee"
LOST="The Lost and the Damned"
PROSPER="Prosper, Tome-Bound"
CALL="Call Forth the Tempest"
BOLTWAVE="Boltwave"
BREACH="Underworld Breach"
LED="Lion's Eye Diamond"
FREEZE="Brain Freeze"
LANDS=("Mountain",)*3+("Island",)*3+("Swamp",)*2
FODDER=("Ancestral Vision","Brainstorm","Cabal Ritual","Dark Ritual","Demonic Tutor","Flame Rift",
        "Gamble","Jeska's Will","Ponder","Rite of Flame","Swan Song","Vampiric Tutor")
MV={"Arcane Signet":2,"Sol Ring":1,BOLTWAVE:1}
INSTANT_SORCERY={CALL,BOLTWAVE,FREEZE}
ZONES=("library","hand","battlefield","graveyard","exile","stack")


def census(s):
    return sum((Counter(s[z]) for z in ZONES),Counter())


def move(s,name,source,target):
    if name not in s[source]:
        raise AssertionError(f"Physical source {name!r} unavailable in {source}")
    s[source].remove(name);s[target].append(name)


def assert_conserved(s):
    if census(s)!=s["source_99"] or s["stack"]:
        raise AssertionError("Original 99 physical cards not conserved/unresolved stack")


def initial(*,nalf=False,lost=False,prosper=False,top=()):
    path=ROOT/PLAN["candidate_path"]
    if hashlib.sha256(path.read_bytes()).hexdigest()!=PLAN["candidate_sha256"]:
        raise AssertionError("Original physical 100 challenger SHA mismatch")
    cards,cmd,companions=parse_list(path)
    if len(cards)!=100 or len(set(cards))!=94 or cmd!=["Abaddon the Despoiler"] or companions:
        raise AssertionError("Candidate must source Abaddon + 99 exact singleton-legal cards")
    s={zone:[] for zone in ZONES}
    s["library"]=list(cards[1:])
    s.update({"source_99":Counter(cards[1:]),"kiln_treasures":0,"prosper_treasures":0,"lost_spawns":0,
        "real_casts":[],"virtual_spell_copies":[],"virtual_permanent_tokens":[],
        "resolved_boltwave_each":0,"prior_opponent_loss":0,
        "source_land_taps":[],"discarded_on_LED":[],"exiled_for_escape":[],
        "storm_copies":0,"timeline":[]})
    move(s,KILN,"library","battlefield")
    if nalf:move(s,NALF,"library","battlefield")
    if lost:move(s,LOST,"library","battlefield")
    if prosper:move(s,PROSPER,"library","battlefield")
    for card in reversed(top):
        if card not in s["library"]:raise AssertionError("Exact top card unavailable "+card)
        s["library"].remove(card);s["library"].insert(0,card)
    assert_conserved(s)
    return s


def on_cast(s,card,zone):
    s["real_casts"].append((card,zone))
    if card in INSTANT_SORCERY and KILN in s["battlefield"]:
        s["kiln_treasures"]+=1
        s["timeline"].append(("magecraft_cast",card))
    if zone=="exile":
        if LOST in s["battlefield"]:s["lost_spawns"]+=1
        if PROSPER in s["battlefield"]:s["prosper_treasures"]+=1
    s["timeline"].append(("actual_spell_cast",card,zone))


def copy_spell(s,card):
    # Copies of spells are separate objects, not physical cards and not cast.
    s["virtual_spell_copies"].append((card,False))
    if card in INSTANT_SORCERY and KILN in s["battlefield"]:
        s["kiln_treasures"]+=1
        s["timeline"].append(("magecraft_spell_copy",card))
    if card==BOLTWAVE:
        s["resolved_boltwave_each"]+=3
    elif card not in INSTANT_SORCERY:
        s["virtual_permanent_tokens"].append((card,"haste","sacrifice at beginning of end step"))
    s["timeline"].append(("copy_resolves",card))


def cast_exile(s,card,*,counter=False):
    if card not in s["exile"]:
        raise AssertionError("Cannot actually cast unexiled card: "+card)
    move(s,card,"exile","stack")
    on_cast(s,card,"exile")
    if counter:
        move(s,card,"stack","graveyard")
        s["timeline"].append(("counter_original_after_cast",card))
    if NALF in s["battlefield"]:
        # Nalf triggers from the actual exile cast; copying spell persists
        # independently of original countering.
        copy_spell(s,card)
    if card in s["stack"]:
        move(s,card,"stack","graveyard" if card==BOLTWAVE else "battlefield")
        if card==BOLTWAVE:s["resolved_boltwave_each"]+=3
    return card


def pay_call(s,*,x=0):
    if x not in (0,9):raise AssertionError("Only preregistered opponent loss")
    move(s,CALL,"library","hand")
    for card in LANDS:move(s,card,"library","battlefield")
    if x==9:
        move(s,"Loyal Subordinate","library","battlefield")
    s["prior_opponent_loss"]=x
    if s["source_land_taps"]:raise AssertionError("Must tap each source once")
    s["source_land_taps"]=list(LANDS)
    move(s,CALL,"hand","stack")
    on_cast(s,CALL,"hand")
    s["cascade_count"]=2+int(x>=8)
    return s


def resolve_call(s,*,counter_first=False):
    for i in range(s["cascade_count"]):
        if not s["library"]:raise AssertionError("No valid arranged cascade hit")
        card=s["library"].pop(0)
        if card not in MV or MV[card]>=8:
            raise AssertionError("Not a prearranged physical strictly-less MV hit: "+card)
        s["exile"].append(card)
        cast_exile(s,card,counter=counter_first and i==0)
    move(s,CALL,"stack","graveyard")
    assert_conserved(s)
    return s


def staged_breach(s):
    # Two real source basics from same 99 pay Breach's {1}{R} from hand,
    # not mana from LED before/within the act of casting it.
    move(s,"Mountain","library","battlefield")
    move(s,"Island","library","battlefield")
    s["source_land_taps"]=["Mountain","Island"]
    move(s,BREACH,"library","hand")
    move(s,BREACH,"hand","stack");on_cast(s,BREACH,"hand")
    move(s,BREACH,"stack","battlefield")
    move(s,LED,"library","graveyard")
    move(s,FREEZE,"library","graveyard")
    for x in FODDER:move(s,x,"library","graveyard")
    # Keep a physical nonempty hand for LED's mandatory discard.
    move(s,"Flusterstorm","library","hand")
    # Escaping LED requires three OTHER physical graveyard cards.
    for x in FODDER[:3]:
        move(s,x,"graveyard","exile");s["exiled_for_escape"].append(x)
    move(s,LED,"graveyard","stack");on_cast(s,LED,"graveyard")
    move(s,LED,"stack","battlefield")
    s["discarded_on_LED"]=list(s["hand"])
    for x in list(s["hand"]):move(s,x,"hand","graveyard")
    move(s,LED,"battlefield","graveyard")
    s["pool_u"]=3
    # Pay Brain Freeze {1}{U} with two U plus three OTHER source graveyard.
    for x in FODDER[3:6]:
        move(s,x,"graveyard","exile");s["exiled_for_escape"].append(x)
    s["pool_u"]-=2
    move(s,FREEZE,"graveyard","stack");on_cast(s,FREEZE,"graveyard")
    prior_casts=len(s["real_casts"])-1
    if prior_casts!=2:raise AssertionError("Breach and LED must be true prior spell casts")
    for _ in range(prior_casts):copy_spell(s,FREEZE)
    s["storm_copies"]=prior_casts
    move(s,FREEZE,"stack","graveyard")
    assert_conserved(s)
    return s


class AbaddonStormKilnP0028(unittest.TestCase):
    def test_kiln_source_paid_hand_boltwave_cast_only(self):
        s=initial(nalf=True,lost=True)
        move(s,"Mountain","library","battlefield")
        move(s,BOLTWAVE,"library","hand")
        s["source_land_taps"]=["Mountain"]
        move(s,BOLTWAVE,"hand","stack");on_cast(s,BOLTWAVE,"hand")
        move(s,BOLTWAVE,"stack","graveyard");s["resolved_boltwave_each"]+=3
        self.assertEqual(s["kiln_treasures"],1)
        self.assertEqual(s["lost_spawns"],0)
        self.assertEqual(s["virtual_spell_copies"],[])
        self.assertEqual(s["resolved_boltwave_each"],3)
        assert_conserved(s)

    def test_kiln_x0_call_nalf_exiled_boltwave(self):
        s=initial(nalf=True,lost=True,top=(BOLTWAVE,"Arcane Signet"))
        pay_call(s,x=0);resolve_call(s)
        self.assertEqual(s["cascade_count"],2)
        self.assertEqual(s["kiln_treasures"],3)
        self.assertEqual(s["resolved_boltwave_each"],6)
        self.assertEqual(s["lost_spawns"],2)
        self.assertEqual(s["real_casts"],[(CALL,"hand"),(BOLTWAVE,"exile"),("Arcane Signet","exile")])
        self.assertEqual(s["virtual_spell_copies"],[(BOLTWAVE,False),("Arcane Signet",False)])

    def test_kiln_x9_mixed_spell_and_permanent_copies(self):
        s=initial(nalf=True,lost=True,top=("Arcane Signet","Sol Ring",BOLTWAVE))
        pay_call(s,x=9);resolve_call(s)
        self.assertEqual(s["cascade_count"],3)
        self.assertEqual(s["kiln_treasures"],3)
        self.assertEqual(s["lost_spawns"],3)
        self.assertEqual(s["resolved_boltwave_each"],6)
        self.assertEqual(len(s["virtual_spell_copies"]),3)
        self.assertEqual([x[0] for x in s["virtual_permanent_tokens"]],["Arcane Signet","Sol Ring"])
        self.assertEqual(len(s["real_casts"]),4)

    def test_kiln_brain_freeze_storm_copies(self):
        s=staged_breach(initial())
        self.assertEqual(s["storm_copies"],2)
        self.assertEqual(s["kiln_treasures"],3)
        self.assertEqual(s["real_casts"],[(BREACH,"hand"),(LED,"graveyard"),(FREEZE,"graveyard")])
        self.assertEqual(s["virtual_spell_copies"],[(FREEZE,False)]*2)
        self.assertEqual(s["exiled_for_escape"],list(FODDER[:6]))
        self.assertEqual(s["pool_u"],1)
        self.assertEqual(s["discarded_on_LED"],["Flusterstorm"])
        self.assertIn(LED,s["graveyard"]);self.assertIn(FREEZE,s["graveyard"])
        assert_conserved(s)

    def test_kiln_countered_original_copy_trigger_still_magecraft(self):
        s=initial(nalf=True,lost=True,top=(BOLTWAVE,"Arcane Signet"))
        pay_call(s,x=0);resolve_call(s,counter_first=True)
        self.assertEqual(s["kiln_treasures"],3)
        self.assertEqual(s["resolved_boltwave_each"],3)
        self.assertIn(BOLTWAVE,s["graveyard"])
        self.assertEqual(s["lost_spawns"],2)
        self.assertEqual(len(s["real_casts"]),3)
        assert_conserved(s)

    def test_kiln_artifact_copy_no_magecraft(self):
        s=initial(nalf=True,lost=True,top=("Arcane Signet","Sol Ring"))
        pay_call(s,x=0);resolve_call(s)
        self.assertEqual(s["kiln_treasures"],1)  # only Call from hand
        self.assertEqual(s["lost_spawns"],2)
        self.assertEqual(len(s["virtual_permanent_tokens"]),2)
        assert_conserved(s)

    def test_kiln_land_play_from_prosper_no_magecraft(self):
        s=initial(prosper=True,lost=True,top=("Swamp",))
        # Preceding end step physically exiles land; next own main permits play.
        land=s["library"].pop(0)
        self.assertEqual(land,"Swamp")
        s["exile"].append(land)
        self.assertEqual(s["kiln_treasures"],0)
        self.assertEqual(s["prosper_treasures"],0)
        move(s,land,"exile","battlefield")
        s["prosper_treasures"]+=1
        s["lost_spawns"]+=1
        self.assertEqual(s["kiln_treasures"],0)
        self.assertEqual(s["real_casts"],[])
        self.assertEqual(s["prosper_treasures"],1)
        self.assertEqual(s["lost_spawns"],1)
        assert_conserved(s)


if __name__=="__main__":
    unittest.main()
