# -*- coding: utf-8 -*-
import sys
O='/sessions/gracious-zealous-maxwell/mnt/outputs/'
s=open(O+'index.html',encoding='utf-8').read()
def sub1(s,a,b,label):
    if a not in s: print('!! MISS',label); sys.exit(1)
    return s.replace(a,b,1)

# --- SECURITY CARD ---
s=sub1(s,'<h3>A VMware guest can now break out to the host, and a federal advisory puts Medusa past 500 victims &mdash; but a print server still owns the only live deadline</h3>',
 '<h3>A 9.8 in a home router joins the watch list with half its details missing &mdash; and the briefing prints which half &mdash; while a print server still owns the only live deadline</h3>','sec h3')
s=sub1(s,'<b>Two items are new at 5:38&nbsp;PM.</b>',
 '<b>One item is new at 6:05&nbsp;PM, and it is the smallest entry on the page:</b> a round-up dated <b>7 September</b> puts <b>CVE-2026-51693</b> at <b>CVSS 9.8</b> in the <b>TOTOLINK T6</b> router. '
 'It goes onto the watch list with <b>no vulnerability class, no affected build and no fixed version</b> &mdash; the summary gives none and no vendor advisory was fetched &mdash; so an owner cannot yet check a box against it, '
 'and the briefing says so instead of implying otherwise. It is <b>not</b> among the ten CVEs the same round-up calls actively exploited, and it carries <b>no deadline</b>. '
 '<b>The two items new at 5:38&nbsp;PM are carried.</b>','sec new')

# --- MARKETS CARD ---
s=sub1(s,'<h3>Wall Street never opened &mdash; and the last equity-index prints anyone quoted came on Sunday evening, mixed and thin</h3>',
 '<h3>The countdown this desk has run since lunchtime hit zero: futures reopened at 6:00&nbsp;PM ET, minutes before this edition, and nobody here has read the new tape yet</h3>','mkt h3')
s=sub1(s,'<b>One item is new at 5:38&nbsp;PM, and it fills a gap the briefing has had since the halt:</b>',
 '<b>The one new thing at 6:05&nbsp;PM is the clock, and it has crossed over:</b> the <b>6:00 PM ET</b> CME reopen <b>has now happened</b>, so the <b>1:00&nbsp;PM ET</b> equity-index halt is a '
 '<b>closed five-hour interval</b> rather than a running one, and the ticker at the top of the markets page <b>has started moving again on Tuesday&rsquo;s trade date</b>. '
 '<b>No level is asserted for the reopened tape</b> &mdash; the reopen time was verified in an earlier edition and the elapsed arithmetic is this desk&rsquo;s, but no return read here gives a post-reopen price for any symbol. '
 'Regular U.S. trading still resumes <b>9:30&nbsp;AM ET Tuesday</b>. <b>The 5:38&nbsp;PM edition&rsquo;s item filled a gap the briefing had carried since the halt:</b>','mkt new')

# --- MMA CARD ---
s=sub1(s,'<h3>No new MMA development today &mdash; but a reference source says Shevchenko was stripped, where the briefing has said all day that she vacated</h3>',
 '<h3>A stale champions list came back with three wrong belts on it, and the briefing refused all three &mdash; while a third source finally backs its word for how Shevchenko lost hers</h3>','mma h3')
s=sub1(s,'A third consecutive sweep returned nothing new, so the briefing carries <b>no New tag</b>',
 'A <b>fourth</b> consecutive sweep returned nothing new, so the briefing carries <b>no New tag</b> &mdash; but two things did happen to what it already carries. '
 '<b>A champions-list return arrived with three superseded belts on it</b> &mdash; <b>Pereira</b> at light heavyweight, <b>Chimaev</b> at middleweight and <b>Shevchenko</b> at women&rsquo;s flyweight &mdash; '
 'and <b>all three were refused</b>: the board carries <b>Ulberg</b>, <b>Strickland</b> and <b>vacant</b>, and a list still seating Shevchenko cannot be current for a card built on her giving the belt up. '
 'The other eight lines matched exactly. <b>And a third return is the first to use the briefing&rsquo;s own verb</b>: a UFC&nbsp;332 preview says she was <b>&ldquo;forced to vacate the title due to injury&rdquo;</b> '
 'that &ldquo;will sideline her for up to a year,&rdquo; matching the about-a-year absence already carried. The count is three returns deep, <b>2&ndash;1 for &ldquo;stripped&rdquo; by volume</b>, '
 'but the one saying <b>vacated</b> agrees with the promotion&rsquo;s <b>5 September</b> announcement, which is the source the briefing follows','mma new')
open(O+'index.html','w',encoding='utf-8').write(s)
print('index done')
