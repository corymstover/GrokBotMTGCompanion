"""Reproducibly stage complete, rejected 100-card Obeka challenge portfolios."""

from collections import Counter
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
CANDIDATE = ROOT / "data/grixis/m7/candidate_lists/Obeka__Brute_Chronologist_chatgpt_rev1.txt"
EXPECTED = "43f1249c9a1da82bc1e74254a44613a0ab5763c91295a56ffae3b75a889029f2"
OUT = ROOT / "data/grixis/m7/candidate_lists"
PACKAGES = {
    "Obeka__Brute_Chronologist_7swap_muddle_alternative.txt": [
        ("Muddle the Mixture", "Counterspell"),
    ],
    "Obeka__Brute_Chronologist_8swap_graveyard_alternative.txt": [
        ("Muddle the Mixture", "Counterspell"),
        ("Corpse Dance", "Rionya, Fire Dancer"),
    ],
}


def main():
    raw = CANDIDATE.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == EXPECTED, "primary candidate changed"
    cards = [row[3:].replace(" [Commander]", "") for row in raw.decode().splitlines()]
    assert len(cards) == len(set(cards)) == 100
    for filename, changes in PACKAGES.items():
        alt = set(cards)
        for add, cut in changes:
            assert cut in alt and add not in alt, (filename, add, cut)
            alt.remove(cut)
            alt.add(add)
        commander = "Obeka, Brute Chronologist"
        assert commander in alt and len(alt) == 100 and len(Counter(alt)) == 100
        out = "1x " + commander + " [Commander]\n"
        out += "".join("1x " + x + "\n" for x in sorted(alt - {commander}, key=str.casefold))
        path = OUT / filename
        path.write_text(out, encoding="utf-8", newline="\n")
        print(f"{filename}: 100 distinct, SHA256 {hashlib.sha256(out.encode()).hexdigest()}")


if __name__ == "__main__":
    main()
