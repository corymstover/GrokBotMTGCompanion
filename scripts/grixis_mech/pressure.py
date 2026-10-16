"""Bounded table-pressure modules for Step E (ChatGPT cycle 66.12).

These modules deliberately model *event demand*, not strategic value or multiplayer outcomes:
- table_life_loss: nominal fixed damage/life loss to each opponent/player from supported spell/ETB/phase/cast events;
- discard_pressure: fixed cards opponents are instructed to discard from the same supported event families.

Unsupported targeting, variable quantities, conditional clauses and opponent-behaviour triggers are refused rather than
forced into a generic estimate. Damage is reported as nominal life loss before prevention/replacement effects.
"""
import re

from . import events
from .semantics import clean, sentences, intervening_if, N_PLAYERS

TURNS = [4, 6, 8, 10]
OPPONENTS = N_PLAYERS - 1
NO_WIN = "multiplayer win rates (never produced)"
NUM = {"a": 1, "an": 1, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
NUMPAT = r"(?:a|an|one|two|three|four|five|\d+)"

LIFE_LOSS = re.compile(
    rf"(?P<who>each opponent|each of your opponents|each player) loses (?P<n>{NUMPAT}) life", re.I)
DAMAGE = re.compile(
    rf"(?:~|this spell) deals (?P<n>{NUMPAT}) damage to (?P<who>each opponent|each of your opponents|each player)", re.I)
DISCARD = re.compile(
    rf"(?P<who>each opponent|each of your opponents|each other player|each player|target opponent) discards? (?P<n>{NUMPAT}) cards?", re.I)


def _amount(s):
    s = s.lower()
    return int(s) if s.isdigit() else NUM[s]


def _who(who):
    w = who.lower()
    if w in ("each opponent", "each of your opponents", "each other player"):
        return OPPONENTS, False
    if w == "each player":
        return OPPONENTS, True
    if w == "target opponent":
        return 1, False
    raise ValueError(who)


def _timing(name, sent, type_line):
    """Return a supported event rule or a refusal reason."""
    if intervening_if(sent):
        return None, "conditional (intervening-if) pressure effect"
    low = sent.lower()
    if re.search(r"whenever (?:an opponent|a player|each opponent|another player) ", low):
        return None, "opponent-behaviour trigger is not modelled by this module"
    if re.search(r"whenever you cast", sent, re.I):
        from .engines import cast_parse
        f, why = cast_parse(name, sent)
        return ({"kind": "cast", "cast_filter": f}, None) if f else (None, why or "unsupported cast trigger")
    if events.ETB.search(sent):
        return {"kind": "etb"}, None
    if events.UPKEEP.search(sent):
        mult = N_PLAYERS if re.search(r"beginning of each", sent, re.I) else 1
        return {"kind": "phase", "multiplier": mult}, None
    if re.search(r"\b(?:whenever|when|at the beginning of)\b", sent, re.I):
        return None, "trigger condition is outside the supported spell/ETB/phase/cast families"
    if "Instant" in type_line or "Sorcery" in type_line:
        return {"kind": "spell"}, None
    return None, "pressure text on a permanent has no supported event timing"


def life_parse(name, text, type_line):
    t = clean(name, text)
    why = None
    for sent in sentences(t):
        m = LIFE_LOSS.search(sent) or DAMAGE.search(sent)
        if not m:
            continue
        timing, w = _timing(name, sent, type_line)
        if not timing:
            why = w
            continue
        targets, self_burden = _who(m.group("who"))
        timing.update(amount=_amount(m.group("n")), opponents=targets, self_burden=self_burden,
                      mode="damage" if DAMAGE.search(sent) else "life_loss")
        return timing, None
    if why:
        return None, why
    if re.search(r"(?:each opponent|each player).{0,50}(?:loses? .* life|damage)|damage to (?:each opponent|each player)", t, re.I):
        return None, "life-loss/damage wording has variable, targeted or unsupported semantics"
    return None, None


def discard_parse(name, text, type_line):
    t = clean(name, text)
    why = None
    for sent in sentences(t):
        m = DISCARD.search(sent)
        if not m:
            continue
        timing, w = _timing(name, sent, type_line)
        if not timing:
            why = w
            continue
        targets, self_burden = _who(m.group("who"))
        timing.update(amount=_amount(m.group("n")), opponents=targets, self_burden=self_burden)
        return timing, None
    if why:
        return None, why
    if re.search(r"\bdiscards?\b", t, re.I):
        return None, "discard wording is self-discard, variable/hand-wide, conditional, or otherwise outside the fixed opponent-pressure model"
    return None, None


def _cast_event_count(rule, source, cs, s, on, ctx):
    f = rule["cast_filter"]
    if not on:
        return 0
    if f.get("commander"):
        return 1 if s.get("commander_cast") == s["turn"] else 0
    other = [c for c in cs if c != source]
    if f.get("ordinal"):
        return 1 if len(other) >= f["ordinal"] else 0
    from .engines import cast_ok
    return sum(1 for c in other if cast_ok(f["kinds"], ctx["models"].get(c)))


def _per_turn_events(trace, source, rule, ctx):
    casts = dict(events.casts(trace, ctx["models"]))
    out, on, prev_bf = {}, False, set()
    for s in trace:
        t = s["turn"]
        bf = set(s.get("battlefield", []))
        k = rule["kind"]
        n = 0
        if k == "spell":
            n = 1 if source in casts.get(t, []) else 0
        elif k == "etb":
            n = 1 if source in bf and source not in prev_bf else 0
        elif k == "phase":
            # Conservative: beginning-of-phase effects start on the turn after the first end-step snapshot with source present.
            n = rule.get("multiplier", 1) if on else 0
        elif k == "cast":
            n = _cast_event_count(rule, source, casts.get(t, []), s, on, ctx)
        if n:
            out[t] = out.get(t, 0) + n
        on = source in bf
        prev_bf = bf
    return out


def _side(games, source, rule, ctx, T, kind):
    totals, maxima, selfs = [], [], []
    for _, tr in games:
        ev = _per_turn_events(tr, source, rule, ctx)
        amount = rule["amount"]
        opp_mult = rule["opponents"]
        by_turn = {t: n * amount * opp_mult for t, n in ev.items() if t <= T}
        totals.append(sum(by_turn.values()))
        maxima.append(max(by_turn.values(), default=0))
        selfs.append(sum(n * amount for t, n in ev.items() if t <= T) if rule.get("self_burden") else 0)
    n = max(1, len(games))
    return {"opponent_demand": sum(totals) / n,
            "max_same_turn_opponent_demand": sum(maxima) / n,
            "self_burden": sum(selfs) / n,
            "kind": kind}


def _evaluate(base_games, chal_games, cut, add, cards, ctx, parser, module_id, metric_name):
    out = {"module": module_id, "evidence_class": "test_result", "metrics": {}}
    pa = parser(add, cards[add]["text"], cards[add]["type_line"])[0] if add in cards else None
    pc = parser(cut, cards[cut]["text"], cards[cut]["type_line"])[0] if cut in cards else None
    for T in TURNS:
        a = _side(chal_games, add, pa, ctx, T, metric_name) if pa else {"opponent_demand": 0.0, "max_same_turn_opponent_demand": 0.0, "self_burden": 0.0, "kind": metric_name}
        c = _side(base_games, cut, pc, ctx, T, metric_name) if pc else {"opponent_demand": 0.0, "max_same_turn_opponent_demand": 0.0, "self_burden": 0.0, "kind": metric_name}
        out["metrics"][str(T)] = {"add": a, "cut": c,
                                  "diff_opponent_demand": round(a["opponent_demand"] - c["opponent_demand"], 4),
                                  "diff_max_same_turn": round(a["max_same_turn_opponent_demand"] - c["max_same_turn_opponent_demand"], 4),
                                  "diff_self_burden": round(a["self_burden"] - c["self_burden"], 4)}
    return out


class TableLifeLoss:
    SPEC = {
        "id": "life_loss", "version": "1", "family": "fixed table life loss / damage",
        "evidence_class": "test_result",
        "models": [
            "fixed 'each opponent/player loses N life' and '~ deals N damage to each opponent/player' payloads",
            "supported event families: one-shot instant/sorcery resolution, ETB, beginning-of-phase, and supported 'whenever you cast' triggers",
            "cumulative nominal opponent life loss and maximum same-turn nominal contribution by turn 4/6/8/10",
        ],
        "does_not_model": [
            "damage prevention, infect/wither-style replacement, lifelink, damage doublers/replacers, or player-specific replacement effects",
            "targeted/choice-based damage, variable X/for-each amounts, combat-damage triggers, death triggers, or conditional/intervening-if effects",
            "whether life loss is strategically useful or sufficient for a commander threshold; judgment/Step D owns that interpretation",
            NO_WIN,
        ],
        "assumptions": [
            "four-player Commander table (three opponents)",
            "supported damage is treated as nominal life loss before prevention/replacement effects",
            "beginning-of-phase permanent triggers begin on the turn after the source first appears in the end-step trace",
            "cast-trigger frequency uses the same supported cast parser and v1.1 cast trace as cast_triggers",
        ],
        "parameters": {"turns": TURNS, "opponents": OPPONENTS},
        "confidence": "low",
        "limitations": ["This is pressure/threshold evidence, not a damage-to-win simulation or card-quality score."],
        "metrics": ["opponent_life_loss_by_turn", "max_same_turn_opponent_life_loss", "self_life_loss_burden"],
        "determinism": "deterministic function of seeded v1.1 zone/cast traces; no extra rng",
        "test_file": "tests/test_mech_pressure_semantics.py",
    }

    @staticmethod
    def matches(name, text, type_line):
        return life_parse(name, text, type_line)[0] is not None

    @staticmethod
    def reason(name, text, type_line):
        return life_parse(name, text, type_line)[1]

    @classmethod
    def evaluate(cls, b, c, cut, add, cards, ctx):
        return _evaluate(b, c, cut, add, cards, ctx, life_parse, cls.SPEC["id"], "life_loss")


class DiscardPressure:
    SPEC = {
        "id": "discard", "version": "1", "family": "fixed opponent discard pressure",
        "evidence_class": "test_result",
        "models": [
            "fixed 'each opponent/other player/target opponent discards N cards' payloads and symmetric each-player discard",
            "supported event families: one-shot instant/sorcery resolution, ETB, beginning-of-phase, and supported 'whenever you cast' triggers",
            "cumulative opponent discard demand and maximum same-turn demand by turn 4/6/8/10",
        ],
        "does_not_model": [
            "opponent hand sizes, whether requested discards can actually be paid, card selection/randomness quality, madness or graveyard synergies",
            "self-discard/loot as an enabler, whole-hand/variable discard, combat-damage discard, opponent-behaviour triggers, conditional effects",
            "the strategic value of stripping a particular card or whether discard converts into a win",
            NO_WIN,
        ],
        "assumptions": [
            "four-player Commander table (three opponents)",
            "discard demand counts instructions, not successful cards discarded; empty hands are not simulated",
            "beginning-of-phase permanent triggers begin on the turn after the source first appears in the end-step trace",
        ],
        "parameters": {"turns": TURNS, "opponents": OPPONENTS},
        "confidence": "low",
        "limitations": ["Demand is deliberately not converted into card advantage or a generic disruption score."],
        "metrics": ["opponent_discard_demand_by_turn", "max_same_turn_opponent_discard_demand", "self_discard_burden"],
        "determinism": "deterministic function of seeded v1.1 zone/cast traces; no extra rng",
        "test_file": "tests/test_mech_pressure_semantics.py",
    }

    @staticmethod
    def matches(name, text, type_line):
        return discard_parse(name, text, type_line)[0] is not None

    @staticmethod
    def reason(name, text, type_line):
        return discard_parse(name, text, type_line)[1]

    @classmethod
    def evaluate(cls, b, c, cut, add, cards, ctx):
        return _evaluate(b, c, cut, add, cards, ctx, discard_parse, cls.SPEC["id"], "discard")
