# Admiral Brass, Unsinkable: M6 I tested-pool local best (M7 candidate), 2026-10-23

Status: **local best within an explicitly tested pool of five complete 100-card lists. This is not a global optimum, not M6 certification, not owner approval, and does not change canonical.** GrokBot prepared and validated this locally on branch `grokbot-deck3-admiral-brass-unsinkable-m7-20261023`. No GitHub CI run exists yet because the push is pending. Owner approval: none.

## Tested pool (five full 100-card configurations)

| id | path | raw SHA-256 | logical hash | judgment |
|---|---|---|---|---|
| BASELINE | `data/grixis/m7/baseline_sources/Admiral_Brass__Unsinkable_approved_source_2026-10-13.txt` | `056f0369bc4b11967365eef65d15a806b2d0f673ecf8097b028ffcdfd472f5cc` | `lh1:3ff7f503d029554c0a6e878680064477a1d3cbbdd56a7b7ec3c1372cdc4f5c05` | RETAIN_CANONICAL_AUTHORITY. The approved list is unchanged and is the comparison anchor. Its weakest Pirates (Scallywag, Francisco, Fathom Fleet Captain, Changeling Outcast, Pitiless Plunderer) add little when Brass returns them as base 4/4 finality bodies. Historic approval does not depend on this pool. |
| PREFERRED_FIVE | `data/grixis/m7/candidate_lists/Admiral_Brass__Unsinkable.txt` | `953a1f8c147239f450ec78704537a2f45c6dde3891d38e7c5f48d178780d2475` | `lh1:39fd58ac40cb3729388c2e9717a37b9af006867b2b9803aa5123bf936d675b3d` | PROVISIONAL_LOCAL_BEST_IN_TESTED_POOL. Exact five in-place swaps: +Kitesail Larcenist +Timestream Navigator +Warkite Marauder +Ragavan +Jhoira / -Scallywag -Francisco -Fathom Fleet Captain -Changeling Outcast -Pitiless Plunderer. Same 31 lands + MDFC, same mana artifacts and same Pirate density. Every add has an ETB, attack or activated payoff that Brass recursion reuses. |
| SIX_NESTING_GROUNDS | `data/grixis/m7/research_challengers/Admiral_Brass__Unsinkable_six_NestingGrounds_20261023.txt` | `873ed9347db8cb3b0cc418844043c53f8e53f1d00e8f0fc1e4821a747a420022` | `lh1:b69e752cd7a864194310cebc14ed85b65788453f60d689372eafa0b9da836fef` | RETAIN_ALTERNATIVE. Preferred five plus Nesting Grounds for Crumbling Necropolis. It can move finality off a returned Pirate, but only at sorcery speed (Power Conduit already does this at instant speed). It drops U/B/R land sources from 26/24/24 to 25/23/23 after the adds raised blue pips to 27. |
| SEVEN_NESTING_ALTAR | `data/grixis/m7/research_challengers/Admiral_Brass__Unsinkable_seven_NestingGrounds_AshnodsAltar_20261023.txt` | `94ac3d88434ed9131fd5a7b63fcb796a07809b7b8fa5f79af536aa49b467d88d` | `lh1:ca5012d70ac21e0c2ffebedec0aa6bf03adac661af2fae96f546f7fdb9078c30` | REJECT. The six-swap list plus Ashnod's Altar for Talisman of Indulgence. The Altar makes mana only by sacrificing creatures; finality exiles returned Pirates and Plunderer is cut. Losing the turn-2 B/R rock weakens the turn-4 Brass that the whole plan depends on. |
| EIGHT_RAVAGER_CREW_PIT | `data/grixis/m7/research_challengers/Admiral_Brass__Unsinkable_eight_Ravager_Crew_SpawningPit_20261023.txt` | `54feef8c62720674044893b7c3db80e550ca0baf73bf1979e7182b2c134d651f` | `lh1:3aa4af1a6720fa22e307d2f5b67e36251f71e5110cc97772980c9aa9e3552af3` | REJECT. Preferred five plus Dire Fleet Ravager, Captivating Crew and Spawning Pit for Corsair Captain, Edward Kenway and Rakdos Signet. Ravager's symmetric life loss taxes Ancient Tomb, Talisman pings and the tutors. Crew duplicates the free Coercive Recruiter threaten, and Spawning Pit is the weakest free outlet. |

Canonical baseline raw `056f0369bc4b11967365eef65d15a806b2d0f673ecf8097b028ffcdfd472f5cc` (vendored byte-exact copy). The historical registry digest `e66e3a59…dd39` does not match the raw file; that mismatch is disclosed and bound in the M7 packet's `baseline_provenance_exception`, never silently replaced. The baseline logical Oracle hash `lh1:3ff7f503d029554c0a6e878680064477a1d3cbbdd56a7b7ec3c1372cdc4f5c05` reproduces the registry value.

## Per-contender record (22 material candidates, each against its named incumbent)

| challenger | named cut | judgment | confidence | reason |
|---|---|---|---|---|
| Kitesail Larcenist | Enterprising Scallywag | SELECT_ADD | HIGH | Highest-impact interaction gain available at three mana; converts the commander's engine into recurring board control for every opponent. |
| Timestream Navigator | Francisco, Fowl Marauder | SELECT_ADD | HIGH | A two-drop that becomes a game-winning extra combat/turn late; directly multiplies the commander's per-turn trigger. |
| Warkite Marauder | Fathom Fleet Captain | SELECT_ADD | HIGH | Cheap, free-every-turn evasion/disruption that protects the attack plan more than a mana-hungry token maker. |
| Ragavan, Nimble Pilferer | Changeling Outcast | SELECT_ADD | MODERATE | Better early tempo and mana than Outcast while preserving the Pirate count and curve. |
| Jhoira, Weatherlight Corsair | Pitiless Plunderer | SELECT_ADD | MODERATE | Exactly the kind of card the commander exists to cheat; outclasses a death-trigger engine that the finality counter switches off. |
| Nesting Grounds | Crumbling Necropolis | RETAIN_ALTERNATIVE | MODERATE | Redundant with Power Conduit at worse speed; fixing loss is real. Recorded as an alternative in the seven-swap configuration. |
| Ashnod's Altar | Talisman of Indulgence | REJECT | MODERATE | Not clearly better than the rock it would replace; the deck's synergy is conditional and Bombardiers/Victimize already cover sacrifice. |
| Spawning Pit | Rakdos Signet | REJECT | HIGH | Verdict: not included. It is the weakest free outlet (no mana like Ashnod's Altar, no reach like Bombardiers) and depends on two other cards. |
| Dire Fleet Ravager | Corsair Captain | REJECT | MODERATE | Changed from the earlier advisory: it does not clearly beat a cheap lord/ramp incumbent once self-damage is counted. |
| Captivating Crew | Edward Kenway | REJECT | MODERATE | Coercive Recruiter already provides free threaten on every Pirate entry; a second, mana-costed version is redundant. |
| Pirated Copy | Merchant Raiders | REJECT | MODERATE | Interesting but not clearly better than an incumbent that triggers on every Brass return. |
| Soul Diviner | Power Conduit | REJECT | HIGH | Power Conduit remains better for the specific timing need (same combat). |
| Back in Town | Patriarch's Bidding | REJECT | MODERATE | Symmetry risk of Bidding is acceptable in a deck that picks Pirate; Back in Town is a slower rate. |
| Big Score | Faithless Looting | REJECT | MODERATE | Not clearly better: Looting's one-mana cost enables Brass on the same turn it is cast. |
| The Grim Captain's Locker | Lightning Greaves | REJECT | MODERATE | Commander protection matters more; Locker competes for the same graveyard. |
| Arm-Mounted Anchor | The Indomitable | REJECT | MODERATE | Not clearly better than an existing draw engine. |
| Port of Karfell | Crumbling Necropolis | REJECT | MODERATE | Too slow for the mana it costs; fixing loss. |
| Herald's Horn | Talisman of Creativity | REJECT | MODERATE | Generic tribal; not clearly better than a two-mana rock for a five-drop commander. |
| Maskwood Nexus | Kindred Discovery | REJECT | HIGH | Identity risk; no non-Pirate payoffs in the list to justify it. |
| Karlach, Fury of Avernus | Edward Kenway | REJECT | MODERATE | Port Razer already provides a recurrable Pirate extra-combat engine. |
| Glint-Horn Buccaneer | Dire Fleet Daredevil | REJECT | MODERATE | Better in a wheel/discard shell than here. |
| Windfall | Faithless Looting | REJECT | HIGH | Not revived: the owner-approved list chose against it and nothing new changes that. |

## Whole-deck comparison (Oracle-text heuristic counts from the committed snapshot)

| config | lands | U/B/R land+rock sources | U/B/R pips | nonland avg MV | Pirate/changeling count |
|---|---|---|---|---|---|
| BASELINE | 31 + MDFC | 26/24/24 | 24/26/23 | 2.985 | 29 |
| PREFERRED_FIVE | 31 + MDFC | 26/24/24 | 27/24/23 | 3.030 | 29 |
| SIX_NESTING_GROUNDS | 31 + MDFC | 25/23/23 | 27/24/23 | 3.030 | 29 |
| SEVEN_NESTING_ALTAR | 31 + MDFC | 25/22/22 | 27/24/23 | 3.045 | 29 |
| EIGHT_RAVAGER_CREW_PIT | 31 + MDFC | 26/23/23 | 25/25/23 | 3.045 | 29 |

## Matchups / opponent assumptions (qualitative, no measured win rates)

- **Four-player Bracket 4 pods** with fast mana, cheap interaction and at least one graveyard-hate piece. Brass's engine depends on the graveyard, so opposing Bojuka Bog, Rest in Peace or Dauthi Voidwalker matter most. The swaps add value outside the graveyard: Ragavan is a turn-1 threat, Larcenist neutralizes one artifact or creature per opponent, and Warkite removes a blocker's abilities.
- **Creature-blocker pods:** Warkite Marauder makes the best blocker a 0/1 with no abilities on each attack. Larcenist turns blockers or mana rocks into Treasure while it stays on the battlefield.
- **Combo/stax pods:** the added interaction is mostly sorcery-speed or on the creature, so speed still matters most. Fierce Guardianship and the other counterspells in the list are unchanged. This is not claimed as an improvement against combo.
- **Board wipes:** finality exiles returned Pirates, so the cut Pitiless Plunderer could not have created Treasure from them anyway. Living Death exiles finality Pirates. Power Conduit (instant speed) remains the counter-removal answer.

## Stopping rationale

Five swaps clear the gate floor, but the floor is not the target. After the five, every remaining slot was re-challenged (packet `open_ended_optimization_audit`). Three larger packages (6, 7, 8 swaps) were built as complete, legal 100-card files and each lost to the preferred five for concrete reasons, not because of a numeric quota.

**Self-challenge on the exact five:**
1. **Nesting Grounds vs Crumbling Necropolis**, the strongest outsider. The upside is real: it can strip finality from a returned Larcenist or Jhoira so it can be recurred again. The costs are concrete. It works only at sorcery speed ({1}, {T}), while Power Conduit already does the job at instant speed. It also turns a three-color land into a colorless one (sources 26/24/24 → 25/23/23) right after the adds raised blue pips from 24 to 27. Verdict: RETAIN_ALTERNATIVE, not clearly better.
2. **Ashnod's Altar vs Talisman of Indulgence.** The Altar makes mana only by sacrificing creatures. Brass-returned Pirates are exiled by finality, Pitiless Plunderer has been cut, and Bombardiers/Victimize already supply outlets. Talisman is a turn-2 B/R source that supports a turn-4 five-mana Brass. Verdict: REJECT.
Close third: Dire Fleet Ravager vs Corsair Captain. It was rejected because the symmetric life loss taxes our own Ancient Tomb, Talisman pings and tutor costs.

## Limitations

Phase-B evidence is a finite, seed-0 bounded rules model (`effect_coverage = bounded_partial`) plus structural and hash tests. There is no game engine, no goldfish run and no multiplayer win-rate measurement, and nothing here supports a statistical improvement claim. EDHREC synergy/inclusion is popularity, not measured lift. Oracle and legality come from the 2026-10-23 live Scryfall `cards/collection` fetch (109 names, zero not found), which matched the frozen 2026-10-16 snapshot text for every card. That live data is not written into the frozen dev snapshot. This memo is not the M6.9 J closure for the program and implies no owner decision.
