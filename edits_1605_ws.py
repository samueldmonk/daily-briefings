import re,sys
P='wallstreet-briefing.html'
h=open(P).read()
n=0
def rep(old,new,cnt=1):
    global h,n
    if old not in h:
        print("!! NOT FOUND:",old[:110]); sys.exit(1)
    h=h.replace(old,new,cnt); n+=1

# 1. demote all 3:15 freshness tags
rep('<span class="tag new">Updated · 3:15 PM ET</span>','<span class="tag new">Updated · 4:05 PM ET</span><span class="tag crit">Bell has rung</span><span class="tag">Carried · 3:15 PM ET</span>')
h=h.replace('<span class="tag new">New &middot; 3:15</span>','<span class="tag">Carried &middot; 3:15</span>')

# 2. TLDR
rep('<div class="tldr"><b>The Tape</b> <span>A live tracker timestamped at 3:05 PM ET has the Dow up just 0.15% and the Nasdaq Composite up 1.32%, both below the reads this page carried at 2:41, and the breadth behind the rally is now numeric as well as anecdotal: the technology sector ETF is up 2.3% while ten of the eleven S&amp;P 500 sectors are lower, led down by healthcare, utilities and consumer staples.</span></div>',
 '<div class="tldr"><b>The Tape</b> <span>The bell has rung and the first full-session reads have the Nasdaq Composite up 1.31%, the S&amp;P 500 up 0.66% and the Dow up 0.33% — but no source had published a settled close in the minutes after four o\'clock, so none is asserted here, and the day\'s first breadth count shows how narrow it was: only 156 of the 503 S&amp;P 500 stocks finished higher.</span></div>')

# 3. Lead headline
rep("<h3>The Dow's gain has shrunk to 0.15% and ten of eleven sectors are red — the rally is one sector wide, as of ~3:15 PM ET</h3>",
 '<h3>The bell has rung on a one-sector rally: the Nasdaq up 1.31%, the S&amp;P up 0.66% — and only 156 of 503 S&amp;P stocks higher, as of ~4:05 PM ET</h3>')

# 4. Note on timing -> post-close version
old_note='<p style="margin:0 0 12px;padding:9px 12px;border-left:3px solid var(--acc);background:rgba(202,166,74,.07);border-radius:8px;font-size:14.3px"><b>Note on timing.</b> The figures in this edition were fetched at about <b>3:15 PM ET</b>, before the closing bell, and every one of them is an intraday read. <b>If you are reading this after 4 PM, the session has closed and no closing figure below is a close</b> — this page publishes official closes only once they are verified, in the Weekly Scorecard, and none for August 27 had been verified when this edition was built. The next edition will carry them.</p>'
new_note='<p style="margin:0 0 12px;padding:9px 12px;border-left:3px solid var(--crit);background:rgba(202,166,74,.07);border-radius:8px;font-size:14.3px"><b>Note on timing — and on what this page will not call a close.</b> Research for this edition was fetched at about <b>4:05 PM ET</b>, <b>four minutes after the closing bell</b>. Two sources now describe the <i>whole session</i> rather than a moment inside it, and their figures are printed below. <b>They are still not published here as the official close.</b> Four minutes is not enough time for a settled closing print to propagate, the reads disagree with each other at the second decimal, and the aggregator levels that did arrive contradict both themselves and Wednesday&rsquo;s verified close. <b>The Weekly Scorecard therefore still carries no August 27 row.</b> The previous edition promised the next one would carry the close; it does not, and this paragraph says so rather than quietly dropping the promise.</p>'
rep(old_note,new_note)

# 5. New lead paragraphs inserted right after the note
anchor='<p style="margin:0 0 10px"><b>New at 3:15 — the second time-stamped cash-session read of the day'
newp='''<p style="margin:0 0 10px"><b>New at 4:05 — the first figures of the day that describe the entire session, and the Dow finished better than it looked at three o&rsquo;clock.</b> A markets column published for August 27 has the <b>Nasdaq Composite up 1.31%</b>, the <b>S&amp;P 500 up 0.66%</b> and the <b>Dow up 0.33%</b>. Set against the <b>3:05 PM</b> tracker quotes this page carried an edition ago — Dow +0.15%, Nasdaq +1.32% — <b>the Nasdaq is unchanged to within a hundredth of a point and the Dow is more than twice as high</b>. <span style="color:var(--mut)"><b>The tempting sentence — that the tape faded into the bell — is not written, because it is only true of one comparison.</b> Against the <b>2:41</b> reads (0.4% / 1.51% / 0.8%) all three are lower; against the <b>3:05</b> reads the Dow rose and the Nasdaq held. A page that had said &ldquo;faded&rdquo; would have been describing the midday comparison and implying the recent one.</span></p>
<p style="margin:0 0 10px"><b>New at 4:05 — and the S&amp;P figure is corroborated twice, from sources that do not share a number anywhere else.</b> Trading Economics independently puts the index at <b>7,727, up 0.67%</b> — one hundredth of a point from the column&rsquo;s 0.66%, and, against Wednesday&rsquo;s verified <b>7,675.70</b> close, arithmetically consistent: 7,675.70 &times; 1.0067 = <b>7,727.1</b>. <span style="color:var(--mut)">That reconciliation is why the <b>7,727</b> level is printed at all, and it is printed <b>untimed and outside the Weekly Scorecard</b>, exactly as it was at 3:15. Two sources landing within 0.01 of a point on the S&amp;P is the tightest agreement this page has recorded today; it is <b>not</b> treated as promoting either figure to a close.</span></p>
<p style="margin:0 0 10px"><b>New at 4:05 — the breadth question gets a count, not just a direction.</b> The same column reports that <b>only 156 of the 503 S&amp;P 500 stocks</b> finished higher and that <b>23 of the 30 Dow components</b> fell. <span style="color:var(--mut)">All day this page could say only that ten of eleven sectors were red; that was a sector tally borrowed from a mid-morning note. <b>This is the first stock-level breadth count of the day</b> — roughly <b>31%</b> of the index higher on a session the index itself finished up two thirds of a percent, which is the arithmetic of a rally carried by a handful of very large names. The 31% is this page&rsquo;s division of 156 by 503 and is labelled as such, not quoted from the source.</span></p>
<p style="margin:0 0 10px"><b>Rejected at 4:05 — a closing set that contradicts itself, and one that contradicts the day.</b> Two aggregator reads arrived claiming August 27 closes. The first: <b>S&amp;P 500 7,673.04 +0.42%</b>, <b>Dow 53,195.36 +0.83%</b>, <b>Nasdaq 26,168.46 +0.39%</b>. The second: <b>S&amp;P +0.24%, Dow −0.19%, Nasdaq +0.83%</b>. <span style="color:var(--mut)"><b>Neither is published.</b> The 7,673.04 level has now been offered to this page <b>three times today with three different percentages attached</b>, and it is <i>below</i> Wednesday&rsquo;s verified 7,675.70 close while being labelled a gain. The second set puts the Dow down and the Nasdaq at 0.83% — a figure the first set assigns to the Dow. <b>A number that arrives attached to a different percentage each time it appears is not a close; it is an aggregator field that has not settled.</b></span></p>
<p style="margin:0 0 10px"><b>Rejected at 4:05 — &ldquo;energy down 1.82%&rdquo;, for the fifth time.</b> The figure returned again in this run&rsquo;s sector coverage, once more with no session date attached to the number itself. <span style="color:var(--mut)">It has now been offered at 11:35, 12:05, 2:21, 2:41 and 4:05. <b>Repetition is not sourcing.</b> The rule stands: a framing sentence does not supply the date the number is missing.</span></p>
'''
rep(anchor,newp+anchor)

# 6. Movers: new card at top of Movers grid
rep('Movers &amp; Drivers</h2>\n<div class="cards">\n','''Movers &amp; Drivers</h2>
<div class="cards">
<div class="card" style="grid-column:1/-1"><span class="tag new">New &middot; 4:05</span><span class="tag acc">Full session</span>
<h3>Salesforce and CrowdStrike both set new highs for the day — and the same run returned figures roughly half as large</h3><p><b>New at 4:05:</b> a movers roundup for August 27 puts <b>Salesforce up 22.87%</b> and <b>CrowdStrike up 20.47%</b>, <b>Okta up 17.4%</b> and <b>Nvidia up 9%</b>. The Salesforce and CrowdStrike figures are the <b>highest either name has been quoted at today</b>, edging past the 22.75% and 19.75% carried at 3:15. <b>But the full-session column fetched in the same run has Salesforce at 19% and CrowdStrike at 9%.</b> <span style="color:var(--mut)">That is a spread of roughly <b>four points on Salesforce and eleven on CrowdStrike, from two sources describing the same finished session</b> — which rules out intraday drift as the explanation, since there is no more intraday left. <b>None is asserted, none is averaged, and none is withdrawn.</b> Salesforce&rsquo;s ladder today, in the order this page received it: 14.78%, 11.2%, 21.04%, 10.4%, 22.68%, 22.75%, 19%, 22.87%. CrowdStrike&rsquo;s: 17.93%, 9%, 19.67%, 19.75%, 20.47%.</span></p></div>
<div class="card" style="grid-column:1/-1"><span class="tag new">New &middot; 4:05</span><span class="tag acc">Nvidia</span>
<h3>Nvidia&rsquo;s market-value gain now has two figures, twenty-six billion dollars apart</h3><p><b>New at 4:05:</b> the full-session column attributes to Nvidia a <b>$461 billion increase in market value</b> and puts the stock <b>up 8.4%</b>, calling it the driving force behind both the S&amp;P 500 and the Nasdaq Composite. <span style="color:var(--mut)">An <b>Eastern Herald</b> piece carried since 3:15 puts the same day&rsquo;s addition at about <b>$435 billion</b>. <b>Both are printed; neither is asserted and they are not averaged.</b> The two are not necessarily in conflict — a market-capitalisation delta depends on the share count and the reference price used — but no source stated its method, so this page states the gap instead of resolving it. The price ladder for the name today, unchanged in shape: 6% (pre-market), 7% (Bloomberg, 1:25 p.m.), 8.34% (3:05 tracker), <b>8.4%</b> (this run), 9%, 9.3%, 9.48%.</span></p></div>
''')

# 7. Chart of the Day note
rep("<b>Updated at 2:21, and the reasoning has narrowed:</b> the","<b>Updated at 4:05:</b> Salesforce&rsquo;s new high of <b>22.87%</b> is the closest any name has come to Okta all day, but it remains <b>below Okta&rsquo;s 26.17% high</b>, and no name has been quoted above that figure at any point today &mdash; so the chart stays where it is. <b>Updated at 2:21, and the reasoning has narrowed:</b> the")

# 8. After-hours section before Weekly Scorecard
rep('<h2 class="sec">Weekly Scorecard</h2>','''<h2 class="sec">After-Hours Movers</h2>
<div class="panel">
<span class="tag new">New &middot; 4:05</span><span class="tag crit">Nothing dated</span>
<h3 style="margin:2px 0 8px;font-size:16px">Four minutes after the bell, no after-hours move could be tied to today&rsquo;s date — so none is printed</h3>
<p style="margin:0 0 10px">This section exists because the session has closed. It is <b>empty of numbers on purpose.</b> A search for after-hours movers run at <b>4:05 PM ET</b> returned an undated block naming <b>Rubrik</b>, <b>Bloom Energy</b> and a special-distribution stock, none of which could be tied to an August 27 post-close print in the material fetched. <span style="color:var(--mut)"><b>Undated movers are exactly the failure mode this page rejects on the cash session, and the standard does not loosen after four o&rsquo;clock.</b> The names are recorded here so the next edition knows they were seen and declined, not so the reader treats them as tonight&rsquo;s movers.</span></p>
<p style="margin:0"><b>What to expect after this bell.</b> The economic calendar fetched this run lists <b>Dollar General, Dollar Tree, Burlington Stores</b> and <b>Best Buy</b> among today&rsquo;s reporters. <span style="color:var(--mut)">No reaction figure for any of them was stated in sources fetched this run and none is printed.</span></p>
</div>

<h2 class="sec">Weekly Scorecard</h2>''')

# 9. Scorecard note
rep('<div class="note">A closing set of 7,677.24','<div class="note"><b>New at 4:05 — still no August 27 row, four minutes after the bell.</b> The session&rsquo;s full-session reads (Nasdaq +1.31%, S&amp;P +0.66%, Dow +0.33%) are in The Lead above; they are <b>not promoted here</b>, because this table holds verified official closes and nothing published in the four minutes after the bell met that bar. The untimed <b>7,727</b> S&amp;P level that reconciles against Wednesday is likewise kept out of this table.<br><br>A closing set of 7,677.24')

open(P,'w').write(h)
print("wallstreet edits applied:",n)
