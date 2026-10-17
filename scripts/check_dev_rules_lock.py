#!/usr/bin/env python3
"""Verify the frozen historical Comprehensive Rules input used by Step A / frozen M5."""
from __future__ import annotations
import hashlib, json, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
LOCK=ROOT/'data/grixis/dev_rules_lock.json'
CACHE=ROOT/'.cache'


def main():
    d=json.loads(LOCK.read_text(encoding='utf-8'))
    p=CACHE/d['file']
    problems=[]
    if not p.is_file():
        problems.append(f"missing locked rules file: {p.relative_to(ROOT)}")
    else:
        b=p.read_bytes()
        got='sha256:'+hashlib.sha256(b).hexdigest()
        blob=hashlib.sha1(f"blob {len(b)}\0".encode()+b).hexdigest()
        if len(b)!=d['size']:
            problems.append(f"size mismatch {len(b)} != {d['size']}")
        if got!=d['sha256']:
            problems.append(f"sha256 mismatch {got} != {d['sha256']}")
        if blob!=d['recovery_source']['git_blob_sha1']:
            problems.append(f"git blob mismatch {blob} != {d['recovery_source']['git_blob_sha1']}")
        text=b.decode('utf-8-sig',errors='strict')
        if d['upstream_identity']['effective_date_sentence'] not in text[:500]:
            problems.append('effective-date identity missing')
    print(f"dev-rules-lock: {0 if problems else 1} locked rules file(s), {len(problems)} problem(s)")
    for x in problems:
        print('FAIL',x)
    return 1 if problems else 0

if __name__=='__main__':
    sys.exit(main())
