"""Step E tutor/graveyard-setup modules (ChatGPT cycle 66.8).

`graveyard_tutoring` covers deterministic selected-to-graveyard search plus fixed self-mill/surveil capacity.
`repeatable_tutors` covers supported activated and own-upkeep library searches. Neither module assigns strategic value
to the card found; they measure opportunity/breadth only.
"""
import re

from . import events, graveyard, semantics

TURNS = [4, 6, 8, 10]
NUM = {"a": 1, "an": 1, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8,
       "nine": 9, "ten": 10}
PIP = re.compile(r"\{([^}]+)\}")
SEARCH = re.compile(r"search your library for (?:a|an|up to one) (?P<desc>[^,.]*?)card\b", re.I)
TO_GY = re.compile(r"put (?:it|that card|the card) into your graveyard", re.I)
DEST = {
    "hand": re.compile(r"put (?:it|that card|the card) into your hand", re.I),
    "battlefield": re.compile(r"put (?:it|that card|the card) onto the battlefield", re.I),
    "top": re.compile(r"put (?:it|that card|the card) on top of your library", re.I),
}
MILL = re.compile(r"\bmills? (a|an|one|two|three|four|five|six|seven|eight|nine|ten|\d+) cards?\b", re.I)
SURVEIL = re.compile(r"\bsurveil (one|two|three|four|five|six|seven|eight|nine|ten|\d+)\b", re.I)


def _num(w):
    w = w.lower()
    return int(w) if w.isdigit() else NUM.get(w)


def _spec(id_, family, models, does_not, assumptions, limits, metrics):
    return {"id": id_, "version": "1", "family": family, "evidence_class": "test_result", "models": models,
            "does_not_model": does_not + ["multiplayer win rates (never produced)"], "assumptions": assumptions,
            "parameters": {"turns": TURNS}, "confidence": "low", "limitations": limits, "metrics": metrics,
            "determinism": "seeded paired v1.1 games; derived from the deterministic zone/mana trace",
            "test_file": "tests/test_mech_tutor_semantics.py"}


def _mode(sent, type_line, action_start):
    if "Instant" in type_line or "Sorcery" in type_line:
        return "spell", None
    if semantics.intervening_if(sent):
        return None, "intervening-if tutor/setup trigger is not modelled"
    if re.match(r"^when(?:ever)? ~ enters\b", sent, re.I):
        return "etb", None
    if re.match(r"^at the beginning of your upkeep\b", sent, re.I):
        return "upkeep", None
    if re.match(r"^at the beginning of|^whenever|^when", sent, re.I):
        return None, "trigger timing other than ETB/your upkeep is not modelled"
    if ":" in sent[:action_start]:
        return "activated", None
    return None, "permanent setup/tutor text is not a supported activated ability or trigger"


def _target(desc):
    return graveyard._target_spec(desc)  # shared semantic target grammar; returns (spec, reason)


def _arrived(n, s, prev_bf):
    return n in s.get("battlefield", []) and n not in prev_bf


def _occurrences(games, n, rule, ctx, T):
    """Mean number of supported rule events by T; activated means one potential use per own turn."""
    total = 0.0
    for _, tr in games:
        casts = dict(events.casts(tr, ctx["models"]))
        prev = set()
        k = 0
        for s in tr:
            if s["turn"] > T:
                break
            mode = rule["mode"]
            if mode == "spell":
                k += 1 if n in casts.get(s["turn"], []) else 0
            elif mode == "etb":
                k += 1 if _arrived(n, s, prev) else 0
            elif mode == "upkeep":
                k += 1 if n in prev else 0
            elif mode == "activated":
                k += 1 if n in s.get("battlefield", []) else 0
            prev = set(s.get("battlefield", []))
        total += k
    return total / max(1, len(games))


# ---------------------------------------------------------------- graveyard setup
def graveyard_parse(name, text, type_line):
    t = semantics.clean(name, text)
    reasons = []
    for sent in semantics.sentences(t):
        sm = SEARCH.search(sent)
        if sm and TO_GY.search(sent):
            spec, why = _target(sm.group("desc"))
            if not spec:
                reasons.append(why)
                continue
            mode, why = _mode(sent, type_line, sm.start())
            if not mode:
                reasons.append(why)
                continue
            return {"kind": "selected_to_graveyard", "mode": mode, "target": spec, "amount": 1}, None
        mm = MILL.search(sent)
        if mm:
            pre = sent[:mm.start()].lower()
            if re.search(r"(?:target|each) (?:player|opponent)|(?:an|each) opponent", pre):
                reasons.append("opponent/other-player mill is not modelled as self graveyard setup")
                continue
            mode, why = _mode(sent, type_line, mm.start())
            if not mode:
                reasons.append(why)
                continue
            return {"kind": "mill", "mode": mode, "amount": _num(mm.group(1))}, None
        sv = SURVEIL.search(sent)
        if sv:
            mode, why = _mode(sent, type_line, sv.start())
            if not mode:
                reasons.append(why)
                continue
            return {"kind": "surveil", "mode": mode, "amount": _num(sv.group(1))}, None
    if re.search(r"search your library[^.]{0,100}graveyard|\bmills?\b|\bsurveils?\b", t, re.I):
        return None, (reasons[0] if reasons else "variable/qualified or otherwise unsupported graveyard-setup wording")
    return None, None


def graveyard_setup_metric(games, n, ctx, T):
    rule, _ = graveyard_parse(n, ctx["cards"][n]["text"], ctx["cards"][n]["type_line"])
    if not rule:
        return {"events": 0.0, "cards": 0.0, "surveil_capacity": 0.0}
    e = _occurrences(games, n, rule, ctx, T)
    if rule["kind"] == "surveil":
        return {"events": e, "cards": 0.0, "surveil_capacity": e * rule["amount"]}
    return {"events": e, "cards": e * rule["amount"], "surveil_capacity": 0.0}


class GraveyardTutoring:
    SPEC = _spec("graveyard_tutoring", "graveyard setup/tutoring",
                 ["supported search-to-your-graveyard effects: event opportunities and selected cards put into the graveyard",
                  "fixed-number self-mill: cards milled by turn 4/6/8/10",
                  "fixed-number surveil: cards looked at/ordered as graveyard-selection capacity, not assumed to be binned"],
                 ["which random cards are milled", "variable X/equal-to/for-each mill counts", "opponent mill",
                  "conditional triggers other than ETB/your upkeep", "mana/tap/non-mana cost affordability of activated setup",
                  "strategic value of the tutored/milled card"],
                 ["spell events use the v1.1 cast trace; ETB uses arrival; your-upkeep triggers begin the turn after arrival",
                  "activated setup is one potential use per own turn while the permanent is on the battlefield (cost not paid)",
                  "surveil N is reported as N cards of selection capacity and zero guaranteed graveyard cards"],
                 ["This module measures setup opportunity, not actual reanimation/combo conversion."],
                 ["graveyard_setup_events_by_turn", "graveyard_cards_added_by_turn", "surveil_capacity_by_turn"])

    @staticmethod
    def matches(name, text, type_line):
        return graveyard_parse(name, text, type_line)[0] is not None

    @staticmethod
    def reason(name, text, type_line):
        return graveyard_parse(name, text, type_line)[1]

    @classmethod
    def evaluate(cls, b, c, cut, add, cards, ctx):
        out = {"module": cls.SPEC["id"], "version": cls.SPEC["version"], "evidence_class": "test_result",
               "semantics": {}, "metrics": {}}
        ia = add in cards and cls.matches(add, cards[add]["text"], cards[add]["type_line"])
        ic = cut in cards and cls.matches(cut, cards[cut]["text"], cards[cut]["type_line"])
        for n in (cut, add):
            if n in cards:
                r, why = graveyard_parse(n, cards[n]["text"], cards[n]["type_line"])
                out["semantics"][n] = {"rule": r, "not_modelable": why}
        zero = {"events": 0.0, "cards": 0.0, "surveil_capacity": 0.0}
        for T in TURNS:
            a = graveyard_setup_metric(c, add, ctx, T) if ia else zero
            z = graveyard_setup_metric(b, cut, ctx, T) if ic else zero
            out["metrics"][str(T)] = {"diff_events": round(a["events"] - z["events"], 4),
                                      "diff_graveyard_cards": round(a["cards"] - z["cards"], 4),
                                      "diff_surveil_capacity": round(a["surveil_capacity"] - z["surveil_capacity"], 4)}
        return out


# ---------------------------------------------------------------- repeatable tutors
def _dest(sent):
    return next((k for k, rx in DEST.items() if rx.search(sent)), None)


def _activation_cost(before):
    """Return {mana,tap} for a simple mana/tap activation cost; reject non-mana resources."""
    if ":" not in before:
        return None, "missing activated-ability colon"
    cost = before.rsplit(":", 1)[0].strip()
    if re.search(r"\b(?:sacrifice|discard|exile|pay \d+ life|remove [^.]{0,20} counter|return [^.]{0,20} to)\b", cost, re.I):
        return None, "repeatable tutor has an unsupported non-mana/resource activation cost"
    pips = PIP.findall(cost)
    if not pips and "{T}" not in cost:
        return None, "activated tutor cost is not parsed"
    mana = 0
    for p in pips:
        u = p.upper()
        if u.isdigit():
            mana += int(u)
        elif u in ("T", "Q"):
            continue
        elif u in ("X", "Y", "Z"):
            return None, "X activation cost is not modelled"
        else:
            mana += 1
    return {"mana": mana, "tap": "{T}" in cost}, None


def repeatable_parse(name, text, type_line):
    if "Instant" in type_line or "Sorcery" in type_line:
        return None, None
    t = semantics.clean(name, text)
    reasons = []
    for sent in semantics.sentences(t):
        sm = SEARCH.search(sent)
        if not sm:
            continue
        dest = _dest(sent)
        if not dest:
            reasons.append("library search destination is not hand/battlefield/top")
            continue
        spec, why = _target(sm.group("desc"))
        if not spec:
            reasons.append(why)
            continue
        if semantics.intervening_if(sent):
            reasons.append("intervening-if repeatable tutor is not modelled")
            continue
        if re.match(r"^at the beginning of your upkeep\b", sent, re.I):
            return {"mode": "upkeep", "target": spec, "destination": dest, "cost": None}, None
        if re.match(r"^at the beginning of|^whenever|^when", sent, re.I):
            reasons.append("repeatable tutor trigger other than your upkeep is not modelled")
            continue
        if ":" in sent[:sm.start()]:
            cost, why = _activation_cost(sent[:sm.start()])
            if not cost:
                reasons.append(why)
                continue
            return {"mode": "activated", "target": spec, "destination": dest, "cost": cost}, None
        reasons.append("library search on a permanent is not repeatable activated/upkeep text")
    if "search your library" in t.lower():
        return None, (reasons[0] if reasons else "unrecognised repeatable tutor wording")
    return None, None


def _unspent(s):
    return max(0, (s.get("mana") or 0) - (s.get("spent") or 0))


def repeatable_uses(games, n, ctx, T):
    rule, _ = repeatable_parse(n, ctx["cards"][n]["text"], ctx["cards"][n]["type_line"])
    if not rule:
        return 0.0
    creature = "Creature" in ctx["cards"][n]["type_line"]
    total = 0.0
    for _, tr in games:
        prev, k = set(), 0
        for s in tr:
            if s["turn"] > T:
                break
            here = n in s.get("battlefield", [])
            arrived = here and n not in prev
            if rule["mode"] == "upkeep":
                # End-step trace cannot prove a trigger if the card vanished during the turn; require it before and after.
                k += 1 if here and n in prev else 0
            elif here:
                cost = rule["cost"]
                if cost["tap"] and creature and arrived:
                    pass  # summoning sickness resets on every re-entry
                elif _unspent(s) >= cost["mana"]:
                    k += 1
            prev = set(s.get("battlefield", []))
        total += k
    return total / max(1, len(games))


class RepeatableTutors:
    SPEC = _spec("repeatable_tutors", "repeatable tutors",
                 ["supported activated library tutors: turns the permanent is on the battlefield with enough end-of-turn unspent mana",
                  "supported 'at the beginning of your upkeep' library tutors: trigger opportunities beginning after the permanent arrives",
                  "simple any-card/type/union/intersection/nonland-permanent target classes and destinations hand/battlefield/top"],
                 ["one-shot spell/ETB tutors already covered by v1.1", "subtype/color/mana-value/legendary or other target qualifiers",
                  "non-mana activation costs", "conditional/other triggered tutor timings", "opponent tutors", "the value of the selected card"],
                 ["one supported activated use per own turn; colored pips count as one mana each",
                  "a creature's {T} tutor cannot activate on its arrival turn; other summoning-sickness nuances are not inferred",
                  "upkeep tutor fires only if the permanent was already present in the prior end-of-turn trace"],
                 ["Readiness is an opportunity count, not proof that using the tutor is strategically correct."],
                 ["repeatable_tutor_uses_by_turn"])

    @staticmethod
    def matches(name, text, type_line):
        return repeatable_parse(name, text, type_line)[0] is not None

    @staticmethod
    def reason(name, text, type_line):
        return repeatable_parse(name, text, type_line)[1]

    @classmethod
    def evaluate(cls, b, c, cut, add, cards, ctx):
        out = {"module": cls.SPEC["id"], "version": cls.SPEC["version"], "evidence_class": "test_result",
               "semantics": {}, "metrics": {}}
        ia = add in cards and cls.matches(add, cards[add]["text"], cards[add]["type_line"])
        ic = cut in cards and cls.matches(cut, cards[cut]["text"], cards[cut]["type_line"])
        for n in (cut, add):
            if n in cards:
                r, why = repeatable_parse(n, cards[n]["text"], cards[n]["type_line"])
                out["semantics"][n] = {"rule": r, "not_modelable": why}
        for T in TURNS:
            a = repeatable_uses(c, add, ctx, T) if ia else 0.0
            z = repeatable_uses(b, cut, ctx, T) if ic else 0.0
            out["metrics"][str(T)] = {"diff_tutor_uses": round(a - z, 4)}
        return out
