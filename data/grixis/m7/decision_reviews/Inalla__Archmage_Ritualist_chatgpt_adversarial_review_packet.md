# Inalla, Archmage Ritualist — ChatGPT adversarial review packet (M7, 2026-10-23)

**Status:** RESEARCH ONLY — NOT APPROVED, NOT CANONICAL, NOT OWNER-PRESENTABLE. Readiness `RESEARCH_ONLY_WITHDRAWN_NOT_OWNER_PRESENTABLE`.
- Blocker: zero genuine swaps were found, and the five-swap floor was not met without padding.
- Only Cory can approve.

**Reviewer instruction:** attack this conclusion. Show any of the following:
- a rules error;
- an illegal card;
- an unpayable line;
- an unsupported combo claim;
- a candidate that clearly beats an incumbent, including a genuine swap we missed;
- an owner-direction contradiction we missed.

No win rates were measured. EDHREC prevalence is discovery evidence only.

## Provenance
**Canonical source (read-only).**
- Repository `corymstover/grixis-commander-encyclopediaGPT` main `9b26aa28fc7e16f6652aaec292b4edf84e20db71`.
- File `refinement/decklists/Inalla_Archmage_Ritualist_Approved_2026-10-14.txt`, git blob `204b8096e4c3c642ca9ade6ea4af252c417bde2c`. It was introduced by canonical commit `afb35c06` (2026-10-14).
- Canonical commit record: 9b26aa28fc7e16f6652aaec292b4edf84e20db71 (blob 204b8096, introduced by afb35c06 2026-10-14; registry source_commit 1836b97 same bytes).
- Raw SHA-256 `81333ac71d483b667af968bf2ab221e1fa0de6edd7c2395170d15786e5b15fa3`. This equals the tracker (Deck #23, index 22) and the registry `recorded_sha256`.
- Vendored byte-exact at `data/grixis/m7/baseline_sources/Inalla__Archmage_Ritualist_approved_source_2026-10-14.txt`.

**Hashes.** The registry `recorded_sha256` equals the raw bytes, so **no provenance exception** is used.
- Logical hash `lh1:c3f633472c2acd8e07b82551fc781d5cc5dd5a56f1b6388a728fa9ef0c855ccd`.
- The registry export `exports/grixis-archidekt/inalla-archmage-ritualist.txt` (raw `45924e0eabb7a253004d5cdf69c32f7ab82d1e0e7406938a033a8f8b39026598`) is the same 100 in export format, with the same logical hash.
- Research candidate `data/grixis/m7/candidate_lists/Inalla__Archmage_Ritualist.txt`, raw `916e056ba387fc7e162a359069f11a1b59e91ffb358931742d2a0b912c6c4ed1`. It is the same 100 re-serialized (commander first, then case-insensitive alphabetical, terminal newline), with the same logical hash.

**Discrepancies.** None. The canonical file has no terminal newline (hashed as-is). It holds 1x Island, 1x Swamp and every other card 1x: 100 physical cards and 27 lands.

## Commander model (attack this first)
Inalla, Archmage Ritualist ({2}{U}{B}{R} 4/5 Legendary Creature — Human Wizard; c17, released 2017-08-25; legal, not a Game Changer).

- **Eminence** works from the command zone or the battlefield. It triggers on another nontoken Wizard entering; pay {1} to make a hasty token copy, which is exiled at the next end step.
  - It is an intervening-if trigger (CR 603.4). Tokens never trigger it.
  - If the Wizard has left, the copy uses last-known information (for example, a sacrificed Spellseeker).
- **"Tap five untapped Wizards you control: Target player loses 7 life."** The cost has no {T}, so summoning-sick Wizards and tokens can be tapped (CR 302.6).
- **Engines:**
  - Spellseeker → Culling the Weak / Burnt Offering / Sacrifice / Persist / Shallow Grave / Saw in Half lines with Scholar of the Ages (10 Spellbook combos).
  - Inalla + Bloodline Necromancer + Ruthless Technomancer (1869-2721-3719).
  - Backups: Thassa's Oracle + Demonic Consultation / Tainted Pact, and Underworld Breach + Lion's Eye Diamond + Brain Freeze / Wheel of Fortune.

## Swaps (0 — below the five-swap floor; RESEARCH_ONLY)
No change is counted.

**Strongest staged OWNER DECISION: +Dualcaster Mage −Kefka, Court Mage // Kefka, Ruler of Ruin.**
- It adds 147-500 (Saw in Half) and 147-4598 (Essence Flux), two-card instant-speed combos using cards already in the 99: 16 → 18 complete combos.
- Lands-only castability at 10 cards seen: RR 0.4605, against Kefka's five lands at 0.0958.
- Blocker: the owner removed Dualcaster Mage on 2026-10-14 ("Cut 49 baseline cards"), and re-adding removed cards is forbidden. **Owner call.**

**Pass C union (OWNER DECISION):** +Dualcaster Mage +Snapcaster Mage / −Kefka −Thundertrap Trainer, staged as a complete 100.

**Rejected:**
- Micromancer (owner-rejected; reach 20 vs Spellseeker's 33).
- Snapcaster Mage (owner-removed; the Trainer's top-4 hit is 0.973).
- Samut, Tyrant of Naktamun (owner-rejected; 5 MV).
- Spectral Arcanist (owner-rejected).
- Defense Grid and Gifts Ungiven (marginal; would cut owner additions).
- Tishana's Tidebinder, Crystal Vein, Tarnished Citadel, Jeweled Amulet, The One Ring, Mindbreak Trap and Phantasmal Image.
- Twinflame (tokens do not trigger Eminence).
- Buried Alive and Grim Tutor.

**Invalid:** Dockside Extortionist (banned) and Culling Ritual (B/G, off-identity).

## Pass C requested tests (bounded; `tests/test_m6_inalla_archmage_ritualist_m7_mechanics.py`)
Pass C said **NEEDS TESTING**. It asked for the baseline vs +Dualcaster −Kefka and vs +Micromancer −Kefka (optionally +Snapcaster −Trainer) on identical 27-land UBR mana: RR vs U castability, tutor reach and combo deltas. The Pass C receipt is non-independent and owner-equivalent.

**T1 castability** (lands only, exact):

| Seen | Dualcaster RR | Kefka 5 lands | Micromancer 4+U | Snapcaster / Trainer 2+U |
|---|---|---|---|---|
| 9 (T3 play) | 0.3846 | 0.0596 | 0.2013 | 0.7494 |
| 10 (T4 play) | 0.4605 | 0.0958 | 0.2717 | 0.8045 |

**T2 tutor reach:** Spellseeker 33, Micromancer 20. Micromancer misses 13, including Demonic Tutor, Tainted Pact, Finale of Promise, Brain Freeze and Pact of Negation.

**T3 combos:** only the Dualcaster lists add combos (+2).

**T4 Thundertrap Trainer:** 58 hits in the 99; 0.973098 in the top 4, 0.999442 with an Eminence copy.

**T5 rules facts:** Oracle text and official rulings.

No games were simulated and no win rates were measured.

## Combos (Commander Spellbook find-my-combos, every list, JSON in research_challengers)
Baseline = candidate: 16 complete combos (742-1295, 1295-3093, 1368-1414-4856, 1368-3518-4856, 1368-2706-3518, 1869-2721-3719 and ten Scholar of the Ages lines).

## Adversarial scenarios (please push here)
1. Is Kefka's legendary token copy worth {1} after the legend rule? (Its ETB still resolves.)
2. Does Defense Grid's off-turn tax (CR 601.2f, pitched FoW/Pact still pay {3}) beat any owner addition?
3. Is there a Wizard with a combo-relevant ETB, reachable by Spellseeker or the Eminence plan, that the owner did not remove or reject?
4. Would the owner reverse the Dualcaster removal given 147-500 and 147-4598?

## Tested pool (9 configurations; `data/grixis/m6/ij/tested_pools/Inalla__Archmage_Ritualist_M7_tested_configurations_20261023.json`)
1. BASELINE
2. CANONICAL_EXPORT
3. RESEARCH_ZERO
4. PASS_C_DUALCASTER_OVER_KEFKA
5. PASS_C_MICROMANCER_OVER_KEFKA
6. PASS_C_SNAPCASTER_OVER_TRAINER
7. TWO_PASS_C_COMBINED
8. TWO_DATA_DEFENSEGRID_GIFTS
9. ONE_TIDEBINDER_OVER_TRAINER

## Distinctness (disclosed)
Nonbasic names shared with the most similar approved Grixis decks (canonical exports):
- Kefka, Court Mage 72
- Kess, Dissident Mage 71
- Jeleva, Nephalia's Scourge 68
- Evelyn, the Covetous 68
- Fire Lord Azula 67

This is the cEDH staple core. Inalla is commander-first through Eminence-doubled Wizard ETBs and the tap-five finisher.

## Infra disclosure
- No shared infrastructure changed: no gate, schema, checker or registry edits.
- New files are deck-scoped artifacts, three deck tests and the workflow `.github/workflows/m7-inalla-archmage-ritualist.yml`.
- Merge order: #651 → … → #670 → this PR.
