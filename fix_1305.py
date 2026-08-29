import io
OLD = (u're-verified a twelfth time this run, the second consecutive check to return all three levels and all three '
 u'percentage moves together, by a search that returned all three index levels and all three percentage moves together, '
 u'so the S&amp;P and Nasdaq levels the previous edition had to flag as carried are carried no longer')
NEW = (u're-verified a twelfth time this run by a search that again returned all three index levels and all three '
 u'percentage moves together &mdash; the second consecutive check of that breadth, which is why the S&amp;P and Nasdaq '
 u'levels the 12:05 edition had to flag as carried stay retired rather than reverting to carried')
for p in ('wallstreet-briefing.html','index.html'):
    s = io.open(p, encoding='utf-8').read()
    assert s.count(OLD) == 1, (p, s.count(OLD))
    io.open(p,'w',encoding='utf-8').write(s.replace(OLD, NEW))
print("FIX OK")
