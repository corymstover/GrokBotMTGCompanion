"""Step E Underworld Breach / Lion's Eye Diamond / Brain Freeze startup model (ChatGPT cycle 66.11).

This is a *resource-readiness* module for the canonical LED/Breach/Brain Freeze loop, not a combo-quality verdict and
not a win-rate simulator. Commander Spellbook remains the factual combo source; Step B later evaluates combo quality.
The module asks whether the v1.1 trace has the three pieces in usable zones, enough mana to establish Breach, and the
minimum pre-loop graveyard fuel to escape the required pieces.
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


def _fuel(s):
    # Underworld Breach's escape additional cost exiles three *other cards*; any card type can pay it.
    return sum(1 for n in s.get("graveyard", []) if n not in PIECES)


def startup_state(s):
    """Return structured startup state for one end-of-turn trace snapshot.

    Standard line modeled:
      Breach in hand/battlefield -> LED in hand/battlefield/graveyard -> activate LED, discarding Brain Freeze if needed
      -> escape Brain Freeze. If LED starts in graveyard it also needs one escape payment before activation.

    Brain Freeze therefore needs 3 pre-loop fuel in every supported zone (hand is discarded to the graveyard by LED);
    LED in graveyard needs another 3. Once Brain Freeze resolves, the first loop mills >=6 cards even when Breach was
    already on the battlefield and LED is the first spell of the turn, enough to pay the next LED+Freeze escape costs.
    """
    z = _zones(s)
    breach_zone = next((k for k in ("battlefield", "hand") if BREACH in z[k]), None)
    led_zone = next((k for k in ("battlefield", "hand", "graveyard") if LED in z[k]), None)
    freeze_zone = next((k for k in ("hand", "graveyard") if FREEZE in z[k]), None)
    if not (breach_zone and led_zone and freeze_zone):
        return {"ready": False, "reason": "piece_zone", "breach_zone": breach_zone, "led_zone": led_zone,
                "freeze_zone": freeze_zone, "fuel": _fuel(s), "fuel_needed": None, "hand_discard": None}

    # Breach must be established before LED activation. Total mana is an upper-bound proxy; exact red source is Step C.
    if breach_zone == "hand" and _unspent(s) < 2:
        return {"ready": False, "reason": "breach_mana", "breach_zone": breach_zone, "led_zone": led_zone,
                "freeze_zone": freeze_zone, "fuel": _fuel(s), "fuel_needed": None, "hand_discard": None}

    fuel_need = 3 + (3 if led_zone == "graveyard" else 0)
    fuel = _fuel(s)
    if fuel < fuel_need:
        return {"ready": False, "reason": "escape_fuel", "breach_zone": breach_zone, "led_zone": led_zone,
                "freeze_zone": freeze_zone, "fuel": fuel, "fuel_needed": fuel_need, "hand_discard": None}

    # LED activation discards the remaining hand. Pieces included: this is a real burden, not hidden.
    hand_discard = len(z["hand"])
    return {"ready": True, "reason": None, "breach_zone": breach_zone, "led_zone": led_zone,
            "freeze_zone": freeze_zone, "fuel": fuel, "fuel_needed": fuel_need, "hand_discard": hand_discard}


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
            margins.append(first[1]["fuel"] - first[1]["fuel_needed"])
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
            "piece-zone requirements, fixed Breach setup mana, initial escape-fuel requirement, hand-discard burden and fuel margin",
            "LED in graveyard requires one extra 3-card escape payment; Brain Freeze in hand is intentionally treated as discarded then escaped",
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
            "Brain Freeze needs 3 initial other-card fuel; LED needs another 3 only if it starts in the graveyard",
            "after the first Brain Freeze, storm produces at least two copies/6 milled cards in the supported line, enough raw cards for the next LED+Freeze escape pair",
            "any graveyard card can pay the escape exile-three additional cost; the three loop pieces themselves are excluded from pre-loop fuel",
        ],
        "parameters": {"turns": TURNS, "breach_setup_total_mana": 2, "escape_cards_per_piece": 3},
        "confidence": "moderate",
        "limitations": [
            "Readiness is a necessary resource/zone proxy for this exact line, not a sufficient protected-win claim.",
            "v1.1 does not natively execute the loop; this module only observes whether startup conditions are present.",
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
