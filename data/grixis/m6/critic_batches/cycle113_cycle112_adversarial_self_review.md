# Cycle 113 — Three new commander-first reviews and skeptical Cycle 112 reassessment

**Source/authority:** protected original 100-card decks in `corymstover/grixis-commander-encyclopediaGPT`, locked. Data here is **author-side review**, **not** independent formal Pass C/I/J, complete balanced effect-aware Phase B, a zero-improvement certificate, or user-approved swaps. Initial preregistration: `data/grixis/m6/phase_b_plans/cycle113_commander_reviews_01.json`, commit `c328868990756c19718cfc0545f259cd9ae58944`.

Full machine-auditable text: `data/grixis/m6/author_reviews/cycle113_three_commander_review_01.json`. Verification receipts: `data/grixis/m6/phase_b_bounded/cycle113_sourced_review_validation_01.json`.

## Kefka — Hullbreaker Horror for Orcish Bowmasters: HOLD

Kefka's cEDH deck does not merely want any spell-based combo. It is engineered to use the front face's ETB/attack hand disruption, card-type-diverse draw, Anger/Arena of Glory haste, clones, Displacer Kitten and Harmonic Prodigy to produce repeated Kefka triggers while retaining fast Oracle/Breach fallback wins.

Hullbreaker Horror is a seven-mana creature with useful spell-cast bounce triggers. Its claimed extra Spellbook combos can matter in some shells, but the candidate packet has not demonstrated a sufficiently fast and legal **Kefka-centered** line. Orcish Bowmasters instead costs two mana, has flash and punishes opponents drawing extra cards, synergizing with the existing wheel turns and early cEDH interaction. Kefka's discard-draw measures the **distinct card types** among cards discarded from its trigger, not raw quantity, so Hullbreaker does not automatically improve that engine.

**Judgment:** preserve Bowmasters. Do not add Hullbreaker on the strength of a generic infinite-combo tag or M5's exploratory test-pass.

Approved raw list SHA-256: `cd36192fedda7a4f54570fb8b8e4605147b40f9254e6985729097fc998f17b03`. M5 proposal: `swap:kefka-court-mage:m5:576cc2cc3744`.

## Sauron, Lord of the Rings — Aggravated Assault for Mystic Remora: HOLD

Sauron's eight-mana defining ability triggers **on casting Sauron**, then amasses Orcs 5, mills five and reanimates a creature from the graveyard. It is not an attack trigger: an extra combat does not repeat this process. The deck prioritizes Entomb/Buried Alive setup, mana and one of several high-impact reanimation targets.

Aggravated Assault can be effective when there are attack-ready threats and enough mana to pay its sorcery-speed five-mana activation for repeated combats, but that payoff is **conditional**, not a demonstrated Sauron loop in this exact 100. Replacing one-mana Mystic Remora deprives an expensive commander build of potentially early draw to find mana, setup and reanimation. The M5 claim of a Spellbook combo does not verify its required other pieces are in this list or that the line improves this commander's natural game.

**Judgment:** preserve Remora and the cast-trigger reanimator identity. Four Nazgûl are permitted by Nazgûl's official card-specific nine-copy permission; this is documented in the project's exception registry but is not a banned-card legalization.

Approved raw list SHA-256: `72a814e6ae1153507c9c1469a7792043b2e5c055d9e5fcd9f6cfcf7781e287b0`. M5 proposal: `swap:sauron-lord-of-the-rings:m5:31ef2948da79`.

## Nathan Drake — Godo, Bandit Warlord for Vampiric Tutor: HOLD

Nathan's primary benefit is an **on-attack** top-card heist from each library, granting one spell cast from the revealed collection. The deck protects and accelerates Nathan to attack repeatedly, with Roaming Throne, firebending, Karlach and Fire Lord Azula supporting the combat-theft package. It deliberately is not a generic Oracle/Breach cEDH deck.

Godo's six-mana Equipment search is real; its first-attack trigger untaps **Godo and Samurai**, then produces another combat. Nathan is Human Rogue, so he is *not* untapped by Godo. A second combat can grant another Nathan heist only when a separate effect or vigilance readies Nathan. Although Godo can retrieve limited Equipment, it does not replicate Vampiric Tutor's unrestricted one-mana instant library search and selection of protection, haste or theft engines. Godo's own bonus combat can be powerful for Godo; that does not establish a second commander heist.

**Judgment:** preserve Vampiric Tutor. The exact approved list contains Lightning Greaves, Swiftfoot Boots, Brotherhood Regalia and Dream-Thief's Bandana as potential Equipment hits, but the opportunity cost and timing are not equivalent to unrestricted tutoring.

Approved raw list SHA-256: `a5d59afc3a78d7ff6454b1d011c82c2f732e11f4d4dd03256df1195a3abe9ba0`. M5 proposal: `swap:nathan-drake-treasure-hunter:m5:79373d803b78`.

## Adversarial retrospective on Cycle 112 (authored, not independent)

**Cormela:** retain the HOLD for Archaeomancer replacing Faithless Looting. However, do not state categorically that Archaeomancer can never matter: it might be reanimated or cloned in actual spell recursion loops. The unproven point is the access/tempo improvement versus a one-mana discard-based graveyard setup and Cormela's restricted instant/sorcery mana.

**Ashnod:** retain the HOLD for Detective's Satchel replacing Dockside Chef. Both are genuine artifact-sacrifice enablers; Satchel-produced Clues themselves can have the activated sacrifice draw copied by Ashnod, but Satchel's own Thopter-production tap ability has no sacrifice activation cost. Avoid dismissing Satchel as having no synergy; the question is whether removing a cheap reusable creature/artifact sacrifice outlet is worth the expensive Clues and Thopter flexibility.

**Gwendlyn (important correction of emphasis):** Aphetto Alchemist + Illusionist's Bracers is an established repeatable-untap two-card engine: with Bracers equipped to Alchemist and Alchemist able to tap, activate targeting itself and have Bracers' copy untap a separate creature/artifact, including Gwendlyn. Each resolution untaps Alchemist for another round. Gwendlyn can then tap repeatedly on **your turn** to force random discard while opponents hold cards, assuming legal targeting, Gwendlyn no longer summoning sick, and no shroud preventing Alchemist targeting her. This is **arbitrarily many untaps**, not necessarily infinite discards, because hand sizes are finite. Moving Bracers off Gwendlyn forfeits simultaneous copying of Gwendlyn's discard ability, and losing Opposition Agent's flash search denial could reduce protection against combo tables. Cycle 112's candidate label `PROMISING_UNRESOLVED` is consistent but should be escalated from generic synergy to a **verified two-card repeatable untap engine needing payoff and opposing-tutor tradeoff**. This is a retrospective author finding, **not independently reviewed**.

An outside combo-reference cross-check corroborates the Aphetto/Bracers repeatable untap sequence; the primary authority for final Magic rules remains official Oracle and game rules, not a community combo summary.

## Completion gates

No changes to the existing 62 APPROVED/LOCKED lists. These are three substantive *candidate-specific holds* and a Cycle112 reassessment, not per-deck no-improvement certificates across every candidate or full M6 acceptance.

**Next:** organize independent criticism of the exact six author's assessments; test one bounded Gwendlyn Bracers/Alchemist activation-vs-Opposition-Agent value scenario if it can be executed without a large unbounded simulator build; then proceed to diverse next-commanders. Every finalized deck would still require current official legality, complete 100-card Oracle/singleton/identity checks and explicit owner approval for any proposed change.
