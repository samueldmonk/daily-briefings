#!/usr/bin/env python3
"""Validator for the 10:50 AM Saturday Aug 29 2026 edition.

Carries the guard families established in validate_1020.py and adds guards for
this run's new material (McKesson, Ubiquiti, the third rate read, the callout,
the two-to-one punch count, the seventh UFC.com fetch).
"""
import io, os, re, sys

D = os.path.dirname(os.path.abspath(__file__))
STAMP = "10:50 AM"
PAGES = {
    "index": "index.html",
    "cyber": "cyber-briefing.html",
    "ws": "wallstreet-briefing.html",
    "mma": "mma-briefing.html",
}
S = {k: io.open(os.path.join(D, v), encoding="utf-8").read() for k, v in PAGES.items()}

checks = 0
fails = []


def ck(cond, msg):
    global checks
    checks += 1
    if not cond:
        fails.append(msg)


def has(page, needle, msg=None):
    ck(needle in S[page], msg or ("%s: missing %r" % (page, needle[:90])))


def hasnt(page, needle, msg=None):
    ck(needle not in S[page], msg or ("%s: FORBIDDEN present %r" % (page, needle[:90])))


def strip_tags(t):
    t = re.sub(r"<script.*?</script>", " ", t, flags=re.S)
    t = re.sub(r"<style.*?</style>", " ", t, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", t)


# ============================================================ structure
for k in S:
    for tab in ["index.html", "cyber-briefing.html", "wallstreet-briefing.html",
                "mma-briefing.html", "archive.html"]:
        has(k, 'href="%s"' % tab, "%s: nav missing %s" % (k, tab))
    ck(S[k].count('class="on"') == 1, "%s: expected exactly one active tab" % k)
    for pid in ['id="edition"', 'id="datestamp"', 'id="updated"', 'id="freshline"']:
        has(k, pid, "%s: missing %s" % (k, pid))
    has(k, "America/New_York", "%s: missing self-stamp JS" % k)
    has(k, "briefings refresh every 30 minutes", "%s: missing freshline text" % k)
    has(k, "Saturday, August 29, 2026", "%s: missing datestamp" % k)
    ck(S[k].rstrip().endswith("</html>"), "%s: truncated file" % k)

# tldr only on the three briefings
for k in ["cyber", "ws", "mma"]:
    has(k, '<div class="tldr">', "%s: missing tldr strip" % k)
hasnt("index", '<div class="tldr">', "index must not carry a tldr strip")

# index cards must equal each page's tldr (whitespace-normalised)
tld = {}
for k, label in [("cyber", "The Wire"), ("ws", "The Tape"), ("mma", "Tale of the Tape")]:
    m = re.search(r'<div class="tldr"><b>%s</b> <span>(.*?)</span></div>' % re.escape(label), S[k], re.S)
    ck(m is not None, "%s: tldr label %r not found" % (k, label))
    if m:
        tld[k] = re.sub(r"\s+", " ", m.group(1)).strip()
idx_paras = [re.sub(r"\s+", " ", p).strip()
             for p in re.findall(r'<p>(.*?)</p>\n<a class="go"', S["index"], re.S)]
ck(len(idx_paras) == 3, "index: expected 3 big cards, found %d" % len(idx_paras))
for k, p in zip(["cyber", "ws", "mma"], idx_paras):
    ck(tld.get(k) == p, "index card for %s does not match that page's tldr" % k)

# ============================================================ live widgets
tv = "s3.tradingview.com/external-embedding/embed-widget-"
ck(S["ws"].count(tv) == 8, "ws: expected 8 TradingView widget scripts, got %d" % S["ws"].count(tv))
for w in ["ticker-tape", "single-quote", "timeline", "stock-heatmap",
          "mini-symbol-overview", "events"]:
    has("ws", tv + w, "ws: missing widget %s" % w)
ck(S["ws"].count(tv + "single-quote") == 3, "ws: expected exactly 3 single-quote widgets")
for sym in ["FOREXCOM:SPXUSD", "FOREXCOM:NSXUSD", "FOREXCOM:DJI", "TVC:USOIL", "TVC:US10Y"]:
    has("ws", sym, "ws: ticker tape missing %s" % sym)
has("ws", '"symbol":"NASDAQ:PYPL"', "ws: Chart of the Day must be NASDAQ:PYPL")
for k in ["index", "cyber", "mma"]:
    hasnt(k, tv, "%s: must carry no live widgets" % k)

# ============================================================ markets: closes
close_rows = [("7,711.76", "26,402.42", "53,559.99"), ("7,730.99", "26,541.35", "53,569.44")]
for row in close_rows:
    for v in row:
        has("ws", v, "ws: missing close %s" % v)
# reconciliation guards, tolerance stricter than the prose
ck(abs((53569.44 - 9.45) - 53559.99) < 0.005, "Dow points reconciliation failed")
ck(abs((7711.76 / 7730.99 - 1) * 100 + 0.25) < 0.005, "S&P percent reconciliation failed")
ck(abs((26402.42 / 26541.35 - 1) * 100 + 0.52) < 0.005, "Nasdaq percent reconciliation failed")
has("ws", "&minus;0.2487%")
has("ws", "&minus;0.5234%")
# closed-market page discipline
hasnt("ws", "as of ~", "ws: intraday marker on a closed-market page")
has("ws", "Monday, August 31", "ws: must say when the tape reopens")
hasnt("ws", "7,673.04", "ws: rejected Thursday level must stay out")
hasnt("ws", "After-Hours", "ws: no after-hours block on a weekend morning")
hasnt("ws", "After Hours", "ws: no after-hours block on a weekend morning")
# 1.82% may appear ONLY inside its own rejection sentence
for m in re.finditer(r"1\.82%", S["ws"]):
    w = strip_tags(S["ws"][max(0, m.start() - 260):m.end() + 120])
    ck("did not reappear" in w or "stays unpublished" in w,
       "ws: 1.82% outside its rejection context")

# ============================================================ markets: the third rate read
has("ws", "about one in three")
has("ws", "above 50/50")
has("ws", "one-in-three odds of a hike is the same state as roughly two-in-three odds of a hold")
has("ws", "48%")
has("ws", "nearly 70%")
has("ws", "three independent looks")
has("ws", "adopts neither and averages nothing")
has("ws", "re-verified a seventh time at " + STAMP)
hasnt("ws", "re-verified a sixth time", "ws: stale re-verification counter")
# Warsh substance sourced this run
has("ws", "muddled July news conference")
has("ws", "declined to set out the conditions")
has("ws", "longstanding 2% goal")
# Salesforce spread: six reads, counted correctly
sf = strip_tags(S["ws"])
ck("Six different percentages" in sf, "ws: Salesforce card must say six")
ck(sf.count("22.87%") >= 1 and "11.2%" in sf, "ws: Salesforce spread incomplete")
hasnt("ws", "a fourth read of the same move", "ws: stale Salesforce miscount")
# no fresh tags on a closed tape
ck(S["ws"].count('tag new"') == 0, "ws: fresh tags are impossible while the market is shut")

# ============================================================ cyber: McKesson
_cyflat = re.sub(r"\s+", " ", S["cyber"])
for n in ["McKesson", "ShinyHunters", "284 million", "$55,236,150", "Form 8-K",
          "August 25, 2026", "Okta", "Snowflake", "Salesforce", "vishing",
          "mckesson[.]claims", "ReliaQuest", "Health-ISAC", "1TB"]:
    has("cyber", n, "cyber: McKesson detail missing: %s" % n)
has("cyber", "raw count of roughly 284 million data records", "cyber: record-vs-people correction required")
has("cyber", "not independently verified", "cyber: must state the outlet did not verify the claims")
ck("McKesson has confirmed none of this list" in _cyflat, "cyber: McKesson confirmation refusal missing")
has("cyber", "not publicly disclosed which third-party applications")
# the 284M must never be asserted as a victim count
cyt = strip_tags(S["cyber"])
ck("284 million patients" not in cyt or "Earlier reporting stated" in cyt,
   "cyber: '284 million patients' must appear only as the superseded earlier framing")
ck("This page prints neither as a victim count." in cyt, "cyber: victim-count refusal required")
# exactly one fresh tag on cyber, and it carries this edition's stamp
ck(S["cyber"].count('tag new"') == 1, "cyber: expected exactly 1 fresh tag, got %d" % S["cyber"].count('tag new"'))
for m in re.finditer(r'tag new">([^<]*)<', S["cyber"]):
    ck(STAMP in m.group(1), "cyber: fresh tag not carrying %s: %r" % (STAMP, m.group(1)))
# PaperCut demoted, not deleted
has("cyber", "Carried &middot; from the 10:20 edition")
has("cyber", "PaperCut's emergency patch was bypassed")
has("cyber", "Emergency Patch Release 2")

# ============================================================ cyber: Ubiquiti
for c in ["CVE-2026-77537", "CVE-2026-77550", "CVE-2026-77554"]:
    has("cyber", c, "cyber: missing Ubiquiti CVE %s" % c)
has("cyber", "UniFi Protect")
has("cyber", "UniFi OS")
has("cyber", "UniFi Talk")
has("cyber", "CRLF injection")
_cyflat = re.sub(r"\s+", " ", S["cyber"])
ck(_cyflat.count("Not KEV-listed; no exploitation stated.") == 2
   and "Not KEV-listed, and no source seen this run states in-the-wild exploitation" in _cyflat,
   "cyber: each Ubiquiti row must disclaim KEV listing and exploitation")

# ============================================================ cyber: CVE whitelist + KEV
ALLOWED = {
    "CVE-2026-8452", "CVE-2019-1068", "CVE-2026-53362", "CVE-2023-49105",
    "CVE-2026-66384", "CVE-2022-0995", "CVE-2021-23758", "CVE-2015-5287",
    "CVE-2015-3246", "CVE-2026-81578", "CVE-2026-82078", "CVE-2026-69836",
    "CVE-2026-21962", "CVE-2026-77537", "CVE-2026-77550", "CVE-2026-77554",
}
found = set(re.findall(r"CVE-\d{4}-\d{4,6}", S["cyber"]))
ck(found <= ALLOWED, "cyber: unlisted CVE identifier(s): %s" % sorted(found - ALLOWED))
ck(len(found) >= 15, "cyber: CVE liveness check failed (%d found)" % len(found))
hasnt("cyber", "9.8", "cyber: the rejected 9.8 score must stay out")
for cd in ["(0 days left &mdash; due today)", "(1 day left)", "(11 days left)", "(12 days left)"]:
    has("cyber", cd, "cyber: missing KEV countdown %s" % cd)
has("cyber", "BOD 26-04")
for m in re.finditer(r"BOD 22-01", S["cyber"]):
    w = strip_tags(S["cyber"][max(0, m.start() - 200):m.end() + 200])
    ck("superseded" in w, "cyber: BOD 22-01 mentioned without being marked superseded")
ck("no CISA alert dated later than August 26" in _cyflat, "cyber: KEV freshness disclosure missing")
has("cyber", "not the same as CISA having published none")
# Citrix: both build sets kept, advisory named
for b in ["14.1-73.32", "13.1-63.21", "14.1-72.61", "13.1-63.18", "13.1-37.272", "CTX696604"]:
    has("cyber", b, "cyber: missing Citrix build/advisory %s" % b)
# Oracle absence explained, not asserted
for m in re.finditer(r"CVE-2026-21962", S["cyber"]):
    w = strip_tags(S["cyber"][max(0, m.start() - 260):m.end() + 260])
    ck("not carried" in w or "not restated" in w,
       "cyber: Oracle CVE mentioned outside its absence note")
# GPUThor stays CVE-less and non-KEV
has("cyber", "no CVE stated")
has("cyber", "this is <b>not</b> a KEV item")

# ============================================================ MMA
mm = strip_tags(S["mma"])
has("mma", "seventh consecutive fetch")
hasnt("mma", "sixth consecutive fetch", "mma: stale UFC.com fetch counter")
has("mma", "2026-08-28T14:03")
has("mma", "two sources for the uppercut against one for the hook")
has("mma", "still prints both")
has("mma", "first male UFC champion from China")
has("mma", "called for a title shot")
ck("Nothing has been announced." in mm, "mma: callout must not be presented as a booking")
has("mma", "second professional MMA loss")
hasnt("mma", "a derivation from the pre-fight record, not a figure any source stated after the fight",
      "mma: the withdrawn derivation caveat must be replaced, not kept")
# results table integrity
for name in ["Song Yadong", "Umar Nurmagomedov", "Denise Gomes", "Yan Xiaonan",
             "Kai Asakura", "Aoriqileng", "Sumudaerji", "Alex Perez", "Liu Ce",
             "Levi Rodrigues Jr.", "Bilal Hasan", "Nilson Rojas", "Andre Lima",
             "Rei Tsuruya", "Sean Woodson", "Francesco Nuzzi", "Hector Santiago",
             "Julia Polastri", "Cam Nelson"]:
    has("mma", name, "mma: missing fighter %s" % name)
has("mma", "1:48")
has("mma", "4:49 of round one")
hasnt("mma", "Undecided", "mma: no bout may remain undecided")
hasnt("mma", "live now", "mma: the card is complete")
# bonuses
has("mma", "$100,000")
has("mma", "Kevin Chang")
has("mma", "ten finishes")
for w in ["Liu Ce", "Levi Rodrigues Jr.", "Song Yadong", "Bilal Hasan"]:
    ck(w in mm, "mma: bonus winner missing: %s" % w)
for banned in ["no bonuses have been announced", "None announced", "bonuses are unannounced",
               "since the main event has not been resulted"]:
    hasnt("mma", banned, "mma: superseded bonus claim present: %r" % banned)
# weight misses: three, and thirteen is the bout count
ck("Three fighters missed weight" in mm or "Three fighters missed" in mm,
   "mma: weight-miss count must be three")
hasnt("mma", "Two fighters missed weight", "mma: stale weight-miss count")
has("mma", "thirteen is the number of contests on the")
hasnt("mma", "115-pound", "mma: unsourced strawweight limit must stay out")
# spelling splits preserved
for form in ["Aoriqileng", "Qileng Aori", "Sumudaerji", "Su Mudaerji"]:
    has("mma", form, "mma: spelling form missing: %s" % form)
# exactly one fresh tag on MMA, carrying this stamp
ck(S["mma"].count('tag new"') == 1, "mma: expected exactly 1 fresh tag, got %d" % S["mma"].count('tag new"'))
for m in re.finditer(r'tag new">([^<]*)<', S["mma"]):
    ck(STAMP in m.group(1), "mma: fresh tag not carrying %s: %r" % (STAMP, m.group(1)))
ck(S["mma"].count('tag pros"') == 4, "mma: expected 4 prospect tags")

# ============================================================ champions board
tds = re.findall(r"<td[^>]*>(.*?)</td>", S["mma"], re.S)
rows = re.findall(r"<tr>(.*?)</tr>", S["mma"], re.S)
champ_rows = [r for r in rows if "Heavyweight" in r or "Flyweight" in r or "Bantamweight" in r
              or "Welterweight" in r or "Lightweight" in r or "Featherweight" in r
              or "Middleweight" in r or "Strawweight" in r]
ck(len(champ_rows) >= 11, "mma: champions board should have >=11 rows, got %d" % len(champ_rows))
CHAMPS = {
    "Heavyweight": "Tom Aspinall", "Light Heavyweight": "Carlos Ulberg",
    "Middleweight": "Sean Strickland", "Welterweight": "Islam Makhachev",
    "Lightweight": "Justin Gaethje", "Featherweight": "Alexander Volkanovski",
    "Bantamweight": "Petr Yan", "Flyweight": "Joshua Van",
}
for div, champ in CHAMPS.items():
    ck(champ in S["mma"], "mma: champion missing for %s: %s" % (div, champ))
# regressions tested in champion cells only
champ_cells = []
for r in champ_rows:
    cells = re.findall(r"<td[^>]*>(.*?)</td>", r, re.S)
    if len(cells) >= 2:
        champ_cells.append(strip_tags(cells[1]))
joined = " || ".join(champ_cells)
for bad in ["Pereira", "Chimaev", "Topuria", "vacant", "Vacant"]:
    ck(bad not in joined, "mma: REGRESSION - %r appears in a champion cell" % bad)

# champions near-miss must be disclosed, and the rejected names explained not adopted
has("mma", "came back naming Alex Pereira at light heavyweight and Khamzat")
has("mma", "3:45 of round one at UFC 327 on April 11, 2026")
has("mma", "split decision at UFC 328 on")
has("mma", "The board was not changed.")
has("mma", "does not extend the agreement counter")
has("mma", "fiftieth consecutive")
has("mma", "not expected back until early")
hasnt("mma", "seventh consecutive edition</b> of", "mma: stale ESPN-agreement counter")
hasnt("mma", "forty-eighth consecutive", "mma: stale unchanged-board counter")
# forty-ninth may appear ONLY as a historical reference to the 10:20 edition, never as this run's claim
for m in re.finditer("forty-ninth consecutive", S["mma"]):
    w = strip_tags(S["mma"][max(0, m.start() - 260):m.end() + 160])
    ck("10:20 AM edition" in w, "mma: forty-ninth counter used outside its historical attribution")
_mmaflat = re.sub(r"\s+", " ", strip_tags(S["mma"]))
for bad in ["Pereira", "Chimaev"]:
    for m in re.finditer(bad, _mmaflat):
        w = _mmaflat[max(0, m.start() - 320):m.end() + 320]
        ck("superseded" in w or "rejected" in w or "Interim" in w or "took the middleweight belt from" in w
           or "regressions" in w or "vacant light-heavyweight" in w,
           "mma: %s appears without its rejection/interim context" % bad)
has("index", "stale listing naming the two men")
hasnt("mma", "Results marked undecided", "mma: vacuous undecided disclaimer")

# ============================================================ trap greps (all pages)
for k in S:
    for trap in ["Shamil Yakhyaev", "Cody Salkilld", "Abdul-Rakhman"]:
        hasnt(k, trap, "%s: known-bad name %r" % (k, trap))

# ============================================================ stale-novelty enumeration
POSITIVE = ["this run", "this edition", "New at", "new this run", "turned over since",
            "the only figure that changed", "sourced this run", "fetched this run",
            "re-confirmed this run", "genuinely new"]
ALLOW = [
    # negatives are always fine
    "no source seen this run", "none was stated", "no source fetched this run",
    "was not restated by any source seen", "no source seen in any edition",
    "no exploitation stated", "no source seen this run states",
    "No source seen this run says",
    # true-for-this-run positives
    STAMP, "fetched this run", "a post-event report fetched this run",
    "A third report, fetched this run",
]
for k in ["cyber", "ws", "mma"]:
    txt = strip_tags(S[k])
    for phrase in ["New at", "turned over since", "the only figure that changed",
                   "the one genuinely new item"]:
        for m in re.finditer(re.escape(phrase), txt):
            w = txt[max(0, m.start() - 200):m.end() + 260]
            ck(any(a in w for a in ALLOW),
               "%s: novelty claim %r without an allow-listed context" % (k, phrase))
# no page may still claim the 10:20 edition's novelty as its own
for k in ["cyber", "ws", "mma", "index"]:
    txt = strip_tags(S[k])
    for m in re.finditer(r"New &middot; 10:20 AM|New · 10:20 AM", S[k]):
        fails.append("%s: a 10:20 AM fresh tag survives into the %s edition" % (k, STAMP))
        checks += 1

# stale-attribution greps: phrases that named the wrong edition and were fixed this run
for bad in ["it finished between this edition and the last one",
            "At fetch time this run the promotion's own main-card",
            "news rail this run links",
            "a second listing this run says",
            "listing seen this run describes the Lima finish",
            "no division label\nin the previous edition",
            "a fact the previous edition had only half of",
            "printed here for the first time",
            "this is the edition that could print them",
            "Three of the four cards below are carried"]:
    hasnt("mma", bad, "mma: stale attribution survived: %r" % bad)
for bad in ["Reporting seen this run adds",
            "Chart of the Day moves from Marvell",
            "10-year figure comes with an explicit cause this run",
            "not this one; it is in On the Radar"]:
    hasnt("ws", bad, "ws: stale attribution survived: %r" % bad)
for bad in ["re-verified against two independent reports this run",
            "The source seen this run gives",
            "material seen this run",
            "That is consistent with the board below"]:
    hasnt("cyber", bad, "cyber: stale attribution survived: %r" % bad)

# ============================================================ stamps + unique hrefs
for k in S:
    hasnt(k, "10:20 AM ET", "%s: stale edition stamp in the meta row" % k)
    has(k, STAMP + " ET", "%s: missing this edition's stamp" % k)
for k in ["cyber", "ws", "mma"]:
    hrefs = re.findall(r'<div class="srcs">(.*?)</div>', S[k], re.S)
    ck(len(hrefs) == 1, "%s: expected exactly one sources block" % k)
    if hrefs:
        links = re.findall(r'href="([^"]+)"', hrefs[0])
        ck(len(links) == len(set(links)),
           "%s: duplicate source links: %s" % (k, [l for l in links if links.count(l) > 1][:3]))
        ck(len(links) >= 10, "%s: source list too short (%d)" % (k, len(links)))

# ============================================================ disclaimers
has("ws", "not investment advice")
has("cyber", "not a substitute for your own vulnerability management process")
has("mma", "subject to change")

print("validate_1050.py: %d checks, %d failures" % (checks, len(fails)))
for f in fails:
    print("  FAIL:", f)
sys.exit(1 if fails else 0)
