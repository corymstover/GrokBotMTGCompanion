# Grixistax___October_2026 (Kraum, Ludevic's Opus + Tevesh Szat, Doom of Fools) — ChatGPT adversarial review packet (M7, 2026-10-23)

**Status:** RESEARCH ONLY — NOT APPROVED, NOT CANONICAL, NOT OWNER-PRESENTABLE. Readiness `RESEARCH_ONLY_WITHDRAWN_NOT_OWNER_PRESENTABLE`.
- Blocker: two genuine swaps were found (+Arcane Signet −Mox Amber, +Bitterblossom −Windfall), and the five-swap floor was not met without padding.
- Only Cory can approve.

**Reviewer instruction:** attack this conclusion. Show any of the following:
- a rules error;
- an illegal card;
- an unpayable line;
- an unsupported combo claim;
- a reason either swap is not a genuine improvement, or a genuine swap we missed;
- an owner-direction contradiction we missed.

No win rates were measured. EDHREC prevalence is discovery evidence only.

## Provenance
**Canonical source (read-only).**
- Repository `corymstover/grixis-commander-encyclopediaGPT` main `9b26aa28fc7e16f6652aaec292b4edf84e20db71`.
- File `refinement/decklists/Grixistax_October_2026_Approved_2026-10-14.txt`, git blob `86b8d18aeb44ab74a720b60e08d661d272fa98c9`, introduced by canonical commit `cc7a938` (2026-10-14).
- Canonical commit record: 9b26aa28fc7e16f6652aaec292b4edf84e20db71 (blob 86b8d18a, introduced by cc7a938 2026-10-14; registry source_commit 1836b97 same bytes).
- Raw SHA-256 `f36346d4ba965db1e098b0aa92d27a968ee3a14c74a2b9401c1a5357f83c025c`. This equals the overrides `approved_list_sha256`, the registry `recorded_sha256` and the Pass C seal `canonical_input_sha256`.
- Vendored byte-exact at `data/grixis/m7/baseline_sources/Grixistax___October_2026_approved_source_2026-10-14.txt`.

**Hashes.** The registry `recorded_sha256` equals the raw bytes, so **no provenance exception** is used.
- Logical hash `lh1:f56e9d1dfe623d6a80dc00e5563e8e3895f739559d334afe04bca64eb56a0e89`.
- The registry canonical export `exports/grixis-archidekt/grixistax-october-2026.txt` (raw `f0a28f936c03705df0e215738e4ad314d337bb3e713dcf7b2c50beba5a2f9a08`) is the same 100 in export format, with the same logical hash. It is current, not stale.
- Research candidate `data/grixis/m7/candidate_lists/Grixistax___October_2026.txt`, raw `a04f16ba3a75bd53963866fd0b18c0390af54930b5526e6893ac6c6a6503b858`, logical `lh1:81656e61ce5b299509c70da8d8d39aaa41d6ecfbf4281f05857a936575207baf`. Serialized with both `[Commander]` lines first, then case-insensitive alphabetical, terminal newline.

**Discrepancies (recorded, not changed).**
- The deck ID `Grixistax___October_2026` is a deck name, not a commander name. The commanders come from the decklist's two `[Commander]` lines and the registry.
- The tracker writes "Kraum, Ludevic's Opus // Tevesh Szat, Doom of Fools". The " // " is only a pair separator; neither commander is a double-faced card.
- The tracker row shows PENDING blueprint fields, while overrides record APPROVED / LOCKED (2026-10-14). The overrides file is not altered.

## Commander model (attack this first)
- Kraum, Ludevic's Opus: {3}{U}{R} 4/4 flying, haste, Partner. "Whenever an opponent casts their second spell each turn, draw a card." Commander 2016 (`c16`), released 2016-11-11.
- Tevesh Szat, Doom of Fools: {4}{B} planeswalker, loyalty 4, "can be your commander", Partner. "+2: Create two 0/1 black Thrull creature tokens. +1: You may sacrifice another creature or planeswalker. If you do, draw two cards, then draw another card if the sacrificed permanent was a commander. −10: Gain control of all commanders. Put all commanders from the command zone onto the battlefield under your control." Commander Legends (`cmr`), released 2020-11-20.
- Both are Commander-legal per live Scryfall and neither is a Game Changer. No exception is used. Partner rules: CR 702.124b/c; commander tax is per commander (CR 903.8).
- The deck's plan is the owner's 2026-10-14 stax shell: land and untap locks (Winter Orb, Static Orb, Tangle Wire, Contamination, Blood Moon, Magus of the Moon, Back to Basics) and taxes (Trinisphere, Damping Sphere, Chalice of the Void, Torpor Orb, Cursed Totem, Overburden). Tevesh's Thrulls pay Contamination and Tangle Wire and feed Skullclamp, Phyrexian Tower, Culling the Weak and Diabolic Intent. The wins are Helm of Obedience + Leyline of the Void / Dauthi Voidwalker and Underworld Breach lines.

## Swaps (2 — below the five-swap floor; RESEARCH_ONLY)
**+Arcane Signet −Mox Amber (MODERATE confidence; the Pass C requested test).**
- Arcane Signet makes U, B or R for the combined Partner identity (ruling 2020-11-10), including under our own Contamination, which affects lands only.
- Mox Amber makes no mana off a colourless Karn, the Great Creator (ruling 2018-04-27), and the coloured legends that enable it are Ragavan, Nimble Pilferer (MV 1), Ashiok, Dream Render and Narset, Parter of Veils (MV 3), Sheoldred, the Apocalypse (MV 4) and the five-mana commanders. Measured P(live, given deployed) turns 1–4: 0.0509/0.0859/0.1729/0.2743.
- Turn 4 (seed 27, N=40000): mean mana 3.138 → 3.193; P(Tevesh castable) 0.1526 → 0.1657; P(U) under Contamination 0.2788 → 0.3299.
- Adoption: Kraum + Tevesh cEDH 79/81 for Arcane Signet against 18/81 for Mox Amber.

**+Bitterblossom −Windfall (MODERATE confidence).**
- Bitterblossom is a Tevesh-independent token stream for Contamination (order its trigger first, CR 603.3b), Skullclamp, Phyrexian Tower, Culling the Weak, Tangle Wire and Tevesh's +1. Faerie tokens do not trigger Overburden.
- P(token engine online by turn 4): 0.1532 → 0.2309; under Contamination 0.1187 → 0.2019; under artifact hate 0.036 → 0.1071.
- Windfall refills opponents in a stax deck and is in no Spellbook combo here; Wheel of Fortune keeps the wheel lines.
- Costs: 1 life per upkeep; the blue pitch count drops 22 → 21; Windfall is in 53/81 partner cEDH lists.

**Staged owner decisions (RETAIN_ALTERNATIVE, not counted):** Opposition over Static Orb, or over Magus of the Moon. P(seen and castable by turn 4) is 0.0329 (0.0034 under Contamination), against Static Orb's 0.0599 (0.0584), and the two clash.

**Staged alternative cuts for Bitterblossom (complete 100s):** keep Windfall and cut Cyclonic Rift, or cut Magus of the Moon.

**Pass C competing cut, rejected:** +Arcane Signet −Overburden (keep Amber) measures slightly more mana (turn 4 3.225), but Overburden is an owner explicit keep whose value is the lock, which a goldfish cannot see.

**Rejected:**
- Talisman of Indulgence (dominated by Arcane Signet: P(U) under Contamination 0.2722).
- Fellwar Stone (dominated).
- Frozen Aether over Static Orb (slower).
- Strip Mine and Urza's Saga over Gemstone Caverns (broken by our own Moon effects).
- Undercity Sewers over Gemstone Caverns (enters tapped).
- City of Traitors over Arid Mesa (owner addition).
- Praetor's Grasp over Windfall.
- Snuff Out over Deadly Rollick.
- Spell Pierce and Dispel over Mental Misstep.
- Null Rod (shuts off our own 22 artifacts).
- Stasis (self-locking).
- Braids, Cabal Minion (owner-rejected Smokestack class).
- Sphere of Resistance (owner-rejected symmetric tax class).
- Valley Floodcaller (turbo creep).

**Invalid:** Archon of Emeria (W), off-identity.

## Pass C requested tests (bounded; `tests/test_m6_grixistax_october_2026_m7_mechanics.py`)
Pass C said **NEEDS TESTING** (retain the canonical deck). It asked for comparisons of the baseline with +Talisman of Indulgence −Mox Amber, +Arcane Signet −Mox Amber and any justified alternative cut, with real payability, the colourless-Karn Mox Amber case and separate Moon / Contamination / Back to Basics states. The Pass C receipt is non-independent and owner-equivalent (alias Josh-Lee-Kwai, ChatGPT/OpenAI GPT-6).

**Turn-4 mana by lock state** (seeded goldfish, seed 27, N=40000; mean mana / P(U)):

| Configuration | No lock | Contamination | Blood Moon | Back to Basics |
|---|---|---|---|---|
| Baseline | 3.138 / 0.9174 | 3.037 / 0.2788 | 3.036 / 0.7587 | 1.977 / 0.7706 |
| +Arcane Signet −Mox Amber | 3.193 / 0.919 | 3.093 / 0.3299 | 3.093 / 0.7713 | 2.024 / 0.7733 |
| +Talisman of Indulgence −Mox Amber | 3.193 / 0.9167 | 3.093 / 0.2722 | 3.093 / 0.7561 | 2.024 / 0.7683 |
| +Arcane Signet −Overburden | 3.225 / 0.9198 | 3.122 / 0.3361 | 3.122 / 0.7726 | 2.042 / 0.7737 |

**Blue Force-pitch availability** (exact; P(another blue card | Force in hand)), turns 1/3/6:

| List (blue cards) | T1 | T3 | T6 |
|---|---|---|---|
| Baseline (22) | 0.7748 | 0.8663 | 0.9404 |
| Candidate (21) | 0.756 | 0.851 | 0.9306 |

No games were simulated and no win rates were measured.

## Combos (Commander Spellbook find-my-combos, every list, JSON in research_challengers)
Six complete combos in the baseline, the candidate and every alternative:
- 1368-1414-4856 (Underworld Breach + Lotus Petal + Brain Freeze)
- 1368-3518-4856 (Underworld Breach + Lion's Eye Diamond + Brain Freeze)
- 1368-1878-2706 (Underworld Breach + Wheel of Fortune + Jeska's Will)
- 1368-2706-3518 (Underworld Breach + Lion's Eye Diamond + Wheel of Fortune)
- 2581-5065 (Helm of Obedience + Dauthi Voidwalker)
- 2163-5065 (Helm of Obedience + Leyline of the Void)

Game Changers 22 → 22. Bracket 5 (cEDH).

## Adversarial scenarios (please push here)
1. Is Mox Amber better than measured because tutors find Ragavan, or because Sheoldred and Narset come down earlier than the goldfish assumes?
2. Does Windfall's refill under Narset, Parter of Veils or Notion Thief outweigh Bitterblossom's stream in real pods?
3. Does Bitterblossom's life loss, together with Necropotence, Ancient Tomb and Mana Vault, cost games against aggressive cEDH starts?
4. Should Opposition replace Static Orb even with the measured deployability gap?
5. Should the owner revisit the Torpor Orb / Overburden tension (Torpor Orb ruling 2024-04-12)?

## Tested pool (12 configurations; `data/grixis/m6/ij/tested_pools/Grixistax___October_2026_M7_tested_configurations_20261023.json`)
1. BASELINE
2. CANONICAL_EXPORT
3. RESEARCH_TWO_SWAP
4. PASS_C_TALISMAN_OF_INDULGENCE_OVER_MOX_AMBER
5. PASS_C_ARCANE_SIGNET_OVER_OVERBURDEN_KEEP_AMBER
6. ARCANE_SIGNET_ONLY
7. BITTERBLOSSOM_OVER_CYCLONIC_RIFT_KEEP_WINDFALL
8. BITTERBLOSSOM_OVER_MAGUS_OF_THE_MOON_KEEP_WINDFALL
9. STAGED_OPPOSITION_OVER_STATIC_ORB
10. STAGED_OPPOSITION_OVER_MAGUS_OF_THE_MOON
11. REJECT_FROZEN_AETHER_OVER_STATIC_ORB
12. REJECT_STRIP_MINE_OVER_GEMSTONE_CAVERNS

Configurations 4, 5 and 7–12 are complete 100s built on the candidate (they keep its other swap), so each differs from it in one slot; ARCANE_SIGNET_ONLY is the baseline with only +Arcane Signet −Mox Amber. The goldfish mana rows above compare single rock swaps on the baseline.

## Distinctness (disclosed)
Nonbasic names shared with the Grixis cEDH cores (registry Archidekt exports), candidate/baseline:
- Kefka, Court Mage 68/67
- Rograkh, Son of Rohgahh + Silas Renn 65/66
- Kess, Dissident Mage 65/65
- Jeleva, Nephalia's Scourge 64/64

This is the cEDH staple core. Grixistax is commander-first through Tevesh's tokens feeding the stax pieces. Bitterblossom is in none of the four; Mox Amber is shared with Rograkh/Silas, and Windfall with Rograkh/Silas and Kess.

## Infra disclosure
- No new shared-infrastructure edits. The gate, schema, checker and shared tests on this branch are byte-identical to PR #674 head b505d828 (carried from the #651 chain); there are no registry edits.
- New files are deck-scoped artifacts, three deck tests and the workflow `.github/workflows/m7-grixistax-october-2026.yml`.
- Merge order: #651 → … → #673 → #674 → this PR (#675).
