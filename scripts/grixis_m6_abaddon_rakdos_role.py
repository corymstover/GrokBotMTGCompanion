#!/usr/bin/env python3
"""Bounded Abaddon/Rakdos cost-reduction fixture; NOT game simulation.

Official rules: https://magic.wizards.com/en/news/feature/ravnica-remastered-release-notes
Only generic mana is reduced, after additional costs. Printed mana value is unchanged.
"""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASELINE = ROOT / "exports/grixis-archidekt/source-baseline/abaddon-the-despoiler.txt"
GRAPH = ROOT / "data/grixis/graph/abaddon-the-despoiler.json"

# Precisely scoped Oracle costs, separately verified against printed card text.
# Fields: (generic component, colored pips, is creature spell, printed mana value).
COSTS = {
    "Abaddon the Despoiler": (2, {"U": 1, "B": 1, "R": 1}, True, 5),
    "Neheb, the Eternal": (3, {"R": 2}, True, 5),
    "Loyal Subordinate": (2, {"B": 1}, True, 3),
    "Prosper, Tome-Bound": (2, {"B": 1, "R": 1}, True, 4),
    "Rakdos, Lord of Riots": (0, {"B": 2, "R": 2}, True, 4),
    "Aggravated Assault": (2, {"R": 1}, False, 3),
}


def payment(name: str, opponents_lost_this_turn: int, *, rakdos_present: bool,
            commander_tax: int = 0) -> dict:
    """Compute *cost only*; never asserts that colored sources or card access exist."""
    if name not in COSTS:
        raise ValueError("Outside verified Oracle cost fixture")
    if min(opponents_lost_this_turn, commander_tax) < 0:
        raise ValueError("Negative life loss or commander tax")
    if commander_tax and name != "Abaddon the Despoiler":
        raise ValueError("Commander tax scenario applies only to Abaddon")
    generic, colored, creature, mana_value = COSTS[name]
    eligible = rakdos_present and creature and name != "Rakdos, Lord of Riots"
    gross_generic = generic + commander_tax
    discount = min(gross_generic, opponents_lost_this_turn) if eligible else 0
    return {
        "name": name, "generic_due": gross_generic - discount,
        "colored_due": dict(colored), "discount": discount,
        "mana_value": mana_value, "rakdos_applies": eligible,
    }


def assault_activation_cost(opponents_lost_this_turn: int,
                            *, rakdos_present: bool) -> dict:
    """Noncreature activated ability cost remains {3}{R}{R}."""
    if opponents_lost_this_turn < 0:
        raise ValueError("Negative life loss")
    return {"generic_due": 3, "colored_due": {"R": 2},
            "rakdos_applies": False}


def baseline_creature_inventory() -> dict:
    """Read existing 100-card export + frozen graph; do not infer full cast access."""
    observed = Counter()
    commander_name = None
    for raw in BASELINE.read_text(encoding="utf-8").splitlines():
        if not raw.strip():
            continue
        match = re.fullmatch(r"(\d+) (.+?)( \[Commander\])?", raw.strip())
        if not match:
            raise ValueError("Malformed canonical source-export entry")
        count, name, commander_marker = match.groups()
        observed[name] += int(count)
        if commander_marker:
            if commander_name:
                raise ValueError("Multiple commanders")
            commander_name = name
    if sum(observed.values()) != 100 or commander_name != "Abaddon the Despoiler":
        raise ValueError("Wrong 100-card Abaddon baseline")
    if any(qty != 1 for name, qty in observed.items()
           if name not in {"Island", "Mountain", "Swamp"}):
        raise ValueError("Unexpected nonbasic duplication")
    graph = json.loads(GRAPH.read_text(encoding="utf-8"))
    creatures = [node["name"] for node in graph["nodes"]
                 if node["kind"] == "card" and "Creature" in node.get("type_line", "")]
    if len(creatures) != 17 or "Rakdos, Lord of Riots" not in creatures:
        raise ValueError("Frozen Abaddon creature-role graph changed")
    if not all(observed[name] == 1 for name in creatures):
        raise ValueError("Graph creature missing from the canonical source-export")
    discountable = sorted([commander_name] + [c for c in creatures
                                               if c != "Rakdos, Lord of Riots"])
    if len(discountable) != 17:
        raise ValueError("Unexpected Rakdos discount beneficiary count")
    return {"cards": sum(observed.values()), "distinct": len(observed),
            "creature_names_including_rakdos_and_commander": 18,
            "potential_discountable_creature_names": len(discountable),
            "potential_beneficiaries": discountable,
            "warning": "Potential only; conditional on drawing/casting Rakdos, surviving, life loss, and appropriate generic costs. Not frequency or value."}


def report() -> dict:
    scenarios = {}
    for loss in (0, 1, 3, 9):
        scenarios[str(loss)] = {
            name: payment(name, loss, rakdos_present=True)
            for name in ("Abaddon the Despoiler", "Neheb, the Eternal",
                         "Loyal Subordinate", "Prosper, Tome-Bound",
                         "Rakdos, Lord of Riots", "Aggravated Assault")
        }
    return {"evidence_class": "deterministic_rules_arithmetic_and_static_inventory",
            "authority": {"can_change_decklist": False, "can_certify_m6": False,
                          "can_approve_or_lock": False, "can_decide_swap": False},
            "inventory": baseline_creature_inventory(), "cost_cases": scenarios,
            "commander_recast_tax_4_at_lost_9": payment(
                "Abaddon the Despoiler", 9, rakdos_present=True, commander_tax=4),
            "assault_activation_at_lost_9": assault_activation_cost(
                9, rakdos_present=True),
            "no_measured_gameplay_or_challenger_superiority": True}


if __name__ == "__main__":
    print(json.dumps(report(), indent=2, sort_keys=True))
