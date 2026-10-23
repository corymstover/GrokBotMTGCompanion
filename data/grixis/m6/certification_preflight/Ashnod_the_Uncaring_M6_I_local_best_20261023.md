# Ashnod the Uncaring — M6 I local-best memo for the M7 candidate (2026-10-23)

Evidence only. NOT owner approved, NOT M6 certification, canonical unchanged. Scope: the six complete 100-card
configurations in `data/grixis/m6/ij/tested_pools/Ashnod_the_Uncaring_M7_tested_configurations_20261023.json` plus
named single-card contenders. Not a global or statistical optimum.

## Result
The preferred five (raw b1078f08…, lh1:4ac4aed8…) is the local best of the tested pool:
+Corridor Monitor, +Aether Spellbomb, +Audacious Reshapers, +Priest of Forgotten Gods, +Thopter Squadron /
−Foundry Inspector, −Fellwar Stone, −Talisman of Indulgence, −Walking Ballista, −Esoteric Duplicator.

## Why
Ashnod copies every non-mana activated ability of an artifact or creature whose cost sacrificed a permanent (no turn
limit). The approved list was a strong artifact-sacrifice shell, but Commander Spellbook found none of its 15 combos
used Ashnod, and several slots (third cost reducer, two rocks, Walking Ballista) never trigger the commander. Each add has
a sacrifice-cost ability Ashnod doubles (Spellbomb bounce/draw, Reshapers two free artifacts, Priest four life/two edicts/
BBBB/two cards), and Corridor Monitor and Thopter Squadron create three Spellbook-listed Ashnod loops from incumbents
(1414-1649-2068-4404; 2034-2068-2762-5346; 2068-2762-4659-5346).

## Self-challenge
- Sage of Lat-Nam over Jhoira, Weatherlight Captain: alternative (six-swap, staged), not selected; Jhoira draws without Ashnod.
- Spire of Industry over Exotic Orchard: alternative (six-swap, staged), not selected; marginal, costs life.
- Seven-swap with both: staged, not selected (padding).
- Priest over Krark-Clan Shaman (keeping Walking Ballista): same-count alternative, rejected; Pass C defended Shaman as the copyable sweeper.
- Marionette Master, Voltaic Key, Manifold Key, Burnished Hart, Skullclamp, Courier's Capsule, Commander's Sphere,
  Mirkwood Bats, Fain, Mindslaver: rejected. Paradox Engine: banned.

## Limits
Finite rules cases only (tests/test_m6_ashnod_the_uncaring_m7_mechanics.py). No simulation or win-rate. Main losses:
Esoteric Duplicator's token copies and sacrifice draw, two rocks (static sources 42 → 40), Walking Ballista's flexibility,
Foundry Inspector's third cost reduction (its two Spellbook variants survive through Etherium Sculptor/Enthusiastic Mechanaut).
