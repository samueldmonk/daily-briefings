# -*- coding: utf-8 -*-
import re, io, sys

def rd(f): return io.open(f,encoding='utf-8').read()
def wr(f,s): io.open(f,'w',encoding='utf-8').write(s)

FAIL=[]
def rep(s, old, new, f, n=1):
    if old not in s:
        FAIL.append((f, old[:90])); return s
    return s.replace(old, new, n)

# ---------------------------------------------------------------- DEMOTE
DEM = [
 ("in this edition", "in the 3:05&nbsp;PM edition"),
 ("This edition adds no new cyber item", "The 3:05&nbsp;PM edition added no new cyber item"),
 ("changed in this edition", "changed in the 3:05&nbsp;PM edition"),
 ("No new item this edition", "No new item in the 3:05&nbsp;PM edition"),
 ("The ESPN return this edition", "The ESPN return in the 3:05&nbsp;PM edition"),
 ("this edition", "the 3:05&nbsp;PM edition"),
 ("This edition", "The 3:05&nbsp;PM edition"),
]
for f in ['index.html','cyber-briefing.html','wallstreet-briefing.html','mma-briefing.html']:
    s = rd(f)
    for a,b in DEM: s = s.replace(a,b)
    # grammar repair for blanket demotion
    s = s.replace("item the 3:05&nbsp;PM edition","item in the 3:05&nbsp;PM edition")
    s = s.replace("return the 3:05&nbsp;PM edition","return in the 3:05&nbsp;PM edition")
    s = s.replace("read the 3:05&nbsp;PM edition","read in the 3:05&nbsp;PM edition")
    # strip previous run's New tags
    s = s.replace('<span class="t new" style="margin-right:6px">New</span>','<span class="t" style="margin-right:6px">Carried</span>')
    s = s.replace('<span class="t new">New</span>','<span class="t">Carried</span>')
    wr(f,s)

# ================================================================ CYBER
f='cyber-briefing.html'; s=rd(f)

NEWROWS = (
'<tr><td><span class="t new">New</span> CVE-2026-84353<br><span class="mut">with CVE-2026-84352</span></td>'
'<td class="down"><b>Critical</b><br><span class="mut">no numeric score stated</span></td>'
'<td>Google <b>Chrome</b> before <b>152.0.7977.75</b><br><span class="mut">.75/.76 Windows &amp; macOS, .75 Linux</span></td>'
'<td><b>Two critical use-after-free bugs in a 26-fix stable update &mdash; and this page already carries the build that supersedes it.</b> '
'<b>CVE-2026-84353</b> is a use-after-free in <b>Shared Tab Groups</b>; the write-up specifies <b>Chrome on Android</b> before 152.0.7977.75, and says a remote attacker <b>leveraging social engineering</b> could execute arbitrary code <b>outside the sandbox</b> via a crafted HTML page. '
'<b>CVE-2026-84352</b> is a use-after-free in <b>WebGL</b>, Chrome&rsquo;s 2D/3D rendering component, with the same outside-the-sandbox outcome via a crafted page. '
'<b>No CVSS is printed for either</b> &mdash; no return read this run stated one, and &ldquo;Critical&rdquo; is Google&rsquo;s own severity label, not a score. '
'<b>Nothing here is exploited and nothing is in KEV,</b> so no countdown appears in this row. '
'<b>Read the version numbers before you act on the headline:</b> the KEV zero-day this page has carried since Friday, <b>CVE-2026-85046</b>, is fixed in <b>152.0.7977.82/.83</b> &mdash; a <i>later</i> build than the .75 that closes these two. '
'A desk that has already applied the 3 September update for the zero-day <b>has these fixes too</b>.</td></tr>\n'
'<tr><td><span class="t new">New</span> CVE-2026-84325</td>'
'<td><b>High</b><br><span class="mut">Google label; no score stated</span></td>'
'<td>Google <b>Chrome</b> before <b>152.0.7977.75</b></td>'
'<td><b>Improper input validation in <code>DataTransfer</code></b> &mdash; a remote attacker <b>leveraging social engineering</b> could bypass system access restrictions <b>via a co-installed app</b>. '
'It is in the same 26-fix update and is <b>not</b> one of the two criticals: one return&rsquo;s summary line grouped all three as &ldquo;critical entries&rdquo;, and that grouping is <b>refused</b> &mdash; the detailed write-ups make the critical pair <b>84353 and 84352</b>, both use-after-free, and rate 84325 <b>High</b>. '
'Superseded by .82/.83 exactly as above.</td></tr>\n'
)
i=s.find('<h2 class="sec">Vulnerability Watch'); j=s.find('</table>',i)
s = s[:j] + NEWROWS + s[j:]

# note under the table
NOTE = ('<p class="note"><b>Why a five-day-old Chrome release is the new cyber item on a day with no new attack.</b> '
'<span class="mut">The two rows above look like breaking news and are not: the 26-fix stable update they belong to '
'(<b>152.0.7977.75/.76</b> on Windows and macOS, <b>.75</b> on Linux) <b>predates</b> the <b>3 September</b> update this page '
'has carried since Friday, which shipped <b>152.0.7977.82/.83</b> and closed 12 flaws including the exploited V8 zero-day '
'<b>CVE-2026-85046</b>. Version order settles it &mdash; <b>.75 is earlier than .82</b> &mdash; so these CVEs are not a new exposure '
'for anyone already patched, and the page says so in both rows rather than letting the headline imply otherwise. '
'For sequence: <b>Chrome 152 reached stable on 25 August</b> as <b>152.0.7977.64/.65</b> with <b>327</b> security fixes; '
'the 26-fix <b>.75</b> update followed in early September; the 12-fix <b>.82/.83</b> update followed that on 3 September. '
'&#9733; <b>A CVE with a fixed-version number carries its own date. Compare the build to the one you already ship before you '
'call the flaw new.</b> Routes read this run: Cyber Security News, GBHackers, Malwarebytes, SecurityWeek, CERT-FR, OffSeq, '
'Cryptika, Cyberpress and the Chrome Releases blog listing; <b>none fetched first-hand</b>.</span></p>\n'
'<p class="note"><b>Tomorrow is Patch Tuesday, and Microsoft has already published four CVEs ahead of it.</b> '
'<span class="mut">Named in returns read this run as pre-disclosed through MSRC before the <b>8 September</b> release: '
'<b>CVE-2026-58641</b> (.NET, elevation of privilege), <b>CVE-2026-62815</b> (Microsoft QUIC, remote code execution), '
'<b>CVE-2026-58612</b> (PowerShell, information disclosure) and <b>CVE-2026-50376</b> (Windows Remote Desktop Client, '
'information disclosure). <b>No CVSS, no exploitation claim and no KEV entry is printed for any of the four</b> &mdash; none was stated. '
'On volume, the forecasts read this run say <b>150&ndash;300+</b> and <b>200&ndash;300</b> CVEs, against August&rsquo;s record <b>421</b>, '
'which this page already carries; they are ranges from commentators, not a Microsoft figure. '
'<b>Two things refused.</b> (1) One publisher gives the release time as <b>10:00&nbsp;AM PST / 1:00&nbsp;PM EST / 6:00&nbsp;PM UTC</b>. '
'Those three do not agree in September: 6:00&nbsp;PM UTC is <b>2:00&nbsp;PM ET</b> on daylight time, and 10:00&nbsp;AM Pacific is <b>PDT</b>, not PST. '
'The <b>UTC figure is carried and the ET figure is not</b>, with the conversion named as this desk&rsquo;s. '
'(2) A vendor page headed &ldquo;<b>9 CVEs, 9 Critical</b>&rdquo; for September is <b>not adopted</b> &mdash; it contradicts both forecasts by two orders of '
'magnitude and reads as an unpopulated template for a release that has not happened. '
'<b>ShieldBreak (CVE-2026-69414) is re-confirmed as still unpatched</b> and still expected rather than promised in tomorrow&rsquo;s release; '
'that item is already on this page and is <b>not</b> tagged again.</span></p>\n')
s = s[:s.find('</table>',i)+8] + NOTE + s[s.find('</table>',i)+8:]
wr(f,s)

# ================================================================ REPORT
if FAIL:
    print("MISSING ANCHORS:")
    for f,o in FAIL: print("  ",f,"|",o)
else:
    print("ok")
