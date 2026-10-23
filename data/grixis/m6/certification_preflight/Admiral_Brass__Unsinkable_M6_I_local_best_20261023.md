# Admiral Brass, Unsinkable: M6 I tested-pool local best (M7 candidate, REV2), 2026-10-23

Status: **local best within an explicitly tested pool of 9 complete 100-card lists. This is not a global optimum, not M6 certification and not owner approval, and canonical is unchanged.** GrokBot prepared this on branch `grokbot-deck3-admiral-brass-unsinkable-m7-20261023` (PR #651). REV2 responds to ChatGPT's review of the rev1 five-swap list (head 73e077ed): it corrects the land count, adds Siren's Ruse and Ripples of Undeath, and reverts Ragavan for Changeling Outcast. Exact-head GitHub Actions run URLs for the focused test files are in the PR body. Owner approval: none.

## Tested pool (full 100-card configurations)

| id | path | raw SHA-256 | logical hash | judgment |
|---|---|---|---|---|
| BASELINE | `data/grixis/m7/baseline_sources/Admiral_Brass__Unsinkable_approved_source_2026-10-13.txt` | `056f0369bc4b11967365eef65d15a806b2d0f673ecf8097b028ffcdfd472f5cc` | `lh1:3ff7f503d029554c0a6e878680064477a1d3cbbdd56a7b7ec3c1372cdc4f5c05` | RETAIN_CANONICAL_AUTHORITY. The approved list is unchanged and is the comparison anchor: 34 physical lands (31 rows), 8 rocks, 28 Pirates in the 99 by quantity (29 with the commander). Scallywag, Francisco and Fathom Fleet Captain add little as Brass returns. Pitiless Plunderer gets nothing from finality Pirates but still pays off on other deaths. Historic approval does not depend on this pool. |
| PREFERRED_SIX_REV2 | `data/grixis/m7/candidate_lists/Admiral_Brass__Unsinkable.txt` | `baf0d451bc5fa1f66065d04fa7826610337d1ffa802eebf6c78ba282a784e967` | `lh1:83da1314067759d3e6406907f06714ba225f62ece24f80bf9a4adeab4458f6c7` | PROVISIONAL_LOCAL_BEST_IN_TESTED_POOL (REV2, after ChatGPT review). Six in-place swaps: +Kitesail Larcenist +Timestream Navigator +Warkite Marauder +Jhoira +Siren's Ruse +Ripples of Undeath / -Scallywag -Francisco -Fathom Fleet Captain -Pitiless Plunderer -Crumbling Necropolis -Faithless Looting. 33 lands + 8 rocks (land sources U20/B18/R17 unrestricted), Pirate count unchanged at 28 in the 99, Changeling Outcast kept. |
| PRIOR_FIVE_REV1 | `data/grixis/m7/research_challengers/Admiral_Brass__Unsinkable_prior_five_rev1_20261023.txt` | `953a1f8c147239f450ec78704537a2f45c6dde3891d38e7c5f48d178780d2475` | `lh1:39fd58ac40cb3729388c2e9717a37b9af006867b2b9803aa5123bf936d675b3d` | SUPERSEDED_HISTORY. The rev1 preferred five (raw 953a1f8c...; lh1:39fd58ac...) with Ragavan over Changeling Outcast and 34 lands. Its mana memo miscounted lands as 31 (rows, not quantities). Superseded by REV2: the Ragavan swap is reverted, and Siren's Ruse and Ripples are added. |
| SEVEN_REV2_RAGAVAN_OVER_OUTCAST | `data/grixis/m7/research_challengers/Admiral_Brass__Unsinkable_rev2_seven_Ragavan_over_Outcast_20261023.txt` | `bbcac21230d06746b8e4eb65836b6d86c58964b078816dd6a39aca4a1c111419` | `lh1:14a5e4df4060a4e63be730ec27d6683108b8489166fce53274b10d1b283bca37` | RETAIN_ALTERNATIVE. REV2 plus Ragavan for Changeling Outcast. Ragavan (Monkey Pirate) has the better hard-cast turn 1. As a Brass return, Outcast's can't-be-blocked 4/4 haste connection reliably feeds Beckett's three-Pirate theft, Breeches, Ramirez and Shared Animosity, while Ragavan's Treasure and card depend on getting through blockers. Not clearly better. |
| SEVEN_REV2_PRISMARI | `data/grixis/m7/research_challengers/Admiral_Brass__Unsinkable_rev2_seven_PrismariCommand_20261023.txt` | `a5a027fe2bd4b395a250190c76757236b3788917a373f22b91b21ac2f02e45a6` | `lh1:d20db7e2ef7efdd20fcdb73ddd10455c1bc9bbb08b7211d3500393af86f1a656` | REJECT. REV2 plus Prismari Command for Feed the Swarm. Instant loot plus Treasure is good setup, but the list loses its cheap creature/enchantment answer, and Ripples already covers precombat setup. |
| SIX_REV2_KEEP34_MINUS_TALISMAN | `data/grixis/m7/research_challengers/Admiral_Brass__Unsinkable_rev2_six_keep34lands_minus_Talisman_20261023.txt` | `747d89d1b2c38150adcca21a4c829b3d80bbad82445f40078d151358968b8c15` | `lh1:8f068800c783974c77c03e4773dfbc09ee174815a40a3029f8dc4ba746a25e80` | REJECT. Same six adds, but Siren's Ruse replaces Talisman of Indulgence so 34 lands are kept. That keeps land-drop odds (P(>=4 lands in 10) 0.470 vs 0.441) at the cost of the turn-2 B/R rock that enables turn-4 Brass. A tapped tri-land is the cheaper mana source to give up. Total mana permanents are 41 either way. |
| REV1_SIX_NESTING_GROUNDS | `data/grixis/m7/research_challengers/Admiral_Brass__Unsinkable_six_NestingGrounds_20261023.txt` | `873ed9347db8cb3b0cc418844043c53f8e53f1d00e8f0fc1e4821a747a420022` | `lh1:b69e752cd7a864194310cebc14ed85b65788453f60d689372eafa0b9da836fef` | HISTORY / RETAIN_ALTERNATIVE (built on rev1 five). Nesting Grounds for Crumbling Necropolis: sorcery-speed finality relocation. Corrected numbers: unrestricted land sources 21/19/18 -> 20/18/17 (the rev1 26/24/24 -> 25/23/23 figures were miscounted). The conclusion holds: it costs one source of each color and duplicates instant-speed Power Conduit, and REV2's Siren's Ruse also fills the reset role. |
| REV1_SEVEN_NESTING_ALTAR | `data/grixis/m7/research_challengers/Admiral_Brass__Unsinkable_seven_NestingGrounds_AshnodsAltar_20261023.txt` | `94ac3d88434ed9131fd5a7b63fcb796a07809b7b8fa5f79af536aa49b467d88d` | `lh1:ca5012d70ac21e0c2ffebedec0aa6bf03adac661af2fae96f546f7fdb9078c30` | HISTORY / REJECT (built on rev1 five). Adds Ashnod's Altar for Talisman of Indulgence. The Altar makes mana only from sacrifices, and finality exiles returned Pirates unless they are reset first. Losing the turn-2 rock weakens turn-4 Brass. |
| REV1_EIGHT_RAVAGER_CREW_PIT | `data/grixis/m7/research_challengers/Admiral_Brass__Unsinkable_eight_Ravager_Crew_SpawningPit_20261023.txt` | `54feef8c62720674044893b7c3db80e550ca0baf73bf1979e7182b2c134d651f` | `lh1:3aa4af1a6720fa22e307d2f5b67e36251f71e5110cc97772980c9aa9e3552af3` | HISTORY / REJECT (built on rev1 five). Ravager's symmetric life loss taxes Ancient Tomb, Talisman pings and the tutors. Crew duplicates Coercive Recruiter, and Spawning Pit is the weakest free outlet. |

Canonical baseline raw `056f0369bc4b11967365eef65d15a806b2d0f673ecf8097b028ffcdfd472f5cc` (vendored byte-exact copy). The historical registry digest `e66e3a59…dd39` does not match the raw file. That mismatch is disclosed and bound in the M7 packet's `baseline_provenance_exception`, never silently replaced. The baseline logical Oracle hash `lh1:3ff7f503d029554c0a6e878680064477a1d3cbbdd56a7b7ec3c1372cdc4f5c05` reproduces the registry value. The rev1 candidate (raw `953a1f8c…2475`, `lh1:39fd58ac…5b3d`) is preserved byte-identical as `PRIOR_FIVE_REV1`.

## Per-contender record (27 material candidates, each against its named incumbent)

| challenger | named cut | judgment | confidence | reason |
|---|---|---|---|---|
| Kitesail Larcenist | Enterprising Scallywag | SELECT_ADD | HIGH | Highest-impact interaction gain available at three mana; converts the commander's engine into recurring board control for every opponent. |
| Timestream Navigator | Francisco, Fowl Marauder | SELECT_ADD | HIGH | A two-drop that becomes a game-winning extra combat/turn late; directly multiplies the commander's per-turn trigger. |
| Warkite Marauder | Fathom Fleet Captain | SELECT_ADD | HIGH | Cheap, free-every-turn evasion/disruption that protects the attack plan more than a mana-hungry token maker. |
| Ragavan, Nimble Pilferer | Changeling Outcast | RETAIN_ALTERNATIVE | MODERATE | REV2 reversal after ChatGPT review: Ragavan does not clearly beat Outcast once Brass is established or opponents have blockers. Against any other incumbent (e.g. Talisman of Indulgence, Corsair Captain) it also loses: reliable mana and a lord beat conditional Treasure. The seven-swap file over Outcast is recorded and not selected. |
| Jhoira, Weatherlight Corsair | Pitiless Plunderer | SELECT_ADD | MODERATE | Exactly the kind of card the commander exists to cheat; outclasses a death-trigger engine that the finality counter switches off. |
| Siren's Ruse | Crumbling Necropolis | SELECT_ADD | HIGH | Cheap instant that is protection, value and finality reset in one card, and it directly multiplies the ETB Pirates Brass recurs. |
| Ripples of Undeath | Faithless Looting | SELECT_ADD | HIGH | A repeatable, card-neutral graveyard engine timed for the commander's trigger beats a one-shot card-disadvantage looter. |
| Prismari Command | Feed the Swarm | REJECT | MODERATE | Flexible, but does not clearly beat the incumbent removal slot; Ripples already covers graveyard setup. Recorded as a seven-swap full-100 file. |
| Ghostly Flicker | Deflecting Swat | REJECT | MODERATE | Not clearly better than Siren's Ruse and does not beat a free protection spell. |
| Spectral Sailor | Siren Stormtamer | REJECT | MODERATE | Lower impact than the incumbent protection Pirate. |
| Nesting Grounds | Crumbling Necropolis | RETAIN_ALTERNATIVE | MODERATE | Redundant with Power Conduit at worse speed; colorless. REV2: its named incumbent (Crumbling Necropolis) is now cut for Siren's Ruse, and replacing a further colored land would drop land sources below 20/18/17. Recorded in the rev1 six- and seven-swap files only. |
| Ashnod's Altar | Talisman of Indulgence | REJECT | MODERATE | Not clearly better than the rock it would replace; the deck's synergy is conditional and Bombardiers/Victimize already cover sacrifice. |
| Spawning Pit | Rakdos Signet | REJECT | HIGH | Verdict: not included. It is the weakest free outlet (no mana like Ashnod's Altar, no reach like Bombardiers) and depends on two other cards. |
| Dire Fleet Ravager | Corsair Captain | REJECT | MODERATE | Changed from the earlier advisory: it does not clearly beat a cheap lord/ramp incumbent once self-damage is counted. |
| Captivating Crew | Edward Kenway | REJECT | MODERATE | Coercive Recruiter already provides free threaten on every Pirate entry; a second, mana-costed version is redundant. |
| Pirated Copy | Merchant Raiders | REJECT | MODERATE | Interesting but not clearly better than an incumbent that triggers on every Brass return. |
| Soul Diviner | Power Conduit | REJECT | HIGH | Power Conduit remains better for the specific timing need (same combat). |
| Back in Town | Patriarch's Bidding | REJECT | MODERATE | Symmetry risk of Bidding is acceptable in a deck that picks Pirate; Back in Town is a slower rate. |
| Big Score | Faithless Looting | REJECT | MODERATE | Not clearly better than the slot's occupant. REV2: that slot now goes to Ripples of Undeath, a repeatable precombat mill that beats both Looting and Big Score. |
| The Grim Captain's Locker | Lightning Greaves | REJECT | MODERATE | Commander protection matters more; Locker competes for the same graveyard. |
| Arm-Mounted Anchor | The Indomitable | REJECT | MODERATE | Not clearly better than an existing draw engine. |
| Port of Karfell | Crumbling Necropolis | REJECT | MODERATE | Too slow for the mana it costs; fixing loss. |
| Herald's Horn | Talisman of Creativity | REJECT | MODERATE | Generic tribal; not clearly better than a two-mana rock for a five-drop commander. |
| Maskwood Nexus | Kindred Discovery | REJECT | HIGH | Identity risk; no non-Pirate payoffs in the list to justify it. |
| Karlach, Fury of Avernus | Edward Kenway | REJECT | MODERATE | Port Razer already provides a recurrable Pirate extra-combat engine. |
| Glint-Horn Buccaneer | Dire Fleet Daredevil | REJECT | MODERATE | Better in a wheel/discard shell than here. |
| Windfall | Faithless Looting | REJECT | HIGH | Not revived: the owner-approved list chose against it, and REV2 fills the Looting slot with Ripples of Undeath instead. |

## Whole-deck comparison (CORRECTED REV2: quantity-counted from the rev2 Oracle snapshot)

Lands are counted by quantity (2x Island/Mountain/Swamp), and Brass's Tunnel-Grinder counts as an artifact (front face), not a land. "Land sources" are unrestricted colored lands. The "conditional" lands are Cavern of Souls, Exotic Orchard and Secluded Courtyard. The rev1 table ("31 + MDFC", "26/24/24") counted rows and is withdrawn.

| config | lands | rocks | U/B/R land sources | U/B/R rock sources | U/B/R pips | nonland avg MV | curve 0/1/2/3/4/5/6+ | Pirates in the 99 (qty, incl. changeling) |
|---|---|---|---|---|---|---|---|---|
| BASELINE | 34 (31 rows) | 8 | 21/19/18 (+3/3/3 conditional) | 5/5/5 | 23/25/22 | 2.954 | 0/7/20/17/13/7/1 | 28 |
| PREFERRED_SIX_REV2 | 33 (30 rows) | 8 | 20/18/17 (+3/3/3 conditional) | 5/5/5 | 27/25/20 | 3.0 | 0/6/21/18/12/7/2 | 28 |
| PRIOR_FIVE_REV1 | 34 (31 rows) | 8 | 21/19/18 (+3/3/3 conditional) | 5/5/5 | 26/23/22 | 3.0 | 0/7/19/18/12/7/2 | 28 |
| SEVEN_REV2_RAGAVAN_OVER_OUTCAST | 33 (30 rows) | 8 | 20/18/17 (+3/3/3 conditional) | 5/5/5 | 27/24/21 | 3.0 | 0/6/21/18/12/7/2 | 28 |
| SEVEN_REV2_PRISMARI | 33 (30 rows) | 8 | 20/18/17 (+3/3/3 conditional) | 5/5/5 | 28/24/21 | 3.015 | 0/6/20/19/12/7/2 | 28 |
| SIX_REV2_KEEP34_MINUS_TALISMAN | 34 (31 rows) | 7 | 21/19/18 (+3/3/3 conditional) | 5/4/4 | 27/25/20 | 3.015 | 0/6/20/18/12/7/2 | 28 |
| REV1_SIX_NESTING_GROUNDS | 34 (31 rows) | 8 | 20/18/17 (+3/3/3 conditional) | 5/5/5 | 26/23/22 | 3.0 | 0/7/19/18/12/7/2 | 28 |
| REV1_SEVEN_NESTING_ALTAR | 34 (31 rows) | 8 | 20/18/17 (+3/3/3 conditional) | 5/4/4 | 26/23/22 | 3.015 | 0/7/18/19/12/7/2 | 28 |
| REV1_EIGHT_RAVAGER_CREW_PIT | 34 (31 rows) | 7 | 21/19/18 (+3/3/3 conditional) | 5/4/4 | 24/24/22 | 3.015 | 0/7/19/17/13/7/2 | 28 |

Hypergeometric draws from 99 cards with no mulligan: P(2–5 lands in opening 7) = 0.758 at 34 lands vs 0.741 at 33. P(≥4 lands in top 10) = 0.470 vs 0.441. P(≥4 lands-or-rocks in top 10) = 0.687 (42) vs 0.662 (41).

## Matchups / opponent assumptions (qualitative, no measured win rates)

- **Four-player Bracket 4 pods** with fast mana, cheap interaction and at least one graveyard-hate piece. Brass's engine depends on the graveyard, so opposing Bojuka Bog, Rest in Peace or Dauthi Voidwalker matter most. Ripples of Undeath increases graveyard reliance, while Larcenist, Warkite and Siren's Ruse (as protection plus a draw) still work from hand.
- **Creature-blocker pods:** Changeling Outcast is kept because it reliably connects as a Brass return. Warkite Marauder makes the best blocker a 0/1 with no abilities on each attack.
- **Spot-removal pods:** Siren's Ruse saves a key Pirate at instant speed and draws a card. A blinked Brass-returned Pirate comes back without finality, at printed P/T and summoning-sick.
- **Combo/stax pods:** the counterspells are unchanged. This is not claimed as an improvement against combo.
- **Board wipes:** finality exiles returned Pirates unless Power Conduit or Siren's Ruse reset them first. Pitiless Plunderer (cut) would still have paid off on non-finality deaths; that real loss is accepted.

## Stopping rationale

Six swaps is a quality stop, not a quota. The rev1 five were re-evaluated after ChatGPT's review: Ragavan was reverted and two outside candidates (Siren's Ruse, Ripples) were added over specific incumbents. Larger packages were built as complete, legal 100-card files and each lost to the preferred six for concrete reasons (see packet `open_ended_optimization_audit`).

**Self-challenge (REV2):**
1. **Ragavan vs Changeling Outcast.** Ragavan is better on turn 1. Outcast is better as a Brass return: an unblockable hasty 4/4 reliably feeds Beckett's three-Pirate theft, Breeches, Ramirez and Shared Animosity. Verdict: RETAIN_ALTERNATIVE (Outcast kept).
2. **Prismari Command vs Feed the Swarm.** Rejected because it would cost the list's cheap enchantment/creature answer.
3. **34 lands vs 33 (Talisman of Indulgence vs Crumbling Necropolis as the cut for Siren's Ruse).** Cut the tapped tri-land, not the turn-2 rock.
4. The rev1 self-challenge still holds with corrected numbers. Nesting Grounds costs one source of each color (land sources 21/19/18 → 20/18/17) and works only at sorcery speed. Ashnod's Altar is conditional. Both stay out.

## Limitations

Phase-B evidence is a finite, seed-0 bounded rules model (`effect_coverage = bounded_partial`) plus structural and hash tests. There is no game engine, no goldfish run and no multiplayer win-rate measurement, and nothing here supports a statistical improvement claim. EDHREC synergy/inclusion is popularity, not measured lift. Oracle and legality come from the 2026-10-23 live Scryfall `cards/collection` fetch (109 names, zero not found), which matched the frozen 2026-10-16 snapshot text for every card. The second-pass names came from one more batched `cards/collection` call; the rev2 snapshot merges both. That live data is not written into the frozen dev snapshot. This memo is not the M6.9 J closure for the program and implies no owner decision.
