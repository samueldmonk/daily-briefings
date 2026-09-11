import io
P = "/sessions/fervent-serene-bohr/mnt/outputs/cyber-briefing.html"
s = io.open(P, encoding="utf-8").read()
n = 0
def rep(old, new):
    global s, n
    assert s.count(old) == 1, ("NOT UNIQUE/ABSENT: %r (%d)" % (old[:70], s.count(old)))
    s = s.replace(old, new); n += 1

# 1 — both carried New tags expire: WatchGuard and IDScan are in the archived 1811 snapshot
rep('<div class="tags"><span class="t new">New</span><span class="t">ransomware</span><span class="t">firewall</span></div>',
    '<div class="tags"><span class="t">ransomware</span><span class="t">firewall</span></div>')
rep('<div class="tags"><span class="t new">New</span><span class="t">identity documents</span><span class="t">dark web</span></div>',
    '<div class="tags"><span class="t">identity documents</span><span class="t">dark web</span></div>')

# 2 — WatchGuard: the KEV field flip and the exposure numbers
rep("""A perimeter firewall reachable from the internet and running unpatched Fireware should be treated as the same tier of urgency as the 12 September batch below.</p>""",
    """A perimeter firewall reachable from the internet and running unpatched Fireware should be treated as the same tier of urgency as the 12 September batch below.</p>
      <p style="margin:10px 0 0">What actually changed is a single field in the catalogue: the December entry carried its ransomware flag as <b>"Unknown"</b>, and it was <b>quietly flipped to "Known" this week</b> — which is why this reads as news without being a new addition or a new deadline. The exposure is the reason it matters: <b>Shadowserver counted more than 115,000 unpatched Fireboxes reachable online in December</b>, and <b>nearly 9,000 remain unpatched nine months later</b>.</p>""")

# 3 — IDScan: the timeline, the marketplace, the FBI and the lawsuit are all sourced now
rep("""<b>No ransom demand, intrusion vector or disclosure timeline appeared in any source read this run</b>, so none is stated here.</p>""",
    """The timeline is now sourced: IDScan says it learned <b>on or around 1 September</b> that data may have been accessed without authorisation and disclosed the incident in a <b>4 September security notice</b>, confirming that attackers reached customer data held in its <b>cloud platform</b>. The leak surfaced after security journalist <b>Brian Krebs</b> reported that a dark-web marketplace called <b>Nexus</b> was selling access to the licence scans — <b>US and Canadian</b> documents — alongside <b>10 million ID cards, 3 million travel documents and 579,000 medical cards</b>. Exposed fields can include full names and driver's-licence or other government-issued identification numbers. The <b>FBI is investigating</b>, and IDScan has already been <b>sued</b> over the alleged breach. <b>No ransom demand or intrusion vector appeared in any source read</b>, so neither is stated here.</p>""")

# 4 — stat strip: swap in the fresher Firebox exposure figure
rep("""<div class="stat"><div class="n">1,079,819</div><div class="l">people in the Mathspace breach</div></div>""",
    """<div class="stat"><div class="n">~9,000</div><div class="l">Fireboxes still unpatched (Shadowserver)</div></div>""")

# 5 — summary strip: sharpen with the FBI probe
rep("""and identity vendor IDScan confirmed a breach after 153 million driver's licences leaked to the dark web.""",
    """and identity vendor IDScan confirmed a breach after 153 million driver's licences leaked to a dark-web marketplace, an incident the FBI is now investigating.""")

# 6 — sources read this run
rep("""    <div class="srcline"><b>Sources read this run</b></div>""",
    """    <div class="srcline"><b>Sources read this run</b></div>
    <div class="srcline">Krebs on Security — FBI Probes Service Selling 153M+ Drivers Licenses — <a href="https://krebsonsecurity.com/2026/09/fbi-probes-service-selling-153m-drivers-licenses/">https://krebsonsecurity.com/2026/09/fbi-probes-service-selling-153m-drivers-licenses/</a></div>
    <div class="srcline">BleepingComputer — IDScan confirms breach tied to 153 million stolen driver's licenses — <a href="https://www.bleepingcomputer.com/news/security/idscan-confirms-breach-tied-to-153-million-stolen-drivers-licenses/">https://www.bleepingcomputer.com/news/security/idscan-confirms-breach-tied-to-153-million-stolen-drivers-licenses/</a></div>
    <div class="srcline">BleepingComputer — IDScan sued over alleged data breach affecting 153 million drivers — <a href="https://www.bleepingcomputer.com/news/security/idscan-sued-over-alleged-data-breach-affecting-153-million-drivers/">https://www.bleepingcomputer.com/news/security/idscan-sued-over-alleged-data-breach-affecting-153-million-drivers/</a></div>
    <div class="srcline">CSO Online — FBI investigates breach of 153 million driving license records at IDscan.net — <a href="https://www.csoonline.com/article/4218789/fbi-investigates-breach-of-153-million-driving-license-records-at-idscan-net.html">https://www.csoonline.com/article/4218789/fbi-investigates-breach-of-153-million-driving-license-records-at-idscan-net.html</a></div>
    <div class="srcline">Help Net Security — IDScan confirms breach after 153 million driver's licenses leak on dark web — <a href="https://www.helpnetsecurity.com/2026/09/11/idscan-net-data-breach-153-million-drivers-licenses/">https://www.helpnetsecurity.com/2026/09/11/idscan-net-data-breach-153-million-drivers-licenses/</a></div>
    <div class="srcline">SC Media — CISA: WatchGuard Firebox bug exploited in ransomware campaigns — <a href="https://www.scworld.com/news/cisa-watchguard-firebox-bug-exploited-in-ransomware-campaigns/">https://www.scworld.com/news/cisa-watchguard-firebox-bug-exploited-in-ransomware-campaigns/</a></div>
    <div class="srcline">The Hacker News — GitLab CVSS 10 File-Read Flaw Draws In-the-Wild Probes After Disclosure — <a href="https://thehackernews.com/2026/09/gitlab-cvss-10-file-read-flaw-draws-in.html">https://thehackernews.com/2026/09/gitlab-cvss-10-file-read-flaw-draws-in.html</a></div>
    <div class="srcline">watchTowr — Rapid Reaction: GitLab Path Traversal Vulnerability (CVE-2026-85706) — <a href="https://watchtowr.com/resources/rapid-reaction-gitlab-critical-path-traversal-vulnerability-cve-2026-85706/">https://watchtowr.com/resources/rapid-reaction-gitlab-critical-path-traversal-vulnerability-cve-2026-85706/</a></div>
    <div class="srcline">The Hacker News — CISA Flags Exploited Cisco, Citrix, Fortinet Flaws, Sets Sept. 12 Federal Patch Deadline — <a href="https://thehackernews.com/2026/09/cisa-flags-exploited-cisco-citrix.html">https://thehackernews.com/2026/09/cisa-flags-exploited-cisco-citrix.html</a></div>
    <div class="srcline">Privacy Guides — Data Breach Roundup (Sep 4–10, 2026) — <a href="https://www.privacyguides.org/news/2026/09/11/data-breach-roundup-sep-4-10-2026/">https://www.privacyguides.org/news/2026/09/11/data-breach-roundup-sep-4-10-2026/</a></div>""")

io.open(P, "w", encoding="utf-8").write(s)
print("cyber edits applied:", n)
