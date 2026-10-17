#!/usr/bin/env python3
"""Cycle 90: prove other Step C mana outputs remain identical for 25 Mox decks.

Recompute timing/opportunity/resilience under current corrected classifier and
compare to frozen SHA-bound originals. Stop on ANY discrepancy. Never overwrite
historical evidence or change approved deck authority.
"""
from __future__ import annotations
import argparse,hashlib,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_mana_base as mb
import grixis_mana_timing as timing
import grixis_mana_opportunity as opportunity
import grixis_mana_resilience as resilience

REG=ROOT/"data/grixis/registry.json"
STATIC=ROOT/"data/grixis/m6/mox_reconciliation/static_manifest.json"
NOFAST=ROOT/"data/grixis/m6/mox_reconciliation/nofast_manifest.json"
OUT=ROOT/"data/grixis/m6/mox_reconciliation/dependency_proof.json"
MODULES={
    "mana_timing":(timing,lambda did,e,db:timing.build_one(did,e,db)),
    "mana_opportunity":(opportunity,lambda did,e,db:opportunity.build_one(did,e,db)),
    "mana_resilience":(resilience,lambda did,e,db:resilience.build_one(did,e)),
}
AUTH={"can_decide":False,"can_apply_swap":False,"can_approve_or_lock":False}

def load(p):return json.loads(p.read_text(encoding="utf-8"))
def sha(p):return "sha256:"+hashlib.sha256(p.read_bytes()).hexdigest()
def fmt(x):return json.dumps(x,indent=1,sort_keys=True,ensure_ascii=False)+"\n"

def compare():
    reg,static,nofast=load(REG),load(STATIC),load(NOFAST)
    if len(reg["decks"])!=62 or static["count"]!=25 or nofast["count"]!=25:
        raise ValueError("inventory/manifest mismatch")
    if reg["program"]["milestones"]["M5"]["status"]!="accepted" or reg["program"]["milestones"]["M6"].get("accepted_by") is not None:
        raise ValueError("accepted evidence authority drift")
    byslug={v["slug"]:(k,v) for k,v in reg["decks"].items()}
    db=mb.CardDB()
    rows=[]
    for row in static["rows"]:
        slug=row["slug"]
        did,entry=byslug[slug]
        checks={}
        for name,(module,run) in MODULES.items():
            old=ROOT/"data/grixis"/name/(slug+".json")
            if not old.exists():raise ValueError("historical missing: "+str(old))
            saved=load(old)
            current=run(did,entry,db)
            if saved!=current:
                def walk(a,b,p=""):
                    if isinstance(a,dict) and isinstance(b,dict):
                        return [j for k in sorted(set(a)|set(b)) for j in walk(a.get(k),b.get(k),p+"."+k)]
                    if isinstance(a,list) and isinstance(b,list) and len(a)==len(b):
                        return [j for i,(x,y) in enumerate(zip(a,b)) for j in walk(x,y,p+"."+str(i))]
                    return [] if a==b else [p]
                raise ValueError(slug+" "+name+" changed unexpectedly: "+repr(walk(saved,current)[:15]))
            if saved.get("canonical_hash")!=entry["canonical_project_list"]["hash"]:
                raise ValueError(slug+" "+name+" stale canonical hash")
            if saved.get("authority",{}).get("can_decide") is not False:
                raise ValueError(slug+" "+name+" decision-capable")
            checks[name]={"historical_sha256":sha(old),"recomputed_equal":True,
                          "changed_fields":0}
        rows.append({"slug":slug,"deck_id":did,"canonical_hash":entry["canonical_project_list"]["hash"],
                    "checks":checks})
        print(slug+": timing/opportunity/resilience exact replay",flush=True)
    if len(rows)!=25 or len({r["slug"] for r in rows})!=25:
        raise ValueError("reconciled coverage not 25")
    return {"schema_version":1,"stage":"M6_Chrome_Mox_secondary_Step_C_dependency_proof",
            "static_manifest_sha256":sha(STATIC),
            "corrected_nofast_manifest_sha256":sha(NOFAST),
            "decks":25,"modules":sorted(MODULES),
            "verified_existing_outputs":len(rows)*len(MODULES),
            "rows":rows,
            "conclusion":"25 affected decks: mana_timing, mana_opportunity, mana_resilience remain bit-for-bit equivalent after the classifier correction",
            "does_not_refresh":"mana_quality_gain and other historical summaries; no canonical or historic artifacts rewritten",
            "scope":"Structural dependency equivalence, not improved card win rate or deck approval",
            "authority":AUTH}

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--build",action="store_true")
    ap.add_argument("--check",action="store_true")
    opt=ap.parse_args()
    if not(opt.build or opt.check):ap.error("require --build/--check")
    d=compare();body=fmt(d)
    if opt.build:OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(body,encoding="utf-8")
    if opt.check and (not OUT.is_file() or OUT.read_text(encoding="utf-8")!=body):raise ValueError("dependency proof stale")
    print("SECONDARY DEPENDENCY PASS:",d["verified_existing_outputs"],"recomputed reports identical, no approvals")
