#!/usr/bin/env python3
# New-tag ledger + read-through polish, run 2026-09-09 ~1:50pm ET
# Demote every card that already existed in the -1315 snapshot; only genuinely
# new-since-1315 cards keep "New", materially-changed ones get "Updated".
import io
D = "/sessions/sharp-bold-tesla/mnt/outputs/"
n = 0
def rep(s, old, new, count=1):
    global n
    assert s.count(old) == count, ("NOT-UNIQUE/MISSING(%d): %s" % (s.count(old), old[:100]))
    n += count
    return s.replace(old, new)

# ---------------- WALL STREET ----------------
P = D + "wallstreet-briefing.html"
s = io.open(P, encoding="utf-8").read()

# read-through defect: paragraph order made the tense read backwards
s = rep(s, '<p>The damage widened as the morning went on. TheStreet&rsquo;s',
           '<p>Earlier in the session the damage had been widening. TheStreet&rsquo;s')

# demotions (all four cards were present in the -1315 snapshot)
s = rep(s, '<span class="t new">New</span><span class="t tag">Guidance</span>',
           '<span class="t carried">Carried</span><span class="t tag">Guidance</span>')
s = rep(s, '<span class="t new">New</span><span class="t tag">Legal</span>',
           '<span class="t carried">Carried</span><span class="t tag">Legal</span>')
s = rep(s, '<span class="t new">New</span><span class="t tag">Product</span>',
           '<span class="t carried">Updated</span><span class="t tag">Product</span>')
s = rep(s, '<span class="t new">New</span><span class="t tag">Earnings</span>',
           '<span class="t carried">Updated</span><span class="t tag">Earnings</span>')
s = rep(s, '<span class="t new">New</span><span class="t tag">Sector</span>',
           '<span class="t carried">Updated</span><span class="t tag">Sector</span>')
# Apple is the only card that did not exist in the previous snapshot
assert s.count('<span class="t new">New</span>') == 1
assert 'Apple &middot; AAPL' in s

# ledger note, mirroring the MMA page's
s = rep(s, '<h2 class="sec">Chart of the Day',
           '<div class="note" style="margin:18px 0 0"><b>On the tags.</b> The previous edition of this page published at 1:15 p.m. ET. Only the <i>Apple</i> card is new since then; <i>Meta</i>, <i>Casey&rsquo;s</i> and <i>Energy &amp; utilities</i> are marked <i>Updated</i> because each carries a figure or a fact read for the first time this run; the rest are honestly marked <i>Carried</i>. A card is not re-tagged &ldquo;New&rdquo; merely because the page was rebuilt.</div>\n\n<h2 class="sec">Chart of the Day')
io.open(P, "w", encoding="utf-8").write(s)

# ---------------- CYBER ----------------
P = D + "cyber-briefing.html"
s = io.open(P, encoding="utf-8").read()
s = rep(s, '<div class="card"><span class="t new">New</span><span class="t tag">Government</span>',
           '<div class="card"><span class="t carried">Carried</span><span class="t tag">Government</span>')
s = rep(s, '<div class="card"><span class="t new">New</span><span class="t tag">MSP</span>',
           '<div class="card"><span class="t carried">Updated</span><span class="t tag">MSP</span>')
assert s.count('<span class="t new">Context</span>') == 1  # the American Tower refusal
assert s.count('<span class="t new">New</span>') == 0

# the Huntress card should reflect what Bernstein said this run
s = rep(s, 'Limited on-appliance logging means the specific exploit used <b>cannot be confirmed</b>, and alternative vulnerabilities cannot be ruled out. For anyone running N-central, that makes this a hunting exercise as well as a patching one.',
           'Limited on-appliance logging means the specific exploit used <b>cannot be confirmed</b>, and alternative vulnerabilities cannot be ruled out. New this run: Huntress says it <b>reproduced a proof-of-concept chain against build 2026.3.1.10</b> that may use one or both of the Hotfix 3 flaws, and that it has <b>not</b> reproduced CVE-2026-86218 nor seen exploitation definitively attributable to it. For anyone running N-central, that makes this a hunting exercise as well as a patching one &mdash; and an argument for restricting inbound access to the console.')

s = rep(s, '<h2 class="sec">Vulnerability Watch</h2>',
           '<div class="note" style="margin:18px 0 0"><b>On the tags.</b> The previous edition published at 1:15 p.m. ET. One card is new since then &mdash; the American Tower refusal &mdash; and the Huntress card is marked <i>Updated</i> for the Bernstein statements read this run. Everything else is <i>Carried</i>.</div>\n\n<h2 class="sec">Vulnerability Watch</h2>')
io.open(P, "w", encoding="utf-8").write(s)
print("ledger OK, %d edits" % n)
