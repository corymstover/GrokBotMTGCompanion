# Admiral Brass, Unsinkable — ChatGPT adversarial review packet (M7, 2026-10-23)

**Status:** REVIEW CANDIDATE — NOT APPROVED, NOT CANONICAL. Gate readiness `READY_FOR_EXACT_OWNER_APPROVAL_NOT_YET_APPROVED`.
Only Cory can approve. Owner question: "This deck is complete. Do you approve it?"

Reviewer instruction: attack this list. Try to break each claim below and show any rules error, illegal card, unpayable line or a candidate that clearly beats an incumbent. No win rates were measured; EDHREC prevalence is discovery evidence only.

## Provenance
- Canonical source (read-only): `corymstover/grixis-commander-encyclopediaGPT` `refinement/decklists/Admiral_Brass_Unsinkable_Whole_List_Approval_Candidate_2026-10-13.txt`, physical raw SHA-256 `056f0369bc4b11967365eef65d15a806b2d0f673ecf8097b028ffcdfd472f5cc` (vendored byte-exact at `data/grixis/m7/baseline_sources/Admiral_Brass__Unsinkable_approved_source_2026-10-13.txt`).
- The historical approval digest `e66e3a59…dd39` in `state/current_deck_overrides.json` does **not** match those bytes (no normalization reproduces it). Both are recorded separately; nothing was re-approved. Logical hash of the baseline matches the registry: `lh1:3ff7f503…5c05`.
- Candidate: `data/grixis/m7/candidate_lists/Admiral_Brass__Unsinkable.txt`, logical hash `lh1:39fd58ac…5b3d`.
- Live Scryfall check (2026-10-23): 109 names (97 baseline + 12 candidates) are all Commander-legal and inside UBR identity, and the Oracle text matches the frozen snapshot. Game Changers in the list: Ancient Tomb, Cyclonic Rift, Demonic Tutor, Fierce Guardianship, Jeska's Will and Vampiric Tutor (6). That puts it in **Power Bracket 4**.
- Project exceptions: none apply to this deck. Exceptions for other decks are unchanged.

## Swaps (5)
| Add | Cut | Why |
|---|---|---|
| Kitesail Larcenist | Enterprising Scallywag | Its ETB turns one artifact or creature per player into a Treasure. When Brass returns it, it's a 4/4 hasty flier that hits every opponent. Throne doubles the ETB. |
| Timestream Navigator | Francisco, Fowl Marauder | Brass gives it haste, so with city's blessing it can activate immediately for an extra turn, which means another Brass trigger. |
| Warkite Marauder | Fathom Fleet Captain | Its free attack trigger neutralizes the best blocker. Throne doubles it. |
| Ragavan, Nimble Pilferer | Changeling Outcast | A better one-drop: Treasure plus cards. As a Brass target it's a 4/4 hasty Treasure engine. |
| Jhoira, Weatherlight Corsair | Pitiless Plunderer | A Brass return triggers both its ETB and its attack, stealing two historic permanents. Plunderer is switched off by finality, because those Pirates are exiled rather than dying. |

## Rules claims to attack
1. **Brass trigger timing.** It triggers at the beginning of combat on our turn. The target Pirate must already be in the graveyard when the trigger goes on the stack. Entomb, Buried Alive and Looting have to happen before combat (Entomb works at instant speed in upkeep or main 1).
2. **Base 4/4.** The returned Pirate's base P/T becomes 4/4. Counters, anthems (Corsair Captain, Shared Animosity) and pumps still apply on top. Haste lasts only until end of turn. The base 4/4 and the finality counter stay.
3. **Finality.** If the creature would die (destroyed, sacrificed, Living Death, Bombardiers boast), it is exiled instead. Bounce, blink or tuck move it normally and the new object has no counter. A finality Pirate that Larcenist turns into a Treasure keeps the counter, so sacrificing that Treasure exiles it.
4. **Counter removal.** Power Conduit ({2}) costs {T} plus removing a counter from our permanent, and is usable at instant speed with no summoning sickness. Its mode puts a charge counter on an artifact or a +1/+1 counter on a creature; Conduit itself is always a legal artifact target. Removing the finality counter lets the Pirate go to the graveyard and be returned again. Nesting Grounds (not included) is sorcery speed only. Soul Diviner (not included) is summoning-sick.
5. **Roaming Throne (Pirate).** Brass's trigger fires twice and each instance picks its own target, so you need **two different** Pirates in the graveyard. Targeting the same card twice means the second trigger fizzles. Throne also doubles the ETB triggers of returned Pirates (Larcenist, Jhoira, Hostage Taker, Amphin Mutineer, Coercive Recruiter, Merchant Raiders) and attack triggers (Jhoira, Warkite).
6. **Port Razer.** Each extra combat phase gives another beginning of combat, so another Brass trigger.
7. **Timestream Navigator** goes to the bottom of the library, not the graveyard, so it is not re-usable by Brass unless redrawn.
8. **Jhoira.** We lose life equal to each stolen permanent's MV. Watch life totals alongside shocks, Talismans, Mana Confluence, Black Market Connections, Vampiric Tutor and Reanimate.

## Adversarial scenarios (please challenge)
- **Commander removed or taxed.** Brass costs 5 plus tax. Fallbacks are castable Pirates, Kindred Discovery, Living Death/Patriarch's Bidding mass reanimation, Animate Dead and Reanimate. Protection: Lightning Greaves, Fierce Guardianship, Deflecting Swat, Counterspell, Mana Drain.
- **Bojuka Bog / Rest in Peace.** Bog in response to the trigger: the trigger fizzles, but the other Throne instance survives if its target remains. Rest in Peace switches off the reanimation half and turns mills into exile. Answers: Chaos Warp, Cyclonic Rift, Otawara and Larcenist (which hits artifacts and creatures only, **not** enchantments).
- **Finality cases.** Sacrifice and destroy exile the creature. Bounce resets it. Blink resets it and also clears the base 4/4 and haste. Counter-moving gives the counter to an opponent's creature (Nesting Grounds only, which isn't in the list).
- **Throne doubling.** Is two-distinct-target availability realistic on turns 5–6? Mill 4 on Brass ETB plus looters.
- **Combat disruption.** Fog, Settle the Wreckage, blockers with deathtouch. Warkite and Larcenist mitigate this; there's no fog protection.
- **Resource pressure.** Opponents' Treasures from Larcenist, and Jhoira's life loss.
- **Symmetric Living Death / Patriarch's Bidding.** Opponents get their creatures back too. Living Death **exiles** our finality Pirates instead of returning them, so sequence it before rebuilding.
- **Payable win lines.** Combat damage scaling via Shared Animosity, Angrath's Marauders, Port Razer combats, Navigator extra turns and Broadside Bombardiers reach. No deterministic two-card infinite was identified. Commander Spellbook was **not** queried live this run, so please check.

## Rejected candidates (attack these too)
- Nesting Grounds: retained as an alternative.
- Ashnod's Altar, Spawning Pit, Dire Fleet Ravager, Captivating Crew, Pirated Copy, Soul Diviner, Back in Town, Big Score, Grim Captain's Locker, Arm-Mounted Anchor, Port of Karfell, Herald's Horn, Maskwood Nexus, Karlach, Glint-Horn Buccaneer, Windfall: rejected.
- **Spawning Pit verdict: not included.** It's the weakest free outlet: no mana, no damage, and it needs Conduit or a stolen creature to matter.
- Larger staged configurations: 6-swap (+Nesting Grounds) kept as a retained alternative; both of these rejected: 7-swap (+Nesting Grounds +Ashnod's Altar) and 8-swap (+Dire Fleet Ravager +Captivating Crew +Spawning Pit). The files are in `data/grixis/m7/research_challengers/`.
- Disclosure: an earlier GrokBot advisory suggested Dire Fleet Ravager. This run reverses that, because of self-damage and redundancy.

## Self-challenge on the exact five (recorded in packet `open_ended_optimization_audit`)
1. **Nesting Grounds vs Crumbling Necropolis** (strongest outsider; six-swap file `Admiral_Brass__Unsinkable_six_NestingGrounds_20261023.txt`, raw `873ed934…0022`).
   - Upside: it can strip finality from a returned Larcenist or Jhoira.
   - Costs: it is sorcery speed only ({1}, {T}), while Power Conduit already does this at instant speed. It also turns a three-color land into a colorless one (U/B/R sources 26/24/24 → 25/23/23) after the adds raised blue pips from 24 to 27.
   - Verdict: **RETAIN_ALTERNATIVE**, not clearly better.
2. **Ashnod's Altar vs Talisman of Indulgence** (seven-swap file).
   - The Altar makes mana only by sacrificing creatures. Finality exiles returned Pirates, Pitiless Plunderer is cut, and Bombardiers/Victimize already supply outlets.
   - Talisman is a turn-2 B/R source that supports a turn-4 five-mana Brass.
   - Verdict: **REJECT**.
- Close third: Dire Fleet Ravager vs Corsair Captain was rejected for symmetric self-damage. Note that the baseline's owner-equivalent Pass C left "+Ravager / −Merchant Raiders" as a NEEDS TESTING hypothesis; this run did not adopt it.

## Whole-deck comparison (five full 100-card configurations; Oracle-text heuristic counts)
| config | raw SHA-256 | U/B/R sources | U/B/R pips | avg MV | judgment |
|---|---|---|---|---|---|
| BASELINE (canonical) | `056f0369…72f5cc` | 26/24/24 | 24/26/23 | 2.985 | retain canonical authority |
| PREFERRED_FIVE | `953a1f8c…0d2475` | 26/24/24 | 27/24/23 | 3.030 | provisional local best |
| SIX (+Nesting Grounds) | `873ed934…a420022` | 25/23/23 | 27/24/23 | 3.030 | retained alternative |
| SEVEN (+Nesting, +Altar) | `94ac3d88…67d88d` | 25/22/22 | 27/24/23 | 3.045 | reject |
| EIGHT (+Ravager, +Crew, +Pit) | `54feef8c…d651f` | 26/23/23 | 25/25/23 | 3.045 | reject |

Per-contender records: there are 22 material candidates, each with a named cut, judgment, confidence and reason. They are listed in `data/grixis/m6/certification_preflight/Admiral_Brass__Unsinkable_M6_I_local_best_20261023.md` and in the packet's `material_candidates`.

## M6 I / J evidence (candidate-specific; follows the Admiral Beckett Brass rev2 pattern)
- I certificate: `data/grixis/m6/ij/certificates/admiral-brass-unsinkable-m7.json`. Tested-pool local only, 5 configurations; not global.
- Tested pool: `data/grixis/m6/ij/tested_pools/Admiral_Brass__Unsinkable_M7_five_configurations_20261023.json`.
- J bundle: `data/grixis/m6/ij/revision_bundles/admiral-brass-unsinkable-m7.json`. It passes `grixis_m6_bundle_check.validate_bundle` locally.
- Oracle/legality snapshot: `data/grixis/m6/oracle_snapshots/Admiral_Brass__Unsinkable_M7_109_Scryfall_20261023.json`. Rules: `data/grixis/m6/rules_snapshots/Admiral_Brass__Unsinkable_M7_20261023.md`. Mana and red-team memos are under `data/grixis/m6/certification_preflight/`.
- Checker change, disclosed: `grixis_m6_bundle_check.py` gained two narrow, fail-closed acceptances. (a) The Pass C ledger may carry the registry's recorded historical digest `e66e3a59…dd39` while the Stage A seal carries the physical raw `056f0369…`, but only when the registry itself records `recorded_matches_raw: false` with exactly that pair. (b) The preserved wording "**Technically independent:** NO." is accepted as explicit non-independence disclosure. Adversarial tests were added; no historical file was edited.

## Open items
- No GitHub CI run yet; the push is pending a token with workflow scope. All gate and test results are local.
- No existing workflow runs the new Brass test files; they are discovered only by a full `pytest`/`unittest discover`.
- Phase-B is a finite bounded rules model, not a game engine. There are no win rates.
- Commander Spellbook was not queried live.
- Owner decision: none. This is not approved and not canonical.

## Candidate 100 (Archidekt import)
Tags: Pirates, Reanimator, Aggro. Bracket 4.
```text
1x Admiral Brass, Unsinkable [Commander]
1x Admiral Beckett Brass
1x Amphin Mutineer
1x Ancient Tomb
1x Angrath's Marauders
1x Animate Dead
1x Arcane Signet
1x Badlands
1x Black Market Connections
1x Blood Crypt
1x Bloodstained Mire
1x Breeches, Brazen Plunderer
1x Breeches, Eager Pillager
1x Broadside Bombardiers
1x Buried Alive
1x Captain Lannery Storm
1x Cavern of Souls
1x Ragavan, Nimble Pilferer
1x Chaos Warp
1x Coercive Recruiter
1x Command Tower
1x Corsair Captain
1x Counterspell
1x Crumbling Necropolis
1x Cyclonic Rift
1x Deadly Rollick
1x Deflecting Swat
1x Demonic Tutor
1x Dimir Signet
1x Dire Fleet Daredevil
1x Drowned Catacomb
1x Edward Kenway
1x Kitesail Larcenist
1x Entomb
1x Exotic Orchard
1x Faithless Looting
1x Warkite Marauder
1x Feed the Swarm
1x Fierce Guardianship
1x Forerunner of the Coalition
1x Timestream Navigator
1x Gemcutter Buccaneer
1x Mary Read and Anne Bonny
1x Hostage Taker
2x Island
1x Izzet Signet
1x Jeska's Will
1x Kindred Discovery
1x Lightning Greaves
1x Living Death
1x Luxury Suite
1x Malcolm, Alluring Scoundrel
1x Malcolm, Keen-Eyed Navigator
1x Mana Confluence
1x Mana Drain
1x Merchant Raiders
1x Morphic Pool
2x Mountain
1x Otawara, Soaring City
1x Path of Ancestry
1x Patriarch's Bidding
1x Jhoira, Weatherlight Corsair
1x Polluted Delta
1x Port Razer
1x Power Conduit
1x Rakdos Signet
1x Ramirez DePietro, Pillager
1x Reanimate
1x Roaming Throne
1x Scalding Tarn
1x Secluded Courtyard
1x Shared Animosity
1x Shipwreck Marsh
1x Siren Stormtamer
1x Skeleton Crew
1x Smoldering Marsh
1x Sol Ring
1x Steam Vents
1x Stormcarved Coast
1x Sulfur Falls
2x Swamp
1x Talisman of Creativity
1x Talisman of Dominance
1x Talisman of Indulgence
1x The Indomitable
1x Toxic Deluge
1x Training Center
1x Underground River
1x Underground Sea
1x Vampiric Tutor
1x Victimize
1x Volcanic Island
1x Watery Grave
1x Brass's Tunnel-Grinder // Tecutlan, the Searing Rift
1x Wonder
1x Xander's Lounge
1x Zara, Renegade Recruiter
```

Raw SHA-256 of candidate file: `953a1f8c147239f450ec78704537a2f45c6dde3891d38e7c5f48d178780d2475`
