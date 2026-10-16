"""Step E cost-model modules (ChatGPT cycle 66.7): X-spell capacity and supported alternate costs.

These modules repair two deliberate v1.1 simplifications without changing grixis_sim.py: v1.1 treats X as zero and
casts cards only at their normal cost. We derive bounded opportunity metrics from the same paired trace instead.
"""
import math
import re

from . import events, semantics

TURNS = [4, 6, 8, 10]
PIP = re.compile(r"\{([^}]+)\}")


def _spec(id_, family, models, does_not, assumptions, limits, metrics):
    return {"id": id_, "version": "1", "family": family, "evidence_class": "test_result",
            "models": models, "does_not_model": does_not + ["multiplayer win rates (never produced)"],
            "assumptions": assumptions, "parameters": {"turns": TURNS}, "confidence": "low",
            "limitations": limits, "metrics": metrics,
            "determinism": "seeded paired v1.1 games; derived from the deterministic zone/mana trace",
            "test_file": "tests/test_mech_cost_semantics.py"}


def _unspent(s):
    return max(0, (s.get("mana") or 0) - (s.get("spent") or 0))


def _front_cost(card):
    return (card or {}).get("mana_cost", "") or ""


def _normal_need(n, ctx):
    return int((ctx.get("models", {}).get(n) or {}).get("mv") or 0)


def _mana_value_of_symbols(cost):
    """Mana-only cost proxy: generic numerals + one per colored/colorless/hybrid pip. X is unsupported here."""
    total = 0
    for p in PIP.findall(cost or ""):
        u = p.upper()
        if u.isdigit():
            total += int(u)
        elif u in ("X", "Y", "Z"):
            return None
        elif u in ("T", "Q"):
            continue
        elif "/P" in u:
            total += 1
        else:
            total += 1
    return total


# ---------------------------------------------------------------- X spells
def x_rule(card):
    cost = _front_cost(card)
    n = sum(1 for p in PIP.findall(cost) if p.upper() == "X")
    return {"x_symbols": n, "mana_cost": cost} if n else None


def x_capacity(games, n, ctx, T):
    card = ctx["cards"].get(n, {})
    rule = x_rule(card)
    if not rule:
        return {"mean_max_x": 0.0, "mean_ready_turns": 0.0}
    xs = rule["x_symbols"]
    base = _normal_need(n, ctx)  # v1.1 MV has X=0, so this is the fixed portion.
    vals, ready = [], []
    for _, tr in games:
        casts = dict(events.casts(tr, ctx["models"]))
        best, nready = 0, 0
        for s in tr:
            if s["turn"] > T:
                break
            spare = _unspent(s)
            if n in s.get("hand", []):
                # Card has not been cast yet: fixed cost must still be paid.
                x = max(0, math.floor((spare - base) / xs)) if spare >= base else 0
                nready += 1 if spare >= base else 0
                best = max(best, x)
            if n in casts.get(s["turn"], []):
                # v1.1 already paid the fixed part with X=0. Spare mana could instead have gone into X.
                x = max(0, math.floor(spare / xs))
                nready += 1
                best = max(best, x)
        vals.append(best)
        ready.append(nready)
    d = max(1, len(games))
    return {"mean_max_x": sum(vals) / d, "mean_ready_turns": sum(ready) / d}


class XSpells:
    SPEC = _spec("x_spells", "X-spell mana scaling",
                 ["for spells with X in the printed mana cost: maximum additional X supported by the v1.1 mana trace by turn 4/6/8/10",
                  "both pre-cast hand opportunities and the turn v1.1 actually casts the spell at X=0"],
                 ["what X buys (damage, cards, tokens, targets)", "X in activated abilities rather than the spell mana cost",
                  "colored-pip constraints beyond v1.1's already-paid fixed cost", "cost reducers/increasers that specifically affect X"],
                 ["v1.1's card-model mana value is the fixed portion because X contributes zero to mana value",
                  "when v1.1 casts the card, all end-of-turn unspent mana is treated as potential additional X without undoing other casts",
                  "multiple {X} symbols divide available extra mana equally (e.g. {X}{X} uses two mana per +1 X)"],
                 ["This is capacity, not strategic value; a larger X is not automatically better than another card."],
                 ["mean_max_x_by_turn", "x_ready_turns_by_turn"])

    @staticmethod
    def matches_card(name, card):
        return x_rule(card) is not None

    @staticmethod
    def reason(name, text, type_line):
        return None

    @classmethod
    def evaluate(cls, b, c, cut, add, cards, ctx):
        out = {"module": cls.SPEC["id"], "version": cls.SPEC["version"], "evidence_class": "test_result", "metrics": {}}
        ia = add in cards and cls.matches_card(add, cards[add])
        ic = cut in cards and cls.matches_card(cut, cards[cut])
        for T in TURNS:
            a = x_capacity(c, add, ctx, T) if ia else {"mean_max_x": 0.0, "mean_ready_turns": 0.0}
            z = x_capacity(b, cut, ctx, T) if ic else {"mean_max_x": 0.0, "mean_ready_turns": 0.0}
            out["metrics"][str(T)] = {"diff_mean_max_x": round(a["mean_max_x"] - z["mean_max_x"], 4),
                                      "diff_x_ready_turns": round(a["mean_ready_turns"] - z["mean_ready_turns"], 4)}
        return out


# ---------------------------------------------------------------- supported alternate costs
PAY_RATHER = re.compile(r"you may pay (?P<cost>(?:\{[^}]+\})+) rather than pay (?:~|this spell)'?s? mana cost", re.I)
NOT_TURN = re.compile(r"if it(?:'|’)s not your turn, you may pay (?P<cost>(?:\{[^}]+\})+) rather than pay (?:~|this spell)'?s? mana cost", re.I)
FREE_COMMANDER = re.compile(r"if you control a commander, you may cast (?:~|this spell) without paying its mana cost", re.I)
EVOKE = re.compile(r"(?:^|\n)evoke (?P<cost>(?:\{[^}]+\})+)", re.I)
RESOURCE_ALT = re.compile(r"(?:rather than pay [^.]{0,80}(?:exile|discard|pay \d+ life)|delve\b|convoke\b|affinity for|improvise\b)", re.I)


def alternate_parse(name, text, type_line):
    t = semantics.clean(name, text)
    if "Instant" not in type_line and "Sorcery" not in type_line and "Creature" not in type_line and "Artifact" not in type_line and "Enchantment" not in type_line:
        return None, None
    if FREE_COMMANDER.search(t):
        return {"kind": "free_with_commander", "mana": 0, "condition": "commander", "drawback": None}, None
    m = NOT_TURN.search(t)
    if m:
        cost = _mana_value_of_symbols(m.group("cost"))
        if cost is not None:
            return {"kind": "fixed_mana", "mana": cost, "condition": "opponent_turn", "drawback": None}, None
    m = PAY_RATHER.search(t)
    if m:
        cost = _mana_value_of_symbols(m.group("cost"))
        if cost is not None:
            return {"kind": "fixed_mana", "mana": cost, "condition": "none", "drawback": None}, None
    m = EVOKE.search(t)
    if m:
        cost = _mana_value_of_symbols(m.group("cost"))
        if cost is not None:
            return {"kind": "evoke", "mana": cost, "condition": "none", "drawback": "sacrifice_after_etb"}, None
    if re.search(r"\b(?:flashback|escape|retrace|jump-start|aftermath)\b", t, re.I):
        return None, "alternate zone/keyword casting cost is not modelled"
    if RESOURCE_ALT.search(t) or re.search(r"rather than pay (?:~|this spell)'?s? mana cost|without paying its mana cost", t, re.I):
        return None, "alternate cost depends on cards/life/resources or an unsupported condition"
    if re.search(r"\b(?:evoke|delve|convoke|improvise)\b", t, re.I):
        return None, "resource-based alternate/cost-reduction keyword is not modelled"
    return None, None


def alternate_ready(games, n, ctx, T):
    rule, _ = alternate_parse(n, ctx["cards"][n]["text"], ctx["cards"][n]["type_line"])
    if not rule:
        return {"alt_ready": 0.0, "alt_only": 0.0}
    normal = _normal_need(n, ctx)
    alt = rule["mana"]
    tot, only = 0.0, 0.0
    for _, tr in games:
        a = o = 0
        for s in tr:
            if s["turn"] > T or n not in s.get("hand", []):
                continue
            spare = _unspent(s)
            cond = rule["condition"]
            ok_condition = True
            if cond == "commander":
                ok_condition = any(x in set(ctx.get("commanders") or ()) for x in s.get("battlefield", []))
            # End-of-own-turn mana is explicitly the resource carried into the next opponent turn, so opponent_turn is true.
            alt_ok = ok_condition and spare >= alt
            normal_ok = spare >= normal
            a += 1 if alt_ok else 0
            o += 1 if alt_ok and not normal_ok else 0
        tot += a
        only += o
    d = max(1, len(games))
    return {"alt_ready": tot / d, "alt_only": only / d}


class AlternateCosts:
    SPEC = _spec("alternate_costs", "alternate casting costs",
                 ["supported self-contained alternate costs: fixed mana rather than normal cost, not-your-turn fixed mana, commander-controlled free cast, and Evoke",
                  "turns by 4/6/8/10 where the card is in hand and the alternate line is affordable; separately, turns where the alternate line works but the normal cost does not"],
                 ["pitch/exile/discard/life-payment alternate costs", "delve/convoke/improvise/affinity resource accounting",
                  "Flashback/escape/retrace/adventure or other alternate zones", "the strategic drawback/value of Evoke", "colored-pip availability"],
                 ["normal and alternate mana requirements are converted to total mana for a readiness proxy",
                  "'if it's not your turn' is evaluated against the following opponent-turn cycle represented by end-of-own-turn held mana",
                  "commander-free costs require a project commander to be on the battlefield in the trace"],
                 ["An alternate-cost opportunity is not a recommendation; resource-based alternate costs stay explicitly not_modelable."],
                 ["alternate_ready_turns_by_turn", "alternate_only_ready_turns_by_turn"])

    @staticmethod
    def matches_card(name, card):
        return alternate_parse(name, card.get("text", ""), card.get("type_line", ""))[0] is not None

    @staticmethod
    def reason(name, text, type_line):
        return alternate_parse(name, text, type_line)[1]

    @classmethod
    def evaluate(cls, b, c, cut, add, cards, ctx):
        out = {"module": cls.SPEC["id"], "version": cls.SPEC["version"], "evidence_class": "test_result",
               "semantics": {}, "metrics": {}}
        ia = add in cards and cls.matches_card(add, cards[add])
        ic = cut in cards and cls.matches_card(cut, cards[cut])
        for n in (cut, add):
            if n in cards:
                r, why = alternate_parse(n, cards[n]["text"], cards[n]["type_line"])
                out["semantics"][n] = {"rule": r, "not_modelable": why}
        for T in TURNS:
            a = alternate_ready(c, add, ctx, T) if ia else {"alt_ready": 0.0, "alt_only": 0.0}
            z = alternate_ready(b, cut, ctx, T) if ic else {"alt_ready": 0.0, "alt_only": 0.0}
            out["metrics"][str(T)] = {"diff_alt_ready_turns": round(a["alt_ready"] - z["alt_ready"], 4),
                                      "diff_alt_only_ready_turns": round(a["alt_only"] - z["alt_only"], 4)}
        return out
