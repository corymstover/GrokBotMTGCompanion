# Lord_Xander__the_Collector (Lord Xander, the Collector) — M7 rules snapshot (2026-10-23, America/Chicago)

Sources:
- Magic Comprehensive Rules 2026-09-25 (frozen cache `MagicCompRules-20260925.txt`, read-only).
- Frozen Scryfall rulings file `rulings-20261015090033.jsonl.gz` (read-only). It has rulings for Necromancy, Lightning Greaves, Swiftfoot Boots, Malakir Rebirth // Malakir Mire, Goryo's Vengeance, Seize the Day and Auton Soldier. It has **no rulings** for Lord Xander, the Collector, Persist or Bojuka Bog, so those rest on Oracle text and the Comprehensive Rules only.
- Candidate Oracle snapshot `data/grixis/m6/oracle_snapshots/Lord_Xander__the_Collector_M7_Scryfall_20261023.json` (live Scryfall `/cards/collection`, 2026-10-23). It has 0 oracle_id/text differences against the frozen 2026-10-16 oracle file for all 194 snapshot names, and 0 names missing.

This snapshot is evidence only. It is not owner approval.

## Deck ID, commander and legality
- Tracker deck #30 (index 29) `Lord_Xander`; the verified deck ID is `Lord_Xander__the_Collector` and the commander is **Lord Xander, the Collector**. The registry, overrides (APPROVED/LOCKED 2026-10-14) and the canonical source file agree on the raw SHA-256 92cdc2f9c1a3583ccf6a311679db66bef825dac2902761859e929f268b6b4787. Disclosed discrepancy, not changed: the tracker key is the short form `Lord_Xander` and the tracker row 29 sub-fields still read PENDING.
- **Lord Xander, the Collector** ({4}{U}{B}{R} Legendary Creature — Vampire Demon Noble 6/6; set `snc`, released 2022-04-29; oracle_id d17bfa94-5046-46ae-80af-be5d1d35af13) reads **commander: legal** on live Scryfall (2026-10-23) and is **not a Game Changer**. No preview caveat and no project exception applies.
- Every card in the baseline, the candidate and all staged alternatives reads commander-legal on live Scryfall and is within U/B/R. Evaluated and excluded: Sorin of House Markov // Sorin, Ravenous Neonate (identity B/W, outside U/B/R).
- Game Changers (live): baseline and candidate both carry the same **20** (Ancient Tomb, Cyclonic Rift, Demonic Tutor, Fierce Guardianship, Force of Will, Gamble, Grim Monolith, Imperial Seal, Jeska's Will, Lion's Eye Diamond, Mana Vault, Mystical Tutor, Notion Thief, Opposition Agent, Orcish Bowmasters, Rhystic Study, Tergrid, God of Fright // Tergrid's Lantern, The One Ring, Underworld Breach, Vampiric Tutor). The deck is **Bracket 4** (owner Bracket 4 Optimized); none of the selected adds is a Game Changer. Chrome Mox (rejected) would make it 21.

## Commander text (current Oracle)
- "When Lord Xander enters, target opponent discards half the cards in their hand, rounded down. / Whenever Lord Xander attacks, defending player mills half their library, rounded down. / When Lord Xander dies, target opponent sacrifices half the nonland permanents they control of their choice, rounded down."
- The deck re-uses all three triggers: clones (Spark Double, Phantasmal Image, Auton Soldier, Helm of the Host and similar) repeat the enters and attack triggers; sacrifice outlets (Altar of Dementia) and recursion repeat the dies trigger. CR 700.4: "dies" means put into a graveyard from the battlefield.

## Selected change 1: +Necromancy −Persist (FLAGGED: Persist is an explicit owner keep)
- Persist ({1}{B} sorcery): "Return target **nonlegendary** creature card from your graveyard to the battlefield with a -1/-1 counter on it." It can never return Lord Xander, the Collector (legendary) or any other legendary creature, and only from your own graveyard. It can return a nonlegendary clone card (for example Auton Soldier), which re-enters as a fresh copy.
- Necromancy ({2}{B} enchantment): "You may cast this spell as though it had flash. If you cast it any time a sorcery couldn't have been cast, the controller of the permanent it becomes sacrifices it at the beginning of the next cleanup step. ... Put target creature card from a graveyard onto the battlefield under your control and attach this enchantment to it. When this enchantment leaves the battlefield, that creature's controller sacrifices it."
  - It returns Lord Xander, the Collector (legendary) or any creature card from **any** graveyard (the commander mills opponents).
  - At instant speed on an opponent's end step, Lord Xander enters (discard trigger), Necromancy is sacrificed at the cleanup step (CR 514.3a lets triggers happen in cleanup), its leaves trigger sacrifices Xander, and Xander's dies trigger fires: one card for an enters trigger plus a dies trigger.
  - Ruling 2022-12-08: the cleanup sacrifice happens only when it is cast using its own flash permission.
  - Ruling 2005-08-01: it enters as an enchantment and then becomes an Aura.
- Pass C (owner-equivalent, NON-INDEPENDENT) named exactly this test and asked to confirm the net advantage against two-mana nonlegendary Auton recursion and two-mana Goryo's Vengeance haste burst. That comparison is grid B1 in the bounded measured tests.

## Selected change 2: +Swiftfoot Boots −Lightning Greaves
- Lightning Greaves: "Equipped creature has haste and shroud." Equip {0}. CR 702.18a: shroud means the permanent "can't be the target of spells or abilities", including your own.
  - Ruling 2020-08-07: "If Lightning Greaves is attached to the only creature you control, you won't be able to attach other equipment to it (or target it with anything else) until you have another creature to which you can attach Lightning Greaves."
  - In this deck, Greaves on Xander blocks equipping Sword of Feast and Famine, Blade of Selves or Helm of the Host to him (equip targets), and blocks Saw in Half, Molten Duplication, Feign Death, Hall of Echoes and Malakir Rebirth on him. Moving Greaves off him (Equip {0}, sorcery speed, onto another creature you control) strips his haste and shroud and can't be done in response to removal.
- Swiftfoot Boots: "Equipped creature has hexproof and haste." Equip {1}. CR 702.11b: hexproof stops only opponents' targeting, and CR 702.6a equip targets "creature you control", so the deck's own effects still work.
  - Cost: equip {1}, not {0}. Ruling 2018-03-16: one equipment can't give haste to two new creatures in the same turn.

## Selected change 3: +Malakir Rebirth // Malakir Mire −Bojuka Bog
- Malakir Rebirth ({B} instant): "Choose target creature. You lose 2 life. Until end of turn, that creature gains 'When this creature dies, return it to the battlefield tapped under its owner's control.'" On Xander in response to removal, or before an Altar of Dementia sacrifice, he dies (dies trigger) and returns (enters trigger). Malakir Mire is a tapped {B} land.
  - Rulings 2020-09-25: the effect works once; you lose no life if the target is illegal; play either face.
- Bojuka Bog: enters tapped, exiles target player's graveyard, taps for {B}. This is the deck's only maindeck graveyard-exile land. Its loss is disclosed: it hits Underworld Breach mirrors and reanimator, and the commander already fills opposing graveyards. The swap is the weakest of the three (grid B3 ties 6/6).

## Pass C requested tests and staged alternatives (not counted)
- Goryo's Vengeance ({1}{B} instant, Arcane): returns a **legendary** creature card from your graveyard with haste, then exiles it at the next end step. With Xander that gives an enters trigger and an attack trigger the same turn, but no dies trigger (exile), and nothing stays. Ruling 2018-12-07: if the creature leaves before the end step, it is not exiled.
- Seize the Day ({3}{R} sorcery, flashback {2}{R}): cast postcombat, it adds a combat in which the untapped Xander can be declared again. Rulings 2018-12-07: an illegal target means no extra phase; flashback keeps sorcery timing.
- Kiki-Jiki, Mirror Breaker: copies only **nonlegendary** creatures. It copies Auton Soldier or Spark Double already copying Xander (both nonlegendary copies), and it combines infinitely with Helm of the Host, Spark Double and Auton Soldier (Commander Spellbook).
- Auton Soldier (owner add) rulings 2023-10-13: myriad tokens enter attacking, so their own attack triggers don't fire. Enters triggers of the copied creature do fire.

## Combos
- Commander Spellbook find-my-combos (2026-10-23): **11** included combos in the baseline and the candidate, and in every staged alternative except Kiki-Jiki (14, adding 618-1692, 618-3908 and 618-5361). Almost-included: baseline 132, candidate 131. The selected swaps add and remove no included combo.
