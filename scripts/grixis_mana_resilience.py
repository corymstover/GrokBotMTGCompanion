#!/usr/bin/env python3
"""Step C batch 68.5: bounded mana/color-screw and one-source fragility diagnostics.

Consumes only committed Step C artifacts. It does not refresh card data, simulate opponents, or decide swaps.
"Screw" here means a declared draw/source-access failure under the exact no-mulligan presence models from 68.1/68.2,
not a claim about real-game loss probability. One-source-unavailable sensitivity replaces one source mask with an empty
mask while keeping library size fixed; it is a structural fragility probe, not a removal-frequency model.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_mana_timing as mt

REGISTRY=ROOT/"data/grixis/registry.json"
BASE=ROOT/"data/grixis/mana_base"
TIMING=ROOT/"data/grixis/mana_timing"
OUT=ROOT/"data/grixis/mana_resilience"
SCHEMA=ROOT/"data/grixis/schemas/mana_resilience.schema.json"
VERSION=1
ORDER="UBR"


def load(p): return json.loads(Path(p).read_text(encoding="utf-8"))

def dump(p,o):
    p=Path(p); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(o,indent=1,sort_keys=True,ensure_ascii=False)+"\n",encoding="utf-8")

def fail(p): return round(max(0.0,min(1.0,1.0-float(p))),6)


def masks_from_timing(timing,N,include_mdfc=False,field="potential_colors"):
    rows=list(timing.get("strict_land_sources",[]))
    if include_mdfc: rows+=list(timing.get("mdfc_optional_sources",[]))
    masks=[r.get(field,"") for r in rows]
    if len(masks)>N: raise ValueError("source rows exceed library size")
    return masks+[""]*(N-len(masks)), rows


def one_source_sensitivity(masks,labels,n,requirements):
    """Exact source-presence delta if any one currently useful source is unavailable from the opening deck.

    Absolute delta can be larger in a stronger/redundant mana base simply because its baseline success probability is
    much higher, so the record also reports delta as a fraction of baseline. Neither quantity is a cut threshold.
    """
    base=mt.distinct_source_match_probability(masks,n,requirements)
    rows=[]
    for i,m in enumerate(masks):
        if not m: continue
        alt=list(masks); alt[i]=""
        p=mt.distinct_source_match_probability(alt,n,requirements)
        delta=max(0.0,base-p)
        rows.append((delta,(delta/base if base>0 else 0.0),labels[i] if i<len(labels) else "<source>",m))
    if not rows:
        return {"baseline":round(base,6),"worst_delta":0.0,"mean_delta":0.0,"worst_relative_delta":0.0,"mean_relative_delta":0.0,"worst_sources":[],"sources_tested":0}
    worst=max(x[0] for x in rows); worst_rel=max(x[1] for x in rows)
    return {
        "baseline":round(base,6),
        "worst_delta":round(worst,6),
        "mean_delta":round(sum(x[0] for x in rows)/len(rows),6),
        "worst_relative_delta":round(worst_rel,6),
        "mean_relative_delta":round(sum(x[1] for x in rows)/len(rows),6),
        "worst_sources":sorted({x[2] for x in rows if abs(x[0]-worst)<1e-12}),
        "sources_tested":len(rows),
    }


def fetch_resilience(timing):
    out=[]
    for f in timing.get("fetch_validation",[]):
        fragile={c:list(v) for c,v in f.get("targets_by_color",{}).items() if len(v)==1}
        out.append({
            "card":f["card"],
            "target_count":f.get("target_count",0),
            "actual_target_colors":f.get("actual_target_colors",""),
            "single_target":f.get("target_count",0)==1,
            "colors_with_only_one_target":fragile,
            "all_supported_colors_have_redundant_targets":bool(f.get("actual_target_colors")) and not fragile,
        })
    return out


def demand_context(base):
    demand=base.get("pip_demand",{})
    sources=base.get("colored_sources",{}).get("land_sources",{})
    raw=demand.get("raw_colored_pip_equivalents",{})
    return {
        "pip_share":demand.get("share",{}),
        "early_pips_mv_le_2":demand.get("mv_le_2",{}),
        "early_pips_mv_le_3":demand.get("mv_le_3",{}),
        "double_pip_spell_count":demand.get("double_pip_spell_count",{}),
        "land_source_count":sources,
        "sources_per_raw_pip_equivalent":{c:(round(float(sources.get(c,0))/float(raw[c]),4) if float(raw.get(c,0) or 0)>0 else None) for c in ORDER},
        "note":"Source/pip ratios are descriptive pressure indicators only; they are not target thresholds or a land score."
    }


def build_one(did,entry):
    slug=entry["slug"]; base=load(BASE/f"{slug}.json"); timing=load(TIMING/f"{slug}.json")
    N=int(base["counts"]["library_cards"])
    strict_masks,strict_rows=masks_from_timing(timing,N,False,"potential_colors")
    strict_labels=[r["card"] for r in strict_rows]+["<non-source>"]*(N-len(strict_rows))
    turn={}
    for t in (2,3,4,5):
        b=base["turn_access_proxies"][str(t)]; r=timing["turn_readiness"][str(t)]; seen=int(r["cards_seen_no_mulligan"])
        turn[str(t)]={
            "cards_seen_no_mulligan":seen,
            "strict_land_drop_failure":fail(r["strict_land_drop_probability"]),
            "flex_land_drop_failure":fail(r["flex_land_drop_probability"]),
            "missing_any_UBR_potential_source_match":fail(r["potential_distinct_source_match_UBR"]),
            "missing_any_UBR_unconditional_source_match":fail(r["unconditional_distinct_source_match_UBR"]),
            "missing_any_UBR_untapped_capable_source_match":fail(r["untapped_capable_distinct_source_match_UBR"]),
            "missing_any_UBR_with_mdfc_option":fail(r["flex_land_potential_distinct_source_match_UBR"]),
            "missing_each_color_at_least_one_strict_land_source":{c:fail(b["per_color_at_least_one_land_source"][c]) for c in ORDER},
            "one_strict_source_unavailable_UBR":one_source_sensitivity(strict_masks,strict_labels,seen,{"U":1,"B":1,"R":1}),
        }
    commanders=[]
    for c in timing.get("commander_colored_readiness",[]):
        req=c.get("colored_requirements",{}); seen=int(c.get("cards_seen_by_base_resource_turn",7))
        commanders.append({
            "name":c["name"],"colored_requirements":req,"cards_seen_by_base_resource_turn":seen,
            "potential_colored_failure":fail(c["potential_distinct_source_match"]),
            "unconditional_colored_failure":fail(c["unconditional_distinct_source_match"]),
            "untapped_capable_colored_failure":fail(c["untapped_capable_distinct_source_match"]),
            "one_strict_source_unavailable":one_source_sensitivity(strict_masks,strict_labels,seen,req),
        })
    fetches=fetch_resilience(timing)
    return {
        "schema_version":1,"deck_id":did,"slug":slug,"canonical_hash":entry["canonical_project_list"]["hash"],
        "status":"provisional_evidence","evidence_class":"derived_metric","confidence":"moderate",
        "authority":{"can_decide":False,"note":"Mana-screw/color-screw and fragility diagnostics cannot decide a land or mana-source swap."},
        "inputs":{"mana_base":f"data/grixis/mana_base/{slug}.json","mana_timing":f"data/grixis/mana_timing/{slug}.json"},
        "turn_failure":turn,"commander_colored_failure":commanders,"demand_context":demand_context(base),
        "fetch_target_resilience":fetches,
        "summary":{"fetches":len(fetches),"single_target_fetches":sum(x["single_target"] for x in fetches),"fetch_color_single_points":sum(len(x["colors_with_only_one_target"]) for x in fetches),"commanders":len(commanders)},
        "limitations":[
            "Failure probabilities are complements of exact no-mulligan draw/source-presence proxies, not real-game loss probabilities or cast probabilities.",
            "The one-source-unavailable probe keeps library size fixed and blanks one source; it measures structural sensitivity, not the chance an opponent removes that source.",
            "Absolute one-source delta depends on the baseline success probability; relative delta is provided separately and neither is a universal fragility threshold.",
            "Conditional source requirements, sequencing, mulligan policy, rocks, rituals and life/payment decisions are not converted into invented reliability percentages.",
            "MDFC land faces remain an optional layer and do not silently increase the strict land count.",
            "Fetch-target fragility is measured at deck start; target depletion after earlier fetches is not simulated.",
            "No universal mana-quality score, threshold, cut, or automatic replacement is produced."
        ]
    }


def build():
    reg=load(REGISTRY); rows=[]; OUT.mkdir(parents=True,exist_ok=True)
    for did,e in sorted(reg["decks"].items(),key=lambda kv:kv[1]["slug"]):
        d=build_one(did,e); dump(OUT/f"{e['slug']}.json",d)
        rows.append({"deck_id":did,"slug":e["slug"],**d["summary"]})
    dump(OUT/"summary.json",{"schema_version":1,"generated_by":f"scripts/grixis_mana_resilience.py v{VERSION}","decks":rows,"totals":{"decks":len(rows),"single_target_fetches":sum(x["single_target_fetches"] for x in rows),"fetch_color_single_points":sum(x["fetch_color_single_points"] for x in rows),"commander_records":sum(x["commanders"] for x in rows)}})
    print(f"mana-resilience: built {len(rows)} decks")


def check():
    try: import jsonschema
    except ImportError: print("mana-resilience: jsonschema required"); return 1
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
        for t,row in d["turn_failure"].items():
            for k,v in row.items():
                if k.endswith("failure") and isinstance(v,(int,float)) and not 0<=v<=1: problems.append(f"{e['slug']}: {t} {k} out of bounds")
    print(f"mana-resilience: {len(expected)} deck files, {len(problems)} problems")
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
