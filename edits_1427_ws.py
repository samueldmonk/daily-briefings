# -*- coding: utf-8 -*-
# Edition 2026-09-08 ~14:27 ET research / Midday. Wall Street page edits.
import io, os, sys
D = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(D, "b_ws.py")
s = io.open(p, encoding="utf-8").read()
n = 0

def rep(old, new):
    global s, n
    assert old in s, "MISSING: " + old[:90]
    s = s.replace(old, new, 1)
    n += 1

# ---------------- sources ----------------
rep(''' ("StreetStats - U.S. Treasury yield curve", "https://streetstats.finance/rates/treasuries"),''',
    ''' ("StreetStats - U.S. Treasury yield curve", "https://streetstats.finance/rates/treasuries"),
 ("Whatfinger Business & Money - Market Midday: Stocks Slide, Dow Loses 500 Points, Oil Moves Higher (9/8/26)", "https://money.whatfinger.com/2026/09/08/market-midday-stocks-slide-dow-loses-500-points-oil-moves-higher-9-8-26/"),
 ("CNBC - Stock market news for Sept. 4, 2026", "https://www.cnbc.com/2026/09/03/stock-market-today-live-updates.html"),
 ("The Washington Post - How major US stock indexes fared Friday 9/4/2026", "https://www.washingtonpost.com/business/2026/09/04/stock-market-dow-nasdaq-jobs/b9e994e6-a89f-11f1-9e38-f705d048bd5a_story.html"),
 ("Gotrade - Week Ahead: August CPI & Oracle Earnings in Focus", "https://www.heygotrade.com/en/news/weekly-economic-outlook-2026-09-07/"),
 ("Yahoo Finance - Inflation data, Oracle earnings, and an energy supply crunch: What to watch this week", "https://finance.yahoo.com/economy/article/inflation-data-oracle-earnings-and-an-energy-supply-crunch-what-to-watch-this-week-120429533.html"),
 ("Finance Calendar - US CPI Report September 2026: Date, Time & What to Expect", "https://www.financecalendar.com/event/us-cpi-report-september-2026/"),
 ("StockMarketWatch - Tech Resilience Amidst Broader Market Softness: Afternoon Update", "https://stockmarketwatch.com/live/stock-market-today"),''')

# ---------------- tldr ----------------
rep('''<div class="tldr"><b>The Tape</b> <span>Stocks are lower across the board into Tuesday afternoon with the Dow much the weakest of the three, as Houthi strikes on Saudi energy facilities push Brent toward $100 and a failed Novartis heart-drug trial drags the health care sector down more than 2%.</span></div>''',
    '''<div class="tldr"><b>The Tape</b> <span>The Dow is now down around 500 points on a midday read as Houthi strikes on Saudi energy facilities push Brent toward $100 and a failed Novartis heart-drug trial drags health care down more than 2%, with an August payrolls print of 162,000 against a 53,000 consensus keeping a September Fed hike in play.</span></div>''')

# ---------------- lead ----------------
rep('''<h3 style="margin:0 0 8px;font-size:20px">As of reads taken ~1:25&ndash;1:50 PM ET: the selling deepens, with two separate shocks &mdash; oil and a failed drug trial &mdash; hitting different ends of the market</h3>''',
    '''<h3 style="margin:0 0 8px;font-size:20px">As of reads taken ~2:25&ndash;2:40 PM ET: the Dow is down about 500 points, and the two shocks driving it &mdash; oil and a failed drug trial &mdash; are still unrelated to each other</h3>''')

rep('''<li>A Tuesday session summary has the <b>Dow down 1%</b>, the <b>S&amp;P 500 down roughly 0.4%</b> and the <b>Nasdaq Composite down 0.1%</b> as the trading day progressed. <span class="mut">Each of those is worse than, or equal to, an earlier read of this same session, which had &minus;0.8% / &minus;0.2% / &minus;0.1%. The deterioration is the direction of travel this edition adds.</span></li>''',
    '''<li><b>New this edition:</b> a midday market wire dated today reports the <b>Dow down 500 points</b> with stocks sliding and oil moving higher. <span class="mut">That is a headline figure from a single outlet and is printed as such, in points rather than converted to a percentage. It is the third successive worsening this briefing has recorded today: &minus;0.8% on the Dow at 10:48 a.m., &minus;1% at 1:50 p.m., and roughly 500 points now.</span></li>
<li>A Tuesday session summary carried from the 1:50 p.m. edition has the <b>Dow down 1%</b>, the <b>S&amp;P 500 down roughly 0.4%</b> and the <b>Nasdaq Composite down 0.1%</b> as the trading day progressed. <span class="mut">Re-confirmed rather than re-dated this run; the 500-point read above is the newer one.</span></li>''')

rep('''A midday desk note describes the divergence plainly: the broad market struggled to find its footing while a resurgence in technology and semiconductor shares cushioned the tech-heavy indexes.''',
    '''An afternoon desk note read this run describes U.S. equities as <b>bifurcated</b> on Tuesday afternoon: technology showed resilience while the broader averages struggled to hold momentum, with investors balancing optimism on artificial intelligence against caution over the inflation data ahead and a softening industrial outlook.''')

# ---------------- new mover card: Hormuz ----------------
rep('''<div class="card">
<div class="tags"><span class="t">Carried</span><span class="t">Rates</span></div>
<h3>The bond leg: 4.8% touched, then given back</h3>''',
    '''<div class="card">
<div class="tags"><span class="t new">New</span><span class="t gold">Hormuz</span></div>
<h3>A second oil story: Iran and Oman on the Strait of Hormuz</h3>
<p>Alongside the Saudi strikes, this run&#39;s reads name a separate driver of the crude bid: <b>Iran said it was close to a deal with Oman to manage traffic through the Strait of Hormuz</b>. Against that backdrop <b>Brent crept toward $100 a barrel</b> and <b>WTI neared $93</b>. <span class="mut">Those two levels come from the same read and sit inside &mdash; not on top of &mdash; the Brent and WTI figures in the commodities table below, which were taken at 11:28 a.m. ET and from a separate afternoon read. No source read this run says whether the Oman talks are supporting prices or capping them, so no direction is attributed to them here.</span></p>
</div>
<div class="card">
<div class="tags"><span class="t new">New</span><span class="t">Jobs</span></div>
<h3>The payrolls consensus resolves to 53,000</h3>
<p>Friday&#39;s August employment report is the reason a September hike is being priced at all, and this run pins down the number it beat. <b>Nonfarm payrolls grew 162,000</b> against the <b>53,000</b> expected by economists polled by <b>Dow Jones</b> &mdash; roughly three times the consensus &mdash; with the <b>unemployment rate unchanged at 4.1%</b>, as expected. <b>Treasury yields rose on the report, and the 2-year hit its highest level since January 2025.</b> <span class="mut">Earlier editions of this briefing printed 53,000, 55,000 and 56,000 side by side because three consensus figures had returned. This run attaches 53,000 to a named poll, so it is used as the consensus; a separate read giving 56,000 is noted below rather than dropped, since different surveys legitimately differ.</span></p>
</div>
<div class="card">
<div class="tags"><span class="t">Carried</span><span class="t">Rates</span></div>
<h3>The bond leg: 4.8% touched, then given back</h3>''')

# demote prior New
rep('''<div class="tags"><span class="t new">New</span><span class="t hot">Health care</span></div>
<h3>Health care is now the worst sector on the board</h3>''',
    '''<div class="tags"><span class="t">Carried</span><span class="t hot">Health care</span></div>
<h3>Health care is now the worst sector on the board</h3>''')

# ---------------- refusals card ----------------
rep('''A mid-morning semiconductor list refused in an earlier edition &mdash; on the evidence that one of its figures was a verified 4 September move &mdash; also remains off the page.</p>''',
    '''A mid-morning semiconductor list refused in an earlier edition &mdash; on the evidence that one of its figures was a verified 4 September move &mdash; also remains off the page.</p>
<p style="margin:9px 0 0"><b>Also refused this run:</b> a sector-performance tool page giving <b>energy down 3.20%</b> &ldquo;as of the afternoon session&rdquo;. It carries no date on the figure itself and it contradicts every other read of this session, in which energy is the leading sector on a crude rally that has Brent near $100. An undated number that points the opposite way from the day&#39;s central story is not a correction to it, so no energy sector percentage is printed on this page.</p>''')

# ---------------- weekly scorecard note ----------------
rep('''<p class="note">These are the most recent official closes, re-verified against source this run:''',
    '''<p class="note">Re-verified against source again this edition, unchanged to the cent. These are the most recent official closes:''')

# ---------------- rates: fed odds ----------------
rep('''and a <b>31 August</b> read gave <b>66%</b>. The band printed on this page therefore widens this edition to <b>49&ndash;66%</b>, and is printed as a range rather than averaged.''',
    '''and a <b>31 August</b> read gave <b>66%</b>. A fresh read this run puts it at <b>roughly 60%</b> for a 25 basis point hike &ldquo;next week&rdquo;, which falls inside the existing band. The band printed on this page therefore holds at <b>49&ndash;66%</b> and is printed as a range rather than averaged. <b>The decision itself is Wednesday 16 September at 2:00 PM ET, with the chair&#39;s press conference at 2:30 PM ET.</b>''')

# ---------------- on the radar ----------------
rep('''<li><b>August CPI, Friday 11 September</b> &mdash; described this run as the pivotal input for the hike-versus-hold argument. <b>PPI and Treasury auctions</b> are also on the week&#39;s slate, and investors returned from the long weekend awaiting all three.</li>''',
    '''<li><b>August CPI lands Friday 11 September at 8:30 AM ET</b> &mdash; five days before the Fed decides, which is why this run&#39;s reads call it the most market-sensitive data point on the autumn calendar and the pivotal input for the hike-versus-hold argument. <b>PPI and Treasury auctions</b> are also on the week&#39;s slate.</li>''')

rep('''<li><b>Oracle&#39;s fiscal Q1 2027 report lands 10 September</b>, with an estimated EPS of <b>$1.67</b>.</li>''',
    '''<li><b>Oracle reports Thursday 10 September</b> &mdash; its fiscal Q1 2027, with an estimated EPS of <b>$1.67</b>. This run&#39;s reads frame it as a bellwether for the state of AI financing, given the company&#39;s turn toward debt.</li>''')

rep('''<li><b>The August payrolls consensus still has three numbers attached to it.</b> The actual print was <b>162,000</b> jobs &mdash; about three times expected growth &mdash; with unemployment unchanged at <b>4.1%</b> and average hourly earnings up <b>3.1%</b> year over year. A source this run gives the consensus as <b>55,000</b>; the figure this desk verified repeatedly in earlier editions is <b>53,000</b>; <b>56,000</b> has also returned. All three are printed with what each is, because a fresh number that contradicts a verified one is often a different statistic rather than a correction.</li>''',
    '''<li><b>The payrolls consensus now has a name attached to it.</b> The actual August print was <b>162,000</b> jobs, with unemployment unchanged at <b>4.1%</b> and average hourly earnings up <b>3.1%</b> year over year. This run gives the consensus as <b>53,000</b> from economists polled by <b>Dow Jones</b> &mdash; the figure this desk had verified repeatedly &mdash; while a separate read this run gives <b>56,000</b> and an earlier edition saw <b>55,000</b>. The 53,000 is the one now tied to a named survey, so it is the one used; the others are kept on the page because different surveys legitimately produce different consensus numbers.</li>''')

io.open(p, "w", encoding="utf-8").write(s)
print("ws edits:", n)
