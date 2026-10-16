"""self_recursion: cards that return themselves from your graveyard (split from graveyard_recursion, Bot cycle 66.2)."""
from . import deaths, graveyard

SPEC = {
    "id": "self_recursion", "version": "1", "family": "graveyard recursion (self)", "evidence_class": "test_result",
    "models": ["P(the card is in your graveyard, so its self-return is available, by turn 4/6/8): from the v1.1 trace "
               "(spent spells) and, for creatures, from the shared death layer"],
    "does_not_model": ["the cost or timing of the self-return", "repeated loops (counted once)",
                       "graveyard hate", "multiplayer win rates (never produced)"],
    "assumptions": deaths.ASSUMPTIONS, "parameters": {"turns": [4, 6, 8], "death_grid": {k: [str(x) for x in v] for k, v in deaths.GRID.items()}},
    "confidence": "low", "limitations": ["Without the death layer a self-returning creature never reaches the graveyard (v1.1)."],
    "metrics": ["p_in_graveyard_by_turn", "p_in_graveyard_by_turn_death_grid"],
    "determinism": "seeded paired v1.1 games; closed-form death layer (no rng)", "test_file": "tests/test_mech.py",
}


def matches(name, text, type_line):
    return graveyard.is_self(name, text)


def p_gy(games, n, ctx, T, pt):
    tot = 0.0
    for _, tr in games:
        pr = deaths.profile(tr, ctx["creatures"], ctx["outlets"], ctx["commanders"], {n}, *pt)
        best = 0.0
        for s, row in zip(tr, pr):
            if s["turn"] > T:
                break
            best = max(best, 1.0 if n in s["graveyard"] else row["p_dead"].get(n, 0.0))
        tot += best
    return tot / max(1, len(games))


def evaluate(base_games, chal_games, cut, add, cards, ctx):
    out = {"module": SPEC["id"], "evidence_class": "test_result", "layer": "deaths", "metrics": {}}
    ia = add in cards and matches(add, cards[add]["text"], "")
    ic = cut in cards and matches(cut, cards[cut]["text"], "")
    for T in SPEC["parameters"]["turns"]:
        grid = {pt: round((p_gy(chal_games, add, ctx, T, pt) if ia else 0.0) - (p_gy(base_games, cut, ctx, T, pt) if ic else 0.0), 4)
                for pt in deaths.points()}
        out["metrics"][str(T)] = {"diff_lower_bound": grid[deaths.LOWER_BOUND], "diff_range": [min(grid.values()), max(grid.values())],
                                  "diff_mid": grid[(0.1, None, True)]}
    return out
