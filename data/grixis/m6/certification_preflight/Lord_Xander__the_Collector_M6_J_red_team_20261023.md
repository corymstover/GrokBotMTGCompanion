# Lord_Xander__the_Collector (Lord Xander, the Collector) — M7 red-team memo (2026-10-23)

1. **Seal blocker (stated first).**
   - The existing Pass C Stage A seal (`seal.json`, commit `bca97b98`) records `stage_a.md` SHA-256 `89a78d80…5a879d1`.
   - The committed file (commit `6ebb511e`, blob `e97d35fe`, unchanged since) hashes to `826f0770…a4cd0322`.
   - The shared checker therefore rejects the bundle. This PR does not edit the seal, the Stage A files or the checker; the owner must decide on a re-seal or a correction exception.
2. **Commander text: attack this first.**
   - Enters: half the hand. Attacks: half the library. Dies: half the nonland permanents. All rounded down.
   - Copies that enter tapped and attacking were not declared as attackers, so they get no attack trigger.
   - With Bruvac the Grandiloquent, an odd library leaves one card, and an empty library loses only on a draw (Pass C correction, accepted).
3. **Necromancy over Persist (swap 1, FLAGGED owner-keep override).**
   - Persist reads "target nonlegendary creature card", so it cannot return Xander. Necromancy can, from any graveyard.
   - Flash use: the enchantment is sacrificed at the next cleanup step (CR 514.3a; ruling 2022-12-08) and the creature is sacrificed with it, which gives a dies trigger. It gives no haste.
   - Risks: removing the enchantment kills Xander at a bad time; graveyard hate in response fizzles it (CR 608.2b); costs {2}{B} against {1}{B}.
   - Persist-only cells: 2/36 (only two mana, a nonlegendary target).
   - Owner-keeping alternatives A and B are complete 100s.
4. **Swiftfoot Boots over Lightning Greaves (swap 2).**
   - Greaves' shroud blocks the deck's own targeting of Xander: equip, Saw in Half, Molten Duplication, Feign Death, Hall of Echoes and Malakir Rebirth (ruling 2020-08-07).
   - Moving Greaves off Xander is sorcery speed and strips his protection. This is encoded conservatively in grid B2 (Greaves 30/44, Boots 44/44).
   - Cost: same-turn haste 22/44 against 44/44. Attack-trigger probability by turn 7 drops by 0.81 points.
   - Hall of the Bandit Lord remains a haste source.
5. **Malakir Rebirth over Bojuka Bog (swap 3, weakest).**
   - Grid B3 ties 6/6.
   - Loss: the deck's only maindeck graveyard exile, against reanimator and Underworld Breach mirrors.
   - Both lands enter tapped. Malakir costs 2 life on the spell side.
   - Xander must be left in the graveyard (not moved to the command zone) for the return.
6. **Pass C items (bounded).**
   - Goryo's Vengeance: retained alternative. It is exiled at end step, so it gives no dies trigger unless Altar of Dementia sacrifices Xander first.
   - Seize the Day: rejected against Karlach.
   - Auton Soldier myriad tokens never "attacked" (ruling 2023-10-13).
7. **Combo / bracket.**
   - Spellbook included combos 11 → 11. No infinite is claimed for any add.
   - Kiki-Jiki would add three (618-1692 Helm of the Host, 618-3908 Spark Double, 618-5361 Auton Soldier), so it is staged only.
   - Game Changers 20 → 20. Bracket 4.
8. **Owner direction.**
   - One explicit owner keep is overridden (Persist), and it is flagged.
   - No owner add (Auton Soldier, Phantasmal Image, Cruel Calculations, Hall of Echoes) is cut.
   - No removed card or rejected class is re-added. Glasspool Mimic was rejected as the owner-rejected clone class.
9. **Non-independence.** The Pass C reviewer (alias Josh-Lee-Kwai) is `technically_independent=false` under `OWNER_WAIVED_FOR_FORMAL_PASS_C`, and disclosed prior exposure to the Necromancy/Persist pair.
