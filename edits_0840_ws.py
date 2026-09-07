#!/usr/bin/env python3
"""Wall Street edits, 2026-09-07 ~08:45 ET (Morning Edition, SECOND run, LABOR DAY).

Driver: equities and Treasuries are shut, but the oil market is open and it moved.
Trading Economics was fetched directly this run and it (a) resolves the Brent refusal
this page has carried for several editions and (b) carries the weekend escalation.
"""
import re, sys, io

P = 'wallstreet-briefing.html'
h = io.open(P, encoding='utf-8').read()
orig = h
n = 0

def sub(old, new, label):
    global h, n
    if h.count(old) != 1:
        sys.exit('MISS(%d): %s' % (h.count(old), label))
    h = h.replace(old, new, 1)
    n += 1
    print('  ok:', label)

# ------------------------------------------------------------------ 1. TLDR
old = ('U.S. stock and bond markets are shut all day for Labor Day and reopen Tuesday, '
       'leaving Friday&rsquo;s lower close as the last word:')
new = ('U.S. stock and bond markets are shut all day for Labor Day, but the oil market is '
       'open and it is where the news is &mdash; Brent has run to a six-week high after the '
       'U.S. and Iran spent the weekend striking each other&rsquo;s tankers &mdash; while on '
       'equities Friday&rsquo;s lower close remains the last word:')
print('  skip: applied')

# ------------------------------------------------------------------ 2. THE LEAD headline
old = ('Labor Day: no session today, and four days to wait for the number that decides the Fed')
new = ('Labor Day: the stock market is shut, the oil market is not &mdash; and Brent is at a '
       'six-week high')
print('  skip: applied')

# ------------------------------------------------------------------ 3. LEAD opening
old = ('The NYSE reopens at normal hours, <b>9:30 AM ET on Tuesday 8 September</b>. '
       'Everything below reflects Friday 4 September, the most recent completed session.')
new = ('The NYSE reopens at normal hours, <b>9:30 AM ET on Tuesday 8 September</b>. '
       'Everything below on <i>equities</i> reflects Friday 4 September, the most recent '
       'completed session. <b>Crude is the exception, and it is the reason this page leads '
       'somewhere different than it did at 8:19 this morning.</b> Oil trades while the NYSE '
       'is dark, and over the weekend the U.S.&ndash;Iran confrontation moved from missiles '
       'to tankers: <b>Brent has run to a six-week high</b>, its highest since July 2026 and '
       '&mdash; per Trading Economics, fetched directly this run &mdash; nearly <b>40% above '
       'levels from before the outbreak of the war in Iran</b>. The escalation, the numbers '
       'and what is holding the move back are set out under Rates, Bonds &amp; Commodities; '
       'the equities story below is unchanged because there was no session in which to change '
       'it.')
sub(old, new, 'lead opening: oil exception')

# ------------------------------------------------------------------ 4. resolve the Brent refusal in On the Radar
old = ('<span class="mut">No Friday settle is asserted &mdash; sources fetched on 6 September '
       'put the level anywhere between roughly $95 and $96.28, and the conflict is set out '
       'under Rates, Bonds &amp; Commodities below.</span>')
new = ('<span class="mut">That refusal is <b>partly resolved this run</b>: Trading Economics&rsquo; '
       'own Brent series, fetched directly this morning, carries a <b>Previous</b> value of '
       '<b>$96.28</b> against Monday&rsquo;s print &mdash; and with Saturday and Sunday absent from '
       'the series, the value before a Monday quote is Friday&rsquo;s. That is the same $96.28 CNBC '
       'reported as the Friday settle, from an unrelated source. Two independent routes to one '
       'number is corroboration, so <b>$96.28 is now printed for Friday</b> &mdash; still attributed, '
       'still not called an official settle, because a CFD series and a settlement price are not the '
       'same object. The lower &ldquo;near $95&rdquo; returns are superseded rather than reconciled.</span>')
sub(old, new, 'Brent Friday refusal resolved')

# ------------------------------------------------------------------ 5. Brent table row
old = ('<tr><td>Brent crude</td><td><b>Not asserted</b></td><td class="mut">Sources disagree on '
       'the level. A CNBC report carried a Friday settle of <b>$96.28</b>; returns fetched on '
       '6 September put Brent <b>&ldquo;near $95&rdquo; on Friday</b> and at <b>$95.26 on 3 '
       'September</b>. A settle is a single number, so the conflict is printed and no level is '
       'published. The direction &mdash; sharply higher on the week on renewed U.S.&ndash;Iran '
       'hostilities &mdash; is not in dispute.</td></tr>')
new = ('<tr><td>Brent crude</td><td><b class="up">~$97 &middot; six-week high</b></td>'
       '<td class="mut"><b>Live, and the one row on this page that is not a Friday number.</b> '
       'Trading Economics, fetched directly at ~8:45 AM ET Monday 7 September, shows Brent '
       '<b>up about 1.1&ndash;1.2% on the day</b> at a <b>six-week high &mdash; its highest since '
       'July 2026</b>, roughly <b>+11% on the month</b> and <b>+47% on the year</b>. A single '
       'level is deliberately not asserted: the same page rendered <b>97.05</b>, <b>97.38</b> and '
       '<b>97.45</b> in three places within one fetch, which is what a live CFD quote looks like '
       'mid-session, not a discrepancy between sources. The week behind it is unambiguous &mdash; '
       'Brent <b>surged 9.3% last week</b>. Friday&rsquo;s value, now corroborated twice, was '
       '<b>$96.28</b>.</td></tr>')
sub(old, new, 'Brent row: live six-week high')

# ------------------------------------------------------------------ 6. WTI row prefix
old = '<tr><td>WTI crude</td><td><b>~$91</b></td><td class="mut">Traded near $91 on Friday.'
new = ('<tr><td>WTI crude</td><td><b class="up">~$92 &middot; 3-month high</b></td>'
       '<td class="mut"><b>Also live and also higher.</b> Trading Economics, same direct fetch '
       'this morning, puts WTI at <b>92.34</b>, <b>+0.94% on the day</b>, <b>+12.4% on the month</b> '
       'and <b>+48.3% on the year</b>, under its own headline <b>&ldquo;Crude Oil Tests 3-Month '
       'Highs.&rdquo;</b> The Friday history below is retained for continuity and is unchanged. '
       'Traded near $91 on Friday.')
sub(old, new, 'WTI row: live 3-month high')

# ------------------------------------------------------------------ 7. weekend escalation block
anchor = '<h2 class="sec">On the Radar</h2>'
if anchor not in h:
    anchor = '<h2>On the Radar</h2>'
if anchor not in h:
    sys.exit('MISS: radar anchor')
block = (
 '<div class="panel" style="margin:14px 0;border-left:3px solid var(--accent)">'
 '<p><b>The weekend, in the order it happened &mdash; and this is new since the 8:19 edition.</b> '
 'Iran&rsquo;s Revolutionary Guard fired ballistic missiles toward a U.S. aircraft carrier and a '
 'destroyer operating near the Strait of Hormuz. The U.S. struck <b>three Iranian oil tankers</b> in '
 'retaliation: CENTCOM-attributed reporting says the crude carriers <b>M/T Downy</b>, off Kharg '
 'Island, and <b>M/T Stark&nbsp;1</b>, near Jask, were &ldquo;permanently disabled,&rdquo; while an '
 'unladen tanker, the <b>M/T Kylo</b>, was &ldquo;completely destroyed&rdquo; after being hit '
 'repeatedly. Iran&rsquo;s Revolutionary Guards then said they had attacked <b>three oil tankers and '
 'three U.S.-linked vessels</b> in the strait on Saturday evening &mdash; a claim Trading Economics '
 'notes <b>could not be independently confirmed</b>, and this desk does not confirm it either. '
 'Tehran has threatened a <b>new restricted maritime zone outside the strait</b>, reportedly running '
 'from the U.S. Navy blockade line into parts of the Persian Gulf. Energy Secretary <b>Chris Wright</b> '
 'says Washington will maintain its naval presence and the blockade, aimed at limiting Iranian exports '
 'while allowing commercial traffic through. Against all of that, Iran says it is <b>close to agreeing '
 'a tanker route through Hormuz with Oman</b> &mdash; the one de-escalatory thread in the day.</p>'
 '<p class="mut"><b>Why crude has not gone higher than it has.</b> Trading Economics attributes the '
 'ceiling to inventory being drawn down rather than to any easing of risk: the <b>U.S. Strategic '
 'Petroleum Reserve has fallen below 290 million barrels, its lowest since 1982</b>, and China has '
 'cut crude imports, with refinery runs down <b>1.6 million barrels per day</b> even as demand for '
 'refined product holds. Two side-effects visible in the same fetch, printed as direction only because '
 'no level here is corroborated: Trading Economics headlines <b>gold slipping</b> and <b>silver '
 'falling</b> on <i>strengthening Fed rate-hike bets</i> &mdash; the same hike trade the equities '
 'section below describes, showing up in metals on a day when the stock market cannot price it.</p>'
 '<p class="mut"><b>Not asserted:</b> no Treasury yield level is published today &mdash; the bond '
 'market is closed for the holiday, so a quote would not be a market. No stock-index level is taken '
 'from the live CFD quotes now visible on data pages; the official Friday closes in the Weekly '
 'Scorecard stand.</p>'
 '</div>\n')
h = h.replace(anchor, block + anchor, 1)
n += 1
print('  ok: weekend escalation block')

# ------------------------------------------------------------------ 8. sources
old = 'Sources</h2><div class="panel srcs">'
new = ('Sources</h2><div class="panel srcs">'
       '<a href="https://tradingeconomics.com/commodity/brent-crude-oil">Trading Economics &mdash; '
       'Brent crude, price/stats/news stream (7 Sep) &mdash; fetched directly this run</a>'
       ' &nbsp;&middot;&nbsp; '
       '<a href="https://www.cnn.com/2026/09/05/middleeast/iran-us-tanker-kharg-intl">CNN &mdash; '
       'U.S. strikes three Iranian tankers</a> &nbsp;&middot;&nbsp; '
       '<a href="https://www.aljazeera.com/news/2026/9/6/us-iran-engaged-in-tanker-war-where-is-the-months-long-conflict-headed">'
       'Al Jazeera &mdash; U.S. and Iran engaged in tanker war (6 Sep)</a> &nbsp;&middot;&nbsp; ')
sub(old, new, 'sources footer')

io.open(P, 'w', encoding='utf-8').write(h)
print('wallstreet: %d edits, %d -> %d bytes' % (n, len(orig), len(h)))
