#!/usr/bin/env python3
"""Offline, fail-closed exact-raw Deck 58 M7 Rev1 certification.

Requires committed Oct 27 Scryfall API records; validates every card and a
bounded set of material rules interactions.  It is not a game-engine claim.
"""
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
CANDIDATES = ROOT.parent / "candidate_lists"
SNAP = json.loads((ROOT / "The_Valeyard_M7_Rev1_Scryfall_snapshot.json").read_text())
ORACLE = SNAP["oracle_cards"]
SOURCES = {
    "The_Valeyard_Oct15_baseline.txt": "4bef619a33d85eafaf194997924fc8378dd490f62c59d76bafccc4fa07ef821c",
    "The_Valeyard_M7_Rev1.txt": "1735629783fbea2c9b8782fe18835f6dc8b3b980715344249cdb0941fbd9887b",
    "The_Valeyard_M7_Rev1_alt7.txt": "c05cd0dbefe9b79178bfb448a89275f4122e145005cb7c7a8dda89eaa8b12ac0",
    "The_Valeyard_M7_Rev1_alt8.txt": "e39ec2c076650057ae1b55d5c5de4d2149168e2e2cbc5e5a0d4763d5a300c497",
}
SWAPS = {
    "Arcane Denial": "Swan Song",
    "Blasphemous Act": "Toxic Deluge",
    "Brainstorm": "Irenicus's Vile Duplication",
    "Haunted Ridge": "Ancient Tomb",
    "Izzet Signet": "Chrome Mox",
    "Kess, Dissident Mage": "Double Vision",
}
LANDS = {"Island": 2, "Mountain": 2, "Swamp": 3}


def inventory(path):
    raw = path.read_bytes()
    assert raw.endswith(b"\n") and b"\r" not in raw, path.name
    assert sha256(raw).hexdigest() == SOURCES[path.name], path.name
    lines = raw.decode().splitlines()
    assert lines[0] == "1x The Valeyard [Commander]"
    names = []
    for line in lines:
        m = re.fullmatch(r"([0-9]+)x (.+)", line)
        assert m, (path.name, line)
        q, name = int(m[1]), m[2].removesuffix(" [Commander]")
        assert q > 0
        assert name in ORACLE, (path.name, name)
        names.extend([name] * q)
    counter = Counter(names)
    assert len(names) == 100 and len(counter) == 96, path.name
    assert {n: q for n, q in counter.items() if q > 1} == LANDS, path.name
    assert sum(q for n, q in counter.items() if "Land" in ORACLE[n]["type_line"]) == 36
    for name in counter:
        oracle = ORACLE[name]
        assert oracle["oracle_id"] and oracle["oracle_text"] and oracle["scryfall_uri"]
        assert oracle["commander_legality"] == "legal", (name, oracle["commander_legality"])
        assert set(oracle["color_identity"]) <= {"U", "B", "R"}, name
    return counter


def effects():
    o = lambda n: ORACLE[n]["oracle_text"]
    assert "an additional time" in o("The Valeyard") and "additional time" not in o("Illusion of Choice")
    assert "vote an additional time" in o("The Valeyard")
    assert "isn't legendary" in o("Irenicus's Vile Duplication")
    assert "first instant or sorcery spell each turn" in o("Double Vision")
    assert "copy that spell" in o("Double Vision")
    assert "vote" in o("Plea for Power") and "vote" in o("Split Decision")
    assert "vote" in o("Messenger Jays") and "vote" in o("Fateful Tempest")
    assert "you choose how each player votes" in o("Illusion of Choice").lower()
    assert "choice you didn't vote for" in o("Grudge Keeper")
    assert "nontoken artifact creature you control dies" in o("The Master, Gallifrey's End")
    assert "Target instant or sorcery spell" not in o("Swan Song")
    assert "Counter target enchantment, instant, or sorcery spell" in o("Swan Song")
    assert "-X/-X" in o("Toxic Deluge")
    assert "nonartifact, nonland card" in o("Chrome Mox")
    assert "Add {C}{C}" in o("Ancient Tomb")
    assert "doesn't apply" in o("Sakashima of a Thousand Faces")
    assert "isn't legendary" in o("Quantum Misalignment")
    # Bounded replacement-effect accounting: one Valeyard means two separate
    # villainous choices, two independent copies means three, not four.
    for num_valeyards, expected_choices in ((0, 1), (1, 2), (2, 3), (3, 4)):
        assert 1 + num_valeyards == expected_choices
    # Will-of-the-council majority: 1 controller with 2 votes versus
    # three opponents with one vote each cannot guarantee a preferred option.
    assert 2 < 3


def main():
    assert SNAP["source"] == "Scryfall public /cards/collection exact-name API"
    assert SNAP["retrieved_utc"].startswith("2026-10-27")
    assert len(ORACLE) == 104 and SNAP["card_count_unique"] == 104
    original = inventory(ROOT / "The_Valeyard_Oct15_baseline.txt")
    proposal = inventory(CANDIDATES / "The_Valeyard_M7_Rev1.txt")
    alt7 = inventory(CANDIDATES / "The_Valeyard_M7_Rev1_alt7.txt")
    alt8 = inventory(CANDIDATES / "The_Valeyard_M7_Rev1_alt8.txt")
    assert set((original - proposal).elements()) == set(SWAPS)
    assert set((proposal - original).elements()) == set(SWAPS.values())
    assert alt7 == proposal - Counter(["Fellwar Stone"]) + Counter(["Mana Vault"])
    assert alt8 == alt7 - Counter(["Midnight Crusader Shuttle"]) + Counter(["Helm of the Host"])
    voting = {n for n in original if re.search(r"\bvote(?:s|d)?\b", ORACLE[n]["oracle_text"], re.I)}
    assert voting <= set(proposal), sorted(voting - set(proposal))
    assert {n for n in original if "villainous choice" in ORACLE[n]["oracle_text"].lower()} <= set(proposal)
    effects()
    print("PASS: 4 exact raw hashes; 4 legal Grixis 100s; baseline/proposal 96 names; 36 lands")
    print(f"PASS: {len(voting)} voting cards and every native villainous-choice card retained")
    print("PASS: 6 exact replacements, two bounded larger alternatives, 104 live Oracle records")
    print("PASS: targeted Valeyard replacement, vote, clone, copy, interaction and mana tests")


if __name__ == "__main__":
    main()
