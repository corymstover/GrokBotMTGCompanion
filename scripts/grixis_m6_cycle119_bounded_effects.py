#!/usr/bin/env python3
"""Cycle119: finite source-linked rule-event witnesses, NOT an MTG rules engine.

Each fixture's cards derive from one approved physical library or a single-slot
challenger; scripted opponent search/spell events are stipulated, NOT sampled.
No win rate, Phase B certificate, external Pass C, infinite loop or card swap.
"""
from __future__ import annotations
import argparse,copy,hashlib,json,sys
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import evaluate_decklist as ev
import grixis_authority as ga

PLAN=ROOT/"data/grixis/m6/phase_b_plans/cycle119_bounded_effect_states_preregistered_01.json"
SOURCE=ROOT/"data/grixis/registry.json"
QUEUE=ROOT/"data/grixis/m6/phase_b_bounded/commander_first_readiness_62_01.json"
ORIG=ROOT/"data/grixis/m6/independent_review_intake/cycle117_counterfactual_protocols_01.json"
OUT=ROOT/"data/grixis/m6/phase_b_bounded/cycle119_bounded_effect_witnesses_01.json"
AUTH={"can_change_canonical_lists":False,"can_approve_deck_swaps":False,
      "can_certify_independent_pass_c":False,"can_certify_phase_b":False,"can_accept_m6":False}
BASICS={"Plains","Island","Swamp","Mountain","Forest","Wastes"}
ORACLE={
"Gwendlyn Di Corci":["target player discards a card at random","activate only during your turn"],
"Aphetto Alchemist":["untap target artifact or creature"],
"Opposition Agent":["flash","you control your opponents while they're searching their libraries"],
"Pemmin's Aura":["enchanted creature gains shroud","untap enchanted creature"],
"Nicol Bolas, the Ravager // Nicol Bolas, the Arisen":["exile nicol bolas","return him to the battlefield transformed","activate only as a sorcery","draw two cards"],
"Mox Diamond":["discard a land card","add one mana of any color"],
"Aetheric Amplifier":["double the number of each kind of counter","activate only as a sorcery"],
"Mai and Zuko":["firebending 3","artifact spells as though they had flash"],
"The Enigma Jewel // Locus of Enlightenment":["enters tapped","only to activate abilities"],
"An Offer You Can't Refuse":["counter target noncreature spell","two treasure tokens"],
"Basalt Monolith":["doesn't untap during your untap step","add {c}{c}{c}","untap this artifact"],
"Rings of Brighthearth":["activate an ability","if it isn't a mana ability","pay {2}","copy that ability"]
}
EXACT={
"Gwendlyn_Di_Corci":("Gwendlyn Di Corci","Opposition Agent","Aphetto Alchemist"),
"Nicol_Bolas__the_Ravager":("Nicol Bolas, the Ravager // Nicol Bolas, the Arisen","Mox Diamond","Aetheric Amplifier"),
"Mai_and_Zuko":("Mai and Zuko","An Offer You Can't Refuse","The Enigma Jewel // Locus of Enlightenment")
}
class Blocked(ValueError):pass
def read(path):return json.loads(Path(path).read_text(encoding="utf-8"))
def sha(path):return "sha256:"+hashlib.sha256(Path(path).read_bytes()).hexdigest()
def encode(obj):return json.dumps(obj,ensure_ascii=False,sort_keys=True,indent=2)+"\n"

class World:
    """Finite scripted mana/tap/stack accounting; no general MTG action resolver."""
    def __init__(self,possessed,own_turn=True,main_phase=True,stack_empty=True,
                 controlled_since_turn=(),mana=None,target_hand=0,shrouded=()):
        self.cards=set(possessed)
        self.tapped=set()
        self.sick=set(self.cards)-set(controlled_since_turn)
        self.shrouded=set(shrouded)
        self.own_turn=own_turn
        self.main_phase=main_phase
        self.stack_empty=stack_empty
        self.mana=dict(mana or {})
        self.restricted_C=0
        self.target_hand=target_hand
        self.discard_activations=0
        self.untaps=0
        self.loyalty=0
        self.loyalty_abilities_used=0
        self.opponent_treasures=0
        self.opponent_search_controlled=0
        self.countered=0
        self.events=[]
    def require(self,test,reason):
        if not test:raise Blocked(reason)
    def has(self,name):self.require(name in self.cards,"not a real controlled fixture card: "+name)
    def tap(self,name):
        self.has(name)
        self.require(name not in self.tapped,"already tapped: "+name)
        if name in ("Gwendlyn Di Corci","Aphetto Alchemist"):
            self.require(name not in self.sick,"creature summoning sickness: "+name)
        self.tapped.add(name)
    def spend(self,price,restricted_allowed=False):
        """Fixed-color/ordinary pool, with restricted C for activated abilities only.
        Failed payments are atomic, not partial."""
        pool=dict(self.mana)
        limited=int(self.restricted_C)
        need=dict(price)
        for color in ("U","B","R"):
            n=int(need.pop(color,0))
            if pool.get(color,0)<n:raise Blocked("required colored mana unavailable: "+color)
            pool[color]=pool.get(color,0)-n
        generic=int(need.pop("generic",0))
        if need:raise Blocked("unsupported mana symbol: "+str(need))
        usable=sum(pool.values())+(limited if restricted_allowed else 0)
        self.require(usable>=generic,"insufficient payable mana")
        # use restricted first for generic activated costs; never for spell costs
        if restricted_allowed:
            r=min(generic,limited);limited-=r;generic-=r
        for color in ("C","U","B","R"):
            taken=min(generic,pool.get(color,0));pool[color]=pool.get(color,0)-taken
            generic-=taken
        self.require(generic==0,"payment invariant broken")
        self.mana=pool
        self.restricted_C=limited
    def event(self,name,**data):self.events.append({"action":name,**data})

def gw_discard(w):
    w.has("Gwendlyn Di Corci")
    w.require(w.own_turn,"Gwendlyn is own-turn only")
    w.require(w.target_hand>0,"no opponent hand card to discard")
    w.tap("Gwendlyn Di Corci")
    w.target_hand-=1;w.discard_activations+=1
    w.event("gwendlyn_targeted_random_discard_resolves",target_hand_remaining=w.target_hand)

def gw_alchemist(w):
    w.has("Aphetto Alchemist")
    w.require("Gwendlyn Di Corci" not in w.shrouded,"shroud prevents own Alchemist target")
    w.tap("Aphetto Alchemist")
    w.require("Gwendlyn Di Corci" in w.tapped,"target is not tapped for planned witness")
    w.tapped.remove("Gwendlyn Di Corci")
    w.untaps+=1;w.event("alchemist_untaps_gwendlyn")

def flash_agent_search(w):
    w.require(not w.own_turn,"stipulated response on an opponent turn")
    w.require("Opposition Agent" in w.cards,"Opposition Agent not held in this deck state")
    w.spend({"B":1,"generic":2},restricted_allowed=False)
    w.event("opposition_agent_flash_resolves")
    # Tutor spell resolves after Agent entered: it has a search event.
    w.opponent_search_controlled+=1
    w.event("agent_controls_opponent_during_one_stipulated_library_search")

def mox_diamond(w,spare_land):
    w.has("Mox Diamond")
    w.require(spare_land,"Mox Diamond requires discard land on replacement entry")
    w.event("mox_diamond_discard_land_and_enter")
    # Activated mana ability, no summoning sickness for noncreature artifact
    w.tap("Mox Diamond")
    w.mana["R"]=w.mana.get("R",0)+1
    w.event("mox_diamond_taps_for_red")

def cast_bolas_from_pool(w):
    w.spend({"generic":1,"U":1,"B":1,"R":1},restricted_allowed=False)
    w.event("ravager_four_mana_cast_possible")
    return True

def amplifier_loyalty(w,loyalty):
    w.has("Aetheric Amplifier")
    w.require(w.own_turn and w.main_phase and w.stack_empty,
         "Amplifier counters activated only at sorcery timing")
    w.require(loyalty>=0,"negative counters impossible")
    w.spend({"generic":4},restricted_allowed=False)
    w.tap("Aetheric Amplifier")
    w.loyalty=loyalty*2
    w.event("amplifier_doubles_existing_loyalty",before=loyalty,after=w.loyalty)
    # Does not grant extra loyalty ability
    return w.loyalty

def jewel_tap(w):
    w.has("The Enigma Jewel // Locus of Enlightenment")
    w.tap("The Enigma Jewel // Locus of Enlightenment")
    w.restricted_C+=2
    w.event("jewel_mana_only_for_activated_abilities",restricted_C=2)

def basalt_tap(w):
    w.tap("Basalt Monolith")
    w.mana["C"]=w.mana.get("C",0)+3
    w.event("basalt_taps_for_ordinary_C3",ordinary_C=w.mana["C"])

def basalt_untap_activate(w):
    w.has("Basalt Monolith")
    w.spend({"generic":3},restricted_allowed=True)
    w.event("basalt_untap_ability_on_stack")
    return ["basalt_original"]

def rings_copy(w,stack):
    w.has("Rings of Brighthearth")
    w.require(stack and stack[-1]=="basalt_original","only a nonmana activated untap ability may be copied here")
    w.spend({"generic":2},restricted_allowed=True)
    stack.append("basalt_copy")
    w.event("rings_copy_paid_two_and_added_copy_to_stack")

def resolve_untap(w,stack):
    w.require(stack and stack[-1] in ("basalt_original","basalt_copy"),"no legal untap effect on stack")
    top=stack.pop()
    w.tapped.discard("Basalt Monolith")
    w.untaps+=1
    w.event("basalt_untap_resolves",ability=top)

def an_offer(w,noncreature=True,spell_counterable=True):
    w.has("An Offer You Can't Refuse")
    w.require(noncreature,"An Offer can target noncreature spells only")
    w.spend({"U":1},restricted_allowed=False)
    if spell_counterable:
        w.countered+=1
        w.opponent_treasures+=2
        w.event("an_offer_counters_noncreature_spell",opponent_treasures=2)
    else:
        w.event("an_offer_resolves_spell_uncounterable",treasures=0)

def blocked_unchanged(w,func):
    before=copy.deepcopy(vars(w))
    try:func()
    except Blocked:return vars(w)==before
    raise ValueError("Expected illegality was accepted")

def check_plan(plan,registry,queue,proto):
    if (plan["cycle"]!=119 or plan["status"]!="preregistered_before_implementation"
        or plan["authority"]!=AUTH or len(plan["studies"])!=3 or len(plan["scenarios"])!=6
        or len(registry["decks"])!=62 or registry["program"]["milestones"]["M6"]["status"]!="in_progress"
        or registry["program"]["milestones"]["M6"]["accepted_by"] is not None
        or proto["cycle"]!=117 or proto["observed_game_results"]!=[] or proto["phase_b_completed"]
        or set(EXACT)!={x["deck_id"] for x in plan["studies"]}
        or {x["id"] for x in plan["scenarios"]}!={s["id"] for p in proto["protocols"] for s in p["scenarios"]}):
        raise ValueError("Cycle119 cannot bypass prior prereg, authority or unfinished Phase B status")
    for x in plan["studies"]:
        id=x["deck_id"];e=registry["decks"][id]
        p=next(y for y in proto["protocols"] if y["deck_id"]==id)
        q=next(y for y in queue["ordered_decks"] if y["deck_id"]==id)
        matches=[y for y in q["first_three_TO_REVIEW_NOT_TO_APPLY"] if y["swap_id"]==x["swap_id"]]
        if (len(matches)!=1 or x["commander"]!=[EXACT[id][0]] or
            (x["approved_cut"],x["candidate_add"])!=EXACT[id][1:] or
            x["source_logical_hash"]!=e["current_canonical_hash"] or
            x["source_raw_sha256"]!=e["source"]["recorded_sha256"] or
            x["source_file"]!=e["source"]["path"] or
            e["source"]["recorded_matches_raw"] is not True or
            (matches[0]["cut"],matches[0]["add"])!=EXACT[id][1:] or
            (p["baseline"],p["candidate"],p["source_swap_id"])!=(x["approved_cut"],x["candidate_add"],x["swap_id"])):
            raise ValueError("Source candidate or protected approval hash drift: "+id)

def card_text(resolver):
    out={}
    for name,required in ORACLE.items():
        card=resolver.get(name)[0]
        oracle=card.get("oracle_text") or "\n".join(face.get("oracle_text") or "" for face in card.get("card_faces",[]))
        if card.get("name")!=name or any(s.casefold() not in oracle.casefold() for s in required):
            raise ValueError("Frozen archived Oracle ability drift: "+name+" "+repr(oracle[:650]))
        out[name]={"text_sha256":"sha256:"+hashlib.sha256(oracle.encode()).hexdigest(),
                   "frozen_archive_not_live_current_legality":True}
    return out

def physical_inventory(study,resolver):
    txt=ga.deck_block_text(study["slug"])
    if ga.text_hash(txt,resolver)!=study["source_logical_hash"]:
        raise ValueError("Local approved source and authority logical hash disagree")
    entries=ga.list_entries(txt,resolver)
    main=Counter({name:qty for z,_,qty,name in entries if z=="main"})
    commanders=[name for z,_,qty,name in entries if z=="commander" for _ in range(qty)]
    if sum(main.values())!=99 or commanders!=study["commander"] or main[study["approved_cut"]]!=1 or main[study["candidate_add"]]!=0:
        raise ValueError("Real physical 99+1 source or single-cut count failed")
    if any(q>1 and n not in BASICS for n,q in main.items()):
        raise ValueError("Nonbasic singleton mismatch")
    return main

def gw_legal():
    base=World(["Gwendlyn Di Corci"],controlled_since_turn=["Gwendlyn Di Corci"],target_hand=3)
    alt=World(["Gwendlyn Di Corci","Aphetto Alchemist"],
       controlled_since_turn=["Gwendlyn Di Corci","Aphetto Alchemist"],target_hand=3)
    gw_discard(base);gw_discard(alt);gw_alchemist(alt);gw_discard(alt)
    assert base.discard_activations==1 and alt.discard_activations==2
    return {"baseline":{"gwendlyn_activations":base.discard_activations,"opponent_cards_discarded":3-base.target_hand,"events":base.events},
            "challenger":{"gwendlyn_activations":alt.discard_activations,"opponent_cards_discarded":3-alt.target_hand,"alchemist_untaps":alt.untaps,"events":alt.events}}

def gw_adverse():
    alt=World(["Gwendlyn Di Corci","Aphetto Alchemist","Pemmin's Aura"],
       controlled_since_turn=["Gwendlyn Di Corci","Aphetto Alchemist"],shrouded=["Gwendlyn Di Corci"])
    alt.tapped.add("Gwendlyn Di Corci")
    shroud_blocked=blocked_unchanged(alt,lambda:gw_alchemist(alt))
    base=World(["Opposition Agent"],own_turn=False,mana={"B":1,"C":2})
    flash_agent_search(base)
    assert shroud_blocked and base.opponent_search_controlled==1
    return {"baseline":{"opponent_searches_controlled":base.opponent_search_controlled,"events":base.events},
        "challenger":{"alchemist_target_legal":False,"blocked_no_mutation":shroud_blocked,"opponent_searches_controlled":0,"events":alt.events}}

def ravager_deploy():
    base=World(["Mox Diamond"],mana={"C":1,"U":1,"B":1})
    mox_diamond(base,spare_land=True);cast_bolas_from_pool(base)
    alt=World(["Aetheric Amplifier"],mana={"C":1,"U":1,"B":1})
    alt.spend({"generic":3},restricted_allowed=False)
    alt.event("amplifier_cast_cost_three_instead_of_zero")
    # Newly cast non-creature mana artifact may tap to generate one mana color,
    # but spending the three opening mana first leaves no full Bolas cost.
    alt.mana["R"]=alt.mana.get("R",0)+1
    can_cast=not blocked_unchanged(alt,lambda:cast_bolas_from_pool(alt))
    assert can_cast is False
    no_spare=World(["Mox Diamond"],mana={"C":1,"U":1,"B":1})
    assert blocked_unchanged(no_spare,lambda:mox_diamond(no_spare,spare_land=False))
    return {"baseline":{"spare_land_discarded":True,"ravager_cast_from_fixture":True,"events":base.events},
            "challenger":{"amplifier_cast_cost":3,"ravager_cast_from_fixture":False,
              "does_not_fix_turn_zero_without_mana":True,"events":alt.events},
            "adversarial_no_spare_land_mox_blocked":True}

def ravager_loyalty():
    base=World(["Mox Diamond"],mana={"C":4})
    base.loyalty=5;base.loyalty_abilities_used=1
    alt=World(["Aetheric Amplifier"],mana={"C":4},controlled_since_turn=["Aetheric Amplifier"])
    alt.loyalty=5;alt.loyalty_abilities_used=1
    amplifier_loyalty(alt,alt.loyalty)
    off_turn=World(["Aetheric Amplifier"],mana={"C":4},own_turn=False,main_phase=False)
    assert blocked_unchanged(off_turn,lambda:amplifier_loyalty(off_turn,5))
    assert alt.loyalty==10 and alt.loyalty_abilities_used==1
    return {"baseline":{"loyalty":base.loyalty,"loyalty_ability_activations_already_used":1},
      "challenger":{"loyalty":alt.loyalty,"loyalty_doubled_from":5,"generic_mana_spent":4,
         "loyalty_activations_added":alt.loyalty_abilities_used-1,"events":alt.events},
      "illegal_opponent_turn_amplifier_blocked":True}

def mai_ability():
    jewel="The Enigma Jewel // Locus of Enlightenment"
    base=World(["Basalt Monolith","Rings of Brighthearth"],controlled_since_turn=["Basalt Monolith","Rings of Brighthearth"])
    alt=World(["Basalt Monolith","Rings of Brighthearth",jewel],controlled_since_turn=["Basalt Monolith","Rings of Brighthearth",jewel])
    alt.tapped.add(jewel)
    entered_tapped_block=blocked_unchanged(alt,lambda:jewel_tap(alt))
    # Simulate the NEXT untap step, not flash-entry mana production.
    alt.tapped.discard(jewel);alt.event("jewel_untaps_on_later_turn")
    for w in (base,alt):
        basalt_tap(w)
        stack=basalt_untap_activate(w)
        if w is alt:
            jewel_tap(w)
            rings_copy(w,stack)
            # Before original untap, the COPY resolves and untaps Basalt.
            resolve_untap(w,stack)
            basalt_tap(w)
        else:
            assert blocked_unchanged(w,lambda:rings_copy(w,stack))
        resolve_untap(w,stack)
        assert not stack and "Basalt Monolith" not in w.tapped
    # At end of one bounded cycle alt has 3 ordinary C floating, baseline 0.
    assert base.mana.get("C",0)==0 and alt.mana.get("C",0)==3
    assert alt.restricted_C==0 and entered_tapped_block
    alt_no_spell=World([jewel],mana={},controlled_since_turn=[jewel])
    jewel_tap(alt_no_spell)
    restricted_spell_block=blocked_unchanged(alt_no_spell,lambda:alt_no_spell.spend({"generic":1},restricted_allowed=False))
    assert restricted_spell_block
    return {"baseline":{"ordinary_C_after_one_cycle":base.mana.get("C",0),"untap_resolutions":base.untaps,"events":base.events},
      "challenger":{"ordinary_C_after_one_cycle":alt.mana.get("C",0),"untap_resolutions":alt.untaps,
          "spent_restricted_C_on_rings_trigger":2,"spent_restricted_C_on_spell_cast":0,
          "entered_tapped_blocked_tap":entered_tapped_block,"restricted_spell_mana_blocked":restricted_spell_block,
          "events":alt.events}}

def mai_counter():
    base=World(["An Offer You Can't Refuse"],own_turn=False,main_phase=False,stack_empty=False,mana={"U":1})
    an_offer(base,noncreature=True)
    challenger=World(["The Enigma Jewel // Locus of Enlightenment"],own_turn=False,main_phase=False,
        stack_empty=False,mana={"U":1})
    assert "An Offer You Can't Refuse" not in challenger.cards
    # Actual opponent spell remains on stack for later response; no opponent AI.
    creature=World(["An Offer You Can't Refuse"],own_turn=False,mana={"U":1})
    assert blocked_unchanged(creature,lambda:an_offer(creature,noncreature=False))
    return {"baseline":{"noncreature_spell_countered":bool(base.countered),"opponent_treasures":base.opponent_treasures,
         "blue_mana_remaining":base.mana.get("U",0),"events":base.events},
       "challenger":{"noncreature_spell_countered_by_jewel":False,
          "opponent_treasures_created":0,"does_not_have_counterspell":True,"events":challenger.events},
       "creature_spell_untargetable_by_an_offer":True}

SCENARIOS={"gw-legal-untap":gw_legal,"gw-shroud-tutor":gw_adverse,
 "ravager-fast-deploy":ravager_deploy,"ravager-loyalty":ravager_loyalty,
 "mai-ability-mana":mai_ability,"mai-interaction-loss":mai_counter}

def produce():
    plan,reg,queue,proto=map(read,(PLAN,SOURCE,QUEUE,ORIG))
    check_plan(plan,reg,queue,proto)
    R=ev.Resolver()
    oracle=card_text(R)
    inventory={item["deck_id"]:physical_inventory(item,R) for item in plan["studies"]}
    required={
        "Gwendlyn_Di_Corci":["Pemmin's Aura","Opposition Agent"],
        "Nicol_Bolas__the_Ravager":["Mox Diamond"],
        "Mai_and_Zuko":["Rings of Brighthearth","Basalt Monolith","An Offer You Can't Refuse"]}
    for did,names in required.items():
        if not all(inventory[did][name]==1 for name in names):raise ValueError("Fixture missing genuine approved source card: "+did)
    records=[]
    for row in plan["scenarios"]:
        case=row["id"]
        result=SCENARIOS[case]()
        records.append({"scenario_id":case,"fixture_type":"finite_original_source_card_state",
          "source_protocol_id":case,"measured_state":result,
          "opponent_actions":"stipulated and static; no opponent AI",
          "source_draw_observations":0,"paired_simulated_full_games":0,
          "formal_independent_review":False})
    if set(SCENARIOS)!={x["scenario_id"] for x in records} or len(records)!=6:
        raise ValueError("Missing registered finite witness")
    return {"cycle":119,"schema_version":1,"stage":"M6_BOUNDED_EFFECT_WITNESS_NOT_COMPLETE_GAMEPLAY",
        "plan_sha256":sha(PLAN),"registry_sha256":sha(SOURCE),"queue_sha256":sha(QUEUE),
        "original_protocol_sha256":sha(ORIG),
        "oracle_evidence":oracle,"physical_source_decks":[{"deck_id":x["deck_id"],
            "recorded_raw_approved_sha256":x["source_raw_sha256"],
            "source_logical_hash":x["source_logical_hash"],"physical_main_count":sum(inventory[x["deck_id"]].values()),
            "commander_count":1} for x in plan["studies"]],
        "scenario_witnesses":records,"bounded_effect_scenarios_executed":6,
        "real_multiplayer_gameplay_results":0,"same_seed_full_effect_aware_paired_trials":0,
        "full_general_oracle_rules_engine":False,"independent_pass_c_count":0,
        "phase_b_certified":False,"owner_approved_swaps":0,"canonical_decks_modified":0,
        "m6_accepted":False,"accepted_m3_simulator_modified":False,"authority":AUTH,
        "limitations":["Manually stipulated card zones/mana, opponent hand, priority windows and responses; no random source draw or probabilistic tactical policy.",
          "Only named card abilities have action semantics. Not a complete MTG rules implementation, priority engine, multiplayer combat or real game evaluator.",
          "All six are positive/adverse fixtures, not actual same-seed Phase B games, win-rate estimates or deck superiority claims.",
          "Frozen Oracle does not itself certify every card's current legal status or future releases."]}

def main():
    a=argparse.ArgumentParser();a.add_argument("--build",action="store_true");a.add_argument("--check",action="store_true")
    args=a.parse_args()
    if not(args.build or args.check):a.error("Use --build or --check")
    txt=encode(produce())
    if args.build:
        OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(txt,encoding="utf-8")
    if args.check and (not OUT.exists() or OUT.read_text(encoding="utf-8")!=txt):
        raise ValueError("Cycle119 bounded event witness receipt failed deterministic replay")
    print("Cycle119: 6 source/Oracle-linked bounded effect witnesses complete. NO Phase B, win rates, independent Pass C, or card approvals.")
if __name__=="__main__":main()
