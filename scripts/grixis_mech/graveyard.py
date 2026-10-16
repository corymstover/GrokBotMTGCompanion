"""graveyard_recursion: zone tracking for 'return target ... card from your graveyard' effects."""
import re

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
    "parameters": {"turns": [4, 6, 8]},
    "confidence": "low", "limitations": ["v1.1 sends few cards to the graveyard (no creature deaths), so live rates are lower bounds."],
    "metrics": ["recursion_live_by_turn", "legal_targets_when_live"],
    "determinism": "seeded paired v1.1 games (grixis_sim.seed_for); no extra rng",
    "test_file": "tests/test_mech.py",
}
RX = re.compile(r"return (?:up to \w+ )?(?:target |another target |each |all )?([a-z ]{0,30}?)cards? from your graveyard to "
                r"(?:the battlefield|your hand)", re.I)
KINDS = ("creature", "artifact", "enchantment", "instant", "sorcery", "planeswalker", "land", "permanent")


def target_kind(text):
    m = RX.search(text)
    if not m:
        return None
    w = m.group(1).lower()
    return next((k for k in KINDS if k in w), "card")


def matches(name, text, type_line):
    return target_kind(text) is not None


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


def evaluate(base_games, chal_games, cut, add, cards, models):
    out = {"module": SPEC["id"], "evidence_class": "test_result", "metrics": {}}
    for T in SPEC["parameters"]["turns"]:
        row = {}
        for side, games, n in (("add", chal_games, add), ("cut", base_games, cut)):
            c = cards.get(n)
            k = target_kind(c["text"]) if c else None
            row[side] = None if k is None else dict(zip(("p_live", "targets_when_live"), [round(x, 4) for x in live(games, n, k, models, T)]))
        a = row["add"]["p_live"] if row["add"] else 0.0
        c = row["cut"]["p_live"] if row["cut"] else 0.0
        row["diff_p_live"] = round(a - c, 4)
        out["metrics"][str(T)] = row
    return out
