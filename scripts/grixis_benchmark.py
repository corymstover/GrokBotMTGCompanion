#!/usr/bin/env python3
"""G0 benchmark corpus (Bot cycle 64.1): frozen retrospective corpus + prospective holdout (Grixis Birthday Upgrade Plan,
decision D2). The corpus (data/grixis/benchmark/corpus.json) holds outcome-free prompts; each expected outcome is in
data/grixis/benchmark/sealed/<id>.json, whose sha256 is recorded in manifest.json. Evaluation inputs are corpus.json
only. Limitation: sealed files sit in the same repository, so sealing is tamper-evidence plus input separation, not secrecy,
and most retrospective items are contamination-flagged because the new system already ingested their sources.

  python3 scripts/grixis_benchmark.py --check     schema, manifest hashes, no leaks, every source exists (validate_all step 'benchmark')
  python3 scripts/grixis_benchmark.py --freeze    (re)write manifest.json; refused once the corpus is immutable
  python3 scripts/grixis_benchmark.py --summary
"""
import argparse
import hashlib
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
B = ROOT / "data" / "grixis" / "benchmark"
SCHEMA = ROOT / "data" / "grixis" / "schemas" / "benchmark_item.schema.json"
REPORTING_RULE = {
    "stratify_by": ["evaluation_role", "originated_by", "contamination.level"],
    "pooled_score_allowed": False,
    "rule": ("Any benchmark report gives results per stratum (evaluation_role x originated_by x contamination level, with counts) "
             "and never one pooled score. regression_guard items measure non-reversion only, never detection; "
             "judgment_calibration items measure agreement with unvalidated v1 or source judgments, never accuracy; "
             "the prospective holdout is reported separately from the retrospective corpus."),
}
FREEZE_RULE = ("The retrospective corpus may grow in G0 batches until step A (adaptive saturation) begins. From the first A commit "
               "it is immutable: no item added, edited or removed; a wrong item is retracted by a new record. Only the "
               "prospective holdout grows afterwards.")


def sha(p):
    return "sha256:" + hashlib.sha256(Path(p).read_bytes()).hexdigest()


def load(p):
    return json.loads(Path(p).read_text())


def validator(defn=None):
    import jsonschema
    s = load(SCHEMA)
    if defn:
        s = dict(s["$defs"][defn], **{"$schema": s["$schema"]})
    return jsonschema.Draft202012Validator(s)


def commit_exists(c):
    try:
        return subprocess.run(["git", "-C", str(ROOT), "cat-file", "-e", c + "^{commit}"], capture_output=True).returncode == 0
    except OSError:
        return None


def source_problems(s):
    k = s["kind"]
    if k == "file":
        p = ROOT / s["path"]
        if not p.is_file():
            return [f"missing file {s['path']}"]
        return [] if s["quote"] in p.read_text(errors="replace") else [f"quote not found in {s['path']}: {s['quote']!r}"]
    if k == "chat":
        p = ROOT / s["recorded_in"]
        if not p.is_file():
            return [f"missing record {s['recorded_in']}"]
        return [] if s["ref"] in p.read_text(errors="replace") else [f"chat ref {s['ref']} not in {s['recorded_in']}"]
    if k == "pr":
        ok = commit_exists(s["merge_commit"])
        return [f"PR #{s['number']} merge commit {s['merge_commit']} not in git history"] if ok is False else []
    return [f"unknown source kind {k}"]


def leak_problems(item, sealed):
    p = item["prompt"].lower()
    out = [f"{item['id']}: prompt leaks sealed term {t!r}" for t in sealed["leak_terms"] if t.lower() in p]
    if sealed["expected_outcome"].lower()[:60] in p:
        out.append(f"{item['id']}: prompt contains the expected outcome")
    return out


def build_manifest(corpus_path=None):
    corpus = load(corpus_path or B / "corpus.json")
    return {"schema_version": 1, "cycle": "Bot cycle 64.1", "status": "growing", "immutable_from": "first commit of step A",
            "freeze_rule": FREEZE_RULE, "reporting_rule": REPORTING_RULE, "corpus_sha256": sha(B / "corpus.json"), "item_count": len(corpus["items"]),
            "sealed": {i["id"]: sha(B / "sealed" / f"{i['id']}.json") for i in corpus["items"]},
            "holdout_sha256": sha(B / "prospective_holdout.json")}


def problems():
    p = []
    corpus, man = load(B / "corpus.json"), load(B / "manifest.json")
    iv, sv = validator(), validator("sealed")
    ids = [i["id"] for i in corpus["items"]]
    if man.get("reporting_rule") != REPORTING_RULE:
        p.append("manifest reporting_rule missing or changed: reports must stratify by evaluation_role, origin and contamination")
    reg = load(ROOT / "data" / "grixis" / "registry.json")["decks"]
    reg_ids = {d["deck_id"] for d in (reg.values() if isinstance(reg, dict) else reg)}
    if len(ids) != len(set(ids)):
        p.append("duplicate item ids")
    if man["corpus_sha256"] != sha(B / "corpus.json"):
        p.append("corpus.json changed since the manifest was written (re-freeze, or the corpus is immutable)")
    if man["holdout_sha256"] != sha(B / "prospective_holdout.json") and man["status"] == "growing":
        p.append("prospective_holdout.json changed without a manifest update")
    if set(man["sealed"]) != set(ids):
        p.append("manifest sealed set differs from corpus ids")
    extra = {f.stem for f in (B / "sealed").glob("*.json")} - set(ids)
    if extra:
        p.append(f"sealed files without a corpus item: {sorted(extra)}")
    for it in corpus["items"]:
        p += [f"{it['id']}: {e.message}" for e in iv.iter_errors(it)]
        sp = B / "sealed" / f"{it['id']}.json"
        if not sp.is_file():
            p.append(f"{it['id']}: no sealed file")
            continue
        if man["sealed"].get(it["id"]) != sha(sp):
            p.append(f"{it['id']}: sealed hash does not match manifest")
        s = load(sp)
        p += [f"{it['id']} sealed: {e.message}" for e in sv.iter_errors(s)]
        if s.get("id") != it["id"]:
            p.append(f"{it['id']}: sealed id mismatch")
        p += leak_problems(it, s)
        if any(k in it for k in ("expected_outcome", "verdict", "answer")):
            p.append(f"{it['id']}: outcome field in the evaluation input")
        ds = it.get("deck_snapshot")
        if ds and ds["registry_deck_id"] not in reg_ids:
            p.append(f"{it['id']}: deck_snapshot id {ds['registry_deck_id']} not in the registry")
        if ds and ds["registry_deck_id"] != it["deck"]:
            p.append(f"{it['id']}: deck field differs from deck_snapshot id")
        if it.get("evaluation_role") == "detection" and s.get("label_authority", "").startswith("unvalidated_v1_judgment"):
            p.append(f"{it['id']}: an unvalidated v1 label cannot be a detection item")
        for src in it["sources"]:
            p += [f"{it['id']}: {x}" for x in source_problems(src)]
    h = load(B / "prospective_holdout.json")
    for it in h["items"]:
        p += [f"holdout {it.get('id')}: {e.message}" for e in iv.iter_errors(it)]
        if it.get("contamination", {}).get("level") != "no":
            p.append(f"holdout {it.get('id')}: holdout items must start uncontaminated")
    return p


def summary():
    c = load(B / "corpus.json")["items"]
    print(f"{len(c)} items")
    for k in ("category", "originated_by", "caught_by"):
        print(k, dict(Counter(i[k] for i in c).most_common()))
    print("contamination", dict(Counter(i["contamination"]["level"] for i in c)))
    print("evaluation_role", dict(Counter(i["evaluation_role"] for i in c)))
    print("strata (role, origin, contamination)", {"/".join(k): v for k, v in sorted(Counter(
        (i["evaluation_role"], i["originated_by"], i["contamination"]["level"]) for i in c).items())})


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--check", action="store_true")
    a.add_argument("--freeze", action="store_true")
    a.add_argument("--summary", action="store_true")
    x = a.parse_args()
    if x.freeze:
        mp = B / "manifest.json"
        if mp.is_file() and load(mp).get("status") == "immutable":
            sys.exit("corpus is immutable (step A has begun); add to the prospective holdout instead")
        mp.write_text(json.dumps(build_manifest(), indent=2) + "\n")
        print("manifest written")
    if x.summary:
        summary()
    if x.check:
        p = problems()
        for e in p:
            print("FAIL", e)
        n = len(load(B / "corpus.json")["items"])
        print(f"benchmark: {n} items, {len(p)} problems")
        sys.exit(1 if p else 0)


if __name__ == "__main__":
    main()
