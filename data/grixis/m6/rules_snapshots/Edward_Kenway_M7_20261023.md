# Edward Kenway — M7 rules snapshot (2026-10-23, America/Chicago)

Sources:
- Magic Comprehensive Rules 2026-09-25 (frozen cache `MagicCompRules-20260925.txt`, read-only).
- Frozen Scryfall rulings file `rulings-20261015090033.jsonl.gz` (read-only).
- Candidate Oracle snapshot `data/grixis/m6/oracle_snapshots/Edward_Kenway_M7_Scryfall_20261023.json` (live Scryfall `/cards/collection`, 2026-10-23).

This snapshot is evidence only. It is not owner approval.

## Legality (recorded honestly)
- **Edward Kenway** (Assassin's Creed, set `acr`, released 2024-07-05) reads **commander: legal** on live Scryfall (2026-10-23).
  - Colour identity U/B/R; **not a Game Changer**.
  - **No future-release or pending-legality project exception applies to this deck.**
- Every card in the baseline, the candidate and all staged alternatives reads commander-legal on live Scryfall and is within U/B/R.
  - Evaluated discovery names that are not legal or not U/B/R were excluded from the snapshot (listed there). No exception is applied.
- Game Changers (live): the baseline and the candidate both carry the same **10**: Ancient Tomb, Chrome Mox, Cyclonic Rift, Fierce Guardianship, Force of Will, Imperial Seal, Jeska's Will, Mana Vault, Mox Diamond, Vampiric Tutor.
  - No add is a Game Changer. Power Bracket 4.

## Commander text (current Oracle)
- {2}{U}{B}{R} 5/5 Legendary Creature — Human Assassin Pirate.
  - "At the beginning of your end step, create a Treasure token for each tapped Assassin, Pirate, and/or Vehicle you control."
  - "Whenever a Vehicle you control deals combat damage to a player, look at the top card of that player's library, then exile it face down. You may play that card for as long as it remains exiled."
- Identity: **tap Pirates, Assassins and Vehicles (attacking or crewing), cash the tapped count into Treasure at end step, and connect with Vehicles to steal cards for good.**

## Rules relied on
- **Edward ruling (2024-07-05):** a tapped permanent with more than one listed subtype is counted **once**. A Pirate Vehicle is one Treasure, not two.
- **Edward ruling (2024-07-05):** the exiled cards stay exiled face down indefinitely. "Play" lets us play lands within the normal land-play limit and cast spells with normal timing; we pay costs normally.
- **702.122a–c (crew):** crew taps "any number of other untapped creatures … with total power N or greater".
  - Over-crewing is legal, so extra Pirates and Assassins can be tapped for Edward's end-step count.
  - A crewed Vehicle is not tapped by crewing. It only counts for Edward if it is tapped (for example, by attacking without vigilance).
- **301.7a/b:** a Vehicle has power and toughness only while it is a creature.
  - **Brotherhood Vertibird ruling (2024-03-08):** its power counts all our artifacts, including itself.
- **702.9b (flying):** **Mu Yanling, Wind Rider** gives every Vehicle we control flying, so Edward's combat-damage trigger is harder to block.
  - Affected Vehicles: Smuggler's Copter, Jackdaw, Adrestia, Deluxe Dragster, Skysovereign, The Indomitable, The Belligerent, Subterranean Schooner, Nautiloid Ship, Luxurious Locomotive, Hoard Hauler, RMS Titanic, the Vertibird and Mu's own 3/2 crew-1 Vehicle token.
  - Mu's second ability ("one or more creatures with flying deal combat damage to a player") draws one card per combat damage step, not one per creature.
- **111.10a (Treasure)** and **701.16a / 111.10f (investigate, Clue)**: Treasures, Clues and Foods are artifact tokens.
  - This matters for Fateful Discovery (draw on each artifact entering), Brotherhood Vertibird (power), Time Sieve (sacrifice five artifacts) and Mirkwood Bats (each opponent loses 1 per token created **or** sacrificed).
- **Time Sieve ruling (2020-08-07):** Time Sieve may be sacrificed as one of its own five artifacts. Each activation needs five artifacts.
  - Urza's Saga cannot find Time Sieve: its mana cost is {U}{B}, not {0} or {1}.
- **Malcolm, the Eyes ruling (2024-04-12):** spells cast before Malcolm entered still count toward "your second spell each turn".
- **603.2d / Roaming Throne:** naming Pirate or Assassin doubles Edward's triggers. The count-once rule still applies.
- **704.5j (legend rule):** relevant for the rejected Double Down line (legendary token copies die). No add depends on it.

## Combo and infinite boundaries (no unsupported claims)
- **Malcolm, Keen-Eyed Navigator + Glint-Horn Buccaneer** (incumbents, unchanged): a **near-infinite multiplayer loop**.
  - It needs at least two opponents, Glint-Horn attacking, a card to discard and {1}{R} to start.
  - It is not a deterministic infinite in one-on-one.
- **Time Sieve lines** (Locomotive over-crew, Reaver Cleaver, Hoard Hauler, Edward plus Academy Manufactor): **repeatable extra turns only while five artifacts are recreated each turn**.
  - They are conditional on surviving permanents and on connecting or tapping enough creatures. They are not unconditional infinites.
- **Mirkwood Bats** adds finite drain per token event; it creates **no new complete combo**.
  - Commander Spellbook find-my-combos (2026-10-23): baseline and candidate have the **same 5** complete combos (Malcolm plus Glint-Horn, and the Time Sieve lines). Almost-included: 43 → 45.
- **Fateful Discovery's draws are compulsory.**
  - With Academy Manufactor, two tapped qualifiers make 6 artifact tokens, so 6 draws. Four qualifiers make 12 draws.
  - A small library can deck the controller. This is recorded in the bounded measured test.
