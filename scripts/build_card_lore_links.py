#!/usr/bin/env python3
"""Phase 2 L213: link priority-pool cards that show "❓ No lore entry … yet" to cited official evidence.

Reads committed artifacts plus the pinned Scryfall snapshot and the gitignored official story cache
(.cache/story/text22 and .cache/story/extra). It writes data/lore_research/card_lore_links_2026-10-30.json,
an overlay. It never edits data/card_enrichment.json, the card shards or any deck file.

Evidence tiers, strongest first (a card records every tier that holds):
  CLAIM_ANCHORED            the card's name anchors an entity that takes part in cited claim-pack claims
                            (data/lore_research/claim_card_anchors_*.json); claim ids and their source URLs are listed.
  OFFICIAL_TEXT_NAMES_CARD  the card's exact printed front-face name appears verbatim in an official Wizards page;
                            a verbatim snippet (>= 25 chars) containing the name is stored. Artist credits and
                            "<name> | Art by" captions do not count, and the name must contain a word of >= 4 letters
                            never seen lower-case in the corpus (so "Six" or "The Thing" cannot match prose).
                            Graded NAMED_IN_OFFICIAL_TEXT: the page names the card; it may be a bio or a passing mention.
  SHORT_NAME_IN_SET_STORY   IMPLIED: the name before the comma (a proper noun: never seen lower-case in the corpus,
                            >= 4 letters) appears in an official page whose story arc is a set the card was printed
                            in (or that set's Commander companion). Identity is inferred, so it is graded IMPLIED.
  ART_ON_OFFICIAL_PAGE      navigation only: the page shows the card's art (exact-name caption or matched image
                            label). Not a claim that the art depicts a story event.
A card with CLAIM_ANCHORED, OFFICIAL_TEXT_NAMES_CARD or SHORT_NAME_IN_SET_STORY is LINKED; with only
ART_ON_OFFICIAL_PAGE it is ART_ONLY; otherwise NO_LORE_YET with a reason. Universes Beyond cards
(triangle security stamp on any printing) are never text-matched: official Magic story pages are not their canon.
"""
from __future__ import annotations

import argparse
import collections
import csv
import glob
import gzip
import hashlib
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data/lore_research/card_lore_links_2026-10-30.json"
ENRICH = ROOT / "data/card_enrichment.json"
CCA = ROOT / "data/lore_research/claim_card_anchors_2026-10-30.json"
ART = ROOT / "data/story_atlas/story_art_captions_2026-10-30.json"
LABELS = ROOT / "data/lore_research/story_image_label_printings_2026-10-30.json"
PRIMARY = ROOT / "data/primary_sources.csv"
EXTRA = ROOT / "data/story_extra_sources.csv"
CATALOG = ROOT / "data/set_atlas/catalog_2026-10-29.json"
STORY = ROOT / ".cache/story"
CACHE = Path(os.environ.get("MTG_MULTIVERSE_CACHE", ROOT / ".cache/multiverse"))
SNAPSHOT = "snap-20261029-40848334824-1"
SCHEMA = "card-lore-links/v1"
NO_LORE = "❓ No lore entry"
MIN_QUOTE = 25
# Commander companions whose Scryfall name is not "<parent> Commander", plus the Reality Fracture arc code.
EXTRA_SETS = {"neo": ["nec"], "snc": ["ncc"], "mid": ["mic"], "vow": ["voc"], "stx": ["c21"], "iko": ["c20"],
              "rf": ["fra", "frc"]}
WORD = re.compile(r"[A-Za-z0-9'\-]+")


def slug(url: str) -> str:
    return url.rstrip("/").split("/")[-1]


def sha(obj) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def load_pages() -> dict:
    meta = {}
    for r in csv.DictReader(PRIMARY.open(encoding="utf-8")):
        meta[slug(r["url"])] = {"url": r["url"], "arc": r["arc"], "dir": "text22"}
    for r in csv.DictReader(EXTRA.open(encoding="utf-8")):
        meta.setdefault(slug(r["url"]), {"url": r["url"], "arc": "", "dir": "extra"})
    pages = {}
    for s, m in meta.items():
        f = STORY / m["dir"] / f"{s}.txt"
        if f.exists():
            pages[s] = dict(m, text=f.read_text(encoding="utf-8"))
    if len(pages) < 600:
        raise SystemExit(f"story cache incomplete ({len(pages)} pages); run scripts/fetch_story_pages.py first")
    return pages


def arc_sets(arc: str, catalog: dict) -> set:
    out = set()
    for a in filter(None, arc.lower().split("/")):
        out.add(a)
        out.update(EXTRA_SETS.get(a, []))
        if a in catalog:
            out.update(c for c, v in catalog.items() if v["name"] == catalog[a]["name"] + " Commander")
    return out


def snippet(text: str, i: int, n: int, pad: int = 110) -> str:
    """Verbatim window centred on the match, trimmed to whole words."""
    a, b = max(i - pad, 0), min(i + n + pad, len(text))
    while a > 0 and not text[a - 1].isspace():
        a += 1
    while b < len(text) and not text[b].isspace() and b > i + n:
        b -= 1
    return re.sub(r"\s+", " ", text[a:b]).strip()


def find_name(text: str, name: str):
    """First whole-word occurrence that is not an artist credit ("Art by: <name>") or art caption ("<name> | Art by")."""
    for m in re.finditer(r"(?<![A-Za-z0-9])" + re.escape(name) + r"(?![A-Za-z0-9])", text):
        before, after = text[max(m.start() - 40, 0):m.start()], text[m.end():m.end() + 12]
        if re.search(r"Art by:?\s*[\w .'-]*$", before) or re.match(r"\s*\|\s*Art by", after):
            continue  # artist credit or art caption: navigation, not text evidence
        return m.start()
    return -1


def proper_name(name: str, lower_words: set) -> bool:
    """At least one word of >= 4 letters that never occurs lower-case in the corpus (rejects Six, X, The Thing)."""
    return any(len(w) >= 4 and w.lower() not in lower_words for w in WORD.findall(name))


def build() -> dict:
    enrich = json.loads(ENRICH.read_text(encoding="utf-8"))["cards"]
    pool = {k: v for k, v in enrich.items() if any(l.startswith("- **Lore:**") and NO_LORE in l for l in v["lines"])}
    oracle_file = sorted(glob.glob(str(CACHE / "oracle-cards-*.jsonl.gz")))[0]
    default_file = sorted(glob.glob(str(CACHE / "default-cards-*.jsonl.gz")))[0]
    orc = {}
    for line in gzip.open(oracle_file, "rt", encoding="utf-8"):
        c = json.loads(line)
        if c["oracle_id"] in pool:
            orc[c["oracle_id"]] = c
    sets, ub = collections.defaultdict(set), set()
    for line in gzip.open(default_file, "rt", encoding="utf-8"):
        p = json.loads(line)
        o = p.get("oracle_id")
        if o in pool:
            sets[o].add(p["set"])
            if p.get("security_stamp") == "triangle":
                ub.add(o)
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))["sets"]
    pages = load_pages()
    words = {s: set(WORD.findall(p["text"])) for s, p in pages.items()}
    lower_words = set().union(*({w for w in ws if w.islower()} for ws in words.values()))
    page_sets = {s: arc_sets(p["arc"], catalog) for s, p in pages.items()}

    cca = collections.defaultdict(list)
    packs = {}
    for a in json.loads(CCA.read_text(encoding="utf-8"))["anchors"]:
        if a["oracle_id"] in pool:
            if a["pack"] not in packs:
                pk = json.loads((ROOT / "data/lore_research" / a["pack"]).read_text(encoding="utf-8"))
                reg = pk.get("source_register") or {}
                packs[a["pack"]] = ({c["id"]: c for c in pk.get("claims", [])},
                                    {k: v.get("url") for k, v in reg.items()} if isinstance(reg, dict) else {})
            claims_by_id, reg = packs[a["pack"]]
            cl = claims_by_id.get(a["claim"], {})
            cca[a["oracle_id"]].append({"claim": a["claim"], "pack": a["pack"], "participant": a["participant"],
                                        "anchor_tier": a["tier"], "grade": cl.get("grade"),
                                        "source_urls": sorted({reg.get(i) or "" for i in cl.get("source_ids", [])} - {""})})
    art = collections.defaultdict(set)
    for p in json.loads(ART.read_text(encoding="utf-8"))["pages"]:
        for c in p["captions"]:
            if c["oracle_id"] in pool:
                art[c["oracle_id"]].add(p["url"])
    by_name = {c["name"]: o for o, c in orc.items()}
    for lab in json.loads(LABELS.read_text(encoding="utf-8"))["labels"]:
        if lab["status"] == "MATCHED" and lab["printing"]["name"] in by_name:
            art[by_name[lab["printing"]["name"]]].add(lab["url"])

    cards, counts, reasons = [], collections.Counter(), collections.Counter()
    for o in sorted(pool, key=lambda k: (pool[k]["name"], k)):
        c = orc.get(o)
        name = pool[o]["name"]
        front = name.split(" // ")[0]
        ev = []
        if cca.get(o):
            ev.append({"tier": "CLAIM_ANCHORED", "grade": "CLAIMS_CANON_CONFIRMED" if all(
                x["grade"] == "CANON_CONFIRMED" for x in cca[o]) else "CLAIMS_MIXED_GRADES", "claims": cca[o][:12],
                "claims_total": len(cca[o])})
        is_ub = o in ub
        if not is_ub:
            fw = set(WORD.findall(front))
            hits = []
            for s, p in pages.items():
                if fw <= words[s] and proper_name(front, lower_words):
                    i = find_name(p["text"], front)
                    if i != -1:
                        q = snippet(p["text"], i, len(front))
                        if len(q) >= MIN_QUOTE and front in q:
                            hits.append({"url": p["url"], "quote": q})
            if hits:
                hits.sort(key=lambda h: h["url"])
                ev.append({"tier": "OFFICIAL_TEXT_NAMES_CARD", "grade": "NAMED_IN_OFFICIAL_TEXT",
                           "pages": hits[:5], "pages_total": len(hits)})
            m = re.match(r"^([A-Z][^,]+), ", front)
            if not hits and m:
                short = m.group(1)
                sw = set(WORD.findall(short))
                proper = len(short) >= 4 and all(w.lower() not in lower_words for w in sw)
                if proper:
                    sh = []
                    for s, p in pages.items():
                        if sw <= words[s] and page_sets[s] & sets[o]:
                            j = find_name(p["text"], short)
                            if j != -1:
                                q = snippet(p["text"], j, len(short))
                                if len(q) >= MIN_QUOTE:
                                    sh.append({"url": p["url"], "arc": p["arc"], "quote": q})
                    if sh:
                        sh.sort(key=lambda h: h["url"])
                        ev.append({"tier": "SHORT_NAME_IN_SET_STORY", "grade": "IMPLIED_SAME_SET_NAME", "short_name": short,
                                   "limitation": "Identity inferred from the character's short name in a story for a "
                                                 "set the card was printed in; the page does not name the card.",
                                   "pages": sh[:5], "pages_total": len(sh)})
        if art.get(o):
            ev.append({"tier": "ART_ON_OFFICIAL_PAGE", "grade": "NAVIGATION_ONLY", "urls": sorted(art[o])[:5],
                       "urls_total": len(art[o])})
        tiers = [e["tier"] for e in ev]
        if set(tiers) & {"CLAIM_ANCHORED", "OFFICIAL_TEXT_NAMES_CARD", "SHORT_NAME_IN_SET_STORY"}:
            status, reason = "LINKED", None
        elif tiers:
            status, reason = "ART_ONLY", "official page shows the art; no text evidence about the card"
        else:
            status = "NO_LORE_YET"
            reason = ("UNIVERSES_BEYOND: not part of official Magic story canon" if is_ub else
                      "NO_OFFICIAL_TEXT_MATCH: no exact-name, same-set short-name or claim evidence in the 652 cached pages")
            reasons[reason.split(":")[0]] += 1
        counts[status] += 1
        for t in tiers:
            counts["tier:" + t] += 1
        cards.append({"oracle_id": o, "name": name, "status": status, "no_lore_reason": reason,
                      "universes_beyond": is_ub, "sets": sorted(sets[o]), "evidence": ev,
                      "scryfall_uri": (c or {}).get("scryfall_uri", "").split("?")[0]})
    body = {"schema": SCHEMA,
            "status": "PRELIMINARY_RESEARCH (mechanical evidence links; not owner approved; not certified)",
            "scope": "priority-pool cards in data/card_enrichment.json whose Lore line reads '❓ No lore entry …'",
            "card_data_source": {"provider": "Scryfall", "snapshot": SNAPSHOT, "oracle": Path(oracle_file).name,
                                 "default": Path(default_file).name},
            "story_source": "cached official magic.wizards.com pages from data/primary_sources.csv and "
                            "data/story_extra_sources.csv",
            "pages_scanned": len(pages), "pool": len(pool),
            "counts": dict(sorted(counts.items())), "no_lore_reasons": dict(sorted(reasons.items())),
            "rule": __doc__.split("Evidence tiers")[1].strip(), "cards": cards}
    body["content_sha256"] = sha(cards)
    return body


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true", help="fail if the committed overlay is stale")
    a = ap.parse_args()
    body = build()
    if a.check:
        old = json.loads(OUT.read_text(encoding="utf-8"))
        if old.get("content_sha256") != body["content_sha256"]:
            print("STALE card lore links: rerun scripts/build_card_lore_links.py")
            return 1
        print("PASS card lore links current:", body["counts"])
        return 0
    OUT.write_text(json.dumps(body, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print("wrote", OUT.relative_to(ROOT), body["pool"], body["counts"], body["no_lore_reasons"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
