# Gwendlyn Di Corci — independent ChatGPT M7 Rev1 research, 2026-10-24

**STATUS: SIX-SWAP RESEARCH CANDIDATE, NOT OWNER APPROVED, NOT CANONICAL.** The owner must see and explicitly approve the *complete* exact 100 and raw SHA before canonical modification. Previous #1–21 new M7 locks remain untouched.

## Sources and frozen baselines

- Historical locked Gwendlyn (October 14): `refinement/decklists/Gwendlyn_Di_Corci_Approved_2026-10-14.txt`, raw SHA-256 `9a393cb7edf40f9bfb388d37dd657839cad851dc6a021440c7d1b239c1fd20a9` **with no trailing newline**. The source was re-fetched directly from exact canonical main and re-hashed.
- GrokBot [PR #670](https://github.com/corymstover/GrokBotMTGCompanion/pull/670), source head `7483728a700e01f2b45172c9c55438903d9092ac`, researched one change (+Hymn/-Dauthi), withdrew as below M7 five-swap floor. Original GROK research, tests, J certificate and workflow stay unchanged.
- Independent six-swap candidate: `data/grixis/m7/independent_candidates/Gwendlyn_Di_Corci_M7_Rev1_Proposed_20261024.txt`, final newline, exact raw SHA `36b76cbe47a04b7492007103e4baaad50324b3e72fb2067b28aa8bb9da70e355`. This is a new engineering source, **NOT** canonical.

## Six independent add/cut pairs

| Add | Cut | Commander-first reason | Material loss |
|---|---|---|---|
| Hymn to Tourach | Dauthi Voidwalker | BB random-discard burst, and no Dauthi graveyard replacement suppression of Tergrid, Tinybones Bauble Burglar or Bloodchief Ascension | Lose shadow clock, graveyard hate and free void-card casting; blank when hellbent |
| Rings of Brighthearth | Underworld Dreams | Copy Gwendlyn's tap ability for **{2} per activation**; Rings plus existing Illusionist's Bracers generates original + two separately triggered copies (3 total, NOT 4) | Lose BBB Wheel draw-punisher damage reach; Rings needs ongoing generic mana and surviving commander |
| Sting, the Glinting Dagger | The Raven Man | Gives Gwendlyn haste and a start-of-**each-combat** untap, so tap in own main, untap at own combat start, tap again | **Cast {2}, equip {2}** (not free); loses Raven's flying Bird tokens and {3}{B},{T} each-opponent discard |
| Misty Rainforest | Crumbling Necropolis | Untapped Island-type typed dual fetch can improve critical UBBR development; supports U/B or U/R, Xander's Lounge all three tapped | 1 life, possible additional shock life, less unconditional tri-color certainty |
| Marsh Flats | Drowned Catacomb | Untapped Swamp-type UB/BR dual selection adds an accessible *red* source and avoids checkland tap conditions | 1 life, shock-life risk, searches/counter-search and narrower targets |
| Shivan Reef | One of the two Mountains | R→U/R untapped choice supports Gwendlyn's blue pip and later Pemmin {U} activations; one basic Mountain remains | Life for colored mana, weaker basic/fetch/Blood Moon resiliency |

**Six is not a cap:** credible seventh candidates were considered (Freed from the Real, other mana rocks, wheel and discard redundancy), but none justified a clean cut without losing owner-protected speed, recursion, draw or tap infrastructure. No filler swap added.

### Actual strategic effects

Gwendlyn is {U}{B}{B}{R}, 3/5, and may tap to make *target player discard a random card only during our turn*. Her commander throughput is the objective, not just generic wheels or a turbo Breach deck. Rings and Sting increase her activation output while preserving Illusionist's Bracers, Pemmin's Aura, Magewright's Stone, Minamo, Patriar's Seal, Thousand-Year Elixir and Greaves.

- Gwendlyn + Rings + Bracers, one tap: one original random discard plus one free Bracers copy plus **one** Rings copy *if {2} paid*, for three total. Targets for copies may be chosen separately. No infinite engine is claimed.
- Sting untaps at the beginning of each combat, including opponents' combats, but Gwendlyn's *only during your turn* restriction means its opponent-combat untaps cannot be spent on her tap-to-discard ability in opponent turns.
- Dauthi's replacement makes cards go to exile instead of graveyard; it removes a card from Tergrid's reanimation path, Tinybones's graveyard-stash path and Bloodchief Ascension's graveyard trigger. Hymn preserves random identity and increases immediate discard density. Do not call Dauthi universally weaker against graveyard-based decks.
- The two fetches improve early untapped typed-dual access *conditional on search targets*. Xander's Lounge can supply UBR to either but enters tapped; fetches can cost 3 life if choosing an untapped shockland. No unqualified paid T4 UBBR probability is asserted.
- Shivan Reef replacing one basic Mountain preserves red access, adds blue, and pays 1 life for colored mana. One Mountain remains available for Blood Moon resilience.

## Audit, alternatives, limitations

- 100 physical cards, 95 rows, basics **2x Island, 1x Mountain, 5x Swamp**, 35 lands, 64 nonland library, 17 unchanged Game Changers, unchanged approximate average nonland MV 2.328, no project exception, B/R/U legal, Bracket 4 Optimized, tags **Discard / Wheels / Untap**.
- 93 exact names sourced from archived 2026-10-23 Scryfall 208-name pool and 2 new manually checked published Scryfall pages (Sting and Misty), without fabricated API identities. Commander Spellbook's existing Underworld Breach + Lion's Eye Diamond + Wheel of Fortune line is retained, no extra infinite asserted.
- Five-swap minus Shivan full 100 control: `data/grixis/m7/independent_candidates/Gwendlyn_Di_Corci_M7_Rev1_Five_Swap_Without_Shivan_20261024.txt`, raw `b62797355940546b1d6fdc1d8485e3c797189225bb2ffdc817a7f5fe29633e53`.
- Six-swap Freed from the Real instead of Sting full 100: `data/grixis/m7/independent_candidates/Gwendlyn_Di_Corci_M7_Rev1_Freed_Six_Swap_Alternative_20261024.txt`, raw `33a86979b9ff1376908e383b8ab4103a37db3eb6cbc8cafad3088f04cd9a93e3`. Freed can untap Gwendlyn repeatedly for U but supplies no haste, has enchant-creature vulnerability and overlaps Pemmin; Sting has a definite {2} equip cost, so the decision is a strategic trade.
- Owner-retained Mind Twist, Geth's Grimoire, Waste Not, Tinybones package, Chains/Notion wheel-denial, fast colored mana, permission and original 2026-10-14 upgrades are preserved.
- Finite source-anchored tests check structure, mana examples, conditional activations, previous protected card presence, and exact hashes. These are **not** actual games, win rates, a full game-engine simulation or an independent third-model review.

**No canonical Gwendlyn change may be made until Cory approves an exact hash after seeing the complete candidate.**
