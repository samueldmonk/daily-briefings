#!/usr/bin/env python3
"""Restamp all four pages from the wall clock, enforce prose <= publish time,
and mirror each briefing's tldr onto the matching index card."""
import re, sys, io, os, datetime, zoneinfo

D = sys.argv[1]
ET = zoneinfo.ZoneInfo('America/New_York')
now = datetime.datetime.now(ET)
stamp = now.strftime('%-I:%M %p')
hour = now.hour
edition = 'Morning Edition' if hour < 11 else ('Midday Edition' if hour < 15 else 'Afternoon Edition')
datestr = now.strftime('%A, %B %-d, %Y')

DRAFT = '3:36 PM'   # observation stamp used while drafting this edition

def mins(s):
    m = re.match(r'(\d+):(\d\d) (AM|PM)', s)
    h, mi, ap = int(m.group(1)), int(m.group(2)), m.group(3)
    if ap == 'PM' and h != 12: h += 12
    if ap == 'AM' and h == 12: h = 0
    return h * 60 + mi

prose = DRAFT if mins(DRAFT) <= mins(stamp) else stamp
if prose != DRAFT:
    print(f'CLOCK CORRECTION: prose {DRAFT} -> {prose} (wall clock {stamp})')

FILES = ['index.html', 'cyber-briefing.html', 'wallstreet-briefing.html', 'mma-briefing.html']
for fn in FILES:
    p = os.path.join(D, fn)
    h = io.open(p, encoding='utf-8').read()
    if prose != DRAFT:
        h = h.replace(DRAFT, prose)
    h = re.sub(r'Data as of [0-9]{1,2}:[0-9]{2} (?:AM|PM) ET', f'Data as of {stamp} ET', h)
    h = re.sub(r'(id="updated">)[^<]*(</span>)', lambda m: m.group(1) + stamp + ' ET' + m.group(2), h)
    h = re.sub(r'(id="edition">)[^<]*(</span>)', lambda m: m.group(1) + edition + m.group(2), h)
    h = re.sub(r'(id="datestamp">)[^<]*(</span>)', lambda m: m.group(1) + datestr + m.group(2), h)
    io.open(p, 'w', encoding='utf-8').write(h)

def tldr_of(fn):
    h = io.open(os.path.join(D, fn), encoding='utf-8').read()
    m = re.search(r'<div class="tldr"><b>[^<]+</b>\s*<span>(.*?)</span></div>', h, re.S)
    return m.group(1) if m else None

idx = io.open(os.path.join(D, 'index.html'), encoding='utf-8').read()
pairs = [('cyber-briefing.html', 'c-cy'), ('wallstreet-briefing.html', 'c-ws'),
         ('mma-briefing.html', 'c-mm')]
fails = []
for fn, cls in pairs:
    t = tldr_of(fn)
    if not t:
        fails.append(f'no tldr in {fn}'); continue
    i = idx.find(f'<div class="bigcard {cls}">')
    if i == -1:
        fails.append(f'index card div missing for {cls}'); continue
    ps = idx.find('<p>', i); pe = idx.find('</p>', ps)
    if ps == -1 or pe == -1:
        fails.append(f'index card <p> missing for {cls}'); continue
    idx = idx[:ps + 3] + t + idx[pe:]
io.open(os.path.join(D, 'index.html'), 'w', encoding='utf-8').write(idx)

print(f'restamp: {stamp} ET | {edition} | {datestr} | prose {prose}')
if fails:
    print('MIRROR NOTES:')
    for f in fails: print(' -', f)
