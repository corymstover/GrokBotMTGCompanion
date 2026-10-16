#!/usr/bin/env python3
"""Grixis Commander Blueprints (milestone M2, Bot cycle 50+).

One machine-readable blueprint per deck in data/grixis/blueprints/<slug>.json, schema
data/grixis/schemas/blueprint.schema.json (v2). Every field is a claim with evidence_class, confidence and
evidence refs. Blueprints are written by hand from evidence (source blueprints, approvals, decision notes, M1
interaction reviews, Oracle text, Spellbook, EDHREC); this script never writes judgments. It:
  --scaffold SLUG   prints the facts and the evidence material for one deck (Oracle text, list, source files,
                    source ceiling lines, M1 interaction ids, Spellbook combos, EDHREC, supporting regex features)
  --render          writes grixis/blueprints/README.md and grixis/blueprints/<slug>.md from the JSON
  --check           validate_all step "blueprints": schema, Oracle text vs the Scryfall cache, card refs in the
                    canonical list (or flagged as candidates), evidence on every field and every ref resolvable,
                    evidence-class rules, canonical hash current, M1 ids exist, ceiling disagreement, pages current
  --m2-status       M2 acceptance criteria (grixis/Grixis Authority Model.md#m2), pass/fail per criterion
"""
import atomic_io  # noqa: F401
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import grixis_authority as ga  # noqa: E402

ROOT = ga.ROOT
BP = ga.DATA / "blueprints"
PAGES = ROOT / "grixis" / "blueprints"
ARCH = ga.ARCHIVE
INTER = ROOT / "data" / "grixis_interactions"
CYCLE = 50
REF_KINDS = ("oracle", "source_archive", "interaction", "deck", "edhrec", "spellbook", "cr", "companion", "registry")
CLASS_RULES = {  # field -> allowed evidence classes
    "commanders": {"fact"}, "plan": {"strategic_judgment"}, "commander_role": {"strategic_judgment"},
    "dependency_level": {"strategic_judgment"}, "recursion": {"fact", "strategic_judgment"},
    "requirements": {"strategic_judgment"}, "project_exceptions": {"fact", "approved_decision"},
    "anti_goals": {"strategic_judgment", "approved_decision"}, "thematic_constraints": {"strategic_judgment", "approved_decision", "fact"},
    "supporting_features": {"heuristic"},
    "power.source_ceiling": {"fact"}, "power.grok_estimated_ceiling": {"strategic_judgment"},
    "power.expected_bracket": {"strategic_judgment", "derived_metric"}, "power.edhrec": {"derived_metric", "heuristic"},
    "construction_rules": {"fact"},
}
_R = []


def R():
    if not _R:
        import evaluate_decklist as ev
        _R.append(ev.Resolver())
    return _R[0]


def oracle_of(card):
    import evaluate_decklist as ev
    return ev.oracle(card)


def tline(c):
    return c.get("type_line") or " // ".join(f.get("type_line", "") for f in c.get("card_faces") or [])


def norm(s):
    return re.sub(r"[^a-z0-9]+", "", s.lower())


def summary():
    return ga.summary()


def deck_list(slug):
    """{name: zone} of the canonical project list."""
    out = {}
    for z, o, q, n in ga.list_entries(ga.deck_block_text(slug), R()):
        out[n] = z
    return out


def m1_ids(slug):
    p = INTER / f"{slug}.json"
    if not p.exists():
        return {}
    return {x["id"]: x for x in json.loads(p.read_text(encoding="utf-8")).get("interactions", [])}


def source_files(did):
    # Bot cycle 55: match the registry id and the source id (they differ only for corrected ids, e.g. Norman Osborn)
    keys = {norm(x) for d in (did, ga.source_deck_id(did)) for x in (d, d.replace("__", "_"))}
    out = []
    for p in ARCH.rglob("*"):
        if p.is_file() and p.suffix in (".md", ".json", ".csv", ".txt") and any(k and k in norm(p.name) for k in keys):
            out.append(str(p.relative_to(ARCH)))
    return sorted(out)


CEIL_RX = re.compile(r"(natural (power )?ceiling|power bracket|bracket\s*[1-5]|cedh)", re.I)


def source_ceiling_lines(did, limit=12):
    hits = []
    for rel in source_files(did):
        if rel.endswith(".csv"):
            continue
        for i, l in enumerate((ARCH / rel).read_text(encoding="utf-8", errors="ignore").splitlines(), 1):
            if CEIL_RX.search(l) and re.search(r"[1-5]|cEDH", l):
                hits.append((rel, i, l.strip()[:220]))
    return hits[:limit]


def card_oracle(name):
    c, _ = R().get(name)
    return c


def oracle_sha(text):
    return "sha256:" + hashlib.sha256(text.encode("utf-8")).hexdigest()


def commander_facts(slug):
    out = []
    for n, z in deck_list(slug).items():
        if z == "commander":
            c = card_oracle(n)
            t = oracle_of(c)
            out.append({"name": c["name"], "oracle_id": c["oracle_id"], "oracle_text": t, "oracle_sha256": oracle_sha(t), "type_line": tline(c)})
    return out


def supporting(did, slug):
    import grixis_refine as gr
    lst = gr.lines_of(ga.deck_block_text(slug), R())
    cmds = [c for q, c, z in lst if z == "commander"]
    ctx = gr.Ctx(cmds)
    roles = Counter(r for q, c, z in lst if z == "main" and not gr.is_land(c) for r in gr.roles(c))
    hooked = sorted(c["name"] for q, c, z in lst if z == "main" and not gr.is_land(c) and ctx.hook(c))
    return {"hooks": sorted({h[0] for h in ctx.hooks}), "hooked_cards": len(hooked), "role_counts": dict(sorted(roles.items())),
            "lands": sum(q for q, c, z in lst if z == "main" and gr.is_land(c)), "edhrec_pages": ctx.pages}


# ---------------------------------------------------------------- scaffold
def scaffold(slug):
    summ = summary()
    src = next(d for d, v in summ.items() if v["slug"] == slug)
    did = ga.registry_id(src)  # Bot cycle 55: registry id (corrected); source-keyed files use src
    reg = ga.load_json(ga.REGISTRY)["decks"][did]
    lst = deck_list(slug)
    combos = json.loads((ROOT / "data" / "grixis_combos.json").read_text(encoding="utf-8"))["decks"].get(src, {}).get("combos", [])
    print(json.dumps({"deck_id": did, "slug": slug, "canonical_hash": reg["current_canonical_hash"],
                      "commanders": commander_facts(slug), "registry_ceiling": reg["ceiling"],
                      "compliance": reg["official_commander_compliance"], "exceptions": reg["project_exceptions"],
                      "supporting_features": supporting(did, slug)}, indent=1, ensure_ascii=False))
    print("\n# canonical list (%d lines):" % len(lst))
    print("; ".join(f"{n}{' [' + z + ']' if z != 'main' else ''}" for n, z in sorted(lst.items())))
    print("\n# source files:")
    for f in source_files(did):
        print("  ", f)
    print("\n# source ceiling lines:")
    for f, i, l in source_ceiling_lines(did):
        print(f"   source_archive:{f}#L{i}: {l}")
    print("\n# M1 interactions:")
    for i, x in m1_ids(slug).items():
        print(f"   interaction:{slug}#{i} [{x.get('category')}/{x.get('status')}] {x.get('title')} :: {x.get('short', '')[:160]}")
    print("\n# Spellbook combos:")
    for co in combos:
        print(f"   spellbook:{co['id']} {'INF ' if co.get('infinite') else ''}{' + '.join(co['cards'])}")


# ---------------------------------------------------------------- validation
def ref_problems(ref, did, slug, combo_ids, ids, cr_text):
    kind, _, rest = ref.partition(":")
    if kind not in REF_KINDS:
        return [f"unknown evidence ref kind '{kind}' ({ref})"]
    if kind == "oracle":
        return [] if card_oracle(rest) else [f"oracle ref: card not found ({rest})"]
    if kind == "source_archive":
        path, _, frag = rest.partition("#")
        p = ARCH / path
        if not p.is_file():
            return [f"source_archive ref: no such file {path}"]
        if frag:
            m = re.fullmatch(r"L(\d+)", frag)
            if not m or int(m.group(1)) > len(p.read_text(encoding="utf-8", errors="ignore").splitlines()):
                return [f"source_archive ref: bad line anchor {ref}"]
        return []
    if kind == "interaction":
        s2, _, i = rest.partition("#")
        return [] if i in (ids if s2 == slug else m1_ids(s2)) else [f"interaction ref: no such M1 interaction {rest}"]
    if kind == "deck":
        return [] if (ROOT / "grixis" / "decks" / f"{rest.partition('#')[0]}.md").exists() else [f"deck ref: no page {rest}"]
    if kind == "edhrec":
        return [] if (ROOT / rest.partition("#")[0]).exists() else [f"edhrec ref: no cache file {rest}"]
    if kind == "spellbook":
        return [] if rest in combo_ids else [f"spellbook ref: combo {rest} is not in this deck's Spellbook results"]
    if kind == "cr":
        return [] if re.search(r"^" + re.escape(rest) + r"[ .]", cr_text, re.M) else [f"cr ref: rule {rest} not in the cached CR"]
    if kind in ("companion", "registry"):
        return [] if (ROOT / rest.partition("#")[0]).exists() else [f"{kind} ref: no file {rest}"]
    return []


def claims(bp):
    """Yield (field_path, claim_dict) for every evidence-carrying object."""
    for k, v in bp.items():
        if k == "power":
            for k2, v2 in v.items():
                if isinstance(v2, dict) and "evidence" in v2:
                    yield f"power.{k2}", v2
        elif isinstance(v, dict) and "evidence" in v:
            yield k, v
        elif isinstance(v, list):
            for i, it in enumerate(v):
                if isinstance(it, dict) and "evidence" in it:
                    yield f"{k}[{i}]", it


CARD_FIELDS = (("win_conditions", ("cards", "enablers")), ("engines", ("cards",)), ("packages", ("cards",)),
               ("key_interactions", ("cards",)), ("identity_core", ("card",)), ("tutor_targets", ("target", "via")))


def card_refs(bp):
    for f, keys in CARD_FIELDS:
        for i, it in enumerate(bp[f]):
            for k in keys:
                vals = it[k] if isinstance(it[k], list) else [it[k]]
                for n in vals:
                    yield f"{f}[{i}].{k}", n
    for n in bp["recursion"]["value"]:
        yield "recursion", n


def check_one(path, summ, reg, cr_text):
    p = []
    bp = json.loads(path.read_text(encoding="utf-8"))
    p += [f"schema: {e}" for e in ga.validate_file(bp, "blueprint.schema.json")[:15]]
    if p:
        return p, bp
    did, slug = bp["deck_id"], bp["slug"]
    sid = ga.source_deck_id(did)  # Bot cycle 55: blueprints carry the registry id; source-keyed files use the source id
    if sid not in summ or summ[sid]["slug"] != slug or path.stem != slug or did not in reg["decks"]:
        return [f"deck_id/slug mismatch ({did}, {slug}, file {path.name})"], bp
    e = reg["decks"][did]
    if bp["canonical_hash"] != e["current_canonical_hash"]:
        p.append(f"written against {bp['canonical_hash'][:16]}…, canonical list is now {e['current_canonical_hash'][:16]}… (re-review)")
    # Oracle text is fact: must equal the cache
    want = {c["name"]: c for c in commander_facts(slug)}
    got = {c["name"]: c for c in bp["commanders"]["value"]}
    if set(want) != set(got):
        p.append(f"commanders {sorted(got)} ≠ canonical list commanders {sorted(want)}")
    for n, c in got.items():
        w = want.get(n)
        if w and (c["oracle_text"] != w["oracle_text"] or c["oracle_sha256"] != w["oracle_sha256"] or c["oracle_id"] != w["oracle_id"] or c["type_line"] != w["type_line"]):
            p.append(f"{n}: Oracle text/type/sha differs from the Scryfall cache (oracle_change: re-review)")
    # evidence on every field, refs resolve, class rules
    combos = json.loads((ROOT / "data" / "grixis_combos.json").read_text(encoding="utf-8"))["decks"].get(sid, {}).get("combos", [])
    combo_ids = {c["id"] for c in combos}
    ids = m1_ids(slug)
    for fp, cl in claims(bp):
        base = re.sub(r"\[\d+\]$", "", fp)
        allowed = CLASS_RULES.get(base)
        if allowed and cl["evidence_class"] not in allowed:
            p.append(f"{fp}: evidence_class {cl['evidence_class']} not allowed (want {sorted(allowed)})")
        if cl["confidence"] in ("blocked",) and base in ("plan", "commander_role", "power.grok_estimated_ceiling"):
            p.append(f"{fp}: blocked confidence on a core field")
        for r in cl["evidence"]:
            p += [f"{fp}: {x}" for x in ref_problems(r, did, slug, combo_ids, ids, cr_text)]
    for r in bp["provenance"]["seeded_from"]:
        p += [f"provenance: {x}" for x in ref_problems(r, did, slug, combo_ids, ids, cr_text)]
    cmd_names = set(want)
    if not all(r.startswith("oracle:") for r in bp["commanders"]["evidence"]) or bp["commanders"]["confidence"] != "verified":
        p.append("commanders: Oracle facts must cite oracle: refs with confidence verified")
    # card refs: in the canonical list, or a declared candidate (not in the list, resolvable, legal, in identity)
    lst = deck_list(slug)
    ci = set().union(*(set(card_oracle(n).get("color_identity", [])) for n in cmd_names)) if cmd_names else set()
    for fp, n in card_refs(bp):
        if n not in lst:
            p.append(f"{fp}: {n} is not in the canonical list (declare it as a package candidate instead)")
    for i, pk in enumerate(bp["packages"]):
        if len(pk["cards"]) < pk["min_count"] and pk["required"]:
            p.append(f"packages[{i}] {pk['id']}: required min_count {pk['min_count']} but the list has {len(pk['cards'])} (record the gap as a failure mode or lower it)")
        for n in pk["candidates"]:
            c = card_oracle(n)
            if not c or c["name"] != n:
                p.append(f"packages[{i}].candidates: {n} does not resolve exactly")
            elif n in lst:
                p.append(f"packages[{i}].candidates: {n} is already in the list")
            elif c.get("legalities", {}).get("commander") != "legal" or not set(c.get("color_identity", [])) <= ci:
                p.append(f"packages[{i}].candidates: {n} is not Commander-legal inside the color identity")
    for i, k in enumerate(bp["key_interactions"]):
        for m in k["m1_refs"]:
            if m not in ids:
                p.append(f"key_interactions[{i}]: M1 id {m} not found in data/grixis_interactions/{slug}.json")
    # ceilings: resolved stays null; disagreement consistent with the registry's source ceiling
    src = bp["power"]["source_ceiling"]["value"]["value"]
    rsc = e["ceiling"]["source_ceiling"]
    reff = rsc["value"] if rsc["value"] is not None else (rsc.get("recovered") or {}).get("value")
    if src != reff:
        p.append(f"power.source_ceiling {src} ≠ registry source ceiling {reff} (run grixis_authority.py --build)")
    if rsc["value"] is None and src is not None and not any(r.startswith("source_archive:") and "#L" in r for r in bp["power"]["source_ceiling"]["evidence"]):
        p.append("power.source_ceiling: a recovered source ceiling must cite source_archive:<file>#L<line>")
    g = bp["power"]["grok_estimated_ceiling"]["value"]["value"]
    want_dis = None if src is None else src != g
    if bp["power"]["disagreement"] != want_dis:
        p.append(f"power.disagreement must be {want_dis} (source {src}, grok {g})")
    fl = e["ceiling"]["bracket_floor"]["value"]
    if bp["power"]["expected_bracket"]["value"]["floor"] != fl:
        p.append(f"power.expected_bracket.floor {bp['power']['expected_bracket']['value']['floor']} ≠ registry bracket floor {fl}")
    if int(bp["power"]["expected_bracket"]["value"]["value"]) < fl:
        p.append("power.expected_bracket below the computed floor")
    # project exceptions must match the registry
    exc = sorted(x["card"] for x in json.loads(ga.EXCEPTIONS.read_text(encoding="utf-8"))["exceptions"]
                 if x["deck_id"] == sid and x["project_authorization_status"] == "AUTHORIZED_EXCEPTION")
    if sorted(bp["project_exceptions"]["value"]) != exc:
        p.append(f"project_exceptions {bp['project_exceptions']['value']} ≠ exception registry {exc}")
    # boilerplate lint: no repeated reason strings
    whys = Counter(x["why"] for x in bp["identity_core"])
    p += [f"identity_core: boilerplate reason repeated {k}× ('{w[:50]}…')" for w, k in whys.items() if k > 1]
    if bp["status"] == "cory_reviewed" and bp["provenance"]["reviewed_by"] not in set(reg["human_approvers"]):
        p.append("status cory_reviewed needs provenance.reviewed_by = a human approver")
    if bp["status"] != "cory_reviewed" and bp["provenance"]["reviewed_by"]:
        p.append("reviewed_by set but status is not cory_reviewed")
    p += mv_problems(bp, cmc_lookup())
    return p, bp


# ---------------------------------------------------------------- Bot cycle 62: mana-value claims are facts
# Root cause of the Thraximundar error (cycle 62, Cory t49u): a "mana value 6" claim was tagged fact/high citing
# oracle:Thraximundar, but nothing compared the number with the Scryfall cache (cmc 7). Every N-mana / N-drop /
# mana value N / MV N claim about a named card (or the commander) is now checked against the cached cmc.
_NUMW = {w: i for i, w in enumerate("zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen".split())}
_N = r"(?:\d+|" + "|".join(_NUMW) + r")"
_RANGE = re.compile(r"\b" + _N + r"-?\s*(?:to|–|—)\s*-?" + _N + r"[- ](?:mana|drop)s?\b", re.I)
_PHRASE = re.compile(r"\b(?P<n>" + _N + r")[- ](?P<k>mana|drop)\b(?![- ](?:value|cost|abilit|activat|tap\b))", re.I)
_MVN = re.compile(r"\b(?:mana value|MV|CMC)\s+(?P<n>\d+)\b(?!\s*(?:or (?:less|more|greater|fewer)|\+))", re.I)
_CMDR_CTX = re.compile(r"^[^.;:()]{0,40}?\bcommanders?\b", re.I)
_PRONOUN = re.compile(r"\b(?:he|she|him|her|it|engine)(?:'s|’s| is)?\s+(?:a|an)\s+$", re.I)
_COMMANDER_FIELDS = ("honest_note", "failure_modes", "grok_estimated_ceiling", "game_plan", "construction")


_COST_MV = re.compile(r"(?P<cost>(?:\{[^}]+\})+)[^{.;]{0,20}?\b(?:mana value|MV)\s+(?P<n>\d+)\b", re.I)


def cost_mv(cost):
    """Mana value of a printed cost such as {4}{U}{B}{R} (X = 0, {2/W} = 2)."""
    t = 0
    for sym in re.findall(r"\{([^}]+)\}", cost):
        if sym.isdigit():
            t += int(sym)
        elif sym.upper() in ("X", "Y", "Z"):
            continue
        elif "/" in sym and sym.split("/")[0].isdigit():
            t += int(sym.split("/")[0])
        else:
            t += 1
    return float(t)


def _num(t):
    return int(t) if t.isdigit() else _NUMW[t.lower()]


def _strings(o, path=""):
    if isinstance(o, str):
        yield path, o, None
    elif isinstance(o, dict):
        card = o.get("card") if isinstance(o.get("card"), str) else None
        for k, v in o.items():
            if k in ("oracle_text", "evidence", "id", "type_line", "oracle_sha256", "oracle_id", "name", "card"):
                continue
            for x in _strings(v, f"{path}.{k}" if path else k):
                yield x[0], x[1], x[2] or (card if isinstance(v, str) else None)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from _strings(v, f"{path}[{i}]")


def mv_claims(bp, cmc_of):
    """[(field, phrase, subject card, claimed MV, cached cmc)] for every checkable mana-value claim in a blueprint.
    Subjects: the commander ("N-mana … commander", "the/a N-drop" in commander fields, "he's/she's a N-mana …"),
    the entry's own card ("card" + a why/note that starts with the claim), cards named in a following parenthesis
    ("N-mana storm engines (A, B)"), and for "mana value N" / "MV N" the claim's single named card or the card named
    right before it. Ranges ("five- to seven-mana") and thresholds ("MV 3 or less") are not single-card claims."""
    cmdrs = [c["name"] for c in bp["commanders"]["value"]]
    out = []
    for field, text, own in _strings(bp):
        if field.startswith(("commanders", "provenance")):  # Oracle copies; recorded retractions quote the wrong claim
            continue
        for m in _COST_MV.finditer(text):  # a printed cost stated next to its mana value must add up
            out.append((field, m.group(0), f"cost {m['cost']}", int(m["n"]), {f"cost {m['cost']}": cost_mv(m["cost"])}))
        t = _RANGE.sub("RANGE", text)
        top = field.split(".")[0].split("[")[0]
        cmdr_field = top in _COMMANDER_FIELDS or field.startswith("power.grok_estimated_ceiling")
        for m in _PHRASE.finditer(t):
            n, after, before = _num(m["n"]), t[m.end():], t[:m.start()]
            subj = None
            par = re.match(r"^[^.;()]{0,60}?\(([^)]*)\)", after)
            if _CMDR_CTX.match(after):
                subj = cmdrs
            elif own and m.start() == 0:
                subj = [own]
            elif par and [x for x in (y.strip() for y in par[1].split(",")) if cmc_of(x) is not None]:
                subj = [x for x in (y.strip() for y in par[1].split(",")) if cmc_of(x) is not None]
                subj = [[x] for x in subj]  # each listed card must match
            elif cmdr_field and m["k"].lower() == "drop" and re.search(r"\b(?:the|a)\s+$", before, re.I) and not re.match(r"^s?\s+[A-Z]", after):
                subj = cmdrs
            elif _PRONOUN.search(before):
                subj = cmdrs
            if subj is None:
                continue
            groups = subj if subj and isinstance(subj[0], list) else [subj]
            for g in groups:
                vals = {x: cmc_of(x) for x in g}
                out.append((field, m.group(0), " / ".join(g), n, vals))
        for m in _MVN.finditer(t):
            n = int(m["n"])
            names = [x for x in re.findall(r"[A-Z][\w',.\- ]+?(?=\s+(?:is|has|keeps?|at)\b|\s*\()", t[:m.start()]) if cmc_of(x.strip()) is not None]
            subj = [names[-1].strip()] if names else None
            if subj is None and own and m.start() == 0:
                subj = [own]
            if subj is None:
                continue
            out.append((field, m.group(0), " / ".join(subj), n, {x: cmc_of(x) for x in subj}))
    # claims with a cards list: "mana value N" must match one of the listed cards
    for fp, cl in claims(bp):
        for key in ("summary", "description", "why", "note"):
            txt = cl.get(key)
            if not isinstance(txt, str) or not isinstance(cl.get("cards"), list):
                continue
            for m in _MVN.finditer(txt):
                if any(f == f"{fp}.{key}" and ph == m.group(0) for f, ph, *_ in out):
                    continue
                out.append((f"{fp}.{key}", m.group(0), " / ".join(cl["cards"]), int(m["n"]), {x: cmc_of(x) for x in cl["cards"]}))
    return out


def mv_problems(bp, cmc_of):
    p = []
    for field, ph, subj, n, vals in mv_claims(bp, cmc_of):
        known = {k: v for k, v in vals.items() if v is not None}
        if known and n not in {int(v) for v in known.values()}:
            p.append(f"{field}: '{ph}' claims mana value {n} for {subj}, Scryfall cache cmc is "
                     + ", ".join(f"{k} {int(v)}" for k, v in known.items()) + " (fact claims must match the cache)")
    return p


def cmc_lookup():
    def f(name):
        c, fuzzy = R().get(name)
        return None if c is None or fuzzy or c.get("cmc") is None else c["cmc"]
    return f


def load_all():
    return {p.stem: json.loads(p.read_text(encoding="utf-8")) for p in sorted(BP.glob("*.json"))}


def check():
    summ, reg = summary(), ga.load_json(ga.REGISTRY)
    cr_text = sorted((ROOT / ".cache").glob("MagicCompRules-*.txt"))[-1].read_text(encoding="utf-8", errors="ignore")
    probs, bps = [], {}
    for path in sorted(BP.glob("*.json")):
        p, bp = check_one(path, summ, reg, cr_text)
        probs += [f"{path.name}: {x}" for x in p]
        bps[path.stem] = bp
        e = reg["decks"].get(bp.get("deck_id"), {})
        if e and e.get("blueprint_version") != bp.get("version"):
            probs.append(f"{path.name}: registry blueprint_version {e.get('blueprint_version')} ≠ {bp.get('version')} (run grixis_authority.py --build)")
    for p_, t in render_files(bps, summ, reg).items():
        if not p_.exists() or p_.read_text(encoding="utf-8") != t:
            probs.append(f"{p_.relative_to(ROOT)} is stale (run scripts/grixis_blueprints.py --render)")
    for p_ in PAGES.glob("*.md"):
        if p_.name != "README.md" and p_.stem not in bps:
            probs.append(f"{p_.relative_to(ROOT)} has no blueprint JSON")
    return probs, bps


# ---------------------------------------------------------------- M2 acceptance
def m2_status(bps=None, reg=None):
    bps = bps if bps is not None else load_all()
    reg = reg or ga.load_json(ga.REGISTRY)
    n = len(bps)
    complete = [s for s, b in bps.items() if len(b["identity_core"]) >= 3 and b["anti_goals"]["value"] and any(p["required"] and p["min_count"] > 0 for p in b["packages"])
                and b["win_conditions"] and len(b["failure_modes"]) >= 2 and b["construction_rules"] and b["tutor_targets"] is not None]
    est = [s for s, b in bps.items() if b["power"]["grok_estimated_ceiling"]["evidence"]]
    flags = [s for s, b in bps.items() if b["power"]["disagreement"] is not None or b["power"]["source_ceiling"]["value"]["value"] is None]
    rev = [s for s, b in bps.items() if b["status"] == "cory_reviewed"]
    ms = reg["program"]["milestones"]["M2"]
    crit = [("62 blueprints validate against blueprint.schema.json and --check", n == 62, f"{n}/62 written"),
            ("each names identity core (≥3), anti-goals, required packages with min counts, win conditions, failure modes (≥2), tutor targets, construction rules", len(complete) == 62, f"{len(complete)}/62 complete"),
            ("each has grok_estimated_ceiling with evidence and a disagreement flag where it differs from the source", len(est) == 62 and len(flags) == 62, f"{len(est)}/62 estimated"),
            ("Cory has reviewed the sample he chooses (status cory_reviewed)", bool(rev), f"{len(rev)} reviewed"),
            ("Cory accepted M2 (registry program.milestones.M2)", ms.get("status") == "accepted" and bool(ms.get("accepted_by")), ms.get("status"))]
    return crit


# ---------------------------------------------------------------- rendering
def lab(cl):
    return f"*{cl['evidence_class']} · {cl['confidence']}*"


_ANCH = {}


def m1_anchor(slug, iid):
    """Anchor of an M1 interaction heading ('### <id>: <title>') on grixis/interactions/<slug>.md, as check_links computes it."""
    if slug not in _ANCH:
        from check_links import anchor
        p = ROOT / "grixis" / "interactions" / f"{slug}.md"
        _ANCH[slug] = {}
        if p.exists():
            for m in re.finditer(r"^#{2,6} ([a-z0-9]+-\d+): .*$", p.read_text(encoding="utf-8"), re.M):
                _ANCH[slug].setdefault(m.group(1), anchor(m.group(0).lstrip("#").strip()))
    return _ANCH[slug].get(iid)


def refs(cl):
    out = []
    for r in cl["evidence"]:
        k, _, rest = r.partition(":")
        if k == "source_archive":
            path, _, frag = rest.partition("#")
            out.append(f"[{Path(path).name}{'#' + frag if frag else ''}](../source-archive/grixis-commander-encyclopediaGPT/{path.replace(' ', '%20')})")
        elif k == "interaction":
            s2, _, i = rest.partition("#")
            a = m1_anchor(s2, i)
            out.append(f"[{i}](../interactions/{s2}.md#{a})" if a else f"`{i}`")
        elif k == "deck":
            s2, _, a = rest.partition("#")
            out.append(f"[deck page](../decks/{s2}.md{'#' + a if a else ''})")
        else:
            out.append(f"`{r}`")
    return " · ".join(out)


def page(bp, summ, reg):
    s, did = bp["slug"], bp["deck_id"]
    e = reg["decks"][did]
    pw = bp["power"]
    t = " + ".join(c["name"] for c in bp["commanders"]["value"])
    L = [f"# Blueprint — {t}", "",
         f"> **Commander Blueprint v{bp['version']}** ({bp['status']}, Bot cycle {bp['cycle']}, {bp['date']}) for the canonical project list "
         f"([deck page](../decks/{s}.md), state `{e['state']}`, list `{bp['canonical_hash'][:20]}…`). Machine-readable source: "
         f"[`data/grixis/blueprints/{s}.json`](../../data/grixis/blueprints/{s}.json). Every claim carries its evidence class and confidence "
         "([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Not reviewed by Cory unless the status says so.", ""]
    L += ["## Commander (Oracle, fact)", ""]
    for c in bp["commanders"]["value"]:
        L += [f"**{c['name']}** — {c['type_line']}", "", "> " + c["oracle_text"].replace("\n", "  \n> "), ""]
    cr = bp["commander_role"]
    L += ["## Plan and commander role", "", f"- **Primary plan:** {bp['plan']['value']['primary']} {lab(bp['plan'])}",
          f"- **Secondary:** {bp['plan']['value']['secondary'] or '—'}", f"  - Evidence: {refs(bp['plan'])}",
          f"- **Commander role: {cr['value']['level']}.** {cr['value']['advances_plan']} {lab(cr)}"]
    if cr["value"]["honest_note"]:
        L.append(f"- ⚠️ **Honest note:** {cr['value']['honest_note']}")
    L += [f"  - Evidence: {refs(cr)}", f"- **Dependency level:** {bp['dependency_level']['value']} {lab(bp['dependency_level'])} — {refs(bp['dependency_level'])}", ""]
    src, g, ex = pw["source_ceiling"], pw["grok_estimated_ceiling"], pw["expected_bracket"]
    L += ["## Power", "", "| Field | Value | Class | Evidence |", "|---|---|---|---|",
          f"| Source ceiling | {src['value']['value'] or '— (none stated)'} {('(' + src['value']['label'] + ')') if src['value']['label'] else ''} | {lab(src)} | {refs(src)} |",
          f"| GrokBot estimated ceiling | {g['value']['value']} ({g['value']['label']}) | {lab(g)} | {refs(g)} |",
          f"| Expected bracket (list as built) | {ex['value']['value']} (computed floor {ex['value']['floor']}) | {lab(ex)} | {refs(ex)} |",
          "| Resolved ceiling | — (only Cory resolves) | | |",
          f"| Disagreement | {'⚠️ **yes**: flagged for Cory, not applied' if pw['disagreement'] else 'no' if pw['disagreement'] is False else '— (no source ceiling)'} | | |", ""]
    if pw["edhrec"]:
        L += [f"- EDHREC: `{json.dumps(pw['edhrec']['value'], ensure_ascii=False)}` {lab(pw['edhrec'])} — {refs(pw['edhrec'])}", ""]
    L += ["## Win conditions", ""]
    for w in bp["win_conditions"]:
        L.append(f"- **{w['id']}** ({w['kind']}): {w['description']} Cards: {', '.join(w['cards'])}." + (f" Enablers: {', '.join(w['enablers'])}." if w["enablers"] else "") + f" {lab(w)} — {refs(w)}")
    L += ["", "## Engines", ""] + [f"- **{x['id']}:** {', '.join(x['cards'])}. Online when: {x['online_condition']} {lab(x)} — {refs(x)}" for x in bp["engines"]]
    L += ["", "## Packages", "", "| Package | Required | Min | Role | In list | Candidates (not in list) | Class | Evidence |", "|---|---|---|---|---|---|---|---|"]
    for x in bp["packages"]:
        L.append(f"| `{x['id']}` | {'yes' if x['required'] else 'optional'} | {x['min_count']} | {x['role']} | {len(x['cards'])}: {', '.join(x['cards'])} | {', '.join(x['candidates']) or '—'} | {lab(x)} | {refs(x)} |")
    L += ["", "## Key interactions", ""] + [f"- **{x['id']}:** {x['summary']} ({', '.join(x['cards'])}) {lab(x)} — {refs(x)}" for x in bp["key_interactions"]]
    L += ["", "## Tutors and recursion", ""] + [f"- Tutor target **{x['target']}** via {', '.join(x['via'])} {lab(x)} — {refs(x)}" for x in bp["tutor_targets"]]
    L += [f"- Recursion: {', '.join(bp['recursion']['value']) or '—'} {lab(bp['recursion'])} — {refs(bp['recursion'])}", ""]
    rq = bp["requirements"]
    L += ["## Requirements", "", f"- **Interaction:** {rq['value']['interaction']}", f"- **Protection:** {rq['value']['protection']}", f"- **Mana:** {rq['value']['mana']}", f"- {lab(rq)} — {refs(rq)}", ""]
    L += ["## Failure modes", ""] + [f"- **{x['id']}:** {x['description']} Mitigations: {'; '.join(x['mitigations']) or '—'}. {lab(x)} — {refs(x)}" for x in bp["failure_modes"]]
    L += ["", "## Identity core", ""] + [f"- **{x['card']}:** {x['why']} {lab(x)} — {refs(x)}" for x in bp["identity_core"]]
    L += ["", "## Anti-goals and thematic constraints", ""] + [f"- ✗ {a}" for a in bp["anti_goals"]["value"]] + [f"  - {lab(bp['anti_goals'])} — {refs(bp['anti_goals'])}"]
    L += [f"- Theme: {t_}" for t_ in bp["thematic_constraints"]["value"]] + ([f"  - {lab(bp['thematic_constraints'])} — {refs(bp['thematic_constraints'])}"] if bp["thematic_constraints"]["value"] else [])
    L += ["", "## Project exceptions", "", (", ".join(bp["project_exceptions"]["value"]) + " (🚩 NOT Commander-legal; registry `data/grixis/exceptions.json`)") if bp["project_exceptions"]["value"] else "None.", ""]
    L += ["## Construction-relevant rules", ""] + [f"- **{x['rule']}:** {x['note']} {lab(x)} — {refs(x)}" for x in bp["construction_rules"]]
    sf = bp["supporting_features"]
    L += ["", "## Supporting features (heuristic, not identity)", "", f"- `{json.dumps(sf['value'], ensure_ascii=False)}` {lab(sf)}", "",
          "## Provenance", "", f"- Seeded from: {refs({'evidence': bp['provenance']['seeded_from']})}", f"- Reviewed by: {bp['provenance']['reviewed_by'] or '— (not yet reviewed by Cory)'}"]
    return "\n".join(L) + "\n"


def render_files(bps, summ, reg):
    files = {PAGES / f"{s}.md": page(b, summ, reg) for s, b in bps.items()}
    nosrc = [d for d, e in reg["decks"].items() if e["ceiling"]["source_ceiling"]["value"] is None]
    crit = m2_status(bps, reg)
    L = ["# Grixis Commander Blueprints", "",
         "> **Milestone M2, Bot cycle 50+.** One machine-readable blueprint per deck (brief §3): Oracle text, plan, the commander's real role, win conditions, engines, "
         "packages, key interactions (linked to the [M1 interaction reviews](../interactions/README.md)), tutors, recursion, requirements, failure modes, dependency level, "
         "ceilings (source vs GrokBot estimate; only Cory resolves), identity core, anti-goals, thematic constraints and construction rules. Every field carries an evidence class "
         "and confidence ([Grixis Authority Model](../Grixis%20Authority%20Model.md#evidence-classes)). Data: `data/grixis/blueprints/`; schema: "
         "`data/grixis/schemas/blueprint.schema.json`; tool and `validate_all` step `blueprints`: `scripts/grixis_blueprints.py`.", "",
         "## Contents", "- [Status](#status)", "- [Blueprints](#blueprints)", "- [Ceiling disagreements](#ceiling-disagreements)", "- [Method](#method)", "",
         "## Status", "", f"**{len(bps)}/62 blueprints written.** M2 acceptance criteria ([definition](../Grixis%20Authority%20Model.md#m2)):", ""]
    L += [f"- {'✅' if ok else '⏳'} {c} — {d}" for c, ok, d in crit]
    L += ["", "## Blueprints", "", "| Deck | Commander role | Dependency | Source ceiling | GrokBot estimate | Expected bracket | Disagreement | Version / status |", "|---|---|---|---|---|---|---|---|"]
    for s, b in sorted(bps.items()):
        pw = b["power"]
        L.append(f"| [{' + '.join(c['name'] for c in b['commanders']['value'])}]({s}.md) | {b['commander_role']['value']['level']} | {b['dependency_level']['value']} | "
                 f"{(pw['source_ceiling']['value']['value'] or '—') + (' (recovered)' if pw['source_ceiling']['value']['value'] and reg['decks'][b['deck_id']]['ceiling']['source_ceiling']['value'] is None else '')} | {pw['grok_estimated_ceiling']['value']['value']} | {pw['expected_bracket']['value']['value']} | "
                 f"{'⚠️ yes' if pw['disagreement'] else 'no' if pw['disagreement'] is False else '—'} | v{b['version']} {b['status']} |")
    todo = sorted(v["slug"] for d, v in summ.items() if v["slug"] not in bps)
    L += ["", f"Not written yet ({len(todo)}): " + (", ".join(f"[{t}](../decks/{t}.md)" for t in todo) or "none") + ".", "",
          "## Ceiling disagreements", "", "Flagged for Cory; never applied. Registry: `ceiling.disagreement`.", ""]
    dis = [(s, b) for s, b in sorted(bps.items()) if b["power"]["disagreement"]]
    L += [f"- **[{' + '.join(c['name'] for c in b['commanders']['value'])}]({s}.md):** source {b['power']['source_ceiling']['value']['value']} vs GrokBot {b['power']['grok_estimated_ceiling']['value']['value']}. {b['power']['grok_estimated_ceiling']['value']['label']}" for s, b in dis] or ["- None so far."]
    L += ["", f"**Decks with no source bracket in the registry's parsed claim ({len(nosrc)}):** " + ", ".join(f"`{d}`" for d in nosrc) +
          ". Where a source blueprint or approval states one, the blueprint cites it and `grixis_authority.py --build` records it as *recovered* (the original parse found nothing; nothing is overwritten).", "",
          "## Method", "",
          "- **Facts first:** commander Oracle text, type line and Oracle id are copied from the Scryfall cache and re-checked on every run (a change fails `validate_all` until re-reviewed).",
          "- **Evidence:** the source's blueprints, approvals, decision notes and whole-list audits (archived byte-identical), the M1 interaction reviews, Commander Spellbook combos and EDHREC (cached) are cited per claim. Source claims superseded by current Oracle (e.g. older once-per-turn readings) are not carried over.",
          "- **Regex hooks** from `grixis_refine.py` appear only under *supporting features* (heuristic). They never define identity.",
          "- **Card refs** must be in the canonical project list; anything else must be declared as a package *candidate* (Commander-legal, in identity, not in the list).",
          "- **Honesty:** when the commander is not what makes the deck work, `commander_role` says so (`supporting` / `incidental`) and the ceiling estimate is flagged against the source instead of forced."]
    files[PAGES / "README.md"] = "\n".join(L) + "\n"
    return files


def render():
    summ, reg = summary(), ga.load_json(ga.REGISTRY)
    bps = load_all()
    PAGES.mkdir(parents=True, exist_ok=True)
    for p, t in render_files(bps, summ, reg).items():
        if not p.exists() or p.read_text(encoding="utf-8") != t:
            p.write_text(t, encoding="utf-8")
    print(f"blueprints: rendered {len(bps)} page(s) + README")


def main(argv):
    if "--scaffold" in argv:
        scaffold(argv[argv.index("--scaffold") + 1])
        return 0
    if "--render" in argv:
        render()
    if "--mv-report" in argv:
        f = cmc_lookup()
        for slug, bp in load_all().items():
            for field, ph, subj, n, vals in mv_claims(bp, f):
                ok = n in {int(v) for v in vals.values() if v is not None}
                print(f"{'OK  ' if ok else 'FAIL'} {slug} {field}: '{ph}' → {subj} {vals}")
    if "--m2-status" in argv:
        for c, ok, d in m2_status():
            print(f"{'PASS' if ok else 'OPEN'}  {c} — {d}")
    if "--check" in argv:
        probs, bps = check()
        crit = m2_status(bps)
        dis = sum(1 for b in bps.values() if b["power"]["disagreement"])
        print(f"blueprints: {len(bps)}/62 written; {dis} ceiling disagreement(s) flagged; M2 criteria {sum(1 for _, ok, _ in crit if ok)}/{len(crit)} met; {len(probs)} problem(s)")
        for x in probs[:40]:
            print("  - " + x)
        return 1 if probs else 0
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
