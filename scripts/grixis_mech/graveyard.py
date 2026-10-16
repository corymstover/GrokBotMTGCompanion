"""graveyard_recursion v2: semantic parsing + zone/death-layer liveness for supported recursion effects.

The module measures whether a recursion effect has at least one legal target while the effect itself is available.
It does not pretend every permanent with recursion text can use that text every turn: spell, activated, and ETB
modes are distinguished. Other trigger timings/conditions are not_modelable with a reason.
"""
import re

from . import deaths, semantics

SPEC = {
    "id": "graveyard_recursion", "version": "2", "family": "graveyard recursion", "evidence_class": "test_result",
    "models": [
        "spell recursion: an instant/sorcery in hand while your graveyard contains a supported legal target",
        "activated recursion: a permanent on the battlefield while your graveyard contains a supported legal target",
        "ETB recursion: the permanent's arrival turn while your graveyard contains a supported legal target",
        "supported target classes: any card; single card types; type unions; type intersections such as artifact creature; nonland permanent",
        "P(recursion live by turn 4/6/8), mean legal targets when live, and the shared creature-death sensitivity grid",
    ],
    "does_not_model": [
        "mana, tap, sacrifice, life or other costs of the recursion spell/ability",
        "trigger timings other than ETB (dies, combat damage, upkeep/end step, cast triggers, etc.)",
        "mana-value, color, subtype, legendary/nonlegendary, owner/source-zone or other target qualifiers",
        "opponents' graveyards or choosing opponent-owned cards",
        "the value of the returned card or destination-specific strategic value",
        "graveyard hate from opponents (see stress scenario graveyard_exiled)",
        "multiplayer win rates (never produced)",
    ],
    "assumptions": [
        "a supported target is legal from its card model's card types/permanent flag; nonland permanent excludes lands",
        "spell/activated liveness is potential access only: costs and timing windows are not paid/simulated",
        "ETB liveness uses the end-of-turn trace and therefore assumes a same-turn graveyard target was available when the ETB trigger resolved",
        "no opponent interaction with the graveyard inside this module",
    ],
    "parameters": {"turns": [4, 6, 8], "death_grid": {k: [str(x) for x in v] for k, v in deaths.GRID.items()}},
    "confidence": "low",
    "limitations": [
        "v1.1's native graveyard is thin; the shared death layer only adds creature deaths, not milled/discarded/noncreature permanents.",
        "The zone trace has end-of-turn resolution, so ETB same-turn ordering is approximate.",
    ],
    "metrics": ["recursion_live_by_turn", "legal_targets_when_live", "recursion_live_by_turn_death_grid"],
    "determinism": "seeded paired v1.1 games (grixis_sim.seed_for); shared death layer is closed-form (no extra rng)",
    "test_file": "tests/test_mech.py",
}

RETURN_RX = re.compile(
    r"return\s+(?P<count>up to\s+\w+\s+)?(?:(?:target|another target|each|all)\s+)?"
    r"(?P<desc>[a-z0-9 \-]*?)cards?\s+from your graveyard to\s+"
    r"(?P<dest>the battlefield|your hand)\b",
    re.I,
)
SELF_RX = re.compile(
    r"return ~ from your graveyard|return this card from your graveyard|"
    r"~ from your graveyard to (?:the battlefield|your hand)",
    re.I,
)
KNOWN_TYPES = ("creature", "artifact", "enchantment", "instant", "sorcery", "planeswalker", "land")
UNSUPPORTED_QUALIFIERS = re.compile(
    r"\b(?:mana value|power|toughness|legendary|nonlegendary|historic|multicolored|monocolored|"
    r"red|blue|black|white|green|colorless|owner|owned|put into|died this turn|left your graveyard)\b",
    re.I,
)


def is_self(name, text):
    return bool(SELF_RX.search(semantics.clean(name, text)))


def _target_spec(desc):
    d = " ".join(desc.lower().split()).strip()
    if not d:
        return {"kind": "any", "types": [], "exclude": []}, None
    if UNSUPPORTED_QUALIFIERS.search(d):
        return None, "target has an unsupported qualifier"
    if d == "nonland permanent":
        return {"kind": "permanent", "types": [], "exclude": ["land"]}, None
    if d.startswith("non") and d != "nonland permanent":
        return None, "negative target qualifier other than nonland permanent is not modelled"
    scrub = d
    for w in KNOWN_TYPES + ("permanent",):
        scrub = re.sub(rf"\b{re.escape(w)}\b", " ", scrub)
    scrub = re.sub(r"\b(?:or|and)\b|[,/\-]", " ", scrub)
    if scrub.strip():
        return None, "target has a subtype or other unsupported qualifier"
    if d == "permanent":
        return {"kind": "permanent", "types": [], "exclude": []}, None

    ts = [w for w in KNOWN_TYPES if re.search(rf"\b{w}\b", d)]
    if not ts:
        return None, "target class is not modelled"
    if "or" in d or "/" in d:
        return {"kind": "any_type", "types": ts, "exclude": []}, None
    if len(ts) > 1:
        return {"kind": "all_types", "types": ts, "exclude": []}, None
    return {"kind": "type", "types": ts, "exclude": []}, None


def _mode(sent, type_line, before):
    tl = type_line.lower()
    if "instant" in tl or "sorcery" in tl:
        return "spell", None
    if semantics.intervening_if(sent):
        return None, "intervening-if recursion trigger is not modelled"
    if re.search(r"^when(?:ever)? ~ enters\b", sent, re.I):
        return "etb", None
    if re.search(r"^(?:when|whenever|at the beginning of)\b", sent, re.I):
        return None, "non-ETB triggered recursion timing is not modelled"
    if ":" in before:
        return "activated", None
    return None, "permanent recursion text is neither a supported activated ability nor ETB trigger"


def parse(name, text, type_line):
    """Return (rule, reason). rule = {mode,target,destination} for one supported recursion clause."""
    t = semantics.clean(name, text)
    t = SELF_RX.sub("", t)
    saw = False
    reasons = []
    for sent in semantics.sentences(t):
        for m in RETURN_RX.finditer(sent):
            saw = True
            spec, why = _target_spec(m.group("desc"))
            if not spec:
                reasons.append(why)
                continue
            mode, why = _mode(sent, type_line, sent[:m.start()])
            if not mode:
                reasons.append(why)
                continue
            return {"mode": mode, "target": spec, "destination": m.group("dest").lower()}, None
    if saw:
        return None, (reasons[0] if reasons else "recursion wording is not modelled")
    if re.search(r"\breturn\b[^.]{0,100}\bgraveyard\b", t, re.I):
        return None, "unrecognised graveyard-recursion wording or zone/destination"
    return None, None


def reason(name, text, type_line):
    return parse(name, text, type_line)[1]


def target_kind(text, name=None):
    """Compatibility helper for simple target text; unions return a canonical joined label."""
    n = name or "~"
    rule, _ = parse(n, text, "Sorcery")
    if not rule:
        return None
    spec = rule["target"]
    if spec["kind"] == "any":
        return "card"
    if spec["kind"] == "permanent":
        return "nonland permanent" if spec["exclude"] else "permanent"
    return "_or_".join(spec["types"]) if spec["kind"] == "any_type" else "_and_".join(spec["types"])


def matches(name, text, type_line):
    return parse(name, text, type_line)[0] is not None


def _types(model):
    return {str(x).lower() for x in (model or {}).get("types", [])}


def legal(spec, model):
    if model is None:
        return False
    ts = _types(model)
    if any(x in ts for x in spec.get("exclude", [])):
        return False
    k = spec["kind"]
    if k == "any":
        return True
    if k == "permanent":
        return bool(model.get("permanent", False))
    want = set(spec["types"])
    if k in ("type", "any_type"):
        return bool(want & ts)
    if k == "all_types":
        return want <= ts
    return False


def _compat_rule(kind):
    if kind == "card":
        spec = {"kind": "any", "types": [], "exclude": []}
    elif kind == "permanent":
        spec = {"kind": "permanent", "types": [], "exclude": []}
    elif kind == "nonland permanent":
        spec = {"kind": "permanent", "types": [], "exclude": ["land"]}
    elif "_or_" in kind:
        spec = {"kind": "any_type", "types": kind.split("_or_"), "exclude": []}
    elif "_and_" in kind:
        spec = {"kind": "all_types", "types": kind.split("_and_"), "exclude": []}
    else:
        spec = {"kind": "type", "types": [kind], "exclude": []}
    return {"mode": "compat", "target": spec, "destination": None}


def _available(rule, name, s, prev_bf):
    mode = rule["mode"]
    if mode == "spell":
        return name in s["hand"]
    if mode == "activated":
        return name in s["battlefield"]
    if mode == "etb":
        return name in s["battlefield"] and name not in prev_bf
    return name in s["battlefield"] or name in s["hand"]


def live(games, name, rule, models, T):
    if isinstance(rule, str):
        rule = _compat_rule(rule)
    hits, tg = 0, []
    for _, tr in games:
        prev_bf = set()
        for s in tr:
            if s["turn"] > T:
                break
            if _available(rule, name, s, prev_bf):
                n = sum(1 for g in s["graveyard"] if g != name and legal(rule["target"], models.get(g)))
                if n:
                    hits += 1
                    tg.append(n)
                    break
            prev_bf = set(s["battlefield"])
    return hits / max(1, len(games)), (sum(tg) / len(tg) if tg else 0.0)


def live_under(games, name, rule, models, ctx, T, pt):
    """P(recursion live by T) when the shared death layer also fills the graveyard with dead creatures."""
    if isinstance(rule, str):
        rule = _compat_rule(rule)
    tot = 0.0
    for _, tr in games:
        pr = deaths.profile(tr, ctx["creatures"], ctx["outlets"], ctx["commanders"], set(), *pt)
        best, prev_bf = 0.0, set()
        for s, row in zip(tr, pr):
            if s["turn"] > T:
                break
            if _available(rule, name, s, prev_bf):
                if any(g != name and legal(rule["target"], models.get(g)) for g in s["graveyard"]):
                    best = 1.0
                    break
                miss = 1.0
                for m, a in row["alive"].items():
                    if m != name and m not in ctx["commanders"] and legal(rule["target"], models.get(m)):
                        miss *= a
                best = max(best, 1.0 - miss)
            prev_bf = set(s["battlefield"])
        tot += best
    return tot / max(1, len(games))


def _rule_for(n, cards):
    c = cards.get(n)
    return parse(n, c["text"], c["type_line"])[0] if c else None


def evaluate_grid(base_games, chal_games, cut, add, cards, models, ctx):
    out = {"module": SPEC["id"], "version": SPEC["version"], "evidence_class": "test_result", "layer": "deaths",
           "semantics": {}, "metrics": {}}
    rules = {n: _rule_for(n, cards) for n in (cut, add)}
    out["semantics"] = {n: rules[n] for n in (cut, add)}
    for T in SPEC["parameters"]["turns"]:
        grid = {}
        for pt in deaths.points():
            v = []
            for games, n in ((chal_games, add), (base_games, cut)):
                r = rules[n]
                v.append(live_under(games, n, r, models, ctx, T, pt) if r else 0.0)
            grid[pt] = round(v[0] - v[1], 4)
        out["metrics"][str(T)] = {"diff_lower_bound": grid[deaths.LOWER_BOUND], "diff_range": [min(grid.values()), max(grid.values())],
                                  "diff_mid": grid[(0.1, None, True)]}
    return out


def evaluate(base_games, chal_games, cut, add, cards, models):
    out = {"module": SPEC["id"], "version": SPEC["version"], "evidence_class": "test_result", "semantics": {}, "metrics": {}}
    rules = {n: _rule_for(n, cards) for n in (cut, add)}
    out["semantics"] = {n: rules[n] for n in (cut, add)}
    for T in SPEC["parameters"]["turns"]:
        row = {}
        for side, games, n in (("add", chal_games, add), ("cut", base_games, cut)):
            r = rules[n]
            row[side] = None if r is None else dict(zip(("p_live", "targets_when_live"),
                                                        [round(x, 4) for x in live(games, n, r, models, T)]))
        a = row["add"]["p_live"] if row["add"] else 0.0
        c = row["cut"]["p_live"] if row["cut"] else 0.0
        row["diff_p_live"] = round(a - c, 4)
        out["metrics"][str(T)] = row
    return out
