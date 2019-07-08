import sys

for line in sys.stdin.readlines():
    # for each case, simply simulate the process
    m, p, l, e, r, s, n = [int(w) for w in line.split()]
    for _ in range(n):
        m, p, l = (p // s), (l // r), (m * e)
    print(m)
