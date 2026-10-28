"""Deterministic Deck #38 Missy M7 Rev1, current-Oracle-backed focused checks.

These are finite structural/rules assertions, not multiplayer simulation or
independent acceptance of the full historical M6 I/J certification suite.
"""
import collections
import hashlib
import json
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent if (HERE.parent / "data/grixis/m7").exists() else HERE
CANDIDATE = ROOT / "data/grixis/m7/candidate_lists/Missy_chatgpt_rev1.txt"
SNAPSHOT = ROOT / "data/grixis/m7/oracle_snapshots/Missy_Rev1_Scryfall_20261026.json"
if not CANDIDATE.exists():
    CANDIDATE = ROOT / "Missy_M7_Rev1_Approval_Candidate_2026-10-26.txt"
if not SNAPSHOT.exists():
    SNAPSHOT = ROOT / "Missy_Rev1_Scryfall_20261026.json"

RAW = CANDIDATE.read_bytes()
LINES = RAW.decode("utf-8").splitlines()
MATCHES = [re.fullmatch(r"(\d+)x (.+?)(?: \[Commander\])?", line) for line in LINES]
assert all(MATCHES)
QUANTITIES = collections.Counter()
for match in MATCHES:
    QUANTITIES[match.group(2)] += int(match.group(1))
SOURCE = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
ORACLE = {card["name"]: card for card in SOURCE["cards"]}

ADDITIONS = {
    "Altar of the Brood", "Carrion Feeder", "Cavern of Souls", "Chrome Mox",
    "Deflecting Swat", "Fierce Guardianship", "Gift of Doom", "Goblin Sharpshooter",
    "Grim Monolith", "Marsh Flats", "Misty Rainforest", "Yawgmoth, Thran Physician",
}
CUTS = {
    "Aphetto Runecaster", "Ashad, the Lone Cyberman", "Bane of the Living",
    "Cybermen Squadron", "Cybership", "Doomsday Confluence",
    "Dragonskull Summit", "Drowned Catacomb", "Etrata, Deadly Fugitive",
    "Inventors' Fair", "Their Name Is Death", "Ugin's Mastery",
}


def oracle(name):
    return ORACLE[name]["oracle_text"]


def test_exact_bytes_100_singleton_and_12_replacements():
    assert hashlib.sha256(RAW).hexdigest() == "f3f8ffa671cef5df9612a52ab0a5003931f2b71110f6d7fef45906b4f052f83d"
    assert LINES[0] == "1x Missy [Commander]"
    assert sum(QUANTITIES.values()) == 100
    assert len(QUANTITIES) == 97
    assert {name: qty for name, qty in QUANTITIES.items() if qty > 1} == {"Island": 2, "Swamp": 3}
    assert len(ADDITIONS) == len(CUTS) == 12
    assert ADDITIONS <= set(QUANTITIES)
    assert not (CUTS & set(QUANTITIES))


def test_current_scryfall_source_97_of_97_and_ubr_legality():
    assert SOURCE["candidate_sha256"] == hashlib.sha256(RAW).hexdigest()
    assert set(ORACLE) == set(QUANTITIES)
    for card in ORACLE.values():
        assert card["commander_legality"] == "legal", card["name"]
        assert set(card["color_identity"]) <= {"U", "B", "R"}, card["name"]
    lands = sum(
        qty for name, qty in QUANTITIES.items()
        if "Land" in ORACLE[name]["type_line"]
        or any("Land" in f["type_line"] for f in ORACLE[name]["faces"])
    )
    assert lands == 35


def test_missy_conversion_identity_and_no_artifact_self_recycling():
    text = oracle("Missy")
    assert "another nonartifact creature dies" in text
    assert "face down and tapped" in text
    assert "2/2 Cyberman artifact creature" in text
    assert "At the beginning of your end step" in text
    # Converted face-down creatures are artifacts; they must be turned up
    # (or otherwise cease to be artifacts) to trigger Missy on a later death.
    for name in ("Ruthless Ripper", "Dragon's Eye Savants", "Horde Ambusher"):
        assert "Morph" in oracle(name), name
        assert "Reveal a " in oracle(name), name
        assert "Creature" in ORACLE[name]["type_line"]
        assert "Artifact" not in ORACLE[name]["type_line"]


def test_exact_non_mana_morph_and_loop_payoffs():
    assert "Morph—Reveal a black card" in oracle("Ruthless Ripper")
    assert "Morph—Reveal a blue card" in oracle("Dragon's Eye Savants")
    assert "Morph—Reveal a red card" in oracle("Horde Ambusher")
    for outlet in ("Altar of Dementia", "Ashnod's Altar", "Phyrexian Altar",
                   "Goblin Bombardment", "Viscera Seer", "Carrion Feeder"):
        assert outlet in QUANTITIES
    assert "Sacrifice a creature:" in oracle("Carrion Feeder")
    assert "Whenever another permanent you control enters" in oracle("Altar of the Brood")
    assert "each opponent mills a card" in oracle("Altar of the Brood")
    assert "Whenever an artifact you control enters" in oracle("Reckless Fireweaver")
    assert "Whenever a face-down creature you control enters" in oracle("They Came from the Pipes")
    # Savants has printed power 0: a Savants / Altar of Dementia loop
    # alone does *not* mill, but Brood will mill after each return.
    assert "Dragon's Eye Savants" in QUANTITIES


def test_sacrifice_board_control_protection_and_caveats():
    assert "Pay 1 life, Sacrifice another creature" in oracle("Yawgmoth, Thran Physician")
    assert "draw a card" in oracle("Yawgmoth, Thran Physician")
    # The life payment means Yawgmoth is not a free unlimited outlet
    # without an additional life-gain engine; no such claim is made.
    assert "Whenever a creature dies, untap" in oracle("Goblin Sharpshooter")
    assert "deals 1 damage to any target" in oracle("Goblin Sharpshooter")
    assert "Morph—Sacrifice another creature" in oracle("Gift of Doom")
    assert "indestructible" in oracle("Gift of Doom")
    assert "If you control a commander" in oracle("Fierce Guardianship")
    assert "If you control a commander" in oracle("Deflecting Swat")
    assert "Destroy all nonartifact creatures" not in oracle("Delete")
    assert "each nonartifact creature" in oracle("Delete")


def test_preserves_cybermen_and_commander_specific_core():
    for retained in (
        "The Cyber-Controller", "The Valeyard", "Death in Heaven",
        "Cyberman Patrol", "The Master, Gallifrey's End",
        "They Came from the Pipes", "Cyber Conversion", "Delete",
        "Panoptic Projektor", "Ixidor, Reality Sculptor", "Skirk Alarmist",
        "Grave Pact", "Plaguecrafter", "Accursed Marauder",
        "Pyrotechnic Performer", "Reckless Fireweaver", "Zulaport Cutthroat",
    ):
        assert retained in QUANTITIES, retained
    assert "If an opponent would face a villainous choice" in oracle("The Valeyard")
    assert "artifact creatures you control" in oracle("The Cyber-Controller")
    assert "Turn target face-down creature you control face up" in oracle("Skirk Alarmist")
    assert "The next face-down creature spell" in oracle("Panoptic Projektor")


if __name__ == "__main__":
    for name, check in sorted(globals().copy().items()):
        if name.startswith("test_") and callable(check):
            check()
            print("PASS", name)

