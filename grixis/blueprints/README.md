# Grixis Commander Blueprints

> **Milestone M2, Bot cycle 50+.** One machine-readable blueprint per deck (brief §3): Oracle text, plan, the commander's real role, win conditions, engines, packages, key interactions (linked to the [M1 interaction reviews](../interactions/README.md)), tutors, recursion, requirements, failure modes, dependency level, ceilings (source vs GrokBot estimate; only Cory resolves), identity core, anti-goals, thematic constraints and construction rules. Every field carries an evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Data: `data/grixis/blueprints/`; schema: `data/grixis/schemas/blueprint.schema.json`; tool and `validate_all` step `blueprints`: `scripts/grixis_blueprints.py`.

## Contents
- [Status](#status)
- [Blueprints](#blueprints)
- [Ceiling disagreements](#ceiling-disagreements)
- [Method](#method)

## Status

**15/62 blueprints written.** M2 acceptance criteria ([definition](../Grixis%20Authority%20Model.md#m2)):

- ⏳ 62 blueprints validate against blueprint.schema.json and --check — 15/62 written
- ⏳ each names identity core (≥3), anti-goals, required packages with min counts, win conditions, failure modes (≥2), tutor targets, construction rules — 15/62 complete
- ⏳ each has grok_estimated_ceiling with evidence and a disagreement flag where it differs from the source — 15/62 estimated
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

Not written yet (47): [edea-possessed-sorceress](../decks/edea-possessed-sorceress.md), [edward-kenway](../decks/edward-kenway.md), [evelyn-the-covetous](../decks/evelyn-the-covetous.md), [fire-lord-azula](../decks/fire-lord-azula.md), [garza-zol-plague-queen](../decks/garza-zol-plague-queen.md), [goro-goro-and-satoru](../decks/goro-goro-and-satoru.md), [grixistax-october-2026](../decks/grixistax-october-2026.md), [gwendlyn-di-corci](../decks/gwendlyn-di-corci.md), [inalla-archmage-ritualist](../decks/inalla-archmage-ritualist.md), [jeleva-nephalias-scourge](../decks/jeleva-nephalias-scourge.md), [kefka-court-mage](../decks/kefka-court-mage.md), [kess-dissident-mage](../decks/kess-dissident-mage.md), [loki-the-deceiver](../decks/loki-the-deceiver.md), [lord-of-tresserhorn](../decks/lord-of-tresserhorn.md), [lord-xander-the-collector](../decks/lord-xander-the-collector.md), [lynde-cheerful-tormentor](../decks/lynde-cheerful-tormentor.md), [mai-and-zuko](../decks/mai-and-zuko.md), [mairsil-the-pretender](../decks/mairsil-the-pretender.md), [marchesa-dealer-of-death](../decks/marchesa-dealer-of-death.md), [marchesa-the-black-rose](../decks/marchesa-the-black-rose.md), [mishra-artificer-prodigy](../decks/mishra-artificer-prodigy.md), [mishra-eminent-one](../decks/mishra-eminent-one.md), [missy](../decks/missy.md), [nathan-drake-treasure-hunter](../decks/nathan-drake-treasure-hunter.md), [nekusar-the-mindrazer](../decks/nekusar-the-mindrazer.md), [nicol-bolas](../decks/nicol-bolas.md), [nicol-bolas-the-ravager](../decks/nicol-bolas-the-ravager.md), [norman-osborn](../decks/norman-osborn.md), [obeka-brute-chronologist](../decks/obeka-brute-chronologist.md), [obeka-splitter-of-seconds](../decks/obeka-splitter-of-seconds.md), [parnesse-the-subtle-brush](../decks/parnesse-the-subtle-brush.md), [rograkh-son-of-rohgahh-silas-renn](../decks/rograkh-son-of-rohgahh-silas-renn.md), [saruman-the-white-hand](../decks/saruman-the-white-hand.md), [sauron-lord-of-the-rings](../decks/sauron-lord-of-the-rings.md), [sauron-the-dark-lord](../decks/sauron-the-dark-lord.md), [sedris-the-traitor-king](../decks/sedris-the-traitor-king.md), [solkanar-the-swamp-king](../decks/solkanar-the-swamp-king.md), [solkanar-the-tainted](../decks/solkanar-the-tainted.md), [tetsuo-imperial-champion](../decks/tetsuo-imperial-champion.md), [tetsuo-umezawa](../decks/tetsuo-umezawa.md), [the-madcap-jester](../decks/the-madcap-jester.md), [the-rani](../decks/the-rani.md), [the-valeyard](../decks/the-valeyard.md), [thraximundar](../decks/thraximundar.md), [tresserhorns-lord-returned](../decks/tresserhorns-lord-returned.md), [wick-the-whorled-mind](../decks/wick-the-whorled-mind.md), [zevlor-elturel-exile](../decks/zevlor-elturel-exile.md).

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
