#!/usr/bin/env python3
"""Generate "EDH Upgrade Paths.md" (Bot cycle 7, #30): budget-to-optimized upgrade paths for the 32 deck commanders.
Compares EDHREC's public *budget* and *expensive* deck pages (json.edhrec.com) per commander. Upgrades are cards much more
common in expensive decks; cuts are cards much more common in budget decks. Every card is checked against Scryfall:
Commander-legal and within the commander's color identity. Prices are Scryfall's cheapest paper printing (snapshot).
Usage: python3 scripts/build_upgrade_paths.py [--refresh]"""
import atomic_io  # noqa: F401  atomic Path.write_text/write_bytes (Bot cycle 34)
import json, re, sys, time, urllib.request
from edh_lib import Data
import ingest_scryfall as ing

CACHE = ing.DEFAULT_CACHE / "edhrec"
OUT_JSON = ing.ROOT / "data" / "upgrade_paths.json"
TIERS = [("Step 1 — cheap upgrades (≤ $5)", 0, 5), ("Step 2 — mid upgrades ($5–$20)", 5, 20), ("Step 3 — optimized (> $20)", 20, 10**9)]
DELTA = 0.10


def edhrec_slug(name):
    n = re.sub(r"[^a-z0-9 -]", "", name.split(" // ")[0].lower())
    return re.sub(r" +", "-", n.strip())


def fetch(path, refresh):
    CACHE.mkdir(parents=True, exist_ok=True)
    f = CACHE / (path.replace("/", "__") + ".json")
    if f.exists() and not refresh:
        return json.loads(f.read_text())
    req = urllib.request.Request(f"https://json.edhrec.com/pages/{path}.json", headers={"User-Agent": "GrokBotMTGCompanion/1.0"})
    d = json.loads(urllib.request.urlopen(req, timeout=60).read()); time.sleep(1)
    f.write_text(json.dumps(d))
    return d


def incl(d):
    out = {}
    for lst in d["container"]["json_dict"]["cardlists"]:
        for cv in lst["cardviews"]:
            if cv.get("potential_decks"):
                out[cv["name"]] = max(out.get(cv["name"], 0), cv["num_decks"] / cv["potential_decks"])
    return out


def commanders():
    out = []
    for p in sorted((ing.ROOT / "decks").glob("*.md")):
        m = re.search(r"^1x (.+?) \[Commander", p.read_text(), re.M)
        if m: out.append((m.group(1), p.name))
    return out


def main():
    d = Data(); refresh = "--refresh" in sys.argv
    price = lambda c: d.price.get(c["oracle_id"])
    L = d.header("EDH Upgrade Paths", "scripts/build_upgrade_paths.py", 30,
                 "Upgrade data comes from EDHREC's public **budget** and **expensive** deck pages for each commander (community decklists; linked per section). *Budget incl.* and *Optimized incl.* are the share of eligible budget or expensive decks that run the card.")
    L[2] = L[2].replace("Bot cycle 6", "Bot cycle 7")
    cmds = commanders()
    L += ["## How to read this", "",
          f"- **Upgrades** are cards whose inclusion in expensive decks exceeds budget decks by at least {DELTA:.0%}. They're grouped by price into three steps, so you can upgrade gradually.",
          "- *Budget incl.* is often 0% for pricier cards: EDHREC's budget pages are built from cheaper decklists, so expensive cards rarely appear in them.",
          f"- **Likely cuts** are cards much more common in budget decks. They're the usual slots to swap out.",
          "- **Bracket check:** Game Changers (**GC**) push a deck to Bracket 3, or to 4 with more than three of them ([Brackets](EDH%20Standards.md#power-bracket-assessment)). Count them before you upgrade.",
          "- *Guidance (opinion):* upgrade the mana base and card advantage first, then interaction, then win conditions. A higher price doesn't always mean a stronger deck at your table.", "",
          "## Contents"] + [f"- [{n}](#{re.sub(r'[^a-z0-9 -]', '', n.lower()).replace(' ', '-')})" for n, _ in cmds] + [""]
    summary, nrows, gcs_total = {}, 0, 0
    for name, deckfile in cmds:
        cmd = d.by_name.get(name)
        if not cmd: print("skip", name); continue
        cid = set(cmd.get("color_identity", []))
        s = edhrec_slug(name)
        b, e = incl(fetch(f"commanders/{s}/budget", refresh)), incl(fetch(f"commanders/{s}/expensive", refresh))
        bc = fetch(f"commanders/{s}", refresh).get("budget_counts") or {}
        ok = lambda n: n in d.by_name and set(d.by_name[n].get("color_identity", [])) <= cid and d.by_name[n]["oracle_id"] != cmd["oracle_id"] \
            and "Basic" not in d.ftype(d.by_name[n])
        names = [n for n in set(b) | set(e) if ok(n)]
        ups = sorted((n for n in names if e.get(n, 0) - b.get(n, 0) >= DELTA), key=lambda n: -(e.get(n, 0) - b.get(n, 0)))
        cuts = sorted((n for n in names if b.get(n, 0) - e.get(n, 0) >= DELTA), key=lambda n: -(b.get(n, 0) - e.get(n, 0)))
        L += [f"## {name}", "",
              f"{d.link(cmd)} · identity **{d.ci(cmd)}** · deck skeleton: [decks/{deckfile}](decks/{deckfile}) · EDHREC [budget](https://edhrec.com/commanders/{s}/budget) / [expensive](https://edhrec.com/commanders/{s}/expensive) pages"
              + (f" · deck counts reported by EDHREC: budget {bc.get('budget', 0):,} · middle {bc.get('middle', 0):,} · expensive {bc.get('expensive', 0):,}" if bc else ""), ""]
        rec = {"upgrades": {}, "cuts": cuts[:8]}
        for lab, lo, hi in TIERS:
            tier = [n for n in ups if price(d.by_name[n]) is not None and lo < price(d.by_name[n]) <= hi or (lo == 0 and price(d.by_name[n]) == 0)][:6]
            rec["upgrades"][lab] = tier
            if not tier: continue
            L += [f"**{lab}**", "", "| Card | Cheapest USD | Budget incl. | Optimized incl. | Δ | GC |", "|---|---|---|---|---|---|"]
            for n in tier:
                c = d.by_name[n]; nrows += 1; gcs_total += bool(c.get("game_changer"))
                L.append(f"| {d.link(c)} | {d.usd(c)} | {b.get(n, 0):.0%} | {e.get(n, 0):.0%} | +{e.get(n, 0) - b.get(n, 0):.0%} | {d.gc(c)} |")
            L.append("")
        if cuts:
            L += ["**Likely cuts** (common in budget decks, rarer in expensive ones): " + ", ".join(f"{d.link(d.by_name[n])} ({b.get(n, 0):.0%} → {e.get(n, 0):.0%})" for n in cuts[:8]), ""]
        gup = [n for t in rec["upgrades"].values() for n in t if d.by_name[n].get("game_changer")]
        L += [f"**Bracket note:** {len(gup)} of the listed upgrades are Game Changers" + (f" ({', '.join(gup)})" if gup else "") + ". " +
              ("Adding all of them puts the deck at Bracket 4 or higher." if len(gup) > 3 else "Adding them keeps the deck within Bracket 3, provided it has no other Game Changers and no early two-card infinites." if gup else "The upgrades on their own don't change the bracket."), ""]
        summary[name] = rec
    OUT_JSON.write_text(json.dumps({"source": "json.edhrec.com budget/expensive commander pages", "delta": DELTA, "commanders": summary}, indent=1) + "\n")
    (ing.ROOT / "EDH Upgrade Paths.md").write_text("\n".join(L) + "\n")
    print("commanders", len(summary), "upgrade rows", nrows, "gc rows", gcs_total, "cuts", sum(len(v["cuts"]) for v in summary.values()))


if __name__ == "__main__":
    main()
