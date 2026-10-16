from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from grixis_mech import pressure


def test_life_loss_parser_supports_fixed_table_pressure_and_flags_symmetry():
    r, why = pressure.life_parse("Boltwave", "Boltwave deals 3 damage to each opponent.", "Instant")
    assert why is None and r["kind"] == "spell" and r["amount"] == 3 and r["opponents"] == 3
    assert not r["self_burden"] and r["mode"] == "damage"

    r, why = pressure.life_parse("Flame Rift", "Flame Rift deals 4 damage to each player.", "Sorcery")
    assert why is None and r["amount"] == 4 and r["opponents"] == 3 and r["self_burden"]


def test_life_loss_refuses_commander_condition_instead_of_guessing():
    text = "At the beginning of combat on your turn, if you control your commander, each opponent loses 3 life."
    r, why = pressure.life_parse("Loyal Subordinate", text, "Creature — Zombie")
    assert r is None and "intervening-if" in why


def test_cast_trigger_pressure_uses_supported_cast_filter():
    text = "Whenever you cast a noncreature spell, Kessig Flamebreather deals 1 damage to each opponent."
    r, why = pressure.life_parse("Kessig Flamebreather", text, "Creature — Jackal Shaman")
    assert why is None and r["kind"] == "cast" and r["cast_filter"]["kinds"] == ("noncreature",)

    models = {
        "Kessig Flamebreather": {"types": ["creature"], "creature": True},
        "Spell": {"types": ["instant"]},
    }
    ctx = {"models": models, "cards": {}}
    tr = [
        {"turn": 1, "battlefield": [], "graveyard": [], "hand": ["Kessig Flamebreather", "Spell"], "commander_cast": None},
        {"turn": 2, "battlefield": ["Kessig Flamebreather"], "graveyard": [], "hand": ["Spell"], "commander_cast": None},
        {"turn": 3, "battlefield": ["Kessig Flamebreather"], "graveyard": ["Spell"], "hand": [], "commander_cast": None},
    ]
    got = pressure._side([(None, tr)], "Kessig Flamebreather", r, ctx, 3, "life_loss")
    assert got["opponent_demand"] == 3
    assert got["max_same_turn_opponent_demand"] == 3
    assert got["self_burden"] == 0


def test_one_shot_symmetric_damage_tracks_opponents_and_self_separately():
    rule, _ = pressure.life_parse("Flame Rift", "Flame Rift deals 4 damage to each player.", "Sorcery")
    models = {"Flame Rift": {"types": ["sorcery"]}}
    ctx = {"models": models, "cards": {}}
    tr = [
        {"turn": 1, "battlefield": [], "graveyard": [], "hand": ["Flame Rift"], "commander_cast": None},
        {"turn": 2, "battlefield": [], "graveyard": ["Flame Rift"], "hand": [], "commander_cast": None},
    ]
    got = pressure._side([(None, tr)], "Flame Rift", rule, ctx, 2, "life_loss")
    assert got["opponent_demand"] == 12
    assert got["self_burden"] == 4


def test_discard_pressure_fixed_and_symmetric_cases():
    r, why = pressure.discard_parse("Syphon Mind", "Each other player discards a card. You draw a card for each card discarded this way.", "Sorcery")
    assert why is None and r["kind"] == "spell" and r["amount"] == 1 and r["opponents"] == 3 and not r["self_burden"]

    r, why = pressure.discard_parse("Delirium Skeins", "Each player discards three cards.", "Sorcery")
    assert why is None and r["amount"] == 3 and r["opponents"] == 3 and r["self_burden"]


def test_discard_pressure_refuses_self_or_whole_hand_semantics():
    r, why = pressure.discard_parse("Wild Guess", "As an additional cost to cast this spell, discard a card. Draw two cards.", "Sorcery")
    assert r is None and "outside" in why
    r, why = pressure.discard_parse("Wheel", "Each player discards their hand, then draws seven cards.", "Sorcery")
    assert r is None and "outside" in why


def test_specs_never_claim_win_rate_or_generic_value():
    for cls in (pressure.TableLifeLoss, pressure.DiscardPressure):
        assert cls.SPEC["evidence_class"] == "test_result"
        assert all("win" not in m.lower() for m in cls.SPEC["metrics"])
        assert "multiplayer win rates (never produced)" in cls.SPEC["does_not_model"]
