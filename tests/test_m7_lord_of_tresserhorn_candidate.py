"""Deck 29 Lord_of_Tresserhorn (Lord of Tresserhorn) M7 review candidate: structural checks only, not approval.

The packet is READY_FOR_EXACT_OWNER_APPROVAL_NOT_YET_APPROVED: five genuine swaps (+Fierce Guardianship -Stubborn Denial;
+Consign to Memory -Feed the Swarm; +Black Market Connections -Cover of Darkness; +Ornithopter of Paradise -Fellwar
Stone; +Skullclamp -Sheoldred's Edict). Every cut is flagged (Stubborn Denial is an owner-cycle add; the other four were
owner audit keeps). Lord's actual Oracle text is used: enters -> lose 2 life, sacrifice two creatures, target opponent
draws two; {B}: regenerate Lord. There is no opponent-regeneration clause. Nothing here is owner approval."""
from __future__ import annotations
import ast
import hashlib
import json
import unittest
from collections import Counter
from pathlib import Path

from scripts import grixis_m7_decision_gate as gate

ROOT = Path(__file__).resolve().parents[1]
D = "Lord_of_Tresserhorn"
LORD = "Lord of Tresserhorn"
PACKET = ROOT / f"data/grixis/m7/decision_reviews/{D}.json"
BASE = ROOT / f"data/grixis/m7/baseline_sources/{D}_approved_source_2026-10-14.txt"
RAW = "95863276f38beff6b0cf7609041006a6f1de94d5e62c73d76551d6793ffa5b8e"
CAND_RAW = "fd09cb267660206b834257e5c455259985b0e53316743835f679760b11200f85"
LH = "lh1:eae4578c6338f3c2caf25f7359154e851b6f51f179c2ddb3ac2883f95489aafa"
CAND_LH = "lh1:c01c0d9c2ea75d54c110a6fa0345ce27094eea53a7a7a226b77f711e22984961"
RC = ROOT / "data/grixis/m7/research_challengers"
ADDS = ["Black Market Connections", "Consign to Memory", "Fierce Guardianship", "Ornithopter of Paradise", "Skullclamp"]
CUTS = ["Cover of Darkness", "Feed the Swarm", "Fellwar Stone", "Sheoldred's Edict", "Stubborn Denial"]
ORACLE = ("When Lord of Tresserhorn enters, you lose 2 life, you sacrifice two creatures, and target opponent draws two "
          "cards.\n{B}: Regenerate Lord of Tresserhorn.")


class LordOfTresserhornM7Tests(unittest.TestCase):
    def setUp(self):
        self.packet = json.loads(PACKET.read_text())
        self.registry = json.loads((ROOT / "data/grixis/registry.json").read_text())
        self.judged = {c["card"]: c for c in self.packet["material_candidates"]}

    def cand(self):
        return Counter(gate.parse_list(ROOT / self.packet["final_candidate"]["path"])[0])

    def test_gate_passes_as_ready_not_approval(self):
        result = gate.verify_packet(self.packet, root=ROOT, registry=self.registry)
        self.assertTrue(result["owner_presentable"])
        self.assertEqual(result["new_swaps"], 5)
        self.assertEqual(result["material_candidates"], 15)
        self.assertEqual(result["status"], "M7_STRUCTURALLY_DECISION_READY_NOT_OWNER_APPROVED")
        self.assertTrue(result["canonical_unchanged"])
        self.assertEqual(self.packet["readiness"], "READY_FOR_EXACT_OWNER_APPROVAL_NOT_YET_APPROVED")
        self.assertFalse(self.packet["owner_authority"]["exact_candidate_owner_approved"])
        self.assertFalse(self.packet["owner_authority"]["canonical_deck_changed"])
        self.assertNotIn("baseline_provenance_exception", self.packet)
        self.assertEqual(self.packet["verification"]["known_hard_blockers"], [])

    def test_registry_matches_raw_and_vendored_copy_is_byte_identical(self):
        src = self.registry["decks"][D]["source"]
        self.assertEqual(src["recorded_sha256"], RAW)
        self.assertEqual(src["raw_sha256"], "sha256:" + RAW)
        self.assertIs(src["recorded_matches_raw"], True)
        self.assertEqual(self.packet["canonical_baseline_sha256"], RAW)
        self.assertEqual(hashlib.sha256(BASE.read_bytes()).hexdigest(), RAW)
        cand = ROOT / self.packet["final_candidate"]["path"]
        self.assertEqual(hashlib.sha256(cand.read_bytes()).hexdigest(), CAND_RAW)
        self.assertEqual(self.packet["final_candidate"]["sha256"], CAND_RAW)
        self.assertEqual(self.packet["canonical_baseline_logical_hash"], LH)
        self.assertEqual(self.registry["decks"][D]["current_canonical_hash"], LH)
        self.assertIn(CAND_LH, self.packet["final_candidate"]["deckwide_reconciliation"])
        self.assertEqual(self.registry["decks"][D]["commanders"], [LORD])

    def test_exactly_five_swaps_against_vendored_and_canonical_source(self):
        cand = self.cand()
        path, md = gate.canonical_source(ROOT, self.registry["decks"][D])
        for base in (Counter(gate.parse_list(BASE)[0]), Counter(gate.parse_list(path, source_markdown=md)[0])):
            self.assertEqual(sorted((cand - base).elements()), ADDS)
            self.assertEqual(sorted((base - cand).elements()), CUTS)
        self.assertEqual(sorted(self.packet["final_changes"]["adds"]), ADDS)
        self.assertEqual(sorted(self.packet["final_changes"]["cuts"]), CUTS)

    def test_commander_first_100_physical_with_basics_alphabetical(self):
        lines = [x for x in (ROOT / self.packet["final_candidate"]["path"]).read_text().splitlines() if x.strip()]
        self.assertEqual(lines[0], f"1x {LORD} [Commander]")
        self.assertEqual(sum(1 for x in lines if x.endswith("[Commander]")), 1)
        self.assertFalse(any("[Companion]" in x for x in lines))
        self.assertEqual(sum(int(x.split("x ", 1)[0]) for x in lines), 100)
        self.assertEqual(sorted(x for x in lines if not x.startswith("1x ")), ["3x Swamp"])
        rest = [x.split("x ", 1)[1] for x in lines[1:]]
        self.assertEqual(rest, sorted(rest, key=str.lower))
        self.assertEqual(len(set(rest)), 97)  # 98 distinct names including Lord

    def test_commander_first_actual_oracle_no_opponent_regeneration(self):
        plan = self.packet["commander_identity"]["mechanical_plan"]
        for s in ("me1, released 2007-09-10", "not a Game Changer", "no project exception",
                  "There is no opponent-regeneration clause; the regeneration is Lord's own, for {B}."):
            self.assertIn(s, plan)
        self.assertIn(ORACLE.replace("\n", " "), plan)
        note = self.packet["commander_identity"]["anti_homogenization"]
        self.assertIn("Commander-first to Lord's actual Oracle text", note)
        for s in ("no owner-removed card (Temur Battle Rage)", "Fierce Guardianship and Distortion Strike were author-rejected "
                  "but reopened by Pass C", "Tresserhorn's Lord, Returned 52 -> 51"):
            self.assertIn(s, note)

    def test_owner_direction_flagged_cuts_core_kept_and_judgments(self):
        cand = self.cand()
        for card in CUTS + ["Temur Battle Rage", "Embercleave", "Psychotic Fury", "Glistening Oil", "Soul's Fire",
                            "Distortion Strike", "Aqueous Form", "Orcish Bowmasters", "Swan Song", "Grafted Exoskeleton"]:
            self.assertNotIn(card, cand)
        for keep in self.packet["commander_identity"]["protected_core"]:
            self.assertEqual(cand[keep], 1, keep)
        for owner in ("Anger", "Brotherhood Regalia", "Chandra's Ignition", "Deflecting Swat", "Karn, Argent Defender",
                      "Muddle the Mixture", "Mystic Remora", "Nightscape Familiar", "Not of This World", "Pain for All",
                      "Phyresis", "Slip Out the Back", "Stifle", "Tale's End", "Torpor Orb", "Uncaged Fury",
                      "Cavern of Souls", "Shizo, Death's Storehouse"):
            self.assertEqual(cand[owner], 1, owner)
        self.assertEqual(sorted(c for c, v in self.judged.items() if v["judgment"] == "SELECT_ADD"), ADDS)
        self.assertEqual(self.judged["Fierce Guardianship"]["named_cuts"][0], "Stubborn Denial")
        self.assertEqual(self.judged["Skullclamp"]["named_cuts"][0], "Sheoldred's Edict")
        for alt in ("Soul's Fire", "Distortion Strike"):
            self.assertEqual(self.judged[alt]["judgment"], "RETAIN_ALTERNATIVE", alt)
        for rej in ("Temur Battle Rage", "Aqueous Form", "Embercleave", "Psychotic Fury", "Glistening Oil",
                    "Orcish Bowmasters", "Swan Song", "Grafted Exoskeleton"):
            self.assertEqual(self.judged[rej]["judgment"], "REJECT", rej)
        self.assertEqual(len(self.judged), 15)
        audit = self.packet["low_swap_heightened_audit"]
        weak = {x["card"] for x in audit["weakest_slot_challenge"]}
        self.assertEqual(weak, set(CUTS) | {"Muddle the Mixture", "Nightscape Familiar", "Rogue's Passage", "Pain for All",
                                            "Terminate"})
        pk = [(sorted(p["adds"]), sorted(p["cuts"])) for p in audit["multi_slot_packages"]]
        self.assertEqual(pk[0], (ADDS, CUTS))
        self.assertEqual(len(pk), 8)

    def test_power_bracket_tags_game_changers(self):
        v = self.packet["verification"]
        self.assertEqual(v["power_bracket"], 4)
        self.assertEqual(v["archidekt_tags"], ["Infect", "Voltron", "Aristocrats"])
        nc = self.packet["commander_identity"]["natural_ceiling"]
        self.assertIn("Game Changers 2 -> 3", nc)
        self.assertIn("19 included combos", nc)
        self.assertIn("almost-included 283 -> 289", nc)

    def test_alternatives_staged_as_complete_hundreds(self):
        def load(name):
            return Counter(gate.parse_list(RC / f"{D}_{name}_20261023.txt")[0])
        four_a = ["Black Market Connections", "Consign to Memory", "Fierce Guardianship", "Ornithopter of Paradise"]
        four_c = ["Cover of Darkness", "Feed the Swarm", "Fellwar Stone", "Stubborn Denial"]
        cases = {
            "alt_A_four_swaps_keep_SheoldredsEdict": (four_a, four_c),
            "alt_B_Skullclamp_minus_MuddleTheMixture_keep_SheoldredsEdict": (ADDS, four_c + ["Muddle the Mixture"]),
            "alt_C_Skullclamp_minus_NightscapeFamiliar": (ADDS, four_c + ["Nightscape Familiar"]),
            "PassC_plus_SoulsFire_minus_SheoldredsEdict_over_candidate_Skullclamp":
                (four_a + ["Soul's Fire"], four_c + ["Sheoldred's Edict"]),
            "PassC_plus_FierceGuardianship_minus_NightscapeFamiliar":
                (ADDS, ["Cover of Darkness", "Feed the Swarm", "Fellwar Stone", "Nightscape Familiar", "Sheoldred's Edict"]),
            "PassC_plus_DistortionStrike_minus_RoguesPassage": (ADDS + ["Distortion Strike"], CUTS + ["Rogue's Passage"]),
            "rejected_plus_AqueousForm_minus_MuddleTheMixture": (ADDS + ["Aqueous Form"], CUTS + ["Muddle the Mixture"]),
            "rejected_prior_draft_TemurBattleRage_minus_PainForAll_owner_cut":
                (["Black Market Connections", "Fierce Guardianship", "Ornithopter of Paradise", "Skullclamp",
                  "Temur Battle Rage"],
                 ["Cover of Darkness", "Fellwar Stone", "Pain for All", "Sheoldred's Edict", "Stubborn Denial"]),
            "rejected_original_tentative_plan":
                (["Aqueous Form", "Fierce Guardianship", "Skullclamp", "Soul's Fire", "Temur Battle Rage"],
                 ["Cover of Darkness", "Fellwar Stone", "Nightscape Familiar", "Pain for All", "Sheoldred's Edict"]),
        }
        base = Counter(gate.parse_list(BASE)[0])
        for name, (adds, cuts) in cases.items():
            a = load(name)
            self.assertEqual(sum(a.values()), 100, name)
            self.assertEqual(sorted((a - base).elements()), sorted(adds), name)
            self.assertEqual(sorted((base - a).elements()), sorted(cuts), name)

    def test_commander_legal_released_no_exception(self):
        snap = json.loads((ROOT / f"data/grixis/m6/oracle_snapshots/{D}_M7_Scryfall_20261023.json").read_text())
        cards = {c["name"]: c for c in snap["cards"]}
        g = cards[LORD]
        self.assertEqual(g["commander_legality"], "legal")
        self.assertIs(g["game_changer"], False)
        self.assertEqual(g["oracle_text"], ORACLE)
        self.assertEqual((g["set"], g["released_at"]), ("me1", "2007-09-10"))
        self.assertEqual(snap["project_exceptions"], "0")
        cand = set(gate.parse_list(ROOT / self.packet["final_candidate"]["path"])[0])
        gc = sorted(c["name"] for c in snap["cards"] if c["name"] in cand | {LORD} and c["game_changer"])
        self.assertEqual(gc, sorted(ast.literal_eval(snap["game_changers_in_candidate"])))
        self.assertEqual(gc, ["Demonic Tutor", "Fierce Guardianship", "Vampiric Tutor"])

    def test_no_approval_or_lock_markers_in_new_artifacts(self):
        for p in [PACKET, ROOT / self.packet["final_candidate"]["path"]]:
            text = p.read_text()
            self.assertNotIn("CANONICAL_LOCKED", text)
            self.assertNotIn('"APPROVED"', text)


if __name__ == "__main__":
    unittest.main()
