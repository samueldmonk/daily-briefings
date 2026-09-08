# -*- coding: utf-8 -*-
import io, os, re, sys, datetime
OUT = os.path.dirname(os.path.abspath(__file__))
PAGES = {p: io.open(os.path.join(OUT, p), encoding="utf-8").read()
         for p in ("index.html","cyber-briefing.html","wallstreet-briefing.html","mma-briefing.html")}
fails=[]; n=0
def ck(cond, msg):
    global n; n+=1
    if not cond: fails.append(msg)

# --- structure -------------------------------------------------------------
for p,h in PAGES.items():
    ck(h.startswith("<!DOCTYPE html>"), p+": doctype")
    ck(h.rstrip().endswith("</html>"), p+": closing html")
    ck('<meta charset="utf-8">' in h, p+": charset")
    ck('name="viewport"' in h, p+": viewport")
    for tag in ("div","p","table","tr","td","h2","h3","span","ul","li","script","header","nav"):
        o=len(re.findall(r"<%s[ >]"%tag,h)); c=len(re.findall(r"</%s>"%tag,h))
        ck(o==c, "%s: %s balance %d/%d"%(p,tag,o,c))
    # five-tab nav
    for href in ("index.html","cyber-briefing.html","wallstreet-briefing.html","mma-briefing.html","archive.html"):
        ck(('href="%s"'%href) in h, "%s: nav missing %s"%(p,href))
    ck(h.count('class="active"')==1, p+": exactly one active tab")
    # masthead pills + stamp
    for i in ('id="edition"','id="datestamp"','id="updated"'):
        ck(i in h, "%s: masthead %s"%(p,i))
    ck("America/New_York" in h, p+": stamp JS tz")
    for ed in ("Morning Edition","Midday Edition","Afternoon Edition"):
        ck(ed in h, "%s: edition bucket %s"%(p,ed))
    ck('id="freshline"' in h, p+": freshline")
    ck("briefings refresh every 30 minutes" in h, p+": freshline text")

ACTIVE={"index.html":'<a href="index.html" class="active">',
        "cyber-briefing.html":'<a href="cyber-briefing.html" class="active">',
        "wallstreet-briefing.html":'<a href="wallstreet-briefing.html" class="active">',
        "mma-briefing.html":'<a href="mma-briefing.html" class="active">'}
for p,a in ACTIVE.items(): ck(a in PAGES[p], p+": correct active tab")

# --- tldr strips -----------------------------------------------------------
ck(PAGES["wallstreet-briefing.html"].count('<div class="tldr">')==1 and "<b>The Tape</b>" in PAGES["wallstreet-briefing.html"], "ws: one tldr labelled The Tape")
ck(PAGES["cyber-briefing.html"].count('<div class="tldr">')==1 and "<b>The Wire</b>" in PAGES["cyber-briefing.html"], "cyber: one tldr labelled The Wire")
ck(PAGES["mma-briefing.html"].count('<div class="tldr">')==1 and "<b>Tale of the Tape</b>" in PAGES["mma-briefing.html"], "mma: one tldr labelled Tale of the Tape")
ck('class="tldr"' not in PAGES["index.html"], "index: no tldr strip")

# --- tradingview blocks (ws only) -----------------------------------------
ws=PAGES["wallstreet-briefing.html"]
for w in ("ticker-tape","single-quote","timeline","stock-heatmap","mini-symbol-overview","events"):
    ck(("embed-widget-%s.js"%w) in ws, "ws: widget "+w)
ck(ws.count("embed-widget-single-quote.js")==3, "ws: exactly three single-quote widgets")
for sym in ("FOREXCOM:SPXUSD","FOREXCOM:NSXUSD","FOREXCOM:DJI","TVC:USOIL","TVC:US10Y"):
    ck(sym in ws, "ws: ticker symbol "+sym)
ck('"symbol":"NYSE:NVS"' in ws, "ws: chart of the day pinned to NYSE:NVS")
ck('class="livebar"' in ws, "ws: livebar wrapper")
ck("Quotes stream live" in ws, "ws: quotes note line")
for p in ("index.html","cyber-briefing.html","mma-briefing.html"):
    ck("tradingview.com" not in PAGES[p], p+": carries no tradingview string")

# --- mma countdown ---------------------------------------------------------
mm=PAGES["mma-briefing.html"]
ck('id="ufccdn"' in mm, "mma: countdown element")
ck("2026-09-12T14:00:00-04:00" in mm, "mma: countdown target datetime")
ck("Fight week" in mm, "mma: countdown elapsed text")

# --- champions guards ------------------------------------------------------
BANNED_CHAMP_CELLS=["<td>Alex Pereira</td>","<td>Khamzat Chimaev</td>","<td>Ilia Topuria</td>","<td>Valentina Shevchenko</td>"]
for b in BANNED_CHAMP_CELLS: ck(b not in mm, "mma: banned champion cell "+b)
for c in ["Tom Aspinall","Carlos Ulberg","Sean Strickland","Islam Makhachev","Justin Gaethje",
          "Alexander Volkanovski","Petr Yan","Joshua Van","Kayla Harrison","Mackenzie Dern"]:
    ck(c in mm, "mma: seated champion missing "+c)
ck('class="mut">Vacant</td>' in mm, "mma: women's flyweight seated Vacant")
for bad in ["Saladhine","Paransse","Cody Salkilld","Diamond Desert Arena"]:
    ck(bad not in mm, "mma: banned string "+bad)
ck("Salahdine Parnasse" in mm, "mma: Parnasse spelling")
ck("Desert Diamond Arena" in mm, "mma: correct Noche venue")
ck("did not come through the Contender Series" in mm, "mma: Parnasse DWCS denial present")
ck("Patrick Rivera" in mm and "1 September" in mm, "mma: Darby opponent+date pair")

# --- KEV countdown arithmetic ---------------------------------------------
today=datetime.date(2026,9,8)
KEV=[("14 September",datetime.date(2026,9,14),6),("16 September",datetime.date(2026,9,16),8),
     ("18 September",datetime.date(2026,9,18),10)]
cy=PAGES["cyber-briefing.html"]
for label,due,days in KEV:
    ck((due-today).days==days, "kev arithmetic self-test %s"%label)
    ck(label in cy, "cyber: KEV date "+label)
    ck(("(%d days left)"%days) in cy, "cyber: KEV countdown %d days"%days)
for bad in ["(5 days left)","(7 days left)","(9 days left)","(11 days left)","overdue"]:
    ck(bad not in cy, "cyber: banned countdown/word "+bad)
# three-week shorthand only next to its negation
for m in re.finditer("three-week", cy):
    seg=cy[max(0,m.start()-260):m.start()+260]
    ck("not" in seg, "cyber: three-week shorthand without negation")

# --- required literals -----------------------------------------------------
REQ={
 "wallstreet-briefing.html":["1:25&ndash;1:50 PM ET","Dow down 1%","down roughly 0.4%","7,707","7,718.60","26,506.99","53,414.25",
   "271.86","$137.63","$394.38","2.46%","$97.99","$99.46","$92.90","11:28 a.m. ET","Jazan","73 civilians",
   "$20 billion","15% to 50%","18-month-old","4.3810%","October 2023","58.7%","49&ndash;66%","162,000","4.1%",
   "3.50&ndash;3.75%","$1.67","10 September","11 September","pelacarsen","Ionis","olpasiran","BMO Capital Markets",
   "Mark Carney","byte-identical","$5.85","5.25%","4.12%","4.55%","4.37%"],
 "cyber-briefing.html":["CVE-2026-67276","CVE-2026-86060","MikroTrick","122,000","82.192.72.4","7.25beta3","6.49.21",
   "3 September","2 September","CERT Polska","1,079,819","Metabase","10 August","27 August","Framework","Kilo Code",
   "CVE-2026-83548","10.0","CVE-2026-83549","CVE-2026-59822","8.8","CVE-2026-81578","CVE-2026-82078","31 August",
   "CVE-2026-85046","The Gentlemen","ArmCorp","269 victims","2,000 victim listings","Check Point","410","14%",
   "$310,000","CVE-2026-68820","afd.sys","421","398","751","BOD 26-04","1:00 PM ET","9.2"],
 "mma-briefing.html":["Michael Page","Nursulton Ruziboev","John Morgan","No. 15","No. 8","Meta rankings",
   "24-2","24-15","2:35","Axel Sola","Losene Keita","Mario Pinto","Muhammad Naimov","Ryan Spann","Fares Ziam",
   "$100,000","$25,000","Jean Silva","Jose Delgado","13 bouts","2 p.m. ET","5 p.m. ET","Curtis Blaydes",
   "Alexandre Pantoja","Crypto.com Arena","26 seconds","Arman Tsarukyan","&minus;400","Natalia Silva","Wang Cong",
   "Delta Center","CBS","14-fight win streak","Tracy Cortez","UFC 329","stripped","Quentin Pasley","Arlind Berisha",
   "Reginaldo Geraldo Jr.","Isaac Moreno","Martin Kozak","Christian Echols","Apollo Gomes","Won Il Kwon",
   "Christian Natividad","Colton Loud","8.2 million","17 million","34 million","4.96 million","$7.7 billion",
   "20 times","12 December","Adam Darby","Cage Warriors"],
 "index.html":["The Cyber Wire","The Closing Bell","The Octagon","122,000","Novartis","Michael Page","Shevchenko","Archive"],
}
for p,lits in REQ.items():
    for l in lits: ck(l in PAGES[p], "%s: missing literal %r"%(p,l))

# --- stale-phrase bans -----------------------------------------------------
STALE=["Labor Day long weekend opened","Dow futures","pre-open","market holiday today","after today&#39;s close",
       "10:35 AM ET","Intel leads the tape","NASDAQ:INTC","+5.2%"]
for p,h in PAGES.items():
    for s in STALE: ck(s not in h, "%s: stale phrase %r"%(p,s))
# refused figures must not appear as live claims
for bad in ["&minus;2.55%","&minus;2.10%","&minus;2.05%","+11.9%","Sandisk"]:
    ck(bad not in ws or "byte-identical" in ws, "ws: refused figure surfaced "+bad)

# --- sources ---------------------------------------------------------------
for p in ("cyber-briefing.html","wallstreet-briefing.html","mma-briefing.html"):
    urls=len(re.findall(r'<a href="https?://', PAGES[p]))
    ck(urls>=12, "%s: >=12 source URLs (got %d)"%(p,urls))
    ck("Sources" in PAGES[p], p+": sources heading")
    ck('class="disc"' in PAGES[p], p+": disclaimer")
ck("not investment advice" in ws, "ws: investment-advice disclaimer")
ck("subject to change" in mm, "mma: cards-subject-to-change disclaimer")

print("checks:", n, "failures:", len(fails))
for f in fails: print("  FAIL:", f)
sys.exit(1 if fails else 0)
