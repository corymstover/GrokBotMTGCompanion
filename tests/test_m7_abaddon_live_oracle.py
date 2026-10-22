"""Fast fail-closed regression tests for network-capable Abaddon Oracle audit.

All tests use fake transport and never contact Scryfall. Live checks run in a
separate, mandatory exact-head CI step.
"""
from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path
import unittest

from scripts.grixis_m7_abaddon_live_oracle import (
    ALLOWED, BASIC, ROOT, SOURCE_ROW, MANIFEST, SCRYFALL,
    OracleGateError, assess, collected_cards, parse_approved_raw,
    sha256_bytes, source_reconcile, staged_variants, text_and_faces,
)

MAN = json.loads(MANIFEST.read_text(encoding="utf-8"))


def fake_record(name):
    expected_mvs = {"The Lost and the Damned":3, "Call Forth the Tempest":8,
                    "Keeper of Secrets":6, "The Ruinous Powers":4,
                    "Grinning Ignus":3,"Chaos Warp":3,
                    "Aggravated Assault":3,"Inevitable Betrayal":0}
    oracle = ("Whenever you cast a spell from anywhere other than your hand"
              if name=="Keeper of Secrets" else
              "Cascade, cascade" if name=="Call Forth the Tempest" else
              "Fixture-only oracle text")
    return {
        "object":"card", "name":name, "oracle_id":"fixture-uuid",
        "id":"fixture-print-id", "scryfall_uri":"https://scryfall.com/fixture",
        "cmc":expected_mvs.get(name,2),
        "oracle_text":oracle, "mana_cost":"{2}", "games":["paper"],
        "legalities":{"commander":"legal"}, "color_identity":[],
        "layout":"normal","released_at":"2026-01-01",
    }


class AbaddonLiveOracleOfflineContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base, cls.cmd, cls.comp = __import__(
            "scripts.grixis_m7_decision_gate",fromlist=["parse_list"]
        ).parse_list(ROOT/MAN["baseline_source_path"])
        cls.variants=staged_variants(MAN,cls.base)
        cls.names={x for cards in cls.variants.values() for x in cards}

    def test_source_and_variants_finite_and_faithful(self):
        self.assertEqual(len(self.variants),5)
        self.assertEqual(len(self.base),100)
        self.assertEqual(len(set(self.base)),94)
        for name,cards in self.variants.items():
            with self.subTest(list=name):
                self.assertEqual(len(cards),100)
                self.assertEqual(len(set(cards)),94)
                self.assertEqual(cards[0],"Abaddon the Despoiler")

    def test_true_canonical_raw_import_compares_source_and_fails_on_hash_drift(self):
        # Construct syntactically valid Archidekt raw fixture from the actual
        # source mirror; only the test's expected digest is substituted.
        lines=[]
        for row in (ROOT/MAN["baseline_source_path"]).read_text().splitlines():
            qty,name=row.split(" ",1)
            if name.endswith(" [Commander]"):
                name=name.removesuffix(" [Commander]")
                role="Commander{top}"
            else:
                role="Land"
            lines.append(f"{qty}x {name} (tst) 1 [{role}]")
        fixture=("\n".join(lines)+"\n").encode("utf-8")
        cards,cmd=parse_approved_raw(fixture)
        self.assertEqual(cards, self.base)
        self.assertEqual(cmd, ["Abaddon the Despoiler"])
        altered={**MAN, "canonical_baseline_raw_sha256":sha256_bytes(fixture)}
        self.assertEqual(source_reconcile(altered,fixture)[0],self.base)
        with self.assertRaisesRegex(OracleGateError,"SHA drift"):
            source_reconcile(MAN,fixture)

    def test_collection_batched_no_missing_or_repeated_requests(self):
        requests=[]
        sleeps=[]
        def fake_fetch(url,payload):
            self.assertEqual(url,SCRYFALL)
            names=[x["name"] for x in payload["identifiers"]]
            requests.append(names)
            rows=[fake_record("Birgi, God of Storytelling // Harnfel, Horn of Bounty"
                              if n=="Birgi, God of Storytelling" else n)
                  for n in names]
            return json.dumps({"object":"list","data":rows,
                               "not_found":[]}).encode("utf-8")
        cards=collected_cards(self.names,fetch=fake_fetch,sleeper=sleeps.append)
        self.assertEqual(set(cards),self.names)
        self.assertEqual(len(requests),2)  # 94 original + 3 material candidates
        self.assertLessEqual(max(map(len,requests)),75)
        self.assertEqual(len(sleeps),1)
        self.assertGreaterEqual(sleeps[0],0.5)

    def test_every_unique_card_current_legality_text_and_identity_validated(self):
        cards={n:fake_record(n) for n in self.names}
        evidence=assess(cards,self.variants)
        self.assertEqual(set(evidence),self.names)
        self.assertEqual(evidence["The Lost and the Damned"]["mana_value"],3)
        self.assertEqual(evidence["Call Forth the Tempest"]["mana_value"],8)
        for name,field,val in (
            ("Chaos Warp","color_identity",["G"]),
            ("Inevitable Betrayal","legalities",{"commander":"banned"}),
            ("Keeper of Secrets","games",["arena"]),
            ("Grinning Ignus","oracle_id",None),
            ("Call Forth the Tempest","oracle_text","No cascade here"),
        ):
            with self.subTest(card=name,problem=field):
                fake={n:dict(c) for n,c in cards.items()}
                fake[name][field]=val
                with self.assertRaises(OracleGateError):
                    assess(fake,self.variants)

    def test_missing_ambiguous_and_corrupt_scryfall_returns_all_fail(self):
        examples=[
            {"object":"list","data":[],"not_found":[{"name":"Ignus"}]},
            {"object":"list","data":[],"not_found":[]},
            {"object":"error","status":429},
            {"object":"list","data":[fake_record("Different Card")],"not_found":[]},
        ]
        for response in examples:
            with self.subTest(payload=response.get("object")):
                with self.assertRaises(OracleGateError):
                    collected_cards(["Grinning Ignus"],fetch=lambda url,payload:json.dumps(response).encode())

    def test_dual_face_oracle_text_and_empty_faces_fail_closed(self):
        self.assertEqual(text_and_faces({"card_faces":[{"oracle_text":"Face 1"},{"oracle_text":"Face 2"}]}),
                         "Face 1\n//\nFace 2")
        with self.assertRaises(OracleGateError):
            text_and_faces({"card_faces":[]})


if __name__=="__main__":
    unittest.main()
