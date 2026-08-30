# -*- coding: utf-8 -*-
"""Edition edits for the Sunday 2026-08-30 ~4:06 PM ET run (eighth of the day)."""
import re, sys, io, os

D = sys.argv[1]
def rd(f): return io.open(os.path.join(D,f), encoding='utf-8').read()
def wr(f,s): io.open(os.path.join(D,f),'w',encoding='utf-8').write(s)

fails = []
def sub(s, old, new, label):
    if old not in s:
        fails.append('MISSING ANCHOR: ' + label); return s
    if s.count(old) != 1:
        fails.append('AMBIGUOUS ANCHOR (%d): %s' % (s.count(old), label)); return s
    return s.replace(old, new)

# ─────────────────────────── CYBER ───────────────────────────
c = rd('cyber-briefing.html')

c = sub(c,
 '<div class="tldr"><b>The Wire</b> <span>A <b>$5.72 million theft across six blockchains</b>',
 '<div class="tldr"><b>The Wire</b> <span>A <b>CVSS 9.8 unauthenticated remote-code-execution flaw in Windows DNS Server</b> is new to this board and it is on it for reachability rather than activity &mdash; <b>CVE-2026-62878</b> is a stack-based buffer overflow reachable by one crafted packet with <b>no user interaction</b>, it affects Windows Server releases from <b>2012 through 2025</b>, researchers call it <b>potentially wormable</b>, and it is <b>neither exploited nor publicly disclosed</b>; a <b>fifteenth KEV check</b> returned nothing dated later than August 27 for a ninth consecutive time, and the <b>two federal deadlines due today</b> &mdash; CVE-2023-49105 in ownCloud and CVE-2026-53362 in the Linux kernel &mdash; were re-read against a 4 PM clock and still fall <b>Sunday, August 30</b>; and an aggregate count of August&rsquo;s KEV additions came back <b>a second way and neither number is adopted</b>. Carried from the previous edition: a <b>$5.72 million theft across six blockchains</b>',
 'cyber tldr')

c = sub(c,
 '<b>Added this run:</b> a critical flaw in the shared <b>Cosmos EVM</b> module was used to drain <b>$5.72 million from six blockchains</b> between August 20 and August 25 &mdash; four months after it was reported and cleared as harmless.',
 '<b>Added this run:</b> <b>CVE-2026-62878</b>, an unauthenticated <b>9.8</b> remote-code-execution flaw in <b>Windows DNS Server</b>, joins the board on severity and reachability &mdash; it is <b>not</b> under exploitation, and the threat level is unchanged by it. Carried: a critical flaw in the shared <b>Cosmos EVM</b> module was used to drain <b>$5.72 million from six blockchains</b> between August 20 and August 25 &mdash; four months after it was reported and cleared as harmless.',
 'cyber threat banner')

# New CVE row, inserted immediately after the Microsoft QUIC row (same release, same posture).
quic_end = 'The only flaw in that release confirmed under exploitation remains <b>CVE-2026-68820</b>.</td></tr>'
dns_row = quic_end + '\n<tr><td><code>CVE-2026-62878</code></td><td>9.8</td><td>Windows DNS Server</td><td><span class="tag new">New &middot; 4:06 PM</span> <b>Stack-based buffer overflow giving unauthenticated remote code execution with elevated privileges</b>, triggered by sending a specially crafted packet to an affected service over the network, with <b>no user interaction</b> required. Shipped in the same August Patch Tuesday release as the row above, and described there as <b>one of four unauthenticated, network-reachable 9.8 RCE flaws</b> in that release. <b>Zero Day Initiative singled this one out</b> of the four, on the grounds that DNS is a fundamental service in every Windows Server domain environment and DNS servers commonly sit on the network perimeter; other researchers describe it as <b>potentially wormable</b> for the same reason. Affected: <b>Windows Server releases from 2012 through 2025</b>, plus listed Windows 10 versions carrying the component. &#9888; <b>Neither exploited in the wild nor publicly disclosed as of the advisory date</b>, and <b>not KEV-listed</b> on anything fetched this run &mdash; the wormability is a researcher&rsquo;s characterisation of what the flaw would permit, <b>not a report of it happening</b>, and this page prints the distinction rather than collapsing it. The only flaw in the August release confirmed under exploitation remains <b>CVE-2026-68820</b>.</td></tr>'
c = sub(c, quic_end, dns_row, 'cyber DNS row insert')

# KEV / aggregate-count note, appended to the Gitea row's closing note (last row of the table).
gitea_tail = '<b>two days past</b> either way.</td></tr>'
c = sub(c, gitea_tail,
 '<b>two days past</b> either way. <b>Unchanged at a fifteenth check, 4:06 PM.</b> CISA&rsquo;s own alert pages returned again for <b>August 7</b> (one: <code>CVE-2026-8037</code>, Progress LoadMaster command injection &mdash; the same vendor-CVSS-9.6 flaw this project&rsquo;s standing corrections file records), <b>August 11</b> (three), <b>August 18</b> (four), <b>August 20</b> (two) and <b>August 26</b> (six). <b>Nothing dated later than August 27</b> for a ninth consecutive check. &#9888; <b>A second aggregate arrived and neither is adopted:</b> one summary this run puts August&rsquo;s additions at <b>&ldquo;at least 16&rdquo;</b> where a tracker read in an earlier edition put them at <b>24</b>. Both are third-party counts of a catalogue this page checks one alert page at a time, and <b>with three known gaps across fifteen checks this page will not certify either as complete</b> &mdash; the individual dated alert pages are what it publishes from.</td></tr>',
 'cyber KEV fifteenth check')

wr('cyber-briefing.html', c)

# ─────────────────────────── MARKETS ───────────────────────────
w = rd('wallstreet-briefing.html')

w = sub(w,
 '<div class="tldr"><b>The Tape</b> <span>The tape is shut for the weekend and Friday&rsquo;s closes stand for a <b>twenty-third verification</b>',
 '<div class="tldr"><b>The Tape</b> <span>The speech that moved the September pricing now has <b>two more of its own sentences on this page</b> &mdash; Kevin Warsh called the 2% goal <b>&ldquo;a firm, fixed target&rdquo;</b> and put <b>&ldquo;responsibility for 65 months of sustained, elevated inflation&hellip; squarely with the central bank&rdquo;</b>, which is the hawkish read stated in his own words rather than in a summary of them; a <b>fourth Friday index figure</b> arrived and is <b>recorded rather than promoted</b>, because the <b>Nasdaq 100</b> closing <b>29,433.43, &minus;0.70%</b> is a different index from the <b>Composite</b> this page&rsquo;s scorecard tracks; and the tape is shut for the weekend with Friday&rsquo;s closes standing for a <b>twenty-fourth verification</b>',
 'ws tldr')

lead_anchor = '<div class="card"><span class="tag new">New &middot; 3:36 PM</span><h3>A twenty-third verification, and this run the interesting number is not a price but a date.</h3>'
new_lead = ('<div class="card"><span class="tag new">New &middot; 4:06 PM</span><h3>The hawkish read finally arrives in Warsh&rsquo;s own sentences &mdash; and a fourth Friday index number is recorded without being promoted.</h3>'
 '<p><b>Two direct quotations, and they sharpen a characterisation this page has been carrying second-hand.</b> Every edition since Friday has described the Jackson Hole address as hawkish on the strength of what coverage said about it. A report fetched this run quotes the Chair directly on both halves of the argument: he reaffirmed that the Fed&rsquo;s 2% inflation goal is <b>&ldquo;a firm, fixed target&rdquo;</b>, and he placed <b>&ldquo;responsibility for 65 months of sustained, elevated inflation&hellip; squarely with the central bank&rdquo;</b>. '
 'Read together those are an argument about credibility rather than about any single data print, which is a different claim from &ldquo;inflation is running hot&rdquo; and explains why the pricing moved as far as it did on a speech containing no new data. This page already carried one Warsh sentence, on the summer PCE and CPI readings; <b>these are additional, not a replacement for it</b>.</p>'
 '<p>&#9888; <b>A fourth Friday index figure arrived, and it is not a fourth reading of the three this page publishes.</b> The same sweep returned the <b>Nasdaq 100</b> closing Friday at <b>29,433.43, down 0.70%</b>. '
 'The Weekly Scorecard below tracks the <b>Nasdaq Composite</b>, which closed <b>26,402.42, &minus;0.52%</b> &mdash; a different index with a different membership, so the two figures do not compete and <b>neither corrects the other</b>. It is recorded here because a 0.70% decline sitting beside a 0.52% one invites exactly the substitution this page keeps refusing to make; <b>the 100 is not promoted into the Composite row</b>, and no line on this page has been changed by it. Also re-confirmed in the same sweep, with one figure sharpened: <b>WTI $83.44, &minus;0.11%</b> and <b>Brent $88.29, &minus;0.26%</b>.</p>'
 '<p><b>One forward-looking read is printed as attribution and not as a forecast.</b> An analyst reading of the same speech, fetched this run, holds that a hike <b>probably will not come in September but will arrive by October or December</b>. That is one interpretation of a question two venues already answer differently on this page &mdash; CME at 57/43 for a hike, Polymarket and Kalshi both at 52% for a hold &mdash; and it is <b>attributed rather than adopted</b>, for an eleventh consecutive read. <b>The FOMC date is unchanged and not in dispute: September 16.</b></p></div>\n'
 + lead_anchor)
w = sub(w, lead_anchor, new_lead, 'ws lead insert')

wr('wallstreet-briefing.html', w)

# ─────────────────────────── MMA ───────────────────────────
m = rd('mma-briefing.html')

m = sub(m,
 '<div class="tldr"><b>Tale of the Tape</b> <span>The <b>UFC 333 card has filled out from two title fights into a full main card</b>',
 '<div class="tldr"><b>Tale of the Tape</b> <span>The <b>Paris card finally has a betting line</b>, and it arrived in <b>three different renderings that this page prints as a spread rather than a price</b> &mdash; <b>Salahdine Parnasse</b> is a heavy favourite over <b>Dan Hooker</b> at every book returned, quoted anywhere from <b>&minus;400 to &minus;500</b> with Hooker <b>+292 to +375</b>, which fills a gap this page had explicitly flagged as empty for several editions; a <b>fourth September card</b> joins the schedule; and a <b>start-time conflict on UFC 331 is recorded rather than resolved</b>. Carried: the <b>UFC 333 card has filled out from two title fights into a full main card</b>',
 'mma tldr')

paris_anchor = '<b>13 bouts, with Fares Ziam vs. Axel Sola'
# find the Paris card's trailing "no betting line" sentence uniquely by its neighbourhood
paris_no_odds = 'Daniel Benouaich vs.'
m_idx = m.find(paris_no_odds)
if m_idx < 0:
    fails.append('MISSING ANCHOR: paris card body')
else:
    tail_marker = '</p>'
    # append the odds paragraph at the end of the Paris card's final paragraph
    end = m.find('</div>', m_idx)
    close_p = m.rfind('</p>', m_idx, end)
    if close_p < 0:
        fails.append('MISSING ANCHOR: paris card closing </p>')
    else:
        odds_p = ('</p><p><b>New at 4:06 PM &mdash; the line this card did not have.</b> Every previous edition carrying UFC Fight Night 287 ended on the same sentence: no source seen had stated a betting line, so none was printed. '
          'One has now been stated, three times, by three different books, and <b>the three do not agree closely enough to quote as a price</b>. A sportsbook quoted in reporting this run has <b>Parnasse &minus;400, Hooker +300</b>; a consensus line has <b>Parnasse &minus;428, Hooker +292</b>; and the promotion&rsquo;s own event page has <b>Parnasse &minus;500, Hooker +375</b>. '
          '<b>Odds: Parnasse &minus;400 to &minus;500 / Hooker +292 to +375 (three books).</b> &#9888; <b>The spread is printed and no single figure is adopted</b> &mdash; a hundred points of moneyline between the widest and narrowest quote is not a rounding difference, and this page has no source stating which of the three is a closing line rather than an opening one. '
          'What all three agree on is the direction, and it is emphatic: <b>the debuting former KSW champion is a heavy favourite over the UFC veteran</b>, which is an unusual way round for a promotional newcomer and is the reason the line is worth printing at all.</p>')
        m = m[:close_p] + odds_p + m[close_p+4:]

# UFC 331 start-time conflict
m = sub(m,
 '13 fights total; prelims 6 PM ET, main card 9 PM ET, Paramount+. No betting line for this card was\nstated by any source seen this run, so none is printed.',
 '13 fights total; prelims 6 PM ET, main card 9 PM ET, Paramount+. &#9888; <b>A start-time conflict is recorded at 4:06 PM and not resolved.</b> A schedule aggregator fetched this run puts the UFC 331 main card at <b>5 PM ET</b>, where this page carries <b>9 PM ET</b> from its earlier sourcing. <b>Neither is adopted over the other</b> &mdash; an aggregator listing many events at once is not the promotion&rsquo;s own page, and a Los Angeles card can plausibly be listed either way depending on whether a schedule is quoting local or Eastern time. The date, venue and card are unaffected. No betting line for this card was stated by any source seen this run, so none is printed.',
 'mma 331 start time')

# Fourth September card
sept26 = ('<span class="tag">New &middot; 4:06 PM</span><div class="date">Sat, Sept 26 &middot; venue not stated</div>'
 '<h3>UFC Fight Night &mdash; Rosas Jr. vs. Barcelos</h3>'
 '<p><b>New to this page at 4:06 PM</b>, from the same schedule sweep that produced the Paris line above. A fourth September card: <b>Rosas Jr. vs. Barcelos</b>, listed at <b>11 fights</b>. '
 '&#9888; <b>That is the whole of what was stated.</b> No venue, no broadcast, no start time, no first names beyond the listing&rsquo;s own abbreviation and <b>no betting line</b> were given by anything fetched this run, and none is filled in here. '
 'It is added because a card this page did not have is worth listing even in outline; it is <b>marked thin on purpose</b> so that the outline is not mistaken for a confirmed booking. The same sweep re-confirmed the three cards already carried above &mdash; <b>Sept 5 Paris</b>, <b>Sept 12 Noche UFC: Rodriguez vs. Silva</b> and <b>Sept 19 UFC 331</b>.</p>')

# insert the new card just before the Paris card block
paris_card_start = m.rfind('<div class="card">', 0, m.find('Sat, Sept 5 &middot; Accor Arena'))
if paris_card_start < 0:
    fails.append('MISSING ANCHOR: paris card start')
else:
    m = m[:paris_card_start] + '<div class="card">' + sept26 + '</div>\n' + m[paris_card_start:]

wr('mma-briefing.html', m)

print('FAILS:', fails if fails else 'none')
