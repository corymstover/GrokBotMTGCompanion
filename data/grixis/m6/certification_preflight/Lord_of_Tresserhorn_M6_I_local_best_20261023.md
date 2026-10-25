# Lord_of_Tresserhorn (Lord of Tresserhorn) — M6 I local-best memo for the M7 review candidate (2026-10-23)

This memo is evidence only. The candidate is NOT owner approved and NOT M6 certified. Its readiness is `READY_FOR_EXACT_OWNER_APPROVAL_NOT_YET_APPROVED`: five genuine swaps, each judged on its own merits. The canonical list is unchanged.

Scope: the twelve complete configurations in `data/grixis/m6/ij/tested_pools/Lord_of_Tresserhorn_M7_tested_configurations_20261023.json`, plus the named single-card contenders. Each configuration is 100 cards (1 commander and a 99-card library). This is not a global or statistical optimum.

Identity:
- Tracker index 28 (Deck 29), deck ID `Lord_of_Tresserhorn`, commander Lord of Tresserhorn.
- The overrides (APPROVED / LOCKED, 2026-10-14) and the registry agree. Tracker row 28 still shows the stale "CURRENT FINAL BASELINE — preserve; new refinement cycle not yet reviewed" text with a blank final hash. That is disclosed, not changed; the overrides are the lock authority.

Baseline:
- Canonical encyclopedia main 9b26aa28fc7e16f6652aaec292b4edf84e20db71, file `refinement/decklists/Lord_of_Tresserhorn_Approved_2026-10-14.txt`.
- Git blob d9ff96da, introduced by canonical commit af3c889 (2026-10-14). Registry source_commit 1836b97 has the same bytes.
- Raw SHA-256 95863276f38beff6b0cf7609041006a6f1de94d5e62c73d76551d6793ffa5b8e. It equals the overrides `approved_list_sha256` and the registry recorded hash, so no provenance exception is used.
- Logical hash lh1:eae4578c….
- The registry Archidekt export `exports/grixis-archidekt/lord-of-tresserhorn.txt` (raw ce42932d…) is the same 100 in export format, with the same logical hash.

## Commander text (frozen cache, identical on live Scryfall)
Lord of Tresserhorn ({1}{U}{B}{R} Legendary Creature — Zombie 10/4):
- "When Lord of Tresserhorn enters, you lose 2 life, you sacrifice two creatures, and target opponent draws two cards."
- "{B}: Regenerate Lord of Tresserhorn."

There is **no opponent-regeneration clause**. The regeneration is Lord's own, it costs {B}, and it does not stop sacrifice (CR 701.19a, 701.21a). The selection rule follows from this text. A card earns a slot if it does one of these:
- turns off, counters or pays for the enters trigger;
- monetises the two forced sacrifices;
- protects the 10-power body that wins through commander damage, infect or Pain for All.

## Result
The candidate (raw fd09cb26…, lh1:c01c0d9c…) is the canonical 100 with five swaps:

| # | Add | Cut | Confidence |
|---|---|---|---|
| 1 | Fierce Guardianship | Stubborn Denial (owner-cycle ADD, flagged) | MODERATE |
| 2 | Consign to Memory | Feed the Swarm (audit KEEP, flagged) | MODERATE |
| 3 | Black Market Connections | Cover of Darkness (audit KEEP, flagged) | MODERATE |
| 4 | Ornithopter of Paradise | Fellwar Stone (audit KEEP, flagged) | MODERATE |
| 5 | Skullclamp | Sheoldred's Edict (audit KEEP, flagged) | MODERATE |

It is the local best of the tested pool on the deployment proxy:
- turn-6 P(Lord on battlefield) is 0.6121 for the baseline and 0.6613 for the candidate;
- turn-6 P(Lord out with free protection in hand) is 0.1208 → 0.1969.

The one tested configuration with a higher deployment number is alt B (+Skullclamp −Muddle the Mixture, keeping Sheoldred's Edict, 0.6672). It is staged, not selected:
- Muddle is an owner-cycle add, and its transmute finds Dress Down, Torpor Orb or Karn;
- the gap (0.6 points) is within the proxy's noise.

Five is a floor, not a target. Fifteen material candidates were judged, and ten incumbents were challenged as weakest slots: the five cuts plus Muddle the Mixture, Nightscape Familiar, Rogue's Passage, Pain for All and Terminate. Apart from the five adds, every candidate failed for one of these reasons:
- **Owner cut, inadmissible:** Temur Battle Rage. The owner cut it on 2026-10-14 (double strike on a 10-power Lord is 20 commander damage, not 21), and Pass C did not reopen it. The prior GrokBot draft swap +TBR −Pain for All is withdrawn and kept only as a disclosed rejected configuration.
- **Author-rejected and not reopened:** Embercleave, Psychotic Fury, Glistening Oil.
- **Pass C requested, tested, kept as an alternative:**
  - Soul's Fire. It is the best conversion card in the B2 grid (216/972 kills), but it needs Lord on the battlefield and answers only 4/14 B3 threats.
  - Distortion Strike over Rogue's Passage. This is the 34-land case; it scored 0.6490 against the candidate's 0.6613.
- **Not better:**
  - Aqueous Form. Cover of Darkness is already cut, and the six-swap package over Muddle scores 0.6637, which is noise, while losing the tutor.
  - Swan Song. It misses creature and artifact spells and gives an opponent a flier.
  - Grafted Exoskeleton. It duplicates the infect finishers.
- **Unmeasured, LOW confidence:** Orcish Bowmasters. It would be a fourth Game Changer, and Torpor Orb and Karn (Lord's suppression plan) also switch off its enters trigger. A Bowmasters already on the battlefield does punish Lord's forced draws. This is disclosed as an open question.

## Why each swap (commander-first)
1. **Fierce Guardianship −Stubborn Denial.**
   - FG is free once Lord is on the battlefield (CR 903.3d). Denial needs ferocious to be a hard counter.
   - B4 grid: FG answers 17/40 cells, Denial 9/40, FG only 8, Denial only 0.
   - While Lord is on the stack, FG costs {2}{U} and Denial is soft. Cavern of Souls naming Zombie remains the clean answer there.
   - Flags: Denial is an owner add. FG was author-rejected, but Pass C Stage A reopened it. It is a Game Changer (2 → 3).
2. **Consign to Memory −Feed the Swarm.**
   - A {U} instant that counters Lord's own trigger, which is a fourth on-stack answer alongside Stifle, Tale's End and Muddle-tutored pieces. It also counters opponents' triggers and colourless spells.
   - B6: Consign only 5/8, Feed only 2/8.
   - Loss: enchantment removal drops to Chaos Warp, plus Otawara bounce.
3. **Black Market Connections −Cover of Darkness.**
   - The changeling token is a Zombie: it is fodder for Lord, Gravecrawler's other Zombie, and a body for Diregraf Captain. BMC also gives a card or a Treasure for {B} regeneration.
   - This is the largest single-swap gain: 0.6121 → 0.6381.
   - Cover's fear is stopped by black and artifact blockers, and Shizo already gives Lord fear.
4. **Ornithopter of Paradise −Fellwar Stone.**
   - A mana source that is also a creature for the two-creature sacrifice, and a flying chump blocker.
   - Single swap 0.6121 → 0.6258. Turn-4 deployment is the best single-swap gain (0.2717 → 0.2879).
   - Cost: summoning sickness.
5. **Skullclamp −Sheoldred's Edict.**
   - Clamped fodder sacrificed to Lord's trigger draws two, offsetting the opponent's two cards. On a toughness-1 recursive creature it is {1}: draw two.
   - Mean Skullclamp draws by turn 6 is 0.26 in the candidate.
   - Loss: the instant edict. B3 shows 2/14 threat cells where it was the only spot answer; sweepers still cover them.

## Owner direction
- Stubborn Denial is an owner-cycle add. Feed the Swarm, Cover of Darkness, Fellwar Stone and Sheoldred's Edict were explicit KEEPs in the owner's 2026-10-14 whole-list audit. **All five cuts are flagged** for Cory's decision.
- The other owner adds are kept: Anger, Brotherhood Regalia, Chandra's Ignition, Deflecting Swat, Karn, Muddle, Mystic Remora, Nightscape Familiar, Not of This World, Pain for All, Phyresis, Slip Out the Back, Stifle, Tale's End, Torpor Orb, Uncaged Fury, Cavern of Souls and Shizo.
- No owner-removed card is re-added.
- The staged alternatives are complete 100s with exact deltas, so the owner can pick one directly:
  - alt A: four swaps, keeping the Edict;
  - alt B: Skullclamp over Muddle;
  - alt C: Skullclamp over Nightscape;
  - Soul's Fire;
  - FG over Nightscape;
  - Distortion Strike.

## Pass C requested tests (bounded finite versions; not win rates)
These are in `data/grixis/m7/research_challengers/Lord_of_Tresserhorn_bounded_measured_tests_20261023.json`, and recomputed or consistency-checked in `tests/test_m6_lord_of_tresserhorn_m7_mechanics.py`. The Pass C receipt is a NON-INDEPENDENT owner-equivalent review (ChatGPT/OpenAI GPT-6, with a technical-independence waiver).

1. **Seeded goldfish** (seed 29, 20,000 games per configuration, on the play, no mulligans), turn 6:

   | Configuration | P(Lord on bf) T4 | T6 | Free protection in hand T6 | Attack-ready with conversion card T6 |
   |---|---|---|---|---|
   | Baseline | 0.2717 | 0.6121 | 0.1208 | 0.2352 |
   | Candidate (5 swaps) | 0.3068 | 0.6613 | 0.1969 | 0.2683 |
   | alt A (4 swaps, keep Edict) | 0.3008 | 0.6563 | 0.1903 | 0.2651 |
   | alt B (Skullclamp −Muddle, keep Edict) | 0.3087 | 0.6672 | 0.2023 | 0.2691 |
   | alt C (Skullclamp −Nightscape) | 0.2897 | 0.6438 | 0.1946 | 0.2571 |
   | +FG −Nightscape (probe) | 0.2559 | 0.5856 | 0.1623 | 0.2222 |
   | +Soul's Fire −Edict (probe) | 0.2710 | 0.6107 | 0.1177 | 0.2631 |
   | Candidate +Distortion −Rogue's Passage | 0.3016 | 0.6490 | 0.1911 | 0.2666 |
   | Candidate +Aqueous −Muddle | 0.3099 | 0.6637 | 0.1956 | 0.2740 |
   | Prior draft (TBR −Pain, owner cut) | 0.2989 | 0.6538 | 0.1943 | 0.2646 |
   | Original tentative plan | 0.2440 | 0.5674 | 0.1651 | 0.2396 |

2. **Exhaustive rules grids** (B1–B6): evasion, conversion (972 cells), interaction, protection, the **Dress Down layer-6 truth table** (24 cells) and Consign vs Feed. The Dress Down result:
   - Phyresis attached before Dress Down is overridden.
   - Phyresis attached after it, or Tainted Strike resolving after it, grants infect.
   - Kediss's trigger is off while Dress Down is on the battlefield.
   - Lord's {B} regeneration is off that turn.
3. **Matched-hand games against opponents.** Not run: the repo has no validated game engine for this deck and no opponent model.

Commander Spellbook: 19 included combos in the baseline, the candidate and every alternative. None are new and none are lost. Almost-included goes 283 → 289.

## Limits
Only finite scripted rules cases and seeded proxies are tested. The deployment model has no opponents, no blockers and no removal.
- Game Changers 2 → 3, Bracket 4 unchanged.
- Lands 35 → 35.
- Average nonland MV 2.44 → 2.45 (library only).
