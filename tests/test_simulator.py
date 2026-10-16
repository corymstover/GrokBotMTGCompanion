"""Bot cycle 57.2 (M3): goldfish simulator core vs exact math (hypergeometric layer, London mulligan, payment, seeds)."""
import itertools
import math
import random
from math import comb

from _helpers import skip  # noqa: F401  (sets sys.path)

import grixis_sim as gs


def land(name="Swamp", cols="B", tapped=False):
    return {"name": name, "mv": 0, "cost": gs.parse_cost(""), "land": True, "flex_land": False, "permanent": True,
            "creature": False, "source": (frozenset(cols), 1), "tapped": tapped}


def spell(name, cost, permanent=True, source=None, creature=False):
    c = gs.parse_cost(cost)
    return {"name": name, "mv": c["generic"] + len(c["pips"]), "cost": c, "land": False, "flex_land": False, "permanent": permanent,
            "creature": creature, "source": source, "tapped": False}


def synth(n_lands=38, N=99, commander_cost="{2}{B}{B}", key=("Key A",)):
    lib = [land(f"Swamp") for _ in range(n_lands)]
    lib += [spell(k, "{3}") for k in key]
    lib += [spell(f"Filler {i}", "{2}") for i in range(N - len(lib))]
    cmd = spell("Commander", commander_cost)
    d = gs.Deck("synthetic", [cmd], lib, {"keys": set(key)}, [])
    d.ci = {"B"}
    return d


def test_hypergeometric_pmf_sums_to_one_and_matches_comb():
    assert abs(sum(gs.hyper_pmf(99, 36, 7, k) for k in range(8)) - 1) < 1e-12
    assert abs(gs.hyper_pmf(99, 36, 7, 3) - comb(36, 3) * comb(63, 4) / comb(99, 7)) < 1e-15
    assert abs(gs.hyper_atleast(99, 1, 10, 1) - 10 / 99) < 1e-12


def test_land_drop_dp_matches_brute_force_on_a_tiny_deck():
    # 8-card deck, 3 lands, hand 2, 3 turns: enumerate every ordering
    N, L, hand, T = 8, 3, 2, 3
    deck = [1] * L + [0] * (N - L)
    tot = ok = 0
    for perm in set(itertools.permutations(deck)):
        tot += 1
        ok += all(sum(perm[:hand + t]) >= t for t in range(1, T + 1))
    assert abs(gs.p_land_drops(N, L, T, hand=hand) - ok / tot) < 1e-12


def test_seen_by_turn_counts_the_multiplayer_turn_one_draw():
    assert gs.cards_seen(1) == 8 and gs.cards_seen(1, skip_first_draw=True) == 7  # CR 103.8c / 103.8a
    assert abs(gs.p_seen_by_turn(99, 1, 3) - 10 / 99) < 1e-12


def test_parse_cost():
    c = gs.parse_cost("{2}{U}{B/R}{B/P}{X}")
    assert c["generic"] == 2 and c["life"] == 1 and frozenset("U") in c["pips"] and frozenset("BR") in c["pips"]


def test_can_pay_matches_colours():
    B, U, C, UB = frozenset("B"), frozenset("U"), frozenset("C"), frozenset("UB")
    assert gs.can_pay(gs.parse_cost("{1}{U}{B}"), [UB, B, C]) is not None
    assert gs.can_pay(gs.parse_cost("{U}{U}"), [UB, B]) is None
    assert gs.can_pay(gs.parse_cost("{B}{B}"), [UB, B]) is not None
    assert gs.can_pay(gs.parse_cost("{2}"), [C], tax=0) is None
    assert gs.can_pay(gs.parse_cost("{B}"), [B, B, B], tax=2) is not None  # commander tax as generic


def test_london_bottoming():
    hand = [land() for _ in range(6)] + [spell("Big", "{7}")]
    h, out = gs.bottom(hand, 2)
    assert len(h) == 5 and all(c["land"] for c in out)  # lands beyond 4 first
    hand = [land() for _ in range(3)] + [spell("Big", "{7}"), spell("Mid", "{4}"), spell("Low", "{1}"), spell("Two", "{2}")]
    h, out = gs.bottom(hand, 2)
    assert [c["name"] for c in out] == ["Big", "Mid"]


def test_free_first_mulligan_in_multiplayer():
    d = synth(n_lands=0, N=99)  # never keepable: every game mulligans to 5 cards
    r = gs.play_game(d, random.Random(1), turns=1, multiplayer=True)
    assert r["kept"] == 5 and r["mulligans"] == 3   # 7 (free), 6, 5
    r = gs.play_game(d, random.Random(1), turns=1, multiplayer=False)
    assert r["kept"] == 5 and r["mulligans"] == 2


def test_same_seed_same_game():
    d = synth()
    a = gs.run(d, 50, seed=9)
    b = gs.run(d, 50, seed=9)
    c = gs.run(d, 50, seed=10)
    strip = lambda rs: [{k: v for k, v in r.items()} for r in rs]
    assert strip(a) == strip(b) and strip(a) != strip(c)


def test_monte_carlo_matches_exact_math():
    d = synth()
    n = 3000
    recs = gs.run(d, n, seed=3, turns=5, mulligan=False)
    checks = [(sum(1 for r in recs if r["lands"][3] >= 4) / n, gs.p_land_drops(99, 38, 4)),
              (sum(1 for r in recs if r["key_turn"]["keys"] is not None and r["key_turn"]["keys"] <= 5) / n, gs.p_seen_by_turn(99, 1, 5))]
    for mc, ex in checks:
        assert abs(mc - ex) <= 4 * math.sqrt(ex * (1 - ex) / n), (mc, ex)


def test_commander_turn_on_a_mono_land_deck():
    # 99 Swamps, a {2}{B}{B} commander: cast on turn 4 in every game (land drop each turn, no other spells)
    d = synth(n_lands=98, N=99, key=("Key A",))
    recs = gs.run(d, 20, seed=1, turns=6)
    assert {r["commander_turn"] for r in recs} == {4}


def test_tapped_land_delays_mana():
    lib = [land("Tapland", "B", tapped=True) for _ in range(99)]
    d = gs.Deck("t", [spell("Commander", "{B}")], lib, {}, [])
    r = gs.play_game(d, random.Random(1), turns=2)
    assert r["mana"][0] == 0 and r["commander_turn"] == 2


def test_wilson_interval():
    p, (lo, hi) = gs.wilson(50, 100)
    assert p == 0.5 and 0.40 < lo < 0.41 and 0.59 < hi < 0.60
