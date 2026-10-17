# Step C 68.3 — Commander Mana / Tax Recovery Validation Gate

`script/grixis_commander_mana.py` is intentionally built on the existing `grixis_sim` v1.1 engine. Loading a real deck through that engine requires the frozen development Oracle bulk named by `data/grixis/dev_snapshot_lock.json`.

GitHub Actions does **not** carry that private/local `.cache` file, and the snapshot lock correctly refuses to download or substitute a newer Scryfall bulk. CI therefore runs only cache-independent semantic tests for this batch.

## Required local gate before 68.3 is counted complete

On the preserved development machine, with the locked bulk restored and its SHA-256 matching `data/grixis/dev_snapshot_lock.json`:

```bash
export SCRYFALL_OFFLINE=1
python3 scripts/check_dev_snapshot_lock.py
pytest -q tests/test_commander_mana.py
python3 scripts/grixis_commander_mana.py --build
python3 scripts/grixis_commander_mana.py --check
python3 scripts/grixis_commander_mana.py --summary
```

Expected outputs after a valid run:

- 62 deck records under `data/grixis/commander_mana/` plus `summary.json`;
- one isolated record per commander in each deck (partner/pair commanders evaluated separately to remove cast-order confounding);
- `simulator_sha256` equal to the current committed `grixis_sim.py` model hash;
- canonical hashes matching `data/grixis/registry.json`;
- schema validation with zero problems;
- the real Abaddon smoke test no longer skipped.

Do **not** set `SCRYFALL_BIRTHDAY_SNAPSHOT=1` to make this gate run. Do not download a replacement bulk. A missing or mismatched locked bulk is a hard stop until the original frozen development file is restored.

68.3 remains **code-ready / pending local frozen-cache validation** until this gate passes. No deck or mana-base decision is implied by code readiness.
