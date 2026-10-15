"""Build "Rules Interactions.md": verbatim Comprehensive Rules (2026-09-25; download the official .txt to .cache/MagicCompRules-20260925.txt or set CR_TXT) + official WotC rulings from the Scryfall rulings bulk. Bot cycle 3."""
import sys,csv,json,gzip,re,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); import ingest_scryfall as ing
R=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..')+'/'
CRURL="https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt"
cr={}
for l in open(os.environ.get('CR_TXT','.cache/MagicCompRules-20260925.txt'),encoding='utf-8'):
    m=re.match(r'^(\d{3}\.\d+[a-z]*)\.? (.*)',l.strip())
    if m and m.group(1) not in cr: cr[m.group(1)]=m.group(2)
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
("Layers & timestamps","613",["613.1","613.1a","613.1b","613.1c","613.1d","613.1e","613.1f","613.1g","613.4","613.4a","613.4b","613.4c","613.4d","613.7"],r'\blayer \d|layers? system|in layer|apply in (the )?(applicable|appropriate) layer',r'wearing|garment',"Continuous effects are applied in seven layers (and sublayers for 1 and 7); within a layer, timestamp order decides unless a dependency exists."),
("Dependency","613.8",["613.8","613.8a","613.8b","613.8c"],r'Humility and Opalescence|Urborg[^.]{0,120}Blood Moon|Blood Moon[^.]{0,120}Urborg|Opalescence[^.]{0,80}Humility',None,"A dependency overrides timestamp order inside the same layer/sublayer. Official card rulings rarely use the word \"dependency\"; the rulings below are the ones in the bulk that settle classic dependency/layer cases (Humility + Opalescence; Blood Moon + Urborg). ⚠️ Any card pair not listed here should be worked through CR 613.8 directly."),
("Replacement effects vs. triggered abilities","614",["614.1","614.1a","603.1","616.1","616.1e","616.1f"],r'replacement effect',None,"A replacement effect modifies an event as it happens (often \"instead\") and never uses the stack; a triggered ability (\"when/whenever/at\") goes on the stack after the event. When several replacement effects apply, the affected object's controller (or the affected player) picks the order."),
("State-based actions","704",["704.3","704.5a"],r'state-based action',None,"SBAs are checked whenever a player would get priority and all applicable ones happen simultaneously; they don't use the stack."),
("Copy effects","707",["707.2","707.2a","707.2b","707.2c"],r'copiable values?|copy effect|enters? (the battlefield )?as a copy|becomes? a copy',None,"Copies take only copiable values (printed values as modified by other copy effects), not counters, Auras, or other effects."),
("Commander: color identity","903.4",["903.4","903.4a","903.4b","903.4c","903.4d","903.4e","903.4f"],r'color identity',r'two commanders|partner',"Color identity is mana symbols in the cost and rules text (plus color indicators/characteristic-defining abilities), including back faces; reminder text is ignored."),
("Commander: returning to the command zone","903.9",["903.9","903.9a","903.9b","903.9c"],r'(put|move|return)[^.]{0,60}(in)?to the command zone|command zone instead|state-based action[^.]*command zone',r'partner|two commanders|dungeon|Undercity',"From graveyard or exile, the owner *may* move the commander to the command zone as a state-based action (so \"dies\"/\"leaves\" triggers still see it go to the graveyard first); from hand or library it's a replacement effect."),
]
def slug(h): h=h.lower(); h=re.sub(r'[^\w\- ]','',h); return h.replace(' ','-')
o=["# Rules Interactions\n",
f"> **Source of truth:** Magic: The Gathering **Comprehensive Rules, effective 2026-09-25** ([official text]({CRURL}), Wizards of the Coast). Rule text below is **quoted verbatim** (long rules trimmed with \"…\"); card rulings are **official WotC rulings** from the Scryfall rulings bulk (2026-10-15), quoted verbatim and linked to the card entries that carry them. Plain-language summaries are labeled **Summary** and are paraphrase, not rules text. Started Bot cycle 3 (issue [#9](https://github.com/corymstover/GrokBotMTGCompanion/issues/9)).\n",
"## Contents"]
for t in topics: o.append(f"- [{t[0]}](#{slug(t[0])}) — CR {t[1]}")
o.append("- [Open questions / next topics](#open-questions--next-topics)\n")
total=0
for name,num,rules,pat,excl,summ in topics:
    o.append(f"## {name}\n")
    o.append(f"**Summary:** {summ}\n")
    for r_ in rules:
        if r_ in cr: o.append(q(r_)); o.append(">")
    if o[-1]==">": o.pop()
    ex=examples(pat,6,excl); total+=len(ex)
    o.append(f"\n**Official rulings that apply these rules** (WotC, most-played cards first by EDHREC rank):\n")
    for _,row,x in ex:
        o.append(f"- {ing.link(row,'')} — *{x['published_at']}* — \"{x['comment']}\"")
    o.append("")
o.append("## Open questions / next topics\n- Next (cycle 4): priority & the stack (CR 117, 405, 608), combat damage assignment (510), protection (702.16), ward (702.21), mutate/merge (702.140, 730), saga & class layers, and a worked example per layer using the card files.\n- ❓ Any rule summary here that disagrees with the quoted text is an error: the quoted CR text wins.")
open(R+'Rules Interactions.md','w').write("\n".join(o)+"\n")
print('topics',len(topics),'rulings quoted',total)
