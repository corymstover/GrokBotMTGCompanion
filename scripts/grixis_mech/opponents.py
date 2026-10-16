"""Step E opponent-facing bounded proxies (ChatGPT cycle 66.9).

`opponent_dependent_draw` intentionally does not simulate opponents. It recognizes a narrow set of Oracle wordings and
reports a deterministic sensitivity grid over declared opponent spell/draw activity and tax nonpayment. The output is
`test_result` evidence only; no point in the grid is claimed to be a real multiplayer rate.
"""
import re

from . import semantics

TURNS = [4, 6, 8, 10]
OPPONENTS = 3
SPELLS_PER_OPPONENT_TURN = (1.0, 2.0, 3.0)
NONCREATURE_SHARE = (0.5, 0.7, 0.9)
NONPAY_SHARE = (0.25, 0.5, 0.75)
CARDS_DRAWN_PER_OPPONENT_TURN = (1.0, 2.0, 3.0)

DRAW_NUM = {"a": 1, "an": 1, "one": 1, "two": 2, "three": 3}
CAST_RX = re.compile(
    r"whenever an opponent casts (?:(?:a|an) )?(?P<qual>noncreature |creature |artifact |enchantment |instant |sorcery )?spell\b",
    re.I,
)
DRAW_TRIGGER_RX = re.compile(
    r"whenever an opponent draws (?P<which>a card|a card except the first one they draw in each of their draw steps|"
    r"their second card each turn|their first card each turn)\b",
    re.I,
)
YOU_DRAW_RX = re.compile(r"\byou (?:may )?draw (a|an|one|two|three|\d+) cards?\b", re.I)
UNLESS_PAY = re.compile(r"unless (?:that player|they|that opponent) pays? (?P<cost>(?:\{[^}]+\})+)", re.I)


def _n(w):
    w = w.lower()
    return int(w) if w.isdigit() else DRAW_NUM.get(w, 1)


def parse(name, text, type_line):
    """Return (rule, reason) for supported opponent-dependent draw text."""
    if "Instant" in type_line or "Sorcery" in type_line:
        return None, None
    t = semantics.clean(name, text)
    reasons = []
    for sent in semantics.sentences(t):
        if semantics.intervening_if(sent) and "opponent" in sent.lower() and "draw" in sent.lower():
            reasons.append("intervening-if opponent-dependent draw is not modelled")
            continue
        cm = CAST_RX.search(sent)
        if cm:
            dm = YOU_DRAW_RX.search(sent)
            if not dm:
                reasons.append("opponent-cast trigger does not directly draw cards for you")
                continue
            if re.search(r"second spell|first spell|from (?:a|their|the) graveyard|from exile|during", sent, re.I):
                reasons.append("qualified opponent-cast condition is not modelled")
                continue
            q = (cm.group("qual") or "").strip().lower()
            scope = q if q else "any"
            pm = UNLESS_PAY.search(sent)
            tax = pm.group("cost") if pm else None
            return {"source": "opponent_cast", "scope": scope, "cards": _n(dm.group(1)), "tax": tax}, None

        om = DRAW_TRIGGER_RX.search(sent)
        if om:
            dm = YOU_DRAW_RX.search(sent)
            if not dm:
                reasons.append("opponent-draw trigger does not directly draw cards for you")
                continue
            w = om.group("which").lower()
            if w == "a card":
                mode = "each_card"
            elif "second card" in w:
                mode = "second_card"
            elif "first card" in w:
                mode = "first_card"
            else:
                mode = "beyond_first_draw_step"
            return {"source": "opponent_draw", "scope": mode, "cards": _n(dm.group(1)), "tax": None}, None

    if re.search(r"whenever an opponent[^.]{0,120}\bdraw\b|whenever an opponent casts[^.]{0,120}\bdraw\b", t, re.I):
        return None, (reasons[0] if reasons else "opponent-dependent draw wording is outside the bounded proxy")
    return None, None


def reason(name, text, type_line):
    return parse(name, text, type_line)[1]


def matches(name, text, type_line):
    return parse(name, text, type_line)[0] is not None


def _active_rounds(trace, name, T):
    """Number of end-of-your-turn states by T where the permanent can observe the following opponent turn cycle."""
    return sum(1 for s in trace if s["turn"] <= T and name in s.get("battlefield", []))


def _cast_events_per_round(rule, spells, noncreature_share):
    scope = rule["scope"]
    base = OPPONENTS * spells
    if scope == "any":
        return base
    if scope == "noncreature":
        return base * noncreature_share
    if scope == "creature":
        return base * (1.0 - noncreature_share)
    # Artifact/enchantment/instant/sorcery shares cannot be inferred from a single noncreature share.
    return None


def _draw_events_per_round(rule, cards_per_turn):
    w = rule["scope"]
    if w == "each_card":
        return OPPONENTS * cards_per_turn
    if w == "second_card":
        return OPPONENTS * (1.0 if cards_per_turn >= 2 else 0.0)
    if w == "first_card":
        return float(OPPONENTS) if cards_per_turn >= 1 else 0.0
    if w == "beyond_first_draw_step":
        return OPPONENTS * max(0.0, cards_per_turn - 1.0)
    return None


def side(games, name, rule, T, point):
    """Expected-card sensitivity value for one declared grid point.

    point = (opponent_spells_per_turn, noncreature_share, nonpay_share, opponent_cards_drawn_per_turn).
    Non-applicable axes are ignored. This is a sensitivity calculation, not an empirical expectation.
    """
    spells, noncreature, nonpay, draws = point
    if rule["source"] == "opponent_cast":
        events = _cast_events_per_round(rule, spells, noncreature)
        if events is None:
            return None
        if rule["tax"] is None:
            nonpay = 1.0
        per_round = events * nonpay * rule["cards"]
    else:
        events = _draw_events_per_round(rule, draws)
        if events is None:
            return None
        per_round = events * rule["cards"]
    vals = []
    for _, tr in games:
        vals.append(_active_rounds(tr, name, T) * per_round)
    return sum(vals) / max(1, len(vals))


def points():
    return [(s, n, p, d) for s in SPELLS_PER_OPPONENT_TURN for n in NONCREATURE_SHARE
            for p in NONPAY_SHARE for d in CARDS_DRAWN_PER_OPPONENT_TURN]


class OpponentDependentDraw:
    SPEC = {
        "id": "opponent_dependent_draw", "version": "1", "family": "opponent-dependent draw",
        "evidence_class": "test_result",
        "models": [
            "Rhystic/Mystic-style 'whenever an opponent casts [noncreature] spell, you draw unless they pay' as a bounded sensitivity grid",
            "unconditional supported opponent-cast draw triggers",
            "supported opponent-draw triggers: each card / first / second / cards beyond the first draw-step card",
            "active opponent turn cycles by turn 4/6/8/10 from the v1.1 battlefield trace",
        ],
        "does_not_model": [
            "actual opponent decks, sequencing, mana, choices, threat assessment or politics",
            "artifact/enchantment/instant/sorcery opponent-cast mix (parsed but left unscored rather than guessed)",
            "tax amount -> payment-behavior conversion; tax is recorded but nonpayment is a declared sensitivity axis",
            "opponent replacement effects, wheels or exact draw-step timing",
            "trigger payloads other than the direct fixed cards you draw",
            "multiplayer win rates (never produced)",
        ],
        "assumptions": [
            "three opponents (four-player Commander table)",
            "opponent spells per opponent turn is swept over 1/2/3; noncreature share over 0.5/0.7/0.9",
            "for taxed draw, nonpayment share is swept over 0.25/0.5/0.75 independent of tax size; these are sensitivity points, not estimates",
            "opponent cards drawn per opponent turn is swept over 1/2/3 for opponent-draw triggers",
            "if the permanent is present at your end step, it observes the following opponent turn cycle",
        ],
        "parameters": {"turns": TURNS, "opponents": OPPONENTS,
                       "opponent_spells_per_turn": list(SPELLS_PER_OPPONENT_TURN),
                       "noncreature_share": list(NONCREATURE_SHARE), "nonpay_share": list(NONPAY_SHARE),
                       "opponent_cards_drawn_per_turn": list(CARDS_DRAWN_PER_OPPONENT_TURN)},
        "confidence": "low",
        "limitations": [
            "The range is deliberately wide and should only distinguish robust direction/availability; no midpoint is a real-game estimate.",
            "Creature/enchantment removal by opponents is not coupled to this proxy; bracket stress handles disruption separately.",
        ],
        "metrics": ["opponent_dependent_draw_range_by_turn"],
        "determinism": "seeded paired v1.1 battlefield trace plus closed-form bounded opponent sensitivity grid",
        "test_file": "tests/test_mech_opponent_semantics.py",
    }

    @staticmethod
    def matches(name, text, type_line):
        return matches(name, text, type_line)

    @staticmethod
    def reason(name, text, type_line):
        return reason(name, text, type_line)

    @classmethod
    def evaluate(cls, base_games, chal_games, cut, add, cards, ctx):
        ra = parse(add, cards[add]["text"], cards[add]["type_line"])[0] if add in cards else None
        rc = parse(cut, cards[cut]["text"], cards[cut]["type_line"])[0] if cut in cards else None
        out = {"module": cls.SPEC["id"], "version": cls.SPEC["version"], "evidence_class": "test_result",
               "semantics": {"add": ra, "cut": rc}, "metrics": {}}
        for T in TURNS:
            vals = []
            for pt in points():
                a = side(chal_games, add, ra, T, pt) if ra else 0.0
                c = side(base_games, cut, rc, T, pt) if rc else 0.0
                if a is None or c is None:
                    continue
                vals.append(round(a - c, 4))
            out["metrics"][str(T)] = ({"diff_range": [min(vals), max(vals)]} if vals else
                                      {"not_modelable": "parsed scope has no declared composition axis"})
        return out
