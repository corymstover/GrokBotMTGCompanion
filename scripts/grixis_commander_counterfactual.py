#!/usr/bin/env python3
"""Step D batch 69.2: paired commander counterfactual simulator architecture.

Modes are intentionally separated rather than collapsed into one commander-value score:
  normal      canonical commander(s) available from the command zone;
  unavailable commander(s) absent for the whole goldfish (library remains 99; no fake replacement card);
  taxed       every commander's first cast pays +2 generic, modelling one extra commander-tax increment;
  disrupted   canonical commander(s), using the existing bounded `commander_removed_twice` stress proxy.

The same library permutation and RNG seed are used across modes for each sample. Outputs are model deltas with explicit
limitations, not multiplayer win rates and not deck-change decisions. Real-deck generation requires the frozen local
Scryfall cache because grixis_sim.load_deck does; synthetic architecture/tests run in cache-free CI.
"""
from __future__ import annotations

import argparse
import copy
import json
import random
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_sim as sim

REG=ROOT/"data/grixis/registry.json"
STRUCT=ROOT/"data/grixis/commander_structure"
OUT=ROOT/"data/grixis/commander_counterfactual"
SCHEMA=ROOT/"data/grixis/schemas/commander_counterfactual.schema.json"
VERSION=1
MODES=("normal","unavailable","taxed","disrupted")


def load(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def dump(p,o):
    p=Path(p); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(o,indent=1,sort_keys=True,ensure_ascii=False)+"\n",encoding="utf-8")

def clone_deck(deck, commanders=None):
    d=sim.Deck(deck.slug,list(deck.commanders if commanders is None else commanders),list(deck.library),
               {k:set(v) for k,v in deck.key_sets.items()},[dict(id=x["id"],cards=list(x["cards"])) for x in deck.combos])
    d.ci=set(deck.ci); d.engine=set(getattr(deck,"engine",set())); d.gy_combo=dict(getattr(deck,"gy_combo",{}))
    return d

def unavailable_deck(deck):
    """Commander absent from the whole game. Library stays the same 99-card library."""
    return clone_deck(deck,[])

def taxed_deck(deck,extra_generic=2):
    """Add a starting generic commander-tax increment without altering mana value."""
    cmds=[]
    for cm in deck.commanders:
        c=copy.deepcopy(cm); c["cost"]=copy.deepcopy(c["cost"]); c["cost"]["generic"]+=extra_generic; cmds.append(c)
    return clone_deck(deck,cmds)


def permutations(deck,samples,seed):
    return [random.Random(sim.seed_for(seed+100003,i)).sample(range(deck.N),deck.N) for i in range(samples)]

def run_mode(deck,mode,samples=500,seed=69,turns=10,perms=None):
    if mode not in MODES: raise ValueError(mode)
    d=unavailable_deck(deck) if mode=="unavailable" else taxed_deck(deck) if mode=="taxed" else deck
    perms=perms or permutations(deck,samples,seed)
    scenario={"kind":"commander_removed_twice","T":4} if mode=="disrupted" else None
    out=[]
    for i in range(samples):
        rng=random.Random(sim.seed_for(seed,i))
        out.append(sim.play_game(d,rng,turns=turns,perm=perms[i],scenario=scenario,model="1.1"))
    return d,out

def mean(xs): return sum(xs)/len(xs) if xs else None
def by_turn(recs,key,t): return mean([r[key][t-1] for r in recs])
def share(recs,pred): return sum(bool(pred(r)) for r in recs)/len(recs) if recs else 0.0


def metric_record(deck,recs,turns=10,mode="normal"):
    n=len(recs); keysets=sorted(deck.key_sets)
    commander_names={c["name"] for c in deck.commanders}
    r={
      "samples":n,
      "commander_cast_by_turn6":share(recs,lambda x:x.get("commander_turn") is not None and x["commander_turn"]<=6),
      "commander_turn_mean_when_cast":mean([x["commander_turn"] for x in recs if x.get("commander_turn") is not None]),
      "mana_spent_t1_6_mean":mean([sum(x["spent"][:6]) for x in recs]),
      "mana_available_t1_6_mean":mean([sum(x["mana"][:6]) for x in recs]),
      "extra_cards_drawn_mean":mean([x.get("drawn_extra",0) for x in recs]),
      "tutors_resolved_mean":mean([len(x.get("tutored",[])) for x in recs]),
      "fast_mana_uses_mean":mean([x.get("fast_mana_used",0) for x in recs]),
      "first_key_set_access_by_turn4":{k:share(recs,lambda x,k=k:x["key_turn"].get(k) is not None and x["key_turn"][k]<=4) for k in keysets},
      "combo_assembled_by_turn6":share(recs,lambda x:x.get("combo_turn") is not None and x["combo_turn"]<=6) if deck.combos else None,
      "win_proxy_by_turn6":share(recs,lambda x:x.get("win_turn_proxy") is not None and x["win_turn_proxy"]<=6) if deck.combos else None,
      "note":"first_key_set_access means first access to any member of the simulator key set; it is not package completion or engine-online probability."
    }
    if mode=="unavailable":
        r["commander_cast_by_turn6"]=0.0; r["commander_turn_mean_when_cast"]=None
    if mode=="disrupted":
        occurred=[x for x in recs if x.get("removals")]
        recast=[x for x in occurred if x.get("recasts")]
        r["disruption_recovery"]={
          "removal_event_share":len(occurred)/n if n else 0.0,
          "recast_after_removal_share":len(recast)/len(occurred) if occurred else None,
          "recovery_turns_mean":mean([x["recasts"][0]-x["removals"][0] for x in recast]),
          "scenario":"commander_removed_twice from turn 4; for multi-commander decks the legacy stress hook removes one on-board commander at a time and is therefore only a bounded disruption proxy"
        }
    return r


def delta(a,b):
    """normal minus counterfactual for scalar metrics; positive generally means normal had more/earlier access only where documented."""
    keys=("commander_cast_by_turn6","mana_spent_t1_6_mean","mana_available_t1_6_mean","extra_cards_drawn_mean","tutors_resolved_mean","fast_mana_uses_mean","combo_assembled_by_turn6","win_proxy_by_turn6")
    out={}
    for k in keys:
        av,bv=a.get(k),b.get(k); out[k]=None if av is None or bv is None else round(av-bv,6)
    out["first_key_set_access_by_turn4"]={k:round(a["first_key_set_access_by_turn4"].get(k,0)-b["first_key_set_access_by_turn4"].get(k,0),6) for k in sorted(set(a["first_key_set_access_by_turn4"])|set(b["first_key_set_access_by_turn4"]))}
    return out


def evaluate(deck,samples=500,seed=69,turns=10):
    perms=permutations(deck,samples,seed); modes={}; raw={}
    for mode in MODES:
        d,recs=run_mode(deck,mode,samples,seed,turns,perms); raw[mode]=recs; modes[mode]=metric_record(d,recs,turns,mode)
    return modes,{m:delta(modes["normal"],modes[m]) for m in ("unavailable","taxed","disrupted")}


def build_one(slug,samples=500,seed=69,turns=10):
    reg=load(REG); did,e=next((did,e) for did,e in reg["decks"].items() if e["slug"]==slug)
    deck=sim.load_deck(slug); modes,deltas=evaluate(deck,samples,seed,turns); structural=load(STRUCT/f"{slug}.json")
    return {
      "schema_version":1,"deck_id":did,"slug":slug,"canonical_hash":e["canonical_project_list"]["hash"],
      "status":"provisional_test_evidence","evidence_class":"test_result","confidence":"low",
      "authority":{"can_decide":False,"note":"Commander counterfactual simulator deltas are bounded test evidence only; they cannot decide commander value or deck changes."},
      "model":{"simulator":"grixis_sim v1.1","samples":samples,"seed":seed,"turns":turns,"paired_library_permutations":True,
               "modes":{"normal":"canonical commander(s) available","unavailable":"commander(s) absent for entire game; 99-card library unchanged","taxed":"+2 generic on every commander's first cast, then normal tax increments","disrupted":"existing commander_removed_twice stress proxy from turn 4"}},
      "structural_context":{"path":f"data/grixis/commander_structure/{slug}.json","accepted_blueprint_role":structural["accepted_blueprint_role"],"summary":structural["summary"]},
      "metrics":modes,"normal_minus_counterfactual":deltas,
      "unmodeled_required_dimensions":["true meaningful-action count (v1.1 does not expose cast/action events)","commander-native triggered/activated value not represented by v1.1 mechanics","opponent interaction and multiplayer politics","exact partner-pair disruption of both commanders simultaneously"],
      "limitations":["Goldfish/proxy results are not multiplayer win rates or estimates of real-game win probability.","The unavailable mode removes commander access without adding a replacement library card; this isolates command-zone availability rather than changing deck size.","The taxed mode is a sensitivity point (+2 starting generic commander cost), not a distribution of commander tax in real games.","The disrupted mode reuses the legacy deterministic commander-removal stress hook; multi-commander decks receive a bounded one-at-a-time proxy, not simultaneous pair disruption.","First key-set access means access to any member, not package completion or engine-online probability.","v1.1 omits many commander-native mechanics; structural Blueprint evidence must be read alongside dynamic deltas.","No scalar commander-dependence score is produced."]
    }


def build_all(samples=500,seed=69,turns=10):
    reg=load(REG); OUT.mkdir(parents=True,exist_ok=True); rows=[]
    for did,e in sorted(reg["decks"].items(),key=lambda kv:kv[1]["slug"]):
        d=build_one(e["slug"],samples,seed,turns); dump(OUT/f"{e['slug']}.json",d); rows.append({"deck_id":did,"slug":e["slug"],"role":d["structural_context"]["accepted_blueprint_role"]["level"]})
    dump(OUT/"summary.json",{"schema_version":1,"generated_by":f"scripts/grixis_commander_counterfactual.py v{VERSION}","samples_per_mode":samples,"decks":rows,"totals":{"decks":len(rows)}})
    print(f"commander-counterfactual: built {len(rows)} decks")


def check():
    try: import jsonschema
    except ImportError: print("commander-counterfactual: jsonschema required"); return 1
    reg=load(REG); schema=load(SCHEMA); expected={e["slug"] for e in reg["decks"].values()}; present={p.stem for p in OUT.glob("*.json") if p.name!="summary.json"} if OUT.exists() else set(); problems=[]
    if not present:
        print("commander-counterfactual: 0/62 generated records; code ready, frozen-local-cache generation pending")
        return 0
    if present!=expected: problems.append(f"partial population missing={sorted(expected-present)} extra={sorted(present-expected)}")
    for did,e in sorted(reg["decks"].items()):
        p=OUT/f"{e['slug']}.json"
        if not p.exists(): continue
        d=load(p)
        for err in jsonschema.Draft202012Validator(schema).iter_errors(d): problems.append(f"{e['slug']}: schema {list(err.path)}: {err.message}")
        if d["canonical_hash"]!=e["canonical_project_list"]["hash"]: problems.append(f"{e['slug']}: canonical hash drift")
        if d["authority"]["can_decide"] is not False: problems.append(f"{e['slug']}: record became decision-capable")
    print(f"commander-counterfactual: {len(present)}/62 records, {len(problems)} problems")
    for p in problems[:40]: print("FAIL",p)
    return 1 if problems else 0


def main(argv=None):
    a=argparse.ArgumentParser(); a.add_argument("--deck"); a.add_argument("--build",action="store_true"); a.add_argument("--check",action="store_true"); a.add_argument("--samples",type=int,default=500); a.add_argument("--seed",type=int,default=69); a.add_argument("--turns",type=int,default=10); x=a.parse_args(argv); rc=0
    if x.deck:
        d=build_one(x.deck,x.samples,x.seed,x.turns); print(json.dumps(d,indent=2,sort_keys=True))
    if x.build: build_all(x.samples,x.seed,x.turns)
    if x.check: rc|=check()
    if not (x.deck or x.build or x.check): a.print_help()
    return rc
if __name__=="__main__": sys.exit(main())
