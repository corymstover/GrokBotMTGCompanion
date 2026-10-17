import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))

import grixis_mana_base as mb
import grixis_mana_opportunity as mo


def card(name, typ="Land", oracle="", mana="—", mv=0, ci="C"):
    return mb.classify({"name":name,"type_line":typ,"oracle":oracle,"mana_cost":mana,"mv":float(mv),"color_identity":ci,"shard":"synthetic"},set("UBR"))


def src(card, potential="", unconditional="", timing="untapped_by_default", conditional=False, kind="direct_land"):
    return {"card":card,"kind":kind,"potential_colors":potential,"unconditional_colors":unconditional,"untapped_capable_colors":potential,"guaranteed_untapped_colors":unconditional,"entry_timing":timing,"conditional_mana_ability":conditional,"fetch_target_count":0}


def test_burden_dimensions_remain_separate_not_scored():
    r=src("X",potential="",unconditional="",timing="always_tapped",conditional=True)
    flags=mo.burden_flags(r)
    assert set(flags)=={"no_usable_grixis_color","always_enters_tapped","conditional_mana_ability"}
    assert not any("score" in x.lower() for x in flags)


def test_single_color_and_conditional_untapped_are_distinct():
    r=src("X",potential="B",unconditional="B",timing="conditional_untapped")
    assert set(mo.burden_flags(r))=={"single_color_source","conditional_untapped"}


def test_utility_categories_ignore_quoted_treasure_reminder_text():
    c=card("Maker",typ="Creature",oracle="Create a Treasure token. (It's an artifact with \"{T}, Sacrifice this artifact: Add one mana of any color.\")")
    cats=mo.utility_categories(c)
    assert "token" in cats
    assert "cost_reduction_or_ramp" not in cats


def test_pure_mana_land_is_not_nonmana_utility():
    c=card("Island",typ="Basic Land — Island",oracle="({T}: Add {U}.)")
    assert mo.utility_categories(c)==[]


def test_fetch_fixing_is_not_mislabeled_as_nonmana_utility():
    c=card("Polluted Delta",oracle="{T}, Pay 1 life, Sacrifice Polluted Delta: Search your library for an Island or Swamp card, put it onto the battlefield, then shuffle.")
    assert mo.utility_categories(c)==[]


def test_utility_categories_detect_real_land_effect():
    c=card("Archive",oracle="{T}: Add {C}.\n{2}, {T}, Sacrifice Archive: Draw two cards.")
    cats=mo.utility_categories(c)
    assert "card_advantage" in cats
    assert "sacrifice" in cats


def test_blueprint_name_support_is_exact_evidence_not_protection():
    bp={"packages":[{"cards":["Bojuka Bog"],"role":"graveyard interaction"}]}
    c=card("Bojuka Bog",oracle="Bojuka Bog enters tapped.\nWhen Bojuka Bog enters, exile target player's graveyard.\n{T}: Add {B}.")
    flags=mo.support_flags("Bojuka Bog",c,bp,None)
    assert "named_in_blueprint" in flags
    assert "graph_identity_core" not in flags


def test_commander_land_hooks_are_textual_only():
    bp={"commanders":{"value":[{"name":"Walker","oracle_text":"Swampwalk (This creature can't be blocked as long as defending player controls a Swamp.)"}]}}
    hooks=mo.commander_hooks(bp)
    assert hooks and "swamp" in hooks[0]["terms"]
    assert "land_generic" not in hooks[0]["terms"]


def test_mdfc_records_spell_and_land_sides_without_free_slot_claim():
    c=card("Flexible",typ="Sorcery // Land",oracle="Draw two cards.\nFlexible enters tapped.\n{T}: Add {U}.",mana="{3}{U}",mv=4,ci="U")
    r=src("Flexible",potential="U",unconditional="U",timing="always_tapped",kind="mdfc_land_face")
    x=mo.mdfc_record("Flexible",c,r,{},None)
    assert x["spell_face"]["mana_value"]==4
    assert x["land_face"]["potential_colors"]=="U"
    assert "high_mv_spell_face" in x["tradeoff_flags"]
    assert "always_enters_tapped" in x["tradeoff_flags"]
    assert x["authority"]["can_decide"] is False


def test_real_abaddon_record_is_nondecisive_and_has_no_universal_score():
    db=mb.CardDB(); reg=mo.load(mo.REGISTRY)
    did,e=next((k,v) for k,v in reg["decks"].items() if v["slug"]=="abaddon-the-despoiler")
    d=mo.build_one(did,e,db)
    assert d["authority"]["can_decide"] is False
    assert not any("score" in k.lower() for k in d["summary"])
    assert all(x["authority"]["can_decide"] is False for x in d["utility_lands"])
