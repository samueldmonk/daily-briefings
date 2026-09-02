# -*- coding: utf-8 -*-
import re,sys
O="/sessions/amazing-determined-planck/mnt/outputs/"
P={n:open(O+n,encoding='utf-8').read() for n in ["index.html","cyber-briefing.html","wallstreet-briefing.html","mma-briefing.html"]}
fail=[];n=0
def chk(cond,msg):
    global n;n+=1
    if not cond: fail.append(msg)

# --- structural ---
for k,v in P.items():
    chk(v.count('id="edition"')==1,k+": edition pill")
    chk(v.count('id="datestamp"')==1,k+": datestamp pill")
    chk(v.count('id="updated"')==1,k+": updated pill")
    chk(v.count('id="freshline"')==1,k+": freshline")
    for tab in ["index.html","cyber-briefing.html","wallstreet-briefing.html","mma-briefing.html","archive.html"]:
        chk(('href="%s"'%tab) in v,"%s: nav missing %s"%(k,tab))
    chk(v.count('class="on"')==1,k+": exactly one active tab")
    chk(v.rstrip().endswith("</html>"),k+": closes html")
    chk("Intl.DateTimeFormat" in v,k+": self-stamp js")
for k in ["cyber-briefing.html","wallstreet-briefing.html","mma-briefing.html"]:
    chk('class="tldr"' in P[k],k+": tldr strip")
chk('class="tldr"' not in P["index.html"],"index: must not carry tldr strip")

# --- banned relative pointers ---
for k,v in P.items():
    body=v
    if k=="wallstreet-briefing.html":
        body=body.replace("References to earlier editions of this page are written as absolute timestamps (the 8:19 AM, 8:48 AM, 9:18 AM or 9:53 AM edition) rather than as &ldquo;the previous edition,&rdquo;","")
    chk("previous edition" not in body, k+": banned phrase 'previous edition'")
    chk("yesterday" not in body.lower(), k+": banned relative word 'yesterday'")
    chk("last night" not in body.lower(), k+": banned relative 'last night'")

# --- markets guards ---
W=P["wallstreet-briefing.html"]
# Sept 2 levels must not appear as index levels
for bad in ["7,647","7,623","52,756","52,900","28,948","29,127","26,853"]:
    chk(bad not in W,"ws: banned index level "+bad)
# permitted closes only in scorecard region
sc=W.split("<h2>Weekly Scorecard</h2>")[1].split("Rates, Bonds")[0]
for lvl in ["7,631.47","26,099.77","52,766.88","7,686.14","26,370.89","53,185.90"]:
    chk(W.count(lvl)==sc.count(lvl) and sc.count(lvl)>=1,"ws: close %s outside scorecard"%lvl)
# arithmetic on Sept 1 changes
for lo,hi,pct,name in [(7631.47,7686.14,0.71,"S&P"),(26099.77,26370.89,1.03,"Nasdaq"),(52766.88,53185.90,0.79,"Dow")]:
    calc=(hi-lo)/hi*100
    chk(abs(calc-pct)<0.02,"ws: %s pct mismatch %.3f vs %.2f"%(name,calc,pct))
chk(abs((53185.90-52766.88)-419.02)<0.01,"ws: Dow points mismatch")
# every published Sept 2 index move present with clock
for s in ["0.06%","0.37%","1.23%","9:35 AM ET"]:
    chk(s in W,"ws: missing opening-read element "+s)
chk("38,000" in W and "47,000" in W and "46,000" in W,"ws: ADP triple")
chk("4.814%" in W and "4.798%" in W,"ws: both 10-yr reads")
chk("$89.58" in W and "$94.28" in W and "$90.51" in W and "$95.19" in W,"ws: both oil legs")
chk("$4,355" in W and "$64.26" in W,"ws: metals")
# no superlative families
for pat in ["biggest mover","worst megacap","worst large-cap","sharpest reversal","the day's biggest"]:
    chk(pat.lower() not in W.lower(),"ws: banned superlative "+pat)
# no unsourced fed funds
chk("federal funds target" not in W.lower() or "none is published" in W,"ws: fed funds unsourced")
# live blocks A-F
for tok in ["embed-widget-ticker-tape","embed-widget-single-quote","embed-widget-timeline","embed-widget-stock-heatmap","embed-widget-mini-symbol-overview","embed-widget-events"]:
    chk(tok in W,"ws: missing live block "+tok)
chk(W.count("embed-widget-single-quote")==3,"ws: need 3 single-quote widgets")
chk("Quotes stream live" in W,"ws: note line")
# after-hours block must be absent pre-4pm
chk("After-Hours" not in W,"ws: after-hours block must not appear before 4pm ET")

# --- cyber guards ---
C=P["cyber-briefing.html"]
chk("CVE-2026-83548" in C and "CVE-2026-83549" in C,"cy: sonicwall CVEs")
chk("CVSS score of 10" in C or "CVSS 10" in C,"cy: cvss 10")
chk("12.4.3-03526" in C and "12.5.0-02952" in C,"cy: fixed versions")
chk("6210" in C and "7210" in C and "8200v" in C,"cy: affected models")
chk("September 14, 2026" in C and "September 10, 2026" in C,"cy: KEV due dates")
chk('id="kev1"' in C and 'id="kev2"' in C,"cy: KEV countdown spans")
chk("BOD 26-04" in C and "three weeks" in C,"cy: risk-based deadline note")
chk("Patch Priority" in C,"cy: patch priority")
chk("callout crit" in C,"cy: patch priority crit border")
chk("Threat Level: High" in C,"cy: threat banner")
chk(C.count('class="stat"')==4,"cy: 4 stats")
chk("Nevada" not in C,"cy: Nevada 2025 incident must stay excluded")
chk("Aflac" not in C,"cy: Aflac 2025 incident excluded")
chk("first AI model ever" not in C and "no other model" not in C,"cy: Astra overclaim")
chk("vendor grading its own product" in C,"cy: Astra precision guard")
chk("CVE-2026-82329" in C and "CVE-2026-66384" in C and "Disambiguation" in C,"cy: JFrog disambiguation")
# no unsourced CVSS
for m in re.finditer(r'CVSS[^<]{0,30}?(\d\.\d|10)\b',C):
    pass
chk("not sourced this run" in C,"cy: unsourced CVSS column labelled")
chk("9.8" not in C,"cy: no borrowed 9.8 score")

# --- mma guards ---
M=P["mma-briefing.html"]
import re as _re
_champ=_re.findall(r"<tr><td>([^<]+)</td><td>([^<]+)</td>",M.split("Champions Board")[1])
_d=dict(_champ)
chk(_d.get("Middleweight")=="Sean Strickland","mma: MW = Strickland, got %s"%_d.get("Middleweight"))
chk("Chimaev" not in _d.values(),"mma: Chimaev must not hold a belt")
chk(_d.get("Light Heavyweight")=="Carlos Ulberg","mma: LHW cell")
chk(_d.get("Featherweight")=="Alexander Volkanovski","mma: FW cell")
chk(_d.get("Lightweight")=="Justin Gaethje","mma: LW cell")
chk(_d.get("Heavyweight")=="Tom Aspinall","mma: HW cell")
chk(_d.get("Interim Heavyweight")=="Ciryl Gane","mma: interim HW cell")
chk(_d.get("Welterweight")=="Islam Makhachev","mma: WW cell")
chk(_d.get("Bantamweight")=="Petr Yan","mma: BW cell")
chk(_d.get("Flyweight")=="Joshua Van","mma: FlyW cell")
chk(_d.get("Women&rsquo;s Bantamweight")=="Kayla Harrison","mma: WBW cell")
chk(_d.get("Women&rsquo;s Flyweight")=="Valentina Shevchenko","mma: WFlyW cell")
chk(_d.get("Women&rsquo;s Strawweight")=="Mackenzie Dern","mma: WSW cell")
chk(len(_d)==12,"mma: expected 12 champion rows, got %d"%len(_d))
chk("Alex Pereira" not in M.split("Champions Board")[1].split("<h2>")[0].replace("KO2 over Alex Pereira",""),"mma: Pereira not a champion cell")
chk("Alexander Volkanovski" in M,"mma: FW not vacant")
chk("Justin Gaethje" in M,"mma: LW = Gaethje")
chk("Contender Series" in M and "did not come through Dana White" in M,"mma: Parnasse provenance guard")
chk("Salahdine" in M and "Saladhine" not in M,"mma: Parnasse spelling")
chk('id="ufccdn"' in M,"mma: countdown element")
chk("2026-09-05T15:00:00-04:00" in M,"mma: countdown target")
chk("Accor Arena" in M and "12:00 PM ET" in M and "3:00 PM ET" in M,"mma: Paris venue/times")
chk("$100,000" in M and "$25,000" in M,"mma: bonuses")
chk("Nurmagomedov" in M and "Song Yadong" in M,"mma: last event")
# card order guard
mc=M.split("Prelims &mdash; 12:00 PM ET")[0]
pl=M.split("Prelims &mdash; 12:00 PM ET")[1]
chk("Kurtis Campbell" in mc,"mma: Campbell must be MAIN card")
chk("Morgan Charriere" in pl,"mma: Charriere must be PRELIM")
# 14 bouts
chk(M.count("Odds (UFC.com)")==1,"mma: odds table")
chk("Gastelum" in M and "refused" in M,"mma: Gastelum refusal recorded")
chk("biggest surprise" not in M,"mma: banned unsourced superlative")
chk("former champion" not in M.lower() or "KSW" in M,"mma: descriptor guard")
chk("Dariush" not in M,"mma: no stale Dariush claim")

# --- index guards: card summaries must match page tldrs ---
I=P["index.html"]
for frag in ["CVSS 10","0.37%","1.23%","38,000","4.814%","&minus;550","+400","$100,000"]:
    chk(frag in I,"index: summary missing "+frag)
chk("Read the briefing &rarr;" in I and I.count("Read the briefing")==3,"index: 3 read links")
chk(I.count('class="card c-')==3,"index: 3 big cards")

print("CHECKS:",n,"RAISED:",len(fail))
for f in fail: print("  !",f)
sys.exit(1 if fail else 0)
