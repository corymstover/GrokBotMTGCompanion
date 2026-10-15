# cEDH Primer

> ## ⚠️ COMPETITIVE — Bracket 5 (cEDH)
> This file covers **competitive Commander** only. Almost everything here breaks the casual-bracket limits: Game Changers, two-card infinites, fast mana and stax. Don't bring it to a Bracket 1–3 table without discussing it in the pre-game talk ([Brackets](EDH%20Standards.md#power-bracket-assessment)). For casual guides, see [EDH Packages](EDH%20Packages.md), [EDH Win Conditions](EDH%20Win%20Conditions.md) and [EDH Interaction](EDH%20Interaction.md).

> **Auto-generated** by `scripts/build_cedh.py` (Bot cycle 6, issue [#29](https://github.com/corymstover/GrokBotMTGCompanion/issues/29)) from Scryfall Oracle bulk 2026-10-15. Do not hand-edit.
> **Data:** every card listed is **Commander-legal** per Scryfall. *Identity* is its color identity: it fits a deck only if that identity is a subset of the commander's ([CR 903.4](Rules%20Interactions.md#commander-color-identity)). Lists are ordered by Scryfall `edhrec_rank` (EDHREC popularity, lower = more played); popularity is not power. **GC** = official Game Changer, which affects the [Commander Brackets](EDH%20Standards.md#power-bracket-assessment). *Cheapest USD* is the lowest current paper price across printings in Scryfall's default-cards bulk (2026-10-15 snapshot; prices move daily). Categories are Oracle-text pattern matches; the patterns are listed in each section.
> **Guidance** paragraphs are strategy advice (opinion), not rules or fact. Combos come from [Commander Spellbook](https://commanderspellbook.com), cached in `data/cedh_combos.json`.

## Contents
- [What cEDH is](#what-cedh-is)
- [Fast mana](#fast-mana)
- [Tutors](#tutors)
- [Free interaction](#free-interaction)
- [Compact combos](#compact-combos)
- [Stax packages](#stax-packages)
- [Guidance (opinion)](#guidance-opinion)

## What cEDH is

**Fact:** cEDH is Bracket 5 ("cEDH") in the official [Commander Brackets](EDH%20Standards.md#power-bracket-assessment). It has no Game Changer, combo or land-denial limits. The ban list still applies: as of this snapshot, Scryfall lists these former cEDH staples as **banned** in Commander: **Mana Crypt**, **Dockside Extortionist**, **Jeweled Lotus**, **Nadu, Winged Wisdom**.
**Guidance (opinion):** decks aim to win, or stop someone else from winning, within the first few turns. They play compact combos, cheap tutors and free interaction, and their builds are tuned to the competitive meta.

## Fast mana

### Mana rocks, MV ≤ 1

Rule: a non-land, non-creature artifact with MV ≤ 1 that has Scryfall `produced_mana` · 39 matches, 4 Game Changers

| Card | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|
| [Sol Ring](cards/S/so.md#sol-ring) | C | 1 | 1 | $1.28 |  |
| [Lotus Petal](cards/L/lo.md#lotus-petal) | C | 0 | 120 | $34.91 |  |
| [Mana Vault](cards/M/man.md#mana-vault) | C | 1 | 152 | $65.50 | **GC** |
| [Chrome Mox](cards/C/chr.md#chrome-mox) | C | 0 | 156 | $51.19 | **GC** |
| [Mox Amber](cards/M/mox.md#mox-amber) | C | 0 | 205 | $84.76 |  |
| [Mox Opal](cards/M/mox.md#mox-opal) | C | 0 | 243 | $227.30 |  |
| [Mox Diamond](cards/M/mox.md#mox-diamond) | C | 0 | 248 | $1,117.50 | **GC** |
| [Everflowing Chalice](cards/E/ev.md#everflowing-chalice) | C | 0 | 252 | $0.28 |  |
| [Springleaf Drum](cards/S/spr.md#springleaf-drum) | C | 1 | 562 | $0.25 |  |
| [Lion's Eye Diamond](cards/L/li.md#lions-eye-diamond) | C | 0 | 741 | $807.47 | **GC** |
| [Astral Cornucopia](cards/A/as.md#astral-cornucopia) | C | 0 | 1,315 | $0.30 |  |
| [Diamond Pick-Axe](cards/D/di.md#diamond-pick-axe) | R | 1 | 1,491 | $2.52 |  |
| [Paradise Mantle](cards/P/pa.md#paradise-mantle) | C | 0 | 1,789 | $7.78 |  |
| [Sol Talisman](cards/S/so.md#sol-talisman) | C | 0 | 2,412 | $0.77 |  |
| [Mox Jasper](cards/M/mox.md#mox-jasper) | C | 0 | 2,494 | $11.37 |  |

### Rituals, MV ≤ 2

Pattern: an instant or sorcery that adds two or more mana · 10 matches, 0 Game Changers

| Card | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|
| [Dark Ritual](cards/D/da.md#dark-ritual) | B | 1 | 33 | $0.25 |  |
| [Cabal Ritual](cards/C/cab.md#cabal-ritual) | B | 2 | 442 | $14.14 |  |
| [Culling the Weak](cards/C/cu.md#culling-the-weak) | B | 1 | 508 | $7.05 |  |
| [Rite of Flame](cards/R/ri.md#rite-of-flame) | R | 1 | 646 | $4.96 |  |
| [Pyretic Ritual](cards/P/py.md#pyretic-ritual) | R | 2 | 711 | $7.38 |  |
| [Desperate Ritual](cards/D/des.md#desperate-ritual) | R | 2 | 953 | $5.38 |  |
| [Infernal Plunge](cards/I/inf.md#infernal-plunge) | R | 1 | 3,044 | $0.42 |  |
| [Burnt Offering](cards/B/bu.md#burnt-offering) | BR | 1 | 3,126 | $1.57 |  |
| [Esper Origins // Summon: Esper Maduin](cards/E/es.md#esper-origins--summon-esper-maduin) | G | 2 | 5,150 | $1.67 |  |
| [Metamorphosis](cards/M/me.md#metamorphosis) | G | 1 | 8,601 | $0.32 |  |

### Mana creatures, MV ≤ 1

Rule: a creature with MV ≤ 1 that has `produced_mana` · 58 matches, 0 Game Changers

| Card | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|
| [Birds of Paradise](cards/B/bi.md#birds-of-paradise) | G | 1 | 35 | $4.98 |  |
| [Llanowar Elves](cards/L/ll.md#llanowar-elves) | G | 1 | 56 | $0.25 |  |
| [Elvish Mystic](cards/E/el.md#elvish-mystic) | G | 1 | 102 | $0.42 |  |
| [Delighted Halfling](cards/D/del.md#delighted-halfling) | G | 1 | 148 | $24.33 |  |
| [Fyndhorn Elves](cards/F/fy.md#fyndhorn-elves) | G | 1 | 217 | $1.13 |  |
| [Avacyn's Pilgrim](cards/A/av.md#avacyns-pilgrim) | WG | 1 | 501 | $0.28 |  |
| [Ignoble Hierarch](cards/I/ig.md#ignoble-hierarch) | BRG | 1 | 535 | $0.92 |  |
| [Deathrite Shaman](cards/D/dea.md#deathrite-shaman) | BG | 1 | 615 | $4.46 |  |
| [Elves of Deep Shadow](cards/E/el.md#elves-of-deep-shadow) | BG | 1 | 742 | $4.42 |  |
| [Noble Hierarch](cards/N/no.md#noble-hierarch) | WUG | 1 | 772 | $10.83 |  |
| [Dryad Arbor](cards/D/dry.md#dryad-arbor) | G | 0 | 778 | $3.34 |  |
| [Gilded Goose](cards/G/gi.md#gilded-goose) | G | 1 | 807 | $0.37 |  |
| [Skirk Prospector](cards/S/sk.md#skirk-prospector) | R | 1 | 1,354 | $0.28 |  |
| [Impulsive Pilferer](cards/I/im.md#impulsive-pilferer) | R | 1 | 1,727 | $0.25 |  |
| [Greedy Freebooter](cards/G/gre.md#greedy-freebooter) | B | 1 | 2,352 | $1.09 |  |

## Tutors

### Tutors, MV ≤ 2

Pattern: `search your library for a/an … card`, excluding land searches · 65 matches, 8 Game Changers

| Card | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|
| [Demonic Tutor](cards/D/dem.md#demonic-tutor) | B | 2 | 64 | $62.34 | **GC** |
| [Vampiric Tutor](cards/V/va.md#vampiric-tutor) | B | 1 | 115 | $48.13 | **GC** |
| [Enlightened Tutor](cards/E/en.md#enlightened-tutor) | W | 1 | 123 | $21.99 | **GC** |
| [Mystical Tutor](cards/M/my.md#mystical-tutor) | U | 1 | 162 | $14.99 | **GC** |
| [Worldly Tutor](cards/W/wo.md#worldly-tutor) | G | 1 | 171 | $26.36 | **GC** |
| [Gamble](cards/G/ga.md#gamble) | R | 1 | 241 | $16.07 | **GC** |
| [Diabolic Intent](cards/D/di.md#diabolic-intent) | B | 2 | 275 | $14.64 |  |
| [Entomb](cards/E/en.md#entomb) | B | 1 | 325 | $11.89 |  |
| [Wishclaw Talisman](cards/W/wi.md#wishclaw-talisman) | B | 2 | 526 | $1.84 |  |
| [Imperial Seal](cards/I/im.md#imperial-seal) | B | 1 | 541 | $162.01 | **GC** |
| [Muddle the Mixture](cards/M/mu.md#muddle-the-mixture) | U | 2 | 709 | $1.88 |  |
| [Eladamri's Call](cards/E/el.md#eladamris-call) | WG | 2 | 780 | $11.25 |  |
| [Nature's Rhythm](cards/N/na.md#natures-rhythm) | G | 2 | 861 | $3.29 |  |
| [Goblin Engineer](cards/G/gob.md#goblin-engineer) | R | 2 | 1,190 | $8.38 |  |
| [Insatiable Avarice](cards/I/ins.md#insatiable-avarice) | B | 1 | 1,213 | $5.43 |  |

## Free interaction

### Free counterspells

Pattern: an instant that counters and has an alternative cost · 19 matches, 2 Game Changers

| Card | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|
| [Fierce Guardianship](cards/F/fi.md#fierce-guardianship) | U | 3 | 82 | $60.84 | **GC** |
| [Force of Will](cards/F/fo.md#force-of-will) | U | 5 | 202 | $26.56 | **GC** |
| [Force of Negation](cards/F/fo.md#force-of-negation) | U | 3 | 272 | $44.31 |  |
| [Tibalt's Trickery](cards/T/ti.md#tibalts-trickery) | R | 2 | 600 | $10.04 |  |
| [Flare of Denial](cards/F/fl.md#flare-of-denial) | U | 3 | 1,444 | $3.53 |  |
| [Delay](cards/D/del.md#delay) | U | 2 | 2,245 | $1.71 |  |
| [Daze](cards/D/da.md#daze) | U | 2 | 3,002 | $0.88 |  |
| [Foil](cards/F/fo.md#foil) | U | 4 | 4,263 | $1.67 |  |
| [Disrupting Shoal](cards/D/di.md#disrupting-shoal) | U | 2 | 9,431 | $15.99 |  |
| [Forceful Denial](cards/F/fo.md#forceful-denial) | U | 5 | 9,482 | $0.26 |  |
| [Counterpoint](cards/C/cou.md#counterpoint) | UB | 5 | 9,755 | $0.38 |  |
| [Reinterpret](cards/R/rei.md#reinterpret) | UR | 4 | 9,916 | $0.45 |  |
| [Admiral's Order](cards/A/ad.md#admirals-order) | U | 3 | 11,499 | $0.30 |  |
| [Thwart](cards/T/thw.md#thwart) | U | 4 | 15,512 | $0.79 |  |
| [Hurl into History](cards/H/hu.md#hurl-into-history) | U | 5 | 16,141 | $0.19 |  |

### Free removal & protection

Pattern: an instant that doesn't counter and has an alternative cost · 62 matches, 0 Game Changers

| Card | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|
| [Deflecting Swat](cards/D/def.md#deflecting-swat) | R | 3 | 74 | $72.06 |  |
| [Deadly Rollick](cards/D/dea.md#deadly-rollick) | B | 4 | 106 | $26.07 |  |
| [Flawless Maneuver](cards/F/fl.md#flawless-maneuver) | W | 3 | 173 | $8.48 |  |
| [Mindbreak Trap](cards/M/min.md#mindbreak-trap) | U | 4 | 551 | $7.09 |  |
| [Snuff Out](cards/S/sn.md#snuff-out) | B | 4 | 691 | $5.28 |  |
| [Flare of Fortitude](cards/F/fl.md#flare-of-fortitude) | W | 4 | 735 | $4.85 |  |
| [Force of Vigor](cards/F/fo.md#force-of-vigor) | G | 4 | 1,021 | $5.62 |  |
| [Flare of Duplication](cards/F/fl.md#flare-of-duplication) | R | 3 | 1,136 | $2.41 |  |
| [Flare of Malice](cards/F/fl.md#flare-of-malice) | B | 4 | 1,303 | $2.94 |  |
| [Baleful Mastery](cards/B/bal.md#baleful-mastery) | B | 4 | 1,429 | $1.94 |  |
| [Obscuring Haze](cards/O/ob.md#obscuring-haze) | G | 3 | 1,493 | $4.92 |  |
| [Misdirection](cards/M/mis.md#misdirection) | U | 5 | 1,498 | $5.96 |  |
| [Commandeer](cards/C/com.md#commandeer) | U | 7 | 1,893 | $3.85 |  |
| [Force of Despair](cards/F/fo.md#force-of-despair) | B | 3 | 2,456 | $6.43 |  |
| [Invigorate](cards/I/inv.md#invigorate) | G | 3 | 3,478 | $0.26 |  |

## Compact combos

Source: Commander Spellbook `find-my-combos` (2026-10-15), queried with 61 well-known competitive combo pieces (the seed list is in `scripts/build_cedh.py`). The table keeps combos of three cards or fewer whose cards are all Commander-legal per Scryfall: 61 of 61. *Spellbook popularity* is the deck count Commander Spellbook reports. ⚠️ Every one of these breaks the Bracket 1–3 limit on early two-card infinites.

| # | Cards | Identity | Result | Extra requirements | Spellbook popularity | Spellbook |
|---|---|---|---|---|---|---|
| 1 | [Hullbreaker Horror](cards/H/hu.md#hullbreaker-horror) + [Sol Ring](cards/S/so.md#sol-ring) | U | Infinite colorless mana, Infinite storm count | Permanent Castable for {C} | 359,378 | [513-5034--46](https://commanderspellbook.com/combo/513-5034--46/) |
| 2 | [Sanguine Bond](cards/S/san.md#sanguine-bond) + [Exquisite Blood](cards/E/ex.md#exquisite-blood) | B | Infinite lifegain triggers, Infinite lifeloss, Infinite lifegain | — | 149,544 | [690-3966](https://commanderspellbook.com/combo/690-3966/) |
| 3 | [Demonic Consultation](cards/D/dem.md#demonic-consultation) + [Thassa's Oracle](cards/T/tha.md#thassas-oracle) **GC** | UB | Exile your library, Win the game | — | 149,189 | [742-1295](https://commanderspellbook.com/combo/742-1295/) |
| 4 | [Tainted Pact](cards/T/ta.md#tainted-pact) + [Thassa's Oracle](cards/T/tha.md#thassas-oracle) **GC** | UB | Win the game | — | 131,438 | [1295-3093](https://commanderspellbook.com/combo/1295-3093/) |
| 5 | [Dramatic Reversal](cards/D/dra.md#dramatic-reversal) + [Isochron Scepter](cards/I/is.md#isochron-scepter) | U | Infinite magecraft triggers, Infinite mana nonland permanents you control can produce, Infinite storm count | — | 106,467 | [4821-5261](https://commanderspellbook.com/combo/4821-5261/) |
| 6 | [Underworld Breach](cards/U/un.md#underworld-breach) **GC** + [Lion's Eye Diamond](cards/L/li.md#lions-eye-diamond) **GC** + [Brain Freeze](cards/B/br.md#brain-freeze) | UR | Infinite self-mill, Near-infinite colored mana, Near-infinite magecraft triggers | — | 95,287 | [1368-3518-4856](https://commanderspellbook.com/combo/1368-3518-4856/) |
| 7 | [Hullbreaker Horror](cards/H/hu.md#hullbreaker-horror) + [Mana Vault](cards/M/man.md#mana-vault) **GC** | U | Infinite colorless mana, Infinite storm count | Permanent Castable for {C}{C} | 77,571 | [513-2364--47](https://commanderspellbook.com/combo/513-2364--47/) |
| 8 | [Curiosity](cards/C/cu.md#curiosity) + [Niv-Mizzet, Parun](cards/N/ni.md#niv-mizzet-parun) | UR | Infinite draw triggers, Infinite card draw, Near-infinite damage | — | 68,558 | [1089-2353](https://commanderspellbook.com/combo/1089-2353/) |
| 9 | [Aetherflux Reservoir](cards/A/ae.md#aetherflux-reservoir) + [Exquisite Blood](cards/E/ex.md#exquisite-blood) | B | Infinite damage, Infinite lifegain triggers | — | 56,295 | [3966-4740](https://commanderspellbook.com/combo/3966-4740/) |
| 10 | [Rings of Brighthearth](cards/R/ri.md#rings-of-brighthearth) + [Basalt Monolith](cards/B/bas.md#basalt-monolith) | C | Infinite colorless mana | — | 53,328 | [4131-4235](https://commanderspellbook.com/combo/4131-4235/) |
| 11 | [Heliod, Sun-Crowned](cards/H/he.md#heliod-sun-crowned) + [Walking Ballista](cards/W/wal.md#walking-ballista) | W | Infinite damage, Infinite lifegain, Infinite lifegain triggers | — | 52,194 | [1274-3693](https://commanderspellbook.com/combo/1274-3693/) |
| 12 | [Sensei's Divining Top](cards/S/sen.md#senseis-divining-top) + [Aetherflux Reservoir](cards/A/ae.md#aetherflux-reservoir) + [Bolas's Citadel](cards/B/bo.md#bolass-citadel) **GC** | B | Infinite card draw, Infinite draw triggers, Near-infinite damage | — | 51,436 | [2173-4740-5078](https://commanderspellbook.com/combo/2173-4740-5078/) |
| 13 | [Peregrine Drake](cards/P/pe.md#peregrine-drake) + [Deadeye Navigator](cards/D/dea.md#deadeye-navigator) | U | Infinite blinking, Infinite creature ETB, Infinite creature LTB | — | 47,389 | [1409-3821](https://commanderspellbook.com/combo/1409-3821/) |
| 14 | [Kinnan, Bonder Prodigy](cards/K/ki.md#kinnan-bonder-prodigy) + [Basalt Monolith](cards/B/bas.md#basalt-monolith) | GU | Infinite colorless mana | — | 46,828 | [129-4131](https://commanderspellbook.com/combo/129-4131/) |
| 15 | [Squee, the Immortal](cards/S/sq.md#squee-the-immortal) + [Food Chain](cards/F/fo.md#food-chain) | RG | Infinite colored mana that can only be spent to cast creature spells, Infinite creature ETB, Infinite creature LTB | — | 35,868 | [3519-3705](https://commanderspellbook.com/combo/3519-3705/) |
| 16 | [Kiki-Jiki, Mirror Breaker](cards/K/ki.md#kiki-jiki-mirror-breaker) + [Zealous Conscripts](cards/Z/ze.md#zealous-conscripts) | R | Infinite creature tokens with haste, Infinite death triggers, Infinite creature ETB | — | 28,017 | [618-1537](https://commanderspellbook.com/combo/618-1537/) |
| 17 | [Godo, Bandit Warlord](cards/G/god.md#godo-bandit-warlord) + [Helm of the Host](cards/H/he.md#helm-of-the-host) | R | Infinite combat phases, Infinite death triggers, Infinite creature ETB | — | 25,750 | [1692-4251](https://commanderspellbook.com/combo/1692-4251/) |
| 18 | [Bloom Tender](cards/B/blo.md#bloom-tender) + [Freed from the Real](cards/F/fr.md#freed-from-the-real) | GU | Infinite non-blue mana of colors among permanents you control, Infinite mana of colors among permanents you control | — | 23,280 | [4222-5168](https://commanderspellbook.com/combo/4222-5168/) |
| 19 | [Eternal Scourge](cards/E/et.md#eternal-scourge) + [Food Chain](cards/F/fo.md#food-chain) | G | Infinite colored mana that can only be spent to cast creature spells, Infinite creature ETB, Infinite creature LTB | — | 19,268 | [1806-3519](https://commanderspellbook.com/combo/1806-3519/) |
| 20 | [Worldgorger Dragon](cards/W/wo.md#worldgorger-dragon) + [Animate Dead](cards/A/an.md#animate-dead) | BR | Infinite death triggers, Infinite blinking of permanents, Infinite colored mana | — | 15,660 | [4812-4846](https://commanderspellbook.com/combo/4812-4846/) |
| 21 | [Kiki-Jiki, Mirror Breaker](cards/K/ki.md#kiki-jiki-mirror-breaker) + [Helm of the Host](cards/H/he.md#helm-of-the-host) | R | Infinite death triggers, Infinite creature ETB, Infinite creature LTB | — | 15,594 | [618-1692](https://commanderspellbook.com/combo/618-1692/) |
| 22 | [Umbral Mantle](cards/U/um.md#umbral-mantle) + [Selvala, Heart of the Wilds](cards/S/sel.md#selvala-heart-of-the-wilds) | G | Infinite colored mana, Infinitely large creature until end of turn, Infinite untap of creatures you control | — | 15,237 | [527-2816](https://commanderspellbook.com/combo/527-2816/) |
| 23 | [Demonic Consultation](cards/D/dem.md#demonic-consultation) + [Laboratory Maniac](cards/L/la.md#laboratory-maniac) | UB | Exile your library, Win the game | — | 14,549 | [742-2836](https://commanderspellbook.com/combo/742-2836/) |
| 24 | [Doomsday](cards/D/do.md#doomsday) + [Thassa's Oracle](cards/T/tha.md#thassas-oracle) **GC** | UB | Win the game | — | 14,531 | [1295-3189](https://commanderspellbook.com/combo/1295-3189/) |
| 25 | [Bloom Tender](cards/B/blo.md#bloom-tender) + [Pemmin's Aura](cards/P/pe.md#pemmins-aura) | GU | Infinite non-blue mana of colors among permanents you control, Infinite mana of colors among permanents you control | — | 14,147 | [3525-5168](https://commanderspellbook.com/combo/3525-5168/) |
| 26 | [Kinnan, Bonder Prodigy](cards/K/ki.md#kinnan-bonder-prodigy) + [Bloom Tender](cards/B/blo.md#bloom-tender) + [Freed from the Real](cards/F/fr.md#freed-from-the-real) | GU | Infinite mana of colors among permanents you control, Infinite non-blue mana of colors among permanents you control, Put most creature cards from your library onto the battlefield | — | 12,242 | [129-4222-5168](https://commanderspellbook.com/combo/129-4222-5168/) |
| 27 | [Walking Ballista](cards/W/wal.md#walking-ballista) + [Mikaeus, the Unhallowed](cards/M/mik.md#mikaeus-the-unhallowed) | B | Infinite death triggers, Infinite creature ETB, Infinite creature LTB | — | 11,976 | [628-3693](https://commanderspellbook.com/combo/628-3693/) |
| 28 | [Power Artifact](cards/P/po.md#power-artifact) + [Basalt Monolith](cards/B/bas.md#basalt-monolith) | U | Infinite colorless mana | — | 10,866 | [4131-5149](https://commanderspellbook.com/combo/4131-5149/) |
| 29 | [Selvala, Heart of the Wilds](cards/S/sel.md#selvala-heart-of-the-wilds) + [Freed from the Real](cards/F/fr.md#freed-from-the-real) | GU | Infinite colored mana | — | 10,370 | [527-4222](https://commanderspellbook.com/combo/527-4222/) |
| 30 | [Hermit Druid](cards/H/he.md#hermit-druid) + [Thassa's Oracle](cards/T/tha.md#thassas-oracle) **GC** | GU | Win the game | — | 10,354 | [1295-4400](https://commanderspellbook.com/combo/1295-4400/) |
| 31 | [Najeela, the Blade-Blossom](cards/N/na.md#najeela-the-blade-blossom) + [Derevi, Empyrial Tactician](cards/D/der.md#derevi-empyrial-tactician) | WUBRG | Infinite creature tokens with haste, Infinite untap of permanents you control, Infinite colored mana | — | 10,066 | [2011-2608](https://commanderspellbook.com/combo/2011-2608/) |
| 32 | [Power Artifact](cards/P/po.md#power-artifact) + [Grim Monolith](cards/G/gri.md#grim-monolith) **GC** | U | Infinite colorless mana | — | 9,898 | [2585-5149](https://commanderspellbook.com/combo/2585-5149/) |
| 33 | [Tainted Pact](cards/T/ta.md#tainted-pact) + [Laboratory Maniac](cards/L/la.md#laboratory-maniac) | UB | Win the game | — | 9,640 | [2836-3093](https://commanderspellbook.com/combo/2836-3093/) |
| 34 | [Demonic Consultation](cards/D/dem.md#demonic-consultation) + [Jace, Wielder of Mysteries](cards/J/ja.md#jace-wielder-of-mysteries) | UB | Exile your library, Win the game | — | 9,443 | [742-3096](https://commanderspellbook.com/combo/742-3096/) |
| 35 | [Mikaeus, the Unhallowed](cards/M/mik.md#mikaeus-the-unhallowed) + [Triskelion](cards/T/tri.md#triskelion) | B | Infinite damage, Infinite death triggers, Infinite creature ETB | — | 8,454 | [628-1495](https://commanderspellbook.com/combo/628-1495/) |
| 36 | [Earthcraft](cards/E/ea.md#earthcraft) + [Squirrel Nest](cards/S/sq.md#squirrel-nest) | G | Infinite creature ETB, Infinite tapped creature tokens | — | 8,431 | [515-2757](https://commanderspellbook.com/combo/515-2757/) |
| 37 | [Mikaeus, the Unhallowed](cards/M/mik.md#mikaeus-the-unhallowed) + [Devoted Druid](cards/D/dev.md#devoted-druid) | BG | Infinite death triggers, Infinite creature ETB, Infinite creature LTB | — | 7,571 | [628-4762](https://commanderspellbook.com/combo/628-4762/) |
| 38 | [Hermit Druid](cards/H/he.md#hermit-druid) + [Laboratory Maniac](cards/L/la.md#laboratory-maniac) | GU | Win the game | — | 7,224 | [2836-4400](https://commanderspellbook.com/combo/2836-4400/) |
| 39 | [Tainted Pact](cards/T/ta.md#tainted-pact) + [Jace, Wielder of Mysteries](cards/J/ja.md#jace-wielder-of-mysteries) | UB | Win the game | — | 7,030 | [3093-3096](https://commanderspellbook.com/combo/3093-3096/) |
| 40 | [Selvala, Heart of the Wilds](cards/S/sel.md#selvala-heart-of-the-wilds) + [Pemmin's Aura](cards/P/pe.md#pemmins-aura) | GU | Infinite colored mana | — | 6,999 | [527-3525](https://commanderspellbook.com/combo/527-3525/) |
| 41 | [Lion's Eye Diamond](cards/L/li.md#lions-eye-diamond) **GC** + [Auriok Salvagers](cards/A/au.md#auriok-salvagers) | W | Infinite colored mana, Infinite storm count, Return some artifact cards from your graveyard to your hand | — | 6,732 | [2055-3518](https://commanderspellbook.com/combo/2055-3518/) |
| 42 | [Heliod, Sun-Crowned](cards/H/he.md#heliod-sun-crowned) + [Triskelion](cards/T/tri.md#triskelion) | W | Infinite damage, Infinite lifegain, Infinite lifegain triggers | — | 6,257 | [1274-1495](https://commanderspellbook.com/combo/1274-1495/) |
| 43 | [Devoted Druid](cards/D/dev.md#devoted-druid) + [Vizier of Remedies](cards/V/vi.md#vizier-of-remedies) | GW | Infinite green mana | — | 4,909 | [978-4762](https://commanderspellbook.com/combo/978-4762/) |
| 44 | [Hermit Druid](cards/H/he.md#hermit-druid) + [Jace, Wielder of Mysteries](cards/J/ja.md#jace-wielder-of-mysteries) | GU | Win the game | — | 4,730 | [3096-4400](https://commanderspellbook.com/combo/3096-4400/) |
| 45 | [Splinter Twin](cards/S/spl.md#splinter-twin) + [Zealous Conscripts](cards/Z/ze.md#zealous-conscripts) | R | Infinite creature tokens with haste, Infinite creature ETB | — | 4,588 | [1537-4702](https://commanderspellbook.com/combo/1537-4702/) |
| 46 | [Najeela, the Blade-Blossom](cards/N/na.md#najeela-the-blade-blossom) + [Selvala, Heart of the Wilds](cards/S/sel.md#selvala-heart-of-the-wilds) | WUBRG | Infinite creature tokens with haste, Infinite colored mana, Infinite combat phases | — | 4,243 | [527-2011](https://commanderspellbook.com/combo/527-2011/) |
| 47 | [Kiki-Jiki, Mirror Breaker](cards/K/ki.md#kiki-jiki-mirror-breaker) + [Deceiver Exarch](cards/D/dec.md#deceiver-exarch) | UR | Infinite creature tokens with haste, Infinite death triggers, Infinite creature ETB | — | 2,521 | [618-2198](https://commanderspellbook.com/combo/618-2198/) |
| 48 | [Kiki-Jiki, Mirror Breaker](cards/K/ki.md#kiki-jiki-mirror-breaker) + [Pestermite](cards/P/pe.md#pestermite) | UR | Infinite creature tokens with haste, Infinite death triggers, Infinite creature ETB | — | 2,218 | [618-2905](https://commanderspellbook.com/combo/618-2905/) |
| 49 | [Kiki-Jiki, Mirror Breaker](cards/K/ki.md#kiki-jiki-mirror-breaker) + [Worldgorger Dragon](cards/W/wo.md#worldgorger-dragon) | R | Infinite blinking of permanents, Infinite blinking, Infinite creature ETB | — | 1,798 | [618-4846](https://commanderspellbook.com/combo/618-4846/) |
| 50 | [Deadeye Navigator](cards/D/dea.md#deadeye-navigator) + [Derevi, Empyrial Tactician](cards/D/der.md#derevi-empyrial-tactician) + [Bloom Tender](cards/B/blo.md#bloom-tender) | GWU | Infinite creature ETB, Infinite green mana, Infinite creature LTB | — | 1,659 | [1409-2608-5168](https://commanderspellbook.com/combo/1409-2608-5168/) |
| 51 | [Splinter Twin](cards/S/spl.md#splinter-twin) + [Deceiver Exarch](cards/D/dec.md#deceiver-exarch) | UR | Infinite creature tokens with haste, Infinite creature ETB | — | 1,317 | [2198-4702](https://commanderspellbook.com/combo/2198-4702/) |
| 52 | [Splinter Twin](cards/S/spl.md#splinter-twin) + [Pestermite](cards/P/pe.md#pestermite) | UR | Infinite creature tokens with haste, Infinite creature ETB | — | 1,235 | [2905-4702](https://commanderspellbook.com/combo/2905-4702/) |
| 53 | [Kiki-Jiki, Mirror Breaker](cards/K/ki.md#kiki-jiki-mirror-breaker) + [Freed from the Real](cards/F/fr.md#freed-from-the-real) | UR | Infinite creature LTB, Infinite creature ETB, Infinite creature sacrifice triggers | Mana Dork or Mana Dork Creator | 952 | [618-4222--140](https://commanderspellbook.com/combo/618-4222--140/) |
| 54 | [Ad Nauseam](cards/A/ad.md#ad-nauseam) **GC** + [Laboratory Maniac](cards/L/la.md#laboratory-maniac) + [Angel's Grace](cards/A/an.md#angels-grace) | WUB | Win the game | — | 715 | [335-1984-2836](https://commanderspellbook.com/combo/335-1984-2836/) |
| 55 | [Najeela, the Blade-Blossom](cards/N/na.md#najeela-the-blade-blossom) + [Bloom Tender](cards/B/blo.md#bloom-tender) + [Helm of the Host](cards/H/he.md#helm-of-the-host) | WUBRG | Infinite creature tokens with haste, Infinite combat phases, Infinite creature ETB | — | 658 | [1692-2011-5168](https://commanderspellbook.com/combo/1692-2011-5168/) |
| 56 | [Kiki-Jiki, Mirror Breaker](cards/K/ki.md#kiki-jiki-mirror-breaker) + [Pemmin's Aura](cards/P/pe.md#pemmins-aura) | UR | Infinite creature LTB, Infinite creature ETB, Infinite creature sacrifice triggers | Mana Dork or Mana Dork Creator | 430 | [618-3525--140](https://commanderspellbook.com/combo/618-3525--140/) |
| 57 | [Ad Nauseam](cards/A/ad.md#ad-nauseam) **GC** + [Angel's Grace](cards/A/an.md#angels-grace) + [Jace, Wielder of Mysteries](cards/J/ja.md#jace-wielder-of-mysteries) | WUB | Infinite card draw, Win the game | — | 425 | [335-1984-3096](https://commanderspellbook.com/combo/335-1984-3096/) |
| 58 | [Nim Deathmantle](cards/N/ni.md#nim-deathmantle) + [Ashnod's Altar](cards/A/as.md#ashnods-altar) + [Peregrine Drake](cards/P/pe.md#peregrine-drake) | U | Infinite colorless mana, Infinite death triggers, Infinite creature ETB | — | 351 | [2034-3821-5003](https://commanderspellbook.com/combo/2034-3821-5003/) |
| 59 | [Derevi, Empyrial Tactician](cards/D/der.md#derevi-empyrial-tactician) + [Bloom Tender](cards/B/blo.md#bloom-tender) + [Ashnod's Altar](cards/A/as.md#ashnods-altar) | GWU | Infinite colorless mana, Infinite death triggers, Infinite creature ETB | — | 283 | [2034-2608-5168](https://commanderspellbook.com/combo/2034-2608-5168/) |
| 60 | [Mikaeus, the Unhallowed](cards/M/mik.md#mikaeus-the-unhallowed) + [Devoted Druid](cards/D/dev.md#devoted-druid) + [Earthcraft](cards/E/ea.md#earthcraft) | BG | Infinite colored mana, Infinite death triggers, Infinite creature ETB | — | 175 | [628-2757-4762](https://commanderspellbook.com/combo/628-2757-4762/) |
| 61 | [Splinter Twin](cards/S/spl.md#splinter-twin) + [Derevi, Empyrial Tactician](cards/D/der.md#derevi-empyrial-tactician) | RGWU | Infinite death triggers, Infinite creature ETB, Infinite creature LTB | — | 55 | [2608-4702](https://commanderspellbook.com/combo/2608-4702/) |

## Stax packages

### Tutor / search hate

Pattern: stops or punishes library searching · 5 matches, 0 Game Changers

| Card | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|
| [Aven Mindcensor](cards/A/av.md#aven-mindcensor) | W | 3 | 1,264 | $0.42 |  |
| [Stranglehold](cards/S/str.md#stranglehold) | R | 4 | 6,843 | $7.03 |  |
| [Leonin Arbiter](cards/L/le.md#leonin-arbiter) | W | 2 | 7,230 | $0.38 |  |
| [Mindlock Orb](cards/M/min.md#mindlock-orb) | U | 4 | 19,090 | $0.48 |  |
| [Shadow of Doubt](cards/S/sha.md#shadow-of-doubt) | UB | 2 | 19,378 | $3.65 |  |

### Spell-count limits

Pattern: one spell per turn · 9 matches, 0 Game Changers

| Card | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|
| [Archon of Emeria](cards/A/arc.md#archon-of-emeria) | W | 3 | 2,134 | $1.06 |  |
| [Rule of Law](cards/R/ru.md#rule-of-law) | W | 3 | 3,465 | $0.40 |  |
| [Eidolon of Rhetoric](cards/E/ei.md#eidolon-of-rhetoric) | W | 3 | 3,562 | $0.47 |  |
| [High Noon](cards/H/hi.md#high-noon) | WR | 2 | 7,826 | $4.69 |  |
| [Curse of Exhaustion](cards/C/cu.md#curse-of-exhaustion) | W | 4 | 9,057 | $0.37 |  |
| [Arcane Laboratory](cards/A/arc.md#arcane-laboratory) | U | 3 | 9,801 | $0.52 |  |
| [Moderation](cards/M/mod.md#moderation) | WU | 3 | 15,428 | $0.26 |  |
| [Colfenor's Plans](cards/C/col.md#colfenors-plans) | B | 4 | 19,506 | $0.37 |  |
| [Yawgmoth's Agenda](cards/Y/ya.md#yawgmoths-agenda) | B | 5 | 27,168 | $0.34 |  |

### Taxes

Pattern: spells or abilities cost more · 31 matches, 1 Game Changers

| Card | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|
| [Grand Arbiter Augustin IV](cards/G/gra.md#grand-arbiter-augustin-iv) | WU | 4 | 1,804 | $18.35 | **GC** |
| [Aura of Silence](cards/A/au.md#aura-of-silence) | W | 3 | 2,201 | $2.39 |  |
| [Thalia, Guardian of Thraben](cards/T/tha.md#thalia-guardian-of-thraben) | W | 2 | 2,375 | $0.42 |  |
| [God-Pharaoh's Statue](cards/G/god.md#god-pharaohs-statue) | C | 6 | 2,450 | $0.67 |  |
| [Elspeth Conquers Death](cards/E/el.md#elspeth-conquers-death) | W | 5 | 3,114 | $0.61 |  |
| [Charix, the Raging Isle](cards/C/cha.md#charix-the-raging-isle) | U | 4 | 3,690 | $0.38 |  |
| [Paladin Class](cards/P/pa.md#paladin-class) | W | 1 | 4,776 | $0.45 |  |
| [Thorn of Amethyst](cards/T/tho.md#thorn-of-amethyst) | C | 2 | 6,675 | $0.55 |  |
| [Charitable Levy](cards/C/cha.md#charitable-levy) | W | 2 | 7,078 | $0.19 |  |
| [Lodestone Golem](cards/L/lo.md#lodestone-golem) | C | 4 | 7,247 | $0.30 |  |
| [Disruptor Flute](cards/D/di.md#disruptor-flute) | C | 2 | 7,327 | $1.72 |  |
| [Tithe Taker](cards/T/ti.md#tithe-taker) | W | 2 | 7,866 | $0.33 |  |
| [Vryn Wingmare](cards/V/vr.md#vryn-wingmare) | W | 3 | 8,420 | $0.18 |  |
| [Sphere of Resistance](cards/S/sph.md#sphere-of-resistance) | C | 2 | 8,484 | $9.91 |  |
| [Tax Collector](cards/T/ta.md#tax-collector) | W | 2 | 8,577 | $0.34 |  |

### Rule-setting hosers

Pattern: rule-setting static abilities · 15 matches, 0 Game Changers

| Card | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|
| [Kutzil, Malamet Exemplar](cards/K/ku.md#kutzil-malamet-exemplar) | WG | 3 | 396 | $2.18 |  |
| [Voice of Victory](cards/V/vo.md#voice-of-victory) | W | 2 | 499 | $18.19 |  |
| [Conqueror's Flail](cards/C/con.md#conquerors-flail) | C | 2 | 1,331 | $0.53 |  |
| [Dragonlord Dromoka](cards/D/dra.md#dragonlord-dromoka) | WG | 6 | 1,891 | $1.84 |  |
| [Grafdigger's Cage](cards/G/gra.md#grafdiggers-cage) | C | 1 | 2,151 | $2.23 |  |
| [Collector Ouphe](cards/C/col.md#collector-ouphe) | G | 2 | 2,489 | $1.96 |  |
| [Tidal Barracuda](cards/T/ti.md#tidal-barracuda) | U | 4 | 4,416 | $7.63 |  |
| [Stony Silence](cards/S/sto.md#stony-silence) | W | 2 | 6,304 | $0.49 |  |
| [Jennifer Walters // The Sensational She-Hulk](cards/J/je.md#jennifer-walters--the-sensational-she-hulk) | WG | 2 | 7,291 | $5.58 |  |
| [Ashes of the Abhorrent](cards/A/as.md#ashes-of-the-abhorrent) | W | 2 | 8,298 | $0.71 |  |
| [Weathered Runestone](cards/W/we.md#weathered-runestone) | C | 2 | 8,321 | $0.34 |  |
| [Overwhelming Splendor](cards/O/ov.md#overwhelming-splendor) | W | 8 | 8,677 | $6.91 |  |
| [Kunoros, Hound of Athreos](cards/K/ku.md#kunoros-hound-of-athreos) | WB | 3 | 9,329 | $0.39 |  |
| [Null Rod](cards/N/nu.md#null-rod) | C | 2 | 9,345 | $110.49 |  |
| [Abeyance](cards/A/ab.md#abeyance) | W | 2 | 13,964 | $4.44 |  |

## Guidance (opinion)

*Strategy opinion, not rules or fact.*
- **Speed and resilience:** a typical cEDH deck plays a low curve, around 28–32 lands with heavy fast mana, many 1–2 MV tutors, 8–15 free or cheap interaction spells and two or more compact win lines.
- **Hold priority on your win:** expect free counters (Force of Will, Fierce Guardianship and others). Play around them with protection (Silence effects, Grand Abolisher) or by baiting.
- **Thassa's Oracle lines** rely on Oracle's ETB trigger checking your devotion to blue against your library size on resolution. See [ETB/LTB triggers](Rules%20Interactions.md#etb--ltb--look-back-triggers). Answering the trigger or the Oracle in response stops the win.
- **Table politics are lighter:** whoever is closest to winning is usually the one to interact with. Hold answers for the critical turn.
- **Community resources:** [Commander Spellbook](https://commanderspellbook.com) for combos and [EDHREC](https://edhrec.com) for popularity data. Competitive decklist databases exist; they are not linked here because they aren't official.

