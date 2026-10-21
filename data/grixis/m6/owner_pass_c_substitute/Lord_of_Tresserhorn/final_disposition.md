# Josh-Lee-Kwai formal owner-equivalent Pass C #29 — Lord of Tresserhorn final disposition

**Final decision: `NEEDS TESTING` — owner-approved exact 100 remains `APPROVED/LOCKED` and UNCHANGED.** The third scrutiny is eligible to count as `FORMAL_PASS_C_OWNER_EQUIVALENT` **only after evidence exact-head CI and merge**, because Cory explicitly waived actual third-model technical independence for project Pass C. This is **not** Phase B certification, I/J completion, M6 milestone acceptance, M7 owner decision or M8 export acceptance.

## Canonical authority and cryptographic evidence

- Canonical repository/branch: `corymstover/grixis-commander-encyclopediaGPT@main`. Approval/lock authority: `state/current_deck_overrides.json`.
- Approved TXT: `refinement/decklists/Lord_of_Tresserhorn_Approved_2026-10-14.txt`, Git blob `d9ff96da998bf5773cf6bdb2c6f0fc05f19c8d76`.
- **Independently reproduced actual raw-file SHA-256:** `95863276f38beff6b0cf7609041006a6f1de94d5e62c73d76551d6793ffa5b8e`, exact match with canonical approval.
- Count: **100 physical cards = 1 commander + 99 library**; 98 distinct names; **35 lands**; Swamp appears three times and is the only repeated name. U/B/R identity, no designated project legality exception for this deck.
- Initial neutral Stage A dedicated commit: **`f6d930bfa97c59fb39a04e3ed6223fbaea6ccb19`**. Stage A MD SHA-256: `02ca73a0c891a418377a17ab61bccd0dfcebfb221d9748bece2f8baa8421043f`. Stage A JSON SHA-256: `ee6c5c80260cc21768a3889a74766ef6517a0bf4a0e76b5ac19b1d55208c07e6`.
- Separate subsequent `seal.json` Git commit: **`e5e8bd91cddb9bcea2964b0f4ff64e9644710581`**; actual unblinding began afterwards. Both original Stage A files remain immutable. [Stage B source comparison](stage_b_reconciliation.md) preserves discrepancies without editing first verdict.
- Clerical Stage A metadata correction: **human-facing ordinal #29 corresponds to zero-based tracker_index 28**, not the Stage A JSON's one-based value 29. Corrected here and in Stage B/progress; the original sealed record is left intact and explicitly annotated.

## Commander-first strategic decision

Lord of Tresserhorn ({1}{U}{B}{R}, **10/4 Zombie**) has a harsh enter-the-battlefield sacrifice-and-card-draw trigger. This deck develops trigger suppression (Karn/Torpor/Dress Down/Stifle/Tale's End) or two disposable creatures, then protects Lord and converts ten power into lethal damage through **infect and evasive combat**, 11-power **double strike** (Uncaged Fury = 22 commander combat damage when both hits connect), and creature-source bursts (Chandra's Ignition/Pain for All). Kediss broadens single-opponent combat damage across the table as **noncombat**, not commander damage. Gravecrawler/Altar/Zombie sacrifice payoffs supply a functional fallback after a thwarted Lord attack. The architecture is substantially commander-first, not generic Grixis goodstuff.

**Natural ceiling:** **Bracket 4 — Optimized** (strategic classification consistent with approved baseline and full author; not asserted as newly official certification or cEDH). Mana sources are well fixed but 35 land slots carry several utility/colorless/tapped risks and Lord needs multiple independently timed pieces to attack safely.

## Rules correctness, counterplay and scope

1. Lord's drawback is **one opponent-targeted triggered ability**. If allowed to resolve without two other sacrificeable creatures, Lord itself may be sacrificed. Regeneration is no protection from sacrifice. Torpor Orb/Karn/Dress Down prevent the trigger at Lord's arrival; Stifle/Tale's End can counter it on the stack. Removing a preexisting suppressor while Lord is still on the stack restores its eventual trigger; removing one afterwards does not retroactively create a trigger.
2. A base unblocked 10-power commander requires three such ordinary hits to reach 21 combat commander damage; infect on a normal ten-power Lord instead eliminates at ten poison. Uncaged Fury grants +1/+1 and double strike for 22 *combat* commander damage if no interruption between strike steps; mere double strike at ten power is only twenty. Noncombat damage from Kediss, Pain or Ignition cannot count as commander damage, though infect on its actual creature source matters.
3. **Dress Down/Kediss collision:** the same-turn Dress Down needed to avoid the ETB temporarily blanks **Kediss's triggered ability**, so don't simultaneously count a same-turn Kediss spreading infect hit. Phyresis/Tainted Strike versus Dress Down invokes layer-6/timestamp ordering and deserves source-paid effect-aware replay.
4. **GrokBot advisory error corrected in Stage B:** Torpor Orb does **not** blank Undead Augur or Zulaport Cutthroat **dies triggers**. The full authored review correctly treats them as death payoffs. Grok's short KEEP did not provide a sufficient rules certificate. Rooftop Storm's zero base Zombie cost also does not nullify commander tax.
5. Opponents can remove/counter a suppressor before entry, counter Stifle, exploit blocker density, exile or bounce rather than destroy Lord, remove Lord in response to infect/Aura/Ignition, counter a Gravecrawler payoff, or shut down recursion with graveyard disruption. Free protection is conditional on what it can target and whether Lord is controlled.
6. **Legality/Oracle receipts:** Current WotC [Commander rules](https://magic.wizards.com/en/formats/commander), [Comprehensive Rules](https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt), historical 2026-10-14 approval gate and the GrokBot *reported* 2026-10-20 Scryfall full collection legality pass are the recorded scope. Lord, Karn, and Pain for All text were independently spot-checked from a current indexed card database. **This Pass C did not run a fresh complete all-100 Oracle/legal verification** or measured games; do not upgrade historical source receipts into contemporary complete certification. No new specific legality blocker identified.

## Full comparison and source-backed final disposition

- Prior comprehensive authored M6 review: **KEEP**, preserving **Soul's Fire for Sheoldred's Edict** as the best focused test; identified practical gains and the substantial cost of losing cheap sacrifice-based answer to hexproof/indestructible.
- GrokBot advisory: **low-confidence KEEP**; rejected **Grafted Exoskeleton for Diregraf Captain**. Its claim that Torpor turns off Undead Augur/Zulaport death triggers is wrong; no deck cut follows from it.
- Two-model reconciliation: **KEEP documentary agreement only**, no fresh effect-aware Phase B.
- **Sealed neutral Stage A:** `NEEDS TESTING`; independently suggested **Fierce Guardianship** protection versus conditional slots and **Distortion Strike/Artful Dodge** evasion, without asserting an approved exact cut. Recovered original Soul's Fire hypothesis after unblinding; historical agreement must not be presented as a new independent finding.
- **Stage C:** `NEEDS TESTING`, not `PROPOSE UPGRADE`. No proposed exact add/cut passes decision-grade net-benefit proof today; **no owner approval requested yet**. KEEP the actual legal owner list as control.

### Narrow, consequential Phase B queue

1. **Protection tradeoff:** paired exact deck variants `+Fierce Guardianship / -Sheoldred's Edict` and `+Fierce Guardianship / -Nightscape Familiar` versus unchanged 100. Conditions: with/without Lord controlled, suppressor on board/on stack, colored-source access, instant noncreature exile vs creature-based ability, and loss of edict/discount. These are *test candidates*, not authorized swaps.
2. **Damage conversion:** original author's `+Soul's Fire / -Sheoldred's Edict` (alternative `-Muddle the Mixture`) against 1/1 blocking Lord, infect present/absent, commander removal in response, and Muddle's transmute targets. Compare *effect-aware timing and opportunity cost*, not a standalone "deals ten" claim.
3. **Mechanics edge:** Dress Down + Kediss + haste + Phyresis/Tainted Strike with layer-6 chronological order; ensure all source control, target, untap, phase and opponent response conditions are recorded. Include Pain for All/Blasphemous Act with last-known-source traits as appropriate.
4. **Mana/evasion only if consequential:** `+Distortion Strike / -Rogue's Passage` as an explicitly **34-land** stress case versus a no-land-loss alternative, with real mulligan policy, turn-4 UBR access, repeat attack and commander tax. This is lower priority than 1–3.

Reuse the authored 21 manual stack-state traces and reported October 20 legality gate wherever current certification contract permits. **Manual constructed states are not new measured testing**. Require decklist/hash source receipts, exact actual spell/mana windows, opponent policies, reproducibility inputs, new rules/Oracle delta checks and material result analysis before any Phase B/I/J/M6 certificate.

**Reviewer factual provenance:** display alias **Josh-Lee-Kwai**, actual evaluator **ChatGPT/OpenAI GPT-6**, same model lineage as the original ChatGPT reviewer; `technically_independent=false`; `independence_requirement=OWNER_WAIVED_FOR_FORMAL_PASS_C`; project qualification `FORMAL_PASS_C_OWNER_EQUIVALENT` per explicit October 20 owner directive. Earlier-session familiarity cannot be erased. A green GitHub check validates recorded evidence integrity and boundary preservation, **not** strategic win rates or independent-model execution.

**Owner gate:** Cory must explicitly approve any future exact card swap, followed by fresh 100-card recount, singleton/color/Oracle/legality and new approved hash verification. No mutation of `state/current_deck_overrides.json`, approved deck TXT or lock status in this review.

