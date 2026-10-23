# Edward Kenway — ChatGPT adversarial review packet (M7, 2026-10-23)

**Status:** REVIEW CANDIDATE — NOT APPROVED, NOT CANONICAL. REVIEW_READY_NOT_OWNER_APPROVED. Only Cory can approve.

**Reviewer instruction:** attack this list. Show any of the following:
- a rules error;
- an illegal card;
- an unpayable line;
- an unsupported combo claim;
- a candidate that clearly beats an incumbent;
- an owner-direction contradiction we missed.

No win rates were measured, and EDHREC prevalence is discovery evidence only.

## Provenance
**Canonical source (read-only).**
- Repository `corymstover/grixis-commander-encyclopediaGPT` main `9b26aa28fc7e16f6652aaec292b4edf84e20db71`.
- File `refinement/decklists/Edward_Kenway_Approved_2026-10-14.txt`, git blob `46df00ee`, frozen by canonical commit `1e0b2e94`.
- Canonical commit record: the bytes were fetched and verified at 9b26aa28. The registry's source commit field says `1836b97`, the import commit, which carries the same bytes.
- Raw SHA-256 `a08d3bc9c283415f1579c493eccb3febd7d10dea3777bf3dc50cfbc0dbed4019`. This equals `state/current_deck_overrides.json` `approved_list_sha256`, the tracker (Deck #17, index 16) and the registry `recorded_sha256`.
- Vendored byte-exact at `data/grixis/m7/baseline_sources/Edward_Kenway_approved_source_2026-10-14.txt`.

**Hashes.** The registry `recorded_sha256` equals the raw bytes, so **no provenance exception** is used.
- Logical hash `lh1:fe8bb5317dbf183c3b20d6c5582ac4f2243f0e7c890e4687161c1725a1dc936c`.
- The registry export `exports/grixis-archidekt/edward-kenway.txt` (raw `1e8b8ea5e52e2ea499f07f0d72cbc4305b81cfbf370a163d1378dacc01690b9b`) is the same 100 in export format, with the same logical hash.

**Discrepancies.** None in the hashes. The candidate is written commander-first, then alphabetical.

**Count convention.** 100 = 1 commander + 99 library; no companion.
- 35 lands: Island ×2, Swamp ×2, Mountain ×1, plus 30 nonbasic (98 rows including the commander).
- Rocks: Sol Ring, Arcane Signet, Mana Vault and three Talismans in both lists; Fellwar Stone and Lotus Petal only in the baseline.

**Candidate.** `data/grixis/m7/candidate_lists/Edward_Kenway.txt`: commander first, then alphabetical; five substitutions.
- Raw `f3aad8e7da61996f27f423b6f0a2c7b33ea68acd9afbd57fb5e8a368b4a88aad`.
- Logical `lh1:875c30b2bac93448e125846441d3ffc6d682f1671463efcbaceb83f3229d14f4`.

**Live data.** Live Scryfall `/cards/collection` was queried on 2026-10-23 (09:53 CDT) for the 98 baseline rows and 160 evaluated names.
- The live results are stored only in the candidate snapshot and the research files; the frozen cache was not written.
- Oracle text and oracle_id show zero differences against the frozen `oracle-cards-20261016090200` snapshot for all 250 snapshot names.
- Dragon's Smile (`mbc`, released 2026-10-19) reads `not_legal` on live Scryfall and is EXCLUDE_INVALID. Off-colour names were dropped.

**Legality.** Edward Kenway (Assassin's Creed `acr`, released 2024-07-05) is Commander-legal on live Scryfall and is not a Game Changer. Every card in all eight configurations is legal and within UBR. **No project exception is used.**

**Game Changers.** 10 in the baseline and the candidate: Ancient Tomb, Chrome Mox, Cyclonic Rift, Fierce Guardianship, Force of Will, Imperial Seal, Jeska's Will, Mana Vault, Mox Diamond, Vampiric Tutor. **Power Bracket 4.**

**Archidekt tags.** Vehicles, Pirates, Treasure.

## Commander model (attack this first)
**Edward Kenway** is a {2}{U}{B}{R} 5/5 Legendary Creature — Human Assassin Pirate. Its Oracle text: "At the beginning of your end step, create a Treasure token for each tapped Assassin, Pirate, and/or Vehicle you control. Whenever a Vehicle you control deals combat damage to a player, look at the top card of that player's library, then exile it face down. You may play that card for as long as it remains exiled."

Rules points:
- **Edward ruling.** A tapped permanent with several of the listed types counts once. Stolen cards stay playable indefinitely, with normal timing and the normal land drop.
- **702.122a–c.** Crewing taps creatures, and over-crew is legal, so crewing Pirates and Assassins still count. The crewed Vehicle counts only if it is tapped (attacking without vigilance).
- **702.9b.** Mu Yanling gives all our Vehicles flying, so Edward's Vehicle-damage theft connects past ground blockers.
- **301.7a/b.** Brotherhood Vertibird has power (number of our artifacts, itself included) only while crewed.
- **111.10a / 701.16a.** Treasures and Clues are artifact tokens. They feed Fateful Discovery, Vertibird, Time Sieve and Mirkwood Bats (each opponent loses 1 per token created or sacrificed).
- **603.2d.** Roaming Throne naming Pirate or Assassin doubles Edward's triggers.
- **704.5j.** Relevant only to the rejected Double Down line.

## Swaps (5 — the floor; eight post-floor challenges, no sixth swap)
| Add | Cut | Why |
|---|---|---|
| Mu Yanling, Wind Rider | Breeches, Brazen Plunderer | All Vehicles fly, so Edward's theft connects; she brings a crew-1 Vehicle token and draws when fliers connect. Breeches' theft lasts only this turn and overlaps Edward, Vaan and Ramirez. Breeches is in 50% of EDHREC Edward decks. |
| Brotherhood Vertibird | Imposter Mech | A flying Vehicle whose power counts Edward's Treasures. Imposter depends on an opposing creature and has crew 3. |
| Mirkwood Bats | Fellwar Stone | Pass C's priority card: every Treasure, Clue, Food and Time Sieve sacrifice drains each opponent. Fellwar is the weakest durable rock. |
| Spectral Sailor | Lotus Petal | A {U} flash flying Pirate (EDHREC Edward general 2879/13036, about 22%) (permanent tapped qualifier) and a Treasure sink. Petal is one-shot mana. |
| Malcolm, the Eyes | Captain Lannery Storm | Absent from the optimized EDHREC page (general 1213/13036). A flying, hasty Pirate tapped for Edward the turn it lands, plus Clues on our second spell. Lannery is a ground 2/2 and is in 66% of EDHREC Edward decks, a notable loss. Not Malcolm, Alluring Scoundrel (owner-rejected). |

**Net:**
- Lands 35 → 35; coloured land sources U21 B20 R19 unchanged.
- Vehicles 13 → 13 (natively flying 4 → 5; all 13 with Mu). Pirate/Assassin creatures 21 → 21 (including Edward). Creatures 24 → 26.
- Durable rocks 7 → 6, and no Petal. Strict turn-5 Edward castability (Petal excluded) 0.5283/0.6295 → 0.5025/0.6038 on the play/draw.
- Average nonland MV 2.797 → 2.844.

**Owner direction.** No explicit owner keep is cut; all five cuts are plain RETAIN lines in the owner's 2026-10-14 ledger. Fateful Discovery (explicit keep) and Imperial Seal stay.

**Losses:** Breeches (50% EDHREC), Imposter Mech, Fellwar Stone, Lotus Petal and Captain Lannery Storm (66% EDHREC).

## Pass C requested tests (bounded; `tests/test_m6_edward_kenway_m7_mechanics.py::PassCBoundedMeasuredTests`)
- **Castability, Bats {3}{B} vs Fateful {3}{U}{U}** (exact hypergeometric, lands plus durable rocks; 10/11/12 cards seen):
  - Baseline: Bats 0.6839/0.7694/0.8364 vs Fateful 0.4191/0.5296/0.6307.
  - Candidate: Bats 0.6597/0.7477/0.8179 vs Fateful 0.3937/0.5024/0.6037.
- **Payoff plus Academy Manufactor both seen:** 0.0093/0.0113/0.0136/0.0216 with 10/11/12/15 cards seen.
- **End-step engine table** (deterministic, 3 opponents at 40): with Manufactor and 2 qualifiers, Fateful makes 6 compulsory draws (we lose if the library has fewer than 6) vs Bats draining 6 per opponent, or 11 with one Time Sieve activation. With 4 qualifiers: 12 vs 12, or 17.
- **Mana:** see Net. The Pass C, Adrestia and four-swap alternatives equal the Petal-excluded baseline.

**Not done.** Pass C asked for matched seven-card hands against opponent interaction and blocker states, plus lethal turn and crewing opportunity cost. There is no opponent model and no matched-shuffle or multiplayer simulation, so no success rates, lethal turns or win rates are reported.

## Combos (Commander Spellbook find-my-combos, both lists, JSON in research_challengers)
- Baseline and candidate: the **same 6 included combos**.
  - Malcolm, Keen-Eyed Navigator + Glint-Horn Buccaneer: near-infinite damage. It needs at least two opponents, Glint-Horn attacking and a card to discard.
  - Five Time Sieve lines (with Edward, Hoard Hauler, The Reaver Cleaver, Luxurious Locomotive, or Malcolm + Academy Manufactor). Spellbook labels them infinite turns. They need five artifacts to sacrifice on every extra turn, so they are conditional, not unconditional.
- Almost-included lines: 43 → 45. Mirkwood Bats adds finite drain and no new complete combo. **No new infinite is claimed.**

## Adversarial scenarios (please push here)
1. **Edward removed.** The fallbacks are the counter suite (Force of Will, Fierce Guardianship, Mana Drain, Swan Song, Deflecting Swat), Siren Stormtamer and Otawara. Malcolm, Keen-Eyed Navigator, Vaan, Ramirez and Bats still produce value from Treasure.
2. **Mu Yanling removed.** Five Vehicles still fly on their own. Is the staged Chandra five-swap (animation, no evasion) better against spot removal?
3. **Mana.** Cutting Fellwar Stone and Petal costs about 0.026 of turn-5 Edward castability. The four-swap keeps Fellwar.
4. **Pass C exact swap.** Bats over Fateful Discovery is better on castability and is safe from decking. Fateful is an explicit owner keep, so the swap is staged, not selected. Should it be?
5. **Compulsory draws.** Fateful stays. With Manufactor, 12 draws from 4 qualifiers can deck us late.
6. **Owner-removed classes.** Sulfur Falls, Revel in Riches, Setzer, Mechanized Production, Magmatic Galleon, Reckoner Bankbuster, Mobilizer Mech, Malcolm, Alluring Scoundrel, tribal taplands and the rest of the 2026-10-14 rejections are not re-added.
7. **Pass C disposition.** Pass C was owner-equivalent; a genuinely independent model was **NO** (technical model independence FALSE). Its final disposition was **NEEDS TESTING**. Both Bats hypotheses are staged as complete 100s.

## Tested pool (8 configurations; `data/grixis/m6/ij/tested_pools/Edward_Kenway_M7_tested_configurations_20261023.json`)
- BASELINE (raw 100) and CANONICAL_EXPORT (registry export, same logical hash).
- PREFERRED_FIVE (selected).
- PASS_C_BATS_OVER_FATEFUL: RETAIN_ALTERNATIVE (Pass C first hypothesis; keeps Fellwar).
- PASS_C_BATS_OVER_ADRESTIA: RETAIN_ALTERNATIVE (Pass C secondary; Vehicles 13 → 12).
- FOUR_NO_BATS_KEEP_FELLWAR: RETAIN_ALTERNATIVE (below the floor).
- FIVE_CHANDRA_INSTEAD_OF_MU: RETAIN_ALTERNATIVE.
- SIX_EAGLE_VISION_OVER_IMPERIAL_SEAL: RETAIN_ALTERNATIVE (the larger staged package).

**Other named rejections:** Goldspan Dragon, Jhoira, Weatherlight Corsair, Reckless Fireweaver, Lydia Frye, Double Down, Cosima // The Omenkeel, Warkite Marauder, Golden Argosy, Path of Ancestry and Changeling Outcast. Dragon's Smile was EXCLUDE_INVALID.

**Post-floor challenges (all incumbents kept):**
- Imperial Seal vs Eagle Vision (RETAIN_ALTERNATIVE).
- Vaan vs Kitesail Freebooter.
- Coastal Piracy vs Kindred Discovery.
- Subterranean Schooner vs Boosted Sloop.
- Xander's Lounge vs Mutavault.
- Hostage Taker vs Possession Engine.
- Smuggler's Copter vs Phoenix Fleet Airship.
- Port Razer vs Timestream Navigator.

## Distinctness (disclosed)
Nonbasic names shared with the pirate decks (`exports/grixis-archidekt/`), baseline → candidate:
- Admiral Beckett Brass (#2) 50 → 49.
- Admiral Brass, Unsinkable (#3) 48 → 46. The export file was used because no file matched its approved hash e66e3a59.
- Don Andres, the Renegade (#14) 49 → 47.
- Nathan Drake, Treasure Hunter 47 → 45.
- Of the adds, only Spectral Sailor appears in another pirate deck (Beckett Brass).

**Commander-first difference.** Every add serves Edward's own two lines: the tapped-count end-step Treasure and the Vehicle combat-damage theft.

## Infra disclosure
**No shared-infrastructure change in this PR.**
- The gate, the schema, the gate test, the Pass C corpus test and `scripts/grixis_m6_bundle_check.py` (SHA-256 `2962a640…`) are byte-identical to PR #664 head cc2e6d45, not modified here.

**Process notes.**
- The focused CI workflow step names contain no `#` characters.
- **Merge order:** #651 → #652 → #653 → #654 → #655 → #656 → #657 → #658 → #659 → #660 → #661 → #662 → #663 → #664 → this PR (#665).
- Pass C is FORMAL_PASS_C_OWNER_EQUIVALENT under the owner waiver and is **not** technically independent.
- CI run URLs are recorded in the PR body, not in hashed files.
