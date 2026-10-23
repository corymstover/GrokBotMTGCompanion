# Kefka, Court Mage // Kefka, Ruler of Ruin — ChatGPT adversarial review packet (M7, 2026-10-23)

**Status:** RESEARCH ONLY — NOT APPROVED, NOT CANONICAL, NOT OWNER-PRESENTABLE. Readiness `RESEARCH_ONLY_WITHDRAWN_NOT_OWNER_PRESENTABLE`.
- Blocker: one genuine swap was found (+Dualcaster Mage −Culling the Weak), and the five-swap floor was not met without padding.
- Only Cory can approve.

**Reviewer instruction:** attack this conclusion. Show any of the following:
- a rules error;
- an illegal card;
- an unpayable line;
- an unsupported combo claim;
- a reason the Dualcaster Mage swap is not a genuine improvement, or a genuine swap we missed;
- an owner-direction contradiction we missed (one is already flagged below).

No win rates were measured. EDHREC prevalence and EDHTop16 conversion are discovery evidence only.

## Provenance
**Canonical source (read-only).**
- Repository `corymstover/grixis-commander-encyclopediaGPT` main `9b26aa28fc7e16f6652aaec292b4edf84e20db71`.
- File `refinement/decklists/Kefka_Court_Mage_Approved_2026-10-14.txt`, git blob `84dbe0b40730cb3a71b63f4183af63af95175ca9`. It was introduced by canonical commit `7bf011ac` (2026-10-14 19:26:31 CDT).
- Canonical commit record: 9b26aa28fc7e16f6652aaec292b4edf84e20db71 (blob 84dbe0b4, introduced by 7bf011ac 2026-10-14; registry source_commit 1836b97 same bytes).
- Raw SHA-256 `cd36192fedda7a4f54570fb8b8e4605147b40f9254e6985729097fc998f17b03`. This equals the tracker (Deck #25, index 24), the overrides `approved_list_sha256` and the registry `recorded_sha256`.
- Vendored byte-exact at `data/grixis/m7/baseline_sources/Kefka__Court_Mage_approved_source_2026-10-14.txt`.

**Hashes.** The registry `recorded_sha256` equals the raw bytes, so **no provenance exception** is used.
- Logical hash `lh1:a858b67801ed8c4703527bd43954e7263653c7b64b1cd1953db9a945d55bbd2e`.
- The registry canonical export `exports/grixis-archidekt/source-baseline/kefka-court-mage.txt` (raw `1bf9bb268230bdf1978b734b906a2d5ff44f0dd06ce8f400fc694f0f90348391`) is the same 100 in export format, with the same logical hash.
- Research candidate `data/grixis/m7/candidate_lists/Kefka__Court_Mage.txt`, raw `4adf02f9a72586b541e980218257f296a3b42bd22318bc9b59dc3dac967d210c`, logical `lh1:ba340792b7383533f17207ac48228ad283d13ad513b0b52d310e6f964f964b01`. Serialized commander first, then case-insensitive alphabetical, terminal newline.

**Discrepancies.**
- The canonical file has no terminal newline (hashed as-is). It holds 1x Island and every other card 1x: 100 physical cards and 28 lands.
- `exports/grixis-archidekt/kefka-court-mage.txt` (raw `9388bb55…`) is an older unapproved GrokBot challenger that re-adds owner-cut cards (Liliana's Caress, Dauthi Voidwalker). It is not used.
- The tracker row still reads PENDING while the overrides record the list as approved and locked. Not changed here.

## Commander model (attack this first)
Kefka, Court Mage // Kefka, Ruler of Ruin ({2}{U}{B}{R} 4/5 Legendary Creature — Human Wizard // Avatar Wizard; `fin`, released 2025-06-13; legal, not a Game Changer).

- **Enter / attack trigger:** each player discards a card, then you draw a card for each card type among the discarded cards (CR 205.2a types; supertypes do not count).
- **Harmonic Prodigy** makes it trigger an additional time (CR 603.2d); Kefka is a Wizard on both faces.
- **Repeat:** Essence Flux and Displacer Kitten blink; Phantasmal Image, Phyrexian Metamorph, Molten Duplication and Saw in Half copy (legend rule CR 704.5j).
- **Haste:** Anger in the graveyard with a Mountain-subtype land, Arena of Glory, Gogo, Mysterious Mime (CR 302.6, 702.10b).
- **Transform:** {8}, sorcery speed; each opponent sacrifices a permanent. The back face draws on actual life loss during your turn. Not an automatic turbo line.
- **Discard payoffs:** Tinybones, Bauble Burglar and Waste Not.
- **Backups:** Thassa's Oracle + Demonic Consultation / Tainted Pact; Underworld Breach + Lotus Petal or Lion's Eye Diamond + Brain Freeze, Wheel of Fortune + Jeska's Will, or LED + Wheel.

## Swaps (1 — below the five-swap floor; RESEARCH_ONLY)
**+Dualcaster Mage −Culling the Weak (MODERATE confidence).**
- Dualcaster Mage ({1}{R}{R} flash Human Wizard) makes three owner-added spine cards into two-card lines: Molten Duplication (147-5487, infinite hasty tokens), Saw in Half (147-500) and Essence Flux (147-4598). Spellbook 6 → 9.
- With Harmonic Prodigy, its enter trigger happens twice; the spare copy may target Kefka (CR 707.10c), so each iteration can also give a Kefka enter trigger.
- Culling the Weak is not an owner explicit keep. It needs a creature to sacrifice (P(an MV≤2 creature seen) 0.4115–0.6075 on turns 1–6) and makes only black.
- **Data caveat:** neutral to slightly against. EDHREC cEDH 497/2232 vs 861/2232; EDHTop16 one-year conversion 0.1706 (252) vs 0.1867 (557), inside noise (difference SE ≈0.027).
- **Owner-direction flag:** the Molten Duplication kill does not require Kefka. That is close to the owner's reason for rejecting the Valley Floodcaller / Banishing Knack / Retraction Helix bounce package. Mitigation: one slot, built from cards already in the deck, and it loops Kefka through Prodigy. **Owner call.**
- **Staged alternatives:** Dualcaster Mage over Diabolic Intent (alternative cut, also 9 combos); Talisman of Indulgence over Culling the Weak (fallback if Dualcaster is declined). The zero-swap baseline remains available.

**Pass C tests, not clearly better:**
- Entomb over Demonic Counsel or over Borne Upon a Wind: the Anger haste window roughly doubles (turn 5: 0.0863 → 0.1642), but the absolute gain is small, it tutors nothing to hand and it is exposed to graveyard hate.
- Dragon's Rage Channeler over Tinybones, Bauble Burglar: Tinybones is an owner keep; only Demonic Counsel uses delirium.

**Rejected:**
- Mockingbird over Molten Duplication (six mana to copy Kefka; Molten Duplication is the best Dualcaster partner).
- Spark Double over Gogo (owner keep; no haste).
- Vivi Ornitier, Mistrise Village, Strix Serenade, Praetor's Grasp, Snapcaster Mage, Flesh Duplicate, Mox Amber, Urza's Saga, Generator Servant (marginal).
- Vexing Bauble (nonbo with the deck's free spells), Defense Grid and Grinding Station (generic), Twinflame (redundant).

**Invalid:** Dockside Extortionist (banned) and Manamorphose (R/G hybrid, off-identity).

## Pass C requested tests (bounded; `tests/test_m6_kefka_court_mage_m7_mechanics.py`)
Pass C said **NEEDS TESTING**. It asked to compare the locked baseline with Entomb/Counsel and Entomb/Borne (four-type delirium before Counsel, Anger plus Mountain-subtype source, earliest Kefka attack, tutor windows, grave hate), and DRC/Tinybones only if it changes the decision. The Pass C receipt is non-independent and owner-equivalent.

**Mountain-subtype sources** (13: 4 duals plus 9 fetches), exact P(at least one) by turn 1–6: 0.6391, 0.6901, 0.7343, 0.7727, 0.8059, 0.8346.

**Anger haste window** (exact):

| Turn (seen) | Baseline | Plus Entomb |
|---|---|---|
| 1 (7) | 0.0413 | 0.0804 |
| 5 (11) | 0.0863 | 0.1642 |

**Demonic Counsel delirium** (seeded Monte Carlo, seed 25, N=200000; no Demon in the 99): turn 4 0.0659 lower / 0.4229 upper; turn 6 0.111 / 0.5463.

**Dualcaster partner access** (exact, before tutors): 0.0123 on turn 1 to 0.0367 on turn 6.

**DRC vs Tinybones:** not run as a separate measurement, because Pass C made it conditional and it does not change the decision.

No games were simulated and no win rates were measured.

## Combos (Commander Spellbook find-my-combos, every list, JSON in research_challengers)
- Baseline: 6 complete combos (742-1295, 1295-3093, 1368-1414-4856, 1368-3518-4856, 1368-1878-2706 and 1368-2706-3518).
- Candidate: 9 (adds 147-5487, 147-500 and 147-4598).
- Every staged alternative stays at 6, except Dualcaster Mage over Diabolic Intent (9).

## Adversarial scenarios (please push here)
1. Is Dualcaster Mage a Kefka card or a generic combo the owner would reject, as with the Floodcaller bounce package?
2. Is Culling the Weak actually better than its data suggest in Phantasmal Image / Simian Spirit Guide / Ragavan hands?
3. Should Diabolic Intent be the cut instead (it also needs a creature)?
4. Does Entomb deserve a slot over a weaker card than Demonic Counsel or Borne Upon a Wind?
5. Is there a haste enabler better than Arena of Glory that the owner did not remove or reject?

## Tested pool (12 configurations; `data/grixis/m6/ij/tested_pools/Kefka__Court_Mage_M7_tested_configurations_20261023.json`)
1. BASELINE
2. CANONICAL_EXPORT
3. RESEARCH_ONE_SWAP
4. PASS_C_ENTOMB_OVER_DEMONIC_COUNSEL
5. PASS_C_ENTOMB_OVER_BORNE
6. PASS_C_DRC_OVER_TINYBONES
7. PASS_C_TALISMAN_INDULGENCE_OVER_CULLING
8. ONE_MOCKINGBIRD_OVER_MOLTEN_DUPLICATION
9. ONE_VIVI_OVER_TALISMAN_CREATIVITY
10. ONE_MISTRISE_OVER_ISLAND
11. ONE_DUALCASTER_OVER_DIABOLIC_INTENT
12. ONE_SPARK_DOUBLE_OVER_GOGO

## Distinctness (disclosed)
Nonbasic names shared with the Grixis cEDH cores (registry Archidekt exports), candidate/baseline:
- Kess, Dissident Mage 80/80
- Jeleva, Nephalia's Scourge 78/78
- Inalla, Archmage Ritualist 72/73 (Inalla runs Kefka itself in its 99)
- Evelyn, the Covetous 67/68

This is the cEDH staple core. Kefka is commander-first through its discard/draw enter trigger and the copy/blink/haste spine. Cards unique to Kefka against all four: Anger, Diabolic Intent, Dualcaster Mage, Gogo, Mysterious Mime, Molten Duplication, Phantasmal Image, Phyrexian Metamorph, Starting Town, Tinybones, Bauble Burglar and Waste Not.

## Infra disclosure
- No new shared-infrastructure edits. The gate, schema, checker and shared tests on this branch are byte-identical to PR #672 head e77466fa (carried from the #651 chain); there are no registry edits.
- New files are deck-scoped artifacts, three deck tests and the workflow `.github/workflows/m7-kefka-court-mage.yml`.
- Merge order: #651 → … → #671 → #672 → this PR (#673).
