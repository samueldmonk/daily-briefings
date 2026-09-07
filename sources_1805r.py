# -*- coding: utf-8 -*-
import sys
O='/sessions/gracious-zealous-maxwell/mnt/outputs/'
def sub1(s,a,b,label):
    if a not in s: print('!! MISS',label); sys.exit(1)
    return s.replace(a,b,1)

# MMA sources
m=open(O+'mma-briefing.html',encoding='utf-8').read()
old='Sources</h2><p class="note" style="margin:-2px 0 10px"><b>Re-checked in the 5:05&nbsp;PM ET edition, none fetched first-hand and none new:</b>'
new=('Sources</h2><p class="note" style="margin:-2px 0 10px"><b>New in this 6:05&nbsp;PM ET edition, not fetched first-hand:</b> <span class="mut">'
 '<a href="https://sports.yahoo.com/articles/vacant-title-fight-headlines-ufc-230937427.html">Yahoo Sports &mdash; Vacant title fight headlines UFC&nbsp;332 in Salt Lake City</a> '
 '(the third return on the vacated belt, and the first to use <b>&ldquo;forced to vacate &hellip; due to injury&rdquo;</b>, with the absence put at <b>up to a year</b>) &nbsp;&middot;&nbsp; '
 '<a href="https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions">ESPN &mdash; Current and all-time UFC champions</a> '
 '(the champions-list return whose <b>light heavyweight, middleweight and women&rsquo;s flyweight</b> lines are refused here as superseded, and whose other eight match this board).</span> '
 '<b>Re-checked, none fetched first-hand and none new:</b>')
m=sub1(m,old,new,'mma sources')
open(O+'mma-briefing.html','w',encoding='utf-8').write(m)

# CYBER sources -- add the round-up behind the TOTOLINK row
c=open(O+'cyber-briefing.html',encoding='utf-8').read()
i=c.rfind('Sources</h2>')
if i<0: print('!! MISS cyber sources'); sys.exit(1)
j=c.find('>',c.find('<p',i))+1
ins=('<b>New in this 6:05&nbsp;PM ET edition, not fetched first-hand:</b> <span class="mut">'
 '<a href="https://cvebrief.com/archive/2026/09/07/">CVE Brief &mdash; 7 September 2026 archive</a> and '
 '<a href="https://securityonline.info/weekly-cve-report-10-exploited-vulnerabilities-hit-cisa-kev/">securityonline.info &mdash; weekly CVE report</a>, '
 'the round-up behind <b>CVE-2026-51693 (CVSS 9.8, TOTOLINK T6)</b> and behind the statement that it is <b>not</b> among the ten CVEs listed there as actively exploited. '
 '<b>No TOTOLINK advisory was read</b>, which is why the row carries no vulnerability class, affected build or fixed version.</span> ')
c=c[:j]+ins+c[j:]
open(O+'cyber-briefing.html','w',encoding='utf-8').write(c)

# WALL STREET sources -- reopen/schedule corroboration
w=open(O+'wallstreet-briefing.html',encoding='utf-8').read()
i=w.rfind('Sources</h2>')
j=w.find('>',w.find('<p',i))+1
ins=('<b>Re-checked in this 6:05&nbsp;PM ET edition, not fetched first-hand:</b> <span class="mut">'
 '<a href="https://finance.yahoo.com/personal-finance/investing/article/is-the-stock-market-open-on-labor-day-heres-the-holiday-trading-schedule-for-2026-210239142.html">Yahoo Finance &mdash; Labor Day 2026 trading schedule</a>, '
 'restating that U.S. stock <b>and bond</b> markets were shut all day and resume normal hours <b>9:30&nbsp;a.m.&ndash;4:00&nbsp;p.m. ET Tuesday 8 September</b>; and '
 '<a href="https://www.kiplinger.com/investing/economy/this-weeks-economic-calendar">Kiplinger &mdash; this week&rsquo;s economic calendar</a>, restating <b>PPI Thursday</b>, <b>CPI Friday 11 September</b> and the '
 '<b>Fed blackout</b> ahead of the <b>15&ndash;16 September</b> FOMC. <b>No return read here gives a post-reopen futures level</b>, so none is printed.</span> ')
w=w[:j]+ins+w[j:]
open(O+'wallstreet-briefing.html','w',encoding='utf-8').write(w)
print('sources done')
