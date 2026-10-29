# Lore-deep-research gate — story-first Commander

This workflow exists because **the same Magic card can tell a different story in different printings**. A generic card-name search, a small sample of flavor hits, or a thematic deck template can miss pivotal quotes, art treatments, aliases, and named supporting characters. The earlier Yawgmoth deck required avoidable manual discovery of `Phyrexian Tyranny`, `Phyrexian Broodlings`, *Corrupt* (Urza's Saga), and other cards.

The repository already stores the English paper-printing snapshot under `data/printing_lore/`, with exact edition/collector-number/face/flavor data. `scripts/lore_query.py` now includes a more thorough second-stage research pass. **This pass is a discovery and omission detector, not a canon oracle and not a deck generator.**

## Before drafting the 100

1. Establish the subject's chronology from primary Magic story sources, official character profiles and (where accessible) published novels. Record the exact events and the known uncertainty. Do not claim to have read an inaccessible novel. Do not copy copyrighted novel text into this repository without authorization.
2. Make or review `profiles/<subject-slug>.json` with named associates, alternate spellings (e.g. **K'rrik / Kerrick**), separate story phases, printed cards and source links. The `yawgmoth.json` profile is an initial, reviewable example. Mark assumptions and loosely thematic associations plainly.
3. Run `python3 scripts/lore_query.py deep "Yawgmoth" --limit 100`. This scans **every** English paper printing in the stored archive; `--limit` only bounds the returned candidate rows, not the search. It also uses matching character/dossier entries and their card links from `data/lore_entries.json` as a separately labeled **editorial** evidence tier, exposing linked arcs/planes without pretending they are confirmed depictions. It ranks exact **printed** subject mentions above associated-character mentions, manual exact-printing links, indexed editorial links, and broad setting keywords. The matching term, evidence type, source and actual printing are exposed for inspection.
4. For high-value cards run `python3 scripts/lore_query.py variants "Corrupt" --limit 30` (or `Toxic Deluge`, `Dark Ritual`, etc.). Record the **exact edition + collector number** to use. A quote appearing on one printing is *not* automatically present on another. A portrait/art depiction requires separate visual verification; printed flavor text alone cannot establish what the art depicts.
5. Evaluate cards in story sequence: **direct scene or utterance > named associate with a clear causal connection > relevant event or setting > abstract thematic metaphor > generic power/filler**. For scenes linked by a novel, keep the bibliographic attribution and the precise level of access. Disambiguate *Old Phyrexia* from *New Phyrexia* and successor factions.
6. Construct a draft with its chosen prints. Run `python3 scripts/lore_query.py gaps "Yawgmoth" --decklist /path/to/decklist.txt --limit 100`. Review the highest-quality omissions and each phase's coverage. For every omission with a better story claim than a deck inclusion, make the swap **before** the owner sees the list. Record the reason for declining otherwise relevant cards. Do not imply the story exhaustively fits 99 cards.
7. Confirm 100 slots, identity, duplicates and any deliberate Rule 0/casual or banned-card exceptions separately. If the user's format explicitly values narrative over legality, document rather than silently correct those exceptions.

For the `deep` and `gaps` actions, parody expansion sets are excluded by default so a joke quote is not treated as continuity evidence. Use `--include-parody` to research them explicitly. All candidates are *proposals requiring human review*, and current archive coverage is English paper printings from one dated snapshot—not every card treatment ever produced.

## Commands

```bash
python3 scripts/lore_query.py --human deep Yawgmoth --limit 40
python3 scripts/lore_query.py --human variants "Corrupt" --limit 30
python3 scripts/lore_query.py --human gaps Yawgmoth --decklist /path/to/list.txt --limit 40
python3 -m unittest discover -s scripts -p 'test_lore_deep_research.py' -v
```

Use the default JSON output for automated comparison and `--human` (placed **before** the subcommand) for a readable digest. Existing `set`, `card`, `flavor`, `lore`, `candidates`, `beats` and `timeline` queries remain available.

## Evidence standards and expansion

The `signals` array in a profile is **not proof of affiliation**. Each signal needs a term, `relation` (`subject`, `associated_character`, `theme`), chronological phase, and ideally the reason/source. A `pinned_printings` entry requires exact card name, `set`, `collector`, phase and reason; each must be checked against the snapshot. Literal flavor matches are reproducible; editorial associations must remain reviewable. Exact quotations are tied to printings, not abstract Oracle card identity.

Each `reading_sources` entry records the work, access level, scope, and link if available. For *The Thran* by J. Robert King (1999), this repository currently records official contextual sources and bibliographic context, **not a verified full-text ingestion**. A future licensed copy could support scene-level annotations, but no book-derived quotes or page claims should be invented in the meantime.

To research another central character, create `profiles/<lowercase-hyphenated-name>.json` using this schema, adding verified aliases and associate names before the first `deep` scan. Without a profile the tool uses only an exact subject-name signal and labels the result `profile_used: false`; the weaker recall is visible, not concealed. Maintain approval hashes and locked decklists separately; never modify already-approved decks as a side effect of research.
