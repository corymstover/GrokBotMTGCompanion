# Blueprint — Tresserhorn's Lord, Returned

> **Commander Blueprint v1** (cory_reviewed, Bot cycle 55, 2026-10-16) for the canonical project list ([deck page](../decks/tresserhorns-lord-returned.md), state `PENDING_RELEASE`, list `lh1:2d34a55fec543ac9…`). Machine-readable source: [`data/grixis/blueprints/tresserhorns-lord-returned.json`](../../data/grixis/blueprints/tresserhorns-lord-returned.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Tresserhorn's Lord, Returned** — Legendary Creature — Zombie Noble

> Trample, indestructible  
> When Tresserhorn's Lord enters, sacrifice him unless you sacrifice three creatures, pay 3 life, and have target opponent draw three cards.  
> Whenever you sacrifice a creature, draw a card.

## Plan and commander role

- **Primary plan:** Sacrifice card-draw aristocrats: build cheap repeatable fodder, resolve Tresserhorn while paying his three-creature ETB (three draw triggers), then turn every sacrifice into a card and close with drain payoffs or loops (The Locust God + a free outlet, Gravecrawler + Phyrexian Altar or Plunderer). *strategic_judgment · high*
- **Secondary:** The 10/4 trample, indestructible commander as a combat threat with Infantry Shield, Wand of Orcus, My Precious and Chandra's Ignition.
  - Evidence: [Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md#L13](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md) · [Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md#L50](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md) · [Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md#L54](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md) · [Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md#L60](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md)
- **Commander role: central.** Tresserhorn is the card-draw engine for every sacrifice, a Zombie for Gravecrawler, and a 10-power threat. *strategic_judgment · high*
- ⚠️ **Honest note:** Commander-native: 6 of the 21 Spellbook combos need him (The Locust God + an outlet + Tresserhorn), and he is the Zombie that lets Gravecrawler loop. The ETB gives an opponent three cards. Legality conflict for Cory: the source says the future-release exception is stale and the card is legal now (verification L48, L67; approvals L18), but the Scryfall cache used by the registry shows it not_legal (mbc, released 2026-10-19), and the Madcap Jester source gives 2026-11-13 for the same set. The registry keeps PENDING_RELEASE and the exception row; this blueprint changes neither.
  - Evidence: [Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md#L54](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md) · [Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md#L48](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md) · [Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md#L67](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md) · [Tresserhorn_s_Lord_Returned_Approved_2026-10-15.md#L18](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Tresserhorn_s_Lord_Returned_Approved_2026-10-15.md) · `spellbook:1339-2292-7920` · `registry:data/grixis/blueprint_reviews.json#tresserhorns-lord-returned`
- **Dependency level:** high *strategic_judgment · high* — `spellbook:1339-2292-7920` · `registry:data/grixis/blueprint_reviews.json#tresserhorns-lord-returned`

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 4 (Power Bracket 4 — Optimized (recovered from the verification record; the registry's extractor found none).) | *fact · verified* | [Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md#L15](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md) |
| GrokBot estimated ceiling | 4 (Bracket 4: many deterministic loops and high card throughput, but the ETB cost and the cards it gives away keep it below cEDH. Agrees with the recovered source ceiling. The registry bracket floor is 3 (fewer Game Changers); the expected bracket is 4.) | *strategic_judgment · high* | [Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md#L15](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md) · `spellbook:1339-2292-7920` · `registry:data/grixis/blueprint_reviews.json#tresserhorns-lord-returned` |
| Expected bracket (list as built) | 4 (computed floor 3) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Tresserhorn_s_Lord__Returned` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"2": 19, "3": 45, "4": 10, "5": 2}, "decks_with_bracket": 76, "share_b4_plus": 0.158, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__tresserhorns-lord-returned.json`

## Win conditions

- **locust-loop** (combo): The Locust God + Tresserhorn + a free outlet: each draw makes an Insect, and sacrificing it draws again; Goblin Bombardment or a drain payoff kills. Cards: The Locust God, Tresserhorn's Lord, Returned, Viscera Seer, Carrion Feeder, Phyrexian Altar, Ashnod's Altar, Goblin Bombardment. Enablers: Diabolic Intent, Demonic Tutor, Vampiric Tutor. *strategic_judgment · high* — `spellbook:1339-2292-7920` · `spellbook:1339-4050-7920` · `spellbook:1339-5147-7920` · [Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md#L54](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md)
- **gravecrawler-loops** (combo): Gravecrawler with Phyrexian Altar, Pitiless Plunderer + outlet, or Warren Soultrader + Blood Artist / Zulaport / Bastion. Cards: Gravecrawler, Phyrexian Altar, Pitiless Plunderer, Warren Soultrader, Blood Artist, Zulaport Cutthroat, Bastion of Remembrance. Enablers: Tresserhorn's Lord, Returned. *strategic_judgment · high* — `spellbook:2577-4050` · `spellbook:2034-2577-4871` · `spellbook:2577-2842-5670` · [Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md#L51](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md) · [Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md#L52](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md) · [Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md#L53](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md)
- **commander-combat** (natural): 10-power trample, indestructible Tresserhorn with Infantry Shield or Wand of Orcus. Cards: Tresserhorn's Lord, Returned, Infantry Shield, Wand of Orcus, My Precious // Allure of Power. Enablers: Lightning Greaves. *strategic_judgment · moderate* — [Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md#L60](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md) · [Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md#L61](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md)

## Engines

- **sacrifice-draw:** Tresserhorn's Lord, Returned. Online when: Tresserhorn on the battlefield. *fact · high* — `oracle:Tresserhorn's Lord, Returned` · [Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md#L49](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md) · [Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md#L50](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md)
- **fodder:** Bitterblossom, Bitterbloom Bearer, Chittering Witch, Mogg War Marshal, Weaponcraft Enthusiast, Endrek Sahr, Master Breeder, Jadar, Ghoulcaller of Nephalia, Lagomos, Hand of Hatred, Ophiomancer, Marionette Apprentice, Tempt with Vengeance, Chasm Skulker, Woe Strider, Bloodghast. Online when: Cheap repeatable bodies. *strategic_judgment · high* — [Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md#L13](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:fodder` | yes | 10 | Bodies for the ETB and outlets. | 14: Bitterblossom, Bitterbloom Bearer, Chittering Witch, Mogg War Marshal, Weaponcraft Enthusiast, Endrek Sahr, Master Breeder, Jadar, Ghoulcaller of Nephalia, Lagomos, Hand of Hatred, Ophiomancer, Marionette Apprentice, Tempt with Vengeance, Chasm Skulker, Woe Strider, Bloodghast | — | *strategic_judgment · high* | [Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md#L13](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md) · [Tresserhorn_s_Lord_Returned_Candidate_Decisions_2026-10-15.md#L50](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Tresserhorn_s_Lord_Returned_Candidate_Decisions_2026-10-15.md) |
| `pkg:outlets` | yes | 6 | Free sacrifice outlets. | 9: Viscera Seer, Carrion Feeder, Phyrexian Altar, Ashnod's Altar, Goblin Bombardment, Yawgmoth, Thran Physician, Phyrexian Tower, High Market, Warren Soultrader | — | *strategic_judgment · high* | [Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md#L54](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md) |
| `pkg:drain` | yes | 4 | Drain payoffs that also offset life costs. | 5: Blood Artist, Zulaport Cutthroat, Bastion of Remembrance, Marionette Apprentice, Mayhem Devil | — | *strategic_judgment · high* | [Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md#L53](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md) |

## Key interactions

- **etb-three-draws:** Paying the ETB by sacrificing three creatures gives three draws while Tresserhorn is on the battlefield; he also triggers for his own sacrifice. (Tresserhorn's Lord, Returned) *fact · high* — [Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md#L49](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md) · [Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md#L50](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md) · `cr:603.10a`
- **plumb-math:** Plumb the Forbidden with N creatures draws 2N+1. (Plumb the Forbidden, Tresserhorn's Lord, Returned) *fact · high* — [Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md#L55](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md)
- **familiar-generic-only:** Nightscape Familiar reduces only the generic part: {1}{U}{B}{R}, no lower. (Nightscape Familiar, Tresserhorn's Lord, Returned) *fact · high* — [Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md#L56](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md)
- **not-of-this-world:** Not of This World is free only against things targeting him, not sweepers or edicts. (Not of This World, Tresserhorn's Lord, Returned) *fact · high* — [Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md#L57](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md)
- **edict-indestructible:** Blasphemous Edict gets around indestructible; keep Tresserhorn out of the chosen set. (Blasphemous Edict, Tresserhorn's Lord, Returned) *fact · high* — [Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md#L59](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md)
- **no-etb-hosers:** Torpor Orb and Karn, Argent Defender were rejected: they shut off his ETB. (Tresserhorn's Lord, Returned) *fact · high* — [Tresserhorn_s_Lord_Returned_Candidate_Decisions_2026-10-15.md#L23](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Tresserhorn_s_Lord_Returned_Candidate_Decisions_2026-10-15.md) · [Tresserhorn_s_Lord_Returned_Candidate_Decisions_2026-10-15.md#L27](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Tresserhorn_s_Lord_Returned_Candidate_Decisions_2026-10-15.md)

## Tutors and recursion

- Tutor target **The Locust God** via Diabolic Intent, Demonic Tutor, Vampiric Tutor *strategic_judgment · high* — `spellbook:1339-2292-7920`
- Recursion: Gravecrawler, Bloodghast, Reanimate, Victimize, Living Death, Wilhelt, the Rotcleaver *strategic_judgment · high* — [Tresserhorn_s_Lord_Returned_Candidate_Decisions_2026-10-15.md#L34](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Tresserhorn_s_Lord_Returned_Candidate_Decisions_2026-10-15.md)

## Requirements

- **Interaction:** Stubborn Denial, Not of This World, Swan Song, Feed the Swarm, Chaos Warp, Blasphemous Edict, Blasphemous Act.
- **Protection:** Lightning Greaves, Not of This World, indestructible.
- **Mana:** 34 land-capable slots with Cavern of Souls and Kher Keep; Sol Ring, Talismans, Nightscape Familiar.
- *strategic_judgment · moderate* — [Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md#L57](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md) · [Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md#L56](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md)

## Failure modes

- **etb-cost:** The ETB needs three creatures, 3 life and gives an opponent three cards; without fodder he is sacrificed. Mitigations: Fodder density; Draw triggers. *strategic_judgment · high* — `oracle:Tresserhorn's Lord, Returned`
- **edicts-exile:** Edicts, exile and bounce get around indestructible. Mitigations: Not of This World; Fodder. *strategic_judgment · high* — [Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md#L59](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md)
- **self-deck:** Optional loops can deck you; stop before it happens. Mitigations: Drain outlet first. *strategic_judgment · moderate* — [Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md#L54](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md)

## Identity core

- **Tresserhorn's Lord, Returned:** Draws on every sacrifice. *fact · verified* — `oracle:Tresserhorn's Lord, Returned`
- **The Locust God:** Loops with Tresserhorn. *strategic_judgment · high* — `spellbook:1339-2292-7920`
- **Gravecrawler:** Recursive Zombie loop body. *strategic_judgment · high* — `spellbook:2577-4050`
- **Plumb the Forbidden:** Burst sacrifice draw. *strategic_judgment · high* — [Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md#L55](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md)
- **Weaponcraft Enthusiast:** Three bodies for the ETB. *strategic_judgment · high* — [Tresserhorn_s_Lord_Returned_Candidate_Decisions_2026-10-15.md#L50](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Tresserhorn_s_Lord_Returned_Candidate_Decisions_2026-10-15.md)

## Anti-goals and thematic constraints

- ✗ No Torpor Orb / Karn, Argent Defender (decisions L23, L27).
- ✗ No Zombie tribal or Voltron drift (L22, L26, L60).
  - *strategic_judgment · high* — [Tresserhorn_s_Lord_Returned_Candidate_Decisions_2026-10-15.md#L23](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Tresserhorn_s_Lord_Returned_Candidate_Decisions_2026-10-15.md) · [Tresserhorn_s_Lord_Returned_Candidate_Decisions_2026-10-15.md#L27](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Tresserhorn_s_Lord_Returned_Candidate_Decisions_2026-10-15.md) · [Tresserhorn_s_Lord_Returned_Candidate_Decisions_2026-10-15.md#L22](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Tresserhorn_s_Lord_Returned_Candidate_Decisions_2026-10-15.md) · [Tresserhorn_s_Lord_Returned_Candidate_Decisions_2026-10-15.md#L60](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Tresserhorn_s_Lord_Returned_Candidate_Decisions_2026-10-15.md)
- Theme: Aristocrats / sacrifice / tokens (verification L17).
  - *strategic_judgment · high* — [Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md#L17](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md)

## Project exceptions

- **Authorized future-release project exception:** Tresserhorn's Lord, Returned. Project authorization `AUTHORIZED_FUTURE_RELEASE`; registry state `PENDING_RELEASE`. Official Commander legality, recorded separately: not legal until 2026-11-13 (Wizards: new-to-Magic MBC cards are legal from 2026-11-13).

## Construction-relevant rules

- **CR 701.21a:** Sacrifice. *fact · verified* — `cr:701.21a`
- **CR 603.10a:** Look-back triggers. *fact · verified* — `cr:603.10a`
- **CR 702.12b:** Indestructible. *fact · verified* — `cr:702.12b`

## Supporting features (heuristic, not identity)

- `{"hooks": ["sacrifice"], "hooked_cards": 45, "role_counts": {"counter": 3, "draw": 12, "protection": 3, "ramp": 14, "removal": 4, "tutor": 4, "wipe": 1}, "lands": 33, "edhrec_pages": ["tresserhorns-lord-returned"]}` *heuristic · low*

## Provenance

- Seeded from: [Tresserhorn_s_Lord_Returned_Candidate_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Tresserhorn_s_Lord_Returned_Candidate_Decisions_2026-10-15.md) · [Tresserhorn_s_Lord_Returned_Approved_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Tresserhorn_s_Lord_Returned_Approved_2026-10-15.md) · [Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Tresserhorn_s_Lord_Returned_Approval_Ready_Verification_2026-10-15.md) · [Tresserhorn_s_Lord_Returned_Approved_2026-10-15.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Tresserhorn_s_Lord_Returned_Approved_2026-10-15.txt)
- Reviewed by: corymstover
- **Cory's review (2026-10-16, chat t50u (2026-10-16T17:47Z, relayed)):** ceiling B4, commander role central, dependency high. Resolves this blueprint's ceiling and commander role. Not M2 acceptance; no list change. *approved_decision · verified*
- **Correction (Bot cycle 62):** retracted Project exceptions section rendered 'None.' → The authorized future-release project exception(s) are recorded in project_exceptions.future_release, separately from official legality (Wizards: legal 2026-11-13). Registry state stays PENDING_RELEASE.
