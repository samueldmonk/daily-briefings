import re,io,sys
F=[];N=[0]
def chk(cond,msg):
    N[0]+=1
    if not cond: F.append(msg)
def rd(p): return io.open(p,encoding='utf-8').read()
W=rd('wallstreet-briefing.html');C=rd('cyber-briefing.html');M=rd('mma-briefing.html');I=rd('index.html')
PAGES={'ws':W,'cy':C,'mma':M,'idx':I}

# ---- arithmetic: every index read reconciled in Python ----
closes={'sp':7677.28,'dow':53577.40,'ndq':26151.30,'rut':3010.02}
reads=[('sp',7673.94,3.34,0.04),('dow',53468.18,109.22,0.20),('ndq',26100.65,50.65,0.19),('rut',3003.80,6.22,0.21),
       ('sp',7667.22,10.06,0.13),('dow',53433.49,143.91,0.27),('ndq',26055.25,96.05,0.37)]
for k,lvl,chg,pct in reads:
    chk(abs((lvl+chg)-closes[k])<0.02, "%s: %s+%s != prior close %s"%(k,lvl,chg,closes[k]))
    chk(abs(chg/closes[k]*100-pct)<0.006, "%s: pct %.4f vs stated %s"%(k,chg/closes[k]*100,pct))
    chk("{:,.2f}".format(lvl) in W, "%s level %s missing from page"%(k,lvl))
# single names
for name,lvl,chg,pct in [('ANF',144.03,35.12,32.25),('XPON',8.00,2.73,51.80),('INTU',344.53,-12.93,-3.62),
                         ('VIX',15.55,0.10,0.65),('BTC',78349.37,-887.63,-1.12),('GOLD',4650.50,-44.00,-0.94)]:
    prior=lvl-chg
    chk(abs(chg/prior*100-pct)<0.02, "%s pct %.3f vs %s"%(name,chg/prior*100,pct))
chk(abs(344.53+12.93-357.46)<0.01,"INTU prior close mismatch")
chk('357.46' in W,"INTU prior close absent")
chk('3,003.80' in W and '3,010.02' in W,"Russell rows missing")
chk('1:24' in W,"1:24 stamp missing")
chk('2h 36m' in W,"countdown provenance missing")

# ---- structural: TradingView widgets ----
chk(W.count('embed-widget-single-quote.js')==3,"single-quote widgets != 3")
for wid in ['ticker-tape','timeline','stock-heatmap','mini-symbol-overview','events']:
    chk(W.count('embed-widget-%s.js'%wid)==1,"widget %s count != 1"%wid)
chk('tradingview' not in I.lower(),"TradingView on index.html")
tape=re.search(r'embed-widget-ticker-tape\.js" async>(\{.*?\})</script>',W,re.S).group(1)
syms=re.findall(r'"proName":"([^"]+)"',tape)
chk(len(syms)==len(set(syms)),"duplicate tape symbols")
for s in ['FOREXCOM:SPXUSD','FOREXCOM:NSXUSD','FOREXCOM:DJI','TVC:USOIL','TVC:US10Y']:
    chk(s in syms,"mandatory tape symbol %s missing"%s)
chk('NASDAQ:INTU' not in tape,"NASDAQ:INTU back in tape")
cod=re.search(r'embed-widget-mini-symbol-overview\.js" async>(\{.*?\})</script>',W,re.S).group(1)
chk('"symbol":"NYSE:ANF"' in cod,"Chart of the Day not ANF")

# ---- KEV board ----
spans=re.findall(r'<span class="kevdue (ok|crit)">([^<]+)</span>',C)
chk(len(spans)==14,"kevdue spans = %d, expected 14"%len(spans))
ok=[s for s in spans if s[0]=='ok']; crit=[s for s in spans if s[0]=='crit']
chk(len(ok)==4 and len(crit)==10,"kev colour split %d ok / %d crit"%(len(ok),len(crit)))
for col,txt in spans:
    overdue=('past due' in txt) or txt.strip().startswith('0 ')
    chk((col=='crit')==overdue,"kev colour/text disagree: %s / %s"%(col,txt))
def strip(s):
    # HARNESS FIX: tag-stripping alone left HTML entities in the text, so date regexes
    # like r'August\s*27' never matched 'August&nbsp;27'. Normalise entities too.
    s=re.sub(r'<[^>]+>','',s)
    for a,b in [('&nbsp;',' '),('&mdash;',' - '),('&ndash;','-'),('&minus;','-'),
                ('&plus;','+'),('&amp;','&'),('&ldquo;','"'),('&rdquo;','"'),
                ('&rsquo;',"'"),('&#9888;','!'),('&divide;','/')]:
        s=s.replace(a,b)
    return s
# scope the patch-priority block from its own lab to the NEXT lab (blocks exceed 3000 chars
# and do not always close a <section> immediately, which the previous regex assumed)
pp=re.search(r'class="lab">Patch priority</div>([\s\S]*?)(?=<div class="lab">)',C)
chk(pp is not None,"patch priority section missing")
if pp:
    t=strip(pp.group(1))
    chk('Oracle' in t,"patch priority does not name Oracle")
    chk(re.search(r'August\s*27|Aug\.?\s*27',t) is not None,"patch priority Oracle Aug 27 absent")
    chk('CVE-2026-21962' in t,"patch priority CVE absent")
    # the KEV board must carry the same Oracle deadline, compared after tag-stripping
    kevblk=re.search(r'CISA KEV &amp; federal deadlines</div>([\s\S]*?)(?=<div class="lab">)',C)
    chk(kevblk is not None,"KEV block not found")
    if kevblk:
        kt=strip(kevblk.group(1))
        chk('CVE-2026-21962' in kt,"Oracle CVE not on KEV board")
        chk(re.search(r'August\s*27|Aug\.?\s*27',kt) is not None,"Aug 27 not on KEV board")
        chk(re.search(r'August\s*28|Aug\.?\s*28',kt) is not None,"Aug 28 not on KEV board")
chk('Aug&nbsp;27' in C or 'August&nbsp;27' in C,"Aug 27 deadline absent")
chk('Aug&nbsp;28' in C or 'August&nbsp;28' in C,"Aug 28 deadline absent")

# ---- champions board ----
cb=re.search(r'Champions board</div>([\s\S]*?)</table>',M)
chk(cb is not None,"champions board missing")
if cb:
    body=cb.group(1); rows=re.findall(r'<tr>([\s\S]*?)</tr>',body)
    chk(len(rows)==12,"champions rows = %d, expected 12"%len(rows))
    champcol=" ".join(strip(r.split('</td>')[1]) if r.count('</td>')>1 else '' for r in rows)
    for bad in ['Pereira','Chimaev','Topuria','vacant','Vacant']:
        chk(bad not in champcol,"stale champion in board: %s"%bad)
    for good in ['Aspinall','Ulberg','Strickland','Makhachev','Gaethje','Volkanovski','Yan','Van','Shevchenko','Harrison','Dern']:
        chk(good in body,"champion missing: %s"%good)

# ---- nav: five tabs, exactly one active, correct order ----
order=['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html']
selfmap={'ws':'wallstreet-briefing.html','cy':'cyber-briefing.html','mma':'mma-briefing.html','idx':'index.html'}
for k,h in PAGES.items():
    nav=re.search(r'<nav class="tabs">([\s\S]*?)</nav>',h)
    chk(nav is not None,"%s: no nav"%k)
    if nav:
        links=re.findall(r'<a[^>]*href="([^"]+)"[^>]*>',nav.group(1))
        chk(links==order,"%s: nav order %s"%(k,links))
        chk(nav.group(1).count('class="on"')==1,"%s: active tab count"%k)
        act=re.search(r'<a class="on" href="([^"]+)"|<a href="([^"]+)" class="on"',nav.group(1))
        if act: chk((act.group(1) or act.group(2))==selfmap[k],"%s: wrong active tab"%k)

# ---- per-page tldr labels / freshline / countdown ----
chk('<b>The Tape</b>' in W,"ws tldr label"); chk('<b>The Wire</b>' in C,"cy tldr label")
chk('<b>Tale of the Tape</b>' in M,"mma tldr label")
for k,h in [('ws',W),('cy',C),('mma',M)]:
    chk(h.count('class="tldr"')==1,"%s tldr count"%k)
    chk('id="freshline"' in h,"%s freshline"%k)
for k,h in PAGES.items():
    chk('id="datestamp"' in h and 'id="updated"' in h and 'id="edition"' in h,"%s masthead ids"%k)
chk('id="ufccdn"' in M,"mma countdown")

# ---- New-tag hygiene: only 1:40 may be tagged New ----
for k,h in PAGES.items():
    bad=re.findall(r'New (?:&middot;|at) (?!1:40)([0-9:]+)',h)
    chk(not bad,"%s stale New tags: %s"%(k,bad))
chk(W.count('New &middot; 1:40')==4,"ws New tags = %d, expected 4"%W.count('New &middot; 1:40'))
chk(re.search(r'New (&middot;|at) 1:09',W+C+M+I) is None,"1:09 New tag survived")

# ---- index cards summarise their own page's lead ----
chk('7,673.94' in I and '3,003.80' in I,"index mkt card lacks the board")
chk('twenty-third' in I and 'twenty-third' in M,"index/mma edition counter disagree")
chk('14' in I and '10' in I,"index sec card lacks KEV board figures")

# ---- balance ----
for k,h in PAGES.items():
    chk(h.count('<div')==h.count('</div>'),"%s div balance %d/%d"%(k,h.count('<div'),h.count('</div>')))
    chk(h.count('<script')==h.count('</script>'),"%s script balance"%k)
    chk(h.count('<tr>')==h.count('</tr>'),"%s tr balance"%k)
    chk(h.count('<section>')==h.count('</section>'),"%s section balance"%k)

# ---- trap greps ----
traps=["Cody Salkilld","Shamil Yakhyaev","Abdul-Rakhman","slipped 0.12%","Fight Night 286","$1.4 trillion","Suno","No opening level for any index"]
for k,h in PAGES.items():
    for t in traps:
        chk(t not in h,"%s trap string present: %s"%(k,t))
# context-allowed strings must sit inside a rejection note
for s in ["Shanghai Indoor Stadium"]:
    for m in re.finditer(re.escape(s),M):
        win=M[max(0,m.start()-700):m.end()+700]
        chk(('reject' in win.lower()) or ('&#9888;' in win),"%s not in a rejection window"%s)
chk('Oriental Sports Center' in M,"correct venue missing")

print("CHECKS: %d  FAILURES: %d"%(N[0],len(F)))
for f in F: print("  FAIL:",f)
sys.exit(1 if F else 0)
