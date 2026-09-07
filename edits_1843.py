# -*- coding: utf-8 -*-
import io, re, sys
CY="cyber-briefing.html"; WS="wallstreet-briefing.html"; MM="mma-briefing.html"; IX="index.html"
def rd(p): return io.open(p,encoding="utf-8").read()
def wr(p,s): io.open(p,"w",encoding="utf-8").write(s)
FAIL=[]
def rep(s, old, new, n=1, tag=""):
    c=s.count(old)
    if c!=n: FAIL.append("REPLACE %s expected %d got %d :: %s"%(tag,n,c,old[:90])); return s
    return s.replace(old,new)

# ---------- 1. DEMOTE inherited self-references ----------
DEM=[("in this 6:05&nbsp;PM edition","in the 6:05&nbsp;PM edition"),
     ("this 6:05&nbsp;PM ET edition","the 6:05&nbsp;PM ET edition"),
     ("this 6:05&nbsp;PM edition","the 6:05&nbsp;PM edition"),
     ("this 6:05 PM edition","the 6:05 PM edition")]
for p in (CY,WS,MM,IX):
    s=rd(p)
    for a,b in DEM: s=s.replace(a,b)
    wr(p,s)

# ---------- 2. CYBER ----------
s=rd(CY)
CY_LEAD=(u"<b>Two items are new in this 6:35&nbsp;PM edition, and the larger one is a theft rather than a flaw:</b> "
 u"self-described white-hat actors moved about <b>4,000 BTC</b> &mdash; put at roughly <b>$320 million</b>, and "
 u"<b>close to 95%</b> of the reserves backing the <b>Liquid</b> Bitcoin sidechain, which stood near <b>4,200 BTC</b> "
 u"beforehand &mdash; out of the network&rsquo;s <b>federation wallet</b> on <b>6 September</b>, and <b>Blockstream "
 u"disabled Liquid&rsquo;s bridge nodes</b>, stopping new transactions and pausing the <b>two-way peg</b> that moves "
 u"bitcoin in and out of the network. <b>3,400 BTC</b>, put at <b>$268 million</b>, has since been <b>returned</b>; "
 u"roughly <b>598.5 BTC</b>, put at <b>$47 million</b>, was <b>kept</b>, and the network was still frozen in the "
 u"reporting read here. <b>The &ldquo;whitehats&rdquo; label is the actors&rsquo; own</b>, written in an on-chain message, "
 u"and <b>no return read here independently confirms it</b>. <b>There is no CVE, no CVSS, no vendor patch and no KEV "
 u"entry</b> &mdash; what the returns describe is the <b>federation-controlled peg-out mechanism</b>, a system built on "
 u"top of Bitcoin, rather than a numbered software defect &mdash; so it carries <b>no federal deadline and no countdown</b>, "
 u"and it does <b>not</b> displace PaperCut as the urgent box. <b>Two arithmetic gaps are printed rather than smoothed:</b> "
 u"4,000 less 3,400 is <b>600</b>, where the returns say <b>598.5</b> kept, and $320m less $268m is <b>$52m</b>, where the "
 u"returns say <b>$47m</b> &mdash; both subtractions are this desk&rsquo;s, on figures the sources themselves round, and "
 u"<b>neither gap is explained by anything read here</b>. <b>The second new item is a correction to this page&rsquo;s own "
 u"account of the federal patching clock:</b> it has said that <b>BOD 26-04</b> supersedes <b>BOD 22-01&rsquo;s uniform "
 u"three weeks</b>, and returns read this run describe the older directive&rsquo;s clock instead as <b>14 days for "
 u"vulnerabilities assigned a CVE after 2021 and six months for older ones</b> &mdash; two windows, neither of them three "
 u"weeks. <b>The line is corrected in the KEV section below rather than left standing</b>, and <b>no deadline printed on "
 u"this page moved on the strength of it</b>. ")
s=rep(s,u"<b>One item is new in the 6:05&nbsp;PM edition, and it is the smallest entry on the page rather than the largest:</b>",
      CY_LEAD+u"<b>The item new in the 6:05&nbsp;PM edition was the smallest entry on the page rather than the largest:</b>",1,"cy-tldr")

ST=(u'<div class="stat"><div class="n">~4,000 BTC</div><div class="l">moved out of the <b>Liquid</b> sidechain&rsquo;s '
 u'<b>federation wallet</b> on <b>6 September</b> &mdash; roughly <b>$320 million</b>, close to <b>95%</b> of reserves that '
 u'stood near <b>4,200 BTC</b>. <b>3,400 BTC ($268m) returned</b>, about <b>598.5 BTC ($47m)</b> kept, bridge nodes disabled '
 u'and the network frozen. <b>No CVE, no CVSS, no KEV entry</b> &mdash; CoinDesk, Bitcoin.com News, coinpaprika, 6&ndash;7 '
 u'September, none fetched first-hand</div></div>'
 u'<div class="stat"><div class="n">3 / 14 / 60</div><div class="l">calendar-day remediation windows under <b>BOD 26-04</b>, '
 u'issued <b>10 June 2026</b>, which scores each asset&ndash;vulnerability pair on <b>public exposure, KEV status, exploit '
 u'automation and technical impact</b> into <b>one of five tiers</b> &mdash; the lowest deferrable to a future system upgrade. '
 u'It replaced <b>BOD 22-01</b>, whose clock the returns give as <b>14 days for post-2021 CVEs and six months for older ones</b> '
 u'&mdash; Tenable, FedTech, Action1, runZero, none fetched first-hand</div></div>')
s=rep(s,u'<div class="stats">\n<div class="stat"><div class="n">500+</div>',u'<div class="stats">\n'+ST+u'<div class="stat"><div class="n">500+</div>',1,"cy-stats")

CARD=(u'<div class="cards"><div class="card"><div class="tags"><span class="t new">New</span><span class="t">Crypto</span>'
 u'<span class="t">Theft</span><span class="t">No CVE</span></div>'
 u'<h3>$320 million walked out of a Bitcoin sidechain&rsquo;s federation wallet &mdash; and most of it walked back in</h3>'
 u'<p><b>This is the largest number on the page today and it has no CVE attached to it.</b> Self-described white-hat actors '
 u'withdrew about <b>4,000 BTC</b> from the <b>Liquid Network</b> federation wallet on <b>6 September 2026</b> &mdash; worth '
 u'roughly <b>$320 million</b> and <b>close to 95%</b> of the sidechain&rsquo;s reserves, which the returns put near '
 u'<b>4,200 BTC</b> before the incident. Liquid is a <b>Bitcoin sidechain</b>, and its federation wallet holds the coins that '
 u'back tokens issued on the network. <b>Blockstream disabled the network&rsquo;s bridge nodes</b>, which stopped new '
 u'transactions from being submitted, pausing the sidechain and halting the <b>two-way peg</b> that moves bitcoin in and out.</p>'
 u'<p><b>Most of it has come back.</b> The actors <b>returned 3,400 BTC</b>, put at about <b>$268 million</b>, while keeping '
 u'roughly <b>598.5 BTC</b>, put at about <b>$47 million</b>; the network was <b>still frozen</b> in the reporting read here. '
 u'An <b>on-chain message</b> tied to the transaction read <b>&ldquo;we are whitehats&rdquo;</b> &mdash; <b>the label came from '
 u'the actors themselves and no return read here independently confirms it</b>, which is why this card does not repeat it '
 u'unquoted. The exploit is described as targeting Liquid&rsquo;s <b>federation-controlled peg-out mechanism</b>, a separate '
 u'system built on top of Bitcoin.</p>'
 u'<p><b>What this desk is not asserting.</b> There is <b>no CVE, no CVSS, no affected version, no vendor patch and no KEV '
 u'entry</b> in anything read here, so the item appears in no table above, carries <b>no federal deadline and no countdown</b>, '
 u'and <b>does not displace PaperCut</b> as the most urgent box for defenders. <b>Two arithmetic gaps are printed rather than '
 u'smoothed:</b> 4,000 less 3,400 is <b>600</b>, where the returns say <b>598.5</b> kept, and $320m less $268m is <b>$52m</b>, '
 u'where the returns say <b>$47m</b>. Both subtractions are <b>this desk&rsquo;s arithmetic on the sources&rsquo; own rounded '
 u'figures</b>, and <b>nothing read here explains either gap</b> &mdash; the likeliest causes, rounding and a moving bitcoin '
 u'price, are <b>not asserted</b> because no return says so. <b>One date needs care:</b> the withdrawal is dated <b>6 September</b> '
 u'and the coverage <b>7 September</b>, and a day-of aggregator filed it under the later date.</p>'
 u'<p class="note"><b>Sources (search returns, none fetched first-hand):</b> <span class="mut">CoinDesk, 7 September; '
 u'Bitcoin.com News on the 3,400 BTC return; coinpaprika; cryptoticker; airdropalert. '
 u'<b>&#9733; The biggest security number of the day had no CVE, no patch and no deadline &mdash; a page organised around '
 u'vulnerability tables has to have somewhere to put that, or it will quietly leave it out.</b></span></p></div>')
s=rep(s,u'<h2 class="sec">Breaches &amp; Incidents</h2>\n<div class="cards"><div class="card">',
      u'<h2 class="sec">Breaches &amp; Incidents</h2>\n'+CARD+u'<div class="card">',1,"cy-card")

BOD=(u'risk-based windows that replace the uniform clock of <b>BOD 22-01</b>. <b>This page&rsquo;s own description of that older '
 u'clock was wrong, and it is corrected in this 6:35&nbsp;PM edition.</b> <span class="mut">It read &ldquo;BOD 22-01&rsquo;s '
 u'uniform three weeks.&rdquo; Returns read this run describe the old directive instead as <b>14 days for vulnerabilities '
 u'assigned a CVE after 2021 and six months for older ones</b> &mdash; two windows, neither of them three weeks &mdash; while a '
 u'separate return says CISA in practice set KEV due dates <b>two to three weeks</b> from the add date, which is the likeliest '
 u'origin of the shorthand and is <b>not</b> the same claim as the directive text. <b>BOD 26-04 was issued 10 June 2026</b> and '
 u'scores each asset&ndash;vulnerability pair on <b>four variables</b> &mdash; <b>public exposure, KEV status, exploit automation '
 u'and technical impact</b> &mdash; into <b>one of five remediation tiers</b>, running from <b>three-day action with forensic '
 u'triage</b> down to <b>deferral until a future system upgrade</b>; the windows named are <b>3, 14 or 60 calendar days</b>, and '
 u'agency policies had to support ongoing remediation by <b>7 August 2026</b>. CISA&rsquo;s directive page for BOD 22-01 is '
 u'<b>titled as revoked</b> in the returns. <b>None of these pages was fetched first-hand</b> &mdash; Tenable, FedTech Magazine, '
 u'Action1, runZero, Qualys, Flashpoint and FOSSA are search returns &mdash; and <b>no deadline printed below moved on the '
 u'strength of them</b>: the 5, 14, 16 and 18 September dates stand exactly as attributed. <b>&#9733; A tidy one-line summary of '
 u'a policy is the easiest thing on a page to inherit without checking, and this one had been inherited for editions.</b></span></p>')
s=rep(s,u'risk-based windows that supersede BOD 22-01&rsquo;s uniform three weeks.</p>',BOD,1,"cy-bod")

SRC=(u'<h2 class="sec">Sources</h2><p class="note" style="margin:-2px 0 10px"><b>New in this 6:35&nbsp;PM ET edition, none '
 u'fetched first-hand:</b> <span class="mut">for the Liquid Network item &mdash; '
 u'<a href="https://www.coindesk.com/markets/2026/09/07/bitcoin-network-used-by-exchanges-hit-by-usd320-million-exploit-hackers-claim-they-re-the-good-guys">'
 u'CoinDesk, 7 September &mdash; $320 million bitcoin exploit hits Liquid Network</a> &middot; '
 u'<a href="https://news.bitcoin.com/security/liquid-hackers-return-3400-btc-keep-47m-as-network-stays-frozen/">Bitcoin.com News '
 u'&mdash; hackers return 3,400 BTC, keep $47M as network stays frozen</a> &middot; '
 u'<a href="https://coinpaprika.com/news/liquid-halts-white-hat-hackers-take-4000-btc/">coinpaprika &mdash; Liquid halts as '
 u'&ldquo;white-hat&rdquo; hackers take 4,000 BTC worth $320M</a> &middot; '
 u'<a href="https://cryptoticker.io/en/liquid-network-hack-bitcoin-drained-white-hat-blockstream/">cryptoticker</a> &middot; '
 u'<a href="https://airdropalert.com/blogs/liquid-network-hack/">airdropalert</a>. '
 u'For the BOD 26-04 correction &mdash; <a href="https://www.tenable.com/blog/cisa-bod-26-04-FAQ-vulnerability-remediation-impact">'
 u'Tenable &mdash; what BOD 26-04 means for vulnerability remediation</a> &middot; '
 u'<a href="https://fedtechmagazine.com/article/2026/09/how-cisa-bod-26-04-changing-risk-based-vulnerability-management-perfcon">'
 u'FedTech Magazine &mdash; BOD 26-04 is changing risk-based vulnerability management</a> &middot; '
 u'<a href="https://www.action1.com/blog/cisa-bod-26-04-why-the-72-hour-patching-window-may-be-too-long/">Action1</a> &middot; '
 u'<a href="https://www.runzero.com/blog/bod-26-04/">runZero &mdash; a new era of prioritized remediation</a> &middot; '
 u'<a href="https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk">CISA &mdash; BOD 26-04 '
 u'directive page (listed as a pointer; not read this run)</a> &middot; '
 u'<a href="https://www.cisa.gov/news-events/directives/bod-22-01-reducing-significant-risk-known-exploited-vulnerabilities-revoked">'
 u'CISA &mdash; BOD 22-01, titled as revoked (pointer; not read this run)</a>. '
 u'<b>Nothing was fetched first-hand in this edition</b>: the ESPN champions page and a CISA alert page were both attempted and '
 u'returned <b>empty bodies</b>, as on every previous attempt, so every sentence added here rests on search returns and says so.'
 u'</span></p>')
s=rep(s,u'<h2 class="sec">Sources</h2>',SRC,1,"cy-src")

LED_CY=(u'<p class="note" style="margin:-2px 0 10px"><b>New-tag ledger &mdash; 2 tags on this page in this 6:35&nbsp;PM ET edition, '
 u'and they are the only tags anywhere on the site.</b> <span class="mut">The single <b>6:05&nbsp;PM</b> tag &mdash; the '
 u'<b>CVE-2026-51693 / TOTOLINK T6</b> row &mdash; is stripped to <b>Carried</b>. <b>Two tags are applied here</b>: the '
 u'<b>Liquid Network</b> incident card and the <b>BOD 26-04</b> correction, which is also the first tag this desk has applied to '
 u'a correction of its own prior text rather than to an outside event. Ledger across the three briefings: <b>2</b> cyber + '
 u'<b>0</b> markets + <b>0</b> MMA = <b>2</b>, against <b>1</b> in the <b>6:05&nbsp;PM</b> snapshots &mdash; a larger total and a '
 u'different distribution, which is the self-test. Every tagged string was proved <b>absent</b> from the <b>2026-09-07-1813</b> '
 u'snapshots before the tag was applied: <b>Liquid</b>, <b>Blockstream</b>, <b>4,000 BTC</b>, <b>598.5</b>, <b>peg-out</b>, '
 u'<b>3 / 14 / 60</b> and <b>five tiers</b> from <code>archive/cyber-2026-09-07-1813.html</code>. <b>BOD 26-04</b> itself was '
 u'proved <b>present</b> in that snapshot and is deliberately <i>not</i> what is tagged &mdash; the page has named the directive '
 u'for editions; what is new is its mechanics and the correction of what it replaced. On the markets page every figure the sweep '
 u'returned &mdash; <b>Brent $97.89</b>, <b>WTI $92.30</b>, the <b>162,000</b> payrolls print against <b>53,000</b> expected and '
 u'the <b>58%</b> hike odds &mdash; was proved <b>present</b> in <code>archive/wallstreet-2026-09-07-1813.html</code>, and on the '
 u'MMA page <b>Tracy Cortez</b>, <b>UFC&nbsp;329</b>, <b>14-fight</b>, <b>Namajunas</b>, <b>Mick Parkin</b> and <b>Johnny Walker</b> '
 u'were proved present in <code>archive/mma-2026-09-07-1813.html</code>, which is why both report zero. '
 u'&#9733; <b>A ledger that can only ever tag outside events will never record the run in which the page fixed itself.</b></span></p>')
s=re.subn(r'<p class="note"[^>]*><b>New-tag ledger.*?</p>',lambda m:LED_CY,s,count=1,flags=re.S)
if s[1]!=1: FAIL.append("cy-ledger not replaced")
s=s[0]
wr(CY,s)

# ---------- 3. WALL STREET ----------
s=rd(WS)
WS_TLDR=(u'<b>Nothing on this page is new in this 6:35&nbsp;PM edition &mdash; the sweep returned only material it already '
 u'carries, so <b>no New tag is attached anywhere on it</b> &mdash; and the only thing that has moved is the clock:</b> the '
 u'<b>6:00 PM ET</b> CME reopen is now <b>about three quarters of an hour in the past</b>, and the <b>1:00 PM ET</b> '
 u'equity-index halt is a <b>closed five-hour interval</b> that ended with it. <b>No level is asserted for the reopened tape</b> '
 u'&mdash; no return read at this desk gives a post-reopen price for any symbol, and a tape that has started moving is not a tape '
 u'anyone here has read. The sweep re-confirmed <b>Brent $97.89</b> and <b>WTI $92.30</b> for <b>7 September</b>, both already '
 u'carried and both <b>below</b> the <b>$97.93</b> touch, and the <b>162,000</b> August payrolls print against <b>53,000</b> '
 u'expected with <b>58%</b> odds on a hike, also already carried. <b>The one thing that was new in the 6:05&nbsp;PM edition was '
 u'that same clock, at the moment it crossed over:</b>')
s=rep(s,u'<b>The one thing that is new in the 6:05&nbsp;PM edition is the clock, and it has crossed over:</b>',WS_TLDR,1,"ws-tldr")
s=rep(s,u'<b>has now happened</b>, minutes before this edition publishes, so',
      u'<b>had just happened</b>, minutes before that edition published, so',1,"ws-tldr2")
s=rep(s,u'As this <b>6:05&nbsp;PM</b> edition publishes, the 1:00&nbsp;PM ET halt is <b>about five hours in the past</b>, and for the first time today it is <b>no longer the event this page is counting from</b>. <b>The reopen has happened.</b> <b>5:00 p.m. CT is 6:00 PM ET</b>, and this edition publishes <b>minutes after it</b> &mdash;',
      u'As this <b>6:35&nbsp;PM</b> edition publishes, the <b>6:00 PM ET</b> reopen is itself <b>about three quarters of an hour '
      u'in the past</b> and the <b>1:00&nbsp;PM ET</b> halt is <b>about five and a half hours</b> behind this edition &mdash; the '
      u'<b>ninth consecutive edition</b> in which this clock has had to be rewritten, and the first in which the number that '
      u'matters is measured from the reopen rather than from the halt. <b>5:00 p.m. CT is 6:00 PM ET</b> &mdash;',1,"ws-body")
s=s.replace(u"thirty-third consecutive edition",u"thirty-fourth consecutive edition")
LED_WS=(u'<p class="note" style="margin:-2px 0 10px"><b>New-tag ledger &mdash; 0 tags on this page in this 6:35&nbsp;PM ET '
 u'edition.</b> <span class="mut">Site-wide the ledger reads <b>2</b> cyber + <b>0</b> markets + <b>0</b> MMA = <b>2</b>, against '
 u'<b>1</b> in the <b>6:05&nbsp;PM</b> snapshots. Every figure this run&rsquo;s market sweep returned was proved <b>present</b> in '
 u'<code>archive/wallstreet-2026-09-07-1813.html</code> before being dismissed: <b>Brent $97.89</b>, <b>WTI $92.30</b>, '
 u'<b>162,000</b>, <b>53,000</b>, <b>58%</b>, <b>Kospi</b> and <b>3.09</b>. The two cyber tags are the <b>Liquid Network</b> '
 u'incident and a correction to that page&rsquo;s own account of the federal patching clock. &#9733; <b>A page whose only moving '
 u'part is a clock should say that plainly rather than dress the clock up as news.</b></span></p>')
s=re.subn(r'<p class="note"[^>]*><b>New-tag ledger.*?</p>',lambda m:LED_WS,s,count=1,flags=re.S)
if s[1]!=1: FAIL.append("ws-ledger not replaced")
s=s[0]
wr(WS,s)

# ---------- 4. MMA ----------
s=rd(MM)
s=rep(s,u'<b>There is no new development in the 6:05&nbsp;PM edition either &mdash; a <b>fourth</b> consecutive sweep returned only material this page already carries</b>',
      u'<b>There is no new development in this 6:35&nbsp;PM edition either &mdash; a <b>fifth</b> consecutive sweep returned only material this page already carries</b>',1,"mma-tldr1")
MMA_NEW=(u'<b>The stale-champions trap fired again in this 6:35&nbsp;PM edition, for a second consecutive edition and on the same '
 u'three belts.</b> A champions list read this run again seats <b>Alex Pereira</b> at light heavyweight, <b>Khamzat Chimaev</b> at '
 u'middleweight and <b>Valentina Shevchenko</b> at women&rsquo;s flyweight. <b>All three are refused.</b> The board below carries '
 u'<b>Carlos Ulberg</b>, <b>Sean Strickland</b> and a <b>vacant</b> women&rsquo;s flyweight belt, and the tell is internal to the '
 u'return: a list still seating Shevchenko cannot be current for a card this page names in full above it, <b>UFC&nbsp;332</b>, '
 u'which exists <i>because</i> that belt is vacant. <b>The other eight lines matched this board exactly</b> &mdash; Aspinall, '
 u'Makhachev, <b>Gaethje</b> (&ldquo;won title June 14, 2026&rdquo;), Volkanovski, Yan, Van, Harrison and Dern &mdash; and are '
 u'printed as corroboration. <b>&#9733; Eight right lines still do not make the other three right; this is the third firing of '
 u'this trap today.</b> The sweep also re-confirmed detail this page already carries and therefore does not tag: <b>Silva&rsquo;s '
 u'14-fight win streak</b> with wins over <b>Rose Namajunas</b>, <b>Alexa Grasso</b> and <b>Jessica Andrade</b> in her last three, '
 u'<b>Wang Cong&rsquo;s</b> four straight, most recently over <b>Tracy Cortez</b> at <b>UFC&nbsp;329</b> in July, and <b>Johnny '
 u'Walker&rsquo;s</b> heavyweight debut against <b>Mick Parkin</b> on the same card. ')
s=rep(s,u'<span class="mut"><b>One word is in dispute and it is printed rather than settled.</b>',
      MMA_NEW+u'<span class="mut"><b>One word is in dispute and it is printed rather than settled.</b>',1,"mma-tldr2")
LED_MM=(u'<p class="note" style="margin:-2px 0 10px"><b>New-tag ledger &mdash; 0 tags on this page in this 6:35&nbsp;PM ET edition, '
 u'a fifth consecutive zero.</b> <span class="mut">Site-wide the ledger reads <b>2</b> cyber + <b>0</b> markets + <b>0</b> MMA = '
 u'<b>2</b>, against <b>1</b> in the <b>6:05&nbsp;PM</b> snapshots. Every token this run&rsquo;s UFC sweeps returned was proved '
 u'<b>present</b> in <code>archive/mma-2026-09-07-1813.html</code> before being dismissed: <b>Tracy Cortez</b>, <b>UFC&nbsp;329</b>, '
 u'<b>14-fight</b>, <b>Namajunas</b>, <b>Mick Parkin</b>, <b>Johnny Walker</b> and <b>CBS</b>. The champions board is unchanged and '
 u'was re-checked cell by cell against the three regressions a list returned this run tried to reinstate. &#9733; <b>Zero is a '
 u'finding when it is proved; it is only an absence when it is assumed.</b></span></p>')
s=re.subn(r'<p class="note"[^>]*><b>New-tag ledger.*?</p>',lambda m:LED_MM,s,count=1,flags=re.S)
if s[1]!=1: FAIL.append("mma-ledger not replaced")
s=s[0]
wr(MM,s)

# ---------- 5. INDEX ----------
s=rd(IX)
s=rep(s,u'<h3>A 9.8 in a TOTOLINK router joins the watch list with half its details missing &mdash; and the briefing prints which half &mdash; while a print server still owns the only live deadline</h3>',
      u'<h3>$320 million in bitcoin left a sidechain&rsquo;s federation wallet and most of it came back &mdash; and the briefing corrects its own account of the federal patching clock</h3>',1,"ix-cy-h3")
IX_CY=(u'<b>Two items are new at 6:35&nbsp;PM, and the larger one has no CVE attached to it.</b> Self-described white-hat actors '
 u'moved about <b>4,000 BTC</b> &mdash; roughly <b>$320 million</b>, close to <b>95%</b> of the reserves backing the <b>Liquid</b> '
 u'Bitcoin sidechain &mdash; out of its <b>federation wallet</b> on <b>6 September</b>; <b>Blockstream disabled the bridge nodes</b>, '
 u'pausing the network and its two-way peg. <b>3,400 BTC ($268m) has been returned</b> and about <b>598.5 BTC ($47m)</b> kept. The '
 u'&ldquo;whitehats&rdquo; label is the actors&rsquo; own, written on-chain, and nothing read confirms it; there is <b>no CVE, no '
 u'patch and no KEV entry</b>, so it carries no deadline and does not displace PaperCut as the urgent box. Two arithmetic gaps are '
 u'printed rather than smoothed: 600 against the <b>598.5</b> stated, and <b>$52m</b> against the <b>$47m</b> stated. <b>The second '
 u'new item is the briefing correcting itself:</b> it had said <b>BOD 26-04</b> replaced <b>BOD 22-01&rsquo;s uniform three weeks</b>; '
 u'returns read this run give the old clock as <b>14 days for post-2021 CVEs and six months for older ones</b>, and the new one as '
 u'<b>3, 14 or 60 calendar days</b> across <b>five risk tiers</b>. <b>No deadline on the page moved.</b> '
 u'<b>The item new at 6:05&nbsp;PM was the smallest entry on the page:</b>')
s=rep(s,u'<b>One item is new at 6:05&nbsp;PM, and it is the smallest entry on the page:</b>',IX_CY,1,"ix-cy")
s=rep(s,u'<h3>The countdown this desk has run since lunchtime hit zero: futures reopened at 6:00&nbsp;PM ET, minutes before this edition, and nobody here has read the new tape yet</h3>',
      u'<h3>Futures have been trading again for about three quarters of an hour, nobody at the desk has read the new tape, and nothing else on the markets page is new</h3>',1,"ix-ws-h3")
IX_WS=(u'<b>Nothing on the markets page is new at 6:35&nbsp;PM</b> &mdash; the sweep returned only carried material, so <b>no New tag '
 u'is attached to it</b> &mdash; and the only thing that has moved is the clock: the <b>6:00 PM ET</b> reopen is now <b>about three '
 u'quarters of an hour in the past</b>, the <b>1:00 PM ET</b> halt is a <b>closed five-hour interval</b>, and <b>no post-reopen level '
 u'is asserted for any symbol</b>. <b>The new thing at 6:05&nbsp;PM was that same clock at the moment it crossed:</b>')
s=rep(s,u'<b>The one new thing at 6:05&nbsp;PM is the clock, and it has crossed over:</b>',IX_WS,1,"ix-ws")
s=rep(s,u'<b>has now happened</b>, so the <b>1:00&nbsp;PM ET</b> equity-index halt is',
      u'<b>had just happened</b>, so the <b>1:00&nbsp;PM ET</b> equity-index halt is',1,"ix-ws2")
s=rep(s,u'<h3>A stale champions list came back with three wrong belts on it, and the briefing refused all three &mdash; while a third source finally backs its word for how Shevchenko lost hers</h3>',
      u'<h3>The same stale champions list came back with the same three wrong belts, and the briefing refused all three again &mdash; a fifth straight edition with nothing new</h3>',1,"ix-mma-h3")
s=rep(s,u'A <b>fourth</b> consecutive sweep returned nothing new',u'A <b>fifth</b> consecutive sweep returned nothing new',1,"ix-mma1")
s=rep(s,u'<b>A champions-list return arrived with three superseded belts on it</b>',
      u'<b>For a second consecutive edition a champions-list return arrived with the same three superseded belts on it</b>',1,"ix-mma2")
s=s.replace(u"thirty-third consecutive edition",u"thirty-fourth consecutive edition")
wr(IX,s)

print("FAILURES:",len(FAIL))
for f in FAIL: print(" -",f)
