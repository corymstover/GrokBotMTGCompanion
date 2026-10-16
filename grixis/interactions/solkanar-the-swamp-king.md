---
title: "Sol'kanar the Swamp King — Interaction Review"
category: rules
tags: [grixis, interactions, rulings]
generated_by: scripts/grixis_interactions.py
sources: [cr, scryfall, grixis-repo]
schema: 2
---

# Sol'kanar the Swamp King — Interaction Review

> Bot cycle 54 · batch E · reviewed 2026-10-16. Deck: [Sol'kanar the Swamp King](../decks/solkanar-the-swamp-king.md) · method and format: [Interaction reviews](README.md). Every ruling below was checked against current Oracle text (Scryfall oracle bulk 2026-10-16), Scryfall rulings (bulk 2026-10-15) and the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25; quotes are verbatim and machine-verified by `scripts/grixis_interactions.py --check`. Source attestations from the archived source repo were re-verified, not copied.

| | |
|---|---|
| Canonical project list | [`exports/grixis-archidekt/source-baseline/solkanar-the-swamp-king.txt`](../../exports/grixis-archidekt/source-baseline/solkanar-the-swamp-king.txt) · SHA-256 `bf475d9c7048874d439972282b85de5684e0fde03095a2257e9249cdb7661ccd` |
| Rulings | **6** (6 verified · 0 uncertain · 0 flags) |
| CR / Oracle / rulings | CR 2026-09-25 · Oracle 2026-10-16 · rulings 2026-10-15 |
| Source attestations | [`Solkanar_the_Swamp_King_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/solkanar_swamp_king_2026-10-15/gate_output/Solkanar_the_Swamp_King_Rules_Attestation.json) (Rules attestation (14 items, all PASS) re-verified) · [`Solkanar_the_Swamp_King_Approval_Ready_Verification_2026-10-15.md`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Solkanar_the_Swamp_King_Approval_Ready_Verification_2026-10-15.md) (Approval-ready verification (delta already in canonical baseline)) |

## Contents
- [Summary](#summary)
- [Commander rules text and edge cases](#commander-rules-text-and-edge-cases)
- [Combos and engine lines](#combos-and-engine-lines)
- [Engines and payoffs](#engines-and-payoffs)
- [Layers and continuous effects](#layers-and-continuous-effects)
- [Rules cited](#rules-cited)

## Summary

Sol'kanar gains 1 life whenever any player casts a black spell, and Demon's Horn copies that. Painter's Servant naming black makes every spell black, and with Grindstone it mills forever. The life gains feed Exquisite Blood / Bloodthirsty Conqueror loops with Vito, Starscape Cleric, Blight-Priest or Tenacity, plus Top + Citadel + Sheoldred or Aetherflux. The canonical list is the source baseline and already contains the approval-ready delta (Withering Torment, The Soul Stone, Fell the Profane, Raucous Theater, Undercity Sewers). All 13 Spellbook lines and all 14 attestation items are re-verified.

Rules surprises: Sol'kanar ignores his own cast; black Painter's makes even a Top recast trigger him; Blanket of Night makes opponents' lands Swamps for swampwalk but doesn't double-count real Swamps. No list errors.

## Commander rules text and edge cases

### solkanar-01: Sol'kanar and Demon's Horn: any player's black spell gains life, one event per spell

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Sol'kanar the Swamp King, Demon's Horn, The Soul Stone, Withering Torment, Fell the Profane // Fell Mire

**Ruling.** Sol'kanar and Demon's Horn each trigger on every black spell any player casts. Each trigger resolves before the spell, as a separate 1-life gain, and it still gains life if the spell is countered. Sol'kanar doesn't trigger on his own cast.

On individual cards:
- The Soul Stone ({1}{B}) is a black spell when cast.
- Withering Torment's 2 life loss doesn't happen if its target is gone, but the cast triggers still gained life.
- Fell the Profane cast as the spell face triggers both. Playing Fell Mire as a land triggers neither.

**Citations**

- Oracle, *Sol'kanar the Swamp King*: “Whenever a player casts a black spell, you gain 1 life.”
- Scryfall ruling, *Sol'kanar the Swamp King*: “Will not trigger off itself being cast.”
- Scryfall ruling, *Demon's Horn*: “The ability triggers whenever any player, not just you, casts a black spell.”
- Scryfall ruling, *Withering Torment*: “If the target creature or enchantment is an illegal target as Withering Torment tries to resolve, it won't resolve and none of its effects will happen. You won't lose life.”
- [CR 105.2](#cr-1052), [CR 113.7a](#cr-1137a), [CR 712.12](#cr-71212)
- Source (re-verified): [`Solkanar_the_Swamp_King_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/solkanar_swamp_king_2026-10-15/gate_output/Solkanar_the_Swamp_King_Rules_Attestation.json) → “Sol'kanar black-spell trigger”
- Source (re-verified): [`Solkanar_the_Swamp_King_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/solkanar_swamp_king_2026-10-15/gate_output/Solkanar_the_Swamp_King_Rules_Attestation.json) → “Demon's Horn parallel trigger”
- Source (re-verified): [`Solkanar_the_Swamp_King_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/solkanar_swamp_king_2026-10-15/gate_output/Solkanar_the_Swamp_King_Rules_Attestation.json) → “The Soul Stone”
- Source (re-verified): [`Solkanar_the_Swamp_King_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/solkanar_swamp_king_2026-10-15/gate_output/Solkanar_the_Swamp_King_Rules_Attestation.json) → “Withering Torment”
- Source (re-verified): [`Solkanar_the_Swamp_King_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/solkanar_swamp_king_2026-10-15/gate_output/Solkanar_the_Swamp_King_Rules_Attestation.json) → “Fell the Profane // Fell Mire”

## Combos and engine lines

### solkanar-03: Exquisite Blood / Bloodthirsty Conqueror + a lifegain-to-loss payoff: infinite drain

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Sol'kanar the Swamp King, Exquisite Blood, Bloodthirsty Conqueror, Vito, Thorn of the Dusk Rose, Starscape Cleric, Marauding Blight-Priest, Enduring Tenacity, Aetherflux Reservoir

**Ruling.** Exquisite Blood or Bloodthirsty Conqueror gains life when an opponent loses life. Vito, Starscape Cleric, Marauding Blight-Priest or Enduring Tenacity makes an opponent lose life when you gain it. Any single gain or loss, such as one Sol'kanar trigger, then loops until the table is dead or someone breaks it. Aetherflux Reservoir with either enabler turns the gains into a 50-damage shot. All 10 Spellbook pairs are present. One limit: if you and an opponent lose life at the same time and you drop to 0, you lose before Exquisite Blood resolves.

**Citations**

- Oracle, *Exquisite Blood*: “Whenever an opponent loses life, you gain that much life.”
- Oracle, *Vito, Thorn of the Dusk Rose*: “Whenever you gain life, target opponent loses that much life.”
- Scryfall ruling, *Vito, Thorn of the Dusk Rose*: “If an ability triggers whenever an opponent loses life and causes you to gain life, such as the ability of Exquisite Blood, this will loop until either you win the game or a player takes an action to break the loop.”
- Scryfall ruling, *Exquisite Blood*: “If you and an opponent both lose life simultaneously, and this causes your life total to become 0 or less, you'll lose the game before Exquisite Blood's triggered ability can resolve.”
- [CR 119.3](#cr-1193), [CR 603.2](#cr-6032)
- Commander Spellbook [314-3966](https://commanderspellbook.com/combo/314-3966/) (community-maintained, retrieved 2026-10-16): “Vito triggers, causing an opponent to lose 1 life.”
- Commander Spellbook [5867-6191](https://commanderspellbook.com/combo/5867-6191/) (community-maintained, retrieved 2026-10-16): “Starscape Cleric triggers, causing each opponent to lose 1 life.”
- Source (re-verified): [`Solkanar_the_Swamp_King_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/solkanar_swamp_king_2026-10-15/gate_output/Solkanar_the_Swamp_King_Rules_Attestation.json) → “Exquisite Blood life loop”
- Source (re-verified): [`Solkanar_the_Swamp_King_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/solkanar_swamp_king_2026-10-15/gate_output/Solkanar_the_Swamp_King_Rules_Attestation.json) → “Repeated lifegain payoffs”

### solkanar-04: Sensei's Divining Top + Bolas's Citadel + Sheoldred or Aetherflux Reservoir

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Sol'kanar the Swamp King, Sensei's Divining Top, Bolas's Citadel, Sheoldred, the Apocalypse, Aetherflux Reservoir, K'rrik, Son of Yawgmoth

**Ruling.** Tap Top to draw and put it back on top of your library, then cast it with Citadel for 1 life.
- **With Sheoldred:** each draw gains 2, for a net +1 per loop and unlimited draws.
- **With Aetherflux:** each recast gains life equal to the spells cast this turn, toward the 50-life shot.
- **With black Painter's Servant:** Sol'kanar and Demon's Horn add more per Top cast.

Citadel still follows normal timing, but Top is an artifact you can recast any time you have priority with an empty stack in your main phase. K'rrik lets you pay 2 life for {B} in any cost, which the lifegain covers.

**Citations**

- Oracle, *Bolas's Citadel*: “You may play lands and cast spells from the top of your library. If you cast a spell this way, pay life equal to its mana value rather than pay its mana cost.”
- Scryfall ruling, *Bolas's Citadel*: “You must follow the normal timing permissions and restrictions of the cards you play from your library.”
- Scryfall ruling, *K'rrik, Son of Yawgmoth*: “K'rrik's ability lets you pay 2 life for {B} in any cost you pay, including the mana costs of spells, activation costs, and even costs for special actions (such as morph). Any time you pay mana, that's a cost.”
- [CR 601.2f](#cr-6012f), [CR 118.9](#cr-1189)
- Commander Spellbook [2173-2498-5078](https://commanderspellbook.com/combo/2173-2498-5078/) (community-maintained, retrieved 2026-10-16): “Cast Sensei's Divining Top from the top of your library by paying 1 life.”
- Commander Spellbook [2173-4740-5078](https://commanderspellbook.com/combo/2173-4740-5078/) (community-maintained, retrieved 2026-10-16): “Cast Sensei's Divining Top from the top of your library by paying 1 life.”
- Source (re-verified): [`Solkanar_the_Swamp_King_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/solkanar_swamp_king_2026-10-15/gate_output/Solkanar_the_Swamp_King_Rules_Attestation.json) → “K'rrik and Bolas's Citadel”

## Engines and payoffs

### solkanar-06: Secondary engines: Bontu's Monument, The Soul Stone, wheels into Sheoldred / Underworld Dreams

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Sol'kanar the Swamp King, Bontu's Monument, The Soul Stone, Wheel of Fortune, Windfall, Sheoldred, the Apocalypse, Underworld Dreams

**Ruling.** Bontu's Monument makes black creature spells cost {1} less and drains 1 per creature spell. Each drain is a separate gain and loss event for the loops. Harnessing The Soul Stone ({6}{B}, {T}, exile a creature you control) turns on an upkeep reanimation, but only on the battlefield. Wheel of Fortune and Windfall make opponents draw seven, which means seven Sheoldred or Underworld Dreams triggers each.

**Citations**

- Oracle, *The Soul Stone*: “∞ — At the beginning of your upkeep, return target creature card from your graveyard to the battlefield.”
- Oracle, *Bontu's Monument*: “Whenever you cast a creature spell, each opponent loses 1 life and you gain 1 life.”
- Scryfall ruling, *The Soul Stone*: “Until it is harnessed, The Soul Stone doesn't have the ability listed after the infinity symbol. It also doesn't have that ability in zones other than the battlefield.”
- [CR 701.64a](#cr-70164a)
- Source (re-verified): [`Solkanar_the_Swamp_King_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/solkanar_swamp_king_2026-10-15/gate_output/Solkanar_the_Swamp_King_Rules_Attestation.json) → “Bontu's Monument”
- Source (re-verified): [`Solkanar_the_Swamp_King_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/solkanar_swamp_king_2026-10-15/gate_output/Solkanar_the_Swamp_King_Rules_Attestation.json) → “Wheel pressure”

## Layers and continuous effects

### solkanar-02: Painter's Servant naming black: every spell is black, and Grindstone mills forever

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Sol'kanar the Swamp King, Painter's Servant, Grindstone, Demon's Horn, Sensei's Divining Top

**Ruling.** Painter's Servant naming black makes every card outside the battlefield, every spell and every permanent black in addition to its other colors. Previously colorless things become just black. Two results:
- Every spell any player casts triggers Sol'kanar and Demon's Horn, including colorless ones like a Sensei's Divining Top recast.
- Grindstone's two milled cards always share a color, so it repeats until the target's library is empty (Spellbook 1078-2302).

A later effect that sets an object's color overrides the Servant for that object.

**Citations**

- Oracle, *Painter's Servant*: “All cards that aren't on the battlefield, spells, and permanents are the chosen color in addition to their other colors.”
- Oracle, *Grindstone*: “{3}, {T}: Target player mills two cards. If two cards that share a color were milled this way, repeat this process.”
- Scryfall ruling, *Painter's Servant*: “This ability affects every card in every game zone, all tokens on the battlefield, and all spell copies on the stack, regardless of who controls or owns them.”
- Scryfall ruling, *Grindstone*: “If the two cards are both colorless, then the effect does not repeat. It only repeats if both cards have at least one color and at least one color is shared between them.”
- [CR 613.1e](#cr-6131e), [CR 105.3](#cr-1053)
- Commander Spellbook [1078-2302](https://commanderspellbook.com/combo/1078-2302/) (community-maintained, retrieved 2026-10-16): “Because both cards will share a color due to Painter's Servant, the process in step 1 repeats until the player has milled their entire library.”
- Source (re-verified): [`Solkanar_the_Swamp_King_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/solkanar_swamp_king_2026-10-15/gate_output/Solkanar_the_Swamp_King_Rules_Attestation.json) → “Painter's Servant naming black”
- Source (re-verified): [`Solkanar_the_Swamp_King_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/solkanar_swamp_king_2026-10-15/gate_output/Solkanar_the_Swamp_King_Rules_Attestation.json) → “Painter's Servant + Grindstone”

### solkanar-05: Blanket of Night / Urborg: every land is a Swamp (swampwalk, Coffers, Crypt Ghast)

**Status:** ✅ verified · **Evidence:** fact · **Cards:** Sol'kanar the Swamp King, Blanket of Night, Urborg, Tomb of Yawgmoth, Cabal Coffers, Crypt Ghast, Consuming Corruption, Raucous Theater, Undercity Sewers, Dread Presence

**Ruling.** Blanket of Night makes every land a Swamp, and Urborg makes every land a Swamp too. So opponents control Swamps, and Sol'kanar's swampwalk makes him unblockable. Your Swamp count for Cabal Coffers and Consuming Corruption counts every land, and Crypt Ghast doubles your Swamp mana. The lands don't gain the name Swamp, and real Swamps aren't counted twice. Raucous Theater and Undercity Sewers are real Swamps, so fetchlands can find them and they trigger Dread Presence. The change is symmetric, so opponents' lands also tap for {B}.

**Citations**

- Oracle, *Blanket of Night*: “Each land is a Swamp in addition to its other land types.”
- Scryfall ruling, *Blanket of Night*: “Anything which counts the number of Swamps on the battlefield will not double count an actual Swamp card while Blanket of Night is on the battlefield.”
- Scryfall ruling, *Blanket of Night*: “The lands do not get the name “Swamp” in addition to their current name. This is a reversal of older rulings.”
- [CR 205.1b](#cr-2051b), [CR 702.14c](#cr-70214c)
- Source (re-verified): [`Solkanar_the_Swamp_King_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/solkanar_swamp_king_2026-10-15/gate_output/Solkanar_the_Swamp_King_Rules_Attestation.json) → “Blanket of Night / Urborg”
- Source (re-verified): [`Solkanar_the_Swamp_King_Rules_Attestation.json`](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/solkanar_swamp_king_2026-10-15/gate_output/Solkanar_the_Swamp_King_Rules_Attestation.json) → “Typed surveil Swamps”

## Rules cited

Verbatim from the [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt) effective 2026-09-25 (long rules shortened with …).

#### CR 105.2

An object can be one or more of the five colors, or it can be no color at all. An object is the color or colors of the mana symbols in its mana cost, regardless of the color of its frame. An object’s color or colors may also be defined by a color indicator or a characteristic-defining ability. See rule 202.2.

#### CR 105.3

Effects may change an object’s color or give a color to a colorless object. If an effect gives an object a new color, the new color replaces all previous colors the object had (unless the effect said the object became that color “in addition” to its other colors). Effects may also make a colored object become colorless.

#### CR 113.7a

Once activated or triggered, an ability exists on the stack independently of its source. Destruction or removal of the source after that time won’t affect the ability. Note that some abilities cause a source to do something (for example, “This creature deals 1 damage to any target”) rather than the ability doing anything directly. In these cases, any activated or triggered ability that references information about the source for use while announcing an activated ability or putting a triggered ability on the stack checks that information when the ability is put onto the stack. Otherwise, it …

#### CR 118.9

Some spells have alternative costs. An alternative cost is a cost listed in a spell’s text, or applied to it from another effect, that its controller may pay rather than paying the spell’s mana cost. Alternative costs are usually phrased, “You may [action] rather than pay [this object’s] mana cost,” or “You may cast [this object] without paying its mana cost.” Note that some alternative costs are listed in keywords; see rule 702.

#### CR 119.3

If an effect causes a player to gain life or lose life, that player’s life total is adjusted accordingly.

#### CR 205.1b

Some effects change an object’s card type, supertype, or subtype but specify that the object retains a prior card type, supertype, or subtype. In such cases, all the object’s prior card types, supertypes, and subtypes are retained. This rule applies to effects that use phrases such as “in addition to its other types” or that state that something is “still a [type, supertype, or subtype].” Some effects state that an object becomes an “artifact creature”; these effects also allow the object to retain all of its prior card types and subtypes. Some effects state that an object becomes a …

#### CR 601.2f

The player determines the total cost of the spell. Usually this is just the mana cost. Some spells have additional or alternative costs. Some effects may increase or reduce the cost to pay, or may provide other alternative costs. Costs may include paying mana, tapping permanents, sacrificing permanents, discarding cards, and so on. The total cost is the mana cost or alternative cost (as determined in rule 601.2b), plus all additional costs and cost increases, and minus all cost reductions. If multiple cost reductions apply, the player may apply them in any order. If the mana component of the …

#### CR 603.2

Whenever a game event or game state matches a triggered ability’s trigger event, that ability automatically triggers. The ability doesn’t do anything at this point.

#### CR 613.1e

Layer 5: Color-changing effects are applied.

#### CR 701.64a

“Harness [this permanent]” means “If this permanent isn’t harnessed, it becomes harnessed.”

#### CR 702.14c

A creature with landwalk can’t be blocked as long as the defending player controls at least one land with the specified land type (as in “islandwalk”), with the specified type or supertype (as in “artifact landwalk”), without the specified type or supertype (as in “nonbasic landwalk”), or with both the specified type or supertype and the specified subtype (as in “snow swampwalk”). (See rule 509, “Declare Blockers Step.”)

#### CR 712.12

A player playing a modal double-faced card or a copy of a modal double-faced card as a land chooses one of its faces that’s a land before putting it onto the battlefield. It enters the battlefield with that face up. See rule 305, “Lands.”

