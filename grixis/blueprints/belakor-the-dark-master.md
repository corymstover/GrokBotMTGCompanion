# Blueprint — Be'lakor, the Dark Master

> **Commander Blueprint v1** (seeded, Bot cycle 50, 2026-10-16) for the canonical project list ([deck page](../decks/belakor-the-dark-master.md), state `SOURCE_BASELINE`, list `lh1:ece0a3ce87a761d8…`). Machine-readable source: [`data/grixis/blueprints/belakor-the-dark-master.json`](../../data/grixis/blueprints/belakor-the-dark-master.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Be'lakor, the Dark Master** — Legendary Creature — Demon Noble

> Flying  
> Prince of Chaos — When Be'lakor enters, you draw X cards and you lose X life, where X is the number of Demons you control.  
> Lord of Torment — Whenever another Demon you control enters, it deals damage equal to its power to any target.

## Plan and commander role

- **Primary plan:** Demon tribal: assemble a board of high-power Demons, turn each Demon arrival into direct damage equal to its power, and refill with Be'lakor's ETB draw; multiply arrivals with Panharmonicon, Roaming Throne and copy effects. *strategic_judgment · high*
- **Secondary:** Cheat and reanimate big Demons (Sneak Attack, Reanimate, Patriarch's Bidding, Whip of Erebos) and the Liliana's Contract alternate win.
  - Evidence: [Be_lakor__the_Dark_Master_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Be_lakor__the_Dark_Master_v1.md) · [belakor-01](../interactions/belakor-the-dark-master.md#belakor-01-prince-of-chaos-counts-demons-on-resolution) · [belakor-02](../interactions/belakor-the-dark-master.md#belakor-02-lord-of-torment-another-demon-its-own-power-last-known-information)
- **Commander role: central.** Lord of Torment converts every Demon ETB into removal or face damage, and Prince of Chaos refuels; copies of Be'lakor (Spark Double, Rite of Replication) are the biggest turns. *strategic_judgment · high*
- ⚠️ **Honest note:** Six mana and needs other Demons; the draw costs life equal to cards drawn. Slow without ramp.
  - Evidence: [Be_lakor__the_Dark_Master_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Be_lakor__the_Dark_Master_v1.md) · [belakor-01](../interactions/belakor-the-dark-master.md#belakor-01-prince-of-chaos-counts-demons-on-resolution) · [belakor-13](../interactions/belakor-the-dark-master.md#belakor-13-commander-tax-at-six-mana)
- **Dependency level:** high *strategic_judgment · high* — [Be_lakor__the_Dark_Master_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Be_lakor__the_Dark_Master_v1.md) · [belakor-02](../interactions/belakor-the-dark-master.md#belakor-02-lord-of-torment-another-demon-its-own-power-last-known-information)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | — (none stated) (No source ceiling stated in the working blueprint, approval or approval-gate dossier (checked Bot cycle 50).) | *fact · high* | [Be_lakor__the_Dark_Master_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Be_lakor__the_Dark_Master_v1.md) · [Be_lakor_the_Dark_Master_Approved_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Be_lakor_the_Dark_Master_Approved_2026-10-13.md) · [Be_lakor_the_Dark_Master_Approval_Gate_Dossier_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/evidence/Be_lakor_the_Dark_Master_Approval_Gate_Dossier_2026-10-13.md) |
| GrokBot estimated ceiling | 4 (Bracket 4: a two-card Spellbook kill (Rite on Be'lakor) and Sneak Attack/reanimation, but a six-mana tribal engine with no cEDH speed.) | *strategic_judgment · high* | [belakor-03](../interactions/belakor-the-dark-master.md#belakor-03-rite-of-replication-on-belakor-legend-rule-then-the-damage) · `spellbook:1744-4071` · [Be_lakor__the_Dark_Master_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Be_lakor__the_Dark_Master_v1.md) |
| Expected bracket (list as built) | 4 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Be_lakor__the_Dark_Master` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | — (no source ceiling) | | |

- EDHREC: `{"bracket_counts": {"1": 19, "2": 1338, "3": 1610, "4": 542, "5": 35}, "decks_with_bracket": 3544, "share_b4_plus": 0.163, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__belakor-the-dark-master.json`

## Win conditions

- **rite-on-belakor** (combo): Kicked Rite of Replication on Be'lakor: five copies each trigger Lord of Torment for the others (≈150 damage). Cards: Rite of Replication, Be'lakor, the Dark Master. Enablers: Molten Echoes. *fact · moderate* — [belakor-03](../interactions/belakor-the-dark-master.md#belakor-03-rite-of-replication-on-belakor-legend-rule-then-the-damage) · `spellbook:1744-4071`
- **demon-etb-burn** (natural): Demon arrivals deal damage equal to power; doubled by Panharmonicon/Roaming Throne and amplified by Archfiend of Despair/Bloodletter. Cards: Be'lakor, the Dark Master, Panharmonicon, Roaming Throne, Archfiend of Despair, Bloodletter of Aclazotz. Enablers: Sneak Attack, Patriarch's Bidding. *strategic_judgment · high* — [Be_lakor__the_Dark_Master_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Be_lakor__the_Dark_Master_v1.md) · [belakor-02](../interactions/belakor-the-dark-master.md#belakor-02-lord-of-torment-another-demon-its-own-power-last-known-information)
- **lilianas-contract** (alternate): Liliana's Contract with four differently named Demons at upkeep. Cards: Liliana's Contract. Enablers: Kindred Discovery. *fact · verified* — [belakor-06](../interactions/belakor-the-dark-master.md#belakor-06-lilianas-contract-needs-four-different-names)

## Engines

- **lord-of-torment:** Be'lakor, the Dark Master, Panharmonicon, Roaming Throne, Spark Double. Online when: Another Demon enters under your control. *fact · verified* — [belakor-02](../interactions/belakor-the-dark-master.md#belakor-02-lord-of-torment-another-demon-its-own-power-last-known-information) · [belakor-05](../interactions/belakor-the-dark-master.md#belakor-05-roaming-throne-and-panharmonicon-stack)
- **cheat-and-copy:** Sneak Attack, Molten Echoes, Reflections of Littjara, Whip of Erebos, Kardur, Doomscourge. Online when: Demons in hand or graveyard. *fact · verified* — [belakor-10](../interactions/belakor-the-dark-master.md#belakor-10-copy-enablers-molten-echoes-and-reflections-of-littjara) · [belakor-11](../interactions/belakor-the-dark-master.md#belakor-11-cheat-in-demons-still-trigger-lord)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:high-power-demons` | yes | 15 | Demons whose power makes Lord of Torment lethal. | 18: Archfiend of Depravity, Archfiend of Despair, Balor, Bloodthirster, Burning-Rune Demon, Chaos Defiler, Doom Whisperer, Great Unclean One, Lord of Change, Orcus, Prince of Undeath, Rakdos, Lord of Riots, Rakdos, the Showstopper, Rune-Scarred Demon, Valgavoth, Terror Eater, Vilis, Broker of Blood, Kardur, Doomscourge, Dream Devourer, Abyssal Harvester | Varragoth, Bloodsky Sire | *strategic_judgment · high* | [Be_lakor__the_Dark_Master_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Be_lakor__the_Dark_Master_v1.md) |
| `pkg:etb-multipliers` | yes | 5 | Double or copy Demon arrivals. | 6: Panharmonicon, Roaming Throne, Molten Echoes, Reflections of Littjara, Rite of Replication, Spark Double | — | *strategic_judgment · high* | [Be_lakor__the_Dark_Master_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Be_lakor__the_Dark_Master_v1.md) |
| `pkg:cheat-reanimate` | yes | 5 | Put six- to eight-drop Demons into play cheaply. | 7: Sneak Attack, Reanimate, Patriarch's Bidding, Whip of Erebos, Herald of Slaanesh, Heartless Summoning, Dark Ritual | — | *strategic_judgment · high* | [Be_lakor__the_Dark_Master_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Be_lakor__the_Dark_Master_v1.md) |
| `pkg:damage-amplifiers` | optional | 2 | Turn Lord damage into bigger life loss. | 3: Archfiend of Despair, Bloodletter of Aclazotz, Sower of Discord | — | *strategic_judgment · high* | [Be_lakor__the_Dark_Master_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Be_lakor__the_Dark_Master_v1.md) · [belakor-08](../interactions/belakor-the-dark-master.md#belakor-08-bloodletter-doubles-life-loss-sower-of-discord-passes-it-on) |

## Key interactions

- **prince-on-resolution:** Draw/lose X counts Demons on resolution (Be'lakor counts himself). (Be'lakor, the Dark Master) *fact · verified* — [belakor-01](../interactions/belakor-the-dark-master.md#belakor-01-prince-of-chaos-counts-demons-on-resolution)
- **lord-lki:** Another Demon entering deals damage equal to its power (last known information). (Be'lakor, the Dark Master) *fact · verified* — [belakor-02](../interactions/belakor-the-dark-master.md#belakor-02-lord-of-torment-another-demon-its-own-power-last-known-information)
- **spark-double:** Spark Double copies Be'lakor without the legend rule. (Spark Double) *fact · verified* — [belakor-04](../interactions/belakor-the-dark-master.md#belakor-04-spark-double-copies-belakor-without-the-legend-rule)
- **heartless-shrinks:** Heartless Summoning shrinks Lord damage by one per Demon. (Heartless Summoning) *fact · verified* — [belakor-07](../interactions/belakor-the-dark-master.md#belakor-07-heartless-summoning-shrinks-lord-damage)
- **life-loss-doubling:** Bloodletter doubles life loss; Sower of Discord passes damage on; Vilis draws off Be'lakor's own life loss. (Bloodletter of Aclazotz, Sower of Discord, Vilis, Broker of Blood) *fact · verified* — [belakor-08](../interactions/belakor-the-dark-master.md#belakor-08-bloodletter-doubles-life-loss-sower-of-discord-passes-it-on) · [belakor-09](../interactions/belakor-the-dark-master.md#belakor-09-vilis-draws-for-belakors-life-loss)

## Tutors and recursion

- Tutor target **Rite of Replication** via Demonic Tutor, Vampiric Tutor *strategic_judgment · high* — [belakor-03](../interactions/belakor-the-dark-master.md#belakor-03-rite-of-replication-on-belakor-legend-rule-then-the-damage)
- Tutor target **Sneak Attack** via Demonic Tutor, Vampiric Tutor *strategic_judgment · moderate* — [Be_lakor__the_Dark_Master_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Be_lakor__the_Dark_Master_v1.md)
- Recursion: Reanimate, Patriarch's Bidding, Whip of Erebos, Unholy Annex // Ritual Chamber *strategic_judgment · moderate* — [Be_lakor__the_Dark_Master_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Be_lakor__the_Dark_Master_v1.md)

## Requirements

- **Interaction:** Counters for the big turn plus sweepers (Blasphemous Act, Toxic Deluge) to buy time.
- **Protection:** Fierce Guardianship, Deflecting Swat; Be'lakor is six mana so recasting is costly.
- **Mana:** Rituals and rocks to reach six; 33-35 lands.
- *strategic_judgment · moderate* — [Be_lakor__the_Dark_Master_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Be_lakor__the_Dark_Master_v1.md) · [Be_lakor_the_Dark_Master_Approval_Gate_Dossier_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/evidence/Be_lakor_the_Dark_Master_Approval_Gate_Dossier_2026-10-13.md)

## Failure modes

- **clunky-curve:** Too many six- to eight-mana Demons: slow, dead hands. Mitigations: Sneak Attack; Dream Devourer; Rituals. *strategic_judgment · high* — [Be_lakor__the_Dark_Master_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Be_lakor__the_Dark_Master_v1.md)
- **self-life-loss:** Prince of Chaos and Demon drawbacks drain your own life. Mitigations: Whip of Erebos lifelink. *strategic_judgment · moderate* — [belakor-01](../interactions/belakor-the-dark-master.md#belakor-01-prince-of-chaos-counts-demons-on-resolution)
- **commander-tax:** Removal on a six-drop commander quickly becomes prohibitive. Mitigations: Spark Double and copies as backups. *strategic_judgment · moderate* — [belakor-13](../interactions/belakor-the-dark-master.md#belakor-13-commander-tax-at-six-mana)

## Identity core

- **Be'lakor, the Dark Master:** Only source of Demon-ETB damage and the tribal draw. *fact · verified* — `oracle:Be'lakor, the Dark Master`
- **Rite of Replication:** Kicked on Be'lakor it is a one-card table kill. *strategic_judgment · high* — [belakor-03](../interactions/belakor-the-dark-master.md#belakor-03-rite-of-replication-on-belakor-legend-rule-then-the-damage)
- **Panharmonicon:** Doubles every Lord of Torment trigger. *strategic_judgment · high* — [belakor-05](../interactions/belakor-the-dark-master.md#belakor-05-roaming-throne-and-panharmonicon-stack)
- **Spark Double:** Approved swap: a second Be'lakor without the legend rule. *strategic_judgment · high* — [Be_lakor_the_Dark_Master_Approved_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Be_lakor_the_Dark_Master_Approved_2026-10-13.md) · [belakor-04](../interactions/belakor-the-dark-master.md#belakor-04-spark-double-copies-belakor-without-the-legend-rule)
- **Sneak Attack:** Puts the eight-drops in for one red and triggers Lord. *strategic_judgment · moderate* — [Be_lakor__the_Dark_Master_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Be_lakor__the_Dark_Master_v1.md)

## Anti-goals and thematic constraints

- ✗ Don't convert into generic Grixis reanimator/control.
- ✗ Don't force a cEDH shell; the plan is Demon density and power.
  - *strategic_judgment · high* — [Be_lakor__the_Dark_Master_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Be_lakor__the_Dark_Master_v1.md)
- Theme: Demon tribal; Warhammer daemons (Lord of Change, Great Unclean One, Bloodthirster) are on-theme.
  - *strategic_judgment · high* — [Be_lakor__the_Dark_Master_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Be_lakor__the_Dark_Master_v1.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 704.5j:** Copies of Be'lakor hit the legend rule unless renamed (Spark Double). *fact · verified* — `cr:704.5j`
- **CR 702.139:** Gyruda is in the 99, not a companion; the deck doesn't meet Gyruda's companion restriction. *fact · verified* — `cr:702.139` · [belakor-12](../interactions/belakor-the-dark-master.md#belakor-12-gyruda-in-the-99-not-as-companion)

## Supporting features (heuristic, not identity)

- `{"hooks": ["Demon synergy", "enters triggers"], "hooked_cards": 30, "role_counts": {"counter": 2, "draw": 7, "protection": 1, "ramp": 8, "removal": 5, "tutor": 4, "wipe": 3}, "lands": 36, "edhrec_pages": ["belakor-the-dark-master"]}` *heuristic · low*

## Provenance

- Seeded from: [Be_lakor__the_Dark_Master_v1.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Be_lakor__the_Dark_Master_v1.md) · [Be_lakor_the_Dark_Master_Approved_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Be_lakor_the_Dark_Master_Approved_2026-10-13.md) · [Be_lakor_the_Dark_Master_Approval_Gate_Dossier_2026-10-13.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/evidence/Be_lakor_the_Dark_Master_Approval_Gate_Dossier_2026-10-13.md) · [Be_lakor_the_Dark_Master_Approved_2026-10-13.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Be_lakor_the_Dark_Master_Approved_2026-10-13.txt)
- Reviewed by: — (not yet reviewed by Cory)
