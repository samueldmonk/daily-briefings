#!/usr/bin/env python3
# Cyber edits, 2026-09-07 ~09:35 ET run (FOURTH of the day).
# STANDING RULES OBSERVED:
#  - write to disk PER EDIT, never once at the end (0847 run's lost-edit defect)
#  - idempotency guard tests a DISTINCTIVE TOKEN OF THE NEW TEXT ONLY (0917 run's duplication defect)
#  - never sed
import io, sys, re

F = 'cyber-briefing.html'

def edit(tell, old, new, label):
    h = io.open(F, encoding='utf-8').read()
    if tell in h:
        print('skip (already applied):', label); return
    if old not in h:
        print('MISS ANCHOR:', label); sys.exit(1)
    h = h.replace(old, new, 1)
    io.open(F, 'w', encoding='utf-8').write(h)          # write per edit
    h2 = io.open(F, encoding='utf-8').read()             # re-read is the only evidence
    assert tell in h2, 'edit did not survive: ' + label
    assert h2.count(tell) == 1, 'edit duplicated: ' + label
    print('ok:', label)

# ---------------------------------------------------------------- C6 provenance
edit('including one made in the 8:47 edition',
     'including one made this run',
     'including one made in the 8:47 edition',
     'C6 CISA-alert fetch claim decayed to the edition it happened in')

# ---------------------------------------------------------------- C7 provenance
edit('Refused in earlier editions, and still refused',
     'Refused this run.',
     'Refused in earlier editions, and still refused &mdash; no daily-CVE aggregator was consulted this morning.',
     'C7 aggregator-refusal claim rewritten (no aggregator seen this run)')

# ---------------------------------------------------------------- C8 provenance in Sources
edit('PostgreSQL fixes 12-year-old logical decoding flaw (4 Sep) &mdash; fetched directly in the 9:17 edition',
     'PostgreSQL fixes 12-year-old logical decoding flaw (4 Sep) &mdash; fetched directly this run',
     'PostgreSQL fixes 12-year-old logical decoding flaw (4 Sep) &mdash; fetched directly in the 9:17 edition',
     'C8 Hacker News source line decayed to the edition it was fetched in')

# ---------------------------------------------------------------- C1 Vulnerability Watch rows
NABLE_ROWS = (
'<tr><td>CVE-2026-86218</td><td class="down"><b>&ldquo;Critical&rdquo; &mdash; no number published</b></td>'
'<td>N-able N-central (RMM) &mdash; hosted <i>and</i> on-premises, Americas / APAC / Europe</td>'
'<td><b>Pre-authenticated remote code execution on the N-central server.</b> N-able&rsquo;s release notes call it a '
'&ldquo;critical-CVSS-rated vulnerability&rdquo; but <b>publish no numeric score</b>, so none is printed here. '
'Fixed <b>5 September</b> in <b>Hotfix 4 for N-central 2026.3</b>, build <b>2026.3.1.14</b>. '
'<span class="mut">The vendor contradicts itself on exploitation: its <b>public status page</b> says there are '
'&ldquo;no confirmations that this vulnerability has been exploited in production environments,&rdquo; while a '
'<b>separate urgent notice sent directly to customers</b> says it &ldquo;has been observed being exploited in the '
'wild&rdquo; and calls it a zero-day. Help Net Security, fetched directly this run, names the contradiction. This '
'page prints both and asserts neither. <b>Not KEV-listed</b> &mdash; no CISA addition exists for 5, 6 or 7 September.</span></td></tr>\n'
'<tr><td>CVE-2026-86206</td><td><b>High &mdash; no number published</b></td><td>N-able N-central</td>'
'<td>Authentication bypass &rarr; unrestricted access to the N-central platform. Patched over the weekend of '
'5&ndash;6 September. Huntress flags it alongside CVE-2026-86218 as a <b>potential</b> zero-day.</td></tr>\n'
'<tr><td>CVE-2026-86207</td><td><b>High &mdash; no number published</b></td><td>N-able N-central</td>'
'<td>Second authentication-bypass flaw patched in the same weekend batch; Huntress says that because logs on the one '
'compromised N-central server it saw <b>had already rotated</b>, it cannot say which of the three CVEs was the one '
'actually used.</td></tr>\n'
)
edit('CVE-2026-86218</td>',
     '<tr><th>CVE</th><th>CVSS</th><th>Affected</th><th>Note</th></tr>\n',
     '<tr><th>CVE</th><th>CVSS</th><th>Affected</th><th>Note</th></tr>\n' + NABLE_ROWS,
     'C1 three N-able rows at the head of Vulnerability Watch')

# ---------------------------------------------------------------- C3 Patch Priority
NABLE_PATCH = (
'<p style="margin:0 0 8px"><b>First, because unlike the item below there is actually something to install: if you '
'run N-able N-central on-premises, apply Hotfix 4 now.</b> <b>CVE-2026-86218</b> is a <b>pre-authenticated remote '
'code execution</b> flaw in the N-central server &mdash; the remote monitoring and management console that managed '
'service providers use to reach every downstream customer estate, which is what makes a single unpatched console a '
'fleet-wide problem rather than a local one. N-able shipped the fix on <b>5 September</b> as <b>N-central 2026.3 '
'HF4</b>, build <b>2026.3.1.14</b>, and told customers to &ldquo;upgrade to N-central 2026.3 HF4 immediately.&rdquo; '
'Hosted and on-premises deployments across the Americas, APAC and Europe are listed as impacted. '
'<b>The vendor&rsquo;s two accounts of exploitation do not agree</b> &mdash; the public status page says there are no '
'confirmations of exploitation in production, the urgent customer notice says it &ldquo;has been observed being '
'exploited in the wild&rdquo; and calls it a zero-day &mdash; so treat the more severe account as the planning '
'assumption and the milder one as unconfirmed. Two further authentication-bypass flaws, <b>CVE-2026-86206</b> and '
'<b>CVE-2026-86207</b>, were patched the same weekend. N-able&rsquo;s own post-patch instruction is to '
'<b>audit N-central user accounts for unexpected users</b>; Huntress adds that on the one compromised server it '
'examined the logs had already rotated, so absence of evidence in your own logs is not evidence of absence. '
'<span class="mut">No numeric CVSS is printed for any of the three because the vendor has published none. '
'No KEV entry exists for them &mdash; CISA has made no addition on 5, 6 or 7 September.</span></p>\n'
)
edit('if you run N-able N-central on-premises, apply Hotfix 4 now',
     '<h3>Patch Priority &mdash; unpatched zero-day, and an elapsed deadline</h3>\n',
     '<h3>Patch Priority &mdash; a fresh MSP-console RCE with a fix, an unpatched zero-day without one, and an elapsed deadline</h3>\n' + NABLE_PATCH,
     'C3 N-able paragraph prepended to Patch Priority + heading rewritten')

print('--- cyber edits done ---')
