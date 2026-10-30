#!/usr/bin/env python3
"""Phase 3: Card name anchors for the Multiverse claim graph (CardRepresentation edges).

Every Character, Object, Place or Event entity in a claim pack is matched against the
**manifest-verified Scryfall snapshot** (oracle cards; card data, not lore). A card counts as
an anchor only when its printed (front-face) name names the entity:

* Characters: a **legendary creature or planeswalker** whose name equals one of the curated
  aliases below, or begins with an alias followed by ``", "``, ``" the "``, ``" of "`` or a single
  further word (``Karn Liberated``). A possessive (``Urza's Saga``) never counts.
* Objects, places and events: a card whose name equals the entity name or an alias.

Cards with at least one paper printing only. Cards printed only in Un-sets ("funny") are reported separately and never anchored. An
anchor says only "this printed card is named for this entity". It is **not** a claim
about a story event, an illustration or a timeline. The graph labels these edges
``named_on_card`` with tier ``NAMED_CARD`` and card-data source Scryfall.

  python3 scripts/build_card_name_anchors.py            # write the pack
  python3 scripts/build_card_name_anchors.py --check    # fail if stale (needs the snapshot)

Without the snapshot, --check verifies the committed file's schema and self-hash only.
"""
from __future__ import annotations

import argparse
import glob
import gzip
import hashlib
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data/multiverse_graph/manifest.json"
OUT = ROOT / "data/lore_research/card_name_anchors_2026-10-30.json"
SNAPSHOT = "snap-20261029-40848334824-1"
CACHE = Path(os.environ.get("MTG_MULTIVERSE_CACHE", ROOT / ".cache/multiverse"))

# Curated aliases: the names under which Wizards prints each entity's cards. They are reviewed
# by hand. An entity with no entry uses its own pack name (minus a parenthetical gloss).
ALIASES = {
    "ugin": ["Ugin"], "nicol_bolas": ["Nicol Bolas"], "sarkhan_vol": ["Sarkhan Vol", "Sarkhan"],
    "narset": ["Narset"], "arcades_sabboth": ["Arcades Sabboth", "Arcades"], "chromium_rhuell": ["Chromium"],
    "palladia_mors": ["Palladia-Mors"], "vaevictis_asmadi": ["Vaevictis Asmadi"], "piru": ["Piru"],
    "crosis": ["Crosis"], "rith": ["Rith"], "geyadrone_dihada": ["Geyadrone Dihada", "Dihada"],
    "dakkon": ["Dakkon Blackblade", "Dakkon"], "yasova_dragonclaw": ["Yasova Dragonclaw", "Yasova"],
    "urza": ["Urza"], "mishra": ["Mishra"], "kayla_bin_kroog": ["Kayla bin-Kroog"], "harbin": ["Harbin"],
    "tawnos": ["Tawnos"], "ashnod": ["Ashnod"], "gix": ["Gix"], "yawgmoth": ["Yawgmoth"], "teferi": ["Teferi"],
    "ajani": ["Ajani"], "saheeli": ["Saheeli"], "karn": ["Karn"], "gerrard": ["Gerrard Capashen", "Gerrard"],
    "jhoira": ["Jhoira"], "shanna": ["Shanna"], "jodah": ["Jodah"], "sheoldred": ["Sheoldred"],
    "elesh_norn": ["Elesh Norn"], "raff_capashen": ["Raff Capashen"],
    "weatherlight": ["Weatherlight"], "golgothian_sylex": ["Golgothian Sylex"],
    "mightstone_and_weakstone": ["The Mightstone and Weakstone"], "argoth": ["Argoth, Sanctum of Nature"],
    "brothers_war": ["The Brothers' War"], "caves_of_koilos": ["Caves of Koilos"],
    "elder_dragon_wars": ["The Elder Dragon War"], "ugins_nexus": ["Ugin's Nexus"],
    "crucible_spirit_dragon": ["Crucible of the Spirit Dragon"], "tomb_spirit_dragon": ["Tomb of the Spirit Dragon"],
    "corondor_chasm": [],  # no card is named for this place
}
TYPES = {"Character", "Object", "Place", "Event"}


def front(c: dict) -> str:
    return c["name"].split(" // ")[0]


def type_line(c: dict) -> str:
    return c.get("type_line") or (c.get("card_faces") or [{}])[0].get("type_line", "")


def char_match(name: str, alias: str) -> bool:
    if name == alias:
        return True
    if not name.startswith(alias + " ") and not name.startswith(alias + ","):
        return False
    rest = name[len(alias):]
    return bool(re.match(r"^(, .+| the .+| of .+| [A-Z][\w-]+)$", rest))


def entities() -> list[dict]:
    m = json.loads(MANIFEST.read_text(encoding="utf-8"))
    seen: dict[str, dict] = {}
    for rel in m["claim_packs"]:
        for e in json.loads((ROOT / rel).read_text(encoding="utf-8")).get("entities", []):
            if e["type"] in TYPES and e["id"] not in seen:
                seen[e["id"]] = {"id": e["id"], "type": e["type"], "name": e["name"], "pack": Path(rel).name}
    return sorted(seen.values(), key=lambda e: e["id"])


def load_cards() -> tuple[list[dict], str]:
    files = sorted(glob.glob(str(CACHE / "oracle-cards-*.jsonl.gz")))
    if not files:
        raise FileNotFoundError("oracle-cards snapshot missing from " + str(CACHE))
    path = Path(files[0])
    cards = [json.loads(line) for line in gzip.open(path, "rt", encoding="utf-8")]
    # The oracle file holds one printing per card, so paper availability and Un-set status are
    # aggregated over every printing in the default-cards snapshot.
    paper, serious = set(), set()
    for f in sorted(glob.glob(str(CACHE / "default-cards-*.jsonl.gz")))[:1]:
        for line in gzip.open(f, "rt", encoding="utf-8"):
            pr = json.loads(line)
            if "paper" in pr.get("games", []):
                paper.add(pr.get("oracle_id"))
                if pr.get("set_type") != "funny":
                    serious.add(pr.get("oracle_id"))
    for c in cards:
        c["_paper"] = c["oracle_id"] in paper
        c["_unset_only"] = c["oracle_id"] in paper and c["oracle_id"] not in serious
    return cards, path.name


def build() -> dict:
    cards, bulk = load_cards()
    paper = [c for c in cards if c["_paper"] and c.get("layout") not in {"token", "art_series", "emblem"}]
    out, unset, unmatched = [], [], []
    for e in entities():
        aliases = ALIASES.get(e["id"], [re.sub(r"\s*\(.*\)$", "", e["name"])])
        hits = []
        for c in paper:
            n, tl = front(c), type_line(c)
            if e["type"] == "Character":
                ok = ("Legendary" in tl and ("Creature" in tl or "Planeswalker" in tl)
                      and any(char_match(n, a) for a in aliases))
            else:
                ok = n in aliases
            if not ok:
                continue
            rec = {"name": c["name"], "oracle_id": c["oracle_id"], "type_line": tl,
                   "scryfall_uri": c.get("scryfall_uri", "").split("?")[0]}
            (unset if c["_unset_only"] else hits).append(rec)
        hits.sort(key=lambda r: (r["name"], r["oracle_id"]))
        if hits:
            out.append({"entity": e["id"], "entity_type": e["type"], "entity_name": e["name"], "aliases": aliases,
                        "pack": e["pack"], "cards": hits})
        else:
            unmatched.append(e["id"])
    body = {
        "schema": "card-name-anchors/v1",
        "status": "PRELIMINARY_RESEARCH (mechanical card-data anchors; not owner approved; not lore claims)",
        "card_data_source": {"provider": "Scryfall", "snapshot": SNAPSHOT, "file": bulk},
        "rule": ("A printed paper card whose front-face name names the entity: legendary creature or planeswalker for "
                 "characters (alias exactly, or alias + ', '/' the '/' of '/one further word; never a possessive); exact "
                 "name for objects, places and events. A name anchor is not evidence about a story event, an "
                 "illustration or a chronology."),
        "tier": "NAMED_CARD",
        "anchors": out,
        "unanchored_entities": sorted(unmatched),
        "excluded_unset_cards": sorted({(r["name"]) for r in unset}),
        "counts": {"entities_anchored": len(out), "anchor_edges": sum(len(a["cards"]) for a in out),
                   "unanchored_entities": len(unmatched)},
    }
    body["content_sha256"] = hashlib.sha256(json.dumps(body, sort_keys=True).encode()).hexdigest()
    return body


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--check", action="store_true")
    a = p.parse_args(argv)
    if a.check:
        cur = json.loads(OUT.read_text(encoding="utf-8"))
        body = {k: v for k, v in cur.items() if k != "content_sha256"}
        if hashlib.sha256(json.dumps(body, sort_keys=True).encode()).hexdigest() != cur.get("content_sha256"):
            print("FAIL: card name anchors self-hash mismatch")
            return 1
        try:
            new = build()
        except FileNotFoundError:
            print(f"PASS (snapshot absent: self-hash verified) {cur['counts']}")
            return 0
        if new != cur:
            print("FAIL: card name anchors are stale; rerun scripts/build_card_name_anchors.py")
            return 1
        print(f"PASS card name anchors current: {cur['counts']}")
        return 0
    d = build()
    OUT.write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}: {d['counts']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
