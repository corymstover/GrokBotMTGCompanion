#!/usr/bin/env python3
"""Generate "EDH Mana Bases.md" (Bot cycle 6, #25): mana-base guide for each of the 32 color identities, from Scryfall data.
Usage: python3 scripts/build_mana_bases.py"""
import re, glob, statistics
from edh_lib import Data, NAMES, ORDER, WUBRG
import ingest_scryfall as ing

KINDS = [  # (label, regex on Oracle text) — first match wins
    ("fetch", r"Pay 1 life, Sacrifice this land: Search your library for an? .* card"),
    ("shock", r"you may pay 2 life\. If you don't, it enters tapped"),
    ("fast", r"enters tapped unless you control two or fewer other lands"),
    ("slow", r"enters tapped unless you control two or more other lands"),
    ("check", r"enters tapped unless you control an? (Plains|Island|Swamp|Mountain|Forest)"),
    ("bond (multiplayer)", r"enters tapped unless you have two or more opponents"),
    ("pain", r"deals 1 damage to you"),
    ("filter (two-color)", r"\{1\}, \{T\}: Add \{[WUBRG]\}\{[WUBRG]\}"),
    ("bounce", r"return a land you control to its owner's hand"),
    ("horizon", r"\{T\}, Pay 1 life: Add"),
    ("filter", r"\{[WUBRG]/[WUBRG]\}, \{T\}: Add"),
    ("cycling tapland", r"enters tapped.*Cycling|Cycling.*enters tapped"),
    ("surveil tapland", r"enters tapped.*[Ss]urveil 1"),
    ("tapland", r"enters tapped"),
]


def kind(d, c):
    t = d.text(c)
    if re.fullmatch(r"\(\{T\}: Add \{[WUBRG]\} or \{[WUBRG]\}\.\)", t.strip()): return "original dual"
    for k, p in KINDS:
        if re.search(p, t, re.I): return k
    return "other"


def deck_land_counts():
    out = {}
    for f in sorted(glob.glob(str(ing.ROOT / "decks/*.md"))):
        t = open(f).read()
        sec = t[t.index("## Decklist"):]; sec = sec[:sec.find("\n## ", 5)]
        n = sum(int(m.group(1)) for m in re.finditer(r"^(\d+)x .+? \[Land", sec, re.M))
        out[f.split("/")[-1][:-3]] = n
    return out


def main():
    d = Data()
    lands = [c for c in d.pool if "Land" in d.ftype(c) and "Basic" not in d.ftype(c)]
    L = d.header("EDH Mana Bases", "scripts/build_mana_bases.py", 25)
    L += ["## Contents", "- [Land counts](#land-counts)", "- [Universal fixing (any identity)](#universal-fixing-any-identity)",
          "- [Colorless utility lands](#colorless-utility-lands)", "- [By color identity](#by-color-identity): " +
          " · ".join(f"[{NAMES[k]}](#{re.sub(r'[^a-z0-9 -]', '', (NAMES[k] + ' ' + k).lower()).replace(' ', '-')})" for k in ORDER),
          "- [Method](#method)", ""]
    # land counts
    lc = deck_land_counts()
    vals = list(lc.values())
    L += ["## Land counts", "",
          (f"**Data (this repo's 32 validated skeletons):** all use {vals[0]} lands, the default of `scripts/build_deck_skeleton.py`." if min(vals) == max(vals) else f"**Data (this repo's 32 validated skeletons):** land counts range {min(vals)}–{max(vals)}, median {statistics.median(vals):g}.") + " See the [decks/](decks/) files.", "",
          "**Guidance (opinion):**",
          "- A common starting point for a 100-card deck is about **36–38 lands** plus roughly **10 ramp pieces**.",
          "- Go lower (33–35) with a low curve, many cheap rocks or a mana-producing commander.",
          "- Go higher (38–40+) for lands-matter/landfall decks or a commander that costs 6+ mana.",
          "- **Basics:** keep enough basics for land-search ramp (Cultivate-style spells and the fetches below) and for the checklands' land types. Mono-color decks can run mostly basics plus utility lands.",
          "- **Budget vs. optimized:** the *Budget picks* rows use the cheapest current printings. Optimized mana bases usually move toward untapped duals: originals, shocks, fetches, fast/slow/check, pain, horizon, bond. Taplands are the first cuts.", ""]
    # universal fixing
    uni = [c for c in lands if d.ci(c) == "C" and len(set(c.get("produced_mana") or []) & set(WUBRG)) >= 3]
    L += ["## Universal fixing (any identity)", "",
          "Lands with colorless identity that can produce three or more colors (pattern: Scryfall `produced_mana` ≥ 3 colors). Some are limited by their own text (for example [Command Tower](cards/C/com.md#command-tower) adds only colors in your commander's identity), while others such as City of Brass make any color. Guidance: most valuable in 3+ color decks.", ""]
    L += d.table(uni, 15, cols=("rank", "usd", "gc"), extra=("Kind", lambda c: kind(d, c)))
    L.append("")
    # utility
    UT = [("Fetch lands & land search", r"Search your library for"),
          ("Land destruction / utility removal", r"destroy target (nonbasic )?land|Sacrifice this land: .*destroy"),
          ("Card advantage", r"draw a card|Scry \d|surveil"),
          ("Graveyard interaction", r"graveyard"),
          ("Creature lands", r"becomes? an? .*creature"),
          ("Mana & untapping", r"Add \{C\}\{C\}|for each|untap target"),
          ("Other utility", r".")]
    L += ["## Colorless utility lands", "", "Non-basic colorless-identity lands with a non-mana ability, grouped by the first pattern they match.", ""]
    used = set()
    for lab, p in UT:
        cs = [c for c in lands if d.ci(c) == "C" and c not in uni and c["oracle_id"] not in used
              and re.search(p, d.text(c), re.I) and d.text(c).strip() not in ("{T}: Add {C}.",)]
        for c in cs[:8]: used.add(c["oracle_id"])
        if cs:
            L += [f"### {lab}", f"Pattern: `{p}`", ""] + d.table(cs, 8, cols=("rank", "usd", "gc")) + [""]
    # by identity
    L += ["## By color identity", "",
          "For each identity, the table lists non-basic lands with **exactly** that color identity, most-played first. *Kind* is a heuristic label from Oracle text (fetch, shock, check …); \"tapland\" means it always or usually enters tapped. A deck can also use the lands of every **subset** of its identity, so a 3+ color deck should start from the sections for its color pairs.", ""]
    for k in ORDER:
        anchor_title = f"{NAMES[k]} ({k})"
        cs = [c for c in lands if d.ci(c) == k]
        L += [f"### {NAMES[k]} {k}", ""]
        if k != "C" and len(k) >= 2:
            subs = [s for s in ORDER if s != k and s != "C" and len(s) == 2 and set(s) <= set(k)]
            if len(k) >= 3: L += ["Pair sections to combine: " + " · ".join(f"[{NAMES[s]} ({s})](#{NAMES[s].lower()}-{s.lower()})" for s in subs), ""]
        if not cs:
            L += ["No non-basic lands have exactly this identity; build from the subsets and the universal fixers.", ""]; continue
        L += [f"**Most played** ({len(cs)} lands with this exact identity):", ""] + d.table(cs, 12 if len(k) <= 2 else 8, cols=("rank", "usd", "gc"), extra=("Kind", lambda c: kind(d, c))) + [""]
        if len(k) == 2:
            BT = {"W": "Plains", "U": "Island", "B": "Swamp", "R": "Mountain", "G": "Forest"}
            fe = [c for c in lands if d.ci(c) == "C" and re.search(r"Search your library for", d.text(c))
                  and all(re.search(BT[x], d.text(c)) for x in k)]
            if fe:
                L += [f"**On-color fetches** (colorless identity; can find a land with the {BT[k[0]]} or {BT[k[1]]} type, so they also find the typed duals above):", ""] + d.table(fe, 6, cols=("rank", "usd")) + [""]
        bud = [c for c in cs if d.price.get(c["oracle_id"], 99) <= 1.0]
        if bud:
            L += ["**Budget picks (≤ $1.00):**", ""] + d.table(bud, 6, cols=("rank", "usd"), extra=("Kind", lambda c: kind(d, c))) + [""]
    L += ["## Method", "",
          "- Pool: Commander-legal cards in this repo's card index (Scryfall Oracle bulk). Basics are excluded from the tables.",
          "- *Kind* patterns (first match wins): " + "; ".join(f"{k}: `{p}`" for k, p in KINDS) + ". \"original dual\" means the Oracle text is only the mana reminder text.",
          "- Cheapest USD comes from Scryfall `default_cards` bulk (2026-10-15): the lowest `usd` or `usd_foil` among paper printings.",
          "- Related: [EDH Staples](EDH%20Staples.md) · [EDH Packages](EDH%20Packages.md) · [EDH Standards](EDH%20Standards.md)."]
    (ing.ROOT / "EDH Mana Bases.md").write_text("\n".join(L) + "\n")
    print("identities", len(ORDER), "lands", len(lands), "universal", len(uni))


if __name__ == "__main__":
    main()
