# -*- coding: utf-8 -*-
"""Guards for the 2026-09-03 10:08 AM ET edition."""
import io, re, sys
D = "/sessions/magical-nifty-noether/mnt/outputs/"
P = {k: io.open(D + f, encoding="utf-8").read()
     for k, f in [("ix","index.html"),("cy","cyber-briefing.html"),
                  ("ws","wallstreet-briefing.html"),("mma","mma-briefing.html")]}
fails, n = [], 0
def has(k, s, why=""):
    global n; n += 1
    if s not in P[k]: fails.append("MISSING [%s] %s :: %r" % (k, why, s[:70]))
def no(k, s, why=""):
    global n; n += 1
    if s in P[k]: fails.append("FORBIDDEN [%s] %s :: %r" % (k, why, s[:70]))
def nore(k, pat, why):
    global n; n += 1
    if re.search(pat, P[k]): fails.append("REGEX [%s] %s :: %s" % (k, why, pat))

# ---- champions: the thirty-run regression -------------------------------
for k in ("mma",):
    has(k, "Sean Strickland", "MW champion")
    has(k, "Carlos Ulberg", "LHW champion")
    has(k, "Alexander Volkanovski", "FW champion not vacant")
    has(k, "Justin Gaethje", "LW champion")
    has(k, "Joshua Van", "FLY champion")
    has(k, "Mackenzie Dern", "W-SW champion")
    has(k, "Kayla Harrison", "W-BW champion")
    has(k, "Petr Yan", "BW champion")
    has(k, "Islam Makhachev", "WW champion")
    has(k, "Tom Aspinall", "HW champion")
    has(k, "Ciryl Gane", "interim HW")
    has(k, "Valentina Shevchenko", "W-FLY champion")
nore("mma", r"Middleweight[^<]*</td>\s*<td[^>]*>Khamzat Chimaev", "Chimaev listed as MW champ")
nore("mma", r"Light Heavyweight[^<]*</td>\s*<td[^>]*>Alex Pereira", "Pereira listed as LHW champ")
nore("mma", r"Featherweight[^<]*</td>\s*<td[^>]*>\s*[Vv]acant", "FW listed vacant")
# Pereira may only appear as the man Gane/Ulberg beat, never as champion
nore("mma", r"Pereira[^<.]{0,40}champion", "Pereira described as champion")

# ---- Parnasse provenance: sixteenth run ---------------------------------
no("mma", "Contender Series earlier in 2026", "Parnasse/DWCS conflation")
nore("mma", r"Parnasse[^.]{0,200}Contender Series", "Parnasse attributed to DWCS")
has("mma", "two-time KSW", "Parnasse KSW provenance")
has("mma", "UFC debutant", "Parnasse still a debutant")
nore("mma", r"Parnasse[^.]{0,80}(veteran|ranked contender)", "Parnasse over-described")

# ---- KEV deadlines: chronological + identical across sections ------------
has("cy", "Saturday, September 5, 2026", "Patch Priority carries Sept 5")
no("cy", "Friday, September 5", "Sept 5 2026 is a Saturday, not a Friday")
has("cy", "<b>Saturday, September 5</b>", "KEV list carries Sept 5")
has("cy", "2 days left", "Sept 5 countdown")
has("cy", "11 days left", "Sept 14 countdown")
has("cy", "13 days left", "Sept 16 countdown")
i5 = P["cy"].find("<b>Saturday, September 5</b>")
i14 = P["cy"].find("<b>Monday, September 14</b>")
i16 = P["cy"].find("<b>Wednesday, September 16</b>")
n += 1
if not (0 < i5 < i14 < i16): fails.append("ORDER [cy] KEV deadlines out of chronological order")
nore("cy", r"KEV[^.]{0,60}September 3", "KEV batch misdated to Sept 3 (CISA page says Sept 2)")

# ---- CVSS: vendor/CISA figures, no invented score for 48710 -------------
has("cy", "CVE-2026-48710")
nore("cy", r"CVE-2026-48710</td><td[^>]*>\s*<?\d", "a digit scored against 48710")
has("cy", "Not stated in sources fetched", "48710 score withheld")
has("cy", "9.4 (v4.0)", "PaperCut 82078 vendor score")
has("cy", "8.8 (v4.0)", "PaperCut 81578 vendor score")
no("cy", "CVE-2026-59822</td>", "59822 given a Vulnerability Watch row it was not sourced for")
has("cy", "CVE-2026-59822", "59822 present in the KEV list")

# ---- Langflow: not asserted as KEV, no unsourced 7,000 -------------------
has("cy", "CVE-2026-0768")
has("cy", "does <b>not</b> appear among the vulnerabilities CISA added", "Langflow KEV status stated")
nore("cy", r"7,000 servers[^.]{0,30}(are|were) ", "unsourced 7,000-server claim asserted")
has("cy", "no source consulted for this edition states it directly", "7,000 disclosed as unadopted")

# ---- date-mismatch traps refused, figures not reprinted -----------------
has("cy", "February 18, 2026", "IDMerit disclosure date given as the reason for refusal")
has("cy", "It is not:", "IDMerit refusal marker follows the framing")
nore("cy", r"IDMerit[^.]{0,400}(disclosed|reported) (today|this week)", "IDMerit asserted as current news")
no("cy", "Pennsylvania Attorney General&rsquo;s Office was hit", "Penn AG published as current")
# the refused Penn AG data volume must never be reprinted
nore("cy", r"INC Ransom[^.]{0,80}\d+(\.\d+)?\s*(TB|GB|million)", "refused Penn AG figure reprinted")

# ---- markets: no invented close, open-session honesty --------------------
has("ws", "7,666.60"); has("ws", "26,217.83"); has("ws", "53,061.95")
has("ws", "+295.07"); has("ws", "ninth consecutive")
has("ws", "readings as of ~10:05&ndash;10:30 AM ET", "as-of window in the lead headline")
has("ws", "nothing in it is the current print", "stale-by-an-hour disclosure")
has("ws", "Nothing in this section is a closing price", "open-session disclaimer")
nore("ws", r"(S&amp;P 500|Dow|Nasdaq)[^.]{0,40}closed (higher|lower) (today|Thursday)", "Thursday framed as closed")
no("ws", "After-Hours Movers", "after-hours block before 4 PM ET")
# no precise Thursday index LEVEL anywhere in editorial
nore("ws", r"S&amp;P 500 (at|to) 7,[0-9]{3}\.[0-9]{2}[^<]{0,30}Thursday", "Thursday S&P level asserted")

# ---- sector breadth: refused, and the refused figures NOT reprinted -----
has("ws", "refused for a fourteenth consecutive run", "sector refusal stated")
nore("ws", r"Information Technology \+1\.03", "refused sector figure reprinted")
nore("ws", r"Energy[^.]{0,20}-1\.25", "refused sector figure reprinted")
nore("ws", r"8 out of 11|eight of eleven", "refused breadth count reprinted")

# ---- Snowflake: windows never blended into one range --------------------
nore("ws", r"22\s*(&ndash;|-|to)\s*24%", "after-hours and pre-market blended into a range")
nore("ix", r"22\s*(&ndash;|-|to)\s*24%", "blended range on the front page")
has("ws", "more than 24% pre-market")
has("ix", "$12.9 billion", "index card matches the WS lead")
has("ws", "two windows, not a range")

# ---- superlative scoping -------------------------------------------------
nore("ws", r"largest (pre-market )?move(?![^<]{0,120}(among|of the))", "unscoped superlative")

# ---- jobless claims: released, actual published -------------------------
has("ws", "206,000"); has("ws", "205,000"); has("ws", "204,000")
nore("ws", r"jobless claims[^.]{0,80}(is due|will be released|due at 8:30)", "claims framed as upcoming after release")

# ---- Waller / FOMC dates -------------------------------------------------
has("ws", "September 15&ndash;16 FOMC")
has("ws", "September 11")
nore("ws", r"FOMC[^.]{0,30}September 16 2:00", "unsourced FOMC time")

# ---- chrome present on all four -----------------------------------------
for k in P:
    has(k, 'id="edition"'); has(k, 'id="datestamp"'); has(k, 'id="updated"')
    has(k, 'id="freshline"'); has(k, 'class="pill live"')
    for href in ("index.html","cyber-briefing.html","wallstreet-briefing.html",
                 "mma-briefing.html","archive.html"):
        has(k, 'href="%s"' % href, "five-tab nav")
    has(k, "America/New_York", "self-stamp JS")
for k, lbl in (("cy","The Wire"), ("ws","The Tape"), ("mma","Tale of the Tape")):
    has(k, '<div class="tldr"><b>%s</b>' % lbl, "tailored summary label")
no("ix", 'class="tldr"', "index should use cards, not a tldr strip")

# ---- live widgets --------------------------------------------------------
for w in ("ticker-tape","single-quote","timeline","stock-heatmap","mini-symbol-overview","events"):
    has("ws", "embed-widget-%s.js" % w, "widget block")
has("ws", "FOREXCOM:SPXUSD"); has("ws", "FOREXCOM:NSXUSD"); has("ws", "FOREXCOM:DJI")
has("ws", "TVC:USOIL"); has("ws", "TVC:US10Y")
for k in ("cy","mma","ix"):
    no(k, "s3.tradingview.com", "live widgets outside the markets page")
has("mma", 'id="ufccdn"', "MMA countdown target")
has("mma", "2026-09-05T19:00:00Z", "countdown to the Sept 5 main card")

# ---- desk jargon must not reach the reader ------------------------------
for k in P:
    for j in ("this run's fetch", "search return", "doubly sourced", "re-sourced this run",
              "the 0816 edition", "the 0849 edition", "snippet"):
        no(k, j, "desk jargon in reader-facing copy")

# ---- counted claims ------------------------------------------------------
n += 1
if "five names against a source that says five" in P["mma"]:
    names = ["Hector Santiago","Francesco Nuzzi","Rei Tsuruya","Kai Asakura","Denise Gomes"]
    seg = P["mma"].split("$25,000</b> finish bonuses to")[1][:400]
    if sum(1 for x in names if x in seg) != 5:
        fails.append("COUNT [mma] finish-bonus names do not total five")

# ---- sources footers -----------------------------------------------------
for k in ("cy","ws","mma"):
    has(k, "<footer>"); has(k, "https://")
    n += 1
    if P[k].count("<li>") < 12: fails.append("SOURCES [%s] fewer than 12 source entries" % k)


# --- guards added from this run's read-through ---
no("ws", "8 AM ET yesterday", "Brent $99.38 misdated to yesterday")
has("ws", "$99.38</b> by 8 AM ET this morning", "Brent second reading dated correctly")
nore("ws", r"snapshots taken minutes apart", "unsupported simultaneity claim about index readings")
has("ws", "They are not all the same moment", "index readings honestly scoped")
no("ws", "the session's outsized move", "pre-market move claimed for the regular session")
has("ws", "a 24% move before the bell", "Snowflake move scoped to pre-market")
for k in P:
    for j in ("this run's return", "this run's listings", "this run's fetches", "a fresh fetch this run",
              "anything fetched this run", "Not re-sourced", "9:05 AM fetch"):
        no(k, j, "desk jargon in reader-facing copy")
# weekday/date integrity across all pages
import datetime as _dt
for k in P:
    n += 1
    for m in __import__("re").finditer(r"(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday), (September|October) (\d{1,2})", P[k]):
        wd, mo, dd = m.group(1), m.group(2), int(m.group(3))
        real = _dt.date(2026, 9 if mo == "September" else 10, dd).strftime("%A")
        if real != wd:
            fails.append("WEEKDAY [%s] %s %s %d is a %s" % (k, wd, mo, dd, real))

print("checks:", n)
print("raised:", len(fails))
for f in fails: print("  -", f)
