#!/usr/bin/env python3
"""Retrieval index + lookup CLI for the knowledge base (Bot cycle 17, issue #65).

  python3 scripts/kb_find.py --build              write data/kb_index.json (pages + decks: front-matter, headings, anchors)
  python3 scripts/kb_find.py --check              exit 1 if data/kb_index.json is stale (step of scripts/validate_all.py)
  python3 scripts/kb_find.py "commander damage"   ranked pages/sections; exact card names also return the card entry
  python3 scripts/kb_find.py layers --category rules      filter by category (lore/edh/rules/cards/meta/deck)
  python3 scripts/kb_find.py --tag two-card-infinite      every entry carrying a tag
  python3 scripts/kb_find.py sylex --kind item            lore entries only (Bot cycle 31, #92): arc/era/dossier/character/plane/item/retcon
Lore entries (one per dossier, plane, item, retcon, character, arc, era; scripts/build_lore_index.py) are indexed with
their computed tags (e.g. spark-lost, unknown, secondary, non-canonical, has-cards) and point at page#anchor.
Scoring (simple, deterministic): per query word, title 5 · tag 4 · commander 4 · section heading 2; all words must hit.
Card facts stay in the card entries (data/card_index.csv); this index only points at them.
"""
import csv
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import front_matter as fm  # noqa: E402
from check_links import anchor  # noqa: E402

ROOT = fm.ROOT
OUT = ROOT / "data" / "kb_index.json"
HEAD = re.compile(r"^(#{2,3})\s+(.*?)\s*$", re.M)
FENCE = re.compile(r"```.*?```", re.S)


def entry(p, kind):
    text = p.read_text(encoding="utf-8")
    m = fm.FM.match(text)
    meta = fm.parse_fm(m.group(0)) if m else {}
    body = FENCE.sub("", fm.body_of(text))
    seen, heads = {}, []
    for lvl, h in HEAD.findall(body):
        a = anchor(h)
        k = seen.get(a, 0)
        seen[a] = k + 1
        if h != "Contents":
            heads.append([len(lvl), h, a if not k else f"{a}-{k}"])
    e = {"path": str(p.relative_to(ROOT)), "kind": kind, "title": meta.get("title", "").strip('"'),
         "category": meta.get("category"), "tags": fm.as_list(meta.get("tags", "[]")) or [], "headings": heads}
    for k in ("issues", "related"):
        if k in meta:
            e[k] = fm.as_list(meta[k])
    for k in ("kind", "commander", "color_identity", "bracket_floor", "game_changers", "two_card_infinites"):
        if kind == "deck" and k in meta:
            e["deck_" + k if k == "kind" else k] = meta[k].strip('"')
    return e


def lore_entries():
    import build_lore_index as B  # noqa: E402
    return [{"path": f"{r['page']}#{r['anchor']}", "kind": "entry", "entry_kind": r["kind"], "title": r["name"],
             "category": "lore", "tags": r["tags"], "headings": []} for r in B.build()["items"]]


def build():
    items = [entry(p, kind) for p, _, kind in fm.targets(shards=False)]
    lore = lore_entries()
    return {"schema": 2, "generated_by": "scripts/kb_find.py --build", "entries": len(items) + len(lore),
            "note": "Pages, decks and lore entries (Bot cycle 31); card entries are indexed by data/card_index.csv.", "items": items + lore}


def dump(d):
    return json.dumps(d, ensure_ascii=False, indent=0, sort_keys=False) + "\n"


def search(idx, words, cat=None, tag=None, ekind=None):
    words = [w.lower() for w in words]
    out = []
    for e in idx["items"]:
        if cat and e.get("category") != cat:
            continue
        if tag and tag not in e["tags"]:
            continue
        if ekind and e.get("entry_kind") != ekind:
            continue
        score, hits = 0, []
        for w in words:
            s = 0
            s += 5 if w in e["title"].lower() else 0
            s += 4 if any(w in t for t in e["tags"]) else 0
            s += 4 if w in e.get("commander", "").lower() else 0
            hh = [h for h in e["headings"] if w in h[1].lower()]
            s += 2 if hh else 0
            if not s:
                break
            score += s
            hits += hh
        else:
            if words:
                full = [h for h in e["headings"] if all(w in h[1].lower() for w in words)]
                out.append((score + 3 * bool(full), e, (full or hits)[:3]))
            else:
                out.append((0, e, []))
    out.sort(key=lambda x: (-x[0], x[1]["path"]))
    return out


def card_hits(q):
    rows = [r for r in csv.DictReader((ROOT / "data/card_index.csv").open(encoding="utf-8")) if r["name"].lower() == q.lower()]
    refs = {}
    rp = ROOT / "data/card_refs.json"
    if rp.exists():
        refs = json.loads(rp.read_text(encoding="utf-8")).get("cards", {})
    return [(r, refs.get(r["oracle_id"])) for r in rows]


def main(argv):
    if "--build" in argv:
        OUT.write_text(dump(build()), encoding="utf-8")
        print(f"kb_index: wrote {OUT.relative_to(ROOT)}")
        return 0
    if "--check" in argv:
        ok = OUT.exists() and OUT.read_text(encoding="utf-8") == dump(build())
        print("kb_index: " + ("up to date" if ok else "STALE — run python3 scripts/kb_find.py --build"))
        return 0 if ok else 1
    opt = lambda k: argv[argv.index(k) + 1] if k in argv else None
    cat, tag, lim, ek = opt("--category"), opt("--tag"), int(opt("--limit") or 10), opt("--kind")
    skip = {x for k in ("--category", "--tag", "--limit", "--kind") if k in argv for x in (k, argv[argv.index(k) + 1])}
    words = [w for w in argv if w not in skip]
    q = " ".join(words)
    for r, ref in card_hits(q) if q else []:
        print(f"CARD  {r['name']} → {r['shard']}#{r['anchor']}" + (f"  (referenced in {ref['n']} pages; see {ref['index']})" if ref else ""))
    idx = json.loads(OUT.read_text(encoding="utf-8"))
    res = search(idx, re.findall(r"[\w+'/-]+", q), cat, tag, ek)
    for score, e, hh in res[:lim]:
        what = f"{e['entry_kind']} entry" if e.get("kind") == "entry" else e.get("category")
        print(f"{score:>3}  {e['path']}  — {e['title']}  [{what}; {', '.join(e['tags'][:5])}]")
        for lvl, h, a in hh:
            print(f"       → {e['path']}#{a}  ({h})")
    if not res:
        print("no matches (try fewer words, or rg -n -i 'phrase' *.md)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
