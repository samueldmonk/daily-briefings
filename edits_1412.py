#!/usr/bin/env python3
"""Daily Briefings — 2026-08-30 Afternoon Edition edits (observation stamp 2:12 PM ET).
Applies this run's verified deltas onto the 1:09 PM pages."""
import re, sys, io, os

D = sys.argv[1]
FAIL = []

def load(n):
    return io.open(os.path.join(D, n), encoding='utf-8').read()

def save(n, h):
    io.open(os.path.join(D, n), 'w', encoding='utf-8').write(h)

def rep(h, old, new, label, count=1):
    n = h.count(old)
    if n != count:
        FAIL.append(f'{label}: expected {count} occurrence(s), found {n}')
        return h
    return h.replace(old, new)

# ───────────────────────────── WALL STREET ─────────────────────────────
ws = load('wallstreet-briefing.html')

ws = rep(ws, 'stand for a <b>nineteenth verification</b>',
             'stand for a <b>twentieth verification</b>', 'WS tldr ordinal')

ws = rep(ws, 'the 10-year Treasury close of <b>4.73%</b> back for a fifth time from a dated yields snapshot.',
             'the 10-year Treasury close of <b>4.73%</b> back for a sixth time from a dated yields snapshot.',
             'WS tldr 10yr count')

# tldr: replace the trailing "September 5" paragraph with the calendar corroboration + seasonality
old_tail = ('&#9888; The payrolls date <b>&ldquo;September 5&rdquo; was rejected a second consecutive run on its own '
            'weekday</b> &mdash; September 5 is a Saturday in 2026 &mdash; leaving the jobs report where this page '
            'already had it, <b>Friday, September 4 at 8:30 a.m.</b>')
new_tail = ('&#9888; The payrolls date <b>&ldquo;September 5&rdquo; was rejected a third consecutive run &mdash; and '
            'this time by the release calendar itself rather than by arithmetic</b>: the <b>New York Fed&rsquo;s own '
            'economic-indicators calendar</b> puts the <b>Employment Situation on Friday, September 4 at 8:30 AM</b>, '
            'which is exactly where this page already had it. And the first <b>seasonal</b> figure this page has '
            'carried arrived with it &mdash; the S&amp;P 500 has averaged <b>&minus;0.7% in September</b> over the past '
            '50 years, with gains in only <b>46%</b> of them, the weakest month on the calendar.')
ws = rep(ws, old_tail, new_tail, 'WS tldr tail')

# Lead time-of-day
ws = rep(ws, 'It is <b>Sunday, just past one o&rsquo;clock</b>',
             'It is <b>Sunday, early afternoon</b>', 'WS lead time-of-day')

# On the Radar / Calendar: append the corroboration block after the September-5 rejection paragraph.
anchor = ('&rdquo;. <b>September 5, 2026 is a Saturday</b> &mdash; today is Sunday August 30, which puts Friday on '
          '<b>September 4')
if anchor not in ws:
    # fall back to a looser anchor
    m = re.search(r'which puts Friday on\s*<b>September 4', ws)
    if not m:
        FAIL.append('WS radar anchor: not found')
    else:
        anchor = ws[m.start():m.end()]

RADAR_ADD = (
 '<p><b>Added at 2:12 PM &mdash; the weekday rejection stopped being an inference and became a citation.</b> '
 'For three consecutive runs this page has refused a week-ahead preview that places nonfarm payrolls on '
 '&ldquo;September 5&rdquo;, on the ground that September 5, 2026 is a Saturday. This run the '
 '<b>Federal Reserve Bank of New York&rsquo;s own economic-indicators calendar for September 2026</b> was fetched, '
 'and it puts the <b>Employment Situation on Friday, September 4 at 8:30 AM</b> &mdash; the date this page has '
 'printed throughout. <b>The rejection is now sourced to a release calendar rather than to a day-of-week '
 'calculation</b>, which is the difference between being right and being able to show it. The same calendar '
 'fills in the rest of the week: <b>ISM Manufacturing and JOLTS, Tuesday September 1 at 10:00 AM</b>; the '
 '<b>ADP National Employment Report, Wednesday September 2 at 8:15 AM</b>; and <b>initial jobless claims, the '
 'trade balance and ISM Services on Thursday September 3</b>, claims and trade at 8:30 AM and ISM at 10:00 AM. '
 '&#9888; Note that <b>Monday August 31 carries no first-tier release</b> on that calendar, so the week&rsquo;s '
 'data does not begin until Tuesday.</p>'
 '<p><b>Also added at 2:12 PM &mdash; the first seasonal figure this page has printed, and it is not a forecast.</b> '
 'A seasonality study dated <b>August 28, 2026</b> reports that over the past <b>50 years</b> the S&amp;P 500 has '
 'lost <b>0.7% on average during September</b>, with the frequency of gains for the month at <b>46%</b> &mdash; '
 'making it the weakest month of the year for equity returns. <b>This is a historical average and nothing more</b>: '
 'it says what fifty Septembers did, not what this one will do, and it is printed here because the week ahead '
 'crosses into that month rather than because it predicts anything. It is also worth setting against what the '
 'market actually just did &mdash; all three indices finished the week green, the Dow for the first time in three '
 'weeks.</p>')

ws = rep(ws, anchor, anchor, 'WS radar anchor present', 1) if anchor in ws else ws
# insert the block just before the closing of the On the Radar section: after the paragraph containing anchor
idx = ws.find(anchor)
if idx == -1:
    FAIL.append('WS radar insert: anchor missing')
else:
    endp = ws.find('</p>', idx)
    if endp == -1:
        FAIL.append('WS radar insert: no closing </p>')
    else:
        ws = ws[:endp+4] + RADAR_ADD + ws[endp+4:]

save('wallstreet-briefing.html', ws)

# ───────────────────────────── CYBER ─────────────────────────────
cy = load('cyber-briefing.html')

cy = rep(cy, 'a <b>tenth check of the KEV catalogue at 1:08 PM</b> again found no CISA alert dated later than August 27, so no countdown moved',
             'an <b>eleventh check of the KEV catalogue at 2:12 PM</b> again found no CISA alert dated later than August 27, so no countdown moved',
             'CY tldr check ordinal')

# tldr tail: swap the "three refused" sentence ending for this run's additions
old_ct = ('Nothing new was published from a roundup.')
new_ct = ('Nothing new was published from a roundup, and <b>Nevada returned a fourth consecutive time and was '
          'refused a fourth time</b>. &#9888; New this run: <b>the 421-CVE figure this page prints for August Patch '
          'Tuesday is not the only count in circulation</b> &mdash; one vendor analysis puts it at <b>398</b> and a '
          'third tracker at <b>751</b>, so the spread is now printed rather than the number alone.')
cy = rep(cy, old_ct, new_ct, 'CY tldr tail')

# KEV narrative: append the eleventh check
kev_anchor = '<b>A tenth check at 1:08 PM returned the same top of the catalogue'
i = cy.find(kev_anchor)
if i == -1:
    FAIL.append('CY kev anchor missing')
else:
    endp = cy.find('</p>', i)
    endd = cy.find('</div>', i)
    cut = min(x for x in (endp, endd) if x != -1)
    KEV_ADD = (
     '<br><br><b>An eleventh check at 2:12 PM confirmed the top of the catalogue from the outside, by name.</b> '
     'A fresh sweep returned CISA&rsquo;s <b>August 27</b> alert with all three of its CVEs stated explicitly &mdash; '
     '<b>CVE-2023-49105</b> (ownCloud improper authentication), <b>CVE-2026-53362</b> (Linux kernel) and '
     '<b>CVE-2026-66384</b> (JFrog Artifactory path traversal) &mdash; which is <b>exactly the three this board '
     'carries</b>, and <b>nothing dated later than August 27</b> came back a fifth consecutive check. '
     'Until now the August 27 rows rested on a single catalogue read; they now have an independent one that names '
     'the same three identifiers. <b>All four countdowns stand unmoved</b>, and the two rows due today are still '
     'due today. &#9888; <b>One new deadline surfaced for a CVE this board already carried, and it gets no row.</b> '
     'Reporting on the August Patch Tuesday states that CISA added <b>CVE-2026-68820</b> &mdash; the exploited '
     'WinSock zero-day &mdash; to the catalogue with a due date of <b>August 25</b>, which is <b>five days past</b>. '
     'That date came from a news write-up rather than from a CISA alert page fetched this run, so it is recorded '
     'in this narrative and <b>not given a countdown row</b>; a deadline this board cannot source to CISA is not a '
     'deadline it will display. It does, however, mean the WinSock flaw&rsquo;s federal deadline expired before '
     'this board ever showed one for it.')
    cy = cy[:cut] + KEV_ADD + cy[cut:]

# Patch Tuesday count spread — attach to the first "421" occurrence context in the stat strip narrative
pt_pat = re.search(r'421[^<]{0,40}CVE', cy)
STAT_ADD = (
 '<p><b>Added at 2:12 PM &mdash; the 421 figure has competition, and the page now prints the spread instead of the '
 'number alone.</b> This page has carried <b>421 CVEs</b> as the size of August&rsquo;s Patch Tuesday, and four '
 'independent write-ups fetched this run repeat it. But a fifth, a major vulnerability-management vendor&rsquo;s own '
 'analysis, titles its post <b>398 CVEs</b>, and a sixth tracker ranks <b>751</b>. <b>Nothing fetched reconciles the '
 'three</b>, and the plausible explanation &mdash; that they count different things, Microsoft-issued versus '
 'republished third-party CVEs versus everything in the update &mdash; is an explanation this page can offer but '
 'cannot source. <b>421 stays, because it is the majority return and is described as the Security Update Guide '
 'total, but it is stated as one count among three rather than as the number.</b> What every version agrees on is '
 'the part that matters operationally: <b>exactly one flaw in the release was being exploited</b>, '
 '<b>CVE-2026-68820</b>, the use-after-free in <b>afd.sys</b> used to reach SYSTEM &mdash; and the vendor putting '
 'the count at 398 adds that it was <b>one of three zero-days</b>, the other two disclosed but not exploited. '
 '<b>A disputed total does not make a disputed zero-day.</b></p>')

# Refused-this-run panel: bump Nevada to a fourth refusal
cy2 = cy
if 'Nevada' in cy2:
    cy2 = re.sub(r'(Nevada[^<]{0,120}?)third consecutive refusal', r'\1fourth consecutive refusal', cy2, count=1)
    cy = cy2

# insert the Patch Tuesday paragraph after the Top Story section's first closing </p> following "421"
if pt_pat:
    endp = cy.find('</p>', pt_pat.end())
    if endp == -1:
        FAIL.append('CY patch tuesday insert: no </p>')
    else:
        cy = cy[:endp+4] + STAT_ADD + cy[endp+4:]
else:
    FAIL.append('CY patch tuesday anchor: 421 not found near CVE')

# Berlin volume variant
if '5.79' in cy:
    b = cy.find('5.79')
    endp = cy.find('</p>', b)
    if endp != -1:
        cy = cy[:endp] + (' <b>Variant recorded at 2:12 PM, figure not swapped:</b> a listing fetched this run '
                          'renders the volume as <b>5.8TB</b> where this page carries <b>5.79 TB</b>. That is a '
                          'rounding of the same figure and not a second claim, so the precise form this page '
                          'sourced first is kept and the rounded one is printed beside it.') + cy[endp:]

save('cyber-briefing.html', cy)

# ───────────────────────────── MMA ─────────────────────────────
mm = load('mma-briefing.html')

mm = rep(mm, 'clean against ESPN for a third consecutive run</b>, all six men&rsquo;s divisions matching on champion, method and date, for a <b>sixtieth unchanged edition</b>.',
             'clean against ESPN for a fourth consecutive run</b>, all six men&rsquo;s divisions matching on champion, '
             'method and date, for a <b>sixty-first unchanged edition</b>. And the Paris main-event price moved from '
             'a three-way spread toward one line: <b>the &minus;500 / +375 pair returned a third time and independently</b>, '
             'while &minus;400 and &minus;428 did not return at all &mdash; still <b>not adopted</b>, but no longer '
             'three equal readings.',
             'MMA tldr')

mm = rep(mm, 'The board is unchanged for a <b>sixtieth consecutive edition</b> &mdash; <b>a third consecutive clean run against ESPN&rsquo;s own page</b>',
             'The board is unchanged for a <b>sixty-first consecutive edition</b> &mdash; <b>a fourth consecutive clean run against ESPN&rsquo;s own page</b>',
             'MMA board ordinal')

# Paris odds — append to the odds paragraph
odds_anchor = 'the <b>UFC&rsquo;s own listing at Parnasse &minus;500 / Hooker +375</b>'
i = mm.find(odds_anchor)
if i == -1:
    FAIL.append('MMA odds anchor missing')
else:
    endp = mm.find('</p>', i)
    if endp == -1:
        FAIL.append('MMA odds: no </p>')
    else:
        ODDS_ADD = (
         ' <b>Updated at 2:12 PM &mdash; the spread narrowed, not because a book moved but because two of the three '
         'lines stopped coming back.</b> A fresh sweep of the card returned <b>Hooker +375 / Parnasse &minus;500</b> '
         'again, from a source other than the UFC listing that first gave it &mdash; a <b>third independent return of '
         'that pair</b> &mdash; while <b>neither &minus;400 nor &minus;428 was returned by anything fetched this run</b>. '
         '<b>No line is adopted even so</b>, because a price that keeps being republished is not thereby the price, '
         'and none of the three sources dates its quote. But it is worth stating plainly which of the three has '
         'independent agreement and which two do not. &#9888; <b>And the undercard has prices on this page for the '
         'first time:</b> <b>Far&egrave;s Ziam &minus;150 / Axel Sola +125</b> and <b>Michael Page &minus;200 / '
         'Nursulton Ruziboev +165</b>, both from the same listing, both single quotes with no second book to check '
         'them against &mdash; printed as one book&rsquo;s line, not as a consensus.')
        mm = mm[:endp] + ODDS_ADD + mm[endp:]

# Shanghai aftermath
sh_anchor = 'nearly 5-1 underdog&rdquo; at DraftKings'
i = mm.find(sh_anchor)
if i == -1:
    FAIL.append('MMA shanghai anchor missing')
else:
    endp = mm.find('</p>', i)
    if endp == -1:
        endp = mm.find('</div>', i)
    if endp == -1:
        FAIL.append('MMA shanghai: no close tag')
    else:
        SH_ADD = (
         ' <b>Added at 2:12 PM &mdash; a second characterisation of the same price, and the aftermath.</b> A report '
         'fetched this run calls Nurmagomedov <b>&ldquo;a 6-to-1 favourite&rdquo;</b>. That sits at the far end of, '
         'but inside, the range this page recorded &mdash; the widest single price it saw was <b>&minus;625</b>, '
         'which is six-and-a-quarter to one &mdash; so it is a <b>third characterisation</b> alongside the '
         '&ldquo;nearly 5-1&rdquo; DraftKings line, and like the others it is <b>printed rather than adopted</b>. '
         'The same reporting adds three things this page had not carried: the knockout was '
         '<b>Nurmagomedov&rsquo;s first finish loss in his career</b>, it ended a <b>two-fight win streak</b>, and '
         'the consequence is positional &mdash; <b>Song now takes the place in the bantamweight contender line</b> '
         'that Nurmagomedov had been working toward. Nurmagomedov posted a statement shortly after the card reading '
         'in part <b>&ldquo;Everything is fine with me&rdquo;</b>. &#9888; <b>No next bout for either man has been '
         'announced by anything fetched this run, and none is printed.</b>')
        mm = mm[:endp] + SH_ADD + mm[endp:]

# UFC 331 co-main upgrade
mm = rep(mm, '(No. 10) over five rounds, with title implications.',
             '(No. 10) over five rounds; reporting fetched this run states a <b>title shot against lightweight '
             'champion Justin Gaethje is likely on the line for the winner</b>, which is firmer than the '
             '&ldquo;title implications&rdquo; this page carried, though the promotion has not said so itself.',
             'MMA 331 comain')

save('mma-briefing.html', mm)

if FAIL:
    print('EDIT FAILURES:')
    for f in FAIL:
        print(' -', f)
    sys.exit(1)
print('edits_1412: OK')
