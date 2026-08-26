#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Programmatic validation harness — 2026-08-26 ~3:12pm ET edition.
All arithmetic computed in Python; no figure is asserted from memory."""
import re, sys, os, datetime, html

D = sys.argv[1] if len(sys.argv) > 1 else "."
PAGES = ["index.html", "cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"]
S = {p: open(os.path.join(D, p), encoding="utf-8").read() for p in PAGES}
TXT = {p: html.unescape(re.sub(r"<[^>]+>", " ", s)) for p, s in S.items()}
TODAY = datetime.date(2026, 8, 26)

checks = 0; fails = []
def ok(cond, msg):
    global checks
    checks += 1
    if not cond: fails.append(msg)

# ---------------------------------------------------------------- 1. quote arithmetic
# (level, change, pct, expected_prior_close, name)  change signed
QUAD = [
    (7670.01,  -7.27,   -0.09, 7677.28, "S&P 500 @12:05"),
    (53455.18, -122.22, -0.23, 53577.40, "Dow 30 @12:05"),
    (26063.23, -88.07,  -0.34, 26151.30, "Nasdaq @12:05"),
    (15.45,     0.00,    0.00, 15.45,    "VIX @12:05"),
    (4655.50,  -39.00,  -0.83, 4694.50,  "Gold @12:05"),
    (82.88,     0.52,    0.63, 82.36,    "WTI Oct-26 @12:05"),
]
for lvl, chg, pct, prior, name in QUAD:
    ok(abs((lvl - chg) - prior) < 0.005, "%s: level-change=%.2f != prior %.2f" % (name, lvl - chg, prior))
    if prior:
        calc = chg / prior * 100.0
        ok(abs(round(calc, 2) - pct) < 0.005 or abs(int(calc * 100) / 100.0 - pct) < 0.005,
           "%s: pct %.4f%% neither rounds nor truncates to %.2f" % (name, calc, pct))

# Russell: the one-cent case must be present AND disclosed on the page
r_lvl, r_chg, r_prior = 3002.71, -7.32, 3010.02
ok(abs((r_lvl - r_chg) - 3010.03) < 0.005, "Russell: implied base is not 3,010.03")
ok(abs((r_lvl - r_chg) - r_prior) > 0.005, "Russell: one-cent gap vanished; check the published close")
ok("one cent out" in TXT["wallstreet-briefing.html"], "Russell one-cent artefact not disclosed on the page")

# Bitcoin: rolling reference — bases must differ and NO staleness claim may be made from it
btc = [(78100.48, -1052.82, -1.33), (78998.81, -907.00, -1.14)]
bases = []
for lvl, chg, pct in btc:
    b = lvl - chg
    bases.append(round(b, 2))
    calc = chg / b * 100.0
    ok(abs(round(calc, 2) - pct) < 0.005, "BTC: %.4f%% does not round to %.2f on its own base %.2f" % (calc, pct, b))
ok(len(set(bases)) == len(bases), "BTC bases coincide; the rolling-reference finding would be wrong")
ok(abs(bases[0] - 79153.30) < 0.005, "BTC 12:05 base is not 79,153.30")
ok(abs(bases[1] - 79905.81) < 0.005, "BTC pre-session base is not 79,905.81")
ok("rolling" in TXT["wallstreet-briefing.html"], "Bitcoin rolling-reference caveat missing")

# Tuesday-close strip carried on the page must still reconcile
STRIP = [(153.40, 44.50, 40.86, 108.90, "ANF"), (8.86, 3.59, 68.12, 5.27, "XPON"),
         (339.41, -18.05, -5.05, 357.46, "INTU"), (577.46, 7.41, 1.30, 570.05, "META")]
for lvl, chg, pct, prior, name in STRIP:
    ok(abs((lvl - chg) - prior) < 0.005, "%s strip: base %.2f != %.2f" % (name, lvl - chg, prior))
    calc = chg / prior * 100.0
    ok(abs(round(calc, 2) - pct) < 0.01 or abs(int(abs(calc) * 100) / 100.0 - abs(pct)) < 0.005,
       "%s strip: pct %.4f does not reconcile to %.2f" % (name, calc, pct))

# ---------------------------------------------------------------- 2. KEV countdowns vs printed due dates
MON = {m: i for i, m in enumerate(
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], 1)}
# HARNESS FIX: scope by the SECTION LABEL (case-insensitive) and stop at that section's end.
# A bare find("CISA KEV") matches the stat strip 56k characters earlier and drags the whole
# document into scope — the same class of bug caught at 2:44, recurring with a new spelling.
kev_sec = S["cyber-briefing.html"]
m_lab = re.search(r'<div class="lab">CISA KEV[^<]*</div>', kev_sec, flags=re.I)
ok(m_lab is not None, "KEV section label not found")
if m_lab:
    end = kev_sec.find("</section>", m_lab.end())
    sec = kev_sec[m_lab.end(): end if end > 0 else len(kev_sec)]
else:
    sec = ""
# HARNESS FIX: the separator group was written `&nbsp;?`, which makes only the SEMICOLON
# optional and therefore *demands* the literal characters "&nbsp" — so every row with a plain
# space ("Aug 27") failed to match and the board parsed as empty. Correct form below.
rows = re.findall(
    r'due <b>((?:Aug|Sep|Oct|Jul)\w*(?:&nbsp;|\s)*\d{1,2})</b>.*?<span class="kevdue (ok|crit)">([^<]+)</span>',
    sec)
ok(len(rows) >= 12, "KEV board: only %d date/countdown pairs parsed (expected >=12)" % len(rows))
past_due = 0
for datestr, cls, label in rows:
    d = html.unescape(datestr).replace("\xa0", " ").split()
    mon, day = MON[d[0][:3]], int(d[1])
    due = datetime.date(2026, mon, day)
    delta = (due - TODAY).days
    lab = html.unescape(label)
    if delta > 0:
        ok(cls == "ok", "KEV %s: future deadline coloured %s" % (due, cls))
        ok(str(delta) in lab and "left" in lab, "KEV %s: label %r != %d days left" % (due, lab, delta))
    else:
        past_due += 1
        ok(cls == "crit", "KEV %s: overdue/today row coloured %s" % (due, cls))
        ok("past due" in lab or "today" in lab or "0 day" in lab, "KEV %s: label %r not an overdue form" % (due, lab))
ok(past_due == 10, "KEV board: %d past-due rows, page claims 10" % past_due)

# Patch Priority must name the same two dates as the board (month spelling normalised)
pp = TXT["cyber-briefing.html"]
pp_norm = pp.replace("August", "Aug").replace("September", "Sep")
ok("Aug 27" in pp_norm or "Aug 27" in pp_norm, "Patch Priority: Oracle Aug 27 missing")
ok("Aug 28" in pp_norm or "Aug 28" in pp_norm, "Patch Priority: Gitea Aug 28 missing")
ok((datetime.date(2026, 8, 27) - TODAY).days == 1, "Oracle deadline is not 1 day out from today")

# ---------------------------------------------------------------- 3. new items must NOT be claimed as KEV
for cve in ["CVE-2026-58231", "CVE-2026-47301"]:
    ok(cve in S["cyber-briefing.html"], "%s missing from the cyber page" % cve)
    # every mention must sit near an explicit not-in-KEV statement.
    # HARNESS FIX: the window was forward-only, so a qualifier stated BEFORE the second
    # mention in a paragraph false-failed. The window is now bidirectional.
    for m in re.finditer(re.escape(cve), TXT["cyber-briefing.html"]):
        w = TXT["cyber-briefing.html"][max(0, m.start() - 1600): m.start() + 1600]
        ok("Not in KEV" in w or "NOT in CISA KEV" in w or "not added to KEV" in w or "not added" in w or "outside KEV" in w,
           "%s: a mention without a not-in-KEV qualifier" % cve)
# HARNESS FIX: the leak test scanned the whole KEV SECTION, which legitimately contains the
# prose note explaining that both new CVEs are OUTSIDE KEV. The test must scan the board ROWS.
board_rows = " ".join(l for l in re.findall(r"<li>(.*?)</li>", sec, flags=re.S) if "kevdue" in l)
ok("58231" not in board_rows, "CVE-2026-58231 leaked onto the KEV board rows")
ok("47301" not in board_rows, "CVE-2026-47301 leaked onto the KEV board rows")
ok(board_rows.count("kevdue") == 14, "KEV board: %d rows, page claims 14" % board_rows.count("kevdue"))

# ---------------------------------------------------------------- 4. champions board (CHAMPION COLUMN ONLY)
mma = S["mma-briefing.html"]
j = mma.find("Champions Board")
if j < 0: j = mma.find("Champions board")
cb = mma[j:] if j >= 0 else ""
champ_col = []
for tr in re.findall(r"<tr>(.*?)</tr>", cb, flags=re.S):
    tds = re.findall(r"<td[^>]*>(.*?)</td>", tr, flags=re.S)
    if len(tds) >= 2:
        champ_col.append(html.unescape(re.sub(r"<[^>]+>", " ", tds[1])))
champs = " | ".join(champ_col)
ok(len(champ_col) >= 10, "Champions board: only %d rows parsed" % len(champ_col))
REQUIRED = ["Aspinall", "Ulberg", "Strickland", "Makhachev", "Gaethje", "Volkanovski",
            "Yan", "Van", "Shevchenko", "Harrison", "Dern"]
for n in REQUIRED:
    ok(n in champs, "Champions column: %s missing" % n)
for bad in ["Pereira", "Chimaev", "Topuria", "vacant", "Vacant"]:
    ok(bad not in champs, "Champions COLUMN contains a superseded name/state: %s" % bad)

# ---------------------------------------------------------------- 5. trap greps
HARD = ["Cody Salkilld", "Shamil Yakhyaev", "Abdul-Rakhman", "Fight Night 286", "$1.4 trillion", "Suno"]
for p in PAGES:
    for t in HARD:
        ok(t not in TXT[p], "%s: hard trap string present: %r" % (p, t))
# window-scoped: allowed only inside a rejection/correction context
WINDOWED = {"wallstreet-briefing.html": ["7,677.24", "30.68", "41.8", "slipped 0.12%"],
            "mma-briefing.html": ["Shanghai Indoor Stadium", "Dooho Choi"]}
# HARNESS FIX: the context vocabulary was too narrow — the page's genuine rejection language
# uses "discrepancy", "not adopted", "declined to adopt", "Tuesday's close", "stale strip" and
# "not a Wednesday move", none of which were listed, so eight correctly-scoped mentions failed.
CONTEXT = ["reject", "Reject", "REJECT", "correct", "Correct", "CORRECT", "not published",
           "NOT published", "does not reconcile", "no Wednesday", "No Wednesday", "⚠",
           "discrepancy", "not adopted", "declined to adopt", "stale strip", "carried forward",
           "not a Wednesday", "that was Tuesday", "Tuesday close", "Tuesday's close",
           "Tuesday’s close", "on Tuesday", "is not published"]
for p, strs in WINDOWED.items():
    for t in strs:
        for m in re.finditer(re.escape(t), TXT[p]):
            w = TXT[p][max(0, m.start() - 700): m.start() + 700]
            ok(any(c in w for c in CONTEXT), "%s: %r appears outside a rejection window" % (p, t))

# ---------------------------------------------------------------- 6. new-tag hygiene (CLASS, not just label)
for p in PAGES:
    for m in re.finditer(r'class="tag new"[^>]*>([^<]*)', S[p]):
        ok("3:12" in html.unescape(m.group(1)),
           "%s: tag new carries a stale stamp %r" % (p, m.group(1).strip()))
ok(S["wallstreet-briefing.html"].count('class="tag new"') >= 1, "WS: no new tag this edition")
ok(S["cyber-briefing.html"].count('class="tag new"') >= 2, "CY: expected 2 new CVE tags")

# ---------------------------------------------------------------- 7. structure
NAV = ["index.html", "cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html", "archive.html"]
for p in PAGES:
    for h in NAV:
        ok(('href="%s"' % h) in S[p], "%s: nav link to %s missing" % (p, h))
    for el in ['id="edition"', 'id="datestamp"', 'id="updated"']:
        ok(el in S[p], "%s: masthead pill %s missing" % (p, el))
    ok("America/New_York" in S[p], "%s: self-stamp JS missing" % p)
for p, lab in [("wallstreet-briefing.html", "The Tape"), ("cyber-briefing.html", "The Wire"),
               ("mma-briefing.html", "Tale of the Tape")]:
    ok(('<div class="tldr"><b>%s</b>' % lab) in S[p], "%s: tldr label %r missing" % (p, lab))
    ok('id="freshline"' in S[p], "%s: freshline missing" % p)
ok('<div class="tldr"' not in S["index.html"], "index.html should show cards, not a tldr strip")
for cls in ["bcard c-sec", "bcard c-mkt", "bcard c-mma"]:
    ok(cls in S["index.html"], "index.html: %s card missing" % cls)

# TradingView blocks A-F on Wall Street
WIDGETS = ["embed-widget-ticker-tape", "embed-widget-single-quote", "embed-widget-timeline",
           "embed-widget-stock-heatmap", "embed-widget-mini-symbol-overview", "embed-widget-events"]
for w in WIDGETS:
    ok(w in S["wallstreet-briefing.html"], "WS: live widget %s missing" % w)
ok(S["wallstreet-briefing.html"].count("embed-widget-single-quote") == 3, "WS: expected 3 single-quote widgets")
for sym in ["FOREXCOM:SPXUSD", "FOREXCOM:NSXUSD", "FOREXCOM:DJI", "TVC:USOIL", "TVC:US10Y"]:
    ok(sym in S["wallstreet-briefing.html"], "WS ticker tape: %s missing" % sym)
ok("ufccdn" in S["mma-briefing.html"], "MMA: countdown element missing")
for p in PAGES[1:]:
    ok("Sources" in TXT[p], "%s: sources footer missing" % p)

# ---------------------------------------------------------------- 8. chronology / consistency
ok("Aug. 29" in TXT["mma-briefing.html"] or "Aug 29" in TXT["mma-briefing.html"] or "August 29" in TXT["mma-briefing.html"],
   "MMA: next card date Aug 29 missing")
ok((datetime.date(2026, 8, 29) - TODAY).days == 3, "MMA: Shanghai is not 3 days out from today")
ok("twenty-sixth" in TXT["mma-briefing.html"], "MMA: champions-board streak not incremented")
ok("eleventh" in TXT["cyber-briefing.html"], "CY: KEV-static streak not incremented")
ok("fourth consecutive run" in TXT["wallstreet-briefing.html"], "WS: TheStreet empty-body streak missing")

print("checks: %d   failures: %d" % (checks, len(fails)))
for f in fails: print("  FAIL:", f)
sys.exit(1 if fails else 0)
