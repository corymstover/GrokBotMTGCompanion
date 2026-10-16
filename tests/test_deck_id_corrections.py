"""Bot cycle 55: registry deck-id corrections (Norman Osborn's stale source tracker id)."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import grixis_authority as ga  # noqa: E402

REG = json.loads((ROOT / "data" / "grixis" / "registry.json").read_text(encoding="utf-8"))
SUMM = json.loads((ROOT / "data" / "grixis_summary.json").read_text(encoding="utf-8"))


def test_norman_uses_corrected_id_with_provenance():
    assert "Goben__Gene_Splice_Savant" not in REG["decks"]
    d = REG["decks"]["Norman_Osborn_Green_Goblin"]
    assert d["deck_id"] == "Norman_Osborn_Green_Goblin" and d["slug"] == "norman-osborn"
    pv = d["deck_id_provenance"]
    assert pv["source_deck_id"] == "Goben__Gene_Splice_Savant" and pv["corrected_cycle"] == 55
    assert pv["evidence"] and "Goben__Gene_Splice_Savant" in pv["note"]


def test_mapping_round_trips_and_covers_the_summary():
    for src in SUMM:
        rid = ga.registry_id(src)
        assert ga.source_deck_id(rid) == src
        assert rid in REG["decks"], rid
        assert ("deck_id_provenance" in REG["decks"][rid]) == (rid != src)
    assert len(REG["decks"]) == len(SUMM) == 62


def test_source_keyed_history_keeps_the_source_id():
    d = REG["decks"]["Norman_Osborn_Green_Goblin"]
    assert d["historical_approvals"][0]["ref"].endswith("#Goben__Gene_Splice_Savant")


def test_blueprint_source_files_found_under_corrected_id():
    import grixis_blueprints as gb
    files = gb.source_files("Norman_Osborn_Green_Goblin")
    assert any("Norman_Osborn_Green_Goblin_Commander_Blueprint" in f for f in files)
    bp = json.loads((ROOT / "data" / "grixis" / "blueprints" / "norman-osborn.json").read_text(encoding="utf-8"))
    assert bp["deck_id"] == "Norman_Osborn_Green_Goblin"
