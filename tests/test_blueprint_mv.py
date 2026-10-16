"""Bot cycle 62: mana-value claims in blueprints must match the Scryfall cache cmc (Thraximundar root cause)."""
import _helpers  # noqa: F401  (sys.path)
import grixis_blueprints as gb


def _bp(text, field="honest_note", cards=None):
    bp = {"commanders": {"value": [{"name": "Thraximundar"}]}, "commander_role": {"value": {field: text}},
          "key_interactions": [], "failure_modes": []}
    if cards:
        bp["key_interactions"] = [{"id": "k", "summary": cards[1], "cards": cards[0], "evidence": []}]
    return bp


def test_cost_mv():
    assert gb.cost_mv("{4}{U}{B}{R}") == 7 and gb.cost_mv("{X}{R}") == 1 and gb.cost_mv("{2/W}{B}") == 3


def test_wrong_commander_mv_fails_right_passes():
    f = gb.cmc_lookup()
    assert gb.mv_problems(_bp("Removal taxes a six-mana commander."), f)
    assert not gb.mv_problems(_bp("Removal taxes a seven-mana commander."), f)
    assert gb.mv_problems(_bp("Oracle cost {4}{U}{B}{R} is mana value 6."), f)
    assert gb.mv_problems({"commanders": {"value": [{"name": "Thraximundar"}]}, "failure_modes": [],
                           "key_interactions": [{"id": "x", "summary": "Thraximundar is mana value 6.", "cards": ["Thraximundar"], "evidence": []}]}, f)


def test_card_entry_and_parenthesised_lists():
    f = gb.cmc_lookup()
    bp = {"commanders": {"value": [{"name": "Thraximundar"}]}, "identity_core": [{"card": "Entomb", "why": "Two-mana setup.", "evidence": []}]}
    assert gb.mv_problems(bp, f)
    bp["identity_core"][0]["why"] = "One-mana setup."
    assert not gb.mv_problems(bp, f)
    assert gb.mv_problems(_bp("Six-mana storm engines (Thousand-Year Storm, Guttersnipe)."), f)
    assert not gb.mv_problems(_bp("five- to seven-mana copy engines; MV 3 or less."), f)


def test_all_blueprints_pass_mv_rule():
    f = gb.cmc_lookup()
    probs = [p for slug, bp in gb.load_all().items() for p in gb.mv_problems(bp, f)]
    assert probs == []
