#!/usr/bin/env python3
"""Phase 3: claim-level card anchors (which printed cards name a claim's participants, and how strongly).

For every claim in every manifest claim pack, each participant (the subject and each ``;``-separated
object) that already has a **card-name anchor** (``data/lore_research/card_name_anchors_2026-10-30.json``)
contributes its anchored cards. Each claim-card pair gets exactly one tier, strongest first:

* ``ART_IN_CITED_SOURCE``: the card's art is credited by exact card name on an official Wizards page
  that the claim itself cites (from the story-art caption atlas, ``data/story_atlas/``).
* ``PRINTED_IN_STORY_SET``: the card has a paper printing in the card set whose official main-story
  episodes the claim's pack covers (``STORY_SETS``; only episode packs with one unambiguous set).
* ``NAMED_PARTICIPANT``: the card is named for a participant and nothing more is known.

An anchor says "this card is named for someone or something in this claim". It is **never** a
statement that the card's art or text depicts the claimed event, and it never changes a claim's grade.
Card data comes from the manifest-verified Scryfall snapshot; lore comes only from the claim packs.

  python3 scripts/build_claim_card_anchors.py            # write the file
  python3 scripts/build_claim_card_anchors.py --check    # fail if stale (snapshot needed for a full rebuild)

Without the snapshot, --check verifies the self-hash and that every committed anchor still refers
to a current claim, participant and card-name anchor.
"""
from __future__ import annotations

import argparse
import glob
import gzip
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_card_name_anchors as N  # noqa: E402

ROOT = N.ROOT
OUT = ROOT / "data/lore_research/claim_card_anchors_2026-10-30.json"
NAMES = N.OUT
ATLAS = ROOT / "data/story_atlas/story_art_captions_2026-10-30.json"
# Episode packs whose official story was published for exactly one card set.
STORY_SETS = {
    "pack_c2_return_to_dominaria_2026-10-30.json": ["dom"],
    "pack_c3_assault_on_new_phyrexia_2026-10-30.json": ["one"],
    "pack_c4_march_of_the_machine_2026-10-30.json": ["mom"],
    # Phase 5 two-set story blocks (each pack spans exactly the block's two sets)
    "pack_p5_kaladesh_aether_revolt_2026-10-30.json": ["kld", "aer"],
    "pack_p5_ixalan_rivals_2026-10-30.json": ["xln", "rix"],
    "pack_p5_amonkhet_hour_of_devastation_2026-10-30.json": ["akh", "hou"],
    "pack_p5_kamigawa_neon_dynasty_2026-10-30.json": ["neo"],
    "pack_p5_innistrad_midnight_hunt_crimson_vow_2026-10-30.json": ["mid", "vow"],
    "pack_p5_streets_of_new_capenna_2026-10-30.json": ["snc"],
    "pack_p5_edge_of_eternities_2026-10-30.json": ["eoe"],
    "pack_p5_reality_fracture_2026-10-30.json": ["fra"],
    "pack_p5_wilds_of_eldraine_2026-10-30.json": ["woe"],
    "pack_p5_murders_at_karlov_manor_2026-10-30.json": ["mkm"],
    "pack_p5_bloomburrow_2026-10-30.json": ["blb"],
    "pack_p5_duskmourn_2026-10-30.json": ["dsk"],
    "pack_p5_outlaws_of_thunder_junction_2026-10-30.json": ["otj"],
    "pack_p5_lost_caverns_of_ixalan_2026-10-30.json": ["lci"],
    "pack_p5_aetherdrift_2026-10-30.json": ["dft"],
    "pack_p5_kaldheim_2026-10-30.json": ["khm"],
    "pack_p5_strixhaven_2026-10-30.json": ["stx"],
    "pack_p5_ikoria_2026-10-30.json": ["iko"],
    "pack_p5_theros_beyond_death_2026-10-30.json": ["thb"],
    "pack_p5_theros_ths_2026-10-30.json": ["ths", "bng", "jou"],
    "pack_p5_mom_aftermath_2026-10-30.json": ["mat"],
    "pack_p5_throne_of_eldraine_2026-10-30.json": ["eld"],
    "pack_p5_secrets_of_strixhaven_2026-10-30.json": ["sos"],
    "pack_p5_shadows_eldritch_moon_2026-10-30.json": ["soi", "emn"],
}
TIERS = ["ART_IN_CITED_SOURCE", "PRINTED_IN_STORY_SET", "NAMED_PARTICIPANT"]


def sha(body: dict) -> str:
    return hashlib.sha256(json.dumps(body, sort_keys=True).encode()).hexdigest()


def participants(c: dict) -> list[str]:
    return [c["subject"]] + [t.strip() for t in str(c["object"]).split(";") if t.strip()]


def claims() -> list[tuple[str, dict, dict]]:
    m = json.loads(N.MANIFEST.read_text(encoding="utf-8"))
    out = []
    for rel in m["claim_packs"]:
        d = json.loads((ROOT / rel).read_text(encoding="utf-8"))
        for c in d.get("claims", []):
            out.append((Path(rel).name, c, d.get("source_register", {})))
    return out


def set_printings(oracle_ids: set[str]) -> dict[str, set[str]]:
    files = sorted(glob.glob(str(N.CACHE / "default-cards-*.jsonl.gz")))
    if not files:
        raise FileNotFoundError("default-cards snapshot missing from " + str(N.CACHE))
    sets: dict[str, set[str]] = {}
    for line in gzip.open(files[0], "rt", encoding="utf-8"):
        pr = json.loads(line)
        if pr.get("oracle_id") in oracle_ids and "paper" in pr.get("games", []):
            sets.setdefault(pr["oracle_id"], set()).add(pr["set"])
    return sets


def build() -> dict:
    names = json.loads(NAMES.read_text(encoding="utf-8"))
    by_entity = {a["entity"]: a["cards"] for a in names["anchors"]}
    atlas = json.loads(ATLAS.read_text(encoding="utf-8"))
    art = {p["url"]: {x["oracle_id"] for x in p["captions"]} for p in atlas["pages"]}
    oids = {c["oracle_id"] for cards in by_entity.values() for c in cards}
    sets = set_printings(oids)
    rows, per_pack = [], {}
    for pack, c, reg in claims():
        urls = sorted({reg[s]["url"] for s in c.get("source_ids", []) if s in reg})
        story_sets = STORY_SETS.get(pack, [])
        seen = set()
        for ent in participants(c):
            for card in by_entity.get(ent, []):
                key = (ent, card["oracle_id"])
                if key in seen:
                    continue
                seen.add(key)
                art_urls = [u for u in urls if card["oracle_id"] in art.get(u, set())]
                in_set = sorted(set(story_sets) & sets.get(card["oracle_id"], set()))
                if art_urls:
                    tier, basis = TIERS[0], {"cited_pages_crediting_art": art_urls}
                elif in_set:
                    tier, basis = TIERS[1], {"story_set_printings": in_set}
                else:
                    tier, basis = TIERS[2], {}
                rows.append({"claim": c["id"], "pack": pack, "participant": ent, "card": card["name"],
                             "oracle_id": card["oracle_id"], "tier": tier, **basis})
        st = per_pack.setdefault(pack, {"claims": 0, "claims_anchored": 0, **{t: 0 for t in TIERS}})
        st["claims"] += 1
        mine = [r for r in rows if r["claim"] == c["id"] and r["pack"] == pack]
        st["claims_anchored"] += bool(mine)
        for r in mine:
            st[r["tier"]] += 1
    body = {
        "schema": "claim-card-anchors/v1",
        "status": "PRELIMINARY_RESEARCH (mechanical card-data anchors; not owner approved; not lore claims)",
        "card_data_source": names["card_data_source"],
        "name_anchor_source": str(NAMES.relative_to(ROOT)),
        "art_source": str(ATLAS.relative_to(ROOT)),
        "story_sets": STORY_SETS,
        "rule": ("Each claim participant with a card-name anchor contributes its cards. Tier ART_IN_CITED_SOURCE: the "
                 "card's art is credited by exact name on an official page the claim cites. PRINTED_IN_STORY_SET: a "
                 "paper printing in the set whose main-story episodes the pack covers. NAMED_PARTICIPANT: otherwise. "
                 "An anchor never asserts that the card depicts the claimed event and never changes a claim grade."),
        "tiers": TIERS,
        "anchors": rows,
        "by_pack": dict(sorted(per_pack.items())),
        "counts": {"claims": sum(v["claims"] for v in per_pack.values()),
                   "claims_anchored": sum(v["claims_anchored"] for v in per_pack.values()),
                   "anchors": len(rows), **{t: sum(r["tier"] == t for r in rows) for t in TIERS}},
    }
    body["content_sha256"] = sha(body)
    return body


def structural_problems(cur: dict) -> list[str]:
    names = json.loads(NAMES.read_text(encoding="utf-8"))
    by_entity = {a["entity"]: {c["oracle_id"] for c in a["cards"]} for a in names["anchors"]}
    known = {(p, c["id"]): set(participants(c)) for p, c, _ in claims()}
    probs = []
    for r in cur["anchors"]:
        parts = known.get((r["pack"], r["claim"]))
        if parts is None:
            probs.append(f"{r['claim']}: claim no longer in {r['pack']}")
        elif r["participant"] not in parts:
            probs.append(f"{r['claim']}: {r['participant']} is not a participant")
        elif r["oracle_id"] not in by_entity.get(r["participant"], set()):
            probs.append(f"{r['claim']}: {r['card']} is not a card-name anchor of {r['participant']}")
        if r["tier"] not in TIERS:
            probs.append(f"{r['claim']}: unknown tier {r['tier']}")
    return probs


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--check", action="store_true")
    a = p.parse_args(argv)
    if a.check:
        cur = json.loads(OUT.read_text(encoding="utf-8"))
        if sha({k: v for k, v in cur.items() if k != "content_sha256"}) != cur.get("content_sha256"):
            print("FAIL: claim card anchors self-hash mismatch"); return 1
        probs = structural_problems(cur)
        if probs:
            print("FAIL:\n" + "\n".join(probs)); return 1
        try:
            new = build()
        except FileNotFoundError:
            print(f"PASS (snapshot absent: self-hash and structure verified) {cur['counts']}"); return 0
        if new != cur:
            print("FAIL: claim card anchors are stale; rerun scripts/build_claim_card_anchors.py"); return 1
        print(f"PASS claim card anchors current: {cur['counts']}"); return 0
    d = build()
    OUT.write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}: {d['counts']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
