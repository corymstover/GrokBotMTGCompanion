"""Step E stack/defense modules (ChatGPT cycle 66.6).

Counterspells and direct protection are modeled as *availability/readiness* from the v1.1 end-of-turn trace, not as
opponent simulation. A card in hand is paid at its normal mana value from mana left unspent after v1.1's own turn;
explicit commander-free counter text is also recognized. Permanent protection is counted only while the permanent is
on the battlefield. The modules never infer that a ready answer had a legal/valuable opponent target.
"""
import re

from . import semantics

TURNS = [4, 6, 8, 10]


def _spec(id_, family, models, does_not, assumptions, limits, metrics):
    return {"id": id_, "version": "1", "family": family, "evidence_class": "test_result",
            "models": models, "does_not_model": does_not + ["multiplayer win rates (never produced)"],
            "assumptions": assumptions, "parameters": {"turns": TURNS}, "confidence": "low",
            "limitations": limits, "metrics": metrics,
            "determinism": "seeded paired v1.1 games; readiness is a deterministic function of the zone/mana trace",
            "test_file": "tests/test_mech_stack_semantics.py"}


def _unspent(s):
    return max(0, (s.get("mana") or 0) - (s.get("spent") or 0))


def _normal_need(n, ctx):
    return int((ctx.get("models", {}).get(n) or {}).get("mv") or 0)


def _commander_present(s, ctx):
    cs = set(ctx.get("commanders") or ())
    return any(n in cs for n in s.get("battlefield", []))


# ---------------------------------------------------------------- counterspells
SOFT = re.compile(r"counter target [^.]+? unless (?:its controller|that spell's controller|that player) pays", re.I)
COUNTER = re.compile(r"counter target (?P<what>[^.]+?)(?:\.|$)", re.I)
FREE_COMMANDER = re.compile(r"if you control a commander, you may cast (?:~|this spell) without paying its mana cost", re.I)


def counter_parse(name, text, type_line):
    """(rule, reason). rule: {mode, scope, normal_cost_only}."""
    t = semantics.clean(name, text)
    why = None
    for sent in semantics.sentences(t):
        if "counter target" not in sent.lower():
            continue
        if SOFT.search(sent):
            why = "soft counter ('unless ... pays') needs an opponent-mana model"
            continue
        if semantics.intervening_if(sent):
            why = "conditional counter effect is not modelled"
            continue
        m = COUNTER.search(sent)
        if not m:
            why = "unrecognised counter wording"
            continue
        w = m.group("what").lower().strip()
        if re.search(r"\b(?:spell|activated ability|triggered ability)\b", w) is None:
            why = "counter effect does not target a spell/ability"
            continue
        if re.search(r"\b(?:with mana value|unless|if|that targets|you don't control|an opponent controls|controller)\b", w):
            why = "qualified counter target is not modelled"
            continue
        scopes = []
        if "spell" in w:
            if "noncreature" in w:
                scopes.append("noncreature_spell")
            elif "creature" in w:
                scopes.append("creature_spell")
            elif re.search(r"instant or sorcery|instant/sorcery", w):
                scopes.append("instant_or_sorcery_spell")
            else:
                scopes.append("spell")
        if "activated ability" in w:
            scopes.append("activated_ability")
        if "triggered ability" in w:
            scopes.append("triggered_ability")
        mode = "spell" if ("Instant" in type_line or "Sorcery" in type_line) else None
        if mode is None:
            # Only support a clearly activated counter ability on a permanent. Triggered counter text is not optional/readiness.
            before = sent[:m.start()]
            if ":" in before:
                mode = "activated"
            else:
                why = "counter text on a permanent is not a supported activated ability"
                continue
        return {"mode": mode, "scope": tuple(scopes),
                "free_with_commander": bool(FREE_COMMANDER.search(t))}, None
    return None, why


def counter_reason(name, text, type_line):
    return counter_parse(name, text, type_line)[1]


def counter_ready(games, n, ctx, T, _pt=None):
    rule, _ = counter_parse(n, ctx["cards"][n]["text"], ctx["cards"][n]["type_line"])
    if not rule:
        return 0.0
    need = _normal_need(n, ctx)
    tot = 0.0
    for _, tr in games:
        live = 0
        for s in tr:
            if s["turn"] > T:
                break
            if rule["mode"] == "spell":
                ready = n in s.get("hand", []) and (_unspent(s) >= need or (rule["free_with_commander"] and _commander_present(s, ctx)))
            else:
                # Mana cost of activated counter abilities is not reconstructed here; report battlefield availability only.
                ready = n in s.get("battlefield", [])
            live += 1 if ready else 0
        tot += live
    return tot / max(1, len(games))


class Counterspells:
    SPEC = _spec("counterspell_density", "counterspell readiness",
                 ["turns by 4/6/8/10 on which a supported counterspell is in hand and normal-cost mana remains unspent",
                  "Fierce-Guardianship-style explicit 'control a commander -> cast without paying' readiness",
                  "supported activated counter abilities: battlefield-available turns (cost not reconstructed)"],
                 ["whether an opponent actually casts a legal/important target", "soft counters ('unless ... pays')",
                  "conditional target qualifiers", "Force-of-Will-style pitch/resource alternate costs", "colored-mana hold-up",
                  "activation costs for permanent counter abilities"],
                 ["end-of-own-turn unspent mana is a proxy for mana held through the following opponent turn cycle",
                  "normal spell cost uses mana value rather than exact colored pips, so readiness is an upper bound when colors are constrained",
                  "readiness is opportunity count, not number of counters actually cast"],
                 ["Does not evaluate counterspell quality, target breadth or opponent pressure; scope is reported but not weighted."],
                 ["counter_ready_turns_by_turn"])

    @staticmethod
    def matches(name, text, type_line):
        return counter_parse(name, text, type_line)[0] is not None

    @staticmethod
    def reason(name, text, type_line):
        return counter_reason(name, text, type_line)

    @classmethod
    def evaluate(cls, b, c, cut, add, cards, ctx):
        ia = add in cards and cls.matches(add, cards[add]["text"], cards[add]["type_line"])
        ic = cut in cards and cls.matches(cut, cards[cut]["text"], cards[cut]["type_line"])
        out = {"module": cls.SPEC["id"], "version": cls.SPEC["version"], "evidence_class": "test_result",
               "semantics": {}, "metrics": {}}
        for n in (cut, add):
            if n in cards:
                r, why = counter_parse(n, cards[n]["text"], cards[n]["type_line"])
                out["semantics"][n] = {"rule": r, "not_modelable": why}
        for T in TURNS:
            av = counter_ready(c, add, ctx, T) if ia else 0.0
            cv = counter_ready(b, cut, ctx, T) if ic else 0.0
            out["metrics"][str(T)] = {"diff_ready_turns": round(av - cv, 4)}
        return out


# ---------------------------------------------------------------- protection
REACTIVE = re.compile(
    r"(?:target|up to (?:one|two) target) [^.]{0,50}? (?:you control )?(?:gains?|gain) "
    r"(?P<kw>hexproof|indestructible)(?: until end of turn)?|"
    r"(?P<phase>(?:target|up to (?:one|two) target) [^.]{0,50}? phases? out)", re.I)
STATIC_TEAM = re.compile(r"(?:spells you control can't be countered|other [^.]{0,40}? you control (?:have|has) (?:hexproof|ward|indestructible))", re.I)
SELF_STATIC = re.compile(r"(?:^|\n)(?:hexproof|indestructible|ward(?:\s|—|-|$)|this spell can't be countered)\b", re.I)


def protection_parse(name, text, type_line):
    t = semantics.clean(name, text)
    why = None
    for sent in semantics.sentences(t):
        if semantics.intervening_if(sent) and re.search(r"hexproof|indestructible|phase", sent, re.I):
            why = "conditional protection effect is not modelled"
            continue
        if REACTIVE.search(sent):
            if "Instant" not in type_line and "Sorcery" not in type_line:
                before = sent[:REACTIVE.search(sent).start()]
                if ":" not in before:
                    why = "reactive protection on a permanent is not a supported activated ability"
                    continue
                return {"mode": "activated", "scope": "target"}, None
            return {"mode": "spell", "scope": "target"}, None
        if STATIC_TEAM.search(sent):
            return {"mode": "static_team", "scope": "team"}, None
        if SELF_STATIC.search(sent):
            return {"mode": "static_self", "scope": "self"}, None
        if re.search(r"\b(?:hexproof|indestructible|ward|phases? out|can't be countered)\b", sent, re.I):
            why = "qualified/other protection wording is not modelled"
    return None, why


def protection_reason(name, text, type_line):
    return protection_parse(name, text, type_line)[1]


def protection_ready(games, n, ctx, T, _pt=None):
    rule, _ = protection_parse(n, ctx["cards"][n]["text"], ctx["cards"][n]["type_line"])
    if not rule:
        return 0.0
    need = _normal_need(n, ctx)
    tot = 0.0
    for _, tr in games:
        live = 0
        for s in tr:
            if s["turn"] > T:
                break
            if rule["mode"] == "spell":
                ready = n in s.get("hand", []) and _unspent(s) >= need
            else:
                ready = n in s.get("battlefield", [])
            live += 1 if ready else 0
        tot += live
    return tot / max(1, len(games))


class StackProtection:
    SPEC = _spec("stack_protection", "protection availability",
                 ["supported reactive protection spells: turns in hand with normal-cost mana left unspent",
                  "supported activated/static team/self protection permanents: battlefield-active turns",
                  "direct hexproof/indestructible/phase-out protection and explicit 'spells you control can't be countered'"],
                 ["whether protection has a valuable legal target", "colored mana", "ward cost/effect magnitude", "conditional protection",
                  "redirects/copies, bounce-as-protection, prevention, regeneration, protection-from-color, Teferi-style timing locks"],
                 ["normal spell cost uses mana value rather than exact colored pips",
                  "active-turn/readiness counts are opportunities, not uses or prevented interactions"],
                 ["Protection modes differ materially; this module reports availability only and does not claim a universal value conversion."],
                 ["protection_ready_or_active_turns_by_turn"])

    @staticmethod
    def matches(name, text, type_line):
        return protection_parse(name, text, type_line)[0] is not None

    @staticmethod
    def reason(name, text, type_line):
        return protection_reason(name, text, type_line)

    @classmethod
    def evaluate(cls, b, c, cut, add, cards, ctx):
        ia = add in cards and cls.matches(add, cards[add]["text"], cards[add]["type_line"])
        ic = cut in cards and cls.matches(cut, cards[cut]["text"], cards[cut]["type_line"])
        out = {"module": cls.SPEC["id"], "version": cls.SPEC["version"], "evidence_class": "test_result",
               "semantics": {}, "metrics": {}}
        for n in (cut, add):
            if n in cards:
                r, why = protection_parse(n, cards[n]["text"], cards[n]["type_line"])
                out["semantics"][n] = {"rule": r, "not_modelable": why}
        for T in TURNS:
            av = protection_ready(c, add, ctx, T) if ia else 0.0
            cv = protection_ready(b, cut, ctx, T) if ic else 0.0
            out["metrics"][str(T)] = {"diff_ready_or_active_turns": round(av - cv, 4)}
        return out
