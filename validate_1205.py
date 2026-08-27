import io, re, sys
D = "/sessions/beautiful-zealous-mendel/mnt/outputs/"
PAGES = ["index.html", "cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"]
S = {p: io.open(D + p, encoding="utf-8").read() for p in PAGES}
fails, checks = [], 0

def ck(cond, msg):
    global checks
    checks += 1
    if not cond:
        fails.append(msg)

def has(p, t, msg=None):
    ck(t in S[p], msg or "%s missing: %s" % (p, t[:90]))

def absent(p, t, msg=None):
    ck(t not in S[p], msg or "%s must not contain: %s" % (p, t[:90]))

def window(p, needle, ctx_words, span=1400):
    """needle must appear, and every occurrence must sit near one of ctx_words."""
    s = S[p]
    idxs = [m.start() for m in re.finditer(re.escape(needle), s)]
    ck(len(idxs) > 0, "%s: window-scoped string vanished (liveness): %s" % (p, needle))
    for i in idxs:
        seg = s[max(0, i - span): i + span]
        ck(any(w in seg for w in ctx_words),
           "%s: '%s' not in rejection/context window" % (p, needle))

# ---------- structural, all pages ----------
for p in PAGES:
    for tab in ['href="index.html"', 'href="cyber-briefing.html"', 'href="wallstreet-briefing.html"',
                'href="mma-briefing.html"', 'href="archive.html"']:
        has(p, tab)
    for pid in ['id="edition"', 'id="datestamp"', 'id="updated"']:
        has(p, pid)
    has(p, "America/New_York")
    has(p, 'class="tabs"')
    ck(S[p].count('class="on"') == 1, "%s: exactly one active tab" % p)
for p in ["cyber-briefing.html", "wallstreet-briefing.html", "mma-briefing.html"]:
    has(p, 'class="tldr"')
    has(p, 'id="freshline"')

# ---------- edition-stamp freshness ----------
for p in PAGES:
    stamps = re.findall(r'<span class="tag new">([^<]*)</span>', S[p])
    for st in stamps:
        ck(st.startswith("New · 12:05") or st.startswith("Updated · 12:05"),
           "%s: stale or unstamped edition tag: %r" % (p, st))
    ck(not re.search(r'<span class="tag new">\s*New\s*</span>', S[p]),
       "%s: bare unstamped New tag" % p)

# ---------- WALL STREET ----------
w = "wallstreet-briefing.html"
for t in ["147.67", "0.28%", "279.61", "1.07%", "7.64", "0.25%", "Russell 2000",
          "12:05 PM ET", "217.20", "327.22", "169.90", "300.97",
          "203,000", "205,500", "$96.2 billion", "$108 billion", "75.0%",
          "7,675.70", "4.66%", "4.22%", "3.50%–3.75%", "36.1%",
          "$266.50", "6.2%", "9.4%", "11.2%", "26.17%", "8.7%", "$184.32"]:
    has(w, t)
# live widget blocks
for blk in ["embed-widget-ticker-tape.js", "embed-widget-single-quote.js", "embed-widget-timeline.js",
            "embed-widget-stock-heatmap.js", "embed-widget-mini-symbol-overview.js", "embed-widget-events.js"]:
    has(w, blk)
for sym in ["FOREXCOM:SPXUSD", "FOREXCOM:NSXUSD", "FOREXCOM:DJI", "TVC:USOIL", "TVC:US10Y"]:
    has(w, sym)
ck(S[w].count("embed-widget-single-quote.js") == 3, "WS: three single-quote widgets")
# rejected figures must stay inside their rejection windows
window(w, "7,673.04", ["rejected", "impossible"])
window(w, "6,279", ["rejected", "2025 levels"])
window(w, "$3.97 trillion", ["rejected", "2025 levels"])
window(w, "232,000", ["rejected", "2022"])
window(w, "$5.90", ["not published", "withheld", "still not published"])
window(w, "Energy down 1.82%", ["withheld", "not published"])
window(w, "$215 from $205", ["not published", "disagree"])
# Jackson Hole guard — INVERTED: must be published, with the correction stated
has(w, "Jackson Hole")
has(w, "That reasoning was wrong.")
has(w, "August 27&ndash;29")
# no invented Kansas City Fed / GDP number
has(w, "no figure from either was corroborated this run")

# ---------- CYBER ----------
c = "cyber-briefing.html"
for t in ["CVE-2026-21962", "CVE-2026-8452", "CVE-2026-19490", "CVE-2026-64633", "CVE-2026-65641",
          "8.8", "9.3 (CVSS v4.0)", "10.0", "Aug 29", "August 29", "x.php", "z.php",
          "BOD 26-04", "Cursor", "nine countries", "17 environments", 'id="kev4"',
          "Boston Scientific", "TeamPCP", "Louis Michael Gaebler", "Ruben Ian Thomson"]:
    has(c, t)
ck(S[c].count("August 29") + S[c].count("Aug 29") >= 4,
   "cyber: Aug 29 deadline must appear in top story, patch priority, vuln table and KEV board")
window(c, "Server Killers", ["not published", "no group has claimed"])
window(c, "CVE-2026-19490", ["no evidence", "not in the KEV", "Rapid7"])
# CVE identifier whitelist
allowed = {"CVE-2026-21962","CVE-2026-64633","CVE-2026-65641","CVE-2026-8452","CVE-2026-19490",
           "CVE-2026-12569","CVE-2026-69836","CVE-2026-68820","CVE-2026-62815","CVE-2026-62893",
           "CVE-2026-60004","CVE-2026-18963","CVE-2026-19913","CVE-2026-19912","CVE-2026-73570",
           "CVE-2026-72529","CVE-2026-72530","CVE-2026-33824","CVE-2026-55040","CVE-2026-59310",
           "CVE-2026-65400","CVE-2026-20349","CVE-2026-72898","CVE-2026-8037","CVE-2015-3246",
           "CVE-2015-5287","CVE-2019-1068","CVE-2021-23758","CVE-2022-0995","CVE-2026-20253"}
found = set(re.findall(r"CVE-\d{4}-\d{4,6}", S[c]))
ck(found <= allowed, "cyber: unrecognised CVE id(s): %s" % (found - allowed))
ck(len(found) >= 20, "cyber: CVE liveness — only %d ids found" % len(found))

# ---------- MMA ----------
m = "mma-briefing.html"
rows = re.findall(r"<tr><td>([^<]*)</td><td><b>([^<]*)</b></td>", S[m])
ck(len(rows) >= 11, "mma: champions board liveness — %d rows parsed" % len(rows))
champs = {d: ch for d, ch in rows}
ck(champs.get("Light Heavyweight") == "Carlos Ulberg", "mma: LHW must be Carlos Ulberg")
ck(champs.get("Middleweight") == "Sean Strickland", "mma: MW must be Sean Strickland")
ck(champs.get("Lightweight") == "Justin Gaethje", "mma: LW must be Justin Gaethje")
ck(champs.get("Featherweight") == "Alexander Volkanovski", "mma: FW must be Volkanovski, never vacant")
ck(champs.get("Heavyweight") == "Tom Aspinall", "mma: HW must be Tom Aspinall")
ck(champs.get("Welterweight") == "Islam Makhachev", "mma: WW must be Islam Makhachev")
for bad in ["Alex Pereira", "Khamzat Chimaev", "Ilia Topuria", "vacant", "Vacant"]:
    ck(not any(bad in ch for ch in champs.values()), "mma: regression in a champion cell: %s" % bad)
absent(m, "Shamil Yakhyaev")
absent(m, "Cody Salkilld")
absent(m, "Abdul-Rakhman")
for t in ["Umar Nurmagomedov", "Song Yadong", "−500", "+385", "+380", "−470", "Qileng Aori",
          "Kai Asakura", "Su Mudaerji", "Yan Xiaonan", "Denise Gomes", "Gregory Rodrigues",
          "Anthony Hernandez", "Curtis Blaydes", "Quillan" if "Quillan" in S[m] else "Champions Board"]:
    has(m, t)
window(m, "Alex Pereira", ["rejected", "Interim", "vacated"])
window(m, "Ilia Topuria", ["rejected", "TKO4", "stopped"])
has(m, "ufccdn")

# ---------- index ----------
i = "index.html"
for t in ["147.67", "0.28%", "8.8", "Nurmagomedov", "Read the briefing"]:
    has(i, t)
ck("217.20" not in S[i], "index: stale 11:35 market figure still on the front page")

print("checks: %d, failures: %d" % (checks, len(fails)))
for f in fails:
    print("  FAIL:", f)
sys.exit(1 if fails else 0)
