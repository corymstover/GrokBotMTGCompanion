"""Cross-commander M6 source-fingerprint, coverage and pass-only cache tests."""
import hashlib
import json
from pathlib import Path
import tempfile
from types import SimpleNamespace
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_m6_reuse as suite

def fake_setup(where):
    root=Path(where)
    for x in ("scripts","tests","data/grixis","data/grixis/m6"):
        (root/x).mkdir(parents=True,exist_ok=True)
    (root/"scripts/grixis_m6_reuse.py").write_bytes((ROOT/"scripts/grixis_m6_reuse.py").read_bytes())
    (root/"tests/test_stub.py").write_text("class Placeholder: pass\n")
    (root/"scripts/physical.py").write_text("A=1\n")
    doc={"schema_version":1,
        "governance":{"can_issue_phase_b_complete":False,"can_issue_m6_certificate":False,
            "can_issue_m7_approval":False,"can_apply_swaps":False},
        "suites":{"physical":{"coverage":"physical_only","test":"test_stub.py",
                 "files":["tests/test_stub.py","scripts/physical.py"],"globs":[]}}}
    (root/suite.MANIFEST).write_text(json.dumps(doc))
    registry={"decks":{
        "A":{"source":{"recorded_sha256":"a"*64,"recorded_matches_raw":True},
             "canonical_project_list":{"export":"scripts/physical.py"}},
        "B":{"source":{"recorded_sha256":"b"*64,"recorded_matches_raw":True},
             "canonical_project_list":{"export":"scripts/physical.py"}}
    }}
    (root/"data/grixis/registry.json").write_text(json.dumps(registry))
    return root

class FakeRun:
    def __init__(self,code=0,stderr="Ran 3 tests in 0.021s\nOK"):
        self.calls=0;self.code=code;self.stderr=stderr
    def __call__(self,args,**opts):
        self.calls+=1
        assert args[1:4]==["-m","unittest","discover"]
        assert "-p" in args and opts["cwd"].is_dir()
        return SimpleNamespace(returncode=self.code,stdout="",stderr=self.stderr)

class CrossDeckReusableSuites(unittest.TestCase):
    def test_real_manifest_governance_and_existing_files(self):
        document=suite.load_manifest(ROOT)
        self.assertTrue(document["suites"])
        self.assertGreaterEqual(len(document["suites"]),3)
        for name,spec in document["suites"].items():
            with self.subTest(name=name):
                fingerprint,files=suite.suite_key(name,spec,document,ROOT)
                self.assertEqual(len(fingerprint),64)
                self.assertGreaterEqual(len(files),3)
                self.assertIn("scripts/grixis_m6_reuse.py",files)
                self.assertIn("data/grixis/m6/reusable_test_suites.json",files)
                self.assertTrue(spec["coverage"])
        self.assertFalse(document["governance"]["can_apply_swaps"])

    def test_exact_unchanged_pass_reuses_from_another_deck(self):
        with tempfile.TemporaryDirectory() as temp:
            root=fake_setup(temp)
            spy=FakeRun()
            a=suite.run_requested(["physical"],"A",root,run=True,subprocess_call=spy)
            b=suite.run_requested(["physical"],"B",root,run=True,subprocess_call=spy)
            self.assertEqual(spy.calls,1)
            self.assertEqual(a["results"][0]["status"],"EXECUTED_AND_CACHED")
            self.assertEqual(b["results"][0]["status"],"REUSED_VALIDATED_PASS")
            self.assertEqual(a["results"][0]["key"],b["results"][0]["key"])
            self.assertNotEqual(a["source_binding"]["registered_raw_sha256"],
                                b["source_binding"]["registered_raw_sha256"])
            self.assertFalse(b["full_phase_b_achieved"])
            self.assertFalse(b["deck_approved"])
            self.assertFalse(b["authority"]["can_certify_m6"])

    def test_changed_suite_source_invalidates_reuse(self):
        with tempfile.TemporaryDirectory() as temp:
            root=fake_setup(temp);spy=FakeRun()
            suite.run_requested(["physical"],root=root,run=True,subprocess_call=spy)
            (root/"scripts/physical.py").write_text("A=2\n")
            next_run=suite.run_requested(["physical"],root=root,run=True,subprocess_call=spy)
            self.assertEqual(spy.calls,2)
            self.assertEqual(next_run["results"][0]["status"],"EXECUTED_AND_CACHED")

    def test_changed_runner_logic_and_test_file_invalidates(self):
        with tempfile.TemporaryDirectory() as temp:
            root=fake_setup(temp)
            manifest=suite.load_manifest(root)
            spec=manifest["suites"]["physical"]
            a,_=suite.suite_key("physical",spec,manifest,root)
            (root/"tests/test_stub.py").write_text("def test_changed(): pass\n")
            b,_=suite.suite_key("physical",spec,manifest,root)
            self.assertNotEqual(a,b)
            (root/"scripts/grixis_m6_reuse.py").write_text("new runner code")
            c,_=suite.suite_key("physical",spec,manifest,root)
            self.assertNotEqual(b,c)

    def test_fail_and_zero_test_never_cached(self):
        for code,stderr in [(1,"Ran 1 test in 0.1s\nFAILED"),
                            (0,"Ran 0 tests in 0.1s\nOK"),(0,"no tests")]:
            with self.subTest(code=code,stderr=stderr):
                with tempfile.TemporaryDirectory() as temp:
                    root=fake_setup(temp)
                    spy=FakeRun(code,stderr)
                    result=suite.run_requested(["physical"],root=root,run=True,
                                               subprocess_call=spy)
                    self.assertEqual(result["results"][0]["status"],"FAILED_NOT_CACHED")
                    self.assertFalse(result["all_suites_pass_or_reused"])
                    result=suite.run_requested(["physical"],root=root,run=True,
                                               subprocess_call=spy)
                    self.assertEqual(spy.calls,2)

    def test_forged_cache_metadata_not_trusted(self):
        with tempfile.TemporaryDirectory() as temp:
            root=fake_setup(temp);spy=FakeRun()
            a=suite.run_requested(["physical"],root=root,run=True,subprocess_call=spy)
            key=a["results"][0]["key"]
            receipt=root/suite.DEFAULT_CACHE/"physical"/(key+".json")
            obj=json.loads(receipt.read_text());obj["authority"]["can_certify_m6"]=True
            receipt.write_text(json.dumps(obj))
            b=suite.run_requested(["physical"],root=root,run=True,subprocess_call=spy)
            self.assertEqual(spy.calls,2)
            self.assertEqual(b["results"][0]["status"],"EXECUTED_AND_CACHED")

    def test_missing_dependency_and_parent_path_blocked(self):
        with tempfile.TemporaryDirectory() as temp:
            root=fake_setup(temp);m=suite.load_manifest(root)
            m["suites"]["physical"]["files"].append("../outside.py")
            with self.assertRaises(ValueError):
                suite.suite_key("physical",m["suites"]["physical"],m,root)
            m["suites"]["physical"]["files"].pop()
            (root/"scripts/physical.py").unlink()
            with self.assertRaises(ValueError):
                suite.suite_key("physical",m["suites"]["physical"],m,root)

    def test_unregistered_test_and_unknown_deck_and_claims_blocked(self):
        with tempfile.TemporaryDirectory() as temp:
            root=fake_setup(temp)
            m=suite.load_manifest(root)
            m["suites"]["physical"]["test"]="something;rm -rf ."
            with self.assertRaises(ValueError):
                suite.suite_key("physical",m["suites"]["physical"],m,root)
            with self.assertRaises(ValueError):
                suite.run_requested(["physical"],deck_id="INVALID",root=root)
            with self.assertRaises(ValueError):
                suite.run_requested(["nonexistent"],root=root)
            m=suite.load_manifest(root);m["governance"]["can_apply_swaps"]=True
            (root/suite.MANIFEST).write_text(json.dumps(m))
            with self.assertRaises(ValueError):
                suite.load_manifest(root)

    def test_dry_plan_never_executes_and_requires_cache_on_reuse(self):
        with tempfile.TemporaryDirectory() as temp:
            root=fake_setup(temp);spy=FakeRun()
            plan=suite.run_requested(["physical"],root=root,run=False,
                                     subprocess_call=spy)
            self.assertEqual(spy.calls,0)
            self.assertEqual(plan["results"][0]["status"],"WOULD_RUN")
            suite.run_requested(["physical"],root=root,run=True,subprocess_call=spy)
            plan=suite.run_requested(["physical"],root=root,run=False,subprocess_call=spy)
            self.assertEqual(plan["results"][0]["status"],"REUSED_VALIDATED_PASS")
            self.assertTrue(plan["all_suites_pass_or_reused"])

    def test_registered_crossdeck_source_binding_is_not_live_canonical(self):
        doc=suite.canonical_registry_binding("Abaddon_the_Despoiler",ROOT)
        self.assertEqual(doc["scope"],"registered_frozen_source_not_live_canonical")
        self.assertEqual(doc["registered_raw_sha256"],
                         "2d6203d274c25e67fb93acf5e6784dce4ee1e8999844a6ab032d9b15995acfbf")
        self.assertEqual(len(doc["source_export_sha256"]),64)

if __name__=="__main__":unittest.main()
