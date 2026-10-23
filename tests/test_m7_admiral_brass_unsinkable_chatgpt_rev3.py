"""Independent exact-byte Admiral Brass, Unsinkable ChatGPT M7 Rev3 checks.

Rev2 remains preserved on PR #651. This is a *separate unapproved owner
candidate*, not a canonical deck, and tests prove structure/source assertions,
not multiplayer wins or strategic optimality.
"""
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = ROOT / "data/grixis/m7/candidate_lists/Admiral_Brass__Unsinkable_ChatGPT_Rev3.txt"
BASELINE = ROOT / "data/grixis/m7/baseline_sources/Admiral_Brass__Unsinkable_approved_source_2026-10-13.txt"
REV2_ORACLE = ROOT / "data/grixis/m6/oracle_snapshots/Admiral_Brass__Unsinkable_M7_rev2_Scryfall_20261023.json"
NEW_ORACLE = ROOT / "data/grixis/m7/research_challengers/Admiral_Brass__Unsinkable_ChatGPT_Rev3_new_card_oracle.json"
EXPECTED_SHA256 = "dfa192cce0d925621e1cfa3f6444fb9da04c995700ca886e95a75c7347d4c7f7"
BASELINE_SHA256 = "056f0369bc4b11967365eef65d15a806b2d0f673ecf8097b028ffcdfd472f5cc"
ADDS = {
    "Kitesail Larcenist", "Timestream Navigator", "Warkite Marauder",
    "Jhoira, Weatherlight Corsair", "Siren's Ruse", "Ripples of Undeath",
    "Thassa, Deep-Dwelling", "City of Brass",
}
CUTS = {
    "Enterprising Scallywag", "Francisco, Fowl Marauder",
    "Fathom Fleet Captain", "Pitiless Plunderer",
    "Crumbling Necropolis", "Forerunner of the Coalition",
    "Wonder", "Path of Ancestry",
}
ROCKS = {
    "Sol Ring", "Arcane Signet", "Dimir Signet", "Izzet Signet",
    "Rakdos Signet", "Talisman of Creativity", "Talisman of Dominance",
    "Talisman of Indulgence",
}


def _cards(path):
    counts = Counter()
    lines = path.read_text(encoding="utf-8").splitlines()
    for index, line in enumerate(lines):
        qty, sep, name = line.partition("x ")
        assert sep and qty.isdigit() and name.strip() == name, line
        if index == 0:
            assert name == "Admiral Brass, Unsinkable [Commander]"
            name = name.replace(" [Commander]", "")
        else:
            assert "[Commander]" not in name and "[Companion]" not in name
        if name == "Brass's Tunnel-Grinder":
            name = "Brass's Tunnel-Grinder // Tecutlan, the Searing Rift"
        counts[name] += int(qty)
    return counts


def _oracle():
    prior = json.loads(REV2_ORACLE.read_text(encoding="utf-8"))
    extra = json.loads(NEW_ORACLE.read_text(encoding="utf-8"))
    return {row["name"]: row for row in (prior["cards"] + extra["cards"])}


def test_exact_bytes_and_eight_real_swaps():
    assert hashlib.sha256(CANDIDATE.read_bytes()).hexdigest() == EXPECTED_SHA256
    assert hashlib.sha256(BASELINE.read_bytes()).hexdigest() == BASELINE_SHA256
    base, new = _cards(BASELINE), _cards(CANDIDATE)
    assert sum(base.values()) == sum(new.values()) == 100
    assert len(new) == 97
    assert all(q == 1 or (n in {"Island", "Mountain", "Swamp"} and q == 2)
               for n, q in new.items())
    assert set(new) - set(base) == ADDS
    assert set(base) - set(new) == CUTS
    assert "Faithless Looting" in base and "Faithless Looting" in new
    assert "Power Conduit" in new and "Changeling Outcast" in new


def test_oracle_color_identity_official_legality_and_shape():
    cards, oracle = _cards(CANDIDATE), _oracle()
    assert not (set(cards) - set(oracle)), set(cards) - set(oracle)
    assert all(row["commander_legality"] == "legal"
               for n, row in oracle.items() if n in cards)
    assert all(set(oracle[n]["color_identity"]) <= {"U", "B", "R"}
               for n in cards)
    assert sum(q for n, q in cards.items()
               if "Land" in oracle[n]["type_line"].split(" // ")[0]) == 33
    assert sum(cards.get(n, 0) for n in ROCKS) == 8
    assert sum(q for n, q in cards.items()
               if "Pirate" in oracle[n]["type_line"] or n == "Changeling Outcast") == 28
    assert not oracle["Brass's Tunnel-Grinder // Tecutlan, the Searing Rift"][
        "type_line"
    ].split(" // ")[0].endswith("Land")
    assert oracle["Thassa, Deep-Dwelling"]["color_identity"] == ["U"]
    assert oracle["City of Brass"]["color_identity"] == []


def test_new_interactions_are_card_text_bound():
    oracle = _oracle()
    thassa = oracle["Thassa, Deep-Dwelling"]["oracle_text"]
    assert "beginning of your end step" in thassa
    assert "return that card to the battlefield under your control" in thassa
    assert "Indestructible" in thassa
    assert "Flashback {2}{R}" in oracle["Faithless Looting"]["oracle_text"]
    assert "beginning of your first main phase" in oracle["Ripples of Undeath"]["oracle_text"]
    assert "gain control of target creature until end of turn" in oracle["Coercive Recruiter"]["oracle_text"]
    assert "Return that creature to its owner's hand" in oracle["Zara, Renegade Recruiter"]["oracle_text"]
    assert "mill four cards" in oracle["Admiral Brass, Unsinkable"]["oracle_text"]
    assert "Remove a counter from a permanent you control" in oracle["Power Conduit"]["oracle_text"]
    # The new-object/finality and temporary-steal rulings are independently
    # documented in the separate review packet and Wizards THB release notes.
