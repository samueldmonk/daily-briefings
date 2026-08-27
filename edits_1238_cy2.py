# -*- coding: utf-8 -*-
import io
F='cyber-briefing.html'
s=io.open(F,encoding='utf-8').read()
def rep(old,new):
    global s
    n=s.count(old); assert n==1,"count=%d %r"%(n,old[:80]); s=s.replace(old,new)
rep(u'<tr><td class="mono">CVE-2026-12569</td>',
    u'<tr><td class="mono">CVE-2019-1068</td><td class="mono">Not confirmed this run</td><td>Microsoft SQL Server</td><td><b>New at 12:38.</b> Added to KEV in the <b>Aug 26</b> batch; The Hacker News reports CISA has set a federal remediation date of <b>Aug 29</b> for this CVE alongside the Citrix flaw. <b>No CVSS figure was stated in any source fetched this run, so none is printed.</b></td></tr>\n<tr><td class="mono">CVE-2026-12569</td>')
io.open(F,'w',encoding='utf-8').write(s); print("CY2 OK")
