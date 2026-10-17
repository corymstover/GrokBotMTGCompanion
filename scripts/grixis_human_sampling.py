#!/usr/bin/env python3
"""Step H batch 71.2: deterministic, pre-registered human-quality sampler.

Static strata are populated now from committed pre-M6 evidence. Dynamic strata are deliberately left empty until their
pre-registered M6-stage inputs exist. The same ranking functions are exposed for synthetic regression tests and later
M6 execution; input order never affects selection.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
REG=ROOT/"data/grixis/registry.json"
POLICY=ROOT/"data/grixis/human_sampling_policy.json"
FREEZE=ROOT/"data/grixis/human_sampling_freeze.json"
SAT=ROOT/"data/grixis/saturation"
STRUCT=ROOT/"data/grixis/commander_structure"
M1=ROOT/"data/grixis_interactions"
BP=ROOT/"data/grixis/blueprints"
OUT=ROOT/"data/grixis/human_sampling_manifest.json"
SCHEMA=ROOT/"data/grixis/schemas/human_sampling_manifest.schema.json"
VERSION=1
ROLE_RANK={"supporting":0,"significant":1,"central":2}
STATIC=("random","anomaly","exception","pending_release","cedh","low_commander_dependence","rules_sensitive")
DYNAMIC=("high_optimizer_disagreement","major_change")


def load(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def dump(p,o): Path(p).write_text(json.dumps(o,indent=1,sort_keys=True,ensure_ascii=False)+"\n",encoding="utf-8")
def tie(seed,stratum,slug): return hashlib.sha256(f"{seed}|{stratum}|{slug}".encode()).hexdigest()

def quota_value(policy,sid):
    q=next(x for x in policy["strata"] if x["id"]==sid)["quota"]
    return q

def ceiling(e):
    c=e.get("ceiling",{})
    for key in ("resolved_ceiling","grok_estimated_ceiling","source_ceiling"):
        v=(c.get(key) or {}).get("value")
        if v is not None:
            try: return int(v),key
            except Exception: pass
    return None,"unresolved"

def authorized_exception(e):
    return bool(e.get("project_exceptions")) or e.get("project_authorization_status") not in (None,"none","NONE","")

def pending_release(e):
    return e.get("state")=="PENDING_RELEASE" or (e.get("official_commander_compliance") or {}).get("status")=="pending_release"

def static_row(did,e,seed):
    slug=e["slug"]
    sat=load(SAT/f"{slug}.json")
    st=load(STRUCT/f"{slug}.json")
    m1=load(M1/f"{slug}.json")
    bp=load(BP/f"{slug}.json")
    s=st["summary"]
    linked=s["combo_direct_commander_piece"]+s["combo_blueprint_supported"]
    combo_frac=linked/max(1,s["spellbook_lines"])
    win_frac=s["blueprint_wins_explicit_commander"]/max(1,s["blueprint_wins"])
    interactions=m1.get("interactions",[])
    non_verified=sum(x.get("status")!="verified" for x in interactions)
    key_count=sum(bool(x.get("key")) for x in interactions)
    construction_rule_count=len(bp.get("construction_rules",[]))
    risk_bonus=2 if authorized_exception(e) or pending_release(e) else 0
    rule_score=3*non_verified+key_count+construction_rule_count+risk_bonus
    anomaly=(sat.get("universe",{}).get("by_escalation_reason",{}) or {}).get("anomaly_source_disagreement",0)
    cv,csrc=ceiling(e)
    return {
      "deck_id":did,"slug":slug,
      "random":{"eligible":True,"tie_hash":tie(seed,"random",slug)},
      "anomaly":{"eligible":anomaly>0,"anomaly_count":anomaly,"tie_hash":tie(seed,"anomaly",slug)},
      "exception":{"eligible":authorized_exception(e),"exception_count":len(e.get("project_exceptions",[])),"project_authorization_status":e.get("project_authorization_status"),"tie_hash":tie(seed,"exception",slug)},
      "pending_release":{"eligible":pending_release(e),"registry_state":e.get("state"),"official_compliance":(e.get("official_commander_compliance") or {}).get("status"),"tie_hash":tie(seed,"pending_release",slug)},
      "cedh":{"eligible":cv==5,"ceiling":cv,"ceiling_source":csrc,"tie_hash":tie(seed,"cedh",slug)},
      "low_commander_dependence":{"eligible":True,"role":st["accepted_blueprint_role"]["level"],"role_rank":ROLE_RANK.get(st["accepted_blueprint_role"]["level"],9),"commander_linked_combo_fraction":round(combo_frac,6),"explicit_commander_win_fraction":round(win_frac,6),"tie_hash":tie(seed,"low_commander_dependence",slug)},
      "rules_sensitive":{"eligible":True,"non_verified_interactions":non_verified,"key_interactions":key_count,"construction_rule_count":construction_rule_count,"exception_pending_bonus":risk_bonus,"rules_risk_score":rule_score,"tie_hash":tie(seed,"rules_sensitive",slug)}
    }

def ranked_static(rows,sid,quota):
    eligible=[r for r in rows if r[sid]["eligible"]]
    if sid=="random": key=lambda r:(r[sid]["tie_hash"],r["slug"])
    elif sid=="anomaly": key=lambda r:(-r[sid]["anomaly_count"],r[sid]["tie_hash"],r["slug"])
    elif sid in ("exception","pending_release"): key=lambda r:(r["slug"],r[sid]["tie_hash"])
    elif sid=="cedh": key=lambda r:(r[sid]["tie_hash"],r["slug"])
    elif sid=="low_commander_dependence": key=lambda r:(r[sid]["role_rank"],r[sid]["commander_linked_combo_fraction"],r[sid]["explicit_commander_win_fraction"],r[sid]["tie_hash"],r["slug"])
    elif sid=="rules_sensitive": key=lambda r:(-r[sid]["rules_risk_score"],r[sid]["tie_hash"],r["slug"])
    else: raise ValueError(sid)
    ranked=sorted(eligible,key=key)
    picked=ranked if quota=="all" else ranked[:int(quota)]
    return [{"rank":i+1,"deck_id":r["deck_id"],"slug":r["slug"],"selection_inputs":{k:v for k,v in r[sid].items() if k!="eligible"}} for i,r in enumerate(picked)],len(eligible)

def swap_pair(s):
    if isinstance(s,str): return s
    if isinstance(s,dict):
        cut=s.get("cut") or (s.get("cuts") or [None])[0]
        add=s.get("add") or (s.get("adds") or [None])[0]
        if cut is None or add is None: raise ValueError(f"swap missing cut/add: {s}")
        return f"{cut}=>{add}"
    raise TypeError(s)

def optimizer_disagreement_selection(records,seed,quota=8):
    scored=[]
    for r in records:
        required=("slug","pass_a_hash","pass_b_hash","pass_a_challenger_hash","pass_b_challenger_hash","pass_a_swaps","pass_b_swaps")
        if any(k not in r or r[k] in (None,"") for k in required): raise ValueError(f"optimizer record missing committed fields: {r.get('slug')}")
        a={swap_pair(x) for x in r["pass_a_swaps"]}; b={swap_pair(x) for x in r["pass_b_swaps"]}
        ca={x.split("=>",1)[0] for x in a}; cb={x.split("=>",1)[0] for x in b}
        score={"challenger_hash_disagreement":int(r["pass_a_challenger_hash"]!=r["pass_b_challenger_hash"]),"swap_symmetric_difference_count":len(a^b),"cut_conflict_count":len(ca^cb),"tie_hash":tie(seed,"high_optimizer_disagreement",r["slug"])}
        scored.append((r,score))
    scored.sort(key=lambda x:(-x[1]["challenger_hash_disagreement"],-x[1]["swap_symmetric_difference_count"],-x[1]["cut_conflict_count"],x[1]["tie_hash"],x[0]["slug"]))
    return [{"rank":i+1,"slug":r["slug"],"selection_inputs":s,"source_hashes":{"pass_a_hash":r["pass_a_hash"],"pass_b_hash":r["pass_b_hash"]}} for i,(r,s) in enumerate(scored[:quota])]

def major_change_selection(records,seed,quota=8):
    scored=[]
    for r in records:
        required=("slug","total_swaps","win_route_changed","required_package_change_count","mana_base_change_count")
        if any(k not in r for k in required): raise ValueError(f"major-change record missing fields: {r.get('slug')}")
        eligible=r["total_swaps"]>=5 or bool(r["win_route_changed"]) or r["required_package_change_count"]>0 or r["mana_base_change_count"]>=3
        if not eligible: continue
        s={"win_route_changed":int(bool(r["win_route_changed"])),"required_package_change_count":int(r["required_package_change_count"]),"total_swaps":int(r["total_swaps"]),"mana_base_change_count":int(r["mana_base_change_count"]),"tie_hash":tie(seed,"major_change",r["slug"])}
        scored.append((r,s))
    scored.sort(key=lambda x:(-x[1]["win_route_changed"],-x[1]["required_package_change_count"],-x[1]["total_swaps"],-x[1]["mana_base_change_count"],x[1]["tie_hash"],x[0]["slug"]))
    return [{"rank":i+1,"slug":r["slug"],"selection_inputs":s} for i,(r,s) in enumerate(scored[:quota])]

def build_manifest():
    reg=load(REG); policy=load(POLICY); freeze=load(FREEZE)
    actual="sha256:"+hashlib.sha256(POLICY.read_bytes()).hexdigest()
    if actual!=freeze["policy_sha256"]: raise RuntimeError("sampling policy hash drift")
    seed=policy["seed"]
    rows=[static_row(did,e,seed) for did,e in sorted(reg["decks"].items(),key=lambda kv:kv[1]["slug"])]
    strata=[]; memberships={}
    for sid in STATIC:
        selected,eligible=ranked_static(rows,sid,quota_value(policy,sid))
        for x in selected: memberships.setdefault(x["slug"],[]).append(sid)
        strata.append({"id":sid,"timing":"pre_m6_static","status":"selected","quota":quota_value(policy,sid),"eligible_count":eligible,"selected_count":len(selected),"selected":selected})
    for sid in DYNAMIC:
        p=next(x for x in policy["strata"] if x["id"]==sid)
        strata.append({"id":sid,"timing":p["timing"],"status":"awaiting_future_inputs","quota":p["quota"],"eligible_count":None,"selected_count":0,"selected":[]})
    dedupe=[{"slug":slug,"memberships":sorted(ms)} for slug,ms in sorted(memberships.items())]
    return {
      "schema_version":1,"status":"static_strata_frozen_dynamic_strata_awaiting_inputs","generated_by":f"scripts/grixis_human_sampling.py v{VERSION}",
      "policy_path":"data/grixis/human_sampling_policy.json","policy_sha256":freeze["policy_sha256"],"freeze_path":"data/grixis/human_sampling_freeze.json","seed":seed,
      "authority":{"can_decide":False,"note":"Sampling selects a minimum review workload only; membership is not a negative deck judgment and scripts may not author the resulting review."},
      "strata":strata,"deduped_static_workload":dedupe,
      "dynamic_hooks":{"high_optimizer_disagreement":{"function":"optimizer_disagreement_selection","required_fields":policy["future_result_contract"]["high_optimizer_disagreement"]["required_fields"]},"major_change":{"function":"major_change_selection","required_fields":policy["future_result_contract"]["major_change"]["required_fields"]}},
      "limitations":["Static selections reflect only the frozen pre-M6 evidence currently committed.","Dynamic strata intentionally contain no selections before their M6-stage inputs exist.","Overlap between strata is preserved even though the total review workload is deduplicated.","Cory may review additional decks beyond this minimum obligation.","Selection does not confer decision authority or certify unselected decks."]
    }

def build(): d=build_manifest(); dump(OUT,d); print(json.dumps({x["id"]:x["selected_count"] for x in d["strata"]},indent=2,sort_keys=True)); print("deduped_static",len(d["deduped_static_workload"]))
def check():
    try: import jsonschema
    except ImportError: print("human-sampling: jsonschema required"); return 1
    probs=[]
    if not OUT.exists(): probs.append("sampling manifest missing")
    else:
        d=load(OUT); schema=load(SCHEMA)
        probs += [f"schema {list(e.path)}: {e.message}" for e in jsonschema.Draft202012Validator(schema).iter_errors(d)]
        try: expected=build_manifest()
        except Exception as e: probs.append(f"cannot replay sampler: {type(e).__name__}: {e}"); expected=None
        if expected is not None and d!=expected: probs.append("sampling manifest is not byte-content-equivalent to deterministic replay")
        ids=[x["id"] for x in d.get("strata",[])]
        if set(ids)!=set(STATIC+DYNAMIC): probs.append("strata set mismatch")
        dyn=[x for x in d.get("strata",[]) if x["id"] in DYNAMIC]
        if any(x["status"]!="awaiting_future_inputs" or x["selected"] or x["selected_count"]!=0 for x in dyn): probs.append("dynamic strata populated before future inputs")
        if d.get("authority",{}).get("can_decide") is not False: probs.append("manifest became decision-capable")
    print(f"human-sampling: {len(probs)} problems")
    for p in probs: print("FAIL",p)
    return 1 if probs else 0

def main(argv=None):
    a=argparse.ArgumentParser(); a.add_argument("--build",action="store_true"); a.add_argument("--check",action="store_true"); a.add_argument("--show",action="store_true"); x=a.parse_args(argv); rc=0
    if x.build: build()
    if x.check: rc|=check()
    if x.show: print(json.dumps(load(OUT),indent=2,sort_keys=True))
    if not (x.build or x.check or x.show): a.print_help()
    return rc
if __name__=="__main__": sys.exit(main())
