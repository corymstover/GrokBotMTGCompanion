#!/usr/bin/env python3
"""Cycle 100: conserved physical-card zone ledger, reusable for all 62 decks.

This is NOT a Magic game rules engine or a gameplay simulator. All abilities,
triggers, priority decisions, and unregistered casts fail closed. Printed mana
preflight is informational only; it cannot authorize a real spell cast.
"""
from __future__ import annotations
import hashlib,json,random
from collections import Counter

ZONES=("library","hand","battlefield","graveyard","exile","stack","command")
BASIC_MANA={"Plains":"W","Island":"U","Swamp":"B","Mountain":"R","Forest":"G","Wastes":"C"}
MANA=("W","U","B","R","G","C")

class BlockedAction(ValueError):
    """The action is unmodeled or fails a declared invariant; do not mutate state."""

def fingerprint(v):
    return "sha256:"+hashlib.sha256(json.dumps(v,sort_keys=True,ensure_ascii=False,separators=(",",":")).encode("utf-8")).hexdigest()

class Ledger:
    """A physical-card ledger. Unique IDs distinguish three Islands from each other.

    Every zone action verifies preconditions before mutation. No tokens or cards
    may be minted; a non-main companion remains external to this 100-card ledger.
    """
    def __init__(self,main_cards,commanders,seed=1):
        if not main_cards or not commanders:
            raise BlockedAction("Deck must have a physical main deck and commander")
        self.cards={}
        self.zones={z:[] for z in ZONES}
        for i,card in enumerate(main_cards):
            uid=f"m{i:03d}"
            self.cards[uid]=dict(card)
            self.zones["library"].append(uid)
        for i,card in enumerate(commanders):
            uid=f"c{i:03d}"
            self.cards[uid]=dict(card)
            self.zones["command"].append(uid)
        self.original={k:v["name"] for k,v in self.cards.items()}
        self.initial_card_count=len(self.cards)
        self.seed=int(seed)
        random.Random(self.seed).shuffle(self.zones["library"])
        self.mana={m:0 for m in MANA}
        self.tapped=set()
        self.turn=1
        self.land_played=False
        self.events=[]
        self.check()
        self.initial_inventory_hash=fingerprint(sorted(self.original.items()))

    def check(self):
        flat=[uid for z in ZONES for uid in self.zones[z]]
        if len(flat)!=self.initial_card_count or len(flat)!=len(set(flat)):
            raise AssertionError("Physical card duplication/loss in zones")
        if set(flat)!=set(self.original):raise AssertionError("Unknown/removed card ID")
        if any(self.cards[k]["name"]!=v for k,v in self.original.items()):
            raise AssertionError("Card names mutated")
        if any(k not in self.zones["battlefield"] for k in self.tapped):
            raise AssertionError("Tapped state outside battlefield")
        if any(not isinstance(v,int) or v<0 for v in self.mana.values()):
            raise AssertionError("Negative/noninteger mana")
        if set(self.mana)!=set(MANA):raise AssertionError("Mana key corruption")
        return True

    def zone_of(self,uid):
        if uid not in self.cards:raise BlockedAction("Unknown physical card")
        for z in ZONES:
            if uid in self.zones[z]:return z
        raise AssertionError("Missing physical card")

    def transfer(self,uid,source,destination,to_top=False):
        if source not in ZONES or destination not in ZONES or source==destination:
            raise BlockedAction("Invalid zone transfer")
        if uid not in self.cards or self.zone_of(uid)!=source:
            raise BlockedAction("Card is not in stated source zone")
        self.zones[source].remove(uid)
        if destination=="library" and to_top:self.zones[destination].insert(0,uid)
        else:self.zones[destination].append(uid)
        self.tapped.discard(uid)
        self.events.append({"event":"physical_transfer","id":uid,"from":source,"to":destination,
                            "authority":"bookkeeping-only-not-legality-proof"})
        self.check()

    def draw(self,n=1):
        if not isinstance(n,int) or n<0:raise BlockedAction("Invalid draw count")
        if len(self.zones["library"])<n:
            raise BlockedAction("Deckout behavior not simulated; no partial draws")
        results=[]
        for _ in range(n):
            uid=self.zones["library"][0]
            self.transfer(uid,"library","hand")
            results.append(uid)
        return results

    def drawn_names(self,ids):
        return [self.cards[uid]["name"] for uid in ids]

    def play_basic(self,uid,own_turn=True,main_phase=True,stack_empty=True):
        if uid not in self.cards:raise BlockedAction("Unknown card")
        card=self.cards[uid]
        if card["name"] not in BASIC_MANA or not card.get("land",False):
            raise BlockedAction("Conditional/nonbasic land ETB/play not modeled")
        if self.zone_of(uid)!="hand" or self.land_played or not own_turn or not main_phase or not stack_empty:
            raise BlockedAction("Basic land play not available")
        self.transfer(uid,"hand","battlefield")
        self.land_played=True
        self.events.append({"event":"basic_land_play","name":card["name"],"id":uid,"turn":self.turn})
        return True

    def tap_basic(self,uid):
        if uid not in self.cards:raise BlockedAction("Unknown card")
        card=self.cards[uid]
        if card["name"] not in BASIC_MANA or self.zone_of(uid)!="battlefield" or uid in self.tapped:
            raise BlockedAction("Basic mana tap unavailable")
        self.tapped.add(uid)
        symbol=BASIC_MANA[card["name"]]
        self.mana[symbol]+=1
        self.events.append({"event":"basic_mana","id":uid,"produced":symbol})
        self.check()
        return symbol

    def next_turn(self):
        if self.zones["stack"]:raise BlockedAction("Stack/priority transition is unmodeled")
        self.turn+=1
        self.land_played=False
        self.tapped.clear()
        self.mana={m:0 for m in MANA}
        self.events.append({"event":"turn_boundary","turn":self.turn,
            "warning":"no upkeep,drawing,opponents,or_triggered_abilities_executed"})
        self.check()

    def printed_cost_probe(self,uid):
        """Static pip matching is only an informational preflight.

        Not a legal cast: reducers/tax/alternative costs/costs of abilities/X
        and priority are not considered. Never deducts mana or moves cards.
        """
        if uid not in self.cards:raise BlockedAction("Unknown card")
        card=self.cards[uid]
        if card.get("land"):return {"status":"not_a_spell","legal_cast":False}
        c=card.get("cost",{})
        if not isinstance(c,dict) or not isinstance(c.get("generic"),int):
            return {"status":"unmodeled_cost","legal_cast":False}
        if c.get("life",0):
            return {"status":"unmodeled_phyrexian_payment","legal_cast":False}
        pips=c.get("pips",[])
        if not all(isinstance(p,(tuple,list,frozenset,set)) and p and set(p)<=set(MANA) for p in pips):
            return {"status":"unmodeled_pips","legal_cast":False}
        import grixis_sim
        units=[frozenset((m,)) for m in MANA for _ in range(self.mana[m])]
        ok=grixis_sim.can_pay(c,units) is not None
        return {"status":"printed_mana_only_affordable" if ok else "printed_mana_only_unaffordable",
                "legal_cast":False,"printed_mana_affordable":ok,
                "limitations":"excludes extra/alternate/X costs, priority, effects and all adjustments"}

    def refuse_effect(self,uid,reason="card effects not represented"):
        if uid not in self.cards:raise BlockedAction("Unknown card")
        old=self.zone_of(uid)
        record={"status":"blocked_unmodeled_effect","name":self.cards[uid]["name"],
                "id":uid,"zone_unchanged":old,"reason":reason}
        self.events.append(record)
        self.check()
        return record

    def receipt(self):
        self.check()
        return {"count":self.initial_card_count,
                "zone_counts":{z:len(self.zones[z]) for z in ZONES},
                "commander_names":[self.cards[i]["name"] for i in self.zones["command"]],
                "inventory_hash":self.initial_inventory_hash,
                "zone_fingerprint":fingerprint(self.zones),
                "physical_id_count":len(set(self.cards)),
                "turn":self.turn,"mana":dict(self.mana),
                "unmodeled_effects":sum(e.get("status")=="blocked_unmodeled_effect" for e in self.events)}
