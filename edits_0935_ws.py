#!/usr/bin/env python3
import io, sys
F = 'wallstreet-briefing.html'

def edit(tell, old, new, label):
    h = io.open(F, encoding='utf-8').read()
    if tell in h:
        print('skip (already applied):', label); return
    if old not in h:
        print('MISS ANCHOR:', label); sys.exit(1)
    h = h.replace(old, new, 1)
    io.open(F, 'w', encoding='utf-8').write(h)
    h2 = io.open(F, encoding='utf-8').read()
    assert tell in h2 and h2.count(tell) == 1, 'edit failed/duplicated: ' + label
    print('ok:', label)

# ================= PROVENANCE GUARD — decay stale "this run" fetch claims =================
edit('while EnergyNow, fetched in the 9:17 edition,',
     'while EnergyNow, fetched this run,',
     'while EnergyNow, fetched in the 9:17 edition,',
     'P1 EnergyNow superlative claim')

edit('per EnergyNow, fetched directly in the 9:17 edition, while members',
     'per EnergyNow, fetched directly this run, while members',
     'per EnergyNow, fetched directly in the 9:17 edition, while members',
     'P2 OPEC+ line')

edit('a date sourced in the 9:17 edition from EnergyNow quoting Reuters',
     'a date newly sourced this run from EnergyNow quoting Reuters',
     'a date sourced in the 9:17 edition from EnergyNow quoting Reuters',
     'P3 Brent 24 July date')

edit('<b>That refusal was lifted in the 9:17 edition.</b> EnergyNow&rsquo;s 7 September report, fetched directly then,',
     '<b>That refusal is lifted this run.</b> EnergyNow&rsquo;s 7 September report, fetched directly,',
     '<b>That refusal was lifted in the 9:17 edition.</b> EnergyNow&rsquo;s 7 September report, fetched directly then,',
     'P4 WTI settle refusal lift')

edit('The competing figures got harder to dismiss in the 9:17 edition',
     'The competing figures got harder to dismiss this run',
     'The competing figures got harder to dismiss in the 9:17 edition',
     'P5 CPI consensus conflict')

# ================= counters that decay =================
edit('the twenty-second consecutive run without one',
     'the twenty-first consecutive run without one',
     'the twenty-second consecutive run without one',
     'K1 VIX refusal counter advanced')

edit('re-verified against a fresh search this run &mdash; the <b>ninth consecutive run</b>',
     'last re-verified against a fresh search in the 8:19 edition &mdash; the <b>eighth consecutive run</b>',
     're-verified against a fresh search this run &mdash; the <b>ninth consecutive run</b>',
     'K2 Sept 4 closes re-verified this run, counter advanced to ninth')

# ================= W4 third reading on crude =================
edit('A third reading arrived this run and it lands between the two',
     '<span class="mut">Th',
     '<span class="mut"><b>A third reading arrived this run and it lands between the two.</b> A search return this '
     'morning puts <b>WTI at approximately $91.98, up about $0.50 or 0.5%</b> against Friday&rsquo;s settlement &mdash; '
     'roughly 36 cents below Trading Economics&rsquo; 8:47 read of 92.34 and a smaller daily move than its +0.94%. '
     'Both are live quotes taken at different minutes of a holiday-thinned session rather than competing settlements, '
     'so the row header stays at <b>~$92</b> and neither intraday level is asserted as the figure. The same return '
     'independently describes <b>$91.48 as Friday&rsquo;s official settlement</b> &mdash; a third path to that number, '
     'after Trading Economics and EnergyNow.</span> <span class="mut">Th',
     'W4 third WTI reading printed as a divergence, not a correction')

edit('Brent&rsquo;s ~$97.27 gained a third independent path this run',
     'The two quotes are a dollar apart and that gap is <b>explained rather than reconciled</b>',
     '<b>Brent&rsquo;s ~$97.27 gained a third independent path this run:</b> a search return this morning gives the '
     'same <b>~$97.27</b>, the same <b>~99 cents / 1.0%</b> move, and the same <b>$96.28 Friday settlement</b> to '
     'measure it from &mdash; arrived at without EnergyNow, which is what makes it corroboration rather than an echo. '
     'The two quotes are a dollar apart and that gap is <b>explained rather than reconciled</b>',
     'W4b Brent corroborated by a third path')

# ================= W5 Warsh / political pressure =================
edit('full-court press to halt the hike in its tracks',
     '<li><b>Over the weekend &mdash; OPEC+ left October output policy unchanged</b>',
     '<li><b>The political pressure on the Fed is now overt, and it is aimed at one man.</b> CNBC reported on '
     '<b>5 September</b>, under the headline &ldquo;Trump turns up the heat on Warsh as Fed rate hike looms,&rdquo; '
     'that ten days ahead of the <b>15&ndash;16 September FOMC meeting</b> the Trump administration &ldquo;looks to be '
     'in a full-court press to halt the hike in its tracks.&rdquo; The meeting is the one at which a rise &mdash; not '
     'a cut &mdash; is the live question, after August payrolls came in at 162,000 against a 53,000 consensus. '
     '<span class="mut">No probability is asserted: this desk has now seen 58%, ~60%, 63% and a near-even split '
     'attributed to different sources for the same meeting, and the spread is the honest reading. What is asserted is '
     'the direction &mdash; below even before payrolls, above even after &mdash; and the sequence: '
     '<b>August CPI on Friday 11 September</b>, then the decision on <b>16 September</b>.</span></li>\n'
     '<li><b>Over the weekend &mdash; OPEC+ left October output policy unchanged</b>',
     'W5 Trump/Warsh pressure item added to On the Radar')

print('--- wall street edits done ---')
