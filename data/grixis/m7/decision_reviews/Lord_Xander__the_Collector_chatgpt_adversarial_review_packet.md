# Lord_Xander__the_Collector (Lord Xander, the Collector) — ChatGPT adversarial review packet (M7, 2026-10-23)

**Status:** RESEARCH ONLY and BLOCKED — NOT APPROVED, NOT CANONICAL, NOT OWNER-PRESENTABLE. Readiness `RESEARCH_ONLY_WITHDRAWN_NOT_OWNER_PRESENTABLE`.
- Blocker 1 (seal): the existing M6 Pass C Stage A seal does not match the committed Stage A file, so the shared J checker rejects any bundle for this deck. Details below. The sealed evidence and the checker are not edited.
- Blocker 2 (floor): three genuine swaps were found, below the five-swap floor; nothing was padded.
- One swap overrides an EXPLICIT owner keep (Persist) and is FLAGGED. Two complete owner-keeping alternatives are staged.
- Only Cory can approve.

**Reviewer instruction:** attack this conclusion. Show any of the following:
- a rules error;
- an illegal card;
- an unpayable line;
- an unsupported combo claim;
- a reason any swap is not a genuine improvement, or a genuine swap we missed;
- an owner-direction contradiction we missed.

No win rates were measured. EDHREC prevalence is discovery evidence only, and it is against Necromancy and Malakir Rebirth.

## Seal blocker (exact cause)
- File: `data/grixis/m6/owner_pass_c_substitute/Lord_Xander__the_Collector/seal.json`, added by commit `bca97b98980869974388134e0b133d75e5782a55` (2026-10-21 10:05:13 -05:00).
- It records `stage_a.md` SHA-256 `89a78d803b5cb5ea886b2402828aaff00b78497db0b3c0fe569c6c0ee5a879d1` and git blob `e97d35fe9666519ed8ff0fc5e605d3ff2b5a5e07`.
- The committed `stage_a.md` (Stage A commit `6ebb511e4b1bc4d6d0b9f0103cf1f95519f7eaae`, 2026-10-21 10:04:46 -05:00) is that same blob `e97d35fe`, but its SHA-256 is `826f07707a6fdd1583b815ba6b80ad99bd8a71d57d03ac05766ed2a0a4cd0322` (13590 bytes). The file has not changed since; only the recorded SHA-256 is wrong. No line-ending or trailing-newline variant reproduces `89a78d80…`.
- `stage_a.json` matches its seal (`aff5f64c…`, blob `c0d52650`).
- `final_disposition.md` repeats the wrong MD hash. The same values were carried forward and merged through #434/#435.
- Effect: `scripts/grixis_m6_bundle_check.py` (sha `2962a640…3bf3b`, unchanged) raises "Stage A source diverged from separately sealed byte commitment" in `validate_pass_c`. The revision bundle in this PR is written in full and is otherwise complete, and `tests/test_m6_lord_xander_the_collector_m7_ij.py` asserts that exact rejection. The checker's `--check` scans only `data/grixis/m6/bundles`, and the corpus test already expects decks 30 and 31 to be rejected.
- Fix (owner decision, NOT done here): re-seal Stage A under a new, disclosed seal record, or record a documented hash-correction exception. Either way, the owner has to authorise touching sealed M6 evidence.

## Provenance
**Canonical source (read-only).**
- Repository `corymstover/grixis-commander-encyclopediaGPT` main `9b26aa28fc7e16f6652aaec292b4edf84e20db71`.
- File `refinement/decklists/Lord_Xander_the_Collector_Approved_2026-10-14.txt`, git blob `025aa284`, introduced by canonical commit `214fd50` (2026-10-14).
- Canonical commit record: 9b26aa28fc7e16f6652aaec292b4edf84e20db71 (blob 025aa284, introduced by 214fd50 2026-10-14; registry source_commit 1836b97 same bytes).
- Raw SHA-256 `92cdc2f9c1a3583ccf6a311679db66bef825dac2902761859e929f268b6b4787`. This equals the overrides `approved_list_sha256`, the registry recorded hash and the decisions-file "approval candidate" SHA.
- Vendored byte-exact at `data/grixis/m7/baseline_sources/Lord_Xander__the_Collector_approved_source_2026-10-14.txt`.

**Hashes.** No provenance exception is used. Logical hash `lh1:84233c9153b8b1c86c521ce4734dab8515e49f448776f66e6c2a450772db773a`. The registry Archidekt export `exports/grixis-archidekt/lord-xander-the-collector.txt` (raw `26b1674f…`) has the same logical hash.

**Identity and discrepancies (recorded, not changed).**
- Tracker Deck 30 (index 29) uses the short key `Lord_Xander`. The overrides and registry use deck ID `Lord_Xander__the_Collector` (registry slug `lord-xander-the-collector`), APPROVED / LOCKED 2026-10-14.
- Tracker row 29 sub-fields are still PENDING. The overrides are the lock authority. Neither file is changed.

## Commander model (attack this first)
Lord Xander, the Collector ({4}{U}{B}{R}, Legendary Creature — Vampire Demon Noble 6/6; `snc`, released 2022-04-29; Commander-legal; not a Game Changer):
- "When Lord Xander enters, target opponent discards half the cards in their hand, rounded down."
- "Whenever Lord Xander attacks, defending player mills half their library, rounded down."
- "When Lord Xander dies, target opponent sacrifices half the nonland permanents they control of their choice, rounded down."

How the deck uses this:
- Xander is reanimated or copied (owner plan, 2026-10-14). Copies that enter tapped and attacking (Blade of Selves, Auton Soldier myriad) were never declared as attackers, so they do not get the attack trigger. Their enters triggers do fire.
- A legend-rule death of a legendary copy is a "dies" event (CR 700.4). Exile at end of combat is not.
- Persist targets only NONLEGENDARY creature cards, so it can never return Xander himself.
- Lightning Greaves' shroud (CR 702.18a) stops the deck's own targeting of Xander. That covers equip (CR 702.6a: Sword of Feast and Famine, Blade of Selves, Helm of the Host), Saw in Half, Molten Duplication, Feign Death, Hall of Echoes and Malakir Rebirth (Greaves ruling 2020-08-07). Swiftfoot Boots' hexproof (CR 702.11b) stops only opponents.
- The frozen rulings have none for Lord Xander, Persist or Bojuka Bog. The analysis cites the rulings for Necromancy (2022-12-08, 2005-08-01), Malakir Rebirth (2020-09-25), Goryo's Vengeance (2018-12-07), Lightning Greaves (2020-08-07), Seize the Day and Auton Soldier (2023-10-13).

## Swaps (3 — below the five-swap floor; RESEARCH_ONLY)
**1. +Necromancy −Persist (MODERATE; FLAGGED owner-keep override).**
- The owner kept Persist "to retain the reanimation axis that makes a seven-mana commander realistic", but Persist cannot target legendary Xander. Necromancy can, and it reaches any graveyard.
- Instant-speed line: cast at an opponent's end step. Xander enters (discard). Necromancy is sacrificed at the cleanup step and Xander with it (dies: half nonland permanents). It does not grant haste.
- Grid B1 (36 cells): Necromancy returns Xander in 12, Persist 4 (nonlegendary targets only); 10 Necromancy-only, 2 Persist-only.
- Costs: {2}{B} against {1}{B}; enchantment-removal exposure; EDHREC upgraded 14/256 only.
- Pass C named this its best defined upgrade test. Pass C also disclosed that the Necromancy/Persist pair was known to the reviewer beforehand (not independently generated).
- **Owner-keeping alternatives (complete 100s, every owner keep and add kept):** alt A, Necromancy over Karlach, Fury of Avernus; alt B, Necromancy over An Offer You Can't Refuse.

**2. +Swiftfoot Boots −Lightning Greaves (MODERATE).**
- Not an owner card. Grid B2 (44 cells): Boots allows the own-target action in 44 cells, Greaves in 30. In 14 cells Greaves must first be moved off Xander, which strips his protection.
- Cost: equip {1} instead of {0}. Haste the turn Xander is cast in 22/44 cells against 44/44. Goldfish P(Xander attack trigger) turn 7 0.2978 → 0.2897, all of it from this swap.

**3. +Malakir Rebirth // Malakir Mire −Bojuka Bog (LOW_WITH_DISCLOSED_LIMITS; weakest).**
- Not an owner card. Both are tapped {B} lands. Malakir's front face turns a Xander death into a dies trigger plus an enters trigger.
- Grid B3 (16 cells): a tie, 6 answers each (4 Malakir-only, 4 Bog-only). The deck loses its only maindeck graveyard exile.
- The owner may reasonably prefer Bog. The swap is counted because the land slot gains commander synergy, and the cost is disclosed.

**Pass C requested comparisons:**
- +Goryo's Vengeance −Persist: staged, not counted. It is a haste burst, but exiled at end step (no dies trigger) and legendary-only; it returns Xander in 8/36 cells against Necromancy's 12.
- +Seize the Day −Karlach, Fury of Avernus: rejected. Karlach already adds a combat every turn it attacks.

**Staged, not counted:** Kiki-Jiki, Mirror Breaker over Karlach. It is a strong Xander multiplier but adds three commander-independent infinites (Spellbook 11 → 14).

**Rejected:**
- Glasspool Mimic // Glasspool Shore over Training Center (owner-rejected redundant-clone class).
- Chrome Mox over Talisman of Creativity (noise-level gain, Game Changer).
- Command Beacon over Xander's Lounge (marginal).
- Dualcaster Mage (generic infinite).
- Mirror-Mad Phantasm, Dauthi Voidwalker (anti-synergy), Counterspell, Mental Misstep, Waste Not, Twinflame, Splinter Twin.
- Supernatural Stamina, Undying Evil, Fake Your Own Death and Victimize: dominated.
- Mox Diamond.
- The Master of Lake-town and Phyrexian Metamorph: owner-rejected by name, not re-added.

**Invalid:** Sorin of House Markov // Sorin, Ravenous Neonate (W in colour identity).

## Pass C requested tests (bounded; `tests/test_m6_lord_xander_the_collector_m7_mechanics.py`)
**Seeded goldfish** (seed 30, N=20000 per configuration, 13 configurations). P(Xander cast) / P(attack trigger) by turn 7:
- Baseline 0.3779 / 0.2978.
- Candidate 0.3779 / 0.2897.
- Chrome Mox 0.3808 / 0.2920.
- Command Beacon 0.3786 / 0.2902.
- Glasspool 0.3749 / 0.2871.
- Goryo's on the baseline equals the baseline. Recursion is not modelled in the goldfish; it is measured in grid B1.

**Exhaustive rules grids:** B1 (36 cells), B2 (44) and B3 (16), as above.

## Combos (Commander Spellbook find-my-combos, every list, JSON in research_challengers)
- Included combos: 11 in the baseline, the candidate and every alternative except Kiki-Jiki (14).
- Almost-included: 132 → 131.
- Game Changers 20 → 20. Bracket 4 (Optimized).

## Adversarial scenarios (please push here)
1. Is Persist's value on nonlegendary copies (Auton Soldier, Spark Double, Opposition Agent) enough to keep it as the owner did? Alt A or B keeps it.
2. Is the end-step Necromancy line (enters, then dies at cleanup) realistic against open mana and graveyard hate?
3. Does losing Greaves' free re-equip and same-turn haste outweigh unblocking the deck's own targeting?
4. Is Bojuka Bog's graveyard hate worth more than Malakir Rebirth's dies-return in your pods?
5. Should Kiki-Jiki be accepted despite the added generic infinites?

## Tested pool (11 configurations; `data/grixis/m6/ij/tested_pools/Lord_Xander__the_Collector_M7_tested_configurations_20261023.json`)
1. BASELINE
2. CANONICAL_EXPORT
3. RESEARCH_THREE_SWAP
4. ALT_A_OWNER_KEEPS_NECROMANCY_OVER_KARLACH
5. ALT_B_OWNER_KEEPS_NECROMANCY_OVER_AN_OFFER
6. PASS_C_GORYOS_VENGEANCE_OVER_PERSIST
7. PASS_C_SEIZE_THE_DAY_OVER_KARLACH
8. STAGED_KIKI_JIKI_OVER_KARLACH
9. REJECT_GLASSPOOL_MIMIC_OVER_TRAINING_CENTER
10. REJECT_CHROME_MOX_OVER_TALISMAN
11. REJECT_COMMAND_BEACON_OVER_XANDERS_LOUNGE

## Distinctness (disclosed)
Nonbasic names shared, candidate/baseline (registry Archidekt exports):
- Cormela, Glamour Thief 52/52
- Kess, Dissident Mage 52/52
- Kefka, Court Mage 51/51
- Mai and Zuko 49/51
- Gwendlyn Di Corci 48/50

The overlap is the Grixis staple core. Necromancy appears in 4 other exports, Swiftfoot Boots in 14 and Malakir Rebirth in none.

## Infra disclosure
- No new shared-infrastructure edits. The gate, schema, checker and shared tests on this branch are byte-identical to PR #677 head e117a5ca (carried from the #651 chain). There are no registry, tracker or overrides edits, and the sealed M6 evidence is untouched.
- New files are deck-scoped artifacts, three deck tests and the workflow `.github/workflows/m7-lord-xander-the-collector.yml`.
- Merge order: #651 → … → #676 → #677 → this PR (#678).
