# Edward Kenway — M6 I local-best memo for the M7 candidate (2026-10-23)

This memo is evidence only. The candidate is NOT owner approved and NOT M6 certified, and the canonical list is unchanged.

Scope: the eight complete configurations in
`data/grixis/m6/ij/tested_pools/Edward_Kenway_M7_tested_configurations_20261023.json`, plus named single-card contenders. Each configuration is 100 = 1 commander + 99 library. This is not a global or statistical optimum.

Baseline: canonical encyclopedia main 9b26aa28, `refinement/decklists/Edward_Kenway_Approved_2026-10-14.txt` (blob 46df00ee, frozen by canonical commit 1e0b2e94); the registry source commit 1836b97 carries the same bytes. Raw SHA-256 a08d3bc9… equals the registry recorded digest (no provenance exception); logical hash lh1:fe8bb531… equals registry baseline_hash.

## Result
The preferred five (raw f3aad8e7…, lh1:875c30b2…) is the local best of the tested pool:
- Adds: +Mu Yanling, Wind Rider, +Brotherhood Vertibird, +Mirkwood Bats, +Spectral Sailor, +Malcolm, the Eyes.
- Cuts: −Breeches, Brazen Plunderer, −Imposter Mech, −Fellwar Stone, −Lotus Petal, −Captain Lannery Storm.

Five is the presentation floor, not a target. After the first five, eight further incumbents were challenged (Imperial Seal, Vaan, Coastal Piracy, Subterranean Schooner, Xander's Lounge, Hostage Taker, Smuggler's Copter, Port Razer); all were kept, and no card was added just to reach a count.

## Why (commander-first)
Edward Kenway ({2}{U}{B}{R} 5/5 Legendary Creature — Human Assassin Pirate): "At the beginning of your end step, create a Treasure token for each tapped Assassin, Pirate, and/or Vehicle you control. Whenever a Vehicle you control deals combat damage to a player, look at the top card of that player's library, then exile it face down. You may play that card for as long as it remains exiled." Each permanent counts once even if it has several of those types (ruling). Stolen cards stay playable indefinitely, under normal timing.

- **Mu Yanling, Wind Rider** ({2}{U}{U}): "Vehicles you control have flying" (702.9b) turns Edward's Vehicle-damage theft from occasional into usual. Only 5 of the candidate's 13 Vehicles fly on their own (4 of 13 in the baseline). She brings a 3/2 crew-1 Vehicle token and draws when fliers connect. **Breeches** (plain RETAIN) only exiles this turn, and that theft overlaps Edward, Vaan and Ramirez.
- **Brotherhood Vertibird** ({3}, flying, power = our artifacts, counts itself): an evasive Vehicle that Edward's Treasures grow. **Imposter Mech** depends on an opponent's creature and has crew 3.
- **Mirkwood Bats** ({3}{B} flier): each opponent loses 1 whenever we create or sacrifice a token, so Edward's Treasures, Manufactor's Clue/Food/Treasure and Time Sieve's five sacrifices become a drain. This is Pass C's priority card. **Fellwar Stone** (plain RETAIN) is the weakest durable rock: its colours depend on the opponents' lands.
- **Spectral Sailor** ({U} flash flying Pirate; {3}{U}: draw): a permanent tapped qualifier and Treasure sink. **Lotus Petal** is one-shot mana.
- **Malcolm, the Eyes** ({U}{R} flying haste Siren Pirate; investigate on our second spell each turn): attacks the turn it lands, so it is tapped for Edward that end step. Its Clues are artifacts for Fateful Discovery, Vertibird and Sieve. **Captain Lannery Storm** is a ground 2/2 (66% EDHREC inclusion, notable loss). Malcolm, the Eyes is not Malcolm, Alluring Scoundrel, which the owner rejected.
- Vehicles 13 → 13; Pirate/Assassin creatures 21 → 21; creatures 24 → 26; durable rocks 7 → 6.

## Owner direction
Every cut is a plain RETAIN line in the owner's 2026-10-14 ledger. **No explicit owner keep is overridden.** Fateful Discovery (explicit keep: "the artifact-entry draw engine") stays. Pass C's exact swap (+Bats / −Fateful Discovery) is staged as a complete 100, not selected. The owner-removed cards and rejected classes are not re-added: Sulfur Falls, Revel in Riches, Setzer, Mechanized Production; Magmatic Galleon, Reckoner Bankbuster, Mobilizer Mech, Malcolm, Alluring Scoundrel, tribal taplands (Path of Ancestry REJECT) and the rest.

## Pass C requested tests (bounded finite versions; not win rates)
These are in `data/grixis/m7/research_challengers/Edward_Kenway_bounded_measured_tests_20261023.json` and asserted in `tests/test_m6_edward_kenway_m7_mechanics.py`. Pass C #17's final disposition was **NEEDS TESTING**. The Pass C receipt is a NON-INDEPENDENT owner-equivalent (technical model independence FALSE).
1. **Castability, Bats {3}{B} vs Fateful {3}{U}{U}** (exact hypergeometric, lands plus durable rocks; 10/11/12 cards seen): baseline Bats 0.6839/0.7694/0.8364 vs Fateful 0.4191/0.5296/0.6307. Candidate: Bats 0.6597/0.7477/0.8179 vs Fateful 0.3937/0.5024/0.6037.
2. **Payoff plus Academy Manufactor both seen** (same for either payoff): 0.0093/0.0113/0.0136/0.0216 with 10/11/12/15 cards seen.
3. **End-step engine table** (deterministic, 3 opponents at 40): without Manufactor, k tapped qualifiers make k tokens, so k Fateful draws vs k drain per opponent. With Manufactor and 2 qualifiers: 6 compulsory draws (we lose if the library holds fewer than 6) vs Bats 6 per opponent, or 11 with a Time Sieve activation. With 4 qualifiers: 12 vs 12, or 17. Rows for fewer than five tokens repeat the no-Sieve values because Sieve needs five artifacts; the duplicate rows are intended.
4. **Mana:** strict turn-5 castability of Edward from lands plus durable rocks, play/draw: Petal counted 0.5538/0.6544 → 0.5025/0.6038; Petal excluded 0.5283/0.6295 → 0.5025/0.6038. The Pass C, Adrestia and four-swap alternatives equal the Petal-excluded baseline.

Not done, stated plainly: Pass C asked for matched seven-card hands against opponent interaction and blocker states, lethal turn and crewing opportunity cost. There is no validated opponent or game model, so no matched-shuffle playtest, win rate or lethal-turn distribution is reported.

## Self-challenge
- **Pass C exact swap (+Bats / −Fateful, keep Fellwar):** staged, RETAIN_ALTERNATIVE. Bats is castable more often and drains through blockers, but Fateful is an explicit owner keep.
- **Pass C secondary (+Bats / −Adrestia, keep Fellwar):** staged, RETAIN_ALTERNATIVE; it loses a Vehicle (13 → 12).
- **Four-swap without Bats (keep Fellwar):** staged, RETAIN_ALTERNATIVE (below the floor).
- **Five-swap with Chandra, Spark Hunter instead of Mu:** staged, RETAIN_ALTERNATIVE.
- **Six-swap with Eagle Vision over Imperial Seal:** staged, RETAIN_ALTERNATIVE.
- **Rejected singles:** Goldspan Dragon, Jhoira, Weatherlight Corsair, Reckless Fireweaver, Lydia Frye (and the other Assassin payoffs), Double Down, Timestream Navigator, Kitesail Freebooter, Warkite Marauder, Boosted Sloop, Cosima // The Omenkeel, Possession Engine, Phoenix Fleet Airship, Golden Argosy, Mutavault (and the other colourless creature lands), Path of Ancestry (owner-rejected class), Changeling Outcast, Kindred Discovery. Dragon's Smile was EXCLUDE_INVALID (not_legal).
- **Owner-removed classes:** none re-added.

## Limits
Only finite rules cases and exact enumerations are tested. Main losses: Breeches, Brazen Plunderer (50% EDHREC), Imposter Mech, Fellwar Stone, Lotus Petal and Captain Lannery Storm (66% EDHREC). Turn-5 castability falls about 0.026 on the play (Petal excluded). Game Changers 10 → 10 (Bracket 4). Average nonland MV 2.797 → 2.844. The castability model counts Cavern of Souls and Exotic Orchard as sources of every Grixis colour (an approximation: Cavern's coloured mana is creature-type restricted and Orchard depends on opponents' lands), so absolute castability figures are slightly optimistic for every list alike; the baseline-to-candidate comparison is unaffected because neither land changes.
