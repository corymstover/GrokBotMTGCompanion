---
title: "Card Data Conventions"
category: meta
tags: [conventions, card-entries]
issues: [96, 99]
generated_by: hand-written
sources: [scryfall]
related: ["EDH Standards.md", "Front-Matter Schema.md", "Card Index.md", "Knowledge Index.md", "Update Log.md"]
schema: 2
---

# Card Data Conventions

> How card entries are stored, formatted, sourced, and flagged. Applies to every file under [`cards/`](cards/).
> Related: [Card Index](Card%20Index.md) · [Knowledge Index](Knowledge%20Index.md) · [EDH Standards](EDH%20Standards.md) · [Project Goal](GOAL.md)

## Contents
- [Source of truth](#source-of-truth)
- [Storage layout (scales to ~33,000+ cards)](#storage-layout-scales-to-33000-cards)
- [Entry format](#entry-format)
- [Field definitions](#field-definitions)
- [Source flags & verification status](#source-flags--verification-status)
- [What counts as a "card" (universe)](#what-counts-as-a-card-universe)
- [Ingestion order](#ingestion-order)
- [Editing rules](#editing-rules)

## Source of truth
- **Scryfall** `oracle_cards` bulk data (<https://api.scryfall.com/bulk-data>) — one object per Oracle ID, with current Oracle (errata'd) text.
- Entries are **generated, never hand-typed**, by [`scripts/ingest_scryfall.py`](scripts/ingest_scryfall.py). Every run regenerates all existing entries from the newest bulk file, so Oracle errata and legality changes propagate automatically.
- **Rulings** come from Scryfall's `rulings` bulk file (<https://api.scryfall.com/bulk-data/rulings>), joined to cards by `oracle_id`, and are rendered **inside each card entry** (see [Rulings](#rulings)).

## Storage layout (scales to ~33,000+ cards)
```
cards/<FIRST LETTER>/<prefix>.md              e.g. cards/S/so.md (Sol Ring …), cards/T/thea.md ("The A…")
cards/0-9/0-9.md                               names starting with a digit
data/card_index.csv                            one row per ingested card (machine-readable index)
data/ingest_state.json                         resumable ingestion state + next target
data/priority_cards.txt                        names ingested before the rank queue
data/categories.json                           curated category trackers (shown in Card Index)
```
- Every shard starts with YAML front-matter (`kind: shard`, `prefix`, `cards`, `bulk`; Bot cycle 17, see [Front-Matter Schema](Front-Matter%20Schema.md#card-shard-keys)), written by `scripts/front_matter.py`, which `ingest_scryfall.py` calls after each render.
- A card cited by any page gets one **Referenced in** line (Bot cycle 18, #66) just before *Source flags*: page count by kind and a link to its section in the [reverse card index](references/README.md). The line is rendered by `ingest_scryfall.py` from `data/card_refs.json` and refreshed by `scripts/build_crossrefs.py`; the full list lives in `references/` so shards stay lean.
- **Phase 8 card enrichment** (Bot cycle 33, [#99](https://github.com/corymstover/GrokBotMTGCompanion/issues/99)): an enriched card gets a **Lore** line and a **Synergy** line just before *Referenced in*. They are rendered by `ingest_scryfall.py` from `data/card_enrichment.json`, so a re-import keeps them, and refreshed by `scripts/build_card_enrichment.py`. The *Lore* line lists the lore entries that depict / feature / only name-match the card, with their official citations, Story Spotlight printings and flavor text found on official pages. The *Synergy* line has a *Proven* tier (KB decks, Commander Spellbook, EDHREC) and a *Guidance (Oracle pattern)* tier (EDH Packages). Neither repeats Oracle text or rulings. Format and coverage: [Card Enrichment](Card%20Enrichment.md). Since Bot cycle 34 the *Lore* line can also cite card art shown on an official story page; this counts only when the caption names the card and the artist matches a printing.
- Shard key = card name with accents stripped and all non-alphanumerics removed, lower-cased (*Æther Vial* → `aethervial`; *Rogue's Passage* → `roguespassage`).
- Prefix = first **2** characters, deepened to 3, 4 or 5 characters when that prefix would hold more than **350** cards across the *full* universe (so `ma` → `mag`, `mal` …; `th` → `tha`, `thea` …). Because the depth is computed from the whole universe, not from what is ingested, **a card's shard never moves** as coverage grows.
- The exact file for every card is in `data/card_index.csv` (`shard` + `anchor` columns) and the per-letter table in [Card Index](Card%20Index.md#shards-by-letter).
- Within a shard, entries are sorted letter-by-letter on that key (so "Sol Ring" (`solring`) sorts after "Solphim" (`solphim`)). Each shard opens with a linked table of contents.
- Projected size at full coverage (~34k cards): ≤350 entries (~350 KB) per shard — comfortably renderable on GitHub.

## Entry format
```markdown
### Card Name

- **Mana cost:** {1}{U} · **MV:** 2 · **Color identity:** U (Blue)
- **Type:** Instant
- **Oracle text:**
  > Counter target spell.
- **Flavor text** (SET printing):
  > *Flavor text, italicised.*
- **Keywords:** …                       (only if Scryfall lists keywords)
- **Commander notes:** Commander format: **legal** · EDHREC rank: #16 · Game Changer: no · Can be commander: No · Pairing: Partner · Reserved List
- **Rulings** (2):
  - *2023-09-01* — Ruling text verbatim.
  - *2024-01-12* *(Scryfall note)* — Ruling authored by Scryfall rather than Wizards.
- **Lore:** Depicts: [Character → …](…) ([source](…)) — Featured in: [Plane → …](…) — ✅ Story Spotlight printing … · [format](…)   (enriched cards only)
- **Synergy:** *Proven* — KB decks (n): … · Commander Spellbook: n combos … · EDHREC … — *Guidance (Oracle pattern)* — packages: … · [format](…)
- **Referenced in:** n pages (…) → [reverse index](…)   (cards cited by any page)
- **Source flags:** [Scryfall](…) · oracle_id `…` · printing: SET #123 (date) · [rulings](…) · source: Scryfall oracle_cards bulk YYYY-MM-DD · status: ✅ verified (Scryfall Oracle)
```
Multi-face cards (split, adventure, transform, MDFC, flip, meld, etc.) show `Layout`, total MV and color identity once, then one `Face N: Name — cost — type line` block per face with that face's Oracle text, P/T/loyalty, and flavor text.

## Field definitions
| Field | Meaning |
|---|---|
| Mana cost | Printed cost in Scryfall symbol notation (`{2}{W}{U}`, `{X}`, hybrid `{W/U}`, Phyrexian `{G/P}`). `—` = no mana cost (lands, some suspend cards). |
| MV | Mana value (Scryfall `cmc`). |
| Color identity | Scryfall `color_identity` (WUBRG letters + names). This is the field used for strict Commander deck legality — see [EDH Standards](EDH%20Standards.md#color-identity-strict). |
| Type | Full type line incl. supertypes/subtypes. |
| P/T · Loyalty · Defense | Shown when present. |
| Oracle text | Current Oracle wording, verbatim. `<` escaped for Markdown. |
| Flavor text | Verbatim flavor text **of the printing Scryfall selects for that Oracle ID** (flavor text is printing-specific and can differ between printings; the printing is named). Absent if that printing has none. |
| Commander notes | Factual, data-derived only: Commander legality, EDHREC rank (popularity rank from Scryfall's `edhrec_rank`; lower = more played), Game Changer flag (Commander Brackets list, via Scryfall `game_changer`), commander eligibility, pairing mechanics (Partner, Partner with, Friends forever, Choose a Background, Doctor's companion, Companion), Reserved List. **No opinions.** |
| Can be commander | *Derived* from [Comprehensive Rules 903.3](https://magic.wizards.com/en/rules) (2026-09-25 edition): "Yes" if the front face is a legendary creature, legendary Vehicle, or legendary Spacecraft with a P/T box, or the Oracle text says "can be your commander" (903.3a); Backgrounds flagged separately. Check Commander banned-as-commander status (see [EDH Standards](EDH%20Standards.md#banned-list--legality)) for edge cases. |

## Rulings
- Source: Scryfall `rulings` bulk (one object per ruling: `oracle_id`, `source` = `wotc` or `scryfall`, `published_at`, `comment`). Rulings apply to the Oracle card, so every printing shares them.
- Rendered after **Commander notes**, sorted by date then text: `  - *YYYY-MM-DD* — comment`. Rulings whose source is Scryfall (not Wizards) are marked *(Scryfall note)*. `<` is escaped; line breaks inside a comment become spaces.
- `- **Rulings:** none published on Scryfall` means the card was processed and has no rulings. A card with **no Rulings line** has not been processed yet (only possible mid-batch); its Source flags then keep a link to the Scryfall rulings API.
- Resumable: the `rulings` column of `data/card_index.csv` is empty (pending) or the number of rulings rendered; `data/ingest_state.json` → `rulings` holds totals, `next_batch_size`, `next_target`, and history. Order = the card ingestion order (priority list, Commander-banned, EDHREC rank, …). `--rulings-batch N` processes the next N cards; every run re-renders processed cards from the newest rulings bulk, so new rulings appear automatically.
- `scripts/verify_cards.py` checks every processed card: ruling count (CSV = file = bulk) and each ruling's date + text verbatim.
- Coverage on 2026-10-15: **78,943 rulings on 19,889 cards; all 33,894 cards processed** (14,005 cards have no rulings on Scryfall). Largest shard with rulings ≈ 500 KB.

## Source flags & verification status
| Flag | Meaning |
|---|---|
| `status: ✅ verified (Scryfall Oracle)` | Generated from Scryfall bulk data on the date shown. All script output carries this flag. |
| `status: ⚠️ manual — unverified` | Reserved for any hand-added entry not regenerated from Scryfall (none exist; avoid). |
| `status: ❓ open question` | Data disputed/unclear (e.g. card previewed but not yet on Scryfall). |

## What counts as a "card" (universe)
Scryfall Oracle cards that exist in paper — a paper printing, or legal/banned/restricted in Vintage, Legacy, or Commander (Scryfall's chosen printing is sometimes an MTGO-only reprint, e.g. Strip Mine → VMA). Excluded: Arena/Alchemy-only digital cards and token, emblem, art-series, Jumpstart front/theme cards (`front_card`), Planechase plane/phenomenon, Archenemy scheme, Vanguard and reversible-card layouts. On 2026-10-15 this universe was **33,894** Oracle cards — consistent with the project's working total of ~33,000 unique cards. **As of 2026-10-15 every one of them has an entry.**

### Duplicate names
A few distinct Oracle cards share a name (Unstable/Unfinity variants such as *Everythingamajig*, Un-set vs. Universes Beyond namesakes such as *Bounty Hunter*). Their headings are disambiguated as `Name (SET #collector)`; the CSV `name` column uses the same heading. Names that collapse to the same anchor (*Clear the Mind* / *Clear, the Mind*) get GitHub's `-1` suffix.

### Verification
`python3 scripts/verify_cards.py` re-checks **every** entry against the bulk file: index ↔ shard agreement (no missing/duplicate entries) and verbatim Oracle text, type line, mana cost, color identity, and flavor text. It must report `0 problems` before a card commit is pushed.

## Ingestion order
1. `data/priority_cards.txt` (the original Grok project's categories: utility lands, land destruction, counterspells, plus ramp/removal/tutors/draw/protection).
2. Cards **banned in Commander** (small list; needed for legality answers).
3. Commander-legal cards by ascending EDHREC rank.
4. Commander-legal cards without an EDHREC rank (alphabetical).
5. Everything else (not legal in Commander), alphabetical.

## Editing rules
- Do not hand-edit generated shard files or `Card Index.md`; change `scripts/` or `data/` inputs and re-run.
- Opinions, synergy notes, and deck advice belong in [EDH Standards](EDH%20Standards.md) or [`decks/`](decks/), clearly labeled as opinion, linking to card entries.
- Rules interactions (planned, see issues) will live in a separate `rules/` area linking to card entries, citing the Comprehensive Rules.
