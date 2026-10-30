#!/usr/bin/env python3
"""Offline audit of the UNAPPROVED Phase 6 Pilot 1 (Ugin & Nicol Bolas duality).

Replays the committed proposal, decklist, Archidekt import and printing evidence:
100 cards, singleton, UBR identity, recorded Commander legality, tier discipline,
official-source provenance, Pack A grade preservation and decklist SHA-256.
It does not re-fetch Scryfall; the dated snapshot hash is recorded in the files.
"""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
D = ROOT / "data/lore_decks/drafts"
STEM = "ugin_bolas_elder_dragon_duality"
PROPOSAL, EVIDENCE = D / f"{STEM}_proposal.json", D / f"{STEM}_printing_evidence.json"
DECK, IMPORT = D / f"{STEM}_decklist.txt", D / f"{STEM}_archidekt_import.txt"
PACK_A = ROOT / "data/lore_research/pack_a_ugin_bolas_evidence_2026-10-30.json"
PACK_A2 = ROOT / "data/lore_research/pack_a_elder_dragon_war_extension_2026-10-30.json"
PACK_A4 = ROOT / "data/lore_research/pack_a4_printing_art_matches_2026-10-30.json"
UUID = re.compile(r"^[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$")
TIERS = ("DIRECT_DEPICTION", "CANON_REFERENCE", "LORE_INSPIRED", "MECHANICAL_SYMBOL")
LINE = re.compile(r"^(\d+)x (.+?)(?: \(([a-z0-9]+)\) (\S+))?( \[Commander\])?$")
FORBIDDEN_STATUS = re.compile(r"\b(APPROVED|LOCKED|CERTIFIED)\b")


def parse(text):
    rows = []
    for raw in text.splitlines():
        m = LINE.match(raw)
        if not m:
            raise ValueError("bad decklist line: " + raw)
        rows.append((int(m[1]), m[2], m[3], m[4], bool(m[5])))
    return rows


def build():
    spec = json.loads(PROPOSAL.read_text(encoding="utf-8"))
    ev = json.loads(EVIDENCE.read_text(encoding="utf-8"))
    deck_text = DECK.read_text(encoding="utf-8")
    sha = hashlib.sha256(deck_text.encode()).hexdigest()
    if not (spec["raw_decklist_sha256"] == ev["raw_sha256"] == sha):
        raise ValueError("decklist SHA-256 mismatch")
    status = spec["status"]
    if not status.startswith("UNAPPROVED") or FORBIDDEN_STATUS.search(status.replace("not approved", "").replace("not locked", "").replace("not certified", "")):
        raise ValueError("pilot must stay UNAPPROVED")
    if any(spec["approval"][k] for k in ("approved", "locked", "certified")):
        raise ValueError("approval flags must all be false")

    rows = parse(deck_text)
    total = sum(r[0] for r in rows)
    commanders = [r for r in rows if r[4]]
    named = [r for r in rows if r[2]]
    if total != 100 or len(commanders) != 1 or not rows[0][4]:
        raise ValueError("need exactly 100 cards with the commander first")
    if any(r[0] != 1 for r in named) or len({r[1] for r in named}) != len(named):
        raise ValueError("singleton violated")
    basics = {r[1]: r[0] for r in rows if not r[2]}
    if set(basics) - {"Island", "Swamp", "Mountain"} or basics != spec["basics"]:
        raise ValueError("basics mismatch")

    cards = ev["cards"]
    if [c["name"] for c in cards] != [r[1] for r in named]:
        raise ValueError("evidence order/names differ from decklist")
    a4 = {c["name"]: c for c in json.loads(PACK_A4.read_text())["cards"]}
    grades = {c["id"]: c["grade"] for c in json.loads(PACK_A.read_text())["claims"]}
    grades.update({c["id"]: c["grade"] for c in json.loads(PACK_A2.read_text())["claims"]})
    seen_ids, tiers, gcs = set(), {t: 0 for t in TIERS}, []
    for c, r in zip(cards, named):
        p = c["printing"]
        if (p["set"], p["collector_number"]) != (r[2], r[3]):
            raise ValueError("printing mismatch: " + c["name"])
        if not (UUID.fullmatch(p["id"]) and UUID.fullmatch(p["oracle_id"] or "")) or p["id"] in seen_ids:
            raise ValueError("bad or duplicate printing UUID: " + c["name"])
        seen_ids.add(p["id"])
        if p["commander_legality"] != "legal" or not set(p["color_identity"]) <= set("UBR"):
            raise ValueError("illegal or off-identity: " + c["name"])
        if c["tier"] not in TIERS:
            raise ValueError("unknown tier: " + c["name"])
        tiers[c["tier"]] += 1
        if p["game_changer"]:
            gcs.append(c["name"])
        if c["tier"] == "MECHANICAL_SYMBOL":
            if c["beat"] != "playability":
                raise ValueError("mechanical card outside playability: " + c["name"])
            continue
        src = c["source"]
        if c["source_id"] == "scryfall_card_text":
            if c["tier"] == "DIRECT_DEPICTION":
                raise ValueError("printed text alone cannot prove a depiction: " + c["name"])
            if c["tier"] == "CANON_REFERENCE" and not (p["printed_flavor"] or "Bolas" in c["name"] or "Ugin" in c["name"]):
                raise ValueError("CANON_REFERENCE by card text needs printed flavor or a canon name: " + c["name"])
        elif not src.startswith("https://magic.wizards.com/"):
            raise ValueError("non-official story source: " + c["name"])
        if c["tier"] == "DIRECT_DEPICTION" and c["name"] in a4 and a4[c["name"]]["context_tier"] != "DIRECT_EVENT_SCENE_CAPTION":
            raise ValueError("A4 tier inflated: " + c["name"])
        if c["name"] in a4 and p["illustration_id"] != a4[c["name"]]["matched_illustration_id"]:
            raise ValueError("A4 exact-art printing not used: " + c["name"])
        for cid in c["pack_a_claims"]:
            if grades.get(cid) != "CANON_CONFIRMED":
                raise ValueError(f"{c['name']} leans on non-confirmed claim {cid}")
    if tiers != spec["counts"]["tiers"]:
        raise ValueError("tier counts drift")
    if len(gcs) > 3:
        raise ValueError("more than three Game Changers (bracket 3 ceiling)")

    imp = IMPORT.read_text(encoding="utf-8").splitlines()
    if imp[0] != "1x " + rows[0][1].split(" // ")[0] or len(imp) != len(rows):
        raise ValueError("Archidekt import must be commander-first and mirror the decklist")
    tags = spec["archidekt_tags"]
    if len(tags) != 3 or len(set(tags)) != 3:
        raise ValueError("need three distinct Archidekt tags")
    return {"result": "PASS", "status": status, "total": total, "named": len(named),
            "basics": sum(basics.values()), "tiers": tiers, "game_changers": gcs,
            "decklist_sha256": sha, "snapshot": spec["snapshot"]["id"],
            "realtime_fetch": False}


if __name__ == "__main__":
    print(json.dumps(build(), indent=1))
