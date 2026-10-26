"""Produce one immutable, alphabetized Nathan Drake M7 Rev1 owner candidate.

The historical canonical list is read-only. The exact 1:1 delta is explicit;
running this script never approves, locks, or writes the canonical repository.
"""
from __future__ import annotations

from collections import Counter
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASELINE = ROOT / "data/grixis/m7/baseline_sources/Nathan_Drake_Treasure_Hunter_Approved_2026-10-15.txt"
DEST = ROOT / "data/grixis/m7/candidate_lists/Nathan_Drake_Treasure_Hunter_M7_Rev1_Approval_Candidate_2026-10-26.txt"

SWAPS = [
    ("Siphon Insight", "Mana Vault"),
    ("Tinybones, the Pickpocket", "Chrome Mox"),
    ("Robber of the Rich", "Grim Monolith"),
    ("Thief of Sanity", "Captain Lannery Storm"),
    ("Gonti, Night Minister", "Combat Celebrant"),
    ("Stolen Strategy", "Goldspan Dragon"),
    ("Court of Locthwain", "Azula, Cunning Usurper"),
    ("Etali, Primal Storm", "Seize the Day"),
    ("Dream-Thief's Bandana", "Dolmen Gate"),
    ("Notion Thief", "Sakashima of a Thousand Faces"),
    ("Force of Negation", "Force of Will"),
]


def read_entries(path: Path) -> Counter[str]:
    cards = Counter()
    for line in path.read_text(encoding="utf-8").splitlines():
        amount, name = line.split("x ", 1)
        cards[name.removesuffix(" [Commander]")] += int(amount)
    return cards


def make_candidate() -> tuple[bytes, Counter[str], Counter[str]]:
    cards = read_entries(BASELINE)
    before = cards.copy()
    assert sha256(BASELINE.read_bytes()).hexdigest() == "a5d59afc3a78d7ff6454b1d011c82c2f732e11f4d4dd03256df1195a3abe9ba0"
    assert sum(cards.values()) == 100 and cards["Nathan Drake, Treasure Hunter"] == 1
    for cut, add in SWAPS:
        assert cards[cut] == 1 and cards[add] == 0, (cut, add)
        del cards[cut]
        cards[add] = 1
    assert len(SWAPS) == 11 and len({a for _, a in SWAPS}) == len(SWAPS)
    assert sum(cards.values()) == 100
    lines = ["1x Nathan Drake, Treasure Hunter [Commander]"]
    lines += [f"{cards[name]}x {name}" for name in sorted(cards, key=str.casefold) if name != "Nathan Drake, Treasure Hunter"]
    return ("\n".join(lines) + "\n").encode("utf-8"), before, cards


def main() -> None:
    raw, before, cards = make_candidate()
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_bytes(raw)
    print("Candidate file:", DEST)
    print("baseline and final physical:", sum(before.values()), sum(cards.values()))
    print("distinct final names:", len(cards))
    print("swaps:", len(SWAPS))
    print("raw SHA-256:", sha256(raw).hexdigest())


if __name__ == "__main__":
    main()
