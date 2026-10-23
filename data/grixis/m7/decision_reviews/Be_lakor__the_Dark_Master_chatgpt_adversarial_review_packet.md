# Be'lakor, the Dark Master — ChatGPT adversarial review packet (M7, 2026-10-23)

**Status:** REVIEW CANDIDATE — NOT APPROVED, NOT CANONICAL. REVIEW_READY_NOT_OWNER_APPROVED. Only Cory can approve.

**Reviewer instruction:** attack this list. Show any rules error, illegal card, unpayable line, unsupported combo claim, or a
candidate that clearly beats an incumbent. No win rates were measured, and EDHREC prevalence is discovery evidence only.

## Provenance
- **Canonical source (read-only):** `corymstover/grixis-commander-encyclopediaGPT`,
  `refinement/decklists/Be_lakor_the_Dark_Master_Approved_2026-10-13.txt` (commit 1836b97).
  - Raw SHA-256: `3abc951606a6db2b17ea2aceb471fc2ef4c55e2ef082d49d9140a83b2491155e`.
  - Vendored byte-exact at `data/grixis/m7/baseline_sources/Be_lakor_the_Dark_Master_approved_source_2026-10-13.txt`.
- **Hashes:** the registry's `recorded_sha256` equals the raw bytes (`recorded_matches_raw: true`), so **no provenance exception** is used.
  The baseline logical hash equals the registry: `lh1:ece0a3ce…3551`.
- **Physical count:** 94 rows = 100 cards (Island x3, Mountain x2, Swamp x4). There are 36 lands, 7 static rocks and 25 printed Demons (commander included).
- **Key discrepancy (disclosed):** `state/current_deck_overrides.json` keys this deck as `Be_lakor_the_Dark_Master` (single underscore),
  while the tracker/registry id is `Be_lakor__the_Dark_Master`. Overrides were not altered.
- **Candidate:** `data/grixis/m7/candidate_lists/Be_lakor__the_Dark_Master.txt`.
  - Raw: `62a96b4f39584fa38947843bea352de923b29d7b266b57fce5918802a79b57bf`.
  - Logical: `lh1:41e4055c616d8e51c7c6019264737fa2300c5bf2609f4b3d9aad226cb0067ccf`.
  - Baseline order, with five in-place substitutions.
- **Live data:** live Scryfall data (2026-10-23) lives only in the candidate snapshot (101 cards; zero Oracle diffs vs the frozen cache).
  The frozen cache was not written. All cards are Commander-legal and within UBR.
- **Game Changers (5, unchanged):** Ancient Tomb, Cyclonic Rift, Demonic Tutor, Fierce Guardianship, Vampiric Tutor → **Power Bracket 4**.

## Commander model (attack this first)
- **Prince of Chaos (ETB):** draw X and lose X, where X is the number of Demons you control, counted when the trigger resolves.
- **Lord of Torment:** whenever *another* Demon you control enters, *it* deals damage equal to its power to any target.
  This means the entering Demon's power is the payload. A 0-power Demon deals 0. Heartless Summoning's −1/−1 costs 1 damage per hit.
- **Copies:** Molten Echoes, Spark Double, Rite of Replication and Reflections of Littjara copies are Demons entering, so they retrigger Lord
  (and copied ETBs). Legendary copies die to the legend rule (704.5j) after their triggers are put on the stack.

## Swaps (5 — the floor, not padded)
| Add | Cut | Why |
|---|---|---|
| Desecration Demon (OFF-RANKING) | Dream Devourer | 6/6 flier for 4. The Lord hit is 0 → 6 at nearly the same curve slot. Devourer's foretell discount is the loss. |
| Kindred Dominance | Blasphemous Act | Naming Demon is one-sided: our Demons, Roaming Throne and Spark Double survive, and only Ancient Cellarspawn of ours dies. Act killed our own board. |
| Demonlord Belzenlok | Rakdos, Patron of Chaos | Copyable card-advantage ETB (draws until MV<4) plus a 6-power hit. Rakdos lets the opponent choose the punisher option and does nothing on entry. |
| Reaper from the Abyss | Bloodthirster | Repeatable non-Demon removal each end step via morbid, fed by Desecration's sacrifices, wipes and Lord kills. The extra combat has no Be'lakor synergy. |
| Herald's Horn | Fellwar Stone | {1} off every Demon, including Be'lakor, plus a Demon reveal each upkeep. Fellwar's colors depend on opponents. |

**Net:**
- Lands 36 → 36; rocks 7 → 6 (43 → 42 static sources); Demons 25 → 25.
- Demon power sum 129 → 135.
- Pips U/B/R 15/58/20 → 15/65/17.
- Average nonland MV 4.109 → 4.125.
- P(≥6 lands-or-rocks in the top 12, before reducers) 0.425 → 0.396.

## Combos (Commander Spellbook find-my-combos, both lists, JSON in research_challengers)
- Both lists: exactly **one** included combo, Be'lakor + Rite of Replication (1744-4071). Spellbook calls it "near-infinite".
  It is **finite**: 25 Lord triggers × 6 = 150 damage, or 50 triggers with Roaming Throne naming Demon. The five token Prince
  triggers can cost about 25 life, so stack them under the Lord triggers.
- No infinite combo exists and none was added. Liliana's Contract is an alternate win, so Abyssal Persecutor was rejected.

## Weakest points (please push here)
1. **Kindred Dominance is 7 mana** versus Blasphemous Act's usually 1–3. Is a one-sided wipe worth losing the cheap emergency reset?
2. **Rock cut:** with Heartless/Herald/Incubator/Cellarspawn/Horn the deck leans on creature-only reduction. Rite, Mana Drain and Cyclonic Rift do not benefit.
3. **Desecration Demon** can be tapped down every combat. Its value is the entry hit, not attacking.
4. **Belzenlok self-damage** stacks with Prince X, Vilis and Ancient Tomb.
5. **Pass C** (owner-equivalent, NOT technically independent) proposed no swap. Its Displacer Kitten over Warstorm Surge challenger
   was rejected there, and the rejection is kept here (Kitten is not a Demon; Surge doubles Lord).

## Tested pool (6 full 100s; `data/grixis/m6/ij/tested_pools/Be_lakor__the_Dark_Master_M7_tested_configurations_20261023.json`)
- BASELINE.
- PREFERRED_FIVE (selected).
- FIVE_ALT_HORN_OVER_HEARTLESS (REJECT: Heartless's −2 on everything beats −1 damage).
- SIX_COURTYARD (Secluded Courtyard over Exotic Orchard, RETAIN_ALTERNATIVE).
- SIX_XANDER (Lord Xander, the Collector over Lord of Change, RETAIN_ALTERNATIVE).
- SEVEN (staged, not selected: padding).

Other named rejections:
- Harvester of Souls, Bloodgift Demon and Ob Nixilis, Captive Kingpin (vs Kardur).
- Abyssal Persecutor (can't-win vs Contract) and Archfiend of the Dross (lose-the-game).
- Razaketh, Varragoth, Quicksilver Amulet, Jet Medallion, Rhystic Study (Game Changer), Displacer Kitten.

## Infra disclosure
- The gate, schema and gate-test files are byte-identical to PR #654 head cb670d59 (they originate in PR #651).
- `scripts/grixis_m6_bundle_check.py` is stabilized corpus-wide (SHA-256 `c5688abc…`). It adds fail-closed, enumerated legacy seal-alias
  mapping, per-deck preserved non-independence wordings, and registry-bound digest reconciliation.
  - 60 of 62 Pass C receipts now validate, with 0 regressions; tests are in `tests/test_m6_pass_c_corpus_stabilization.py`.
  - #30 Lord Xander and #31 Lynde stay rejected because their seal's stage_a.md SHA-256 does not match the committed bytes. This needs an owner decision.
- **Merge order:** #651 → #652 → #653 → #654 → this PR. After merge, the #653 Ashad and #654 Ashnod bundle checker pins must be refreshed to `c5688abc…`.
- Pass C is FORMAL_PASS_C_OWNER_EQUIVALENT under the owner waiver and is **not** technically independent.
- CI run URLs are recorded in the PR body, not in hashed files.
