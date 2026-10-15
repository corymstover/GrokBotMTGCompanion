#!/usr/bin/env python3
"""Bidirectional cross-references between lore entries (Bot cycle 32, Phase 7 priority 2, issue #93).

Relations between the lore entries (lore_lib.ENTRY_PAGES) come from two places already on the pages:
  link     entry A's hand-written text links entry B (page#anchor of B's heading)
  mention  entry A's text names entry B: a character's full name (or an unambiguous first name such as "Karn"),
           an item's name or one of its &-separated parts, or a plane's unambiguous name. Matching is case-sensitive
           and whole-word. A mention is a pointer only; it adds no facts.
Every relation is made symmetric. Each entry ends with a generated block listing the related entries that its
hand-written text does not already link, grouped by kind, plus — for items — cards whose Scryfall name is the
item's name ("name match", not a canon claim):
  <!-- LOREXREF:START --> *Cross-references (generated):* Characters: … · Planes: … <!-- LOREXREF:END -->
So whenever A points at B, B's text or block points back at A. scripts/check_lore.py verifies that reciprocity
and that the blocks are current.
  python3 scripts/build_lore_xrefs.py           rewrite the blocks on the lore entry pages
  python3 scripts/build_lore_xrefs.py --check   exit 1 if any block is stale
"""
import atomic_io  # noqa: F401  atomic Path.write_text/write_bytes (Bot cycle 34)
import csv
import re
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import quote as urlq

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lore_lib as L  # noqa: E402

ROOT = L.ROOT
START, END = "<!-- LOREXREF:START -->", "<!-- LOREXREF:END -->"
BLOCK = re.compile(r"\n*<!-- LOREXREF:START -->.*?<!-- LOREXREF:END -->\n?", re.S)
ORDER = [("dossier", "Dossiers"), ("character", "Characters"), ("plane", "Planes"), ("item", "Items"),
         ("arc", "Arcs"), ("summary", "Arc summaries"), ("era", "Eras"), ("retcon", "Retcons")]
SKIP_FIRST = {"Will", "The", "Lord", "General", "High", "Queen", "King"}  # first names too common to match alone


def split_names(h):
    h = re.sub(r"\s*\([^)]*\)", "", h)
    parts = re.split(r"\s*(?:,|&| / | — | → )\s*", h)
    return [p.strip() for p in parts if p.strip()]


def aliases(entries):
    """{alias: entry key}; ambiguous aliases dropped unless one entry's heading is exactly the alias."""
    cand = defaultdict(set)
    exact = {}
    for e in entries:
        k = (e["page"], e["anchor"])
        if e["kind"] in ("character", "dossier", "item", "plane"):
            names = split_names(e["name"])
            if e["kind"] == "plane":
                names = [x.strip() for x in re.split(r"\s*→\s*", re.split(r"\s*[:(—]", e["name"])[0])]
            if e["kind"] == "character" and " / " in e["name"]:
                names = []  # group entries such as "Pinnacle / Sothera cast (…)" are reached by links only
            for n in names:
                n = re.sub(r"^(the|a|an) ", "", n, flags=re.I) if e["kind"] == "item" else n
                if len(n) >= 3:
                    cand[(e["kind"], n)].add(k)
                    if n == e["name"]:
                        exact[(e["kind"], n)] = k
                first = n.split()[0]
                if e["kind"] in ("character", "dossier") and len(n.split()) > 1 and len(first) >= 3 and first not in SKIP_FIRST:
                    cand[(e["kind"], first)].add(k)
    # a plane name that is the prefix of another era's name ("Ravnica" vs "Ravnica after the invasion") is ambiguous
    pl = {n for (kind, n) in cand if kind == "plane"}
    amb = {n for n in pl if any(x.startswith(n + " ") for x in pl)}
    out = {}
    for (kind, n), ks in cand.items():
        if kind == "plane" and n in amb:
            continue
        if len(ks) == 1:
            out[(kind, n)] = next(iter(ks))
        elif (kind, n) in exact:
            out[(kind, n)] = exact[(kind, n)]
    return out


def card_names():
    rows = {}
    for r in csv.DictReader((ROOT / "data" / "card_index.csv").open(encoding="utf-8")):
        rows.setdefault(r["name"], (r["shard"], r["anchor"]))
    return rows


def deck_pointers():
    """{(page, anchor): [(deck title, deck path)]} from data/lore_decks/lore_decks.json story_map (Bot cycle 32, #95)."""
    import json
    spec = json.loads((ROOT / "data" / "lore_decks" / "lore_decks.json").read_text(encoding="utf-8"))
    out = defaultdict(list)
    for d in spec["decks"]:
        for keys in d.get("story_map", {}).values():
            for k in keys:
                pg, _, a = k.partition("#")
                item = (d["title"].replace("Lore Deck — ", ""), f"decks/{d['slug']}.md")
                if item not in out[(pg, a)]:
                    out[(pg, a)].append(item)
    return out


def relations(entries):
    by_key = {(e["page"], e["anchor"]): e for e in entries}
    al = aliases(entries)
    rx = {a: re.compile(rf"(?<![\w-]){re.escape(a[1])}(?![\w-])") for a in al}
    rel = defaultdict(set)
    linked = defaultdict(set)
    for e in entries:
        k = (e["page"], e["anchor"])
        text = e["text"].split("\n", 1)[1] if "\n" in e["text"] else ""
        for dest, frag in L.links(text, e["page"]):
            t = (dest, frag)
            if t in by_key and t != k:
                linked[k].add(t)
                rel[k].add(t)
                rel[t].add(k)
        plain = re.sub(r"\]\([^)]*\)", "]", text)
        for a, t in al.items():
            if t != k and rx[a].search(plain):
                if by_key[t]["kind"] == "dossier" and e["kind"] != "character":
                    continue  # dossiers are reached through their Characters Index twin; avoid doubling every name
                rel[k].add(t)
                rel[t].add(k)
    return by_key, rel, linked


def block_for(e, by_key, rel, linked, cards):
    k = (e["page"], e["anchor"])
    show = sorted(rel[k] - linked[k] - {k}, key=lambda t: (t[0], t[1]))
    groups = defaultdict(list)
    for t in show:
        o = by_key[t]
        href = f"#{o['anchor']}" if o["page"] == e["page"] else f"{urlq(o['page'])}#{o['anchor']}"
        groups[o["kind"]].append(f"[{o['name']}]({href})")
    parts = [f"{label}: " + " · ".join(groups[kind]) for kind, label in ORDER if groups.get(kind)]
    dk = DECKS.get(k, [])
    if dk:
        parts.append("Lore decks: " + " · ".join(f"[{t}]({urlq(path)}#story-map)" for t, path in dk))
    if e["kind"] == "item":
        cm = []
        for n in split_names(e["name"]):
            n0 = re.sub(r"^(the|a|an) ", "", n, flags=re.I)
            for cand in (n, n0, "The " + n0):
                if cand in cards and not any(cand == c[0] for c in cm):
                    cm.append((cand, cards[cand]))
        linked_cards = {d for d, _ in L.links(e["text"], e["page"]) if d.startswith("cards/")}
        cm = [(n, s) for n, s in cm if s[0] not in linked_cards or True]
        own = {f"{d}#{f}" for d, f in L.links(e["text"], e["page"])}
        cm = [(n, s) for n, s in cm if f"{s[0]}#{s[1]}" not in own]
        if cm:
            parts.append("Cards (name match): " + " · ".join(f"[{n}]({s[0]}#{s[1]})" for n, s in cm))
    if not parts:
        return ""
    return f"{START}\n*Cross-references (generated by `scripts/build_lore_xrefs.py`; both directions):* " + " — ".join(parts) + f"\n{END}"


DECKS = {}


def render():
    global DECKS
    DECKS = deck_pointers()
    entries = L.all_entries()  # lore_lib strips existing blocks from entry text
    by_key, rel, linked = relations(entries)
    cards = card_names()
    blocks = {(e["page"], e["anchor"]): block_for(e, by_key, rel, linked, cards) for e in entries}
    out = {}
    for page in L.ENTRY_PAGES:
        p = ROOT / page
        full = p.read_text(encoding="utf-8")
        m = L.FM.match(full)
        fm, text = (m.group(0), full[m.end():]) if m else ("", full)
        text = BLOCK.sub("\n", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        secs = L.entries(page, raw=text)
        for e in reversed(secs):  # insert from the end so offsets stay valid
            b = blocks[(page, e["anchor"])]
            if not b:
                continue
            end = e["end"]
            chunk = text[e["start"]:end].rstrip("\n")
            text = text[:e["start"]] + chunk + "\n\n" + b + "\n" + ("\n" if end < len(text) else "") + text[end:].lstrip("\n")
        out[page] = fm + text
    return out, rel, blocks


def main(argv):
    out, rel, blocks = render()
    stale = [pg for pg, t in out.items() if (ROOT / pg).read_text(encoding="utf-8") != t]
    n_rel = sum(len(v) for v in rel.values()) // 2
    n_blk = sum(1 for b in blocks.values() if b)
    if "--check" in argv:
        print(f"lore xrefs: {n_rel} symmetric relations; {n_blk} blocks; " + (f"STALE: {stale} — run python3 scripts/build_lore_xrefs.py" if stale else "up to date"))
        return 1 if stale else 0
    for pg in stale:
        (ROOT / pg).write_text(out[pg], encoding="utf-8")
    print(f"lore xrefs: {n_rel} symmetric relations; {n_blk} blocks; {len(stale)} pages updated")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
