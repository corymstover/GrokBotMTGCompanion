"""Router: cut/add Oracle features -> mechanic modules (implemented or planned). Unmatched stays not_modelable."""
import re

from . import MODULES

PLANNED = {  # step E family -> Oracle feature regex (module ids not in MODULES are planned for later 66.x batches)
    "attack_trigger_proxy": None,  # uses the module's own matcher
    "graveyard_recursion": None,
    "graveyard_tutoring": r"(?:search your library|mill|surveil|put [^.]{0,40} into your graveyard)",
    "sacrifice_costs": r"sacrifice (?:a|an|another|two|X) [^:]{0,40}:|, sacrifice ",
    "death_triggers": r"whenever [^.]{0,60}\bdies\b|when [^.]{0,30} dies",
    "cast_triggers": r"whenever you cast",
    "activated_engines": r"\{T\}(?:, [^:]{0,40})?: (?!add )|^\{[^}]+\}(?:\{[^}]+\})*: ",
    "repeatable_draw": r"(?:at the beginning of|whenever)[^.]{0,80}draw (?:a|one|two|\w+) cards?",
    "repeatable_tutors": r"(?:at the beginning of|whenever|\{T\}[^:]*:)[^.]{0,80}search your library",
    "stax_tax": r"(?:spells? (?:your opponents|each opponent) casts? cost|can't cast|players can't|don't untap|costs? \{\d\} more)",
    "stack_protection": r"(?:can't be countered|hexproof|indestructible|phase out|ward)",
    "counterspell_density": r"counter target",
    "opponent_dependent_draw": r"(?:whenever an opponent|each opponent)[^.]{0,80}(?:draw|cards?)",
    "led_breach_sequences": r"(?:Lion's Eye Diamond|Underworld Breach|escape—|discard your hand)",
    "x_spells": r"\{X\}",
    "alternate_costs": r"(?:rather than pay|without paying its mana cost|you may pay [^.]{0,30} rather|evoke|flash ?back|delve|convoke)",
    "commander_specific": None,  # matched against the commander's own hook (grixis_refine HOOKS) by the caller
    "tokens": r"create (?:a|an|one|two|three|X|\w+) [^.]{0,60}tokens?",
    "life_loss": r"(?:loses? \d+ life|lose X life|each opponent loses)",
    "discard": r"(?:discards?|discard a card)",
}
RX = {k: re.compile(v, re.I | re.M) for k, v in PLANNED.items() if v}


def route(name, text, type_line, hook=None):
    """[(module_id, implemented)] for one card, in stable order."""
    t = text.replace(name, "~")
    out = []
    for k in PLANNED:
        if k in MODULES:
            hit = MODULES[k].matches(name, text, type_line)
        elif k == "commander_specific":
            hit = bool(hook)
        else:
            hit = bool(RX[k].search(t))
        if hit:
            out.append((k, k in MODULES))
    return out


def route_swap(cut, add, cards, hooks=None):
    hooks = hooks or {}
    r = {}
    for n in (cut, add):
        c = cards.get(n)
        if c:
            for k, imp in route(n, c["text"], c["type_line"], hooks.get(n)):
                r.setdefault(k, {"implemented": imp, "cards": []})["cards"].append(n)
    impl = sorted(k for k, v in r.items() if v["implemented"])
    return {"modules": impl, "planned": sorted(k for k, v in r.items() if not v["implemented"]),
            "status": "routed" if impl else ("planned_module" if r else "not_modelable"),
            "reason": None if impl else ("only planned modules match: " + ", ".join(sorted(r)) if r else "no Oracle feature matches any step-E module family")}
