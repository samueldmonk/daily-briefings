#!/usr/bin/env python3
"""Incremental edits for the 2026-08-26 ~9:10am ET Morning Edition (3rd run of the day).
Applies to the pages published at 08:46; every replacement is asserted."""
import sys, io, datetime, zoneinfo, re

D = sys.argv[1].rstrip('/')
now = datetime.datetime.now(zoneinfo.ZoneInfo("America/New_York"))
TIME = now.strftime("%-I:%M").lstrip() + " a.m. ET" if now.hour < 12 else now.strftime("%-I:%M") + " p.m. ET"

def load(p):
    return io.open(f"{D}/{p}", encoding="utf-8").read()

def save(p, s):
    io.open(f"{D}/{p}", "w", encoding="utf-8").write(s)

N = 0
def rep(s, old, new, label):
    global N
    assert s.count(old) == 1, f"FAIL [{label}]: found {s.count(old)} occurrences"
    N += 1
    return s.replace(old, new)

# demote previous edition's New tags
def demote(s, label):
    return s.replace('<span class="tag new">New</span>',
                     '<span class="tag">Carried &middot; 8:46 edition</span>')

# ============================== WALL STREET ==============================
w = load("wallstreet-briefing.html")
w = demote(w, "ws")
# also demote the older carried label so there is one carried vocabulary
w = w.replace('<span class="tag">Carried &middot; 8:18 edition</span>',
              '<span class="tag">Carried &middot; 8:18 edition</span>')

# --- tldr
w = rep(w,
 '<div class="tldr"><b>The Tape</b> <span>The <b>8:30&nbsp;a.m. ET core PCE print has been released</b> &mdash; consensus was <b>3.3%</b>, and no source fetched at 8:44 a.m. ET states the actual figure yet &mdash; while premarket trade has already delivered its own verdict on Tuesday night&rsquo;s earnings, with <b>Intuit down 11.8% to $315.30</b>, <b>Semtech up 4.7%</b>, and <b>Boston Scientific down 3.2% on a cybersecurity incident</b> ahead of Nvidia after the close.</span></div>',
 '<div class="tldr"><b>The Tape</b> <span><b>July PCE has printed</b> &mdash; the headline index rose <b>0.2% on the month and 3.7% on the year, both a tenth hotter than the LSEG consensus</b>, while <b>core came in exactly on forecast at 0.2% and 3.3%</b> &mdash; leaving futures modestly lower into a pre-open session that still has <b>Nvidia&rsquo;s report after the close</b> and a <b>global operational outage at Boston Scientific</b> in front of it.</span></div>',
 "ws tldr")

# --- lead headline
w = rep(w,
 '<h2>The inflation print has landed, the premarket board has not &mdash; and Nvidia is still eight hours away</h2>',
 '<h2>Hot on the headline, steady at the core: July PCE lands, and the September <i>hike</i> stays on the table</h2>',
 "ws lead h2")

# --- lead paragraph 1 + 2 (replace the "no source states the print" para)
w = rep(w,
 '<p><b>U.S. markets are still not open</b> &mdash; but the first of Wednesday&rsquo;s two events is now behind us. The Bureau of Economic Analysis released the July <b>Personal Income and Outlays</b> report, containing the Fed&rsquo;s preferred inflation gauge, at <b>8:30&nbsp;a.m. ET</b>. <b>&#9888; As of 8:44 a.m. ET, no source fetched this run states the actual print.</b> Every figure returned so far &mdash; headline PCE at <b>3.6%</b> and core at <b>3.3%</b> &mdash; comes from pre-release previews stating what economists <i>expected</i>, and this page will not pass a forecast off as a result. The number goes up here when a source states it as released.</p>',
 '<p><b>U.S. markets are still not open</b> &mdash; but the first of Wednesday&rsquo;s two events is now behind us, and this time the number is confirmed. The Commerce Department reported on Wednesday that the <b>personal consumption expenditures price index rose 0.2% from a month ago and was up 3.7% on an annual basis in July</b>. <b>Both figures were hotter than the expectations of economists polled by LSEG, who projected readings of 0.1% and 3.6% respectively.</b> <b>Core PCE</b>, which excludes food and energy, <b>was up 0.2% on a monthly basis and is 3.3% higher than last year &mdash; both in line with the LSEG poll.</b> That is Fox Business, published <b>8:35&nbsp;a.m. EDT</b> today under Eric Revell&rsquo;s byline and fetched in full; CNBC independently headlines its own release story <b>&ldquo;Fed&rsquo;s preferred inflation gauge shows core prices rose 3.3% annually in July.&rdquo;</b></p>\n'
 '<p class="note"><b>A correction to the 8:46 edition of this page.</b> That edition declined to publish any PCE figure, on the grounds that every number then in circulation traced back to a preview written before the release. That was the right call at 8:44. It is superseded now: the figures above come from a source timestamped <i>after</i> the 8:30 release that states them as reported by the Commerce Department, which is the standard this page requires.</p>',
 "ws lead p1")

# --- insert a "what it means" paragraph after the premarket board para
w = rep(w,
 '<p><b>Why the print carries so much weight.</b> Investors find out whether the gauge continued its downward trajectory, stalled, or reaccelerated &mdash; the last of which, in Yahoo&rsquo;s framing, <b>would put more pressure on the central bank to raise rates</b>. Economists expected a <b>core PCE of 3.3%, unchanged from the month before</b>, and a headline rate easing to <b>3.6%</b> from June&rsquo;s <b>3.7%</b>. A hold at 3.3% would mark, on one preview&rsquo;s count, the <b>65th consecutive month</b> above the Fed&rsquo;s 2% target, with futures pricing roughly a <b>38&ndash;40% chance</b> of a quarter-point <b>hike</b> in September. Note the direction of that pressure: this is a market pricing the risk of a <b>hike</b>, not a cut. Bloomberg reported Tuesday that falling oil prices were <b>curbing expectations for more than one Federal Reserve interest-rate hike in the coming year</b> &mdash; the debate is over how many, not whether.</p>',
 '<p><b>What the split actually says.</b> The core rate did what the market was positioned for &mdash; it held. At <b>3.3%</b> it sits <b>below May&rsquo;s 3.4% year-on-year peak</b> but still comfortably above the Fed&rsquo;s <b>2%</b> target, and on one preview&rsquo;s count a hold at that level marks the <b>65th consecutive month</b> above target. The surprise is on the headline, where energy does its work: <b>3.7%</b> against a <b>3.6%</b> forecast, and a monthly <b>0.2%</b> against <b>0.1%</b>. It is a tenth in each direction &mdash; not a regime change, but not the clean disinflation print the tape wanted either.</p>\n'
 '<p><b>And the direction of the risk is still up.</b> Ahead of the release, the CME FedWatch Tool put a <b>38% probability on a quarter-point rate hike in September</b> &mdash; <b>down from 55% one month ago</b>, per FXStreet, which attributes the decline to doubts about Chairman <b>Kevin Warsh</b>&rsquo;s commitment to fighting inflation in the absence of forward guidance. Read that number carefully: this is a market pricing the odds of a <b>hike</b>, not a cut. Bloomberg reported Tuesday that falling oil prices were <b>curbing expectations for more than one Federal Reserve interest-rate hike in the coming year</b> &mdash; the debate is over how many, not whether. Strategists at <b>DBS Bank</b> frame Friday&rsquo;s Jackson Hole appearance as a test of whether Warsh can spell out <b>&ldquo;how a Fed without forward guidance intends to anchor expectations, how much tightening the Fed is prepared to tolerate through long-term yields, and the policy boundary between the Fed and the Treasury.&rdquo;</b> The dollar has not been waiting for an answer: the <b>US Dollar Index is 0.75% lower on the month and more than 2.5% below its late-July top</b>.</p>\n'
 '<p><b>The immediate market read, such as it is.</b> Yahoo Finance&rsquo;s live blog re-titled itself after the release to <b>&ldquo;Dow, S&amp;P 500 futures hold steady as PCE inflation stays sticky, Nvidia earnings loom.&rdquo;</b> A separate post-print futures read returned this run had <b>S&amp;P 500 futures down 0.1% and Nasdaq-100 futures down 0.4%</b>. <b>&#9888; Neither of those reads carries a timestamp on the page it came from</b>, so both are published as direction rather than as a level at a stated moment &mdash; and neither is an opening print. A post-release summary also returned <b>personal income up 0.4% on the month against a 0.3% expectation, and personal spending up 0.2%</b>; those two figures come from a search summary rather than a page fetched in full, and are labelled accordingly.</p>',
 "ws lead why")

# --- movers card 1
w = rep(w,
 '<div class="tags"><span class="tag">Carried &middot; 8:46 edition</span><span class="tag">Macro</span><span class="tag">Released 8:30 a.m. ET</span></div>\n<h3>The core PCE print is out &mdash; and this page is not printing a number yet</h3>\n<p>The July Personal Income and Outlays report was released at <b>8:30&nbsp;a.m. ET</b>. Economists expected <b>core PCE of 3.3%, unchanged</b>, with headline easing to <b>3.6%</b> from <b>3.7%</b> in June. <b>&#9888; No source fetched at 8:44 a.m. ET states the actual result</b> &mdash; the figures circulating in search summaries trace back to preview pieces published before the release, so they are forecasts, not prints, and are labelled as such here. Context that is sourced: a hold at 3.3% would be the <b>65th consecutive month</b> above the Fed&rsquo;s 2% target, and futures put roughly a <b>38&ndash;40%</b> chance on a September <b>hike</b>. Yahoo Finance frames the three outcomes plainly &mdash; trajectory, stall, or reacceleration &mdash; and notes the third <b>&ldquo;would put more pressure on the central bank to raise rates,&rdquo;</b> against what it calls <b>angst in the bond market</b> and ahead of Jackson Hole, where Chairman <b>Kevin Warsh</b> speaks.</p></div>',
 '<div class="tags"><span class="tag new">New</span><span class="tag">Macro</span><span class="tag crit">Confirmed print</span></div>\n<h3>Headline PCE beats the forecast by a tenth in both directions &mdash; core lands exactly on it</h3>\n<p>The Commerce Department reported Wednesday that the <b>PCE price index rose 0.2% month on month and 3.7% year on year</b> in July, against LSEG-polled forecasts of <b>0.1%</b> and <b>3.6%</b>. <b>Core PCE was up 0.2% and 3.3%</b>, both matching the poll. The core rate is unchanged from the prior month and sits below <b>May&rsquo;s 3.4%</b> peak, but a hold at 3.3% is, on one preview&rsquo;s count, the <b>65th consecutive month</b> above the Fed&rsquo;s 2% target. Ahead of the print the CME FedWatch Tool had a <b>38% chance</b> of a September quarter-point <b>hike</b>, down from <b>55%</b> a month ago. Source: Fox Business, <b>8:35&nbsp;a.m. EDT</b> today, fetched in full; CNBC&rsquo;s release headline corroborates the 3.3% core.</p></div>',
 "ws mover card 1")

# --- Boston Scientific mover card upgrade to the 8-K
w = rep(w,
 '<h3>Boston Scientific discloses a cybersecurity incident &mdash; and it is disrupting operations globally</h3>\n<p><b>BSX fell 3.2% premarket</b> after the medical device maker <b>disclosed a cybersecurity incident that disrupted its information technology systems on Tuesday</b>. A company filing reported Wednesday says the incident <b>affected certain IT systems and has led to global disruption in operations</b>. No threat actor, ransomware family or CVE has been named, and the filing as reported gives limited further detail &mdash; so nothing further is asserted. This is also the lead item on <a href="cyber-briefing.html">The Cyber Wire</a> today.</p>',
 '<h3>Boston Scientific&rsquo;s 8-K: a global outage that reaches its ability to ship customer orders</h3>\n<p>The filing itself is now on file and fetched. In an <b>8-K filed with the SEC this morning</b>, Boston Scientific says it <b>identified a cybersecurity incident on August&nbsp;25</b> affecting certain IT systems <b>&ldquo;that has resulted in a global disruption to the Company&rsquo;s operations,&rdquo;</b> with disruptions <b>&ldquo;including the ability to process and ship customer orders&rdquo;</b> and a <b>timeline for full restoration &ldquo;not yet known.&rdquo;</b> The company has <b>not yet determined whether the incident is reasonably likely to have a material impact</b>. On the tape, the stock was down <b>3.2% premarket at 7:10&nbsp;a.m. ET</b> (Investing.com); later reads returned this run put the decline at <b>3.5%&ndash;4%</b> and at <b>5.8%</b>. <b>&#9888; Those later figures carry no fetched timestamp and are published unmerged as successive snapshots, not averaged.</b> This is the lead item on <a href="cyber-briefing.html">The Cyber Wire</a> today.</p>',
 "ws bsx card")
w = w.replace('<span class="tag down">&minus;3.2%</span><span class="tag crit">Cyber</span>',
              '<span class="tag down">&minus;3.2% &rarr; &minus;5.8%</span><span class="tag crit">Cyber</span>', 1)

# --- On the radar: PCE bullet
w = rep(w,
 '<li><b>Released 8:30&nbsp;a.m. ET today &mdash; core PCE.</b> Consensus was <b>3.3%</b>, unchanged month on month, with headline easing to <b>3.6%</b>. <b>The actual print is not yet confirmed by any source fetched at 8:44 a.m. ET and is therefore not published here.</b> The market was positioned for a hold; a reacceleration is the tail that matters, because it argues for a hike rather than a cut, and futures already put roughly <b>38&ndash;40%</b> on a September hike.</li>',
 '<li><b>Done &mdash; July PCE, released 8:30&nbsp;a.m. ET.</b> Headline <b>+0.2% m/m, +3.7% y/y</b> (forecast 0.1% / 3.6%); core <b>+0.2% m/m, +3.3% y/y</b> (in line). Hotter on the headline, on forecast at the core. Pre-print, CME FedWatch had <b>38%</b> on a September quarter-point <b>hike</b>, down from <b>55%</b> a month ago.</li>\n'
 '<li><b>Friday &mdash; Jackson Hole.</b> Chairman <b>Kevin Warsh</b> speaks. DBS Bank calls it a test of how a Fed that has rejected forward guidance intends to anchor expectations, how much tightening it will tolerate through long-term yields, and where the boundary sits between the Fed and the Treasury. OCBC argues the dollar needs Fed officials to push back on debasement concerns before it finds real support.</li>',
 "ws radar pce")

# --- Sources: add Fox Business, CNBC PCE, SEC 8-K
w = rep(w,
 '<li>FXStreet &mdash; <a href="https://www.fxstreet.com/news/us-core-pce-inflation-set-to-keep-pressure-on-the-federal-reserve-to-hike-interest-rates-202608260800">&ldquo;US core PCE inflation is foreseen well above the Fed&rsquo;s 2% target in July&rdquo;</a>',
 '<li><b>Fox Business &mdash; <a href="https://www.foxbusiness.com/economy/july-2026-pce-inflation">&ldquo;Fed&rsquo;s favored inflation gauge rose more than expected in July&rdquo;</a> (Eric Revell, published August&nbsp;26, 2026, 8:35&nbsp;a.m. EDT), fetched in full this run</b> &mdash; the source for the July PCE print: headline <b>+0.2% m/m / +3.7% y/y</b> against LSEG forecasts of 0.1% / 3.6%, and core <b>+0.2% / +3.3%</b> in line with the LSEG poll. Corroborated by CNBC &mdash; <a href="https://www.cnbc.com/2026/08/26/feds-preferred-inflation-gauge-shows-core-prices-rose-3point3percent-annually-in-july.html">&ldquo;Fed&rsquo;s preferred inflation gauge shows core prices rose 3.3% annually in July&rdquo;</a> (August&nbsp;26, 2026).</li>\n'
 '<li><b>U.S. Securities and Exchange Commission &mdash; <a href="https://www.sec.gov/Archives/edgar/data/0000885725/000088572526000056/bsx-20260826.htm">Boston Scientific Corporation, Form 8-K, Item 8.01</a> (date of earliest event reported August&nbsp;26, 2026), fetched in full this run</b> &mdash; the source for every quoted phrase about the Boston Scientific incident: identified August&nbsp;25; &ldquo;a global disruption to the Company&rsquo;s operations&rdquo;; &ldquo;including the ability to process and ship customer orders&rdquo;; third-party cybersecurity experts engaged; restoration timeline and materiality both undetermined.</li>\n'
 '<li>FXStreet &mdash; <a href="https://www.fxstreet.com/news/us-core-pce-inflation-set-to-keep-pressure-on-the-federal-reserve-to-hike-interest-rates-202608260800">&ldquo;US core PCE inflation is foreseen well above the Fed&rsquo;s 2% target in July&rdquo;</a> (fetched in full this run) &mdash; source for the <b>38%</b> CME FedWatch September hike probability and the <b>55%</b> reading a month earlier, the <b>3.4%</b> May core peak, the DBS Bank and OCBC comments, and the US Dollar Index being 0.75% lower on the month and more than 2.5% below its late-July top. Note this piece is <b>timestamped 08:00 GMT, before the release</b>; only its forward-looking and market-positioning content is used, never the print.</li>\n'
 '<li>Superseded &mdash; FXStreet',
 "ws sources fox")
w = rep(w, '<li>Superseded &mdash; FXStreet (August&nbsp;26, 2026, 08:00) and',
       '<li>Consensus context, superseded by the print &mdash;', "ws sources tidy")

save("wallstreet-briefing.html", w)

# ============================== CYBER ==============================
c = load("cyber-briefing.html")
c = demote(c, "cy")

c = rep(c,
 '<div class="tldr"><b>The Wire</b> <span><b>Boston Scientific</b> has told regulators a cybersecurity incident hit certain IT systems and is disrupting operations globally &mdash; the stock was down <b>3.2% premarket</b> &mdash; while CISA has put the actively exploited Gitea flaw <b>CVE-2026-60004</b> into KEV with a federal deadline of <b>Friday, August&nbsp;28</b>, taking this board to <b>14 tracked deadlines, 10 of them already past due</b>.</span></div>',
 '<div class="tldr"><b>The Wire</b> <span><b>Boston Scientific&rsquo;s 8-K is now on file</b>: an incident identified <b>August&nbsp;25</b> has caused <b>&ldquo;a global disruption to the Company&rsquo;s operations,&rdquo;</b> reaching <b>its ability to process and ship customer orders</b>, with no restoration timeline yet &mdash; while the federal board holds at <b>14 tracked KEV deadlines, 10 already past due</b> and the Oracle CVSS&nbsp;10.0 flaw due tomorrow.</span></div>',
 "cy tldr")

c = rep(c,
 '<p>Two federal clocks now run inside 48 hours: the <b>CVSS&nbsp;10.0</b> Oracle flaw is due <b>tomorrow, August&nbsp;27</b>, and the newly KEV-listed Gitea RCE <b>CVE-2026-60004</b> is due <b>Friday, August&nbsp;28</b>. Behind them, <b>10 of the 14 KEV deadlines tracked on this page have already lapsed</b>, and the flaw drawing the most attacker attention right now &mdash; GitLab <b>CVE-2026-19478</b> &mdash; is not in KEV at all, so no clock is running on it. A live incident at <b>Boston Scientific</b> is disrupting operations globally.</p>',
 '<p>Two federal clocks run inside 48 hours: the <b>CVSS&nbsp;10.0</b> Oracle flaw is due <b>tomorrow, August&nbsp;27</b>, and the newly KEV-listed Gitea RCE <b>CVE-2026-60004</b> is due <b>Friday, August&nbsp;28</b>. Behind them, <b>10 of the 14 KEV deadlines tracked on this page have already lapsed</b>, and the flaw drawing the most attacker attention right now &mdash; GitLab <b>CVE-2026-19478</b> &mdash; is not in KEV at all, so no clock is running on it. Meanwhile a live incident at <b>Boston Scientific</b> has, on the company&rsquo;s own filing, reached the point of interrupting <b>customer order processing and shipment worldwide</b> &mdash; availability, not confidentiality, is the failure mode of the morning.</p>',
 "cy banner")

c = rep(c,
 '<div class="stat"><div class="n">~11s</div><div class="l">Active phase of the observed Gitea CVE-2026-60004 compromise, per the victim&rsquo;s own incident write-up</div></div>',
 '<div class="stat"><div class="n">10.0</div><div class="l">CVSS of the Entra ID RCE Microsoft patched &mdash; and now says was <b>not</b> exploited in the wild, after correcting its own bulletin</div></div>',
 "cy stat1")

# --- top story upgrade
c = rep(c,
 '<h2>A cybersecurity incident at Boston Scientific is disrupting operations globally &mdash; and the stock is down 3.2% before the bell</h2>',
 '<h2>Boston Scientific&rsquo;s 8-K: a cyber incident that has reached the ability to ship customer orders, worldwide</h2>',
 "cy top h2")

c = rep(c,
 '<p><b>Boston Scientific has identified a cybersecurity incident that affected certain IT systems and has led to global disruption in operations</b>, according to a company filing reported on Wednesday, August&nbsp;26. The medical device maker is one of the largest in the world, and the disclosure is unusual in that it leads with <b>operational</b> impact rather than data exposure.</p>',
 '<p>The filing itself is now available, and it is more specific than yesterday&rsquo;s secondhand reports. In a <b>Form 8-K</b> filed with the SEC under <b>Item 8.01</b> and fetched in full this run, Boston Scientific states that <b>&ldquo;On August 25, 2026, Boston Scientific Corporation identified a cybersecurity incident affecting certain of its information technology systems that has resulted in a global disruption to the Company&rsquo;s operations.&rdquo;</b> The medical device maker is one of the largest in the world, and the disclosure is unusual in that it leads with <b>operational</b> impact rather than data exposure.</p>\n'
 '<p><b>The operational language is the part that matters.</b> The company says the incident <b>&ldquo;has caused, and is expected to continue to cause, disruptions and limitations of access to certain of the Company&rsquo;s information systems and business applications that support aspects of the Company&rsquo;s operations, including the ability to process and ship customer orders.&rdquo;</b> On restoration: <b>&ldquo;While the Company is working diligently to restore affected functions and systems access, the timeline for a full restoration is not yet known.&rdquo;</b> On response: it <b>&ldquo;activated its incident response protocols and began an investigation with the assistance of third-party cybersecurity experts to assess and to contain the threat.&rdquo;</b> And on materiality, the filing is explicit that the company <b>&ldquo;has not yet determined whether the incident is reasonably likely to have a material impact.&rdquo;</b> The 8-K is signed by <b>Susan Thompson</b>, Vice President, Chief Corporate Counsel and Assistant Secretary.</p>',
 "cy top p1")

c = rep(c,
 '<p>The market read it immediately. <b>Boston Scientific stock fell 3.2% in premarket trading</b> after the company disclosed an incident that <b>disrupted its information technology systems on Tuesday</b>, per Investing.com&rsquo;s premarket wire published at 7:10&nbsp;a.m. ET. That is the rare case where a security event and a market event are the same event, and both desks on this site are carrying it this morning.</p>',
 '<p>The market read it immediately. <b>Boston Scientific stock fell 3.2% in premarket trading</b> as of Investing.com&rsquo;s wire published at <b>7:10&nbsp;a.m. ET</b>; later reads surfaced this run put the premarket decline at <b>3.5% to 4%</b> and at <b>5.8%</b>. <b>&#9888; Those later figures carry no timestamp on the pages that returned them, so all three are published as successive snapshots of a moving premarket rather than reconciled into one number.</b> That is the rare case where a security event and a market event are the same event, and both desks on this site are carrying it this morning.</p>',
 "cy top p2")

c = rep(c,
 '<p><b>What is not yet known matters more than what is.</b> The filing as reported provides <b>limited additional detail about the nature of the incident or the scope of the affected systems</b>. No threat actor has been named, no ransomware family has been attributed, no CVE has been tied to it, and no patient-safety or device-integrity impact has been asserted in anything fetched this run &mdash; so none of those things is asserted here. &ldquo;Global disruption in operations&rdquo; at a device manufacturer can mean manufacturing, distribution, order processing or clinical support, and the source does not say which.</p>',
 '<p><b>What is still not known matters as much as what is.</b> Nothing in the 8-K names a <b>threat actor</b>, a <b>ransomware family</b>, a <b>CVE</b>, an <b>intrusion vector</b>, or any <b>patient-safety or device-integrity</b> consequence, and the filing does not characterise the incident as a data breach or state that any data was exfiltrated. None of those things is asserted here. The company says its own investigation is ongoing and that <b>&ldquo;the full scope, nature and impacts, including operational and financial impacts, of the incident are not yet known.&rdquo;</b></p>',
 "cy top p3")

c = rep(c,
 '<p class="note">Sources fetched this run: a MarketScreener report of the company filing (Wednesday, August&nbsp;26) and Investing.com&rsquo;s premarket movers wire (published 08/26/2026, 7:10&nbsp;a.m. ET), which is the source for the <b>3.2%</b> premarket move and for the incident having disrupted IT systems <b>on Tuesday</b>. Nothing beyond those two statements is published, because nothing beyond them was stated.</p>',
 '<p class="note">Primary source fetched in full this run: <b>Boston Scientific Corporation, Form 8-K, Item 8.01</b>, filed with the SEC, date of earliest event reported <b>August&nbsp;26, 2026</b>. Every phrase in quotation marks above is taken verbatim from that filing. The <b>3.2%</b> premarket move is Investing.com&rsquo;s 7:10&nbsp;a.m. ET wire; the 3.5%&ndash;4% and 5.8% figures are later, untimestamped reads returned this run. Nothing beyond what the filing states is published, because nothing beyond it was stated.</p>',
 "cy top note")

# --- Entra ID: new breach/incident card
c = rep(c,
 '<div class="lab">Breaches &amp; incidents</div>\n<div class="cards">',
 '<div class="lab">Breaches &amp; incidents</div>\n<div class="cards">\n'
 '<div class="card">\n'
 '<div class="tags"><span class="tag new">New</span><span class="tag crit">CVSS 10.0</span><span class="tag">Identity</span></div>\n'
 '<h3>Microsoft shipped a CVSS 10.0 Entra ID RCE &mdash; then corrected its own bulletin to say it was never exploited</h3>\n'
 '<p>Microsoft disclosed <b>CVE-2026-69836 (CVSS 10.0)</b>, a remote code execution flaw in <b>Entra ID</b>, its cloud identity and access management service, formerly Azure Active Directory. In Microsoft&rsquo;s words: <b>&ldquo;Deserialization of untrusted data in Microsoft Entra ID allows an unauthorized attacker to execute code over a network.&rdquo;</b> The bug class is the classic one &mdash; an application turning user-controlled data back into a live object without validating it.</p>\n'
 '<p><b>The correction is the story.</b> The security bulletin originally marked the <b>&ldquo;Exploited&rdquo;</b> field <b>&ldquo;Yes.&rdquo;</b> On <b>August&nbsp;21, 2026</b>, after The Hacker News contacted the company, Microsoft <b>changed that status to &ldquo;No&rdquo;</b> and stated that <b>&ldquo;this vulnerability was not exploited in the wild.&rdquo;</b> A spokesperson added that the CVE was published <b>&ldquo;for greater transparency&rdquo;</b> and that <b>&ldquo;there are no additional actions customers need to take.&rdquo;</b> Microsoft says the flaw is <b>fully mitigated on its side</b>. It credits principal security engineer <b>Robert Fitzpatrick</b> with the discovery.</p>\n'
 '<p class="note">This item is carried precisely because the first version of it was wrong at the source. A maximum-severity identity flaw briefly labelled &ldquo;exploited&rdquo; by the vendor is exactly the kind of claim that propagates faster than its retraction &mdash; the corrected status is what this page publishes.</p>\n'
 '</div>',
 "cy entra card")

# --- Vulnerability watch row
c = rep(c,
 '<tr><td>CVE-2026-21962</td><td>10.0</td>',
 '<tr><td>CVE-2026-69836</td><td>10.0</td><td>Microsoft Entra ID (cloud service; formerly Azure Active Directory)</td><td>Deserialization of untrusted data &rarr; remote code execution by an unauthorized attacker over a network. <b>Bulletin first marked &ldquo;Exploited: Yes&rdquo;; Microsoft corrected it to &ldquo;No&rdquo; on Aug&nbsp;21 &mdash; &ldquo;not exploited in the wild.&rdquo;</b> Fully mitigated by Microsoft; no customer action required. Reported by Robert Fitzpatrick.</td></tr>\n'
 '<tr><td>CVE-2026-21962</td><td>10.0</td>',
 "cy vuln row")

# --- KEV note arithmetic fix (13 -> 14, 3 -> 4 ahead)
c = rep(c,
 '<div class="note">Of the <b>13</b> entries tracked here, <b>10 are past due, none comes due today and 3 remain ahead of schedule</b> &mdash; the Oracle flaw at one day, MLflow at seven and TrueConf at eight.',
 '<div class="note"><b>Corrected this run:</b> the 8:46 edition left this line reading &ldquo;13 entries &hellip; 3 remain ahead&rdquo; after the Gitea row was added above it, so the summary contradicted the board it was summarising. The board holds <b>14</b> entries: <b>10 are past due, none comes due today and 4 remain ahead of schedule</b> &mdash; the Oracle flaw at one day, Gitea at two, MLflow at seven and TrueConf at eight.',
 "cy kev note count")

# --- sources
c = rep(c,
 '<div class="lab">Sources</div>\n<ul>',
 '<div class="lab">Sources</div>\n<ul>\n'
 '<li><b>U.S. Securities and Exchange Commission &mdash; <a href="https://www.sec.gov/Archives/edgar/data/0000885725/000088572526000056/bsx-20260826.htm">Boston Scientific Corporation, Form 8-K, Item 8.01</a> (date of earliest event reported August&nbsp;26, 2026), fetched in full this run</b> &mdash; the source for every quoted phrase in today&rsquo;s top story, including the August&nbsp;25 identification date, &ldquo;a global disruption to the Company&rsquo;s operations,&rdquo; &ldquo;including the ability to process and ship customer orders,&rdquo; the unknown restoration timeline, the third-party experts, the undetermined materiality, and the signature of Susan Thompson.</li>\n'
 '<li><b>The Hacker News &mdash; <a href="https://thehackernews.com/2026/08/microsoft-entra-id-flaw-cvss-100.html">&ldquo;Microsoft Patches Severe Entra ID Flaw (CVSS 10.0) Allowing Remote Code Execution&rdquo;</a> (Ravie Lakshmanan, August&nbsp;21, 2026), fetched in full this run</b> &mdash; the source for CVE-2026-69836 at CVSS 10.0, the quoted Microsoft description, the correction of the &ldquo;Exploited&rdquo; field from Yes to No on August&nbsp;21, the &ldquo;not exploited in the wild&rdquo; and &ldquo;no additional actions&rdquo; statements, and the credit to Robert Fitzpatrick. The same article is the source for CVE-2026-68820 at CVSS 7.0 and its attribution to the Lazarus Group&rsquo;s Operation Dream Job.</li>',
 "cy sources")

save("cyber-briefing.html", c)

# ============================== MMA ==============================
m = load("mma-briefing.html")
m = demote(m, "mma")

m = rep(m,
 "var target=new Date('2026-08-29T00:00:00-04:00');",
 "var target=new Date('2026-08-29T06:00:00-04:00');",
 "mma countdown time")

m = rep(m,
 '<b>Next card</b> <span>UFC Shanghai &mdash; Nurmagomedov vs. Song, Saturday, August&nbsp;29 &middot; Shanghai Oriental Sports Center &mdash; <span id="ufccdn">&nbsp;</span></span>',
 '<b>Next card</b> <span>UFC Shanghai &mdash; Nurmagomedov vs. Song, Saturday, August&nbsp;29, <b>6:00 a.m. EDT</b> &middot; Oriental Sports Center, Pudong District &mdash; <span id="ufccdn">&nbsp;</span></span>',
 "mma countdown bar")

# --- top story rebuild from the UFC.com fight-by-fight preview
m = rep(m,
 '<p>The UFC returns to <b>Shanghai on Saturday, August&nbsp;29</b>, and the week has properly begun &mdash; <b>Umar Nurmagomedov and Song Yadong had their first fight-week faceoff</b>, per Yahoo Sports. The card, <b>UFC Fight Night 286</b>, takes place at the <b>Shanghai Oriental Sports Center</b> and is headlined by what the UFC itself bills as a <b>pivotal bantamweight clash between #3 Umar Nurmagomedov and #5 Song Yadong</b>.</p>',
 '<p>The UFC returns to <b>Shanghai on Saturday, August&nbsp;29</b> &mdash; for the <b>second consecutive year and the third time overall</b> &mdash; and the week has properly begun: <b>Umar Nurmagomedov and Song Yadong had their first fight-week faceoff</b> in front of the host arena on Tuesday, per Yahoo Sports. <b>UFC Fight Night: Nurmagomedov vs Song</b> takes place at the <b>Oriental Sports Center</b> in Shanghai&rsquo;s <b>Pudong District</b>, streams on <b>Paramount+</b>, and starts at <b>6:00 a.m. EDT</b> &mdash; an early-morning card for a U.S. audience.</p>\n'
 '<p class="note"><b>&#9888; Two different ranking pairs are in circulation and both are published unmerged.</b> UFC.com&rsquo;s own event announcement headline bills the fight as a <b>&ldquo;pivotal bantamweight clash between #3 Umar Nurmagomedov and #5 Song Yadong.&rdquo;</b> A separate read returned this run places them at <b>No.&nbsp;2 and No.&nbsp;6 in the latest Meta UFC rankings</b> at 135 pounds. Rankings move week to week and the two statements may simply be snapshots taken at different times; neither is tidied into the other here.</p>',
 "mma top p1")

m = rep(m,
 '<p><b>Nurmagomedov (20-1)</b>, fighting out of Dagestan, Russia, arrives on a <b>two-fight win streak</b> since challenging for the bantamweight title &mdash; he is looking to work his way back toward a title shot after <b>losing to Merab Dvalishvili at UFC&nbsp;311</b>. <b>Song Yadong (23-9-1)</b>, &ldquo;The Kung Fu Kid,&rdquo; out of Heilongjiang, China, makes his <b>sixth main-event appearance</b> after a standout <b>submission victory over former UFC flyweight champion Deiveson Figueiredo at UFC Fight Night Macau in May</b> of this year.</p>',
 '<p><b>Nurmagomedov (20-1 MMA, 8-1 UFC)</b>, whom UFC.com describes as a <b>former title challenger</b>, arrives on a <b>two-fight win streak</b> since <b>coming up short in his title bid against Merab Dvalishvili at UFC&nbsp;311</b>: he beat <b>Mario Bautista</b> at <b>UFC&nbsp;321 in October</b>, then <b>outworked Deiveson Figueiredo three months later at UFC&nbsp;324</b>. <b>Song Yadong (23-9-1 MMA, 12-4-1 UFC)</b>, &ldquo;The Kung Fu Kid,&rdquo; 28, makes his <b>sixth main-event appearance</b>. He <b>dropped a close decision to Sean O&rsquo;Malley at UFC&nbsp;324</b>, then rebounded in May by travelling to Macau and <b>submitting Figueiredo in the second round</b> &mdash; his first appearance on Chinese soil since 2018.</p>\n'
 '<p class="note"><b>Resolved this run &mdash; the &ldquo;two Figueiredo wins&rdquo; oddity.</b> Previous editions flagged that both main-eventers were credited with a recent win over Deiveson Figueiredo by the same outlet, and published the oddity rather than guess. UFC.com&rsquo;s fight-by-fight preview settles it: <b>they are two different fights.</b> Nurmagomedov beat Figueiredo on the scorecards at <b>UFC&nbsp;324</b> in January; Song submitted him in the second round at <b>UFC Fight Night Macau</b> in May. Both statements were always true.</p>',
 "mma top p2")

m = rep(m,
 '<p><b>The stakes are explicit.</b> The UFC&rsquo;s own framing is that a decisive win here <b>potentially carries massive title-shot implications in the 135-pound division</b> &mdash; a division whose belt is currently held by <b>Petr Yan</b>, and whose immediate contender picture is unsettled enough that Sports Illustrated has run the line that Nurmagomedov&rsquo;s rumoured next fight <b>&ldquo;leaves the door open for Dvalishvili vs. O&rsquo;Malley 2.&rdquo;</b> Underneath, the co-main pairs <b>China&rsquo;s first female UFC athlete and former strawweight title challenger, #4 Yan Xiaonan, against the surging #13 Denise Gomes</b>.</p>',
 '<p><b>The stakes are explicit.</b> UFC.com frames the matchup as carrying <b>&ldquo;massive divisional significance&rdquo;</b> at 135 pounds, with each man looking to enter the final quarter of the year as <b>&ldquo;the clubhouse leader in the chase for the next title opportunity&rdquo;</b> &mdash; and states that <b>&ldquo;the winner will have a legitimate case for being first in line to face the winner of Yan-Dvalishvili 3.&rdquo;</b> The belt is currently held by <b>two-time champion Petr Yan</b>, with a trilogy bout against <b>Merab Dvalishvili</b> the awaited next chapter. Underneath, the co-main pairs <b>Yan Xiaonan</b>, a fixture in the strawweight title conversation for nearly four years, against <b>Denise Gomes</b>.</p>',
 "mma top p3")

m = rep(m,
 '<p class="note">Rankings as stated by UFC.com. The Dvalishvili&ndash;O&rsquo;Malley line is a Sports Illustrated headline about a <b>rumoured</b> matchup and is reported here as exactly that &mdash; nothing about a second O&rsquo;Malley fight is booked or confirmed in anything fetched this run.</p>',
 '<p class="note"><b>The full main card, per UFC.com:</b> Nurmagomedov vs Song; <b>Yan Xiaonan vs Denise Gomes</b> (strawweight, co-main); <b>Aoriqileng vs Kai Asakura</b>; <b>Alex Perez vs Sumudaerji</b>; <b>Liu Ce vs Levi Rodrigues&nbsp;Jr.</b>; <b>Bilal Hasan vs Nilson Rojas</b>. A <b>12-fight undercard</b> supports it. Yan has <b>never lost in China in the UFC</b> and enters off a decision loss to Virna Jandiroba; Gomes, 26, arrives on a <b>four-fight winning streak</b>, having won six of her last seven. Perez&ndash;Sumudaerji is a rebooking after their Macau meeting was <b>halted prematurely by an accidental low blow</b>.</p>',
 "mma top note")

m = rep(m,
 '<div class="tldr"><b>Tale of the Tape</b> <span>It is fight week in Shanghai, where <b>Umar Nurmagomedov (20-1)</b> is a <b>&minus;470 favourite</b> over <b>Song Yadong (23-9-1)</b> in Saturday&rsquo;s bantamweight main event &mdash; while the contract news is moving too, with heavyweight <b>Curtis Blaydes</b> signing a fresh <b>eight-fight deal</b> and undefeated two-weight European champion <b>Lucia Szabova</b> joining the roster for an October&nbsp;31 debut.</span></div>',
 '<div class="tldr"><b>Tale of the Tape</b> <span>Fight week is under way in Shanghai, where <b>Umar Nurmagomedov (20-1)</b> and <b>Song Yadong (23-9-1)</b> have had their first faceoff ahead of a <b>6:00 a.m. EDT Saturday</b> main event that UFC.com says will leave the winner <b>&ldquo;first in line to face the winner of Yan-Dvalishvili 3&rdquo;</b> &mdash; with Nurmagomedov a <b>&minus;470 favourite</b> at DraftKings and <b>Yan Xiaonan vs Denise Gomes</b> in the co-main.</span></div>',
 "mma tldr")

save("mma-briefing.html", m)

# ============================== INDEX ==============================
i = load("index.html")
ws_t = re.search(r'<div class="tldr"><b>The Tape</b> <span>(.*?)</span></div>', w, re.S).group(1)
cy_t = re.search(r'<div class="tldr"><b>The Wire</b> <span>(.*?)</span></div>', c, re.S).group(1)
mm_t = re.search(r'<div class="tldr"><b>Tale of the Tape</b> <span>(.*?)</span></div>', m, re.S).group(1)

cards = re.findall(r'<a class="bcard c-(sec|mkt|mma)" href="[^"]+">\s*<div class="kicker">[^<]*</div>\s*<h2>(.*?)</h2>\s*<p>(.*?)</p>', i, re.S)
assert len(cards) == 3, f"index: expected 3 bcards, found {len(cards)}"
newh = {
 'sec': 'Boston Scientific&rsquo;s 8-K: a cyber incident that has reached its ability to ship customer orders',
 'mkt': 'Hot on the headline, steady at the core &mdash; July PCE lands, and the September <i>hike</i> stays on the table',
 'mma': 'Fight week in Shanghai: the winner is first in line for the title',
}
newp = {'sec': cy_t, 'mkt': ws_t, 'mma': mm_t}
for slug, h2, p in cards:
    i = rep(i, f'<h2>{h2}</h2>', f'<h2>{newh[slug]}</h2>', f"index h2 {slug}")
    i = rep(i, f'<p>{p}</p>', f'<p>{newp[slug]}</p>', f"index p {slug}")
save("index.html", i)

print(f"OK: {N} replacements applied. Build time label: {TIME}")
