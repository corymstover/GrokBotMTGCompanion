#!/usr/bin/env python3
"""Cycle121 source-locked physical-basic-mana paid-cast witnesses.

Not a full MTG rules engine. No opponents, nonbasic mana, tutors, ability
resolution, commander cast, card utility or win-rate interpretation.
"""
from __future__ import annotations
import argparse, hashlib, json, random, sys
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import evaluate_decklist as ev
import grixis_authority as ga
import grixis_sim as sim
import grixis_m6_cycle120_physical_access as c120

PLAN=ROOT/"data/grixis/m6/phase_b_plans/cycle121_source_paid_cast_prereg_01.json"
REG=ROOT/"data/grixis/registry.json"
PRIOR=ROOT/"data/grixis/m6/phase_b_plans/cycle120_physical_access_preregistered_01.json"
OUT=ROOT/"data/grixis/m6/phase_b_bounded/cycle121_source_paid_basic_casts_01.json"
BASIC={"Island":"U","Swamp":"B","Mountain":"R","Plains":"W","Forest":"G","Wastes":"C"}
COST={
 "Opposition Agent":(2,{"B":1}),
 "Aphetto Alchemist":(1,{"U":1}),
 "Aetheric Amplifier":(3,{}),
 "The Enigma Jewel // Locus of Enlightenment":(1,{}),
 "An Offer You Can't Refuse":(0,{"U":1})}
EXPECTED={
 "Gwendlyn_Di_Corci":("Opposition Agent","Aphetto Alchemist"),
 "Nicol_Bolas__the_Ravager":("Mox Diamond","Aetheric Amplifier"),
 "Mai_and_Zuko":("An Offer You Can't Refuse","The Enigma Jewel // Locus of Enlightenment")}
class Blocked(ValueError):pass
def read(p):return json.loads(Path(p).read_text(encoding="utf-8"))
def sha(p):return "sha256:"+hashlib.sha256(Path(p).read_bytes()).hexdigest()
def encode(x):return json.dumps(x,ensure_ascii=False,sort_keys=True,indent=2)+"\n"

def verify_plan(p,reg,prior,R):
 if (p["cycle"]!=121 or p["status"]!="preregistered_before_ci" or
     p["sample_count_per_deck"]!=1024 or p["seed"]!=120026 or p["turns"]!=8 or
     p["no_mulligans"] is not True or len(p["studies"])!=3 or
     reg["program"]["milestones"]["M6"]["status"]!="in_progress" or
     len(reg["decks"])!=62 or prior["cycle"]!=120 or
     any(v!=0 and v is not False for v in p["approval"].values()) or
     set(EXPECTED)!={s["deck_id"] for s in p["studies"]}):
  raise Blocked("Source authority or frozen preregistration drift")
 old={s["deck_id"]:s for s in prior["studies"]}
 for st in p["studies"]:
  did=st["deck_id"]
  approved=reg["decks"][did]
  o=old[did]
  if (st["slug"]!=approved["slug"] or st["commander"]!=approved["commanders"][0] or
      (st["cut"],st["add"])!=EXPECTED[did] or
      (st["cut"],st["add"],st["swap_id"])!=(o["cut"],o["add"],o["swap_id"]) or
      st["approved_logical_hash"]!=approved["current_canonical_hash"] or
      st["approved_logical_hash"]!=o["approved_logical_hash"] or
      st["approved_raw_sha256"]!=approved["source"]["recorded_sha256"] or
      approved["source"]["recorded_matches_raw"] is not True):
    raise Blocked("M5/authority/card identity source drift: "+did)
  if ga.text_hash(ga.deck_block_text(st["slug"]),R)!=st["approved_logical_hash"]:
    raise Blocked("Physical approved decklist logical hash drift")
 for name, (generic,pips) in COST.items():
  c=R.get(name)[0]
  f=c["card_faces"][0] if c.get("card_faces") else c
  observed=sim.parse_cost(f.get("mana_cost"))
  if (observed["generic"]!=generic or observed["life"] or
      Counter(next(iter(x)) for x in observed["pips"])!=Counter(pips)):
   raise Blocked("Frozen Oracle printed mana cost differs from simple witness: "+name)
 jewel=R.get("The Enigma Jewel // Locus of Enlightenment")[0]
 if "enters tapped" not in jewel["card_faces"][0]["oracle_text"].lower():
  raise Blocked("Jewel tapped entry rule is missing from frozen Oracle")
 mox=R.get("Mox Diamond")[0]
 if "discard a land card" not in mox["oracle_text"].lower():
  raise Blocked("Mox requires discard replacement Oracle guard")

def pay(mana,cost):
 g,pips=cost
 pool=Counter(mana)
 for color,n in pips.items():
  if pool[color]<n:return None
  pool[color]-=n
 if sum(pool.values())<g:return None
 for color in "CBRUWG":
  used=min(pool[color],g);pool[color]-=used;g-=used
 if g:raise AssertionError("Atomic colored payment failure")
 return dict(pool)

class Physical:
 def __init__(self,library,target,permutation):
  if len(library)!=99 or len(set(permutation))!=99:raise Blocked("99 physical slots required")
  self.z={"library":[(f"m{i:03d}",library[i]) for i in permutation],
          "hand":[],"battlefield":[],"graveyard":[]}
  self.target=target;self.tapped=set();self.mana={}
  self.first_cast=None;self.ever_seen=False;self.turn=0;self.events=[]
  self.mox_basic_discard=0;self.payable_no_opponent=0;self.check()
 def check(self):
  rows=[x for v in self.z.values() for x in v]
  if len(rows)!=99 or len({uid for uid,_ in rows})!=99:raise AssertionError("Physical card conservation")
  if not self.tapped <= {uid for uid,_ in self.z["battlefield"]}:raise AssertionError("Tapped outside battlefield")
  if any(n<0 for n in self.mana.values()):raise AssertionError("Negative mana")
 def transfer(self,card,src,dest):
  if card not in self.z[src]:raise Blocked("Unowned source card")
  self.z[src].remove(card);self.z[dest].append(card);self.check()
 def hand(self,name):return next((c for c in self.z["hand"] if c[1]==name),None)
 def draw(self,n):
  if len(self.z["library"])<n:raise Blocked("Not enough physical cards")
  moved=self.z["library"][:n];self.z["library"]=self.z["library"][n:]
  self.z["hand"].extend(moved);self.check()
 def mox_entry(self):
  mox=self.hand("Mox Diamond")
  if not mox:return False
  cards=sorted((c for c in self.z["hand"] if c[1] in BASIC),key=lambda c:(c[1],c[0]))
  if not cards:return False # Nonbasic discards are UNMODELED, not officially illegal.
  self.transfer(cards[0],"hand","graveyard")
  self.transfer(mox,"hand","battlefield")
  self.first_cast=self.turn;self.mox_basic_discard+=1
  self.events.append({"t":self.turn,"event":"mox_enters_with_actual_basic_discard",
                      "physical_card":mox[0],"discarded":cards[0][0],"mox_mana_used":False})
  return True
 def land_drop(self):
  options=[c for c in self.z["hand"] if c[1] in BASIC]
  if not options:return
  preferred=COST.get(self.target,(0,{}))[1]
  options.sort(key=lambda c:(0 if BASIC[c[1]] in preferred else 1,c[1],c[0]))
  chosen=options[0]
  self.transfer(chosen,"hand","battlefield")
  self.events.append({"t":self.turn,"event":"basic_land_play","card":chosen[0],"name":chosen[1]})
 def tap_basics(self):
  for uid,name in self.z["battlefield"]:
   if name in BASIC and uid not in self.tapped:
    self.tapped.add(uid);color=BASIC[name];self.mana[color]=self.mana.get(color,0)+1
  self.check()
 def paid_simple_cast(self):
  card=self.hand(self.target)
  if not card:return False
  if self.target=="An Offer You Can't Refuse":
   if pay(self.mana,COST[self.target]) is not None:self.payable_no_opponent+=1
   return False  # No opponent noncreature spell. Do not create one.
  if self.target not in COST:raise Blocked("Unmodeled spell")
  after=pay(self.mana,COST[self.target])
  if after is None:return False
  self.mana=after
  self.transfer(card,"hand","battlefield")
  if self.target.startswith("The Enigma Jewel"):self.tapped.add(card[0])
  self.first_cast=self.turn
  self.events.append({"t":self.turn,"event":"source_paid_simple_main_phase_permanent",
    "physical_card":card[0],"name":self.target,"abilities_resolved":False})
  self.check();return True
 def turn_step(self):
  self.turn+=1;self.mana={};self.tapped.clear()  # Basic land untap only; no upkeep triggers.
  self.draw(1);self.ever_seen|=self.hand(self.target) is not None
  if self.first_cast is None and self.target=="Mox Diamond":self.mox_entry()
  self.land_drop();self.tap_basics()
  if self.first_cast is None and self.target!="Mox Diamond":self.paid_simple_cast()
  self.check()

def one_arm(library,name,index):
 perm=random.Random(sim.seed_for(120026,index)^0x5EED).sample(range(99),99)
 state=Physical(library,name,perm)
 state.draw(7);state.ever_seen=state.hand(name) is not None
 for _ in range(8):state.turn_step()
 return state

def run():
 p,reg,prior=map(read,(PLAN,REG,PRIOR))
 R=ev.Resolver()
 verify_plan(p,reg,prior,R)
 records=[]
 for st in p["studies"]:
  a,b,slot,original,landflags=c120.verify_exact_pair(
    {"slug":st["slug"],"cut":st["cut"],"add":st["add"],
     "commander":st["commander"],"approved_logical_hash":st["approved_logical_hash"],
     "opportunities":[]},R)
  counts={}
  for arm,lib,name in (("baseline",a,st["cut"]),("candidate",b,st["add"])):
   counts[arm]={"arm":arm,"card":name,"seen":0,"supported_cast_or_entry":0,
      "first_by_turn":Counter(),"payable_missing_opponent_event":0,"mox_basic_discard":0,"witnesses":[]}
  for i in range(1024):
   for arm,lib,name in (("baseline",a,st["cut"]),("candidate",b,st["add"])):
    s=one_arm(lib,name,i);d=counts[arm]
    d["seen"]+=int(s.ever_seen)
    if s.first_cast is not None:
     d["supported_cast_or_entry"]+=1;d["first_by_turn"][str(s.first_cast)]+=1
     if len(d["witnesses"])<2:
      d["witnesses"].append({"sample_index":i,"turn":s.first_cast,"resource_events":s.events,
                            "opponent_responses_executed":0})
    d["payable_missing_opponent_event"]+=int(s.payable_no_opponent>0)
    d["mox_basic_discard"]+=s.mox_basic_discard
  rows=[]
  for arm in ("baseline","candidate"):
   d=counts[arm];d["first_by_turn"]=dict(d["first_by_turn"]);rows.append(d)
  if rows[0]["seen"]!=rows[1]["seen"]:
   raise AssertionError("Aligned physical slot access drift")
  records.append({"deck_id":st["deck_id"],"commander":st["commander"],
     "approved_logical_hash":st["approved_logical_hash"],"approved_raw_sha256_recorded":st["approved_raw_sha256"],
     "engineering_source_text_sha256":"sha256:"+hashlib.sha256(original.encode()).hexdigest(),
     "physical_main_cards":99,"commanders":1,"shared_library_slots":98,
     "same_slot_index":slot,"samples":1024,"results":rows,
     "legal_opponent_spell_targets_observed":0,"commander_ability_resolutions":0,
     "unsupported_nonbasic_land_resources_not_counted_as_failure":True})
 return {"schema_version":1,"cycle":121,"stage":"M6_LIMITED_PHYSICAL_BASIC_LAND_CASTING_NOT_GAMEPLAY",
   "plan_sha256":sha(PLAN),"source_registry_sha256":sha(REG),"prior_prereg_sha256":sha(PRIOR),
   "total_paired_samples":3072,"total_arm_views":6144,"cases":records,
   "scripted_opponent_events":0,"multiplayer_results":0,"phase_b_certified":False,
   "independent_pass_c_reviews":0,"approved_swaps":0,"canonical_decks_modified":0,
   "M6_accepted":False,
   "limitations":["Only physical basic lands, one per turn; no nonbasic mana, rocks, conditional mana, tutors or alternative costs",
                  "Mox Diamond entry only with physical BASIC land discard; no Mox mana or other ramp modeled",
                  "An Offer cannot be tested without actual opponent noncreature spell on stack",
                  "No commander abilities, actual combat, stack priority, full Phase B or candidate strength conclusion"]}
def main():
 parser=argparse.ArgumentParser()
 parser.add_argument("--build",action="store_true");parser.add_argument("--check",action="store_true")
 a=parser.parse_args()
 if not(a.build or a.check):parser.error("Provide --build or --check")
 out=encode(run())
 if a.build:OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(out,encoding="utf-8")
 if a.check and (not OUT.exists() or OUT.read_text(encoding="utf-8")!=out):
  raise Blocked("Cycle121 source-paid basic-only result not reproducible")
 print("Cycle121: source-locked 3072 paired shuffles; legal basic-land-only cast witnesses; no independent Pass C, Phase B or approval.")
if __name__=="__main__":main()
