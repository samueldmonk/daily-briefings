import re,sys
R='/tmp/db_1792616601/'
def load(f): return open(R+f,encoding='utf-8').read()
def save(f,s): open(R+f,'w',encoding='utf-8').write(s)
def rep(s,a,b,f):
    if a not in s: sys.exit('MISSING in %s: %s'%(f,a[:80]))
    return s.replace(a,b)
NEW='<span class="tag new">New</span>'
INV_T='https://www.investing.com/news/earnings/tesla-stock-up-after-hours-on-results-beat-improved-automotive-gross-margin-4963976'
INV_L='https://www.investing.com/news/earnings/lam-research-tops-firstquarter-targets-and-issues-upbeat-guidance-stock-falls-4963987'
# ---- WS
f='wallstreet-briefing.html'; s=load(f)
s=s.replace(NEW,'')
s=rep(s,'Official close (investingLive, 4:16 PM ET): Nasdaq +1.05%, S&amp;P 500 +0.60%, Dow +0.69% — SpaceX relights the AI trade; Meta and Tesla beat after the bell','Official close (investingLive, 4:16 PM ET): Nasdaq +1.05%, S&amp;P 500 +0.60%, Dow +0.69% — SpaceX relights the AI trade; after the bell (as of ~4:45 PM ET) Meta and Tesla rise, Lam Research slips',f)
s=rep(s,'<p><b>Tesla after the bell.</b>','<p>'+NEW+'<b>Tesla after the bell.</b>',f)
s=rep(s,'No settled after-hours Tesla move was verified at publication.','Shares rose more than 1% after hours as automotive gross margin excluding regulatory credits improved to 18.1% from 15.4% a year earlier and 16.3% in Q2 (<a href="'+INV_T+'">Investing.com</a>, updated 4:45 PM ET).</p><p>'+NEW+'<b>Lam Research after the bell.</b> Shares slipped 6% after hours despite fiscal Q1 non-GAAP EPS of $2.20 on $8.22 billion revenue, ahead of the $2.18 and $8.13 billion estimates; Investing.com pointed to a wide Q2 guidance range ($8.2–$9.0 billion revenue, $2.18–$2.48 EPS) after a nearly 80% run in the stock (<a href="'+INV_L+'">Investing.com</a>).',f)
s=rep(s,'<p><b>Tesla (TSLA):</b>','<p>'+NEW+'<b>Tesla (TSLA):</b>',f)
s=rep(s,'No after-hours price move verified at publication.</p>','Shares were up more than 1% after hours (<a href="'+INV_T+'">Investing.com</a>, updated 4:45 PM ET).</p><p>'+NEW+'<b>Lam Research (LRCX):</b> down 6% after hours despite a beat — non-GAAP EPS $2.20 vs $2.18 and revenue $8.22 billion vs $8.13 billion; non-GAAP gross margin 52.4%, operating margin 40.2% (<a href="'+INV_L+'">Investing.com</a>, 4:22 PM ET).</p>',f)
s=rep(s,'and Tesla beat on adjusted EPS of $0.48.</span>','Tesla rose more than 1% after beating on adjusted EPS of $0.48, and Lam Research fell 6% despite a beat.</span>',f)
s=rep(s,'<li>Also reporting: IBM, Lam Research, Texas Instruments','<li>Also reporting: IBM, Texas Instruments',f)
s=rep(s,'<footer><b>Sources (read this edition)</b><ol>','<footer><b>Sources (read this edition)</b><ol><li><a href="'+INV_T+'">Investing.com — Tesla stock up as automotive gross margin improves (Oct. 21, updated 4:45 PM)</a></li><li><a href="'+INV_L+'">Investing.com — Lam Research tops first-quarter targets, stock falls (Oct. 21, 4:22 PM)</a></li>',f)
s=s.replace('4:35 PM ET','5:05 PM ET'); save(f,s)
# ---- CYBER
f='cyber-briefing.html'; s=load(f)
s=s.replace(NEW,'')
HR='https://hackread.com/inc-the-gentlemen-ransomware-affiliates-ai-messages/'
card='<div class="card">'+NEW+'<span class="tag crit">Ransomware</span><h3>Exposed INC / The Gentlemen affiliate servers show AI-assisted intrusions</h3><p>SOCRadar found seven exposed servers tied to INC and The Gentlemen affiliates holding 8,257 AI messages across 133 OpenCode sessions, stolen credentials and 46 INC encryptor builds prepared for six victims; operator records name 62 organizations (36 in the U.S.) and claim exploitation of cPanel CVE-2026-41940, SimpleHelp CVE-2024-57727 and FortiClient EMS CVE-2026-35616 — figures from the attackers’ own records, not independently verified. Session logs show humans approving each AI step (<a href="'+HR+'">Hackread</a>).</p></div>'
s=rep(s,'<h2 class="sec">Breaches &amp; Incidents</h2><div class="cards">','<h2 class="sec">Breaches &amp; Incidents</h2><div class="cards">'+card,f)
s=rep(s,'<footer><b>Sources (read this edition)</b><ol>','<footer><b>Sources (read this edition)</b><ol><li><a href="'+HR+'">Hackread — INC and The Gentlemen affiliates expose 8,257 AI messages (Oct. 21)</a></li>',f)
s=s.replace('4:35 PM ET','5:05 PM ET'); save(f,s)
# ---- MMA
f='mma-briefing.html'; s=load(f)
s=s.replace(NEW,'')
Y='https://sports.yahoo.com/mma/article/ufc-333-alexander-volkanovski-vs-movsar-evloev-full-fight-card-odds-start-time-everything-for-saturdays-early-event-202451448.html'
s=rep(s,'Kalshi 50% / 50% (<a href="https://www.covers.com/ufc/333-odds-saturday-oct-24-2026">Covers</a>).</p>','Kalshi 50% / 50% (<a href="https://www.covers.com/ufc/333-odds-saturday-oct-24-2026">Covers</a>).<br>'+NEW+'<b>Odds:</b> Volkanovski −110 / Evloev −110; Yan −175 / Dvalishvili +145. Main card 2 p.m. ET, prelims 12 p.m., early prelims 10 a.m. on Paramount+ (<a href="'+Y+'">Uncrowned via Yahoo Sports</a>, Oct. 19).</p>',f)
s=rep(s,'<footer><b>Sources (read this edition)</b><ol>','<footer><b>Sources (read this edition)</b><ol><li><a href="'+Y+'">Uncrowned / Yahoo Sports — UFC 333 full fight card, odds, start time (Oct. 19)</a></li>',f)
s=s.replace('4:35 PM ET','5:05 PM ET'); save(f,s)
print('ok')
