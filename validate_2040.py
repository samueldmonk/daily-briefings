import re, sys, subprocess
FILES = ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']
BRIEFS = FILES[1:]
S = {f: open(f).read() for f in FILES}
fails=[]; checks=0
STAMP = sys.argv[1]

def ck(cond, msg):
    global checks; checks+=1
    if not cond: fails.append(msg)

def has(f, sub, n=None):
    c = S[f].count(sub)
    ck(c>0 if n is None else c==n, f"{f}: {sub[:70]!r} count={c} expected={n or '>0'}")

def no(f, sub):
    ck(sub not in S[f], f"{f}: FORBIDDEN present {sub[:70]!r}")

# --- structure: five-tab nav, masthead ids, self-stamp ---
for f in FILES:
    for href in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html']:
        has(f, f'href="{href}"')
    for i in ['id="edition"','id="datestamp"','id="updated"','id="freshline"']:
        has(f, i)
    has(f, "America/New_York")
    has(f, "briefings refresh every 30 minutes")
    ck(S[f].count('class="on"')==1, f"{f}: exactly one active tab")

# --- fresh stamp everywhere; stale stamps forbidden ---
for f in FILES:
    ck(S[f].count(STAMP) >= 2, f"{f}: stamp {STAMP} appears {S[f].count(STAMP)}x, need >=2")
for stale in ["8:31 PM","5:15 PM ET","1:45 PM ET","1:35 PM ET","6:35 PM ET"]:
    for f in FILES:
        seg = S[f][:S[f].find('</header>')+400]
        ck(stale not in seg, f"{f}: stale stamp {stale} in masthead/freshline region")

# --- tldr strips ---
for f, label in [('cyber-briefing.html','The Wire'),('wallstreet-briefing.html','The Tape'),('mma-briefing.html','Tale of the Tape')]:
    has(f, '<div class="tldr">', 1)
    has(f, f'<b>{label}</b>')

# --- TradingView blocks: WS only ---
WIDGETS = ['embed-widget-ticker-tape.js','embed-widget-single-quote.js','embed-widget-timeline.js',
           'embed-widget-stock-heatmap.js','embed-widget-mini-symbol-overview.js','embed-widget-events.js']
for w in WIDGETS: has('wallstreet-briefing.html', w)
for f in ['index.html','cyber-briefing.html','mma-briefing.html']:
    for w in WIDGETS: no(f, w)
for sym in ['TVC:USOIL','TVC:US10Y','FOREXCOM:SPXUSD','FOREXCOM:NSXUSD','FOREXCOM:DJI','NASDAQ:PYPL']:
    has('wallstreet-briefing.html', sym)

# --- market closes (Friday Aug 28, re-verified this run) ---
for v in ['7,711.76','26,402.42','53,559.99','0.25%','0.52%','9.45']:
    has('wallstreet-briefing.html', v)
no('wallstreet-briefing.html','7,673.04')
no('wallstreet-briefing.html','as of ~')
no('wallstreet-briefing.html','After-Hours Movers')
# Dow points/percent reconciliation
ck(abs(9.45/53569.44*100 - 0.02) < 0.005, "Dow points/percent reconciliation")
# weekly figures
for v in ['first winning week in three']: has('wallstreet-briefing.html', v)
# advanced counter
has('wallstreet-briefing.html','<b>fifteenth</b> time this run',1)
has('wallstreet-briefing.html','<b>fifth consecutive</b> check of that breadth',1)
no('wallstreet-briefing.html','<b>fourteenth</b> time this run')
no('wallstreet-briefing.html','<b>fourth consecutive</b> check of that breadth')
# rates family
for v in ['4.73','4.34','5.20','CME FedWatch']: has('wallstreet-briefing.html', v)
# time-of-day prose still true at publish
has('wallstreet-briefing.html','Saturday evening')
no('wallstreet-briefing.html','It is <b>Saturday morning</b>')

# --- index mirrors the WS tldr counter ---
has('index.html','<b>fifteenth</b> time this run',1)
no('index.html','<b>fourteenth</b> time this run')

# --- cyber: KEV board, sixth check, standing caveats ---
C='cyber-briefing.html'
for cve in ['CVE-2026-53362','CVE-2023-49105','CVE-2026-66384','CVE-2026-8452','CVE-2019-1068']:
    has(C, cve)
has(C,'BOD 26-04')
has(C,'A sixth check at 8:35 PM returned no CISA alert dated later than August 27',1)
has(C,'A fifth check at 6:20 PM')
no(C,'A sixth check at 9:01 PM')
# Oracle CVE never carried in a table row
oid='CVE-2026-21962'
for m in re.finditer(re.escape(oid), S[C]):
    seg = S[C][max(0,m.start()-600):m.start()+600]
    ck('not carried' in seg or 'not being carried' in seg, f"{C}: {oid} lacks not-carried frame")
    row_open = S[C].rfind('<tr', 0, m.start()); row_close = S[C].rfind('</tr>', 0, m.start())
    ck(row_close >= row_open, f"{C}: {oid} appears inside a table row")
# ServiceNow status separation
for m in re.finditer('CVE-2026-6875', S[C]):
    ck('exploited' in S[C][max(0,m.start()-420):m.start()+420], f"{C}: 6875 missing exploited status")
# Unitree: no CVSS may attach
for uid in ['CVE-2026-76640','CVE-2026-76639']:
    has(C, uid)
    for m in re.finditer(re.escape(uid), S[C]):
        seg = S[C][max(0,m.start()-200):m.start()+200]
        ck(not re.search(r'CVSS\s*\d', seg), f"{C}: a CVSS was attached to {uid}")
has(C,'UniBLEed')
# TITAN 700GB must sit near the not-validated caveat
for m in re.finditer('700GB', S[C]):
    seg = S[C][max(0,m.start()-700):m.start()+700]
    seg_l = seg.lower()
    ck(('independently validated' in seg_l) or ('own marketing' in seg_l)
       or ('own claim' in seg_l) or ('own advertisement' in seg_l),
       f"{C}: 700GB lacks marketing/not-validated framing")
# collective-defence letter: range, never a single number
has(C,'116'); has(C,'130')
for bad in ['signed by 116 companies','128 organisations in total','exactly 130']:
    no(C, bad)
# CVE well-formedness + liveness
cves = set(re.findall(r'CVE-\d{4}-\d{4,6}', S[C]))
ck(len(cves) >= 15, f"{C}: only {len(cves)} distinct CVEs")
for c in cves: ck(re.fullmatch(r'CVE-\d{4}-\d{4,6}', c) is not None, f"malformed {c}")

# --- MMA: champions board rows, forbidden affirmatives ---
M='mma-briefing.html'
CHAMPS = ['Tom Aspinall','Ciryl Gane','Carlos Ulberg','Sean Strickland','Islam Makhachev',
          'Justin Gaethje','Alexander Volkanovski','Petr Yan','Joshua Van',
          'Valentina Shevchenko','Kayla Harrison','Mackenzie Dern']
for c in CHAMPS: has(M, c)
for bad in ['Pereira</b></td>','champion Khamzat Chimaev','Khamzat Chimaev</b></td>',
            'featherweight title is vacant','vacant featherweight title']:
    no(M, bad)
for m in re.finditer('vacant', S[M]):
    seg = S[M][max(0,m.start()-300):m.start()+300]
    ok = any(k in seg for k in ['Ulberg','Prochazka','Procházka','Topuria','not vacant',
                                'Volkanovski','not a vacancy','An absence in a listing'])
    ck(ok, f"{M}: unframed 'vacant' at {m.start()}")
ck('former champion Beneil Dariush' not in S[M] and 'title challenger Beneil Dariush' not in S[M],
   f"{M}: Dariush descriptor")
# Shanghai results figures upheld last run
for v in ['Song Yadong','Umar Nurmagomedov','UFC 333','October 24']: has(M, v)
has(M,'2:28'); has(M,'4:14')
for m_ in re.finditer(r'(?<![\d:])4:03(?![\d])', S[M]):
    seg = S[M][max(0,m_.start()-400):m_.start()+400]
    ck('not 4:03' in seg or 'at <b>4:03</b>' in seg or 'Neither figure was adopted' in seg,
       f"{M}: 4:03 appears without a rejection frame at {m_.start()}")
ck(re.search(r'<td[^>]*>[^<]*4:03', S[M]) is None, f"{M}: 4:03 appears in a results-table cell")
# bonus family
has(M,'$25,000'); has(M,'$400,000')
has(M,'did not receive one of the four $100,000 awards')
no(M,'Denise Gomes did not receive a bonus')
# countdown
has(M,'ufccdn')
ck(('September 5' in S[M]) or ('Sept 5' in S[M]), f"{M}: next-card date Sept 5 missing")

# --- footers: sources present, absolute, unique ---
for f in BRIEFS:
    fi = S[f].rfind('<footer')
    ck(fi != -1, f"{f}: no <footer>")
    foot = S[f][fi:]
    hrefs = re.findall(r'href="([^"]+)"', foot)
    ext = [h for h in hrefs if not h.endswith('.html')]
    ck(len(ext) >= 5, f"{f}: only {len(ext)} source links in footer")
    for h in ext: ck(h.startswith('http'), f"{f}: non-absolute footer href {h}")
    ck(len(ext) == len(set(ext)), f"{f}: duplicate footer hrefs")
    ck('class="disc"' in foot, f"{f}: no .disc disclaimer block in footer")

print(f"validate: {checks} checks, {len(fails)} failures")
for x in fails: print("  FAIL:", x)
sys.exit(1 if fails else 0)
