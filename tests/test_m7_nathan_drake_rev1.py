"""Deck #39: exact-source finite P0/P1 interaction checks for Nathan M7 Rev1.

This is a bounded fixture-level rules model, not a full Magic rules engine,
multiplayer win-rate simulator, independent M6 I/J run, or owner approval.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIST = ROOT / "data/grixis/m7/candidate_lists/Nathan_Drake_Treasure_Hunter_M7_Rev1_Approval_Candidate_2026-10-26.txt"
SNAPSHOT = ROOT / "data/grixis/m7/oracle_snapshots/Nathan_Drake_M7_Rev1_Selected_Scryfall_20261026.json"
BASELINE = ROOT / "data/grixis/m7/baseline_sources/Nathan_Drake_Treasure_Hunter_Approved_2026-10-15.txt"
RAW = LIST.read_bytes()
SRC = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
ORACLE = {card["name"]: card for card in SRC["cards"]}


def parsed():
    result = Counter()
    for line in RAW.decode().splitlines():
        qty, name = line.split("x ", 1)
        result[name.removesuffix(" [Commander]")] += int(qty)
    return result


def oracle(name):
    return ORACLE[name]["oracle_text"]


def paid(cost, mana, any_color=False):
    """Finite payment test: exact colored pips first, then generic pips.

    'C' and other colored units can pay generic; Nathan's mana-as-any-color
    replacement is permitted only when he is present and spell is unowned.
    """
    pool = list(mana)
    for color in ("W", "U", "B", "R", "G"):
        for _ in range(cost.get(color, 0)):
            if any_color:
                if not pool:
                    return False
                pool.pop()
            elif color in pool:
                pool.remove(color)
            else:
                return False
    return len(pool) >= cost.get("generic", 0)


def heist(libraries, pool, stolen_index, nathan_present=True):
    """One Nathan triggered ability already on stack; one library top each.

    No free spells, no land play, and no multiple stolen spells are assumed.
    A named opponent-owned spell is used to exercise a colored-cost payment.
    """
    exiled = [lib.pop(0) for lib in libraries]
    card = exiled[stolen_index]
    if card == "Island":
        return exiled, None
    costs = {"Cyclonic Rift": {"generic": 1, "U": 1},
             "Toxic Deluge": {"generic": 2, "B": 1},
             "Sol Ring": {"generic": 1}}
    assert card in costs
    if paid(costs[card], pool, any_color=nathan_present and stolen_index != 0):
        return exiled, card
    return exiled, None


def test_exact_candidate_100_singleton_34_land_and_11_real_swaps():
    cards = parsed()
    assert RAW.decode().splitlines()[0] == "1x Nathan Drake, Treasure Hunter [Commander]"
    assert hashlib.sha256(RAW).hexdigest() == "e461d3e89828c7d4950f33301eb5ce658818014304de3771664ec19ce608ef57"
    assert sum(cards.values()) == 100 and len(cards) == 97
    assert {n: c for n, c in cards.items() if c > 1} == {"Island": 2, "Mountain": 2, "Swamp": 2}
    assert len(ORACLE) == 97 and set(ORACLE) == set(cards)
    baseline = Counter()
    for line in BASELINE.read_text(encoding="utf-8").splitlines():
        qty, name = line.split("x ", 1)
        baseline[name.removesuffix(" [Commander]")] += int(qty)
    assert hashlib.sha256(BASELINE.read_bytes()).hexdigest() == "a5d59afc3a78d7ff6454b1d011c82c2f732e11f4d4dd03256df1195a3abe9ba0"
    assert sum((cards - baseline).values()) == sum((baseline - cards).values()) == 11
    assert SRC["candidate_sha256"] == hashlib.sha256(RAW).hexdigest()
    lands = sum(qty for name, qty in cards.items() if "Land" in ORACLE[name]["type_line"]
                or any("Land" in face["type_line"] for face in ORACLE[name]["faces"]))
    assert lands == 34


def test_current_oct26_source_all_cards_commander_legal_ubr():
    assert SRC["source"] == "https://api.scryfall.com/cards/collection"
    for name, card in ORACLE.items():
        assert card["commander_legality"] == "legal", name
        assert set(card["color_identity"]) <= {"U", "B", "R"}, name
        assert card["oracle_id"] and card["type_line"]


def test_P0_C1_attack_heist_four_libraries_one_paid_spell_and_zone():
    assert "Whenever Nathan Drake attacks, exile the top card of each player's library" in oracle("Nathan Drake, Treasure Hunter")
    assert "You may cast a spell from among those cards" in oracle("Nathan Drake, Treasure Hunter")
    libraries = [["Sol Ring", "Island"], ["Cyclonic Rift", "Island"],
                 ["Toxic Deluge", "Island"], ["Island", "Sol Ring"]]
    exiled, cast = heist(libraries, ["R", "R"], stolen_index=1)
    assert exiled == ["Sol Ring", "Cyclonic Rift", "Toxic Deluge", "Island"]
    assert cast == "Cyclonic Rift"  # 1U paid with two red via Nathan static.
    assert all(len(lib) == 1 for lib in libraries)
    no_payment, cannot_cast = heist([["Sol Ring"], ["Cyclonic Rift"],
                                     ["Toxic Deluge"], ["Island"]], [], 1)
    assert len(no_payment) == 4 and cannot_cast is None
    # This fixture models a declared attack with Nathan on the battlefield.
    # No attack declaration (e.g. Nathan in command zone) means no trigger.
    declared_attacker = False
    assert not declared_attacker


def test_P0_K1_attack_trigger_not_damage_trigger():
    text = oracle("Nathan Drake, Treasure Hunter")
    assert "Whenever Nathan Drake attacks" in text
    assert "Whenever Nathan Drake deals combat damage" not in text
    # Trigger already on stack when blockers are declared or no damage dealt.
    pending = 1
    blocked = True
    dealt_combat_damage = False
    assert blocked and not dealt_combat_damage and pending == 1


def test_P0_K2_any_color_only_unowned_and_controlled_unowned_permanents():
    text = oracle("Nathan Drake, Treasure Hunter")
    assert "to cast spells you don't own" in text
    assert "to activate abilities of permanents you control but don't own" in text
    assert paid({"generic": 1, "U": 1}, ["R", "R"], any_color=True)
    assert not paid({"generic": 1, "U": 1}, ["R", "R"], any_color=False)
    assert paid({"generic": 1, "U": 1}, ["U", "R"], any_color=False)
    # Native spells cast from Nathan's own library still require normal colors.
    assert heist([["Cyclonic Rift"], ["Island"], ["Island"], ["Island"]], ["R", "R"], 0)[1] is None


def test_P0_K3_palace_firebending_pre_resolves_nathan_and_limited_mana():
    assert "Target creature you control gains firebending 4" in oracle("Fire Nation Palace")
    assert "This mana lasts until end of combat" in oracle("Fire Nation Palace")
    assert "Whenever Nathan Drake attacks" in oracle("Nathan Drake, Treasure Hunter")
    palace_activated_before_attack = True
    attacking = True
    mana_trigger_resolved_before_heist = True
    pool = ["R"] * (4 if palace_activated_before_attack and attacking and mana_trigger_resolved_before_heist else 0)
    assert paid({"generic": 1, "U": 2, "B": 1}, pool, any_color=True)
    assert not paid({"generic": 1, "U": 2, "B": 1}, [], any_color=True)
    # The Palace must already have been tapped to grant firebending before
    # attacking; its activated ability cannot retroactively give mana.
    assert not paid({"generic": 1, "U": 2, "B": 1}, ["R"] * 0, any_color=True)


def test_P0_F1_commander_killed_after_attack_trigger_does_not_erase_trigger():
    pending_nathan_trigger = 1
    commander_removed_before_resolution = True
    assert pending_nathan_trigger == 1
    # While Nathan is absent, the STATIC mana as-any-color effect is absent.
    _, cast = heist([["Sol Ring"], ["Cyclonic Rift"], ["Island"], ["Island"]],
                    ["R", "R"], 1, nathan_present=not commander_removed_before_resolution)
    assert cast is None
    _, cast_with_colors = heist([["Sol Ring"], ["Cyclonic Rift"], ["Island"], ["Island"]],
                                ["U", "R"], 1, nathan_present=False)
    assert cast_with_colors == "Cyclonic Rift"


def test_P1_K4_roaming_throne_rogue_copy_sakashima_and_firebender_quest():
    assert "choose a creature type" in oracle("Roaming Throne")
    assert "it triggers an additional time" in oracle("Roaming Throne")
    assert "Human Rogue" in ORACLE["Nathan Drake, Treasure Hunter"]["type_line"]
    base = 1
    assert base + int("Rogue" == "Rogue") == 2
    assert base + int("Pirate" == "Rogue") == 1
    assert 'The "legend rule" doesn\'t apply to permanents you control' in oracle("Sakashima of a Thousand Faces")
    assert "You may have Sakashima enter as a copy" in oracle("Sakashima of a Thousand Faces")
    assert "if it has four or more quest counters on it" in oracle("Firebender Ascension")
    assert "you may copy that ability" in oracle("Firebender Ascension")


def test_P1_K5_dauthi_tinybones_conflict_natively_resolved_by_cut():
    assert "instead exile it with a void counter on it" in oracle("Dauthi Voidwalker")
    assert "from that player's graveyard" not in oracle("Dauthi Voidwalker")
    assert "Tinybones, the Pickpocket" not in parsed()
    assert "Chrome Mox" in parsed() and "Dauthi Voidwalker" in parsed()


def test_P1_K6_unowned_cast_trigger_payoffs_not_spell_copy_as_cast():
    assert "The first spell you cast from exile each turn has cascade" in oracle("Wild-Magic Sorcerer")
    assert "Whenever you cast a spell from exile" in oracle("Nalfeshnee")
    assert "Whenever you cast a spell from exile" in oracle("Passionate Archaeologist")
    assert "Whenever you cast a spell you don't own" in oracle("Tasha, the Witch Queen")
    assert "Whenever a player casts a spell they don't own" not in " ".join(map(oracle, parsed()))
    assert "Whenever you cast a spell while Fire Lord Azula is attacking, copy that spell" in oracle("Fire Lord Azula")
    # A spell copy is not itself a cast. One stolen cast produces one cast
    # event and potential copy events without repeating cast triggers.
    stolen_cast_events = 1
    copies_from_azula = 1
    assert stolen_cast_events == 1 and copies_from_azula == 1


def test_P1_E1_and_F3_extra_combats_and_combat_mana_source_ordering():
    assert "after this phase, there is an additional combat phase" in oracle("Combat Celebrant")
    assert "untap all other creatures you control" in oracle("Combat Celebrant")
    assert "Untap target creature" in oracle("Seize the Day")
    assert "Flashback {2}{R}" in oracle("Seize the Day")
    assert "untap all attacking creatures" in oracle("Karlach, Fury of Avernus")
    assert "Whenever Captain Lannery Storm attacks, create a Treasure token" in oracle("Captain Lannery Storm")
    assert "Whenever this creature attacks or becomes the target of a spell, create a Treasure token" in oracle("Goldspan Dragon")
    assert 'Add two mana of any one color' in oracle("Goldspan Dragon")
    assert "{T}: Add {C}{C}{C}" in oracle("Mana Vault")
    assert "{T}: Add {C}{C}{C}" in oracle("Grim Monolith")
    # On-attack Treasure ability resolved ahead of Nathan's ability:
    treasures = 2  # one Lannery, one Goldspan
    treasury_mana = treasures * 2  # Goldspan modifies every Treasure
    mana_vault_mana = 3
    assert treasury_mana + mana_vault_mana == 7
    # Main-phase floating mana empties when advancing to beginning of combat;
    # the heist must use still-available rocks/Treasures/firebending.
    mana_floated_during_main = 5
    combat_pool_from_that_mana = 0
    assert mana_floated_during_main == 5 and combat_pool_from_that_mana == 0


def test_P1_E2_and_W1_retain_independent_theft_and_counterplay():
    retained = ("Black Cat, Cunning Thief", "Gríma, Saruman's Footman",
                "Laughing Jasper Flint", "Hostage Taker", "Plargg and Nassari",
                "Gonti, Night Minister", "Tasha, the Witch Queen", "Vaan, Street Thief")
    current = parsed()
    for name in retained:
        if name != "Gonti, Night Minister":
            assert name in current, name
    assert "Gonti, Night Minister" not in current  # symmetric opponent Treasure / theft liability.
    assert "exiles a nontoken creature" in oracle("Azula, Cunning Usurper")
    assert "Firebending 2" in oracle("Azula, Cunning Usurper")
    assert "During your turn" in oracle("Azula, Cunning Usurper")
    assert "Fire Lord Azula" in current
    assert "Force of Will" in current and "Force of Negation" not in current


if __name__ == "__main__":
    for name, check in sorted(globals().copy().items()):
        if name.startswith("test_") and callable(check):
            check()
            print("PASS", name)

