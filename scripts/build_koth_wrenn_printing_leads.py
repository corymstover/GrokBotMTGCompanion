#!/usr/bin/env python3
"""Phase 2 review of the Koth and Wrenn official-source leads at the printing level (2026-10-30).

For each Koth or Wrenn card name that appears verbatim on a cached official Wizards page, this
records what the page shows and which exact Scryfall printings, if any, that evidence picks out.

Evidence kinds, strongest first:
  COLLECTOR_NUMBER_IN_IMAGE_LABEL  the page's image label carries the set code and collector number
  ART_CREDIT_NAME_AND_ARTIST       an art caption gives the card name and an artist that the printing credits
  CAPTION_FRAME_TREATMENT          a caption names the card and its frame treatment (e.g. Borderless), with no artist
  NAMED_ON_OFFICIAL_PAGE           the full card name appears on the page; this does not identify a printing
  CHARACTER_PROSE_ONLY             the string names the characters in story prose; it is not a card reference

Only short single-line quotes, URLs, set codes, collector numbers and Scryfall ids are stored.
Nothing here sets a lore grade or approves anything.

  python3 scripts/build_koth_wrenn_printing_leads.py           # rebuild (needs .cache/story and the snapshot)
  python3 scripts/build_koth_wrenn_printing_leads.py --check   # self-hash + structure; full compare if caches exist
"""
import argparse
import glob
import gzip
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data/lore_research/koth_wrenn_printing_leads_2026-10-30.json"
STORY = ROOT / ".cache/story"
SNAP = ROOT / ".cache/multiverse"
SCHEMA = "koth-wrenn-printing-leads/v1"
KINDS = ["COLLECTOR_NUMBER_IN_IMAGE_LABEL", "ART_CREDIT_NAME_AND_ARTIST", "CAPTION_FRAME_TREATMENT",
         "NAMED_ON_OFFICIAL_PAGE", "CHARACTER_PROSE_ONLY"]

U = "https://magic.wizards.com/en/"
# (card name, page URL, exact cached line, kind, printing selector, note)
LEADS = [
    ("Koth, the Geomancer", U + "news/magic-story/the-legends-of-reality-fracture",
     "0248_MTGFRA_MainPair: Koth, the Geomancer", "COLLECTOR_NUMBER_IN_IMAGE_LABEL",
     {"set": "fra", "collector_number": "248"},
     "The image label names set FRA and collector number 248."),
    ("Koth of the Homestead", U + "news/magic-story/the-legends-of-reality-fracture",
     "0199_MTGFRA_MainPair: Koth of the Homestead", "COLLECTOR_NUMBER_IN_IMAGE_LABEL",
     {"set": "fra", "collector_number": "199"},
     "The image label names set FRA and collector number 199. The page describes a Koth who 'has known "
     "nothing but peace his entire life'; its place in the main timeline is not assessed here."),
    ("Koth, Fire of Resistance", U + "news/feature/planeswalkers-guide-to-phyrexia-all-will-be-one",
     "Koth, Fire of Resistance | Art by: Eric Wilkerson", "ART_CREDIT_NAME_AND_ARTIST",
     {"artist": "Eric Wilkerson"},
     "The same art appears on several printings; the caption does not say which one."),
    ("Wrenn and Seven", U + "news/magic-story/tangles-2021-09-03",
     "Wrenn and Seven | Art by: Heonhwa Choe", "ART_CREDIT_NAME_AND_ARTIST",
     {"artist": "Heonhwa", "artist_note": "Scryfall credits 'Heonhwa'; the caption says 'Heonhwa Choe'."},
     "The artist match uses Scryfall's shorter credit. The same art is reprinted; the caption does not say which printing."),
    ("Wrenn and Realmbreaker", U + "news/magic-story/episode-8-wrenn-and-eight",
     "Wrenn and Realmbreaker", "CAPTION_FRAME_TREATMENT",
     {"set": "mom", "border_color": "black"},
     "The plain caption, next to a separate Borderless caption, is read as the regular-frame printing; no artist is given."),
    ("Wrenn and Realmbreaker", U + "news/magic-story/episode-8-wrenn-and-eight",
     "Borderless Wrenn and Realmbreaker", "CAPTION_FRAME_TREATMENT",
     {"set": "mom", "border_color": "borderless"},
     "The caption names the borderless treatment; MOM has one borderless printing of the card."),
    ("Koth of the Hammer", U + "story/koth-planeswalker",
     "TITLE: Koth of the Hammer | Planeswalker | Magic: The Gathering", "NAMED_ON_OFFICIAL_PAGE", None,
     "The official planeswalker page is titled with the card name. That ties the card to the character, not to one printing."),
    ("Wrenn and Six", U + "news/magic-story/tangles-2021-09-03",
     "Wrenn and Six took a step\u2014one of their last together\u2014and put their massive foot down on the soil of Innistrad, deep within the Kessig forest.",
     "CHARACTER_PROSE_ONLY", None,
     "This is story prose about Wrenn and the treefolk Six; it is not a reference to the card or any printing."),
    ("Wrenn and Seven", U + "news/magic-story/episode-5-cathartic-reunion",
     None, "CHARACTER_PROSE_ONLY", None,
     "The MOM Episode 5 prose names Wrenn and the treefolk Seven; this is not a card reference."),
    ("Wrenn and Seven", U + "news/magic-story/the-brothers-war-chapter-5-exodus",
     None, "CHARACTER_PROSE_ONLY", None,
     "The BRO Chapter 5 prose names Wrenn and the treefolk Seven; this is not a card reference."),
]


def sha(body):
    return hashlib.sha256(json.dumps(body, sort_keys=True).encode()).hexdigest()


def page(url):
    for p in sorted(glob.glob(str(STORY / "*" / "*.txt"))):
        t = Path(p).read_text(encoding="utf-8")
        if t.split("\n", 1)[0] == "URL: " + url:
            return t.split("\n")
    raise FileNotFoundError(url)


def snapshot_printings(names):
    snaps = sorted(glob.glob(str(SNAP / "default-cards-*.jsonl.gz")))
    if not snaps:
        raise FileNotFoundError("default-cards snapshot")
    out = {n: [] for n in names}
    with gzip.open(snaps[-1], "rt", encoding="utf-8") as fh:
        for line in fh:
            c = json.loads(line)
            if c["name"] in out and c.get("lang") == "en" and "paper" in c.get("games", []):
                out[c["name"]].append(c)
    return Path(snaps[-1]).name, out


def select(cards, sel):
    keep = []
    for c in cards:
        if "set" in sel and c["set"] != sel["set"]:
            continue
        if "collector_number" in sel and c["collector_number"] != sel["collector_number"]:
            continue
        if "border_color" in sel and c["border_color"] != sel["border_color"]:
            continue
        if "artist" in sel and c.get("artist") != sel["artist"]:
            continue
        keep.append({"set": c["set"], "collector_number": c["collector_number"], "released_at": c["released_at"],
                     "artist": c.get("artist"), "border_color": c["border_color"], "scryfall_id": c["id"]})
    return sorted(keep, key=lambda r: (r["released_at"], r["set"], r["collector_number"]))


def build():
    snap, prints = snapshot_printings({lead[0] for lead in LEADS})
    rows = []
    for name, url, quote, kind, sel, note in LEADS:
        lines = page(url)
        if quote is None:
            hits = [l for l in lines if name in l]
            if not hits:
                raise ValueError(f"{name} not on {url}")
            quote = min(hits, key=len)[:240]
            if quote not in lines and not any(quote in l for l in lines):
                raise ValueError(quote)
        elif not (any(quote == l.strip() for l in lines) if kind != "CHARACTER_PROSE_ONLY"
                  else any(quote in l for l in lines)):
            raise ValueError(f"quote not verbatim on {url}: {quote}")
        matched = select(prints[name], {k: v for k, v in (sel or {}).items() if k != "artist_note"}) if sel else []
        if sel and not matched:
            raise ValueError(f"no printing for {name} {sel}")
        first = min(prints[name], key=lambda c: c["released_at"]) if prints[name] else None
        rows.append({"card": name, "url": url, "quote": quote, "kind": kind,
                     "printing_specific": kind in KINDS[:3], "selector": sel, "matched_printings": matched,
                     "first_paper_printing": None if not first else
                     {"set": first["set"], "collector_number": first["collector_number"], "released_at": first["released_at"]},
                     "note": note})
    body = {"schema": SCHEMA, "snapshot": snap, "source_text_embedded": "single-line quotes only",
            "counts": {k: sum(r["kind"] == k for r in rows) for k in KINDS},
            "printing_specific_leads": sum(r["printing_specific"] for r in rows),
            "matched_printings": sum(len(r["matched_printings"]) for r in rows),
            "leads": rows,
            "limitations": [
                "Only Koth and Wrenn card names that appear verbatim in the cached official pages are reviewed; a page that shows a card without naming it is missed.",
                "Same-art reprints and promos match an art credit equally; the caption does not choose among them.",
                "Grades, approvals and deck lists are unchanged."]}
    body["sha256"] = sha(body)
    return body


def structural_problems(d):
    p = []
    if d.get("schema") != SCHEMA:
        p.append("schema")
    if d.get("sha256") != sha({k: v for k, v in d.items() if k != "sha256"}):
        p.append("self-hash")
    for r in d.get("leads", []):
        if r["kind"] not in KINDS:
            p.append(f"kind {r['kind']}")
        if not r["url"].startswith("https://magic.wizards.com/"):
            p.append(f"non-Wizards url {r['url']}")
        if r["printing_specific"] != (r["kind"] in KINDS[:3]):
            p.append(f"printing_specific mismatch {r['card']}")
        if r["printing_specific"] and not r["matched_printings"]:
            p.append(f"no printings {r['card']}")
        if not r["printing_specific"] and r["matched_printings"]:
            p.append(f"printings on non-specific lead {r['card']}")
    return p


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    if a.check:
        d = json.loads(OUT.read_text(encoding="utf-8"))
        probs = structural_problems(d)
        try:
            fresh = build()
            if fresh != d:
                probs.append("stale: rebuild differs")
        except FileNotFoundError as e:
            print(f"caches absent ({e}); structural check only")
        print("PASS" if not probs else "FAIL " + "; ".join(probs))
        return 1 if probs else 0
    d = build()
    OUT.write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"counts": d["counts"], "printing_specific_leads": d["printing_specific_leads"],
                      "matched_printings": d["matched_printings"]}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
