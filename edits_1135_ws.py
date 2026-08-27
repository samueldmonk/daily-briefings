import io,sys
P='/sessions/optimistic-youthful-curie/mnt/outputs/wallstreet-briefing.html'
s=io.open(P,encoding='utf-8').read()
n=0
def R(old,new):
    global s,n
    c=s.count(old)
    assert c==1,('COUNT %d for: %s'%(c,old[:110]))
    s=s.replace(old,new); n+=1

# 1 — TLDR
R('<div class="tldr"><b>The Tape</b> <span>The bell has rung on a tech-led tape: Nvidia, Salesforce, CrowdStrike and now Okta are all higher on their results, with Okta up more than 20% and Salesforce and CrowdStrike each up about 14% in the latest quotes seen this run.</span></div>',
  '<div class="tldr"><b>The Tape</b> <span>Two hours into the session the tech-led rally has broadened and the Dow has joined it — the latest read has the Dow up 217.20 points (+0.41%) and the Nasdaq Composite up 327.22 points (+1.25%), with Okta still the biggest single-stock mover on its results.</span></div>')

# 2 — ticker tape: feature the session's movers, keep the five mandatory symbols
R('{"proName":"NASDAQ:MRVL","title":"Marvell"},{"proName":"NASDAQ:MU","title":"Micron"}',
  '{"proName":"NASDAQ:OKTA","title":"Okta"},{"proName":"NASDAQ:ZS","title":"Zscaler"}')

# 3 — Lead tags + headline
R('<span class="tag new">New · 9:35 AM ET</span><span class="tag acc">Just after the open</span>',
  '<span class="tag new">Updated · 11:35 AM ET</span><span class="tag acc">Midday session</span>')
R('<h3>Four earnings beats open the tape, with Okta the biggest mover — as of ~9:35 AM ET</h3>',
  '<h3>The rally broadens at midday: the Dow joins in, Okta still leads — as of ~11:35 AM ET</h3>')

# 4 — Lead para 1 (index reads) + the provenance caveat, rewritten for the midday reads
R('<p style="margin:0 0 10px">The regular session is open. Yahoo Finance\'s Thursday live coverage has US stocks <b>climbing</b> after results from Nvidia, Salesforce and CrowdStrike lifted the technology trade, with the <b>S&amp;P 500 up 0.4%</b>, the <b>Nasdaq Composite up about 1%</b> and the <b>Dow hovering near the flat line</b>.</p>',
  '<p style="margin:0 0 10px">Roughly two hours into the regular session, US stocks are <b>climbing</b> after results from Nvidia, Salesforce and CrowdStrike lifted the technology trade. The strongest-anchored read seen this run has the <b>Dow up 217.20 points, or 0.41%</b>, the <b>Nasdaq Composite up 327.22 points, or 1.25%</b>, and the <b>S&amp;P 500 up 0.4%</b>. <b>That is a change from this page\'s 9:35 edition</b>, which had the Dow hovering near the flat line — the Dow has since moved decisively higher, and the page names the change rather than quietly overwriting it.</p>')

R('<p style="margin:0 0 10px"><span style="color:var(--mut)"><b>A caution this page is placing on its own index figures.</b> Those three readings are numerically identical to the pre-open futures reads carried in the 9:05 edition (Nasdaq 100 futures +0.9%, S&amp;P 500 futures +0.4%, Dow near flat), and no source fetched this run stamped them with a post-open time. They are therefore printed as the latest available index reads, <b>not</b> asserted as prices struck after the 9:30 bell. The single-stock quotes below <i>have</i> moved off their pre-market levels, which is the evidence that live trading is being quoted.</span></p>',
  '<p style="margin:0 0 10px"><span style="color:var(--mut)"><b>How this page chose between three competing index sets, and why.</b> A second read this run has the <b>Dow up 169.90 points (+0.32%)</b> and the <b>Nasdaq Composite up 300.97 points (+1.15%)</b>. Both sets are internally consistent, but only the first reconciles against Wednesday\'s verified close: 217.20 points on the Dow is 0.41% of Wednesday\'s level, and 327.22 on the Nasdaq is 1.25% of its level, while the second set implies a prior close that does not match Wednesday\'s. The first set therefore leads and the second is printed alongside; <b>neither is averaged, and neither source stamped its figures with a time</b>, so no level is asserted in this section — levels live in the Weekly Scorecard. <b>A third set was rejected outright:</b> an aggregator page offered <b>7,673.04 / 53,195.36 / 26,168.46</b> as the <i>close</i> of August 27 — impossible before 4 PM, and its Dow figure is irreconcilable with its own stated percentage. <b>A fourth item was also rejected:</b> a "midday" snippet reporting <b>Nvidia up 39 cents to $163</b> with a <b>$3.97 trillion</b> market cap and the <b>S&amp;P 500 up 16 points to 6,279</b>. Those are 2025 levels — the same late-August anniversary collision that has caught this page before, because Nvidia reports its second quarter in the last week of August every year.</span></p>')

# 5 — Lead: rotation paragraph refreshed
R('<p style="margin:0 0 10px"><b>The leadership has rotated away from Nvidia since the pre-market.</b> The latest quotes seen this run have <b>Okta up more than 20%</b>, <b>Salesforce up 14.78%</b> and <b>CrowdStrike up 14.34%</b> — Salesforce and CrowdStrike both well above their pre-open reads, and Okta a name this page could put no number on an hour ago — while <b>Nvidia is up 5.87%</b>, <i>below</i> the 6% to 7.4% range quoted before the bell. In other words the software and identity names have extended and the chip that caused the rally has given a little back. Earlier in the pre-market the read-through had hit the whole semiconductor complex: <b>Marvell Technology +5.8%</b>, <b>Micron +4.5%</b>, the <b>VanEck Semiconductor ETF +3.5%</b> and the <b>iShares Semiconductor ETF +3%</b>.</p>',
  '<p style="margin:0 0 10px"><b>Okta remains the largest single-stock move, and the breadth has widened beyond the four earnings names.</b> The latest tally seen this run puts <b>Okta up 26.17%</b>, with a separate line in the same coverage describing the shares as having <b>surged 19%</b> — both printed, neither averaged, and both above the "more than 20%" this page carried at 9:35. <b>Salesforce is quoted at +11.2%</b> in the same coverage, against the <b>14.78%</b> carried at 9:35, and <b>CrowdStrike at +9%</b> against <b>14.34%</b>; the software pair have given back part of their opening pop, and every read is shown rather than the highest one being kept. <b>Nvidia</b> is described as up <b>6% to 7%</b>, the figures attached to its pre-market move rather than a fresh post-open quote, so the <b>5.87%</b> read carried at 9:35 remains the last live quote this page has for it. New names on the board this run: <b>Zscaler up 8.7%</b> and <b>Palantir up 3.8% at $184.32</b>, both in morning trading.</p>')

# 6 — Movers: Okta card
R('<div class="card"><span class="tag new">Updated · 9:35</span><span class="tag acc">Identity</span>\n<h3>Okta (OKTA) — up more than 20%, the session\'s biggest mover</h3><p>Okta has gone from a name this page could not put a number on to the largest single-stock move on the board: shares are <b>up more than 20%</b> after the company beat on both lines and pointed to booming demand tied to agentic AI. Adjusted earnings were <b>$1.05 per share on revenue of $805 million</b>, against the <b>97 cents</b> and <b>$795 million</b> analysts expected. Separately, <b>Bank of America upgraded Okta to Neutral from Underperform with a $170 price target</b>. <span style="color:var(--mut)">The 9:05 edition printed no percentage for Okta because none had been stated; one has now been.</span></p></div>',
  '<div class="card"><span class="tag new">Updated · 11:35</span><span class="tag acc">Identity</span>\n<h3>Okta (OKTA) — up 26.17%, still the session\'s biggest mover</h3><p>Okta holds the largest single-stock move on the board. The latest tally has shares <b>up 26.17%</b>; the same coverage separately describes them as having <b>surged 19%</b> after the company beat on both lines and pointed to booming demand tied to agentic AI. <b>Both figures are printed and neither is averaged</b>, and both sit above the "more than 20%" this page carried at 9:35. Adjusted earnings were <b>$1.05 per share on revenue of $805 million</b>, against the <b>97 cents</b> and <b>$795 million</b> analysts expected. Separately, <b>Bank of America upgraded Okta to Neutral from Underperform with a $170 price target</b>. <span style="color:var(--mut)">The 9:05 edition printed no percentage for Okta because none had been stated; two have now been, and they disagree.</span></p></div>')

# 7 — Nvidia card
R('<h3>Nvidia (NVDA) — up 5.87%, off its pre-market high</h3><p>The latest quote seen this run has <b>NVDA up 5.87%</b>. That is <i>below</i> every pre-market read this page carried an hour ago — <b>7.4%</b> (Reuters/AOL), <b>7.32%</b> (Benzinga) and <b>6%</b> (CNBC) — and above Wednesday evening\'s first post-call read of "more than 4%" in extended trading. All four figures are printed and none averaged. The driver is unchanged: the <b>$108 billion</b> third-quarter guide and Huang\'s fiscal-2028 growth comment.</p></div>',
  '<h3>Nvidia (NVDA) — last live quote +5.87%, with coverage still citing the pre-market move</h3><p>The last live quote this page has for <b>NVDA is +5.87%</b>, taken just after the open. Coverage fetched this run still describes the stock as up <b>6%</b> to <b>7%</b>, but those figures are attached to <i>pre-market</i> trading in the same sentences, so they are not treated as a fresher post-open read. Every figure the page has carried is shown and none averaged: <b>7.4%</b> (Reuters/AOL), <b>7.32%</b> (Benzinga) and <b>6%</b> (CNBC) before the bell, "more than 4%" in Wednesday\'s extended session, and <b>5.87%</b> live. The driver is unchanged: the <b>$108 billion</b> third-quarter guide and Huang\'s fiscal-2028 growth comment.</p></div>')

# 8 — CRM / CRWD card tags + latest reads
R('<h3>Salesforce (CRM) — up 14.78%, extending past its pre-market gain</h3><p>The latest quote seen this run has <b>CRM up 14.78%</b>, above the <b>nearly 12%</b> it was showing in pre-market trade.',
  '<h3>Salesforce (CRM) — quoted at +11.2% at midday, off its opening pop</h3><p>The latest coverage seen this run has <b>CRM up 11.2%</b>, against the <b>14.78%</b> this page carried at 9:35 and the <b>nearly 12%</b> it showed in pre-market trade. All three reads are printed and none averaged.')
R('<h3>CrowdStrike (CRWD) — up 14.34%, with a record ARR quarter</h3><p>The latest quote seen this run has <b>CRWD up 14.34%</b>, well beyond the <b>8.9%</b> it showed pre-open.',
  '<h3>CrowdStrike (CRWD) — quoted at +9% at midday, with a record ARR quarter</h3><p>The latest coverage seen this run has <b>CRWD up 9%</b>, against the <b>14.34%</b> this page carried at 9:35 and the <b>8.9%</b> it showed pre-open. All three reads are printed and none averaged.')
R('<div class="card"><span class="tag new">Updated · 9:35</span><span class="tag acc">Software</span>','<div class="card"><span class="tag new">Updated · 11:35</span><span class="tag acc">Software</span>')
R('<div class="card"><span class="tag new">Updated · 9:35</span><span class="tag acc">Cybersecurity</span>','<div class="card"><span class="tag new">Updated · 11:35</span><span class="tag acc">Cybersecurity</span>')
R('<div class="card"><span class="tag new">Updated · 9:35</span><span class="tag acc">Semis</span>','<div class="card"><span class="tag new">Updated · 11:35</span><span class="tag acc">Semis</span>')
R('<div class="card"><span class="tag new">New</span><span class="tag acc">Retail</span>','<div class="card"><span class="tag">Carried</span><span class="tag acc">Retail</span>')

# 9 — two new mover cards
R('It is the clearest counter-example on the board this morning to the idea that a beat guarantees a bid.</p></div>\n</div>',
  '''It is the clearest counter-example on the board this morning to the idea that a beat guarantees a bid.</p></div>

<div class="card"><span class="tag new">New · 11:35</span><span class="tag acc">Cybersecurity</span>
<h3>Zscaler (ZS) — up 8.7% in morning trading</h3><p>Zscaler shares are <b>up 8.7% in morning trading</b>, attributed in the coverage seen this run to a <b>JPMorgan price-target increase</b>. <span style="color:var(--mut)"><b>No price-target number is published here, and the reason is that the sources disagree in both size and direction.</b> One summary this run gives a raise to <b>$215 from $205</b>; a separate headline gives a raise to <b>$250 from $240</b>; and a third, undated headline says JPMorgan <i>cut</i> its Zscaler target on FY27 outlook concerns. The 8.7% move is stated plainly in this run\'s coverage and is published; the target figures are not, because three sources cannot be reconciled into one.</span></p></div>

<div class="card"><span class="tag new">New · 11:35</span><span class="tag acc">Software</span>
<h3>Palantir (PLTR) — up 3.8% to $184.32</h3><p>Palantir is <b>up 3.8% in morning trading, at $184.32</b>, lifted in the coverage seen this run by a fresh analyst endorsement. <span style="color:var(--mut)">The endorsing firm is not named in the text fetched here, so none is named on this page.</span></p></div>
</div>''')

# 10 — Chart of the Day -> the session's biggest mover
R('{"symbol":"NASDAQ:NVDA","width":"100%","height":240,"locale":"en","dateRange":"1D","colorTheme":"dark","isTransparent":true,"autosize":false}',
  '{"symbol":"NASDAQ:OKTA","width":"100%","height":240,"locale":"en","dateRange":"1D","colorTheme":"dark","isTransparent":true,"autosize":false}')
R('<div class="note">Nvidia set the tone for the session with Wednesday evening\'s report, though on the latest quotes it is no longer the largest mover — Okta, Salesforce and CrowdStrike are all ahead of it.</div>',
  '<div class="note">Okta is the session\'s single biggest mover on the latest tallies seen this run — <b>+26.17%</b> on one and <b>+19%</b> on another — so the chart tracks it. Nvidia set the tone with Wednesday evening\'s report, but it is no longer the largest move on the board.</div>')

# 11 — Sector note: reject the contaminated sector figures
R('<div class="note">Trading has leaned decisively toward technology, software and identity names on Thursday. The two sector proxies that were quoted in sources this run — the VanEck Semiconductor ETF at <b>+3.5%</b> and the iShares Semiconductor ETF at <b>+3%</b> — are the only numeric sector reads printed here. No S&amp;P sector-level or breadth figure is asserted; none was stated in sources seen this run.</div>',
  '<div class="note">Trading has leaned decisively toward technology, software, cybersecurity and identity names on Thursday. The two sector proxies quoted in sources this run — the VanEck Semiconductor ETF at <b>+3.5%</b> and the iShares Semiconductor ETF at <b>+3%</b> — remain the only numeric sector reads printed here, and both date from before the open. <span style="color:var(--mut)"><b>A sector table offering "Information Technology +1.03%, Energy −1.25%, 8 of 11 sectors higher" was fetched this run and is not published.</b> The same result also asserted that "US equity markets ended the session slightly lower on August 27" — impossible at 11:35 in the morning — and attributed its figures to the August 26 session in one line while presenting them as today\'s in another. A source that cannot say which session it is describing cannot supply this page with a sector number.</span></div>')

# 12 — Rates table: 30-year now verified; oil second read; add bitcoin
R('<tr><td>US 30-year Treasury yield</td><td class="mono" style="color:var(--mut)">not verified this run</td><td>No figure seen in sources fetched this run — none asserted.</td></tr>',
  '<tr><td>US 30-year Treasury yield</td><td class="mono">5.25%</td><td><b>Newly verified this run</b>, after four editions printing "not verified." Trading Economics has the 30-year <b>ending trading at 5.25%</b> alongside the 10-year easing to 4.65% from its Aug 21 high. For context, CNBC reported the 30-year topping <b>5.33%</b> on Aug 18 — a 19-year high — before slipping back to <b>5.285%</b> the same day.</td></tr>')
R('<tr><td>WTI crude</td><td class="mono">$81.36</td><td>Down 1.06% from the previous day on Aug 27 (Trading Economics), with prices falling for a third consecutive session. Investing.com showed a WTI futures range of $81.44–$82.15.</td></tr>',
  '<tr><td>WTI crude</td><td class="mono">$81.36–$81.63</td><td>Two reads this run, both for Aug 27 and both printed: <b>$81.36, down 1.06%</b> (Trading Economics), a third consecutive down session; and <b>$81.63, down 0.73%</b> in the early New York session (Benzinga). Investing.com showed a WTI futures range of $81.44–$82.15.</td></tr>\n<tr><td>Bitcoin</td><td class="mono">$79,836.71</td><td>Up <b>1.30%</b> over the prior 24 hours as of Thursday\'s pre-market (Benzinga). Carried here as a risk-appetite read, not as a market this page covers.</td></tr>')

# 13 — On the Radar: KC Fed has now passed
R('<li><b>11:00 AM ET — Kansas City Fed manufacturing index for August.</b></li>',
  '<li><b>11:00 AM ET — the Kansas City Fed manufacturing index for August has now been released.</b> <span style="color:var(--mut)">No figure from it was corroborated in sources fetched this run, so none is printed. The release window is stated; the number is not invented.</span></li>')

io.open(P,'w',encoding='utf-8').write(s)
print('wallstreet edits applied:',n)
