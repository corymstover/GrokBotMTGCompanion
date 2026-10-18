# Cycle 112 — Three distinct commander-first strategic reviews

**Status:** source-anchored strategic judgments by the engineering author, **not** an independent Pass C reviewer, completed Phase B, owner-approved swap, tested-pool zero-improvement certificate, or milestone acceptance.

Preregistered plan: `data/grixis/m6/phase_b_plans/cycle112_commander_review_batch_01.json` (first plan commit `e43d873e71483cdbfcffa1c702e971cd1c27056e`). Complete authored evidence: `data/grixis/m6/author_reviews/cycle112_three_commander_authored_judgments_01.json`. Deterministic archived Oracle/source verification: `data/grixis/m6/phase_b_bounded/cycle112_commander_first_reviews_01.json`.

The three full approved 100-card source lists remain intact, with recorded raw SHA-256:

| Commander | Raw approved list SHA-256 | Proposed add / cut | Author decision |
|---|---|---|---|
| Cormela, Glamour Thief | `80f4bdef2b8b140aeae23775cfdf87fda81e7215038b8db9b1746c806f366e0b` | Archaeomancer / Faithless Looting | **HOLD** |
| Ashnod the Uncaring | `f574e4fad4749603294f53d2fe5536a159f884a8f1a8a7b6b1a22b3a637cf1cf` | Detective's Satchel / Dockside Chef | **HOLD** |
| Gwendlyn Di Corci | `9a393cb7edf40f9bfb388d37dd657839cad851dc6a021440c7d1b239c1fd20a9` | Aphetto Alchemist / Opposition Agent | **IDENTITY-POSITIVE CANDIDATE, UNRESOLVED — NO SWAP** |

## 1. Cormela — Archaeomancer for Faithless Looting

**Current 100-card strategy:** cEDH instant/sorcery loops leveraging Cormela's haste, restricted ritual activation, death recursion, Saw in Half, reanimation spells and compact storm/protection. The approved list has Faithless Looting, Goryo's Vengeance, Shallow Grave, Molten Duplication, Saw in Half, rituals, and artifact sacrifice access.

**Rules fact:** Cormela's `{1}, {T}: Add {U}{B}{R}` mana is spendable **only to cast instant and/or sorcery spells**. It cannot pay any part of Archaeomancer's four-mana creature casting cost. Archaeomancer does return an instant or sorcery from graveyard on entry, but it must enter and trigger; Cormela already returns one when she dies. Faithless Looting is a one-mana sorcery that draws two, discards two, and can be cast again with flashback.

**Commander-specific tradeoff:** Adding slow creature ETB recursion raises the cost of assembling the engine while removing one of the most efficient ways to move required spells into the graveyard, reselect cards and exploit Cormela's own instant/sorcery-only mana. The M5 packet labels the swap source agreement and exploratory test-pass, but its annotated Spellbook completions do not establish reliable access, faster wins or stronger commander participation. Nor does the swapped-in card replace a unique current loop.

**Decision:** retain Faithless Looting. Investigate Archaeomancer only if a separately verified, affordable Cormela-specific recursion line materially outperforms existing Saw in Half / reanimation routes. **Do not swap.**

## 2. Ashnod — Detective's Satchel for Dockside Chef

**Current 100-card strategy:** copy nonmana activated abilities whose **own activation costs** sacrifice artifacts or creatures; generate or recur artifacts with Trading Post, Time Sieve, Scrap Trawler, Myr Retriever and stations, converting repeated activations into draw, value, turns and damage.

**Rules fact:** Dockside Chef is a `{B}` permanent with `{1}{B}, Sacrifice an artifact or creature: Draw a card`. Sacrificing an artifact or creature pays for *that very ability*, so Ashnod copies it once, giving two draws from the sacrificed permanent when Ashnod is available.

Detective's Satchel costs `{2}{U}{R}`, investigates twice as it enters and therefore creates two Clues. **The Clues' own** `{2}, Sacrifice this artifact: Draw a card` activations also qualify for Ashnod's copying effect, so the card has *real commander synergy*. However, Satchel's `{T}: Create a 1/1 Thopter` activated ability is conditioned on an earlier artifact sacrifice; no sacrifice is paid as a cost of the Satchel's ability itself, so **Ashnod does not copy that Thopter ability**. Current Ashnod Oracle has neither a once-per-turn restriction nor an exclusion of sacrificed token permanents.

**Commander-specific tradeoff:** Satchel supplies a few Clues and conditional Thopters but demands four mana before the Clue activation costs, whereas Chef is a cheap, repeatable sacrifice outlet that converts varied artifact and creature fodder into copied draw. Removing Chef also eliminates its ability to sacrifice arbitrary artifact/creature permanents for other triggers and recursion lines. M5 test-pass cannot determine which effect provides more net usable draw and engine cycles.

**Decision:** retain Dockside Chef. Detective's Satchel may remain a separate add candidate against a different weaker cut if a real game-state model demonstrates useful extra Clues/Thopters at acceptable tempo. **Do not swap.**

## 3. Gwendlyn — Aphetto Alchemist for Opposition Agent

**Current 100-card strategy:** repeatedly activate Gwendlyn's on-your-turn `{T}` random discard via haste, untappers, and Illusionist's Bracers; convert real opponent discards/wheel refills to Waste Not, Liliana's Caress, Geth's Grimoire and Tinybones value. Existing enablers already include Pemmin's Aura, Minamo, Magewright's Stone, Patriar's Seal, Thousand-Year Elixir and Lightning Greaves.

**Rules fact:** Aphetto Alchemist's `{T}: Untap target artifact or creature` can untap Gwendlyn for another legal discard activation **on the player's own turn**, subject to Alchemist's own summoning sickness, available targets and ability timing. If Illusionist's Bracers is equipped to Alchemist, the copied untap can target Alchemist while the original targets Gwendlyn (or the other way around), allowing repeated untapping while source and timing constraints permit. The Bracers would be on **Alchemist**, not Gwendlyn, so they no longer simultaneously copy Gwendlyn's activation. If Pemmin's Aura grants Gwendlyn shroud, Alchemist cannot target her. Opponents' finite hands and hand-refill access prevent treating repeated activation as an automatic kill.

**Tradeoff:** Unlike the first two proposals, Aphetto adds an immediately relevant commander engine. But replacing Opposition Agent removes flash interaction with opposing library searches, opponents' tutor suppression and potentially valuable exiled-card access. The approved deck has other untappers, so the marginal extra Gwendlyn activations and their usable discard triggers must exceed this lost interaction in the appropriate bracket. M5 combo-pass is not an opponent-interactive performance measurement.

**Decision:** Aphetto Alchemist is a **legitimate, commander-first candidate to pursue**. Its proposed cut is not yet justified. Keep the current list. A follow-up test must compare actual Gwendlyn activation counts with/without Alchemist, whether Bracers is equipped to the commander or Alchemist, legal shroud states, opponent hand sizes and Opposition Agent's prevented tutor value. An independent strategy reviewer must then evaluate the evidence before any user-approved exact swap.

## Verified scope versus open gates

The CI-generated receipt checks the named cards' archived Oracle text, approved 99+1 list composition, baseline card presence/absence, blueprint primary plan, identity core and M5 packet provenance. It is a bounded **source-and-rules text verification**, not a full card rules-engine simulation or date-current legality certification.

No 100-card list changes. No new user approval. No formal independent Pass C, complete Phase B or tested-pool no-improvement certificate issued. Existing approvals remain locked and M6 remains in progress.

**Next project step:** commission skeptical *independent* review of these exact author judgments; prioritize a limited Gwendlyn activation-vs-opp-search-interaction test, then continue a new diverse commander batch rather than reopen completed or untouched approved lists.
