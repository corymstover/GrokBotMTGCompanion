#!/usr/bin/env python3
"""100-card physical Abaddon slot access with conservative source-paid snapshots.

Not full Magic gameplay: no actual spell casts, stack, opponent policy, tutors,
mana rocks/rituals, extra draw, cascade, mulligans, conditional life loss or wins.
All three variants have a verified frozen 99-card physical main library and the
same 1-card commander zone. Each land drop/fetch follows an explicit fixed policy.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import itertools
import json
import random
import re
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from grixis_m6_priority_nonbasic import LANDS, TYPED
from grixis_m6_fetch_city_tomb import FETCHES
PLAN = ROOT / "data/grixis/m6/phase_b_plans/abaddon_assault_mana_access_20261021.json"
SPELL_COST = {
    "Abaddon the Despoiler": (5, (1, 1, 1)),   # {2}{U}{B}{R}
    "Aggravated Assault": (3, (0, 0, 1)),       # {2}{R}
    "Rakdos, Lord of Riots": (4, (0, 2, 2)),    # {B}{B}{R}{R}
    "Loyal Subordinate": (3, (0, 1, 0)),        # {2}{B}
    "Neheb, the Eternal": (5, (0, 0, 2)),       # {3}{R}{R}
}
SPECIAL_LANDS = {
    "Ancient Tomb": ("C",), "City of Brass": ("U", "B", "R"),
    "Exotic Orchard": (), "Otawara, Soaring City": ("U",),
    "Takenuma, Abandoned Mire": ("B",),
    "Urborg, Tomb of Yawgmoth": ("B",),
}
BASICS = {"Island": "U", "Swamp": "B", "Mountain": "R"}
LANDS_KNOWN = set(LANDS) | set(BASICS) | set(FETCHES) | set(SPECIAL_LANDS)
TYPED_KNOWN = {**TYPED, **{name: name for name in BASICS}}
TARGETS = ("Neheb, the Eternal", "Loyal Subordinate", "Aggravated Assault")


def frozen_source():
    plan = json.loads(PLAN.read_text(encoding="utf-8"))
    raw = (ROOT / plan["source_path"]).read_bytes()
    if hashlib.sha256(raw).hexdigest() != plan["source_sha256"]:
        raise ValueError("Frozen source SHA drift")
    entries = []
    commander = []
    for line in raw.decode("utf-8").splitlines():
        m = re.fullmatch(r"(\d+) (.+?)(?: \[Commander\])?", line)
        if not m:
            raise ValueError("Source line cannot be parsed: " + line)
        qty, name = int(m.group(1)), m.group(2)
        if "[Commander]" in line:
            commander.extend([name] * qty)
        else:
            entries.extend([name] * qty)
    if commander != ["Abaddon the Despoiler"] or len(entries) != 99:
        raise ValueError("Baseline commander/physical main count changed")
    names = Counter(commander + entries)
    if sum(names.values()) != 100 or len(names) != 94:
        raise ValueError("100-card or frozen 94-identity count changed")
    if {n for n, q in names.items() if q > 1} != set(BASICS):
        raise ValueError("Only three Grixis basic land types may repeat")
    if any(names[x] != 3 for x in BASICS):
        raise ValueError("Basics changed")
    if sum(n in LANDS_KNOWN for n in entries) != 34:
        raise ValueError("Expected 34 physical, source-recognized lands")
    if not all(entries.count(n) == 1 for n in SPELL_COST if n != "Aggravated Assault" and n != "Abaddon the Despoiler"):
        raise ValueError("Protected named spells are not singletons")
    return plan, entries


def libraries(entries, plan):
    variants = {}
    for v in plan["variants"]:
        lib = list(entries)
        if v["cut"]:
            if lib.count(v["cut"]) != 1 or v["add"] in lib:
                raise ValueError("Incorrect frozen swap slot")
            lib[lib.index(v["cut"])] = v["add"]
        if len(lib) != 99 or sum(lib.count(n) for n in BASICS) != 9:
            raise ValueError("Bad library size")
        c = Counter(lib)
        if {k for k, qty in c.items() if qty > 1} != set(BASICS):
            raise ValueError("Singleton drift")
        variants[v["id"]] = lib
    return variants


def land_colors(name, urborg=False):
    if name == "Ancient Tomb":
        opts = [("C", "C")]  # One activation, two generic units
    elif name in BASICS:
        opts = [(BASICS[name],)]
    elif name in SPECIAL_LANDS:
        opts = [(c,) for c in SPECIAL_LANDS[name]]
    elif name in LANDS:
        opts = [(c,) for c in LANDS[name][0]]
    else:
        raise ValueError("Unsupported land: " + name)
    if urborg and ("B",) not in opts:
        opts.append(("B",))  # Alternative tap ability, never extra mana
    return opts


def source_payable(battlefield, name):
    total_req, colored = SPELL_COST[name]
    present = [n for n, tapped in battlefield if not tapped]
    urborg = "Urborg, Tomb of Yawgmoth" in [n for n, _ in battlefield]
    possible = {(0, 0, 0, 0)}  # total units, U, B, R assigned (clamped)
    for land in present:
        opts = land_colors(land, urborg)
        if not opts:
            continue
        follow = set(possible)
        for total, u, b, r in possible:
            for units in opts:
                new = (
                    min(total_req, total + len(units)),
                    min(colored[0], u + units.count("U")),
                    min(colored[1], b + units.count("B")),
                    min(colored[2], r + units.count("R")),
                )
                follow.add(new)
        possible = follow
    return (total_req, *colored) in possible


def tapped_on_entry(name):
    return name == "Xander's Lounge" or name in LANDS and LANDS[name][1] == "tapped"


def eligible_fetch_targets(fetch, library):
    want = set(FETCHES[fetch])
    available = [n for n in library if n in TYPED_KNOWN
                 and set(TYPED_KNOWN[n].split()) & want]
    # Fetch only typed duals/shocks and basic lands; normal policy pays shock life.
    return sorted(available, key=lambda n: (tapped_on_entry(n),
                  -len(land_colors(n)), n))


def land_rank(name, library):
    if name in FETCHES:
        opts = eligible_fetch_targets(name, library)
        if not opts:
            return (2, 0, name)
        return (int(tapped_on_entry(opts[0])), -len(land_colors(opts[0])), name)
    return (int(tapped_on_entry(name)), -len(land_colors(name)), name)


def play_land(hand, library, battlefield, seed, turn):
    choices = [n for n in hand if n in LANDS_KNOWN]
    if not choices:
        return 0, None
    land = min(choices, key=lambda n: land_rank(n, library))
    hand.remove(land)
    if land in FETCHES:
        target = eligible_fetch_targets(land, library)
        if target:
            chosen = target[0]
            library.remove(chosen)
            battlefield.append((chosen, tapped_on_entry(chosen)))
        # Actual fetch removes a land from library and shuffles residual physical IDs.
        random.Random(seed ^ (turn * 0x9E3779B1)).shuffle(library)
        return 1, land
    battlefield.append((land, tapped_on_entry(land)))
    return 0, land


def draw_only_probabilities(turn):
    # No mulligans / extra draw: n=7+turn of N=99, 3 distinct library cards.
    n = 7 + turn
    return {
        "one_named_singleton": str(Fraction(n, 99)),
        "two_named_singletons": str(Fraction(n * (n - 1), 99 * 98)),
        "three_named_singletons": str(Fraction(n * (n - 1) * (n - 2), 99 * 98 * 97)),
    }


def trial(lib, seed, checkpoints):
    rng = random.Random(seed)
    deck = list(lib)
    rng.shuffle(deck)
    hand, deck = deck[:7], deck[7:]
    battlefield = []
    metrics = {}
    fetches = 0
    for turn in range(1, max(checkpoints) + 1):
        battlefield = [(n, False) for n, _ in battlefield]
        hand.append(deck.pop(0))  # Multiplayer draw step on own first turn
        count, _ = play_land(hand, deck, battlefield, seed, turn)
        fetches += count
        if turn not in checkpoints:
            continue
        slot = "Aggravated Assault" if "Aggravated Assault" in lib else "Rakdos, Lord of Riots"
        # Source-paid results mean individually affordable at this snapshot.
        all_seen = all(n in hand for n in TARGETS)
        all_payable = all(source_payable(battlefield, n) for n in TARGETS)
        metrics[turn] = {
            "slot_seen": slot in hand,
            "slot_source_payable": slot in hand and source_payable(battlefield, slot),
            "neheb_seen": "Neheb, the Eternal" in hand,
            "loyal_seen": "Loyal Subordinate" in hand,
            "assault_three_seen": all_seen,
            "assault_three_individually_payable": all_seen and all_payable,
            "commander_source_payable": source_payable(battlefield, "Abaddon the Despoiler"),
            "known_untapped_land_sources": sum(not tapped and bool(land_colors(n, any(x == "Urborg, Tomb of Yawgmoth" for x, _ in battlefield))) for n, tapped in battlefield),
        }
    return metrics, fetches


def run(samples=2000):
    plan, base = frozen_source()
    variants = libraries(base, plan)
    if set(variants) != {"baseline", "assault_for_rakdos", "assault_for_lost"}:
        raise ValueError("Variant roster drift")
    if samples <= 0:
        raise ValueError("Samples must be positive")
    checkpoints = plan["checkpoints"]
    results = {v: {t: Counter() for t in checkpoints} for v in variants}
    fetch_stats = Counter()
    for i in range(samples):
        sd = plan["seed"] + i * 104729
        for variant, lib in variants.items():
            metrics, fetch_count = trial(lib, sd, checkpoints)
            fetch_stats[variant] += fetch_count
            for t, rec in metrics.items():
                for name, value in rec.items():
                    if isinstance(value, bool):
                        results[variant][t][name] += int(value)
                    else:
                        results[variant][t][name + "_total"] += value
    return {
        "schema_version": 1,
        "test_class": "paired_100_card_draw_and_land_source_only_snapshots",
        "approved_sha256": plan["canonical_approved_raw_sha256"],
        "preregistration": str(PLAN.relative_to(ROOT)),
        "samples_per_variant": samples,
        "seed": plan["seed"],
        "checkpoints": checkpoints,
        "exact_draw_only_probabilities": {str(t): draw_only_probabilities(t) for t in checkpoints},
        "observations": {v: {str(t): dict(sorted(results[v][t].items()))
                             for t in checkpoints} for v in variants},
        "fetch_shuffles": dict(fetch_stats),
        "limits": {
            "has_real_spell_casts": False, "has_actual_combo_assembly": False,
            "models_nonland_mana_or_card_effects": False,
            "models_actual_opponent_decisions": False, "multiplayer_win_rate": None,
            "proves_swap_superiority": False, "full_phase_b_complete": False,
            "new_m6_certificates": 0, "approved_deck_changed": False,
        },
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--samples", type=int, default=2000)
    p.add_argument("--out", type=str, default=None)
    args = p.parse_args()
    data = run(args.samples)
    serialized = json.dumps(data, indent=2, sort_keys=True) + "\n"
    if args.out:
        Path(args.out).write_text(serialized, encoding="utf-8")
    for v in data["observations"]:
        rec = data["observations"][v]["10"]
        print(v, "T10 slot_drawn", rec.get("slot_seen", 0),
              "slot_source_payable", rec.get("slot_source_payable", 0),
              "three_drawn", rec.get("assault_three_seen", 0),
              "three_separately_payable", rec.get("assault_three_individually_payable", 0))
    print("NO spell casting, modeled opponents or win-rate evidence.")
if __name__ == "__main__":
    main()
