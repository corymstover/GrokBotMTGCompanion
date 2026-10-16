"""Read-only zone observer for grixis_sim.play_game (no edit to grixis_sim.py; no rng use)."""
import inspect
import random
import sys

import grixis_sim as gs

_SRC, _START = inspect.getsourcelines(gs.play_game)
_MARK = 'rec["lands"].append(lands_played)'
END_OF_TURN_LINE = _START + next(i for i, l in enumerate(_SRC) if _MARK in l)
_CODE = gs.play_game.__code__


def _snap(f):
    L = f.f_locals
    return {"turn": L["t"], "battlefield": [p["card"]["name"] for p in L["battlefield"]],
            "graveyard": [c["name"] for c in L["graveyard"]], "hand": [c["name"] for c in L["hand"]],
            "mana": L.get("avail"), "commander_cast": L["rec"]["commander_turn"]}


def play_traced(deck, rng, **kw):
    trace = []

    def local(frame, event, arg):
        if event == "line" and frame.f_lineno == END_OF_TURN_LINE:
            trace.append(_snap(frame))
        return local

    def glob(frame, event, arg):
        return local if frame.f_code is _CODE else None

    old = sys.gettrace()
    sys.settrace(glob)
    try:
        rec = gs.play_game(deck, rng, **kw)
    finally:
        sys.settrace(old)
    return rec, trace


def trace_games(deck, samples, seed, model="1.1", perms=None):
    """Same seeds as grixis_sim.run(); returns [(rec, trace)]."""
    out = []
    for i in range(samples):
        rng = random.Random(gs.seed_for(seed, i))
        out.append(play_traced(deck, rng, perm=perms[i] if perms else None, model=model))
    return out
