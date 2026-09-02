# -*- coding: utf-8 -*-
"""Guards for the Sept 2 2026 Afternoon Edition (post-close, 14th run)."""
import io, os, re, sys

OUT = os.path.dirname(os.path.abspath(__file__))
P = {}
for n in ("index.html", "cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"):
    P[n] = io.open(os.path.join(OUT, n), encoding="utf-8").read()
ALL = "".join(P.values())

fails, checks = [], [0]

def ck(cond, msg):
    checks[0] += 1
    if not cond:
        fails.append(msg)

def ran(pat, text, msg):
    """Assert a guard's pattern actually matches something (anti-over-reach)."""
    checks[0] += 1
    if not re.search(pat, text, re.S):
        fails.append("GUARD-INERT: " + msg)

CY, WS, MM, IX = P["cyber-briefing.html"], P["wallstreet-briefing.html"], P["mma-briefing.html"], P["index.html"]

# ---- 1. Champions board -------------------------------------------------
ran(r"<td><b>Middleweight</b></td><td>([^<]+)</td>", MM, "middleweight row present")
mw = re.search(r"<td><b>Middleweight</b></td><td>([^<]+)</td>", MM).group(1)
ck("Strickland" in mw, "MIDDLEWEIGHT champion cell is not Strickland: %r" % mw)
ck("Chimaev" not in mw, "MIDDLEWEIGHT champion cell names Chimaev")

ran(r"<td><b>Featherweight</b></td><td>([^<]+)</td>", MM, "men's featherweight row present")
fw = re.search(r"<td><b>Featherweight</b></td><td>([^<]+)</td>", MM).group(1)
ck("Volkanovski" in fw, "FEATHERWEIGHT champion cell is not Volkanovski: %r" % fw)
ck("Vacant" not in fw, "men's FEATHERWEIGHT listed vacant")

ran(r"Women’s Featherweight</b></td><td>([^<]+)</td>", MM, "women's featherweight row present")
wfw = re.search(r"Women’s Featherweight</b></td><td>([^<]+)</td>", MM).group(1)
ck("Vacant" in wfw, "women's FEATHERWEIGHT must be Vacant, got %r" % wfw)

for div, champ in (("Light Heavyweight", "Carlos Ulberg"), ("Lightweight", "Justin Gaethje"),
                   ("Welterweight", "Islam Makhachev"), ("Bantamweight", "Petr Yan"),
                   ("Flyweight", "Joshua Van"), ("Heavyweight", "Tom Aspinall")):
    ck(("<td><b>%s</b></td><td>%s</td>" % (div, champ)) in MM, "champions row wrong/missing: %s = %s" % (div, champ))
ck("Pereira" not in MM, "Pereira appears on the MMA page (was wrongly listed as LHW champ historically)")

# ---- 2. Standing corrections --------------------------------------------
ck(not re.search(r"Parnasse[^.]{0,200}Contender Series", MM, re.S),
   "Parnasse attributed to the Contender Series")
ck(not re.search(r"Contender Series[^.]{0,200}Parnasse", MM, re.S),
   "Contender Series linked to Parnasse")
ran(r"did <b>not</b> come through Dana White’s Contender Series", MM, "Parnasse KSW provenance clause present")
ck("KSW" in MM, "Parnasse's KSW provenance is missing")
ck("Nevada" not in ALL, "Nevada statewide ransomware (Aug 2025) resurfaced")
ck("Dariush" not in ALL, "Dariush mentioned; if reinstated he must be a CONTENDER, never a challenger")
# forbidden Aug-dated bond figures wrongly attached to Sept 2
for bad in ("4.639", "5.185"):
    ck(bad not in WS, "August-dated Treasury figure published as Sept 2: %s" % bad)
ran(r"were <b>refused</b> and the rates table below carries only the September 2 readings", WS,
    "the August-figures refusal note is present")
ck("4.79%" in WS, "verified Sept 2 10-year level (4.79%) missing")

# ---- 3. Index reconciliation --------------------------------------------
ck(abs((7631.47 + 35.13) - 7666.60) < 0.005, "S&P reconciliation fails")
ck(abs((26099.77 + 118.06) - 26217.83) < 0.005, "Nasdaq reconciliation fails")
ck(abs((52766.88 + 295.07) - 53061.95) < 0.005, "Dow reconciliation fails")
for lvl in ("7,666.60", "26,217.83", "53,061.95", "+295.07", "+0.46%", "+0.45%", "+0.56%"):
    ck(lvl in WS, "scorecard figure missing: %s" % lvl)

# ---- 4. KEV deadline consistency ----------------------------------------
ck("September 14" in CY and "12 days left" in CY, "PaperCut KEV date/countdown missing")
ck("September 16, 2026" in CY and "14 days left" in CY, "LiteLLM KEV date/countdown missing")
ran(r"shortest verified CISA deadline</b> below belongs to the two <b>PaperCut", CY,
    "patch-priority points at the PaperCut clock")
ck(CY.count("September 14") >= 2, "Patch Priority and KEV section must both carry Sept 14")
ck("due September 14 &mdash; 12 days from today" in CY or "due September 14 — 12 days from today" in CY,
   "Patch Priority does not state the same verified deadline")
# no invented KEV listing for JFrog
ck("places CVE-2026-82329 in the CISA KEV catalog" in CY, "JFrog KEV disclaimer missing")
ck(not re.search(r"CVE-2026-82329[^<]{0,80}KEV[^<]{0,40}due", CY), "JFrog given a federal deadline")

# ---- 5. Cyber accuracy --------------------------------------------------
ck("maximum-severity" not in CY, "'maximum-severity' asserted")
ck("⚘" not in ALL and "&#9880;" not in ALL, "U+2698 flower used instead of U+26E8 shield")
ck("&#9960;" in CY and "&#9960;" in IX, "shield glyph (U+26E8 / &#9960;) missing from cyber masthead or index kicker")
ran(r"&#9960; The Cyber Wire", CY, "cyber masthead shield present")
ck("9,540,683" in CY, "Aesto figure missing")
ck("CVE-2026-83548" in CY and "CVE-2026-83549" in CY, "SonicWall CVEs missing")
ck("The Gentlemen" in CY, "Nutex claimant missing")
ck("No record count is asserted" in CY, "Nutex record-count guard missing")
ck("1.11.6" in CY and "1.84.0" in CY, "fixed versions missing")

# ---- 6. Wall Street widgets ---------------------------------------------
for blk, name in (("embed-widget-ticker-tape.js", "A ticker tape"),
                  ("embed-widget-single-quote.js", "B single quotes"),
                  ("embed-widget-timeline.js", "C timeline"),
                  ("embed-widget-stock-heatmap.js", "D heatmap"),
                  ("embed-widget-mini-symbol-overview.js", "E chart of the day"),
                  ("embed-widget-events.js", "F economic calendar")):
    ck(blk in WS, "missing live block %s" % name)
ck(WS.count("embed-widget-single-quote.js") == 3, "need exactly 3 single-quote widgets")
for sym in ("FOREXCOM:SPXUSD", "FOREXCOM:NSXUSD", "FOREXCOM:DJI", "TVC:USOIL", "TVC:US10Y"):
    ck(sym in WS, "ticker tape must keep %s" % sym)
ck('"symbol":"NYSE:DELL"' in WS, "Chart of the Day should be the session's biggest mover, Dell")
ck("livebar" in WS, "livebar wrapper missing")
ck("After-Hours Movers" in WS, "post-4pm run must carry an After-Hours block")
ck("Quotes stream live" in WS, "single-quote note line missing")

# ---- 7. Chrome on every page --------------------------------------------
for n, html in P.items():
    for tab in ("index.html", "cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html", "archive.html"):
        ck('href="%s"' % tab in html, "%s missing nav tab %s" % (n, tab))
    for pid in ('id="edition"', 'id="datestamp"', 'id="updated"', 'id="freshline"'):
        ck(pid in html, "%s missing %s" % (n, pid))
    ck("America/New_York" in html, "%s missing stamp JS" % n)
    ck("<span class=\"pill live\">" in html, "%s missing LIVE pill" % n)
ck('class="active"' in IX and IX.count('class="active"') == 1, "index active tab")
ck(re.search(r'<a href="cyber-briefing.html" class="active">', CY) is not None, "cyber active tab")
ck(re.search(r'<a href="wallstreet-briefing.html" class="active">', WS) is not None, "ws active tab")
ck(re.search(r'<a href="mma-briefing.html" class="active">', MM) is not None, "mma active tab")

# ---- 8. Summary strips --------------------------------------------------
ck('<b>The Wire</b>' in CY, "cyber tldr label")
ck('<b>The Tape</b>' in WS, "ws tldr label")
ck('<b>Tale of the Tape</b>' in MM, "mma tldr label")
ck('class="tldr"' not in IX, "index must show summaries as cards, not a tldr strip")
for lbl in ("The Wire", "The Tape", "Tale of the Tape"):
    ck(lbl in IX, "index missing kicker/heading %s" % lbl)

# summaries must match between index cards and their pages
def strip(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s)).strip()
for html, label in ((CY, "cyber"), (WS, "ws"), (MM, "mma")):
    body = strip(re.search(r'<div class="tldr">.*?</div>', html, re.S).group(0))
    core = body.split("</b>")[-1] if "</b>" in body else body
    ck(strip(core)[-60:] in strip(IX), "index card summary drifted from the %s page" % label)

# ---- 9. MMA specifics ---------------------------------------------------
ck('id="ufccdn"' in MM and "2026-09-05T00:00:00-04:00" in MM, "MMA countdown missing/wrong target")
ck("Fight week" in MM, "countdown elapsed text missing")
ck("Song Yadong</td><td>def. Umar Nurmagomedov</td><td>KO (right uppercut), R2 1:48" in MM,
   "main-event result line wrong")
ck("Natália Silva" in MM, "Silva name spelling")
ck("Accor Arena" in MM, "Paris venue missing")
ck("Delta Center" in MM and "October 3, 2026" in MM, "UFC 332 venue/date missing")
ck("No total count is asserted" in MM, "bonus-count guard missing")
ck("No viewership, gate or TKO Group figures are printed" in MM, "business-figures guard missing")
# nothing 'upcoming' that already happened
ck("August 29, 2026" in MM and "Last Event" in MM, "last event framing")
_cards = re.search(r'Fight Week &mdash; Upcoming Cards</h2>(.*?)<h2 class="sec">Last Event', MM, re.S) \
    or re.search(r'Fight Week — Upcoming Cards</h2>(.*?)<h2 class="sec">Last Event', MM, re.S)
ran(r'Fight Week — Upcoming Cards</h2>(.*?)<h2 class="sec">Last Event', MM, "upcoming-cards block isolated")
_c = _cards.group(1)
# only the .when date lines are event dates; body prose may legitimately cite past months
_whens = re.findall(r'<div class="when">(.*?)</div>', _c)
ck(len(_whens) == 6, "expected 6 upcoming-card date lines, got %d" % len(_whens))
for _wn in _whens:
    for past in ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"):
        ck(past not in _wn, "a past month appears in an Upcoming Cards date line: %r" % _wn)
for d in ("Sept 5", "Sept 12", "Sept 19", "Sept 26", "Oct 3", "Oct 24"):
    ck(d in _c, "Upcoming Cards missing %s" % d)

# ---- 10. Odds only where sourced ----------------------------------------
ck("Parnasse −600 / Hooker +440 (DraftKings)" in MM, "sourced odds line missing")
ck(MM.count("Odds:") == 1, "odds printed for an unsourced headliner")

# ---- 11. Structure ------------------------------------------------------
for n, html in P.items():
    ck(html.startswith("<!DOCTYPE html>"), "%s doctype" % n)
    ck(html.rstrip().endswith("</body></html>"), "%s close tags" % n)
    ck(html.count("<footer>") == 1, "%s footer count" % n)
for n in ("cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"):
    ck("<h5>Sources</h5>" in P[n], "%s sources footer missing" % n)
    ck('class="disc"' in P[n], "%s disclaimer missing" % n)
    ck(P[n].count("https://") >= 10, "%s has too few real source URLs" % n)
ck("For information only" in WS and "is investment advice" in WS, "WS disclaimer wording")
ck("subject to change" in MM, "MMA disclaimer wording")

# ---- 12. Read-through defects from this run, now guarded ----------------
import datetime
TODAY = datetime.date(2026, 9, 2)

# (a) weekday words must match the real weekday of the date they describe
for text, label in ((MM, "mma"), (IX, "index")):
    for m in re.finditer(r"(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)[’']s Paris headliner", text):
        ck(m.group(1) == "Saturday",
           "%s: Paris headliner is Sept 5 2026, a Saturday, not %s" % (label, m.group(1)))
ran(r"Saturday[’']s Paris headliner", MM, "Paris weekday phrase present on the MMA page")
ck(datetime.date(2026, 9, 5).strftime("%A") == "Saturday", "sanity: Sept 5 2026 is a Saturday")
for wd, d in (("Saturday, September 5", datetime.date(2026, 9, 5)),
              ("Saturday, August 29, 2026", datetime.date(2026, 8, 29))):
    ck(wd not in MM or d.strftime("%A") == wd.split(",")[0], "weekday/date mismatch: %s" % wd)
for wd, d in (("Thursday, Sept 3", datetime.date(2026, 9, 3)), ("Friday, Sept 4", datetime.date(2026, 9, 4)),
              ("Wednesday, Sept 16", datetime.date(2026, 9, 16)),
              ("Wednesday, September 2, 2026", TODAY)):
    ck(wd in WS and d.strftime("%A") == wd.split(",")[0], "WS calendar weekday/date mismatch: %s" % wd)

# (a2) every "Weekday, Month D, YYYY" string on any page must be calendrically true
_MON = {m: i + 1 for i, m in enumerate(
    ["January", "February", "March", "April", "May", "June", "July",
     "August", "September", "October", "November", "December"])}
_seen = 0
for n, html_ in P.items():
    txt = re.sub(r"<[^>]+>", " ", html_)
    for m in re.finditer(r"(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday),\s+"
                         r"(January|February|March|April|May|June|July|August|September|October|November|December)\s+"
                         r"(\d{1,2}),?\s+(\d{4})", txt):
        _seen += 1
        wd, mon, day, yr = m.group(1), m.group(2), int(m.group(3)), int(m.group(4))
        real = datetime.date(yr, _MON[mon], day).strftime("%A")
        ck(real == wd, "%s: '%s, %s %d, %d' is actually a %s" % (n, wd, mon, day, yr, real))
ck(_seen >= 2, "GUARD-INERT: weekday/date scanner matched nothing")
ck("Sunday, May 10" not in MM and "Saturday, May 10" not in MM,
   "a weekday is attached to the disputed UFC 328 date")

# (b) elapsed-days arithmetic in prose must be right
ran(r"exploited now, (\w+) days after the fix", CY, "JFrog elapsed-days clause present")
_n = re.search(r"exploited now, (\w+) days after the fix", CY).group(1)
ck(_n == "five", "JFrog patched Aug 28, today Sept 2 = five days, page says %r" % _n)
ck((TODAY - datetime.date(2026, 8, 28)).days == 5, "sanity: Aug 28 -> Sept 2 is 5 days")
ck((datetime.date(2026, 9, 14) - TODAY).days == 12, "sanity: PaperCut 12-day countdown")
ck((datetime.date(2026, 9, 16) - TODAY).days == 14, "sanity: LiteLLM 14-day countdown")

# (c) don't claim a finish count the results table doesn't support
ck("Ten fights ended inside the distance" not in MM, "unsupported finish count restored")
ck("not asserted to be the complete card" in MM, "results-completeness caveat missing")

# (d) one fighter, one spelling: Ce Liu appears in results and bonuses
ck(MM.count("Ce Liu") >= 2, "bonus and results sections must use the same rendering of Ce Liu")
ran(r"the same fighter, one bout", MM, "Ce Liu / Liu Ce reconciliation note present")

# (e) 'biggest mover' must not be claimed for a gainer when a bigger decliner is on the page
for phrase in ("largest move among the majors", "biggest mover among large caps"):
    ck(phrase not in WS, "imprecise superlative restored: %s" % phrase)
ck("largest gain among the session" in WS and "biggest gainer" in WS, "gain-scoped superlatives missing")

# (f) provenance of each disagreeing reading must be attributed
ran(r"\+20% \(CNBC, this run\)", WS, "Snowflake readings attributed per source")
ck("an earlier edition" in WS, "cross-edition readings must be labelled as such")

print("checks: %d, failures: %d" % (checks[0], len(fails)))
for f in fails:
    print("  FAIL:", f)
sys.exit(1 if fails else 0)
