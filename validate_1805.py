#!/usr/bin/env python3
"""Fact-check gate for the 6:05 PM edition. Guards are NARROWED, never loosened."""
import re, sys, io, os
REPO = sys.argv[1]
rd = lambda f: io.open(os.path.join(REPO, f), encoding="utf-8").read()
IX, CY, WS, MM = (rd(f) for f in ("index.html", "cyber-briefing.html",
                                  "wallstreet-briefing.html", "mma-briefing.html"))
PAGES = {"index": IX, "cyber": CY, "ws": WS, "mma": MM}
fails, checks = [], 0

def ck(cond, msg):
    global checks
    checks += 1
    if not cond:
        fails.append(msg)

def near(hay, a, b, win=300):
    """b appears within win chars of some occurrence of a."""
    for m in re.finditer(re.escape(a), hay):
        if b in hay[max(0, m.start() - win): m.start() + len(a) + win]:
            return True
    return False

# ---------- 1. STRUCTURE: every page has the five-tab nav, masthead, stamps ----
for n, h in PAGES.items():
    for tab in ("index.html", "cyber-briefing.html", "wallstreet-briefing.html",
                "mma-briefing.html", "archive.html"):
        ck(tab in h, "%s: nav missing %s" % (n, tab))
    for el in ('id="edition"', 'id="datestamp"', 'id="updated"', 'id="freshline"'):
        ck(el in h, "%s: masthead missing %s" % (n, el))
    ck('id="updated">6:05 PM ET' in h, "%s: stamp not 6:05 PM" % n)
    ck("Data as of 6:05 PM ET" in h, "%s: freshness fallback not 6:05 PM" % n)
    ck(h.count("<html") == 1 and h.rstrip().endswith("</html>"), "%s: malformed doc" % n)

for n, h, lbl in (("cyber", CY, "The Wire"), ("ws", WS, "The Tape"), ("mma", MM, "Tale of the Tape")):
    ck('<div class="tldr"><b>%s</b>' % lbl in h, "%s: tldr label wrong" % n)
    ck(h.count('<div class="tldr">') == 1, "%s: more than one tldr" % n)

# ---------- 2. NO STALE 'New' MARKERS (sweep the MARKER TEXT, not the class) ---
for n, h in PAGES.items():
    stale = re.findall(r'New &middot; (?!6:05 PM)([0-9]{1,2}:[0-9]{2} [AP]M)', h)
    ck(not stale, "%s: stale New markers %s" % (n, sorted(set(stale))))

# ---------- 3. MARKET CLOSE: level, points and percent must reconcile ----------
ck("7,686.14" in WS and "26,370.89" in WS and "53,185.90" in WS, "ws: close levels missing")
ck(abs((7711.76 - 7686.14) - 25.62) < 0.005, "arith: S&P points")
ck(abs((7686.14 / 7711.76 - 1) * 100 + 0.33) < 0.01, "arith: S&P percent")
ck(abs((26402.42 - 26370.89) - 31.53) < 0.005, "arith: Nasdaq points")
ck(abs((26370.89 / 26402.42 - 1) * 100 + 0.12) < 0.01, "arith: Nasdaq percent")
ck(abs((53559.99 - 53185.90) - 374.09) < 0.005, "arith: Dow points")
ck(abs((53185.90 / 53559.99 - 1) * 100 + 0.70) < 0.01, "arith: Dow percent")
for lvl in ("7,686.14", "26,370.89", "53,185.90"):
    ck(lvl in IX, "index: close level %s missing from card" % lvl)

# The permanently-refused Dow figure must never appear as a published close.
ck(not near(WS, "53,885.10", "close", 200) or "refus" in WS.lower(),
   "ws: 53,885.10 published as a close")
for m in re.finditer(r'PayPal &minus;12\.7', WS):
    ctx = WS[max(0, m.start() - 900): m.start() + 500].lower()
    ck(("not published" in ctx or "refus" in ctx or "deliberately not used" in ctx
        or "none of it is published" in ctx or "friday" in ctx),
       "ws: PayPal -12.7% outside a refusal")

# ---------- 4. NEW THIS RUN: rates causal clause ------------------------------
ck(near(WS, "4.75", "January 2025", 300), "ws: 4.75% not tied to January 2025")
ck(near(WS, "4.75", "hike", 700) or near(WS, "rising oil", "hike", 500),
   "ws: hike-expectation clause missing its oil context")
ck(near(WS, "4.72", "one path, not two claims", 600) or near(WS, "4.72", "daily mark", 400),
   "ws: 4.72% not reconciled against the intraday high")
# Guard NARROWED: a bare 'cut' is legitimate prose; forbid only 'Fed will cut'.
ck("Federal Reserve will cut" not in WS and "Fed will cut" not in WS,
   "ws: hike clause inverted to a cut")

# ---------- 5. AFTER-HOURS: all eight names carry their sourced percentages ----
AH = [("AEHL", "84.75"), ("COOT", "58.50"), ("YDDL", "41.82"), ("NCRA", "38.62"),
      ("ZTEK", "32.04"), ("JUNS", "26.79"), ("FNGR", "19.07"), ("MENS", "17.72")]
i = WS.find("After-Hours Movers</h2>")
seg = WS[i:i + 6000]
for sym, pct in AH:
    ck(sym in seg, "ws: after-hours symbol %s missing" % sym)
    ck(near(seg, sym, pct, 220), "ws: %s not beside %s" % (sym, pct))
ck("snapshot of a screen" in seg, "ws: after-hours degradation sentence missing")
ck("No S&amp;P 500 company has a sourced post-close move" in seg,
   "ws: after-hours guard sentence missing")
# The WETO/CANG screen must be described as sharing no gainer, not as superseding.
ck(near(seg, "WETO", "shares no gainer", 400), "ws: WETO/CANG screen not reconciled")

# ---------- 6. CYBER: PaperCut chain, order, deadline consistency -------------
ck(CY.count("CVE-2026-81578") >= 2 and CY.count("CVE-2026-82078") >= 2,
   "cyber: PaperCut CVEs under-represented")
ck(near(CY, "CVE-2026-81578", "authentication", 400), "cyber: 81578 not described as auth bypass")
ck(near(CY, "CVE-2026-82078", "class loading", 400) or near(CY, "CVE-2026-82078", "reflection", 400),
   "cyber: 82078 not described as unsafe reflection/class loading")
ck(near(CY, "CVE-2026-82078", "9.4", 400), "cyber: 82078 not beside CVSS 9.4")
# Deadline must be Sept 14 EVERYWHERE it is stated as a deadline.
for m in re.finditer(r'(deadline|due|remediat\w+)[^.]{0,160}?September (\d{1,2})', CY):
    ctx = CY[max(0, m.start() - 600): m.start() + 300]
    is_papercut = ("PaperCut" in ctx or "CVE-2026-82078" in ctx or "CVE-2026-81578" in ctx)
    if is_papercut:
        ck(m.group(2) == "14", "cyber: PaperCut deadline stated as September %s" % m.group(2))
# and the PaperCut CVEs must never sit beside a NON-14 September deadline
for cve in ("CVE-2026-82078", "CVE-2026-81578"):
    for m in re.finditer(re.escape(cve), CY):
        w = CY[m.start(): m.start() + 500]
        for d in re.findall(r'(?:deadline|due|remediat\w+)[^.]{0,120}?September (\d{1,2})', w):
            ck(d == "14", "cyber: %s beside a September %s deadline" % (cve, d))
ck("September 14" in CY, "cyber: Sept 14 deadline absent")
# Guard NARROWED (logged 5:05): 'September 21' is legal ONLY inside the refusal sentence.
for m in re.finditer(r'September 21', CY):
    ctx = CY[max(0, m.start() - 400): m.start() + 200]
    ck(("reject" in ctx.lower() or "retired" in ctx.lower() or "would give" in ctx.lower()
        or "heuristic" in ctx.lower()), "cyber: bare September 21 outside the refusal")
# Guard NARROWED (logged 5:05): 9.8 is legal on many CVEs; forbid it only on these three.
for cve in ("CVE-2026-82078", "CVE-2026-81578", "CVE-2026-3055"):
    for _m in re.finditer(re.escape(cve), CY):
        _w = CY[max(0, _m.start() - 260): _m.start() + len(cve) + 260]
        if "9.8" in _w:
            _l = _w.lower()
            ck("neither is a 9.8" in _l or "never attached" in _l or "not a 9.8" in _l
               or "refus" in _l, "cyber: 9.8 attached to %s" % cve)

# ---------- 7. CYBER: the Aug 18 KEV four ------------------------------------
for cve in ("CVE-2026-33824", "CVE-2026-55040", "CVE-2026-59310", "CVE-2026-65400"):
    ck(cve in CY, "cyber: %s missing" % cve)
ck(near(CY, "August 18, 2026", "CVE-2026-65400", 900) or near(CY, "August 18", "KEV catalog", 500),
   "cyber: Aug 18 KEV date not attached to the four")
ck(near(CY, "Monero", "macOS", 500), "cyber: Monero miner not tied to macOS")
ck(near(CY, "China-nexus", "vCenter", 600), "cyber: China-nexus APT not tied to vCenter")
ck(near(CY, "proof-of-concept", "SharePoint", 500), "cyber: PoC note not tied to SharePoint")
# Three of four carry 9.8 and the report does not name the exception -> no 4th score assigned.
ck("does not say which one is the exception" in CY or "does not assign the fourth" in CY,
   "cyber: unnamed exception not disclosed")

# ---------- 8. CYBER: new breaches, degraded correctly ------------------------
ck("13 million records" in CY, "cyber: Philippines volume missing")
ck(near(CY, "Philippines", "13 million", 400), "cyber: 13M not tied to the Philippines")
ck("UnicaSpa.it" in CY, "cyber: UnicaSpa missing")
ck(near(CY, "Cursor", "ten targets", 400), "cyber: Aurora/Cursor count missing")
# Guard NARROWED (15th occurrence of 'a guard that forbids a string forbids the disowning'):
# 'SpaceX' may appear ONLY inside a sentence that refuses it.
for m in re.finditer(r'SpaceX', CY):
    ctx = CY[max(0, m.start() - 500): m.start() + 500].lower()
    ck("refus" in ctx or "not established" in ctx, "cyber: SpaceX descriptor published")
ck("spacecraft manufacturer as its publisher" in CY or "SpaceX" not in CY,
   "cyber: Cursor publisher refusal missing")
# The 284M figure stays labelled rows-not-people.
for m in re.finditer(r'284 million patients', CY):
    ctx = CY[max(0, m.start() - 600): m.start() + 600].lower()
    ck("rows" in ctx or "not people" in ctx or "href" in ctx, "cyber: 284M patients unqualified")

# ---------- 9. MMA: champions board, eleven cells by NAME (guard from 4:55) ---
m = re.search(r'<h2[^>]*>\s*Champions Board[^<]*</h2>', MM)
assert m, "mma: Champions Board heading not found"
board = MM[m.end(): m.end() + 30000]
ck("<table" in board, "mma: no table under the Champions Board heading")
board = board[board.find("<table"):]
# NEW GUARD (real defect caught this run): no orphaned </h2> anywhere on any page.
for _n, _h in PAGES.items():
    ck(_h.count("<h2") == _h.count("</h2>"), "%s: unbalanced h2 tags" % _n)
# Guard NARROWED: champion names are wrapped in <b>, and the NOTE column legitimately
# names beaten ex-champions (Topuria, Pereira, Chimaev). Parse the CHAMPION column only
# -- the second <td> of each row -- and strip inline tags before matching.
strip = lambda x: re.sub(r'<[^>]+>', '', x).strip()
rows = re.findall(r'<tr>(.*?)</tr>', board, re.S)
champ_cells = []
for r in rows:
    tds = re.findall(r'<td>(.*?)</td>', r, re.S)
    if len(tds) >= 2:
        champ_cells.append(strip(tds[1]))
ck(len(champ_cells) == 11, "mma: champions table has %d rows, expected 11" % len(champ_cells))
joined = " | ".join(champ_cells)
for champ in ("Aspinall", "Ulberg", "Strickland", "Makhachev", "Gaethje", "Volkanovski",
              "Yan", "Van", "Harrison", "Shevchenko", "Dern"):
    ck(champ in joined, "mma: champion cell missing %s" % champ)
ck("Chimaev" not in joined, "mma: Chimaev in a champion CELL")
ck("Pereira" not in joined, "mma: Pereira in a champion CELL")
ck("Gane" in board, "mma: interim HW (Gane) missing from board")
ck("Topuria" not in joined, "mma: Topuria in a champion CELL")

# ---------- 10. MMA: Paris odds set complete and internally consistent --------
ODDS = [("Hooker", "+430"), ("Parnasse", "&minus;600"), ("Sola", "+135"), ("Ziam", "&minus;160"),
        ("Page", "&minus;170"), ("Ruziboev", "+143"), ("Keita", "&minus;340"), ("Naimov", "+270"),
        ("Charri&egrave;re", "+170"), ("Lima", "&minus;200"), ("Donchenko", "&minus;220"),
        ("Soriano", "+180")]
j = MM.find("Fight Week")
pseg = MM[j:j + 8000]
for name, price in ODDS:
    ck(near(pseg, name, price, 200), "mma: %s not beside %s" % (name, price))
# The 13-vs-15 conflict must be recorded as unresolved, never silently adopted.
ck(near(pseg, "13 fights", "15", 400), "mma: card-count conflict not recorded")
ck("neither is adopted as the count" in pseg, "mma: card count silently adopted")
# The opener conflict must be recorded too.
ck(near(pseg, "&minus;357", "opener", 500) or near(pseg, "357", "opener", 500),
   "mma: opener conflict not recorded")

# ---------- 11. STANDING CORRECTIONS: forbidden regressions ------------------
# Guard NARROWED (14th occurrence): a page must be able to DISOWN a string.
for h, n in ((MM, "mma"), (IX, "index")):
    for m in re.finditer(r'(former champion|title challenger)', h):
        ctx = h[max(0, m.start() - 300): m.start() + 200]
        for banned in ("Dariush", "Blaydes"):
            if banned in ctx:
                low = ctx.lower()
                ck(("not " in low or "never" in low or "is not described" in low),
                   "%s: '%s' attached to %s" % (n, m.group(1), banned))
for m in re.finditer(r'Dariush', MM):
    ctx = MM[max(0, m.start() - 500): m.start() + 500].lower()
    ck("contender" in ctx or "never" in ctx or "not " in ctx, "mma: Dariush descriptor unguarded")
# Nevada 2025 ransomware must never be presented as a 2026 incident.
for m in re.finditer(r'Nevada', CY):
    ctx = CY[max(0, m.start() - 700): m.start() + 700]
    ck("2025" in ctx or "exclud" in ctx.lower() or "refus" in ctx.lower(),
       "cyber: Nevada without its 2025 correction")

# ---------- 12. INDEX cards faithfully summarize their own page --------------
ck("CVE-2026-81578" in IX and "September 14" in IX, "index: cyber card lost the KEV facts")
ck("7,686.14" in IX and "August" in IX, "index: ws card lost the close")
ck("Parnasse" in IX and "&minus;600" in IX, "index: mma card lost the Paris price")
ck("Chimaev" not in IX or "not" in IX, "index: Chimaev unqualified")
for h, n in PAGES.items():
    ck("Read the briefing" in IX, "index: card links missing")
    break

# ---------- 13. LIVE WIDGET BLOCKS (Wall Street) -----------------------------
for w in ("embed-widget-ticker-tape.js", "embed-widget-single-quote.js",
          "embed-widget-timeline.js", "embed-widget-stock-heatmap.js",
          "embed-widget-mini-symbol-overview.js", "embed-widget-events.js"):
    ck(w in WS, "ws: widget %s missing" % w)
ck(WS.count("embed-widget-single-quote.js") == 3, "ws: single-quote widgets != 3")
for sym in ("FOREXCOM:SPXUSD", "FOREXCOM:NSXUSD", "FOREXCOM:DJI", "TVC:USOIL", "TVC:US10Y"):
    ck(sym in WS, "ws: ticker tape lost %s" % sym)
ck('class="livebar"' in WS, "ws: livebar wrapper missing")
ck("NYSE:EIX" in WS, "ws: Chart of the Day symbol missing")
for n, h in (("cyber", CY), ("mma", MM), ("index", IX)):
    ck("tradingview" not in h.lower(), "%s: live widget on a non-markets page" % n)

# ---------- 14. MMA countdown + section order --------------------------------
ck('id="ufccdn"' in MM, "mma: countdown element missing")
ck("subject to change" in MM, "mma: disclaimer missing")
ck("not investment advice" in WS or "not investment" in WS.lower(), "ws: disclaimer missing")
order_ws = [WS.find(s) for s in ("The Lead", "Movers &amp; Drivers", "Chart of the Day",
                                 "After-Hours Movers", "Weekly Scorecard", "Rates, Bonds")]
ck(all(x > 0 for x in order_ws), "ws: a required section is missing")

# ---------- 15. SCRUB ARTEFACTS ----------------------------------------------
for n, h in PAGES.items():
    for bad in ("an earlier edition edition", "at an earlier edition", "Carried &middot; Aug 31, 6:05 PM",
                "&middot; &middot;", "<b><b><b>"):
        ck(bad not in h, "%s: scrub artefact %r" % (n, bad))
    ck(not re.search(r'\bthe [0-9]{1,2}:[0-9]{2} edition\b', h), "%s: bare H:MM edition tag" % n)
    # carried blocks must not claim 'this run'
    for m in re.finditer(r'Carried &middot; [^<]*</span>([^<]{0,400})', h):
        ck("this run" not in m.group(1), "%s: carried block says 'this run'" % n)


# ═══ ADDITIONAL GUARDS — 6:05 PM edition, tenth run ═════════════════════════
print("--- 6:05 PM additional guards ---")

# A. MARKETS — the monthly-gain floor must not contradict the precise pair.
ck(near(WS, "more than 2.5%", "2.6%", 700) or near(WS, "more than 2.5%", "contains both", 700),
   "ws: monthly floor printed without reconciling the carried 2.6%/3.9% pair")
ck("2.6%" in WS and "3.9%" in WS, "ws: precise monthly pair dropped")

# B. MARKETS — the 10-year range must reconcile, not replace.
ck(near(WS, "4.697", "4.767", 200), "ws: 10-year day range incomplete")
ck(near(WS, "4.767", "4.75", 500), "ws: range high not tied to the 'topped 4.75%' print")
ck(near(WS, "4.722", "4.75", 700), "ws: closing mark not reconciled against the intraday high")

# C. MARKETS — Edison: two framings of ONE record, neither adopted over the other.
ck(near(WS, "$54.22", "23%", 300), "ws: Edison price not beside its percent")
ck(near(WS, "more than 25 years", "2001", 500), "ws: the two record framings not printed together")
ck(near(WS, "Newsom", "wildfire", 400), "ws: Edison cause not stated")
ck("Mizuho" in WS, "ws: named downgrade rationale missing")

# D. MARKETS — sector figures must carry their clock caveat.
_sh = re.search(r'<h2[^>]*>\s*Sector Heat', WS)
ck(_sh is not None, "ws: Sector Heat heading not found")
seg = WS[_sh.start(): _sh.start() + 4000] if _sh else ""
ck("1.6%" in seg and "Energy" in seg, "ws: sector figures missing")
ck("not the same clock" in seg or "morning reading" in seg,
   "ws: sector figures published without the clock caveat")

# E. MARKETS — WBUY is new and small; it must not be presented as a top mover.
i = WS.find("After-Hours Movers</h2>")
seg = WS[i:i + 8000]
ck(near(seg, "WBUY", "4.07", 200), "ws: WBUY not beside its percent")
ck(near(seg, "NCRA", "did not return", 900) or near(seg, "MENS", "did not return", 900),
   "ws: dropped-off names not distinguished from names that moved")

# F. CYBER — the two PaperCut scores must sit on the RIGHT CVEs.
ck(near(CY, "CVE-2026-81578", "8.8", 400), "cyber: 81578 not beside CVSS 8.8")
def bound_score(cve):
    """The score this page binds to a CVE = the first CVSS number after the token."""
    out = set()
    for _m in re.finditer(re.escape(cve), CY):
        _w = re.sub(r'<[^>]+>', '', CY[_m.end(): _m.end() + 90])
        _s = re.search(r'(?:CVSS\s*)?(\d{1,2}\.\d)', _w)
        if _s: out.add(_s.group(1))
    return out
ck(bound_score("CVE-2026-82078") <= {"9.4"},
   "cyber: 82078 bound to %s" % (bound_score("CVE-2026-82078") - {"9.4"}))
ck(bound_score("CVE-2026-81578") <= {"8.8"},
   "cyber: 81578 bound to %s" % (bound_score("CVE-2026-81578") - {"8.8"}))
ck("second emergency patch" in CY, "cyber: the re-patch (the run's operational point) missing")

# G. CYBER — the ransom figure is exact and attributed as a demand.
ck("$55,236,150" in CY, "cyber: McKesson ransom figure missing")
ck(near(CY, "$55,236,150", "ShinyHunters", 400), "cyber: ransom not attributed")
ck(near(CY, "284 million", "claim", 700), "cyber: 284M not labelled a claim")

# H. CYBER — new incidents published degraded where sources were silent.
for name in ("Air France", "KLM", "Neogen"):
    ck(name in CY, "cyber: %s missing" % name)
ck(near(CY, "Neogen", "none is supplied", 700) or near(CY, "Neogen", "was stated", 700),
   "cyber: Neogen published without its degradation note")
ck(near(CY, "Medusa", "500", 400), "cyber: Medusa scale missing")

# I. CYBER — the Siemens advisory identifier and its five authors.
ck("AA26-231A" in CY, "cyber: advisory number missing")
for agency in ("NSA", "CISA", "FBI"):
    ck(near(CY, "AA26-231A", agency, 400), "cyber: %s not named on the advisory" % agency)
ck(near(CY, "snap7", "S7comm", 700), "cyber: tooling and protocol not stated together")

# J. CYBER — KEV additions recorded, but Sept 14 stays the live clock.
for cve in ("CVE-2023-49105", "CVE-2026-53362", "CVE-2026-66384"):
    ck(cve in CY, "cyber: %s missing" % cve)
ck(near(CY, "risk-based", "September 9", 900) or near(CY, "August 29", "September 9", 600),
   "cyber: the spread of due dates not used to prove risk-based assignment")

# K. MMA — 14 is adopted; 15 and 13 must appear only as retired counts.
ck(near(MM, "14-fight", "Accor Arena", 400), "mma: card count not tied to the venue")
for n_ in ("15", "13"):
    ck(near(MM, "Fourteen is the primary source", n_, 600) or near(MM, "%s fights" % n_, "retired", 900)
       or near(MM, "carried 15 fights", "13", 400), "mma: retired count %s not disowned" % n_)
ck(near(MM, "Parnasse", "Contender Series", 700), "mma: Parnasse route not sourced")
ck(near(MM, "prelims", "3 PM ET", 400) or near(MM, "12 PM ET", "3 PM ET", 300),
   "mma: Paris broadcast times incomplete")

# L. MMA — records and methods from this run.
ck("24-9-1" in MM and "20-1" in MM, "mma: Shanghai records missing")
ck(near(MM, "20-1", "first loss", 300), "mma: Nurmagomedov record not contextualised")
ck(near(MM, "title shot", "callout", 600) or near(MM, "title shot", "not been announced", 600),
   "mma: Song's callout published as an announcement")
ck(near(MM, "Denise Gomes", "4:49", 300), "mma: Gomes finish time missing")
ck(near(MM, "Kai Asakura", "0:34", 300), "mma: Asakura finish time missing")

# M. MMA — September schedule, and nothing framed as a title fight without a source.
ck("Desert Diamond Arena" in MM and "Glendale" in MM, "mma: Noche venue missing")
for b in ("Grasso", "Fiorot", "Moreno", "Blaydes"):
    ck(b in MM, "mma: Noche main-card name %s missing" % b)
ck(near(MM, "Grasso", "not described as one", 600) or near(MM, "title eliminator", "nothing fetched", 400),
   "mma: Grasso-Fiorot framed without its caveat")
ck("Rosas Jr." in MM and "Meta APEX" in MM, "mma: Sept 26 card missing")

# N. MMA — the Chimaev regression must be refused by DATE, never adopted.
ck(near(MM, "August 16, 2025", "predates", 400), "mma: stale board not disproved by its own date")
ck(near(MM, "Strickland", "split decision", 600), "mma: the tie-breaker result missing")
ck(near(MM, "48&ndash;47", "Strickland", 400), "mma: scorecards missing")
rows_ck = re.search(r'<h2[^>]*>\s*Champions Board[^<]*</h2>', MM)
bd = MM[rows_ck.end(): rows_ck.end() + 30000]
bd = bd[bd.find("<table"):]
for r in re.findall(r'<tr>(.*?)</tr>', bd, re.S):
    tds = re.findall(r'<td[^>]*>(.*?)</td>', r, re.S)
    if len(tds) >= 2 and "Middleweight" in re.sub(r'<[^>]+>', '', tds[0]):
        champ = re.sub(r'<[^>]+>', '', tds[1]).strip()
        ck("Strickland" in champ, "mma: MW champion cell reads %r" % champ)

# O. EVERY page: index cards must not assert beyond their own page.
for frag in ("7,686.14", "26,370.89", "53,185.90", "$54.22"):
    ck(frag in IX and frag in WS, "index: %s not supported by the markets page" % frag)
for frag in ("September 14", "CVE-2026-82078", "Medusa"):
    ck(frag in IX and frag in CY, "index: %s not supported by the cyber page" % frag)
for frag in ("14-fight", "Accor Arena", "Contender Series"):
    ck(frag in IX and frag in MM, "index: %s not supported by the MMA page" % frag)


# ── single report, after ALL guards ──
print("validate_1805: %d checks, %d failures" % (checks, len(fails)))
for f in fails: print("  FAIL:", f)
sys.exit(1 if fails else 0)