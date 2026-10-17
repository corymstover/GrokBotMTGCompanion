import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))

import grixis_sim as sim
import grixis_commander_counterfactual as cf


def mk(name,cost="{9}",permanent=True):
    c=sim.parse_cost(cost)
    return {"name":name,"mv":c["generic"]+len(c["pips"]),"cost":c,"land":False,"flex_land":False,
            "permanent":permanent,"creature":False,"artifact":False,"gy_text":False,"source":None,"tapped":False,
            "legendary":False,"types":[],"colors":[],"v11":{}}

def land(i):
    d=mk(f"Island {i}",""); d.update({"land":True,"source":(frozenset("U"),1),"types":["land"]}); return d

def deck():
    cmd=mk("Commander","{0}"); cmd["legendary"]=True
    piece=mk("Piece","{0}")
    lib=[land(i) for i in range(40)]+[piece]+[mk(f"Filler {i}") for i in range(58)]
    d=sim.Deck("synthetic",[cmd],lib,{"identity":{"Commander","Piece"}},[{"id":"c1","cards":["Commander","Piece"]}])
    d.ci={"U"}; d.engine={"Piece"}; d.gy_combo={"c1":False}; return d


def test_unavailable_mode_keeps_99_library_but_removes_command_zone_access():
    d=deck(); u=cf.unavailable_deck(d)
    assert d.N==u.N==99
    assert u.commanders==[]
    assert u.combos==d.combos
    assert "Commander" in u.key_sets["identity"]


def test_taxed_mode_adds_exactly_two_generic_without_changing_mv():
    d=deck(); t=cf.taxed_deck(d)
    assert t.commanders[0]["cost"]["generic"]==d.commanders[0]["cost"]["generic"]+2
    assert t.commanders[0]["mv"]==d.commanders[0]["mv"]
    assert d.commanders[0]["cost"]["generic"]==0


def test_paired_modes_remove_commander_combo_access_when_unavailable():
    d=deck(); modes,deltas=cf.evaluate(d,samples=80,seed=6902,turns=8)
    assert modes["normal"]["commander_cast_by_turn6"]==1.0
    assert modes["unavailable"]["commander_cast_by_turn6"]==0.0
    assert modes["unavailable"]["combo_assembled_by_turn6"]==0.0
    assert modes["normal"]["combo_assembled_by_turn6"] >= modes["unavailable"]["combo_assembled_by_turn6"]
    assert modes["taxed"]["commander_turn_mean_when_cast"] >= modes["normal"]["commander_turn_mean_when_cast"]
    assert set(deltas)=={"unavailable","taxed","disrupted"}


def test_disruption_mode_reports_recovery_without_calling_it_real_game_probability():
    d=deck(); perms=cf.permutations(d,40,6903); dd,recs=cf.run_mode(d,"disrupted",40,6903,8,perms)
    m=cf.metric_record(dd,recs,8,"disrupted")
    r=m["disruption_recovery"]
    assert 0<=r["removal_event_share"]<=1
    assert r["recast_after_removal_share"] is None or 0<=r["recast_after_removal_share"]<=1
    assert "bounded" in r["scenario"]


def test_counterfactual_module_never_emits_win_rate_language_or_scalar_value_score():
    txt=(ROOT/"scripts/grixis_commander_counterfactual.py").read_text().lower()
    assert 'win_rate' not in txt
    assert 'commander_value_score' not in txt
    assert 'marginal_value_score' not in txt
