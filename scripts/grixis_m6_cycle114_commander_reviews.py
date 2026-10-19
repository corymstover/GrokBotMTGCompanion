#!/usr/bin/env python3
"""Cycle114: verify 3 authored commander-first reviews on exact source decks.
No approval, legality certification, end-to-end play, or independent Pass C.
"""
from __future__ import annotations
import argparse,hashlib,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import evaluate_decklist as ev
import grixis_sim as sim
PLAN=ROOT/"data/grixis/m6/phase_b_plans/cycle114_commander_reviews_01.json"
REV=ROOT/"data/grixis/m6/author_reviews/cycle114_three_commander_reviews_01.json"
REG=ROOT/"data/grixis/registry.json"
TRIAGE=ROOT/"data/grixis/m6/phase_b_bounded/commander_first_readiness_62_01.json"
OUT=ROOT/"data/grixis/m6/phase_b_bounded/cycle114_sourced_review_validation_01.json"
AUTH={"can_change_decklists":False,"can_approve_or_lock":False,"can_decide":False,"can_certify_M6":False}
EXP={
 "Inalla__Archmage_Ritualist":("inalla-archmage-ritualist","Inalla, Archmage Ritualist","Pitiless Plunderer","Blood Pet","swap:inalla-archmage-ritualist:m5:217e55a1ecd0","81333ac71d483b667af968bf2ab221e1fa0de6edd7c2395170d15786e5b15fa3","HOLD_EXISTING_LIST_NO_SWAP"),
 "The_Rani":("the-rani","The Rani","Drafna, Founder of Lat-Nam","Curse of Opulence","swap:the-rani:m5:225ed1a7c9c4","7220937ed5817b4ef9cacd2463a3434b98ae58690ffa1d7ef440881ba97d729c","HOLD_EXISTING_LIST_NO_SWAP"),
 "Nicol_Bolas__the_Ravager":("nicol-bolas-the-ravager","Nicol Bolas, the Ravager // Nicol Bolas, the Arisen","Aetheric Amplifier","Mox Diamond","swap:nicol-bolas-the-ravager:m5:14aef623f1e4","5a5fff7dcea61a8e1e0b5ea6da41f6158033bbd899088d7e6abbe6b7c52fb63e","PROMISING_UNRESOLVED_DIFFERENT_CUT_NEEDED")
}
ORACLE={
 "Inalla, Archmage Ritualist":["eminence","nontoken wizard","tap five untapped wizards"],
 "Pitiless Plunderer":["another creature you control dies","create a treasure token"],
 "Blood Pet":["sacrifice","add {b}"],
 "The Rani":["mark of the rani","goaded","investigate"],
 "Drafna, Founder of Lat-Nam":["return target artifact you control","copy target artifact spell you control"],
 "Curse of Opulence":["enchant player","whenever enchanted player is attacked","create a gold token"],
 "Academy Manufactor":["clue","food","treasure"],
 "Nicol Bolas, the Ravager // Nicol Bolas, the Arisen":["when nicol bolas enters","exile nicol bolas","return him to the battlefield transformed","+2: draw two cards"],
 "Aetheric Amplifier":["add one mana of any color","double the number of each kind of counter on target permanent","activate only as a sorcery"],
 "Mox Diamond":["discard a land card","add one mana of any color"],
 "Training Grounds":["activated abilities","cost {2} less"],
 "Bloodline Necromancer":["wizard"],
 "Spellseeker":["search your library"],
 "The Chain Veil":["activate a loyalty ability"]
}
def read(p):return json.loads(p.read_text(encoding="utf-8"))
def sha(p):return "sha256:"+hashlib.sha256(p.read_bytes()).hexdigest()
def encode(x):return json.dumps(x,sort_keys=True,ensure_ascii=False,indent=2)+"\n"
def oracle(res):
 result={}
 for name,phrases in ORACLE.items():
  card=res.get(name)[0]
  txt=card.get("oracle_text") or "\n".join((face.get("oracle_text") or "") for face in card.get("card_faces",[]))
  if card.get("name")!=name or not txt:
   raise ValueError("Archived Oracle card identity missing: "+name)
  if any(s.casefold() not in txt.casefold() for s in phrases):
   raise ValueError("Archived Oracle mechanic mismatch for "+name+": "+repr(txt))
  result[name]={"oracle_sha256":"sha256:"+hashlib.sha256(txt.encode()).hexdigest(),"type_line":card.get("type_line"),
    "mana_cost":card.get("mana_cost"),"frozen_snapshot_not_live_current_legality":True}
 return result
def validate(item,plan,reg,bp,queue,lib,oracle_cards):
 did=item["deck_id"]
 slug,cmd,add,cut,swap,approved,outcome=EXP[did]
 if (item["slug"]!=slug or item["commander"]!=cmd or item["approved_sha256"]!=approved or
    item["swap_id"]!=swap or item["add"]!=add or item["cut"]!=cut or item["disposition"]!=outcome or
    plan["slug"]!=slug or plan["deck_id"]!=did or plan["source_swap_id"]!=swap or
    plan["approved_raw_sha256"]!=approved or plan["add"]!=add or plan["cut"]!=cut or
    reg["deck_id"]!=did or reg["slug"]!=slug or reg["commanders"]!=[cmd] or
    reg["source"]["recorded_sha256"]!=approved or reg["source"]["recorded_matches_raw"] is not True or
    bp["deck_id"]!=did or bp["canonical_hash"]!=reg["current_canonical_hash"] or
    queue["source_canonical_logical_hash"]!=reg["current_canonical_hash"]):
  raise ValueError("Named candidate, approved hash or source commander drift: "+did)
 if len(lib.library)!=99 or len(lib.commanders)!=1 or lib.commanders[0]["name"]!=cmd:
  raise ValueError("Approved 99+1 physical list was not reconstructed: "+did)
 names=[card["name"] for card in lib.library]
 if names.count(cut)!=1 or add in names:
  raise ValueError("Canonical cut/add presence does not match original source: "+did)
 actual_core={c["card"] for c in bp["identity_core"]}
 if cmd not in actual_core or any(c!=cmd and c not in names for c in actual_core):
  raise ValueError("Blueprint commander identity package missing from source: "+did)
 source_match=[x for x in queue["first_three_TO_REVIEW_NOT_TO_APPLY"] if x["swap_id"]==swap]
 if len(source_match)!=1 or source_match[0]["add"]!=add or source_match[0]["cut"]!=cut:
  raise ValueError("Cycle111 exact source M5 candidate provenance missing: "+did)
 if "test_pass" not in source_match[0]["M5_flags"]:
  raise ValueError("Source M5 screening gate drift")
 if add not in oracle_cards or cut not in oracle_cards or cmd not in oracle_cards:
  raise ValueError("No frozen Oracle for investigated change")
 if item["swap_applied"] or item["full_phase_b_complete"] or item["official_current_legality_certified"]:
  raise ValueError("Author judgment has no approved swap or full Phase B authority")
 if len(item["rules"])<4 or not item["why_hold"] or not item["positive_case"] or not item["next_gate"]:
  raise ValueError("Commander-first review not substantive enough")
 if did=="The_Rani":
  if "Curse of Opulence" not in names:raise ValueError("Rani lost Curse source")
  if "Academy Manufactor" not in names:raise ValueError("Rani Clue payoff missing")
 if did=="Nicol_Bolas__the_Ravager" and not {"Training Grounds","The Chain Veil","Deepglow Skate"}.issubset(set(names)):
  raise ValueError("Bolas superfriends commander-centric package missing")
 if did=="Inalla__Archmage_Ritualist" and not {"Spellseeker","Scholar of the Ages","Bloodline Necromancer"}.issubset(set(names)):
  raise ValueError("Inalla Wizard commander package missing")
 return {"deck_id":did,"commander":cmd,"approved_raw_sha256":approved,
  "blueprint_sha256":sha(ROOT/"data/grixis/blueprints"/(slug+".json")),
  "actual_main_library_cards":99,"commander_count":1,
  "source_M5_swap_id":swap,"source_M5_test_pass_not_card_effect_test":True,
  "approved_cut_present":True,"candidate_add_absent":True,
  "source_blueprint_core_preserved":True,"author_disposition":outcome,
  "effect_aware_phase_b_complete":False,"independent_pass_c_complete":False,
  "zero_improvement_certified":False,"card_swap_applied":False}
def run():
 p=read(PLAN);r=read(REV);reg=read(REG);triage=read(TRIAGE)
 if (p["cycle"]!=114 or p["status"]!="preregistered_before_author_reviews" or
   p["authority"]!=AUTH or r["authority"]!=AUTH or r["cycle"]!=114 or r["review_count"]!=3 or
   len(r["reviews"])!=3 or len(reg["decks"])!=62 or
   reg["program"]["milestones"]["M6"]["status"]!="in_progress" or
   reg["program"]["milestones"]["M6"]["accepted_by"] is not None or
   set(x["deck_id"] for x in r["reviews"])!=set(EXP)):
  raise ValueError("Cycle114 fixed source/authority review baseline changed")
 res=ev.Resolver()
 checks=oracle(res)
 queues={x["deck_id"]:x for x in triage["ordered_decks"]}
 rows=[]
 for item in r["reviews"]:
  did=item["deck_id"];slug=EXP[did][0]
  bp=read(ROOT/"data/grixis/blueprints"/(slug+".json"))
  lib=sim.load_deck(slug,res)
  pp=next((x for x in p["candidates"] if x["deck_id"]==did),None)
  if pp is None:raise ValueError("Unexpected unpreregistered deck")
  rows.append(validate(item,pp,reg["decks"][did],bp,queues[did],lib,checks))
 return {"cycle":114,"schema_version":1,"plan_sha256":sha(PLAN),"review_sha256":sha(REV),
   "registry_sha256":sha(REG),"Cycle111_readiness_sha256":sha(TRIAGE),
   "oracle_checked":checks,"source_verified_deck_count":3,
   "reviewed_decks":rows,"author_review_count":3,"formal_independent_Pass_C_count":0,
   "full_effect_aware_phase_B_count":0,"canonical_decks_modified":0,
   "swaps_approved_or_applied":0,"current_official_legality_reverified":False,
   "M6_accepted":False,"authority":AUTH}
def main():
 p=argparse.ArgumentParser();p.add_argument("--build",action="store_true");p.add_argument("--check",action="store_true")
 args=p.parse_args()
 if not(args.build or args.check):p.error("use --build or --check")
 result=run();txt=encode(result)
 if args.build:
  OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(txt,encoding="utf-8")
 if args.check and (not OUT.is_file() or OUT.read_text(encoding="utf-8")!=txt):
  raise ValueError("Cycle114 source replay is not deterministic")
 print("Cycle114 three source-verified commander-first author reviews; no independent certification",flush=True)
if __name__=="__main__":main()
