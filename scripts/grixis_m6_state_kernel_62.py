#!/usr/bin/env python3
"""Cycle 100: verify physical-card zone ledger on all 62 frozen Grixis decks.

Four deterministic 7+4-card draw samples per deck. No mulligan, real turn,
cast, effect, policy, opponent or win-rate simulation. Never modifies originals.
"""
from __future__ import annotations
import argparse,hashlib,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_authority as authority
import grixis_sim as sim
import evaluate_decklist as ev
from grixis_m6_state_kernel import Ledger,fingerprint

PLAN=ROOT/"data/grixis/m6/phase_b_plans/general_state_kernel_62_01.json"
OUT=ROOT/"data/grixis/m6/phase_b_bounded/general_state_kernel_62_01.json"
REG=ROOT/"data/grixis/registry.json"
SUMMARY=ROOT/"data/grixis_summary.json"
PRIOR=ROOT/"data/grixis/m6/phase_b_bounded/abaddon_tutor_state_01.json"
AUTH={"can_change_decklists":False,"can_approve_or_lock":False,
      "can_mark_m6_complete":False,"can_make_improvement_claim":False}
def data(p):return json.loads(p.read_text(encoding="utf-8"))
def sha(p):return "sha256:"+hashlib.sha256(p.read_bytes()).hexdigest()
def dump(a):return json.dumps(a,sort_keys=True,indent=2,ensure_ascii=False)+"\n"

def verify():
 p=data(PLAN);reg=data(REG);summ=data(SUMMARY);prior=data(PRIOR)
 c=p["coverage"];pol=p["fixed_policy"]
 if (p["cycle"]!=100 or p["preregistration_status"]!="registered_before_implementation"
     or p["protected"]!=AUTH or prior["supports_improvement_claim"]
     or len(reg["decks"])!=62 or len(summ)!=62
     or set(reg["decks"])!=set(summ)
     or reg["program"]["milestones"]["M5"]["status"]!="accepted"
     or reg["program"]["milestones"]["M6"]["accepted_by"] is not None
     or c["roster_decks"]!=62 or c["samples_per_deck"]!=4
     or c["seed"]!=100017 or c["starting_hand_size"]!=7
     or c["draws_after_opening"]!=4):
  raise ValueError("Unaccepted authority, prereg or 62-deck scope drift")
 resolver=ev.Resolver()
 cards_report=[]
 all_seeds=set();n_samples=0
 for ordinal,did in enumerate(sorted(summ)):
  info=summ[did];r=reg["decks"][did]
  slug=info["slug"]
  if slug!=r["slug"]:raise ValueError("Slug drift "+did)
  deck=sim.load_deck(slug,resolver)
  if len(deck.commanders)!=len(info["commanders"]):
   raise ValueError("Commander count mismatch: "+did)
  if [c["name"] for c in deck.commanders]!=info["commanders"]:
   raise ValueError("Commander identity drift: "+did)
  if len(deck.library)+len(deck.commanders)!=100:
   raise ValueError("Physical deck cardinality not 100: "+did+" "+str(len(deck.library))+"+"+str(len(deck.commanders)))
  samples=[]
  for j in range(c["samples_per_deck"]):
   seed=sim.seed_for(c["seed"],ordinal*c["samples_per_deck"]+j)
   if seed in all_seeds:raise ValueError("Repeated seed")
   all_seeds.add(seed)
   ledger=Ledger(deck.library,deck.commanders,seed)
   initial=ledger.initial_inventory_hash
   hand=ledger.draw(c["starting_hand_size"])
   extra=ledger.draw(c["draws_after_opening"])
   ledger.check()
   assert initial==ledger.initial_inventory_hash
   assert ledger.initial_card_count==100
   assert len(ledger.zones["hand"])==11
   assert len(ledger.zones["command"])==len(deck.commanders)
   assert len(ledger.zones["library"])==len(deck.library)-11
   assert not ledger.zones["battlefield"] and not ledger.zones["stack"]
   assert all(x==0 for x in ledger.mana.values())
   receipt=ledger.receipt()
   if receipt["unmodeled_effects"]!=0:raise ValueError("An unregistered effect was executed")
   samples.append({"sample":j,"seed":seed,"opening_names":ledger.drawn_names(hand),
                   "subsequent_draw_names":ledger.drawn_names(extra),
                   "post_draw_zone_hash":receipt["zone_fingerprint"],
                   "inventory_hash":receipt["inventory_hash"],
                   "post_draw_zone_counts":receipt["zone_counts"],
                   "conservation_pass":True})
   n_samples+=1
  cards_report.append({"deck_id":did,"slug":slug,
       "commanders":info["commanders"],"main_library_size":len(deck.library),
       "physical_card_count":len(deck.library)+len(deck.commanders),
       "authoritative_baseline_hash":r.get("baseline_hash"),
       "data_source":"existing frozen official-cache resolver and registry baseline",
       "samples":samples,
       "all_samples_conserve_100":True})
  print("Cycle 100 conserved",did,len(deck.library),len(deck.commanders),flush=True)
 if n_samples!=248 or len(cards_report)!=62:raise ValueError("Incomplete roster samples")
 return {"schema_version":1,"cycle":100,
   "stage":"M6_cross_62_conserved_state_kernel_access_only",
   "preregistration_sha256":sha(PLAN),
   "registry_sha256":sha(REG),"summaries_sha256":sha(SUMMARY),
   "cycle99_evidence_sha256":sha(PRIOR),
   "roster_decks":len(cards_report),"total_samples":n_samples,
   "seed":c["seed"],"opening_hand_size":c["starting_hand_size"],
   "draws_after_opening":c["draws_after_opening"],
   "all_samples_physical_conservation_verified":True,
   "zone_names":pol["zones"],"policies":pol,"limits":p["missing_capabilities"],
   "deck_samples":cards_report,
   "oracle_text_resolution_during_sampler":False,
   "card_abilities_executed":False,"full_gameplay_simulator":False,
   "commander_first_decisions_certified":0,"full_phase_b_complete":False,
   "supports_improvement_claim":False,"authority":AUTH}

def main():
 ap=argparse.ArgumentParser();ap.add_argument("--build",action="store_true");ap.add_argument("--check",action="store_true")
 args=ap.parse_args()
 if not(args.build or args.check):ap.error("require --build or --check")
 txt=dump(verify())
 if args.build:OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(txt,encoding="utf-8")
 if args.check and (not OUT.exists() or OUT.read_text(encoding="utf-8")!=txt):
  raise ValueError("Cycle 100 62-deck zone accounting replay mismatch")
 print("Cycle100: 62 exact baselines, 248 conserved shuffled sample hands; NO gameplay or deck decisions.")
if __name__=="__main__":main()
