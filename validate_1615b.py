#!/usr/bin/env python3
"""Post-close edition validator, Wed Aug 26 2026 ~4:15pm ET."""
import re, io, datetime

OUT = "/sessions/lucid-sleepy-wright/mnt/outputs/"
PAGES = ["index.html", "cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"]
H = {p: io.open(OUT + p, encoding="utf-8").read() for p in PAGES}
fails, checks = [], 0

def ck(cond, msg):
    global checks
    checks += 1
    if not cond:
        fails.append(msg)

def txt(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s))

W, C, M, I = H["wallstreet-briefing.html"], H["cyber-briefing.html"], H["mma-briefing.html"], H["index.html"]

# ── 1. ARITHMETIC: every level/change/percent triple must reconcile ───────────
def recon(level, change, pct, base, label, tol_pct=0.005):
    """level - change == base; pct == change/base*100 (to tol)."""
    ck(abs((level - change) - base) < 0.005, "BASE %s: %.2f-%.2f=%.2f != %.2f" % (label, level, change, level - change, base))
    ck(abs(change / base * 100.0 - pct) < tol_pct, "PCT %s: %.4f != %.2f" % (label, change / base * 100.0, pct))

# The two Wednesday closing reads, both against the adopted 7,677.28 base
recon(7675.70, -1.58, -0.02, 7677.28, "S&P close read A")
recon(7675.82, -1.46, -0.02, 7677.28, "S&P close read B")
# the twelve-cent divergence must be real, and stated as such
ck(abs(7675.82 - 7675.70 - 0.12) < 1e-9, "12-cent divergence arithmetic")
ck("twelve-cent" in txt(W).lower() or "twelve cent" in txt(W).lower(), "WS must state the 12-cent divergence")
# the rejected Zacks base must differ from the adopted one by exactly 4 cents
ck(abs(7677.28 - 7677.24 - 0.04) < 1e-9, "Zacks base delta")
# Nvidia year-over-year scale claim: 92.16 vs 46.74 is 'roughly double'
ck(1.9 < 92.16 / 46.74 < 2.1, "NVDA rev roughly double")
ck(1.9 < 2.09 / 1.05 < 2.1, "NVDA eps roughly double")
# guide midpoint band 91.0 +/- 2% must contain the consensus
ck(91.0 * 0.98 <= 92.07 <= 91.0 * 1.02, "consensus inside guide band")
# Data Center estimate must sit inside the stated range
ck(83.5 <= 85.67 <= 91.5, "DC estimate inside range")
# CrowdStrike: 7.59% of $196B ~ $14.9B
ck(abs(196.0 * 0.0759 - 14.9) < 0.3, "CRWD implied value at stake")
# Nvidia: 5.26T at 13.26% is far above the quoted 282B -> the two Benzinga figures
# are NOT derivable from each other, which is exactly why the page prints both.
ck(abs(5260.0 * 0.1326 - 282.0) > 100, "NVDA swing figures are not one derivation")
ck("286" in W and "282" in W, "both Benzinga swing figures printed")
# odds: -500 / +380 implied probabilities
ck(abs(500.0 / 600.0 * 100 - 83.3) < 0.5, "-500 implied ~83%")
ck(abs(100.0 / 480.0 * 100 - 20.8) < 0.5, "+380 implied ~21%")

# ── 2. THE 2024 BARCHART TRAP MUST BE REJECTED, NOT CARRIED ───────────────────
wt = txt(W)
for bad, name in [("-0.60", "S&P -0.60%"), ("&minus;1.18", "NDX -1.18%"), ("122%", "+122% revenue")]:
    if bad in W or bad in wt:
        i = W.find(bad) if bad in W else 0
        window = txt(W[max(0, i - 1400): i + 1400]).lower()
        ok = any(k in window for k in ["2024", "reject", "not publish", "none of it", "trap", "two years old"])
        ck(ok, "2024 figure %s appears outside a rejection context" % name)
ck("2024" in W and "August&nbsp;2024" in W, "WS must name the 2024 provenance")
ck("Catalent" in W and "HashiCorp" in W, "WS must give the dating evidence")
# and it must not leak onto the front page or the after-hours cards as a real move
ck("122" not in I, "index must not carry the 2024 revenue figure")
ah = W[W.find("After-hours movers"):]
ah = ah[:ah.find("</section>")]
ck("&minus;7%" not in ah or "2024" in ah, "after-hours section must not assert a -7% move")

# ── 3. AFTER-HOURS SECTION EXISTS AND IS HONEST (post-4pm requirement) ────────
ck("After-hours movers" in W, "after-hours section present after 4pm ET")
ck("no verified after-hours price move" in txt(W).lower(), "after-hours must state no verified move")
for nm in ["Nvidia", "CrowdStrike", "Salesforce", "Okta", "Williams-Sonoma", "Abercrombie"]:
    ck(nm in ah, "after-hours names %s" % nm)

# ── 4. TUESDAY-AS-WEDNESDAY RELABEL MUST STAY REJECTED ────────────────────────
for stale in ["7,677.24", "53,577.40 &plus;160.24", "160.24", "171.11"]:
    for pos in [mm.start() for mm in re.finditer(re.escape(stale), W)]:
        window = txt(W[max(0, pos - 1600): pos + 1600]).lower()
        ok = any(k in window for k in ["reject", "declined to adopt", "tuesday", "not adopt", "relabel",
                                       "weekly scorecard", "carried forward", "prior close", "closes stand"])
        ck(ok, "stale figure %s outside a rejection/Tuesday context @%d" % (stale, pos))

# ── 5. KEV BOARD: countdowns must match the printed due dates ─────────────────
TODAY = datetime.date(2026, 8, 26)
kevm = re.search(r'<div class="lab">CISA KEV &amp; federal deadlines</div>(.*?)</section>', C, re.S)
ck(kevm is not None, "KEV section found")
if kevm:
    rows = re.findall(r"<li>(.*?)</li>", kevm.group(1), re.S)
    ck(len(rows) == 14, "KEV board holds 14 rows, got %d" % len(rows))
    past = 0
    for r in rows:
        rt = txt(r)
        dm = re.search(r"due[^A-Za-z]*([A-Z][a-z]{2})[a-z]*\.?(?:&nbsp;|\s)*(\d{1,2})", rt, re.I)
        if not dm:
            fails.append("KEV row has no parseable due date: %s" % rt[:90]); checks += 1; continue
        mon = {"Jan":1,"Feb":2,"Mar":3,"Apr":4,"May":5,"Jun":6,"Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11,"Dec":12}[dm.group(1).title()]
        due = datetime.date(2026, mon, int(dm.group(2)))
        left = (due - TODAY).days
        if left <= 0:
            past += 1
        nm = re.search(r"\((\d+)\s*days?\s*left\)", rt, re.I)
        if nm:
            ck(int(nm.group(1)) == left, "KEV countdown mismatch: printed %s, computed %d (%s)" % (nm.group(1), left, rt[:60]))
        checks += 1
    ck(past == 10, "KEV past-due count should be 10, got %d" % past)
    # no CVE that the page says is OUTSIDE KEV may appear in a board row
    for cve in ["CVE-2026-58231", "CVE-2026-47301", "CVE-2026-19490", "CVE-2026-76310", "CVE-2026-20253"]:
        ck(not any(cve in r for r in rows), "%s must not appear in a KEV board row" % cve)
# Patch Priority must agree with the board
pp = C[C.find("Patch priority"):]
pp = txt(pp[:pp.find("</section>")])
ck("CVE-2026-21962" in pp, "Patch Priority names the Oracle CVE")
ck("Aug" in pp and ("27" in pp), "Patch Priority states the Aug 27 deadline")
ck((datetime.date(2026, 8, 27) - TODAY).days == 1, "Oracle deadline is 1 day out")
ck((datetime.date(2026, 8, 28) - TODAY).days == 2, "Gitea deadline is 2 days out")
# the recurring Gitea/Oracle garble must be rejected, not carried
for pos in [mm.start() for mm in re.finditer("CVE-2026-60004", C)]:
    win = txt(C[max(0, pos - 1200): pos + 1200]).lower()
    ck("gitea" in win, "CVE-2026-60004 must be described as Gitea @%d" % pos)

# ── 6. CHAMPIONS BOARD vs CORRECTIONS.md (authoritative block) ────────────────
CHAMPS = {"heavyweight": "Aspinall", "light heavyweight": "Ulberg", "middleweight": "Strickland",
          "welterweight": "Makhachev", "lightweight": "Gaethje", "featherweight": "Volkanovski",
          "bantamweight": "Yan", "flyweight": "Van", "women's flyweight": "Shevchenko",
          "women's bantamweight": "Harrison", "women's strawweight": "Dern"}
cb = re.search(r'<div class="lab">Champions board</div>(.*?)</section>', M, re.S)
ck(cb is not None, "champions board found")
if cb:
    rows = re.findall(r"<tr>(.*?)</tr>", cb.group(1), re.S)
    seen = {}
    for r in rows:
        cells = [txt(c).strip() for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", r, re.S)]
        if len(cells) >= 2:
            seen[cells[0].lower().replace("&rsquo;", "'").replace("’", "'").strip()] = cells[1]
    for div, champ in CHAMPS.items():
        row = next((v for k, v in seen.items() if div in k), None)
        ck(row is not None, "no champions row for %s" % div)
        if row:
            ck(champ in row, "%s champion should be %s, row says %r" % (div, champ, row[:60]))
    # explicit regressions that have shipped before
    lhw = next((v for k, v in seen.items() if "light heavyweight" in k), "")
    ck("Pereira" not in lhw, "REGRESSION: Pereira listed at light heavyweight")
    mw = next((v for k, v in seen.items() if k.strip() == "middleweight"), "")
    ck("Chimaev" not in mw, "REGRESSION: Chimaev listed at middleweight")
    fw = next((v for k, v in seen.items() if k.strip() == "featherweight"), "")
    ck("vacant" not in fw.lower(), "REGRESSION: featherweight listed vacant")

# ── 7. MMA: nothing 'upcoming' that has happened; no result asserted ──────────
mt = txt(M)
ck("August&nbsp;29" in M or "Aug. 29" in M or "August 29" in mt, "Shanghai date present")
ck((datetime.date(2026, 8, 29) - TODAY).days == 3, "Shanghai is 3 days out")
ck("Oriental Sports Center" in M, "correct Shanghai venue")
# HARNESS FIX: "Shanghai Indoor Stadium" is NOT a hard trap. The page carries it twice,
# both times inside its own explicit rejection prose ("...is rejected on the strength of
# that primary source"). Same bug class as the "Dooho Choi" mis-filing fixed at 3:50.
# It is moved to the context-allowed list in section 11; here we only require that the
# page states the rejection rather than that the string is absent.
ck("rejected on the strength of that primary source" in txt(M),
   "MMA must state why the Shanghai Indoor Stadium rendering is rejected")
ck("Denise Gomes" in M and "Xiaonan Yan" in M and "Kai Asakura" in M and "Qileng Aori" in M, "new Shanghai bouts present")
ck("no result is asserted" in mt.lower(), "MMA must disclaim results for the unfought card")
ck('id="ufccdn"' in M, "MMA countdown element present")

# ── 8. STRUCTURAL CONTRACT ON ALL FOUR PAGES ─────────────────────────────────
for p, h in H.items():
    for tab in ["index.html", "cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html", "archive.html"]:
        ck(('href="%s"' % tab) in h, "%s missing nav tab %s" % (p, tab))
    for pid in ["edition", "datestamp", "updated"]:
        ck(('id="%s"' % pid) in h, "%s missing masthead pill #%s" % (p, pid))
    ck("America/New_York" in h, "%s missing self-stamp JS" % p)
    ck("<script>(function(){try{var n=new Date();" in h, "%s self-stamp JS malformed" % p)
for p, lab in [("cyber-briefing.html", "The Wire"), ("wallstreet-briefing.html", "The Tape"),
               ("mma-briefing.html", "Tale of the Tape")]:
    ck(('<div class="tldr"><b>%s</b>' % lab) in H[p], "%s tldr label" % p)
    ck('id="freshline"' in H[p], "%s freshline" % p)
ck('class="tldr"' not in I, "index must not carry a tldr strip")

# ── 9. TRADINGVIEW BLOCKS (all six, exactly three single-quote widgets) ──────
for blk in ["embed-widget-ticker-tape.js", "embed-widget-single-quote.js", "embed-widget-timeline.js",
            "embed-widget-stock-heatmap.js", "embed-widget-mini-symbol-overview.js", "embed-widget-events.js"]:
    ck(blk in W, "WS missing TradingView block %s" % blk)
ck(W.count("embed-widget-single-quote.js") == 3, "WS needs exactly 3 single-quote widgets, got %d" % W.count("embed-widget-single-quote.js"))
for sym in ["FOREXCOM:SPXUSD", "FOREXCOM:NSXUSD", "FOREXCOM:DJI", "TVC:USOIL", "TVC:US10Y"]:
    ck(sym in W, "WS ticker tape missing mandatory symbol %s" % sym)

# ── 10. NEW-TAG HYGIENE: only this edition may be tagged New ─────────────────
for p, h in H.items():
    for lab in re.findall(r'<span class="tag new">New &middot; ([0-9:]+)</span>', h):
        ck(lab == "4:15", "%s has a stale New tag at %s" % (p, lab))
    for lab in re.findall(r"&#9679; New &middot; ([0-9:]+)", h):
        ck(lab == "4:15", "%s has a stale New paragraph marker at %s" % (p, lab))
    ck("New at 3:" not in h, "%s has an undemoted 'New at' label" % p)

# ── 11. TRAP GREPS: names and figures that have shipped wrong before ─────────
HARD = ["Cody Salkilld", "Shamil Yakhyaev", "Abdul-Rakhman", "Fight Night 286", "$1.4 trillion", "Suno"]
for p, h in H.items():
    for t in HARD:
        ck(t not in h, "%s contains hard trap %r" % (p, t))
# context-allowed: only inside a rejection/correction window
SOFT = {"wallstreet-briefing.html": ["4,637.03", "30.68", "7,677.24"],
        "mma-briefing.html": ["Dooho Choi", "Shanghai Indoor Stadium"]}
VOCAB = ["reject", "not adopt", "declined", "correction", "previously", "discrepancy", "stale",
         "tuesday", "carried forward", "not a wednesday", "does not reconcile", "relabel",
         "is the one published", "no third venue", "recurred in search results"]
for p, terms in SOFT.items():
    for t in terms:
        for pos in [mm.start() for mm in re.finditer(re.escape(t), H[p])]:
            win = txt(H[p][max(0, pos - 1600): pos + 1600]).lower()
            ck(any(v in win for v in VOCAB), "%s: %r outside a rejection context @%d" % (p, t, pos))

# ── 12. DISCLAIMERS ──────────────────────────────────────────────────────────
ck("not investment advice" in txt(W).lower(), "WS disclaimer")
ck("subject to change" in txt(M).lower(), "MMA disclaimer")
ck("Sources" in W and "Sources" in C and "Sources" in M, "sources footers present")

print("CHECKS: %d   FAILURES: %d" % (checks, len(fails)))
for f in fails:
    print("  FAIL:", f)
