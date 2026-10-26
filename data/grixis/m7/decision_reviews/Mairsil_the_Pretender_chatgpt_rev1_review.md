# Deck #33 — Mairsil, the Pretender — M7 Rev1 six-swap owner candidate

**State:** READY FOR OWNER REVIEW ONLY. This is not owner-approved, not canonical, and not locked as an M7 replacement. The 2026-10-14 approved/locked version is untouched.
**Authority:** `corymstover/grixis-commander-encyclopediaGPT` main; `refinement/decklists/Mairsil_the_Pretender_Approved_2026-10-14.txt`.
**Baseline raw SHA-256:** `51e8fd18c7ded6744a4fa2f871925a0679f85dada3e6e517334bd13c07889ee5`.
**Selected M7 Rev1 raw SHA-256:** `fd5e44773c829311254193d5c6d4433676e787743249451cc37a7345b0cf83ad`.
**Owner requirement:** One ordinary "Approve" of the entire exact 100-card candidate authorizes routine scoped GitHub certification and canonical locking; no second approval should be demanded.

## Commander-first review

Mairsil's ETB cages a card **you own** that is an artifact or creature from your hand or graveyard. It acquires activated abilities of owned exiled cards with cage counters and restricts each original acquired ability to once per turn. The core therefore needs selective yard loading, repeatable cages, affordable haste/untap, activated-ability multiplication, draw/protection, and payoffs that exploit the omission of caged cards' nonactivated drawbacks. Not Grixis generic Oracle/Consultation turbo.

The entire 99 was reconsidered by role against prior Oct 14 closeout, Oct 16 M6 deep review PR #285, sealed Pass C PR #440, EDHREC Top/High Lift, and Commander Spellbook's Mairsil-specific lines. Protected core includes Aetherling, Anger, Essence Flux, Displacer Kitten, Pack Rat, Spark Double, Asmodeus, Quicksilver Elemental, Marvin, Gilded Lotus, Horseshoe Crab, Morphling, Endling, Rings, Staff, Tree of Perdition, Hateflayer, Walking Ballista, tutors, free interaction and major mana acceleration.

## Six selected exact replacements

| Add | Cut | Commander value / honest loss |
|---|---|---|
| Marsh Flats | Haunted Ridge | Untapped search for Swamp-typed Grixis dual/shock and flexible choice of colors; costs life, shuffles, vulnerable to search hate; loses safe later untapped BR dual. M6 #285/#440 already identified this. |
| Misty Rainforest | Shipwreck Marsh | Finds Island-typed Grixis dual/shock, fixing blue and another needed color now; costs life and search exposure; loses later untapped UB dual. Also identified by M6. |
| Riptide Laboratory | Sokenzan, Crucible of Defiance | Mairsil is a Wizard; {1}{U},{T} reclaims him to hand at instant speed, dodging removal or enabling more cage ETBs without commander tax. Loses a red source and channel Spirit token utility; the two fetches mitigate but do not erase the color cost. |
| Cavern Harpy | Cephalid Inkshrouder | When caged, Harpy's Pay 1 life: return this creature to hand becomes a low-resource Mairsil self-bounce/protection and hand-recast cage reset. Loses Inkshrouder's discard-a-card-to-shroud effect, which both protects and loads a graveyard; Harpy recasts cost {1}{U}{B}{R} for Mairsil and is not a free blink. |
| Agatha's Soul Cauldron | Omen Hawker | On battlefield, Cauldron lets mana be spent as any color for creatures' activated abilities; it also exiles creature cards from graveyards and can grant their activated abilities to your +1/+1-counter creatures, including Mairsil. Gains graveyard disruption and a separate ability engine, replacing Hawker's narrow one-mana activation-only accelerator. **Cauldron exiles are not cage counters**, so the engines do not automatically share their exiled pools. |
| Phyrexian Devourer | Torchling | Caged Devourer contributes library-exile-to-+1/+1-counters without importing its power>=7 sacrifice triggered ability; creates a substantial payoff with caged Hateflayer and supports existing counter/damage paths. Loses Torchling's red untap, redirection and combat manipulation. Morphling/Endling/Horseshoe Crab/Eater provide distinct backup untap; Devourer still needs Quicksilver or a new object for repeated activations in a turn. |

The two fetches are not presented as newly discovered: original M6 endorsed them but no owner approval was granted. The other four are a fresh strategic challenge. Six is quality-derived, not a compulsory count or ceiling.

## Adversarial alternatives and larger full-100 configurations

- **Seven-swap Sanctum**: Selected six **plus** `Sanctum of Eternity` / **minus** `Stormcarved Coast`, exact 100 SHA `7327154c34cdc34fd18f1bde36b096d10491000da946b3b36d775e9bb6e76f33`. Sanctum bounces commanders but only on your turn; the additional colorless land compounds the deck's early UBR fixing pressure. Riptide is already an instant-speed bounce slot.
- **Seven-swap Resonator**: Selected six **plus** `Strionic Resonator` / **minus** `Fellwar Stone`, exact 100 SHA `1e690ac39a8994635d2e72b47d15b8a7049b38ace92f1b3c4bfe1dcd0860950e`. Resonator copies cage ETB triggers, but removing another colored two-mana accelerator makes casting the commander on curve less dependable.
- **Pili-Pala** vs retained Morphling/Horseshoe Crab: another untap route but expensive and redundant against the already compact Quicksilver/Gilded Lotus lines; does not justify reducing interaction or mana.
- **The One Ring** vs Cauldron: enormous generic draw and temporary safety, but less Mairsil-specific activity than ability color-fixing, +1/+1 sharing and opponent graveyard exile.
- **Necrotic Ooze** vs Marvin/Cauldron: strong alternate static ability engine, but Mairsil's cage exiles the best creature payloads out of the graveyard, weakening Ooze's pool. No clear net improvement at an existing protected slot.
- **Lightning Greaves vs Swiftfoot Boots**: Hexproof allows self-targeting by Quicksilver whereas Greaves shroud obstructs it. Boots requires equip {1}; with zero equip and faster haste, Greaves was held while combo setup can move equipment first. Not claimed to be a strictly stronger keep.
- No generic Thoracle/Consultation, faster ritual packages, or unrelated Grixis goodstuff takeover.

## Rules, structure and limits

- Exact text: 100 lines, 100 distinct names, Mairsil first and unique [Commander], 32 land faces, no companion, singleton PASS. Exactly six additions and six cuts relative to baseline.
- New card color identities are all UBR-compatible: Harpy UB, Cauldron/Devourer colorless, fetches and Laboratory lands colorless. Frozen Oct 14 100-card Oracle/legality audit plus live Oct 25 Scryfall added-card rulings and Wizards' current Commander ban list were cross-checked; zero exceptions.
- Mairsil's own once-per-turn restriction still applies to each acquired original ability. Quicksilver grants additional instances, not removal of printed restrictions; target/self-copy and priority/timing requirements matter. Marvin does not inherit Mairsil's static restriction, only his activated abilities; do not confuse either with infinite mana in isolation.
- Cavern Harpy ETB triggered bounce is **not** inherited; only the activated pay-life self-return is. Riptide requires untapped land and a legal Wizard target.
- Agatha's Cauldron's on-board static text is **not** gained if the Cauldron itself is caged. Its exiled cards are separate from Mairsil's cage-counted cards.
- Phyrexian Devourer's triggered sacrifice is **not** inherited from a caged card. The deck still has to use the granted activated ability legally under Mairsil's per-turn restriction; exiling the whole library automatically is not asserted.
- At the selected 32 lands, swapping Sokenzan's red output for colorless Laboratory remains a real risk despite two new fetches. If further testing disproves this trade, revise the candidate and SHA before requesting owner approval.
- Oracle pages and live community research: https://scryfall.com/card/pls/97/cavern-harpy ; https://scryfall.com/card/woe/242/agathas-soul-cauldron ; https://scryfall.com/card/me2/216/phyrexian-devourer ; https://scryfall.com/card/jmp/494/riptide-laboratory ; https://edhrec.com/commanders/mairsil-the-pretender ; https://commanderspellbook.com/card/5112/ ; https://magic.wizards.com/en/banned-restricted-list .
- No measured multiplayer win rate, no independent third model, and no fresh M6 I/J *sealed* evidence transfer asserted. Comparisons here are finite rules/whole-list and structural audits.

**Disposition:** M7 Rev1 6-swap candidate, **Power Bracket 4 — Optimized**, Archidekt tags **Cage Toolbox / Activated Abilities / Combo**. Owner approval **PENDING**; canonical Oct 14 locked Mairsil unmodified.
