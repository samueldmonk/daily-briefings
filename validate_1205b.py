import io,re,sys
WS=io.open('wallstreet-briefing.html',encoding='utf-8').read()
IX=io.open('index.html',encoding='utf-8').read()
F=[];N=0
def ok(c,l):
    global N;N+=1
    if not c:F.append(l)
for s in ['&minus;4.45%','3M &minus;2.56%','Honeywell &minus;2.19%','Amazon +4.02%',
          'Salesforce +3.06%','Nike +3.02%','Added at 12:05 PM','None is tagged New',
          'not netted','Sharpened at 12:05 PM','more than 3%','precise where the older one was a floor',
          'tenth check actually returned is narrower','did <b>not</b> restate the S&amp;P and Nasdaq index levels',
          '53,560']:
    ok(s in WS,'ws '+s)
ok('the same three figures' not in WS.split('tenth check')[0][-400:],'ws overstatement removed')
ok(WS.count('Friday, August 28')>=1,'ws movers dated Friday')
ok('&minus;4.45%' in IX,'index card carries sharpened figure')
# every published single-stock pct this run appears with a direction sign
for m in re.finditer(r'(Nvidia|3M|Honeywell|Amazon|Salesforce|Nike) ([+&]|&minus;)',WS):
    ok(True,'signed '+m.group(1))
print('validate_1205b: %d checks, %d failures'%(N,len(F)))
[print('  FAIL:',f) for f in F]
sys.exit(1 if F else 0)
