# Blueprint — Obeka, Brute Chronologist

> **Commander Blueprint v1** (seeded, Bot cycle 55, 2026-10-16) for the canonical project list ([deck page](../decks/obeka-brute-chronologist.md), state `SOURCE_BASELINE`, list `lh1:958f40565c66c18b…`). Machine-readable source: [`data/grixis/blueprints/obeka-brute-chronologist.json`](../../data/grixis/blueprints/obeka-brute-chronologist.json). Every claim carries its evidence class and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.

## Commander (Oracle, fact)

**Obeka, Brute Chronologist** — Legendary Creature — Ogre Wizard

> {T}: The player whose turn it is may end the turn. (Exile all spells and abilities from the stack. The player whose turn it is discards down to their maximum hand size. Damage wears off, and "this turn" and "until end of turn" effects end.)

## Plan and commander role

- **Primary plan:** Delayed-trigger abuse: on your own turn, let the 'at the beginning of the next end step' liability (lose the game, sacrifice, exile) go on the stack, then tap Obeka to end the turn and exile it. Risky extra turns become free extra turns, and temporary tokens, clones and reanimations become permanent. *strategic_judgment · high*
- **Secondary:** Kiki-Jiki/Twinflame clone infinites and Isochron Scepter + Final Fortune (+ Obeka or Sundial) infinite turns.
  - Evidence: [Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md#L13](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md) · [Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md#L35](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md) · [Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md#L54](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md)
- **Commander role: central.** Obeka's end-the-turn is what makes the risky extra turns and temporary effects profitable. *strategic_judgment · high*
- ⚠️ **Honest note:** Commander-native identity with one commander combo (Scepter + Final Fortune + Obeka). Sundial of the Infinite does the same job without her, and the Kiki/Dualcaster infinites are commander-free. On opponents' turns the active player decides whether to end the turn, so she can't erase liabilities then (blueprint L17). M1 review (obekabc-01..05, all verified) confirms the end-the-turn timing and both combos.
  - Evidence: [Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md#L17](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md) · `spellbook:126-1173-5261` · `spellbook:1173-2160-5261`
- **Dependency level:** high *strategic_judgment · high* — [Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md#L13](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md)

## Power

| Field | Value | Class | Evidence |
|---|---|---|---|
| Source ceiling | 4 (Power Bracket 4 — Optimized (blueprint).) | *fact · verified* | [Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md#L9](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md) |
| GrokBot estimated ceiling | 4 (Bracket 4 ceiling: commander-native infinite turns and clone loops, but sequencing-heavy and fragile to removal at the key moment. Agrees with the source.) | *strategic_judgment · high* | [Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md#L69](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md) · `spellbook:126-1173-5261` |
| Expected bracket (list as built) | 4 (computed floor 4) | *strategic_judgment · high* | `companion:data/grixis_summary.json#Obeka__Brute_Chronologist` |
| Resolved ceiling | — (only Cory resolves) | | |
| Disagreement | no | | |

- EDHREC: `{"bracket_counts": {"1": 17, "2": 340, "3": 781, "4": 474, "5": 44}, "decks_with_bracket": 1656, "share_b4_plus": 0.313, "note": "Self-reported brackets of public EDHREC lists; popularity, not a power measurement."}` *derived_metric · moderate* — `edhrec:.cache/edhrec/commanders__obeka-brute-chronologist.json`

## Win conditions

- **scepter-fortune** (combo): Isochron Scepter imprinting Final Fortune + Obeka or Sundial of the Infinite: infinite turns. Cards: Isochron Scepter, Final Fortune, Obeka, Brute Chronologist, Sundial of the Infinite. *fact · verified* — `spellbook:126-1173-5261` · `spellbook:1173-2160-5261` · [Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md#L35](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md)
- **clone-loops** (combo): Kiki-Jiki + Delina, Wild Mage; Dualcaster Mage + Twinflame: infinite hasty tokens. Cards: Kiki-Jiki, Mirror Breaker, Delina, Wild Mage, Dualcaster Mage, Twinflame. *fact · verified* — `spellbook:282-618` · `spellbook:147-1235`
- **risky-turns** (natural): Free extra turns from Last Chance/Warrior's Oath/Glorious End/Alchemist's Gambit, with permanent tokens beating down. Cards: Obeka, Brute Chronologist, Final Fortune, Last Chance, Warrior's Oath, Alchemist's Gambit, Glorious End. Enablers: Fable of the Mirror-Breaker // Reflection of Kiki-Jiki, Flameshadow Conjuring, Delina, Wild Mage, Jaxis, the Troublemaker. *strategic_judgment · moderate* — [Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md#L26](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md)

## Engines

- **end-the-turn:** Obeka, Brute Chronologist, Sundial of the Infinite. Online when: Obeka untapped on your turn after the delayed trigger is on the stack. *fact · high* — `oracle:Obeka, Brute Chronologist` · [Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md#L18](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md) · `cr:724.1`
- **temporary-to-permanent:** Fable of the Mirror-Breaker // Reflection of Kiki-Jiki, Flameshadow Conjuring, Delina, Wild Mage, Jaxis, the Troublemaker, Rionya, Fire Dancer, Saheeli, the Sun's Brilliance, Hate Mirage, Venser, Fervent Forger, Identity Thief, Come Back Wrong, Apprentice Necromancer, Feldon of the Third Path, Puppeteer Clique, Sneak Attack. Online when: Obeka can end the turn before the end-step sacrifice/exile resolves. *strategic_judgment · high* — [Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md#L37](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md) · [Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md#L54](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md)

## Packages

| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |
|---|---|---|---|---|---|---|---|
| `pkg:risky-turns` | yes | 5 | Extra turns with delayed liabilities. | 6: Final Fortune, Last Chance, Warrior's Oath, Alchemist's Gambit, Glorious End, Isochron Scepter | — | *strategic_judgment · high* | [Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md#L26](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md) |
| `pkg:temporary-effects` | yes | 8 | Temporary tokens, clones and reanimation made permanent. | 14: Fable of the Mirror-Breaker // Reflection of Kiki-Jiki, Flameshadow Conjuring, Delina, Wild Mage, Jaxis, the Troublemaker, Rionya, Fire Dancer, Saheeli, the Sun's Brilliance, Hate Mirage, Venser, Fervent Forger, Identity Thief, Come Back Wrong, Apprentice Necromancer, Feldon of the Third Path, Puppeteer Clique, Sneak Attack | — | *strategic_judgment · high* | [Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md#L37](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md) |
| `pkg:deploy-activate` | yes | 5 | Deploy and activate Obeka immediately. | 6: Lightning Greaves, Swiftfoot Boots, Thousand-Year Elixir, Arena of Glory, Minamo, School at Water's Edge, Hellkite Courser | — | *strategic_judgment · high* | [Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md#L56](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md) |

## Key interactions

- **active-player-chooses:** The player whose turn it is decides whether to end it; opponents can decline on their turns. (Obeka, Brute Chronologist) *fact · verified* — [obekabc-01](../interactions/obeka-brute-chronologist.md#obekabc-01-obeka-ends-the-turn-timing-the-activation-against-end-step-triggers) · [Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md#L17](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md)
- **respond-to-end-step-trigger:** Let the next-end-step liability trigger in your own end step, then end the turn in response. Ending the turn earlier only pushes the trigger to the next player's end step. (Obeka, Brute Chronologist) *fact · verified* — [obekabc-01](../interactions/obeka-brute-chronologist.md#obekabc-01-obeka-ends-the-turn-timing-the-activation-against-end-step-triggers) · [Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md#L18](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md) · `cr:724.1a`
- **next-occurrence-only:** A delayed trigger for the next end step doesn't trigger again once it has triggered and been exiled. (Obeka, Brute Chronologist) *fact · verified* — [obekabc-03](../interactions/obeka-brute-chronologist.md#obekabc-03-delayed-liabilities-become-permanent-identity-thief-come-back-wrong-hate-mirage-apprentice-necromancer-venser-sneak-attack) · [Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md#L20](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md)
- **courser-return:** Hellkite Courser's return-to-command-zone delayed trigger can be erased, keeping the commander on the battlefield. (Hellkite Courser, Obeka, Brute Chronologist) *fact · verified* — [obekabc-04](../interactions/obeka-brute-chronologist.md#obekabc-04-hellkite-courser-puts-obeka-in-play-hasty-and-tax-free-obeka-keeps-herself-there) · [Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md#L65](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md)
- **scepter-final-fortune:** Isochron Scepter + Final Fortune + Obeka (or Sundial) is infinite turns: end the turn on the lose trigger. (Isochron Scepter, Final Fortune, Obeka, Brute Chronologist, Sundial of the Infinite) *fact · verified* — [obekabc-02](../interactions/obeka-brute-chronologist.md#obekabc-02-isochron-scepter--final-fortune--obeka-or-sundial-of-the-infinite-infinite-turns)
- **hasty-token-loops:** Kiki-Jiki + Delina and Dualcaster Mage + Twinflame make infinite hasty tokens. (Kiki-Jiki, Mirror Breaker, Delina, Wild Mage, Dualcaster Mage) *fact · verified* — [obekabc-05](../interactions/obeka-brute-chronologist.md#obekabc-05-kiki-jiki--delina-and-dualcaster-mage--twinflame-infinite-hasty-tokens)

## Tutors and recursion

- Tutor target **Isochron Scepter** via Demonic Tutor, Vampiric Tutor, Gamble *strategic_judgment · high* — `spellbook:126-1173-5261`
- Tutor target **Final Fortune** via Mystical Tutor *strategic_judgment · high* — `spellbook:126-1173-5261`
- Recursion: Underworld Breach, Jeska's Will, Animate Dead, Necromancy, Reanimate *strategic_judgment · moderate* — [Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md#L76](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md)

## Requirements

- **Interaction:** Force of Will, Mana Drain, Counterspell, Chaos Warp, Cyclonic Rift, Toxic Deluge.
- **Protection:** Fierce Guardianship, Deflecting Swat, Greaves, Boots.
- **Mana:** 34 lands, Sol Ring, Mana Vault, Chrome Mox, Lotus Petal, Talismans.
- *strategic_judgment · moderate* — [Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md)

## Failure modes

- **obeka-removed-with-liability:** Losing Obeka with a Final Fortune trigger pending loses the game. Mitigations: Sundial redundancy; Protection before going for it. *strategic_judgment · high* — [Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md#L21](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md)
- **sequencing-errors:** Ending the turn too early pushes the liability into an opponent's end step. Mitigations: Explicit sequencing. *strategic_judgment · high* — [Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md#L79](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md)
- **summoning-sick:** The tap ability needs haste the turn she comes down. Mitigations: Greaves; Boots; Thousand-Year Elixir. *strategic_judgment · moderate* — `oracle:Obeka, Brute Chronologist`

## Identity core

- **Obeka, Brute Chronologist:** Ends the turn to erase delayed liabilities. *fact · verified* — `oracle:Obeka, Brute Chronologist`
- **Isochron Scepter:** Repeats Final Fortune each turn. *strategic_judgment · high* — `spellbook:126-1173-5261`
- **Final Fortune:** Extra turn whose loss trigger Obeka erases. *strategic_judgment · high* — `spellbook:126-1173-5261`
- **Fable of the Mirror-Breaker // Reflection of Kiki-Jiki:** Reflection copies kept permanently. *strategic_judgment · high* — [Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md#L39](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md)
- **Hellkite Courser:** Tax-free commander redeploy with haste. *strategic_judgment · high* — [Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md#L65](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md)

## Anti-goals and thematic constraints

- ✗ No generic Oracle/Breach packages (blueprint L75); Breach stays only as recursion (L76).
- ✗ Don't overuse The Master, Multiplied-style independent fixes (L78).
- ✗ Don't end the turn prematurely (L79).
  - *strategic_judgment · high* — [Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md#L75](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md) · [Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md#L76](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md) · [Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md#L78](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md)
- Theme: Delayed triggers / extra turns / clones (blueprint L11).
  - *strategic_judgment · high* — [Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md#L11](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md)

## Project exceptions

None.

## Construction-relevant rules

- **CR 724.1:** Ending the turn. *fact · verified* — `cr:724.1`
- **CR 603.7c:** Delayed triggered abilities. *fact · verified* — `cr:603.7c`

## Supporting features (heuristic, not identity)

- `{"hooks": ["card draw / hand size", "discard"], "hooked_cards": 13, "role_counts": {"counter": 4, "draw": 8, "protection": 3, "ramp": 12, "removal": 4, "tutor": 4, "wipe": 1}, "lands": 34, "edhrec_pages": ["obeka-brute-chronologist"]}` *heuristic · low*

## Provenance

- Seeded from: [Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/blueprints/Obeka_Brute_Chronologist_Commander_Blueprint_2026-10-15.md) · [Obeka_Brute_Chronologist_Candidate_Decisions_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/decisions/Obeka_Brute_Chronologist_Candidate_Decisions_2026-10-15.md) · [Obeka_Brute_Chronologist_Approved_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/approvals/Obeka_Brute_Chronologist_Approved_2026-10-15.md) · [Obeka_Brute_Chronologist_Approval_Ready_Verification_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Obeka_Brute_Chronologist_Approval_Ready_Verification_2026-10-15.md) · [Obeka_Brute_Chronologist_Whole_List_Audit_2026-10-15.md](../source-archive/grixis-commander-encyclopediaGPT/refinement/verification/Obeka_Brute_Chronologist_Whole_List_Audit_2026-10-15.md) · [Obeka_Brute_Chronologist_Approved_2026-10-15.txt](../source-archive/grixis-commander-encyclopediaGPT/refinement/decklists/Obeka_Brute_Chronologist_Approved_2026-10-15.txt)
- Reviewed by: — (not yet reviewed by Cory)
