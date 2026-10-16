# Coverage audit: grixis-commander-encyclopediaGPT → GrokBotMTGCompanion (2026-10-16)

> **Provenance.** Cory ran this as a separate, read-only analysis on 2026-10-16, before the Bot cycle 45 import. These are his findings, recorded verbatim in substance as he reported them in the Bot cycle 46 brief. The companion did not re-run the audit. The archive itself is described in [README.md](README.md).

## Contents
- [Question](#question)
- [Method](#method)
- [Results](#results)
- [Estimate](#estimate)
- [Top gaps](#top-gaps)
- [How the gaps are being closed](#how-the-gaps-are-being-closed)

## Question
How much of the source repo's unique content was already carried into the companion's Grixis pages before the full archive was imported?

## Method
- **Per-line verbatim matching.** Every source line over 40 characters was normalized, and its first 60 normalized characters were matched against the companion's **62 deck pages plus 7 Grixis docs**.
- **Quote-block inventory.** The audit counted **160 quote blocks** in the companion that cite **157 source files**.

## Results
**Fully covered**
- **Final lists:** all 62. 59 are identical; 3 differ only through logged corrections ([Grixis Corrections](../Grixis%20Corrections.md)).
- **Approvals:** all 54 approval records.
- **Decision notes:** all 63 decision `.md` notes, 100% of 2,929 lines.
- **Blueprints:** 32 of 33. The missing one is `refinement/blueprints/Norman_Osborn_Green_Goblin_Commander_Blueprint_2026-10-15.md`.

**Partially covered**
| Area | Coverage |
|---|---|
| CSV candidate/decision ledgers | 8 abridged, 25 only linked. 202 of 328 CUT cards are named; KEEP reasons are not carried |
| Rules attestations (`*_Rules_Attestation.json`) | 37–38 decks, 518 rulings: about 45% |
| Abaddon Interaction Review (`refinement/rules/`) | about 30% |
| Admiral evidence JSON (Deck Quality v3) | about 50% |

## Estimate
**About 78% (range 70–85%)** of the source's unique content, weighted by unique characters: about **1.10M of 1.41M** characters.

## Top gaps
1. Rules attestations (518 rulings).
2. The Abaddon Interaction Review and the rulings in its tests (`refinement/tests/`).
3. Ledger keep/cut reasons.
4. The Norman Osborn // Green Goblin blueprint.
5. The two Admiral `Deck_Quality_v3` evidence files.
6. The Bjorna // Cecily Rule 0 variant (Lutri, Trade Secrets, Yawgmoth's Bargain as project exceptions).
7. The dependency-invalidation and Forge-qualification methods.

## How the gaps are being closed
- **All gaps:** since Bot cycle 45 the complete source is archived verbatim in [grixis-commander-encyclopediaGPT/](grixis-commander-encyclopediaGPT/README.md), so nothing is lost.
- **Gaps 1–2 and 6:** phase 2 (Bot cycle 46+) re-verifies the rulings and folds them into per-deck [interaction reviews](../interactions/README.md).
- **Gaps 3–5 and 7:** left for the later phases (candidate deep dives, decision tooling).
