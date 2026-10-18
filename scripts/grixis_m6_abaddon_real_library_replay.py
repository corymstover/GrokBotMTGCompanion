#!/usr/bin/env python3
"""Cycle 97: real 99-card seed-paired cascade hit replay with bounded real effects.

NOT sampled games, an optimizer, full effect coverage, win rates or Phase-B certification.
Full official library metadata determines cascade reveals; unsupported resolved effects
are never invented and are conservatively DECLINED under a preregistered policy.
"""
from __future__ import annotations
import argparse,collections,hashlib,json,random,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_sim as sim
import grixis_paired as paired
import evaluate_decklist as ev
from grixis_m6_abaddon_turn_state import TurnState,CARDS,Unsupported

PLAN=ROOT/"data/grixis/m6/phase_b_plans/abaddon_real_library_replay_01.json"
SOURCE=ROOT/"exports/grixis-archidekt/source-baseline/abaddon-the-despoiler.txt"
PREV=ROOT/"data/grixis/m6/phase_b_bounded/abaddon_turn_state_01.json"
OUT=ROOT/"data/grixis/m6/phase_b_bounded/abaddon_real_library_replay_01.json"
AUTH={"can_decide":False,"can_apply_swap":False,"can_change_canonical_list":False,"can_approve_or_lock":False}

def read(p):return json.loads(p.read_text(encoding="utf-8"))
def digest(p):return "sha256:"+hashlib.sha256(p.read_bytes()).hexdigest()
def serial(v):return json.dumps(v,sort_keys=True,indent=2,ensure_ascii=False)+"\n"

# No aliases for other double-faced cards: they are explicitly declined unless fully modeled.
FRONTS={"Birgi, God of Storytelling // Harnfel, Horn of Bounty":"Birgi, God of Storytelling"}
FORCED=("Boltwave","Flame Rift")
def profile_metadata(cards):
    d={}
    for c in cards:
        n=c["name"]
        entry={"mv":c["mv"],"land":bool(c["land"]),"front":FRONTS.get(n,n)}
        if n in d and d[n]!=entry:raise ValueError("Inconsistent frozen metadata for "+n)
        d[n]=entry
    return d

def stripped_library(order,slot):
    """Order is one entire 99-card shuffled source library, not a selected-card proxy."""
    kept=[];removed=collections.Counter()
    for c in order:
        if c["name"] in (*FORCED,slot):
            removed[c["name"]]+=1
        else:kept.append(c["name"])
    if len(kept)!=96 or removed!={n:1 for n in (*FORCED,slot)}:
        raise ValueError("Forced hand absent, duplicate or wrong library size: "+str(removed))
    return kept

class RealCascade(TurnState):
    def __init__(self,library,metadata,slot,opponents,turn6_mana,turn):
        # Cycle 96 strictly rejects unknown library effects. This adapter carries
        # all real library identities only to inspect CAST-TIME CASCADE reveals.
        super().__init__(hand=["Boltwave",slot,"Flame Rift"],mana=turn6_mana,
                         library=[],opponents=opponents,pilot=40,turn=turn,target_creature=True)
        self.library=list(library);self.metadata=metadata
        if any(n not in metadata for n in library):raise ValueError("Unresolved source library card")

    def resolve_top(self):
        if not self.stack or self.stack[-1]["kind"]!="cascade":
            return super().resolve_top()
        obj=self.stack.pop()
        revealed=[];hit=None
        while self.library:
            n=self.library.pop(0)
            meta=self.metadata[n]
            revealed.append(n)
            if not meta["land"] and meta["mv"]<obj["mv"]:
                hit=n;break
        if hit is None:
            self.events.append({"event":"real_cascade_no_eligible_hit","from":obj["name"],
                                "why":obj["why"],"revealed_count":len(revealed)})
        else:
            front=self.metadata[hit]["front"]
            supported=front in CARDS and not CARDS[front].get("synthetic",False)
            outcome="declined_unmodeled"
            if supported:
                self._cascade_offer=front
                try:
                    self.cast(front,origin="cascade_exile",free=True)
                    outcome="cast_supported"
                except ValueError:
                    outcome="declined_legal_constraint"
                finally:
                    self._cascade_offer=None
            self.events.append({"event":"real_cascade_offer","name":hit,"mv":self.metadata[hit]["mv"],
                   "from":obj["name"],"why":obj["why"],"supported":supported,"outcome":outcome})
            if outcome=="cast_supported":revealed.remove(hit)
        # Simulates one explicitly registered optional-cast policy; actual quality
        # or legality of unsupported effects cannot be inferred from this policy.
        self.rng.shuffle(revealed);self.library.extend(revealed)
        return obj

def replay(deck_cards,slot,metadata,scenario):
    p=scenario["setup"]
    t=RealCascade(deck_cards,metadata,slot,p["opponents_life"],
                  p["turn6_mana"],p["initial_turn"])
    t.place("Abaddon the Despoiler",entered=5)
    t.cast("Boltwave");t.resolve_all(250)
    t.cast(slot);t.resolve_all(250)
    t.next_turn()
    t.mana=dict(p["turn7_mana"])
    if slot in ("Heartless Hidetsugu","Tree of Perdition"):
        if scenario["removal"]=="remove_added_source_before_t7_activation":
            t.remove(slot)
        else:
            t.tap_activate(slot);t.resolve_all(250)
    if not t.over:
        t.cast("Flame Rift");t.resolve_all(250)
    offers=[e for e in t.events if e["event"]=="real_cascade_offer"]
    casts=[e for e in t.events if e["event"]=="cast"]
    return {"scripted_slot":slot,"removal":scenario["removal"],
        "hand_casts":sum(e["origin"]=="hand" for e in casts),
        "granted_cast_triggers":sum(e["granted_cascade"] for e in casts),
        "printed_cast_triggers":sum(e["printed_cascade"] for e in casts),
        "cascade_offers":len(offers),
        "supported_casts":sum(e["outcome"]=="cast_supported" for e in offers),
        "declined_unmodeled":sum(e["outcome"]=="declined_unmodeled" for e in offers),
        "declined_legal_constraint":sum(e["outcome"]=="declined_legal_constraint" for e in offers),
        "first_hit_names":[e["name"] for e in offers],
        "life_lost_conditional":t.lost,
        "events":t.events}

def basic_stats(rows):
    fieldnames=["hand_casts","granted_cast_triggers","printed_cast_triggers",
        "cascade_offers","supported_casts","declined_unmodeled","declined_legal_constraint"]
    n=len(rows);tot={k:sum(row[k] for row in rows) for k in fieldnames}
    hits=collections.Counter(x for r in rows for x in r["first_hit_names"])
    return {"samples":n,"event_totals":tot,
            "per_scripted_trial_means":{k:round(v/n,5) for k,v in tot.items()},
            "effect_coverage":{"offered":tot["cascade_offers"],
                "modeled_casts":tot["supported_casts"],
                "unmodeled_offers":tot["declined_unmodeled"],
                "legal_declines":tot["declined_legal_constraint"]},
            "actual_full_library_hit_names":dict(sorted(hits.items(),key=lambda x:(-x[1],x[0]))[:16])}

def run():
    plan=read(PLAN);prev=read(PREV)
    if (plan["cycle"]!=97 or plan["status"]!="preregistered_test_not_executed"
        or not plan["preregistered_before_simulation"]
        or plan["authority"]!=AUTH or prev["full_deck_paired_effect_simulator"]
        or prev["supports_improvement_claim"] or sim.model_sha256()!=plan["frozen_source"]["sim_sha256"]
        or digest(SOURCE)!="sha256:"+plan["baseline_export_sha256"]):
        raise ValueError("Preregistration, frozen model or canonical source drift")
    lines=SOURCE.read_text(encoding="utf-8").splitlines()
    if sum(int(l.split(" ",1)[0]) for l in lines)!=100 or lines[0]!="1 Abaddon the Despoiler [Commander]":
        raise ValueError("Official 100-card Abaddon list drift")
    resolver=ev.Resolver()
    a=sim.load_deck(plan["slug"],resolver)
    if a.N!=99 or [x["name"] for x in a.commanders]!=["Abaddon the Despoiler"]:
        raise ValueError("Baseline not a 99-card library plus Abaddon")
    samples=plan["sample_count_per_swap"]
    seed=plan["seed"]
    profiles=plan["fixed_setup"]["opponent_response_profiles"]
    report=[];baseline_sha_reference={}
    for hyp in plan["swap_hypotheses"]:
        cut,add=hyp["cut"],hyp["add"]
        if cut!="Bituminous Blast" or add not in ("Heartless Hidetsugu","Tree of Perdition"):
            raise ValueError("Unexpected swap hypothesis")
        variant_source=SOURCE.read_text(encoding="utf-8").replace("1 "+cut+"\n","1 "+add+"\n")
        if variant_source==SOURCE.read_text(encoding="utf-8"):raise ValueError("Swap missing")
        b=sim.load_deck(plan["slug"],resolver,text=variant_source)
        orig,variant,changes=paired.align(a,b,[(cut,add)])
        if orig.N!=99 or variant.N!=99 or changes!=[(cut,add)]:raise ValueError("Pair not full-99 aligned")
        if sum(orig.library[k]["name"]!=variant.library[k]["name"] for k in range(99))!=1:
            raise ValueError("Expected exactly one changing slot")
        meta=profile_metadata(orig.library+variant.library)
        scenario_reports={}
        for response in profiles:
            rows_base=[];rows_variant=[];trace_base=[];examples=[]
            sc={"setup":plan["fixed_setup"],"removal":response}
            for i in range(samples):
                sd=sim.seed_for(seed,i)
                perm=random.Random(sd^0x5EED).sample(range(99),99)
                s0=stripped_library([orig.library[j] for j in perm],cut)
                s1=stripped_library([variant.library[j] for j in perm],add)
                if s0!=s1:raise ValueError("Paired same-seed 96 library order drift")
                rb=replay(s0,cut,meta,sc)
                rv=replay(s1,add,meta,sc)
                trace_base.append({k:v for k,v in rb.items() if k!="events"})
                rows_base.append(rb);rows_variant.append(rv)
                if i<2:
                    examples.append({"sample":i,
                      "baseline":{"events":rb["events"][:50],"offers":rb["first_hit_names"]},
                      "challenger":{"events":rv["events"][:50],"offers":rv["first_hit_names"]}})
            trace_sha="sha256:"+hashlib.sha256(serial(trace_base).encode()).hexdigest()
            if response in baseline_sha_reference and baseline_sha_reference[response]!=trace_sha:
                raise ValueError("Baseline replay differs across independently compared variants")
            baseline_sha_reference[response]=trace_sha
            scenario_reports[response]={
                "baseline_trace_sha256":trace_sha,
                "baseline":basic_stats(rows_base),
                "challenger":basic_stats(rows_variant),
                "representative_traces":examples,
                "comparison_limitation":"Different scripted effects and unsupported-card declines; no improvement or win-rate inference"}
            print("Cycle 97 paired",add,"profile",response,"n",samples,flush=True)
        report.append({"swap":hyp,"profiles":scenario_reports,
                       "canonical_source_preserved":True,"source_cards_per_deck":100})
    return {"schema_version":1,
        "stage":"M6_Abaddon_seed_paired_real_99_cascade_hit_replay",
        "canonical_hash":plan["accepted_list_logical_hash"],"approved_raw_sha256":plan["accepted_list_raw_sha256"],
        "plan_sha256":digest(PLAN),"source_sha256":digest(SOURCE),
        "prior_turn_state_sha256":digest(PREV),"simulator_sha256":sim.model_sha256(),
        "seed":seed,"samples_per_swap_per_response_profile":samples,"response_profiles":profiles,
        "results":report,"baseline_trace_sha256_by_response_profile":baseline_sha_reference,
        "fixed_synthetic_setup":plan["fixed_setup"],"known_limitations":plan["explicit_limitations"],
        "full_99_library_shuffle_used":True,"limited_real_effect_resolver_used":True,
        "true_full_deck_gameplay_simulation":False,"full_phase_b_complete":False,
        "supports_improvement_claim":False,"can_certify_zero_improvement":False,"authority":AUTH}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--build",action="store_true");ap.add_argument("--check",action="store_true")
    args=ap.parse_args()
    if not(args.build or args.check):ap.error("need --build or --check")
    s=serial(run())
    if args.build:
        OUT.parent.mkdir(parents=True,exist_ok=True)
        OUT.write_text(s,encoding="utf-8")
    if args.check and (not OUT.exists() or OUT.read_text(encoding="utf-8")!=s):
        raise ValueError("Cycle 97 paired full-library effect replay drift")
    print("Cycle 97: paired full-99 cascade hit and limited effect replay; NO deck or milestone authority.")
if __name__=="__main__":main()
