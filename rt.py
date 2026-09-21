import io,re,sys,html
B="/sessions/youthful-bold-tesla/mnt/outputs/"
f=sys.argv[1]
s=io.open(B+f,encoding="utf-8").read()
s=re.sub(r'<style>.*?</style>','',s,flags=re.S)
s=re.sub(r'<script.*?</script>','',s,flags=re.S)
s=re.sub(r'<h2 class="sec">','\n\n## ',s)
s=re.sub(r'<li>','\n - ',s)
s=re.sub(r'<tr>','\n | ',s)
s=re.sub(r'</td><td[^>]*>',' | ',s)
s=re.sub(r'<h3[^>]*>','\n### ',s)
s=re.sub(r'<p[^>]*>','\n',s)
s=re.sub(r'<div class="card"[^>]*>','\n--- ',s)
s=re.sub(r'<[^>]+>',' ',s)
s=html.unescape(s)
s=re.sub(r'[ \t]+',' ',s)
s=re.sub(r'\n{3,}','\n\n',s)
print(s.strip())
