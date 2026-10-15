#!/usr/bin/env python3
"""Generate "EDH Pairings.md" (Bot cycle 6, #32): a matrix of Partner, Partner—[text], Partner with, Choose a Background
and Doctor's companion pairs by combined color identity (CR 702.124), from Scryfall data. Every card is Commander-legal.
Usage: python3 scripts/build_pairings.py"""
import re, itertools, collections
from edh_lib import Data, NAMES, ORDER, WUBRG
import ingest_scryfall as ing


def lines(d, c):
    t = c.get("oracle_text") or (c.get("card_faces") or [{}])[0].get("oracle_text", "")
    return [re.sub(r"\s*\(.*", "", l).strip() for l in t.split("\n")]


def union(*cs):
    s = set().union(*[set(c.get("color_identity", [])) for c in cs])
    return "".join(x for x in WUBRG if x in s) or "C"


def main():
    d = Data()
    G = collections.defaultdict(list)  # mechanic -> cards
    pw = []
    for c in d.pool:
        t = d.ftype(c)
        if "Legendary" not in t: continue
        ls = lines(d, c)
        if "Partner" in ls: G["Partner"].append(c)
        for l in ls:
            m = re.match(r"Partner—(.+)$", l)
            if m: G["Partner—" + m.group(1)].append(c)
            m = re.match(r"Partner with (.+)$", l)
            if m: pw.append((c, m.group(1)))
            if l == "Choose a Background": G["bg_cmd"].append(c)
            if l == "Doctor's companion": G["companion"].append(c)
        if re.search(r"Enchantment — Background", t): G["Background"].append(c)
        if "Creature" in t and re.search(r"— Time Lord Doctor$", t): G["Doctor"].append(c)
    rank = lambda *cs: sum((c.get("edhrec_rank") or 10**6) for c in cs)
    pairs = collections.defaultdict(list)  # mech -> (a,b)
    for k in [k for k in G if k == "Partner" or k.startswith("Partner—")]:
        pairs[k] = list(itertools.combinations(G[k], 2))
    seen = set()
    for c, nm in pw:
        o = d.by_name.get(nm)
        if o and any(x[0] is o and x[1] == c["name"] for x in pw):
            key = tuple(sorted([c["name"], o["name"]]))
            if key not in seen: seen.add(key); pairs["Partner with"].append((c, o))
    pairs["Choose a Background"] = [(a, b) for a in G["bg_cmd"] for b in G["Background"]]
    pairs["Doctor's companion"] = [(a, b) for a in G["companion"] for b in G["Doctor"]]
    mechs = ["Partner"] + sorted(k for k in pairs if k.startswith("Partner—")) + ["Partner with", "Choose a Background", "Doctor's companion"]
    L = d.header("EDH Pairings — Partner, Background, Friends forever & Doctor's companion", "scripts/build_pairings.py", 32,
                 "Pairs are every legal combination of two cards with the same partner ability. The *most-played pair* is the one with the lowest summed EDHREC rank (popularity, not power).")
    L += ["## Rules (fact)", "",
          "- Each partner ability lets you have **two commanders**. The deck is still 100 cards, including both commanders (CR 702.124a–b).",
          "- Your **color identity** is the combined identity of both commanders (CR 702.124c; [Color identity](Rules%20Interactions.md#commander-color-identity)).",
          "- Each commander has its own **commander tax** and its own **21 commander-damage** count (CR 702.124d; [Commander damage](Rules%20Interactions.md#commander-damage)).",
          "- **Different partner abilities can't be combined.** *Partner* doesn't pair with *Partner with*, and Backgrounds only pair with *Choose a Background* (CR 702.124f, 702.124k).",
          "- *Partner—[text]* pairs only with the **same** text. CR 702.124i lists Character select, Father & son, Friends forever and Survivors.",
          "- *Doctor's companion* pairs with a legendary **Time Lord Doctor** creature that has no other creature types (CR 702.124m).",
          "- More detail and rulings: [Rules Interactions → Partner & Backgrounds](Rules%20Interactions.md#partner--backgrounds).", "",
          "## Card counts", "", "| Ability | Cards | Legal pairs |", "|---|---|---|"]
    cnt = {"Partner": len(G["Partner"]), "Partner with": len(pairs["Partner with"]) * 2,
           "Choose a Background": f"{len(G['bg_cmd'])} commanders + {len(G['Background'])} Backgrounds",
           "Doctor's companion": f"{len(G['companion'])} companions + {len(G['Doctor'])} Doctors"}
    for m in mechs:
        L.append(f"| {m} | {cnt.get(m, len(G.get(m, [])))} | {len(pairs[m]):,} |")
    L += ["", "## Identity matrix", "", "Each cell is the number of legal pairs whose **combined** identity is exactly that identity. — means no pair produces it.", "",
          "| Identity | " + " | ".join(mechs) + " |", "|---|" + "---|" * len(mechs)]
    by = {m: collections.defaultdict(list) for m in mechs}
    for m in mechs:
        for a, b in pairs[m]:
            by[m][union(a, b)].append((a, b))
    for idt in ORDER:
        L.append(f"| {NAMES[idt]} ({idt}) | " + " | ".join(f"{len(by[m][idt]):,}" if by[m][idt] else "—" for m in mechs) + " |")
    L.append("")
    for m in mechs:
        L += [f"## {m}", ""]
        if m == "Partner with":
            L += ["Fixed pairs. Each card's ETB lets a target player tutor its partner (CR 702.124j).", "",
                  "| Pair | Identity | GC |", "|---|---|---|"]
            for a, b in sorted(pairs[m], key=lambda p: rank(*p)):
                L.append(f"| {d.link(a)} + {d.link(b)} | {union(a, b)} | {' '.join(x for x in (d.gc(a), d.gc(b)) if x)} |")
        else:
            L += ["Most-played pair for each combined identity:", "", "| Identity | Pairs | Most-played pair | GC |", "|---|---|---|---|"]
            for idt in ORDER:
                ps = by[m][idt]
                if not ps: continue
                a, b = min(ps, key=lambda p: rank(*p))
                L.append(f"| {NAMES[idt]} ({idt}) | {len(ps):,} | {d.link(a)} + {d.link(b)} | {' '.join(x for x in (d.gc(a), d.gc(b)) if x)} |")
            if m.startswith("Partner—") or m == "Doctor's companion" or m == "Choose a Background":
                pool = (G[m] if m.startswith("Partner—") else (G["bg_cmd"] + G["Background"] if m == "Choose a Background" else G["companion"] + G["Doctor"]))
                L += ["", f"<details><summary>All {len(pool)} cards</summary>", "", ", ".join(f"{d.link(c)} ({d.ci(c)})" for c in pool), "", "</details>"]
        L.append("")
    L += ["## Guidance (opinion)", "",
          "*Strategy opinion, not rules or fact.*",
          "- Pairs give you flexible colors and two cards that are always available, but each one dies to removal separately and has its own tax.",
          "- Backgrounds are usually cheap enchantments that are hard to remove. Pick the creature commander first, then the Background that supports its plan.",
          "- With a two-commander deck, decide early which commander is the engine and which is the support or win condition. Track commander damage for each one separately.", ""]
    (ing.ROOT / "EDH Pairings.md").write_text("\n".join(L) + "\n")
    print({m: len(pairs[m]) for m in mechs}, {k: len(v) for k, v in G.items()})


if __name__ == "__main__":
    main()
