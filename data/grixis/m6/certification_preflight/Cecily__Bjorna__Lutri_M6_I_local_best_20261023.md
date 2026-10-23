# Cecily, Haunted Mage + Bjorna, Nightfall Alchemist (companion Lutri) — M6 I local-best memo for the M7 candidate (2026-10-23)

This memo is evidence only. The candidate is NOT owner approved and NOT M6 certified, and the canonical list is unchanged.
Scope: the seven complete configurations in
`data/grixis/m6/ij/tested_pools/Cecily__Bjorna__Lutri_M7_tested_configurations_20261023.json` (each 100 = 2 commanders + 98
library, with 1x Lutri, the Spellchaser [Companion] outside the 100 where the file carries the companion line), plus named
single-card contenders. This is not a global or statistical optimum.

## Result
The preferred six (raw 2cc7227f…, lh1:514596aa…) is the local best of the tested pool:
- Adds: +Strionic Resonator, +Echo, Perceptive Prodigy, +Twenty-Toed Toad, +Sea Gate Restoration // Sea Gate, Reborn,
  +Deflecting Swat, +Mana Drain.
- Cuts: −Emry, Lurker of the Loch, −Goblin Engineer, −Sai, Master Thopterist, −Dark Deal, −Mana Geyser, −Seething Song.

## Why
Cecily draws one and loses one on attack, then, if we have eleven or more cards in hand as that trigger resolves, lets us cast
one instant or sorcery from hand for free. The approved list is built around holding ten cards before combat and converting
the trigger into Apex of Power, Mnemonic Deluge, In Garruk's Wake, Enter-the-library draws or Breach lines. However:
- Emry, Goblin Engineer and Sai are artifact-value creatures with little Cecily or Bjorna payoff in this list.
- Dark Deal shrinks our own hand below Cecily's eleven.
- Mana Geyser and Seething Song are one-shot rituals; the free cast already removes the mana problem for the big spell.

Each add is better in Cecily's specific engine:
- Strionic Resonator and Echo copy Cecily's attack trigger. Each copy draws again and checks hand size again on resolution,
  so a ten-card hand converts to two free casts instead of one (finite model in the mechanics test).
- Twenty-Toed Toad turns the big hand into a win (Commander Spellbook 1561-5850 with Peer into the Abyss), independent of Cecily.
- Sea Gate Restoration is a land in bad hands and a free-cast draw-hand-plus-one with no maximum hand size in good ones.
- Deflecting Swat (free with a commander out) and Mana Drain protect the attack turn; the deck had only Counterspell and
  Fierce Guardianship as stack interaction.

## Self-challenge
- **Five-swap floor without Mana Drain (Seething Song kept):** staged and rejected. Song's burst is one-shot; Drain protects
  the Cecily turn and its delayed mana pays for Lutri or post-combat spells.
- **Pass C's own challenger, Strionic Resonator over In Garruk's Wake (Emry kept):** staged as a six-swap and rejected. Pass C
  defended the one-sided nine-mana wipe as a top free-cast payoff; cutting Emry keeps it.
- **Enter the Infinite over Wheel of Misfortune:** seven-swap, staged, RETAIN_ALTERNATIVE, not selected. It is uncastable by
  hand and Peer + Toad already does the job.
- **Peter Parker's Camera over Lightning Greaves:** seven-swap, staged, RETAIN_ALTERNATIVE, not selected. A third copier is
  overkill and Greaves' haste lets Cecily attack the turn she lands.
- **Rejected:** Arcane Denial, Reliquary Tower (over Bojuka Bog), Gogo, Master of Mimicry (over Academy Manufactor),
  Spellbook (over Ichor Wellspring), Lithoform Engine, Double Vision, Veyran, Necrodominance, Fevered Suspicion (over In
  Garruk's Wake), Hit the Mother Lode, Swan Song, Wizard Class and Library of Leng (over Thought Vessel), Time Stretch (over
  Mnemonic Deluge), Galvanic Iteration and Whispersilk Cloak.

## Limits
Only finite rules cases are tested (tests/test_m6_bjorna_nightfall_alchemist_cecily_m7_mechanics.py). There is no simulation
or win-rate data.

Main losses:
- Emry/Engineer/Sai artifact recursion and Thopter value (creatures 16 → 15, artifacts 16 → 17).
- Dark Deal as a cheap symmetrical refill.
- Two red rituals (red pips 29 → 26) that could chain into Apex of Power by hand.
