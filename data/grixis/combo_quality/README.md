# Combo Quality Model — Step B

Status: **provisional evidence only**. These records do not approve a combo, swap, challenger, deck, or milestone.

`grixis_combo_quality.py` evaluates every cached Commander Spellbook line in the 62 canonical Birthday baselines against the accepted Commander Blueprint and dependency graph. It is intentionally a **vector model**, not one opaque combo-power score.

For each line it records:

- card count;
- a mana-value sum **proxy**, while explicitly deferring exact/colored startup mana to Step C;
- known card types and the fact that normalized execution zones are unavailable in the cached Spellbook snapshot;
- direct commander participation and Blueprint-supported commander contribution;
- Spellbook requirements and Blueprint external enablers/payoffs;
- broad timing/type and interaction-window proxies, never exact stack-window claims;
- Blueprint tutor-target coverage;
- Spellbook variant redundancy;
- a low-independent-signal dead-card-burden proxy;
- resilience and Blueprint recursion/recovery signals;
- immediate-win status as **test required**, never inferred from `infinite=true`;
- independent-usefulness structural signals per piece;
- provisional structural/outcome classification hints.

## Classification discipline

The script may identify a line as commander-native, commander-supported, commander-independent, or unlinked to a Blueprint combo win. It may also distinguish a Blueprint-designated win line from a line that still names an external payoff/enabler.

It **does not** decide `primary compact win`, `secondary win`, `backup`, `incidental infinite`, `value loop`, or `non-winning infinite`. Those are strategic judgments and remain `unresolved_requires_judgment` until the later judgment layer.

This is deliberate: Commander Spellbook's `infinite` flag is a fact about a loop, not proof that the loop immediately wins a multiplayer Commander game.

## First full build

Cycle 67.1 built all **62** deck records from the frozen development inputs:

- **418** cached Spellbook lines;
- **369** marked infinite by Spellbook;
- **349** linked to a Blueprint combo win condition;
- **78** lines containing a commander as a direct piece;
- **205** provisional commander-independent Blueprint-win hints.

All **418** priority/classification decisions remain unresolved by design.

The large number of commander-independent hints is *not* a finding that those packages should remain in their decks. It is exactly the population Step B's `power_core` materiality overlay and later Commander-first judgment must scrutinize.

## Worked example: Abaddon

Abaddon's cached Breach lines demonstrate why the vector model is necessary. The Blueprint explicitly says the Breach engine is commander-independent, while its Brain Freeze lines name Wheel of Fortune / Windfall as external finishers. The model therefore records:

- compact Spellbook piece count;
- commander-independent structural relationship;
- Blueprint win linkage;
- external-payoff requirement;
- tutor/recovery/redundancy signals;
- `immediate_win: test_required` rather than treating the infinite loop as an automatic win.

That is strictly more informative than the old binary `combo exists` treatment without pretending to know more than the source evidence supports.

## Commands

```text
python3 scripts/grixis_combo_quality.py --build
python3 scripts/grixis_combo_quality.py --check
python3 scripts/grixis_combo_quality.py --summary
python3 scripts/grixis_combo_quality.py --show abaddon-the-despoiler 1368-3518-4856
```
