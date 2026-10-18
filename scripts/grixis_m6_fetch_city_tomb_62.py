#!/usr/bin/env python3
"""Cycle104: matched source-backed fetch/City/Tomb limited access for 62 decks.

All 744 opening hands reproduce Cycle103. Fetch search legitimately shuffles
later draws, so no artificial post-search draw equality is asserted.
This is coverage sampling, not 744 games, mana-base strength or win rates.
"""
from __future__ import annotations
import argparse,hashlib,json,sys
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import evaluate_decklist as ev
import grixis_sim as sim
from grixis_m6_state_kernel import BASIC_MANA,BlockedAction
from grixis_m6_priority_nonbasic import LANDS
from grixis_m6_fetch_city_tomb import PriorityFetchCityTomb,FETCHES,SPECIALS,MODEL_LANDS

PLAN=ROOT/"data/grixis/m6/phase_b_plans/fetch_city_tomb_62_01.json"
PRIOR=ROOT/"data/grixis/m6/phase_b_bounded/nonbasic_land_access_62_01.json"
OUT=ROOT/"data/grixis/m6/phase_b_bounded/fetch_city_tomb_62_01.json"
SMALL=ROOT/"data/grixis/m6/phase_b_bounded/fetch_city_tomb_62_summary_01.json"
REG=ROOT/"data/grixis/registry.json"
SOURCE=ROOT/"exports/grixis-archidekt/source-baseline/abaddon-the-despoiler.txt"
AUTH={"can_change_decklists":False,"can_approve_or_lock":False,
      "can_decide":False,"can_certify_M6":False}
def read(p):return json.loads(p.read_text(encoding="utf-8"))
def sha(p):return "sha256:"+hashlib.sha256(p.read_bytes()).hexdigest()
def fmt(x):return json.dumps(x,sort_keys=True,indent=2,ensure_ascii=False)+"\n"

def gate(resolver,plan):
 if set(plan["fetchlands"])!=set(FETCHES) or plan["utility_lands"]!=list(SPECIALS):
  raise ValueError("Cycle104 supported fetch/utility names differ from plan")
 results={}
 for name,types in FETCHES.items():
  if tuple(types)!=FETCHES[name]:raise ValueError("Fetch target subtype prereg drift")
  c=resolver.get(name)[0];txt=c.get("oracle_text") or ""
  if c.get("name")!=name or "Land" not in c.get("type_line",""):
   raise ValueError("Missing frozen fetch land identity "+name)
  low=txt.casefold()
  required=["pay 1 life","sacrifice","search your library","put it onto the battlefield","shuffle"]
  required+= [t.casefold() for t in types]
  if any(x not in low for x in required) or "{T}" not in txt:
   raise ValueError("Fetch Oracle timing, costs or search changed "+name+": "+repr(txt))
  results[name]={"oracle_sha256":"sha256:"+hashlib.sha256(txt.encode()).hexdigest(),
     "type_line":c["type_line"],"registered_target_types":types,
     "modeled_cost":"tap, pay 1 life, sacrifice"}
 for name in SPECIALS:
  c=resolver.get(name)[0];txt=c.get("oracle_text") or "";low=txt.casefold()
  if c.get("name")!=name or "Land" not in c.get("type_line","") or "{T}" not in txt:
   raise ValueError("Frozen utility land identity changed "+name)
  if name=="Ancient Tomb":
   required=["add {c}{c}","deals 2 damage to you"]
  else:required=["add one mana of any color","whenever","becomes tapped","deals 1 damage to you"]
  if any(s not in low for s in required):
   raise ValueError("Utility land Oracle damage or mana timing changed "+name+": "+repr(txt))
  results[name]={"oracle_sha256":"sha256:"+hashlib.sha256(txt.encode()).hexdigest(),
   "type_line":c["type_line"],
   "timing":"direct immediate damage within mana ability" if name=="Ancient Tomb" else
       "mana now, distinct on-tap damage trigger"}
 return results

def simulate(deck,seed,prior):
 t=PriorityFetchCityTomb(deck.library,deck.commanders,seed=seed,opponent_count=3)
 original=t.initial_inventory_hash
 ids=t.draw(7);opening=t.drawn_names(ids)
 if seed!=prior["seed"] or opening!=prior["opening_names"]:
  raise ValueError("Same-seed opening changed since Cycle103")
 draws=[];lands_played=[];signet_turn=None;fail=Counter()
 for turn in range(1,5):
  if turn>1:t.next_turn()
  card=t.draw(1)[0];draws.append(t.cards[card]["name"])
  valid=[i for i in t.zones["hand"] if t.cards[i].get("land",False)
         and t.cards[i]["name"] in MODEL_LANDS]
  if valid:
   land=valid[0];name=t.cards[land]["name"]
   ready=t.play_supported_land(land)
   lands_played.append({"name":name,"id":land,"turn":turn,"entered_untapped":ready})
   if name in FETCHES:
    if t.pilot>1:
     t.activate_fetch(land);t.resolve_by_passes()
    else:fail["fetch_ability_not_activated_at_low_life"]+=1
  else:fail["no_registered_land_available"]+=1
  if signet_turn is None:
   signet=next((i for i in t.zones["hand"] if t.cards[i]["name"]=="Arcane Signet"),None)
   if signet:
    try:src=t.cast_with_land_sources(signet)
    except BlockedAction as e:
     if "cascade" in str(e):raise
     fail["signet_unaffordable_with_modeled_sources"]+=1
    else:
     if not src:raise AssertionError("No physical land source used for Signet")
     t.resolve_by_passes()
     if t.zone_of(signet)!="battlefield":raise AssertionError("Signet missing battlefield")
     signet_turn=turn
  t.check();t.validate_stack()
 if original!=t.initial_inventory_hash or t.initial_card_count!=100:
  raise AssertionError("Physical card inventory changed")
 if t.frames or t.zones["stack"]:raise AssertionError("Unresolved modeled stack")
 if len(draws)!=4 or len(opening)!=7:
  raise AssertionError("Opening/draw samples incomplete")
 utility=Counter(e["event"] for e in t.utility_events)
 divergence=(draws!=prior["draw_step_names"])
 first_different=next((i+1 for i,(a,b) in enumerate(zip(draws,prior["draw_step_names"])) if a!=b),None)
 if divergence and not t.fetch_resolutions:
  raise AssertionError("Draw stream diverged without fetching/shuffling")
 # Drawing on turn one occurs before first possible fetch activation.
 if draws[0]!=prior["draw_step_names"][0]:
  raise AssertionError("First draw differs before any search")
 return {"seed":seed,"opening_names":opening,"draw_step_names":draws,
   "cycle103_draws":prior["draw_step_names"],"post_search_draws_diverged":divergence,
   "first_different_draw_step":first_different,"played_lands":lands_played,
   "signet_seen_by_four":"Arcane Signet" in opening+draws,
   "signet_paid_from_modeled_lands":signet_turn is not None,
   "signet_turn":signet_turn,"fetch_activations":utility["fetch_activated_costs_paid"],
   "fetch_searches_resolved":utility["fetch_search_resolved"],
   "city_trigger_resolutions":utility["city_of_brass_damage_resolves"],
   "ancient_tomb_mana_activations":utility["ancient_tomb_mana_and_damage"],
   "life_after_four_turns":t.pilot,
   "source_target_receipts":t.fetch_search_events,
   "blocked_counts":dict(sorted(fail.items())),
   "final_zone_counts":t.receipt()["zone_counts"],
   "final_zone_hash":t.receipt()["zone_fingerprint"],
   "same_physical_inventory":True,"no_injected_mana":True,
   "no_real_opponent_actions":True}

def verify():
 p=read(PLAN);old=read(PRIOR);reg=read(REG)
 if (p["cycle"]!=104 or p["status"]!="preregistered_before_implementation"
     or p["seed"]!=102017 or p["roster"]!=62 or p["samples_per_deck"]!=12
     or p["authority"]!=AUTH or old["samples"]!=744 or old["deck_count"]!=62
     or old["candidate_improvement_inferred"]
     or len(reg["decks"])!=62 or reg["program"]["milestones"]["M6"]["status"]!="in_progress"
     or sha(SOURCE)!="sha256:5448d76193923a3f9e3d4c41a327eaeaa9c6326d484d8e5a9abaf3852db2efff"):
  raise ValueError("Frozen Cycle104 plan or provenance drift")
 resolver=ev.Resolver();oracle=gate(resolver,p)
 olddeck={x["deck_id"]:x for x in old["deck_samples"]}
 if set(olddeck)!=set(reg["decks"]):raise ValueError("62 roster IDs not reconciled")
 rows=[];agg=Counter();played=Counter()
 for ord,did in enumerate(sorted(reg["decks"])):
  prev=olddeck[did]
  deck=sim.load_deck(prev["slug"],resolver)
  if len(deck.commanders)+len(deck.library)!=100:raise AssertionError("Non-100-card source deck")
  trials=[]
  for j,src in enumerate(prev["samples"]):
   sd=sim.seed_for(p["seed"],ord*12+j)
   x=simulate(deck,sd,src)
   trials.append(x);agg["samples"]+=1
   for k in ("signet_seen_by_four","signet_paid_from_modeled_lands",
             "post_search_draws_diverged"):
    agg[k]+=int(x[k])
   for k in ("fetch_activations","fetch_searches_resolved",
             "city_trigger_resolutions","ancient_tomb_mana_activations"):
    agg[k]+=x[k]
   played.update(x["name"] for x in x["played_lands"])
  rows.append({"deck_id":did,"slug":prev["slug"],"samples":trials,
       "signet_seen":sum(z["signet_seen_by_four"] for z in trials),
       "signet_paid":sum(z["signet_paid_from_modeled_lands"] for z in trials),
       "fetch_resolutions":sum(z["fetch_searches_resolved"] for z in trials)})
  print("Cycle104 checked",did,len(trials),flush=True)
 if agg["samples"]!=744:raise ValueError("Incomplete samples")
 return {"schema_version":1,"cycle":104,"stage":"M6_62_decks_fetch_city_tomb_bounded",
  "plan_sha256":sha(PLAN),"previous_cycle103_sha256":sha(PRIOR),
  "registry_sha256":sha(REG),"oracle_verified_new_lands":oracle,
  "decks":62,"samples":agg["samples"],"original_cycle103_signet_seen":old["signet_seen"],
  "original_cycle103_signet_paid":old["signet_cast_with_supported_lands"],
  "new_signets_seen":agg["signet_seen_by_four"],"new_signets_paid":agg["signet_paid_from_modeled_lands"],
  "fetch_activations":agg["fetch_activations"],"fetch_searches_resolved":agg["fetch_searches_resolved"],
  "city_damage_trigger_resolutions":agg["city_trigger_resolutions"],
  "ancient_tomb_mana_activations":agg["ancient_tomb_mana_activations"],
  "post_search_draw_divergences":agg["post_search_draws_diverged"],
  "played_land_names":dict(sorted(played.items())),
  "deck_samples":rows,"full_gameplay_model":False,"complete_priority":False,
  "full_phase_b_complete":False,"M6_accepted":False,"supports_improvement_claim":False,
  "source_legal_coverage_only":True,"authority":AUTH,"limitations":p["limits"]}

def compact(a):
 return {"schema_version":1,"cycle":104,"plan_sha256":a["plan_sha256"],
  "decks":a["decks"],"samples":a["samples"],
  "oracle_verified_lands":sorted(a["oracle_verified_new_lands"]),
  "prior_signet_seen":a["original_cycle103_signet_seen"],
  "prior_signet_paid":a["original_cycle103_signet_paid"],
  "new_signet_seen":a["new_signets_seen"],"new_signet_paid":a["new_signets_paid"],
  "fetch_activations":a["fetch_activations"],"fetch_resolutions":a["fetch_searches_resolved"],
  "city_damage_resolutions":a["city_damage_trigger_resolutions"],
  "ancient_tomb_taps":a["ancient_tomb_mana_activations"],
  "post_search_draw_divergences":a["post_search_draw_divergences"],
  "played_land_names":a["played_land_names"],
  "per_deck":[{"deck_id":x["deck_id"],"signet_seen":x["signet_seen"],
    "signet_paid":x["signet_paid"],"fetch_resolutions":x["fetch_resolutions"]} for x in a["deck_samples"]],
  "no_win_probability_or_card_strength_claim":True,"all_source_lists_unchanged":True}

def main():
 parser=argparse.ArgumentParser()
 parser.add_argument("--build",action="store_true")
 parser.add_argument("--check",action="store_true")
 args=parser.parse_args()
 if not(args.build or args.check):parser.error("Require --build or --check")
 r=verify();large=fmt(r);small=fmt(compact(r))
 if args.build:
  OUT.parent.mkdir(parents=True,exist_ok=True)
  OUT.write_text(large,encoding="utf-8")
  SMALL.write_text(small,encoding="utf-8")
 if args.check and (not OUT.exists() or OUT.read_text(encoding="utf-8")!=large
    or not SMALL.exists() or SMALL.read_text(encoding="utf-8")!=small):
  raise ValueError("Cycle104 replay not reproducible")
 print("Cycle104 same 744 openings; real fetch shuffle, City trigger, Tomb source; no win/upgrade claim",flush=True)
if __name__=="__main__":main()
