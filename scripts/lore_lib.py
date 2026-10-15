#!/usr/bin/env python3
"""Shared parsing for the lore entry pages (Bot cycle 31, Phase 7).

An *entry* is one heading-delimited unit on a lore page (a dossier, a plane, an item, a retcon, a character, an arc, an era).
ENTRY_PAGES says, per page, which headings are entries. Everything here is read-only parsing: no facts are produced,
only pointers (anchors, links, citation URLs, flags) that already exist on the pages.
"""
import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
FM = re.compile(r"\A---\n.*?\n---\n\n?", re.S)
LINK = re.compile(r"(?<!!)\[([^\]]*)\]\(([^)\s]+)\)")
URL = re.compile(r"https?://[^\s)\]>|]+")
OFFICIAL = re.compile(r"^https?://([a-z0-9-]+\.)*wizards\.com/", re.I)
FLAGS = {"✅": "confirmed", "⚠️": "secondary", "❓": "unknown", "🚫": "non-canonical", "🔄": "retcon"}

# page: (entry kind, heading level of entries, container headings whose children are entries, headings that are never entries)
GEN_START = re.compile(r"^<!-- (?!LOREXREF)[A-Z-]+:START -->", re.M)
ENTRY_PAGES = {
    "Planeswalker Dossiers.md": ("dossier", 2, None, {"Contents", "Spark & allegiance summary", "Character cards (name-matched)"}),
    "Planes Index.md": ("plane", 3, {"Detailed plane entries"}, set()),
    "Items & Artifacts Index.md": ("item", 3, {"Artifacts", "Spells & world-scale magic"}, set()),
    "Contradictions & Retcons Log.md": ("retcon", 3, None, set()),
    "Characters Index.md": ("character", 3, None, set()),
    "Master Timeline.md": ("era", 3, {"A. In-universe eras"}, set()),
    "Conflicts & Arcs.md": ("arc", 0, None, set()),  # mixed levels, see MIXED
    "Story Arc Summaries.md": ("summary", 0, None, set()),  # Bot cycle 32 (#96): one entry per arc summary, mixed levels
}
ARC_CONTAINERS = {"Post–War of the Spark arcs (2019–2022)", "Phyrexian Invasion of the Multiverse", "Omenpath-era arcs (2024–2026)"}
ARC_SKIP = {"Contents", "Cross-arc threads", "Open questions"}
# mixed-level pages: every ## heading is an entry except containers (whose ### children are the entries) and skips
MIXED = {"arc": (ARC_CONTAINERS, ARC_SKIP),
         "summary": ({"The Phyrexian Invasion saga (2023)"}, {"Contents"})}


def anchor(h):
    """GitHub-style heading anchor (same rule as scripts/check_links.py)."""
    import check_links  # noqa: E402  (scripts/ is on sys.path for every caller)
    return check_links.anchor(h)


def body(path):
    return FM.sub("", Path(path).read_text(encoding="utf-8"), count=1)


def sections(text):
    """[(level, heading, start, end)] for ## and ### headings outside code fences."""
    heads = [(len(m.group(1)), m.group(2).strip(), m.start()) for m in re.finditer(r"^(#{2,3}) (.+)$", text, re.M)]
    out = []
    for i, (lvl, h, s) in enumerate(heads):
        e = len(text)
        for lvl2, _, s2 in heads[i + 1:]:
            if lvl2 <= lvl:
                e = s2
                break
        out.append((lvl, h, s, e))
    return out


XREF_BLOCK = re.compile(r"\n*<!-- LOREXREF:START -->.*?<!-- LOREXREF:END -->\n?", re.S)


def entries(page, raw=None):
    """Entries on one registered lore page: [{page, kind, name, anchor, text, start, end}] in page order.
    `text` has generated LOREXREF blocks removed (they are derived from these entries, Bot cycle 32);
    start/end are offsets into `raw` (default: the page body) for the generator that writes the blocks."""
    kind, lvl, containers, skip = ENTRY_PAGES[page]
    text = body(ROOT / page) if raw is None else raw
    secs = sections(text)
    seen, res = {}, []
    parent = None
    for l, h, s, e in secs:
        a = anchor(h)
        k = seen.get(a, 0)
        seen[a] = k + 1
        a = a if not k else f"{a}-{k}"
        if l == 2:
            parent = h
        if kind in MIXED:
            cont, skp = MIXED[kind]
            ok = (l == 2 and h not in cont | skp) or (l == 3 and parent in cont)
        else:
            ok = l == lvl and h not in skip and (containers is None or parent in containers)
            if kind == "retcon" and parent and (parent.startswith("Queue") or parent.startswith("Open")):
                ok = False
        if ok:
            # an entry ends before another generator's region (e.g. <!-- CHARCARDS:START --> after the last character)
            m = GEN_START.search(text, s, e)
            e = m.start() if m else e
            res.append({"page": page, "kind": kind, "name": h, "anchor": a, "text": XREF_BLOCK.sub("\n", text[s:e]), "start": s, "end": e})
    return res


def all_entries():
    return [e for p in ENTRY_PAGES for e in entries(p)]


def links(text, page):
    """Internal links → (dest page, anchor) resolved relative to the repo root."""
    out = []
    for _, t in LINK.findall(text):
        if re.match(r"^[a-z]+:", t):
            continue
        path, _, frag = t.partition("#")
        dest = unquote(path) if path else page
        out.append((dest, frag))
    return out


def official_urls(text):
    return sorted({u.rstrip(".,;") for u in URL.findall(text) if OFFICIAL.match(u)})


def flags(text):
    return {v: text.count(k) for k, v in FLAGS.items() if text.count(k)}
