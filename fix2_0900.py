#!/usr/bin/env python3
"""Re-apply edits lost to a write-after-exit bug in the earlier scripts, and settle
the 10-year row for a day when the bond market is shut. 2026-09-07 ~09:00 ET.

Every edit here writes to disk immediately, so a later failure cannot silently
discard an earlier success. That was the defect.
"""
import io, sys

n = 0
def sub(path, old, new, label, expect=1):
    global n
    h = io.open(path, encoding='utf-8').read()
    if h.count(old) != expect:
        print('  MISS(%d): %s' % (h.count(old), label)); return False
    io.open(path, 'w', encoding='utf-8').write(h.replace(old, new, expect))
    n += 1; print('  ok:', label); return True

def insert_before(path, anchor, block, label):
    global n
    h = io.open(path, encoding='utf-8').read()
    if h.count(anchor) != 1:
        print('  MISS(%d): %s' % (h.count(anchor), label)); return False
    io.open(path, 'w', encoding='utf-8').write(h.replace(anchor, block + anchor, 1))
    n += 1; print('  ok:', label); return True

C = 'cyber-briefing.html'; M = 'mma-briefing.html'; W = 'wallstreet-briefing.html'

# ===================== CYBER: the "Flagged" marker block (lost)
insert_before(C, '<h2 class="sec">CISA KEV &amp; Federal Deadlines</h2>',
 '<div class="panel" style="margin:14px 0">'
 '<p><b>Newly read from the primary this run: the &ldquo;Flagged&rdquo; marker, and what it does '
 'and does not tell you.</b> The patched RouterOS builds ship a mechanism that, at startup, scans '
 'the configuration for known signs of unauthorised change, <b>disables the entries it recognises '
 'as suspicious</b>, writes a critical message to the log and sets a warning marker. Administrators '
 'read it with <span style="font-family:var(--mono);font-size:12.5px">/system/device-mode/print</span>. '
 'CERT Polska is unusually blunt about its limits: the mechanism &ldquo;detects only selected traces '
 'left after a compromise &mdash; the absence of the marker is not proof that the device is '
 'safe,&rdquo; and it cannot rule out bugs the vendor never described in the changelog. So the marker '
 'is evidence of a <i>possible</i> earlier compromise, not proof that one of these six CVEs was the '
 'way in. <b>If a device is flagged, treat it as taken over:</b> isolate it, secure the logs and '
 'configuration <i>before</i> resetting, factory-reset it, rebuild from a configuration you trust '
 'rather than restoring a backup taken off the suspect device, and rotate every password, key and '
 'secret it held. Do not clear the marker until that material is secured.</p>'
 '<p class="mut"><b>If you cannot patch today,</b> CERT Polska&rsquo;s interim measures &mdash; which '
 'it is explicit only reduce attack surface and do not replace the update &mdash; are to block or '
 'disable the exposed services from everything outside a trusted management network, naming <b>SSH</b>, '
 '<b>WWW/WWW-SSL</b> and the <b>bandwidth-test server</b> in particular; and, from an unpatched device, '
 'to stop initiating TLS connections and stop using the built-in SSH clients '
 '(<span style="font-family:var(--mono);font-size:12.5px">/system ssh</span>, '
 '<span style="font-family:var(--mono);font-size:12.5px">/system ssh-exec</span>), especially across '
 'untrusted networks or toward untrusted hosts. A newly-sourced remediation detail on an item already '
 'on this page, so it carries no New tag.</p></div>\n',
 'CYBER: Flagged marker + interim mitigations')

# ===================== MMA: name fix (lost)
sub(M, 'Jose Miguel Delgado', 'Jose Delgado', 'MMA: exact name (drop unsourced middle name)')

# ===================== MMA: Delgado detail + 13 bouts (lost)
sub(M, ('Delgado is <b>12&ndash;2</b> and 4&ndash;1 with a pair of knockouts. '
        'Officially UFC Fight Night 288, billed as Noche UFC 4.'),
       ('Delgado is <b>12&ndash;2</b> and 4&ndash;1 with a pair of knockouts, and newly sourced this '
        'edition: he has <b>won nine of his last ten</b>, he earned his roster spot with a knee to the '
        'head of <b>Ernie Juarez</b> on season 8 of Dana White&rsquo;s Contender Series in '
        '<b>August 2024</b>, and his only UFC loss came to <b>Nathaniel Wood</b> in <b>October 2025</b> '
        'by unanimous decision, in a bout he <b>missed weight</b> for. The same reporting describes '
        'Silva as the <b>No. 6-ranked</b> featherweight contender and Delgado as a sizable underdog '
        '&mdash; which the odds line below already says numerically. Officially UFC Fight Night 288, '
        'billed as Noche UFC 4, and the card carries <b>13 bouts</b> in total.'),
       'MMA: Delgado record detail + 13-bout card')

# ===================== MMA: Blaydes / Cortes-Acosta descriptors (lost)
sub(M, '<b>Waldo Cortes-Acosta vs. Curtis Blaydes</b> at heavyweight',
       ('<b>Waldo Cortes-Acosta vs. Curtis Blaydes</b> at heavyweight &mdash; the event page describes '
        'Blaydes as a former interim heavyweight <i>title challenger</i> and Cortes-Acosta as a former '
        '<b>LFA</b> heavyweight champion; both descriptors carry that attribution, and neither man is '
        'called a former UFC champion, because neither is'),
       'MMA: Blaydes / Cortes-Acosta descriptors')

# ===================== WS: 10-year row, holiday-aware
sub(W, 'US 10-year Treasury yield</td><td><b>Not asserted</b></td><td class="mut">Withdrawn this run.',
       ('US 10-year Treasury yield</td><td><b>Not asserted</b></td><td class="mut"><b>The bond market '
        'is closed today for Labor Day</b>, so there is no fresh reading to take and none is attempted; '
        'the row stands as it was withdrawn in an earlier edition, for the reason below. Withdrawn '
        'originally because:'),
       'WS: 10Y row holiday-aware')

print('fix2_0900: %d edits' % n)
