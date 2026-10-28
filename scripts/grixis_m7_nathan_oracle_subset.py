"""Bind current Scryfall card records to exactly Nathan M7 Rev1's 100-card list."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIST = ROOT / "data/grixis/m7/candidate_lists/Nathan_Drake_Treasure_Hunter_M7_Rev1_Approval_Candidate_2026-10-26.txt"
RESEARCH = ROOT / "data/grixis/m7/oracle_snapshots/Nathan_Drake_M7_Research_Scryfall_20261026.json"
SELECTED = ROOT / "data/grixis/m7/oracle_snapshots/Nathan_Drake_M7_Rev1_Selected_Scryfall_20261026.json"

raw = LIST.read_bytes()
names = {line.split("x ", 1)[1].removesuffix(" [Commander]") for line in raw.decode().splitlines()}
source = json.loads(RESEARCH.read_text(encoding="utf-8"))
cards = [c for c in source["cards"] if c["name"] in names]
assert len(cards) == len(names) == 97
assert all(c["commander_legality"] == "legal" for c in cards)
assert all(set(c["color_identity"]) <= {"U", "B", "R"} for c in cards)
out = {
    "source": source["source"],
    "retrieved_utc": source["retrieved_utc"],
    "candidate_sha256": hashlib.sha256(raw).hexdigest(),
    "distinct_selected_names": len(names),
    "cards": sorted(cards, key=lambda c: c["name"]),
}
SELECTED.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print("Scryfall selected:", len(cards), "exact candidate:", out["candidate_sha256"])
