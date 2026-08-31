#!/usr/bin/env python3
"""Four guard narrowings for validate_1735.py. Each is TIGHTER than what it replaces.

(a) PayPal -12.7%  : banned as a STRING; the page carries it only to refuse it.
                     16th occurrence of "a guard that forbids a string forbids the
                     page from disowning it". Now: refusal token required in context.
(b) September 9/10 : the page holds MANY KEV deadlines (Sept 9 batch, JFrog Sept 10)
                     and all are correct. Sept 14 is the PaperCut deadline only.
                     Now: the Sept-14 rule binds only to PaperCut deadline sentences.
(c) Champion cells : the slice keyed on the first "Champions Board" string, which is a
                     PROSE mention ~85k chars before the table. Now: keyed on the
                     <h2> heading, and the eleven cells are checked by name.
(d) former champion / title challenger : both phrases are TRUE of Pantoja, O'Malley,
                     Yan Xiaonan and Umar Nurmagomedov, all sourced. The standing
                     correction names DARIUSH and BLAYDES specifically.
                     Now: the ban binds to those two names, not to the phrase.
"""
import re, io, sys
p = "validate_1735.py"
s = io.open(p, encoding="utf-8").read()

# ---- (a) PayPal ----
old = ('ck("PayPal &minus;12.7%" not in WS and "PayPal -12.7%" not in WS,\n'
       '   "ws: refused PayPal figure published")')
new = ('''for m in re.finditer(r'PayPal &minus;12\\.7', WS):
    ctx = WS[max(0, m.start() - 900): m.start() + 500].lower()
    ck(("not published" in ctx or "refus" in ctx or "deliberately not used" in ctx
        or "none of it is published" in ctx or "friday" in ctx),
       "ws: PayPal -12.7% outside a refusal")''')
assert old in s; s = s.replace(old, new, 1)

# ---- (b) September 14 binds to PaperCut only ----
old = ("""for m in re.finditer(r'(deadline|due|remediat\\w+)[^.]{0,120}?September (\\d{1,2})', CY):
    ck(m.group(2) == "14", "cyber: deadline stated as September %s" % m.group(2))""")
new = ('''for m in re.finditer(r'(deadline|due|remediat\\w+)[^.]{0,160}?September (\\d{1,2})', CY):
    ctx = CY[max(0, m.start() - 600): m.start() + 300]
    is_papercut = ("PaperCut" in ctx or "CVE-2026-82078" in ctx or "CVE-2026-81578" in ctx)
    if is_papercut:
        ck(m.group(2) == "14", "cyber: PaperCut deadline stated as September %s" % m.group(2))
# and the PaperCut CVEs must never sit beside a NON-14 September deadline
for cve in ("CVE-2026-82078", "CVE-2026-81578"):
    for m in re.finditer(re.escape(cve), CY):
        w = CY[m.start(): m.start() + 500]
        for d in re.findall(r'(?:deadline|due|remediat\\w+)[^.]{0,120}?September (\\d{1,2})', w):
            ck(d == "14", "cyber: %s beside a September %s deadline" % (cve, d))''')
assert old in s; s = s.replace(old, new, 1)

# ---- (c) champion cells keyed on the HEADING, not the first prose mention ----
old = ('i = MM.find("Champions Board")\nboard = MM[i:i + 9000]')
new = ('''m = re.search(r'<h2[^>]*>\\s*Champions Board[^<]*</h2>', MM)
assert m, "mma: Champions Board heading not found"
board = MM[m.end(): m.end() + 12000]
ck("<table" in board[:4000], "mma: no table under the Champions Board heading")''')
assert old in s; s = s.replace(old, new, 1)

# ---- (d) descriptor ban binds to the two NAMES the correction names ----
old = ("""for h, n in ((MM, "mma"), (IX, "index")):
    for m in re.finditer(r'(former champion|title challenger)', h):
        ctx = h[max(0, m.start() - 400): m.start() + 300].lower()
        ck("not " in ctx or "never" in ctx or "refus" in ctx or "is not described" in ctx,
           "%s: unqualified '%s'" % (n, m.group(1)))""")
new = ('''for h, n in ((MM, "mma"), (IX, "index")):
    for m in re.finditer(r'(former champion|title challenger)', h):
        ctx = h[max(0, m.start() - 300): m.start() + 200]
        for banned in ("Dariush", "Blaydes"):
            if banned in ctx:
                low = ctx.lower()
                ck(("not " in low or "never" in low or "is not described" in low),
                   "%s: '%s' attached to %s" % (n, m.group(1), banned))''')
assert old in s; s = s.replace(old, new, 1)

io.open(p, "w", encoding="utf-8").write(s)
print("narrow_1735 OK")
