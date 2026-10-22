# Abaddon — dated rules and Oracle source inventory for M6 J

Snapshot assembled 2026-10-22 (America/Chicago); reviewer and assembler: ChatGPT/OpenAI GPT-6, **not independent**.

## Primary comprehensive-rules baseline

- Wizards of the Coast, *Magic: The Gathering Comprehensive Rules*, rules effective **August 7, 2026**: https://media.wizards.com/2026/downloads/MagicCompRules%2020260807.pdf
- Wizards rules index for checking whether a newer edition supersedes the pinned text: https://magic.wizards.com/en/rules
- Wizards *Warhammer 40,000 Commander Release Notes* (cascade, Abaddon, Noise Marine and Warhammer-specific interactions): https://magic.wizards.com/en/news/feature/warhammer-40000-commander-release-notes-2022-09-19
- Wizards *Strixhaven School of Mages / Commander 2021 release notes* (storm, copies, Jeska rules as relevant): https://magic.wizards.com/en/news/feature/strixhaven-school-mages-and-commander-2021-edition-release-notes-2021-04-16
- Wizards *Secrets of Strixhaven release notes* (updated Jeska's Will timing and opponent hand-size clarification): https://magic.wizards.com/en/news/feature/secrets-of-strixhaven-release-notes
- Wizards *FINAL FANTASY* card release notes (Vivi's counters and once-per-turn mana ability): https://media.wizards.com/2025/downloads/FIN_Release_Notes_3O87RLY5EO/EN_FIN_Release_Notes_2025_1_15.pdf

## Full exact-name Oracle source

The permanent, source-bound 97 distinct-card snapshot is
`data/grixis/m6/oracle_snapshots/Abaddon_the_Despoiler_Scryfall_20261022.json`:

- Scryfall public card-collection responses, obtained and verified **2026-10-22T17:23:43.510224+00:00** in GitHub Actions run [39822223496](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/39822223496).
- Exact submitted names from five complete 100-card physical source lists, Oracle IDs and text, per-name Oracle text SHA-256, Grixis color identity and by-name official Commander legality.
- Captured output from merged PR #570; full archived copy merged via PR #571. The source 97-card response report SHA-256 was `3d0b5a7bac2d574a30fcc07ad022d0d25fef2f218e964b1adf1055d5cae5f4a0`. The committed reformatted record has a distinct file SHA-256 and must be bound separately.
- Canonical baseline physical raw SHA-256 `2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf`, logical `lh1:5a1e5e5bb86ba35d7dbf712fbc3a7d29c3e05a17569c05e8a11976321699b793`.
- Research selected candidate physical raw SHA-256 `1fabe1251a7868838365144bf0cb1ee903d394ed90ac146b2dd9cdd45683b7dd`, logical `lh1:4bb15eb5acc051871e7d818890f71705eb74f1281e933e73b0e77ff770be1efc`.

## Decision-critical rules interpretations covered by executed finite fixtures

1. Abaddon's opponents' actual aggregate life loss is tracked for the current own turn; a qualifying spell gains cascade only if **cast from hand** with printed mana value no greater than X. Exile-cast cascade hits do not inherit his cascade.
2. Cascade is a cast trigger independent of whether the originating spell resolves or is countered; printed and newly granted cascade instances each resolve. A zero-MV effect can exile the remaining library without an eligible lower-MV nonland hit.
3. A virtual spell copy is **not cast**. Magecraft additionally triggers when instant/sorcery spells are copied; cast-only 40K/Lost/Keeper/Prosper triggers do not count mere virtual copies. Mana value ignores a generic cost reducer.
4. Bloodletter replaces life **loss** on its controller's turn; Solphim modifies noncombat **damage to opponents**, not damage to their creatures or controller. Flame Rift hits all players, but caster loss is not opponent threshold.
5. Noise Marine's printed cascade cast resolves before its enters effect and counts as a cast for its single-target damage. Vivi gains counters from noncreature casts and its zero-mana mana ability is restricted to one activation during its controller's turn.
6. Delayed Blast Fireball's exile-cast damage is 5 to each opponent and their creatures versus 2 on normal hand-cast; exile cast cannot earn Abaddon hand cascade. Prosper prior end-step impulse authorizes an exact physical following-turn exile cast.
7. Jeska's Will chooses both modes when a commander is controlled at **cast**, independent of later commander removal; red mana depends on target opponent hand size at resolution, and exiled cards still require ordinary legal play costs and timing.
8. Nightscape Familiar's red/blue cost reduction removes only one generic even if a spell is both colors; it does not lower actual printed mana value for Abaddon cascade.

The associated actual named executions, file-level source snapshots, payable source costs, admitted unsupported effects and bounded adversarial conditions are separately indexed in
`data/grixis/m6/phase_b_plans/abaddon_p0_case_inventory_20261022.json`,
`data/grixis/m6/certification_preflight/abaddon_residual_70_decision_relevance_20261022.json` and
`data/grixis/m6/certification_preflight/Abaddon_M6_6_7_Gate_Adjudication_20261022.md`.

This inventory is a dated crosswalk, **not** a self-certifying game simulator, global optimality proof, evergreen legality guarantee, independent review or owner approval. Canonical source lists remain unchanged.
