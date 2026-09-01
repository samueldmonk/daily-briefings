# -*- coding: utf-8 -*-
import io
P='/tmp/db_1788305419/mma-briefing.html'
s=io.open(P,encoding='utf-8').read(); n=0
def rep(old,new,label):
    global s,n
    c=s.count(old)
    if c!=1: print(('MISS: ' if c==0 else 'AMBIG(%d): '%c)+label); return False
    s=s.replace(old,new); n+=1; print('ok:',label); return True

# M1 -- TLDR
rep('while the main event holds with debutant Salahdine Parnasse a &minus;600 favourite over Dan Hooker, a price implying 81.8%, '
    'Contender Series Week 4 runs tonight at the Meta APEX, and a champions list fetched this run is stale for a thirteenth time, wrong in one cell.',
    'while the main event holds with debutant Salahdine Parnasse a &minus;600 favourite over Dan Hooker on the consensus line &mdash; a price implying 81.8%, '
    'though a fourth book fetched this run quotes it as short as &minus;526 &mdash; Contender Series Week 4 is now under way at the Meta APEX with no result yet verified, '
    'and a champions list fetched this run is stale for a fourteenth time, wrong in the same single cell as last time.',
    'M1 tldr')

# M2 -- DWCS card: tonight -> under way
rep('Five fights tonight at the Meta APEX, main card 7 PM ET on Paramount+; fighters weighed in yesterday.',
    'Five fights at the Meta APEX, main card 7 PM ET on Paramount+; fighters weighed in yesterday. '
    '<b>The card is now under way</b> &mdash; the 7 PM ET start has passed. '
    '&#9888; <b>No result from it appears anywhere on this page.</b> Searches run this run returned the card, the weigh-ins and the preview but '
    '<b>no verified winners and no contract announcements</b>, which is what a live event looks like from the outside. '
    'The most recent <i>completed</i> event on this page remains UFC Shanghai on August 29.',
    'M2 dwcs underway')

rep('Week 4 runs tonight.</p>', 'Week 4 is under way as this edition publishes; its contract winners are not yet verified and are not listed.</p>', 'M2b week4 ledger line')

# M3 -- odds: add the fourth book
rep('Odds: consensus Parnasse &minus;600 / Hooker +425; DraftKings &minus;600 / +440; a second book at &minus;667 / +417 and a third at &minus;575 / +431.',
    'Odds: consensus Parnasse &minus;600 / Hooker +425; DraftKings &minus;600 / +440; a second book at &minus;667 / +417 and a third at &minus;575 / +431. '
    'A <b>fourth</b> book fetched this run, <b>Caesars, is materially shorter at &minus;526 / +372</b>. '
    '&#9888; <b>That widens the spread rather than settling it:</b> the books now run from &minus;526 to &minus;667 on the same fighter, '
    'and the consensus &minus;600 is a summary of a disagreement, not a price anyone is actually offering everywhere. '
    'The DraftKings and second-book quotes were <b>re-confirmed unchanged</b> this run.',
    'M3 odds fourth book')

# M4 -- champions note
rep('&#9888; <b>A thirteenth stale champions list was fetched this run, and it was wrong in exactly one cell.</b>',
    '&#9888; <b>A fourteenth stale champions list was fetched this run, and it was wrong in exactly one cell &mdash; the same cell as last time.</b>',
    'M4a')
rep('<b>Error counts across the last six sightings: 1, 3, 1, 3, 1, 1.</b>',
    '<b>Error counts across the last seven sightings: 3, 1, 3, 1, 1, 1.</b> '
    '&#9888; <b>Two consecutive fetches have now failed in the identical cell</b>, which is new: '
    'the previous pattern was a wrong cell that moved around. <b>It does not change the board and it does not change the rule</b> &mdash; '
    'every cell is checked every run regardless of which one failed last &mdash; but a repeat in the same position is worth recording, '
    'because a stable error is easier to mistake for a stable fact than a wandering one.',
    'M4b')
rep('<b>The board below is the verified one and it is unchanged for a thirteenth consecutive edition.</b>',
    '<b>The board below is the verified one and it is unchanged for a fourteenth consecutive edition.</b>',
    'M4c')

# M5 -- sources
rep('<h2>Sources</h2><div class="panel srcs">',
 '<h2>Sources</h2><div class="panel srcs">'
 '<a href="https://www.espn.com/mma/story/_/id/14947566/current-all-ufc-champions" target="_blank" rel="noopener">ESPN &mdash; current and all-time UFC champions (cross-checked this run)</a> &middot; '
 '<a href="https://www.espn.com/mma/fightcenter/_/id/600060735/league/ufc" target="_blank" rel="noopener">ESPN &mdash; DWCS Season 10 Week 4 live fight coverage</a> &middot; '
 '<a href="https://www.ufc.com/event/ufc-fight-night-september-05-2026" target="_blank" rel="noopener">UFC.com &mdash; UFC Fight Night: Hooker vs. Parnasse</a> &middot; '
 '<a href="https://www.wagertalk.com/news/mma/ufc-fight-night-hooker-vs-parnasse-picks-predictions-and-odds-september-5-2026/" target="_blank" rel="noopener">WagerTalk &mdash; Hooker vs. Parnasse odds across books (Sept 5)</a> &middot; '
 '<a href="https://www.ufc.com/news/dana-whites-contender-series-season-10-week-4-results" target="_blank" rel="noopener">UFC.com &mdash; DWCS Season 10 Week 4 results + scorecards</a> &middot; ',
 'M5 sources')

io.open(P,'w',encoding='utf-8').write(s); print('applied',n)
