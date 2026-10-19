#!/usr/bin/env python3
"""Cycle118 read-only same-seed real-library goldfish proxy. NEVER Phase B, wins or owner approval.

The Enigma Jewel v1.1 model is explicitly neutralized because its restricted
activation-only mana and entering tapped are unsupported. This is conservative,
not an estimate of its full actual in-game utility.
"""
from __future__ import annotations
import argparse, hashlib, json, re, sys
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import evaluate_decklist as ev
import grixis_authority as ga
import grixis_sim as sim
import grixis_paired as paired

PLAN=ROOT/"data/grixis/m6/phase_b_plans/cycle118_supported_paired_goldfish_preregistered_01.json"
GUARD=ROOT/"data/grixis/m6/phase_b_plans/cycle118_simulator_coverage_guard_01.json"
PROTO=ROOT/"data/grixis/m6/independent_review_intake/cycle117_counterfactual_protocols_01.json"
REG=ROOT/"data/grixis/registry.json"
QUEUE=ROOT/"data/grixis/m6/phase_b_bounded/commander_first_readiness_62_01.json"
OUT=ROOT/"data/grixis/m6/phase_b_bounded/cycle118_supported_paired_goldfish_01.json"
NAMES={
"Gwendlyn_Di_Corci":("Gwendlyn Di Corci","Aphetto Alchemist","Opposition Agent"),
"Nicol_Bolas__the_Ravager":("Nicol Bolas, the Ravager // Nicol Bolas, the Arisen","Aetheric Amplifier","Mox Diamond"),
"Mai_and_Zuko":("Mai and Zuko","The Enigma Jewel // Locus of Enlightenment","An Offer You Can't Refuse")
}
AUTH={"can_change_decklists":False,"can_approve_or_lock":False,"can_certify_M6":False,
      "can_certify_independent_pass_c":False,"can_claim_effect_aware_multiplayer_results":False}

def read(p):return json.loads(Path(p).read_text(encoding="utf-8"))
def sha(p):return "sha256:"+hashlib.sha256(Path(p).read_bytes()).hexdigest()
def formatted(x):return json.dumps(x,sort_keys=True,indent=2,ensure_ascii=False)+"\n"

def replace_exact_slot(text,cut,add):
    # preserve commander line and every untouched physical slot; remove cut's old tags.
    lines=text.splitlines()
    match=re.compile(r"^1x?\s+"+re.escape(cut)+r"(?:\s*\[[^]]*\])?\s*$")
    found=[i for i,x in enumerate(lines) if match.fullmatch(x.strip())]
    if len(found)!=1:raise ValueError("Expected exactly one physical cut: "+cut)
    lines[found[0]]="1x "+add
    return "\n".join(lines)+"\n"

def verify_inputs(plan,guard,proto,reg,queue):
    spec=plan["engine"]
    if (plan["cycle"]!=118 or plan["status"]!="preregistered_before_execution"
       or plan["authority"]!=AUTH or len(plan["benchmarks"])!=3
       or spec["model_version"]!=sim.VERSION or sim.VERSION!="1.1"
       or spec["fixed_seed"]!=118026 or spec["samples_per_pair"]!=96 or spec["turns"]!=8
       or guard["cycle"]!=118 or guard["stage"]!="M6_paired_model_coverage_guard_registered_before_results"
       or guard["policy"]["when_card"]!=NAMES["Mai_and_Zuko"][1]
       or guard["policy"]["apply_to_challenger_card_model"]!={"source":None,"tapped":True,"v11":{}}
       or proto["cycle"]!=117 or proto["observed_game_results"]!=[]
       or proto["formal_independent_pass_c_completed"] or proto["phase_b_completed"]
       or len(reg["decks"])!=62 or reg["program"]["milestones"]["M6"]["status"]!="in_progress"
       or reg["program"]["milestones"]["M6"]["accepted_by"] is not None
       or set(NAMES)!={b["deck_id"] for b in plan["benchmarks"]}
       or len(queue["ordered_decks"])!=62):
        raise ValueError("Cycle118 prereg, model coverage, previous evidence or protected authority drift")
    for ix in range(6):
        if reg["program"]["milestones"][f"M{ix}"]["status"]!="accepted":
            raise ValueError("Source milestone acceptance drift")
    for b in plan["benchmarks"]:
        did=b["deck_id"];registered=reg["decks"][did]
        source=next((x for x in proto["protocols"] if x["deck_id"]==did),None)
        q=next((x for x in queue["ordered_decks"] if x["deck_id"]==did),None)
        if not source or not q:raise ValueError("Missing registered source scenario "+did)
        matches=[x for x in q["first_three_TO_REVIEW_NOT_TO_APPLY"] if x["swap_id"]==b["swap_id"]]
        if (len(matches)!=1 or b["commander"]!=registered["commanders"]
            or registered["commanders"]!=[NAMES[did][0]]
            or (b["add"],b["cut"])!=(NAMES[did][1],NAMES[did][2])
            or (matches[0]["add"],matches[0]["cut"])!=(b["add"],b["cut"])
            or source["candidate"]!=b["add"] or source["baseline"]!=b["cut"]
            or source["source_swap_id"]!=b["swap_id"] or
            b["approved_raw_sha256"]!=registered["source"]["recorded_sha256"] or
            b["approved_source_txt"]!=registered["source"]["path"] or
            registered["source"]["recorded_matches_raw"] is not True or
            b["canonical_logical_hash"]!=registered["current_canonical_hash"] or
            q["source_canonical_logical_hash"]!=b["canonical_logical_hash"]):
            raise ValueError("M5 source, canonical approval identity or swapped slot drift: "+did)

def oracle_gate(R):
    cardset=["Gwendlyn Di Corci","Aphetto Alchemist","Opposition Agent",
        "Nicol Bolas, the Ravager // Nicol Bolas, the Arisen","Aetheric Amplifier","Mox Diamond",
        "Mai and Zuko","The Enigma Jewel // Locus of Enlightenment","An Offer You Can't Refuse"]
    evidence={}
    for name in cardset:
        c=R.get(name)[0]
        if c["name"]!=name:raise ValueError("Frozen Oracle card resolution mismatch: "+name)
        t=c.get("oracle_text") or "\n".join((f.get("oracle_text") or "") for f in c.get("card_faces",[]))
        if not t:raise ValueError("Missing Oracle text: "+name)
        evidence[name]={"oracle_text_sha256":"sha256:"+hashlib.sha256(t.encode()).hexdigest()}
        if name=="The Enigma Jewel // Locus of Enlightenment":
            front=c["card_faces"][0]["oracle_text"].lower()
            if "enters tapped" not in front or "only to activate abilities" not in front:
                raise ValueError("The Enigma Jewel restricted-mana/tapped-entry Oracle does not match")
        if name=="Mox Diamond" and not ("discard a land card" in t.lower() and "{t}: add one mana of any color" in t.lower()):
            raise ValueError("Mox Diamond conditional fast mana drift")
    return evidence

def model_capability_guard(baseline,challenger,add):
    item=next((x for x in challenger.library if x["name"]==add),None)
    if item is None:raise ValueError("Candidate physically missing from challenger")
    native={"source":str(item["source"]),"tapped":item["tapped"],"v11":list(item.get("v11",{}))}
    if add=="The Enigma Jewel // Locus of Enlightenment":
        # CANNOT allow unrestricted Jewel mana to be spent on spells, nor count same-turn tapping.
        item["source"]=None
        item["tapped"]=True
        item["v11"]={}
        if item["source"] is not None:raise ValueError("Jewel restricted mana model contamination")
    return {"native_v11_model":native,
        "applied_guard":"Jewel inert castable artifact, does not provide general mana" if add.startswith("The Enigma Jewel") else "no special override",
        "no_activated_ability_model":True,
        "opponent_interaction_model":False,
        "no_effect_aware_combat_or_counterspell_model":True}

def one(b,R,reg):
    did=b["deck_id"];slug=b["slug"];cut=b["cut"];add=b["add"]
    original=ga.deck_block_text(slug)
    if ga.text_hash(original,R)!=b["canonical_logical_hash"]:
        raise ValueError("Physical repository deck does not match locked registry logical hash: "+did)
    baseline=sim.load_deck(slug,R,text=original)
    newtext=replace_exact_slot(original,cut,add)
    challenger=sim.load_deck(slug,R,text=newtext)
    if (baseline.N!=99 or challenger.N!=99 or len(baseline.commanders)!=1
        or len(challenger.commanders)!=1 or baseline.commanders[0]["name"]!=b["commander"][0]
        or ga.text_hash(newtext,R)==b["canonical_logical_hash"]):
        raise ValueError("99+1 or single-slot challenger altered commander: "+did)
    pre=Counter(x["name"] for x in baseline.library)
    aft=Counter(x["name"] for x in challenger.library)
    if pre[cut]!=1 or aft[cut] or aft[add]!=1 or pre[add] or (pre-Counter({cut:1}))!=(aft-Counter({add:1})):
        raise ValueError("Single physical candidate swap could not be isolated: "+did)
    native=model_capability_guard(baseline,challenger,add)
    scores,pairs=paired.paired(baseline,challenger,96,118026,turns=8,pairs=[(cut,add)],model="1.1")
    if pairs!=[(cut,add)]:raise ValueError("Paired seed alignment lost the exact slot")
    metrics={x["metric"]:x for x in scores}
    selected=["mana_spent_t1_t6","commander_cast_by_t4","mana_available_t4","win_turn_proxy_by_t8","mulligans_neg"]
    if not all(x in metrics for x in selected):raise ValueError("Missing preregistered fixed outcomes")
    if any(x["method"].find("paired goldfish")<0 or len(x["ci95"])!=2 for x in scores):
        raise ValueError("Unpaired or missing confidence interval in goldfish metrics")
    return {"deck_id":did,"commander":b["commander"],"source_sha256_recorded":b["approved_raw_sha256"],
       "raw_approved_list_bytes_not_freshly_downloaded":True,"list_logical_hash":b["canonical_logical_hash"],
       "source_project_markdown_sha256":"sha256:"+hashlib.sha256(original.encode()).hexdigest(),
       "source_deck_99_main_plus_one_commander":True,
       "baseline_vs_challenger":[cut,add],"paired_permutations":96,"model_version":"1.1",
       "seed":118026,"turns":8,"metrics":[metrics[x] for x in selected],
       "whole_deck_gameplay_decision":"NOT_SUPPORTED",
       "coverage":paired.coverage(baseline,challenger,pairs,"1.1"),
       "model_capability_guard":native,"real_multiplayer_game_results":0,
       "independent_pass_c_complete":False,"swap_authorized_or_applied":False}

def run():
    plan=read(PLAN);guard=read(GUARD);proto=read(PROTO);reg=read(REG);queue=read(QUEUE)
    verify_inputs(plan,guard,proto,reg,queue)
    R=ev.Resolver()
    oracle=oracle_gate(R)
    rows=[one(b,R,reg) for b in plan["benchmarks"]]
    if len(rows)!=3:raise ValueError("Missing three planned pairs")
    return {"cycle":118,"schema_version":1,"stage":"M6_GOLDFISH_PAIRED_EVIDENCE_NOT_EFFECT_AWARE_PHASE_B",
       "engine":"grixis_sim 1.1 via grixis_paired.paired (shared shuffle, seeded)",
       "analysis_note":"Modelled goldfish proxies only; 288 paired shuffles (576 game branches), zero live opponents and no outcomes for any of six Cycle117 effect-aware scenarios.",
       "authoritative_registry_sha256":sha(REG),"preregistered_plan_sha256":sha(PLAN),
       "preregistered_model_guard_sha256":sha(GUARD),"source_protocol_sha256":sha(PROTO),
       "original_model_sha256":sim.model_sha256(),
       "original_paired_code_sha256":sha(ROOT/"scripts/grixis_paired.py"),
       "frozen_oracle_text_evidence":oracle,"paired_results":rows,
       "completed_effect_aware_cycle117_scenarios":0,"actual_paired_goldfish_permutations":288,
       "actual_real_multiplayer_gameplay_results":0,"formal_independent_pass_c_count":0,
       "independent_reviewer_assigned":False,"approved_swaps":0,"canonical_decks_modified":0,
       "M6_accepted":False,"phase_B_certified":False,"whole_deck_current_legality_reverified":False,
       "authority":AUTH}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--build",action="store_true")
    p.add_argument("--check",action="store_true")
    args=p.parse_args()
    if not args.build and not args.check:p.error("Use --build or --check")
    d=formatted(run())
    if args.build:
        OUT.parent.mkdir(parents=True,exist_ok=True)
        OUT.write_text(d,encoding="utf-8")
    if args.check and (not OUT.is_file() or OUT.read_text(encoding="utf-8")!=d):
        raise ValueError("Paired reproducibility check failed")
    print("Cycle118: 3 source-bound real-library paired M3 goldfish comparisons complete; 288 paired shuffles; NOT a gameplay or independent-M6 decision")

if __name__=="__main__":main()
