# -*- coding: utf-8 -*-
import re, sys
h = open('index.html', encoding='utf-8').read()
fails=[]
def rep(old,new,lab):
    global h
    if h.count(old)!=1:
        fails.append(lab+' n=%d'%h.count(old)); return
    h = h.replace(old,new,1)

rep('<h2>Apollo Global confirms a breach with Social Security numbers in it</h2>',
    '<h2>DOJ and FBI seize two China-run hacking platforms &mdash; NASA, the Fed and the Senate named as victims</h2>','sec-h2')
i = h.find('<h2>DOJ and FBI seize'); j = h.find('<p>', i); k = h.find('</p>', j)
if i<0 or j<0: fails.append('sec-p')
else:
    h = h[:j] + ('<p><b>The Justice Department and FBI have seized the domains behind QScan and QTRouter</b>, complementary platforms built and run by the PRC state-sponsored group <b>QTFY</b>, employed by China&rsquo;s <b>Nanjing Xinjiuwei Network Technology Company</b>. DOJ names <b>NASA, the Federal Reserve, the Departments of Energy, Justice and Health and Human Services, the NIH and the U.S. Senate</b> among the victims. Because the domains were hard-coded into both, <b>the seizures made the malware inoperable.</b> KEV is static; <b>Oracle CVE-2026-21962 is due tomorrow.</b></p>') + h[k+4:]

rep('<h2>Nvidia&rsquo;s after-hours loss reverses on the call</h2>',
    '<h2>Nvidia settles up more than 4% once the call ends</h2>','mkt-h2')
i = h.find('<h2>Nvidia settles up'); j = h.find('<p>', i); k = h.find('</p>', j)
if i<0: fails.append('mkt-p')
else:
    h = h[:j] + ('<p>With the conference call over, <b>CNBC reports Nvidia up more than 4% in extended trading</b> and stock futures rising with it, after a quarter it says beat forecasts <b>by the largest margin in two years</b>. That sits below the <b>~&plus;5% peak at 5:10&nbsp;p.m.</b> and above the <b>&minus;1% / &minus;1.3%</b> reads taken before the call &mdash; <b>all four are kept as timestamped observations, none retracted.</b> <b>HP Inc &minus;11%</b> is still the night&rsquo;s worst move.</p>') + h[k+4:]

rep('<h2>The Sacramento rankings fallout gets its numbers</h2>',
    '<h2>Fight week in Shanghai, and a disagreement about two rankings</h2>','mma-h2')
i = h.find('<h2>Fight week in Shanghai'); j = h.find('<p>', i); k = h.find('</p>', j)
if i<0: fails.append('mma-p')
else:
    h = h[:j] + ('<p>Nothing moved this run. <b>UFC Shanghai &mdash; Umar Nurmagomedov vs. Song Yadong, Saturday at the Oriental Sports Center</b> &mdash; is re-confirmed with the line at <b>&minus;500 / &plus;380</b>. &#9888; <b>UFC.com bills them &ldquo;#3&rdquo; and &ldquo;#5&rdquo;; a summary of the same coverage says No.&nbsp;2 and No.&nbsp;6 &mdash; both printed, neither adopted.</b> The most recent completed event is still <b>Sacramento, August&nbsp;22</b>, and the <b>champions board is unchanged for a thirty-third edition.</b></p>') + h[k+4:]

if fails:
    print('FAILED', fails); sys.exit(1)
open('index.html','w',encoding='utf-8').write(h)
print('index OK', len(h))
