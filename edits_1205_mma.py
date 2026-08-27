import io
P = "/sessions/beautiful-zealous-mendel/mnt/outputs/mma-briefing.html"
s = io.open(P, encoding="utf-8").read()
n = 0
def rep(old, new):
    global s, n
    c = s.count(old)
    assert c == 1, "count=%d for: %s" % (c, old[:110])
    s = s.replace(old, new); n += 1

# 1 — Shanghai card: fuller main card + a third odds read
rep('<div class="card"><span class="tag acc">Fight week</span><span class="tag">Carried</span>\n<div class="mono" style="color:var(--acc2);font-size:12px;letter-spacing:.08em;margin-bottom:6px">SAT AUG 29 · SHANGHAI ORIENTAL SPORTS CENTER</div>\n<h3>UFC Fight Night: Nurmagomedov vs. Song</h3>\n<p>Bantamweight main event with title-eliminator stakes; Paramount+ exclusive in the US. Co-main: <b>Yan Xiaonan vs. Denise Gomes</b> at women\'s strawweight. Prelims 3 a.m. ET, main card 6 a.m. ET.<br><b>Odds:</b> Nurmagomedov −500 / Song +380 consensus (roughly 80% / 20% implied); DraftKings opened the fight at −470 / +360.</p></div>',
    '<div class="card" style="grid-column:1/-1"><span class="tag new">Updated · 12:05</span><span class="tag acc">Fight week</span>\n<div class="mono" style="color:var(--acc2);font-size:12px;letter-spacing:.08em;margin-bottom:6px">SAT AUG 29 · SHANGHAI ORIENTAL SPORTS CENTER</div>\n<h3>UFC Fight Night: Nurmagomedov vs. Song</h3>\n<p>Bantamweight main event with title-eliminator stakes — a top-ten matchup with a title shot reported to be on the line for the winner. Paramount+ exclusive in the US; prelims <b>3 a.m. ET</b>, main card <b>6 a.m. ET</b>.<br><br><b>The rest of the main card, as listed this run:</b> co-main <b>Yan Xiaonan vs. Denise Gomes</b> at women\'s strawweight, described as carrying significant title implications in that division; <b>Qileng Aori vs. Kai Asakura</b>; and <b>Alex Perez vs. Su Mudaerji</b>, a rematch — their first meeting in <b>May</b> ended prematurely after a low blow.<br><br><b>Odds:</b> Nurmagomedov <b>−500</b> / Song <b>+380</b> consensus (roughly 80% / 20% implied); <b>MMAOddsBreaker\'s opening line was −500 / +385</b>; DraftKings opened the fight at <b>−470 / +360</b>. <span style="color:var(--mut)">All three reads are printed and none averaged; the favourite\'s price is stable across them, and the spread sits on the underdog side.</span></p></div>')

# 2 — Champions Board: log the stale-list trap resurfacing
rep('<h2 class="sec">Champions Board</h2>',
    '<h2 class="sec">Champions Board</h2>\n<div class="note" style="margin:0 0 10px"><b>Trap logged at 12:05, and the board did not move.</b> A fresh query against ESPN\'s "Current and all-time UFC champions" page returned a summary listing <b>Alex Pereira at light heavyweight, Khamzat Chimaev at middleweight and Ilia Topuria at lightweight</b>. Those three lines are the exact regression this briefing has published wrongly before: Pereira vacated at 205 and lost the interim-heavyweight bid to Ciryl Gane, Sean Strickland took the middleweight belt by split decision at UFC 328 on May 9, and Justin Gaethje stopped Topuria in the fourth round at Freedom 250 on June 14. <b>The stale summary was rejected and the verified board below is unchanged</b> — a champions list that predates the most recent title fight is wrong no matter how authoritative the domain.</div>')

io.open(P, "w", encoding="utf-8").write(s)
print("mma edits applied:", n)
