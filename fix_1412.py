#!/usr/bin/env python3
"""Fixes for real page defects found by validate_1412:
   (a) masthead pill fallback text still carried the previous run's clock;
   (b) the Refused panel said Nevada was refused a THIRD time while the tldr,
       correctly, said a FOURTH — an internal contradiction introduced this run."""
import re, sys, io, os, datetime, zoneinfo

D = sys.argv[1]
ET = zoneinfo.ZoneInfo('America/New_York')
now = datetime.datetime.now(ET)
stamp = now.strftime('%-I:%M %p')
hour = now.hour
edition = 'Morning Edition' if hour < 11 else ('Midday Edition' if hour < 15 else 'Afternoon Edition')
datestr = now.strftime('%A, %B %-d, %Y')
FAIL = []

# (a) masthead pill fallbacks on all four pages
for fn in ('index.html', 'cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html'):
    p = os.path.join(D, fn)
    h = io.open(p, encoding='utf-8').read()
    h2 = re.sub(r'(<span id="updated">)[^<]*(</span>)', r'\g<1>' + stamp + ' ET' + r'\g<2>', h)
    h2 = re.sub(r'(id="edition"[^>]*>)[^<]*(</span>)', r'\g<1>' + edition + r'\g<2>', h2)
    h2 = re.sub(r'(id="datestamp"[^>]*>)[^<]*(</span>)', r'\g<1>' + datestr + r'\g<2>', h2)
    # assert the RESULT, not that something changed (so the fix is idempotent)
    if f'<span id="updated">{stamp} ET</span>' not in h2:
        FAIL.append(f'{fn}: updated pill not stamped {stamp}')
    if f'>{edition}<' not in h2:
        FAIL.append(f'{fn}: edition pill not set to {edition}')
    io.open(p, 'w', encoding='utf-8').write(h2)

# (b) Refused panel — Nevada is now a fourth refusal, and the panel was re-checked this run
p = os.path.join(D, 'cyber-briefing.html')
cy = io.open(p, encoding='utf-8').read()

subs = [
 ('Three items were fetched from &ldquo;biggest breaches of 2026&rdquo; roundups at 1:08 PM and none of them reached this page.',
  'Three items were fetched from &ldquo;biggest breaches of 2026&rdquo; roundups at 1:08 PM and none of them reached this page, '
  'and a re-check at ' + stamp + ' returned the first of them <b>again</b>.'),
 ('Nevada &mdash; refused for a third consecutive run.',
  'Nevada &mdash; refused for a fourth consecutive run.'),
 ('No source fetched on any of the three runs dates that attack to 2026',
  'No source fetched on any of the four runs dates that attack to 2026'),
 ('Nevada for a third consecutive run,',
  'Nevada for a fourth consecutive run,'),
]
for old, new in subs:
    if cy.count(old) < 1:
        # idempotent: already applied on an earlier pass is not a failure
        key = new.split('.')[0][:50]
        if key not in cy:
            FAIL.append(f'refused panel: neither old nor new form present: {old[:60]!r}')
        continue
    cy = cy.replace(old, new)

# the tldr already says "fourth consecutive time"; collapse the now-redundant duplicate clause
cy = cy.replace(', and <b>Nevada returned a fourth consecutive time and was '
                'refused a fourth time</b>.',
                ' &mdash; Nevada now for a <b>fourth</b> consecutive run.')

io.open(p, 'w', encoding='utf-8').write(cy)

print(f'fix_1412: stamped {stamp} ET | {edition} | {datestr}')
if FAIL:
    print('FIX NOTES:')
    for f in FAIL: print(' -', f)
    sys.exit(1)
