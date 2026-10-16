"""graveyard_recursion: zone tracking for 'return target ... card from your graveyard' effects."""
import re

from . import deaths

SPEC = {
    "id": "graveyard_recursion", "version": "1", "family": "graveyard recursion", "evidence_class": "test_result",
    "models": ["graveyard contents by turn from the v1.1 zone trace (cards the model already puts there: spent spells, "
               "sacrificed/used one-shots, scenario events)",
               "turn a recursion card is available (on battlefield or in hand) while your graveyard holds a legal target "
               "of the type it names",
               "P(recursion live by turn 4/6/8) and mean legal targets when live"],
    "does_not_model": ["self-mill, discard outlets, opponents' removal filling the graveyard (the v1.1 graveyard is "
                       "thin, so this under-counts)", "the value of the returned card", "graveyard hate from opponents "
                       "(see stress scenario graveyard_exiled)", "multiplayer win rates (never produced)"],
    "assumptions": ["a target is legal if its card model has the type the recursion text names (creature/artifact/"
                    "instant/sorcery/permanent/any card)", "no opponent interaction with the graveyard"],
    "parameters": {"turns": [4, 6, 8], "death_grid": {k: [str(x) for x in v] for k, v in deaths.GRID.items()}},
    "confidence": "low", "limitations": ["v1.1 sends few cards to the graveyard (no creature deaths), so live rates are lower bounds."],
    "metrics": ["recursion_live_by_turn", "legal_targets_when_live", "recursion_live_by_turn_death_grid"],
    "determinism": "seeded paired v1.1 games (grixis_sim.seed_for); no extra rng",
    "test_file": "tests/test_mech.py",
}
RX = re.compile(r"return (?:up to \w+ )?(?:target |another target |each |all )?([a-z ]{0,30}?)cards? from your graveyard to "
                r"(?:the battlefield|your hand)", re.I)
KINDS = ("creature", "artifact", "enchantment", "instant", "sorcery", "planeswalker", "land", "permanent")


SELF_RX = re.compile(r"return ~ from your graveyard|return this card from your graveyard|~ from your graveyard to (?:the battlefield|your hand)", re.I)


def is_self(name, text):
    return bool(SELF_RX.search(text.replace(name, "~")))


def target_kind(text, name=None):
    if name and is_self(name, text) and not RX.search(SELF_RX.sub("", text.replace(name, "~"))):
        return None  # self-recursion only: routed to self_recursion (Bot cycle 66.2 split)
    m = RX.search(SELF_RX.sub("", text.replace(name, "~")) if name else text)
    if not m:
        return None
    w = m.group(1).lower()
    return next((k for k in KINDS if k in w), "card")


def matches(name, text, type_line):
    return target_kind(text, name) is not None


def legal(kind, model):
    if model is None:
        return False
    if kind == "card":
        return True
    if kind == "permanent":
        return model.get("permanent", False)
    return kind in model.get("types", [])


def live(games, name, kind, models, T):
    hits, tg = 0, []
    for _, tr in games:
        for s in tr:
            if s["turn"] > T:
                break
            if name in s["battlefield"] or name in s["hand"]:
                n = sum(1 for g in s["graveyard"] if g != name and legal(kind, models.get(g)))
                if n:
                    hits += 1
                    tg.append(n)
                    break
    return hits / max(1, len(games)), (sum(tg) / len(tg) if tg else 0.0)


def live_under(games, name, kind, models, ctx, T, pt):
    """P(recursion live by T) when dead creatures also fill the graveyard (shared death layer)."""
    tot = 0.0
    for _, tr in games:
        pr = deaths.profile(tr, ctx["creatures"], ctx["outlets"], ctx["commanders"], set(), *pt)
        best = 0.0
        for s, row in zip(tr, pr):
            if s["turn"] > T:
                break
            if name in s["battlefield"] or name in s["hand"]:
                if any(g != name and legal(kind, models.get(g)) for g in s["graveyard"]):
                    best = 1.0
                    break
                miss = 1.0
                for m, a in row["alive"].items():
                    if m != name and m not in ctx["commanders"] and legal(kind, models.get(m)):
                        miss *= a
                best = max(best, 1.0 - miss)
        tot += best
    return tot / max(1, len(games))


def evaluate_grid(base_games, chal_games, cut, add, cards, models, ctx):
    out = {"module": SPEC["id"], "evidence_class": "test_result", "layer": "deaths", "metrics": {}}
    for T in SPEC["parameters"]["turns"]:
        grid = {}
        for pt in deaths.points():
            v = []
            for games, n in ((chal_games, add), (base_games, cut)):
                c = cards.get(n)
                k = target_kind(c["text"], n) if c else None
                v.append(live_under(games, n, k, models, ctx, T, pt) if k else 0.0)
            grid[pt] = round(v[0] - v[1], 4)
        out["metrics"][str(T)] = {"diff_lower_bound": grid[deaths.LOWER_BOUND], "diff_range": [min(grid.values()), max(grid.values())],
                                  "diff_mid": grid[(0.1, None, True)]}
    return out


def evaluate(base_games, chal_games, cut, add, cards, models):
    out = {"module": SPEC["id"], "evidence_class": "test_result", "metrics": {}}
    for T in SPEC["parameters"]["turns"]:
        row = {}
        for side, games, n in (("add", chal_games, add), ("cut", base_games, cut)):
            c = cards.get(n)
            k = target_kind(c["text"], n) if c else None
            row[side] = None if k is None else dict(zip(("p_live", "targets_when_live"), [round(x, 4) for x in live(games, n, k, models, T)]))
        a = row["add"]["p_live"] if row["add"] else 0.0
        c = row["cut"]["p_live"] if row["cut"] else 0.0
        row["diff_p_live"] = round(a - c, 4)
        out["metrics"][str(T)] = row
    return out
