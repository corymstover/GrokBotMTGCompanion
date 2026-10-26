# Deck #37 — Mishra, Eminent One M7 Rev1

2026-10-26. **Engineering evidence only. NOT OWNER APPROVED.** Canonical 2026-10-15 source remains approved/locked and unchanged until Cory explicitly approves this exact candidate.

## Authority and immutable sources

- Current canonical source: `corymstover/grixis-commander-encyclopediaGPT/main/refinement/decklists/Mishra_Eminent_One_Approved_2026-10-15.txt`, exact raw SHA-256 `ca94785fa43094a0053aac5c87e517c9cfaafb34c3baf9b3eccb067a167dd1a0`.
- Historical source October15 whole-99 audit: `refinement/decisions/Mishra_Eminent_One_Whole_List_Audit_2026-10-15.csv`, historical complete decision closeout and rules verification. No historical approved file is overwritten.
- Staged candidate: `data/grixis/m7/candidate_lists/Mishra__Eminent_One_chatgpt_rev1.txt`. Exact 100-line raw SHA-256: `0fa7b00d9d74b208f3fd5783b30aa190c4e5b17e72ea64851f895315f05083a0` (UTF-8, trailing LF).
- Scryfall `/cards/collection` live 2026-10-26, 100/100 exact names, 100/100 Commander legal, 100/100 color identities within U/B/R, 100/100 Oracle IDs; source-bound normalized snapshot in `data/grixis/m7/oracle_snapshots/Mishra__Eminent_One_Rev1_Scryfall_20261026.json`. Wizards' current Commander ban list checked separately. 34 lands, 100 distinct, one commander, no project exceptions.

## Identity and role audit

Mishra is a **five-mana noncreature-artifact copier**, not generic Grixis combo. At the beginning of combat the Warform gets ETBs and activated abilities from a noncreature artifact, becomes a 4/4 hasty artifact creature, and is sacrificed at the next end step. We optimize *repeated Warform ETBs, end-step sacrifices, artifact triggers, token copying, artifact tutors and artifact-based finishes*.

The original 99-slot audit was a major 16-swap refinement. Its 34-land base, premium tutors/protection, engine copies, KCI recursion, and split of expensive and cheap artifact targets remain the baseline. This fresh M7 pass preserves Gonti's Aether Heart, Determined Iteration, Strionic Resonator, Lithoform Engine, Worldwalker Helm, Thousand-Year Elixir, Urza, Coveted Jewel, Portal to Phyrexia, Ichor Wellspring, Cryogen Relic, Prized Statue, Simulacrum Synthesizer, Esoteric Duplicator, Mindslaver and Brudiclad. The prior decision to remove generic Brain Freeze/Underworld Breach is not reversed.

**Key corrected interaction:** Simulacrum Synthesizer does not require a *nontoken* artifact. Mishra's Warform copies retain source mana value, so copying a noncreature artifact with MV 3 or more triggers Synthesizer. Cutting it would sacrifice a real commander payoff. Brudiclad can turn Map/Treasure/Servo tokens into copies of a high-value Warform and remains the distinct token-swarm finisher.

## Six selected changes — incremental value and actual loss

| Add | Cut | Decisive reason and downside |
|---|---|---|
| **Panharmonicon** | Smelting Vat | All artifact/creature ETBs trigger twice: high-impact Wellspring/Prized/Coveted/Portal/Heart payoffs. Together with Mishra + Heart, duplicated energy triggers reach eight each combat, another deterministic extra-turn enabler. Loses Vat's activated sacrifice/top-eight artifact deployment; Repurposing Bay, Arcum, Transmute, Whir and Engineer retain substantial tutoring. |
| **Roaming Throne** | The Mightstone and Weakstone | Choosing Human or Artificer makes Mishra trigger twice at each beginning of combat without ongoing mana payments. Two Warform Heart entries give at least ten energy, another native infinite-turn route. Loses a five-mana real artifact that could be copied for two cards, -5/-5, or 2 restricted mana; other copied ETB draw/removal engines remain. |
| **Idol of Oblivion** | Uthros Research Craft | Once Mishra creates a token each turn, original Idol can tap to draw; a hasty Warform copy of Idol can also tap to draw that turn. Costs two to deploy with no station setup. Loses Uthros's many-artifact-spell cast-draw ceiling once stationed; Idol is capped by the number of available activations. |
| **Lightning Greaves** | Padeem, Consul of Innovation | Protects the five-mana commander directly with shroud and equip zero; Padeem protected artifacts but *not Mishra* and drew conditionally at upkeep. Loss: artifacts lose blanket hexproof, and shroud on equipped Mishra prevents targeting him with own spells or equip effects until Greaves move. |
| **Grinding Station** | Lich's Relic | A two-mana searchable artifact sacrifices an expendable Warform on demand, untaps on artifact entry, supplies repeatable self-mill for Welder/Emry and a bounded mill outlet for actual repeatable artifact-token loops. Loses Lich's Relic's powerful pay-two, per-opponent creature/planeswalker removal on Warform ETB. This is the sharpest removal-versus-finisher tradeoff. |
| **Marionette Apprentice** | Enthusiastic Mechanaut | Two-mana death payoff that drains **each** opponent whenever Warforms or other artifacts go from battlefield to graveyard, and provides a Servo via fabricate. Connects KCI/Helm sacrifice lines to a multiplayer finish. Loses an artifact-cost reduction and a flying body; Etherium Sculptor, fast mana and artifact tutors remain. |

## Rules and adversarial checks

1. Original Gonti's Aether Heart plus first Warform Heart each triggers on the token entering. Panharmonicon makes each trigger twice: `2 Hearts × 2 triggers × 2 energy = 8`. The token Heart can be exiled to pay eight for an extra turn, leaving the original source Heart on the battlefield for next combat.
2. Roaming Throne choosing Human/Artificer doubles **Mishra's** beginning-of-combat trigger, not triggered abilities of noncreature artifacts. First Heart Warform yields four energy; second yields six, totaling ten. This is not a claim that Roaming Throne doubles every noncreature ETB.
3. Worldwalker Helm + Urza + Thousand-Year Elixir is preserved. Additional untapped Maps from Helm can pay the repeated `{1}{U}` token-copy cost via Urza's artifact-tapping ability. The Warform copy does not inherit temporary granted haste, so the Elixir is still essential for the newly created hasty-*looking* (actually non-hasty) creature token's `{T}` copy ability. Grinding Station supplies a mill outlet but requires real artifacts per activation. Marionette Apprentice counts an artifact creature Warform dying **once**, not twice.
4. Idol can be activated only after a token was created that turn. Mishra creates the qualifying token; the original Idol and its Warform may each activate when untapped, since the Warform has haste. No unconditional double draw from a lone Idol before Mishra arrives.
5. Braids, Arisen Nightmare was challenged against Brudiclad as a seventh swap. Opponents may sacrifice *either* a creature *or* artifact when Warform is sacrificed, reducing Braids's draw reliability; losing Brudiclad also removes the unique whole-token conversion finisher. Rejected.
6. Copy Artifact was challenged against Mindslaver as another seventh swap. A cheap redundant artifact copy is attractive, but it replaces a premium copied activated ability with recurring opponent-turn control; not selected.
7. Memory Jar would turn Warforms into repeatable temporary seven-card hands, but opponents receive a fresh hand and instant-speed interaction too. Coveted Jewel's copied draw-three and mana stay with us. Bolas's Citadel improves generic Top/Aetherflux combo but needs BBB in an artifact/Workshop-heavy manabase, and copying it supplies no ETB. These are researched alternatives, not assumed superior.
8. Curated Commander EDHREC includes Idol, Panharmonicon, Roaming Throne and other synergies; inclusion is used only for discovery, not as optimization proof. The live Scryfall Oracle receipts and Wizards rule notes control mechanical claims. No randomized gameplay win rate or full multiplayer simulator is asserted.

## Quality-based stop

Six is an outcome, not a target. We challenged ten+ material candidates, the six chosen cuts plus extra retained targets Brudiclad, Mindslaver, Master Transmuter and Coveted Jewel; compared alternative seventh swaps and a generic Citadel variant. Additional substitutions would dilute Mishra's best existing Warform targets, remove protected deterministic engines, increase black pip demands, or swap away token-swarm finishing for effects opponents can cheaply neutralize. The selected list retains 34 lands, commander-native extra-turn lines, all critical KCI/Top/Helm pieces, substantial board interaction and artifact-specific tutoring. Biggest unanswered cost is swapping Lich's Relic removal for Station; one-way strategic judgment, not measured win-rate improvement.

Power Bracket: **4 — Optimized**. Archidekt tags: **Artifacts / Warform Tokens / Combo**.

**Status: engineering candidate only.** Gate and exact-head Actions evidence are required before requesting one owner approval; canonical locking follows only that approval.
