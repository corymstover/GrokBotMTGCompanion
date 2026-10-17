import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import grixis_mana_base as mb
import grixis_mana_timing as mt


def raw(name, typ="Land", oracle="", ci="C", mana="—", mv=0):
    return {"name":name,"type_line":typ,"oracle":oracle,"color_identity":ci,"mana_cost":mana,"mv":float(mv),"shard":"synthetic"}


def modeled(name, typ="Land", oracle="", ci="C"):
    d = mb.classify(raw(name, typ=typ, oracle=oracle, ci=ci), set("UBR"))
    d["direct_mask"] = mt.direct_mask(d, set("UBR"))
    return d


def test_distinct_source_matching_does_not_let_one_triland_pay_three_pips():
    masks = ["UBR"] + [""] * 98
    assert mt.distinct_source_match_probability(masks, 12, {"U":1,"B":1,"R":1}) == 0.0


def test_distinct_source_matching_accepts_three_distinct_flexible_sources():
    masks = ["UBR", "UBR", "UBR"] + [""] * 96
    p = mt.distinct_source_match_probability(masks, 99, {"U":1,"B":1,"R":1})
    assert p == 1.0


def test_double_pip_requires_two_source_cards():
    one = ["B"] + [""] * 98
    two = ["B", "UB"] + [""] * 97
    assert mt.distinct_source_match_probability(one, 99, {"B":2}) == 0.0
    assert mt.distinct_source_match_probability(two, 99, {"B":2}) == 1.0


def test_fetch_validation_uses_actual_typed_duals_not_off_identity_type_word():
    fetch = modeled("Flooded Strand", oracle="{T}, Pay 1 life, Sacrifice Flooded Strand: Search your library for a Plains or Island card, put it onto the battlefield, then shuffle.")
    watery = modeled("Watery Grave", typ="Land — Island Swamp", oracle="({T}: Add {U} or {B}.)\nAs Watery Grave enters, you may pay 2 life. If you don't, it enters tapped.")
    steam = modeled("Steam Vents", typ="Land — Island Mountain", oracle="({T}: Add {U} or {R}.)\nAs Steam Vents enters, you may pay 2 life. If you don't, it enters tapped.")
    mountain = modeled("Mountain", typ="Basic Land — Mountain", oracle="({T}: Add {R}.)")
    targets = mt.fetch_targets("Flooded Strand", fetch, [("Flooded Strand", fetch), ("Watery Grave", watery), ("Steam Vents", steam), ("Mountain", mountain)])
    assert {x["card"] for x in targets} == {"Watery Grave", "Steam Vents"}
    assert mt.color_union(targets) == "UBR"


def test_fetch_can_be_stranded_when_no_actual_target_exists():
    fetch = modeled("Flooded Strand", oracle="{T}, Pay 1 life, Sacrifice Flooded Strand: Search your library for a Plains or Island card, put it onto the battlefield, then shuffle.")
    mountain = modeled("Mountain", typ="Basic Land — Mountain", oracle="({T}: Add {R}.)")
    assert mt.fetch_targets("Flooded Strand", fetch, [("Flooded Strand", fetch), ("Mountain", mountain)]) == []


def test_basic_fetch_requires_basic_supertype():
    vista = modeled("Prismatic Vista", oracle="{T}, Pay 1 life, Sacrifice Prismatic Vista: Search your library for a basic land card, put it onto the battlefield, then shuffle.")
    island = modeled("Island", typ="Basic Land — Island", oracle="({T}: Add {U}.)")
    grave = modeled("Watery Grave", typ="Land — Island Swamp", oracle="({T}: Add {U} or {B}.)")
    targets = mt.fetch_targets("Prismatic Vista", vista, [("Prismatic Vista", vista), ("Island", island), ("Watery Grave", grave)])
    assert [x["card"] for x in targets] == ["Island"]


def test_source_timing_categories_remain_categorical():
    tapped = modeled("Tapland", oracle="Tapland enters tapped.\n{T}: Add {U}.")
    shock = modeled("Shock", typ="Land — Island Swamp", oracle="({T}: Add {U} or {B}.)\nAs Shock enters, you may pay 2 life. If you don't, it enters tapped.")
    basic = modeled("Island", typ="Basic Land — Island", oracle="({T}: Add {U}.)")
    assert mt.entry_timing(tapped) == "always_tapped"
    assert mt.entry_timing(shock) == "conditional_untapped"
    assert mt.entry_timing(basic) == "untapped_by_default"


def test_conditional_mana_ability_not_promoted_to_unconditional_colors():
    reflecting = modeled("Reflecting Pool", oracle="{T}: Add one mana of any type that a land you control could produce.")
    r = mt.source_record("Reflecting Pool", reflecting, [])
    assert r["conditional_mana_ability"] is True
    assert r["unconditional_colors"] == ""


def test_real_abaddon_fetches_have_targets_and_flooded_strand_actual_access_expands():
    db = mb.CardDB(); reg = mt.load(mt.REGISTRY)
    did, entry = next((k,v) for k,v in reg["decks"].items() if v["slug"] == "abaddon-the-despoiler")
    d = mt.build_one(did, entry, db)
    assert d["authority"]["can_decide"] is False
    assert d["stranded_fetches"] == []
    flooded = next(x for x in d["fetch_validation"] if x["card"] == "Flooded Strand")
    assert flooded["target_count"] > 0
    assert "U" in flooded["actual_target_colors"]
    # With typed Grixis duals, an Island fetch can often bridge into B/R as well.
    assert set(flooded["actual_target_colors"]) >= {"U", "B", "R"}


def test_real_commander_readiness_is_bounded_and_nondecisive():
    db = mb.CardDB(); reg = mt.load(mt.REGISTRY)
    did, entry = next((k,v) for k,v in reg["decks"].items() if v["slug"] == "thraximundar")
    d = mt.build_one(did, entry, db)
    row = d["commander_colored_readiness"][0]
    assert row["name"] == "Thraximundar"
    assert row["colored_requirements"] == {"U":1,"B":1,"R":1}
    assert 0 <= row["untapped_capable_distinct_source_match"] <= row["potential_distinct_source_match"] <= 1
    assert d["authority"]["can_decide"] is False
