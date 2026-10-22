#!/usr/bin/env python3
"""Abaddon bounded chronological 100-card mana-spending and one Assault activation.

Rule subset only. This is NOT a full gameplay simulator, combo-win estimator,
opponent model or canonical deck modification. It extends the source-hash-locked
physical library and land policy from Cycle 2026-10-21 PR #512.
"""
from __future__ import annotations
import argparse
from collections import Counter
import json
import random
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from grixis_m6_abaddon_assault_access import (
    ROOT, SPELL_COST, frozen_source, libraries, land_colors, play_land,
)

PLAN = ROOT / "data/grixis/m6/phase_b_plans/abaddon_chronological_engine_20261021.json"
ZERO = (0, 0, 0, 0)  # U, B, R, C; no floating mana at a new phase
ENGINE = ("Abaddon the Despoiler", "Loyal Subordinate",
          "Neheb, the Eternal", "Aggravated Assault")


def _available_ability_choices(land, urborg):
    return land_colors(land, urborg)


def _life_cost(land, ability, urborg):
    if urborg and ability == ("B",):
        return 0  # Tapping a swamp for Urborg's black mana has no City/Tomb side effect
    if land == "Ancient Tomb":
        return 2 if ability == ("C", "C") else 0
    return int(land in ("City of Brass", "Mana Confluence"))


def _pay_from_pool(mana, printed):
    """Pay all colored pips then generic, preferring C, B, U, R for generic.

    Return remaining mana, or None. Only flat {n} plus U/B/R pips are supported.
    """
    mv, colored = printed
    u, b, r, c = mana
    needu, needb, needr = colored
    if u < needu or b < needb or r < needr:
        return None
    generic = mv - needu - needb - needr
    if generic < 0:
        raise ValueError("Malformed printed-cost fixture")
    result = [u - needu, b - needb, r - needr, c]
    # Actual all-colored generic payment is permitted; this is one fixed policy.
    for idx in (3, 1, 0, 2):
        use = min(generic, result[idx])
        result[idx] -= use
        generic -= use
    return tuple(result) if generic == 0 else None


def physical_payment(lands, pool, spell, *, source_cost_override=None):
    """Return (source indices, remaining pool), or None.

    Each land is tapped at most once; preserve surplus Ancient Tomb mana within
    the same main phase. Exhaustively discover bounded land-ability choices and
    choose a fixed least-tap, then least-life-loss policy. The land-life-cost
    ranking is NOT tracked as player life; no effects beyond these taps modeled.
    """
    printed = source_cost_override or SPELL_COST[spell]
    if len(pool) != 4 or any(not isinstance(n, int) or n < 0 for n in pool):
        raise ValueError("Mana pool must be four nonnegative integer components")
    urborg = any(n == "Urborg, Tomb of Yawgmoth" for n, _ in lands)
    states = {tuple(pool): (0, ())}  # mana tuple -> (life payment ranking, land indices)
    for idx, (land, tapped) in enumerate(lands):
        if tapped:
            continue
        choices = _available_ability_choices(land, urborg)
        updated = dict(states)  # skipping a source is a legal choice
        for mana, (life, used) in states.items():
            for ability in choices:
                add = (ability.count("U"), ability.count("B"),
                       ability.count("R"), ability.count("C"))
                result = tuple(mana[j] + add[j] for j in range(4))
                contender = (life + _life_cost(land, ability, urborg),
                             used + (idx,))
                previous = updated.get(result)
                if previous is None or (len(contender[1]), contender[0], contender[1]) < (
                        len(previous[1]), previous[0], previous[1]):
                    updated[result] = contender
        states = updated
    options = []
    for mana, (life, used) in states.items():
        remaining = _pay_from_pool(mana, printed)
        if remaining is not None:
            options.append(((len(used), life, used, remaining), used, remaining))
    if not options:
        return None
    _, taps, remainder = min(options, key=lambda item: item[0])
    return taps, remainder


def pay_and_tap(lands, pool, spell, *, source_cost_override=None):
    plan = physical_payment(lands, pool, spell, source_cost_override=source_cost_override)
    if plan is None:
        return None
    taps, new_pool = plan
    for i in taps:
        if lands[i][1]:
            raise AssertionError("Double-spent physical land")
        lands[i] = (lands[i][0], True)
    return new_pool


def postcombat_window(permanents, *, commander_removed_before_combat=False):
    """Single normal combat only, with no attacks or other opponent loss.

    No Loyal loss unless its lieutenant clause and Abaddon both hold at the
    beginning of combat and on resolution. Neheb red enters after combat.
    The first Assault activation pays {3}{R}{R} (five red) in postcombat main.
    Future extra combats are outside this fixture; PR #504 already tested that
    separately under preassembled unopposed battlefield assumptions.
    """
    s = set(permanents)
    active_commander = "Abaddon the Despoiler" in s and not commander_removed_before_combat
    loss = 9 if active_commander and "Loyal Subordinate" in s else 0
    red = loss if "Neheb, the Eternal" in s else 0
    can_assault = "Aggravated Assault" in s and red >= 5
    return {"opponents_lost": loss, "neheb_red": red,
            "assault_first_postcombat_activation": bool(can_assault),
            "assault_red_spent": 5 if can_assault else 0,
            "extra_combat_win_proved": False}


def one_physical_trial(library, seed, *, horizon=10):
    """One fixed pilot policy: draw, land, commander, Loyal, Neheb, Assault.

    Only these named spells are cast. Rakdos may be cast after normal combat if
    a Loyal/Abaddon drain made it legal; all his discounts and the Lost Spawn
    engine are deliberately UNKNOWN and unmodeled, so do not score against them.
    """
    if len(library) != 99 or horizon < 1:
        raise ValueError("Library must be 99 cards and turn horizon positive")
    deck = list(library)
    random.Random(seed).shuffle(deck)
    hand, deck = deck[:7], deck[7:]
    lands = []
    battlefield = set()
    paid_turns = {}
    first_activation_turn = None
    first_all_board_turn = None
    fetches = 0
    rakdos_blocked_by_loss = 0
    for turn in range(1, horizon + 1):
        lands = [(n, False) for n, _ in lands]
        mana = ZERO
        hand.append(deck.pop(0))
        count, _ = play_land(hand, deck, lands, seed, turn)
        fetches += count
        for name in ENGINE:
            if name == "Aggravated Assault" and name not in library:
                continue
            if name in battlefield:
                continue
            if name != "Abaddon the Despoiler" and name not in hand:
                continue
            remaining = pay_and_tap(lands, mana, name)
            if remaining is None:
                continue
            mana = remaining
            battlefield.add(name)
            paid_turns[name] = turn
            if name != "Abaddon the Despoiler":
                hand.remove(name)
        # All floating mana empties on leaving precombat main.
        result = postcombat_window(battlefield)
        if all(x in battlefield for x in ENGINE) and first_all_board_turn is None:
            first_all_board_turn = turn
        if result["assault_first_postcombat_activation"] and first_activation_turn is None:
            first_activation_turn = turn
        if "Rakdos, Lord of Riots" in hand and "Rakdos, Lord of Riots" not in battlefield:
            if result["opponents_lost"] == 0:
                rakdos_blocked_by_loss += 1
            else:
                # A postcombat Neheb trigger may contribute red, which is
                # allowed to pay a Rakdos red pip. Never use precombat mana.
                mana = (0, 0, result["neheb_red"], 0)
                rem = pay_and_tap(lands, mana, "Rakdos, Lord of Riots")
                if rem is not None:
                    battlefield.add("Rakdos, Lord of Riots")
                    hand.remove("Rakdos, Lord of Riots")
                    paid_turns["Rakdos, Lord of Riots"] = turn
    if not all(name != "Aggravated Assault" or first_activation_turn is not None
               for name in battlefield if name in ENGINE):
        # Not every cast Assault will have a payable Neheb/Loyal line; no
        # assertion about activation on its own.
        pass
    return {
        "cast_turns": paid_turns,
        "engine_all_on_battlefield_turn": first_all_board_turn,
        "first_payable_postcombat_assault_activation_turn": first_activation_turn,
        "rakdos_cast_blocked_for_no_opponent_loss_turns": rakdos_blocked_by_loss,
        "physical_fetch_searches": fetches,
        "all_cards_from_physical_library": True,
        "actual_modeled_land_payments": True,
        "actual_multiplayer_game_win": None,
    }


def verify_and_run():
    p = json.loads(PLAN.read_text(encoding="utf-8"))
    prior, cards = frozen_source()
    if (p["canonical_raw_sha256"] != prior["canonical_approved_raw_sha256"]
            or p["source_sha256"] != prior["source_sha256"]
            or p["samples_per_variant"] != prior["samples_per_variant"]
            or p["seed"] != prior["seed"]
            or [v["id"] for v in prior["variants"]] != p["variants"]):
        raise ValueError("Preregistered and predecessor authorities disagree")
    candidates = libraries(cards, prior)
    reports = {}
    for variant, lib in candidates.items():
        measures = Counter()
        examples = []
        for i in range(p["samples_per_variant"]):
            seed = p["seed"] + i * 104729
            row = one_physical_trial(lib, seed, horizon=p["turns"])
            for target in ("Abaddon the Despoiler", "Loyal Subordinate",
                           "Neheb, the Eternal", "Aggravated Assault",
                           "Rakdos, Lord of Riots"):
                measures["cast_" + target] += int(target in row["cast_turns"])
            measures["four_piece_battlefield"] += int(
                row["engine_all_on_battlefield_turn"] is not None)
            measures["first_assault_activation_paid"] += int(
                row["first_payable_postcombat_assault_activation_turn"] is not None)
            measures["rakdos_no_loss_blocked_turns"] += row[
                "rakdos_cast_blocked_for_no_opponent_loss_turns"]
            measures["physical_fetch_searches"] += row["physical_fetch_searches"]
            if row["first_payable_postcombat_assault_activation_turn"] is not None:
                if len(examples) < 5:
                    examples.append({"seed": seed, **row})
        reports[variant] = {"n": p["samples_per_variant"],
                            "observed": dict(sorted(measures.items())),
                            "bounded_activation_examples": examples}
    return {"schema_version": 1, "test_class":
            "closed_deterministic_chronological_named_spell_casts_paid_from_actual_modeled_lands",
            "preregistration": str(PLAN.relative_to(ROOT)),
            "canonical_raw_sha256": p["canonical_raw_sha256"],
            "variants": reports, "policy": p["policy"],
            "authority": p["authorities"], "true_multiplayer_win_rate": None,
            "full_game_effect_coverage": False, "sufficient_to_recommend_a_swap": False,
            "m6_6_complete": False, "m6_certificates_issued": 0,
            "m7_approved_decks": 0, "canonical_deck_changed": False}


def main():
    arg = argparse.ArgumentParser()
    arg.add_argument("--out")
    args = arg.parse_args()
    d = verify_and_run()
    if args.out:
        Path(args.out).write_text(json.dumps(d, indent=2, sort_keys=True) + "\n",
                                  encoding="utf-8")
    for name, data in d["variants"].items():
        print(name, json.dumps(data["observed"], sort_keys=True))
    print("NOT a deck-strength comparison or measured win rate.")
if __name__ == "__main__":
    main()
