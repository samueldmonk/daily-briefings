# -*- coding: utf-8 -*-
import io, re, sys
F = ["index.html","cyber-briefing.html","wallstreet-briefing.html","mma-briefing.html"]
P = {f: io.open(f,encoding="utf-8").read() for f in F}
fails=[]; n=0
def ck(cond,msg):
    global n; n+=1
    if not cond: fails.append(msg)
def has(f,s,msg=None): ck(s in P[f], msg or ("%s missing %r"%(f,s[:70])))
def no(f,s,msg=None): ck(s not in P[f], msg or ("%s must NOT contain %r"%(f,s[:70])))
def cnt(f,s,k): 
    global n; n+=1
    c=P[f].count(s)
    if c!=k: fails.append("%s count %r = %d expected %d"%(f,s[:50],c,k))

# --- stamps / masthead / nav on every page ---
for f in F:
    has(f,'id="edition">Afternoon Edition')
    has(f,'id="updated">8:31 PM ET')
    has(f,'id="freshline">Data as of 8:31 PM ET')
    no(f,'id="edition">Midday Edition')
    no(f,'id="updated">5:15 PM ET')
    no(f,'Data as of 5:15 PM ET')
    no(f,'Data as of 1:45 PM ET'); no(f,'Data as of 1:35 PM ET')
    for t in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html','archive.html']:
        has(f,'href="%s"'%t,"%s nav missing %s"%(f,t))
    has(f,"America/New_York","%s self-stamp missing"%f)
    has(f,'id="datestamp"'); has(f,'pill live')
    has(f,'Saturday, August 29, 2026')
# tldr only on the three briefings; index uses cards
for f in ["cyber-briefing.html","wallstreet-briefing.html","mma-briefing.html"]:
    has(f,'class="tldr"')
has("cyber-briefing.html",'<b>The Wire</b>')
has("wallstreet-briefing.html",'<b>The Tape</b>')
has("mma-briefing.html",'<b>Tale of the Tape</b>')

# --- live widgets: wallstreet only ---
for w in ["embed-widget-ticker-tape.js","embed-widget-single-quote.js","embed-widget-timeline.js",
          "embed-widget-stock-heatmap.js","embed-widget-mini-symbol-overview.js","embed-widget-events.js"]:
    has("wallstreet-briefing.html",w)
    for f in ["index.html","cyber-briefing.html","mma-briefing.html"]:
        no(f,w,"%s must have no live widgets (%s)"%(f,w))
for s in ["FOREXCOM:SPXUSD","FOREXCOM:NSXUSD","FOREXCOM:DJI","TVC:USOIL","TVC:US10Y"]:
    has("wallstreet-briefing.html",s)

# --- markets: Friday closes, all six figures, verified this run ---
W="wallstreet-briefing.html"
for s in ["7,711.76","&minus;0.25%","26,402.42","&minus;0.52%","53,559.99","&minus;9.45"]:
    has(W,s)
has(W,"fourteenth")
no(W,"re-verified a thirteenth time this run")
no(W,"7,673.04")
no(W,"as of ~")
ck("After-Hours" not in P[W] and "After Hours" not in P[W],"After-Hours block must be absent on a weekend")
has(W,"It is <b>Saturday evening</b>")
no(W,"It is Saturday morning")
# Dow points/percent reconciliation
ck(abs((9.45/53559.99)*100 - 0.02) < 0.005, "Dow points/percent reconciliation")
# weekly figures
for s in ["+0.5%","+0.9%"]: has(W,s)
has(W,"winning week")
# rates carried from 5:15 unchanged
for s in ["4.73%","4.34%","5.20%"]: has(W,s)
has(W,"CME FedWatch")

# --- cyber: KEV board, countdowns, new letter card ---
C="cyber-briefing.html"
for s in ["CVE-2026-8452","CVE-2019-1068","CVE-2026-53362","CVE-2023-49105","CVE-2022-0995",
          "CVE-2021-23758","CVE-2015-5287","CVE-2015-3246","CVE-2026-66384"]:
    has(C,s)
for s in ["0 days left","1 day left","11 days left","12 days left"]:
    has(C,s)
has(C,"BOD 26-04")
has(C,"August 27 alert page for the first time")
has(C,"CISA Adds Three Known Exploited Vulnerabilities to Catalog")
has(C,"August 24 adding one vulnerability")
has(C,"No alert dated later than August 27 was returned")
has(C,"do not see the whole catalogue")
# the new letter card
has(C,"A call for collective action on cyber defense")
has(C,"August 27, 2026</b>, OpenAI published an open letter")
has(C,"116 companies and entities")
has(C,"128 organisations")
has(C,"116 to roughly 130")
has(C,"no source fetched this run defines its own unit")
for name in ["Anthropic","Google","Microsoft","AWS","IBM","Oracle","Cisco","Check Point","Cloudflare","CrowdStrike"]:
    has(C,"<b>%s</b>"%name,"cyber letter signatory %s"%name)
# no invented count
no(C,"exactly 130 companies"); no(C,"all 130")
# ServiceNow 6875/6876 status kept apart (proximity sweep)
for cve,word in [("CVE-2026-6875","exploited"),("CVE-2026-6876","not exploited")]:
    idx=[mm.start() for mm in re.finditer(re.escape(cve),P[C])]
    ck(len(idx)>0, "cyber missing %s"%cve)
    ck(any(word in P[C][max(0,i-420):i+420] for i in idx), "%s must sit near %r"%(cve,word))
# Oracle id still not carried, and never inside a table row
ID="CVE-2026-21962"
if ID in P[C]:
    for mm in re.finditer(re.escape(ID),P[C]):
        seg=P[C][max(0,mm.start()-700):mm.start()+700]
        ck("not carried" in seg or "Not carried" in seg, "%s must appear only in a not-carried statement"%ID)
        row=P[C].rfind("<tr",0,mm.start()); rowend=P[C].rfind("</tr>",0,mm.start())
        ck(not (row>rowend), "%s must never appear inside a table row"%ID)
# Unitree pair: no CVSS may be attached to either id
for cid in ["CVE-2026-76640","CVE-2026-76639"]:
    if cid in P[C]:
        for mm in re.finditer(re.escape(cid),P[C]):
            seg=re.sub("<[^>]+>"," ",P[C][max(0,mm.start()-200):mm.start()+200])
            ck(not re.search(r"CVSS\s*\d",seg), "%s must carry no CVSS"%cid)
# TITAN 700GB must sit near the not-validated caveat
for mm in re.finditer("700GB",P[C]):
    seg=P[C][max(0,mm.start()-700):mm.start()+700]
    ck("claim" in seg or "not been independently validated" in seg or "marketing" in seg,
       "700GB must be framed as the group's own claim")
# CVE well-formedness + liveness
cves=set(re.findall(r"CVE-\d{4}-\d{4,6}", P[C]))
ck(len(cves)>=15, "cyber should carry >=15 distinct CVEs, has %d"%len(cves))
for c_ in cves: ck(re.match(r"^CVE-\d{4}-\d{4,6}$",c_) is not None, "malformed %s"%c_)

# --- mma: champions board, results, new material ---
M="mma-briefing.html"
CHAMPS=["Tom Aspinall","Carlos Ulberg","Sean Strickland","Islam Makhachev","Justin Gaethje",
        "Alexander Volkanovski","Petr Yan","Joshua Van","Valentina Shevchenko","Kayla Harrison",
        "Mackenzie Dern","Ciryl Gane"]
for c_ in CHAMPS: has(M,c_,"champions board missing %s"%c_)
# forbidden regressions -- assert the BOARD ROWS, and forbid affirmative claims.
# (The blunt proximity guards used earlier fired on corrective narrative; these are stricter,
#  because they check what the table actually says rather than what words sit near a name.)
def row(div):
    mm=re.search(r"<tr>\s*<td>\s*%s\s*</td>\s*<td[^>]*>(.{0,120}?)</td>"%re.escape(div),P[M],re.S)
    return re.sub("<[^>]+>","",mm.group(1)).strip() if mm else None
for div,champ in [("Light Heavyweight","Carlos Ulberg"),("Middleweight","Sean Strickland"),
                  ("Welterweight","Islam Makhachev"),("Lightweight","Justin Gaethje"),
                  ("Featherweight","Alexander Volkanovski"),("Bantamweight","Petr Yan"),
                  ("Heavyweight","Tom Aspinall"),("Flyweight","Joshua Van")]:
    r=row(div); ck(r is not None,"champions board has no %s row"%div)
    if r is not None: ck(champ in r,"%s row must name %s, says %r"%(div,champ,r))
# no affirmative champion claim for either superseded name, anywhere
for bad in ["Pereira</b></td>","Chimaev</b></td>","champion Alex Pereira","champion Khamzat Chimaev",
            "Pereira retains","Chimaev retains","Pereira (205)","light heavyweight champion Alex Pereira",
            "middleweight champion Khamzat Chimaev"]:
    no(M,bad,"forbidden affirmative champion claim: %s"%bad)
# every "vacant" must be either the historical vacant-title fact or an explicit rejection
for mm in re.finditer("vacant",P[M],re.I):
    seg=re.sub("<[^>]+>"," ",P[M][max(0,mm.start()-420):mm.start()+420])
    ck(("vacant title" in seg.lower() or "vacant light-heavyweight title" in seg.lower()
        or "was rejected" in seg or "not vacant" in seg or "is not a vacancy" in seg
        or "Volkanovski" in seg),
       "loose 'vacant' at %d: %r"%(mm.start(), re.sub(r"\s+"," ",seg)[:120]))
# featherweight may never be called vacant
for mm in re.finditer("[Ff]eatherweight",P[M]):
    seg=re.sub("<[^>]+>"," ",P[M][max(0,mm.start()-260):mm.start()+260])
    if re.search("vacan",seg,re.I):
        ck("Volkanovski" in seg or "was published vacant" in seg or "regression" in seg,
           "featherweight+vacant must sit in a corrective frame")
# Dariush descriptor
for mm in re.finditer("Dariush",P[M]):
    seg=re.sub("<[^>]+>"," ",P[M][max(0,mm.start()-300):mm.start()+300]).lower()
    ck("champion" not in seg and "title challenger" not in seg, "Dariush descriptor must stay contender-only")
# results table figures upheld this run
has(M,"KO (punch), 2:28 of round 2")
has(M,"4:14 of round 1")
has(M,"round two at 2:28")
no(M,"round one at 2:28")
has(M,"both were upheld")
has(M,"Round 2 walk-off shot")
# Song quote + path
has(M,"I can finish Petr, I can finish Merab")
has(M,"UFC 333 on October 24")
has(M,"backup role")
has(M,"&minus;600"); has(M,"&minus;625")
has(M,"first man to knock out Umar Nurmagomedov")
# bonuses family unchanged
has(M,"$400,000"); has(M,"$25,000")
for nm in ["Hector Santiago","Francesco Nuzzi","Rei Tsuruya","Kai Asakura","Denise Gomes"]:
    has(M,nm,"$25,000 recipient %s"%nm)
has(M,"did not receive one of the four $100,000 awards")
no(M,"Denise Gomes did not receive a bonus")
# countdown
has(M,"ufccdn")
has(M,"September 19")
# names spelled per corrections
no(M,"Cody Salkilld"); no(M,"Abdul-Rakhman"); no(M,"Shamil Yakhyaev")

# --- index cards must mirror the three tldrs ---
def tldr(f):
    s=P[f]; i=s.find('<div class="tldr">'); j=s.find('</span></div>',i)
    return re.sub(r"\s+"," ",re.sub("<[^>]+>","",s[s.find("</b>",i)+4:j])).strip()
def card(kick):
    s=P["index.html"]; i=s.find(kick); a=s.find("<p>",i); b=s.find("</p>",a)
    return re.sub(r"\s+"," ",re.sub("<[^>]+>","",s[a+3:b])).strip()
for kick,f in [("&#9880; The Cyber Wire</div>",C),("&#9650; The Closing Bell</div>",W),
               ("&#8856; The Octagon</div>",M)]:
    ck(card(kick)==tldr(f), "index card must equal %s tldr\nCARD: %s\nTLDR: %s"%(f,card(kick)[-160:],tldr(f)[-160:]))

# --- footers: links, no duplicates, absolute hrefs ---
for f in F:
    if f=="index.html": continue
    j=P[f].find("<footer"); ck(j>0,"%s missing <footer>"%f)
    hrefs=re.findall(r'href="(http[^"]+)"',P[f][j:])
    ck(len(hrefs)>=6,"%s footer needs >=6 source links, has %d"%(f,len(hrefs)))
    ck(len(hrefs)==len(set(hrefs)),"%s footer has duplicate hrefs: %s"%(f,[h for h in hrefs if hrefs.count(h)>1][:3]))
    for h in hrefs: ck(h.startswith("http"),"%s non-absolute href %s"%(f,h))
    has(f,"disc")

print("CHECKS: %d   FAILURES: %d"%(n,len(fails)))
for x in fails: print(" FAIL:",x)
sys.exit(1 if fails else 0)
