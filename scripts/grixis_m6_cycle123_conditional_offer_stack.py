#!/usr/bin/env python3
"""Cycle123 bounded actual pilot spell zones vs STIPULATED opponent instant.

Physical baseline 99-card library, approved hash, source-paid {U}, explicit
stack/priority pass witness. Opponent spell is virtual, not from any observed
opponent deck. Its occurrence, opponent passing and target's counterability
are assumptions, never real multiplayer or win-rate evidence.
"""
from __future__ import annotations
import argparse,copy,hashlib,json,random,sys
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import evaluate_decklist as ev
import grixis_authority as ga
import grixis_sim as sim
import grixis_paired as paired
import grixis_m6_cycle120_physical_access as c120
import grixis_m6_cycle121_basic_paid_casts as c121
import grixis_m6_cycle122_nonbasic_source_casts as c122
from grixis_m6_priority_nonbasic import PriorityNonbasic
from grixis_m6_state_kernel import BlockedAction

PLAN=ROOT/"data/grixis/m6/phase_b_plans/cycle123_conditional_offer_stack_prereg_01.json"
PARENT=ROOT/"data/grixis/m6/phase_b_plans/cycle122_nonbasic_source_casts_prereg_01.json"
REG=ROOT/"data/grixis/registry.json"
OUT=ROOT/"data/grixis/m6/phase_b_bounded/cycle123_conditional_offer_stack_01.json"
AUTH={"can_change_62_canonical_decks":False,"can_apply_candidate":False,
      "can_claim_completed_phase_b":False,"can_issue_independent_pass_c":False,
      "can_accept_m6_or_m7":False}
OFFER="An Offer You Can't Refuse"
JEWEL="The Enigma Jewel // Locus of Enlightenment"
def read(p):return json.loads(Path(p).read_text(encoding="utf-8"))
def sha(p):return "sha256:"+hashlib.sha256(Path(p).read_bytes()).hexdigest()
def fmt(x):return json.dumps(x,sort_keys=True,ensure_ascii=False,indent=2)+"\n"

def verify(plan,parent,reg,R):
  if (plan["schema_version"]!=1 or plan["cycle"]!=123 or
      plan["status"]!="preregistered_before_result_generation" or plan["authority"]!=AUTH or
      plan["depends_on"]["cycle122_merge_sha"]!="d6c4bf4076310d23e93af60e10e81fbe950200a9" or
      parent["cycle"]!=122 or reg["program"]["milestones"]["M6"]["status"]!="in_progress" or
      reg["program"]["milestones"]["M7"]["status"]!="not_started" or len(reg["decks"])!=62 or
      plan["fixed_sampling"]["seed"]!=120026 or plan["fixed_sampling"]["n"]!=1024 or
      plan["fixed_sampling"]["opening"]!=7 or plan["fixed_sampling"]["draw_one_own_turn"]!=8 or
      plan["fixed_sampling"]["mulligans"] is not False or
      [x["id"] for x in plan["preregistered_counterfactuals"]]!=
      ["offer_noncreature_counterable","offer_uncounterable","offer_becomes_illegal",
       "offer_illegal_creature_target","no_opponent_spell"]):
    raise ValueError("Registered source/conditional event protocol has changed")
  source=next(x for x in parent["studies"] if x["deck_id"]=="Mai_and_Zuko")
  if plan["deck"]!=source or source["cut"]!=OFFER or source["add"]!=JEWEL:
    raise ValueError("M5 baseline/candidate swapped, source deck drift")
  d=reg["decks"]["Mai_and_Zuko"]
  if (d["current_canonical_hash"]!=source["approved_logical_hash"] or
      d["source"]["recorded_sha256"]!=source["approved_raw_sha256"] or
      ga.text_hash(ga.deck_block_text(source["slug"]),R)!=source["approved_logical_hash"]):
    raise ValueError("Source deck approval hash mismatch")
  oracle=R.get(OFFER)[0]
  if (oracle["name"]!=OFFER or oracle["mana_cost"]!="{U}" or
      "Counter target noncreature spell" not in oracle["oracle_text"] or
      "Its controller creates two Treasure tokens" not in oracle["oracle_text"]):
    raise ValueError("An Offer frozen Oracle ability or blue-cost drift")
  if c121.COST[JEWEL]!=(0,{"U":1}):
    raise ValueError("Jewel must still require blue mana")
  # Cycle122's 19 named-land source models and Oracle checks are prerequisites.
  c122.verify(parent,reg,read(c122.PRIOR),R)
  return {"offer_oracle_text_sha256":"sha256:"+hashlib.sha256(oracle["oracle_text"].encode()).hexdigest(),
          "nineteen_frozen_oracle_nonbasic_land_gates":True}

def eligible_offer_sources(t):
  uid=next((u for u in t.zones["hand"] if t.cards[u]["name"]==OFFER),None)
  if uid is None:return None
  payment=c122.source_payment(t,OFFER)
  return (uid,payment) if payment else None

def source_paid_offer_fixture(t,kind="noncreature",spell_present=True,
                              pilot_priority=True,counterable=True,removed_after_cast=False):
  """One bounded virtual spell stack + physical Offer. All three other seats pass.
  Rejected illegal targets/priority preserve source zones/mana/life."""
  if not spell_present:raise BlockedAction("No opponent spell exists in this fixture")
  if kind!="noncreature":raise BlockedAction("An Offer can only target noncreature spells")
  if not pilot_priority or t.priority_seat!=0 or t.pass_count or t.frames or t.zones["stack"]:
    raise BlockedAction("Pilot priority to respond with legal empty pilot stack unavailable")
  held=eligible_offer_sources(t)
  if held is None:raise BlockedAction("Missing physical Offer or source-payable {U}")
  uid,payment=held
  # Opponent instant is an EXTERNAL stipulated virtual fixture, never an
  # opponent source-deck card; do not mint one into the 100-card physical deck.
  events=[{"event":"hypothetical_opponent_noncreature_instant_on_virtual_stack",
           "actual_opponent_spell_observed":False,"kind":kind}]
  before_pilot=t.pilot
  with t.atomic():
    for land,color in payment:
      t.tap_land(land,color)
      t.mana[color]-=1
    t.transfer(uid,"hand","stack")
    t.frames.append({"kind":"spell","uid":uid,"name":OFFER,
                     "virtual_target":"opponent_noncreature_instant"})
    t.priority_events.append({"event":"physical_offer_paid_cast",
                              "physical_card":uid,
                              "sources":[{"uid":land,"name":t.cards[land]["name"],"color":color}
                                         for land,color in payment]})
  t.validate_stack()
  # Four explicit stipulated priority passes. Do not call generic resolver:
  # Cycle101 does NOT register An Offer as a resolved card.
  for seat in range(4):
    events.append({"event":"stipulated_priority_pass","seat":seat,
                   "opponent_action_modeled":False})
  with t.atomic():
    t.frames.pop()
    t.transfer(uid,"stack","graveyard")
    t.priority_seat=0;t.pass_count=0
    t.priority_events.append({"event":"bounded_offer_virtual_resolution",
         "target_still_legal":not removed_after_cast,
         "counterable":counterable,"actual_multiplayer_outcome":False})
  t.validate_stack()
  resolved=not removed_after_cast
  countered=int(resolved and counterable)
  treasures=2 if resolved else 0
  events.append({"event":"bounded_fixture_effect_resolution",
     "resolved":resolved,"virtual_target_countered":countered,
     "opponent_virtual_treasures":treasures})
  return {"physical_offer_uid":uid,"final_zone":t.zone_of(uid),
     "source_payment":[{"uid":land,"name":t.cards[land]["name"],"color":color}
                       for land,color in payment],
     "source_life_paid":before_pilot-t.pilot,
     "four_stipulated_passes":4,"resolved":resolved,"countered":countered,
     "opponent_virtual_treasures":treasures,"virtual_opponent_spell_observed":False,
     "actual_multiplayer_game":False,"events":events,
     "physical_card_total":t.receipt()["count"]}

def sample_one(library,commanders,perm,index):
  t=PriorityNonbasic(library,commanders,seed=120026,opponent_count=3)
  t.zones["library"]=[f"m{i:03d}" for i in perm]
  t.check();t.draw(7)
  seen=False;found=None;turn=None;trace=None
  for step in range(1,9):
    if step>1:t.next_turn()
    t.draw(1)
    seen|=any(t.cards[u]["name"]==OFFER for u in t.zones["hand"])
    c122.choose_land(t,OFFER)
    if eligible_offer_sources(t) is not None:
      found=copy.deepcopy(t);turn=step
      trace=source_paid_offer_fixture(t)
      break
  rows={"seen":int(seen),"eligible":int(found is not None),
        "supported_offer_resolution":int(trace is not None),
        "turn":turn,"trace":trace}
  if found is not None:
    # Each branch starts from the same physical source state; no carry-over.
    unc=source_paid_offer_fixture(copy.deepcopy(found),counterable=False)
    illegal=source_paid_offer_fixture(copy.deepcopy(found),removed_after_cast=True)
    before=fmt(found.receipt())
    blocked=0
    for kwargs in ({"kind":"creature"},{"spell_present":False},{"pilot_priority":False}):
      state=copy.deepcopy(found)
      a=fmt(state.receipt())
      try:source_paid_offer_fixture(state,**kwargs)
      except BlockedAction:
        if fmt(state.receipt())!=a:raise AssertionError("Blocked event mutated source ledger")
        blocked+=1
      else:raise AssertionError("Scripted illegal counter was accepted")
    if (blocked!=3 or fmt(found.receipt())!=before or
        unc["countered"]!=0 or unc["opponent_virtual_treasures"]!=2 or
        illegal["resolved"] or illegal["opponent_virtual_treasures"] or
        trace["countered"]!=1 or trace["opponent_virtual_treasures"]!=2):
      raise AssertionError("Virtual counter semantics drift")
    rows["uncounterable"]=unc
    rows["target_removed"]=illegal
    rows["blocked_invalid_stacks"]=blocked
  return rows

def run():
  plan,parent,reg=map(read,(PLAN,PARENT,REG))
  R=ev.Resolver()
  oracle=verify(plan,parent,reg,R)
  d=plan["deck"]
  source=ga.deck_block_text(d["slug"])
  challenger=c120.c118.replace_exact_slot(source,OFFER,JEWEL)
  base=sim.load_deck(d["slug"],R,text=source)
  alt=sim.load_deck(d["slug"],R,text=challenger)
  a,b,pairs=paired.align(base,alt,[(OFFER,JEWEL)])
  if pairs!=[(OFFER,JEWEL)] or a.N!=99 or b.N!=99:
    raise ValueError("Physical 99+1 one-slot pair mismatch")
  counts=Counter();witnesses=[]
  for i in range(1024):
    perm=random.Random(sim.seed_for(120026,i)^0x5EED).sample(range(99),99)
    v=sample_one(a.library,a.commanders,perm,i)
    counts["baseline_offer_seen"]+=v["seen"]
    counts["baseline_source_payable"]+=v["eligible"]
    counts["conditional_virtual_countered"]+=v["supported_offer_resolution"]
    if v["eligible"]:
      counts["counterable_opponent_virtual_treasures"]+=v["trace"]["opponent_virtual_treasures"]
      counts["uncounterable_not_countered"]+=int(v["uncounterable"]["countered"]==0)
      counts["uncounterable_treasures"]+=v["uncounterable"]["opponent_virtual_treasures"]
      counts["removed_target_no_treasures"]+=int(not v["target_removed"]["opponent_virtual_treasures"])
      counts["invalid_event_tests_rejected"]+=v["blocked_invalid_stacks"]
      if len(witnesses)<2:
        witnesses.append({"sample_index":i,"first_payable_turn":v["turn"],
                          "primary_offer_receipt":v["trace"],
                          "uncounterable_receipt":v["uncounterable"],
                          "target_removed_receipt":v["target_removed"]})
    # The challenger has the identical physical changed-slot draw position,
    # but the Jewel's VALUE as response is not modeled. Main-phase payable
    # access is sourced independently from the existing Cycle122 engine.
    q=c122.simulate_one(b.library,b.commanders,JEWEL,perm)
    counts["challenger_jewel_seen"]+=q["seen"]
    counts["challenger_jewel_paid_own_main"]+=q["paid"]
    if q["physical_card_count"]!=100:raise AssertionError("Physical challenger lost a card")
  if counts["baseline_offer_seen"]!=counts["challenger_jewel_seen"]:
    raise AssertionError("Paired source slot became misaligned")
  return {"schema_version":1,"cycle":123,
          "stage":"M6_CONDITIONAL_STIPULATED_OPPONENT_SPELL_NOT_GAMEPLAY",
          "preregistered_plan_sha256":sha(PLAN),"registry_sha256":sha(REG),
          "parent_nonbasic_oracle_sha256":sha(PARENT),**oracle,
          "paired_source_99_card_samples":1024,"physical_arm_views":2048,
          "deck_id":"Mai_and_Zuko","commander":"Mai and Zuko",
          "source_approved_logical_hash":d["approved_logical_hash"],
          "source_recorded_raw_sha256":d["approved_raw_sha256"],
          "swapped_one_card":[OFFER,JEWEL],
          "counts":dict(sorted(counts.items())),"source_paid_trace_witnesses":witnesses,
          "opponent_spell_instances_observed_in_actual_games":0,
          "actual_opponent_cards_or_hand_sampled":0,"simulated_game_wins":0,
          "independent_pass_c_completed":0,"phase_b_certified":False,
          "M6_accepted":False,"M7_started":False,
          "candidate_approved_or_applied":False,"canonical_decks_modified":0,
          "boundaries":["All response events are hypothetical noncreature opponent instant on a virtual stack at earliest source-payable pilot window, with every opponent passing by stipulation.",
             "Cannot estimate how often this enemy stack window occurs; no opponent strategy, resources or spell identity is sampled.",
             "Only physically held/paid An Offer is moved through pilot stack to graveyard, and its conditional counter + virtual Treasures are recorded.",
             "Jewel side uses Cycle122 payable main-phase placement only. It does not simulate additional activated abilities or flash timing of Mai and Zuko.",
             "Counterable, uncounterable, disappears-after-cast and illegal target cases establish scoped Oracle outcomes only; no upgrade verdict or gameplay win-rate."]}

def main():
  p=argparse.ArgumentParser();p.add_argument("--build",action="store_true");p.add_argument("--check",action="store_true")
  args=p.parse_args()
  if not(args.build or args.check):p.error("Use --build or --check")
  out=fmt(run())
  if args.build:OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(out,encoding="utf-8")
  if args.check and (not OUT.exists() or OUT.read_text(encoding="utf-8")!=out):
    raise ValueError("Cycle123 conditional opponent stack evidence not reproducible")
  print("Cycle123: 1024 source-paired conditional opponent spell fixtures; NO actual opponent observed, wins, Phase B, Pass C, or approvals.")
if __name__=="__main__":main()
