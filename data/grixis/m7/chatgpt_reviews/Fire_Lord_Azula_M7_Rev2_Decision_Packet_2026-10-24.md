# Deck #19 — Fire Lord Azula: ChatGPT M7 Rev2 owner-approval packet (2026-10-24)

**STATUS: VERIFIED ENGINEERING PROPOSAL — AWAITING CORY'S EXPLICIT APPROVAL. NOT CANONICAL, NOT LOCKED.**

## Exact identity and provenance

- Commander: Fire Lord Azula ({1}{U}{B}{R}), combat-triggered spell copying and firebending 2. Strategy: proactive cEDH with attack-window duplicated spells, flash/haste support, Narset's Reversal engines, Oracle/Consultation/Pact and Underworld Breach lines.
- Source: canonical approved Oct14 `refinement/decklists/Fire_Lord_Azula_Approved_2026-10-14.txt`, **raw SHA-256 `b6ef396641f2b5cfac0eb81fb494f21f3745e2a3fd47fa75d2eaadbdc34ddee5`**; owner approval of this historical source is preserved.
- ChatGPT exact 100-card approval candidate: `data/grixis/m7/candidate_lists/Fire_Lord_Azula_ChatGPT_M7_Rev2_Approval_Candidate_2026-10-24.txt`, **raw SHA-256 `77ac26a4f4ff70d0a7a666b07fa9fe051e52fe0547d8320d84490d088c0cc273`**. Identical bytes to archived full-100 `Fire_Lord_Azula_ChatGPT_Electro_Five_Under_Review.txt`.
- Engineering research PR #667 = Grok's first pass, PR #694 = independent adversarial review/approval packet. Neither automatically authorizes canonical replacement.
- Power Bracket **5 — cEDH**. Archidekt tags: **Combat-Flash / Spell Copy / Combo**. No project legality exception.

## Five selected swaps — MINIMUM FLOOR, NOT CAP

| Add | Cut | Why the commander improves | Significant opportunity cost |
|---|---|---|---|
| **Turnabout** | **Samut, Tyrant of Naktamun** | While Azula attacks, original and copy can untap lands; verified Spellbook Azula/Narset's Reversal/Turnabout loop `11-4276-7089`. Removing Samut also eliminates split-second interference with our own Narset's Reversal and spells free-cast during Beseech/Electro resolution. | Loses Samut's split-second counter-response protection—an **explicit Oct14 owner addition**. Hexing Squelcher, counters, Cavern and free protection are retained; no substitute fully recreates split second. |
| **Sink into Stupor // Soporific Springs** | **Exotic Orchard** | Spell/land MDFC: flexible combat instant copying to bounce two spells/permanents, or blue source as the land face. | Orchard's often-rainbow mana removed in a three-color deck. MDFC blue face requires 3 life to enter untapped, enters tapped otherwise; front face MV3 increases Ad Nauseam damage vs a zero-MV land. |
| **Samut, Hazoret's Champion** | **Vivi Ornitier** | A **two-mana global haste** enabler increases access to same-turn Azula attack (the condition for every copied spell). Raw 10-card access from 99-library rises from 27.60% for three named haste effects to 35.14% for four, assuming random draws; not a playable-haste or win-rate rate. | Vivi is a repeatable mana engine and damage/counter payoff. Samut has lower combo/repeated-mana upside; must be on battlefield for haste. |
| **Flashback** | **Repeal** | One-red-mana instant grants a graveyard spell another cast; copied by an attacking Azula, potentially giving flashback to two *different* graveyard instants/sorceries. Adds commander-specific recursion and re-use of copied rituals/interaction. | Lose Repeal's reusable-in-hand bounce+cantrip flexibility; flashback still requires actual card's flashback cost and the card is exiled after casting. |
| **Electrodominance** | **Redirect Lightning** | Explicit, disclosed re-challenge of an **Oct14 owner removal**. At X=2, attack firebending {R}{R} can cover both red pips, leaving two other mana. Azula copies Electro; copy and original each may cast an eligible MV≤2 hand spell for free on resolution. Those spells are newly **cast**, so Azula can copy each while she remains attacking: high-impact combat storm/combo lines. Archived EDHREC cEDH: **126/566, 13.06× lift** (discovery only). | Lose conditional one-red-mana retarget/protection (`Redirect Lightning` was in **46.4%** of the stored 181-list stats.cedh.events top-staples snapshot). Electro requires a legal target at resolution and appropriate hand contents. Electro's original owner cut cited its mana intensity / weaker baseline floor. Retesting found higher ceiling specifically because Azula copies each resolution, but that does not make the change risk-free. |

### Electrodominance rules: explicit failure cases

Official Wizards *Avatar: The Last Airbender* release notes confirm Azula's trigger makes a spell copy **not cast**, but copies `X` and resolves before its original. Official *Outlaws of Thunder Junction* release notes say Electrodominance casts a hand spell **during its own resolution**, ignoring card-type timing restrictions. For the combo explanation above:

1. Azula must **still be attacking when each free spell is cast**; if she leaves combat, free spells cease to receive her trigger.
2. The Electrodominance copy and original require legal targets to resolve. **If the target is illegal at resolution, that instance fizzles and gives NO free cast.** Choosing an opponent as target often reduces, but does not eliminate, this exposure.
3. Free casting a card without paying its cost cannot use an alternate cost, still requires mandatory additional costs, cannot play land cards, and forces X=0 on an X-card cast for free.
4. At X=2 the candidate provides **up to two** Electro-resolution free-cast opportunities, but only if enough eligible cards are in hand; there is **no unconditional infinite combo**.
5. Azula's spell copies are placed on the stack; free-cast spell triggers from Electro are queued until Electro finishes resolving. Any triggered copy of a permanent spell will enter as a token after its copy resolves and the legend rule can apply.

Official rule sources:
- https://magic.wizards.com/en/news/feature/avatar-the-last-airbender-release-notes
- https://magic.wizards.com/en/news/feature/outlaws-of-thunder-junction-release-notes

## Alternatives actually tested / stopping decision

The five complete full-100 singleton options and exact raw hashes are documented in `Fire_Lord_Azula_M7_Independent_Audit_Checkpoint_2026-10-24.md`; companion test: `tests/test_m7_fire_lord_azula_chatgpt_alternatives.py`. In particular:

- **REJECT** Grok #667 five because its proposed cuts of Swan Song and Gemstone Caverns lose disproportionately useful cEDH one-mana stack interaction and turn-zero mana acceleration.
- **REJECT** extra Unexpected Windfall over Vivi as strictly better: **Big Score and Windfall both cost two other mana after {R}{R} firebending**, Windfall needs RR outside combat, and 4-MV duplicate draw is not obviously stronger than attack haste.
- **REJECT FOR FINAL** sixth `+Mistrise Village/-Wooded Foothills` (`Electro Six` under review raw `5c50bffd5335e03e9739d1b1d8f552bf23cce0eb050bccabf0b53196b21ea25b`). The blue-only Village sometimes enters tapped and displaces a live fetch in a 26-land UBR cEDH deck. It does give useful {U}+{T} next-spell uncounterability, but **not enough proven net value in this precise shell**, where Hexing Squelcher and substantial countermagic already defend key wins. This is a reasoned stopping point beyond five, not a five-swap cap.
- **REJECT FOR FINAL** preserving Samut Tyrant and skipping Turnabout: makes self-interaction with Narset's Reversal and Electro/Beseech free casts worse, forfeits a verified Azula-dependent combo.
- **REJECT FOR FINAL** dropping Redirect Lightning without an explicit protection cost statement: documented above for Cory's owner-level scrutiny.

## Verification gates and limits

- Candidate string: **100 quantity-1 lines, first line `1x Fire Lord Azula [Commander]`, 100 distinct names**, 26 land faces including one MDFC, 20 Game Changers.
- Frozen card source: `data/grixis/m6/oracle_snapshots/Fire_Lord_Azula_M7_Scryfall_20261023.json`: 205 names. Each candidate's current archived Scryfall Oracle resolution, UBR/identity, and `commander_legality == legal` verified by independent targeted test; no project exception or unresolved card. Explicit target-vs-timing interaction checked against above official Wizards notes.
- Exact raw SHA check, baseline SHA, protected Swan Song / Gemstone Caverns / Hexing Squelcher, five exact add/cut diffs, Big Score vs Windfall mana payment, MDFC/Ad Nauseam costs, copy/flashback ability text, and finite castability proxy are included in the test.
- Finite turn-four Azula castability proxy **baseline 0.4920 vs chosen 0.4900** with MDFC as a land, or **0.4626** with MDFC never as land (draw 0.5834). This rough combinatorial source model treats fetches as rainbow, ignores many fast mana/ramp/haste/sequencing/tapped-land constraints, and is **not a match win-rate estimate**. Real-world play testing/opponent interaction remains unmeasured.
- **CI gate:** recheck exact GitHub PR #694 HEAD `azula-exploratory-alternatives` after final packet commit; previous intermediate head `41b10b565eda6f55cd117b3627106a8124edba09` passed. Do **not** label the final commit CI-passing until it is verified.

## Explicit approval boundary

This entire packet is **approval-ready research only**, with no changes to the canonical `main` branch or `state/current_deck_overrides.json`. Cory must see the exact full 100 and explicitly approve raw SHA `77ac26a4f4ff70d0a7a666b07fa9fe051e52fe0547d8320d84490d088c0cc273` before a canonical PR, tracker update, merge, or lock. Any owner rejection reopens the strategic comparison; any materially altered card list requires a **new hash and fresh approval**.
