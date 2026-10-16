#!/usr/bin/env python3
"""Grixis authority layer (Bot cycle 47, milestone M0): one canonical project list per commander, a state machine,
human-approval enforcement, evidence classes, official legality kept apart from project authorization.

Data (data/grixis/; JSON Schemas in data/grixis/schemas/, design in grixis/Grixis Authority Model.md):
  registry.json      canonical authority registry, one entry per deck (state, hashes, ceilings, challengers, triggers)
  exceptions.json    project-exception registry (imported from the source's 8-row CSV, verified and corrected)
  approvals.json     human approval records: the ONLY path to APPROVED / CANONICAL_LOCKED (Cory's explicit sign-off)
  projections.json   derived compliance projections (never canonical, never approved)
Shared library (stdlib only; imported by validate_all, grixis_refine, build_grixis, the tests):
  hashing (logical list hash `lh1:` vs raw file `sha256:`), JSON Schema subset validator, evidence classes,
  state transitions, approval enforcement, legality/authorization labels, disposition / escalation / reconciliation rules.
Usage:
  python3 scripts/grixis_authority.py --build-exceptions   (re)write exceptions.json from the archived source CSV + Scryfall
  python3 scripts/grixis_authority.py --build              (re)write registry.json (human fields are preserved)
  python3 scripts/grixis_authority.py --check              validate_all step "authority" (no writes)
"""
import csv
import datetime as dt
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "grixis"
SCHEMAS = DATA / "schemas"
REGISTRY = DATA / "registry.json"
EXCEPTIONS = DATA / "exceptions.json"
APPROVALS = DATA / "approvals.json"
PROJECTIONS = DATA / "projections.json"
REFINE_V2 = ROOT / "data" / "grixis_refine_v2.json"
ARCHIVE = ROOT / "grixis" / "source-archive" / "grixis-commander-encyclopediaGPT"
SOURCE_REPO = "corymstover/grixis-commander-encyclopediaGPT"
CYCLE = 47
M0_DATE = "2026-10-16"

# ---------------------------------------------------------------- evidence classes (brief §15; ideas from the archived
# grixis_pipeline/epistemic.py: VERIFIED / HIGH_CONFIDENCE / PROVISIONAL / TEST_REQUIRED / BLOCKED)
EVIDENCE_CLASSES = ("fact", "derived_metric", "heuristic", "hypothesis", "test_result", "strategic_judgment", "approved_decision")
CONFIDENCE = ("verified", "high", "moderate", "low", "test_required", "blocked")
SOURCE_CONFIDENCE_MAP = {"VERIFIED": "verified", "HIGH_CONFIDENCE": "high", "PROVISIONAL": "moderate", "TEST_REQUIRED": "test_required", "BLOCKED": "blocked"}
DECISION_CLASSES = {"fact", "test_result", "strategic_judgment", "approved_decision"}  # at least one needed to justify a decision


def decision_support_ok(items):
    """(ok, reasons). Heuristics and derived metrics are diagnostics: alone they never justify a decision.
    Any blocked / test_required item blocks the decision (it must be resolved first)."""
    reasons = []
    if not items:
        return False, ["no evidence"]
    bad = [i.get("id", "?") for i in items if i.get("class") not in EVIDENCE_CLASSES or i.get("confidence") not in CONFIDENCE]
    if bad:
        reasons.append(f"unknown class/confidence: {bad}")
    if not any(i.get("class") in DECISION_CLASSES for i in items):
        reasons.append("only heuristic / derived-metric / hypothesis evidence: diagnostics cannot decide")
    blk = [i.get("id", "?") for i in items if i.get("confidence") in ("blocked", "test_required")]
    if blk:
        reasons.append(f"unresolved evidence (blocked / test_required): {blk}")
    return not reasons, reasons


# ---------------------------------------------------------------- states (brief §18; Cory constraint 8)
STATES = ("SOURCE_BASELINE", "UNDER_REVIEW", "CHALLENGER", "TESTING", "REVIEW_REQUIRED", "APPROVAL_READY",
          "APPROVED", "CANONICAL_LOCKED", "REOPEN_REQUIRED", "PENDING_RELEASE")
INITIAL_STATES = {"SOURCE_BASELINE", "PENDING_RELEASE"}
HUMAN_STATES = {"APPROVED", "CANONICAL_LOCKED"}       # need an explicit approval record from a human approver
GATED_STATES = {"APPROVAL_READY", "APPROVED", "CANONICAL_LOCKED"}  # need M2 + M4 accepted (Cory constraint 6)
TRANSITIONS = {
    "SOURCE_BASELINE": {"UNDER_REVIEW", "PENDING_RELEASE", "REOPEN_REQUIRED"},
    "PENDING_RELEASE": {"SOURCE_BASELINE", "UNDER_REVIEW"},
    "UNDER_REVIEW": {"CHALLENGER", "TESTING", "REVIEW_REQUIRED", "SOURCE_BASELINE"},
    "CHALLENGER": {"TESTING", "REVIEW_REQUIRED", "UNDER_REVIEW"},
    "TESTING": {"REVIEW_REQUIRED", "APPROVAL_READY", "CHALLENGER"},
    "REVIEW_REQUIRED": {"UNDER_REVIEW", "TESTING", "APPROVAL_READY"},
    "APPROVAL_READY": {"APPROVED", "REVIEW_REQUIRED", "UNDER_REVIEW"},
    "APPROVED": {"CANONICAL_LOCKED", "REOPEN_REQUIRED"},
    "CANONICAL_LOCKED": {"REOPEN_REQUIRED"},
    "REOPEN_REQUIRED": {"UNDER_REVIEW"},
}
TRIGGER_KINDS = ("new_card", "oracle_change", "rules_change", "legality_change", "new_exception", "test_failure",
                 "new_interaction", "meta_shift", "audit_error", "user_instruction")


def allowed_transition(a, b):
    return b in TRANSITIONS.get(a, set())


def approval_problems(deck_id, entry, approvals, approvers, milestones):
    """Problems with a deck's state given the human approval records (list of dicts) and program milestones."""
    p = []
    st = entry["state"]
    if st not in STATES:
        return [f"{deck_id}: unknown state {st}"]
    hist = entry.get("state_history") or []
    if not hist or hist[0]["state"] not in INITIAL_STATES:
        p.append(f"{deck_id}: state_history must start at SOURCE_BASELINE or PENDING_RELEASE")
    for a, b in zip(hist, hist[1:]):
        if not allowed_transition(a["state"], b["state"]):
            p.append(f"{deck_id}: illegal transition {a['state']} → {b['state']} ({b.get('date')})")
    if hist and hist[-1]["state"] != st:
        p.append(f"{deck_id}: state {st} is not the last state_history entry ({hist[-1]['state']})")
    if st in GATED_STATES:
        for m in ("M2", "M4"):
            if (milestones.get(m) or {}).get("status") != "accepted" or not (milestones.get(m) or {}).get("accepted_by"):
                p.append(f"{deck_id}: {st} needs milestone {m} accepted (blueprints and dependency graphs mature first)")
    if st == "APPROVAL_READY" and not entry.get("finalization_certificate"):
        p.append(f"{deck_id}: APPROVAL_READY needs a finalization certificate")
    if st in HUMAN_STATES:
        need = {"APPROVED": {"APPROVED", "CANONICAL_LOCKED"}, "CANONICAL_LOCKED": {"CANONICAL_LOCKED"}}[st]
        rec = [r for r in approvals if r.get("deck_id") == deck_id and r.get("decision") in need
               and r.get("list_hash") == entry.get("current_canonical_hash")]
        if not rec:
            p.append(f"{deck_id}: {st} without a human approval record for list {entry.get('current_canonical_hash')}")
        elif not any(r.get("approved_by") in approvers for r in rec):
            p.append(f"{deck_id}: {st} approval record is not by a human approver {sorted(approvers)}")
        ap = entry.get("approval") or {}
        if not ap.get("record_id") or ap.get("record_id") not in {r.get("id") for r in rec}:
            p.append(f"{deck_id}: approval.record_id must name the approval record")
    elif (entry.get("approval") or {}).get("record_id") or (entry.get("approval") or {}).get("by"):
        p.append(f"{deck_id}: approval fields are set but the state is {st}")
    pj = entry.get("official_legal_projection")
    if pj:
        if pj.get("canonical") is not False or pj.get("approval_state") is not None:
            p.append(f"{deck_id}: a derived compliance projection can never be canonical or in an approval state")
        if pj.get("label") != PROJECTION_LABEL:
            p.append(f"{deck_id}: projection label must read '{PROJECTION_LABEL}'")
        if pj.get("hash") == entry.get("current_canonical_hash"):
            p.append(f"{deck_id}: projection hash equals the canonical hash (it would compete for authority)")
        if any(r.get("list_hash") == pj.get("hash") for r in approvals):
            p.append(f"{deck_id}: an approval record names the derived compliance projection; projections are never approved")
    for c in entry.get("challengers", []):
        if any(r.get("list_hash") == c["hash"] and r.get("decision") != "REJECTED" for r in approvals) and c["hash"] != entry.get("current_canonical_hash"):
            p.append(f"{deck_id}: challenger {c['id']} has an approval but was never promoted to canonical (supersedes_hash)")
    ce = entry.get("ceiling") or {}
    rc = ce.get("resolved_ceiling") or {}
    if rc.get("value") is not None and (not rc.get("resolved_by") or rc.get("resolved_by") not in approvers):
        p.append(f"{deck_id}: resolved_ceiling needs resolved_by (a human approver); grok estimates never resolve themselves")
    sc = ce.get("source_ceiling") or {}
    s = sc.get("value") if sc.get("value") is not None else (sc.get("recovered") or {}).get("value")  # Bot cycle 50: recovered claim
    g = (ce.get("grok_estimated_ceiling") or {}).get("value")
    want = None if s is None or g is None else (s != g)
    if ce.get("disagreement") != want:
        p.append(f"{deck_id}: ceiling.disagreement must be {want} (source {s}, grok estimate {g})")
    return p


# ---------------------------------------------------------------- legality vs authorization (brief §13)
PROJECTION_LABEL = "derived compliance projection (not canonical)"
CHALLENGER_LABEL = "GrokBot challenger (unapproved)"
BASELINE_LABEL = "source baseline (canonical project list, SOURCE_BASELINE)"
V1_HEURISTIC_LABEL = "heuristic: no candidate passed v1 gates (not a certificate)"
OFFICIAL_TEXT = {"legal": "Commander-legal", "banned": "banned in Commander", "banned_as_companion": "banned as a companion in Commander (legal in the 99)",
                 "not_legal": "not Commander-legal", "not_legal_until_release": "not Commander-legal yet"}


def legality_label(official, authorization, legal_from=None):
    """Human label. A project exception is never reported as legal."""
    if official == "legal":
        return "Commander-legal"
    base = OFFICIAL_TEXT.get(official, "not Commander-legal")
    if official == "not_legal_until_release" and legal_from:
        base += f" (legal from {legal_from})"
    if authorization == "AUTHORIZED_EXCEPTION":
        return f"🚩 project exception, NOT Commander-legal: {base}"
    if authorization == "AUTHORIZED_FUTURE_RELEASE":
        return "⏳ authorized future release, NOT Commander-legal yet" + (f" (legal from {legal_from})" if legal_from else "")
    return f"❌ {base} (no project authorization)"


def load_json(p, default=None):
    return json.loads(Path(p).read_text(encoding="utf-8")) if Path(p).exists() else default


def exception_index(path=EXCEPTIONS):
    """{(deck_id, card): row} for AUTHORIZED rows only (official_card_rule rows are not exceptions)."""
    d = load_json(path, {"exceptions": []})
    return {(r["deck_id"], r["card"]): r for r in d["exceptions"]
            if r["project_authorization_status"] in ("AUTHORIZED_EXCEPTION", "AUTHORIZED_FUTURE_RELEASE")}


def accepted_hard_issues(deck_id, issues, path=EXCEPTIONS):
    """Split hard issues into (still_failing, accepted_as_project_exception). Only registered, authorized
    (deck, card) pairs on a Commander-legality issue are accepted; identity, size, singleton never are."""
    ix = exception_index(path)
    keep, acc = [], []
    for i in issues:
        r = ix.get((deck_id, i.get("card")))
        if r and r["project_authorization_status"] == "AUTHORIZED_EXCEPTION" and i.get("type") in ("banned", "not Commander-legal"):
            acc.append(i)
        else:
            keep.append(i)
    return keep, acc


# ---------------------------------------------------------------- hashing (brief §19)
HASH_DEFINITION = {
    "logical": "lh1 = sha256 over UTF-8 lines '<zone>|<oracle_id>|<qty>' (zone: commander / companion / main; one line per distinct card after summing quantities), sorted, each followed by \\n. Independent of file layout, line order, printings, role tags and spelling variants; changes when any card, quantity or zone changes.",
    "raw": "sha256 = SHA-256 of the file bytes exactly as stored. Changes with any byte (tags, order, set codes, whitespace).",
    "note": "The source repo mixed the two: two decks' recorded approved_list_sha256 values match no file because they are logical/list digests (source exports/archidekt_2026-10-15/README.txt). The companion stores both, under different prefixes, and only lh1 is authoritative.",
}


def logical_hash(entries):
    """entries: iterable of (zone, oracle_id, qty). Returns 'lh1:<hex>'."""
    tot = {}
    for zone, oid, qty in entries:
        if zone not in ("commander", "companion", "main"):
            raise ValueError(f"bad zone {zone}")
        if not oid:
            raise ValueError("unresolved card: no oracle_id")
        tot[(zone, oid)] = tot.get((zone, oid), 0) + int(qty)
    text = "".join(f"{z}|{o}|{q}\n" for (z, o), q in sorted(tot.items()))
    return "lh1:" + hashlib.sha256(text.encode("utf-8")).hexdigest()


def raw_hash(data):
    return "sha256:" + hashlib.sha256(data if isinstance(data, bytes) else data.encode("utf-8")).hexdigest()


def list_entries(text, R):
    """Parse an import list with evaluate_decklist and resolve to (zone, oracle_id, qty, name)."""
    import evaluate_decklist as ev
    out = []
    for e in ev.parse(text):
        if e.get("bad"):
            raise ValueError(f"unparseable line: {e['raw']}")
        c, _ = R.get(e["name"])
        if not c:
            raise ValueError(f"unresolved card: {e['name']}")
        t = e["tags"].lower()
        out.append(("commander" if "commander" in t else "companion" if "companion" in t else "main", c["oracle_id"], e["qty"], c["name"]))
    return out


def text_hash(text, R):
    return logical_hash((z, o, q) for z, o, q, _ in list_entries(text, R))


# ---------------------------------------------------------------- JSON Schema subset validator (stdlib; the test suite
# cross-checks it against the `jsonschema` package when that is installed)
_SCHEMA_CACHE = {}


def load_schema(name):
    if name not in _SCHEMA_CACHE:
        _SCHEMA_CACHE[name] = json.loads((SCHEMAS / name).read_text(encoding="utf-8"))
    return _SCHEMA_CACHE[name]


def _resolve(ref, cur_file):
    f, _, frag = ref.partition("#")
    fname = f or cur_file
    node = load_schema(fname)
    for part in [x for x in frag.split("/") if x]:
        node = node[part]
    return node, fname


TYPES = {"object": dict, "array": list, "string": str, "boolean": bool, "null": type(None)}


def _is_type(v, t):
    if t == "integer":
        return isinstance(v, int) and not isinstance(v, bool)
    if t == "number":
        return isinstance(v, (int, float)) and not isinstance(v, bool)
    return isinstance(v, TYPES[t])


def validate(inst, schema, cur_file="common.schema.json", path="$"):
    """Return a list of error strings (empty = valid). Supports the keywords used in data/grixis/schemas/."""
    errs = []
    if "$ref" in schema:
        sub, f = _resolve(schema["$ref"], cur_file)
        errs += validate(inst, sub, f, path)
    if "type" in schema:
        ts = schema["type"] if isinstance(schema["type"], list) else [schema["type"]]
        if not any(_is_type(inst, t) for t in ts):
            return errs + [f"{path}: expected {'/'.join(ts)}, got {type(inst).__name__}"]
    if "const" in schema and inst != schema["const"]:
        errs.append(f"{path}: must be {schema['const']!r}")
    if "enum" in schema and inst not in schema["enum"]:
        errs.append(f"{path}: {inst!r} not in {schema['enum']}")
    if isinstance(inst, str):
        if "pattern" in schema and not re.search(schema["pattern"], inst):
            errs.append(f"{path}: {inst!r} does not match {schema['pattern']}")
        if len(inst) < schema.get("minLength", 0):
            errs.append(f"{path}: shorter than {schema['minLength']}")
    if _is_type(inst, "number"):
        if "minimum" in schema and inst < schema["minimum"]:
            errs.append(f"{path}: below minimum {schema['minimum']}")
        if "maximum" in schema and inst > schema["maximum"]:
            errs.append(f"{path}: above maximum {schema['maximum']}")
    if isinstance(inst, dict):
        for k in schema.get("required", []):
            if k not in inst:
                errs.append(f"{path}: missing required '{k}'")
        props = schema.get("properties", {})
        ap = schema.get("additionalProperties", True)
        for k, v in inst.items():
            if k in props:
                errs += validate(v, props[k], cur_file, f"{path}.{k}")
            elif ap is False:
                errs.append(f"{path}: unexpected property '{k}'")
            elif isinstance(ap, dict):
                errs += validate(v, ap, cur_file, f"{path}.{k}")
    if isinstance(inst, list):
        if len(inst) < schema.get("minItems", 0):
            errs.append(f"{path}: fewer than {schema['minItems']} items")
        if "maxItems" in schema and len(inst) > schema["maxItems"]:
            errs.append(f"{path}: more than {schema['maxItems']} items")
        if "items" in schema:
            for i, v in enumerate(inst):
                errs += validate(v, schema["items"], cur_file, f"{path}[{i}]")
    if "anyOf" in schema:
        if not any(not validate(inst, s, cur_file, path) for s in schema["anyOf"]):
            errs.append(f"{path}: matches none of anyOf")
    if "oneOf" in schema:
        if sum(1 for s in schema["oneOf"] if not validate(inst, s, cur_file, path)) != 1:
            errs.append(f"{path}: must match exactly one of oneOf")
    for s in schema.get("allOf", []):
        errs += validate(inst, s, cur_file, path)
    return errs


def validate_file(doc, schema_name):
    return validate(doc, load_schema(schema_name), schema_name)


# ---------------------------------------------------------------- review rules encoded for M2+ (Cory constraints 2, 3, 7)
def disposition_status(slot):
    """'complete' only when the card was evaluated against the blueprint, the dependency graph, plausible alternatives
    and redundancy, with a role/package; a script classification alone is 'provisional'."""
    ok = (slot.get("blueprint_refs") and slot.get("graph_refs") and slot.get("alternatives")
          and slot.get("redundancy") is not None and (slot.get("roles") or slot.get("packages")) and (slot.get("reason") or "").strip())
    return "complete" if ok else "provisional"


def audit_problems(audit):
    p = []
    for s in audit.get("slots", []):
        want = disposition_status(s)
        if s.get("review_status") == "complete" and want != "complete":
            p.append(f"{audit.get('deck_id')}: {s.get('card')} marked complete without blueprint/graph/alternative refs and redundancy")
    return p


ESCALATION_REASONS = ("dependency_analysis", "new_card", "unusual_oracle_interaction", "package_gap", "reviewer_evidence", "rank_miss_suspected")


def candidate_problems(c):
    p = []
    e = c.get("escalation") or {}
    if e.get("escalated"):
        if not e.get("reasons") or any(r not in ESCALATION_REASONS for r in e["reasons"]):
            p.append(f"{c.get('card')}: escalation needs at least one known reason")
        if not e.get("evidence_refs"):
            p.append(f"{c.get('card')}: escalation needs evidence refs")
        if not c.get("full_review"):
            p.append(f"{c.get('card')}: an escalated candidate must get full review regardless of rank")
    return p


PERF_INPUTS = {"simulator", "goldfish", "stress", "edhrec_inclusion", "edhrec_lift", "edhrec_rank", "tournament", "mana_efficiency", "hypergeometric"}
CMDR_INPUTS = {"blueprint", "oracle_hooks", "packages", "dependency_graph", "identity_core", "anti_goals", "interaction_review"}


def check_reconciliation(pass_a, pass_b):
    """Independent first passes: different optimizer, objective family and formula; neither informed by the other;
    commander-first objective inputs exclude performance metrics and vice versa. Returns a list of problems."""
    p = []
    if {pass_a["optimizer"], pass_b["optimizer"]} != {"commander_first", "performance"}:
        p.append("need one commander_first and one performance pass")
    fa, fb = pass_a["objective_function"], pass_b["objective_function"]
    if fa["family"] == fb["family"]:
        p.append("both passes use the same objective family")
    if fa["formula_sha256"] == fb["formula_sha256"]:
        p.append("same objective formula: two weightings of one score are not independent passes")
    for x, y in ((pass_a, pass_b), (pass_b, pass_a)):
        if y["pass_id"] in x.get("informed_by", []):
            p.append(f"{x['pass_id']} was informed by {y['pass_id']}: first passes must be independent")
    for ps in (pass_a, pass_b):
        ins = set(ps["objective_function"]["inputs"])
        if ps["optimizer"] == "commander_first" and ins & PERF_INPUTS:
            p.append(f"commander-first objective uses performance inputs {sorted(ins & PERF_INPUTS)}")
        if ps["optimizer"] == "performance" and ins & CMDR_INPUTS:
            p.append(f"performance objective uses commander-first inputs {sorted(ins & CMDR_INPUTS)}")
    return p


# ---------------------------------------------------------------- build helpers
# Bot cycle 55: registry deck-id corrections. The source keys some decks by a stale tracker id; the registry uses the
# corrected id and keeps the source id plus a provenance note. Every source-keyed lookup (data/grixis_summary.json,
# grixis_combos.json, current_deck_overrides.json, pending, plans, projections, exceptions) still uses the source id.
DECK_ID_CORRECTIONS = {
    "Goben__Gene_Splice_Savant": {
        "deck_id": "Norman_Osborn_Green_Goblin",
        "corrected_cycle": 55, "corrected_date": "2026-10-16",
        "note": ("The source keys this deck by the stale tracker id Goben__Gene_Splice_Savant (deck #21), already so in the frozen "
                 "FINAL baseline. The list, approval record and every refinement artifact are Norman Osborn // Green Goblin "
                 "(files Norman_Osborn_Green_Goblin_*), so the registry uses the corrected id. The source id is kept as "
                 "source_deck_id; nothing in the source archive was changed."),
        "evidence": ["source_archive:state/current_deck_overrides.json#Goben__Gene_Splice_Savant",
                     "source_archive:refinement/approvals/Norman_Osborn_Green_Goblin_Approved_2026-10-15.md",
                     "companion:grixis/Grixis Corrections.md#L178"]},
}
_SOURCE_OF = {v["deck_id"]: k for k, v in DECK_ID_CORRECTIONS.items()}


def registry_id(source_deck_id):
    """Registry deck id for a source deck id (identity unless corrected)."""
    return DECK_ID_CORRECTIONS.get(source_deck_id, {}).get("deck_id", source_deck_id)


def source_deck_id(deck_id):
    """Source deck id for a registry deck id (identity unless corrected)."""
    return _SOURCE_OF.get(deck_id, deck_id)


def summary():
    return json.loads((ROOT / "data" / "grixis_summary.json").read_text(encoding="utf-8"))


def deck_block_text(slug):
    t = (ROOT / "grixis" / "decks" / f"{slug}.md").read_text(encoding="utf-8")
    m = re.search(r"## Decklist[^\n]*\n.*?```[^\n]*\n(.*?)```", t, re.S)
    return m.group(1)


def projection_text(deck_id, canonical_text, proj=None):
    """Derive the official-legal projection from the canonical list (None when the deck has no projection)."""
    proj = proj if proj is not None else load_json(PROJECTIONS, {"decks": {}})
    d = proj["decks"].get(deck_id)
    if not d:
        return None
    sub = {s["from"]: s["to"] for s in d["substitutions"]}
    out = []
    for l in canonical_text.strip().splitlines():
        m = re.match(r"^(\d+x?) (.+?)( \[.*\])?$", l.strip())
        if m and d.get("drop_companion") and m.group(2) == d["drop_companion"] and "Companion" in (m.group(3) or ""):
            continue
        if m and m.group(2) in sub:
            l = f"{m.group(1)} {sub[m.group(2)]}{m.group(3) or ''}"
        out.append(l)
    return "\n".join(out) + "\n"


def challenger_base(deck_id, canonical_text, proj=None):
    """(text, base) the GrokBot v1 challenger swaps apply to. Bjorna's cycle 39 challenger was computed on the Bot
    cycle 16 legal list, which since Bot cycle 47 is the derived compliance projection; every other deck uses its
    canonical project list. Keeps v1 reproducible and the exported challenger byte-identical."""
    pt = projection_text(deck_id, canonical_text, proj)
    return (pt, "official_legal_projection") if pt else (canonical_text, "canonical_project_list")


def oracle_cards():
    import ingest_scryfall as ing
    cards, bulk = ing.get_bulk(ing.DEFAULT_CACHE, None)
    return {c["name"]: c for c in cards}, bulk


def build_exceptions():
    """Import the source's 8-row registry, verify each row against Scryfall + Wizards, correct where needed."""
    by, bulk = oracle_cards()
    src = ARCHIVE / "source-package/research/Project_Exceptions_Current_2026-10-12.csv"
    rows = list(csv.DictReader(src.open(encoding="utf-8")))
    summ = summary()
    pend = load_json(ROOT / "data" / "grixis_pending.json")["decks"]
    WOTC = "wizards:https://magic.wizards.com/en/banned-restricted-list (Commander section, fetched 2026-10-16)"
    MBC = "wizards:" + pend["The_Madcap_Jester"]["legal_from_source"]["url"]
    out = []
    for i, r in enumerate(rows, 1):
        did, card = r["deck_id"], r["card_name"]
        c = by[card]
        slug = summ[did]["slug"]
        canon = deck_block_text(slug)
        in_list = bool(re.search(r"^\d+x? " + re.escape(card) + r"( \[|$)", canon, re.M))
        sc = c["legalities"]["commander"]
        notes = [f"Scryfall oracle bulk {bulk[:10]}: legalities.commander = {sc}."]
        status, zone, authorized_by, legal_from = "verified", "main", None, None
        if card.startswith("Lutri"):
            typ, off, auth, zone = "banned_as_companion", "banned_as_companion", "AUTHORIZED_EXCEPTION", "companion"
            ev_ = [WOTC + ": 'Lutri, the Spellchaser - only banned as a companion'", f"scryfall:{bulk[:10]} legalities.commander={sc} (Scryfall cannot express a companion-only ban)"]
            authorized_by = "Cory (source registry v8.1.4: 'User explicitly permits Lutri as companion'; re-confirmed in the Bot cycle 47 brief, decision 1)"
            status = "corrected"
            notes += ["Correction: the source row says present_in_current_final_exports = YES, but the source's approved 100-card file (refinement/decklists/Cecily__Bjorna__Lutri_Approved_2026-10-13.txt) has no Lutri line; the companion designation lives only in the approval record. Bot cycle 47 adds `1x Lutri, the Spellchaser [Companion]` to the canonical project list from that record.",
                      "Correction: the companion ban is not visible in Scryfall's legality field (Lutri is legal in the 99), so it is verified against the Wizards list, not Scryfall."]
        elif sc == "banned":
            typ, off, auth = "banned_card", "banned", "AUTHORIZED_EXCEPTION"
            ev_ = [WOTC + f": '{card}' listed under Commander Banned Cards", f"scryfall:{bulk[:10]} legalities.commander=banned"]
            authorized_by = f"Cory (source registry v8.1.4: 'User explicitly permits {card} in this project deck'; re-confirmed in the Bot cycle 47 brief, decision 1)"
            notes.append("Bot cycle 16 had replaced this card on import (projection substitution since Bot cycle 47); the canonical project list restores it.")
        elif "Nazg" in card:
            typ, off, auth = "official_card_rule", "legal", "NOT_REQUIRED"
            m = re.search(r"A deck can have up to (\w+) cards named Nazgûl", c["oracle_text"])
            qty = int(re.search(r"^(\d+)x? Nazgûl", canon, re.M).group(1))
            ev_ = [f"scryfall:{bulk[:10]} Oracle text: 'A deck can have up to {m.group(1)} cards named Nazgûl.'", "cr:903.5b"]
            status = "corrected"
            notes += [f"Correction: not a project exception. Multiple copies are allowed by the card's own Oracle text (CR 903.5b), so this is official Commander legality, not a project authorization. This list runs {qty} (limit nine).",
                      "Kept in the registry as a documented copy rule so validators and readers see why the singleton check passes."]
        elif sc == "not_legal":
            typ, off, auth = "future_release", "not_legal_until_release", "AUTHORIZED_FUTURE_RELEASE"
            legal_from = pend[did]["legal_from"]
            ev_ = [f"{MBC}: 'New-to-Magic MBC cards will be legal in Commander on November 13, 2026.'", f"scryfall:{bulk[:10]} legalities.commander=not_legal, set {c['set']}, released {c.get('released_at')}"]
            authorized_by = "Cory (source registry v8.1.4: future-release deck planning; re-confirmed in the Bot cycle 47 brief)"
            if did.startswith("Tresserhorn"):
                status = "corrected"
                notes.append("Correction: the source's 2026-10-15 approval record reports 'current official Commander legality PASS, no project exception required'. That is wrong today: the card is not_legal until 2026-11-13. Its own registry row (future-release commander) is the correct classification.")
        else:
            raise SystemExit(f"unexpected exception row {card}: {sc}")
        out.append({"id": f"exc:{slug}:{re.sub(r'[^a-z0-9]+', '-', card.lower().replace('û', 'u')).strip('-')}", "deck_id": did, "card": card,
                    "oracle_id": c["oracle_id"], "zone": zone, "exception_type": typ, "official_commander_legality": off,
                    "official_evidence": ev_, "legal_from": legal_from, "project_authorization_status": auth, "authorized_by": authorized_by,
                    "source_row": {"index": i, "exception_type": r["exception_type"], "project_status": r["project_status"], "project_rule": r["project_rule"]},
                    "in_canonical_project_list": in_list,
                    "verification": {"status": status, "notes": notes},
                    "render_label": legality_label(off, auth, legal_from)})
    doc = {"_doc": "Bot cycle 47 (M0): project-exception registry, imported from the source's 8-row CSV and verified against Scryfall and the official Wizards banned list. official_commander_legality and project_authorization_status are separate; an exception never counts as Commander-legal. Built by scripts/grixis_authority.py --build-exceptions; schema data/grixis/schemas/exception.schema.json.",
           "schema_version": 1,
           "verified": {"date": M0_DATE, "scryfall_bulk": bulk[:19], "wizards_source": "https://magic.wizards.com/en/banned-restricted-list", "by": "GrokBot (Bot cycle 47)"},
           "source": {"path": "grixis/source-archive/grixis-commander-encyclopediaGPT/source-package/research/Project_Exceptions_Current_2026-10-12.csv", "commit": source_commit(), "rows": len(rows)},
           "exceptions": out}
    EXCEPTIONS.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    return doc


def source_commit():
    import grixis_archive
    return grixis_archive.source_commit()


def cache_snapshot():
    import glob
    c = ROOT / ".cache"
    pick = lambda pat: Path(sorted(glob.glob(str(c / pat)))[-1]).name if glob.glob(str(c / pat)) else None
    edh = sorted(glob.glob(str(c / "edhrec" / "commanders__*.json")))
    mt = sorted(dt.datetime.fromtimestamp(Path(p).stat().st_mtime, dt.timezone.utc).date().isoformat() for p in edh)
    return {"oracle_bulk": pick("oracle-cards-*.jsonl.gz"), "rulings_bulk": pick("rulings-*.jsonl.gz"),
            "comprehensive_rules": pick("MagicCompRules-*.txt"),
            "edhrec_cache": f"{len(edh)} commander pages, file dates {mt[0]}..{mt[-1]}" if mt else "none",
            "spellbook": "data/grixis_combos.json + data/grixis_refine_batches.json spellbook cache"}


def build_registry(R=None):
    import evaluate_decklist as ev
    import grixis_refine as gr
    R = R or ev.Resolver()
    summ = summary()
    old = load_json(REGISTRY, {"decks": {}})
    exc = load_json(EXCEPTIONS)["exceptions"]
    proj = load_json(PROJECTIONS)
    plans = load_json(ROOT / "data" / "grixis_refine_batches.json")
    pend = load_json(ROOT / "data" / "grixis_pending.json")["decks"]
    raw_st = load_json(ARCHIVE / "state" / "current_deck_overrides.json")["decks"]
    norm = lambda k: re.sub(r"_+", "_", k).strip("_").lower()
    by_norm = {norm(k): v for k, v in raw_st.items()}
    st_src = {did: raw_st.get(did) or by_norm.get(norm(did)) for did in summ}  # source keys use single underscores (Anhelo_the_Painter)
    sha = source_commit()
    snap = cache_snapshot()
    snap_id = "snap-" + (snap["oracle_bulk"] or "none").split("-")[-1][:8]
    decks = {}
    for did, v in summ.items():
        slug = v["slug"]
        canon = deck_block_text(slug)
        ce = list_entries(canon, R)
        ch = logical_hash((z, o, q) for z, o, q, _ in ce)
        sp = ARCHIVE / v["source_path"]
        raw = sp.read_bytes()
        se = list_entries(raw.decode("utf-8-sig"), R)
        bh = logical_hash((z, o, q) for z, o, q, _ in se)
        names = {o: n for z, o, q, n in ce + se}
        a, b = {(z, o, q) for z, o, q, _ in se}, {(z, o, q) for z, o, q, _ in ce}
        diff = [f"canonical adds {q}x {names[o]} ({z})" for z, o, q in sorted(b - a)] + [f"canonical removes {q}x {names[o]} ({z})" for z, o, q in sorted(a - b)]
        if diff and did == "Cecily__Bjorna__Lutri":
            diff.append("reason: the source's approval record designates Lutri as companion outside the 100 (missing from its approved 100-card file); authorized project exception")
        rec = (st_src.get(did) or {}).get("approved_list_sha256")
        mine = [x for x in exc if x["deck_id"] == did and x["project_authorization_status"] != "NOT_REQUIRED"]
        if did in pend and pend[did].get("status") == "pending":
            comp = {"status": "pending_release", "cards": pend[did]["cards"], "checked": f"Scryfall {snap['oracle_bulk']}; legal from {pend[did]['legal_from']} (Wizards)"}
            auth = "authorized_future_release"
        elif any(x["project_authorization_status"] == "AUTHORIZED_EXCEPTION" for x in mine):
            comp = {"status": "not_compliant_project_exceptions", "cards": [x["card"] for x in mine], "checked": f"Scryfall {snap['oracle_bulk']} + Wizards B&R (2026-10-16)"}
            auth = "authorized_exceptions"
        else:
            res = ev.check(canon, R)
            hard = [i for i in res["issues"] if i["type"] in ev.HARD]
            if hard:
                raise SystemExit(f"{did}: canonical list fails hard checks without a registered exception: {hard}")
            comp = {"status": "compliant", "cards": [], "checked": f"Scryfall {snap['oracle_bulk']}"}
            auth = "none"
        pj = None
        pt = projection_text(did, canon, proj)
        if pt:
            pj = {"label": PROJECTION_LABEL, "canonical": False, "approval_state": None, "hash": text_hash(pt, R),
                  "path": f"exports/grixis-archidekt/projections/{slug}.official-legal-projection.txt", "derived_from": ch,
                  "substitutions": [f"{s['from']} → {s['to']}" for s in proj["decks"][did]["substitutions"]] + [f"companion {proj['decks'][did]['drop_companion']} removed"],
                  "official_commander_compliance": "compliant"}
        e = (plans["decks"].get(did) or {})
        chal = []
        if e.get("swaps"):
            bt, base = challenger_base(did, canon, proj)
            ct = gr.apply_swaps(bt, e["swaps"])
            chal.append({"id": f"chal:{slug}:grokbot-v1", "label": CHALLENGER_LABEL, "origin": "GrokBot refinement, Bot cycles 39-44 (data/grixis_refine_batches.json)",
                         "engine": "grixis_refine v1", "state": "CHALLENGER", "base": base, "hash": text_hash(ct, R),
                         "export_path": f"exports/grixis-archidekt/{slug}.txt", "swaps": [{"cut": w["cut"], "add": w["add"], "cycle": w["cycle"]} for w in e["swaps"]]})
            verdict = f"v1 produced a challenger ({len(e['swaps'])} swap(s)); evidence only, not approved"
        elif e:
            verdict = V1_HEURISTIC_LABEL
        else:
            verdict = "not reviewed by v1"
        claim = v.get("src_claim")
        sval = (claim.split(" ")[0] if claim and claim[0] in "12345" else None)
        if sval == "5":
            sval = "5"
        rid = registry_id(did)
        o = old["decks"].get(rid) or old["decks"].get(did, {})
        initial = "PENDING_RELEASE" if comp["status"] == "pending_release" else "SOURCE_BASELINE"
        hist = o.get("state_history") or [{"state": initial, "date": M0_DATE, "cycle": CYCLE,
                                           "reason": "M0 import: source list as baseline; prior source approval kept as evidence (Cory decision 2)" + ("; cards not Commander-legal before " + pend[did]["legal_from"] if initial == "PENDING_RELEASE" else "")}]
        state = o.get("state", initial)
        oc = o.get("ceiling", {})
        g = oc.get("grok_estimated_ceiling") or {"value": None, "evidence": [], "cycle": None}
        rc = oc.get("resolved_ceiling") or {"value": None, "resolved_by": None, "date": None, "evidence": []}
        # Bot cycle 50 (M2): the commander blueprint supplies blueprint_version and the GrokBot ceiling estimate, and may
        # recover a source ceiling the parse missed (cited per file); the parsed claim is never overwritten.
        bpf = DATA / "blueprints" / f"{slug}.json"
        bp = json.loads(bpf.read_text(encoding="utf-8")) if bpf.exists() else None
        bp_version = bp["version"] if bp else o.get("blueprint_version")
        src_ceiling = {"value": sval, "label": claim, "evidence": [f"source_archive:{v['source_path']} (approval/blueprint records, parsed by build_grixis.py)"] if claim else []}
        eff = sval
        if bp:
            g = {"value": bp["power"]["grok_estimated_ceiling"]["value"]["value"],
                 "evidence": [f"companion:data/grixis/blueprints/{slug}.json#power.grok_estimated_ceiling"], "cycle": bp["cycle"]}
            bsc = bp["power"]["source_ceiling"]
            if sval is None and bsc["value"]["value"] is not None:
                eff = bsc["value"]["value"]
                src_ceiling["recovered"] = {"value": eff, "label": bsc["value"]["label"], "evidence": bsc["evidence"], "cycle": bp["cycle"],
                                            "note": "build_grixis.py parsed no claim; recovered from the cited source file by the M2 blueprint (recovery, not an overwrite)"}
        dis = None if eff is None or g["value"] is None else eff != g["value"]
        decks[rid] = {
            "deck_id": rid, "slug": slug, "commanders": v["commanders"], "state": state, "state_history": hist,
            "approval": o.get("approval") or {"state": None, "cycle": None, "date": None, "by": None, "record_id": None},
            "baseline_hash": bh,
            "source": {"repository": SOURCE_REPO, "commit": sha, "path": v["source_path"], "raw_sha256": raw_hash(raw),
                       "recorded_sha256": rec, "recorded_matches_raw": (None if not rec else ("sha256:" + rec) == raw_hash(raw))},
            "canonical_project_list": {"hash": ch, "path": f"grixis/decks/{slug}.md#decklist-archidekt-import",
                                       "companion": next((n for z, o_, q, n in ce if z == "companion"), None), "export": f"exports/grixis-archidekt/" + (f"source-baseline/{slug}.txt" if chal or pj else f"{slug}.txt")},
            "current_canonical_hash": ch, "canonical_differs_from_source": diff,
            "supersedes_hash": o.get("supersedes_hash"),
            "official_commander_compliance": comp, "project_authorization_status": auth,
            "project_exceptions": [x["id"] for x in exc if x["deck_id"] == did],
            "official_legal_projection": pj, "challengers": chal, "heuristic_v1_verdict": verdict,
            "historical_approvals": [{"origin": "source", "state": f"{(st_src.get(did) or {}).get('approval_status')}/{(st_src.get(did) or {}).get('lock_status')}",
                                      "date": (st_src.get(did) or {}).get("user_approval_date"), "hash_recorded": rec, "counts_as": "evidence",
                                      "ref": f"source_archive:state/current_deck_overrides.json#{did}"}],
            "ceiling": {"source_ceiling": src_ceiling,
                        "bracket_floor": {"value": v["cfloor"], "evidence": ["companion:data/grixis_summary.json cfloor (Game Changers, mass land denial, two-card infinites)"]},
                        "grok_estimated_ceiling": g, "resolved_ceiling": rc, "disagreement": dis,
                        "floor_above_source_claim": bool(eff and eff.isdigit() and v["cfloor"] > int(eff))},
            "blueprint_version": bp_version, "snapshots": snap_id,
            "test_suite_version": o.get("test_suite_version"), "test_result_hash": o.get("test_result_hash"),
            "finalization_certificate": o.get("finalization_certificate"),
            "reopen_triggers": list(TRIGGER_KINDS), "open_triggers": o.get("open_triggers", []),
            "source_repository": SOURCE_REPO, "source_commit": sha}
        if rid != did:
            c = DECK_ID_CORRECTIONS[did]
            decks[rid]["deck_id_provenance"] = {"source_deck_id": did, "corrected_cycle": c["corrected_cycle"],
                                                "corrected_date": c["corrected_date"], "note": c["note"], "evidence": list(c["evidence"])}
    prog = (old.get("program") or {}).get("milestones") or {}
    ms = {}
    for m, s0 in (("M0", "complete_pending_acceptance"), ("M1", "in_progress")) + tuple((f"M{i}", "not_started") for i in range(2, 9)):
        x = prog.get(m) or {"status": s0, "accepted_by": None, "accepted_date": None}
        x["criteria_doc"] = f"grixis/Grixis Authority Model.md#{m.lower()}"
        ms[m] = x
    doc = {"_doc": "Bot cycle 47 (M0): canonical authority registry for the 62 Grixis decks. One canonical project list per commander; every deck starts at SOURCE_BASELINE (PENDING_RELEASE for cards not yet Commander-legal); source approvals and GrokBot cycle 39-44 refinements are evidence / challengers. APPROVED and CANONICAL_LOCKED need a human approval record (data/grixis/approvals.json). Built by scripts/grixis_authority.py --build; checked by validate_all step 'authority'. Model: grixis/Grixis Authority Model.md.",
           "schema_version": 1, "generated_by": "scripts/grixis_authority.py --build",
           "source_repository": SOURCE_REPO, "source_commit": sha, "hash_definition": HASH_DEFINITION,
           "snapshots": {"id": snap_id, **snap}, "reopen_trigger_kinds": list(TRIGGER_KINDS),
           "human_approvers": old.get("human_approvers") or ["corymstover"],
           "program": {"milestones": ms}, "decks": decks}
    return doc


# ---------------------------------------------------------------- check
def milestone_problems(ms, approvers):
    """Bot cycle 50: only a human approver accepts a milestone, with a date and recorded evidence."""
    p = []
    for m, x in ms.items():
        if x["status"] == "accepted" and (x.get("accepted_by") not in approvers or not x.get("accepted_date") or not x.get("acceptance_evidence")):
            p.append(f"program.milestones.{m}: accepted needs accepted_by (a human approver), accepted_date and acceptance_evidence")
        if x["status"] != "accepted" and x.get("accepted_by"):
            p.append(f"program.milestones.{m}: accepted_by set but status is {x['status']}")
    return p


def check(R=None):
    problems, warnings = [], []
    reg, exc, appr = load_json(REGISTRY), load_json(EXCEPTIONS), load_json(APPROVALS)
    for doc, sch, name in ((reg, "registry.schema.json", "registry.json"), (exc, "exception.schema.json", "exceptions.json"),
                           (appr, "approval.schema.json", "approvals.json")):
        if doc is None:
            problems.append(f"data/grixis/{name} missing")
            continue
        problems += [f"{name}: {e}" for e in validate_file(doc, sch)[:20]]
    for f in sorted(SCHEMAS.glob("*.schema.json")):
        try:
            s = json.loads(f.read_text(encoding="utf-8"))
            assert s.get("$schema") and s.get("$id", "").endswith(f.name)
        except Exception as e:  # noqa: BLE001
            problems.append(f"schema {f.name} unreadable or missing $schema/$id: {e}")
    v2 = load_json(REFINE_V2)
    if v2 is not None:
        problems += [f"grixis_refine_v2.json: {e}" for e in validate_file(v2, "refine_v2.schema.json")[:20]]
    if problems or reg is None:
        return problems, warnings
    ms = reg["program"]["milestones"]
    if v2 is not None and not v2.get("exploratory") and not all((ms.get(m) or {}).get("status") == "accepted" for m in ("M2", "M4")):
        problems.append("grixis_refine_v2.json: recommendations must be labeled exploratory until M2 and M4 are accepted")
    approvers = set(reg["human_approvers"])
    problems += milestone_problems(ms, approvers)
    recs = appr["records"]
    for r in recs:
        if r["approved_by"] not in approvers:
            problems.append(f"approvals.json {r['id']}: approved_by {r['approved_by']} is not a human approver")
        if r["deck_id"] not in reg["decks"]:
            problems.append(f"approvals.json {r['id']}: unknown deck {r['deck_id']}")
    # rebuild the derived registry and compare (catches stale hashes, new challengers, edited lists)
    fresh = build_registry(R)
    if len(reg["decks"]) != 62 or set(reg["decks"]) != set(fresh["decks"]):
        problems.append(f"registry must hold the same 62 decks as data/grixis_summary.json ({len(reg['decks'])})")
    for did, e in reg["decks"].items():
        problems += approval_problems(did, e, recs, approvers, ms)
        f = fresh["decks"].get(did)
        if not f:
            continue
        for k in ("baseline_hash", "current_canonical_hash", "canonical_project_list", "challengers", "official_legal_projection",
                  "official_commander_compliance", "project_authorization_status", "project_exceptions", "source", "heuristic_v1_verdict",
                  "blueprint_version", "ceiling", "deck_id_provenance"):
            if e.get(k) != f.get(k):
                if k == "current_canonical_hash" and e["state"] in HUMAN_STATES | {"APPROVAL_READY"}:
                    problems.append(f"{did}: canonical list changed after {e['state']} — set REOPEN_REQUIRED (trigger audit_error/user_instruction) and re-review")
                else:
                    problems.append(f"{did}: registry field '{k}' is stale (run scripts/grixis_authority.py --build)")
        if e["state"] == "PENDING_RELEASE" and e["official_commander_compliance"]["status"] != "pending_release":
            problems.append(f"{did}: PENDING_RELEASE but the cards are no longer pending (open trigger legality_change; move to SOURCE_BASELINE)")
        if e["official_commander_compliance"]["status"] == "pending_release" and e["state"] not in ("PENDING_RELEASE",) and not e["open_triggers"]:
            problems.append(f"{did}: pending-release cards but state {e['state']}")
    snap = cache_snapshot()
    for k in ("oracle_bulk", "rulings_bulk", "comprehensive_rules"):
        if reg["snapshots"].get(k) != snap.get(k):
            gated = [d for d, e in reg["decks"].items() if e["state"] in GATED_STATES and not any(t["kind"] in ("oracle_change", "rules_change") for t in e["open_triggers"])]
            (problems if gated else warnings).append(f"snapshot {k} changed ({reg['snapshots'].get(k)} → {snap.get(k)})" +
                                                     (f": decks {gated} need an open oracle_change/rules_change trigger" if gated else "; re-run --build to record the new snapshot"))
    # exceptions: verified against current Scryfall and the canonical lists
    by, bulk = oracle_cards()
    pend = load_json(ROOT / "data" / "grixis_pending.json")["decks"]
    for x in exc["exceptions"]:
        c = by.get(x["card"])
        sc = c["legalities"]["commander"] if c else None
        exp = {"banned": "banned", "banned_as_companion": "legal", "not_legal_until_release": "not_legal", "legal": "legal"}[x["official_commander_legality"]]
        if sc != exp:
            problems.append(f"exceptions.json {x['id']}: Scryfall now says {sc}, registry expects {exp} (trigger legality_change; re-verify)")
        if x["official_commander_legality"] != "legal" and x["project_authorization_status"] == "NOT_REQUIRED":
            problems.append(f"exceptions.json {x['id']}: a card that is not Commander-legal needs a project authorization")
        if x["project_authorization_status"] in ("AUTHORIZED_EXCEPTION", "AUTHORIZED_FUTURE_RELEASE") and not x["authorized_by"]:
            problems.append(f"exceptions.json {x['id']}: authorized without authorized_by")
        if x["render_label"] != legality_label(x["official_commander_legality"], x["project_authorization_status"], x["legal_from"]):
            problems.append(f"exceptions.json {x['id']}: render_label must come from legality_label()")
        if x["official_commander_legality"] != "legal" and re.search(r"(?<!NOT )Commander-legal(?! yet)", x["render_label"]) and "NOT" not in x["render_label"]:
            problems.append(f"exceptions.json {x['id']}: label reports an exception as legal")
        slug = reg["decks"][registry_id(x["deck_id"])]["slug"]
        canon = deck_block_text(slug)
        tag = "Companion" if x["zone"] == "companion" else None
        hit = re.search(r"^\d+x? " + re.escape(x["card"]) + r"( \[([^\]]*)\])?$", canon, re.M)
        if not hit or (tag and tag not in (hit.group(2) or "")):
            problems.append(f"exceptions.json {x['id']}: {x['card']} is not in the canonical project list of {x['deck_id']} ({x['zone']})")
        if x["exception_type"] == "future_release":
            pr = pend.get(x["deck_id"], {})
            if pr.get("status") != "pending" or x["card"] not in pr.get("cards", []) or pr.get("legal_from") != x["legal_from"]:
                problems.append(f"exceptions.json {x['id']}: disagrees with data/grixis_pending.json")
    for did, pr in pend.items():
        if pr.get("status") == "pending":
            for card in pr["cards"]:
                if not any(x["deck_id"] == did and x["card"] == card for x in exc["exceptions"]):
                    problems.append(f"data/grixis_pending.json {did}: {card} has no exception-registry row")
    return problems, warnings


def main(argv):
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    if "--build-exceptions" in argv:
        d = build_exceptions()
        print(f"exceptions: {len(d['exceptions'])} rows ({sum(1 for x in d['exceptions'] if x['verification']['status'] == 'corrected')} corrected)")
    if "--build" in argv:
        doc = build_registry()
        REGISTRY.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        if not APPROVALS.exists():
            APPROVALS.write_text(json.dumps({"_doc": "Human approval records (Bot cycle 47+). The ONLY path for a deck to reach APPROVED or CANONICAL_LOCKED: each record names the exact canonical list hash (lh1), the decision, the human approver (registry.human_approvers) and the instruction that carries the sign-off. No record exists until Cory explicitly approves a list. Schema: data/grixis/schemas/approval.schema.json.", "schema_version": 1, "records": []}, indent=1) + "\n", encoding="utf-8")
        from collections import Counter
        print(f"registry: {len(doc['decks'])} decks; states {dict(Counter(e['state'] for e in doc['decks'].values()))}")
    if "--check" in argv:
        p, w = check()
        reg = load_json(REGISTRY) or {"decks": {}}
        from collections import Counter
        st = Counter(e["state"] for e in reg["decks"].values())
        nchal = sum(len(e["challengers"]) for e in reg["decks"].values())
        nexc = len((load_json(EXCEPTIONS) or {"exceptions": []})["exceptions"])
        print(f"authority: {len(reg['decks'])} decks ({', '.join(f'{k} {v}' for k, v in sorted(st.items()))}); {nchal} challengers; {nexc} exception rows; "
              f"{len((load_json(APPROVALS) or {'records': []})['records'])} human approvals; {len(list(SCHEMAS.glob('*.schema.json')))} schemas; {len(p)} problem(s), {len(w)} warning(s)")
        for x in p[:40]:
            print("  - " + x)
        for x in w[:10]:
            print("  ⚠️ " + x)
        return 1 if p else 0
    return 0


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    sys.exit(main(sys.argv[1:]))
