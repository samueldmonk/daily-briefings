#!/usr/bin/env python3
"""Tag hygiene, narrowed: demote stale New tags, date the bare ones, and strip
bare EDITION stamps out of prose. Only times in this site's own run cadence are
touched -- a source's as-of time (Bloomberg 10:22 AM, an 8:30 AM data release)
is a different measurement and is left alone."""
import io, re

TAG_FIX = {
'cyber-briefing.html': [
  ('<span class="tag new">New &middot; 12:51 PM</span>', '<span class="tag">Carried &middot; Aug 31, 12:51 PM</span>'),
  ('<span class="tag crit">New &middot; 5:15 PM</span>', '<span class="tag">Carried &middot; earlier edition</span>'),
  ('New &middot; 5:15 PM', 'Carried &middot; earlier edition'),
  ('Refused &middot; 3:10 PM', 'Refused &middot; Aug 30, 3:10 PM'),
  ('Corrected &middot; 6:45 PM', 'Corrected &middot; Aug 30, 6:45 PM'),
  ('Rewritten &middot; researched 8:10 AM', 'Rewritten &middot; researched Aug 31, 8:10 AM'),
],
'wallstreet-briefing.html': [
  ('<span class="tag new">New &middot; 12:51 PM</span>', '<span class="tag">Carried &middot; Aug 31, 12:51 PM</span>'),
  ('New &middot; 12:51 PM', 'Carried &middot; Aug 31, 12:51 PM'),
  ('Refused &middot; 3:36 PM', 'Refused &middot; Aug 30, 3:36 PM'),
  ('Rejected &middot; 3:10 PM', 'Rejected &middot; Aug 30, 3:10 PM'),
  ('Corrected &middot; 6:45 PM', 'Corrected &middot; Aug 30, 6:45 PM'),
],
'mma-briefing.html': [
  ('<span class="tag new">New &middot; 12:51 PM</span>', '<span class="tag">Carried &middot; Aug 31, 12:51 PM</span>'),
  ('New &middot; 12:51 PM', 'Carried &middot; Aug 31, 12:51 PM'),
  ('New &middot; 4:06 PM', 'Carried &middot; Aug 30, 4:06 PM'),
  ('Cross-check &middot; 6:45 PM', 'Cross-check &middot; Aug 30, 6:45 PM'),
],
}

# Times this site has published editions at, excluding today's runs.
PRIOR_RUNS = {'8:19','8:35','8:38','8:46','9:15','9:42','9:40','10:20','10:50','11:05',
              '11:35','12:05','12:35','12:58','1:05','1:08','1:35','2:11','2:39','3:10',
              '3:36','4:06','4:36','5:10','5:15','5:38','5:48','6:10','6:20','6:45',
              '8:10','2:13','1:48','4:49','12:45'}
DAYS = ('Saturday','Sunday','Monday','Friday','Thursday','Wednesday','Tuesday','ET','Eastern')

STAMP = re.compile(r'(?<![\d:])(\d{1,2}:\d{2})(\s*(?:AM|PM))(?![\s ]*ET)', re.I)

def scrub(seg):
    spans = []
    for m in STAMP.finditer(seg):
        if m.group(1) not in PRIOR_RUNS:
            continue                                   # not one of our editions
        before = seg[max(0, m.start() - 16):m.start()]
        after = seg[m.end():m.end() + 16]
        if re.search(r'Aug(?:ust)? \d{1,2},?\s*$', before):
            continue                                   # already dated
        if any(after.lstrip().startswith(d) for d in DAYS):
            continue                                   # already carries a day
        spans.append((m.start(), m.end()))
    if not spans:
        return seg
    res, last = [], 0
    for s, e in spans:
        res.append(seg[last:s]); res.append('\x00'); last = e
    res.append(seg[last:])
    seg = ''.join(res)
    # fold the placeholder into English. Order matters: longest context first.
    R = [(r'in the \x00(?: AM| PM)? edition', 'in an earlier edition'),
         (r'the \x00(?: AM| PM)? and \d{1,2}:\d{2} editions', 'earlier editions'),
         (r'the \x00(?: AM| PM)? edition', 'an earlier edition'),
         (r'\bsince the \x00', 'since an earlier edition'),
         (r'\bSince the \x00', 'Since an earlier edition'),
         (r'\bsince \x00', 'since an earlier edition'),
         (r'\bSince \x00', 'Since an earlier edition'),
         (r'\bat \x00', 'in an earlier edition'),
         (r'\bAt \x00', 'In an earlier edition'),
         (r'\bfrom \x00', 'from an earlier edition'),
         (r'\bby \x00', 'by an earlier edition'),
         (r'\bbefore \x00', 'before an earlier edition'),
         (r'\bretired \x00', 'retired in an earlier edition'),
         (r'\bsourced \x00', 'sourced in an earlier edition'),
         (r'\bupdated \x00', 'updated in an earlier edition'),
         (r'\bNew \x00', 'Added in an earlier edition'),
         (r'\bAdded \x00', 'Added in an earlier edition'),
         (r'\bFilled in \x00', 'Filled in an earlier edition'),
         (r'\bNamed \x00', 'Named in an earlier edition'),
         (r'\bDated \x00', 'Dated in an earlier edition'),
         (r'\bCorroborated \x00', 'Corroborated in an earlier edition'),
         (r'\bCarried \x00', 'Carried from an earlier edition')]
    for pat, rep in R:
        seg = re.sub(pat, rep, seg)
    seg = seg.replace('\x00', 'an earlier edition')
    # tidy artefacts
    seg = seg.replace('an earlier edition edition', 'an earlier edition')
    seg = seg.replace('in the an earlier edition', 'in an earlier edition')
    seg = seg.replace('the an earlier edition', 'an earlier edition')
    return seg

for p, fixes in TAG_FIX.items():
    h = io.open(p, encoding='utf-8').read()
    for a, b in fixes:
        h = h.replace(a, b)
    fi = h.find('<footer')
    body, foot = (h[:fi], h[fi:]) if fi > 0 else (h, '')
    parts = re.split(r'(<span class="tag[^"]*">.*?</span>|<a\b[^>]*>.*?</a>|<script.*?</script>)',
                     body, flags=re.S)
    for i in range(0, len(parts), 2):
        parts[i] = scrub(parts[i])
    io.open(p, 'w', encoding='utf-8').write(''.join(parts) + foot)
    print('tag hygiene applied', p)
