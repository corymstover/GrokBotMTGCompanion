#!/usr/bin/env python3
"""Bounded exact-resources Station/Petal/Breach trace; NOT a game or win-rate simulator."""
import argparse,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"exports/grixis-archidekt/source-baseline/abaddon-the-despoiler.txt"
OUT=ROOT/"data/grixis/m6/phase_b_bounded/abaddon_station_breach_line.json"
def enc(o):return json.dumps(o,sort_keys=True,indent=1,ensure_ascii=False)+"\n"
def sha(p):return "sha256:"+hashlib.sha256(p.read_bytes()).hexdigest()
def check_list():
    lines=[s.split(" ",1)[-1].split(" [")[0] for s in BASE.read_text().splitlines() if s.strip()]
    needed=["Underworld Breach","Lotus Petal","Brain Freeze","Lion\u0027s Eye Diamond"]
    assert all(lines.count(x)==1 for x in needed)
    assert lines.count("Grinding Station")==0
def trace(library,grave_other=0,petal_field=True,breach=True,station=True,exile_mill=False):
    if min(library,grave_other)<0: raise ValueError("negative resource")
    n=0;milled=0;escaped=0;station_untapped=station;petal_present=petal_field
    if not(breach and station): return {"cycles":0,"self_milled":0,"escape_casts":0,"library_left":library,"stopped":"missing_breach_or_station"}
    if not petal_present and grave_other>=3:
        grave_other-=3;petal_present=True;escaped+=1
    if not petal_present:return {"cycles":0,"self_milled":0,"escape_casts":0,"library_left":library,"stopped":"no_initial_petal_or_escape_fuel"}
    while petal_present and station_untapped and library>0:
        # Activate Station: tap it and sacrifice Petal as its cost; resolution mills 3.
        petal_present=False;station_untapped=False
        k=min(3,library);library-=k;milled+=k;n+=1
        if not exile_mill: grave_other+=k
        # Underworld Breach: Petal escape costs 0 mana and exiles THREE OTHER grave cards.
        if grave_other<3:break
        grave_other-=3;escaped+=1;petal_present=True
        # Petal enters: Grinding Station optional untap trigger resolves.
        station_untapped=True
    return {"cycles":n,"self_milled":milled,"escape_casts":escaped,
       "storm_added_by_petal_escapes":escaped,"library_left":library,
       "other_graveyard_cards_left":grave_other,"petal_on_battlefield":petal_present,
       "station_untapped":station_untapped,"net_mana":0,
       "brain_freeze_cast":False,"opponents_milled":0,"win_proven":False,
       "finite_and_library_bounded":True}
def data():
    check_list()
    d={"schema_version":1,"stage":"M6_Grinding_Station_Breach_conditional_trace",
       "slug":"abaddon-the-despoiler","baseline_sha256":sha(BASE),
       "covered_hypothesis":"swap:abaddon-the-despoiler:m5:1eb1c0ea9334",
       "present_baseline_engine":["Underworld Breach","Lotus Petal","Brain Freeze","Lion\u0027s Eye Diamond"],
       "missing_proposed_piece":"Grinding Station",
       "examples":{"ninety_card_library":trace(90),
         "one_card_library":trace(1),
         "petal_initially_in_grave_with_no_fuel":trace(90,petal_field=False),
         "petal_in_grave_with_three_fuel":trace(90,grave_other=3,petal_field=False),
         "graveyard_exile_replacement":trace(90,exile_mill=True),
         "no_breach":trace(90,breach=False)},
       "required_for_finisher":["Brain Freeze cast requires {1}{U} (or equivalent) plus priority",
         "Storm copies and targeting must be sufficient for opponents\u0027 actual library sizes",
         "If Brain Freeze is escaped from graveyard, three OTHER cards and mana must be available",
         "Petal cannot both pay the Station sacrifice cost and produce mana in the same iteration",
         "Opponents can respond to spells, abilities and graveyard recursion"],
       "limitations":["Conditional exact loop only; not a full game, infinite library, or victory proof",
         "Station can mill at most three fresh cards per sacrifice and the library is finite",
         "Artifact escape must exile three other cards; interruption/replacement effects may terminate loop",
         "Does not calculate a probability or value of the proposed replacement cut Chrome Mox"],
       "supports_improvement_claim":False,"phase_b_complete":False,
       "authority":{"can_decide":False,"can_apply_swap":False,"can_approve_or_lock":False}}
    assert d["examples"]["ninety_card_library"]["cycles"]==30
    assert d["examples"]["ninety_card_library"]["self_milled"]==90
    assert d["examples"]["ninety_card_library"]["net_mana"]==0
    assert d["examples"]["ninety_card_library"]["win_proven"] is False
    assert d["examples"]["petal_initially_in_grave_with_no_fuel"]["cycles"]==0
    assert d["examples"]["graveyard_exile_replacement"]["cycles"]==1
    return d
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--build",action="store_true");ap.add_argument("--check",action="store_true");a=ap.parse_args()
    if not(a.build or a.check):ap.error("need --build/--check")
    d=data()
    if a.build: OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(enc(d))
    if a.check and (not OUT.is_file() or OUT.read_text()!=enc(d)): raise ValueError("trace drift")
    print("Station+Petal+Breach bounded:",d["examples"]["ninety_card_library"],"NO WIN CLAIM")
if __name__=="__main__":main()
