#!/usr/bin/env python3
"""Build a data-derived Commander deck skeleton and validate it.

Pulls a commander's public EDHREC page data (json.edhrec.com), ranks candidate cards
by inclusion rate (decks with card / decks that could play it), and assembles a
100-card list that is then validated against Scryfall Oracle bulk data:
  * every card exists, is Commander-legal, and fits the commander's color identity (CR 903.5c)
  * singleton except basic lands (CR 903.5b), exactly 100 cards (CR 903.5a)
  * commander eligibility (CR 903.3), Game Changer count -> minimum Commander Bracket
  * flags extra-turn and mass-land-denial cards (bracket barometers)
Output: decks/<slug>.md in Archidekt import format (EDH Standards.md).

Usage: python3 scripts/build_deck_skeleton.py "Krenko, Mob Boss" [--lands 36] [--min-nonbasic 8]
Uses the cached Scryfall bulk file from scripts/ingest_scryfall.py (.cache/).
"""
import argparse
import csv
import datetime as dt
import json
import re
import sys
import time
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ingest_scryfall as ing  # noqa: E402

ROOT = ing.ROOT
DECKS = ROOT / "decks"
EDHREC = "https://json.edhrec.com/pages/commanders/{slug}.json"
MLD_PAT = re.compile(r"destroy all lands|each player sacrifices [^.]*lands|destroy all (nonbasic )?lands|lands don't untap", re.I)
BASICS = {"W": "Plains", "U": "Island", "B": "Swamp", "R": "Mountain", "G": "Forest"}


def slugify(name: str) -> str:
    s = ing.ascii_key(name.replace(" ", "-").replace(",", ""))
    s = re.sub(r"[^a-z0-9-]", "", name.lower().replace(" ", "-"))
    return re.sub(r"-+", "-", s.replace("'", "")).strip("-")


def edhrec_slug(name: str) -> str:
    n = name.split(" // ")[0].lower()
    n = re.sub(r"[^a-z0-9 -]", "", n)
    return re.sub(r"[ ]+", "-", n.strip())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("commander")
    ap.add_argument("--lands", type=int, default=36, help="total land count (default 36)")
    ap.add_argument("--max-nonbasic", type=int, default=16)
    ap.add_argument("--min-land-inclusion", type=float, default=0.25,
                    help="only add nonbasic lands played in at least this share of eligible decks")
    args = ap.parse_args()

    cards, bulk_date = ing.get_bulk(ing.DEFAULT_CACHE, None)
    uni = [c for c in cards if c.get("layout") not in ing.EXCLUDED_LAYOUTS and ing.in_universe(c)]
    by_name = {c["name"].lower(): c for c in uni}
    for c in uni:
        for f in c.get("card_faces") or []:
            by_name.setdefault(f["name"].lower(), c)
    cmd = by_name[args.commander.lower()]
    cid = set(cmd.get("color_identity", []))
    index = {}
    if ing.INDEX_CSV.exists():
        with ing.INDEX_CSV.open(encoding="utf-8") as fh:
            index = {r["name"]: r for r in csv.DictReader(fh)}

    slug = edhrec_slug(cmd["name"])
    req = urllib.request.Request(EDHREC.format(slug=slug), headers={"User-Agent": ing.HEADERS["User-Agent"]})
    data = json.loads(urllib.request.urlopen(req, timeout=60).read())
    time.sleep(1)
    num_decks = data.get("container", {}).get("json_dict", {}).get("card", {}).get("num_decks") or \
        data.get("num_decks_avg")
    cand = {}
    for lst in data["container"]["json_dict"]["cardlists"]:
        for cv in lst["cardviews"]:
            if not cv.get("potential_decks"):
                continue
            incl = cv["num_decks"] / cv["potential_decks"]
            if cv["name"] not in cand or incl > cand[cv["name"]][0]:
                cand[cv["name"]] = (incl, lst.get("header"))
    rejected = []
    nonland, nonbasic = [], []
    for name, (incl, header) in sorted(cand.items(), key=lambda kv: -kv[1][0]):
        c = by_name.get(name.lower())
        if not c:
            rejected.append((name, "not found on Scryfall")); continue
        if c["legalities"].get("commander") != "legal":
            rejected.append((name, "not Commander-legal")); continue
        if not set(c.get("color_identity", [])) <= cid:
            rejected.append((name, "outside color identity")); continue
        if c["oracle_id"] == cmd["oracle_id"]:
            continue
        front = (c.get("card_faces") or [c])[0].get("type_line") or c["type_line"]
        if "Land" in front and "//" not in c["name"] or front.startswith("Land"):
            if "Basic" not in front:
                nonbasic.append((c, incl, header))
        else:
            nonland.append((c, incl, header))
    nonbasic = [x for x in nonbasic if x[1] >= args.min_land_inclusion][:args.max_nonbasic]
    n_nonland = 99 - args.lands
    nonland = nonland[:n_nonland]
    basics_needed = args.lands - len(nonbasic)
    colors = [x for x in "WUBRG" if x in cid] or ["C"]
    basic_counts = {}
    for i in range(basics_needed):
        col = colors[i % len(colors)]
        basic_counts[BASICS.get(col, "Wastes")] = basic_counts.get(BASICS.get(col, "Wastes"), 0) + 1

    # ---- validation
    deck = [cmd] + [c for c, _, _ in nonland] + [c for c, _, _ in nonbasic]
    names = [c["name"] for c in deck]
    total = len(deck) + sum(basic_counts.values())
    problems = []
    if total != 100:
        problems.append(f"deck has {total} cards, expected 100 (CR 903.5a)")
    if len(set(names)) != len(names):
        problems.append("duplicate non-basic card (CR 903.5b)")
    for c in deck:
        if not set(c.get("color_identity", [])) <= cid:
            problems.append(f"{c['name']} outside color identity (CR 903.5c)")
        if c["legalities"].get("commander") != "legal":
            problems.append(f"{c['name']} not Commander-legal")
    elig = ing.commander_eligibility(cmd)
    if elig.startswith("No"):
        problems.append("commander is not eligible (CR 903.3)")
    gcs = [c["name"] for c in deck if c.get("game_changer")]
    xturn = [c["name"] for c in deck if "extra turn" in (c.get("oracle_text") or "").lower()]
    mld = [c["name"] for c in deck if MLD_PAT.search(c.get("oracle_text") or "")]
    if mld:
        floor = "4 (Optimized) — mass land denial present"
    elif len(gcs) > 3:
        floor = "4 (Optimized) — more than three Game Changers"
    elif gcs:
        floor = "3 (Upgraded) — 1–3 Game Changers"
    else:
        floor = "2 (Core) or 1 (Exhibition) — no Game Changers; final call depends on combos/intent"

    def entry_link(name):
        r = index.get(name)
        return f"[{name}](../{r['shard']}#{r['anchor']})" if r else name

    today = dt.date.today().isoformat()
    cats = {}
    for c, incl, header in nonland:
        front = ((c.get("card_faces") or [c])[0].get("type_line") or c["type_line"])
        t = next((k for k in ("Creature", "Planeswalker", "Battle", "Instant", "Sorcery", "Artifact", "Enchantment") if k in front), "Other")
        cats.setdefault(t, []).append((c, incl))
    archi = [f"1x {cmd['name']} [Commander{{top}}]"]
    for t, lst in cats.items():
        for c, incl in lst:
            archi.append(f"1x {c['name']} [{t}]")
    for c, incl, _ in nonbasic:
        archi.append(f"1x {c['name']} [Land]")
    for b, n in basic_counts.items():
        archi.append(f"{n}x {b} [Land]")

    L = [f"# Deck Skeleton — {cmd['name']}", "",
         f"> **Data-derived skeleton, not a tuned list.** Built {today} by `scripts/build_deck_skeleton.py` from "
         f"[EDHREC]({'https://edhrec.com/commanders/' + slug}) inclusion rates (community data) and validated against Scryfall Oracle bulk "
         f"({bulk_date[:10]}). Card choices = most-included cards for this commander; *any judgment about what to cut/add is Opinion*. "
         "Format per [EDH Standards](../EDH%20Standards.md).", "",
         "## Contents", "- [Commander](#commander)", "- [Validation](#validation)", "- [Bracket assessment](#bracket-assessment)",
         "- [Decklist (Archidekt import)](#decklist-archidekt-import)", "- [Card breakdown](#card-breakdown)", "- [Rejected candidates](#rejected-candidates)", "",
         "## Commander", "",
         f"- **{entry_link(cmd['name'])}** — {cmd.get('mana_cost') or ''} — {cmd['type_line']}",
         f"- Color identity: **{ing.ci_label(cmd.get('color_identity', []))}**",
         f"- Eligibility: {elig}",
         f"- EDHREC sample: {data.get('num_decks_avg') or num_decks or 'n/a'} decks · bracket distribution reported by EDHREC: "
         + (", ".join(f"B{k}: {v:,}" for k, v in sorted((data.get('bracket_counts') or {}).items())) or "n/a"), "",
         "## Validation", "",
         f"- Total cards: **{total}** (1 commander + {len(nonland)} nonland + {len(nonbasic)} nonbasic lands + {sum(basic_counts.values())} basics)",
         f"- Strict color identity (CR 903.5c), singleton (903.5b), Commander-legal, size (903.5a): "
         + ("✅ **all checks pass**" if not problems else "❌ " + "; ".join(problems)), "",
         "## Bracket assessment", "",
         f"- Game Changers ({len(gcs)}): " + (", ".join(gcs) or "none"),
         f"- Extra-turn cards: " + (", ".join(xturn) or "none"),
         f"- Mass land denial: " + (", ".join(mld) or "none"),
         "- Two-card infinite combos: ⚠️ not machine-checked — review manually.",
         f"- **Minimum bracket by the published barometers: {floor}.** (Brackets are a pregame-conversation tool; see [EDH Standards](../EDH%20Standards.md#power-bracket-assessment).)", "",
         "## Decklist (Archidekt import)", "", "```text", *archi, "```", "",
         "## Card breakdown", "", "| Card | Section | EDHREC inclusion | Identity |", "|---|---|---|---|"]
    for t, lst in cats.items():
        for c, incl in lst:
            L.append(f"| {entry_link(c['name'])} | {t} | {incl:.0%} | {''.join(c.get('color_identity', [])) or 'C'} |")
    for c, incl, _ in nonbasic:
        L.append(f"| {entry_link(c['name'])} | Land | {incl:.0%} | {''.join(c.get('color_identity', [])) or 'C'} |")
    for b, n in basic_counts.items():
        L.append(f"| {n}× {b} | Basic land | — | — |")
    L += ["", "## Rejected candidates", "",
          "EDHREC suggestions excluded by validation (should normally be empty or only off-identity/illegal cards):", ""]
    L += [f"- {n} — {why}" for n, why in rejected[:30]] or ["- none"]
    DECKS.mkdir(exist_ok=True)
    out = DECKS / f"{slug}.md"
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(json.dumps({"deck": str(out.relative_to(ROOT)), "total": total, "problems": problems,
                      "game_changers": len(gcs), "bracket_floor": floor, "rejected": len(rejected)}))


if __name__ == "__main__":
    main()
