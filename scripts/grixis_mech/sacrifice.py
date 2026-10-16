"""sacrifice_costs: sacrifice outlets (cost 'Sacrifice a creature: ...') and how often they have fodder."""
from . import deaths

SPEC = {
    "id": "sacrifice_costs", "version": "1", "family": "sacrifice costs", "evidence_class": "test_result",
    "models": ["turns a sacrifice outlet is on the battlefield with at least one other creature (fodder) alive, by turn 6/8/10",
               "expected creatures sacrificed through it (one per turn when fodder exists), over the death-perturbation grid"],
    "does_not_model": ["the outlet's payoff (mana, scry, damage)", "sacrifice as a combo step (Spellbook layer handles combos)",
                       "token fodder from cards v1.1 does not model", "multiplayer win rates (never produced)"],
    "assumptions": deaths.ASSUMPTIONS + ["only creature fodder seen on the battlefield in the v1.1 trace counts"],
    "parameters": {"grid": {k: [str(x) for x in v] for k, v in deaths.GRID.items()}, "turns": [6, 8, 10]},
    "confidence": "low", "limitations": ["Fodder is under-counted: v1.1 does not create most tokens."],
    "metrics": ["outlet_uses_by_turn"],
    "determinism": "seeded paired v1.1 games; closed-form death layer (no rng)", "test_file": "tests/test_mech.py",
}


def matches(name, text, type_line):
    return deaths.is_outlet(text)


def uses(games, n, ctx, T, pt):
    """Expected sacrifices through outlet n by turn T: per turn on the battlefield, min(1, expected live fodder) x P(outlet alive)."""
    tot = 0.0
    for _, tr in games:
        pr = deaths.profile(tr, ctx["creatures"], set(), ctx["commanders"], set(), pt[0], pt[1], False)
        prev = {}
        for s, row in zip(tr, pr):
            if s["turn"] > T:
                break
            if n in s["battlefield"]:
                fod = sum(a for m, a in prev.items() if m != n and m not in ctx["commanders"])
                tot += min(1.0, fod) * prev.get(n, 1.0)
            prev = row["alive"]
    return tot / max(1, len(games))


def evaluate(base_games, chal_games, cut, add, cards, ctx):
    out = {"module": SPEC["id"], "evidence_class": "test_result", "metrics": {}}
    ia, ic = add in cards and matches(add, cards[add]["text"], ""), cut in cards and matches(cut, cards[cut]["text"], "")
    for T in SPEC["parameters"]["turns"]:
        grid = {}
        for pt in deaths.points():
            if pt[2]:
                continue  # the outlet itself is the sacrifice use; the sac axis does not apply
            grid[pt] = round((uses(chal_games, add, ctx, T, pt) if ia else 0.0) - (uses(base_games, cut, ctx, T, pt) if ic else 0.0), 4)
        out["metrics"][str(T)] = {"diff_lower_bound": grid[deaths.LOWER_BOUND], "diff_range": [min(grid.values()), max(grid.values())]}
    return out
