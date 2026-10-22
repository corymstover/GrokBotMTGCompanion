# Admiral Beckett Brass — source-complete 121-card Oracle refresh and third full package

**2026-10-22, RESEARCH_ONLY.** Supplement to the complete opportunity audit (merged PR #590). No canonical deck mutation, final M7 owner presentation, M6.10 certification or owner acceptance is authorized by this record.

## Complete current source verification

On Oct 22, queried Scryfall's `POST https://api.scryfall.com/cards/collection` using **each exact canonical approved card name (97 distinct)** and **all 24 substantive additional material challengers** in two bounded requests (75 and 46 items, both returned all items, `not_found=[]`). The immutable response projection is the adjacent `Admiral_Beckett_Brass_Full_Source_Oracle_20261022.json`, including 121 Oracle IDs, present oracle texts, mana costs, type lines, Commander legalities and actual color identities. **121/121 resolved; 121/121 Commander legality = `legal`; 121/121 color identity ⊆ U/B/R; no exceptions or card-face omissions.** The snapshot confirms card-name identity and current recorded legality, not commander-optimality. A future legality change needs a fresh source check before approval.

Exact canonical byte mirror remains SHA-256 `4ba5c483eb67b5f2647d375450adf9c2b7e79a036d0ba1866e58de8441bf3414`. A package list has 100 physical cards and is not a replacement for the locked canonical source. Current source-bound role counts computed from present Scryfall card types:

| Full configuration | Physical cards | Land cards | Creature cards | Printed Pirate/changeling creatures | M7 disposition |
|---|---:|---:|---:|---:|---|
| Canonical locked | 100 | 35 | 34 | 33 | Old approved, not replaced |
| Package A — faster breakthrough | 100 | 35 | 34 | 33 | RESEARCH_ONLY |
| Package B — slower grind and fleet buffs | 100 | 35 | 33 | 32 | RESEARCH_ONLY; comparatively disfavored |
| Package C — resilient early Pirate evasion | 100 | 35 | 34 | 33 | RESEARCH_ONLY; currently favored for examination |

## Package C — retain both incumbent engines while advancing early connection

Fully specified exact 100-card source: `Admiral_Beckett_Brass_resilient_connection_package.txt`.

Research-only raw SHA-256: `4944605fdd284d1eca9caca7a18d2d1a82705c9add891f11aff15558bf830dce`. This is **not** a final M7 approval hash or certifying I/J bundle. Full 121-record Oracle source snapshot SHA-256: `5b8ee25e57d061bbd3d754402668ade7cdac6b2946ae01be378194bc98a5eac8`.

| ADD | CUT | Specific commander-first tradeoff |
|---|---|---|
| City of Brass | Crumbling Necropolis | Same 35-land count and U/B/R access; City untapped on entry but deals one triggered self-damage on tapping. |
| Departed Deckhand | Daring Saboteur | A {1}{U} Spirit **Pirate** with passive non-Spirit evasion, freeing 3 mana per connection attempt; targeted spells sacrifice it and Spirit blockers still work. |
| Cloud Pirates | Dire Fleet Captain | One-blue 1/1 flying **Pirate** can be deployed earlier as a distinct source; loses a growing two-drop Pirate attacker and cannot block ground creatures. |
| Skyship Plunderer | Dire Fleet Poisoner | A {1}{U} 2/1 flying **Pirate** at the same MV as Poisoner; incremental existing-counter value on connection, loses Poisoner's instant-speed flash/deathtouch combat defense. |
| Blustersquall | Open into Wonder | Four-mana overload taps all opponents' potential blockers at instant speed, compared with XUU sorcery-speed guaranteed unblockability *plus cards drawn* on hits; X=3 costs 5 mana. A powerful card-draw/evasion tool is being sacrificed; this is not a free upgrade. |

**Why C is meaningfully distinct from A:** C **keeps both Merchant Raiders and The Indomitable**. Raiders repeatedly pins blockers as Pirates enter; Indomitable draws from any creature hit and can be recast from the grave with correct conditions and costs. C gains three early *evasive Pirate creatures* instead of A's Broadside haste/menace/boast route. The pirate source count and lands remain unchanged, while the package improves one-drop/flying-source density. C does lose Open's exceptional unblockability and hit-based draw and Poisoner's combat trick; those may still outweigh the gains. This contrast is serious because one can improve opening connection frequency but weaken ability to rebuild after removal. Neither list is proven best by the five-swap count.

## Decision-grade adverse *finite* comparisons, not invented win rates

1. **Two 3/3 grounded non-Spirit blockers, no flyer/reach, no removal, three attack-ready Pirates:** C's Departed Deckhand, Cloud Pirates and Skyship Plunderer all evade those blockers; three distinct Pirates can deal combat damage if the opponent takes it. A's Departed Deckhand and Skyship Plunderer can deal damage but Broadside Bombardiers (menace) can be blocked by **both** ground creatures. A needs a legal removal line or an additional four-mana Blustersquall overload to secure the third hit. Sacrificing a Treasure to Broadside's boast deals only **2** damage, insufficient to kill either 3/3 blocker; cannot declare an unproven three-source steal.
2. **A haste window:** If Broadside is just cast before combat, its printed haste means it can attack immediately. C's just-cast Cloud Pirates lacks haste and cannot join that combat, although its mana cost is only {U}. The previous fixture deliberately required all three Pirates already attack-ready. A is preferable in some post-wipe recast hands.
3. **Longer games:** A cuts repeatable Raider blocker taps and Indomitable card draw; C retains both, whereas C loses Open into Wonder card draw and Poisoner's reactive deathtouch. C is likely more stable when Commander theft must be attempted repeatedly; the relative value depends on availability of Open and timing of two-flyer attacks, not a fabricated win-rate number.
4. **Real counterplay:** Any Fog stops combat damage; a Spirit can block Departed Deckhand; a creature with flying/reach can block Skyship or Cloud Pirates; the third Pirate may be killed before damage; the commander must exist when the end-step trigger would begin; a targeted stolen permanent must stay legal on resolution. Blustersquall cannot by itself prevent these effects.
5. **Colored mana:** Cloud Pirates needs {U} on turn one, and Skyship/Deckhand need U on turn two; City creates a tempo opportunity but doesn't guarantee U in the opener. There are exactly **three** fetchlands in the canonical source (Bloodstained Mire, Polluted Delta, Scalding Tarn), alongside unrestricted rainbow lands and tribal-restricted/colorless sources with real colored-pip limitations.

## Qualitative conclusion, remaining certification

The *research preference* advances from A toward **C as the better-sustained three-source strategy**, pending critical re-evaluation of two high-quality incumbent cuts (`Open into Wonder`, `Dire Fleet Poisoner`). The evidence supports three real alternatives, not a declaration of global or tested-pool optimality. No further large simulation is warranted before resolving the exact Open/Blustersquall role tradeoff and realistic paid attack windows with a small bounded fixture. The original 13 Admiral M6 blueprint cases already executed and passed under limited finite contracts; do not rerun unchanged fixtures merely to inflate counts.

**Still required for owner readiness:** decide between final packages without padding to five swaps, verify changed-source M6 I/J and reproducibility bindings, verify mana sequencing/opponent response cases relevant to the *chosen* exact list, compute its **fresh** final source-bound raw SHA-256, pass the full M7 schema/gate and exact-head CI, and obtain explicit owner approval of that exact 100 before touching the canonical repo. Historical approvals, 121 Oracle lookups and local structural tests do not satisfy those remaining steps.
