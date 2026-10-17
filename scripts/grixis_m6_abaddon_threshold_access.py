#!/usr/bin/env python3
"""Cycle 92: paired, preregistered Abaddon mana/access comparison; NO effect or upgrade claim.

M3 v1.1 does not model Heartless Hidetsugu or Tree of Perdition abilities.
This tool compares ONLY early commander tempo and mana in a fixed 99.
"""
from __future__ import annotations
import argparse,hashlib,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_authority as ga
import grixis_paired as paired
import grixis_sim as sim
import evaluate_decklist as ev
PLAN=ROOT/"data/grixis/m6/phase_b_plans/abaddon_threshold_access_01.json"
SOURCE=ROOT/"exports/grixis-archidekt/source-baseline/abaddon-the-despoiler.txt"
M5=ROOT/"data/grixis/m6/review_packets/abaddon-the-despoiler.json"
BLUEPRINT=ROOT/"data/grixis/blueprints/abaddon-the-despoiler.json"
OUT=ROOT/"data/grixis/m6/phase_b_bounded/abaddon_threshold_access_01.json"
AUTH={"can_decide":False,"can_apply_swap":False,"can_approve_or_lock":False}

def load(x):return json.loads(x.read_text(encoding="utf-8"))
def sha(x):return "sha256:"+hashlib.sha256(x.read_bytes()).hexdigest()
def fmt(x):return json.dumps(x,sort_keys=True,indent=1,ensure_ascii=False)+"\n"

def alternatives(plan,source,m5,blue):
    lines=ga.deck_block_text(plan["slug"]).splitlines()
    allnames=[line.split(" ",1)[-1].split(" [")[0].strip() for line in lines]
    if len(allnames)!=92: # number of physical lines includes nine basic lands, 99+commander quantities
        raise ValueError("Unexpected baseline physical-line count; verify source")
    if lines[0].split(" ",1)[-1].split(" [")[0]!="Abaddon the Despoiler":
        raise ValueError("commander identity changed")
    existing={x["swap_id"]:(x["cut"],x["add"]) for x in m5["items"]}
    core_enablers=set(next(p["cards"] for p in blue["packages"] if p["id"]=="pkg:threshold-enablers"))
    printed=set(next(p["cards"] for p in blue["packages"] if p["id"]=="pkg:cascade-spells"))
    variants=[]
    for x in plan["targeted"]:
        a,b=x["add"],x["cut"]
        if a in allnames or allnames.count(b)!=1:
            raise ValueError("missing baseline cut or duplicate add: "+a+" / "+b)
        if x["existing_m5_id"] is not None and existing.get(x["existing_m5_id"])!=(b,a):
            raise ValueError("registered M5 source swap mismatch")
        if x["existing_m5_id"] is None:
            if b!="Bituminous Blast" or len(printed-set([b]))<4:
                raise ValueError("alternative cut violates printed cascade blueprint")
        replaced=[line if i!=allnames.index(b) else "1 "+a for i,line in enumerate(lines)]
        challenger="\n".join(replaced)+"\n"
        variants.append((x,challenger,{"removed_core_threshold":b in core_enablers,
                                         "printed_cascade_after_cut":len(printed-set([b]))}))
    return variants

def run():
    plan,packet,blue=load(PLAN),load(M5),load(BLUEPRINT)
    if plan["status"]!="registered_before_test" or plan["model"]!=sim.VERSION or plan["samples"]!=600 or plan["seed"]!=92017:
        raise ValueError("precommitted test parameters drift")
    if plan["canonical_hash"]!=packet["list_hash"] or plan["canonical_hash"]!=blue["canonical_hash"]:
        raise ValueError("canonical/source identity mismatch")
    reg=load(ROOT/"data/grixis/registry.json")
    if reg["program"]["milestones"]["M5"]["status"]!="accepted" or reg["program"]["milestones"]["M6"].get("accepted_by") is not None:
        raise ValueError("M5/M6 authority mismatch")
    v=alternatives(plan,SOURCE,packet,blue)
    resolver=ev.Resolver()
    original=sim.load_deck(plan["slug"],resolver)
    if original.N!=99:raise ValueError("not a 99-card source library")
    output=[]
    for i,(candidate,source,roles) in enumerate(v):
        change=sim.load_deck(plan["slug"],resolver,text=source)
        if change.N!=99:raise ValueError("not 99 card challenger: "+str(i))
        scores,pairs=paired.paired(original,change,plan["samples"],plan["seed"],plan["turns"],
                                   pairs=[(candidate["cut"],candidate["add"])],model=plan["model"])
        if pairs!=[(candidate["cut"],candidate["add"])]:
            raise ValueError("unregistered paired swap")
        score={s["metric"]:s for s in scores}
        if not all(e in score for e in plan["endpoint_set"]):
            raise ValueError("paired requested metric missing")
        coverage=paired.coverage(original,change,pairs,plan["model"])
        if not any(candidate["add"]+" [no effect modelled beyond being a castable card]" in s for s in coverage):
            raise ValueError("new capability modeled; must re-register before conclusions")
        output.append({"add":candidate["add"],"cut":candidate["cut"],
             "registered_m5_id":candidate["existing_m5_id"],
             "cut_class":candidate["tag"],"roles":roles,
             "metric_results":[score[m] for m in plan["endpoint_set"]],
             "coverage":coverage,
             "effect_aware_threshold_test_executed":False,
             "supports_improvement_claim":False})
        print("paired mana-only",i+1,"/",len(v),candidate["add"],"vs",candidate["cut"],flush=True)
    if len(output)!=6:raise ValueError("six hypotheses not evaluated")
    return {"schema_version":1,"stage":"M6_Abaddon_threshold_mana_only_paired",
      "deck_id":plan["deck_id"],"slug":plan["slug"],"canonical_hash":plan["canonical_hash"],
      "preregistration_sha256":sha(PLAN),"m5_review_packet_sha256":sha(M5),
      "blueprint_sha256":sha(BLUEPRINT),"baseline_export_sha256":sha(SOURCE),
      "simulator_sha256":sim.model_sha256(),
      "samples":plan["samples"],"seed":plan["seed"],"model":plan["model"],"turns":plan["turns"],
      "alternatives":output,
      "limits":["Mana and early commander access ONLY; both Heartless and Tree active effects unmodeled",
                "Also missing Birgi mana-on-cast, Kessig ping and Bituminous Blast cascade effects",
                "Fixed-shuffle goldfish has no interaction/summoning-sickness/survival policy",
                "The alternate printed-cascade cut is not a recommended cut",
                "True effect-aware comparison and mana/stack/opponent review remain unexecuted"],
      "full_phase_b_complete":False,"supports_improvement_claim":False,
      "authority":AUTH}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--build",action="store_true")
    ap.add_argument("--check",action="store_true")
    args=ap.parse_args()
    if not(args.build or args.check):ap.error("require --build/--check")
    d=run()
    text=fmt(d)
    if args.build:OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(text,encoding="utf-8")
    if args.check and (not OUT.exists() or OUT.read_text(encoding="utf-8")!=text):
        raise ValueError("paired mana evidence mismatch")
    print("DONE 6 mana-only swap hypotheses; zero threshold effect models, zero approvals")
if __name__=="__main__":main()
