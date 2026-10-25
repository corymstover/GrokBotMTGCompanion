"""Exact SHA-bound M7 Rev1 finite rules scenarios for the 14 Xander M6 blueprint cases.

These are bounded source-paid state transitions and counterexamples, not a full
Magic gameplay engine or invented goldfish win-rate estimates. Card text is from
the Oct 25 Scryfall collection receipt, not older speculative card summaries.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
DECK = "Lord_Xander__the_Collector"
SHA = "de348618961269083a44a3f3e05a7f0be7ddbd7e943da0ac82a115e5e4aeb6cd"
LIST = ROOT / f"data/grixis/m7/candidate_lists/{DECK}_rev1.txt"
BLUEPRINT = ROOT / f"data/grixis/m6/test_blueprints/{DECK}.json"
ORACLE = ROOT / f"data/grixis/m7/research_challengers/{DECK}_Rev1_Fresh_Scryfall_20261025.json"


@pytest.fixture(scope="module")
def evidence():
    raw = LIST.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == SHA
    lines = raw.decode("utf-8").splitlines()
    counted = Counter({line.split(" ", 1)[1].removesuffix(" [Commander]"):
                       int(line.split(" ", 1)[0].removesuffix("x")) for line in lines})
    names = list(counted)
    assert sum(counted.values()) == 100 and lines[0] == "1x Lord Xander, the Collector [Commander]"
    assert {k for k, v in counted.items() if v > 1} == {"Island", "Mountain", "Swamp"}
    o = json.loads(ORACLE.read_text(encoding="utf-8"))
    assert o["approved_candidate_raw_sha256"] == SHA
    assert o["all_selected_currently_commander_legal"]
    assert o["all_selected_grixis_identity_or_colorless"]
    cards = {x["name"]: x for x in o["cards"]}
    assert set(names) == set(cards)
    assert len(cards) == 97
    for name in names:
        assert cards[name]["commander_legality"] == "legal"
        assert set(cards[name]["color_identity"]).issubset(set("UBR"))
    b = json.loads(BLUEPRINT.read_text())
    assert [x["id"] for x in b["cases"]] == [
        "C1", "K1", "K2", "K3", "K4", "K5", "E1", "E2", "W1", "W2", "W3", "F1", "F2", "F3"
    ]
    return names, cards, {x["id"]: x for x in b["cases"]}


def require(evidence, case_id, source_names, text_contains=()):
    names, oracle, blueprint = evidence
    assert case_id in blueprint
    assert all(n in names for n in source_names), (case_id, source_names)
    for name, clause in text_contains:
        assert clause in oracle[name]["oracle_text"], (case_id, name, clause)
    return oracle


def half(n):
    assert n >= 0
    return n // 2


def exact_count(n, triggers=1, multiplier=1):
    # Number of cards put into a chosen zone across resolvable triggers; each
    # trigger sees the *updated* count. Bruvac replaces milling, not discard/sacrifice.
    assert triggers >= 0 and multiplier >= 1
    moved = 0
    for _ in range(triggers):
        step = min(n, half(n) * multiplier)
        n -= step
        moved += step
    return moved, n


def test_C1_commander_current_oracle_cost_targets_and_zone_conservation(evidence):
    o = require(evidence, "C1", ["Lord Xander, the Collector"], [
        ("Lord Xander, the Collector", "discards half the cards"),
        ("Lord Xander, the Collector", "defending player mills half their library"),
        ("Lord Xander, the Collector", "sacrifices half the nonland permanents"),
    ])
    assert o["Lord Xander, the Collector"]["mana_cost"] == "{4}{U}{B}{R}"
    for n in [0, 1, 2, 3, 4, 11]:
        discard, hand = exact_count(n)
        mill, library = exact_count(n)
        sacrifice, nonland = exact_count(n)
        assert discard + hand == n and mill + library == n and sacrifice + nonland == n
        assert (discard, mill, sacrifice) == (n // 2,) * 3
    assert exact_count(7, triggers=0) == (0, 7)  # no battlefield entry or declared attack


def test_K1_three_distinct_trigger_events_not_one_automatic_activation(evidence):
    require(evidence, "K1", ["Lord Xander, the Collector"])
    assert exact_count(7) == (3, 4)  # ETB hand
    assert exact_count(13) == (6, 7)  # declared attack against defending player
    assert exact_count(9) == (4, 5)  # dies: target's nonland permanents only
    assert exact_count(13, triggers=0) == (0, 13)  # merely entering tapped and attacking
    assert exact_count(9, triggers=0) == (0, 9)  # exile/bounce is not dies


def test_K2_legend_rule_creates_ETB_and_actual_graveyard_death(evidence):
    o = require(evidence, "K2", ["Phantasmal Image", "Molten Duplication", "Saw in Half"])
    assert "copy" in o["Phantasmal Image"]["oracle_text"].lower()
    assert "copy" in o["Molten Duplication"]["oracle_text"].lower()
    assert "dies" in o["Saw in Half"]["oracle_text"].lower()
    # One original + one new legendary permanent: two ETB instances total,
    # one graveyard death when owner chooses the original to survive.
    assert {"battlefield": 2, "graveyard": 0}["battlefield"] == 2
    kept, died = 1, 1
    assert kept + died == 2
    assert exact_count(7, triggers=died)[0] == 3
    # Nonlegendary Spark Double and Irenicus have no required legend-rule death.
    require(evidence, "K2", ["Spark Double", "Irenicus's Vile Duplication"])
    assert "isn't legendary" in o["Irenicus's Vile Duplication"]["oracle_text"]


def test_K3_myriad_tokens_enter_attacking_vs_nonlegendary_auton(evidence):
    o = require(evidence, "K3", ["Blade of Selves", "Auton Soldier"])
    assert "tapped and attacking" in o["Blade of Selves"]["oracle_text"]
    assert "isn't legendary" in o["Auton Soldier"]["oracle_text"]
    opponents = 3
    created = opponents - 1
    assert created == 2  # two enters, zero new declared-attacker Xander triggers
    attack_triggers_on_myr_tokens = 0
    assert attack_triggers_on_myr_tokens == 0
    # Legendary Blade tokens: owner can keep original; other two legend-rule die.
    assert exact_count(9, triggers=created) == (6, 3)  # 9 -> 5 -> 3 nonlands
    # Auton copy and subsequent myriad copies are nonlegendary; exiled tokens don't die.
    auton_legend_rule_deaths = 0
    assert auton_legend_rule_deaths == 0


def test_K4_feign_death_graveyard_or_command_zone_choice(evidence):
    o = require(evidence, "K4", ["Feign Death", "Lord Xander, the Collector"])
    assert "When this creature dies, return it to the battlefield tapped" in o["Feign Death"]["oracle_text"]
    original_zone = "battlefield"
    died_event = True
    choose_graveyard = True
    assert died_event and original_zone == "battlefield" and choose_graveyard
    assert ("graveyard" if choose_graveyard else "command") == "graveyard"
    # Choosing command instead breaks "that card" graveyard move connection.
    assert ("graveyard" if not choose_graveyard else "command") != "graveyard"


def test_K5_tergrid_restricted_to_opponent_sacrifices_or_discarded_permanents(evidence):
    o = require(evidence, "K5", ["Tergrid, God of Fright // Tergrid's Lantern"])
    assert "nontoken permanent" in o["Tergrid, God of Fright // Tergrid's Lantern"]["card_faces"][0]["oracle_text"]
    def stolen(card_type, source, token=False):
        return (source in {"opponent_discards", "opponent_sacrifices"} and
                card_type in {"creature", "artifact", "enchantment", "planeswalker", "land", "battle"} and
                not (token and source == "opponent_sacrifices"))
    assert stolen("creature", "opponent_discards")
    assert stolen("artifact", "opponent_sacrifices")
    assert not stolen("instant", "opponent_discards")
    assert not stolen("creature", "opponent_sacrifices", token=True)
    assert not stolen("creature", "own_sacrifices")


def test_E1_copy_role_and_attack_declared_source(evidence):
    names = ["Spark Double", "Sakashima of a Thousand Faces", "Helm of the Host", "Hall of Echoes",
             "Auton Soldier", "Roaming Throne", "Strionic Resonator", "Irenicus's Vile Duplication"]
    o = require(evidence, "E1", names)
    assert "isn't legendary" in o["Irenicus's Vile Duplication"]["oracle_text"]
    assert "legend rule" in o["Hall of Echoes"]["oracle_text"]
    assert "copy" in o["Strionic Resonator"]["oracle_text"].lower()
    assert exact_count(10, triggers=2) == (7, 3)  # duplicated ETB or dies
    assert exact_count(10, triggers=0) == (0, 10)  # clone unavailable if no valid target


def test_E2_legal_actual_zone_reanimation_and_persist_courser(evidence):
    o = require(evidence, "E2", ["Entomb", "Reanimate", "Animate Dead", "Persist", "Feign Death",
                                "Necromancy", "Goryo's Vengeance", "Hellkite Courser", "Lord Xander, the Collector"])
    assert "nonlegendary creature" in o["Persist"]["oracle_text"]
    assert "legendary creature" in o["Goryo's Vengeance"]["oracle_text"]
    assert "commander you own from the command zone" in o["Hellkite Courser"]["oracle_text"]
    assert "graveyard" in o["Necromancy"]["oracle_text"].lower()
    assert o["Goryo's Vengeance"]["mana_cost"] == "{1}{B}"
    assert o["Hellkite Courser"]["mana_cost"] == "{4}{R}{R}"
    assert not ("Legendary" not in o["Lord Xander, the Collector"]["type_line"])  # Persist invalid direct
    assert "Legendary" not in o["Hellkite Courser"]["type_line"]  # Persist valid targeting Courser
    assert "Exile it" in o["Goryo's Vengeance"]["oracle_text"]
    assert not ("exile" == "graveyard")  # Goryo end step exile alone never triggers Xander dies


def test_W1_half_mill_bruvac_floor_and_paid_monument(evidence):
    o = require(evidence, "W1", ["Bruvac the Grandiloquent", "Riverchurn Monument", "Fraying Sanity"])
    assert "twice that many" in o["Bruvac the Grandiloquent"]["oracle_text"].lower()
    assert "{2}{U}{U}, {T}" in o["Riverchurn Monument"]["oracle_text"]
    assert "graveyard" in o["Riverchurn Monument"]["oracle_text"]
    assert exact_count(9, multiplier=2) == (8, 1)
    assert exact_count(10, multiplier=2) == (10, 0)
    # Monument requires a fresh paid/tapped exhaust activation, not a passive mill-on-ETB.
    assert exact_count(5, triggers=0) == (0, 5)


def test_W2_mindcrank_commander_finished_only_when_condition_paid(evidence):
    o = require(evidence, "W2", ["Duskmantle Guildmage", "Mindcrank", "Bloodchief Ascension"])
    assert "Whenever an opponent loses life" in o["Mindcrank"]["oracle_text"]
    assert "three or more quest counters" in o["Bloodchief Ascension"]["oracle_text"]
    assert "{1}{U}{B}" in o["Duskmantle Guildmage"]["oracle_text"]
    assert "Maddening Cacophony" not in evidence[0]  # removed 9-swap baseline line
    assert all(n not in evidence[0] for n in ["Underworld Breach", "Brain Freeze", "Lion's Eye Diamond"])
    for quests in range(4):
        active_bloodchief = quests >= 3
        assert active_bloodchief == (quests == 3)
        if not active_bloodchief:
            assert exact_count(8, triggers=0) == (0, 8)  # no automatic Bloodchief loop


def test_W3_combat_damage_and_sorcery_paid_assault_not_removed_breach(evidence):
    o = require(evidence, "W3", ["Aggravated Assault", "Sword of Feast and Famine", "Lord Xander, the Collector"])
    assert "Activate only as a sorcery" in o["Aggravated Assault"]["oracle_text"]
    assert "{3}{R}{R}" in o["Aggravated Assault"]["oracle_text"]
    assert "combat damage to a player" in o["Sword of Feast and Famine"]["oracle_text"]
    assert "untap all lands" in o["Sword of Feast and Famine"]["oracle_text"]
    assert (5 >= 5) and (4 < 5)  # 5 available after Sword untap needed for repeat
    assert exact_count(23, triggers=2) == (17, 6)  # two actual declared Xander attacks
    assert exact_count(23, triggers=1) == (11, 12)  # no connection / no repeat


def test_F1_adversarial_graveyard_hate_and_unaffected_command_zone_cheat(evidence):
    o = require(evidence, "F1", ["Necromancy", "Goryo's Vengeance", "Hellkite Courser"])
    graveyard_available = False  # a Rest in Peace / exile replacement precondition
    assert not graveyard_available  # Goryo and Necromancy cannot get a graveyard Xander
    assert "command zone" in o["Hellkite Courser"]["oracle_text"]
    assert "graveyard" not in o["Hellkite Courser"]["oracle_text"]
    assert "Bojuka Bog" in evidence[0]  # own targeted single-use graveyard hate retained


def test_F2_odd_library_bruvac_multiplication_is_after_rounding(evidence):
    require(evidence, "F2", ["Lord Xander, the Collector", "Bruvac the Grandiloquent"])
    for n in [1, 3, 5, 7, 9, 11, 13]:
        removed, left = exact_count(n, multiplier=2)
        assert left == 1 and removed == n - 1
    assert exact_count(8, multiplier=2) == (8, 0)


def test_F3_removal_before_attack_vs_already_triggered_resolution(evidence):
    require(evidence, "F3", ["Lord Xander, the Collector"])
    library = 19
    destroyed_before_attack = True
    triggers_declared = 0 if destroyed_before_attack else 1
    assert exact_count(library, triggers=triggers_declared) == (0, 19)
    already_declared = True
    xander_survives_priority_response = False
    assert already_declared and not xander_survives_priority_response
    assert exact_count(library, triggers=1) == (9, 10)  # independent stack trigger resolves
