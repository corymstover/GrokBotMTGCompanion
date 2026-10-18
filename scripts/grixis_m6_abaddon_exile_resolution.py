#!/usr/bin/env python3
"""Cycle109: narrow REAL cascade exile casts from original physical Abaddon deck.

Only Sol Ring, Mana Vault, Demonic Tutor and Vampiric Tutor are fully offered,
cast without mana, and resolved. Other actual offers remain declined/UNKNOWN.
No comprehensive Magic engine, opponent decisions or deck superiority inference.
"""
from __future__ import annotations
import argparse,copy,hashlib,json,random,sys
from collections import Counter
from contextlib import contextmanager
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import evaluate_decklist as ev
import grixis_sim as sim
from grixis_m6_abaddon_blast_target_cascade import BlastCascade
from grixis_m6_abaddon_physical_slot import slot_in_hand,sources_can_pay
from grixis_m6_fetch_city_tomb import MODEL_LANDS,FETCHES
from grixis_m6_state_kernel import BlockedAction

PLAN=ROOT/"data/grixis/m6/phase_b_plans/abaddon_exile_resolution_01.json"
C107=ROOT/"data/grixis/m6/phase_b_bounded/abaddon_blast_target_cascade_01.json"
C108=ROOT/"data/grixis/m6/phase_b_bounded/abaddon_cascade_offer_triage_01.json"
SOURCE=ROOT/"exports/grixis-archidekt/source-baseline/abaddon-the-despoiler.txt"
REG=ROOT/"data/grixis/registry.json"
OUT=ROOT/"data/grixis/m6/phase_b_bounded/abaddon_exile_resolution_01.json"
SHORT=ROOT/"data/grixis/m6/phase_b_bounded/abaddon_exile_resolution_summary_01.json"
AUTH={"can_change_decklists":False,"can_approve_or_lock":False,
      "can_decide":False,"can_certify_M6":False}
ROLE={
 "Sol Ring":{"cost":"{1}","type":"Artifact",
   "oracle":["{T}: Add {C}{C}."],"amount":2},
 "Mana Vault":{"cost":"{1}","type":"Artifact",
   "oracle":["{T}: Add {C}{C}{C}.","doesn't untap"],"amount":3},
 "Demonic Tutor":{"cost":"{1}{B}","type":"Sorcery",
   "oracle":["Search your library for a card, put that card into your hand, then shuffle."],
   "destination":"hand"},
 "Vampiric Tutor":{"cost":"{B}","type":"Instant",
   "oracle":["Search your library for a card, then shuffle and put that card on top.","You lose 2 life."],
   "destination":"top"}
}
TUTOR_ORDER=("Boltwave","Flame Rift","Kessig Flamebreather","Dark Ritual","Arcane Signet")
def load(p):return json.loads(p.read_text(encoding="utf-8"))
def sha(p):return "sha256:"+hashlib.sha256(p.read_bytes()).hexdigest()
def dump(j):return json.dumps(j,sort_keys=True,ensure_ascii=False,indent=2)+"\n"

def oracle_gate(res):
 out={}
 for name,v in ROLE.items():
  src=res.get(name)[0];actual=src.get("oracle_text") or ""
  if (src.get("name")!=name or v["type"].casefold() not in (src.get("type_line") or "").casefold()
      or sim.parse_cost(src.get("mana_cost") or "")!=sim.parse_cost(v["cost"])):
   raise ValueError("Frozen Oracle identity/cost/type incorrect for "+name)
  if any(q.casefold() not in actual.casefold() for q in v["oracle"]):
   raise ValueError("Frozen Oracle effect clause missing for "+name+": "+repr(actual))
  out[name]={"oracle_sha256":"sha256:"+hashlib.sha256(actual.encode()).hexdigest(),
    "mana_cost":src.get("mana_cost"),"type_line":src.get("type_line")}
 return out

class ActualCascade(BlastCascade):
 def __init__(self,*a,**k):
  super().__init__(*a,**k)
  self.executed_hits=[]
  self.unknown_hits=[]
  self.hit_cascade_triggers_created=0
  self.available_mana_unspent_after_rock=0

 @contextmanager
 def atomic(self):
  fields=("executed_hits","unknown_hits","hit_cascade_triggers_created",
          "available_mana_unspent_after_rock")
  prior={k:copy.deepcopy(getattr(self,k)) for k in fields}
  try:
   with super().atomic():yield
  except Exception:
   for k,v in prior.items():setattr(self,k,v)
   raise

 def _cascade_offer(self,frame):
  exiled=[]
  eligible=None
  while self.zones["library"]:
   uid=self.zones["library"][0]
   self.transfer(uid,"library","exile")
   exiled.append(uid)
   if not self.cards[uid].get("land",False) and self.cards[uid]["mv"]<frame["mv"]:
    eligible=uid
    break
  name=self.cards[eligible]["name"] if eligible else None
  chosen=bool(name in ROLE)
  if chosen:
   if self.cards[eligible]["cost"]!=sim.parse_cost(ROLE[name]["cost"]):
    raise BlockedAction("Wrong printed cost at actual cascade hit")
   # The cascade permission casts the hit *during resolution* even if it is
   # a sorcery or artifact. It is from EXILE not HAND: Abaddon grants NO cascade.
   self.transfer(eligible,"exile","stack")
   self.frames.append({"kind":"spell","name":name,"uid":eligible,
       "origin":"cascade_exile","cast_without_mana":True})
   self.executed_hits.append({"name":name,"uid":eligible,
       "offered_from":"exile","real_physical_cast":True,
       "mana_paid":0,"resolved":False,"result":None,
       "new_Abaddon_hand_cascade_triggers":0})
  else:
   if eligible is not None:
    self.unknown_hits.append({"name":name,"uid":eligible,
       "decision":"decline_optional_cast","potential_value":"UNKNOWN_NOT_ZERO"})
  self.cascade_offers.append({"trigger":frame["why"],"eligible_uid":eligible,
     "eligible_name":name,"eligible_mv":self.cards[eligible]["mv"] if eligible else None,
     "revealed_physical_ids":list(exiled),"number_of_revealed":len(exiled),
     "controller_choice":"cast_from_exile" if chosen else "decline_optional_cast",
     "potential_if_declined":"UNKNOWN_NOT_ZERO" if eligible and not chosen else None,
     "actual_effect_kind":"SUPPORTED_SOURCE_VERIFIED" if chosen else "UNMODELED",
     "new_hand_only_cascade":0})
  self.cascade_resolved+=1
  # Leave the just-cast physical hit on stack, return ALL other exiled cards
  # to library bottom in deterministic randomized order.
  remaining=[u for u in exiled if u!=eligible or not chosen]
  random.Random(self.seed ^ (self.cascade_resolved*0x9e3779b1)).shuffle(remaining)
  for uid in remaining:self.transfer(uid,"exile","library")
  return self.cascade_offers[-1]

 def _choose_tutor_target(self):
  for name in TUTOR_ORDER:
   for uid in self.zones["library"]:
    if self.cards[uid]["name"]==name:return uid
  return next(iter(self.zones["library"]),None)

 def _resolve_exile_spell(self,frame):
  uid=frame["uid"];name=frame["name"]
  if self.zone_of(uid)!="stack":raise AssertionError("Expected cast-from-exile spell on physical stack")
  rec=next(v for v in self.executed_hits if v["uid"]==uid and not v["resolved"])
  destination="battlefield" if name in ("Sol Ring","Mana Vault") else "graveyard"
  if name in ("Demonic Tutor","Vampiric Tutor"):
   selected=self._choose_tutor_target()
   selected_name=self.cards[selected]["name"] if selected is not None else None
   if selected is not None:self.transfer(selected,"library","exile")
   rng=random.Random(self.seed ^ (self.cascade_resolved*0x517cc1b7))
   rng.shuffle(self.zones["library"])
   if selected is not None:
    self.transfer(selected,"exile","hand" if name=="Demonic Tutor" else "library",
                  to_top=name=="Vampiric Tutor")
   if name=="Vampiric Tutor":
    if self.pilot<=2:raise BlockedAction("Lethal Vampiric life loss unsupported")
    self.pilot-=2
   rec["result"]={"chosen_from_physical_library":selected_name,
     "chosen_uid":selected,"destination":"hand" if name=="Demonic Tutor" else "top_of_library",
     "library_shuffled":True,"controller_life_paid":2 if name=="Vampiric Tutor" else 0,
     "access_to_selected_card":"now_in_hand" if name=="Demonic Tutor" else "requires_real_future_draw",
     "chosen_policy":"first available from frozen tutor priority"}
  else:
   rec["result"]={"artifact_entered":True,"colorless_per_tap":ROLE[name]["amount"],
     "no_automatic_legal_follow_up_spell":True}
  self.transfer(uid,"stack",destination)
  rec["destination"]=destination
  rec["resolved"]=True

 def _tap_resolved_rock(self):
  # Fixed optional bookkeeping policy: tap cast artifact immediately after
  # resolving on own turn if there is a priority window. Generated mana is
  # real in this bounded turn but NOT proof of a payable useful hand spell.
  for e in self.executed_hits:
   if not e["resolved"] or e["name"] not in ("Sol Ring","Mana Vault") or e.get("rock_tapped"):
    continue
   uid=e["uid"]
   if self.zone_of(uid)!="battlefield" or uid in self.tapped:continue
   self.tapped.add(uid)
   amount=ROLE[e["name"]]["amount"]
   self.mana["C"]+=amount
   self.available_mana_unspent_after_rock+=amount
   e["rock_tapped"]=True;e["colorless_mana_generated"]=amount
   e["colorless_mana_consumed_in_a_followup_spell"]=0
   self.check()

 def pass_priority(self):
  if self.frames and self.frames[-1]["kind"]=="spell" and self.frames[-1].get("origin")=="cascade_exile":
   with self.atomic():
    seat=self.priority_seat
    self.pass_count+=1;self.priority_seat=(seat+1)%4
    self.priority_events.append({"event":"priority_pass","seat":seat,
      "consecutive":self.pass_count})
    if self.pass_count==4:
     frame=self.frames.pop()
     self._resolve_exile_spell(frame)
     self.priority_events.append({"event":"four_passes_resolve_top",
       "name":frame["name"],"kind":"spell","origin":"cascade_exile"})
     self.pass_count=0;self.priority_seat=0
     self._tap_resolved_rock()
    self.validate_stack()
   return self.priority_seat
  return super().pass_priority()

def one_trial(library,commanders,seed,turns,removal):
 t=ActualCascade(library,commanders,seed=seed,opponents=(40,39,31),pilot=40)
 opening=t.drawn_names(t.draw(7))
 draw_names=[]
 for turn in range(1,turns+1):
  if turn>1:t.next_turn()
  draw=t.draw(1)[0];draw_names.append(t.cards[draw]["name"])
  land=next((u for u in t.zones["hand"] if
      t.cards[u].get("land") and t.cards[u]["name"] in MODEL_LANDS),None)
  if land is not None:
   land_name=t.cards[land]["name"]
   t.play_supported_land(land)
   if land_name in FETCHES and t.pilot>1:
    t.activate_fetch(land);t.resolve_by_passes()
  if t.command_casts.get("c000",0)==0:
   try:t.cast_with_land_sources("c000","command")
   except BlockedAction:pass
   else:t.resolve_by_passes()
  blast=slot_in_hand(t)
  if not t.blast_cast and blast is not None:
   try:t.cast_with_land_sources(blast)
   except BlockedAction:pass
   else:
    if removal:
     t.pass_priority();t.externally_remove_target()
    t.resolve_by_passes()
  t.check();t.validate_stack()
 if sum(t.receipt()["zone_counts"].values())!=100 or t.zones["exile"] or t.zones["stack"]:
  raise AssertionError("Physical card conservation or stranded zone after real cascade")
 if any(not q["resolved"] for q in t.executed_hits):
  raise AssertionError("A supported physical cascade spell did not resolve")
 return {"seed":seed,"opening":opening,"draws":draw_names,
   "blast_cast":t.blast_cast,"blast_resolution":t.blast_resolution,
   "cascade_offers":t.cascade_offers,
   "executed_hit_spells":t.executed_hits,
   "declined_unknown_hits":t.unknown_hits,
   "generated_rock_mana_not_spent_in_followup":t.available_mana_unspent_after_rock,
   "commander_present_at_end":any(t.cards[u]["name"]=="Abaddon the Despoiler" for u in t.zones["battlefield"]),
   "initial_inventory":t.initial_inventory_hash,"zone_counts":t.receipt()["zone_counts"],
   "trigger_count":t.cascade_triggers,"triggers_resolved":t.cascade_resolved,
   "new_Abaddon_cascades_from_exile":t.hit_cascade_triggers_created}

def run():
 plan=load(PLAN);prior=load(C107);audit=load(C108);reg=load(REG)
 if (plan["cycle"]!=109 or plan["status"]!="preregistered_before_implementation"
    or plan["authority"]!=AUTH or plan["seed"]!=106017 or plan["samples"]!=240
    or plan["effect_whitelist"]!=["Mana Vault","Sol Ring","Demonic Tutor","Vampiric Tutor"]
    or sha(SOURCE)!="sha256:"+plan["source_export_sha256"]
    or prior["approved_sha256"]!=plan["approved_raw_sha256"]
    or audit["paired_seeds"]!=240 or audit["relative_value"]!="CANNOT_EVALUATE"
    or len(reg["decks"])!=62 or reg["program"]["milestones"]["M6"]["status"]!="in_progress"):
  raise ValueError("Cycle109 prereg, source or M6 authority drift")
 resolver=ev.Resolver()
 oracle=oracle_gate(resolver)
 deck=sim.load_deck("abaddon-the-despoiler",resolver)
 if len(deck.library)!=99 or len(deck.commanders)!=1:raise ValueError("Approved source not 99+1")
 cases={}
 for policy in plan["scenarios"]:
  rec=[];tot=Counter();by_name=Counter();unknown=Counter()
  for index,old in enumerate(prior["policies"][policy]["trials"]):
   seed=sim.seed_for(plan["seed"],index)
   trial=one_trial(deck.library,deck.commanders,seed,plan["turns"],
     policy=="target_removed_after_cast")
   if trial["seed"]!=old["seed"] or trial["opening"]!=old["opening"]:
    raise ValueError("Paired opening drift compared to Cycle107")
   if bool(trial["blast_cast"])!=bool(old["blast_cast"]):
    raise ValueError("Paired Blast-cast opportunity changed")
   if trial["blast_cast"]:
    if len(trial["cascade_offers"])!=len(old["offers"]):
     raise ValueError("Printed cascade offer count drift")
    for now,then in zip(trial["cascade_offers"],old["offers"]):
     for field in ("eligible_uid","eligible_name","number_of_revealed"):
      if now[field]!=then[field]:raise ValueError("Cascade offer identity drift: "+field)
   for hit in trial["executed_hit_spells"]:
    tot["actual_spell_resolutions"]+=1
    by_name[hit["name"]]+=1
    if hit["name"] in ("Sol Ring","Mana Vault"):tot["mana_rocks_resolved"]+=1
    if hit["name"] in ("Demonic Tutor","Vampiric Tutor"):tot["tutors_resolved"]+=1
   unknown.update(x["name"] for x in trial["declined_unknown_hits"])
   tot["real_Blast_casts"]+=int(trial["blast_cast"])
   tot["eligible_offers"]+=len(trial["cascade_offers"])
   tot["unknown_offers_declined"]+=len(trial["declined_unknown_hits"])
   tot["colorless_mana_generated_but_unspent"]+=trial["generated_rock_mana_not_spent_in_followup"]
   tot["supported_cascade_from_exile_granted_again"]+=trial["new_Abaddon_cascades_from_exile"]
   rec.append(trial)
  if tot["real_Blast_casts"]!=7 or tot["eligible_offers"]!=7:
   raise ValueError("Expected exact same seven printed cascade opportunities")
  cases[policy]={"counts":dict(sorted(tot.items())),
    "executed_hit_names":dict(sorted(by_name.items())),
    "declined_unknown_names":dict(sorted(unknown.items())),
    "samples":rec}
  print("Cycle109",policy,tot,dict(by_name),dict(unknown),flush=True)
 for left,right in zip(cases[plan["scenarios"][0]]["samples"],cases[plan["scenarios"][1]]["samples"]):
  if left["opening"]!=right["opening"] or left["executed_hit_spells"]!=right["executed_hit_spells"]:
   raise ValueError("Scripted Blast target removal changed independent printed cascade hit behavior")
 return {"schema_version":1,"cycle":109,"stage":"M6_Abaddon_real_four_card_cascade_exile_spell_resolution",
   "plan_sha256":sha(PLAN),"previous_cycle107_sha256":sha(C107),
   "previous_cycle108_sha256":sha(C108),"approved_source_sha256":sha(SOURCE),
   "approved_raw_sha256":plan["approved_raw_sha256"],
   "oracle_checks":oracle,"sample_count":plan["samples"],
   "two_target_response_policies":cases,
   "actual_cascade_from_exile_spells_can_resolve":True,
   "four_card_effect_subset_only":True,
   "realized_downstream_deck_win_value":"UNKNOWN_NOT_ZERO",
   "three_deferred_effects":["Windfall","Chrome Mox","Deflecting Swat"],
   "full_multiplayer_gameplay":False,"balanced_three_variant_phase_b":False,
   "comparative_deck_strength":"CANNOT_EVALUATE",
   "supports_improvement_claim":False,"zero_improvement_certified":False,
   "full_phase_b_complete":False,"independent_pass_c_complete":False,
   "M6_accepted":False,"authority":AUTH}
def compact(x):
 return {"cycle":109,"sample_count":x["sample_count"],
  "per_policy":{k:{"counts":v["counts"],"executed_hit_names":v["executed_hit_names"],
     "declined_unknown_names":v["declined_unknown_names"]} for k,v in x["two_target_response_policies"].items()},
  "full_effect_comparison":False,"relative_deck_strength":x["comparative_deck_strength"],
  "approved":False,"M6_accepted":False}
def main():
 p=argparse.ArgumentParser();p.add_argument("--build",action="store_true");p.add_argument("--check",action="store_true")
 a=p.parse_args()
 if not(a.build or a.check):p.error("require --build/--check")
 o=run();txt=dump(o);small=dump(compact(o))
 if a.build:
  OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(txt,encoding="utf-8");SHORT.write_text(small,encoding="utf-8")
 if a.check and (not OUT.exists() or OUT.read_text(encoding="utf-8")!=txt or not SHORT.exists() or SHORT.read_text(encoding="utf-8")!=small):
  raise ValueError("Cycle109 deterministic actual-hit replay differs")
 print("Cycle109 source-verified real cascade exile resolution; downstream game impact UNKNOWN.")
if __name__=="__main__":main()
