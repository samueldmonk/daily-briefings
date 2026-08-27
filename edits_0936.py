import io,sys
def ed(path,pairs):
    s=io.open(path,encoding='utf-8').read()
    for i,(a,b) in enumerate(pairs):
        n=s.count(a)
        if n!=1:
            print("FAIL %s pair#%d count=%d :: %s"%(path,i,n,a[:90])); sys.exit(1)
        s=s.replace(a,b)
    io.open(path,'w',encoding='utf-8').write(s)
    print("OK",path,len(pairs),"edits")

W='wallstreet-briefing.html'; C='cyber-briefing.html'; M='mma-briefing.html'; I='index.html'

# ---------------- WALL STREET ----------------
ws=[]
ws.append((
'<div class="tldr"><b>The Tape</b> <span>Nvidia, Salesforce and CrowdStrike are all sharply higher before the bell after their results, lifting Nasdaq futures roughly 0.9%, while the 8:30 jobless-claims print came in at 203,000 — a fresh sign of a steady labour market.</span></div>',
'<div class="tldr"><b>The Tape</b> <span>The bell has rung on a tech-led tape: Nvidia, Salesforce, CrowdStrike and now Okta are all higher on their results, with Okta up more than 20% and Salesforce and CrowdStrike each up about 14% in the latest quotes seen this run.</span></div>'))

ws.append((
'<span class="tag new">New · 9:05 AM ET</span><span class="tag acc">Pre-open</span>\n<h3>Three earnings beats and a 203,000 claims print carry the tape into the open</h3>',
'<span class="tag new">New · 9:35 AM ET</span><span class="tag acc">Just after the open</span>\n<h3>Four earnings beats open the tape, with Okta the biggest mover — as of ~9:35 AM ET</h3>'))

ws.append((
'<p style="margin:0 0 10px">With about half an hour to the open, the tape is led by technology and the lead has narrowed rather than broadened. Yahoo Finance\'s Thursday-morning read has <b>Nasdaq 100 futures up 0.9%</b>, <b>S&amp;P 500 futures up 0.4%</b> and <b>Dow futures hovering near the flat line</b> — a step back from the <b>8:40 AM ET</b> read this page carried 25 minutes earlier, when all three were green and Dow contracts were up <b>0.23%</b>. Bloomberg separately reported S&amp;P 500 contracts up about <b>1%</b> in early Thursday trade after CFO <b>Colette Kress</b> signalled strong sales growth into fiscal 2028. The two headline ETF proxies tell the same story: <b>QQQ +1.04%</b> against <b>SPY +0.4%</b>.</p>',
'<p style="margin:0 0 10px">The regular session is open. Yahoo Finance\'s Thursday live coverage has US stocks <b>climbing</b> after results from Nvidia, Salesforce and CrowdStrike lifted the technology trade, with the <b>S&amp;P 500 up 0.4%</b>, the <b>Nasdaq Composite up about 1%</b> and the <b>Dow hovering near the flat line</b>.</p>\n<p style="margin:0 0 10px" class="note" style2=""><span style="color:var(--mut)"><b>A caution this page is placing on its own index figures.</b> Those three readings are numerically identical to the pre-open futures reads carried in the 9:05 edition (Nasdaq 100 futures +0.9%, S&amp;P 500 futures +0.4%, Dow near flat), and no source fetched this run stamped them with a post-open time. They are therefore printed as the latest available index reads, <b>not</b> asserted as prices struck after the 9:30 bell. The single-stock quotes below <i>have</i> moved off their pre-market levels, which is the evidence that live trading is being quoted.</span></p>'))

ws.append((
'<p style="margin:0 0 10px">The move is not confined to Nvidia, and it is not confined to semiconductors. <b>Nvidia rose 7.4%</b> in pre-market trade, <b>Marvell Technology 5.8%</b> and <b>Micron 4.5%</b>, while the <b>VanEck Semiconductor ETF jumped 3.5%</b> and the <b>iShares Semiconductor ETF gained 3%</b>. Software and security joined in: <b>Salesforce climbed nearly 12%</b> and <b>CrowdStrike about 8.9%</b> pre-open on their own results, with <b>Okta</b> also among the morning\'s risers.</p>',
'<p style="margin:0 0 10px"><b>The leadership has rotated away from Nvidia since the pre-market.</b> The latest quotes seen this run have <b>Okta up more than 20%</b>, <b>Salesforce up 14.78%</b> and <b>CrowdStrike up 14.34%</b> — each well above its pre-open read — while <b>Nvidia is up 5.87%</b>, <i>below</i> the 6% to 7.4% range quoted before the bell. In other words the software and identity names have extended and the chip that caused the rally has given a little back. Earlier in the pre-market the read-through had hit the whole semiconductor complex: <b>Marvell Technology +5.8%</b>, <b>Micron +4.5%</b>, the <b>VanEck Semiconductor ETF +3.5%</b> and the <b>iShares Semiconductor ETF +3%</b>.</p>'))

# Movers cards
ws.append((
'<h3>Nvidia (NVDA) — up sharply pre-market</h3><p>Three reads this morning, all printed and none averaged: <b>Reuters/AOL has NVDA up 7.4%</b>, <b>Benzinga has it up 7.32%</b> and <b>CNBC has it up 6%</b> in pre-market trade. Wednesday evening\'s first post-call read was "more than 4%" in extended trading. The driver is the $108 billion third-quarter guide and Huang\'s fiscal-2028 growth comment.</p>',
'<h3>Nvidia (NVDA) — up 5.87%, off its pre-market high</h3><p>The latest quote seen this run has <b>NVDA up 5.87%</b>. That is <i>below</i> every pre-market read this page carried an hour ago — <b>7.4%</b> (Reuters/AOL), <b>7.32%</b> (Benzinga) and <b>6%</b> (CNBC) — and above Wednesday evening\'s first post-call read of "more than 4%" in extended trading. All four figures are printed and none averaged. The driver is unchanged: the <b>$108 billion</b> third-quarter guide and Huang\'s fiscal-2028 growth comment.</p>'))

ws.append((
'<h3>Salesforce (CRM) — up nearly 12% pre-open</h3><p>Shares jumped <b>nearly 12%</b> in pre-market trade on Thursday.',
'<h3>Salesforce (CRM) — up 14.78%, extending past its pre-market gain</h3><p>The latest quote seen this run has <b>CRM up 14.78%</b>, above the <b>nearly 12%</b> it was showing in pre-market trade.'))

ws.append((
'<span style="color:var(--mut)">An "adjusted EPS of $5.90 versus $3.27 expected" line has now appeared in pre-market coverage two runs running. It is still not published here: a beat of that magnitude is far more likely a mismatched consensus figure than a real result, and no company filing confirming it has been fetched.</span>',
'<span style="color:var(--mut)">An "adjusted EPS of $5.90 versus $3.27 expected" line has now appeared in coverage <b>three runs running</b>, and it is still not published here — but the reasoning has weakened and this page says so. The original objection was that a beat of that magnitude is more likely a mismatched consensus figure than a result. In the same movers feed this run, <b>Abercrombie &amp; Fitch</b> is reported at <b>$4.17</b> against a <b>$1.99</b> estimate — a beat of very similar proportion — which suggests the feed may be comparing against an estimate on a different basis rather than simply being wrong. Absent a company filing fetched here, the figure is still withheld rather than asserted.</span>'))

ws.append((
'<h3>CrowdStrike (CRWD) — the quarter now has numbers</h3><p>Fiscal second-quarter 2027 revenue, for the quarter ended <b>July 31</b>, rose <b>26%</b> year over year to <b>$1.47 billion</b>, ahead of a <b>$1.44 billion</b> consensus, with adjusted EPS of <b>$0.31</b> against <b>$0.29</b> expected. The company <b>raised its full-year outlook</b>. Shares were up about <b>8.9%</b> pre-open, having closed Wednesday at <b>$189.18, up 2.05%</b>, and traded <b>10.49% higher at $209.02</b> in the after-hours session. HP (HPQ) is also on the earnings watchlist this morning.</p>',
'<h3>CrowdStrike (CRWD) — up 14.34%, with a record ARR quarter</h3><p>The latest quote seen this run has <b>CRWD up 14.34%</b>, well beyond the <b>8.9%</b> it showed pre-open. Fiscal second-quarter 2027 revenue, for the quarter ended <b>July 31</b>, rose <b>26%</b> year over year to <b>$1.47 billion</b>, ahead of a <b>$1.44 billion</b> consensus, with adjusted EPS of <b>$0.31</b> against <b>$0.29</b> expected, and the company <b>raised its full-year outlook</b>. New this run: the headline metric was <b>net new annual recurring revenue of a record $333 million, up 51%</b> from a year earlier. Shares closed Wednesday at <b>$189.18, up 2.05%</b>, and traded <b>10.49% higher at $209.02</b> after hours. HP (HPQ) is also on the earnings watchlist this morning.</p>'))

ws.append((
'<div class="card"><span class="tag new">New</span><span class="tag acc">Identity</span>\n<h3>Okta (OKTA) — joins the earnings risers</h3><p>Okta appears alongside Nvidia, Salesforce and CrowdStrike in Thursday\'s biggest-movers coverage, with Yahoo Finance\'s earnings live blog describing Salesforce, CrowdStrike and Okta shares as surging as the AI boom lifted second-quarter results. <b>No pre-market percentage for Okta was stated in the sources seen this run, so none is printed.</b></p></div>',
'<div class="card"><span class="tag new">Updated · 9:35</span><span class="tag acc">Identity</span>\n<h3>Okta (OKTA) — up more than 20%, the session\'s biggest mover</h3><p>Okta has gone from a name this page could not put a number on to the largest single-stock move on the board: shares are <b>up more than 20%</b> after the company beat on both lines and pointed to booming demand tied to agentic AI. Adjusted earnings were <b>$1.05 per share on revenue of $805 million</b>, against the <b>97 cents</b> and <b>$795 million</b> analysts expected. Separately, <b>Bank of America upgraded Okta to Neutral from Underperform with a $170 price target</b>. <span style="color:var(--mut)">The 9:05 edition printed no percentage for Okta because none had been stated; one has now been.</span></p></div>\n\n<div class="card"><span class="tag new">New</span><span class="tag acc">Retail</span>\n<h3>Abercrombie &amp; Fitch (ANF) — a big beat and a lower share price</h3><p>ANF reported second-quarter earnings of <b>$4.17 per diluted share on $1.267 billion in sales</b>, against estimates of <b>$1.99</b> and <b>$1.248 billion</b>, and <b>raised fiscal 2026 EPS guidance to $13.10–$13.60 from $10.20–$11.00</b>. Shares nonetheless <b>fell 1.4%</b> after <b>Citi downgraded the stock to neutral from buy</b>, arguing there is limited upside left after a long run. It is the clearest counter-example on the board this morning to the idea that a beat guarantees a bid.</p></div>'))

ws.append((
'<td>Thursday pre-market read (Benzinga).</td>',
'<td>Thursday pre-market read (Benzinga). Yahoo Finance\'s Thursday coverage describes bond yields as having <b>stabilised</b> after spiking last week, with investors weighing the Treasury\'s intervention in the bond market.</td>'))

ws.append((
'<tr><td>Federal funds target range</td><td class="mono">3.50%–3.75%</td><td>Upper limit of 3.75% in August 2026; the range was left unchanged at the July meeting (Trading Economics).</td></tr>',
'<tr><td>Federal funds target range</td><td class="mono">3.50%–3.75%</td><td>Upper limit of 3.75% in August 2026; the range was left unchanged at the July meeting (Trading Economics).</td></tr>\n<tr><td>September meeting — market-implied odds</td><td class="mono">~52%</td><td>Trading Economics reports traders pricing a <b>nearly 52% chance of a rate <i>rise</i></b> in September, <b>down from 67%</b> a week earlier. Yahoo Finance\'s Thursday coverage frames the same setup from the other side, as investors weighing "the likelihood that the Fed would hold rates steady." Both framings are printed; the direction of travel in the odds is the point.</td></tr>'))

ws.append((
'<li><b>Fed policy.</b> The federal funds target range stands at <b>3.50%–3.75%</b>, left unchanged at the July meeting (Trading Economics). <span style="color:var(--mut)">A "Jackson Hole address" framing carried on this page earlier has been removed: it could not be re-confirmed for August 2026 in sources fetched this run, and the same phrasing appears in coverage from a prior year.</span></li>',
'<li><b class="crit-ish" style="color:var(--acc2)">Jackson Hole is this week, and this page was wrong to drop it.</b> The <b>2026 Jackson Hole Economic Policy Symposium runs August 27&ndash;29</b> at <b>Jackson Lake Lodge</b>, hosted by the <b>Federal Reserve Bank of Kansas City</b>, on the theme <b>"Financial Innovation: Implications for Payments and Policy,"</b> with roughly <b>120 central bankers, economists and officials from more than 70 countries</b> attending. Chair <b>Kevin Warsh</b> delivers the keynote on the <b>morning of Friday, August 28</b> — his first as Fed Chair — and is <b>not expected to give clear guidance</b> on the September decision. <span style="color:var(--mut)"><b>Correction, made in the open:</b> the 9:05 edition removed a Jackson Hole line on the reasoning that the symposium falls in the third week of August and that the phrasing had appeared in prior-year coverage. That reasoning was wrong. The symposium is a Thursday-to-Saturday event in the last full week of August, and in 2026 that is <b>this week</b>. The item is restored, and the standing corrections file has been amended so the mistake is not repeated.</span></li>\n<li><b>Fed policy.</b> The federal funds target range stands at <b>3.50%–3.75%</b>, left unchanged at the July meeting (Trading Economics).</li>'))

ws.append((
'<div class="note">Pre-market activity leaned decisively toward technology and semiconductors on Thursday.',
'<div class="note">Trading has leaned decisively toward technology, software and identity names on Thursday.'))

ws.append((
'<div class="note">Nvidia is the session\'s dominant single-stock story after Wednesday evening\'s report.</div>',
'<div class="note">Nvidia set the tone for the session with Wednesday evening\'s report, though on the latest quotes it is no longer the largest mover — Okta, Salesforce and CrowdStrike are all ahead of it.</div>'))

ws.append((
'<li><a href="https://stockmarketwatch.com/live/stock-market-today">StockMarketWatch',
'<li><a href="https://www.kansascityfed.org/research/jackson-hole-economic-symposium/">Federal Reserve Bank of Kansas City — Jackson Hole Economic Symposium (2026: Aug 27&ndash;29, "Financial Innovation: Implications for Payments and Policy")</a></li><li><a href="https://www.regardsofwallstreet.com/news/jackson-hole-2026-dates-schedule-warsh-first-speech">Regards of Wallstreet — Jackson Hole 2026: Dates, Schedule, and Warsh\'s First Speech as Fed Chair (August 27&ndash;29)</a></li><li><a href="https://seekingalpha.com/news/4637302-biggest-stock-movers-thursday-nvda-okta-and-more">Seeking Alpha — Biggest stock movers Thursday: NVDA, OKTA and more</a></li><li><a href="https://finance.yahoo.com/markets/stocks/articles/thursday-top-wall-street-analyst-120136428.html">Yahoo Finance — Thursday\'s top Wall Street analyst research calls (Okta upgraded at BofA; Abercrombie &amp; Fitch downgraded at Citi)</a></li><li><a href="https://stockmarketwatch.com/live/stock-market-today">StockMarketWatch'))
ed(W,ws)

# ---------------- CYBER ----------------
cy=[]
cy.append((
'<div style="margin-top:5px;font-size:14.6px">A CVSS 10.0, unauthenticated Oracle flaw is being exploited in the wild and the federal remediation deadline lands today — while Cl0p continues to publish victims from its PTC Windchill data-theft campaign.</div>',
'<div style="margin-top:5px;font-size:14.6px">A CVSS 10.0, unauthenticated Oracle flaw is being exploited in the wild and the federal remediation deadline lands today; a <i>second</i> maximum-severity flaw, this one unauthenticated RCE in Veeam ONE, has just been disclosed and patched; and Cl0p continues to publish victims from its PTC Windchill data-theft campaign.</div>'))

cy.append(('<span class="tag new">Updated · 9:05</span><span class="tag crit">Deadline today</span>',
           '<span class="tag new">Updated · 9:35</span><span class="tag crit">Deadline today</span>'))

cy.append((
'<p style="margin:0;font-size:14.4px">This is the single most urgent item on the board: maximum severity (CVSS 10.0 per Oracle), unauthenticated and remotely reachable over HTTP, confirmed exploited by CISA, and the BOD-assigned federal remediation date expires today.',
'<p style="margin:0;font-size:14.4px">This is the single most urgent item on the board: maximum severity (CVSS 10.0 per Oracle), unauthenticated and remotely reachable over HTTP, confirmed exploited by CISA, and the BOD-assigned federal remediation date expires today. <b>It still outranks the new Veeam ONE flaw below</b>, which also scores 10.0 but has <i>no</i> reported exploitation and <i>no</i> federal deadline — exploitation plus a deadline beats severity alone.'))

cy.append((
'<div class="card"><span class="tag crit">Extortion</span><span class="tag">Manufacturing</span><span class="tag">Carried</span>\n<h3>Cl0p names 40+ Windchill victims</h3>',
'''<div class="card" style="grid-column:1/-1"><span class="tag crit">Critical vulnerability</span><span class="tag">Backup &amp; monitoring</span><span class="tag new">New</span>
<h3>Veeam patches a CVSS 10.0 unauthenticated RCE in Veeam ONE</h3><p>Veeam has fixed a set of vulnerabilities in <b>Veeam ONE</b>, its monitoring and reporting platform. The most severe, <span class="mono">CVE-2026-64633</span>, carries a <b>CVSS v4.0 score of 10.0</b> — the maximum — because it allows <b>remote, unauthenticated code execution on the Veeam ONE agent host</b>. Affected builds are <b>Veeam ONE 13.0.2.6723 and all earlier version 13 releases</b>; the fix is <b>Veeam ONE 13.1.0.7034</b>, described in Veeam knowledge-base article <b>KB4892</b>. Separately, <span class="mono">CVE-2026-65641</span>, <b>CVSS v4.0 9.3</b>, lets a remote unauthenticated attacker force the Veeam ONE service to initiate an <b>SMB authentication attempt</b> — a classic credential-relay primitive; Veeam disclosed it in <b>KB4905, published August 25, 2026</b>, and credited a report via HackerOne. The wider update set also addresses flaws allowing sensitive-file access, database data theft and privilege escalation. <b>No source seen this run reports exploitation in the wild, and neither CVE appears in the KEV additions verified this run</b>, so no federal deadline is stated. <span style="color:var(--mut)">(Cybersecurity News, GBHackers, Veeam KB4892 / KB4905)</span></p></div>

<div class="card"><span class="tag crit">Ransomware</span><span class="tag">AI-assisted</span><span class="tag new">New</span>
<h3>Aurora ransomware affiliate used an AI coding assistant</h3><p><b>Aurora</b> ransomware has been tied to a <b>Russian-speaking affiliate</b> that used an <b>AI coding assistant</b> while targeting <b>more than 20 organisations</b>. <span style="color:var(--mut)">No victim names, sectors or ransom figures were stated in the reporting seen this run, so none are printed. (Cybersecurity News)</span></p></div>

<div class="card"><span class="tag crit">Extortion</span><span class="tag">Leak site</span><span class="tag new">New</span>
<h3>Displaydata named on a ransomware leak site</h3><p>Electronic-shelf-label maker <b>Displaydata</b> has been named on a ransomware group\'s data-leak site. <span style="color:var(--mut)">The reporting seen this run does not name the group, quantify the stolen data or confirm the company\'s response, and none of that is asserted here. (Cybersecurity News)</span></p></div>

<div class="card"><span class="tag crit">Extortion</span><span class="tag">Manufacturing</span><span class="tag">Carried</span>
<h3>Cl0p names 40+ Windchill victims</h3>'''))

cy.append((
'<tr><td class="mono">CVE-2026-12569</td>',
'<tr><td class="mono">CVE-2026-64633</td><td class="mono" style="color:var(--crit)">10.0 (CVSS v4.0)</td><td>Veeam ONE 13.0.2.6723 and all earlier v13 builds</td><td>Remote <b>unauthenticated</b> code execution on the Veeam ONE agent host. Fixed in <b>13.1.0.7034</b> (Veeam KB4892). No reported exploitation; not in KEV as of this run.</td></tr>\n<tr><td class="mono">CVE-2026-65641</td><td class="mono">9.3 (CVSS v4.0)</td><td>Veeam ONE</td><td>Remote unauthenticated attacker can coerce the Veeam ONE service into an SMB authentication attempt. Disclosed in Veeam KB4905, published <b>Aug 25, 2026</b>; reported via HackerOne.</td></tr>\n<tr><td class="mono">CVE-2026-12569</td>'))

cy.append((
'<li><b>Aug 26 batch — new this run</b> — <b>six</b> vulnerabilities added: <span class="mono">CVE-2015-3246</span>, <span class="mono">CVE-2015-5287</span>, <span class="mono">CVE-2019-1068</span>, <span class="mono">CVE-2021-23758</span>, <span class="mono">CVE-2022-0995</span> and <span class="mono">CVE-2026-8452</span>. Five of the six are legacy CVEs from 2015&ndash;2022, a reminder that KEV additions are driven by observed exploitation, not by disclosure date. No due dates verified this run.</li>',
'<li><b>Aug 26 batch</b> — <b>six</b> vulnerabilities added: <span class="mono">CVE-2015-3246</span>, <span class="mono">CVE-2015-5287</span>, <span class="mono">CVE-2019-1068</span>, <span class="mono">CVE-2021-23758</span>, <span class="mono">CVE-2022-0995</span> and <span class="mono">CVE-2026-8452</span> — the last of which the CISA alert identifies as a <b>Citrix NetScaler ADC and NetScaler Gateway</b> improper-restriction-of-memory-buffer flaw. Five of the six are legacy CVEs from 2015&ndash;2022, a reminder that KEV additions are driven by observed exploitation, not by disclosure date. No due dates verified this run.</li>'))

cy.append((
'<li><a href="https://tech.co/news/data-breaches-updated-list">',
'<li><a href="https://cybersecuritynews.com/multiple-veeam-one-vulnerabilities/">Cybersecurity News — Multiple Veeam ONE Vulnerabilities Allow Code Execution Attacks (CVE-2026-64633, CVSS 10.0)</a></li><li><a href="https://gbhackers.com/critical-veeam-one-flaw-2/">GBHackers — Critical Veeam ONE Flaw Lets Unauthenticated Attackers Coerce SMB Authentication (CVE-2026-65641, CVSS 9.3)</a></li><li><a href="https://www.veeam.com/kb4892">Veeam — KB4892: Vulnerabilities Resolved in Veeam ONE 13.1</a></li><li><a href="https://cybersecuritynews.com/">Cybersecurity News — front page (Aug 27, 2026: Aurora ransomware AI-assisted affiliate, Displaydata leak-site listing)</a></li><li><a href="https://tech.co/news/data-breaches-updated-list">'))
ed(C,cy)

# ---------------- MMA ----------------
mm=[]
mm.append((
'<p style="margin:0 0 10px">UFC Fight Night: Nurmagomedov vs. Song takes place <b>Saturday, August 29</b> at the <b>Shanghai Oriental Sports Center</b>, streaming exclusively on <b>Paramount+</b> in the United States.',
'<p style="margin:0 0 10px">UFC Fight Night: Nurmagomedov vs. Song takes place <b>Saturday, August 29</b> at the <b>Pudong Development Bank Shanghai Oriental Sports Center</b>, streaming exclusively on <b>Paramount+</b> in the United States.'))

mm.append((
'is on a two-fight win streak since challenging for the bantamweight title.',
'is on a two-fight win streak since challenging for the bantamweight title, and holds wins over former UFC flyweight champion <b>Deiveson Figueiredo</b>, former title challenger <b>Cory Sandhagen</b> and <b>Mario Bautista</b>.'))

mm.append((
'Because of the time difference, the card runs in the American morning: <b>prelims at 3 a.m. ET</b>, <b>main card at 6 a.m. ET</b>. Official weights for the Oriental Sports Center athletes are due on <b>August 28</b>.</p>',
'Because of the time difference, the card runs in the American morning: <b>prelims at 3 a.m. ET</b>, <b>main card at 6 a.m. ET</b> — 3 p.m. and 6 p.m. China Standard Time. Fight week is a back-to-back double: the <b>Road to UFC season 5 semifinals</b> run on <b>Friday, August 28</b> at <b>5 a.m. ET / 5 p.m. CST</b>, and UFC.com has now <b>published official weights</b> for the athletes competing at the Oriental Sports Center on August 28. <span style="color:var(--mut)">The 9:05 edition said those weights were "due on August 28"; they have since been released, and the wording is corrected rather than left standing.</span></p>'))

mm.append((
'<div class="card"><span class="tag">Carried</span><span class="tag acc">Developmental</span>',
'''<div class="card"><span class="tag new">New</span><span class="tag acc">Main event booked</span>
<div class="mono" style="color:var(--acc2);font-size:12px;letter-spacing:.08em;margin-bottom:6px">SAT SEP 12 · NOCHE UFC</div>
<h3>Noche UFC: Silva vs. Delgado</h3>
<p>A new main event has been announced for <b>Noche UFC</b> on <b>September 12</b>: <b>Jean Silva vs. Jos&eacute; Miguel Delgado</b>, streaming on <b>Paramount+</b>.<br><span style="color:var(--mut)">No venue, weight class or odds were stated in the announcement seen this run, so none are printed.</span></p></div>

<div class="card"><span class="tag">Carried</span><span class="tag acc">Developmental</span>'''))

mm.append((
'<li><b>Broadcast.</b> Both UFC Shanghai and Contender Series season 10 stream exclusively on <b>Paramount+</b> in the United States. Shanghai\'s start times are set by the time difference: prelims <b>3 a.m. ET</b>, main card <b>6 a.m. ET</b>.</li>',
'<li><b>Broadcast.</b> UFC Shanghai, Contender Series season 10 and the newly announced <b>Noche UFC</b> main event all stream on <b>Paramount+</b> in the United States. Shanghai\'s start times are set by the time difference: prelims <b>3 a.m. ET</b>, main card <b>6 a.m. ET</b>. The <b>Road to UFC season 5 semifinals</b> on <b>Friday, August 28</b> air at <b>5 a.m. ET</b> on <b>UFC Fight Pass</b>.</li>\n<li><b>A Contender Series signee gets his debut date.</b> <b>Bilal Hasan</b>, who earned a UFC contract in week 1 of Contender Series season 10 on August 11, is <b>preparing for his UFC debut at UFC Shanghai</b> on Saturday.</li>'))

mm.append((
'UFC Shanghai and Dana White\'s Contender Series both run on Paramount+ in the US; UFC 331 fills the Crypto.com Arena in Los Angeles on September 19 with a 13-fight card.',
'UFC Shanghai, Dana White\'s Contender Series and the September 12 Noche UFC main event all run on Paramount+ in the US; UFC 331 fills the Crypto.com Arena in Los Angeles on September 19 with a 13-fight card.'))
ed(M,mm)

# ---------------- INDEX ----------------
ix=[]
ix.append((
'<h3>Oracle\'s CVSS 10.0 WebLogic proxy flaw hits its federal deadline today</h3>\n<p>CISA\'s federal deadline to patch the maximum-severity Oracle WebLogic Proxy flaw CVE-2026-21962 — CVSS 10.0 and confirmed under active exploitation — expires today, August 27.</p>',
'<h3>Oracle\'s CVSS 10.0 WebLogic proxy flaw hits its federal deadline today</h3>\n<p>CISA\'s federal deadline to patch the maximum-severity Oracle WebLogic Proxy flaw CVE-2026-21962 — CVSS 10.0 and confirmed under active exploitation — expires today, August 27, and a second maximum-severity flaw has just been patched in Veeam ONE.</p>'))
ix.append((
'<h3>Earnings beats and a 203,000 claims print lead the tape into the open</h3>\n<p>Nvidia, Salesforce and CrowdStrike are all sharply higher before the bell after their results, lifting Nasdaq futures roughly 0.9%, while the 8:30 jobless-claims print came in at 203,000 — a fresh sign of a steady labour market.</p>',
'<h3>Four earnings beats open the tape, and Okta is the biggest mover</h3>\n<p>The bell has rung on a tech-led tape: Nvidia, Salesforce, CrowdStrike and now Okta are all higher on their results, with Okta up more than 20% and Salesforce and CrowdStrike each up about 14% in the latest quotes seen this run.</p>'))
ix.append((
'<h3>Shanghai fight week: Nurmagomedov vs. Song for the next title shot</h3>\n<p>It is fight week in Shanghai: bantamweight contenders Umar Nurmagomedov and Song Yadong headline Saturday\'s card at the Oriental Sports Center, with Nurmagomedov roughly a −500 favourite and Yan Xiaonan vs. Denise Gomes in the co-main.</p>',
'<h3>Shanghai fight week: Nurmagomedov vs. Song for the next title shot</h3>\n<p>It is fight week in Shanghai: bantamweight contenders Umar Nurmagomedov and Song Yadong headline Saturday\'s card at the Oriental Sports Center, with Nurmagomedov roughly a −500 favourite, and a new Noche UFC main event has been booked for September 12.</p>'))
ed(I,ix)
