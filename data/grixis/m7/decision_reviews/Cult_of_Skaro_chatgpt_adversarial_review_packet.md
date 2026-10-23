# Cult of Skaro — ChatGPT adversarial review packet (M7, 2026-10-23)

**Status:** REVIEW CANDIDATE — NOT APPROVED, NOT CANONICAL. REVIEW_READY_NOT_OWNER_APPROVED. Only Cory can approve.

**Reviewer instruction:** attack this list. Show any rules error, illegal card, unpayable line, unsupported combo claim, or a
candidate that clearly beats an incumbent. No win rates were measured, and EDHREC prevalence is discovery evidence only.

## Provenance
- **Canonical source (read-only):** `corymstover/grixis-commander-encyclopediaGPT` main
  `9b26aa28fc7e16f6652aaec292b4edf84e20db71`, `refinement/decklists/Cult_of_Skaro_Approval_Candidate_2026-10-14.txt`
  (git blob `bcb22f01`; registry import commit 1836b97; the file name says "candidate", but it is the approved list).
  - Raw SHA-256: `4c221e5be0439338823ef621cd91706da8d405129cf6f5a41de36a83b875ef3b` = `state/current_deck_overrides.json`
    `approved_list_sha256` = registry `recorded_sha256`.
  - Vendored byte-exact at `data/grixis/m7/baseline_sources/Cult_of_Skaro_approved_source_2026-10-14.txt`.
- **Hashes:** registry `recorded_sha256` equals the raw bytes, so **no provenance exception** is used.
  - Logical `lh1:b5f92812…2aac`. The registry export `exports/grixis-archidekt/cult-of-skaro.txt` (raw `e17919e4…`) is the same 100
    without the `[Commander]` marker (same logical hash).
- **Tracker note discrepancy (documented, not repaired):** the tracker CSV note cites "Revised clean-list SHA-256 cc2f7a54…" and
  "Only change: Skorpekh Lord -> Ashad". cc2f7a54 is the 2026-10-13 file; the approved 2026-10-14 list differs from it by 11 more swaps.
  The same CSV row's final hash and the overrides record `4c221e5b`, which is authoritative.
- **Count convention:** 100 = 1 commander + 99 library; no companion. 34 lands (Island x3, Mountain x3, Swamp x3 + 25 nonbasic), 9 mana rocks.
- **Candidate:** `data/grixis/m7/candidate_lists/Cult_of_Skaro.txt` (commander first, then alphabetical; six substitutions).
  - Raw: `8b765d85649db64607c508bb3535466673593768ce729a9087a0260dc512624d`.
  - Logical: `lh1:59daa556db94bb2a0ba3226415e82871cd9e98fb3bb3888049ed0eda31b3b7f7`.
- **Live data:** live Scryfall (2026-10-23, /cards/collection; 94 baseline rows + 116 candidate names) is only in the candidate
  snapshot and research files. The frozen cache was not written. Oracle text and oracle_id show zero differences against the frozen
  `oracle-cards-20261016090200` snapshot.
- **Legality:** every card is Commander-legal on live Scryfall and within UBR. No project exception is used.
  Grand Abolisher (white) was evaluated and excluded.
- **Game Changers (3, unchanged):** Cyclonic Rift, Fierce Guardianship, Mana Vault → **Power Bracket 4** (registry ceiling 4, floor 3).
- **Archidekt tags:** Artifacts, Extra Combats, Copies (the three themes Pass C names).

## Commander model (attack this first)
- **Cult of Skaro** ({1}{U}{B}{R} 4/4 legendary artifact Dalek, no haste): "Whenever Cult of Skaro attacks, choose one at random" —
  Thay (+1/+1 counter on each artifact creature you control), Caan (draw two), Sec (3/3 black Dalek artifact token with menace),
  Jast (each opponent loses 4). One trigger = 1/2 card, 1/4 Dalek, 1 life per opponent in expectation. Connection is not needed.
- **603.3c / 707.10:** the mode is chosen as the trigger goes on the stack. Strionic Resonator / Scientist Supreme copies keep it;
  Roaming Throne (Dalek) gives a separate trigger with its own roll.
- **508.3a / 508.4:** tokens that enter tapped and attacking (myriad, Shaun's Synth) were never declared, so they do not trigger Cult that combat.
- **Karlach, Fury of Avernus:** "whenever you attack, if it's the first combat phase, untap all attacking creatures ... additional
  combat phase". Cult and every legal Cult copy are declared again, so the trigger count doubles (1 → 2 per turn).
- **Shaun + Karlach (603.3b):** put Shaun's trigger above Karlach's. The Synth copy enters tapped and attacking, Karlach untaps it,
  and it can be declared in the extra combat **only with haste** (302.6; Hammer of Purphoros or The Dalek Emperor): 3 triggers that turn,
  otherwise 2. On later turns the Synth is a normal non-legendary Cult copy until Shaun leaves (then all Synths are exiled).
- **Sword of Feast and Famine + Aggravated Assault (Spellbook 900-3750):** unchanged from the baseline; conditional on connecting each
  combat and on {3}{R}{R} from untapped lands. Disclosed as conditional, not as a deterministic win.

## Swaps (6 — five floor swaps plus one post-floor)
| Add | Cut | Why |
|---|---|---|
| Karlach, Fury of Avernus | Cybermen Squadron | An extra combat every turn: a second trigger for Cult and every copy. Squadron's myriad copies enter attacking and never trigger Cult; 7 mana for damage only. |
| Kindred Discovery | Canoptek Spyder | Pre-damage draw on every Dalek entry and attack. Off-ranking (Pass C's own hypothesis). Beats Spyder on 4 of 5 bounded boards; Spyder ignores tokens. |
| Hammer of Purphoros | Adaptive Omnitool | Global haste: Cult from the command zone, every clone and Shaun's Synth attack at once. Off-ranking. Omnitool is an equip-3 dig. |
| Shaun, Father of Synths | The Master, Multiplied | A persistent non-legendary Cult copy each attack. The Master mainly preserved myriad tokens that do not trigger Cult. |
| Quantum Misalignment | Anrakyr the Traveller | Two non-legendary Cult copies over two turns (rebound). Anrakyr's free cast costs life and rarely has a good target. |
| Skorpekh Lord | Etherium Sculptor | Post-floor: other artifact creatures get +1/+0 and menace for Thief, Spy Network, Sword and Jast finishes. Sculptor is the third reducer. |

**Net:** lands 34 → 34; rocks 9 → 9; artifact reducers 3 → 2; creatures 30 → 28; instants/sorceries 16 → 17; enchantments 5 → 7.
Curve by MV 0/1/2/3/4/5/6/7+: 1/4/21/11/14/4/7/3 → 1/4/19/13/14/6/6/2. Average nonland MV 3.354 → 3.338.
Heuristic R/B/U land sources 18/17/17 unchanged. P(2–5 lands in 7) 0.758 → 0.758.
**Losses:** the myriad package (Squadron + The Master, including token preservation), Spyder's draws, Omnitool's dig, Anrakyr's free casts,
one reducer.

## Pass C requested tests (bounded; `tests/test_m6_cult_of_skaro_m7_mechanics.py::PassCBoundedMeasuredTests`)
- Kindred vs Research Thief vs Thopter Spy Network vs Spyder over 5 fixed boards × 5 hit rates (0, 1/4, 1/2, 3/4, 1). Kindred draws 5/4 (Cult
  alone), 29/4 (Genesis chapter III turn), 13/4 (mixed board). Kindred ≥ Thief at hit rate ≤ 1/2 on the 4 Dalek boards; Thief wins on the
  post-wipe non-Dalek board and on fully connecting wide boards. Decision: keep Thief and Spy Network, cut Spyder.
- Karlach: 1 → 2 triggers per turn (3 with Shaun and haste for the Synth). Hexplate Wallbreaker: 9 mana before its first extra combat. Rejected.
- Not done: no shared opponent/mana sample, no removal-response rates, no matched simulation (no simulator here models Cult's random
  modes, copies or extra combats). Kindred overdraw is disclosed, not modeled.

## Combos (Commander Spellbook find-my-combos, both lists, JSON in research_challengers)
- Baseline: 1 included combo, **900-3750** (Sword of Feast and Famine + Aggravated Assault). Candidate: the same single combo. No new combo.

## Weakest points (please push here)
1. **Shaun is non-artifact and fragile:** if it dies, all Synths are exiled. It copies only legendary attackers.
2. **Kindred Discovery** is UU and mandatory; a big token turn can overdraw. It is dead on a non-Dalek rebuild.
3. **The myriad package is gone:** Pass C did not ask for this cut; it is our own judgment (myriad does not trigger Cult). Four-swap keeping it is staged.
4. **Skorpekh Lord** was cut by an earlier owner revision for Ashad. Here it returns over Etherium Sculptor and Ashad stays; needs owner review.
   The five-swap keeping Sculptor is RETAIN_ALTERNATIVE.
5. **Pass C** (owner-equivalent, NOT technically independent) final disposition was **NEEDS TESTING**, leading with Kindred over Research Thief
   and Karlach over Biotransference. This candidate takes both cards but different cuts. Both exact Pass C pairings are staged and rejected,
   so they need owner review.

## Tested pool (8 configurations; `data/grixis/m6/ij/tested_pools/Cult_of_Skaro_M7_tested_configurations_20261023.json`)
- BASELINE (raw 100) and CANONICAL_EXPORT (registry export, same logical hash).
- PREFERRED_SIX (selected).
- FIVE_KEEP_ETHERIUM_SCULPTOR (RETAIN_ALTERNATIVE).
- FOUR_KEEP_MYRIAD_PACKAGE (REJECT: myriad never triggers Cult).
- SIX_PASS_C_KINDRED_OVER_RESEARCH_THIEF (REJECT: bounded draw test).
- SIX_PASS_C_KARLACH_OVER_BIOTRANSFERENCE (REJECT: Biotransference makes Necrons and turns Shaun, Karlach and the clones into artifacts).
- SEVEN_CELEBRANT_OVER_THOUGHT_MONITOR (REJECT: redundant exerting extra combat).

Other named rejections: Hexplate Wallbreaker, Mechanized Production, Rising of the Day, Reckless Fireweaver, Cryptothrall, Mirror Box,
World at War, Foundry Inspector, Weeping Angel.

## Distinctness
Cult is the roster's random-attack-trigger Dalek deck. Every add multiplies the commander's own attack trigger (extra combat, persistent
and rebound copies, haste) or turns Dalek attacks into cards. Generic artifact staples were rejected. It stays apart from Davros (Dalek
villainous choices), Brudiclad (token conversion) and the Grixis artifact-combo decks.

## Infra disclosure
- No shared-infrastructure change in this PR. The gate, schema, gate test, Pass C corpus test and `scripts/grixis_m6_bundle_check.py`
  (SHA-256 `2962a640…`) are byte-identical to PR #658 head 7953eef5 (vendored from the #651–#658 stack; not modified here). This deck's
  preserved Pass C receipt ("Technically independent: false.") passes the checker's existing strict explicit-FALSE disclosure path.
- The focused CI workflow step names contain no `#` characters.
- **Merge order:** #651 → #652 → #653 → #654 → #655 → #656 → #657 → #658 → this PR.
- Pass C is FORMAL_PASS_C_OWNER_EQUIVALENT under the owner waiver and is **not** technically independent.
- CI run URLs are recorded in the PR body, not in hashed files.
