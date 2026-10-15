"""Build "Rules Interactions.md": verbatim Comprehensive Rules (2026-09-25; download the official .txt to .cache/MagicCompRules-20260925.txt or set CR_TXT) + official WotC rulings from the Scryfall rulings bulk. Bot cycles 3–4. CR "Example:" paragraphs (official) are attached to the rule they follow."""
import sys,csv,json,gzip,re,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); import ingest_scryfall as ing
R=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')+'/'
CRURL="https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt"
cr={}; crex={}; last=None; body=False
for l in open(os.environ.get('CR_TXT','.cache/MagicCompRules-20260925.txt'),encoding='utf-8'):
    s=l.strip()
    if s=='Glossary' and len(cr)>2000: break
    m=re.match(r'^(\d{3}\.\d+[a-z]*)\.? (.*)',s)
    if m:
        if m.group(1) not in cr: cr[m.group(1)]=m.group(2)
        last=m.group(1)
    elif s.startswith('Example:') and last: crex.setdefault(last,[]).append(s[len('Example:'):].strip())
idx=list(csv.DictReader(open(R+'data/card_index.csv')))
byoid={r['oracle_id']:r for r in idx}
def rank(r):
    try: return int(r['edhrec_rank'])
    except: return 10**9
rul={}
for l in gzip.open(R+'.cache/rulings-20261015090033.jsonl.gz','rt'):
    x=json.loads(l)
    if x['oracle_id'] in byoid and x.get('source')=='wotc': rul.setdefault(x['oracle_id'],[]).append(x)
def examples(pat,n=6,excl=None):
    out=[]
    for oid,rs in rul.items():
        for x in rs:
            if re.search(pat,x['comment'],re.I) and not (excl and re.search(excl,x['comment'],re.I)):
                out.append((rank(byoid[oid]),byoid[oid],x)); break
    out.sort(key=lambda t:t[0]); seen=set(); res=[]
    for e in out:
        k=e[2]['comment'][-60:]
        if k in seen: continue
        seen.add(k); res.append(e)
    return res[:n]
def q(num,full=False):
    t=cr[num]
    if not full and len(t)>420: t=t[:420].rsplit(' ',1)[0]+' …'
    return f"> **CR {num}** — {t}"
topics=[
("Layers & timestamps","613",["613.1","613.1a","613.1b","613.1c","613.1d","613.1e","613.1f","613.1g","613.4","613.4a","613.4b","613.4c","613.4d","613.7"],r'\blayer \d|layers? system|in layer|apply in (the )?(applicable|appropriate) layer',r'wearing|garment',"Continuous effects are applied in seven layers (and sublayers for 1 and 7); within a layer, timestamp order decides unless a dependency exists.",[]),
("Dependency","613.8",["613.8","613.8a","613.8b","613.8c"],r'Humility and Opalescence|Urborg[^.]{0,120}Blood Moon|Blood Moon[^.]{0,120}Urborg|Opalescence[^.]{0,80}Humility',None,"A dependency overrides timestamp order inside the same layer/sublayer. Official card rulings rarely use the word \"dependency\"; the rulings below are the ones in the bulk that settle classic dependency/layer cases (Humility + Opalescence; Blood Moon + Urborg). ⚠️ Any card pair not listed here should be worked through CR 613.8 directly.",[]),
("Replacement effects vs. triggered abilities","614",["614.1","614.1a","603.1","616.1","616.1e","616.1f"],r'replacement effect',None,"A replacement effect modifies an event as it happens (often \"instead\") and never uses the stack; a triggered ability (\"when/whenever/at\") goes on the stack after the event. When several replacement effects apply, the affected object's controller (or the affected player) picks the order.",[]),
("State-based actions","704",["704.3","704.5a"],r'state-based action',None,"SBAs are checked whenever a player would get priority and all applicable ones happen simultaneously; they don't use the stack.",[]),
("Copy effects","707",["707.2","707.2a","707.2b","707.2c"],r'copiable values?|copy effect|enters? (the battlefield )?as a copy|becomes? a copy',None,"Copies take only copiable values (printed values as modified by other copy effects), not counters, Auras, or other effects.",[]),
("Commander: color identity","903.4",["903.4","903.4a","903.4b","903.4c","903.4d","903.4e","903.4f"],r'color identity',r'two commanders|partner',"Color identity is mana symbols in the cost and rules text (plus color indicators/characteristic-defining abilities), including back faces; reminder text is ignored.",[]),
("Commander: returning to the command zone","903.9",["903.9","903.9a","903.9b","903.9c"],r'(put|move|return)[^.]{0,60}(in)?to the command zone|command zone instead|state-based action[^.]*command zone',r'partner|two commanders|dungeon|Undercity',"From graveyard or exile, the owner *may* move the commander to the command zone as a state-based action (so \"dies\"/\"leaves\" triggers still see it go to the graveyard first); from hand or library it's a replacement effect.",[]),
("Worked layer examples (official CR examples)","613",[],r'Humility and Opalescence|layer 7[a-d]|layer 1|layer 4',None,"Every example below is an **official Example paragraph from the CR**, printed under the rule it illustrates; they are the safest worked layer cases because Wizards wrote them.",["613.4c","613.4d","613.5","613.6","613.7a","613.8a","613.9"]),
("Stack & priority","117 / 405 / 608",["117.1a","117.3a","117.3b","117.3c","117.3d","117.4","405.1","405.2","405.5","405.6","608.2b"],r'in response|holds? priority|while (it|that ability|the ability) is on the stack',None,"The active player gets priority first; a player who casts a spell or activates an ability gets priority again afterward (117.3c). The top object of the stack resolves only when all players pass in succession (117.4, 405.5). Some things don't use the stack (405.6). On resolution a spell or ability rechecks its targets; if all are illegal it doesn't resolve (608.2b).",[]),
("Casting vs. copying a spell","601 / 707.10 / 707.12",["601.2","601.2a","601.2f","601.2h","601.2i","707.10","707.10a","707.10c","707.12"],r"(isn't|wasn't|aren't|is not) cast|cast a copy|copy of (a|the|that) spell",None,"A copy of a spell put onto the stack **isn't cast** (707.10), so \"whenever you cast\" triggers don't see it; it copies modes, targets, X and costs paid. An effect that says **cast a copy** follows casting steps 601.2a–h and the copy **is** cast (707.12).",["707.10"]),
("Combat damage assignment","510",["510.1","510.1a","510.1b","510.1c","510.1d","510.1e","510.2","510.4","702.7b"],r'assigns? (its )?combat damage|combat damage step',None,"Each creature assigns combat damage equal to its power; a blocked creature divides damage among its blockers as its controller chooses (510.1c), and all combat damage is dealt simultaneously (510.2). First or double strike creates an extra combat damage step (510.4).",["510.1c"]),
("Deathtouch + trample","702.2 / 702.19",["702.2b","702.2c","702.19b","702.19c"],r'deathtouch[^.]*trample|trample[^.]*deathtouch',None,"With deathtouch, any nonzero combat damage assigned to a creature counts as lethal for assigning excess (702.2c), so a deathtouch + trample attacker needs to assign only 1 damage to each blocker and can assign the rest to the player, planeswalker or battle (702.19b).",["702.19b","702.19c"]),
("Protection","702.16",["702.16a","702.16b","702.16c","702.16d","702.16e","702.16f","702.16j","702.16k"],r'protection from',r'phas',"Protection from a quality means: can't be targeted by spells/abilities with that quality, enchanted or equipped by such Auras/Equipment, blocked by such creatures (when attacking), and damage from such sources is prevented (702.16b–f).",[]),
("Hexproof, shroud & ward","702.11 / 702.18 / 702.21",["702.11b","702.11c","702.11d","702.11e","702.18a","702.21a","702.21b"],r'\bward\b|hexproof|shroud',None,"Hexproof stops targeting by spells/abilities **opponents** control (702.11b); shroud stops targeting by **any** player (702.18a); ward is a **triggered ability** that counters an opponent's spell or ability targeting the permanent unless they pay the cost (702.21a) — so it uses the stack and can be responded to.",[]),
("ETB / LTB & look-back triggers","603.6 / 603.10",["603.2","603.6a","603.6c","603.6d","603.10","603.10a"],r'leaves the battlefield|look(s)? back in time|last known information',None,"Enters-the-battlefield triggers check the battlefield after the event, including the newcomers (603.6a). Leaves-the-battlefield triggers \"look back in time\" (603.10a), so they see the game as it was just before the permanent left. \"Enters with …\" / \"enters tapped\" text is a static ability, not a triggered ability; its effect happens as part of the event (603.6d).",["603.10a"]),
("Mutate & merged permanents","702.140 / 730",["702.140a","702.140b","702.140c","702.140d","702.140e","730.2","730.2a","730.2b","730.2c","730.3"],r'\\bmutates?\\b|mutating|merged (creature|permanent)',None,"A mutating creature spell with a legal target doesn't enter the battlefield; it merges with the target (702.140c). The merged permanent is the **same object** it was before — it hasn't just come under your control and existing effects keep applying (730.2c) — and uses the characteristics of its topmost component (730.2a) plus all abilities of every component (702.140e).",[]),
("Commander tax","903.8",["903.8"],r'commander tax|additional \{2\}|cast (it )?from the command zone',r'partner|two commanders',"Casting your commander from the command zone costs {2} more for each previous time **you** cast it from the command zone this game (903.8); casts from anywhere else don't count.",[]),
]
def slug(h): h=h.lower(); h=re.sub(r'[^\w\- ]','',h); return h.replace(' ','-')
o=["# Rules Interactions\n",
f"> **Source of truth:** Magic: The Gathering **Comprehensive Rules, effective 2026-09-25** ([official text]({CRURL}), Wizards of the Coast). Rule text below is **quoted verbatim** (long rules trimmed with \"…\"); card rulings are **official WotC rulings** from the Scryfall rulings bulk (2026-10-15), quoted verbatim and linked to the card entries that carry them. Plain-language summaries are labeled **Summary** and are paraphrase, not rules text. Started Bot cycle 3, extended Bot cycle 4 (issue [#9](https://github.com/corymstover/GrokBotMTGCompanion/issues/9)).\n",
"## Contents"]
for t in topics: o.append(f"- [{t[0]}](#{slug(t[0])}) — CR {t[1]}")
o.append("- [Open questions / next topics](#open-questions--next-topics)\n")
total=0; crx=[0]
for name,num,rules,pat,excl,summ,exr in topics:
    o.append(f"## {name}\n")
    o.append(f"**Summary:** {summ}\n")
    for r_ in rules:
        if r_ in cr: o.append(q(r_)); o.append(">")
    if o and o[-1]==">": o.pop()
    exs=[(r_,e) for r_ in exr for e in crex.get(r_,[])]
    if exs:
        o.append(f"\n**Official CR examples** ({len(exs)}):\n")
        for r_,e in exs: o.append(f"- *CR {r_} example* — {e}")
        crx[0]+=len(exs)
    ex=examples(pat,6,excl); total+=len(ex)
    o.append(f"\n**Official rulings that apply these rules** (WotC, most-played cards first by EDHREC rank):\n")
    for _,row,x in ex:
        o.append(f"- {ing.link(row,'')} — *{x['published_at']}* — \"{x['comment']}\"")
    o.append("")
o.append("## Open questions / next topics\n- Next: sagas & classes (714, 717), phasing (702.26), double-faced cards & transform (712, 701.27), the legend rule (704.5j), \"can't\" vs. \"can\" (101.2), and replacement-effect ordering worked examples (616).\n- ❓ Any rule summary here that disagrees with the quoted text is an error: the quoted CR text wins.")
open(R+'Rules Interactions.md','w').write("\n".join(o)+"\n")
print('topics',len(topics),'rulings quoted',total,'CR examples',crx[0])
