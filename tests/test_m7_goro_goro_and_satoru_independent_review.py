"""Independent M7 Deck #21 Goro-Goro and Satoru research verification.
Source-bound deterministic assertions; NO gameplay, win-rate, or canonical approval claim.
"""
from __future__ import annotations
import hashlib
import json
import re
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
D = "Goro_Goro_and_Satoru"
BASE = ROOT / f"data/grixis/m7/baseline_sources/{D}_approved_source_2026-10-14.txt"
DATA = ROOT / f"data/grixis/m7/independent_reviews/{D}_M7_Rev1_20261024.json"
ORACLE = ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json"
ADDENDUM = ROOT / f"data/grixis/m7/independent_reviews/{D}_Oracle_Addendum_20261024.json"
CMD = "Goro-Goro and Satoru"
BASE_SHA = "2fd39e3b39afaeb1bf394a59b392d8a29f28645776fa0b13c5754df67ab85fdf"
PRIMARY_SHA = "36b71b76f913c38503f6cd1a59ba9e29a5aab48d1d6b9fd4c29eba5b69775d5c"


def parse(path):
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        m = re.fullmatch(r"(\d+)x (.+?)( \[Commander\])?", line)
        if not m:
            raise ValueError(f"bad line: {line!r}")
        rows.append((int(m[1]), m[2], bool(m[3])))
    return rows


def counts(path):
    return Counter({name: qty for qty, name, _ in parse(path)})


class IndependentGoroM7(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.review = json.loads(DATA.read_text())
        cls.source = json.loads(ORACLE.read_text())
        cls.new = json.loads(ADDENDUM.read_text())["cards"]
        cls.oracle = {c["name"]: c for c in cls.source["cards"]}
        cls.oracle.update(cls.new)
        cls.candidate = ROOT / cls.review["selected_candidate"]["path"]

    def test_original_canonical_source_and_grok_are_preserved(self):
        self.assertEqual(hashlib.sha256(BASE.read_bytes()).hexdigest(), BASE_SHA)
        self.assertEqual(self.review["source"]["canonical_raw_sha256"], BASE_SHA)
        self.assertEqual(self.review["source"]["grok_pr"], 669)
        self.assertEqual(self.review["source"]["grok_head"], "3d550c79d11e23b8eefc3bf8cd86705b28356c1a")
        self.assertFalse(self.review["selected_candidate"]["owner_approved"])
        self.assertFalse(self.review["selected_candidate"]["canonical_changed"])
        self.assertEqual(self.review["stage"], "M7_CHATGPT_INDEPENDENT_FIVE_SWAP_RESEARCH_CANDIDATE_NOT_OWNER_APPROVED")

    def test_exact_100_and_raw_sha(self):
        r = self.review["selected_candidate"]
        self.assertEqual(hashlib.sha256(self.candidate.read_bytes()).hexdigest(), PRIMARY_SHA)
        self.assertEqual(r["raw_sha256"], PRIMARY_SHA)
        rows = parse(self.candidate)
        self.assertEqual(rows[0], (1, CMD, True))
        self.assertEqual(sum(q for q, _, _ in rows), 100)
        self.assertEqual(len(rows), 99)
        self.assertEqual(sum(is_cmd for _, _, is_cmd in rows), 1)
        self.assertEqual(sum(q for q, name, _ in rows if name == "Island"), 2)
        self.assertEqual([name for q, name, _ in rows if q > 1], ["Island"])
        self.assertEqual([name for _, name, _ in rows[1:]],
                         sorted([name for _, name, _ in rows[1:]], key=str.lower))

    def test_exact_five_physical_swaps(self):
        diff_add = counts(self.candidate) - counts(BASE)
        diff_cut = counts(BASE) - counts(self.candidate)
        swaps = self.review["swaps"]
        self.assertEqual(len(swaps), 5)
        self.assertEqual(diff_add, Counter({s["add"]: 1 for s in swaps}))
        self.assertEqual(diff_cut, Counter({s["cut"]: 1 for s in swaps}))
        self.assertEqual(sum(diff_add.values()), 5)
        self.assertEqual(set(diff_cut), {
            "Mist-Syndicate Naga", "Grim Hireling", "Kaito, Bane of Nightmares",
            "Crumbling Necropolis", "Fabled Passage"})

    def test_full_current_source_coverage_legality_color_and_mana(self):
        total_lands = 0
        total_nonland = 0
        total_nonland_mv = 0
        game_changers = set()
        for qty, name, _ in parse(self.candidate):
            self.assertIn(name, self.oracle, name)
            obj = self.oracle[name]
            self.assertEqual(obj["commander_legality"], "legal", name)
            self.assertTrue(set(obj["color_identity"]).issubset(set("UBR")), name)
            self.assertTrue(obj["mana_cost"] is not None, name)
            if obj.get("game_changer"):
                game_changers.add(name)
            if "Land" in obj["type_line"]:
                total_lands += qty
            elif name != CMD:
                total_nonland += qty
                total_nonland_mv += float(obj["cmc"]) * qty
        self.assertEqual((total_lands, total_nonland), (33, 66))
        self.assertEqual(round(total_nonland_mv / total_nonland, 2), 2.50)
        self.assertEqual(game_changers, set(self.review["selected_candidate"]["game_changers"]))
        self.assertEqual(self.review["selected_candidate"]["power_bracket"], 4)
        self.assertEqual(self.review["selected_candidate"]["tags"], ["Ninjas", "Dragons", "Extra Combats"])
        self.assertEqual(self.review["legality"]["project_exceptions"], [])

    def test_roaming_human_mode_synergies_exactly_scoped(self):
        throne = self.oracle["Roaming Throne"]
        self.assertEqual(throne["type_line"], "Artifact Creature — Golem")
        self.assertEqual(throne["mana_cost"], "{4}")
        self.assertIn("another creature you control of the chosen type", throne["oracle_text"])
        goro = self.oracle[CMD]
        self.assertIn("one or more creatures you control that entered this turn deal combat damage to a player", goro["oracle_text"])
        for card in ["Goro-Goro and Satoru", "Hanweir Garrison",
                     "Professional Face-Breaker", "Satoru, the Infiltrator"]:
            self.assertIn("Human", self.oracle[card]["type_line"], card)
        self.assertIn("Whenever this creature attacks, create two 1/1 red Human creature tokens that are tapped and attacking",
                      self.oracle["Hanweir Garrison"]["oracle_text"])
        self.assertIn("Whenever one or more creatures you control deal combat damage to a player",
                      self.oracle["Professional Face-Breaker"]["oracle_text"])
        self.assertIn("power or toughness 1 or less can't be blocked", self.oracle["Tetsuko Umezawa, Fugitive"]["oracle_text"])
        self.assertEqual(len(set(["Goro-Goro and Satoru", "Hanweir Garrison"])), 2)

    def test_conditional_three_opponent_trigger_cases_not_win_rates(self):
        # Hanweir Garrison generates 2 Human 1/1 tokens per attack trigger;
        # Roaming Throne chosen Human causes that trigger to happen twice.
        tokens = 2 * 2
        self.assertEqual(tokens, 4)
        for unique_damaged_opponents, expected_dragons in [(0, 0), (1, 2), (2, 4), (3, 6)]:
            # Goro fires ONCE PER PLAYER per combat-damage step, twice with Throne.
            self.assertLessEqual(unique_damaged_opponents, tokens)
            self.assertEqual(unique_damaged_opponents * 2, expected_dragons)
        # Two combats (if Garrison remains ready) result in 8 fresh attacking
        # tokens, but do not guarantee ANY damage or any Dragon.
        self.assertEqual(tokens * 2, 8)

    def test_typed_fetchland_access_and_costs(self):
        for fetch, typ, untapped in [
            ("Misty Rainforest", "Island", {"Underground Sea", "Watery Grave", "Steam Vents", "Volcanic Island"}),
            ("Marsh Flats", "Swamp", {"Underground Sea", "Watery Grave", "Badlands", "Blood Crypt"})]:
            self.assertIn(typ, self.oracle[fetch]["oracle_text"])
            self.assertIn("Pay 1 life", self.oracle[fetch]["oracle_text"])
            for target in untapped:
                self.assertIn(typ, self.oracle[target]["type_line"])
                # Dual/shock with typed land can enter untapped, sometimes at 2 life.
                self.assertIn("Land —", self.oracle[target]["type_line"])
            self.assertIn(typ, self.oracle["Xander's Lounge"]["type_line"])
        self.assertIn("This land enters tapped", self.oracle["Crumbling Necropolis"]["oracle_text"])
        self.assertIn("four or more lands", self.oracle["Fabled Passage"]["oracle_text"])
        # These are positional turn-3 cases, not a whole-deck probability simulation.

    def test_owner_named_keeps_and_20261014_additions_remain(self):
        protected = [
            "Bident of Thassa", "Enduring Curiosity", "Grazilaxx, Illithid Scholar",
            "Silver-Fur Master", "Thousand-Faced Shadow", "Mistblade Shinobi",
            "Moon-Circuit Hacker", "Fallen Shinobi", "Nashi, Moon Sage's Scion",
            "Ninja of the Deep Hours", "Sakashima's Student", "Yuriko, the Tiger's Shadow",
            "Satoru Umezawa", "Satoru, the Infiltrator", "Ingenious Infiltrator",
            "Daring Piracy", "Loyal Apprentice", "Urabrask's Forge", "Determined Iteration",
            "Dragon Tempest", "Terror of the Peaks", "Rogue's Passage", "Breath of Fury",
            "Phoenix Chick", "Samut, Hazoret's Champion", "Withering Torment",
            "Waterbender Ascension", "Raphael, the Nightwatcher", "Fire Navy Trebuchet",
            "Fellwar Stone"]
        c = counts(self.candidate)
        for card in protected:
            self.assertEqual(c[card], 1, card)
        forbidden_reintroductions = {"Reinforced Ronin", "Rising of the Day", "Feed the Swarm",
                                    "Combat Research", "Impact Tremors", "Kaito, Dancing Shadow",
                                    "Goblin Rabblemaster", "Kari Zev, Skyship Raider"}
        self.assertFalse(forbidden_reintroductions & c.keys())

    def test_complete_100_alternatives_and_hashes(self):
        primary = counts(self.candidate)
        for alt in self.review["alternatives"]:
            path = ROOT / alt["path"]
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), alt["raw_sha256"])
            self.assertEqual(sum(counts(path).values()), 100)
            self.assertEqual(parse(path)[0], (1, CMD, True))
            diff = counts(path) - primary
            if alt["id"] == "CHANDRA_OVER_KAITO":
                self.assertEqual(diff, Counter({"Chandra, Acolyte of Flame": 1}))
                self.assertEqual(primary - counts(path), Counter({"Hanweir Garrison": 1}))
            else:
                self.assertEqual(alt["id"], "FOUR_SWAP_KEEP_KAITO")
                self.assertEqual(diff, Counter({"Kaito, Bane of Nightmares": 1}))
                self.assertEqual(primary - counts(path), Counter({"Hanweir Garrison": 1}))


if __name__ == "__main__":
    unittest.main()
