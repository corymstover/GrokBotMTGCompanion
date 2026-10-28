#!/usr/bin/env python3
"""Source integrity for Deck #60 M7 RESEARCH ONLY, never an owner-ready gate.

Card legality and Oracle identity are checked against the engineering
2026-10-15 Scryfall-derived frozen index.  This is NOT a fresh October 27
100-name lookup, source-verified P1 execution, M7 decision-gate execution,
nor owner approval. The MBC commander is project-only until 2026-11-13.
"""
from __future__ import annotations

import collections
import csv
import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
BASE = HERE / "Tresserhorn_Returned_Oct15_baseline.txt"
CAND = ROOT / "data/grixis/m7/candidate_lists/Tresserhorn_s_Lord__Returned_M7_Rev1_RESEARCH.txt"
ALT5 = ROOT / "data/grixis/m7/candidate_lists/Tresserhorn_s_Lord__Returned_M7_Rev1_alt5.txt"
ALT9 = ROOT / "data/grixis/m7/candidate_lists/Tresserhorn_s_Lord__Returned_M7_Rev1_alt9.txt"
REVIEW = ROOT / "data/grixis/m7/decision_reviews/Tresserhorn_s_Lord__Returned_M7_Rev1_RESEARCH.md"
INDEX = ROOT / "data/card_index.csv"
ORIGINAL_SHA = "8c802586a4742156fb96246f4f23331eb51d1a77d6717da63ceed2446e98adf8"
MAIN_SHA = "9a9d2f7a344e2491444c0a0e4c48525dfe8faa37032eaf8e22a94082f6fbf60e"
ALT5_SHA = "a57de231aba0bce4b9b194e3dd466e40a466375259dc615b454ea02f10a5f113"
ALT9_SHA = "5d2991dda31f00d4099185de8b791e0da1a057eb4ebb6d5e0dcc32648eb96b4d"
COMMANDER = "Tresserhorn's Lord, Returned"
EXPECTED_ADDS = {
    "Genesis Chamber", "Sengir Autocrat", "Deflecting Swat",
    "Fierce Guardianship", "Song of Totentanz", "The Meathook Massacre",
    "Agadeem's Awakening // Agadeem, the Undercrypt",
}
EXPECTED_CUTS = {
    "Dark Ritual", "Endrek Sahr, Master Breeder", "Village Rites",
    "Stubborn Denial", "Tempt with Vengeance", "Blasphemous Edict",
}


def deck(path: Path):
    data = path.read_bytes()
    assert data.endswith(b"\n"), "LF-terminated source required"
    assert b"\r" not in data, "CRLF source not permitted"
    names = []
    for i, line in enumerate(data.decode("utf-8").splitlines()):
        m = re.fullmatch(r"(\d+)x (.+)", line)
        assert m, (i, line)
        qty, name = int(m[1]), m[2]
        if i == 0:
            assert name == COMMANDER + " [Commander]", name
            assert qty == 1
        else:
            assert "[Commander]" not in name, name
        names.extend([name.removesuffix(" [Commander]")] * qty)
    assert len(names) == 100, len(names)
    counts = collections.Counter(names)
    assert all(v == 1 or k in {"Island", "Mountain", "Swamp"}
               for k, v in counts.items()), counts
    return names, hashlib.sha256(data).hexdigest()


def main():
    base, original_sha = deck(BASE)
    final, sha = deck(CAND)
    conservative, alt5_sha = deck(ALT5)
    aggressive, alt9_sha = deck(ALT9)
    assert original_sha == ORIGINAL_SHA
    assert sha == MAIN_SHA
    assert alt5_sha == ALT5_SHA
    assert alt9_sha == ALT9_SHA
    review = REVIEW.read_text(encoding="utf-8")
    for exact_sha in (ORIGINAL_SHA, MAIN_SHA, ALT5_SHA, ALT9_SHA):
        assert exact_sha in review, f"unbound SHA in review: {exact_sha}"
    before, after = collections.Counter(base), collections.Counter(final)
    added, removed = after - before, before - after
    assert set(added) == EXPECTED_ADDS, added
    assert set(removed) == EXPECTED_CUTS | {"Swamp"}, removed
    assert all(n == 1 for n in added.values())
    assert all(n == 1 for n in removed.values())
    assert len(added) == len(removed) == 7
    assert after["Swamp"] == 3
    assert collections.Counter(conservative) == (after - collections.Counter(
        {"Sengir Autocrat": 1, "Deflecting Swat": 1}) + collections.Counter(
        {"Endrek Sahr, Master Breeder": 1, "Village Rites": 1}))
    assert collections.Counter(aggressive) == (after - collections.Counter(
        {"Mountain": 1, "Nightscape Familiar": 1}) + collections.Counter(
        {"Kazuul's Fury // Kazuul's Cliffs": 1, "Pawn of Ulamog": 1}))
    with INDEX.open(newline="", encoding="utf-8") as f:
        index = {row["name"]: row for row in csv.DictReader(f)}
    for label, names in (("baseline", base), ("main7", final),
                         ("alt5", conservative), ("alt9", aggressive)):
        assert all(n in index for n in names), (label, [n for n in names if n not in index])
        for n in names:
            info = index[n]
            assert info["oracle_id"] and info["shard"], (label, n)
            # This frozen catalog encodes colorless as 'C', not the empty
            # set; colorless is valid in a UBR Commander deck.
            assert set(info["color_identity"]) <= set("UBRC"), (label, n, info["color_identity"])
            if n == COMMANDER:
                assert info["commander_legality"] == "not_legal"
            else:
                assert info["commander_legality"] == "legal", (label, n, info["commander_legality"])
    assert after[COMMANDER] == 1
    # Board count: 32 front-face Land cards plus two spell/land modal cards.
    front_lands = sum(q for n, q in after.items()
                      if "Land" in index[n]["type_line"].split(" // ")[0])
    mdfc_lands = sum(q for n, q in after.items()
                     if " // Land" in index[n]["type_line"])
    assert front_lands == 32, front_lands
    assert mdfc_lands == 2, mdfc_lands
    print("Deck #60 candidate: RESEARCH_ONLY_NOT_OWNER_READY")
    print("Approved source SHA-256:", original_sha)
    print("Research 7-swap SHA-256:", sha)
    print("Alt5 SHA-256:", alt5_sha, "| Alt9 SHA-256:", alt9_sha)
    print("Physical: 100; names:", len(after),
          "; front lands:", front_lands, "; land MDFCs:", mdfc_lands)
    print("Frozen October 15 Oracle/singleton/UBR for baseline and all alternatives: PASS")
    print("Official Commander legality: PENDING RELEASE 2026-11-13")
    print("Fresh full Oracle and M6 P1/IJ/M7 CI: NOT CERTIFIED")


if __name__ == "__main__":
    main()
