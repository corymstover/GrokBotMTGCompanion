# Blueprint — Loki, the Deceiver

> **Commander Blueprint v1** (seeded, Bot cycle 52, 2026-10-16) for the canonical project list ([deck page](../decks/loki-the-deceiver.md), state `SOURCE_BASELINE`, list `lh1:1af6ee049bf73721…`). Machine-readable source: [`data/grixis/blueprints/loki-the-deceiver.json`](../../data/grixis/blueprints/loki-the-deceiver.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Loki, the Deceiver** — Legendary Creature — God Sorcerer Villain

> Whenever Loki attacks, create a tapped and attacking token that's a copy of another target Villain you control, except it isn't legendary and it's an Illusion in addition to its other types. Sacrifice that token at the beginning of the next end step.  
> Whenever one or more Villains you control deal combat damage to a player, draw a card.

## Plan and commander role

- **Primary plan:** Villain-copy combat value: Loki attacks safely, copies the best Villain for the combat (enters, static and combat-damage text, not attack triggers), and connecting Villains draw cards. *strategic_judgment · high*
- **Secondary:** Keep the temporary copies (The Master, Multiplied; Sundial of the Infinite), double Loki's trigger (Roaming Throne, Hall of Echoes, Titan of Littjara), and grind with Villain tribal draw (Kindred Discovery) and premium Grixis interaction.
  - Evidence: [Loki_the_Deceiver_Current_Cycle_Decisions_2026-10-14.md#L15](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Loki_the_Deceiver_Current_Cycle_Decisions_2026-10-14.md) · [loki-01](../interactions/loki-the-deceiver.md#loki-01-the-token-enters-attacking-so-its-own-attack-triggers-dont-fire) · [loki-02](../interactions/loki-the-deceiver.md#loki-02-villain-combat-damage-draws-once-per-batch)
- **Commander role: central.** Loki's attack copy and Villain combat draw are the deck's main engine. *strategic_judgment · high*
- ⚠️ **Honest note:** There is no compact win: Commander Spellbook finds no combos in the list. The copy enters attacking, so attack-trigger Villains do nothing as targets (M1 loki-01). Loki has to attack and survive combat to generate value.
  - Evidence: [Loki_the_Deceiver_Current_Cycle_Decisions_2026-10-14.md#L17](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Loki_the_Deceiver_Current_Cycle_Decisions_2026-10-14.md) · [loki-01](../interactions/loki-the-deceiver.md#loki-01-the-token-enters-attacking-so-its-own-attack-triggers-dont-fire)
- **Dependency level:** high *strategic_judgment · high* — [Loki_the_Deceiver_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Loki_the_Deceiver_Current_Cycle_Decisions_2026-10-14.md)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 4 (Power Bracket 4 — Optimized (decisions).) | *fact · verified* | [Loki_the_Deceiver_Current_Cycle_Decisions_2026-10-14.md#L21](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Loki_the_Deceiver_Current_Cycle_Decisions_2026-10-14.md) |
| GrokBot estimated ceiling | 4 (Bracket 4 ceiling, low end: premium Grixis interaction and Game Changers put the list in B4, but there's no compact win and the commander is a combat-value engine. Agrees with the source.) | *strategic_judgment · high* | [Loki_the_Deceiver_Current_Cycle_Decisions_2026-10-14.md#L21](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Loki_the_Deceiver_Current_Cycle_Decisions_2026-10-14.md) · [loki-01](../interactions/loki-the-deceiver.md#loki-01-the-token-enters-attacking-so-its-own-attack-triggers-dont-fire) |
| Expected bracket (list as built) | 4 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Loki__the_Deceiver` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 7, "2": 140, "3": 169, "4": 26, "5": 2}, "decks_with_bracket": 344, "share_b4_plus": 0.081, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__loki-the-deceiver.json`

## Win conditions

- **villain-combat** (natural): A wide, anthem-boosted Villain board with copied bodies attacks every turn while Loki draws. Cards: Avengers: Under Siege, Doctor Octopus, Master Planner, Red Ghost, Intangible Genius, Titan of Littjara, The Master, Multiplied. Enablers: Loki, the Deceiver. *strategic_judgment · high* — [Loki_the_Deceiver_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Loki_the_Deceiver_Current_Cycle_Decisions_2026-10-14.md) · [loki-06](../interactions/loki-the-deceiver.md#loki-06-doctor-octopus-token-anthem-now-draw-before-the-sacrifice)
- **card-advantage-grind** (natural): Villain card draw (Loki, Kindred Discovery, Rhystic Study) out-grinds the table behind counters and wipes. Cards: Kindred Discovery, Rhystic Study, Black Market Connections. Enablers: Loki, the Deceiver. *strategic_judgment · moderate* — [Loki_the_Deceiver_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Loki_the_Deceiver_Current_Cycle_Decisions_2026-10-14.md)

## Engines

- **attack-copy:** Loki, the Deceiver, Roaming Throne, Hall of Echoes, Titan of Littjara, Spark Double. Online when: Loki attacks with another Villain in play. *fact · verified* — [loki-01](../interactions/loki-the-deceiver.md#loki-01-the-token-enters-attacking-so-its-own-attack-triggers-dont-fire) · [loki-03](../interactions/loki-the-deceiver.md#loki-03-titan-of-littjara-and-roaming-throne-choose-villain) · [loki-04](../interactions/loki-the-deceiver.md#loki-04-hall-of-echoes-as-a-second-loki)
- **keep-copies:** The Master, Multiplied, Sundial of the Infinite, Doctor Octopus, Master Planner. Online when: A Loki token in play before end step. *fact · verified* — [loki-05](../interactions/loki-the-deceiver.md#loki-05-keeping-the-token-the-master-multiplied-and-sundial) · [loki-06](../interactions/loki-the-deceiver.md#loki-06-doctor-octopus-token-anthem-now-draw-before-the-sacrifice)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:villains` | yes | 20 | Villains with enters, static or combat-damage text worth copying. | 22: Baron Strucker, HYDRA Overlord, Black Cat, Cunning Thief, Carnage, Crimson Chaos, Crimson Cowl, Master of Evil, Crossbones, Malicious Mercenary, Doctor Doom, King of Latveria, Doctor Octopus, Master Planner, Iron Monger, Sadistic Tycoon, Kang Prime, Kang, Temporal Tyrant, Killmonger, Ruthless Usurper, Leader, Super-Genius, M.O.D.O.K., Madame Hydra, Norman Osborn // Green Goblin, Prowler, Clawed Thief, Red Ghost, Intangible Genius, Stilt-Man, Towering Terror, Tombstone, Career Criminal, Ultron, Unlimited, Venom, Eddie Brock, Mysterio, Master of Illusion | — | *strategic_judgment · high* | [Loki_the_Deceiver_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Loki_the_Deceiver_Current_Cycle_Decisions_2026-10-14.md) · [Loki_the_Deceiver_Whole_List_Audit_2026-10-14.csv](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Loki_the_Deceiver_Whole_List_Audit_2026-10-14.csv) |
| `pkg:copy` | yes | 5 | More copies of Loki or his targets. | 7: Spark Double, Taskmaster, Mercenary Mimic, Mysterio, Master of Illusion, Chameleon, Master of Disguise, Loki, Lord of Misrule, Hall of Echoes, Titan of Littjara | — | *strategic_judgment · high* | [Loki_the_Deceiver_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Loki_the_Deceiver_Current_Cycle_Decisions_2026-10-14.md) |

## Key interactions

- **enters-attacking:** The copy enters attacking: no attack triggers, but ETB, statics and combat-damage triggers work. (Loki, the Deceiver) *fact · verified* — [loki-01](../interactions/loki-the-deceiver.md#loki-01-the-token-enters-attacking-so-its-own-attack-triggers-dont-fire)
- **batch-draw:** Villain combat damage draws once per batch. (Loki, the Deceiver) *fact · verified* — [loki-02](../interactions/loki-the-deceiver.md#loki-02-villain-combat-damage-draws-once-per-batch)
- **throne-villain:** Roaming Throne naming Villain doubles Loki's attack trigger. (Roaming Throne, Titan of Littjara) *fact · verified* — [loki-03](../interactions/loki-the-deceiver.md#loki-03-titan-of-littjara-and-roaming-throne-choose-villain)
- **keep-token:** The Master stops the sacrifice; Sundial only with the trigger on the stack. (The Master, Multiplied, Sundial of the Infinite) *fact · verified* — [loki-05](../interactions/loki-the-deceiver.md#loki-05-keeping-the-token-the-master-multiplied-and-sundial)
- **scepter:** Loki's Scepter's temporary Villain type doesn't carry onto Loki's copy. (Loki's Scepter) *fact · verified* — [loki-07](../interactions/loki-the-deceiver.md#loki-07-lokis-scepter-a-temporary-villain-copies-as-a-non-villain)

## Tutors and recursion

- Tutor target **The Master, Multiplied** via Demonic Tutor *strategic_judgment · moderate* — [Loki_the_Deceiver_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Loki_the_Deceiver_Current_Cycle_Decisions_2026-10-14.md)
- Recursion: Reanimate, Jeska's Will *strategic_judgment · low* — [Loki_the_Deceiver_Whole_List_Audit_2026-10-14.csv](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Loki_the_Deceiver_Whole_List_Audit_2026-10-14.csv)

## Requirements

- **Interaction:** Mana Drain, Fierce Guardianship, An Offer You Can't Refuse, Deadly Rollick, Toxic Deluge, Blasphemous Act, Cyclonic Rift.
- **Protection:** Swiftfoot Boots, Lightning Greaves, Deflecting Swat.
- **Mana:** 34 lands, Sol Ring, Talismans, Dark Ritual; Cavern of Souls and Path of Ancestry for Villains.
- *strategic_judgment · moderate* — [Loki_the_Deceiver_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Loki_the_Deceiver_Current_Cycle_Decisions_2026-10-14.md)

## Failure modes

- **no-combo:** No compact win; the deck has to win through combat. Mitigations: Card advantage; Interaction suite. *strategic_judgment · high* — [Loki_the_Deceiver_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Loki_the_Deceiver_Current_Cycle_Decisions_2026-10-14.md)
- **attack-trigger-targets:** Attack-trigger Villains are poor copy targets. Mitigations: Source cut most of them. *strategic_judgment · high* — [loki-01](../interactions/loki-the-deceiver.md#loki-01-the-token-enters-attacking-so-its-own-attack-triggers-dont-fire)
- **loki-removed:** Loki removed or unable to attack safely. Mitigations: Boots, Greaves; Copy redundancy. *strategic_judgment · moderate* — [Loki_the_Deceiver_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Loki_the_Deceiver_Current_Cycle_Decisions_2026-10-14.md)

## Identity core

- **Loki, the Deceiver:** Attack-time Villain copy plus Villain combat draw. *fact · verified* — `oracle:Loki, the Deceiver`
- **The Master, Multiplied:** Keeps Loki's temporary copies. *strategic_judgment · high* — [loki-05](../interactions/loki-the-deceiver.md#loki-05-keeping-the-token-the-master-multiplied-and-sundial)
- **Roaming Throne:** Doubles Loki's attack trigger. *strategic_judgment · high* — [loki-03](../interactions/loki-the-deceiver.md#loki-03-titan-of-littjara-and-roaming-throne-choose-villain)
- **Hall of Echoes:** Becomes a second Loki without the legend rule. *strategic_judgment · high* — [loki-04](../interactions/loki-the-deceiver.md#loki-04-hall-of-echoes-as-a-second-loki)
- **Red Ghost, Intangible Genius:** Unblockable warded Villain that makes hasty Apes. *strategic_judgment · moderate* — [Loki_the_Deceiver_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Loki_the_Deceiver_Current_Cycle_Decisions_2026-10-14.md)

## Anti-goals and thematic constraints

- ✗ No generic Thassa's Oracle/Consultation or fast-combo packages (decisions, rejected under no-forced-homogenization).
- ✗ Avoid attack-trigger-only Villains as copy targets.
  - *strategic_judgment · high* — [Loki_the_Deceiver_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Loki_the_Deceiver_Current_Cycle_Decisions_2026-10-14.md)
- Theme: Marvel's Loki and his Villains: deception, copies and illusions.
  - *strategic_judgment · high* — [Loki_the_Deceiver_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Loki_the_Deceiver_Current_Cycle_Decisions_2026-10-14.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 508.4:** Creatures put onto the battlefield attacking were never declared as attackers. *fact · verified* — `cr:508.4`
- **CR 707.9b:** Copy exceptions (not legendary, Illusion) become copiable values. *fact · verified* — `cr:707.9b`

## Supporting features (heuristic, not identity)

- `{"hooks": ["Illusion synergy", "Villain synergy", "combat damage / attack triggers", "copying", "sacrifice", "tokens"], "hooked_cards": 41, "role_counts": {"counter": 3, "draw": 9, "protection": 3, "ramp": 14, "removal": 5, "tutor": 1, "wipe": 2}, "lands": 34, "edhrec_pages": ["loki-the-deceiver"]}` *heuristic · low*

## Provenance

- Seeded from: [Loki_the_Deceiver_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Loki_the_Deceiver_Current_Cycle_Decisions_2026-10-14.md) · [Loki_the_Deceiver_Approved_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Loki_the_Deceiver_Approved_2026-10-14.md) · [Loki_the_Deceiver_Whole_List_Audit_2026-10-14.csv](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Loki_the_Deceiver_Whole_List_Audit_2026-10-14.csv) · [Loki_the_Deceiver_Approved_2026-10-14.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Loki_the_Deceiver_Approved_2026-10-14.txt)
- Reviewed by: — (not yet reviewed by Cory)
