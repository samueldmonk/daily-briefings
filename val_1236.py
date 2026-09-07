import io, re, html, sys

D = "/sessions/lucid-loving-wright/mnt/outputs/"
PAGES = ["index.html", "cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"]
S = {p: io.open(D + p, encoding="utf-8").read() for p in PAGES}

fails, checks = [], 0
def ck(cond, msg):
    global checks
    checks += 1
    if not cond: fails.append(msg)

def txt(p):
    s = S[p]
    s = re.sub(r'<script.*?</script>', '', s, flags=re.S)
    s = re.sub(r'<style.*?</style>', '', s, flags=re.S)
    s = re.sub(r'<[^>]+>', ' ', s)
    return html.unescape(s).replace('\xa0', ' ')

T = {p: txt(p) for p in PAGES}

# ---- 1. structural: tag balance and first-open/last-close pairing -----------
for p in PAGES:
    opens = len(re.findall(r'<div\b', S[p]))
    closes = len(re.findall(r'</div>', S[p]))
    ck(opens == closes, "%s div imbalance: %d open / %d close" % (p, opens, closes))
    # stack walk: the container that closes last must be the one that opened first
    stack, first_open_id, last_closed_id = [], None, None
    nid = 0
    for m in re.finditer(r'<div\b|</div>', S[p]):
        if m.group(0).startswith('</'):
            if stack: last_closed_id = stack.pop()
        else:
            nid += 1
            if first_open_id is None: first_open_id = nid
            stack.append(nid)
    ck(not stack, "%s: %d unclosed div(s)" % (p, len(stack)))
    ck(last_closed_id == first_open_id,
       "%s: last div closed (#%s) is not the first div opened (#%s)" % (p, last_closed_id, first_open_id))

# ---- 2. every page: nav, masthead ids, freshline, stamp script --------------
for p in PAGES:
    for href in ["index.html", "cyber-briefing.html", "wallstreet-briefing.html",
                 "mma-briefing.html", "archive.html"]:
        ck('href="%s"' % href in S[p], "%s missing nav link %s" % (p, href))
    for i in ["edition", "datestamp", "updated", "freshline"]:
        ck('id="%s"' % i in S[p], "%s missing id=%s" % (p, i))
    ck("America/New_York" in S[p], "%s missing ET stamp script" % p)
    ck("briefings refresh every 30 minutes" in S[p], "%s missing freshness line" % p)
    ck(S[p].count('class="active"') == 1, "%s active tab count" % p)

for p, label in [("cyber-briefing.html", "The Wire"),
                 ("wallstreet-briefing.html", "The Tape"),
                 ("mma-briefing.html", "Tale of the Tape")]:
    ck('class="tldr"' in S[p], "%s missing tldr" % p)
    ck(label in S[p], "%s missing tldr label %s" % (p, label))
ck('class="tldr"' not in S["index.html"], "index must not carry a tldr strip")

# ---- 3. Wall Street live widget blocks -------------------------------------
W = S["wallstreet-briefing.html"]
for w in ["embed-widget-ticker-tape.js", "embed-widget-single-quote.js",
          "embed-widget-timeline.js", "embed-widget-stock-heatmap.js",
          "embed-widget-mini-symbol-overview.js", "embed-widget-events.js"]:
    ck(w in W, "wallstreet missing widget %s" % w)
ck(W.count("embed-widget-single-quote.js") == 3, "wallstreet needs 3 single-quote widgets")
for sym in ["FOREXCOM:SPXUSD", "FOREXCOM:NSXUSD", "FOREXCOM:DJI", "TVC:USOIL", "TVC:US10Y"]:
    ck(sym in W, "wallstreet ticker tape missing %s" % sym)
ck('class="livebar"' in W, "wallstreet missing livebar")

# ---- 4. THE DIESEL CORRECTION ---------------------------------------------
WT = T["wallstreet-briefing.html"]
ck("$5.85" in WT, "WS: new diesel record $5.85 absent")
ck("4 September" in WT, "WS: diesel record date absent")
# the OLD figure may appear only inside the correction trail, never as the record
for m in re.finditer(r'\$5\.820', WT):
    seg = WT[max(0, m.start() - 400): m.start() + 400]
    ck(("3 September" in seg) or ("superseded" in seg) or ("had been" in seg)
       or ("correction trail" in seg) or ("corrected" in seg),
       "WS: $5.820 appears without the superseding context: ..." + seg[350:450])
ck("all-time high of $5.820" not in WT, "WS: $5.820 still asserted as the all-time high")
ck("hit an all-time high of $5.85" in WT, "WS tldr must carry $5.85")
IT = T["index.html"]
ck("$5.85" in IT, "index: markets card must carry $5.85")
ck("record $5.820 a gallon, one-tenth" not in IT, "index: stale diesel record still present")
ck("58%" in WT, "WS: AP twelve-month diesel figure absent")
ck("28 February 2026" in WT, "WS: war start date absent")

# ---- 5. markets: closure, closes, arithmetic -------------------------------
ck("Labor Day" in WT and "9:30" in WT, "WS: closure/reopen absent")
ck("7,718.60" in WT and "26,506.99" in WT and "53,414.25" in WT, "WS: Friday closes absent")
ck(abs((53686.11 - 271.86) - 53414.25) < 0.005, "WS: Dow arithmetic")
ck("162,000" in WT and "53,000" in WT and "4.1%" in WT, "WS: payrolls trio absent")
ck("97.39" in WT and "1.15%" in WT, "WS: Brent print absent")
# no VIX level may be asserted
ck(not re.search(r'VIX (?:at|is|of) \d', WT), "WS: a VIX level appears")
# no after-hours block on a holiday
ck("After-Hours Movers" not in W, "WS: after-hours section on a closed session")
ck("no extended-hours tape" in WT or "no after-hours" in WT.lower(), "WS: holiday after-hours note absent")

# ---- 6. cyber: countdowns, KEV, new CVE ------------------------------------
C = S["cyber-briefing.html"]; CT = T["cyber-briefing.html"]
import datetime
TODAY = datetime.date(2026, 9, 7)
for due, days in [(datetime.date(2026, 9, 18), 11), (datetime.date(2026, 9, 16), 9),
                  (datetime.date(2026, 9, 14), 7)]:
    ck((due - TODAY).days == days, "cyber countdown arithmetic for %s" % due)
    ck("(%d days left)" % days in CT, "cyber: missing '(%d days left)' countdown" % days)
ck("overdue by 2" in CT, "cyber: 5 September group must read 2 days overdue")
ck("Patch Priority" in CT, "cyber missing Patch Priority")
ck("14 September" in CT, "cyber: Patch Priority deadline absent")
# Patch Priority deadline must match the KEV section
ck(CT.count("14 September") >= 2, "cyber: 14 September must appear in both Patch Priority and KEV")
ck("BOD 26-04" in CT, "cyber: governing directive absent")
# new CVE
ck("CVE-2026-84147" in CT, "cyber: new CVE absent")
ck("Manacle" in CT, "cyber: affected product absent")
seg = CT[CT.find("CVE-2026-84147"): CT.find("CVE-2026-84147") + 1800]
ck("10.0" in seg, "cyber: CVSS 10.0 absent from the 84147 row")
ck("Disclosed, not exploited" in seg, "cyber: 84147 must be labelled disclosed-not-exploited")
ck("no CISA KEV" in seg, "cyber: 84147 must disclaim a KEV entry")
ck("days left" not in seg, "cyber: 84147 must carry no countdown")
# ScreenConnect card must carry no CVE id, no CVSS, no countdown
i = CT.find("ScreenConnect file transfers")
if i == -1: i = CT.find("ConnectWise")
sc = CT[i:i + 1200]
ck(not re.search(r'CVE-\d{4}-\d+', sc), "cyber: a CVE id appears in the ScreenConnect passage")
ck("no CVE, no score and no patch yet" in CT, "cyber: ScreenConnect status line absent")
ck("within the week" in CT, "cyber: ScreenConnect fix expectation absent")
ck("Threat Level" in CT or "threat level" in CT.lower(), "cyber missing threat-level banner")
ck("Threat Actor Spotlight" in CT, "cyber missing threat actor spotlight")
ck("Vulnerability Watch" in CT, "cyber missing vulnerability watch")

# ---- 7. MMA: champions, dates, day-of-week ---------------------------------
M = S["mma-briefing.html"]; MT = T["mma-briefing.html"]
CHAMPS = {"Tom Aspinall": "Heavyweight", "Carlos Ulberg": "Light Heavyweight",
          "Sean Strickland": "Middleweight", "Islam Makhachev": "Welterweight",
          "Justin Gaethje": "Lightweight", "Alexander Volkanovski": "Featherweight",
          "Petr Yan": "Bantamweight", "Joshua Van": "Flyweight",
          "Kayla Harrison": "Women's Bantamweight", "Mackenzie Dern": "Women's Strawweight",
          "Ciryl Gane": "Interim Heavyweight"}
for name in CHAMPS:
    ck(name in MT, "MMA: champion %s missing from the board" % name)
# known regressions must never be asserted as champions
for bad, div in [("Alex Pereira", "light heavyweight"), ("Khamzat Chimaev", "middleweight"),
                 ("Ilia Topuria", "lightweight"), ("Alexandre Pantoja", "flyweight"),
                 ("Merab Dvalishvili", "bantamweight")]:
    for m in re.finditer(re.escape(bad), MT):
        seg2 = MT[m.start(): m.start() + 90]
        pre = MT[max(0, m.start() - 60): m.start()]
        beaten = re.search(r'\b(SD|UD|KO\d?|TKO\d?|Sub\d?|over|beat|defeated|upset of)\s*$', pre.strip() + " ")
        ck(beaten is not None or "champion" not in seg2.lower() or "former" in seg2.lower()
           or "no longer" in seg2.lower() or "lost" in seg2.lower() or "interim" in seg2.lower(),
           "MMA: %s appears next to 'champion': %s" % (bad, seg2[:80]))
# Paris was a SATURDAY
ck("Friday" not in MT.split("Sources")[0] or "Saturday 5 September" in MT,
   "MMA: Paris day-of-week")
for m in re.finditer(r'Friday', MT):
    seg3 = MT[max(0, m.start() - 160): m.start() + 160]
    ck("Paris" not in seg3, "MMA: Paris still described as Friday: " + seg3[100:220])
ck("Saturday 5 September" in MT, "MMA: Paris date heading absent")
ck("Salahdine Parnasse" in MT, "MMA: main-event winner absent")
ck("Cody Salkilld" not in MT and "Saladhine" not in MT, "MMA: known misspelling present")
# (crude prefix heuristic removed: superseded by the per-occurrence loop below,
#  which is the correct implementation and does not false-positive on the page's
#  own explicit disclaimer "He is not a Dana White's Contender Series signee.")
# Parnasse must never be tied to the Contender Series
for m in re.finditer(r'Contender Series', MT):
    seg4 = MT[max(0, m.start() - 300): m.start() + 300]
    ck("Parnasse" not in seg4 or "not a Dana White" in seg4 or "is not a" in seg4,
       "MMA: Parnasse attributed to the Contender Series")
ck("ufccdn" in M, "MMA missing countdown element")
ck("Next card" in MT or "Next Card" in MT, "MMA missing next-card bar")
ck("Champions Board" in MT, "MMA missing champions board")
ck("subject to change" in MT, "MMA missing disclaimer")
# new items this edition
ck("+324" in MT and "-428" in MT.replace("−", "-"), "MMA: second odds route absent")
ck("14-fight win streak" in MT, "MMA: UFC 332 detail absent")
ck("Tracy Cortez" in MT, "MMA: Wang Cong's last result absent")

# ---- 8. index cards ---------------------------------------------------------
I = S["index.html"]
for cls in ["c-sec", "c-mkt", "c-mma"]:
    ck('class="card %s"' % cls in I, "index missing card %s" % cls)
ck(I.count("Read the briefing") == 3, "index needs 3 read links")
ck("tradingview" not in I.lower(), "index must carry no live widgets")
ck("CVE-2026-84147" in IT, "index: cyber card not synced")
ck("Saturday" in IT and "Friday" not in IT.split("Paris")[0][-200:], "index: MMA card day-of-week")

# ---- 9. provenance: no inherited "this run" claims survive ------------------
for p in ["cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"]:
    for m in re.finditer(r'this run', T[p]):
        seg5 = T[p][max(0, m.start() - 120): m.start() + 60]
        ck(False, "%s: stale 'this run' survived: %s" % (p, seg5[-120:]))

# ---- 10. sources footers ----------------------------------------------------
for p in ["cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"]:
    ck("Sources" in S[p], "%s missing sources footer" % p)
    ck(S[p].count("12:36 PM ET edition") >= 5, "%s: fewer than 5 sources added this edition" % p)
    ck("http" in S[p], "%s: no source URLs" % p)

# ---- 11. no secrets ---------------------------------------------------------
for p in PAGES:
    ck("github_pat" not in S[p], "%s: token leaked into page" % p)

print("checks run: %d" % checks)
if fails:
    print("FAILURES: %d" % len(fails))
    for f in fails: print("  -", f)
    sys.exit(1)
print("ALL PASS")
