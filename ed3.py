# -*- coding: utf-8 -*-
import io
D='/tmp/db_1788782763/'
def load(f): return io.open(D+f,encoding='utf-8').read()
def save(f,h): io.open(D+f,'w',encoding='utf-8').write(h)
N=[0]
def rep(h,old,new,cnt=1):
    assert h.count(old)==cnt, ("COUNT %d!=%d for: %r"%(h.count(old),cnt,old[:110]))
    N[0]+=1; return h.replace(old,new)

c=load('cyber-briefing.html')

# 7) rewrite the New-tag accounting note for this edition
i=c.find('<p class="note" style="margin:-4px 0 12px"><b>One item is tagged New this edition')
j=c.find('</p>',i)+4
old=c[i:j]
new=('<p class="note" style="margin:-4px 0 12px"><b>One item is tagged New this edition, and the previous edition&rsquo;s tag has been stripped rather than left to decay.</b> '
 'The new card is the MikroTik exposure count below, taken from '
 '<span style="font-family:var(--mono);font-size:12.5px">cybernews.com/security/mikrotik-routers-under-active-exploitation/</span>, which was <b>fetched directly</b> this run and carries '
 '<span style="font-family:var(--mono);font-size:12.5px">article:published_time 2026-09-07T09:14:26+00:00</span> &mdash; published this morning, making it the freshest source on the page. '
 'The tokens <b>Shadowserver</b>, <b>122,500</b> and <b>Pratley</b> were each grepped against <span style="font-family:var(--mono);font-size:12.5px">archive/cyber-2026-09-06-1843.html</span> and '
 'returned <b>zero matches</b> apiece before the tag went on. The <b>NodeStealer</b> card tagged New at 6:43 PM yesterday appears in that same snapshot, so its tag has been removed and its content kept. '
 '<b>Cyber carries 1 New tag this edition; Wall Street 0; MMA 0.</b></p>')
c=rep(c,old,new)

# 8) the New card itself
c=rep(c,'<div class="cards">\n<div class="card">\n<div class="tags"><span class="t">Infostealer</span></div>',
 '<div class="cards">\n<div class="card">\n<div class="tags"><span class="t new">New</span><span class="t hot">Exposure</span></div>\n'
 '<h3>122,500 MikroTik routers are sitting on the open internet with SSH reachable &mdash; and the six MikroTrick CVEs now all have scores</h3>\n'
 '<p><b>Cybernews reported this morning that the Shadowserver Foundation has found more than 122,500 MikroTik devices exposing SSH to the public internet</b>, concentrated in '
 '<b>Brazil (11,300)</b>, the <b>United States (7,100)</b>, <b>Indonesia (7,100)</b>, the <b>Czech Republic (6,300)</b> and <b>Ukraine (5,100)</b>. How many of those remain unpatched is unknown '
 'and the report says so. The same piece closes the scoring gap this page has carried since the story broke: CERT Polska registered <b>six</b> RouterOS CVEs and all six now have published severity '
 'ratings &mdash; the two that chain into MikroTrick at <b>9.2</b> apiece, a kernel-memory disclosure at <b>8.8</b>, an unauthenticated WebFig file read at <b>8.7</b>, an SSH rekey-state bypass at '
 '<b>6.9</b> and TLS server impersonation at <b>6.3</b>. Independent researcher <b>Nick Pratley</b>, who reverse-engineered MikroTik&rsquo;s deliberately vague patch, recommends '
 '<b>&ldquo;a clean rebuild rather than trusting only automatic cleanup&rdquo;</b> for any device that was exposed. <span class="mut">MikroTik also sent a push notification through its mobile app '
 'about the update &mdash; a first for the company, noted by both Cybernews and CERT Polska.</span></p>\n</div>\n'
 '<div class="card">\n<div class="tags"><span class="t">Infostealer</span></div>')

# 9) tldr tail
c=rep(c,'has a public exploit estimated one to two days out and five KEV entries passed their federal deadline yesterday.</span></div>',
        'now has all six of its CVEs scored and more than 122,500 exposed routers counted, and five KEV entries are past their federal deadline.</span></div>')

# 10) sources
c=rep(c,'<h2 class="sec">Sources</h2><div class="panel srcs"><a href="https://securityaffairs.com/198538',
 '<h2 class="sec">Sources</h2><div class="panel srcs"><a href="https://cybernews.com/security/mikrotik-routers-under-active-exploitation/">Cybernews &mdash; 122,500 MikroTik routers expose SSH; six CVEs scored (7 Sep)</a> &nbsp;&middot;&nbsp; <a href="https://mikrotik.com/supportsec/september-2026-vulnerability/">MikroTik &mdash; September 2026 vulnerability advisory</a> &nbsp;&middot;&nbsp; <a href="https://npratley.net/reversing-mikrotiks-silent-patch-the-routeros-7-23-4-fix-they-wouldnt-explain/">Nick Pratley &mdash; reversing MikroTik&rsquo;s silent patch</a> &nbsp;&middot;&nbsp; <a href="https://www.cisa.gov/known-exploited-vulnerabilities-catalog">CISA &mdash; Known Exploited Vulnerabilities catalog</a> &nbsp;&middot;&nbsp; <a href="https://securityaffairs.com/198538')

save('cyber-briefing.html',c)
print("cyber part3:",N[0])
