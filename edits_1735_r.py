import io,sys
def rep(h, old, new, n=1):
    c = h.count(old)
    assert c == n, "count %d != %d for: %r" % (c, n, old[:90])
    return h.replace(old, new)

# ---------------- CYBER ----------------
f='cyber-briefing.html'; h=open(f).read()

# 1. strip stale New tags (both present in archive/cyber-2026-09-06-1715.html)
h = rep(h, '<span class="t hot">Network edge</span><span class="t new">New</span>',
           '<span class="t hot">Network edge</span>')
h = rep(h, '<span class="t hot">E-commerce</span><span class="t new">New</span>',
           '<span class="t hot">E-commerce</span>')

# 2. new card: MikroTik's own advisory read first-hand
raiu_anchor = '<div class="card">\n<div class="tags"><span class="t hot">Network edge</span></div>\n<h3>MikroTrick gets an independent breakdown'
if raiu_anchor not in h:
    # tolerate whitespace differences
    import re
    m = re.search(r'<div class="card">\s*<div class="tags"><span class="t hot">Network edge</span></div>\s*<h3>MikroTrick gets an independent breakdown', h)
    assert m, "raiu card anchor not found"
    raiu_anchor = m.group(0)

newcard = '''<div class="card">
<div class="tags"><span class="t hot">Network edge</span><span class="t new">New</span></div>
<h3>MikroTik&rsquo;s own advisory, read first-hand &mdash; the router will tell you if it was owned</h3>
<p><b>This desk had cited MikroTik&rsquo;s security bulletin as a source for three editions without ever reading it. It was fetched directly this run</b>, and it carries a detection mechanism that has not appeared on this page before. The vendor page, dated <b>3 September</b>, says RouterOS <b>&ldquo;will check if your device has been compromised, and set it to &lsquo;Flagged&rsquo; status if it is&rdquo;</b> &mdash; written to the <b>Log</b> section as a <i>critical</i> entry, with recovery steps on MikroTik&rsquo;s Flagged-status documentation page. The vendor adds the warning that matters for anyone reading a clean log: even a device that is <b>not</b> Flagged should be inspected after upgrading for unrecognised scripts, users and configuration. That is the vendor&rsquo;s own instruction, and it lines up with Costin Raiu&rsquo;s separate caution below that the absence of a failed-login artefact proves nothing.</p>
<p style="margin:10px 0 0"><b>Two further things the vendor page settles.</b> First, MikroTik is <b>deliberately withholding technical detail</b> &mdash; <span class="mut">&ldquo;To give time to update your systems, we are not currently publishing detailed information&rdquo;</span> &mdash; and says the article will be updated in due time, which is why no vendor CVE or CVSS is quoted anywhere on this page. Second, the vendor&rsquo;s fixed-build list is <b>exactly four</b>: <b>7.25 beta 3, 7.24.2, 7.23.4 and 6.49.21</b>. That matches CERT Polska and <b>does not include 7.23.5</b>, so the divergence recorded below is now three-to-one and is still printed rather than merged.</p>
<p style="margin:10px 0 0"><b>One note of caution about the vendor&rsquo;s framing.</b> MikroTik calls this &ldquo;an important security update&rdquo; but says <b>&ldquo;most configurations are not at risk&rdquo;</b> and that for <b>&ldquo;regular home device users the issue does not pose an immediate risk.&rdquo;</b> That is a materially calmer reading than CERT Polska&rsquo;s, which describes active exploitation since 2 September. <span class="mut">Both are printed as each party stated them; this desk does not adjudicate between the vendor&rsquo;s risk assessment and the CERT&rsquo;s.</span></p>
</div>
'''
h = rep(h, raiu_anchor, newcard + raiu_anchor)

# 3. rewrite the New-tag accounting note
old_note_start = '<p class="note" style="margin:-4px 0 12px"><b>Two items are tagged New this edition.</b>'
i = h.find(old_note_start); assert i >= 0
j = h.find('</p>', i) + 4
new_note = '''<p class="note" style="margin:-4px 0 12px"><b>One item is tagged New this edition, and two stale tags were removed.</b> The new one is the MikroTik vendor-advisory card below: <span style="font-family:var(--mono);font-size:12.5px">mikrotik.com/supportsec/september-2026-vulnerability/</span> was fetched directly for the first time this run, and the terms it turns on &mdash; &ldquo;Flagged,&rdquo; &ldquo;not currently publishing detailed information&rdquo; and &ldquo;home device users&rdquo; &mdash; each return <b>zero</b> matches in <span style="font-family:var(--mono);font-size:12.5px">archive/cyber-2026-09-06-1715.html</span>, so the tag is earned rather than assumed. <b>Removed:</b> the Raiu card and the StyleSmuggler-mitigation card both still carried <b>New</b> from earlier editions, and both appear in the 1715 snapshot &mdash; the tags were stripped rather than left to decay, the same discipline applied to the CPI item earlier today. Everything else was re-checked and carried: CrowdStrike SafeMind, the StyleSmuggler vulnerability row and Cisco Nexus 9000 all remain <b>Carried forward</b>. <b>Cyber carries 1 New tag, Wall Street 0, MMA 0.</b></p>'''
h = h[:i] + new_note + h[j:]

# 4. Sansec partial-fetch refusal appended to the refusals note
anchor = 'They are named here so the next run knows what to chase, not asserted.</p>'
h = rep(h, anchor, anchor + '''
<p class="note" style="margin:0 0 12px"><b>A direct fetch that only half-worked, reported as such.</b> <span style="font-family:var(--mono);font-size:12.5px">sansec.io/research/stylesmuggler</span> &mdash; the primary StyleSmuggler advisory, which this page has so far only ever read through other outlets &mdash; was requested this run. The response returned the page&rsquo;s <b>metadata</b> (author <b>Sansec Forensics Team</b>, <span style="font-family:var(--mono);font-size:12.5px">article:modified_time 2026-09-05T20:18:09Z</span>) and its section headings, but <b>the article body did not render</b>. <b>No figure, indicator or detail is taken from it</b>, and nothing on this page is upgraded to first-hand Sansec sourcing on the strength of a fetch that returned navigation. &#9733; Next run: retry the body.</p>''')

open(f,'w').write(h); print('cyber ok', len(h))

# ---------------- WALL STREET ----------------
f='wallstreet-briefing.html'; h=open(f).read()
h = rep(h, ' <span class="t new" style="margin-left:4px">New</span>', '')
h = rep(h, '<li><span class="t new" style="margin-right:7px">New</span>', '<li>')

h = rep(h,
 '<tr><td>WTI crude</td><td><b>~$91</b></td><td class="mut">Traded near $91 on Friday. No settle figure is asserted &mdash; none was sourced.</td></tr>',
 '<tr><td>WTI crude</td><td><b>~$91</b></td><td class="mut">Traded near $91 on Friday. A figure is sourced this run for the first time: <b>Trading Economics puts WTI at $91.48 on 4 September, up 0.20% on the day</b>. That is printed with its name on it and <b>not</b> as an official settle &mdash; one return is not corroboration, and the Brent row directly above is a standing reminder of what happens when a single crude print is treated as settled. The <b>~$91</b> level, which two earlier runs agreed on, is what the row still carries.</td></tr>')

h = rep(h,
 'A yield is a single number, so the conflict is printed and no level is carried. The direction &mdash; higher on the week, then lower after Waller &mdash; is not in dispute.',
 'A yield is a single number, so the conflict is printed and no level is carried. <b>The withdrawal is corroborated a second time this run:</b> a fresh pair of returns gave <b>&ldquo;around 4.76%&rdquo;</b> and <b>&ldquo;closed at 4.78%&rdquo;</b> for the same Friday &mdash; two more readings that are not roundings of one another, let alone of 4.79%. Four independent returns across two runs have now failed to agree on this one number, so the row stays empty. The direction &mdash; higher on the week, then lower after Waller &mdash; is not in dispute.')

open(f,'w').write(h); print('ws ok', len(h))

# ---------------- MMA ----------------
f='mma-briefing.html'; h=open(f).read()
h = rep(h,
 'That is four named outlets against the promotion&rsquo;s own page, and the <b>eighth consecutive edition</b> in which the two have failed to converge.',
 'That is four named outlets against the promotion&rsquo;s own page, and the <b>ninth consecutive edition</b> in which the two have failed to converge.')
h = rep(h,
 'byte-for-byte identical across five consecutive runs now, so the promotion has not revised it.',
 'byte-for-byte identical across <b>six</b> consecutive runs now, so the promotion has not revised it.')

h = rep(h, '<h2 class="sec">Champions Board</h2>',
 '''<h2 class="sec">Champions Board</h2>
<p class="note" style="margin:-4px 0 12px"><b>A division label was mis-stated in this run&rsquo;s sources and was not taken.</b> An ESPN-sourced return re-listed the champions with the right names, dates, methods and defence counts &mdash; Aspinall, Ulberg, Strickland, Makhachev, Gaethje, Volkanovski, Yan, Van, Shevchenko and Dern all matched what is printed below &mdash; but it filed <b>Kayla Harrison under &ldquo;Women&rsquo;s Featherweight.&rdquo;</b> She holds the <b>women&rsquo;s bantamweight</b> title, won by second-round submission over Julianna Pe&ntilde;a at UFC 316 on 7 June 2025, and the table below is unchanged. <span class="mut">No card has been contested since UFC Paris, a non-title Fight Night, so no belt could have moved. A correct set of names carrying one wrong label is exactly the kind of return that has caused this board&rsquo;s past regressions, so it is logged rather than quietly discarded.</span></p>''')

open(f,'w').write(h); print('mma ok', len(h))
