# Inalla, Archmage Ritualist — independent ChatGPT M7 adversarial review (2026-10-24)

**RESEARCH_ONLY — BELOW THE MANDATORY FIVE-SWAP MINIMUM. NOT OWNER APPROVED. NOT CANONICAL.**

Deck #23 follows the 22 newly M7-locked decks. Cory has approved **Gwendlyn #22**, not a new Inalla M7 candidate. The historical October 14 Inalla 100-card artifact (raw `81333ac71d483b667af968bf2ab221e1fa0de6edd7c2395170d15786e5b15fa3`, **without** a final newline) and all prior locks remain untouched.

## Independent finding: the original Grok 0-swap review was overly categorical

GrokBot [PR #671](https://github.com/corymstover/GrokBotMTGCompanion/pull/671) correctly preserved owner consent but asserted reintroducing any October 14 cut was **forbidden**. Project governance instead permits a *clearly justified proposed reversal* for owner decision; it does **not** let research silently reverse the cut.

### Most serious potential upgrade

**+ Dualcaster Mage / − Kefka, Court Mage // Kefka, Ruler of Ruin** is a defensible commander-first reconsideration, **not yet approved**:

- Dualcaster is a Flash Wizard that copies any target instant/sorcery on ETB and can itself be copied via Inalla's Eminence for `{1}`.
- Already-retained `Saw in Half` + Dualcaster and `Essence Flux` + Dualcaster provide two additional saved Commander Spellbook combos (16 → 18), with exact interaction prerequisites. Neither is a fabricated Inalla-exclusive combo.
- The tested lands-only proxy reports RR available in 46.05% of 10-card states; Kefka's five-land threshold in 9.58%. They are different thresholds and not duel win rates or real cast probabilities because rocks, rituals and table interaction are excluded.
- **Material cost:** Cory explicitly cut Dualcaster on October 14. Kefka's enter/attack discard-and-draw ETB and the alternate legend-copy trigger are lost. Dualcaster asks for `{1}{R}{R}` and does not automatically win without spell and targets. This must be disclosed before any possible owner acceptance.

## New overlooked challenges and why none establishes five quality-positive substitutions

| Candidate | Potential gain | Why it does **not** yet justify changing canonical Inalla |
| --- | --- | --- |
| Pyroblast over Red Elemental Blast | Both cost `{R}`; Pyroblast can legally target a nonblue spell/permanent for storm/yard setup and only affects it if blue. | REB's narrower target requirement can resist redirection to nonblue targets, and both perform blue counter/removal job. Small context-dependent gain; EDHREC cEDH 36.6% Pyro vs 52.8% REB, which is not authority. |
| Gitaxian Probe over Ragavan | Zero mana at 2 life, one-card replacement, information before protected Spellseeker/Breach turn; one more cheap sorcery and graveyard card. | Loses turn-one Ragavan treasure/card advantage clock. Sample cEDH 24.6% Probe vs 67.6% Ragavan; opponent blockers and pod pace decide, and those outcomes were not measured. |
| Starting Town over Exotic Orchard | 5-color on early first-three turns, untapped and independent of opponents, pays life1 for colored. | Tapped when deployed after turn three, whereas Orchard often painless rainbow in multiplayer; not a clear land tempo upgrade. |
| Exhibition Tidecaller over Blood Pet | `{U}` Wizard with Inalla copy can self-mill 6 total per following instant/sorcery cast, fueling Breach in the same turn. | Requires extra `{1}` and spell; token ends this turn. Blood Pet enables Culling the Weak / Sacrifice burst and is a protected owner addition. |
| Molten Duplication over Final Fortune | With Dualcaster, can make an independent infinite copy line; can clone Spellseeker ETB; tokens don't re-trigger Eminence. | Dependent on unapproved Dualcaster and a starting creature/artifact; loses all-in extra-turn line. |
| Snap over Chain of Vapor | Rebuys Wizard for ETB and untaps up to two lands. | Snap cannot answer noncreature stax, while Chain is one-blue flexible nonland bounce and can save an attempted combo. |
| Phantasmal Image over Thundertrap Trainer | Copy existing Wizard, become Wizard and trigger Eminence, potentially duplicate Spellseeker triggers. | Needs another suitable creature, whereas Trainer's self-contained ETB top-four selection is high-hit and owner-selected. |
| Rain of Filth over Cabal Ritual | Short all-in burst from sacrificing lands. | Sacrifices future colored sources and loses an essential early ritual with threshold upside; not a generic improvement. |
| Defense Grid + Gifts Ungiven over Kefka + Blood Pet | Stack tax and graveyard tutor access. | Taxes own off-turn free interaction, adds four-mana / Game Changer tutor; loses deterministic black-sac burst. |

Other legacy proposals (Micromancer, Snapcaster Mage, Tishana's Tidebinder, The One Ring, Crystal Vein, Tarnished Citadel, Phyrexian Tower, Jeweled Amulet, Daze, Into the Flood Maw, Lightning variants, Vexing Bauble) remain below a proved cut threshold; see Grok's archived testing and the companion JSON. A card's prevalence is discovery evidence, never automatic replacement.

## Full-100 stress candidates committed for verification

1. **Two-swap challenge, NOT approval-ready:** +Dualcaster −Kefka; +Pyroblast −Red Elemental Blast; exact 100, 27 lands; raw SHA-256 `5d182d9b9814fde5e04ec0687d7245bf3cd29c31d200c70a13f76e72bb932aef`.
2. **Three-swap stress only, NOT approval-ready:** above plus +Gitaxian Probe −Ragavan; exact 100, 27 lands; raw SHA-256 `b3ce0a3f6943889dd2bdfb0221a6daed4e07b338e5c3c5026bf1da0bc4e0ca26`.

Both preserve the Spellseeker/Scholar/Finale, Bloodline/Ruthless and Oracle/Breach win engines, all other retained October 14 cards, the 18 Game Changers, UBR identity and Tainted Pact singleton. The candidate path strings and complete Oracle source checks are in the companion JSON and test. Baseline remains **100 physical / 100 distinct / 27 lands / Bracket 5 — cEDH**.

## Recommendation and blocker

**Do not advance to a Gwendlyn-style canonical approval yet.** One real owner-decision candidate (+Dualcaster) is defensible, Pyroblast is borderline, and Probe is strategic but not demonstrated to beat Ragavan. Five independent, material net-positive swaps have **not** survived audit. Upgrading anyway would manufacture card churn and violate the permanent M7 rule.

Next research, if revisited: opponent/hand-context modeled turbo comparisons or new commander-specific Wizard candidate with a well-defined deterministic payoff. Do not pay for Grok or rerun a broad Colab research pipeline for this normal deck update. These focused tests are finite mechanical assertions, not multiplayer win-rate claims. Preserve prior locked decks and historical owner decision unless Cory explicitly approves an exact future new 100.
