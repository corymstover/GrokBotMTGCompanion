"""ChatGPT cycle 66.5b: adversarial tests for graveyard_recursion v2."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from grixis_mech import graveyard  # noqa: E402


def _rule(name, text, type_line):
    r, why = graveyard.parse(name, text, type_line)
    assert why is None, (text, why)
    return r


def test_recursion_parser_distinguishes_spell_activated_and_etb():
    s = _rule("Raise Dead", "Return target creature card from your graveyard to your hand.", "Sorcery")
    assert s["mode"] == "spell" and s["target"]["types"] == ["creature"]

    a = _rule("Engine", "{2}, {T}: Return target artifact or creature card from your graveyard to the battlefield.", "Artifact")
    assert a["mode"] == "activated" and a["target"]["kind"] == "any_type"
    assert set(a["target"]["types"]) == {"artifact", "creature"}

    e = _rule("Witness", "When Witness enters, return target nonland permanent card from your graveyard to your hand.", "Creature — Elf")
    assert e["mode"] == "etb" and e["target"] == {"kind": "permanent", "types": [], "exclude": ["land"]}


def test_nonland_and_multitype_targets_are_not_collapsed_to_wrong_type():
    nonland = {"kind": "permanent", "types": [], "exclude": ["land"]}
    assert graveyard.legal(nonland, {"permanent": True, "types": ["artifact"]})
    assert not graveyard.legal(nonland, {"permanent": True, "types": ["land"]})

    both = _rule("Reclaimer", "Return target artifact creature card from your graveyard to your hand.", "Sorcery")["target"]
    assert both["kind"] == "all_types"
    assert graveyard.legal(both, {"types": ["artifact", "creature"], "permanent": True})
    assert not graveyard.legal(both, {"types": ["artifact"], "permanent": True})

    union = _rule("Recall", "Return target instant or sorcery card from your graveyard to your hand.", "Sorcery")["target"]
    assert union["kind"] == "any_type"
    assert graveyard.legal(union, {"types": ["instant"]}) and graveyard.legal(union, {"types": ["sorcery"]})


def test_recursion_parser_refuses_conditions_it_cannot_model():
    cases = (
        ("At the beginning of your upkeep, return target creature card from your graveyard to the battlefield.", "Enchantment", "non-ETB"),
        ("When Recur dies, return target creature card from your graveyard to the battlefield.", "Creature", "non-ETB"),
        ("Return target creature card with mana value 3 or less from your graveyard to the battlefield.", "Sorcery", "unrecognised"),
        ("Return target legendary creature card from your graveyard to your hand.", "Sorcery", "unsupported qualifier"),
        ("Return target Zombie card from your graveyard to your hand.", "Sorcery", "subtype"),
        ("Return target creature card from a graveyard to the battlefield.", "Sorcery", "unrecognised"),
    )
    for text, tl, fragment in cases:
        rule, why = graveyard.parse("Recur", text, tl)
        assert rule is None and why and fragment in why, (text, rule, why)


def test_self_recursion_and_granted_quoted_text_do_not_become_other_card_recursion():
    self_text = "Whenever you cast a spell from anywhere other than your hand, return Selfwalker from your graveyard to the battlefield tapped."
    assert graveyard.is_self("Selfwalker", self_text)
    assert not graveyard.matches("Selfwalker", self_text, "Creature")

    granted = 'When Maker enters, create a token with "Return target creature card from your graveyard to your hand."'
    assert graveyard.parse("Maker", granted, "Creature")[0] is None


def test_liveness_respects_effect_mode_instead_of_permanent_text_forever():
    models = {"C": {"types": ["creature"], "permanent": True}}
    target = {"kind": "type", "types": ["creature"], "exclude": []}
    spell = {"mode": "spell", "target": target, "destination": "your hand"}
    activated = {"mode": "activated", "target": target, "destination": "your hand"}
    etb = {"mode": "etb", "target": target, "destination": "your hand"}

    games = [(None, [
        {"turn": 1, "battlefield": [], "graveyard": [], "hand": ["R"]},
        {"turn": 2, "battlefield": ["R"], "graveyard": ["C"], "hand": []},
        {"turn": 3, "battlefield": ["R"], "graveyard": ["C"], "hand": []},
    ])]
    # Spell mode is no longer available once R leaves hand.
    assert graveyard.live(games, "R", spell, models, 3)[0] == 0.0
    # Activated mode is live on the battlefield once a target exists.
    assert graveyard.live(games, "R", activated, models, 3)[0] == 1.0
    # ETB mode is live only on the arrival turn (T2); it does not become a repeatable engine on T3.
    assert graveyard.live(games, "R", etb, models, 3)[0] == 1.0

    late = [(None, [
        {"turn": 1, "battlefield": [], "graveyard": [], "hand": ["R"]},
        {"turn": 2, "battlefield": ["R"], "graveyard": [], "hand": []},
        {"turn": 3, "battlefield": ["R"], "graveyard": ["C"], "hand": []},
    ])]
    # Target appears only after the ETB turn, so the ETB recursion was not live.
    assert graveyard.live(late, "R", etb, models, 3)[0] == 0.0


def test_target_kind_compatibility_helper_keeps_simple_legacy_calls():
    assert graveyard.target_kind("Return target creature card from your graveyard to the battlefield.") == "creature"
    assert graveyard.target_kind("Return target instant or sorcery card from your graveyard to your hand.") == "instant_or_sorcery"
    assert graveyard.target_kind("Return target nonland permanent card from your graveyard to your hand.") == "nonland permanent"
