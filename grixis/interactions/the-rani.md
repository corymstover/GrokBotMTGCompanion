---
title: "The Rani — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# The Rani — Interaction Review

> Bot cycle 56 · batch F · reviewed 2026-10-16. Deck: [The Rani](../decks/the-rani.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-16), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/source-baseline/the-rani.txt`](../../exports/grixis-archidekt/source-baseline/the-rani.txt) · SHA-256 `4f0bccdd5201b57b7a57ced76afbd62d97bc3db7ca2bac08694b37abf25b98c7` |
| Rulings | **6** (5 verified · 0 uncertain · 1 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-16 · rulings 2026-10-15 |
| Source attestations | [`The_Rani_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/the_rani_2026-10-15/gate_output/The_Rani_Rules_Attestation.json) (Rules attestation (11 items, all PASS) re-verified) · [`The_Rani_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/The_Rani_Approval_Ready_Verification_2026-10-15.md) (Approval-ready verification (delta already in canonical baseline)) |

## Contents
- [Summary](#summary)
- [Flags and open questions](#flags-and-open-questions)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Engines and payoffs](#engines-and-payoffs)
- [Key card-pair interactions](#key-card-pair-interactions)
- [Replacement and prevention effects](#replacement-and-prevention-effects)
- [Zones, commander tax and the command zone](#zones-commander-tax-and-the-command-zone)
- [Legality and project exceptions](#legality-and-project-exceptions)
- [Rules cited](#rules-cited)

## Summary

The Rani makes Mark of the Rani Aura tokens (+2/+2, goaded) when she enters and attacks, and investigates whenever any goaded creature hits one of your opponents. The deck adds more goad (Impetus Auras, Baeloth, The Master, Disrupt Decorum, Bloodthirsty Blade) and multiplies Clues (Academy Manufactor, Erdwal Illuminator) into Time Sieve turns. The canonical list is the source baseline, which already contains the approval-ready delta. No Spellbook lines; all 11 attestation items are re-verified.

Rules surprises: any goaded creature counts, including opponents goaded by others hitting each other; Mark goad lasts as long as the Mark, not until your next turn; Manufactor's extra Clues don't count as investigating. One documentation flag (the Force of Will pitch count is 23, not 28). No list errors.

## Flags and open questions

Input for later refinement. **No decklist was changed in this phase.**

| # | Status | Interaction | Note |
|---|---|---|---|
| [rani-06](#rani-06-force-of-will-pitch-pool-is-23-blue-nonland-cards-not-28) | 🚩 list flag (documentation) | Force of Will pitch pool is 23 blue nonland cards, not 28 | Source says 28 other blue nonland cards for Force of Will; the canonical list has 23. |

## Commander rules text and edge cases

### rani-01: Mark of the Rani: a targeted trigger makes an Aura token; investigate on ANY goaded creature hitting your opponents

**Status:** ✅ verified · **Evidence:** fact · **Cards:** The Rani

**Ruling.** The Rani's enter and attack trigger targets another creature. If that target is illegal on resolution, no Mark is made. The Mark is an Aura token that enters attached, so it's never cast. It gives +2/+2 and goads for as long as it stays attached, not just until your next turn.

The investigate trigger doesn't care who goaded the creature or who controls it. It fires when any goaded creature, yours or an opponent's, deals combat damage to one of your opponents. That includes opponents' goaded creatures hitting each other.

**Citations**

- Oracle, *The Rani*: “Whenever The Rani enters or attacks, create a red Aura enchantment token named Mark of the Rani attached to another target creature. That token has enchant creature and "Enchanted creature gets +2/+2 and is goaded."”
- Oracle, *The Rani*: “Whenever a goaded creature deals combat damage to one of your opponents, investigate.”
- [CR 701.15b](#cr-70115b), [CR 701.16a](#cr-70116a)
- Source (re-verified): [`The_Rani_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/the_rani_2026-10-15/gate_output/The_Rani_Rules_Attestation.json) → “Rani Mark trigger and target”
- Source (re-verified): [`The_Rani_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/the_rani_2026-10-15/gate_output/The_Rani_Rules_Attestation.json) → “Own-creature Mark and goad”

## Engines and payoffs

### rani-05: Incriminating Impetus: suspected and goaded

**Status:** ✅ verified · **Evidence:** fact · **Cards:** The Rani, Incriminating Impetus

**Ruling.** Incriminating Impetus suspects the creature when it enters, giving it menace and "can't block" for as long as it's suspected. It also gives +2/+2 and goads it. The forced attacker is harder to block, so it's more likely to connect for a Rani Clue. The creature stays suspected even if the Aura is later removed.

**Citations**

- Scryfall ruling, *Incriminating Impetus*: “When an effect suspects a creature, it becomes suspected. It gains menace and "This creature can't block" for as long as it's suspected. It stays suspected until it leaves the battlefield or another effect causes it to no longer be suspected.”
- [CR 701.60a](#cr-70160a), [CR 701.15b](#cr-70115b)
- Source (re-verified): [`The_Rani_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/the_rani_2026-10-15/gate_output/The_Rani_Rules_Attestation.json) → “Incriminating Impetus”

## Key card-pair interactions

### rani-02: Marks on your own creatures: The Master, Mesmerist and Baeloth

**Status:** ✅ verified · **Evidence:** fact · **Cards:** The Rani, The Master, Mesmerist, Baeloth Barrityl, Entertainer

**Ruling.** A Mark can go on your own creature. It must attack each combat but can't attack you anyway, and it triggers The Rani when it connects with an opponent.
- **On The Master:** +2 power raises the cap for his skulk-and-goad tap. A creature he goads that connects triggers both The Rani's investigate and The Master's counter and draw.
- **On Baeloth:** +2 power goads more opposing creatures, for as long as his power stays high. Baeloth's goad is static, not "until your next turn", and being goaded himself doesn't turn it off.

**Citations**

- Oracle, *The Master, Mesmerist*: “Whenever a creature with skulk deals combat damage to one of your opponents, put a +1/+1 counter on The Master and draw a card.”
- Scryfall ruling, *Baeloth Barrityl, Entertainer*: “Unlike most similar effects, Baeloth Barrityl's first ability doesn't cause a creature to be goaded until your next turn. Rather, it causes it to be goaded for as long as Baeloth Barrityl is on battlefield, has the ability, and has sufficient power.”
- [CR 701.15b](#cr-70115b), [CR 702.118b](#cr-702118b)
- Source (re-verified): [`The_Rani_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/the_rani_2026-10-15/gate_output/The_Rani_Rules_Attestation.json) → “The Master Mesmerist plus Mark”
- Source (re-verified): [`The_Rani_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/the_rani_2026-10-15/gate_output/The_Rani_Rules_Attestation.json) → “Baeloth plus Mark”

## Replacement and prevention effects

### rani-04: Academy Manufactor + Erdwal Illuminator: two investigates, six tokens; Time Sieve

**Status:** ✅ verified · **Evidence:** fact · **Cards:** The Rani, Academy Manufactor, Erdwal Illuminator, Time Sieve

**Ruling.** Erdwal Illuminator adds a second investigate the first time you investigate each turn. Academy Manufactor turns each Clue into a Clue, a Food and a Treasure, so the first Rani investigate each turn makes six artifacts. Manufactor's extra Clues aren't investigating, so they don't trigger the Illuminator again. Time Sieve can sacrifice any five of those for an extra turn. That's a value engine, not a guaranteed loop, as the attestation correctly says.

**Citations**

- Oracle, *Erdwal Illuminator*: “Whenever you investigate for the first time each turn, investigate an additional time.”
- Oracle, *Time Sieve*: “{T}, Sacrifice five artifacts: Take an extra turn after this one.”
- Scryfall ruling, *Academy Manufactor*: “If you control one Academy Manufactor and would create some number of Clue, Food, or Treasure tokens, you will instead create that many Clue tokens, that many Food tokens, and that many Treasure tokens.”
- [CR 614.1a](#cr-6141a), [CR 701.16a](#cr-70116a)
- Source (re-verified): [`The_Rani_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/the_rani_2026-10-15/gate_output/The_Rani_Rules_Attestation.json) → “Academy Manufactor plus investigate”
- Source (re-verified): [`The_Rani_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/the_rani_2026-10-15/gate_output/The_Rani_Rules_Attestation.json) → “Erdwal Illuminator plus Manufactor”
- Source (re-verified): [`The_Rani_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/the_rani_2026-10-15/gate_output/The_Rani_Rules_Attestation.json) → “Time Sieve”

## Zones, commander tax and the command zone

### rani-03: Blinking The Rani: Thassa and Displacer Kitten make new Marks; old Marks stay

**Status:** ✅ verified · **Evidence:** fact · **Cards:** The Rani, Thassa, Deep-Dwelling, Displacer Kitten

**Ruling.** Thassa's end-step blink or Displacer Kitten's blink on each noncreature spell returns The Rani as a new object, so her enter trigger makes another Mark. Marks already attached to other creatures don't depend on the old Rani and stay. Kitten returns the card under its owner's control.

**Citations**

- Oracle, *Displacer Kitten*: “Avoidance — Whenever you cast a noncreature spell, exile up to one target nonland permanent you control, then return that card to the battlefield under its owner's control.”
- Scryfall ruling, *Displacer Kitten*: “When the card returns to the battlefield, it will be a new object with no connection to the card that was exiled. Auras attached to the exiled creature will be put into their owners' graveyards. Any Equipment will become unattached and remain on the battlefield. Any counters on the exiled permanent will cease to exist.”
- [CR 400.7](#cr-4007), [CR 603.6a](#cr-6036a)
- Source (re-verified): [`The_Rani_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/the_rani_2026-10-15/gate_output/The_Rani_Rules_Attestation.json) → “Thassa blink”
- Source (re-verified): [`The_Rani_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/the_rani_2026-10-15/gate_output/The_Rani_Rules_Attestation.json) → “Displacer Kitten blink”

## Legality and project exceptions

### rani-06: Force of Will pitch pool is 23 blue nonland cards, not 28

**Status:** 🚩 list flag · **Evidence:** fact · **Cards:** The Rani, Force of Will

**Ruling.** The canonical list is the source baseline, and it already includes the approval-ready delta (Agitator Ant → The Master, Insurrection → Thassa, Counterspell → Force of Will). Counting it gives 23 other blue nonland cards in the 99 that could be exiled to pay for Force of Will. The Rani starts in the command zone and can't be pitched. The attestation and approval-ready file say 28. Force of Will still works; only the documented number is wrong.

**List flag (documentation).** Source says 28 other blue nonland cards for Force of Will; the canonical list has 23.

**Citations**

- Oracle, *Force of Will*: “You may pay 1 life and exile a blue card from your hand rather than pay this spell's mana cost.”
- Source (re-verified): [`The_Rani_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/the_rani_2026-10-15/gate_output/The_Rani_Rules_Attestation.json) → “Force of Will pitch support”
- Source (re-verified): [`The_Rani_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/The_Rani_Approval_Ready_Verification_2026-10-15.md) → “Force of Will blue-pitch pool: **28 other blue nonland cards**”

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 400.7

An object that moves from one zone to another becomes a new object with no memory of, or relation to, its previous existence. This rule has the following exceptions.

#### CR 603.6a

Enters-the-battlefield abilities trigger when a permanent enters the battlefield. These are written, “When [this object] enters, . . . “ or “Whenever a [type] enters, . . .” Each time an event puts one or more permanents onto the battlefield, all permanents on the battlefield (including the newcomers) are checked for any enters-the-battlefield triggers that match the event.

#### CR 614.1a

Effects that use the word “instead” are replacement effects. Most replacement effects use the word “instead” to indicate what events will be replaced with other events.

#### CR 701.15b

Goaded is a designation a permanent can have. A goaded creature attacks each combat if able and attacks a player other than the controller of the permanent, spell, or ability that caused it to be goaded if able. Goaded is neither an ability nor part of the permanent’s copiable values.

#### CR 701.16a

“Investigate” means “Create a Clue token.” See rule 111.10f.

#### CR 701.60a

Certain spells and abilities instruct a player to suspect a creature. That creature becomes suspected until it leaves the battlefield or until a spell or ability causes it to no longer be suspected.

#### CR 702.118b

A creature with skulk can’t be blocked by creatures with greater power. (See rule 509, “Declare Blockers Step.”)

