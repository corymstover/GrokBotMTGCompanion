"""ChatGPT cycle 66.10: semantic tests for category-specific stax/tax proxy."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from grixis_mech import stax  # noqa: E402


def _games(name="S", turns=3):
    return [(None, [{"turn": t, "battlefield": ([name] if t >= 2 else []), "graveyard": [], "hand": []}
                    for t in range(1, turns + 1)])]


def test_asymmetric_and_symmetric_spell_taxes_are_distinguished():
    r, why = stax.parse("Tax", "Spells your opponents cast cost {1} more to cast.", "Artifact")
    assert why is None and r == [{"kind": "spell_tax", "scope": "any", "amount": 1, "self_burden": False}]

    r, why = stax.parse("Sphere", "Spells cost {1} more to cast.", "Artifact")
    assert why is None and r == [{"kind": "spell_tax", "scope": "any", "amount": 1, "self_burden": True}]

    r, why = stax.parse("Thorn", "Noncreature spells cost {1} more to cast.", "Artifact")
    assert why is None and r[0]["scope"] == "noncreature" and r[0]["self_burden"]


def test_rule_of_law_and_narset_style_caps():
    r, why = stax.parse("Lab", "Each player can't cast more than one spell each turn.", "Enchantment")
    assert why is None and r[0] == {"kind": "cast_cap", "cap": 1, "self_burden": True}

    r, why = stax.parse("Narset", "Each opponent can't draw more than one card each turn.", "Planeswalker")
    assert why is None and r[0] == {"kind": "draw_cap", "cap": 1, "self_burden": False}


def test_static_locks_keep_self_burden_separate():
    cases = (
        ("Your opponents can't search libraries.", "search_lock", False),
        ("Your opponents can't cast spells during your turn.", "your_turn_cast_lock", False),
        ("Artifacts your opponents control enter the battlefield tapped.", "opponent_artifact_etb_tapped", False),
        ("Activated abilities of artifacts can't be activated.", "activated_lock", True),
        ("Players can't cast spells from graveyards.", "graveyard_cast_lock", True),
        ("Creatures entering the battlefield don't cause abilities to trigger.", "creature_etb_trigger_lock", True),
    )
    for text, kind, burden in cases:
        r, why = stax.parse("S", text, "Artifact")
        assert why is None and r[0]["kind"] == kind and r[0]["self_burden"] is burden, (text, r, why)


def test_tax_friction_math_is_category_specific_not_composite():
    rules = [{"kind": "spell_tax", "scope": "any", "amount": 1, "self_burden": False},
             {"kind": "cast_cap", "cap": 1, "self_burden": False}]
    # Two active rounds (T2,T3); three opponents; two spells/opponent turn.
    m = stax.metrics(_games(), "S", rules, 3, spells=2.0, noncreature_share=0.5, draws=1.0)
    assert m["opponent_extra_mana"] == 12.0
    assert m["opponent_spells_blocked"] == 6.0
    assert m["opponent_draws_blocked"] == 0.0
    assert set(m["kinds"]) == {"spell_tax", "cast_cap"}


def test_noncreature_tax_uses_declared_noncreature_share():
    rules = [{"kind": "spell_tax", "scope": "noncreature", "amount": 1, "self_burden": True}]
    # One active round at T2: 3 opponents * 2 spells * .5 = 3 extra mana demanded.
    m = stax.metrics(_games(turns=2), "S", rules, 2, spells=2.0, noncreature_share=0.5, draws=1.0)
    assert m["opponent_extra_mana"] == 3.0 and m["self_burden"] is True


def test_caps_use_declared_activity_not_fake_win_rate():
    cast = [{"kind": "cast_cap", "cap": 1, "self_burden": True}]
    draw = [{"kind": "draw_cap", "cap": 1, "self_burden": False}]
    assert stax.metrics(_games(turns=2), "S", cast, 2, 3.0, 0.7, 1.0)["opponent_spells_blocked"] == 6.0
    assert stax.metrics(_games(turns=2), "S", draw, 2, 1.0, 0.7, 3.0)["opponent_draws_blocked"] == 6.0


def test_unmodelled_dynamic_tax_is_refused():
    text = "Each spell a player casts costs {1} more to cast for each other spell that player has cast this turn."
    r, why = stax.parse("Damping Sphere", text, "Artifact")
    assert r is None
    assert not stax.matches("Damping Sphere", text, "Artifact")


def test_stax_spec_never_collapses_categories_or_claims_win_rate():
    spec = stax.StaxTax.SPEC
    assert spec["evidence_class"] == "test_result" and spec["confidence"] == "low"
    assert any("not summed" in x for x in spec["limitations"])
    assert any("win rates" in x for x in spec["does_not_model"])
