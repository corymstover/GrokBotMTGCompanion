# Doctor Doom, King of Latveria — ChatGPT adversarial review packet (M7, 2026-10-23)

**Status:** REVIEW CANDIDATE — NOT APPROVED, NOT CANONICAL. REVIEW_READY_NOT_OWNER_APPROVED. Only Cory can approve.

**Reviewer instruction:** attack this list. Show any of the following:
- a rules error;
- an illegal card;
- an unpayable line;
- an unsupported combo claim;
- a candidate that clearly beats an incumbent.

No win rates were measured, and EDHREC prevalence is discovery evidence only.

## Provenance
**Canonical source (read-only).**
- Repository `corymstover/grixis-commander-encyclopediaGPT` main `9b26aa28fc7e16f6652aaec292b4edf84e20db71`.
- File `refinement/decklists/Doctor_Doom_King_of_Latveria_Approved_2026-10-14.txt`, git blob `324fdb3070be086b89a99a1cc3dcab33f92c08e6`.
- Canonical commit record: the bytes were fetched and verified at 9b26aa28. The registry's source commit field says `1836b97`, the import commit, which carries the same bytes.
- Raw SHA-256 `c97bd448aa4b18d2f7ed15e5d67006ab320ed67ad3ed267e44150de472e1dc58`. This equals `state/current_deck_overrides.json` `approved_list_sha256`, the tracker `final_list_hash` and the registry `recorded_sha256`.
- Vendored byte-exact at `data/grixis/m7/baseline_sources/Doctor_Doom__King_of_Latveria_approved_source_2026-10-14.txt`.

**Hashes.** The registry `recorded_sha256` equals the raw bytes, so **no provenance exception** is used.
- Logical hash `lh1:bdc7cc1f7dc0eeb6866bf80ada6790b5d21339bb63058b80321f352a874a3eca`.
- The registry export `exports/grixis-archidekt/doctor-doom-king-of-latveria.txt` (raw `3505f9a465a8ed61f9689d7a38c67b47d68b487001565b9ccc08de82a62f1574`) is the same 100 in export format ("1 " instead of "1x ", sorted), with the same logical hash.

**Discrepancies.** None in the hashes. The approved source file is not alphabetical; the candidate is written commander-first, then alphabetical.

**Count convention.** 100 = 1 commander + 99 library; no companion.
- 38 lands: Island, Mountain and Swamp one each, plus 35 nonbasic.
- 7 mana rocks in the baseline, 6 in the candidate.

**Candidate.** `data/grixis/m7/candidate_lists/Doctor_Doom__King_of_Latveria.txt`: commander first, then alphabetical; six substitutions.
- Raw `21d5ebd66352c34e9f7b786e71d121e9e0101f2426049741c2ddb1d95d1ab3fb`.
- Logical `lh1:6e779fc71f33bb82f2d4ed3a4813956c04454e0fab8370f662b97bfd5be1926d`.

**Live data.** Live Scryfall `/cards/collection` was queried on 2026-10-23 for the 100 baseline rows and 135 evaluated names.
- The live results are stored only in the candidate snapshot and the research files; the frozen cache was not written.
- Oracle text and oracle_id show zero differences against the frozen `oracle-cards-20261016090200` snapshot for all 231 names.

**Legality.** Every card is Commander-legal on live Scryfall and within UBR. Doctor Doom, King of Latveria is **officially** Commander-legal from its Marvel Super Heroes Commander (msc) release on 2026-06-26; the 2026-12-18 pmei promo is a later printing, not a legality date. The registry's `official_commander_compliance` is `compliant`. **No project exception is used**, and the paused Nov 13 legality-activation plan does not cover this card.

**Game Changers.** 6 in the baseline: Ancient Tomb, Cyclonic Rift, Demonic Tutor, Fierce Guardianship, Jeska's Will, Vampiric Tutor. 7 in the candidate (+Mox Diamond). **Power Bracket 4.**

**Archidekt tags.** Land Discard, Villains, Connive.

## Commander model (attack this first)
**Doctor Doom, King of Latveria** is a {1}{U}{B}{R} 3/3 legendary Human Noble Villain. Its Oracle text: "Whenever you discard one or more land cards, each opponent loses 2 life. At the beginning of combat on your turn, target Villain you control gains menace until end of turn. It connives."

Rules points:
- **603.2c.** "One or more land cards" triggers once per discard event. A wheel that discards three lands drains 2, not 6, so the deck counts separate events (Seismic Assault activations, cycling, connive, Mox Diamond, Lightning Axe).
- **701.50a.** Connive: draw, then discard. A discarded land drains 2 and gives no +1/+1 counter; a nonland gives the counter.
- **Self-targeting.** Doom is a Villain and can target himself. Swiftfoot Boots' hexproof does not stop that; Lightning Greaves' shroud (702.18a) would, which is why Greaves is rejected.
- **603.3b.** In the Dakmor loop, the discard triggers (Doom, Glint-Horn, Cool but Rude, Badgersaur, Monument) go on the stack before the cycling draw resolves.
- **702.52b.** Dredge 2 can replace a draw only if the library holds at least two cards. The loop is therefore library-bounded.
- **Mox Diamond** is a replacement: discarding a land "instead" is still a discard, so it triggers Doom.
- **Villainous Hideout** coloured mana pays only for Villain spells and Villain-source abilities, so it cannot pay Seismic Assault or Tectonic Reformation's granted cycling {R}.

## Swaps (6 — five floor swaps plus one post-floor)
| Add | Cut | Why |
|---|---|---|
| Lightning Axe | Feed the Swarm | {R} instant, 5 damage to a creature; discarding a land as the cost also drains 2. Feed the Swarm is sorcery-speed, costs life and does not discard. |
| Glint-Horn Buccaneer | Change of Fortune | Haste; 1 damage to each opponent per card discarded, on top of Doom's drain; loots on the attack. Ahead of Magmakin Artillerist in every bounded grid cell. Change of Fortune is a 4-mana refill whose hand discard is one event. |
| Red Ghost, Intangible Genius | Loki, the Deceiver | Doom's combat connive guarantees our second draw each turn, so Red Ghost makes a hasty 3/3 Ape Villain every turn (Prowler, Strucker and Doom Reigns Supreme trigger). Loki needs Villains connecting in combat. |
| Coastal Peak | Shipwreck Marsh | UR cycling land: the cycling discard is a land discard. Red land sources 20 → 21. |
| Swiftfoot Boots | Fellwar Stone | Hexproof that still lets Doom target himself. Fellwar is the most redundant of seven rocks. |
| Mox Diamond | Talisman of Creativity | Post-floor. 0-mana rock whose cost is a land discard (a free Doom trigger). Game Changer. |

**Net:**
- Lands 38 → 38; rocks 7 → 6.
- Creatures 22 → 23; instants/sorceries 22 → 21.
- Curve by MV 0/1/2/3/4/5/6/7+: 0/7/19/17/13/4/1/0 → 1/8/17/18/12/4/1/0. Average nonland MV 2.852 → 2.787.
- P(2–5 lands in 7) 0.817 → 0.817.

**Losses:**
- Feed the Swarm's enchantment answer.
- Change of Fortune's one-sided refill.
- Loki, the Deceiver.
- Shipwreck Marsh (one black land source).
- Fellwar Stone and Talisman of Creativity.

## Pass C requested tests (bounded; `tests/test_m6_doctor_doom_king_of_latveria_m7_mechanics.py::PassCBoundedMeasuredTests`)
**Dakmor sequence (Pass C item 1).**
- Doom alone, 40 life, 40-card library: 20 iterations, 40 drain, lethal. 38 cards give 20 iterations; 37 cards give 19 iterations and 38 drain, not lethal.
- With Buccaneer: 14 iterations, 42 drain; lethal from a 26-card library, not from 25. With Buccaneer and Cool but Rude level 2: 8 iterations.
- Monument adds at most three modes: 19 iterations, 41 drain.
- No external {R}: 0 iterations. Green Goblin, Nemesis's tapped Treasure: 3 iterations with 3 red.
- Graveyard hate at iteration 5: 5 iterations, 10 drain. Taking an optional exile on Dakmor: 1 iteration.

**Glint-Horn Buccaneer vs Green Goblin, Revenant (Pass C item 2): 20-cell grid.** The axes are five fixed turn patterns × attack possible or not × removal before attacks or not.
- Totals (damage / cards): Buccaneer 79/5, Revenant 8/19, Artillerist 64/0.
- Buccaneer beats Revenant on damage in 20/20 cells. Revenant beats it on cards in 4/20 and does nothing in 16/20 (it needs an attack; no haste). Revenant's best cell is the wheel: 2 damage, 8 cards.
- Buccaneer ≥ Artillerist in every cell.

**Resource dependence (Pass C item 3).** Exact lands-only hypergeometric:
- Doom by 10 / 11 cards: 0.5550 / 0.6477 → 0.5570 / 0.6498.
- RRR by 11 / 12 cards: 0.3895 / 0.4529 → 0.4248 / 0.4904.
- 10 graveyard-independent land-discard outlets vs 3 graveyard-dependent ones.

**Not done.** There was no matched-opening playtest sample, no opponent or removal-response model, and no multiplayer simulation. No simulator here models Doom's connive choices or multiplayer life totals.

## Combos (Commander Spellbook find-my-combos, both lists, JSON in research_challengers)
- Baseline: **1 included combo**. Candidate: **1 included combo**. Both are 779-2546-4467: Surly Badgersaur + Tectonic Reformation + Dakmor Salvage.
- Spellbook labels it "Infinite self-mill" and "Near-infinite self-discard triggers". With a finite library it is library-bounded (see the trace above). **No infinite is claimed.**
- Almost-included lines: 16 → 22. They need cards that are not in the list.

## Adversarial scenarios (please push here)
1. **Graveyard hate.** It ends the Dakmor loop and blanks Crucible and Oscorp's mayhem. Ten graveyard-independent outlets remain.
2. **Red-light draws.** Seismic Assault needs RRR and cycling needs {R}; Hideout pays neither. P(three red lands among the top 11) is 0.4248.
3. **Doom removed.** Buccaneer, Cool but Rude, Monument and Seismic Assault still deal damage from discards; Boots protects against targeted removal only.
4. **Short library.** The loop needs 38 cards (Doom alone) or 26 (with Buccaneer) to drain 40.
5. **Optional exile.** Construct, Moonstone and Converter say "may"; taking the exile on Dakmor ends the loop.
6. **Refill.** With Change of Fortune cut, Revenant, Demand Answers and Jeska's Will remain. The five-swap list keeping Talisman of Creativity is RETAIN_ALTERNATIVE.
7. **Owner-removed class.** The owner's 2026-10-14 approval removed opponent-discard punishers (Liliana's Caress, Geth's Grimoire, Waste Not) and Dark Deal. Kefka, Court Mage and Syphon Mind were evaluated and rejected as that class; Tinybones, Trinket Thief and Dark Deal are not re-added. Buccaneer punishes our own discards; please confirm the owner sees that as a different class.
8. **Pass C disposition.** Pass C was owner-equivalent; a genuinely independent third model was **not executed**. Its final disposition was **NEEDS TESTING**. Its exact pairing (+Buccaneer −Revenant) is staged as complete 100s, both inside the six and alone on the baseline, and rejected.

## Tested pool (10 configurations; `data/grixis/m6/ij/tested_pools/Doctor_Doom__King_of_Latveria_M7_tested_configurations_20261023.json`)
- BASELINE (raw 100) and CANONICAL_EXPORT (registry export, same logical hash).
- PREFERRED_SIX (selected).
- FIVE_KEEP_TALISMAN_OF_CREATIVITY: RETAIN_ALTERNATIVE.
- SIX_WITHERING_TORMENT_INSTEAD_OF_LIGHTNING_AXE: REJECT.
- SIX_ARTILLERIST_INSTEAD_OF_BUCCANEER: REJECT.
- SIX_PASS_C_EXACT_PAIRING_BUCCANEER_OVER_REVENANT: REJECT.
- ONE_PASS_C_EXACT_SINGLE_SWAP_ON_BASELINE: REJECT.
- SEVEN_PASS_C_LEDGER_SHREDDER_OVER_IRON_MONGER: REJECT.
- SEVEN_PASS_C_PUTRID_IMP_OVER_DEMAND_ANSWERS: REJECT.

Other named rejections: Bazaar of Baghdad, Faith of the Devoted, Lonely Sandbar, Living Laser, Madame Hydra, Terminate, Bedevil, Lightning Greaves, Ash Barrens, Kefka, Court Mage and Syphon Mind (owner-removed class).

## Distinctness (disclosed)
**Vs the Loki deck** (`exports/grixis-archidekt/loki-the-deceiver.txt`):
- The baseline shares **53** nonbasic names with it, and so does the candidate. Loki and Talisman of Creativity are cut, but Red Ghost and Swiftfoot Boots are also in the Loki deck. **This candidate does not reduce that overlap.**

**Vs Deck #12 Davros (PR #660 candidate):** 34 → 32 shared nonbasic names.

**Commander-first difference.** The Loki deck copies attacking Villains. Doom drains on separate land-discard events and connives a Villain every combat. The Doom-only core is Seismic Assault, Tectonic Reformation, Dakmor Salvage, Surly Badgersaur, Green Goblin, Nemesis, Monument to Endurance, Cool but Rude and Crucible of Worlds, plus Lightning Axe, Glint-Horn Buccaneer, Coastal Peak and Mox Diamond.

## Infra disclosure
**No shared-infrastructure change in this PR.**
- These files are byte-identical to PR #660 head bb3be7d3 (vendored from the #651–#660 stack; not modified here):
  - the gate;
  - the schema;
  - the gate test;
  - the Pass C corpus test;
  - `scripts/grixis_m6_bundle_check.py` (SHA-256 `2962a640…`).
- This deck's preserved Pass C receipt ("genuinely independent third model **not executed**") passes the checker's existing preserved-non-independence path.

**Process notes.**
- The focused CI workflow step names contain no `#` characters.
- **Merge order:** #651 → #652 → #653 → #654 → #655 → #656 → #657 → #658 → #659 → #660 → this PR.
- Pass C is FORMAL_PASS_C_OWNER_EQUIVALENT under the owner waiver and is **not** technically independent.
- CI run URLs are recorded in the PR body, not in hashed files.
