#!/usr/bin/env python3
"""Cycle101 read-only cross-62 stack adapter smoke run + physical Abaddon witnesses.

Each tested spell is manually retrieved from an existing physical main library
as a fixture. This is NOT sampled opening access, human play, legal interaction
probabilities, comparative win rate, M6 acceptance, or a swap recommendation.
"""
from __future__ import annotations
import argparse,hashlib,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import evaluate_decklist as ev
import grixis_sim as sim
from grixis_m6_transactional_stack import TransactionalLedger,SUPPORTED,BlockedAction
from grixis_m6_state_kernel import fingerprint

PLAN=ROOT/"data/grixis/m6/phase_b_plans/transactional_stack_62_01.json"
OUT=ROOT/"data/grixis/m6/phase_b_bounded/transactional_stack_62_01.json"
REG=ROOT/"data/grixis/registry.json"
PREV=ROOT/"data/grixis/m6/phase_b_bounded/general_state_kernel_62_01.json"
SOURCE=ROOT/"exports/grixis-archidekt/source-baseline/abaddon-the-despoiler.txt"
AUTH={"can_decide":False,"can_change_decklists":False,"can_approve_or_lock":False}
ORACLE_PHRASES={
 "Abaddon the Despoiler":["cascade","spells you cast from your hand"],
 "Kessig Flamebreather":["noncreature spell","1 damage to each opponent"],
 "Dark Ritual":["Add {B}{B}{B}."],
 "Boltwave":["3 damage to each opponent"],
 "Flame Rift":["4 damage to each player"],
 "Arcane Signet":["Add one mana of any color in your commander's color identity."]
}
TYPE={"Abaddon the Despoiler":"creature","Kessig Flamebreather":"creature",
      "Arcane Signet":"artifact","Dark Ritual":"instant","Boltwave":"sorcery",
      "Flame Rift":"sorcery"}
def read(p):return json.loads(p.read_text(encoding="utf-8"))
def digest(p):return "sha256:"+hashlib.sha256(p.read_bytes()).hexdigest()
def enc(a):return json.dumps(a,sort_keys=True,indent=2,ensure_ascii=False)+"\n"
def oracle_gate(resolver):
 rec={}
 for name,checks in ORACLE_PHRASES.items():
  s=resolver.get(name)[0];t=s.get("oracle_text") or ""
  if not t or any(check.casefold() not in t.casefold() for check in checks):
   raise ValueError("Pinned Oracle effect mismatch "+name+" actual: "+repr(t))
  if TYPE[name] not in (s.get("type_line") or "").casefold():
   raise ValueError("Pinned Oracle type mismatch "+name)
  spec=SUPPORTED[name]["cost"]
  if sim.parse_cost(s.get("mana_cost") or "")!=sim.parse_cost(spec):
   raise ValueError("Pinned Oracle cost mismatch "+name)
  rec[name]={"oracle_sha256":"sha256:"+hashlib.sha256(t.encode()).hexdigest(),
             "type_line":s["type_line"],"mana_cost":s["mana_cost"],
             "mana_value":int(s["cmc"])}
 return rec

def force_hand(t,name):
 matches=[uid for uid in t.zones["library"] if t.cards[uid]["name"]==name]
 if len(matches)!=1:raise ValueError("Required scripted unique source card absent: "+name)
 uid=matches[0]
 t.transfer(uid,"library","hand")
 t.outcome_events.append({"event":"scripted_forced_hand","id":uid,"name":name,
       "not_naturally_drawn_or_access_probability":True})
 return uid

def witness(deck,scenario):
 t=TransactionalLedger(deck.library,deck.commanders,seed=101017,opponents=(40,39,31),pilot=40)
 before=t.initial_inventory_hash
 if scenario=="commander_tax":
  if len(deck.commanders)!=1 or deck.commanders[0]["name"]!="Abaddon the Despoiler":
   raise ValueError("Wrong commander identity")
  c=t.zones["command"][0]
  t.inject_mana({"U":2,"B":2,"R":2,"C":10})
  t.cast(c,"command");t.resolve_all()
  t.commander_to_command(c)
  t.cast(c,"command");t.resolve_all()
  if t.command_casts[c]!=2 or t.zone_of(c)!="battlefield":
   raise AssertionError("Physical commander/tax state incorrect")
 elif scenario=="kessig_counter":
  k=force_hand(t,"Kessig Flamebreather")
  r=force_hand(t,"Dark Ritual")
  t.inject_mana({"R":2,"B":1,"C":1})
  t.cast(k);t.resolve_all()
  t.cast(r);t.scripted_counter_spell(r);t.resolve_all()
  if t.opponents_lost_this_turn!=3 or t.zone_of(r)!="graveyard" or t.mana["B"]!=0:
   raise AssertionError("Kessig trigger/counter order incorrect")
 elif scenario=="damage_resolution":
  b=force_hand(t,"Boltwave")
  f=force_hand(t,"Flame Rift")
  t.inject_mana({"R":3,"C":3})
  t.cast(b);t.resolve_all()
  t.cast(f);t.resolve_all()
  if t.opponents_lost_this_turn!=21 or t.pilot!=36:
   raise AssertionError("Real noncreature damage not resolved correctly")
 elif scenario=="abaddon_cascade_block":
  b=force_hand(t,"Boltwave");f=force_hand(t,"Flame Rift")
  t.inject_mana({"U":1,"B":1,"R":3,"C":5})
  c=t.zones["command"][0]
  t.cast(c,"command");t.resolve_all()
  t.cast(b);t.resolve_all()
  pre=(t.receipt(),dict(t.mana),list(t.outcome_events))
  try:t.cast(f)
  except BlockedAction as e:
   if "cascade" not in str(e):raise
  else:raise AssertionError("Active Abaddon cascade incorrectly ignored")
  if t.receipt()!=pre[0] or t.mana!=pre[1] or t.outcome_events!=pre[2]:
   raise AssertionError("Blocked cascade action mutated state")
 elif scenario=="signet":
  a=force_hand(t,"Arcane Signet")
  t.inject_mana({"C":2})
  t.cast(a);t.resolve_all()
  t.tap_signet(a,"U")
  t.next_turn()
  t.tap_signet(a,"B")
  if t.zone_of(a)!="battlefield" or t.mana["B"]!=1:
   raise AssertionError("Signet ID or mana state incorrect")
 elif scenario=="unsupported_effect":
  uid=force_hand(t,"Force of Will")
  before_receipt=t.receipt()
  try:t.cast(uid)
  except BlockedAction:pass
  else:raise AssertionError("Unsupported real Oracle card was cast")
  if before_receipt!=t.receipt():
   raise AssertionError("Blocked unsupported effect mutated physical ledger")
 else:raise ValueError("Unknown fixed scenario")
 if t.initial_inventory_hash!=before or t.initial_card_count!=100:
  raise AssertionError("Card inventory changed unexpectedly")
 t.check();t.validate_stack()
 return {"scenario":scenario,"receipt":t.receipt(),
         "opponents":t.opponents,"pilot":t.pilot,
         "opponents_lost_this_turn":t.opponents_lost_this_turn,
         "events":t.outcome_events,"physical_cards_conserved":True}

def verify():
 p=read(PLAN);reg=read(REG);previous=read(PREV)
 if (p["cycle"]!=101 or p["status"]!="preregistered_before_implementation"
     or p["authority"]!=AUTH or p["seed"]!=101017 or p["roster"]!=62
     or len(reg["decks"])!=62 or previous["roster_decks"]!=62
     or previous["total_samples"]!=248 or previous["supports_improvement_claim"]
     or reg["program"]["milestones"]["M5"]["status"]!="accepted"
     or reg["program"]["milestones"]["M6"]["accepted_by"] is not None
     or digest(SOURCE)!="sha256:5448d76193923a3f9e3d4c41a327eaeaa9c6326d484d8e5a9abaf3852db2efff"):
  raise ValueError("Cycle101 prereg authority or frozen cycle100 source drift")
 resolver=ev.Resolver()
 oracle=oracle_gate(resolver)
 prior_by_id={x["deck_id"]:x for x in previous["deck_samples"]}
 if set(prior_by_id)!=set(reg["decks"]):raise ValueError("Cycle100 roster drift")
 receipts=[];smoke_executed=0
 order=("Arcane Signet","Dark Ritual","Boltwave","Flame Rift","Kessig Flamebreather")
 for did in sorted(reg["decks"]):
  old=prior_by_id[did]
  deck=sim.load_deck(old["slug"],resolver)
  t=TransactionalLedger(deck.library,deck.commanders,seed=101017)
  if len(deck.library)+len(deck.commanders)!=100 or t.initial_card_count!=100:
   raise ValueError("Physical roster count incorrect: "+did)
  if [x["name"] for x in deck.commanders]!=old["commanders"]:
   raise ValueError("Commander identity differs: "+did)
  choice=next((n for n in order if sum(x["name"]==n for x in deck.library)==1),None)
  status="no_supported_main_spell"
  if choice:
   x=force_hand(t,choice)
   t.inject_mana({"U":3,"B":5,"R":6,"C":9})
   t.cast(x);t.resolve_all()
   if t.zone_of(x)!=("battlefield" if choice in ("Arcane Signet","Kessig Flamebreather") else "graveyard"):
    raise AssertionError("Resolved spell in wrong zone for "+did)
   smoke_executed+=1
   status="supported_fixture_cast_and_resolution"
  t.check();t.validate_stack()
  receipts.append({"deck_id":did,"slug":old["slug"],"commanders":old["commanders"],
       "physical_cards":t.initial_card_count,"ledger_inventory_hash":t.initial_inventory_hash,
       "chosen_registered_card":choice,"result":status,
       "receipt":t.receipt(),
       "artificial_mana_and_card_access":True})
  print("Cycle 101 representative",did,choice or "none",flush=True)
 if len(receipts)!=62:raise ValueError("Not all 62 represented")
 abaddon=sim.load_deck("abaddon-the-despoiler",resolver)
 scenarios=("commander_tax","kessig_counter","damage_resolution","abaddon_cascade_block",
            "signet","unsupported_effect")
 cases=[witness(abaddon,s) for s in scenarios]
 return {"schema_version":1,"cycle":101,"stage":"M6_62_roster_bounded_transactional_real_card_actions",
         "preregistration_sha256":digest(PLAN),"registry_sha256":digest(REG),
         "previous_cycle100_sha256":digest(PREV),"source_abaddon_sha256":digest(SOURCE),
         "frozen_oracle_receipts":oracle,
         "roster_cards_verified":62,"roster_fixture_casts":smoke_executed,
         "per_deck":receipts,"abaddon_witnesses":cases,
         "complete_physical_zone_conservation":True,
         "live_opponent_policy_simulated":False,"full_gameplay_simulator":False,
         "cascade_effect_execution_supported":False,
         "Phase_B_complete":False,"supports_improvement_claim":False,
         "M6_accepted":False,"authority":AUTH,
         "limitations":p["limits"]}

def main():
 parser=argparse.ArgumentParser()
 parser.add_argument("--build",action="store_true");parser.add_argument("--check",action="store_true")
 args=parser.parse_args()
 if not (args.build or args.check):parser.error("require --build/--check")
 content=enc(verify())
 if args.build:OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(content,encoding="utf-8")
 if args.check and (not OUT.is_file() or OUT.read_text(encoding="utf-8")!=content):
  raise ValueError("Cycle101 evidence not deterministic")
 print("Cycle101: source-verified, 62 physical card receipts, bounded real casts only; NO approval authority.")
if __name__=="__main__":main()
