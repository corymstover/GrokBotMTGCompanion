#!/usr/bin/env python3
"""Fail-closed verifier for FINAL M6 J reproducibility bundles.

This script never creates receipts or certificates and never changes deck state.
Missing bundles are reported as pending; a missing bundle cannot be counted ready.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import grixis_authority as ga

BUNDLES = ROOT / "data/grixis/m6/bundles"
REGISTRY = ROOT / "data/grixis/registry.json"
SEALS = ROOT / "data/grixis/m6/sealed/reconciliation_manifest.json"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def safe_repo_file(name):
    path = Path(name)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError("unsafe artifact path")
    full = (ROOT / path).resolve()
    if not full.is_relative_to(ROOT.resolve()) or not full.is_file():
        raise ValueError("missing/outside-repo artifact: " + name)
    return full


def content_hash(name):
    return "sha256:" + hashlib.sha256(safe_repo_file(name).read_bytes()).hexdigest()


def bind(name, h):
    if content_hash(name) != h:
        raise ValueError("SHA-256 drift: " + name)


OWNER_EQUIVALENT = "FORMAL_PASS_C_OWNER_EQUIVALENT"
OWNER_WAIVER = "data/grixis/m6/governance/pass_c_owner_waiver_20261021.json"
OWNER_PROGRESS = "data/grixis/m6/owner_pass_c_substitute/progress.json"

# The original Xander Stage A Markdown, Stage A JSON, and original seal are IMMUTABLE.
# Cory explicitly authorized a VERSIONED, DISCLOSED byte-hash correction on 2026-10-25.
# This is deliberately a one-deck/one-file exception with every old/new byte digest and
# the original Git blob pinned; never broaden it to Lynde or other mismatched seals.
_XANDER_CORRECTION = (
    "data/grixis/m6/owner_pass_c_substitute/Lord_Xander__the_Collector/"
    "stage_a_seal_correction_v2_20261025.json"
)
_XANDER_CORRECTION_SHA = "7db5628952da3d4ca165fff30e9ab443071ed99f97b521ff84239c8692e16c0b"
_XANDER_ORIGINAL_SEAL_SHA = "1052e6b3032c1d5d018c3740222ce586b8ea30eaecfd6f86ad05a8d8e6837dd4"
_XANDER_SEALED_MD_SHA = "89a78d803b5cb5ea886b2402828aaff00b78497db0b3c0fe569c6c0ee5a879d1"
_XANDER_ACTUAL_MD_SHA = "826f07707a6fdd1583b815ba6b80ad99bd8a71d57d03ac05766ed2a0a4cd0322"
_XANDER_STAGE_A_BLOB = "e97d35fe9666519ed8ff0fc5e605d3ff2b5a5e07"


def verify_xander_versioned_stage_a_correction(deck_id, seal, ext):
    """Accept only Cory's exact v2 record; never substitute a fabricated digest.

    We recompute the original Stage A Markdown SHA, Git object hash, sealed JSON,
    original seal SHA and immutable correction-record SHA. This only reconciles the
    historical *recorded digest*, not Stage A content or actual independence.
    """
    if deck_id != "Lord_Xander__the_Collector" or ext != "md":
        return False
    base = "data/grixis/m6/owner_pass_c_substitute/Lord_Xander__the_Collector/"
    correct_path = base + "stage_a.md"
    seal_path = base + "seal.json"
    if (seal.get("stage_a_md_path") != correct_path
            or seal.get("stage_a_md_sha256") != _XANDER_SEALED_MD_SHA
            or content_hash(seal_path) != "sha256:" + _XANDER_ORIGINAL_SEAL_SHA):
        return False
    if content_hash(_XANDER_CORRECTION) != "sha256:" + _XANDER_CORRECTION_SHA:
        return False
    correction = load(safe_repo_file(_XANDER_CORRECTION))
    if not all((
        correction.get("schema_version") == "xander-stage-a-byte-hash-correction-v2",
        correction.get("deck_id") == deck_id,
        correction.get("historical_original_seal_sha256") == _XANDER_ORIGINAL_SEAL_SHA,
        correction.get("historical_original_recorded_stage_a_md_sha256") == _XANDER_SEALED_MD_SHA,
        correction.get("observed_original_stage_a_md_sha256") == _XANDER_ACTUAL_MD_SHA,
        correction.get("original_stage_a_git_blob_sha") == _XANDER_STAGE_A_BLOB,
        correction.get("technically_independent") is False,
        correction.get("canonical_historical_baseline_sha256") == seal.get("canonical_input_sha256"),
    )):
        return False
    data = safe_repo_file(correct_path).read_bytes()
    computed_blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
    return (hashlib.sha256(data).hexdigest() == _XANDER_ACTUAL_MD_SHA
            and computed_blob == _XANDER_STAGE_A_BLOB
            and content_hash(base + "stage_a.json")
            == "sha256:" + correction["original_stage_a_json_sha256"]
            and correction["original_stage_a_json_sha256"] == seal.get("stage_a_json_sha256"))

# Lynde carries its own provenance-only Stage A correction. This is not a global waiver.
# Original Stage A MD/JSON/seal remain byte-identical; owner approval is one deck decision.
_LYNDE_CORRECTION = (
    "data/grixis/m6/owner_pass_c_substitute/Lynde__Cheerful_Tormentor/"
    "stage_a_seal_correction_v2_20261025.json"
)
_LYNDE_CORRECTION_SHA = "f7ffaef0d8e5181e959de30b061fcf56a8fd09a854d18b745691c60a9ec7087c"
_LYNDE_ORIGINAL_SEAL_SHA = "ed5a1c20af6bdf0e999499fd1e07ad8652796051438ec59ec802b6f619e51a98"
_LYNDE_SEALED_MD_SHA = "59f2dc10eedec5797f3f5dcfdb0a206b380a037e9b17a29e740d6ca94829c12e"
_LYNDE_ACTUAL_MD_SHA = "02adfb85db19aa42d5dfe36b96906874ea1abd232b6f8bfc3861c1108035b72a"
_LYNDE_STAGE_A_BLOB = "b253ed9c4c7543b4c369dba957b2b4971c059133"


def verify_lynde_versioned_stage_a_correction(deck_id, seal, ext):
    """Validate exactly one immutable Lynde MD hash correction, fail closed."""
    if deck_id != "Lynde__Cheerful_Tormentor" or ext != "md":
        return False
    base = "data/grixis/m6/owner_pass_c_substitute/Lynde__Cheerful_Tormentor/"
    md_path, seal_path = base + "stage_a.md", base + "seal.json"
    if (seal.get("stage_a_md_path") != md_path
            or seal.get("stage_a_md_sha256") != _LYNDE_SEALED_MD_SHA
            or content_hash(seal_path) != "sha256:" + _LYNDE_ORIGINAL_SEAL_SHA):
        return False
    if content_hash(_LYNDE_CORRECTION) != "sha256:" + _LYNDE_CORRECTION_SHA:
        return False
    correction = load(safe_repo_file(_LYNDE_CORRECTION))
    if not all((
        correction.get("schema_version") == "lynde-stage-a-byte-hash-correction-v2",
        correction.get("deck_id") == deck_id,
        correction.get("historical_original_seal_sha256") == _LYNDE_ORIGINAL_SEAL_SHA,
        correction.get("historical_original_recorded_stage_a_md_sha256") == _LYNDE_SEALED_MD_SHA,
        correction.get("observed_original_stage_a_md_sha256") == _LYNDE_ACTUAL_MD_SHA,
        correction.get("original_stage_a_git_blob_sha") == _LYNDE_STAGE_A_BLOB,
        correction.get("technically_independent") is False,
        correction.get("canonical_historical_baseline_sha256") == seal.get("canonical_input_sha256"),
    )):
        return False
    data = safe_repo_file(md_path).read_bytes()
    computed_blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
    return (hashlib.sha256(data).hexdigest() == _LYNDE_ACTUAL_MD_SHA
            and computed_blob == _LYNDE_STAGE_A_BLOB
            and content_hash(base + "stage_a.json")
            == "sha256:" + correction["original_stage_a_json_sha256"]
            and correction["original_stage_a_json_sha256"] == seal.get("stage_a_json_sha256"))


# Strict Pass C non-independence disclosure (added for PR #653, Ashad): "technical(ly) independen(ce|t)"
# followed only by markdown/colon punctuation and then an explicit FALSE, or a NO that ends the clause
# (so "no longer ..." never matches). Any explicit TRUE/YES statement anywhere vetoes this path.
# The four legacy substrings below are kept unchanged so every receipt accepted before stays accepted.
_PASS_C_EXPLICIT_FALSE = re.compile(
    r"\btechnical(?:ly)?\s+independen(?:ce|t)[\s*:_`]*(?:false\b|no(?=[\s*_`]*(?:[.,;)]|$)))", re.I | re.M)
_PASS_C_EXPLICIT_TRUE = re.compile(r"\btechnical(?:ly)?\s+independen(?:ce|t)[\s*:_`]*(?:true|yes)\b", re.I)


# Strict parenthetical Pass C non-independence disclosure (added after PR #653 for Ashnod_the_Uncaring,
# whose preserved receipt reads "technical third-model independence (actual evaluator ...; independent=FALSE,
# owner-waived)"). Accepts only an explicit independent=FALSE inside the parenthetical that directly follows
# "technical third-model independence"; any independent=TRUE/YES or explicit TRUE/YES statement anywhere vetoes.
_PASS_C_PAREN_FALSE = re.compile(
    r"\btechnical\s+third-model\s+independence\s*\([^()]*?\bindependent\s*=\s*false\b[^()]*\)", re.I)
_PASS_C_PAREN_TRUE = re.compile(r"\bindependent\s*=\s*(?:true|yes)\b", re.I)


def pass_c_parenthetical_false_disclosure(text):
    """Fail closed: True only for the explicit parenthetical independent=FALSE form, with no
    independent=TRUE/YES and no explicit TRUE/YES technical-independence statement anywhere."""
    return (bool(_PASS_C_PAREN_FALSE.search(text)) and not _PASS_C_PAREN_TRUE.search(text)
            and not _PASS_C_EXPLICIT_TRUE.search(text))


def pass_c_explicit_false_disclosure(text):
    """Fail closed: True only for an explicit FALSE/NO technical-independence statement with no
    explicit TRUE/YES statement anywhere in the receipt. Absent or ambiguous wording returns False."""
    return bool(_PASS_C_EXPLICIT_FALSE.search(text)) and not _PASS_C_EXPLICIT_TRUE.search(text)


def _bare(h):
    return (h or "").removeprefix("sha256:")


# Legacy Stage A seal field names (added after PR #653 for Ashnod_the_Uncaring, whose preserved, immutable
# seal.json uses the "A_SEAL" schema). Only these exact one-to-one renames are mapped; values are never
# rewritten or inferred. Fail closed: a seal carrying both a canonical key and its legacy alias is rejected,
# and a seal that is not the complete A_SEAL legacy form is returned unchanged (so it fails as before).
_LEGACY_A_SEAL_ALIASES = {
    "canonical_input_sha256": "canonical_approved_sha256",
    "git_first_stage_commit_sha": "first_stage_git_commit_sha",
    "review_class_after_final": "formal_pass_c_classification",
    "technically_independent": "technical_independence",
    "actual_evaluator": "actual_model",
}


def normalize_legacy_stage_a_seal(seal):
    """Return seal with canonical field names for the exact legacy A_SEAL schema, else unchanged."""
    if any(c in seal and a in seal for c, a in _LEGACY_A_SEAL_ALIASES.items()):
        raise ValueError("Stage A seal carries both canonical and legacy field names")
    if (seal.get("stage") != "A_SEAL" or seal.get("owner_independence_waiver") is not True
            or any(c in seal for c in _LEGACY_A_SEAL_ALIASES)
            or not all(a in seal for a in _LEGACY_A_SEAL_ALIASES.values())):
        return seal
    out = {k: v for k, v in seal.items() if k not in _LEGACY_A_SEAL_ALIASES.values()}
    for c, a in _LEGACY_A_SEAL_ALIASES.items():
        out[c] = seal[a]
    return out


# ---------------------------------------------------------------------------------------------------
# M7 Deck #7 (Be_lakor__the_Dark_Master) ONE-TIME stabilization for decks #7-#62 (surveyed over the full
# preserved 62-receipt owner-equivalent corpus at data/grixis/m6/owner_pass_c_substitute/*). Decks #8-#62
# are expected to copy this file byte-identically. Everything below is an explicit, enumerated, fail-closed
# compatibility layer; nothing accepted by the PR #654 logic above is changed or newly rejected.
#
# Seal fields: each canonical field may be read from exactly the enumerated legacy key paths below (one-to-one
# rename; values are copied verbatim and never coerced). Every present source for a field must carry an
# identical value (conflict => reject). A required field with no source => reject. Stage A paths that a legacy
# seal never recorded are bound to the fixed conventional location {deck dir}/stage_a.{md,json} -- the same fixed
# directory the judgment paths above are required to use -- and any recorded path must equal it exactly.
_SEAL_FIELD_ALIASES = {
    "canonical_input_sha256": (
        ("canonical_input_sha256",), ("canonical_approved_sha256",), ("canonical_sha256",),
        ("canonical_approved_raw_sha256",), ("canonical_raw_sha256",), ("owner_canonical_raw_sha256",),
        ("canonical_owner_sha256",), ("canonical_exact_sha256",), ("canonical_deck_sha256",),
        ("approved_canonical_list_sha256",), ("canonical_txt_raw_sha256_recomputed",), ("source", "raw_sha256")),
    "git_first_stage_commit_sha": (
        ("git_first_stage_commit_sha",), ("first_stage_git_commit_sha",), ("first_stage_commit_sha",),
        ("stage_a_first_commit_sha",), ("stage_a_commit_sha",), ("stage_a_first_stage_commit_sha",),
        ("first_complete_stage_a_commit_sha",)),
    "review_class_after_final": (
        ("review_class_after_final",), ("review_class",), ("formal_pass_c_classification",), ("formal_class",),
        ("formal_pass_c_class",), ("formal_classification",), ("classification",), ("review_classification",),
        ("formal_pass_c_qualification",), ("review_class_if_qualified",), ("review_class_upon_completion",),
        ("review_class_if_verified",)),
    "technically_independent": (
        ("technically_independent",), ("technical_independence",), ("technical_model_independence",),
        ("technically_independent_model",)),
    "actual_evaluator": (("actual_evaluator",), ("actual_model",)),
}
_STAGE_A_FILE_ALIASES = {
    "md": {
        "path": (("stage_a_md_path",), ("stage_a_markdown_path",), ("artifacts", "stage_a.md", "path"),
                 ("stage_a_markdown", "path"), ("immutable_stage_a", "markdown", "path")),
        "sha256": (("stage_a_md_sha256",), ("stage_a_markdown_sha256",), ("stage_a_markdown_raw_sha256",),
                   ("artifacts", "stage_a.md", "sha256"), ("stage_a_files", "stage_a.md", "sha256"),
                   ("immutable_stage_a_files", "stage_a.md", "sha256"), ("stage_a_markdown", "sha256"),
                   ("immutable_stage_a", "markdown", "raw_sha256")),
    },
    "json": {
        "path": (("stage_a_json_path",), ("artifacts", "stage_a.json", "path"), ("stage_a_json", "path"),
                 ("immutable_stage_a", "json", "path")),
        "sha256": (("stage_a_json_sha256",), ("stage_a_json_raw_sha256",), ("artifacts", "stage_a.json", "sha256"),
                   ("stage_a_files", "stage_a.json", "sha256"), ("immutable_stage_a_files", "stage_a.json", "sha256"),
                   ("stage_a_json", "sha256"), ("immutable_stage_a", "json", "raw_sha256")),
    },
}
# List-form file records ("files" / "stage_a_files" as a list of {path, sha256}) are matched by exact path only.
_STAGE_A_FILE_LISTS = ("files", "stage_a_files")
# Exact evaluator spellings accepted in a seal (verbatim; Saruman/Sauron seals use the spaced form).
_SEAL_EVALUATOR_SPELLINGS = ("ChatGPT/OpenAI GPT-6", "ChatGPT / OpenAI GPT-6")
# Two minimal legacy seal schemas record only the commit and Stage A hashes (plus some identity fields); the
# missing identity fields are read verbatim from the Stage A JSON that the seal itself hash-binds, using these
# exact one-to-one names. Schema/deck/hash mismatch rejects; a field present in both must be identical.
#   "jlk_stage_a_seal_v1" (Cormela__Glamour_Thief)  -> Stage A JSON schema "jlk_stage_a_v1"
#   "jlk-neutral-seal-1"  (Jeleva/Kefka/Kess/Grixistax/Loki/Lynde ...) -> Stage A JSON schema_version "jlk-stage-a-1"
_SEALED_STAGE_A_JSON_FIELDS = {
    ("schema", "jlk_stage_a_seal_v1"): (("schema", "jlk_stage_a_v1"), {
        "canonical_input_sha256": "canonical_sha256",
        "review_class_after_final": "formal_classification",
        "technically_independent": "independent_model_execution",
        "actual_evaluator": "actual_evaluator",
    }),
    ("schema_version", "jlk-neutral-seal-1"): (("schema_version", "jlk-stage-a-1"), {
        "canonical_input_sha256": "canonical_approved_list_sha256",
        "review_class_after_final": "review_class",
        "technically_independent": "technically_independent",
        "actual_evaluator": "actual_evaluator",
    }),
}
_MISSING = object()

# Seal-level fail-closed vetoes (checked for every seal, canonical or legacy). Each key is optional, but when a
# seal carries it, its value must be exactly one of the enumerated values preserved in the 62-receipt corpus:
# the seal must be a Stage A seal, must record the owner waiver, and must never assert independence or a
# Stage B unblinding before sealing. Anything else (e.g. stage "B_SEAL", waiver False) rejects.
_SEAL_STAGE_VALUES = frozenset({
    "A_SEAL", "A_CRYPTOGRAPHIC_SEAL", "A_SEALED_BEFORE_UNBLINDING", "A_SEALED_PRE_UNBLINDING",
    "A_SHA256_SEALED_BEFORE_UNBLIND", "STAGE_A_CRYPTOGRAPHIC_SEAL", "STAGE_A_SEALED_BEFORE_UNBLIND",
    "STAGE_A_SEALED_BEFORE_UNBLINDING"})
_SEAL_REQUIRED_IF_PRESENT = {
    "stage": _SEAL_STAGE_VALUES,
    "sealed_stage": frozenset({"STAGE_A_NEUTRAL"}),
    "owner_independence_waiver": (True,),
    "owner_authorized_independence_waiver": (True,),
    "owner_waived_independence": (True,),
    "cannot_claim_technical_independence": (True,),
    "independence_requirement": frozenset({"OWNER_WAIVED_FOR_FORMAL_PASS_C"}),
    "stage_b_unblinded_before_seal": (False,),
    "stage_b_unblinding_not_performed_before_seal": (True,),
}


def check_seal_vetoes(seal):
    """Reject a seal whose optional stage/waiver/independence fields carry any non-enumerated value."""
    for key, allowed in _SEAL_REQUIRED_IF_PRESENT.items():
        if key in seal:
            value = seal[key]
            if isinstance(value, bool) or any(isinstance(a, bool) for a in allowed):
                ok = any(value is a for a in allowed)
            else:
                ok = isinstance(value, str) and value in allowed
            if not ok:
                raise ValueError("Stage A seal veto field has a non-permitted value: " + key)




def _dig(obj, path):
    for key in path:
        if not isinstance(obj, dict) or key not in obj:
            return _MISSING
        obj = obj[key]
    return obj


def _one_value(name, values):
    present = [v for v in values if v is not _MISSING]
    if not present:
        return _MISSING
    if any(type(v) is not type(present[0]) or v != present[0] for v in present[1:]):
        raise ValueError("Stage A seal carries contradictory values for " + name)
    return present[0]


def normalize_stage_a_seal_aliases(seal, deck_id):
    """Return a seal carrying canonical field names, mapped only from enumerated legacy key paths.

    A seal that already carries every canonical field is returned unchanged (decks #1-#6 and the PR #654
    A_SEAL mapping keep their exact prior behaviour). Otherwise every field must resolve, unambiguously, from
    the explicit alias table; anything missing, partial or contradictory raises ValueError.
    """
    canonical = tuple(_SEAL_FIELD_ALIASES) + tuple(
        f"stage_a_{e}_{k}" for e in ("md", "json") for k in ("path", "sha256"))
    if all(c in seal for c in canonical):
        return seal
    directory = f"data/grixis/m6/owner_pass_c_substitute/{deck_id}"
    out = dict(seal)
    for name, paths in _SEAL_FIELD_ALIASES.items():
        out[name] = _one_value(name, [_dig(seal, p) for p in paths])
    for (key, value), ((a_key, a_value), fields) in _SEALED_STAGE_A_JSON_FIELDS.items():
        if seal.get(key) != value or all(out[n] is not _MISSING for n in fields):
            continue
        json_sha = _one_value("stage_a_json_sha256", [_dig(seal, p) for p in _STAGE_A_FILE_ALIASES["json"]["sha256"]])
        stage_a_json = f"{directory}/stage_a.json"
        if not isinstance(json_sha, str) or content_hash(stage_a_json) != "sha256:" + json_sha:
            raise ValueError(value + " Stage A JSON not bound by its seal")
        stage_a = load(safe_repo_file(stage_a_json))
        if stage_a.get(a_key) != a_value or stage_a.get("deck_id") != deck_id:
            raise ValueError(value + " Stage A JSON schema/deck mismatch")
        for n, src in fields.items():
            out[n] = _one_value(n, [out[n], _dig(stage_a, (src,))])
    for ext, spec in _STAGE_A_FILE_ALIASES.items():
        conventional = f"{directory}/stage_a.{ext}"
        paths = [_dig(seal, p) for p in spec["path"]]
        shas = [_dig(seal, p) for p in spec["sha256"]]
        for listed in _STAGE_A_FILE_LISTS:
            records = seal.get(listed)
            if isinstance(records, list):
                for rec in records:
                    if isinstance(rec, dict) and rec.get("path") == conventional:
                        paths.append(rec["path"])
                        shas.append(rec.get("sha256", _MISSING))
        path = _one_value(f"stage_a_{ext}_path", paths)
        if path is _MISSING:
            path = conventional
        if path != conventional:
            raise ValueError("Stage A seal path is not the fixed deck Stage A location")
        out[f"stage_a_{ext}_path"] = path
        out[f"stage_a_{ext}_sha256"] = _one_value(f"stage_a_{ext}_sha256", shas)
    missing = [k for k, v in out.items() if v is _MISSING]
    if missing:
        raise ValueError("Stage A seal missing required field(s): " + ", ".join(sorted(missing)))
    return out


# Preserved per-deck receipt wordings (verbatim substrings of each immutable final_disposition.md) that state
# technical NON-independence explicitly. Bound to their own deck only; accepted only when no explicit
# independence TRUE/YES statement appears anywhere in the receipt (_PASS_C_ANY_TRUE / existing vetoes).
_PASS_C_PRESERVED_NONINDEPENDENCE = {
    "Be_lakor__the_Dark_Master": "technical third-model independence **NOT PRESENT**",
    "Cecily__Bjorna__Lutri": "Technical independent model FALSE",
    "Cormela__Glamour_Thief": "**not a technically independent third model**",
    "Davros__Dalek_Creator": "**not an actually independent third model**; technical independence absent",
    "Doctor_Doom__King_of_Latveria": "genuinely independent third model **not executed**",
    "Don_Andres__the_Renegade": "genuinely independent model **NO**",
    "Dr__Eggman": "technically independent third model **NO**",
    "Edea__Possessed_Sorceress": "Technically third-model independent **false**",
    "Edward_Kenway": "Technical model independence **FALSE**",
    "Evelyn__the_Covetous": "**Actual technical third-model independence FALSE**",
    "Goro_Goro_and_Satoru": "Actual independent third-model execution **did not occur**",
    "Inalla__Archmage_Ritualist": "Real technical independent third-model execution **not present**",
    "Grixistax___October_2026": "**Actual independent third model:** **NO**",
    "Loki__the_Deceiver": "technical model independence **false**",
    "Lord_of_Tresserhorn": "`technically_independent=false`",
    "Lord_Xander__the_Collector": "`technically_independent=false`",
    "Lynde__Cheerful_Tormentor": "`technically_independent=false`",
    "Mai_and_Zuko": "**not** genuinely independent technical third-model execution",
    "Mairsil__the_Pretender": "Technical third-model independence **false**",
    "Marchesa__Dealer_of_Death": "**Actual technical independence is absent**",
    "Marchesa__the_Black_Rose": "**no actual independent third-model execution**",
    "Mishra__Eminent_One": "actual technical model independence **false**",
    "Missy": "**technical model independence is false**",
    "Nekusar__the_Mindrazer": "Technical independence **NOT PRESENT**",
    "Nicol_Bolas": "Actual technical model independence **absent**",
    "Nicol_Bolas__the_Ravager": "Technical independence absent;",
    "Goben__Gene_Splice_Savant": "(technical independence absent;",
    "Obeka__Brute_Chronologist": "**Technical model independence NOT PRESENT;",
    "Obeka__Splitter_of_Seconds": "**Technical independence:** none;",
    "Parnesse__the_Subtle_Brush": "(not a third technically independent executed model)",
    "Saruman__the_White_Hand": "**actual independent third-model evaluation absent/owner-waived**",
    "Sauron__Lord_of_the_Rings": "technical model independence **FALSE / WAIVED**",
    "Sauron__the_Dark_Lord": "Technical evaluator independence FALSE.**",
    "Sol_kanar_the_Swamp_King": "technical independent-third-model review **not performed**",
    "Tetsuo_Umezawa": "(not a technically independent third model)",
    "The_Madcap_Jester": "Reviewer technically independent = FALSE;",
    "The_Rani": "**technically independent third-model review: NO**",
    "Tresserhorn_s_Lord__Returned": "**not genuinely independent**",
    "Wick__the_Whorled_Mind": "NOT a genuinely independent external/third-model review",
    "Zevlor__Elturel_Exile": "**NOT technically independent external third-model review**",
}
# Preserved per-deck receipt spellings of the actual evaluator for receipts that do not contain the exact
# "ChatGPT/OpenAI GPT-6" string. Verbatim; bound to their own deck only.
_PASS_C_PRESERVED_EVALUATOR_SPELLING = {
    "Lord_Xander__the_Collector": "ChatGPT GPT-6",
    "Mai_and_Zuko": "ChatGPT, OpenAI GPT-6",
    "Obeka__Brute_Chronologist": "ChatGPT / OpenAI GPT-6",
    "Obeka__Splitter_of_Seconds": "ChatGPT / OpenAI GPT-6",
    "Saruman__the_White_Hand": "ChatGPT / OpenAI GPT-6",
    "Sauron__Lord_of_the_Rings": "ChatGPT / OpenAI GPT-6",
    "The_Valeyard": "GPT-6 / ChatGPT",
}
_PASS_C_ANY_TRUE = re.compile(
    r"\b(?:technical(?:ly)?[ _-]+(?:model[ _-]+|third-model[ _-]+|evaluator[ _-]+)?independen(?:ce|t)"
    r"(?:[ _-]+third[ _-]+model)?|independent[ _-]+third[ _-]+model|independent[ _-]+model)"
    r"[\s*:_`=]*(?:true|yes)\b", re.I)


def pass_c_preserved_nonindependence(text, deck_id):
    """Fail closed: True only if this deck's enumerated explicit non-independence wording is present and no
    explicit independence TRUE/YES statement appears anywhere."""
    phrase = _PASS_C_PRESERVED_NONINDEPENDENCE.get(deck_id)
    return (bool(phrase) and phrase in text and not _PASS_C_ANY_TRUE.search(text)
            and not _PASS_C_EXPLICIT_TRUE.search(text) and not _PASS_C_PAREN_TRUE.search(text))


def registry_bound_digest_discrepancy(row, seal, deck_id):
    """Accept a progress-ledger/seal digest mismatch ONLY when it is the registry's own
    recorded historical-digest vs physical-raw discrepancy for this deck.

    Fail closed: the registry must say recorded_matches_raw is False, the ledger must
    carry exactly the registry's recorded (historical) digest, the Stage A seal must
    carry exactly the registry's physical raw SHA-256, and the two must differ. Nothing
    is rewritten; the historical value is preserved and merely reconciled.
    """
    deck = load(REGISTRY)["decks"].get(deck_id) or {}
    src = deck.get("source") or {}
    recorded, physical = _bare(src.get("recorded_sha256")), _bare(src.get("raw_sha256"))
    return (src.get("recorded_matches_raw") is False
            and bool(recorded) and bool(physical) and recorded != physical
            and _bare(row.get("canonical_approved_sha256")) == recorded
            and _bare(seal.get("canonical_input_sha256")) == physical)


def validate_pass_c(judgment, deck_id):
    """Validate either original independent reviewer receipt or owner's exact waiver.

    The waived mode is explicitly NON-INDEPENDENT, with the real owner decision,
    the 62/62 progress ledger, this deck's sealed Stage A and final disposition
    bound to immutable SHA-256 references. This never waives Phase B or M6 J.
    """
    bind(judgment["judgment_receipt_path"], judgment["judgment_receipt_sha256"])
    if judgment.get("review_class") != OWNER_EQUIVALENT:
        reviewer = load(safe_repo_file(judgment["judgment_receipt_path"]))
        if reviewer.get("reviewer") != judgment["reviewer"] or reviewer.get("status") != "critical_review_complete":
            raise ValueError("Pass C reviewer receipt not complete/identified")
        if reviewer.get("can_approve_or_lock") is not False:
            raise ValueError("Pass C reviewer attempted approval")
        return True

    directory = f"data/grixis/m6/owner_pass_c_substitute/{deck_id}"
    expected = {
        "judgment_receipt_path": f"{directory}/final_disposition.md",
        "waiver_receipt_path": OWNER_WAIVER,
        "progress_receipt_path": OWNER_PROGRESS,
        "stage_a_seal_path": f"{directory}/seal.json",
    }
    for key, path in expected.items():
        if judgment.get(key) != path:
            raise ValueError("Wrong owner-equivalent Pass C source: " + key)
    for key in ("waiver_receipt", "progress_receipt", "stage_a_seal"):
        bind(judgment[key + "_path"], judgment[key + "_sha256"])
    waiver = load(safe_repo_file(OWNER_WAIVER))
    progress = load(safe_repo_file(OWNER_PROGRESS))
    raw_seal = load(safe_repo_file(expected["stage_a_seal_path"]))
    check_seal_vetoes(raw_seal)  # fail-closed stage/waiver vetoes (M7 Deck #7)
    seal = normalize_legacy_stage_a_seal(raw_seal)  # e.g. Ashnod_the_Uncaring
    seal = normalize_stage_a_seal_aliases(seal, deck_id)  # decks #7-#62 legacy seal schemas (M7 Deck #7)
    if (judgment.get("technically_independent") is not False
        or progress.get("technically_independent") is not False
        or progress.get("genuinely_independent_third_model_reviews") != 0
        or progress.get("review_class") != OWNER_EQUIVALENT
        or progress.get("actual_model") != "ChatGPT/OpenAI GPT-6"
        or judgment.get("reviewer") != progress["actual_model"]
        or progress.get("formal_pass_c_owner_equivalent_completed") != 62
        or progress.get("final_complete") != 62
        or waiver.get("decision") != "AUTHORIZE_OWNER_EQUIVALENT_PASS_C_AS_REPLACEMENT_FOR_INDEPENDENT_THIRD_MODEL_REQUIREMENT_FOR_M6_GOVERNANCE"
        or waiver.get("applies_to", {}).get("gate") != "M6.5"
        or waiver.get("scope_and_effect", {}).get("m6_5_governance_condition_satisfied") is not True
        or waiver.get("accepted_substitute", {}).get("technically_independent") is not False
        or waiver.get("accepted_substitute", {}).get("genuinely_independent_third_model_reviews") != 0
        or waiver.get("scope_and_effect", {}).get("other_m6_gates_remain_independently_required") is not True):
        raise ValueError("Owner-equivalent Pass C provenance/waiver not valid")
    rows = [x for x in progress.get("decks", []) if x.get("deck_id") == deck_id]
    if len(rows) != 1:
        raise ValueError("Missing or duplicated owner-equivalent deck review")
    row = rows[0]
    if (row.get("stage_status") != "FINAL_EVIDENCE_MERGED"
        or not all(row.get(k) is True for k in ("stage_a_complete", "stage_b_complete", "final_complete", "canonical_unchanged"))
        or row.get("owner_swap_approved") is not False
        or row.get("final_evidence_path") != expected["judgment_receipt_path"]
        or not (row.get("canonical_approved_sha256") == seal.get("canonical_input_sha256")
                or registry_bound_digest_discrepancy(row, seal, deck_id))
        or row.get("first_stage_commit_sha") != seal.get("git_first_stage_commit_sha")
        or seal.get("deck_id") != deck_id
        or seal.get("review_class_after_final") != OWNER_EQUIVALENT
        or seal.get("technically_independent") is not False
        or (seal.get("actual_evaluator") != progress["actual_model"]
            and seal.get("actual_evaluator") not in _SEAL_EVALUATOR_SPELLINGS)):
        raise ValueError("Owner-equivalent deck/Stage A seal provenance mismatch")
    for ext in ("md", "json"):
        if content_hash(seal["stage_a_" + ext + "_path"]) != "sha256:" + seal["stage_a_" + ext + "_sha256"]:
            if not (verify_xander_versioned_stage_a_correction(deck_id, seal, ext)
                    or verify_lynde_versioned_stage_a_correction(deck_id, seal, ext)):
                raise ValueError("Stage A source diverged from separately sealed byte commitment")
    final = safe_repo_file(judgment["judgment_receipt_path"]).read_text(encoding="utf-8")
    # Historical owner-equivalent reviews used two explicit negative-independence labels.
    # Accept the actual preserved wordings, never an absent or implied disclosure.
    disclosed_nonindependence = (
        "Technically independent third model" in final
        or "**actual technical independence:** false" in final
        or "**Technically independent:** NO." in final
        or "**Technically independent:** FALSE." in final  # Anhelo__the_Painter preserved wording
        or pass_c_explicit_false_disclosure(final)  # strict pattern, e.g. Ashad__the_Lone_Cyberman
        or pass_c_parenthetical_false_disclosure(final)  # strict parenthetical, e.g. Ashnod_the_Uncaring
        or pass_c_preserved_nonindependence(final, deck_id)  # enumerated per-deck wording, decks #7-#62
    )
    spelling = _PASS_C_PRESERVED_EVALUATOR_SPELLING.get(deck_id)
    if (("ChatGPT/OpenAI GPT-6" not in final and not (spelling and spelling in final))
        or not disclosed_nonindependence
        or row["final_disposition"] not in final):
        raise ValueError("Owner-equivalent final review missing provenance/disposition")
    return True


def validate_bundle(b, registry, seals):
    errors = ga.validate_file(b, "m6_reproducibility_bundle.schema.json")
    if errors:
        raise ValueError("invalid J bundle schema: " + "; ".join(errors[:8]))
    deck = registry["decks"].get(b["deck_id"])
    if not deck or b["slug"] != deck["slug"] or b["baseline_hash"] != deck["current_canonical_hash"]:
        raise ValueError("bundle baseline is not the preserved canonical hash")
    if b["snapshot"]["birthday_id"] != load(ROOT / "data/grixis/birthday_m5/summary.json")["birthday_authority_snapshot"]:
        raise ValueError("bundle Birthday snapshot mismatch")
    for item in b["inputs"]:
        bind(item["path"], item["sha256"])
    if b["sealed_passes"]["a_commit"] != seals["pass_a_commit"] or b["sealed_passes"]["b_commit"] != seals["pass_b_commit"]:
        raise ValueError("A/B committed hashes mismatch")
    bind("data/grixis/m6/sealed/reconciliation_manifest.json",
         b["sealed_passes"]["reconciliation_manifest_sha256"])
    slug = b["slug"]
    for side in ("a", "b"):
        name = b["sealed_passes"][side + "_output_ref"]
        expected = f"data/grixis/m6/sealed/{side.upper()}/{slug}.json"
        if name != expected:
            raise ValueError("sealed pass path mismatch")
        sealed = load(safe_repo_file(name))
        if sealed["pass"]["list_hash"] != b["baseline_hash"]:
            raise ValueError("sealed pass list hash mismatch")
    judgment = b["pass_c"]
    validate_pass_c(judgment, b["deck_id"])
    for t in b["phase_b"]["tests"]:
        bind(t["test_ref"], t["source_sha256"])
        if t["supports_improvement_claim"] and (t["effect_coverage"] != "fully_modeled" or t["verdict"] != "pass"):
            raise ValueError("unmodeled or failing test was promoted as improvement proof")
    for key in ("red_team", "mana_analysis"):
        bind(b[key]["report_path"], b[key]["sha256"])
    for key in ("oracle_ref", "rules_ref", "legality_ref"):
        safe_repo_file(b["snapshot"][key])
    if b["authority"]["can_approve_or_lock"] or b["authority"]["can_decide"]:
        raise ValueError("bundle illegally contains human approval")
    return True


def check():
    reg = load(REGISTRY)
    if len(reg["decks"]) != 62 or reg["program"]["milestones"]["M5"]["status"] != "accepted":
        raise ValueError("M5 authority incomplete")
    seals = load(SEALS)
    if seals["pass_c"]["complete"] is not False:
        raise ValueError("reconciliation manifest may not self-certify Pass C")
    expected = {x["slug"] for x in reg["decks"].values()}
    files = sorted(BUNDLES.glob("*.json")) if BUNDLES.exists() else []
    if len(files) > 62:
        raise ValueError("more than 62 bundles")
    seen = set()
    for p in files:
        bundle = load(p)
        if p.stem != bundle.get("slug") or p.stem not in expected or p.stem in seen:
            raise ValueError("unknown/duplicated final bundle: " + p.name)
        seen.add(p.stem)
        validate_bundle(bundle, reg, seals)
    print(f"M6 J final bundle verification: {len(seen)}/62 valid; {62-len(seen)} pending; no approval authority")
    return len(seen)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", required=True)
    ap.add_argument("--require-complete", action="store_true")
    args = ap.parse_args()
    count = check()
    if args.require_complete and count != 62:
        raise SystemExit("not enough complete bundles for M6 closure")
