# Admiral Beckett Brass D — exact-deck mana and development preflight

**2026-10-22 · M6 J supporting research, NOT a completed J bundle, M6.10 acceptance, or owner-ready M7 list.** Canonical approved raw hash remains `4ba5c483eb67b5f2647d375450adf9c2b7e79a036d0ba1866e58de8441bf3414`. Candidate D is physically 100 cards, raw hash `201a1d5fc90e30d6aff9a565603fcf8caef69604dad2c07b4951be2b41cc92ee`, logical `lh1:1f6ae6fa721c3bd7e8b888c4a216edca7cdb25c587d5ce812282662cb0118d58` (registry's sorted `zone|oracle_id|qty` formula). Current card authority: `data/grixis/m7/research_challengers/Admiral_Beckett_Brass_Full_Source_Oracle_20261022.json` (121 resolved names, all UBR Commander legal on October 22).

## Actual construction and mana costs

- Exactly **35 land cards** both before and after, with **3 Island, 2 Mountain, 1 Swamp**, and **3 one-life fetch lands** (Bloodstained Mire, Polluted Delta, Scalding Tarn). Fetch color depends on which *typed* dual is still in the deck/library and can be found; a fetch is not a free five-color mana source.
- The sole land replacement is **City of Brass IN / Crumbling Necropolis OUT**. City can produce the necessary color on its entry turn, but **each time it becomes tapped, its triggered ability deals 1 damage** to its controller. Crumbling always entered tapped and never caused that damage. The remaining **Path of Ancestry** and **Xander's Lounge** also unconditionally enter tapped. Check-land and slow-land availability is conditional, not a guaranteed untapped source on turn one.
- **Cavern of Souls** and **Secluded Courtyard** can produce generic colorless mana for general use. Their five-color abilities are restricted to the chosen creature type. With *Pirate* chosen they can cast Admiral Beckett Brass or other Pirates, but not freely pay colored costs for Counterspell or a non-Pirate spell. **Exotic Orchard** depends on what lands opponents control. **Mana Confluence** has an actual 1-life activation cost; Ancient Tomb and Shivan Reef deal damage through their printed effects. Never treat these constraints as interchangeable.
- D contains **34 creature cards, 33 printed Pirate/changeling creature cards**. Its creature mana-value distribution *including the commander* is **6 at one, 8 at two, 7 at three, 8 at four, 5 at five**. The canonical counterpart is **5/9/7/8/5**, so this is one deliberate move into the turn-one Pirate slot, not an invented huge reduction in average curve.
- The three new evasive Pirates all want blue mana early. City improves an exact-turn U/B/R bottleneck but does not make every hand castable; fetch decisions, untapped conditions, blue-source distribution, hand texture, life budget and opponents still matter.

## Verified one-state turn-four payment

| Turn | Available land, tap and exact payment | Spell and implication |
|---|---|---|
| 1 | Underground Sea taps `{U}` | Cloud Pirates `{U}`; attacks only from turn 2 |
| 2 | Volcanic Island `{U}` plus Sea `{U}` as one generic | Skyship Plunderer `{1}{U}`; attacks only from turn 3 |
| 3 | Sea `{U}` and Badlands `{B}` as generic | Departed Deckhand `{1}{U}`; attacks only from turn 4 |
| 4 | Sea `{B}`, Volcanic `{U}`, Badlands `{R}`, City `{R}` as generic | Admiral `{1}{U}{B}{R}` before combat; City trigger deals 1 self-damage |

If the three older Pirates deal combat damage to **one same opponent** and a nonland permanent controlled by that opponent is a legal target at beginning of endstep while Admiral is present, the commanded theft trigger may occur. A grounded opponent board with no Spirits/flyers/reach gives a plausible protected line. Any missing land, Spirit or flying/reach blocker, Fog, correctly timed removal or absent target can defeat the line. This is a **conditional payable witness**, not the odds of drawing seven exact cards or a goldfish win rate.

Executable receipts: `tests/test_m6_admiral_beckett_pirate_density_candidate_turn4.py` (GitHub Actions #39853282652) and `tests/test_m6_admiral_beckett_candidate_d_adversarial.py` (GitHub Actions #39857260951). Full deck legality and structural checks: `tests/test_m7_admiral_beckett_full_source_and_resilience.py` and `tests/test_m6_admiral_beckett_ij_preflight.py` (the latter must receive exact-head CI in its own PR). All are deterministic bounded evidence; none computes full multiplayer matchups or certifies M6 I/J.

**Remaining for final J:** Bind this report's actual committed raw SHA-256 in a complete bundle, along with exact Oracle/rules, source-backed full-list logical hash, all sealed/waived provenance, valid Phase B receipts and red-team report. Do not set `phase_b.complete=true` until the outstanding candidate-specific coverage and I reconciliation are genuinely adjudicated.
