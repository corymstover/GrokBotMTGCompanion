"""Source-bound physical-list and Scryfall checks for Obeka M7 Rev1.

Live mode requests public Oracle records. Offline mode validates the saved
Oracle snapshot; it does not claim a fresh network check.
"""

import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
from urllib.request import Request, urlopen
from urllib.error import HTTPError


ROOT = Path(__file__).resolve().parents[4]
CANDIDATE = ROOT / "data/grixis/m7/candidate_lists/Obeka__Brute_Chronologist_chatgpt_rev1.txt"
SNAPSHOT = ROOT / "data/grixis/m7/oracle_snapshots/Obeka__Brute_Chronologist_Rev1_Scryfall_20261027.json"
BASELINE_SHA = "31b6ff7f23effa78512c2a409a21440bccf457e6faece51d8db38b74102169a8"
SWAPS = [
    ("Footsteps of the Goryo", "Delina, Wild Mage"),
    ("Entomb", "Windfall"),
    ("Mimic Vat", "Purphoros, Bronze-Blooded"),
    ("Zealous Conscripts", "Ilharg, the Raze-Boar"),
    ("Splinter Twin", "Hate Mirage"),
    ("Spellseeker", "Avaricious Dragon"),
]


def read_deck(path):
    raw = path.read_bytes()
    assert raw.endswith(b"\n") and b"\r" not in raw, "exact LF-terminated UTF-8 required"
    rows = raw.decode("utf-8").splitlines()
    assert len(rows) == 100, f"{path}: {len(rows)} rows"
    assert rows[0] == "1x Obeka, Brute Chronologist [Commander]"
    assert all(re.fullmatch(r"1x .+", row) for row in rows)
    names = [row[3:].replace(" [Commander]", "") for row in rows]
    assert len(set(n.casefold() for n in names)) == 100, "singleton failure"
    return names, hashlib.sha256(raw).hexdigest()


def verify_baseline(baseline, names):
    old, digest = read_deck(baseline)
    assert digest == BASELINE_SHA, (digest, BASELINE_SHA)
    added = set(names) - set(old)
    removed = set(old) - set(names)
    assert added == {a for a, _ in SWAPS}, added
    assert removed == {b for _, b in SWAPS}, removed
    assert len(names) == len(old) == 100


def pull_live_oracle(names, digest):
    cards = []
    for start in range(0, len(names), 50):
        batch = names[start : start + 50]
        request = Request(
            "https://api.scryfall.com/cards/collection",
            data=json.dumps({"identifiers": [{"name": n.split(' // ')[0]} for n in batch]}).encode("utf-8"),
            headers={"Content-Type": "application/json", "Accept": "application/json", "User-Agent": "Grixis-Encyclopedia-Obeka-M7/1.0"},
            method="POST",
        )
        try:
            with urlopen(request, timeout=25) as response:
                result = json.load(response)
        except HTTPError as exc:
            raise RuntimeError(f"Scryfall batch starting {start}: {exc.read().decode('utf-8')}") from exc
        assert not result.get("not_found"), result.get("not_found")
        lookup = {card["name"].split(" // ")[0].casefold(): card for card in result["data"]}
        for name in batch:
            card = lookup.get(name.split(" // ")[0].casefold())
            if card is None:
                raise AssertionError(f"Scryfall did not resolve exact name: {name}")
            cards.append(
                {
                    "query": name,
                    "name": card["name"],
                    "oracle_id": card["oracle_id"],
                    "type_line": card["type_line"],
                    "mana_cost": card.get("mana_cost"),
                    "oracle_text": card.get("oracle_text"),
                    "card_faces": [
                        {"name": f["name"], "type_line": f.get("type_line"), "oracle_text": f.get("oracle_text")}
                        for f in card.get("card_faces", [])
                    ],
                    "color_identity": card["color_identity"],
                    "commander_legality": card["legalities"]["commander"],
                }
            )
    return {
        "source": "https://api.scryfall.com/cards/collection",
        "retrieved_utc": datetime.now(timezone.utc).isoformat(),
        "candidate_sha256": digest,
        "source_count": len(cards),
        "cards": cards,
    }


def verify_snapshot(snapshot, names, digest):
    assert snapshot["candidate_sha256"] == digest, "snapshot belongs to a different physical candidate"
    cards = snapshot["cards"]
    assert len(cards) == 100
    assert [c["query"] for c in cards] == names
    invalid = [(c["query"], c["commander_legality"], c["color_identity"]) for c in cards
               if c["commander_legality"] != "legal" or not set(c["color_identity"]) <= {"U", "B", "R"}]
    assert not invalid, invalid
    land_names = [c["query"] for c in cards if "Land" in c["type_line"].split(" // ")[0]]
    assert len(land_names) == 34, (len(land_names), land_names)
    print(json.dumps({
        "status": "PASS",
        "candidate_raw_sha256": digest,
        "physical_cards": len(cards),
        "singleton_names": len(set(names)),
        "lands": len(land_names),
        "swaps": len(SWAPS),
        "official_commander_legal": len(cards),
        "grixis_identity": len(cards),
        "scryfall_source": snapshot["source"],
        "scryfall_retrieved_utc": snapshot["retrieved_utc"],
    }, indent=2))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--baseline", type=Path, help="exact canonical 2026-10-15 TXT for six-swap readback")
    ap.add_argument("--live", action="store_true", help="request all 100 live Scryfall records and save pinned snapshot")
    args = ap.parse_args()
    names, digest = read_deck(CANDIDATE)
    if args.baseline:
        verify_baseline(args.baseline, names)
    if args.live:
        snapshot = pull_live_oracle(names, digest)
        SNAPSHOT.write_text(json.dumps(snapshot, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    else:
        snapshot = json.loads(SNAPSHOT.read_text())
    verify_snapshot(snapshot, names, digest)


if __name__ == "__main__":
    main()
