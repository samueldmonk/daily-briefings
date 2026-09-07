#!/usr/bin/env python3
"""Cyber page edits, 2026-09-07 ~08:40 ET (Morning Edition, SECOND run of the day).

Driver: cert.pl WAS fetched first-hand this run. That upgrades the provenance of the
whole MikroTrick block from relayed to primary, and it CORRECTS one thing the previous
edition asserted about CERT Polska's own fixed-version list.
"""
import re, sys, io

P = 'cyber-briefing.html'
h = io.open(P, encoding='utf-8').read()
orig = h
n = 0

def sub(old, new, label):
    global h, n
    if old not in h:
        sys.exit('MISS: ' + label)
    h = h.replace(old, new, 1)
    n += 1
    print('  ok:', label)

# ---------------------------------------------------------------- 1. fixed-version list
old1 = ('The 7.23.5 divergence is also resolved, and not in favour of either earlier '
        'reading:</b> CERT Polska&rsquo;s own list, as relayed by Cybernews, names three '
        'fixed builds (6.49.21, 7.23.4, 7.24.2) and omits both 7.25beta3 and 7.23.5, while '
        'Security Affairs on 6 September gives the combined five &mdash; 7.25beta3, 7.24.2, '
        '7.23.4, <b>7.23.5 (released 4 September)</b> and 6.49.21 &mdash; and states the '
        'release date explicitly. A shorter list published before a build shipped is not '
        'evidence against that build, so the fuller list is the one to patch to. ')
new1 = ('The fixed-version list is corrected this edition, against the primary source, and '
        'the previous edition had it wrong.</b> That edition reported &mdash; on Cybernews&rsquo; '
        'relay &mdash; that CERT Polska&rsquo;s own list named <i>three</i> builds and omitted '
        '7.25beta3. CERT Polska&rsquo;s advisory was fetched directly this morning and it names '
        '<b>four</b>: &ldquo;MikroTik has released fixes in versions 7.25beta3, 7.24.2, 7.23.4, '
        'and 6.49.21.&rdquo; The missing beta was an artefact of the relay, not of the advisory. '
        'That leaves exactly one build in dispute: <b>7.23.5</b>, which Security Affairs on '
        '6 September lists as fixed and dates to <b>4 September</b>, and which cert.pl does not '
        'mention. A list published before a build shipped is not evidence against that build, so '
        'the five-build set remains what this page tells readers to patch to &mdash; but the '
        'four that carry the vendor-coordinated CERT Polska imprimatur are now named as such. ')
print('  skip: already applied (1)')

# ---------------------------------------------------------------- 2. provenance
old2 = ('CERT Polska’s advisory was fetched directly from cert.pl in an <i>earlier</i> '
        'edition, <b>not this one</b> — and this page says so rather than repeating a fetch '
        'claim it cannot support this morning. Corroboration today comes by a different and '
        'independent route: <b>Cybernews</b> and <b>Security Affairs</b> were each fetched '
        'directly this run, both quote that same CERT Polska advisory, and the IoCs, the two '
        'source IPs and all <b>six</b> RouterOS CVEs above match what this page already carried. ')
new2 = ('<b>Provenance, corrected upward this run:</b> CERT Polska’s advisory '
        '<b>was fetched directly from cert.pl this morning</b>, which is what allowed the '
        'correction above. The previous edition could only reach it through Cybernews and '
        'Security Affairs and said so; this edition reads the primary. Everything in this block '
        '— the MikroTrick name, the two chained CVEs and their 9.2 scores, the 8.8 on the '
        'bandwidth-test bug, the log-line IoCs, the <span class="mono">ops</span> account, both '
        'source IPs and the 2 September start date — now traces to CERT Polska’s own '
        'text rather than to a relay of it, and every one of them matches what this page already '
        'carried. ')
print('  skip: already applied (2)')

# ------------------------------------------------- 3. NEW: the "Flagged" marker + fallbacks
anchor = '<h2 class="sec">CISA KEV &amp; Federal Deadlines</h2>'
if anchor not in h:
    sys.exit('MISS: kev anchor')
block = (
 '<div class="panel" style="margin:14px 0">'
 '<p><b>Newly read from the primary this run: the &ldquo;Flagged&rdquo; marker, and what it does '
 'and does not tell you.</b> The patched RouterOS builds ship a mechanism that, at startup, scans '
 'the configuration for known signs of unauthorised change, <b>disables the entries it recognises '
 'as suspicious</b>, writes a critical message to the log and sets a warning marker. Administrators '
 'read it with <span class="mono">/system/device-mode/print</span>. CERT Polska is unusually blunt '
 'about its limits: the mechanism &ldquo;detects only selected traces left after a compromise &mdash; '
 'the absence of the marker is not proof that the device is safe,&rdquo; and it cannot rule out bugs '
 'the vendor did not describe in the changelog. So the marker is evidence of a <i>possible</i> earlier '
 'compromise, not proof that one of these six CVEs was the way in. <b>If a device is flagged, treat it '
 'as taken over:</b> isolate it, secure the logs and configuration <i>before</i> resetting, factory-reset '
 'it, rebuild from a configuration you trust rather than restoring a backup off the suspect device, and '
 'rotate every password, key and secret it held. Do not clear the marker until that material is secured.</p>'
 '<p class="mut"><b>If you cannot patch today,</b> CERT Polska&rsquo;s interim measures &mdash; explicitly '
 'described as reducing attack surface rather than replacing the update &mdash; are to block or disable '
 'the exposed services from everything outside a trusted management network, naming <b>SSH</b>, '
 '<b>WWW/WWW-SSL</b> and the <b>bandwidth-test server</b> in particular; and, from an unpatched device, '
 'to stop initiating TLS connections and stop using the built-in SSH clients '
 '(<span class="mono">/system ssh</span>, <span class="mono">/system ssh-exec</span>), especially across '
 'untrusted networks or toward untrusted hosts. This is a newly-sourced remediation detail on an item '
 'already on this page, so it carries no New tag.</p>'
 '</div>\n')
h = h.replace(anchor, block + anchor, 1)
n += 1
print('  ok: Flagged marker + interim mitigations block')

# ---------------------------------------------------------------- 4. sources footer
src_new = ('<li><a href="https://cert.pl/en/posts/2026/09/vulnerabilities-in-mikrotik-routeros-actively-exploited/">'
           'CERT Polska &mdash; &ldquo;Critical vulnerabilities in MikroTik RouterOS are being actively '
           'exploited&rdquo; (05 September 2026) &mdash; fetched directly this run</a></li>')
m = re.search(r'(<h2 class="sec">Sources</h2>.*?<ul[^>]*>)', h, re.S)
if not m:
    sys.exit('MISS: sources list')
h = h[:m.end()] + src_new + h[m.end():]
n += 1
print('  ok: sources footer')

io.open(P, 'w', encoding='utf-8').write(h)
print('cyber: %d edits, %d -> %d bytes' % (n, len(orig), len(h)))
