#!/usr/bin/env python3
"""Step C batch 68.3: commander casting, fast-mana contribution, and commander-tax recovery evidence.

Uses the existing frozen grixis_sim v1.1 goldfish engine without changing it. Each commander is evaluated in isolation
from co-commanders to avoid command-zone cast-order confounding; deck color identity and the 99 stay unchanged. The same
library permutations are used for baseline, no-fast-mana counterfactual, and deterministic removal/tax stress runs.

This is bounded test evidence, not a multiplayer win model and not a mana-base swap decision.
"""
from __future__ import annotations

import argparse
import copy
import json
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import grixis_sim as sim

REGISTRY = ROOT / "data" / "grixis" / "registry.json"
MANA = ROOT / "data" / "grixis" / "mana_base"
OUT = ROOT / "data" / "grixis" / "commander_mana"
SCHEMA = ROOT / "data" / "grixis" / "schemas" / "commander_mana.schema.json"
VERSION = 1
SAMPLES = 500
SEED = 6813
TURNS = 10


def load(p): return json.loads(Path(p).read_text(encoding="utf-8"))

def dump(p, obj):
    p=Path(p); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(obj,indent=1,sort_keys=True,ensure_ascii=False)+"\n",encoding="utf-8")


def isolate_commander(deck, name):
    d=copy.deepcopy(deck)
    d.commanders=[c for c in d.commanders if c["name"]==name]
    if len(d.commanders)!=1: raise ValueError(f"{deck.slug}: commander {name!r} not uniquely found")
    return d


def disable_fast_mana(deck, names):
    """Counterfactual: keep fast-mana cards in the 99/draws but make their mana mode unavailable and uncastable.

    Setting an impossible cost avoids the engine spending mana to cast an otherwise stripped rock/ritual. This is a
    diagnostic counterfactual, not a proposed card cut and not a claim that those cards have no non-mana utility.
    """
    d=copy.deepcopy(deck)
    for c in d.library:
        if c["name"] not in names: continue
        c["source"]=None
        c["cost"]={"generic":99,"pips":[],"life":0}
        f=dict(c.get("v11") or {})
        for k in ("ritual","oneshot","condition"):
            f.pop(k,None)
        c["v11"]=f
    return d


def permutations(deck, samples=SAMPLES, seed=SEED):
    return [random.Random(sim.seed_for(seed,i)).sample(range(deck.N),deck.N) for i in range(samples)]


def run_scenario(deck, perms, kind=None):
    out=[]
    scenario={"kind":kind,"T":1} if kind else None
    for i,perm in enumerate(perms):
        rng=random.Random(sim.seed_for(SEED,i))
        out.append(sim.play_game(deck,rng,turns=TURNS,multiplayer=True,skip_first_draw=False,mulligan=True,
                                 perm=perm,scenario=scenario,model="1.1"))
    return out


def share(xs): return sum(bool(x) for x in xs)/len(xs) if xs else 0.0


def paired_indicator_delta(a,b,pred):
    vals=[(1 if pred(x) else 0)-(1 if pred(y) else 0) for x,y in zip(a,b)]
    m,ci=sim.mean_ci(vals)
    return {"value":round(m,6),"ci95":[round(ci[0],6),round(ci[1],6)]}


def cast_summary(recs):
    ct=[r["commander_turn"] for r in recs]
    got=[x for x in ct if x is not None]
    return {
        "cast_by_turn": {str(t):round(sum(1 for x in ct if x is not None and x<=t)/len(ct),6) for t in (2,3,4,5,6,8,10)},
        "mean_turn_when_cast": round(sum(got)/len(got),4) if got else None,
        "cast_share_by_turn10": round(len(got)/len(ct),6),
        "mana_available_by_turn": [round(sum(r["mana"][t] for r in recs)/len(recs),4) for t in range(TURNS)],
        "mana_spent_by_turn": [round(sum(r["spent"][t] for r in recs)/len(recs),4) for t in range(TURNS)],
    }


def fast_effect(base,nofast):
    both=[(a["commander_turn"],b["commander_turn"]) for a,b in zip(base,nofast) if a["commander_turn"] is not None and b["commander_turn"] is not None]
    shift=[b-a for a,b in both]
    m,ci=sim.mean_ci(shift)
    return {
        "paired_cast_probability_delta_by_turn": {str(t):paired_indicator_delta(base,nofast,lambda r,t=t:r["commander_turn"] is not None and r["commander_turn"]<=t) for t in (2,3,4,5,6)},
        "mean_turn_acceleration_when_both_cast": {"value":round(m,4) if m is not None else None,"ci95":[round(ci[0],4),round(ci[1],4)] if m is not None else [None,None],"paired_games":len(shift)},
        "interpretation": "Positive values mean the listed fast-mana package increases/accelerates commander casting in this bounded goldfish counterfactual."
    }


def recovery(recs,index=0):
    eligible=[]; recovered=[]; delays=[]
    for r in recs:
        if len(r.get("removals",[]))<=index: continue
        eligible.append(r)
        rem=r["removals"][index]
        if len(r.get("recasts",[]))>index:
            rec=r["recasts"][index]; recovered.append(r); delays.append(rec-rem)
    m,ci=sim.mean_ci(delays)
    return {
        "removal_event_share":round(len(eligible)/len(recs),6),
        "recast_share_given_removal":round(len(recovered)/len(eligible),6) if eligible else 0.0,
        "recast_within_turns_given_removal": {str(k):round(sum(1 for x in delays if x<=k)/len(eligible),6) if eligible else 0.0 for k in (1,2,3)},
        "recovery_turns_mean_when_recast":{"value":round(m,4) if m is not None else None,"ci95":[round(ci[0],4),round(ci[1],4)] if m is not None else [None,None]},
        "event_count":len(eligible),"recast_count":len(recovered)
    }


def build_commander(slug,deck,name,fast_names,static,perms):
    iso=isolate_commander(deck,name)
    base=run_scenario(iso,perms)
    nofast=run_scenario(disable_fast_mana(iso,fast_names),perms)
    once=run_scenario(iso,perms,"commander_removed_once")
    twice=run_scenario(iso,perms,"commander_removed_twice")
    static_row=next((x for x in static["commander_casting"] if x["name"]==name),None)
    return {
        "commander":name,
        "static_cost":static_row,
        "fast_mana_inventory":sorted(fast_names),
        "baseline":cast_summary(base),
        "no_fast_mana_counterfactual":cast_summary(nofast),
        "fast_mana_contribution":fast_effect(base,nofast),
        "tax_recovery_after_one_removal":recovery(once,0),
        "tax_recovery_after_two_removals":{"first":recovery(twice,0),"second":recovery(twice,1)},
    }


def build_one(did,entry):
    slug=entry["slug"]; static=load(MANA/f"{slug}.json"); deck=sim.load_deck(slug)
    fast=set(static["fast_mana_cards"])
    # Same permutations for every commander and every perturbation in this deck.
    perms=permutations(deck)
    commanders=[build_commander(slug,deck,c["name"],fast,static,perms) for c in deck.commanders]
    return {
        "schema_version":1,"deck_id":did,"slug":slug,"canonical_hash":entry["canonical_project_list"]["hash"],
        "status":"provisional_test_evidence","evidence_class":"test_result","confidence":"moderate",
        "authority":{"can_decide":False,"note":"Commander-casting/tax stress cannot decide mana-base swaps or deck changes."},
        "method":{"simulator":"grixis_sim","model":"1.1","simulator_sha256":sim.model_sha256(),"samples":SAMPLES,"seed":SEED,"turns":TURNS,
                  "pairing":"same library permutations for baseline, no-fast counterfactual, and removal perturbations",
                  "commander_pair_policy":"each commander is simulated separately with the same 99 and deck color identity; co-commander cast-order competition is intentionally removed"},
        "commanders":commanders,
        "limitations":[
            "Goldfish engine only: no real opponents, interaction, politics or multiplayer win rates.",
            "Removal stress deterministically removes the isolated commander at end of the first eligible turn; it is a tax-recovery stress, not a real removal-frequency estimate.",
            "The no-fast counterfactual keeps fast-mana cards in draws but disables their mana modes and makes them uncastable; this isolates acceleration but ignores any alternate non-mana use.",
            "Existing grixis_sim v1.1 mana/card-effect limitations remain in force; this wrapper does not silently upgrade that simulator.",
            "Partner/background-style pairs are evaluated per commander to remove cast-order confounding; actual games can allocate mana between commanders differently.",
            "These tests measure commander access/recovery only; Step D separately measures commander marginal strategic value once available.",
        ]
    }


def build():
    reg=load(REGISTRY); rows=[]; OUT.mkdir(parents=True,exist_ok=True)
    for did,e in sorted(reg["decks"].items(),key=lambda kv:kv[1]["slug"]):
        d=build_one(did,e); dump(OUT/f"{e['slug']}.json",d)
        rows.append({"deck_id":did,"slug":e["slug"],"commanders":len(d["commanders"]),
                     "mean_cast_turn":round(sum((c["baseline"]["mean_turn_when_cast"] or TURNS) for c in d["commanders"])/len(d["commanders"]),4),
                     "mean_recast_share":round(sum(c["tax_recovery_after_one_removal"]["recast_share_given_removal"] for c in d["commanders"])/len(d["commanders"]),4)})
    dump(OUT/"summary.json",{"schema_version":1,"generated_by":f"scripts/grixis_commander_mana.py v{VERSION}","samples_per_scenario":SAMPLES,"decks":rows,
                             "totals":{"decks":len(rows),"commander_records":sum(x["commanders"] for x in rows)}})
    print(f"commander-mana: built {len(rows)} decks / {sum(x['commanders'] for x in rows)} commander records")


def check():
    try: import jsonschema
    except ImportError: print("commander-mana: jsonschema required"); return 1
    schema=load(SCHEMA); reg=load(REGISTRY); problems=[]
    expected={e["slug"] for e in reg["decks"].values()}; present={p.stem for p in OUT.glob("*.json") if p.name!="summary.json"}
    if expected!=present: problems.append(f"coverage mismatch missing={sorted(expected-present)} extra={sorted(present-expected)}")
    for did,e in sorted(reg["decks"].items()):
        p=OUT/f"{e['slug']}.json"
        if not p.exists(): continue
        d=load(p)
        for err in jsonschema.Draft202012Validator(schema).iter_errors(d): problems.append(f"{e['slug']}: schema {list(err.path)}: {err.message}")
        if d["canonical_hash"]!=e["canonical_project_list"]["hash"]: problems.append(f"{e['slug']}: canonical hash drift")
        if d["authority"]["can_decide"] is not False: problems.append(f"{e['slug']}: record became decision-capable")
        if d["method"]["simulator_sha256"]!=sim.model_sha256(): problems.append(f"{e['slug']}: simulator hash drift")
    print(f"commander-mana: {len(expected)} deck files, {len(problems)} problems")
    for p in problems[:40]: print("FAIL",p)
    return 1 if problems else 0


def main(argv=None):
    a=argparse.ArgumentParser(); a.add_argument("--build",action="store_true"); a.add_argument("--check",action="store_true"); a.add_argument("--summary",action="store_true"); x=a.parse_args(argv); rc=0
    if x.build: build()
    if x.check: rc|=check()
    if x.summary: print(json.dumps(load(OUT/"summary.json"),indent=2,sort_keys=True))
    if not (x.build or x.check or x.summary): a.print_help()
    return rc

if __name__=="__main__": sys.exit(main())
