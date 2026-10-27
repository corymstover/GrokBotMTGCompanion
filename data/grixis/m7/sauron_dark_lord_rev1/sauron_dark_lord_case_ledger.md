# Deck 50 — M7 Rev1 case-level M6/I-J transfer ledger

Date: 2026-10-27. Research stage only; no M6, M7 or M8 certification.

- Baseline canonical raw SHA-256: `fab194f69a6e15b83679c1419f88ba6fdd56cd9527946cb94a6d8efe23a7dfc8`.
- Candidate raw SHA-256: `266660c6a3241c07a052da7624366be1f9617cb5db4c35c422b0e8f828977d9b`.
- Source blueprint: `data/grixis/m6/test_blueprints/Sauron__the_Dark_Lord.json`, 15 designed cases (P0 5 and P1 10). *All* original cases were recorded there as `DESIGN_ONLY_UNIMPLEMENTED_NOT_RUN`.
- Prior M6 I/J receipt: `data/grixis/m6/ij/input_receipts/sauron-the-dark-lord.json`, stage `M6_IJ_input_receipt`, downstream **incomplete**. It attests source inputs/hashes, NOT Phase B replay, actual model evaluation or complete candidate acceptance.
- New source-bound finite assertion suite: `sauron_dark_lord_verify.py` executed on the current physical 100, local PASS and GitHub exact-head CI as recorded in PR #731. This is a lightweight card-state model, **not** a Magic comprehensive rules engine and not an independent reviewer.

| Case | P | Preliminary new evidence / changed-card impact | Still required for formal M6 certification |
|---|---|---|---|
| C1 commander | P0 | Sauron's opponent CAST, Army player combat-damage and optional discard/draw triggers represented; neither Sauron identity nor name changed | Execute source-paid entire spell/trigger stack in a rules-faithful fixture with negative zones/countered spells |
| K1 ward legendary | P0 | Positive legendary creature/artifact sacrifice and no-permanent negative controls | Model targeting, ward-stack payment choices and untargeted sweeper |
| K2 amass on cast | P0 | One opponent spell countered still yields one amass; own casts produce none; Throne Avatar yields two | Stack order and changing Army creature objects after removal |
| K3 Mauhúr replacement | P0 | One counter per counter-placement event, not one per individual counter | Real zone/counter ledger with prior Army status |
| F1 compact win | P0 | Source-specific source-bound critique rejects unsupported deterministic compact wins; no automatic Breach/Oracle loop added | Exhaust relevant payable line candidates rather than treat the negative unit assertion as proof of absence |
| K4 The Great Goblin | P1 | One trigger per eligible counter event; amount increased by Mauhúr not extra trigger | Full positive/negative controller/event targets including no Army present |
| K5 Roaming Throne | P1 | Avatar versus Wraith choice yields mutually exclusive trigger doubling | Actual two separate tempt/hand-discard stacks with response windows |
| K6 seven Nazgûl | P1 | Seven legal copies; event wave and Sauron optional draw paths | Oracle card-name construction check (live CI) + token and replacement wave fixtures |
| K7 Minas Morgul | P1 | Army retains Army/Orc and gains Wraith under shadow counter | Pay {3}{B} and tap land; shadow evasion with actual blockers |
| E1 opponent-spell amass | P1 | Opponent casts, not resolving spell, drives Sauron | Three-opponent cast-turn ordering and priority |
| E2 Ring draw | P1 | Optional discard hand and only then draw 4 modeled | Multiple simultaneous Nazgûl/Throne triggers and changing hand |
| W1 Army combat | P1 | Only actual combat damage to a PLAYER by Army tempts; blocked and noncombat damage negative controls | Attacking/blocked/shadow/flying/trample state and lethal accounting |
| W2 The Great Goblin | P1 | Per event, not per counter, asserted | Opponent life/target damage and loss/prevention handling |
| F2 quiet opponents | P1 | Zero opponent casts yields no commander amass, Call/Nazgûl still relevant | Real 2-3-turn adversarial low-spell fixture |
| F3 sweepers | P1 | Loss of Ozolith noted; Army token disappears after destruction | Actual mass-removal resolution and recovery next turn |

## Exact candidate changed-card follow-through

- **Arcane Adaptation:** choosing Wraith affects all controlled creatures, including Orc Army, so the Nazgûl pump applies to Army only while Adaptation survives. Removing Adaptation in response can eliminate type before the trigger resolves. It does **not** itself trigger Ring temptation.
- **Lord of the Nazgûl:** creates Wraith tokens on *our* instant/sorcery spells, not opponents' casts. The nine-Wraith bonus requires controlling the threshold; no automatic nine Wraiths are assumed.
- **Bone Miser:** Sauron's one hand-discard choice creates one discard event per discarded card; Bone Miser's effects follow actual discarded card types. Sources cannot spend mana from a later trigger to pay earlier costs.
- **Moonstone, Harsh Mistress:** discard-to-exile is optional, cards remain subject to normal playing costs and timing, and choosing exile eliminates those cards as ordinary graveyard reanimation targets.
- **Glint-Horn Buccaneer:** discards each deal 1 to EACH opponent if Buccaneer survives while triggers resolve; no burn if commander draw trigger is declined or no cards discarded.
- **Herald of Secret Streams:** an amass counter makes Army unblockable while Herald persists; no false unblockable claim after Herald removal, or on zero-counter bodies.
- **Lazotep Plating:** two mana produces hexproof for player and permanents and amass Zombie 1, but does not counter untargeted destruction/exile or save a creature from damage.
- **Birthday Escape/Soothing of Sméagol:** actual spell resolution creates one Ring temptation; Soothing needs a legal nontoken creature target and can be fizzled if the only target becomes illegal.
- **Cavern of Souls:** Avatar chosen supports Sauron uncounterability and colored casting. It cannot be treated as a universal UBR source for other card types.

## Fail-closed status and next bounded action

The new verifier covers exact card identities/structure and finite tabletop
interactions; current whole-name Scryfall check is performed in PR CI.
However, the historical I/J receipt explicitly lacks downstream replay
and qualified adjudication; the 15 blueprint P0/P1 cases need a **formal
source-payable case matrix** under their prescribed fixtures, not merely
the illustrative unit assertions. Until this correspondence is accepted
and the repository M7 decision gate passes, status is **RESEARCH_ONLY —
NOT OWNER PRESENTABLE / NOT APPROVED**. No canonical change, no copied
historical evidence, and no fabricated certification.
