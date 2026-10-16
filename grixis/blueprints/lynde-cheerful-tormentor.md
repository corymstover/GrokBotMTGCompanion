# Blueprint — Lynde, Cheerful Tormentor

> **Commander Blueprint v1** (seeded, Bot cycle 53, 2026-10-16) for the canonical project list ([deck page](../decks/lynde-cheerful-tormentor.md), state `SOURCE_BASELINE`, list `lh1:7359723b249d034d…`). Machine-readable source: [`data/grixis/blueprints/lynde-cheerful-tormentor.json`](../../data/grixis/blueprints/lynde-cheerful-tormentor.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Lynde, Cheerful Tormentor** — Legendary Creature — Human Warlock

> Deathtouch  
> Whenever a Curse is put into your graveyard from the battlefield, return it to the battlefield attached to you at the beginning of the next end step.  
> At the beginning of your upkeep, you may attach a Curse attached to you to one of your opponents. If you do, draw two cards.

## Plan and commander role

- **Primary plan:** Curse recycling and control: land high-impact Curses on opponents, deliberately send your own Curses to the graveyard (Despotic Scepter, Claws of Gix, Braids, Perilous Research), let Lynde return them attached to you, then move one to an opponent each upkeep and draw two. *strategic_judgment · high*
- **Secondary:** Extra upkeeps (Paradox Haze, The Ninth Doctor, Obeka) multiply Lynde's draw-two and upkeep Curses; enchantment payoffs, Curse copies and premium Grixis interaction hold the table.
  - Evidence: [Lynde_Cheerful_Tormentor_Current_Cycle_Decisions_2026-10-14.md#L13](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lynde_Cheerful_Tormentor_Current_Cycle_Decisions_2026-10-14.md) · [lynde-01](../interactions/lynde-cheerful-tormentor.md#lynde-01-return-trigger-battlefield-to-graveyard-only-back-at-the-next-end-step-attached-to-you) · [lynde-02](../interactions/lynde-cheerful-tormentor.md#lynde-02-upkeep-move-one-curse-no-targeting-draw-two) · [lynde-04](../interactions/lynde-cheerful-tormentor.md#lynde-04-extra-upkeeps-paradox-haze-the-ninth-doctor-obeka--curse-of-bloodletting)
- **Commander role: central.** Lynde is the Curse recursion and the draw-two engine; the reset outlets only exist to feed her. *strategic_judgment · high*
- ⚠️ **Honest note:** There is no compact win: Commander Spellbook finds no combos in the list, so the deck wins slowly through stacked Curse damage. Returned Curses also hit you until Lynde moves them (M1 lynde-06).
  - Evidence: [Lynde_Cheerful_Tormentor_Current_Cycle_Decisions_2026-10-14.md#L19](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lynde_Cheerful_Tormentor_Current_Cycle_Decisions_2026-10-14.md) · [lynde-06](../interactions/lynde-cheerful-tormentor.md#lynde-06-curses-returned-to-you-hit-you-until-they-move)
- **Dependency level:** high *strategic_judgment · high* — [Lynde_Cheerful_Tormentor_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lynde_Cheerful_Tormentor_Current_Cycle_Decisions_2026-10-14.md)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 4 (Power Bracket 4 — Optimized (decisions).) | *fact · verified* | [Lynde_Cheerful_Tormentor_Current_Cycle_Decisions_2026-10-14.md#L19](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lynde_Cheerful_Tormentor_Current_Cycle_Decisions_2026-10-14.md) |
| GrokBot estimated ceiling | 4 (Bracket 4 ceiling, low end: premium interaction and Game Changers put it in B4, but there's no compact win and the Curse engine is slow. Agrees with the source.) | *strategic_judgment · high* | [Lynde_Cheerful_Tormentor_Current_Cycle_Decisions_2026-10-14.md#L19](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lynde_Cheerful_Tormentor_Current_Cycle_Decisions_2026-10-14.md) · [lynde-04](../interactions/lynde-cheerful-tormentor.md#lynde-04-extra-upkeeps-paradox-haze-the-ninth-doctor-obeka--curse-of-bloodletting) |
| Expected bracket (list as built) | 4 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Lynde__Cheerful_Tormentor` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 51, "2": 869, "3": 440, "4": 81, "5": 3}, "decks_with_bracket": 1444, "share_b4_plus": 0.058, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__lynde-cheerful-tormentor.json`

## Win conditions

- **curse-attrition** (natural): Damage and drain Curses (Bloodletting doubling, Torment of Scarabs, Restless Dead, Vengeance, Thirst) recycled every upkeep grind the table out. Cards: Curse of Bloodletting, Torment of Scarabs, Curse of the Restless Dead, Curse of Vengeance, Curse of Thirst, Curse of Death's Hold. Enablers: Lynde, Cheerful Tormentor, Paradox Haze. *strategic_judgment · high* — [Lynde_Cheerful_Tormentor_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lynde_Cheerful_Tormentor_Current_Cycle_Decisions_2026-10-14.md) · [lynde-04](../interactions/lynde-cheerful-tormentor.md#lynde-04-extra-upkeeps-paradox-haze-the-ninth-doctor-obeka--curse-of-bloodletting)
- **constellation-drain** (natural): Curses re-entering trigger constellation and enchantment payoffs (Doomwake Giant, Grim Guardian). Cards: Doomwake Giant, Grim Guardian, Ashiok's Reaper. Enablers: Lynde, Cheerful Tormentor. *strategic_judgment · moderate* — [Lynde_Cheerful_Tormentor_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lynde_Cheerful_Tormentor_Current_Cycle_Decisions_2026-10-14.md)

## Engines

- **curse-reset:** Lynde, Cheerful Tormentor, Despotic Scepter, Claws of Gix, Braids, Arisen Nightmare, Demon of Fate's Design, Perilous Research. Online when: A Curse you own goes from the battlefield to your graveyard. *fact · verified* — [lynde-01](../interactions/lynde-cheerful-tormentor.md#lynde-01-return-trigger-battlefield-to-graveyard-only-back-at-the-next-end-step-attached-to-you) · [lynde-03](../interactions/lynde-cheerful-tormentor.md#lynde-03-resetting-curses-despotic-scepter-claws-of-gix-braids-demon-of-fates-design-perilous-research)
- **extra-upkeeps:** Lynde, Cheerful Tormentor, Paradox Haze, The Ninth Doctor, Obeka, Splitter of Seconds, Curse of Bloodletting. Online when: A Curse attached to you at upkeep. *fact · verified* — [lynde-02](../interactions/lynde-cheerful-tormentor.md#lynde-02-upkeep-move-one-curse-no-targeting-draw-two) · [lynde-04](../interactions/lynde-cheerful-tormentor.md#lynde-04-extra-upkeeps-paradox-haze-the-ninth-doctor-obeka--curse-of-bloodletting)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:curses` | yes | 15 | Curses worth recycling. | 20: Curse of Bloodletting, Curse of Death's Hold, Curse of Disturbance, Curse of Echoes, Curse of Fool's Wisdom, Curse of Hospitality, Curse of Misfortunes, Curse of Obsession, Curse of Opulence, Curse of Shaken Faith, Curse of Surveillance, Curse of Thirst, Curse of Unbinding, Curse of Vengeance, Curse of Verbosity, Curse of the Restless Dead, Torment of Scarabs, Trespasser's Curse, Cruel Reality, Maddening Hex | — | *strategic_judgment · high* | [Lynde_Cheerful_Tormentor_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lynde_Cheerful_Tormentor_Current_Cycle_Decisions_2026-10-14.md) · [Lynde_Cheerful_Tormentor_Whole_List_Audit_2026-10-14.csv](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lynde_Cheerful_Tormentor_Whole_List_Audit_2026-10-14.csv) |
| `pkg:reset-outlets` | yes | 4 | Send your own Curses to the graveyard. | 5: Despotic Scepter, Claws of Gix, Braids, Arisen Nightmare, Demon of Fate's Design, Perilous Research | — | *strategic_judgment · high* | [Lynde_Cheerful_Tormentor_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lynde_Cheerful_Tormentor_Current_Cycle_Decisions_2026-10-14.md) · [lynde-03](../interactions/lynde-cheerful-tormentor.md#lynde-03-resetting-curses-despotic-scepter-claws-of-gix-braids-demon-of-fates-design-perilous-research) |
| `pkg:extra-upkeep` | yes | 3 | More Lynde upkeep triggers. | 3: Paradox Haze, The Ninth Doctor, Obeka, Splitter of Seconds | — | *strategic_judgment · high* | [Lynde_Cheerful_Tormentor_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lynde_Cheerful_Tormentor_Current_Cycle_Decisions_2026-10-14.md) · [lynde-04](../interactions/lynde-cheerful-tormentor.md#lynde-04-extra-upkeeps-paradox-haze-the-ninth-doctor-obeka--curse-of-bloodletting) |

## Key interactions

- **return-window:** Only battlefield-to-graveyard Curses return, attached to you at the next end step. (Lynde, Cheerful Tormentor) *fact · verified* — [lynde-01](../interactions/lynde-cheerful-tormentor.md#lynde-01-return-trigger-battlefield-to-graveyard-only-back-at-the-next-end-step-attached-to-you)
- **upkeep-move:** One Curse per upkeep moves without targeting (ignores hexproof) and draws two. (Lynde, Cheerful Tormentor) *fact · verified* — [lynde-02](../interactions/lynde-cheerful-tormentor.md#lynde-02-upkeep-move-one-curse-no-targeting-draw-two)
- **misfortunes-order:** Order Curse of Misfortunes before Lynde's move when it's on you. (Curse of Misfortunes, Lynde, Cheerful Tormentor) *fact · verified* — [lynde-05](../interactions/lynde-cheerful-tormentor.md#lynde-05-curse-of-misfortunes-on-yourself-order-it-before-lynde)
- **self-punish:** Returned Curses hit you until Lynde moves them. (Lynde, Cheerful Tormentor) *fact · verified* — [lynde-06](../interactions/lynde-cheerful-tormentor.md#lynde-06-curses-returned-to-you-hit-you-until-they-move)
- **harmless-on-you:** Fool's Wisdom, Surveillance and Unbinding are harmless parked on you. (Curse of Fool's Wisdom, Curse of Surveillance, Curse of Unbinding) *fact · verified* — [lynde-07](../interactions/lynde-cheerful-tormentor.md#lynde-07-harmless-on-yourself-fools-wisdom-surveillance-unbinding)

## Tutors and recursion

- Tutor target **Paradox Haze** via Demonic Tutor, Vampiric Tutor, Imperial Seal *strategic_judgment · moderate* — [Lynde_Cheerful_Tormentor_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lynde_Cheerful_Tormentor_Current_Cycle_Decisions_2026-10-14.md)
- Tutor target **Curse of Bloodletting** via Demonic Tutor, Vampiric Tutor *strategic_judgment · moderate* — [Lynde_Cheerful_Tormentor_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lynde_Cheerful_Tormentor_Current_Cycle_Decisions_2026-10-14.md)
- Recursion: Lynde, Cheerful Tormentor, Jeska's Will *strategic_judgment · moderate* — [Lynde_Cheerful_Tormentor_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lynde_Cheerful_Tormentor_Current_Cycle_Decisions_2026-10-14.md)

## Requirements

- **Interaction:** Mana Drain, Fierce Guardianship, Swan Song, Deadly Rollick, Toxic Deluge, Damnation, Cyclonic Rift.
- **Protection:** Deathtouch, Propaganda, Deflecting Swat, attack-tax Curses.
- **Mana:** 35 lands, Sol Ring, Ancient Tomb, Signets and Talismans.
- *strategic_judgment · moderate* — [Lynde_Cheerful_Tormentor_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lynde_Cheerful_Tormentor_Current_Cycle_Decisions_2026-10-14.md)

## Failure modes

- **enchantment-removal:** Enchantment wipes remove the whole Curse board at once. Mitigations: Lynde returns Curses that hit the graveyard; Counters. *strategic_judgment · high* — [Lynde_Cheerful_Tormentor_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lynde_Cheerful_Tormentor_Current_Cycle_Decisions_2026-10-14.md)
- **self-damage:** Curses parked on you hurt you. Mitigations: Move dangerous Curses first; Park harmless ones (lynde-07). *strategic_judgment · high* — [lynde-06](../interactions/lynde-cheerful-tormentor.md#lynde-06-curses-returned-to-you-hit-you-until-they-move)
- **slow-clock:** No compact win: a slow damage clock gives opponents time. Mitigations: Extra upkeeps; Premium interaction. *strategic_judgment · moderate* — [Lynde_Cheerful_Tormentor_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lynde_Cheerful_Tormentor_Current_Cycle_Decisions_2026-10-14.md)

## Identity core

- **Lynde, Cheerful Tormentor:** Returns dead Curses to you and moves one each upkeep for two cards. *fact · verified* — `oracle:Lynde, Cheerful Tormentor`
- **Paradox Haze:** Extra upkeep: another move and two more cards. *strategic_judgment · high* — [lynde-04](../interactions/lynde-cheerful-tormentor.md#lynde-04-extra-upkeeps-paradox-haze-the-ninth-doctor-obeka--curse-of-bloodletting)
- **Despotic Scepter:** One-mana repeatable Curse reset. *strategic_judgment · high* — [lynde-03](../interactions/lynde-cheerful-tormentor.md#lynde-03-resetting-curses-despotic-scepter-claws-of-gix-braids-demon-of-fates-design-perilous-research)
- **Curse of Bloodletting:** Doubles damage to the cursed player. *strategic_judgment · high* — [lynde-04](../interactions/lynde-cheerful-tormentor.md#lynde-04-extra-upkeeps-paradox-haze-the-ninth-doctor-obeka--curse-of-bloodletting)
- **The Ninth Doctor:** Cheap extra-upkeep engine. *strategic_judgment · moderate* — [lynde-04](../interactions/lynde-cheerful-tormentor.md#lynde-04-extra-upkeeps-paradox-haze-the-ninth-doctor-obeka--curse-of-bloodletting)

## Anti-goals and thematic constraints

- ✗ No generic combo packages added just to raise the theoretical ceiling (decisions L17).
- ✗ Prefer Curses that are good to recycle over narrow ones (decisions swaps).
  - *strategic_judgment · high* — [Lynde_Cheerful_Tormentor_Current_Cycle_Decisions_2026-10-14.md#L17](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lynde_Cheerful_Tormentor_Current_Cycle_Decisions_2026-10-14.md)
- Theme: Innistrad Curse witch: tormenting opponents with recycled Curses.
  - *strategic_judgment · high* — [Lynde_Cheerful_Tormentor_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lynde_Cheerful_Tormentor_Current_Cycle_Decisions_2026-10-14.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 303.4f:** A Curse returned by Lynde enters attached without targeting. *fact · verified* — `cr:303.4f`
- **CR 303.4e:** You keep control of a Curse attached to an opponent. *fact · verified* — `cr:303.4e`

## Supporting features (heuristic, not identity)

- `{"hooks": ["graveyard as a resource"], "hooked_cards": 2, "role_counts": {"counter": 3, "draw": 9, "protection": 1, "ramp": 8, "removal": 5, "tutor": 5, "wipe": 3}, "lands": 35, "edhrec_pages": ["lynde-cheerful-tormentor"]}` *heuristic · low*

## Provenance

- Seeded from: [Lynde_Cheerful_Tormentor_Current_Cycle_Decisions_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lynde_Cheerful_Tormentor_Current_Cycle_Decisions_2026-10-14.md) · [Lynde_Cheerful_Tormentor_Approved_2026-10-14.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Lynde_Cheerful_Tormentor_Approved_2026-10-14.md) · [Lynde_Cheerful_Tormentor_Whole_List_Audit_2026-10-14.csv](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Lynde_Cheerful_Tormentor_Whole_List_Audit_2026-10-14.csv) · [Lynde_Cheerful_Tormentor_Approved_2026-10-14.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Lynde_Cheerful_Tormentor_Approved_2026-10-14.txt)
- Reviewed by: — (not yet reviewed by Cory)
