#!/usr/bin/env python3
# Sept 2, 2026 -- 9:35 AM ET run. MMA page: UFC.com odds board resolved and published,
# main-card/prelim split corrected, champions board re-verified (17th stale-list sighting).
import re, sys
P = 'mma-briefing.html'
h = open(P, encoding='utf-8').read()
orig = h; n = 0

def sub(pattern, repl, count=1, flags=0, label=''):
    global h, n
    new, k = re.subn(pattern, lambda m: repl, h, count=count, flags=flags)
    if k != count:
        print('FAIL[%s]: matched %d expected %d' % (label, k, count)); sys.exit(1)
    h = new; n += k

# ------------------------------------------------------------------ 1. TL;DR
sub(r'<b>Tale of the Tape</b> <span>.*?</span></div>',
    '<b>Tale of the Tape</b> <span>UFC.com now carries a price on every one of Saturday&rsquo;s fourteen Paris bouts, '
    'and this page can finally read them: the main-event line is <b>Parnasse &minus;550 / Hooker +400</b>, with the '
    'promotion&rsquo;s own board confirming that the debuting two-division KSW champion is the favourite over a man '
    'in his fourth UFC main event &mdash; while the card&rsquo;s biggest surprise is on the prelims, where '
    'promotional newcomer <b>Pavel Andrusca</b> is favoured at <b>&minus;130</b> over the ranked veteran '
    '<b>Nathaniel Wood</b>.</span></div>',
    flags=re.S, label='tldr')

# ------------------------------------------------------------------ 2. Paris card block -> full odds board
sub(r'<p><b>Dan Hooker \(155\) vs\. Salahdine Parnasse</b>.*?submitting Ismael Bonfim in the first round in July\.</p>',
    '<p><b>Dan Hooker (#10) vs. Salahdine Parnasse</b>, five rounds at lightweight. Parnasse is a <b>promotional '
    'newcomer</b> &mdash; a former two-time KSW featherweight champion and one-time KSW lightweight champion, '
    '<b>23-2 with fifteen finishes</b>, handed a main event on debut. <b>UFC.com&rsquo;s own card lists the fight at '
    'Hooker +400 / Parnasse &minus;550.</b> Across other books this desk has fetched, Hooker has been available from '
    '<b>+360 to +450</b> and Parnasse from roughly <b>&minus;500 to &minus;700</b>, DraftKings at &minus;600 / +440, '
    'off an opening line near &minus;400 / +300. <b>The range is printed and no average is taken.</b></p>\n'
    '<p class="note" style="border-left:3px solid var(--accent2);padding-left:11px"><b>A refusal this page made '
    'yesterday is now resolved, and the way it was resolved is the point.</b> The previous edition declined to print '
    'UFC.com odds because the promotion&rsquo;s card renders a bout as &ldquo;+275 odds -350&rdquo; between two names '
    '<b>without saying which price belongs to which man</b>, and layout order alone is not a key. This run the same '
    'page was read across <b>all fourteen bouts at once</b>, and five of them can be checked against independent '
    'quotes fetched separately: Ziam&ndash;Sola, Page&ndash;Ruziboev, Keita&ndash;Naimov, Charriere&ndash;Lima and '
    'Donchenko&ndash;Soriano <b>all resolve the same way &mdash; the first price belongs to the first-named '
    'fighter</b>, and in every case the favourite/underdog assignment matches the outside book. <b>Five independent '
    'confirmations establish the convention, so the main-event line can now be assigned.</b> The ambiguity was in the '
    'single row, not in the page; reading the whole table dissolved it.</p>\n'
    '<p><b>Main card &mdash; UFC.com, with its prices (3 PM ET, Paramount+):</b> Hooker <b>+400</b> / Parnasse '
    '<b>&minus;550</b> (LW) &middot; Far&egrave;s Ziam <b>&minus;145</b> / Axel Sola <b>+125</b> (LW) &middot; '
    'Michael &ldquo;Venom&rdquo; Page (#15) <b>&minus;175</b> / Nursulton Ruziboev <b>+145</b> (MW) &middot; '
    'Daniil Donchenko <b>&minus;245</b> / Punahele Soriano <b>+200</b> (WW) &middot; Kurtis Campbell '
    '<b>&minus;390</b> / Trevor Peek <b>+310</b> (FW) &middot; Losene Keita <b>&minus;360</b> / Muhammad Naimov '
    '<b>+280</b> (FW).</p>\n'
    '<p><b>Prelims &mdash; UFC.com (12 PM ET):</b> Morgan Charriere <b>+155</b> / Felipe Lima <b>&minus;185</b> '
    '&middot; Mario Pinto <b>&minus;275</b> / Ryan Spann <b>+225</b> (HW) &middot; Oumar Sy <b>&minus;210</b> / '
    'Modestas Bukauskas <b>+175</b> (LHW) &middot; <b>Nathaniel Wood +110 / Pavel Andrusca &minus;130</b> at '
    'featherweight &middot; Michael Aljarouj <b>&minus;130</b> / Fabia Sintes <b>+110</b> (FLW) &middot; '
    'Nora Cornolle (#13) <b>&minus;125</b> / Klaudia Sygula <b>+105</b> (W-BW) &middot; Matthieu Duclos '
    '<b>&minus;115</b> / Luis Felipe Dias <b>&minus;105</b> (MW) &middot; Delphine Benouaich <b>&minus;150</b> / '
    'Sofia Montenegro <b>+125</b> (W-SW).</p>\n'
    '<p class="note" style="border-left:3px solid var(--crit);padding-left:11px"><b>A correction to this page.</b> '
    'The previous edition placed <b>Charriere vs. Lima on the main card and Campbell vs. Peek on the prelims</b>. '
    'UFC.com&rsquo;s card, re-read primary this run, has them <b>the other way round</b>: Campbell&ndash;Peek is the '
    'sixth main-card bout and Charriere&ndash;Lima opens the prelims. Corrected above.</p>\n'
    '<p><b>The line that stands out is not the main event.</b> <b>Pavel Andrusca is a &minus;130 favourite over '
    'Nathaniel Wood</b> &mdash; a promotional newcomer, brought in when <b>Mairon Santos</b> withdrew with an '
    'unspecified health problem, priced above a ranked and long-tenured opponent. <b>Nothing fetched this run '
    'explains why the market sees it that way</b>, and no explanation is invented; the price is simply reported. '
    'Start times remain unusual for a UFC card: prelims <b>12 PM ET / 9 AM PT</b>, main card <b>3 PM ET / 12 PM PT</b>. '
    'In the co-main, Ziam entered 2026 on a six-fight winning streak that Tom Nolan halted in June; he is <b>2-0 in '
    'Paris</b> and knocked out Matt Frevola on his last appearance there. Sola most recently submitted Ismael Bonfim '
    'in the first round in July.</p>',
    flags=re.S, label='paris')

# tag the Paris card New-ish marker
sub(r'(<div class="card"><div class="tags"><span class="tag t-a">Next up</span><span class="tag t-c">Main event</span>)</div>',
    '<div class="card"><div class="tags"><span class="tag t-a">Next up</span><span class="tag t-c">Main event</span>'
    '<span class="tag t-new">Odds board resolved</span></div>', label='paris-tag')

# ------------------------------------------------------------------ 3. UFC 331 times
sub(r'Thirteen fights; prelims 6 PM ET, main card 9 PM ET, Paramount\+\.',
    'Thirteen fights, on Paramount+. <b>The undercard timings changed between reads and both are recorded:</b> the '
    'previous edition had prelims at 6 PM ET; a listing fetched this run gives a three-tier schedule &mdash; '
    '<b>early prelims about 5 PM ET, prelims 7 PM ET, main card 9 PM ET</b>. <b>The 9 PM main card is the one figure '
    'both reads agree on</b>, so it is the one to rely on. Also confirmed on the card this run: '
    '<b>Renato Moicano vs. Brian Ortega</b> and <b>Patricio Pitbull vs. Doo Ho Choi</b>.',
    label='ufc331')

# ------------------------------------------------------------------ 4. Champions board footnote
m = re.search(r'(<h2>Champions Board</h2>)', h)
if not m: print('FAIL: champs header'); sys.exit(1)
note = ('\n<div class="note" style="border-left:3px solid var(--crit);padding-left:11px"><b>The stale champions list '
        'came back a seventeenth time, wrong in the same single cell.</b> A fresh aggregate fetch this run returned '
        '<b>middleweight = Khamzat Chimaev</b>. It is <b>Sean Strickland</b>, by split decision over Chimaev at '
        '<b>UFC 328</b> on <b>May 9, 2026</b> at the Prudential Center in Newark &mdash; two judges 48-47 Strickland, '
        'one 48-47 Chimaev, making Strickland a two-time champion and Chimaev a loser for the first time. '
        'Re-confirmed this run against <b>ESPN, UFC.com, Al Jazeera, Sky Sports and CBS Sports</b> independently. '
        'The other eleven cells came back correct. <b>Error counts across the last eleven fetches: 1, 3, 1, 3, 1, 1, '
        '1, 0, 1, 1, 1</b> &mdash; middleweight has been the sole bad cell in five of the last six, the exception '
        'being the one clean fetch at 8:19 this morning. The board below is unchanged for a <b>seventeenth '
        'consecutive edition</b>.</div>\n')
h = h[:m.end(1)] + note + h[m.end(1):]; n += 1

# ------------------------------------------------------------------ 5. Sources
m = re.search(r'(<h2>Sources</h2><div class="panel srcs">\n?)', h)
if not m: print('FAIL: mma sources'); sys.exit(1)
srcs = ('<a href="https://www.ufc.com/event/ufc-fight-night-september-05-2026">UFC.com &mdash; UFC Fight Night: Hooker vs Parnasse, official card and odds (page modified Sept 1, 3:54 PM ET)</a><br>\n'
        '<a href="https://www.espn.com/mma/ufc/story/_/id/48728368/strickland-stuns-chimaev-ufc-middleweight-title">ESPN &mdash; Strickland stuns Chimaev for the UFC middleweight title (UFC 328)</a><br>\n'
        '<a href="https://www.ufc.com/news/ufc-328-chimaev-vs-strickland-results-highlights-main-card-winners-interviews-newark">UFC.com &mdash; UFC 328 results and highlights</a><br>\n'
        '<a href="https://www.ufc.com/news/noche-ufc-take-place-september-12-ufc-returns-glendale-arizona">UFC.com &mdash; Noche UFC, September 12, Glendale</a><br>\n'
        '<a href="https://www.aljazeera.com/sports/2026/8/6/ufc-331-van-pantoja-rematch-tsarukyan-returns-and-full-fight-card">Al Jazeera &mdash; UFC 331: Van&ndash;Pantoja rematch and full fight card</a><br>\n')
h = h[:m.end(1)] + srcs + h[m.end(1):]; n += 1

open(P, 'w', encoding='utf-8').write(h)
print('OK mma: %d edits, %d -> %d bytes' % (n, len(orig), len(h)))
