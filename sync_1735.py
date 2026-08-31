#!/usr/bin/env python3
"""Sync summary strips, index cards, masthead stamps and source footers to the 5:35 PM run."""
import re, sys, io, os
REPO = sys.argv[1]
NOW = "5:35 PM"
rd = lambda f: io.open(os.path.join(REPO, f), encoding="utf-8").read()
wr = lambda f, s: io.open(os.path.join(REPO, f), "w", encoding="utf-8").write(s)

def stamp(s):
    return re.sub(r'(id="updated"[^>]*>)[^<]*(<)', r'\g<1>%s ET\g<2>' % NOW, s, count=1)

L = lambda u, t: '<a href="%s" target="_blank" rel="noopener">%s</a>' % (u, t)

def prepend_sources(s, links):
    """Insert a fresh 'Sources checked this run' block at the head of the footer."""
    anchor = '<footer><p><b>Sources checked this run &mdash; '
    i = s.find(anchor)
    assert i >= 0
    blk = ('<footer><p><b>Sources checked this run &mdash; %s:</b><br>%s</p><p><b>' % (
        NOW, '<br>'.join(links)))
    return s[:i] + blk + s[i + len('<footer><p><b>'):]

# ---------------------------------------------------------------- WALL STREET
ws = rd("wallstreet-briefing.html")
ws = stamp(ws)
new_ws = ('<div class="tldr"><b>The Tape</b> <span>The session closed lower and reconciled to the point '
 '&mdash; <b>S&amp;P 500 7,686.14 (&minus;0.33%)</b>, <b>Nasdaq Composite 26,370.89 (&minus;0.12%)</b>, '
 '<b>Dow 53,185.90 (&minus;374.09, &minus;0.70%)</b> after U.S. and Iranian forces exchanged fire for '
 'the first time in about a month &mdash; and yet all three <b>closed out August with a monthly gain</b>; '
 'the after-bell story is that the <b>10-year topped 4.75%, its highest since January 2025, as rising '
 'oil bolstered expectations the Fed will <i>hike</i></b>.</span></div>')
ws = re.sub(r'<div class="tldr"><b>The Tape</b>.*?</div>', new_ws, ws, count=1, flags=re.S)
ws = prepend_sources(ws, [
  L("https://www.cnbc.com/2026/08/30/stock-market-today-live-updates.html",
    "CNBC &mdash; Stock market news for Aug. 31, 2026 (official close; U.S. and Iran trade fire)"),
  L("https://finance.yahoo.com/markets/live/stock-market-today-monday-august-31-dow-sp-500-nasdaq-113851714.html",
    "Yahoo Finance &mdash; Dow, S&amp;P 500, Nasdaq slip but cap winning month (Aug 31)"),
  L("https://www.thestreet.com/stock-market-today/stock-market-today-dow-jones-sp-500-nasdaq-updates-aug-31-2026",
    "TheStreet &mdash; Stock Market Today, Aug. 31, 2026 (energy leads)"),
  L("https://www.bloomberg.com/news/articles/2026-08-31/treasury-10-year-yield-tops-4-75-highest-since-january-2025",
    "Bloomberg &mdash; Treasury 10-year yield tops 4.75%, highest since January 2025 (oil lifts hike expectations)"),
  L("https://tradingeconomics.com/united-states/government-bond-yield",
    "Trading Economics &mdash; US 10-year note yield, Aug 31 mark (4.72%)"),
  L("https://stockanalysis.com/markets/afterhours/",
    "Stock Analysis &mdash; after-hours movers screen (AEHL, COOT, YDDL, NCRA / ZTEK, JUNS, FNGR, MENS)"),
])
wr("wallstreet-briefing.html", ws)

# ---------------------------------------------------------------------- CYBER
cy = rd("cyber-briefing.html")
cy = stamp(cy)
new_cy = ('<div class="tldr"><b>The Wire</b> <span>The <b>PaperCut NG/MF</b> chain now has an order as well '
 'as a deadline: <b>CVE-2026-81578</b> is an <b>authentication bypass that lets an unauthenticated '
 'attacker change system configuration</b>, and <b>CVE-2026-82078</b> turns that changed configuration '
 'into <b>arbitrary Java bytecode running as the PaperCut server process</b> &mdash; both were added to '
 'CISA&rsquo;s Known Exploited Vulnerabilities catalog on <b>August 31 with a September 14 remediation '
 'date</b>, and with the first emergency patch already bypassed, patching once is not enough.</span></div>')
cy = re.sub(r'<div class="tldr"><b>The Wire</b>.*?</div>', new_cy, cy, count=1, flags=re.S)
cy = prepend_sources(cy, [
  L("https://cybersecuritynews.com/papercut-ng-mf-vulnerabilities-exploited/",
    "Cyber Security News &mdash; CISA warns of PaperCut NG/MF flaws actively exploited (chain order; Sept 14 deadline)"),
  L("https://www.cisa.gov/known-exploited-vulnerabilities-catalog",
    "CISA &mdash; Known Exploited Vulnerabilities Catalog"),
  L("https://www.cisa.gov/news-events/alerts/2026/08/18/cisa-adds-four-known-exploited-vulnerabilities-catalog",
    "CISA &mdash; Adds Four Known Exploited Vulnerabilities to Catalog (Aug 18: IKE, SharePoint, vCenter, macOS)"),
  L("https://thehackernews.com/2026/08/critical-macos-sharepoint-vcenter-and.html",
    "The Hacker News &mdash; Critical macOS, SharePoint, vCenter and Microsoft IKE flaws under active exploitation"),
  L("https://www.securityweek.com/more-details-emerge-on-exploited-papercut-vulnerabilities/",
    "SecurityWeek &mdash; More details emerge on exploited PaperCut vulnerabilities"),
  L("https://cybernews.com/security/",
    "Cybernews &mdash; security desk (Philippines 13M-record leak; UnicaSpa.it; Aurora operators using Cursor across ten targets)"),
])
wr("cyber-briefing.html", cy)

# ------------------------------------------------------------------------ MMA
mm = rd("mma-briefing.html")
mm = stamp(mm)
new_mm = ('<div class="tldr"><b>Tale of the Tape</b> <span>Paris now has a market rather than a single '
 'price &mdash; <b>Hooker +430 / Parnasse &minus;600</b> plus five undercard lines '
 '(<b>Ziam &minus;160</b>, <b>Page &minus;170</b>, <b>Keita &minus;340</b>, <b>Lima &minus;200</b>, '
 '<b>Donchenko &minus;220</b>) &mdash; and four of those five sit inside &minus;220, which makes the '
 'main-event number look like a judgement about one debutant rather than a general market lean; the '
 'champions board is unchanged for a seventy-ninth straight edition.</span></div>')
mm = re.sub(r'<div class="tldr"><b>Tale of the Tape</b>.*?</div>', new_mm, mm, count=1, flags=re.S)
mm = prepend_sources(mm, [
  L("https://www.ufc.com/event/ufc-fight-night-september-05-2026",
    "UFC.com &mdash; UFC Fight Night: Hooker vs Parnasse, Sept 5, Accor Arena, Paris"),
  L("https://www.ufcalendar.com/events/ufc-fight-night-2026-09-05",
    "UFCalendar &mdash; Hooker vs Parnasse fight card and odds (main-card lines; 13 fights)"),
  L("https://www.mmaoddsbreaker.com/fight-odds/opening-odds/161246-opening-betting-odds-for-ufc-paris-hooker-vs-parnasse/",
    "MMA Odds Breaker &mdash; opening betting odds for UFC Paris"),
  L("https://www.tapology.com/fightcenter/events/144513-ufc-fight-night",
    "Tapology &mdash; UFC Fight Night: Hooker vs. Parnasse"),
  L("https://en.wikipedia.org/wiki/2026_in_UFC",
    "Wikipedia &mdash; 2026 in UFC (event schedule)"),
  L("https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions",
    "ESPN &mdash; Current and all-time UFC champions"),
])
wr("mma-briefing.html", mm)

# ---------------------------------------------------------------------- INDEX
ix = rd("index.html")
ix = stamp(ix)
cards = {
 "c-cy": ('<p><b>The PaperCut chain now has an order, not just a deadline.</b> An attacker uses '
   '<b>CVE-2026-81578</b> first &mdash; an <b>authentication bypass that changes system configuration '
   'with no credentials</b> &mdash; then <b>CVE-2026-82078</b> (<b>CVSS 9.4</b>, unsafe dynamic class '
   'loading) to run <b>arbitrary Java bytecode as the PaperCut server process</b>. Both entered CISA&rsquo;s '
   'KEV catalog on <b>August 31</b>, remediation due <b>September 14</b>; the first emergency patch was '
   'already bypassed. Also new: a leak of <b>13M+ Philippine records</b>, a breach at Italian energy '
   'retailer <b>UnicaSpa.it</b>, and <b>Aurora ransomware operators using the Cursor AI assistant across '
   'ten targets</b>.</p>'),
 "c-ws": ('<p><b>A lower close that still capped a winning month.</b> <b>S&amp;P 500 7,686.14 '
   '(&minus;0.33%)</b>, <b>Nasdaq Composite 26,370.89 (&minus;0.12%)</b>, <b>Dow 53,185.90, down 374.09 '
   'points (&minus;0.70%)</b> after <b>U.S. and Iranian forces exchanged fire for the first time in about '
   'a month</b> &mdash; yet all three <b>finished August higher</b>. The <b>10-year topped 4.75%, its '
   'highest since January 2025, as rising oil bolstered expectations the Fed will hike</b>; '
   '<b>WTI settled +2.83% at $85.76</b>, <b>Brent +2.71% at $90.49</b>, and <b>energy was the only sector '
   'to finish up</b>.</p>'),
 "c-mm": ('<p><b>Paris finally has a market instead of a single price.</b> <b>Hooker +430 / Parnasse '
   '&minus;600</b> in the main event, with five undercard lines fetched alongside it &mdash; '
   '<b>Sola +135 / Ziam &minus;160</b>, <b>Page &minus;170 / Ruziboev +143</b>, <b>Keita &minus;340 / '
   'Naimov +270</b>, <b>Charri&egrave;re +170 / Lima &minus;200</b>, <b>Donchenko &minus;220 / Soriano '
   '+180</b>. Four of the five sit inside &minus;220, which makes the main-event number a judgement about '
   'one debutant rather than a market lean. The <b>champions board is unchanged</b>.</p>'),
}
for cid, body in cards.items():
    # cards are <a|div class="bigcard c-xx"> ... first <p>...</p> is the summary
    j = ix.find('bigcard %s' % cid)
    if j < 0:
        j = ix.find('%s ' % cid, ix.find('</style>'))
    assert j > 0, cid
    a = ix.find('<p>', j); b = ix.find('</p>', a) + 4
    assert a > 0 and b > a, cid
    ix = ix[:a] + body + ix[b:]
ix = re.sub(r'(<b>Sources checked this run &mdash; )[^:<]*(:</b>)', r'\g<1>%s ET\g<2>' % NOW, ix, count=1)
wr("index.html", ix)
print("sync_1735 OK")
