from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from grixis_mech import breach


def snap(turn=4, hand=None, battlefield=None, graveyard=None, mana=2, spent=0):
    return {"turn": turn, "hand": hand or [], "battlefield": battlefield or [], "graveyard": graveyard or [],
            "mana": mana, "spent": spent}


def test_exact_roles_and_refusal_are_narrow():
    assert breach.role("Underworld Breach", "Each nonland card in your graveyard has escape.", "Enchantment") == "breach"
    assert breach.role("Lion's Eye Diamond", "Discard your hand, Sacrifice Lion's Eye Diamond: Add three mana of any one color.", "Artifact") == "led"
    assert breach.role("Brain Freeze", "Target player mills three cards. Storm", "Instant") == "brain_freeze"
    assert breach.role("Escape Artist", "Escape—{2}{U}", "Creature") is None
    assert "not one of the modeled" in breach.reason("Escape Artist", "Escape—{2}{U}", "Creature")


def test_breach_in_hand_needs_two_total_unspent_mana():
    s = snap(hand=[breach.BREACH, breach.LED, breach.FREEZE, "A", "B", "C"], mana=1)
    st = breach.startup_state(s)
    assert not st["ready"] and st["reason"] == "breach_mana"
    s["mana"] = 2
    st = breach.startup_state(s)
    assert st["ready"]


def test_led_in_graveyard_must_pay_before_hand_discard_fuel_exists():
    # Three pre-existing graveyard cards escape LED; three non-piece hand cards are then discarded and pay for Freeze.
    s = snap(hand=[breach.BREACH, breach.FREEZE, "H1", "H2", "H3"],
             graveyard=[breach.LED, "G1", "G2", "G3"], mana=2)
    st = breach.startup_state(s)
    assert st["ready"]
    assert st["graveyard_fuel"] == 3
    assert st["discard_fuel"] == 3
    assert st["brain_freeze_fuel"] == 3
    assert st["hand_discard"] == 4  # Freeze + H1/H2/H3; Breach was cast first.

    s2 = snap(hand=[breach.BREACH, breach.FREEZE, "H1", "H2", "H3"],
              graveyard=[breach.LED, "G1", "G2"], mana=2)
    st2 = breach.startup_state(s2)
    assert not st2["ready"] and st2["reason"] == "led_escape_fuel"


def test_led_from_hand_can_use_discarded_nonpieces_as_freeze_fuel():
    s = snap(hand=[breach.BREACH, breach.LED, breach.FREEZE, "H1", "H2", "H3"], mana=2)
    st = breach.startup_state(s)
    assert st["ready"]
    assert st["graveyard_fuel"] == 0
    assert st["discard_fuel"] == 3
    assert st["brain_freeze_fuel"] == 3
    assert st["hand_discard"] == 4  # Freeze + three nonpieces; Breach and LED are cast first.


def test_brain_freeze_escape_needs_three_post_led_other_cards():
    s = snap(hand=[breach.BREACH, breach.LED, breach.FREEZE, "H1", "H2"], mana=2)
    st = breach.startup_state(s)
    assert not st["ready"] and st["reason"] == "brain_freeze_escape_fuel"
    assert st["brain_freeze_fuel"] == 2


def test_side_reports_readiness_without_calling_it_a_win():
    tr = [
        snap(turn=3, hand=[breach.BREACH, breach.LED, breach.FREEZE, "H1", "H2"], mana=2),
        snap(turn=4, hand=[breach.BREACH, breach.LED, breach.FREEZE, "H1", "H2", "H3"], mana=2),
    ]
    out = breach.side([(None, tr)], 4)
    assert out["p_startup_ready"] == 1.0
    assert out["mean_earliest_turn_when_ready"] == 4
    assert all("win" not in m.lower() for m in breach.LEDBreachSequences.SPEC["metrics"])
    assert "multiplayer win rates (never produced)" in breach.LEDBreachSequences.SPEC["does_not_model"]
