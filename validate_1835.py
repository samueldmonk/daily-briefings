#!/usr/bin/env python3
import io, os, re, json, sys, datetime
from html.parser import HTMLParser

OUT = "/sessions/epic-cool-pasteur/mnt/outputs"
PAGES = ["index.html", "cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html", "archive.html"]
VOID = {"area","base","br","col","embed","hr","img","input","link","meta","param","source","track","wbr"}
fails, notes = [], []

def ck(cond, msg):
    (notes if cond else fails).append(("OK  " if cond else "FAIL ") + msg)

class Bal(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True); self.stack=[]; self.errs=[]
    def handle_starttag(self, t, a):
        if t not in VOID: self.stack.append(t)
    def handle_endtag(self, t):
        if t in VOID: return
        if self.stack and self.stack[-1]==t: self.stack.pop()
        elif t in self.stack:
            while self.stack and self.stack.pop()!=t: pass
        else: self.errs.append("stray </%s>"%t)

src = {}
for p in PAGES:
    fp = os.path.join(OUT, p)
    if not os.path.exists(fp):
        fails.append("FAIL missing page %s" % p); continue
    src[p] = io.open(fp, encoding="utf-8").read()

# 1. balance
for p, s in src.items():
    b = Bal(); b.feed(s)
    ck(not b.stack and not b.errs, "%s balanced (unclosed=%d errs=%d)" % (p, len(b.stack), len(b.errs)))

# 2. nav + stamp ids
for p, s in src.items():
    nav = re.search(r"<nav class=\"tabs\">(.*?)</nav>", s, re.S)
    ck(bool(nav), "%s has <nav class=tabs>" % p)
    if nav:
        links = re.findall(r'href="([^"]+)"', nav.group(1))
        ck(links == ["index.html","cyber-briefing.html","wallstreet-briefing.html","mma-briefing.html","archive.html"],
           "%s nav = 5 tabs in order (%s)" % (p, links))
        ck(nav.group(1).count("border-color:") == 1, "%s exactly 1 active tab" % p)
    for i in ("datestamp","updated","edition"):
        ck(('id="%s"'%i) in s, "%s has id=%s" % (p, i))
    if p != "archive.html":
        ck('id="freshline"' in s, "%s has freshline" % p)

# 3. tldr labels
for p, lab in [("cyber-briefing.html","The Wire"),("wallstreet-briefing.html","The Tape"),("mma-briefing.html","Tale of the Tape")]:
    s = src[p]
    ck(s.count('class="tldr"') == 1, "%s exactly 1 .tldr" % p)
    ck("<b>%s</b>" % lab in s, "%s tldr label = %s" % (p, lab))
ck('class="tldr"' not in src["index.html"], "index has no .tldr (by design)")

# 4. TradingView widget JSON
w = src["wallstreet-briefing.html"]
blocks = re.findall(r'embed-widget-[a-z\-]+\.js"\s+async>\s*(\{.*?\})\s*</script>', w, re.S)
ck(len(blocks) == 8, "wallstreet has 8 widget blocks (found %d)" % len(blocks))
good = 0
for b in blocks:
    try: json.loads(b); good += 1
    except Exception as e: fails.append("FAIL widget JSON: %s" % e)
ck(good == len(blocks), "%d/%d widget JSON blocks parse" % (good, len(blocks)))
for sym in ["FOREXCOM:SPXUSD","FOREXCOM:NSXUSD","FOREXCOM:DJI","TVC:USOIL","TVC:US10Y"]:
    ck(sym in w, "ticker retains %s" % sym)
ck('"symbol":"NASDAQ:HOOD"' in w, "Chart of the Day = NASDAQ:HOOD")

# 5. KEV countdowns
TODAY = datetime.date(2026, 8, 22)
c = src["cyber-briefing.html"]
kev = re.findall(r'due <b>(\d{4}-\d{2}-\d{2})</b> <span class="(kev-[a-z]+)">\(([^)]+)\)</span>', c)
ck(len(kev) == 8, "KEV rows with explicit due dates = 8 (found %d)" % len(kev))
for d, cls, label in kev:
    due = datetime.date(*map(int, d.split("-")))
    delta = (due - TODAY).days
    if delta < 0:
        exp_lbl, exp_cls = "%d day%s PAST DUE" % (-delta, "" if -delta == 1 else "s"), "kev-crit"
    elif delta == 0:
        exp_lbl, exp_cls = "due today", "kev-crit"
    else:
        exp_lbl = "%d day%s left" % (delta, "" if delta == 1 else "s")
        exp_cls = "kev-soon" if delta <= 3 else "kev-ok"
    ck(label.strip() == exp_lbl, "KEV %s label '%s' == '%s'" % (d, label, exp_lbl))
    ck(cls == exp_cls, "KEV %s class %s == %s" % (d, cls, exp_cls))

rows = c.count("<li><b>CVE-")
ck(rows == 11, "KEV list has 11 rows (found %d)" % rows)
pastdue = c.count("PAST DUE") + c.count("window elapsed")
ck(pastdue == 8, "8 past-due markers (found %d)" % pastdue)
for t in ["Of the 11 entries tracked here, <b>8 are past due</b>",
          '<div class="n">8</div><div class="l">KEV entries past due</div>',
          "8 KEV entries sit past their federal due date"]:
    ck(t in c, "count consistency: %s" % t[:48])

# Patch Priority <-> KEV agreement
ck("CVE-2026-59310" in c and "CVE-2026-72529" in c and "CVE-2025-62593" in c, "Patch Priority CVEs present")
ck(c.count("CVE-2025-62593") >= 3, "Ray CVE appears in priority box, table and KEV list")
ck("due <b>2026-08-20</b>" in c, "Ray KEV due date 2026-08-20 present")

# 6. Entra ID must never be called exploited
ck("<b>Not exploited.</b>" in c, "Entra ID labelled Not exploited")
for bad in ["Entra ID zero-day", "Entra ID flaw exploited"]:
    ck(bad not in c, "no regression: '%s' absent" % bad)

# 7. Scorecard arithmetic
sc = re.findall(r'<td><b>([^<]+)</b></td><td>([\d,]+\.\d\d)</td><td[^>]*>([+\-][\d,]+\.\d\d)</td><td[^>]*>([+\-][\d.]+)%</td>', w)
if sc:
    for name, lvl, chg, pct in sc:
        L = float(lvl.replace(",","")); C = float(chg.replace(",","")); P = float(pct)
        prior = L - C
        calc = C / prior * 100
        ck(abs(calc - P) < 0.06, "%s arithmetic %.2f%% vs printed %s%%" % (name, calc, pct))
else:
    notes.append("OK  scorecard rows not in the strict 4-col pattern; skipped arithmetic")
for lvl in ["7,674.37", "26,180.45", "53,277.01"]:
    ck(lvl in w, "scorecard level %s present" % lvl)
ck("4.737" in w and "5.276" in w, "yields 4.737% / 5.276% published")

# 8. Champions board
m = src["mma-briefing.html"]
champs = {"Tom Aspinall":"HW","Carlos Ulberg":"LHW","Sean Strickland":"MW","Islam Makhachev":"WW",
          "Justin Gaethje":"LW","Alexander Volkanovski":"FW","Petr Yan":"BW","Joshua Van":"FLW",
          "Valentina Shevchenko":"WFLW","Kayla Harrison":"WBW","Mackenzie Dern":"WSW"}
for n in champs:
    ck(n in m, "champion present: %s" % n)
ck(">Vacant<" not in m, "no Vacant belt")
for bad in ["Cody Salkilld","Shamil Yakhyaev","Abdul-Rakhman","MacKenzie","Joshua Vance",
            "Pereira (205)","pay-per-view","former champion","title challenger"]:
    ck(bad not in m, "trap grep clean: %s" % bad)
for stale in ["Khamzat Chimaev</td>","Alexandre Pantoja</td>","Merab Dvalishvili</td>","Ilia Topuria</td>"]:
    ck(stale not in m, "no stale champion cell: %s" % stale)

# 9. MMA results discipline
ck("Jackson McVey" in m and "4:13" in m, "McVey result published with time")
ck("Shanelle Dyer" in m and "1:42" in m, "Dyer result published with time")
for uncorroborated in ["Douglas def", "Gaziev def", "Haqparast def", "Young def", "Hernandez def", "Spivac def", "de Ridder def"]:
    ck(uncorroborated not in m, "uncorroborated result absent: %s" % uncorroborated)
ck("Only these two bouts are published" in m, "MMA states the publication limit")

# 10. After-hours must be absent (weekend)
ah = w.split('lab">After-Hours Movers')[-1].split("</section>")[0] if 'lab">After-Hours Movers' in w else ""
ck(ah.count('class="card"') == 0, "After-Hours block has 0 mover cards (weekend placeholder only)")
ck("No after-hours section this edition" in w, "After-Hours omission is explained on the page")

# 11. index cards
i = src["index.html"]
for t in ["The Cyber Wire", "The Closing Bell", "The Octagon"]:
    ck(t in i, "index card: %s" % t)
ck(i.count('class="rd"') == 3, "index has 3 'Read the briefing' links")
ck("Eight federal patch deadlines" in i, "index cyber headline updated")
ck("Shanelle Dyer" in i and "Jackson McVey" in i, "index mma card names the two results")

print("\n".join(notes))
print("")
if fails:
    print("=== %d FAILURES ===" % len(fails))
    print("\n".join(fails)); sys.exit(1)
print("=== ALL %d CHECKS PASSED ===" % len(notes))
