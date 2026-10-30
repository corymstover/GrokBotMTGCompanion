# Pack A4 — six specific printed illustrations behind the Ugin–Bolas story

**Reviewed 2026-10-30.** This is an additive follow-up to [Pack A3](PACK_A3_Tarkir_Ugin_Bolas_Story_Card_Connections.md), not a replacement for the protected 62-deck Grixis Encyclopedia or an approval of any new deck.

## What is newly verified

For each of the six cards, a reviewer opened the **actual Wizards story image** and the corresponding **Scryfall printing's art crop** side by side, checked that the painting (despite differences in crop and aspect ratio) is the same, and cross-checked the credited illustrator. The 2026-10-30 Scryfall Cards API record supplied a stable **printing UUID, Oracle UUID, and illustration UUID**. The [machine-readable six-record ledger](../data/lore_research/pack_a4_printing_art_matches_2026-10-30.json) retains both URLs and the precise IDs. The source images are **linked, not rehosted**.

| Card | Exact image-matched printing | Artist | Narrative tier from Pack A3 | Other printings reusing the same Scryfall illustration ID |
| --- | --- | --- | --- | ---: |
| [Crux of Fate](https://scryfall.com/card/frf/65/crux-of-fate) | `frf/65` · `e1d45374-a41b-4b3f-a7c8-3eb5ca767cf6` | Michael Komarck | **Direct scene caption** of the Ugin–Bolas confrontation | 3 |
| [Ugin's Nexus](https://scryfall.com/card/ktk/227/ugins-nexus) | `ktk/227` · `94002868-a48a-4ea8-bfce-17257078f5db` | Sam Burley | Official story time-travel device, and later illustration caption | 0 |
| [Crucible of the Spirit Dragon](https://scryfall.com/card/frf/167/crucible-of-the-spirit-dragon) | `frf/167` · `6bf563e0-1f42-4768-a667-3e120bdb6534` | Jung Park | Story-location caption | 2 |
| [Tomb of the Spirit Dragon](https://scryfall.com/card/ktk/245/tomb-of-the-spirit-dragon) | `ktk/245` · `eb6be7ab-8fad-4606-b623-f2188219d60b` | Sam Burley | Story-location caption | 2 |
| [Ugin, the Spirit Dragon](https://scryfall.com/card/frf/1/ugin-the-spirit-dragon) | **`frf/1`** · `58c1e824-c8a9-4312-8e4c-a29a26d189a4` | **Raymond Swanland** | Character portrait in the duel narrative | 5 |
| [Nicol Bolas, Planeswalker](https://scryfall.com/card/con/120/nicol-bolas-planeswalker) | `con/120` · `48ee3939-bc12-4275-a446-9de36f0b4672` | D. Alexander Gregory | Character portrait in the duel narrative | 2 |

**Result:** **6** specifically inspected source-image/printing pairs, with **20** Scryfall printing UUIDs sharing those **6** illustration UUIDs as of the dated query. Only the six representative pairs were directly visually compared. The other 14 are metadata-based same-illustration associations—not 14 new visual inspections, and not 20 literal duel scenes.

### Crucial Ugin printing correction

The *earliest indexed paper printing* in Pack A3 is [Ugin promo `ugin/1`](https://scryfall.com/card/ugin/1/ugin-the-spirit-dragon), issued 2015-01-17, with **Chris Rahn** art (`ffc481bb-314d-4d22-b959-3878649f7af6`). But the image captioned *Ugin, the Spirit Dragon* inside Wizards' [*The Reforged Chain*](https://magic.wizards.com/en/news/feature/reforged-chain-2015-01-21) expressly credits **Raymond Swanland**. Its visually matching printed art is [*Fate Reforged* `frf/1`](https://scryfall.com/card/frf/1/ugin-the-spirit-dragon), issued 2015-01-23, illustration UUID `47715ae0-7456-449e-ad32-0a7bc47a4e7a`. **Both are real cards; only `frf/1` is the direct art match to this official story image.** This is why earliest printing, printed name and exact artwork must be separate evidence fields.

### Evidence strength and guardrails

- **Direct event scene:** Wizards' [*The Reforged Chain*](https://magic.wizards.com/en/news/feature/reforged-chain-2015-01-21) places Michael Komarck's *Crux of Fate* illustration at the face-to-face duel. The image is now tied to a specific Scryfall printing. The title, placement and art do not establish that *every* reprint art shows that scene.
- **Time-travel device:** The [2014 Wizards design explanation](https://magic.wizards.com/en/news/making-magic/prose-and-khans-part-2-2014-09-22) connects *Ugin's Nexus* to Sarkhan's time travel; the [2018 Chronicle](https://magic.wizards.com/en/news/magic-story/chronicle-bolas-familiar-stranger-2018-08-01) captions Sam Burley's art. This does not require the illustration to depict Sarkhan crossing it.
- **Place, not duel:** [*Journey to the Nexus*](https://magic.wizards.com/en/news/feature/journey-nexus-2014-12-10) captions *Tomb of the Spirit Dragon*, and the [Chronicle](https://magic.wizards.com/en/news/magic-story/chronicle-bolas-familiar-stranger-2018-08-01) captions *Crucible of the Spirit Dragon*. Both are locations associated with the apparent grave, not unique paintings of Bolas striking Ugin.
- **Characters, not scenes:** The Ugin and Bolas planeswalker portraits appear inside the fight's text, but neither portrait alone shows the complete fight. The first-person events and Tarkir's original/revised branches retain Pack A's continuity separation.
- **Rules snapshot:** All six specific printing cards returned `legalities.commander = legal` on the **2026-10-30 Scryfall API** query, and their colors are compatible with a Grixis Bolas deck. This is not validation of any candidate 100-card deck or a permanent legality promise.

The offline [audit](../scripts/audit_lore_pack_a4_printing_art.py) and [four tests](../tests/test_lore_pack_a4_printing_art.py) guard **ledger consistency and tier separation**. They do **not** make live internet requests, compare source pixels in CI, or independently prove the dated human visual judgment. Future illustrations and live legality require a fresh dated review.

## Beginning the independent Ugin–Bolas lore-first Commander pilot

**Stage: research/architecture only; no assembled 100-card list, no new deck approval.** The approved *Nicol Bolas, the Ravager* Grixis Encyclopedia list and the separate [unmerged Ugin biography proposal PR #776](https://github.com/corymstover/GrokBotMTGCompanion/pull/776) are both out of scope and remain untouched.

The narrative has to cover: ancient twin origin and rivalry; Bolas's role in the Elder Dragon War; separate Meditation Realm and Tarkir duels; Sarkhan's altered Tarkir history; Ugin/Bolas's Planeswalker conflict; 2019 imprisonment; the 2025 escape and unresolved spark. An honest lore deck must not pass off symbolic mechanics as literal events.

Two viable structural directions need a complete new candidate-card audit before choosing a final build:

1. **Five-color full-history exhibit:** *The Ur-Dragon* as an explicitly symbolic primordial framing commander—not an asserted participant in the later duel. This permits real story cards such as **Yasova Dragonclaw**, **Sarkhan Unbroken**, **Narset**, **Nahiri** and **Sorin** alongside Ugin and Bolas, and can represent original Elder Dragon relations. It is strongest for **historical coverage** but gives up a Bolas-centered command-zone gameplay identity. The earlier *Ugin biography* draft is not a substitute and cannot be reused or approved implicitly.
2. **Grixis Bolas-vs-Ugin rivalry:** A newly written *Nicol Bolas, the Ravager* commander list with colorless Ugin in the 99 and the **six specifically matched cards** as research anchors. It makes the gameplay strongly Bolas-first, but must identify off-color figures such as Yasova and multicolored Sarkhan as **unrepresentable**, rather than pretending the reduced card pool covers the entire conflict.

**Next gate:** Independently grade a full candidate pool by `DIRECT_DEPICTION / CANON_REFERENCE / LORE_INSPIRED / MECHANICAL_SYMBOL`, verify specific illustration variants for chosen narrative beats, then test a fresh 100-card list for current color identity, legality, singleton, mana, gameplay and bracket. A full Archidekt import is appropriate **only** after this new deck is ready for Cory's separate approval. Preserve the six-image printing ledger regardless of commander choice.
