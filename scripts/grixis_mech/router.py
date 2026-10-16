"""Router: cut/add Oracle/card features -> mechanic modules (implemented or planned). Unmatched stays not_modelable."""
import re

from . import MODULES

PLANNED = {  # step E family -> Oracle feature regex (module ids not in MODULES are planned for later 66.x batches)
    "attack_trigger_proxy": None,
    "graveyard_recursion": None,
    "self_recursion": None,
    "graveyard_tutoring": r"(?:search your library|mill|surveil|put [^.]{0,40} into your graveyard)",
    "sacrifice_costs": None,
    "death_triggers": None,
    "sacrifice_other": r", sacrifice |sacrifice (?:a|an|another|two|X) [^:]{0,40}:|as an additional cost to cast [^,]{0,40}, sacrifice",
    "death_other": r"\bdies\b",
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
    "commander_specific": None,
    "tokens_other": r"create (?:a|an|one|two|three|X|\w+) [^.]{0,60}tokens?",
    "life_loss": r"(?:loses? \d+ life|lose X life|each opponent loses)",
    "discard": r"(?:discards?|discard a card)",
}
RX = {k: re.compile(v, re.I | re.M) for k, v in PLANNED.items() if v}


def route(name, text, type_line, hook=None, card=None):
    """[(module_id, implemented)] for one card, in stable order.

    Most modules consume Oracle text/type line. Cost-aware modules may expose matches_card(name, card) and receive
    the card-index metadata (currently mana_cost in addition to text/type_line).
    """
    t = text.replace(name, "~")
    c = card or {"text": text, "type_line": type_line}
    out = []
    for k in PLANNED:
        if k in MODULES:
            m = MODULES[k]
            hit = m.matches_card(name, c) if callable(getattr(m, "matches_card", None)) else m.matches(name, text, type_line)
        elif k == "commander_specific":
            hit = bool(hook)
        elif k in RX:
            hit = bool(RX[k].search(t))
        else:
            hit = False
        if hit:
            out.append((k, k in MODULES))
    return out


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
    r = {}
    for n in (cut, add):
        c = cards.get(n)
        if c:
            for k, imp in route(n, c["text"], c["type_line"], hooks.get(n), c):
                r.setdefault(k, {"implemented": imp, "cards": []})["cards"].append(n)
    impl = sorted(k for k, v in r.items() if v["implemented"])
    if impl:
        status, reason = "routed", None
    elif r:
        status, reason = "planned_module", "only planned modules match: " + ", ".join(sorted(r))
    else:
        specific = []
        for n in (cut, add):
            if n in cards:
                specific.extend(_specific_not_modelable(n, cards[n]))
        status = "not_modelable"
        reason = "; ".join(specific) if specific else "no Oracle feature matches any step-E module family"
    return {"modules": impl, "planned": sorted(k for k, v in r.items() if not v["implemented"]),
            "status": status, "reason": reason}
