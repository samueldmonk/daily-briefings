# -*- coding: utf-8 -*-
import sys
O='/sessions/gracious-zealous-maxwell/mnt/outputs/'
def rd(f): return open(O+f,encoding='utf-8').read()
def wr(f,s): open(O+f,'w',encoding='utf-8').write(s)
def sub1(s,a,b,label):
    if a not in s: print('!! MISS',label); sys.exit(1)
    return s.replace(a,b,1)

c=rd('cyber-briefing.html')

# 1. strip prior New tags -> Carried
c=c.replace('<span class="t new" style="margin-right:6px">New</span>','<span class="t" style="margin-right:6px">Carried</span>')
c=c.replace('<span class="t new">New</span>','<span class="t">Carried</span>')

# 2. insert the one genuinely new row at the top of Vulnerability Watch
hdr='<tr><th>CVE</th><th>CVSS</th><th>Affected</th><th>Note</th></tr> '
row=('<tr><td><span class="t new" style="margin-right:6px">New</span> CVE-2026-51693</td>'
 '<td class="down"><b>9.8 (Critical)</b><br><span class="mut">per the summary, not the vendor</span></td>'
 '<td><b>TOTOLINK T6</b> router</td>'
 '<td><b>The one new entry in this 6:05&nbsp;PM edition, and it is deliberately the smallest item on the page.</b> A CVE round-up read at this desk lists '
 '<b>CVE-2026-51693</b> at <b>CVSS 9.8</b> in the <b>TOTOLINK T6</b> router, among the critical disclosures dated <b>7 September</b>. '
 '<span class="mut"><b>Almost everything about it is deliberately not claimed.</b> <b>No vulnerability class, no affected firmware build and no fixed version</b> is stated, because '
 'the summary gives none and <b>no TOTOLINK advisory was fetched here</b> &mdash; so an owner cannot yet check a box against it, and this page says so rather than implying they can. '
 '<b>It is not described as exploited</b>: the same round-up lists the ten CVEs it calls actively exploited, and <b>this is not among them</b>. It carries <b>no federal deadline and no countdown</b>, '
 'and it <b>does not appear in the 2 or 4 September KEV additions this page lists</b> &mdash; a statement about those two lists, not about the whole catalog. '
 'It is published because a <b>9.8 on consumer-edge hardware</b> belongs on a vulnerability watch even when the only honest version of the entry is four facts long. '
 'Source: a securityonline.info / CVE Brief round-up dated <b>7 September</b> &mdash; <b>not fetched first-hand</b>. '
 '&#9733; <b>An entry you can only half-source is still worth printing if you print which half is missing; what is not acceptable is filling the gap from memory.</b></span></td></tr> ')
c=sub1(c,hdr,hdr+row,'cyber new row')

# 3. tldr rewrite of the opener
old=('<b>Two items are new in the 5:38&nbsp;PM edition, and neither is an appliance or a router &mdash; one is a virtual-machine escape, '
     'the other a federal tally that has to be read with its dates attached.</b>')
new=('<b>One item is new in this 6:05&nbsp;PM edition, and it is the smallest entry on the page rather than the largest:</b> a round-up read at this desk puts '
     '<b>CVE-2026-51693</b> at <b>CVSS 9.8</b> in the <b>TOTOLINK T6</b> router among the critical disclosures dated <b>7 September</b> &mdash; and it goes into Vulnerability Watch with '
     '<b>no vulnerability class, no affected build and no fixed version</b>, because the summary gives none and no vendor advisory was fetched here. It is <b>not</b> among the ten CVEs that same round-up calls '
     'actively exploited, and it carries <b>no deadline</b>. <b>The two items new in the 5:38&nbsp;PM edition are carried, and neither was an appliance or a router &mdash; one a virtual-machine escape, '
     'the other a federal tally that has to be read with its dates attached.</b>')
c=sub1(c,old,new,'cyber tldr')
wr('cyber-briefing.html',c)
print('cyber done; new tags',c.count('class="t new"'))
