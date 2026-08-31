#!/usr/bin/env python3
"""Targeted edits onto the 5:05 PM pages -> 5:35 PM Afternoon Edition (post-close).
Every inserted fact was fetched THIS run (2026-08-31 ~17:35-17:45 ET)."""
import re, sys, io, os

REPO = sys.argv[1]
NOW = "5:35 PM"

rd = lambda f: io.open(os.path.join(REPO, f), encoding="utf-8").read()
wr = lambda f, s: io.open(os.path.join(REPO, f), "w", encoding="utf-8").write(s)

def demote(s, stamp="5:05 PM"):
    """Sweep on the MARKER TEXT, never on the tag variant (defect class logged 4:55)."""
    pat = re.compile(r'<span class="tag[^"]*">New &middot; ' + re.escape(stamp) + r'</span>')
    return pat.sub('<span class="tag">Carried &middot; Aug 31, ' + stamp + '</span>', s)

def restamp(s):
    return s.replace("Data as of 5:05 PM ET", "Data as of %s ET" % NOW)

NEW = lambda: '<span class="tag new">New &middot; %s</span>' % NOW

# ================================================================ WALL STREET
ws = rd("wallstreet-briefing.html")
ws = demote(ws); ws = restamp(ws)

# 1) After-Hours: the screen came BACK to the 4:55 set. That is the finding.
ah = 'After-Hours Movers</h2>'
assert ah in ws
blk = (ah + '<div class="note" style="margin-bottom:14px">' + NEW() +
  ' <b>The screen turned over once and then turned straight back, and the return trip is the more '
  'useful of the two observations.</b> An after-hours movers screen fetched this run lists '
  '<b>Antelope Enterprise Holdings (AEHL) +84.75% at $6.54</b>, <b>Australian Oilseeds Holdings '
  '(COOT) +58.50% at $0.73</b>, <b>One and One Green Technologies (YDDL) +41.82% at $2.34</b> and '
  '<b>Nocera (NCRA) +38.62% at $2.62</b> among gainers, and <b>Zentek (ZTEK) &minus;32.04% at $0.37</b>, '
  '<b>Jupiter Neurosciences (JUNS) &minus;26.79% at $3.06</b>, <b>FingerMotion (FNGR) &minus;19.07% at '
  '$0.32</b> and <b>Jyong Biotech (MENS) &minus;17.72% at $1.95</b> among losers. '
  '&#9888; <b>Six of those eight percentages match the 4:55 PM screen to the hundredth of a point</b> '
  '&mdash; AEHL, COOT, YDDL, ZTEK, JUNS and FNGR are identical, and <b>NCRA and MENS are simply two '
  'names further down the same list</b>. <b>The 5:05 PM screen, which returned WETO and CANG as gainers '
  'and named no percentages at all, shares no gainer with either.</b><br><br>'
  '&#9888; <b>The conclusion this page draws is about the instrument, not the market.</b> Three '
  'after-hours screens inside forty minutes produced two identical readings separated by a third that '
  'agrees with neither, which means <b>a screener return is not reliably a timestamp</b>: an intervening '
  'read that disagrees does not supersede the ones on either side of it, and matching percentages across '
  'a half-hour are evidence of a cached list rather than of a market that stood still. '
  '<b>Nothing here is upgraded to news.</b> No catalyst is attached to any of the eight in anything '
  'fetched, all are microcaps, and <b>no S&amp;P 500 company has a sourced post-close move this run '
  'either</b>. The next after-the-bell event of size remains <b>Broadcom&rsquo;s third-quarter fiscal '
  '2026 report on Wednesday, September 2</b>.</div>')
ws = ws.replace(ah, blk, 1)

# 2) Rates: Bloomberg's CAUSAL clause, new this run.
rb = 'Rates, Bonds'
i = ws.find(rb)
h2 = ws.find('</h2>', i) + 5
rate_note = ('<div class="note" style="margin-bottom:14px">' + NEW() +
  ' <b>The yield story acquires a cause this run, and the cause runs through the oil price rather than '
  'through the Fed.</b> The reporting behind the <b>10-year topping 4.75%, its highest since January '
  '2025</b>, states that it did so <b>as rising oil prices bolstered expectations that the Federal '
  'Reserve will <i>hike</i> rates</b> &mdash; not cut them. &#9888; <b>That is the same chain this '
  'page&rsquo;s lead already describes, read from the other end</b>: the strike in the Strait of Hormuz '
  'lifted crude, crude lifted the inflation path, and the inflation path lifted the long end. '
  '<b>A separate rates read marks the 10-year at 4.72% for August 31</b>; that is a daily mark against '
  'an intraday high and the two are <b>one path, not two claims</b>. '
  '&#9888; <b>No policy expectation is quantified here</b> &mdash; nothing fetched this run put a '
  'probability, a meeting or a size on a hike, and none is invented.</div>')
ws = ws[:h2] + rate_note + ws[h2:]

wr("wallstreet-briefing.html", ws)

# ====================================================================== CYBER
cy = rd("cyber-briefing.html")
cy = demote(cy); cy = restamp(cy)

# 1) Top story: the chain ORDER, stated explicitly for the first time.
ts = 'Top Story</h2>'
assert ts in cy
blk = (ts + '<div class="note lead" style="margin-bottom:14px">' + NEW() +
  ' <b>The PaperCut pair is confirmed a third time, and this run is the first to state which order the '
  'two flaws are used in.</b> Per a fresh read of the catalog entry, an attacker exploits '
  '<b>CVE-2026-81578 first</b> &mdash; described here as an <b>authentication bypass that lets an '
  'unauthenticated remote attacker modify certain system configuration settings without ever supplying '
  'credentials</b> &mdash; and then uses <b>CVE-2026-82078</b>, <b>unsafe dynamic class loading in the '
  'database connector</b>, to turn those manipulated configuration parameters into <b>execution of '
  'arbitrary Java bytecode already on the application classpath, under the security context of the '
  'PaperCut server process</b>. <b>CISA&rsquo;s remediation deadline for federal civilian agencies is '
  'restated as September 14, 2026</b>, matching the Patch Priority box and the KEV row below.<br><br>'
  '&#9888; <b>Why the order is worth a paragraph.</b> Read separately, one flaw changes a setting and '
  'the other loads a class &mdash; neither sounds like a takeover. <b>Read in sequence, the first '
  'supplies the input the second trusts</b>, and the pair becomes pre-authentication remote code '
  'execution on a print server that by design sits between every desktop and every device on the '
  'network. <b>The bytecode is already on the classpath; nothing has to be uploaded</b>, which is why '
  'controls that watch for dropped files see nothing until the remote-access tooling arrives '
  'afterwards.</div>')
cy = cy.replace(ts, blk, 1)

# 2) Breaches: two new incidents + the Aurora count.
br = 'Breaches &amp; Incidents</h2>'
assert br in cy
blk = (br + '<div class="note" style="margin-bottom:14px">' + NEW() +
  ' <b>Two incidents enter the page this run and one carried item finally acquires a number.</b> '
  '<b>A data leak has exposed more than 13 million records covering customers, citizens and businesses '
  'in the Philippines</b>; separately, <b>a breach at UnicaSpa.it, an Italian energy retailer, involved '
  'customer and operational data</b>. &#9888; <b>Neither has an actor, an intrusion method or a '
  'disclosure date in anything fetched this run, and none is supplied here</b> &mdash; the volume and '
  'the sectors are what the sources state and the rest is left blank rather than filled in.<br><br>'
  '<b>The Aurora ransomware finding is now scoped: the operators have been observed using the AI coding '
  'assistant Cursor in attacks against ten targets.</b> &#9888; <b>The ownership descriptor attached to '
  'Cursor in the same sentence &mdash; naming a spacecraft manufacturer as its publisher &mdash; is '
  'refused for the third edition running</b>: nothing fetched establishes who publishes the tool, and a '
  'wrong descriptor would discredit the sentence it sits in. <b>The count, the actor and the tool are '
  'published; the publisher is not.</b> Ten is also small enough to be worth saying plainly: this is a '
  'technique observation, not a campaign at scale.</div>')
cy = cy.replace(br, blk, 1)

# 3) Vulnerability Watch: the Aug 18 KEV four are dated, and three carry 9.8.
vw = 'Vulnerability Watch</h2>'
assert vw in cy
blk = (vw + '<div class="note" style="margin-bottom:14px">' + NEW() +
  ' <b>The four flaws this page has carried since mid-month now have a confirmed catalog date and a '
  'severity distribution.</b> <b>CVE-2026-33824</b> (double free, Microsoft IKE Service Extensions), '
  '<b>CVE-2026-55040</b> (weak authentication, Microsoft SharePoint), <b>CVE-2026-59310</b> (path '
  'traversal, Broadcom VMware vCenter) and <b>CVE-2026-65400</b> (improper authentication, Apple macOS) '
  'were <b>added to the KEV catalog on August 18, 2026</b>, and <b>three of the four carry a critical '
  '9.8</b> &mdash; <b>Windows IKE, VMware vCenter and macOS</b>. &#9888; <b>The report does not say '
  'which one is the exception, so this page does not assign the fourth a score.</b><br><br>'
  '<b>The exploitation notes differ by product and are worth keeping apart</b>: the <b>macOS</b> flaw '
  'has been abused to deliver a <b>Monero cryptocurrency miner</b>; the <b>SharePoint</b> flaw was '
  'exploited by unknown actors <b>after proof-of-concept code was released</b>; and the <b>vCenter</b> '
  'flaw is assessed to have been used by a <b>suspected China-nexus APT actor to deploy backdoors</b>. '
  '&#9888; <b>Three different classes of adversary reached three different products through the same '
  'catalog entry batch</b>, which is the argument against triaging a KEV list by CVSS alone: the '
  'coinminer and the espionage backdoor arrived on comparable scores.</div>')
cy = cy.replace(vw, blk, 1)

wr("cyber-briefing.html", cy)

# ======================================================================== MMA
mm = rd("mma-briefing.html")
mm = demote(mm); mm = restamp(mm)

fw = None
for cand in ['Fight Week &mdash; Upcoming Cards</h2>', 'Fight Week</h2>']:
    if cand in mm:
        fw = cand; break
if fw is None:
    m = re.search(r'<h2 class="sec">Fight Week[^<]*</h2>', mm)
    fw = m.group(0)
blk = (fw + '<div class="note lead" style="margin-bottom:14px">' + NEW() +
  ' <b>Paris stops being a main event with a price and becomes a card with a market.</b> A read fetched '
  'this run prices six main-card bouts at once: <b>Hooker +430 / Parnasse &minus;600</b>; '
  '<b>Axel Sola +135 / Fares Ziam &minus;160</b>; <b>Michael Page &minus;170 / Nursulton Ruziboev '
  '+143</b>; <b>Losene Keita &minus;340 / Muhammad Naimov +270</b>; <b>Morgan Charri&egrave;re +170 / '
  'Felipe Lima &minus;200</b>; <b>Daniil Donchenko &minus;220 / Punahele Soriano +180</b>. '
  '<b>Every one of those six bouts was already on this page by name; not one of them had a price until '
  'now.</b><br><br>'
  '&#9888; <b>Two discrepancies are recorded rather than resolved.</b> First, this source calls the card '
  '<b>13 fights</b>, where the reporting this page carried at 5:05 PM called it <b>15</b>; '
  '<b>both renderings stand and neither is adopted as the count</b>, because nothing fetched reconciles '
  'them and a fight card can lose bouts without anyone announcing it to a search index. Second, it '
  'describes the opener as <b>Parnasse around &minus;400, Hooker +300</b>, while this page has carried '
  '<b>&minus;357 / +275</b> as the opener and <b>&minus;400 / +300</b> as a later price &mdash; '
  '<b>so the same pair of numbers is the first price in one account and a mid-drift price in another.</b> '
  '<b>The drift itself is not in dispute</b>: every price fetched across every edition moves in one '
  'direction, toward the debutant, and <b>&minus;600 / +430 remains the widest consensus-side number '
  'this page has seen.</b><br><br>'
  '<b>What the undercard prices add is a check on the headline read.</b> Four of the five non-main bouts '
  'are priced inside &minus;220, which is a card of close fights with <b>one lopsided line '
  '(Keita &minus;340)</b> and <b>one that is nearly twice as lopsided as that in the main event</b> '
  '&mdash; a shape that makes the Parnasse number look less like a general market lean and more like a '
  'judgement about one fighter.</div>')
mm = mm.replace(fw, blk, 1)

wr("mma-briefing.html", mm)
print("edits_1735 OK")
