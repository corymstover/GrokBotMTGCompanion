# Grixis Commander Blueprints

> **Milestone M2, Bot cycle 50+.** One machine-readable blueprint per deck (brief §3): Oracle text, plan, the commander's real role, win conditions, engines, packages, key interactions (linked to the [M1 interaction reviews](../interactions/README.md)), tutors, recursion, requirements, failure modes, dependency level, ceilings (source vs GrokBot estimate; only Cory resolves), identity core, anti-goals, thematic constraints and construction rules. Every field carries an evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Data: `data/grixis/blueprints/`; schema: `data/grixis/schemas/blueprint.schema.json`; tool and `validate_all` step `blueprints`: `scripts/grixis_blueprints.py`.

## Contents
- [Status](#status)
- [Blueprints](#blueprints)
- [Ceiling disagreements](#ceiling-disagreements)
- [Method](#method)

## Status

**46/62 blueprints written.** M2 acceptance criteria ([definition](../Grixis%20Authority%20Model.md#m2)):

- ⏳ 62 blueprints validate against blueprint.schema.json and --check — 46/62 written
- ⏳ each names identity core (≥3), anti-goals, required packages with min counts, win conditions, failure modes (≥2), tutor targets, construction rules — 46/62 complete
- ⏳ each has grok_estimated_ceiling with evidence and a disagreement flag where it differs from the source — 46/62 estimated
- ⏳ Cory has reviewed the sample he chooses (status cory_reviewed) — 0 reviewed
- ⏳ Cory accepted M2 (registry program.milestones.M2) — in_progress

## Blueprints

| Deck | Commander role | Dependency | Source ceiling | GrokBot estimate | Expected bracket | Disagreement | Version / status |
|---|---|---|---|---|---|---|---|
| [Abaddon the Despoiler](abaddon-the-despoiler.md) | central | high | 4 | 4 | 4 | no | v1 seeded |
| [Admiral Beckett Brass](admiral-beckett-brass.md) | central | high | — | 4 | 4 | — | v1 seeded |
| [Admiral Brass, Unsinkable](admiral-brass-unsinkable.md) | central | high | — | 4 | 4 | — | v1 seeded |
| [Anhelo, the Painter](anhelo-the-painter.md) | significant | medium | — | 4 | 4 | — | v1 seeded |
| [Ashad, the Lone Cyberman](ashad-the-lone-cyberman.md) | significant | medium | — | 4 | 3 | — | v1 seeded |
| [Ashnod the Uncaring](ashnod-the-uncaring.md) | central | medium | 4 (recovered) | 4 | 4 | no | v1 seeded |
| [Be'lakor, the Dark Master](belakor-the-dark-master.md) | central | high | — | 4 | 4 | — | v1 seeded |
| [Bjorna, Nightfall Alchemist + Cecily, Haunted Mage](bjorna-nightfall-alchemist-cecily.md) | supporting | low | — | 4 | 4 | — | v1 seeded |
| [Cormela, Glamour Thief](cormela-glamour-thief.md) | central | medium | 5 (recovered) | 5 | 5 | no | v1 seeded |
| [Crosis, the Purger](crosis-the-purger.md) | central | high | 4 | 4 | 4 | no | v1 seeded |
| [Cult of Skaro](cult-of-skaro.md) | central | high | 4 | 4 | 3 | no | v1 seeded |
| [Davros, Dalek Creator](davros-dalek-creator.md) | central | high | 4 | 4 | 4 | no | v1 seeded |
| [Doctor Doom, King of Latveria](doctor-doom-king-of-latveria.md) | central | high | 4 | 4 | 4 | no | v1 seeded |
| [Don Andres, the Renegade](don-andres-the-renegade.md) | central | high | 4 | 4 | 4 | no | v1 seeded |
| [Dr. Eggman](dr-eggman.md) | central | high | 4 | 4 | 3 | no | v1 seeded |
| [Edea, Possessed Sorceress](edea-possessed-sorceress.md) | central | high | 4 | 4 | 4 | no | v1 seeded |
| [Edward Kenway](edward-kenway.md) | central | medium | 4 | 4 | 4 | no | v1 seeded |
| [Evelyn, the Covetous](evelyn-the-covetous.md) | significant | low | 5 | 5 | 5 | no | v1 seeded |
| [Fire Lord Azula](fire-lord-azula.md) | significant | medium | 5 | 5 | 5 | no | v1 seeded |
| [Garza Zol, Plague Queen](garza-zol-plague-queen.md) | central | high | 4 | 4 | 4 | no | v1 seeded |
| [Goro-Goro and Satoru](goro-goro-and-satoru.md) | central | high | 4 | 4 | 4 | no | v1 seeded |
| [Kraum, Ludevic's Opus + Tevesh Szat, Doom of Fools](grixistax-october-2026.md) | significant | medium | 5 | 5 | 5 | no | v1 seeded |
| [Gwendlyn Di Corci](gwendlyn-di-corci.md) | central | medium | 4 | 4 | 4 | no | v1 seeded |
| [Inalla, Archmage Ritualist](inalla-archmage-ritualist.md) | central | medium | 5 | 5 | 5 | no | v1 seeded |
| [Jeleva, Nephalia's Scourge](jeleva-nephalias-scourge.md) | significant | medium | 5 | 5 | 5 | no | v1 seeded |
| [Kefka, Court Mage // Kefka, Ruler of Ruin](kefka-court-mage.md) | central | medium | 5 | 5 | 5 | no | v1 seeded |
| [Kess, Dissident Mage](kess-dissident-mage.md) | central | medium | 5 | 5 | 5 | no | v1 seeded |
| [Loki, the Deceiver](loki-the-deceiver.md) | central | high | 4 | 4 | 4 | no | v1 seeded |
| [Lord of Tresserhorn](lord-of-tresserhorn.md) | central | high | 4 | 4 | 4 | no | v1 seeded |
| [Lord Xander, the Collector](lord-xander-the-collector.md) | central | medium | 4 | 4 | 4 | no | v1 seeded |
| [Lynde, Cheerful Tormentor](lynde-cheerful-tormentor.md) | central | high | 4 | 4 | 4 | no | v1 seeded |
| [Mai and Zuko](mai-and-zuko.md) | significant | low | 4 | 4 | 4 | no | v1 seeded |
| [Mairsil, the Pretender](mairsil-the-pretender.md) | central | high | 4 | 4 | 4 | no | v1 seeded |
| [Marchesa, Dealer of Death](marchesa-dealer-of-death.md) | significant | low | 5 | 5 | 5 | no | v1 seeded |
| [Marchesa, the Black Rose](marchesa-the-black-rose.md) | significant | low | 4 | 4 | 4 | no | v1 seeded |
| [Mishra, Artificer Prodigy](mishra-artificer-prodigy.md) | central | medium | 5 | 5 | 5 | no | v1 seeded |
| [Mishra, Eminent One](mishra-eminent-one.md) | central | high | 4 | 4 | 4 | no | v1 seeded |
| [Missy](missy.md) | central | high | 4 | 4 | 4 | no | v1 seeded |
| [Nathan Drake, Treasure Hunter](nathan-drake-treasure-hunter.md) | central | high | 4 | 4 | 4 | no | v1 seeded |
| [Nekusar, the Mindrazer](nekusar-the-mindrazer.md) | significant | medium | 4 | 4 | 4 | no | v1 seeded |
| [Nicol Bolas](nicol-bolas.md) | central | total | 4 | 4 | 4 | no | v1 seeded |
| [Nicol Bolas, the Ravager // Nicol Bolas, the Arisen](nicol-bolas-the-ravager.md) | significant | low | 4 | 4 | 4 | no | v1 seeded |
| [Norman Osborn // Green Goblin](norman-osborn.md) | significant | low | 5 | 5 | 5 | no | v1 seeded |
| [Obeka, Brute Chronologist](obeka-brute-chronologist.md) | central | high | 4 | 4 | 4 | no | v1 seeded |
| [Obeka, Splitter of Seconds](obeka-splitter-of-seconds.md) | central | high | 4 | 4 | 4 | no | v1 seeded |
| [Parnesse, the Subtle Brush](parnesse-the-subtle-brush.md) | supporting | low | 4 | 4 | 4 | no | v1 seeded |

Not written yet (16): [rograkh-son-of-rohgahh-silas-renn](../decks/rograkh-son-of-rohgahh-silas-renn.md), [saruman-the-white-hand](../decks/saruman-the-white-hand.md), [sauron-lord-of-the-rings](../decks/sauron-lord-of-the-rings.md), [sauron-the-dark-lord](../decks/sauron-the-dark-lord.md), [sedris-the-traitor-king](../decks/sedris-the-traitor-king.md), [solkanar-the-swamp-king](../decks/solkanar-the-swamp-king.md), [solkanar-the-tainted](../decks/solkanar-the-tainted.md), [tetsuo-imperial-champion](../decks/tetsuo-imperial-champion.md), [tetsuo-umezawa](../decks/tetsuo-umezawa.md), [the-madcap-jester](../decks/the-madcap-jester.md), [the-rani](../decks/the-rani.md), [the-valeyard](../decks/the-valeyard.md), [thraximundar](../decks/thraximundar.md), [tresserhorns-lord-returned](../decks/tresserhorns-lord-returned.md), [wick-the-whorled-mind](../decks/wick-the-whorled-mind.md), [zevlor-elturel-exile](../decks/zevlor-elturel-exile.md).

## Ceiling disagreements

Flagged for Cory; never applied. Registry: `ceiling.disagreement`.

- None so far.

**Decks with no source bracket in the registry's parsed claim (9):** `Admiral_Beckett_Brass`, `Admiral_Brass__Unsinkable`, `Anhelo__the_Painter`, `Ashad__the_Lone_Cyberman`, `Ashnod_the_Uncaring`, `Be_lakor__the_Dark_Master`, `Cecily__Bjorna__Lutri`, `Cormela__Glamour_Thief`, `Tresserhorn_s_Lord__Returned`. Where a source blueprint or approval states one, the blueprint cites it and `grixis_authority.py --build` records it as *recovered* (the original parse found nothing; nothing is overwritten).

## Method

- **Facts first:** commander Oracle text, type line and Oracle id are copied from the Scryfall cache and re-checked on every run (a change fails `validate_all` until re-reviewed).
- **Evidence:** the source's blueprints, approvals, decision notes and whole-list audits (archived byte-identical), the M1 interaction reviews, Commander Spellbook combos and EDHREC (cached) are cited per claim. Source claims superseded by current Oracle (e.g. older once-per-turn readings) are not carried over.
- **Regex hooks** from `grixis_refine.py` appear only under *supporting features* (heuristic). They never define identity.
- **Card refs** must be in the canonical project list; anything else must be declared as a package *candidate* (Commander-legal, in identity, not in the list).
- **Honesty:** when the commander is not what makes the deck work, `commander_role` says so (`supporting` / `incidental`) and the ceiling estimate is flagged against the source instead of forced.
