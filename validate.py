import io,re,json,sys
from html.parser import HTMLParser
files=['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']
VOID={'meta','link','br','img','hr','input','source','wbr'}
class P(HTMLParser):
    def __init__(s):
        super().__init__(convert_charrefs=True); s.stack=[]; s.err=[]
    def handle_starttag(s,t,a):
        if t not in VOID: s.stack.append(t)
    def handle_endtag(s,t):
        if t in VOID: return
        if s.stack and s.stack[-1]==t: s.stack.pop()
        else: s.err.append('mismatch:'+t)
ok=True
for f in files:
    txt=io.open(f,encoding='utf-8').read()
    p=P(); p.feed(txt)
    print(f, 'stack:',len(p.stack),'errs:',len(p.err))
    if p.stack or p.err: ok=False; print('  ',p.stack[:5],p.err[:5])
    # nav + stamps
    for req in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html','id="edition"','id="datestamp"','id="updated"','id="freshline"']:
        if req not in txt: print('  MISSING',req,'in',f); ok=False
# trap greps
traps=['Cody Salkilld','Shamil Yakhyaev','Abdul-Rakhman','54,215','1,036.66','54,124','7,720.01','3:45 PM','unification','Joshua Vance','7,758.21','54,272.60','nine organizations','420 npm','across 420']
allt=''.join(io.open(f,encoding='utf-8').read() for f in files)
for t in traps:
    n=allt.count(t)
    if n: print('TRAP HIT:',t,n); ok=False
# intentional supersession mentions of 1,684
print('1,684 mentions (expect only supersession notes):',allt.count('1,684'))
for m in re.finditer(r'.{60}1,684.{60}',allt): print('  ...'+m.group(0).replace('\n',' ')+'...')
# vacant only in Ulberg line
mma=io.open('mma-briefing.html',encoding='utf-8').read()
for m in re.finditer(r'.{50}[Vv]acant.{50}',mma): print('VACANT ctx: ...'+m.group(0).replace('\n',' ')+'...')
# WS widget JSON
ws=io.open('wallstreet-briefing.html',encoding='utf-8').read()
wid=re.findall(r'embed-widget-[a-z-]+\.js" async>(\{.*?\})</script>',ws,re.S)
print('WS widgets:',len(wid))
for w in wid:
    try: json.loads(w)
    except Exception as e: print('WIDGET JSON FAIL:',e); ok=False
# consistency: 2,234 & 444 counts
print('2,234 count:',allt.count('2,234'),'444 package/pkg mentions:',allt.count('444'))
# Dow close reconciliation
assert abs((54085.88+263.24)-54349.12)<0.001, 'DOW MISMATCH'
print('Dow reconciles to the penny')
# KEV countdowns vs today Aug 5
print('countdown labels:', re.findall(r'(\d+ days? left)', io.open('cyber-briefing.html',encoding='utf-8').read()))
print('OK' if ok else 'PROBLEMS')
