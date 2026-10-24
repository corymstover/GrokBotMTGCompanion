# Ashnod the Uncaring — independent M7 Rev2 nine-swap review

**STATUS: NOT OWNER APPROVED / NOT CANONICAL.** Prepared for Cory's explicit review after exact-head testing. Original Grok #654 research and historical canonical list are preserved.

Original canonical October 13 raw SHA: `f574e4fad4749603294f53d2fe5536a159f884a8f1a8a7b6b1a22b3a637cf1cf`. Grok five-swap raw SHA: `b1078f084c2fa53426910edb66f0a036978e06bd9c9a2061f460af397503143d`. Independent Rev2 nine-swap raw SHA: `a045579b6f9d21f50c47da0096cb0dfc0dee772493eb522186944f61cb6c4761`; logical `lh1:bd81a60cfbd2728705bfe2e14bd32f56a4081b51cf72b46a7d6cb057e9a30140`.

## Identity and choice

Copy non-mana activated artifact/creature abilities with sacrifice in their activation costs; recursive artifacts, fodder generation, extra turns and sacrifice payoffs, with specific Ashnod commander-dependent infinite lines. Basalt's two artifact-loop synergies and the Pit/Module sacrifice/token loops are selected for this deck's existing engine, not to insert a generic Grixis combo package. No Thassa's Oracle/Consultation package.

### Nine replacement decisions

| Add | Cut | Independent commander-specific judgment |
|---|---|---|
| Corridor Monitor | Foundry Inspector | The Goblin Engineer + Lotus Petal + Monitor loop actually uses Ashnod's copy, creates repeatable artifact/creature death and ETBs, and Monitor untaps key artifacts even outside the combo. Inspector was the third reducer; two remain. |
| Basalt Monolith | Fellwar Stone | Missed by first-pass M7: one card unlocks TWO independent two-card colorless-infinite combos with existing Rings of Brighthearth or Forensic Gadgeteer (Spellbook 4131-4235 and 4131-5390), plus triples mana once without combo. The deck keeps Walking Ballista to convert colorless mana into a win. |
| Aether Spellbomb | Talisman of Indulgence | Both sacrifice abilities are copied by Ashnod: bounce up to two target creatures for U or draw two for 1. Replaces the most replaceable color Talisman; 33 lands/8 rocks plus more reliable untapped rainbow lands mitigate the one-rock loss. |
| Spawning Pit | Esoteric Duplicator | Two-mana free repeatable artifact activated sacrifice outlet; Ashnod copies its charge-counter ability. Along with Crime Novelist, a creature to start, and 1 mana if that creature is not an artifact, it can repeat sacrificing the newly made artifact Spawn, adding two Pit counters, getting R from Novelist and spending R to replace the Spawn. New manually derived Ashnod-specific death/ETB/sacrifice loop. Duplicator's late end-step copying remains a real opportunity cost. |
| Animation Module | Reckless Fireweaver | One-mana Urza's Saga target, exploits Novelist's counters and already-present Arcbound Ravager/Ashnod's Altar/KCI. Commander Spellbook independently lists three near-complete three-card combos with exactly Module missing: 2829-3490-5346, 2034-3490-5346, 3490-4659-5346. Fireweaver is a reliable damage payoff, but several other sacrifice-win outlets remain. |
| Priest of Forgotten Gods | Jhoira, Weatherlight Captain | Ashnod copies targeted Priest ability after two other creatures are sacrificed: each selected opponent may lose 4/sacrifice two creatures and we receive BBBB plus two draws. This trades unconditional 4-MV historic-card draw for a 2-MV commander-doubled mana, removal and draw engine. |
| Ruthless Knave | Farid, Enterprising Salvager | Ruthless is 3 MV and immediately turns 2B plus one creature into four Treasure tokens with Ashnod; sacrificing three Treasures to Knave's second ability draws two instead of one. Farid's nontoken-death Scrap production, rummaging and one Deathmantle combo are meaningful losses, but Knave's mana and no-tap doubled draw better support this token-sacrifice build. |
| City of Brass | Xander's Lounge | Immediate unconditional three-color mana avoids a turn-tapped land for casting UBR five-mana Ashnod; pay one damage when tapped, forgo cycling. |
| Mana Confluence | Exotic Orchard | Guarantees all Ashnod colors independently of opponents' land types, at one life per colored tap; improving commander access outweighs the life cost in this high-power shell. |

## New lines and rule caveats

- Spellbook 4131-4235: **Basalt Monolith + Rings of Brighthearth** — infinite colorless mana, with available activation-seeding mana.
- Spellbook 4131-5390: **Basalt Monolith + Forensic Gadgeteer** — infinite colorless mana after Basalt untap costs 2 and its tap produces 3.
- Spellbook 2829-3490-5346: **Arcbound Ravager + Animation Module + Crime Novelist** — unbounded token ETB/death/sac, Novelist counter growth when supplied initial artifact creature.
- Spellbook 2034-3490-5346: **Ashnod's Altar + Animation Module + Crime Novelist** — infinite colorless/red mana and sacrifice/death/ETB with artifact creature fuel.
- Spellbook 3490-4659-5346: **Animation Module + Krark-Clan Ironworks + Crime Novelist** — infinite colorless/red mana with artifact creature fuel.
- **Manually reasoned, not indexed:** Ashnod the Uncaring + Spawning Pit + Crime Novelist — Activate Spawning Pit sacrificing the creature. Ashnod copies the nonmana ability; both counters resolve for two charges. Create a 2/2 Spawn artifact creature for 1. Sacrifice that Spawn to the first Pit ability: two charges again, Crime Novelist adds R. Spend that R to create the next Spawn; loop. No infinite mana claim. Starting condition: A creature to sacrifice initially; if nonartifact, 1 starting generic mana; opponent interaction can interrupt; Ashnod and Crime Novelist remain in play.

Basalt Monolith makes **colorless** mana only. Infinite colorless is an engine, not automatically game-ending: Walking Ballista is deliberately retained as a deterministic outlet, alongside Retrofitter Foundry and sacrifice payoffs. Ashnod's trigger does not copy mana abilities or abilities of ordinary lands and does not retrigger merely because another ability was copied. Sacrificing during an activated ability's resolution (for example Goblin Welder) is not enough; it must be an activation cost.

## Finite mana and cost tradeoffs

Baseline 33 lands + 9 rocks = 42 static sources; Grok 33+7 = 40; Rev2 33+8 = 41. Hypergeometric P(>=5 static sources among first 11 cards from 99-card library): 53.74% baseline, 47.89% Grok, 50.83% Rev2. This measures early source access only. The new City of Brass and Mana Confluence never enter tapped and are unconditional UBR, while one of the two removed rocks remains a real cost.

## Open-ended alternatives (not padded)

- Audacious Reshapers for Ruthless Knave: Audacious Reshapers frees two random artifacts each tap with Ashnod, but has summoning sickness, self-damage and no guarantee of mana or payoff; Knave gives repeatable immediate four Treasures and doubled draw.
- Thopter Squadron for Spawning Pit: Thopter Squadron's Commander-specific lines are four-piece, five-mana and need Novelist plus Altar/KCI; Pit is two-mana and requires no taps, makes a smaller three-card loop.
- Weapons Manufacturing for Animation Module: Weapons Manufacturing yields Munitions for nontoken artifact ETBs and potential lethal damage; Animation Module enables three existing-inventory Spellbook loops with Ravager/Altar/KCI and Novelist, at one mana.
- Skullclamp for Dross Skullbomb: Skullclamp is efficient token draw; Skullbomb is a commander-doubled instant draw-two/recursion piece, one-mana artifact sacrifice fodder and has more direct commander identity.
- Sage of Lat-Nam for Priest of Forgotten Gods: Sage draws two with Ashnod, but Priest also produces four black mana, double edict/life loss and two draws while retaining creature fodder synergy.

Additional Mana Vault, Spire of Industry, Burnished Hart, Dross Scorpion cuts, Marionette Master, Mirkwood Bats, Voltaic Key, Sage of Lat-Nam, Thran Dynamo, Mindslaver, Transmutation Font and other card candidates were considered; none was supported as an additional strictly quality-positive full-100 swap. Jhoira, Fireweaver, Farid, and Duplicator are genuine value costs, not described as universally bad cards. The original Grok choice to sacrifice Walking Ballista was reversed because its infinite-colorless mana outlet becomes more important when Basalt is selected.

## Governance

Current Oracle snapshot covers 95 distinct selected names and exactly 100 physical cards; all recorded as Commander-legal and within Grixis identity on 2026-10-23 evidence. Six Game Changers; no known project exceptions; bracket 4, tags Ability Copy / Artifact Sacrifice / Artifact Combo. The source-bound finite tests and dedicated new M6 I/J bundle must pass at exact PR head before owner presentation. No owner approval is implied by a green CI. Keep canonical Ashnod historical lock untouched until Cory explicitly approves this exact file and raw SHA.
