# Ashad, the Lone Cyberman — M6 I local-best memo for the M7 candidate (2026-10-23)

Evidence only. NOT owner approved, NOT M6 certification, canonical unchanged. Scope: the six complete 100-card
configurations in `data/grixis/m6/ij/tested_pools/Ashad__the_Lone_Cyberman_M7_tested_configurations_20261023.json` plus
named single-card contenders. Not a global or statistical optimum.

## Result
The preferred five (raw dfd1158c…, lh1:672c3945…) is the local best of the tested pool:
+Skullclamp, +Piggy Bank, +Razorlash Transmogrant, +Necron Deathmark, +Royal Warden /
−Fellwar Stone, −Reckless Fireweaver, −Thoughtcast, −Marionette Master, −Thopter Spy Network.

## Why
Ashad copies the first nonlegendary artifact spell each turn only by sacrificing a power-2+ creature. The approved list had
ten 1-power creatures, and Thopter Spy Network makes 1/1 tokens, so the copy was often unavailable. The package raises
casualty-eligible creature cards from 17 to 21 (plus two 2/2 Warden tokens per Warden), adds Skullclamp draw and copyable
instant-speed removal, and creates a disclosed three-card conditional loop from incumbents (Spellbook 4050-4871-6429).

## Self-challenge
- Cyberman Patrol over Ichor Wellspring: alternative (six-swap, staged), not selected; Wellspring's card flow is worth more.
- Treasure Keeper (off-ranked) over Auton Soldier: alternative (six-swap, staged), not selected; Auton has the higher ceiling.
- Seven-swap with both: staged, not selected.
- Razorlash over Disciple of the Vault (keeping Thoughtcast): same-count alternative, rejected; Disciple is the loop payoff.
- Three Steps Ahead over Artificer Class, Missy over Cybermen Squadron, Dalek Drone over Cursed Mirror: rejected.

## Limits
Finite rules cases only (tests/test_m6_ashad_the_lone_cyberman_m7_mechanics.py). No simulation or win-rate. Main losses:
Marionette Master's drain, Spy Network's draw, one rock.
