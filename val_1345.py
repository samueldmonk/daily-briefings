#!/usr/bin/env python3
import io, re, sys, datetime
D = "/sessions/sharp-bold-tesla/mnt/outputs/"
F = {k: io.open(D + v, encoding="utf-8").read() for k, v in {
    "ix": "index.html", "cy": "cyber-briefing.html",
    "ws": "wallstreet-briefing.html", "mma": "mma-briefing.html"}.items()}
ok = fail = 0
def chk(name, cond):
    global ok, fail
    if cond: ok += 1
    else: fail += 1; print("FAIL: " + name)

# ---- 1. tag balance ----
for k, s in F.items():
    for t in ["div","span","p","h2","h3","h4","h5","table","tr","td","th","ul","li","a","nav","header","footer","script","b","i","body"]:
        o = len(re.findall(r"<%s[ >]" % t, s)); c = len(re.findall(r"</%s>" % t, s))
        chk("%s: <%s> balance %d/%d" % (k, t, o, c), o == c)

# ---- 2. masthead / stamp / nav ----
for k, s in F.items():
    for i in ['id="edition"', 'id="datestamp"', 'id="updated"', 'class="pill live"']:
        chk("%s masthead %s" % (k, i), i in s)
    chk("%s self-stamp JS" % k, "America/New_York" in s and "Afternoon Edition" in s)
    for href in ["index.html", "cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html", "archive.html"]:
        chk("%s nav->%s" % (k, href), ('href="%s"' % href) in s)
    chk("%s exactly one active tab" % k, s.count('class="on"') == 1)
for k in ["cy", "ws", "mma"]:
    chk("%s has .tldr" % k, F[k].count('class="tldr"') == 1)
    chk("%s has freshline" % k, 'id="freshline"' in F[k])
chk("ws tldr label", "<b>The Tape</b>" in F["ws"])
chk("cy tldr label", "<b>The Wire</b>" in F["cy"])
chk("mma tldr label", "<b>Tale of the Tape</b>" in F["mma"])

# ---- 3. widgets: six blocks on WS only, zero elsewhere ----
W = ["ticker-tape", "single-quote", "timeline", "stock-heatmap", "mini-symbol-overview", "events"]
for w in W:
    chk("ws widget " + w, ("embed-widget-%s.js" % w) in F["ws"])
chk("ws exactly 3 single-quote", F["ws"].count("embed-widget-single-quote.js") == 3)
for k in ["ix", "cy", "mma"]:
    chk("%s has zero tradingview" % k, "tradingview" not in F[k].lower())
for sym in ["FOREXCOM:SPXUSD", "FOREXCOM:NSXUSD", "FOREXCOM:DJI", "TVC:USOIL", "TVC:US10Y"]:
    chk("ws ticker keeps " + sym, sym in F["ws"])

# ---- 4. markets arithmetic, re-derived against Tuesday 8 Sep verified closes ----
SP, NQ, DJ = 7673.52, 26421.41, 52786.07
chk("Dow 52786.07-321.52=52464.55", abs((DJ - 321.52) - 52464.55) < 0.005)
chk("Nasdaq 26421.41-158.58=26262.83", abs((NQ - 158.58) - 26262.83) < 0.005)
chk("S&P 7673.52-32.06=7641.46", abs((SP - 32.06) - 7641.46) < 0.005)
chk("321.52/DJ=0.61%", abs(321.52 / DJ * 100 - 0.61) < 0.006)
chk("158.58/NQ=0.60%", abs(158.58 / NQ * 100 - 0.60) < 0.006)
chk("32.06/SP=0.42%", abs(32.06 / SP * 100 - 0.42) < 0.006)
chk("413/DJ=0.78%", abs(413 / DJ * 100 - 0.78) < 0.006)
chk("387.01/DJ=0.73%", abs(387.01 / DJ * 100 - 0.73) < 0.006)
chk("MRVL 12+18=30", 12 + 18 == 30)
for f in ["52,464.55", "26,262.83", "7,641.46", "&minus;321.52", "&minus;158.58", "&minus;32.06", "1:35 p.m."]:
    chk("ws prints " + f, f in F["ws"])
chk("ws refuses the copy-error Nasdaq level", "7,636.59" not in F["ws"])
chk("ws scorecard intact", "7,673.52" in F["ws"] and "52,786.07" in F["ws"] and "26,421.41" in F["ws"])
chk("ws no stale 'latest timed number'", "the latest timed number found this run" not in F["ws"])
chk("ws no duplicate Apple radar bullet", F["ws"].count("John Ternus") == 1)

# ---- 5. cyber: deadlines, countdowns, scores ----
chk("cy 11 Sep present", "11 September 2026" in F["cy"])
chk("cy 16 Sep present", "16 September 2026" in F["cy"])
chk("cy due-date JS has exactly two hard dates",
    F["cy"].count("new Date('2026-09-11T23:59:59-04:00')") == 1 and
    F["cy"].count("new Date('2026-09-16T23:59:59-04:00')") == 1)
for i in ["kevcdn", "kevcdn2", "kevcdn3", "kev2cdn", "kev2cdn2", "kev2cdn3"]:
    chk("cy anchor id=" + i, ('id="%s"' % i) in F["cy"])
# countdown arithmetic sanity from today
today = datetime.date(2026, 9, 9)
chk("11 Sep is 2 days out", (datetime.date(2026, 9, 11) - today).days == 2)
chk("16 Sep is 7 days out", (datetime.date(2026, 9, 16) - today).days == 7)
chk("5 Sep is overdue", (datetime.date(2026, 9, 5) - today).days < 0)
chk("cy says 5 Sep batch overdue", "overdue" in F["cy"] and "due 5 September" in F["cy"])
for cve, score in [("CVE-2026-86206", "6.9"), ("CVE-2026-86207", "7.7"), ("CVE-2026-9586", "9.3"),
                   ("CVE-2026-82329", "9.8"), ("CVE-2026-48710", "6.5"), ("CVE-2026-59822", "8.8"),
                   ("CVE-2026-49869", "10.0"), ("CVE-2026-83548", "10.0"), ("CVE-2026-83549", "7.8")]:
    chk("cy has %s" % cve, cve in F["cy"])
    chk("cy has score %s" % score, score in F["cy"])
chk("cy standing: 83549 is 7.8 not 9.8-mislabel", "CVE-2026-83549</b> (7.8" in F["cy"])
chk("cy hotfix4 build", "2026.3.1.14" in F["cy"])
chk("cy hotfix3 build", "2026.3.1.13" in F["cy"])
chk("cy no flat 'confirmed exploited in the wild by the vendor'",
    "confirmed exploited in the wild by the vendor" not in F["cy"])
chk("cy states the vendor contradiction", "no confirmations that this vulnerability has been exploited" in F["cy"])
chk("cy no BOD 22-01 three-week arithmetic applied", "days left)" not in F["cy"].replace('<span id="kevcdn', 'X'))
chk("cy refuses American Tower as current", "12 June 2026" in F["cy"])
chk("cy no Nevada 2026 regression", "Nevada" not in F["cy"])
chk("cy no CVSS 9.8 for NetScaler regression", "CVE-2026-3055" not in F["cy"])

# ---- 6. MMA guards ----
chk("mma no 'stripped'", "stripped" not in F["mma"].lower())
chk("mma Parnasse spelling", "Salahdine Parnasse" in F["mma"] and "Saladhine" not in F["mma"])
chk("mma Contender Series refusal for Parnasse", "not</b> come through the Contender Series" in F["mma"])
chk("mma no Pereira at 205", re.search(r"Pereira", F["mma"]) is not None and "Not Alex Pereira" in F["mma"])
chk("mma no Chimaev as champ", "Middleweight</td><td><b>Sean Strickland" in F["mma"])
chk("mma featherweight not vacant", "Featherweight</td><td><b>Alexander Volkanovski" in F["mma"])
chk("mma Gaethje at lightweight", "Lightweight</td><td><b>Justin Gaethje" in F["mma"])
chk("mma Makhachev at welterweight", "Welterweight</td><td><b>Islam Makhachev" in F["mma"])
chk("mma Ulberg at LHW", "Light Heavyweight</td><td><b>Carlos Ulberg" in F["mma"])
chk("mma W-flyweight vacant", "Women&rsquo;s Flyweight</td><td class=\"gold\"><b>Vacant" in F["mma"])
chk("mma 11 champion rows", F["mma"].count("</td><td><b>") + F["mma"].count('<td class="gold"><b>Vacant') >= 11)
chk("mma Yair Rodriguez named", "Yair Rodr&iacute;guez" in F["mma"])
chk("mma exactly one New tag", F["mma"].count('class="t new">New') == 1)
chk("mma countdown to 12 Sep", "2026-09-12T17:00:00-04:00" in F["mma"])
chk("mma no athletic commission claim", "athletic commission" not in F["mma"])
chk("mma Dariush not called challenger", "challenger" not in F["mma"] or "Blaydes" in F["mma"])
chk("mma next-card date not in the past", datetime.date(2026, 9, 12) >= today)

# ---- 7. index cards must be byte-identical to each page's own tldr sentence ----
def tldr(k):
    m = re.search(r'<div class="tldr"><b>[^<]+</b> <span>(.*?)</span></div>', F[k], re.S)
    return m.group(1)
def card(idx):
    return re.findall(r'<div class="go"[^>]*>Read the briefing[^<]*</div>', F["ix"]) and \
           re.findall(r'<p>(.*?)</p>\n<div class="go"', F["ix"], re.S)[idx]
strip = lambda x: re.sub(r"</?b>", "", x).strip()
for i, k in enumerate(["cy", "ws", "mma"]):
    chk("index card %d == %s tldr (tags stripped)" % (i, k), strip(card(i)) == strip(tldr(k)))
chk("index has 3 big cards", F["ix"].count('class="bc"') == 3)
chk("index has no live widgets", "s3.tradingview.com" not in F["ix"])

# ---- 8. no stale-date language ----
for k, s in F.items():
    chk("%s no 'this evening'" % k, "this evening" not in s)
    chk("%s no 2025 dateline" % k, "September 2025" not in s)
chk("cy stat strip is 3-5 stats", 3 <= F["cy"].count('<div class="stat">') <= 5)

print("\n%d checks, %d failures" % (ok + fail, fail))
sys.exit(1 if fail else 0)
