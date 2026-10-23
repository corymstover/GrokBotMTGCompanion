# Jeleva, Nephalia's Scourge — ChatGPT adversarial review packet (M7, 2026-10-23)

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
- File `refinement/decklists/Jeleva_Nephalia_s_Scourge_Approved_2026-10-14.txt`, git blob `8cdc5b5a5d4d1cde1d803d2eceac95c83819be94`. It was introduced by canonical commit `d53789d1` (2026-10-14 17:03:57 CDT).
- Canonical commit record: 9b26aa28fc7e16f6652aaec292b4edf84e20db71 (blob 8cdc5b5a, introduced by d53789d1 2026-10-14; registry source_commit 1836b97 same bytes).
- Raw SHA-256 `00e3f52118f5944684ebc49a5398acf8184f7ca878e861221e4c99931191bc2f`. This equals the tracker (Deck #24, index 23), the overrides `approved_list_sha256` and the registry `recorded_sha256`.
- Vendored byte-exact at `data/grixis/m7/baseline_sources/Jeleva__Nephalia_s_Scourge_approved_source_2026-10-14.txt`.

**Hashes.** The registry `recorded_sha256` equals the raw bytes, so **no provenance exception** is used.
- Logical hash `lh1:21c3ebbd08ef90b8499cb9087e5ea26440e3b33615be0a60b8c246ab3b045c4c`.
- The registry export `exports/grixis-archidekt/jeleva-nephalias-scourge.txt` (raw `900a09d494293665662756ef2be07998b9d86af42c2a23ea54900953f9f181af`) is the same 100 in export format, with the same logical hash.
- Research candidate `data/grixis/m7/candidate_lists/Jeleva__Nephalia_s_Scourge.txt`, raw `4818b32a8f8bcbbadef7c4a46bead2b089d1e104d2faa68c4c1c14cd65ce6df1`. It is the same 100 re-serialized (commander first, then case-insensitive alphabetical, terminal newline), with the same logical hash.

**Discrepancies.** None. The canonical file has no terminal newline (hashed as-is). It holds 1x Island, 1x Swamp and every other card 1x: 100 physical cards and 27 lands.

## Commander model (attack this first)
Jeleva, Nephalia's Scourge ({1}{U}{B}{R} 1/3 flying Legendary Creature — Vampire Wizard; c13, released 2013-11-01; legal, not a Game Changer).

- **ETB:** each player exiles the top X cards of their library, where X is the mana spent to cast her.
  - Commander tax raises X (CR 903.8).
  - A blink, a reanimation or a token copy is not cast, so no mana was spent and X=0.
- **Attack trigger:** you may cast an instant or sorcery from among the cards exiled with her, without paying its mana cost.
  - Her two abilities are linked (CR 607.2a). If she leaves and returns, the old pool is lost.
  - The spell is cast during resolution, ignoring type-timing (2013-10-17 rulings); {X} is 0.
- **Harmonic Prodigy** makes both triggers trigger an additional time (CR 603.2d): two exile pools, or two free casts.
- **Line:** stage a spell on top (11 direct stagers), cast Jeleva, give her haste or cast her at end step (Torch Courier, Lightning Greaves, Arena of Glory, Borne Upon a Wind; CR 302.6, 702.10b), attack, and cast it free. Payoffs: Mind's Desire, Peer into the Abyss, Mnemonic Betrayal, Doomsday, Yawgmoth's Will and Final Fortune.
- **Backups:** Thassa's Oracle + Demonic Consultation / Tainted Pact / Doomsday, and Underworld Breach + Lion's Eye Diamond or Lotus Petal + Brain Freeze, Wheel of Fortune + Jeska's Will, or LED + Wheel.

## Swaps (0 — below the five-swap floor; RESEARCH_ONLY)
No change is counted.

**Closest call, staged as an OWNER DECISION: +Snap −Gitaxian Probe.**
- Snap is mana-neutral with two untapped lands. It saves Jeleva from removal, and the recast exiles a larger pool.
- Blocker: Gitaxian Probe has more data (17/30 vs 11/30), is free on turn 1, and is storm/Breach fuel. The case is not clearly better. **Owner call.**

**Pass C tests, measured worse:**
- Intuition over Long-Term Plans or over Scheming Symmetry: one fewer direct stager, and hostile piles fail.
- Galvanic Iteration over Borne Upon a Wind: copies are not cast, and one fewer enabler.

**Rejected:**
- Dramatic Reversal + Isochron Scepter over Scroll Rack + Personal Tutor (a generic combo: Spellbook 4821-5261, 7 → 8). It cuts the owner keep Scroll Rack and homogenizes the deck toward Kess and Kefka.
- Reanimate (generic).
- Spellseeker (over Mental Misstep: a creature-speed tutor that does not stage).
- Forbidden Orchard, Hanweir Battlements, Hall of the Bandit Lord and Starting Town (mana).
- Mox Amber, Merchant Scroll, Cruel Tutor, Insidious Dreams, Goblin Bushwhacker and Snapback.
- Twinflame and Conjurer's Closet (an uncast Jeleva has X=0).
- Savage Beating.

**Invalid:** Dockside Extortionist (banned) and Manamorphose (R/G hybrid, off-identity).

## Pass C requested tests (bounded; `tests/test_m6_jeleva_nephalias_scourge_m7_mechanics.py`)
Pass C said **NEEDS TESTING**. It asked for the baseline vs +Intuition −Long-Term Plans and vs +Intuition −Scheming Symmetry (Jeleva top-stage success, haste access, hostile Breach-pile castability), and vs +Galvanic Iteration −Borne Upon a Wind (casts vs copies). The Pass C receipt is non-independent and owner-equivalent.

**T1 stager access** (exact P(at least one direct stager)):

| Seen | Baseline (11) | Intuition swap (10) |
|---|---|---|
| 7 | 0.5736 | 0.5372 |
| 8 | 0.6246 | 0.5875 |
| 9 | 0.6699 | 0.6328 |
| 10 | 0.7103 | 0.6736 |

- Long-Term Plans' third-from-top card is captured at once by any X≥3.
- Jeleva's minimum normal cast is X=4.

**T2 Intuition hostile piles:**
- Breach / LED / Brain Freeze and Oracle / Consultation / Pact are both dead early under hostile choice.
- Triple tutor: a slower stager.
- Scheming Symmetry must target two different players (CR 115.3).

**T3 Galvanic vs Borne:**
- The copy is not cast (CR 707.10).
- 8 key targets gain nothing or are harmed.
- Enablers 4 → 3: 0.2577–0.3514 → 0.1994–0.2760.

**T4 Mox Opal:** P(at least 2 other artifacts) is 0.2277–0.4152 over 6–9 other cards, with 16 artifacts. Kept.

**T5 Spellseeker reach:** 29 instants and sorceries with MV≤2.

**T6 colour sources:** U/B/R 21/20/19.

No games were simulated and no win rates were measured.

## Combos (Commander Spellbook find-my-combos, every list, JSON in research_challengers)
Baseline = candidate: 7 complete combos (742-1295, 1295-3093, 1295-3189, 1368-1414-4856, 1368-3518-4856, 1368-1878-2706 and 1368-2706-3518).
- Every staged alternative stays at 7, except Reversal + Scepter (+4821-5261).

## Adversarial scenarios (please push here)
1. Is Snap over Gitaxian Probe actually better, given that Jeleva re-cast with tax exiles more?
2. Does an X≥4 Jeleva really make Long-Term Plans as good as a top-tutor in practice (shuffle effects, opposing Scheming Symmetry target)?
3. Is there a haste or flash enabler better than Arena of Glory or Torch Courier that the owner did not remove or reject?
4. Would Galvanic Iteration ever beat Borne in a Mind's Desire / Peer line, given that copies are not cast?

## Tested pool (11 configurations; `data/grixis/m6/ij/tested_pools/Jeleva__Nephalia_s_Scourge_M7_tested_configurations_20261023.json`)
1. BASELINE
2. CANONICAL_EXPORT
3. RESEARCH_ZERO
4. PASS_C_INTUITION_OVER_LONG_TERM_PLANS
5. PASS_C_INTUITION_OVER_SCHEMING_SYMMETRY
6. PASS_C_GALVANIC_OVER_BORNE
7. ONE_SNAP_OVER_GITAXIAN_PROBE
8. ONE_SPELLSEEKER_OVER_MENTAL_MISSTEP
9. ONE_FORBIDDEN_ORCHARD_OVER_EXOTIC_ORCHARD
10. ONE_HANWEIR_OVER_ARENA
11. TWO_REVERSAL_SCEPTER_OVER_SCROLL_RACK_PERSONAL_TUTOR

## Distinctness (disclosed)
Nonbasic names shared with the Grixis cEDH cores (canonical exports):
- Kess, Dissident Mage 78
- Kefka, Court Mage 77
- Inalla, Archmage Ritualist 68
- Evelyn, the Covetous 67

This is the cEDH staple core. Jeleva is commander-first through her top-staging and free-cast line. Cards unique to Jeleva against all four: Doomsday, Lightning Greaves, Long-Term Plans, Mind's Desire, Peer into the Abyss, Preordain, Scheming Symmetry, Scroll Rack, Sensei's Divining Top, Torch Courier and Yawgmoth's Will.

## Infra disclosure
- No shared infrastructure changed: no gate, schema, checker or registry edits.
- New files are deck-scoped artifacts, three deck tests and the workflow `.github/workflows/m7-jeleva-nephalias-scourge.yml`.
- Merge order: #651 → … → #671 → this PR.
