# -*- coding: utf-8 -*-
import io, os
D = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(D, "val.py")
s = io.open(p, encoding="utf-8").read()
n = 0
def rep(old, new):
    global s, n
    assert old in s, "MISSING: " + old[:80]
    s = s.replace(old, new, 1); n += 1

# WS literals
rep('''"wallstreet-briefing.html":["1:25&ndash;1:50 PM ET",''',
    '''"wallstreet-briefing.html":["2:25&ndash;2:40 PM ET","500 points","53,000","Dow Jones","Strait of Hormuz",
   "Oman","8:30 AM ET","2:00 PM ET","2:30 PM ET","January 2025","3.20%","bifurcated","56,000","Thursday 10 September",''')

# cyber literals: add September Patch Tuesday set, drop the retired 1:00 PM ET string
rep('''"421","398","751","BOD 26-04","1:00 PM ET","9.2"]''',
    '''"421","398","751","BOD 26-04","9.2",
   "973","113","CVE-2026-85880","CVE-2026-81963","KB5122871","KB5122876","Windows Update Stack",
   "Advanced Local Procedure Call","CVE-2026-6471","PostGREShell","AssetMark","570,000","7,551","24.9%",
   "723","943","8 September"]''')

# mma literals
rep('''"12 December","Adam Darby","Cage Warriors"]''',
    '''"12 December","Adam Darby","Cage Warriors",
   "welterweight","39-year-old","December 2023","5-1 across six appearances","Yair Rodriguez",
   "&minus;450","+350","&minus;425","+355","17-3","12-2","Delphine Benouaich","Matthieu Duclos",
   "Modestas Bukauskas","Kurtis Campbell","Magomed Ankalaev","Paulo Costa","Bogdan Guskov",
   "early next year","ACL","Punahele Soriano","Trevor Peek"]''')

# index literals
rep('''"index.html":["The Cyber Wire","The Closing Bell","The Octagon","122,000","Novartis","Michael Page","Shevchenko","Archive"],''',
    '''"index.html":["The Cyber Wire","The Closing Bell","The Octagon","122,000","Novartis","Michael Page","Archive","973","500 points"],''')

# new stale bans for this edition
rep('''STALE=["Labor Day long weekend opened","Dow futures","pre-open","market holiday today","after today&#39;s close",
       "10:35 AM ET","Intel leads the tape","NASDAQ:INTC","+5.2%"]''',
    '''STALE=["Labor Day long weekend opened","Dow futures","pre-open","market holiday today","after today&#39;s close",
       "10:35 AM ET","Intel leads the tape","NASDAQ:INTC","+5.2%","1:25&ndash;1:50 PM ET",
       "UFC middleweight <b>Michael","release is reportedly looming","no September CVE count",
       "No September CVE count","had not shipped at publication"]''')

# extra guards for this edition
rep('''print("checks:", n, "failures:", len(fails))''',
    '''# --- edition-specific guards ----------------------------------------------
ck("973 vulnerabilities" in cy or "973 CVEs" in cy, "cyber: September total stated")
ck("9 CVEs, 9 Critical" not in cy or "refused" in cy, "cyber: template count refused not asserted")
ck(cy.count("Top Story")>=1, "cyber: top story heading")
ck("middleweight" not in mm.split("Michael &ldquo;Venom&rdquo; Page")[1][:400], "mma: Page not called a middleweight")
ck("Alex Pereira" in mm and "<td>Alex Pereira</td>" not in mm, "mma: Pereira named only as a refusal")
ck("refused" in mm.lower(), "mma: refusal stated in print")
ck("Whatfinger" in ws or "500 points" in ws, "ws: 500-point read attributed")
ck("53,000" in ws and "Dow Jones" in ws, "ws: payrolls consensus attributed")

print("checks:", n, "failures:", len(fails))''')

io.open(p, "w", encoding="utf-8").write(s)
print("val patch:", n)
