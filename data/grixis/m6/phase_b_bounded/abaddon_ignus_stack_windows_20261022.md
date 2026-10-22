# Abaddon — eight Oracle-correct Grinning Ignus disruption windows

**M6.6 targeted Phase B evidence; not a full opponent metagame or a deck certificate.** Registered *before* implementation at commit `1ba376c066569e4e0ab3d8d4ad11a3073aacd67c`. Frozen 99 cards + one command-zone Abaddon, approved SHA-256 `2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf`; unapplied `+Grinning Ignus/-Rakdos, Lord of Riots` used only as a single-slot, 100-card conditional fixture. **Canonical deck remains locked and unchanged.**

## Critical Oracle correction (higher priority than win-rate estimates)

**Grinning Ignus's return ability is a MANA ABILITY.** Despite the “activate only as a sorcery” timing restriction, it does not use the stack and **opponents cannot respond to its activation**. Under a quiet post-resolution battlefield and during your main phase with priority and no other triggers pending, its controller can pay one red and immediately return Ignus to hand without opening a removal window. Prior Abaddon experimental documentation must not depict this activation as an ordinary stack object an opponent can interrupt. Opponents instead must stop Ignus before the spell resolves, or act when a genuine priority window exists (e.g., another effect triggers when Ignus enters).

Primary authority: [Wizards Time Spiral Remastered release notes, Grinning Ignus](https://magic.wizards.com/en/news/feature/time-spiral-remastered-release-notes-2021-03-23). Separate **Birgi** front-face spell-cast mana-producing trigger **does use the stack**; removing Birgi after that trigger exists does not cancel the existing trigger, but prevents later ones.

## Adversarial fixtures

Unlike the 20,000 trajectories in PR #526, this study is a finite set of **eight deliberately prearranged conditional states**—zero frequency estimates. Every fixture draws the exact same candidate 99-card library and physically relocates existing Birgi, Ignus, a legal `{U}`/`{B}`/`{R}` or `{R}` land source, and a verified source of at least nine aggregate opponent life lost. A preexisting **Loyal Subordinate** combat-beginning trigger (three to each of three opponents while Abaddon is controlled, in the postcombat main) permits Ignus to be the *first spell* under Rule of Law; an already-resolved paid Boltwave instead consumes the one spell permitted by Rule of Law. Combat is assumed for the Loyal fixture, not simulated, and sources and opponent cards are never duplicated. The source-paid creature spell is cast from a physical hand. Every completed path passes real card-zone conservation, legal cascade exiling, and optional supported-hit resolution from PR #524.

| Response window | Legally meaningful outcome |
| --- | --- |
| Uncontested | Birgi and Abaddon present; source-paid Ignus bounce/recasts repeatedly in a conditional controlled state |
| Rule of Law, Boltwave already cast | Initial Ignus is itself forbidden as a second spell, not merely its cascade hit |
| Rule of Law, Ignus first spell | Ignus can be cast if a non-spell source supplied opponent loss; cascade triggers/exiles but free exile hit cannot be cast, and further Ignus hand casts are forbidden |
| Drannith Magistrate | Hand Ignus still casts and may be repeatedly recast; cascade trigger/exile still happens but **casts from exile fail**, so hit bottoms |
| Abaddon removed before subsequent hand cast | Previously created cascade trigger remains; subsequent Ignus hand casts don't gain cascade if Abaddon no longer grants it |
| Birgi removed before subsequent hand cast | Previous Birgi trigger is not undone; without new triggers, physically available red usually permits fewer recasts |
| Original Ignus spell countered | Abaddon and Birgi cast triggers survive countering the source Ignus spell. Ignus itself ends in physical graveyard and cannot bounce |
| Quiet board after Ignus resolves | Active player can activate Ignus's return mana ability immediately when priority/normal sorcery activation timing is satisfied; removal cannot respond to the activation itself |

The existing `scripts/grixis_m6_abaddon_ignus_shared_effects.py` functions gain **opt-in**, default-false Rule of Law and Drannith casting restrictions for the already-implemented real cascade exiling. Original no-hate trajectories are unchanged. Rule of Law forbids a second own spell even if the first was countered. Neither Rule of Law nor Drannith stops the original cascade **trigger**; each stops the free spell cast for the specified reason. Under these conditions, the exiled hit is returned to the bottom rather than illegally casting it.

The response cases do **not** sample opponent mana, opponent decklists, counterspell rates, combat choices, the likelihood of a quiet Ignus resolution, or win outcomes. Other triggered abilities entering the stack at Ignus resolution can change the timing; do not overgeneralize the quiet-board window. The original 99-card source and all 62 canonical APPROVED/LOCKED records remain untouched, with M6.6/M6.7 still PARTIAL and M7 new approvals zero.

## Oracle and rules sources

- [Wizards, Time Spiral Remastered: Grinning Ignus mana ability and priority](https://magic.wizards.com/en/news/feature/time-spiral-remastered-release-notes-2021-03-23)
- [Wizards, Double Masters 2022: cascade survives countering original spell](https://magic.wizards.com/en/news/feature/double-masters-2022-release-notes-2022-06-24)
- [Wizards, Core Set 2020: Rule of Law counts all spells cast](https://www.magic.wizards.com/en/news/feature/core-set-2020-release-notes-2019-06-25)
- [Wizards, Avatar: The Last Airbender release notes: Drannith Magistrate](https://magic.wizards.com/en/news/feature/avatar-the-last-airbender-release-notes)
