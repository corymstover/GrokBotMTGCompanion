---
title: "Alela, Artful Provocateur — Living Weapon Assassins (Cory personal deck revision)"
category: edh
tags: [commander, esper, alela, equipment, living-weapon, assassin, personal, proposal]
generated_by: "human-directed review with GitHub companion data and first-party rulings"
sources: [scryfall-2026-10-15, wizards-rules, cory-original-list]
related: ["EDH Deck Evaluation Checklist.md", "EDH Deck Template.md"]
schema: 2
---

# Living Weapon Assassins — Alela, Artful Provocateur

**Status: UNAPPROVED PROPOSAL — not locked, not a member of the protected 62-deck Grixis Encyclopedia.**

- **Review date:** 2026-11-04 (America/Chicago)
- **Commander:** Alela, Artful Provocateur · white/blue/black · legendary creature, eligible under CR 903.3
- **Goal:** strong, identity-preserving Esper Equipment/Living Weapon deck with evasive assassin/poison pressure; no specified budget cap.
- **Original, byte-identical user attachment:** [source list](sources/alela-living-weapon-assassins-original-2026-11-04.txt) · SHA-256 `39a068221d08861c0520ec9792537702d6bca730c24716f8bb3e72bb119ae0ba`.
- **Revised Archidekt-ready candidate:** [100-card import](../../exports/personal/alela-living-weapon-assassins-2026-11-04.txt) · SHA-256 `38417683be19bad17239ce0baeba67cb20146f760e9b0ffdf9d7c21c3bcc3968`.
- **Ownership/approvals:** Proposed by ChatGPT after Cory asked for improvements. This is **not** an owner-approved SHA and does not change any historical approvals.

## Strategy and identity

Alela generates a 1/1 flying Faerie when an artifact or enchantment spell is **cast**, and gives other flying creatures +1/+0. The deck therefore wants (1) castable Equipment, (2) creatures and Germs that carry Equipment, (3) free/cheap attachment, and (4) enough draw and colored mana to keep casting. [Official Alela ruling](https://magic.wizards.com/en/news/feature/throne-eldraine-release-notes-2019-09-20).

The original package remains: Batterskull, Bitterthorn, Bonehoard, Drossclaw, Flayer Husk, Hylderblade, Kaldra Compleat, Lashwrithe, Mortarpod, Necropouncer, Nettlecyst, Scytheclaw, Skinwing, evasive carriers Blighted Agent/Invisible Stalker/Tormented Soul, and assassin pressure from Virulent Silencer/Winter Soldier. Also preserved: Ardenn, Arna, Forge Anew, Puresteel Paladin, Sram, Kíli, Sigarda's Aid, Simulacrum Synthesizer, Cranial Plating and Colossus Hammer. No intentional generic two-card infinite-combo shell was added.

Primary wins: equip unblockable/flying attackers for lethal damage; land a large Kaldra/Batterskull/Nettlecyst/Colossus Hammer threat; occasionally end a player with poison from Blighted Agent or Virulent Silencer plus qualifying nontoken artifact creatures. Alela's Faeries also supply combat pressure or Skullclamp fuel. This is not a dedicated all-in poison deck: ordinary Germ tokens and Faeries are **not** nontoken artifact creatures for Virulent Silencer's trigger.

## Swaps (15 one-for-one changes)

| Remove | Add | Evidence-based reason |
|---|---|---|
| Dark Ritual | Skullclamp | Replace one-shot black mana with a castable Equipment that converts Alela's expendable Faeries into two cards per equip. Alela's buff makes the 1/1 Faeries 2/1, and Skullclamp's +1/-1 kills them. |
| Diabolic Tutor | Stoneforge Mystic | Two-mana Equipment searcher with a repeatable {1}{W}, tap option to deploy expensive Equipment. Putting a Living Weapon onto the battlefield makes a Germ, but does **not** count as casting for Alela. [Official Stoneforge text](https://magic.wizards.com/en/news/feature/outlaws-of-thunder-junction-release-notes). |
| Banishing Light | Swords to Plowshares | One-mana instant creature answer; fewer sorcery-speed, enchantment-dependent removal bottlenecks. |
| Extinguisher Battleship | Hammer of Nazahn | Remove an eight-mana creature-sweeping Spacecraft that conflicts with the token board; add a lower-cost Equipment that attaches new Equipment and protects its carrier with indestructible. |
| Rewrite Regrets | Emry, Lurker of the Loch | Recur and **cast** artifact spells from the graveyard to keep Alela making Faeries, instead of a creature/Jace-token recursion package unrelated to Equipment. |
| Singularity Rupture | Teferi's Protection | Replace a six-mana symmetrical creature wipe/mill with an instant that preserves the assembled board against removal. |
| Unburial Rites | Steelshaper's Gift | Swap redundant, creature-only recursion for a one-mana tutor that finds the exact Equipment needed. |
| The Echoverse Fulcrum | Talisman of Progress | Replace the delayed seven-mana-total wipe (which destroys our creatures) with a two-mana white/blue rock, which triggers Alela when cast. |
| Return to the Light Realms | Talisman of Dominance | Replace a nine-mana mass reanimation payoff with early blue/black fixing; the deck still has Dance of the Manse, Forge Anew, Noctis, Anrakyr and Scour for Scrap as recovery/recursion. |
| Island | Hallowed Fountain | Fetchable white/blue source. |
| Island | Flooded Strand | Flexible fetchland for a Plains- or Island-typed source. |
| Plains | Godless Shrine | Fetchable white/black source; also retains the Swamp type for Lashwrithe. |
| Plains | Marsh Flats | Flexible fetchland for a Plains- or Swamp-typed source. |
| Swamp | Polluted Delta | Flexible fetchland for an Island- or Swamp-typed source. |
| Swamp | Urza's Saga | Colorless Saga land payoff: makes Construct carriers and finds mana-cost-{0}/{1} artifacts such as Sol Ring, Skullclamp, Flayer Husk or Colossus Hammer. |

## Structural assessment

- **100 cards total:** 1 commander, 99 main-deck cards; no duplicate nonbasic/non-exception names.
- **Lands:** 36 before and after; originals 29 basics + 7 nonbasics; revision 23 basics + 13 nonbasics. The land swaps improve fixing while protecting the original Equipment core.
- **Repeatable draw:** Skullclamp joins Sram, Puresteel Paladin and Kíli. The latter triggers from Equipment *entering*, including when cheated into play; Alela specifically needs a *cast*.
- **Early ramp:** Sol Ring and Arcane Signet are joined by two Talismans, supplementing Ancient Tomb/Foundry Inspector/Bitterthorn/Ashnod's artifact game plan.
- **Interaction:** Austere Command and Beyond the Quiet remain as board-reset options; Swords to Plowshares and Teferi's Protection increase instant-speed agency. The list may still need more stack interaction in a combo-heavy pod.
- **Provisional bracket:** **Bracket 3 (Upgraded)**. The repository's October 15 Scryfall-derived index flags two Game Changers: Ancient Tomb and Teferi's Protection. Estimated table power **about 6.5–7/10**, subjective, no goldfish/win-rate proof.
- **Rules subtlety:** Arna's token copies of Living Weapon Equipment enter attached to attackers, then their own Living Weapon triggers can move those Equipment to fresh Germs. Timing matters; do not assume every copied Equipment will remain attached to the original attacker. [Wizards MH3 rulings](https://magic.wizards.com/en/news/feature/modern-horizons-3-release-notes).

## Verification and bounds

`python3 -m unittest tests.test_personal_alela_living_weapon -v` passed 4 offline tests on 2026-11-04:

1. Exact original source SHA-256 retained.
2. Both lists exactly 100, one Alela commander, singleton except basics, intended Living Weapon core preserved.
3. All nine nonland swaps and six land substitutions accounted for; land count remains 36.
4. All candidate names resolve in the repository's **2026-10-15 pinned Scryfall index**; each is `legal` in Commander and its recorded color identity fits W/U/B.

The [current Wizards Commander banned list](https://magic.wizards.com/en/banned-restricted-list) and October 12, 2026 B&R announcement were also consulted. This is **not** a claim of a refreshed Scryfall bulk replay, full Commander Spellbook run, post-November releases, actual gameplay testing, or guaranteed optimality. No 62-deck Grixis approval, lore-deck approval, foundation checklist or release certificate was touched. Future owner approval should name the *exact revision file SHA-256*; edits require a new hash.
