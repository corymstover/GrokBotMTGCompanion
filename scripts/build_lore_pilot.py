#!/usr/bin/env python3
"""Spec-driven builder for UNAPPROVED Phase 6 lore-first Commander pilot proposals.

Card choice, story order, tiers and sources are authored in a JSON spec under
data/lore_decks/specs/ (no silent fill-ins: every non-basic card is named in the spec).
Printing facts (UUID, illustration id, artist, printed flavor, legality, identity,
Game Changer flag) are read from an explicit, dated modern Scryfall default-cards
snapshot -- never the frozen Grixis lock. It writes only the four
data/lore_decks/drafts/<stem>_* files and never touches approvals, locks or Grixis data.

    python3 scripts/build_lore_pilot.py --spec data/lore_decks/specs/X.json --default-bulk PATH.jsonl.gz
"""
import argparse
import gzip
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DRAFTS = ROOT / "data/lore_decks/drafts"
TIERS = ("DIRECT_DEPICTION", "CANON_REFERENCE", "LORE_INSPIRED", "MECHANICAL_SYMBOL")
BASIC_FOR = {"W": "Plains", "U": "Island", "B": "Swamp", "R": "Mountain", "G": "Forest"}
FORBIDDEN = re.compile(r"\b(APPROVED|LOCKED|CERTIFIED)\b")


class SpecError(ValueError):
    pass


def load_spec(path):
    spec = json.loads(Path(path).read_text(encoding="utf-8"))
    if spec.get("schema") != "lore-pilot-spec/v1":
        raise SpecError("spec schema must be lore-pilot-spec/v1")
    st = spec["status"]
    if not st.startswith("UNAPPROVED") or FORBIDDEN.search(
            st.replace("not approved", "").replace("not locked", "").replace("not certified", "")):
        raise SpecError("a pilot spec must stay UNAPPROVED")
    if not re.fullmatch(r"[a-z0-9_]+", spec["stem"]):
        raise SpecError("stem must be lowercase snake_case")
    rows = [spec["commander"]] + [c for a in spec["acts"] for c in a["cards"]] + spec["story_lands"]["cards"]
    for r in rows:
        if r["tier"] not in TIERS[:3]:
            raise SpecError(f"story card needs a story tier: {r['name']}")
        if r["source_id"] not in spec["sources"]:
            raise SpecError(f"unknown source id {r['source_id']} for {r['name']}")
    if set(spec["basics"]) - {BASIC_FOR[c] for c in spec["color_identity"]}:
        raise SpecError("basics outside the commander's colours")
    return spec


def printings(bulk):
    out = {}
    opener = gzip.open if str(bulk).endswith(".gz") else open
    with opener(bulk, "rt", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip().rstrip(",")
            if not line or line in "[]":
                continue
            c = json.loads(line)
            if c.get("lang") != "en" or "paper" not in c.get("games", []) or c.get("layout") == "art_series":
                continue
            out.setdefault(c["name"], []).append(c)
    return out


def flavor(c):
    if c.get("flavor_text"):
        return c["flavor_text"]
    return " / ".join(f["flavor_text"] for f in c.get("card_faces", []) if f.get("flavor_text"))


def pick(cands, name, set_code=None, cn=None):
    if not cands:
        raise SystemExit("not in snapshot: " + name)
    if set_code:
        hit = [c for c in cands if c["set"] == set_code and c["collector_number"] == cn]
        if not hit:
            raise SystemExit(f"printing not found: {name} {set_code}/{cn}")
        return hit[0]
    normal = [c for c in cands if not c.get("promo") and c.get("border_color") == "black"
              and not c.get("full_art") and c["set_type"] in ("core", "expansion", "commander", "masters")]
    normal.sort(key=lambda c: (c["released_at"], c["set"], c["collector_number"]))
    return (normal or sorted(cands, key=lambda c: c["released_at"]))[0]


def record(spec, c, tier, source_id, claims, why, beat):
    ill = c.get("illustration_id") or (c.get("card_faces") or [{}])[0].get("illustration_id")
    return {"name": c["name"], "beat": beat, "tier": tier, "source_id": source_id,
            "source": spec["sources"][source_id], spec.get("claims_key", "claims"): claims, "why": why,
            "printing": {"set": c["set"], "collector_number": c["collector_number"], "id": c["id"],
                         "oracle_id": c.get("oracle_id"), "illustration_id": ill,
                         "artist": c.get("artist"), "released_at": c["released_at"],
                         "printed_flavor": flavor(c),
                         "commander_legality": c.get("legalities", {}).get("commander"),
                         "color_identity": c.get("color_identity"), "type_line": c.get("type_line"),
                         "game_changer": bool(c.get("game_changer"))}}


def _row(spec, db, r, beat):
    return record(spec, pick(db.get(r["name"]), r["name"], r.get("set"), r.get("collector_number")),
                  r["tier"], r["source_id"], r.get("claims", []), r["why"], beat)


def build(spec, db, snapshot):
    cards = [_row(spec, db, spec["commander"], "commander")]
    beats = []

    def beat(title, keys, rows):
        out = []
        for r in rows:
            cards.append(_row(spec, db, r, title if title != spec["story_lands"]["title"] else "story lands"))
            out.append({"name": r["name"], "why": r["why"], "evidence": r["tier"],
                        "source": spec["sources"][r["source_id"]],
                        "printing": {"set": r.get("set"), "collector": r.get("collector_number")}})
        return out
    for a in spec["acts"]:
        beats.append({"title": a["title"], "lore_keys": a["lore_keys"], "cards": beat(a["title"], a["lore_keys"], a["cards"])})
    sl = spec["story_lands"]
    if sl["cards"]:
        beats.append({"title": sl["title"], "lore_keys": sl["lore_keys"], "cards": beat(sl["title"], sl["lore_keys"], sl["cards"])})
    play = []
    pl = spec["playability"]
    for name in pl["names"]:
        cards.append(record(spec, pick(db.get(name), name), "MECHANICAL_SYMBOL", "scryfall_card_text", [],
                            pl["why"], "playability"))
        play.append({"name": name, "why": pl.get("spec_why", pl["why"])})

    ident = set(spec["color_identity"])
    for c in cards:
        if c["printing"]["commander_legality"] != "legal":
            raise SystemExit("not Commander-legal in snapshot: " + c["name"])
        if not set(c["printing"]["color_identity"]) <= ident:
            raise SystemExit(f"outside {''.join(spec['color_identity'])} identity: " + c["name"])
    names = [c["name"] for c in cards]
    if len(set(names)) != len(names):
        raise SystemExit("singleton violated: " + ", ".join(sorted({n for n in names if names.count(n) > 1})))
    basics = spec["basics"]
    total = len(cards) + sum(basics.values())
    if total != 100:
        raise SystemExit(f"deck has {total} cards, need 100")
    gcs = [c["name"] for c in cards if c["printing"]["game_changer"]]
    if len(gcs) > spec.get("game_changer_ceiling", 3):
        raise SystemExit("too many Game Changers: " + ", ".join(gcs))

    lines = []
    for c in cards:
        p = c["printing"]
        tag = " [Commander]" if c["beat"] == "commander" else ""
        lines.append(f"1x {c['name']} ({p['set']}) {p['collector_number']}{tag}")
    lines += [f"{q}x {n}" for n, q in basics.items()]
    decklist = "\n".join(lines) + "\n"
    import_list = "\n".join([f"1x {c['name'].split(' // ')[0]}" for c in cards] +
                            [f"{q}x {n}" for n, q in basics.items()]) + "\n"
    deck_sha = hashlib.sha256(decklist.encode()).hexdigest()
    tiers = {t: sum(1 for c in cards if c["tier"] == t) for t in TIERS}
    proposal = {
        "schema": "lore_story_deck_draft/v1", "theme": spec["theme"], "status": spec["status"],
        "approval": {"approved": False, "locked": False, "certified": False, "owner": "Cory"},
        "commander": cards[0]["name"],
        "narrator_note": spec["narrator_note"],
        "story_sources": sorted(set(v for v in spec["sources"].values() if v.startswith("https://"))),
        "canon_caveats": spec["canon_caveats"],
        "unrepresentable_in_identity": spec["unrepresentable_in_identity"],
        "beats": beats, "playability": play, "basics": basics,
        "archidekt_tags": spec["archidekt_tags"], "snapshot": snapshot,
        "raw_decklist_sha256": deck_sha,
        "counts": {"total": total, "named_cards": len(cards), "basics": sum(basics.values()), "tiers": tiers},
    }
    if "spec_file" in spec:
        proposal["spec"] = spec["spec_file"]
    evidence = {"theme": spec["theme"], "status": spec["status"], "raw_sha256": deck_sha,
                "snapshot": snapshot, "tier_definitions": spec["tier_definitions"], "cards": cards}
    return proposal, evidence, decklist, import_list


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--spec", required=True, type=Path)
    ap.add_argument("--default-bulk", required=True, type=Path)
    ap.add_argument("--snapshot-id", default="snap-20261029-40848334824-1")
    ap.add_argument("--out-dir", type=Path, default=DRAFTS)
    a = ap.parse_args(argv)
    spec = load_spec(a.spec)
    snapshot = {"id": a.snapshot_id, "default_cards_file": a.default_bulk.name,
                "default_cards_sha256": hashlib.sha256(a.default_bulk.read_bytes()).hexdigest()}
    proposal, evidence, decklist, import_list = build(spec, printings(a.default_bulk), snapshot)
    stem = spec["stem"]
    a.out_dir.mkdir(parents=True, exist_ok=True)
    (a.out_dir / f"{stem}_proposal.json").write_text(json.dumps(proposal, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    (a.out_dir / f"{stem}_printing_evidence.json").write_text(json.dumps(evidence, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    (a.out_dir / f"{stem}_decklist.txt").write_text(decklist, encoding="utf-8")
    (a.out_dir / f"{stem}_archidekt_import.txt").write_text(import_list, encoding="utf-8")
    print(json.dumps({"stem": stem, "total": proposal["counts"]["total"], "tiers": proposal["counts"]["tiers"],
                      "sha256": proposal["raw_decklist_sha256"]}, indent=1))


if __name__ == "__main__":
    main()
