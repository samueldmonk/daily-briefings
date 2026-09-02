# -*- coding: utf-8 -*-
import io, re, datetime, sys

P = {k: io.open(f, encoding="utf-8").read() for k, f in [
    ("ix", "index.html"), ("cy", "cyber-briefing.html"),
    ("ws", "wallstreet-briefing.html"), ("mma", "mma-briefing.html")]}
ALL = "".join(P.values())
raised = []
n = 0
def chk(cond, msg):
    global n
    n += 1
    if not cond:
        raised.append(msg)

# ---- structural: five-tab nav, masthead pills, stamp, summary strips
for k, h in P.items():
    for href in ["index.html", "cyber-briefing.html", "wallstreet-briefing.html",
                 "mma-briefing.html", "archive.html"]:
        chk(f'href="{href}"' in h, f"{k}: nav missing {href}")
    chk(h.count('class="on"') == 1, f"{k}: exactly one active tab")
    for i in ["edition", "datestamp", "updated", "freshline"]:
        chk(f'id="{i}"' in h, f"{k}: missing #{i}")
    chk("America/New_York" in h, f"{k}: missing self-stamp")
    chk("Daily Briefings" in h or "The " in h, f"{k}: title")
for k in ("cy", "ws", "mma"):
    chk('class="tldr"' in P[k], f"{k}: missing summary strip")
chk('<b>The Wire</b>' in P["cy"], "cy: label")
chk('<b>The Tape</b>' in P["ws"], "ws: label")
chk('<b>Tale of the Tape</b>' in P["mma"], "mma: label")
chk('class="tldr"' not in P["ix"], "ix: must use cards not a strip")

# ---- index cards must be BYTE-IDENTICAL to the page summaries they echo
def tldr(h):
    return re.search(r'<div class="tldr"><b>[^<]+</b> <span>(.*?)</span></div>', h, re.S).group(1)
for k in ("cy", "ws", "mma"):
    chk(tldr(P[k]) in P["ix"], f"ix: card text not byte-identical to {k} summary strip")

# ---- CHAMPIONS (CORRECTIONS.md authoritative block)
mm = P["mma"]
board = mm[mm.index("Champions Board"):]
chk("Sean Strickland" in board, "champ: MW must be Strickland")
chk(not re.search(r"<td><b>Middleweight</b></td><td>Khamzat Chimaev", board), "champ: MW must not be Chimaev")
chk("Carlos Ulberg" in board, "champ: LHW must be Ulberg")
chk(not re.search(r"Light Heavyweight</b></td><td>Alex Pereira", board), "champ: LHW not Pereira")
chk("Alexander Volkanovski" in board, "champ: FW must be Volkanovski")
# narrowed: anchor on the row start so the (correctly) vacant WOMEN'S featherweight
# title is not swallowed as a substring. Proof the guard is still alive:
assert re.search(r"<td><b>Featherweight</b></td><td>", board), "FW-vacant guard is dead"
chk(not re.search(r"<td><b>Featherweight</b></td><td>Vacant", board), "champ: FW not vacant")
chk(re.search(r"<td><b>Women's Featherweight</b></td><td>Vacant", board) is not None,
    "champ: W-FW must be vacant")
chk("Justin Gaethje" in board, "champ: LW Gaethje")
chk("Tom Aspinall" in board and "Ciryl Gane" in board, "champ: HW + interim")
chk("Islam Makhachev" in board, "champ: WW")
chk("Petr Yan" in board, "champ: BW")
chk("Joshua Van" in board, "champ: FLW")
chk("Kayla Harrison" in board, "champ: WBW")
chk("Valentina Shevchenko" in board, "champ: WFLW")
chk("Mackenzie Dern" in board, "champ: WSW")
chk("Women's Featherweight</b></td><td>Vacant" in board, "champ: W-FW vacant")
# Harrison must not be credited with a Nunes defence
chk(not re.search(r"Harrison[^<]{0,200}defence over Amanda Nunes", mm), "champ: Harrison 0 defences")

# ---- Parnasse: never Contender Series
for m in re.finditer(r"Parnasse", mm):
    seg = mm[max(0, m.start()-400):m.start()+400]
    if "Contender Series" in seg:
        chk("did not come through the Contender Series" in seg or
            "did <i>not</i> come through the Contender Series" in seg,
            "Parnasse: Contender Series attributed without denial")
chk("KSW" in mm, "Parnasse: KSW provenance missing")
# Hooker record is a record, not a fight count
chk("24-14 professional" in mm and "14-10 in the UFC" in mm, "Hooker: record framing")
# no unsourced family relationship
chk("cousin" not in mm, "mma: 'cousin' blocked")
chk(re.search(r"\bbrother\b", mm) is None, "mma: 'brother' blocked")
# no prose day-count fighting the countdown widget
chk("three days out" not in mm and "days out" not in mm, "mma: prose day-count blocked")
# no false 'former champion'/'challenger' descriptors on debutants
# narrowed: the name is wrapped in <b> tags, so match the framing clause itself.
assert "UFC debut" in mm, "debutant guard is dead"
chk("who makes his UFC debut" in mm, "Parnasse: debutant framing")
chk("ranked contender" not in mm or "not a ranked contender" in mm,
    "Parnasse: must never be called a ranked contender")

# ---- CVSS attribution: SonicWall 10.0 / 7.8 must be qualified everywhere
cy = P["cy"]
for m in re.finditer(r"10\.0", cy):
    seg = cy[max(0, m.start()-160):m.start()+160]
    chk("reported" in seg, "cy: a bare 10.0 without '(reported)'")
for m in re.finditer(r"\b7\.8\b", cy):
    seg = cy[max(0, m.start()-160):m.start()+160]
    chk("reported" in seg, "cy: a bare 7.8 without '(reported)'")
# 9.8 must be a CVSS, never next to a record count
for m in re.finditer(r"9\.8", cy):
    seg = cy[max(0, m.start()-90):m.start()+90]
    chk("million" not in seg, "cy: 9.8 adjacent to a record count")

# ---- KEV: weekday names must match the real calendar, on every page
WD = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
MO = {m: i+1 for i, m in enumerate(
    ["January","February","March","April","May","June","July","August","September",
     "October","November","December"])}
hits = 0
for k, h in P.items():
    for m in re.finditer(r"(%s),?\s+(%s)\s+(\d{1,2})" % ("|".join(WD), "|".join(MO)), h):
        wd, mo, d = m.group(1), m.group(2), int(m.group(3))
        hits += 1
        real = WD[datetime.date(2026, MO[mo], d).weekday()]
        chk(real == wd, f"{k}: '{wd}, {mo} {d}' is actually a {real}")
chk(hits >= 3, "calendar guard matched too little to be alive (%d)" % hits)
# Sept 5 must never be called a Friday
chk("Friday, September 5" not in ALL and "until Friday" not in ALL, "Sept 5 is a Saturday")

# ---- KEV countdowns: verified due dates only, consistent across the page
chk("(3 days left)" in cy and "September 5, 2026" in cy, "cy: Switchvox 3-day countdown")
chk("(14 days left)" in cy and "September 16, 2026" in cy, "cy: 48710 14-day countdown")
# PaperCut must carry no countdown
pc = cy[cy.index("PaperCut")-400:cy.index("PaperCut")+400] if "PaperCut" in cy else ""
chk("days left" not in pc, "cy: PaperCut must have no inferred countdown")
# Patch Priority deadline must match the KEV section
chk(cy.count("September 5") >= 2, "cy: patch priority / KEV deadline agreement")
# Entra ID must never be listed as exploited or a zero-day
chk("Entra" not in cy, "cy: Entra ID retracted-exploitation item must stay off")

# ---- Markets
ws = P["ws"]
chk("7,666.60" in ws and "26,217.83" in ws and "53,061.95" in ws, "ws: closes")
chk("+295.07" in ws or "295.07 points" in ws, "ws: Dow points")
# levels only in the scorecard/lead, never presented as intraday
chk("as of ~" not in ws, "ws: no stale intraday framing post-close")
chk("official close" in ws.lower(), "ws: must lead with the official close after 4 PM")
# $7.04 must sit within 200 chars of 'before certain costs'
for m in re.finditer(r"\$7\.04", ws):
    seg = ws[max(0, m.start()-200):m.start()+200]
    chk("before certain costs" in seg, "ws: $7.04 unqualified")
# no invented fiscal-quarter label on Palo Alto
pa = ws[ws.index("Palo Alto Networks &mdash; down")-100:] if "Palo Alto Networks &mdash; down" in ws else ""
chk(not re.search(r"fiscal Q[1-4]", pa[:1400]), "ws: invented Palo Alto fiscal quarter")
chk("No fiscal-quarter label is asserted" in ws, "ws: fiscal-quarter refusal must be printed")
# $425 must not be tied to a named weekday unless explicitly denied
for m in re.finditer(r"\$425", ws):
    seg = ws[max(0, m.start()-200):m.start()+200]
    if any(w in seg for w in WD):
        chk("prior close" in seg, "ws: $425 tied to a weekday")
# no 'highest since' inside a table cell
for m in re.finditer(r"highest since", ws):
    seg = ws[max(0, m.start()-500):m.start()]
    chk(seg.rfind("<td") <= seg.rfind("</td>"), "ws: 'highest since' inside a table cell")
# GitLab must not be given a direction
chk("GitLab" not in ws or "decliner" not in ws, "ws: GitLab direction fabricated")
# live widget blocks all present
for w in ["ticker-tape", "single-quote", "timeline", "stock-heatmap",
          "mini-symbol-overview", "embed-widget-events"]:
    chk(w in ws, f"ws: missing live block {w}")
chk(ws.count("embed-widget-single-quote") == 3, "ws: three single-quote widgets")
chk("FOREXCOM:SPXUSD" in ws and "FOREXCOM:NSXUSD" in ws and "FOREXCOM:DJI" in ws, "ws: index symbols")
chk("TVC:USOIL" in ws and "TVC:US10Y" in ws, "ws: tape must keep oil + 10Y")
chk('class="livebar"' in ws and "LIVE QUOTES" in ws, "ws: livebar")
chk("Quotes stream live" in ws, "ws: note line")
chk("After-Hours Movers" in ws, "ws: after-hours section required after 4 PM ET")
chk("Nothing here is investment advice" in ws, "ws: disclaimer")
# no live widgets anywhere else
for k in ("ix", "cy", "mma"):
    chk("tradingview.com" not in P[k], f"{k}: must carry no live widgets")

# ---- carried material must be labelled
for k in ("cy", "ws", "mma"):
    chk("arried" in P[k], f"{k}: carried-material labelling absent")

# ---- sources present on all four
for k in ("cy", "ws", "mma"):
    chk(P[k].count("https://") >= 8, f"{k}: source footer too thin")
    chk("<footer>" in P[k], f"{k}: footer")
chk('class="disc"' in P["cy"] and 'class="disc"' in P["ws"] and 'class="disc"' in P["mma"], "disclaimers")

# ---- MMA countdown script
chk('id="ufccdn"' in mm and "2026-09-05T16:00:00Z" in mm, "mma: countdown to Sept 5 12 PM ET")

# ---- nothing 'upcoming' that has already happened
chk("August 29" in mm and "Last Event" in mm, "mma: last event section")
chk("Shevchenko vs. Silva is off" in mm, "mma: UFC 332 status")

# ---- NEW GUARDS from this run's read-through ----
# (1) masthead/kicker glyph must be the shield, never the flower
chk("⚘" not in ALL, "glyph: U+2698 flower used where the shield U+26E8 belongs")
chk("⛨" in P["cy"] and "⛨" in P["ix"], "glyph: shield missing from cyber masthead / index kicker")
# (2) severity adjectives must not assert an unadopted score
for k in ("cy", "ix"):
    for m in re.finditer(r"maximum-severity|max-severity", P[k]):
        seg = P[k][max(0, m.start()-200):m.start()+200]
        chk("reported" in seg, f"{k}: 'maximum-severity' asserts an attributed CVSS")
# (3) no doubled preposition in the corroboration sentence
chk("fetches across four editions" in ws or "independent fetches" not in ws,
    "ws: doubled 'across' in the corroboration sentence")
chk("identical across four independent fetches across" not in ws, "ws: doubled 'across'")
# (4) a timestamped reading must never be demoted below an untimed one silently
for m in re.finditer(r"carrying a timestamp|the only timed reading|the only reading carrying a timestamp", ws):
    seg = ws[max(0, m.start()-320):m.start()+320]
    chk("neither is adopted" in seg or "only the direction" in seg or "disputed" in seg,
        "ws: timed vs untimed reading printed without saying neither is adopted")
# (5) article agreement before a vowel-sound percentage
chk(not re.search(r"\ba (?=<b>1[18]\.)", ws), "ws: 'a' before an 18/11 percentage")
assert re.search(r"\ban <b>18\.7%", ws), "article guard is dead"

print("checks:", n, "raised:", len(raised))
for r in raised:
    print("  RAISED:", r)
sys.exit(1 if raised else 0)
