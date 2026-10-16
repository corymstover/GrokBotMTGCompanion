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
**49/62 decks reviewed · 516 rulings (9 uncertain, 30 flags).**

| Batch | Status | Decks |
|---|---|---|
| A | done (Bot cycle 46) | [abaddon-the-despoiler](abaddon-the-despoiler.md) (29) · [admiral-beckett-brass](admiral-beckett-brass.md) (17) · [admiral-brass-unsinkable](admiral-brass-unsinkable.md) (15) · [anhelo-the-painter](anhelo-the-painter.md) (14) · [ashad-the-lone-cyberman](ashad-the-lone-cyberman.md) (14) · [ashnod-the-uncaring](ashnod-the-uncaring.md) (12) · [belakor-the-dark-master](belakor-the-dark-master.md) (13) · [bjorna-nightfall-alchemist-cecily](bjorna-nightfall-alchemist-cecily.md) (15) · [cormela-glamour-thief](cormela-glamour-thief.md) (10) · [crosis-the-purger](crosis-the-purger.md) (11) · [cult-of-skaro](cult-of-skaro.md) (10) · [davros-dalek-creator](davros-dalek-creator.md) (9) |
| B | done (Bot cycle 48) | [doctor-doom-king-of-latveria](doctor-doom-king-of-latveria.md) (11) · [don-andres-the-renegade](don-andres-the-renegade.md) (12) · [dr-eggman](dr-eggman.md) (10) · [edea-possessed-sorceress](edea-possessed-sorceress.md) (11) · [edward-kenway](edward-kenway.md) (11) · [evelyn-the-covetous](evelyn-the-covetous.md) (10) · [fire-lord-azula](fire-lord-azula.md) (11) · [garza-zol-plague-queen](garza-zol-plague-queen.md) (11) · [goro-goro-and-satoru](goro-goro-and-satoru.md) (9) · [grixistax-october-2026](grixistax-october-2026.md) (11) |
| C | done (Bot cycle 49) | [gwendlyn-di-corci](gwendlyn-di-corci.md) (10) · [inalla-archmage-ritualist](inalla-archmage-ritualist.md) (9) · [jeleva-nephalias-scourge](jeleva-nephalias-scourge.md) (10) · [kefka-court-mage](kefka-court-mage.md) (13) · [kess-dissident-mage](kess-dissident-mage.md) (9) · [loki-the-deceiver](loki-the-deceiver.md) (7) · [lord-of-tresserhorn](lord-of-tresserhorn.md) (13) · [lord-xander-the-collector](lord-xander-the-collector.md) (11) · [lynde-cheerful-tormentor](lynde-cheerful-tormentor.md) (8) · [mai-and-zuko](mai-and-zuko.md) (9) |
| D | done (Bot cycle 51) | [mairsil-the-pretender](mairsil-the-pretender.md) (11) · [marchesa-dealer-of-death](marchesa-dealer-of-death.md) (8) · [marchesa-the-black-rose](marchesa-the-black-rose.md) (11) · [mishra-artificer-prodigy](mishra-artificer-prodigy.md) (10) · [mishra-eminent-one](mishra-eminent-one.md) (9) · [missy](missy.md) (9) · [nathan-drake-treasure-hunter](nathan-drake-treasure-hunter.md) (8) · [nekusar-the-mindrazer](nekusar-the-mindrazer.md) (9) · [nicol-bolas-the-ravager](nicol-bolas-the-ravager.md) (8) · [nicol-bolas](nicol-bolas.md) (9) |
| E | in progress (Bot cycle 54) | [norman-osborn](norman-osborn.md) (9) · [obeka-brute-chronologist](obeka-brute-chronologist.md) (5) · [obeka-splitter-of-seconds](obeka-splitter-of-seconds.md) (5) · [parnesse-the-subtle-brush](parnesse-the-subtle-brush.md) (10) · [rograkh-son-of-rohgahh-silas-renn](rograkh-son-of-rohgahh-silas-renn.md) (8) · [saruman-the-white-hand](saruman-the-white-hand.md) (7) · [sauron-lord-of-the-rings](sauron-lord-of-the-rings.md) (5) · sauron-the-dark-lord · sedris-the-traitor-king · solkanar-the-swamp-king |
| F | planned | solkanar-the-tainted · tetsuo-imperial-champion · tetsuo-umezawa · the-madcap-jester · the-rani · the-valeyard · thraximundar · tresserhorns-lord-returned · wick-the-whorled-mind · zevlor-elturel-exile |
<!-- INTERACTIONS-STATUS:END -->

## Method
1. **Fix the list.**
   - The review is of the deck's **canonical project list**: the `canonical_project_list.export` in the M0 registry (`data/grixis/registry.json`, read-only here) (Bot cycle 49). That's [`exports/grixis-archidekt/<slug>.txt`](../../exports/grixis-archidekt/README.md) for most decks, and `exports/grixis-archidekt/source-baseline/<slug>.txt` for the 7 decks whose GrokBot refinement is only an unapproved challenger. A `[Companion]` line is recorded in `companion`.
   - Its SHA-256 is recorded. If the list changes, the review goes stale and fails validation until the changed cards are re-reviewed.
2. **Gather facts (authoring dossier).** `python3 scripts/grixis_interactions.py --dossier <slug>` prints:
   - the commander's Oracle text and rulings;
   - every card's current Oracle text;
   - the Commander Spellbook combos that are still complete in the final list, with their cached prerequisites and steps (Bot cycle 48);
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
   - **Verbatim Commander Spellbook steps or prerequisites** for combo lines (Bot cycle 48). They come from the cached `data/grixis_spellbook_steps.json`, built by `scripts/spellbook_steps.py` from the public API with a retrieval date. Spellbook is community-maintained, so it confirms a combo line's steps but is not an official rules source. Each line's rules points still cite CR, Oracle and rulings.
   
   An interaction with no citation is not allowed.
5. **Fold in the source, re-verified.**
   - Source attestations and Abaddon rulings are cited with their archived path and the exact item or quote.
   - Each one is checked against current Oracle text and rules, not copied.
   - Where the source is wrong or stale, the entry says so and is flagged `documentation`. Example: Call Forth the Tempest's mana value.
6. **Mark uncertainty.**
   - Use `uncertain` with a note when the answer depends on table state, an unresolved rules question, or something the cited sources don't settle.
   - A combo line rebuilt from a source attestation that no cached Spellbook variant confirms stays `uncertain`, with `evidence_class: hypothesis`, until it's Spellbook-confirmed (Bot cycle 48).
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
 "deck_sha256": "<sha256 of the canonical project list>", "list_source": "<registry canonical_project_list.export>",
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
   "spellbook": [{"id": "<Spellbook variant id>", "quote": "verbatim step or prerequisite"}],
   "evidence_class": "required: fact|derived_metric|heuristic|hypothesis|test_result|strategic_judgment|approved_decision",
   "source": [{"path": "<archived file>", "item": "<attestation interaction name>"} , {"path": "<archived .md>", "quote": "verbatim"}]
 }]
}
```

`spellbook` and `evidence_class` were added in Bot cycle 48. `evidence_class` uses the evidence classes of Cory's authority program (milestone M0). Since Bot cycle 49 (M0 on main) every record has one: verified rulings and rules-derived flags `fact`, rebuilt or unconfirmed lines `hypothesis` until Spellbook-confirmed, table-size arithmetic `derived_metric`, strategic calls `strategic_judgment`, and Cory's authorized project exceptions `approved_decision`. A review redone against a changed canonical list carries `rereview` (cycle, date, reason).

Batches are in `data/grixis_interactions/_batches.json`: A–F, alphabetical by slug, about 10–12 decks each, with status `planned`, `in progress` or `done`.

## Validation
`python3 scripts/grixis_interactions.py --check` is the `interactions` step of `validate_all`. It fails if any of these is not true:
- `list_source` is the deck's canonical project list (M0 registry), and the deck hash matches it;
- a `[Companion]` in that list matches the record's `companion`;
- every named card is in the list (or listed in `absent`/`companion`);
- every CR rule exists in the cached CR and the CR version matches;
- every Oracle quote and ruling quote is verbatim (whitespace and curly quotes normalized);
- every source reference resolves to an archived file and item;
- every Spellbook citation names a cached variant, and its quote appears verbatim in that variant's steps or prerequisites (normalized);
- every interaction has an `evidence_class` from the seven classes;
- every done batch has all its reviews;
- the rendered pages, deck-page blocks and this status table are current.

## Statuses and flags
| Status | Meaning |
|---|---|
| ✅ verified | Checked against current Oracle text, rulings and CR. |
| ⚠️ uncertain | The answer depends on table state or something the sources don't settle; the note says what. |
| 🚩 list flag | A rules finding that matters for refinement: `non-bo`, `anti-synergy`, `misunderstood-combo`, `dead-card`, `dependency-risk`, `documentation` (source/companion text wrong), `other`. |
