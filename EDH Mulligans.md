# EDH Mulligans

> **Auto-generated** by `scripts/build_mulligans.py` (Bot cycle 6, issue [#31](https://github.com/corymstover/GrokBotMTGCompanion/issues/31)) from Scryfall Oracle bulk 2026-10-15. Do not hand-edit.
> **Data:** every card listed is **Commander-legal** per Scryfall. *Identity* is its color identity: it fits a deck only if that identity is a subset of the commander's ([CR 903.4](Rules%20Interactions.md#commander-color-identity)). Lists are ordered by Scryfall `edhrec_rank` (EDHREC popularity, lower = more played); popularity is not power. **GC** = official Game Changer, which affects the [Commander Brackets](EDH%20Standards.md#power-bracket-assessment). *Cheapest USD* is the lowest current paper price across printings in Scryfall's default-cards bulk (2026-10-15 snapshot; prices move daily). Categories are Oracle-text pattern matches; the patterns are listed in each section.
> **Guidance** paragraphs are strategy advice (opinion), not rules or fact. Rules are quoted from the cached Comprehensive Rules (`MagicCompRules-20260925.txt`). The odds are exact hypergeometric math for a 99-card library (one commander; with two commanders it's 98, and the numbers barely change).

## Rules (fact)

> **CR 103.5** — Each player draws a number of cards equal to their starting hand size, which is normally seven. (Some effects can modify a player’s starting hand size.) A player who is dissatisfied with their initial hand may take a mulligan. First, the starting player declares whether they will take a mulligan. Then each other player in turn order does the same. Once each player has made a declaration, all players who decided to take mulligans do so at the same time. To take a mulligan, a player shuffles the cards in their hand back into their library, draws a new hand of cards equal to their starting hand size, then puts a number of those cards equal to the number of times that player has taken a mulligan on the bottom of their library in any order. Once a player chooses not to take a mulligan, the remaining cards become that player’s opening hand, and that player may not take any further mulligans. This process is then repeated until no player takes a mulligan. A player can take mulligans until their opening hand would be zero cards, after which they may not take further mulligans.

> **CR 103.5c** — In a multiplayer game and in any Brawl game, the first mulligan a player takes doesn’t count toward the number of cards that player will put on the bottom of their library or the number of mulligans that player may take. Subsequent mulligans are counted toward these numbers as normal.

> **CR 103.6** — Some cards allow a player to take actions with them from their opening hand. Once the mulligan process (see rule 103.5) is complete, the starting player may take any such actions in any order. Then each other player in turn order may do the same.

> **CR 103.6a** — If a card allows a player to begin the game with that card on the battlefield, the player taking this action puts that card onto the battlefield.

> **CR 103.6b** — If a card allows a player to reveal it from their opening hand, the player taking this action does so. The card remains revealed until the first turn begins. Each card may be revealed this way only once.

**In practice (fact, from the rules above):** in a multiplayer Commander game your **first mulligan is free**. You draw a fresh 7 and bottom 0. The second mulligan bottoms 1, the third bottoms 2, and so on. Players decide in turn order, starting with the starting player, and then everyone who chose to mulligan does so at the same time (103.5).

> **Note:** some tables play house rules, such as extra free mulligans or the older "Partial Paris" style. Those aren't in the CR, so agree on them in the pre-game talk.

## Opening-hand land odds (math)

P(the opening 7 has the given number of lands), drawn from 99 cards:

| Lands in deck | 0–1 lands | 2 lands | 3–4 lands | 5+ lands | ≥ 2 lands | ≥ 3 lands |
|---|---|---|---|---|---|---|
| 33 | 25.4% | 31.7% | 39.0% | 3.9% | 74.6% | 42.9% |
| 34 | 23.5% | 31.1% | 40.8% | 4.5% | 76.5% | 45.3% |
| 35 | 21.8% | 30.5% | 42.6% | 5.1% | 78.2% | 47.7% |
| 36 | 20.1% | 29.7% | 44.3% | 5.8% | 79.9% | 50.1% |
| 37 | 18.6% | 28.9% | 45.9% | 6.6% | 81.4% | 52.5% |
| 38 | 17.1% | 28.1% | 47.4% | 7.4% | 82.9% | 54.8% |
| 40 | 14.4% | 26.2% | 50.2% | 9.2% | 85.6% | 59.4% |

## Odds of seeing a key piece (math)

P(at least one copy of a card group, such as ramp, removal or your combo pieces), by group size and cards seen. 7 is the opening hand; 8, 10 and 12 are by your turns 1, 3 and 5 on the draw, drawing one card a turn with no other card draw.

| Copies in deck | 7 cards | 8 cards | 10 cards | 12 cards |
|---|---|---|---|---|
| 1 | 7.1% | 8.1% | 10.1% | 12.1% |
| 3 | 19.9% | 22.5% | 27.6% | 32.4% |
| 5 | 31.2% | 35.0% | 42.0% | 48.3% |
| 8 | 45.6% | 50.4% | 58.7% | 65.9% |
| 10 | 53.7% | 58.7% | 67.4% | 74.3% |
| 12 | 60.7% | 65.9% | 74.3% | 80.8% |
| 15 | 69.6% | 74.5% | 82.3% | 87.8% |

## Opening-hand cards (CR 103.6)

Cards that act from your opening hand. They're Commander-legal and sorted by EDHREC rank. Pattern: `in your opening hand`.

| Card | Identity | MV | EDHREC rank | Cheapest USD | GC |
|---|---|---|---|---|---|
| [Gemstone Caverns](cards/G/ge.md#gemstone-caverns) | C | 0 | 181 | $60.64 |  |
| [Leyline of Anticipation](cards/L/le.md#leyline-of-anticipation) | U | 4 | 755 | $5.11 |  |
| [Leyline Axe](cards/L/le.md#leyline-axe) | C | 4 | 1,356 | $5.04 |  |
| [Leyline of the Guildpact](cards/L/le.md#leyline-of-the-guildpact) | WUBRG | 4 | 1,721 | $4.02 |  |
| [Leyline of Abundance](cards/L/le.md#leyline-of-abundance) | G | 4 | 3,021 | $1.81 |  |
| [Leyline of Hope](cards/L/le.md#leyline-of-hope) | W | 4 | 3,376 | $0.74 |  |
| [Leyline of the Void](cards/L/le.md#leyline-of-the-void) | B | 4 | 3,534 | $0.36 |  |
| [Leyline of Transformation](cards/L/le.md#leyline-of-transformation) | U | 4 | 3,550 | $0.51 |  |
| [Leyline of Resonance](cards/L/le.md#leyline-of-resonance) | R | 4 | 5,376 | $0.72 |  |
| [Leyline of Mutation](cards/L/le.md#leyline-of-mutation) | WUBRG | 4 | 6,457 | $0.31 |  |
| [Leyline of Sanctity](cards/L/le.md#leyline-of-sanctity) | W | 4 | 7,603 | $0.25 |  |
| [Leyline of Punishment](cards/L/le.md#leyline-of-punishment) | R | 4 | 10,652 | $2.99 |  |
| [Leyline of Combustion](cards/L/le.md#leyline-of-combustion) | R | 4 | 10,870 | $0.42 |  |
| [Leyline of Vitality](cards/L/le.md#leyline-of-vitality) | G | 4 | 11,328 | $3.18 |  |
| [Leyline of Lifeforce](cards/L/le.md#leyline-of-lifeforce) | G | 4 | 13,289 | $5.97 |  |
| [Leyline of Lightning](cards/L/le.md#leyline-of-lightning) | R | 4 | 13,291 | $0.25 |  |
| [Leyline of Singularity](cards/L/le.md#leyline-of-singularity) | U | 4 | 14,256 | $5.45 |  |
| [Quicksilver, Brash Blur](cards/Q/qu.md#quicksilver-brash-blur) | R | 1 | 14,594 | $0.26 |  |
| [Leyline of the Meek](cards/L/le.md#leyline-of-the-meek) | W | 4 | 17,528 | $1.47 |  |

19 matches in total.

## Keep or mulligan? (guidance)

*Strategy opinion, not rules or fact. Adjust it to your deck and bracket.*

**Usually keep:**
- 3–4 lands plus at least one early play (ramp, card draw or interaction).
- 2 lands plus 2+ cheap ramp pieces or cantrips, especially on the draw.
- Any hand that executes your deck's plan by turn 3–4.

**Usually mulligan (the first one is free):**
- 0–1 lands, unless it's a cEDH hand with heavy fast mana and you've weighed the risk.
- 6–7 lands with no card draw.
- Hands where every spell costs 5 or more mana.
- Hands missing the colors your spells need, with no fixing.

**Mulligan to a plan:**
- After the free mulligan, keep a functional 6 rather than chasing a perfect hand.
- In competitive play (Bracket 5) you may mulligan more aggressively for fast mana, tutors or a protected win. See the [cEDH Primer](cEDH%20Primer.md).
- Use the land odds above to set your deck's land count. The [EDH Mana Bases](EDH%20Mana%20Bases.md) guide recommends 36–38 lands plus about 10 ramp pieces for casual decks.

## Priorities by archetype (guidance)

*Strategy opinion, not rules or fact.* Archetype names link to the [EDH Archetypes](EDH%20Archetypes.md) guides.

| Archetype | Opening hand wants | Early-game priorities |
|---|---|---|
| [Aristocrats](EDH%20Archetypes.md#aristocrats-sacrifice--death-triggers) | A sac outlet or a death-trigger payoff, plus fodder | Turns 2–4: assemble an outlet, a payoff and fodder; keep a recursion piece in reserve |
| [Tokens / go-wide](EDH%20Archetypes.md#tokens--go-wide) | A token maker by turn 3 and ramp | Build the board, then hold the anthem or overrun until it's lethal or close |
| [Spellslinger](EDH%20Archetypes.md#spellslinger-instants--sorceries) | Cheap cantrips or rituals plus a payoff, or the commander castable on time | Get the engine (commander or payoff) down first; keep a counterspell up afterwards |
| [Lands / landfall](EDH%20Archetypes.md#lands-matter--landfall) | 4+ lands or land-ramp; extra-land-drop effects | Ramp every turn; get landfall payoffs down before fetches and extra drops |
| [+1/+1 counters](EDH%20Archetypes.md#11-counters) | 2-drop counter creatures or a proliferate engine | Curve out; get doublers (Hardened Scales effects) down before the payoffs |
| [Graveyard / reanimator](EDH%20Archetypes.md#graveyard-value--reanimator) | A self-mill or discard outlet plus a reanimation spell | Fill the graveyard early; be wary of opposing graveyard hate before going all in |
| [Blink / flicker](EDH%20Archetypes.md#blink--flicker) | ETB creatures plus ramp to reach the blink engine | Value ETBs first; land the repeatable blink engine when it can be protected |
| [Artifacts](EDH%20Archetypes.md#artifacts) | Mana rocks or cheap artifacts plus a payoff | Use rocks to reach the payoffs fast; spread artifacts out in case of a board wipe |
| [Voltron / extra combats](EDH%20Archetypes.md#combat--voltron--extra-combats) | Protection plus equipment or auras, or a fast commander | Commander out by turn 2–3; hold protection up instead of overcommitting auras |
| [Cascade & big spells](EDH%20Archetypes.md#cascade--big-spells) | Heavy ramp: 2+ ramp pieces or 4+ lands | Ramp turns 1–3, then cast the cascade engine or the commander |
| [Group hug / slug](EDH%20Archetypes.md#group-hug--group-slug) | Lands and the commander castable on time | Develop quietly; let the table spread its aggression around |
| [Life as a resource](EDH%20Archetypes.md#life-as-a-resource--lifedrain) | A lifegain or drain engine and cheap card advantage | Get engines down early; pay life aggressively only when it's safe |

