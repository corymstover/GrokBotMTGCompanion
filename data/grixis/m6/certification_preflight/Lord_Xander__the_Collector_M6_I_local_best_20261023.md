# Lord_Xander__the_Collector (Lord Xander, the Collector) — M6 I local-best memo for the M7 research candidate (2026-10-23)

This memo is evidence only. The candidate is NOT owner approved, NOT M6 certified and NOT owner-presentable. Its readiness is `RESEARCH_ONLY_WITHDRAWN_NOT_OWNER_PRESENTABLE` for two reasons:
- there are three genuine swaps, below the five-swap floor;
- the existing M6 Pass C Stage A seal does not match its file, so the shared J checker rejects any bundle for this deck. Expected `89a78d80…`, actual `826f0770…`, seal commit `bca97b98`. See the adversarial packet.

The canonical list is unchanged.

Scope: the eleven complete configurations in `data/grixis/m6/ij/tested_pools/Lord_Xander__the_Collector_M7_tested_configurations_20261023.json`, plus the named single-card contenders. Each configuration is 100 cards (1 commander and a 99-card library). This is not a global or statistical optimum.

Identity:
- Tracker Deck 30 (index 29), short key `Lord_Xander`. Deck ID `Lord_Xander__the_Collector`, commander Lord Xander, the Collector.
- The overrides (APPROVED / LOCKED, 2026-10-14) and the registry agree. Tracker row 29 sub-fields still read PENDING. That is disclosed, not changed.

Baseline:
- Canonical encyclopedia main 9b26aa28fc7e16f6652aaec292b4edf84e20db71, file `refinement/decklists/Lord_Xander_the_Collector_Approved_2026-10-14.txt`.
- Git blob 025aa284, introduced by canonical commit 214fd50 (2026-10-14). Registry source_commit 1836b97 has the same bytes.
- Raw SHA-256 92cdc2f9c1a3583ccf6a311679db66bef825dac2902761859e929f268b6b4787. It equals the overrides `approved_list_sha256` and the registry recorded hash, so no provenance exception is used.
- Logical hash lh1:84233c91…, the same as the registry Archidekt export (raw 26b1674f…).

## Commander text (frozen cache, identical on live Scryfall)
Lord Xander, the Collector ({4}{U}{B}{R} Legendary Creature — Vampire Demon Noble 6/6):
- enters: target opponent discards half their hand, rounded down;
- attacks: defending player mills half their library, rounded down;
- dies: target opponent sacrifices half their nonland permanents, rounded down.

Selection rule: a card earns a slot if it gets Xander back, keeps him safe without blocking the deck's own copy/death tricks, or turns one Xander event into more.

## Result
The candidate (raw 8dc20968…, lh1:51caa7ea…) is the canonical 100 with three swaps:

| # | Add | Cut | Confidence |
|---|---|---|---|
| 1 | Necromancy | Persist (EXPLICIT owner keep, FLAGGED) | MODERATE |
| 2 | Swiftfoot Boots | Lightning Greaves | MODERATE |
| 3 | Malakir Rebirth // Malakir Mire | Bojuka Bog | LOW_WITH_DISCLOSED_LIMITS |

Local best within the pool, by measure:
- **Recursion (grid B1):** Necromancy returns Xander in 12/36 cells. Goryo's Vengeance returns him in 8/36 and Persist in 4/36.
- **Own-targeting (grid B2):** Boots 44/44, Greaves 30/44.
- **Death enabler (grid B3):** Malakir and Bog tie 6/16.
- **Deployment cost:** P(Xander attack trigger) by turn 7 is 0.2978 for the baseline and 0.2897 for the candidate, all from Boots. Chrome Mox, Command Beacon and Glasspool Mimic do not beat the candidate beyond noise.
- **Kiki-Jiki:** staged, because it changes the combo identity (Spellbook 11 → 14).
- **Owner-keeping alternatives:** alt A and alt B are equal to the candidate on every bounded measure except the slot they cut. They are the right choice if the owner keeps Persist.

## Not claimed
No win rate, no source-bound engine receipt and no M6 certification. The I/J certificate in this PR is `blocked`, not `pass`.
