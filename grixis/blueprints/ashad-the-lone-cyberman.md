# Blueprint — Ashad, the Lone Cyberman

> **Commander Blueprint v1** (seeded, Bot cycle 50, 2026-10-16) for the canonical project list ([deck page](../decks/ashad-the-lone-cyberman.md), state `SOURCE_BASELINE`, list `lh1:6d87a5e4a87ac6dd…`). Machine-readable source: [`data/grixis/blueprints/ashad-the-lone-cyberman.json`](../../data/grixis/blueprints/ashad-the-lone-cyberman.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Ashad, the Lone Cyberman** — Legendary Artifact Creature — Cyberman

> The first nonlegendary artifact spell you cast each turn has casualty 2. (As you cast it, you may sacrifice a creature with power 2 or greater. When you do, copy it. A copy of an artifact spell becomes a token.)  
> Whenever you sacrifice another creature, put a +1/+1 counter on Ashad.

## Plan and commander role

- **Primary plan:** Artifact-copy value: make the first nonlegendary artifact spell each turn a two-for-one by sacrificing a power-2+ creature (often an artifact creature or token), growing Ashad with every sacrifice; flash artifacts extend 'first each turn' to opponents' turns. *strategic_judgment · high*
- **Secondary:** Artifact-sacrifice drains and recursion (Disciple of the Vault, Mayhem Devil, KCI, altars, Scrap Trawler, Goblin Welder), and the Urza + Worldwalker Helm + Artificer Class infinite.
  - Evidence: [Ashad_the_Lone_Cyberman_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Ashad_the_Lone_Cyberman_v1.md) · [Ashad_the_Lone_Cyberman_Approval_Ready_Closeout_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Ashad_the_Lone_Cyberman_Approval_Ready_Closeout_2026-10-13.md) · [ashad-01](../interactions/ashad-the-lone-cyberman.md#ashad-01-casualty-2-on-your-first-nonlegendary-artifact-spell) · [ashad-05](../interactions/ashad-the-lone-cyberman.md#ashad-05-urza--worldwalker-helm--artificer-class)
- **Commander role: significant.** Ashad copies one artifact spell per turn into a token and turns every sacrifice into a counter on himself. *strategic_judgment · moderate*
- ⚠️ **Honest note:** Once per turn and only nonlegendary artifact spells; the deck's artifact-sacrifice core (KCI, altars, Urza) would run under any Grixis artifact commander. Ashad is a strong value engine, not the deck's sole win source.
  - Evidence: [Ashad_the_Lone_Cyberman_Approval_Ready_Closeout_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Ashad_the_Lone_Cyberman_Approval_Ready_Closeout_2026-10-13.md) · [ashad-01](../interactions/ashad-the-lone-cyberman.md#ashad-01-casualty-2-on-your-first-nonlegendary-artifact-spell) · [ashad-02](../interactions/ashad-the-lone-cyberman.md#ashad-02-the-11-trigger-needs-another-creature-sacrificed) · [ashad-08](../interactions/ashad-the-lone-cyberman.md#ashad-08-flash-artifacts-reuse-first-each-turn-on-other-turns)
- **Dependency level:** medium *strategic_judgment · moderate* — [Ashad_the_Lone_Cyberman_Approval_Ready_Closeout_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Ashad_the_Lone_Cyberman_Approval_Ready_Closeout_2026-10-13.md) · [ashad-05](../interactions/ashad-the-lone-cyberman.md#ashad-05-urza--worldwalker-helm--artificer-class)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | — (none stated) (No source ceiling stated in the blueprint, slot audit, closeout or final verification (checked Bot cycle 50).) | *fact · high* | [Ashad_the_Lone_Cyberman_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Ashad_the_Lone_Cyberman_v1.md) · [Ashad_the_Lone_Cyberman_Approval_Ready_Closeout_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Ashad_the_Lone_Cyberman_Approval_Ready_Closeout_2026-10-13.md) |
| GrokBot estimated ceiling | 4 (Bracket 4 ceiling for an artifact-copy engine with a Spellbook infinite and KCI/altar density; the list as built sits at its computed floor of 3.) | *strategic_judgment · moderate* | [ashad-05](../interactions/ashad-the-lone-cyberman.md#ashad-05-urza--worldwalker-helm--artificer-class) · `spellbook:66-457-5491` · [Ashad_the_Lone_Cyberman_Approval_Ready_Closeout_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Ashad_the_Lone_Cyberman_Approval_Ready_Closeout_2026-10-13.md) |
| Expected bracket (list as built) | 3 (computed floor 3) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Ashad__the_Lone_Cyberman` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | — (no source ceiling) | | |

- EDHREC: `{"bracket_counts": {"1": 2, "2": 198, "3": 90, "4": 18, "5": 4}, "decks_with_bracket": 312, "share_b4_plus": 0.071, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__ashad-the-lone-cyberman.json`

## Win conditions

- **urza-helm-class** (combo): Urza, Lord High Artificer + Worldwalker Helm + Artificer Class (Spellbook infinite). Cards: Urza, Lord High Artificer, Worldwalker Helm, Artificer Class. *fact · verified* — [ashad-05](../interactions/ashad-the-lone-cyberman.md#ashad-05-urza--worldwalker-helm--artificer-class) · `spellbook:66-457-5491`
- **sacrifice-drain** (natural): Disciple of the Vault / Mayhem Devil / Reckless Fireweaver drain as artifacts are sacrificed to KCI and altars. Cards: Disciple of the Vault, Mayhem Devil, Reckless Fireweaver, Krark-Clan Ironworks, Ashnod's Altar. Enablers: Marionette Master. *strategic_judgment · moderate* — [ashad-09](../interactions/ashad-the-lone-cyberman.md#ashad-09-sacrifice-and-artifact-death-drains) · [Ashad_the_Lone_Cyberman_Approval_Ready_Closeout_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Ashad_the_Lone_Cyberman_Approval_Ready_Closeout_2026-10-13.md)
- **copied-bombs** (natural): Casualty-copied Wurmcoil Engine, Portal to Phyrexia or Noxious Gearhulk overwhelm the board. Cards: Wurmcoil Engine, Portal to Phyrexia, Noxious Gearhulk. Enablers: Ashad, the Lone Cyberman. *strategic_judgment · moderate* — [Ashad_the_Lone_Cyberman_Approval_Ready_Closeout_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Ashad_the_Lone_Cyberman_Approval_Ready_Closeout_2026-10-13.md) · [ashad-12](../interactions/ashad-the-lone-cyberman.md#ashad-12-portal-to-phyrexia-with-casualty)

## Engines

- **artifact-casualty:** Ashad, the Lone Cyberman, Twinning Staff, Poetic Ingenuity, Biotransference. Online when: A power-2+ creature to sacrifice when casting the turn's first nonlegendary artifact spell. *fact · verified* — [ashad-01](../interactions/ashad-the-lone-cyberman.md#ashad-01-casualty-2-on-your-first-nonlegendary-artifact-spell) · [ashad-04](../interactions/ashad-the-lone-cyberman.md#ashad-04-twinning-staff-applies-to-artifact-spell-copies)
- **flash-artifacts:** Shimmer Myr, Unwinding Clock. Online when: Artifact spells cast on opponents' turns reuse 'first each turn'. *fact · verified* — [ashad-08](../interactions/ashad-the-lone-cyberman.md#ashad-08-flash-artifacts-reuse-first-each-turn-on-other-turns)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:copy-targets` | yes | 8 | Nonlegendary artifacts that are much better copied. | 10: Solemn Simulacrum, Ichor Wellspring, Wurmcoil Engine, Portal to Phyrexia, Noxious Gearhulk, Phyrexian Metamorph, Sculpting Steel, Simulacrum Synthesizer, Worldwalker Helm, Thopter Spy Network | — | *strategic_judgment · high* | [Ashad_the_Lone_Cyberman_Approval_Ready_Closeout_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Ashad_the_Lone_Cyberman_Approval_Ready_Closeout_2026-10-13.md) |
| `pkg:power-2-fodder` | yes | 6 | Artifact creatures/tokens with power 2+ for casualty. | 8: Cybermen Squadron, Solemn Simulacrum, Kappa Cannoneer, Scrap Trawler, Thought Monitor, Enthusiastic Mechanaut, Foundry Inspector, Cyberdrive Awakener | — | *strategic_judgment · high* | [Ashad_the_Lone_Cyberman_Approval_Ready_Closeout_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Ashad_the_Lone_Cyberman_Approval_Ready_Closeout_2026-10-13.md) · [Ashad_the_Lone_Cyberman_99_Slot_Audit_Working_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Ashad_the_Lone_Cyberman_99_Slot_Audit_Working_2026-10-13.md) |
| `pkg:sac-outlets-and-payoffs` | yes | 5 | Convert artifacts into mana, cards and drain. | 7: Krark-Clan Ironworks, Ashnod's Altar, Phyrexian Altar, Disciple of the Vault, Mayhem Devil, Pitiless Plunderer, Marionette Master | — | *strategic_judgment · high* | [Ashad_the_Lone_Cyberman_Approval_Ready_Closeout_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Ashad_the_Lone_Cyberman_Approval_Ready_Closeout_2026-10-13.md) |
| `pkg:artifact-recursion` | yes | 4 | Rebuy sacrificed artifacts. | 5: Scrap Trawler, Emry, Lurker of the Loch, Goblin Welder, Academy Ruins, Esoteric Duplicator | — | *strategic_judgment · high* | [Ashad_the_Lone_Cyberman_Approval_Ready_Closeout_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Ashad_the_Lone_Cyberman_Approval_Ready_Closeout_2026-10-13.md) |

## Key interactions

- **casualty-artifact:** First nonlegendary artifact spell each turn: sacrifice power 2+ to copy it into a token. (Ashad, the Lone Cyberman) *fact · verified* — [ashad-01](../interactions/ashad-the-lone-cyberman.md#ashad-01-casualty-2-on-your-first-nonlegendary-artifact-spell)
- **not-created:** Casualty copies enter as tokens but aren't 'created': Worldwalker Helm makes no Map. (Worldwalker Helm) *fact · verified* — [ashad-03](../interactions/ashad-the-lone-cyberman.md#ashad-03-casualty-tokens-arent-created-no-worldwalker-helm-map)
- **staff-applies:** Twinning Staff applies to artifact spell copies. (Twinning Staff) *fact · verified* — [ashad-04](../interactions/ashad-the-lone-cyberman.md#ashad-04-twinning-staff-applies-to-artifact-spell-copies)
- **biotransference:** Biotransference makes creature spells artifact spells, so they get casualty. (Biotransference) *fact · verified* — [ashad-06](../interactions/ashad-the-lone-cyberman.md#ashad-06-biotransference-makes-creature-spells-artifact-spells)
- **iron-man-legendary:** Iron Man copies legendary artifacts as nonlegendary. (Iron Man, Bleeding Edge) *fact · verified* — [ashad-07](../interactions/ashad-the-lone-cyberman.md#ashad-07-iron-man-copies-legendary-artifacts-as-nonlegendary)

## Tutors and recursion

- Tutor target **Urza, Lord High Artificer** via Demonic Tutor *strategic_judgment · moderate* — [ashad-05](../interactions/ashad-the-lone-cyberman.md#ashad-05-urza--worldwalker-helm--artificer-class)
- Tutor target **Worldwalker Helm** via Fabricate, Inventors' Fair, Demonic Tutor *strategic_judgment · moderate* — [ashad-05](../interactions/ashad-the-lone-cyberman.md#ashad-05-urza--worldwalker-helm--artificer-class)
- Recursion: Scrap Trawler, Emry, Lurker of the Loch, Goblin Welder, Academy Ruins, Esoteric Duplicator *fact · verified* — [Ashad_the_Lone_Cyberman_Approval_Ready_Closeout_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Ashad_the_Lone_Cyberman_Approval_Ready_Closeout_2026-10-13.md) · [ashad-11](../interactions/ashad-the-lone-cyberman.md#ashad-11-esoteric-duplicator-rebuys-sacrificed-artifacts)

## Requirements

- **Interaction:** Artifact hate is the main threat; keep counters (Mana Drain, Arcane Denial) and flexible removal.
- **Protection:** Greaves, Fierce Guardianship, Deflecting Swat, Padeem for artifacts.
- **Mana:** Artifact mana (Mox Opal, Urza's Saga, KCI) and 30+ lands.
- *strategic_judgment · moderate* — [Ashad_the_Lone_Cyberman_Approval_Ready_Closeout_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Ashad_the_Lone_Cyberman_Approval_Ready_Closeout_2026-10-13.md)

## Failure modes

- **artifact-wipe:** Vandalblast/Bane of Progress resets the board and the copy targets. Mitigations: Recursion package; Padeem; Counters. *strategic_judgment · high* — [Ashad_the_Lone_Cyberman_Approval_Ready_Closeout_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Ashad_the_Lone_Cyberman_Approval_Ready_Closeout_2026-10-13.md)
- **no-fodder:** No power-2+ creature to sacrifice: no copy. Mitigations: Poetic Ingenuity Dinosaurs; Biotransference Necrons. *strategic_judgment · moderate* — [ashad-01](../interactions/ashad-the-lone-cyberman.md#ashad-01-casualty-2-on-your-first-nonlegendary-artifact-spell)
- **legendary-clog:** Legendary artifacts don't get casualty. Mitigations: Iron Man copies legendary artifacts as nonlegendary. *strategic_judgment · moderate* — [ashad-02](../interactions/ashad-the-lone-cyberman.md#ashad-02-the-11-trigger-needs-another-creature-sacrificed)

## Identity core

- **Ashad, the Lone Cyberman:** Turns the first artifact spell each turn into a free token copy. *fact · verified* — `oracle:Ashad, the Lone Cyberman`
- **Twinning Staff:** Core multiplier: each casualty copy becomes two. *strategic_judgment · high* — [Ashad_the_Lone_Cyberman_Approval_Ready_Closeout_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Ashad_the_Lone_Cyberman_Approval_Ready_Closeout_2026-10-13.md) · [ashad-04](../interactions/ashad-the-lone-cyberman.md#ashad-04-twinning-staff-applies-to-artifact-spell-copies)
- **Shimmer Myr:** Flash for artifacts uses 'first each turn' on every opponent's turn too. *strategic_judgment · high* — [Ashad_the_Lone_Cyberman_Approval_Ready_Closeout_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Ashad_the_Lone_Cyberman_Approval_Ready_Closeout_2026-10-13.md) · [ashad-08](../interactions/ashad-the-lone-cyberman.md#ashad-08-flash-artifacts-reuse-first-each-turn-on-other-turns)
- **Poetic Ingenuity:** Artifact casts make 3/1 Dinosaurs: casualty fodder that also makes Treasure. *strategic_judgment · high* — [Ashad_the_Lone_Cyberman_Approval_Ready_Closeout_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Ashad_the_Lone_Cyberman_Approval_Ready_Closeout_2026-10-13.md)
- **Solemn Simulacrum:** Both fodder and copy target; each copy ramps and later draws. *strategic_judgment · moderate* — [Ashad_the_Lone_Cyberman_Approval_Ready_Closeout_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Ashad_the_Lone_Cyberman_Approval_Ready_Closeout_2026-10-13.md)

## Anti-goals and thematic constraints

- ✗ Don't reduce the deck to generic artifact combo without copy targets.
- ✗ Don't add legendary artifacts that Ashad can't copy without a reason.
  - *strategic_judgment · high* — [Ashad_the_Lone_Cyberman_Approval_Ready_Closeout_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Ashad_the_Lone_Cyberman_Approval_Ready_Closeout_2026-10-13.md)
- Theme: Doctor Who Cybermen flavor (Cyber-Controller, Cybermen Squadron, Cyber Conversion) is part of the identity.
  - *strategic_judgment · moderate* — [Ashad_the_Lone_Cyberman_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Ashad_the_Lone_Cyberman_v1.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 702.153a:** Casualty is paid while casting; the sacrificed creature is gone before opponents can respond. *fact · verified* — `cr:702.153a`
- **CR 707.10:** A copy of a permanent spell becomes a token as it resolves. *fact · verified* — `cr:707.10`

## Supporting features (heuristic, not identity)

- `{"hooks": ["+1/+1 counters", "artifacts", "casualty / power 2 or greater", "copying", "sacrifice"], "hooked_cards": 62, "role_counts": {"counter": 3, "draw": 11, "protection": 3, "ramp": 15, "removal": 4, "tutor": 2, "wipe": 1}, "lands": 30, "edhrec_pages": ["ashad-the-lone-cyberman"]}` *heuristic · low*

## Provenance

- Seeded from: [Ashad_the_Lone_Cyberman_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Ashad_the_Lone_Cyberman_v1.md) · [Ashad_the_Lone_Cyberman_Approval_Ready_Closeout_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Ashad_the_Lone_Cyberman_Approval_Ready_Closeout_2026-10-13.md) · [Ashad_the_Lone_Cyberman_99_Slot_Audit_Working_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Ashad_the_Lone_Cyberman_99_Slot_Audit_Working_2026-10-13.md) · [Ashad_the_Lone_Cyberman_Approval_Ready_2026-10-13.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Ashad_the_Lone_Cyberman_Approval_Ready_2026-10-13.txt)
- Reviewed by: — (not yet reviewed by Cory)
