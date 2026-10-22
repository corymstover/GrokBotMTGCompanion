# Abaddon — one physically joined paid-Ignus / cascade-effect subset

**M6.6 bounded engine study, October 22, 2026.** Pre-registered immutable decisions at commit `701f88d31e140afc09e81a8f327d3cdd927256d8` before implementation. Source: approved Abaddon one commander + 99-card physical library, canonical raw SHA-256 `2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf`, engineering frozen source `5448d76193923a3f9e3d4c41a327eaeaa9c6326d484d8e5a9abaf3852db2efff`. Nothing changed in the canonical list.

## What is newly joined

PR #520 **paid for Ignus casts but never resolved cascade**; PR #522 **resolved hypothetical first cascade exiles and legal cast opportunities but did not assemble or pay for Ignus**. This fixture now takes the **same exact mutable 99-card library, physical hand, land sources/taps, graveyard, battlefield, floated U/B/R/C mana and within-turn opponent life-loss** through each of ten own turns. It uses the same matched fixed source-bound card selection and two engine/burn casting orders as #520. An Ignus cascade trigger is possible only after paying for a real **Ignus hand cast** while Abaddon is already present and the opponents collectively lost at least three life this turn. Birgi's **front-face** red cast trigger must resolve in the registered stack order before that Ignus cascade; casting a hit from exile grants **a separate Birgi trigger, not Abaddon hand-only cascade**. At most five extra real mana-paid Ignus bounce/recasts per main phase, with cascade effects feeding the exact same mana and library state. Exact physical zone conservation is checked on **every simulated turn** (99 physical cards, commander outside library), including fetchlands as graveyard sacrifices.

**This is not the 99-card rules engine:** the casting policy *only* plays Birgi, Familiar, Abaddon, two initial burn spells, Rakdos, the proposed Ignus, and Assault (Assault activation deliberately omitted); initial mana sources are modeled lands only, supplemented by *supported cascade-created mana*. All other source cards, card-selection effects, spells from other zones, cascade triggers on other qualifying hand spells, full storm, commander recast tax, opponents' interaction, combat/Neheb/Loyal, and wins remain out of model. These omissions can bias decisions in both directions. This also assumes once-controlled permanents survive the observed turns.

## Actual source-verified effects covered

Under the preregistered conservative casting subset, **the FIRST eligible card** with MV < 3 is found and exiled from the actual mutated library on each paid Ignus cascade. If it is unsupported, the pilot declines that cast (it **cannot** skip to the next favorable hit). Uncast exiled cards are returned to the library bottom in seeded random order. For verified supported hits, effects actually run before original Ignus resolves:

| Source card | What changes in this shared state |
| --- | --- |
| Dark Ritual | Add `{B}{B}{B}`; go to physical graveyard |
| Rite of Flame | Add `{R}{R}`, with the documented own-graveyard count of other Rites when relevant; opponents' graveyards not modeled, so undercounts uncommon extra-red cases |
| Boltwave | Three damage to each of three opponents; +9 aggregate opponent life lost |
| Flame Rift | Four to each of three opponents (+12 aggregate), four damage to pilot |
| Ancestral Vision | Choose yourself; draw three **physical cards** from the actual library |
| Sol Ring | Enter battlefield and tap once for `{C}{C}`; untaps on future modeled turns, but cannot double tap this turn |
| Lotus Petal | Enter, tap and sacrifice; choose red, move physical card to graveyard |
| Profane Tutor / Demonic Tutor | Search **the actual remaining library**, remove one real prioritized target into physical hand, seeded shuffle |
| Vampiric Tutor / Imperial Seal | Search physical library, shuffle, place a real found card on top, pilot loses two life; **not** free instant hand access |
| Gamble | Search/shuffle a real card to hand, then randomly discard exactly one from physical hand (possibly the tutored card) |

The priority search policy chooses available Boltwave, Flame Rift, Rite of Flame, Dark Ritual, Sol Ring, Lotus Petal, Familiar, Birgi, in order, then lexical first eligible nonland. Tutor policy is **not** a claim of optimal gameplay; its decisions are fixed and auditable.

The other qualifying first hits (including **Lion's Eye Diamond**, **Chrome Mox**, **Mana Vault**, Arcane Signet, Talismans, Inevitable Betrayal, Swan Song, Flusterstorm, and all other unmodeled spells) **are declined, not counted as if they generated useful mana, stolen a creature, or resolved to victory**. No wishful free artifacts. Conditional opponent grief (Rule of Law, Drannith, removal/counterspells) is represented only by earlier isolated cases; no fictitious response frequency.

## What a successful test can and cannot conclude

The output records both **paid real Ignus cascades** and *actually resolved* supported cascade effects in the same seeded trajectory, including physical cards drawn, tutored, damage and added mana. It directly fixes the prior disjoint-snapshot weakness, but still omits enough other real effects that it **cannot** estimate genuine combo reliability or assign a win rate. Any positive count does not establish that `+Ignus/-Rakdos`, `+Ignus/-Familiar` or `+Ignus/-Rite` is stronger; no direct comparison of Rakdos threat/damage/discount or Assault Neheb line is scored.

**Decision:** keep `Grinning Ignus` as a serious commander-specific **HOLD** candidate pending comprehensive gameplay and protection opportunity-cost testing. Approved Abaddon unchanged. M6.6 and M6.7 remain PARTIAL, M6 certified 0/62, M7 new owner approvals 0/62.

**Authoritative Oracle:** `corymstover/grixis-commander-encyclopediaGPT/refinement/tests/Abaddon_Current_Card_Audit_2026-10-13.csv`, including the correct Oracle text of all 12 resolved effects. Physical cards and immutable candidate costs from engineering graph and preregistration files. The authorized owner waiver changes the third-reviewer independence requirement only; it does not certify any of these games.
