---
title: "Deck Skeleton — The Gitrog Monster — Innistrad-only"
category: deck
kind: plane
commander: "The Gitrog Monster"
color_identity: BG
bracket_floor: 2
game_changers: 0
validated: true
plane: innistrad
---

# Deck Skeleton — The Gitrog Monster — Innistrad-only

> **Data-derived skeleton, not a tuned list.** Built 2026-10-15 by `scripts/build_deck_skeleton.py` from [EDHREC](https://edhrec.com/commanders/the-gitrog-monster) inclusion rates (community data) and validated against Scryfall Oracle bulk (2026-10-15). Card choices = most-included cards for this commander; *any judgment about what to cut/add is Opinion*. Format per [EDH Standards](../EDH%20Standards.md).

## Contents
- [Commander](#commander)
- [Validation](#validation)
- [Bracket assessment](#bracket-assessment)
- [Decklist (Archidekt import)](#decklist-archidekt-import)
- [Card breakdown](#card-breakdown)
- [Rejected candidates](#rejected-candidates)
- [Commander rules & rulings](#commander-rules--rulings)
- [Combos (Commander Spellbook)](#combos-commander-spellbook)

## Commander

- **[The Gitrog Monster](../cards/T/theg.md#the-gitrog-monster)** — {3}{B}{G} — Legendary Creature — Frog Horror
- Color identity: **BG (Black, Green)**
- Eligibility: Yes (legendary creature)
- EDHREC sample: 10160 decks · bracket distribution reported by EDHREC: B1: 15, B2: 492, B3: 855, B4: 750, B5: 684

## Validation

- Total cards: **100** (1 commander + 63 nonland + 8 nonbasic lands + 28 basics)
- **Plane restriction (Innistrad):** every non-basic card has a paper printing in sets `avr, dka, emn, isd, mid, soi, vow` (Scryfall default-cards). 53 slots were filled from that card pool by EDHREC rank because the EDHREC suggestions ran out (marked — in the inclusion column). Filler prefers the commander's creature types (tribe: Frog, Horror), then EDHREC rank; multicolor decks also get up to 8 on-plane dual lands. *This is an outline: filler cards are popular on-plane cards, not hand-tuned synergy (Opinion: review them).*
- Strict color identity (CR 903.5c), singleton (903.5b), Commander-legal, size (903.5a): ✅ **all checks pass**

## Bracket assessment

- Game Changers (0): none
- Extra-turn cards: Emrakul, the Promised End
- Mass land denial: none
- Two-card infinite combos: ⚠️ not machine-checked — review manually.
- **Minimum bracket by the published barometers: 2 (Core) or 1 (Exhibition) — no Game Changers; final call depends on combos/intent.** (Brackets are a pregame-conversation tool; see [EDH Standards](../EDH%20Standards.md#power-bracket-assessment).)

## Decklist (Archidekt import)

```text
1x The Gitrog Monster [Commander{top}]
1x Splendid Reclamation [Sorcery]
1x Traverse the Ulvenwald [Sorcery]
1x Eldritch Evolution [Sorcery]
1x Army of the Damned [Sorcery]
1x Noose Constrictor [Creature]
1x Tireless Tracker [Creature]
1x Cultivator Colossus [Creature]
1x Olivia's Dragoon [Creature]
1x Old Stickfingers [Creature]
1x Eternal Scourge [Creature]
1x Gnarlwood Dryad [Creature]
1x Moldgraf Millipede [Creature]
1x Loam Dryad [Creature]
1x Voldaren Pariah // Abolisher of Bloodlines [Creature]
1x Vorstclaw [Creature]
1x Ulvenwald Captive // Ulvenwald Abomination [Creature]
1x Emrakul's Evangel [Creature]
1x Stromkirk Condemned [Creature]
1x Morkrut Necropod [Creature]
1x Dread Slaver [Creature]
1x Weirded Vampire [Creature]
1x Shrill Howler // Howling Chorus [Creature]
1x Kessig Prowler // Sinuous Predator [Creature]
1x Tangleclaw Werewolf // Fibrous Entangler [Creature]
1x Kessig Dire Swine [Creature]
1x Foul Emissary [Creature]
1x Blood Artist [Creature]
1x Morbid Opportunist [Creature]
1x Craterhoof Behemoth [Creature]
1x Champion of Lambholt [Creature]
1x Gravecrawler [Creature]
1x Augur of Autumn [Creature]
1x Saryth, the Viper's Fang [Creature]
1x Mikaeus, the Unhallowed [Creature]
1x Jadar, Ghoulcaller of Nephalia [Creature]
1x Soul of the Harvest [Creature]
1x Emrakul, the Promised End [Creature]
1x Tree of Perdition [Creature]
1x Harvester of Souls [Creature]
1x Cryptbreaker [Creature]
1x Falkenrath Noble [Creature]
1x Diregraf Colossus [Creature]
1x Grapple with the Past [Instant]
1x Infernal Grasp [Instant]
1x Second Harvest [Instant]
1x Return to Nature [Instant]
1x Murder [Instant]
1x Tragic Slip [Instant]
1x Undying Malice [Instant]
1x Hero's Downfall [Instant]
1x Naturalize [Instant]
1x Wrenn and Seven [Planeswalker]
1x Parallel Lives [Enchantment]
1x Unnatural Growth [Enchantment]
1x The Meathook Massacre [Enchantment]
1x Exquisite Blood [Enchantment]
1x Cryptolith Rite [Enchantment]
1x Descendants' Path [Enchantment]
1x Endless Ranks of the Dead [Enchantment]
1x Conjurer's Closet [Artifact]
1x Moonsilver Key [Artifact]
1x Haunted Cloak [Artifact]
1x Grafdigger's Cage [Artifact]
1x Evolving Wilds [Land]
1x Woodland Cemetery [Land]
1x Ghost Quarter [Land]
1x Cavern of Souls [Land]
1x Deathcap Glade [Land]
1x Voldaren Estate [Land]
1x Foul Orchard [Land]
1x Shimmering Grotto [Land]
14x Swamp [Land]
14x Forest [Land]
```

## Card breakdown

| Card | Section | EDHREC inclusion | Identity |
|---|---|---|---|
| [Splendid Reclamation](../cards/S/spl.md#splendid-reclamation) | Sorcery | 50% | G |
| [Traverse the Ulvenwald](../cards/T/tra.md#traverse-the-ulvenwald) | Sorcery | 10% | G |
| [Eldritch Evolution](../cards/E/el.md#eldritch-evolution) | Sorcery | 8% | G |
| [Army of the Damned](../cards/A/arm.md#army-of-the-damned) | Sorcery | — | B |
| [Noose Constrictor](../cards/N/no.md#noose-constrictor) | Creature | 49% | G |
| [Tireless Tracker](../cards/T/ti.md#tireless-tracker) | Creature | 16% | G |
| [Cultivator Colossus](../cards/C/cu.md#cultivator-colossus) | Creature | 13% | G |
| [Olivia's Dragoon](../cards/O/ol.md#olivias-dragoon) | Creature | 6% | B |
| [Old Stickfingers](../cards/O/ol.md#old-stickfingers) | Creature | — | BG |
| [Eternal Scourge](../cards/E/et.md#eternal-scourge) | Creature | — | C |
| [Gnarlwood Dryad](../cards/G/gn.md#gnarlwood-dryad) | Creature | — | G |
| [Moldgraf Millipede](../cards/M/mol.md#moldgraf-millipede) | Creature | — | G |
| [Loam Dryad](../cards/L/lo.md#loam-dryad) | Creature | — | G |
| [Voldaren Pariah // Abolisher of Bloodlines](../cards/V/vo.md#voldaren-pariah--abolisher-of-bloodlines) | Creature | — | B |
| [Vorstclaw](../cards/V/vo.md#vorstclaw) | Creature | — | G |
| [Ulvenwald Captive // Ulvenwald Abomination](../cards/U/ul.md#ulvenwald-captive--ulvenwald-abomination) | Creature | — | G |
| [Emrakul's Evangel](../cards/E/em.md#emrakuls-evangel) | Creature | — | G |
| [Stromkirk Condemned](../cards/S/str.md#stromkirk-condemned) | Creature | — | B |
| [Morkrut Necropod](../cards/M/mor.md#morkrut-necropod) | Creature | — | B |
| [Dread Slaver](../cards/D/dre.md#dread-slaver) | Creature | — | B |
| [Weirded Vampire](../cards/W/we.md#weirded-vampire) | Creature | — | B |
| [Shrill Howler // Howling Chorus](../cards/S/shr.md#shrill-howler--howling-chorus) | Creature | — | G |
| [Kessig Prowler // Sinuous Predator](../cards/K/ke.md#kessig-prowler--sinuous-predator) | Creature | — | G |
| [Tangleclaw Werewolf // Fibrous Entangler](../cards/T/ta.md#tangleclaw-werewolf--fibrous-entangler) | Creature | — | G |
| [Kessig Dire Swine](../cards/K/ke.md#kessig-dire-swine) | Creature | — | G |
| [Foul Emissary](../cards/F/fo.md#foul-emissary) | Creature | — | G |
| [Blood Artist](../cards/B/blo.md#blood-artist) | Creature | — | B |
| [Morbid Opportunist](../cards/M/mor.md#morbid-opportunist) | Creature | — | B |
| [Craterhoof Behemoth](../cards/C/cr.md#craterhoof-behemoth) | Creature | — | G |
| [Champion of Lambholt](../cards/C/cha.md#champion-of-lambholt) | Creature | — | G |
| [Gravecrawler](../cards/G/gra.md#gravecrawler) | Creature | — | B |
| [Augur of Autumn](../cards/A/au.md#augur-of-autumn) | Creature | — | G |
| [Saryth, the Viper's Fang](../cards/S/sar.md#saryth-the-vipers-fang) | Creature | — | G |
| [Mikaeus, the Unhallowed](../cards/M/mik.md#mikaeus-the-unhallowed) | Creature | — | B |
| [Jadar, Ghoulcaller of Nephalia](../cards/J/ja.md#jadar-ghoulcaller-of-nephalia) | Creature | — | B |
| [Soul of the Harvest](../cards/S/so.md#soul-of-the-harvest) | Creature | — | G |
| [Emrakul, the Promised End](../cards/E/em.md#emrakul-the-promised-end) | Creature | — | C |
| [Tree of Perdition](../cards/T/tre.md#tree-of-perdition) | Creature | — | B |
| [Harvester of Souls](../cards/H/ha.md#harvester-of-souls) | Creature | — | B |
| [Cryptbreaker](../cards/C/cr.md#cryptbreaker) | Creature | — | B |
| [Falkenrath Noble](../cards/F/fa.md#falkenrath-noble) | Creature | — | B |
| [Diregraf Colossus](../cards/D/di.md#diregraf-colossus) | Creature | — | B |
| [Grapple with the Past](../cards/G/gra.md#grapple-with-the-past) | Instant | 14% | G |
| [Infernal Grasp](../cards/I/inf.md#infernal-grasp) | Instant | 10% | B |
| [Second Harvest](../cards/S/sec.md#second-harvest) | Instant | — | G |
| [Return to Nature](../cards/R/ret.md#return-to-nature) | Instant | — | G |
| [Murder](../cards/M/mu.md#murder) | Instant | — | B |
| [Tragic Slip](../cards/T/tra.md#tragic-slip) | Instant | — | B |
| [Undying Malice](../cards/U/un.md#undying-malice) | Instant | — | B |
| [Hero's Downfall](../cards/H/he.md#heros-downfall) | Instant | — | B |
| [Naturalize](../cards/N/na.md#naturalize) | Instant | — | G |
| [Wrenn and Seven](../cards/W/wr.md#wrenn-and-seven) | Planeswalker | 8% | G |
| [Parallel Lives](../cards/P/pa.md#parallel-lives) | Enchantment | — | G |
| [Unnatural Growth](../cards/U/un.md#unnatural-growth) | Enchantment | — | G |
| [The Meathook Massacre](../cards/T/them.md#the-meathook-massacre) | Enchantment | — | B |
| [Exquisite Blood](../cards/E/ex.md#exquisite-blood) | Enchantment | — | B |
| [Cryptolith Rite](../cards/C/cr.md#cryptolith-rite) | Enchantment | — | G |
| [Descendants' Path](../cards/D/des.md#descendants-path) | Enchantment | — | G |
| [Endless Ranks of the Dead](../cards/E/en.md#endless-ranks-of-the-dead) | Enchantment | — | B |
| [Conjurer's Closet](../cards/C/con.md#conjurers-closet) | Artifact | — | C |
| [Moonsilver Key](../cards/M/moo.md#moonsilver-key) | Artifact | — | C |
| [Haunted Cloak](../cards/H/ha.md#haunted-cloak) | Artifact | — | C |
| [Grafdigger's Cage](../cards/G/gra.md#grafdiggers-cage) | Artifact | — | C |
| [Evolving Wilds](../cards/E/ev.md#evolving-wilds) | Land | 46% | C |
| [Woodland Cemetery](../cards/W/wo.md#woodland-cemetery) | Land | 42% | BG |
| [Ghost Quarter](../cards/G/gh.md#ghost-quarter) | Land | 25% | C |
| [Cavern of Souls](../cards/C/cav.md#cavern-of-souls) | Land | — | C |
| [Deathcap Glade](../cards/D/dea.md#deathcap-glade) | Land | — | BG |
| [Voldaren Estate](../cards/V/vo.md#voldaren-estate) | Land | — | C |
| [Foul Orchard](../cards/F/fo.md#foul-orchard) | Land | — | BG |
| [Shimmering Grotto](../cards/S/shi.md#shimmering-grotto) | Land | — | C |
| 14× Swamp | Basic land | — | — |
| 14× Forest | Basic land | — | — |

## Rejected candidates

EDHREC suggestions excluded by validation (should normally be empty or only off-identity/illegal cards):

- Command Tower — no printing in Innistrad
- Sol Ring — no printing in Innistrad
- Dakmor Salvage — no printing in Innistrad
- Crop Rotation — no printing in Innistrad
- Ramunap Excavator — no printing in Innistrad
- Life from the Loam — no printing in Innistrad
- Sylvan Safekeeper — no printing in Innistrad
- Assassin's Trophy — no printing in Innistrad
- Overgrown Tomb — no printing in Innistrad
- Icetill Explorer — no printing in Innistrad
- Verdant Catacombs — no printing in Innistrad
- Harrow — no printing in Innistrad
- Six — no printing in Innistrad
- Lotus Cobra — no printing in Innistrad
- Dark Ritual — no printing in Innistrad
- Llanowar Wastes — no printing in Innistrad
- Zuran Orb — no printing in Innistrad
- Azusa, Lost but Seeking — no printing in Innistrad
- Llanowar Elves — no printing in Innistrad
- Abrupt Decay — no printing in Innistrad
- Titania, Protector of Argoth — no printing in Innistrad
- Sylvan Scrying — no printing in Innistrad
- Crucible of Worlds — no printing in Innistrad
- Golgari Grave-Troll — no printing in Innistrad
- Scute Swarm — no printing in Innistrad
- Culling Ritual — no printing in Innistrad
- Aftermath Analyst — no printing in Innistrad
- Arcane Signet — no printing in Innistrad
- Oblivion Crown — no printing in Innistrad
- Tireless Provisioner — no printing in Innistrad

<!-- RULES-NOTES:START -->
## Commander rules & rulings

> Auto-generated by `scripts/deck_rules_notes.py` from Scryfall Oracle bulk (2026-10-15) and rulings bulk (2026-10-15); rulings are quoted verbatim (source: Wizards of the Coast unless marked). Facts only — strategy is in [EDH Standards](../EDH%20Standards.md#synergy-notes), labeled Opinion.

**Oracle text — [The Gitrog Monster](../cards/T/theg.md#the-gitrog-monster):**
> The Gitrog Monster: Deathtouch / At the beginning of your upkeep, sacrifice The Gitrog Monster unless you sacrifice a land. / You may play an additional land on each of your turns. / Whenever one or more land cards are put into your graveyard from anywhere, draw a card.

**Official rulings on the commander (1):**
- *2025-01-24* — If multiple land cards are put into your graveyard at once, The Gitrog Monster's last ability triggers only once. This could happen because an effect put them there from your library at the same time (such as by a mill effect) or because they were destroyed at the same time (such as two land creatures that were dealt lethal combat damage).

**Creature-type overlap** with the commander (Frog, Horror): 18 card(s) — [Old Stickfingers](../cards/O/ol.md#old-stickfingers), [Eternal Scourge](../cards/E/et.md#eternal-scourge), [Gnarlwood Dryad](../cards/G/gn.md#gnarlwood-dryad), [Moldgraf Millipede](../cards/M/mol.md#moldgraf-millipede), [Loam Dryad](../cards/L/lo.md#loam-dryad), [Voldaren Pariah // Abolisher of Bloodlines](../cards/V/vo.md#voldaren-pariah--abolisher-of-bloodlines), [Vorstclaw](../cards/V/vo.md#vorstclaw), [Ulvenwald Captive // Ulvenwald Abomination](../cards/U/ul.md#ulvenwald-captive--ulvenwald-abomination), [Emrakul's Evangel](../cards/E/em.md#emrakuls-evangel), [Stromkirk Condemned](../cards/S/str.md#stromkirk-condemned), [Morkrut Necropod](../cards/M/mor.md#morkrut-necropod), [Dread Slaver](../cards/D/dre.md#dread-slaver) ….

**Deck cards with official rulings:** 55 of 71 non-basic cards — [Splendid Reclamation](../cards/S/spl.md#splendid-reclamation) (1), [Traverse the Ulvenwald](../cards/T/tra.md#traverse-the-ulvenwald) (6), [Eldritch Evolution](../cards/E/el.md#eldritch-evolution) (6), [Army of the Damned](../cards/A/arm.md#army-of-the-damned) (6), [Tireless Tracker](../cards/T/ti.md#tireless-tracker) (8), [Cultivator Colossus](../cards/C/cu.md#cultivator-colossus) (2), [Olivia's Dragoon](../cards/O/ol.md#olivias-dragoon) (1), [Old Stickfingers](../cards/O/ol.md#old-stickfingers) (2), [Eternal Scourge](../cards/E/et.md#eternal-scourge) (3), [Moldgraf Millipede](../cards/M/mol.md#moldgraf-millipede) (1), [Loam Dryad](../cards/L/lo.md#loam-dryad) (1), [Voldaren Pariah // Abolisher of Bloodlines](../cards/V/vo.md#voldaren-pariah--abolisher-of-bloodlines) (10), [Ulvenwald Captive // Ulvenwald Abomination](../cards/U/ul.md#ulvenwald-captive--ulvenwald-abomination) (1), [Emrakul's Evangel](../cards/E/em.md#emrakuls-evangel) (1), [Stromkirk Condemned](../cards/S/str.md#stromkirk-condemned) (2), [Morkrut Necropod](../cards/M/mor.md#morkrut-necropod) (2), [Dread Slaver](../cards/D/dre.md#dread-slaver) (4), [Weirded Vampire](../cards/W/we.md#weirded-vampire) (9), [Shrill Howler // Howling Chorus](../cards/S/shr.md#shrill-howler--howling-chorus) (2), [Kessig Prowler // Sinuous Predator](../cards/K/ke.md#kessig-prowler--sinuous-predator) (1), [Tangleclaw Werewolf // Fibrous Entangler](../cards/T/ta.md#tangleclaw-werewolf--fibrous-entangler) (4), [Kessig Dire Swine](../cards/K/ke.md#kessig-dire-swine) (5), [Foul Emissary](../cards/F/fo.md#foul-emissary) (1), [Blood Artist](../cards/B/blo.md#blood-artist) (1), [Morbid Opportunist](../cards/M/mor.md#morbid-opportunist) (1), [Craterhoof Behemoth](../cards/C/cr.md#craterhoof-behemoth) (2), [Champion of Lambholt](../cards/C/cha.md#champion-of-lambholt) (2), [Gravecrawler](../cards/G/gra.md#gravecrawler) (2), [Augur of Autumn](../cards/A/au.md#augur-of-autumn) (9), [Saryth, the Viper's Fang](../cards/S/sar.md#saryth-the-vipers-fang) (1), [Mikaeus, the Unhallowed](../cards/M/mik.md#mikaeus-the-unhallowed) (4), [Jadar, Ghoulcaller of Nephalia](../cards/J/ja.md#jadar-ghoulcaller-of-nephalia) (4), [Soul of the Harvest](../cards/S/so.md#soul-of-the-harvest) (1), [Emrakul, the Promised End](../cards/E/em.md#emrakul-the-promised-end) (18), [Tree of Perdition](../cards/T/tre.md#tree-of-perdition) (3), [Harvester of Souls](../cards/H/ha.md#harvester-of-souls) (1), [Cryptbreaker](../cards/C/cr.md#cryptbreaker) (1), [Falkenrath Noble](../cards/F/fa.md#falkenrath-noble) (1), [Diregraf Colossus](../cards/D/di.md#diregraf-colossus) (2), [Grapple with the Past](../cards/G/gra.md#grapple-with-the-past) (1), [Second Harvest](../cards/S/sec.md#second-harvest) (2), [Parallel Lives](../cards/P/pa.md#parallel-lives) (2), [Unnatural Growth](../cards/U/un.md#unnatural-growth) (1), [The Meathook Massacre](../cards/T/them.md#the-meathook-massacre) (1), [Exquisite Blood](../cards/E/ex.md#exquisite-blood) (2), [Cryptolith Rite](../cards/C/cr.md#cryptolith-rite) (1), [Descendants' Path](../cards/D/des.md#descendants-path) (3), [Endless Ranks of the Dead](../cards/E/en.md#endless-ranks-of-the-dead) (2), [Conjurer's Closet](../cards/C/con.md#conjurers-closet) (4), [Moonsilver Key](../cards/M/moo.md#moonsilver-key) (2), [Haunted Cloak](../cards/H/ha.md#haunted-cloak) (1), [Grafdigger's Cage](../cards/G/gra.md#grafdiggers-cage) (4), [Ghost Quarter](../cards/G/gh.md#ghost-quarter) (3), [Cavern of Souls](../cards/C/cav.md#cavern-of-souls) (4), [Voldaren Estate](../cards/V/vo.md#voldaren-estate) (4).
<!-- RULES-NOTES:END -->

<!-- COMBOS:START -->
## Combos (Commander Spellbook)

> Auto-generated 2026-10-15 by `scripts/detect_combos.py` from the [Commander Spellbook](https://commanderspellbook.com) public API (community-maintained combo database; each combo links to its page). Only combos whose **every card is in this list** are shown. Bracket note uses the official barometer: *Brackets 1–2 — no intentional two-card infinite combos; Bracket 3 — no early-game two-card infinite combos*.

**No complete combos found** (35 combos are one card away — not listed).
<!-- COMBOS:END -->
