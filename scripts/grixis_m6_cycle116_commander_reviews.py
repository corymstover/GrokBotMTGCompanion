#!/usr/bin/env python3
"""Cycle116: deterministic source/Oracle verification for three authored HOLD reviews.

Produces evidence only: no canonical edits, independent Pass C, Phase B or M6 approval.
"""
from __future__ import annotations
import argparse, hashlib, json, sys
from collections import Counter
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import evaluate_decklist as ev
import grixis_sim as sim

PLAN = ROOT / "data/grixis/m6/phase_b_plans/cycle116_three_decks_preregistered_01.json"
REV = ROOT / "data/grixis/m6/author_reviews/cycle116_commander_first_reviews_01.json"
REG = ROOT / "data/grixis/registry.json"
TRIAGE = ROOT / "data/grixis/m6/phase_b_bounded/commander_first_readiness_62_01.json"
OUT = ROOT / "data/grixis/m6/phase_b_bounded/cycle116_sourced_review_validation_01.json"
AUTH={"can_change_decklists":False,"can_approve_or_lock":False,
      "can_certify_M6":False,"can_issue_final_swaps":False}
EXPECTED={
"Kess__Dissident_Mage":("kess-dissident-mage","Kess, Dissident Mage",
    "Hullbreaker Horror","Orcish Bowmasters",
    "swap:kess-dissident-mage:m5:49904d9f8805",
    "93d27d605bbdf0737ebe32c911fafe3a002b06d7d90f00b7bfc402cb1d3faccb"),
"Edea__Possessed_Sorceress":("edea-possessed-sorceress","Edea, Possessed Sorceress",
    "Tidespout Tyrant","Deadly Rollick",
    "swap:edea-possessed-sorceress:m5:5f2787335006",
    "fd560a9b0777088b3ad1684ded030566c894faa206ddf6763b74d95d82c532e4"),
"Lynde__Cheerful_Tormentor":("lynde-cheerful-tormentor","Lynde, Cheerful Tormentor",
    "Hullbreaker Horror","Withering Torment",
    "swap:lynde-cheerful-tormentor:m5:bb1cc7a27136",
    "05d1c4eea023d25e4308f78b109e80b78e0a3f4d655c3df36743ba3afbf04166"),
}
ORACLE={
"Kess, Dissident Mage":("once during each of your turns","instant or sorcery spell from your graveyard","exile it instead"),
"Edea, Possessed Sorceress":("at the beginning of combat on your turn","creature you control but don't own dies","under its owner's control"),
"Lynde, Cheerful Tormentor":("a curse is put into your graveyard from the battlefield","at the beginning of your upkeep","draw two cards"),
"Hullbreaker Horror":("flash","this spell can't be countered","whenever you cast a spell","return target nonland permanent"),
"Orcish Bowmasters":("flash","whenever an opponent draws a card","amass orcs 1"),
"Tidespout Tyrant":("whenever you cast a spell","return target permanent to its owner's hand"),
"Deadly Rollick":("if you control a commander","exile target creature"),
"Withering Torment":("destroy target creature or enchantment","you lose 2 life"),
"Despotic Scepter":("destroy target permanent you own",),
"Curse of Bloodletting":("enchant player",),
}
BASICS={"Plains","Island","Swamp","Mountain","Forest","Wastes"}
def read(path):return json.loads(path.read_text(encoding="utf-8"))
def digest(path):return "sha256:"+hashlib.sha256(path.read_bytes()).hexdigest()
def encode(obj):return json.dumps(obj,sort_keys=True,indent=2,ensure_ascii=False)+"\n"
def check_oracle(resolver):
    results={}
    for name,phrases in ORACLE.items():
        card=resolver.get(name)[0]
        actual=card.get("oracle_text") or "\n".join(face.get("oracle_text") or "" for face in card.get("card_faces",[]))
        if card.get("name")!=name or not actual or any(w.casefold() not in actual.casefold() for w in phrases):
            raise ValueError("Frozen Oracle mechanic mismatch: "+name+": "+repr(actual[:450]))
        results[name]={"text_sha256":"sha256:"+hashlib.sha256(actual.encode()).hexdigest(),
            "frozen_source_only_not_live_current_legality":True}
    return results

def validate(row,original,registry,blueprint,queue,deck,oracle):
    did=row["deck_id"]
    slug,name,add,cut,swap,sha=EXPECTED[did]
    names=[c["name"] for c in deck.library]
    if (row["slug"]!=slug or row["commander"]!=name or row["proposed_add"]!=add or
        row["proposed_cut"]!=cut or row["m5_swap_id"]!=swap or
        row["approved_raw_sha256"]!=sha or
        original["deck_id"]!=did or original["slug"]!=slug or original["commander"]!=name or
        original["approved_raw_sha256"]!=sha or original["m5_swap_id"]!=swap or
        original["proposed_add"]!=add or original["proposed_cut"]!=cut or
        registry["deck_id"]!=did or registry["slug"]!=slug or registry["commanders"]!=[name] or
        registry["source"]["recorded_sha256"]!=sha or
        registry["source"]["raw_sha256"]!="sha256:"+sha or
        registry["source"]["path"]!=original["source_file"] or
        registry["source"]["recorded_matches_raw"] is not True or
        blueprint["deck_id"]!=did or blueprint["canonical_hash"]!=registry["current_canonical_hash"] or
        registry["current_canonical_hash"]!=original["canonical_logical_hash"] or
        queue["source_canonical_logical_hash"]!=original["canonical_logical_hash"]):
        raise ValueError("Named candidate, frozen source approval SHA or identity drift: "+did)
    if len(names)!=99 or len(deck.commanders)!=1 or deck.commanders[0]["name"]!=name:
        raise ValueError("Real 99+commander physical approved source mismatch: "+did)
    if any(q>1 and card not in BASICS for card,q in Counter(names).items()):
        raise ValueError("Nonbasic singleton source violation: "+did)
    if names.count(cut)!=1 or add in names:
        raise ValueError("Named candidate added or cut missing from approved original: "+did)
    if any(x["card"]!=name and x["card"] not in names for x in blueprint["identity_core"]):
        raise ValueError("Source protected commander identity package drift: "+did)
    hits=[h for h in queue["first_three_TO_REVIEW_NOT_TO_APPLY"] if h["swap_id"]==swap]
    if len(hits)!=1 or (hits[0]["add"],hits[0]["cut"])!=(add,cut) or "test_pass" not in hits[0]["M5_flags"]:
        raise ValueError("Source Cycle111/M5 hypothesis provenance drift: "+did)
    if not {name,add,cut}.issubset(oracle):
        raise ValueError("Source-specific Oracle mechanics not verified: "+did)
    if original["order"]!=row["order"] or row["disposition"]!="HOLD_EXISTING_LIST_NO_SWAP":
        raise ValueError("M6 named review was re-ordered or promoted: "+did)
    if (row["approved_swaps"]!=0 or row["performance_modeling_completed"] or
        row["independent_pass_c_completed"] or row["official_current_legality_checked"] or
        len(row["specific_rules"])<5 or not row["why_this_specific_proposal_fails"] or
        not row["positive_case"] or not row["cut_cost"] or not row["next_evidence"]):
        raise ValueError("Incomplete or improperly certified author judgment: "+did)
    if did=="Kess__Dissident_Mage" and not {"Demonic Consultation","Thassa's Oracle","Underworld Breach","Orcish Bowmasters"}.issubset(names):
        raise ValueError("Kess source fast graveyard identity absent")
    if did=="Edea__Possessed_Sorceress" and not {"Mass Mutiny","Goblin Bombardment","Deadly Rollick","Thassa, Deep-Dwelling"}.issubset(names):
        raise ValueError("Edea theft/sacrifice source package absent")
    if did=="Lynde__Cheerful_Tormentor" and not {"Despotic Scepter","Claws of Gix","Paradox Haze","Withering Torment","Curse of Bloodletting"}.issubset(names):
        raise ValueError("Lynde Curse-reset and removal role package absent")
    return {"deck_id":did,"commander":name,"approved_sha256":sha,
        "approved_raw_sha_recorded_in_registry_not_fresh_rehash":True,
        "source_blueprint_sha256":digest(ROOT/"data/grixis/blueprints"/(slug+".json")),
        "source_main_count":len(names),"commander_count":len(deck.commanders),
        "nonbasic_singleton_checked":True,
        "add_absent_cut_present":True,"source_swap_id":swap,
        "author_disposition":row["disposition"],
        "canonical_deck_modified":False,"formal_independent_pass_c":False,
        "full_effect_aware_phase_b":False,"tested_pool_zero_improvement_certified":False}

def run():
    plan=read(PLAN);reviews=read(REV);reg=read(REG);tri=read(TRIAGE)
    if (plan["cycle"]!=116 or plan["status"]!="preregistered_before_conclusions" or
        plan["authority"]!=AUTH or reviews["cycle"]!=116 or reviews["authority"]!=AUTH or
        reviews["review_count"]!=3 or len(reviews["reviews"])!=3 or
        len(reg["decks"])!=62 or reg["program"]["milestones"]["M6"]["status"]!="in_progress" or
        reg["program"]["milestones"]["M6"]["accepted_by"] is not None or
        set(EXPECTED)!={x["deck_id"] for x in plan["decks"]} or
        set(EXPECTED)!={x["deck_id"] for x in reviews["reviews"]} or
        reviews["global_gates"]["M6_accepted"] is not False or
        reviews["global_gates"]["canonical_swaps_applied"]!=0):
        raise ValueError("Cycle116 prereg, authority or source identity changed")
    oracle=check_oracle(ev.Resolver())
    queue={x["deck_id"]:x for x in tri["ordered_decks"]}
    targets={x["deck_id"]:x for x in plan["decks"]}
    results=[]
    resolver=ev.Resolver()
    for row in reviews["reviews"]:
        did=row["deck_id"];slug=EXPECTED[did][0]
        blueprint=read(ROOT/"data/grixis/blueprints"/(slug+".json"))
        results.append(validate(row,targets[did],reg["decks"][did],blueprint,queue[did],sim.load_deck(slug,resolver),oracle))
    return {"cycle":116,"schema_version":1,"reviewed":results,"review_count":3,
        "plan_sha256":digest(PLAN),"author_review_sha256":digest(REV),"registry_sha256":digest(REG),
        "m5_readiness_sha256":digest(TRIAGE),"frozen_oracle":oracle,
        "canonical_decks_modified":0,"swaps_approved_or_applied":0,
        "formal_independent_pass_c_count":0,"effect_aware_multiplayer_phase_b_count":0,
        "entire_deck_current_official_legality_certified":False,
        "source_bytes_independently_rehashed":False,"M6_accepted":False,"authority":AUTH}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--build",action="store_true");p.add_argument("--check",action="store_true")
    args=p.parse_args()
    if not args.build and not args.check:p.error("choose --build or --check")
    txt=encode(run())
    if args.build:
        OUT.parent.mkdir(parents=True,exist_ok=True)
        OUT.write_text(txt,encoding="utf-8")
    if args.check and (not OUT.is_file() or OUT.read_text(encoding="utf-8")!=txt):
        raise ValueError("Cycle116 source/Oracle verification is not reproducible")
    print("Cycle116: three source-specific reviews verified; no Pass C/Phase B/M6 promotion")
if __name__=="__main__":main()
