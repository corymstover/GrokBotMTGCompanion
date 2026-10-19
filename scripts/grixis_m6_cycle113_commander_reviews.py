#!/usr/bin/env python3
"""Cycle113 3-source commander-first author review verification.

Checks all 99+1 source-deck models, proposed add absent / cut present, actual
plan + identity core + M5 original candidate IDs, frozen Oracle mechanics,
special Nazgul official deck construction text, and prior Cycle112 source
review distinction. No full-game performance or approval conclusions.
"""
import argparse,hashlib,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import evaluate_decklist as ev
import grixis_sim as sim

PLAN=ROOT/"data/grixis/m6/phase_b_plans/cycle113_commander_reviews_01.json"
REV=ROOT/"data/grixis/m6/author_reviews/cycle113_three_commander_review_01.json"
REG=ROOT/"data/grixis/registry.json"
TRIAGE=ROOT/"data/grixis/m6/phase_b_bounded/commander_first_readiness_62_01.json"
PREVIOUS=ROOT/"data/grixis/m6/author_reviews/cycle112_three_commander_authored_judgments_01.json"
OUT=ROOT/"data/grixis/m6/phase_b_bounded/cycle113_sourced_review_validation_01.json"
AUTH={"can_change_decklists":False,"can_approve_or_lock":False,"can_decide":False,"can_certify_M6":False}

ORACLE={
 "Kefka, Court Mage // Kefka, Ruler of Ruin":("each player discards a card","card type","whenever an opponent loses life during your turn"),
 "Hullbreaker Horror":("whenever you cast a spell","return target","nonland permanent"),
 "Orcish Bowmasters":("flash","whenever an opponent draws a card","amass orcs 1"),
 "Sauron, Lord of the Rings":("when you cast this spell","amass orcs 5","mill five cards","return a creature card"),
 "Aggravated Assault":("untap all creatures you control","additional combat phase","activate only as a sorcery"),
 "Mystic Remora":("cumulative upkeep","noncreature spell"),
 "Nazgûl":("up to nine","ring tempts you"),
 "Nathan Drake, Treasure Hunter":("whenever nathan drake attacks","you may cast a spell from among those cards"),
 "Godo, Bandit Warlord":("when godo enters","all samurai you control","additional combat phase"),
 "Vampiric Tutor":("search your library for a card","put that card on top","lose 2 life"),
 "Aphetto Alchemist":("untap target artifact or creature",),
 "Illusionist's Bracers":("ability of equipped creature","copy that ability"),
 "Gwendlyn Di Corci":("discards a card at random","activate only during your turn"),
 "Pemmin's Aura":("shroud","untap enchanted creature")
}
EXPECTED={
 "Kefka__Court_Mage":("kefka-court-mage","Kefka, Court Mage // Kefka, Ruler of Ruin",
   "Hullbreaker Horror","Orcish Bowmasters","swap:kefka-court-mage:m5:576cc2cc3744",
   "cd36192fedda7a4f54570fb8b8e4605147b40f9254e6985729097fc998f17b03"),
 "Sauron__Lord_of_the_Rings":("sauron-lord-of-the-rings","Sauron, Lord of the Rings",
   "Aggravated Assault","Mystic Remora","swap:sauron-lord-of-the-rings:m5:31ef2948da79",
   "72a814e6ae1153507c9c1469a7792043b2e5c055d9e5fcd9f6cfcf7781e287b0"),
 "Nathan_Drake__Treasure_Hunter":("nathan-drake-treasure-hunter","Nathan Drake, Treasure Hunter",
   "Godo, Bandit Warlord","Vampiric Tutor","swap:nathan-drake-treasure-hunter:m5:79373d803b78",
   "a5d59afc3a78d7ff6454b1d011c82c2f732e11f4d4dd03256df1195a3abe9ba0")
}
def read(p):return json.loads(p.read_text(encoding="utf-8"))
def digest(p):return "sha256:"+hashlib.sha256(p.read_bytes()).hexdigest()
def to_json(a):return json.dumps(a,sort_keys=True,indent=2,ensure_ascii=False)+"\n"

def verify_oracle(res):
 found={}
 for name,words in ORACLE.items():
  record=res.get(name)[0]
  txt=record.get("oracle_text") or "\\n".join(
   f.get("oracle_text") or "" for f in record.get("card_faces",[]))
  if record.get("name")!=name or not txt or any(w.casefold() not in txt.casefold() for w in words):
   raise ValueError("Source-locked Oracle ability changed: "+name+" "+repr(txt))
  found[name]={"oracle_sha256":"sha256:"+hashlib.sha256(txt.encode()).hexdigest(),
    "mana_cost":record.get("mana_cost"),"type_line":record.get("type_line"),
    "as_of_frozen_archive_not_current_legality":True}
 return found

def verify_deck(r,plan,metadata,blueprint,deck,triage,oracle):
 did=r["deck_id"]
 slug,name,add,cut,swap,sha=EXPECTED[did]
 if (r["slug"]!=slug or metadata["deck_id"]!=did or metadata["slug"]!=slug or
     plan["deck_id"]!=did or r["commander"]!=name or
     metadata["commanders"]!=[name] or
     r["approved_raw_sha256"]!=sha or
     metadata["source"]["recorded_sha256"]!=sha or
     not metadata["source"]["recorded_matches_raw"] or
     blueprint["canonical_hash"]!=metadata["current_canonical_hash"] or
     triage["source_canonical_logical_hash"]!=metadata["current_canonical_hash"] or
     r["add"]!=add or r["cut"]!=cut or r["m5_swap_id"]!=swap or
     plan["source_swap_id"]!=swap or plan["add"]!=add or plan["cut"]!=cut):
  raise ValueError("Cross-source approved hash or named original M5 swap mismatch "+did)
 if (len(deck.library)!=99 or len(deck.commanders)!=1 or
   deck.commanders[0]["name"]!=name):
  raise ValueError("Source physical library not 99+1 "+did)
 names=[x["name"] for x in deck.library]
 if add in names or cut not in names:
  raise ValueError("Original approved cut absent or add already approved "+did)
 if any(v["card"] not in names and v["card"]!=name for v in blueprint["identity_core"]):
  raise ValueError("Identity core package not in approved original 100 "+did)
 source_item=next((v for v in triage["first_three_TO_REVIEW_NOT_TO_APPLY"]
   if v["swap_id"]==swap),None)
 if source_item is None or (source_item["add"],source_item["cut"])!=(add,cut):
  raise ValueError("Cycle111 top-three audit omitted named real M5 hypothesis "+did)
 if source_item["M5_priority_class"]!="P0_independent_agreement" or (
    "test_pass" not in source_item["M5_flags"]):
  raise ValueError("M5 exploratory source flags incorrectly represented "+did)
 if (r["disposition"]!="HOLD_EXISTING_LIST_NO_SWAP" or
     not r["rules"] or len(r["rules"])<4 or
     not r["next_evidence"] or not r["why"] or r["proposed_change_approved"]):
  raise ValueError("Card-level author judgment improperly promoted or missing "+did)
 if (add not in oracle or cut not in oracle or name not in oracle):
  raise ValueError("Unverified declared Oracle key")
 if did=="Sauron__Lord_of_the_Rings":
  if names.count("Nazgûl")!=4 or not metadata["project_exceptions"]:
   raise ValueError("Registered four official-ability Nazgul deck rule lost")
 if did=="Nathan_Drake__Treasure_Hunter":
  if "Godo, Bandit Warlord" in names:
   raise ValueError("No candidate Godo should appear in existing approved source")
  for equipment in ("Lightning Greaves","Swiftfoot Boots","Brotherhood Regalia","Dream-Thief's Bandana"):
   if equipment not in names:raise ValueError("Existing Godo Equipment hit assumption drift")
 return {"deck_id":did,"commander":name,"approved_sha256":sha,
   "blueprint_sha256":digest(ROOT/"data/grixis/blueprints"/(slug+".json")),
   "source_M5_review_swap_id":swap,"source_P0_agreement_not_an_approval":True,
   "actual_main_cards":len(deck.library),"actual_commanders":len(deck.commanders),
   "proposed_add_absent":add not in names,"proposed_cut_present":cut in names,
   "commander_blueprint_required_core_preserved":True,
   "commander_specific_source_review":"HOLD_EXISTING_LIST_NO_SWAP",
   "independent_Pass_C_completed":False,"actual_opponent_game_simulation_completed":False,
   "canonical_deck_changed":False,"tested_pool_zero_improvement_certified":False}

def build():
 p=read(PLAN);a=read(REV);reg=read(REG);old=read(PREVIOUS);triage=read(TRIAGE)
 if (p["cycle"]!=113 or p["authority"]!=AUTH or
     p["status"]!="preregistered_before_authored_review" or
     a["cycle"]!=113 or a["source_new_deck_count"]!=3 or
     a["existing_locked_lists_changed"]!=0 or len(reg["decks"])!=62 or
     reg["program"]["milestones"]["M6"]["status"]!="in_progress" or
     reg["program"]["milestones"]["M6"]["accepted_by"] is not None or
     len(a["reviews"])!=3 or set(x["deck_id"] for x in a["reviews"])!=set(EXPECTED) or
     len(p["new_reviews"])!=3 or old["cycle"]!=112 or
     old["review_count"]!=3 or not a["retrospective"]["Gwendlyn"].startswith("Cycle112")):
  raise ValueError("Cycle113 source authority/regression or retrospective provenance drift")
 oracle=verify_oracle(ev.Resolver())
 resolver=ev.Resolver()
 triage_rows={x["deck_id"]:x for x in triage["ordered_decks"]}
 rows=[]
 for row in a["reviews"]:
  did=row["deck_id"];slug=EXPECTED[did][0]
  blueprint=read(ROOT/"data/grixis/blueprints"/(slug+".json"))
  library=sim.load_deck(slug,resolver)
  meta=reg["decks"][did]
  rows.append(verify_deck(row,next(x for x in p["new_reviews"] if x["deck_id"]==did),
    meta,blueprint,library,triage_rows[did],oracle))
 if ("Aphetto Alchemist" not in oracle or "Illusionist's Bracers" not in oracle or
    not a["retrospective"]["Gwendlyn"].find("unbounded untap")>=0):
  raise ValueError("Skeptical Alchemist and Bracers engine must remain explicit")
 return {"schema_version":1,"cycle":113,"plan_sha256":digest(PLAN),
  "authored_reviews_sha256":digest(REV),"source_registry_sha256":digest(REG),
  "cycle111_triage_sha256":digest(TRIAGE),"cycle112_prior_sha256":digest(PREVIOUS),
  "verified_frozen_oracle_records":oracle,"new_source_verified_decks":rows,
  "new_commander_author_reviews_count":3,
  "adversarial_cycle112_reassessment_count":3,
  "real_independent_reviewers_not_claimed":True,
  "formal_independent_Pass_C_reviews_completed":0,
  "effect_aware_balanced_phase_B_completed":0,
  "official_current_legality_reverified":False,
  "reviewed_holds_do_not_certify_all_candidate_pools":True,
  "approved_decks_modified":0,"new_owner_approvals":0,"M6_accepted":False,
  "authority":AUTH}
def main():
 z=argparse.ArgumentParser()
 z.add_argument("--build",action="store_true");z.add_argument("--check",action="store_true")
 args=z.parse_args()
 if not (args.build or args.check):z.error("--build or --check needed")
 data=build();txt=to_json(data)
 if args.build:
  OUT.parent.mkdir(parents=True,exist_ok=True)
  OUT.write_text(txt,encoding="utf-8")
 if args.check and (not OUT.exists() or OUT.read_text(encoding="utf-8")!=txt):
  raise ValueError("Source Oracle review validation not deterministic")
 print("Cycle113: verified",len(data["new_source_verified_decks"]),
   "source-locked commander holds; no Phase B/independence/approved swap",flush=True)
if __name__=="__main__":main()
