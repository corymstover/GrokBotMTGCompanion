"""Bot cycle 57.4 (M3): scripted stress scenarios (deterministic perturbations, exact expectations, no win rates)."""
import random

from _helpers import ga

import grixis_sim as gs
import grixis_stress as st
from test_simulator import land, spell


def mono(cmd="{B}{B}", extra=()):
    lib = [spell(n, c, **kw) for n, c, kw in extra]
    lib += [land() for _ in range(99 - len(lib))]
    d = gs.Deck("t", [spell("Commander", cmd, creature=True)], lib, {}, [])
    d.ci = {"B"}
    return d


def g(d, kind=None, seed=1):
    return gs.play_game(d, random.Random(seed), 10, scenario={"kind": kind} if kind else None)


def test_none_scenario_matches_the_unperturbed_game():
    d = mono()
    a, b = g(d), g(d, "none")
    for k in a:
        assert a[k] == b[k], k


def test_commander_removed_once_exact():
    # all lands: commander {B}{B} cast turn 2; removed at end of turn 4; recast turn 5 ({2}{B}{B}, 5 lands)
    r = g(mono(), "commander_removed_once")
    assert r["removals"] == [4] and r["recasts"] == [5]
    assert r["cmd_bf"] == [False, True, True, False] + [True] * 6
    assert sum(g(mono(), "none")["cmd_bf"]) - sum(r["cmd_bf"]) == 1


def test_commander_removed_twice_pays_more_tax():
    r = g(mono(), "commander_removed_twice")
    assert r["removals"] == [4, 5] and r["recasts"] == [5, 6]  # 2nd recast {4}{B}{B} needs 6 lands


def test_mana_screw_skips_two_land_drops():
    r = g(mono(), "mana_screw")
    assert r["lands"][:6] == [1, 2, 2, 2, 3, 4]


def test_artifact_wipe_removes_rocks():
    d = mono(cmd="{9}", extra=[("Rock", "{1}", {"source": (frozenset("C"), 2)})] * 1)
    for c in d.library:
        c["artifact"] = c["name"] == "Rock"
    base = [g(d, "none", s)["mana"][7] for s in range(40)]
    wiped = [g(d, "artifacts_wiped", s)["mana"][7] for s in range(40)]
    assert sum(wiped) < sum(base) and all(w <= b for w, b in zip(wiped, base))


def test_first_key_spell_is_countered_not_the_commander():
    d = mono(extra=[("Key", "{1}", {})] * 30)
    d.key_sets = {"pkg:k": {"Key", "Commander"}}
    r = gs.play_game(d, random.Random(3), 10, scenario={"kind": "first_key_spell_countered"})
    assert r["event_turn"] is not None and r["commander_turn"] == g(d, "none", 3)["commander_turn"]


def test_color_screw_delays_a_coloured_commander():
    d = mono(cmd="{B}{B}")
    r = g(d, "color_screw")
    assert r["commander_turn"] == 5  # black produces only {C} before turn 5


def test_stress_verdict_rule():
    def res(diff, lo, hi):
        return [{"metric": "m", "baseline": 0, "challenger": 0, "diff": diff, "ci95": [lo, hi], "method": ""}]
    assert st.verdict(res(0, -0.1, 0.1), "m", 1) == "no_detectable_difference"
    assert st.verdict(res(-0.3, -0.5, -0.1), "m", 1) == "pass"
    assert st.verdict(res(-2, -2.5, -1.5), "m", 1) == "fail"
    assert st.verdict(res(-0.9, -1.5, -0.3), "m", 1) == "inconclusive"  # straddles -threshold
    assert st.verdict(res(0.5, 0.2, 0.8), "m", 1) == "inconclusive"  # a detectable gain


def test_every_scenario_is_preregistered_and_records_validate():
    assert set(st.STRESS_PREREG) == set(gs.SCENARIOS) - {"none"}
    f = sorted(st.OUT.glob("*.json"))
    if f:
        import json
        for r in json.loads(f[0].read_text(encoding="utf-8"))["records"]:
            assert not ga.validate_file(r, "test.schema.json")
            assert r["kind"] == "stress_scenario" and r["challenger_hash"] is None
            assert not any("win_rate" in x["metric"] for x in r["results"])
