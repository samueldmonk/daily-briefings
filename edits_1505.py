#!/usr/bin/env python3
"""Incremental edits: Wednesday Aug 26 2026, ~3:05 p.m. ET Midday Edition (13th run).
Builds all four pages in memory, aborts before writing if any anchor check fails."""
import re, sys, io

D = "/sessions/festive-upbeat-carson/mnt/outputs/"
def rd(f): return io.open(D+f, encoding="utf-8").read()

fails = []
def must(cond, msg):
    if not cond: fails.append(msg)

def demote(h, old="2:44"):
    h = h.replace('class="tag new">New &middot; %s</span>' % old,
                  'class="tag">Carried &middot; %s edition</span>' % old)
    h = h.replace('New at %s &mdash;' % old, 'Carried from the %s edition &mdash;' % old)
    h = h.replace('New at %s' % old, 'Carried from the %s edition' % old)
    return h

def add_source(h, li, tag):
    """Insert a <li> immediately after the <ul> that follows the last Sources label."""
    i = h.rfind('<div class="lab">Sources</div>')
    must(i > 0, tag + ": sources label missing")
    if i <= 0: return h
    u = h.find('<ul', i)
    must(u > i, tag + ": sources <ul> missing")
    if u <= i: return h
    u = h.find('>', u) + 1
    return h[:u] + "\n" + li + h[u:]

# ================================================================ WALL STREET
ws = rd("wallstreet-briefing.html")
ws = demote(ws)
must('New &middot; 2:44' not in ws, "WS: stale New tag 2:44 survived")
must('New at 2:44' not in ws, "WS: stale 'New at 2:44' survived")

m = re.search(r'<div class="tldr"><b>The Tape</b> <span>.*?</span></div>', ws, re.S)
must(m is not None, "WS: tldr not found")
if m:
    ws = ws[:m.start()] + ('<div class="tldr"><b>The Tape</b> <span>Three separate Yahoo index boards fetched this run '
 '&mdash; self-stamped ~9:59&nbsp;a.m., ~11:59&nbsp;a.m. and ~12:29&nbsp;p.m. by their own countdowns &mdash; '
 'reconcile <b>all eight of their lines each</b>, and together they show a session that <b>opened green and turned red</b>: '
 'the S&amp;P was <b>&plus;0.12%</b> at 9:59 and <b>&minus;0.15%</b> by 12:29, with the Dow, Nasdaq and Russell all '
 'following; the latest single-name strip has <b>Abercrombie &amp; Fitch &plus;40.43% at $152.93</b> and '
 '<b>Expion360 &plus;71.16% at $9.02</b>, the largest percentage move anyone has numbered today, while '
 '<b>&#9888; Bitcoin&rsquo;s implied prior close differs on all three boards</b> and one small-cap percent field '
 'does not reconcile with its own change field &mdash; both printed rather than smoothed.</span></div>') + ws[m.end():]

old_h2 = "<h2>Two widgets, one page, ninety minutes apart &mdash; and the day&rsquo;s biggest move is bigger than this desk had it</h2>"
must(old_h2 in ws, "WS: lead h2 not found")
ws = ws.replace(old_h2, "<h2>Three boards, three clocks, twenty-four clean reconciliations &mdash; and a session that opened green and turned red</h2>", 1)

lead_anchor = '<div class="lead">\n'
must(lead_anchor in ws, "WS: lead anchor missing")
NEW_LEAD = """
<p><b>&#9679; New at 3:05 &mdash; three full index boards, three different self-stamped times, and every line on every one of them reconciles.</b> Yahoo syndication pages fetched this run each carry an eight-line board headed by its own countdown to the 4&nbsp;p.m. close, which is the only clock any of them offers. TheStreet&rsquo;s Aug.&nbsp;26 syndication reads &ldquo;close in 6h 1m&rdquo; &rarr; <b>~9:59&nbsp;a.m. ET</b>; the 24/7 Wall St. page reads &ldquo;close in 4h 1m&rdquo; &rarr; <b>~11:59&nbsp;a.m.</b>; the WWD page reads &ldquo;close in 3h 31m&rdquo; &rarr; <b>~12:29&nbsp;p.m.</b> At <b>9:59</b>: <b>S&amp;P&nbsp;500 7,686.64, &plus;9.36, &plus;0.12%</b>; <b>Dow&nbsp;30 53,594.69, &plus;17.29, &plus;0.03%</b>; <b>Nasdaq 26,173.36, &plus;22.06, &plus;0.08%</b>; <b>Russell&nbsp;2000 3,007.66, &minus;2.36, &minus;0.08%</b>. At <b>11:59</b>: <b>7,670.89, &minus;6.39, &minus;0.08%</b>; <b>53,474.94, &minus;102.46, &minus;0.19%</b>; <b>26,060.89, &minus;90.41, &minus;0.35%</b>; <b>3,003.16, &minus;6.86, &minus;0.23%</b>. At <b>12:29</b>: <b>7,665.46, &minus;11.82, &minus;0.15%</b>; <b>53,425.42, &minus;151.98, &minus;0.28%</b>; <b>26,049.37, &minus;101.93, &minus;0.39%</b>; <b>3,002.26, &minus;7.76, &minus;0.26%</b>. Each of those twelve lines subtracts exactly to the Weekly Scorecard closes &mdash; <b>7,677.28 / 53,577.40 / 26,151.30 / 3,010.02</b> &mdash; and each percent equals its own points-over-prior-close. <b>The 9:59 board is the only reading all day with the three headline indices green</b>, which makes the shape of the session explicit rather than inferred: it opened higher and gave it back, and by 12:29 the Nasdaq was the worst of the four.</p>
<p><b>&#9679; New at 3:05 &mdash; the four index prior closes are now corroborated three more times, and the Zacks figure loses again.</b> All three boards above independently imply <b>7,677.28</b> for Tuesday&rsquo;s S&amp;P close, not the <b>7,677.24</b> Zacks printed and this desk declined to adopt at 2:44. The same three boards agree on <b>VIX 15.45</b> as Tuesday&rsquo;s close (15.51/&plus;0.06 at 9:59, 15.45/0.00 flat at 11:59, 15.59/&plus;0.14 at 12:29 &mdash; note the VIX crossed its own prior close during the morning), and on <b>gold&rsquo;s $4,694.50 prior close</b>, which settles the earlier gap in favour of $4,694.50 and against the ~$4,637 implied by the Motley Fool strip. Gold on the three boards: <b>$4,680.70 &minus;0.29%</b>, <b>$4,663.10 &minus;0.67%</b>, <b>$4,654.20 &minus;0.86%</b> &mdash; a steady slide through the morning. <b>WTI Oct-26 agrees on an $82.36 prior close on all three</b> and crossed it twice: <b>$81.52 &minus;1.02%</b> at 9:59, <b>$82.32 &minus;0.05%</b> at 11:59, <b>$83.14 &plus;0.95%</b> at 12:29. That sign-crossing is the explanation for the unadjudicated opposite-signed oil rows carried below &mdash; the barrel genuinely traded on both sides of Tuesday&rsquo;s close today.</p>
<p><b>&#9679; New at 3:05 &mdash; &#9888; NEW GOTCHA #51: Bitcoin has no fixed prior close, and three boards prove it.</b> The BTC line reads <b>$78,410.76, &minus;$222.59, &minus;0.28%</b> at 9:59; <b>$78,049.39, &minus;$1,457.77, &minus;1.83%</b> at 11:59; and <b>$78,056.02, &minus;$1,097.27, &minus;1.39%</b> at 12:29. Each percent equals its own change over its own implied base &mdash; but those bases are <b>$78,633.35</b>, <b>$79,507.16</b> and <b>$79,153.29</b>, three different numbers within two and a half hours. Bitcoin trades continuously, so Yahoo&rsquo;s &ldquo;previous close&rdquo; for it is a <b>rolling 24-hour reference that moves with the clock</b>, not the fixed session close that anchors an equity index. <b>RULE for this desk: never reconcile a crypto quote against a stored prior close, and never treat a shifting crypto base as evidence that a board is stale or wrong.</b> Every equity and commodity line on all three boards held its base exactly; only BTC moved.</p>
<p><b>&#9679; New at 3:05 &mdash; the latest single-name strip, and one percent field that will not reconcile.</b> The trending-ticker strip on the 24/7 Wall St. page, fetched at approximately <b>3:00&nbsp;p.m. ET</b>, reads: <b>ANF $152.93, &plus;$44.03, &plus;40.43%</b>; <b>XPON (Expion360) $9.02, &plus;$3.75, &plus;71.16%</b>; <b>INTU $339.18, &minus;$18.29, &minus;5.11%</b>; <b>META $575.47, &plus;$5.42, &plus;0.95%</b>; <b>CRE (Cre8 Enterprise) $6.40, &plus;$3.83, &plus;148.54%</b>. ANF, XPON and META reconcile exactly against $108.90, $5.27 and $570.05. <b>XPON at &plus;71.16% is the largest percentage move any source has put a number on today</b>, and it has extended on every read; <b>&#9888; no catalyst is stated by any source fetched this run and none is asserted here.</b> <b>&#9888; INTU is one cent out</b>: 339.18 &plus; 18.29 = 357.47 against the $357.46 close eleven other renderings have given, though the percent (18.29 &divide; 357.46 = 5.1166%) lands on the stated 5.11. <b>&#9888; CRE does not reconcile at all</b>: 6.40 &minus; 3.83 = 2.57, the same base every earlier CRE read implied, but 3.83 &divide; 2.57 = <b>149.03%</b>, not the 148.54% printed. The level and the change are published; <b>the source&rsquo;s percent is printed as found and flagged as internally inconsistent</b>. A second strip on the WWD page, fetched two minutes earlier, gives <b>ANF $148.96 &plus;36.78%</b> (a truncation of 36.786, not a rounding), <b>XPON $8.56 &plus;62.43%</b>, <b>INTU $341.35 &minus;4.51%</b>, <b>META $576.82 &plus;1.19%</b> and <b>CRE $6.26 &plus;145.84%</b> &mdash; where 3.69 &divide; 2.57 = 143.58%, so <b>CRE&rsquo;s percent field fails on that strip too</b>. <b>&#9888; Ordering the 3:00 strip against the 2:40 strip below is indeterminate</b>: XPON and CRE both sit above their 2:40 readings and INTU is deeper, but ANF sits 47&nbsp;cents <em>below</em> $153.40. No claim is made about which tick is later on ANF alone.</p>
"""
ws = ws.replace(lead_anchor, lead_anchor + NEW_LEAD, 1)

mv = ws.find('<div class="lab">Movers &amp; drivers</div>')
must(mv > 0, "WS: movers label missing")
ins = ws.find('<div class="card">', mv)
must(ins > mv, "WS: movers first card missing")
NEW_CARDS = """<div class="card"><div class="tags"><span class="tag new">New &middot; 3:05</span><span class="tag">&plus;40.43%</span><span class="tag">Retail</span></div>
<h3>Abercrombie: the quarter underneath the move, line by line</h3>
<p>Two accounts published this run put numbers on the quarter that produced the day&rsquo;s largest move. WWD, in a <b>12:20&nbsp;p.m. ET</b> piece built on an interview with chief executive <b>Fran Horowitz</b>, reports a <b>37 percent lift to $149.26</b> and the retailer&rsquo;s <b>15th consecutive quarter of growth</b>. For the three months ended <b>Aug.&nbsp;1</b>: net sales <b>&plus;5% to $1.3&nbsp;billion</b> from $1.2&nbsp;billion; operating income <b>$252.7&nbsp;million</b> against <b>$206.7&nbsp;million</b>; net income <b>$185.5&nbsp;million, or $4.17 a diluted share</b>, against <b>$143.4&nbsp;million, or $2.91</b>. By brand: <b>Abercrombie net sales &plus;8% with comps &plus;4%</b>; <b>Hollister net sales &plus;2% with comps &minus;3%</b>. By region: <b>Americas &plus;5%, Asia-Pacific &plus;19%, EMEA &plus;2%</b>. 24/7 Wall St. adds an <b>operating margin of 19.9% against 13.9% adjusted</b> a year earlier, <b>APAC comparable sales &plus;13%</b>, and the detail that companywide <b>comparable sales were flat</b>.</p>
<p><b>The refund, precisely.</b> The <b>~$100&nbsp;million</b> benefit is an <b>IEEPA tariff refund booked as a reduction of cost of sales</b>, contributing <b>$1.75 of the $4.17</b> and <b>220 basis points</b> of the raised margin outlook; Horowitz told WWD a further <b>~$20&nbsp;million</b> is expected. Full-year guidance goes to <b>$13.10&ndash;$13.60</b> from <b>$10.20&ndash;$11.00</b>; the third quarter is guided to <b>$2.90&ndash;$3.20 on 5&ndash;6% sales growth</b>. Horowitz attributed the Hollister comp decline to inventory rather than demand: &ldquo;<b>Truly our demand exceeded our inventory. We were chasing inventory literally all quarter.</b>&rdquo; <b>&#9888; The 24/7 article contradicts itself on the size of the move</b> &mdash; its Quick Read says the stock &ldquo;surged 34%&rdquo; while its own body says &ldquo;surging 37% to $148.91.&rdquo; <b>Neither is published as the move; the reconciling strip readings are.</b> The same piece notes ANF had been <b>down 13% year to date through Tuesday&rsquo;s close</b>, so the session is repricing a name the market had already marked down.</p></div>
<div class="card"><div class="tags"><span class="tag new">New &middot; 3:05</span><span class="tag">Retail</span><span class="tag">Same catalyst</span></div>
<h3>Three retailers, one tariff refund, three different answers</h3>
<p>24/7 Wall St., at approximately <b>11:30&nbsp;a.m. ET</b>, prices the peer group against Abercrombie&rsquo;s move: <b>Ross Stores (ROST) &minus;0.5% to $240.09</b>, its own tariff-refund quarter having landed <b>last Wednesday</b> and carried the stock to a <b>34% year-to-date gain through Tuesday&rsquo;s close</b>; <b>Kohl&rsquo;s (KSS) &plus;0.4% to $17.75</b> after reporting the same catalyst before the open, from a starting point <b>12% down year to date</b>; and the <b>SPDR S&amp;P Retail ETF (XRT) &plus;1% to $88.58</b>. The <b>SPDR S&amp;P 500 ETF (SPY) is described as practically unchanged at $765.57</b>, which is what makes this an idiosyncratic apparel repricing rather than a market move.</p>
<p><b>&#9888; Kohl&rsquo;s crossed the flat line inside ninety minutes, and both readings reconcile off the same prior close.</b> The ~9:59&nbsp;a.m. Yahoo strip carried <b>KSS $16.85, &minus;$0.83, &minus;4.69%</b>; the 11:30 figure is <b>&plus;0.40% at $17.75</b>. Both imply a <b>$17.68</b> Tuesday close (16.85 &plus; 0.83 = 17.68, and 0.83 &divide; 17.68 = 4.694%; 17.75 &minus; 17.68 = 0.07, and 0.07 &divide; 17.68 = 0.396%). <b>Both are printed as successive ticks; neither is presented as the day&rsquo;s move.</b> The interpretive line 24/7 draws &mdash; that the tariff mechanic is identical across all three names while the demand stories underneath diverge &mdash; is the publication&rsquo;s, and is carried as such.</p></div>
<div class="card"><div class="tags"><span class="tag new">New &middot; 3:05</span><span class="tag">Rejections</span><span class="tag">Method</span></div>
<h3>Two stale boards caught, and a fourth source on the Dick&rsquo;s date</h3>
<p><b>Two of the pages fetched this run served pre-session data, and neither was used.</b> Yahoo&rsquo;s Wednesday live blog returned a board headed &ldquo;U.S. markets <em>open</em> in 5h 4m&rdquo; &mdash; a <b>~4:26&nbsp;a.m. ET</b> futures snapshot (S&amp;P futures 7,687.00, Dow futures 53,701.00, Nasdaq futures 29,215.50) &mdash; with a trending strip still carrying Tuesday&rsquo;s closes. The TS2/TechStock&sup2; US live page was stamped <b>00:14 EDT</b>, i.e. overnight. <b>Neither is published as a Wednesday reading.</b></p>
<p><b>A fourth source touches the Dick&rsquo;s Sporting Goods date, and the 2:44 rejection stands.</b> TS2 carries a write-up headlined &ldquo;DICK&rsquo;S Sporting Goods tumbles 30.7% after Foot Locker selloff wipes out <b>$4.9 billion</b>&rdquo; and dates it <b>26 August</b> &mdash; but that site&rsquo;s own live clock last advanced at <b>00:14 EDT on the 26th</b>, making it an overnight write-up of <em>Tuesday&rsquo;s</em> session, consistent with Seeking Alpha, Schaeffer&rsquo;s and The Motley Fool all placing the collapse on <b>Aug.&nbsp;25</b>. <b>No Wednesday DKS figure is asserted</b>; the $4.9&nbsp;billion market-value figure is attributed to that headline and not independently confirmed.</p>
<p><b>One more name carries a clean number, from the ~9:59 board rather than from now.</b> <b>Oklo (OKLO) $44.84, &plus;$0.57, &plus;1.29%</b> against a <b>$44.27</b> Tuesday close &mdash; and that $44.27 was itself an <b>&plus;11.54%</b> Tuesday session, per the premarket strip, off a $39.69 Monday close. <b>&#9888; Both figures reconcile, but neither is a 3&nbsp;p.m. reading, and each is labelled with the time it carries.</b></p></div>
"""
if ins > mv: ws = ws[:ins] + NEW_CARDS + ws[ins:]

ws = add_source(ws, ('<li><b>&#9679; New at 3:05 &mdash; three self-stamped index boards, two trending strips, the Abercrombie quarter and the retail peer group:</b> '
 '<a href="https://finance.yahoo.com/markets/stocks/articles/abercrombie-fitch-soars-37-100m-153035394.html">Yahoo Finance / 24/7 Wall St., &ldquo;Abercrombie &amp; Fitch Soars 37% on a $100M Tariff Refund and Raised Guidance, Ross and Kohl&rsquo;s Hold Steady&rdquo; (article 11:30&nbsp;a.m. ET; board self-stamped ~11:59&nbsp;a.m.; strip fetched ~3:00&nbsp;p.m.)</a>'
 ' &middot; <a href="https://finance.yahoo.com/markets/stocks/articles/abercrombie-fitch-shares-rise-37-162036584.html">Yahoo Finance / WWD, &ldquo;Abercrombie &amp; Fitch Shares Rise 37 Percent on Q2 Sales Beat and Raised 2026 Forecast&rdquo; (article 12:20&nbsp;p.m. ET; board self-stamped ~12:29&nbsp;p.m.)</a>'
 ' &middot; <a href="https://finance.yahoo.com/markets/stocks/articles/stock-market-today-aug-26-134309776.html">Yahoo Finance / TheStreet, &ldquo;Stock Market Today (Aug. 26, 2026)&rdquo; (board self-stamped ~9:59&nbsp;a.m.; PCE detail and the Zaccarelli and Hathorn comments)</a>'
 ' &middot; <b>Fetched and rejected as current:</b> <a href="https://finance.yahoo.com/markets/live/stock-market-today-wednesday-august-26-dow-sp-500-nasdaq-081834782.html">Yahoo Finance &mdash; Wednesday live blog (premarket board)</a>'
 ' and <a href="https://ts2.tech/en/stock-market-today-08-26-2026/">TS2/TechStock&sup2; &mdash; US market live page (stamped 00:14 EDT)</a>.</li>'), "WS")

# ================================================================ CYBER
cy = rd("cyber-briefing.html")
cy = demote(cy)
must('New &middot; 2:44' not in cy, "CY: stale New tag survived")

m = re.search(r'<div class="tldr"><b>The Wire</b> <span>.*?</span></div>', cy, re.S)
must(m is not None, "CY: tldr not found")
if m:
    cy = cy[:m.start()] + ('<div class="tldr"><b>The Wire</b> <span>Boston Scientific&rsquo;s 8-K still leads &mdash; a cyber incident the '
 'company itself says has disrupted <b>its ability to process and ship customer orders worldwide</b> &mdash; and a tenth '
 'consecutive edition has produced <b>no CISA KEV alert page later than Aug.&nbsp;24</b>, so the board holds at '
 '<b>14 deadlines, 10 past due</b>, with <b>Oracle due tomorrow</b> and <b>Gitea on Friday</b>; the single item this run '
 'surfaced that was not already carried is <b>CISA&rsquo;s #StopRansomware advisory AA26-222A for Gunra ransomware</b>, '
 'added below with its own caveat, because the advisory page returned an empty body when fetched.</span></div>') + cy[m.end():]

bi = cy.find('Breaches &amp; incidents')
if bi < 0: bi = cy.find('Breaches &amp; Incidents')
must(bi > 0, "CY: breaches label missing")
ins = cy.find('<div class="card">', bi)
must(ins > bi, "CY: breaches first card missing")
CY_CARD = """<div class="card"><div class="tags"><span class="tag new">New &middot; 3:05</span><span class="tag">Ransomware</span><span class="tag">CISA advisory</span></div>
<h3>CISA has a #StopRansomware advisory out for Gunra &mdash; published here with a hard caveat</h3>
<p>The one cybersecurity item surfaced this run that is not already on this page is a <b>CISA #StopRansomware advisory carrying the identifier AA26-222A, titled &ldquo;#StopRansomware: Gunra Ransomware.&rdquo;</b> A search result returned this run characterises <b>Gunra</b> as an emerging <b>ransomware-as-a-service</b> operation and places its emergence within the August 2026 threat picture.</p>
<p><b>&#9888; The advisory page itself returned an empty body when fetched this run, so nothing beyond the advisory&rsquo;s existence, its identifier and that one-line characterisation is asserted here.</b> No affiliate names, initial-access vectors, encryption details, indicators of compromise, victim counts, sectors or dates are published, because none was read. Defenders should treat <b>CISA&rsquo;s own advisory page as the source of record</b> and read it directly rather than relying on this entry. It changes nothing in Patch Priority, which remains driven by the two KEV deadlines already on the board.</p></div>
"""
if ins > bi: cy = cy[:ins] + CY_CARD + cy[ins:]

cy = add_source(cy, ('<li><b>&#9679; New at 3:05 &mdash; the Gunra advisory, and a tenth consecutive edition with a static KEV board:</b> '
 '<a href="https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-222a">CISA, &ldquo;#StopRansomware: Gunra Ransomware&rdquo; (AA26-222A) &mdash; page returned an empty body when fetched this run</a>'
 ' &middot; <a href="https://www.cisa.gov/news-events/alerts/2026/08/24/cisa-adds-one-known-exploited-vulnerability-catalog">CISA &mdash; Aug.&nbsp;24 KEV addition (CVE-2026-21962, Oracle HTTP Server and WebLogic Server proxy plug-in); still the latest alert page found</a>'
 ' &middot; <a href="https://www.cisa.gov/news-events/alerts/2026/08/20/cisa-adds-two-known-exploited-vulnerabilities-catalog">CISA &mdash; Aug.&nbsp;20 KEV additions (TrueConf Server CVE-2026-72529 and CVE-2026-72530; already carried)</a>'
 ' &middot; <a href="https://www.cisa.gov/known-exploited-vulnerabilities-catalog">CISA &mdash; Known Exploited Vulnerabilities Catalog</a>. '
 '<b>Re-searched this run and already on the page, so nothing added:</b> the OpenSSL denial-of-service flaws, the Balonx Sistema credential-harvesting kit, the Taco Bell and Pizza Hut franchise-operator disclosure, CoreRAT, Metabase CVE-2026-72898, Cisco Secure Firewall CVE-2026-20349, Windows AFD CVE-2026-68820, the Aug.&nbsp;18 KEV batch, the miniOrange SAML SSO pair and the Adobe and Nvidia advisory waves.</li>'), "CY")

# ================================================================ MMA
mm = rd("mma-briefing.html")
mm = demote(mm)
must('New at 2:44' not in mm, "MMA: stale New marker survived")

m = re.search(r'<div class="tldr"><b>Tale of the Tape</b> <span>.*?</span></div>', mm, re.S)
must(m is not None, "MMA: tldr not found")
if m:
    mm = mm[:m.start()] + ('<div class="tldr"><b>Tale of the Tape</b> <span>Three days out from UFC Shanghai, the line on '
 '<b>Umar Nurmagomedov (20-1) vs. Song Yadong (23-9-1)</b> has now been read five different ways &mdash; '
 '&minus;470/&plus;360, &minus;700/&plus;500, &minus;500/&plus;385, &minus;500/&plus;375 on UFC.com and a consensus '
 '&minus;500/&plus;380 worth about 80% implied, all published unmerged &mdash; and the one thing added this run is the '
 '<b>full twelve-bout UFC&nbsp;331 line-up</b> for Sept.&nbsp;19 at Crypto.com Arena, with prelims at <b>6&nbsp;p.m. ET</b> '
 'and the main card at <b>9&nbsp;p.m. ET</b> on Paramount+; no card, result, signing or title change landed anywhere else, '
 'so the champions board is unchanged for a <b>twenty-fifth</b> consecutive edition.</span></div>') + mm[m.end():]

ar = mm.find('Around the sport')
if ar < 0: ar = mm.find('Around the Sport')
must(ar > 0, "MMA: around-the-sport label missing")
u = mm.find('<ul', ar)
must(u > ar, "MMA: around list missing")
MMA_LI = """<li><b>New at 3:05 &mdash; the full UFC&nbsp;331 line-up, and a main-card start time that has moved.</b> MMA Mania&rsquo;s card listing, carried by Yahoo Sports, gives twelve bouts for <b>Saturday, Sept.&nbsp;19 at Crypto.com Arena in Los Angeles</b>, streaming on <b>Paramount+</b> with <b>prelims at 6&nbsp;p.m. ET and the main card at 9&nbsp;p.m. ET</b> &mdash; the listing notes that <b>numbered UFC events have moved from a 10&nbsp;p.m. to a 9&nbsp;p.m. main-card start on Paramount+</b>. Beneath the <b>Joshua Van vs. Alexandre Pantoja 2</b> flyweight title headliner and the five-round <b>Arman Tsarukyan vs. Mauricio Ruffy</b> lightweight co-main: <b>Renato Moicano vs. Brian Ortega 2</b> (155), <b>Patricio Pitbull vs. Doo Ho Choi</b> (145), <b>Charles Jourdain vs. Marlon Vera</b> (135), <b>Ryan Gandra vs. Ozzy Diaz</b> (185), <b>Casey O&rsquo;Neill vs. Eduarda Moura</b> (125), <b>Edmen Shahbazyan vs. Brunno Ferreira</b> (185), <b>Tai Tuivasa vs. Robelis Despaigne</b> (265), <b>Gable Steveson vs. Sean Sharaf</b> (265), <b>Iwo Baraniewski vs. Alonzo Menifield</b> (205), <b>Giga Chikadze vs. Joanderson Brito</b> (145) and <b>Michael Aswell Jr. vs. Joo Sang Yoo</b> (145). <b>&#9888; The source states plainly that fight card, bout order and number of fights are subject to change</b>, and the Moicano&ndash;Ortega bout is listed as a <b>rematch</b>. Names are reproduced exactly as the listing spells them, including <b>Doo Ho Choi</b> rather than the one-word rendering a search summary returned.</li>
"""
if u > ar:
    u = mm.find('>', u) + 1
    mm = mm[:u] + "\n" + MMA_LI + mm[u:]

mm = add_source(mm, ('<li><b>&#9679; New at 3:05 &mdash; the full UFC&nbsp;331 card and its start times:</b> '
 '<a href="https://sports.yahoo.com/articles/ufc-331-fight-card-start-140351479.html">Yahoo Sports / MMA Mania, &ldquo;UFC 331 fight card, start time, date and location | Van vs. Pantoja 2&rdquo;</a>'
 ' &middot; <a href="https://www.ufc.com/event/ufc-fight-night-august-29-2026">UFC.com &mdash; UFC Fight Night: Nurmagomedov vs. Song (Shanghai, Aug.&nbsp;29)</a>. '
 '<b>Re-searched this run and already on the page, so nothing added:</b> the LowKick consensus line, the Tuesday fight-week faceoff, the Bloody Elbow Shanghai preview and the UFC.com fight-by-fight preview. '
 '<b>&#9888; A search summary again gave the Shanghai headliners as #2 and #6 in &ldquo;the latest Meta UFC rankings&rdquo;; UFC.com&rsquo;s own announcement ranks them #3 and #5, which is what this page publishes &mdash; the alternative numbering is recorded and rejected for a second time.</b></li>'), "MMA")

# ================================================================ INDEX
ix = rd("index.html")
def swap(hay, marker, new_p, tag):
    i = hay.find(marker)
    must(i > 0, tag + ": card marker missing")
    if i <= 0: return hay
    a = hay.find('<p>', i); b = hay.find('</p>', a)
    must(a > i and b > a, tag + ": card paragraph missing")
    if not (a > i and b > a): return hay
    return hay[:a] + new_p + hay[b+4:]

ix = swap(ix, 'href="cyber-briefing.html"',
 '<p>A tenth consecutive edition with <b>no CISA KEV alert page later than Aug.&nbsp;24</b>: the board holds at '
 '<b>14 deadlines, 10 past due</b>, <b>Oracle due tomorrow</b>, <b>Gitea Friday</b>. The only item not already carried '
 'is <b>CISA&rsquo;s #StopRansomware advisory AA26-222A for Gunra ransomware</b> &mdash; published with a caveat, because '
 'the advisory page returned an empty body when fetched.</p>\n', "index/cyber")
ix = swap(ix, 'href="wallstreet-briefing.html"',
 '<p>Three Yahoo index boards self-stamped <b>~9:59&nbsp;a.m.</b>, <b>~11:59&nbsp;a.m.</b> and <b>~12:29&nbsp;p.m.</b> '
 'reconcile on all eight lines each and show a session that <b>opened green and turned red</b> &mdash; the S&amp;P '
 '<b>&plus;0.12%</b> then <b>&minus;0.15%</b>. Latest strip: <b>ANF &plus;40.43%</b>, <b>XPON &plus;71.16%</b>. '
 '<b>&#9888; Bitcoin&rsquo;s implied prior close differs on all three boards.</b></p>\n', "index/ws")
ix = swap(ix, 'href="mma-briefing.html"',
 '<p>The <b>full twelve-bout UFC&nbsp;331 card</b> for Sept.&nbsp;19 at Crypto.com Arena is now on the page, with prelims '
 'at <b>6&nbsp;p.m. ET</b> and the main card at <b>9&nbsp;p.m. ET</b> on Paramount+. Shanghai is three days out with the '
 'line read five ways, all pointing at <b>Umar Nurmagomedov</b>. The champions board is unchanged for a '
 '<b>twenty-fifth</b> consecutive edition.</p>\n', "index/mma")

# ================================================================ WRITE (gated)
if fails:
    print("FAILURES — nothing written:")
    for f in fails: print(" -", f)
    sys.exit(1)
for name, body in (("wallstreet-briefing.html", ws), ("cyber-briefing.html", cy),
                   ("mma-briefing.html", mm), ("index.html", ix)):
    io.open(D+name, "w", encoding="utf-8").write(body)
print("edits_1505: OK — 4 pages written")
