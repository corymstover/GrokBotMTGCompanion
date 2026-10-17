#!/usr/bin/env python3
"""Cycle 80: replay A/B in physically separate Actions runner jobs.

Projection producer has full authority to READ accepted evidence; pass runners
receive only side-specific whitelist projections and side-specific sealed output
files via sparse checkout, with checkout credentials disabled. They do NOT get
the full accepted corpus in their working trees. This is a reproducibility and
operational-blinding improvement, not a proof against malicious remote fetch.
Older sealed commits stay intact. No approvals or final decisions are written.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import grixis_m6_sealed as sealed  # noqa: E402

INPUTS=ROOT/"data/grixis/m6/blind_inputs"
SEALED=ROOT/"data/grixis/m6/sealed"
SUMMARY=ROOT/"data/grixis/birthday_m5/summary.json"
AUTH={"can_decide":False,"can_apply_swap":False,"can_approve_or_lock":False}


def encode(obj):
    return json.dumps(obj, sort_keys=True, ensure_ascii=False, indent=1)+"\n"


def sha(bytes_):
    return "sha256:"+hashlib.sha256(bytes_).hexdigest()


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def sanitized(side,doc):
    projection=sealed.project_a(doc) if side=="A" else sealed.project_b(doc)
    # Each side only sees preselected whitelisted fields. Neither sees the other
    # side's objective inputs. Neither input includes the other pass's decision.
    if side=="A":
        assert "tests" not in projection
        assert all("test" not in c["review"] and "edhrec" not in c["review"]
                   for c in projection["candidates"])
    else:
        assert "candidates" not in projection
        assert all("blueprint" not in s and "D_commander" not in s for s in projection["swaps"])
    return projection


def prepare():
    rows=sealed.summary_rows()
    for side in ("A","B"):
        (INPUTS/side).mkdir(parents=True,exist_ok=True)
    expected={r["slug"] for r in rows}
    for r in rows:
        slug=r["slug"]
        doc=sealed.load_document(slug)
        if doc["list_hash"]!=r["canonical_hash"]:
            raise ValueError(slug+": canonical hash drift")
        for side in ("A","B"):
            dest=INPUTS/side/(slug+".json")
            dest.write_text(encode(sanitized(side,doc)),encoding="utf-8")
    for side in ("A","B"):
        found={p.stem for p in (INPUTS/side).glob("*.json")}
        if found!=expected:
            raise ValueError("unexpected input projection set: "+side)
    print("prepared",len(expected),"side-specific projections per pass; no decisions")


def verify_inputs():
    rows=sealed.summary_rows()
    for r in rows:
        doc=sealed.load_document(r["slug"])
        for side in ("A","B"):
            p=INPUTS/side/(r["slug"]+".json")
            if not p.is_file() or p.read_text(encoding="utf-8")!=encode(sanitized(side,doc)):
                raise ValueError("untrusted or drifted projection: "+str(p))
    print("62x2 sanitized input projections match accepted M5 evidence")


def runner(side):
    if (ROOT/"data/grixis/birthday_m5").exists():
        raise ValueError("full M5 corpus must not be materialized in pass replay runner")
    if (ROOT/"data/grixis/registry.json").exists():
        raise ValueError("full registry must not be materialized in pass replay runner")
    if (INPUTS/("B" if side=="A" else "A")).exists():
        raise ValueError("opposite side's projection exposed")
    if (SEALED/("B" if side=="A" else "A")).exists():
        raise ValueError("opposite side's sealed output exposed")
    folder=INPUTS/side
    actual={p.stem for p in folder.glob("*.json")}
    if len(actual)!=62:
        raise ValueError("sparse input coverage != 62 for side "+side)
    failures=[]
    count=0
    for slug in sorted(actual):
        projection=load(folder/(slug+".json"))
        if projection["slug"]!=slug:
            raise ValueError("projection slug mismatch")
        if side=="A" and ("tests" in projection or "tournament" in projection):
            raise ValueError("performance fields leaked to A")
        if side=="B" and ("candidates" in projection or "blueprint" in projection):
            raise ValueError("commander-first fields leaked to B")
        expected=sealed.pass_output(side,projection)
        sealed_path=SEALED/side/(slug+".json")
        if not sealed_path.exists() or sealed_path.read_text(encoding="utf-8")!=encode(expected):
            failures.append(slug)
        count+=len(expected["pass"]["recommendations"])
    if failures:
        raise ValueError(side+" isolated output != sealed Git record: "+str(failures[:5]))
    print(side,": 62 isolated side-only projections yield byte-identical accepted sealed output;",
          count,"recommendations; no approval authority")
    return count


def main():
    ap=argparse.ArgumentParser()
    mode=ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--prepare",action="store_true")
    mode.add_argument("--verify-inputs",action="store_true")
    mode.add_argument("--replay-a",action="store_true")
    mode.add_argument("--replay-b",action="store_true")
    a=ap.parse_args()
    if a.prepare:prepare()
    if a.verify_inputs:verify_inputs()
    if a.replay_a:runner("A")
    if a.replay_b:runner("B")


if __name__=="__main__":
    main()
