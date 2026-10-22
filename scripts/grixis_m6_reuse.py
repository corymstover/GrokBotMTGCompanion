#!/usr/bin/env python3
"""Cross-deck M6 test-suite reuse: exact-input cache, not automated deck verdicts.

No user-controlled command execution: suite test filenames are declared in a
repository manifest and run through Python unittest discovery. This caches
only successful, nonempty test-suite executions under hashes of ALL registered
dependencies, baseline exports, manifest and this runner. An unregistered
effect or changed input must be separately tested. Never changes decklists.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = Path("data/grixis/m6/reusable_test_suites.json")
DEFAULT_CACHE = Path(".cache/grixis_m6_reuse")
AUTHORITY = {
    "supports_deck_improvement_claim": False,
    "supports_full_phase_b": False,
    "can_certify_m6": False,
    "can_approve_m7": False,
    "can_change_decklists": False,
}
TEST_PATTERN = re.compile(r"^test_[a-z0-9_]+\.py$")
SHA_PATTERN = re.compile(r"^[0-9a-f]{64}$")
COUNT_PATTERN = re.compile(r"Ran\s+(\d+)\s+tests?\s+in\s+", re.IGNORECASE)


def load_manifest(root=ROOT):
    doc = json.loads((root / MANIFEST).read_text(encoding="utf-8"))
    if doc.get("schema_version") != 1 or not isinstance(doc.get("suites"), dict):
        raise ValueError("Unrecognized reusable test manifest")
    if not doc["suites"]:
        raise ValueError("Empty reusable suite manifest")
    if any(doc.get("governance", {}).get(k) is not False
           for k in ("can_issue_phase_b_complete", "can_issue_m6_certificate",
                     "can_issue_m7_approval", "can_apply_swaps")):
        raise ValueError("Reuse manifest cannot authorize milestone or list mutations")
    return doc


def safe_path(root, relative):
    if not isinstance(relative, str) or not relative or "\\" in relative:
        raise ValueError("Invalid dependency pathname")
    p = Path(relative)
    if p.is_absolute() or ".." in p.parts or str(p) != relative:
        raise ValueError("Dependency paths must be repository-relative")
    f = root / p
    if not f.is_file():
        raise ValueError("Missing source-bound test dependency: " + relative)
    return f


def suite_dependencies(name, spec, root=ROOT):
    if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9-]+", name):
        raise ValueError("Invalid suite name")
    test = spec.get("test")
    if not isinstance(test, str) or not TEST_PATTERN.fullmatch(test):
        raise ValueError("Only known unittest files can be executed")
    expected = safe_path(root, "tests/" + test)
    if "tests/" + test not in spec.get("files", []):
        raise ValueError("Every test file must be in its own dependency hash")
    paths = {expected}
    for rel in spec.get("files", []):
        paths.add(safe_path(root, rel))
    for gl in spec.get("globs", []):
        if not isinstance(gl, str) or gl.startswith("/") or ".." in Path(gl).parts or "\\" in gl:
            raise ValueError("Unsafe dependency glob")
        matches = list(root.glob(gl))
        if not matches or any(not x.is_file() for x in matches):
            raise ValueError("Empty or non-file dependency glob: " + gl)
        paths.update(matches)
    # All hash paths must resolve within ROOT, even if symbolic links appear.
    base = root.resolve()
    for p in paths:
        if not p.resolve().is_relative_to(base):
            raise ValueError("Dependency escapes repository")
    return tuple(sorted(paths, key=lambda x: x.relative_to(root).as_posix()))


def suite_key(name, spec, manifest, root=ROOT):
    files = suite_dependencies(name, spec, root)
    # Fingerprint runner logic as well: no stale cache after code changes.
    runner = safe_path(root, "scripts/grixis_m6_reuse.py")
    manifest_path = safe_path(root, MANIFEST.as_posix())
    files = tuple(sorted(set(files) | {runner, manifest_path},
                         key=lambda x: x.relative_to(root).as_posix()))
    digest = hashlib.sha256()
    digest.update(b"grixis-m6-shared-suite-v1\0")
    digest.update(name.encode() + b"\0")
    for f in files:
        rel = f.relative_to(root).as_posix().encode()
        data = f.read_bytes()
        digest.update(len(rel).to_bytes(4, "big") + rel)
        digest.update(len(data).to_bytes(8, "big") + hashlib.sha256(data).digest())
    return digest.hexdigest(), [str(x.relative_to(root)) for x in files]


def canonical_registry_binding(deck_id, root=ROOT):
    if deck_id is None:
        return {"scope": "repository_62_source_snapshot", "deck_id": None}
    registry = json.loads(safe_path(root, "data/grixis/registry.json").read_text(encoding="utf-8"))
    record = registry.get("decks", {}).get(deck_id)
    if record is None:
        raise ValueError("Deck not in the registered 62: " + str(deck_id))
    source = record.get("source", {})
    sha = source.get("recorded_sha256")
    if not isinstance(sha, str) or not SHA_PATTERN.fullmatch(sha) or not source.get("recorded_matches_raw"):
        raise ValueError("Registered source hash not trusted")
    rel = record.get("canonical_project_list", {}).get("export")
    f = safe_path(root, rel)
    # This is a frozen REGISTERED SOURCE binding. It does not fetch the
    # current external canonical GitHub approval. Never call it live checked.
    return {"scope": "registered_frozen_source_not_live_canonical",
            "deck_id": deck_id, "registered_raw_sha256": sha,
            "source_export": rel,
            "source_export_sha256": hashlib.sha256(f.read_bytes()).hexdigest()}


def cached_pass(path, key, suite):
    try:
        rec = json.loads(path.read_text(encoding="utf-8"))
        return (rec.get("suite") == suite and rec.get("key") == key and
                rec.get("status") == "PASS" and
                isinstance(rec.get("tests_run"), int) and
                rec["tests_run"] > 0 and
                rec.get("authority") == AUTHORITY and
                rec.get("coverage") == "foundation_only_no_gameplay")
    except (OSError, ValueError, TypeError, AttributeError):
        return False


def execute_suite(name, spec, root, cache, manifest, force=False, run=False,
                  subprocess_call=subprocess.run):
    key, inputs = suite_key(name, spec, manifest, root)
    dest = cache / name / (key + ".json")
    was_cached = cached_pass(dest, key, name)
    base = {"suite": name, "key": key, "coverage": "foundation_only_no_gameplay",
            "limitations": spec["coverage"], "hash_bound_inputs": inputs,
            "authority": dict(AUTHORITY)}
    if was_cached and not force:
        return {**base, "status": "REUSED_VALIDATED_PASS", "tests_run": json.loads(dest.read_text())["tests_run"]}
    if not run:
        return {**base, "status": "WOULD_RUN", "reason": "no validated identical-input pass"}
    # Never accept a caller-supplied shell command.
    command = [sys.executable, "-m", "unittest", "discover", "-s", "tests",
               "-p", spec["test"], "-v"]
    result = subprocess_call(command, cwd=root, capture_output=True, text=True)
    output = (result.stdout or "") + "\n" + (result.stderr or "")
    counts = COUNT_PATTERN.findall(output)
    tests_run = int(counts[-1]) if counts else 0
    if result.returncode != 0 or tests_run < 1:
        return {**base, "status": "FAILED_NOT_CACHED",
                "tests_run": tests_run, "exit_code": result.returncode,
                "diagnostic_tail": output[-4000:]}
    rec = {**base, "status": "PASS", "tests_run": tests_run}
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(rec, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return {**base, "status": "EXECUTED_AND_CACHED", "tests_run": tests_run}


def run_requested(suites, deck_id=None, root=ROOT, cache=None, force=False, run=False,
                  subprocess_call=subprocess.run):
    manifest = load_manifest(root)
    suite_names = list(manifest["suites"])
    if suites and "all" not in suites:
        chosen = list(dict.fromkeys(suites))
    else:
        chosen = suite_names
    if any(x not in manifest["suites"] for x in chosen):
        raise ValueError("Unknown suite: " + ",".join(x for x in chosen if x not in manifest["suites"]))
    binding = canonical_registry_binding(deck_id, root)
    cache_root = (root / DEFAULT_CACHE) if cache is None else Path(cache)
    results = [execute_suite(name, manifest["suites"][name], root, cache_root, manifest,
                             force=force, run=run, subprocess_call=subprocess_call)
               for name in chosen]
    return {"schema_version": 1, "runner": "source_bound_m6_shared_foundation_cache_v1",
            "source_binding": binding, "authority": dict(AUTHORITY),
            "all_suites": suite_names, "results": results,
            "all_suites_pass_or_reused": bool(run or all(x["status"]=="REUSED_VALIDATED_PASS" for x in results))
                  and all(x["status"] in ("EXECUTED_AND_CACHED", "REUSED_VALIDATED_PASS") for x in results),
            "full_phase_b_achieved": False, "deck_approved": False}


def main():
    ap = argparse.ArgumentParser(description="Cache verified common M6 foundations; NEVER game wins/certification")
    ap.add_argument("--suite", action="append", default=[], help="reusable suite name, repeatable, or all")
    ap.add_argument("--deck-id", help="optional frozen registry-only deck source/provenance check")
    ap.add_argument("--run", action="store_true", help="execute uncached tests, otherwise plan only")
    ap.add_argument("--force", action="store_true", help="rerun even a matching passing cache")
    ap.add_argument("--cache-dir", type=Path)
    ap.add_argument("--json-out", type=Path)
    args = ap.parse_args()
    try:
        report = run_requested(args.suite, deck_id=args.deck_id,
            cache=args.cache_dir, run=args.run, force=args.force)
    except (ValueError, OSError, KeyError) as ex:
        ap.error(str(ex))
    rendered = json.dumps(report, sort_keys=True, indent=2) + "\n"
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(rendered, encoding="utf-8")
    print(rendered)
    if args.run and not report["all_suites_pass_or_reused"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
