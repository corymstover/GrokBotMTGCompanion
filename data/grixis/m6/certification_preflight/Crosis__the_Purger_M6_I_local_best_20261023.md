# Crosis, the Purger — M6 I local-best memo for the M7 candidate (2026-10-23)

This memo is evidence only. The candidate is NOT owner approved and NOT M6 certified, and the canonical list is unchanged.

Scope: the seven complete configurations in
`data/grixis/m6/ij/tested_pools/Crosis__the_Purger_M7_tested_configurations_20261023.json`, plus named single-card contenders. Each configuration is 100 = 1 commander + 99 library. This is not a global or statistical optimum.

## Result
The preferred five (raw 244f19b9…) is the local best of the tested pool:
- Adds: +Megrim, +Rankle, Master of Pranks, +Aggravated Assault, +Raiders' Wake, +Deadly Rollick.
- Cuts: −Jet Medallion, −Blizzard Specter, −Dream Salvage, −Oppression, −Izzet Signet.

## Why (commander-first)
Crosis ({3}{U}{B}{R} 6/6 flying Dragon) wins through combat damage. Each hit can cost {2}{B} to make that player discard every card of a chosen color, or the whole hand with Painter's Servant. The approved list ramps into him, protects and connects him (Greaves, Boots, Brotherhood Regalia, Sword of Feast and Famine, Cavern of Souls), and surrounds him with discard and discard payoffs (Liliana's Caress, Waste Not, Tergrid, Tinybones, the wheels).

The five adds each serve that plan better than the slot they take:
- **Megrim** deals 2 damage per discarded card (CR 603.2c: once per card in a multi-card purge). It is the signature Crosis payoff (64% of EDHREC Crosis decks) and Pass C's top hypothesis. **Jet Medallion** only discounts black spells and is the weakest of 13 rocks.
- **Rankle, Master of Pranks** is a hasty flyer with three modes per hit. **Blizzard Specter** has no haste (Pass C correction) and one mode.
- **Aggravated Assault** gives extra combats, so Crosis triggers again. With the incumbent Sword of Feast and Famine, put Crosis's trigger on the stack first so Sword resolves first and untaps the lands; then pay {2}{B} and use {3}{R}{R} in the next main phase. Spellbook 900-3750 lists this as infinite combat phases, here conditional on connecting each combat. **Dream Salvage** only draws after a purge.
- **Raiders' Wake** is asymmetric: 2 life per opponent discard, plus a raid discard each turn we attack. **Oppression** is symmetric: it taxes our own 25 instants/sorceries and empties hands before Crosis purges them.
- **Deadly Rollick** is free exile while Crosis is on the battlefield (CR 903.3d). It clears blockers or answers threats while {2}{B} stays up for the trigger. **Izzet Signet** is the third Signet in a 36-land list, on the least-needed color pair.

## Self-challenge
- **Four-swap keeping Oppression:** staged and rejected (MODERATE). Oppression's symmetric tax fights our spells and the purge.
- **Pass C's pairing, Megrim over Sedraxis Specter with Jet Medallion kept:** staged five-swap, rejected (HIGH). Sedraxis kept: it is a three-mana recursive flyer (unearth) that feeds every punisher, and Medallion is the weaker slot.
- **Bloodchief Ascension over Dark Deal:** six-swap, staged, RETAIN_ALTERNATIVE, not selected. It needs three end steps to activate; Dark Deal is an immediate burst with three punishers.
- **Painful Quandary over Bottomless Pit (plus Bloodchief):** seven-swap, staged, rejected. Five mana, opponents choose, and Pit is a 3-mana every-upkeep discard.
- **Rejected singles:** Blazing Specter (vs Sedraxis), Dauthi Voidwalker (conflicts with Tergrid and Tinybones, Bauble Burglar), Snuff Out (cannot hit black creatures), Whispersilk Cloak (Greaves' haste matters more), Counterspell (UU; Mana Drain fills it), Sulfurous Springs (Xander's Lounge is the tri-typed fetch target), Hypnotic Specter (Tinybones legendary package). Excluded: Hullbreacher and Hymn of the Wilds (banned), Valgavoth's Onslaught (green).

## Limits
Only finite rules cases are tested (tests/test_m6_crosis_the_purger_m7_mechanics.py). There is no simulation or win-rate data. Pass C's requested risk-based Phase B (Megrim with hand depletion 0/3/5/7) is answered here only with deterministic finite damage arithmetic, not a measured multiplayer delta.

Main losses:
- Jet Medallion's black cost reduction and Izzet Signet's ramp (mana rocks 13 → 11).
- Blizzard Specter's bounce mode.
- Dream Salvage's post-purge draw.
- Oppression's symmetric stax.
- Average nonland MV 2.286 → 2.381.
