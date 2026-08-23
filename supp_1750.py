import re,io,datetime
O="/sessions/awesome-youthful-ramanujan/mnt/outputs/"
S={p:io.open(O+p,encoding='utf-8').read() for p in
   ["index.html","cyber-briefing.html","wallstreet-briefing.html","mma-briefing.html"]}
f=[];n=0
def ck(c,m):
    global n
    n+=1
    if not c: f.append(m)

c=S["cyber-briefing.html"]; m=S["mma-briefing.html"]; w=S["wallstreet-briefing.html"]; i=S["index.html"]

# --- new cyber material
ck(c.count("CVE-2026-19490")==2,"citrix cve count %d"%c.count("CVE-2026-19490"))
ck("14.1-73.32" in c and "13.1-63.21" in c,"citrix fixed builds")
ck(c.count("14,530")==2,"dahua count")
ck("CVE-2021-33044" in c and "CVE-2021-33045" in c,"dahua cves")
ck("9.8" in c and "CVE-2026-72529" in c,"patch priority cve")
# patch priority & KEV agree
ck(c.count("Added Aug 20, due <strong>Aug 23</strong>")==1,"kev truecon row")
ck("action due date of <strong>August 23</strong>" in c,"patch priority date")
# KEV countdown integrity
rows=re.findall(r'due <strong>([A-Za-z]+ \d+)</strong>\. <span class="kev-(crit|soon|ok)">([^<]+)</span>',c)
ck(len(rows)==12,"kev rows %d"%len(rows))
today=datetime.date(2026,8,23)
past=due=ahead=0
for d,cls,lab in rows:
    dt=datetime.datetime.strptime(d+" 2026","%b %d %Y").date() if len(d.split()[0])==3 else datetime.datetime.strptime(d+" 2026","%B %d %Y").date()
    delta=(dt-today).days
    if delta<0:
        past+=1; ck(cls=="crit" and "PAST DUE" in lab and lab.startswith(str(-delta)),"kev %s label %s"%(d,lab))
    elif delta==0:
        due+=1; ck(cls=="crit" and "DUE TODAY" in lab,"kev %s today"%d)
    else:
        ahead+=1
        ck((cls=="soon" and delta<=2) or (cls=="ok" and delta>2),"kev %s class %s d=%d"%(d,cls,delta))
        ck(lab.startswith(str(delta)),"kev %s days %s vs %d"%(d,lab,delta))
ck((past,due,ahead)==(7,1,4),"kev split %s"%str((past,due,ahead)))
ck("7 are past due, 1 comes due today and 4 remain ahead" in c,"kev prose split")

# --- MMA
ck("Noche UFC 4: Jean Silva vs Jose Delgado" in m,"noche headline")
ck("Yair Rodriguez vs Jean Silva" not in m,"stale noche headline present")
ck("&minus;425" in m and "+355" in m,"noche odds")
ck("Madison Square Garden" in m and "November 14" in m,"ufc334")
ck("T-Mobile Arena" in m and "December 12" in m,"ufc335")
ck("Polymarket UFC 334" in m,"polymarket")
ck(all(x in m for x in ["Max Holloway","Paddy Pimblett","Gable Steveson"]),"nsac names")
ck("Graham Boyland" in m,"boyland")
# champions board
champs={"Tom Aspinall":"Heavyweight","Carlos Ulberg":"Light Heavyweight","Sean Strickland":"Middleweight",
 "Islam Makhachev":"Welterweight","Justin Gaethje":"Lightweight","Alexander Volkanovski":"Featherweight",
 "Petr Yan":"Bantamweight","Joshua Van":"Flyweight","Valentina Shevchenko":"Women","Kayla Harrison":"Women",
 "Mackenzie Dern":"Women"}
for name in champs: ck(name in m,"champ missing %s"%name)
for bad in ["Cody Salkilld","Shamil Yakhyaev","Abdul-Rakhman","MacKenzie","Joshua Vance","Pereira (205)","pay-per-view","Jahmall Emmers def"]:
    for p,s in S.items(): ck(bad not in s,"trap %s in %s"%(bad,p))
ck(m.count("<td>Middleweight</td><td>Sean Strickland</td>")==1,"MW row")
ck(m.count("<td>Lightweight</td><td>Justin Gaethje</td>")==1,"LW row")
ck(m.count("<td>Flyweight</td><td>Joshua Van</td>")==1,"FLW row")
ck(m.count("<td>Bantamweight</td><td>Petr Yan</td>")==1,"BW row")
ck("vacant" not in m.lower().replace("the vacant belt",""),"vacant word")
ck(len(re.findall(r'<tr><td class="win">',m))==13,"results rows")

# --- markets (weekend framing)
ck("closed for the weekend" in w,"weekend framing")
ck("After-Hours" not in w or "No After-Hours Movers section appears this edition" in w,"after hours")
sc=re.search(r'<tbody>(.*?)</tbody>',w,re.S).group(1)
for lvl,chg,pct in re.findall(r'<td>([\d,\.]+)</td><td class="up">\+([\d\.]+)</td><td class="up">\+([\d\.]+)%</td>',sc):
    L=float(lvl.replace(",","")); C=float(chg); P=float(pct)
    ck(abs((C/(L-C)*100)-P)<0.02,"scorecard math %s"%lvl)
ck("&minus;1.43%" in w and "&minus;2.05%" in w,"weekly pct")
ck("10 a.m." in w,"warsh time")
ck("NASDAQ:MRNA" in w,"chart of day")
for sym in ["FOREXCOM:SPXUSD","FOREXCOM:NSXUSD","FOREXCOM:DJI","TVC:USOIL","TVC:US10Y"]:
    ck(sym in w,"ticker %s"%sym)

# --- index cards echo the leads
ck("CVE-2026-19490" in i and "14,500 Dahua" in i,"index cyber card")
ck("Jose Delgado" in i and "UFC 334" in i,"index mma card")
ck("closed for the weekend" in i,"index markets card")

print("SUPPLEMENTAL CHECKS: %d  FAILURES: %d"%(n,len(f)))
for x in f: print("  -",x)
