"""Bot cycle 57.3 (M3): paired-seed champion-vs-challenger tests (alignment, identical shuffles, CI, verdict rule, record)."""
import random

from _helpers import ga

import grixis_paired as gp
import grixis_sim as gs
from test_simulator import land, spell


def deck(lands=36, extra=()):
    lib = [land() for _ in range(lands)] + [spell(n, c) for n, c in extra]
    lib += [spell(f"Filler {i}", "{2}") for i in range(99 - len(lib))]
    d = gs.Deck("synthetic", [spell("Commander", "{2}{B}{B}")], lib, {"pkg:x": {"Filler 0", "Filler 1"}}, [])
    d.ci = {"B"}
    return d


def test_identical_lists_give_zero_difference_every_game():
    a = deck()
    res, swaps = gp.paired(a, deck(), 200, seed=5)
    assert swaps == []
    assert all(r["diff"] == 0 and r["ci95"] == [0, 0] for r in res)
    assert gp.verdict(res) == "no_detectable_difference"


def test_alignment_puts_swaps_in_the_same_position():
    a = deck(extra=[("Cut A", "{1}"), ("Cut B", "{5}")])
    b = deck(extra=[("Add A", "{1}"), ("Add B", "{5}")])
    a2, b2, sw = gp.align(a, b, pairs=[("Cut B", "Add A"), ("Cut A", "Add B")])
    assert sw == [("Cut B", "Add A"), ("Cut A", "Add B")]
    for x, y in zip(a2.library, b2.library):
        assert x["name"] == y["name"] or (x["name"], y["name"]) in sw


def test_cutting_lands_is_detected_as_worse():
    a = deck(lands=36)
    b = deck(lands=30, extra=[(f"Spell {i}", "{2}") for i in range(6)])
    res, _ = gp.paired(a, b, 600, seed=2)
    m = {r["metric"]: r for r in res}
    assert m["mana_available_t4"]["diff"] < 0 and m["mana_available_t4"]["ci95"][1] < 0


def test_pairing_shrinks_the_interval():
    a = deck(lands=36)
    b = deck(lands=35, extra=[("Spell", "{2}")])
    res, _ = gp.paired(a, b, 600, seed=4)
    paired_w = next(r for r in res if r["metric"] == "mana_spent_t1_t6")
    lo, hi = paired_w["ci95"]
    # unpaired: independent shuffles for the challenger
    ra = gs.run(a, 600, seed=4)
    rb = gs.run(b, 600, seed=99)
    xa = [sum(r["spent"][:6]) for r in ra]
    xb = [sum(r["spent"][:6]) for r in rb]
    sd = lambda x: (sum((v - sum(x) / len(x)) ** 2 for v in x) / (len(x) - 1)) ** 0.5
    unpaired_half = 1.96 * ((sd(xa) ** 2 + sd(xb) ** 2) / 600) ** 0.5
    assert (hi - lo) / 2 < unpaired_half


def test_verdict_rule():
    def r(diff, lo, hi):
        return [{"metric": gp.PREREG["primary"]["metric"], "baseline": 0, "challenger": 0, "diff": diff, "ci95": [lo, hi], "method": ""}]
    t = gp.PREREG["primary"]["threshold"]
    assert gp.verdict(r(t + 0.1, 0.05, 1)) == "pass"
    assert gp.verdict(r(-t - 0.1, -1, -0.05)) == "fail"
    assert gp.verdict(r(0.01, -0.02, 0.04)) == "no_detectable_difference"
    assert gp.verdict(r(t / 2, 0.01, t)) == "inconclusive"


def test_record_validates_against_test_schema():
    a = deck()
    b = deck(lands=35, extra=[("Spell", "{2}")])
    res, sw = gp.paired(a, b, 50, seed=1)
    ch = {"id": "chal:x:1", "label": "test", "hash": "lh1:" + "1" * 64}
    rec = gp.record("abaddon-the-despoiler", "Abaddon_the_Despoiler", "lh1:" + "0" * 64, ch, 50, 1, res, sw)
    assert not ga.validate_file(rec, "test.schema.json")
    assert rec["limitations"] and rec["preregistered"]["registered"].startswith("2026-10-16")
    assert all(not r["metric"].startswith("win_rate") for r in rec["results"])  # no win-rate simulation
