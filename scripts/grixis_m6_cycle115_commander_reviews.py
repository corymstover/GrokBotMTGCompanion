#!/usr/bin/env python3
"""Cycle115 source-verified commander-first review regression (NOT Pass C or M6)."""
from __future__ import annotations
import argparse,hashlib,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import evaluate_decklist as ev
import grixis_sim as sim
PLAN=ROOT/"data/grixis/m6/phase_b_plans/cycle115_three_commander_reviews_01.json"
REV=ROOT/"data/grixis/m6/author_reviews/cycle115_three_commander_reviews_01.json"
REG=ROOT/"data/grixis/registry.json"
TRIAGE=ROOT/"data/grixis/m6/phase_b_bounded/commander_first_readiness_62_01.json"
OUT=ROOT/"data/grixis/m6/phase_b_bounded/cycle115_sourced_review_validation_01.json"
AUTH={"can_change_decklists":False,"can_approve_or_lock":False,"can_decide":False,"can_certify_M6":False}
EXPECTED={
 "RogSi":("rograkh-son-of-rohgahh-silas-renn",("Rograkh, Son of Rohgahh","Silas Renn, Seeker Adept"),"The Enigma Jewel // Locus of Enlightenment","Birgi, God of Storytelling // Harnfel, Horn of Bounty","swap:rograkh-son-of-rohgahh-silas-renn:m5:c0b52a884319","06c9e22b5afc46bd58bbbfdef5c42a796d2a986a2972456107c29aee1b5f905c","HOLD_EXISTING_LIST_NO_SWAP"),
 "Nicol_Bolas":("nicol-bolas",("Nicol Bolas",),"Volcano Hellion","Mystic Remora","swap:nicol-bolas:m5:3adba7cabda7","e47fdd5c31dce2d5b05e8fa8c217fe94caa16ef150057f98748254fc3c841617","HOLD_EXISTING_LIST_NO_SWAP"),
 "Mai_and_Zuko":("mai-and-zuko",("Mai and Zuko",),"The Enigma Jewel // Locus of Enlightenment","An Offer You Can't Refuse","swap:mai-and-zuko:m5:efea4143158c","aa2036f49f38e6503734d99c852acdfa704aa1b27e44bb26d6e9566a73a0d4a2","PROMISING_ARTIFACT_SYNERGY_BUT_PROPOSED_CUT_HOLD")}
ORACLE={
 "Rograkh, Son of Rohgahh":("first strike","partner"),
 "Silas Renn, Seeker Adept":("artifact card in your graveyard","partner"),
 "The Enigma Jewel // Locus of Enlightenment":("enters tapped","activate abilities","craft with four or more nonlands","isn\'t a mana ability"),
 "Birgi, God of Storytelling // Harnfel, Horn of Bounty":("whenever you cast a spell","add {R}","discard a card","exile the top two cards"),
 "Nicol Bolas":("whenever nicol bolas deals damage","discards their hand","sacrifice nicol bolas unless you pay"),
 "Volcano Hellion":("echo","to you and target creature"),
 "Mystic Remora":("cumulative upkeep","noncreature spell"),
 "Mai and Zuko":("firebending 3","artifact spells as though they had flash"),
 "An Offer You Can't Refuse":("counter target noncreature spell","two treasure tokens"),
 "Basalt Monolith":("add {C}{C}{C}","untap this artifact"),
 "Rings of Brighthearth":("pay {2}","copy that ability"),
}
BASICS={"Plains","Island","Swamp","Mountain","Forest","Wastes"}
def read(p):return json.loads(p.read_text(encoding="utf-8"))
def sha(p):return "sha256:"+hashlib.sha256(p.read_bytes()).hexdigest()
def output(d):return json.dumps(d,sort_keys=True,indent=2,ensure_ascii=False)+"\n"
def check_oracle(res):
 seen={}
 for name,phrases in ORACLE.items():
  card=res.get(name)[0]
  txt=card.get("oracle_text") or "\n".join(f.get("oracle_text") or "" for f in card.get("card_faces",[]))
  if card.get("name")!=name or not txt or any(w.casefold() not in txt.casefold() for w in phrases):
   raise ValueError("Frozen Oracle mechanic missing or changed: "+name+": "+repr(txt[:500]))
  seen[name]={"oracle_sha256":"sha256:"+hashlib.sha256(txt.encode()).hexdigest(),"frozen_archive_not_current_legality":True}
 return seen
def validate(item,p,meta,bp,queue,deck,oc):
 did=item["deck_id"]
 slug,cmds,add,cut,swap,approved,verdict=EXPECTED[did]
 names=[x["name"] for x in deck.library]
 actual_commands=tuple(c["name"] for c in deck.commanders)
 if (p["id"]!=did or p["slug"]!=slug or p["approved_raw_sha256"]!=approved or
     tuple(p["commander_names"])!=cmds or p["commander_count"]!=len(cmds) or
     p["main_count"]!=100-len(cmds) or p["add"]!=add or p["cut"]!=cut or p["swap_id"]!=swap or
     item["approved_raw_sha256"]!=approved or item["source_swap_id"]!=swap or
     item["add"]!=add or item["cut"]!=cut or item["verdict"]!=verdict or
     meta["deck_id"]!=did or meta["slug"]!=slug or tuple(meta["commanders"])!=cmds or
     meta["source"]["recorded_sha256"]!=approved or meta["source"]["raw_sha256"]!="sha256:"+approved or
     meta["source"]["recorded_matches_raw"] is not True or
     bp["deck_id"]!=did or bp["canonical_hash"]!=meta["current_canonical_hash"] or
     queue["source_canonical_logical_hash"]!=meta["current_canonical_hash"]):
  raise ValueError("Source/approved hash/candidate cross-check drift: "+did)
 if len(names)!=100-len(cmds) or actual_commands!=cmds:
  raise ValueError("Incorrect real physical commander/main counts: "+did)
 from collections import Counter
 if any(n>1 and name not in BASICS for name,n in Counter(names).items()):
  raise ValueError("Nonbasic singleton violation: "+did)
 if names.count(cut)!=1 or add in names:
  raise ValueError("Approved cut/add not unchanged: "+did)
 if any(v["card"] not in names and v["card"] not in cmds for v in bp["identity_core"]):
  raise ValueError("Commander identity protected core is absent: "+did)
 matches=[x for x in queue["first_three_TO_REVIEW_NOT_TO_APPLY"] if x["swap_id"]==swap]
 if len(matches)!=1 or (matches[0]["add"],matches[0]["cut"])!=(add,cut) or "test_pass" not in matches[0]["M5_flags"]:
  raise ValueError("Source M5 hypothesis provenance drift: "+did)
 if not all(x in oc for x in (*cmds,add,cut)):
  raise ValueError("Named original card Oracle mismatch")
 if (item["list_modified"] or item["formal_phase_b"] or item["independent_review"] or
     not item["commander_identity"] or len(item["verified_card_text_implications"])<4 or
     not item["evidence_needed"] or not item["cut_cost"]):
  raise ValueError("Incomplete author judgment or incorrect claimed verification: "+did)
 if did=="RogSi" and not {"Mox Amber","Culling the Weak"}.issubset(names):
  raise ValueError("RogSi free-commander synergy absent")
 if did=="Mai_and_Zuko" and not {"Basalt Monolith","Rings of Brighthearth","Sensei's Divining Top"}.issubset(names):
  raise ValueError("Mai/Zuko actual activated-ability engine absent")
 if did=="Nicol_Bolas" and not {"Dragon Tempest","Waste Not","Chandra's Ignition"}.issubset(names):
  raise ValueError("Original Bolas commander source package absent")
 return {"deck_id":did,"source_approved_sha256_recorded_not_independently_rehashed":approved,
         "commander_count":len(cmds),"main_library_card_count":len(names),"nonbasic_singleton_pass":True,
         "source_blueprint_hash_match":True,"m5_swap_id_match":True,
         "candidate_add_absent":True,"candidate_cut_present":True,
         "verdict":verdict,"source_oracle_frozen_not_current_legality":True,
         "formal_independent_pass_c":False,"card_swap_applied":False}
def run():
 p=read(PLAN);r=read(REV);reg=read(REG);tri=read(TRIAGE)
 if (p["cycle"]!=115 or p["status"]!="preregistered_before_authored_reviews" or
     p["authority"]!=AUTH or r["cycle"]!=115 or len(r["items"])!=3 or
     len(reg["decks"])!=62 or
     reg["program"]["milestones"]["M6"]["status"]!="in_progress" or
     reg["program"]["milestones"]["M6"]["accepted_by"] is not None or
     set(x["deck_id"] for x in r["items"])!=set(EXPECTED) or
     r["global_state"]["canonical_cards_changed"]!=0 or
     r["global_state"]["M6_accepted"] is not False):
  raise ValueError("115 authority or preregistered source drift")
 oracle=check_oracle(ev.Resolver())
 planned={x["id"]:x for x in p["decks"]}
 queued={x["deck_id"]:x for x in tri["ordered_decks"]}
 rows=[]
 for item in r["items"]:
  did=item["deck_id"];slug=EXPECTED[did][0]
  rows.append(validate(item,planned[did],reg["decks"][did],
      read(ROOT/"data/grixis/blueprints"/(slug+".json")),queued[did],
      sim.load_deck(slug,ev.Resolver()),oracle))
 return {"schema_version":1,"cycle":115,"reviewed_decks":rows,
         "approved_deck_count":62,"source_verified_deck_count":3,
         "plan_sha256":sha(PLAN),"review_sha256":sha(REV),"registry_sha256":sha(REG),
         "readiness_sha256":sha(TRI),"oracle_checked":oracle,
         "fresh_original_source_bytes_rehashed":False,
         "whole_deck_legality_currently_verified":False,
         "formal_independent_pass_c_count":0,"full_effect_aware_phase_b_count":0,
         "canonical_decks_modified":0,"swaps_approved_or_applied":0,"M6_accepted":False,"authority":AUTH}
def main():
 parser=argparse.ArgumentParser();parser.add_argument("--build",action="store_true");parser.add_argument("--check",action="store_true")
 a=parser.parse_args()
 if not(a.build or a.check):parser.error("Specify --build or --check")
 t=output(run())
 if a.build:OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(t,encoding="utf-8")
 if a.check and (not OUT.exists() or OUT.read_text(encoding="utf-8")!=t):
  raise ValueError("Cycle115 deterministic source verification receipt mismatch")
 print("Cycle115 verified 3 commander-first author reviews, no independent Pass C or approval")
if __name__=="__main__":main()
