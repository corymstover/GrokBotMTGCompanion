#!/usr/bin/env python3
"""Cycle 99: four real Oracle-gated tutor effects in bounded paired Abaddon replay.

Evidence-only, with exact card zones and deterministic (nonoptimal) selection.
The prior Cycle97/98 source and evidence are not modified.
"""
from __future__ import annotations
import argparse,hashlib,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import evaluate_decklist as ev
import grixis_m6_abaddon_effect_coverage as prior
from grixis_m6_abaddon_turn_state import CARDS,Unsupported

PLAN=ROOT/"data/grixis/m6/phase_b_plans/abaddon_tutor_state_01.json"
OUT=ROOT/"data/grixis/m6/phase_b_bounded/abaddon_tutor_state_01.json"
PREV=ROOT/"data/grixis/m6/phase_b_bounded/abaddon_effect_coverage_01.json"
SOURCE=ROOT/"exports/grixis-archidekt/source-baseline/abaddon-the-despoiler.txt"
AUTH={"can_decide":False,"can_apply_swap":False,"can_change_canonical_list":False,"can_approve_or_lock":False}
TARGET_ORDER=("Brainstorm","Ponder","Dark Ritual","Rite of Flame","Kessig Flamebreather","Sol Ring")
TUTOR_SPECS={
 "Demonic Tutor":{"mv":2,"cost":{"B":1,"generic":1},"type":"sorcery","destination":"hand","allowed_types":[],"life_cost_on_resolution":0},
 "Mystical Tutor":{"mv":1,"cost":{"U":1,"generic":0},"type":"instant","destination":"top","allowed_types":["instant","sorcery"],"life_cost_on_resolution":0},
 "Imperial Seal":{"mv":1,"cost":{"B":1,"generic":0},"type":"sorcery","destination":"top","allowed_types":[],"life_cost_on_resolution":2},
 "Vampiric Tutor":{"mv":1,"cost":{"B":1,"generic":0},"type":"instant","destination":"top","allowed_types":[],"life_cost_on_resolution":2}
}
for _name,_spec in TUTOR_SPECS.items():
 if _name in CARDS:raise RuntimeError("Attempted overwrite "+_name)
 CARDS[_name]=dict(_spec)

def digest(p):return "sha256:"+hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text(encoding="utf-8"))
def pretty(p):return json.dumps(p,sort_keys=True,ensure_ascii=False,indent=2)+"\n"

def oracle_gate(plan):
 r=ev.Resolver();out={}
 for name,phrases in plan["oracle_assertions"].items():
  if name not in TUTOR_SPECS:raise ValueError("Undeclared Oracle tutor")
  src=r.get(name)[0]
  t=src.get("oracle_text") or ""
  if not t:raise ValueError("Frozen Oracle missing: "+name)
  for snippet in phrases:
   if snippet.casefold() not in t.casefold():raise ValueError(name+" Oracle snippet not found: "+repr(snippet)+" actual: "+repr(t))
  expected=TUTOR_SPECS[name]
  if int(src.get("cmc") or -1)!=expected["mv"]:
   raise ValueError(name+" mana value diverged")
  tl=src.get("type_line","").casefold()
  if expected["type"] not in tl:raise ValueError(name+" frozen type mismatch")
  out[name]={"oracle_sha256":"sha256:"+hashlib.sha256(t.encode()).hexdigest(),
       "type_line":src.get("type_line"),"cmc":src.get("cmc"),"mana_cost":src.get("mana_cost")}
 return out

# Add literal front-face Oracle types to the exact, previously approved
# Cycle 97 full-99 metadata. No inference from filenames or partial names.
def typed_metadata(cards):
 d=ORIG_METADATA(cards)
 for card in cards:
  n=card["name"]
  ty=list(card.get("types") or [])
  if n not in d:raise ValueError("No library metadata "+n)
  if "types" in d[n] and d[n]["types"]!=ty:raise ValueError("Inconsistent Oracle types "+n)
  d[n]["types"]=ty
 return d

ORIG_METADATA=prior.previous.profile_metadata

class TutorCascade(prior.ExpandedCascade):
 def find_tutor_target(self,name):
  want=set(TUTOR_SPECS[name]["allowed_types"])
  eligible=[]
  for n in self.library:
   data=self.metadata.get(n)
   if data is None:raise ValueError("Library metadata missing "+n)
   if not want or want.intersection(data.get("types",())):eligible.append(n)
  if not eligible:return None
  for n in TARGET_ORDER:
   if n in eligible:return n
  return sorted(eligible,key=lambda n:(-self.metadata[n]["mv"],n))[0]

 def resolve_tutor(self,name):
  specs=TUTOR_SPECS[name]
  target=self.find_tutor_target(name)
  if target is not None:
   self.library.remove(target)
  self.rng.shuffle(self.library)
  if target is not None:
   if specs["destination"]=="hand":self.hand.append(target)
   elif specs["destination"]=="top":self.library.insert(0,target)
   else:raise Unsupported("Unknown tutor destination")
  if specs["life_cost_on_resolution"]:
   self.pilot-=specs["life_cost_on_resolution"]
   self.over=(self.pilot<=0 or all(v<=0 for v in self.opponents))
  self.events.append({"event":"oracle_tutor_resolved","name":name,
    "selected":target,"target_type":self.metadata[target].get("types") if target else [],
    "destination":specs["destination"],"controller_life":self.pilot,
    "opponent_life_lost_this_turn":self.lost,"shuffle_performed":True,
    "candidate_priority_policy":list(TARGET_ORDER)})
  return target

 def resolve_top(self):
  if self.stack and self.stack[-1]["kind"]=="spell" and self.stack[-1]["name"] in TUTOR_SPECS:
   obj=self.stack.pop();name=obj["name"]
   self.resolve_tutor(name)
   self.graveyard.append(name)
   self.events.append({"event":"spell_resolves","name":name,"oracle_tutor":True})
   return obj
  return super().resolve_top()

def replay_tutors(*args,**kwargs):
 r=ORIG_REPLAY(*args,**kwargs)
 evs=[e for e in r["events"] if e["event"]=="oracle_tutor_resolved"]
 r["tutor_resolution_count"]=len(evs)
 r["tutor_to_top_count"]=sum(e["destination"]=="top" and e["selected"] is not None for e in evs)
 r["tutor_to_hand_count"]=sum(e["destination"]=="hand" and e["selected"] is not None for e in evs)
 r["tutor_fail_find_count"]=sum(e["selected"] is None for e in evs)
 r["tutor_controller_life_paid"]=sum(TUTOR_SPECS[e["name"]]["life_cost_on_resolution"] for e in evs)
 return r

def summarize_tutors(rows):
 d=ORIG_STATS(rows)
 attrs=("tutor_resolution_count","tutor_to_top_count","tutor_to_hand_count",
       "tutor_fail_find_count","tutor_controller_life_paid")
 d["oracle_tutor_zone_effect_totals"]={k:sum(row[k] for row in rows) for k in attrs}
 return d

ORIG_REPLAY=prior.replay98
ORIG_STATS=prior.previous.basic_stats

def run():
 p=read(PLAN);old=read(PREV)
 if p["cycle"]!=99 or p["status"]!="registered_before_execution" or p["authority"]!=AUTH:
  raise ValueError("Pre-registered scope changed")
 if (digest(SOURCE)!="sha256:"+p["source_sha256"]
     or old["supports_improvement_claim"] or old["full_phase_b_complete"]
     or p["seed"]!=97017 or p["sample_count"]!=240):
  raise ValueError("Prior source, model or seed drift")
 if p["effects"]!=TUTOR_SPECS or set(p["oracle_assertions"])!=set(TUTOR_SPECS):
  raise ValueError("Tutor effects differ from prereg")
 oracle=oracle_gate(p)
 oldcls,oldmeta,oldreplay,oldstats=(prior.ExpandedCascade,prior.previous.profile_metadata,prior.replay98,prior.previous.basic_stats)
 prior.ExpandedCascade=TutorCascade
 prior.previous.profile_metadata=typed_metadata
 prior.replay98=replay_tutors
 prior.previous.basic_stats=summarize_tutors
 try:
  new=prior.run()
 finally:
  prior.ExpandedCascade=oldcls
  prior.previous.profile_metadata=oldmeta
  prior.replay98=oldreplay
  prior.previous.basic_stats=oldstats
 for x,previous in zip(new["results"],old["results"]):
  if x["swap"]!=previous["swap"]:raise ValueError("Hypothesis drift")
  for profile,v in x["profiles"].items():
   priorprofile=previous["profiles"][profile]
   for side in ("baseline","challenger"):
    z=v[side]["effect_coverage"]
    if z["offered"]!=z["modeled_casts"]+z["unmodeled_offers"]+z["legal_declines"]:
     raise ValueError("Invalid accounted cascade offerings")
   v["cycle_98_coverage"]={side:priorprofile[side]["effect_coverage"] for side in ("baseline","challenger")}
 return {"schema_version":1,"cycle":99,"stage":"M6_Abaddon_Oracle_verified_four_tutors",
     "source_sha256":digest(SOURCE),"preregistration_sha256":digest(PLAN),
     "prior_evidence_sha256":digest(PREV),"approved_raw_sha256":p["approved_raw_sha256"],
     "logical_hash":p["logical_hash"],"frozen_oracle_checks":oracle,
     "tutor_spells":sorted(TUTOR_SPECS),"seed":p["seed"],"samples_per_swap_per_profile":p["sample_count"],
     "results":new["results"],"baseline_replay_sha256_by_profile":new["baseline_replay_sha256_by_profile"],
     "model_limitations":p["limits"],"full_99_library_shuffle_used":True,
     "full_deck_gameplay_simulation":False,"full_phase_b_complete":False,
     "supports_improvement_claim":False,"can_certify_zero_improvement":False,
     "formal_independent_pass_c_complete":False,"authority":AUTH}

def main():
 ap=argparse.ArgumentParser()
 ap.add_argument("--build",action="store_true");ap.add_argument("--check",action="store_true")
 args=ap.parse_args()
 if not (args.build or args.check):ap.error("requires --build/--check")
 text=pretty(run())
 if args.build:OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(text,encoding="utf-8")
 if args.check and (not OUT.exists() or OUT.read_text(encoding="utf-8")!=text):
  raise ValueError("Cycle99 deterministic evidence changed")
 print("Cycle99: Oracle-gated tutor paired replay, no Phase-B claim.")
if __name__=="__main__":main()
