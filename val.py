# -*- coding: utf-8 -*-
import io, os, re, datetime, sys
D = os.path.dirname(os.path.abspath(__file__))
F = {}
for k, fn in [("ix","index.html"),("cy","cyber-briefing.html"),("ws","wallstreet-briefing.html"),("mm","mma-briefing.html")]:
    F[k] = io.open(os.path.join(D, fn), encoding="utf-8").read()

N = [0]; FAIL = []
def ck(cond, label):
    N[0] += 1
    if not cond: FAIL.append(label)

# ---------- structure ----------
for k, v in F.items():
    ck(v.startswith("<!DOCTYPE html>"), k+": doctype")
    ck(v.rstrip().endswith("</html>"), k+": closing html")
    ck('<meta charset="utf-8">' in v, k+": charset")
    ck('name="viewport"' in v, k+": viewport")
    for tag in ["div","p","table","tr","td","h2","h3","span","ul","li","script","header","nav"]:
        o = len(re.findall(r"<%s[ >]" % tag, v)); c = len(re.findall(r"</%s>" % tag, v))
        ck(o == c, "%s: balanced <%s> (%d/%d)" % (k, tag, o, c))

# ---------- nav ----------
TABS = ["index.html","cyber-briefing.html","wallstreet-briefing.html","mma-briefing.html","archive.html"]
for k, v in F.items():
    nv = v.split('<nav class="tabs">')[1].split("</nav>")[0]
    for t in TABS: ck('href="%s"' % t in nv, "%s: nav link %s" % (k, t))
    ck(nv.count("<a ") == 5, k+": exactly five tabs")
    ck(nv.count('class="active"') == 1, k+": exactly one active tab")
    for lab in ["Front Page","The Cyber Wire","The Closing Bell","The Octagon","Archive"]:
        ck(lab in nv, "%s: nav label %s" % (k, lab))
ck('href="index.html" class="active"' in F["ix"], "ix: active tab is Front Page")
ck('href="cyber-briefing.html" class="active"' in F["cy"], "cy: active tab is Cyber")
ck('href="wallstreet-briefing.html" class="active"' in F["ws"], "ws: active tab is Closing Bell")
ck('href="mma-briefing.html" class="active"' in F["mm"], "mm: active tab is Octagon")

# ---------- masthead / stamp ----------
for k, v in F.items():
    ck('class="pill live"' in v, k+": live pill")
    ck('id="edition"' in v, k+": edition pill")
    ck('id="datestamp"' in v, k+": datestamp pill")
    ck('id="updated"' in v, k+": updated pill")
    ck('id="freshline"' in v, k+": freshline element")
    ck("America/New_York" in v, k+": stamp uses ET")
    ck("'Morning Edition'" in v, k+": edition bucket morning")
    ck("'Midday Edition'" in v, k+": edition bucket midday")
    ck("'Afternoon Edition'" in v, k+": edition bucket afternoon")
    ck("briefings refresh every 30 minutes" in v, k+": freshline text")

# ---------- tldr ----------
ck('<div class="tldr"><b>The Wire</b>' in F["cy"], "cy: tldr label The Wire")
ck('<div class="tldr"><b>The Tape</b>' in F["ws"], "ws: tldr label The Tape")
ck('<div class="tldr"><b>Tale of the Tape</b>' in F["mm"], "mm: tldr label Tale of the Tape")
ck('class="tldr"' not in F["ix"], "ix: no tldr strip (cards instead)")
for k in ["cy","ws","mm"]:
    ck(F[k].count('class="tldr"') == 1, k+": exactly one tldr")

# ---------- live widgets ----------
W = ["embed-widget-ticker-tape.js","embed-widget-single-quote.js","embed-widget-timeline.js",
     "embed-widget-stock-heatmap.js","embed-widget-mini-symbol-overview.js","embed-widget-events.js"]
for w in W: ck(w in F["ws"], "ws: widget "+w)
ck(F["ws"].count("embed-widget-single-quote.js") == 3, "ws: exactly three single-quote widgets")
for s in ["FOREXCOM:SPXUSD","FOREXCOM:NSXUSD","FOREXCOM:DJI","TVC:USOIL","TVC:US10Y"]:
    ck(s in F["ws"], "ws: ticker symbol "+s)
ck('"symbol":"NASDAQ:INTC"' in F["ws"], "ws: chart-of-the-day symbol is Intel")
ck('class="livebar"' in F["ws"] and "LIVE QUOTES" in F["ws"], "ws: livebar wrapper")
ck("Quotes stream live" in F["ws"], "ws: note line under quotes")
for k in ["ix","cy","mm"]:
    ck("tradingview.com" not in F[k], k+": carries no live widget")

# ---------- MMA countdown ----------
ck('id="ufccdn"' in F["mm"], "mm: countdown element")
ck("2026-09-12T17:00:00-04:00" in F["mm"], "mm: countdown target datetime")
ck("Fight week" in F["mm"], "mm: countdown elapsed text")

# ---------- champions: refusals and required seats ----------
CH = F["mm"].split("Champions Board")[1]
for banned in ["<td>Alex Pereira</td>","<td>Valentina Shevchenko</td>","<td>Khamzat Chimaev</td>","<td>Ilia Topuria</td>"]:
    ck(banned not in CH, "mm: banned champion cell "+banned)
for name in ["Tom Aspinall","Carlos Ulberg","Sean Strickland","Islam Makhachev","Justin Gaethje",
             "Alexander Volkanovski","Petr Yan","Joshua Van","Kayla Harrison","Mackenzie Dern"]:
    ck("<td>%s</td>" % name in CH, "mm: seated champion "+name)
ck('<td class="mut">Vacant</td>' in CH, "mm: women's flyweight vacant")
ck("refused" in CH, "mm: refusals stated in print")

# ---------- name-spelling guards from past regressions ----------
ck("Salahdine Parnasse" in F["mm"], "mm: Parnasse present")
for bad in ["Saladhine","Paransse","Cody Salkilld","Kerry Hatley’s","Diamond Desert Arena</div>"]:
    ck(bad not in F["mm"].replace("&ldquo;Kerry Hatley&rdquo;",""), "mm: bad spelling "+bad)
ck("did not come through Dana White&#39;s Contender Series" in F["mm"], "mm: Parnasse DWCS denial")
ck("Desert Diamond Arena" in F["mm"], "mm: correct venue name")
ck("Patrick Rivera" in F["mm"] and "1 September 2026" in F["mm"], "mm: Darby opponent+date corrected")

# ---------- KEV countdown arithmetic ----------
TODAY = datetime.date(2026, 9, 8)
for due, days, label in [((2026,9,14), 6, "PaperCut"), ((2026,9,16), 8, "2 Sep batch"), ((2026,9,18), 10, "Chrome V8")]:
    d = (datetime.date(*due) - TODAY).days
    ck(d == days, "arith: %s should be %d days, computed %d" % (label, days, d))
ck("<b class=\"down\">6 days left</b>" in F["cy"], "cy: PaperCut 6 days left")
ck(">8 days left</b>" in F["cy"], "cy: 2 Sep batch 8 days left")
ck(">10 days left</b>" in F["cy"], "cy: Chrome V8 10 days left")
for bad in ["5 days left","7 days left","9 days left","11 days left","overdue"]:
    ck(bad not in F["cy"], "cy: off-by-one / stale countdown "+bad)
# patch priority must agree with KEV section
pp = F["cy"].split("Patch Priority")[1].split("</div>")[0] + F["cy"].split("Patch Priority")[1][:1400]
ck("14 September" in pp and "6 days left" in pp, "cy: patch priority matches KEV deadline")
ck("callout crit" in F["cy"], "cy: patch priority is crit-bordered")

# ---------- BOD wording guard ----------
i = F["cy"].find("three weeks from the add date")
ck(i == -1 or ("not</b> the text of BOD 22-01" in F["cy"][i:i+200]), "cy: three-week shorthand only next to its negation")
ck("BOD 26-04" in F["cy"], "cy: BOD 26-04 named")
ck("3, 14 or 60 calendar days" in F["cy"], "cy: BOD 26-04 windows")

# ---------- required literals ----------
REQ = {
 "cy": ["CVE-2026-75650","CVSS score of 10.0","APSB26-146","StyleSmuggler","4 September 2026","VULN-39341",
        "2.4.4-p18","CVE-2026-44756","SAP Note 3747649","CVE-2026-58240","SAP Note 3759472","CVE-2026-76969",
        "CVE-2026-59346","CVE-2026-85046","18 September 2026","CVE-2026-81578","CVE-2026-82078","31 August",
        "CVE-2026-83548","CVE-2026-83549","Sangoma Switchvox","Kludex Starlette","Kestra OSS","BerriAI LiteLLM",
        "JFrog Artifactory","SonicWall SMA1000","19 new security notes","Qilin","1,358","The Gentlemen",
        "Majinahanashi","AA26-222A","67,000","ShipMonk","7,551","24.9","421 vulnerabilities","1:00 PM ET",
        "Threat Level: High","pc-app.exe"],
 "ws": ["10:35 AM ET","52,800.65","613.60","26,379.01","127.98","7,707","7,718.60","26,506.99","53,414.25",
        "271.86","Intel (INTC) has jumped 5.2","SMH","Micron (MU) up 2.0","Nvidia (NVDA) up 1.2","XLE",
        "URA","XOP","4.12","4.37","4.55","4.79","5.25","3.50&ndash;3.75","52","50&ndash;63","99.73","94.28",
        "98.50","5.85","5.816","10 September","1.67","11 September","162,000","4.1","53,000","56,000","55,000",
        "$20 billion","toilet paper","Labor Day","Weekly Scorecard","not investment advice"],
 "mm": ["UFC 332","Nat&aacute;lia Silva","Wang Cong","3 October","CBS","vacant","Delta Center",
        "Noche UFC","Jean Silva","Jose Delgado","Desert Diamond Arena","Yair Rodr&iacute;guez",
        "&minus;428","+324","&minus;425","+355","&minus;450","+350","UFC 331","Crypto.com Arena",
        "Alexandre Pantoja","+100","&minus;120","&minus;105","&minus;115","Arman Tsarukyan","&minus;380",
        "+305","Gable Steveson","&minus;1500","+600","Accor Arena","5 September","Dan Hooker","2:35",
        "Axel Sola","Fares Ziam","Mario Pinto","Ryan Spann","Losene Keita","Delphine Benouaich",
        "Matthieu Duclos","Modestas Bukauskas","Kurtis Campbell","24-2","Adam Darby","Cage Warriors",
        "7-1","Joaquin Buckley","Mike Malott","Raul Rosas Jr.","Raoni Barcelos","34 million","7.0 million",
        "UFC 327","subject to change"],
 "ix": ["Daily Briefings","The Cyber Wire","The Closing Bell","The Octagon","The Wire","The Tape",
        "Tale of the Tape","Read the briefing"],
}
for k, lits in REQ.items():
    for lit in lits: ck(lit in F[k], "%s: literal %r" % (k, lit))

# ---------- index cards ----------
ck(F["ix"].count('class="bcard') == 3, "ix: three big cards")
ck(F["ix"].count('class="read"') == 3, "ix: three read links")
for h in ["cyber-briefing.html","wallstreet-briefing.html","mma-briefing.html"]:
    ck(F["ix"].count('href="%s"' % h) >= 2, "ix: card+nav link to "+h)

# ---------- sources ----------
for k in ["cy","ws","mm"]:
    ck("<h2 class=\"sec\">Sources</h2>" in F[k], k+": sources section")
    n = len(re.findall(r'<a href="https?://', F[k].split("Sources</h2>")[1]))
    ck(n >= 12, "%s: >=12 source URLs (found %d)" % (k, n))
    ck('class="disc"' in F[k], k+": disclaimer")
ck("Nothing here is investment advice" in F["ws"] or "not investment advice" in F["ws"], "ws: investment disclaimer")
ck("not security advice" in F["cy"], "cy: security disclaimer")
ck("subject to change" in F["mm"], "mm: cards-change disclaimer")

# ---------- stale-phrase bans ----------
BAN_ALL = ["Labor Day, U.S. stock AND bond markets CLOSED","futures halt","pre-market movers as of 8:04",
           "after today&#39;s close</b>, est","Freedom 250 is underway","fetched directly this run"]
for k, v in F.items():
    for b in BAN_ALL: ck(b not in v, "%s: stale phrase %r" % (k, b))
ck("Oracle&#39;s fiscal Q1 2027 report lands 10 September" in F["ws"], "ws: Oracle date corrected")
# the phrase may appear ONLY inside the sentence that corrects the earlier edition
_j = F["ws"].find("after today&#39;s close")
ck(F["ws"].count("after today&#39;s close") <= 1, "ws: 'after today's close' appears more than once")
ck(_j == -1 or "This corrects an earlier edition" in F["ws"][max(0,_j-200):_j],
   "ws: Oracle 'after today's close' only inside its correction")
# markets are open: page must not describe the session as closed or pre-open
for b in ["markets are closed","pre-open","PRE-OPEN","market is closed today"]:
    ck(b not in F["ws"], "ws: stale closed/pre-open framing %r" % b)
ck("Dow futures" not in F["ws"], "ws: no futures framing during an open session")

print("checks:", N[0], "failures:", len(FAIL))
for f in FAIL: print("  FAIL:", f)
sys.exit(1 if FAIL else 0)
