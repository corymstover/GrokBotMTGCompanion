"""Step E stax/tax availability and bounded friction metrics (ChatGPT cycle 66.10).

This module never turns unlike effects into one 'stax score'. It parses a narrow set of static restrictions/taxes and
reports category-specific opportunity/friction ranges under declared opponent-activity assumptions. Symmetric effects
carry an explicit self_burden flag rather than being scored as pure upside.
"""
import re

from . import semantics

TURNS = [4, 6, 8, 10]
OPPONENTS = 3
SPELLS = (1.0, 2.0, 3.0)
NONCREATURE_SHARE = (0.5, 0.7, 0.9)
DRAWS = (1.0, 2.0, 3.0)

COST_MORE = re.compile(
    r"(?P<scope>noncreature )?spells (?P<who>your opponents|opponents|players)? ?cast cost (?P<cost>(?:\{[^}]+\})+) more to cast",
    re.I,
)
CAP_CAST = re.compile(r"(?P<who>each opponent|your opponents|each player|players) can(?:'|’)t cast more than (?P<n>one|two|\d+) spells? each turn", re.I)
CAP_DRAW = re.compile(r"(?P<who>each opponent|your opponents|each player|players) can(?:'|’)t draw more than (?P<n>one|two|\d+) cards? each turn", re.I)
NO_SEARCH = re.compile(r"(?P<who>your opponents|opponents|players) can(?:'|’)t search librar(?:y|ies)", re.I)
NO_CAST_YOUR_TURN = re.compile(r"your opponents can(?:'|’)t cast spells during your turn", re.I)
ARTIFACTS_ETB_TAPPED = re.compile(r"artifacts your opponents control enter (?:the battlefield )?tapped", re.I)
ACTIVATED_LOCK = re.compile(r"activated abilities of (?P<kind>artifacts|creatures) can(?:'|’)t be activated", re.I)
UNTAP_CAP = re.compile(r"players can(?:'|’)t untap more than (?P<n>one|two|\d+) (?P<kind>artifacts?|permanents?) during their untap steps", re.I)
GY_CAST_LOCK = re.compile(r"players can(?:'|’)t cast spells from graveyards", re.I)
ETB_TRIGGER_LOCK = re.compile(r"creatures entering (?:the battlefield )?don(?:'|’)t cause abilities to trigger", re.I)

NUM = {"one": 1, "two": 2}


def _n(s):
    s = s.lower()
    return int(s) if s.isdigit() else NUM[s]


def _mana(cost):
    total = 0
    for p in re.findall(r"\{([^}]+)\}", cost):
        if p.isdigit():
            total += int(p)
        elif p.upper() in ("X", "Y", "Z"):
            return None
        else:
            total += 1
    return total


def parse(name, text, type_line):
    if "Instant" in type_line or "Sorcery" in type_line:
        return None, None
    t = semantics.clean(name, text)
    rules, reasons = [], []
    for sent in semantics.sentences(t):
        m = COST_MORE.search(sent)
        if m:
            mana = _mana(m.group("cost"))
            if mana is None:
                reasons.append("variable spell tax is not modelled")
            else:
                who = (m.group("who") or "players").lower()
                rules.append({"kind": "spell_tax", "scope": "noncreature" if m.group("scope") else "any",
                              "amount": mana, "self_burden": "player" in who and "opponent" not in who})
            continue
        m = CAP_CAST.search(sent)
        if m:
            who = m.group("who").lower()
            rules.append({"kind": "cast_cap", "cap": _n(m.group("n")),
                          "self_burden": "player" in who and "opponent" not in who})
            continue
        m = CAP_DRAW.search(sent)
        if m:
            who = m.group("who").lower()
            rules.append({"kind": "draw_cap", "cap": _n(m.group("n")),
                          "self_burden": "player" in who and "opponent" not in who})
            continue
        m = NO_SEARCH.search(sent)
        if m:
            who = m.group("who").lower()
            rules.append({"kind": "search_lock", "self_burden": who == "players"})
            continue
        if NO_CAST_YOUR_TURN.search(sent):
            rules.append({"kind": "your_turn_cast_lock", "self_burden": False})
            continue
        if ARTIFACTS_ETB_TAPPED.search(sent):
            rules.append({"kind": "opponent_artifact_etb_tapped", "self_burden": False})
            continue
        m = ACTIVATED_LOCK.search(sent)
        if m:
            rules.append({"kind": "activated_lock", "scope": m.group("kind").lower(), "self_burden": True})
            continue
        m = UNTAP_CAP.search(sent)
        if m:
            rules.append({"kind": "untap_cap", "scope": m.group("kind").lower(), "cap": _n(m.group("n")), "self_burden": True})
            continue
        if GY_CAST_LOCK.search(sent):
            rules.append({"kind": "graveyard_cast_lock", "self_burden": True})
            continue
        if ETB_TRIGGER_LOCK.search(sent):
            rules.append({"kind": "creature_etb_trigger_lock", "self_burden": True})
            continue
        if re.search(r"\b(?:cost .* more|can't cast|can’t cast|can't draw|can’t draw|can't search|can’t search|don't untap|"
                     r"can’t untap|can't be activated|can’t be activated|enter(?:s)? tapped)\b", sent, re.I):
            reasons.append("stax/tax wording outside the supported static families")
    if rules:
        return rules, None
    return None, (reasons[0] if reasons else None)


def reason(name, text, type_line):
    return parse(name, text, type_line)[1]


def matches(name, text, type_line):
    return parse(name, text, type_line)[0] is not None


def _active_rounds(games, n, T):
    vals = []
    for _, tr in games:
        vals.append(sum(1 for s in tr if s["turn"] <= T and n in s.get("battlefield", [])))
    return sum(vals) / max(1, len(vals))


def metrics(games, n, rules, T, spells, noncreature_share, draws):
    rounds = _active_rounds(games, n, T)
    out = {"active_rounds": rounds, "opponent_extra_mana": 0.0, "opponent_spells_blocked": 0.0,
           "opponent_draws_blocked": 0.0, "static_lock_rounds": 0.0,
           "self_burden": any(r.get("self_burden") for r in rules),
           "kinds": sorted({r["kind"] for r in rules})}
    for r in rules:
        k = r["kind"]
        if k == "spell_tax":
            events = OPPONENTS * spells * (noncreature_share if r["scope"] == "noncreature" else 1.0)
            out["opponent_extra_mana"] += rounds * events * r["amount"]
        elif k == "cast_cap":
            out["opponent_spells_blocked"] += rounds * OPPONENTS * max(0.0, spells - r["cap"])
        elif k == "draw_cap":
            out["opponent_draws_blocked"] += rounds * OPPONENTS * max(0.0, draws - r["cap"])
        else:
            out["static_lock_rounds"] += rounds
    return out


def points():
    return [(s, n, d) for s in SPELLS for n in NONCREATURE_SHARE for d in DRAWS]


class StaxTax:
    SPEC = {
        "id": "stax_tax", "version": "1", "family": "stax/tax static effects", "evidence_class": "test_result",
        "models": [
            "fixed spell taxes on opponents or all players: opponent extra-mana demand range",
            "cast-per-turn caps: opponent spells blocked range under declared spell-volume sensitivity",
            "draw-per-turn caps: opponent draws blocked range under declared draw-volume sensitivity",
            "supported static locks (search, cast-during-your-turn, artifact ETB tapped, activated-ability, untap, graveyard-cast, creature-ETB-trigger): active rounds only",
            "symmetric effects retain an explicit self_burden flag; no composite score hides that cost",
        ],
        "does_not_model": [
            "whether opponents can/will pay taxes, exact opponent mana curves, or which spells are most important",
            "Trinisphere-style minimum total costs, dynamic per-spell taxes, type/color/subtype-specific locks outside supported families",
            "resource denial, mana-base conversion, combat restrictions, graveyard replacement effects, or removal timing",
            "a universal conversion between tax mana, blocked spells, blocked draws and static-lock uptime",
            "multiplayer win rates (never produced)",
        ],
        "assumptions": [
            "three opponents; opponent spells per turn is swept over 1/2/3, noncreature share over 0.5/0.7/0.9, opponent cards drawn per turn over 1/2/3",
            "if the permanent is present at your end step, its static text applies through the following opponent turn cycle",
            "spell-tax mana is friction demanded, not mana actually paid; cap metrics are upper-bound prevented-event counts given the declared activity point",
        ],
        "parameters": {"turns": TURNS, "opponents": OPPONENTS, "opponent_spells_per_turn": list(SPELLS),
                       "noncreature_share": list(NONCREATURE_SHARE), "opponent_cards_drawn_per_turn": list(DRAWS)},
        "confidence": "low",
        "limitations": [
            "Category metrics are intentionally not summed. M6 judgment must consider self-burden, asymmetry and commander-specific leverage.",
            "Static-lock active rounds measure availability only; opponent dependence is handled later by bracket stress/red-team review.",
        ],
        "metrics": ["opponent_extra_mana_range", "opponent_spells_blocked_range", "opponent_draws_blocked_range",
                    "static_lock_active_rounds", "self_burden"],
        "determinism": "seeded paired v1.1 battlefield trace plus closed-form declared opponent-activity grid",
        "test_file": "tests/test_mech_stax_semantics.py",
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
            rows = []
            for s, n, d in points():
                a = metrics(chal_games, add, ra, T, s, n, d) if ra else {"opponent_extra_mana": 0.0, "opponent_spells_blocked": 0.0,
                                                                         "opponent_draws_blocked": 0.0, "static_lock_rounds": 0.0,
                                                                         "self_burden": False, "kinds": []}
                c = metrics(base_games, cut, rc, T, s, n, d) if rc else {"opponent_extra_mana": 0.0, "opponent_spells_blocked": 0.0,
                                                                        "opponent_draws_blocked": 0.0, "static_lock_rounds": 0.0,
                                                                        "self_burden": False, "kinds": []}
                rows.append({k: a[k] - c[k] for k in ("opponent_extra_mana", "opponent_spells_blocked", "opponent_draws_blocked", "static_lock_rounds")})
            out["metrics"][str(T)] = {
                "diff_opponent_extra_mana_range": [round(min(r["opponent_extra_mana"] for r in rows), 4), round(max(r["opponent_extra_mana"] for r in rows), 4)],
                "diff_opponent_spells_blocked_range": [round(min(r["opponent_spells_blocked"] for r in rows), 4), round(max(r["opponent_spells_blocked"] for r in rows), 4)],
                "diff_opponent_draws_blocked_range": [round(min(r["opponent_draws_blocked"] for r in rows), 4), round(max(r["opponent_draws_blocked"] for r in rows), 4)],
                "diff_static_lock_rounds": round(rows[0]["static_lock_rounds"], 4),
                "add_self_burden": any(r.get("self_burden") for r in (ra or [])),
                "cut_self_burden": any(r.get("self_burden") for r in (rc or [])),
            }
        return out
