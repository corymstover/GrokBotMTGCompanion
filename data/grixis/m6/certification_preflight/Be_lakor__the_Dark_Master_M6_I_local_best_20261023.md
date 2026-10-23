# Be'lakor, the Dark Master — M6 I local-best memo for the M7 candidate (2026-10-23)

This memo is evidence only. The candidate is NOT owner approved and NOT M6 certified, and the canonical list is unchanged.
Scope: the six complete 100-card configurations in
`data/grixis/m6/ij/tested_pools/Be_lakor__the_Dark_Master_M7_tested_configurations_20261023.json`, plus named single-card
contenders. This is not a global or statistical optimum.

## Result
The preferred five (raw 62a96b4f…, lh1:41e4055c…) is the local best of the tested pool:
- Adds: +Desecration Demon, +Kindred Dominance, +Demonlord Belzenlok, +Reaper from the Abyss, +Herald's Horn.
- Cuts: −Dream Devourer, −Blasphemous Act, −Rakdos, Patron of Chaos, −Bloodthirster, −Fellwar Stone.

## Why
Be'lakor turns every other Demon's entry into damage equal to its power (Lord of Torment) and draws one card per Demon when he
enters (Prince of Chaos). The approved list is a strong Demon shell. However:
- Dream Devourer enters as a 0-power Demon, so its Lord trigger deals 0.
- Blasphemous Act destroys our own Demon board.
- Rakdos, Patron of Chaos lets opponents choose to sacrifice instead of giving us cards.
- Bloodthirster's extra combat does nothing with Be'lakor.
- Fellwar Stone's colors depend on opponents.

Each add is better in Be'lakor's specific engine:
- Desecration Demon is a 6-power hit at 4 mana.
- Kindred Dominance, naming Demon, is a one-sided wipe.
- Belzenlok's ETB (and any Molten Echoes, Spark Double or Rite copy) digs for nonlegendary cards. It is also a 6-power hit.
- Reaper gives repeatable morbid removal and is a 6-power hit.
- Herald's Horn makes Demons cheaper and reveals Demons into hand.

## Self-challenge
- **Herald's Horn over Heartless Summoning (keeping Fellwar Stone):** a same-count alternative, staged and rejected. Removing
  −1/−1 adds 1 damage per hit, but Heartless's −2 on every creature spell is the stronger ramp.
- **Secluded Courtyard over Exotic Orchard:** six-swap, staged as an alternative and not selected. Courtyard is better for Demons
  but adds no colored mana to the noncreature spells (Rite, Mana Drain, Cyclonic Rift).
- **Lord Xander, the Collector over Lord of Change:** six-swap, staged as an alternative and not selected. Xander is a 6/6
  hand/library/permanent mill in the copy suite, but it costs 7 against Lord of Change's draw three and ward 2.
- **Seven-swap with both:** staged and not selected, because it would be padding.
- **Rejected:**
  - Harvester of Souls, Bloodgift Demon and Ob Nixilis, Captive Kingpin over Kardur.
  - Abyssal Persecutor, which blocks Liliana's Contract.
  - Archfiend of the Dross, which loses the game when its counters run out.
  - Varragoth, Razaketh, Quicksilver Amulet, Jet Medallion and Rhystic Study.
  - Displacer Kitten over Warstorm Surge (a Pass C challenger; Kitten is not a Demon).

## Limits
Only finite rules cases are tested (tests/test_m6_belakor_the_dark_master_m7_mechanics.py). There is no simulation or win-rate data.

Main losses:
- Blasphemous Act as a cheap emergency reset. Kindred Dominance costs 7, and Act costs 9 with affinity for creatures.
- The extra combat.
- Rakdos's 6-power body at 6 MV.
- Fellwar Stone (rocks 7 → 6).
- Dream Devourer's foretell discount.
