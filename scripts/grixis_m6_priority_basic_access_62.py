#!/usr/bin/env python3
"""Cycle 102: 62-deck, 12-seed source-access benchmark and priority witness.

Four turns each: 7 shuffled opening cards, draw once per turn, at most one
real basic-land play per turn, and Arcane Signet paid with actual untapped basics
if drawn and affordable. No mulligan, other mana sources, opponent turns, or win
rate. This is a deliberately partial LOWER-COVERAGE execution policy.
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
from grixis_m6_priority_basics import PriorityBasics,BlockedAction

PLAN=ROOT/"data/grixis/m6/phase_b_plans/priority_basic_access_62_01.json"
OUT=ROOT/"data/grixis/m6/phase_b_bounded/priority_basic_access_62_01.json"
SUMMARY=ROOT/"data/grixis/m6/phase_b_bounded/priority_basic_access_62_summary_01.json"
REG=ROOT/"data/grixis/registry.json"
PRIOR=ROOT/"data/grixis/m6/phase_b_bounded/transactional_stack_62_01.json"
BEFORE=ROOT/"data/grixis/m6/phase_b_bounded/general_state_kernel_62_01.json"
SOURCE=ROOT/"exports/grixis-archidekt/source-baseline/abaddon-the-despoiler.txt"
AUTH={"can_change_decklists":False,"can_approve_or_lock":False,
      "can_decide":False,"can_certify_M6":False}
def load(p):return json.loads(p.read_text(encoding="utf-8"))
def sha(p):return "sha256:"+hashlib.sha256(p.read_bytes()).hexdigest()
def encode(a):return json.dumps(a,sort_keys=True,indent=2,ensure_ascii=False)+"\n"

def available_uid(t,name,zone="hand"):
 x=[uid for uid in t.zones[zone] if t.cards[uid]["name"]==name]
 if not x:return None
 return sorted(x)[0]

def trial(deck,seed):
 t=PriorityBasics(deck.library,deck.commanders,seed=seed)
 original=t.initial_inventory_hash
 opening=t.draw(7)
 opening_names=t.drawn_names(opening)
 draws=[];played=[];signet_cast_turn=None;failure_types=Counter()
 for turn in range(1,5):
  if turn>1:t.next_turn()
  drawn=t.draw(1)[0]
  draws.append(t.cards[drawn]["name"])
  # First basic physically in hand, not a hypothetical generic color source.
  basics=[u for u in t.zones["hand"] if t.cards[u]["name"] in BASIC_MANA
          and t.cards[u].get("land",False)]
  if basics:
   land=basics[0];t.play_basic(land);played.append(t.cards[land]["name"])
  else:
   failure_types["no_basic_land_in_hand_"+str(turn)]+=1
  if signet_cast_turn is None:
   signet=available_uid(t,"Arcane Signet")
   if signet is not None:
    try:
     paid=t.cast_with_basic_sources(signet)
    except BlockedAction as e:
     failure_types["signet_basic_payment_unavailable"]+=1
     if "cascade" in str(e):raise
    else:
     if len(paid)!=2:raise AssertionError("Signet actual physical-source payment should be two basics")
     t.resolve_by_passes()
     if t.zone_of(signet)!="battlefield":raise AssertionError("Signet did not enter battlefield")
     signet_cast_turn=turn
  t.check();t.validate_stack()
 if not (t.initial_inventory_hash==original and t.initial_card_count==100
         and len(opening_names)==7 and len(draws)==4
         and t.receipt()["zone_counts"]["stack"]==0
         and len(played)<=4):
  raise AssertionError("Card count or fixture turn policy drift")
 return {"seed":seed,"opening_names":opening_names,"draw_step_names":draws,
         "basic_lands_played":played,"basic_play_count":len(played),
         "signet_seen_by_turn4":sum(1 for x in opening_names+draws if x=="Arcane Signet")>0,
         "signet_cast_turn":signet_cast_turn,
         "signet_physically_cast":signet_cast_turn is not None,
         "blocked_policy_reasons":dict(sorted(failure_types.items())),
         "inventory_hash":original,"final_zone_hash":t.receipt()["zone_fingerprint"],
         "final_zones":t.receipt()["zone_counts"],"physical_cards_conserved":True,
         "source_injected_mana":False,"opponent_actions":0,
         "all_spells_resolved_by_four_seat_passes":True}

def abaddon_witness(deck):
 """Uses existing frozen canonical physical IDs, but FORCED hand for rules tests."""
 t=PriorityBasics(deck.library,deck.commanders,seed=102017)
 names=("Mountain","Swamp","Kessig Flamebreather","Dark Ritual")
 forced=[]
 for name in names:
  candidates=[u for u in t.zones["library"] if t.cards[u]["name"]==name]
  if not candidates:raise ValueError("Abaddon source identity missing: "+name)
  uid=candidates[0]
  t.transfer(uid,"library","hand");forced.append({"uid":uid,"name":name})
 t.play_basic(available_uid(t,"Mountain"))
 t.next_turn()
 t.play_basic(available_uid(t,"Swamp"))
 k=available_uid(t,"Kessig Flamebreather")
 t.cast_with_basic_sources(k)
 t.resolve_by_passes()
 t.next_turn()
 d=available_uid(t,"Dark Ritual")
 t.cast_with_basic_sources(d)
 t.pass_priority() # active passes and opponent seat 1 receives priority
 t.scripted_counter_spell(d)
 t.resolve_by_passes()
 if (t.zone_of(k)!="battlefield" or t.zone_of(d)!="graveyard"
     or t.opponents_lost_this_turn!=3 or t.mana["B"]!=0
     or t.opponents!=[39,38,30] or t.receipt()["count"]!=100):
  raise AssertionError("Source-backed priority/counter outcome witness incorrect")
 return {"source_deck":"Abaddon_the_Despoiler","fixture_forced_cards":forced,
         "priority_events":t.priority_events,"outcome_events":t.outcome_events,
         "receipt":t.receipt(),"opponents":t.opponents,
         "life_lost_by_opponents_this_turn":t.opponents_lost_this_turn,
         "actual_opponent_counterspell_cast":False,
         "all_physical_card_ids_conserved":True}

def verify():
 p=load(PLAN);reg=load(REG);old=load(PRIOR);old100=load(BEFORE)
 if (p["cycle"]!=102 or p["status"]!="preregistered_before_implementation"
     or p["authority"]!=AUTH or p["seed"]!=102017
     or p["roster"]!=62 or p["samples_per_deck"]!=12
     or p["starting_hand"]!=7 or p["draws_per_trial"]!=4
     or p["turns"]!=4 or p["players"]!=4
     or len(reg["decks"])!=62 or old["roster_cards_verified"]!=62
     or old100["roster_decks"]!=62 or old100["total_samples"]!=248
     or old["supports_improvement_claim"]
     or reg["program"]["milestones"]["M5"]["status"]!="accepted"
     or reg["program"]["milestones"]["M6"]["accepted_by"] is not None
     or sha(SOURCE)!="sha256:5448d76193923a3f9e3d4c41a327eaeaa9c6326d484d8e5a9abaf3852db2efff"):
  raise ValueError("Cycle 102 frozen prereg/authority/roster drift")
 resolver=ev.Resolver()
 source_decks={x["deck_id"]:x for x in old100["deck_samples"]}
 if set(source_decks)!=set(reg["decks"]):raise ValueError("Registry alias/slug mismatch")
 out=[];samples=0;signet_seen=0;signet_casts=0
 for ordinal,did in enumerate(sorted(reg["decks"])):
  slug=source_decks[did]["slug"]
  deck=sim.load_deck(slug,resolver)
  if [x["name"] for x in deck.commanders]!=reg["decks"][did]["commanders"]:
   raise ValueError("Commander identity drift "+did)
  if len(deck.library)+len(deck.commanders)!=100:
   raise ValueError("Deck not 100 cards "+did)
  tests=[]
  for i in range(p["samples_per_deck"]):
   seed=sim.seed_for(p["seed"],ordinal*p["samples_per_deck"]+i)
   receipt=trial(deck,seed)
   tests.append(receipt)
   samples+=1;signet_seen+=int(receipt["signet_seen_by_turn4"])
   signet_casts+=int(receipt["signet_physically_cast"])
  out.append({"deck_id":did,"slug":slug,
      "normalized_registry_commander_count":len(deck.commanders),
      "main_library_count":len(deck.library),
      "total_physical_cards":100,"sample_count":len(tests),
      "supported_card":"Arcane Signet",
      "sampled_signet_seen":sum(x["signet_seen_by_turn4"] for x in tests),
      "sampled_signet_casts_from_basics":sum(x["signet_physically_cast"] for x in tests),
      "samples":tests})
  print("Cycle102 sampled",did,len(tests),flush=True)
 if len(out)!=62 or samples!=744:raise ValueError("Incomplete Cycle102 roster")
 abaddon=sim.load_deck("abaddon-the-despoiler",resolver)
 witness=abaddon_witness(abaddon)
 return {"schema_version":1,"cycle":102,"stage":"M6_basic_mana_actual_access_priority_pass_bounded",
    "plan_sha256":sha(PLAN),"registry_sha256":sha(REG),
    "cycle101_sha256":sha(PRIOR),"cycle100_sha256":sha(BEFORE),
    "deck_count":len(out),"sample_count":samples,
    "seed":p["seed"],"sampled_signet_seen":signet_seen,
    "sampled_signet_basic_casts":signet_casts,
    "deck_access_receipts":out,"abaddon_priority_witness":witness,
    "full_deck_gameplay_simulator":False,"comprehensive_priority_rules":False,
    "opponent_counterspell_modeled":False,"nonbasic_mana_modeled":False,
    "mulligan_policy_modeled":False,"cascade_execution_modeled":False,
    "uses_injected_mana_in_access_samples":False,
    "supports_improvement_claim":False,"full_phase_b_complete":False,
    "formal_independent_pass_c_complete":False,"M6_accepted":False,
    "limits":p["non_goals"],"authority":AUTH}

def compact_receipt(full):
 rows=[]
 for deck in full["deck_access_receipts"]:
  rows.append({"deck_id":deck["deck_id"],
    "signet_seen":deck["sampled_signet_seen"],
    "signet_paid_from_basic_sources":deck["sampled_signet_casts_from_basics"],
    "total_basic_land_plays":sum(s["basic_play_count"] for s in deck["samples"]),
    "samples":deck["sample_count"]})
 return {"schema_version":1,"cycle":102,
   "full_source_sha256":full["plan_sha256"],
   "description":"Deterministic audit index derived from 744 fixed-seed partial basic-only access samples; NOT game or win percentages",
   "decks":full["deck_count"],"samples":full["sample_count"],
   "signet_seen":full["sampled_signet_seen"],
   "signet_paid_from_basic_sources":full["sampled_signet_basic_casts"],
   "total_basic_land_plays":sum(r["total_basic_land_plays"] for r in rows),
   "no_nonbasic_mana":True,"no_injected_mana":True,
   "no_wins_or_candidate_comparisons":True,"no_improvement_claim":True,
   "per_deck":rows}

def main():
 q=argparse.ArgumentParser();q.add_argument("--build",action="store_true");q.add_argument("--check",action="store_true")
 args=q.parse_args()
 if not(args.build or args.check):q.error("require --build or --check")
 report=verify()
 txt=encode(report)
 small=encode(compact_receipt(report))
 if args.build:
  OUT.parent.mkdir(parents=True,exist_ok=True)
  OUT.write_text(txt,encoding="utf-8")
  SUMMARY.write_text(small,encoding="utf-8")
 if args.check and (not OUT.exists() or OUT.read_text(encoding="utf-8")!=txt
     or not SUMMARY.exists() or SUMMARY.read_text(encoding="utf-8")!=small):
  raise ValueError("Cycle102 full evidence or compact audit summary drift")
 print("Cycle102 62 decks / 744 samples: sampled signet seen",report["sampled_signet_seen"],
       "actual basic-source casts",report["sampled_signet_basic_casts"],
       "no win/strength inference",flush=True)
if __name__=="__main__":main()
