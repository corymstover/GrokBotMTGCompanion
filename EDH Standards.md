---
title: "EDH Standards"
category: edh
tags: [deckbuilding-rules, color-identity, brackets]
issues: [6]
generated_by: hand-written
sources: [cr, wotc-articles]
related: ["grixis/Grixis Corrections.md", "EDH Archetypes.md", "EDH Staples.md", "EDH Deck Template.md", "EDH Deck Evaluation Checklist.md", "EDH Win Conditions.md"]
schema: 2
---

# EDH Standards

> House rules for every Commander (EDH) answer, list, and deck skeleton in this knowledge base.
> Related: [Card Data Conventions](Card%20Data%20Conventions.md) · [Card Index](Card%20Index.md) · [decks/](decks/) · [Project Goal](GOAL.md)
> Sources (fetched 2026-10-15): [Comprehensive Rules 2026-09-25, rule 903](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) · [Commander format page](https://magic.wizards.com/en/formats/commander) · [Introducing Commander Brackets Beta](https://magic.wizards.com/en/news/announcements/introducing-commander-brackets-beta) · [Brackets beta update, Oct 21 2025](https://magic.wizards.com/en/news/announcements/commander-brackets-beta-update-october-21-2025) · [Brackets beta update, Feb 9 2026](https://magic.wizards.com/en/news/announcements/commander-brackets-beta-update-february-9-2026) · [Commander B&R, Feb 9 2026](https://magic.wizards.com/en/news/announcements/commander-banned-and-restricted-february-9-2026)

## Contents
- [Core rules (verified)](#core-rules-verified)
- [Color identity (strict)](#color-identity-strict)
- [Commander first](#commander-first)
- [List format: Archidekt](#list-format-archidekt)
- [Power bracket assessment](#power-bracket-assessment)
- [Banned list & legality](#banned-list--legality)
- [Game Changers](#game-changers)
- [Deck skeletons](#deck-skeletons)
- [Synergy notes](#synergy-notes)
- [Staples by color & role → EDH Staples](EDH%20Staples.md)
- [Deck-building checklist](#deck-building-checklist)
- [Deck evaluation method (from the Grixis repo)](#deck-evaluation-method-from-the-grixis-repo)
- [Official legality vs house exceptions](#official-legality-vs-house-exceptions)
- [Open questions](#open-questions)

## Core rules (verified)

> Deeper rules topics (layers, replacement vs. triggers, SBAs, copy effects, color identity, command-zone returns) with verbatim CR 2026-09-25 text: [Rules Interactions](Rules%20Interactions.md).
| Rule | Source |
|---|---|
| Exactly **100 cards** including the commander. | CR 903.5a |
| **Singleton**: other than basic lands, every card has a different English name. | CR 903.5b |
| Commander = a **legendary** card that is (a) a creature, (b) a Vehicle, or (c) a Spacecraft with a P/T box — or a card whose text says it "can be your commander". | CR 903.3, 903.3a |
| **40 life**, 7-card opening hand; no sideboards. | CR 903.7, 903.5e |
| Commander tax: +{2} for each previous cast from the command zone. | CR 903.8 |
| Commander may return to the command zone from graveyard/exile (state-based action) or instead of going to hand/library. | CR 903.9a–b |
| **21 combat damage** from the same commander → that player loses. | CR 903.10a |
| Default multiplayer: Free-for-All, attack multiple players, no limited range of influence. | CR 903.2 |

## Color identity (strict)
- A card's color identity = colors of all mana symbols in its **mana cost and rules text**, plus color indicators and characteristic-defining abilities (CR 903.4). Reminder text is ignored (903.4c); **back faces of DFCs count** (903.4d); adventure/alternative characteristics count (903.4e).
- A card may be in the deck **only if every color of its identity is in the commander's identity** (CR 903.5c). Basic-land-typed cards: only if every color they could produce is in the identity (903.5d).
- **Hybrid** symbols count as *both* colors. The Commander Format Panel discussed changing this to "or" and on **2026-02-09 decided to make no change** ([source](https://magic.wizards.com/en/news/announcements/commander-brackets-beta-update-february-9-2026)).
- In this repo, identity is always taken from the Scryfall `color_identity` field shown in each card entry; deck skeletons are machine-checked against it ([`scripts/build_deck_skeleton.py`](scripts/build_deck_skeleton.py)).

## Commander first
Every list or answer starts with the commander block: name (linked to its card entry), mana cost, type line, color identity, eligibility basis (CR rule), and any pairing mechanic (Partner, Friends forever, Choose a Background, Doctor's companion). Only then the 99.

## List format: Archidekt
All deck lists use Archidekt's text import format in a fenced `text` block:
```text
1x Krenko, Mob Boss [Commander{top}]
1x Sol Ring [Artifact]
1x Goblin Matron [Creature]
20x Mountain [Land]
```
- `Nx Card Name` per line; optional `(set) collector-number` after the name pins a printing.
- `[Commander{top}]` marks the commander; other bracketed tags are categories. `[Maybeboard{noDeck}]` / `[Sideboard]` mark non-deck boards.
- Format confirmed from public Archidekt exports and third-party import docs (community source, not Wizards).

## Power bracket assessment
The official **Commander Brackets** (beta) are a pregame-conversation tool, not a hard rule ([format page](https://magic.wizards.com/en/formats/commander); Feb 2026 update reiterates this).

| Bracket | Intent (official wording, condensed) | Game Changers | Expected turns before win/loss (Oct 2025 update) |
|---|---|---|---|
| 1 Exhibition | Theme/idea over power; legality flexibility by pod agreement; thematic or substandard wins. | 0 | ≥ 9 |
| 2 Core | Unoptimized, straightforward; incremental, telegraphed, disruptable wins; low pressure. | 0 | ≥ 8 |
| 3 Upgraded | Strong synergy and card quality; can deploy a win in one big turn from accrued resources. | ≤ 3 | ≥ 6 |
| 4 Optimized | Lethal, consistent, fast; not built for the cEDH metagame. | Unlimited | ≥ 4 |
| 5 cEDH | Meticulously designed for the cEDH metagame; victory prioritized. | Unlimited | any turn |

Barometers from the original beta article (Feb 2025): Brackets 1–2 — no intentional two-card infinite combos, no mass land denial; Bracket 1 no extra-turn cards; Brackets 2–3 extra turns only in low quantity, not chained/looped; Bracket 3 — no *early-game* two-card infinite combos, no mass land denial; Brackets 4–5 — no restrictions beyond the banned list. The **Oct 21 2025 update removed tutor restrictions** (efficient tutors are caught by the Game Changers list instead) and decoupled precons from Bracket 2.

**How this repo assesses a deck** (method, not opinion): count Game Changers (Scryfall `game_changer` flag) → minimum bracket; flag extra-turn and mass-land-denial cards; two-card combos are detected automatically with the [Commander Spellbook](https://commanderspellbook.com) public API (`scripts/detect_combos.py`, results in each deck's *Combos* block and `data/combos.json`); a deck with a two-card infinite combo gets a combo-adjusted floor of at least Bracket 3 (barometer: none in Brackets 1–2). Whether a combo is "early-game" (Bracket 3 vs. 4) stays **Opinion**. ⚠️ Spellbook is community-maintained, so a missing combo is not proof that none exists. Final placement beyond these floors is **Opinion** and must be labeled so. Every deck's floor rationale, lower-bracket cut paths and pilot notes: [EDH Bracket Calibration](EDH%20Bracket%20Calibration.md) (Bot cycle 19, `scripts/deck_calibration.py`).

## Banned list & legality
Card legality in every entry comes from Scryfall. Latest Commander-specific B&R change found on magic.wizards.com: **2026-02-09 — Biorhythm unbanned (added to Game Changers); Lutri, the Spellchaser unbanned but remains banned as a companion.** (The 2026-10-12 B&R announcement made no Commander changes; its "banned as a commander" items apply to **Brawl**, an MTG Arena format.)

<!-- BANNED-LIST:START -->
*Auto-generated from Scryfall bulk data (2026-10-15); Scryfall mirrors the official lists.* **83 cards banned in Commander:**

[Adriana's Valor](cards/A/ad.md#adrianas-valor) · [Advantageous Proclamation](cards/A/ad.md#advantageous-proclamation) · [Amulet of Quoz](cards/A/am.md#amulet-of-quoz) · [Ancestral Recall](cards/A/an.md#ancestral-recall) · [Assemble the Rank and Vile](cards/A/as.md#assemble-the-rank-and-vile) · [Backup Plan](cards/B/bac.md#backup-plan) · [Balance](cards/B/bal.md#balance) · [Black Lotus](cards/B/bla.md#black-lotus) · [Brago's Favor](cards/B/br.md#bragos-favor) · [Bronze Tablet](cards/B/br.md#bronze-tablet) · [Channel](cards/C/cha.md#channel) · [Chaos Orb](cards/C/cha.md#chaos-orb) · [Cleanse](cards/C/cl.md#cleanse) · [Contract from Below](cards/C/con.md#contract-from-below) · [Crusade](cards/C/cr.md#crusade) · [Darkpact](cards/D/da.md#darkpact) · [Demonic Attorney](cards/D/dem.md#demonic-attorney) · [Dockside Extortionist](cards/D/do.md#dockside-extortionist) · [Double Stroke](cards/D/do.md#double-stroke) · [Echoing Boon](cards/E/ec.md#echoing-boon) · [Emissary's Ploy](cards/E/em.md#emissarys-ploy) · [Emrakul, the Aeons Torn](cards/E/em.md#emrakul-the-aeons-torn) · [Erayo, Soratami Ascendant // Erayo's Essence](cards/E/er.md#erayo-soratami-ascendant--erayos-essence) · [Falling Star](cards/F/fa.md#falling-star) · [Fastbond](cards/F/fa.md#fastbond) · [Flash](cards/F/fl.md#flash) · [Golos, Tireless Pilgrim](cards/G/gol.md#golos-tireless-pilgrim) · [Griselbrand](cards/G/gri.md#griselbrand) · [Hired Heist](cards/H/hi.md#hired-heist) · [Hold the Perimeter](cards/H/ho.md#hold-the-perimeter) · [Hullbreacher](cards/H/hu.md#hullbreacher) · [Hymn of the Wilds](cards/H/hy.md#hymn-of-the-wilds) · [Immediate Action](cards/I/im.md#immediate-action) · [Imprison](cards/I/im.md#imprison) · [Incendiary Dissent](cards/I/inc.md#incendiary-dissent) · [Invoke Prejudice](cards/I/inv.md#invoke-prejudice) · [Iona, Shield of Emeria](cards/I/io.md#iona-shield-of-emeria) · [Iterative Analysis](cards/I/it.md#iterative-analysis) · [Jeweled Bird](cards/J/je.md#jeweled-bird) · [Jeweled Lotus](cards/J/je.md#jeweled-lotus) · [Jihad](cards/J/ji.md#jihad) · [Karakas](cards/K/ka.md#karakas) · [Leovold, Emissary of Trest](cards/L/le.md#leovold-emissary-of-trest) · [Library of Alexandria](cards/L/li.md#library-of-alexandria) · [Limited Resources](cards/L/li.md#limited-resources) · [Mana Crypt](cards/M/man.md#mana-crypt) · [Mox Emerald](cards/M/mox.md#mox-emerald) · [Mox Jet](cards/M/mox.md#mox-jet) · [Mox Pearl](cards/M/mox.md#mox-pearl) · [Mox Ruby](cards/M/mox.md#mox-ruby) · [Mox Sapphire](cards/M/mox.md#mox-sapphire) · [Muzzio's Preparations](cards/M/mu.md#muzzios-preparations) · [Nadu, Winged Wisdom](cards/N/na.md#nadu-winged-wisdom) · [Natural Unity](cards/N/na.md#natural-unity) · [Paradox Engine](cards/P/pa.md#paradox-engine) · [Power Play](cards/P/po.md#power-play) · [Pradesh Gypsies](cards/P/pr.md#pradesh-gypsies) · [Primeval Titan](cards/P/pr.md#primeval-titan) · [Prophet of Kruphix](cards/P/pr.md#prophet-of-kruphix) · [Rebirth](cards/R/reb.md#rebirth) · [Recurring Nightmare](cards/R/rec.md#recurring-nightmare) · [Rofellos, Llanowar Emissary](cards/R/ro.md#rofellos-llanowar-emissary) · [Secret Summoning](cards/S/sec.md#secret-summoning) · [Secrets of Paradise](cards/S/sec.md#secrets-of-paradise) · [Sentinel Dispatch](cards/S/sen.md#sentinel-dispatch) · [Shahrazad](cards/S/sha.md#shahrazad) · [Sovereign's Realm](cards/S/so.md#sovereigns-realm) · [Stone-Throwing Devils](cards/S/sto.md#stone-throwing-devils) · [Summoner's Bond](cards/S/sum.md#summoners-bond) · [Sundering Titan](cards/S/sun.md#sundering-titan) · [Sylvan Primordial](cards/S/sy.md#sylvan-primordial) · [Tempest Efreet](cards/T/te.md#tempest-efreet) · [Time Vault](cards/T/ti.md#time-vault) · [Time Walk](cards/T/ti.md#time-walk) · [Timmerian Fiends](cards/T/ti.md#timmerian-fiends) · [Tinker](cards/T/ti.md#tinker) · [Tolarian Academy](cards/T/to.md#tolarian-academy) · [Trade Secrets](cards/T/tra.md#trade-secrets) · [Unexpected Potential](cards/U/un.md#unexpected-potential) · [Upheaval](cards/U/up.md#upheaval) · [Weight Advantage](cards/W/we.md#weight-advantage) · [Worldknit](cards/W/wo.md#worldknit) · [Yawgmoth's Bargain](cards/Y/ya.md#yawgmoths-bargain)
<!-- BANNED-LIST:END -->

## Game Changers
Definition (official): cards that "can dramatically warp Commander games… run away with resources… block people from play, efficiently search for their strongest cards, or have commanders that tend to take away from more casual games." Brackets 1–2: none; Bracket 3: up to three; Brackets 4–5: unlimited. Feb 9 2026: **Farewell** and **Biorhythm** added; **Lutri** deliberately not added.

<!-- GAME-CHANGERS:START -->
*Auto-generated from Scryfall bulk data (2026-10-15); Scryfall mirrors the official lists.* **53 Game Changers:**

- **White (7):** [Drannith Magistrate](cards/D/dra.md#drannith-magistrate) · [Enlightened Tutor](cards/E/en.md#enlightened-tutor) · [Farewell](cards/F/fa.md#farewell) · [Humility](cards/H/hu.md#humility) · [Serra's Sanctum](cards/S/ser.md#serras-sanctum) · [Smothering Tithe](cards/S/sm.md#smothering-tithe) · [Teferi's Protection](cards/T/te.md#teferis-protection)
- **Blue (10):** [Consecrated Sphinx](cards/C/con.md#consecrated-sphinx) · [Cyclonic Rift](cards/C/cy.md#cyclonic-rift) · [Fierce Guardianship](cards/F/fi.md#fierce-guardianship) · [Force of Will](cards/F/fo.md#force-of-will) · [Gifts Ungiven](cards/G/gi.md#gifts-ungiven) · [Intuition](cards/I/int.md#intuition) · [Mystical Tutor](cards/M/my.md#mystical-tutor) · [Narset, Parter of Veils](cards/N/na.md#narset-parter-of-veils) · [Rhystic Study](cards/R/rh.md#rhystic-study) · [Thassa's Oracle](cards/T/tha.md#thassas-oracle)
- **Black (10):** [Ad Nauseam](cards/A/ad.md#ad-nauseam) · [Bolas's Citadel](cards/B/bo.md#bolass-citadel) · [Braids, Cabal Minion](cards/B/br.md#braids-cabal-minion) · [Demonic Tutor](cards/D/dem.md#demonic-tutor) · [Imperial Seal](cards/I/im.md#imperial-seal) · [Necropotence](cards/N/ne.md#necropotence) · [Opposition Agent](cards/O/op.md#opposition-agent) · [Orcish Bowmasters](cards/O/or.md#orcish-bowmasters) · [Tergrid, God of Fright // Tergrid's Lantern](cards/T/te.md#tergrid-god-of-fright--tergrids-lantern) · [Vampiric Tutor](cards/V/va.md#vampiric-tutor)
- **Red (3):** [Gamble](cards/G/ga.md#gamble) · [Jeska's Will](cards/J/je.md#jeskas-will) · [Underworld Breach](cards/U/un.md#underworld-breach)
- **Green (7):** [Biorhythm](cards/B/bi.md#biorhythm) · [Crop Rotation](cards/C/cr.md#crop-rotation) · [Gaea's Cradle](cards/G/ga.md#gaeas-cradle) · [Natural Order](cards/N/na.md#natural-order) · [Seedborn Muse](cards/S/see.md#seedborn-muse) · [Survival of the Fittest](cards/S/sur.md#survival-of-the-fittest) · [Worldly Tutor](cards/W/wo.md#worldly-tutor)
- **Multicolor (4):** [Aura Shards](cards/A/au.md#aura-shards) · [Coalition Victory](cards/C/coa.md#coalition-victory) · [Grand Arbiter Augustin IV](cards/G/gra.md#grand-arbiter-augustin-iv) · [Notion Thief](cards/N/no.md#notion-thief)
- **Colorless (12):** [Ancient Tomb](cards/A/an.md#ancient-tomb) · [Chrome Mox](cards/C/chr.md#chrome-mox) · [Field of the Dead](cards/F/fi.md#field-of-the-dead) · [Glacial Chasm](cards/G/gl.md#glacial-chasm) · [Grim Monolith](cards/G/gri.md#grim-monolith) · [Lion's Eye Diamond](cards/L/li.md#lions-eye-diamond) · [Mana Vault](cards/M/man.md#mana-vault) · [Mishra's Workshop](cards/M/mis.md#mishras-workshop) · [Mox Diamond](cards/M/mox.md#mox-diamond) · [Panoptic Mirror](cards/P/pa.md#panoptic-mirror) · [The One Ring](cards/T/theo.md#the-one-ring) · [The Tabernacle at Pendrell Vale](cards/T/thet.md#the-tabernacle-at-pendrell-vale)
<!-- GAME-CHANGERS:END -->

## Deck skeletons
Built by [`scripts/build_deck_skeleton.py`](scripts/build_deck_skeleton.py): highest-inclusion cards for the commander from EDHREC (community data, fetched 2026-10-15), then **validated** (100 cards, singleton, strict identity, Commander-legal, commander eligibility) and bracket-floored. They are *starting points*, not tuned lists. Each skeleton ends with an auto-generated **Commander rules & rulings** block (`scripts/deck_rules_notes.py`): commander Oracle text, every official ruling, creature-type overlap, and which deck cards carry rulings. **Coverage: 32 skeletons — all 32 color identities** (5 mono-colors + colorless, 10 two-color pairs, 10 three-color combinations, all 5 four-color identities, and five-color). Bot cycle 3 added the last four: WUBR (Breya), UBRG (Yidris), BRGW (Saskia), RGWU (Kynaios and Tiro).

| Deck | Identity | Game Changers | Bracket floor (GC) | Spellbook combos / two-card infinite | Combo-adjusted floor |
|---|---|---|---|---|---|
| [Kozilek, the Great Distortion](decks/kozilek-the-great-distortion.md) | Colorless | 1 | 3 | 1 / 1 | 3 ⚠️ |
| [K'rrik, Son of Yawgmoth](decks/krrik-son-of-yawgmoth.md) | B | 7 | 4 | 15 / 5 | 4 ⚠️ |
| [Selvala, Heart of the Wilds](decks/selvala-heart-of-the-wilds.md) | G | 2 | 3 | 27 / 9 | 3 ⚠️ |
| [Krenko, Mob Boss](decks/krenko-mob-boss.md) | R | 0 | 2 (or 1) | 4 / 0 | 2 (or 1) |
| [Talrand, Sky Summoner](decks/talrand-sky-summoner.md) | U | 3 | 3 | 2 / 1 | 3 ⚠️ |
| [Giada, Font of Hope](decks/giada-font-of-hope.md) | W | 3 | 3 | 0 / 0 | 3 |
| [Lathril, Blade of the Elves](decks/lathril-blade-of-the-elves.md) | BG | 1 | 3 | 0 / 0 | 3 |
| [Prosper, Tome-Bound](decks/prosper-tome-bound.md) | BR | 1 | 3 | 2 / 0 | 3 |
| [Yuriko, the Tiger's Shadow](decks/yuriko-the-tigers-shadow.md) | BU | 4 | 4 | 0 / 0 | 4 |
| [Teysa Karlov](decks/teysa-karlov.md) | BW | 2 | 3 | 23 / 0 | 3 |
| [Xenagos, God of Revels](decks/xenagos-god-of-revels.md) | GR | 0 | 2 (or 1) | 4 / 3 | **3** ⚠️ |
| [Tatyova, Benthic Druid](decks/tatyova-benthic-druid.md) | GU | 2 | 3 | 2 / 0 | 3 |
| [Trostani, Selesnya's Voice](decks/trostani-selesnyas-voice.md) | GW | 1 | 3 | 0 / 0 | 3 |
| [Niv-Mizzet, Parun](decks/niv-mizzet-parun.md) | RU | 4 | 4 | 8 / 8 | 4 ⚠️ |
| [Feather, the Redeemed](decks/feather-the-redeemed.md) | RW | 0 | 2 (or 1) | 0 / 0 | 2 (or 1) |
| [Brago, King Eternal](decks/brago-king-eternal.md) | UW | 1 | 3 | 11 / 4 | 3 ⚠️ |
| [Korvold, Fae-Cursed King](decks/korvold-fae-cursed-king.md) | BGR | 4 | 4 | 11 / 1 | 4 ⚠️ |
| [Muldrotha, the Gravetide](decks/muldrotha-the-gravetide.md) | BGU | 1 | 3 | 1 / 0 | 3 |
| [Karador, Ghost Chieftain](decks/karador-ghost-chieftain.md) | BGW | 0 | 2 (or 1) | 14 / 0 | 2 (or 1) |
| [Nekusar, the Mindrazer](decks/nekusar-the-mindrazer.md) | BRU | 2 | 3 | 7 / 5 | 3 ⚠️ |
| [Edgar Markov](decks/edgar-markov.md) | BRW | 3 | 3 | 6 / 6 | 3 ⚠️ |
| [Zur the Enchanter](decks/zur-the-enchanter.md) | BUW | 8 | 4 | 1 / 0 | 4 |
| [Animar, Soul of Elements](decks/animar-soul-of-elements.md) | GRU | 5 | 4 | 4 / 3 | 4 ⚠️ |
| [Gishath, Sun's Avatar](decks/gishath-suns-avatar.md) | GRW | 0 | 2 (or 1) | 3 / 1 | **3** ⚠️ |
| [Chulane, Teller of Tales](decks/chulane-teller-of-tales.md) | GUW | 6 | 4 | 8 / 3 | 4 ⚠️ |
| [Kykar, Wind's Fury](decks/kykar-winds-fury.md) | RUW | 6 | 4 | 0 / 0 | 4 |
| [Breya, Etherium Shaper](decks/breya-etherium-shaper.md) | BRUW | 3 | 3 | 32 / 0 | 3 |
| [Yidris, Maelstrom Wielder](decks/yidris-maelstrom-wielder.md) | BGRU | 0 | 2 (or 1) | 0 / 0 | 2 (or 1) |
| [Saskia the Unyielding](decks/saskia-the-unyielding.md) | BGRW | 1 | 3 | 0 / 0 | 3 |
| [Kynaios and Tiro of Meletis](decks/kynaios-and-tiro-of-meletis.md) | GRUW | 1 | 3 | 0 / 0 | 3 |
| [Atraxa, Praetors' Voice](decks/atraxa-praetors-voice.md) | BGUW | 5 | 4 | 1 / 0 | 4 |
| [The Ur-Dragon](decks/the-ur-dragon.md) | BGRUW | 3 | 3 | 2 / 1 | 3 ⚠️ |

## Synergy notes

> Archetype-level guides (aristocrats, tokens, spellslinger, landfall, counters, graveyard, blink, artifacts, combat, cascade, group hug/slug, lifedrain): [EDH Archetypes](EDH%20Archetypes.md).

> Each note pairs a commander's **Oracle text** (rules fact, quoted from the linked entry) with cards in its validated skeleton, plus official **rulings** where they settle an interaction (Scryfall rulings bulk, source Wizards of the Coast). Anything about *how good* a line is = **Opinion**. Role and identity staples: [EDH Staples](EDH%20Staples.md).

### Death triggers ×2 — Teysa Karlov (WB, aristocrats)
- **Rules fact:** [Teysa Karlov](cards/T/te.md#teysa-karlov) — "If a creature dying causes a triggered ability of a permanent you control to trigger, that ability triggers an additional time." Her creature tokens also have vigilance and lifelink.
- **Doubled (they trigger on a creature dying):** [Blood Artist](cards/B/blo.md#blood-artist), [Zulaport Cutthroat](cards/Z/zu.md#zulaport-cutthroat), [Cruel Celebrant](cards/C/cr.md#cruel-celebrant), [Bastion of Remembrance](cards/B/bas.md#bastion-of-remembrance) (drain), [Pitiless Plunderer](cards/P/pi.md#pitiless-plunderer) (two Treasures per death).
- **Not doubled (ruling 2019-01-25, WotC):** "An ability that triggers on an event that causes a creature to die doesn't trigger twice. For example, an ability that triggers 'whenever you sacrifice a creature' triggers only once." So the sacrifice clause of [Mirkwood Bats](cards/M/mir.md#mirkwood-bats) triggers once; sacrifice outlets [Ashnod's Altar](cards/A/as.md#ashnods-altar) and [Viscera Seer](cards/V/vi.md#viscera-seer) are the *enablers*, not the doubled payoff.
- **Opinion:** the deck wants ~4–6 free sacrifice outlets and ~8+ death payoffs; protect Teysa, since the doubling is the engine. Skeleton: [Teysa Karlov](decks/teysa-karlov.md).

### Instants & sorceries make bodies — Talrand, Sky Summoner (U, spellslinger)
- **Rules fact:** [Talrand, Sky Summoner](cards/T/ta.md#talrand-sky-summoner) — "Whenever you cast an instant or sorcery spell, create a 2/2 blue Drake creature token with flying." Ruling (2021-03-19, WotC): the trigger "resolves before the spell that caused it to trigger … It resolves even if that spell is countered."
- **Stacks with:** [Murmuring Mystic](cards/M/mu.md#murmuring-mystic) (1/1 flying Bird per instant/sorcery) and [Archmage Emeritus](cards/A/arc.md#archmage-emeritus) (magecraft: draw a card on cast *or copy*) — each cheap cantrip or counterspell becomes card + flier(s).
- **Opinion:** cheap interaction (counterspells such as [Counterspell](cards/C/cou.md#counterspell) and [Arcane Denial](cards/A/arc.md#arcane-denial)) doubles as threat production; prioritize low-MV spells over big sorceries. Skeleton: [Talrand, Sky Summoner](decks/talrand-sky-summoner.md) (3 Game Changers → bracket floor 3).

### Landfall card draw — Tatyova, Benthic Druid (GU, lands matter)
- **Rules fact:** [Tatyova, Benthic Druid](cards/T/ta.md#tatyova-benthic-druid) — "Landfall — Whenever a land you control enters, you gain 1 life and draw a card." Ruling (2024-11-08, WotC): landfall "triggers whenever you play a land, as well as whenever a spell or ability puts a land onto the battlefield under your control"; it does **not** trigger "if a permanent already on the battlefield becomes a land."
- **Extra land drops (more triggers per turn):** [Exploration](cards/E/ex.md#exploration), [Azusa, Lost but Seeking](cards/A/az.md#azusa-lost-but-seeking) (two additional lands), [Dryad of the Ilysian Grove](cards/D/dry.md#dryad-of-the-ilysian-grove), [Oracle of Mul Daya](cards/O/or.md#oracle-of-mul-daya) (also plays lands from the top of the library).
- **Land recursion (reuse fetch/sacrifice lands):** [Crucible of Worlds](cards/C/cr.md#crucible-of-worlds), [Ramunap Excavator](cards/R/ram.md#ramunap-excavator) — "You may play lands from your graveyard."
- **Opinion:** run more lands than usual (~38–40) plus fetch-style lands so each land drop yields two triggers. Skeleton: [Tatyova, Benthic Druid](decks/tatyova-benthic-druid.md).

### Sacrifice = card + counter — Korvold, Fae-Cursed King (BRG, sacrifice/Treasure)
- **Rules fact:** [Korvold, Fae-Cursed King](cards/K/ko.md#korvold-fae-cursed-king) — "Whenever you sacrifice a permanent, put a +1/+1 counter on Korvold and draw a card." Rulings (2019-10-04, WotC): it "is a triggered ability, not an activated ability … you need some other way of sacrificing permanents"; a sacrifice paid as a cost resolves its trigger "before that spell or ability"; a legendary permanent put into the graveyard by the legend rule "isn't sacrificed."
- **Enablers in the skeleton (each sacrifice = a Korvold trigger):** Treasure makers [Pitiless Plunderer](cards/P/pi.md#pitiless-plunderer), [Mahadi, Emporium Master](cards/M/mah.md#mahadi-emporium-master), [Tireless Provisioner](cards/T/ti.md#tireless-provisioner) (Food or Treasure); outlets [Viscera Seer](cards/V/vi.md#viscera-seer), [Ashnod's Altar](cards/A/as.md#ashnods-altar); even [Evolving Wilds](cards/E/ev.md#evolving-wilds) ("Sacrifice this land"). [Mayhem Devil](cards/M/may.md#mayhem-devil) pings on *any player's* sacrifice.
- **Opinion:** Treasures are the cleanest fodder (mana now, card later). Skeleton: [Korvold](decks/korvold-fae-cursed-king.md) (4 GC → floor 4).

### One permanent of each type from the graveyard — Muldrotha, the Gravetide (BGU, self-mill)
- **Rules fact:** [Muldrotha, the Gravetide](cards/M/mu.md#muldrotha-the-gravetide) — "During each of your turns, you may play a land and cast a permanent spell of each permanent type from your graveyard." Rulings (2020-11-10, WotC): you "must follow the normal timing permissions" (no land without an available land play); an artifact creature can count as *either* type, chosen as you cast it; costs must be paid.
- **In the skeleton:** mill enablers [Stitcher's Supplier](cards/S/sti.md#stitchers-supplier), [Satyr Wayfinder](cards/S/sat.md#satyr-wayfinder), [Mesmeric Orb](cards/M/me.md#mesmeric-orb); recastable sacrifice creatures [Sakura-Tribe Elder](cards/S/sak.md#sakura-tribe-elder) and [Spore Frog](cards/S/spo.md#spore-frog) (one creature recast per turn — the creature "slot" is shared); [Eternal Witness](cards/E/et.md#eternal-witness) returns nonpermanents Muldrotha can't cast.
- **Opinion:** diversify permanent types (artifact, enchantment, land, creature, planeswalker, battle) to use every slot. Skeleton: [Muldrotha](decks/muldrotha-the-gravetide.md).

### Recursion with a cost reduction — Karador, Ghost Chieftain (WBG, graveyard creatures)
- **Rules fact:** [Karador, Ghost Chieftain](cards/K/ka.md#karador-ghost-chieftain) — costs "{1} less to cast for each creature card in your graveyard" and "Once during each of your turns, you may cast a creature spell from your graveyard." Ruling (2020-11-10): total cost = mana cost + increases (e.g. **commander tax**) − reductions; mana value is unchanged.
- **In the skeleton:** the same sacrifice-and-recast pieces as Muldrotha ([Sakura-Tribe Elder](cards/S/sak.md#sakura-tribe-elder), [Spore Frog](cards/S/spo.md#spore-frog), [Viscera Seer](cards/V/vi.md#viscera-seer)) plus mill ([Stitcher's Supplier](cards/S/sti.md#stitchers-supplier), [Satyr Wayfinder](cards/S/sat.md#satyr-wayfinder)) that also shrinks Karador's own cost.
- Skeleton: [Karador](decks/karador-ghost-chieftain.md) (0 GC → floor 2).

### Ninjas reveal and drain — Yuriko, the Tiger's Shadow (UB, ninjutsu)
- **Rules fact:** [Yuriko, the Tiger's Shadow](cards/Y/yu.md#yuriko-the-tigers-shadow) — whenever a Ninja you control deals combat damage to a player, reveal the top card; "Each opponent loses life equal to that card's mana value." Rulings (2020-11-10): activating commander ninjutsu "isn't the same as casting Yuriko … You won't have to pay the commander tax"; the Ninja "was never declared as an attacking creature" (no attack triggers); X in a revealed card's cost is 0.
- **In the skeleton:** evasive 1-drops that start ninjutsu — [Changeling Outcast](cards/C/cha.md#changeling-outcast) (is every creature type, so it is also a Ninja for Yuriko's trigger; "can't be blocked"), [Ornithopter](cards/O/or.md#ornithopter), [Gingerbrute](cards/G/gi.md#gingerbrute); Ninjas [Ingenious Infiltrator](cards/I/ing.md#ingenious-infiltrator), [Fallen Shinobi](cards/F/fa.md#fallen-shinobi), [Mistblade Shinobi](cards/M/mis.md#mistblade-shinobi); [Sensei's Divining Top](cards/S/sen.md#senseis-divining-top) arranges the top card before the reveal.
- Skeleton: [Yuriko](decks/yuriko-the-tigers-shadow.md) (4 GC → floor 4).

### Life as black mana — K'rrik, Son of Yawgmoth (B, life-payment)
- **Rules fact:** [K'rrik, Son of Yawgmoth](cards/K/kr.md#krrik-son-of-yawgmoth) — "For each {B} in a cost, you may pay 2 life rather than pay that mana." Rulings: it "doesn't modify or reduce costs" (only how you pay); you can't pay life for **generic** mana; it applies to "any cost you pay, including … activation costs, and even costs for special actions"; K'rrik's mana value is always 7.
- **In the skeleton:** [Dark Ritual](cards/D/da.md#dark-ritual) for 2 life (adds {B}{B}{B}); [Necropotence](cards/N/ne.md#necropotence) and [Bolas's Citadel](cards/B/bo.md#bolass-citadel) convert life into cards/spells; lifelink plus [Gray Merchant of Asphodel](cards/G/gra.md#gray-merchant-of-asphodel), [Exsanguinate](cards/E/ex.md#exsanguinate) and [Sanguine Bond](cards/S/san.md#sanguine-bond) refill life.
- Skeleton: [K'rrik](decks/krrik-son-of-yawgmoth.md) (7 GC → floor 4).

### Blink on combat damage — Brago, King Eternal (WU, flicker)
- **Rules fact:** [Brago, King Eternal](cards/B/br.md#brago-king-eternal) — on combat damage to a player, exile any number of target nonland permanents you control, then return them. Rulings (2020-11-10): this happens "after combat damage is dealt" (creatures that died can't be targeted); Brago may blink itself; a returning Aura "doesn't target anything."
- **In the skeleton:** enter-the-battlefield value — [Mulldrifter](cards/M/mu.md#mulldrifter), [Cloudblazer](cards/C/cl.md#cloudblazer) (draw two), [Solemn Simulacrum](cards/S/so.md#solemn-simulacrum) (land), [Venser, Shaper Savant](cards/V/ve.md#venser-shaper-savant) (bounce), [Sun Titan](cards/S/sun.md#sun-titan).
- Skeleton: [Brago](decks/brago-king-eternal.md).

### Playing from exile makes Treasure — Prosper, Tome-Bound (BR, impulse draw)
- **Rules fact:** [Prosper, Tome-Bound](cards/P/pr.md#prosper-tome-bound) — "Pact Boon — Whenever you play a card from exile, create a Treasure token." Ruling (2021-07-23): it "triggers whenever you play any cards from exile, not just those exiled with the Mystic Arcanum ability."
- **In the skeleton:** other exile-and-play sources — [Light Up the Stage](cards/L/li.md#light-up-the-stage), [Jeska's Will](cards/J/je.md#jeskas-will), [Professional Face-Breaker](cards/P/pr.md#professional-face-breaker) (whose Treasures also feed its own exile ability).
- Skeleton: [Prosper](decks/prosper-tome-bound.md).

### Draw ↔ damage loop — Niv-Mizzet, Parun (UR, spellslinger) ⚠️ two-card combo
- **Rules fact:** [Niv-Mizzet, Parun](cards/N/ni.md#niv-mizzet-parun) — "Whenever you draw a card, Niv-Mizzet deals 1 damage to any target." Rulings (2018-10-05): drawing multiple cards triggers it that many times; putting cards into hand without the word "draw" doesn't.
- **Combo (rules fact from Oracle text):** with [Curiosity](cards/C/cu.md#curiosity) or [Ophidian Eye](cards/O/op.md#ophidian-eye) on Niv-Mizzet ("Whenever enchanted creature deals damage to an opponent, you may draw a card"), each ping at an opponent draws a card, which pings again — a loop that only stops when you decline the optional draw or run out of library/opponents. [Tandem Lookout](cards/T/ta.md#tandem-lookout) paired with Niv-Mizzet does the same (mandatory draw). [Psychosis Crawler](cards/P/ps.md#psychosis-crawler) adds 1 life loss per draw.
- **Bracket note:** the [Commander Brackets](#power-bracket-assessment) restrict two-card infinite combos in the lower brackets; this skeleton already floors at 4 (4 GC). Flagged because `build_deck_skeleton.py` does not detect combos (#15).

### Artifacts as ammunition — Breya, Etherium Shaper (WUBR, artifacts)
- **Rules fact:** [Breya, Etherium Shaper](cards/B/br.md#breya-etherium-shaper) — "When Breya enters, create two 1/1 blue Thopter artifact creature tokens with flying. / {2}, Sacrifice two artifacts: Choose one — … Breya deals 3 damage to target player or planeswalker … Target creature gets -4/-4 … You gain 5 life."
- **Ruling (2020-08-07, WotC):** "Breya can be one of the two artifacts sacrificed to pay the cost of its last ability."
- **Artifact token makers in the skeleton (fuel the sacrifice cost):** [Sai, Master Thopterist](cards/S/sai.md#sai-master-thopterist), [Efficient Construction](cards/E/ef.md#efficient-construction), [Pinnacle Emissary](cards/P/pi.md#pinnacle-emissary), [Thopter Spy Network](cards/T/tho.md#thopter-spy-network), [Marionette Master](cards/M/mar.md#marionette-master), [Myr Battlesphere](cards/M/my.md#myr-battlesphere); [Stridehangar Automaton](cards/S/str.md#stridehangar-automaton) adds one more artifact token whenever artifact tokens would be created (Oracle).
- **Other sacrifice outlets / payoffs:** [Krark-Clan Ironworks](cards/K/kr.md#krark-clan-ironworks), [Thopter Foundry](cards/T/tho.md#thopter-foundry), [Jan Jansen, Chaos Crafter](cards/J/ja.md#jan-jansen-chaos-crafter); [Reckless Fireweaver](cards/R/rec.md#reckless-fireweaver) pings each opponent whenever an artifact enters.
- **Opinion:** the deck is a value/aristocrats engine; check [#15](https://github.com/corymstover/GrokBotMTGCompanion/issues/15) combo notes before calling it Bracket 3.

### Cascade on combat damage — Yidris, Maelstrom Wielder (UBRG, cascade)
- **Rules fact:** [Yidris, Maelstrom Wielder](cards/Y/yi.md#yidris-maelstrom-wielder) — "Whenever Yidris deals combat damage to a player, as you cast spells from your hand this turn, they gain cascade."
- **Rulings (2016-11-08, WotC):** "If Yidris's triggered ability resolves more than once in one turn, spells you cast from your hand will gain cascade that many times." · "Spells you cast from your hand this turn will gain cascade even if Yidris leaves the battlefield."
- **Getting the trigger (evasion in the skeleton):** [Whispersilk Cloak](cards/W/wh.md#whispersilk-cloak), [Brotherhood Regalia](cards/B/br.md#brotherhood-regalia) ("can't be blocked").
- **Native cascade (works without Yidris):** [Maelstrom Wanderer](cards/M/mae.md#maelstrom-wanderer), [Apex Devastator](cards/A/ap.md#apex-devastator), [Bloodbraid Elf](cards/B/blo.md#bloodbraid-elf), [Shardless Agent](cards/S/sha.md#shardless-agent), [Imoti, Celebrant of Bounty](cards/I/im.md#imoti-celebrant-of-bounty), [Aurora Phoenix](cards/A/au.md#aurora-phoenix); [Averna, the Chaos Bloom](cards/A/av.md#averna-the-chaos-bloom) lets you put a land from the exiled cards onto the battlefield as you cascade.
- **Opinion:** cast the spells *after* combat (second main phase) so the trigger has already resolved.

### Combat damage, redirected — Saskia the Unyielding (BRGW, aggro)
- **Rules fact:** [Saskia the Unyielding](cards/S/sas.md#saskia-the-unyielding) — "As Saskia enters, choose a player. / Whenever a creature you control deals combat damage to a player, it deals that much damage to the chosen player."
- **Rulings (2016-11-08, WotC):** "The damage that Saskia's ability causes a creature to deal isn't combat damage." · "If a creature you control deals combat damage to the chosen player, it deals that much damage to that player again." · "If Saskia leaves the battlefield and returns, you choose a player again."
- **Consequence:** the redirected damage does **not** trigger "deals combat damage to a player" abilities such as [Ohran Frostfang](cards/O/oh.md#ohran-frostfang), [Toski, Bearer of Secrets](cards/T/to.md#toski-bearer-of-secrets), [Marisi, Breaker of the Coil](cards/M/mar.md#marisi-breaker-of-the-coil) a second time — only the original combat damage does (follows from the first ruling; CR 120.2a combat damage).
- **More combat damage events:** double strike from [Samut, Voice of Dissent](cards/S/sam.md#samut-voice-of-dissent) (two combat damage steps ⇒ two triggers, CR 702.4b, 510.4), extra combats from [Aurelia, the Warleader](cards/A/au.md#aurelia-the-warleader), [Karlach, Fury of Avernus](cards/K/ka.md#karlach-fury-of-avernus).

### Group hug lands & cards — Kynaios and Tiro of Meletis (RGWU, group hug)
- **Rules fact:** [Kynaios and Tiro of Meletis](cards/K/ky.md#kynaios-and-tiro-of-meletis) — "At the beginning of your end step, draw a card. Each player may put a land card from their hand onto the battlefield, then each opponent who didn't draws a card."
- **Ruling (2016-11-08, WotC):** "Starting with you and proceeding in turn order, each player chooses a land card from their hand or chooses not to choose one, but doesn't reveal any chosen lands yet. Once all players have made this choice, all chosen lands are revealed and enter the battlefield simultaneously." · "If the card you draw is a land card, you may choose it to put onto the battlefield."
- **Symmetric effects in the skeleton:** [Temple Bell](cards/T/te.md#temple-bell), [Folio of Fancies](cards/F/fo.md#folio-of-fancies), [Minds Aglow](cards/M/min.md#minds-aglow), [Collective Voyage](cards/C/col.md#collective-voyage), [Tempt with Discovery](cards/T/te.md#tempt-with-discovery), [Veteran Explorer](cards/V/ve.md#veteran-explorer), [The Second Doctor](cards/T/thes.md#the-second-doctor); punishers that turn opponents' draws into value: [Scrawling Crawler](cards/S/sc.md#scrawling-crawler), [Psychosis Crawler](cards/P/ps.md#psychosis-crawler).
- **Opinion:** group hug relies on table politics; disclose this in Rule 0 (see [Bracket assessment](#power-bracket-assessment)).

## Deck-building checklist
1. Commander block first (eligibility per CR 903.3; pairing mechanics).
2. Every card's identity ⊆ commander identity (check entry's **Color identity** line).
3. 100 cards, singleton, no banned cards.
4. Count Game Changers → bracket floor; flag extra turns, mass land denial, two-card combos.
5. Output in Archidekt format; link each card to its entry; label any recommendation **Opinion**.
6. Typical ratios (e.g., ~36 lands, ~10 ramp, ~10 draw, ~8–10 interaction) are **community convention / Opinion**, not rules.
7. For an external or hand-built list, run `python3 scripts/evaluate_decklist.py list.txt --combos` (any identity). It checks steps 1–4 and prints the bracket floor (Bot cycle 16).

## Deck evaluation method (from the Grixis repo)
Bot cycle 16 ([#62](https://github.com/corymstover/GrokBotMTGCompanion/issues/62)) adopted the user's Grixis project method ([grixis-commander-encyclopediaGPT](https://github.com/corymstover/grixis-commander-encyclopediaGPT), Deck Quality Gates v3 and Refinement Protocol v1) as this repo's **standard process for building or refining any deck**. The rules above still decide legality. The method adds the strategic and evidence gates:
- **Commander-first blueprint** before any card is evaluated. **Whole-list audit** of all 99 slots. **Named swaps** (candidate vs cut) in a ledger. A 0–5 **card-fit rubric**. **Red-team** and **commander-necessity** reviews. **Evidence labels** (VERIFIED / HIGH_CONFIDENCE / PROVISIONAL / TEST_REQUIRED / BLOCKED). A **stop rule** (a complete pass with zero new material improvements) and explicit **reopen triggers**.
- Pages: [EDH Deck Template](EDH%20Deck%20Template.md) (blueprint, role map, ledger, rubric, finalization record) · [EDH Deck Evaluation Checklist](EDH%20Deck%20Evaluation%20Checklist.md) (gates A–E). Worked examples: the 40 [Grixis decks](grixis/README.md).
- **Repo addition:** every stated target bracket must be ≥ the Game Changer and combo floor. The Grixis records never counted Game Changers, so the import added them ([Grixis Corrections](grixis/Grixis%20Corrections.md)).

## Official legality vs house exceptions
A Rule 0 group may allow banned cards or companions. Lists published in this repo must be **officially Commander-legal**. A house-allowed card is recorded separately and replaced or flagged, never labeled legal. Example: the Grixis import replaced Trade Secrets and Yawgmoth's Bargain and dropped Lutri as companion ([corrections table](grixis/Grixis%20Corrections.md#corrections-table)).

## Open questions
- ❓ The Commander format page says "choose a legendary creature or artifact" while CR 903.3 (2026-09-25) specifies creature, Vehicle, or Spacecraft-with-P/T. This repo follows the CR.
- ❓ Brackets remain "beta"; the Feb 2026 update said the beta tag may be dropped later in 2026. Re-check each cycle.
- ✅ Two-card combo detection is automated through Commander Spellbook (`scripts/detect_combos.py`, `scripts/evaluate_decklist.py --combos`). Spellbook is community-maintained, so a missing combo does not prove that none exists.
