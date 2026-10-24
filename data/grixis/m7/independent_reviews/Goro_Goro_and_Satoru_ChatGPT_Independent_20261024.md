# Goro-Goro and Satoru — independent ChatGPT M7 Rev1, 2026-10-24

**Status: RESEARCH CANDIDATE; NOT APPROVED OR CANONICAL.** Only Cory can approve the full exact 100 and raw hash. The 20 previous M7 locks stay unchanged.

## Provenance and five-substitution candidate

- Canonical 2026-10-14 approved baseline (read only): `refinement/decklists/Goro_Goro_and_Satoru_Approved_2026-10-14.txt`; raw SHA-256 `2fd39e3b39afaeb1bf394a59b392d8a29f28645776fa0b13c5754df67ab85fdf`.
- GrokBot [PR #669](https://github.com/corymstover/GrokBotMTGCompanion/pull/669) at `3d550c79...` produced just +Bitterblossom/-Mist-Syndicate Naga; the one-swap proposal is not owner-presentable.
- Independent Rev1 tested proposal raw SHA-256: `36b71b76f913c38503f6cd1a59ba9e29a5aab48d1d6b9fd4c29eba5b69775d5c`.
- Five swaps are the surviving *qualitative* alternatives here, **not a blanket claim that five is a cap**. Other routes were examined; no weak extra swap is included merely to increase the count.

| Add | Cut | Commander-specific improvement | What is lost |
|---|---|---|---|
| **Bitterblossom** | Mist-Syndicate Naga | A new flying body every upkeep, can attack under haste, works after sweepers | Life per upkeep; a Ninja body; 1/1 can be blocked by flyers |
| **Roaming Throne** | Grim Hireling | Choose **Human**: doubles Goro's fresh-damage triggers, Hanweir Garrison's attack-trigger tokens, Professional Face-Breaker's Treasure triggers and Satoru the Infiltrator's draw triggers | Independent Treasure production, Treasure-based shrink removal; four-mana creature vulnerability |
| **Hanweir Garrison** | Kaito, Bane of Nightmares | Two newly entered *tapped-and-attacking* Humans per attack; four if Throne chose Human; scales with extra combats and Tetsuko's 1-toughness evasion | Kaito's Ninja-ninjutsu, card selection/draw, hexproof, emblems, stun effect |
| **Misty Rainforest** | Crumbling Necropolis | Untapped Island-type dual access in early turns; can fetch Xander's Lounge if needed | 1 life; shock life when chosen; no unconditional no-cost UBR production |
| **Marsh Flats** | Fabled Passage | Untapped Swamp-type dual access, especially the crucial turn-three UBR window | 1 life, optional shock life; narrower typed targets than Fabled Passage's basics |

The **choice of Human** for Throne is crucial. It does not duplicate the Dragon Tempest enchantment trigger or automatically make an additional Dragon per 1/1; Goro triggers once per damaged *opponent* per damage step, then Throne adds one extra copy of that trigger. Example: if four Hanweir tokens enter tapped and attacking and connect with three *different* opponents while Goro and a Human-chosen Throne remain, Goro creates six Dragons (3 damage events × 2). If all four connect with a single player, it creates two Dragons—not eight. This is a conditional rules example, not a measured success rate.

**Owner-retained identity stays:** Bident of Thassa, Enduring Curiosity, Grazilaxx, Silver-Fur Master, Yuriko, both Satoru cards, Ninja of the Deep Hours, Moon-Circuit Hacker, Mistblade Shinobi, Thousand-Faced Shadow, Daring Piracy, Loyal Apprentice, Urabrask's Forge, Determined Iteration, Samut, Frostcliff Siege, Dragon Tempest, Terror of the Peaks, Rogue's Passage, Breath of Fury, Aggravated Assault, Karlach and Great Train Heist. The user-added October 14 cards are untouched.

## Challenged alternatives and caveats

- **Chandra, Acolyte of Flame / -Kaito** is staged as an exact second 100: its two hasty tokens appear immediately each turn and survive a creature-wipe turn while Chandra lives; however, the token-making 0 loyalty *activated* ability cannot be doubled by Roaming Throne, nor repeated in each extra combat. With Throne, Hanweir generates four per attack and more across extra combats. Hanweir wins strategic fit; Chandra may win when attacks and blockers are hard.
- **Keeping Kaito** is staged as the four-swap control, not owner-presentable under ordinary five-swap floor.
- **Bident** is retained because the old owner explicitly prized combat draw. **Fellwar Stone** and all other rocks retained to avoid destabilizing paid UBR on turn 3. **Grim Hireling** is not strictly weaker in all states: without Goro, it produces two treasures on *any* connecting group, while Throne needs another Human trigger to matter. **Kaito** has better card selection and ninjutsu.
- **Hanweir blockers:** freshly attacking 1/1 Humans are only evasive with Tetsuko (or a comparable evasion effect); if blockers absorb them, there are no Dragons. Roaming Throne alone doesn't make an attacker unblockable.
- **Fetchland mana:** Misty fetches Island types (Underground Sea, Watery Grave, Steam Vents, Volcanic Island or tapped Xander's Lounge); Marsh fetches Swamp types (Underground Sea, Watery Grave, Badlands, Blood Crypt or tapped Xander's Lounge). Early untapped duals require paying 1 life and sometimes 2 shock life. Crumbling's guaranteed all-color tap and Fabled's free basic are real costs lost.
- **EDHREC** commander-specific pages were used for discovery, never as a vote or authority. **Commander Spellbook** old Breath of Fury loops retained, no newly asserted unbounded loop.
- **No gameplay/win-rate claims.** The test suite checks mechanical deterministic scenarios, structural Oracle/legality, owners' keeps, source hashes, and mana-entry examples, not multiplayer games.

## Independent verification intent

- Proposed list: 100 physical cards (99 rows with 2x Island); one commander; 33 lands, 66 library nonlands, nonland average MV 2.50; 6 Game Changers unchanged; Bracket 4 Optimized; Ninjas / Dragons / Extra Combats.
- All 100 names resolve from Grok's frozen Scryfall 2026-10-23 pool (215 evaluated) and manually sourced Scryfall Oct24 addendum (Roaming Throne, Misty Rainforest, Marsh Flats); current legality and Grixis identity checked for addendum. Hanweir was already in frozen legal Oracle pool.
- Until full GitHub Actions checks pass, this is an engineered candidate, not verified owner-ready. Even after tests, Cory must approve its exact complete 100 and hash separately.
- Neither canonical registry nor prior locked decklist changes are permitted here.
