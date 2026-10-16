"""Step E Underworld Breach / Lion's Eye Diamond / Brain Freeze startup model (ChatGPT cycle 66.11).

This is a *resource-readiness* module for the canonical LED/Breach/Brain Freeze loop, not a combo-quality verdict and
not a win-rate simulator. Commander Spellbook remains the factual combo source; Step B later evaluates combo quality.
The module asks whether the v1.1 trace has the three pieces in usable zones, enough mana to establish Breach, and the
minimum pre-loop graveyard/hand fuel needed to begin the first sustainable escape cycle.
"""
import re

TURNS = [4, 6, 8, 10]
BREACH = "Underworld Breach"
LED = "Lion's Eye Diamond"
FREEZE = "Brain Freeze"
PIECES = {BREACH, LED, FREEZE}


def role(name, text, type_line):
    t = text.lower()
    if name == BREACH or ("each nonland card in your graveyard has escape" in t and "exile three other cards" in t):
        return "breach"
    if name == LED or ("discard your hand" in t and "sacrifice" in t and "add three mana" in t):
        return "led"
    if name == FREEZE or ("storm" in t and re.search(r"target player mills three cards", t)):
        return "brain_freeze"
    return None


def matches(name, text, type_line):
    return role(name, text, type_line) is not None


def reason(name, text, type_line):
    # This module is intentionally exact/narrow; unrelated escape/storm/discard effects are other families.
    if re.search(r"\b(?:escape|storm|discard your hand)\b", text, re.I) and role(name, text, type_line) is None:
        return "escape/storm/hand-discard card is not one of the modeled LED/Breach/Brain Freeze loop roles"
    return None


def _unspent(s):
    return max(0, (s.get("mana") or 0) - (s.get("spent") or 0))


def _zones(s):
    return {"hand": set(s.get("hand", [])), "battlefield": set(s.get("battlefield", [])),
            "graveyard": set(s.get("graveyard", []))}


def _graveyard_fuel(s):
    # Underworld Breach's escape additional cost exiles three *other cards*; preserve all three loop pieces.
    return sum(1 for n in s.get("graveyard", []) if n not in PIECES)


def _discard_fuel(s, breach_zone, led_zone):
    """Non-piece cards that LED will discard before Brain Freeze is escaped.

    Breach/LED that begin in hand are cast before LED activation and are therefore not discarded. Brain Freeze in
    hand is deliberately discarded so it can be escaped, but as the card being escaped it cannot pay its own exile-3
    cost and therefore does not count as fuel.
    """
    hand = list(s.get("hand", []))
    return sum(1 for n in hand if n not in PIECES)


def startup_state(s):
    """Return structured startup state for one end-of-turn trace snapshot.

    Supported line:
      establish Breach -> cast/escape LED -> activate LED, discarding Brain Freeze if needed -> escape Brain Freeze.

    If LED starts in the graveyard, its first escape must be paid entirely from the pre-existing graveyard, because
    LED's hand discard has not happened yet. After LED activates, non-piece cards discarded from hand become legal
    fuel for Brain Freeze. This distinguishes pre-LED fuel from post-discard fuel instead of requiring all six cards to
    have been in the graveyard already.
    """
    z = _zones(s)
    breach_zone = next((k for k in ("battlefield", "hand") if BREACH in z[k]), None)
    led_zone = next((k for k in ("battlefield", "hand", "graveyard") if LED in z[k]), None)
    freeze_zone = next((k for k in ("hand", "graveyard") if FREEZE in z[k]), None)
    gy_fuel = _graveyard_fuel(s)
    if not (breach_zone and led_zone and freeze_zone):
        return {"ready": False, "reason": "piece_zone", "breach_zone": breach_zone, "led_zone": led_zone,
                "freeze_zone": freeze_zone, "graveyard_fuel": gy_fuel, "discard_fuel": None,
                "brain_freeze_fuel": None, "hand_discard": None}

    # Breach must be established before LED activation. Total mana is an upper-bound proxy; exact red source is Step C.
    if breach_zone == "hand" and _unspent(s) < 2:
        return {"ready": False, "reason": "breach_mana", "breach_zone": breach_zone, "led_zone": led_zone,
                "freeze_zone": freeze_zone, "graveyard_fuel": gy_fuel, "discard_fuel": None,
                "brain_freeze_fuel": None, "hand_discard": None}

    # LED in the graveyard must escape before it can discard the hand, so this first payment cannot use discard fuel.
    spent_for_led = 3 if led_zone == "graveyard" else 0
    if gy_fuel < spent_for_led:
        return {"ready": False, "reason": "led_escape_fuel", "breach_zone": breach_zone, "led_zone": led_zone,
                "freeze_zone": freeze_zone, "graveyard_fuel": gy_fuel, "discard_fuel": 0,
                "brain_freeze_fuel": None, "hand_discard": None}

    discarded_nonpieces = _discard_fuel(s, breach_zone, led_zone)
    post_led_fuel = gy_fuel - spent_for_led + discarded_nonpieces
    if post_led_fuel < 3:
        return {"ready": False, "reason": "brain_freeze_escape_fuel", "breach_zone": breach_zone,
                "led_zone": led_zone, "freeze_zone": freeze_zone, "graveyard_fuel": gy_fuel,
                "discard_fuel": discarded_nonpieces, "brain_freeze_fuel": post_led_fuel, "hand_discard": None}

    # Cast Breach/LED leave the hand before LED activation; Brain Freeze and all other remaining cards are discarded.
    hand_discard = len(z["hand"])
    if breach_zone == "hand":
        hand_discard -= 1
    if led_zone == "hand":
        hand_discard -= 1
    hand_discard = max(0, hand_discard)
    return {"ready": True, "reason": None, "breach_zone": breach_zone, "led_zone": led_zone,
            "freeze_zone": freeze_zone, "graveyard_fuel": gy_fuel, "discard_fuel": discarded_nonpieces,
            "brain_freeze_fuel": post_led_fuel, "hand_discard": hand_discard,
            "fuel_margin": post_led_fuel - 3}


def side(games, T):
    ready, earliest, burdens, margins = 0, [], [], []
    for _, tr in games:
        first = None
        for s in tr:
            if s["turn"] > T:
                break
            st = startup_state(s)
            if st["ready"]:
                first = (s["turn"], st)
                break
        if first:
            ready += 1
            earliest.append(first[0])
            burdens.append(first[1]["hand_discard"])
            margins.append(first[1]["fuel_margin"])
    n = max(1, len(games))
    return {"p_startup_ready": ready / n,
            "mean_earliest_turn_when_ready": (sum(earliest) / len(earliest) if earliest else None),
            "mean_hand_discard_when_ready": (sum(burdens) / len(burdens) if burdens else None),
            "mean_fuel_margin_when_ready": (sum(margins) / len(margins) if margins else None)}


class LEDBreachSequences:
    SPEC = {
        "id": "led_breach_sequences", "version": "1", "family": "LED/Breach resource sequence",
        "evidence_class": "test_result",
        "models": [
            "Underworld Breach + Lion's Eye Diamond + Brain Freeze startup readiness by turn 4/6/8/10",
            "piece-zone requirements, fixed Breach setup mana, ordered LED escape payment, LED hand-discard fuel, Brain Freeze escape fuel, discard burden and remaining fuel margin",
            "LED in graveyard must pay its first exile-three from the pre-existing graveyard; non-piece hand cards become fuel only after LED activation",
        ],
        "does_not_model": [
            "tutor chains into the pieces, protection, stack interaction, graveyard hate, Drannith/Rule-of-Law effects or other stax",
            "exact colored source availability for Breach (Step C mana optimizer handles color); only total unspent mana is checked",
            "nonstandard Breach/LED payoffs, Intuition piles, Grinding Station variants or other Commander Spellbook variants",
            "the probability/value of winning after startup; Step B owns combo quality",
            "multiplayer win rates (never produced)",
        ],
        "assumptions": [
            "standard loop order: establish Breach, cast/escape LED, activate LED and discard hand, escape Brain Freeze",
            "Brain Freeze needs three other cards after LED activation; non-piece cards discarded by LED may pay this first Brain Freeze escape cost",
            "LED needs three pre-existing graveyard cards if it begins in the graveyard, because its discard event occurs only after LED has been escaped and activated",
            "after the first Brain Freeze, storm produces at least two total Brain Freeze copies in the supported line and mills at least six cards, enough raw cards for the next LED+Freeze escape pair",
            "the three loop pieces are preserved and never counted as pre-loop escape fuel",
        ],
        "parameters": {"turns": TURNS, "breach_setup_total_mana": 2, "escape_cards_per_piece": 3},
        "confidence": "moderate",
        "limitations": [
            "Readiness is a necessary resource/zone proxy for this exact line, not a sufficient protected-win claim.",
            "v1.1 does not natively execute the loop; this module only observes whether startup conditions are present.",
            "End-of-turn traces abstract away exact intra-turn mana colors and sequencing details beyond the explicit resource-order rules above.",
        ],
        "metrics": ["startup_ready_by_turn", "earliest_ready_turn", "hand_discard_burden", "escape_fuel_margin"],
        "determinism": "deterministic evaluation of the seeded v1.1 zone/mana trace; no extra rng",
        "test_file": "tests/test_mech_breach_semantics.py",
    }

    @staticmethod
    def matches(name, text, type_line):
        return matches(name, text, type_line)

    @staticmethod
    def reason(name, text, type_line):
        return reason(name, text, type_line)

    @classmethod
    def evaluate(cls, base_games, chal_games, cut, add, cards, ctx):
        out = {"module": cls.SPEC["id"], "version": cls.SPEC["version"], "evidence_class": "test_result", "metrics": {}}
        for T in TURNS:
            a, c = side(chal_games, T), side(base_games, T)
            row = {"add": a, "cut": c, "diff_p_startup_ready": round(a["p_startup_ready"] - c["p_startup_ready"], 4)}
            out["metrics"][str(T)] = row
        return out
