"""Authoring helper (batch 8): append pages, entities and claims to a <arc>.py generator in place.
Usage from Python: patch(file, pages={key: slug}, ents=[(id,type,name)], claims=[tuple], remaining=(old,new)|None).
The generator script remains the source of truth; run it afterwards to regenerate the spec JSON."""
import re
def _lit(x): return repr(x)
def patch(fn, pages=None, ents=None, claims=None, remaining=None):
    s = open(fn, encoding="utf-8").read()
    if pages:
        i = s.index("},\n[")
        lead = "" if s[:i].rstrip().endswith((",", "{")) else ","
        add = lead + ",".join(f'{_lit(k)}:{_lit(v)}' for k, v in pages.items())
        s = s[:i] + add + s[i:]
    if ents:
        i = s.index("],\n[", s.index("},\n["))
        lead = "" if s[:i].rstrip().endswith((",", "[")) else ","
        s = s[:i] + lead + ",".join(_lit(e) for e in ents) + s[i:]
    if claims:
        i = s.rindex("],\n[")
        s = s[:i] + "".join(_lit(tuple(c)) + ",\n" for c in claims) + s[i:]
    if remaining:
        old, new = remaining
        assert old in s, (fn, old)
        s = s.replace(old, new, 1)
    open(fn, "w", encoding="utf-8").write(s)
