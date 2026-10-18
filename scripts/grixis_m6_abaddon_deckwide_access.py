#!/usr/bin/env python3
"""Cycle 95: paired full-library gross-exposure proxies, not an effect-aware game/win-rate simulator.

We do not modify frozen grixis_sim 1.1. Its recorded first_seen and gross available mana
are NEITHER necessary NOR sufficient for legal casting (rituals/reducers/colored pips); no activation feeds back.
"""
from __future__ import annotations
import argparse,hashlib,json,random,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_sim as sim
import grixis_paired as paired
import grixis_m6_abaddon_followthrough as bounded
import evaluate_decklist as ev

PLAN=ROOT/"data/grixis/m6/phase_b_plans/abaddon_deckwide_access_01.json"
SOURCE=ROOT/"exports/grixis-archidekt/source-baseline/abaddon-the-despoiler.txt"
PRIOR=ROOT/"data/grixis/m6/phase_b_bounded/abaddon_followthrough_01.json"
OUT=ROOT/"data/grixis/m6/phase_b_bounded/abaddon_deckwide_access_01.json"
AUTH={"can_decide":False,"can_apply_swap":False,"can_change_canonical_list":False,"can_approve_or_lock":False}

def read(p):return json.loads(p.read_text(encoding="utf-8"))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(d):return json.dumps(d,indent=2,sort_keys=True,ensure_ascii=False)+"\n"

def early_seen_gross(rec,name,mv,through):
    """First gross pre-action exposure (seen and model mana >= MV), NOT a legal-cast gate."""
    seen=rec["first_seen"].get(name)
    if seen is None:return None
    for t in range(max(1,seen),min(through,len(rec["mana"]))+1):
        if rec["mana"][t-1]>=mv:return t
    return None

def summary(values):
    avg,ci=sim.mean_ci(values)
    return {"estimate":round(avg,5),"ci95":[round(ci[0],5),round(ci[1],5)],"successes":sum(values),
            "trials":len(values),"kind":"paired-draw-model-gross-mana-exposure-neither-necessary-nor-sufficient"}

def diff_stats(baseline,challenger):
    diffs=[b-a for a,b in zip(baseline,challenger)]
    mean,ci=sim.mean_ci(diffs)
    return {"baseline":round(sum(baseline)/len(baseline),5),
            "challenger":round(sum(challenger)/len(challenger),5),
            "paired_diff":round(mean,5),"paired_normal_ci95":[round(ci[0],5),round(ci[1],5)],
            "trials":len(diffs),"interpretation":"M3 v1.1 DEVELOPMENT proxy only, not life-loss or winning"}

def conditional_candidate(rec,name,mv,turns,probes):
    src=early_seen_gross(rec,name,mv,turns-1)
    active=None
    if src is not None:
        active=src+1  # no haste, source SURVIVED and was actually cast (both unverified)
    cmd=rec["commander_turn"]
    chain=False
    if active is not None:
        for t in range(active,turns+1):
            if cmd is not None and cmd<t and rec["mana"][t-1]>=1 and any(
                rec["first_seen"].get(n,999)<=t for n in probes):
                chain=True;break
    return {"source_gross_castable_by_t6":int(early_seen_gross(rec,name,mv,6) is not None),
            "conditional_next_turn_activation_by_t8":int(active is not None and active<=turns),
            "conditional_commander_prior_and_seen_1mv_followup_by_t8":int(chain)}

def blast_opportunity(rec,turns,threshold,target_available):
    """Counts NECESSARY gross access gate, with fixed hypothetical X and target availability."""
    first=early_seen_gross(rec,"Bituminous Blast",5,turns)
    if first is None or not target_available:
        return {"printed":False,"double":False}
    cmd=rec["commander_turn"]
    printed=True
    double=bool(cmd is not None and any(
        rec["mana"][t-1]>=5 and cmd<t and rec["first_seen"].get("Bituminous Blast",999)<=t
        for t in range(first,turns+1)) and threshold>=5)
    return {"printed":printed,"double":double}

def paired_one(champion,variant,cut,add,samples,seed,turns,probes):
    a,b,swaps=paired.align(champion,variant,[(cut,add)])
    if a.N!=99 or b.N!=99 or swaps!=[(cut,add)]:
        raise ValueError("Unpaired or incorrect 99-card candidate")
    # verify EXACTLY the card swap, including quantities.
    orig=[c["name"] for c in a.library];next_names=[c["name"] for c in b.library]
    assert sum(x!=y for x,y in zip(orig,next_names))==1
    records={"baseline_commander_t4":[],"variant_commander_t4":[],
             "baseline_mana_spent_t1_t6":[],"variant_mana_spent_t1_t6":[]}
    opp={k:[] for k in ("source_gross_castable_by_t6",
                       "conditional_next_turn_activation_by_t8",
                       "conditional_commander_prior_and_seen_1mv_followup_by_t8")}
    blast={"printed_target_present":[],"printed_no_target":[],"double_x0":[],"double_x5":[]}
    baseline_signatures=[]
    for i in range(samples):
        sd=sim.seed_for(seed,i)
        perm=random.Random(sd^0x5EED).sample(range(99),99)
        ra=sim.play_game(a,random.Random(sd),turns,perm=perm,model="1.1")
        rb=sim.play_game(b,random.Random(sd),turns,perm=perm,model="1.1")
        baseline_signatures.append([ra["commander_turn"],ra["first_seen"],ra["mana"],ra["spent"],ra["mulligans"]])
        records["baseline_commander_t4"].append(int(ra["commander_turn"] is not None and ra["commander_turn"]<=4))
        records["variant_commander_t4"].append(int(rb["commander_turn"] is not None and rb["commander_turn"]<=4))
        records["baseline_mana_spent_t1_t6"].append(sum(ra["spent"][:6]))
        records["variant_mana_spent_t1_t6"].append(sum(rb["spent"][:6]))
        s=conditional_candidate(rb,add,5 if add=="Heartless Hidetsugu" else 4,turns,probes)
        for k in opp:opp[k].append(s[k])
        b0=blast_opportunity(ra,turns,0,True)
        b5=blast_opportunity(ra,turns,5,True)
        blast["printed_target_present"].append(int(b0["printed"]))
        blast["printed_no_target"].append(int(blast_opportunity(ra,turns,5,False)["printed"]))
        blast["double_x0"].append(int(b0["double"]))
        blast["double_x5"].append(int(b5["double"]))
    return {
        "cut":cut,"add":add,"samples":samples,"seed":seed,
        "baseline_trace_sha256":"sha256:"+hashlib.sha256(dump(baseline_signatures).encode()).hexdigest(),
        "paired_development":{
            "commander_cast_by_t4":diff_stats(records["baseline_commander_t4"],records["variant_commander_t4"]),
            "mana_spent_t1_t6":diff_stats(records["baseline_mana_spent_t1_t6"],records["variant_mana_spent_t1_t6"])},
        "candidate_conditional_upper_bounds":{k:summary(v) for k,v in opp.items()},
        "removed_blast_access_upper_bounds":{k:summary(v) for k,v in blast.items()},
        "fixed_rule_witness":{
            "candidate_activation_life_loss_at_40_39_31":54 if add=="Heartless Hidetsugu" else 27,
            "candidate_self_damage":20 if add=="Heartless Hidetsugu" else 0,
            "candidate_removed_after_activation_life_loss":54 if add=="Heartless Hidetsugu" else 0,
            "candidate_removed_before_legal_activation_life_loss":0,
            "lost_printed_cascade_instances_if_bituminous_cast":1,
            "lost_removal_mode":"instant-speed creature damage; cannot cast without legal creature target",
            "hypothetical_blast_own_turn_hand_with_X_ge_5_has_two_cascade_triggers":True
        },
        "status":"bounded_observation_not_win_rate_or_swap_verdict"
    }

def run():
    plan=read(PLAN);previous=read(PRIOR)
    if (plan["status"]!="registered_before_test" or plan["authority"]!=AUTH
        or any(previous["authority"].values()) or previous["full_phase_b_complete"]
        or sim.model_sha256()!=plan["prior_simulator_sha256"]
        or plan["model"]!="1.1" or plan["samples"]!=800 or plan["seed"]!=95017
        or sha(SOURCE)!=plan["source_baseline_sha256"]):
        raise ValueError("Prereg, frozen model, or approved baseline drift")
    source=SOURCE.read_text(encoding="utf-8")
    if source.count("1 Bituminous Blast\n")!=1:
        raise ValueError("missing exactly one Bituminous Blast")
    resolver=ev.Resolver()
    champion=sim.load_deck(plan["slug"],resolver)
    if champion.N!=99 or [x["name"] for x in champion.commanders]!=["Abaddon the Despoiler"]:
        raise ValueError("Canonical Abaddon commander/list mismatch")
    probes=[x["card"] for x in plan["followup_probes"]]
    for name in probes:
        if name not in {x["name"] for x in champion.library}:raise ValueError("Missing probe "+name)
    results=[]
    for h in plan["hypotheses"]:
        if h["cut"]!="Bituminous Blast" or h["add"] not in ("Heartless Hidetsugu","Tree of Perdition"):
            raise ValueError("unregistered substitution")
        changed=source.replace("1 Bituminous Blast\n","1 "+h["add"]+"\n")
        variant=sim.load_deck(plan["slug"],resolver,text=changed)
        if variant.N!=99:raise ValueError("Unverified candidate library size")
        r=paired_one(champion,variant,h["cut"],h["add"],
                     plan["samples"],plan["seed"],plan["turns"],probes)
        results.append(r)
        print("paired draw/access",h["add"],"->",h["cut"],flush=True)
    # The unchanged champion MUST be bitwise reproducible across both candidate tests.
    if results[0]["baseline_trace_sha256"]!=results[1]["baseline_trace_sha256"]:
        raise ValueError("Champion baseline changed across candidate comparisons")
    for r in results:
        assert r["removed_blast_access_upper_bounds"]["printed_no_target"]["successes"]==0
        assert r["removed_blast_access_upper_bounds"]["double_x0"]["successes"]==0
        assert r["candidate_conditional_upper_bounds"]["conditional_commander_prior_and_seen_1mv_followup_by_t8"]["successes"]<=r["candidate_conditional_upper_bounds"]["conditional_next_turn_activation_by_t8"]["successes"]
    return {"schema_version":1,"stage":"M6_Abaddon_paired_full_99_exposure_proxies_NOT_effect_aware_game_simulation",
            "canonical_hash":plan["canonical_hash"],"approved_source_sha256":plan["approved_source_sha256"],
            "source_baseline_sha256":"sha256:"+sha(SOURCE),"preregistration_sha256":"sha256:"+sha(PLAN),
            "prior_rule_grid_sha256":"sha256:"+sha(PRIOR),"simulator_sha256":sim.model_sha256(),
            "samples_per_swap":plan["samples"],"seed":plan["seed"],"turns":plan["turns"],"model":plan["model"],
            "hypotheses":results,
            "limitations":plan["interpretation_boundaries"],
            "hard_unclosed_gates":["Actual hand-held spell casts, life-loss trigger-resolution, cascade hit quality and target availability in paired games are NOT modeled","Opponent policy, source survival probability and color-accurate spell follow-through are NOT modeled","Formal independent Pass C, I/J certificates, user acceptance remain pending"],
            "effect_aware_deckwide_paired_test_executed":False,
            "full_phase_b_complete":False,"supports_improvement_claim":False,"authority":AUTH}

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--build",action="store_true");ap.add_argument("--check",action="store_true")
    args=ap.parse_args()
    if not(args.build or args.check):ap.error("require --build or --check")
    s=dump(run())
    if args.build:OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(s,encoding="utf-8")
    if args.check and (not OUT.exists() or OUT.read_text(encoding="utf-8")!=s):
        raise ValueError("Cycle 95 paired evidence drift")
    print("Cycle 95: paired full-99 necessary-access bounds only; zero decision authority")
if __name__=="__main__":main()
