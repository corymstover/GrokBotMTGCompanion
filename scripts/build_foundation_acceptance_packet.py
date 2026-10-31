#!/usr/bin/env python3
"""Deterministic Phase 8 KNOWLEDGE-ONLY foundation evidence packet.

Builds a bounded review surface from already committed source-graded evidence.
Neither a passing packet nor a passing CI run signifies owner acceptance,
exhaustive lore, a rules simulation or permission to start Phase 6 decks.

  python3 scripts/build_foundation_acceptance_packet.py
  python3 scripts/build_foundation_acceptance_packet.py --check
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path

import mv_ask


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'data/release/foundation_acceptance_packet_2026-10-30.json'
REPORT = ROOT / 'research/FOUNDATION_ACCEPTANCE_PACKET_2026-10-30.md'
INPUTS = {
    'graph': 'data/multiverse_graph/multiverse_graph.json',
    'plane_histories': 'data/lore_research/plane_history_dossiers_2026-10-30.json',
    'chronology': 'data/lore_research/relative_chronology_2026-10-30.json',
    'source_local_chronology': 'data/lore_research/source_event_sequences_2026-10-30.json',
    'story_coverage': 'data/lore_research/story_coverage_inventory_2026-10-30.json',
    'genealogy_disputes': 'data/lore_research/pack_a_genealogy_disputes_2026-10-30.json',
}

# Each route is actually executed; tests cover both supported answers and
# explicit UNKNOWN, retcon and present-day-leader uncertainty. This is a
# representative *sample*, not a claim of open-domain Q&A completeness.
QA_CASES = [
    ('plane_alara', 'What is the history of Alara?', 'ask->plane_history', 'QUALIFIED'),
    ('plane_new_capenna_background', 'What is the historical background of New Capenna?', 'ask->plane_history', 'QUALIFIED'),
    ('character_bolas', 'What is the lore of Nicol Bolas?', 'ask->entity_history', 'QUALIFIED'),
    ('faction_gatewatch', 'What is the history of the Gatewatch?', 'ask->entity_history', 'QUALIFIED'),
    ('faction_izzet_alias', 'What is the history of the Izzet?', 'ask->entity_history', 'QUALIFIED'),
    ('twin_identity', "Who is Ugin's twin?", 'ask->lore:sibling_of|twin_sibling_of', 'VERIFIED'),
    ('confirmed_death', 'Who killed Elesh Norn?', 'ask->lore:killed', 'VERIFIED'),
    ('continuity_caveat', 'Explain the continuity of Ugin', 'ask->continuity', 'QUALIFIED'),
    ('present_leader_unknown', 'Who currently leads the Orzhov Syndicate?',
     'ask->lore:led|leader_of|leads', 'QUALIFIED'),
    ('plain_present_izzet_leader_not_current_proof', 'Who leads the Izzet?',
     'ask->lore:led|leader_of|leads', 'QUALIFIED'),
    ('plain_present_azorius_ruler_not_current_proof', 'Who rules the Azorius?',
     'ask->lore:ruled|led|leader_of|leads', 'QUALIFIED'),
    ('historical_izzet_leader_still_cited', 'Who led the Izzet?',
     'ask->lore:led|leader_of|leads', 'VERIFIED'),
    ('source_order', 'Did Konda imprisons a part happen before Kyodai and Michiko defeat Konda?',
     'ask->chronology', 'QUALIFIED'),
    ('unanchored_order', 'Did Konda imprisons a part happen before Marina lures her bullies?',
     'ask->chronology', 'QUALIFIED'),
    ('commander_identity', 'Can Sol Ring go in a Urza, Lord High Artificer deck?',
     'ask->rules:include', 'VERIFIED'),
    ('set_alpha', 'How many cards are in Alpha?', 'ask->set_atlas:set', 'QUALIFIED'),
    ('card_lotus_printings', 'Which sets was Black Lotus printed in?',
     'ask->set_atlas:card_printings', 'QUALIFIED'),
    ('rules_published_interaction', "How does Urza's Saga interact with Urza's Tower?",
     'ask->rules_evidence:interaction', 'QUALIFIED'),
    ('new_phyrexia_source_order',
     'Did Karn introduces Phyrexian oil to Mirrodin happen before Mirran forces are overwhelmed in the early conquest?',
     'ask->chronology', 'QUALIFIED'),
    ('new_phyrexia_order_unknown',
     'Did P:mirrans_overwhelmed happen before P:venser_restores_karn?',
     'ask->chronology', 'QUALIFIED'),
    ('mercadia_weatherlight_source_order',
     'Did T:weatherlight_seized happen before T:mercadia_strike?',
     'ask->chronology', 'QUALIFIED'),
    ('original_mirrodin_source_order',
     'Did H:karn_creates_argentum happen before H:karn_restores_order?',
     'ask->chronology', 'QUALIFIED'),
    ('mercadia_overlay_order_unknown',
     'Did T:weatherlight_leaves_mercadia happen before T:rath_overlay?',
     'ask->chronology', 'QUALIFIED'),
    ('mirrodin_cross_account_unknown',
     'Did H:karn_restores_order happen before P:mirrans_overwhelmed?',
     'ask->chronology', 'QUALIFIED'),
    ('brothers_war_to_weatherlight',
     'Did R:brothers_war happen before R:weatherlight_thwarts_phyrexia?',
     'ask->chronology', 'QUALIFIED'),
    ('dominarian_damage_to_kamigawa',
     'Did R:dominarian_temporal_fractures happen before R:kami_war_begins?',
     'ask->chronology', 'QUALIFIED'),
    ('karn_origin_identity_bridge',
     'Did C:karn_created happen before U:world_phyrexian_corruption?',
     'ask->chronology', 'QUALIFIED'),
    ('ice_age_urza_discovery_order_unknown',
     'Did R:dominarian_ice_age happen before R:urza_discovers_phyrexia?',
     'ask->chronology', 'QUALIFIED'),
    ('kamigawa_mending_order_unknown',
     'Did R:kami_war_begins happen before R:planeswalkers_mend_rifts?',
     'ask->chronology', 'QUALIFIED'),
    ('karn_2008_profile_equivalence_unknown',
     'Did H:karn_creates_argentum happen before U:karn_creates_world?',
     'ask->chronology', 'QUALIFIED'),
    ('bolas_war_spark_imprisonment_before_escape',
     'Did W:bolas_imprisoned happen before W:bolas_freed?',
     'ask->chronology', 'QUALIFIED'),
    ('bolas_escape_before_ugin_intervention',
     'Did W:bolas_freed happen before W:ugin_grapples?',
     'ask->chronology', 'QUALIFIED'),
    ('brothers_disappearance_before_ajani_report',
     'Did W:brothers_vanish happen before W:ajani_reports?',
     'ask->chronology', 'QUALIFIED'),
    ('meditation_realm_collapse_vs_escaping_bolas_unknown',
     'Did W:meditation_unravels happen before W:bolas_freed?',
     'ask->chronology', 'QUALIFIED'),
    ('ancient_realm_to_post_war_status_unbridged',
     'Did B:ugin_reforms happen before W:bolas_imprisoned?',
     'ask->chronology', 'QUALIFIED'),
    ('history_eric', 'What is the history of Eric Kenrith?', 'ask->entity_history', 'QUALIFIED'),
    ('history_hazel', 'What is the history of Hazel Kenrith?', 'ask->entity_history', 'QUALIFIED'),
    ('history_lyra', 'What is the history of Lyra Dawnbringer?', 'ask->entity_history', 'QUALIFIED'),
    ('history_valentin', 'What is the history of Valentin?', 'ask->entity_history', 'QUALIFIED'),
    ('history_cabaretti', 'What is the history of the Cabaretti?', 'ask->entity_history', 'QUALIFIED'),
    ('plane_argentum', 'What is the history of Argentum?', 'ask->plane_history', 'QUALIFIED'),
    ('plane_eldraine', 'What is the history of Eldraine?', 'ask->plane_history', 'QUALIFIED'),
    ('plane_ikoria', 'What is the history of Ikoria?', 'ask->plane_history', 'QUALIFIED'),
    ('plane_new_capenna', 'What is the history of New Capenna?', 'ask->plane_history', 'QUALIFIED'),
    ('plane_arcavios', 'What is the history of Arcavios?', 'ask->plane_history', 'QUALIFIED'),
    ('plane_vryn', 'What is the history of Vryn?', 'ask->plane_history', 'QUALIFIED'),
    ('plane_serras_realm', "What is the history of Serra's Realm?", 'ask->plane_history', 'QUALIFIED'),
    ('plane_regatha', 'What is the history of Regatha?', 'ask->plane_history', 'QUALIFIED'),
    ('plane_fiora', 'What is the history of Fiora?', 'ask->plane_history', 'QUALIFIED'),
    ('plane_kaldheim', 'What is the history of Kaldheim?', 'ask->plane_history', 'QUALIFIED'),
    ('plane_lorwyn_shadowmoor', 'What is the history of Lorwyn-Shadowmoor?', 'ask->plane_history', 'QUALIFIED'),
    ('plane_thunder_junction', 'What is the history of Thunder Junction?', 'ask->plane_history', 'QUALIFIED'),
    ('plane_bablovia_unset', 'What is the history of Bablovia?', 'ask->plane_history', 'QUALIFIED'),
    ('plane_meditation_realm', 'What is the history of Meditation Realm?', 'ask->plane_history', 'QUALIFIED'),
    ('plane_muraganda', 'What is the history of Muraganda?', 'ask->plane_history', 'QUALIFIED'),
    ('plane_skalla', 'What is the history of Skalla?', 'ask->plane_history', 'QUALIFIED'),
    ('muraganda_magic_before_collapse',
     'Did M:ancient_magic_discovered happen before M:ancient_collapse?',
     'ask->chronology', 'QUALIFIED'),
    ('muraganda_moonfall_order_unknown',
     'Did M:ancient_collapse happen before M:moons_shatter?',
     'ask->chronology', 'QUALIFIED'),
    ('meditation_early_conflict_order',
     'Did B:bolas_attacks happen before B:realm_cataclysm?',
     'ask->chronology', 'QUALIFIED'),
    ('meditation_displacement_order_unknown',
     'Did B:bolas_displaced happen before B:ugin_reforms?',
     'ask->chronology', 'QUALIFIED'),
    ('thran_creator_before_war',
     'Did T:phyrexian_creator_dies happen before T:thran_defeated?',
     'ask->chronology', 'QUALIFIED'),
    ('phyrexia_vs_yawgmoth_outcome_unknown',
     'Did T:old_phyrexia_decimated happen before T:yawgmoth_destroyed?',
     'ask->chronology', 'QUALIFIED'),
    ('serras_realm_historical_order',
     'Did S:urza_flees happen before S:realm_powerstone_collapse?',
     'ask->chronology', 'QUALIFIED'),
    ('serras_realm_radiant_order_unknown',
     'Did S:radiant_assumes_rule happen before S:realm_powerstone_collapse?',
     'ask->chronology', 'QUALIFIED'),
    ('cross_ledger_cited_before',
     'Did B:phyrexia_creator_dies happen before T:rath_constructed?',
     'ask->chronology', 'QUALIFIED'),
    ('cross_ledger_same_event',
     'Did B:phyrexia_portal_closed happen before T:portal_closed?',
     'ask->chronology', 'QUALIFIED'),
    ('cross_ledger_beyond_bridge_unknown',
     'Did B:phyrexia_creator_dies happen before T:yawgmoth_destroyed?',
     'ask->chronology', 'QUALIFIED'),
]


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding='utf-8'))


def sha(body: dict) -> str:
    return hashlib.sha256(json.dumps(body, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def qa_cases() -> list[dict]:
    if len({case[0] for case in QA_CASES}) != len(QA_CASES):
        raise ValueError('Duplicate foundation Q&A identifiers would silently overwrite review evidence')
    rows = []
    for key, question, route, confidence in QA_CASES:
        r = mv_ask.ask(question)
        if (r['route'], r['confidence']) != (route, confidence):
            raise ValueError(f'Q&A evidence drift for {key}: {r["route"]}, {r["confidence"]}')
        if key == 'unanchored_order' and (r['result']['relation'] != 'UNKNOWN' or r['sources']):
            raise ValueError('Unanchored chronology was falsely answered or sourced')
        if key == 'source_order' and r['result']['relation'] != 'BEFORE':
            raise ValueError('Source-grounded chronology no longer supported')
        if key == 'new_phyrexia_source_order' and (r['result']['relation'] != 'BEFORE' or
                                                  len(r['result']['proof']) != 4):
            raise ValueError('New Phyrexia source-local order lost its cited path')
        if key == 'new_phyrexia_order_unknown' and (
                r['result']['relation'] != 'UNKNOWN' or r['sources']):
            raise ValueError('New Phyrexia unordered events falsely linked')
        if key in {'mercadia_weatherlight_source_order','original_mirrodin_source_order'} and (
                r['result']['relation'] != 'BEFORE' or not r['result']['proof'] or
                'https://magic.wizards.com/en/news/feature/known-mutliverse-2008-03-19' not in r['sources']):
            raise ValueError(f'Mercadia/Mirrodin chronology lost cited source path for {key}')
        if key in {'mercadia_overlay_order_unknown','mirrodin_cross_account_unknown'} and (
                r['result']['relation'] != 'UNKNOWN' or r['sources'] or
                'NO_CITED_CHRONOLOGY_PATH' not in r['flags']):
            raise ValueError(f'Unproven historic sequence falsely answered for {key}')
        if key in {'brothers_war_to_weatherlight','dominarian_damage_to_kamigawa'} and (
                r['result']['relation'] != 'BEFORE' or not r['result']['proof'] or not r['sources']):
            raise ValueError(f'Source-backed cross-plane and long-history path lost: {key}')
        if key == 'karn_origin_identity_bridge' and (
                r['result']['relation'] != 'BEFORE' or
                'CROSS_LEDGER_SOURCE_BRIDGED' not in r['flags'] or
                'https://magic.wizards.com/en/story/karn-planeswalker' not in r['sources']):
            raise ValueError('Karn origin chronology lacks explicit sourced same-event identity')
        if key in {'ice_age_urza_discovery_order_unknown',
                   'kamigawa_mending_order_unknown',
                   'karn_2008_profile_equivalence_unknown'} and (
                r['result']['relation'] != 'UNKNOWN' or r['sources'] or
                'NO_CITED_CHRONOLOGY_PATH' not in r['flags']):
            raise ValueError(f'Unsupported broad-history ordering was falsely inferred: {key}')
        if key in {'muraganda_magic_before_collapse','meditation_early_conflict_order'} and (
                r['result']['relation'] != 'BEFORE' or not r['result']['proof'] or not r['sources']):
            raise ValueError(f'New source-local order lacks cited path for {key}')
        if key in {'muraganda_moonfall_order_unknown','meditation_displacement_order_unknown'} and (
                r['result']['relation'] != 'UNKNOWN' or r['sources']):
            raise ValueError(f'Unsupported source-local order falsely linked for {key}')
        if key in {'thran_creator_before_war','serras_realm_historical_order'} and (
                r['result']['relation'] != 'BEFORE' or not r['result']['proof'] or not r['sources']):
            raise ValueError(f'Legacy historical source-local path regressed for {key}')
        if key in {'phyrexia_vs_yawgmoth_outcome_unknown','serras_realm_radiant_order_unknown'} and (
                r['result']['relation'] != 'UNKNOWN' or r['sources']):
            raise ValueError(f'Unsupported first-invasion/Serra order falsely inferred for {key}')
        if key == 'cross_ledger_cited_before' and (
                r['result']['relation'] != 'BEFORE' or
                'CROSS_LEDGER_SOURCE_BRIDGED' not in r['flags'] or not r['sources']):
            raise ValueError('Proven cross-ledger ordering lost its source bridge')
        if key == 'cross_ledger_same_event' and (
                r['result']['relation'] != 'SAME_EVENT' or
                'CROSS_LEDGER_SOURCE_BRIDGED' not in r['flags'] or r['result']['answer'] is not None):
            raise ValueError('Source-equivalent events falsely ordered')
        if key == 'cross_ledger_beyond_bridge_unknown' and (
                r['result']['relation'] != 'UNKNOWN' or r['sources'] or
                'CROSS_LEDGER_UNANCHORED' not in r['flags']):
            raise ValueError('Unproven cross-ledger sequence falsely answered')
        if key == 'present_leader_unknown' and 'CURRENT_LEADER_NOT_ESTABLISHED' not in r['flags']:
            raise ValueError('Present-day leadership is overstated')
        if key == 'commander_identity' and not r['result']['allowed']:
            raise ValueError('Known Commander identity regression')
        if key == 'set_alpha' and (r['result']['distinct_identities_or_unresolved'] != 290 or
                                   r['result']['printing_records'] != 295):
            raise ValueError('Set Atlas identity/printing distinction drift')
        if key == 'card_lotus_printings' and (
                r['result']['cards'][0]['first_recorded_printing_date'] != '1993-08-05' or
                r['result']['cards'][0]['printing_record_count'] != 13):
            raise ValueError('Historical card-printing evidence drift')
        if key == 'rules_published_interaction' and not any(
                "doesn't interact" in x['text'] for x in r['result']['direct_rulings']):
            raise ValueError('Published ruling interaction evidence drift')
        if route.endswith('history') and (r['result']['complete_history'] or
                                         r['result']['verified_total_chronology']):
            raise ValueError('History route claims unsupported completeness')
        if key.startswith('plane_') and r['result']['direct_claims'] < 5:
            raise ValueError(f'Thin-plane history evidence regressed for {key}')
        if key == 'plane_bablovia_unset' and (
                'ALTERNATE_CONTINUITY_PRESENT' not in r['flags'] or
                sum(item['grade'] == 'ALTERNATE_CONTINUITY' for item in r['result']['claims']) < 4):
            raise ValueError('Bablovia Un-set continuity was erased from foundation answer')
        result = r.get('result', {})
        urls = set(r.get('sources', []))
        # The rules answer uses a separate cited-rule envelope, not `sources`.
        if r.get('rules_source', {}).get('url'):
            urls.add(r['rules_source']['url'])
        rows.append({
            'id': key, 'question': question, 'route': route, 'confidence': confidence,
            'flags': r.get('flags', []),
            'sources': sorted(urls),
            'response_sha256': sha(r),
            'direct_claims': result.get('direct_claims'),
            'chronology_relation': result.get('relation'),
            'known_limitations': result.get('known_gaps', []),
        })
    return rows


def cross_plane_navigation(graph: mv_ask.MG) -> list[dict]:
    # These are evidence-linked GRAPH PATHS, not a proof that the path is a
    # chronological, causal, geographical or canonical travel sequence.
    exemplars = [('tezzeret_kaladesh', 'character:tezzeret', 'plane:kaladesh'),
                 ('elspeth_new_phyrexia', 'character:elspeth_tirel', 'plane:new_phyrexia')]
    rows = []
    for key, first, last in exemplars:
        path = graph.path(first, last)
        if not path or not all(p['claim'] and p['source_urls'] for p in path):
            raise ValueError(f'Cross-plane navigation lost cited path: {key}')
        rows.append({'id': key, 'from': graph.nodes[first]['name'],
                     'to': graph.nodes[last]['name'],
                     'evidence_type': 'GRAPH_NAVIGATION_ONLY_NOT_TEMPORAL_OR_CAUSAL_PROOF',
                     'hops': path})
    return rows


def build() -> dict:
    inputs = {key: load(path) for key, path in INPUTS.items()}
    graph, planes, chronology, local, coverage = (inputs[k] for k in
        ('graph', 'plane_histories', 'chronology', 'source_local_chronology', 'story_coverage'))
    if graph['content_sha256'] != planes['source_graph_sha256']:
        raise ValueError('Plane history dossiers were not built from this exact graph')
    if chronology['counts']['cycles']:
        raise ValueError('Cited chronology contains a directed cycle')
    mg = mv_ask.graph()
    if mg.g['content_sha256'] != graph['content_sha256']:
        raise ValueError('Q&A graph differs from foundation evidence graph')
    entities = {nid for nid, n in mg.nodes.items() if n['type'] in {'Character', 'Faction'}}
    direct = {nid: set() for nid in entities}
    for edge in mg.g['edges']:
        if edge.get('claim') and edge['relation'] not in mv_ask.STRUCTURAL:
            for nid in (edge['from'], edge['to']):
                if nid in direct:
                    direct[nid].add(edge['claim'])
    entity_types = Counter(mg.nodes[nid]['type'] for nid in entities)
    cc, lc, pc = chronology['counts'], local['counts'], planes['counts']
    body = {
        'schema': 'foundation-acceptance-packet/v1', 'as_of': '2026-10-30',
        'status': 'RESEARCH_EVIDENCE_FOR_OWNER_REVIEW_NOT_CERTIFICATION',
        'scope': 'KNOWLEDGE_FOUNDATION_ONLY',
        'owner_accepted': False, 'release_certified': False,
        'phase6_deckbuilding_deferred': True,
        'input_sha256': {key: {'path': path,
                               'sha256': hashlib.sha256((ROOT / path).read_bytes()).hexdigest()}
                         for key, path in INPUTS.items()},
        'coverage': {
            'source_pages_in_inventoried_scope': coverage['totals']['pages'],
            'source_pages_cited': coverage['totals']['cited_pages'],
            'source_pages_reviewed_without_claim': coverage['totals']['reviewed_no_claim_pages'],
            'graph_nodes': len(graph['nodes']), 'graph_edges': len(graph['edges']),
            'graph_claims': sum(graph['stats']['claims_by_status'].values()),
            'registered_plane_nodes': pc['registered_planes'],
            'thin_plane_dossiers': pc['thin_planes_fewer_than_five_claims'],
            'curated_context_plane_count': pc['planes_with_curated_context'],
            'distinct_existing_context_claims': pc['distinct_contextual_claims'],
            'registered_character_nodes': entity_types['Character'],
            'registered_faction_nodes': entity_types['Faction'],
            'characters_and_factions_with_direct_claims': sum(bool(x) for x in direct.values()),
            'characters_and_factions_without_direct_claims': sum(not x for x in direct.values()),
            'registered_character_faction_direct_claim_gaps': sorted(nid for nid, claims in direct.items()
                                                                    if not claims),
        },
        'chronology': {
            'legacy_events': cc['event_nodes'], 'legacy_ordered_pairs': cc['comparable_pairs'],
            'legacy_total_pairs': cc['total_pairs'],
            'legacy_unresolved_pairs': cc['total_pairs'] - cc['comparable_pairs'],
            'legacy_disconnected_components': cc['components'],
            'legacy_cycles': cc['cycles'],
            'source_local_events': lc['events'], 'source_local_ordered_pairs': lc['ordered_pairs'],
            'source_local_total_pairs': lc['total_pairs'],
            'not_additive': 'Legacy and source-local data are separately scoped; their pairs may not be summed as one chronology.',
            'l244_complete': chronology['l244_closure'].get('complete', False),
        },
        'representative_questions': qa_cases(),
        'cross_plane_graph_navigation': cross_plane_navigation(mg),
        'unresolved_gates': [
            'Quoted relative ordering does not yet establish a complete cross-source or cross-plane chronology.',
            'Plane histories and direct character/faction claims are incomplete, not a census of Magic canon.',
            'Pack A genealogy disputes GD2–GD7 require source-backed resolution or explicit owner decisions.',
            'No general game-state simulation or proof for uncited complex card interactions exists.',
            'Phase 1B qualified snapshot limits and release-time Oracle freshness require separate review.',
            'Actual owner foundation-scope acceptance and exact-release CI have not occurred.',
        ],
        'validation_commands': [
            'python3 scripts/build_foundation_acceptance_packet.py --check',
            "python3 -m unittest discover -s tests -p 'test_foundation_acceptance_packet.py' -q",
            "python3 -m unittest discover -s tests -p 'test_mv_ask*.py' -q",
            'python3 scripts/certification_dry_run.py --check',
            'python3 scripts/update_multiverse_progress_tracker.py --check',
        ],
        'owner_review_status': 'PENDING_NOT_REQUESTED_UNTIL_ENGINEERING_EVIDENCE_AND_CI_COMPLETE',
    }
    body['content_sha256'] = sha(body)
    return body


def markdown(p: dict) -> str:
    cov, chron = p['coverage'], p['chronology']
    lines = [
        '# Knowledge-foundation evidence for owner review — 2026-10-30', '',
        '**Status: PRELIMINARY / NOT A CERTIFICATION / NOT OWNER ACCEPTED.**', '',
        'This source-graded packet is reproducible from the repository, with exact input hashes. '
        'It is a bounded acceptance *review surface*, not a claim to know all Magic history. '
        'Phase 6 deckbuilding and its three pilots remain deferred.', '',
        '## Inventory and supported lookups', '',
        f'- {cov["source_pages_cited"]} official source pages cited and {cov["source_pages_reviewed_without_claim"]} reviewed without a claim '
        f'within the inventoried {cov["source_pages_in_inventoried_scope"]}-page scope. Citation does not mean exhaustive reading.',
        f'- {cov["graph_claims"]} source-graded graph claims across {cov["graph_nodes"]} nodes; '
        f'{cov["registered_plane_nodes"]} registered planes, {cov["thin_plane_dossiers"]} still thin.',
        f'- {cov["registered_character_nodes"]} registered characters and {cov["registered_faction_nodes"]} factions; '
        f'{cov["characters_and_factions_with_direct_claims"]} with direct cited claims, '
        f'{cov["characters_and_factions_without_direct_claims"]} without.',
        f'- {cov["distinct_existing_context_claims"]} previously researched on-plane contextual claims in '
        f'{cov["curated_context_plane_count"]} dossiers, strictly distinct from new/direct graph claims.', '',
        '## In-universe chronology (not a complete timeline)', '',
        f'- Legacy ledger: {chron["legacy_events"]} events, {chron["legacy_ordered_pairs"]}/{chron["legacy_total_pairs"]} '
        f'ordered event pairs; {chron["legacy_unresolved_pairs"]} unresolved, '
        f'{chron["legacy_disconnected_components"]} components, {chron["legacy_cycles"]} cycles.',
        f'- Source-local ledger: {chron["source_local_events"]} events, '
        f'{chron["source_local_ordered_pairs"]}/{chron["source_local_total_pairs"]} pairs. '
        'These counts are separate, not additive.',
        '- L244 cross-source historical ordering remains open. UNKNOWN is the correct answer when no cited bridge exists.', '',
        '## Representative end-to-end questions', '',
        '| Question | Route | Confidence | Cited URLs |', '| --- | --- | --- | ---: |',
    ]
    for q in p['representative_questions']:
        lines.append(f'| {q["question"]} | `{q["route"]}` | `{q["confidence"]}` | {len(q["sources"])} |')
    lines += ['', 'The underlying JSON retains response digests, exact source URLs and caveat flags. '
              'The two graph-navigation examples are **not** evidence of chronological or causal paths.', '',
              '## Still open before foundation certification', '']
    lines += [f'- {gap}' for gap in p['unresolved_gates']]
    lines += ['', '## Reproduce', '', '```bash', *p['validation_commands'], '```', '',
              f'Packet SHA-256 (canonical JSON): `{p["content_sha256"]}`', '',
              '**No decks were built, modified, reviewed or approved.**', '']
    return '\n'.join(lines)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--check', action='store_true')
    args = ap.parse_args(argv)
    p = build()
    js = json.dumps(p, indent=2, ensure_ascii=False) + '\n'
    md = markdown(p)
    if args.check:
        good = OUT.is_file() and OUT.read_text(encoding='utf-8') == js and \
               REPORT.is_file() and REPORT.read_text(encoding='utf-8') == md
        print('PASS foundation evidence packet' if good else 'STALE foundation evidence packet')
        return 0 if good else 1
    OUT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(js, encoding='utf-8')
    REPORT.write_text(md, encoding='utf-8')
    print(f'Wrote foundation evidence packet: {len(p["representative_questions"])} representative Q&A cases; NOT CERTIFIED')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
