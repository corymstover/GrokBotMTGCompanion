# Grixis interaction reviews

> **Phase 2, Bot cycle 46+.** This is an Abaddon-style, card-level rules review for every one of the 62 Grixis decks. It is modelled on the source repo's [Abaddon the Despoiler Interaction Review](../source-archive/grixis-commander-encyclopediaGPT/refinement/rules/Abaddon_the_Despoiler_Interaction_Review_2026-10-13.md) and its [coverage inventory](../source-archive/grixis-commander-encyclopediaGPT/refinement/tests/Abaddon_Interaction_Coverage_Inventory_2026-10-13.csv) and [triage](../source-archive/grixis-commander-encyclopediaGPT/refinement/tests/Abaddon_Interaction_Triage_Updated_2026-10-13.csv) CSVs. It also draws on the 518 interaction attestations in the source's 38 `*_Rules_Attestation.json` files. Those files are archived under [source-archive/](../source-archive/README.md). Each deck page links its review from a **Rules notes** section.

## Contents
- [Status](#status)
- [Method](#method)
- [Template](#template)
- [Data format](#data-format)
- [Validation](#validation)
- [Statuses and flags](#statuses-and-flags)

## Status
<!-- INTERACTIONS-STATUS:START -->
**8/62 decks reviewed · 124 rulings (10 uncertain, 10 list flags).**

| Batch | Status | Decks |
|---|---|---|
| A | in progress (Bot cycle 46) | [abaddon-the-despoiler](abaddon-the-despoiler.md) (28) · [admiral-beckett-brass](admiral-beckett-brass.md) (16) · [admiral-brass-unsinkable](admiral-brass-unsinkable.md) (15) · [anhelo-the-painter](anhelo-the-painter.md) (14) · [ashad-the-lone-cyberman](ashad-the-lone-cyberman.md) (13) · [ashnod-the-uncaring](ashnod-the-uncaring.md) (12) · [belakor-the-dark-master](belakor-the-dark-master.md) (13) · [bjorna-nightfall-alchemist-cecily](bjorna-nightfall-alchemist-cecily.md) (13) · cormela-glamour-thief · crosis-the-purger · cult-of-skaro · davros-dalek-creator |
| B | planned | doctor-doom-king-of-latveria · don-andres-the-renegade · dr-eggman · edea-possessed-sorceress · edward-kenway · evelyn-the-covetous · fire-lord-azula · garza-zol-plague-queen · goro-goro-and-satoru · grixistax-october-2026 |
| C | planned | gwendlyn-di-corci · inalla-archmage-ritualist · jeleva-nephalias-scourge · kefka-court-mage · kess-dissident-mage · loki-the-deceiver · lord-of-tresserhorn · lord-xander-the-collector · lynde-cheerful-tormentor · mai-and-zuko |
| D | planned | mairsil-the-pretender · marchesa-dealer-of-death · marchesa-the-black-rose · mishra-artificer-prodigy · mishra-eminent-one · missy · nathan-drake-treasure-hunter · nekusar-the-mindrazer · nicol-bolas-the-ravager · nicol-bolas |
| E | planned | norman-osborn · obeka-brute-chronologist · obeka-splitter-of-seconds · parnesse-the-subtle-brush · rograkh-son-of-rohgahh-silas-renn · saruman-the-white-hand · sauron-lord-of-the-rings · sauron-the-dark-lord · sedris-the-traitor-king · solkanar-the-swamp-king |
| F | planned | solkanar-the-tainted · tetsuo-imperial-champion · tetsuo-umezawa · the-madcap-jester · the-rani · the-valeyard · thraximundar · tresserhorns-lord-returned · wick-the-whorled-mind · zevlor-elturel-exile |
<!-- INTERACTIONS-STATUS:END -->

## Method
1. **Fix the list.**
   - The review is of the deck's **current final list**: [`exports/grixis-archidekt/<slug>.txt`](../../exports/grixis-archidekt/README.md), the refined list where a batch changed it.
   - Its SHA-256 is recorded. If the list changes, the review goes stale and fails validation until the changed cards are re-reviewed.
2. **Gather facts (authoring dossier).** `python3 scripts/grixis_interactions.py --dossier <slug>` prints:
   - the commander's Oracle text and rulings;
   - every card's current Oracle text;
   - the Commander Spellbook combos that are still complete in the final list;
   - the source's attestation entries for the deck.
3. **Work through these areas, in order:**
   - the commander's own text and its edge cases;
   - every combo and engine line;
   - key card pairs;
   - layers and continuous effects;
   - timing and priority;
   - replacement and prevention effects;
   - trigger ordering;
   - zones, commander tax and the command zone;
   - what the list depends on;
   - legality and project exceptions.
   
   As in the source's audit stopping rule, routine cards with no commander-specific or nontrivial interaction are not given essays. Only interactions that change how the deck is built or played get an entry.
4. **Cite every ruling.**
   - **CR rule numbers** from the current Comprehensive Rules (effective 2026-09-25).
   - **Verbatim Oracle text** (Scryfall oracle bulk).
   - **Verbatim Scryfall rulings** (rulings bulk).
   
   An interaction with no citation is not allowed.
5. **Fold in the source, re-verified.**
   - Source attestations and Abaddon rulings are cited with their archived path and the exact item or quote.
   - Each one is checked against current Oracle text and rules, not copied.
   - Where the source is wrong or stale, the entry says so and is flagged `documentation`. Example: Call Forth the Tempest's mana value.
6. **Mark uncertainty.**
   - Use `uncertain` with a note when the answer depends on table state, an unresolved rules question, or something the cited sources don't settle.
   - Never invent a ruling.
7. **Flag list problems** for later refinement (`flag` status): non-bos, anti-synergies, misunderstood combos, dead cards, dependency risks and documentation errors. **No decklist is changed in phase 2.**

## Template
Each `grixis/interactions/<slug>.md` page is rendered from its JSON and has the same parts:
- a header table: the current list and its hash, the ruling counts, the CR/Oracle/rulings versions, and the source attestations;
- a **Summary**;
- **Flags and open questions**: every `flag` and `uncertain` entry;
- one section per category, with one entry per interaction. Each entry has a status, cards, the question, the ruling, an uncertainty or flag note if any, and its citations (Oracle quotes, Scryfall rulings, CR links, source references);
- **Rules cited**: the verbatim text of every CR rule the page cites.

The deck page's **Rules notes** block lists the entries marked `key` as one-line summaries, plus every flag.

## Data format
`data/grixis_interactions/<slug>.json` (schema 1). It is modelled on the source attestation schema (`deck_sha256`, `rules_checkpoint`, `sources`, `interactions[{name, status, note}]`), with per-ruling citations added:

```json
{
 "schema": 1, "deck_id": "Abaddon_the_Despoiler", "slug": "abaddon-the-despoiler", "commanders": ["Abaddon the Despoiler"],
 "deck_sha256": "<sha256 of exports/grixis-archidekt/<slug>.txt>", "list_source": "exports/grixis-archidekt/<slug>.txt",
 "reviewed": "2026-10-16", "cycle": 46, "batch": "A",
 "cr_version": "2026-09-25", "oracle_bulk": "2026-10-15", "rulings_bulk": "2026-10-15", "sources": ["<url or bulk>", "…"],
 "source_attestations": [{"path": "<path inside the archived source tree>", "note": "…"}],
 "summary": "…", "absent": ["cards named but deliberately not in the list"], "companion": ["Lutri, the Spellchaser"],
 "interactions": [{
   "id": "abaddon-01", "category": "commander|combo|engine|pair|layers|timing|replacement|trigger-order|zone|dependency|legality",
   "title": "…", "cards": ["…"], "question": "optional", "ruling": "…", "short": "optional one-liner for Rules notes",
   "status": "verified|uncertain|flag", "uncertainty": "required if uncertain",
   "flag": {"kind": "non-bo|anti-synergy|misunderstood-combo|dead-card|dependency-risk|documentation|other", "note": "…"},
   "key": true,
   "cr": ["702.85a"], "oracle": [{"card": "…", "quote": "verbatim"}], "rulings": [{"card": "…", "quote": "verbatim"}],
   "source": [{"path": "<archived file>", "item": "<attestation interaction name>"} , {"path": "<archived .md>", "quote": "verbatim"}]
 }]
}
```

Batches are in `data/grixis_interactions/_batches.json`: A–F, alphabetical by slug, about 10–12 decks each, with status `planned`, `in progress` or `done`.

## Validation
`python3 scripts/grixis_interactions.py --check` is the `interactions` step of `validate_all`. It fails if any of these is not true:
- the deck hash matches the current list;
- every named card is in the list (or listed in `absent`/`companion`);
- every CR rule exists in the cached CR and the CR version matches;
- every Oracle quote and ruling quote is verbatim (whitespace and curly quotes normalized);
- every source reference resolves to an archived file and item;
- every done batch has all its reviews;
- the rendered pages, deck-page blocks and this status table are current.

## Statuses and flags
| Status | Meaning |
|---|---|
| ✅ verified | Checked against current Oracle text, rulings and CR. |
| ⚠️ uncertain | The answer depends on table state or something the sources don't settle; the note says what. |
| 🚩 list flag | A rules finding that matters for refinement: `non-bo`, `anti-synergy`, `misunderstood-combo`, `dead-card`, `dependency-risk`, `documentation` (source/companion text wrong), `other`. |
