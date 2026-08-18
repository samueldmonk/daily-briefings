import io, sys

ENT = {'&mdash;':'—','&ndash;':'-','&minus;':'-','&rsquo;':"'",'&lsquo;':"'",
       '&ldquo;':'"','&rdquo;':'"','&amp;':'&','&nbsp;':' ','&apos;':"'",'&quot;':'"',
       '&le;':'≤','&ge;':'≥'}
CHR = {'–':'-','−':'-','’':"'",'‘':"'",'“':'"','”':'"',' ':' '}

def canon_map(s):
    out = []; idx = []; i = 0; n = len(s)
    while i < n:
        hit = None
        if s[i] == '&':
            for k, v in ENT.items():
                if s.startswith(k, i):
                    hit = (len(k), v); break
        if hit:
            out.append(hit[1]); idx.append(i); i += hit[0]
        else:
            c = s[i]
            out.append(CHR.get(c, c)); idx.append(i); i += 1
    idx.append(n)
    return ''.join(out), idx

def canon(s):
    return canon_map(s)[0]

def load(f):
    return io.open(f, encoding='utf-8').read()

def save(f, t):
    io.open(f, 'w', encoding='utf-8').write(t)

def rep(t, old, new, f, label, n=1):
    """Replace `old` in `t` matching on an entity-normalised view, preserving the
    original bytes outside the match. Fails loudly on a count mismatch."""
    ct, idx = canon_map(t)
    co = canon(old)
    c = ct.count(co)
    if c != n:
        print('FAIL [%s/%s] expected %d, found %d' % (f, label, n, c))
        print('   canon-needle head: %r' % co[:110])
        sys.exit(1)
    outp = []
    pos = 0
    for _ in range(n):
        k = ct.index(co, pos)
        outp.append(t[idx[pos] if pos else 0:idx[k]] if pos else t[:idx[k]])
        outp.append(new)
        pos = k + len(co)
    outp.append(t[idx[pos]:])
    print('  ok  %-38s %s' % (label, f))
    return ''.join(outp)

def slice_between(t, a, b):
    """Return the original-text slice from the start of canon marker `a` to the
    start of canon marker `b`."""
    ct, idx = canon_map(t)
    ca, cb = canon(a), canon(b)
    i = ct.index(ca); j = ct.index(cb, i)
    return t[idx[i]:idx[j]]
