#!/usr/bin/env python3
"""Audit static conditional Chrome Mox detection without editing existing deck evidence."""
import argparse,hashlib,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_mana_base as mana
OUT=ROOT/"data/grixis/m6/classifier_corrections/chrome_mox.json"
def load(p): return json.loads(p.read_text())
def digest(p): return "sha256:"+hashlib.sha256(p.read_bytes()).hexdigest()
def calculate():
    reg=load(ROOT/"data/grixis/registry.json")
    assert len(reg["decks"])==62 and reg["program"]["milestones"]["M5"]["status"]=="accepted"
    assert reg["program"]["milestones"]["M6"]["accepted_by"] is None
    c=mana.classify(mana.CardDB().get("Chrome Mox"),set("UBR"))
    assert c["fast_mana"] and c["conditional_source"] and c["imprint_dependent_mana"]
    assert c["source_colors"]=="UBR"
    affected=[]
    for did,e in sorted(reg["decks"].items()):
        src=ROOT/e["canonical_project_list"]["export"]
        n=sum(q for z,q,name in mana.parse_export(src) if z=="main" and name=="Chrome Mox")
        if not n: continue
        assert n==1
        old=ROOT/"data/grixis/mana_base"/(e["slug"]+".json")
        stat=load(old)
        assert stat["canonical_hash"]==e["canonical_project_list"]["hash"]
        affected.append({"deck_id":did,"slug":e["slug"],"canonical_hash":stat["canonical_hash"],
          "frozen_step_c_sha256":digest(old),"source_export_sha256":digest(src),
          "historically_omitted":"Chrome Mox" not in stat["fast_mana_cards"]})
    if not affected: raise ValueError("No Chrome Mox decks found")
    return {"schema_version":1,"stage":"M6_Chrome_Mox_conditional_fast_mana_audit",
      "decks_examined":62,"affected_decks":affected,"affected_count":len(affected),
      "historical_omissions":sum(x["historically_omitted"] for x in affected),
      "classifier_sha256":digest(ROOT/"scripts/grixis_mana_base.py"),
      "classification":"conditionally available colored fast mana (imprint required)",
      "downstream_status":"Step C and commander_mana derived data require scoped review",
      "authority":{"can_decide":False,"can_approve_or_lock":False,"can_apply_swap":False}}
def show(o): return json.dumps(o,sort_keys=True,indent=1)+"\n"
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--build",action="store_true");ap.add_argument("--check",action="store_true");a=ap.parse_args()
    if not a.build and not a.check: ap.error("need --build or --check")
    d=calculate()
    if a.build: OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(show(d))
    if a.check and (not OUT.exists() or OUT.read_text()!=show(d)): raise ValueError("audit drift")
    print("Chrome Mox classification correction:",d["historical_omissions"],"historical omissions /",d["affected_count"],"decks")
if __name__=="__main__": main()
