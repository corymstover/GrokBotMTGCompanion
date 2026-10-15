#!/usr/bin/env python3
"""Build "Keyword Encyclopedia.md" (issue #39, Bot cycle 8).

For every keyword ability (CR 702.x) and keyword action (CR 701.x) in the cached
Comprehensive Rules, the entry gives:
  - its CR number and the definition quoted verbatim (subrule "a", or the section's first rule),
  - how many Oracle cards carry it (Scryfall `keywords` field) and how many are Commander-legal,
  - the earliest printing in Scryfall default-cards,
  - whether it appears on Wizards' official "Common Keywords" glossary (magic.wizards.com/en/keyword-glossary),
  - up to 3 Commander-legal example cards (best EDHREC rank, cards with rulings preferred). Each links
    to its card entry, which carries the card's rulings.
Usage: python3 scripts/build_keywords.py && python3 scripts/resolve_card_links.py "Keyword Encyclopedia.md"
"""
import csv
import gzip
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import ingest_scryfall as ing  # noqa: E402

OUT = ROOT / "Keyword Encyclopedia.md"
GLOSSARY_URL = "https://magic.wizards.com/en/keyword-glossary"
# Keywords and actions on the official Common Keywords glossary page (fetched 2026-10-15)
GLOSSARY = {"deathtouch", "defender", "double strike", "enchant", "first strike", "flash", "flashback",
            "flying", "haste", "hexproof", "indestructible", "lifelink", "menace", "reach", "trample",
            "vigilance", "goad", "scry", "shuffle", "equip"}


def parse_cr(path: Path):
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    start = max(i for i, l in enumerate(lines) if l.startswith("701.1. "))
    end = max(i for i, l in enumerate(lines) if l.strip() == "Glossary")
    secs = []
    cur = None
    for l in lines[start:end]:
        m = re.match(r"^(70[12])\.(\d+)\. (.+)$", l)
        if m:
            cur = {"sec": m.group(1), "n": int(m.group(2)), "name": m.group(3).strip(), "rules": []}
            secs.append(cur)
            continue
        m = re.match(r"^(70[12])\.(\d+)([a-z]+) (.+)$", l)
        if m and cur and int(m.group(2)) == cur["n"]:
            cur["rules"].append((m.group(3), m.group(4).strip()))
    return [s for s in secs if s["n"] > 1]


def main() -> int:
    cr = sorted((ROOT / ".cache").glob("MagicCompRules-*.txt"))[-1]
    crdate = re.search(r"(\d{8})", cr.name).group(1)
    crdate = f"{crdate[:4]}-{crdate[4:6]}-{crdate[6:]}"
    secs = parse_cr(cr)
    index = {r["oracle_id"]: r for r in csv.DictReader((ROOT / "data" / "card_index.csv").open(encoding="utf-8"))}
    cards, _ = ing.get_bulk(ing.DEFAULT_CACHE, None)
    kw_cards = defaultdict(list)
    for c in cards:
        if c.get("oracle_id") not in index:
            continue
        for k in c.get("keywords", []):
            kw_cards[k.lower()].append(c)
    first = {}
    gz = sorted((ROOT / ".cache").glob("default-cards-*.jsonl.gz"))[-1]
    for ln in gzip.open(gz, "rt", encoding="utf-8"):
        c = json.loads(ln)
        for k in c.get("keywords", []):
            k = k.lower()
            if k not in first or c["released_at"] < first[k][0]:
                first[k] = (c["released_at"], c["set_name"])

    def match(name):
        n = name.lower()
        keys = [k for k in kw_cards if k == n or k.startswith(n + " ")]
        if n == "landwalk":
            keys = [k for k in kw_cards if k.endswith("walk") and k != "planeswalk"]
        return keys

    def entry(s):
        keys = match(s["name"])
        cs = {c["oracle_id"]: c for k in keys for c in kw_cards[k]}
        rows = [index[o] for o in cs]
        legal = [r for r in rows if r["commander_legality"] == "legal"]
        rank = lambda r: (int(r["rulings"] or 0) == 0, int(r["edhrec_rank"]) if r["edhrec_rank"] else 10**9, r["name"])
        ex = sorted(legal, key=rank)[:3]
        fp = min((first[k] for k in keys if k in first), default=None)
        defn = next((t for sub, t in s["rules"] if sub == "a"), s["rules"][0][1] if s["rules"] else "")
        cr_id = f"{s['sec']}.{s['n']}"
        g = " · ✅ on Wizards' [Common Keywords]({}) glossary".format(GLOSSARY_URL) if s["name"].lower() in GLOSSARY else ""
        out = [f"#### {s['name']}", "",
               f"**CR {cr_id}** ({len(s['rules'])} subrules){g}", "",
               f"> {cr_id}a {defn}" if any(sub == "a" for sub, _ in s["rules"]) else f"> {defn}", ""]
        stats = f"**Cards:** {len(rows)} Oracle cards · {len(legal)} Commander-legal"
        if fp:
            stats += f" · earliest Scryfall printing of a card that has it now (includes Oracle errata): {fp[1]} ({fp[0]})"
        if not keys:
            stats = "**Cards:** no card in Scryfall's `keywords` data lists this name (it may be rules-only, reminder-only, or worded differently on cards) ❓"
        out.append(stats)
        if ex:
            out.append("")
            out.append("**Examples (Commander-legal; each entry includes its rulings):** " + ", ".join(f"[[{r['name']}]]" for r in ex))
        return out, len(rows), bool(keys)

    body = []
    counts = {"702": [0, 0], "701": [0, 0]}
    toc = []
    for sec, title in (("702", "Keyword abilities (CR 702)"), ("701", "Keyword actions (CR 701)")):
        body.append(f"\n## {title}\n")
        toc.append(f"- [{title}](#{ing.gh_anchor(title)})")
        items = sorted([s for s in secs if s["sec"] == sec], key=lambda s: s["name"].lower())
        letters = sorted({s["name"][0].upper() for s in items})
        lab = "Abilities" if sec == "702" else "Actions"
        body.append("Jump: " + " · ".join(f"[{L}](#{ing.gh_anchor(lab + ': ' + L)})" for L in letters) + "\n")
        for L in letters:
            body.append(f"### {lab}: {L}\n")
            for s in [x for x in items if x["name"][0].upper() == L]:
                e, n, ok = entry(s)
                counts[sec][0] += 1
                counts[sec][1] += ok
                body.extend(e)
                body.append("")
    head = [
        "# Keyword Encyclopedia", "",
        "> **Bot cycle 8 · issue [#39](https://github.com/corymstover/GrokBotMTGCompanion/issues/39) (Phase 3).** Every keyword ability (CR 702) and keyword action (CR 701), with the Comprehensive Rules definition quoted verbatim, card counts, the earliest printing, and Commander-legal examples. Generated by `scripts/build_keywords.py`.",
        f"> **Sources:** Comprehensive Rules dated {crdate} (cached as `.cache/{cr.name}`); Scryfall Oracle and default-cards bulk data (`keywords` field); Wizards' [Common Keywords]({GLOSSARY_URL}) page for the ✅ marks. ✅ means the term is on that beginner glossary. It is **not** an official evergreen list, and this page does not label any keyword evergreen.",
        "> Each example links to its card entry, which includes the card's official rulings. For tricky interactions see [Rules Interactions](Rules%20Interactions.md).", "",
        f"**Coverage:** {counts['702'][0]} keyword abilities ({counts['702'][1]} matched to cards) · {counts['701'][0]} keyword actions ({counts['701'][1]} matched to cards).", "",
        "## Contents", *toc, "",
    ]
    OUT.write_text("\n".join(head + body) + "\n", encoding="utf-8")
    print(f"{OUT.name}: {counts}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
