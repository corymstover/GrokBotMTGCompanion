#!/usr/bin/env python3
"""Per-entry retrieval index for lore material (Bot cycle 31, Phase 7 priority 1).

Reads the 7 lore entry pages (lore_lib.ENTRY_PAGES) and writes
  data/lore_entries.json   one record per entry: page, kind, name, anchor, computed tags, official citations,
                           flag counts, and internal links grouped by target (cards, characters, dossiers, planes, items,
                           arcs, eras, retcons) — pointers only, no new facts
  Lore Entry Index.md      the same as a browsable table (one row per entry, grouped by kind)
Tags are computed from what the entry already says: its kind, the flags it carries (has-secondary ⚠️ · has-unknowns ❓ ·
has-non-canonical 🚫 · has-retcon 🔄), the spark state on the summary tables (dossiers/characters), and whether it
links cards. kb_find.py indexes these records, so `python3 scripts/kb_find.py sylex` returns the item entry's anchor.

  python3 scripts/build_lore_index.py           write both files
  python3 scripts/build_lore_index.py --check   exit 1 if either is stale (run by scripts/check_lore.py)
"""
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import quote as urlq

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lore_lib as L  # noqa: E402

ROOT = L.ROOT
OUT = ROOT / "data" / "lore_entries.json"
PAGE = ROOT / "Lore Entry Index.md"
TARGET = {"Characters Index.md": "characters", "Planeswalker Dossiers.md": "dossiers", "Planes Index.md": "planes",
          "Items & Artifacts Index.md": "items", "Conflicts & Arcs.md": "arcs", "Master Timeline.md": "eras",
          "Contradictions & Retcons Log.md": "retcons", "Story Arc Summaries.md": "arcs",
          "Omenpath & Multiverse Connections.md": "planes"}
FLAG_TAG = {"secondary": "secondary", "unknown": "unknowns", "non-canonical": "non-canonical", "retcon": "retcon"}
KIND_ORDER = ["arc", "era", "dossier", "character", "plane", "item", "retcon"]
KIND_LABEL = {"arc": "Arcs (Conflicts & Arcs)", "era": "Eras (Master Timeline)", "dossier": "Planeswalker Dossiers",
              "character": "Characters", "plane": "Planes (detailed entries)", "item": "Items & artifacts", "retcon": "Retcons & contradictions"}


def spark_states():
    """{entry name: spark tag} from the Characters Index 'Status at a glance' table (the owner of status)."""
    import check_lore  # noqa: E402
    out = {}
    for name, status in check_lore.glance().items():
        c = check_lore.cls_index(status)
        for k in ("dead", "lost", "faded", "given", "kept"):
            if k in c:
                out[name] = {"dead": "dead", "lost": "spark-lost", "faded": "spark-faded", "given": "spark-given-up", "kept": "planeswalker"}[k]
                break
        else:
            out[name] = "status-unknown" if status.strip().startswith(("❓", "⚠️")) else "alive-or-active"
    return out


def record(e, sparks):
    t = e["text"]
    groups = defaultdict(set)
    for dest, frag in L.links(t, e["page"]):
        if dest.startswith("cards/"):
            groups["cards"].add(f"{dest}#{frag}")
        elif dest in TARGET and not (dest == e["page"] and not frag):
            if dest == e["page"] and frag == e["anchor"]:
                continue
            groups[TARGET[dest]].add(f"{dest}#{frag}" if frag else dest)
    fl = L.flags(t)
    tags = [e["kind"]] + ["has-" + FLAG_TAG[v] for v in fl if v != "confirmed"]
    if e["kind"] in ("dossier", "character") and " & " not in e["name"]:  # shared entries (Rowan & Will) get no spark tag
        key = e["name"] if e["name"] in sparks else next((k for k in sparks if k.split()[0] == e["name"].split()[0]), None)
        if key:
            tags.append(sparks[key])
    if groups.get("cards"):
        tags.append("has-cards")
    return {"page": e["page"], "kind": e["kind"], "name": e["name"], "anchor": e["anchor"],
            "tags": sorted(set(tags), key=tags.index), "citations": len(L.official_urls(t)), "flags": fl,
            "links": {k: sorted(v) for k, v in sorted(groups.items())}}


def build():
    sparks = spark_states()
    recs = [record(e, sparks) for e in L.all_entries()]
    return {"generated_by": "scripts/build_lore_index.py", "entries": len(recs),
            "by_kind": dict(Counter(r["kind"] for r in recs)), "items": recs}


def page(d):
    recs = d["items"]
    n_c = sum(r["citations"] for r in recs)
    L_ = ["---", 'title: "Lore Entry Index"', "PLACEHOLDER", "---", "", "# Lore Entry Index", "",
          "> **Generated** by `scripts/build_lore_index.py` (Bot cycle 31, Phase 7 — retrieval for lore material). One row per entry on the seven lore entry pages; do not hand-edit. "
          "Tags are computed from what each entry already says (kind; `has-secondary` ⚠️ · `has-unknowns` ❓ · `has-non-canonical` 🚫 · `has-retcon` 🔄 when the entry carries that flag; spark state from [Characters Index → Status at a glance](Characters%20Index.md#status-at-a-glance), card links). "
          "Links = internal links from the entry, by target (C = cards, Ch = characters, D = dossiers, P = planes, I = items, A = arcs, E = eras, R = retcons). Machine-readable copy: `data/lore_entries.json`; search with `python3 scripts/kb_find.py <words> --category lore`.",
          f"> **{len(recs)} entries** · " + " · ".join(f"{KIND_LABEL[k].split(' (')[0]} {d['by_kind'].get(k, 0)}" for k in KIND_ORDER) + f" · {n_c} official citations (distinct URLs per entry, summed). Every entry cites ≥ 1 official page (`scripts/check_lore.py`).", "",
          "## Contents"] + [f"- [{KIND_LABEL[k]}](#{L.anchor(KIND_LABEL[k])})" for k in KIND_ORDER] + [""]
    ab = {"cards": "C", "characters": "Ch", "dossiers": "D", "planes": "P", "items": "I", "arcs": "A", "eras": "E", "retcons": "R"}
    for k in KIND_ORDER:
        L_ += [f"## {KIND_LABEL[k]}", "", "| Entry | Tags | Cites | Links |", "|---|---|---|---|"]
        for r in recs:
            if r["kind"] != k:
                continue
            links = " ".join(f"{ab[g]} {len(v)}" for g, v in r["links"].items())
            name = r["name"].replace("|", "\\|")
            L_.append(f"| [{name}]({urlq(r['page'])}#{r['anchor']}) | {', '.join('`' + t + '`' for t in r['tags'])} | {r['citations']} | {links or '—'} |")
        L_.append("")
    return "\n".join(L_) + "\n"


def dump(d):
    return json.dumps(d, ensure_ascii=False, indent=1) + "\n"


def render():
    d = build()
    text = page(d)
    pf = ROOT / "Lore Entry Index.md"
    old = pf.read_text(encoding="utf-8") if pf.exists() else ""
    m = L.FM.match(old)
    fm = m.group(0) if m else "---\nPLACEHOLDER\n---\n\n"
    body = text.split("---\n", 2)[2].lstrip("\n")
    return d, fm + body


def main(argv):
    d, text = render()
    if "--check" in argv:
        bad = []
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != dump(d):
            bad.append("data/lore_entries.json stale")
        if not PAGE.exists() or L.body(PAGE) != L.FM.sub("", text, count=1):
            bad.append("Lore Entry Index.md stale")
        print(f"lore index: {d['entries']} entries; " + ("up to date" if not bad else "; ".join(bad) + " — run python3 scripts/build_lore_index.py"))
        return 1 if bad else 0
    OUT.write_text(dump(d), encoding="utf-8")
    PAGE.write_text(text, encoding="utf-8")
    print(f"lore index: wrote {OUT.relative_to(ROOT)} and {PAGE.name} ({d['entries']} entries)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
