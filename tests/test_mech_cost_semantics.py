"""ChatGPT cycle 66.7: regression tests for X-spell and alternate-cost modules."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from grixis_mech import costs, router  # noqa: E402


def _games(rows):
    return [(None, rows)]


def test_x_rule_uses_printed_mana_cost_not_oracle_x_text():
    assert costs.x_rule({"mana_cost": "{X}{B}{B}"}) == {"x_symbols": 1, "mana_cost": "{X}{B}{B}"}
    assert costs.x_rule({"mana_cost": "{X}{X}{R}"})["x_symbols"] == 2
    assert costs.x_rule({"mana_cost": "{2}{R}", "text": "{X}: Deal X damage."}) is None


def test_x_capacity_counts_hand_and_v11_x_zero_cast_opportunities():
    rows = [
        {"turn": 1, "battlefield": [], "hand": ["Fireball"], "graveyard": [], "mana": 1, "spent": 0},
        {"turn": 2, "battlefield": [], "hand": ["Fireball"], "graveyard": [], "mana": 3, "spent": 0},
        {"turn": 3, "battlefield": [], "hand": [], "graveyard": ["Fireball"], "mana": 5, "spent": 1},
    ]
    ctx = {"cards": {"Fireball": {"text": "Fireball deals X damage.", "type_line": "Sorcery", "mana_cost": "{X}{R}"}},
           "models": {"Fireball": {"mv": 1, "types": ["sorcery"], "land": False}}}
    r = costs.x_capacity(_games(rows), "Fireball", ctx, 3)
    assert r == {"mean_max_x": 4.0, "mean_ready_turns": 3.0}


def test_x_capacity_respects_multiple_x_symbols():
    rows = [{"turn": 1, "battlefield": [], "hand": ["XX"], "graveyard": [], "mana": 5, "spent": 0}]
    ctx = {"cards": {"XX": {"text": "XX enters with X counters.", "type_line": "Artifact Creature", "mana_cost": "{X}{X}{1}"}},
           "models": {"XX": {"mv": 1, "types": ["artifact", "creature"], "land": False}}}
    assert costs.x_capacity(_games(rows), "XX", ctx, 1)["mean_max_x"] == 2.0


def test_alternate_parser_supports_fixed_commander_and_evoke_lines():
    r, why = costs.alternate_parse("Alt", "You may pay {1}{R} rather than pay Alt's mana cost.", "Instant")
    assert why is None and r["kind"] == "fixed_mana" and r["mana"] == 2 and r["condition"] == "none"

    r, why = costs.alternate_parse("Guard", "If you control a commander, you may cast Guard without paying its mana cost.", "Instant")
    assert why is None and r == {"kind": "free_with_commander", "mana": 0, "condition": "commander", "drawback": None}

    r, why = costs.alternate_parse("Mulldrifter", "Flying\nEvoke {2}{U}", "Creature — Elemental")
    assert why is None and r["kind"] == "evoke" and r["mana"] == 3 and r["drawback"] == "sacrifice_after_etb"


def test_alternate_parser_refuses_resource_based_and_zone_alternatives():
    cases = (
        ("You may exile a blue card from your hand rather than pay Force's mana cost.", "resource"),
        ("Delve", "resource"),
        ("Flashback {2}{U}", "zone"),
        ("Escape—{1}{B}, Exile three other cards from your graveyard.", "zone"),
    )
    for text, fragment in cases:
        r, why = costs.alternate_parse("Force", text, "Instant")
        assert r is None and why and fragment in why, (text, r, why)


def test_alternate_readiness_separates_alt_only_turns():
    rows = [
        {"turn": 1, "battlefield": [], "hand": ["Alt"], "graveyard": [], "mana": 2, "spent": 0},
        {"turn": 2, "battlefield": [], "hand": ["Alt"], "graveyard": [], "mana": 5, "spent": 0},
    ]
    ctx = {"cards": {"Alt": {"text": "You may pay {1}{R} rather than pay Alt's mana cost.", "type_line": "Instant", "mana_cost": "{4}{R}"}},
           "models": {"Alt": {"mv": 5}}, "commanders": set()}
    assert costs.alternate_ready(_games(rows), "Alt", ctx, 2) == {"alt_ready": 2.0, "alt_only": 1.0}


def test_commander_free_alternate_requires_commander_on_battlefield():
    rows = [
        {"turn": 1, "battlefield": [], "hand": ["Guard"], "graveyard": [], "mana": 0, "spent": 0},
        {"turn": 2, "battlefield": ["Cmdr"], "hand": ["Guard"], "graveyard": [], "mana": 0, "spent": 0},
    ]
    ctx = {"cards": {"Guard": {"text": "If you control a commander, you may cast Guard without paying its mana cost.", "type_line": "Instant", "mana_cost": "{2}{U}"}},
           "models": {"Guard": {"mv": 3}}, "commanders": {"Cmdr"}}
    assert costs.alternate_ready(_games(rows), "Guard", ctx, 2) == {"alt_ready": 1.0, "alt_only": 1.0}


def test_router_uses_card_metadata_for_x_spells_and_does_not_confuse_activated_x():
    cards = {
        "Xspell": {"text": "Xspell deals X damage to any target.", "type_line": "Sorcery", "mana_cost": "{X}{R}"},
        "Engine": {"text": "{X}: Engine gets +X/+0 until end of turn.", "type_line": "Creature", "mana_cost": "{2}{R}"},
    }
    r = router.route_swap("Engine", "Xspell", cards)
    assert "x_spells" in r["modules"]
    assert costs.XSpells.matches_card("Xspell", cards["Xspell"])
    assert not costs.XSpells.matches_card("Engine", cards["Engine"])


def test_cost_specs_are_test_results_without_win_rate_claims():
    for m in (costs.XSpells, costs.AlternateCosts):
        assert m.SPEC["evidence_class"] == "test_result"
        assert any("win rates" in x for x in m.SPEC["does_not_model"])
