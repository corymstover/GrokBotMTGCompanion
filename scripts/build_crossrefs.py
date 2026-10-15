#!/usr/bin/env python3
"""Bidirectional cross-references between cards, decks, EDH packages, rules and lore (Bot cycle 18, issue #66).

Writes (all generated, idempotent; facts only — name matches and pattern matches are labeled as such):
  1. Character cards: a "Character cards (name-matched)" table at the end of Characters Index and
     Planeswalker Dossiers → legendary cards named after each character (Scryfall names; not a canon claim).
  2. Deck "Cross-references" block in every deck (decks/, grixis/decks/): EDH Packages sub-packages present
     (Oracle-pattern matches, same patterns as EDH Packages), keywords → Keyword Encyclopedia, rules / story /
     lore sections that cite cards in the list, and the decks sharing the most cards. data/deck_packages.json
     feeds the "Used in decks" lines that scripts/build_packages.py prints under each sub-package.
  3. Reverse card index: references/<L>.md lists, for every card cited anywhere outside the card shards, every
     page and section that cites it, grouped by kind (decks · EDH · rules · lore & story · card data · meta);
     data/card_refs.json holds the compact counts.
  4. One "Referenced in" line per cited card entry (cards/), pointing at its reverse-index section — the shards
     gain a single line per cited card instead of the full list (ingest_scryfall.py renders the same line).
Usage:
  python3 scripts/build_crossrefs.py            apply everything (then: build_packages.py, front_matter.py, kb_find.py --build)
  python3 scripts/build_crossrefs.py --check    exit 1 if any generated block, reverse-index page, JSON or shard line is stale
"""
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import quote, unquote

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ingest_scryfall as ing  # noqa: E402
from check_links import anchor  # noqa: E402
import front_matter as fm  # noqa: E402

ROOT = ing.ROOT
REFS_DIR = ROOT / "references"
REFS_JSON = ROOT / "data" / "card_refs.json"
DECKPKG_JSON = ROOT / "data" / "deck_packages.json"
DECK_DIRS = ["decks", "grixis/decks"]
CARD_LINK = re.compile(r"(?<!!)\[([^\]]*)\]\(((?:\.\./)*cards/[^)#\s]+\.md)#([^)\s]+)\)")
HEAD = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
GROUPS = [("deck", "Decks"), ("edh", "EDH guides"), ("rules", "Rules"), ("lore", "Lore & story"), ("cards", "Card data"), ("meta", "Meta")]
EXCLUDE = {"Card Index.md", "Card Enrichment.md"}  # coverage indexes list cards; they are not references
CC_START, CC_END = "<!-- CHARCARDS:START -->", "<!-- CHARCARDS:END -->"
XR_START, XR_END = "<!-- CROSSREFS:START -->", "<!-- CROSSREFS:END -->"
STOP_FIRST = {"Lord", "Will", "The", "Lady", "Sir", "King", "Queen", "General", "Captain"}
REF_LINE = "- **Referenced in:**"
# Names shared by different characters, skipped inside group headings (the cards show another character):
AMBIGUOUS = {"Mirri"}  # Mirri cards are the Weatherlight's cat warrior, not the Sothera crew member


def esc_url(path):
    return quote(path, safe="/#")


def rel_link(from_path: Path, to: str):
    depth = len(from_path.relative_to(ROOT).parts) - 1
    return "../" * depth + esc_url(to)


def index_rows():
    rows = list(csv.DictReader(ing.INDEX_CSV.open(encoding="utf-8")))
    return rows, {(r["shard"], r["anchor"]): r for r in rows}, {r["name"]: r for r in rows}


def meta_of(p):
    m = fm.FM.match(p.read_text(encoding="utf-8"))
    return fm.parse_fm(m.group(0)) if m else {}


# ------------------------------------------------------------------ sections + card links in a page
def scan(p: Path, text: str):
    """Yield (shard, anchor, section_anchor, section_title) for every card-entry link in the page."""
    seen = Counter()
    sec_a, sec_t = "", ""
    fence = False
    for line in text.splitlines():
        if line.startswith("```"):
            fence = not fence
            continue
        if fence:
            continue
        m = HEAD.match(line)
        if m:
            a = anchor(m.group(2))
            a2 = a if not seen[a] else f"{a}-{seen[a]}"
            seen[a] += 1
            if len(m.group(1)) > 1 and m.group(2) != "Contents":
                sec_a, sec_t = a2, re.sub(r"[*`\[\]]", "", m.group(2))
                sec_t = re.sub(r"\(([^)]*)\)", r"(\1)", sec_t)
            continue
        for _, target, anc in CARD_LINK.findall(line):
            dest = (p.parent / unquote(target)).resolve()
            try:
                shard = str(dest.relative_to(ROOT))
            except ValueError:
                continue
            yield shard, unquote(anc), sec_a, sec_t


def page_kind(rel, meta):
    if rel.startswith(("decks/", "grixis/decks/")):
        return "deck"
    return meta.get("category", "meta")


def deck_label(rel, meta):
    c = meta.get("commander", "").strip('"') or Path(rel).stem
    k = meta.get("kind")
    if k == "grixis":
        return f"{c} (Grixis)"
    if k == "plane":
        return f"{c} ({meta.get('plane', '').title()}-only)"
    if k == "theme":
        return f"{c} ({meta.get('theme', '').replace('-', ' ')} theme)"
    return c


def source_pages():
    out = [ROOT / n for n in sorted(fm.PAGES) if (ROOT / n).exists() and n not in EXCLUDE]
    for d in DECK_DIRS:
        out += sorted((ROOT / d).glob("*.md"))
    return out


# ------------------------------------------------------------------ 1. character cards
def char_names(page):
    text = (ROOT / page).read_text(encoding="utf-8")
    lvl = "### " if page == "Characters Index.md" else "## "
    names = []
    skip = {"Contents", "Spark & allegiance summary", "Status at a glance", "Open questions"}
    for line in text.splitlines():
        if line.startswith(lvl) and not line.startswith(lvl + "#"):
            h = line[len(lvl):].strip()
            if h in skip or h.startswith("Character cards"):
                continue
            names.append(h)
    return names


def split_names(h):
    inner = re.findall(r"\(([^)]*)\)", h)
    base = re.sub(r"\([^)]*\)", "", h)
    parts = [x.strip() for x in re.split(r",|/", base) if x.strip()]
    for i in inner:
        parts += [x.strip() for x in i.split(",") if x.strip()]
    parts = [x for x in parts if x and not x.endswith(" cast")]
    if len(parts) > 1:
        parts = [x for x in parts if x not in AMBIGUOUS]
    return parts or [h]


def char_cards(names, bulk_by_name, rows_by_name):
    legend = []
    for name, r in rows_by_name.items():
        c = bulk_by_name.get(name)
        if c and "Legendary" in (c.get("type_line") or ""):
            legend.append((name.split(" // ")[0], name))
    out = {}
    for h in names:
        hits = set()
        for n in split_names(h):
            keys = {n}
            first = n.split()[0]
            if " " in n and first not in STOP_FIRST and len(first) >= 3:
                keys.add(first)
            for front, full in legend:
                for k in keys:
                    if front == k or front.startswith(k + ",") or front.startswith(k + " "):
                        hits.add(full)
        out[h] = sorted(hits)
    return out


def charcards_block(page, mapping, rows_by_name):
    p = ROOT / page
    L = [CC_START, "## Character cards (name-matched)", "",
         "> Generated by `scripts/build_crossrefs.py` (Bot cycle 18, [#66](https://github.com/corymstover/GrokBotMTGCompanion/issues/66)). "
         "Legendary cards whose Scryfall name is the character's name, or starts with it (e.g. *Jace, …*). **A name match only:** it is not a claim about canon, timing or which version of the character a card shows; Echoverse and Universes Beyond versions are included when the name matches. Each card entry links back here through its *Referenced in* line.", "",
         "| Character | Cards | Count |", "|---|---|---|"]
    n = 0
    for h, cards in mapping.items():
        if not cards:
            continue
        n += len(cards)
        links = " · ".join(f"[{c}]({rel_link(p, rows_by_name[c]['shard'])}#{rows_by_name[c]['anchor']})" for c in cards)
        L.append(f"| [{h}](#{anchor(h)}) | {links} | {len(cards)} |")
    L += ["", f"{sum(1 for v in mapping.values() if v)} of {len(mapping)} characters have name-matched cards ({n} card links).", CC_END]
    return "\n".join(L)


def put_block(text, start, end, block, before=None, contents_line=None):
    if start in text:
        a, b = text.index(start), text.index(end) + len(end)
        text = text[:a] + block + text[b:]
    else:
        if before and before in text:
            i = text.index(before)
            text = text[:i] + block + "\n\n" + text[i:]
        else:
            text = text.rstrip("\n") + "\n\n" + block + "\n"
    if contents_line and contents_line not in text and "## Contents\n" in text:
        i = text.index("## Contents\n") + len("## Contents\n")
        j = text.find("\n\n", i)
        text = text[:j] + "\n" + contents_line + text[j:]
    return text


# ------------------------------------------------------------------ 2. deck blocks
def deck_cards(p):
    m = re.search(r"## Decklist[^\n]*\n.*?```[^\n]*\n(.*?)```", p.read_text(encoding="utf-8"), re.S)
    out = []
    for l in (m.group(1) if m else "").splitlines():
        mm = re.match(r"^(\d+)x?\s+(.+?)(?:\s+\([^)]+\)\s+\S+)?(?:\s+\*[A-Z]\*)?\s*(?:\[(.*)\])?\s*$", l.strip())
        if mm and "companion" not in (mm.group(3) or "").lower():
            out.append(mm.group(2).strip())
    return out


def package_matcher():
    import build_packages as bp
    from edh_lib import Data
    subs = []
    for name, _plan, sp in bp.PKG:
        for lab, pat, kw in sp:
            subs.append((f"{name}: {lab}", re.compile(pat, re.I), kw))

    def match(c):
        t = Data.ftype(c)
        tx = Data.text(c)
        hits = []
        for full, rx, kw in subs:
            kind = kw.get("kind", "nonland")
            if kind == "nonland" and "Land" in t.split("—")[0] and "Creature" not in t:
                continue
            if kind == "land" and "Land" not in t:
                continue
            if kw.get("types") and not re.search(kw["types"], t):
                continue
            if kw.get("maxmv") is not None and (c.get("cmc") or 0) > kw["maxmv"]:
                continue
            if not rx.search(tx) or (kw.get("excl") and re.search(kw["excl"], tx, re.I)):
                continue
            hits.append(full)
        return hits
    return match, [s[0] for s in subs]


def kw_anchors():
    out = {}
    seen = Counter()
    for line in (ROOT / "Keyword Encyclopedia.md").read_text(encoding="utf-8").splitlines():
        m = HEAD.match(line)
        if m:
            a = anchor(m.group(2))
            a2 = a if not seen[a] else f"{a}-{seen[a]}"
            seen[a] += 1
            if len(m.group(1)) == 4:
                out.setdefault(m.group(2).strip().lower(), a2)
    return out


def pkg_anchor(full):
    return anchor(full)


# ------------------------------------------------------------------ build everything in memory
def build():
    rows, by_key, rows_by_name = index_rows()
    cards, bulk_date = ing.get_bulk(ing.DEFAULT_CACHE, None)
    by_oid = {c["oracle_id"]: c for c in cards}
    bulk_by_name = {r["name"]: by_oid.get(r["oracle_id"]) for r in rows}
    files = {}  # path -> new text

    # 1. character cards
    for page, before in (("Characters Index.md", "## Open questions"), ("Planeswalker Dossiers.md", None)):
        p = ROOT / page
        mapping = char_cards(char_names(page), bulk_by_name, rows_by_name)
        files[p] = put_block(p.read_text(encoding="utf-8"), CC_START, CC_END, charcards_block(page, mapping, rows_by_name),
                             before=before, contents_line="- [Character cards (name-matched)](#character-cards-name-matched)")

    # 3a. reverse references from all source pages (character blocks included; deck blocks add no card links)
    def collect():
        refs = defaultdict(dict)  # oid -> {page_rel: [kind, label, [(sec_a, sec_t)], count]}
        for p in source_pages():
            rel = str(p.relative_to(ROOT))
            text = files.get(p) or p.read_text(encoding="utf-8")
            meta = fm.parse_fm(fm.FM.match(text).group(0)) if fm.FM.match(text) else {}
            kind = page_kind(rel, meta)
            label = deck_label(rel, meta) if kind == "deck" else (meta.get("title", "").strip('"') or p.stem)
            for shard, anc, sa, st in scan(p, text):
                r = by_key.get((shard, anc))
                if not r:
                    continue
                e = refs[r["oracle_id"]].setdefault(rel, [kind, label, [], 0])
                e[3] += 1
                if (sa, st) not in e[2]:
                    e[2].append((sa, st))
        return refs
    refs = collect()

    # 2. deck blocks
    match, sub_names = package_matcher()
    kwa = kw_anchors()
    deck_sets, deck_meta, deck_pkg = {}, {}, {}
    name_to_card = {}
    for c in cards:
        if c.get("layout") not in ing.EXCLUDED_LAYOUTS:
            name_to_card.setdefault(c["name"], c)
            for f in c.get("card_faces") or []:
                name_to_card.setdefault(f["name"], c)
    deck_files = [p for d in DECK_DIRS for p in sorted((ROOT / d).glob("*.md"))]
    for p in deck_files:
        names = deck_cards(p)
        cs = [name_to_card[n] for n in names if n in name_to_card]
        deck_sets[p] = {c["oracle_id"] for c in cs}
        deck_meta[p] = meta_of(p)
        pk = defaultdict(list)
        for c in cs:
            for s in match(c):
                pk[s].append(c["name"])
        deck_pkg[p] = pk
    for p in deck_files:
        rel = str(p.relative_to(ROOT))
        cs = [by_oid[o] for o in deck_sets[p] if o in by_oid]
        pk = deck_pkg[p]
        L = [XR_START, "## Cross-references", "",
             "> Generated by `scripts/build_crossrefs.py` (Bot cycle 18, [#66](https://github.com/corymstover/GrokBotMTGCompanion/issues/66)) from this list. "
             "Package counts are Oracle-text pattern matches using the [EDH Packages](" + rel_link(p, "EDH Packages.md") + ") patterns, so a card can fit loosely or count in several packages. Facts, not advice. "
             "Every card entry also lists where else it is cited (*Referenced in* → the [reverse card index](" + rel_link(p, "references/README.md") + ")).", ""]
        if pk:
            L.append("- **EDH packages in this list:** " + " · ".join(
                f"[{s}]({rel_link(p, 'EDH Packages.md')}#{pkg_anchor(s)}) {len(v)}" for s, v in sorted(pk.items(), key=lambda x: (-len(x[1]), x[0]))))
        kc = Counter()
        for c in cs:
            for k in c.get("keywords") or []:
                if k.lower() in kwa:
                    kc[k] += 1
        if kc:
            L.append("- **Keywords → [Keyword Encyclopedia](" + rel_link(p, "Keyword Encyclopedia.md") + "):** " + " · ".join(
                f"[{k}]({rel_link(p, 'Keyword Encyclopedia.md')}#{kwa[k.lower()]}) {n}" for k, n in sorted(kc.items(), key=lambda x: (-x[1], x[0]))[:12]))
        for kind, head in (("rules", "Rules sections citing cards in this list"), ("lore", "Lore & story sections citing cards in this list"),
                           ("edh", "EDH guide sections citing cards in this list")):
            secs = defaultdict(set)
            for o in deck_sets[p]:
                for prel, (k, label, ss, _n) in refs.get(o, {}).items():
                    if k == kind and not prel.startswith("grixis/decks"):
                        for sa, st in ss:
                            secs[(prel, label, sa, st)].add(by_oid[o]["name"] if o in by_oid else o)
            if secs:
                items = sorted(secs.items(), key=lambda x: (-len(x[1]), x[0][0], x[0][3]))
                cap = 8 if kind != "edh" else 6
                parts = []
                for (prel, label, sa, st), names in items[:cap]:
                    ex = sorted(names)
                    more = f" +{len(ex) - 3}" if len(ex) > 3 else ""
                    parts.append(f"[{label} → {st}]({rel_link(p, prel)}#{sa}) ({', '.join(ex[:3])}{more})" if sa else f"[{label}]({rel_link(p, prel)}) ({', '.join(ex[:3])}{more})")
                extra = f" · …{len(items) - cap} more sections" if len(items) > cap else ""
                L.append(f"- **{head}:** " + " · ".join(parts) + extra)
        sims = sorted(((len(deck_sets[p] & deck_sets[q]), q) for q in deck_files if q != p), key=lambda x: (-x[0], str(x[1])))[:4]
        L.append("- **Decks sharing the most cards:** " + " · ".join(
            f"[{deck_label(str(q.relative_to(ROOT)), deck_meta[q])}]({rel_link(p, str(q.relative_to(ROOT)))}) {n}" for n, q in sims if n))
        L.append(XR_END)
        files[p] = put_block(p.read_text(encoding="utf-8"), XR_START, XR_END, "\n".join(L), contents_line="- [Cross-references](#cross-references)")

    dp = {"generated_by": "scripts/build_crossrefs.py", "note": "Oracle-pattern matches of each deck list against the EDH Packages sub-packages",
          "packages": {}}
    for s in sub_names:
        used = []
        for p in deck_files:
            if len(deck_pkg[p].get(s, [])) >= 3:
                used.append({"deck": str(p.relative_to(ROOT)), "label": deck_label(str(p.relative_to(ROOT)), deck_meta[p]), "cards": len(deck_pkg[p][s])})
        used.sort(key=lambda x: (-x["cards"], x["deck"]))
        dp["packages"][s] = used
    files[DECKPKG_JSON] = json.dumps(dp, indent=1, ensure_ascii=False) + "\n"

    # 3b. reverse index pages + json
    by_letter = defaultdict(list)
    for o, pages in refs.items():
        r = next((x for x in rows if x["oracle_id"] == o), None) if False else None
    oid_row = {r["oracle_id"]: r for r in rows}
    for o in refs:
        r = oid_row[o]
        by_letter[r["shard"].split("/")[1]].append(r)
    jcards = {}
    REFS_DIR.mkdir(exist_ok=True)
    letters = sorted(by_letter)
    for L_ in letters:
        p = REFS_DIR / f"{L_}.md"
        rs = sorted(by_letter[L_], key=lambda r: (ing.ascii_key(r["name"]), r["name"]))
        seen = Counter()
        out = [f"# Reverse card index — {L_}", "",
               "> Generated by `scripts/build_crossrefs.py` (Bot cycle 18, [#66](https://github.com/corymstover/GrokBotMTGCompanion/issues/66)). "
               "For each card cited outside the card shards: every page and section that cites it, grouped by kind. "
               "The card entry's *Referenced in* line links here. Index: [README](README.md).", "",
               f"**{len(rs)} cards referenced.**", ""]
        for r in rs:
            a = anchor(r["name"])
            a2 = a if not seen[a] else f"{a}-{seen[a]}"
            seen[a] += 1
            pages = refs[r["oracle_id"]]
            kc = Counter(v[0] for v in pages.values())
            summary = " · ".join(f"{dict(GROUPS)[k].lower()} {kc[k]}" for k, _ in GROUPS if kc[k])
            out += [f"### {r['name']}", "", f"[Card entry]({rel_link(p, r['shard'])}#{r['anchor']}) · **{len(pages)} pages** ({summary})", ""]
            for k, head in GROUPS:
                items = sorted(((rel, v) for rel, v in pages.items() if v[0] == k), key=lambda x: (x[1][1].lower(), x[0]))
                if not items:
                    continue
                parts = []
                for rel, (kind, label, ss, n) in items:
                    if kind == "deck" or not ss or not ss[0][0]:
                        parts.append(f"[{label}]({rel_link(p, rel)})")
                    else:
                        more = f" (+{len(ss) - 1} more)" if len(ss) > 1 else ""
                        parts.append(f"[{label} → {ss[0][1]}]({rel_link(p, rel)}#{ss[0][0]}){more}")
                out.append(f"- **{head} ({len(items)}):** " + " · ".join(parts))
            en = enrichment().get(r["oracle_id"])
            if en and en["lore"]["relations"]:
                rl = en["lore"]["relations"]
                out.append(f"- **Lore entries ({len(rl)}; [card enrichment](../Card%20Enrichment.md), Bot cycle 33):** " + " · ".join(
                    f"[{x['name']}]({rel_link(p, x['entry'].split('#')[0])}#{x['entry'].split('#', 1)[1]}) ({x['relation']})" for x in rl))
            out.append("")
            jcards[r["oracle_id"]] = {"name": r["name"], "n": len(pages), "kinds": {k: kc[k] for k, _ in GROUPS if kc[k]},
                                      "index": f"references/{L_}.md#{a2}"}
        files[p] = "\n".join(out).rstrip("\n") + "\n"
    tot = Counter()
    for v in jcards.values():
        for k, n in v["kinds"].items():
            tot[k] += n
    readme = ["# Reverse card index", "",
              "> Generated by `scripts/build_crossrefs.py` (Bot cycle 18, [#66](https://github.com/corymstover/GrokBotMTGCompanion/issues/66)). "
              "Answers *where is this card discussed?* — the reverse of the card links on every page. Card shards stay lean: each cited card entry gains one *Referenced in* line pointing here. "
              "`data/card_refs.json` has the same counts for scripts (`python3 scripts/kb_find.py \"Sol Ring\"` prints them).", "",
              f"**{len(jcards):,} cards** are cited by at least one page (of {len(rows):,} entries); "
              f"{sum(v['n'] for v in jcards.values()):,} card–page links: " + " · ".join(f"{dict(GROUPS)[k].lower()} {tot[k]:,}" for k, _ in GROUPS if tot[k]) + ". "
              "Not counted: [Card Index](../Card%20Index.md) (it lists every card).", "",
              "| Shard letter | Cards referenced |", "|---|---|"]
    readme += [f"| [{L_}]({esc_url(L_)}.md) | {len(by_letter[L_]):,} |" for L_ in letters]
    top = sorted(jcards.values(), key=lambda v: (-v["n"], v["name"]))[:25]
    readme += ["", "## Most-referenced cards", "", "| Card | Pages | Decks |", "|---|---|---|"]
    readme += [f"| [{v['name']}]({v['index'][len('references/'):]}) | {v['n']} | {v['kinds'].get('deck', 0)} |" for v in top]
    files[REFS_DIR / "README.md"] = "\n".join(readme) + "\n"
    files[REFS_JSON] = json.dumps({"generated_by": "scripts/build_crossrefs.py", "bulk": bulk_date[:10], "cards_referenced": len(jcards),
                                   "cards": dict(sorted(jcards.items()))}, ensure_ascii=False, indent=0) + "\n"
    return files, jcards


_ENR = None


def enrichment():
    """data/card_enrichment.json cards (Bot cycle 33, #102): the reverse index lists each enriched card's lore entries."""
    global _ENR
    if _ENR is None:
        p = ROOT / "data" / "card_enrichment.json"
        _ENR = json.loads(p.read_text(encoding="utf-8"))["cards"] if p.exists() else {}
    return _ENR


# ------------------------------------------------------------------ 4. shard lines
def ref_line(info, shard_rel):
    return ing.ref_line_text(info)  # same text ingest_scryfall.py renders, so a re-ingest keeps the shards current


def patch_shards(jcards, write):
    rows, _, _ = index_rows()
    want = {}
    for r in rows:
        info = jcards.get(r["oracle_id"])
        if info:
            want[(r["shard"], r["anchor"])] = ref_line(info, r["shard"])
    stale = 0
    for p in sorted((ROOT / "cards").rglob("*.md")):
        if p.name == "README.md":
            continue
        rel = str(p.relative_to(ROOT))
        text = p.read_text(encoding="utf-8")
        head, sep, body = text.partition("\n## Entries\n")
        seen = Counter()
        chunks = re.split(r"\n(?=### )", body)
        out = []
        for ch in chunks:
            if ch.startswith("### "):
                a = ing.gh_anchor(ch.split("\n", 1)[0][4:])
                a2 = f"{a}-{seen[a]}" if seen[a] else a
                seen[a] += 1
                lines = [l for l in ch.split("\n") if not l.startswith(REF_LINE)]
                line = want.get((rel, a2))
                if line:
                    i = next((k for k, l in enumerate(lines) if l.startswith("- **Source flags:**")), len(lines))
                    lines.insert(i, line)
                ch = "\n".join(lines)
            out.append(ch)
        new = head + sep + "\n".join(out)
        if new != text:
            stale += 1
            if write:
                p.write_text(new, encoding="utf-8")
    return stale


def main(argv):
    check = "--check" in argv
    files, jcards = build()
    stale = []
    for p, content in files.items():
        old = p.read_text(encoding="utf-8") if p.exists() else None
        if p.parent == REFS_DIR or p in (REFS_JSON, DECKPKG_JSON):
            cur = old
            if p.suffix == ".md" and old is not None:
                cur = fm.body_of(old)
            if cur != content:
                stale.append(p)
                if not check:
                    p.write_text(content, encoding="utf-8")
        elif fm.body_of(old or "") != fm.body_of(content):
            stale.append(p)
            if not check:
                p.write_text(content, encoding="utf-8")
    if REFS_DIR.exists():
        for p in REFS_DIR.glob("*.md"):
            if p not in files:
                stale.append(p)
                if not check:
                    p.unlink()
    ns = patch_shards(jcards, write=not check)
    rel = lambda p: str(p.relative_to(ROOT))
    print(f"crossrefs: {len(jcards):,} cards referenced; {len(files)} generated files ({len(stale)} {'stale' if check else 'updated'}); "
          f"{ns} card shards {'stale' if check else 'updated'}")
    for p in stale[:15]:
        print("  " + rel(p))
    return 1 if check and (stale or ns) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
