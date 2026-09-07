#!/usr/bin/env python3
"""Re-apply the two lost cyber edits, and clear EVERY stale 'this run' provenance
claim carried forward from the 08:19 edition. 2026-09-07 ~08:55 ET.

Sources actually fetched first-hand THIS run: cert.pl (MikroTik advisory),
tradingeconomics.com/commodity/brent-crude-oil, and an ATTEMPT at the CISA
2 September alert page which returned empty. Nothing else.
"""
import io, sys

n = 0
def sub(path, old, new, label, expect=1):
    global n
    h = io.open(path, encoding='utf-8').read()
    if h.count(old) != expect:
        sys.exit('MISS(%d != %d): %s' % (h.count(old), expect, label))
    io.open(path, 'w', encoding='utf-8').write(h.replace(old, new, expect))
    n += 1
    print('  ok:', label)

C = 'cyber-briefing.html'
W = 'wallstreet-briefing.html'
M = 'mma-briefing.html'

# ============================ 1. LOST EDIT: fixed-version list corrected vs primary
sub(C,
 ('The 7.23.5 divergence is also resolved, and not in favour of either earlier '
  'reading:</b> CERT Polska&rsquo;s own list, as relayed by Cybernews, names three '
  'fixed builds (6.49.21, 7.23.4, 7.24.2) and omits both 7.25beta3 and 7.23.5, while '
  'Security Affairs on 6 September gives the combined five &mdash; 7.25beta3, 7.24.2, '
  '7.23.4, <b>7.23.5 (released 4 September)</b> and 6.49.21 &mdash; and states the '
  'release date explicitly. A shorter list published before a build shipped is not '
  'evidence against that build, so the fuller list is the one to patch to. '),
 ('The fixed-version list is corrected this edition against the primary source, and the '
  'previous edition had it wrong.</b> That edition reported &mdash; on Cybernews&rsquo; relay '
  '&mdash; that CERT Polska&rsquo;s own list named <i>three</i> builds and omitted 7.25beta3. '
  'CERT Polska&rsquo;s advisory was fetched directly this morning and it names <b>four</b>: '
  '&ldquo;MikroTik has released fixes in versions 7.25beta3, 7.24.2, 7.23.4, and 6.49.21.&rdquo; '
  'The missing beta was an artefact of the relay, not of the advisory. That leaves exactly one '
  'build in dispute &mdash; <b>7.23.5</b>, which Security Affairs on 6 September lists as fixed '
  'and dates to <b>4 September</b>, and which cert.pl does not mention. A list published before a '
  'build shipped is not evidence against that build, so the five-build set remains what this page '
  'tells readers to patch to; the four carrying CERT Polska&rsquo;s vendor-coordinated imprimatur '
  'are now named as such. '),
 'LOST EDIT 1: fixed-version list corrected vs primary')

# ============================ 2. LOST EDIT: provenance upgraded to first-hand
sub(C,
 ('CERT Polska’s advisory was fetched directly from cert.pl in an <i>earlier</i> '
  'edition, <b>not this one</b> — and this page says so rather than repeating a fetch '
  'claim it cannot support this morning. Corroboration today comes by a different and '
  'independent route: <b>Cybernews</b> and <b>Security Affairs</b> were each fetched '
  'directly this run, both quote that same CERT Polska advisory, and the IoCs, the two '
  'source IPs and all <b>six</b> RouterOS CVEs above match what this page already carried. '),
 ('<b>Provenance, corrected upward this edition:</b> CERT Polska’s advisory '
  '<b>was fetched directly from cert.pl this morning</b>, which is what made the correction '
  'above possible. The previous edition could reach it only through Cybernews and Security '
  'Affairs — each fetched directly in <i>that</i> edition, not this one — and said so. '
  'This edition reads the primary. Everything in this block — the MikroTrick name, the two '
  'chained CVEs and their 9.2 scores, the 8.8 on the bandwidth-test bug, the log-line IoCs, the '
  '<b>ops</b> account, both source IPs and the 2 September start date — now traces to CERT '
  'Polska’s own text rather than to a relay of it, and every one of them matches what this '
  'page already carried. '),
 'LOST EDIT 2: provenance upgraded to first-hand')

# ============================ 3. Cybernews timestamp claim -> previous edition
sub(C,
 'which was fetched directly this run and carries <span',
 'which was fetched directly in the previous edition &mdash; not this one &mdash; and carries <span',
 'cybernews fetch claim -> previous edition')

# ============================ 4. CISA: it WAS re-attempted this run, and returned empty
sub(C,
 ('CISA&rsquo;s own alert page has returned empty on every previous run that attempted it; '
  'it was not re-attempted this morning, and no fetch of it is claimed here.'),
 ('CISA&rsquo;s own alert page <b>was re-attempted this morning and returned empty again</b> '
  '&mdash; the fetch completed with no body, as it has on every previous attempt. That is a '
  'genuine attempt with a null result, not a skipped one, and it is why these dates remain '
  'attributed to reporting rather than to CISA directly.'),
 'CISA alert page: attempted this run, empty')

sub(C,
 ('CISA&rsquo;s alert page has returned empty on every fetch this desk has attempted, and it '
  'was not re-attempted this run, so these dates are attributed to reporting.'),
 ('CISA&rsquo;s alert page has returned empty on every fetch this desk has attempted, '
  '<b>including one made this run</b>, so these dates are attributed to reporting.'),
 'CISA alert page: second mention')

# ============================ 5. MMA: stale 'this run' -> previous edition
sub(M,
 'This run that page could not be retrieved at all',
 'In the previous edition that page could not be retrieved at all',
 'MMA: ufc.com refusal -> previous edition')

sub(M,
 ('What did corroborate the bonuses independently this run was Wikipedia&rsquo;s event page, '
  'fetched directly:'),
 ('What corroborated the bonuses independently was Wikipedia&rsquo;s event page, fetched directly '
  'in the previous edition &mdash; not this one:'),
 'MMA: wikipedia fetch -> previous edition')

print('fix_0850: %d edits' % n)
