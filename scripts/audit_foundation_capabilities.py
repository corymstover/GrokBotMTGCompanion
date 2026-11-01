#!/usr/bin/env python3
"""Fail-closed engineering scope audit; NEVER an owner or release certification.

Confirms five *bounded capabilities* using the already independently generated
source coverage, graph, two chronology ledgers and executed Q&A review packet.
This is deliberately distinct from finishing all historical research or
waiving the unresolved owner/source/release gates.

  python3 scripts/audit_foundation_capabilities.py
  python3 scripts/audit_foundation_capabilities.py --check
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'data/release/foundation_capability_scope_2026-11-01.json'
REPORT = ROOT / 'research/FOUNDATION_CAPABILITY_SCOPE_2026-11-01.md'

NEW_STORY_ARCS = {'BLB', 'DFT', 'DSK', 'ECL', 'EOE', 'LCI', 'MKM', 'MOM', 'OTJ',
                  'TDM', 'WOE'}
REQUIRED_QA = {
    'hard_vito_killer', 'hard_valgavoth_release', 'hard_loot_capture',
    'hard_tamiyo_abduction', 'hard_kellan_father', 'hard_chandra_partner',
    'hard_jace_allies', 'graph_nav_tezzeret_kaladesh',
    'graph_nav_amonkhet_ravnica', 'graph_nav_unknown', 'retcon_bolas',
    'cross_domain_ugin_ineligible', 'cross_domain_bolas_dual_face',
    'cross_domain_blackblade_no_name_bridge', 'cross_domain_unknown_card',
    'cross_domain_black_lotus', 'rules_published_interaction',
    'dual_timeline_bro_exact_source_join', 'dual_timeline_unknown_set',
    'strand_mirrodin_ambiguous', 'strand_bloomburrow_legend',
    'strand_mirrodin_new_phyrexia_explicit',
    'strand_mirrodin_argentum_explicit',
    'unanchored_order', 'karn_origin_identity_bridge',
}


def load(rel: str) -> dict:
    return json.loads((ROOT / rel).read_text(encoding='utf-8'))


def require(ok: bool, reason: str) -> None:
    if not ok:
        raise ValueError('Foundation capability scope failed: ' + reason)


def build() -> dict:
    inventory = load('data/lore_research/story_coverage_inventory_2026-10-30.json')
    graph = load('data/multiverse_graph/multiverse_graph.json')
    timeline = load('data/lore_research/source_event_sequences_2026-10-30.json')
    packet = load('data/release/foundation_acceptance_packet_2026-10-30.json')
    totals, stats = inventory['totals'], graph['stats']
    arcs = {r['arc']: r for r in inventory['arcs']}
    qa = {r['id']: r for r in packet['representative_questions']}
    require(len(qa) == len(packet['representative_questions']), 'duplicate Q&A identifiers')
    require(REQUIRED_QA <= qa.keys(), 'required source/negative/cross-domain Q&A missing')
    require(not packet['owner_accepted'] and not packet['release_certified'] and
            packet['phase6_deckbuilding_deferred'] and
            packet['scope'] == 'KNOWLEDGE_FOUNDATION_ONLY', 'release approval was falsely implied')

    # Covered means cited at least once or explicitly reviewed as no-claim,
    # NOT exhaustively read and NOT all Wizards stories in existence.
    require(totals['pages'] >= 626 and
            totals['cited_pages'] + totals['reviewed_no_claim_pages'] == totals['pages'] and
            totals['arcs_all_cited_or_reviewed'] == totals['arcs'] == len(arcs) >= 33 and
            all(r['review_status'] == 'ALL_PAGES_CITED_OR_REVIEWED' and not r['unreviewed_urls']
                for r in arcs.values()), 'inventory has missing or unreviewed declared pages')
    require(stats['non_wizards_sources'] == 0 and
            stats['claim_edges_with_in_universe_date'] > 0 and
            sum(stats['claims_by_status'].values()) == totals['claims'],
            'graph provenance/date coverage no longer matches cited inventory')

    require(NEW_STORY_ARCS <= arcs.keys(), 'an Omenpaths/later curated arc disappeared')
    require(all(arcs[a]['cited_pages'] > 0 and
                arcs[a]['review_status'] == 'ALL_PAGES_CITED_OR_REVIEWED'
                for a in NEW_STORY_ARCS), 'later arc lacks any cited story or full page triage')

    require(timeline['counts']['verified_legacy_bridges'] >= 8 and
            all(b['relation'] == 'SAME_EVENT' and
                b['source_url'].startswith('https://magic.wizards.com/')
                for b in timeline['legacy_bridges']),
            'cross-ledger history joined without official same-event proof')
    require(len(packet['cross_plane_graph_navigation']) >= 2 and
            all(r['evidence_type'] == 'GRAPH_NAVIGATION_ONLY_NOT_TEMPORAL_OR_CAUSAL_PROOF'
                and r['hops'] for r in packet['cross_plane_graph_navigation']),
            'cross-plane graph navigation overstates historical proof')
    require('CANON_DISPUTED_PRESENT' in qa['retcon_bolas']['flags'] and
            qa['graph_nav_unknown']['confidence'] == 'NOT_FOUND' and
            not qa['graph_nav_unknown']['sources'],
            'retcon/unknown relationship safety has regressed')

    routes = Counter(r['route'] for r in qa.values())
    confidences = Counter(r['confidence'] for r in qa.values())
    require(len(qa) >= 115 and len(routes) >= 12 and
            confidences['VERIFIED'] > 0 and confidences['QUALIFIED'] > 0 and
            confidences['NOT_FOUND'] >= 6 and
            all(r['sources'] or r['confidence'] == 'NOT_FOUND' or
                r['chronology_relation'] == 'UNKNOWN' for r in qa.values()),
            'hard Q&A suite lacks breadth or has an unqualified source-free answer')
    require(qa['strand_mirrodin_ambiguous']['confidence'] == 'NOT_FOUND' and
            'AMBIGUOUS_SOURCE_STRAND' in qa['strand_mirrodin_ambiguous']['flags'] and
            'NARRATED_LEGEND_NOT_VERIFIED_HISTORY' in
            qa['strand_bloomburrow_legend']['flags'],
            'ambiguous/legend chronology flattened into asserted fact')

    cross = [qa[k] for k in sorted(REQUIRED_QA) if k.startswith('cross_domain_')]
    require(len(cross) >= 5 and
            all(r['route'] == 'ask->card_lore_commander_evidence' for r in cross) and
            all(('DATED_SCRYFALL_LEGALITY_NOT_LIVE' in r['flags'] and
                 'GRAPH_NAME_BRIDGE_NOT_DEPICTION_PROOF' in r['flags'])
                for r in cross if r['confidence'] != 'NOT_FOUND') and
            qa['cross_domain_unknown_card']['confidence'] == 'NOT_FOUND' and
            not qa['cross_domain_unknown_card']['sources'] and
            qa['rules_published_interaction']['sources'] and
            'NO_REAL_WORLD_TO_FICTIONAL_TIME_CONVERSION' in
            qa['dual_timeline_bro_exact_source_join']['flags'],
            'integrated card/lore/rules/set searches lost independence or dating')

    report = {
        'schema': 'foundation-capability-scope/v1', 'as_of': '2026-11-01',
        'status': 'BOUNDED_ENGINEERING_CAPABILITIES_VERIFIED_NOT_RELEASE_CERTIFIED',
        'capabilities': {
            'primary_source_inventory_and_integrity': {
                'supported': True, 'pages_in_declared_inventory': totals['pages'],
                'cited_pages': totals['cited_pages'],
                'reviewed_without_claim': totals['reviewed_no_claim_pages'],
                'arcs_accounted_for': totals['arcs_all_cited_or_reviewed'],
            },
            'later_stories_and_omenpaths_curated_scope': {
                'supported': True, 'reviewed_arcs': sorted(NEW_STORY_ARCS),
                'all_inventory_arcs_accounted_for': totals['arcs'],
            },
            'cross_plane_navigation_and_retcon_qualification': {
                'supported': True, 'official_legacy_identity_bridges':
                timeline['counts']['verified_legacy_bridges'],
                'bounded_graph_path_exemplars': len(packet['cross_plane_graph_navigation']),
                'no_cross_strand_total_order': True,
            },
            'hard_lore_and_chronology_qa': {
                'supported': True, 'representative_questions': len(qa),
                'distinct_routes': len(routes),
                'confidence_distribution': dict(sorted(confidences.items())),
            },
            'integrated_card_lore_rules_set_lookup': {
                'supported': True, 'three_domain_probes': len(cross),
                'published_rulings_and_dual_timeline_cases': 2,
                'dated_not_live': True,
            },
        },
        'limitations': [
            'A cited page is not an exhaustive reading or the entire Wizards story corpus.',
            'This verifies retrieval/provenance within the declared scope, not every fictional fact or later release.',
            'Cross-plane graph paths are navigation only; unquoted temporal edges stay UNKNOWN.',
            'Unreviewed Elder Dragon genealogies and source-pending historical set product identities stay open.',
            'Published rules evidence does not simulate gameplay or certify live rulings, Oracle or bans.',
            'Owner acceptance, exact-release CI, current-bulk reconciliation, and 62 protected-deck checks remain separate gates.',
            'Phase 6 deckbuilding and three unapproved pilots remain parked.',
        ],
        'release_certified': False, 'owner_accepted': False,
        'phase6_deckbuilding_deferred': True,
    }
    report['sha256'] = hashlib.sha256(json.dumps(report, sort_keys=True,
                                                   ensure_ascii=False).encode()).hexdigest()
    return report


def markdown(d: dict) -> str:
    c = d['capabilities']
    return '\n'.join([
        '# Foundation v2.95 — bounded engineering capability audit', '',
        '**PRELIMINARY · NOT_RELEASE_READY · not owner acceptance or canon certification.**', '',
        'The following are finite, machine-evidenced **features**, not claims of exhaustive research:', '',
        '| Capability | Evidence |', '| --- | --- |',
        f"| Official primary-source inventory | {c['primary_source_inventory_and_integrity']['pages_in_declared_inventory']} declared pages: {c['primary_source_inventory_and_integrity']['cited_pages']} cited, {c['primary_source_inventory_and_integrity']['reviewed_without_claim']} reviewed without a claim; 33/33 arc buckets accounted for |",
        f"| Later/Omenpaths research within curated scope | {len(c['later_stories_and_omenpaths_curated_scope']['reviewed_arcs'])} named recent arc buckets have cited claims and all inventoried pages triaged |",
        f"| Cross-plane paths and continuity | {c['cross_plane_navigation_and_retcon_qualification']['official_legacy_identity_bridges']} official same-event bridges, {c['cross_plane_navigation_and_retcon_qualification']['bounded_graph_path_exemplars']} independent cited graph path exemplars; no temporal synthesis |",
        f"| Difficult lore/chronology Q&A | {c['hard_lore_and_chronology_qa']['representative_questions']} distinct executable representative questions across {c['hard_lore_and_chronology_qa']['distinct_routes']} routes, including confirmed, qualified and unknown |",
        f"| Joined card/lore/rules and sets | {c['integrated_card_lore_rules_set_lookup']['three_domain_probes']} cross-domain probes, published ruling and two-axis timeline cases; dated and qualified |",
        '', '## Explicitly unfinished or owner-blocked', '',
        *[f'- {item}' for item in d['limitations']], '',
        'Pass means the documented *bounded capability exists* and is reproducible. '
        'It does not make Packs A–C approved, identify unsupported print products, '
        'resolve all in-universe chronology, or permit Phase 6 deck construction.', '',
    ])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    d = build()
    doc = markdown(d)
    if a.check:
        ok = (OUT.is_file() and json.loads(OUT.read_text(encoding='utf-8')) == d and
              REPORT.is_file() and REPORT.read_text(encoding='utf-8') == doc)
        print('PASS bounded foundation capability scope' if ok else 'STALE bounded capability scope')
        return 0 if ok else 1
    OUT.write_text(json.dumps(d, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    REPORT.write_text(doc, encoding='utf-8')
    print('Verified five bounded foundation capabilities; NOT a release certification')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
