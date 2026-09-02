#!/usr/bin/env python3
# Sept 2, 2026 -- 9:35 AM ET run (FOURTH of the day, FIRST POST-OPEN edition).
# Targeted edits onto the 9:18 AM pre-open wallstreet page.
import re, sys

P = 'wallstreet-briefing.html'
h = open(P, encoding='utf-8').read()
orig = h
n = 0

def sub(pattern, repl, count=1, flags=0, label=''):
    global h, n
    new, k = re.subn(pattern, lambda m: repl, h, count=count, flags=flags)
    if k != count:
        print('FAIL[%s]: matched %d, expected %d' % (label, k, count)); sys.exit(1)
    h = new; n += k

# ---------------------------------------------------------------- 1. TL;DR
sub(r'<b>The Tape</b> <span>.*?</span></div>',
    '<b>The Tape</b> <span>Stocks opened mixed rather than lower after a soft ADP payrolls print '
    '&mdash; the Dow up about <b>187 points</b> while the S&amp;P 500 and Nasdaq hugged the flat line '
    '&mdash; and the day&rsquo;s sharpest reversal is in oil, which hit a one-month high overnight on '
    'U.S.&ndash;Iran strikes and then turned <b>lower</b> by the opening bell, even as the 10-year '
    'Treasury yield holds at multi-year highs.</span></div>',
    flags=re.S, label='tldr')

# ---------------------------------------------------------------- 2. Lead headline
sub(re.escape('<h3 class="lead-h">August private payrolls miss, and two live blogs disagree on which way futures point</h3>'),
    '<h3 class="lead-h">Stocks open mixed after a soft payroll print &mdash; and oil gives back its '
    'overnight spike <span style="color:var(--muted);font-weight:400">(as of the 9:30 open)</span></h3>\n'
    '<p><b>The bell has rung, and the tape is not doing the one thing the futures session kept arguing about.</b> '
    'Shortly after the 9:30 open, CNBC has the <b>Dow up about 187 points, or 0.4%</b>, the <b>S&amp;P 500 up 0.1%</b> '
    'and the <b>Nasdaq Composite down 0.1%</b> &mdash; mixed, with the industrials leading and the growth end lagging. '
    '<b>Those are the only September 2 index figures on this page, they are moves and not levels, and the only clock '
    'attached to them by the source is &ldquo;shortly after the opening bell.&rdquo;</b> No more precise timestamp was '
    'fetched, so none is asserted.</p>\n'
    '<p class="note" style="border-left:3px solid var(--up);padding-left:11px"><b>The reversal worth watching is in '
    'crude, not in equities.</b> At <b>7:04 AM ET</b> TheStreet had WTI <span class="up">+0.32% at $90.51</span> and '
    'Brent <span class="up">+0.57% at $95.19</span>, rising on the overnight strikes. By its <b>9:24 AM ET</b> update '
    'the same live blog has oil <b>falling</b> after touching more than one-month highs earlier in the session: '
    '<b>WTI <span class="down">&minus;0.71% at $89.58</span></b> and <b>Brent <span class="down">&minus;0.39% at '
    '$94.28</span></b>, as traders weighed supply-disruption risk against evidence, per Reuters, that crude is still '
    'reaching the market. <b>This is a genuine intraday turn inside one source, not a disagreement between two</b> '
    '&mdash; both prints carry the same byline and their own clocks. Saxo Bank&rsquo;s head of commodity strategy '
    'Ole Hansen calls it &ldquo;a binary risk&rdquo;: news of a deal &ldquo;could send prices tumbling, while any '
    'escalation would further undermine the prospect of a peace deal,&rdquo; leaving oil volatile with &ldquo;a '
    'potential $5 move in either direction.&rdquo;</p>\n'
    '<p><b>And a new policy headline landed seventeen minutes before the open.</b> Commerce Secretary '
    '<b>Howard Lutnick</b> told CNBC that the administration is developing <b>a tariff framework for semiconductors</b> '
    'and that companies know the tariffs are coming, confirming a Politico report from last week. &ldquo;I think what '
    'you&rsquo;re going to see is targeted, thoughtful tariff policy that basically says if you build here, you '
    'don&rsquo;t pay, but if you don&rsquo;t build here, expect to pay to enter the greatest market in the world,&rdquo; '
    'Lutnick said, adding: &ldquo;We will be successful in semiconductors. They&rsquo;re going to be built in America.&rdquo; '
    '<b>No detail of the framework has been published and no chip-stock reaction to it was sourced this run</b>, so none '
    'is described &mdash; but it arrives on the morning Broadcom reports.</p>',
    label='lead-h3')

# ---------------------------------------------------------------- 3. Futures-disagreement para -> retained as record
sub(r'<p><b>The futures picture changed character between reads.*?</p>',
    '<p><b>The pre-open futures record, kept because it is now settled by the tape rather than by argument.</b> '
    'TheStreet&rsquo;s 8:26 AM ET update opened &ldquo;stock futures were falling&rdquo;; Yahoo Finance&rsquo;s '
    'Wednesday live blog gave <b>Dow futures up 0.2%, S&amp;P 500 futures edging higher and Nasdaq-100 contracts '
    'down 0.1%</b>, which is <b>mixed</b>. The previous edition printed both and adopted neither. <b>The open has '
    'now come in mixed, with the Dow leading and the Nasdaq lower</b> &mdash; which resembles the Yahoo read. '
    '<b>That is not a retroactive vindication and is not published as one:</b> a futures quote at 8 AM and an index '
    'move at 9:31 are different measurements, and one matching the other is consistent with the earlier read having '
    'been right, with it having been wrong, or with coincidence.</p>',
    flags=re.S, label='futures-para')

# ---------------------------------------------------------------- 4. Final lead note -> post-open
sub(r'<p class="note"><b>No September 2 index level or percentage move appears anywhere in this editorial as a completed figure\.</b>.*?</p>',
    '<p class="note"><b>What this page does and does not claim now that the session is live.</b> The September 2 '
    'figures above are <b>moves shortly after the open</b>, not levels and not closes; the only index <i>levels</i> '
    'published anywhere here remain Tuesday&rsquo;s official closes, in the Weekly Scorecard. Single-stock '
    'percentages in Movers &amp; Drivers are <b>pre-market</b> quotes unless a card says otherwise, and a pre-market '
    'move is not a session move. <b>The live widgets on this page update continuously; this editorial was fixed at '
    'the time in the masthead.</b></p>\n'
    '<p class="note" style="border-left:3px solid var(--crit);padding-left:11px"><b>A trap this desk walked up to '
    'this run and did not walk into, recorded because it would have put three false claims on the page.</b> A search '
    'result offered Medtronic <span class="up">+3%</span>, Nvidia <span class="down">&minus;1.7%</span> and an Apple '
    'figure as <i>today&rsquo;s</i> early movers, sourced to Schwab&rsquo;s market-open commentary. Fetching that page '
    'shows it is <b>Tuesday&rsquo;s</b> edition &mdash; &ldquo;Published as of: September 1, 2026, 9:11 a.m. ET,&rdquo; '
    'headed &ldquo;(Tuesday market open)&rdquo; &mdash; sitting on a <b>rolling URL</b> that always resolves to the '
    'newest instalment and had not yet rolled. <b>Those are September 1 movers.</b> The Apple percentage was worse '
    'than stale: the Schwab page says only that Apple &ldquo;stood its ground early&rdquo; and is up almost 17% year '
    'to date, and <b>carries no daily percentage at all</b>. <b>New defect class: an evergreen URL is a citation to a '
    'slot, not to an article &mdash; it is correct today and silently wrong tomorrow, and the fetched page&rsquo;s own '
    'dateline is the only tell.</b></p>',
    flags=re.S, label='lead-final-note')

# ---------------------------------------------------------------- 5. Movers note
sub(r'<div class="note">Pre-market quotes as TheStreet reported them at <b>7:27 AM ET</b>.*?</div>',
    '<div class="note">Single-stock figures below are <b>pre-market</b> quotes as TheStreet reported them at '
    '<b>7:27 AM ET</b> and as CNBC&rsquo;s September 2 pre-market roundup reported them, except where a card states '
    'otherwise. <b>The session is now open and no September 2 single-stock session move or closing figure has been '
    'sourced this run</b>, so none is published. <b>&ldquo;New&rdquo; tags mark items absent from the previous '
    'edition</b> (the 9:18 AM snapshot); names carried over may still carry figures that are new this run, so the '
    'absence of a tag is not a claim of staleness.</div>',
    flags=re.S, label='movers-note')

# ---------------------------------------------------------------- 6. Expire stale novelty tags (CRDO/SIRI/VRT/PANW were New at 09:18)
before = h.count('<span class="tag t-new">New</span>')
h = h.replace('<span class="tag t-new">New</span>', '<span class="tag t-a">Carried forward</span>')
print('  expired %d stale New tags on markets' % before)

# ---------------------------------------------------------------- 7. New cards (prepended into the cards grid)
newcards = (
 '<div class="card"><div class="tags"><span class="tag t-new">New</span><span class="tag t-a">Reversal</span>'
 '<span class="tag t-a">Commodities</span></div>\n'
 '<h3>Crude oil &mdash; up overnight, down by the bell</h3><p>WTI <span class="down">&minus;0.71%</span> to '
 '<b>$89.58</b> and Brent <span class="down">&minus;0.39%</span> to <b>$94.28</b> as of TheStreet&rsquo;s '
 '<b>9:24 AM ET</b> update, <b>after</b> climbing to more than one-month highs earlier in the same session '
 '&mdash; the 7:04 AM prints were $90.51 and $95.19, both higher. Reuters attributes the fade to traders weighing '
 'disruption risk against signs that crude is still reaching the market despite overnight U.S. and Iranian strikes. '
 '<b>Both ends of the move are printed; neither is averaged into the other.</b></p></div>\n'
 '<div class="card"><div class="tags"><span class="tag t-new">New</span><span class="tag t-a">Policy</span></div>\n'
 '<h3>Chip tariffs &mdash; a framework, not yet a rate</h3><p>Commerce Secretary <b>Howard Lutnick</b> told CNBC at '
 '<b>9:07 AM ET</b> that the administration is building <b>a semiconductor tariff framework</b> and that companies '
 'are aware the tariffs are coming, confirming a Politico report from last week. The stated principle is '
 '&ldquo;if you build here, you don&rsquo;t pay.&rdquo; <b>No rate, no scope and no start date has been published, '
 'and the administration has never publicly detailed what it is considering</b> &mdash; so this is a direction of '
 'travel, not a number, and it is not attached to any move in a chip stock here because no such move was sourced.</p></div>\n'
 '<div class="card"><div class="tags"><span class="tag t-a">Reports tonight</span><span class="tag t-a">Consensus</span></div>\n'
 '<h3>Broadcom (AVGO) &mdash; tonight&rsquo;s number</h3><p>Reports after the close. Consensus compiled ahead of the '
 'print looks for <b>Q3 revenue of $29.43 billion</b> and <b>GAAP EPS of $2.55</b>; management had previously guided '
 '<b>AI semiconductor revenue to grow more than 200% year over year to about $16 billion</b>. Schwab frames the read '
 'as an echo test on Nvidia&rsquo;s recent results &mdash; whether those reflected broad AI strength or Nvidia&rsquo;s '
 'own metrics. <b>These are expectations, not results.</b> Snowflake, also after the bell, is seen at <b>$1.48 billion</b> '
 'revenue and <b>$0.45</b> per share.</p></div>\n'
 '<div class="card"><div class="tags"><span class="tag t-new">New</span><span class="tag t-a">No figure sourced</span></div>\n'
 '<h3>SpaceX (SPCX)</h3><p>Shares &ldquo;edge up&rdquo; after a Falcon 9 carried <b>27</b> Starlink satellites to '
 'orbit from Vandenberg Space Force Base at <b>4:42 a.m. EDT</b> &mdash; the <b>35th</b> flight for that first stage, '
 'booster B1063, two short of the reuse record set by B1067 last week. <b>No percentage is published because the '
 'source states none</b>: &ldquo;edges up&rdquo; is the whole of the claim. For scale, and dated: the stock debuted at '
 '<b>$135</b> on June 12 and reached a record <b>$225.64</b> on June 16.</p></div>\n'
)
sub(r'(<h2>Movers &amp; Drivers</h2><div class="note">.*?</div><div class="cards">\n)',
    None, count=0, label='noop') if False else None
idx = h.find('<div class="cards">\n')
if idx < 0:
    print('FAIL: cards grid not found'); sys.exit(1)
h = h[:idx+len('<div class="cards">\n')] + newcards + h[idx+len('<div class="cards">\n'):]
n += 1

# ---------------------------------------------------------------- 8. Scorecard note
sub(r'<div class="note">September 1 closes corroborated this run by CNBC and TheStreet\..*?</div>',
    '<div class="note">September 1 closes corroborated by CNBC and TheStreet. August 31 closes carried from this '
    'desk&rsquo;s verified standing record. <b>No September 2 level is published: the session is open but not closed, '
    'and an intraday level is not a close.</b> The September 2 figures in The Lead are percentage moves shortly after '
    'the open.</div>',
    flags=re.S, label='scorecard-note')

# ---------------------------------------------------------------- 9. Sector note
sub(r'<div class="note">Editorial reference for the completed session:.*?will diverge once the bell rings\.</div>',
    '<div class="note">Editorial reference for Tuesday&rsquo;s completed session: four of eleven S&amp;P 500 sectors '
    'higher, energy +1.3%, consumer discretionary &minus;1.9%. <b>No September 2 sector figure has been sourced this '
    'run and none is asserted</b> &mdash; the map above is live and is the current picture. Context, dated to Tuesday '
    'and sourced to Schwab: just under <b>49%</b> of S&amp;P 500 members were above their 50-day moving average on '
    'Monday, down from <b>62%</b> at the start of August and a peak above 70% in mid-August.</div>',
    flags=re.S, label='sector-note')

# ---------------------------------------------------------------- 10. Oil rows
sub(r'<tr><td>Brent crude</td>.*?</tr>',
    '<tr><td>Brent crude</td><td>$94.28</td><td class="down">&minus;0.39% as of TheStreet&rsquo;s <b>9:24 AM ET</b> '
    'update &mdash; <b>oil turned lower after touching more than one-month highs earlier in the session</b> (Reuters '
    'via TheStreet). Earlier prints the same morning, all higher and all printed: $95.19 / +0.57% at 7:04 AM '
    '(TheStreet), &ldquo;above $95&rdquo; (Yahoo Finance), $94.86 / +0.23% (Trading Economics). '
    '<span style="color:var(--muted)">Four clocks, none averaged.</span></td></tr>',
    flags=re.S, label='brent')
sub(r'<tr><td>WTI crude</td>.*?</tr>',
    '<tr><td>WTI crude</td><td>$89.58</td><td class="down">&minus;0.71% as of <b>9:24 AM ET</b> (TheStreet), after '
    '<span class="up">+0.32% at $90.51</span> at 7:04 AM the same morning and an overnight quote board showing the '
    'October contract at $90.32 (+0.11%). <b>The direction changed inside the session; every print is kept with its '
    'own clock.</b></td></tr>',
    flags=re.S, label='wti')

# ---------------------------------------------------------------- 11. Fed funds row: add sourced hike-odds
sub(r'(<tr><td>Fed funds target</td><td>3\.50%&ndash;3\.75%</td><td>.*?)</td></tr>',
    None, count=0, label='noop2') if False else None
m = re.search(r'<tr><td>Fed funds target</td><td>3\.50%&ndash;3\.75%</td><td>(.*?)</td></tr>', h, re.S)
if not m:
    print('FAIL: fed funds row'); sys.exit(1)
h = h[:m.end(1)] + (' <b>Newly sourced this run, and dated:</b> Schwab, writing Tuesday, put the probability of a '
    '<b>hike</b> at the Fed&rsquo;s September meeting at <b>66%</b> on the CME FedWatch Tool, <b>up from 40% a week '
    'earlier</b>. That is a Tuesday reading, not a Wednesday one.') + h[m.end(1):]
n += 1

# ---------------------------------------------------------------- 12. On the Radar
sub(r'<li><b>Friday: the monthly jobs report</b>.*?</li>',
    '<li><b>Friday, Sept 4: the August jobs report</b> &mdash; nonfarm payrolls and the unemployment rate; the number '
    'that decides whether September&rsquo;s hike pricing survives, and the one this morning&rsquo;s 38,000 will be '
    'measured against.</li>\n'
    '<li><b>Monday, Sept 7: U.S. markets are closed for Labor Day.</b> This is a four-session week.</li>\n'
    '<li><b>Thursday, Sept 3:</b> August ISM Services PMI, plus earnings from Ciena and lululemon. Tesla holds a '
    '<b>Cybercab launch event in Austin</b> the same day.</li>\n'
    '<li><b>A dispersion note, dated to Tuesday and sourced to Schwab citing CNBC:</b> intra-stock correlation within '
    'the S&amp;P 500 is at <b>0.10</b> on a zero-to-one scale &mdash; described as the lowest on record back to 1990. '
    'Schwab&rsquo;s Alex Coffey: &ldquo;Stock pickers are experiencing a lot more volatility than passive index '
    'investors.&rdquo; It is one reason a mixed open with a 187-point Dow and a lower Nasdaq is not a contradiction.</li>\n'
    '<li><b>Eurozone inflation reached 3.3% annually in August</b>, a multi-year high; the European Central Bank meets '
    'next week (Schwab, Tuesday). The <b>30-year U.S. Treasury yield has spent 55 days above 5% this year, the most in '
    'any year since 2006.</b></li>',
    flags=re.S, label='radar')

# ---------------------------------------------------------------- 13. Sources
sub(r'(<h2>Sources</h2><div class="panel srcs">\n)',
    '<h2>Sources</h2><div class="panel srcs">\n'
    '<a href="https://www.cnbc.com/2026/09/01/stock-market-today-live-updates.html">CNBC &mdash; Stock market today: live updates (Sept 2 open: Dow +187 / +0.4%, S&amp;P +0.1%, Nasdaq &minus;0.1%)</a><br>\n'
    '<a href="https://www.reuters.com/business/energy/oil-up-nearly-1-us-iran-trade-fresh-strikes-2026-09-02/">Reuters &mdash; Oil, U.S. and Iran trade fresh strikes (Sept 2, 2026)</a><br>\n'
    '<a href="https://www.cnbc.com/2026/09/02/g20-innovation-ministerial-live-updates.html">CNBC &mdash; Lutnick on the semiconductor tariff framework (Sept 2, 2026)</a><br>\n'
    '<a href="https://www.schwab.com/learn/story/stock-market-update-open">Charles Schwab &mdash; Schwab Market Update, market open (the instalment fetched this run is dated <b>September 1, 2026, 9:11 a.m. ET</b>; rolling URL)</a><br>\n'
    '<a href="https://www.space.com/space-exploration/launches-spacecraft/spacex-falcon-9-starlink-group-15-23-launch-ocisly">Space.com &mdash; Falcon 9 Starlink launch from Vandenberg (Sept 2, 2026)</a><br>\n',
    label='sources')

open(P, 'w', encoding='utf-8').write(h)
print('OK wallstreet: %d edits, %d -> %d bytes' % (n, len(orig), len(h)))
