#!/usr/bin/env python3
"""Closing Bell edits — Sunday Aug 30 2026, ~3:36 PM ET research, seventh run of the day."""
import io, os, sys

D = sys.argv[1]
P = os.path.join(D, 'wallstreet-briefing.html')
h = io.open(P, encoding='utf-8').read()
n = 0

def sub(old, new, label):
    global h, n
    if old not in h:
        print('MISS:', label); return
    h = h.replace(old, new, 1); n += 1
    print('  ok:', label)

# ── 1. TLDR ─────────────────────────────────────────────────────────────────
i = h.find('<div class="tldr"><b>The Tape</b> <span>')
j = h.find('</span></div>', i)
new_tldr = ('<div class="tldr"><b>The Tape</b> <span>The tape is shut for the weekend and Friday&rsquo;s closes '
            'stand for a <b>twenty-third verification</b> &mdash; S&amp;P 500 <b>7,711.76</b> &minus;0.25%, '
            'Nasdaq <b>26,402.42</b> &minus;0.52%, Dow <b>53,559.99</b> &minus;9.45 points &mdash; and the '
            'September rate question got a <b>tenth read</b> that finally has a <b>dated anchor</b> under it: '
            'CME FedWatch&rsquo;s <b>57% hike</b> is stated against <b>39.9% on August 21</b>, so the move is '
            'now measurable rather than merely asserted, and the hike in question would lift the range to '
            '<b>3.75&ndash;4%</b>; against that, the seasonal case for September came back in <b>four '
            'incompatible renderings</b> and <b>none is adopted</b>; and a <b>third rendering of Friday&rsquo;s '
            '10-year close, 4.72%</b>, was recorded and refused in favour of the dated snapshot&rsquo;s 4.73%.')
h = h[:i] + new_tldr + h[j:]
n += 1
print('  ok: tldr')

# ── 2. The Lead — new top paragraph ─────────────────────────────────────────
sub('<h2 class="sec">The Lead</h2>\n<p><span class="tag new">New &middot; 3:10 PM</span>',
    '<h2 class="sec">The Lead</h2>\n'
    '<p><span class="tag new">New &middot; 3:36 PM</span> <b>A twenty-third verification, and this run the '
    'interesting number is not a price but a date.</b> Friday&rsquo;s three closes returned again in full '
    '&mdash; <b>S&amp;P 500 7,711.76, &minus;0.25%</b>; <b>Nasdaq Composite 26,402.42, &minus;0.52%</b>; '
    '<b>Dow 53,559.99, &minus;9.45 points, &minus;0.02%</b> &mdash; from a live-blog wrap headlined on the '
    'same fact this page has led with all weekend, that the week finished green while Friday finished red as '
    'rate-hike bets jumped. <b>What is new is that the September pricing finally has a prior attached to it.</b> '
    'For nine consecutive runs this page has printed CME FedWatch&rsquo;s hike probability without being able '
    'to say what it had moved <i>from</i>. A source fetched this run states it: <b>57% today against 39.9% on '
    'August 21</b> &mdash; a swing of roughly <b>17 points in a week</b>, either side of Kevin Warsh&rsquo;s '
    'Jackson Hole speech. It also states what the hike would do, which this page had never printed: lift the '
    'target range from <b>3.50&ndash;3.75%</b> to <b>3.75&ndash;4%</b>. <b>A probability with a dated prior is '
    'a different object from a probability on its own</b> &mdash; the first can be checked next week, the '
    'second cannot. &#9888; <b>The venue split is unchanged and still not adopted:</b> CME at 57/43 for a hike, '
    '<b>Polymarket and Kalshi both at 52% for a hold</b>. A tenth read, and a tenth refusal to publish one '
    'number for a question the venues answer differently.</p>\n'
    '<p><span class="tag warn">Refused &middot; 3:36 PM</span> <b>A third rendering of Friday&rsquo;s 10-year '
    'close arrived, and it loses to the one already in the table.</b> A yields-and-oil result fetched this run '
    'puts the 10-year Treasury at <b>4.72%</b> on August 28. This page carries <b>4.73%</b> from a dedicated '
    'end-of-day Treasury series dated to that session, now returned three separate times, and reconciled at '
    '2:39 PM against the intraday <b>4.67%</b> by a source that stated both in one breath. <b>A one-basis-point '
    'difference is still a difference</b>, and the tie-break is not the size of the gap but the specificity of '
    'the source: a dated end-of-day series beats a mixed rates-and-commodities round-up. <b>4.72% is recorded '
    'and not adopted.</b> The same result put <b>Brent at $88.29, &minus;0.26%</b>, which is a precise form of '
    'a figure this page carried as &ldquo;~$88&rdquo; &mdash; that one is taken up, because it sharpens a '
    'number rather than contradicting one.</p>\n'
    '<p><span class="tag new">New &middot; 3:10 PM</span>',
    'lead new paras')

# ── 3. Rates table — Brent precision ────────────────────────────────────────
sub('<tr><td>Brent crude</td><td>~$88 a barrel</td><td>Fri, Aug 28</td></tr>',
    '<tr><td>Brent crude</td><td><b>$88.29</b>, &minus;0.26% on the day &mdash; a commodity tracker fetched at '
    '3:36 PM puts a precise figure on the &ldquo;~$88&rdquo; this page carried; the round form is retired</td>'
    '<td>Fri, Aug 28</td></tr>',
    'brent precision')

# ── 4. Rates table — record the 4.72% variant against the 10-year row ───────
sub('the third independent return of the pair and the reason the retired ~4.67% stays retired.',
    'the third independent return of the pair and the reason the retired ~4.67% stays retired. '
    '&#9888; <b>A third rendering, 4.72%, arrived at 3:36 PM and was refused</b> &mdash; one basis point below '
    'the dated close, from a general rates-and-oil round-up rather than a Treasury series. It is recorded in '
    'The Lead and is not promoted into this table.',
    '4.72 variant')

# ── 5. On the Radar — seasonality spread + the Monday/Tuesday calendar ──────
sub('<h2 class="sec" id="radar">On the Radar</h2>\n<div class="panel"><ul class="bul">\n',
    '<h2 class="sec" id="radar">On the Radar</h2>\n<div class="panel"><ul class="bul">\n'
    '<li><span class="tag new">New &middot; 3:36 PM</span> <b>September&rsquo;s reputation came back in four '
    'incompatible forms, which is the argument for printing the spread rather than the stat.</b> Every source '
    'fetched this run agrees September is historically the weakest month for the S&amp;P 500 and none of them '
    'agrees on by how much. One puts the average September return at <b>&minus;0.7% over the last 75 years</b>; '
    'a seasonality service puts it at <b>&minus;0.7% over 50 years with gains 46% of the time</b>; a third goes '
    'back to <b>1928</b> for an average of <b>&minus;1.2%</b>; a fourth, also from 1928, renders it '
    '<b>&minus;1.17%</b>. On frequency, one states the index has been positive in September only <b>44% of the '
    'time since 1950</b>, the lowest of any month, against the seasonality service&rsquo;s <b>46%</b>. '
    '<b>Different start years and different return definitions almost certainly explain the gap &mdash; but no '
    'source fetched this run states its own basis</b>, so none of the four is adopted and the range is printed '
    'instead: <b>an average September loss somewhere between 0.7% and 1.2%, positive in 44&ndash;46% of years</b>. '
    '&#9888; <b>And the conditional matters more than the average.</b> One analysis states that when the index '
    'enters September <b>above its 200-day moving average</b>, the average September return turns <b>positive at '
    '+1.3%</b> with <b>60%</b> of occurrences green, against <b>&minus;4.2%</b> and only <b>15%</b> green when '
    'it enters below. <b>This page does not state which side of its 200-day the S&amp;P 500 is on</b>, because '
    'no source fetched this run says so &mdash; which is exactly why the conditional is printed and the '
    'conclusion is not.</li>\n'
    '<li><span class="tag new">New &middot; 3:36 PM</span> <b>The two sessions either side of the month-end '
    'are, on the calendar, unusually empty and then not.</b> A week-ahead outlook fetched this run states that '
    '<b>Monday, August 31 &mdash; the final trading day of August &mdash; carries no major earnings or '
    'scheduled events</b>, and that <b>Tuesday, September 1</b> brings <b>July construction spending</b> '
    'alongside the <b>August ISM Manufacturing PMI</b>. The ISM print corroborates the Tuesday entry this page '
    'already carries from a separate preview; <b>construction spending is new to this page</b>. Nothing here '
    'moves payrolls, which stay <b>Friday, September 4 at 8:30 AM</b>.</li>\n',
    'radar seasonality + calendar')

# ── 6. Sources ──────────────────────────────────────────────────────────────
sub('<a href="https://finance.yahoo.com/markets/stocks/articles/stock-market-news-aug-28-133400922.html">',
    '<a href="https://finance.yahoo.com/markets/live/stock-market-today-friday-august-28-dow-sp-500-nasdaq-dip-fed-warsh-jackson-hole-speech-081514091.html">Yahoo Finance &mdash; Dow, S&amp;P 500, Nasdaq end week on down note as rate-hike bets jump (Aug 28 closes)</a><br>'
    '<a href="https://news.bitcoin.com/finance/fedwatch-turns-hawkish-with-57-odds-of-september-rate-increase/">FedWatch turns hawkish: 57% odds of a September increase, against 39.9% on Aug 21; range would move to 3.75&ndash;4%</a><br>'
    '<a href="https://equityclock.com/2026/08/28/stock-market-outlook-for-august-31-2026/">Equity Clock &mdash; Stock market outlook for August 31, 2026 (September &minus;0.7% over 50 years, 46% frequency of gains; Sept 1 construction spending and ISM)</a><br>'
    '<a href="https://www.chase.com/personal/investments/learning-and-insights/article/september-worst-month-for-stocks-what-investors-can-do">Chase &mdash; Why September is historically the worst month for stocks</a><br>'
    '<a href="https://www.investing.com/analysis/sp-500-seasonality-shows-september-as-weakest-month-but-trend-matters-more-200666084">Investing.com &mdash; S&amp;P 500 seasonality: September weakest, but the 200-day trend matters more</a><br>'
    '<a href="https://www.fool.com/investing/2026/08/27/history-says-september-is-the-worst-month-for-stoc/">The Motley Fool &mdash; History says September is the worst month for stocks</a><br>'
    '<a href="https://tradingeconomics.com/united-states/government-bond-yield">Trading Economics &mdash; US 10-year Treasury yield (4.72% rendering, recorded and refused)</a><br>'
    '<a href="https://finance.yahoo.com/markets/stocks/articles/stock-market-news-aug-28-133400922.html">',
    'ws sources')

io.open(P, 'w', encoding='utf-8').write(h)
print(f'wallstreet edits applied: {n}')
