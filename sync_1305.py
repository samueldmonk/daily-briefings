#!/usr/bin/env python3
"""Sync index.html cards to each briefing's own tldr sentence; append this run's sources."""
import re, os, shutil
SRC = "/tmp/db_1789232738"
OUT = "/sessions/sleepy-hopeful-carson/mnt/outputs"
def load(f, src=OUT): return open(os.path.join(src, f), encoding="utf-8").read()
def save(f, s): open(os.path.join(OUT, f), "w", encoding="utf-8").write(s)

fails = []

# index.html starts from the repo copy
shutil.copy(os.path.join(SRC, "index.html"), os.path.join(OUT, "index.html"))
ix = load("index.html")

def tldr_of(f):
    s = load(f)
    m = re.search(r'<div class="tldr"><b>[^<]*</b>\s*<span>(.*?)</span></div>', s, re.S)
    if not m: fails.append("no tldr in " + f); return None
    return m.group(1)

pairs = [("cyber-briefing.html", "c-sec"), ("wallstreet-briefing.html", "c-mkt"), ("mma-briefing.html", "c-mma")]
for f, cls in pairs:
    t = tldr_of(f)
    if t is None: continue
    pat = re.compile(r'(<a class="%s"[^>]*>.*?<h3>[^<]*</h3><p>)(.*?)(</p>)' % cls, re.S)
    if not pat.search(ix):
        fails.append("no index card for " + cls); continue
    ix = pat.sub(lambda m: m.group(1) + t + m.group(3), ix, count=1)

save("index.html", ix)

# ---------- footers: append this run's sources ----------
NEW_SOURCES = {
 "cyber-briefing.html": [
   ("Privacy Guides — Data Breach Roundup (Sep 4–10, 2026)", "https://www.privacyguides.org/news/2026/09/11/data-breach-roundup-sep-4-10-2026/"),
   ("BleepingComputer — Trezor data breach impact now reaches 81,000 customers", "https://www.bleepingcomputer.com/news/security/trezor-data-breach-impact-now-reaches-81-000-customers/"),
   ("BleepingComputer — Trezor: 347,000 users targeted in phishing after Brevo breach", "https://www.bleepingcomputer.com/news/security/trezor-347-000-users-targeted-in-phishing-attacks-after-brevo-breach/"),
   ("BleepingComputer — 220 million traveler records exposed in Vietnam-linked APIS leak", "https://www.bleepingcomputer.com/news/security/220-million-traveler-records-exposed-in-vietnam-linked-apis-leak/"),
   ("BleepingComputer — Veradigm warns of patient data breach", "https://www.bleepingcomputer.com/news/security/veradigm-discloses-patient-data-breach-after-gentlemen-gang-claims-attack/"),
   ("BleepingComputer — AdaptHealth confirms 4.1 million people exposed", "https://www.bleepingcomputer.com/news/security/adapthealth-confirms-41-million-people-exposed-in-july-cyberattack/"),
   ("Wiz — Inside the Metabase SQLi: Exploited in the Wild", "https://www.wiz.io/blog/inside-the-metabase-sqli-exploited-in-the-wild"),
   ("OffSec — CVE-2026-72898: Critical Metabase Unauthenticated SQL Injection", "https://www.offsec.com/blog/cve-2026-72898/"),
   ("IONIX — CVE-2026-72898 affected versions", "https://www.ionix.io/threat-center/cve-2026-72898/"),
   ("The Hacker News — Metabase zero-day exploited in wild", "https://thehackernews.com/2026/08/metabase-zero-day-exploited-in-wild.html"),
   ("Rescana — Trezor/ShipMonk breach attributed to CVE-2026-72898", "https://www.rescana.com/post/trezor-shipmonk-breach-exposes-67-000-u-s-customer-records-via-metabase-zero-day-vulnerability-cve-2026-72898"),
   ("CISA — Adds four Known Exploited Vulnerabilities to Catalog (9 Sep 2026)", "https://www.cisa.gov/news-events/alerts/2026/09/09/cisa-adds-four-known-exploited-vulnerabilities-catalog"),
   ("CISA — Adds two Known Exploited Vulnerabilities to Catalog (10 Sep 2026)", "https://www.cisa.gov/news-events/alerts/2026/09/10/cisa-adds-two-known-exploited-vulnerabilities-catalog"),
   ("Tenable — September 2026 Patch Tuesday (964 CVEs)", "https://www.tenable.com/blog/microsofts-september-2026-patch-tuesday-addresses-964-cves-cve-2026-81963-cve-2026-85880"),
   ("The Cyber Express — Patch Tuesday September 2026 fixes 974 CVEs", "https://thecyberexpress.com/patch-tuesday-september-2026/"),
 ],
 "wallstreet-briefing.html": [
   ("CNBC — Oil prices fall Friday but post sharp weekly gains", "https://www.cnbc.com/2026/09/11/oil-price-today-iran-brent-wti-trump.html"),
   ("CNBC — Stock market next week: outlook for Sept. 14–18, 2026", "https://www.cnbc.com/2026/09/11/stock-market-next-week-outlook-for-sept-14-18-2026.html"),
   ("IG — Week Ahead: 14 September 2026", "https://www.ig.com/ae/news-and-trade-ideas/week-ahead--14-september-2026-260911"),
   ("CNBC — Stock market news for Sept. 11, 2026", "https://www.cnbc.com/2026/09/10/stock-market-today-live-updates.html"),
 ],
 "mma-briefing.html": [
   ("UFC.com — Prelim Results | Noche UFC (matchup previews at build time)", "https://www.ufc.com/news/noche-ufc-prelim-results-silva-vs-delgado"),
   ("UFC.com — Noche UFC: Silva vs Delgado event page", "https://www.ufc.com/event/ufc-fight-night-september-12-2026"),
   ("Yahoo Sports — Noche UFC live results and start time", "https://sports.yahoo.com/mma/live/noche-ufc-live-results-jean-silva-vs-jose-delgado-updates-round-by-round-scoring-and-start-time-063000680.html"),
 ],
}

for f, items in NEW_SOURCES.items():
    s = load(f)
    m = re.search(r"(<footer>.*?<ul[^>]*>)(.*?)(</ul>)", s, re.S)
    if not m:
        fails.append("no footer ul in " + f); continue
    existing = m.group(2)
    add = ""
    for title, url in items:
        if url in existing:   # dedupe
            continue
        add += '<li><a href="%s" target="_blank" rel="noopener">%s</a></li>' % (url, title)
    s = s.replace(m.group(0), m.group(1) + existing + add + m.group(3), 1)
    save(f, s)

print("SYNC FAILURES:", len(fails))
for f in fails: print("  " + f)
