"""Exact-hash Admiral A/B/C/D tested-pool preflight, deliberately NOT M6 I certification."""

from collections import Counter
import hashlib
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
POOL_PATH = ROOT / "data/grixis/m6/ij/tested_pools/Admiral_Beckett_Brass_candidate_D_20261022.json"
CERT_PATH = ROOT / "data/grixis/m6/ij/certificates/admiral-beckett-brass.json"
MANA_PATH = ROOT / "data/grixis/m6/certification_preflight/Admiral_M6_J_candidate_D_mana_20261022.md"
RED_TEAM_PATH = ROOT / "data/grixis/m6/certification_preflight/Admiral_M6_J_candidate_D_red_team_20261022.md"
BASE_PATH = ROOT / "data/grixis/m6/authority_snapshots/Admiral_Beckett_Brass_Canonical_Approved_20261022.txt"
ORACLE_PATH = ROOT / "data/grixis/m7/research_challengers/Admiral_Beckett_Brass_Full_Source_Oracle_20261022.json"
BASE_LH1 = "lh1:38598ad4616bb80278e5e8e24c313afdc8bcd555312bbac3fca33fe84d6e9e86"
D_LH1 = "lh1:1f6ae6fa721c3bd7e8b888c4a216edca7cdb25c587d5ce812282662cb0118d58"


def parse_physical(path: Path) -> tuple[Counter[str], set[str]]:
    quantities: Counter[str] = Counter()
    commanders = set()
    lines = path.read_text(encoding="utf-8").splitlines()
    assert lines[0] == "1x Admiral Beckett Brass [Commander]"
    for line in lines:
        n, raw_name = line.split("x ", 1)
        if raw_name.endswith(" [Commander]"):
            commanders.add(raw_name.removesuffix(" [Commander]"))
        name = raw_name.removesuffix(" [Commander]")
        assert name not in quantities, name
        quantities[name] = int(n)
    assert sum(quantities.values()) == 100
    return quantities, commanders


def logical_digest(cards: Counter[str], commander: set[str], oracle: dict) -> str:
    rows = [f'{"commander" if name in commander else "main"}|{oracle[name]["oracle_id"]}|{quantity}'
            for name, quantity in cards.items()]
    return "lh1:" + hashlib.sha256("".join(r + "\n" for r in sorted(rows)).encode("utf-8")).hexdigest()


class AdmiralIJPreflightTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pool = json.loads(POOL_PATH.read_text(encoding="utf-8"))
        cls.certificate = json.loads(CERT_PATH.read_text(encoding="utf-8"))
        cls.oracle = {c["name"]: c for c in json.loads(ORACLE_PATH.read_text(encoding="utf-8"))["cards"]}
        cls.base, cls.base_commander = parse_physical(BASE_PATH)

    def test_baseline_logical_hash_reproduces_registry_authority(self):
        self.assertEqual(logical_digest(self.base, self.base_commander, self.oracle), BASE_LH1)
        self.assertEqual(self.pool["canonical_locked_logical_hash"], BASE_LH1)
        self.assertEqual(self.pool["canonical_locked_raw_sha256"], hashlib.sha256(BASE_PATH.read_bytes()).hexdigest())

    def test_four_actual_complete_100_card_alternatives_and_real_five_changes(self):
        entries = self.pool["alternative_configurations"]
        self.assertEqual([e["id"] for e in entries], ["A", "B", "C", "D"])
        for e in entries:
            path = ROOT / e["path"]
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), e["raw_sha256"])
            cards, commanders = parse_physical(path)
            self.assertEqual(e["physical_cards"], sum(cards.values()))
            self.assertEqual(commanders, {"Admiral Beckett Brass"})
            self.assertEqual(sum((cards - self.base).values()), 5)
            self.assertEqual(sum((self.base - cards).values()), 5)
            self.assertEqual(set((cards - self.base).elements()), set(e["additions"]))
            self.assertEqual(set((self.base - cards).elements()), set(e["cuts"]))
            self.assertTrue(all(self.oracle[n]["legalities"]["commander"] == "legal" for n in cards))
            self.assertTrue(all(set(self.oracle[n]["color_identity"]) <= {"U", "B", "R"} for n in cards))
            for name, qty in cards.items():
                if name not in {"Island", "Swamp", "Mountain"}:
                    self.assertEqual(qty, 1)

    def test_candidate_D_logical_hash_and_protected_commander_engines(self):
        d = self.pool["alternative_configurations"][3]
        cards, commander = parse_physical(ROOT / d["path"])
        self.assertEqual(logical_digest(cards, commander, self.oracle), D_LH1)
        self.assertEqual(self.pool["preferred_logical_hash"], D_LH1)
        self.assertEqual(self.certificate["list_hash"], D_LH1)
        for keep in ("Merchant Raiders", "The Indomitable", "Open into Wonder"):
            self.assertEqual(cards[keep], 1)
        for e in self.pool["alternative_configurations"][:2]:
            alternative, _ = parse_physical(ROOT / e["path"])
            self.assertEqual(alternative["Merchant Raiders"], 0)
            self.assertEqual(alternative["The Indomitable"], 0)
        c, _ = parse_physical(ROOT / self.pool["alternative_configurations"][2]["path"])
        self.assertEqual(c["Open into Wonder"], 0)

    def test_certificate_pins_exact_pool_bytes_and_refuses_positive_ij_gate(self):
        cert = self.certificate
        self.assertEqual(cert["candidate_pool"]["source_ref"], str(POOL_PATH.relative_to(ROOT)))
        self.assertEqual(cert["candidate_pool"]["source_sha256"],
                         "sha256:" + hashlib.sha256(POOL_PATH.read_bytes()).hexdigest())
        self.assertEqual(cert["candidate_pool"]["tested_pool_size"], 4)
        self.assertEqual(cert["certificate_status"], "incomplete")
        self.assertFalse(cert["reconciliation_complete"])
        self.assertFalse(cert["phase_b"]["all_required_tests_pass"])
        self.assertFalse(cert["local_optimum_for_tested_pool"])
        self.assertTrue(cert["blockers"])
        self.assertFalse(cert["authority"]["can_approve_or_lock"])
        self.assertFalse(cert["authority"]["can_decide"])
        self.assertFalse(self.pool["scope"]["all_four_historically_tested_as_fully_effect_aware_matched_games"])
        self.assertFalse(self.pool["scope"]["tested_pool_zero_improvement_M6_I_certified"])
        self.assertFalse(self.pool["scope"]["current_owner_approval"])

    def test_preliminary_red_team_and_mana_reports_are_exact_D_and_not_fake_J(self):
        for path in (MANA_PATH, RED_TEAM_PATH):
            report = path.read_text(encoding="utf-8")
            self.assertIn("201a1d5fc90e30d6aff9a565603fcf8caef69604dad2c07b4951be2b41cc92ee", report)
            self.assertIn("4ba5c483eb67b5f2647d375450adf9c2b7e79a036d0ba1866e58de8441bf3414", report)
            self.assertIn("not", report.lower())
        mana = MANA_PATH.read_text(encoding="utf-8")
        red = RED_TEAM_PATH.read_text(encoding="utf-8")
        self.assertIn("35 land cards", mana)
        self.assertIn("Cavern of Souls", mana)
        self.assertIn("Forerunner", red)
        self.assertIn("Poisoner", red)
        self.assertIn("RESEARCH_ONLY", red)


if __name__ == "__main__":
    unittest.main()
