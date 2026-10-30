#!/usr/bin/env python3
"""Offline, spec-driven audit of UNAPPROVED Phase 6 lore-pilot proposals.

For each spec in data/lore_decks/specs/ (or the --spec given), it replays the committed
proposal, decklist, Archidekt import and printing evidence and checks:
- 100 cards, singleton, the commander first, colour identity, recorded Commander legality;
- tier discipline and official-source provenance;
- claim-grade preservation and the Game Changer ceiling;
- decklist SHA-256, and that the files mirror the spec's card order.
It does not re-fetch Scryfall; the dated snapshot hash is recorded in the files.
"""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPECS = ROOT / "data/lore_decks/specs"
DRAFTS = ROOT / "data/lore_decks/drafts"
UUID = re.compile(r"^[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$")
TIERS = ("DIRECT_DEPICTION", "CANON_REFERENCE", "LORE_INSPIRED", "MECHANICAL_SYMBOL")
LINE = re.compile(r"^(\d+)x (.+?)(?: \(([a-z0-9]+)\) (\S+))?( \[Commander\])?$")
FORBIDDEN_STATUS = re.compile(r"\b(APPROVED|LOCKED|CERTIFIED)\b")
BASIC_FOR = {"W": "Plains", "U": "Island", "B": "Swamp", "R": "Mountain", "G": "Forest"}


def parse(text):
    rows = []
    for raw in text.splitlines():
        m = LINE.match(raw)
        if not m:
            raise ValueError("bad decklist line: " + raw)
        rows.append((int(m[1]), m[2], m[3], m[4], bool(m[5])))
    return rows


def files(spec):
    s = spec["stem"]
    return {k: DRAFTS / f"{s}_{k}" for k in ("proposal.json", "printing_evidence.json", "decklist.txt", "archidekt_import.txt")}


def audit(spec_path):
    spec = json.loads(Path(spec_path).read_text(encoding="utf-8"))
    f = files(spec)
    prop = json.loads(f["proposal.json"].read_text(encoding="utf-8"))
    ev = json.loads(f["printing_evidence.json"].read_text(encoding="utf-8"))
    deck_text = f["decklist.txt"].read_text(encoding="utf-8")
    sha = hashlib.sha256(deck_text.encode()).hexdigest()
    if not (prop["raw_decklist_sha256"] == ev["raw_sha256"] == sha):
        raise ValueError("decklist SHA-256 mismatch")
    status = prop["status"]
    if status != spec["status"] or not status.startswith("UNAPPROVED") or FORBIDDEN_STATUS.search(
            status.replace("not approved", "").replace("not locked", "").replace("not certified", "")):
        raise ValueError("pilot must stay UNAPPROVED")
    if any(prop["approval"][k] for k in ("approved", "locked", "certified")):
        raise ValueError("approval flags must all be false")

    rows = parse(deck_text)
    total = sum(r[0] for r in rows)
    named = [r for r in rows if r[2]]
    if total != 100 or sum(r[4] for r in rows) != 1 or not rows[0][4]:
        raise ValueError("need exactly 100 cards with the commander first")
    if any(r[0] != 1 for r in named) or len({r[1] for r in named}) != len(named):
        raise ValueError("singleton violated")
    ident = set(spec["color_identity"])
    basics = {r[1]: r[0] for r in rows if not r[2]}
    if set(basics) - {BASIC_FOR[c] for c in ident} or basics != spec["basics"] or basics != prop["basics"]:
        raise ValueError("basics mismatch")

    cards = ev["cards"]
    spec_names = ([spec["commander"]["name"]] + [c["name"] for a in spec["acts"] for c in a["cards"]]
                  + [c["name"] for c in spec["story_lands"]["cards"]] + spec["playability"]["names"])
    if [c["name"] for c in cards] != [r[1] for r in named]:
        raise ValueError("evidence order/names differ from decklist")
    if [n.split(" // ")[0] for n in spec_names] != [c["name"].split(" // ")[0] for c in cards]:
        raise ValueError("committed files no longer mirror the spec; rerun build_lore_pilot.py")
    grades = {}
    for rel in spec.get("claim_packs", []):
        grades.update({c["id"]: c["grade"] for c in json.loads((ROOT / rel).read_text())["claims"]})
    art = {}
    if spec.get("exact_art_pack"):
        art = {c["name"]: c for c in json.loads((ROOT / spec["exact_art_pack"]).read_text())["cards"]}
    ck = spec.get("claims_key", "claims")
    seen, tiers, gcs = set(), {t: 0 for t in TIERS}, []
    for c, r in zip(cards, named):
        p = c["printing"]
        if (p["set"], p["collector_number"]) != (r[2], r[3]):
            raise ValueError("printing mismatch: " + c["name"])
        if not (UUID.fullmatch(p["id"]) and UUID.fullmatch(p["oracle_id"] or "")) or p["id"] in seen:
            raise ValueError("bad or duplicate printing UUID: " + c["name"])
        seen.add(p["id"])
        if p["commander_legality"] != "legal" or not set(p["color_identity"]) <= ident:
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
        if c["source_id"] == "scryfall_card_text":
            if c["tier"] == "DIRECT_DEPICTION":
                raise ValueError("printed text alone cannot prove a depiction: " + c["name"])
        elif not c["source"].startswith("https://magic.wizards.com/"):
            raise ValueError("non-official story source: " + c["name"])
        if c["tier"] == "DIRECT_DEPICTION" and c["name"] in art and art[c["name"]]["context_tier"] != "DIRECT_EVENT_SCENE_CAPTION":
            raise ValueError("exact-art tier inflated: " + c["name"])
        if c["name"] in art and p["illustration_id"] != art[c["name"]]["matched_illustration_id"]:
            raise ValueError("exact-art printing not used: " + c["name"])
        for cid in c.get(ck, []):
            if grades.get(cid) != "CANON_CONFIRMED":
                raise ValueError(f"{c['name']} leans on non-confirmed claim {cid}")
    if tiers != prop["counts"]["tiers"]:
        raise ValueError("tier counts drift")
    if len(gcs) > spec.get("game_changer_ceiling", 3):
        raise ValueError("Game Changer ceiling exceeded")
    imp = f["archidekt_import.txt"].read_text(encoding="utf-8").splitlines()
    if imp[0] != "1x " + rows[0][1].split(" // ")[0] or len(imp) != len(rows):
        raise ValueError("Archidekt import must be commander-first and mirror the decklist")
    tags = prop["archidekt_tags"]
    if len(tags) != 3 or len(set(tags)) != 3:
        raise ValueError("need three distinct Archidekt tags")
    return {"result": "PASS", "stem": spec["stem"], "status": status, "total": total, "named": len(named),
            "basics": sum(basics.values()), "tiers": tiers, "game_changers": gcs,
            "decklist_sha256": sha, "snapshot": prop["snapshot"]["id"], "realtime_fetch": False}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--spec", type=Path, action="append")
    a = ap.parse_args(argv)
    specs = a.spec or sorted(SPECS.glob("*.json"))
    bad = 0
    for s in specs:
        try:
            print(json.dumps(audit(s)))
        except (ValueError, KeyError, FileNotFoundError) as e:
            bad += 1
            print(f"FAIL {s}: {e}", file=sys.stderr)
    return 1 if bad or not specs else 0


if __name__ == "__main__":
    sys.exit(main())
