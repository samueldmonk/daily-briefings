# -*- coding: utf-8 -*-
import re, sys, os
R = "/tmp/db_1788800764"
OUT = "/sessions/brave-zen-dijkstra/mnt/outputs"
PREV = "12:45"          # previous edition label
PAGES = ["index","cyber-briefing","wallstreet-briefing","mma-briefing"]
S = {p: open(os.path.join(R,p+".html"),encoding="utf-8").read() for p in PAGES}
log = []
def sub1(page, old, new, why):
    s = S[page]
    n = s.count(old)
    assert n == 1, "EXPECTED 1 OCCURRENCE, GOT %d :: %s :: %s" % (n, page, why)
    S[page] = s.replace(old, new)
    log.append("%-20s %s" % (page, why))

# ---------- A. demote provenance: "this edition" -> "the 12:45 edition" ----------
for p in PAGES:
    before = S[p].count("this edition")
    S[p] = S[p].replace("this edition", "the %s edition" % PREV)
    if before:
        log.append("%-20s demoted %d 'this edition' -> 'the %s edition'" % (p, before, PREV))

# ---------- B. strip the stale New tag (CVE-2026-84147 row, new at 12:45) ----------
assert S["cyber-briefing"].count('class="t new">New') == 1
S["cyber-briefing"] = S["cyber-briefing"].replace('class="t new">New', 'class="t">Carried', 1)
log.append("cyber-briefing       stripped stale New tag on CVE-2026-84147 (was new at %s)" % PREV)

# ---------- C. insert the Tengu card, tagged New ----------
anchor = '<div class="card">\n<div class="tags"><span class="t">Carried</span><span class="t crit">No patch</span><span class="t hot">RMM</span></div>'
tengu = '''<div class="card">
<div class="tags"><span class="t new">New</span><span class="t hot">Linux / IoT</span><span class="t">Botnet</span></div>
<h3>Tengu: a Mirai-derived Linux bot that reboots the machine when you kill it &mdash; a fresh static analysis lands today</h3>
<p><b>A static analysis of the <b>Tengu</b> Linux bot dated <b>7&nbsp;September 2026</b> is the one piece of genuinely new security research this desk found today.</b> The malware itself is not new &mdash; it was first documented in <b>late July 2026</b> by Nozomi Networks and picked up then by Help Net Security and The Hacker News &mdash; but the sample dissected in the new write-up is described as <b>newly analysed</b>, and it puts numbers on the framework: <b>464 functions</b> recovered from a <b>stripped 32-bit ELF</b>. <span class="mut">Carried from search returns; the underlying vendor research was not fetched first-hand this edition, and this card says so.</span></p>
<p><b>What makes it awkward to remove is the point of it.</b> Tengu masquerades as a Linux kernel worker, overwriting its own argument memory with a randomised process name in the <code>kworker/%d:%d</code> pattern so it reads as routine system activity in a process list. A <b>hidden guardian process checks every 60&nbsp;seconds</b> whether the main process is still alive and restarts it. If that is defeated, the bot <b>abuses the Linux hardware watchdog to force a reboot</b> when its main process is killed &mdash; giving itself another chance to start. It also <b>overwrites the <code>reboot</code> and <code>shutdown</code> binaries</b> with the string <code>ELFOOD</code>, so an administrator cannot restart or power down an infected host through the standard commands.</p>
<p><b>Capability and spread.</b> It propagates by <b>brute-forcing Telnet credentials</b> and supports <b>25 DDoS methods</b> &mdash; raw UDP and standard datagram floods alongside web-request generation &mdash; plus <b>SOCKS5 proxying</b>, shell-command execution, SSH probing, data collection, self-update, and retrieval of further <b>ELF or APK</b> payloads. Targets are described as servers, embedded devices and IoT-adjacent systems; infected hosts can be used to relay traffic as well as to send it.</p>
<p><b>What is deliberately absent.</b> There is <b>no victim count, no attribution, no CVE and no CVSS</b> in any return read this edition, and Tengu is <b>not in the CISA KEV catalog</b> &mdash; it is malware, not a vulnerability, so no federal remediation deadline attaches to it and none is printed. <span class="mut">Sources this edition: search returns citing the 7&nbsp;September analysis, alongside the July research from Nozomi Networks, Help Net Security (29&nbsp;July 2026), The Hacker News and SC Media. None fetched first-hand.</span></p>
</div>
'''
sub1("cyber-briefing", anchor, tengu + anchor, "inserted Tengu card (New) at the head of Breaches & Incidents")

# ---------- D. rewrite the new-tag ledger note on the cyber page ----------
m = re.search(r'<p class="note" style="margin:-4px 0 12px"><b>Two items are tagged New.*?</p>\n', S["cyber-briefing"], re.S)
assert m, "cyber new-tag note not found"
newnote = ('<p class="note" style="margin:-4px 0 12px"><b>One item is tagged New this edition, and it is on this page: the <b>Tengu</b> Linux-bot analysis immediately below. '
 'The Wall Street and MMA pages carry no new item this edition, and neither is given a tag.</b> '
 '<span class="mut">Measured against <code>archive/cyber-2026-09-07-1245.html</code>, <code>archive/wallstreet-2026-09-07-1245.html</code> and <code>archive/mma-2026-09-07-1245.html</code>, counting the markup these pages actually emit (<code>class=&quot;t new&quot;</code>) and asserting <b>placement per page</b> rather than a bare total. '
 'The 12:45 snapshots carried <b>one</b> New tag in total &mdash; CVE-2026-84147 on this page &mdash; and that item is still here and still correct, but it was in the previous archived edition, so its tag has been removed and replaced with <b>Carried</b>. '
 'A tag is a statement about the previous snapshot, not about how recently the underlying event happened.</span> '
 '<b>Nothing new was found for markets or MMA this edition</b> &mdash; U.S. exchanges are shut for Labor Day and the UFC calendar did not move &mdash; <span class="mut">and an edition with one new item is reported as one, rather than padded to three.</span></p>\n')
S["cyber-briefing"] = S["cyber-briefing"][:m.start()] + newnote + S["cyber-briefing"][m.end():]
log.append("cyber-briefing       rewrote new-tag ledger note (1 new: Tengu; 0 markets, 0 MMA)")

open(os.path.join(R,"_stage1.txt"),"w").write("\n".join(log))
for p in PAGES:
    open(os.path.join(R,p+".html"),"w",encoding="utf-8").write(S[p])
print("\n".join(log))
