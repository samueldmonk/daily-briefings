# -*- coding: utf-8 -*-
import io,re,sys
P={"cy":"cyber-briefing.html","ws":"wallstreet-briefing.html","mma":"mma-briefing.html","ix":"index.html"}
S={k:io.open(v,encoding="utf-8").read() for k,v in P.items()}
A_CY=io.open("archive/cyber-2026-09-07-1813.html",encoding="utf-8").read()
A_WS=io.open("archive/wallstreet-2026-09-07-1813.html",encoding="utf-8").read()
A_MM=io.open("archive/mma-2026-09-07-1813.html",encoding="utf-8").read()
n=0; fails=[]
def ck(cond,msg):
    global n; n+=1
    if not cond: fails.append(msg)
def has(k,t,c=None):
    if c is None: ck(t in S[k], "%s missing: %s"%(k,t[:70]))
    else: ck(S[k].count(t)==c, "%s count!=%d (%d): %s"%(k,c,S[k].count(t),t[:70]))
def no(k,t): ck(t not in S[k], "%s must not contain: %s"%(k,t[:70]))

# --- structural balance ---
for k,s in S.items():
    for tag in ("div","p","table","tr","td","h2","h3","span","ul","li"):
        o=len(re.findall(r"<%s[ >]"%tag,s)); c=len(re.findall(r"</%s>"%tag,s))
        ck(o==c,"%s unbalanced <%s>: %d open %d close"%(k,tag,o,c))
# --- nav / masthead / stamp ---
for k in P:
    for href in ("index.html","cyber-briefing.html","wallstreet-briefing.html","mma-briefing.html","archive.html"):
        has(k,'href="%s"'%href)
    for i in ("id=\"edition\"","id=\"datestamp\"","id=\"updated\"","America/New_York"):
        has(k,i)
for k in ("cy","ws","mma"): has(k,'class="tldr"'); has(k,'id="freshline"')
has("cy","<b>The Wire</b>"); has("ws","<b>The Tape</b>"); has("mma","<b>Tale of the Tape</b>")
# --- TradingView blocks ---
for w in ("embed-widget-ticker-tape.js","embed-widget-single-quote.js","embed-widget-timeline.js",
          "embed-widget-stock-heatmap.js","embed-widget-mini-symbol-overview.js","embed-widget-events.js"):
    has("ws",w)
has("ws","embed-widget-single-quote.js",3)
for sym in ("FOREXCOM:SPXUSD","FOREXCOM:NSXUSD","FOREXCOM:DJI","TVC:USOIL","TVC:US10Y"): has("ws",sym)
has("mma","ufccdn")
# --- champions board, cell-anchored, four banned regressions ---
for c in ("Tom Aspinall","Carlos Ulberg","Sean Strickland","Islam Makhachev","Justin Gaethje",
          "Alexander Volkanovski","Petr Yan","Joshua Van"): has("mma",c)
for bad in ("<td><b>Alex Pereira</b></td>","<td><b>Khamzat Chimaev</b></td>",
            "<td><b>Ilia Topuria</b></td>","<td><b>Valentina Shevchenko</b></td>"): no("mma",bad)
# --- NEW: cyber Liquid Network item ---
for t in ("Liquid Network","Blockstream","4,000 BTC","3,400 BTC","598.5","$268 million","$47 million",
          "federation wallet","peg-out","4,200 BTC","we are whitehats","95%"): has("cy",t)
for t in ("Liquid Network","Blockstream","598.5","peg-out"): ck(t not in A_CY,"cy tagged token present in 1813: %s"%t)
ck("Liquid" in A_CY,"expected bare 'Liquid' collision in 1813 snapshot (Nexcess and Liquid Web)")
has("cy","Nexcess and Liquid Web")
# no CVE/deadline invented for it
has("cy","no CVE, no CVSS, no affected version, no vendor patch and no KEV")
# --- NEW: BOD 26-04 correction ---
for t in ("3, 14 or 60 calendar days","one of five remediation tiers","10 June 2026","7 August 2026",
          "public exposure, KEV status, exploit automation","14 days for vulnerabilities assigned a CVE after 2021",
          "titled as revoked"): has("cy",t)
no("cy","supersede BOD 22-01&rsquo;s uniform three weeks")
ck("3, 14 or 60" not in A_CY,"BOD windows already in 1813")
ck("BOD 26-04" in A_CY,"BOD 26-04 should be carried, not tagged")
# --- deadlines unchanged & consistent ---
has("cy","14 September"); has("cy","7 days left"); no("cy","6 days left"); no("cy","8 days left")
for d in ("Due Wednesday 16 September 2026","due Friday 18 September 2026","Due Saturday 5 September 2026"): has("cy",d)
# --- new-tag ledger: 2 / 0 / 0 ---
ck(S["cy"].count('class="t new"')==2,"cy New tags != 2 (%d)"%S["cy"].count('class="t new"'))
ck(S["ws"].count('class="t new"')==0,"ws New tags != 0")
ck(S["mma"].count('class="t new"')==0,"mma New tags != 0")
for k in ("cy","ws","mma"): has(k,"<b>2</b> cyber + <b>0</b> markets + <b>0</b> MMA = <b>2</b>")
no("cy",'<span class="t new" style="margin-right:6px">New</span> CVE-2026-51693')
# --- markets: zero-new claim proved, clock rewritten, stale figures banned ---
for t in ("Brent $97.89","WTI $92.30","162,000","53,000","58%"):
    ck(t in A_WS,"ws claimed-carried token absent from 1813: %s"%t)
    has("ws",t)
has("ws","about half an hour in the past")
has("ws","ninth consecutive edition")
no("ws","about five hours in the past")
no("ws","minutes after it")
no("ws","minutes before this edition publishes")
has("ws","no New tag is attached anywhere on it")
has("ws","No level is asserted for the reopened tape")
# Brent refusal counter advanced
ck(S["ws"].count("thirty-fourth consecutive edition")==2,"ws Brent counter != 2")
has("ix","thirty-fourth consecutive edition")
no("ws","thirty-third"); no("ix","thirty-third")
has("ws","$97.93")
# --- MMA: fifth zero, champions trap refused, carried tokens proved present ---
has("mma","<b>fifth</b> consecutive sweep")
no("mma","<b>fourth</b> consecutive sweep")
for t in ("Tracy Cortez","UFC&nbsp;329","14-fight","Namajunas","Mick Parkin","Johnny Walker"):
    ck(t in A_MM or t.replace("&nbsp;"," ") in A_MM,"mma claimed-carried token absent from 1813: %s"%t)
has("mma","All three are refused.")
has("mma","third firing of")
has("mma","Alexa Grasso")
# --- index cards sync ---
has("ix","$320 million"); has("ix","598.5"); has("ix","BOD 22-01"); has("ix","3, 14 or 60 calendar days")
has("ix","<b>fifth</b> consecutive sweep returned nothing new")
has("ix","about half an hour in the past")
no("ix","<b>fourth</b> consecutive sweep")
for k in ("cy","ws","mma","ix"): no(k,"6:35&nbsp;PM edition&rsquo;s")
# --- demotion of prior self-references ---
for k in ("cy","ws","mma","ix"):
    no(k,"in this 6:05&nbsp;PM edition"); no(k,"this 6:05&nbsp;PM ET edition")
has("ix","<b>The item new at 6:05&nbsp;PM was the smallest entry on the page:</b>")
# --- grammar / defect bans ---
for k in ("cy","ws","mma","ix"):
    for b in (" in in "," the the "," a a ","item the "):
        no(k,b)
# --- disclaimers ---
has("ws","investment advice"); has("mma","subject to change")
# --- sources present ---
has("cy","coindesk.com/markets/2026/09/07"); has("cy","news.bitcoin.com"); has("cy","tenable.com/blog/cisa-bod-26-04")
has("cy","fedtechmagazine.com"); has("cy","runzero.com/blog/bod-26-04")
print("CHECKS: %d  FAILURES: %d"%(n,len(fails)))
for f in fails: print("  -",f)
sys.exit(1 if fails else 0)
