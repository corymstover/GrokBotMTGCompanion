#!/usr/bin/env python3
"""Cycle128: Oracle-verified, source-specific authored reviews for six commanders.

This does not verify fresh 2026-10-19 legality, complete Phase B, named
independent Pass C, local optimum, or any canonical deck change.
"""
from __future__ import annotations
import argparse, hashlib, json, sys
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import evaluate_decklist as ev
import grixis_authority as ga
import grixis_sim as sim
import grixis_m6_cycle117_independent_review_readiness as c117
PLAN=ROOT/"data/grixis/m6/phase_b_plans/cycle128_six_commander_judgments_preregistered_01.json"
REV=ROOT/"data/grixis/m6/author_reviews/cycle128_six_commander_authored_judgments_01.json"
TRI=ROOT/"data/grixis/m6/phase_b_bounded/commander_first_readiness_62_01.json"
REG=ROOT/"data/grixis/registry.json"
TRACK=ROOT/"data/grixis/milestone_m6_m7_subtracker.json"
OUT=ROOT/"data/grixis/m6/phase_b_bounded/cycle128_six_review_validation_01.json"
BASICS={"Plains","Island","Swamp","Mountain","Forest","Wastes"}
EXPECTED={
"The_Valeyard":("Hullbreaker Horror","Deadly Rollick","swap:the-valeyard:m5:bf011ab33c85"),
"Norman_Osborn_Green_Goblin":("Hullbreaker Horror","Orcish Bowmasters","swap:norman-osborn:m5:f12ed085e218"),
"Sol_kanar_the_Swamp_King":("Hullbreaker Horror","Rakdos Charm","swap:solkanar-the-swamp-king:m5:ff6a922276cd"),
"Garza_Zol__Plague_Queen":("Kamahl, Pit Fighter","Rapid Hybridization","swap:garza-zol-plague-queen:m5:c03c643ca61a"),
"Evelyn__the_Covetous":("Hullbreaker Horror","Orcish Bowmasters","swap:evelyn-the-covetous:m5:1a9adc07779d"),
"Sauron__the_Dark_Lord":("Tidespout Tyrant","Deadly Rollick","swap:sauron-the-dark-lord:m5:99c9c90172f1"),
}
ORACLE={
"The Valeyard":("villainous choice","vote"),
"Norman Osborn // Green Goblin":(),
"Sol'kanar the Swamp King":("black spell",),
"Garza Zol, Plague Queen":("combat damage","creature dealt damage"),
"Evelyn, the Covetous":("collection counter","once each turn"),
"Sauron, the Dark Lord":("amass Orcs 1","Ring tempts you"),
"Hullbreaker Horror":("whenever you cast a spell","return target nonland permanent"),
"Deadly Rollick":("if you control a commander","exile target creature"),
"Orcish Bowmasters":("flash","amass Orcs 1"),
"Rakdos Charm":("destroy target artifact","graveyard","each creature deals 1 damage"),
"Kamahl, Pit Fighter":("haste","deals 3 damage"),
"Rapid Hybridization":("destroy target creature","Frog Lizard"),
"Tidespout Tyrant":("whenever you cast a spell","return target permanent"),
"Nazgûl":("up to nine cards named",),
"Basilisk Collar":("deathtouch","lifelink"),
"Painter's Servant":("chosen color",),
"Worldgorger Dragon":("exile all other permanents",),
}
def read(p):return json.loads(Path(p).read_text(encoding="utf-8"))
def sha(p):return "sha256:"+hashlib.sha256(Path(p).read_bytes()).hexdigest()
def encode(d):return json.dumps(d,ensure_ascii=False,indent=2,sort_keys=True)+"\n"
def verified_oracle(R):
    out={}
    for name,words in ORACLE.items():
        card,fuzzy=R.get(name)
        if card is None or fuzzy or card.get("name")!=name:
            raise ValueError("Frozen Oracle identity is missing or fuzzy: "+name)
        text=card.get("oracle_text") or "\n".join(f.get("oracle_text") or "" for f in card.get("card_faces",[]))
        if not text or any(w.casefold() not in text.casefold() for w in words):
            raise ValueError("Frozen Oracle text mismatch: "+name+" "+repr(text[:200]))
        out[name]={"frozen_oracle_text_sha256":"sha256:"+hashlib.sha256(text.encode()).hexdigest(),
                   "frozen_card_identity_verified":True,
                   "fresh_2026_10_19_commander_legality_claim":False}
    return out
def verify(row,plan,meta,q,bp,deck,oracle,R):
    did=row["deck_id"]
    if did not in EXPECTED or EXPECTED[did]!=(row["proposed_add"],row["proposed_cut"],row["m5_swap_id"]):
        raise ValueError("Unexpected candidate or unpreregistered swap")
    if (plan["deck_id"]!=did or plan["proposed_add"]!=row["proposed_add"] or
        plan["proposed_cut"]!=row["proposed_cut"] or plan["m5_swap_id"]!=row["m5_swap_id"] or
        meta["slug"]!=row["slug"] or meta["current_canonical_hash"]!=row["canonical_logical_hash"] or
        meta["current_canonical_hash"]!=q["source_canonical_logical_hash"] or
        meta["source"]["recorded_sha256"]!=row["recorded_source_raw_sha256"] or
        meta["source"]["recorded_matches_raw"] is not True or
        row["recorded_source_raw_bytes_match"] is not True or
        bp["deck_id"]!=did or bp["canonical_hash"]!=meta["current_canonical_hash"] or
        len(row["commander"].split(" // "))<1 or
        meta["commanders"]!=q["commanders"]):
        raise ValueError("Source approved hash, commander identity or blueprint drift: "+did)
    hits=[x for x in q["first_three_TO_REVIEW_NOT_TO_APPLY"] if x["swap_id"]==row["m5_swap_id"]]
    if len(hits)!=1 or (hits[0]["add"],hits[0]["cut"])!=(row["proposed_add"],row["proposed_cut"]) or "test_pass" not in hits[0]["M5_flags"]:
        raise ValueError("M5 hypothesis no longer in locked Cycle111 queue: "+did)
    names=[x["name"] for x in deck.library]
    if (len(deck.commanders)!=1 or len(names)!=99 or
        [c["name"] for c in deck.commanders]!=meta["commanders"] or
        names.count(row["proposed_cut"])!=1 or row["proposed_add"] in names or
        ga.text_hash(ga.deck_block_text(meta["slug"]),R)!=meta["current_canonical_hash"]):
        raise ValueError("Physical approved 99+commander source drift: "+did)
    repetitions={n:k for n,k in Counter(names).items() if k>1 and n not in BASICS}
    if did=="Sauron__the_Dark_Lord":
        if repetitions!={"Nazgûl":7} or "Nazgûl" not in oracle:
            raise ValueError("Nazgûl printed-nine-copy source exception drift")
    elif repetitions:
        raise ValueError("Repeated nonbasic and non-Nazgûl singleton violation: "+did)
    if (row["disposition"]!="HOLD_EXISTING_LIST_NO_SWAP" or
        row["approved_swaps"]!=0 or row["independent_pass_c_completed"] or
        row["complete_effect_aware_phase_b"] or
        row["current_entire_deck_legality_reverified"] or row["proxy_win_rate_claimed"] or
        len(row["source_specific_rules"])<5 or
        not all(row[k] for k in ("commander_mechanic","positive_case","cut_cost",
             "why_this_proposal_does_not_prove_an_upgrade","next_empirical_evidence"))):
        raise ValueError("Authored judgment illegitimately promoted to certificate: "+did)
    if row["proposed_add"] not in oracle or row["proposed_cut"] not in oracle:
        raise ValueError("Oracle verified candidate missing")
    for card in row["protected_interactions"]:
        if card not in names and card not in meta["commanders"]:
            raise ValueError("Protected named card absent from actual approved list: "+did+": "+card)
    return {"deck_id":did,"commander":meta["commanders"],"source_list_hash":meta["current_canonical_hash"],
      "recorded_source_raw_sha_not_rehashed":meta["source"]["recorded_sha256"],
      "physical_main_cards":len(names),"physical_commanders":len(deck.commanders),
      "cut_present_once_and_add_absent":True,
      "source_blueprint_sha256":sha(ROOT/"data/grixis/blueprints"/(meta["slug"]+".json")),
      "source_M5_candidate_verified":True,
      "oracle_add_cut_and_commander_bound":True,
      "authored_no_swap":True,
      "formal_independent_pass_c":False,"full_phase_b":False,"entire_list_current_legality":False}

def build():
    plan,reviews,reg,tri,track=map(read,(PLAN,REV,REG,TRI,TRACK))
    if (plan["cycle"]!=128 or plan["status"]!="PREREGISTERED_BEFORE_JUDGMENTS" or
        any(plan["authority"].values()) or reviews["cycle"]!=128 or
        reviews["reviewer_class"]!="ChatGPT engineering author, NOT independent critic" or
        reviews["review_count"]!=6 or len(reviews["rows"])!=6 or
        reviews["historical_authored_count_before"]!=15 or
        reviews["authored_count_after_if_verified"]!=21 or
        not all(x in (False,0) for x in reviews["global"].values()) or
        len(reg["decks"])!=62 or track["m6"]["formal_m6_certified_decks"]!=0 or
        track["m6"]["gates"][3]["completed"]!=15 or
        reg["program"]["milestones"]["M6"]["status"]!="in_progress" or
        reg["program"]["milestones"]["M7"]["status"]!="not_started" or
        set(EXPECTED)!={x["deck_id"] for x in plan["cases"]} or
        set(EXPECTED)!={x["deck_id"] for x in reviews["rows"]}):
        raise ValueError("M6 preregistration, retrospective count or authority drift")
    old={x["deck_id"] for x in c117.source_rows()}
    if old & set(EXPECTED) or len(old)!=15:
        raise ValueError("Cycle128 cases duplicate previously authored work")
    R=ev.Resolver()
    oracle=verified_oracle(R)
    queues={x["deck_id"]:x for x in tri["ordered_decks"]}
    cases={x["deck_id"]:x for x in plan["cases"]}
    receipts=[]
    for row in reviews["rows"]:
        did=row["deck_id"];meta=reg["decks"][did]
        bp=read(ROOT/"data/grixis/blueprints"/(meta["slug"]+".json"))
        receipts.append(verify(row,cases[did],meta,queues[did],bp,sim.load_deck(meta["slug"],R),oracle,R))
    if len(receipts)!=6 or len({x["deck_id"] for x in receipts})!=6:
        raise ValueError("Authored packet duplication")
    return {"schema_version":1,"cycle":128,"source_reviewed_count":6,
      "prior_authored_count":15,"authored_total_if_verified":21,
      "authored_only_receipts":receipts,
      "frozen_oracle":oracle,"source_sha256":{"plan":sha(PLAN),"authored_reviews":sha(REV),
        "registry":sha(REG),"triage":sha(TRI),"tracker":sha(TRACK)},
      "canonical_deck_changes":0,"approved_swaps":0,
      "formal_independent_pass_c_count":0,"complete_effect_aware_multiplayer_phase_b_count":0,
      "frozen_oracle_not_fresh_legality":True,
      "current_whole_list_legality_checked":False,"M6_accepted":False,"M7_started":False}
def main():
    a=argparse.ArgumentParser();a.add_argument("--build",action="store_true")
    a.add_argument("--check",action="store_true");args=a.parse_args()
    if not(args.build or args.check):a.error("Select --build and/or --check")
    txt=encode(build())
    if args.build:OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(txt,encoding="utf-8")
    if args.check and (not OUT.exists() or OUT.read_text(encoding="utf-8")!=txt):
        raise ValueError("Cycle128 deterministic Oracle/physical source replay differs")
    print("Cycle128: SIX new source-bound authored HOLD reviews, 21/62 total authored; NO independent Pass C, full Phase B or M6 promotion")
if __name__=="__main__":main()
