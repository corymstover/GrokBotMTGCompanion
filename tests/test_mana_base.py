import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import grixis_mana_base as mb


def card(name, mana="—", mv=0, ci="C", typ="Land", oracle=""):
    return {"name": name, "mana_cost": mana, "mv": float(mv), "color_identity": ci, "type_line": typ, "oracle": oracle, "shard": "synthetic"}


def test_parse_cost_fixed_hybrid_and_phyrexian():
    p = mb.parse_cost("{2}{U}{B/R}{U/P}")
    assert p["generic"] == 2
    assert p["colored_equivalent"] == {"U": 1.0, "B": 0.5, "R": 0.5}
    assert p["flexible_groups"] == [["B", "R"]]
    assert p["phyrexian_optional"] == ["U"]
    assert "mana_value_proxy" not in p


def test_any_color_uses_deck_identity_not_card_identity():
    tower = card("Command Tower", oracle="{T}: Add one mana of any color in your commander's color identity.")
    x = mb.classify(tower, set("UBR"))
    assert x["source_colors"] == "UBR"
    assert not x["conditional_source"]


def test_fetchland_type_words_become_potential_colors():
    delta = card(
        "Polluted Delta",
        oracle="{T}, Pay 1 life, Sacrifice Polluted Delta: Search your library for an Island or Swamp card, put it onto the battlefield, then shuffle.",
    )
    x = mb.classify(delta, set("UBR"))
    assert set(x["fetch_types"]) == {"Island", "Swamp"}
    assert x["basic_fetch"] is False
    assert set(x["source_colors"]) == {"U", "B"}


def test_off_identity_fetch_type_does_not_become_usable_color():
    strand = card(
        "Flooded Strand",
        oracle="{T}, Pay 1 life, Sacrifice Flooded Strand: Search your library for a Plains or Island card, put it onto the battlefield, then shuffle.",
    )
    x = mb.classify(strand, set("UBR"))
    assert set(x["fetch_types"]) == {"Plains", "Island"}
    assert x["source_colors"] == "U"


def test_basic_fetch_uses_deck_identity_as_potential_colors():
    vista = card(
        "Prismatic Vista",
        oracle="{T}, Pay 1 life, Sacrifice Prismatic Vista: Search your library for a basic land card, put it onto the battlefield, then shuffle.",
    )
    x = mb.classify(vista, set("UBR"))
    assert x["basic_fetch"] is True
    assert x["fetch_types"] == []
    assert set(x["source_colors"]) == {"U", "B", "R"}


def test_tapped_unconditional_and_conditional_are_separate():
    always = card("Always", oracle="Always enters tapped.\n{T}: Add {U}.")
    check = card("Check", oracle="Check enters tapped unless you control an Island.\n{T}: Add {B}.")
    a = mb.classify(always, set("UBR")); b = mb.classify(check, set("UBR"))
    assert a["tapped_unconditional"] and not a["tapped_conditional"]
    assert b["tapped_conditional"] and not b["tapped_unconditional"]


def test_restricted_source_is_labeled_conditional():
    d = card("Restricted", mana="{1}", mv=1, typ="Artifact", oracle="{T}: Add {R}. Spend this mana only to cast creature spells.")
    x = mb.classify(d, set("UBR"))
    assert x["repeatable_nonland_source"]
    assert x["conditional_source"]


def test_treasure_grant_is_not_mistaken_for_card_self_sacrifice():
    maker = card(
        "Treasure Maker",
        mana="{3}{R}",
        mv=4,
        ci="R",
        typ="Creature — Dwarf",
        oracle="Whenever you cast an instant or sorcery spell, create a Treasure token. (It's an artifact with \"{T}, Sacrifice this artifact: Add one mana of any color.\")",
    )
    x = mb.classify(maker, set("UBR"))
    assert x["one_shot_mana"] is False


def test_named_self_sacrifice_is_one_shot_mana():
    petal = card("Lotus Petal", mv=0, typ="Artifact", oracle="{T}, Sacrifice Lotus Petal: Add one mana of any color.")
    x = mb.classify(petal, set("UBR"))
    assert x["one_shot_mana"] is True
    assert x["fast_mana"] is True


def test_hypergeometric_and_color_presence_sanity():
    assert mb.hyper_atleast(99, 0, 10, 1) == 0.0
    assert mb.hyper_atleast(99, 99, 10, 1) == 1.0
    p = mb.hyper_atleast(99, 20, 10, 1)
    assert 0 < p < 1
    masks = ["U", "B", "R"] + ["UBR"] * 3
    p3 = mb.p_all_colors_seen(99, masks, "UBR", 12)
    assert 0 <= p3 <= 1
    assert mb.p_all_colors_seen(99, masks, "", 12) == 1.0


def test_land_drop_probabilities_are_bounded_and_harder_by_turn():
    vals = [mb.p_land_drops(99, 34, t) for t in range(1, 6)]
    assert all(0 <= x <= 1 for x in vals)
    assert vals == sorted(vals, reverse=True)


def test_real_frozen_card_page_smoke():
    db = mb.CardDB()
    abaddon = db.get("Abaddon the Despoiler")
    assert abaddon["mana_cost"] == "{2}{U}{B}{R}"
    assert abaddon["mv"] == 5.0
    assert set(abaddon["color_identity"]) == {"U", "B", "R"}
    modeled = mb.classify(abaddon, set("UBR"))
    assert modeled["cost"]["colored_equivalent"] == {"U": 1.0, "B": 1.0, "R": 1.0}


def test_build_record_is_never_decision_capable():
    db = mb.CardDB()
    reg = mb.load(mb.REGISTRY)
    did, entry = next((k, v) for k, v in reg["decks"].items() if v["slug"] == "abaddon-the-despoiler")
    d = mb.build_one(did, entry, db)
    assert d["authority"]["can_decide"] is False
    assert d["status"] == "provisional_evidence"
    assert d["evidence_class"] == "derived_metric"
    assert d["deck_color_identity"] == "UBR"
