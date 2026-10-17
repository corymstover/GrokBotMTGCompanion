import json
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))

import grixis_mana_quality_gain as gain
import grixis_mana_step as step


def test_gain_record_has_four_real_nondeciding_examples():
    d=gain.build_record()
    assert d["authority"]["can_decide"] is False
    assert d["measured_deltas"]["automatic_land_swap_decisions"]==0
    assert all(d["measured_deltas"][k]==62 for k in ("mana_base_decks","mana_timing_decks","mana_opportunity_decks","mana_resilience_decks"))
    assert {x["kind"] for x in d["worked_examples"]}=={"timing_and_condition_distinction","mdfc_optionality","utility_land_burden_vs_support","source_resilience"}
    assert all(x["slug"] for x in d["worked_examples"])


def test_commander_mana_is_explicitly_pending_or_fully_validated_never_partial():
    state,n,expected,rc,_=step.commander_state()
    assert expected==62
    assert state in ("pending_local_cache_validation","validated")
    assert n in (0,62)
    assert rc==0


def test_gain_examples_preserve_utility_burden_and_support_separately():
    d=gain.build_record()
    x=next(x for x in d["worked_examples"] if x["kind"]=="utility_land_burden_vs_support")
    assert "burdens" in x["after"] and "support signals" in x["after"]
    assert "auto" in x["why_it_matters"].lower()
