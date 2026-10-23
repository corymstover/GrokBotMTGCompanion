# Garza Zol, Plague Queen — M7 rules snapshot (2026-10-23, America/Chicago)

Sources:
- Magic Comprehensive Rules 2026-09-25 (frozen cache `MagicCompRules-20260925.txt`, read-only).
- Frozen Scryfall rulings file `rulings-20261015090033.jsonl.gz` (read-only). Rulings are quoted for Kediss, Emberclaw Familiar, Inquisitor's Flail, Lizard Blades, Giantfall, Sink into Stupor // Soporific Springs, Fell the Profane // Fell Mire, Quietus Spike, Curiosity, Nibelheim Aflame, Rapid Hybridization, Takenuma, Abandoned Mire, Exotic Orchard and Fellwar Stone.
- Candidate Oracle snapshot `data/grixis/m6/oracle_snapshots/Garza_Zol__Plague_Queen_M7_Scryfall_20261023.json` (live Scryfall `/cards/collection`, 2026-10-23). It has 0 oracle_id/text differences against the frozen 2026-10-16 oracle file for all 218 snapshot names, and 0 names missing.

This snapshot is evidence only. It is not owner approval.

## Legality (recorded honestly)
- **Garza Zol, Plague Queen** (Coldsnap, set `csp`, released 2006-07-21) reads **commander: legal** on live Scryfall (2026-10-23).
  - Colour identity U/B/R; **not a Game Changer**. Long-released card; **no project exception applies to this deck.**
- Every card in the baseline, the candidate and all staged alternatives reads commander-legal on live Scryfall and is within U/B/R.
  - Evaluated discovery names outside U/B/R or not legal were excluded from the snapshot and are listed there; Jeweled Lotus is **banned** and was rejected.
- Game Changers (live): the baseline and the candidate both carry the same **9**:
  - Ancient Tomb, Cyclonic Rift, Demonic Tutor, Fierce Guardianship, Grim Monolith, Jeska's Will, Mana Vault, Rhystic Study, Vampiric Tutor.
  - No add and no cut is a Game Changer.
  - **Power Bracket 4 (Optimized)**, unchanged.

## Commander text (current Oracle)
- {4}{U}{B}{R} 5/5 Legendary Creature — Vampire Noble. "Flying, haste"
  - "Whenever a creature dealt damage by Garza Zol this turn dies, put a +1/+1 counter on Garza Zol."
  - "Whenever Garza Zol deals combat damage to a player, you may draw a card."

## Rules relied on
- **510.4 / 702.4b-c (double strike)**: with a first or double striker in combat there are two combat damage steps. State-based actions and triggers (Garza's draw, her +1/+1 counter, Curiosity, Kediss, Quietus Spike, Swords, Robe of the Archmagi) happen between them. Removing Garza or double strike during the first step stops the second hit (702.4c). The bounded test's "removal after first strike" row: double strike deals 5, Inquisitor's Flail 10.
- **704.5g / 704.5h**: lethal damage and deathtouch damage are checked as state-based actions before the +1/+1 counter trigger resolves. A 5/5 Garza trading with a 5/5 blocker in the same step dies. Under double strike she kills a 5/5 vanilla blocker in the first-strike step and takes no damage.
- **702.2b-c (deathtouch)**: Basilisk Collar or Quietus Spike makes any nonzero Garza damage lethal, including Giantfall's bite and Chandra's Ignition or Nova Flame damage. Each such death gives Garza a counter.
- **120.3b / 702.90b (infect)**: Grafted Exoskeleton makes Garza's damage poison counters. 704.5c: ten poison loses. At 7 power, double strike or Inquisitor's Flail gives 14 poison.
- **903.10a**: 21 combat damage from one commander loses. Bounded test: Inquisitor's Flail + Lizard Blades on a 6-power Garza deals 24 in one unblocked hit (2 × 12).
- **Inquisitor's Flail** rulings (2011-09-22): it doubles combat damage dealt *by and to* the creature; a second Flail multiplies by four; divided damage is doubled after division.
- **Lizard Blades / reconfigure (702.151a)** rulings (2022-02-18): reconfigure is not an equip ability; while attached Lizard Blades is not a creature, so creature sweepers and creature removal don't hit it. Unattached, it is a 1/1 double-strike creature.
- **Kediss, Emberclaw Familiar** rulings (2020-11-10): it triggers when a commander we control deals combat damage to an opponent. The extra damage is not combat damage, so it doesn't count as commander damage and doesn't retrigger Kediss. With double strike Kediss triggers once per strike step.
- **Curiosity** rulings (2011-09-22 / 2023-09-01): one draw per damage event to an opponent, combat or not. That includes Kediss's damage from Garza, so Curiosity draws for each opponent hit.
- **Quietus Spike** ruling (2008-10-01): life loss is computed when the trigger resolves; multiple triggers halve sequentially. Double strike gives two triggers, so an opponent at 40 goes to 6 (40 -> 35 after the first hit, minus half rounded up -> 17; -> 12 after the second hit, minus half -> 6). With Inquisitor's Flail it is 15.
- **Giantfall** ruling (2025-11-17): if either target is illegal as it resolves, our creature deals no damage. The damage comes from Garza, so her counter text applies.
- **Sink into Stupor // Soporific Springs** rulings (2024-06-07): a spell returned to hand is not countered, so this works against uncounterable spells. MDFC rules (712): it can be played as an untapped U land for 3 life.
- **Fell the Profane // Fell Mire** (MDFC, 712): an untapped B land for 3 life, or a {2}{B}{B} instant that destroys a creature or planeswalker.
- **Nibelheim Aflame** ruling (2025-06-06): the creature is the source of the damage. Not added; staged only.

## Combo and infinite boundaries (no unsupported claims)
- Commander Spellbook find-my-combos (2026-10-23): baseline 3 complete combos, candidate 3, the same ones. Almost-included 86 -> 86.
  - 3750-5039 The Reaver Cleaver + Aggravated Assault, and 900-3750 Sword of Feast and Famine + Aggravated Assault: both need Garza to connect each combat.
  - 2822-3681 Kediss, Emberclaw Familiar + Grafted Exoskeleton: each opponent gets the poison.
- No add creates or removes a combo. Lizard Blades only speeds up the Exoskeleton and commander-damage clocks; we claim no new infinite.
