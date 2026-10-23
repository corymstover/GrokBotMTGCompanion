# Grixistax___October_2026 (Kraum, Ludevic's Opus + Tevesh Szat, Doom of Fools) — M6 I local-best memo for the M7 research candidate (2026-10-23)

This memo is evidence only. The candidate is NOT owner approved, NOT M6 certified and NOT owner-presentable. It is RESEARCH_ONLY: two genuine swaps, below the five-swap floor. The canonical list is unchanged.

Scope: the twelve complete configurations in `data/grixis/m6/ij/tested_pools/Grixistax___October_2026_M7_tested_configurations_20261023.json`, plus named single-card contenders. Each configuration is 100 cards (2 Partner commanders + 98 library). This is not a global or statistical optimum.

Naming: the tracker deck ID `Grixistax___October_2026` is a deck name, not a commander name. The decklist's two `[Commander]` lines and the registry name the Partner pair Kraum, Ludevic's Opus and Tevesh Szat, Doom of Fools. The tracker writes the pair with " // ", which is only a pair separator, not a double-faced card.

Baseline:
- Source: canonical encyclopedia main 9b26aa28fc7e16f6652aaec292b4edf84e20db71, file `refinement/decklists/Grixistax_October_2026_Approved_2026-10-14.txt`.
- Blob 86b8d18a, introduced by canonical commit cc7a938, the owner's 2026-10-14 approved build (12 swaps that cycle). Registry source_commit 1836b97 has the same bytes.
- Raw SHA-256 f36346d4… equals the overrides approved_list_sha256 and the registry recorded_sha256, so no provenance exception is used. Logical hash lh1:f56e9d1d….
- Disclosed, not changed: the tracker row still shows PENDING blueprint fields while overrides record the deck APPROVED/LOCKED; the registry Archidekt export `exports/grixis-archidekt/grixistax-october-2026.txt` (raw f0a28f93…) is the same 100 in export format, with the same logical hash, so it is current, not stale.

## Result
The research candidate (raw a04f16ba…, lh1:81656e61…) is the canonical 100 with **+Arcane Signet −Mox Amber** and **+Bitterblossom −Windfall**. It is the local best of the tested pool.

**Two genuine improvements were found, so the deck is RESEARCH_ONLY.** Five is a floor, not a target. Twenty candidates were judged and seventeen incumbents were challenged. Apart from Arcane Signet and Bitterblossom, every candidate failed for one of these reasons:
- **Dominated for the same slot:** Talisman of Indulgence (the Pass C challenger: same raw mana as Arcane Signet but no blue, so under our own Contamination P(U) on turn 4 is 0.272 against Signet's 0.330), Fellwar Stone (opponent-dependent colours), Spell Pierce and Dispel (cost mana against the free Mental Misstep, partner cEDH 71/81).
- **Self-defeating under our own locks:** Strip Mine and Urza's Saga (both become Mountains under our Blood Moon / Magus of the Moon), Null Rod (shuts off our 22 artifacts' mana and Helm of Obedience), Stasis (self-locking under our colour locks).
- **Slower or not clearly better than an owner addition or incumbent:** Frozen Aether over Static Orb (four mana, does not stop instant-speed combo), City of Traitors over Arid Mesa (owner addition), Praetor's Grasp over Windfall (not better than the stax-synergy add), Snuff Out over Deadly Rollick, Undercity Sewers over Gemstone Caverns (enters tapped).
- **Owner-rejected on 2026-10-14, inadmissible:** Braids, Cabal Minion (the Smokestack class), Sphere of Resistance (broad symmetric taxes), Valley Floodcaller (turbo creep).
- **Invalid:** Archon of Emeria (W) is outside U/B/R.
- **Staged alternative, not counted (RETAIN_ALTERNATIVE):** Opposition over Static Orb or Magus of the Moon. Tokens can pay Opposition's tap even when summoning-sick (not a {T} cost), but it needs {U}{U} under our own Contamination and Moon effects: P(seen and castable by turn 4) 0.0329, and 0.0034 under Contamination, against Static Orb's 0.0599 and 0.0584. Static Orb also caps our own untaps, so the two clash. This is an owner decision only.

Challenged incumbents: Mox Amber (cut), Windfall (cut), Static Orb, Magus of the Moon, Cyclonic Rift, Cursed Totem, Torpor Orb, Red Elemental Blast, Mental Misstep, Gemstone Caverns, Chain of Vapor, Jeska's Will, Gamble, Wishclaw Talisman, Overburden, Karn, the Great Creator and Tangle Wire. All except Mox Amber and Windfall were kept.

## Why (commander-first)
- Kraum, Ludevic's Opus ({3}{U}{R} 4/4 flying, haste): "Whenever an opponent casts their second spell each turn, draw a card."
- Tevesh Szat, Doom of Fools ({4}{B} planeswalker that can be your commander): "+2: Create two 0/1 black Thrull creature tokens. +1: You may sacrifice another creature or planeswalker. If you do, draw two cards, then draw another card if the sacrificed permanent was a commander."

The owner's plan is stax first: Winter Orb, Static Orb, Tangle Wire, Contamination, Blood Moon, Back to Basics, Trinisphere, Damping Sphere and Chalice of the Void. Tevesh's Thrulls pay Contamination's upkeep and Tangle Wire, and feed Phyrexian Tower, Skullclamp, Culling the Weak and Diabolic Intent. The wins are Helm of Obedience + Leyline of the Void / Dauthi Voidwalker and Underworld Breach + Lion's Eye Diamond / Lotus Petal + Brain Freeze.

**Swap 1: +Arcane Signet −Mox Amber (MODERATE confidence; the Pass C requested test).**
- Under our own Contamination every land taps for {B} only. Arcane Signet still makes U, B or R for the combined Partner identity (ruling 2020-11-10), so it pays Kraum and blue interaction inside our own lock.
- Mox Amber needs a coloured legendary creature or planeswalker. Karn, the Great Creator is colourless, so a Karn-only board makes no mana (Mox Amber ruling 2018-04-27); the commanders cost five mana each. Measured P(Amber live, given deployed) turns 1–4: 0.051/0.086/0.173/0.274.
- Bounded measured gains, turn 4 with no lock: mean mana 3.138 → 3.193; P(five mana including B for Tevesh) 0.1526 → 0.1657. Under Contamination: P(U) 0.279 → 0.330; P(UU) 0.038 → 0.053.
- Adoption: EDHREC Kraum + Tevesh cEDH 79/81 for Arcane Signet against Mox Amber's 18/81.
- Cost: the rare turn-1 Ragavan + Amber line and a free artifact for Mox Opal / Mox Diamond-style counts are lost.

**Swap 2: +Bitterblossom −Windfall (MODERATE confidence).**
- Bitterblossom makes a 1/1 flying Faerie each upkeep without Tevesh. Ordering its trigger before Contamination's (CR 603.3b) lets the new Faerie pay Contamination. The Faeries also feed Tevesh's +1, Skullclamp (a 1/1 becomes 2/0 and dies, drawing two), Phyrexian Tower, Culling the Weak and Tangle Wire.
- Measured P(token engine online by turn 4), Tevesh or Bitterblossom against the baseline's Tevesh only: 0.153 → 0.231. Under Contamination 0.119 → 0.202; under artifact hate 0.036 → 0.107.
- Windfall refills every opponent in a stax deck unless Narset or Notion Thief is out, and it is in none of the deck's six Commander Spellbook combos; Wheel of Fortune keeps the Breach wheel line (1368-1878-2706, 1368-2706-3518).
- **Data caveat:** Windfall is in 53/81 Kraum + Tevesh cEDH lists. Bitterblossom is on 40/122 lists on the solo Tevesh page, but on only 2/19 on a smaller EDHREC partner page and is not among the 81-list cEDH page's listed cards. The case rests on this deck's sacrifice outlets and the measured engine gain, not on adoption.
- Cost: 1 life every upkeep, alongside Necropotence. The blue Force pitch count drops 22 → 21.
- Staged alternatives keep Windfall and cut Cyclonic Rift or Magus of the Moon instead; both are complete 100s.

## Owner direction
- Neither cut is an owner addition or explicit keep. The owner's 2026-10-14 adds were Damping Sphere, Necropotence, An Offer You Can't Refuse, Contamination, Dark Ritual, Force of Negation, Mindbreak Trap, Skullclamp, Flooded Strand, Marsh Flats, Arid Mesa and Phyrexian Tower. The owner explicitly retained Damping Sphere, Trinisphere, Chalice of the Void, Blood Moon, Back to Basics, Necropotence, Overburden, Tangle Wire and Karn, the Great Creator. All of these are kept, so no owner card is overridden.
- Pass C's competing cut, Overburden, is an owner explicit keep. The test +Arcane Signet −Overburden (keep Amber) measures slightly more mana (turn 4 mean 3.225), but Overburden's value is its lock, which a mana goldfish does not see. Without clear evidence against an owner keep, it is rejected.
- **Owner-removed cards and classes are not re-added:** Arcane Laboratory and the one-spell-cap class, Black Market Connections, Defense Grid, Grafdigger's Cage, Kederekt Parasite, Nekusar, the Mindrazer, Phyrexian Tyranny, Psychosis Crawler, Exotic Orchard, Luxury Suite, Training Center, Urborg, Tomb of Yawgmoth, the turbo package (Thassa's Oracle, Demonic Consultation, Ad Nauseam, Rite of Flame, Cabal Ritual, Simian Spirit Guide, Final Fortune, Borne Upon a Wind), Gilded Drake, Dress Down, Mnemonic Betrayal, The One Ring, Hullbreaker Horror, Stranglehold, Vexing Bauble, Chains of Mephistopheles, Nether Void, Smokestack and broad symmetric taxes.
- The staged alternatives are complete 100s built on the candidate, so the owner can pick one directly.
- Disclosed baseline tension, not changed: our own Torpor Orb stops Overburden's trigger and our own Orcish Bowmasters' enter trigger (Torpor Orb ruling 2024-04-12). Both are owner cards.

## Pass C requested tests (bounded finite versions; not win rates)
These are in `data/grixis/m7/research_challengers/Grixistax___October_2026_bounded_measured_tests_20261023.json` and recomputed or consistency-checked in `tests/test_m6_grixistax_october_2026_m7_mechanics.py`.

Pass C's final disposition was **NEEDS TESTING**: retain the canonical deck, and compare it against +Talisman of Indulgence −Mox Amber, +Arcane Signet −Mox Amber and any justified alternative cut, with real payability, the colourless-Karn Mox Amber case and separate Moon / Contamination / Back to Basics states. The Pass C receipt is a NON-INDEPENDENT owner-equivalent review (alias Josh-Lee-Kwai, ChatGPT/OpenAI GPT-6, with a technical-independence waiver).

1. **Mana deployment by lock state** (seeded Monte Carlo goldfish, seed 27, 40,000 games per cell, on the play, no mulligans; turn 4):

   | Configuration | Mean mana (no lock) | P(5 with B, Tevesh) | P(U) under Contamination | P(UU) under Contamination |
   |---|---|---|---|---|
   | Baseline (Mox Amber) | 3.138 | 0.1526 | 0.2788 | 0.0377 |
   | +Arcane Signet −Mox Amber (candidate) | 3.193 | 0.1657 | 0.3299 | 0.0533 |
   | +Talisman of Indulgence −Mox Amber | 3.193 | 0.1657 | 0.2722 | 0.0342 |
   | +Arcane Signet −Overburden (keep Amber) | 3.225 | 0.1721 | 0.3361 | 0.0576 |

   Arcane Signet matches or beats Talisman of Indulgence in every lock state and turn, so Talisman is dominated. Mox Amber is live given deployed only 0.051/0.086/0.173/0.274 on turns 1–4, and never off Karn alone.
2. **Token engine and staged Opposition** (same model): see the table in the red-team memo. Opposition's deployability is below Static Orb's in every lock state.
3. **Blue Force-pitch availability (exact hypergeometric).** P(another blue card in hand, given a Force in hand), turns 1–6:

   | List (blue nonland cards in 98) | T1 | T2 | T3 | T4 | T5 | T6 |
   |---|---|---|---|---|---|---|
   | Baseline (22) | 0.7748 | 0.8262 | 0.8663 | 0.8975 | 0.9217 | 0.9404 |
   | Candidate (21) | 0.756 | 0.809 | 0.851 | 0.8841 | 0.9102 | 0.9306 |

   Colour is from Oracle; Pact of Negation is blue by its colour indicator despite its {0} cost.
4. **Matched-hand games against opponents.** Not run: the repo has no validated game engine for this deck and no opponent model.

Commander Spellbook: 6 complete combos in the baseline, the candidate and every alternative (1368-1414-4856, 1368-3518-4856, 1368-1878-2706, 1368-2706-3518, 2581-5065, 2163-5065).

Not done, stated plainly: there were no matched-hand games, no opponent model and no win rates. The deployment model ignores what the locks do to opponents, so the numbers measure our own mana and engine access only.

## Limits
Only finite scripted rules cases, exact enumerations and seeded proxies are tested.

- Game Changers 22 → 22 (Bracket 5).
- Average nonland MV 2.06 → 2.07.
- Commander Spellbook 6 → 6 complete combos.
