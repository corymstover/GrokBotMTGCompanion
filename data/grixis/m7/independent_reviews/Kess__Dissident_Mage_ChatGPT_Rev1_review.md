# Kess, Dissident Mage — ChatGPT independent M7 Rev1 candidate (2026-10-24)

**Status: OWNER REVIEW CANDIDATE ONLY. NOT APPROVED, NOT LOCKED, NOT CANONICAL.**

## Scope and authoritative source

- Deck #26, `Kess__Dissident_Mage`, commander `Kess, Dissident Mage`.
- Existing approved/locked October 14 source: `corymstover/grixis-commander-encyclopediaGPT/main/refinement/decklists/Kess_Dissident_Mage_Approved_2026-10-14.txt`.
- Existing baseline raw SHA-256: `93d27d605bbdf0737ebe32c911fafe3a002b06d7d90f00b7bfc402cb1d3faccb`, 100 physical singleton cards, 27 lands.
- Engineering Grok first-pass research PR #674, exact head `b505d828cf8936871385d33f57725def295f0b7c`, proposed only +Mana Drain / -Personal Tutor; its `RESEARCH_ONLY` 1-swap outcome is preserved unchanged as a historical comparator, not relabeled as approved.
- This separate five-swap candidate is `data/grixis/m7/independent_reviews/Kess__Dissident_Mage_ChatGPT_Rev1_candidate.txt` when committed. Raw SHA-256 with trailing newline: **`11415352a453e52afe4b1cc6881061e0d255e8403f8d5af5a24f9803c004fde4`**.
- No canonical repository, registry, owner approval field, prior deck or M6 sealed certificate is changed by this research branch.

## Five independent, substantive replacements

| Add | Cut | Why it is justified; what is lost |
|---|---|---|
| **Mana Drain** | **Personal Tutor** | Upgrades a card-to-top, sorcery-only tutor that cannot find Consultation/Pact into a hard counter. Kess can recast Drain against a spell on **her controller's own turn**; the delayed colorless mana can help in the next main phase, but only if Drain resolves countering a legal target. **Loss:** a one-mana recastable tutor for Demonic Tutor, Wheel, Reanimate, Beseech. **Owner override:** Personal Tutor was an October 14 owner addition. |
| **Grim Tutor** | **Demonic Counsel** | Always searches any card, including Oracle, Breach and protection, then can be replayed by Kess. Counsel searches only for a Demon without delirium, and **this 99 has no Demon**. The pre-existing Pass C proxy gave a strict turn-six delirium probability near **9%**, not a reliable early tutor. **Loss:** Counsel costs 2 instead of 3; Grim additionally costs 3 life. **Owner override:** Counsel was affirmatively accepted on October 14. |
| **Jeska's Will** | **Ledger Shredder** | With Kess controlled it selects **both** the red mana and top-three impulse modes, and a graveyard recast on a later own turn repeats them. It helps force a decisive combo turn. **Loss:** Shredder was a blue Force-pitch card and a recurring connive/graveyard outlet; blue-pitch count falls 26 to 25, weakening early Force availability slightly. **Owner reversal:** Jeska's Will was cut on October 14, and Shredder belongs to the chosen commander spine. Hand sizes are unmeasured, so Jeska's mana is not guaranteed. |
| **Cyclonic Rift** | **Into the Flood Maw** | For 2 mana, Rift bounces any opposing nonland permanent without handing an opponent a Fish; overload is an expensive, real late-game reset, and Kess may replay Rift on an own turn. **Loss:** Flood Maw costs only 1 mana and is better for immediate tempo against a creature, or a gifted opposing nonland permanent. This is flexibility over one-mana speed, not a universal dominance claim. |
| **Exotic Orchard** | **Fiery Islet** | A normally untapped multiplayer color source that may supply **black** as well as U/R, valuable for Necropotence, Beseech and Grim Tutor while keeping 27 lands. EDHREC cEDH Kess inclusion is 265/387 vs Fiery Islet 58/387 in the October 23 archived discovery. **Loss:** Islet always taps for U/R (with life payment), even if opponents have no lands, and can later sacrifice to draw a card. Orchard's colors are contingent on opponents' land abilities; no unconditional black-source increase is claimed. |

## Structural and strategic consequences

- Exact 100 = Kess commander + 99 library cards. 100 distinct names, no repeated nonbasics or basics, no companion. All 100 names are present in the **October 23 live-Scryfall-sourced 187-name Kess Oracle/legality archive** in engineering PR #674; all are Commander legal and have color identity within U/B/R. No project exception.
- Lands 27 to 27; front-face lands unchanged in number; Exotic Orchard is a conditional additional black source, but cannot be assumed to tap for a specific color without an opponent source.
- Force-pitch blue cards 26 to 25; library nonland average mana value **1.8472 to 1.9028**, using archive front-face values, 72 nonland library cards.
- Game Changers **21 to 23**: Cyclonic Rift and Jeska's Will are Game Changers in archived current Scryfall. Natural ceiling remains **Bracket 5 — cEDH**.
- Preserved: Kess; `Demonic Consultation`, `Tainted Pact`, `Thassa's Oracle`; `Underworld Breach`, `Lion's Eye Diamond`, `Brain Freeze`, `Grinding Station`; `Gifts Ungiven`, `Intuition`, `Entomb`, `Reanimate`, `Displacer Kitten`, `Snapcaster Mage`, `Spellseeker`, `Faithless Looting`, `Dragon's Rage Channeler`, `Valley Floodcaller`; all 27 land counts; full Force / Flusterstorm / Pact interaction spine.
- Kess permission is **once on each of your own turns**; a spell cast with it is exiled if it would go to the graveyard. Neither Drain nor Rift can normally be recast during opponents' turns merely because Kess exists. A new blinked Kess object provides fresh permission. Force of Negation's alternate casting cost does not work on the Kess controller's turn.
- Signature conditional win: Consultation/Pact can find Oracle from hand, then be recast from graveyard with Kess in response to Oracle's trigger, with sufficient library depletion and protection. Gifts/Intuition piles and Breach combos retain all named pieces. No claim of guaranteed wins or empirically improved match win rate.

## Adversarial countercase, candidate exhaustion and limitations

1. **The owner-overrides are deliberate proposed reversals, not silent changes**: Personal Tutor and Demonic Counsel were October 14 additions/keeps; Ledger Shredder was core; Jeska's Will was cut. Their actual losses are specified above and Cory must decide whether this new M7 tradeoff wins.
2. Mana Drain ({U}{U}) demands two blue sources; a Kess recast can counter only spells cast while it is the Kess player's turn, so do not model it as free banked mana. The initial source's blue-source bounds 0.50–0.84 on turns 2–6 are applicable, not a win-rate calculation.
3. Jeska's Will on three cards in target opponent's hand is net 0 red mana for its three-mana cost (plus top-three impulse if Kess is controlled). It is mana-negative at lower hand sizes; no real opponent-hand distribution was measured.
4. Cyclonic Rift costs one more than Maw at normal casting and cannot answer a land; emergency plays may worsen. Overload for seven is expensive and is not considered a normal cEDH line.
5. Exotic Orchard can fail to produce U/B/R in an unusual pod or as the opening land before opponents deploy. If this conditional weakness is unacceptable, the original Fiery Islet slot is fully preserved as the zero-swap alternative.
6. The October 23 Grok M6 I/J certification is **exact-source-bound to a different one-swap candidate**, not inherited by this five-swap candidate. The scoped independent structural/Oracle/rules regression checks here are new checks, not an equivalent formal M6 I/J seal. No validated matched-hand game engine or four-player tournament win-rate simulation exists.
7. Further options independently challenged but not selected: Frantic Search (land-only untap, 3-mana up-front, not clearly above protected slots), Spell Pierce (soft permission), Muddle the Mixture (3-mana transmute for Oracle/Breach but lowers early defensive density), Mana Drain instead of Deadly Rollick (retains Tutor, loses free creature removal), Undercity Sewers instead of City of Traitors (enters tapped), Gemstone Mine instead of Fiery Islet (sacrifices after three taps), and owner-rejected The One Ring, Opposition Agent and Dauthi Voidwalker (not re-added). Five results from judged 99-slot opportunities, not a fixed cap.

## Evidence and owner gate

- Primary project evidence: engineering PR #674's October 23 `Kess__Dissident_Mage_M7_Scryfall_20261023.json`, Pass C measured tests, EDHREC discovery cache, current-cycle October 14 decisions and canonical exact source.
- EDHREC Kess cEDH first-party data: https://edhrec.com/commanders/kess-dissident-mage/cedh (observational inclusion; not causal win-rate data).
- Source card rules: https://scryfall.com/card/ima/65/mana-drain ; https://scryfall.com/card/dsk/92/demonic-counsel ; https://scryfall.com/card/cmr/187/jeskas-will ; https://scryfall.com/card/rvr/40/cyclonic-rift ; https://scryfall.com/card/c21/288/exotic-orchard.
- **Approval is requested only for exact raw 100-card candidate SHA `11415352a453e52afe4b1cc6881061e0d255e8403f8d5af5a24f9803c004fde4`, never automatically inferred**. Do not update canonical overrides, merge into canonical `main`, or declare M7 lock until Cory expressly approves this precise candidate and a separate exact-head canonical PR passes relevant CI and postmerge raw hashing.

**Recommended power bracket:** 5 — cEDH. **Archidekt tags:** cEDH / Graveyard Spells / Consultation Combo.
