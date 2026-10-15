---
title: "Card Enrichment"
category: cards
tags: [card-enrichment, lore, synergy, coverage, phase-8]
issues: [99, 100, 101, 102]
generated_by: scripts/build_card_enrichment.py
sources: [scryfall, wizards-story, spellbook, edhrec]
related: ["Characters Index.md", "Items & Artifacts Index.md", "EDH Packages.md", "Planes Index.md", "Planeswalker Dossiers.md", "Conflicts & Arcs.md"]
schema: 2
---

# Card Enrichment

> **Generated** by `scripts/build_card_enrichment.py` (Bot cycle 33, Phase 8 — [#99](https://github.com/corymstover/GrokBotMTGCompanion/issues/99) format, [#100](https://github.com/corymstover/GrokBotMTGCompanion/issues/100) lore, [#101](https://github.com/corymstover/GrokBotMTGCompanion/issues/101) synergy, [#102](https://github.com/corymstover/GrokBotMTGCompanion/issues/102) links + validation). Do not hand-edit; curated lore notes go in `data/card_lore_notes.json`. Machine copy: `data/card_enrichment.json`.
> Each enriched card entry gains a **Lore** line and a **Synergy** line, placed before *Referenced in*. They are pointers to existing KB entries, Scryfall fields, cached official pages and cited third-party data. They never repeat Oracle text or rulings, and they add no new facts.

## Contents
- [Lore line](#lore-line)
- [Synergy line](#synergy-line)
- [Coverage of the priority pool](#coverage-of-the-priority-pool)
- [Enriched cards](#enriched-cards)
- [By lore entry](#by-lore-entry)
- [By package](#by-package)
- [Synergy clusters](#synergy-clusters)

## Lore line
| Part | Meaning | Evidence |
|---|---|---|
| **Depicts** | the lore entry's own text links this card, and the card is that character or item (its name contains the entry's name) | official URLs on the entry line that links the card; *via entry* = the entry's own citations when that line has none |
| **Featured in** | the entry's text links the card in another context: a plane's notable cards, an arc beat, a retcon | same |
| ✅ **Story Spotlight** | a printing Wizards marked as depicting a story moment (Scryfall `story_spotlight`) | Scryfall default-cards bulk |
| ✅ **Flavor text verbatim on** | a printed flavor text that appears word for word on a cached official page | `.cache/story/` (Wizards pages) |
| *Depicts / References / Echoes:* note | curated note (`data/card_lore_notes.json`). *Echoes* = the card's mechanics mirror a cited story moment (guidance) | official sources listed in the note |
| (the entry line carries ⚠️/❓/🚫) | the lore-entry line that links the card has an uncertainty flag; read the entry before relying on the link | the entry |
| ⚠️ **Name match only** | the card's name matches a character entry (the generated *Character cards (name-matched)* tables). Not a claim about canon, timing or which version | Scryfall names |
| 🚫 | every paper printing is Universes Beyond (triangle security stamp), so it is outside the Multiverse story | Scryfall `security_stamp` |

## Synergy line
| Tier | Contents | Source |
|---|---|---|
| *Proven* | **KB decks** that run the card · **Commander Spellbook** combo count (Commander-legal variants) and the most popular one · **EDHREC as commander**: decks and highest-synergy cards · **EDHREC**: decks that run the card and the commanders it appears under most (share of that commander's decks) | repo decklists; [Commander Spellbook](https://commanderspellbook.com) API; [EDHREC](https://edhrec.com) JSON pages (community data, snapshot; cached in `.cache/`) |
| *Guidance (Oracle pattern)* | [EDH Packages](EDH%20Packages.md) sub-packages whose Oracle-text pattern the card matches: its archetype role | `scripts/build_packages.py` patterns |

EDHREC and Spellbook numbers are snapshots of community data, not rules or canon. A missing value means the source had no page for the card. *n+ combos* = the query returned its first 100 variants by popularity, so there are more.

## Coverage of the priority pool
Phase 8 priority order: legendary creatures, planeswalkers, story-significant cards (linked from lore entries or name-matched to characters), strong flavor-text cards (Story Spotlight, or flavor text quoted on a cached official page); then outward. A card can be in several tiers.

| Tier | Cards in the KB | Enriched | Coverage |
|---|---|---|---|
| entry-linked | 128 | 93 | 72.7% |
| character-card | 414 | 18 | 4.3% |
| legendary-creature | 3,786 | 62 | 1.6% |
| planeswalker | 338 | 11 | 3.3% |
| story-flavor | 396 | 3 | 0.8% |
| priority pool (any tier) | 4,549 | 93 | 2.0% |

Batches: Bot cycle 33 — legendary cards and planeswalkers already linked from lore entries.

## Enriched cards
| Card | Type | Lore relations | Evidence | Proven synergy | Guidance packages |
|---|---|---|---|---|---|
| [Agatha of the Vile Cauldron](cards/A/ag.md#agatha-of-the-vile-cauldron) | legendary creature | featured 1 | line citation | 100+ combos, EDHREC 23,168 | 0 |
| [Alrund, God of the Cosmos // Hakka, Whispering Raven](cards/A/al.md#alrund-god-of-the-cosmos--hakka-whispering-raven) | legendary creature | featured 1 | via entry | EDHREC 9,896 | 0 |
| [Aurelia, Exemplar of Justice](cards/A/au.md#aurelia-exemplar-of-justice) | legendary creature | featured 1 | via entry | 1 decks, EDHREC 15,617 | 0 |
| [Baron Sengir](cards/B/bar.md#baron-sengir) | legendary creature | featured 1 | via entry | EDHREC 743 | 0 |
| [Bident of Thassa](cards/B/bi.md#bident-of-thassa) | legendary artifact | featured 1 | line citation | 4 decks, EDHREC 286,833 | 1 |
| [Birgi, God of Storytelling // Harnfel, Horn of Bounty](cards/B/bi.md#birgi-god-of-storytelling--harnfel-horn-of-bounty) | legendary creature | featured 1 | via entry | 5 decks, 100+ combos, EDHREC 262,152 | 1 |
| [Blackblade Reforged](cards/B/bla.md#blackblade-reforged) | legendary artifact | depicts 1 | note | 2 decks, EDHREC 329,650 | 0 |
| [Borborygmos](cards/B/bo.md#borborygmos) | legendary creature | featured 1 | via entry | EDHREC 3,392 | 0 |
| [Bow of Nylea](cards/B/bo.md#bow-of-nylea) | legendary artifact | featured 1 | line citation | 1 decks, EDHREC 68,663 | 0 |
| [Brokkos, Apex of Forever](cards/B/br.md#brokkos-apex-of-forever) | legendary creature | featured 1 | via entry | 18 combos, EDHREC 15,331 | 0 |
| [Cosima, God of the Voyage // The Omenkeel](cards/C/cos.md#cosima-god-of-the-voyage--the-omenkeel) | legendary creature | featured 1 | via entry | EDHREC 28,306 | 1 |
| [Drana, Liberator of Malakir](cards/D/dra.md#drana-liberator-of-malakir) | legendary creature | featured 1 | line citation | 2 decks, EDHREC 105,348 | 0 |
| [Egon, God of Death // Throne of Death](cards/E/eg.md#egon-god-of-death--throne-of-death) | legendary creature | featured 1 | via entry | EDHREC 9,627 | 0 |
| [Eiganjo, Seat of the Empire](cards/E/ei.md#eiganjo-seat-of-the-empire) | legendary land | featured 1 | line citation | EDHREC 320,199 | 0 |
| [Elesh Norn, Mother of Machines](cards/E/el.md#elesh-norn-mother-of-machines) | legendary creature | featured 1, name-match 1 | via entry | 2 decks, 100+ combos, EDHREC 141,868 | 1 |
| [Eriette of the Charmed Apple](cards/E/er.md#eriette-of-the-charmed-apple) | legendary creature | featured 1 | line citation | EDHREC 23,176 | 0 |
| [Esika, God of the Tree // The Prismatic Bridge](cards/E/es.md#esika-god-of-the-tree--the-prismatic-bridge) | legendary creature | featured 1 | via entry | 59 combos, EDHREC 39,678 | 0 |
| [Falco Spara, Pactweaver](cards/F/fa.md#falco-spara-pactweaver) | legendary creature | featured 1 | via entry | 100+ combos, EDHREC 16,487 | 0 |
| [Gadwick, the Wizened](cards/G/ga.md#gadwick-the-wizened) | legendary creature | featured 1 | via entry | EDHREC 22,678 | 0 |
| [General Kudro of Drannith](cards/G/ge.md#general-kudro-of-drannith) | legendary creature | featured 1 | via entry | EDHREC 10,753 | 0 |
| [Glissa Sunslayer](cards/G/gl.md#glissa-sunslayer) | legendary creature | featured 1 | via entry | 1 decks, EDHREC 114,255 | 1 |
| [Godsend](cards/G/god.md#godsend) | legendary artifact | depicts 1 | note | EDHREC 18,640 | 0 |
| [Grandmother Sengir](cards/G/gra.md#grandmother-sengir) | legendary creature | featured 1 | via entry | EDHREC 213 | 0 |
| [Halvar, God of Battle // Sword of the Realms](cards/H/ha.md#halvar-god-of-battle--sword-of-the-realms) | legendary creature | featured 1 | via entry | 82 combos, EDHREC 68,646 | 0 |
| [Hammer of Purphoros](cards/H/ha.md#hammer-of-purphoros) | legendary artifact | featured 1 | line citation | 100+ combos, EDHREC 55,115 | 0 |
| [Helvault](cards/H/he.md#helvault) | legendary artifact | depicts 1 | note | 1 decks, 3 combos, EDHREC 1,495 | 0 |
| [Hidetsugu, Devouring Chaos](cards/H/hi.md#hidetsugu-devouring-chaos) | legendary creature | featured 1 | line citation | 10 combos, EDHREC 9,052 | 1 |
| [Hylda of the Icy Crown](cards/H/hy.md#hylda-of-the-icy-crown) | legendary creature | featured 1 | line citation | 18 combos, EDHREC 9,942 | 0 |
| [Illuna, Apex of Wishes](cards/I/il.md#illuna-apex-of-wishes) | legendary creature | featured 1 | via entry | 2 combos, EDHREC 8,875 | 0 |
| [Inga Rune-Eyes](cards/I/ing.md#inga-rune-eyes) | legendary creature | featured 1 | via entry | 4 combos, EDHREC 2,846 | 0 |
| [Jace, Vryn's Prodigy // Jace, Telepath Unbound](cards/J/ja.md#jace-vryns-prodigy--jace-telepath-unbound) | legendary creature | depicts 1, name-match 2 | line citation | EDHREC 22,313 | 0 |
| [Jetmir, Nexus of Revels](cards/J/je.md#jetmir-nexus-of-revels) | legendary creature | featured 1 | via entry | 15 combos, EDHREC 63,275 | 1 |
| [Jhoira, Ageless Innovator](cards/J/jh.md#jhoira-ageless-innovator) | legendary creature | featured 1 | line citation | 1 combos, EDHREC 9,113 | 0 |
| [Jin-Gitaxias, Progress Tyrant](cards/J/ji.md#jin-gitaxias-progress-tyrant) | legendary creature | featured 1, name-match 1 | via entry | 32 combos, EDHREC 92,823 | 0 |
| [Jorn, God of Winter // Kaldring, the Rimestaff](cards/J/jo.md#jorn-god-of-winter--kaldring-the-rimestaff) | legendary creature | featured 1 | via entry | 7 combos, EDHREC 1,502 | 0 |
| [Kaito Shizuki](cards/K/ka.md#kaito-shizuki) | planeswalker | featured 1, name-match 2 | line citation | EDHREC 24,394 | 0 |
| [Karn's Sylex](cards/K/ka.md#karns-sylex) | legendary artifact | featured 1 | line citation | 1 decks, 1 combos, EDHREC 7,022 | 0 |
| [Kellan, the Fae-Blooded // Birthright Boon](cards/K/ke.md#kellan-the-fae-blooded--birthright-boon) | legendary creature | featured 1, name-match 1 | line citation | EDHREC 49,006 | 1 |
| [Kinnan, Bonder Prodigy](cards/K/ki.md#kinnan-bonder-prodigy) | legendary creature | featured 1 | via entry | 100+ combos, EDHREC 95,521 | 0 |
| [Kolvori, God of Kinship // The Ringhart Crest](cards/K/ko.md#kolvori-god-of-kinship--the-ringhart-crest) | legendary creature | featured 1 | via entry | EDHREC 15,161 | 0 |
| [Koma, Cosmos Serpent](cards/K/ko.md#koma-cosmos-serpent) | legendary creature | featured 2 | via entry | 1 combos, EDHREC 103,177 | 0 |
| [Lavinia, Azorius Renegade](cards/L/la.md#lavinia-azorius-renegade) | legendary creature | featured 1 | via entry | 4 combos, EDHREC 48,580 | 0 |
| [Lazav, Familiar Stranger](cards/L/la.md#lazav-familiar-stranger) | legendary creature | featured 1 | via entry | EDHREC 6,339 | 0 |
| [Linden, the Steadfast Queen](cards/L/li.md#linden-the-steadfast-queen) | legendary creature | featured 1 | via entry | EDHREC 23,811 | 0 |
| [Linvala, the Preserver](cards/L/li.md#linvala-the-preserver) | legendary creature | featured 1 | line citation | EDHREC 6,204 | 0 |
| [Lithoform Engine](cards/L/li.md#lithoform-engine) | legendary artifact | featured 1 | Spotlight | 1 decks, 100+ combos, EDHREC 93,954 | 1 |
| [Lord Xander, the Collector](cards/L/lo.md#lord-xander-the-collector) | legendary creature | featured 1 | via entry | 1 decks, 5 combos, EDHREC 15,320 | 0 |
| [Lukka, Coppercoat Outcast](cards/L/lu.md#lukka-coppercoat-outcast) | planeswalker | featured 1, name-match 1 | via entry | EDHREC 8,005 | 0 |
| [Memnarch](cards/M/me.md#memnarch) | legendary creature | featured 1 | via entry | 79 combos, EDHREC 15,580 | 0 |
| [Nahiri, Heir of the Ancients](cards/N/na.md#nahiri-heir-of-the-ancients) | planeswalker | featured 1, name-match 2 | line citation | EDHREC 10,928 | 0 |
| [Nethroi, Apex of Death](cards/N/ne.md#nethroi-apex-of-death) | legendary creature | featured 1 | via entry | 32 combos, EDHREC 20,926 | 0 |
| [Niv-Mizzet Reborn](cards/N/ni.md#niv-mizzet-reborn) | legendary creature | featured 1, name-match 2 | Spotlight | EDHREC 10,004 | 0 |
| [Planar Bridge](cards/P/pl.md#planar-bridge) | legendary artifact | depicts 1 | via entry | 1 decks, 5 combos, EDHREC 35,848 | 0 |
| [Questing Beast](cards/Q/qu.md#questing-beast) | legendary creature | featured 1 | via entry | EDHREC 61,348 | 0 |
| [Radha, Coalition Warlord](cards/R/rad.md#radha-coalition-warlord) | legendary creature | featured 1 | line citation | EDHREC 2,548 | 0 |
| [Raffine, Scheming Seer](cards/R/raf.md#raffine-scheming-seer) | legendary creature | featured 1 | via entry | EDHREC 25,963 | 0 |
| [Rakdos, Lord of Riots](cards/R/rak.md#rakdos-lord-of-riots) | legendary creature | featured 1 | via entry | 2 decks, 100+ combos, EDHREC 52,077 | 1 |
| [Ral, Crackling Wit](cards/R/ral.md#ral-crackling-wit) | planeswalker | featured 1, name-match 2 | via entry | EDHREC 73,492 | 1 |
| [Rankle, Master of Pranks](cards/R/ran.md#rankle-master-of-pranks) | legendary creature | featured 1 | line citation | 1 decks, EDHREC 112,989 | 0 |
| [Realmbreaker, the Invasion Tree](cards/R/rea.md#realmbreaker-the-invasion-tree) | legendary artifact | depicts 1 | line citation | 5 combos, EDHREC 38,764 | 0 |
| [Reidane, God of the Worthy // Valkmira, Protector's Shield](cards/R/rei.md#reidane-god-of-the-worthy--valkmira-protectors-shield) | legendary creature | featured 1 | via entry | EDHREC 23,795 | 0 |
| [Risona, Asari Commander](cards/R/ri.md#risona-asari-commander) | legendary creature | featured 1 | line citation | EDHREC 5,901 | 0 |
| [Ruby, Daring Tracker](cards/R/ru.md#ruby-daring-tracker) | legendary creature | featured 1 | line citation | 10 combos, EDHREC 71,818 | 1 |
| [Sheoldred, the Apocalypse](cards/S/she.md#sheoldred-the-apocalypse) | legendary creature | featured 2, name-match 1 | line citation | 6 decks, 98+ combos, EDHREC 267,947 | 1 |
| [Snapdax, Apex of the Hunt](cards/S/sn.md#snapdax-apex-of-the-hunt) | legendary creature | featured 1 | via entry | EDHREC 5,054 | 0 |
| [Sothera, the Supervoid](cards/S/so.md#sothera-the-supervoid) | other legendary | featured 1 | via entry | EDHREC 32,688 | 0 |
| [Talion, the Kindly Lord](cards/T/ta.md#talion-the-kindly-lord) | legendary creature | featured 1 | line citation | EDHREC 86,552 | 1 |
| [Tergrid, God of Fright // Tergrid's Lantern](cards/T/te.md#tergrid-god-of-fright--tergrids-lantern) | legendary creature | featured 1 | via entry | 3 decks, 1 combos, EDHREC 90,388 | 0 |
| [Tezzeret, Betrayer of Flesh](cards/T/te.md#tezzeret-betrayer-of-flesh) | planeswalker | featured 1, name-match 2 | via entry | 64 combos, EDHREC 40,774 | 1 |
| [The Celestus](cards/T/thec.md#the-celestus) | legendary artifact | depicts 1 | Spotlight | 1 combos, EDHREC 24,547 | 0 |
| [The Chain Veil](cards/T/thec.md#the-chain-veil) | legendary artifact | depicts 1 | via entry | 1 decks, 88 combos, EDHREC 63,764 | 0 |
| [The Endstone](cards/T/thee.md#the-endstone) | legendary artifact | depicts 1 | line citation | EDHREC 52,611 | 1 |
| [The Immortal Sun](cards/T/thei.md#the-immortal-sun) | legendary artifact | depicts 1 | note | 1 decks, 100+ combos, EDHREC 62,765 | 2 |
| [The Mana Rig](cards/T/them.md#the-mana-rig) | legendary artifact | depicts 1 | via entry | EDHREC 3,482 | 0 |
| [The Mightstone and Weakstone](cards/T/them.md#the-mightstone-and-weakstone) | legendary artifact | depicts 1 | note | 2 decks, 8 combos, EDHREC 54,511 | 0 |
| [The Ozolith](cards/T/theo.md#the-ozolith) | legendary artifact | depicts 1, featured 1 | line citation | 3 decks, 76 combos, EDHREC 368,403 | 0 |
| [The Reality Chip](cards/T/ther.md#the-reality-chip) | legendary creature | depicts 1 | via entry | 1 decks, 100+ combos, EDHREC 144,431 | 0 |
| [Toralf, God of Fury // Toralf's Hammer](cards/T/to.md#toralf-god-of-fury--toralfs-hammer) | legendary creature | featured 1 | via entry | 28 combos, EDHREC 31,392 | 0 |
| [Toski, Bearer of Secrets](cards/T/to.md#toski-bearer-of-secrets) | legendary creature | featured 1 | via entry | 1 decks, EDHREC 311,458 | 1 |
| [Trostani, Three Whispers](cards/T/tro.md#trostani-three-whispers) | legendary creature | featured 1 | via entry | EDHREC 10,510 | 0 |
| [Tyvar Kell](cards/T/ty.md#tyvar-kell) | planeswalker | featured 1, name-match 1 | line citation | 1 decks, 6 combos, EDHREC 38,224 | 0 |
| [Urabrask // The Great Work](cards/U/ur.md#urabrask--the-great-work) | legendary creature | featured 1, name-match 1 | via entry | 86 combos, EDHREC 82,584 | 1 |
| [Vadrok, Apex of Thunder](cards/V/va.md#vadrok-apex-of-thunder) | legendary creature | featured 1 | via entry | 19 combos, EDHREC 5,314 | 0 |
| [Valki, God of Lies // Tibalt, Cosmic Impostor](cards/V/va.md#valki-god-of-lies--tibalt-cosmic-impostor) | legendary creature | featured 1 | via entry | 1 decks, 1 combos, EDHREC 23,232 | 0 |
| [Varragoth, Bloodsky Sire](cards/V/va.md#varragoth-bloodsky-sire) | legendary creature | featured 1 | via entry | 9 combos, EDHREC 81,357 | 0 |
| [Vivien Reid](cards/V/vi.md#vivien-reid) | planeswalker | featured 1, name-match 1 | line citation | EDHREC 40,605 | 1 |
| [Vivien, Monsters' Advocate](cards/V/vi.md#vivien-monsters-advocate) | planeswalker | featured 1, name-match 1 | via entry | 35 combos, EDHREC 23,455 | 0 |
| [Vorinclex, Monstrous Raider](cards/V/vo.md#vorinclex-monstrous-raider) | legendary creature | featured 1, name-match 1 | via entry | 2 decks, 100+ combos, EDHREC 123,004 | 0 |
| [Vraska, Golgari Queen](cards/V/vr.md#vraska-golgari-queen) | planeswalker | featured 1, name-match 2 | via entry | EDHREC 38,892 | 0 |
| [Whip of Erebos](cards/W/wh.md#whip-of-erebos) | legendary artifact | featured 1 | line citation | 1 decks, 2 combos, EDHREC 196,453 | 1 |
| [Winota, Joiner of Forces](cards/W/wi.md#winota-joiner-of-forces) | legendary creature | featured 1 | via entry | EDHREC 18,716 | 0 |
| [Yawgmoth, Thran Physician](cards/Y/ya.md#yawgmoth-thran-physician) | legendary creature | featured 1, name-match 1 | via entry | 1 decks, 100+ combos, EDHREC 168,100 | 1 |
| [Ziatora, the Incinerator](cards/Z/zi.md#ziatora-the-incinerator) | legendary creature | featured 1 | via entry | 1 decks, 13 combos, EDHREC 42,126 | 0 |

## By lore entry
Every lore entry named on an enriched card's Lore line, with the cards that name it. The entry links each card back in its own text (or, for name matches, in the *Character cards (name-matched)* table).

| Lore entry | Enriched cards |
|---|---|
| [Arc → Ikoria: Lair of Behemoths (2020)](Conflicts%20%26%20Arcs.md#ikoria-lair-of-behemoths-2020) | [General Kudro of Drannith](cards/G/ge.md#general-kudro-of-drannith) (featured) · [Lukka, Coppercoat Outcast](cards/L/lu.md#lukka-coppercoat-outcast) (featured) · [The Ozolith](cards/T/theo.md#the-ozolith) (featured) · [Vivien, Monsters' Advocate](cards/V/vi.md#vivien-monsters-advocate) (featured) |
| [Character → Elesh Norn](Characters%20Index.md#elesh-norn) | [Elesh Norn, Mother of Machines](cards/E/el.md#elesh-norn-mother-of-machines) (name-match) |
| [Character → Jace Beleren](Characters%20Index.md#jace-beleren) | [Jace, Vryn's Prodigy // Jace, Telepath Unbound](cards/J/ja.md#jace-vryns-prodigy--jace-telepath-unbound) (name-match) |
| [Character → Jin-Gitaxias](Characters%20Index.md#jin-gitaxias) | [Jin-Gitaxias, Progress Tyrant](cards/J/ji.md#jin-gitaxias-progress-tyrant) (name-match) |
| [Character → Kaito Shizuki](Characters%20Index.md#kaito-shizuki) | [Kaito Shizuki](cards/K/ka.md#kaito-shizuki) (name-match) |
| [Character → Kellan](Characters%20Index.md#kellan) | [Kellan, the Fae-Blooded // Birthright Boon](cards/K/ke.md#kellan-the-fae-blooded--birthright-boon) (name-match) |
| [Character → Lukka](Characters%20Index.md#lukka) | [Lukka, Coppercoat Outcast](cards/L/lu.md#lukka-coppercoat-outcast) (name-match) |
| [Character → Nahiri](Characters%20Index.md#nahiri) | [Nahiri, Heir of the Ancients](cards/N/na.md#nahiri-heir-of-the-ancients) (name-match) |
| [Character → Proft, Etrata, Aminatou, Niv-Mizzet](Characters%20Index.md#proft-etrata-aminatou-niv-mizzet) | [Niv-Mizzet Reborn](cards/N/ni.md#niv-mizzet-reborn) (name-match) |
| [Character → Ral Zarek](Characters%20Index.md#ral-zarek) | [Ral, Crackling Wit](cards/R/ral.md#ral-crackling-wit) (name-match) |
| [Character → Sheoldred](Characters%20Index.md#sheoldred) | [Sheoldred, the Apocalypse](cards/S/she.md#sheoldred-the-apocalypse) (name-match) |
| [Character → Tezzeret](Characters%20Index.md#tezzeret) | [Tezzeret, Betrayer of Flesh](cards/T/te.md#tezzeret-betrayer-of-flesh) (name-match) |
| [Character → Tyvar Kell](Characters%20Index.md#tyvar-kell) | [Tyvar Kell](cards/T/ty.md#tyvar-kell) (name-match) |
| [Character → Urabrask](Characters%20Index.md#urabrask) | [Urabrask // The Great Work](cards/U/ur.md#urabrask--the-great-work) (name-match) |
| [Character → Vivien Reid](Characters%20Index.md#vivien-reid) | [Vivien Reid](cards/V/vi.md#vivien-reid) (name-match) · [Vivien, Monsters' Advocate](cards/V/vi.md#vivien-monsters-advocate) (name-match) |
| [Character → Vorinclex](Characters%20Index.md#vorinclex) | [Vorinclex, Monstrous Raider](cards/V/vo.md#vorinclex-monstrous-raider) (name-match) |
| [Character → Vraska](Characters%20Index.md#vraska) | [Vraska, Golgari Queen](cards/V/vr.md#vraska-golgari-queen) (name-match) |
| [Character → Yawgmoth](Characters%20Index.md#yawgmoth) | [Yawgmoth, Thran Physician](cards/Y/ya.md#yawgmoth-thran-physician) (name-match) |
| [Dossier → Jace Beleren](Planeswalker%20Dossiers.md#jace-beleren) | [Jace, Vryn's Prodigy // Jace, Telepath Unbound](cards/J/ja.md#jace-vryns-prodigy--jace-telepath-unbound) (name-match) |
| [Dossier → Kaito Shizuki](Planeswalker%20Dossiers.md#kaito-shizuki) | [Kaito Shizuki](cards/K/ka.md#kaito-shizuki) (name-match) |
| [Dossier → Nahiri](Planeswalker%20Dossiers.md#nahiri) | [Nahiri, Heir of the Ancients](cards/N/na.md#nahiri-heir-of-the-ancients) (name-match) |
| [Dossier → Niv-Mizzet](Planeswalker%20Dossiers.md#niv-mizzet) | [Niv-Mizzet Reborn](cards/N/ni.md#niv-mizzet-reborn) (name-match) |
| [Dossier → Ral Zarek](Planeswalker%20Dossiers.md#ral-zarek) | [Ral, Crackling Wit](cards/R/ral.md#ral-crackling-wit) (name-match) |
| [Dossier → Tezzeret](Planeswalker%20Dossiers.md#tezzeret) | [Tezzeret, Betrayer of Flesh](cards/T/te.md#tezzeret-betrayer-of-flesh) (name-match) |
| [Dossier → Vraska](Planeswalker%20Dossiers.md#vraska) | [Vraska, Golgari Queen](cards/V/vr.md#vraska-golgari-queen) (name-match) |
| [Item → Blackblade](Items%20%26%20Artifacts%20Index.md#blackblade) | [Blackblade Reforged](cards/B/bla.md#blackblade-reforged) (depicts) |
| [Item → Celestus, Sungold Lock & Moonsilver Key](Items%20%26%20Artifacts%20Index.md#celestus-sungold-lock--moonsilver-key) | [The Celestus](cards/T/thec.md#the-celestus) (depicts) |
| [Item → Chain Veil](Items%20%26%20Artifacts%20Index.md#chain-veil) | [The Chain Veil](cards/T/thec.md#the-chain-veil) (depicts) |
| [Item → Endstone](Items%20%26%20Artifacts%20Index.md#endstone) | [The Endstone](cards/T/thee.md#the-endstone) (depicts) |
| [Item → Godsend & Khrusor](Items%20%26%20Artifacts%20Index.md#godsend--khrusor) | [Godsend](cards/G/god.md#godsend) (depicts) |
| [Item → Golgothian Sylex](Items%20%26%20Artifacts%20Index.md#golgothian-sylex) | [Karn's Sylex](cards/K/ka.md#karns-sylex) (featured) |
| [Item → Helvault](Items%20%26%20Artifacts%20Index.md#helvault) | [Helvault](cards/H/he.md#helvault) (depicts) |
| [Item → Immortal Sun](Items%20%26%20Artifacts%20Index.md#immortal-sun) | [The Immortal Sun](cards/T/thei.md#the-immortal-sun) (depicts) |
| [Item → Lithoform Core](Items%20%26%20Artifacts%20Index.md#lithoform-core) | [Lithoform Engine](cards/L/li.md#lithoform-engine) (featured) |
| [Item → Mana Rig, powerstones & Thran steel (DMU)](Items%20%26%20Artifacts%20Index.md#mana-rig-powerstones--thran-steel-dmu) | [The Mana Rig](cards/T/them.md#the-mana-rig) (depicts) |
| [Item → Mightstone & Weakstone](Items%20%26%20Artifacts%20Index.md#mightstone--weakstone) | [The Mightstone and Weakstone](cards/T/them.md#the-mightstone-and-weakstone) (depicts) |
| [Item → Ozolith](Items%20%26%20Artifacts%20Index.md#ozolith) | [The Ozolith](cards/T/theo.md#the-ozolith) (depicts) |
| [Item → Planar Bridge](Items%20%26%20Artifacts%20Index.md#planar-bridge) | [Planar Bridge](cards/P/pl.md#planar-bridge) (depicts) |
| [Item → Reality Chip](Items%20%26%20Artifacts%20Index.md#reality-chip) | [The Reality Chip](cards/T/ther.md#the-reality-chip) (depicts) |
| [Item → Realmbreaker, the Invasion Tree](Items%20%26%20Artifacts%20Index.md#realmbreaker-the-invasion-tree) | [Realmbreaker, the Invasion Tree](cards/R/rea.md#realmbreaker-the-invasion-tree) (depicts) |
| [Item → Theros god weapons](Items%20%26%20Artifacts%20Index.md#theros-god-weapons) | [Bident of Thassa](cards/B/bi.md#bident-of-thassa) (featured) · [Bow of Nylea](cards/B/bo.md#bow-of-nylea) (featured) · [Hammer of Purphoros](cards/H/ha.md#hammer-of-purphoros) (featured) · [Whip of Erebos](cards/W/wh.md#whip-of-erebos) (featured) |
| [Item → World Tree & the Sword of the Realms (Kaldheim)](Items%20%26%20Artifacts%20Index.md#world-tree--the-sword-of-the-realms-kaldheim) | [Koma, Cosmos Serpent](cards/K/ko.md#koma-cosmos-serpent) (featured) |
| [Plane → Dominaria (Dominaria United era)](Planes%20Index.md#dominaria-dominaria-united-era) | [Jhoira, Ageless Innovator](cards/J/jh.md#jhoira-ageless-innovator) (featured) · [Radha, Coalition Warlord](cards/R/rad.md#radha-coalition-warlord) (featured) · [Sheoldred, the Apocalypse](cards/S/she.md#sheoldred-the-apocalypse) (featured) |
| [Plane → Eldraine](Planes%20Index.md#eldraine) | [Agatha of the Vile Cauldron](cards/A/ag.md#agatha-of-the-vile-cauldron) (featured) · [Eriette of the Charmed Apple](cards/E/er.md#eriette-of-the-charmed-apple) (featured) · [Gadwick, the Wizened](cards/G/ga.md#gadwick-the-wizened) (featured) · [Hylda of the Icy Crown](cards/H/hy.md#hylda-of-the-icy-crown) (featured) · [Kellan, the Fae-Blooded // Birthright Boon](cards/K/ke.md#kellan-the-fae-blooded--birthright-boon) (featured) · [Linden, the Steadfast Queen](cards/L/li.md#linden-the-steadfast-queen) (featured) · [Questing Beast](cards/Q/qu.md#questing-beast) (featured) · [Rankle, Master of Pranks](cards/R/ran.md#rankle-master-of-pranks) (featured) · [Ruby, Daring Tracker](cards/R/ru.md#ruby-daring-tracker) (featured) · [Talion, the Kindly Lord](cards/T/ta.md#talion-the-kindly-lord) (featured) |
| [Plane → Ikoria](Planes%20Index.md#ikoria) | [Brokkos, Apex of Forever](cards/B/br.md#brokkos-apex-of-forever) (featured) · [Illuna, Apex of Wishes](cards/I/il.md#illuna-apex-of-wishes) (featured) · [Kinnan, Bonder Prodigy](cards/K/ki.md#kinnan-bonder-prodigy) (featured) · [Nethroi, Apex of Death](cards/N/ne.md#nethroi-apex-of-death) (featured) · [Snapdax, Apex of the Hunt](cards/S/sn.md#snapdax-apex-of-the-hunt) (featured) · [Vadrok, Apex of Thunder](cards/V/va.md#vadrok-apex-of-thunder) (featured) · [Winota, Joiner of Forces](cards/W/wi.md#winota-joiner-of-forces) (featured) |
| [Plane → Kaldheim](Planes%20Index.md#kaldheim) | [Alrund, God of the Cosmos // Hakka, Whispering Raven](cards/A/al.md#alrund-god-of-the-cosmos--hakka-whispering-raven) (featured) · [Birgi, God of Storytelling // Harnfel, Horn of Bounty](cards/B/bi.md#birgi-god-of-storytelling--harnfel-horn-of-bounty) (featured) · [Cosima, God of the Voyage // The Omenkeel](cards/C/cos.md#cosima-god-of-the-voyage--the-omenkeel) (featured) · [Egon, God of Death // Throne of Death](cards/E/eg.md#egon-god-of-death--throne-of-death) (featured) · [Esika, God of the Tree // The Prismatic Bridge](cards/E/es.md#esika-god-of-the-tree--the-prismatic-bridge) (featured) · [Halvar, God of Battle // Sword of the Realms](cards/H/ha.md#halvar-god-of-battle--sword-of-the-realms) (featured) · [Inga Rune-Eyes](cards/I/ing.md#inga-rune-eyes) (featured) · [Jorn, God of Winter // Kaldring, the Rimestaff](cards/J/jo.md#jorn-god-of-winter--kaldring-the-rimestaff) (featured) · [Kolvori, God of Kinship // The Ringhart Crest](cards/K/ko.md#kolvori-god-of-kinship--the-ringhart-crest) (featured) · [Koma, Cosmos Serpent](cards/K/ko.md#koma-cosmos-serpent) (featured) · [Reidane, God of the Worthy // Valkmira, Protector's Shield](cards/R/rei.md#reidane-god-of-the-worthy--valkmira-protectors-shield) (featured) · [Tergrid, God of Fright // Tergrid's Lantern](cards/T/te.md#tergrid-god-of-fright--tergrids-lantern) (featured) · [Toralf, God of Fury // Toralf's Hammer](cards/T/to.md#toralf-god-of-fury--toralfs-hammer) (featured) · [Toski, Bearer of Secrets](cards/T/to.md#toski-bearer-of-secrets) (featured) · [Tyvar Kell](cards/T/ty.md#tyvar-kell) (featured) · [Valki, God of Lies // Tibalt, Cosmic Impostor](cards/V/va.md#valki-god-of-lies--tibalt-cosmic-impostor) (featured) · [Varragoth, Bloodsky Sire](cards/V/va.md#varragoth-bloodsky-sire) (featured) |
| [Plane → Kamigawa (Neon Dynasty era)](Planes%20Index.md#kamigawa-neon-dynasty-era) | [Eiganjo, Seat of the Empire](cards/E/ei.md#eiganjo-seat-of-the-empire) (featured) · [Hidetsugu, Devouring Chaos](cards/H/hi.md#hidetsugu-devouring-chaos) (featured) · [Kaito Shizuki](cards/K/ka.md#kaito-shizuki) (featured) · [Risona, Asari Commander](cards/R/ri.md#risona-asari-commander) (featured) |
| [Plane → New Capenna](Planes%20Index.md#new-capenna) | [Falco Spara, Pactweaver](cards/F/fa.md#falco-spara-pactweaver) (featured) · [Jetmir, Nexus of Revels](cards/J/je.md#jetmir-nexus-of-revels) (featured) · [Lord Xander, the Collector](cards/L/lo.md#lord-xander-the-collector) (featured) · [Raffine, Scheming Seer](cards/R/raf.md#raffine-scheming-seer) (featured) · [Ziatora, the Incinerator](cards/Z/zi.md#ziatora-the-incinerator) (featured) |
| [Plane → Phyrexia (Old Phyrexia) & New Phyrexia's spheres](Planes%20Index.md#phyrexia-old-phyrexia--new-phyrexias-spheres) | [Elesh Norn, Mother of Machines](cards/E/el.md#elesh-norn-mother-of-machines) (featured) · [Glissa Sunslayer](cards/G/gl.md#glissa-sunslayer) (featured) · [Jin-Gitaxias, Progress Tyrant](cards/J/ji.md#jin-gitaxias-progress-tyrant) (featured) · [Memnarch](cards/M/me.md#memnarch) (featured) · [Sheoldred, the Apocalypse](cards/S/she.md#sheoldred-the-apocalypse) (featured) · [Tezzeret, Betrayer of Flesh](cards/T/te.md#tezzeret-betrayer-of-flesh) (featured) · [Urabrask // The Great Work](cards/U/ur.md#urabrask--the-great-work) (featured) · [Vorinclex, Monstrous Raider](cards/V/vo.md#vorinclex-monstrous-raider) (featured) · [Yawgmoth, Thran Physician](cards/Y/ya.md#yawgmoth-thran-physician) (featured) |
| [Plane → Ravnica after the invasion (Murders at Karlov Manor)](Planes%20Index.md#ravnica-after-the-invasion-murders-at-karlov-manor) | [Aurelia, Exemplar of Justice](cards/A/au.md#aurelia-exemplar-of-justice) (featured) · [Borborygmos](cards/B/bo.md#borborygmos) (featured) · [Lavinia, Azorius Renegade](cards/L/la.md#lavinia-azorius-renegade) (featured) · [Lazav, Familiar Stranger](cards/L/la.md#lazav-familiar-stranger) (featured) · [Niv-Mizzet Reborn](cards/N/ni.md#niv-mizzet-reborn) (featured) · [Rakdos, Lord of Riots](cards/R/rak.md#rakdos-lord-of-riots) (featured) · [Ral, Crackling Wit](cards/R/ral.md#ral-crackling-wit) (featured) · [Trostani, Three Whispers](cards/T/tro.md#trostani-three-whispers) (featured) · [Vraska, Golgari Queen](cards/V/vr.md#vraska-golgari-queen) (featured) |
| [Plane → Skalla](Planes%20Index.md#skalla) | [Vivien Reid](cards/V/vi.md#vivien-reid) (featured) |
| [Plane → Sothera system (the Edge)](Planes%20Index.md#sothera-system-the-edge) | [Sothera, the Supervoid](cards/S/so.md#sothera-the-supervoid) (featured) |
| [Plane → Ulgrotha](Planes%20Index.md#ulgrotha) | [Baron Sengir](cards/B/bar.md#baron-sengir) (featured) · [Grandmother Sengir](cards/G/gra.md#grandmother-sengir) (featured) |
| [Plane → Vryn](Planes%20Index.md#vryn) | [Jace, Vryn's Prodigy // Jace, Telepath Unbound](cards/J/ja.md#jace-vryns-prodigy--jace-telepath-unbound) (depicts) |
| [Plane → Zendikar (Zendikar Rising era)](Planes%20Index.md#zendikar-zendikar-rising-era) | [Drana, Liberator of Malakir](cards/D/dra.md#drana-liberator-of-malakir) (featured) · [Linvala, the Preserver](cards/L/li.md#linvala-the-preserver) (featured) · [Nahiri, Heir of the Ancients](cards/N/na.md#nahiri-heir-of-the-ancients) (featured) |

## By package
Guidance tier: the [EDH Packages](EDH%20Packages.md) sub-packages named on enriched cards' Synergy lines (Oracle-pattern matches).

| Package | Enriched cards |
|---|---|
| [Card advantage: Repeatable draw engines (permanents)](EDH%20Packages.md#card-advantage-repeatable-draw-engines-permanents) | [Bident of Thassa](cards/B/bi.md#bident-of-thassa) · [Glissa Sunslayer](cards/G/gl.md#glissa-sunslayer) · [Sheoldred, the Apocalypse](cards/S/she.md#sheoldred-the-apocalypse) · [Talion, the Kindly Lord](cards/T/ta.md#talion-the-kindly-lord) · [Tezzeret, Betrayer of Flesh](cards/T/te.md#tezzeret-betrayer-of-flesh) · [The Endstone](cards/T/thee.md#the-endstone) · [Toski, Bearer of Secrets](cards/T/to.md#toski-bearer-of-secrets) |
| [Tokens: Anthems](EDH%20Packages.md#tokens-anthems) | [Jetmir, Nexus of Revels](cards/J/je.md#jetmir-nexus-of-revels) · [Kellan, the Fae-Blooded // Birthright Boon](cards/K/ke.md#kellan-the-fae-blooded--birthright-boon) · [The Immortal Sun](cards/T/thei.md#the-immortal-sun) · [Vivien Reid](cards/V/vi.md#vivien-reid) |
| [Card advantage: Impulse / exile-to-play](EDH%20Packages.md#card-advantage-impulse--exile-to-play) | [Birgi, God of Storytelling // Harnfel, Horn of Bounty](cards/B/bi.md#birgi-god-of-storytelling--harnfel-horn-of-bounty) · [Hidetsugu, Devouring Chaos](cards/H/hi.md#hidetsugu-devouring-chaos) |
| [Ramp: Cost reducers](EDH%20Packages.md#ramp-cost-reducers) | [Rakdos, Lord of Riots](cards/R/rak.md#rakdos-lord-of-riots) · [The Immortal Sun](cards/T/thei.md#the-immortal-sun) |
| [Spellslinger: Cast-trigger payoffs](EDH%20Packages.md#spellslinger-cast-trigger-payoffs) | [Ral, Crackling Wit](cards/R/ral.md#ral-crackling-wit) · [Urabrask // The Great Work](cards/U/ur.md#urabrask--the-great-work) |
| [+1/+1 counters: Proliferate](EDH%20Packages.md#11-counters-proliferate) | [Yawgmoth, Thran Physician](cards/Y/ya.md#yawgmoth-thran-physician) |
| [Blink: ETB doublers](EDH%20Packages.md#blink-etb-doublers) | [Elesh Norn, Mother of Machines](cards/E/el.md#elesh-norn-mother-of-machines) |
| [Graveyard: Reanimation](EDH%20Packages.md#graveyard-reanimation) | [Whip of Erebos](cards/W/wh.md#whip-of-erebos) |
| [Lands / landfall: Landfall payoffs](EDH%20Packages.md#lands--landfall-landfall-payoffs) | [Cosima, God of the Voyage // The Omenkeel](cards/C/cos.md#cosima-god-of-the-voyage--the-omenkeel) |
| [Ramp: Mana creatures (MV ≤ 2)](EDH%20Packages.md#ramp-mana-creatures-mv--2) | [Ruby, Daring Tracker](cards/R/ru.md#ruby-daring-tracker) |
| [Spellslinger: Spell copiers](EDH%20Packages.md#spellslinger-spell-copiers) | [Lithoform Engine](cards/L/li.md#lithoform-engine) |

## Synergy clusters
Commanders (EDHREC) under which two or more enriched cards appear most often: proven co-occurrence, not a recommendation.

| Commander | Enriched cards it runs most |
|---|---|
| Esika, God of the Tree | [Alrund, God of the Cosmos // Hakka, Whispering Raven](cards/A/al.md#alrund-god-of-the-cosmos--hakka-whispering-raven) · [Egon, God of Death // Throne of Death](cards/E/eg.md#egon-god-of-death--throne-of-death) · [Jorn, God of Winter // Kaldring, the Rimestaff](cards/J/jo.md#jorn-god-of-winter--kaldring-the-rimestaff) · [Kolvori, God of Kinship // The Ringhart Crest](cards/K/ko.md#kolvori-god-of-kinship--the-ringhart-crest) · [Reidane, God of the Worthy // Valkmira, Protector's Shield](cards/R/rei.md#reidane-god-of-the-worthy--valkmira-protectors-shield) · [The Chain Veil](cards/T/thec.md#the-chain-veil) · [Valki, God of Lies // Tibalt, Cosmic Impostor](cards/V/va.md#valki-god-of-lies--tibalt-cosmic-impostor) · [Vorinclex, Monstrous Raider](cards/V/vo.md#vorinclex-monstrous-raider) |
| [Jodah, the Unifier](cards/J/jo.md#jodah-the-unifier) | [Esika, God of the Tree // The Prismatic Bridge](cards/E/es.md#esika-god-of-the-tree--the-prismatic-bridge) · [Jorn, God of Winter // Kaldring, the Rimestaff](cards/J/jo.md#jorn-god-of-winter--kaldring-the-rimestaff) · [Kolvori, God of Kinship // The Ringhart Crest](cards/K/ko.md#kolvori-god-of-kinship--the-ringhart-crest) · [Radha, Coalition Warlord](cards/R/rad.md#radha-coalition-warlord) · [The Celestus](cards/T/thec.md#the-celestus) · [Toski, Bearer of Secrets](cards/T/to.md#toski-bearer-of-secrets) · [Winota, Joiner of Forces](cards/W/wi.md#winota-joiner-of-forces) |
| [Be'lakor, the Dark Master](cards/B/be.md#belakor-the-dark-master) | [Hidetsugu, Devouring Chaos](cards/H/hi.md#hidetsugu-devouring-chaos) · [Lord Xander, the Collector](cards/L/lo.md#lord-xander-the-collector) · [Rakdos, Lord of Riots](cards/R/rak.md#rakdos-lord-of-riots) · [Varragoth, Bloodsky Sire](cards/V/va.md#varragoth-bloodsky-sire) · [Whip of Erebos](cards/W/wh.md#whip-of-erebos) |
| [Cloud, Ex-SOLDIER](cards/C/cl.md#cloud-ex-soldier) | [Blackblade Reforged](cards/B/bla.md#blackblade-reforged) · [Godsend](cards/G/god.md#godsend) · [Halvar, God of Battle // Sword of the Realms](cards/H/ha.md#halvar-god-of-battle--sword-of-the-realms) · [Kellan, the Fae-Blooded // Birthright Boon](cards/K/ke.md#kellan-the-fae-blooded--birthright-boon) · [Nahiri, Heir of the Ancients](cards/N/na.md#nahiri-heir-of-the-ancients) |
| [Ramos, Dragon Engine](cards/R/ram.md#ramos-dragon-engine) | [Brokkos, Apex of Forever](cards/B/br.md#brokkos-apex-of-forever) · [Illuna, Apex of Wishes](cards/I/il.md#illuna-apex-of-wishes) · [Nethroi, Apex of Death](cards/N/ne.md#nethroi-apex-of-death) · [Snapdax, Apex of the Hunt](cards/S/sn.md#snapdax-apex-of-the-hunt) · [Vadrok, Apex of Thunder](cards/V/va.md#vadrok-apex-of-thunder) |
| Atreus, Impulsive Son // Kratos, Stoic Father | [Alrund, God of the Cosmos // Hakka, Whispering Raven](cards/A/al.md#alrund-god-of-the-cosmos--hakka-whispering-raven) · [Cosima, God of the Voyage // The Omenkeel](cards/C/cos.md#cosima-god-of-the-voyage--the-omenkeel) · [Reidane, God of the Worthy // Valkmira, Protector's Shield](cards/R/rei.md#reidane-god-of-the-worthy--valkmira-protectors-shield) · [Toralf, God of Fury // Toralf's Hammer](cards/T/to.md#toralf-god-of-fury--toralfs-hammer) |
| [Kaalia of the Vast](cards/K/ka.md#kaalia-of-the-vast) | [Aurelia, Exemplar of Justice](cards/A/au.md#aurelia-exemplar-of-justice) · [Linvala, the Preserver](cards/L/li.md#linvala-the-preserver) · [Rakdos, Lord of Riots](cards/R/rak.md#rakdos-lord-of-riots) · [Varragoth, Bloodsky Sire](cards/V/va.md#varragoth-bloodsky-sire) |
| [Omnath, Locus of All](cards/O/om.md#omnath-locus-of-all) | [Illuna, Apex of Wishes](cards/I/il.md#illuna-apex-of-wishes) · [Realmbreaker, the Invasion Tree](cards/R/rea.md#realmbreaker-the-invasion-tree) · [Snapdax, Apex of the Hunt](cards/S/sn.md#snapdax-apex-of-the-hunt) · [Vadrok, Apex of Thunder](cards/V/va.md#vadrok-apex-of-thunder) |
| [Sisay, Weatherlight Captain](cards/S/si.md#sisay-weatherlight-captain) | [Esika, God of the Tree // The Prismatic Bridge](cards/E/es.md#esika-god-of-the-tree--the-prismatic-bridge) · [Kinnan, Bonder Prodigy](cards/K/ki.md#kinnan-bonder-prodigy) · [Lavinia, Azorius Renegade](cards/L/la.md#lavinia-azorius-renegade) · [Ruby, Daring Tracker](cards/R/ru.md#ruby-daring-tracker) |
| [Zhulodok, Void Gorger](cards/Z/zh.md#zhulodok-void-gorger) | [Karn's Sylex](cards/K/ka.md#karns-sylex) · [Planar Bridge](cards/P/pl.md#planar-bridge) · [The Endstone](cards/T/thee.md#the-endstone) · [The Immortal Sun](cards/T/thei.md#the-immortal-sun) |
| [Breya, Etherium Shaper](cards/B/br.md#breya-etherium-shaper) | [Jhoira, Ageless Innovator](cards/J/jh.md#jhoira-ageless-innovator) · [Memnarch](cards/M/me.md#memnarch) · [Tezzeret, Betrayer of Flesh](cards/T/te.md#tezzeret-betrayer-of-flesh) |
| [Edgar Markov](cards/E/ed.md#edgar-markov) | [Baron Sengir](cards/B/bar.md#baron-sengir) · [Drana, Liberator of Malakir](cards/D/dra.md#drana-liberator-of-malakir) · [Helvault](cards/H/he.md#helvault) |
| [Fynn, the Fangbearer](cards/F/fy.md#fynn-the-fangbearer) | [Bow of Nylea](cards/B/bo.md#bow-of-nylea) · [Questing Beast](cards/Q/qu.md#questing-beast) · [Vorinclex, Monstrous Raider](cards/V/vo.md#vorinclex-monstrous-raider) |
| [Grand Arbiter Augustin IV](cards/G/gra.md#grand-arbiter-augustin-iv) | [Jin-Gitaxias, Progress Tyrant](cards/J/ji.md#jin-gitaxias-progress-tyrant) · [Lavinia, Azorius Renegade](cards/L/la.md#lavinia-azorius-renegade) · [Reidane, God of the Worthy // Valkmira, Protector's Shield](cards/R/rei.md#reidane-god-of-the-worthy--valkmira-protectors-shield) |
| [Hashaton, Scarab's Fist](cards/H/ha.md#hashaton-scarabs-fist) | [Jace, Vryn's Prodigy // Jace, Telepath Unbound](cards/J/ja.md#jace-vryns-prodigy--jace-telepath-unbound) · [Jin-Gitaxias, Progress Tyrant](cards/J/ji.md#jin-gitaxias-progress-tyrant) · [Raffine, Scheming Seer](cards/R/raf.md#raffine-scheming-seer) |
| [Isshin, Two Heavens as One](cards/I/is.md#isshin-two-heavens-as-one) | [Eiganjo, Seat of the Empire](cards/E/ei.md#eiganjo-seat-of-the-empire) · [Risona, Asari Commander](cards/R/ri.md#risona-asari-commander) · [Winota, Joiner of Forces](cards/W/wi.md#winota-joiner-of-forces) |
| [Alela, Cunning Conqueror](cards/A/al.md#alela-cunning-conqueror) | [Rankle, Master of Pranks](cards/R/ran.md#rankle-master-of-pranks) · [Talion, the Kindly Lord](cards/T/ta.md#talion-the-kindly-lord) |
| Ardenn, Intrepid Archaeologist // Rograkh, Son of Rohgahh | [Kellan, the Fae-Blooded // Birthright Boon](cards/K/ke.md#kellan-the-fae-blooded--birthright-boon) · [Nahiri, Heir of the Ancients](cards/N/na.md#nahiri-heir-of-the-ancients) |
| [Atraxa, Praetors' Voice](cards/A/at.md#atraxa-praetors-voice) | [The Chain Veil](cards/T/thec.md#the-chain-veil) · [Vorinclex, Monstrous Raider](cards/V/vo.md#vorinclex-monstrous-raider) |
| [Auntie Ool, Cursewretch](cards/A/au.md#auntie-ool-cursewretch) | [Glissa Sunslayer](cards/G/gl.md#glissa-sunslayer) · [Yawgmoth, Thran Physician](cards/Y/ya.md#yawgmoth-thran-physician) |
| [Brago, King Eternal](cards/B/br.md#brago-king-eternal) | [Elesh Norn, Mother of Machines](cards/E/el.md#elesh-norn-mother-of-machines) · [Lithoform Engine](cards/L/li.md#lithoform-engine) |
| [Captain America, First Avenger](cards/C/cap.md#captain-america-first-avenger) | [Halvar, God of Battle // Sword of the Realms](cards/H/ha.md#halvar-god-of-battle--sword-of-the-realms) · [Kellan, the Fae-Blooded // Birthright Boon](cards/K/ke.md#kellan-the-fae-blooded--birthright-boon) |
| [Carth the Lion](cards/C/car.md#carth-the-lion) | [Vivien Reid](cards/V/vi.md#vivien-reid) · [Vraska, Golgari Queen](cards/V/vr.md#vraska-golgari-queen) |
| [Cromat](cards/C/cr.md#cromat) | [Snapdax, Apex of the Hunt](cards/S/sn.md#snapdax-apex-of-the-hunt) · [Vadrok, Apex of Thunder](cards/V/va.md#vadrok-apex-of-thunder) |
| [General Ferrous Rokiric](cards/G/ge.md#general-ferrous-rokiric) | [Aurelia, Exemplar of Justice](cards/A/au.md#aurelia-exemplar-of-justice) · [The Mana Rig](cards/T/them.md#the-mana-rig) |
| [Giada, Font of Hope](cards/G/gi.md#giada-font-of-hope) | [Eiganjo, Seat of the Empire](cards/E/ei.md#eiganjo-seat-of-the-empire) · [Linvala, the Preserver](cards/L/li.md#linvala-the-preserver) |
| [Helga, Skittish Seer](cards/H/he.md#helga-skittish-seer) | [Falco Spara, Pactweaver](cards/F/fa.md#falco-spara-pactweaver) · [Koma, Cosmos Serpent](cards/K/ko.md#koma-cosmos-serpent) |
| [High Perfect Morcant](cards/H/hi.md#high-perfect-morcant) | [Glissa Sunslayer](cards/G/gl.md#glissa-sunslayer) · [Tyvar Kell](cards/T/ty.md#tyvar-kell) |
| [Illuna, Apex of Wishes](cards/I/il.md#illuna-apex-of-wishes) | [Lukka, Coppercoat Outcast](cards/L/lu.md#lukka-coppercoat-outcast) · [Vivien, Monsters' Advocate](cards/V/vi.md#vivien-monsters-advocate) |
| [Karn, Legacy Reforged](cards/K/ka.md#karn-legacy-reforged) | [Karn's Sylex](cards/K/ka.md#karns-sylex) · [Planar Bridge](cards/P/pl.md#planar-bridge) |
| Kefka, Court Mage | [Lord Xander, the Collector](cards/L/lo.md#lord-xander-the-collector) · [Tergrid, God of Fright // Tergrid's Lantern](cards/T/te.md#tergrid-god-of-fright--tergrids-lantern) |
| [Kenrith, the Returned King](cards/K/ke.md#kenrith-the-returned-king) | [Agatha of the Vile Cauldron](cards/A/ag.md#agatha-of-the-vile-cauldron) · [Jorn, God of Winter // Kaldring, the Rimestaff](cards/J/jo.md#jorn-god-of-winter--kaldring-the-rimestaff) |
| [Kotis, the Fangkeeper](cards/K/ko.md#kotis-the-fangkeeper) | [Blackblade Reforged](cards/B/bla.md#blackblade-reforged) · [Brokkos, Apex of Forever](cards/B/br.md#brokkos-apex-of-forever) |
| [Lathril, Blade of the Elves](cards/L/la.md#lathril-blade-of-the-elves) | [Glissa Sunslayer](cards/G/gl.md#glissa-sunslayer) · [Tyvar Kell](cards/T/ty.md#tyvar-kell) |
| [Meren of Clan Nel Toth](cards/M/me.md#meren-of-clan-nel-toth) | [Vraska, Golgari Queen](cards/V/vr.md#vraska-golgari-queen) · [Yawgmoth, Thran Physician](cards/Y/ya.md#yawgmoth-thran-physician) |
| [Najeela, the Blade-Blossom](cards/N/na.md#najeela-the-blade-blossom) | [Radha, Coalition Warlord](cards/R/rad.md#radha-coalition-warlord) · [Winota, Joiner of Forces](cards/W/wi.md#winota-joiner-of-forces) |
| [Nekusar, the Mindrazer](cards/N/ne.md#nekusar-the-mindrazer) | [Sheoldred, the Apocalypse](cards/S/she.md#sheoldred-the-apocalypse) · [Tergrid, God of Fright // Tergrid's Lantern](cards/T/te.md#tergrid-god-of-fright--tergrids-lantern) |
| [Niv-Mizzet, Guildpact](cards/N/ni.md#niv-mizzet-guildpact) | [Niv-Mizzet Reborn](cards/N/ni.md#niv-mizzet-reborn) · [Trostani, Three Whispers](cards/T/tro.md#trostani-three-whispers) |
| [Prosper, Tome-Bound](cards/P/pr.md#prosper-tome-bound) | [Hidetsugu, Devouring Chaos](cards/H/hi.md#hidetsugu-devouring-chaos) · [Valki, God of Lies // Tibalt, Cosmic Impostor](cards/V/va.md#valki-god-of-lies--tibalt-cosmic-impostor) |
| [Rendmaw, Creaking Nest](cards/R/ren.md#rendmaw-creaking-nest) | [Bow of Nylea](cards/B/bo.md#bow-of-nylea) · [Whip of Erebos](cards/W/wh.md#whip-of-erebos) |
| [Satoru Umezawa](cards/S/sat.md#satoru-umezawa) | [Jin-Gitaxias, Progress Tyrant](cards/J/ji.md#jin-gitaxias-progress-tyrant) · [Kaito Shizuki](cards/K/ka.md#kaito-shizuki) |
| Sephiroth, Fabled SOLDIER | [Sothera, the Supervoid](cards/S/so.md#sothera-the-supervoid) · [Yawgmoth, Thran Physician](cards/Y/ya.md#yawgmoth-thran-physician) |
| [Shorikai, Genesis Engine](cards/S/sho.md#shorikai-genesis-engine) | [Cosima, God of the Voyage // The Omenkeel](cards/C/cos.md#cosima-god-of-the-voyage--the-omenkeel) · [Tezzeret, Betrayer of Flesh](cards/T/te.md#tezzeret-betrayer-of-flesh) |
| [Slinza, the Spiked Stampede](cards/S/sl.md#slinza-the-spiked-stampede) | [Questing Beast](cards/Q/qu.md#questing-beast) · [Vivien, Monsters' Advocate](cards/V/vi.md#vivien-monsters-advocate) |
| [Tinybones, Bauble Burglar](cards/T/ti.md#tinybones-bauble-burglar) | [Rankle, Master of Pranks](cards/R/ran.md#rankle-master-of-pranks) · [Tergrid, God of Fright // Tergrid's Lantern](cards/T/te.md#tergrid-god-of-fright--tergrids-lantern) |
| [Toph, the First Metalbender](cards/T/to.md#toph-the-first-metalbender) | [Karn's Sylex](cards/K/ka.md#karns-sylex) · [The Ozolith](cards/T/theo.md#the-ozolith) |
| [Urza, Chief Artificer](cards/U/ur.md#urza-chief-artificer) | [Bident of Thassa](cards/B/bi.md#bident-of-thassa) · [The Mightstone and Weakstone](cards/T/them.md#the-mightstone-and-weakstone) |
| [Urza, Lord High Artificer](cards/U/ur.md#urza-lord-high-artificer) | [Memnarch](cards/M/me.md#memnarch) · [The Reality Chip](cards/T/ther.md#the-reality-chip) |
| [Valgavoth, Harrower of Souls](cards/V/va.md#valgavoth-harrower-of-souls) | [Rakdos, Lord of Riots](cards/R/rak.md#rakdos-lord-of-riots) · [Sheoldred, the Apocalypse](cards/S/she.md#sheoldred-the-apocalypse) |
| [Vivi Ornitier](cards/V/vi.md#vivi-ornitier) | [Birgi, God of Storytelling // Harnfel, Horn of Bounty](cards/B/bi.md#birgi-god-of-storytelling--harnfel-horn-of-bounty) · [Ral, Crackling Wit](cards/R/ral.md#ral-crackling-wit) |
| [Y'shtola, Night's Blessed](cards/Y/ys.md#yshtola-nights-blessed) | [Sheoldred, the Apocalypse](cards/S/she.md#sheoldred-the-apocalypse) · [Talion, the Kindly Lord](cards/T/ta.md#talion-the-kindly-lord) |
