#!/usr/bin/env python3
"""Step C batch 68.4: utility-land/MDFC opportunity costs and land-type Commander-first signals.

This layer deliberately keeps costs and benefits as separate dimensions. It never collapses them into a universal
"land score" because a colorless/tapped utility land can be correct for one commander and wrong for another. Blueprint
and commander-text signals are evidence for later judgment, not automatic protections or cuts.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_mana_base as mb
import grixis_mana_timing as mt

REGISTRY=ROOT/"data/grixis/registry.json"
BASE=ROOT/"data/grixis/mana_base"
TIMING=ROOT/"data/grixis/mana_timing"
BLUE=ROOT/"data/grixis/blueprints"
OUT=ROOT/"data/grixis/mana_opportunity"
SCHEMA=ROOT/"data/grixis/schemas/mana_opportunity.schema.json"
VERSION=1

LAND_HOOKS={
    "landfall":r"\blandfall\b",
    "land_enters":r"\b(?:a|another|one or more) lands? enters?\b|\bland enters the battlefield\b",
    "lands_you_control":r"\blands? you control\b",
    "land_card":r"\bland cards?\b",
    "basic_land":r"\bbasic lands?\b",
    "nonbasic_land":r"\bnonbasic lands?\b",
    "island":r"\bIsland\b",
    "swamp":r"\bSwamp\b",
    "mountain":r"\bMountain\b",
    "land_generic":r"\blands?\b",
}
UTILITY_PATTERNS={
    "card_advantage":r"\bdraw (?:a|one|two|three|that many|X) cards?\b|\bexile the top\b",
    "graveyard":r"\bgraveyard\b|\bmill\b",
    "sacrifice":r"\bsacrifice\b",
    "token":r"\bcreate\b[^.]*\btoken",
    "removal_or_damage":r"\bdestroy target\b|\bexile target\b|\bdeals? \d+ damage\b|\bdamage to\b",
    "tutor_or_search":r"\bsearch your library\b",
    "recursion":r"\breturn target\b[^.]*\bfrom your graveyard\b|\breturn\b[^.]*\bfrom your graveyard\b",
    "creature_mode":r"\bbecomes? a\b[^.]*\bcreature\b|\bcreate\b[^.]*\bcreature token",
    "cost_reduction_or_ramp":r"\bcosts? .* less\b",
    "protection":r"\bhexproof\b|\bindestructible\b|\bprotection from\b",
}


def load(p): return json.loads(Path(p).read_text(encoding="utf-8"))

def dump(p,o):
    p=Path(p); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(o,indent=1,sort_keys=True,ensure_ascii=False)+"\n",encoding="utf-8")


def strings(obj):
    if isinstance(obj,str): return [obj]
    if isinstance(obj,list):
        out=[]
        for x in obj: out.extend(strings(x))
        return out
    if isinstance(obj,dict):
        out=[]
        for x in obj.values(): out.extend(strings(x))
        return out
    return []


def direct_oracle(card):
    return "\n".join(mb._direct_lines(card["oracle"]))


def utility_text(card):
    """Direct non-mana utility text. Pure mana abilities, fetch-fixing clauses and ETB-tapped boilerplate are excluded."""
    keep=[]
    for line in mb._direct_lines(card["oracle"]):
        low=line.lower()
        if "add " in low:
            continue
        if "search your library" in low and ("land card" in low or any(t.lower() in low for t in mb.BASIC_TYPE_COLOR)):
            continue
        if re.search(r"enters(?: the battlefield)? tapped",low) and not any(x in low for x in ("draw","exile","sacrifice","create","destroy","return","mill")):
            continue
        keep.append(line)
    return "\n".join(keep)


def utility_categories(card):
    text=utility_text(card)
    return sorted(k for k,pat in UTILITY_PATTERNS.items() if re.search(pat,text,re.I))


def commander_hooks(blueprint):
    out=[]
    for c in blueprint.get("commanders",{}).get("value",[]):
        text=c.get("oracle_text","")
        terms=sorted(k for k,pat in LAND_HOOKS.items() if re.search(pat,text,re.I))
        if terms: out.append({"commander":c.get("name"),"terms":terms,"oracle_text":text})
    return out


def blueprint_mentions(blueprint,name):
    return any(name in s for s in strings(blueprint))


def source_map(timing):
    return {x["card"]:x for x in timing.get("strict_land_sources",[])+timing.get("mdfc_optional_sources",[])}


def burden_flags(src):
    out=[]
    if not src.get("potential_colors"): out.append("no_usable_grixis_color")
    elif len(src["potential_colors"])==1: out.append("single_color_source")
    if src.get("entry_timing")=="always_tapped": out.append("always_enters_tapped")
    elif src.get("entry_timing")=="conditional_untapped": out.append("conditional_untapped")
    if src.get("conditional_mana_ability"): out.append("conditional_mana_ability")
    if src.get("kind")=="fetch" and not src.get("fetch_target_count"): out.append("stranded_fetch")
    return out


def support_flags(name,card,blueprint,graph_node=None):
    out=[]
    if blueprint_mentions(blueprint,name): out.append("named_in_blueprint")
    cats=utility_categories(card)
    if cats: out.append("nonmana_utility_text")
    if graph_node:
        if graph_node.get("identity_core"): out.append("graph_identity_core")
        if graph_node.get("packages"): out.append("graph_package_member")
        if graph_node.get("tutor_target"): out.append("graph_tutor_target")
    return sorted(out)


def graph_nodes(slug):
    p=ROOT/"data/grixis/graph"/f"{slug}.json"
    if not p.exists(): return {}
    d=load(p)
    return {x.get("name"):x for x in d.get("nodes",[]) if x.get("kind")=="card" and x.get("name")}


def library(entry,db):
    ents=mb.parse_export(ROOT/entry["canonical_project_list"]["export"])
    cmds=[db.get(n) for z,q,n in ents if z=="commander"]
    ci=set().union(*(set(c["color_identity"])&set(mb.COLORS) for c in cmds))
    rows=[]
    for z,q,n in ents:
        if z!="main": continue
        c=mb.classify(db.get(n),ci)
        for _ in range(q): rows.append((n,c))
    return rows


def utility_record(name,card,src,blueprint,node):
    cats=utility_categories(card)
    return {
        "card":name,
        "potential_colors":src.get("potential_colors",""),
        "unconditional_colors":src.get("unconditional_colors",""),
        "entry_timing":src.get("entry_timing"),
        "conditional_mana_ability":bool(src.get("conditional_mana_ability")),
        "burden_flags":burden_flags(src),
        "utility_categories":cats,
        "support_flags":support_flags(name,card,blueprint,node),
        "blueprint_named":blueprint_mentions(blueprint,name),
        "graph_roles":sorted(node.get("roles",[])) if node else [],
        "graph_packages":sorted(node.get("packages",[])) if node else [],
        "oracle_text":card["oracle"],
        "authority":{"can_decide":False,"note":"Separate burden/support dimensions only; no utility land is automatically cut or retained."},
    }


def mdfc_record(name,card,src,blueprint,node):
    pips=card["cost"]
    flags=burden_flags(src)
    if card["mv"]>=4: flags.append("high_mv_spell_face")
    return {
        "card":name,
        "spell_face":{"mana_cost":card["mana_cost"],"mana_value":card["mv"],"colored_pip_equivalents":pips["colored_equivalent"]},
        "land_face":{"potential_colors":src.get("potential_colors",""),"unconditional_colors":src.get("unconditional_colors",""),"entry_timing":src.get("entry_timing")},
        "tradeoff_flags":sorted(set(flags)),
        "support_flags":support_flags(name,card,blueprint,node),
        "blueprint_named":blueprint_mentions(blueprint,name),
        "graph_roles":sorted(node.get("roles",[])) if node else [],
        "graph_packages":sorted(node.get("packages",[])) if node else [],
        "authority":{"can_decide":False,"note":"MDFC flexibility is recorded as an option-value tradeoff; this does not silently count the card as a full land or a free spell slot."},
    }


def build_one(did,entry,db):
    slug=entry["slug"]; base=load(BASE/f"{slug}.json"); timing=load(TIMING/f"{slug}.json"); blue=load(BLUE/f"{slug}.json"); srcs=source_map(timing); nodes=graph_nodes(slug); lib=library(entry,db)
    byname={}
    for n,c in lib: byname.setdefault(n,c)
    # 68.1 used a deliberately narrow utility heuristic. 68.4 widens the review population to any strict land
    # with direct non-mana utility text, while preserving the old list as a signal source.
    utility_names=set(base["utility_opportunity_cost"]["utility_lands"])
    for name,c in byname.items():
        if c["land"] and utility_categories(c): utility_names.add(name)
    utilities=[]
    for name in sorted(utility_names):
        c=byname.get(name); src=srcs.get(name)
        if c and src: utilities.append(utility_record(name,c,src,blue,nodes.get(name)))
    mdfcs=[]
    for name in base["mdfc_cards"]:
        c=byname.get(name); src=srcs.get(name)
        if c and src: mdfcs.append(mdfc_record(name,c,src,blue,nodes.get(name)))
    hooks=commander_hooks(blue)
    own_type_counts={k:v for k,v in base["land_type_coverage"]["typed_land_counts"].items() if k in ("Island","Swamp","Mountain")}
    relevant_types=sorted({term.capitalize() for h in hooks for term in h["terms"] if term in ("island","swamp","mountain")})
    named_lands=sorted(n for n,c in lib if c["land"] and blueprint_mentions(blue,n))
    burdens=Counter(x for u in utilities for x in u["burden_flags"]); supports=Counter(x for u in utilities for x in u["support_flags"])
    return {
        "schema_version":1,"deck_id":did,"slug":slug,"canonical_hash":entry["canonical_project_list"]["hash"],"status":"provisional_evidence","evidence_class":"derived_metric","confidence":"moderate",
        "authority":{"can_decide":False,"note":"Step C opportunity-cost evidence does not rank/cut lands; burden and Commander-first support remain separate for later judgment."},
        "inputs":{"mana_base":f"data/grixis/mana_base/{slug}.json","mana_timing":f"data/grixis/mana_timing/{slug}.json","blueprint":f"data/grixis/blueprints/{slug}.json","graph":f"data/grixis/graph/{slug}.json"},
        "utility_lands":utilities,"mdfcs":mdfcs,
        "commander_land_text_hooks":hooks,
        "land_type_context":{"typed_land_counts":own_type_counts,"commander_text_relevant_types":relevant_types,"blueprint_named_lands":named_lands,
                             "interpretation":"Commander Oracle land/type matches are textual hooks only; they may be opponent-facing or otherwise non-beneficial and require rules/strategic judgment."},
        "summary":{"utility_land_count":len(utilities),"mdfc_count":len(mdfcs),"utility_burden_flags":dict(sorted(burdens.items())),"utility_support_flags":dict(sorted(supports.items())),"blueprint_named_utility_lands":sum(u["blueprint_named"] for u in utilities),"commander_land_hook_count":sum(len(x["terms"]) for x in hooks)},
        "limitations":[
            "No universal opportunity-cost score is produced; color/timing burdens and strategic support signals stay separate.",
            "Blueprint exact-name mentions are Commander-first evidence, not automatic protections; absence is not evidence that a land lacks strategic value.",
            "Utility categories are Oracle-text heuristics and do not price the magnitude, activation cost, timing window or multiplayer value of the effect.",
            "Commander land/type matches are textual hooks only and can be opponent-facing (for example landwalk) or otherwise irrelevant to own mana-base construction.",
            "MDFCs are represented as spell/land option-value tradeoffs; later candidate optimization decides whether that flexibility is worth the tapped/color/slot cost.",
            "Graph package/identity signals are inherited accepted M4 evidence but do not decide a mana-base swap by themselves.",
        ]
    }


def build():
    reg=load(REGISTRY); db=mb.CardDB(); rows=[]; OUT.mkdir(parents=True,exist_ok=True)
    for did,e in sorted(reg["decks"].items(),key=lambda kv:kv[1]["slug"]):
        d=build_one(did,e,db); dump(OUT/f"{e['slug']}.json",d)
        rows.append({"deck_id":did,"slug":e["slug"],"utility_lands":d["summary"]["utility_land_count"],"mdfcs":d["summary"]["mdfc_count"],"blueprint_named_utility_lands":d["summary"]["blueprint_named_utility_lands"],"commander_land_hooks":d["summary"]["commander_land_hook_count"]})
    dump(OUT/"summary.json",{"schema_version":1,"generated_by":f"scripts/grixis_mana_opportunity.py v{VERSION}","decks":rows,"totals":{"decks":len(rows),"utility_lands":sum(x["utility_lands"] for x in rows),"mdfcs":sum(x["mdfcs"] for x in rows),"blueprint_named_utility_lands":sum(x["blueprint_named_utility_lands"] for x in rows),"commander_land_hooks":sum(x["commander_land_hooks"] for x in rows)}})
    print(f"mana-opportunity: built {len(rows)} decks; utility={sum(x['utility_lands'] for x in rows)} MDFC={sum(x['mdfcs'] for x in rows)}")


def check():
    try: import jsonschema
    except ImportError: print("mana-opportunity: jsonschema required"); return 1
    schema=load(SCHEMA); reg=load(REGISTRY); problems=[]; expected={e["slug"] for e in reg["decks"].values()}; present={p.stem for p in OUT.glob("*.json") if p.name!="summary.json"}
    if expected!=present: problems.append(f"coverage mismatch missing={sorted(expected-present)} extra={sorted(present-expected)}")
    for did,e in sorted(reg["decks"].items()):
        p=OUT/f"{e['slug']}.json"
        if not p.exists(): continue
        d=load(p)
        for err in jsonschema.Draft202012Validator(schema).iter_errors(d): problems.append(f"{e['slug']}: schema {list(err.path)}: {err.message}")
        if d["canonical_hash"]!=e["canonical_project_list"]["hash"]: problems.append(f"{e['slug']}: canonical hash drift")
        if d["authority"]["can_decide"] is not False: problems.append(f"{e['slug']}: opportunity record became decision-capable")
        if any("score" in k.lower() for k in d["summary"]): problems.append(f"{e['slug']}: synthetic universal score introduced")
        for u in d["utility_lands"]:
            if u["authority"]["can_decide"] is not False: problems.append(f"{e['slug']}: utility {u['card']} became decision-capable")
    print(f"mana-opportunity: {len(expected)} deck files, {len(problems)} problems")
    for p in problems[:50]: print("FAIL",p)
    return 1 if problems else 0


def main(argv=None):
    a=argparse.ArgumentParser(); a.add_argument("--build",action="store_true"); a.add_argument("--check",action="store_true"); a.add_argument("--summary",action="store_true"); x=a.parse_args(argv); rc=0
    if x.build: build()
    if x.check: rc|=check()
    if x.summary: print(json.dumps(load(OUT/"summary.json"),indent=2,sort_keys=True))
    if not (x.build or x.check or x.summary): a.print_help()
    return rc

if __name__=="__main__": sys.exit(main())
