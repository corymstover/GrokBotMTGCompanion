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
- [Deck-building checklist](#deck-building-checklist)
- [Open questions](#open-questions)

## Core rules (verified)
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

**How this repo assesses a deck** (method, not opinion): count Game Changers (Scryfall `game_changer` flag) → minimum bracket; flag extra-turn and mass-land-denial cards; two-card combos are reviewed manually and labeled ⚠️ until verified. Final placement beyond these floors is **Opinion** and must be labeled so.

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
Built by [`scripts/build_deck_skeleton.py`](scripts/build_deck_skeleton.py): highest-inclusion cards for the commander from EDHREC (community data, fetched 2026-10-15), then **validated** (100 cards, singleton, strict identity, Commander-legal, commander eligibility) and bracket-floored. They are *starting points*, not tuned lists.

| Deck | Identity | Game Changers | Bracket floor |
|---|---|---|---|
| [Krenko, Mob Boss](decks/krenko-mob-boss.md) | R | 0 | 2 (or 1) |
| [Lathril, Blade of the Elves](decks/lathril-blade-of-the-elves.md) | BG | 1 | 3 |
| [Edgar Markov](decks/edgar-markov.md) | BRW | 3 | 3 |
| [Atraxa, Praetors' Voice](decks/atraxa-praetors-voice.md) | BGUW | 5 | 4 |
| [The Ur-Dragon](decks/the-ur-dragon.md) | WUBRG | 3 | 3 |

## Deck-building checklist
1. Commander block first (eligibility per CR 903.3; pairing mechanics).
2. Every card's identity ⊆ commander identity (check entry's **Color identity** line).
3. 100 cards, singleton, no banned cards.
4. Count Game Changers → bracket floor; flag extra turns, mass land denial, two-card combos.
5. Output in Archidekt format; link each card to its entry; label any recommendation **Opinion**.
6. Typical ratios (e.g., ~36 lands, ~10 ramp, ~10 draw, ~8–10 interaction) are **community convention / Opinion**, not rules.

## Open questions
- ❓ The Commander format page says "choose a legendary creature or artifact" while CR 903.3 (2026-09-25) specifies creature, Vehicle, or Spacecraft-with-P/T. This repo follows the CR.
- ❓ Brackets remain "beta"; the Feb 2026 update said the beta tag may be dropped later in 2026. Re-check each cycle.
- ⚠️ Two-card combo detection is not automated (candidate future source: Commander Spellbook).
