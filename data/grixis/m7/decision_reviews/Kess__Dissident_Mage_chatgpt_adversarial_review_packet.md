# Kess, Dissident Mage — ChatGPT adversarial review packet (M7, 2026-10-23)

**Status:** RESEARCH ONLY — NOT APPROVED, NOT CANONICAL, NOT OWNER-PRESENTABLE. Readiness `RESEARCH_ONLY_WITHDRAWN_NOT_OWNER_PRESENTABLE`.
- Blocker: one genuine swap was found (+Mana Drain −Personal Tutor), and the five-swap floor was not met without padding.
- Only Cory can approve.

**Reviewer instruction:** attack this conclusion. Show any of the following:
- a rules error;
- an illegal card;
- an unpayable line;
- an unsupported combo claim;
- a reason the Mana Drain swap is not a genuine improvement, or a genuine swap we missed;
- an owner-direction contradiction we missed (one is already flagged below).

No win rates were measured. EDHREC prevalence, stats.cedh.events staple rates and EDHTop16 conversion are discovery evidence only.

## Provenance
**Canonical source (read-only).**
- Repository `corymstover/grixis-commander-encyclopediaGPT` main `9b26aa28fc7e16f6652aaec292b4edf84e20db71`.
- File `refinement/decklists/Kess_Dissident_Mage_Approved_2026-10-14.txt`, git blob `4e3feb62796a8d1371e6872ce960376993275d7e`, introduced by canonical commit `b83e7d0` (2026-10-14).
- Canonical commit record: 9b26aa28fc7e16f6652aaec292b4edf84e20db71 (blob 4e3feb62, introduced by b83e7d0 2026-10-14; registry source_commit 1836b97 same bytes).
- Raw SHA-256 `93d27d605bbdf0737ebe32c911fafe3a002b06d7d90f00b7bfc402cb1d3faccb`. This equals the overrides `approved_list_sha256`, the registry `recorded_sha256` and the Pass C seal `canonical_raw_sha256`.
- Vendored byte-exact at `data/grixis/m7/baseline_sources/Kess__Dissident_Mage_approved_source_2026-10-14.txt`.

**Hashes.** The registry `recorded_sha256` equals the raw bytes, so **no provenance exception** is used.
- Logical hash `lh1:d89d5778424e5aa61244cd1aea7aa6967ad678860c59cafbb62e14abbe6dfa9b`.
- The registry canonical export `exports/grixis-archidekt/kess-dissident-mage.txt` (raw `94dee35afe9fdb9871ee84abc0ac616ab23e133198d7d5d0ddba090b6942f2bd`) is the same 100 in `1 Card` export format, with the same logical hash. It is current, not stale.
- Research candidate `data/grixis/m7/candidate_lists/Kess__Dissident_Mage.txt`, raw `d8fc71c1ee48948509de155b3b93571c2d9d0e5f426fb5b5679478dadf7ae57b`, logical `lh1:066fc59a46090816ed94931d072fec96fd2d511d4590097d930f9be7ce4810b0`. Serialized commander first, then case-insensitive alphabetical, terminal newline.

**Discrepancies.**
- The canonical file holds every card 1x, with no basics (100 physical cards, 27 lands), so there are no basic-quantity normalisation issues.
- The tracker row still reads PENDING while the overrides record the list as approved and locked. Not changed here.

## Commander model (attack this first)
Kess, Dissident Mage ({1}{U}{B}{R} 3/4 flying Legendary Creature — Human Wizard; `ncc`, released 2022-04-29; legal, not a Game Changer).

- **Permission:** once during each of your turns, cast an instant or sorcery from your graveyard, paying its costs (an alternative cost is allowed, CR 118.9) with normal timing (CR 117.1a). If it would go to the graveyard, it is exiled instead (replacing CR 608.2n).
- **No permission on opponents' turns.** Escape/flashback casts do not use Kess's permission.
- **A new Kess object** (Displacer Kitten blink, CR 400.7) grants another cast that turn.
- **Signature line:** cast Demonic Consultation (or Tainted Pact) from hand to find Thassa's Oracle, cast Oracle, then recast the spell from the graveyard via Kess with Oracle's trigger on the stack.
- **Engines:** Gifts Ungiven, Intuition, Entomb, Faithless Looting, Dragon's Rage Channeler and Ledger Shredder fill the graveyard; Underworld Breach + Lion's Eye Diamond / Lotus Petal + Brain Freeze or Wheel of Fortune; Grinding Station; Reanimate; Final Fortune (an extra turn is another Kess turn).

## Swaps (1 — below the five-swap floor; RESEARCH_ONLY)
**+Mana Drain −Personal Tutor (MODERATE confidence).**
- Mana Drain ({U}{U} instant) is the most-played non-incumbent card for Kess: EDHREC cEDH 234/387 (60.5%), stats.cedh.events 51.7% of 87 Kess decklists, repo EDHTop16 one-year 32 entries / 4 top cuts.
- Recast via Kess in your precombat main phase or combat, its mana arrives in the postcombat main phase of the same turn (ruling 2020-11-10; CR 505.1, 106.4). The blue pitch count for Force of Will / Force of Negation stays 26.
- Personal Tutor ({U} sorcery) is the least-adopted card in the 99 (EDHREC cEDH 26/387; absent from the cedh.events staple list). It puts a sorcery on top, cannot find the instant wins, and overlaps Mystical Tutor inside a 14-card tutor suite.
- **Data caveat:** EDHTop16 one-year Kess entries with Mana Drain 32 (4 top cuts), conversion 0.125 vs field 0.1207 (58 entries) — neutral, small sample.
- **Owner-direction flag:** Personal Tutor is an owner addition from the 2026-10-14 rebuild. The owner-respecting fallback **+Mana Drain −Deadly Rollick** is staged as a complete 100. **Owner call.** The zero-swap baseline remains available.

**Staged owner decisions (RETAIN_ALTERNATIVE, not counted):**
- Grim Tutor over Demonic Counsel (Counsel is an accepted owner keep; Grim Tutor cEDH 88/387 vs 25/387, but cEDH events only 42.5%).
- Jeska's Will over Ledger Shredder (Pass C test configuration; owner-cut card).
- Frantic Search over Personal Tutor (Pass C test configuration; owner-cut card).

**Rejected:** Spell Pierce (dominated by Mana Drain; the two-card package also cuts Fellwar Stone), Praetor's Grasp (low confidence over Ponder), Cyclonic Rift (equal adoption to Into the Flood Maw; adds a Game Changer), Notion Thief, Narset, Parter of Veils and Hexing Squelcher (owner spine Ledger Shredder), Undercity Sewers, Urza's Saga and Exotic Orchard (City of Traitors), Mnemonic Betrayal (exiles itself), Lim-Dûl's Vault, Snap, Muddle the Mixture, Dispel, Timetwister (anti-Kess), Lightning Bolt; The One Ring, Opposition Agent and Dauthi Voidwalker (owner-rejected).

**Invalid:** Manamorphose (R/G hybrid) and Silence (W), off-identity.

## Pass C requested tests (bounded; `tests/test_m6_kess_dissident_mage_m7_mechanics.py`)
Pass C said **NEEDS TESTING** (retain the canonical deck). It asked for matched comparisons of the baseline with +Jeska's Will −Ledger Shredder and +Frantic Search −Personal Tutor: real coloured sources, land-vs-rock payment, first Kess deployment, own-turn graveyard casts, four-type delirium, blue Force-pitch availability and opponents' hand sizes. The Pass C receipt is non-independent and owner-equivalent.

**Blue Force-pitch availability** (exact; P(another blue card | Force in hand)), turns 1/3/6:

| List (blue cards) | T1 | T3 | T6 |
|---|---|---|---|
| Baseline (26) | 0.8383 | 0.9146 | 0.9682 |
| +Will −Shredder (25) | 0.824 | 0.9042 | 0.9627 |
| Candidate (26) | 0.8383 | 0.9146 | 0.9682 |

**Jeska's Will:** net mana = target opponent's hand size − 3 (exact table 0–7 cards); no hand-size logs exist, so no distribution is claimed.

**Frantic Search:** P(three lands in play) turns 3–6 0.4658/0.5485/0.6236/0.6912 (seed 26, N=200000); rocks are not refunded.

**First Kess deployment** (four mana including U, B, R; conservative): turns 3–6 0.1215/0.3577/0.4488/0.5328, identical for every non-land swap.

**Demonic Counsel delirium** (no Demon in the 99; seeded proxy): turn 6 baseline 0.0922 / 0.401, candidate 0.0868 / 0.3858, +Frantic −Personal 0.086 / 0.4013.

No games were simulated and no win rates were measured.

## Combos (Commander Spellbook find-my-combos, every list, JSON in research_challengers)
- Baseline: 6 complete combos (742-1295, 1295-3093, 1368-1414-4856, 1368-3518-4856, 1368-2706-3518 and 1368-3698--44).
- Candidate: 6 (unchanged).
- +Jeska's Will −Ledger Shredder adds 1368-1878-2706 (7); +Frantic Search −Personal Tutor adds 1368-2196-3766 (7). Every other staged alternative stays at 6.

## Adversarial scenarios (please push here)
1. Is Personal Tutor better in this list than its adoption suggests (topdecking Wheel of Fortune or Reanimate, then a Kess recast for a second tutor)?
2. Should Deadly Rollick be the cut instead, respecting the owner's addition?
3. Is {U}{U} too strict for a list that often taps out for Kess on turn 3–4?
4. Does Grim Tutor deserve Demonic Counsel's slot given the low delirium rates?
5. Is there an own-turn interaction card better than Mana Drain that the owner did not remove or reject?

## Tested pool (14 configurations; `data/grixis/m6/ij/tested_pools/Kess__Dissident_Mage_M7_tested_configurations_20261023.json`)
1. BASELINE
2. CANONICAL_EXPORT
3. RESEARCH_ONE_SWAP
4. ALT_MANA_DRAIN_OVER_DEADLY_ROLLICK
5. ONE_SPELL_PIERCE_OVER_PERSONAL_TUTOR
6. TWO_MANA_DRAIN_SPELL_PIERCE
7. ONE_GRIM_TUTOR_OVER_PERSONAL_TUTOR
8. ONE_GRIM_TUTOR_OVER_DEMONIC_COUNSEL
9. ONE_PRAETORS_GRASP_OVER_PONDER
10. ONE_CYCLONIC_RIFT_OVER_INTO_THE_FLOOD_MAW
11. ONE_NOTION_THIEF_OVER_LEDGER_SHREDDER
12. ONE_UNDERCITY_SEWERS_OVER_CITY_OF_TRAITORS
13. PASS_C_JESKAS_WILL_OVER_LEDGER_SHREDDER
14. PASS_C_FRANTIC_SEARCH_OVER_PERSONAL_TUTOR

## Distinctness (disclosed)
Nonbasic names shared with the Grixis cEDH cores (registry Archidekt exports), candidate/baseline:
- Kefka, Court Mage 80/80
- Jeleva, Nephalia's Scourge 77/78
- Inalla, Archmage Ritualist 71/71
- Evelyn, the Covetous 71/71

This is the cEDH staple core. Kess is commander-first through the own-turn graveyard recast. Cards unique to Kess against all four: Deadly Rollick, Dragon's Rage Channeler, Fiery Islet, Gifts Ungiven, Grinding Station, Ledger Shredder, Mana Drain, Snapcaster Mage and Training Center.

## Infra disclosure
- No new shared-infrastructure edits. The gate, schema, checker and shared tests on this branch are byte-identical to PR #673 head ee2abd0a (carried from the #651 chain); there are no registry edits.
- New files are deck-scoped artifacts, three deck tests and the workflow `.github/workflows/m7-kess-dissident-mage.yml`.
- Merge order: #651 → … → #672 → #673 → this PR (#674).
