# Full review-only audit of tentative lore references — October 31, 2026

The Companion previously flagged **341** character-card `name-match` relations for caution. After restoring the complete official Wizards story cache and the exact October 30 Scryfall Default Cards archive, `scripts/audit_unresolved_lore_links.py` independently rechecked every relation against official text, a card's paper printings, printed flavor, artist-matched official story-art captions and Story Spotlight flags. The script is **read-only**: it changes neither `data/card_enrichment.json` nor claim grades, approval locks, card shards or decks.

| Result | Count | Decision |
| --- | ---: | --- |
| Name-only links without direct evidence | 339 | Stay **UNRESOLVED_NAME_ONLY** |
| Official-page co-occurrence leads | 2 | Stay **EVIDENCE_LEAD_REVIEW_ONLY** (not proof of specific depiction) |
| New printing/flavor/Story Spotlight confirmations | 0 | No canon promotions |
| Total tentative links | **341** across **209 Oracle identities** | **341 remain tentative** |

The two existing official-text review leads concern **Wrenn and Six** (*Tangles*) and **Koth of the Hammer** (Wizards' Koth planeswalker profile); both still require context-specific human evidence assessment before any direct depiction or card-to-character claim is promoted. A card's name on an official page and the character's appearance there do **not** by themselves establish that the particular printing depicts that event.

The separate story-image-label provenance contains **570 exactly matched official labels**, six `NAME_MISMATCH` labels pointing at a different Scryfall card under the same set/collector code, and one `NO_PRINTING` label. All seven remain unresolved with source URL, caption name, Scryfall printing candidate (if any), and explicit reason. An image label or card name is not a substitute for a visually reviewed scene.

The JSON report at `data/lore_research/unresolved_printing_name_match_audit_2026-10-31.json` preserves all 341 card/entry/Oracle IDs, status, source lead and reason, plus all seven art exceptions. It binds the output to the exact original input hashes, the 660-page source recovery and the new Default Cards archive (SHA-256 `7c62468c9c34607ae5fe232b24235f62a30eb798a3508968d2f5888e65f6a5a7`). No copyrighted source-body text is committed.

Reproduce using an independently downloaded copy of the exact archive named in the release manifest:

```bash
python3 scripts/story_cache_audit.py --strict
python3 scripts/audit_unresolved_lore_links.py --bulk /path/to/default-cards-20261030210604.jsonl.gz
python3 scripts/audit_unresolved_lore_links.py --check --bulk /path/to/default-cards-20261030210604.jsonl.gz
python3 -m unittest discover -s tests -p 'test_unresolved_lore_links.py' -v
```

CI runs the portable `--check` against source hashes and the committed candidate inventory without needing the large copyrighted source files. A machine with the original cache and bulk can replay the independent printing/text checks in full. This completes the **conservative unresolved-reference tracking procedure**, not comprehensive character histories, proof of all physical depictions, or a release gate accepting disputed lore. Phase 6 remains deferred.
