"""Materialize two genuinely larger 13-swap whole-deck challengers for M7."""
from collections import Counter
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CAN = ROOT / "data/grixis/m7/candidate_lists/Nathan_Drake_Treasure_Hunter_M7_Rev1_Approval_Candidate_2026-10-26.txt"
PACKAGES = {
    "Nathan_Drake_M7_Rev1_Alt13_FastManaBoard.txt": [
        ("Fellwar Stone", "Mox Diamond"),
        ("Blasphemous Act", "Toxic Deluge"),
    ],
    "Nathan_Drake_M7_Rev1_Alt13_AggressiveHeist.txt": [
        ("Plargg and Nassari", "Port Razer"),
        ("Hostage Taker", "Strionic Resonator"),
    ],
}

base = Counter()
for line in CAN.read_text(encoding="utf-8").splitlines():
    q, name = line.split("x ", 1)
    base[name.removesuffix(" [Commander]")] += int(q)

for filename, pairs in PACKAGES.items():
    cards = base.copy()
    for cut, add in pairs:
        assert cards[cut] == 1 and cards[add] == 0
        del cards[cut]
        cards[add] = 1
    assert sum(cards.values()) == 100 and len(cards) == 97
    raw = ("1x Nathan Drake, Treasure Hunter [Commander]\n" + "\n".join(
        f"{cards[name]}x {name}" for name in sorted(cards, key=str.casefold) if name != "Nathan Drake, Treasure Hunter"
    ) + "\n").encode("utf-8")
    target = ROOT / "data/grixis/m7/research_challengers" / filename
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(raw)
    print(filename, sha256(raw).hexdigest(), "100 physical", "13 changes from October 15")
