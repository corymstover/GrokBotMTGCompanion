"""Collect an exact-list dated Scryfall source snapshot for Obeka Splitter Rev1.

This is an explicit network command; the resulting JSON is inspected and
committed as evidence. No approved source list is modified.
"""

from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError


ROOT = Path(__file__).resolve().parents[4]
CANDIDATE = ROOT / "data/grixis/m7/candidate_lists/Obeka__Splitter_of_Seconds_chatgpt_rev1.txt"
DEST = ROOT / "data/grixis/m7/oracle_snapshots/Obeka__Splitter_of_Seconds_Rev1_Scryfall_20261028.json"
EXPECTED = "f80d882944d5e39f3c6661da4dcdce3ec6eead577cd981dc54f7dc522be50859"


def main():
    raw = CANDIDATE.read_bytes()
    assert sha256(raw).hexdigest() == EXPECTED
    weighted = Counter()
    for line in raw.decode("utf-8").splitlines():
        quantity, name = line.split("x ", 1)
        weighted[name.removesuffix(" [Commander]")] += int(quantity)
    assert sum(weighted.values()) == 100 and len(weighted) == 96
    cards = []
    for start in range(0, len(weighted), 50):
        names = list(weighted)[start:start + 50]
        data = json.dumps({"identifiers": [{"name": name} for name in names]}).encode()
        req = Request("https://api.scryfall.com/cards/collection", data=data,
                      headers={"Content-Type": "application/json", "Accept": "application/json", "User-Agent": "Cory-Grixis-M7-Audit/1.0"})
        try:
            with urlopen(req, timeout=40) as response:
                result = json.load(response)
        except HTTPError as exc:
            raise RuntimeError(f"Scryfall collection batch error: {exc.read().decode()[:1000]}") from exc
        assert not result.get("not_found"), result.get("not_found")
        assert len(result["data"]) == len(names), (len(result["data"]), len(names))
        for card in result["data"]:
            cards.append({
                "query": card["name"], "oracle_id": card["oracle_id"],
                "type_line": card["type_line"], "oracle_text": card.get("oracle_text", ""),
                "mana_cost": card.get("mana_cost", ""),
                "color_identity": card["color_identity"],
                "commander_legality": card["legalities"]["commander"],
                "scryfall_uri": card["scryfall_uri"],
            })
    assert {c["query"] for c in cards} == set(weighted)
    assert all(set(c["color_identity"]) <= set("UBR") for c in cards)
    assert all(c["commander_legality"] == "legal" for c in cards)
    doc = {"schema": "OBEKA_SPLITTER_M7_REV1_SCRYFALL_100",
           "retrieved_utc": datetime.now(timezone.utc).isoformat(),
           "candidate_raw_sha256": EXPECTED, "physical_cards": 100,
           "unique_oracle_names": len(cards), "source": "Scryfall API cards/collection",
           "cards": sorted(cards, key=lambda c: c["query"])}
    DEST.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"PASS Scryfall collection: {len(cards)} names, all legal and UBR; {DEST}")


if __name__ == "__main__":
    main()
