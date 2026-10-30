# Pack A3 — The Tarkir duel on printed cards

**Checkpoint:** 2026-10-30 · **Scope:** six primary-source-reviewed, tiered card/art links to the Ugin–Bolas Tarkir narrative, plus the events around Sarkhan's intervention. This is an extension of [Pack A](PACK_A_Ugin_Bolas_Elder_Dragon_Duality.md) and [Pack A2](PACK_A2_Elder_Dragon_War_and_Primeval_Lineages.md), **not** an Elder Dragon War event, a complete art archive or a finalized Commander deck.

## Direct scene evidence vs. nearby art

**One card is linked at the direct scene-caption level:** Wizards' [*The Reforged Chain*](https://magic.wizards.com/en/news/feature/reforged-chain-2015-01-21) positions an image captioned **Crux of Fate**, credited to **Michael Komarck**, precisely where the story depicts Ugin and Nicol Bolas facing one another above Tarkir. A card-name match alone would not have justified this tier. The official card-art placement now supports **`DIRECT_EVENT_SCENE_CAPTION`** for this named art, though it does **not** identify every printed version of the card as carrying that illustration (A030).

Other artifacts and landscapes are related but have lower grades:

| Card | Historical first indexed English-paper set | Tier | Why it qualifies, and what it does not prove |
| --- | --- | --- | --- |
| **Crux of Fate** | `frf` | `DIRECT_EVENT_SCENE_CAPTION` | [The Reforged Chain](https://magic.wizards.com/en/news/feature/reforged-chain-2015-01-21) places captioned Michael Komarck art at the face-to-face duel. **Direct illustrated-story context**, not a per-printing art match. |
| **Ugin's Nexus** | `ktk` | `OFFICIAL_STORY_DEVICE` | Wizards [specifically designed](https://magic.wizards.com/en/news/making-magic/prose-and-khans-part-2-2014-09-22) it as the time-travel mechanism needed for Sarkhan's narrative. A [Chronicle](https://magic.wizards.com/en/news/magic-story/chronicle-bolas-familiar-stranger-2018-08-01) also captions the card's Sam Burley artwork. **Design purpose**, not proof the art shows a specific crossing. |
| **Crucible of the Spirit Dragon** | `frf` | `STORY_LOCATION_ART_CAPTION` | [The Chronicle's grave-site passage](https://magic.wizards.com/en/news/magic-story/chronicle-bolas-familiar-stranger-2018-08-01) captions Jung Park's art alongside the canyon and hedron cocoon. **Identified location**, not the ancient duel itself. |
| **Tomb of the Spirit Dragon** | `ktk` | `STORY_LOCATION_ART_CAPTION` | Official [Journey to the Nexus](https://magic.wizards.com/en/news/feature/journey-nexus-2014-12-10) and [Chronicle](https://magic.wizards.com/en/news/magic-story/chronicle-bolas-familiar-stranger-2018-08-01) use Sam Burley's card artwork with the site of Ugin's supposed death. **Location**, not final confirmation of permanent death. |
| **Ugin, the Spirit Dragon** | `ugin` | `NAMED_CHARACTER_ART_IN_STORY` | Captioned character art accompanies the clash in [*The Reforged Chain*](https://magic.wizards.com/en/news/feature/reforged-chain-2015-01-21) and later visions in [*A Familiar Stranger*](https://magic.wizards.com/en/news/magic-story/chronicle-bolas-familiar-stranger-2018-08-01). Official stories credit different illustrators, so art versions cannot be conflated. |
| **Nicol Bolas, Planeswalker** | `con` | `NAMED_CHARACTER_ART_IN_STORY` | D. Alexander Gregory's named Bolas card art appears during [*The Reforged Chain*](https://magic.wizards.com/en/news/feature/reforged-chain-2015-01-21). **Character illustration**, not independently certified framing of the whole battle. |

The `ugin` and `con` set codes in this table are **earliest indexed English-paper printing rows** from the current historical snapshot; a promotional printing may precede or coincide with the retail expansion printing. A printed art version may differ. The full reproducible [audit](../data/lore_research/pack_a_tarkir_card_scenes_audit_2026-10-30.json) records each card's Oracle ID, dated first-indexed printing ID, source labels and context tier. **None of the six have an independent artist-to-Scryfall-printing-ID match certified yet.**

## The chronological card-to-event sequence

1. **Sarkhan reaches the past:** The [official Tarkir block synopsis](https://magic.wizards.com/en/news/magic-story/story-tarkir-block-2015-04-29) describes a journey approximately 1,280 years into the past. Wizards' [design explanation](https://magic.wizards.com/en/news/making-magic/prose-and-khans-part-2-2014-09-22) ties **Ugin's Nexus** directly to this time-travel storytelling requirement (A025, A029).
2. **Bolas meets Ugin:** In [*The Reforged Chain*](https://magic.wizards.com/en/news/feature/reforged-chain-2015-01-21), Yasova's rune pattern guides Bolas toward Ugin. As Sarkhan approaches, the dragons confront one another; **Crux of Fate** art is explicitly captioned at that moment (A026, A030).
3. **Dragon forces reverse:** Ugin calls dragons to aid him. Yasova's spell diverts them into attacking Ugin. **The printed Ugin and Bolas character pictures accompany this narrative**, but must not be promoted to uniquely certified spell-event images (A027).
4. **The crucial intervention:** Bolas strikes Ugin; Sarkhan shields the fallen dragon with a hedron cocoon. This creates the history in which Ugin survives and the dragon tempests persist, rather than the dragonless present Sarkhan knew. See [official synopsis](https://magic.wizards.com/en/news/magic-story/story-tarkir-block-2015-04-29) and [current plane guide](https://magic.wizards.com/en/story/tarkir-plane) (A028).
5. **The canyon becomes a remembered tomb:** Subsequent characters seek Ugin in the place associated with **Crucible of the Spirit Dragon** and **Tomb of the Spirit Dragon**, both captioned in Wizards stories. Their assumptions that Ugin is dead must be distinguished from the survival later established in revised continuity (A031–A032).

**Timeline safety:** The Ugin–Bolas confrontation precedes the branch-changing rescue. The original and altered Tarkir outcomes are **not** two consecutive battles or both true simultaneously in the same unchanged timeline. Also, the ancient **Elder Dragon War on Dominaria** is not this duel over Tarkir.

## Practical deckbuilding value

All six exact card names presently match the repository's historical card index. Their **historically indexed identities are black, blue-red-black, or colorless**, so all six are color-identity compatible with a prospective **independent Grixis Nicol Bolas Commander concept** at that snapshot. The four artifacts/lands/spells can represent actual locations, a time-travel device and a witnessed showdown. Ugin's colorless card can represent the opposed twin without a separate five-color commander. Current legality, present-day Oracle text, mana curve and bracket remain to be checked when a complete new 100-card list is built. **The approved 62-deck collection is immutable**; no modifications have been made to it.

This focused six-card sample provides a stronger research bar for later expansion: **direct scene caption → official story device → location art → character picture → merely thematic analogy**. The audit specifically refuses to treat the last three as interchangeable.

## Remaining evidence work

- Compare each directly captioned official illustration with each specific card printing's art/artist metadata and image ID before asserting variant-level attribution.
- Expand the story-spotlight mapping to the War of the Spark prison aftermath and the 2025 escape, retaining strict source/context grades.
- Build and independently verify a complete legal, mechanically coherent lore-first 100-card deck; present an approval-ready Archidekt block only after the card-by-card checks.

Replay: `python3 scripts/audit_lore_pack_a_scenes.py` and `python3 -m unittest discover -s tests -p 'test_lore_pack_a_scenes.py' -v`. The script checks primary-source boundaries, stable claims and the full historical name-to-printing-ID joins; it is **not** a machine art classifier.
