# Phase 5 — Valley's legendary history and Duskmourn's origins

**Preliminary history research only. No deck construction, review, owner approval or release certification.**

Source baseline: three official 2024 Wizards primary articles, all registered
in previous packs under unchanged source IDs:

- [Bloomburrow Planeswalker's Guide, Part 1](https://magic.wizards.com/en/news/feature/planeswalkers-guide-to-bloomburrow-part-1) (`blb_guide1`)
- [Bloomburrow Planeswalker's Guide, Part 2](https://magic.wizards.com/en/news/feature/planeswalkers-guide-to-bloomburrow-part-2) (`blb_guide2`)
- [Duskmourn Planeswalker's Guide](https://magic.wizards.com/en/news/feature/planeswalkers-guide-to-duskmourn) (`dsk_guide`)

`python3 scripts/audit_lore_bloomburrow_duskmourn.py --live` checked all
**25** individual short excerpts against the live official pages. Offline
CI enforces source identity, entity declarations, evidence markers and
conservative grade choice. The new claim IDs are `BLH001`–`BLH013`
and `DH001`–`DH012`.

## Why Bloomburrow's history needs qualification

The Valley history is presented as an in-world account narrated to a visitor
by Ms. Bumbleflower. The text explicitly says the **Order of the Holly Leaf
is legendary to most residents**. Accordingly, the historic claims about
Calamity domination, animalfolk shelter, the Order's pact, War of Cinders,
Wildsear, Lily's Seed Flame, and post-war weaving backlash are graded
`CANON_IMPLIED` and retain their individual limitations. Their existence
as *narrated traditions* is reliably sourced; their every detail has not
been independently verified. The guide's **two generations** of conflict
is a verbatim relative span with no AR conversion. The guide's description
of Valley's five biomes and local mayors/councils is separately confirmed;
neither makes claims about the entire plane's geography or political system.

## What Duskmourn's guide verifies

The plane's original name is forgotten. Physical artifacts **suggest** a
lost technologically and magically developed society, so that claim is
`CANON_IMPLIED`. The guide directly describes multiple older realms,
Marina Vendrell's relationship with Valgavoth, the early House victims,
its expansion around a neighborhood, the deception of Marina's perception,
Valgavoth's interplanar doors, and the recurring Quiescence–molt–Harrowing
cycle. The Below is described as a fixed location, but a rumored exit is
**not** promoted to fact. The historical and spatial details supplement
earlier `DS001`–`DS003`, which already record Valgavoth's binding and the
Ascension; they do not duplicate or replace those claims.

## Reproducibility and release boundary

Generated graph, date extraction, direct-claim plane dossiers, priorities,
claim-card anchors, source inventory, audit and progress tracker should
be rebuilt together. Questions through `scripts/mv_ask.py` remain explicitly
QUALIFIED because these are only partial histories. No shared story-present
or cross-plane AR date is invented. Continue with thin plane histories,
actual cross-plane chronology, unresolved names, niche rules/Q&A, and
foundation release gates. **The three lore pilot decks remain unapproved
and untouched; the finalized 62 Grixis decks remain protected.**
