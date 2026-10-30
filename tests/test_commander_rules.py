"""Tests for scripts/commander_rules.py (CR 2026-09-25 Commander deck-construction checks)."""
import json
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import commander_rules as cr  # noqa: E402
import mv_ask  # noqa: E402


def allowed(names):
    out = cr.commander(names)
    assert out["confidence"] == "VERIFIED", out
    return out["result"]


def _deck(path):
    lines = [l for l in (ROOT / path).read_text(encoding="utf-8").splitlines() if l.strip()]
    names = [re.match(r"\d+x (.+?)(?: \(| \[|$)", l).group(1).strip() for l in lines]
    cmd = [l for l, n in zip(lines, names) if "[Commander]" in l] or lines[:1]
    return names[lines.index(cmd[0])], [n for l, n in zip(lines, names) if l != cmd[0]]


class CommanderRulesTests(unittest.TestCase):
    def test_excerpt_is_official_and_cited(self):
        d = cr.CR
        assert d["source_url"].startswith("https://media.wizards.com/") and d["effective"] == "2026-09-25"
        assert re.fullmatch(r"[0-9a-f]{64}", d["source_sha256"])
        assert d["rules"]["903.5c"].startswith("A card can be included in a Commander deck only if every color")
        for out in (cr.commander(["Krark, the Thumbless"]), cr.include("Sol Ring", ["Krark, the Thumbless"])):
            assert out["rules"] and all(r["text"] == d["rules"][r["rule"]] for r in out["rules"])

    def test_single_commanders(self):
        assert allowed(["Krark, the Thumbless"])["allowed"]
        assert allowed(["Teferi, Temporal Archmage"])["allowed"]  # 903.3a text
        assert allowed(["Adrestia"])["allowed"]  # legendary Vehicle, 903.3 (2026 rules)
        assert allowed(["Nicol Bolas, the Ravager"])["allowed"]  # front face resolves to the DFC
        r = allowed(["Griselbrand"])
        assert not r["allowed"] and "banned" in r["reason"]
        assert not allowed(["Llanowar Elves"])["allowed"]
        r = allowed(["Raised by Giants"])
        assert not r["allowed"] and "Background" in r["reason"]

    def test_pairs(self):
        r = allowed(["Krark, the Thumbless", "Sakashima of a Thousand Faces"])
        assert r["allowed"] and r["pairing_ability"] == "partner"
        r = allowed(["Pir, Imaginative Rascal", "Toothy, Imaginary Friend"])
        assert r["allowed"] and r["pairing_ability"] == "partner with [name]"
        assert not allowed(["Pir, Imaginative Rascal", "Krark, the Thumbless"])["allowed"]  # 702.124f
        r = allowed(["Wernog, Rider's Chaplain", "Sophina, Spearsage Deserter"])
        assert r["allowed"] and r["pairing_ability"] == "partner\u2014friends forever"
        assert not allowed(["Wernog, Rider's Chaplain", "Krark, the Thumbless"])["allowed"]
        assert allowed(["Wilson, Refined Grizzly", "Raised by Giants"])["allowed"]
        assert not allowed(["Krark, the Thumbless", "Raised by Giants"])["allowed"]
        assert allowed(["Clara Oswald", "The Eleventh Doctor"])["allowed"]
        assert cr.commander(["Krark, the Thumbless", "Sakashima of a Thousand Faces", "Adrestia"])["confidence"] == "NOT_FOUND"

    def test_include_identity_and_basic_types(self):
        k = ["Krark, the Thumbless"]
        assert cr.include("Lightning Bolt", k)["result"]["allowed"]
        r = cr.include("Counterspell", k)["result"]
        assert not r["allowed"] and "U" in r["reasons"][0]
        assert cr.include("Counterspell", k + ["Sakashima of a Thousand Faces"])["result"]["allowed"]  # 702.124c
        r = cr.include("Murmuring Bosk", k)
        assert not r["result"]["allowed"] and "903.5d" in [x["rule"] for x in r["rules"]]
        assert not cr.include("Mana Crypt", k)["result"]["allowed"]

    def test_not_found(self):
        assert cr.commander(["No Such Card Zzz"])["confidence"] == "NOT_FOUND"
        assert cr.main(["commander", "No Such Card Zzz"]) == 3

    def test_lore_drafts_pass_include_checks(self):
        """Colour identity must hold for every draft. A card that is banned per Scryfall is allowed
        only where an owner approval record already names it as an intentional exception (read-only)."""
        approvals = " ".join(p.read_text(encoding="utf-8") for p in (ROOT / "data/lore_decks/approvals").glob("*.md"))
        drafts = sorted((ROOT / "data/lore_decks/drafts").glob("*_decklist.txt"))
        assert len(drafts) >= 2
        for path in (d.relative_to(ROOT) for d in drafts):
            cmd, rest = _deck(path)
            assert cr.commander([cmd])["result"]["allowed"], cmd
            for n in rest:
                r = cr.include(n, [cmd])["result"]
                assert not any("color identity" in x or "basic land" in x for x in r["reasons"]), (path, n, r)
                if not r["allowed"]:
                    assert f"**{n}**" in approvals, (path, n, r["reasons"])

    def test_spec_pilots_have_no_exceptions(self):
        for spec in sorted((ROOT / "data/lore_decks/specs").glob("*.json")):
            stem = json.loads(spec.read_text(encoding="utf-8"))["stem"]
            cmd, rest = _deck(f"data/lore_decks/drafts/{stem}_decklist.txt")
            assert [n for n in rest if not cr.include(n, [cmd])["result"]["allowed"]] == [], stem

    def test_eligibility_matches_shard_notes(self):
        out = cr.audit_eligibility()
        assert out["cards_compared"] == len(mv_ask.card_index()) and out["cards_without_note"] == 0
        assert out["disagree"] == 0, out["disagreements"][:5]

    def test_mv_ask_routes_rules_questions(self):
        a = mv_ask.ask("Can Krark, the Thumbless and Sakashima of a Thousand Faces be commanders together?")
        assert a["route"] == "ask->rules:pair" and a["result"]["allowed"]
        a = mv_ask.ask("Can Griselbrand be my commander?")
        assert a["route"] == "ask->rules:single" and not a["result"]["allowed"]
        a = mv_ask.ask("Can Counterspell go in a Krark, the Thumbless deck?")
        assert a["route"] == "ask->rules:include" and not a["result"]["allowed"]
        a = mv_ask.ask("Who is Ugin's brother?")
        assert a["confidence"] == "VERIFIED" and a["route"] == "ask->lore:twin_sibling_of"


if __name__ == "__main__":
    unittest.main()
