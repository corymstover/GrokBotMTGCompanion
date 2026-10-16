# Blueprint — Cult of Skaro

> **Commander Blueprint v1** (seeded, Bot cycle 50, 2026-10-16) for the canonical project list ([deck page](../decks/cult-of-skaro.md), state `SOURCE_BASELINE`, list `lh1:b5f92812544811f4…`). Machine-readable source: [`data/grixis/blueprints/cult-of-skaro.json`](../../data/grixis/blueprints/cult-of-skaro.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Cult of Skaro** — Legendary Artifact Creature — Dalek

> Whenever Cult of Skaro attacks, choose one at random —  
> • Thay — Put a +1/+1 counter on each artifact creature you control.  
> • Caan — Draw two cards.  
> • Sec — Create a 3/3 black Dalek artifact creature token with menace.  
> • Jast — Each opponent loses 4 life.

## Plan and commander role

- **Primary plan:** Attack-trigger artifact army: protect Cult of Skaro and attack every turn for a random but always useful mode (counters on artifact creatures, two cards, a 3/3 Dalek, or 4 life from each opponent); multiply attacks and triggers with Helm of the Host, extra combats and Strionic Resonator/Scientist Supreme. *strategic_judgment · high*
- **Secondary:** Wide artifact-creature board scaled by Steel Overseer, Master of Etherium and The Cyber-Controller; Sword of Feast and Famine + Aggravated Assault infinite combats.
  - Evidence: [Cult_of_Skaro_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Cult_of_Skaro_Current_Cycle_Decisions_2026-10-14.md) · [skaro-01](../interactions/cult-of-skaro.md#skaro-01-the-random-mode-is-chosen-as-the-trigger-goes-on-the-stack) · [skaro-05](../interactions/cult-of-skaro.md#skaro-05-sword-of-feast-and-famine--aggravated-assault)
- **Commander role: central.** Every Cult attack produces value; Helm tokens, extra combats and copies each roll another trigger. *strategic_judgment · high*
- ⚠️ **Honest note:** The mode is random and fixed when the trigger goes on the stack, so the engine is high-variance; copies repeat the rolled mode, extra triggers re-roll.
  - Evidence: [Cult_of_Skaro_Current_Cycle_Decisions_2026-10-14.md#L36](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Cult_of_Skaro_Current_Cycle_Decisions_2026-10-14.md) · [skaro-01](../interactions/cult-of-skaro.md#skaro-01-the-random-mode-is-chosen-as-the-trigger-goes-on-the-stack) · [skaro-02](../interactions/cult-of-skaro.md#skaro-02-copies-keep-the-mode-extra-triggers-re-roll)
- **Dependency level:** high *strategic_judgment · high* — [Cult_of_Skaro_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Cult_of_Skaro_Current_Cycle_Decisions_2026-10-14.md)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 4 (Bracket 4 — Optimized (current-cycle decisions).) | *fact · verified* | [Cult_of_Skaro_Current_Cycle_Decisions_2026-10-14.md#L36](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Cult_of_Skaro_Current_Cycle_Decisions_2026-10-14.md) · [Cult_of_Skaro_Current_Cycle_Decisions_2026-10-14.md#L75](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Cult_of_Skaro_Current_Cycle_Decisions_2026-10-14.md) |
| GrokBot estimated ceiling | 4 (Bracket 4 ceiling: commander-native infinite combats with Sword + Assault; random, combat-dependent engine; list sits at its computed floor of 3. Agrees with the source ceiling.) | *strategic_judgment · high* | [Cult_of_Skaro_Current_Cycle_Decisions_2026-10-14.md#L36](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Cult_of_Skaro_Current_Cycle_Decisions_2026-10-14.md) · [skaro-05](../interactions/cult-of-skaro.md#skaro-05-sword-of-feast-and-famine--aggravated-assault) |
| Expected bracket (list as built) | 3 (computed floor 3) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Cult_of_Skaro` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 5, "2": 89, "3": 62, "4": 13, "5": 2}, "decks_with_bracket": 171, "share_b4_plus": 0.088, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__cult-of-skaro.json`

## Win conditions

- **sword-assault** (combo): Sword of Feast and Famine + Aggravated Assault: infinite combats, each one a new Cult trigger. Cards: Sword of Feast and Famine, Aggravated Assault. Enablers: Cult of Skaro. *fact · verified* — [skaro-05](../interactions/cult-of-skaro.md#skaro-05-sword-of-feast-and-famine--aggravated-assault) · `spellbook:900-3750`
- **multiplied-attacks** (natural): Helm of the Host Cult copies, extra combats (Full Throttle, Great Train Heist) and trigger copiers stack drain (Jast) and Dalek tokens. Cards: Helm of the Host, Full Throttle, Great Train Heist, Strionic Resonator, Scientist Supreme of A.I.M.. Enablers: Lightning Greaves, Swiftfoot Boots. *strategic_judgment · high* — [Cult_of_Skaro_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Cult_of_Skaro_Current_Cycle_Decisions_2026-10-14.md) · [skaro-03](../interactions/cult-of-skaro.md#skaro-03-helm-of-the-host-spark-double-sakashima-auton-soldier-copies)
- **artifact-swarm** (natural): Wide artifact army pumped by lords and the counter mode. Cards: Steel Overseer, Master of Etherium, The Cyber-Controller, Genesis of the Daleks, Dalek Squadron. *strategic_judgment · moderate* — [Cult_of_Skaro_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Cult_of_Skaro_v1.md)

## Engines

- **cult-attack:** Cult of Skaro, Helm of the Host, Strionic Resonator, Scientist Supreme of A.I.M., Roaming Throne. Online when: Cult (or a Cult copy) attacks. *fact · verified* — [skaro-01](../interactions/cult-of-skaro.md#skaro-01-the-random-mode-is-chosen-as-the-trigger-goes-on-the-stack) · [skaro-02](../interactions/cult-of-skaro.md#skaro-02-copies-keep-the-mode-extra-triggers-re-roll)
- **extra-combats:** Full Throttle, Great Train Heist, Aggravated Assault. Online when: Mana for extra combat costs. *fact · verified* — [skaro-06](../interactions/cult-of-skaro.md#skaro-06-full-throttle-and-great-train-heist-extra-combats)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:attack-protection` | yes | 6 | Haste and protection so Cult attacks every turn. | 7: Lightning Greaves, Swiftfoot Boots, Padeem, Consul of Innovation, Arena of Glory, Plaza of Heroes, Fierce Guardianship, Deflecting Swat | — | *strategic_judgment · high* | [Cult_of_Skaro_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Cult_of_Skaro_Current_Cycle_Decisions_2026-10-14.md) |
| `pkg:trigger-multipliers` | yes | 5 | Extra Cult triggers or copies. | 7: Helm of the Host, Strionic Resonator, Scientist Supreme of A.I.M., Roaming Throne, Spark Double, Sakashima of a Thousand Faces, Phyrexian Metamorph | — | *strategic_judgment · high* | [Cult_of_Skaro_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Cult_of_Skaro_Current_Cycle_Decisions_2026-10-14.md) |
| `pkg:artifact-creature-army` | yes | 10 | Artifact creatures and token makers that the counter and Dalek modes scale. | 12: Dalek Drone, Dalek Squadron, Cybermen Squadron, Cyberman Patrol, Auton Soldier, Thought Monitor, Canoptek Spyder, Davros, Dalek Creator, The Dalek Emperor, Genesis of the Daleks, Thopter Spy Network, Sai, Master Thopterist | Cybermat | *strategic_judgment · high* | [Cult_of_Skaro_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Cult_of_Skaro_v1.md) |
| `pkg:artifact-lords` | yes | 3 | Scale the board. | 3: Steel Overseer, Master of Etherium, The Cyber-Controller | — | *strategic_judgment · high* | [Cult_of_Skaro_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Cult_of_Skaro_v1.md) |

## Key interactions

- **random-on-stack:** The mode is chosen at random as the trigger is put on the stack. (Cult of Skaro) *fact · verified* — [skaro-01](../interactions/cult-of-skaro.md#skaro-01-the-random-mode-is-chosen-as-the-trigger-goes-on-the-stack)
- **copies-vs-triggers:** Resonator/Scientist copies repeat the rolled mode; Roaming Throne extra triggers re-roll. (Strionic Resonator, Scientist Supreme of A.I.M., Roaming Throne) *fact · verified* — [skaro-02](../interactions/cult-of-skaro.md#skaro-02-copies-keep-the-mode-extra-triggers-re-roll)
- **helm-copies:** Helm of the Host, Spark Double, Sakashima and Auton Soldier make Cult copies that attack. (Helm of the Host, Spark Double, Sakashima of a Thousand Faces, Auton Soldier) *fact · verified* — [skaro-03](../interactions/cult-of-skaro.md#skaro-03-helm-of-the-host-spark-double-sakashima-auton-soldier-copies)
- **exterminate:** Exterminate! replicates by tapping Daleks. (Exterminate!) *fact · verified* — [skaro-08](../interactions/cult-of-skaro.md#skaro-08-exterminate-replicates-by-tapping-daleks)

## Tutors and recursion

- Tutor target **Sword of Feast and Famine** via Inventors' Fair *strategic_judgment · moderate* — [skaro-05](../interactions/cult-of-skaro.md#skaro-05-sword-of-feast-and-famine--aggravated-assault)
- Tutor target **Helm of the Host** via Inventors' Fair *strategic_judgment · moderate* — [Cult_of_Skaro_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Cult_of_Skaro_Current_Cycle_Decisions_2026-10-14.md)
- Recursion: Academy Ruins, Emry, Lurker of the Loch *strategic_judgment · moderate* — [skaro-10](../interactions/cult-of-skaro.md#skaro-10-commander-tax-and-artifact-recursion)

## Requirements

- **Interaction:** Counters (Mana Drain) and flexible removal (Delete, Chaos Warp, Cyclonic Rift).
- **Protection:** Greaves, Boots, Padeem, Plaza; the engine needs Cult to survive attacking.
- **Mana:** Artifact mana (Mox Opal, Mana Vault, Urza's Saga) for extra-combat turns.
- *strategic_judgment · moderate* — [Cult_of_Skaro_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Cult_of_Skaro_Current_Cycle_Decisions_2026-10-14.md)

## Failure modes

- **bad-rolls:** Random modes miss what the board needs. Mitigations: More triggers average out the variance. *strategic_judgment · high* — [skaro-01](../interactions/cult-of-skaro.md#skaro-01-the-random-mode-is-chosen-as-the-trigger-goes-on-the-stack)
- **cult-removed:** Cult dies attacking or to removal. Mitigations: Haste/protection package; Helm copies. *strategic_judgment · high* — [Cult_of_Skaro_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Cult_of_Skaro_Current_Cycle_Decisions_2026-10-14.md)
- **artifact-wipe:** Artifact wipes reset the army. Mitigations: Academy Ruins; Counters. *strategic_judgment · moderate* — [Cult_of_Skaro_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Cult_of_Skaro_v1.md)
- **few-tutors:** Almost no tutors (Inventors' Fair only for artifacts; Urza's Saga finds 0-1 cost artifacts), so the Sword + Assault combo is found by drawing. Mitigations: Caan draw mode; Thought Monitor; Research Thief. *strategic_judgment · moderate* — [Cult_of_Skaro_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Cult_of_Skaro_Current_Cycle_Decisions_2026-10-14.md)

## Identity core

- **Cult of Skaro:** Attack trigger with four random payoffs. *fact · verified* — `oracle:Cult of Skaro`
- **Helm of the Host:** A hasty nonlegendary Cult every combat, each rolling its own trigger. *strategic_judgment · high* — [Cult_of_Skaro_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Cult_of_Skaro_Current_Cycle_Decisions_2026-10-14.md)
- **Aggravated Assault:** With Sword it is infinite combats; alone it is a repeatable extra attack. *strategic_judgment · high* — [skaro-05](../interactions/cult-of-skaro.md#skaro-05-sword-of-feast-and-famine--aggravated-assault)
- **Scientist Supreme of A.I.M.:** Two-mana copier for Cult's artifact-source trigger. *strategic_judgment · high* — [Cult_of_Skaro_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Cult_of_Skaro_Current_Cycle_Decisions_2026-10-14.md)
- **The Cyber-Controller:** Doctor Who artifact payoff that scales the counter mode. *strategic_judgment · moderate* — [Cult_of_Skaro_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Cult_of_Skaro_v1.md)

## Anti-goals and thematic constraints

- ✗ Don't become a generic Grixis combo shell; the infinite should be commander-native combat.
- ✗ Don't add non-artifact creatures that the counter mode ignores without reason.
  - *strategic_judgment · high* — [Cult_of_Skaro_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Cult_of_Skaro_Current_Cycle_Decisions_2026-10-14.md)
- Theme: Doctor Who Daleks and Cybermen.
  - *strategic_judgment · high* — [Cult_of_Skaro_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Cult_of_Skaro_v1.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 707.10:** A copied triggered ability keeps the mode chosen for the original. *fact · verified* — `cr:707.10`
- **CR 702.111:** Menace on Dalek tokens. *fact · verified* — `cr:702.111`

## Supporting features (heuristic, not identity)

- `{"hooks": ["+1/+1 counters", "Dalek synergy", "artifacts", "combat damage / attack triggers", "opponents losing life", "tokens"], "hooked_cards": 57, "role_counts": {"counter": 2, "draw": 9, "protection": 5, "ramp": 10, "removal": 5, "wipe": 2}, "lands": 34, "edhrec_pages": ["cult-of-skaro"]}` *heuristic · low*

## Provenance

- Seeded from: [Cult_of_Skaro_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Cult_of_Skaro_v1.md) · [Cult_of_Skaro_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Cult_of_Skaro_Current_Cycle_Decisions_2026-10-14.md) · [Cult_of_Skaro_Approval_Candidate_2026-10-14.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Cult_of_Skaro_Approval_Candidate_2026-10-14.txt)
- Reviewed by: — (not yet reviewed by Cory)
