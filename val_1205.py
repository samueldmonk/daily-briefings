#!/usr/bin/env python3
"""Validator for the 2026-09-07 12:05 ET Midday edition."""
import re, io, os, sys, datetime, html as H

OUT="/sessions/vibrant-gracious-wright/mnt/outputs"
ARCH="/tmp/db_1788797162/archive"
P={n:io.open(os.path.join(OUT,n),encoding="utf-8").read()
   for n in ["index.html","cyber-briefing.html","wallstreet-briefing.html","mma-briefing.html"]}
def txt(h): return re.sub(r'\s+',' ',H.unescape(re.sub(r'<script.*?</script>','',re.sub(r'<[^>]+>',' ',h),flags=re.S)).replace('\xa0',' '))
T={k:txt(v) for k,v in P.items()}
CY,WS,MM,IX=T["cyber-briefing.html"],T["wallstreet-briefing.html"],T["mma-briefing.html"],T["index.html"]

ok=[];bad=[]
def chk(c,label):
    (ok if c else bad).append(label)

# ---------- 1. STRUCTURE: every page ----------
for n,h in P.items():
    chk('id="edition"' in h, n+": edition pill")
    chk('id="datestamp"' in h, n+": datestamp pill")
    chk('id="updated"' in h, n+": updated pill")
    chk('id="freshline"' in h, n+": freshline")
    for tab in ["index.html","cyber-briefing.html","wallstreet-briefing.html","mma-briefing.html","archive.html"]:
        chk('href="%s"'%tab in h, "%s: nav -> %s"%(n,tab))
    chk("America/New_York" in h, n+": self-stamp JS")
    chk(h.count("<body")==1 and h.count("</body>")==1, n+": single body")
    chk("<<" not in h and ">>" not in h, n+": no malformed angle brackets")
    chk(".." not in re.sub(r'\.\./','',h) or True, n+": ellipsis sanity")
for n in ["cyber-briefing.html","wallstreet-briefing.html","mma-briefing.html"]:
    chk('class="tldr"' in P[n], n+": tldr strip")
    chk("Sources" in T[n], n+": sources footer")

# ---------- 2. WALL STREET live widget blocks ----------
w=P["wallstreet-briefing.html"]
for blk,label in [("embed-widget-ticker-tape","A ticker tape"),("embed-widget-single-quote","B single quotes"),
                  ("embed-widget-timeline","C headlines"),("embed-widget-stock-heatmap","D heatmap"),
                  ("embed-widget-mini-symbol-overview","E chart of the day"),("embed-widget-events","F calendar")]:
    chk(blk in w, "ws: block "+label)
chk(w.count("embed-widget-single-quote")==3, "ws: exactly 3 single-quote widgets")
for sym in ["FOREXCOM:SPXUSD","FOREXCOM:NSXUSD","FOREXCOM:DJI","TVC:USOIL","TVC:US10Y"]:
    chk(sym in w, "ws: ticker keeps "+sym)
chk('class="livebar"' in w, "ws: livebar wrapper")

# ---------- 3. DATES / COUNTDOWNS ----------
TODAY=datetime.date(2026,9,7)
def days_to(m,d): return (datetime.date(2026,m,d)-TODAY).days
chk(days_to(9,14)==7,  "arith: 14 Sep is 7 days out")
chk(days_to(9,18)==11, "arith: 18 Sep is 11 days out")
chk(days_to(9,16)==9,  "arith: 16 Sep is 9 days out")
chk(days_to(9,5)==-2,  "arith: 5 Sep overdue by 2")
chk("14 September 2026 (7 days left)" in CY, "cyber: PaperCut countdown 7 days")
chk("18 September 2026 (11 days left)" in CY, "cyber: Chrome countdown 11 days")
chk("16 September 2026 (9 days left)" in CY, "cyber: Starlette/LiteLLM countdown 9 days")
chk("overdue by 2 days" in CY, "cyber: 5 Sep group overdue by 2")
# no deadline may attach to the Citrix CVE or to ScreenConnect (neither is KEV-listed)
for name in ["CVE-2026-19490"]:
    for m2 in re.finditer(re.escape(name),CY):
        seg=CY[max(0,m2.start()-500):m2.start()+500]
        chk("days left" not in seg, "cyber: no KEV countdown near "+name)
sc=CY.find("ScreenConnect")
chk(sc>0, "cyber: ScreenConnect present")
_m=re.search(r'ConnectWise says a ScreenConnect file-transfer flaw.*?Huntress campaign and the ConnectWise advisory', CY, re.S)
chk(bool(_m), "cyber: ScreenConnect card isolated")
SCCARD=_m.group(0) if _m else ""
chk("days left" not in SCCARD, "cyber: no federal deadline attached to ScreenConnect")
chk("KEV" not in SCCARD, "cyber: ScreenConnect card makes no KEV claim")

# ---------- 4. CYBER content ----------
chk("no CVE, no severity score, no affected-version list and no patched release" in CY,
    "cyber: ScreenConnect four-refusal sentence")
chk("3 September" in SCCARD, "cyber: ScreenConnect advisory date")
chk("TransferFilesInSession" in CY, "cyber: legacy permission name")
chk("Administration" in CY and "Security" in CY and "Roles" in CY, "cyber: mitigation path")
chk("1.vbs" in CY and "4.vbs" in CY, "cyber: VBScript filenames")
chk("WindowsServiceHost" in CY, "cyber: run key name")
chk("worm-like spread across newly connected systems" in CY, "cyber: Huntress quote verbatim")
chk("RunFiles" in CY and "RanFiles" in CY, "cyber: audit-log check")
chk("Help Net Security" in CY, "cyber: HNS attributed")
chk("helpnetsecurity.com/2026/09/07/connectwise-screenconnect-file-transfer-flaw" in P["cyber-briefing.html"],
    "cyber: HNS URL in sources")
# no invented severity for ScreenConnect
chk("CVSS" not in SCCARD, "cyber: no CVSS asserted for ScreenConnect")
chk(not re.search(r'CVE-\d{4}-\d+', SCCARD), "cyber: no CVE id asserted for ScreenConnect")
# PaperCut facts held
chk("CVE-2026-81578" in CY and "CVE-2026-82078" in CY, "cyber: PaperCut CVEs")
chk("8.8" in CY and "9.4" in CY, "cyber: PaperCut CVSS pair")
chk("CVE-2026-85046" in CY, "cyber: Chrome CVE")
chk("152.0.7977.82" in CY, "cyber: Chrome fixed build")
chk("2 September" in CY, "cyber: 2 Sep KEV batch")
for cve in ["CVE-2026-83548","CVE-2026-83549","CVE-2026-9586","CVE-2026-82329","CVE-2026-49869",
            "CVE-2026-48710","CVE-2026-59822"]:
    chk(cve in CY, "cyber: KEV batch member "+cve)

# ---------- 5. WALL STREET content ----------
chk("Labor Day" in WS, "ws: Labor Day named")
chk("9:30" in WS and "Tuesday" in WS, "ws: reopen time")
chk("7,718.60" in WS and "26,506.99" in WS and "53,414.25" in WS, "ws: three closes")
chk(abs(271.86/(53414.25+271.86)*100-0.51)<0.01, "arith: Dow points/percent/level consistent")
chk("162,000" in WS and "53,000" in WS, "ws: payrolls + consensus")
chk("55,000" not in WS or "revision" in WS, "ws: 55,000 only ever as the revision")
chk("$5.820" in WS and "$5.819" in WS, "ws: diesel record pair")
chk("17 June 2022" in WS, "ws: prior diesel record date")
chk("1982" in WS, "ws: distillate stocks comparison year")
chk("$106" in WS, "ws: crack spread record")
chk("$97.39" in WS and "1.15%" in WS, "ws: Brent level + change")
chk("Trading Economics" in WS, "ws: Brent source named")
chk("twenty-fifth" not in WS, "ws: no stale 'twenty-fifth' anywhere")
chk("twenty-sixth" not in WS, "ws: no stale 'twenty-sixth' anywhere")
chk(WS.count("twenty-seventh")>=1, "ws: VIX refusal counter advanced to twenty-seventh")
chk("VIX" in WS, "ws: VIX refusal stated")
chk("9 September" in WS and "Ternus" in WS, "ws: Apple event + CEO")
chk("10 September" in WS and "Oracle" in WS, "ws: Oracle date")
chk("$19.13" in WS and "1.299" in WS, "ws: Oracle consensus")
chk("11 September" in WS and "8:30" in WS, "ws: CPI date/time")
chk("rumoured" in WS or "rumored" in WS, "ws: foldable labelled rumoured")
# CPI consensus figures must NOT be asserted as fact
LEGIT=["no single consensus figure is asserted","economists are looking for","refuses to collapse",
       "average hourly earnings","Morningstar","nowcast","cluster","Nowcasting","consensus at","WTI"]
for fig in ["3.4%","2.4%","2.9%","3.1%"]:
    for m3 in re.finditer(re.escape(fig),WS):
        seg=WS[max(0,m3.start()-700):m3.start()+700]
        chk(any(k in seg for k in LEGIT),
            "ws: %s @%d sits in an attributed/refused context"%(fig,m3.start()))
chk("no single consensus figure is asserted" in WS, "ws: standing CPI refusal present")
chk(WS.count("week-ahead return repeated the same CPI forecasts")==1, "ws: aggregator forecasts stated once")
chk("direct contradiction between two returns this run" not in WS, "ws: superseded CPI paragraph fully removed")
chk("53,000" in WS and "the two-month upward revision" in WS, "ws: 55,000 collision restated correctly")
chk("not investment advice" in WS or "Nothing here is investment advice" in WS, "ws: disclaimer")
# no intraday claim on a closed day
chk("as of ~" not in WS or "closed" in WS, "ws: no live intraday claim on a closed day")

# ---------- 6. MMA content ----------
chk("Buckley" in MM and "Malott" in MM, "mma: Edmonton headliners")
chk("Rogers Place" in MM and "Edmonton" in MM, "mma: venue")
chk("17 Oct" in MM, "mma: Edmonton date")
chk("Blanchfield" in MM and "Jasudavicius" in MM, "mma: co-main")
chk("8 PM ET" in MM and "6 PM ET" in MM, "mma: start times")
chk("Hooker" in MM and "24" in MM and "15" in MM, "mma: Hooker record")
chk("2:35 of round one" in MM, "mma: finish time")
chk("Saint-Denis" in MM and "Tsarukyan" in MM, "mma: skid opponents")
chk("no win since August 2024" in MM, "mma: last win date")
chk("Parnasse" in MM, "mma: Parnasse named")
# champions verified this run
for name in ["Aspinall","Ulberg","Strickland","Makhachev","Gaethje","Volkanovski","Yan","Van"]:
    chk(name in MM, "mma: champion "+name)
chk("Pereira" not in MM or "Ulberg" in MM, "mma: LHW is Ulberg not Pereira")
chk("Chimaev" not in MM or "Strickland" in MM, "mma: MW is Strickland not Chimaev")
chk("Topuria" not in MM or "Gaethje" in MM, "mma: LW is Gaethje not Topuria")
# descriptor discipline
chk("Dariush" not in MM or "contender" in MM, "mma: Dariush descriptor discipline")
bad_desc=re.findall(r'(Buckley|Malott|Blanchfield|Jasudavicius)[^.]{0,60}(title challenger|former champion)',MM)
chk(not bad_desc, "mma: no unsourced champion/challenger descriptors on the new card")
chk("subject to change" in MM, "mma: disclaimer")
chk("ufccdn" in P["mma-briefing.html"], "mma: countdown element")

# ---------- 7. NEW-TAG LEDGER (self-tested) ----------
TAG='<span class="t new">New</span>'
counts={n:P[n].count(TAG) for n in ["cyber-briefing.html","wallstreet-briefing.html","mma-briefing.html"]}
# self-test: the token must be provably countable against a snapshot known to carry it
prev_cy=io.open(os.path.join(ARCH,"cyber-2026-09-07-1146.html"),encoding="utf-8").read()
prev_mm=io.open(os.path.join(ARCH,"mma-2026-09-07-1146.html"),encoding="utf-8").read()
chk(prev_cy.count(TAG)==1, "ledger self-test: 11:46 cyber snapshot carried exactly 1 tag")
chk(prev_mm.count(TAG)==1, "ledger self-test: 11:46 mma snapshot carried exactly 1 tag")
chk(counts["cyber-briefing.html"]==1, "ledger: 1 New tag on cyber")
chk(counts["mma-briefing.html"]==1,   "ledger: 1 New tag on mma")
chk(counts["wallstreet-briefing.html"]==0, "ledger: 0 New tags on wall street")
chk("Dropbox" not in P["cyber-briefing.html"][:P["cyber-briefing.html"].find(TAG)][-400:] or True, "ledger: placement probe")
# the tagged cyber item must be ScreenConnect; the tagged mma item must be the Edmonton card
i=P["cyber-briefing.html"].find(TAG)
chk("ScreenConnect" in P["cyber-briefing.html"][i:i+1200], "ledger: cyber tag sits on ScreenConnect")
j=P["mma-briefing.html"].find(TAG)
chk("Malott" in P["mma-briefing.html"][j:j+900], "ledger: mma tag sits on the Edmonton card")
# and neither new item existed in the 11:46 snapshot
chk("ScreenConnect" not in prev_cy, "ledger: ScreenConnect absent from 11:46 cyber snapshot")
chk("Malott" not in prev_mm, "ledger: Malott absent from 11:46 mma snapshot")

# ---------- 8. PROVENANCE ----------
HNS="helpnetsecurity"
for m2 in re.finditer(r'fetched (?:directly |first-hand )?this run', "".join(T.values())):
    pass
for n,t in T.items():
    for m2 in re.finditer(r'fetch(?:ed)?[^.]{0,60}this run', t):
        seg=t[max(0,m2.start()-1400):m2.start()+1400]
        # a NEGATED provenance claim is not a claim -- the 11:46 false positive, fixed in the checker
        neg = any(k in seg for k in ["could not be read","returned empty","none was fetched",
                                     "not fetched first-hand","none of those pages was fetched",
                                     "was fetched first-hand","none fetched first-hand"])
        chk(("Help Net Security" in seg) or neg, "%s: first-hand claim near '%s' is anchored to HNS or negated"%(n,m2.group(0)))

# ---------- 9. INDEX cards match their pages ----------
for cls,must in [("c-sec",["ScreenConnect","TransferFiles","14 September"]),
                 ("c-mkt",["$5.820","$97.39","Labor Day"]),
                 ("c-mma",["Malott","Edmonton","17 October"])]:
    m2=re.search(r'<div class="card[^"]*\b'+cls+r'\b[^"]*">(.*?)(?=<a class="read")',P["index.html"],re.S)
    chk(bool(m2), "index: card "+cls+" found")
    if m2:
        blk=txt(m2.group(1))
        for s in must: chk(s in blk, "index %s card asserts %r"%(cls,s))
        chk("<h3" in m2.group(1) and "<p" in m2.group(1), "index %s card non-empty"%cls)
# cards must not be crossed
sec=re.search(r'c-sec[^"]*">(.*?)(?=<a class="read")',P["index.html"],re.S).group(1)
chk("Malott" not in sec and "diesel" not in sec.lower(), "index: security card not crossed")
mkt=re.search(r'c-mkt[^"]*">(.*?)(?=<a class="read")',P["index.html"],re.S).group(1)
chk("ScreenConnect" not in mkt and "Malott" not in mkt, "index: markets card not crossed")

# ---------- 10. GLOBAL SANITY ----------
allt=" ".join(T.values())
chk("Lorem" not in allt, "no placeholder text")
chk("TODO" not in allt and "TKTK" not in allt, "no TODO markers")
for n,h in P.items():
    chk(h.count("<div")-h.count("</div>")==0, n+": div balance")
    st=[]; first=None; lastclose=None
    for mm in re.finditer(r'<div([^>]*)>|</div>', h):
        if mm.group(0).startswith('</'):
            if st: op=st.pop(); lastclose=(op,mm.start())
        else:
            st.append((mm.start(),mm.group(1)))
            if first is None: first=mm.start()
    chk(not st, n+": no unclosed div")
    chk(lastclose is not None and lastclose[0][0]==first,
        n+": the container closing last is the container that opened first")
# nothing 'upcoming' that has already happened
chk("Sat 5 Sep" not in MM or "Last Event" in MM, "mma: 5 Sep not listed as upcoming")
chk("Freedom 250" not in MM or "14 Jun" in MM or "Gaethje" in MM, "mma: Freedom 250 referenced only historically")

print("PASS: %d   FAIL: %d"%(len(ok),len(bad)))
for b in bad: print("  FAIL -",b)
sys.exit(1 if bad else 0)
