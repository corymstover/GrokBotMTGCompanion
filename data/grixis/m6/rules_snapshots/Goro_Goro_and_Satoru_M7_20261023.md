# Goro-Goro and Satoru — M7 rules snapshot (2026-10-23, America/Chicago)

Sources:
- Magic Comprehensive Rules 2026-09-25 (frozen cache `MagicCompRules-20260925.txt`, read-only).
- Frozen Scryfall rulings file `rulings-20261015090033.jsonl.gz` (read-only). Rulings are quoted for Goro-Goro and Satoru, Bitterblossom, Mist-Syndicate Naga, Redoubled Stormsinger, Dragon Tempest, Tetsuko Umezawa, Fugitive, Grazilaxx, Illithid Scholar, Bident of Thassa, Determined Iteration, Frostcliff Siege, Silver-Fur Master and Breath of Fury.
- Candidate Oracle snapshot `data/grixis/m6/oracle_snapshots/Goro_Goro_and_Satoru_M7_Scryfall_20261023.json` (live Scryfall `/cards/collection`, 2026-10-23). It has 0 oracle_id/text differences against the frozen 2026-10-16 oracle file for all 215 snapshot names, and 0 names missing.

This snapshot is evidence only. It is not owner approval.

## Legality (recorded honestly)
- **Goro-Goro and Satoru** (March of the Machine Commander, set `moc`, released 2023-04-21) reads **commander: legal** on live Scryfall (2026-10-23).
  - Colour identity U/B/R; **not a Game Changer**. Released card; **no project exception applies to this deck.**
- Every card in the baseline, the candidate and all staged alternatives reads commander-legal on live Scryfall and is within U/B/R.
  - Evaluated discovery names outside U/B/R or not legal were excluded from the snapshot and are listed there; Jeweled Lotus is **banned** and was rejected.
- Game Changers (live): the baseline and the candidate both carry the same **6**:
  - Ancient Tomb, Cyclonic Rift, Demonic Tutor, Fierce Guardianship, Jeska's Will, Vampiric Tutor.
  - Neither Bitterblossom nor Mist-Syndicate Naga is a Game Changer.
  - **Power Bracket 4 (Optimized)**, unchanged.

## Commander text (current Oracle)
- {U}{B}{R} 3/4 Legendary Creature — Goblin Human.
  - "Whenever one or more creatures you control that entered this turn deal combat damage to a player, create a 5/5 red Dragon Spirit creature token with flying."
  - "{1}{R}: Creatures you control gain haste until end of turn."

## Rules relied on
- **Goro-Goro and Satoru ruling (2023-04-14)**: the haste ability affects only creatures on the battlefield as it resolves. A Bitterblossom Faerie made in the upkeep is present in main phase 1, so one activation covers it; Dragons made later that turn do not gain haste.
- **Trigger count (603.2, "one or more")**: the Dragon trigger fires once per player dealt combat damage in a combat damage step by at least one creature that entered this turn. Extra combat phases (Breath of Fury, Great Train Heist) and double strike (Raphael, the Nightwatcher, 702.4) give additional damage events and so additional triggers.
- **Ninjutsu (702.49) and sneak**: a ninja put onto the battlefield tapped and attacking entered this turn, so it qualifies for Goro's trigger. Mist-Syndicate Naga ruling (2019-06-14): the ninja was never declared as an attacker. The Naga's copy token is created by its combat-damage trigger, i.e. **after** damage, so the copy cannot contribute to that combat's Goro trigger; it can only attack in a later extra combat (and needs haste).
- **Bitterblossom** rulings (2008-04-01): the upkeep trigger is mandatory; you lose 1 life even at 1 life. It makes a 1/1 black Faerie Rogue with flying each upkeep: a creature that "entered this turn" on our turn.
  - Dragon Tempest (Oracle): "Whenever a creature you control with flying enters, it gains haste until end of turn": the Faerie can attack the turn it is made with no mana spent. Otherwise Goro's {1}{R}, Samut, Hazoret's Champion or Frostcliff Siege (Temur) gives it haste.
  - Tetsuko Umezawa, Fugitive: a 1/1 Faerie has power 1 or less, so it can't be blocked (ruling 2018-04-27: changing power after blocks does not unblock).
  - Silver-Fur Master: the Faerie is a Rogue and becomes 2/2 (this removes the Tetsuko evasion, but it still flies). Prosperous Thief: a Rogue dealing combat damage makes a Treasure.
  - Determined Iteration (rulings 2024-01-12): populate may copy a Faerie token; the copy gains haste and entered this turn.
  - As an unblocked attacker the Faerie can be returned for ninjutsu, as can any 1-drop evasive creature.
- **Redoubled Stormsinger** rulings (2025-04-04): copies enter tapped and attacking but were never declared as attackers; it copies only tokens that entered this turn, so it adds nothing without a fresh token. It was tested and rejected.
- **Grazilaxx, Illithid Scholar** ruling (2021-07-23): the return-to-hand trigger is before damage; a returned creature deals no damage. **Bident of Thassa**: one optional draw per creature that connects.
- **Frostcliff Siege** ruling (2025-04-04): in Jeskai mode it triggers once per player dealt combat damage. In Temur mode it grants haste to all our creatures continuously, including Dragons and Faeries made later.
- **Breath of Fury** ruling (2005-10-01): it needs another creature to move to, or there is no untap and no extra combat. Bitterblossom gives a steady supply of receivers.

## Combo and infinite boundaries (no unsupported claims)
- Commander Spellbook find-my-combos (2026-10-23): the baseline and the candidate have the same 5 complete combos. All use Breath of Fury, with Loyal Apprentice (33-3259), Urabrask's Forge (1347-3259), Goro-Goro and Satoru (2237-3259), Determined Iteration (3259-3934) and Daring Piracy (1674-3259).
  - Each needs Breath of Fury's enchanted creature to connect every combat. They are combat-dependent, not instant two-card wins.
  - Almost-included counts are 142 for the baseline and 138 for the candidate. These are near-misses (one card short) shifted by the Mist-Syndicate Naga -> Bitterblossom swap; not decision-relevant.
- No add creates and no cut removes a complete combo.
