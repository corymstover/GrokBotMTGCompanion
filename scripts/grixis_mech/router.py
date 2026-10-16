"""Router: cut/add Oracle/card features -> mechanic modules.

Step E closure rule (cycle 66.13): broad residual text buckets are *not* promises of future generic simulators.  Death,
sacrifice and token wording that a semantic module deliberately refuses stays explicitly not_modelable and is surfaced
as a residual review family.  Commander-specific hooks likewise route to judgment / Step D rather than being converted
into a generic numerical proxy.  This prevents coverage pressure from becoming false precision.
"""
import re

from . import MODULES

# Stable module-family order.  A key not present in MODULES is a genuinely planned Step-E module; after cycle 66.13
# there are no such keys.  The name PLANNED is retained for compatibility with the build/report code.
PLANNED = {
    "attack_trigger_proxy": None,
    "graveyard_recursion": None,
    "self_recursion": None,
    "graveyard_tutoring": r"(?:search your library|mill|surveil|put [^.]{0,40} into your graveyard)",
    "sacrifice_costs": None,
    "death_triggers": None,
    "cast_triggers": None,
    "activated_engines": None,
    "repeatable_draw": None,
    "token_makers": None,
    "sacrifice_additional_cost": None,
    "repeatable_tutors": r"(?:at the beginning of|whenever|\{T\}[^:]*:)[^.]{0,80}search your library",
    "stax_tax": r"(?:spells? (?:your opponents|each opponent) casts? cost|can't cast|players can't|don't untap|costs? \{\d\} more)",
    "stack_protection": None,
    "counterspell_density": None,
    "opponent_dependent_draw": r"(?:whenever an opponent|each opponent)[^.]{0,80}(?:draw|cards?)",
    "led_breach_sequences": r"(?:Lion's Eye Diamond|Underworld Breach|escape—|discard your hand)",
    "x_spells": None,
    "alternate_costs": None,
    "life_loss": r"(?:loses? \d+ life|lose X life|each opponent loses|damage to each opponent|damage to each player)",
    "discard": r"(?:discards?|discard a card)",
}
RX = {k: re.compile(v, re.I | re.M) for k, v in PLANNED.items() if v}

# Diagnostic residuals: deliberately *not* modeled generically.  A dedicated parser may still route the same card to
# an implemented module; the residual is retained as a warning that other text on the card was not interpreted.
RESIDUAL = {
    "sacrifice_other": r", sacrifice |sacrifice (?:a|an|another|two|X) [^:]{0,40}:|as an additional cost to cast [^,]{0,40}, sacrifice",
    "death_other": r"\bdies\b",
    "tokens_other": r"create (?:a|an|one|two|three|X|\w+) [^.]{0,60}tokens?",
}
RESIDUAL_RX = {k: re.compile(v, re.I | re.M) for k, v in RESIDUAL.items()}
COMMANDER_REVIEW = "commander_specific"


def route(name, text, type_line, hook=None, card=None):
    """[(module_id, implemented)] for one card, in stable order.

    Most modules consume Oracle text/type line. Cost-aware modules may expose matches_card(name, card) and receive
    card-index metadata. Commander-specific hooks are intentionally *not* emitted here; route_swap records them as a
    judgment escalation rather than a planned numerical module.
    """
    t = text.replace(name, "~")
    c = card or {"text": text, "type_line": type_line}
    out = []
    for k in PLANNED:
        if k in MODULES:
            m = MODULES[k]
            hit = m.matches_card(name, c) if callable(getattr(m, "matches_card", None)) else m.matches(name, text, type_line)
        elif k in RX:
            hit = bool(RX[k].search(t))
        else:
            hit = False
        if hit:
            out.append((k, k in MODULES))
    return out


def residual_families(name, text):
    t = text.replace(name, "~")
    return sorted(k for k, rx in RESIDUAL_RX.items() if rx.search(t))


def _specific_not_modelable(name, card):
    """Reasons from implemented parsers that recognized a mechanic but deliberately refused its semantics."""
    out = []
    for k, m in sorted(MODULES.items()):
        f = getattr(m, "reason", None)
        if not callable(f):
            continue
        why = f(name, card["text"], card["type_line"])
        if why:
            out.append(f"{name} / {k}: {why}")
    return out


def route_swap(cut, add, cards, hooks=None):
    hooks = hooks or {}
    r, residual, commander = {}, {}, {}
    for n in (cut, add):
        c = cards.get(n)
        if not c:
            continue
        for k, imp in route(n, c["text"], c["type_line"], hooks.get(n), c):
            r.setdefault(k, {"implemented": imp, "cards": []})["cards"].append(n)
        for k in residual_families(n, c["text"]):
            residual.setdefault(k, []).append(n)
        if hooks.get(n):
            commander[n] = hooks[n]

    impl = sorted(k for k, v in r.items() if v["implemented"])
    planned = sorted(k for k, v in r.items() if not v["implemented"])
    if impl:
        status, reason = "routed", None
    elif planned:
        status, reason = "planned_module", "only genuine planned modules match: " + ", ".join(planned)
    else:
        specific = []
        for n in (cut, add):
            if n in cards:
                specific.extend(_specific_not_modelable(n, cards[n]))
        notes = list(specific)
        if residual:
            notes.append("residual semantics intentionally require judgment/dedicated modeling: " + ", ".join(sorted(residual)))
        if commander:
            notes.append("commander-specific Oracle hook requires Commander-first judgment/Step D: " +
                         ", ".join(f"{n}={commander[n]}" for n in sorted(commander)))
        status = "not_modelable"
        reason = "; ".join(notes) if notes else "no Oracle feature matches an implemented Step-E module"

    return {"modules": impl, "planned": planned,
            "residual": {k: sorted(v) for k, v in sorted(residual.items())},
            "commander_specific": {k: commander[k] for k in sorted(commander)},
            "status": status, "reason": reason}
