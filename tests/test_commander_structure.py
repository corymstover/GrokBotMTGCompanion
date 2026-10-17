import json
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_commander_structure as cs


def reg_entry(slug):
    r=json.loads((ROOT/"data/grixis/registry.json").read_text())
    return next((did,e) for did,e in r["decks"].items() if e["slug"]==slug)


def test_kess_preserves_supported_and_independent_routes():
    did,e=reg_entry("kess-dissident-mage"); d=cs.build_one(did,e); s=d["summary"]
    assert d["authority"]["can_decide"] is False
    assert d["accepted_blueprint_role"]["level"]=="central"
    assert s["blueprint_wins_explicit_commander"]>=1
    assert s["blueprint_wins_structurally_independent"]>=1
    assert s["combo_blueprint_supported"]>=1
    assert s["combo_commander_independent"]>=1


def test_combo_modes_are_exhaustive_partition():
    did,e=reg_entry("kess-dissident-mage"); d=cs.build_one(did,e); s=d["summary"]
    assert s["spellbook_lines"]==s["combo_direct_commander_piece"]+s["combo_blueprint_supported"]+s["combo_commander_independent"]


def test_partner_deck_keeps_both_commander_names():
    did,e=reg_entry("bjorna-nightfall-alchemist-cecily"); d=cs.build_one(did,e)
    assert set(d["commanders"])=={"Bjorna, Nightfall Alchemist","Cecily, Haunted Mage"}
    assert d["authority"]["can_decide"] is False


def test_no_synthetic_commander_value_score_is_emitted():
    did,e=reg_entry("kess-dissident-mage"); d=cs.build_one(did,e)
    txt=json.dumps(d).lower()
    assert 'commander_value_score' not in txt
    assert 'marginal_value_score' not in txt
