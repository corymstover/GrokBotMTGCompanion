# Crosis, the Purger — ChatGPT independent M7 Rev2 (2026-10-23)

**Status: FINAL OWNER-REVIEW CANDIDATE ONLY. NOT OWNER APPROVED. NOT LOCKED. DO NOT CHANGE CANONICAL.**

- Tracker: Deck #10 (`Crosis__the_Purger`).
- Canonical baseline (historically approved Oct 14): `corymstover/grixis-commander-encyclopediaGPT:main/refinement/decklists/Crosis_the_Purger_Approval_Candidate_2026-10-14.txt`. Raw SHA-256 `a59150c323aa1e21cbda65291a3b172d08ecc3b83266b708768f4e14f0b07ec1`. The registry records this exact raw; no provenance exception. Its tracker note claims a prior Regalia/Specter substitution inconsistent with the bound list, which contains both. Preserve original evidence.
- Grok first pass PR #658: 5 swaps, SHA `244f19b9465e499c390bcac10eb96ad04d73f4b760a09cfef1d526f47be98347`. Retain unmodified as research. Its source-bound full 197-card Scryfall pool and finite tests remain untouched; this revision does **not** imply an official independent second-model Pass C.
- ChatGPT Rev2 exact raw candidate `a2f842355958dc8579b01eb067197ea303102e358d1c4ff658c3aed18cfd9d4a` (trailing LF, UTF-8). Exactly 100 physical, 1 commander and 99 library, 95 rows, only Island/Mountain/Swamp repeat; 36 lands, 12 baseline acceleration artifacts after -Jet and keeping Izzet, 14 Game Changers, no project legality exceptions. Grixis identity U/B/R; all 95 card names resolved against Oct23 Scryfall records. **Power Bracket 4 — Optimized**. Tags: **Discard / Dragons / Extra Combats**.
- New named cards `Otawara, Soaring City`, `Takenuma, Abandoned Mire`, `Sokenzan, Crucible of Defiance`: exact Oracle IDs, text, legality from Oct23 live Scryfall records archived in the *canonical* Cecily/Bjorna selected verification JSON, separately re-bound for this deck as `Crosis__the_Purger_M7_Rev2_Addon_Scryfall_20261023.json`. Every other name is in the Crosis archived Oct23 snapshot. No live Scryfall API rerun or pipeline rerun is claimed.

## Commander-first decision

Crosis is a six-mana flying 6/6. Combat damage to a player allows paying {2}{B} and naming one color; that player discards all cards of that color. Painter's Servant lets the chosen color catch *all* cards, even originally colorless cards in hands. The deck must get Crosis into play on time, deliver reliable combat damage, have usable {2}{B}, and convert multiple discards into lethal damage/value. Brotherhood Regalia (unblockable, ward 2), Greaves/Boots (haste/protection), Shizo, Sword of Feast and Famine, Cavern of Souls and the six-color fetch/dual base are preserved.

## Exactly nine swaps — five is a floor, not a ceiling

| Add | Cut | Independent reasoning / downside |
|---|---|---|
| Megrim | Jet Medallion | Each discarded opponent card deals 2 additional **damage**, tripling the original Caress-only payoff together with Raiders' Wake. Lose an actual commander-generic-cost discount on Crosis and other black spells; do not pretend Medallion was a dead card. |
| Rankle, Master of Pranks | Blizzard Specter | Hasty flyer that can choose discard, symmetric draw/loss or sacrifice on combat damage, enabling pressure before Crosis. Its chosen modes affect **each** player, including controller; not a free unilateral discard. |
| Aggravated Assault | Dream Salvage | Extra combat creates another chance for the commander to connect; incumbent Sword of Feast and Famine can untap lands for repeat Assault activations. Requires {3}{R}{R} in a main phase each time, and connecting; pay extra {2}{B} for each Crosis purge. Lose post-discard card draw from Salvage. |
| Raiders' Wake | Oppression | Asymmetric per-card 2-life loss with raid discard after attacking, not the original both-sided spell-cast discard that taxed our own spells and could empty hands *before* Crosis connects. Lose symmetric prison pressure. |
| Deadly Rollick | Fell Specter | Free exile interaction while controlling Crosis, leaving mana for {2}{B} and clearing a blocker; **keeps Izzet Signet** and therefore one more early acceleration artifact than Grok's five. Fell's four-mana 1/3 ETB discard and repeat Caress-style trigger are real losses; the lower-cost Megrim/Wake/Ascension package now supplies repeated punishments. |
| Bloodchief Ascension | Bottomless Pit | {B} quest adds late per-card life drain and life gain on opponents' cards entering graves, synergizing with Crosis purge/wheels while removing another symmetric discard that strips our hand and pre-emptively empties opponents'. It requires **three** qualifying end steps before draining: explicitly no immediate 2-life loss claimed. |
| Otawara, Soaring City | 1 Island | Untapped U source with channel bounce of a blocker/enchantment at {3}{U}, one less per legend; stronger commander-connect utility. Lose one fetchable basic Island and add Back to Basics/Blood Moon exposure. |
| Takenuma, Abandoned Mire | 1 Swamp | Untapped B source with instant-speed channel mill three and recover Painter's Servant, Rankle, Tergrid or another creature from graveyard; reduced per controlled legend. Lose one fetchable basic Swamp, more nonbasic exposure. |
| Sokenzan, Crucible of Defiance | 1 Mountain | Untapped R source with channel two hasty 1/1 Spirits, makes attackers for Raiders' Wake raid and blockers when commander is expensive; legendary discount. Lose one fetchable basic Mountain and nonbasic-hate resilience. |

**Why correct Grok's rock cut:** The first-pass removed both Jet Medallion and Izzet Signet, from 13 to 11 acceleration artifacts, in a six-drop commander. This independent nine-swap candidate preserves **Izzet Signet**, cutting a redundant slower four-mana discard body instead, and retains 12 acceleration artifacts. It keeps Dark Deal: a wheel that refills opponents' hands and produces a burst of per-card triggers is crucial for a color-purge commander, so using it as the Bloodchief cut was rejected.

**Remaining hold/cut challenges:**
- Court of Ambition over Bottomless Pit: another asymmetric monarchy/punishment tool, but the opponent can choose life loss instead of discarding, so it often does **not** fire the card-discard payoff suite. Bloodchief does more for actual purge outcomes at one mana and removes the symmetric Pit. No Court added.
- Painful Quandary: 5 mana and each opponent chooses life rather than discard; too slow and unreliable for this engine.
- Dauthi Voidwalker: exiles discarded cards, directly conflicting with Tergrid and Tinybones, Bauble Burglar graveyard theft; rejected.
- Blazing Specter over Sedraxis Specter: costs more for smaller body and lacks unearth; rejected.
- Whispersilk Cloak/Rogue's Passage: make Crosis unblockable but Regalia already does cheaply; Cloak cannot grant the Greaves' haste, Passage costs four mana to activate.
- Counterspell over Swan Song: tighter UU on a black-heavy curve; hold Swan Song and Mana Drain.
- Rhystic Study/Mystic Remora or non-engine Grixis goodstuff: would dilute commander-first identity or crowd already strong draw, rather than enhance the paid color-purge.
- Sokenzan is the most marginal channel addition; under heavy basic-land-hate/Back to Basics metagame it can rationally stay Mountain. In this optimized general-meta list, its option value and same untapped red production beat that risk.

## Verification and honest limits

- Counts: 100 physical, 95 distinct rows, 36 lands (Island x3, Swamp x3, Mountain x2 + 28 nonbasic), 12 acceleration artifacts; all nonbasics singleton.
- Oracle/identity: archived source-bound Oct23 records for all 95 names; all `commander_legality=legal`, color identities subsets of UBR. The three channel lands tap for the same colors they replace, so B/R/U **source counts are unchanged**, while basic resilience decreases.
- Game Changers: 14, same as baseline and first pass. Bracket 4. No project exception.
- Five-card Painter+Crosis purge with Megrim + Caress + Raiders' Wake: 5×(2 damage +2 life +2 life)=30 opponent life lost (assuming all stay, damage unprevented); an **active** Bloodchief adds another 10 life loss and 10 life gain. Unactivated Bloodchief adds zero.
- New Sword+Aggravated Assault interaction **conditional**, never automatic: sword-equipped creature must hit a player for Sword to untap lands; activation as sorcery after combat needs five mana with {R}{R}; Crosis's paid trigger separately needs {2}{B}. To pay both per repeat from untapped lands requires at least eight usable mana with the color requirements. When an opponent has no cards in hand a paid Crosis trigger discards zero even if Crosis still hits.
- Existing Notion Thief + Teferi's Puzzle Box hand lock remains, conditional on both being present.
- Independent strategic judgments; source-bound finite checks and focused CI are not gameplay simulations, statistical win rates, or external owner approval.
- The research PR is stacked on Grok #658 and includes inherited unmerged earlier PR infrastructure. Do not blind merge into integration; retain as engineering proposal until safely consolidated. Canonical October 14 approval remains exactly as-is unless Cory explicitly approves **this raw 100**.

**Gate:** PRESENT `a2f842355958dc8579b01eb067197ea303102e358d1c4ff658c3aed18cfd9d4a` to Cory with the entire list, nine add/cut pairs and tradeoffs; only his explicit approval of the exact candidate authorizes canonical PR, merge and post-merge lock.
