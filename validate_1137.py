#!/usr/bin/env python3
"""Validation gate for the 2026-08-24 ~11:40am ET Midday Edition."""
import re, sys, json, os
from html.parser import HTMLParser

D = os.path.dirname(os.path.abspath(__file__))
PAGES = ["index.html", "cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"]
src = {p: open(os.path.join(D, p), encoding="utf-8").read() for p in PAGES}
fails, checks = [], 0

def ck(cond, msg):
    global checks
    checks += 1
    if not cond:
        fails.append(msg)

VOID = {"br","hr","img","meta","link","input","source","col","area","base","embed","param","track","wbr"}
class Bal(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True); self.stack=[]; self.stray=0
    def handle_starttag(self,t,a):
        if t not in VOID: self.stack.append(t)
    def handle_endtag(self,t):
        if t in VOID: return
        if self.stack and self.stack[-1]==t: self.stack.pop()
        elif t in self.stack:
            while self.stack and self.stack.pop()!=t: pass
        else: self.stray+=1

for p in PAGES:
    b=Bal(); b.feed(src[p])
    ck(not b.stack, f"{p}: unclosed tags {b.stack[:6]}")
    ck(b.stray==0, f"{p}: {b.stray} stray end tags")

# --- nav: five tabs, exactly one active ---
for p in PAGES:
    for href in ["index.html","cyber-briefing.html","wallstreet-briefing.html","mma-briefing.html","archive.html"]:
        ck(href in src[p], f"{p}: nav missing {href}")
    ck(len(re.findall(r'<a href="[^"]+" class="on">', src[p]))==1, f"{p}: active tab count != 1")

# --- stamp ids ---
for p in PAGES:
    for i in ["datestamp","updated","edition"]:
        ck(f'id="{i}"' in src[p], f"{p}: missing id {i}")
    ck("America/New_York" in src[p], f"{p}: missing ET stamp script")
for p in ["cyber-briefing.html","wallstreet-briefing.html","mma-briefing.html"]:
    ck('id="freshline"' in src[p], f"{p}: missing freshline")

# --- tldr labels ---
LAB = {"wallstreet-briefing.html":"The Tape","cyber-briefing.html":"The Wire","mma-briefing.html":"Tale of the Tape"}
for p,l in LAB.items():
    ck(src[p].count('class="tldr"')==1, f"{p}: tldr count != 1")
    ck(f"<b>{l}</b>" in src[p], f"{p}: tldr label wrong (want {l})")
ck('class="tldr"' not in src["index.html"], "index.html must not have a .tldr")

# --- index cards carry each page's tldr sentence verbatim ---
for p in LAB:
    m = re.search(r'<div class="tldr"><b>[^<]+</b>\s*<span>(.*?)</span></div>', src[p], re.S)
    ck(m is not None, f"{p}: tldr span not parseable")
    if m:
        ck(m.group(1).strip() in src["index.html"], f"index.html missing verbatim tldr for {p}")

# --- TradingView widget JSON parses ---
blocks = re.findall(r'embed-widget-[a-z\-]+\.js"\s+async>\s*(\{.*?\})\s*</script>', src["wallstreet-briefing.html"], re.S)
ck(len(blocks)==8, f"wallstreet: expected 8 widget blocks, found {len(blocks)}")
for i,b in enumerate(blocks):
    try: json.loads(b)
    except Exception as e: fails.append(f"wallstreet: widget block {i} bad JSON: {e}")
    checks += 1
for sym in ["FOREXCOM:SPXUSD","FOREXCOM:NSXUSD","FOREXCOM:DJI","TVC:USOIL","TVC:US10Y"]:
    ck(sym in src["wallstreet-briefing.html"], f"wallstreet: ticker missing {sym}")
ck('"symbol":"NASDAQ:AAOI"' in src["wallstreet-briefing.html"], "wallstreet: Chart of the Day != NASDAQ:AAOI")

# --- STALE-FIGURE BLACKLIST (prior editions' bars must be gone from live editorial) ---
BLACK = ["7,645.21","53,391.49","25,935.17","7,652.36","53,441.18","25,971.85","5.248%","4.72% on Monday, down two"]
for b in BLACK:
    ck(b not in src["wallstreet-briefing.html"] or b in ("5.248%",),
       f"wallstreet: stale figure present: {b}")
# 5.248% may survive only as an explicitly-earlier attribution
if "5.248%" in src["wallstreet-briefing.html"]:
    ck("Earlier Monday" in src["wallstreet-briefing.html"], "wallstreet: 5.248% not framed as earlier Monday")

# --- FRIDAY-CLOSE TRAP: Friday closes must not be presented as Monday's close ---
ws = src["wallstreet-briefing.html"]
for lvl in ["7,674.37","53,277.01","26,180.46"]:
    ck(lvl in ws, f"wallstreet: Friday close {lvl} missing from scorecard")
ck("Monday" not in re.sub(r"\s+"," ",ws)[max(0,ws.find("7,674.37")-160):ws.find("7,674.37")]
   or "Friday" in ws, "wallstreet: Friday close context check")

# --- current bar: percentages only, and they must be the fresh ones ---
for frag in ["0.48%","0.25%","0.32%","4.7%","5.23%"]:
    ck(frag in ws, f"wallstreet: fresh figure missing: {frag}")

# --- KEV countdowns ---
cy = src["cyber-briefing.html"]
kev = re.findall(r'due <b>([A-Z][a-z]{2} \d{1,2})</b>\.\s*<span[^>]*>([^<]+)</span>', cy)
ck(len(kev)==12, f"cyber: expected 12 KEV countdown rows, found {len(kev)}")
past = sum(1 for _,l in kev if "past due" in l.lower() or "overdue" in l.lower())
today = sum(1 for _,l in kev if "today" in l.lower())
ck(past==8, f"cyber: expected 8 past-due, got {past}")
ck(today==1, f"cyber: expected 1 due-today, got {today}")
ck(len(kev)-past-today==3, "cyber: expected 3 KEV rows still ahead")
ck("CVE-2026-73570" in cy and "8.9" in cy, "cyber: Zimbra CVE/CVSS missing")
ck("10.1.20" in cy, "cyber: Zimbra fixed version missing")

# --- new-tag budget: WS 1, CYBER 1, MMA 0 ---
counts = {p: src[p].count('tag new">New') for p in PAGES}
ck(counts["wallstreet-briefing.html"]==1, f"wallstreet New tags = {counts['wallstreet-briefing.html']} (want 1)")
ck(counts["cyber-briefing.html"]==1, f"cyber New tags = {counts['cyber-briefing.html']} (want 1)")
ck(counts["mma-briefing.html"]==0, f"mma New tags = {counts['mma-briefing.html']} (want 0)")
ck(counts["index.html"]==0, "index should carry no New tags")
# the dropped tags must really be dropped
ck("UT San Antonio starts its fall semester today, three days late, after a cyberattack</h3>" in cy, "cyber: UTSA card missing")
ck('Disruption</span><span class="tag new">New' not in cy, "cyber: UTSA New tag not dropped")
ck('Joint advisory</span><span class="tag new">New' not in cy, "cyber: Medusa New tag not dropped")
ck('Dow breadth</span><span class="tag new">New' not in ws, "wallstreet: Dow-breadth New tag not dropped")
ck('$1T TGA</span><span class="tag new">New' in ws, "wallstreet: TGA card missing its New tag")

# --- champions board: 11 rows, none vacant, key names per CORRECTIONS.md ---
mm = src["mma-briefing.html"]
champ = mm[mm.find("Champions board"):]
champ = champ[:champ.find("</section>")]
rows = re.findall(r"<tr>", champ)
ck(len(rows)==12, f"mma: champions table rows (1 header + 11) = {len(rows)}")
ck(not re.search(r"<td>\s*[Vv]acant\s*</td>", champ), "mma: champions board has a VACANT cell")
ck("none vacant" in champ.lower(), "mma: champions note should assert none vacant")
for div, name in [("Heavyweight","Tom Aspinall"),("Light Heavyweight","Carlos Ulberg"),
                  ("Middleweight","Sean Strickland"),("Welterweight","Islam Makhachev"),
                  ("Lightweight","Justin Gaethje"),("Featherweight","Alexander Volkanovski"),
                  ("Bantamweight","Petr Yan"),("Flyweight","Joshua Van")]:
    ck(name in champ, f"mma: champions board missing {div} champ {name}")
for bad in ["Alex Pereira</td>","Khamzat Chimaev</td>","Ilia Topuria</td>"]:
    ck(bad not in champ, f"mma: REGRESSION — stale champion cell {bad}")

# --- trap greps across all pages ---
TRAPS = ["Cody Salkilld","Abdul-Rakhman","Shamil Yakhyaev","former champion Beneil","title challenger Beneil"]
for p in PAGES:
    for t in TRAPS:
        ck(t not in src[p], f"{p}: trap phrase present: {t}")

# --- MMA countdown target ---
ck("2026-08-29T06:00:00-04:00" in mm, "mma: countdown target missing")
ck('id="ufccdn"' in mm, "mma: #ufccdn missing")

# --- sources footers ---
for p in ["cyber-briefing.html","wallstreet-briefing.html","mma-briefing.html"]:
    ck("Sources" in src[p] and "http" in src[p], f"{p}: sources footer missing")
ck("cnbc.com/2026/08/24/bessent-1-trillion-treasury-general-account-bond-buybacks" in ws,
   "wallstreet: CNBC TGA source URL missing")
ck("resecurity.com/blog/article/from-wsproxy-to-root" in cy, "cyber: Resecurity source URL missing")

print(f"checks run: {checks}")
if fails:
    print(f"FAILURES: {len(fails)}")
    for f in fails: print("  -", f)
    sys.exit(1)
print("ALL CHECKS PASSED")
