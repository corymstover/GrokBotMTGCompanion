#!/usr/bin/env python3
"""Cycle112: verify three AUTHOR commander-first strategic judgments against
locked-source fingerprints, complete M6 packet/blueprint, and pinned Oracle.
No independent external review, real-game test, M6 or decklist authority.
"""
from __future__ import annotations
import argparse,hashlib,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_sim as sim
import evaluate_decklist as ev
PLAN=ROOT/"data/grixis/m6/phase_b_plans/cycle112_commander_review_batch_01.json"
REVIEWS=ROOT/"data/grixis/m6/author_reviews/cycle112_three_commander_authored_judgments_01.json"
REG=ROOT/"data/grixis/registry.json"
OUT=ROOT/"data/grixis/m6/phase_b_bounded/cycle112_commander_first_reviews_01.json"
AUTH={"can_change_decklists":False,"can_approve_or_lock":False,"can_decide":False,"can_certify_M6":False}
KEYS={
 "Cormela__Glamour_Thief":{"cmd":"Cormela, Glamour Thief","add":"Archaeomancer","cut":"Faithless Looting",
  "disposition":"HOLD_EXISTING_LIST_NO_SWAP"},
 "Ashnod_the_Uncaring":{"cmd":"Ashnod the Uncaring","add":"Detective's Satchel","cut":"Dockside Chef",
  "disposition":"HOLD_EXISTING_LIST_NO_SWAP"},
 "Gwendlyn_Di_Corci":{"cmd":"Gwendlyn Di Corci","add":"Aphetto Alchemist","cut":"Opposition Agent",
  "disposition":"PROMISING_UNRESOLVED_REQUIRES_TARGETED_EVIDENCE"}
}
ORACLE={
 "Cormela, Glamour Thief":["haste","spend this mana only","when cormela dies"],
 "Archaeomancer":["return target instant or sorcery card from your graveyard to your hand"],
 "Faithless Looting":["draw two cards, then discard two cards","flashback"],
 "Ashnod the Uncaring":["isn't a mana ability","permanents were sacrificed to activate it"],
 "Detective's Satchel":["investigate twice","create a 1/1 colorless thopter","sacrificed an artifact this turn"],
 "Dockside Chef":["sacrifice an artifact or creature","draw a card"],
 "Gwendlyn Di Corci":["target player discards a card at random","activate only during your turn"],
 "Aphetto Alchemist":["untap target artifact or creature"],
 "Opposition Agent":["flash","you control your opponents while they're searching their libraries"],
 "Illusionist's Bracers":["whenever an ability of equipped creature is activated","copy that ability"],
 "Pemmin's Aura":["shroud","untap enchanted creature"]
}
def read(p):return json.loads(p.read_text(encoding="utf-8"))
def sha(p):return "sha256:"+hashlib.sha256(p.read_bytes()).hexdigest()
def dump(o):return json.dumps(o,indent=2,sort_keys=True,ensure_ascii=False)+"\n"
def oracle_gate(resolver):
  found={}
  for name,clauses in ORACLE.items():
   card=resolver.get(name)[0]
   if card.get("name")!=name or not card.get("oracle_text"):
    raise ValueError("Frozen Oracle name/text missing: "+name)
   text=card["oracle_text"].casefold()
   if any(needle.casefold() not in text for needle in clauses):
    raise ValueError("Archived Oracle core mechanic drift: "+name+" "+repr(card["oracle_text"]))
   found[name]={"oracle_sha256":"sha256:"+hashlib.sha256(card["oracle_text"].encode()).hexdigest(),
     "printed_mana_cost":card.get("mana_cost"),"type_line":card.get("type_line"),
     "snapshot_legality_claim_not_current":True}
  return found
def validate_review(item,plan_item,registry,blueprint,packet,library,oracle):
  did=item["deck_id"];meta=KEYS[did]
  if (item["slug"]!=registry["slug"] or
      registry["deck_id"]!=did or blueprint["deck_id"]!=did or packet["deck_id"]!=did or
      blueprint["slug"]!=item["slug"] or packet["slug"]!=item["slug"]):
   raise ValueError("Deck ID/slug misaligned in authored review "+did)
  if (registry["source"]["recorded_sha256"]!=item["approved_raw_sha256"] or
      registry["source"]["recorded_matches_raw"] is not True or
      registry["current_canonical_hash"]!=blueprint["canonical_hash"] or
      registry["current_canonical_hash"]!=packet["list_hash"]):
   raise ValueError("Approved deck source/blueprint hash mismatch "+did)
  if (item["add"]!=meta["add"] or item["cut"]!=meta["cut"] or
      item["commander"]!=meta["cmd"] or item["disposition"]!=meta["disposition"] or
      plan_item["deck_id"]!=did or plan_item["primary_proposal"]!={"add":item["add"],"cut":item["cut"]}):
   raise ValueError("Unauthorized changed hypothetical swap/disposition "+did)
  if (len(library.library)!=99 or len(library.commanders)!=1 or
      library.commanders[0]["name"]!=meta["cmd"]):
   raise ValueError("Missing approved source 99-card main/commander "+did)
  names={c["name"] for c in library.library}
  if item["cut"] not in names or item["add"] in names:
   raise ValueError("Original slot absent or unapproved card already present "+did)
  swaps=[x for x in packet["items"] if x["swap_id"]==item["m5_swap_id"]]
  if len(swaps)!=1 or swaps[0]["add"]!=item["add"] or swaps[0]["cut"]!=item["cut"]:
   raise ValueError("Named M5 candidate not in correct deep-review packet "+did)
  if (swaps[0]["priority_class"]!="P0_independent_agreement" or
      not set(["combo_review_required","test_pass"]).issubset(swaps[0]["flags"])):
   raise ValueError("M5 agreement source flags changed "+did)
  if (swaps[0]["candidate"]["screening_can_decide"] is not False or
      swaps[0]["authority"]["can_apply_swap"] is not False):
   raise ValueError("M5 candidate screening illegally promoted to approval")
  bp_core=[x["card"] for x in blueprint["identity_core"]]
  if meta["cmd"] not in bp_core:
   raise ValueError("Source blueprint did not identify its own commander")
  if any(not item.get(k) for k in ["commander_specific_rules","existing_strategic_role",
    "added_strategic_role","why_no_change","missing_evidence","next_action"]):
   raise ValueError("Substantive commander-first author review omitted "+did)
  for k in ("Archaeomancer","Faithless Looting") if did=="Cormela__Glamour_Thief" else (
      ("Detective's Satchel","Dockside Chef") if did=="Ashnod_the_Uncaring" else
      ("Aphetto Alchemist","Opposition Agent","Illusionist's Bracers","Pemmin's Aura")):
   if k not in oracle:raise ValueError("Missing frozen Oracle checked mechanism")
  return {"deck_id":did,"commander":meta["cmd"],"approved_raw_sha256":item["approved_raw_sha256"],
    "blueprint_sha256":sha(ROOT/"data/grixis/blueprints"/(item["slug"]+".json")),
    "packet_sha256":sha(ROOT/"data/grixis/m6/review_packets"/(item["slug"]+".json")),
    "original_99_card_main_verified":True,"commander_on_100th_slot_verified":True,
    "M5_original_swap_id":item["m5_swap_id"],
    "M5_source_priority_not_a_swap_approval":swaps[0]["priority_class"],
    "source_M5_test_flags_are_only_exploratory":swaps[0]["flags"],
    "protected_blueprint_core":[x["card"] for x in blueprint["identity_core"]],
    "commander_native_role":blueprint["commander_role"]["value"]["level"],
    "commander_primary_plan":blueprint["plan"]["value"]["primary"],
    "proposed_add_present_in_current_99":False,
    "proposed_cut_present_in_current_99":True,
    "proposed_card_legality_rechecked_at_decision_time":False,
    "strategic_disposition":item["disposition"],
    "author_rationale_from_review":item["why_no_change"],
    "named_independent_Pass_C_complete":False,
    "balanced_effect_aware_Phase_B_complete":False,
    "swap_applied_or_approved":False,
    "tested_pool_zero_improvement_certified":False}
def run():
  p=read(PLAN);reviews=read(REVIEWS);reg=read(REG)
  if (p["cycle"]!=112 or p["status"]!="preregistered_before_review_artifacts" or
    p["authority"]!=AUTH or reviews["cycle"]!=112 or reviews["review_count"]!=3 or
    reviews["decision_authority"] is not False or
    len(reg["decks"])!=62 or reg["program"]["milestones"]["M6"]["status"]!="in_progress" or
    reg["program"]["milestones"]["M6"]["accepted_by"] is not None or
    len(reviews["reviews"])!=3 or set(x["deck_id"] for x in reviews["reviews"])!=set(KEYS)):
   raise ValueError("Cycle112 plan, authored batch or milestone authority drift")
  resolver=ev.Resolver()
  oracle=oracle_gate(resolver)
  byid={x["deck_id"]:x for x in reviews["reviews"]}
  pbyid={x["deck_id"]:x for x in p["first_batch"]}
  outputs=[]
  for did in KEYS:
   d=reg["decks"][did];slug=d["slug"]
   b=read(ROOT/"data/grixis/blueprints"/(slug+".json"))
   m=read(ROOT/"data/grixis/m6/review_packets"/(slug+".json"))
   lib=sim.load_deck(slug,resolver)
   outputs.append(validate_review(byid[did],pbyid[did],d,b,m,lib,oracle))
  dispositions={x["commander"]:x["strategic_disposition"] for x in outputs}
  return {"schema_version":1,"cycle":112,
    "plan_sha256":sha(PLAN),"authored_review_sha256":sha(REVIEWS),
    "source_registry_sha256":sha(REG),"frozen_oracle_checks":oracle,
    "source_conservation":{"full_approved_lists_read":3,"reviewed_additions_applied":0,"canonical_repo_modified":False},
    "reviewed_decks":outputs,"dispositions":dispositions,
    "author_strategic_reviews_completed":3,
    "independent_Pass_C_reviews_completed":0,
    "full_effect_aware_M6_Phase_B_reviews_completed":0,
    "approvals_or_certifications_issued":0,
    "M6_accepted":False,"authority":AUTH,
    "next_required":"Independent critical assessment of these source-bound holds and narrowly scoped opponent-aware Gwendlyn untap-vs-tutor-denial pilot. No approved deck changes without explicit owner approval."}
def main():
  ap=argparse.ArgumentParser();ap.add_argument("--build",action="store_true");ap.add_argument("--check",action="store_true")
  args=ap.parse_args()
  if not(args.build or args.check):ap.error("Require --build or --check")
  x=run();text=dump(x)
  if args.build:
   OUT.parent.mkdir(parents=True,exist_ok=True)
   OUT.write_text(text,encoding="utf-8")
  if args.check and (not OUT.exists() or OUT.read_text(encoding="utf-8")!=text):
   raise ValueError("Cycle112 actual reviewed source evidence failed deterministic replay")
  print("Cycle112 3 author strategic reviews, source list / Oracle verified; no swap/Pass C approval",x["dispositions"],flush=True)
if __name__=="__main__":main()
