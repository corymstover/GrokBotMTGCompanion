#!/usr/bin/env python3
"""Generate "EDH Staples.md": data-derived Commander staples by color identity and by role/archetype.

Source: Scryfall oracle_cards bulk (same cache as scripts/ingest_scryfall.py). Only cards that are
**legal in Commander** are listed. Ordering = Scryfall `edhrec_rank` (EDHREC popularity: lower = in
more decks). Popularity is not power; categories are Oracle-text pattern matches (heuristics,
listed in the page). Game Changer flags come from Scryfall `game_changer` (official Commander
Brackets list). Every card links to its Scryfall-verified entry in cards/.
Usage: python3 scripts/build_staples.py [--per-identity 15] [--per-role 15]
"""
import argparse
import csv
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ingest_scryfall as ing  # noqa: E402

OUT = ing.ROOT / "EDH Staples.md"
WUBRG = "WUBRG"
GUILDS = {"WU": "Azorius", "UB": "Dimir", "BR": "Rakdos", "RG": "Gruul", "WG": "Selesnya",
          "WB": "Orzhov", "UR": "Izzet", "BG": "Golgari", "WR": "Boros", "UG": "Simic"}
SHARDS = {"WUG": "Bant", "WUB": "Esper", "UBR": "Grixis", "BRG": "Jund", "WRG": "Naya",
          "WBG": "Abzan", "WUR": "Jeskai", "UBG": "Sultai", "WBR": "Mardu", "URG": "Temur"}


def text_of(c):
    faces = c.get("card_faces") or []
    return (c.get("oracle_text") or " ".join(f.get("oracle_text", "") for f in faces)).replace("\n", " ")


def front_type(c):
    faces = c.get("card_faces") or [c]
    return faces[0].get("type_line") or c.get("type_line", "")


# Role / archetype patterns (Oracle text, case-insensitive). Heuristics — documented in the output.
ROLES = [
    ("Ramp (mana rocks & land ramp)", "nonland", r"add \{[WUBRGC]|add (one|two|three) mana|search your library for (a|up to \w+) (basic )?lands? card|put (a|up to \w+) lands? cards? .*onto the battlefield"),
    ("Card draw & advantage", "nonland", r"draw (two|three|four|x|\w+) cards|whenever .* draw a card|draws? a card for each|draw cards equal"),
    ("Targeted removal", "nonland", r"(destroy|exile) target (creature|artifact|enchantment|planeswalker|permanent|nonland)"),
    ("Board wipes", "nonland", r"(destroy|exile) all (creatures|nonland permanents|other creatures|permanents|artifacts)|all creatures get -\d+/-\d+|each (player|opponent) sacrifices (all|.*creatures)"),
    ("Counterspells", "nonland", r"counter target (spell|noncreature spell|instant|creature spell|activated)"),
    ("Tutors", "nonland", r"search your library for (a|an|up to one) (card|creature|artifact|enchantment|instant|sorcery|planeswalker|land|legendary)"),
    ("Protection", "nonland", r"(hexproof|indestructible|protection from|phase out|can't be countered).*(you control|target creature|permanents you control)|gains? (hexproof|indestructible|shroud)"),
    ("Graveyard recursion", "nonland", r"return (target|up to \w+|all|each) .*from (your|a) graveyard to (your hand|the battlefield)"),
    ("Tokens / go-wide", "nonland", r"create (a|an|two|three|four|x|that many|\w+) .*tokens?"),
    ("Sacrifice / aristocrats", "nonland", r"sacrifice (a|another) (creature|permanent|artifact)[^.]*:|whenever (a|another) creature (you control )?dies"),
    ("+1/+1 counters", "nonland", r"\+1/\+1 counters?"),
    ("Spellslinger (instants & sorceries matter)", "nonland", r"whenever you cast (an|a) (instant|sorcery|noncreature)|instant (and|or) sorcery spells? you cast"),
    ("Landfall / lands matter", "nonland", r"landfall|whenever a land (you control )?enters|play an additional land|play lands from"),
    ("Utility lands", "land", r"."),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--per-identity", type=int, default=15)
    ap.add_argument("--per-role", type=int, default=15)
    args = ap.parse_args()
    cards, bulk = ing.get_bulk(ing.DEFAULT_CACHE, None)
    rows = {r["oracle_id"]: r for r in csv.DictReader(ing.INDEX_CSV.open(encoding="utf-8"))}
    pool = [c for c in cards if c.get("layout") not in ing.EXCLUDED_LAYOUTS and ing.in_universe(c)
            and c.get("legalities", {}).get("commander") == "legal" and c.get("edhrec_rank")
            and c["oracle_id"] in rows]
    pool.sort(key=lambda c: c["edhrec_rank"])

    def ci(c):
        s = set(c.get("color_identity", []))
        return "".join(x for x in WUBRG if x in s) or "C"

    def is_land(c):
        return "Land" in front_type(c)

    def is_basic(c):
        return "Basic" in front_type(c) and "Land" in front_type(c)

    def link(c):
        r = rows[c["oracle_id"]]
        return f"[{r['name']}]({r['shard'].replace(' ', '%20')}#{r['anchor']})"

    def gc(c):
        return "**GC**" if c.get("game_changer") else ""

    def table(cs, show_ci=True):
        head = "| # | Card | EDHREC rank | " + ("Identity | " if show_ci else "") + "MV | Type | GC |"
        sep = "|---|---|---|" + ("---|" if show_ci else "") + "---|---|---|"
        out = [head, sep]
        for i, c in enumerate(cs, 1):
            mv = c.get("cmc", 0)
            mv = int(mv) if float(mv).is_integer() else mv
            out.append(f"| {i} | {link(c)} | {c['edhrec_rank']:,} | " + (f"{ci(c)} | " if show_ci else "")
                       + f"{mv} | {front_type(c).replace('|', '/')} | {gc(c)} |")
        return out

    by_ci = defaultdict(list)
    for c in pool:
        if not is_basic(c):
            by_ci[ci(c)].append(c)

    L = ["# EDH Staples", "",
         f"> **Auto-generated** by `scripts/build_staples.py` from Scryfall Oracle bulk data ({bulk[:10]}) — do not hand-edit. "
         "**Data, not opinion:** lists are Commander-legal cards ordered by Scryfall's `edhrec_rank` "
         "(EDHREC popularity: the lower the rank, the more decks play it). Popularity ≠ power or fit for your deck. "
         "**GC** = on the official Game Changers list (affects [Commander Brackets](EDH%20Standards.md#power-bracket-assessment)). "
         "Strict color identity: a card fits a deck only if its identity is a subset of the commander's ([EDH Standards](EDH%20Standards.md#color-identity-strict)).",
         "> Related: [EDH Standards](EDH%20Standards.md) · [Deck skeletons](EDH%20Standards.md#deck-skeletons) · [Synergy notes](EDH%20Standards.md#synergy-notes) · [Card Index](Card%20Index.md)", "",
         "## Contents", "- [How to use](#how-to-use)", "- [By color identity](#by-color-identity)",
         "  - [Colorless](#colorless) · " + " · ".join(f"[{n}](#{n.lower()})" for n in ["White", "Blue", "Black", "Red", "Green"]),
         "  - Two-color: " + " · ".join(f"[{v} ({k})](#{v.lower()}-{k.lower()})" for k, v in GUILDS.items()),
         "  - Three-color: " + " · ".join(f"[{v} ({k})](#{v.lower()}-{k.lower()})" for k, v in SHARDS.items()),
         "- [By role and archetype](#by-role-and-archetype)", "- [Method & patterns](#method--patterns)", "",
         "## How to use", "",
         "1. Pick your commander and note its color identity.",
         "2. Staples for that deck = the lists for its identity **and every subset** (a Golgari deck can use Colorless, Black, Green and Golgari staples).",
         "3. Use the role lists to fill the standard deck slots (ramp, draw, removal, wipes — see the [deck-building checklist](EDH%20Standards.md#deck-building-checklist)); filter by identity column.",
         "4. Count **GC** cards against your target bracket.", "",
         "## By color identity", "",
         f"Top {args.per_identity} non-basic cards whose color identity is **exactly** that identity (lands included).", ""]
    names = {"C": "Colorless", "W": "White", "U": "Blue", "B": "Black", "R": "Red", "G": "Green"}
    for k in ["C", "W", "U", "B", "R", "G"]:
        L += [f"### {names[k]}", "", f"*{len(by_ci[k]):,} ranked Commander-legal cards with this identity.*", ""]
        L += table(by_ci[k][:args.per_identity], show_ci=False) + [""]
    for group in (GUILDS, SHARDS):
        for k, v in group.items():
            key = "".join(x for x in WUBRG if x in k)
            L += [f"### {v} ({k})", "", f"*{len(by_ci[key]):,} ranked Commander-legal cards with identity {key}.*", ""]
            L += table(by_ci[key][:args.per_identity], show_ci=False) + [""]
    L += ["## By role and archetype", "",
          f"Top {args.per_role} Commander-legal cards per role (any identity). Role = Oracle-text pattern match (see [Method](#method--patterns)); "
          "a card can appear in several roles.", ""]
    counts = {}
    for title, kind, pat in ROLES:
        rx = re.compile(pat, re.I)
        cs = [c for c in pool if (is_land(c) if kind == "land" else not is_land(c)) and not is_basic(c) and rx.search(text_of(c))]
        counts[title] = len(cs)
        L += [f"### {title}", "", f"*{len(cs):,} matching cards.*", ""] + table(cs[:args.per_role]) + [""]
    L += ["## Method & patterns", "",
          f"- Pool: {len(pool):,} Commander-legal cards with an EDHREC rank, all with entries in [`cards/`](cards/).",
          "- Identity lists exclude basic lands; role lists exclude lands except *Utility lands* (all non-basic lands by rank).",
          "- Regular expressions (case-insensitive, on Oracle text of all faces):", ""]
    for title, kind, pat in ROLES:
        L.append(f"  - **{title}** ({counts[title]:,}): `{pat}`")
    L += ["", "Patterns are heuristics: e.g. *Ramp* also catches some mana-ability creatures; *Tokens* catches cards that give tokens to opponents. "
          "Check each card's Oracle text (linked) before including it.", ""]
    OUT.write_text("\n".join(L), encoding="utf-8")
    print(f"wrote {OUT.name}: pool {len(pool)}; roles {counts}")


if __name__ == "__main__":
    sys.exit(main())
