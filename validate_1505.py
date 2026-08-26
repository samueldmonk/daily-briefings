#!/usr/bin/env python3
"""Programmatic validation, Aug 26 2026 3:05 p.m. ET edition. Arithmetic in Python, not grepped."""
import re, io, sys, html as H

D = "/sessions/festive-upbeat-carson/mnt/outputs/"
PAGES = {"index": "index.html", "cy": "cyber-briefing.html",
         "ws": "wallstreet-briefing.html", "mma": "mma-briefing.html"}
S = {k: io.open(D+v, encoding="utf-8").read() for k, v in PAGES.items()}

n = 0; bad = []
def ck(cond, msg):
    global n; n += 1
    if not cond: bad.append(msg)

def txt(s):
    s = re.sub(r'<script.*?</script>', ' ', s, flags=re.S)
    s = re.sub(r'<[^>]+>', ' ', s)
    s = H.unescape(s).replace('\u2212', '-').replace('\u00a0', ' ').replace('\u2014', '--')
    return re.sub(r'\s+', ' ', s)

T = {k: txt(v) for k, v in S.items()}

# ---------------------------------------------------------------- 1. index arithmetic
# (level, change, pct, prior_close, label)
QUADS = [
 # 9:59 board
 (7686.64,   9.36,  0.12, 7677.28,  "SPX 9:59"),
 (53594.69, 17.29,  0.03, 53577.40, "DJI 9:59"),
 (26173.36, 22.06,  0.08, 26151.30, "IXIC 9:59"),
 (3007.66, -2.36,  -0.08, 3010.02,  "RUT 9:59"),
 (15.51,    0.06,   0.39, 15.45,    "VIX 9:59"),
 (4680.70, -13.80, -0.29, 4694.50,  "Gold 9:59"),
 (81.52,   -0.84,  -1.02, 82.36,    "WTI 9:59"),
 # 11:59 board
 (7670.89,  -6.39,  -0.08, 7677.28,  "SPX 11:59"),
 (53474.94,-102.46, -0.19, 53577.40, "DJI 11:59"),
 (26060.89, -90.41, -0.35, 26151.30, "IXIC 11:59"),
 (3003.16,   -6.86, -0.23, 3010.02,  "RUT 11:59"),
 (4663.10,  -31.40, -0.67, 4694.50,  "Gold 11:59"),
 (82.32,     -0.04, -0.05, 82.36,    "WTI 11:59"),
 # 12:29 board
 (7665.46,  -11.82, -0.15, 7677.28,  "SPX 12:29"),
 (53425.42,-151.98, -0.28, 53577.40, "DJI 12:29"),
 (26049.37,-101.93, -0.39, 26151.30, "IXIC 12:29"),
 (3002.26,   -7.76, -0.26, 3010.02,  "RUT 12:29"),
 (15.59,      0.14,  0.91, 15.45,    "VIX 12:29"),
 (4654.20,  -40.30, -0.86, 4694.50,  "Gold 12:29"),
 (83.14,      0.78,  0.95, 82.36,    "WTI 12:29"),
 # 3:00 single-name strip
 (152.93,  44.03,  40.43, 108.90, "ANF 3:00"),
 (9.02,     3.75,  71.16, 5.27,   "XPON 3:00"),
 (575.47,   5.42,   0.95, 570.05, "META 3:00"),
 # ~2:58 strip
 (148.96,  40.06,  36.78, 108.90, "ANF 2:58"),
 (8.56,     3.29,  62.43, 5.27,   "XPON 2:58"),
 (341.35, -16.11,  -4.51, 357.46, "INTU 2:58"),
 (576.82,   6.77,   1.19, 570.05, "META 2:58"),
 # peers / earlier ticks
 (16.85,   -0.83,  -4.69, 17.68,  "KSS 9:59"),
 (44.84,    0.57,   1.29, 44.27,  "OKLO 9:59"),
]
for lvl, chg, pct, prior, lab in QUADS:
    ck(abs((lvl - chg) - prior) < 0.005, "%s: level-change != prior (%.2f vs %.2f)" % (lab, lvl-chg, prior))
    calc = chg / prior * 100.0
    ok = abs(round(calc, 2) - pct) < 0.005 or abs(int(calc*100)/100.0 - pct) < 0.005
    ck(ok, "%s: percent %.4f%% does not match stated %.2f%%" % (lab, calc, pct))
    ck(("%.2f" % abs(lvl)) in T["ws"] or ("{:,.2f}".format(abs(lvl))) in T["ws"],
       "%s: level %s absent from WS page" % (lab, lvl))

# INTU 3:00 -- deliberately one cent out; assert the page DISCLOSES it
ck(abs((339.18 + 18.29) - 357.47) < 0.005, "INTU 3:00 arithmetic setup wrong")
ck("one cent out" in T["ws"], "WS: INTU one-cent discrepancy not disclosed")
ck("357.47" in T["ws"] and "357.46" in T["ws"], "WS: both INTU bases must appear")
# HARNESS BUG FIXED: 18.29/357.46 = 5.1166% -> rounds to 5.12, TRUNCATES to 5.11.
# The feed truncates; require the page to say so rather than asserting a rounding.
_intu = 18.29/357.46*100
ck(abs(round(_intu, 2) - 5.12) < 0.005, "INTU 3:00: rounded percent should be 5.12")
ck(abs(int(_intu*100)/100.0 - 5.11) < 0.005, "INTU 3:00: truncated percent should be 5.11")
ck("truncated rather than rounded" in T["ws"], "WS: INTU percent truncation not disclosed")

# CRE -- percent must NOT reconcile, and the page must say so with the correct value
for lvl, chg, stated, correct in ((6.40, 3.83, 148.54, 149.03), (6.26, 3.69, 145.84, 143.58)):
    ck(abs((lvl - chg) - 2.57) < 0.005, "CRE %.2f: base is not 2.57" % lvl)
    calc = chg / 2.57 * 100.0
    ck(abs(round(calc, 2) - stated) > 0.01, "CRE %.2f: percent unexpectedly reconciles" % lvl)
    ck(abs(round(calc, 2) - correct) < 0.02, "CRE %.2f: correct percent is %.2f not %.2f" % (lvl, calc, correct))
    ck(("%.2f" % correct) in T["ws"], "WS: corrected CRE percent %.2f not printed" % correct)
ck("does not reconcile" in T["ws"], "WS: CRE non-reconciliation not stated")

# Bitcoin -- three DIFFERENT implied bases; assert all three printed and the rule stated
BTC = [(78410.76, -222.59, -0.28, 78633.35), (78049.39, -1457.77, -1.83, 79507.16),
       (78056.02, -1097.27, -1.39, 79153.29)]
bases = set()
for lvl, chg, pct, prior in BTC:
    ck(abs((lvl - chg) - prior) < 0.02, "BTC %.2f: implied base wrong" % lvl)
    ck(abs(round(chg/prior*100, 2) - pct) < 0.01, "BTC %.2f: percent off" % lvl)
    ck("{:,.2f}".format(prior) in T["ws"], "WS: BTC base %s not printed" % prior)
    bases.add(prior)
ck(len(bases) == 3, "BTC: expected three distinct bases, got %d" % len(bases))
ck("rolling 24-hour reference" in T["ws"], "WS: BTC rolling-base rule not stated")

# Session shape: 9:59 green -> 12:29 red on all three headline indices
ck(7686.64 > 7677.28 and 7665.46 < 7677.28, "SPX: green-then-red claim unsupported")
ck(53594.69 > 53577.40 and 53425.42 < 53577.40, "DJI: green-then-red claim unsupported")
ck(26173.36 > 26151.30 and 26049.37 < 26151.30, "IXIC: green-then-red claim unsupported")
ck("opened green and turned red" in T["ws"] and "opened green and turned red" in T["index"],
   "green-then-red phrasing missing from WS or index")
# Nasdaq worst of four at 12:29
p1229 = {"SPX": -0.15, "DJI": -0.28, "IXIC": -0.39, "RUT": -0.26}
ck(min(p1229, key=p1229.get) == "IXIC", "12:29: Nasdaq is not the worst of the four")

# Countdown -> clock derivations (close 16:00)
for hh, mm_, want in ((6, 1, "9:59"), (4, 1, "11:59"), (3, 31, "12:29")):
    mins = 16*60 - (hh*60 + mm_)
    got = "%d:%02d" % (mins//60 if mins//60 <= 12 else mins//60 - 12, mins % 60)
    ck(got == want, "countdown %dh %dm -> %s, page says %s" % (hh, mm_, got, want))
    ck(want in T["ws"], "WS: derived time %s not printed" % want)

# ---------------------------------------------------------------- 2. structural gates (WS widgets)
w = S["ws"]
ck(w.count("embed-widget-single-quote.js") == 3, "WS: single-quote widgets != 3")
for widget in ("ticker-tape", "timeline", "stock-heatmap", "mini-symbol-overview", "events"):
    ck(w.count("embed-widget-%s.js" % widget) == 1, "WS: %s widget count != 1" % widget)
tape = w[w.find("embed-widget-ticker-tape.js"):]
tape = tape[:tape.find("</script>")]
syms = re.findall(r'"proName":"([^"]+)"', tape)
ck(len(syms) == len(set(syms)), "WS: duplicate ticker-tape symbols")
for req in ("FOREXCOM:SPXUSD", "FOREXCOM:NSXUSD", "FOREXCOM:DJI", "TVC:USOIL", "TVC:US10Y"):
    ck(req in syms, "WS: mandatory tape symbol %s missing" % req)
mini = w[w.find("embed-widget-mini-symbol-overview.js"):]
mini = mini[:mini.find("</script>")]
ck('"symbol":"NYSE:ANF"' in mini, "WS: Chart of the Day is not NYSE:ANF")
ck("embed-widget" not in S["index"], "index.html must carry no TradingView widgets")

# ---------------------------------------------------------------- 3. nav (five tabs, one active)
ORDER = ["index.html", "cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html", "archive.html"]
for k, v in PAGES.items():
    nav = re.search(r'<nav class="tabs">(.*?)</nav>', S[k], re.S)
    ck(nav is not None, "%s: <nav class=\"tabs\"> missing" % k)
    if not nav: continue
    links = re.findall(r'<a[^>]*href="([^"]+)"[^>]*>', nav.group(1))
    ck(links == ORDER, "%s: nav order %s" % (k, links))
    ons = re.findall(r'<a([^>]*class="on"[^>]*)>', nav.group(1))
    ck(len(ons) == 1, "%s: expected exactly one active tab, got %d" % (k, len(ons)))
    if len(ons) == 1:
        ck(('href="%s"' % v) in ons[0], "%s: active tab is not %s" % (k, v))

# ---------------------------------------------------------------- 4. per-page furniture
for k in ("cy", "ws", "mma"):
    ck('id="freshline"' in S[k], "%s: #freshline missing" % k)
for k in PAGES:
    for el in ('id="edition"', 'id="datestamp"', 'id="updated"'):
        ck(el in S[k], "%s: %s missing" % (k, el))
ck('id="ufccdn"' in S["mma"], "mma: #ufccdn countdown missing")
ck(S["ws"].count('<div class="tldr">') == 1 and "The Tape" in S["ws"], "ws: tldr label")
ck(S["cy"].count('<div class="tldr">') == 1 and "The Wire" in S["cy"], "cy: tldr label")
ck(S["mma"].count('<div class="tldr">') == 1 and "Tale of the Tape" in S["mma"], "mma: tldr label")
ck('<div class="tldr">' not in S["index"], "index: should use cards, not a tldr strip")

# ---------------------------------------------------------------- 5. KEV board integrity
kev = S["cy"]
i = kev.find("CISA KEV")
i = kev.find("CISA KEV", i+1) if kev.count("CISA KEV") > 1 else i
lab = re.search(r'<div class="lab">[^<]*KEV[^<]*</div>', kev)
ck(lab is not None, "cy: KEV section label missing")
if lab:
    block = kev[lab.end():]
    block = block[:block.find('<div class="lab">')] if '<div class="lab">' in block else block
    spans = re.findall(r'class="kevdue (ok|crit)"[^>]*>([^<]*)<', block)
    ck(len(spans) == 14, "cy: KEV countdown spans = %d, expected 14" % len(spans))
    okc = sum(1 for c, _ in spans if c == "ok"); critc = len(spans) - okc
    ck(okc == 4 and critc == 10, "cy: KEV colour split %d ok / %d crit, expected 4/10" % (okc, critc))
    for cls, label in spans:
        lo = H.unescape(label).lower()
        # HARNESS BUG FIXED: the board renders overdue rows as "N days past due",
        # which the previous rule ("overdue"/"0 day") never matched.
        overdue = ("overdue" in lo or "past due" in lo or re.match(r'^\s*0 day', lo) is not None)
        ck((cls == "crit") == overdue, "cy: KEV span colour/text mismatch: %s / %s" % (cls, label))
# Patch Priority must match the board deadlines
tcy = T["cy"].replace("August", "Aug").replace("Aug.", "Aug")
ck("Aug 27" in tcy or "Aug 27" in tcy, "cy: Oracle Aug 27 deadline missing")
ck("Aug 28" in tcy, "cy: Gitea Aug 28 deadline missing")

# ---------------------------------------------------------------- 6. champions board
cb = S["mma"]
lab = re.search(r'<div class="lab">[^<]*Champions[^<]*</div>', cb, re.I)
ck(lab is not None, "mma: champions label missing")
if lab:
    blk = cb[lab.end():]
    end = blk.find('<div class="lab">')
    blk = blk[:end] if end > 0 else blk
    rows = re.findall(r'<tr>(.*?)</tr>', blk, re.S)
    ck(len(rows) == 12, "mma: champions rows = %d, expected 12 incl. header" % len(rows))
    champ_col = []
    for r in rows[1:]:
        cells = re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>', r, re.S)
        if len(cells) >= 2: champ_col.append(txt(cells[1]))
    ck(len(champ_col) == 11, "mma: %d incumbents, expected 11" % len(champ_col))
    joined = " ".join(champ_col)
    for stale in ("Pereira", "Chimaev", "Topuria", "vacant", "Vacant"):
        ck(stale not in joined, "mma: STALE champion in champion column: %s" % stale)
    for req in ("Aspinall", "Ulberg", "Strickland", "Makhachev", "Gaethje",
                "Volkanovski", "Yan", "Van", "Shevchenko", "Harrison", "Dern"):
        ck(req in joined, "mma: incumbent %s missing from champions board" % req)

# ---------------------------------------------------------------- 7. New-tag hygiene
for k in ("ws", "cy", "mma"):
    stale_cls = re.findall(r'class="tag new">New &middot; (?!3:05)([^<]*)</span>', S[k])
    ck(not stale_cls, "%s: tag-new class on non-3:05 label(s): %s" % (k, stale_cls))
    stale_txt = re.findall(r'New at (?!3:05)(\d?\d:\d\d)', S[k])
    ck(not stale_txt, "%s: stale 'New at' markers: %s" % (k, sorted(set(stale_txt))))
ck(S["ws"].count('class="tag new">New &middot; 3:05') == 3, "ws: expected 3 new-tagged cards")
ck(S["cy"].count('class="tag new">New &middot; 3:05') == 1, "cy: expected 1 new-tagged card")
ck("New at 3:05" in S["mma"], "mma: new item not tagged")

# ---------------------------------------------------------------- 8. index cards mirror their pages
ck("40.43" in T["index"] and "40.43" in T["ws"], "index/ws: ANF figure mismatch")
ck("71.16" in T["index"] and "71.16" in T["ws"], "index/ws: XPON figure mismatch")
ck("Gunra" in T["index"] and "Gunra" in T["cy"], "index/cy: Gunra mismatch")
ck("AA26-222A" in T["index"] and "AA26-222A" in T["cy"], "index/cy: advisory ID mismatch")
ck("UFC 331" in T["index"] and "UFC 331" in T["mma"], "index/mma: UFC 331 mismatch")
ck("twenty-fifth" in T["index"] and "twenty-fifth" in T["mma"], "index/mma: streak count mismatch")
ck("Aug 24" in T["index"].replace("Aug.", "Aug") and "Aug 24" in tcy, "index/cy: KEV date mismatch")

# ---------------------------------------------------------------- 9. chronology / descriptors
ck("Sept. 19" in T["mma"] or "Sept 19" in T["mma"].replace("Sept.", "Sept"), "mma: UFC 331 date missing")
ck("Aug. 29" in T["mma"] or "Aug 29" in T["mma"].replace("Aug.", "Aug"), "mma: Shanghai date missing")
for spell in ("Doo Ho Choi", "Robelis Despaigne", "Gable Steveson", "Mauricio Ruffy"):
    ck(spell in T["mma"], "mma: exact spelling missing: %s" % spell)

# ---------------------------------------------------------------- 10. trap greps
# HARNESS BUG FIXED: "slipped 0.12%" is a CONTEXT-ALLOWED string (it may be quoted
# inside a rejection), not a hard trap; it is checked in the window scan below.
TRAPS = ["Cody Salkilld", "Shamil Yakhyaev", "Abdul-Rakhman", "Fight Night 286",
         "$1.4 trillion", "Suno"]
# "Dooho Choi" likewise: banned except inside this run's self-correction note.
for k in PAGES:
    for t in TRAPS:
        ck(t not in T[k], "%s: trap string present: %s" % (k, t))
# context-allowed strings must sit inside a rejection window
def in_rejection(page, needle, span=1400):
    t = T[page]; out = True
    for m in re.finditer(re.escape(needle), t):
        w = t[max(0, m.start()-span): m.end()+span].lower()
        if not any(x in w for x in ("reject", "not adopted", "not asserted", "not published",
                                    "not used", "recorded and", "declined to adopt", "does not reconcile",
                                    "contradicts itself", "one cent out", "not a wednesday",
                                    "tuesday's close", "tuesday’s close", "corrected at")):
            out = False
    return out
for needle in ("Shanghai Indoor Stadium", "7,677.24", "30.68", "#6", "34%", "slipped 0.12%", "Dooho Choi"):
    for k in ("ws", "mma"):
        if needle in T[k]:
            ck(in_rejection(k, needle), "%s: '%s' appears outside a rejection window" % (k, needle))

# ---------------------------------------------------------------- 11. balance
for k in PAGES:
    s = S[k]
    ck(s.count("<div") == s.count("</div>"), "%s: div imbalance %d/%d" % (k, s.count("<div"), s.count("</div>")))
    ck(s.count("<script") == s.count("</script>"), "%s: script imbalance" % k)
    ck(s.count("<tr") == s.count("</tr>"), "%s: tr imbalance" % k)
    ck(s.count("<ul") == s.count("</ul>"), "%s: ul imbalance" % k)
    ck(s.count("<li>") == s.count("</li>"), "%s: li imbalance %d/%d" % (k, s.count("<li>"), s.count("</li>")))

print("checks: %d   failures: %d" % (n, len(bad)))
for b in bad: print("  FAIL:", b)
sys.exit(1 if bad else 0)
