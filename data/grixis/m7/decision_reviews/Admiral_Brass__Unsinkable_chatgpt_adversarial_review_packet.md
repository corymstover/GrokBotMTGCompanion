# Admiral Brass, Unsinkable — ChatGPT adversarial review packet (M7, REV2, 2026-10-23)

**Status:** REVIEW CANDIDATE — NOT APPROVED, NOT CANONICAL. Gate readiness `READY_FOR_EXACT_OWNER_APPROVAL_NOT_YET_APPROVED`.
Only Cory can approve. Owner question: "This deck is complete. Do you approve it?"

Reviewer instruction: attack this list. Try to break each claim below and show any rules error, illegal card, unpayable line or a candidate that clearly beats an incumbent. No win rates were measured; EDHREC prevalence is discovery evidence only.

REV2 supersedes the rev1 five-swap candidate at PR #651 head `73e077ed` (raw `953a1f8c…0d2475`, `lh1:39fd58ac…5b3d`). That candidate is preserved byte-identical at `data/grixis/m7/research_challengers/Admiral_Brass__Unsinkable_prior_five_rev1_20261023.txt`.

## Response to ChatGPT review

**1. Land-count error: accepted and fixed.** Rev1 counted land *rows* (31), not cards. The baseline has **34 physical lands** (2x Island, 2x Mountain, 2x Swamp), and Brass's Tunnel-Grinder is a front-face Legendary Artifact (MV 3) that only becomes a land after three descend end steps, so it is not counted as a land. The corrected baseline has unrestricted colored land sources U/B/R 21/19/18 (+3/3/3 conditional: Cavern, Orchard, Courtyard), 8 rocks with 5/5/5 color sources, and 42 lands+rocks. The rev1 "26/24/24" figures are withdrawn everywhere (packet, pool judgments, I memo, mana memo, this file).
- The mechanics test now asserts `sum(q for n,q in base.items() if land(n)) == 34`, 31 rows, and that the Tunnel-Grinder front face is not a land. The candidate asserts 33.
- **Dependent conclusions re-checked.** Nesting Grounds still loses: it costs one source of each color (21/19/18 → 20/18/17), is sorcery speed only, and duplicates instant-speed Power Conduit and now Siren's Ruse.
- **Is 34 + 8 too many?** With a 3.0 average and many Treasure makers, yes, it is heavy enough that a land is a legitimate cut. REV2 cuts **Crumbling Necropolis**, the always-tapped tri-land that can't be fetched (Xander's Lounge is fetchable and cycles).
  - Cost: P(2–5 lands in 7) 0.758 → 0.741; P(≥4 lands in 10) 0.470 → 0.441; P(≥4 lands-or-rocks in 10) 0.687 → 0.662.
  - A full-100 alternative that keeps 34 lands and cuts Talisman of Indulgence instead was built and rejected, because the rock is the turn-4 Brass accelerant. MODERATE confidence.

**2. Overlooked candidates: two added, one rejected, as full 100s.**
- **Siren's Ruse: SELECT_ADD over Crumbling Necropolis.** It is an instant reset: the Brass-returned Pirate comes back as a new object without finality, so it can later die and be recurred. It retriggers ETBs (Larcenist, Amphin Mutineer, Hostage Taker, Jhoira, Coercive Recruiter), protects against removal, and draws on a Pirate.
  - Downsides: printed P/T, no haste, and a stolen creature returns to its owner.
- **Ripples of Undeath: SELECT_ADD over Faithless Looting.** It triggers in the first main phase, before Brass's beginning-of-combat trigger, so it is repeatable precombat setup (mill 3 each turn, optional 1+3 life to keep one). Looting is one-shot card disadvantage.
- **Prismari Command: REJECT vs Feed the Swarm.** Its instant loot+Treasure is good, but it would lose the cheap creature/enchantment answer, and Ripples already covers setup. It was built as the seven-swap full 100.
- **Brief scan of the same categories:**
  - Ghostly Flicker (3 mana, no draw; Ruse already fills the role) REJECT vs Deflecting Swat.
  - Spectral Sailor (low-impact return) REJECT vs Siren Stormtamer.
  - Big Score and Windfall were already rejected for the Looting slot that Ripples now takes.
- One batched live Scryfall `/cards/collection` call covered all second-pass names (`data/grixis/m7/research_challengers/Admiral_Brass__Unsinkable_Scryfall_secondpass_20261023.json`). They are merged only into the candidate-specific rev2 snapshot, not the frozen dev snapshot.

**3. Re-evaluated cuts.**
- **(a) Pitiless Plunderer → Jhoira: KEPT, wording corrected.** Plunderer is *not* globally switched off. It still pays off on hard-cast creature deaths, tokens, stolen creatures, Victimize/Bombardiers sacrifices of non-finality creatures, Pirates cleared by Conduit or Ruse, and our side of Toxic Deluge or Living Death. It produces nothing only from finality-exiled Brass returns. Those cases are real but incidental. A Brass-returned Jhoira steals two historic permanents the turn it arrives (four with Throne), so the swap stays at MODERATE confidence. A test now checks that non-finality deaths still trigger Plunderer.
- **(b) Changeling Outcast → Ragavan: REVERTED; Outcast kept.**
  - Ragavan is verified as a Legendary Creature — **Monkey Pirate**.
  - A Brass-returned Outcast is a hasty 4/4 that **can't be blocked**, so it always connects. That feeds Beckett's three-Pirate theft condition and triggers Breeches, Brazen Plunderer, Ramirez and Shared Animosity. A returned Ragavan is a blockable 4/4 whose Treasure and card need the same connection.
  - Ragavan in over a different incumbent: considered against Talisman of Indulgence (not clearly better, now that a land is cut) and Corsair Captain (lord + Treasure). Rejected.
  - The seven-swap full 100 "REV2 + Ragavan over Outcast" was built and kept as an alternative (RETAIN_ALTERNATIVE).

**4. CI: added.** The new focused workflow `.github/workflows/m7-admiral-brass-unsinkable.yml` runs on pull requests into `chatgpt-cycle76-m6-refinement`. Its path triggers include `data/grixis/m7/**`, `data/grixis/m6/**`, the gate and bundle-checker scripts, the three test files and the workflow itself. It checks out the exact PR head, runs `pytest` on `tests/test_m7_admiral_brass_unsinkable_candidate.py`, `tests/test_m6_admiral_brass_unsinkable_m7_mechanics.py` and `tests/test_m6_admiral_brass_unsinkable_m7_ij.py`, then runs `scripts/grixis_m7_decision_gate.py --check --check-sources`. Exact-head run URLs and conclusions are recorded in the PR #651 body. They are not recorded in this file because adding them would change the hashed head.

**Open-ended rule.** Five was a floor. REV2 has six swaps because two outside cards beat specific incumbents and one rev1 swap lost. The pool compares 9 complete 100-card files, listed below.

## Provenance
- Canonical source (read-only): `corymstover/grixis-commander-encyclopediaGPT` `refinement/decklists/Admiral_Brass_Unsinkable_Whole_List_Approval_Candidate_2026-10-13.txt`, physical raw SHA-256 `056f0369bc4b11967365eef65d15a806b2d0f673ecf8097b028ffcdfd472f5cc`, vendored byte-exact at `data/grixis/m7/baseline_sources/Admiral_Brass__Unsinkable_approved_source_2026-10-13.txt`.
- The historical approval digest `e66e3a59…dd39` in `state/current_deck_overrides.json` does **not** match those bytes, and no normalization reproduces it. Both values are recorded separately; nothing was re-approved. The baseline logical hash matches the registry: `lh1:3ff7f503…5c05`.
- Candidate: `data/grixis/m7/candidate_lists/Admiral_Brass__Unsinkable.txt`, raw `baf0d451bc5fa1f66065d04fa7826610337d1ffa802eebf6c78ba282a784e967`, logical hash `lh1:83da1314067759d3e6406907f06714ba225f62ece24f80bf9a4adeab4458f6c7`.
- Live Scryfall (2026-10-23): 109 names plus one second-pass batch of 5 new names. All are Commander-legal and inside UBR identity. Game Changers in the list: Ancient Tomb, Cyclonic Rift, Demonic Tutor, Fierce Guardianship, Jeska's Will, Vampiric Tutor (6), which makes it **Power Bracket 4**.
- Project exceptions: none apply to this deck, and other decks' exceptions are unchanged.

## Swaps (6)
| Add | Cut | Why |
|---|---|---|
| Kitesail Larcenist | Enterprising Scallywag | Its ETB turns one artifact or creature per player into a Treasure. A Brass return is a 4/4 hasty flier that hits every opponent, and Throne doubles the ETB. |
| Timestream Navigator | Francisco, Fowl Marauder | Brass gives it haste, so with the city's blessing it can take an extra turn at once, which means another Brass trigger. |
| Warkite Marauder | Fathom Fleet Captain | Its free attack trigger neutralizes the best blocker, and Throne doubles it. |
| Jhoira, Weatherlight Corsair | Pitiless Plunderer | A Brass return gets the ETB and the attack trigger, stealing two historic permanents. Plunderer still triggers on non-finality deaths; see Response 3a. |
| Siren's Ruse | Crumbling Necropolis | Instant finality reset, ETB retrigger, protection and a Pirate draw. Lands go 34 → 33 (see Response 1). |
| Ripples of Undeath | Faithless Looting | Repeatable precombat mill 3 ahead of Brass's combat trigger, versus a one-shot looter. |

Changeling Outcast stays; rev1's Ragavan swap is reverted. The Pirate count is unchanged: 28 in the 99, 29 with the commander.

## Rules claims to attack
1. **Brass trigger timing.** It triggers at the beginning of combat on our turn. The target Pirate must already be in the graveyard when the trigger goes on the stack. Entomb, Buried Alive and Ripples of Undeath (first main phase trigger) happen before combat. Entomb also works at instant speed in upkeep.
2. **Base 4/4.** The returned Pirate's base P/T becomes 4/4. Counters, anthems (Corsair Captain, Shared Animosity) and pumps still apply on top. Haste lasts only until end of turn. The base 4/4 and the finality counter stay.
3. **Finality.** If the creature would die (destroyed, sacrificed, Living Death, Bombardiers boast), it is exiled instead. Bounce, blink or tuck move it normally and the new object has no counter. A finality Pirate that Larcenist turns into a Treasure keeps the counter, so sacrificing that Treasure exiles it.
4. **Counter removal.** Power Conduit ({2}) costs {T} plus removing a counter from our permanent, and is usable at instant speed with no summoning sickness. Its mode puts a charge counter on an artifact or a +1/+1 counter on a creature; Conduit itself is always a legal artifact target. Removing the finality counter lets the Pirate go to the graveyard and be returned again. Nesting Grounds (not included) is sorcery speed only. Soul Diviner (not included) is summoning-sick.
5. **Roaming Throne (Pirate).** Brass's trigger fires twice and each instance picks its own target, so you need **two different** Pirates in the graveyard. Targeting the same card twice means the second trigger fizzles. Throne also doubles the ETB triggers of returned Pirates (Larcenist, Jhoira, Hostage Taker, Amphin Mutineer, Coercive Recruiter, Merchant Raiders) and attack triggers (Jhoira, Warkite).
6. **Port Razer.** Each extra combat phase gives another beginning of combat, so another Brass trigger.
7. **Timestream Navigator** goes to the bottom of the library, not the graveyard, so it is not re-usable by Brass unless redrawn.
8. **Siren's Ruse.** It exiles and returns the card under its **owner's** control as a new object (CR 400.7): no finality counter, printed P/T, no haste, and ETBs trigger again. It draws a card if the card is a Pirate. A stolen creature goes back to its owner.
9. **Ripples of Undeath.** It mills three at the beginning of our first main phase, before beginning of combat, so a milled Pirate is a legal Brass target that turn. Optional: pay {1} and 3 life to take one milled card.
10. **Changeling Outcast.** It can't block and can't be blocked. Changeling works in the graveyard, so it is a legal Brass target and, once returned, a hasty unblockable 4/4 Pirate.
11. **Jhoira.** We lose life equal to each stolen permanent's MV. Watch life totals alongside shocks, Talismans, Mana Confluence, Black Market Connections, Vampiric Tutor and Reanimate.

## Adversarial scenarios (please challenge)
- **Commander removed or taxed.** Brass costs 5 plus tax. Fallbacks are castable Pirates, Kindred Discovery, Living Death/Patriarch's Bidding mass reanimation, Animate Dead and Reanimate. Protection: Lightning Greaves, Fierce Guardianship, Deflecting Swat, Counterspell, Mana Drain.
- **Bojuka Bog / Rest in Peace.** Bog in response to the trigger: the trigger fizzles, but the other Throne instance survives if its target remains. Rest in Peace switches off the reanimation half and turns mills into exile. Answers: Chaos Warp, Cyclonic Rift, Otawara and Larcenist (which hits artifacts and creatures only, **not** enchantments).
- **Finality cases.** Sacrifice and destroy exile the creature. Bounce resets it. Blink resets it and also clears the base 4/4 and haste. Siren's Ruse resets one Pirate at instant speed (rev2 add). Counter-moving onto an opponent's creature would need Nesting Grounds, which isn't in the list.
- **Throne doubling.** Is two-distinct-target availability realistic on turns 5–6? Sources: mill 4 on Brass ETB, Ripples' mill 3 every turn, Entomb/Buried Alive.
- **Combat disruption.** Fog, Settle the Wreckage, blockers with deathtouch. Warkite and Larcenist mitigate this; there's no fog protection.
- **Resource pressure.** Opponents' Treasures from Larcenist, and Jhoira's life loss.
- **Symmetric Living Death / Patriarch's Bidding.** Opponents get their creatures back too. Living Death **exiles** our finality Pirates instead of returning them, so sequence it before rebuilding.
- **Payable win lines.** Combat damage scaling via Shared Animosity, Angrath's Marauders, Port Razer combats, Navigator extra turns and Broadside Bombardiers reach. No deterministic two-card infinite was identified. Commander Spellbook was **not** queried live this run, so please check.

## Rejected candidates (attack these too)
- Ragavan (over Changeling Outcast): retained as an alternative (seven-swap file).
- Prismari Command (over Feed the Swarm): rejected (seven-swap file).
- Ghostly Flicker, Spectral Sailor: rejected.
- Nesting Grounds: not selected (rev1 alternative; its target land is now cut).
- Also rejected: Ashnod's Altar, Spawning Pit, Dire Fleet Ravager, Captivating Crew, Pirated Copy, Soul Diviner, Back in Town, Big Score, Grim Captain's Locker, Arm-Mounted Anchor, Port of Karfell, Herald's Horn, Maskwood Nexus, Karlach, Glint-Horn Buccaneer, Windfall.
- Disclosure: an earlier GrokBot advisory suggested Dire Fleet Ravager; this run reverses that because of self-damage and redundancy.

## Whole-deck comparison (9 full 100-card configurations; quantity-counted, rev2 snapshot)
| config | raw SHA-256 | lands | rocks | U/B/R land sources | U/B/R pips | nonland avg MV | judgment |
|---|---|---|---|---|---|---|---|
| BASELINE | `056f0369…72f5cc` | 34 | 8 | 21/19/18 | 23/25/22 | 2.954 | RETAIN_CANONICAL_AUTHORITY |
| PREFERRED_SIX_REV2 | `baf0d451…84e967` | 33 | 8 | 20/18/17 | 27/25/20 | 3.0 | PROVISIONAL_LOCAL_BEST_IN_TESTED_POOL (REV2, after ChatGPT review) |
| PRIOR_FIVE_REV1 | `953a1f8c…0d2475` | 34 | 8 | 21/19/18 | 26/23/22 | 3.0 | SUPERSEDED_HISTORY |
| SEVEN_REV2_RAGAVAN_OVER_OUTCAST | `bbcac212…111419` | 33 | 8 | 20/18/17 | 27/24/21 | 3.0 | RETAIN_ALTERNATIVE |
| SEVEN_REV2_PRISMARI | `a5a027fe…2e45a6` | 33 | 8 | 20/18/17 | 28/24/21 | 3.015 | REJECT |
| SIX_REV2_KEEP34_MINUS_TALISMAN | `747d89d1…8b8c15` | 34 | 7 | 21/19/18 | 27/25/20 | 3.015 | REJECT |
| REV1_SIX_NESTING_GROUNDS | `873ed934…420022` | 34 | 8 | 20/18/17 | 26/23/22 | 3.0 | HISTORY / RETAIN_ALTERNATIVE (built on rev1 five) |
| REV1_SEVEN_NESTING_ALTAR | `94ac3d88…67d88d` | 34 | 8 | 20/18/17 | 26/23/22 | 3.015 | HISTORY / REJECT (built on rev1 five) |
| REV1_EIGHT_RAVAGER_CREW_PIT | `54feef8c…4d651f` | 34 | 7 | 21/19/18 | 24/24/22 | 3.015 | HISTORY / REJECT (built on rev1 five) |

All per-contender records (named cut, judgment, confidence, reason) are in `data/grixis/m6/certification_preflight/Admiral_Brass__Unsinkable_M6_I_local_best_20261023.md` and in the packet's `material_candidates`.

## M6 I / J evidence (candidate-specific; Admiral Beckett Brass rev2 pattern)
- I certificate: `data/grixis/m6/ij/certificates/admiral-brass-unsinkable-m7.json`. It is local to the tested pool (9 configurations), not global.
- Tested pool: `data/grixis/m6/ij/tested_pools/Admiral_Brass__Unsinkable_M7_rev2_tested_configurations_20261023.json` (renamed from the rev1 five-configuration file, with the rev1 hashes kept as history).
- J bundle: `data/grixis/m6/ij/revision_bundles/admiral-brass-unsinkable-m7.json`. It passes `grixis_m6_bundle_check.validate_bundle`.
- Oracle/legality: `data/grixis/m6/oracle_snapshots/Admiral_Brass__Unsinkable_M7_rev2_Scryfall_20261023.json`. The rev1 109-name snapshot is kept as history.
- Rules: `data/grixis/m6/rules_snapshots/Admiral_Brass__Unsinkable_M7_20261023.md`. The mana and red-team memos are under `data/grixis/m6/certification_preflight/`.
- Disclosed checker changes from rev1, unchanged in rev2: `grixis_m6_bundle_check.py` has a narrow, fail-closed registry-bound digest-discrepancy acceptance and accepts the "**Technically independent:** NO." disclosure wording.

## Open items
- Phase-B is a finite bounded rules model, not a game engine, and there are no win rates.
- The 33-vs-34-land call and Ragavan-vs-Outcast are judgment calls at MODERATE confidence.
- Commander Spellbook was not queried live.
- Owner decision: none. The list is not approved and not canonical.

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
1x Changeling Outcast
1x Chaos Warp
1x Coercive Recruiter
1x Command Tower
1x Corsair Captain
1x Counterspell
1x Siren's Ruse
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
1x Ripples of Undeath
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
Raw SHA-256 of candidate file: `baf0d451bc5fa1f66065d04fa7826610337d1ffa802eebf6c78ba282a784e967`
