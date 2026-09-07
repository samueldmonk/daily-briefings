# -*- coding: utf-8 -*-
import io,re
def ins(f,new):
    s=io.open(f,encoding='utf-8').read()
    m=re.search(r'<p class="note"[^>]*><b>New-tag ledger.*?</p>',s,re.S); assert m,f
    s=s[:m.end()]+new+s[m.end():]
    io.open(f,'w',encoding='utf-8').write(s)

A='https://cybersecuritynews.com/google-fixes-26-chrome-vulnerabilities/'
CY=('<p class="note"><b>Added to sources in the 3:35&nbsp;PM ET edition.</b> <span class="mut">For the Chrome rows: '
'<a href="%s">Cyber Security News, &ldquo;Google Fixes 26 Chrome Vulnerabilities, Including 2 Critical Use-After-Free Flaws&rdquo;</a>; '
'<a href="https://gbhackers.com/google-patches-26-chrome-vulnerabilities/">GBHackers on the WebGL and Shared Tab Groups pair</a>; '
'<a href="https://www.malwarebytes.com/blog/bugs/2026/09/two-critical-chrome-flaws-put-users-at-risk-on-malicious-websites">Malwarebytes</a>; '
'<a href="https://www.securityweek.com/chrome-and-firefox-updates-patch-dozens-of-vulnerabilities/">SecurityWeek</a>; '
'<a href="https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-1105">CERT-FR advisory CERTFR-2026-AVI-1105</a>; '
'<a href="https://radar.offseq.com/threat/cve-2026-84353-use-after-free-in-google-chrome-4a4993a5c3130e45">OffSeq on CVE-2026-84353</a> and '
'<a href="https://radar.offseq.com/threat/cve-2026-84325-improper-input-validation-in-google-chrome-a25c992ce169f819">on CVE-2026-84325</a>; '
'<a href="https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop.html">the Chrome Releases stable-channel listing</a>; and '
'<a href="https://cvebrief.com/archive/2026/09/06/">CVE Brief, 6 September</a>, which is where the two CVE numbers first surfaced this run. '
'For tomorrow&rsquo;s release: '
'<a href="https://www.helpnetsecurity.com/2026/09/04/september-2026-patch-tuesday-forecast/">Help Net Security&rsquo;s 4 September forecast</a>, '
'<a href="https://senserva.com/patch-tuesday-2026-09.html">Senserva</a> and a Meridian Micro preparation note for the four MSRC pre-publications. '
'<b>None of these was fetched first-hand this run</b> &mdash; all are search returns, and every sentence built on them says so. '
'<b>CISA&rsquo;s own KEV alert pages were not reachable again</b>, so the 14, 16 and 18 September dates remain attributed to reporting.</span></p>')%A

WS=('<p class="note"><b>Added to sources in the 3:35&nbsp;PM ET edition.</b> <span class="mut">The July energy and gasoline components come from '
'<a href="https://www.fool.com/investing/2026/09/07/why-friday-critical-days-stock-market-september/">a Motley Fool commentary dated today, 7 September</a>, '
'which also restates the nowcast and the Waller line this page already carried; '
'<a href="https://www.kiplinger.com/investing/economy/this-weeks-economic-calendar">Kiplinger&rsquo;s 7&ndash;11 September calendar</a> corroborates the '
'PPI-Thursday / CPI-Friday sequence and the 8:30&nbsp;AM ET release time. The holiday schedule and the reopen were re-confirmed against '
'<a href="https://www.kucoin.com/news/flash/u-s-markets-closed-on-sept-7-for-labor-day-futures-trading-ends-early">a Labor Day market-hours flash</a> and '
'<a href="https://finance.yahoo.com/markets/stocks/articles/stock-market-closed-today-why-100314745.html">Yahoo Finance</a>. '
'<b>The $91.30 and $95.52 settlements in the Motley Fool return are refused</b>, for the reason printed above. '
'<b>Nothing was fetched first-hand this run.</b></span></p>')

MMA=('<p class="note"><b>Added to sources in the 3:35&nbsp;PM ET edition.</b> <span class="mut">Nothing new was published on this page this edition, so '
'nothing was added to it; the returns read were '
'<a href="https://sports.yahoo.com/articles/ufc-fight-night-287-post-161026018.html">Yahoo Sports&rsquo; UFC Fight Night 287 post-event facts</a> '
'(Hooker&rsquo;s three-fight skid, longest of his career; no win since August 2024; 3&ndash;3 since returning to lightweight in November 2022 &mdash; all already carried), '
'<a href="https://fightomic.com/newly-booked-ufc-fights-week-ending-6-september-2026/">Fightomic&rsquo;s newly-booked-fights roundup for the week ending 6 September</a>, '
'<a href="https://en.wikipedia.org/wiki/UFC_Fight_Night:_Silva_vs._Delgado">the Noche UFC card listing</a>, '
'<a href="https://bloodyelbow.com/2026/09/05/full-ufc-332-card-finalized-with-star-signing-roberto-soldics-debut-among-main-card-additions/">Bloody Elbow on the finalised UFC&nbsp;332 card</a>, and '
'<a href="https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions">ESPN&rsquo;s current UFC champions page</a>. '
'<b>Every one of them matched material already on the page.</b> '
'<b>One return is refused outright:</b> a CBS Sports event-schedule article headed &ldquo;Justin Gaethje vs. Paddy Pimblett, Alexander Volkanovski vs. '
'Diego Lopes 2 on tap&rdquo;. The Volkanovski&ndash;Lopes rematch is <b>not</b> upcoming &mdash; it was <b>UFC&nbsp;325 on 31 January 2026</b> &mdash; '
'so the article is a living page that has not been updated, and <b>no booking from it is printed</b>, including the Gaethje&ndash;Pimblett bout beside it. '
'&#9733; <b>An event-schedule article that lists a fight which has already happened has told you its date; do not take the fight beside it on trust.</b> '
'<b>Nothing was fetched first-hand this run.</b></span></p>')

ins('cyber-briefing.html',CY); ins('wallstreet-briefing.html',WS); ins('mma-briefing.html',MMA)
print("ok")
