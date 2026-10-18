#!/usr/bin/env python3
"""Cycle 98: Oracle-gated extension of Cycle 97's real-library cascade replay.

Adds ten exact card effects under documented deterministic policies. Does not alter
accepted Cycle 96/97 scripts or archived results. Source, seed, paired libraries and
scripted turn setup are otherwise unchanged. NOT a gameplay/win-rate simulator.
"""
from __future__ import annotations
import argparse,collections,hashlib,json,sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import evaluate_decklist as ev
import grixis_m6_abaddon_real_library_replay as previous
from grixis_m6_abaddon_turn_state import CARDS,Unsupported

PLAN=ROOT/"data/grixis/m6/phase_b_plans/abaddon_effect_coverage_01.json"
PREVIOUS=ROOT/"data/grixis/m6/phase_b_bounded/abaddon_real_library_replay_01.json"
SOURCE=ROOT/"exports/grixis-archidekt/source-baseline/abaddon-the-despoiler.txt"
OUT=ROOT/"data/grixis/m6/phase_b_bounded/abaddon_effect_coverage_01.json"
AUTH={"can_decide":False,"can_apply_swap":False,"can_change_canonical_list":False,"can_approve_or_lock":False}

# Only real oracle-backed effects. No card with an unimplemented mandatory
# behavior may be added here merely to make coverage metrics appear higher.
EXTRA_CARDS={
 "Sol Ring":{"mv":1,"cost":{"generic":1},"type":"artifact","mana_choices":["C"],"amount":2},
 "Arcane Signet":{"mv":2,"cost":{"generic":2},"type":"artifact","mana_choices":["U","B","R"],"amount":1},
 "Lotus Petal":{"mv":0,"cost":{"generic":0},"type":"artifact","mana_choices":["U","B","R"],"amount":1,"sacrifice":True},
 "Talisman of Creativity":{"mv":2,"cost":{"generic":2},"type":"artifact","mana_choices":["C","U","R"],"amount":1},
 "Talisman of Dominance":{"mv":2,"cost":{"generic":2},"type":"artifact","mana_choices":["C","U","B"],"amount":1},
 "Talisman of Indulgence":{"mv":2,"cost":{"generic":2},"type":"artifact","mana_choices":["C","B","R"],"amount":1},
 "Dark Ritual":{"mv":1,"cost":{"B":1,"generic":0},"type":"instant"},
 "Rite of Flame":{"mv":1,"cost":{"R":1,"generic":0},"type":"sorcery"},
 "Brainstorm":{"mv":1,"cost":{"U":1,"generic":0},"type":"instant"},
 "Ponder":{"mv":1,"cost":{"U":1,"generic":0},"type":"sorcery"}
}
# Register only in this new script's runtime; the accepted preceding scripts,
# source files, and their historical data remain byte-for-byte unchanged.
for _name,_entry in EXTRA_CARDS.items():
 if _name in CARDS:raise RuntimeError("Attempted to replace previously modeled card: "+_name)
 CARDS[_name]=_entry

def sha(p):return "sha256:"+hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text(encoding="utf-8"))
def encode(v):return json.dumps(v,indent=2,sort_keys=True,ensure_ascii=False)+"\n"

def check_frozen_oracle(plan):
    resolver=ev.Resolver()
    out={}
    for name,phrases in plan["frozen_oracle_assertions"].items():
        if name not in EXTRA_CARDS:raise ValueError("Non-preregistered Oracle card: "+name)
        card=resolver.get(name)[0]
        txt=card.get("oracle_text") or ""
        if not txt:raise ValueError("Missing frozen Oracle text: "+name)
        for p in phrases:
            if p.casefold() not in txt.casefold():
                raise ValueError("Frozen Oracle mismatch for "+name+": "+repr(p)+" not in "+repr(txt))
        mana_cost=card.get("mana_cost") or ""
        mvalue=int(card.get("cmc") or 0)
        if mvalue!=EXTRA_CARDS[name]["mv"]:
            raise ValueError("Mana value drift: "+name)
        out[name]={"oracle_sha256":"sha256:"+hashlib.sha256(txt.encode()).hexdigest(),
                   "mana_cost":mana_cost,"mana_value":mvalue,
                   "color_identity":sorted(card.get("color_identity") or [])}
    return out

class ExpandedCascade(previous.RealCascade):
    """Only the registered new effects; relies on Cycle 96 for cast-time triggers,
    payment, stack, cascade eligibility, supported earlier-card effects and game end.
    """
    def tap_mana(self,name,color):
        if name not in EXTRA_CARDS or EXTRA_CARDS[name]["type"]!="artifact":
            raise Unsupported("Mana tap of unmodeled artifact: "+name)
        p=self.board.get(name)
        if p is None or p["tapped"]:raise ValueError("Source absent or already tapped")
        entry=EXTRA_CARDS[name]
        if color not in entry["mana_choices"]:raise ValueError("Color not provided by mana ability")
        p["tapped"]=True
        if name.startswith("Talisman of ") and color!="C":
            self.pilot-=1
            self.over=self.pilot<=0 or all(v<=0 for v in self.opponents)
        self.mana[color]+=entry.get("amount",1)
        self.events.append({"event":"expanded_artifact_mana_ability","name":name,
             "produced":{color:entry.get("amount",1)},
             "pilot":self.pilot,"opponent_life_lost_this_turn":self.lost,
             "source_sacrificed":bool(entry.get("sacrifice"))})
        if entry.get("sacrifice"):self.remove(name)

    def _draw(self,n):
        if len(self.library)<n:
            # Player would lose for attempting to draw from an empty library at SBA.
            # Stop rather than treating a deckout as normal card draw.
            raise Unsupported("Drawing from library too small requires SBA modeling")
        drawn=self.library[:n]
        del self.library[:n]
        self.hand.extend(drawn)
        return drawn

    def _effect(self,name):
        if EXTRA_CARDS[name]["type"]=="artifact":
            self.place(name,entered=self.turn)
        elif name=="Dark Ritual":
            self.mana["B"]+=3
            self.events.append({"event":"expanded_ritual","name":name,"generated":{"B":3}})
        elif name=="Rite of Flame":
            extra=sum(x=="Rite of Flame" for x in self.graveyard)
            self.mana["R"]+=2+extra
            self.events.append({"event":"expanded_ritual","name":name,"generated":{"R":2+extra},
                                "prior_rites_in_graveyards":extra,
                                "opponents_graveyard_rites_assumed":0})
        elif name=="Brainstorm":
            drawn=self._draw(3)
            # Explicit legal policy: two highest-MV cards in hand, with
            # deterministic name tiebreak. This is NOT optimal play.
            top=sorted(self.hand,key=lambda n:(-self.metadata[n]["mv"],n))[:2]
            for n in top:self.hand.remove(n)
            self.library[:0]=top
            self.events.append({"event":"expanded_brainstorm","drawn":drawn,
                                "put_on_top":top,"selection_policy":"largest_mv_then_name"})
        elif name=="Ponder":
            looked=list(self.library[:3])
            drawn=self._draw(1)
            self.events.append({"event":"expanded_ponder","looked":looked,
                        "drawn":drawn,"selection_policy":"keep_original_top_three_order_no_shuffle"})
        else:raise Unsupported("Effect unregistered "+name)

    def resolve_top(self):
        if self.stack and self.stack[-1]["kind"]=="spell" and self.stack[-1]["name"] in EXTRA_CARDS:
            obj=self.stack.pop()
            name=obj["name"]
            self._effect(name)
            if EXTRA_CARDS[name]["type"]!="artifact":self.graveyard.append(name)
            self.events.append({"event":"spell_resolves","name":name,
                                "expanded_effect":True})
            return obj
        return super().resolve_top()

def scripted_followup(t):
    """A modeled Brainstorm can legally put the fixed Flame Rift back into
    the library. Never invent access to that card; record the missed follow-up.
    """
    if t.over:return False
    if "Flame Rift" not in t.hand:
        t.events.append({"event":"fixed_followup_not_held","name":"Flame Rift",
                          "reason":"changed_hand_after_resolved_card_selection"})
        return False
    t.cast("Flame Rift")
    t.resolve_all(250)
    return True

def replay98(deck_cards,slot,metadata,scenario):
    """Cycle 97 setup preserved, but actual changed hand state is respected."""
    p=scenario["setup"]
    t=ExpandedCascade(deck_cards,metadata,slot,p["opponents_life"],
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
    scripted_followup(t)
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
        "fixed_followup_unavailable":sum(e["event"]=="fixed_followup_not_held" for e in t.events),
        "life_lost_conditional":t.lost,
        "events":t.events}

def run():
    plan=read(PLAN);prev=read(PREVIOUS)
    if (plan["cycle"]!=98 or plan["status"]!="pre_registered_before_implementation"
        or plan["authority"]!=AUTH or prev["supports_improvement_claim"]
        or plan["samples"]!=240 or plan["seed"]!=97017
        or sha(SOURCE)!="sha256:"+plan["source_txt_sha256"]):
        raise ValueError("Cycle 98 preregistered authority/seed/source drift")
    oracle=check_frozen_oracle(plan)
    # The only intentional replay delta is support for the ten new effects.
    original=previous.RealCascade
    original_replay=previous.replay
    previous.RealCascade=ExpandedCascade
    previous.replay=replay98
    try:
        new=previous.run()
    finally:
        previous.replay=original_replay
        previous.RealCascade=original
    for outcome,prior in zip(new["results"],prev["results"]):
        if outcome["swap"]!=prior["swap"]:raise ValueError("Hypothesis pairing changed")
        for response in new["response_profiles"]:
            z=outcome["profiles"][response]
            p=prior["profiles"][response]
            if z["baseline"]["samples"]!=p["baseline"]["samples"]:
                raise ValueError("Mismatched per-swap samples")
            for label in ("baseline","challenger"):
                e=z[label]["effect_coverage"]
                if e["offered"]!=e["modeled_casts"]+e["unmodeled_offers"]+e["legal_declines"]:
                    raise ValueError("Hit support counts fail to conserve")
            z["cycle_97_comparison"]={
              "prior_baseline":p["baseline"]["effect_coverage"],
              "prior_challenger":p["challenger"]["effect_coverage"],
              "comparison_warning":"More card-effect coverage does not equal better deck performance."}
    return {"schema_version":1,"stage":"M6_Abaddon_10_added_oracle_verified_real_effects",
      "deck_id":plan["deck_id"],"canonical_hash":plan["canonical_hash"],
      "approved_raw_sha256":plan["approved_raw_sha256"],
      "frozen_oracle_receipts":oracle,
      "new_effect_cards":sorted(EXTRA_CARDS),
      "seed":plan["seed"],"samples_per_swap_per_profile":plan["samples"],
      "preregistration_sha256":sha(PLAN),"baseline_source_sha256":sha(SOURCE),
      "prior_cycle_97_sha256":sha(PREVIOUS),
      "results":new["results"],"baseline_replay_sha256_by_profile":
          new["baseline_trace_sha256_by_response_profile"],
      "limitations":plan["safety"],
      "turn_state_effect_extensions":True,
      "full_deck_gameplay_simulator":False,"full_phase_b_complete":False,
      "supports_improvement_claim":False,"formal_pass_c_complete":False,
      "can_certify_zero_improvement":False,"authority":AUTH}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--build",action="store_true")
    ap.add_argument("--check",action="store_true")
    args=ap.parse_args()
    if not (args.build or args.check):ap.error("requires --build or --check")
    content=encode(run())
    if args.build:OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(content,encoding="utf-8")
    if args.check and (not OUT.is_file() or OUT.read_text(encoding="utf-8")!=content):
        raise ValueError("Cycle 98 evidence reproducibility drift")
    print("Cycle 98: 10 frozen-Oracle-verified effect extensions with paired reproducible real-library replay. No approvals.")
if __name__=="__main__":main()
