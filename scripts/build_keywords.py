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


EEH = ("Evergreen Eggs & Ham (2015)", "https://magic.wizards.com/en/news/making-magic/evergreen-eggs-ham-2015-06-08")
WARD = ("Introducing Ward (2021)", "https://magic.wizards.com/en/news/card-preview/introducing-ward-2021-03-25")
DEC = ("Deciduous (2022)", "https://magic.wizards.com/en/news/making-magic/deciduous-2022-03-28")
M21 = ("Core Set 2021 Release Notes (2020)", "https://magic.wizards.com/en/news/feature/core-set-2021-and-jumpstart-release-notes-2020-06-20")
# Status labels used ONLY where an official Wizards article says so. Anything else stays unlabeled.
EVERGREEN_2015 = ["deathtouch", "defender", "double strike", "enchant", "equip", "first strike", "flash", "flying",
                  "haste", "hexproof", "indestructible", "lifelink", "menace", "reach", "trample", "vigilance",
                  "activate", "attach", "cast", "counter", "destroy", "discard", "exchange", "exile", "fight",
                  "play", "regenerate", "reveal", "sacrifice", "scry", "search", "shuffle", "tap and untap"]
STATUS = {k: ("🌲 Evergreen", "on the Magic Origins (2015) evergreen list", [EEH]) for k in EVERGREEN_2015}
STATUS.update({
    "ward": ("🌲 Evergreen", "\"a new evergreen keyword\" as of Strixhaven (2021)", [WARD]),
    "prowess": ("🍂 Deciduous", "evergreen in 2015, later \"changed to be deciduous\"", [EEH, DEC]),
    "protection": ("🍂 Deciduous ⚠️", "moved \"from what we call evergreen to deciduous\" in 2015. The 2022 article says it was \"sort of returned to evergreen status\" and is \"slightly more evergreen than deciduous\"", [EEH, DEC]),
    "cycling": ("🍂 Deciduous", "\"As of Streets of New Capenna, we've added it to deciduous status\"", [DEC]),
    "investigate": ("🍂 Deciduous", "listed under \"Clue Tokens and Investigate\"", [DEC]),
    "banding": ("🍁 Retired from evergreen", "removed in Sixth Edition", [EEH]),
    "fear": ("🍁 Retired from evergreen", "removed in Magic 2010", [EEH]),
    "shroud": ("🍁 Retired from evergreen", "replaced by hexproof (M12): \"we no longer use the keyword on new cards\"", [EEH]),
    "intimidate": ("🍁 Retired from evergreen", "removed in Magic Origins", [EEH]),
    "landwalk": ("🍁 Retired from evergreen", "removed in Magic Origins", [EEH]),
    "mill": ("Keyword action since M21", "\"promoted to an official game term\" in Core Set 2021. Not called evergreen by the source ❓", [M21]),
})


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
    rul = defaultdict(list)
    for r, _ in [ing.get_bulk(ing.DEFAULT_CACHE, None, "rulings")]:
        for x in r:
            if x.get("source") == "wotc":
                rul[x["oracle_id"]].append(x)
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
        st = STATUS.get(s["name"].lower())
        stline = (f"**Status:** {st[0]}: {st[1]} ({' · '.join(f'[{a}]({u})' for a, u in st[2])})" if st
                  else "**Status:** not labeled (no official evergreen/deciduous statement found)")
        out = [f"#### {s['name']}", "",
               f"**CR {cr_id}** ({len(s['rules'])} subrules){g}", "", stline, "",
               f"> {cr_id}a {defn}" if any(sub == "a" for sub, _ in s["rules"]) else f"> {defn}", ""]
        stats = f"**Cards:** {len(rows)} Oracle cards · {len(legal)} Commander-legal"
        if fp:
            stats += f" · earliest Scryfall printing of a card that has it now (includes Oracle errata): {fp[1]} ({fp[0]})"
        if not keys:
            stats = "**Cards:** no card in Scryfall's `keywords` data lists this name (it may be rules-only, reminder-only, or worded differently on cards) ❓"
        out.append(stats)
        terms = [t for t in re.split(r" and ", s["name"].lower().split(" [")[0]) if t]
        word = re.compile(r"\b(" + "|".join(map(re.escape, terms)) + r")\b", re.I)
        freq = defaultdict(list)
        for o in cs:
            for x in rul.get(o, []):
                bare = x["comment"]
                for part in index[o]["name"].split(" // "):
                    bare = bare.replace(part, "")
                if word.search(bare):
                    key = re.sub(r"\s+", " ", x["comment"].replace("’", "'").replace("“", '"').replace("”", '"')).strip()
                    freq[key].append((x["published_at"], index[o]["name"]))
        top = sorted(freq.items(), key=lambda kv: (-len(kv[1]), kv[0]))[:2]
        if top and len(top[0][1]) == 1:
            top = top[:1]
        if top:
            out.append("")
            out.append("**Ruling excerpts** (official Wizards rulings, verbatim; the most widely shared among this keyword's cards):")
            for text, uses in top:
                d, nm = max(uses)
                text = text.replace("\n", " ").replace("<", "&lt;").replace("[[", "[ [")
                out.append(f"- \"{text}\" ({len(uses)} card{'s' if len(uses) > 1 else ''}, e.g. [[{nm}]], {d})")
            counts_r[0] += 1
        if ex:
            out.append("")
            out.append("**Examples (Commander-legal; each entry includes its rulings):** " + ", ".join(f"[[{r['name']}]]" for r in ex))
        return out, len(rows), bool(keys)

    counts_r = [0]
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
        "> **Bot cycle 8 · issue [#39](https://github.com/corymstover/GrokBotMTGCompanion/issues/39) (Phase 3; Bot cycle 9 added status labels and ruling excerpts).** Every keyword ability (CR 702) and keyword action (CR 701), with the Comprehensive Rules definition quoted verbatim, card counts, the earliest printing, and Commander-legal examples. Generated by `scripts/build_keywords.py`.",
        f"> **Sources:** Comprehensive Rules dated {crdate} (cached as `.cache/{cr.name}`); Scryfall Oracle and default-cards bulk data (`keywords` field and WotC rulings); Wizards' [Common Keywords]({GLOSSARY_URL}) page for the ✅ marks; [{EEH[0]}]({EEH[1]}), [{WARD[0]}]({WARD[1]}), [{DEC[0]}]({DEC[1]}), and [{M21[0]}]({M21[1]}) for status labels only where those articles name a term. ✅ means the term is on the beginner glossary. Status labels are separate and appear only with a cited official article.",
        "> Each example links to its card entry, which includes the card's official rulings. For tricky interactions see [Rules Interactions](Rules%20Interactions.md).", "",
        f"**Status labels:** 🌲 evergreen · 🍂 deciduous · 🍁 retired from evergreen. A label appears only where an official Wizards article ({EEH[0]}, {WARD[0]}, {DEC[0]}) says so, with a quote. Everything else is **not labeled**: most of those are set or block mechanics, but this page does not claim that without a source. The 2015 evergreen list predates later changes, which are noted where a source exists. ❓ the current status of 2015 actions such as regenerate.",
        "",
        f"**Coverage:** {counts['702'][0]} keyword abilities ({counts['702'][1]} matched to cards) · {counts['701'][0]} keyword actions ({counts['701'][1]} matched to cards) · {sum(1 for k in STATUS)} status labels · ruling excerpts for {counts_r[0]} entries.", "",
        "## Contents", *toc, "",
    ]
    OUT.write_text("\n".join(head + body) + "\n", encoding="utf-8")
    import resolve_card_links  # Bot cycle 18 (#66): example placeholders become card-entry links on every run
    resolve_card_links.main([str(OUT)])
    print(f"{OUT.name}: {counts} rulings={counts_r[0]} status={len(STATUS)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
