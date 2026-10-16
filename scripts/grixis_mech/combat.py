"""attack_trigger_proxy v2: Oracle-parsed attack-trigger semantics under a bounded declaration/survival proxy.

Supported trigger forms:
  self              "Whenever ~ attacks"
  you_attack        "Whenever you attack" / "Whenever one or more creatures you control attack"
  creature_attacks  "Whenever a creature you control attacks"
  another_attacks   "Whenever another creature you control attacks"

The module counts attack declarations, not combat damage or blocks. Blockers cannot stop an attack trigger that already
triggered during declare attackers, so v1's blocker factor was removed. Unsupported qualifiers (attacks alone, attack a
particular player, intervening-if clauses, creature-type filters, opponent attacks, attack-or-block abilities) are
not_modelable rather than coerced into a generic rule.
"""
import re

from . import semantics

SPEC = {
    "id": "attack_trigger_proxy", "version": "2", "family": "attack/combat triggers", "evidence_class": "test_result",
    "models": [
        "self attack triggers: expected triggers when the card itself can attack",
        "controller attack-event triggers ('whenever you attack' / 'one or more creatures you control attack'): at most one trigger per combat",
        "per-attacker triggers ('a creature you control attacks' / 'another creature you control attacks'): one trigger per qualifying attacker",
        "summoning sickness and haste from the v1.1 zone trace",
        "bounded attack-declaration and creature-survival sensitivity by turns 6/8/10",
    ],
    "does_not_model": [
        "trigger payloads (damage, tokens, cards): counted as triggers only",
        "extra combats, vigilance/tap trade-offs, goad, attack taxes, attack restrictions or politics",
        "which player/battle/planeswalker is attacked",
        "creature-type attack filters, attack-alone/attack-with conditions, intervening-if clauses, attack-or-block abilities",
        "actual blockers or combat damage (blockers occur after attack triggers have triggered)",
        "multiplayer win rates (never produced)",
    ],
    "assumptions": [
        "an otherwise eligible attacker is declared with probability `attack_rate` (deterministic expectation)",
        "a creature that has remained on the battlefield survives each opponent turn cycle with probability `survive`; the proxy resets on re-entry",
        "haste permits attacking on the turn the creature first appears in the end-of-turn zone trace; otherwise it must have been present on the prior turn",
        "for controller attack-event triggers, different other attackers' declaration/survival events are treated as independent; the watcher's own attack is handled without double-counting its survival",
    ],
    "parameters": {"attack_rate": [1.0, 0.75, 0.5], "survive": [1.0, 0.85, 0.7], "turns": [6, 8, 10]},
    "confidence": "low",
    "limitations": [
        "Proxy only: it ranks how often supported attack triggers can happen, not what the trigger is worth.",
        "The end-of-turn trace cannot see mid-turn blink/control changes or whether a creature is tapped before combat.",
        "Opponent behaviour is represented only by declared sensitivity parameters, not simulated players.",
    ],
    "metrics": ["attack_triggers_by_turn", "attack_triggers_by_turn_sensitivity"],
    "determinism": "seeded paired v1.1 games (grixis_sim.seed_for); perturbations are closed-form expectations (no rng)",
    "test_file": "tests/test_mech.py",
}

SELF = re.compile(r"^when(?:ever)? ~ attacks\b", re.I)
YOU = re.compile(r"^whenever you attack\b", re.I)
ONE_OR_MORE = re.compile(r"^whenever one or more creatures you control attack\b", re.I)
A_CREATURE = re.compile(r"^whenever a creature you control attacks\b", re.I)
ANOTHER = re.compile(r"^whenever another creature you control attacks\b", re.I)

UNSUPPORTED = (
    (re.compile(r"\battacks? (?:a|an) (?:player|opponent|battle|planeswalker)\b", re.I),
     "defender-specific attack trigger is not modelled"),
    (re.compile(r"\battacks? alone\b|\battacks? with\b|\battacks? and (?:is|isn't|is not) blocked\b", re.I),
     "conditional attack pattern (alone/with/blocked) is not modelled"),
    (re.compile(r"\battacks? or blocks?\b|\battacks? or becomes blocked\b", re.I),
     "combined attack/block trigger is not modelled"),
)


def parse(name, text, type_line):
    """Return (semantic, reason). semantic is one supported scope or None."""
    t = semantics.clean(name, text)
    reasons = []
    for sent in semantics.sentences(t):
        if not re.search(r"\bwhen(?:ever)?\b[^.]{0,100}\battacks?\b|\bwhenever you attack\b", sent, re.I):
            continue
        if semantics.intervening_if(sent):
            reasons.append("intervening-if attack trigger is not modelled")
            continue
        bad = next((why for rx, why in UNSUPPORTED if rx.search(sent)), None)
        if bad:
            reasons.append(bad)
            continue
        if re.search(r"^whenever (?:an opponent|a player|one or more creatures (?:attack|an opponent controls attacks))", sent, re.I):
            reasons.append("opponent/any-player attack trigger is not modelled")
            continue
        if SELF.search(sent):
            if "Creature" not in type_line:
                reasons.append("self-attack trigger on a noncreature permanent requires animation and is not modelled")
                continue
            return "self", None
        if YOU.search(sent) or ONE_OR_MORE.search(sent):
            return "you_attack", None
        if A_CREATURE.search(sent):
            return "creature_attacks", None
        if ANOTHER.search(sent):
            return "another_attacks", None
        if re.search(r"^whenever [^.]{0,60}creatures?[^.]{0,30} attacks?\b", sent, re.I):
            reasons.append("creature-type/qualified attack trigger is not modelled")
            continue
        reasons.append("unrecognised attack-trigger wording")
    return None, (reasons[0] if reasons else None)


def reason(name, text, type_line):
    return parse(name, text, type_line)[1]


def matches(name, text, type_line):
    return parse(name, text, type_line)[0] is not None


def _haste(name, cards):
    c = cards.get(name)
    if not c:
        return False
    # Conservative: only explicit haste on the card itself. Conditional/granted haste is not inferred.
    return bool(re.search(r"(?:^|[\n,.; ])haste(?:$|[\n,.; ])", c.get("text", ""), re.I))


def _is_creature(name, cards):
    c = cards.get(name)
    return bool(c and "Creature" in c.get("type_line", ""))


def _age_map(trace, cards):
    """Per turn -> {creature: consecutive end-step presences since most recent entry, starting at 0}."""
    out, prev, ages = {}, set(), {}
    for s in trace:
        cur = {n for n in s["battlefield"] if _is_creature(n, cards)}
        nxt = {}
        for n in cur:
            nxt[n] = ages.get(n, -1) + 1 if n in prev else 0
        out[s["turn"]] = nxt
        prev, ages = cur, nxt
    return out


def _watcher_alive(name, s, ages, survive, cards):
    if name not in s["battlefield"]:
        return 0.0
    if _is_creature(name, cards):
        return survive ** ages.get(name, 0)
    return 1.0


def _eligible_attackers(ages, survive, cards):
    """[(name, availability probability)] for creatures that are not summoning-sick."""
    out = []
    for n, age in ages.items():
        if age >= 1 or _haste(n, cards):
            out.append((n, survive ** age))
    return out


def triggers(games, name, semantic, turns, attack_rate, survive, cards):
    tot = 0.0
    for _, tr in games:
        age_by_turn = _age_map(tr, cards)
        for s in tr:
            if s["turn"] > turns:
                break
            ages = age_by_turn.get(s["turn"], {})
            attackers = _eligible_attackers(ages, survive, cards)
            p_w = _watcher_alive(name, s, ages, survive, cards)
            if p_w <= 0:
                continue

            if semantic == "self":
                p_self = next((p for n, p in attackers if n == name), 0.0)
                tot += p_self * attack_rate
                continue

            if semantic == "creature_attacks":
                # If the watcher itself is an eligible attacker, do not multiply its survival twice.
                own = next((p for n, p in attackers if n == name), 0.0)
                others = sum(p for n, p in attackers if n != name)
                tot += own * attack_rate + p_w * others * attack_rate
                continue

            if semantic == "another_attacks":
                tot += p_w * sum(p for n, p in attackers if n != name) * attack_rate
                continue

            # you_attack: at most once per combat. Condition on the watcher being alive.
            own_eligible = any(n == name for n, _ in attackers)
            miss = 1.0 - attack_rate if own_eligible else 1.0
            for n, p in attackers:
                if n != name:
                    miss *= 1.0 - min(1.0, p * attack_rate)
            tot += p_w * (1.0 - miss)
    return tot / max(1, len(games))


def evaluate(base_games, chal_games, cut, add, cards):
    """Paired metric: E[supported attack triggers of add] - E[supported attack triggers of cut]."""
    P = SPEC["parameters"]
    out = {"module": SPEC["id"], "version": SPEC["version"], "evidence_class": "test_result", "semantics": {}, "metrics": {}}

    def one(games, n):
        c = cards.get(n)
        if not c:
            return None
        sem, why = parse(n, c["text"], c["type_line"])
        out["semantics"][n] = {"scope": sem, "not_modelable": why}
        if not sem:
            return None
        return lambda T, a, s: triggers(games, n, sem, T, a, s, cards)

    fa, fc = one(chal_games, add), one(base_games, cut)
    for T in P["turns"]:
        grid = []
        for a in P["attack_rate"]:
            for s in P["survive"]:
                grid.append(round((fa(T, a, s) if fa else 0.0) - (fc(T, a, s) if fc else 0.0), 4))
        out["metrics"][str(T)] = {"diff_nominal": grid[0], "diff_range": [min(grid), max(grid)]}
    return out
