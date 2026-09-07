# -*- coding: utf-8 -*-
import io,sys,re
D='/tmp/db_1788782763/'
def load(f): return io.open(D+f,encoding='utf-8').read()
def save(f,h): io.open(D+f,'w',encoding='utf-8').write(h)
N=[0]
def rep(h,old,new,cnt=1):
    assert h.count(old)==cnt, ("COUNT %d!=%d for: %r"%(h.count(old),cnt,old[:110]))
    N[0]+=1
    return h.replace(old,new)

# ================= CYBER =================
c=load('cyber-briefing.html')

# 1) strip previous run's New tag (NodeStealer, tagged at 1843)
c=rep(c,'<div class="tags"><span class="t new">New</span><span class="t">Infostealer</span></div>',
        '<div class="tags"><span class="t">Infostealer</span></div>')

# 2) threat banner -> add exposure count
c=rep(c,'and five KEV entries carrying a 5 September federal deadline are now past due.',
        'the Shadowserver Foundation counts more than <b>122,500</b> MikroTik devices with SSH reachable from the open internet, and five KEV entries carrying a 5 September federal deadline are now past due.')

# 3) new stat tiles
c=rep(c,'<div class="stat"><div class="n">1&ndash;2 days</div>',
 '<div class="stat"><div class="n">122,500+</div><div class="l">MikroTik devices with SSH reachable on the open internet, per the Shadowserver Foundation via Cybernews, 7 September</div></div>\n'
 '<div class="stat"><div class="n">6</div><div class="l">RouterOS CVEs CERT Polska registered &mdash; all six now carry published severity scores, two of them 9.2</div></div>\n'
 '<div class="stat"><div class="n">1&ndash;2 days</div>')

# 4) three remaining MikroTik CVEs into the table
c=rep(c,'<tr><td>CVE-2026-48710</td>',
 '<tr><td>CVE-2026-67281</td><td><b>8.7</b></td><td>MikroTik RouterOS (WebFig)</td>'
 '<td>Unauthenticated file read. The <span style="font-family:var(--mono);font-size:12.5px">/jsproxy</span> path in the web management interface lets an attacker manipulate memory allocation and traverse directories to read files outside the intended web folder, <b>including root-owned config files containing credentials</b>.</td></tr>\n'
 '<tr><td>CVE-2026-67279</td><td><b>6.9</b></td><td>MikroTik RouterOS (SSH)</td>'
 '<td>Pre-authentication rekey state bypass &mdash; an unauthenticated attacker can send commands and potentially create, overwrite or reconstruct files in the RouterOS managed file namespace, including support files holding configuration and diagnostic data.</td></tr>\n'
 '<tr><td>CVE-2026-67278</td><td><b>6.3</b></td><td>MikroTik RouterOS (TLS)</td>'
 '<td>TLS server impersonation &mdash; routers can be tricked into trusting forged certificates.</td></tr>\n'
 '<tr><td>CVE-2026-48710</td>')

save('cyber-briefing.html',c)
print("cyber part1 edits:",N[0])
