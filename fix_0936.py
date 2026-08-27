import io,sys
def ed(path,pairs):
    s=io.open(path,encoding='utf-8').read()
    for i,(a,b) in enumerate(pairs):
        n=s.count(a)
        if n!=1: print("FAIL %s #%d count=%d :: %s"%(path,i,n,a[:80])); sys.exit(1)
        s=s.replace(a,b)
    io.open(path,'w',encoding='utf-8').write(s); print("OK",path,len(pairs))

ed('wallstreet-briefing.html',[
# (1) "each well above" was false for Okta, which had no pre-open number at all
('The latest quotes seen this run have <b>Okta up more than 20%</b>, <b>Salesforce up 14.78%</b> and <b>CrowdStrike up 14.34%</b> — each well above its pre-open read — while <b>Nvidia is up 5.87%</b>,',
 'The latest quotes seen this run have <b>Okta up more than 20%</b>, <b>Salesforce up 14.78%</b> and <b>CrowdStrike up 14.34%</b> — Salesforce and CrowdStrike both well above their pre-open reads, and Okta a name this page could put no number on an hour ago — while <b>Nvidia is up 5.87%</b>,'),
# (2) mover-card tags: reflect what actually changed this run
('<div class="card"><span class="tag new">Updated</span><span class="tag acc">Semis</span>\n<h3>Nvidia (NVDA) — up 5.87%',
 '<div class="card"><span class="tag new">Updated · 9:35</span><span class="tag acc">Semis</span>\n<h3>Nvidia (NVDA) — up 5.87%'),
('<div class="card"><span class="tag new">New</span><span class="tag acc">Semis</span>\n<h3>The semiconductor complex follows Nvidia up</h3>',
 '<div class="card"><span class="tag">Carried</span><span class="tag acc">Semis</span>\n<h3>The semiconductor complex follows Nvidia up</h3>'),
('<div class="card"><span class="tag">Carried</span><span class="tag acc">Software</span>\n<h3>Salesforce (CRM) — up 14.78%',
 '<div class="card"><span class="tag new">Updated · 9:35</span><span class="tag acc">Software</span>\n<h3>Salesforce (CRM) — up 14.78%'),
('<div class="card"><span class="tag">Carried</span><span class="tag acc">Cybersecurity</span>\n<h3>CrowdStrike (CRWD) — up 14.34%',
 '<div class="card"><span class="tag new">Updated · 9:35</span><span class="tag acc">Cybersecurity</span>\n<h3>CrowdStrike (CRWD) — up 14.34%'),
# (3) record the consensus-revenue discrepancy rather than silently keeping one figure
('ahead of a <b>$11.32 billion</b> consensus.',
 'ahead of a <b>$11.32 billion</b> consensus. <span style="color:var(--mut)">(A second summary this run puts the consensus at <b>$11.33 billion</b>; the difference does not change the direction of the beat, and both figures are recorded rather than one being picked.)</span>'),
])
