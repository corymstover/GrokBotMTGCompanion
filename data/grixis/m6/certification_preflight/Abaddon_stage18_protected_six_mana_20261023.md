# Abaddon protected-wheel six — candidate-specific M6 J mana and curve assessment

Status: **authored candidate-specific resource evidence, not a simulation or final M6 J certification**. 2026-10-23, America/Chicago.

- Exact locked canonical source: `corymstover/grixis-commander-encyclopediaGPT/main/refinement/decklists/Abaddon_the_Despoiler_M7_Approved_2026-10-22.txt`; raw SHA-256 `0d9f6df80cafc2a380199b7aec8112e4e54ccfec70024679607032cdf10f5790`.
- New research-only six: `data/grixis/m7/research_challengers/Abaddon_the_Despoiler_stage13_protected_wheel_six_research_20261023.txt`; raw SHA-256 `5ab1a3628352016be52233917b27ce8cbb0a538916fe757a5384cd06ad3dee24`. **100 physical cards, Abaddon commander first, 34 lands, 95 names**. Six real additions/cuts: Impact Tremors/Thermo-Alchemist, Sanctum of Stone Fangs/The Ruinous Powers, Coruscation Mage/Kessig Flamebreather, Sakashima of a Thousand Faces/Keeper of Secrets, Mount Doom/Mountain, Sheoldred, the Apocalypse/Ponder.
- Source-bound all-95 Oracle and identity record: `data/grixis/m6/oracle_snapshots/Abaddon_the_Despoiler_Stage17_95_Source_Reconciled_20261023.json`. Direct exact-head live Scryfall full100 replay: [PR #636, run 39906252605](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/39906252605). New-candidate paid interaction cases: [PR #638, 14 passed, run 39906969961](https://github.com/corymstover/GrokBotMTGCompanion/actions/runs/39906969961).

## Exact mana differences

The list **preserves 34 lands** but replaces the *third* basic Mountain with Mount Doom. Its seven physical fetch lands remain Bloodstained Mire, Flooded Strand, Marsh Flats, Misty Rainforest, Polluted Delta, Scalding Tarn and Verdant Catacombs. There are still three Swamps and three Islands, but only two basic Mountains. Badlands, Blood Crypt, Underground Sea, Watery Grave, Steam Vents, Volcanic Island and Xander's Lounge remain fetch-reachable typed lands; dual production depends on their actual Oracle land types and the fetch being able to find one still in the library. Exotics/conditional lands are not all unconditional colored sources: Exotic Orchard needs an opponent's producing land, Xander's Lounge enters tapped, and Mount Doom pays **one life every time** its tap ability adds B/R. City of Brass and Mana Confluence have their own costs. The old candidate's unchanged-land no-risk claim **does not transfer**.

Added spells move curve/colored requirements in opposing ways:

| Added | Removed | Payable-resource consequence |
| --- | --- | --- |
| Impact Tremors `{1}{R}` | Thermo-Alchemist `{1}{R}` | Same nominal pip/turn-two window, but Tremors requires a creature ETB rather than creature untap + tap activation; not an early guaranteed X3. |
| Sanctum of Stone Fangs `{1}{B}` | The Ruinous Powers `{2}{B}{R}` | Cheaper, fewer colored pips; loss occurs at **first main on a later turn** if shrine survives, not immediately at cast. |
| Coruscation Mage `{1}{R}`, optional offspring `{2}` | Kessig Flamebreather `{1}{R}` | Equal printed casting cost; any offspring token costs **two extra generic** to actually make a second ping source, including if Mage itself is cast free off cascade. |
| Sakashima of a Thousand Faces `{3}{U}` | Keeper of Secrets `{5}{R}` | Two lower MV but needs commander or worthy creature on entry; duplicate Abaddon cascade only from qualifying later hand casts, not free on its own entry. |
| Mount Doom | basic Mountain | Adds conditional B and own-turn {1}{B}{R},{T} three-opponent damage. This **consumes the land tap and three other mana** and cannot fund another spell with that same tap. |
| Sheoldred, the Apocalypse `{2}{B}{B}` | Ponder `{U}` | Removes premium one-mana blue top-three draw smoothing and adds a four-mana double-black spell, exposing black-pip and higher-curve hand risks. |

Abaddon costs `{2}{U}{B}{R}`; double black on Sheoldred is not interchangeable with commander UBR access. Seven fetches, typed black duals, Swamps, Urborg, black-producing premium lands and Talisman of Dominance/Indulgence supply meaningful access, but this document **does not calculate an observed turn-four double-black casting probability**. It would be dishonest to reuse the previous baseline's 500-draw proxy percentages for this new six-card replacement.

## Threshold timing, casts and hard costs

- At three opponents, Sanctum alone at a surviving *first main phase* gives X3 before a hand spell **on that turn**. It cannot give X3 on the same turn it was played after the beginning-of-main trigger window, and losing the shrine in response reduces shrine count at resolution. Bloodletter may double the resulting life loss on your turn; Solphim cannot double non-damage.
- Mount Doom can make X3 with a payable `{1}{B}{R},{T}` activation without casting a spell; absent enough other mana or a ready untapped Doom, there is no free X3. Rule of Law prohibits additional spell casts from cascades but cannot prohibit a properly paid land activated ability merely for being Rule of Law.
- Coruscation Mage plus paid offspring makes two separate source pings **on later noncreature casts**. An initial noncreature spell does not retroactively see the entering Mage or its offspring. Impact Tremors receives creature-entry triggers if both bodies enter, and may be removed before those triggers resolve; ordinary replacement and prevention effects apply.
- Sheoldred + fully resolving Wheel of Fortune giving seven draws to each of three opponents creates 21 *opponent draw events*, each losing two life, hence X42 on your turn **after those draw triggers resolve**; Bloodletter then potentially turns that into X84. The wheel **itself** does not gain Abaddon cascade from loss caused by its postcast draw resolution. Windfall hand-size-dependent draws cannot be hardcoded as seven.
- With Nightscape Familiar front-face Birgi + Grinning Ignus, each properly paid return/recast has a real net colorless progression under the previously certified finite assumptions; removing Familiar changes that throughput. All six variants preserve those three cards and Impact pays creature-entry damage; repeated casts are impossible under Rule of Law.

## Adverse colored-mana and opportunity-cost verdict

The added double-black four-drop alongside a five-mana tri-color commander can be slow against land denial, Blood Moon-style shocks, and awkward fetch sequences, especially after removing Ponder. However, compared with the alternative seven-card shell deleting **Noise Marine** or **Nalfeshnee**, the candidate keeps printed independent cascade and copy-on-exile payoffs while adding a second commander cascade source at MV4, two cheap early access tools and a draw-punishing wheel payoff. A provisional six-card selection is therefore strategically defensible **despite** the Ponder cost; it is not an empirical cast-turn improvement claim. Test or structurally revisit the Ponder-vs-Sheoldred slot if a later decision-relevant physical sample actually falsifies colored-mana availability, without padding swaps to reach a count.

**Mana decision: no seventh cosmetic land swap proposed.** No land should be called a free upgrade; Mount Doom's life/activation opportunity cost and reduction from three to two basic Mountains remain explicitly recorded. Full M6 I/J proof and Cory's new exact-list M7 owner approval remain outstanding.
