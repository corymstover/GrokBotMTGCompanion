# Admiral Beckett Brass rev2 — source-paid mana, curve and color constraints for exact M6 J (2026-10-22)

**Exact physical source:** `data/grixis/m7/research_challengers/Admiral_Beckett_Brass_six_Wave_Palisade_draw_resilient_20261022.txt`. Raw SHA-256 `ff5f54f9f608ab0facd62fd3b79df16a0255b4dbbc12d39154a127f27bb8c000`. This is a mana *feasibility and opportunity-cost analysis*, not a statistical hand-frequency or four-player game proxy.

## Mana and role inventory from saved 97-name Oracle source

The complete 100 includes **35 physical lands** and **65 nonlands**, **34 creature cards**, **97 distinct names** (three Islands, two Mountains and one Swamp, with otherwise singleton card names). Printed mana-value histogram across all 65 nonland cards, counting X as zero: MV1 **9**, MV2 **23**, MV3 **15**, MV4 **12**, MV5 **6**; calculated mean approximately **2.74**. The commander is MV4 `{1}{U}{B}{R}`. `Cosmotronic Wave` `{3}{R}` replaces `Raise the Palisade` `{4}{U}`; both sorceries, so it moves one spell from MV5 into MV4 and changes its colored pip from U to R. The 35-land and 34-creature quantities are unchanged from D. The source-bound count tests reject a falsely rounded or extra card.

### Real four-land source witness

Assume the precise four *untapped and available* lands **Underground Sea**, **Volcanic Island**, **Badlands**, **City of Brass** under our control, with no mana-spending actions yet this main phase:

- Commander: tap Underground Sea for U, Badlands for B, Volcanic Island for R and City of Brass for the generic {1} (City deals 1 damage to its controller when tapped). This genuinely pays `{1}{U}{B}{R}`, but uses **all four lands**.
- A different turn with the same four untapped land sources: tap Volcanic Island for R, the other three for `{3}`; this pays Wave `{3}{R}`. It is invalid to cast Admiral on turn 4 using all four and then also claim a same-main-phase Wave paid from those lands; a normal line plays Admiral while three *older* Pirates exist, then Wave on a later untap turn if Admiral survives.
- The same four lands do **not** pay Palisade `{4}{U}` (five mana required), nor Open X=3 `{3}{U}{U}` (five mana required).
- If a fifth untapped mana source is added and two of Underground Sea, Volcanic Island and an additional blue-capable source are available, both Palisade `{4}{U}` and Open X3 `{3}{U}{U}` may be payable separately, not simultaneously from the same sources. Colored restrictions remain real; five available exclusively red/black mana cannot cast Open X3.
- Instant Cannonade `{2}{R}` requires three untapped mana on the opponent's turn if used defensively, and prevents spending those same reserved sources on earlier unrelated actions. Wave cannot be held up as a similar flash-speed defensive spell.

The source does **not** claim a probability of having this hand, three old Pirates and commander on turn four, nor unopposed survival. Previous D exact four-turn and adversarial fixtures provide a *conditional legally paid witness only*; M6 I qualitative judgment weighs it with resilience and actual card roles rather than treating one witness as a win-rate advantage.

## Why the land and color choices matter to a Pirate theft shell

The earlier D `City of Brass` IN / `Crumbling Necropolis` OUT improves an untapped one-of-each-color opening, but City costs one life on each use and is a real downside. `Path of Ancestry` remains deliberately: it enters tapped but supplies U/B/R for Pirate/commander costs and a conditional scry when spent casting a matching Pirate. Replacing it with black-only `Shizo, Death's Storehouse` is not just a free turn-speed improvement; Shizo's additional `{B}, {T}` activation needs another black source for fear on a legendary creature and cannot fund a spell/color cost and its own fear simultaneously.

The source includes Cavern of Souls and Secluded Courtyard tribal restrictions, fetchlands with real target/fetch decisions, mana rocks with colored symbols, the `{U}{U}` of Open/Counterspell and `{1}{U}{B}{R}` commander. A raw 35-land count cannot by itself prove colored consistency, but the choice preserves the same proven D mana core with no changed lands. Side-by-side current list/oracle checks and bounded source-payability tests are reusable; new Wave is one red pip, with generic 3, and does not impose a novel double-color requirement. No unsupported claim of an exact opening-hand percentage is made.

## Draw, sweep and tempo resource tradeoffs

- Retained `Bident of Thassa` and `The Indomitable` both cost `{2}{U}{U}`, but can draw each time our creatures connect; `Kindred Discovery` MV5 rewards Pirate attacks/entries. Cutting any of these for a narrow extra one-shot evasion tool would reduce continuation after the theft turn.
- Retained `March of the Drowned` is `{B}` **sorcery**, returning one creature or two Pirates from graveyard; this cheaply recharges the low-drop threat plan after removal but does not operate at instant timing.
- Retained `Fiery Cannonade` `{2}{R}` instant can remove 2-toughness **non-Pirate** defenders on another player's turn. With Cannonade cut, even having `Wave` `{3}{R}` and Palisade `{4}{U}` in hand cannot substitute on that turn.
- Removing Palisade gives up a longer-term non-Pirate creature bounce. Wave's block ban expires at end of turn and its one damage usually leaves high-toughness creatures intact. This loss is accepted as the strategically preferable all-purpose *role allocation* in the seven-candidate bounded pool, not denied.

### Limits, ownership and reproducibility

The model is exact-source arithmetic, no Monte Carlo, no invented mana or extra land drops. Mana values derive from the archived 97-name Scryfall snapshot and exact approved-source-derived TXT. The original D M6 J mana report is preserved as an immutable historical artifact; this report binds the *new* six-change candidate. The new J checker must SHA-bind these report bytes and the result list, and disclose that M6 I is local tested-pool best, not global best. M6.10 remains 0 owner-accepted, Admiral M7 owner approval withheld and canonical deck locked.
