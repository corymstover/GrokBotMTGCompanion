# Gwendlyn Di Corci — M6 I local-best memo for the M7 research candidate (2026-10-23)

This memo is evidence only. The candidate is NOT owner approved, NOT M6 certified and NOT owner-presentable. It is RESEARCH_ONLY: one genuine swap, below the five-swap floor. The canonical list is unchanged.

Scope: the nine complete configurations in `data/grixis/m6/ij/tested_pools/Gwendlyn_Di_Corci_M7_tested_configurations_20261023.json`, plus named single-card contenders. Each configuration is 100 cards (1 commander + 99 library). This is not a global or statistical optimum.

Baseline:
- Source: canonical encyclopedia main 9b26aa28fc7e16f6652aaec292b4edf84e20db71, file `refinement/decklists/Gwendlyn_Di_Corci_Approved_2026-10-14.txt` (no terminal newline).
- Blob 4ef2c267314322be9793a1e5490613b98520a24e, introduced by 111f903e. Registry source_commit 1836b97 has the same bytes.
- Raw SHA-256 9a393cb7… equals the registry's recorded_sha256, so no provenance exception is used.

## Result
The research one-swap (raw f5f26b78…, lh1:0540cd42…) is the local best of the tested pool:
- Add: +Hymn to Tourach.
- Cut: −Dauthi Voidwalker.

**Only one genuine improvement was found, so the deck is RESEARCH_ONLY.** Five is a floor, not a target. Seventeen candidates were judged and fourteen incumbents were challenged. Every other candidate failed for one of these reasons:
- **It cut an owner keep or addition without clearly better evidence:** Aphetto Alchemist over Magewright's Stone (owner keep, and the owner removed Aphetto); Rings of Brighthearth over Mind Twist (owner addition); Sulfurous Springs over Crumbling Necropolis (owner mana keep, and it measured worse).
- **It was owner-removed or in a rejected class:** Megrim (owner-removed); Whispering Madness and Drown in the Loch are generic wheel/interaction redundancy; Kederekt Parasite and Lavaborn Muse are draw/hand-size punishment bodies of the kind the owner trimmed (Bone Miser, Fell Specter, Hypnotic Specter).
- **It was marginal or off-plan:** Swiftfoot Boots duplicates Lightning Greaves; Rankle, Master of Pranks and Tinybones, the Pickpocket are combat-dependent; Davriel, Rogue Shadowmage is a weak walker; Vizier of Tumbling Sands and Retreat to Coralhelm are worse untappers than the kept Stone, Pemmin's Aura and Patriar's Seal; Mana Vault adds an 18th Game Changer for colourless mana that cannot pay Gwendlyn's pips.
- **Invalid:** Jeweled Lotus is banned.

None of these was counted. Fourteen incumbents were challenged; all except Dauthi Voidwalker were kept: Magewright's Stone, Dream Salvage, Anvil of Bogardan, Reforge the Soul, Underworld Dreams, Crumbling Necropolis, Ancient Tomb, Opposition Agent, Mind Twist, Jace's Archivist, The Raven Man, Exotic Orchard and Gamble.

## Why (commander-first)
Gwendlyn Di Corci ({U}{B}{B}{R} 3/5 Legendary Creature — Human Rogue): "{T}: Target player discards a card at random. Activate only during your turn."

- **Hymn to Tourach over Dauthi Voidwalker.** Both cost {B}{B}. Hymn is two more random discards, in the commander's own idiom.
  - Dauthi's "instead exile it with a void counter" is a replacement effect (CR 614.1a). While it is on the battlefield, an opponent's discarded or sacrificed card never reaches a graveyard.
  - That switches off three owner-kept engines: Tergrid, God of Fright ("from a graveyard"), Tinybones, Bauble Burglar ("exile it from their graveyard") and Bloodchief Ascension ("put into an opponent's graveyard"). Discard triggers (Waste Not, Liliana's Caress, Tinybones, Trinket Thief) still fire either way.
  - Bounded ledger example (7-card hand, 3 permanents, one Gwendlyn activation): with Tergrid, 0 vs 9/7 expected reanimations; with Bloodchief Ascension at 3+, 0 vs 6 life drained.
- **Cost:** continuous graveyard hate (Bojuka Bog remains), a 3-power shadow clock, Dauthi's one free void card, and Hymn is blank against empty hands.

## Owner direction
- **Cut:** Dauthi Voidwalker is not in the owner's explicit retained list, but it is named in the owner's blueprint. **Flagged owner-blueprint override:** the evidence is rules-level (it disables three explicit owner keeps), and alternatives that keep Dauthi are staged.
- **Owner keeps stand:** Lightning Greaves, Thousand-Year Elixir, Magewright's Stone, Patriar's Seal, Bottomless Pit, Oppression, Chains of Mephistopheles, Notion Thief, Waste Not, Geth's Grimoire, Liliana's Caress, the three Tinybones, Tergrid, Underworld Breach, Yawgmoth's Will, Kess, Dissident Mage and Bloodchief Ascension.
- **Owner additions stand:** Mind Twist, Illusionist's Bracers, Pemmin's Aura, Tinybones, Pocket Nuisance, Withering Torment and Minamo, School at Water's Edge.
- **Owner-removed cards are not re-added:** Bone Miser, Fell Specter, Hypnotic Specter, Sangromancer, Feed the Swarm, Megrim, Counterspell, Burning Inquiry, Winds of Change, The Locust God, Aphetto Alchemist, Battlemage's Bracers, Mindcrank and Mox Diamond. The generic Thoracle/Breach turbo-combo conversion is not adopted.
- Hymn is a single-target random discard like the owner-added Mind Twist. The owner rejected Syphon Mind, Unnerve and Necrogen Mists as generic redundancy; Hymn's distinction (random, 2 MV, one target) is a judgment call and is disclosed.

## Pass C requested tests (bounded finite versions; not win rates)
These are in `data/grixis/m7/research_challengers/Gwendlyn_Di_Corci_bounded_measured_tests_20261023.json` and recomputed in `tests/test_m6_gwendlyn_di_corci_m7_mechanics.py`.

Pass C's final disposition was **NEEDS TESTING**. It asked for a narrow controlled matrix: the untouched locked 100 vs +Aphetto Alchemist −Magewright's Stone (fallback Rings/Mind Twist only if it mattered), source-paid UBBR by turns 3–5, and resolution of the Dauthi/Tergrid interaction. The Pass C receipt is a NON-INDEPENDENT owner-equivalent review (same model family, with a technical-independence waiver).

1. **Untapper matrix.** Nine fixed states, useful random discards, Stone vs Alchemist:

   | State | Stone | Alchemist |
   |---|---|---|
   | A1 Bracers on Gwendlyn, untapper ready | 4 | 4 |
   | A2 Bracers moved to the untapper | 4 | 9 |
   | A3 untapper cast this turn | 2 | 1 |
   | A4 untapper cast this turn, Elixir out | 2 | 2 |
   | A5 Alchemist killed after 2 loops | 4 | 3 |
   | A6 Gwendlyn removed | 0 | 0 |
   | A7 opponents hellbent | 0 | 0 |
   | A8 big hands after own Wheel of Fortune | 4 | 21 |
   | A9 Pemmin's Aura, no Bracers | 4 | 5 |

   The Alchemist wins only once its Bracers loop (Commander Spellbook 283-4091, a generic infinite) is assembled. It loses the turn it is cast and when it is killed. Exact no-tutor chance of seeing two specific cards: 0.0093 / 0.0113 / 0.0136 / 0.0188 in 10 / 11 / 12 / 14 cards.
2. **Castability.** Exact chance of a source-paid {U}{B}{B}{R}: play T3 0.1439, play T4 0.511, draw T4 0.6035, play T5 0.6035, the same for baseline and candidate. Colour-agnostic upper bound play T4 0.555. Sulfurous Springs over Crumbling Necropolis: play T4 0.5094, so the Necropolis stays.
3. **Hymn vs Dauthi ledger.** 36 exact-expectation rows (6 hand states × 6 engines) and 5 adversarial scenarios (2 candidate gains, 3 disclosed candidate losses).
4. **Rings fallback.** Exact mana arithmetic: after a {3} setup, Rings out-discards Hymn's two-card one-shot within a single turn only with 6+ spare mana; with 4+ spare mana every turn it passes Hymn only over repeated turns. Pass C deprioritized the full Rings matrix, so it was not run as a state matrix.

Not done, stated plainly: there were no matched-hand games, no opponent model and no win rates. The repo has no validated Gwendlyn game engine.

## Self-challenge
- **Pass C exact (+Aphetto Alchemist −Magewright's Stone):** staged as a complete 100 on the baseline and on the candidate; RETAIN_ALTERNATIVE as an OWNER DECISION. It overrides an owner keep and an owner removal and adds a generic infinite, so it is not counted.
- **Pass C fallback (+Rings of Brighthearth −Mind Twist):** staged and rejected; it cuts an owner addition. Rings is also staged in Dauthi's slot (RETAIN_ALTERNATIVE) as the throughput option.
- **Two-swaps:** +Hymn +Aphetto / −Dauthi −Magewright's Stone (OWNER DECISION) and +Hymn +Whispering Madness / −Dauthi −Reforge the Soul (rejected; cuts an owner-listed wheel). Neither was counted.
- **Mana challenge:** Sulfurous Springs over Crumbling Necropolis measured worse and was rejected.
- **Rejected singles:** Whispering Madness, Swiftfoot Boots, Drown in the Loch, Kederekt Parasite, Lavaborn Muse, Rankle, Master of Pranks, Tinybones, the Pickpocket, Davriel, Rogue Shadowmage, Vizier of Tumbling Sands, Retreat to Coralhelm, Sulfurous Springs and Mana Vault. Jeweled Lotus is banned; Megrim is owner-removed.

## Limits
Only finite scripted rules cases and exact enumerations are tested. Main loss: Dauthi Voidwalker's continuous graveyard hate and shadow clock.

Game Changers 17 → 17 (Bracket 4). Average nonland MV 2.328 → 2.328. Commander Spellbook 1 → 1 complete combo (1368-2706-3518).
