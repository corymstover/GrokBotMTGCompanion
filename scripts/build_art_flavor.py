#!/usr/bin/env python3
"""Build "Art & Flavor Story Links.md" (issue #37, Bot cycle 8).

Ties story-significant cards to official story pages using two data sources:
  1. Scryfall default-cards `story_spotlight` printings (Wizards' Story Spotlight cards), plus
     their artist and flavor text, verbatim from the cached bulk file.
  2. Art captions ("<Card> | Art by <Artist>") on official magic.wizards.com story pages,
     harvested from the off-repo lore corpus into data/story_art_captions.csv.
A caption link is recorded only when the caption artist matches a Scryfall printing of that card.
Usage:
  python3 scripts/build_art_flavor.py --harvest /workspace/lore_src   (refresh the captions CSV)
  python3 scripts/build_art_flavor.py                                  (write the Markdown)
Card names are written as [[Name]] and resolved by scripts/resolve_card_links.py.
"""
import csv
import glob
import gzip
import json
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import ingest_scryfall as ing  # noqa: E402

CAP_CSV = ROOT / "data" / "story_art_captions.csv"
OUT = ROOT / "Art & Flavor Story Links.md"
ARCS = "Story Arc Summaries.md"
# set code -> Story Arc Summaries heading (None = covered in Conflicts & Arcs)
SET_ARC = {
    "kld": "Kaladesh & Aether Revolt (2016–17)", "aer": "Kaladesh & Aether Revolt (2016–17)",
    "akh": "Amonkhet & Hour of Devastation (2017)", "hou": "Amonkhet & Hour of Devastation (2017)",
    "dom": "Return to Dominaria (2018)", "war": "War of the Spark (2019)",
    "dmu": "The Phyrexian Invasion saga (2023)", "bro": "The Phyrexian Invasion saga (2023)",
    "one": "The Phyrexian Invasion saga (2023)", "mom": "The Phyrexian Invasion saga (2023)",
    "woe": "Wilds of Eldraine (2023)", "lci": "The Lost Caverns of Ixalan (2023)",
    "mkm": "Murders at Karlov Manor (2024)", "otj": "Outlaws of Thunder Junction (2024)",
    "blb": "Bloomburrow (2024)", "dsk": "Duskmourn: House of Horror (2024)",
    "dft": "Aetherdrift (2025)", "tdm": "Tarkir: Dragonstorm (2025)",
    "eoe": "Edge of Eternities (2025)", "ecl": "Lorwyn Eclipsed (2025–26)",
    "sos": "Secrets of Strixhaven (2026)", "fra": "Reality Fracture (2026)",
}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def harvest(corpus: str) -> None:
    rows = set()
    for f in sorted(glob.glob(f"{corpus}/*/*.txt")):
        L = [x.strip() for x in open(f, encoding="utf-8", errors="ignore").read().split("\n")]
        url = L[0][5:].strip() if L and L[0].startswith("URL: ") else ""
        title = L[1][7:].strip() if len(L) > 1 and L[1].startswith("TITLE: ") else ""
        url = re.sub(r"^https://web\.archive\.org/web/\w+/", "", url)
        if "magic.wizards.com" not in url:
            continue
        for i, ln in enumerate(L):
            if re.fullmatch(r"\| Art by:?", ln) and 0 < i < len(L) - 1 and L[i - 1] and L[i + 1]:
                rows.add((L[i - 1], L[i + 1], url, title))
    CAP_CSV.parent.mkdir(exist_ok=True)
    with CAP_CSV.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["caption_name", "caption_artist", "url", "title"])
        w.writerows(sorted(rows))
    print(f"{CAP_CSV.relative_to(ROOT)}: {len(rows)} captions")


def flavor_of(c: dict) -> str:
    if c.get("flavor_text"):
        return c["flavor_text"]
    return " / ".join(f["flavor_text"] for f in c.get("card_faces", []) if f.get("flavor_text"))


def esc(s: str) -> str:
    s = re.sub(r" \| MAGIC: THE GATHERING$", "", s, flags=re.I)
    return s.replace("|", "\\|").replace("\n", " ").replace("[[", "[ [")


def build() -> int:
    index = {r["name"]: r for r in csv.DictReader((ROOT / "data" / "card_index.csv").open(encoding="utf-8"))}
    front = {n.split(" // ")[0]: n for n in index}
    lookup = {norm(k): v for k, v in front.items()} | {norm(k): k for k in index}
    caps = list(csv.DictReader(CAP_CSV.open(encoding="utf-8")))
    arc_text = (ROOT / ARCS).read_text(encoding="utf-8")
    cited = set(re.findall(r"https://magic\.wizards\.com/[^)\s]+", arc_text))
    gz = sorted((ROOT / ".cache").glob("default-cards-*.jsonl.gz"))[-1]
    prints = defaultdict(list)
    for ln in gzip.open(gz, "rt", encoding="utf-8"):
        c = json.loads(ln)
        if c.get("lang") == "en" and c["name"] in index:
            prints[c["name"]].append(c)
    # caption -> (card, page) when the artist matches a printing
    cap_by_card = defaultdict(list)
    for r in caps:
        name = lookup.get(norm(r["caption_name"]))
        if not name:
            continue
        arts = {norm(a) for p in prints[name] for a in re.split(r" & ", p.get("artist") or "")}
        if norm(r["caption_artist"]) in arts or norm(r["caption_artist"]) in {norm(p.get("artist") or "") for p in prints[name]}:
            cap_by_card[name].append(r)
    for v in cap_by_card.values():
        v.sort(key=lambda r: (r["url"] not in cited, "/magic-story/" not in r["url"], r["url"]))
    spot = {}
    for name, ps in prints.items():
        for p in ps:
            if p.get("story_spotlight") and p["set"] in SET_ARC:
                spot.setdefault(name, p)
    by_arc = defaultdict(list)
    for name, p in spot.items():
        by_arc[SET_ARC[p["set"]]].append((p["released_at"], p["collector_number"].zfill(4), name, p))
    order = list(dict.fromkeys(SET_ARC.values()))
    out = []
    linked = 0
    for arc in order:
        rows = sorted(by_arc.get(arc, []))
        if not rows:
            continue
        out.append(f"\n### {arc}\n")
        out.append(f"Arc summary: [{arc}]({ARCS.replace(' ', '%20')}#{ing.gh_anchor(arc)})\n")
        out.append("| Card | Set · artist | Flavor text (Scryfall, verbatim) | Story page showing this art |")
        out.append("|---|---|---|---|")
        for _, _, name, p in rows:
            cr = cap_by_card.get(name)
            if cr:
                linked += 1
                story = f"[{esc(cr[0]['title'] or cr[0]['url'])}]({cr[0]['url']})"
            else:
                story = "❓ no art caption found in the corpus"
            fl = esc(flavor_of(p)) or "—"
            out.append(f"| [[{name}]] | {p['set'].upper()} #{p['collector_number']} · {esc(p.get('artist') or '?')} | {fl} | {story} |")
    # captioned cards on arc-cited pages that are not spotlights (pre-KLD arcs especially)
    extra = defaultdict(list)
    for name, rs in cap_by_card.items():
        if name in spot:
            continue
        for r in rs:
            if r["url"] in cited and index[name]["type_line"].split(" — ")[0].find("Basic") < 0 and "Token" not in index[name]["type_line"]:
                extra[r["url"]].append((name, r))
                break
    total_spot = len(spot)
    head = [
        "# Art & Flavor Story Links",
        "",
        "> **Bot cycle 8 · issue [#37](https://github.com/corymstover/GrokBotMTGCompanion/issues/37).** Links story-significant cards to the official story moment they depict. Generated by `scripts/build_art_flavor.py`.",
        "> **Sources:** card art credits and flavor text are verbatim from Scryfall bulk data. A card counts as \"story-significant\" if (a) Scryfall marks its printing as a Wizards **Story Spotlight** card, or (b) its art is captioned (\"Card | Art by …\") on an official magic.wizards.com story page cited in [Story Arc Summaries](Story%20Arc%20Summaries.md). A story page is linked only when its caption artist matches a Scryfall printing of that card.",
        "> **Not a deck list:** cards appear here for lore, not as recommendations. Check legality and color identity in each card's entry. Related: [Side-Media Index](Side-Media%20Index.md) · [Planeswalker Dossiers](Planeswalker%20Dossiers.md).",
        "",
        f"**Coverage:** {total_spot} Story Spotlight cards across {sum(1 for a in order if by_arc.get(a))} arcs, {linked} of them linked to the story page that shows their art · {sum(len(v) for v in extra.values())} more captioned cards on {len(extra)} cited story pages.",
        "",
        "## Contents",
        "- [Story Spotlight cards by arc](#story-spotlight-cards-by-arc)",
        *[f"  - [{a}](#{ing.gh_anchor(a)})" for a in order if by_arc.get(a)],
        "- [Captioned art on cited story pages](#captioned-art-on-cited-story-pages)",
        "",
        "## Story Spotlight cards by arc",
        "Story Spotlight printings in each arc's main set, in collector-number order. A ❓ in the last column means the corpus has no art caption for that card. It does not mean the card has no story link.",
    ]
    tail = ["", "## Captioned art on cited story pages",
            "Non-spotlight cards whose art appears, with a matching artist credit, on a story page cited in Story Arc Summaries. This covers the pre-Kaladesh arcs (BFZ, SOI) that predate Story Spotlights.", "",
            "| Story page | Cards shown (art credit matches Scryfall) |", "|---|---|"]
    titles = {r["url"]: r["title"] for r in caps}
    for url in sorted(extra, key=lambda u: titles.get(u, u)):
        names = ", ".join(f"[[{n}]]" for n, _ in sorted(extra[url]))
        tail.append(f"| [{esc(titles.get(url) or url)}]({url}) | {names} |")
    OUT.write_text("\n".join(head + out + tail) + "\n", encoding="utf-8")
    print(f"{OUT.name}: {total_spot} spotlight cards, {linked} caption-linked, {sum(len(v) for v in extra.values())} extra")
    return 0


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "--harvest":
        harvest(sys.argv[2])
    else:
        sys.exit(build())
