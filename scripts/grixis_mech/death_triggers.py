"""death_triggers: 'when ~ dies' (self) and 'whenever a/another creature dies' (watcher) triggers under the death layer."""
import re
from . import deaths

SPEC = {
    "id": "death_triggers", "version": "1", "family": "death triggers", "evidence_class": "test_result",
    "models": ["self death triggers: P(the card has died by turn 6/8/10)",
               "watcher death triggers: expected creature deaths (yours) while the watcher is on the battlefield, by turn 6/8/10",
               "every metric over the shared death-perturbation grid (deaths.GRID), with the no-death lower bound reported separately"],
    "does_not_model": ["trigger payloads (value of the trigger)", "opponents' creatures dying (watchers that count all "
                       "creatures are under-counted)", "real removal choices, combat deaths, politics",
                       "multiplayer win rates (never produced)"],
    "assumptions": deaths.ASSUMPTIONS, "parameters": {"grid": {k: [str(x) for x in v] for k, v in deaths.GRID.items()}, "turns": [6, 8, 10]},
    "confidence": "low", "limitations": ["The death layer is a scripted proxy; results are a sensitivity range, not an estimate of real games.",
                                         "Opponents' creature deaths are not modelled."],
    "metrics": ["self_p_dead_by_turn", "watcher_expected_triggers_by_turn"],
    "determinism": "seeded paired v1.1 games (grixis_sim.seed_for); the death layer is closed-form (no rng)",
    "test_file": "tests/test_mech.py",
}
SELF = re.compile(r"when(?:ever)? ~ dies", re.I)
WATCH = re.compile(r"whenever (?:a|another|one or more)(?: nontoken)? (?:creature|[a-z]+ creatures?)(?: you control)? (?:dies|die)", re.I)


def kind(name, text):
    t = text.replace(name, "~")
    return "watcher" if WATCH.search(t) else "self" if SELF.search(t) else None


def matches(name, text, type_line):
    return kind(name, text) is not None


def side(games, n, k, ctx, T, pt):
    tot = 0.0
    for _, tr in games:
        pr = deaths.profile(tr, ctx["creatures"], ctx["outlets"], ctx["commanders"], {n}, *pt)
        row = next((x for x in pr if x["turn"] == T), pr[-1])
        if k == "self":
            tot += row["p_dead"].get(n, 0.0)
        else:
            on = {s["turn"] for s in tr if n in s["battlefield"]}
            tot += sum(x["step"] for x in pr if x["turn"] <= T and x["turn"] in on)
    return tot / max(1, len(games))


def evaluate(base_games, chal_games, cut, add, cards, ctx):
    out = {"module": SPEC["id"], "evidence_class": "test_result", "metrics": {}}
    ka = kind(add, cards[add]["text"]) if add in cards else None
    kc = kind(cut, cards[cut]["text"]) if cut in cards else None
    for T in SPEC["parameters"]["turns"]:
        grid = {}
        for pt in deaths.points():
            a = side(chal_games, add, ka, ctx, T, pt) if ka else 0.0
            c = side(base_games, cut, kc, ctx, T, pt) if kc else 0.0
            grid[pt] = round(a - c, 4)
        out["metrics"][str(T)] = {"add_kind": ka, "cut_kind": kc, "diff_lower_bound": grid[deaths.LOWER_BOUND],
                                  "diff_range": [min(grid.values()), max(grid.values())],
                                  "diff_mid": grid[(0.1, None, True)]}
    return out
