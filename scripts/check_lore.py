#!/usr/bin/env python3
"""Lore-specific validation (Bot cycle 31, Phase 7 priority 3). Step `lore-entries` of scripts/validate_all.py.

Checks, over the eight lore entry pages (lore_lib.ENTRY_PAGES: dossiers, planes, items, retcons, characters, arcs, arc summaries, eras):
  1 citations   every entry cites ≥ 1 official Wizards page (magic.wizards.com / *.wizards.com)
  2 rows        every dossier timeline row and every retcon statement row (Earlier / Later / Conflict) cites an official
                page or links a lore entry that does (delegated), or is explicitly a KB-internal note ("The KB …", ❓)
  3 anchors     every entry's computed anchor exists on its page (same rule as check_links.py)
  4 sparks      spark state agrees between the Characters Index (Status at a glance + Sparks after the Phyrexian
                Invasion), the dossier "Spark & allegiance summary" and the retcon log's spark rulings (KB treatment rows)
  5 index       data/lore_entries.json + Lore Entry Index.md are current (scripts/build_lore_index.py --check)
  6 xrefs       generated cross-reference blocks are current (scripts/build_lore_xrefs.py --check) and reciprocal:
                whenever entry A links entry B (hand-written or generated), B links A back (Bot cycle 32, #93)
Quote verification is its own step (`lore-quotes`, scripts/lore_quotes.py).
  python3 scripts/check_lore.py            all checks (exit 1 on any problem)
  python3 scripts/check_lore.py --sparks   print the spark comparison table
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lore_lib as L  # noqa: E402

ROOT = L.ROOT
SPARKLESS = {"lost", "faded", "given"}


def glance():
    c = L.body(ROOT / "Characters Index.md")
    c = c[c.index("## Status at a glance"):]
    c = c[:c.index("\n## ", 5)]
    return {m.group(1): m.group(2) for m in re.finditer(r"^\| \[([^\]]+)\]\(#[^)]+\) \| [^|]+ \| ([^|]+?) \|$", c, re.M)}


def cls_index(t):
    t = t.lower()
    s = set()
    if re.search(r"\b(dead|deceased|died|killed)\b", t):
        s.add("dead")
    if re.search(r"spark lost|former planeswalker|lost (her|his|their) spark|no longer a planeswalker", t):
        s.add("lost")
    if "spark faded" in t:
        s.add("faded")
    if re.search(r"gave (up )?(his|her|their) spark", t):
        s.add("given")
    if re.search(r"still a planeswalker|planeswalker \(|^✅ active", t):
        s.add("kept")
    if "spark status unknown" in t:
        s.add("unknown")
    return s


def cls_dossier(t):
    t = t.strip().lower()
    if t.startswith(("❓", "⚠️")):
        return {"unknown"}
    if t.startswith(("n/a", "see index")):
        return set()
    s = set()
    if "dead" in t:
        s.add("dead")
    if re.match(r"^lost\b", t) or "lost (" in t:
        s.add("lost")
    if "faded" in t:
        s.add("faded")
    if "given up" in t or "gave it" in t:
        s.add("given")
    if re.match(r"^(kept|active)", t):
        s.add("kept")
    return s


def dossier_summary():
    d = L.body(ROOT / "Planeswalker Dossiers.md")
    tab = re.search(r"## Spark & allegiance summary\n(.*?)\n\n", d, re.S).group(1)
    out = {}
    for row in tab.splitlines()[2:]:
        c = [x.strip() for x in row.strip("|").split("|")]
        out[c[0]] = c[2]
    return out


def sparks_table():
    """(sparkless names, still-Planeswalker names) from Characters Index → Sparks after the Phyrexian Invasion."""
    c = L.body(ROOT / "Characters Index.md")
    sec = c[c.index("## Sparks after the Phyrexian Invasion"):]
    row = next(l for l in sec.splitlines()[3:] if l.startswith("|"))
    lost, kept = [re.sub(r"\([^)]*\)|\[[^\]]*\]|\*\([^)]*\)\*", "", x) for x in row.strip("|").split("|")[:2]]
    names = lambda s: {w for w in re.findall(r"\b([A-Z][a-z]+(?:-[A-Z][a-z]+)?)\b", s)}
    return names(lost), names(kept)


def resolve(short, keys):
    return next((k for k in keys if k == short), None) or next((k for k in keys if k.split()[0] == short.split()[0]), None)


def spark_rows():
    g, ds = glance(), dossier_summary()
    lost, kept = sparks_table()
    rows, bad = [], []
    for short, cell in ds.items():
        for who in [p.strip() for p in short.split("&")] if "&" in short else [short]:
            sub = cell
            if "&" in short:  # "Rowan lost; Will ❓"
                m = re.search(rf"{who}\s+([^;]+)", cell)
                sub = m.group(1) if m else "❓"
            gk = resolve(who, g)
            a, b = cls_dossier(sub), cls_index(g.get(gk, "")) if gk else set()
            first = who.split()[0]
            t = "sparkless" if first in lost else "planeswalker" if first in kept else ""
            prob = ""
            if a - {"unknown"} and b - {"unknown"} and not (a & b):
                prob = "dossier vs Characters Index status disagree"
            elif a == {"unknown"} and b - {"unknown"}:
                prob = "dossier says ❓ but the Characters Index states it"
            elif t == "sparkless" and a - {"unknown"} and not (a & (SPARKLESS | {"dead"})):
                prob = "Sparks table says sparkless, dossier does not"
            elif t == "planeswalker" and a - {"unknown"} and "kept" not in a and "dead" not in a:
                prob = "Sparks table says still a Planeswalker, dossier does not"
            rows.append((who, sub, sorted(a), gk, sorted(b), t, prob))
            if prob:
                bad.append(f"sparks: {who}: {prob} (dossier '{sub}' · index '{g.get(gk, '—')[:60]}' · sparks table '{t or '—'}')")
    # retcon log spark rulings
    ds_cls = {r[0].split()[0]: set(r[2]) for r in rows}
    for e in L.entries("Contradictions & Retcons Log.md"):
        kb = re.search(r"^\| \*\*KB treatment\*\* \|(.*)$", e["text"], re.M)
        if not kb or "spark" not in kb.group(1).lower():
            continue
        line = kb.group(1)
        scope = line
        if re.search(r"\bthese (six|five|four|three|two)\b", line):
            er = re.search(r"^\| \*\*Earlier statement\*\* \|(.*)$", e["text"], re.M)
            scope = er.group(1) if er else line
        group = scope is not line  # "Treat these six as sparkless": every name in the Earlier statement
        for name in ds_cls:
            if not re.search(rf"\b{re.escape(name)}\b", scope):
                continue
            c = ds_cls[name]
            ruled = group or re.search(rf"\b{re.escape(name)}\b\s*(?:=|:)[^|]*?\b(?:sparkless|spark lost)", line)
            if ruled and ("sparkless" in line or "spark lost" in line) and c - {"unknown"} and not c & (SPARKLESS | {"dead"}):
                bad.append(f"sparks: retcon '{e['name']}' rules {name} sparkless; dossier summary says {sorted(c)}")
            if "carrying" in line and "spark" in line and re.search(rf"{name}[^.]*carrying", line) and "kept" not in c:
                bad.append(f"sparks: retcon '{e['name']}' says {name} carries a spark; dossier summary says {sorted(c)}")
    return rows, bad


def row_ok(line):
    if L.official_urls(line):
        return True
    if any(d in L.ENTRY_PAGES or d in ("Story Arc Summaries.md",) for d, _ in L.links(line, "")):
        return True
    return bool(re.search(r"\bThe KB\b|❓|not stated", line))


def main(argv):
    import check_links
    if "--sparks" in argv:
        for r in spark_rows()[0]:
            print(" | ".join(str(x) for x in r))
        return 0
    bad, E = [], L.all_entries()
    nrows = 0
    for e in E:
        if not L.official_urls(e["text"]):
            bad.append(f"citations: {e['page']} → {e['name']}: no official Wizards citation")
        if e["anchor"] not in check_links.anchors_of(ROOT / e["page"]):
            bad.append(f"anchors: {e['page']}#{e['anchor']} does not resolve")
        for line in e["text"].splitlines():
            stmt = e["kind"] == "retcon" and re.match(r"^\| \*\*(Earlier statement|Later / overriding statement|Conflict)\*\* \|", line)
            tl = e["kind"] == "dossier" and line.startswith("| ") and not line.startswith(("| When", "|---")) and line.count("|") >= 4
            if stmt or tl:
                nrows += 1
                if not row_ok(line):
                    bad.append(f"rows: {e['page']} → {e['name']}: uncited row: {line[:100]}")
    rows, sb = spark_rows()
    bad += sb
    import build_lore_index as B
    d, text = B.render()
    stale = (not B.OUT.exists() or B.OUT.read_text(encoding="utf-8") != B.dump(d)
             or not B.PAGE.exists() or L.body(B.PAGE) != L.FM.sub("", text, count=1))
    if stale:
        bad.append("index: data/lore_entries.json / Lore Entry Index.md stale — run python3 scripts/build_lore_index.py")
    import build_lore_xrefs as X
    out, rel, blocks = X.render()
    if any((ROOT / pg).read_text(encoding="utf-8") != t for pg, t in out.items()):
        bad.append("xrefs: generated cross-reference blocks stale — run python3 scripts/build_lore_xrefs.py")
    full = {}
    for page in L.ENTRY_PAGES:
        raw = L.body(ROOT / page)
        for e in L.entries(page, raw=raw):
            full[(page, e["anchor"])] = raw[e["start"]:e["end"]]
    nlinks = 0
    for k, t in full.items():
        for dest, frag in L.links(t, k[0]):
            b = (dest, frag)
            if b in full and b != k:
                nlinks += 1
                if not any((d2, f2) == k for d2, f2 in L.links(full[b], b[0])):
                    bad.append(f"xrefs: {k[0]}#{k[1]} → {b[0]}#{b[1]} has no link back")
    # lore decks (Bot cycle 32, #95): every story_map pointer resolves to an entry, and that entry links the deck back
    ndp = 0
    for (pg, a), decks in X.deck_pointers().items():
        for title, path in decks:
            ndp += 1
            if (pg, a) not in full:
                bad.append(f"decks: {path} story_map points at {pg}#{a}, which is not a lore entry")
            elif not any(d2 == path for d2, _ in L.links(full[(pg, a)], pg)):
                bad.append(f"decks: {pg}#{a} does not link back to {path}")
            dt = (ROOT / path).read_text(encoding="utf-8")
            if f"#{a})" not in dt:
                bad.append(f"decks: {path} story map does not link {pg}#{a} (re-run scripts/build_lore_decks.py)")
    kinds = {}
    for e in E:
        kinds[e["kind"]] = kinds.get(e["kind"], 0) + 1
    print(f"lore entries: {len(E)} entries (" + ", ".join(f"{k} {n}" for k, n in kinds.items()) + f"); {nrows} statement/timeline rows; "
          f"{len(rows)} spark states compared; {nlinks} entry→entry links + {ndp} deck→entry pointers, all reciprocal unless listed; {len(bad)} problems")
    for b in bad[:40]:
        print("  " + b)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
