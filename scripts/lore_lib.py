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
ENTRY_PAGES = {
    "Planeswalker Dossiers.md": ("dossier", 2, None, {"Contents", "Spark & allegiance summary", "Character cards (name-matched)"}),
    "Planes Index.md": ("plane", 3, {"Detailed plane entries"}, set()),
    "Items & Artifacts Index.md": ("item", 3, {"Artifacts", "Spells & world-scale magic"}, set()),
    "Contradictions & Retcons Log.md": ("retcon", 3, None, set()),
    "Characters Index.md": ("character", 3, None, set()),
    "Master Timeline.md": ("era", 3, {"A. In-universe eras"}, set()),
    "Conflicts & Arcs.md": ("arc", 0, None, set()),  # mixed levels, see arc_entries()
}
ARC_CONTAINERS = {"Post–War of the Spark arcs (2019–2022)", "Phyrexian Invasion of the Multiverse", "Omenpath-era arcs (2024–2026)"}
ARC_SKIP = {"Contents", "Cross-arc threads", "Open questions"}


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


def entries(page):
    """Entries on one registered lore page: [{page, kind, name, anchor, text}] in page order."""
    kind, lvl, containers, skip = ENTRY_PAGES[page]
    text = body(ROOT / page)
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
        if kind == "arc":
            ok = (l == 2 and h not in ARC_CONTAINERS | ARC_SKIP) or (l == 3 and parent in ARC_CONTAINERS)
        else:
            ok = l == lvl and h not in skip and (containers is None or parent in containers)
            if kind == "retcon" and parent and (parent.startswith("Queue") or parent.startswith("Open")):
                ok = False
        if ok:
            res.append({"page": page, "kind": kind, "name": h, "anchor": a, "text": text[s:e]})
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
