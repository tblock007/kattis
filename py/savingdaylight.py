from sys import stdin

for line in stdin.readlines():
    m, d, y, a, b = line.split()
    ah, am = [int(w) for w in a.split(':')]
    bh, bm = [int(w) for w in b.split(':')]
    dh = bh - ah
    dm = bm - am
    if (dm < 0):
        dh -= 1
        dm += 60
    print('{0} {1} {2} {3} hours {4} minutes'.format(m, d, y, dh, dm))