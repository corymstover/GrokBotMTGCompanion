#!/usr/bin/env python3
"""Cycle103: 62 baseline decks / same 744 exact draws as Cycle102, 19 lands.

Improvement metric is ONLY implemented mana-source coverage for Arcane Signet.
Card access remains fixed seed and artificially simplified; not wins/strength.
"""
from __future__ import annotations
import argparse,hashlib,json,sys
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import evaluate_decklist as ev
import grixis_sim as sim
from grixis_m6_state_kernel import BASIC_MANA
from grixis_m6_priority_nonbasic import PriorityNonbasic,LANDS,TYPED,REQUIRES

PLAN=ROOT/"data/grixis/m6/phase_b_plans/nonbasic_land_access_62_01.json"
PRIOR=ROOT/"data/grixis/m6/phase_b_bounded/priority_basic_access_62_01.json"
OUT=ROOT/"data/grixis/m6/phase_b_bounded/nonbasic_land_access_62_01.json"
SUMMARY=ROOT/"data/grixis/m6/phase_b_bounded/nonbasic_land_access_62_summary_01.json"
REG=ROOT/"data/grixis/registry.json"
SOURCE=ROOT/"exports/grixis-archidekt/source-baseline/abaddon-the-despoiler.txt"
AUTH={"can_change_decklists":False,"can_approve_or_lock":False,
      "can_decide":False,"can_certify_M6":False}
def read(p):return json.loads(p.read_text(encoding="utf-8"))
def sha(p):return "sha256:"+hashlib.sha256(p.read_bytes()).hexdigest()
def fmt(x):return json.dumps(x,sort_keys=True,indent=2,ensure_ascii=False)+"\n"

def oracle_checks(resolver,plan):
 receipt={}
 if set(plan["supported_nonbasic_mana_colors"])!=set(LANDS):
  raise ValueError("Model/preregistered source count changed")
 groups=plan["entry_groups"]
 for name,(choices,tag) in LANDS.items():
  card=resolver.get(name)[0]
  text=card.get("oracle_text") or ""
  lower=text.casefold()
  typ=card.get("type_line") or ""
  if "Land" not in typ or not text or card.get("name")!=name:
   raise ValueError("Unverified named land source: "+name)
  if list(choices)!=plan["supported_nonbasic_mana_colors"][name]:
   raise ValueError("Mana color mismatched plan: "+name)
  expected_group={
   "always":"always_untapped","life_mana":"always_untapped",
   "tapped":"always_tapped","shock":"shock_optional_two_life",
   "typed":"typed_check","fast":"fast_two_or_fewer_other_lands",
   "bond":"multiplayer_two_plus_opponents"}[tag]
  if name not in groups[expected_group]:raise ValueError("Wrong prereg entry group "+name)
  for c in choices:
   if name not in ("Command Tower","Mana Confluence") and ("{"+c+"}").casefold() not in lower:
    raise ValueError("Oracle lacks expected printed source color: "+name+" / "+c)
  if name=="Command Tower" and "commander's color identity" not in lower:
   raise ValueError("Command Tower mana depends on commander color identity")
  if name=="Mana Confluence" and ("pay 1 life" not in lower or "any color" not in lower):
   raise ValueError("Mana Confluence activation life cost or flexible mana drift")
  if tag=="tapped" and "enters tapped" not in lower:
   raise ValueError("Mandatory tapped land Oracle drift "+name)
  if tag=="shock" and ("pay 2 life" not in lower or "enters tapped" not in lower):
   raise ValueError("Shockland life replacement choice Oracle drift "+name)
  if tag=="typed":
   if "enters tapped unless" not in lower or any(w.casefold() not in lower for w in REQUIRES[name]):
    raise ValueError("Typed checkland entry condition Oracle drift "+name)
  if tag=="fast" and "two or fewer other lands" not in lower:
   raise ValueError("Fastland entry condition drift "+name)
  if tag=="bond" and "two or more opponents" not in lower:
   raise ValueError("Multiplayer bondland condition drift "+name)
  if name in TYPED and any(w not in typ.split("—")[-1] for w in TYPED[name].split()):
   raise ValueError("Printed land subtype drift "+name)
  receipt[name]={"oracle_sha256":"sha256:"+hashlib.sha256(text.encode()).hexdigest(),
    "type_line":typ,"modeled_color_choices":list(choices),"entry_policy":tag,
    "unmodeled_abilities_exist":name=="Xander's Lounge"}
 return receipt

def trial(deck,seed,previous):
 t=PriorityNonbasic(deck.library,deck.commanders,seed=seed,opponent_count=3)
 init=t.initial_inventory_hash
 hand=t.draw(7);opened=t.drawn_names(hand)
 draws=[];played=[];unsupported_seen=set();signet_turn=None
 failure=Counter()
 for turn in range(1,5):
  if turn>1:t.next_turn()
  new=t.draw(1)[0];draws.append(t.cards[new]["name"])
  # All physical drawn cards are preserved. Unsupported lands are not treated
  # as tapped, mana-producing, or played by the model.
  unsupported_seen|={t.cards[u]["name"] for u in t.zones["hand"]
    if t.cards[u].get("land") and t.cards[u]["name"] not in LANDS
    and t.cards[u]["name"] not in BASIC_MANA}
  choices=[u for u in t.zones["hand"]
      if t.cards[u].get("land") and (t.cards[u]["name"] in LANDS or t.cards[u]["name"] in BASIC_MANA)]
  if choices:
   u=choices[0];name=t.cards[u]["name"]
   ready=t.play_supported_land(u)
   played.append({"id":u,"name":name,"entered_tapped":not ready,
      "life_after_entry":t.pilot,"turn":turn})
  else:failure["no_supported_land_in_hand"]+=1
  if signet_turn is None:
   signet=next((u for u in t.zones["hand"] if t.cards[u]["name"]=="Arcane Signet"),None)
   if signet is not None:
    from grixis_m6_priority_nonbasic import BlockedAction
    try:source_ids=t.cast_with_land_sources(signet)
    except BlockedAction:failure["signet_not_payable_with_modeled_lands"]+=1
    else:
     if len(source_ids)!=2:raise AssertionError("Arcane Signet cost must be exactly two land sources")
     t.resolve_by_passes()
     if t.zone_of(signet)!="battlefield":raise AssertionError("Signet physical destination incorrect")
     signet_turn=turn
  t.check();t.validate_stack()
 if opened!=previous["opening_names"] or draws!=previous["draw_step_names"] or seed!=previous["seed"]:
  raise ValueError("Cycle103 shuffled sequence differs from Cycle102 SAME seed")
 if t.initial_inventory_hash!=init or init!=previous["inventory_hash"]:
  raise ValueError("Changed card identity after source-backed sampling")
 if t.initial_card_count!=100 or sum(t.receipt()["zone_counts"].values())!=100:
  raise ValueError("Physical card count changed")
 return {"seed":seed,"opening_names":opened,"draw_step_names":draws,
   "lands_played":played,"play_count":len(played),
   "supported_nonbasic_play_count":sum(x["name"] in LANDS for x in played),
   "entered_tapped":sum(x["entered_tapped"] for x in played),
   "unsupported_land_names_seen":sorted(unsupported_seen),
   "signet_seen_by_turn4":"Arcane Signet" in opened+draws,
   "signet_cast_turn":signet_turn,"signet_paid_with_real_land_sources":signet_turn is not None,
   "source_mana_injected":False,"source_life_after_turn4":t.pilot,
   "fail_closed_counts":dict(sorted(failure.items())),
   "initial_inventory_hash":init,"final_zone_hash":t.receipt()["zone_fingerprint"],
   "final_zone_counts":t.receipt()["zone_counts"],"physical_card_conservation":True}

def verify():
 p=read(PLAN);old=read(PRIOR);r=read(REG)
 if (p["cycle"]!=103 or p["status"]!="preregistered_before_implementation"
     or p["seed"]!=102017 or p["roster"]!=62 or p["samples_per_deck"]!=12
     or p["authority"]!=AUTH or old["sample_count"]!=744
     or old["deck_count"]!=62 or old["supports_improvement_claim"]
     or len(r["decks"])!=62 or r["program"]["milestones"]["M6"]["status"]!="in_progress"
     or sha(SOURCE)!="sha256:5448d76193923a3f9e3d4c41a327eaeaa9c6326d484d8e5a9abaf3852db2efff"):
  raise ValueError("Frozen registry, prereg, or Cycle102 source changed")
 resolver=ev.Resolver()
 receipts=oracle_checks(resolver,p)
 before={x["deck_id"]:x for x in old["deck_access_receipts"]}
 if set(before)!=set(r["decks"]):raise ValueError("Deck roster drift since Cycle102")
 rows=[];aggregate=Counter();by_land=Counter();unsupported=Counter()
 for ord,did in enumerate(sorted(r["decks"])):
  previous=before[did];deck=sim.load_deck(previous["slug"],resolver)
  if len(deck.library)+len(deck.commanders)!=100:raise ValueError("Deck count not 100 "+did)
  trials=[]
  for idx,old_trial in enumerate(previous["samples"]):
   seed=sim.seed_for(p["seed"],ord*p["samples_per_deck"]+idx)
   record=trial(deck,seed,old_trial)
   trials.append(record)
   aggregate["samples"]+=1
   aggregate["seen"]+=int(record["signet_seen_by_turn4"])
   aggregate["cast"]+=int(record["signet_paid_with_real_land_sources"])
   aggregate["land_plays"]+=record["play_count"]
   aggregate["nonbasic_plays"]+=record["supported_nonbasic_play_count"]
   aggregate["tapped_entries"]+=record["entered_tapped"]
   by_land.update(x["name"] for x in record["lands_played"])
   unsupported.update(record["unsupported_land_names_seen"])
  rows.append({"deck_id":did,"slug":previous["slug"],"samples":trials,
     "signet_seen":sum(x["signet_seen_by_turn4"] for x in trials),
     "signet_source_paid":sum(x["signet_paid_with_real_land_sources"] for x in trials),
     "modeled_land_plays":sum(x["play_count"] for x in trials),
     "supported_nonbasic_plays":sum(x["supported_nonbasic_play_count"] for x in trials)})
  print("Cycle103 checked",did,len(trials),flush=True)
 if aggregate["samples"]!=744 or aggregate["seen"]!=old["sampled_signet_seen"]:
  raise ValueError("Deckwide access or Signet seeing changed against Cycle102")
 return {"schema_version":1,"cycle":103,"stage":"M6_19_nonbasic_real_mana_sources_62_decks",
  "preregistration_sha256":sha(PLAN),"previous_cycle102_sha256":sha(PRIOR),
  "registry_sha256":sha(REG),"oracle_verified_lands":receipts,
  "deck_count":len(rows),"samples":aggregate["samples"],"signet_seen":aggregate["seen"],
  "signet_cast_with_supported_lands":aggregate["cast"],
  "comparison_basic_only_cycle102_casts":old["sampled_signet_basic_casts"],
  "modeled_land_plays":aggregate["land_plays"],"modeled_nonbasic_plays":aggregate["nonbasic_plays"],
  "tapped_entries":aggregate["tapped_entries"],
  "land_play_name_counts":dict(sorted(by_land.items())),
  "unsupported_land_seen_count":dict(sorted(unsupported.items())),
  "deck_samples":rows,
  "no_actual_opponent_decisions":True,"no_nonland_spells_other_than_signet":True,
  "complete_gameplay_model":False,"candidate_improvement_inferred":False,
  "phase_b_complete":False,"M6_accepted":False,"authority":AUTH,"limitations":p["limitations"]}

def compact(x):
 return {"schema_version":1,"cycle":103,"source_preregistration_sha256":x["preregistration_sha256"],
  "decks":x["deck_count"],"samples":x["samples"],"signet_seen":x["signet_seen"],
  "source_paid_signet_casts":x["signet_cast_with_supported_lands"],
  "prior_basic_only_casts":x["comparison_basic_only_cycle102_casts"],
  "modeled_land_plays":x["modeled_land_plays"],
  "supported_nonbasic_plays":x["modeled_nonbasic_plays"],
  "tapped_entries":x["tapped_entries"],
  "land_play_name_counts":x["land_play_name_counts"],
  "unsupported_land_seen_count":x["unsupported_land_seen_count"],
  "per_deck":[{"deck_id":d["deck_id"],"signet_seen":d["signet_seen"],
    "source_paid":d["signet_source_paid"],"land_plays":d["modeled_land_plays"],
    "nonbasic_plays":d["supported_nonbasic_plays"]} for d in x["deck_samples"]],
  "no_game_or_commander_strength_claim":True}

def main():
 q=argparse.ArgumentParser()
 q.add_argument("--build",action="store_true");q.add_argument("--check",action="store_true")
 a=q.parse_args()
 if not(a.build or a.check):q.error("require --build or --check")
 result=verify();big=fmt(result);small=fmt(compact(result))
 if a.build:
  OUT.parent.mkdir(parents=True,exist_ok=True)
  OUT.write_text(big,encoding="utf-8")
  SUMMARY.write_text(small,encoding="utf-8")
 if a.check and (not OUT.exists() or OUT.read_text(encoding="utf-8")!=big
          or not SUMMARY.exists() or SUMMARY.read_text(encoding="utf-8")!=small):
  raise ValueError("Cycle103 full/compact paired replay drift")
 print("Cycle103",result["samples"],"trials",result["signet_cast_with_supported_lands"],
       "land-source casts versus",result["comparison_basic_only_cycle102_casts"],
       "basic-only; NO win/strength inference",flush=True)
if __name__=="__main__":main()
