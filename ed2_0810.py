# -*- coding: utf-8 -*-
import io
D='/tmp/db_1788782763/'
def load(f): return io.open(D+f,encoding='utf-8').read()
def save(f,h): io.open(D+f,'w',encoding='utf-8').write(h)
N=[0]
def rep(h,old,new,cnt=1):
    assert h.count(old)==cnt, ("COUNT %d!=%d for: %r"%(h.count(old),cnt,old[:110]))
    N[0]+=1
    return h.replace(old,new)

c=load('cyber-briefing.html')

# 5) rewrite the MikroTik refusal note: six CVEs now described; 7.23.5 resolved
old=('(2) <b>MikroTik:</b> MikroTik&rsquo;s own 3 September bulletin says it is not publishing detailed information yet, '
     'so only the three CVEs above are described; CERT Polska coordinated <b>six</b> RouterOS disclosures in total, of which two chain into the unauthenticated takeover. '
     'Affected builds run <b>up to 6.49.20 / 7.23.3 / 7.24.1</b>; fixes are in 7.25 beta 3 / 7.24.2 / 7.23.4 / 6.49.21 per that advisory, and Security Affairs today adds <b>7.23.5</b>, '
     'released 4 September &mdash; after CERT Polska published, so the two lists are printed side by side rather than merged.')
new=('(2) <b>MikroTik &mdash; the gap this page carried for four editions is now closed.</b> MikroTik&rsquo;s own 3 September bulletin still says it is '
     '&ldquo;not currently publishing detailed information,&rdquo; and it still assigns no CVE and no score of its own. But <b>CERT Polska registered all six CVEs itself</b>, and as of a '
     'Cybernews report published <b>this morning</b> every one of the six carries a published severity score &mdash; so all six are now in the table above, where previously only three were. '
     'Two chain into the unauthenticated takeover. Affected builds run <b>up to 6.49.20 / 7.23.3 / 7.24.1</b>. <b>The 7.23.5 divergence is also resolved, and not in favour of either earlier reading:</b> '
     'CERT Polska&rsquo;s own list, as relayed by Cybernews, names three fixed builds (6.49.21, 7.23.4, 7.24.2) and omits both 7.25beta3 and 7.23.5, while Security Affairs on 6 September gives the '
     'combined five &mdash; 7.25beta3, 7.24.2, 7.23.4, <b>7.23.5 (released 4 September)</b> and 6.49.21 &mdash; and states the release date explicitly. A shorter list published before a build shipped is not '
     'evidence against that build, so the fuller list is the one to patch to. <span class="mut">One transcription caveat, printed rather than smoothed: the Cybernews article&rsquo;s body text renders the '
     'kernel-memory bug as &ldquo;CVE-2026-6727&rdquo; while its own link points at CVE-2026-67277. The table above uses the linked identifier, which is also the one this page already carried.</span>')
c=rep(c,old,new)

# 6) Patch Priority: add the exposure + clean-rebuild guidance
c=rep(c,'<p style="margin:0 0 8px"><b>Third in the queue, and the one every desk can action today:</b> update Chrome.',
 '<p style="margin:0 0 8px"><b>Second, and newly quantified this morning:</b> if you run MikroTik RouterOS with SSH reachable from the internet, patch and then <i>assume compromise</i>. '
 'The <b>Shadowserver Foundation</b> now counts more than <b>122,500</b> MikroTik devices with SSH exposed &mdash; most of them in <b>Brazil (11,300)</b>, the <b>United States (7,100)</b>, '
 '<b>Indonesia (7,100)</b>, the <b>Czech Republic (6,300)</b> and <b>Ukraine (5,100)</b> &mdash; and Cybernews notes it is unclear how many remain unpatched. Upgrading alone is not sufficient: '
 'MikroTik&rsquo;s advisory says RouterOS will itself check for compromise and set a device to <b>&ldquo;Flagged&rdquo;</b> status, written to the Log as a critical entry, and that even an unflagged '
 'device should be inspected for unrecognised scripts, users and configuration. Independent researcher <b>Nick Pratley</b>, who reverse-engineered the silent patch, goes further and recommends '
 '&ldquo;a clean rebuild rather than trusting only automatic cleanup.&rdquo; <span class="mut">The two named log artefacts remain the SSH username <span style="font-family:var(--mono);font-size:13px">-2</span> '
 'and an account called <span style="font-family:var(--mono);font-size:13px">ops</span>; CERT Polska cautions that their absence does not rule out unauthorised activity.</span></p>\n'
 '<p style="margin:0 0 8px"><b>Third in the queue, and the one every desk can action today:</b> update Chrome.')

save('cyber-briefing.html',c)
print("cyber part2:",N[0])
