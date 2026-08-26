#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Incremental edits for the 2026-08-26 ~3:12pm ET edition (fourteenth run of the day).
Applied to the 1509 pages. Every inserted fact traces to a source fetched THIS run."""
import re, sys, os

D = sys.argv[1] if len(sys.argv) > 1 else "."
def rd(p):
    with open(os.path.join(D, p), encoding="utf-8") as f: return f.read()
def wr(p, s):
    with open(os.path.join(D, p), "w", encoding="utf-8") as f: f.write(s)

fails = []
def sub_once(s, old, new, label):
    if s.count(old) != 1:
        fails.append("%s: anchor count=%d" % (label, s.count(old)))
        return s
    return s.replace(old, new, 1)

# ---------------------------------------------------------------- demote stale New tags
def demote(s, stamp):
    # replace class + label together so superseded cards stop rendering in the highlight colour
    return s.replace('class="tag new">New &middot; %s' % stamp,
                     'class="tag">Carried &middot; %s' % stamp) \
            .replace('<b>&#9679; New at %s &mdash;' % stamp,
                     '<b>&#9679; Carried from the %s edition &mdash;' % stamp)

# ================================================================ WALL STREET
ws = rd("wallstreet-briefing.html")
ws = demote(ws, "3:05")

NEW_WS_TLDR = ('<div class="tldr"><b>The Tape</b> <span>Nothing on the tape has moved since the 3:00 strip &mdash; the Zacks/Yahoo '
 'page re-fetched at <b>~3:12&nbsp;p.m.</b> returned the <b>same 2:40 trending strip</b> and the <b>same ~12:05 index board</b> it '
 'served an hour ago, so <b>both of that one page&rsquo;s two independent caches are now static</b>, and <b>TheStreet&rsquo;s Aug.&nbsp;26 '
 'page came back with an empty body for a fourth consecutive run</b>; what the re-fetch did buy is verification &mdash; all eight lines of '
 'the 12:05 board reconcile (<b>S&amp;P&nbsp;7,670.01 &minus;0.09%</b>, <b>Dow&nbsp;53,455.18 &minus;0.23%</b>, '
 '<b>Nasdaq&nbsp;26,063.23 &minus;0.34%</b>, Russell one cent out again), and <b>gold&rsquo;s $4,694.50 prior close is confirmed a '
 'further time</b>, while <b>&#9888; Bitcoin&rsquo;s implied base lands at 79,153.30 against the 79,153.29 recorded earlier</b> &mdash; a '
 'penny of drift in a reference that is rolling, not fixed.</span></div>')
ws = re.sub(r'<div class="tldr"><b>The Tape</b>.*?</div>', NEW_WS_TLDR, ws, count=1, flags=re.S)

WS_H2_NEW = ('<h2>Two caches on one page, both frozen &mdash; and a re-fetch that bought verification instead of news</h2>')
ws = sub_once(ws,
 '<h2>Three boards, three clocks, twenty-four clean reconciliations &mdash; and a session that opened green and turned red</h2>',
 WS_H2_NEW, "ws-h2")

WS_LEAD_NEW = ("""<p><b>&#9679; New at 3:12 &mdash; the freshest thing this desk can say about the tape is that it has not changed.</b> The Yahoo syndication of the Zacks Aug.&nbsp;26 recap was re-fetched at <b>~3:12&nbsp;p.m. ET</b>. Its index board still carries the countdown <b>&ldquo;close in 3h 55m&rdquo;</b>, which places it at <b>~12:05&nbsp;p.m. &mdash; now more than three hours stale</b>; its trending-ticker strip still reads <b>ANF $153.40 &plus;$44.50 &plus;40.86%</b>, <b>INTU $339.41 &minus;$18.05 &minus;5.05%</b>, <b>CRE $6.18 &plus;$3.61 &plus;140.47%</b>, <b>XPON $8.86 &plus;$3.59 &plus;68.12%</b> and <b>META $577.46 &plus;$7.41 &plus;1.30%</b> &mdash; <b>byte-for-byte the 2:40 strip this page already carries</b>. Per <b>Gotcha&nbsp;#50</b>, the two widgets are dated independently; this run both of them are frozen, and <b>neither is published as a later reading than what is already on the page</b>. <b>&#9888; TheStreet&rsquo;s Aug.&nbsp;26 page returned an EMPTY body for a fourth consecutive run.</b></p>
<p><b>&#9679; New at 3:12 &mdash; what the stale board is still good for: eight lines, eight reconciliations.</b> A stale board is not a wrong board, and this one was re-verified in Python line by line. <b>S&amp;P&nbsp;500 7,670.01, &minus;7.27, &minus;0.09%</b>; <b>Dow&nbsp;30 53,455.18, &minus;122.22, &minus;0.23%</b>; <b>Nasdaq 26,063.23, &minus;88.07, &minus;0.34%</b> &mdash; the three add back exactly to <b>7,677.28 / 53,577.40 / 26,151.30</b>, the Tuesday closes this desk publishes. <b>VIX 15.45, 0.00, 0.00%</b> sits exactly flat on its own Tuesday close, which is the base every VIX reconciliation on this page uses. <b>Gold $4,655.50, &minus;$39.00, &minus;0.83%</b> implies a <b>$4,694.50</b> prior close &mdash; the figure this desk adopted over the ~$4,637 the Motley Fool strip implied, now confirmed a further time. <b>WTI Oct-26 $82.88, &plus;$0.52, &plus;0.63%</b> implies <b>$82.36</b>, the same barrel base all three earlier boards gave, and puts crude <b>above</b> Tuesday&rsquo;s close at midday after trading below it in the morning. <b>&#9888; Russell&nbsp;2000 3,002.71, &minus;7.32, &minus;0.24% adds back to 3,010.03 against the 3,010.02 close eleven other renderings give</b> &mdash; the same one-cent rounding artefact flagged at 2:44, recurring, and printed rather than smoothed.</p>
<p><b>&#9679; New at 3:12 &mdash; and Bitcoin drifts a penny, exactly as Gotcha&nbsp;#51 predicts.</b> The same board reads <b>BTC $78,100.48, &minus;$1,052.82, &minus;1.33%</b>, implying a base of <b>79,153.30</b>. An earlier board this session implied <b>79,153.29</b> &mdash; one cent apart. <b>That is not evidence either board is wrong.</b> Bitcoin trades continuously, so the &ldquo;previous close&rdquo; a quote feed shows for it is a <b>rolling 24-hour reference</b> that moves under the quote; a fourth base, <b>79,905.81</b>, is implied by the pre-session futures board this page already carries at ~4:25&nbsp;a.m. Every equity, index and commodity line held its base to the cent. Only the crypto reference moved. <b>No claim of staleness is made from it.</b></p>
""")
ws = sub_once(ws, '<div class="lab">The lead</div>', '<div class="lab">The lead</div>', "ws-lead-anchor")
ws = sub_once(ws, WS_H2_NEW, WS_H2_NEW + "\n" + WS_LEAD_NEW, "ws-lead-insert")

WS_CARD = ("""<div class="card"><div class="tags"><span class="tag new">New &middot; 3:12</span><span class="tag">Cache</span><span class="tag">No new number</span></div>
<h3>The 3:12 re-fetch: one page, two caches, both frozen</h3>
<p>Re-fetched at <b>~3:12&nbsp;p.m. ET</b>, the Zacks/Yahoo Aug.&nbsp;26 recap served an index board still self-dating to <b>~12:05&nbsp;p.m.</b> by its own <b>&ldquo;close in 3h 55m&rdquo;</b> countdown, and a trending strip identical to the <b>2:40</b> one this page already publishes. <b>Neither widget is republished here as a later reading.</b> The single-name numbers on that strip &mdash; ANF, INTU, CRE, XPON, META &mdash; are the ones already carried, unchanged.</p>
<p><b>&#9888; No mover on this page is being restated as a 3:12 figure, and no new mover is asserted.</b> The last genuinely later single-name read this desk has is the <b>~3:00&nbsp;p.m.</b> strip carried above. Where a cache does not advance, this page says so rather than re-dressing the same numbers with a newer clock.</p></div>
""")
ws = sub_once(ws, '<div class="lab">Movers &amp; drivers</div>\n<div class="cards">',
              '<div class="lab">Movers &amp; drivers</div>\n<div class="cards">\n' + WS_CARD, "ws-card")
wr("wallstreet-briefing.html", ws)

# ================================================================ CYBER
cy = rd("cyber-briefing.html")
cy = demote(cy, "3:05")

NEW_CY_TLDR = ('<div class="tldr"><b>The Wire</b> <span>Two flaws this page had not carried arrive together &mdash; '
 '<b>SAP Commerce Cloud CVE-2026-58231</b>, a <b>CVSS&nbsp;10.0</b> improper-authorization bug in the <b>Data Hub Adapter</b> that '
 'unauthenticated attackers began probing in honeypots <b>three days after SAP&rsquo;s Aug.&nbsp;11 patch</b> and that <b>CISA has still '
 'not added to KEV</b>, and <b>Microsoft Configuration Manager CVE-2026-47301</b>, <b>CVSS&nbsp;8.8</b>, whose full exploit chain now has '
 '<b>public proof-of-concept code</b> and stays <b>partly unpatched until October</b> &mdash; while the KEV board itself is unchanged for '
 'an <b>eleventh consecutive edition</b> at <b>14 deadlines, 10 past due</b>, with <b>Oracle due tomorrow</b> and <b>Gitea on Friday</b>.'
 '</span></div>')
cy = re.sub(r'<div class="tldr"><b>The Wire</b>.*?</div>', NEW_CY_TLDR, cy, count=1, flags=re.S)

CY_PARAS = ("""<p><b>&#9679; New at 3:12 &mdash; CVE-2026-58231, SAP Commerce Cloud: a maximum-severity flaw, already being probed, and still outside KEV.</b> The vulnerability is an <b>improper authorization</b> issue in the <b>Data Hub Adapter for SAP Commerce Cloud</b>, rated <b>CVSS&nbsp;10.0</b> &mdash; the top of the scale. SAP&rsquo;s description of the mechanism: the product <b>&ldquo;allows an unauthenticated attacker to abuse a default authentication client and submit specially crafted input to certain functions lacking sufficient validation&rdquo;</b>, and successful exploitation <b>&ldquo;could enable arbitrary code execution and compromise internal components, resulting in high impact on confidentiality, integrity, and availability of the application.&rdquo;</b> SAP shipped the fix on <b>August&nbsp;11</b>, as part of an <b>August 2026 Security Patch Day carrying 28 new security notes</b>, one GitHub security advisory and two updates to previously released notes. <b>Exploitation attempts began hitting honeypots on August&nbsp;14 &mdash; three days later</b> &mdash; reported by <b>Defused</b> and independently confirmed by <b>KEVIntel</b>, which runs its own proprietary sensors. <b>There is no public proof-of-concept</b>, which is precisely what makes the timeline notable: with no exploit code circulating, attackers appear to have <b>reverse-engineered the vendor patch on release</b>. <b>&#9888; CISA has NOT added CVE-2026-58231 to the KEV catalog</b>, so <b>no federal deadline attaches to it</b> and it does <b>not</b> appear on the board below &mdash; the KEV catalog lists 14 SAP product flaws, only one of which (the 2019-era CVE-2019-0344) touches Commerce Cloud. <b>&#9888; One source read this run carried a database status line saying the flaw has &ldquo;no public PoC and is not known to be exploited&rdquo;</b>; that is recorded and <b>not</b> merged into the honeypot reporting above, which four outlets state directly. Sources: SecurityWeek, BleepingComputer, The Hacker News, SC Media, SoCRadar, Cybersecurity Dive.</p>
<p><b>&#9679; New at 3:12 &mdash; CVE-2026-47301, Microsoft Configuration Manager (SCCM): public exploit code, and a chain that stays open until October.</b> Researcher <b>Omri Baso</b> has published a proof-of-concept repository &mdash; source, project files, a crafted CAB archive and a compiled release &mdash; for a chain that takes <b>a low-privileged domain user to SYSTEM execution on a Configuration Manager Primary Site Server</b>. The chain combines <b>broken access control, path traversal during CAB extraction, arbitrary file write, a certificate-verification bypass and DLL hijacking</b>. Why it matters operationally: the site server <b>manages the entire estate</b>, so taking it means taking every client it manages. <b>CVSS&nbsp;8.8 (High), CWE-284 Improper Access Control</b>, per the SentinelOne advisory. <b>&#9888; Only part of the chain is fixed.</b> The issues were reported to Microsoft on <b>May&nbsp;23</b>; one high-severity CVE was assigned and fixed by <b>July&nbsp;14</b>, but <b>the remainder of the chain is currently unpatched, with fixes planned for ConfigMgr&nbsp;2609 in October&nbsp;2026</b>. <b>Not in KEV, so no federal deadline.</b> Sources: Cybersecurity News, GBHackers, XM Cyber, the researcher&rsquo;s own Medium write-up and GitHub repository.</p>
""")
anchor = '<p><b>Overnight, one deadline lapsed.</b>'
cy = sub_once(cy, anchor, CY_PARAS + anchor, "cy-paras")

CY_ROWS = ("""<tr><td>CVE-2026-58231 <span class="tag new">New &middot; 3:12</span></td><td>10.0</td><td>Data Hub Adapter for SAP Commerce Cloud (fixed on SAP Security Patch Day, Aug&nbsp;11, 2026)</td><td>Improper authorization &mdash; an <b>unauthenticated</b> attacker with network access can <b>abuse a default authentication client</b> and submit crafted input to functions lacking sufficient validation, enabling <b>arbitrary code execution</b> and compromise of internal components. <b>Exploitation attempts observed in honeypots on Aug&nbsp;14, three days after the patch</b> (Defused; independently confirmed by KEVIntel). <b>No public PoC</b> &mdash; consistent with attackers reverse-engineering the vendor patch. <b>&#9888; NOT in CISA KEV, so no federal deadline.</b> SecurityWeek / BleepingComputer / The Hacker News / SC Media.</td></tr>
<tr><td>CVE-2026-47301 <span class="tag new">New &middot; 3:12</span></td><td>8.8 <span class="muted">(SentinelOne advisory, CWE-284)</span></td><td>Microsoft Configuration Manager (SCCM) &mdash; one CVE fixed Jul&nbsp;14, 2026; <b>rest of the chain unpatched until ConfigMgr 2609, October 2026</b></td><td>Exploit chain from <b>low-privileged domain user to SYSTEM on a Primary Site Server</b>: broken access control &rarr; path traversal during CAB extraction &rarr; arbitrary file write &rarr; certificate-verification bypass &rarr; DLL hijacking. Compromising the site server implies control of every client it manages. <b>Public proof-of-concept code released by researcher Omri Baso</b> (source, project files, crafted CAB, compiled release). Reported to Microsoft May&nbsp;23. <b>Not in KEV, no federal deadline.</b></td></tr>
""")
cy = sub_once(cy, '<tr><td>CVE-2026-19490 <span class="tag">Carried',
              CY_ROWS + '<tr><td>CVE-2026-19490 <span class="tag">Carried', "cy-rows")

CY_KEVNOTE = ('<div class="note" style="margin-bottom:10px"><b>&#9679; New at 3:12 &mdash; still nothing new from CISA, for an eleventh '
 'consecutive edition.</b> Searches this run for KEV additions surfaced <b>no alert page later than the ones already on this board</b>. '
 '<b>&#9888; The two flaws added to this page this run &mdash; SAP CVE-2026-58231 and SCCM CVE-2026-47301 &mdash; are BOTH outside KEV</b>, '
 'so neither appears below and neither changes the count. <b>The board holds at 14 rows, 10 past due, and the Patch Priority deadlines '
 'above are unchanged and match it.</b></div>\n')
cy = sub_once(cy, '<div class="note" style="margin-bottom:10px"><b>&#9679; Carried from the 2:44 edition &mdash; still nothing new from CISA',
              CY_KEVNOTE + '<div class="note" style="margin-bottom:10px"><b>&#9679; Carried from the 2:44 edition &mdash; still nothing new from CISA',
              "cy-kevnote")
wr("cyber-briefing.html", cy)

# ================================================================ MMA
mm = rd("mma-briefing.html")
mm = demote(mm, "3:05")
NEW_MMA_TLDR = ('<div class="tldr"><b>Tale of the Tape</b> <span>Fresh searches this run returned <b>no UFC item this page does not '
 'already carry</b>: the most recent completed event is still <b>UFC Fight Night 285, Hernandez vs. Rodrigues, Aug.&nbsp;22 at the '
 'Golden&nbsp;1 Center in Sacramento</b>, and the next card is still <b>Saturday, Aug.&nbsp;29 at the Oriental Sports Center in '
 'Shanghai&rsquo;s Pudong District</b> &mdash; three days out, with the line on <b>Umar Nurmagomedov vs. Song Yadong</b> read five '
 'different ways and all five published unmerged; the full <b>twelve-bout UFC&nbsp;331 line-up</b> for Sept.&nbsp;19 stands as carried, '
 'and the <b>champions board is unchanged for a twenty-sixth consecutive edition</b>.</span></div>')
mm = re.sub(r'<div class="tldr"><b>Tale of the Tape</b>.*?</div>', NEW_MMA_TLDR, mm, count=1, flags=re.S)
wr("mma-briefing.html", mm)

# ================================================================ INDEX
ix = rd("index.html")
CARDS = {
 "c-sec": ("Two new flaws, both outside KEV",
   '<p>Two flaws this page had not carried arrive together: <b>SAP Commerce Cloud CVE-2026-58231</b> (<b>CVSS&nbsp;10.0</b>, Data Hub '
   'Adapter) drew honeypot exploitation attempts <b>three days after SAP&rsquo;s Aug.&nbsp;11 patch</b> and is <b>still not in KEV</b>; '
   '<b>SCCM CVE-2026-47301</b> (<b>8.8</b>) now has <b>public PoC code</b> and stays partly unpatched until October. The KEV board is '
   'unchanged for an <b>eleventh</b> edition &mdash; <b>14 deadlines, 10 past due</b>, Oracle due tomorrow.</p>'),
 "c-mkt": ("One page, two caches, both frozen",
   '<p>The Zacks/Yahoo recap re-fetched at <b>~3:12&nbsp;p.m.</b> served the <b>same ~12:05 index board</b> and the <b>same 2:40 '
   'trending strip</b> as an hour ago &mdash; both caches static &mdash; and <b>TheStreet came back empty a fourth time</b>. The '
   're-fetch bought verification instead: all eight board lines reconcile, <b>gold&rsquo;s $4,694.50 base is confirmed again</b>, and '
   '<b>&#9888; Bitcoin&rsquo;s implied base drifts a penny</b>, exactly as a rolling reference should.</p>'),
 "c-mma": ("Nothing new &mdash; and the page says so",
   '<p>Fresh searches returned <b>no UFC item not already carried</b>. Last completed event: <b>Fight Night 285, Hernandez vs. '
   'Rodrigues, Aug.&nbsp;22, Sacramento</b>. Next: <b>Saturday, Aug.&nbsp;29, Oriental Sports Center, Shanghai</b> &mdash; three days '
   'out, the line on <b>Umar Nurmagomedov vs. Song Yadong</b> read five ways and all five published unmerged. Champions board unchanged '
   'for a <b>twenty-sixth</b> consecutive edition.</p>'),
}
for cls, (h2, para) in CARDS.items():
    m = re.search(r'(<a class="bcard %s"[^>]*>)(.*?)(</a>)' % cls, ix, flags=re.S)
    if not m:
        fails.append("index %s: card not found" % cls); continue
    body = m.group(2)
    b2, n = re.subn(r'<h2>.*?</h2>', '<h2>%s</h2>' % h2, body, count=1, flags=re.S)
    if n != 1: fails.append("index %s: h2 not replaced" % cls); continue
    b3, n = re.subn(r'<p>.*?</p>', para, b2, count=1, flags=re.S)
    if n != 1: fails.append("index %s: p not replaced" % cls); continue
    ix = ix[:m.start()] + m.group(1) + b3 + m.group(3) + ix[m.end():]
wr("index.html", ix)

print("FAILS:" , fails if fails else "none")
