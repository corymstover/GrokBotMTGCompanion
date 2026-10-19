#!/usr/bin/env python3
"""Cycle120: paired source-library physical-card draw exposure, not a turn/action engine.

No mulligan. Each of N identical seeded shuffles per approved 99-card source
and exact one-slot challenger reveals seven opening + one draw each own turn.
Supports exactly the nine preregistered opportunities. Cards are not cast.
"""
from __future__ import annotations
import argparse,hashlib,json,random,sys
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import evaluate_decklist as ev
import grixis_authority as ga
import grixis_sim as sim
import grixis_paired as paired
import grixis_m6_cycle118_paired_goldfish as c118
import grixis_m6_cycle119_bounded_effects as c119

PLAN=ROOT/"data/grixis/m6/phase_b_plans/cycle120_physical_access_preregistered_01.json"
REG=ROOT/"data/grixis/registry.json"
PRIOR=ROOT/"data/grixis/m6/phase_b_plans/cycle119_bounded_effect_states_preregistered_01.json"
PROTO=ROOT/"data/grixis/m6/independent_review_intake/cycle117_counterfactual_protocols_01.json"
OUT=ROOT/"data/grixis/m6/phase_b_bounded/cycle120_physical_access_pairs_01.json"
AUTH={"can_apply_deck_swaps":False,"can_modify_approved_lists":False,
      "can_certify_M6":False,"can_claim_effect_aware_paired_gameplay":False,"can_issue_pass_c":False}
EXPECTED={
"Gwendlyn_Di_Corci":("gwendlyn-di-corci","Opposition Agent","Aphetto Alchemist"),
"Nicol_Bolas__the_Ravager":("nicol-bolas-the-ravager","Mox Diamond","Aetheric Amplifier"),
"Mai_and_Zuko":("mai-and-zuko","An Offer You Can't Refuse","The Enigma Jewel // Locus of Enlightenment")
}
BASICS={"Plains","Island","Swamp","Mountain","Forest","Wastes"}
def load(p):return json.loads(Path(p).read_text(encoding="utf-8"))
def digest(p):return "sha256:"+hashlib.sha256(Path(p).read_bytes()).hexdigest()
def encode(x):return json.dumps(x,sort_keys=True,ensure_ascii=False,indent=2)+"\n"

def verify_plan(p,reg,old,proto):
  cfg=p["sampling"]
  if (p["schema_version"]!=1 or p["cycle"]!=120 or p["status"]!="preregistered_before_result_generation"
      or p["authority"]!=AUTH or p["base_head_sha"]!="7031fa408befb8130a6469a84ec1465a018ba836"
      or cfg["seed"]!=120026 or cfg["samples_per_deck"]!=8192 or cfg["turns"]!=8
      or cfg["opening_hand"]!=7 or cfg["draws_per_turn"]!=1 or cfg["allow_mulligans"] is not False
      or cfg["checkpoints"]!=[4,8] or cfg["return_example_physical_witnesses"]!=2
      or set(EXPECTED)!={x["deck_id"] for x in p["studies"]}
      or old["cycle"]!=119 or proto["cycle"]!=117 or proto["observed_game_results"]!=[]
      or len(reg["decks"])!=62 or reg["program"]["milestones"]["M6"]["status"]!="in_progress"
      or reg["program"]["milestones"]["M6"]["accepted_by"] is not None
      or any(reg["program"]["milestones"][f"M{i}"]["status"]!="accepted" for i in range(6))):
    raise ValueError("Preregistered physical source sampling gates not met")
  oldids={x["deck_id"]:x for x in old["studies"]}
  srcids={x["deck_id"]:x for x in proto["protocols"]}
  expectedopps={
    "Gwendlyn_Di_Corci":["gwendlyn-alchemist-activation-access","gwendlyn-shroud-overlap","gwendlyn-agent-search-response-access"],
    "Nicol_Bolas__the_Ravager":["ravager-mox-spare-land-opening","ravager-amplifier-access","ravager-mox-spare-land-through-turn8"],
    "Mai_and_Zuko":["mai-jewel-restriction-access","mai-jewel-basalt-rings-access","mai-offer-counterspell-access"]
  }
  for x in p["studies"]:
    did=x["deck_id"]
    slug,cut,add=EXPECTED[did]
    e=reg["decks"][did]
    oldx=oldids[did]
    prior=srcids[did]
    if (x["slug"]!=slug or x["cut"]!=cut or x["add"]!=add or x["commander"]!=e["commanders"][0]
        or e["commanders"]!=oldx["commander"] or e["source"]["recorded_sha256"]!=x["approved_raw_sha256"]
        or e["source"]["recorded_matches_raw"] is not True or
        e["current_canonical_hash"]!=x["approved_logical_hash"] or
        x["source_file"]!=e["source"]["path"] or
        oldx["source_logical_hash"]!=x["approved_logical_hash"] or
        x["swap_id"]!=oldx["swap_id"] or
        (prior["baseline"],prior["candidate"],prior["source_swap_id"])!=(cut,add,x["swap_id"])):
      raise ValueError("Source/candidate/approved hash drift: "+did)
    ops=x["opportunities"]
    if len(ops)!=3 or [a["id"] for a in ops]!=expectedopps[did]:
      raise ValueError("Opportunity registration drift: "+did)
    for op in ops:
      if op["arm"] not in ("baseline","candidate") or not op["meaning"] or
          not op["required_main"] or len(op["required_main"])!=len(set(op["required_main"])):
        raise ValueError("Unregistered, missing or duplicate opportunity requirements")
      if op.get("extra_requirement") not in (None,"at_least_one_other_land_in_opening_seven","at_least_one_other_land_in_seen"):
        raise ValueError("Unknown optional source condition")

def verify_exact_pair(p,R):
  original=ga.deck_block_text(p["slug"])
  if ga.text_hash(original,R)!=p["approved_logical_hash"]:
    raise ValueError("Source 99+commander logical approval mismatch")
  alttext=c118.replace_exact_slot(original,p["cut"],p["add"])
  original_deck=sim.load_deck(p["slug"],R,text=original)
  alt_deck=sim.load_deck(p["slug"],R,text=alttext)
  champion,challenger,pairs=paired.align(original_deck,alt_deck,[(p["cut"],p["add"])])
  if pairs!=[(p["cut"],p["add"])]:
    raise ValueError("Physical one-slot pair differs from M5 registration")
  if (champion.N!=99 or challenger.N!=99 or len(champion.commanders)!=1 or
      len(challenger.commanders)!=1 or champion.commanders[0]["name"]!=p["commander"] or
      challenger.commanders[0]["name"]!=p["commander"]):
    raise ValueError("Physical source and challenger are not 99+one commander")
  a=[c["name"] for c in champion.library]
  b=[c["name"] for c in challenger.library]
  differences=[i for i in range(99) if a[i]!=b[i]]
  if len(differences)!=1 or (a[differences[0]],b[differences[0]])!=(p["cut"],p["add"]):
    raise ValueError("Physical challenger changes another card or cannot align")
  if Counter(a)[p["cut"]]!=1 or Counter(b)[p["add"]]!=1 or Counter(a)[p["add"]] or Counter(b)[p["cut"]]:
    raise ValueError("Card identity/singleton violation")
  if any(n!=b[i] for i,n in enumerate(a) if i!=differences[0]):
    raise ValueError("Common 98 source slots no longer align")
  for names in (a,b):
    if any(v>1 and card not in BASICS for card,v in Counter(names).items()):
      raise ValueError("Nonbasic singleton violated")
  for op in p["opportunities"]:
    included=Counter(a if op["arm"]=="baseline" else b)
    if any(included[c]!=1 for c in op["required_main"]):
      raise ValueError("Required source card missing or duplicate in "+op["id"])
  return a,b,differences[0],original

def sampled(draw_indices,names,op,checkpoint,landflags):
  limit=7+checkpoint
  indices=draw_indices[:limit]
  present={names[i] for i in indices}
  if not set(op["required_main"])<=present:return False
  req=op.get("extra_requirement")
  if req=="at_least_one_other_land_in_opening_seven":
    if op["required_main"][0] not in {names[i] for i in draw_indices[:7]}:return False
    return any(landflags[i] for i in draw_indices[:7])
  if req=="at_least_one_other_land_in_seen":
    return any(landflags[i] for i in indices)
  return True

def witness(draw_indices,names,op,turn,seed,index):
  required=set(op["required_main"])
  observed=[]
  for j,i in enumerate(draw_indices[:7+turn]):
    if names[i] in required:
      observed.append({"physical_uid":f"m{i:03d}","name":names[i],
                       "position_in_sample":j+1,
                       "first_seen_turn":0 if j<7 else j-6,
                       "draw_zone":"opening" if j<7 else "draw_step"})
  if {x["name"] for x in observed}!=required:raise ValueError("Invalid physical witness")
  return {"sample_index":index,"seed_used":seed,"checkpoint_turn":turn,
          "source_card_ids":observed,
          "source_libraries_untouched":True,"assumed_cast_and_mana_payments":False,
          "conditional_prior_cycle119_state_does_not_follow_from_draw":True}

def sample_one(p,R,config):
  a,b,slot,original=verify_exact_pair(p,R)
  n=config["samples_per_deck"];seed=config["seed"]
  names={"baseline":a,"candidate":b}
  lands={arm:[sim.load_deck(p["slug"],R,
         text=(original if arm=="baseline" else c118.replace_exact_slot(original,p["cut"],p["add"]))).library[i]["land"]
         for i in range(0)] for arm in []} # no mutation; create aligned flags from frozen Oracle
  # Same physical index alignment from paired.align; all cards carry their printed land indicator.
  # Infer land from frozen resolution only, never treating Mox Diamond as a land.
  info={name:bool("Land" in (R.get(name)[0].get("card_faces",[R.get(name)[0]])[0].get("type_line","")
                        if name in {"Mox Diamond","The Enigma Jewel // Locus of Enlightenment"} else
                         "Land" in (R.get(name)[0].get("type_line") or R.get(name)[0].get("card_faces",[R.get(name)[0]])[0].get("type_line","")))
        for name in set(a)|set(b)}
  landflags={arm:[info[name] for name in names[arm]] for arm in ("baseline","candidate")}
  counts={op["id"]:{turn:0 for turn in config["checkpoints"]} for op in p["opportunities"]}
  examples={op["id"]:[] for op in p["opportunities"]}
  paired_slot_checks={turn:0 for turn in config["checkpoints"]}
  common_support_checks=0
  for index in range(n):
    s=sim.seed_for(seed,index)
    perm=random.Random(s^0x5EED).sample(range(99),99)
    for turn in config["checkpoints"]:
      indices=perm[:7+turn]
      slot_seen=slot in indices
      # Candidate and baseline source slot are the same physical position/shuffle.
      if (p["cut"] in {a[i] for i in indices}) != (p["add"] in {b[i] for i in indices}):
        raise ValueError("Physical paired one-slot access alignment changed")
      paired_slot_checks[turn]+=int(slot_seen)
    if index==0 and any(a[i]!=b[i] for i in perm if i!=slot):
      raise ValueError("Common physical source/variant slot changed")
    for op in p["opportunities"]:
      arm=op["arm"]
      for turn in config["checkpoints"]:
        if sampled(perm,names[arm],op,turn,landflags[arm]):
          counts[op["id"]][turn]+=1
          if turn==8 and len(examples[op["id"]])<config["return_example_physical_witnesses"]:
            examples[op["id"]].append(witness(perm,names[arm],op,turn,s,index))
  records=[]
  for op in p["opportunities"]:
    seen=[]
    for turn in config["checkpoints"]:
      k=counts[op["id"]][turn]
      prob,ci=sim.wilson(k,n)
      seen.append({"through_turn":turn,"matching_physical_samples":k,
                   "total_physical_samples":n,"fraction":round(prob,6),
                   "wilson95":[round(v,6) for v in ci]})
    records.append({"id":op["id"],"arm":op["arm"],"required_cards":op["required_main"],
                    "extra_requirement":op.get("extra_requirement"),
                    "sample_exposure":seen,"physical_examples":examples[op["id"]],
                    "conditional_rule_witness_not_a_deployment_result":True,
                    "interpretation":op["meaning"]})
  match_byturn={str(t):{"matched_seen_counts":paired_slot_checks[t],
                       "probability":round(paired_slot_checks[t]/n,6)} for t in config["checkpoints"]}
  return {"deck_id":p["deck_id"],"commander":p["commander"],
          "registered_approved_raw_sha256":p["approved_raw_sha256"],
          "approved_logical_hash":p["approved_logical_hash"],
          "source_markdown_sha256":"sha256:"+hashlib.sha256(original.encode()).hexdigest(),
          "physical_main_cards":99,"command_zone_cards":1,
          "one_different_main_slot_uid":f"m{slot:03d}",
          "shared_physical_card_slots":98,
          "registered_swap":[p["cut"],p["add"]],
          "paired_card_slot_seen_identically_at_every_checkpoint":match_byturn,
          "source_access_opportunities":records,
          "expected_probability_for_one_specific_physical_card_by_turn8":round(15/99,6),
          "legally_castable_or_resolved_combos_proven":0,
          "real_game_win_rate_or_improvement_claim":False}

def run():
  p,reg,old,proto=map(load,(PLAN,REG,PRIOR,PROTO))
  verify_plan(p,reg,old,proto)
  R=ev.Resolver()
  row=[sample_one(x,R,p["sampling"]) for x in p["studies"]]
  return {"schema_version":1,"cycle":120,
          "stage":"M6_REAL_99_CARD_PAIRED_PHYSICAL_ACCESS_NOT_EFFECT_AWARE_GAMEPLAY",
          "plan_sha256":digest(PLAN),"registry_sha256":digest(REG),
          "prior_cycle119_sha256":digest(PRIOR),"protocol_sha256":digest(PROTO),
          "model_source_sha256":sim.model_sha256(),
          "draw_policy":"no mulligan, 7 opening + 1 draw each turn including T1; no tutors or other card draws",
          "seed":120026,"physical_samples_per_deck":8192,
          "total_paired_physical_shuffles":24576,"total_arm_sample_views":49152,
          "paired_results":row,"number_of_preregistered_source_opportunities":9,
          "source_bound_rule_event_actions_actually_executed_in_sampling":0,
          "previously_executed_cycle119_conditional_scenario_types":6,
          "independent_pass_c":0,"phase_b_certified":False,
          "real_multiplayer_games":0,"owner_approved_swaps":0,"canonical_decks_modified":0,
          "M6_accepted":False,"all_62_current_legality_recataloged":False,
          "limitations":p["limitations"],"authority":AUTH}

def main():
  cmd=argparse.ArgumentParser()
  cmd.add_argument("--build",action="store_true")
  cmd.add_argument("--check",action="store_true")
  args=cmd.parse_args()
  if not(args.build or args.check):cmd.error("use --build or --check")
  record=encode(run())
  if args.build:OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(record,encoding="utf-8")
  if args.check and (not OUT.exists() or OUT.read_text(encoding="utf-8")!=record):
    raise ValueError("Cycle120 paired physical source access result is not reproducible")
  print("Cycle120: 24576 paired physical shuffles and 9 source-access conditions verified; NO legal game-play outcome, Phase B, Pass C or approval.")
if __name__=="__main__":main()
