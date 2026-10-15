#!/usr/bin/env python3
"""Generate "cEDH Primer.md" (Bot cycle 6, #29). COMPETITIVE (Bracket 5) content, kept separate from casual guides.
Cards come from Scryfall data and must be Commander-legal. Combos come from the Commander Spellbook find-my-combos API,
queried with a fixed list of well-known competitive combo pieces and cached in data/cedh_combos.json.
Usage: python3 scripts/build_cedh.py [--refresh]"""
import json, re, sys, urllib.request, datetime
from edh_lib import Data
import ingest_scryfall as ing

API = "https://backend.commanderspellbook.com/find-my-combos"
CACHE = ing.ROOT / "data" / "cedh_combos.json"
SEED = ["Thassa's Oracle", "Demonic Consultation", "Tainted Pact", "Underworld Breach", "Brain Freeze", "Lion's Eye Diamond",
        "Dramatic Reversal", "Isochron Scepter", "Kiki-Jiki, Mirror Breaker", "Zealous Conscripts", "Heliod, Sun-Crowned",
        "Walking Ballista", "Sanguine Bond", "Exquisite Blood", "Laboratory Maniac", "Jace, Wielder of Mysteries", "Ad Nauseam",
        "Angel's Grace", "Basalt Monolith", "Rings of Brighthearth", "Grim Monolith", "Power Artifact", "Animate Dead",
        "Worldgorger Dragon", "Food Chain", "Squee, the Immortal", "Eternal Scourge", "Hermit Druid", "Peregrine Drake",
        "Deadeye Navigator", "Bolas's Citadel", "Sensei's Divining Top", "Aetherflux Reservoir", "Godo, Bandit Warlord",
        "Helm of the Host", "Niv-Mizzet, Parun", "Curiosity", "Splinter Twin", "Pestermite", "Deceiver Exarch", "Doomsday",
        "Earthcraft", "Squirrel Nest", "Mikaeus, the Unhallowed", "Triskelion", "Ashnod's Altar", "Nim Deathmantle",
        "Hullbreaker Horror", "Sol Ring", "Mana Vault", "Auriok Salvagers", "Bloom Tender", "Freed from the Real",
        "Pemmin's Aura", "Devoted Druid", "Vizier of Remedies", "Selvala, Heart of the Wilds", "Umbral Mantle",
        "Kinnan, Bonder Prodigy", "Najeela, the Blade-Blossom", "Derevi, Empyrial Tactician"]


def combos(refresh):
    if CACHE.exists() and not refresh:
        return json.loads(CACHE.read_text())
    body = json.dumps({"commanders": [], "main": [{"card": c} for c in SEED]}).encode()
    req = urllib.request.Request(API, data=body, headers={"Content-Type": "application/json", "User-Agent": "GrokBotMTGCompanion/1.0"})
    inc = json.load(urllib.request.urlopen(req, timeout=120))["results"]["included"]
    out = {"generated": datetime.date.today().isoformat(), "source": API, "seed": SEED, "combos": [
        {"id": v["id"], "cards": [u["card"]["name"] for u in v["uses"]], "identity": v["identity"],
         "produces": [p["feature"]["name"] for p in v["produces"]], "requires": [t["template"]["name"] for t in v.get("requires", [])],
         "popularity": v.get("popularity") or 0, "prerequisites": v.get("easyPrerequisites", "") + " " + v.get("notablePrerequisites", "")}
        for v in inc]}
    CACHE.write_text(json.dumps(out, indent=1) + "\n")
    return out


def main():
    d = Data()
    cb = combos("--refresh" in sys.argv)
    L = d.header("cEDH Primer", "scripts/build_cedh.py", 29,
                 "Combos come from [Commander Spellbook](https://commanderspellbook.com), cached in `data/cedh_combos.json`.")
    L.insert(2, "> ## ⚠️ COMPETITIVE — Bracket 5 (cEDH)\n> This file covers **competitive Commander** only. Almost everything here breaks the casual-bracket limits: Game Changers, two-card infinites, fast mana and stax. Don't bring it to a Bracket 1–3 table without discussing it in the pre-game talk ([Brackets](EDH%20Standards.md#power-bracket-assessment)). For casual guides, see [EDH Packages](EDH%20Packages.md), [EDH Win Conditions](EDH%20Win%20Conditions.md) and [EDH Interaction](EDH%20Interaction.md).\n")
    banned = [n for n in ("Mana Crypt", "Dockside Extortionist", "Jeweled Lotus", "Nadu, Winged Wisdom")
              if any(c["name"] == n and c["legalities"]["commander"] == "banned" for c in [d.bulk_card(n)] if c)]
    L += ["## Contents", "- [What cEDH is](#what-cedh-is)", "- [Fast mana](#fast-mana)", "- [Tutors](#tutors)",
          "- [Free interaction](#free-interaction)", "- [Compact combos](#compact-combos)", "- [Stax packages](#stax-packages)",
          "- [Guidance (opinion)](#guidance-opinion)", "",
          "## What cEDH is", "",
          "**Fact:** cEDH is Bracket 5 (\"cEDH\") in the official [Commander Brackets](EDH%20Standards.md#power-bracket-assessment). It has no Game Changer, combo or land-denial limits. The ban list still applies: as of this snapshot, Scryfall lists these former cEDH staples as **banned** in Commander: " + ", ".join(f"**{n}**" for n in banned) + ".",
          "**Guidance (opinion):** decks aim to win, or stop someone else from winning, within the first few turns. They play compact combos, cheap tutors and free interaction, and their builds are tuned to the competitive meta.", ""]
    rows = 0

    def sec(title, subs):
        nonlocal rows
        L.extend([f"## {title}", ""])
        for lab, cs, note in subs:
            rows += min(15, len(cs))
            L.extend([f"### {lab}", "", note + f" · {len(cs)} matches, {sum(1 for c in cs if c.get('game_changer'))} Game Changers", ""] + d.table(cs, 15) + [""])

    rocks = [c for c in d.pool if (c.get("cmc") or 0) <= 1 and c.get("produced_mana") and re.search(r"Artifact", d.ftype(c)) and not re.search(r"Creature|Land", d.ftype(c))]
    rituals = d.find(r"Add \{[WUBRG]\}\{[WUBRG]\}\{[WUBRG]\}|Add \{[WUBRG]\}\{[WUBRG]\}|Add three mana|Add X mana", types=r"Instant|Sorcery", maxmv=2)
    dorks = [c for c in d.pool if (c.get("cmc") or 0) <= 1 and c.get("produced_mana") and "Creature" in d.ftype(c)]
    sec("Fast mana", [("Mana rocks, MV ≤ 1", rocks, "Rule: a non-land, non-creature artifact with MV ≤ 1 that has Scryfall `produced_mana`"),
                      ("Rituals, MV ≤ 2", rituals, "Pattern: an instant or sorcery that adds two or more mana"),
                      ("Mana creatures, MV ≤ 1", dorks, "Rule: a creature with MV ≤ 1 that has `produced_mana`")])
    tut = d.find(r"search your library for (a|an|up to one) (card|(instant|sorcery|artifact|creature|enchantment)[^.]*card)(?! with [^.]*land)", maxmv=2, excl=r"basic land")
    sec("Tutors", [("Tutors, MV ≤ 2", tut, "Pattern: `search your library for a/an … card`, excluding land searches")])
    free_ct = d.find(r"rather than pay this spell's mana cost|If you control a commander, you may cast this spell without paying|without paying its mana cost|you may (exile|pay|sacrifice)[^.]*rather than pay", types=r"Instant",
                     extra=lambda c: bool(re.search(r"counter target", d.text(c), re.I)))
    free_rm = d.find(r"rather than pay this spell's mana cost|If you control a commander, you may cast this spell without paying", types=r"Instant",
                     extra=lambda c: not re.search(r"counter target", d.text(c), re.I))
    sec("Free interaction", [("Free counterspells", free_ct, "Pattern: an instant that counters and has an alternative cost"),
                             ("Free removal & protection", free_rm, "Pattern: an instant that doesn't counter and has an alternative cost")])
    legal = set(c["name"] for c in d.pool)
    ok = [x for x in cb["combos"] if all(n in legal for n in x["cards"]) and len(x["cards"]) <= 3]
    ok.sort(key=lambda x: -x["popularity"])
    L += ["## Compact combos", "",
          f"Source: Commander Spellbook `find-my-combos` ({cb['generated']}), queried with {len(cb['seed'])} well-known competitive combo pieces (the seed list is in `scripts/build_cedh.py`). The table keeps combos of three cards or fewer whose cards are all Commander-legal per Scryfall: {len(ok)} of {len(cb['combos'])}. *Spellbook popularity* is the deck count Commander Spellbook reports. ⚠️ Every one of these breaks the Bracket 1–3 limit on early two-card infinites.", "",
          "| # | Cards | Identity | Result | Extra requirements | Spellbook popularity | Spellbook |", "|---|---|---|---|---|---|---|"]
    for i, x in enumerate(ok, 1):
        cl = " + ".join(d.link(d.by_name[n]) + (" **GC**" if d.by_name[n].get("game_changer") else "") for n in x["cards"])
        L.append(f"| {i} | {cl} | {x['identity']} | {', '.join(x['produces'][:3])} | {'; '.join(x['requires']) or '—'} | {x['popularity']:,} | [{x['id']}](https://commanderspellbook.com/combo/{x['id']}/) |")
    L.append("")
    sec("Stax packages", [
        ("Tutor / search hate", d.find(r"can't search libraries|If (an opponent|a player) would search a library"), "Pattern: stops or punishes library searching"),
        ("Spell-count limits", d.find(r"can't cast more than one spell each turn"), "Pattern: one spell per turn"),
        ("Taxes", d.find(r"(spells|noncreature spells|creature spells|activated abilities)[^.]{0,40}cost \{\d\} more", types=r"Artifact|Enchantment|Creature"), "Pattern: spells or abilities cost more"),
        ("Rule-setting hosers", d.find(r"Players can't cast spells from graveyards|Activated abilities of artifacts can't be activated|can't activate abilities that aren't mana abilities|Your opponents can't cast spells during your turn|Each player can't cast noncreature spells"), "Pattern: rule-setting static abilities")])
    L += ["## Guidance (opinion)", "",
          "*Strategy opinion, not rules or fact.*",
          "- **Speed and resilience:** a typical cEDH deck plays a low curve, around 28–32 lands with heavy fast mana, many 1–2 MV tutors, 8–15 free or cheap interaction spells and two or more compact win lines.",
          "- **Hold priority on your win:** expect free counters (Force of Will, Fierce Guardianship and others). Play around them with protection (Silence effects, Grand Abolisher) or by baiting.",
          "- **Thassa's Oracle lines** rely on Oracle's ETB trigger checking your devotion to blue against your library size on resolution. See [ETB/LTB triggers](Rules%20Interactions.md#etb--ltb--look-back-triggers). Answering the trigger or the Oracle in response stops the win.",
          "- **Table politics are lighter:** whoever is closest to winning is usually the one to interact with. Hold answers for the critical turn.",
          "- **Community resources:** [Commander Spellbook](https://commanderspellbook.com) for combos and [EDHREC](https://edhrec.com) for popularity data. Competitive decklist databases exist; they are not linked here because they aren't official.", ""]
    (ing.ROOT / "cEDH Primer.md").write_text("\n".join(L) + "\n")
    print("rows", rows, "combos", len(ok), "of", len(cb["combos"]), "banned", banned)


if __name__ == "__main__":
    main()
