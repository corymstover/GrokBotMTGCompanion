"""attack_trigger_proxy: a creature with an attack trigger attacks every turn from the first turn it could."""
import re

SPEC = {
    "id": "attack_trigger_proxy", "version": "1", "family": "attack/combat triggers", "evidence_class": "test_result",
    "models": ["turn a creature with a 'whenever ~ attacks' / 'whenever you attack' trigger is on your battlefield (zone trace)",
               "summoning sickness (haste attacks the turn it lands)",
               "expected attack-trigger count by turns 6/8/10 under a bounded blocker/removal perturbation grid"],
    "does_not_model": ["trigger payloads (damage, tokens, cards): counted as triggers only", "actual opponents, blockers, "
                       "combat math or politics", "attack restrictions, tapping for other costs, vigilance trade-offs",
                       "multiplayer win rates (never produced)"],
    "assumptions": ["the creature attacks every turn it is untapped and not summoning-sick",
                    "blocker perturbation: each attack's trigger is lost with probability `block` (deterministic expectation)",
                    "removal perturbation: the creature survives each opponent turn cycle with probability `survive`, "
                    "compounded from the turn it lands (deterministic expectation)"],
    "parameters": {"block": [0.0, 0.25, 0.5], "survive": [1.0, 0.85, 0.7], "turns": [6, 8, 10]},
    "confidence": "low", "limitations": ["Proxy only: ranks how often a trigger can happen, not what it is worth.",
                                         "Opponent behaviour is a fixed perturbation grid, reported as a sensitivity range."],
    "metrics": ["attack_triggers_by_turn", "attack_triggers_by_turn_sensitivity"],
    "determinism": "seeded paired v1.1 games (grixis_sim.seed_for); perturbations are closed-form expectations (no rng)",
    "test_file": "tests/test_mech.py",
}
RX = re.compile(r"whenever (?:~|this creature|[^.,]{0,40}?) attacks|whenever you attack|attacks each combat|"
                r"whenever one or more (?:creatures you control|[^.,]{0,30}) attack", re.I)


def matches(name, text, type_line):
    return "Creature" in type_line and bool(RX.search(text.replace(name, "~")))


def triggers(games, name, haste, turns, block, survive):
    tot = 0.0
    for _, tr in games:
        land = next((s["turn"] for s in tr if name in s["battlefield"]), None)
        if land is None:
            continue
        for t in range(land if haste else land + 1, turns + 1):
            tot += (1 - block) * survive ** (t - land)
    return tot / max(1, len(games))


def evaluate(base_games, chal_games, cut, add, cards):
    """Paired metric: E[triggers of add in challenger games] - E[triggers of cut in baseline games]."""
    P = SPEC["parameters"]
    out = {"module": SPEC["id"], "evidence_class": "test_result", "metrics": {}}

    def one(games, n):
        c = cards.get(n)
        if not c or not matches(n, c["text"], c["type_line"]):
            return None
        return lambda T, b, s: triggers(games, n, "haste" in c["text"].lower(), T, b, s)
    fa, fc = one(chal_games, add), one(base_games, cut)
    for T in P["turns"]:
        grid = []
        for b in P["block"]:
            for s in P["survive"]:
                grid.append(round((fa(T, b, s) if fa else 0.0) - (fc(T, b, s) if fc else 0.0), 4))
        out["metrics"][str(T)] = {"diff_nominal": grid[0], "diff_range": [min(grid), max(grid)]}
    return out
