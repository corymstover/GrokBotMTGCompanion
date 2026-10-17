import copy
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))

import grixis_commander_mana as cm
import grixis_sim as sim


def model(name, source=None, ritual=None, oneshot=None):
    v={}
    if ritual: v["ritual"]=ritual
    if oneshot: v["oneshot"]=oneshot
    return {"name":name,"source":source,"cost":{"generic":0,"pips":[],"life":0},"v11":v,"land":False,
            "flex_land":False,"permanent":True,"creature":False,"artifact":True,"gy_text":False,"tapped":False,
            "legendary":False,"types":["artifact"],"colors":[],"mv":0}


def test_disable_fast_mana_preserves_library_but_removes_mana_mode():
    fast=model("Fast",source=(frozenset("C"),2),oneshot=(frozenset("U"),1,"sacrifice",None))
    other=model("Other",source=(frozenset("B"),1))
    cmd=model("Commander")
    d=sim.Deck("x",[cmd],[fast,other]); d.ci=set("UBR")
    z=cm.disable_fast_mana(d,{"Fast"})
    assert len(z.library)==2
    f=next(x for x in z.library if x["name"]=="Fast")
    o=next(x for x in z.library if x["name"]=="Other")
    assert f["source"] is None and f["cost"]["generic"]==99 and "oneshot" not in f["v11"]
    assert o["source"]==(frozenset("B"),1)
    assert d.library[0]["source"]==(frozenset("C"),2)  # deep-copy: original untouched


def test_isolate_commander_keeps_99_and_color_identity():
    a=model("A"); b=model("B"); lib=[model(str(i)) for i in range(99)]
    d=sim.Deck("x",[a,b],lib); d.ci=set("UBR")
    x=cm.isolate_commander(d,"B")
    assert [c["name"] for c in x.commanders]==["B"]
    assert len(x.library)==99 and x.ci==set("UBR")
    assert len(d.commanders)==2


def test_recovery_metrics_condition_on_actual_removal():
    recs=[
        {"removals":[2],"recasts":[4]},
        {"removals":[3],"recasts":[4]},
        {"removals":[3],"recasts":[]},
        {"removals":[],"recasts":[]},
    ]
    r=cm.recovery(recs,0)
    assert r["removal_event_share"]==0.75
    assert r["recast_share_given_removal"]==round(2/3,6)
    assert r["recast_within_turns_given_removal"]["1"]==round(1/3,6)
    assert r["recast_within_turns_given_removal"]["2"]==round(2/3,6)
    assert r["recovery_turns_mean_when_recast"]["value"]==1.5


def test_second_recovery_uses_second_event_only():
    recs=[
        {"removals":[2,5],"recasts":[3,8]},
        {"removals":[2],"recasts":[4]},
        {"removals":[3,7],"recasts":[4]},
    ]
    r=cm.recovery(recs,1)
    assert r["event_count"]==2
    assert r["recast_count"]==1
    assert r["recast_share_given_removal"]==0.5
    assert r["recovery_turns_mean_when_recast"]["value"]==3.0


def test_paired_fast_delta_sign():
    base=[{"commander_turn":2},{"commander_turn":3},{"commander_turn":None}]
    nofast=[{"commander_turn":3},{"commander_turn":5},{"commander_turn":None}]
    d=cm.fast_effect(base,nofast)
    assert d["paired_cast_probability_delta_by_turn"]["2"]["value"]>0
    assert d["mean_turn_acceleration_when_both_cast"]["value"]==1.5


def test_real_abaddon_small_sample_smoke():
    d=sim.load_deck("abaddon-the-despoiler")
    iso=cm.isolate_commander(d,"Abaddon the Despoiler")
    perms=cm.permutations(iso,samples=8,seed=123)
    # Override the module seed only for RNG consumed after the fixed permutations; this is a structural smoke test.
    rec=[]
    for i,p in enumerate(perms):
        import random
        rec.append(sim.play_game(iso,random.Random(sim.seed_for(123,i)),turns=6,perm=p,scenario=None,model="1.1"))
    s=cm.cast_summary(rec)
    assert 0<=s["cast_share_by_turn10"]<=1
    assert len(s["mana_available_by_turn"])==6
