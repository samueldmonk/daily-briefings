# -*- coding: utf-8 -*-
import io,re
def rd(f): return io.open(f,encoding='utf-8').read()
def wr(f,s): io.open(f,'w',encoding='utf-8').write(s)

# ---------------- CYBER
f='cyber-briefing.html'; s=rd(f)
NEW=('<div class="tldr"><b>The Wire</b> <span>A print server is still today&rsquo;s most urgent box &mdash; '
'<b>PaperCut NG/MF</b> is under hands-on human intrusion and carries the <b>only federal deadline on this page that has not elapsed</b>, '
'<b>Monday 14 September</b>. <b>The one new item this edition is a Chrome update that is already behind the one you have probably installed.</b> '
'Google&rsquo;s 26-fix stable release closed two critical use-after-free flaws &mdash; <b>CVE-2026-84353</b> in Shared Tab Groups and '
'<b>CVE-2026-84352</b> in WebGL, both reachable from a crafted page and both escaping the sandbox &mdash; plus <b>CVE-2026-84325</b>, a high-severity '
'input-validation flaw in <code>DataTransfer</code>. All three are fixed in <b>152.0.7977.75</b>, and this page has carried <b>152.0.7977.82/.83</b> '
'since Friday as the fix for the exploited V8 zero-day <b>CVE-2026-85046</b> &mdash; <b>.82 is the later build, so anyone patched for the zero-day is '
'already covered for these</b>. None of the three is exploited, none is in KEV, and no countdown is attached to any of them. '
'<b>Tomorrow is Patch Tuesday</b>, with four CVEs pre-published through MSRC and <b>ShieldBreak (CVE-2026-69414)</b> still unpatched and still only '
'<i>expected</i> in the release. Everything else the day&rsquo;s sweeps returned was already on the page &mdash; StyleSmuggler, the N-able hotfix, '
'the MikroTrick RouterOS chain, Tengu, Natural Resources Wales and the <b>2</b>&nbsp;and&nbsp;<b>4 September KEV additions</b> &mdash; and the '
'deadlines below are unchanged, the date not having rolled.</span></div>')
s=re.sub(r'<div class="tldr">.*?</div>',lambda m:NEW,s,count=1,flags=re.S); wr(f,s)

# ---------------- WALL STREET
f='wallstreet-briefing.html'; s=rd(f)
NEW=('<div class="tldr"><b>The Tape</b> <span>U.S. stock and bond markets are shut all day for Labor Day and reopen at '
'<b>9:30&nbsp;AM ET Tuesday</b>, and the oil futures that were still trading have <b>all halted too</b> &mdash; ICE Brent at about '
'<b>1:30&nbsp;PM ET</b> and CME crude at about <b>2:30&nbsp;PM ET</b> on a relayed schedule, after CME&rsquo;s equity-index halt at '
'<b>1:00&nbsp;PM ET</b> &mdash; so <b>every symbol on the live ticker at the top of this page has been showing a last matched price for '
'more than an hour</b>, and the equity-index halt is now the oldest of the three rather than a thing about to happen. '
'<b>The one new item this edition is a component breakdown of the print the whole week is pointed at:</b> the <b>energy component of CPI '
'rose 14.7% year over year in July</b> and <b>gasoline rose 24.6%</b> &mdash; July figures, not a forecast of Friday&rsquo;s August number &mdash; '
'which is the arithmetic connecting today&rsquo;s only live market to Friday&rsquo;s only live data point, with <b>Brent around $97</b> and at a '
'<b>six-week high</b>. <span class="mut">Two undated settlement prices in the same return, <b>WTI $91.30</b> and <b>Brent $95.52</b>, are '
'<b>refused</b> &mdash; this page holds Friday&rsquo;s Brent settlement at <b>$96.28</b> and no Monday settlement exists at all. '
'Still no single Brent level is asserted as <i>the</i> price, and the session is still described as having run both ways. '
'The nowcast (<b>3.38%</b> headline, <b>0.36%</b> monthly), the Waller hike line, and the ECB, PPI, CPI, FOMC, quiet-period and earnings '
'lines below were all already on this page and none of them is tagged New.</span></span></div>')
s=re.sub(r'<div class="tldr">.*?</div>',lambda m:NEW,s,count=1,flags=re.S); wr(f,s)

# ---------------- MMA
f='mma-briefing.html'; s=rd(f)
NEW=('<div class="tldr"><b>Tale of the Tape</b> <span>Valentina Shevchenko&rsquo;s vacated women&rsquo;s flyweight title still leads the page &mdash; '
'<b>Nat&aacute;lia Silva</b> (20&ndash;5&ndash;1, 8&ndash;0 UFC) meets <b>Wang Cong</b> (10&ndash;1, 5&ndash;1 UFC) for the vacant belt at '
'<b>UFC&nbsp;332</b> on <b>3 October</b> in Salt Lake City, on a card that is now <b>finalised at twelve bouts</b>. '
'<b>There is no new MMA item this edition, and the page says so rather than manufacturing one:</b> fresh sweeps of the day&rsquo;s UFC news, '
'newly-booked-fights roundups, the Noche UFC card and the post-event reporting from Paris returned <b>only material already carried</b> &mdash; '
'the 12 September Glendale card in full, Roberto Soldic&rsquo;s signing and debut against Khaos Williams, the UFC&nbsp;334 opener at Madison Square '
'Garden, Brendan Allen vs. Christian Leroy Duncan on 10 October, Paddy Pimblett&rsquo;s December line, and <b>Dan Hooker&rsquo;s three-fight skid, '
'the longest of his career and his first stretch without a win since August 2024</b>, after <b>Salahdine Parnasse</b> stopped him on debut in Paris. '
'<span class="mut">One headline is refused: a living event-schedule article surfaced this run advertises &ldquo;Justin Gaethje vs. Paddy Pimblett&rdquo; '
'and &ldquo;Alexander Volkanovski vs. Diego Lopes 2&rdquo; as upcoming. The Volkanovski&ndash;Lopes rematch <b>already happened</b>, at UFC&nbsp;325 on '
'31 January 2026, and this page carries the result &mdash; so the article is stale, and <b>no Gaethje&ndash;Pimblett booking is printed</b> on the '
'strength of it. Pimblett&rsquo;s own words, already on this page, are that no one has spoken to him. '
'<b>No odds are printed for any UFC&nbsp;332 bout &mdash; no return stated one.</b></span></span></div>')
s=re.sub(r'<div class="tldr">.*?</div>',lambda m:NEW,s,count=1,flags=re.S); wr(f,s)
print("ok")
