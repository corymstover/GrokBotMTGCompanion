# Blueprint — Lord of Tresserhorn

> **Commander Blueprint v1** (seeded, Bot cycle 52, 2026-10-16) for the canonical project list ([deck page](../decks/lord-of-tresserhorn.md), state `SOURCE_BASELINE`, list `lh1:eae4578c6338f3c2…`). Machine-readable source: [`data/grixis/blueprints/lord-of-tresserhorn.json`](../../data/grixis/blueprints/lord-of-tresserhorn.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Lord of Tresserhorn** — Legendary Creature — Zombie

> When Lord of Tresserhorn enters, you lose 2 life, you sacrifice two creatures, and target opponent draws two cards.  
> {B}: Regenerate Lord of Tresserhorn.

## Plan and commander role

- **Primary plan:** Voltron/Infect with drawback suppression: neutralise Lord's enter trigger (Torpor Orb, Karn, Dress Down, Stifle, Tale's End), give the 10/4 haste and evasion, and convert 10 power into a kill with Tainted Strike/Phyresis (+ Kediss for every opponent), Uncaged Fury or Chandra's Ignition. *strategic_judgment · high*
- **Secondary:** Zombie/sacrifice backup: feed the trigger with recursive fodder (Gravecrawler, Reassembling Skeleton, Bloodghast) and win with Gravecrawler/Skeleton loops into Blood Artist, Zulaport Cutthroat or Goblin Bombardment.
  - Evidence: [Lord_of_Tresserhorn_Current_Cycle_Decisions_2026-10-14.md#L18](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lord_of_Tresserhorn_Current_Cycle_Decisions_2026-10-14.md) · [tresserhorn-02](../interactions/lord-of-tresserhorn.md#tresserhorn-02-turning-off-the-drawback-torpor-orb-karn-dress-down-stifle-tales-end) · [tresserhorn-05](../interactions/lord-of-tresserhorn.md#tresserhorn-05-infect-lord-tainted-strike-or-phyresis-then-kediss)
- **Commander role: central.** Lord's 10 power is the kill; the infect and double-strike cards only work on him. *strategic_judgment · high*
- ⚠️ **Honest note:** The enter trigger is a real cost: lose 2, sacrifice two creatures (Lord himself if needed; regeneration doesn't help) and an opponent draws two (M1 tresserhorn-01). The source admits the Torpor Orb/Karn slots trade away flexibility (tresserhorn-13). The sacrifice loops win without him.
  - Evidence: [Lord_of_Tresserhorn_Current_Cycle_Decisions_2026-10-14.md#L20](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lord_of_Tresserhorn_Current_Cycle_Decisions_2026-10-14.md) · [tresserhorn-01](../interactions/lord-of-tresserhorn.md#tresserhorn-01-the-enter-trigger-life-loss-two-sacrifices-possibly-lord-opponent-draws) · [tresserhorn-13](../interactions/lord-of-tresserhorn.md#tresserhorn-13-torpor-orb-and-karn-what-the-list-gave-up)
- **Dependency level:** high *strategic_judgment · high* — [Lord_of_Tresserhorn_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lord_of_Tresserhorn_Current_Cycle_Decisions_2026-10-14.md)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 4 (Power Bracket 4 — Optimized (decisions).) | *fact · verified* | [Lord_of_Tresserhorn_Current_Cycle_Decisions_2026-10-14.md#L35](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lord_of_Tresserhorn_Current_Cycle_Decisions_2026-10-14.md) |
| GrokBot estimated ceiling | 4 (Bracket 4 ceiling: two-card infect kills on the commander and many sacrifice loops, limited by a punishing ETB and a fragile 10/4. Agrees with the source.) | *strategic_judgment · high* | [Lord_of_Tresserhorn_Current_Cycle_Decisions_2026-10-14.md#L35](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lord_of_Tresserhorn_Current_Cycle_Decisions_2026-10-14.md) · `spellbook:264-1218` |
| Expected bracket (list as built) | 4 (computed floor 3) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Lord_of_Tresserhorn` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 20, "2": 123, "3": 80, "4": 28, "5": 4}, "decks_with_bracket": 255, "share_b4_plus": 0.125, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__lord-of-tresserhorn.json`

## Win conditions

- **infect-lord** (combo): Lord with Tainted Strike or Phyresis is a 10-poison hit; add Kediss and one connection poisons every opponent. Cards: Lord of Tresserhorn, Tainted Strike, Phyresis, Kediss, Emberclaw Familiar. Enablers: Brotherhood Regalia, Rogue's Passage, Shizo, Death's Storehouse. *fact · verified* — `spellbook:264-1218` · `spellbook:264-4651` · `spellbook:1218-2822` · `spellbook:2822-4651` · [tresserhorn-05](../interactions/lord-of-tresserhorn.md#tresserhorn-05-infect-lord-tainted-strike-or-phyresis-then-kediss)
- **big-hits** (natural): Uncaged Fury makes 22 commander damage; Chandra's Ignition or Pain for All turns 10 power into board-wide (infect) damage. Cards: Uncaged Fury, Chandra's Ignition, Pain for All. Enablers: Lord of Tresserhorn. *fact · verified* — [tresserhorn-06](../interactions/lord-of-tresserhorn.md#tresserhorn-06-noncombat-infect-chandras-ignition-and-pain-for-all) · [tresserhorn-07](../interactions/lord-of-tresserhorn.md#tresserhorn-07-uncaged-fury-22-commander-damage)
- **sac-loops** (combo): Gravecrawler (Lord is the needed Zombie) or Reassembling Skeleton with Phyrexian/Ashnod's Altar, Rooftop Storm or Pitiless Plunderer, into Blood Artist, Zulaport Cutthroat or Goblin Bombardment. Cards: Gravecrawler, Reassembling Skeleton, Phyrexian Altar, Ashnod's Altar, Rooftop Storm, Pitiless Plunderer, Blood Artist, Zulaport Cutthroat, Goblin Bombardment, Warren Soultrader. Enablers: Lord of Tresserhorn. *fact · verified* — `spellbook:2577-4050` · `spellbook:2034-2452-2577` · `spellbook:2292-2577-4871` · `spellbook:1580-4050-4871` · `spellbook:1385-2577-5670` · `spellbook:2577-2842-5670` · `spellbook:2452-2577-5147` · [tresserhorn-11](../interactions/lord-of-tresserhorn.md#tresserhorn-11-gravecrawler-loops-lord-himself-is-the-other-zombie) · [tresserhorn-12](../interactions/lord-of-tresserhorn.md#tresserhorn-12-reassembling-skeleton-loops-without-a-zombie)

## Engines

- **drawback-suppression:** Torpor Orb, Karn, Argent Defender, Dress Down, Stifle, Tale's End. Online when: In place before Lord enters, or held up for the trigger. *fact · verified* — [tresserhorn-02](../interactions/lord-of-tresserhorn.md#tresserhorn-02-turning-off-the-drawback-torpor-orb-karn-dress-down-stifle-tales-end)
- **recursive-fodder:** Gravecrawler, Reassembling Skeleton, Bloodghast, Nether Traitor, Bitterblossom, Shambling Ghast, Headless Rider. Online when: Fodder in play when the enter trigger resolves. *fact · verified* — [tresserhorn-01](../interactions/lord-of-tresserhorn.md#tresserhorn-01-the-enter-trigger-life-loss-two-sacrifices-possibly-lord-opponent-draws) · [tresserhorn-11](../interactions/lord-of-tresserhorn.md#tresserhorn-11-gravecrawler-loops-lord-himself-is-the-other-zombie)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:suppression` | yes | 5 | Turn off or answer the enter trigger. | 5: Torpor Orb, Karn, Argent Defender, Dress Down, Stifle, Tale's End | — | *strategic_judgment · high* | [Lord_of_Tresserhorn_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lord_of_Tresserhorn_Current_Cycle_Decisions_2026-10-14.md) · [tresserhorn-02](../interactions/lord-of-tresserhorn.md#tresserhorn-02-turning-off-the-drawback-torpor-orb-karn-dress-down-stifle-tales-end) |
| `pkg:evasion-haste-protection` | yes | 10 | Make the 10/4 connect the turn it lands. | 13: Brotherhood Regalia, Shizo, Death's Storehouse, Rogue's Passage, Wonder, Anger, Arena of Glory, Swiftfoot Boots, Lightning Greaves, Not of This World, Slip Out the Back, Stubborn Denial, Deflecting Swat, Cover of Darkness | — | *strategic_judgment · high* | [Lord_of_Tresserhorn_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lord_of_Tresserhorn_Current_Cycle_Decisions_2026-10-14.md) |
| `pkg:ten-power-conversion` | yes | 5 | Turn 10 power into a kill. | 7: Tainted Strike, Phyresis, Kediss, Emberclaw Familiar, Chandra's Ignition, Uncaged Fury, Pain for All, Shadowspear | — | *strategic_judgment · high* | [Lord_of_Tresserhorn_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lord_of_Tresserhorn_Current_Cycle_Decisions_2026-10-14.md) |

## Key interactions

- **etb-cost:** Lose 2, sacrifice two creatures (Lord too if needed), opponent draws two. (Lord of Tresserhorn) *fact · verified* — [tresserhorn-01](../interactions/lord-of-tresserhorn.md#tresserhorn-01-the-enter-trigger-life-loss-two-sacrifices-possibly-lord-opponent-draws)
- **suppression-timing:** Torpor/Karn/Dress Down must be in place first; Stifle/Tale's End counter the trigger. (Torpor Orb, Karn, Argent Defender, Dress Down, Stifle, Tale's End) *fact · verified* — [tresserhorn-02](../interactions/lord-of-tresserhorn.md#tresserhorn-02-turning-off-the-drawback-torpor-orb-karn-dress-down-stifle-tales-end)
- **regen-scope:** Regeneration only replaces destruction, not sacrifice. (Lord of Tresserhorn) *fact · verified* — [tresserhorn-03](../interactions/lord-of-tresserhorn.md#tresserhorn-03-regeneration-only-replaces-destruction)
- **greaves-shroud:** Greaves' shroud blocks your own targeted Lord spells; Brotherhood Regalia doesn't. (Lightning Greaves, Brotherhood Regalia) *fact · verified* — [tresserhorn-08](../interactions/lord-of-tresserhorn.md#tresserhorn-08-lightning-greaves-shroud-blocks-your-own-lord-spells-brotherhood-regalia-doesnt)
- **rooftop:** Rooftop Storm makes Lord cost {0} plus tax. (Rooftop Storm, Lord of Tresserhorn) *fact · verified* — [tresserhorn-10](../interactions/lord-of-tresserhorn.md#tresserhorn-10-rooftop-storm-makes-lord-cost-0-plus-tax)

## Tutors and recursion

- Tutor target **Tainted Strike** via Demonic Tutor, Vampiric Tutor *strategic_judgment · high* — `spellbook:264-1218`
- Tutor target **Torpor Orb** via Demonic Tutor *strategic_judgment · moderate* — [Lord_of_Tresserhorn_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lord_of_Tresserhorn_Current_Cycle_Decisions_2026-10-14.md)
- Recursion: Gravecrawler, Reassembling Skeleton, Bloodghast, Nether Traitor, Undead Augur, Jadar, Ghoulcaller of Nephalia *strategic_judgment · moderate* — [Lord_of_Tresserhorn_Whole_List_Audit_2026-10-14.csv](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lord_of_Tresserhorn_Whole_List_Audit_2026-10-14.csv)

## Requirements

- **Interaction:** Cheap removal and stack interaction (Terminate, Deadly Rollick, Sheoldred's Edict, Stifle, Muddle the Mixture, Toxic Deluge).
- **Protection:** Boots/Greaves, Not of This World, Slip Out the Back, Stubborn Denial, Deflecting Swat.
- **Mana:** Four-mana commander; Sol Ring, Signets, Talismans.
- *strategic_judgment · moderate* — [Lord_of_Tresserhorn_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lord_of_Tresserhorn_Current_Cycle_Decisions_2026-10-14.md)

## Failure modes

- **drawback:** Unsuppressed trigger costs two creatures, 2 life and gives an opponent two cards. Mitigations: Suppression package; Recursive fodder. *strategic_judgment · high* — [tresserhorn-01](../interactions/lord-of-tresserhorn.md#tresserhorn-01-the-enter-trigger-life-loss-two-sacrifices-possibly-lord-opponent-draws)
- **chump-removal:** A 10/4 dies to most removal and can be chump-blocked. Mitigations: Evasion and protection suite. *strategic_judgment · high* — [Lord_of_Tresserhorn_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lord_of_Tresserhorn_Current_Cycle_Decisions_2026-10-14.md)
- **torpor-self:** Torpor Orb also stops your own ETB creatures. Mitigations: Karn as a removable alternative. *strategic_judgment · moderate* — [tresserhorn-13](../interactions/lord-of-tresserhorn.md#tresserhorn-13-torpor-orb-and-karn-what-the-list-gave-up)

## Identity core

- **Lord of Tresserhorn:** Four-mana 10/4 with a punishing enter trigger and regeneration. *fact · verified* — `oracle:Lord of Tresserhorn`
- **Tainted Strike:** 10 infect damage from one hit. *strategic_judgment · high* — [tresserhorn-05](../interactions/lord-of-tresserhorn.md#tresserhorn-05-infect-lord-tainted-strike-or-phyresis-then-kediss)
- **Torpor Orb:** Permanently turns off the enter trigger. *strategic_judgment · high* — [tresserhorn-02](../interactions/lord-of-tresserhorn.md#tresserhorn-02-turning-off-the-drawback-torpor-orb-karn-dress-down-stifle-tales-end)
- **Kediss, Emberclaw Familiar:** Copies Lord's damage to every opponent. *strategic_judgment · high* — [tresserhorn-05](../interactions/lord-of-tresserhorn.md#tresserhorn-05-infect-lord-tainted-strike-or-phyresis-then-kediss)
- **Gravecrawler:** Recursive fodder and loop piece; Lord is its Zombie. *strategic_judgment · moderate* — [tresserhorn-11](../interactions/lord-of-tresserhorn.md#tresserhorn-11-gravecrawler-loops-lord-himself-is-the-other-zombie)

## Anti-goals and thematic constraints

- ✗ Current optimized Lord evidence is Infect/Voltron, not sacrifice; keep the sacrifice shell as backup (decisions L33).
- ✗ Dictate of Erebos cut on the adversarial pass (decisions).
  - *strategic_judgment · high* — [Lord_of_Tresserhorn_Current_Cycle_Decisions_2026-10-14.md#L33](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lord_of_Tresserhorn_Current_Cycle_Decisions_2026-10-14.md)
- Theme: Zombie lord of Tresserhorn: undead fodder and one enormous threat.
  - *strategic_judgment · moderate* — [Lord_of_Tresserhorn_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lord_of_Tresserhorn_Current_Cycle_Decisions_2026-10-14.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 701.19a:** Regeneration replaces destruction only. *fact · verified* — `cr:701.19a`
- **CR 702.90b:** Infect damage to players is poison counters. *fact · verified* — `cr:702.90b`

## Supporting features (heuristic, not identity)

- `{"hooks": ["sacrifice"], "hooked_cards": 20, "role_counts": {"counter": 5, "draw": 4, "protection": 4, "ramp": 12, "removal": 5, "tutor": 2, "wipe": 2}, "lands": 35, "edhrec_pages": ["lord-of-tresserhorn"]}` *heuristic · low*

## Provenance

- Seeded from: [Lord_of_Tresserhorn_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lord_of_Tresserhorn_Current_Cycle_Decisions_2026-10-14.md) · [Lord_of_Tresserhorn_Approved_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Lord_of_Tresserhorn_Approved_2026-10-14.md) · [Lord_of_Tresserhorn_Whole_List_Audit_2026-10-14.csv](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lord_of_Tresserhorn_Whole_List_Audit_2026-10-14.csv) · [Lord_of_Tresserhorn_Approved_2026-10-14.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Lord_of_Tresserhorn_Approved_2026-10-14.txt)
- Reviewed by: — (not yet reviewed by Cory)
